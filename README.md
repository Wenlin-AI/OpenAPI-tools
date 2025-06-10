# OpenAPI-tools
Within this repo I have OpenAPI-tools which you can use as MCP or directly with AI.
It is inspired by [open-webui/openapi-servers](https://github.com/open-webui/openapi-servers).
I'm experimenting with different OpenAPI tools which I either consume directly with AI agents or convert into MCP servers.

Each server lives under `servers/<name>` and exposes a small FastAPI application that can run on its own or be incorporated into your automation pipelines.

## VS Code build task
The `.vscode/tasks.json` file contains a chain of tasks to help you run any server quickly:

1. **Check for Virtual Environment** – ensures a `.venv` directory exists.
2. **Install Requirements** – installs packages from the active server's `requirements.txt`.
3. **Run API in localhost** – starts the API using Uvicorn with the host and port defined in `.vscode/settings.json`.

Because these commands rely on PowerShell, the tasks currently work only on Windows. Linux and macOS users can run the same commands manually or adapt the tasks to their preferred shell.

To try it out, open a `main.py` file inside one of the server folders and press `Ctrl+Shift+B`. Once the build finishes, visit `http://localhost:8282/docs` (or your configured port) to explore the API.

## Servers
- `token_counter` – Simple API that counts tokens using tiktoken
- `confluence_toolset_with_scope_restrictions` – API for reading and writing Confluence Cloud pages
