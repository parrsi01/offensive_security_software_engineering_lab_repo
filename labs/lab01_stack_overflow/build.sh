#!/usr/bin/env bash
set -euo pipefail

LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SRC_DIR="$LAB_DIR/src"
OUT_DIR="$LAB_DIR/build"
mkdir -p "$OUT_DIR"
COMMON=(-O0 -g -Wall -Wextra)

gcc "${COMMON[@]}" -fno-stack-protector -U_FORTIFY_SOURCE -no-pie -Wl,-z,execstack \
  "$SRC_DIR/vulnerable_stack_overflow.c" -o "$OUT_DIR/vuln_unprotected"

gcc "${COMMON[@]}" -fstack-protector-strong -D_FORTIFY_SOURCE=2 -fPIE -pie \
  -Wl,-z,relro,-z,now -Wl,-z,noexecstack \
  "$SRC_DIR/vulnerable_stack_overflow.c" -o "$OUT_DIR/vuln_protected"

gcc "${COMMON[@]}" -fstack-protector-strong -D_FORTIFY_SOURCE=2 -fPIE -pie \
  -Wl,-z,relro,-z,now -Wl,-z,noexecstack \
  "$SRC_DIR/secure_stack_overflow_fixed.c" -o "$OUT_DIR/secure_fixed"

echo "Built binaries in $OUT_DIR"
