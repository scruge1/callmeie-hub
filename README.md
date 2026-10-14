# callmeie-hub

Public brand site for **CallMeIE**, currently operated by **Adam Vaughan trading as CallMeIE**. The brand is not itself a separate legal person. Historical company references do not identify the current supplier.
This repo serves the apex domain `callmeie.ie` via GitHub Pages.

- **Live**: https://callmeie.ie
- **Hosting**: GitHub Pages, `main` branch, `/` root
- **DNS**: Cloudflare (NS swap from GoDaddy 2026-05-03) → GitHub Pages anycast
- **Domain registrar**: GoDaddy (callmeie.ie)
- **CDN / 301s**: Cloudflare Bulk Redirects (post-cutover)
- **Custom domain**: `CNAME` file at repo root

## Brand contract

The site follows [DESIGN.md](DESIGN.md) and preserves the original `6578619`
design. Irish AI phone reception is the main offer; websites are secondary.
This cleanup shortens copy, standardises supporting typography, repairs actual
demo thumbnails and corrects alignment while keeping the original layouts.

- Original warm paper, ink and Fraunces display headings
- Inter for company supporting text; distinct demo art direction remains
- Existing graphic logo and burgundy accents across parent pages
- No new generated imagery or 3D in this pass

Scoped cleanup styling is in `cleanup.css`; shared HTML is in `_partials/`.
Run `python scripts/inject-cohesion.py` after changing a partial, then use its
`--check` mode. Private browser captures stay outside Git.

Push-to-talk is specified in
[the integration plan](reports/push-to-talk-integration-plan-20261011.md).
Its local browser control and backend bridge are now built and tested against
an isolated HTTP fixture. Public configuration remains disabled. The existing
voice/tracking owners are reused; real provider/media acceptance remains open.
See [the build receipt](reports/push-to-talk-build-20261011.md) and
ACTIVE-CHECKPOINT.md for scope, source and acceptance boundaries.

## Original design cleanup — 11 October 2026

The original cleanup is published as `5f42901`. Adam's new screenshots require
label, phone, footer, logo and colour corrections. This branch also refreshes
the player with three fictional call types using current V4 Turbo voices.
Release `d63bf9e` is live. Pages, cohesion and235 exact served-file checks pass;
bounded live visual/audio checks pass. ACTIVE-CHECKPOINT.md owns the evidence.
All 228 browser source and asset files are pinned to the candidate that passed
320 browser cases across all80 content pages. [ACTIVE-CHECKPOINT.md](ACTIVE-CHECKPOINT.md)
owns current verification and publication state; see the
[cleanup report](reports/original-cleanup-20261011.md) and
[publication report](reports/original-cleanup-publication-20261011.md).

## Previous craft pass — historical

The `06dcc58` craft release was owner-rejected and is superseded by the original
design cleanup. Recovered requirements and comparisons remain in
[the history report](reports/design-direction-history-20261010.md) and
[the design review](reports/design-comparison-20261010.md).

## Previous published correction — 10 October 2026

The previous GN house-style restoration is historical and was superseded by the craft release.
Source release: `adc21bc5b8cb04b6ab4294b9362700d92c522a1c`. GitHub Pages and cohesion checks succeeded.
All80 content pages have mobile/desktop visual coverage; the final runtime matrix
and shared-header checks passed. Actual live checks confirm the fonts, artwork
and working gallery previews. See ACTIVE-CHECKPOINT.md and
reports/site-brand-restoration-20261010.md for evidence and limits.

## First consolidation — historical publication

Adam rejected the first published design as basic and off-brand. The subsequent
GN correction was also superseded by the original-design cleanup; see DESIGN.md.
The original publication below remains historical evidence, not design acceptance.

Branch `review/site-consolidation-20261010` starts from published commit
`657861961e8297853a2c6e62c6c453c56488f159`. Published site release:
`faceddd2696f5af77cb029913d82a8229338528e`. GitHub Pages deployment succeeded.
See [ACTIVE-CHECKPOINT.md](ACTIVE-CHECKPOINT.md) for verification and remaining
publication status. Private browser captures stay outside Git.

## Companion plans

This repo implements the plan locked in:

- `document-ops-portal/CALLMEIE-PARENT-HUB-BUILD-SPEC.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-PRD.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-DESIGN-RECIPE.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-CODEBASE-PLAN.md`

These documents describe the earlier build. The authorised local review
uses DESIGN.md and ACTIVE-CHECKPOINT.md for its current scope.

## Stack

Static HTML, CSS and local JavaScript. No framework or site build step. The
optional voice vendor bundle has a pinned, separate build; it is disabled
publicly. Push to `main` to trigger GitHub Pages publication.

```
callmeie-hub/
├── CNAME              callmeie.ie
├── index.html         parent-brand hub (7-section page)
├── about.html         single-paragraph signed about page
├── site.css           ~430 lines, brand tokens + per-block styles
├── site.js            ~30 lines, Fraunces variable-font kinetic load
├── favicon.svg        indigo on paper square mark
├── favicon.png        32×32 PNG fallback
├── og-image.png       1200×630 social share card (TODO: generate via Codex)
├── robots.txt         allows all + sitemap pointer
├── sitemap.xml        2 URLs (/ and /about.html)
├── tiktokDsJqSWF...   TikTok dev verification (preserved from old site)
├── dental.html        meta-refresh → receptionist.callmeie.ie/dental.html
├── motor-factors.html ↑ (and 7 more redirect stubs for legacy receptionist URLs)
├── salon.html
├── solicitor.html
├── demo.html
├── onboard.html
├── onboard-details.html
├── privacy.html
├── terms.html
├── README.md
└── .gitignore
```

## Cutover (sister repo migration)

This repo replaces `scruge1/CallMeIE` as the GitHub Pages site for `callmeie.ie`.
The receptionist site moves to `receptionist.callmeie.ie` (CNAME swap on
the existing repo). Cutover is a single deploy window — both repos must
ship simultaneously.

See `CALLMEIE-PARENT-HUB-BUILD-SPEC.md` §6 for the 7-phase runbook.

## License

Proprietary materials and third-party components retain their applicable ownership and licences. The trading name does not establish ownership of every asset.

## Legal alignment publication - 14 October 2026

Adam authorised publication of the reviewed `review/pi-legal-20261014` candidate. Terms, Privacy and DPA v1.3 and the modular Order v2.0 identify the sole-trader supplier and scope future services by agreement. The old Order is retained in Git history and a clearly superseded local archive; it is excluded from the current reference and this publication's added files. [ACTIVE-CHECKPOINT.md](ACTIVE-CHECKPOINT.md) and [the publication report](reports/legal-publication-20261014.md) record deployment and verification. The final unsigned insurance package and broker-only questions are owned by `C:/Users/a33_s/Downloads/CallMeIE-PI-draft-20261014/CHECKPOINT.txt`. No existing client contract, billing configuration or provider setting is amended.
