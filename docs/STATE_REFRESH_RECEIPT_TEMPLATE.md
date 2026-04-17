# State Refresh Receipt Template

Purpose: leave a durable audit trail for each supercell maintenance cycle.

Use this template after completing a refresh under `docs/STATE_REFRESH_PROTOCOL.md`.

---

## Receipt Identity
- receipt_id:
- generated_at:
- refresh_scope:
- trigger_event:
- source_repo:
- source_branch:

## Source Validation
- source event confirmed landed:
- active source baseline confirmed:
- mirrored artifact(s):
- ambiguity or blockers:

## Refresh Outputs Touched
- mirror summaries updated:
- current-state surfaces updated:
- durable memory cells added or superseded:
- resume packets updated:
- lifecycle / registry / index files updated:

## Current Pointers After Refresh
- latest current resume packet:
- latest current baseline cell:
- latest current milestone cell(s):
- affected project registry entry:

## Follow-up Remaining
- 

## Result
- refresh status:
- notes:

---

## Operating Rule
Use one receipt per coherent refresh cycle. Keep it compact, auditable, and explicit about what is now current.
