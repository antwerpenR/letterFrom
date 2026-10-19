import json, re, pathlib
from urllib.parse import urlparse

POSTS = pathlib.Path("posts")
PAGES = pathlib.Path("pages")
OUT = pathlib.Path("data/chunks.jsonl")
OUT.parent.mkdir(exist_ok=True)

TARGET_CHARS = 2800      # ~700 tokens
OVERLAP_CHARS = 400
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
NAME = re.compile(r"^(\d+)-(.+)-([0-9a-f]{6})$", re.I)
HASH6 = re.compile(r"-[0-9a-f]{6}$", re.I)
IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")
WIKI_LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")

# only links pointing at your own site can be page links
SITE_HOSTS = {"rogerprice.me", "www.rogerprice.me"}


def split_fm(text):
    m = FM.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    return meta, text[m.end():]


def parse_name(p):
    m = NAME.match(p.stem)
    if m:
        return int(m.group(1)), m.group(2).replace("-", " ").strip().title()
    return None, p.stem


def bare_slug(stem):
    """10-tips-for-obes-2765ed -> 10-tips-for-obes"""
    return HASH6.sub("", stem)


def build_page_index():
    """Map every plausible link target -> canonical page stem."""
    idx = {}
    for p in sorted(PAGES.glob("*.md")):
        idx[p.stem] = p.stem
        idx[bare_slug(p.stem)] = p.stem
    return idx


def extract_links(body, page_idx):
    """Return sorted page doc_ids referenced by this document."""
    body = IMG.sub("", body)          # ignore image URLs
    out = set()

    def lookup(seg):
        seg = (seg or "").strip().rstrip("/").split("#")[0]
        if seg.endswith(".md"):
            seg = seg[:-3]
        if not seg:
            return None
        return page_idx.get(seg) or page_idx.get(bare_slug(seg))

    for m in MD_LINK.finditer(body):
        raw = m.group(2).strip()
        if raw.startswith(("#", "mailto:")):
            continue
        u = urlparse(raw)
        if u.scheme in ("http", "https"):
            if u.hostname not in SITE_HOSTS:   # drops translate.goog, youtube, ...
                continue
        seg = u.path.rstrip("/").split("/")[-1]
        stem = lookup(seg)
        if stem:
            out.add(f"page:{stem}")

    for m in WIKI_LINK.finditer(body):          # inert here (footnote refs),
        stem = lookup(m.group(1))               # kept for future [[page]] links
        if stem:
            out.add(f"page:{stem}")

    return sorted(out)


def chunk_md(text, target=TARGET_CHARS, overlap=OVERLAP_CHARS):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    chunks, buf, size = [], [], 0
    for b in blocks:
        if size + len(b) > target and buf:
            chunks.append("\n\n".join(buf))
            tail, tsz = [], 0
            for prev in reversed(buf):
                if tsz + len(prev) > overlap:
                    break
                tail.insert(0, prev); tsz += len(prev)
            buf, size = tail, tsz
        buf.append(b); size += len(b)
    if buf:
        chunks.append("\n\n".join(buf))
    return chunks


def main():
    page_idx = build_page_index()

    post_files = sorted(POSTS.glob("*.md"),
                        key=lambda p: (parse_name(p)[0] is None, parse_name(p)[0] or 0))
    page_files = sorted(PAGES.glob("*.md"))

    n_posts = n_pages = 0
    with OUT.open("w", encoding="utf-8") as f:
        # ---- posts ----
        for p in post_files:
            num, title = parse_name(p)
            meta, body = split_fm(p.read_text(encoding="utf-8"))
            title = meta.get("title", title)
            iid = f"{num:03d}" if num is not None else p.stem
            links = extract_links(body, page_idx)      # doc-level, on every chunk
            for i, ch in enumerate(chunk_md(body)):
                f.write(json.dumps({
                    "id": f"{iid}-{i:03d}", "issue_id": iid,
                    "issue_num": num if num is not None else -1,
                    "title": title, "date": meta.get("date", ""), "source": p.name,
                    "doc_type": "post", "doc_id": f"post:{iid}",
                    "slug": "", "links": links, "text": ch,
                }, ensure_ascii=False) + "\n")
                n_posts += 1

        # ---- pages ----
        for p in page_files:
            stem = p.stem
            meta, body = split_fm(p.read_text(encoding="utf-8"))
            title = meta.get("title", bare_slug(stem).replace("-", " ").title())
            links = extract_links(body, page_idx)      # page -> page links
            for i, ch in enumerate(chunk_md(body)):
                f.write(json.dumps({
                    "id": f"page-{stem}-{i:03d}", "issue_id": "",
                    "issue_num": -1, "title": title, "date": meta.get("date", ""),
                    "source": p.name, "doc_type": "page",
                    "doc_id": f"page:{stem}", "slug": bare_slug(stem),
                    "links": links, "text": ch,
                }, ensure_ascii=False) + "\n")
                n_pages += 1

    print(f"posts={len(post_files)} ({n_posts} chunks)  "
          f"pages={len(page_files)} ({n_pages} chunks) -> {OUT}")


if __name__ == "__main__":
    main()

