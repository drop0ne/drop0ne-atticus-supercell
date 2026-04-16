# ATTICUS//LOCKED BUILDER PACKET

NAME: MPO_MEMORY_ENGINE_CONTEXT_CELL_UPGRADE_v1  
AUTHORITY: OPERATOR  
REPO: drop0ne/atticus-mpo  
BASE_BRANCH: release-candidate  
MODE: STRICT  
TASK_CLASS: runtime / persistence / context

## Signal Intake

ATTICUS_MPO currently stores thin memory cells and injects them into prompt context using a shallow formatting layer.
The next memory-engine upgrade must make stored memory cells carry compact reusable context rather than only detached findings.

## Objective

Upgrade the MPO memory engine so stored memory cells preserve enough bounded context to support safer reuse, better retrieval, and reliable rehydration.

## Definition of Done

1. Stored memory cell model includes compact context-bearing fields.
2. SQLite persistence supports those fields with backward-compatible migration.
3. Context injection ranks and formats cells using relevance and scope, not only recency.
4. Prompt injection remains bounded.
5. Tests cover migration compatibility, formatting, and retrieval behavior.

## Required design direction

### Data model
Extend the current stored memory cell shape to include compact context-bearing fields such as:
- context_summary
- context_scope
- context_tags
- baseline_app_version
- baseline_framework_version
- active_pack_id
- parent_cell_id
- source_turn_start
- source_turn_end
- context_fingerprint

### Persistence
- add append-only schema migration
- preserve backward compatibility with existing stored cells
- avoid silent destructive rewrite

### Retrieval / injection
- update prompt injection to separate:
  - context summary
  - finding content
- prefer best-fit bounded cells based on:
  - scope
  - tag overlap
  - branch / baseline match
  - recency

### Boundedness
- do not turn stored cells into full raw transcript dumps
- preserve strong size limits on injected prompt context

## Likely implementation surfaces
- `core/types.py`
- `services/context_injection.py`
- `persistence/sqlite_store.py`
- `persistence/migrations.py`
- tests covering migration and retrieval behavior

## Non-goals
- no attempt to make every cell a full chat archive
- no unbounded prompt injection growth
- no silent migration rewrite of old persisted state

## Acceptance checks
- old cells still load
- new cells persist and retrieve correctly
- prompt format is deterministic and bounded
- relevance ordering is testable
- no regressions to current session behavior
