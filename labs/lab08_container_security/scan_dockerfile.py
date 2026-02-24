from __future__ import annotations

from pathlib import Path

RISKY_PATTERNS = {
    "USER root": "Container runs as root",
    "FLASK_ENV=development": "Development mode enabled",
    "COPY . /app": "Broad copy may include secrets or build artifacts",
}


def scan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings = []
    for token, msg in RISKY_PATTERNS.items():
        if token in text:
            findings.append(f"{path.name}: {msg} ({token})")
    return findings


def main() -> int:
    lab = Path(__file__).resolve().parent
    for name in ["Dockerfile.vulnerable", "Dockerfile.hardened"]:
        path = lab / name
        print(f"Scanning {name}")
        findings = scan(path)
        if findings:
            for finding in findings:
                print(f"- {finding}")
        else:
            print("- No simple rule matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
