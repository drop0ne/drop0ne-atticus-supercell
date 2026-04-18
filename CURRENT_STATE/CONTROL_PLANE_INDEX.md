# Control Plane Index

Status: active
Purpose: provide a one-page map of the ATTICUS supercell control-plane artifacts and their purpose.

---

## Core authority surfaces

### `AUTHORITY.md`
Role:
- defines repository authority boundaries
- identifies what this repo is canonical for
- preserves source-repo canon boundaries

### `CURRENT_STATE/ACTIVE_RECEIPTS.md`
Role:
- points to currently governing authority-resolution receipts
- gives the smallest receipt-entry surface for early boot

### `MIRRORS/AUTHORITY_RESOLUTION_RECEIPT_AMAS_0001.md`
Role:
- active AMAS/supercell runtime governance receipt
- anchors the explicit rehydration-safe floor

### `MIRRORS/DRIFT_LEDGER.md`
Role:
- preserves unresolved doctrine/version drift
- prevents silent normalization of conflicting surfaces

---

## Boot and reporting surfaces

### `CURRENT_STATE/BOOT_ASSERTIONS.md`
Role:
- compact pass/fail boot assertion sheet
- identifies required control-plane surfaces

### `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md`
Role:
- standardized format for emitting boot results

### `CURRENT_STATE/BOOT_REPORT_2026-04-17.md`
Role:
- first live example boot report
- records a PASS control-plane boot under current state

### `CURRENT_STATE/COLD_START_BOOT_REPORT_TEMPLATE.md`
Role:
- ultra-compact standardized report format for quickstart boots

### `CURRENT_STATE/COLD_START_BOOT_REPORT_2026-04-17.md`
Role:
- first live example cold-start boot report
- records a PASS quickstart boot under current state

### `CURRENT_STATE/AUDIT_REPORT_TEMPLATE.md`
Role:
- standardized format for emitting recurring audit results
- pairs with `CURRENT_STATE/AUDIT_CHECKLIST.md`

### `SUPERCELL_LOAD_ORDER.md`
Role:
- deterministic boot path
- controls early-load sequence and mutation-capable gate

---

## Hydrator behavior surfaces

### `CURRENT_STATE/HANDOFF_MODES.md`
Role:
- explicitly defines the supported handoff entry paths
- distinguishes packet-first direct handoff, compact cold-start handoff, and full control-plane handoff
- maps each handoff mode to its primary implementation surface and companion surfaces

### `CURRENT_STATE/HANDOFF_EXAMPLES.md`
Role:
- provides short worked examples for each supported handoff mode
- shows when to use packet-first direct handoff, compact cold-start handoff, and full control-plane handoff

### `CURRENT_STATE/HYDRATOR_PROFILE.md`
Role:
- default hydrator behavior contract
- read-only-first posture and escalation ladder

### `CURRENT_STATE/TASK_ROUTING_MATRIX.md`
Role:
- maps common tasks to minimum escalation levels
- helps nodes avoid unnecessary deep reads

### `CURRENT_STATE/QUERY_CHECKLIST.md`
Role:
- live-use checklist before answering, escalating, claiming mutation authority, or asserting certainty

### `CURRENT_STATE/SESSION_STATE_REFRESH_2026-04-17.md`
Role:
- records that current session state was refreshed against the rehydrated global control plane

### `CURRENT_STATE/OPERATING_MODES.md`
Role:
- explicitly names the supported entry modes
- defines when to use compact vs full control-plane boot

### `CURRENT_STATE/OPERATING_MODE_EXAMPLES.md`
Role:
- provides short worked examples for each operating mode
- shows practical difference between compact and full boot behavior

### `CURRENT_STATE/QUICKSTART.md`
Role:
- very short cold-start entrypoint
- tells new nodes which five files to read first and when to stop

### `CURRENT_STATE/RECEIPT_LIFECYCLE.md`
Role:
- defines how governance receipts are created, activated, superseded, revoked, and referenced by current-state surfaces
- keeps future receipt updates mechanically consistent

---

## Baseline and state surfaces

### `CURRENT_STATE/CONTROL_PLANE_PACKET.md`
Role:
- one compact handoff surface pointing to the active receipt, active baselines, current status, quickstart, and load order
- implementation surface for `packet_first_direct_handoff`
- preferred first file for direct model-to-model or runtime-to-runtime handoff
- intended as the smallest practical current-state entry surface before deeper escalation

