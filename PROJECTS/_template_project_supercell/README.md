# Project Supercell Template Pack

Purpose: provide a reusable starting structure for future project-local supercells.

## What this template is for

Use this template when a new project needs:
- its own durable long-term memory surface
- compact context-bearing memory cells
- normalized current-state snapshots
- resume packets for new sessions
- a clean authority boundary between project-local canon and the global ATTICUS supercell

## Core rule

A project-local supercell does not replace the global ATTICUS supercell.
It narrows and localizes memory for one project while preserving compatibility with the ATTICUS umbrella memory model.

## Expected usage

1. Copy this template pack into the new project repo or its paired supercell repo.
2. Fill in the project identity and source-repo authority boundaries.
3. Start with normalized state files before adding many memory cells.
4. Add durable milestone cells only for information worth preserving beyond a single chat.

## Minimum template contents

- `PROJECT_SUPERCELL_SPEC.md`
- `PROJECT_AUTHORITY.md`
- `CURRENT_STATE_TEMPLATE.md`
- `SESSION_BOOTSTRAP_TEMPLATE.md`
- `MEMORY_CELL_TEMPLATE.json`
- `PROJECT_MIRROR_POLICY.md`
