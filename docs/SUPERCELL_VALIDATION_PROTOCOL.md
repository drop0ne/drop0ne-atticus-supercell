# Supercell Validation Protocol

Purpose: define the canonical validation cycle for the ATTICUS supercell so schemas, pointers, indexes, registries, and generator artifacts remain internally consistent.

## 1. Scope

Run this validation protocol whenever:
- a refresh cycle completes
- a new project-local supercell is instantiated
- current pointers change
- generator inputs or outputs change
- schema-bearing files are added or revised

## 2. Validation domains

### A. Schema validation
Validate machine-readable artifacts against their declared schemas when applicable:
- refresh manifests
- generator inputs
- session-state bundles
- future structured artifacts

### B. Pointer consistency
Confirm that current pointers resolve to existing current artifacts:
- `CURRENT_REFRESH.json`
- `PROJECTS/PROJECT_REGISTRY.json`
- `SESSION_PACKETS/RESUME_PACKET_INDEX.json`
- `MEMORY/MEMORY_CELL_INDEX.json`

### C. Stale-current detection
Check that artifacts marked `current` are not contradicted by newer superseding pointers or refresh entries.

### D. Registry / index alignment
Confirm that:
- project registry latest resume packets match the resume-packet index
- project registry latest baseline cells match the memory-cell index
- lifecycle entries remain consistent with instantiated project roots

### E. Generator integrity
Confirm that:
- generator input references valid current packets/cells
- generated bundle output matches the bundle schema
- bundle selections are consistent with current pointers and bounds

## 3. Canonical validation order

Run validation in this order:
1. validate schemas
2. validate current pointers
3. validate registry/index alignment
4. validate stale-current conditions
5. validate generator input/output integrity
6. emit a validation report

## 4. Minimum validation outputs

A valid validation run should report:
- validation_run_id
- scope
- checks performed
- pass/fail/warn status by domain
- blocking errors if any
- recommended remediation if any

## 5. Stop conditions

Fail the validation run if:
- a current pointer targets a missing file
- a schema-governed artifact violates its schema
- registry/index current pointers disagree
- generator bundle references missing or stale current artifacts

## 6. Operating rule

Use this protocol as the default ATTICUS supercell validation pass unless a project-local validation protocol explicitly narrows it.
