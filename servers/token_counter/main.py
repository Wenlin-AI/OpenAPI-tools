from fastapi import FastAPI
from pydantic import BaseModel, Field
import tiktoken

app = FastAPI(
    title="Token Counter API",
    version="0.0.1",
    description="Simple API to count tokens for a given text"
)

class TokenCountInput(BaseModel):
    text: str = Field(..., description="Text to tokenize")
    model: str = Field(
        "gpt-3.5-turbo",
        description="Model name for tokenization (determines encoding)",
    )

@app.post("/count_tokens", summary="Count tokens in text")
def count_tokens(data: TokenCountInput):
    """Return the number of tokens for the given text and model."""
    try:
        # tiktoken supports gpt-3.5-turbo and gpt-4o directly
        encoding = tiktoken.encoding_for_model(data.model)
    except Exception:
        # gpt-4.1 or unknown models fallback to cl100k_base or o200k_base
        fallback_map = {
            "gpt-4o": "o200k_base",
            "gpt-4.1": "o200k_base",
        }
        encoding = tiktoken.get_encoding(fallback_map.get(data.model, "cl100k_base"))
    num_tokens = len(encoding.encode(data.text))
    return {"tokens": num_tokens}

@app.get("/health", summary="Health check")
def health():
    return {"status": "ok"}
