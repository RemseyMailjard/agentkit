# MCP Test Matrix

Recommended layers:
- unit tests for domain logic and validation;
- adapter tests for backend translation;
- protocol/capability tests for MCP behavior;
- end-to-end tests where environment access allows.

For writes, test duplicate/retry behavior and verify side effects. For auth, distinguish unauthenticated from unauthorized. For external dependencies, test timeout, rate limit, malformed response and backend error mapping.

Include routing checks when multiple tools could plausibly satisfy the same prompt.
