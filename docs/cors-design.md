# CORS Design Rationale

Both example servers in this repository expose simple FastAPI apps that are often
called from browser-based tools like Open WebUI. Browsers enforce the
**Same-Origin Policy**, which blocks requests to different domains unless the
server opts in via [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

For convenience during experimentation, each server enables the `CORSMiddleware`
to allow requests from any origin:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

This setup makes it trivial for local UI clients or remote agents to interact
with the APIs without running into CORS errors. You can safely keep the
`allow_origins=["*"]` configuration when running the servers only on
`localhost`, such as during development or testing. **However, it is not meant
for production use.** When deploying these servers publicly, you should restrict
`allow_origins` to the specific domains that are permitted to access the API, or
configure the values via environment variables.

Keeping the CORS configuration wide open is handy for demos and testing but
carries security risks if left unchanged in a cloud environment.
