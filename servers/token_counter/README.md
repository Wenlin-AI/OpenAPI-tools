# 🧮 Token Counter Server

A tiny FastAPI service (v0.0.1) that counts tokens in text using [tiktoken](https://github.com/openai/tiktoken).
It understands models such as `gpt-3.5-turbo`, `gpt-4o` and also falls back for
unknown models like `gpt-4.1`.

> **Note**
> The server expects **Python 3.12** when run locally or in Docker.

## 🚀 Quickstart

```bash
git clone <your repo here>
cd OpenAPI-tools/servers/token_counter
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --reload
```

Visit `http://localhost:8000/docs` to try it out.
