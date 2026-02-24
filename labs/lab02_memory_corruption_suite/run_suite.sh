#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
"$LAB_DIR/build_all.sh"

printf "[format string] demonstration\n"
"$LAB_DIR/build/format_string_demo" "%x %x %x"

printf "[integer overflow] demonstration\n"
set +e
"$LAB_DIR/build/integer_overflow_demo" 64
rc=$?
set -e
printf "Exit code: %s\n" "$rc"

printf "[use-after-free simulation] demonstration\n"
"$LAB_DIR/build/use_after_free_simulation"

printf "[secure rewrites] demonstration\n"
"$LAB_DIR/build/secure_rewrites" "hello" 10
