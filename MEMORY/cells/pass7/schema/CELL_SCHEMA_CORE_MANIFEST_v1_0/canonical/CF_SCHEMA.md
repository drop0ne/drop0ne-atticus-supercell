# CELL_SCHEMA_CORE_MANIFEST_v1_0

## Purpose
Core manifest schema

## Canonical rules
- Every sealed cell must expose a stable manifest contract.
- The manifest must preserve identity, version, creation time, integrity state, and authority metadata.
- Optional fields may extend the schema, but may not contradict required identity or integrity fields.
- The manifest is a schema contract, not a substitute for canonical content.

## Notes
- Governs the `manifest.json` shape used across PASS7 cells.
- Supports registry integrity, bundle composition, and rehydration-safe parsing.

## Provenance note
- Promoted from conversation-anchored Atticus memory plus prior cell structure.
- This is a bounded canonical summary, not a verbatim transcription of a newly uploaded source file.
