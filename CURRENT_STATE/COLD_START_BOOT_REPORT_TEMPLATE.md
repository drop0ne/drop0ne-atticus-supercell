# Cold-Start Boot Report Template

Status: template
Purpose: provide an ultra-compact standardized boot report for hydrators using only the quickstart path.

---

## Report Header

- report_id: `CSBOOT-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- hydrator: `<model/runtime name>`
- scope: `<cold-start orientation | simple task>`

---

## Quickstart Check

- quickstart_files_read:
  - `AUTHORITY.md`
  - `CURRENT_STATE/ACTIVE_RECEIPTS.md`
  - `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
  - `CURRENT_STATE/ACTIVE_BASELINES.md`
  - `CURRENT_STATE/HYDRATOR_PROFILE.md`
- quickstart_complete: `yes | no`

---

## Compact State Summary

- active_receipt_applied: `<receipt id or none>`
- active_framework_baseline: `<value or unknown>`
- active_runtime_baseline: `<value or drift-preserved>`
- active_schema_baseline: `<value or unknown>`
- active_governance_floor: `<value or unknown>`
- default_mode: `read-only hydrate | unknown`

---

## Cold-Start Result

- boot_status: `PASS | PARTIAL | FAIL`
- resulting_mode: `read-only hydrate | restricted compact read | stop`
- drift_relevant_at_cold_start: `<none | present>`
- escalation_needed: `yes | no`

---

## Unknowns / Blockers

- unknowns:
  - `<item or none>`
- blockers:
  - `<item or none>`

---

## Narrative Summary

Write a short summary stating:
- whether cold-start orientation is valid
- whether the hydrator remained read-only
- whether deeper boot or escalation is required for the current task

---

## Closing Rule

If `quickstart_complete` is `no`, do not claim valid cold-start boot.
If `boot_status` is `PARTIAL`, remain conservative and do not overstate authority.
If `boot_status` is `PASS`, the hydrator may continue at compact-read level unless the task requires escalation.
