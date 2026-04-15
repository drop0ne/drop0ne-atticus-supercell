# Session Bootstrap

## Goal

Generate a bounded session-state packet that can be handed to ChatGPT, Gemini, Claude, or ATTICUS_MPO so work can resume with the needed context.

## Minimum packet contents

- repo identity
- current framework state
- current MPO state
- active branch / baseline
- current sprint or packet
- unresolved blockers
- selected relevant memory-cell summaries
- mirror timestamps / source refs
- recommended next action

## Generation rule

Bootstrap packets should prefer compact state summaries and linked memory cells over dumping entire raw histories.

## Output targets

- cross-model human-readable resume packet
- machine-readable bootstrap packet
- project-scoped packet variants when needed
