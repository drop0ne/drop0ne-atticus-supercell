# Planned Work

## Recently completed
- First ATTICUS_MPO memory-engine upgrade merged in PR #99.
- Stored memory cells now carry compact context.
- Context injection now emits bounded structured memory blocks.
- SQLite schema v9 introduced compact context-bearing stored-memory fields.
- Query-aware retrieval hints merged in PR #100.
- Retrieval ranking now accepts objective, pack, scope, and baseline hints while preserving deterministic fallback behavior.

## Active items
- Mirror merged MPO retrieval-ranking state into durable supercell memory cells.
- Evaluate whether a stronger semantic or query-matching layer is needed beyond the current hint-based ranking system.
- Standardize session bootstrap packet generation for ChatGPT, Gemini, Claude, and ATTICUS_MPO.
- Continue mirroring key doctrine and project state from `amas-spec` and `atticus-mpo`.
- Expose context-bearing stored-memory surfaces more explicitly in higher-level workflows.

## Notes
This file is the normalized planning surface, not the source-code canon.
Source-code and project-local docs remain authoritative in their own repos.
