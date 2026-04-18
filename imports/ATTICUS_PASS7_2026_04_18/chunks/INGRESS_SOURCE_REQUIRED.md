# ATTICUS PASS7 Ingress — Source Required

## Status

Further raw corpus ingress beyond the currently committed chunk artifacts must not proceed blindly.

## Reason

To truthfully continue Phase 1A, the preserved source payload used for ATTICUS full-load ingress must be available to the operator/runtime performing the embedding step.

Required source artifact:
- preserved ATTICUS raw import bundle or deterministic chunk source equivalent
- expected source lineage sha256: `9e411ccd4b445b33b7854115669afae786fbcfc78a2850750f435a9940f90357`

## Constraint

Without the real source payload, additional chunk files cannot be verified as authentic representations of the preserved corpus.

## Next correct action

1. Provide the preserved ATTICUS bundle or deterministic chunk source to the ingest workflow.
2. Verify bundle hash against the expected source lineage sha.
3. Continue chunked repo ingress with verified chunk artifacts only.
4. Normalize `versions/ATTICUS_CLAUDE_INIT_v1/raw_bundle_manifest.json` after verified ingress reaches the required threshold.

## Integrity rule

- no silent substitution
- no guessed chunk payloads
- no mutation of canonical artifacts
- append-only verified ingress only
