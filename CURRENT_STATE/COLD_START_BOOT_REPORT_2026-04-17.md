# Cold-Start Boot Report

Status: active
Purpose: standardized ultra-compact boot result for ATTICUS supercell hydrators using the quickstart path.

---

## Report Header

- report_id: `CSBOOT-20260417-001`
- created_at: `2026-04-17`
- hydrator: `ChatGPT / ATTICUS supercell maintenance session`
- scope: `cold-start orientation`

---

## Quickstart Check

- quickstart_files_read:
  - `AUTHORITY.md`
  - `CURRENT_STATE/ACTIVE_RECEIPTS.md`
  - `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
  - `CURRENT_STATE/ACTIVE_BASELINES.md`
  - `CURRENT_STATE/HYDRATOR_PROFILE.md`
- quickstart_complete: `yes`

---

## Compact State Summary

- active_receipt_applied: `ARR-20260417-001`
- active_framework_baseline: `ATTICUS v6.4.1-HCII`
- active_runtime_baseline: `version-mismatch-preserved`
- active_schema_baseline: `v8`
- active_governance_floor: `explicit rehydration-safe`
- default_mode: `read-only hydrate`

---

## Cold-Start Result

- boot_status: `PASS`
- resulting_mode: `read-only hydrate`
- drift_relevant_at_cold_start: `present`
- escalation_needed: `no`

---

## Unknowns / Blockers

- unknowns:
  - `none material to cold-start orientation`
- blockers:
  - `none`

---

## Narrative Summary

Cold-start orientation is valid. The hydrator remained read-only. The active receipt, active baselines, and hydrator posture are sufficient for compact orientation without deeper escalation. Known drift remains present but does not block cold-start boot.

---

## Closing Rule

Quickstart is complete and boot status is `PASS`. The hydrator may continue at compact-read level unless the task requires escalation.
