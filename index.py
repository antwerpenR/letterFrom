import os, sys, json, time, random, base64, hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI, APIStatusError, APITimeoutError, APIConnectionError
import lancedb, pyarrow as pa
from lancedb.index import FTS          # Lance-native FTS (LanceDB 0.25.0+)

load_dotenv()
client = OpenAI(
    api_key=os.environ["NANOGPT_API_KEY"],
    base_url=os.environ.get("NANOGPT_BASE_URL", "https://api.nano-gpt.com/api/v1"),
    timeout=float(os.environ.get("EMBED_TIMEOUT", "90")),
    max_retries=0,          # we do our own retries so every failure is visible
)

EMBED_MODEL = os.environ.get("EMBED_MODEL", "text-embedding-3-small")
BATCH    = int(os.environ.get("EMBED_BATCH", "16"))     # 16 proven to fit the timeout
WORKERS  = int(os.environ.get("EMBED_WORKERS", "12"))   # well under the 25 RPS cap
ATTEMPTS = int(os.environ.get("EMBED_ATTEMPTS", "3"))

# --- Fix A ------------------------------------------------------------------
# Prepend each document's title to the indexed text so the headline is
# searchable by BOTH legs (the FTS index is built on `text` only, and `title`
# is never embedded). Without this a post can only be found by whatever its
# BODY happens to say.
#   "all"   -> every chunk carries the title (max recall; strongest BM25 boost)
#   "first" -> only the doc's first chunk carries it (gentler on BM25)
#   "off"   -> original behaviour
TITLE_PREFIX = os.environ.get("EMBED_TITLE_PREFIX", "all").strip().lower()
if TITLE_PREFIX not in ("all", "first", "off"):
    TITLE_PREFIX = "all"

RETRYABLE = {408, 429, 500, 502, 503, 504}

# The checkpoint is named after everything that changes the vectors, so a
# config change (model, or title-prefix mode) starts a FRESH, correctly-named
# file instead of silently reusing stale vectors.
SIG  = hashlib.sha1((EMBED_MODEL + "|" + TITLE_PREFIX).encode()).hexdigest()[:8]
CKPT = Path("data/embeddings." + SIG + ".jsonl")


def enc(vec):
    return base64.b64encode(np.asarray(vec, np.float32).tobytes()).decode()


def dec(s):
    return np.frombuffer(base64.b64decode(s), np.float32).tolist()


def indexed_text(r):
    """Chunk text as it will be embedded AND stored in the `text` column."""
    body = r.get("text", "")
    if TITLE_PREFIX == "off":
        return body
    title = (r.get("title") or "").strip()
    if not title:
        return body
    if TITLE_PREFIX == "first" and not str(r.get("id", "")).endswith("-000"):
        return body
    return title + "\n\n" + body


def embed_adaptive(rows, depth=0):
    """Retry transient errors; on 504/timeout split in half and recurse."""
    texts = [r["text"] for r in rows]
    for a in range(ATTEMPTS):
        try:
            resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
            return list(zip(rows, [list(map(float, d.embedding)) for d in resp.data]))
        except (APIStatusError, APITimeoutError, APIConnectionError) as e:
            st = getattr(e, "status_code", None)
            if st is not None and st not in RETRYABLE:
                raise                       # 400/401/402/403/404/413 -> fail fast
            if st == 504 or isinstance(e, APITimeoutError):
                break                       # too big -> split, don't burn retries
            if a == ATTEMPTS - 1:
                raise
            time.sleep(2.0 * 2 ** a + random.uniform(0, 1))

    if len(rows) == 1:
        raise RuntimeError("could not embed chunk id=" + repr(rows[0].get("id")))
    mid = len(rows) // 2
    print("  split " + str(len(rows)) + " -> " + str(mid) + "+" + str(len(rows) - mid),
          file=sys.stderr, flush=True)
    return embed_adaptive(rows[:mid], depth + 1) + embed_adaptive(rows[mid:], depth + 1)


# ---------------- load ----------------
rows = [json.loads(l) for l in open("data/chunks.jsonl", encoding="utf-8")]
for i, r in enumerate(rows):
    r.setdefault("id", f"row:{i}")
    r["text"] = indexed_text(r)          # Fix A applied here, before embedding
print("chunks:", len(rows), "| title prefix:", TITLE_PREFIX, "| sig:", SIG)

# ---------------- resume from checkpoint ----------------
done = {}
if CKPT.exists():
    for line in CKPT.open(encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        rec = json.loads(line)
        done[rec["id"]] = dec(rec["vec"])
    print(f"checkpoint: {len(done)} already embedded ({CKPT.name})")

todo = [r for r in rows if r["id"] not in done]
print("to embed :", len(todo))

batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
print("batches  :", len(batches), f"x ~{BATCH}  workers={WORKERS}")

# ---------------- embed concurrently, checkpoint on the main thread ----------------
if todo:
    fh = CKPT.open("a", encoding="utf-8")
    n = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(embed_adaptive, b): b for b in batches}
        for fut in as_completed(futs):
            for r, vec in fut.result():      # raises -> run aborts, checkpoint kept
                done[r["id"]] = vec
                fh.write(json.dumps({"id": r["id"], "vec": enc(vec)}) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
            n += len(futs[fut])
            print(f"embedded {n}/{len(todo)}", flush=True)
    fh.close()

for r in rows:
    r["vector"] = done[r["id"]]

# ---------------- table (unchanged) ----------------
for r in rows:
    r.setdefault("doc_type", "post")
    r.setdefault("doc_id", f"post:{r.get('issue_id','')}")
    r.setdefault("slug", "")
    r.setdefault("links", [])

dim = len(rows[0]["vector"])
db = lancedb.connect("data/lancedb")
schema = pa.schema([
    ("id",        pa.string()),
    ("issue_id",  pa.string()),
    ("issue_num", pa.int64()),
    ("title",     pa.string()),
    ("date",      pa.string()),
    ("source",    pa.string()),
    ("doc_type",  pa.string()),
    ("doc_id",    pa.string()),
    ("slug",      pa.string()),
    ("links",     pa.list_(pa.string())),
    ("text",      pa.string()),
    ("vector",    pa.list_(pa.float32(), dim)),
])
tbl = db.create_table("chunks", data=rows, schema=schema, mode="overwrite")
tbl.create_index("text", config=FTS(with_position=True), replace=True)
print("table rows:", tbl.count_rows(), "dim:", dim)

