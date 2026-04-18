# Normalization Rules

Status: active
Purpose: define what kinds of normalization are allowed for ATTICUS supercell summaries and indexes, and what kinds are forbidden because they would collapse drift, erase history, or outrank controlling governance surfaces.

---

## 1. Why normalization rules exist

The control plane contains many compact surfaces:
- indexes
- summaries
- status pages
- quickstart surfaces
- examples
- reports

These are useful only if they remain subordinate to controlling surfaces.
Normalization is allowed when it improves navigation or readability without changing governance meaning.
Normalization is forbidden when it would silently change what is true, settled, or authorized.

---

## 2. Allowed normalization

Allowed normalization includes:

### A. Navigation compression
You may summarize where things live and what they are for.
Examples:
- index pages
- quickstart pages
- one-page maps

### B. Compact current-state summaries
You may summarize active current-state interpretation when it is clearly sourced from controlling surfaces.
Examples:
- active baselines
- control-plane status
- boot reports

### C. Example simplification
You may simplify worked examples for readability, provided they do not claim stronger authority than the controlling surfaces.

### D. Reporting condensation
You may condense audit or boot outcomes into structured templates, provided material uncertainty and drift are still represented.

### E. Terminology harmonization
You may standardize naming for readability when meaning does not change.
Example:
- consistently referring to the active governance floor as `explicit rehydration-safe`

---

## 3. Forbidden normalization

Forbidden normalization includes:

### F1. Drift collapse
Do not summarize unresolved drift as though it were resolved.
If a mismatch or ambiguity remains active, summaries must preserve that fact.

### F2. History erasure
Do not remove or silently overwrite dated receipts, dated reports, drift entries, or dated state artifacts when they still matter for audit and provenance.

### F3. Receipt laundering
Do not let a summary, example, quickstart, or status page imply authority that only an active approved receipt can provide.

### F4. Certainty inflation
Do not restate ambiguous or conditional governance as unconditional.
If something is conditional, summaries must preserve the condition.

### F5. Mode overreach
Do not let compact mode summaries imply permissions or conclusions that require full control-plane boot or deeper source review.

### F6. Example promotion
Do not let examples or templates become de facto controlling doctrine.
Examples illustrate use; they do not define active interpretation.

### F7. Silent canonicality laundering
Do not rewrite summary surfaces so that non-canonical mirrors, examples, or history artifacts appear to be the canonical controlling layer.

---

## 4. Normalization priority order

When deciding whether a normalization is safe, use this priority order:
1. higher-tier platform safety
2. active approved receipts relevant to scope
3. active baselines
4. drift-preserved controlling surfaces
5. deterministic boot and routing surfaces
6. summaries, indexes, examples, templates, and reports

A lower-priority surface may summarize a higher-priority surface, but it must not silently override it.

---

## 5. Practical tests

Before normalizing a surface, ask:
- does this remove a live ambiguity?
- does this hide drift?
- does this erase history that still matters?
- does this make a conditional rule sound unconditional?
- does this make a summary look stronger than the receipt or baseline it came from?

If the answer to any is yes, the normalization is not safe.

---

## 6. Allowed wording patterns

Safe wording examples:
- `version-mismatch-preserved`
- `conditionally blocked`
- `active receipt governs this scope`
- `read-only unless explicit activation and preflight are present`
- `unknown pending controlling artifact`

These preserve the actual state of certainty and authorization.

---

## 7. Required follow-up when normalization-relevant changes occur

If a controlling receipt, active baseline, or drift state changes:
- review summary surfaces
- update them only after controlling surfaces are correct
- preserve explicit mention of any still-live conditions or drift
- log material summary changes in the changelog when appropriate

---

## Interpretation rule

These rules govern summary and index discipline.
If an active approved receipt, active baseline, or drift-preserved controlling surface conflicts with a normalized summary, the controlling surface wins and the summary should be repaired.
