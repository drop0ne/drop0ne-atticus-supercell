# CELL_SCHEMA_CORE_REHYDRATION_HEADER_v1_0

## Purpose
Rehydration header schema

## Canonical rules
- Rehydration headers must declare scope, source lineage, and recovery bounds.
- Headers should distinguish what is restored directly from source versus what is reconstructed or summarized.
- Rehydration framing may not imply full source recovery when only a bounded subset is available.

## Notes
- Works with ERP, SSP, and link-layer/context hydration runtime behavior.
- Important for honest continuity claims across sessions and handoffs.

## Provenance note
- Promoted from conversation-anchored Atticus memory plus prior cell structure.
- This is a bounded canonical summary, not a verbatim transcription of a newly uploaded source file.
