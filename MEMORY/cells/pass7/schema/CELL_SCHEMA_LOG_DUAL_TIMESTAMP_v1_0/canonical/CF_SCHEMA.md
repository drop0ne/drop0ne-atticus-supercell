# CELL_SCHEMA_LOG_DUAL_TIMESTAMP_v1_0

## Purpose
Dual-timestamp logging schema

## Canonical rules
- Log structures should preserve both event-time and record-time when they differ.
- Dual timestamps improve auditability, replay accuracy, and reconstruction fidelity.
- Missing or ambiguous temporal data should remain explicit rather than inferred away.

## Notes
- Supports investigative logging, CCFLP discipline, and quantized exports.
- Useful whenever evidence chronology and recording chronology diverge.

## Provenance note
- Promoted from conversation-anchored Atticus memory plus prior cell structure.
- This is a bounded canonical summary, not a verbatim transcription of a newly uploaded source file.
