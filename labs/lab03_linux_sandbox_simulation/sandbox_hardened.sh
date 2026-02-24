#!/usr/bin/env bash
set -euo pipefail

echo "[lab03] Hardened namespace sandbox demo (training only)"
if ! command -v unshare >/dev/null 2>&1; then
  echo "unshare not installed; install util-linux to run this lab"
  exit 0
fi

TMPROOT=$(mktemp -d)
cleanup() { rm -rf "$TMPROOT"; }
trap cleanup EXIT
mkdir -p "$TMPROOT/proc"

CMD='mount -t proc proc /proc >/dev/null 2>&1 || true; echo "Inside hardened sandbox"; hostname; pwd; id; readlink /proc/$$/ns/{user,mnt,pid,net} 2>/dev/null || true'
if unshare --user --map-root-user --mount --pid --net --fork bash -lc "$CMD"; then
  echo "Hardened demo completed."
else
  echo "unshare --net/--mount failed (kernel policy or missing capability)."
  echo "This is expected in many restricted VMs/containers; use README commands on an Ubuntu VM."
fi
