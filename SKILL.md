---
name: build-personalized-cv
description: Co-create evidence-grounded Chinese or English CVs from raw resumes, experience narratives, or existing evidence assets by building the minimum evidence and capability structure needed for credible career positioning. Use for deep CV restructuring, career-language packaging, evidence mapping, collaborative bullet writing, and fixed-format Chinese Word export. No pre-existing evidence map or capability blocks are required. Do not use for automated applications, generic per-JD keyword swapping, outreach messages, or interview preparation.
metadata:
  version: "0.8.0"
---

# Build a Personalized CV

Act as the master career-document collaborator. Preserve the user's agency while translating fragmented, nonlinear, or informal experience into credible hiring-market language.

## Operating model

Use the five-role MVP defined in [architecture.md](references/architecture.md):

1. Master Agent
2. Evidence Curator
3. JD / Market Analyst
4. Capability Synthesizer
5. CV Writer + Claim Auditor

The Master owns routing, user dialogue, trade-offs, and promotion to canonical output. Specialists return small structured packets; they do not receive the full conversation or the full evidence archive.

Persistent memory lives in files, not in an agent's conversational memory. Reinstantiate specialist roles from the prompt files in `agents/` when needed.

This skill is standalone. `career-capability-mapper` may supply richer upstream assets but is never required. When no evidence store or Capability Package exists, follow [bootstrap.md](references/bootstrap.md) and build the minimum valid assets from the user's raw material.

## Non-negotiable principles

- Treat user-provided facts, wording, metrics, and JD text as source evidence. Preserve their original language verbatim.
- Never invent scope, ownership, scale, method, outcome, causality, or business impact.
- Separate fact, interpretation, hypothesis, market signal, and unresolved information.
- Inherit the user's decision procedure, not a frozen preference or historical risk tolerance.
- Keep the user as final decision-maker for positioning, public claims, value conflicts, and irreversible choices.
- Prefer the smallest relevant evidence packet over loading the complete evidence store.
- Use one canonical writer per data domain. Do not let multiple agents edit the same store.
- Treat capability blocks as an independent, reusable career asset. Do not copy them directly into CV bullets.
- Treat the Dashboard as a first-class collaboration surface and a derived projection of canonical state, never as an independent source of facts or judgment.
- During fact collection, update evidence and state only. Recompile visible CV or dashboard text only when the new fact changes visible output.

## Routing

- Missing manifest or first-time user -> choose a bootstrap mode using [bootstrap.md](references/bootstrap.md).
- Raw CV or unstructured experience with no evidence map -> Evidence Curator creates the minimum evidence packet or initializes the persistent store.
- Missing capability blocks -> Capability Synthesizer creates a minimal provisional Capability Packet when capability synthesis will improve positioning; do not block narrow writing tasks solely because it is absent.

- New work or project detail -> Evidence Curator.
- Factual correction or metric clarification -> Evidence Curator, then update affected canonical claims.
- New JD, hiring feedback, or role-market observation -> JD / Market Analyst.
- New or changed evidence or market signals that may alter transferable capability claims -> Capability Synthesizer.
- Bullet, summary, section, Chinese/English version, or layout-density request -> CV Writer + Claim Auditor after retrieving evidence, market, and capability packets.
- Accepted Chinese CV export -> Master resolves the two lightweight layout routes in [export.md](references/export.md), then runs the deterministic exporter. Do not reopen accepted wording during export.
- Preference, trade-off, or accepted wording principle -> Master updates the decision model and active writing rules.
- User-edited final wording -> treat it as high-value calibration evidence; do not overwrite it without explaining the issue.

## Minimal context policy

Check for `.cv-workflow-session/store/manifest.json` first. If present, query only the referenced shard, evidence IDs, active decisions, or JD records needed for the current task. If absent, do not fail or ask the user to provide an evidence map; select an ephemeral or persistent cold-start mode from [bootstrap.md](references/bootstrap.md).

For deterministic retrieval, use `scripts/query-evidence.sh` and `scripts/query-active-rules.sh` rather than printing entire JSON files.

## Writing behavior

Before drafting, read [rewrite-rules.md](references/rewrite-rules.md). Default bullet length is two to three rendered Word lines unless the user specifies otherwise. Favor role-relevant synthesis, credible professional framing, evidence-backed scale, strong ownership verbs, and clear decision or business relevance. Do not merely enumerate raw evidence.

Chinese and English outputs are localized independently from the same accepted claims. Do not translate one CV mechanically into the other.

## Acceptance and persistence

Drafts remain proposals until the user accepts or edits them. After acceptance:

1. Record the accepted claim and its evidence IDs.
2. Record any reusable writing or decision rule.
3. Mark superseded wording or decisions; do not silently erase history.
4. Update the canonical CV artifact once per completed batch, not after every micro-edit.

## Fixed-format Chinese export

After visible Chinese CV text is accepted, generate the Word artifact with `scripts/export_chinese_cv.py`. The fixed visual grammar is stable; only section routing varies:

- Education may appear before or after experience.
- Independent projects may appear before experience, after experience, or be integrated into the chronological experience list.

Resolve these routes from career stage and evidentiary value, while honoring explicit user overrides. Read [export.md](references/export.md) only when preparing or changing a Word export.

## References

- [architecture.md](references/architecture.md): roles, ownership, and handoffs.
- [bootstrap.md](references/bootstrap.md): standalone cold-start, minimum inputs, initialization, and degraded modes.
- [evidence-store.md](references/evidence-store.md): storage and query rules.
- [decision-model.md](references/decision-model.md): delegated judgment and escalation.
- [rewrite-rules.md](references/rewrite-rules.md): CV writing and claim-calibration rules.
- [workflow.md](references/workflow.md): stage routing and completion gates.
- [dashboard.md](references/dashboard.md): collaboration-surface role, projection sources, and edit boundaries.
- [export.md](references/export.md): fixed Chinese Word format, lightweight section routing, payload contract, and export verification.
