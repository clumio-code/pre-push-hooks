pre-push-hooks
================

Some out-of-the-box hooks for pre-push.

See also: https://github.com/clumio-oss/pre-commit


### Using pre-push-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/clumio-oss/pre-push-hooks
    rev: v1.0.0 # use the release tag from github
    hooks:
    -   id: check-branch-for-push
        args: ['--pattern', '^testbranch.*']
    ...
```

### Hooks available

#### `no-push-to-branch`
Protect specific branches from direct checkins.
  - `-p` / `--pattern` can be used to protect branches that match a supplied regex
    (e.g. `--pattern, release/.*`). May be specified multiple times.
