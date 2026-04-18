# Quickstart

Status: active
Purpose: provide a very short cold-start entrypoint for any model or runtime loading the ATTICUS supercell for the first time.

---

## If you are starting cold

Read these 5 files in order:

1. `AUTHORITY.md`
2. `CURRENT_STATE/ACTIVE_RECEIPTS.md`
3. `CURRENT_STATE/CONTROL_PLANE_INDEX.md`
4. `CURRENT_STATE/ACTIVE_BASELINES.md`
5. `CURRENT_STATE/HYDRATOR_PROFILE.md`

Then stop.

Do not read deeper unless the task requires more.

---

## What this gives you

After those 5 files, you should know:

- what this repo is canonical for
- which receipt currently governs runtime behavior
- where the control-plane artifacts live
- what framework/runtime/schema/governance baselines are active
- what default hydrator posture to use

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
