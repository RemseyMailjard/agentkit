# Changelog

## 2.4.1
- Added a missing `## Boundary` section to 146 micro-tools that shipped without one.
- Added a missing `## Output` section to `edge-case-finder` and `requirement-extractor`.
- Removed `change-impact-checker`, a duplicate of `impact-estimator` (already used by `plan-change`).
- Wired the 5 remaining orphaned micro-tools into an existing skill:
  `cta-quality-checker` (plan-content-campaign), `decision-summary-builder`
  (analyze-decision), `personal-review-question-builder` (run-weekly-review),
  `semantic-model-boundary-checker` (review-data-quality),
  `training-reuse-scorer` (plan-content-reuse).
- Registered `agentkit-core` in `.agents/plugins/marketplace.json` (it was
  never discoverable before this).
- Rebuilt `evals/agentkit-core/cases.json` as a validator-compliant JSON
  array with `prompt` fields; added baseline routing cases for all 119
  skills (116 auto-generated from each skill's own description, 10 kept
  from the original hand-written set). `scripts/validate_agentkit.py` now
  passes for this plugin.

## 2.4.0
- Added batches 19–24 across .NET, Power Platform, MCP, training business, consulting delivery and person-context workflows.
