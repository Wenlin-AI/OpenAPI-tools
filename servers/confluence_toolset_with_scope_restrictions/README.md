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
