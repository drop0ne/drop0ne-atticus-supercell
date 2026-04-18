# Contributing

## Repo role

This repository is a maintainer-controlled ATTICUS supercell reference surface.
It is designed to preserve a clear canonical root, explicit authority boundaries, and machine-readable continuity artifacts.

## Contribution posture

Contributions should be narrow, explicit, and governance-aware.
Do not treat this repository like an unrestricted general-purpose collaboration surface.

## Before proposing changes

Check the following first:

- `README.md`
- `AUTHORITY.md`
- `SUPERCELL_SPEC.md`
- `SESSION_BOOTSTRAP.md`
- `CURRENT_REFRESH.json`
- `docs/PUBLIC_RELEASE_SETTINGS_HANDOFF.md`

## Rules for changes

1. Preserve canonicality.
   - Do not create ambiguity about what is current.
2. Preserve provenance.
   - Do not silently rewrite the meaning of existing durable artifacts.
3. Preserve labeling discipline.
   - Seeded, example, current, and generated artifacts must stay clearly labeled.
4. Keep scope bounded.
   - Avoid mixing architecture redesign with small hygiene changes.
5. Prefer additive, reviewable changes.
   - Small PRs are preferred.

## Types of acceptable changes

- documentation corrections
- schema improvements
- validation hardening
- labeling clarity
- runner hardening
- workflow / CI improvements
- authority-boundary clarifications

## Changes that require extra caution

- changing canonical pointers
- changing baseline cells
- changing registry/index meaning
- changing authority rules
- changing artifact lifecycle semantics
- changing public/private posture wording

## Pull request expectations

A good PR should include:

- a short objective
- exact files changed
- whether the change is docs-only, schema-only, workflow-only, or runtime-affecting
- any canonicality impact
- any public-surface impact

## Maintainer authority

The maintainer retains final authority over canonical-surface changes.
Code-owner review should be treated as mandatory where branch protection supports it.
