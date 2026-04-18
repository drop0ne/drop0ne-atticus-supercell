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

## Claude cowork execution instructions

Use this section as the direct execution brief.

### Mission

Finish the GitHub UI settings that cannot be changed from inside the repository.
Do not redesign the repo. Do not broaden scope.

### Required actions

1. In repo settings, set feature posture intentionally:
   - Wiki: OFF
   - Discussions: OFF unless explicitly needed
   - Projects: OFF unless actively needed
   - Issues: OFF by default for a read-mostly canonical repo, unless public issue intake is intentionally wanted

2. In merge settings, prefer a curated history:
   - Squash merge: ON
   - Merge commits: OFF if available
   - Rebase merge: OFF unless there is a reason to keep it

3. In branch protection or rulesets for `main`, enable best-available enforcement:
   - require pull requests
   - require at least 1 approval
   - require code owner review
   - dismiss stale approvals
   - require conversation resolution
   - block force-push
   - block branch deletion
   - restrict direct push to maintainer only if supported

4. In Actions / status checks:
   - ensure Actions is enabled as needed
   - if supported, require the validation workflow from `.github/workflows/validate-supercell.yml`
   - if the workflow check is not yet selectable, report that as pending rather than guessing

5. Only after all prior items are verified:
   - change visibility from private to public

### Verification report format

Report each item as `pass`, `fail`, or `unavailable`.

Return a final note in this structure:

- Completed
- Unavailable in current repo type
- Still pending
- Visibility state
- Main protection state
- Recommended next action

### Stop conditions

Stop and report if:

- expected controls do not exist for this repo type
- visibility is changed before `main` protection is applied
- a setting cannot be verified after changing it

## Operator reply for Claude

Use this exact response if Claude asks what path to take:

- Choose **Path 2 — Execute the brief**.
- You are the intended executor.
- The repository is `drop0ne/drop0ne-atticus-supercell`.
- The handoff doc to follow is this file: `docs/PUBLIC_RELEASE_SETTINGS_HANDOFF.md`.
- Treat this file as the authoritative execution brief.
- Do not ask to redesign the repo.
- Do not broaden scope.
- Apply the GitHub UI settings using the required actions and stop conditions above.
- Verify each setting and return the verification report in the requested format.
- If a control is unavailable in a personal-user-owned repo, mark it `unavailable` rather than guessing.
- Do not flip visibility to public until `main` protection is in place and verified.
