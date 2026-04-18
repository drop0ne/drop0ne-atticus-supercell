# Operating Mode Examples

Status: active
Purpose: provide short worked examples showing how `cold_start_compact` differs from `full_control_plane_boot` in practice.

---

## Example 1 — Cold-Start Compact Mode

Mode:
- `cold_start_compact`

Task:
- `What framework line is active in this repo?`

Minimum surfaces read:
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`

Route:
- task route: `framework baseline check`
- highest level used: `L0`

Expected answer shape:
- active framework baseline = `ATTICUS v6.4.1-HCII`
- governance floor = `explicit rehydration-safe`
- default posture = `read-only hydrate`
- no deeper escalation needed

Why compact mode is sufficient:
- the question is answered by active baselines and does not require doctrine comparison, provenance inspection, or mutation authority analysis.

Stop point:
- stop after compact answer
- do not read full-body mirrors

---

## Example 2 — Full Control-Plane Boot Mode

Mode:
- `full_control_plane_boot`

Task:
- `Is mutation-capable interpretation authorized for this task, given the AMAS ambiguity and current supercell state?`

Minimum surfaces read:
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `MIRRORS/DRIFT_LEDGER.md`
4. `CURRENT_STATE/BOOT_ASSERTIONS.md`
5. `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md`
6. `CURRENT_STATE/HYDRATOR_PROFILE.md`
7. `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
8. `CURRENT_STATE/QUERY_CHECKLIST.md`
9. `CURRENT_STATE/ACTIVE_BASELINES.md`
10. `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
11. `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
12. `SUPERCELL_LOAD_ORDER.md`

Route:
- task route: `mutation authorization question`
- highest level used: `L1` or `L3` depending on whether doctrine-line comparison is required

Expected answer shape:
- active receipt = `ARR-20260417-001`
- governance floor = `explicit rehydration-safe`
- current answer = `read-only only unless explicit activation and preflight are present`
- drift and doctrine ambiguity remain preserved
- mutation-capable interpretation is not authorized unless further explicit scope conditions are met

Why full control-plane mode is required:
- the question touches governance, authorization, drift, and mutation-sensitive interpretation.

Stop point:
- stop before claiming mutation authority if activation/preflight/canonical-root clarity is missing
- report `not authorized` or `unknown` rather than infer

---

## Example comparison summary

Use `cold_start_compact` when:
- compact state answers the task
- no doctrine comparison is needed
- no mutation-sensitive decision is involved

Use `full_control_plane_boot` when:
- authority, governance, drift, provenance, or mutation-capable interpretation are material to the task
- the answer could be unsafe if ambiguity is collapsed

---

## Interpretation rule

These examples illustrate the intended behavior of the operating modes.
If a signed receipt, active baseline, or drift-preserved conflict changes, follow the controlling artifact rather than the example narrative.
