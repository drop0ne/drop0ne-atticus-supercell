# Active Effective Baselines

Status: active
Purpose: provide one minimal current-state surface for the effective ATTICUS framework baseline, product/runtime baseline, schema baseline, and governance floor used by the supercell.

---

## Effective baselines

### Framework baseline
- name: `ATTICUS`
- effective_version: `v6.4.1-HCII`
- status: `active`
- interpretation_rule: `Treat as the strongest continuity surface across mirrored doctrine, runtime docs, and supercell cells unless superseded by a later approved receipt.`

### Product / runtime baseline
- name: `ATTICUS MPO`
- effective_version: `version-mismatch-preserved`
- observed_values:
  - `v5.0.1` from `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/INDEX.md`
  - `v5.0.0b6` from `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/README.md` when consulted upstream
  - `v5.0.0b6` from `MIRRORS/SOURCE_CANON/FULL_BODY/atticus-mpo/ARCHITECTURE.md`
- status: `drift-preserved`
- interpretation_rule: `Do not collapse product-version mismatch inside the supercell. Treat framework version continuity as stronger than product-version display until source-repo docs are harmonized or a later receipt declares an effective MPO baseline.`

### Schema baseline
- name: `ATTICUS persistence schema`
- effective_version: `v8`
- status: `active`
- interpretation_rule: `Use schema v8 as the current mirrored runtime baseline unless superseded by a later source-canon update or approved receipt.`

### Governance floor
- name: `Supercell runtime governance floor`
- effective_behavior: `explicit rehydration-safe`
- source: `CURRENT_STATE/ACTIVE_RECEIPTS.md` -> `ARR-20260417-001`
- status: `active`
- interpretation_rule: `Block implicit hydrate, implicit autoload, and implicit auto-assimilation. Treat append/repair/export semantics as authoritative only after explicit activation and preflight.`

---

## Read order rule

Hydrators should read this file during early current-state boot.
Use it as the compact answer to: what framework line is active, what runtime/schema line is active, and what governance floor controls mutation-capable behavior.

If a later approved receipt changes any baseline here:
- update this file
- preserve prior values in drift or receipt history
- do not silently rewrite history-bearing mirrors
