# Audit Checklist

Status: active
Purpose: provide a short recurring audit pass for ATTICUS supercell maintainers so the control plane does not silently drift.

---

## When to run

Run this checklist:
- weekly during active maintenance
- after any material governance update
- after any active-receipt change
- after any effective baseline change
- after any material drift-ledger update
- before relying on the repo as a mutation-sensitive governance surface

---

## Audit pass 1 — Current control surfaces

Verify:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md` points to the intended active receipts
- `CURRENT_STATE/ACTIVE_BASELINES.md` matches the intended effective framework/runtime/schema/governance-floor state
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md` still accurately reflects readiness and mutation-capable restrictions
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md` still lists all key control-plane surfaces

Pass condition:
- no stale current-state summary surfaces

---

## Audit pass 2 — Governance consistency

Verify:
- active receipt interpretation matches `ACTIVE_BASELINES.md`
- `RECEIPT_LIFECYCLE.md`, `MAINTENANCE_RULES.md`, and `GOVERNANCE_DEPENDENCY_MAP.md` do not contradict current update practice
- `SUPERCELL_LOAD_ORDER.md` still reflects how receipts and baselines are actually consulted during early boot

Pass condition:
- controlling surfaces, lifecycle rules, and boot behavior agree

---

## Audit pass 3 — Drift preservation

Verify:
- `MIRRORS/DRIFT_LEDGER.md` still preserves known unresolved drift
- any resolved drift was appended as resolution state rather than erased
- examples, status surfaces, and quickstart guidance do not overstate certainty where drift remains

Pass condition:
- drift remains visible and correctly reflected in downstream summary surfaces

---

## Audit pass 4 — Reporting surfaces

Verify:
- `BOOT_ASSERTIONS.md` still matches required control-plane surfaces
- `BOOT_REPORT_TEMPLATE.md` and `COLD_START_BOOT_REPORT_TEMPLATE.md` still match the current boot model
- live boot reports are still valid examples or are clearly historical

Pass condition:
- reporting surfaces are aligned with the current boot/control-plane model

---

## Audit pass 5 — Entry-mode coherence

Verify:
- `QUICKSTART.md` still matches compact orientation behavior
- `OPERATING_MODES.md` still matches actual supported entry modes
- `OPERATING_MODE_EXAMPLES.md` still reflects current governance floor and routing behavior
- `TASK_ROUTING_MATRIX.md` still points tasks to the minimum correct escalation level

Pass condition:
- compact and full entry modes still behave as documented

---

## Audit pass 6 — History and maintenance discipline

Verify:
- `CHANGELOG_CONTROL_PLANE.md` includes material control-plane changes
- dated artifacts remain preserved where history matters
- no history-bearing receipt, drift, or dated-state artifact was silently overwritten
- `UPDATE_PLAYBOOK.md` still matches practical maintenance flow

Pass condition:
- history remains auditable and maintenance guidance remains usable

---

## Audit outcomes

### PASS
Use when:
- all audit passes are satisfactory
- no material stale current-state surface is found

### PARTIAL
Use when:
- minor staleness or navigation/reporting mismatches exist
- governance floor is still clear, but some dependent surfaces need refresh

### FAIL
Use when:
- active receipts, active baselines, load order, or status surfaces materially disagree
- the repo can no longer be trusted as a deterministic control-plane boot surface until repaired

---

## Minimum audit report

Record at minimum:
- date
- auditor
- audit outcome: `PASS | PARTIAL | FAIL`
- surfaces reviewed
- material mismatches found
- repair actions required

---

## Interpretation rule

This checklist is an audit aid.
If an active signed receipt conflicts with a stale example, template, or summary surface found during audit, the signed receipt controls and the stale surface should be repaired.
