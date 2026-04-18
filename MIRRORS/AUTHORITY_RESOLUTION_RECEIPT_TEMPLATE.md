# Authority Resolution Receipt Template

Status: template
Purpose: provide an operator-approved arbitration artifact when doctrine lines, runtime baselines, or memory-governance states conflict.

---

## Receipt Header

- receipt_id: `ARR-YYYYMMDD-###`
- created_at: `<ISO-8601>`
- operator: `Jake`
- repository: `drop0ne/drop0ne-atticus-supercell`
- scope: `global | framework | runtime | supercell | session-bootstrap`
- status: `draft | approved | superseded | revoked`

---

## Conflict Summary

- conflict_class: `version_mismatch | doctrine_ambiguity | runtime_binding | canonical_root | other`
- affected_surfaces:
  - `<path or source>`
  - `<path or source>`
- short_description: `<one-paragraph summary>`

---

## Evidence Inputs

- source_repo_refs:
  - repo: `<owner/name>`
    ref: `<branch/tag/sha>`
    path: `<path>`
    blob_sha: `<sha or unknown>`
- supercell_refs:
  - `<repo-local path>`
- file_library_refs:
  - `<artifact name>`
- root_chat_refs:
  - `<locator or unknown>`

---

## Resolution Decision

- governing_line_selected: `<example: AMAS v1.2 | AMAS-1 v1.0 rollback line | AMAS 2.0-draft doctrine only>`
- effective_behavior_floor: `<explicit rehydration-safe | append-capable | read-only hydrate | other>`
- backward_compatibility_rule: `<how older surfaces should be interpreted>`
- supersedes_receipt_id: `<receipt id or none>`

---

## Enforcement Rule

State exactly what future hydrators and writers must do.

Example:
- Treat AMAS-1 v1.0 runtime behavior as authoritative for supercell activation.
- Preserve AMAS 2.0-draft as doctrine mirror only.
- Block implicit hydrate / autoload behavior.
- Require explicit rehydration and preflight before append/export.

---

## Notes

- unresolved_risks:
  - `<risk>`
- deferred_questions:
  - `<question>`
- comments:
  - `<free text>`

---

## Approval

- approved_by: `Jake`
- approval_timestamp: `<ISO-8601>`
- approval_statement: `I designate the above resolution as the governing interpretation for the defined scope until superseded by a later signed receipt.`
