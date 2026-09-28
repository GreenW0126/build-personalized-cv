# Five-Role MVP Architecture

## 1. Master Agent

Owns user dialogue, current intent, constraints, routing, trade-offs, and canonical acceptance. It normally reads only the manifest, current state, active rules, and specialist packets.

The Master may inspect source references when packets conflict, confidence is low, or a consequential claim is at stake. It must not delegate the user's final agency.

At entry, the Master detects whether canonical assets exist and selects ephemeral, persistent, or import bootstrap mode. It must not treat missing files as missing user ability or require another skill to run first. If delegation is unavailable, the Master may execute the five role contracts sequentially while preserving their writer boundaries.

## 2. Evidence Curator

The sole writer for the evidence store. It preserves verbatim source statements, normalizes facts without changing meaning, links evidence to experiences, maintains conservative metrics, and reports ambiguity or missing support.

It does not write CV prose, choose career strategy, or inflate business impact.

In cold start, it may create the first experience records and evidence units directly from raw resumes or user narratives. It must keep raw text, mark unresolved fields, and return a usable Evidence Packet before the full archive is complete.

## 3. JD / Market Analyst

The sole writer for structured JD and market-signal records. It preserves original JD wording, extracts demand clusters, distinguishes repeated signals from one-off opinions, and identifies hiring needs and risks.

It does not edit evidence or draft CV copy.

## 4. Capability Synthesizer

The sole writer for the Capability Package and capability-to-evidence mappings. It determines whether evidence supports a repeatable result or compound ability, connects capabilities to market demand, keeps blocks distinct, and records safe claims and claim boundaries.

It does not write CV bullets. Capability blocks are reusable career assets and must remain more stable than any one CV version.

In cold start, it may emit a minimal provisional packet or zero blocks when the available evidence does not yet support a stable capability. A missing Capability Package is a construction task, not a prerequisite failure.

## 5. CV Writer + Claim Auditor

Consumes bounded evidence, market, and capability packets plus active rules, language, and line budget. It returns to the underlying evidence rather than copying capability-block prose. It produces one to three draft options, identifies trade-offs, and audits ownership, metrics, dates, unsupported claims, negative framing, terminology, and density.

It writes proposals only. The Master promotes accepted text to canonical artifacts.

It may accept explicit empty or provisional market/capability packets in cold start. It must never accept an empty Evidence Packet for a factual public claim.

## Single-writer matrix

| Data domain | Writer | Other roles |
|---|---|---|
| Evidence shards and evidence index | Evidence Curator | Read/query only |
| JD sources and market signals | JD / Market Analyst | Read/query only |
| Capability Package, capability mappings, and user-facing capability blocks | Capability Synthesizer | Read/query only |
| Active decisions and acceptance status | Master | Suggest only |
| Draft variants | CV Writer + Claim Auditor | Read/comment only |
| Canonical CV | Master after user acceptance | No direct edits |
| Dashboard projection | Mechanical Dashboard Publisher | Derived read-only projection of canonical state; user edits enter controlled review events |

## Dashboard projection layer

The Dashboard is a first-class collaboration and observability surface, not a sixth reasoning agent. It allows the user to see how nonlinear input changes the shared model while continuing the conversation.

It projects current workflow state, target role family, market signals, capability blocks, evidence links and gaps, current CV claims, and agent ownership from canonical files. It must not create facts, infer capabilities, resolve trade-offs, or become a parallel source of truth.

The Dashboard Publisher performs deterministic rendering only. The Master decides when a visible state change warrants recompilation. User edits made through editable Dashboard fields are interaction events: CV wording enters claim review, factual corrections route to the Evidence Curator, and capability corrections route to the Capability Synthesizer. No edit may silently overwrite another canonical domain.

## Runtime rules

- Give specialists a task packet, exact file paths, and IDs; never the full thread by default.
- Use one specialist turn per bounded task. A specialist is a re-instantiated role, not a permanent memory service.
- Do not allow specialists to spawn further agents in the MVP.
- Parallelize only independent retrieval or analysis. Capability synthesis waits for evidence and relevant market packets; CV writing waits for evidence, market, and capability packets.
- Use structured handoffs instead of vague summaries such as "what happened?"

## Handoff contracts

### Evidence request

```json
{
  "task_id": "string",
  "experience_ids": ["EXP-..."],
  "claim_goal": "string",
  "requested_fields": ["method", "ownership", "metric", "outcome"],
  "max_units": 5
}
```

### Evidence packet

```json
{
  "task_id": "string",
  "verified_evidence": [
    {
      "evidence_id": "E-...",
      "fact": "source-language fact",
      "ownership": "string or null",
      "metric": "string or null",
      "boundary": "string or null",
      "source_ref": "string"
    }
  ],
  "unresolved": [],
  "contradictions": [],
  "confidence": "high|medium|low"
}
```

### Market packet

```json
{
  "role_cluster": "string",
  "top_needs": [],
  "hiring_risks": [],
  "keywords_original": [],
  "company_stage_problem": "string or null",
  "source_ids": []
}
```

### Capability request

```json
{
  "task_id": "string",
  "target_role_family": "string or null",
  "evidence_packet": {},
  "market_packet": {},
  "affected_capability_ids": [],
  "max_blocks": 4
}
```

### Capability packet

```json
{
  "task_id": "string",
  "capabilities": [
    {
      "capability_id": "CB-...",
      "title": "source-language label",
      "core_claim": "string",
      "evidence_ids": [],
      "market_demand_refs": [],
      "safe_claims": [],
      "claim_boundaries": []
    }
  ],
  "evidence_gaps": [],
  "stale_capability_ids": [],
  "confidence": "high|medium|low"
}
```

### Writing request

```json
{
  "target_signal": "string",
  "evidence_packet": {},
  "market_packet": {},
  "capability_packet": {},
  "active_rule_ids": [],
  "locale": "zh-CN|en",
  "line_budget": "2-3 Word lines"
}
```

### Writing and audit response

```json
{
  "variants": [{"text": "string", "used_evidence_ids": [], "tradeoff": "string"}],
  "audit_status": "pass|revise",
  "issues": [],
  "unsupported_claims": [],
  "recommended_variant": 0
}
```
