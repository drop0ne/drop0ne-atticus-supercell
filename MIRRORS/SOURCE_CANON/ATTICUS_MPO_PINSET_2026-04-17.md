# ATTICUS MPO Pinset — 2026-04-17

Pinned source repo: `drop0ne/atticus-mpo`
Mirror purpose: preserve the runtime/product governance and architecture surfaces referenced by the ATTICUS framework mirror.

---

## Pinned source: `INDEX.md`
Source ref: `release-candidate`
Blob SHA: `21c790bc26b481ee66d2b914fcf5e42a3998de81`

### Snapshot excerpt
- Declares ATTICUS MPO as a governed desktop orchestrator for multi-provider AI workflows.
- Current baseline shown in source: v5.0.1 / ATTICUS v6.4.1-HCII.
- Establishes documentation reading order and role table.
- Preserves the four-layer single-writer orchestration pipeline.

---

## Pinned source: `ORCHESTRATION.md`
Source ref: `release-candidate`
Blob SHA: `4e80860fc0da551e063a289cfef1a205a0073956`

### Snapshot excerpt
- Operator Jake is final authority.
- Claude Code is sole repository writer.
- Canonical scaffold remains:
  [Signal Intake] [Plan & DoD] [Execution] [Verification] [Final] [Backlog / Next]
- Defines consensus policy, packet lifecycle, review append standard, and builder packet format.
- Separates Claude review surface from Claude build surface.

---

## Pinned source: `ARCHITECTURE.md`
Source ref: `release-candidate`
Blob SHA: `d139cef22c6c2d7eaad8aed1b9dc5910afed222f`

### Snapshot excerpt
- Runtime baseline shown in source: v5.0.0b6 / schema v8 / ATTICUS v6.4.1-HCII.
- WorkerSession is the active execution model.
- TranscriptManager is the authoritative in-memory transcript source of truth.
- Providers: OpenAI, Anthropic, Gemini, Ollama.
- Memory system: 27 builtin cells, 7 packs.

---

## Mirror boundary
These are pinned local mirror anchors for future hydration.
They preserve the source identity and read path even if upstream docs move.
