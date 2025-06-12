#!/usr/bin/env bash
set -e

repo_url="https://github.com/Wenlin-AI/OpenAPI-tools"
repo_dir=${1:-OpenAPI-tools}
server=${2:-token_counter}

if [ ! -d "$repo_dir/.git" ]; then
  git clone "$repo_url" "$repo_dir"
else
  git -C "$repo_dir" pull
fi

cd "$repo_dir"
./setup.sh "$server"
