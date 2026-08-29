---
name: review-ef-core
description: >
  Use when a user asks to review Entity Framework Core data access, including
  DbContext lifetime, query efficiency, tracking, migrations or concurrency.
---

# Review Entity Framework Core

Review the data-access layer unless broader review is requested.

Check DbContext lifetime, parallel use, cancellation, N+1, projections, tracking,
pagination, relationships, keys, indexes, transactions, SaveChanges, concurrency
and migration safety.

Return:
1. data-access summary;
2. correctness findings;
3. performance findings;
4. migration risks;
5. recommended changes;
6. tests or benchmarks to add.

Use the general .NET reviewer when the root cause is outside EF Core.
