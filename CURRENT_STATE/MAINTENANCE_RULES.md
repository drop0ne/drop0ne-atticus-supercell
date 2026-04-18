# Maintenance Rules

Status: active
Purpose: define how future maintainers should update the ATTICUS supercell control plane without breaking determinism, provenance, or governance clarity.

---

## Rule class A — Files that should usually be updated together

### A1. Receipt changes
If an active authority-resolution receipt changes, review and update together as needed:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `SUPERCELL_LOAD_ORDER.md` if boot behavior changes
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md` if navigation needs to change
- `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`

### A2. Governance-floor or mutation-readiness changes
If the effective governance floor changes, review and update together as needed:
- `CURRENT_STATE/HYDRATOR_PROFILE.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/OPERATING_MODES.md`
- `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`
- `SUPERCELL_LOAD_ORDER.md`

### A3. Framework-baseline changes
If the effective framework baseline changes, review and update together as needed:
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_YYYY-MM-DD.md` or successor snapshot
- framework cells under `MEMORY/cells/...`
- `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`

### A4. Source-canon changes
If source mirrors or pinned upstream docs change materially, review and update together as needed:
- `MIRRORS/SOURCE_CANON/SOURCE_CANON_MANIFEST_*.md`
- relevant pinset summaries
- relevant full-body mirrors
- `MIRRORS/DRIFT_LEDGER.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md` if readiness changes

---

## Rule class B — Files that should be append-only or history-preserving

Prefer append-only or history-preserving treatment for:
- `MIRRORS/DRIFT_LEDGER.md`
- `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`
- authority-resolution receipts under `MIRRORS/`
- dated boot reports
- dated session refresh anchors
- dated framework state snapshots when superseded rather than silently overwritten

Do not silently erase historical control-plane states if they were once active and auditable.

---

## Rule class C — Changes that require a new receipt

Create a new authority-resolution receipt when any of the following occur:
- the effective governance floor changes
- mutation-capable interpretation becomes newly authorized or newly blocked for a scope
- a previously preserved doctrine ambiguity is formally resolved for runtime use
- a canonical-root or writable-ledger interpretation changes materially
- a mode description would otherwise conflict with active governance behavior

A receipt should be treated as required whenever a change would alter what future hydrators are allowed to infer about authority or mutation behavior.

---

## Rule class D — Changes that do not require a new receipt by default

A new receipt is not usually required for:
- navigation improvements
- new examples
- new templates
- additional reporting surfaces
- changelog/index improvements
- additive provenance mirrors that do not change active interpretation

These should still be logged in the changelog when material.

---

## Rule class E — Determinism safeguards

When updating the control plane:
1. update the controlling current-state surface first
2. update dependent navigation/reporting surfaces second
3. preserve drift instead of collapsing it unless a new receipt resolves it
4. prefer dated state artifacts when meaningfully superseding prior state
5. do not treat examples or summaries as stronger than receipts, drift ledger, or active baselines

---

## Rule class F — Minimum post-update checks

After a material control-plane update, verify at minimum:
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md` still points to the new artifact set
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md` still describes readiness accurately
- `SUPERCELL_LOAD_ORDER.md` still matches the intended boot path
- active receipts and active baselines are not stale relative to the change
- historical artifacts remain preserved where required

---

## Interpretation rule

These maintenance rules govern update discipline.
They do not override signed receipts or drift-preserved conflicts.
If a signed receipt requires behavior that conflicts with a maintenance convenience, the signed receipt controls.
