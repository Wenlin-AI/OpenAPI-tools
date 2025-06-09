import os
from typing import Any, Dict, List, Optional

import requests
from fastapi import HTTPException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ConfluenceClient:
    """Simple client for interacting with Confluence Cloud."""

    def __init__(self) -> None:
        self.url = os.environ.get("CONFLUENCE_URL")
        self.username = os.environ.get("CONFLUENCE_USERNAME")
        self.token = os.environ.get("CONFLUENCE_TOKEN")
        self.space_key = os.environ.get("CONFLUENCE_SPACE_KEY")
        self.parent_page = os.environ.get("CONFLUENCE_PARENT_PAGE", None)
        if not all([self.url, self.username, self.token]):
            raise RuntimeError(
                "CONFLUENCE_URL, CONFLUENCE_USERNAME and CONFLUENCE_TOKEN must be set"
            )
        # Make sure url is not None before checking endswith
        if self.url and not self.url.endswith('/'):
            self.url += '/'
        self.session = requests.Session()
        # Ensure username and token are not None before setting auth
        assert self.username is not None and self.token is not None, "Username and token must not be None"
        self.session.auth = (self.username, self.token)
        self.session.headers.update({"Content-Type": "application/json"})

    def _make_request(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        method: str = "GET",
        json: Any = None,
    ) -> Dict[str, Any]:
        url = endpoint if endpoint.startswith("http") else f"{self.url}{endpoint}"
        response = self.session.request(method, url, params=params, json=json)
        if not response.ok:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

    def _make_direct_request(self, url: str) -> Dict[str, Any]:
        response = self.session.get(url)
        if not response.ok:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

    def search(
        self,
        cql_query: str,
        batch_size: int = 25,
        limit: int = 100,
        cursor: Optional[str] = None,
        expand: Optional[List[str]] = None,
        cql_context: Optional[str] = None,
        excerpt: Optional[str] = None,
        include_archived_spaces: bool = False,
        exclude_current_spaces: bool = False,
    ) -> Dict[str, Any]:
        """Search Confluence using CQL with cursor-based pagination."""
        endpoint = f"{self.url}rest/api/search"
        params = {
            "cql": cql_query,
            "limit": min(batch_size, limit),
        }
        if cursor:
            params["cursor"] = cursor
        if cql_context:
            params["cqlcontext"] = cql_context
        if expand:
            params["expand"] = ",".join(expand)
        if excerpt:
            params["excerpt"] = excerpt
        if include_archived_spaces:
            params["includeArchivedSpaces"] = "true"
        if exclude_current_spaces:
            params["excludeCurrentSpaces"] = "true"

        response = self._make_request(endpoint, params)
        result = response.copy()
        all_results = response.get("results", [])
        results_count = len(all_results)

        while (
            "_links" in response
            and "next" in response["_links"]
            and results_count < limit
        ):
            next_link = response["_links"]["next"]
            if next_link.startswith("/"):
                base_url = self.url.rstrip("/") if self.url else ""
                next_url = f"{base_url}{next_link}"
            else:
                next_url = next_link
            response = self._make_direct_request(next_url)
            new_results = response.get("results", [])
            all_results.extend(new_results)
            results_count = len(all_results)

        result["results"] = all_results[:limit]
        result["size"] = len(result["results"])
        return result

    def get_page(self, page_id: str) -> Dict[str, Any]:
        endpoint = f"rest/api/content/{page_id}"
        return self._make_request(endpoint, params={"expand": "body.storage,version"})

    def list_pages(self) -> List[Dict[str, Any]]:
        cql = f"space={self.space_key} and type=page"
        if self.parent_page:
            cql += f" and ancestor={self.parent_page}"
        print(cql)
        data = self.search(cql, limit=1000)
        return data.get("results", [])

    def create_page(self, title: str, content: str) -> Dict[str, Any]:
        if not self.space_key:
            raise HTTPException(status_code=500, detail="CONFLUENCE_SPACE_KEY not set")
        parent_id = self.parent_page
        if parent_id:
            cql = f"id={parent_id}"
            self.search(cql, limit=1)
        data = {
            "type": "page",
            "title": title,
            "space": {"key": self.space_key},
            "body": {"storage": {"value": content, "representation": "storage"}},
        }
        if parent_id:
            data["ancestors"] = [{"id": parent_id}]
        return self._make_request("rest/api/content", method="POST", json=data)

    def update_page(self, page_id: str, title: Optional[str], content: Optional[str]) -> Dict[str, Any]:
        page = self.get_page(page_id)
        version = page.get("version", {}).get("number", 1)
        new_version = version + 1
        data = {
            "id": page_id,
            "type": "page",
            "title": title or page["title"],
            "version": {"number": new_version},
            "body": {
                "storage": {
                    "value": content or page["body"]["storage"]["value"],
                    "representation": "storage",
                }
            },
        }
        return self._make_request(f"rest/api/content/{page_id}", method="PUT", json=data)

    def delete_page(self, page_id: str) -> None:
        self._make_request(f"rest/api/content/{page_id}", method="DELETE")
