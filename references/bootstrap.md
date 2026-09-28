# Standalone Cold Start

Read this reference when the workspace has no valid `.cv-workflow-session/store/manifest.json`, when the user supplies only a raw CV or narrative, or when capability assets are missing.

## Independence contract

`build-personalized-cv` must complete without `career-capability-mapper`, a pre-existing Evidence Map, capability blocks, JDs, or a Dashboard. Those assets may improve depth or reuse but are never prerequisites.

The skill builds only the minimum upstream structure required by the user's requested scope. Missing files are a bootstrap condition, not an error.

## Choose one mode

### Ephemeral packet

Use for one bullet, one section, a claim audit, or another narrow one-off task.

- Preserve the supplied text as the source reference.
- Build an in-memory Evidence Packet containing only the facts needed for the requested claim.
- Use an explicit empty or provisional Market Packet and Capability Packet when they are not needed.
- Do not create a persistent session merely to satisfy architecture.
- Persist only if the user requests continuity or the task expands into a full CV.

### Persistent session

Use for a full CV, career repositioning, repeated collaboration, Dashboard use, multiple versions, or future reuse.

1. Run `scripts/init-session.py --root <workspace>`.
2. Ingest the user's raw CV and narratives into experience records and evidence units.
3. Establish a provisional target role family from the user's stated goal. JDs may be added later.
4. Synthesize the smallest defensible Capability Package. Zero stable blocks is acceptable early; record gaps instead of inventing.
5. Draft, calibrate, accept, publish, and export through the normal workflow.

### Import

Use when the user already has an Evidence Map, Capability Package, or compatible career asset.

- Preserve the source unchanged.
- Map it into the current schema without claiming unsupported equivalence.
- Import evidence before derived capability claims.
- Mark ambiguous or unmapped fields for review; do not discard them.

## Minimum input

Do not demand a complete intake form. Start when the user supplies:

- at least one factual experience source: raw CV, project description, work narrative, or portfolio excerpt;
- a requested scope: bullet, section, full CV, or exploratory restructuring;
- a language or inferable output language.

A target role family materially improves positioning but may remain provisional. Ask one focused question only when its absence would produce a materially different public claim. Otherwise continue and display the uncertainty.

## Minimum gates

### Narrow task

Drafting may begin when:

- the requested claim has traceable factual support;
- ownership and metrics are either known or explicitly omitted;
- target signal is stated or provisionally inferred;
- missing market/capability context is declared.

### Full CV

Final acceptance requires:

- every public claim mapped to evidence;
- experiences and dates reconciled or visibly marked unresolved;
- a target role family or explicit general-purpose positioning;
- capability synthesis attempted, with stable blocks or recorded evidence gaps;
- section order, language, density, and claim boundaries audited.

## Promotion from ephemeral to persistent

When a narrow task grows into repeated or full-CV work:

1. initialize the session safely;
2. preserve the original ephemeral source references;
3. assign persistent IDs without changing claim meaning;
4. record accepted wording and relevant decision rules;
5. continue without asking the user to repeat already supplied facts.

## Failure and recovery

- Existing valid manifest: do not initialize; use it.
- Session directory exists without a manifest: stop before writing and inspect. Do not overwrite unknown files.
- Partially imported assets: use verified evidence, mark derived assets stale, and continue from the smallest safe reconstruction point.
- No factual source at all: ask for one experience source; do not generate a generic CV as if it were personalized.
