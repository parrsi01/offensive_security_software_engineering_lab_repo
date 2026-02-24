#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SRC_DIR="$LAB_DIR/src"
OUT_DIR="$LAB_DIR/build"
mkdir -p "$OUT_DIR"
COMMON=(-O0 -g -Wall -Wextra)

gcc "${COMMON[@]}" -Wno-format-security "$SRC_DIR/format_string_demo.c" -o "$OUT_DIR/format_string_demo"
gcc "${COMMON[@]}" "$SRC_DIR/integer_overflow_demo.c" -o "$OUT_DIR/integer_overflow_demo"
gcc "${COMMON[@]}" "$SRC_DIR/use_after_free_simulation.c" -o "$OUT_DIR/use_after_free_simulation"
gcc "${COMMON[@]}" "$SRC_DIR/secure_rewrites.c" -o "$OUT_DIR/secure_rewrites"

echo "Built memory corruption suite in $OUT_DIR"
