# Authority Model

## Role of this repository

This repository is the canonical cross-model long-term memory root for ATTICUS work.

## Authority boundaries

- `drop0ne/amas-spec` remains canonical for AMAS doctrine.
- `drop0ne/atticus-mpo` remains canonical for ATTICUS_MPO code and local implementation docs.
- `drop0ne/drop0ne-atticus-supercell` is canonical for cross-model long-term memory, unified state snapshots, supercell manifests, and session bootstrap artifacts.

## Write policy

This repository should be treated as a single-writer authoritative memory ledger.
Changes should be deliberate, traceable, and structured.

## Invariants

1. One active global supercell root.
2. Memory cells must carry compact context.
3. Mirrors summarize and reference source canon; they do not silently replace it.
4. Session bootstrap artifacts must be reproducible from repo state.
5. Long-term memory must preserve provenance, scope, lineage, and retrieval tags.

## Mutation rules

- No silent rewrite of prior memory-cell meaning.
- New information should normally append or supersede with traceability.
- Historical branches may be retained as part of the audit trail.
