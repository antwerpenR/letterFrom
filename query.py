import os, sys, json, hashlib, argparse, pathlib, time, tempfile
from dotenv import load_dotenv
from openai import OpenAI
import lancedb

NL = chr(10)

load_dotenv()
client = OpenAI(
    api_key=os.environ["NANOGPT_API_KEY"],
    base_url=os.environ.get("NANOGPT_BASE_URL", "https://api.nano-gpt.com/api/v1"),
)
db = lancedb.connect("data/lancedb")
tbl = db.open_table("chunks")

EMBED_MODEL  = os.environ.get("EMBED_MODEL", "text-embedding-3-small")
CHAT_MODEL   = os.environ.get("CHAT_MODEL", "qwen/qwen3.7-flash")
REDUCE_MODEL = os.environ.get("REDUCE_MODEL", "deepseek/deepseek-v3.2")

MAP_MODELS = []
for m in (
    os.environ.get("MAP_MODEL", "qwen/qwen3.7-flash"),
    "deepseek/deepseek-v4-flash-0731",
    "mistralai/mistral-nemo-instruct-2407",
):
    if m and m not in MAP_MODELS:
        MAP_MODELS.append(m)

MAP_CACHE = pathlib.Path("data/map_cache.json")
ANSWER_CACHE = pathlib.Path("data/answer_cache.json")

BLOCK_WORDS = ("content_policy", "safety filter", "blocked", "policy violation")

GENERIC_INSTR = (
    "Summarize this newsletter issue as a structured digest. Use these exact "
    "field labels, one per line, and write 'none' when a field does not apply." + NL +
    "PLACES: where the author was and any travel." + NL +
    "EVENTS: what happened, with any dates or times of year mentioned." + NL +
    "PEOPLE: named people who appear (family, friends, colleagues)." + NL +
    "PROJECTS: work, business, building, writing, or technical projects." + NL +
    "THEMES: recurring ideas, opinions, or arguments." + NL +
    "READING: any books, films, podcasts, or articles mentioned by title." + NL +
    "QUOTES: one or two short verbatim lines worth remembering." + NL +
    "Be factual and specific. Do not add commentary."
)

QUESTION_INSTR = (
    "Summarize this newsletter issue in 3-5 concise bullets. Focus on "
    "anything relevant to the question below. Be factual and specific."
)

PROMPT_VER = hashlib.sha1(
    (GENERIC_INSTR + "||" + QUESTION_INSTR + "||" + ",".join(MAP_MODELS)).encode()
).hexdigest()[:10]


def norm(q):
    return " ".join(q.split()).strip()


def sha(s):
    return hashlib.sha1(s.encode()).hexdigest()


