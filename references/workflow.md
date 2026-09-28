# Workflow and Gates

## 0. Entry and bootstrap

Check whether a valid store manifest exists. If it does not, read `bootstrap.md` and select the smallest sufficient mode:

- ephemeral packet for a narrow rewrite or audit;
- persistent session for a full CV, ongoing collaboration, Dashboard, or later reuse;
- import mode when the user already has an Evidence Map or Capability Package.

Do not require the user to call another skill first. Do not initialize persistent files for a one-off micro-edit unless persistence will materially help or the user requests it.

## 1. Context and target

Capture target role families, geography, language, career constraints, and current application goal. Do not force a linear interview; route nonlinear input in the background.

## 2. Evidence accumulation

Send new experience facts to the Evidence Curator. Ask at most one focused question when ambiguity would change ownership, meaning, or a public claim. Otherwise store the ambiguity and continue.

## 3. Market signals

Send JDs and hiring feedback to the JD / Market Analyst. Distinguish contact, interview round, repeated market signal, and one person's opinion. Preserve original role and JD wording.

## 4. Capability and narrative synthesis

Send relevant evidence and market packets to the Capability Synthesizer. Form capability blocks only after evidence supports a repeatable result or compound ability. Link every material claim to evidence IDs, connect it to a repeated market need when available, keep blocks non-overlapping, and state what each block does not prove.

The Capability Package is independently reusable. It may be produced as the endpoint of capability exploration or consumed as an upstream asset for CV writing.

Pre-existing capability blocks are not an entry requirement. For a narrow writing task, a minimal provisional Capability Packet may contain zero blocks plus an explicit target signal, provided every public claim remains supported by the Evidence Packet. For a full CV or career repositioning task, synthesize the smallest stable set of capability blocks before finalizing the narrative.

## 5. Drafting

Retrieve only the relevant evidence, market, and capability packets that exist. Provide the Writer with target signal, locale, line budget, and active rule IDs. Evidence is mandatory for public claims; pre-existing market and capability assets are not. When either is missing, pass an explicit empty/provisional packet and its confidence rather than blocking or inventing. The Writer returns to concrete evidence and must not paste capability-block prose into bullets. Generate a small number of materially different variants.

## 6. Human calibration

The user's edits reveal hiring-market judgment, not merely style preference. Compare the user's version with the agent version, extract the reusable decision rule, and update active rules only when its applicability boundary is clear.

## 7. Acceptance

The user accepts, edits, or rejects the draft. Promote only accepted claims. Batch canonical file writes when practical.

## 8. Dashboard projection

When canonical or accepted visible state changes, mechanically publish the relevant workflow state, capability blocks, evidence gaps, and CV text to the Dashboard. Do not recompile it for invisible bookkeeping changes. Treat user edits as routed review events rather than direct cross-domain writes.

## 9. Final audit

Check evidence support, dates, ownership, metrics, negative signals, terminology, localization consistency, line density, and section order. Do not reopen settled content without a concrete risk.

## 10. Fixed-format export

When the user requests a Word artifact after accepting visible text:

1. Freeze wording for the export batch.
2. Resolve education and independent-project placement using `export.md`.
3. Publish one structured export payload from canonical state; do not scrape rendered Dashboard HTML when a canonical payload exists.
4. Run the deterministic exporter once, render every page, and correct layout defects without rewriting accepted content.
5. Return the Word artifact. A visual preview is QA output, not a second deliverable unless requested.

## Stop conditions

- Stop evidence probing when the claim is supportable and further detail will not change positioning.
- Stop rewriting when the text passes the user's meaning, market, evidence, and layout requirements.
- Do not keep optimizing after the user declares the version final unless a factual or material risk remains.
