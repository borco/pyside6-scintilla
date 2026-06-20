# Setting up TestPyPI trusted publishing

## Why TestPyPI

[TestPyPI](https://test.pypi.org/) is a separate instance of the Python
Package Index, isolated from the real `pypi.org`. It exists so a publish
pipeline -- the GitHub Actions workflow, the trusted-publishing (OIDC)
wiring, the artifact-gathering steps, the package metadata -- can be
exercised end to end without:

- risking a botched or incomplete release landing on real PyPI (versions
  can't be re-uploaded once published, so mistakes are permanent there)
- needing a separate throwaway project name on real PyPI just to test
  plumbing

It's a tracer-bullet step: verify the whole pipeline against TestPyPI first,
then point the same pattern at real PyPI with confidence. This is
[the approach recommended by the Python Packaging
Guide](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)
for GitHub Actions-based publishing.

[Trusted publishing](https://docs.pypi.org/trusted-publishers/) means the
workflow authenticates to PyPI/TestPyPI via short-lived GitHub OIDC tokens
instead of a long-lived API token stored as a repo secret -- nothing to
rotate, leak, or scope too broadly.

## Prerequisites

- A GitHub repo with a release-publishing workflow (`publish.yml`) that
  builds an sdist/wheels and uploads them with
  [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish).
- Accounts on both <https://test.pypi.org/account/register/> and
  <https://pypi.org/account/register/> -- these are independent accounts,
  registering on one doesn't create the other.
- The `lexilla` package name available (or already owned by you) on
  TestPyPI. TestPyPI's namespace is independent of pypi.org's, so a name
  claimed on real PyPI is *not* automatically reserved on TestPyPI.

## Step-by-step setup

### 1. Create a GitHub environment for TestPyPI

In the repo: **Settings → Environments → New environment**, name it
`testpypi` (must match the workflow's `environment:` block and the
trusted-publisher config in step 2). No protection rules are needed for a
personal project -- the environment mainly exists here to scope the
trusted-publisher binding to a specific job.

Repeat later for `pypi` (real PyPI) once the TestPyPI tracer is verified.

### 2. Add a *pending* trusted publisher on test.pypi.org

Trusted publishers can be registered **before the project exists** on
TestPyPI -- this is a "pending" publisher, and TestPyPI creates the project
automatically on the first successful publish from a matching workflow run.

Go to <https://test.pypi.org/manage/account/publishing/> and fill in:

| Field | Value |
| --- | --- |
| PyPI project name | `lexilla` |
| Owner | `borco` |
| Repository name | `lexilla-py` |
| Workflow filename | `publish.yml` (just the filename, no path) |
| Environment name | `testpypi` (must match step 1) |

### 3. Wire up the workflow job

Already done in `.github/workflows/publish.yml`'s `publish-testpypi` job --
it has `environment: testpypi`, `permissions: id-token: write`, downloads
the sdist/wheels into `dist/`, and uploads via
`pypa/gh-action-pypi-publish@release/v1` with
`repository-url: https://test.pypi.org/legacy/`.

### 4. Trigger a tracer run

`release: types: [published]` is only invocable for an actual GitHub
Release. To verify the pipeline *before* cutting a real release (and from a
non-default branch, since `workflow_dispatch` is only invocable on the
default branch), add a temporary trigger -- either `workflow_dispatch:` (if
already on the default branch) or a branch-scoped `push:` trigger:

```yaml
on:
  release:
    types: [published]
  workflow_dispatch:
  # Temporary: verify the TestPyPI tracer on this branch before merge.
  # Remove once verified.
  push:
    branches: [your-feature-branch]
```

Push and watch the run. Confirm:

- the build/upload jobs succeed
- `publish-testpypi` succeeds and the environment's `url:` link in the run
  summary resolves to the new project page on test.pypi.org

### 5. Smoke-test the install

TestPyPI doesn't host most dependencies, so install with TestPyPI as the
primary index and real PyPI as a fallback for everything else, in a
throwaway venv:

```bash
pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  lexilla==X.Y.Z.N
python -c "import lexilla"
```

### 6. Remove the temporary trigger

Once the tracer is verified, remove the temporary `workflow_dispatch:`/
`push:` trigger added in step 4, leaving only `release: types: [published]`
(plus `workflow_dispatch:` if you want it as a permanent manual-trigger
option).

## Gating real PyPI on TestPyPI success

`.github/workflows/publish.yml`'s `publish-pypi` job `needs:
publish-testpypi` and is gated `if: github.event_name == 'release'`, so
tracer runs (via `workflow_dispatch` or the temporary `push` trigger) only
ever reach TestPyPI -- real PyPI is only touched by an actual GitHub
Release.

## Moving to real PyPI

Once TestPyPI is green end to end:

1. Create the `pypi` GitHub environment (step 1, same process).
2. On <https://pypi.org/manage/account/publishing/>, add a trusted publisher
   with the same fields as step 2 but `environment name: pypi`. If the
   project already exists on real PyPI (e.g. a placeholder release), this is
   added under that project's **Settings → Publishing** instead of the
   pending-publisher flow.
3. Cut a real GitHub Release matching the version being published -- this
   triggers `release: types: [published]`, which runs both
   `publish-testpypi` and (gated) `publish-pypi`.

## Gotchas

- TestPyPI and real PyPI are **completely separate**: separate accounts,
  separate project namespaces, separate trusted-publisher configs. Setting
  one up does nothing for the other.
- `workflow_dispatch` can only be triggered from the repo's **default
  branch** -- for tracer runs on a feature branch, use a temporary
  branch-scoped `push:` trigger instead (and remove it afterward).
- Pending trusted publishers create the project on TestPyPI/PyPI on first
  successful publish -- no need to manually create the project first.
- `repository-url: https://test.pypi.org/legacy/` is TestPyPI-specific; omit
  `repository-url` for real PyPI (it defaults to `pypi.org`).
