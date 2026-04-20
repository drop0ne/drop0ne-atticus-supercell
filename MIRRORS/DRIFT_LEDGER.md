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

---

## Entry 0003 — AMAS runtime-binding version divergence across repo and runtime-visible memory

Date discovered: 2026-04-20  
Severity: high  
Category: runtime-binding / authority-line divergence

### Observed state
- runtime-visible shared/global memory still carries a draft `AMAS_RUNTIME_BINDING_v1.json` baseline companion artifact
- repo-local supercell state contains `amas/v2/contracts/AMAS_RUNTIME_BINDING_v2.json`
- repo-local `AMAS_RUNTIME_BINDING_v2.json` declares:
  - version: `2.0.0-draft`
  - hydrate default mode: `read_only`
  - `auto_append_on_load: false`
  - mutation protocol requires `two_phase_commit`
  - authority ledger path: `canonical/ledger/authority_events.jsonl`
  - invariant breach handling: `enter_FAILED_state`

### Interpretation
This is related to, but narrower than, the broader AMAS baseline ambiguity already preserved in Entry 0002.

The supercell now exposes a more concrete repo-local runtime-binding contract at the `v2` line while runtime-visible memory still carries a `v1` companion artifact as part of the accessible continuity surface.

This should not be silently normalized into “v2 is active everywhere” or “v1 is obsolete everywhere” without an operator-approved authority resolution receipt.

### Supercell handling rule
- preserve both runtime-binding lines explicitly
- do not silently replace memory-visible `v1` with repo-local `v2`
- treat repo-local `v2` as the stronger repo-materialized contract surface for local control-plane interpretation
- treat memory-visible `v1` as active continuity evidence until supersession is explicitly declared
- continue using the explicit rehydration-safe / read-only-first posture as the compatibility floor

### Suggested remediation
Create an operator-approved authority resolution receipt that declares one of the following:

1. `v1 historical / v2 active`
2. `v2 repo-local active but v1 remains cross-runtime compatibility evidence`
3. `parallel draft lines pending broader reconciliation`

Until that receipt exists:
- preserve both lines
- avoid rewriting `CURRENT_STATE/ACTIVE_BASELINES.md` to imply final resolution
- avoid updating compact handoff surfaces in a way that erases the divergence
