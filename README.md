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

The site design follows [DESIGN.md](DESIGN.md). It presents
AI receptionists and websites as the two main services. Supporting services
and legal scope stay available without crowding the main pages.

- Paper `#f5f1e8` · Ink `#0b0a08` · Burgundy `#5a1420`
- Archivo Black (display) + IBM Plex Sans (body, labels and data), self-hosted
- No glassmorphism, no purple gradients, no emoji, no rounded floating cards

Shared styling is in `brand.css`; shared HTML is in `_partials/`.
Run `py -3 scripts/inject-cohesion.py` after changing a partial, then its
`--check` mode. Demo designs retain their distinct visual styles.

## Published consolidation — 10 October 2026

Adam rejected the first published design as basic and off-brand. The current
correction restores the GN proposal reference and original logo; see DESIGN.md.
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

Static HTML + CSS + one tiny JS file. No framework. No build step. Push
to `main`, GitHub Pages rebuilds in ~30s.

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

Proprietary. CallMeIE Technologies Ltd.
