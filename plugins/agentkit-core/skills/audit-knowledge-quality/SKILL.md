---
name: audit-knowledge-quality
description: >
  Use when a knowledge base, memory set or project context should be reviewed for staleness, duplication, unsupported claims and weak provenance.
---
# Audit Knowledge Quality
Compose:
staleness-detector → knowledge-deduplicator → fact-opinion-separator → provenance-tagger → research-gap-finder.

Return quality risks, stale items, duplicates, unsupported claims and remediation priority.
