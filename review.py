import subprocess, sys

YEARS = {
    "2021": "0-5",
    "2022": "6-44",
    "2023": "45-96",
    "2024": "97-148",
    "2025": "149-201",
    "2026": "202-240",
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in YEARS:
        print("usage: uv run review.py <year> [extra query text]")
        print("years:", ", ".join(sorted(YEARS)))
        return
    year = sys.argv[1]
    rng = YEARS[year]
    extra = " ".join(sys.argv[2:]).strip()
    q = (
        "Summarize the year " + year + ": the main events, where I travelled, "
        "the recurring themes, project updates, and book recommendations. "
        "Cite issue numbers."
    )
    if extra:
        q = q + " " + extra
    cmd = ["uv", "run", "query.py", q, "--range", rng]
    print("running:", " ".join(cmd), file=sys.stderr)
    subprocess.run(cmd, check=False)


if __name__ == "__main__":
    main()
