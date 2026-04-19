# ATTICUS historical cell decode import — 2026-04-19

This namespace contains decoded historical ATTICUS memory cells extracted from uploaded supercell package archives.

Design intent:
- preserve decoded historical cells in-repo
- keep the import isolated from the active PASS7 namespace and load order
- provide a repo-safe per-cell JSON representation that bundles manifest data, selected decoded text, provenance, and file indexes

Input packages:
- `ATTICUS_SUPERCELL_ASSIMILATION_PACKAGE_2026-04-03.zip`
- `ATTICUS_SUPERCELL_ASSIMILATION_PACKAGE_2026-04-04_REPAIRED_v1_2_append22r2_autoload(1).zip`
- `ATTICUS_SUPERCELL_SEED_FROM_CURRENT_CELL_2026-04-04.zip`

Import contents:
- `CELL_PACKAGE_REGISTRY.json`
- `CELL_INVENTORY.md`
- `cells/*.json`

Boundary:
- this import does **not** alter active PASS7 framework load order
- this import is a decoded historical inventory surface
- deeper merges into active namespaces should be explicit and audited
