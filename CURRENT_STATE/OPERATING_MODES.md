# Operating Modes

Status: active
Purpose: explicitly name the supported ATTICUS supercell entry modes and their intended use.

---

## Mode 1 — Cold-Start Compact Mode

Name:
- `cold_start_compact`

Purpose:
- low-cost orientation
- simple tasks
- compact baseline reading without deeper framework hydration

Primary surfaces:
- `AUTHORITY.md`
- `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- `CURRENT_STATE/QUICKSTART.md`
- `CURRENT_STATE/COLD_START_BOOT_REPORT_TEMPLATE.md`
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/HYDRATOR_PROFILE.md`

Default posture:
- `read-only hydrate`
- no deep escalation unless the task requires it

Typical use cases:
- what is this repo?
- what framework line is active?
- what receipt governs behavior?
- basic orientation and state reporting

Stop rule:
- stop after compact orientation unless the task requires deeper routing

---

## Mode 2 — Full Control-Plane Boot Mode

Name:
- `full_control_plane_boot`

Purpose:
- governance-sensitive tasks
- framework restoration
- doctrine comparison
- drift analysis
- boot validation/reporting

Primary surfaces:
- everything in cold-start compact mode, plus:
- `CURRENT_STATE/BOOT_ASSERTIONS.md`
- `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `CURRENT_STATE/SESSION_STATE_REFRESH_2026-04-17.md`
- `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
- `MIRRORS/ATTICUS_FRAMEWORK/CANONICAL_DERIVATION_LEDGER.md`
- framework cells
- source-canon mirrors as needed
- full-body mirrors only when needed

Default posture:
- `read-only hydrate` unless explicit authority permits more
- validation-first, routing-aware, drift-preserving

Typical use cases:
- full boot validation
- doctrine or runtime drift analysis
- provenance-sensitive answers
- determining whether mutation-capable interpretation is authorized

Stop rule:
- do not escalate past the task’s minimum needed level
- do not enter mutation-capable interpretation without receipt + activation + preflight clarity

---

## Mode Selection Rule

Use `cold_start_compact` when:
- the task is simple
- compact state answers the question
- no doctrine-level or mutation-sensitive decision is required

Use `full_control_plane_boot` when:
- the task is governance-sensitive
- drift or doctrine ambiguity is material
- provenance matters
- the answer may touch mutation, append, repair, or export authority

---

## Interpretation Rule

These modes organize behavior.
They do not override receipts, drift-preserved conflicts, or the active governance floor.
If a signed receipt conflicts with a mode description, the signed receipt controls.
