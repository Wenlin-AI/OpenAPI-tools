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

source .venv/bin/activate

host="localhost"
port=8000
settings="$root_dir/.vscode/settings.json"
if [ -f "$settings" ]; then
  host=$(python3 -c "import json,sys;d=json.load(open('$settings'));print(d.get('local_server',{}).get('host','localhost'))")
  port=$(python3 -c "import json,sys;d=json.load(open('$settings'));print(d.get('local_server',{}).get('port',8000))")
fi

exec uvicorn main:app --host "$host" --port "$port"
