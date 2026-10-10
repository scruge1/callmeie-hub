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
Final flagged-route repair: 04-physio-neumorphism.html now gives .topbar__phone margin-left:auto inside the same max-width:720px breakpoint that hides .topbar__nav. Visually checked375/390/1280. Brand and phone share first mobile header row; booking action wraps below. Desktop navigation stays aligned. No document overflow at any checked width. Only this static sample CSS rule changed.


## Final strict-gate repairs and accepted decorations

Repaired Murphy hero phone opacity0 with static CSS visibility/opacity1 and transform none. Repaired Curtin hero action persistent inline12px translation with static transform none/opacity1. All four gate configurations now retain only aria-hidden decorative image overlay flags. Public Murphy/Curtin WebP previews refreshed to match these visible actions, using reviewed public crops without chrome.

Clancys suspected broken scenes are lazy responsive duplicate imagery, not404 resources. Initial hidden duplicate chef image has0×0 bounds; visible offscreen table scene is lazy. After scrolling, all visible images decode in WebKit375/390 and Chrome768/1280. Remaining watermark flag is explicitly aria-hidden=true with intended opacity.04. Keep it decorative.

Swiss sample01 mobile safety CSS had collapsed main to1column while children spanned1/7, causing implicit tracks and clipped heading. Narrow mobile override uses six minmax(0,1fr) tracks and wraps heading words. Known gate0 on WebKit375/390 and Chrome768/1280; document width matches viewport, no h3 clipping. Visually viewed fresh Safari top/middle/footer crops.

Clay sample08 blobs are fixed, empty, pointer-events:none decorative shapes behind content. Document width375/390/768/1280 is bounded; no clipping or text-overflow flag. All14 known gate ghost-box entries are CSS owl body/eyes/beak/feet, tile icons and streak dots. Visually viewed actual mascot, colored icons and full mobile content; accepted decoration, no source fix needed.

Vetcare booking gate entries are its five empty input controls, visible labeled fields rather than missing content. All four widths now bounded; form screenshot shows aligned inputs. Root repaired hidden drawer shared CSS and labels demo concepts through canonical pill.

Repaired13 nested Vetcare undefined privacy/accessibility URLs to existing demo pages. Missing Clancys/Slaney/Wildflour policies link to actual CallMeIE privacy with explicit label; accessibility links say Accessibility contact and mailto hello@callmeie.ie. Murphy missing services/about pages route to the actual design gallery. No extra pages created. Whole-site local target checker reports0 missing targets after root and other agents’ fixes.

Bounded evidence: outside-repo output/playwright/lab/bounded-final-gate.json,24 checks across six routes (WebKit375/390, Chrome768/1280). Fresh visual crops and action screenshots viewed. Existing global inventory remains main-owned; this report does not claim all routes share these results.

## Final sample05 mobile header repair

