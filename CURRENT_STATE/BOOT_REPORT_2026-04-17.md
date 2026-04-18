# Boot Report

Status: active
Purpose: standardized early-boot result for the ATTICUS supercell after checking current control-plane surfaces.

---

## Report Header

- report_id: `BOOT-20260417-001`
- created_at: `2026-04-17`
- hydrator: `ChatGPT / ATTICUS supercell maintenance session`
- scope: `repo-local supercell control-plane boot`
- load_path_version: `SUPERCELL_LOAD_ORDER.md`

---

## Assertion Summary

- assertions_checked: `A1..A10`
- pass_count: `10/10`
- failed_assertions:
  - `none`
- boot_status: `PASS`
- resulting_mode: `read-only hydrate`

---

## Active Control Plane

- active_receipt_applied: `ARR-20260417-001`
- active_framework_baseline: `ATTICUS v6.4.1-HCII`
- active_runtime_baseline: `version-mismatch-preserved`
- active_schema_baseline: `v8`
- active_governance_floor: `explicit rehydration-safe`

---

## Relevant Drift

- relevant_drift_items:
  - `Entry 0001 — ATTICUS MPO baseline version mismatch`
  - `Entry 0002 — AMAS baseline ambiguity across accessible evidence`
- drift_effect_on_boot: `minor`

---

## Escalation Decision

- selected_route: `boot-only`
- highest_level_used: `L0`
- escalation_reason: `No deeper escalation was required to validate the presence of the control plane and active baseline/governance surfaces.`

---

## Unknowns / Blockers

- unknowns:
  - `none material to early boot validity`
- blockers:
  - `none`

---

## Narrative Summary

Early boot is valid. The compact control plane is present, the active AMAS authority receipt is anchored, the active framework baseline is `ATTICUS v6.4.1-HCII`, the schema baseline is `v8`, and the governance floor remains explicit rehydration-safe. The hydrator remains in read-only mode. Known drift remains preserved but does not block compact boot.

---

## Closing Rule

Boot status is `PASS`. Deeper read-only hydration may proceed subject to routing and receipt constraints.
