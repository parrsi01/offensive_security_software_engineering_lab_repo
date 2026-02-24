#!/usr/bin/env bash
set -euo pipefail

echo "[lab03] Misconfigured namespace sandbox demo (training only)"
if ! command -v unshare >/dev/null 2>&1; then
  echo "unshare not installed; install util-linux to run this lab"
  exit 0
fi

echo "Host namespace references:"
readlink /proc/$$/ns/{user,mnt,pid,net} 2>/dev/null || true

echo
if unshare --user --map-root-user --pid --fork bash -lc 'echo "Inside sandbox"; readlink /proc/$$/ns/{user,mnt,pid,net}'; then
  echo "\nMisconfiguration note: this demo does not isolate network namespace or filesystem mounts."
  echo "It shows how partial namespace isolation can create a false sense of containment."
else
  echo "unshare failed on this kernel configuration (common in restricted environments)."
  echo "Review the hardening script and README for the intended configuration."
fi
