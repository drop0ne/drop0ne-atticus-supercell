# Session State Generator Specification

Purpose: define how the ATTICUS supercell should assemble a bounded, model-ready session-state package from current resume packets, durable memory cells, registries, and project-local state.

## 1. Objective

Generate a compact session-state bundle that can be used to resume work for:
- ATTICUS umbrella scope
- ATTICUS working-baseline scope
- any registered project-local supercell

The generator should prefer durable current state and explicit pointers over raw chat replay.

## 2. Inputs

Required inputs:
- `target_scope`
- `project_id`
- `mode`
- `objective`

Optional inputs:
- `active_packet`
- `preferred_resume_packet`
- `preferred_cells[]`
- `include_global_baseline`
- `include_project_baseline`
- `include_latest_milestones`
- `max_cells`
- `max_chars`

## 3. Canonical selection order

Resolve session-state inputs in this order:

1. `CURRENT_REFRESH.json`
2. `SESSION_PACKETS/RESUME_PACKET_INDEX.json`
3. `MEMORY/MEMORY_CELL_INDEX.json`
4. `PROJECTS/PROJECT_REGISTRY.json`
5. project-local `CURRENT_STATE/` surfaces
6. explicitly requested preferred packets/cells

## 4. Default generation logic

### Global ATTICUS scope
- include current ATTICUS global resume packet
- include current ATTICUS working-baseline resume packet when relevant
- include ATTICUS current working baseline cell
- include AMAS governance baseline when governance context is required

### Project-local scope
- include latest current project-local resume packet
- include latest current project-local baseline cell
- include current project-local normalized state
- include latest project milestone cells when they materially affect restart continuity

## 5. Output contract

A valid generated session-state bundle should contain:
- `generator_run_id`
- `target_scope`
- `project_id`
- `selected_resume_packets[]`
- `selected_cells[]`
- `selected_state_surfaces[]`
- `recommended_next_action`
- `notes`

## 6. Boundedness rules

- prefer compact current-state packets over raw history
- prefer current baseline/milestone cells over stale cells
- do not exceed configured `max_cells`
- do not exceed configured `max_chars`
- do not include raw full-chat dumps by default

## 7. Stop conditions

Stop before emitting output if:
- no valid current resume packet exists for the requested scope
- no valid current baseline cell exists where one is required
- project registry and indexes disagree on current pointers
- selected inputs exceed bounds without a safe reduced subset

## 8. Operating rule

Use this specification as the default session-state generation behavior for ATTICUS umbrella resume and project-local resume until a project-specific generator spec narrows it.
