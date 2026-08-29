---
name: review-security
description: >
  Perform a security-focused review of a .NET application. Use for authentication,
  authorization, secrets, data protection, injection, unsafe deserialization,
  request validation, tenant isolation and sensitive-data exposure.
---

# Security Review .NET

Do not begin by rewriting code. Identify trust boundaries and security-sensitive flows first.

## Review areas

### Identity
- authentication setup;
- token validation;
- cookie/JWT configuration;
- delegated vs application identity.

### Authorization
- endpoint protection;
- policy/role checks;
- resource-level authorization;
- tenant isolation;
- privilege escalation risks.

### Secrets and configuration
- hard-coded credentials;
- connection strings;
- unsafe configuration exposure;
- secret-provider usage.

### Input and injection
- SQL/query injection;
- command/process invocation;
- path traversal;
- SSRF/unsafe URLs;
- unsafe deserialization;
- untrusted HTML/content.

### Data protection
- PII exposure;
- logging of sensitive values;
- encryption concerns;
- over-broad API responses.

### Web concerns
- CORS;
- CSRF where relevant;
- HTTPS/proxy configuration;
- security headers when applicable.

## Severity

- Critical
- High
- Medium
- Low
- Hardening

## Output

Return:

1. threat summary;
2. trust boundaries;
3. prioritized findings with evidence;
4. likely exploit path or failure mode;
5. recommended controls;
6. residual risks;
7. remediation order.

## Cross-plugin boundary

If the repository is specifically an MCP server and the issue concerns MCP tool
design, prompt/tool injection, MCP approval semantics or agent-facing capabilities,
also consider the MCP Builder `secure-mcp-server` skill. Avoid duplicating findings;
use each skill for its own layer.
