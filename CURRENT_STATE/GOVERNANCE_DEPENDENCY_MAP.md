# Governance Dependency Map

Status: active
Purpose: show which ATTICUS supercell current-state artifacts depend on receipts, active baselines, drift ledger state, and load-order behavior so future maintainers can see the dependency graph before changing anything.

---

## 1. Primary controlling surfaces

These are the strongest routine control surfaces for repo-local governance interpretation:

### A. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
Controls:
- which receipts are currently active for a scope
- which receipt should be consulted before mutation-capable interpretation

Downstream dependents:
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/HYDRATOR_PROFILE.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `SUPERCELL_LOAD_ORDER.md`
- boot reports and cold-start boot reports

### B. `CURRENT_STATE/ACTIVE_BASELINES.md`
Controls:
- effective framework baseline
- effective runtime/schema baseline summary
- effective governance floor summary

Downstream dependents:
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/QUICKSTART.md`
- `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`
- boot reports and cold-start boot reports
- any compact baseline answer path

### C. `MIRRORS/DRIFT_LEDGER.md`
Controls:
- preserved unresolved ambiguity and version/doc drift
- whether a surface may claim clean certainty

Downstream dependents:
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `SUPERCELL_LOAD_ORDER.md`
- drift-sensitive answers and provenance audits

### D. `SUPERCELL_LOAD_ORDER.md`
Controls:
- deterministic boot sequence
- when and where receipts/baselines/drift are consulted
- mutation-capable gate behavior

Downstream dependents:
- full boot behavior
- compact vs full mode behavior in practice
- boot assertions and boot reporting interpretation

---

## 2. Dependency clusters

### Cluster 1 — Receipt-driven governance cluster
Primary sources:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- active approved receipt files under `MIRRORS/`

Main dependents:
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/HYDRATOR_PROFILE.md`
- `CURRENT_STATE/RECEIPT_LIFECYCLE.md`
- `CURRENT_STATE/MAINTENANCE_RULES.md`

Meaning:
- if active receipt interpretation changes, these surfaces are at highest risk of becoming stale

### Cluster 2 — Baseline summary cluster
Primary sources:
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- framework state snapshot

Main dependents:
- `CURRENT_STATE/QUICKSTART.md`
- `CURRENT_STATE/COLD_START_BOOT_REPORT_2026-04-17.md`
- `CURRENT_STATE/BOOT_REPORT_2026-04-17.md`
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- compact answering paths

Meaning:
- if effective framework/runtime/schema/governance summary changes, compact read paths must be reviewed

### Cluster 3 — Drift-preservation cluster
Primary sources:
- `MIRRORS/DRIFT_LEDGER.md`
- derivation ledger

Main dependents:
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- `CURRENT_STATE/QUERY_CHECKLIST.md`
- `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`
- provenance/drift analysis paths

Meaning:
- if drift is resolved or newly discovered, certainty and routing surfaces may need revision

### Cluster 4 — Boot/orientation cluster
Primary sources:
- `SUPERCELL_LOAD_ORDER.md`
- `CURRENT_STATE/BOOT_ASSERTIONS.md`
- `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md`
- `CURRENT_STATE/COLD_START_BOOT_REPORT_TEMPLATE.md`

Main dependents:
- live boot reports
- quickstart behavior
- control-plane status
- control-plane index navigation expectations

Meaning:
- if boot order changes, reporting and status surfaces must be checked for stale assumptions

---

## 3. Practical dependency rules

### Rule D1
If `ACTIVE_RECEIPTS.md` changes:
- review `ACTIVE_BASELINES.md` first
- then review status, hydrator, routing, query, and load-order surfaces

### Rule D2
If `ACTIVE_BASELINES.md` changes:
- review quickstart, operating-mode examples, status, and live boot reports

### Rule D3
If `DRIFT_LEDGER.md` changes materially:
- review status, routing, query, and any example that claims certainty

### Rule D4
If `SUPERCELL_LOAD_ORDER.md` changes materially:
- review boot assertions, boot report templates, quickstart, status, and control-plane index

---

## 4. Safe update order

Recommended order when changing governance interpretation:
1. controlling receipt or active receipt pointer
2. active baselines
3. drift ledger or derivation surface if needed
4. control-plane status
5. load order / hydrator / routing / query surfaces
6. examples, quickstart, and reports
7. changelog and index

This reduces the chance of navigation or examples getting ahead of controlling interpretation.

---

## 5. Interpretation rule

This dependency map is a maintenance aid.
It does not override signed receipts, active baselines, or drift-preserved conflicts.
If a dependency description conflicts with an active receipt or current controlling surface, the controlling surface wins.
