# Active Governing Receipts

Status: active
Purpose: provide one minimal pointer surface to the currently governing authority-resolution receipts for ATTICUS supercell hydration and runtime interpretation.

---

## Active receipts

### 1. AMAS / supercell runtime behavior
- receipt_id: `ARR-20260417-001`
- path: `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
- scope: `framework | supercell | session-bootstrap`
- status: `approved`
- governing effect:
  - preserve AMAS `2.0-draft` as doctrine mirror
  - preserve AMAS v1.2 + runtime-binding as historical/governance evidence
  - govern supercell runtime behavior using the explicit rehydration-safe floor
  - block implicit hydrate, implicit autoload, and implicit auto-assimilation
  - require explicit activation and preflight before append/repair/export semantics are treated as authoritative

---

## Load rule

Hydrators should read this file during early boot.
If a receipt listed here applies to the current scope, apply it before mutation-capable interpretation.
If no applicable receipt exists, fall back to `SUPERCELL_LOAD_ORDER.md` compatibility-floor behavior.

---

## Update rule

When a new receipt supersedes an active one:
- update this file
- preserve the prior receipt in place for audit history
- record any resulting interpretation change in `MIRRORS/DRIFT_LEDGER.md` if relevant
