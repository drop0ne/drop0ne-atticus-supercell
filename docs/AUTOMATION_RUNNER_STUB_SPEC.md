# Automation Runner Stub Specification

Purpose: define the first execution-oriented automation runner stub for the ATTICUS supercell.

This stub does not yet execute repository mutations automatically. It defines the minimal control flow and machine-readable inputs required for a future script or GitHub Action to run a coherent maintenance + generation + validation cycle.

## 1. Objective

Consume the current supercell operating contracts and emit a reproducible run result for:
- refresh maintenance preparation
- session-state generation preparation
- validation preparation
- audit/report capture

## 2. Required runner inputs

The runner stub must consume these current artifacts:
- `CURRENT_REFRESH.json`
- `docs/REFRESH_RUNNER_INPUT.current.json`
- `docs/SESSION_STATE_GENERATOR_INPUT.current.json`
- `docs/SUPERCELL_VALIDATION_PROTOCOL.md`
- `docs/VALIDATION_REPORT.current.json`

Optional future inputs:
- project-specific refresh manifest
- project-specific generator input
- project-specific validation overrides

## 3. Canonical stub flow

Run in this order:
1. read `CURRENT_REFRESH.json`
2. resolve all current pointers needed for refresh/generation/validation
3. load the current refresh-runner input JSON
4. load the current session-state generator input JSON
5. load the current validation report and validation protocol
6. emit a runner execution record describing:
   - resolved inputs
   - current pointers used
   - target scope
   - next executable steps

## 4. Minimum stub outputs

A valid stub run should emit:
- `runner_run_id`
- `current_refresh_id`
- `resolved_inputs[]`
- `resolved_current_pointers[]`
- `planned_phases[]`
- `status`
- `notes`

## 5. Non-goals for the stub layer

- no repo mutations
- no automatic schema execution yet
- no automatic file existence checks yet
- no automatic PR or merge operations

This layer is a control-plane stub, not the final automation runner.

## 6. Success condition

The stub is successful when a future script can use it to deterministically discover:
- what inputs to load
- what pointers are current
- what phases to run next
- what outputs should be emitted later

## 7. Operating rule

Use this stub specification as the first automation runner contract until a real script or GitHub Action implementation replaces it.