def load_json(path):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_json(path, data):
    path.parent.mkdir(exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    os.replace(tmp, path)


def chat_with_fallback(prompt, models, tries=2):
    last = None
    for model in models:
        for attempt in range(tries):
            try:
                r = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
                return r.choices[0].message.content, model
            except Exception as e:
                last = e
                s = str(e).lower()
                if any(w in s for w in BLOCK_WORDS):
                    break
                time.sleep(1.5 * (attempt + 1))
    raise last


def retrieve(question, k=8):
    qv = client.embeddings.create(model=EMBED_MODEL, input=[question]).data[0].embedding
    return tbl.search(query_type="hybrid").vector(qv).text(question).limit(k).to_list()


def answer(question, k=8):
    hits = retrieve(question, k)
    ctx = (NL + NL + "---" + NL + NL).join(
        "[" + h["issue_id"] + "] " + h["title"] + NL + h["text"] for h in hits)
    prompt = ("Answer using ONLY the excerpts below. Cite the issue number "
              "of each excerpt you use." + NL + NL + ctx + NL + NL +
              "Question: " + question)
    out, _ = chat_with_fallback(prompt, [CHAT_MODEL])
    print(out)
    print(NL + "Sources:")
    seen = set()
    for h in hits:
        if h["issue_id"] in seen:
            continue
        seen.add(h["issue_id"])
        print("  - [" + h["issue_id"] + "] " + h["title"])


def _group_issues(year=None, lo=None, hi=None):
    rows = tbl.to_arrow().to_pylist()
    by = {}
    for r in rows:
        by.setdefault(r["issue_id"], []).append(r)
    items = []
    for iid, cs in by.items():
        cs.sort(key=lambda c: c["id"])
        items.append((cs[0]["issue_num"], iid, cs))
    items.sort(key=lambda t: t[0])
    if year:
        items = [t for t in items if str(t[2][0].get("date", "")).startswith(str(year))]
    if lo is not None:
        items = [t for t in items if t[0] >= lo]
    if hi is not None:
        items = [t for t in items if t[0] <= hi]
    return items


def map_key(question, iid, mode):
    if mode == "issue":
        return "issue:" + iid + ":" + PROMPT_VER
    return "q:" + sha(norm(question)) + ":" + iid + ":" + PROMPT_VER


def build_map_prompt(question, iid, title, text, mode):
    head = "Issue " + iid + ": " + title
    if mode == "issue":
        instr = GENERIC_INSTR
    else:
        instr = QUESTION_INSTR + NL + "Question: " + question
    return instr + NL + NL + head + NL + NL + text


def _summarize(question, iid, title, text, cache, mode, read, write):
    key = map_key(question, iid, mode)
    if read and key in cache:
        return cache[key], "cache"
    prompt = build_map_prompt(question, iid, title, text, mode)
    summary, model = chat_with_fallback(prompt, MAP_MODELS)
    if write:
        cache[key] = summary
        save_json(MAP_CACHE, cache)
    return summary, model


def answer_key(question, year, lo, hi, mode):
    sig = "|".join([norm(question), str(year), str(lo), str(hi), mode,
                    ",".join(MAP_MODELS), REDUCE_MODEL, PROMPT_VER])
    return sha(sig)


def answer_mapreduce(question, year=None, lo=None, hi=None, mode="issue",
                     use_cache=True, refresh=False):
    items = _group_issues(year, lo, hi)
    if not items:
        print("No issues matched (check --range / --year).")
        return

    akey = answer_key(question, year, lo, hi, mode)
    acache = load_json(ANSWER_CACHE)
    if use_cache and not refresh and akey in acache:
        print(acache[akey]["answer"])
        print(NL + "(from answer cache; use --no-cache or --refresh to recompute)",
              file=sys.stderr)
        return

    cache = load_json(MAP_CACHE)
    read = use_cache and not refresh
    write = use_cache

    partials, skipped = [], []
    have = sum(1 for num, iid, cs in items
               if read and map_key(question, iid, mode) in cache)
    print("mapping " + str(len(items)) + " issues (" + str(have) + " cached, " +
          str(len(items) - have) + " to compute)...", file=sys.stderr)

    for i, (num, iid, cs) in enumerate(items, 1):
        text = (NL + NL).join(c["text"] for c in cs)
        title = cs[0]["title"]
        try:
            s, model = _summarize(question, iid, title, text, cache, mode, read, write)
            partials.append((iid, title, s))
            tag = "cache" if model == "cache" else model
            print("  [" + str(i) + "/" + str(len(items)) + "] " + iid +
                  " ok (" + tag + ")", file=sys.stderr)
        except Exception as e:
            skipped.append((iid, title, str(e)[:90]))
            print("  [" + str(i) + "/" + str(len(items)) + "] " + iid +
                  " SKIP " + str(e)[:90], file=sys.stderr)

    if not partials:
        print("Every issue was blocked; nothing to summarize.")
        return

    joined = (NL + NL).join("[" + iid + "] " + t + NL + s for iid, t, s in partials)
    note = ""
    if skipped:
        note = (NL + NL + "Note: these issues could not be summarized and are "
                "excluded: " + ", ".join(iid for iid, _, _ in skipped))
    prompt = (
        "Below are summaries of " + str(len(partials)) + " newsletter issues in "
        "chronological order. Using ONLY these, answer the question and cite "
        "issue numbers." + NL + NL + joined + note + NL + NL +
        "Question: " + question)
    out, model = chat_with_fallback(prompt, [REDUCE_MODEL, CHAT_MODEL])
    print(out)
    print(NL + "(reduced with " + model + ")", file=sys.stderr)

    if write:
        acache[akey] = {"answer": out, "models": model,
                        "n": len(partials),
                        "skipped": [i for i, _, _ in skipped]}
        save_json(ANSWER_CACHE, acache)

    if skipped:
        print(NL + "Skipped (blocked by provider filter):")
        for iid, t, _ in skipped:
            print("  - [" + iid + "] " + t)


def show_stats():
    m = load_json(MAP_CACHE)
    a = load_json(ANSWER_CACHE)
    issues = [k for k in m if k.startswith("issue:")]
    quests = [k for k in m if k.startswith("q:")]
    print("map_cache.json   :", len(m), "entries")
    print("  generic (issue):", len(issues), "  <- unique issues summarized generically")
    print("  per-question   :", len(quests))
    print("answer_cache.json:", len(a), "final answers")
    print("prompt version   :", PROMPT_VER)
    ids = sorted(set(k.split(":")[1] for k in issues))
    if ids:
        print("generic issues   :", len(ids), "of 241")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?", default=None)
    ap.add_argument("--full", action="store_true", help="map-reduce over the whole corpus")
    ap.add_argument("--year", type=int, help="map-reduce over one year (needs dates)")
    ap.add_argument("--range", dest="rng", help="issue-number range, e.g. 45-96")
    ap.add_argument("-k", type=int, default=8)
    ap.add_argument("--cache-mode", choices=["issue", "question"], default="issue",
                    help="issue: one generic summary per issue, reused across all "
                         "questions (default); question: tailored per-question summaries")
    ap.add_argument("--no-cache", action="store_true",
                    help="uncached run: ignore both caches and write nothing")
    ap.add_argument("--refresh", action="store_true",
                    help="ignore existing summaries, recompute, and update the cache")
    ap.add_argument("--stats", action="store_true", help="show cache contents and exit")
    a = ap.parse_args()

    if a.stats:
        show_stats()
        raise SystemExit(0)

    if not a.question:
        ap.error("a question is required (unless using --stats)")

    lo = hi = None
    if a.rng:
        parts = a.rng.split("-")
        lo = int(parts[0])
        hi = int(parts[1]) if len(parts) > 1 else lo

    if a.full or a.year or a.rng:
        answer_mapreduce(a.question, a.year, lo, hi,
                         mode=a.cache_mode,
                         use_cache=not a.no_cache,
                         refresh=a.refresh)
    else:
        answer(a.question, a.k)
