# API Reverse Engineering Reference

Classify operations by user intent:
- lookup/search;
- read detail;
- create/update;
- append/comment;
- execute action;
- destructive operation;
- administrative/privileged operation.

Look for pagination, filtering, idempotency, rate limits, tenant boundaries, asynchronous operations, auth scopes and error contracts.

Do not assume every GET is a tool: stable read-only information can be a resource when that produces a clearer agent surface.
