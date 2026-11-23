# sync_check.py — corrected version decoding
import lancedb, pathlib

U64MAX = (1 << 64) - 1
t = lancedb.connect("data/lancedb").open_table("chunks")
print("table rows :", t.count_rows())
print("chunks.jsonl:", sum(1 for _ in open("data/chunks.jsonl", encoding="utf-8")))

vf = sorted(pathlib.Path("data/lancedb/chunks.lance/_versions").glob("*.manifest"))
vers = sorted(U64MAX - int(p.stem) for p in vf)
print("versions   :", vers, "| latest:", vers[-1], "of", len(vers))

# label the FTS hits properly (see note below)
r = t.search("Hong Kong", query_type="fts").limit(3).to_list()
for x in r:
    print("  fts:", repr(x["issue_id"]), x["doc_type"], repr(x["slug"]), round(x["_score"], 2))

devnull = open("/dev/null", "w") if False else None
ok = (t.count_rows() == 3465)
print("verdict    :", "OK" if ok else "MISMATCH — wait for sync, then re-run")
