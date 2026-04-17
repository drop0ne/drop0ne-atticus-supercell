# ATTICUS//LOCKED BUILDER PACKET

NAME: MPO_QUERY_AWARE_RETRIEVAL_RANKING_v1  
AUTHORITY: OPERATOR  
REPO: drop0ne/atticus-mpo  
BASE_BRANCH: release-candidate  
MODE: STRICT  
TASK_CLASS: runtime / retrieval / ranking

## Signal Intake

PR #99 merged the first context-carrying memory-cell upgrade into ATTICUS_MPO.
The next gap is retrieval quality: current ranking uses scope and tag richness with recency fallback, but does not yet consume explicit query, session-task, or packet-level relevance hints.

## Objective

Improve memory-cell retrieval quality so context injection can rank cells using stronger task-aware or query-aware relevance without losing boundedness or backward compatibility.

## Definition of Done

1. Retrieval ranking accepts higher-quality relevance hints from the call surface when available.
2. Ranking remains deterministic and bounded.
3. Existing behavior remains safe when no query/task hints are supplied.
4. Tests cover ranking behavior under both hinted and non-hinted paths.

## Required design direction

### Ranking inputs
Add optional ranking hints such as:
- active objective
- active packet id
- active branch or baseline
- query or prompt text
- scope preference

### Ranking behavior
Prefer cells by a weighted combination of:
- explicit query/task overlap
- scope fit
- tag overlap
- branch / baseline match
- recency fallback

### Boundedness
- preserve strong cap on injected cells
- preserve strong cap on injected characters
- do not emit full raw transcript dumps

## Likely implementation surfaces
- `services/context_injection.py`
- any higher-level seam that can pass query/task hints into context injection
- tests for ranking behavior and fallback safety

## Non-goals
- no semantic-vector system in this sprint unless explicitly authorized
- no unbounded retrieval growth
- no breaking change for callers that pass only session_id

## Acceptance checks
- hinted path ranks task-relevant cells above generic cells
- non-hinted path still behaves deterministically
- prompt injection remains bounded
- old callers remain compatible
