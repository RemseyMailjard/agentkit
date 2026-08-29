# MCP Security Checklist

Verify identity propagation and authorization at the real backend boundary, not only at the MCP layer.

Check write/destructive capabilities for confirmation, scope and idempotency where relevant. Treat model-provided URLs, filenames, commands, SQL and remote content as untrusted input.

Review tenant isolation, secret storage, logging redaction, outbound network access, dependency trust and over-broad service credentials.

When fixes are implemented, add regression tests for the affected security boundary.
