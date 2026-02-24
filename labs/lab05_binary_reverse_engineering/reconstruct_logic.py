from __future__ import annotations

from pathlib import Path


def main() -> int:
    lab_dir = Path(__file__).resolve().parent
    dump = lab_dir / "build" / "challenge.objdump.txt"
    if not dump.exists():
        print("Run build_and_disassemble.sh first")
        return 1

    text = dump.read_text(encoding="utf-8", errors="ignore")
    keywords = ["<main>", "<score_input>", "cmp", "jne", "je", "xor"]
    print("Reverse engineering hints from objdump output:")
    for line in text.splitlines():
        if any(k in line for k in keywords):
            print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
