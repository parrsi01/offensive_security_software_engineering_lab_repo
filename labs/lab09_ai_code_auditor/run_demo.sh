#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
export PYTHONPATH="$REPO_ROOT${PYTHONPATH:+:$PYTHONPATH}"
python3 "$REPO_ROOT/labs/lab09_ai_code_auditor/auditor.py" "$REPO_ROOT/labs/lab09_ai_code_auditor/sample_targets"
