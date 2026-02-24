#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
PYTHON_ONLY=0
NO_PIP=0
USE_VENV=1

for arg in "$@"; do
  case "$arg" in
    --python-only) PYTHON_ONLY=1 ;;
    --no-pip) NO_PIP=1 ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Usage: $0 [--python-only] [--no-pip]" >&2
      exit 2
      ;;
  esac
done

log() { printf "[install] %s\n" "$*"; }

log "Date: $(date +%Y-%m-%d)"
log "Repository: $ROOT_DIR"

if [[ $PYTHON_ONLY -eq 0 ]]; then
  if command -v apt-get >/dev/null 2>&1; then
    log "Suggested Ubuntu packages (run with sudo if needed):"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install -y build-essential gdb binutils tcpdump docker.io python3-venv"
  else
    log "apt-get not found; skipping OS package guidance"
  fi
fi

if [[ $NO_PIP -eq 0 ]]; then
  if command -v python3 >/dev/null 2>&1; then
    if [[ $USE_VENV -eq 1 ]]; then
      if [[ ! -x "$ROOT_DIR/.venv/bin/python" ]]; then
        log "Creating local virtual environment at $ROOT_DIR/.venv"
        python3 -m venv "$ROOT_DIR/.venv"
      fi
      log "Installing Python dependencies into local virtual environment"
      "$ROOT_DIR/.venv/bin/pip" install -r "$ROOT_DIR/requirements.txt"
      log "Activate with: source $ROOT_DIR/.venv/bin/activate"
    else
      log "Installing Python dependencies from requirements.txt (user scope)"
      python3 -m pip install --user -r "$ROOT_DIR/requirements.txt"
    fi
  else
    log "python3 not found; cannot install Python dependencies"
    exit 1
  fi
fi

if [[ -x "$ROOT_DIR/.venv/bin/pytest" ]]; then
  log "Done. Verify with: $ROOT_DIR/.venv/bin/pytest -q $ROOT_DIR/tests"
else
  log "Done. Verify with: pytest -q $ROOT_DIR/tests"
fi
