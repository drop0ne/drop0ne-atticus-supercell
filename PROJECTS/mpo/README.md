# ATTICUS_MPO Project Supercell

Purpose: project-local supercell surface for ATTICUS_MPO.

## Authority boundary

- Source repo: `drop0ne/atticus-mpo`
- Source branch: `release-candidate`
- This project-local supercell is a narrowed memory surface for MPO-specific continuity.
- The global ATTICUS supercell remains the umbrella cross-project memory root.

## What this project-local supercell stores

- normalized MPO project state
- MPO-specific durable milestone cells
- MPO resume packets
- project-local mirror summaries when needed
- locked project packets tied to MPO implementation work

## Compatibility rule

This project-local supercell inherits the ATTICUS supercell model:
- compact context-bearing memory cells
- normalized current-state surfaces
- bounded resume packets
- source-repo canon remains authoritative
