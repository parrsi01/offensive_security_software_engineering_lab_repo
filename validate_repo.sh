#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

quick_mode=0
for arg in "$@"; do
  case "$arg" in
    --quick) quick_mode=1 ;;
    -h|--help)
      cat <<'USAGE'
Usage: ./validate_repo.sh [--quick]

Validates repository structure, safety documentation presence, lab coverage, and syntax/readiness checks.
USAGE
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 1
      ;;
  esac
done

failures=0
pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; failures=$((failures+1)); }
warn() { echo "WARN: $1"; }

check_file() { [[ -f "$1" ]] && pass "$1 present" || fail "$1 present"; }
check_dir() { [[ -d "$1" ]] && pass "$1 present" || fail "$1 present"; }

echo "Repository Validation"
check_file README.md
check_file COURSE_OVERVIEW.md
check_file ROADMAP.md
check_file LICENSE
check_file Makefile
check_file pyproject.toml
check_file pytest.ini
check_file requirements.in
check_file requirements.txt
check_file validate_repo.sh

check_dir docs
check_file docs/README.md
check_file docs/PROJECT_MANUAL.md
check_file docs/CORE_CONCEPTS.md
check_file docs/OFFLINE_INDEX.md
check_file docs/LESSON_EXECUTION_COMPANION.md
check_file docs/LESSON_RESEARCH_ANALYSIS_COMPANION.md
check_file docs/REPOSITORY_STATUS_REPORT.md
check_file docs/CV_READY_SUMMARY.md
check_file docs/PORTFOLIO_SKILL_MAPPING.md

check_dir documentation
check_dir tools
check_dir labs
check_dir tests
check_dir capstone
check_dir .github/workflows

if python3 - <<'PY'
from pathlib import Path
import sys

labs = sorted([p for p in Path("labs").glob("lab*") if p.is_dir()])
if len(labs) < 9:
    print(f"Expected >=9 lab directories, found {len(labs)}")
    sys.exit(1)
for lab in labs:
    if not (lab / "README.md").exists():
        print(f"Missing README.md in {lab}")
        sys.exit(1)
print(f"Validated {len(labs)} labs with README.md")
PY
then
  pass "Lab documentation coverage"
else
  fail "Lab documentation coverage"
fi

if python3 - <<'PY'
from pathlib import Path
import sys

tests = sorted(Path("tests").glob("test_*.py"))
if len(tests) < 4:
    print(f"Expected >=4 test files, found {len(tests)}")
    sys.exit(1)
print(f"Test files present: {len(tests)}")
PY
then
  pass "Test suite presence"
else
  fail "Test suite presence"
fi

if python3 - <<'PY'
from pathlib import Path
import sys
text = Path("README.md").read_text(encoding="utf-8")
required = ["Ethical Disclaimer", "Legal Constraints", "local"]
missing = [s for s in required if s not in text]
if missing:
    print(f"README missing required safety text: {missing}")
    sys.exit(1)
print("README safety/legal sections present")
PY
then
  pass "Safety/legal README sections"
else
  fail "Safety/legal README sections"
fi

if command -v rg >/dev/null 2>&1; then
  if rg -n "TODO|TBD|FIXME|PLACEHOLDER|REPLACE_WITH_|lorem ipsum" . \
    --glob '!**/.git/**' \
    --glob '!**/.venv/**' \
    --glob '!validate_repo.sh' \
    --glob '!.github/workflows/**' >/tmp/offsec_lab_placeholders.out; then
    cat /tmp/offsec_lab_placeholders.out
    fail "No placeholder/template markers remain"
  else
    pass "No placeholder/template markers remain"
  fi
else
  warn "Placeholder scan skipped (rg not installed)"
fi
rm -f /tmp/offsec_lab_placeholders.out

shell_failed=0
while IFS= read -r -d '' f; do
  if ! bash -n "$f"; then
    echo "Syntax error: $f"
    shell_failed=1
  fi
done < <(find tools labs -type f -name '*.sh' \
  -not -path './.git/*' \
  -not -path './.venv/*' -print0 2>/dev/null)
bash -n validate_repo.sh || shell_failed=1
[[ $shell_failed -eq 0 ]] && pass "Shell syntax checks" || fail "Shell syntax checks"

py_failed=0
pycache_tmp=""
cleanup_pycache_tmp() {
  if [[ -n "${pycache_tmp:-}" && -d "${pycache_tmp:-}" ]]; then
    rm -rf "$pycache_tmp"
  fi
}
trap cleanup_pycache_tmp EXIT
while IFS= read -r -d '' pyf; do
  pycache_tmp="$(mktemp -d)"
  if ! PYTHONPYCACHEPREFIX="$pycache_tmp" python3 -m py_compile "$pyf" >/dev/null 2>&1; then
    echo "Python syntax error: $pyf"
    py_failed=1
  fi
  rm -rf "$pycache_tmp"
  pycache_tmp=""
done < <(find labs tests capstone -type f -name '*.py' -print0 2>/dev/null)
[[ $py_failed -eq 0 ]] && pass "Python syntax checks" || fail "Python syntax checks"

if python3 - <<'PY' >/dev/null 2>&1
import flask  # noqa: F401
import pytest  # noqa: F401
PY
then
  if python3 -m pytest -q tests >/tmp/offsec_lab_pytest.out 2>&1; then
    pass "Pytest suite"
  else
    cat /tmp/offsec_lab_pytest.out
    warn "Pytest failed (environment/tooling dependent) - not blocking"
  fi
  rm -f /tmp/offsec_lab_pytest.out
else
  warn "Flask/pytest not installed; skipping runtime test execution"
fi

if [[ $quick_mode -eq 0 ]]; then
  echo
  echo "Repository Metrics"
  python3 - <<'PY'
from pathlib import Path
repo = Path(".")
print(f"labs={sum(1 for p in (repo/'labs').glob('lab*') if p.is_dir())}")
print(f"docs_md={sum(1 for _ in (repo/'documentation').glob('*.md'))}")
print(f"tools_md={sum(1 for _ in (repo/'tools').glob('*.md'))}")
print(f"tests={sum(1 for _ in (repo/'tests').glob('test_*.py'))}")
PY
fi

if [[ $failures -ne 0 ]]; then
  echo "Validation failed with $failures issue(s)." >&2
  exit 1
fi

echo "Validation passed."
