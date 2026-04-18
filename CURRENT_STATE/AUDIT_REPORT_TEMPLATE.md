# Audit Report Template

Status: template
Purpose: provide a standardized report format for ATTICUS supercell audits run from `CURRENT_STATE/AUDIT_CHECKLIST.md`.

---

## Report Header

- report_id: `AUDIT-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- auditor: `<name or runtime>`
- audit_scope: `<weekly | post-governance-update | post-receipt-change | other>`

---

## Audit Outcome

- outcome: `PASS | PARTIAL | FAIL`
- confidence: `high | medium | low`
- resulting_posture: `unchanged | conservative until repaired | stop relying on control plane until repaired`

---

## Surfaces Reviewed

- reviewed_surfaces:
  - `CURRENT_STATE/ACTIVE_RECEIPTS.md`
  - `CURRENT_STATE/ACTIVE_BASELINES.md`
  - `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
  - `SUPERCELL_LOAD_ORDER.md`
  - `MIRRORS/DRIFT_LEDGER.md`
  - `<additional surfaces as needed>`

---

## Audit Pass Results

### Pass 1 — Current control surfaces
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 2 — Governance consistency
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 3 — Drift preservation
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 4 — Reporting surfaces
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 5 — Entry-mode coherence
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 6 — History and maintenance discipline
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

---

## Material Mismatches Found

- mismatches:
  - `<item or none>`

---

## Repair Actions Required

- required_actions:
  - `<action or none>`
- priority: `low | medium | high | critical`

---

## Practical Summary

Write a short plain-language summary stating:
- whether the control plane is still trustworthy for compact use
- whether it is still trustworthy for full control-plane boot
- whether any surfaces became stale or contradictory
- whether immediate repair is required

---

## Closing Rule

If outcome is `FAIL`, do not treat the repo as a fully reliable deterministic control-plane surface until the listed repairs are made.
If outcome is `PARTIAL`, remain conservative and update stale current-state surfaces before relying on them for governance-sensitive work.
If outcome is `PASS`, continue using the current control plane subject to normal drift-preservation and receipt rules.
