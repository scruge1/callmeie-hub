# Git Hooks

Tracked-in-repo hooks. Activate once per clone:

```bash
git config core.hooksPath .githooks
```

After that, `git commit` runs `pre-commit` which calls
`python scripts/inject-cohesion.py --check` and rejects the commit if any
HTML page has drifted from canonical partials.

To bypass once (only when you know what you're doing):

```bash
git commit --no-verify
```

Strongly discouraged for normal workflow — drift = next page also drifts.

## Hooks

| Hook | What it checks |
|---|---|
| `pre-commit` | Cohesion-layer drift (see `_partials/README.md`) |
