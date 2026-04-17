# Supersession and Archival Policy

Purpose: define how the ATTICUS supercell distinguishes among artifacts that are current, superseded, archived, or retired.

## 1. Scope

Apply this policy to:
- durable memory cells
- resume packets
- project-local baseline cells
- machine-readable indexes and registries when they reference current artifacts

## 2. Lifecycle states

### current
The artifact is the active canonical pointer for its role.
Examples:
- latest resume packet for a project
- latest baseline cell for a project
- latest umbrella working-baseline cell

### superseded
The artifact remains historically valid but is no longer the active current pointer because a newer artifact for the same role replaced it.
Examples:
- an older resume packet replaced by a newer packet
- a prior baseline cell replaced by a new baseline cell

### archived
The artifact is intentionally preserved for history or audit purposes but is no longer part of normal current traversal.
Examples:
- old milestone packets kept for reference
- deprecated lifecycle notes retained for audit continuity

### retired
The artifact should no longer be used operationally and is retained only for minimal historical trace or should be removed from active indexes entirely.
Examples:
- invalidated starter artifacts replaced by a new contract
- old experimental files no longer suitable for reuse

## 3. Canonical rules

- Only one artifact should be marked `current` for a given project-role combination unless an explicit multi-current exception is documented.
- Superseded artifacts may remain in the repo, but indexes and registries must not point to them as current.
- Archived artifacts may remain linked from lifecycle or audit surfaces but should not be traversed as default restart surfaces.
- Retired artifacts should be excluded from current registries and indexes.

## 4. Trigger conditions

Mark an artifact as superseded when:
- a newer artifact becomes the active pointer for the same role
- a project baseline is replaced
- a project resume packet is replaced
- an umbrella working-baseline artifact is replaced

Mark an artifact as archived when:
- it is kept for audit/history only
- it should remain discoverable but not current

Mark an artifact as retired when:
- it should no longer be used operationally
- it is intentionally removed from current discovery paths

## 5. Update requirements

When an artifact changes lifecycle state:
- update relevant current pointer files
- update indexes and registries if current pointers changed
- update lifecycle or refresh logs when the change is material
- avoid silent current/superseded contradictions

## 6. Operating rule

Use this policy as the default artifact lifecycle rule for the ATTICUS supercell unless a project-local policy explicitly narrows it.
