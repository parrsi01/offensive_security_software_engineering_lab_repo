#!/usr/bin/env bash
set -euo pipefail

echo "Host namespace IDs (current shell):"
readlink /proc/$$/ns/{user,mnt,pid,net} 2>/dev/null || true

echo "Run sandbox_demo.sh or sandbox_hardened.sh and compare the namespace IDs printed inside the sandbox."
