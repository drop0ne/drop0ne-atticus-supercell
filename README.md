# ATTICUS Supercell

Status: bootstrap draft  
Purpose: canonical cross-model long-term memory root for ATTICUS.

## What this repo is

This repository is the authoritative super-memory cell for ATTICUS work.
It is intended to support:
- ChatGPT
- Gemini
- Claude
- ATTICUS_MPO

It stores normalized long-term memory cells, supercell manifests, mirror summaries, and session bootstrap artifacts so new sessions can be resumed with bounded but meaningful context.

## What this repo is not

This repository does not replace:
- `drop0ne/amas-spec`
- `drop0ne/atticus-mpo`

Those repositories remain authoritative for their own doctrine and code. This repository mirrors selected state from them into a unified long-term memory surface.

## Core design rules

1. One cross-model authority root for ATTICUS long-term memory.
2. Mirrors do not replace project-local canon.
3. Memory cells must include compact context, not just detached findings.
4. Session bootstrap packets are first-class artifacts.
5. Future projects may have their own local supercells while this repository remains the global ATTICUS umbrella root.

## Initial layout

- `AUTHORITY.md` — authority boundaries and write rules
- `SUPERCELL_SPEC.md` — structure of valid super-memory cells
- `SESSION_BOOTSTRAP.md` — how to generate session resume packets
- `CURRENT_STATE/` — current ATTICUS and MPO status snapshots
- `MEMORY/` — cells, manifests, receipts, and supercells
- `MIRRORS/` — normalized mirrors of key project state
- `SESSION_PACKETS/` — templates and generated handoff packets
- `SCHEMAS/` — machine-readable contracts for cells and bootstraps
- `docs/` — operating policy and change-control guidance
