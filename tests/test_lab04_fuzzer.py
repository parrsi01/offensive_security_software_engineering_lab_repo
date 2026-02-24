from __future__ import annotations

import json
from pathlib import Path

from labs.lab04_simple_fuzzer_engine.fuzzer import run_fuzz_session


def test_fuzzer_detects_crash_and_writes_reports(tmp_path: Path) -> None:
    summary = run_fuzz_session(
        target_name="crash_on_magic",
        iterations=5,
        out_dir=str(tmp_path),
        seed_corpus=[b"CRASHME", b"A"],
        random_seed=1,
    )

    assert summary.crashes >= 1
    assert summary.crash_files, "expected crash reproducer files"
    for crash_file in summary.crash_files:
        data = json.loads(Path(crash_file).read_text(encoding="utf-8"))
        assert data["exception_type"] in {"RuntimeError", "ValueError"}

    summary_report = tmp_path / "reports" / "summary.json"
    assert summary_report.exists()
    report_data = json.loads(summary_report.read_text(encoding="utf-8"))
    assert report_data["crashes"] >= 1
