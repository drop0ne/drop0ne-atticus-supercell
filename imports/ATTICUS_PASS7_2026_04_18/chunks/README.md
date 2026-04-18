# ATTICUS PASS7 Raw Bundle Chunk Landing Path

## Purpose

This directory is the planned repo-side landing path for chunked ingress of the preserved ATTICUS raw import bundle.

## Source lineage

- source archive: `atticus_cells_20260302_PASS7_FULL.tar.gz`
- source sha256: `9e411ccd4b445b33b7854115669afae786fbcfc78a2850750f435a9940f90357`
- encoded bundle label: `ATTICUS_SUPERCELL_IMPORT_BUNDLE.tar.gz`

## Status

- landing path prepared
- chunk payloads not yet embedded
- canonical artifacts remain unchanged

## Rules

- append-only ingress
- deterministic ordering
- no mutation of canonical Atticus artifacts
- chunk lineage must match the preserved source sha

## Next action

Populate this directory with deterministic chunk artifacts and then normalize `versions/ATTICUS_CLAUDE_INIT_v1/raw_bundle_manifest.json` to reflect repo-backed payload presence.
