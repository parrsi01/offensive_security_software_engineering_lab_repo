#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
OUT_DIR="$LAB_DIR/build"
mkdir -p "$OUT_DIR"

gcc -O0 -g -Wall -Wextra "$LAB_DIR/challenge.c" -o "$OUT_DIR/challenge"
objdump -d -M intel "$OUT_DIR/challenge" > "$OUT_DIR/challenge.objdump.txt"

echo "Built $OUT_DIR/challenge"
echo "Disassembly written to $OUT_DIR/challenge.objdump.txt"
