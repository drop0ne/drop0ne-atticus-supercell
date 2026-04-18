# ATTICUS Supercell Drift Ledger

Status: active
Purpose: preserve discovered canon/version mismatches and unresolved mirror-state deltas without silently normalizing them.

---

## Entry 0001 — ATTICUS MPO baseline version mismatch

Date discovered: 2026-04-17
Severity: medium
Category: documentation baseline divergence

### Observed state
- `drop0ne/atticus-mpo/INDEX.md` reports current baseline: `v5.0.1` with framework `ATTICUS v6.4.1-HCII`
- `drop0ne/atticus-mpo/ARCHITECTURE.md` reports current baseline: `v5.0.0b6` with schema `v8` and framework `ATTICUS v6.4.1-HCII`
- `drop0ne/atticus-mpo/README.md` reports current version: `v5.0.0b6` with framework `ATTICUS v6.4.1-HCII`

### Interpretation
The framework mapping is consistent at `ATTICUS v6.4.1-HCII`, but the ATTICUS MPO product-version surface is not fully synchronized across docs.

### Supercell handling rule
- preserve all reported values as-is
- do not collapse to one version without source-repo correction or operator decision
- allow hydration consumers to treat framework version as stronger than product-version display when conflict exists

### Suggested remediation
Source repo should harmonize `INDEX.md`, `README.md`, and `ARCHITECTURE.md` on one product baseline.

---

## Entry 0002 — AMAS baseline ambiguity across accessible evidence

Date discovered: 2026-04-17
Severity: high
Category: doctrine / authority ambiguity

### Observed state
- accessible source repo surfaces show AMAS `2.0-draft`
- accessible persistent/global state still carries AMAS v1.2 + runtime-binding companion as the active global baseline
- accessible rollback evidence indicates a requested rollback target to AMAS-1 v1.0 with explicit rehydration and no implicit autoload

### Interpretation
This is not a simple doc mismatch. It is an authority-state ambiguity across doctrine evolution, runtime preference, and rollback instruction history.

### Supercell handling rule
- preserve all three states explicitly
- do not silently canonize one over the others inside the supercell mirror
- treat explicit rehydration-safe behavior as the compatibility floor until operator arbitration resolves the ambiguity

### Suggested remediation
Create an operator-approved authority resolution receipt that declares which AMAS line governs supercell runtime behavior.
