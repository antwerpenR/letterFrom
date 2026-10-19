# letterFrom

Local RAG over 241 weekly newsletter issues (Markdown) using nano-gpt for
embeddings and inference. Ask questions, get cited answers, and summarize
any year or the whole archive.

## Quick start

    uv run check.py                      # verify API + models
    uv run load.py && uv run index.py    # build the index (once, ~$0.02)
    uv run query.py "your question"      # ask
    uv run review.py 2023                # summarize a year

## Scripts

| File | Purpose |
|---|---|
| `load.py` | `posts/*.md` → `data/chunks.jsonl` |
| `index.py` | Embed chunks → LanceDB (hybrid vector + BM25) |
| `query.py` | Retrieve → generate; map-reduce for `--full`/`--range` |
| `review.py` | Year → issue-range wrapper |
| `probe.py` | Diagnose content-filter blocks |
| `check.py` | API connectivity + model sanity check |

## Notes

- `data/` is generated and git-ignored. Rebuild with `load.py` + `index.py`.
- Frontmatter dates are empty, so use `--range` (issue numbers), not `--year`.
