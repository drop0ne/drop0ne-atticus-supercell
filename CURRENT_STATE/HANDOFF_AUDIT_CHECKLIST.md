# Handoff Audit Checklist

Status: active
Purpose: provide a short recurring audit pass specifically for ATTICUS supercell handoff surfaces so packet, quickstart, handoff modes, handoff examples, and related navigation remain aligned after repo changes.

---

## When to run

Run this checklist:
- after any change to active receipts or active baselines
- after any change to governance floor or handoff rules
- after any update to `CONTROL_PLANE_PACKET.md`
- after any update to `QUICKSTART.md`
- after any update to `HANDOFF_MODES.md` or `HANDOFF_EXAMPLES.md`
- before relying on the repo for direct model-to-model handoff after material changes

---

## Audit pass 1 — Packet alignment

Verify:
- `CURRENT_STATE/CONTROL_PLANE_PACKET.md` still reflects the current active receipt, active baselines, and current status
- the packet still declares `packet_first_direct_handoff`
- the packet still points to the correct next-hop escalation surfaces

Pass condition:
- packet summary and next-hop surfaces match current control-plane reality

---

## Audit pass 2 — Quickstart alignment

Verify:
- `CURRENT_STATE/QUICKSTART.md` still distinguishes packet-first handoff from standard compact cold-start
- quickstart escalation guidance still matches current handoff and boot surfaces
- quickstart does not outrank packet, baselines, or load-order surfaces

Pass condition:
- quickstart remains a valid compact expansion surface without drifting the handoff model

---

## Audit pass 3 — Handoff mode coherence

Verify:
- `CURRENT_STATE/HANDOFF_MODES.md` still names the supported handoff modes correctly
- each mode still points to the correct primary implementation surface
- companion surfaces listed for each mode remain correct

Pass condition:
- named handoff modes still map cleanly to real repo surfaces

---

## Audit pass 4 — Handoff examples coherence

Verify:
- `CURRENT_STATE/HANDOFF_EXAMPLES.md` still reflects current receipt, baseline, status, and authorization posture
- examples do not claim stronger authority than controlling surfaces
- examples still show the right stop points for each handoff mode

Pass condition:
- examples remain illustrative without laundering authority or collapsing drift

---

## Audit pass 5 — Index and navigation coherence

Verify:
- `CURRENT_STATE/CONTROL_PLANE_INDEX.md` still lists packet, quickstart, handoff modes, handoff examples, and handoff packet template accurately
- the index still marks `CONTROL_PLANE_PACKET.md` as the preferred direct handoff entry
- navigation text still uses the current handoff vocabulary consistently

Pass condition:
- handoff navigation remains discoverable and terminology-consistent

---

## Audit pass 6 — Template and regeneration readiness

Verify:
- `CURRENT_STATE/HANDOFF_PACKET_TEMPLATE.md` still matches the current packet structure
- if active receipt, baselines, or governance floor changed, the template still produces a correct packet shape
- normalization rules are still respected by packet-style summaries

Pass condition:
- maintainers could regenerate packet-style handoff surfaces without drifting governance meaning

---

## Audit outcomes

### PASS
Use when:
- all handoff surfaces are aligned with current controlling surfaces
- packet-first, compact, and full handoff paths remain coherent

### PARTIAL
Use when:
- small navigation or wording mismatches exist
- the handoff layer still works, but one or more dependent surfaces need refresh

### FAIL
Use when:
- packet, quickstart, handoff modes, examples, or index materially disagree about the supported handoff paths or active current-state posture
- the repo should not be relied on for clean handoff until repaired

---

## Minimum handoff audit report

Record at minimum:
- date
- auditor
- audit outcome: `PASS | PARTIAL | FAIL`
- handoff surfaces reviewed
- material mismatches found
- repair actions required

---

## Interpretation rule

This checklist is a handoff-specific audit aid.
If an active approved receipt, active baseline, or drift-preserved controlling surface conflicts with a stale handoff surface, the controlling surface wins and the handoff surface should be repaired.
