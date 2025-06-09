from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .confluence_client import ConfluenceClient

client = ConfluenceClient()
app = FastAPI(title="Confluence API")


class PageCreate(BaseModel):
    title: str
    content: str


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
    return client.create_page(data.title, data.content)


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
