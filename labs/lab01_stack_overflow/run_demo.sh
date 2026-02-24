#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
"$LAB_DIR/build.sh"

printf "[1/3] Safe input on vulnerable binary\n"
"$LAB_DIR/build/vuln_unprotected" SAFE

printf "[2/3] Oversized input on vulnerable binary (expected overwrite simulation)\n"
set +e
"$LAB_DIR/build/vuln_unprotected" AAAAAAAAAAAAAAAAAAAAAAAA
rc=$?
set -e
printf "Exit code: %s (expected non-zero)\n" "$rc"

printf "[3/3] Oversized input on secure binary (expected rejection)\n"
set +e
"$LAB_DIR/build/secure_fixed" AAAAAAAAAAAAAAAAAAAAAAAA
rc=$?
set -e
printf "Exit code: %s (expected 1)\n" "$rc"
