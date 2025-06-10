from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from confluence_client import ConfluenceClient

client = ConfluenceClient()
app = FastAPI(title="Confluence API")


class PageCreate(BaseModel):
    title: str
    content: str
    parent_id: Optional[str] = Field(None, description="Parent page ID")


class PageUpdate(BaseModel):
    title: Optional[str] = Field(None, description="New title")
    content: Optional[str] = Field(None, description="New content in storage format")


@app.get("/pages", summary="List pages")
def list_pages():
    return client.list_pages()


@app.get("/pages/{page_id}", summary="Read page")
def read_page(page_id: str):
    return client.get_page(page_id)


@app.post("/pages", summary="Create page")
def create_page(data: PageCreate):
    return client.create_page(data.title, data.content, data.parent_id)


@app.put("/pages/{page_id}", summary="Update page")
def update_page(page_id: str, data: PageUpdate):
    return client.update_page(page_id, data.title, data.content)


@app.delete("/pages/{page_id}", summary="Delete page")
def remove_page(page_id: str):
    client.delete_page(page_id)
    return {"status": "deleted"}


@app.get("/search", summary="Search pages")
def search(cql: str, limit: int = 100):
    return client.search(cql_query=cql, limit=limit)


@app.get(
    "/pages/{page_id}/inline-comments",
    summary="List inline comments for a page",
)
def list_inline_comments(page_id: str, body_format: str = "storage"):
    return client.get_inline_comments(page_id, body_format=body_format)
