# Project-Local Supercell Creation Checklist

Use this checklist when instantiating a new project-local supercell.

## Phase 1 — Identity and authority
- [ ] Set `project_name`
- [ ] Set `source_repo`
- [ ] Set `source_branch`
- [ ] Set `project_supercell_repo` if separate from the source repo
- [ ] Confirm source repo remains authoritative for code and project-local primary docs
- [ ] Confirm project-local supercell is authoritative for long-term memory, normalized state, and resume packets
- [ ] Confirm the global ATTICUS supercell remains the umbrella continuity root

## Phase 2 — Core files
- [ ] Create `README.md`
- [ ] Create `CURRENT_STATE/<project>_state.md`
- [ ] Create `MEMORY/cells/`
- [ ] Create `SESSION_PACKETS/generated/`
- [ ] Add at least one durable baseline memory cell
- [ ] Add at least one project-local resume packet

## Phase 3 — Baseline normalization
- [ ] Record active branch
- [ ] Record current baseline version
- [ ] Record current known state
- [ ] Record active next-step focus
- [ ] Record any known governance packet / roadmap anchor if applicable

## Phase 4 — Durable memory discipline
- [ ] Use compact context-bearing cells only
- [ ] Include provenance, scope, tags, baseline snapshot, lineage, and context fingerprint
- [ ] Avoid raw full-chat dumps by default
- [ ] Add milestone cells only for state worth preserving beyond one session

## Phase 5 — Resume readiness
- [ ] Generate a project-local resume packet
- [ ] Include relevant durable cells
- [ ] Keep the packet compact and restart-oriented
- [ ] Ensure recommended next action is explicit

## Exit criteria
- [ ] New project can be resumed from the project-local supercell without needing the full original chat
- [ ] Authority boundaries are explicit
- [ ] Project-local supercell remains compatible with the ATTICUS umbrella model
