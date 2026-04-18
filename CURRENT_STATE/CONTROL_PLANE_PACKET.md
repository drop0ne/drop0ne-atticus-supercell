# Control Plane Packet

Status: active
Purpose: provide one compact handoff surface that points a new model or runtime to the minimum controlling current-state artifacts before it does anything else.

---

## Active handoff mode

- mode: `packet_first_direct_handoff`
- mode_source: `CURRENT_STATE/HANDOFF_MODES.md`
- intended_use: `smallest practical current-state entry surface for direct model-to-model or runtime-to-runtime handoff`

---

## Primary handoff

Read these in order:

1. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
2. `CURRENT_STATE/ACTIVE_BASELINES.md`
3. `CURRENT_STATE/CONTROL_PLANE_STATUS.md`

Then stop unless the task requires more.

---

## Next-hop escalation surfaces

If you need the next level of orientation after this packet:

1. `CURRENT_STATE/QUICKSTART.md`
   - use for compact cold-start expansion
   - gives the standard small-file orientation path

2. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
   - use for broader control-plane navigation
   - gives the full map of current control-plane artifacts

3. `SUPERCELL_LOAD_ORDER.md`
   - use when the task needs deterministic full boot behavior
   - gives the ordered escalation path into deeper surfaces

---

## Compact current-state summary

### Active receipt
- current_active_receipt: `ARR-20260417-001`
- receipt_path: `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`

### Active framework baseline
- framework: `ATTICUS v6.4.1-HCII`

### Active runtime baseline
- runtime: `version-mismatch-preserved`

### Active schema baseline
- schema: `v8`

### Active governance floor
- governance_floor: `explicit rehydration-safe`

### Current operational status
- cold_start_compact: `READY`
- full_control_plane_boot: `READY`
- mutation_capable_interpretation: `CONDITIONALLY_BLOCKED`

---

## Default operating rule

Use the repo in `read-only hydrate` mode unless a controlling receipt and explicit runtime conditions justify more.

---

## Escalation rule

If the task is simple:
- stop after the compact current-state surfaces

If the task is governance-sensitive, provenance-sensitive, drift-sensitive, or mutation-adjacent:
- follow `SUPERCELL_LOAD_ORDER.md`
- use `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- consult `CURRENT_STATE/QUERY_CHECKLIST.md` before asserting conclusions

---

## Interpretation rule

This packet is a compact handoff surface.
It does not supersede active receipts, active baselines, drift-preserved controlling surfaces, or deterministic boot rules.
