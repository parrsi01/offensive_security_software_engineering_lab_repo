from __future__ import annotations

from pathlib import Path

from labs.lab09_ai_code_auditor.auditor import format_text_report, scan_path


def test_ai_auditor_flags_insecure_patterns(tmp_path: Path) -> None:
    sample = tmp_path / "demo.c"
    sample.write_text(
        "#include <string.h>\n"
        "void f(char *a, char *b){ strcpy(a,b); }\n",
        encoding="utf-8",
    )

    py_sample = tmp_path / "runner.py"
    py_sample.write_text(
        "import subprocess\n"
        "subprocess.run(cmd, shell=True)\n",
        encoding="utf-8",
    )

    result = scan_path(str(tmp_path))
    ids = {finding.pattern_id for finding in result.findings}

    assert "c_strcpy" in ids
    assert "py_shell_true" in ids
    assert result.finding_count >= 2

    text_report = format_text_report(result)
    assert "Suggestion:" in text_report
    assert "shell=False" in text_report or "shell=False" in str([f.secure_rewrite_hint for f in result.findings])