### `CURRENT_STATE/HANDOFF_PACKET_TEMPLATE.md`
Role:
- reusable template for generating or refreshing compact packet-style handoff surfaces
- keeps future packet updates consistent when active receipts, baselines, governance floor, or handoff rules change

### `CURRENT_STATE/ACTIVE_BASELINES.md`
Role:
- compact current-state source for framework, runtime, schema, and governance-floor baselines

### `CURRENT_STATE/CONTROL_PLANE_STATUS.md`
Role:
- one-page readiness/health summary for compact use, full boot, framework restoration, provenance audit, and mutation-capable interpretation

### `CURRENT_STATE/GOVERNANCE_DEPENDENCY_MAP.md`
Role:
- shows which control-plane surfaces depend on receipts, active baselines, drift, and load-order behavior
- helps maintainers see the dependency graph before making governance changes

### `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
Role:
- detailed framework state snapshot
- main mirrored framework summary surface

### `MIRRORS/ATTICUS_FRAMEWORK/CANONICAL_DERIVATION_LEDGER.md`
Role:
- records deterministic derivation order and conflict handling choices

### `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md`
Role:
- deterministic framework bootstrap packet for future model nodes

### `MIRRORS/ATTICUS_FRAMEWORK/ROOT_CHAT_INDEX.md`
Role:
- root-chat provenance locator
- explicit gap logging for unrecovered raw roots

### `CURRENT_STATE/CHANGELOG_CONTROL_PLANE.md`
Role:
- append-only history of the control-plane buildout
- helps future maintainers understand how boot/governance surfaces evolved

### `CURRENT_STATE/CONTROL_PLANE_DOCTRINE.md`
Role:
- plain-language summary of the repo’s governing control-plane principles
- summarizes receipt-first, drift-preserving, read-only-first, deterministic boot, and history-preserving maintenance

### `CURRENT_STATE/CONTROL_PLANE_GLOSSARY.md`
Role:
- defines recurring control-plane terms in one place
- standardizes vocabulary such as active receipt, governance floor, drift-preserved, read-only hydrate, compact mode, and mutation-capable interpretation

### `CURRENT_STATE/NORMALIZATION_RULES.md`
Role:
- defines which kinds of summary/index normalization are allowed and which are forbidden
- prevents summaries, quickstarts, examples, or indexes from collapsing drift, erasing history, or outranking receipts

### `CURRENT_STATE/MAINTENANCE_RULES.md`
Role:
- defines update discipline for future control-plane changes
- identifies which files move together, what should remain append-only, and what requires a new receipt

### `CURRENT_STATE/UPDATE_PLAYBOOK.md`
Role:
- short worked maintenance scenarios for common governance/control-plane changes
- shows practical update order for receipts, baselines, drift resolution, and dependent surfaces

### `CURRENT_STATE/AUDIT_CHECKLIST.md`
Role:
- short recurring audit pass for weekly or post-governance-update review
- helps detect stale current-state, boot, drift, and maintenance surfaces before they silently diverge

### `CURRENT_STATE/AUDIT_REPORT_TEMPLATE.md`
Role:
- standardized format for recording audit outcomes, mismatches, and repair actions
- completes the recurring audit workflow with `AUDIT_CHECKLIST.md`

---

## Source-canon surfaces

### `MIRRORS/SOURCE_CANON/SOURCE_CANON_MANIFEST_2026-04-17.md`
Role:
- source-canon manifest for pinned upstream surfaces

### `MIRRORS/SOURCE_CANON/AMAS_CORE_PINSET_2026-04-17.md`
Role:
- compact AMAS doctrine pinset summary

### `MIRRORS/SOURCE_CANON/ATTICUS_MPO_PINSET_2026-04-17.md`
Role:
- compact ATTICUS MPO doctrine/runtime pinset summary

### `MIRRORS/SOURCE_CANON/FULL_BODY/...`
Role:
- full-body mirrored source docs
- used only when line-accurate doctrine/runtime analysis is needed

---

## Fast orientation rule

For direct handoff using `packet_first_direct_handoff`:
1. `CURRENT_STATE/CONTROL_PLANE_PACKET.md`

For standard fast orientation:
1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`
6. `SUPERCELL_LOAD_ORDER.md`

---

## Interpretation rule

This index is a navigation surface.
It does not supersede receipts, drift entries, or mirrored canon.
If any listed artifact conflicts with a signed receipt or drift-preserved state, the signed receipt and drift-preserved state control interpretation.
