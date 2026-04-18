# Handoff Modes

Status: active
Purpose: explicitly define the supported ATTICUS supercell handoff paths so future models and runtimes can choose the minimum correct entry mode.

---

## Mode 1 — Packet-First Direct Handoff

Name:
- `packet_first_direct_handoff`

Purpose:
- fastest model-to-model or runtime-to-runtime handoff
- smallest practical current-state entry surface
- minimal orientation before a simple task

Primary implementation surface:
- `CURRENT_STATE/CONTROL_PLANE_PACKET.md`

Companion surfaces:
- `CURRENT_STATE/HANDOFF_EXAMPLES.md`
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md`

Use when:
- the receiving model needs the smallest possible first read
- the task is simple or bounded
- the next system only needs the active receipt, active baselines, current status, and the next-hop escalation pointers

Default posture:
- `read-only hydrate`

Escalation path:
- `CURRENT_STATE/QUICKSTART.md` for compact expansion
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md` for broader navigation
- `CURRENT_STATE/HANDOFF_EXAMPLES.md` for worked path selection examples
- `SUPERCELL_LOAD_ORDER.md` for deterministic full boot

Stop rule:
- stop after the packet unless the task requires more

---

## Mode 2 — Compact Cold-Start Handoff

Name:
- `compact_cold_start_handoff`

Purpose:
- low-cost but fuller orientation than packet-first handoff
- compact baseline restoration for simple to moderate tasks

Primary implementation surface:
- `CURRENT_STATE/QUICKSTART.md`

Companion surfaces:
- `CURRENT_STATE/HANDOFF_EXAMPLES.md`
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md`

Primary path:
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`

Use when:
- the receiving model is starting cold
- the task needs more than a packet summary but does not yet require full control-plane boot
- the model should understand the main navigation and default posture before going deeper

Default posture:
- `read-only hydrate`

Escalation path:
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `CURRENT_STATE/HANDOFF_EXAMPLES.md`
- `SUPERCELL_LOAD_ORDER.md`

Stop rule:
- stop after compact orientation unless the task requires deeper governance, provenance, drift, or authorization analysis

---

## Mode 3 — Full Control-Plane Handoff

Name:
- `full_control_plane_handoff`

Purpose:
- governance-sensitive work
- provenance-sensitive work
- drift-sensitive work
- mutation-adjacent or authorization-sensitive work

Primary implementation surface:
- `SUPERCELL_LOAD_ORDER.md`

Companion surfaces:
- `CURRENT_STATE/HANDOFF_EXAMPLES.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`

Primary path:
- follow `SUPERCELL_LOAD_ORDER.md`

Use when:
- authority interpretation matters
- drift or doctrine ambiguity materially affects the task
- the task may touch mutation-capable interpretation, export, append, or repair semantics
- the model needs the full boot, routing, and verification surfaces

Default posture:
- `read-only hydrate` unless a controlling receipt and explicit runtime conditions justify more

Escalation path:
- deterministic boot order through current-state, framework, source-canon, and full-body mirror surfaces as needed

Stop rule:
- do not claim mutation-capable authorization unless controlling receipt and explicit runtime conditions are satisfied for the relevant scope

---

## Selection rule

Choose:
- `packet_first_direct_handoff` for smallest possible direct handoff
- `compact_cold_start_handoff` for standard cold-start orientation
- `full_control_plane_handoff` for governance-sensitive, provenance-sensitive, or mutation-adjacent tasks

---

## Interpretation rule

These handoff modes organize entry behavior.
They do not supersede active receipts, active baselines, drift-preserved controlling surfaces, or deterministic boot rules.
