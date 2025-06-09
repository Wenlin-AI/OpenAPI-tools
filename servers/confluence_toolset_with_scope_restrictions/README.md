# 📝 Confluence Toolset with Scope Restrictions

A simple FastAPI server to interact with Confluence Cloud pages.

## Environment Variables
- `CONFLUENCE_URL` – Base URL of your Confluence Cloud instance (e.g. `https://your-site.atlassian.net/`)
- `CONFLUENCE_USERNAME` – Username or email used for authentication
- `CONFLUENCE_TOKEN` – API token for authentication
- `CONFLUENCE_SPACE_KEY` – Space key where new pages are created
- `CONFLUENCE_PARENT_PAGE` – *(optional)* Parent page ID limiting write operations

## Quickstart
```bash
cd OpenAPI-tools/servers/confluence_toolset_with_scope_restrictions
pip install -r requirements.txt
uvicorn main:app --reload
```
Then visit [http://localhost:8000/docs](http://localhost:8000/docs).
