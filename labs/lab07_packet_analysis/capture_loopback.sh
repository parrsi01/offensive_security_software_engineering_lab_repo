#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
OUT_FILE="$LAB_DIR/loopback_capture.pcap"

if ! command -v tcpdump >/dev/null 2>&1; then
  echo "tcpdump not installed. Review sample_tcpdump.txt and README offline."
  exit 0
fi
if ! command -v timeout >/dev/null 2>&1; then
  echo "timeout command not found; install coreutils."
  exit 0
fi
if ! command -v ping >/dev/null 2>&1; then
  echo "ping not found; install iputils-ping or use another local traffic generator."
  exit 0
fi

rm -f "$OUT_FILE"
( timeout 4 tcpdump -i lo -nn -w "$OUT_FILE" icmp >/dev/null 2>&1 ) &
TCPDUMP_PID=$!
sleep 1
ping -c 1 127.0.0.1 >/dev/null 2>&1 || true
wait "$TCPDUMP_PID" || true

echo "Capture saved to $OUT_FILE"
