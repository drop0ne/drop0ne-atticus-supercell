# Update Playbook

Status: active
Purpose: provide short worked maintenance scenarios for common ATTICUS supercell governance/control-plane updates.

---

## Scenario 1 — Changing an active receipt

Example change:
- a new receipt supersedes `ARR-20260417-001` for AMAS runtime behavior

### Goal
Update the active governance interpretation without breaking determinism or erasing history.

### Steps
1. Create the new approved receipt under `MIRRORS/`.
2. Preserve the old receipt in place and mark it `superseded` if appropriate.
3. Update `CURRENT_STATE/ACTIVE_RECEIPTS.md` to point to the new receipt.
4. Update `CURRENT_STATE/ACTIVE_BASELINES.md` if the effective governance floor changed.
5. Update `CURRENT_STATE/CONTROL_PLANE_STATUS.md` if mutation-capable readiness or operating readiness changed.
6. Update `SUPERCELL_LOAD_ORDER.md` if early-boot receipt handling changed.
7. Review `CURRENT_STATE/HYDRATOR_PROFILE.md`, `CURRENT_STATE/TASK_ROUTING_MATRIX.md`, and `CURRENT_STATE/QUERY_CHECKLIST.md` for stale assumptions.
8. Append the change to `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`.

### Do not
- delete the older receipt
- silently change runtime interpretation without updating `ACTIVE_RECEIPTS.md`
- update examples before the controlling surfaces are updated

### Minimum post-update check
- confirm active receipt pointer, active baselines, status, and load order all reflect the new controlling receipt

---

## Scenario 2 — Changing the effective framework baseline

Example change:
- ATTICUS framework baseline moves from `v6.4.1-HCII` to a later approved version

### Goal
Refresh framework continuity surfaces without breaking provenance or compact-read behavior.

### Steps
1. Create a new dated framework state snapshot rather than silently overwriting the old one when appropriate.
2. Update `CURRENT_STATE/ACTIVE_BASELINES.md` with the new effective framework line.
3. Update framework cells under `MEMORY/cells/...` if the canonical framework content changed.
4. Update `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md` if the boot packet should point to new framework cells or state surfaces.
5. Update `CURRENT_STATE/CONTROL_PLANE_STATUS.md` if readiness claims depend on the new baseline.
6. Review `CURRENT_STATE/QUICKSTART.md`, `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`, and live boot reports for stale baseline references.
7. Append the change to `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`.

### Do not
- silently rewrite history-bearing framework snapshots if a dated successor is more appropriate
- leave compact baseline surfaces pointing to an old framework line

### Minimum post-update check
- confirm active baselines, framework snapshot, bootstrap packet, and any compact baseline examples all agree on the effective framework line

---

## Scenario 3 — Resolving a drift item without breaking history

Example change:
- an upstream source mismatch is resolved, or a previously ambiguous doctrine line is clarified

### Goal
Reflect the new certainty while preserving the fact that drift once existed.

### Steps
1. Update `MIRRORS/DRIFT_LEDGER.md` by appending the resolution state; do not erase the original drift entry.
2. If the drift resolution changes runtime interpretation, create or update a receipt rather than relying on the drift note alone.
3. Update `CURRENT_STATE/ACTIVE_BASELINES.md` if the compact summary changed.
4. Update `CURRENT_STATE/CONTROL_PLANE_STATUS.md` if readiness or certainty changed.
5. Review `CURRENT_STATE/TASK_ROUTING_MATRIX.md`, `CURRENT_STATE/QUERY_CHECKLIST.md`, and `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md` for stale drift assumptions.
6. Append the update to `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`.

### Do not
- delete the old drift entry
- claim drift never existed
- let examples or summaries outrank the controlling receipt/baseline surfaces

### Minimum post-update check
- confirm drift history is still visible, while active surfaces reflect the new current interpretation

---

## General playbook rule

For governance-sensitive changes, update in this order:
1. controlling receipt or receipt pointer
2. active baselines
3. drift/history surface if relevant
4. status surface
5. load-order / hydrator / routing / query surfaces
6. quickstart, examples, and reports
7. changelog and index

---

## Interpretation rule

This playbook is operational guidance.
If a signed approved receipt or active controlling surface conflicts with an example step here, the controlling surface wins.