Static style `nocturne-mobile-header` added to websites/samples/05-3d-hyperrealism.html. At640px and below, the primary body navigation wraps with16px gap, the brand takes a full row, and its gold CTA has max-width100%. This resolves the overlapping logo and Reserve label without changing JS, desktop typography or headphone artwork. Fresh CSS-loaded, font-ready, progressively scrolled and3200ms-settled viewport captures were visually viewed at375/390/768/1280. All four headers are readable and distinct; document widths match viewport widths. Evidence external output/playwright/final-settled/*05-3d-hyperrealism* and nocturne-results.json.

## Final restored-brand visual verification

All 44 demo, sample and nested content routes received fresh captures at 375 and 1280 pixels (88 cases). Each capture waited for local CSS, fonts and progressive scrolling, then settled for 3200 ms after returning to the top. Normal viewport screenshots were taken before full-page screenshots. Full-page expansion can disturb ScrollTrigger, so the normal viewport images are the authority for hero visibility. All 12 top contact sheets and all 12 footer contact sheets were visually reviewed. Fresh normal viewport captures also verify each changed footer and form. Earlier complete body reviews support unchanged content. The initial 132 captures with malformed stylesheet URLs are excluded from final CSS evidence.

All 88 document widths fit their viewports. The CallMeIE return control preserves each concept's distinct typography and palette. Root fixed the Clancys, Strand Road and sample 06 header offsets, moved the gallery return dock into normal flow, and separated sample 06 mobile logo and navigation rows. Fresh Clancys views at 375 and 390 pixels show unobstructed hero actions.

Confirmed static CSS repairs in this lane:

- Sample 05: mobile navigation wraps, the Nocturne brand occupies its own row, and the Reserve button fits. Visually verified at 375, 390, 768 and 1280 pixels.
- Sample 04: the mobile CONCRETE/SLAB footer logo now uses a scoped font clamp on `main > footer .brand`. Fresh normal viewport images at 375 and 390 pixels show the complete logo.
- Sample 06: the mobile contact email button uses smaller text, padding and gaps with a fixed icon size. Fresh normal viewport images at 375 and 390 pixels show the complete address. Root owns its separate navigation grid repair.

The shared industry enquiry form is an intentional section in normal document flow. All 10 industry HTML routes load `_owl-form.js`; all 10 slugs exist in its mapping. Static presentation strings now identify CallMeIE, label the page as an illustrative business website, ask about the visitor's business and preferred design, and link to the real privacy notice and website plans. Unsupported 24-hour reply and fictional administrator claims were removed. Form IDs, endpoint, site mapping, handlers and state logic are unchanged. No provider configuration changed. `node --check` passes.

All 20 final normal viewport form images (10 routes at 375 and 1280 pixels) were visually reviewed across four contact sheets. They show the shared paper and burgundy CallMeIE treatment, readable labels, inputs and submit controls, plus visible privacy and plan links. Every case contains the expected illustrative-demo copy and has bounded document width. No forms were submitted.

GitNexus impact was attempted with CLI 1.6.12 against the parent New repos index. The `_owl-form` target was not found, risk remained UNKNOWN, and the FTS extension was unavailable. The anonymous IIFE and isolated worktree lookup prevent a resolved graph result. This is a documented limitation, not evidence of no impact. Manual review of all 10 HTML call sites and the exact presentation-string diff establishes the bounded change scope.

Evidence is outside Git at `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/final-settled/` and `form-final/`. These contain the 88-route capture results, normal viewport top images, final footer proofs, sample 05 four-width proofs and 20 final form results/contact sheets. Root owns the complete browser gate and publication decision. No confirmed visual defects remain in this lane. Source is frozen.

## Editorial showcase revision after user rejection

The user rejected the basic card layout and decorative arrows. This revision retains the established Great National paper, burgundy, Archivo Black and IBM Plex Sans identity. It changes composition and image hierarchy rather than replacing the palette.

Reference work: read the Design Hub mandatory router, installed-tool manifest, toolchain, foundation documents, HeroSplit template and CSS scroll-driven recipe. Current project DESIGN.md overrides the historical dark/Geist hub defaults. Real browser captures of https://k95.it/ and https://metajive.com/ were visually viewed. K95's immersive canvas is a reference limitation for business conversion; Metajive's dominant imagery and editorial split informed the composition. No claims are made about unviewed references.

Changed source: websites/index.html, lab/index.html and new websites/websites-showcase.css. Websites uses a large photographic Slaney Dental concept preview and one direct heading, followed by asymmetric image spreads with captions. The Lab uses a product-design preview and separates business concepts from creative directions. Gallery cards no longer have uniform framed boxes. Wide chapter images and alternating widths establish a clearer rhythm. Mobile stacks the same real previews without horizontal scrolling.

Motion: CSS hover and keyboard focus reveal the gallery action and apply a restrained preview zoom. Lab preview links lift slightly on hover/focus. A guarded CSS view-timeline applies a small crop/translation settle on viewport entry. Content remains visible without animation support or JavaScript. Reduced motion disables animations and transitions. Mobile preview actions remain visible. No scroll hijacking or new 3D runtime was added.

Removed decorative arrows and emoji from static page presentation. Existing script bodies were preserved. Root was notified of remaining JS-generated wizard arrow labels so they can be handled in its function-impact lane. Removed a stale May date placeholder and a duplicate Care introduction; the Care details, prices and terms remain. All approved plan prices, minimum terms, ownership rules, modal/form identifiers, integrations and endpoints remain intact. No provider settings changed and no forms were submitted.

Visual QA: both pages at 375, 390, 768 and 1440 pixels, normal top and gallery viewport captures (16 images) were reviewed through two contact sheets and representative full-size images. All eight document widths match their viewports. The new stylesheet loads and reduced-motion computes animation:none. Four progressive full-page passes at 375 and 1440 verified every visible image decoded, no rendered arrow characters, both Websites forms present and keyboard focus reveals the concept action. Full-page images were visually reviewed for all gallery spreads and lower sections. Final targeted Lab footer images at 375 and 1440 verify ink text and burgundy action after a legacy white-text contrast defect was corrected.

Plan-selection regression at 375, 768 and 1440: selecting Business opens the existing modal with the correct tier; close returns it to the closed state. All six pricing/modal viewport images were visually reviewed. No submission occurred.

Evidence: C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/editorial-reference/ and editorial-showcase/. Results files: results.json (eight layout cases), full-results.json (four all-image/focus cases), modal-results.json (three no-submit selection cases). Final footer proofs are lab-375-footer-final.png and lab-1440-footer-final.png. Operator captures remain outside Git. Root owns final shared-chrome injection, global checks and publication.

## Caption control correction after independent craft review

Independent design-comparison-20261010.md rejected the pale image-overlay action slabs and customer-facing style taxonomy. The bounded Websites/Lab correction moves all 10 Websites concept actions outside the images, below the captions, as always-visible text links. Their underline changes on hover and focus. The black gradient and pale rectangle no longer cover any preview. Mobile and desktop use the same quiet caption control. The asymmetric spreads remain; no uniform card layout was introduced.

Websites captions now name business categories such as dental practice, veterinary practice, electrical services and bakery. Lab business captions also use categories. Creative entries use concept names or plain descriptions such as Nocturne, The Grid and layered dashboard. Preview alt text identifies illustrative website concepts rather than style jargon. Scripts, plan/form identifiers, prices, terms and endpoints remain unchanged.

Fresh normal viewport captures at 375, 390, 768 and 1440 pixels for both pages were visually reviewed through refreshed top and gallery contact sheets plus full-size mobile, tablet and desktop gallery frames. All eight widths are bounded and reduced motion still disables animation. Critical visual assessment: images now remain uninterrupted, captions have a clear name/category/action hierarchy, and the repeated controls are subordinate to the varied imagery. These specific gallery defects are resolved. This does not claim the separate whole-Home premium-composition gaps are resolved; those remain root-owned.

Current review evidence: external editorial-showcase/gallery-sheet.jpg, websites-375-gallery.png, websites-1440-gallery.png and lab-768-gallery.png. Earlier overlay screenshots and overlay-opacity evidence are superseded by the caption-link treatment.

## Final craft visual coverage

The complete 320-case matrix was available before visual review. All 44 demo content routes were actually viewed at 375 and 1280 px in 30 top/footer contact sheets. External evidence: output/playwright/craft-final/demo-review/demos-375-01.jpg through -15.jpg and demos-1280-01.jpg through -15.jpg. Distinct business and creative styles remain visible.

Fresh normal viewport scrolling checked all ten Websites previews at both widths. All twenty instances loaded with nonzero dimensions, opacity 1 and clip inset0. All twenty screenshots were viewed in normal/thumb-sheet.jpg. The empty Dental practice region in a full-page screenshot is a capture artefact. The Clancy restaurant preview was compared visually with Slaney and selected for the Websites hero.

Sample05 normal375/390 captures show a clean header and settled typography. Sample04 normal375/390 confirmed its logo text overflows its flex box below the CTA although the element rectangles only touch. Root authorised a bounded mobile CSS repair: max560 logo responsive13-18px with reduced padding, no shrinking or wrapping; CTA13px with reduced padding and no shrinking; header gap10px. Static Hire Us arrow removed. Only sample04 HTML changed for this repair.

Root owns the common dock arrow label correction. Ten affected demo routes require the fresh follow-up matrix images; other34 remain current. Initial full-page split-text and bottom mockup anomalies are capture artefacts, not verified new defects. Shared forms retained their honest enquiry copy and distinct demo bodies remain intact.

| Route | Both-width sheet |
| --- | --- |
| /websites/demos/clancys-restaurant-cork/ | 01 |
| /websites/demos/curtin-electrical/about/ | 01 |
| /websites/demos/curtin-electrical/accessibility/ | 01 |
| /websites/demos/curtin-electrical/ | 02 |
| /websites/demos/curtin-electrical/privacy/ | 02 |
| /websites/demos/curtin-electrical/services/ | 02 |
| /websites/demos/murphy-plumbing-cork/ | 03 |
| /websites/demos/slaney-dental-wexford/ | 03 |
| /websites/demos/strand-road-dental/ | 03 |
| /websites/demos/vetcare-limerick/about/ | 04 |
| /websites/demos/vetcare-limerick/accessibility/ | 04 |
| /websites/demos/vetcare-limerick/book/ | 04 |
| /websites/demos/vetcare-limerick/contact/ | 05 |
| /websites/demos/vetcare-limerick/ | 05 |
| /websites/demos/vetcare-limerick/privacy/ | 05 |
| /websites/demos/vetcare-limerick/services/consultations/ | 06 |
| /websites/demos/vetcare-limerick/services/dental/ | 06 |
| /websites/demos/vetcare-limerick/services/emergency/ | 06 |
| /websites/demos/vetcare-limerick/services/ | 07 |
| /websites/demos/vetcare-limerick/services/neutering/ | 07 |
| /websites/demos/vetcare-limerick/services/surgery/ | 07 |
| /websites/demos/vetcare-limerick/services/vaccinations/ | 08 |
| /websites/demos/vetcare-limerick/team/ | 08 |
| /websites/demos/wildflour-bakery-galway/ | 08 |
| /websites/samples/01-minimalism-swiss.html | 09 |
| /websites/samples/02-neumorphism.html | 09 |
| /websites/samples/03-glassmorphism.html | 09 |
| /websites/samples/04-brutalism.html | 10 |
| /websites/samples/05-3d-hyperrealism.html | 10 |
| /websites/samples/06-vibrant-block.html | 10 |
| /websites/samples/07-dark-oled.html | 11 |
| /websites/samples/08-claymorphism.html | 11 |
| /websites/samples/09-aurora-ui.html | 11 |
| /websites/samples/10-retro-futurism.html | 12 |
| /websites/samples/industries/01-dental-swiss.html | 12 |
| /websites/samples/industries/02-solicitor-swiss.html | 12 |
| /websites/samples/industries/03-accountant-minimalism.html | 13 |
| /websites/samples/industries/04-physio-neumorphism.html | 13 |
| /websites/samples/industries/05-opticians-glassmorphism.html | 13 |
| /websites/samples/industries/06-trade-pro-dark-oled.html | 14 |
| /websites/samples/industries/07-vet-claymorphism.html | 14 |
| /websites/samples/industries/08-financial-brutalism-editorial.html | 14 |
| /websites/samples/industries/09-architects-3d.html | 15 |
| /websites/samples/industries/10-local-services-brutalism.html | 15 |

Sample04 repair verification: all six normal top/footer screenshots at320/375/390 were actually viewed. Logo textWidth equals clientWidth147/168/174px, CTA gap24.9/49.4/56.2px, horizontal overflow0. Header and footer branding are fully readable. Evidence normal/04-fixed-{320,375,390}-{top,footer}.png and04-fixed-results.json. Pending privacy prompt overlays lower content as intended until a choice is made. Source frozen.

Follow-up correction: root completed and merged the92-case pass. The ten industry demo routes were re-viewed in regenerated sheets12-15 at375/1280. Parent dock labels now read Gallery, Previous and Next with no decorative arrows. Forms remain legible and shared identity is consistent. Physio full-page footer crop remains a known capture artefact; prior normal viewport form proof supplies its visual evidence. No new defect was identified in the refreshed ten-route review.

Exact dock refresh coverage correction: the earlier phrase ten industry routes described a wider visual re-view, not the ten indexed dock callsites. The actual ten affected callsites are seven demo roots (Slaney, Strand Road, Vetcare, Murphy, Curtin, Clancy and Wildflour), plus industry01 dental, industry02 solicitor and industry06 trade. Fresh seven-root footer crops were now actually viewed at375/1280 in regenerated sheets01,02,03,05,08, in addition to the three affected industry routes in sheets12 and14. All twenty actual affected-route footer crops show Gallery, Previous and Next with no parent-control arrows. No new layout defect was found. This exact list supersedes the generic refresh description.
