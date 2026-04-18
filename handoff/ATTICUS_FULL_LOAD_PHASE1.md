# ATTICUS — Full Load Phase 1

## Objective

Move the repository from a promoted/selectable Atticus release shell to a genuinely fuller Atticus load state.

## Current truth

What is already present on `main`:
- `ATTICUS_CLAUDE_INIT_v1` as a promoted selectable release package
- canonical cell, activation, lineage, semantic/dependency maps
- runtime contract and release-control metadata
- post-merge normalization and runtime-hookup handoff

What is not yet fully loaded:
- full raw Atticus corpus embedded in the repo
- repo-backed raw-file cell population for the preserved corpus
- runtime hookup implementation

## Phase 1 target

Establish the repo-side loading plan and attachment contract for bringing in the preserved raw Atticus bundle without mutating canonical artifacts.

## Definition of done

- a dedicated full-load work branch exists
- a committed handoff spec exists for full-load work
- the branch is anchored on current `main`
- next-phase work is explicitly split into:
  1. raw corpus ingestion into repo-backed artifacts
  2. cell population / segmentation projection
  3. runtime hookup

## Recommended subphases

### Phase 1A — Raw corpus ingress
- add the preserved import bundle or a chunked equivalent into the repo
- update `raw_bundle_manifest.json` so it no longer reports `partial_metadata_only`
- preserve source SHA lineage and append-only discipline

### Phase 1B — Raw cell population
- attach repo-backed raw-file cells for the preserved corpus
- upgrade `raw_cells_stub_index.json` from stub to populated index
- keep derivation additive and non-authoritative

### Phase 1C — Higher-order projection
- project segment cells and claim-cluster cells
- update `segment_cells_stub_index.json` and `claim_cluster_stub_index.json`
- refresh `semantic_map.json` and `dependency_graph.json` only as derived overlays

### Phase 1D — Runtime hookup
- implement selector resolution and activation path for `atticus_claude_init_v1`
- validate fail-closed behavior
- keep raw-preserved artifacts immutable

## Boundary

This branch is a planning/launch branch for the full-load effort.
It does not yet claim that the raw corpus has been fully embedded.
