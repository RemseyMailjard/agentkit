"""Intentionally flawed MCP-style server fixture."""

API_TOKEN = "hard-coded-demo-token"

def customer_get(customer_id, tenant_id=None):
    # No authorization or tenant validation.
    return {"id": customer_id, "tenant": tenant_id}

def append_customer_note(customer_id, text):
    # Write capability has no validation, authorization, audit or idempotency.
    return {"customer_id": customer_id, "text": text, "status": "saved"}

def get_url(url):
    # Intentionally accepts arbitrary outbound URLs.
    import urllib.request
    return urllib.request.urlopen(url).read().decode()
