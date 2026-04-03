import copy
import re
import httpx
from fastmcp import FastMCP

API_BASE = "http://localhost:5294"

METHOD_SUFFIXES = {
    "get": "",
    "head": "_exists",
    "post": "_create",
    "put": "_update",
    "patch": "_patch",
    "delete": "_delete",
}

# Shorten verbose path segments to keep names under FastMCP's 56-char limit
PATH_ABBREVIATIONS = {
    "operator-payouts": "op-payouts",
}


def path_to_tool_name(path: str, method: str) -> str:
    """Generate a concise tool name from the URL path and HTTP method.

    Examples:
        GET  /api/v1/machines             -> machines
        GET  /api/v1/machines/{id}        -> machines_by_id
        POST /api/v1/machines             -> machines_create
        PUT  /api/v1/machines/{id}        -> machines_by_id_update
        DELETE /api/v1/machines/{id}      -> machines_by_id_delete
        GET  /api/v1/machines/{id}/meters -> machines_by_id_meters
    """
    # Apply path abbreviations before name generation
    for long, short in PATH_ABBREVIATIONS.items():
        path = path.replace(long, short)
    # Strip /api/v1 (or /api/v2 etc.) prefix
    cleaned = re.sub(r"^/api/v\d+/", "", path)
    # Replace path params {param} with "by_param"
    cleaned = re.sub(r"\{(\w+)\}", r"by_\1", cleaned)
    # Replace hyphens and slashes with underscores
    cleaned = cleaned.replace("-", "_").replace("/", "_")
    # Remove leading/trailing underscores
    cleaned = cleaned.strip("_")
    # Append method suffix
    suffix = METHOD_SUFFIXES.get(method.lower(), f"_{method.lower()}")
    return cleaned + suffix


def resolve_request_body_refs(spec: dict) -> dict:
    """Inline $ref-ed request body schemas so FastMCP preserves their 'required' array.

    FastMCP.from_openapi resolves $ref properties but drops the 'required' array
    when the request body schema is a top-level $ref to a component schema.
    Inlining the schema directly ensures the required fields are enforced.
    """
    schemas = spec.get("components", {}).get("schemas", {})
    for path_item in spec.get("paths", {}).values():
        for method in ("post", "put", "patch"):
            operation = path_item.get(method)
            if not operation:
                continue
            content = (
                operation.get("requestBody", {})
                .get("content", {})
                .get("application/json", {})
            )
            schema = content.get("schema", {})
            ref = schema.get("$ref", "")
            if ref.startswith("#/components/schemas/"):
                schema_name = ref.split("/")[-1]
                if schema_name in schemas:
                    content["schema"] = copy.deepcopy(schemas[schema_name])
            # FastMCP only promotes body schema required[] when requestBody.required is true.
            # Only set it when the requestBody actually has content; empty-body action
            # endpoints (e.g. /open, /close) have no content and must be left alone.
            if operation.get("requestBody", {}).get("content"):
                operation["requestBody"]["required"] = True
    return spec


def set_operation_ids(spec: dict) -> dict:
    """Rewrite all operationId values in the spec to be URL-based."""
    seen: dict[str, int] = {}
    for path, path_item in spec.get("paths", {}).items():
        for method in ("get", "head", "post", "put", "patch", "delete"):
            if method not in path_item:
                continue
            name = path_to_tool_name(path, method)
            # Deduplicate if two paths produce the same name
            if name in seen:
                seen[name] += 1
                name = f"{name}_{seen[name]}"
            else:
                seen[name] = 0
            path_item[method]["operationId"] = name
    return spec


class BearerTokenAuth(httpx.Auth):
    """Fetches a dev token on first use and re-fetches it whenever a 401 is received."""

    def __init__(self, token_url: str) -> None:
        self.token_url = token_url
        self.token: str | None = None

    async def _fetch_token(self) -> str:
        async with httpx.AsyncClient() as c:
            r = await c.post(self.token_url)
            r.raise_for_status()
            return r.json()["token"]

    async def async_auth_flow(self, request: httpx.Request):
        if self.token is None:
            self.token = await self._fetch_token()
        request.headers["Authorization"] = f"Bearer {self.token}"
        response = yield request
        if response.status_code == 401:
            self.token = await self._fetch_token()
            request.headers["Authorization"] = f"Bearer {self.token}"
            yield request


# Create authenticated client (token is fetched lazily and refreshed on 401)
auth = BearerTokenAuth(f"{API_BASE}/api/v1/dev/auth/token/full-access")
client = httpx.AsyncClient(base_url=API_BASE, auth=auth)

# Load spec and rewrite operationIds to URL-based names
spec = httpx.get(f"{API_BASE}/swagger/v1/swagger.json").json()
set_operation_ids(spec)
resolve_request_body_refs(spec)

mcp = FastMCP.from_openapi(openapi_spec=spec, client=client, name="MA API")

if __name__ == "__main__":
    mcp.run()
