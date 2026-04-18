# Public Release Settings Handoff

## Objective

Prepare this repository to be a public, read-mostly reference example of AMAS / ATTICUS supercell governance while keeping `main` maintainer-controlled.

## Current facts

- Repo: `drop0ne/drop0ne-atticus-supercell`
- Owner type: personal user account
- Current visibility: private
- Default branch: `main`
- `CODEOWNERS` now assigns all paths to `@drop0ne`

## Important limitation

This is a personal-user-owned repo, not an organization-owned repo. Team-scoped controls are weaker here than they would be in an org.

Long-term preferred path if team-only governance is required:

- create a GitHub organization
- transfer this repo into the organization
- create a maintainers/admin team
- apply rulesets there

## Recommended GitHub UI settings

### Visibility

- Make the repo public only after the checklist below passes.

### Features

Recommended for a read-mostly canonical reference repo:

- Issues: disable unless public issue intake is desired
- Discussions: disable unless public discussion is desired
- Wiki: disable
- Projects: optional; usually disable for this repo type
- Forking: set to the most restrictive allowed option if such a control exists, but do not assume this prevents copying or mirroring

### Pull requests / merge policy for `main`

- Require pull requests before merge
- Require at least 1 approval
- Require review from code owners
- Dismiss stale approvals when new commits are pushed
- Require conversation resolution before merge
- Restrict direct pushes to maintainers only
- Disallow force pushes
- Disallow deletion of protected branches
- Prefer squash merge only
- Disable merge commits if you want a linear curated history

### Actions / validation

- If a minimal validation workflow exists, require it on `main`
- If no workflow exists yet, do not pretend there is CI enforcement

## Public wording

Describe the repo publicly as:

- prototype
- reference implementation
- active development
- canonical for this repo surface

Do not describe it as:

- production-hardened autonomous memory system
- impossible to fork or copy once public

## Recommended follow-up files

- `SECURITY.md`
- `CONTRIBUTING.md`
- minimal GitHub Action for non-mutating validation

## Checklist before making public

- [ ] README wording is accurate
- [ ] AUTHORITY.md still matches repo role
- [ ] seeded/example artifacts are clearly labeled
- [ ] CURRENT_REFRESH.json points only to real current files
- [ ] branch protection / rulesets for `main` are configured
- [ ] merge method policy is configured
- [ ] feature toggles are intentionally chosen
- [ ] public wording does not overclaim maturity

## Execution order

1. Verify wording and artifact labels
2. Configure `main` protection / rulesets
3. Configure feature toggles
4. Add minimal CI if desired
5. Re-check seeded vs runtime-generated artifacts
6. Only then flip visibility to public
