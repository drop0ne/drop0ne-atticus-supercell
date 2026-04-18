# Quickstart

Status: active
Purpose: provide a very short cold-start entrypoint for any model or runtime loading the ATTICUS supercell for the first time.

---

## Fastest handoff option

If another model or runtime is being handed into this repo and needs the smallest possible first read:

1. `CURRENT_STATE/CONTROL_PLANE_PACKET.md`

Then stop unless the task requires more.

Use this when:
- the task is simple
- the goal is fast orientation
- the next model only needs the active receipt, active baselines, current status, quickstart rule, and load-order pointer

---

## Standard cold-start option

If you are starting cold and need the normal compact orientation path, read these 5 files in order:

1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`

Then stop.

Do not read deeper unless the task requires more.

---

## What this gives you

After the standard 5-file path, you should know:

- what this repo is canonical for
- which receipt currently governs runtime behavior
- where the control-plane artifacts live
- what framework/runtime/schema/governance baselines are active
- what default hydrator posture to use

After the packet-first path, you should know the minimum current handoff state and where to escalate next if needed.

---

## If you need more after that

Use:
- `SUPERCELL_LOAD_ORDER.md` for deterministic boot order
- `CURRENT_STATE/TASK_ROUTING_MATRIX.md` to choose the minimum escalation level
- `CURRENT_STATE/QUERY_CHECKLIST.md` before answering or escalating
- `CURRENT_STATE/BOOT_ASSERTIONS.md` and `CURRENT_STATE/BOOT_REPORT_TEMPLATE.md` for boot validation/reporting

---

## Default stop rule

Remain in read-only hydrate mode unless a valid receipt, explicit activation expectation, and explicit preflight expectation justify deeper mutation-capable interpretation.
