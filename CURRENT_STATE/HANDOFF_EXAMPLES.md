# Handoff Examples

Status: active
Purpose: provide short worked examples showing when to use each supported ATTICUS supercell handoff mode.

---

## Example 1 — Packet-First Direct Handoff

Mode:
- `packet_first_direct_handoff`

Task:
- `Tell me the current governance floor and whether mutation-capable interpretation is allowed.`

First file:
- `CURRENT_STATE/CONTROL_PLANE_PACKET.md`

Expected read depth:
- compact only

Expected answer shape:
- active governance floor = `explicit rehydration-safe`
- mutation-capable interpretation = `CONDITIONALLY_BLOCKED`
- default posture = `read-only hydrate`

Why this mode is sufficient:
- the question only needs the active receipt summary, active baselines, and current status
- no deeper provenance or doctrine comparison is required

Stop point:
- stop after packet-level answer
- do not enter full boot unless the user asks for underlying evidence or drift analysis

---

## Example 2 — Compact Cold-Start Handoff

Mode:
- `compact_cold_start_handoff`

Task:
- `What is this repo for, what framework line is active, and where do I look next if I need more detail?`

Primary path:
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`

Expected read depth:
- compact orientation

Expected answer shape:
- repo purpose / canonical boundary summary
- active framework baseline = `ATTICUS v6.4.1-HCII`
- default posture = `read-only hydrate`
- next-hop surfaces = control-plane index, quickstart, load order

Why this mode is sufficient:
- the task needs more than a packet but still does not require full deterministic boot or doctrine-level inspection

Stop point:
- stop after compact orientation unless the task becomes governance-sensitive or provenance-sensitive

---

## Example 3 — Full Control-Plane Handoff

Mode:
- `full_control_plane_handoff`

Task:
- `Given the AMAS ambiguity and current repo state, is export or mutation-capable interpretation authorized for this scope? Show the governing surfaces.`

Primary path:
- follow `SUPERCELL_LOAD_ORDER.md`

Expected read depth:
- full control-plane boot
- escalate through receipts, baselines, drift, routing, and possibly source-canon mirrors if required

Expected answer shape:
- active receipt identified
- active governance floor identified
- drift and ambiguity preserved
- authorization answer remains conditional or blocked unless explicit runtime conditions exist
- controlling surfaces cited before conclusion

Why this mode is required:
- the question is governance-sensitive and mutation-adjacent
- compact summaries alone are not enough for a trustworthy answer

Stop point:
- stop before claiming authorization if controlling receipt and explicit runtime conditions do not justify it

---

## Selection summary

Use:
- `packet_first_direct_handoff` for smallest practical direct handoff
- `compact_cold_start_handoff` for standard compact orientation
- `full_control_plane_handoff` for governance-sensitive, provenance-sensitive, drift-sensitive, or mutation-adjacent tasks

---

## Interpretation rule

These examples illustrate intended handoff behavior.
If an active approved receipt, active baseline, or drift-preserved controlling surface conflicts with an example, the controlling surface wins.
