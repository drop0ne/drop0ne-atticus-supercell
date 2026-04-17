# ATTICUS//REFRESH_RUNNER_PACKET_v1

Purpose: define the first repeatable operator/automation packet for executing a coherent ATTICUS supercell refresh cycle.

## 1. Objective

Execute a refresh cycle that updates the ATTICUS supercell in one coherent pass after a merged source event, baseline shift, project-local instantiation, or authority-boundary change.

## 2. Inputs

Required inputs:
- `trigger_event`
- `source_repo`
- `source_branch`
- `refresh_scope`
- `affected_projects[]`
- `expected_current_resume_packets[]`
- `expected_current_baseline_cells[]`

Optional inputs:
- `merged_pr`
- `merged_commit`
- `active_packet`
- `follow_up_notes`

## 3. Canonical execution order

Run in this order:

1. validate source event landed
2. confirm active source baseline
3. update normalized mirrors
4. update affected current-state surfaces
5. add or supersede durable milestone cells if warranted
6. refresh resume packets if current restart surfaces changed
7. refresh lifecycle / registry / index files if pointers changed
8. write refresh receipt / log entry
9. update `CURRENT_REFRESH.json` if the umbrella current pointer changed

## 4. Minimum outputs

A valid refresh run should produce all affected outputs together:
- mirror summary or note
- current-state file updates
- durable cell updates if warranted
- resume packet updates if warranted
- index / registry / lifecycle updates if warranted
- refresh receipt/log entry
- current refresh pointer update if warranted

## 5. Stop conditions

Stop before completing the run if:
- source event is not actually landed
- source baseline is ambiguous
- refresh would create contradictory current pointers
- durable memory lacks provenance or scope
- resume packets would point to stale state

## 6. Result contract

At the end of a successful run, the following should all be true:
- current mirrors match landed source state
- current-state files reflect the intended baseline
- current resume packets point to valid restart surfaces
- current durable cells reflect the latest baseline/milestone state
- lifecycle / registry / indexes remain internally aligned
- `CURRENT_REFRESH.json` points to the latest valid umbrella maintenance state

## 7. Recommended future automation target

This packet is the first intended automation target for:
- GitHub Action or local runner
- manual operator refresh runs
- future ATTICUS_MPO supercell maintenance integration
