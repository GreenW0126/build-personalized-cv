# Evidence Store

## Canonical location

Check `.cv-workflow-session/store/manifest.json` before accessing evidence. If it is absent, follow `bootstrap.md`; do not assume the user must supply an existing map.

The store is split into:

- `evidence/experiences.json`: experience metadata.
- `evidence/index.json`: lightweight lookup metadata.
- `evidence/by-experience/*.jsonl`: complete evidence units grouped by experience.
- `market/jd-sources.jsonl`: original JD source metadata and role titles.
- `market/demand-clusters.json`: extracted market patterns.
- `capabilities/capability-mappings.json`: capability-to-evidence mappings.
- `capabilities/capability-package.json`: Capability Package metadata, ownership, consumer contract, and pointers to canonical capability assets.
- `decisions/active/index.json`: lightweight decision lookup metadata.
- `decisions/active/*.jsonl`: current and provisional procedures split into orchestration, dashboard, career-market, and writing-evidence shards.
- `decisions/active-rules.jsonl`: compatibility snapshot only; do not load it during normal work.
- `decisions/history.jsonl`: complete decision history; load only for audit or recalibration.
- `archive/`: read-only migration snapshots.

## Language policy

- Preserve `raw_statement` exactly as supplied by the user.
- Preserve JD and role wording in the source language.
- Use English schema keys and English operational instructions.
- Keep normalized facts in the source language unless a localized claim is explicitly requested.
- Add search tags only when needed; do not translate the whole archive for retrieval convenience.

## Evidence unit rules

Every evidence unit must keep or explicitly mark:

- `evidence_id`
- `experience_id`
- `raw_statement`
- `normalized_fact`
- `information_type`
- `problem`, `action`, `method`, `output`, `impact`, and `judgment` when known
- `ownership`
- `scope`
- `source_type`
- `source_ref`

Unknown values remain unknown. Do not fill gaps with plausible inference.

## Metric rules

- Prefer exact counts when the source supports them.
- When calculating a lower bound, store the inputs and arithmetic.
- Distinguish people, sessions, responses, interview hours, projects, and concepts.
- Use conservative wording such as `220+ hours` only when the lower bound supports it.
- Never convert a rough recollection into a precise number.

## Update procedure

1. Resolve the target experience.
2. Preserve the new raw statement.
3. Create or update the smallest affected evidence units.
4. Deduplicate without deleting source history.
5. Update the index.
6. Report changed IDs, unresolved ambiguity, and any downstream canonical claims that may now be stale.

When evidence changes a capability claim or boundary, mark the affected capability IDs stale for the Capability Synthesizer. Do not let the Evidence Curator rewrite capability blocks directly.

Do not update the dashboard during pure fact collection unless visible content changes.

## Empty-store initialization

For persistent cold start, run `scripts/init-session.py --root <workspace>`. It creates only an empty schema and never imports or fabricates evidence. If a manifest already exists, the script exits without modifying it. After initialization, the Evidence Curator adds the first experiences and evidence units through the normal update procedure.
