# ATTICUS_CLAUDE_INIT_v1 — Runtime Hookup Next

## Objective

Hook up the merged `ATTICUS_CLAUDE_INIT_v1` package to an actual runtime selection and activation path.

## Why this is next

The package is merged into `main`, post-merge normalization is complete, and the highest-value next step is to make the selector usable by a runtime.

## Canonical runtime inputs

- `supercell/root_manifest.json`
- `supercell/selection_registry.json`
- `versions/index.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/version.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/activation.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/loader_contract.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/selection_resolver.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/activation_sequence.json`
- `versions/ATTICUS_CLAUDE_INIT_v1/validation_gate.json`

## Definition of done

- runtime resolves selector key `atticus_claude_init_v1`
- runtime loads the canonical cell and activation descriptor deterministically
- validation gate executes before activation
- activation sequence runs in documented order
- failure mode is fail-closed with explicit reason
- raw-preserved artifacts are not mutated

## Suggested deliverables

- loader entrypoint spec or code stub
- selector resolution routine
- validation gate executor
- activation sequence executor
- minimal runtime smoke-test notes

## Boundary

This handoff is for runtime hookup only.
Raw corpus internalization remains a separate later step.
