# MCP Tool Design Reference

A model should be able to infer:
- when to use the capability;
- when not to use it;
- what each parameter means;
- whether it writes or causes side effects;
- what success and failure look like.

Prefer task-oriented names such as `customer.search`, `customer.get` and `customer.notes.append` over direct HTTP endpoint mirroring.

Keep backend-specific concerns behind an adapter when practical. Test valid, invalid, missing, empty, backend-failure and authorization paths.
