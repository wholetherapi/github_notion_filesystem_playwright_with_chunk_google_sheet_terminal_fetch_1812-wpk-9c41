#!/usr/bin/env bash
set -euo pipefail

echo "verifying WPK-2405"
python3 src/handler.py --self-check
echo "verification passed"
