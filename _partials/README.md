# Cohesion Partials

HTML fragments injected into every callmeie.ie page by `scripts/inject-cohesion.py`.
Source of truth — DO NOT edit injected output in pages directly. Edit the partial here
and run `python scripts/inject-cohesion.py` to roll forward.

## Sentinel comment convention

Every page that participates in cohesion carries one or more of these marker pairs:

```html
<!-- COHESION:STRIP-START -->
  <!-- (auto-generated, do not edit) -->
<!-- COHESION:STRIP-END -->

<!-- COHESION:STRIP-START variant=pill -->
  <!-- (auto-generated, do not edit) -->
<!-- COHESION:STRIP-END -->

<!-- COHESION:BREADCRUMB-START section="Receptionist" section_url="/receptionist/" page="Dental" -->
  <!-- (auto-generated, do not edit) -->
<!-- COHESION:BREADCRUMB-END -->

<!-- COHESION:FOOTER-START -->
  <!-- (auto-generated, do not edit) -->
<!-- COHESION:FOOTER-END -->
```

Place sentinels where the rendered fragment should land. The script:

1. Walks every `*.html` under repo root (excluding `_partials/` and `node_modules/`).
2. For each sentinel pair, reads the matching partial file.
3. Substitutes placeholder tokens (`{{key}}`) using attributes parsed from the START sentinel (e.g. `section="Receptionist"`).
4. Writes the rendered fragment back between the sentinel markers, leaving the rest of the page untouched.
5. Idempotent — re-running with no upstream changes is a no-op.

## Variants

| Sentinel | Source partial |
|---|---|
| `STRIP` (default) | `_partials/cohesion-strip.html` |
| `STRIP variant=pill` | `_partials/cohesion-strip-pill.html` (demos + samples) |
| `BREADCRUMB` | `_partials/cohesion-breadcrumb.html` |
| `FOOTER` (default) | `_partials/cohesion-footer.html` |
| `FOOTER variant=demo` | `_partials/cohesion-footer-demo.html` (compact, demo pages) |

## Placeholder tokens

Tokens use `{{name}}` syntax inside partials. Values come from sentinel attributes.

| Token | Source | Default |
|---|---|---|
| `{{section}}` | `section="..."` attr | empty |
| `{{section_url}}` | `section_url="..."` attr | `/` |
| `{{page}}` | `page="..."` attr | (page title) |

## Drift detection

`scripts/inject-cohesion.py --check` walks every page, renders partials in-memory,
diffs against on-disk content. Non-zero exit if any page drifted from canonical
partial. Wired into pre-commit hook + `.github/workflows/cohesion.yml` CI check.

## When to NOT inject

Pages with no sentinels are skipped entirely. To opt a page out of cohesion:

- Don't add sentinels to the page (script ignores it)

To opt a page out of one specific partial but keep others (e.g. footer-only):

- Add only the sentinels you want; skip the rest

## Edge cases

- **Demos with bespoke aesthetic** — use `STRIP variant=pill` only, NO breadcrumb, NO universal footer. Their bespoke footer survives.
- **Parent hub `/` and `/about.html`** — NO strip (parent IS the hub). Use FOOTER only.
- **Root-relative URLs in partials** — partials use `/{path}` absolute URLs, not relative. Works because canonical domain is single.

## File layout

```
_partials/
├── README.md                         (this file)
├── cohesion-strip.html               (universal CallMeIE strip — sales + product pages)
├── cohesion-strip-pill.html          (minimal pill — demos + samples)
├── cohesion-breadcrumb.html          (3-segment breadcrumb)
├── cohesion-footer.html              (universal footer — sales + product pages)
└── cohesion-footer-demo.html         (compact footer — demos + samples)
```
