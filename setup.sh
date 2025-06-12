#!/usr/bin/env bash
set -e

server=${1:-token_counter}
root_dir="$(cd "$(dirname "$0")" && pwd)"
server_path="$root_dir/servers/$server"

if [ ! -d "$server_path" ]; then
  echo "Server '$server' not found" >&2
  exit 1
fi

cd "$server_path"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

if [ ! -f .env ] && [ -f .env.example ]; then
  cp .env.example .env
fi

echo "Setup complete"
