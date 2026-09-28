# Dashboard Collaboration Surface

## Architectural position

The Dashboard is a first-class collaboration, observability, and navigation layer across the full workflow. It is not an after-the-fact report and not an autonomous reasoning agent.

Its purpose is to let the user see how nonlinear conversation input is being classified, what the system currently believes, what remains unsupported, which agent owns the next transformation, and how those assets affect the CV.

## Canonical projection sources

The Dashboard may project:

- current workflow stage and active target role family;
- market and JD demand signals;
- Capability Package summaries and drill-down links;
- supporting experiences, evidence boundaries, and evidence gaps;
- current CV section text and acceptance status;
- active decision procedures relevant to the visible task;
- agent ownership, current handoff, and unresolved user decisions.

It reads canonical state through a deterministic publisher. It does not independently parse conversation history or reconstruct facts from rendered HTML.

## Interaction boundaries

- Dashboard content is never the factual source of record.
- A factual user correction routes to the Evidence Curator.
- A capability interpretation or boundary correction routes to the Capability Synthesizer.
- A CV wording edit enters claim review and remains a proposal until accepted or explicitly promoted.
- A target, risk, or trade-off change routes to the Master.
- Dashboard UI state, expansion state, and navigation do not alter career data.

If the current Dashboard implementation cannot emit structured edit events, treat user-visible edits as local drafts and require explicit conversational confirmation before canonical promotion.

## Update policy

- Recompile only when visible canonical state changes.
- Pure bookkeeping, indexing, or archive changes do not trigger recompilation.
- Modify one canonical Dashboard source and mechanically synchronize any live view; do not hand-edit multiple copies.
- Do not automatically open, inspect, or visually validate the Dashboard. The user performs visual verification unless they explicitly request an audit.
- Avoid periodic full-page refresh. Poll only a lightweight version signal and refresh after a version change.

## Export handoff

The Dashboard may expose a one-click export control after all included CV sections are accepted. The control emits a structured payload matching `export.md`; it must not pass arbitrary rendered HTML to the document generator.

The export action may offer only lightweight layout choices:

- education placement: automatic, before experience, or after experience;
- independent-project placement: automatic, before experience, after experience, or integrated chronologically;
- output container: DOCX or DOCM.

Automatic routing remains reversible. The visible Dashboard should show the resolved order before download when the user has not explicitly selected an order.

## Design priority

The main view should make the system legible in one glance. Keep primary workflow state, target, capability blocks, market signals, and evidence gaps visible without requiring section-by-section navigation. Use subpages for capability evidence, claim boundaries, and interview-expression detail.
