import os, json
from dotenv import load_dotenv
from openai import OpenAI
import lancedb, pyarrow as pa

load_dotenv()
client = OpenAI(api_key=os.environ["NANOGPT_API_KEY"],
                base_url=os.environ.get("NANOGPT_BASE_URL", "https://api.nano-gpt.com/api/v1"))

EMBED_MODEL = os.environ.get("EMBED_MODEL", "text-embedding-3-small")
BATCH = 256

rows = [json.loads(l) for l in open("data/chunks.jsonl", encoding="utf-8")]
print("chunks:", len(rows))

for i in range(0, len(rows), BATCH):
    batch = rows[i:i+BATCH]
    resp = client.embeddings.create(model=EMBED_MODEL, input=[r["text"] for r in batch])
    for r, d in zip(batch, resp.data):
        r["vector"] = [float(x) for x in d.embedding]
    print(f"embedded {min(i+BATCH, len(rows))}/{len(rows)}")

dim = len(rows[0]["vector"])
db = lancedb.connect("data/lancedb")
schema = pa.schema([
    ("id", pa.string()), ("issue_id", pa.string()), ("issue_num", pa.int64()),
    ("title", pa.string()), ("date", pa.string()), ("source", pa.string()),
    ("text", pa.string()), ("vector", pa.list_(pa.float32(), dim)),
])
tbl = db.create_table("chunks", data=rows, schema=schema, mode="overwrite")
tbl.create_fts_index("text")          # BM25 keyword index on sync connections
print("table rows:", tbl.count_rows(), "dim:", dim)
