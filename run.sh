#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/venv"

if [ ! -d "$VENV" ]; then
  echo "Creating venv and installing dependencies (one-time)..."
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"
fi

cd "$SCRIPT_DIR"
(sleep 2 && open "http://localhost:5002") &
exec "$VENV/bin/python" app.py
