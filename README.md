# ATTICUS Supercell

Status: prototype / reference implementation / active development  
Purpose: canonical cross-model long-term memory root for ATTICUS.

## Public release posture

This repository is intended to function as a **read-mostly canonical reference surface** for ATTICUS supercell governance, schemas, continuity artifacts, and validation scaffolding.

It should be read as:
- a prototype
- a reference implementation
- an active-development supercell surface

It should **not** be read as:
- a finished autonomous production memory substrate
- a claim that public visibility prevents copying, mirroring, or re-hosting
- a replacement for project-local source canon

## What this repo is

This repository is the authoritative super-memory cell for ATTICUS work.
It is intended to support:
- ChatGPT
- Gemini
- Claude
- ATTICUS_MPO

It stores normalized long-term memory cells, supercell manifests, mirror summaries, session bootstrap artifacts, machine-readable indexes, and validation scaffolding so new sessions can be resumed with bounded but meaningful context.

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
5. Validation and labeling surfaces should remain machine-auditable.
6. Future projects may have their own local supercells while this repository remains the global ATTICUS umbrella root.

## Current implementation status

Current repo-native implementation includes:
- authority and supercell specification documents
- machine-readable current-state pointers
- machine-readable project registry and memory-cell index
- concrete runner scaffold for non-mutating validation
- built-in schema validation for key runner inputs and emitted execution records
- generated and current example execution records
- public release hardening files such as `CODEOWNERS`, `SECURITY.md`, and `CONTRIBUTING.md`

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
- `tools/runner/` — non-mutating validation scaffold and schema-checking runner
