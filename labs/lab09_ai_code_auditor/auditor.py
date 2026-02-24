from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List

from labs.lab09_ai_code_auditor.patterns import PATTERNS

TEXT_SUFFIXES = {".c", ".h", ".cpp", ".py", ".js", ".ts", ".java", ".go", ".rb", ".php", ".sql"}


@dataclass
class Finding:
    file_path: str
    line_number: int
    pattern_id: str
    severity: str
    description: str
    matched_text: str
    secure_rewrite_hint: str


@dataclass
class ScanResult:
    root: str
    file_count: int
    finding_count: int
    findings: List[Finding]


def _iter_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        yield root
        return
    for path in root.rglob("*"):
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name.startswith("Dockerfile")):
            yield path


def _scan_file(path: Path) -> List[Finding]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    findings: List[Finding] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern in PATTERNS:
            if pattern.regex.search(line):
                findings.append(
                    Finding(
                        file_path=str(path),
                        line_number=lineno,
                        pattern_id=pattern.id,
                        severity=pattern.severity,
                        description=pattern.description,
                        matched_text=line.strip()[:160],
                        secure_rewrite_hint=pattern.secure_rewrite_hint,
                    )
                )
    return findings


def scan_path(path: str) -> ScanResult:
    root = Path(path)
    all_files = list(_iter_files(root))
    findings: List[Finding] = []
    for file_path in all_files:
        findings.extend(_scan_file(file_path))
    return ScanResult(root=str(root), file_count=len(all_files), finding_count=len(findings), findings=findings)


def format_text_report(result: ScanResult) -> str:
    lines = [f"Scan root: {result.root}", f"Files scanned: {result.file_count}", f"Findings: {result.finding_count}"]
    for finding in result.findings:
        lines.append(f"- [{finding.severity}] {finding.pattern_id} {finding.file_path}:{finding.line_number}")
        lines.append(f"  Pattern: {finding.description}")
        lines.append(f"  Match: {finding.matched_text}")
        lines.append(f"  Suggestion: {finding.secure_rewrite_hint}")
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Educational AI-assisted code auditor (pattern-based)")
    parser.add_argument("path", help="File or directory to scan")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit JSON report")
    args = parser.parse_args(list(argv) if argv is not None else None)

    result = scan_path(args.path)
    if args.json_output:
        print(json.dumps(asdict(result), indent=2))
    else:
        print(format_text_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
