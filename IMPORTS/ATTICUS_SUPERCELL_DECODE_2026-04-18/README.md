# ATTICUS supercell decoded cell import

This import decodes the uploaded historical ATTICUS supercell packages into a repo-safe, non-active namespace.

Purpose:
- preserve decoded inventory for the three uploaded historical supercell packages
- keep the import outside active PASS7 load order
- record per-cell decode status and file counts before any deeper merge work

Boundaries:
- this import does **not** alter the active PASS7 framework namespace
- this import is a historical / forensic decode surface
- deeper per-cell file explosion can happen later without changing the decode boundary established here

Artifacts in this import:
- `PACKAGE_SUMMARY.json`
- `CELL_INVENTORY.md`

Status:
- decoded locally from the uploaded zip packages
- encoded into the repo as an isolated historical inventory surface
