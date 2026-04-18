# ATTICUS MPO — Documentation Index

**This is the master entry point for all project documentation.**

ATTICUS MPO is a governed desktop orchestrator for multi-provider AI workflows, built in Python with a Tkinter operator console. It combines typed provider adapters, structured model catalogs, memory-cell prompt compilation, persistence, and guardrails for safe runtime control.

Current baseline: **v5.0.1** — Framework: **ATTICUS v6.4.1-HCII**

---

## Reading Order

If you are an AI model or human contributor joining this project, read in this order:

| Order | Document | Purpose |
|-------|----------|---------|
| 1 | **INDEX.md** (this file) | Orientation, doc map, roles |
| 2 | **DEV_LIFECYCLE.md** | Engineering rules, gates, protected surfaces |
| 3 | **ORCHESTRATION.md** | Multi-model governance, packet schema, review pipeline |
| 4 | **ROADMAP.md** | Current status, backlog, deferred tracks, how to add work |
| 5 | **KNOWN_ISSUES.md** | Open debt, test failures, active verification items |
| 6 | **ARCHITECTURE.md** | Code structure, layers, runtime flow |
| 7 | **README.md** | Project description, install, run, provider support |
| 8 | **DECISIONS.md** | Historical decision log (consult as needed) |
| 9 | **WORK_LOG.md** | Consolidated work history (consult as needed) |

---

## Document Map

### Governance (rules for all workers)

| Document | Content | Update Frequency |
|----------|---------|------------------|
| `DEV_LIFECYCLE.md` | Sprint scaffold, gate requirements, protected surfaces, epistemic discipline | Updated when process rules change |
| `ORCHESTRATION.md` | Four-layer role model, packet lifecycle, consensus policy, handoff schema | Updated when governance structure changes |
| `VERSIONING.md` | Version surfaces, increment policy, builder checklist | Updated when versioning policy changes |
| `SECURITY.md` | Secret handling, key storage, logging safety, runtime paths | Updated when security posture changes |

### Project State (current truth)

| Document | Content | Update Frequency |
|----------|---------|------------------|
| `README.md` | Project description, install, run, provider support, known limitations | Updated each release |
| `ARCHITECTURE.md` | Package structure, layer responsibilities, runtime flow, provider pipeline | Updated when architecture changes |
| `ROADMAP.md` | Completed stages, planned work, deferred tracks, pipeline phase | Updated each sprint |
| `KNOWN_ISSUES.md` | Open debt, test failures, verification gaps, gate summary | Updated each sprint |

### History (reference material)

| Document | Content | Update Frequency |
|----------|---------|------------------|
| `DECISIONS.md` | Append-only engineering decision log | Append when decisions are made |
| `WORK_LOG.md` | Consolidated record of all completed sprints, recovery phases, and migrations | Append after each sprint closes |

### Templates (for new work)

| Template | Use |
|----------|-----|
| `templates/PACKET_TEMPLATE.md` | Starting point for new orchestration packets |
| `templates/BUILD_PACKET_TEMPLATE.md` | Stripped execution packet for `ATTICUS-BUILD-NODE` |
| `templates/REVIEW_APPEND_TEMPLATE.md` | Reviewer note format |
| `templates/WORK_LOG_ENTRY_TEMPLATE.md` | Format for logging completed work |

---

## Role Table

ATTICUS is developed using a four-layer, single-writer orchestration pipeline. Every worker — human or AI — must know which role they occupy before starting work.

| Role | ID | Function | Constraint |
|------|----|----------|------------|
| **Operator** | — | Final authority on all decisions | Approves or rejects all work |
| **Packet Controller** | `ATTICUS-CTRL-NODE` | Drafts scope, normalizes packets, tracks backlog | No repo writes |
| **Strategist / Verifier** | `ATTICUS-STRAT-NODE` | Challenges assumptions, hardens scope, alternate-path review | No repo writes |
| **Implementation Reviewer** | `ATTICUS-IMPL-NODE` | Deep technical review, architecture critique, failure-mode analysis | No repo writes |
| **Builder / Writer** | `ATTICUS-BUILD-NODE` | Executes approved packets, edits repo, runs tests, prepares commits/PRs | No scope expansion; sole writer |

