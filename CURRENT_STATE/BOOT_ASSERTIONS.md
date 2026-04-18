# Boot Assertions

Status: active
Purpose: provide a compact pass/fail assertion sheet for early ATTICUS supercell boot.

---

## Required control-plane surfaces

### Assertion A1 — Authority boundary present
- required_path: `AUTHORITY.md`
- expected_state: `present`
- failure_effect: `stop boot and report missing authority boundary`

### Assertion A2 — Active receipt index present
- required_path: `CURRENT_STATE/ACTIVE_RECEIPTS.md`
- expected_state: `present`
- failure_effect: `remain conservative and use compatibility floor only`

### Assertion A3 — Drift ledger present
- required_path: `MIRRORS/DRIFT_LEDGER.md`
- expected_state: `present`
- failure_effect: `do not claim drift-clean state`

### Assertion A4 — Active baselines present
- required_path: `CURRENT_STATE/ACTIVE_BASELINES.md`
- expected_state: `present`
- failure_effect: `do not state effective framework/runtime/schema baselines as settled`

### Assertion A5 — Hydrator profile present
- required_path: `CURRENT_STATE/HYDRATOR_PROFILE.md`
- expected_state: `present`
- failure_effect: `default to strict read-only hydrate with no escalation beyond compact read`

### Assertion A6 — Task routing matrix present
- required_path: `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
- expected_state: `present`
- failure_effect: `use manual minimum-escalation reasoning and report routing uncertainty`

### Assertion A7 — Query checklist present
- required_path: `CURRENT_STATE/QUERY_CHECKLIST.md`
- expected_state: `present`
- failure_effect: `do not claim checked certainty/mutation conditions as fully verified`

### Assertion A8 — Framework state snapshot present
- required_path: `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
- expected_state: `present`
- failure_effect: `do not claim refreshed framework continuity`

### Assertion A9 — Session refresh anchor present
- required_path: `CURRENT_STATE/SESSION_STATE_REFRESH_2026-04-17.md`
- expected_state: `present`
- failure_effect: `session should be treated as not explicitly refreshed against current global state`

### Assertion A10 — Governing AMAS receipt present
- required_path: `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
- expected_state: `present`
- failure_effect: `do not treat explicit rehydration-safe governance floor as formally anchored`

---

## Boot outcome rules

### PASS
All A1–A10 present.
Result:
- compact control plane is complete
- early boot may proceed using active receipts, baselines, routing, and read-only governance floor

### PARTIAL
Any non-authority-critical assertion missing.
Result:
- remain read-only
- report which assertions failed
- do not overstate certainty

### FAIL
A1 missing, or multiple core control-plane assertions missing such that authority and baseline interpretation cannot be trusted.
Result:
- stop deeper hydration
- report missing surfaces
- do not claim valid boot

---

## Reporting format

Hydrators should report boot assertions as:
- assertions_checked: `A1..A10`
- pass_count: `<n>/10`
- failed_assertions:
  - `<assertion id>`
- boot_status: `PASS | PARTIAL | FAIL`
- resulting_mode: `read-only hydrate | restricted compact read | stop`
