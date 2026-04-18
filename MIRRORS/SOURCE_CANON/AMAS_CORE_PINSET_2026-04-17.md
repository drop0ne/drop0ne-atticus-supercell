# AMAS Core Pinset — 2026-04-17

Pinned source repo: `drop0ne/amas-spec`
Mirror purpose: preserve a repo-local doctrine read surface for ATTICUS supercell hydration.

---

## Pinned source: `SPEC.md`
Source ref: `main`
Blob SHA: `d8060ad89bade2c1b9fb160bc1b1ea890f3dcdc8`

### Notes
This snapshot is the AMAS core doctrine surface describing the four-tier authority hierarchy, conflict rules, invariants, and Memory Object schema.

### Snapshot excerpt
- Defines Tier 0 CANONICAL, Tier 1 OPERATOR, Tier 2 SESSION, Tier 3 INFERRED.
- Defines immutable governance invariants including single canonical root, explicit memory only, hydrate-never-mutates, and durable-memory rule.
- Splits runtime mechanics into `RUNTIME_BINDING.md` and preserves governance/runtime separation.
- Preserves AMCS mapping into AMAS authority structure.

---

## Pinned source: `RUNTIME_BINDING.md`
Source ref: `main`
Blob SHA: `e0223d0ee86c75d27b9f84b4fb39a7af063b47e9`

### Notes
This snapshot is the runtime-binding doctrine surface describing activation, preflight validation, append, repair, export, and runtime state transitions under AMAS.

### Snapshot excerpt
- No mutation without validated activation.
- Preflight must pass before append, repair, or export.
- Append sequence = stage, validate, hash, commit, regenerate derived views, emit receipt.
- Silent repair and silent chain-tip replacement are forbidden.
- Defines runtime states: READ_ONLY_HYDRATE, VALIDATING, BIND_READY, APPEND_READY, REPAIR_READY, EXPORT_READY, CLOSED_FINALIZED, BLOCKED.

---

## Mirror boundary
These pinned notes are local rehydration anchors.
For full source bodies, consult the source repo or later full-body mirrors.
