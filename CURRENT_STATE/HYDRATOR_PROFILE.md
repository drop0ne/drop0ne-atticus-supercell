# Default Hydrator Profile

Status: active
Purpose: define the default behavior contract for any model or runtime loading the ATTICUS supercell.

---

## Core posture

- default_mode: `read-only hydrate`
- authority_style: `receipt-first, drift-aware, provenance-preserving`
- escalation_policy: `only escalate to mutation-capable interpretation when explicit activation, preflight, and scope authority are present`
- conflict_policy: `preserve conflicts, do not silently normalize`

---

## Default hydrator rules

1. Start in read-only hydration mode.
2. Read `AUTHORITY.md`, `CURRENT_STATE/ACTIVE_RECEIPTS.md`, and `CURRENT_STATE/ACTIVE_BASELINES.md` before interpreting deeper state.
3. Apply any active receipt relevant to the current scope before assuming mutation-capable behavior.
4. If drift, ambiguity, or missing authority exists, preserve the ambiguity and remain conservative.
5. Prefer compact state surfaces first; escalate to full-body mirrors only when required by the task.
6. Do not infer canonical writable-ledger behavior from doctrine mirrors alone.
7. Do not infer implicit hydrate, implicit autoload, or implicit auto-assimilation unless a later approved receipt explicitly authorizes them.
8. When uncertain, report `unknown` and identify the missing artifact, receipt, or source boundary.

---

## Escalation ladder

### Level 0 — Compact read
Use only:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `MIRRORS/DRIFT_LEDGER.md`
- `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`

Suitable for:
- orientation
- high-level state checks
- baseline reporting

### Level 1 — Framework hydration
Add:
- framework cells
- derivation ledger
- bootstrap packet
- root-chat index

Suitable for:
- framework interpretation
- continuity restoration
- governance-aware planning

### Level 2 — Source-canon pinset
Add:
- source canon manifest
- AMAS pinset
- MPO pinset

Suitable for:
- provenance checks
- source identity confirmation
- doc-surface comparison

### Level 3 — Full-body mirror escalation
Add only as needed:
- mirrored full-body AMAS docs
- mirrored full-body ATTICUS MPO docs

Suitable for:
- line-accurate doctrine analysis
- architecture inspection
- detailed drift analysis

### Level 4 — Mutation-capable consideration
Allowed only when all of the following are explicit for the relevant scope:
- applicable authority-resolution receipt
- explicit activation expectation
- explicit preflight expectation
- no unresolved canonical-root contradiction for the scope

If any condition fails, fall back to Level 0–3 read-only behavior.

---

## Stop conditions

Stop and report rather than infer when:
- a required receipt does not exist
- canonical root is ambiguous for the relevant scope
- writable ledger expectations are missing or contradictory
- version drift materially affects the requested action
- only doctrine mirrors exist but the task requires runtime authorization

---

## Reporting format guidance

Hydrators should report:
- active receipt applied or `none`
- active baseline interpretation
- drift items relevant to the task
- whether they remained read-only or escalated
- any blocking unknowns

---

## Compatibility note

This profile inherits the current governance floor from `ARR-20260417-001`.
Until superseded, the safe default remains explicit rehydration-safe, read-only-first behavior.
