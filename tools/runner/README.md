# ATTICUS Supercell Runner Scaffold

Purpose: provide the first concrete runtime scaffold for ATTICUS supercell automation.

## Scope

This scaffold is intentionally minimal and non-mutating.
It is designed to:
- read current machine-readable pointers
- load current refresh/generator/validation inputs
- call phase hooks for refresh, generation, and validation
- emit a machine-readable execution record

## File layout

```text
tools/runner/
├── README.md
├── main.py
└── phases/
    ├── __init__.py
    ├── refresh.py
    ├── generate.py
    └── validate.py
```

## Expected default inputs

- `CURRENT_REFRESH.json`
- `docs/REFRESH_RUNNER_INPUT.current.json`
- `docs/SESSION_STATE_GENERATOR_INPUT.current.json`
- `docs/VALIDATION_REPORT.current.json`

## Expected default output

- `docs/AUTOMATION_RUNNER_EXECUTION_RECORD.generated.json`

## Current behavior

- execution-oriented
- non-mutating
- uses placeholder phase hooks
- emits a runner execution record JSON

## Future expansion

Planned future upgrades:
- real schema validation
- real pointer existence checks
- real refresh/generation/validation execution
- GitHub Action integration
- project-specific runner overrides
