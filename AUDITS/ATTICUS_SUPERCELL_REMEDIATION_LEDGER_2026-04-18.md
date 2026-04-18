# ATTICUS Supercell Remediation Ledger — 2026-04-18

Status: active remediation plan  
Repository: `drop0ne/drop0ne-atticus-supercell`  
Depends on: `AUDITS/ATTICUS_SUPERCELL_ENCODING_GAP_LEDGER_2026-04-18.md`

---

## Purpose

Convert the quantified encoding-gap audit into an ordered remediation plan with explicit phases, gates, deliverables, and success criteria.

---

## Remediation objective

Advance the supercell from:
- strong **framework hydration / control-plane encoding**
- weak **deep corpus / internalization-plane encoding**

to:
- deterministic, internally consistent corpus state
- raw payload either fully embedded or formally declared externally canonical
- raw-file cells populated
- segment cells populated
- claim clusters populated

---

## Current baseline

### Completed already
- framework hydration surface is present
- source-canon mirrors are present
- selector / loader / release-control package scaffolding is present
- raw archive set is registered by metadata and hash
- partial raw chunk embedding has begun

### Open deficits
- ingress truth state drift
- incomplete raw corpus repo embedding
- no populated raw-file cells
- no populated segment cells
- no populated claim clusters

---

## Ordered remediation phases

### Phase 1A — Normalize ingress truth state
Priority: **P0**  
Status: **open**

#### Problem
Repo metadata disagrees on whether raw ingress has begun.

#### Affected artifacts
- `versions/ATTICUS_CLAUDE_INIT_v1/raw_ingress_plan.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/raw_chunks_manifest.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/raw_bundle_manifest.json`

#### Required decisions
Choose one truth state and propagate it consistently:

Option A:
- ingress is still planning-only
- remove or neutralize claims that real repo-backed chunk embedding has started

Option B:
- ingress has started
- update planning artifacts to reflect actual partial progress

#### Deliverables
- normalized ingress status fields
- one consistent statement of current ingress mode
- one consistent statement of whether chunk embedding is active
- updated DoD text aligned to real state

#### Definition of done
- all three artifacts agree on ingress state
- no artifact implies a different phase than the others
- current repo state is readable by future hydrators without ambiguity

#### Exit gate
- **Phase 1A PASS** when ingress-state contradiction is removed

---

### Phase 1B — Decide canonical raw payload strategy
Priority: **P0**  
Status: **open**

#### Problem
The repo currently mixes two models:
- external archive registration by hash/upload identity
- partial in-repo chunk embedding

This creates ambiguity about what counts as canonical deep-corpus storage.

#### Decision required
Pick one canonical path:

Path 1:
- **full repo-backed raw embedding** is canonical target
- continue chunked embedding until the full preserved payload is present in-repo

Path 2:
- **external archive registration** is canonical target
- stop implying that repo embedding is expected beyond metadata and minimal proof chunks

#### Deliverables
- updated policy note in `raw_bundle_manifest.json`
- updated policy note in `raw_archive_set_manifest.json`
- explicit sentence in release/hydration docs describing the canonical storage model

#### Definition of done
- future operators can answer “where is the authoritative raw corpus?” with one answer
- the repo no longer implies both models simultaneously without hierarchy

#### Exit gate
- **Phase 1B PASS** when raw storage model is unambiguous

---

### Phase 1C — Complete raw bundle embedding if repo-backed path is chosen
Priority: **P1**  
Conditional: only required if Phase 1B selects repo-backed raw embedding  
Status: **open / conditional**

#### Problem
Only a small prefix of the raw bundle is repo-backed today.

#### Current quantified state
- embedded bytes: `16,384`
- full bundle bytes: `194,228`
- completion: `8.4%`

#### Deliverables
- remaining chunk artifacts under `imports/ATTICUS_PASS7_2026_04_18/chunks/`
- normalized `raw_chunks_manifest.json`
- normalized `raw_bundle_manifest.json`
- checksum continuity verification against source SHA-256

#### Definition of done
- repo-backed chunk set reconstructs the preserved raw bundle deterministically
- manifests report complete embedding rather than partial embedding
- bundle lineage remains intact

#### Exit gate
- **Phase 1C PASS** when repo can deterministically reconstruct the full raw bundle

---

### Phase 2 — Populate raw-file cells
Priority: **P1**  
Status: **open**

#### Problem
`raw_cells_stub_index.json` defines intent for 348 raw-file cells, but none are populated.

#### Required outputs
- one raw-file cell per source raw file
- deterministic cell IDs using documented format
- provenance tags and source class
- raw/derived distinction preserved

