# letterFrom — Local RAG for a Newsletter Archive

A local retrieval-augmented search over a personal newsletter archive. Hybrid (vector + keyword) search across two document types — **posts** (newsletter issues) and **pages** (standalone linked articles) — with two query modes: fast single-shot retrieval, and cached map-reduce over the whole corpus or any date/number range.

## Contents

1. [Architecture](#1-architecture)
2. [Repository layout](#2-repository-layout)
3. [Setup](#3-setup)
4. [Building the index](#4-building-the-index)
5. [Querying: single-shot](#5-querying-single-shot)
6. [Querying: map-reduce](#6-querying-map-reduce)
7. [CLI reference](#7-cli-reference)
8. [Caching model](#8-caching-model)
9. [Data schema](#9-data-schema)
10. [Design notes & gotchas](#10-design-notes--gotchas)
11. [Troubleshooting](#11-troubleshooting)
12. [Maintenance](#12-maintenance)
13. [Environment variables](#13-environment-variables)

---

## 1. Architecture

Two pipelines share one LanceDB table.

```
posts/*.md  ─┐
             ├─► load.py ──► data/chunks.jsonl ──► index.py ──► data/lancedb/chunks
pages/*.md  ─┘

                                  query.py
                        ┌────────────┴────────────┐
              single-shot │                        │ map-reduce
        retrieve() + expand_links()        _group_issues() → map → reduce
                        │                        │
              data/map_cache.json ◄──────────────┘
              data/answer_cache.json ◄───────────┘
```

| Stage | Script | Output |
|---|---|---|
| Load | `load.py` | `data/chunks.jsonl` — chunked, stripped text with metadata |
| Index | `index.py` | `data/lancedb/chunks` — embeddings + FTS index |
| Query | `query.py` | answer to stdout, sources to stdout, progress to stderr |

**Two query modes:**

- **Single-shot** — embed the question, hybrid-search, optionally pull in linked pages, answer in one model call. No caching (fresh call every time).
- **Map-reduce** — summarize each issue once (the *map*), then answer over the summaries (the *reduce*). Heavily cached; ideal for cross-issue questions.

---

## 2. Repository layout

```
letterFrom/
├── posts/                  # newsletter issues, NNN-slug-hash.md
├── pages/                  # linked standalone articles, slug.md
├── author/                 # author pages (committed, NOT indexed)
├── tag/                    # tag pages (committed, NOT indexed)
├── load.py                 # posts+pages → chunks.jsonl
├── index.py                # chunks.jsonl → LanceDB (resumable)
├── query.py                # all query modes
├── .env                    # NANOGPT_API_KEY, model overrides
├── .gitignore              # data/, .obsidian/
└── data/                   # DERIVED — gitignored
    ├── chunks.jsonl
    ├── lancedb/
    ├── embeddings.<sig>.jsonl   # per-config embed checkpoint (resume point)
    ├── map_cache.json
    └── answer_cache.json
```

---

## 3. Setup

**Requirements:** Python via [`uv`](https://docs.astral.sh/uv/), a nano-gpt API key.

```bash
uv sync                     # install deps from pyproject/uv.lock
```

`.env` at the repo root:

```bash
NANOGPT_API_KEY=sk-...
# optional overrides — see §13 for the full list:
# NANOGPT_BASE_URL=https://api.nano-gpt.com/api/v1
# EMBED_MODEL=text-embedding-3-small
# CHAT_MODEL=qwen/qwen3.7-flash
# REDUCE_MODEL=deepseek/deepseek-v3.2
# MAP_MODEL=qwen/qwen3.7-flash
```

> **Note:** this project has no bare `python` — always use `uv run python`.

---

## 4. Building the index

Run both stages after any content change:

```bash
uv run load.py && uv run index.py
```

Expected output (243 posts, 373 pages):

```
posts=243 (1565 chunks)  pages=373 (1900 chunks) -> data/chunks.jsonl
chunks: 3465 | title prefix: all | sig: 3f9c1a2b
checkpoint: 0 already embedded (data/embeddings.3f9c1a2b.jsonl)
to embed : 3465
batches  : 217 x ~16  workers=12
embedded 3465/3465
table rows: 3465 dim: 1536
```

### 4.1 `load.py`

Parses front-matter, strips image/link markup, chunks to ~2800 chars with 400-char overlap, and emits for every chunk:

- `doc_type` — `post` or `page`
- `doc_id` — `NNN` for posts, `page:<slug>` for pages
- `slug`, `links` — for pages: slug; for posts: array of linked `page:` doc_ids

`load.py` emits the document title into the **first chunk only** (as an H1). See §4.3 for how the indexer extends that.

### 4.2 `index.py` — resumable, concurrent

`index.py` builds the LanceDB table (vector + FTS) with columns `id, doc_id, doc_type, issue_id, issue_num, title, date, source, slug, links, text, vector`, and creates the FTS index via `create_index(config=FTS(with_position=True))` (the LanceDB 0.25+ API).

Three properties make it robust against a slow or flaky embedding gateway:

- **Checkpointing.** Every vector is appended to `data/embeddings.<sig>.jsonl` as it is computed. On restart, already-embedded chunks are skipped. The `<sig>` is a hash of `EMBED_MODEL` + `EMBED_TITLE_PREFIX`, so changing either starts a *fresh, correctly-named* checkpoint instead of silently reusing stale vectors.
- **Adaptive batching.** On a `504`/timeout the batch is **split in half and retried**, recursively, down to a single chunk — rather than failing the whole run. Transient errors (`408/429/5xx`) retry with backoff; non-retryable errors (`400/401/402/403/404/413`) fail fast.
- **Concurrency.** Batches are embedded in parallel via `ThreadPoolExecutor` (default 12 workers), which is what lets a run finish despite high per-request latency. Checkpoint writes are serialized on the main thread and `fsync`ed.

The table is written with `mode="overwrite"`, so a rebuild safely drops and recreates `chunks` — an interrupted run never corrupts the existing table.

### 4.3 Title indexing

The FTS index is built on the `text` column only, and `title` is never embedded. To make headlines searchable by **both** legs, `index.py` prepends the document title to each chunk's text before embedding and storing:

```
242 - Home in Hong Kong        ← prepended by index.py
# 242 - Home in Hong Kong      ← already present in load.py's first chunk
debt spiral mechanics
```

Controlled by `EMBED_TITLE_PREFIX`:

| Value | Effect |
|---|---|
| `all` (default) | Every chunk carries the title — max recall, strongest BM25 boost |
| `first` | Only the doc's first chunk — gentler on BM25 |
| `off` | Original behaviour (title only where `load.py` put it) |

Note the cosmetic duplication on chunk `-000` (the title appears up to three times, because `load.py` already emitted it twice). This is harmless — BM25 term frequency saturates — and only affects the first chunk.

---

## 5. Querying: single-shot

```bash
uv run query.py "what tips does he give for OBEs?" --type page
uv run query.py "OBEs and the matrix" --type all --expand
uv run query.py "home in Hong Kong" --type post --no-expand
```

| Flag | Default | Effect |
|---|---|---|
| `--type post\|page\|all` | `all` | Which document types to retrieve |
| `--expand` / `--no-expand` | `expand` | Pull linked pages into context |
| `--expand-pages N` | `5` | Max linked pages pulled in |
| `--expand-per-page N` | `2` | Max chunks per linked page |
| `--expand-from-top N` | `3` | Only the top-N post hits seed expansion |
| `--per-doc N` | `0` | Max chunks per doc in retrieval (`0` = off) |
| `-k N` | `8` | Result count **and** per-leg candidate pool |
| `--pool N` | `1` | Per-leg over-fetch factor before RRF fusion (`1` = tuned behaviour) |

**Choosing a mode:**

| Question type | Best mode |
|---|---|
| Topical / thematic ("his view on X", "tips for Y") | `--type page` — distilled content, no post noise |
| General / unsure | `--type all --expand` (the default) |
| Diary / temporal ("where was I in June?") | `--type post` |
| Deep dive into one long document | `--per-doc 3` |
| Broad survey, want many distinct sources | `--per-doc 1` |

**Expansion** only applies when `--type` is `post` or `all` (not `page`). Retrieved posts carry their `links`; the top `--expand-from-top` posts seed the pull, capped at `--expand-pages` pages × `--expand-per-page` chunks. Linked-only docs are marked `(linked)` in the source list.

**Citation format** in answers: `[237]` for issues, `[page 10-tips-for-obes]` for pages.

**On `--pool`:** it exists as an escape hatch, but see §10 — widening it is **non-monotonic** and made things worse in testing. Prefer `-k` to widen output.

---

## 6. Querying: map-reduce

```bash
uv run query.py "how did his views on privacy evolve?" --full
uv run query.py "what happened in 2023?" --year 2023
uv run query.py "summarize the Europe trip" --range 76-96
```

Map-reduce is **post-only** — pages are supplementary and excluded.

| Flag | Effect |
|---|---|
| `--full` | All issues |
| `--year YYYY` | One year (needs front-matter dates) |
| `--range LO-HI` | Issue-number range |
| `--cache-mode issue\|question` | `issue` (default): one generic digest per issue, reused across all questions. `question`: tailored per-question summaries |
| `--no-cache` | Ignore both caches, write nothing |
| `--refresh` | Recompute summaries, update the cache |

Progress and the reduce model go to **stderr**; the answer goes to **stdout**, so `> out.md` captures clean text.

The map step uses the structured digest prompt (fields: `PLACES, EVENTS, PEOPLE, PROJECTS, THEMES, READING, QUOTES`). Provider-filter-blocked issues are skipped and reported, not fatal.

---

## 7. CLI reference

| Command | Purpose |
|---|---|
| `uv run query.py --stats` | Cache contents + index chunk counts per doc type |
| `uv run query.py "Q"` | Single-shot, all types, expand on |
| `uv run query.py "Q" --type page` | Pages only |
| `uv run query.py "Q" --type post --no-expand` | Posts only, no linked pages |
| `uv run query.py "Q" --expand-pages 2` | Cheaper expansion |
| `uv run query.py "Q" --per-doc 1` | Maximise source diversity |
| `uv run query.py "Q" -k 30` | Wider output (and a wider per-leg pool) |
| `uv run query.py "Q" --pool 3` | Over-fetch per leg before fusion (see §10) |
| `uv run query.py "Q" --full` | Map-reduce, whole corpus |
| `uv run query.py "Q" --year 2025` | Map-reduce, one year |
| `uv run query.py "Q" --range 45-96` | Map-reduce, issue range |

`--stats` reads the post count from the index, so "generic issues : N of M" reflects the actual corpus.

---

## 8. Caching model

Two caches, both `data/*.json`, both gitignored, both written **atomically** (temp file + `os.replace`).

| Cache | Key | Scope |
|---|---|---|
| `map_cache.json` | `issue:<iid>:<PROMPT_VER>` (generic) or `q:<hash>:<iid>:<PROMPT_VER>` (per-question) | Per-issue summaries |
| `answer_cache.json` | hash of `(question, year, range, mode, models, PROMPT_VER)` | Final map-reduce answers |

**`PROMPT_VER`** is a hash of the map prompts + map model list. Change a map prompt or map model → the version changes → stale summaries are ignored and recomputed. Retrieval-only changes (in `query.py`) do **not** invalidate the cache.

**Important:** single-shot queries bypass the caches entirely — they always make a fresh API call. Only map-reduce is cached.

**The answer cache has no content hash.** If you ingest new content and re-ask a `--full`/`--year` question, the cached answer is served from before the ingest. Use `--refresh` (or `--no-cache`) after a content change.

Current state: **241 of 243 issues warm**. Issues 241 and 242 will map on demand.

---

## 9. Data schema

`data/lancedb/chunks` columns:

| Column | Type | Notes |
|---|---|---|
| `id` | str | `<doc_id>-<chunk index>`, e.g. `237-003` |
| `doc_id` | str | `237` (post) or `page:10-tips-for-obes` (page) |
| `doc_type` | str | `post` \| `page` |
| `issue_id` | str | Zero-padded `237`; empty for pages |
| `issue_num` | int | Numeric sort key; `-1` for pages |
| `title` | str | From front-matter or filename |
| `date` | str | ISO date from front-matter |
| `source` | str | Original filename |
| `slug` | str | Page slug (empty for posts) |
| `links` | list[str] | Linked `page:` doc_ids |
| `text` | str | Chunk body **with the title prepended** (see §4.3) |
| `vector` | vector[1536] | `text-embedding-3-small` |

Current counts: **`{'post': 1565, 'page': 1900}`** — 3,465 chunks.

> Note: `text` is stored **as indexed**, i.e. including the prepended title. `data/chunks.jsonl` remains the untouched `load.py` output, so the two differ by the title prefix.

---

## 10. Design notes & gotchas

**`limit()` on a hybrid query is a ranking knob, not a page size.** In LanceDB, `limit()` bounds the candidates *each leg* (vector, FTS) contributes *before* RRF fusion. Over-fetching changes the fused ranking, and the effect is **non-monotonic** — widening the pool can *demote* a correct result. Measured on the real corpus:

| Query | `--pool 1` | `--pool 3` |
|---|---|---|
| `home in Hong Kong` | issue 242 at rank 4 ✓ | 242 drops to rank 9 |
| `Hong Kong` | absent from top-8 | rank 22 — still cut |
| `Bangkok` | absent from top-8 | rank 18 — still cut |

So widening the pool helped nothing and hurt the one query that worked. **Keep `--pool 1`** (the default). To widen output, raise `-k` — that widens the per-leg pool *and* keeps the extra results, rather than discarding them at the final trim. Filter-only queries (`tbl.search().where(...)`, as in `expand_links`) have no legs to fuse, so their limits are safe.

**The per-leg pool is a hard recall ceiling.** With `--pool 1`, a chunk ranked 19th in FTS and 48th in vector is invisible to fusion no matter how well it would score. If a document you know exists won't surface, either raise `-k` or use a more specific query.

**Saturated queries are not bugs.** Travel terms (`Hong Kong`, `Bangkok`) match hundreds of chunks across the archive. A post ranking ~20th for such a term is correct relevance behaviour. Test newly ingested content with a **discriminating** phrase drawn from its own body or headline (e.g. `home in Hong Kong`), not a term that saturates the corpus.

**Title indexing is an index-time decision.** See §4.3. `load.py` emits the title only in the first chunk; `index.py` extends it to every chunk so headline terms are searchable across all chunks and both legs. This changed every chunk's text, so a rebuild recomputes every embedding and rankings shift globally — re-run the regression queries in §12 after any change to `EMBED_TITLE_PREFIX`.

**`--per-doc` defaults to 0 (off).** Capping chunks per doc removes the depth that long pages need — test A got all ten OBE tips *because* several chunks of `10-tips-of-obes` were in context. Turn it on (`--per-doc 2`) only for broad survey questions.

**`links` are extracted at load time.** Absolute URLs are parsed and suffixes stripped (`translate.goog` noise is excluded). 93 posts carry page links. Only post→page expansion is wired; pages *have* `links` populated (page→page) but `expand_links` ignores them.

**Title cleaning matches numerically.** `_clean_title` strips a leading `NNN - ` prefix by comparing the number, not the string — so `"84 - Back in Bangkok"` on issue `084` strips correctly. String-prefix matching failed on zero-padded ids.

**Filename normalisation.** macOS stores some filenames as NFD (decomposed); git and globs expect NFC. Duplicate issue 232 was a symptom; handled.

**Expansion cost.** Defaults (`5` pages × `2` chunks × ~700 tokens) can add up to ~7,000 tokens to the answer call. Tune per-question with `--expand-pages` / `--expand-from-top`; no re-index needed.

---

## 11. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `zsh: command not found: python` | Use `uv run python` — no global interpreter |
| `504` / `upstream_timeout` on embeddings | nano-gpt gateway congestion, not your code. `index.py` retries, splits, and checkpoints automatically. Confirm with a one-word `curl`; tune `EMBED_BATCH` / `EMBED_WORKERS` |
| Index rebuild starts from zero | Checkpoint missing, or its signature changed (`EMBED_MODEL` / `EMBED_TITLE_PREFIX` edited → new checkpoint → full re-embed by design) |
| New content indexed but not retrieved | `--pool 1` and `-k 8` cap the per-leg pool; try a discriminating query, or `-k 30`. See §10 |
| `question-everything` missing from results | Pool over-fetch — confirm `--pool 1` and `.limit(k)` in `retrieve()` |
| `--stats` prints a stale "of 241" | Post count is now derived from the index; if it's hardcoded, see §7 |
| `ModuleNotFoundError: No module named 'pandas'` | `lancedb`'s `to_pandas()` needs pandas; use `tbl.to_arrow().to_pylist()` instead (no install needed) |
| Answer cites `[page] 084` for a post | Prompt labels posts `[NNN]`; if a post slug leaks, check `doc_type` on the hit |
| Duplicate issue file | NFD/NFC filename collision |
| Range/year query recomputes everything | `PROMPT_VER` changed (map prompt or map model edited) |
| `--full`/`--year` answer ignores new content | `answer_cache.json` has no content hash; use `--refresh` |
| `Repository not found` on push | Create the empty repo on GitHub first; `ssh -T git@github.com` to test the key |

---

## 12. Maintenance

**Re-index when:** posts/pages are added or edited, or `load.py`/`index.py` change.

```bash
uv run load.py && uv run index.py
```

For a long rebuild, run it detached and log it:

```bash
caffeinate -i nohup bash -c 'uv run index.py' > index.log 2>&1 &
tail -f index.log
```

The job resumes from the checkpoint if interrupted — re-running `uv run index.py` skips already-embedded chunks.

**After any re-index, re-run the regression queries** (rankings shift when text changes):

```bash
uv run query.py "OBEs and the matrix" --type page --no-expand   # must surface question-everything
uv run query.py "home in Hong Kong"   --type post --no-expand   # must surface issue 242
```

**Re-warm the map cache when:** a map prompt or map model changes (PROMPT_VER changes) — otherwise it self-serves from cache.

```bash
uv run query.py "overview" --full      # ~$0.04 for the whole corpus
```

**Tune retrieval** (no re-index, no cache impact): `--per-doc`, `--expand-from-top`, `--expand-pages`, `--type`, `-k`.

**Housekeeping:**

- `data/embeddings.<sig>.jsonl` — keep as your resume point; delete only when you're satisfied the index is good.
- Superseded checkpoints (from an older model or title-prefix setting) are safe to delete.
- `answer_cache.json` goes stale on content changes — `--refresh` affected questions.

**Git:** `data/` and `.obsidian/` are ignored; only authored content and code are tracked. Backup remote: `origin` → GitHub. Verify with `git status` (clean) and `uv run query.py --stats`.

**Not indexed:** `author/` and `tag/` are committed but outside the `pages/` glob. Indexing them is a small `load.py` change (a third `doc_type`), deferred by choice.

---

## 13. Environment variables

| Variable | Default | Used by |
|---|---|---|
| `NANOGPT_API_KEY` | — (required) | all |
| `NANOGPT_BASE_URL` | `https://api.nano-gpt.com/api/v1` | all |
| `EMBED_MODEL` | `text-embedding-3-small` | `index.py`, `query.py` |
| `CHAT_MODEL` | `qwen/qwen3.7-flash` | `query.py` (single-shot, reduce fallback) |
| `REDUCE_MODEL` | `deepseek/deepseek-v3.2` | `query.py` (map-reduce reduce) |
| `MAP_MODEL` | `qwen/qwen3.7-flash` | `query.py` (map step) |
| `EMBED_TITLE_PREFIX` | `all` | `index.py` (`all` \| `first` \| `off`) |
| `EMBED_BATCH` | `16` | `index.py` |
| `EMBED_WORKERS` | `12` | `index.py` |
| `EMBED_ATTEMPTS` | `3` | `index.py` |
| `EMBED_TIMEOUT` | `90` | `index.py` |

`MAP_MODELS` also falls back to `deepseek/deepseek-v4-flash-0731` then `mistralai/mistral-nemo-instruct-2407` if the primary is blocked.

