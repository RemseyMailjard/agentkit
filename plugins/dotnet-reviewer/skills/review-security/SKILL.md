---
name: review-security
description: >
  Use when a user asks for a security-focused .NET review involving identity,
  authorization, secrets, injection, tenant isolation or sensitive data.
---

# Security Review .NET

Review before modifying code and identify trust boundaries first.

Check authentication, authorization, tenant isolation, secrets, configuration,
SQL/command injection, path traversal, SSRF, unsafe deserialization, PII exposure,
logging, over-broad responses, CORS and CSRF where relevant.

Return a threat summary, prioritized evidence-backed findings, likely failure or
exploit paths, recommended controls, residual risks and remediation order.

For MCP-specific tool/agent boundaries, also use MCP Builder security without duplicating findings.
