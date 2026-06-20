#!/usr/bin/env bash
# Integrity gate entrypoint. Optional arg: path to a commit message file for the provenance check.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$DIR/scripts/gate.py" "$@"
