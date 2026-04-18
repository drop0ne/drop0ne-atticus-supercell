# ATTICUS Multi-Model Orchestration Policy v1.1

MPO_SPEC_VERSION: 1.1

---

## 1. Core Operating Policy

This repository operates under strict multi-model, single-writer governance.

1. The operator (Jake) is the final authority.
2. Claude Code (`ATTICUS-BUILD-NODE`) is the sole repository writer.
3. ChatGPT, Gemini, and Claude Desktop App / Cowork are review/planning peers and are non-writing by default.
4. Every chat output is a handoff packet using the canonical scaffold: `[Signal Intake]` `[Plan & DoD]` `[Execution]` `[Verification]` `[Final]` `[Backlog / Next]`
5. The `[Execution]` block must contain orchestration metadata, the last review note, the consensus ledger, and the builder packet.
6. No build may begin until consensus is reached and the operator approves.
7. Claude Code may execute only the approved builder packet.
8. **Post-Build Audit:** Post-build output must be re-audited. At least one post-build audit pass from a non-Claude model (ChatGPT or Gemini) is required before marking the packet `COMPLETE`.
9. Scope expansion is forbidden unless explicitly approved by the operator.
10. Unresolved disagreements must be preserved in the packet, not silently erased.
11. **Consensus Override Policy:** If a required reviewer is unavailable after an operator-verified attempt, the operator may set `CONSENSUS_OVERRIDE` to one of:
    - `operator_bypass` — reviewer unreachable
    - `operator_override` — reviewer disagreed, operator proceeds

    The override reason must be recorded in the consensus ledger. No override may be used to skip the operator approval step itself.

---

## 2. Canonical Orchestration Topology & Surfaces

### Role Table

| Role | ID | Default Occupant | Surface | Authority |
|------|----|------------------|---------|-----------|
| Packet Controller | `ATTICUS-CTRL-NODE` | ChatGPT | ChatGPT session | non-writing |
| Strategist / Verifier | `ATTICUS-STRAT-NODE` | Gemini | browser session | non-writing |
| Implementation Reviewer | `ATTICUS-IMPL-NODE` | Claude Desktop App (primary) / Cowork (alternate) | Claude desktop app | non-writing |
| Builder / Writer | `ATTICUS-BUILD-NODE` | Claude Code | Claude Code + local repo + VS26 | sole writer |

### Tool-Surface Map

- **ChatGPT** — packet author, packet normalizer, contradiction detector, backlog and handoff manager.
- **Gemini (browser)** — external verifier, alternate-read strategist, scope hardener, blind-spot check against the other models.
- **Claude Desktop App / Cowork** — deep technical reviewer, architecture critic, failure-mode detector, implementation-quality reviewer.
- **Claude Code** — only system allowed to mutate the repository. Edits files, runs local commands/tests, prepares commits/PRs, reports exact changed files and outcomes.
- **Visual Studio 2026** — not a cognitive node. IDE surface / local workspace host. Primary observable editing environment for Claude Code.

### Critical Claude Surface Split

Do not treat "Claude" as one thing. Use these separate identities:

- `CLAUDE_REVIEW_SURFACE` — Claude Desktop App / Cowork. Review only.
- `CLAUDE_BUILD_SURFACE` — Claude Code. Writer only.

This prevents one Claude surface from silently self-approving the other.

### Independence Rule

Claude Desktop App / Cowork review is **required but not independence-qualifying**. Both Claude surfaces share a model family, so IMPL-NODE review does not count toward the cross-model independence gate.

The true cross-model independence gate requires:

- ChatGPT = pass
- Gemini = pass
- Operator = approved

Claude review is mandatory before build but does not satisfy an independence slot.

---

## 3. Authority Model

- **Final authority:** Jake (operator)
- **Writer of record:** Claude Code (`ATTICUS-BUILD-NODE`)
- **Non-writing reviewers:** ChatGPT, Gemini, Claude Desktop App / Cowork
- **Repository mutation rule:** only `ATTICUS-BUILD-NODE` may edit tracked files, stage, commit, open PRs, or merge (when authorized by the operator).

---

## 4. How VS26 Fits

Claude Code works against the same local folder that Visual Studio 2026 already has open.

- **Primary mode:** Claude Code performs file mutations in the local repo. VS26 reflects that work as the visible IDE shell, editor, terminal, diff viewer, and test-observation surface.
- **Secondary mode:** GUI interaction with VS26 only when necessary for debugging, run configuration, IDE-specific commands, or local inspection.

Policy: Claude Code writes to the local repo. VS26 reflects and hosts that work. GUI automation is not required for every edit.

---

## 5. Packet Lifecycle

### Phase 1 — Packet Draft

ChatGPT creates the initial work packet. Status: `DRAFT`

### Phase 2 — Strategic Challenge

Gemini reviews scope, alternative fix paths, hidden assumptions, and regression risk. Status: `UNDER_REVIEW`

### Phase 3 — Deep Implementation Review

Claude Desktop App / Cowork reviews architecture, failure modes, patch quality, deadlocks, lifecycle, and test risk. Status: `UNDER_REVIEW`

### Phase 4 — Operator Approval

Jake approves, sends back for revision, narrows scope, or rejects. Status: `READY_FOR_OPERATOR` → `APPROVED_FOR_BUILD`

### Phase 5 — Build Execution

Claude Code executes against the local repo in the VS26-open workspace. Status: `APPROVED_FOR_BUILD`

### Phase 6 — Post-Build Audit

At least one non-Claude model (ChatGPT or Gemini) audits changed files, test outcomes, diff summary, and scope compliance. Status: `BUILT_PENDING_AUDIT` → `COMPLETE`

---

## 6. Consensus Policy

### Minimum Build Gate

