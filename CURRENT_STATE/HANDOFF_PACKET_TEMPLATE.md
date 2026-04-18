# Handoff Packet Template

Status: template
Purpose: provide a reusable template for creating or refreshing compact packet-style handoff surfaces when the active receipt, active baselines, governance floor, or handoff rules change.

---

## Template Header

- packet_id: `PACKET-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- status: `active | superseded | historical`
- mode: `packet_first_direct_handoff`
- mode_source: `CURRENT_STATE/HANDOFF_MODES.md`

---

## Purpose

State in one or two lines:
- what the packet is for
- which scope it summarizes
- that it is a compact handoff surface and not a controlling governance artifact

---

## Primary handoff

Read these in order:

1. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
2. `CURRENT_STATE/ACTIVE_BASELINES.md`
3. `CURRENT_STATE/CONTROL_PLANE_STATUS.md`

Then stop unless the task requires more.

---

## Next-hop escalation surfaces

1. `CURRENT_STATE/QUICKSTART.md`
   - compact cold-start expansion

2. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
   - broader control-plane navigation

3. `CURRENT_STATE/HANDOFF_EXAMPLES.md`
   - worked examples for handoff-path selection

4. `SUPERCELL_LOAD_ORDER.md`
   - deterministic full control-plane boot

---

## Compact current-state summary

### Active receipt
- current_active_receipt: `<receipt id>`
- receipt_path: `<path>`

### Active framework baseline
- framework: `<framework line>`

### Active runtime baseline
- runtime: `<runtime summary>`

### Active schema baseline
- schema: `<schema version>`

### Active governance floor
- governance_floor: `<governance floor>`

### Current operational status
- cold_start_compact: `<READY | PARTIAL | BLOCKED | other>`
- full_control_plane_boot: `<READY | PARTIAL | BLOCKED | other>`
- mutation_capable_interpretation: `<CONDITIONALLY_BLOCKED | READY | other>`

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

## Maintenance notes

When refreshing this packet:
- update controlling surfaces first
- then refresh packet summary fields
- preserve the packet as a compact summary surface only
- do not let the packet outrank active receipts, active baselines, drift-preserved controlling surfaces, or deterministic boot rules

---

## Interpretation rule

This packet template is for summary/handoff use.
If a generated packet conflicts with an active approved receipt, active baselines, or drift-preserved controlling surface, the controlling surface wins and the packet should be repaired.
