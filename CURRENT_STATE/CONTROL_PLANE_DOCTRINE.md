# Control Plane Doctrine

Status: active
Purpose: summarize the core governing principles of the ATTICUS supercell control plane in one plain-language surface.

---

## Core doctrine

### 1. Receipt-first governance
When runtime interpretation matters, active approved receipts control.
Receipts make operational governance explicit where history, drift, or ambiguity would otherwise leave room for inconsistent interpretation.

### 2. Drift-preserving interpretation
Known drift, disagreement, or unresolved ambiguity should be preserved, not silently normalized.
The repo should state clearly what is settled and what is not.

### 3. Read-only-first posture
Default interpretation is conservative.
Hydration is read-only unless a controlling receipt and explicit runtime conditions justify more.

### 4. Compact before deep
Cold-start and compact-read surfaces exist so a model does not need to over-hydrate for simple tasks.
Deeper doctrine and source mirrors should be consulted only when the task requires them.

### 5. Deterministic boot
The repo is intended to boot in a predictable order.
Authority, receipts, drift, status, baselines, and routing surfaces should be consulted in a stable sequence rather than ad hoc.

### 6. History matters
Receipts, drift entries, changelogs, dated reports, and dated state surfaces should not be silently erased when they still matter for audit and provenance.
Historical context is part of governance integrity.

### 7. Examples do not outrank control surfaces
Examples, templates, quickstarts, and summaries guide usage.
They do not outrank active receipts, active baselines, or drift-preserved controlling surfaces.

### 8. Mutation authority is explicit
The repo should not be treated as implicit authorization for append, repair, export, or mutation-capable interpretation.
Such behavior requires explicit controlling conditions.

---

## Practical implications

This repo is designed to support:
- cold-start compact orientation
- full control-plane boot
- framework continuity restoration
- provenance-sensitive review
- governance-aware maintenance

This repo does not implicitly authorize:
- mutation-capable behavior
- implicit hydrate, autoload, or auto-assimilation
- certainty where drift or ambiguity still exists

---

## Control-plane operating principle

Prefer this order of reasoning:
1. What receipt is active?
2. What baseline is active?
3. What drift remains unresolved?
4. What boot or routing surface applies to this task?
5. What is the minimum sufficient escalation level?

---

## Maintenance principle

When changing the control plane:
- update controlling surfaces first
- update dependent summaries second
- preserve history rather than removing it
- append changelog state for material changes

---

## Interpretation rule

This doctrine page is a plain-language summary surface.
If it conflicts with an active approved receipt, active baselines, or a drift-preserved controlling surface, the controlling surface wins.
