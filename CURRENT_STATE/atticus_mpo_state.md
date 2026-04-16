# ATTICUS_MPO State

Status: normalized current state

## Current baseline
- Source repo: `drop0ne/atticus-mpo`
- Source branch: `release-candidate`
- Current app baseline recorded in repo surfaces: **v5.0.1**

## Current known state
- PR #99 is merged into `release-candidate`.
- The first memory-engine context-cell upgrade is now part of the active MPO baseline.
- `StoredMemoryCell` now carries compact context rather than only detached findings.
- Stored-memory persistence now includes schema v9 support for context-bearing fields.
- Prompt-context injection now includes scope, baseline, tags, summary, and finding in a bounded block.
- Ranking is no longer pure recency.

## Active next-step focus
- Mirror this merged state into the supercell memory layer.
- Build the next retrieval-quality pass for query-aware ranking and stronger task/session relevance.
- Expose context-bearing stored-memory surfaces more explicitly in higher-level workflows.

## Notes
This file is a normalized supercell mirror of current MPO state.
The source repo remains authoritative.
