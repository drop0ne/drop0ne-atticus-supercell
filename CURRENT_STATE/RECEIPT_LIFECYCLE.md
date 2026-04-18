# Receipt Lifecycle

Status: active
Purpose: define how ATTICUS supercell authority-resolution receipts are created, activated, superseded, deprecated, and referenced by current-state surfaces.

---

## 1. Receipt role

A receipt is the controlling artifact when governance interpretation must be made explicit for runtime behavior.

Receipts are used to:
- resolve doctrine ambiguity for operational use
- anchor an effective governance floor
- define when future hydrators may or may not infer mutation-capable behavior
- preserve the reasoning path for governance changes without silently rewriting history

Receipts do not replace:
- drift-preserved history
- doctrine mirrors as source material
- active baselines as compact summary surfaces

They govern interpretation where ambiguity would otherwise affect runtime behavior.

---

## 2. Receipt creation triggers

Create a new receipt when any of the following occur:
- the effective governance floor changes
- mutation-capable interpretation becomes newly authorized or newly blocked for a scope
- a doctrine ambiguity is operationally resolved for runtime use
- a canonical-root or writable-ledger interpretation changes materially
- a prior receipt no longer matches the intended runtime behavior

Recommended creation path:
1. identify the ambiguity or governance change
2. preserve unresolved drift in `MIRRORS/DRIFT_LEDGER.md`
3. create the new receipt under `MIRRORS/`
4. update `CURRENT_STATE/ACTIVE_RECEIPTS.md`
5. update dependent current-state surfaces if the effective interpretation changed
6. log the change in `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`

---

## 3. Receipt statuses

Supported operational statuses:
- `draft`
- `approved`
- `superseded`
- `revoked`

Interpretation:
- `draft` = not controlling
- `approved` = controlling for its defined scope unless superseded
- `superseded` = historical only; preserved for audit
- `revoked` = preserved for history but not active for interpretation

---

## 4. Activation rules

A receipt becomes operationally active when:
- its status is `approved`
- its scope is relevant to the task or runtime surface
- `CURRENT_STATE/ACTIVE_RECEIPTS.md` points to it as active for that scope

A receipt should not be treated as active merely because it exists in the repo.

---

## 5. Supersession rules

When a new receipt supersedes an older one:
1. mark the older receipt as `superseded` if appropriate
2. preserve the older receipt in place
3. update `CURRENT_STATE/ACTIVE_RECEIPTS.md` to point to the new receipt
4. update `CURRENT_STATE/ACTIVE_BASELINES.md` if effective interpretation changed
5. update `CURRENT_STATE/CONTROL_PLANE_STATUS.md` if readiness changed
6. update `SUPERCELL_LOAD_ORDER.md` if boot behavior changed
7. log the supersession in `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`

Do not delete the older receipt.
Do not silently redirect interpretation without updating `ACTIVE_RECEIPTS.md`.

---

## 6. Deprecation / revocation rules

Use `revoked` when:
- a receipt should no longer be used
- it was issued in error
- its governing interpretation must be explicitly withdrawn

Revocation discipline:
- preserve the revoked receipt in place
- remove it from active receipt surfaces
- log the revocation in the changelog
- update dependent current-state surfaces if the active interpretation changes

---

## 7. Scope rules

Every receipt should make scope explicit.
Typical scope examples:
- `framework`
- `supercell`
- `session-bootstrap`
- `runtime-authorization`
- `export-authorization`

Hydrators should apply only receipts relevant to the current scope.
If scope relevance is unclear, report `unknown` and remain conservative.

---

## 8. Interaction with other current-state surfaces

### `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- authoritative pointer surface for which receipts are currently active

### `CURRENT_STATE/ACTIVE_BASELINES.md`
- compact summary of the effective interpretation resulting from active receipts

### `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
- readiness summary that should reflect material receipt-driven changes

### `MIRRORS/DRIFT_LEDGER.md`
- preserves unresolved ambiguity even when a receipt chooses a safe operational floor

### `SUPERCELL_LOAD_ORDER.md`
- should reference receipts in early boot when they matter to behavior

---

## 9. Receipt naming guidance

Recommended naming pattern:
- `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_<DOMAIN>_<NNNN>.md`

Examples:
- `AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
- `AUTHORITY_RESOLUTION_RECEIPT_EXPORT_0001.md`

The numeric suffix should be monotonic within the receipt domain.

---

## 10. Receipt interpretation priority

For runtime interpretation priority:
1. higher-tier platform safety
2. active approved receipt relevant to scope
3. active baselines
4. drift-preserved ambiguity and doctrine mirrors
5. examples, templates, and changelog history

This prevents examples or summaries from outranking controlling governance artifacts.

---

## 11. Minimum post-receipt checks

After creating or superseding a receipt, verify at minimum:
- `CURRENT_STATE/ACTIVE_RECEIPTS.md` is correct
- `CURRENT_STATE/ACTIVE_BASELINES.md` is not stale
- `CURRENT_STATE/CONTROL_PLANE_STATUS.md` still reflects readiness accurately
- `SUPERCELL_LOAD_ORDER.md` still reflects early-boot receipt handling
- historical receipts remain preserved

---

## Interpretation rule

This lifecycle document governs receipt maintenance discipline.
If a signed approved receipt conflicts with an example, template, or convenience surface, the signed approved receipt controls.
