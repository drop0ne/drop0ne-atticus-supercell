# Query Checklist

Status: active
Purpose: provide a minimal live-use checklist for hydrators and operators before answering, before escalating, before claiming mutation authority, and before asserting certainty.

---

## Before answering

Check:
- what is the task class?
- what is the minimum routing level required?
- is there an active receipt relevant to this scope?
- are there drift entries relevant to this question?
- is the answer available from compact state, or is deeper escalation required?

---

## Before escalating

Check:
- did the lower level actually fail to answer the question?
- is the escalation justified by the task, or just curiosity?
- will escalation cross from compact state into doctrine or full-body mirrors unnecessarily?
- is there a relevant stop condition already triggered?

If no real need exists, do not escalate.

---

## Before claiming mutation authority

Check all of the following:
- applicable authority-resolution receipt exists for the scope
- active governance floor permits the requested interpretation
- activation expectations are explicit
- preflight expectations are explicit
- canonical root is not ambiguous for the task scope
- writable-ledger expectations are not missing or contradictory

If any check fails, remain read-only and report `unknown` or `not authorized` as appropriate.

---

## Before asserting certainty

Check:
- is the claim grounded in active baselines, receipts, or mirrored canon?
- does drift materially weaken the claim?
- does unresolved doctrine ambiguity materially weaken the claim?
- are you stating a compact baseline, a doctrine interpretation, or a runtime authorization claim?
- should the answer be labeled `unknown`, `drift-preserved`, or `requires higher-level review` instead of certain?

---

## Output reminder

When relevant, report:
- selected task route
- highest level used
- active receipt applied or `none`
- relevant drift items
- whether behavior remained read-only
- unknowns or blockers
