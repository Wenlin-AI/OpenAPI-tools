# 🧮 Token Counter Server

A tiny FastAPI service (v0.0.1) that counts tokens in text using [tiktoken](https://github.com/openai/tiktoken).
It understands models such as `gpt-3.5-turbo`, `gpt-4o` and also falls back for
unknown models like `gpt-4.1`.

> **Note**
> The server expects **Python 3.12** when run locally or in Docker.

## 🚀 Quickstart

### Manual Setup

```bash
git clone <your repo here>
cd OpenAPI-tools/servers/token_counter
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --reload
```

Visit `http://localhost:8000/docs` to try it out.

### VS Code Tasks (Recommended)

This project includes VS Code tasks for easy setup and execution:

1. Open the project in VS Code
2. Open the `main.py` file (to make it the active file)
3. Press `Ctrl+Shift+B` to run the default build task
4. This will automatically:
   - Check for a virtual environment (`.venv`) and create one if needed
   - Install required dependencies from `requirements.txt`
   - Start the server on port 8282 with hot-reload enabled

The tasks will use the directory of the currently active file, so you can simply open `main.py` and run the tasks directly.

Once running, visit [http://localhost:8282/docs](http://localhost:8282/docs) to access the Swagger UI documentation.

## ⚙️ Configuration

You can customize the server settings in `.vscode/settings.json`:

```json
{
    "local_server": {
        "host": "localhost", // Change to "0.0.0.0" to allow external connections
        "port": 8282         // Change to your preferred port
    }
}
```

## 🔧 How it Works

The VS Code tasks system:

1. **Virtual Environment Check**: The first task checks if a `.venv` directory exists in the same folder as your active file. If not, it creates a new Python virtual environment.

2. **Install Dependencies**: The second task activates the virtual environment and installs the required packages from `requirements.txt` found in the same directory.

3. **Run Server**: The final task starts the FastAPI server using Uvicorn with the settings from `.vscode/settings.json`.

The task chain is executed in sequence, with each task depending on the successful completion of the previous one. All tasks use the directory of your currently active file, which allows you to simply click on `main.py` and press `Ctrl+Shift+B` to run everything.
