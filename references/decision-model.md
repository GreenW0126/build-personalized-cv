# Decision Model

The purpose of the decision model is to externalize a repeatable judgment procedure, not to preserve preference labels or copy the user's historical risk tolerance.

## Decision layers

1. **Decision episodes** record the situation, constraints, options, trade-off, and observed outcome.
2. **Decision procedures** generalize reusable reasoning from supported episodes.
3. **Calibration history** records when a procedure is narrowed, expanded, superseded, or invalidated.

## Invocation order

1. Identify the current goal, hard constraints, reversibility, and affected audience.
2. Separate facts, market signals, interpretations, assumptions, and missing information.
3. Retrieve procedures whose applicability boundaries match the situation. Do not match on labels alone.
4. Compare viable options using the procedure's evidence priorities and trade-off rule.
5. Select authority: execute, recommend, or return the decision to the user.
6. State the provisional conclusion, basis, confidence, missing context, and what new evidence would change it.
7. When outcomes arrive, append an episode and decide whether the procedure needs recalibration.

## Authority levels

- **Execute:** low-risk, reversible, internal organization or retrieval inside a validated boundary.
- **Recommend:** multiple reasonable trade-offs exist, but the user can cheaply revise the result.
- **Return to user:** value conflict, risk tolerance, irreversible or external action, career-direction change, key factual gap, conflicting procedures, or out-of-bound context.

## Minimum procedure fields

`procedure_id`, `status`, `version`, `goal`, `applies_when`, `required_context`, `evidence_priority`, `tradeoff_rule`, `default_action`, `return_to_user_when`, `counterexamples`, `supporting_decisions`, and `supersedes`.

## Core constraints

- Stable reasoning may produce different choices under different constraints.
- Use conservative defaults only for low-risk reversible work.
- A procedure becomes active only after repeated episodes or real-world feedback support it.
- Keep only the minimum reasoning needed for a future agent to reproduce the judgment.

