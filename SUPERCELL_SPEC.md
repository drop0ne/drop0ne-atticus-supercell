# Supercell Specification

## Purpose

A supercell is the repository-level memory structure that allows multiple model environments to recover bounded, useful working state.

## Required components

A valid supercell should maintain:
- memory-cell index
- current state summaries
- mirror summaries of source repos
- session bootstrap templates
- receipts / manifests as they are introduced

## Memory cell design

Each long-term memory cell should contain:
- `cell_id`
- `title`
- `content`
- `context_summary`
- `context_scope`
- `context_tags[]`
- `source_repo`
- `source_ref`
- `source_branch`
- `baseline_app_version`
- `baseline_framework_version`
- `parent_cell_id`
- `created_at`
- `provenance`
- `context_fingerprint`
- `receipt_hash`

## Design rule

A memory cell must include enough context to be safely reused later without requiring the entire original chat to be reopened.
It should remain compact and should not become an unbounded raw transcript dump by default.
