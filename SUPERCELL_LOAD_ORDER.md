# ATTICUS Supercell Load Order

Status: active
Purpose: provide a deterministic, minimal, explicit boot path for future AI nodes loading the ATTICUS supercell.

---

## Load Rules

1. Load only what is required for the task.
2. Prefer repo-local mirrored canon before relying on upstream availability.
3. Preserve higher-tier platform safety and operator authority.
4. Do not silently resolve documented drift or authority conflicts.
5. If an approved authority-resolution receipt exists for the relevant scope, apply it before mutation-capable behavior.
6. If no such receipt exists, use the compatibility floor defined in this file.

---

## Compatibility Floor

Until superseded by an operator-approved authority-resolution receipt:

- use explicit rehydration-safe behavior by default
- treat implicit hydrate / implicit autoload / implicit auto-assimilation as non-canonical
- allow read-only hydration from mirrored state and cells
- require explicit activation / preflight before append, repair, or export semantics are treated as authoritative
- preserve all unresolved doctrine/version conflicts as recorded in `MIRRORS/DRIFT_LEDGER.md`

---

## Minimal Boot Path

### Phase 0 — Authority and invariants
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `MIRRORS/DRIFT_LEDGER.md`
4. latest applicable authority-resolution receipt, if any

### Phase 1 — Current behavior contract, effective baselines, and framework state
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`
6. `CURRENT_STATE/ACTIVE_BASELINES.md`
7. `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
8. `MIRRORS/ATTICUS_FRAMEWORK/CANONICAL_DERIVATION_LEDGER.md`

### Phase 2 — Framework cells
9. `MEMORY/cells/atticus_framework_v6_4_1_hcii/0001_identity_and_kernel.md`
10. `MEMORY/cells/atticus_framework_v6_4_1_hcii/0002_stack_and_governance.md`
11. `MEMORY/cells/atticus_framework_v6_4_1_hcii/0003_runtime_mapping_lineage_and_gaps.md`

### Phase 3 — Bootstrap and provenance
12. `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md`
13. `MIRRORS/ATTICUS_FRAMEWORK/ROOT_CHAT_INDEX.md`

### Phase 4 — Source-canon mirrors
14. `MIRRORS/SOURCE_CANON/SOURCE_CANON_MANIFEST_2026-04-17.md`
15. `MIRRORS/SOURCE_CANON/AMAS_CORE_PINSET_2026-04-17.md`
16. `MIRRORS/SOURCE_CANON/ATTICUS_MPO_PINSET_2026-04-17.md`

### Phase 5 — Full-body mirrors (only when needed)
17. `MIRRORS/SOURCE_CANON/FULL_BODY/amas-spec/SPEC.md`
18. `MIRRORS/SOURCE_CANON/FULL_BODY/amas-spec/RUNTIME_BINDING.md`
19. `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/INDEX.md`
20. `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/ORCHESTRATION.md`
21. `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/ARCHITECTURE.md`

---

## Mutation-Capable Gate

Before any node treats the supercell as mutation-capable memory rather than read-only hydrate material, it should confirm:

- canonical root is unambiguous for the relevant scope
- writable ledger expectations are explicit
- an authority-resolution receipt exists when needed
- preflight/activation semantics are not being inferred from outdated doctrine alone

If these checks fail, remain in read-only hydration mode.

---

## Notes for Hydrators

- Framework version continuity is currently stronger than product-version continuity.
- Source-repo documents may disagree on MPO product version while agreeing on `ATTICUS v6.4.1-HCII`.
- AMAS doctrine surfaces currently span multiple lines (`2.0-draft`, v1.2 state, rollback-to-v1.0 evidence). Do not collapse them without a signed resolution artifact.
