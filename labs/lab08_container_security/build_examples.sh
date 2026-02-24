#!/usr/bin/env bash
set -euo pipefail
LAB_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

echo "Build vulnerable image: docker build -f $LAB_DIR/Dockerfile.vulnerable -t ose-lab:vuln $LAB_DIR"
echo "Build hardened image:  docker build -f $LAB_DIR/Dockerfile.hardened -t ose-lab:hard $LAB_DIR"
echo "Run scanner:           python3 $LAB_DIR/scan_dockerfile.py"
