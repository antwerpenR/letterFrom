import os, json, argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["NANOGPT_API_KEY"],
    base_url=os.environ.get("NANOGPT_BASE_URL", "https://api.nano-gpt.com/api/v1"),
)

NL = chr(10)
BLOCK_WORDS = [
    "content_policy",
    "safety filter",
    "blocked",
    "policy violation",
]


def check(prompt, model):
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return "ok", r.choices[0].message.content
    except Exception as e:
        low = str(e).lower()
        if any(w in low for w in BLOCK_WORDS):
            return "block", str(e)[:300]
        return "error", str(e)[:300]


def load_issue(issue_id):
    rows = []
    with open("data/chunks.jsonl", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r["issue_id"] == issue_id:
                rows.append(r)
    rows.sort(key=lambda r: r["id"])
    return rows


def build(question, iid, title, text, raw):
    if raw:
        return text
    return (
        "Summarize this newsletter issue in 3-5 concise bullets. Focus on "
        "anything relevant to: " + question + NL + NL +
        "Issue " + iid + ": " + title + NL + NL + text
    )


def bisect(pieces, make, model, joiner):
    status, _ = check(make(joiner.join(pieces)), model)
    if status != "block":
        return None
    if len(pieces) == 1:
        return pieces[0]
    mid = len(pieces) // 2
    for half in (pieces[:mid], pieces[mid:]):
        if not half:
            continue
        res = bisect(half, make, model, joiner)
        if res is not None:
            return res
    return "COMBINATION OF: " + joiner.join(pieces)


def isolate(text, make, model):
    paras = [p for p in text.split(NL + NL) if p.strip()]
    hit = bisect(paras, make, model, NL + NL) if len(paras) > 1 else text
    if hit and len(hit) > 350:
        sents = [s for s in hit.replace("? ", ". ").replace("! ", ". ").split(". ") if s.strip()]
        if len(sents) > 1:
            deeper = bisect(sents, make, model, ". ")
            if deeper:
                hit = deeper
    return hit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("issue_id")
    ap.add_argument("--question", default="Summarize the whole arc of 2022")
    ap.add_argument("--model", default="qwen/qwen3.7-flash")
    ap.add_argument("--raw", action="store_true")
    a = ap.parse_args()

    rows = load_issue(a.issue_id)
    if not rows:
        print("no chunks found for issue", a.issue_id)
        return
    title = rows[0]["title"]
    print("issue", a.issue_id, "|", title, "| chunks:", len(rows),
          "| model:", a.model, "| raw:", a.raw)

    def make(text):
        return build(a.question, a.issue_id, title, text, a.raw)

    st, _ = check(a.question, a.model)
    print("bare question alone:", st)

    blocking = []
    for r in rows:
        st, detail = check(make(r["text"]), a.model)
        print("  " + r["id"], st)
        if st == "block":
            blocking.append(r)

    if not blocking:
        print(NL + "No single chunk blocks. Testing the whole issue as one prompt...")
        whole = NL.join(r["text"] for r in rows)
        st, _ = check(make(whole), a.model)
        print("whole issue:", st)
        if st == "block":
            report(isolate(whole, make, a.model), make, a.model)
        return

    print(NL + "Blocking chunks: " + ", ".join(r["id"] for r in blocking))
    for r in blocking:
        report(isolate(r["text"], make, a.model), make, a.model)


def report(hit, make, model):
    print(NL + "=== ISOLATED TRIGGER ===")
    if not hit:
        print("Could not isolate (block may be non-deterministic).")
        return
    print(hit[:1200])
    print(NL + "--- re-testing this text alone ---")
    st, detail = check(make(hit), model)
    print("verdict:", st)
    if st != "ok":
        print(detail)


if __name__ == "__main__":
    main()
