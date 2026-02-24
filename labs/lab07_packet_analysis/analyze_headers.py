from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

LINE_RE = re.compile(r"\bIP\s+([^ ]+)\s+>\s+([^:]+):\s+(.*)$")


def parse_lines(text: str) -> Counter:
    counts: Counter[str] = Counter()
    for line in text.splitlines():
        m = LINE_RE.search(line)
        if not m:
            continue
        payload = m.group(3)
        if payload.startswith("ICMP"):
            counts["ICMP"] += 1
        elif "Flags" in payload:
            counts["TCP"] += 1
        else:
            counts["OTHER"] += 1
    return counts


def main() -> int:
    path = Path(__file__).resolve().parent / "sample_tcpdump.txt"
    counts = parse_lines(path.read_text(encoding="utf-8"))
    print("Parsed protocol counts:")
    for proto, count in sorted(counts.items()):
        print(f"- {proto}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
