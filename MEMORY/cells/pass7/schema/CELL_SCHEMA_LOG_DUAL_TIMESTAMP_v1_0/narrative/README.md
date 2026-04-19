# Narrative — CELL_SCHEMA_LOG_DUAL_TIMESTAMP_v1_0

This cell explains why some logs need both event-time and record-time to remain reconstructable.

Its narrative purpose is to show that chronology can diverge from write order, and that a trustworthy structure should preserve both rather than collapse them into one timestamp.

Within PASS7, this layer supports replay accuracy, auditability, and investigative timeline hygiene.

This is a bounded repo-authored narrative companion, not a verbatim source export.
