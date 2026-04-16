# AMAS Spec Mirror State

Source repo: `drop0ne/amas-spec`  
Source branch: `main`

## Current normalized state

- AMAS is currently presented as **v2.0-draft**.
- The repo now explicitly separates:
  - governance core
  - runtime binding
  - conformance profiles
- The four-tier authority model remains:
  - CANONICAL
  - OPERATOR
  - SESSION
  - INFERRED
- The governance core now explicitly includes invariants for:
  - single canonical root
  - single writable truth ledger
  - explicit memory activation
  - hydrate immutability
  - provenance-gated activation
  - derived-artifact truth/read boundaries
  - repair/export discipline
  - sealed-memory durability

## Current roadmap status

- governance/core vs runtime-binding split: draft complete
- conformance-profile extraction with migration path: draft complete
- remaining future work includes:
  - conformance test suite
  - prompt injection resistance benchmark
  - arXiv preprint
  - multi-agent authority negotiation extension

## Mirror rule

This file is a normalized mirror for supercell use.
Source repo remains authoritative.
