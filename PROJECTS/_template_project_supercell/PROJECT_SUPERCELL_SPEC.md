# Project Supercell Specification Template

## Purpose

This template defines the minimum structure for a project-local supercell.

## Required surfaces

A project-local supercell should maintain:
- project identity
- authority boundaries
- normalized current-state summaries
- compact context-bearing memory cells
- mirror summaries for the project's source repo(s)
- session bootstrap artifacts

## Memory cell rule

A project memory cell should contain:
- durable finding or state
- compact context summary
- scope
- tags
- source repo / branch / ref
- baseline snapshot
- lineage
- provenance
- context fingerprint

It should not default to a full raw transcript dump.

## Recommended folder map

- `CURRENT_STATE/`
- `MEMORY/cells/`
- `MIRRORS/`
- `SESSION_PACKETS/`
- `docs/`

## Project inheritance rule

Project-local supercells should remain compatible with the global ATTICUS supercell model while narrowing memory to the project's own canon and workflow.
