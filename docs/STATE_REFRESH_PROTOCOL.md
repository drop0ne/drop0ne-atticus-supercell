# State Refresh Protocol

Purpose: define the canonical maintenance cycle for updating the ATTICUS supercell so mirrors, normalized state, durable memory cells, lifecycle ledgers, and indexes remain aligned.

## 1. Scope

This protocol applies whenever the supercell is refreshed after:
- a merged PR or release-state shift in a source repo
- a new project-local supercell instantiation
- a material authority-boundary change
- a change to the current working baseline or restart surface

## 2. Canonical refresh order

Refresh the supercell in this order unless a project-specific override is explicitly documented.

### Phase 1 — Source validation
- confirm the source repo event actually landed
- confirm the active source branch / baseline
- identify the exact source artifact to mirror
- avoid mirroring speculative or unmerged state as canon

### Phase 2 — Mirror refresh
- update normalized mirror summaries for the affected source repo
- update project-local mirror notes if needed
- preserve source repo authority and avoid rewriting source canon

### Phase 3 — Current-state refresh
- update affected `CURRENT_STATE/` surfaces
- keep state summaries normalized and compact
- record the new active next-step focus if it changed

### Phase 4 — Durable memory refresh
- add or supersede durable milestone cells only when the change is worth preserving beyond one session
- keep memory cells compact, context-bearing, and provenance-linked
- avoid raw full-chat dumps by default

### Phase 5 — Resume refresh
- refresh the relevant resume packet(s)
- update the machine-readable resume-packet index if the primary restart surface changed

### Phase 6 — Registry / lifecycle refresh
- update the lifecycle ledger if a project was instantiated, rebuilt, or materially changed its creation method or authority boundary
- update the machine-readable project registry if project-local canonical pointers changed
- update the machine-readable memory-cell index if the latest current durable cell changed

### Phase 7 — Refresh receipt
- emit a refresh receipt or note summarizing:
  - what changed
  - what was refreshed
  - what is now current
  - what follow-up remains

## 3. Invariants

- Source repos remain authoritative for their own code and primary docs.
- The supercell mirrors and normalizes state; it does not silently replace source canon.
- Resume packets and indexes must point to currently valid restart surfaces.
- Durable memory cells must remain compact, context-bearing, and provenance-linked.
- Lifecycle and registry updates must stay synchronized with actual project-local state.

## 4. Minimum refresh outputs

A valid state refresh should update all affected outputs in one coherent pass:
- mirror summary or note
- current-state surface
- durable milestone cell if warranted
- latest resume packet if warranted
- machine-readable index/registry entries if pointers changed

## 5. Stop conditions

Pause and resolve before proceeding if:
- the source event is not actually merged / landed
- the source baseline is ambiguous
- the refresh would create contradictory current pointers
- a durable cell would be created without adequate provenance or scope
- the resume packet would point at stale or superseded baseline state

## 6. Operating rule

Use this protocol as the default maintenance cycle for the ATTICUS supercell unless a project-local protocol explicitly narrows it for that project.
