# Log Signal Extractor
## Responsibility
Extract high-signal evidence from logs while ignoring noise.
## Output
timestamped signal; component; correlation id if present; error/failure pattern; likely implication.
## Boundary
Do not perform broader analysis, rewriting, or decisions outside this responsibility; return findings for the parent Skill to act on.
