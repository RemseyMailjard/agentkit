---
name: review-dotnet
description: >
  Use when a user asks for a broad .NET repository review covering correctness,
  maintainability, testability, reliability or idiomatic C#/.NET usage.
---

# Review .NET Repository

Review before modifying code unless remediation is explicitly requested.

Check correctness, nullability, async/concurrency, DI/configuration, error handling,
logging, maintainability, boundaries, tests, dependencies and obvious performance risks.

Workflow:
1. Inspect solution structure and application type.
2. Review high-risk paths first.
3. Record evidence-backed findings.
4. Classify Critical, High, Medium, Low or Improvement.
5. Separate defects from style suggestions.
6. Recommend the smallest useful remediation.

Use `review-aspnet-api`, `review-ef-core` or `review-security` for those focused requests.
