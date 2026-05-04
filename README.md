# callmeie-hub

Parent-brand hub for **CallMeIE Technologies Ltd** — the Limerick AI ops studio.
This repo serves the apex domain `callmeie.ie` via GitHub Pages.

- **Live**: https://callmeie.ie
- **Hosting**: GitHub Pages, `main` branch, `/` root
- **DNS**: Cloudflare (NS swap from GoDaddy 2026-05-03) → GitHub Pages anycast
- **Domain registrar**: GoDaddy (callmeie.ie)
- **CDN / 301s**: Cloudflare Bulk Redirects (post-cutover)
- **Custom domain**: `CNAME` file at repo root

## Brand contract

Same tokens as `portal.callmeie.ie` (Document Ops console) and
`docs.callmeie.ie` (Document Ops sales site). Single product family =
single brand language.

- Paper `#f8f5f0` · Ink `#1c1f24` · Indigo `#1d3557` · Amber `#c08a3f`
- Fraunces (display) + Inter (body) + JetBrains Mono (mono)
- No glassmorphism, no purple gradients, no emoji, no rounded floating cards

Source of truth: `document-ops-portal/app/static/portal.css` lines 1–58.
If brand tokens change, update there first then mirror here.

## Companion plans

This repo implements the plan locked in:

- `document-ops-portal/CALLMEIE-PARENT-HUB-BUILD-SPEC.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-PRD.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-DESIGN-RECIPE.md`
- `document-ops-portal/CALLMEIE-PARENT-HUB-CODEBASE-PLAN.md`

If this repo and those plans diverge, the plans win until updated.

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
