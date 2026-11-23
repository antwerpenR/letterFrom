#!/usr/bin/env python
"""sync_check.py — verify the LanceDB index agrees with data/chunks.jsonl.

chunks.jsonl is the single source of truth (the builder writes it; Syncthing
carries it). This script derives every expectation from it, so nothing here
needs updating when the archive grows.

Run on the builder AND the reader. The `table text sha` line must match on
both machines — that is the real coherence test.

Exit status: 0 = coherent, 1 = divergence.
"""
import collections
import hashlib
import json
import pathlib
import sys

import lancedb

CHUNKS = pathlib.Path("data/chunks.jsonl")
DB_DIR = pathlib.Path("data/lancedb")
TABLE = "chunks"
U64MAX = (1 << 64) - 1

fail = []


def check(label, ok, detail=""):
    print(f"{label:<14}: {'OK' if ok else 'FAIL'}" + (f" {detail}" if detail else ""))
    if not ok:
        fail.append(label)


def text_sha(pairs):
    """Stable hash over (id, text) sorted by id."""
    h = hashlib.sha256()
    for cid, txt in sorted(pairs):
        h.update(cid.encode())
        h.update(b"\x00")
        h.update((txt or "").encode())
    return h.hexdigest()[:16]


def main():
    if not CHUNKS.exists():
        print(f"missing {CHUNKS} — run load.py first")
        return 1
    if not DB_DIR.exists():
        print(f"missing {DB_DIR} — run index.py first")
        return 1

    chunks = [json.loads(line) for line in CHUNKS.open(encoding="utf-8") if line.strip()]
    ch = {}
    dupe = []
    for c in chunks:
        if c["id"] in ch:
            dupe.append(c["id"])
        ch[c["id"]] = c

    tbl = lancedb.connect(str(DB_DIR)).open_table(TABLE)

    # ---- versions (Lance names manifests as U64MAX - version) --------------
    vf = sorted((DB_DIR / f"{TABLE}.lance" / "_versions").glob("*.manifest"))
    vers = sorted(U64MAX - int(p.stem) for p in vf) if vf else []
    print(f"{'versions':<14}: {vers[-1] if vers else 0} writes"
          f" | manifests: {len(vers)}")

    # ---- read table without the vector column -----------------------------
    arrow = tbl.to_arrow()
    cols = [n for n in arrow.column_names if n != "vector"]
    rows = arrow.select(cols).to_pylist()
    tab = {r["id"]: r for r in rows}

    # ---- counts ------------------------------------------------------------
    print(f"{'table rows':<14}: {tbl.count_rows()}")
    print(f"{'chunks.jsonl':<14}: {len(chunks)}")
    check("row counts", tbl.count_rows() == len(chunks))
    check("unique ids", not dupe, str(dupe[:3]) if dupe else "")

    # ---- id sets -----------------------------------------------------------
    only_tab = set(tab) - set(ch)
    only_ch = set(ch) - set(tab)
    check("id sets", not only_tab and not only_ch,
          f"+{len(only_tab)} table-only / -{len(only_ch)} chunks-only"
          if (only_tab or only_ch) else "")

    # ---- per-field drift (metadata changes without re-embedding) -----------
    drift = [(k, tab[k].get("date"), ch[k].get("date"))
             for k in ch if k in tab and tab[k].get("date") != ch[k].get("date")]
    check("date drift", not drift, str(drift[:3]) if drift else "")

    # ---- text identity: table vs source of truth ---------------------------
    ch_sha = text_sha((k, c.get("text")) for k, c in ch.items())
    tb_sha = text_sha((k, r.get("text")) for k, r in tab.items())
    print(f"{'chunks sha':<14}: {ch_sha}")
    print(f"{'table text sha':<14}: {tb_sha}")
    check("text match", ch_sha == tb_sha)

    # ---- embeddings present ------------------------------------------------
    vec_col = tbl.to_arrow().column("vector") if "vector" in arrow.column_names else None
    if vec_col is not None:
        dims = {len(v) for v in vec_col.to_pylist() if v is not None and len(v)}
        nulls = sum(1 for v in vec_col.to_pylist() if v is None or len(v) == 0)
        print(f"{'vector dim':<14}: {sorted(dims)} | missing: {nulls}")
        check("embeddings", nulls == 0 and len(dims) == 1)

    # ---- issue coverage (one row per issue, not per chunk) -----------------
    posts = [c for c in chunks if c.get("doc_type") == "post"]
    issue_year = {}
    for c in posts:
        iid = c.get("issue_id")
        if iid and iid not in issue_year:
            issue_year[iid] = (c.get("date") or "")[:4]

    dateless = [iid for iid, y in issue_year.items() if not y]
    check("undated issues", not dateless, str(dateless[:5]) if dateless else "")
    print(f"{'issues':<14}: {len(issue_year)}")
    print(f"{'issues/year':<14}: "
          f"{dict(sorted(collections.Counter(y for y in issue_year.values() if y).items()))}")

    # ---- doc_type split ----------------------------------------------------
    print(f"{'doc types':<14}: "
          f"{dict(sorted(collections.Counter(c.get('doc_type') for c in chunks).items()))}")

    # ---- FTS smoke test ----------------------------------------------------
    if tbl.count_rows():
        try:
            hits = tbl.search("Hong Kong", query_type="fts").limit(3).to_list()
            for x in hits:
                print(f"  fts: {x.get('doc_type')} {x.get('slug')!r} "
                      f"{round(x.get('_score', 0), 2)}")
            check("fts probe", bool(hits))
        except Exception as e:  # noqa: BLE001
            check("fts probe", False, f"{type(e).__name__}: {e}")

    # ---- verdict -----------------------------------------------------------
    print()
    if fail:
        print("verdict       : MISMATCH — " + ", ".join(fail)
              + " | re-run load.py then index.py")
        return 1
    print("verdict       : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

