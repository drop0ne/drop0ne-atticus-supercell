# ATTICUS Supercell Runner Scaffold

Purpose: provide the first concrete runtime scaffold for ATTICUS supercell automation.

## Scope

This scaffold is intentionally minimal and non-mutating.
It is designed to:
- read current machine-readable pointers
- load current refresh/generator/validation inputs
- call phase hooks for refresh, generation, and validation
- perform basic live file-existence checks on required inputs and key schema pointers
- validate current runner inputs and the emitted execution record against repo JSON Schemas
- emit a machine-readable execution record with runtime-emission receipt fields and schema audit details

## File layout

```text
tools/runner/
├── README.md
├── main.py
├── schema_validate.py
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

## Expected default outputs

- `docs/AUTOMATION_RUNNER_EXECUTION_RECORD.generated.json`

## Local run recipe

From the repo root:

```bash
cd tools/runner
python3 main.py --repo-root ../.. --print-json
```

To write to a custom output path:

```bash
cd tools/runner
python3 main.py --repo-root ../.. --output docs/AUTOMATION_RUNNER_EXECUTION_RECORD.generated.json --print-json
```

## Current behavior

- execution-oriented
- non-mutating
- uses placeholder phase hooks for semantic phase summaries
- validates required input existence
- validates key schema-pointer existence
- performs built-in JSON Schema validation for `REFRESH_RUNNER_INPUT`, `SESSION_STATE_GENERATOR_INPUT`, `VALIDATION_REPORT`, and the emitted execution record
- emits `pass`, `warn`, or `fail` based on actual live path-check results, schema-check results, and phase-hook outcomes
- writes a runner execution record JSON
- includes `emitted_at`, `runner_version`, `repo_root`, and `output_path` so each execution record is self-describing as a runtime artifact
- includes `schema_checks` so validation outcomes remain machine-auditable in the emitted record

## Future expansion

Planned future upgrades:
- deeper JSON Schema coverage and parity with external validators
- deeper pointer and artifact integrity checks
- real refresh/generation/validation execution
- GitHub Action integration
- project-specific runner overrides
