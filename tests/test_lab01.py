from __future__ import annotations

import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LAB_DIR = REPO_ROOT / "labs" / "lab01_stack_overflow"


def _run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=True)


def test_lab01_vulnerability_exists_and_secure_rewrite_blocks_it() -> None:
    build = _run(["bash", str(LAB_DIR / "build.sh")], cwd=LAB_DIR)
    assert build.returncode == 0, build.stderr

    oversized = "A" * 24
    vuln = _run([str(LAB_DIR / "build" / "vuln_unprotected"), oversized])
    assert vuln.returncode != 0
    assert "OVERFLOW_SIMULATED" in vuln.stdout
    assert "guard=0x41414141" in vuln.stdout.lower()

    secure = _run([str(LAB_DIR / "build" / "secure_fixed"), oversized])
    assert secure.returncode == 1
    assert "Rejected input" in secure.stderr


def test_lab01_secure_binary_accepts_safe_input() -> None:
    build = _run(["bash", str(LAB_DIR / "build.sh")], cwd=LAB_DIR)
    assert build.returncode == 0, build.stderr

    safe = _run([str(LAB_DIR / "build" / "secure_fixed"), "SAFE"])
    assert safe.returncode == 0
    assert "Secure path completed" in safe.stdout
    assert "guard=0xb16b00b5" in safe.stdout.lower()
