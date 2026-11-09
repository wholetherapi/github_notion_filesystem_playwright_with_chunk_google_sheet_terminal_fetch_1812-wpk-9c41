#!/usr/bin/env bash
set -euo pipefail

echo "verifying WPK-2204"
python3 src/handler.py --self-check
echo "verification passed"
