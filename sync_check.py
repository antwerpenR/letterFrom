#!/usr/bin/env python
"""sync_check.py v4 — verify LanceDB index vs data/chunks.jsonl.

index.py embeds  title + SEP + chunk_text  (EMBED_TITLE_PREFIX=all),
so the table's `text` column is PREFIXED while chunks.jsonl holds the RAW
chunk. This check reproduces that transform before comparing.

  expected embed == table text sha  -> table matches chunks.jsonl
  table text sha                    -> must be IDENTICAL across machines

Exit 0 = coherent, 1 = divergence.
"""
import collections
import hashlib
import json
import os
import pathlib
import sys

import lancedb

VERSION = 4

# --- must mirror index.py --------------------------------------------------
PREFIX = os.environ.get("EMBED_TITLE_PREFIX", "all").lower()
SEP = "\n\n"                       # confirm: grep -n 'prefix\|title' index.py
PREFIXED = PREFIX in ("all", "1", "true", "yes")
# ---------------------------------------------------------------------------

CHUNKS = pathlib.Path("data/chunks.jsonl")
DB_DIR = pathlib.Path("data/lancedb")
TABLE = "chunks"
U64MAX = (1 << 64) - 1

fail = []


def check(label, ok, detail=""):
    print(f"{label:<16}: {'OK' if ok else 'FAIL'}" + (f" {detail}" if detail else ""))
    if not ok:
        fail.append(label)


def embed_doc(c):
    """Reproduce the text index.py actually embedded for this chunk."""
    txt = c.get("text") or ""
    title = (c.get("title") or "").strip()
    if PREFIXED and title:
        return f"{title}{SEP}{txt}"
    return txt


def sha(pairs):
    h = hashlib.sha256()
    for cid, txt in sorted(pairs):
        h.update(cid.encode())
        h.update(b"\x00")
        h.update((txt or "").encode())
    return h.hexdigest()[:16]


def main():
    print(f"{'check ver':<16}: {VERSION} "
          f"(prefix={PREFIX!r} sep={SEP!r} prefixed={PREFIXED})")

    for p, hint in ((CHUNKS, "run load.py"), (DB_DIR, "run index.py")):
        if not p.exists():
            print(f"missing {p} — {hint} first")
            return 1

    chunks = [json.loads(l) for l in CHUNKS.open(encoding="utf-8") if l.strip()]
    ch, dupe = {}, []
    for c in chunks:
        if c["id"] in ch:
            dupe.append(c["id"])
        ch[c["id"]] = c

    tbl = lancedb.connect(str(DB_DIR)).open_table(TABLE)
    arrow = tbl.to_arrow()
    cols = [n for n in arrow.column_names if n != "vector"]
    tab = {r["id"]: r for r in arrow.select(cols).to_pylist()}

    # ---- versions ---------------------------------------------------------
    vf = sorted((DB_DIR / f"{TABLE}.lance" / "_versions").glob("*.manifest"))
    vers = sorted(U64MAX - int(p.stem) for p in vf) if vf else []
    print(f"{'versions':<16}: {vers[-1] if vers else 0} writes | manifests: {len(vers)}")

    # ---- counts / ids -----------------------------------------------------
    print(f"{'table rows':<16}: {tbl.count_rows()}")
    print(f"{'chunks.jsonl':<16}: {len(chunks)}")
    check("row counts", tbl.count_rows() == len(chunks))
    check("unique ids", not dupe, str(dupe[:3]) if dupe else "")

    only_t = set(tab) - set(ch)
    only_c = set(ch) - set(tab)
    check("id sets", not only_t and not only_c,
          f"+{len(only_t)} table-only / -{len(only_c)} chunks-only"
          if (only_t or only_c) else "")

    # ---- metadata drift (changes without re-embedding) --------------------
    drift = [(k, tab[k].get("date"), ch[k].get("date"))
             for k in ch if k in tab and tab[k].get("date") != ch[k].get("date")]
    check("date drift", not drift, str(drift[:3]) if drift else "")

    # ---- text identity ----------------------------------------------------
    raw_sha = sha((k, c.get("text")) for k, c in ch.items())
    exp_sha = sha((k, embed_doc(c)) for k, c in ch.items())
    tab_sha = sha((k, r.get("text")) for k, r in tab.items())
    print(f"{'chunks raw sha':<16}: {raw_sha}")
    print(f"{'expected embed':<16}: {exp_sha}")
    print(f"{'table text sha':<16}: {tab_sha}   <- compare across machines")

    if tab_sha == exp_sha:
        check("text match", True)
    else:
        bad = [k for k in ch if k in tab and embed_doc(ch[k]) != tab[k].get("text")]
        check("text match", False, f"{len(bad)} rows disagree")
        if bad:
            k = bad[0]
            a, b = embed_doc(ch[k]), (tab[k].get("text") or "")
            print(f"  first diff id={k} len {len(a)} vs {len(b)}")
            print(f"    expected {a[:120]!r}")
            print(f"    table    {b[:120]!r}")
            print("  -> every row differs: SEP/PREFIX wrong |"
                  " few rows: index stale")

    # ---- embeddings -------------------------------------------------------
    if "vector" in arrow.column_names:
        vecs = arrow.column("vector").to_pylist()
        dims = {len(v) for v in vecs if v}
        nulls = sum(1 for v in vecs if not v)
        print(f"{'vector dim':<16}: {sorted(dims)} | missing: {nulls}")
        check("embeddings", nulls == 0 and len(dims) == 1)

    # ---- issue coverage (per issue, not per chunk) ------------------------
    posts = [c for c in chunks if c.get("doc_type") == "post"]
    issue_year = {}
    for c in posts:
        iid = c.get("issue_id")
        if iid and iid not in issue_year:
            issue_year[iid] = (c.get("date") or "")[:4]
    dateless = [iid for iid, y in issue_year.items() if not y]
    check("undated issues", not dateless, str(dateless[:5]) if dateless else "")
    print(f"{'issues':<16}: {len(issue_year)}")
    print(f"{'issues/year':<16}: "
          f"{dict(sorted(collections.Counter(y for y in issue_year.values() if y).items()))}")
    print(f"{'doc types':<16}: "
          f"{dict(sorted(collections.Counter(c.get('doc_type') for c in chunks).items()))}")

    # ---- FTS smoke test ---------------------------------------------------
    if tbl.count_rows():
        try:
            hits = tbl.search("Hong Kong", query_type="fts").limit(3).to_list()
            for x in hits:
                print(f"  fts: {x.get('doc_type')} {x.get('slug')!r} "
                      f"{round(x.get('_score', 0), 2)}")
            check("fts probe", bool(hits))
        except Exception as e:
            check("fts probe", False, f"{type(e).__name__}: {e}")

    print()
    if fail:
        print("verdict         : MISMATCH — " + ", ".join(fail))
        return 1
    print("verdict         : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