- ChatGPT = pass
- Gemini = pass
- Claude review = pass (required, not independence-qualifying)
- Operator = approved

All required changes from reviewers must be resolved before build. Unresolved blocking objections halt the packet.

### Override

If a required reviewer is unavailable after operator-verified attempt, the operator may override per Rule 11 above. The override is logged in the consensus ledger with a reason string.

---

## 7. Canonical Handoff Packet Schema

Every model-to-model relay must embed this structure within the `[Execution]` block:

    ORCHESTRATION_METADATA
    - MPO_SPEC_VERSION: 1.1
    - PACKET_ID: ORCH-YYYYMMDD-###
    - REPO: drop0ne/atticus-mpo
    - BASE_BRANCH: release/stable
    - TARGET_BRANCH: <branch>
    - TASK_CLASS: bugfix | feature | refactor | test | docs | infra
    - OPERATOR: Jake

    - CTRL_ROLE_ID: ATTICUS-CTRL-NODE
    - CTRL_SURFACE: chatgpt
    - STRAT_ROLE_ID: ATTICUS-STRAT-NODE
    - STRAT_SURFACE: gemini-browser
    - IMPL_ROLE_ID: ATTICUS-IMPL-NODE
    - IMPL_SURFACE: claude-desktop-app | cowork
    - BUILD_ROLE_ID: ATTICUS-BUILD-NODE
    - BUILD_SURFACE: claude-code

    - WRITER_OF_RECORD: Claude Code
    - WRITER_IDENTITY: claude-code-local
    - IDE_SURFACE: visual-studio-2026
    - REPO_WRITE_ALLOWED: true (for ATTICUS-BUILD-NODE only)

    - CONSENSUS_STATUS: DRAFT | UNDER_REVIEW | READY_FOR_OPERATOR | APPROVED_FOR_BUILD | BUILT_PENDING_AUDIT | COMPLETE
    - CONSENSUS_OVERRIDE: none | operator_bypass | operator_override
    - LAST_REVIEWER: <model_name>
    - NEXT_REVIEWER: <model_name>

    - SCOPE_LOCK:
      - IN_SCOPE: ...
      - OUT_OF_SCOPE: ...

    LAST_REVIEW_NOTE
    - reviewer: <model>
    - assessment: pass | pass_with_changes | blocked
    - key_findings:
      - ...
    - required_changes:
      - ...
    - risk_flags:
      - ...

    CONSENSUS_LEDGER
    - ChatGPT: <status>
    - ClaudeReview: <status>
    - Gemini: <status>
    - Operator: pending | approved | blocked

    BUILDER_PACKET
    - objective:
    - files_expected_to_change:
    - tests_to_run:
    - acceptance_criteria:
    - constraints:
    - commit_message_template:
    - stop_conditions:

---

## 8. Review Append Standard

Each reviewer appends exactly one note per review round in this format:

    REVIEW_APPEND
    - reviewer: <model>
    - review_round: <n>
    - verdict: pass | pass_with_changes | blocked
    - confidence: high | medium | low
    - scope_check: pass | fail
    - safety_check: pass | fail
    - factuality_check: pass | fail
    - clarity_check: pass | fail
    - issues_found:
      1. ...
    - required_edits_before_build:
      1. ...
    - optional_improvements:
      1. ...
    - handoff_decision: relay_to_next_reviewer | relay_to_operator | blocked

---

## 9. Claude Code Build Packet

When consensus is reached, hand Claude Code only this stripped execution packet:

    CLAUDE_CODE_BUILD_PACKET

    REPO
    - repo: drop0ne/atticus-mpo
    - base_branch: release/stable
    - target_branch: <bugfix/...>

    AUTHORITY
    - writer_of_record: Claude Code
    - approved_by: Jake
    - consensus_status: APPROVED_FOR_BUILD

    OBJECTIVE
    - <single concrete objective>

    IN_SCOPE
    - ...

    OUT_OF_SCOPE
    - ...

    FILES_EXPECTED_TO_CHANGE
    - path/to/file1.py
    - path/to/file2.py

    REQUIRED_ACTIONS
    1. ...
    2. ...

    TEST_PLAN
    - command: ...

    ACCEPTANCE_CRITERIA
    - ...

    STOP_CONDITIONS
    - do not widen scope
    - do not rename unrelated files
    - do not edit docs unless listed
    - stop and report if hidden dependency blocks progress

    OUTPUT_FORMAT
    - summary
    - changed files
    - tests run
    - failures
    - diff notes
    - commit message proposal
    - PR summary draft

Claude Code should receive the normalized builder packet, not the full chat history.

---

## 10. Branching Discipline

- **Base branch:** `release/stable`
- **Task branches:**
  - `bugfix/<date>-<slug>`
  - `feature/<date>-<slug>`
  - `refactor/<date>-<slug>`
  - `test/<date>-<slug>`
  - `docs/<date>-<slug>`
  - `orchestration/<date>-<slug>`

Example: `bugfix/2026-04-05-worker-session-teardown`

---

## 11. Repo-Side Governance Files

Required minimum:

- `INDEX.md` — master entry point and documentation map
- `ORCHESTRATION.md` — this file
- `DEV_LIFECYCLE.md` — engineering rules, gates, and protected surfaces
- `WORK_LOG.md` — consolidated work history (append after every sprint)
- `core/packet_validator.py` — raw-text MPO v1.1 packet validator (`validate_packet(text: str) -> PacketValidationResult`)

Templates (in `templates/`):

- `templates/PACKET_TEMPLATE.md` — orchestration packet starting point
- `templates/BUILD_PACKET_TEMPLATE.md` — stripped builder execution packet
- `templates/REVIEW_APPEND_TEMPLATE.md` — reviewer note format
- `templates/WORK_LOG_ENTRY_TEMPLATE.md` — work log entry format
