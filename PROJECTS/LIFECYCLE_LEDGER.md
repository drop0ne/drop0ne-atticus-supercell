# Supercell Lifecycle Ledger

Purpose: record when and how each project-local supercell was instantiated and how it fits into the ATTICUS umbrella memory model.

## Ledger Entries

### 2026-04-17 — `AMAS`
- type: doctrine-local project supercell
- source_repo: `drop0ne/amas-spec`
- source_branch: `main`
- creation_mode: template-pack instantiation
- primary artifacts:
  - `PROJECTS/amas/README.md`
  - `PROJECTS/amas/CURRENT_STATE/amas_state.md`
  - `PROJECTS/amas/MEMORY/cells/AMAS_PROJECT_BASELINE_v1.json`
  - `PROJECTS/amas/SESSION_PACKETS/generated/amas_project_resume_2026-04-17.md`
- purpose: preserve AMAS-specific doctrine continuity as a narrowed project-local memory surface

### 2026-04-17 — `ATTICUS_MPO`
- type: implementation-local project supercell
- source_repo: `drop0ne/atticus-mpo`
- source_branch: `release-candidate`
- creation_mode: template-pack instantiation
- primary artifacts:
  - `PROJECTS/mpo/README.md`
  - `PROJECTS/mpo/CURRENT_STATE/mpo_state.md`
  - `PROJECTS/mpo/MEMORY/cells/MPO_PROJECT_BASELINE_v1.json`
  - `PROJECTS/mpo/SESSION_PACKETS/generated/mpo_project_resume_2026-04-17.md`
- purpose: preserve MPO implementation continuity as a narrowed project-local memory surface

### 2026-04-17 — `ATTICUS framework`
- type: framework-local project supercell
- source_repo: `drop0ne/drop0ne-atticus-supercell`
- source_branch: `main`
- creation_mode: checklist + starter manifest workflow
- primary artifacts:
  - `PROJECTS/atticus/STARTER_MANIFEST.instantiated.json`
  - `PROJECTS/atticus/PROJECT_CREATION_RECEIPT.md`
  - `PROJECTS/atticus/CURRENT_STATE/atticus_state.md`
  - `PROJECTS/atticus/MEMORY/cells/ATTICUS_FRAMEWORK_PROJECT_BASELINE_v1.json`
  - `PROJECTS/atticus/SESSION_PACKETS/generated/atticus_framework_project_resume_2026-04-17.md`
- purpose: preserve ATTICUS framework continuity as a narrowed umbrella-level working surface

### 2026-04-17 — `supercell_ops`
- type: supercell-operations project supercell
- source_repo: `drop0ne/drop0ne-atticus-supercell`
- source_branch: `main`
- creation_mode: one-file instantiation packet workflow
- primary artifacts:
  - `PROJECTS/supercell_ops/PROJECT_INSTANTIATION_PACKET.instantiated.md`
  - `PROJECTS/supercell_ops/CURRENT_STATE/supercell_ops_state.md`
  - `PROJECTS/supercell_ops/MEMORY/cells/SUPERCELL_OPS_PROJECT_BASELINE_v1.json`
  - `PROJECTS/supercell_ops/SESSION_PACKETS/generated/supercell_ops_resume_2026-04-17.md`
- purpose: preserve supercell architecture and instantiation-workflow continuity as a narrowed project-local working surface

## Operating Rule

Add a new ledger entry whenever:
- a project-local supercell is first instantiated
- its creation workflow materially changes
- its authority boundary materially changes
- its baseline is rebuilt under a new lifecycle method
