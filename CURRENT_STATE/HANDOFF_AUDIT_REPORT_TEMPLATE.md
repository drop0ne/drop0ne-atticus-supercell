# Handoff Audit Report Template

Status: template
Purpose: provide a standardized report format for ATTICUS supercell handoff audits run from `CURRENT_STATE/HANDOFF_AUDIT_CHECKLIST.md`.

---

## Report Header

- report_id: `HANDOFF-AUDIT-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- auditor: `<name or runtime>`
- audit_scope: `<post-handoff-change | post-governance-change | periodic | other>`

---

## Audit Outcome

- outcome: `PASS | PARTIAL | FAIL`
- confidence: `high | medium | low`
- resulting_posture: `unchanged | conservative until repaired | do not rely on handoff layer until repaired`

---

## Handoff Surfaces Reviewed

- reviewed_surfaces:
  - `CURRENT_STATE/CONTROL_PLANE_PACKET.md`
  - `CURRENT_STATE/QUICKSTART.md`
  - `CURRENT_STATE/HANDOFF_MODES.md`
  - `CURRENT_STATE/HANDOFF_EXAMPLES.md`
  - `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
  - `CURRENT_STATE/HANDOFF_PACKET_TEMPLATE.md`
  - `<additional surfaces as needed>`

---

## Audit Pass Results

### Pass 1 — Packet alignment
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 2 — Quickstart alignment
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 3 — Handoff mode coherence
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 4 — Handoff examples coherence
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 5 — Index and navigation coherence
- result: `PASS | PARTIAL | FAIL`
- notes:
  - `<notes>`

### Pass 6 — Template and regeneration readiness
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
- whether packet-first direct handoff remains trustworthy
- whether compact cold-start handoff remains trustworthy
- whether full control-plane handoff remains clearly separated from compact handoff paths
- whether any handoff surfaces became stale or contradictory
- whether immediate repair is required

---

## Closing Rule

If outcome is `FAIL`, do not rely on the handoff layer for clean model-to-model or runtime-to-runtime handoff until listed repairs are made.
If outcome is `PARTIAL`, remain conservative and refresh stale handoff surfaces before relying on them for important handoff scenarios.
If outcome is `PASS`, continue using the handoff layer subject to normal receipt, baseline, drift, and deterministic boot rules.