#### Suggested target location
- `MEMORY/raw_cells/atticus_claude_init_v1/` or equivalent repo-approved namespace

#### Minimum fields per raw-file cell
- `cell_id`
- `source_bundle_sha256`
- `source_relative_path`
- `file_sha256`
- `payload_mode`
- `origin_class`
- `mutation=false`
- `content` or deterministic pointer to canonical embedded content

#### Definition of done
- populated raw-file cells: **348 / 348**
- every raw-file cell traceable to source bundle lineage
- `raw_cells_stub_index.json` superseded by a populated index or marked historical

#### Exit gate
- **Phase 2 PASS** when all raw files are internalized as cells or deterministic equivalents

---

### Phase 3 — Populate segment cells
Priority: **P2**  
Status: **open**

#### Problem
Segment-cell derivation is specified but not realized.

#### Required outputs
- segment cells derived from raw-file cells
- segment classes at minimum:
  - governance_spec
  - reasoning_stack
  - runtime_contract
  - lineage_provenance
- populated segment index

#### Rules
- additive projection only
- source mutation forbidden
- derived artifacts remain non-authoritative

#### Definition of done
- real segment cells exist in repo
- segment index reflects actual cells, not only a stub
- each segment cell links back to one or more raw-file cells

#### Exit gate
- **Phase 3 PASS** when segmentation is materialized and traceable

---

### Phase 4 — Populate claim clusters
Priority: **P2**  
Status: **open**

#### Problem
Claim-cluster projection is defined but empty.

#### Required outputs
- claim clusters derived from segment cells
- minimum domains:
  - governance
  - reasoning
  - safety
  - runtime
  - lineage
- populated cluster index
- links into semantic/dependency overlays where appropriate

#### Rules
- claim clusters are derived
- canonical truth remains with canonical cells and source mirrors
- unresolved conflicts must remain explicit

#### Definition of done
- real claim clusters exist in repo
- claim cluster index reflects actual populated clusters
- semantic/dependency overlays can reference real cluster products

#### Exit gate
- **Phase 4 PASS** when higher-order claim structure is present and wired

---

### Phase 5 — Refresh framework-hydration docs
Priority: **P2**  
Status: **open**

#### Problem
Once Phases 1–4 advance, current-state docs will understate actual completion or continue to describe scaffold-era limitations.

#### Affected docs
- `CURRENT_STATE/ATTICUS_FRAMEWORK_STATE_2026-04-17.md`
- `SESSION_PACKETS/ATTICUS_FRAMEWORK_BOOTSTRAP_PACKET.md`
- `SUPERCELL_LOAD_ORDER.md`
- `CURRENT_STATE/ACTIVE_BASELINES.md`
- `versions/ATTICUS_CLAUDE_INIT_v1/RELEASE_DOSSIER.md`

#### Deliverables
- updated completion language
- updated load-order notes
- explicit description of whether deep-corpus layers are hydrated from mirrors, raw cells, or higher-order projections

#### Definition of done
- boot docs match actual repo state
- no doc overstates or understates completion after remediation

#### Exit gate
- **Phase 5 PASS** when hydration docs match implementation reality

---

## Execution order

1. Phase 1A — normalize ingress truth state
2. Phase 1B — decide canonical raw storage model
3. Phase 1C — complete raw embedding if repo-backed path chosen
4. Phase 2 — populate raw-file cells
5. Phase 3 — populate segment cells
6. Phase 4 — populate claim clusters
7. Phase 5 — refresh boot/hydration docs

---

## Risk notes

### Risk 1 — Canonicality confusion
If external registration and repo embedding are both treated as primary without hierarchy, future hydrators may derive incompatible truth states.

### Risk 2 — Stub permanence
If stub indexes remain in place too long without populated replacements, the repo will look more complete than it is.

### Risk 3 — Overstatement in bootstrap docs
If current-state docs are not refreshed after deeper internalization, future nodes may either miss available depth or assume unsupported depth.

---

## Recommended operator path

Recommended path: **Phase 1A -> Phase 1B -> Phase 2**

Reason:
- first remove truth-state ambiguity
- then settle canonical raw storage model
- then move directly into raw-file cellization, which is the first major step that materially increases encoded framework depth

Confidence: **high**

---

## Minimal success condition

The minimum meaningful success state for this remediation cycle is:
- ingress truth state normalized
- canonical raw storage model decided
- raw-file cells materially populated

That would convert the repo from a mainly control-plane mirror into a genuine internalized corpus root.
