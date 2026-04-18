# Control Plane Changelog

Status: active
Purpose: append-only summary of control-plane artifacts added during the ATTICUS supercell control-plane buildout.

---

## 2026-04-17 — Initial control-plane buildout sequence

### Phase A — Framework mirror and state anchoring
Added:
- `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
- `MIRRORS/ATTICUS_FRAMEWORK/CANONICAL_DERIVATION_LEDGER.md`
- `MIRRORS/ATTICUS_FRAMEWORK/ROOT_CHAT_INDEX.md`
- `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md`
- framework composite cells under `MEMORY/cells/atticus_framework_v6_4_1_hcii/`

Purpose:
- establish ATTICUS v6.4.1-HCII as mirrored framework baseline
- preserve derivation order, provenance, and reachable root-chat scope

### Phase B — Source-canon pinning and mirrors
Added:
- source canon manifest
- AMAS pinset summary
- ATTICUS MPO pinset summary
- full-body mirrors for key AMAS and ATTICUS MPO docs

Purpose:
- preserve stable repo-local source surfaces for future hydrators
- reduce dependency on upstream repo availability

### Phase C — Drift and authority resolution
Added:
- `MIRRORS/DRIFT_LEDGER.md`
- `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_TEMPLATE.md`
- `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`

Purpose:
- preserve unresolved drift explicitly
- anchor the explicit rehydration-safe governance floor through a signed receipt

### Phase D — Active current-state surfaces
Added:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/HYDRATOR_PROFILE.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `CURRENT_STATE/SESSION_STATE_REFRESH_2026-04-17.md`

Purpose:
- give hydrators compact current-state answers
- standardize read-only-first posture, routing, and live-use checks

### Phase E — Boot validation and reporting
Added:
- `CURRENT_STATE/BOOT_ASSERTIONS.md`
- `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md`
- `CURRENT_STATE/BOOT_REPORT_2026-04-17.md`
- `CURRENT_STATE/COLD_START_BOOT_REPORT_TEMPLATE.md`
- `CURRENT_STATE/COLD_START_BOOT_REPORT_2026-04-17.md`

Purpose:
- provide both full boot and cold-start boot reporting surfaces
- give future nodes concrete examples, not only templates

### Phase F — Orientation and mode surfaces
Added:
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
- `CURRENT_STATE/QUICKSTART.md`
- `CURRENT_STATE/OPERATING_MODES.md`
- `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`

Purpose:
- reduce cold-start cost
- explicitly name compact vs full control-plane entry modes
- show worked examples for each mode

### Phase G — Load-order integration
Updated repeatedly:
- `SUPERCELL_LOAD_ORDER.md`

Purpose:
- turn the repo into a deterministic boot surface instead of a loose artifact pile
- ensure every major control-plane addition is reflected in the boot path

---

## Change discipline

Rules:
- append new entries; do not rewrite prior history silently
- if a later receipt supersedes prior governance interpretation, log that here
- if a control-plane artifact is deprecated, log the deprecation rather than erasing the record

---

## Interpretation rule

This changelog is historical context.
It does not override active receipts, active baselines, or drift-preserved conflicts.
When in doubt, controlling current-state surfaces outrank this history log.
