# OpenAPI-tools
Within this repo I have OpenAPI-tools which you can use as MCP or directly with AI.
It is inspired by [open-webui/openapi-servers](https://github.com/open-webui/openapi-servers).
I'm experimenting with different OpenAPI tools which I either consume directly with AI agents or convert into MCP servers.

Each server lives under `servers/<name>` and exposes a small FastAPI application that can run on its own or be incorporated into your automation pipelines.

## Installation

To fetch the repository and set up a server in one step you can use the `install` scripts. They clone the repo from GitHub if needed or pull the latest changes before running the `setup` script.

### Windows

```powershell
PS> .\install.ps1 [path] [server_name]
```

### Linux/WSL

```bash
$ ./install.sh [path] [server_name]
```

`path` is the directory where the repository will be cloned (defaults to `OpenAPI-tools`). `server_name` defaults to `token_counter`.

## VS Code build task
The `.vscode/tasks.json` file contains a chain of tasks to help you run any server quickly:

1. **Check for Virtual Environment** – ensures a `.venv` directory exists.
2. **Install Requirements** – installs packages from the active server's `requirements.txt`.
3. **Run API in localhost** – starts the API using Uvicorn with the host and port defined in `.vscode/settings.json`.

Because these commands rely on PowerShell, the tasks currently work only on Windows. Linux and macOS users can run the same commands manually or adapt the tasks to their preferred shell.

To try it out, open a `main.py` file inside one of the server folders and press `Ctrl+Shift+B`. Once the build finishes, visit `http://localhost:8282/docs` (or your configured port) to explore the API.

## Helper scripts

If you don't want to rely on the VS Code tasks, the repository also provides cross-platform setup and run scripts. Each script accepts an optional server name (defaults to `token_counter`).

### Windows

```powershell
PS> .\setup.ps1 [server_name]
PS> .\run.ps1 [server_name]
```

### Linux/WSL

```bash
$ ./setup.sh [server_name]
$ ./run.sh [server_name]
```

`setup` creates the virtual environment, installs the `requirements.txt` packages and copies `.env.example` to `.env` if needed. `run` activates the environment and starts the API using the host and port from `.vscode/settings.json` (falling back to `localhost:8000`).

## Servers
- `token_counter` – Simple API that counts tokens using tiktoken
- `confluence_toolset_with_scope_restrictions` – API for reading and writing Confluence Cloud pages

## Design Notes

See [docs/cors-design.md](docs/cors-design.md) for background on why CORS is
enabled on the example servers and how to tighten it for production deployments.
