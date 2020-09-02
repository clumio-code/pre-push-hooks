[![Build Status](https://asottile.visualstudio.com/asottile/_apis/build/status/pre-commit.pre-commit-hooks?branchName=master)](https://asottile.visualstudio.com/asottile/_build/latest?definitionId=17&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/17/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=17&branchName=master)

pre-push-hooks
================

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/surafelabebe/pre-push-hooks
    rev: v1.0.0 # use the release tag from github
    hooks:
    -   id: no-push-to-branch
        args: ['--pattern', '^testbranch.*']
    ...
```

### Hooks available

#### `no-push-to-branch`
Protect specific branches from direct checkins.
  - Use `args: [--branch, staging, --branch, master]` to set the branch.
    `master` is the default if no branch argument is set.
  - `-b` / `--branch` may be specified multiple times to protect multiple
    branches.
  - `-p` / `--pattern` can be used to protect branches that match a supplied regex
    (e.g. `--pattern, release/.*`). May be specified multiple times.

Note that `no-push-to-branch` is configured by default to [`always_run`](https://pre-commit.com/#config-always_run).
As a result, it will ignore any setting of [`files`](https://pre-commit.com/#config-files),
[`exclude`](https://pre-commit.com/#config-exclude), [`types`](https://pre-commit.com/#config-types)
or [`exclude_types`](https://pre-commit.com/#config-exclude_types).
Set [`always_run: false`](https://pre-commit.com/#config-always_run) to allow this hook to be skipped according to these
file filters. Caveat: In this configuration, empty commits (`git commit --allow-empty`) would always be allowed by this hook.

### As a standalone package

If you'd like to use these hooks, they're also available as a standalone package.

Simply `pip install pre-push-hooks`
