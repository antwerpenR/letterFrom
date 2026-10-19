import json, re, pathlib

POSTS = pathlib.Path("posts")
OUT = pathlib.Path("data/chunks.jsonl")
OUT.parent.mkdir(exist_ok=True)

TARGET_CHARS = 2800      # ~700 tokens
OVERLAP_CHARS = 400
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
NAME = re.compile(r"^(\d+)-(.+)-([0-9a-f]{6})$", re.I)

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
    files = sorted(POSTS.glob("*.md"),
                   key=lambda p: (parse_name(p)[0] is None, parse_name(p)[0] or 0))
    n = 0
    with OUT.open("w", encoding="utf-8") as f:
        for p in files:
            num, title = parse_name(p)
            meta, body = split_fm(p.read_text(encoding="utf-8"))
            title = meta.get("title", title)
            date = meta.get("date", "")
            iid = f"{num:03d}" if num is not None else p.stem
            chs = chunk_md(body)
            for i, ch in enumerate(chs):
                f.write(json.dumps({
                    "id": f"{iid}-{i:03d}", "issue_id": iid,
                    "issue_num": num if num is not None else -1,
                    "title": title, "date": date, "source": p.name, "text": ch,
                }, ensure_ascii=False) + "\n")
            n += len(chs)
    print(f"files={len(files)} chunks={n} -> {OUT}")

if __name__ == "__main__":
    main()
