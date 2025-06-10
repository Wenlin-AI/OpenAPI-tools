# 📝 Confluence Toolset with Scope Restrictions

A simple FastAPI server to interact with Confluence Cloud pages.

## Environment Variables
- `CONFLUENCE_URL` – Base URL of your Confluence Cloud instance (e.g. `https://your-site.atlassian.net/`)
- `CONFLUENCE_USERNAME` – Username or email used for authentication
- `CONFLUENCE_TOKEN` – API token for authentication
- `CONFLUENCE_SPACE_KEY` – Space key where new pages are created
- `CONFLUENCE_PARENT_PAGE` – *(optional)* Parent page ID limiting write operations
  
  When this variable is set, all write operations (create, update and delete) are allowed only on pages that are descendants of the configured parent page.

## Quickstart
```bash
cd OpenAPI-tools/servers/confluence_toolset_with_scope_restrictions
pip install -r requirements.txt
uvicorn main:app --reload
```
Then visit [http://localhost:8000/docs](http://localhost:8000/docs).

### Creating Pages

The `/pages` endpoint accepts an optional `parent_id` field allowing you to specify under which Confluence page the new page should be created. When scope restrictions are enabled, the provided `parent_id` must be a descendant of `CONFLUENCE_PARENT_PAGE`.

### Fetching Inline Comments

Use `/pages/{page_id}/inline-comments` to list inline comments on a page. Include
the `body_format` query parameter to retrieve the comment body, e.g.

```bash
GET /pages/12345/inline-comments?body_format=storage
```

### Replying to Inline Comments

Send a reply using `/inline-comments/{comment_id}/reply`.
Provide the reply text using the `body` query parameter.

```bash
curl -X POST "http://localhost:8282/inline-comments/123/reply?body=Thanks" \
  -H "accept: application/json"
```

### Footer Comments

Fetch footer comments for a page with `/pages/{page_id}/footer-comments`. Submit
a new footer comment using the same path with `POST`.
