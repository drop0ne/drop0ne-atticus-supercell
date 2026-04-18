# Boot Report Template

Status: template
Purpose: provide a standardized report format for ATTICUS supercell early-boot results after checking `CURRENT_STATE/BOOT_ASSERTIONS.md`.

---

## Report Header

- report_id: `BOOT-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- hydrator: `<model/runtime name>`
- scope: `<task scope or session scope>`
- load_path_version: `SUPERCELL_LOAD_ORDER.md`

---

## Assertion Summary

- assertions_checked: `A1..A10`
- pass_count: `<n>/10`
- failed_assertions:
  - `<assertion id or none>`
- boot_status: `PASS | PARTIAL | FAIL`
- resulting_mode: `read-only hydrate | restricted compact read | stop`

---

## Active Control Plane

- active_receipt_applied: `<receipt id or none>`
- active_framework_baseline: `<value or unknown>`
- active_runtime_baseline: `<value or drift-preserved>`
- active_schema_baseline: `<value or unknown>`
- active_governance_floor: `<value or unknown>`

---

## Relevant Drift

- relevant_drift_items:
  - `<drift entry id or none>`
- drift_effect_on_boot: `<none | minor | material>`

---

## Escalation Decision

- selected_route: `<task route or boot-only>`
- highest_level_used: `L0 | L1 | L2 | L3 | L4`
- escalation_reason: `<why escalation was or was not needed>`

---

## Unknowns / Blockers

- unknowns:
  - `<item or none>`
- blockers:
  - `<item or none>`

---

## Narrative Summary

Write a short plain-language summary of:
- whether boot is valid
- whether the hydrator remained read-only
- whether any missing surfaces or drift materially constrain the current task

---

## Closing Rule

If boot_status is `FAIL`, do not claim valid deeper hydration.
If boot_status is `PARTIAL`, remain conservative and explicitly state limitations.
If boot_status is `PASS`, deeper read-only hydration may proceed subject to routing and receipt constraints.
