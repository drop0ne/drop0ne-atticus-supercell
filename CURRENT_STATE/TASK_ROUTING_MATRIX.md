# Task Routing Matrix

Status: active
Purpose: help hydrators choose the minimum required escalation level for common ATTICUS supercell tasks.

---

## Routing rules

- Start at the lowest level that can answer the task.
- Escalate only when the current level cannot answer with sufficient certainty.
- If a task touches mutation, export, or runtime authority, check active receipts first.
- If drift or ambiguity materially affects the task, report it instead of collapsing it.

---

## Escalation levels

- `L0` = compact read
- `L1` = framework hydration
- `L2` = source-canon pinset
- `L3` = full-body mirrors
- `L4` = mutation-capable consideration

Reference source: `CURRENT_STATE/HYDRATOR_PROFILE.md`

---

## Common task routes

### 1. Orientation / what is this repo?
- minimum_level: `L0`
- read:
  - `AUTHORITY.md`
  - `CURRENT_STATE/ACTIVE_RECEIPTS.md`
  - `CURRENT_STATE/ACTIVE_BASELINES.md`
  - `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
- stop_if:
  - repo identity and active baseline are clear

### 2. What framework version is active?
- minimum_level: `L0`
- read:
  - `CURRENT_STATE/ACTIVE_BASELINES.md`
  - `MIRRORS/DRIFT_LEDGER.md`
- escalate_if:
  - task requires source justification for version continuity

### 3. What governance floor controls behavior?
- minimum_level: `L0`
- read:
  - `CURRENT_STATE/ACTIVE_RECEIPTS.md`
  - `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
  - `CURRENT_STATE/HYDRATOR_PROFILE.md`
- escalate_if:
  - task requires doctrine-line justification

### 4. Restore ATTICUS framework continuity
- minimum_level: `L1`
- read:
  - framework state snapshot
  - derivation ledger
  - framework cells
  - bootstrap packet
  - root-chat index
- escalate_if:
  - provenance or source-repo identity must be confirmed

### 5. Compare doctrine lines / analyze AMAS ambiguity
- minimum_level: `L3`
- read:
  - drift ledger
  - authority receipt
  - AMAS full-body mirrors
  - derivation ledger
- stop_if:
  - doctrinal differences are identified and reported with preserved ambiguity

### 6. Compare runtime/product docs for drift
- minimum_level: `L3`
- read:
  - drift ledger
  - ATTICUS MPO full-body mirrors
  - pinset summaries
- stop_if:
  - mismatches are enumerated with source paths

### 7. Determine whether mutation-capable behavior is authorized
- minimum_level: `L0`
- read:
  - active receipts
  - hydrator profile
  - load order mutation-capable gate
- escalate_to: `L4` only if task actually needs mutation-capable interpretation
- stop_if:
  - authority, activation, or preflight remains unclear

### 8. Export or append question
- minimum_level: `L1`
- read:
  - active receipts
  - hydrator profile
  - current framework state
  - load order
- escalate_if:
  - AMAS runtime-binding details are required
- likely_target_level: `L3`

### 9. Source provenance audit
- minimum_level: `L2`
- read:
  - source canon manifest
  - pinsets
  - derivation ledger
- escalate_if:
  - exact doctrinal language or exact runtime doc language is needed

### 10. Root-chat provenance / what original sessions informed this?
- minimum_level: `L1`
- read:
  - root-chat index
  - derivation ledger
  - framework state snapshot
- stop_if:
  - reachable roots and explicit gaps are enumerated

---

## Hard stops

Do not escalate to `L4` unless all are explicit for the relevant scope:
- applicable authority-resolution receipt
- explicit activation expectation
- explicit preflight expectation
- no unresolved canonical-root contradiction for the task scope

If any of these are missing, remain in `L0`–`L3` read-only mode.

---

## Reporting output

For routed tasks, hydrators should report:
- selected route
- highest level used
- active receipt applied or `none`
- drift items relevant to the task
- unknowns / stop conditions encountered
