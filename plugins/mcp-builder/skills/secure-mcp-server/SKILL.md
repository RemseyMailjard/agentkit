---
name: secure-mcp-server
description: >
  Use when the user asks for an MCP-specific security review, threat analysis or
  hardening of tools, resources, authentication, authorization or sensitive operations.
---

# Secure MCP Server

Review trust boundaries before proposing fixes.

Focus on:
- authentication and authorization;
- secrets and credential handling;
- destructive or privileged actions;
- untrusted input and prompt/tool injection;
- data exposure and tenant isolation;
- SSRF and unsafe URLs;
- logs/privacy;
- supply-chain risk and least privilege.

Classify findings Critical/High/Medium/Low/Hardening. Implement fixes only when requested.

Read [references/security-checklist.md](references/security-checklist.md) for detailed checks.