Default bindings (current baseline):

| Role | Default Occupant | Surface |
|------|-----------------|---------|
| Operator | Jake | All surfaces |
| `ATTICUS-CTRL-NODE` | ChatGPT | ChatGPT session |
| `ATTICUS-STRAT-NODE` | Gemini | Browser session |
| `ATTICUS-IMPL-NODE` | Claude Desktop App / Cowork | Claude desktop app |
| `ATTICUS-BUILD-NODE` | Claude Code | Claude Code + local repo |

**You must identify which role you are assigned before proceeding.** Your role is specified in the builder prompt you received. If no role is specified, ask the operator.

---

## How New Work Enters the System

All work — features, bugs, refactors, docs — follows the same pipeline:

1. **Propose:** Identify the work item. Consult `ROADMAP.md` for existing backlog.
2. **Draft:** The Packet Controller creates an orchestration packet using `templates/PACKET_TEMPLATE.md`.
3. **Review:** Strategist and Implementation Reviewer challenge and harden the packet.
4. **Approve:** The Operator approves, revises, or rejects.
5. **Build:** The Builder executes the approved packet. No scope expansion.
6. **Audit:** At least one non-Claude model audits the result.
7. **Log:** The completed work is recorded in `WORK_LOG.md` using `templates/WORK_LOG_ENTRY_TEMPLATE.md`.
8. **Update:** `ROADMAP.md` and `KNOWN_ISSUES.md` are updated to reflect the new state.

Full details: `DEV_LIFECYCLE.md` (rules), `ORCHESTRATION.md` (governance).

---

## How Work Gets Logged

Every completed sprint, packet, or significant change must be recorded in `WORK_LOG.md`. This is not optional. The work log is the project's institutional memory and the primary tool for preventing re-derivation of settled decisions.

Required fields per entry: date, packet ID (if applicable), scope summary, changed files, test evidence, commit/PR reference, and any decisions made. See `templates/WORK_LOG_ENTRY_TEMPLATE.md` for the format.

---

## Documents Retired by This Consolidation

The following documents from the prior documentation set have been absorbed into the current set and should not be recreated:

| Retired Document | Absorbed Into |
|-----------------|---------------|
| `RECOVERY_READ_FIRST.md` | `INDEX.md` (this file) |
| `RECOVERY_PROGRAM.md` | `WORK_LOG.md` (recovery phases are historical record) |
| `RECOVERY_LEDGER.md` | `WORK_LOG.md` (completion evidence preserved) |
| `PROCESS_PIPELINE.md` | `ROADMAP.md` (pipeline phase, deferred tracks, anti-debt rules) |
| `CLAUDE_CODE_SPRINT_DIRECTIVE.md` | `DEV_LIFECYCLE.md` + `ORCHESTRATION.md` (rules are in governance docs) |
| `CODEBASE_STACK_LOG.md` | `ARCHITECTURE.md` (runtime flow section) |
| `ARCHITECTURE_PLAN.md` | `WORK_LOG.md` (TDC-1 completion record) |
| `ARCHITECTURE_PROGRESS_LOG.md` | `WORK_LOG.md` (TDC-1 progress record) |
| `TEST_MATRIX.md` | `KNOWN_ISSUES.md` (gate summary) |
| `MIGRATION_NOTES.md` | `WORK_LOG.md` (version migration records) |
| `MPO_META_COGNITION_ARCH_EXTENSION.md` | `ROADMAP.md` (deferred track) |
| `MPO_META_COGNITION_PROGRESS.md` | `WORK_LOG.md` (progress record) |
| `STREAMING_HEADLESS_ARCH_PLAN.md` | `ROADMAP.md` (completed/deferred) |
| `STREAMING_HEADLESS_PROGRESS.md` | `WORK_LOG.md` (completion record) |
| All `SPRINT_*.md` files | `WORK_LOG.md` (sprint completion records) |
| All `ORCH-*.md` packets | `archive/packets/` (historical reference only) |

**Rule:** Do not create new top-level documentation files without operator approval. New work is logged in `WORK_LOG.md`, not in new standalone documents.
