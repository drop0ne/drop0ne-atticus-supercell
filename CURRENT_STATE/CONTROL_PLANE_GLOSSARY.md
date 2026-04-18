# Control Plane Glossary

Status: active
Purpose: define recurring ATTICUS supercell control-plane terms in one place so future hydrators and maintainers use a consistent vocabulary.

---

## Core governance terms

### Active receipt
A receipt that is both:
- `approved`
- listed in `CURRENT_STATE/ACTIVE_RECEIPTS.md`
for the relevant scope.

Active receipts control runtime interpretation for that scope.

### Governance floor
The effective minimum behavior rule currently governing runtime interpretation.
In the present control plane, the governance floor is `explicit rehydration-safe` unless superseded by a later active receipt.

### Drift-preserved
A state where a mismatch, ambiguity, or disagreement is still represented explicitly rather than collapsed into a false single answer.

### Controlling surface
A surface whose contents are authoritative enough to determine interpretation for a given question.
Examples:
- active approved receipts
- active baselines
- drift-preserved controlling artifacts

### Summary surface
A compact surface that explains or indexes controlling surfaces without outranking them.
Examples:
- quickstart
- control-plane index
- status page
- examples
- reports

---

## Hydration and boot terms

### Read-only hydrate
The default conservative posture in which the repo is read and interpreted without assuming append, repair, export, or mutation-capable authority.

### Compact mode
The low-cost entry mode for simple orientation and baseline questions.
In repo terminology, this corresponds to `cold_start_compact`.

### Full control-plane boot
The deeper entry mode for governance-sensitive, provenance-sensitive, drift-sensitive, or mutation-adjacent tasks.
In repo terminology, this corresponds to `full_control_plane_boot`.

### Deterministic boot
A stable, explicit boot sequence in which authority, receipts, drift, baselines, and routing surfaces are consulted in a known order instead of ad hoc.

### Boot assertion
A required early-boot check used to determine whether the control plane is complete enough to trust for the intended task.

### Boot report
A structured result emitted after checking the boot surfaces, summarizing readiness and any blockers.

---

## Authorization terms

### Mutation-capable interpretation
Any interpretation that would treat the repo as authorizing append, repair, export, or other write-like runtime behavior rather than read-only hydration.

### Explicit activation
A clearly defined runtime condition showing that a context may move beyond read-only hydration for the relevant scope.

### Explicit preflight
A clearly defined validation step that must succeed before mutation-capable interpretation is treated as authorized.

### Conditionally blocked
A status meaning something is not authorized under the current control plane unless additional explicit conditions are satisfied.

### Not authorized
The correct answer when controlling conditions required for mutation-capable behavior are absent.

---

## Maintenance terms

### Receipt lifecycle
The set of rules governing how receipts are created, activated, superseded, revoked, and referenced by current-state surfaces.

### Dependency graph
The map of which surfaces depend on receipts, baselines, drift, and load-order behavior.
In repo terminology, this is documented in `CURRENT_STATE/GOVERNANCE_DEPENDENCY_MAP.md`.

### Normalization
Any act of compressing, summarizing, harmonizing, or simplifying control-plane information for navigation or readability.
Allowed normalization must not collapse drift, erase history, or outrank controlling surfaces.

### History-preserving
A maintenance rule meaning dated receipts, reports, drift entries, and state artifacts should remain visible when they still matter for audit and provenance.

### Changelog surface
An append-only history artifact that records material control-plane evolution.
In repo terminology, this is `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`.

### Audit pass
A recurring review of current-state, boot, drift, and maintenance surfaces to detect stale or divergent control-plane state.

---

## Practical interpretation notes

- If a term here conflicts with an active approved receipt, the active approved receipt controls.
- If a summary surface uses one of these terms loosely, the controlling surface defines the real meaning for the current scope.
- This glossary is a vocabulary aid, not a replacement for current-state governance surfaces.

---

## Interpretation rule

This glossary standardizes terminology.
It does not supersede active receipts, active baselines, drift-preserved controlling surfaces, or deterministic boot rules.
