# Project-Local Supercell Instantiation Packet v1

Purpose: provide a single operator handoff artifact for creating a new project-local supercell in one pass.

---

## 1. Signal Intake

Fill these fields first:

- `project_name`:
- `source_repo`:
- `source_branch`:
- `project_supercell_repo`:
- `baseline_version`:
- `active_packet`:
- `current_known_state`:
- `active_next_step_focus`:

---

## 2. Authority Model

Use this authority split unless explicitly overridden:

- Source repo is authoritative for:
  - code
  - project-local primary docs
- Project-local supercell is authoritative for:
  - long-term memory
  - normalized current state
  - resume packets
- Global ATTICUS supercell remains authoritative for:
  - umbrella cross-project continuity

Core invariants:
- one project-local authority root
- compact context-bearing memory cells only
- mirrors summarize source canon and link back to it
- resume packets must be reproducible from current state and durable memory

---

## 3. Required Files

Create these minimum files and folders:

```text
PROJECTS/<project>/
├── README.md
├── CURRENT_STATE/
│   └── <project>_state.md
├── MEMORY/
│   └── cells/
│       └── <PROJECT>_BASELINE_v1.json
└── SESSION_PACKETS/
    └── generated/
        └── <project>_resume_<date>.md
```

---

## 4. Current State Template

Use this normalized state format:

```markdown
# <Project> Project State

Status: normalized current state

## Identity
- source_repo: `<owner/repo>`
- source_branch: `<branch>`
- project-local supercell scope: <project continuity>

## Current known state
- <baseline / milestone / branch / release / doctrine state>

## Active next-step focus
- <next step 1>
- <next step 2>

## Notes
This file is a normalized project-local state surface.
The source repo remains authoritative.
```

---

## 5. Baseline Memory Cell Template

Use this compact context-bearing baseline cell:

```json
{
  "cell_id": "<PROJECT>_BASELINE_v1",
  "domain": "<domain>",
  "project": "<project>",
  "title": "<Project> project-local baseline",
  "content": "<durable baseline summary>",
  "context_summary": "<compact restart-oriented summary>",
  "context_scope": "project",
  "context_tags": ["<tag1>", "<tag2>", "baseline"],
  "source_repo": "<owner/repo>",
  "source_ref": "<branch or ref>",
  "source_branch": "<branch>",
  "baseline_app_version": "<version or null>",
  "baseline_framework_version": "<framework version or umbrella context>",
  "parent_cell_id": "<parent or null>",
  "created_at": "<YYYY-MM-DD>",
  "updated_at": null,
  "provenance": {
    "origin": "project_local_instantiation"
  },
  "context_fingerprint": "<stable fingerprint>",
  "receipt_hash": null
}
```

Rule:
- do not use raw full-chat dumps by default
- preserve only durable, reusable, bounded context

---

## 6. Resume Packet Template

Use this compact project-local resume format:

```markdown
# <Project> Project Resume Packet

Generated: <YYYY-MM-DD>
Project: <project>
Scope: project-local continuity

## Identity
- source_repo: `<owner/repo>`
- source_branch: `<branch>`
- project-local supercell scope: <project continuity>

## Current State
- <current baseline summary>
- <recent merged milestone>
- <current next-step state>

## Relevant Memory Cells
- `<PROJECT>_BASELINE_v1`
  - project-local baseline

## Recommended Next Action
- <next action>
```

---

## 7. Creation Checklist

### Phase 1 — Identity and authority
- [ ] project_name set
- [ ] source_repo set
- [ ] source_branch set
- [ ] project_supercell_repo set
- [ ] authority boundary confirmed

### Phase 2 — Core files
- [ ] README created
- [ ] normalized current-state file created
- [ ] baseline memory cell created
- [ ] project-local resume packet created

### Phase 3 — Baseline normalization
- [ ] active branch recorded
- [ ] baseline version recorded
- [ ] current known state recorded
- [ ] active next-step focus recorded

### Phase 4 — Durable memory discipline
- [ ] compact context-bearing cells only
- [ ] provenance, scope, tags, lineage, and fingerprint included
- [ ] no raw full-chat dump by default

### Phase 5 — Resume readiness
- [ ] resume packet generated
- [ ] packet linked to durable cells
- [ ] recommended next action made explicit

---

## 8. Exit Criteria

The instantiation is complete when:
- the project can be resumed from the project-local supercell without full original chat replay
- authority boundaries are explicit
- the project-local supercell remains compatible with the global ATTICUS model

---

## 9. Operator Use Rule

Use this single file as the default operator handoff artifact for new project-local supercell creation unless a project requires a specialized override.
