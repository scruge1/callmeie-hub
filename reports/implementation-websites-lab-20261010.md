# Websites and Lab implementation — 2026-10-10

Local worktree: callmeie-hub-review-20261010, based on published 6578619. No commit, publish or provider change.

## Changes

Websites now opens with a short headline and gallery, followed by three managed plans, ownership details, optional care, three process steps, short FAQ and the existing enquiry form. Removed doc ops, bundle assumptions, stats, stale May availability, client claims, local duplicate header and repeated narration. Demo concepts are labelled illustrative. Kept Launch €69/12-month, Business €100/12-month, Premium €149/18-month and €0 upfront; ownership prices €695, €1,595 and from €2,950; material edit caps, extra-work rates, VAT and cancellation terms. Full scope links retain detailed contract coverage. Quote modal IDs, form IDs/actions, legal wiring and original JavaScript logic remain.

Lab is now a short visual gallery using the shared paper/ink/indigo identity and Inter/Fraunces. Removed card IDs and taxonomy paragraphs. Retained all 20 sample routes. Existing interactive gallery redirect has a consistent title/paper color.

Added 27 deliberately curated public thumbnails in websites/previews/, generated from local public concept pages after render repairs. They contain no operator UI, browser chrome, consent panel or demo return chrome. Private verification captures remain outside the repo. Existing capture ignores remain.

Fixed Slaney mobile hero by replacing dark conic backdrop with readable pale static backdrop and explicit mobile spacing. Removed its unavailable optional animation tags. Repaired other demos’ missing /js animation references by vendoring pinned GSAP3.13.0, ScrollTrigger and SplitText under websites/demos/_vendor and updating static resource paths. Download source: https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/. Headers retain GSAP copyright and standard-license reference. This pin needs normal maintenance review and tested refresh; no runtime CDN dependency.

Fixed shared sample navigation parser failure: comment contained demos/*/index.html, which prematurely terminated its block comment. Changed comment wording only. No JavaScript function implementation edits.

## Verification

All 27 demo/sample routes rendered on local Chrome at1440×900 desktop and390×844 mobile. Viewed desktop/mobile contact sheets for all27. Second run: zero JavaScript page errors and scrollWidth390 at390 for every route. Browser artifacts and machine-readable results: C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/lab/.

Websites and Lab checked visually at390 and1280: one main landmark each; no horizontal document overflow. Quote modal opens with Business selected; contact form remains aligned. Found/fixed invisible contact heading and overly italic modal title. Native details preserve ownership/care visibility. Gallery image diagnostics must force lazy images to load before reporting failures; unloaded offscreen lazy images are not404 evidence.

## Remaining root integration

Shared nav/footer/brand/injector belong to root. Apply common header to Lab, remove outdated trust/status strips and repeated sticky sales dock, fix demo pill branding collision and consent text color through shared components. Main inventory QA owns375/768 widths, WebKit, full-page overflow/table/stuck-transform checks and final visual inspection after reinjection. No final all-browser claim here. Do not publish without Adam’s later approval.


## Shared integration regression

After root brand rollout: visually viewed Websites and Lab at375/390/1280, pricing and contact form, quote modal, and Slaney/architects first-visit return/consent controls. All gallery images decoded successfully, one main per page, no horizontal document overflow. Regression opens Business quote, verifies selected tier, selects Launch through its visible label, and verifies changed value without submitting. Passed all three widths. Script and results: outside-repo check-shared.cjs and output/playwright/lab/shared-regression.json.

Added Lab canonical header/footer sentinels for root reinjection. Removed Websites redundant global trust/breadcrumb blocks and compacted hero/gallery introduction. Root owns final demo navigation/consent stack repair; observed old bottom navigation can cover consent buttons and reported it for shared correction.

Pinned vendor provenance, SHA256:

- GSAP3.13.0: https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js — 96C01B81F44A3290E2B4532F55E2C9534B2ADC43273A19F3756B2CB41F0FD0B6
- ScrollTrigger3.13.0: https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js — 308219390E5E3B84CDA0C481E70CAA9820883AE10BDA44E6E9A149A81AAC4B3F
- SplitText3.13.0: https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js — 5E519EA2470FAA15CA4D4F27E9263E5906C07C034A9B4771164DEE108136563A
`nFinal flagged-route repair: 04-physio-neumorphism.html now gives .topbar__phone margin-left:auto inside the same max-width:720px breakpoint that hides .topbar__nav. Visually checked375/390/1280. Brand and phone share first mobile header row; booking action wraps below. Desktop navigation stays aligned. No document overflow at any checked width. Only this static sample CSS rule changed.


## Final strict-gate repairs and accepted decorations

Repaired Murphy hero phone opacity0 with static CSS visibility/opacity1 and transform none. Repaired Curtin hero action persistent inline12px translation with static transform none/opacity1. All four gate configurations now retain only aria-hidden decorative image overlay flags. Public Murphy/Curtin WebP previews refreshed to match these visible actions, using reviewed public crops without chrome.

Clancys suspected broken scenes are lazy responsive duplicate imagery, not404 resources. Initial hidden duplicate chef image has0×0 bounds; visible offscreen table scene is lazy. After scrolling, all visible images decode in WebKit375/390 and Chrome768/1280. Remaining watermark flag is explicitly aria-hidden=true with intended opacity.04. Keep it decorative.

Swiss sample01 mobile safety CSS had collapsed main to1column while children spanned1/7, causing implicit tracks and clipped heading. Narrow mobile override uses six minmax(0,1fr) tracks and wraps heading words. Known gate0 on WebKit375/390 and Chrome768/1280; document width matches viewport, no h3 clipping. Visually viewed fresh Safari top/middle/footer crops.

Clay sample08 blobs are fixed, empty, pointer-events:none decorative shapes behind content. Document width375/390/768/1280 is bounded; no clipping or text-overflow flag. All14 known gate ghost-box entries are CSS owl body/eyes/beak/feet, tile icons and streak dots. Visually viewed actual mascot, colored icons and full mobile content; accepted decoration, no source fix needed.

Vetcare booking gate entries are its five empty input controls, visible labeled fields rather than missing content. All four widths now bounded; form screenshot shows aligned inputs. Root repaired hidden drawer shared CSS and labels demo concepts through canonical pill.

Repaired13 nested Vetcare undefined privacy/accessibility URLs to existing demo pages. Missing Clancys/Slaney/Wildflour policies link to actual CallMeIE privacy with explicit label; accessibility links say Accessibility contact and mailto hello@callmeie.ie. Murphy missing services/about pages route to the actual design gallery. No extra pages created. Whole-site local target checker reports0 missing targets after root and other agents’ fixes.

Bounded evidence: outside-repo output/playwright/lab/bounded-final-gate.json,24 checks across six routes (WebKit375/390, Chrome768/1280). Fresh visual crops and action screenshots viewed. Existing global inventory remains main-owned; this report does not claim all routes share these results.
