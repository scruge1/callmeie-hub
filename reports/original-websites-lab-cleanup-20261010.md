# Original Websites and Lab cleanup

Baseline: original commit6578619 in callmeie-hub-original-6578619. Only websites/index.html and lab/index.html were edited in this lane. Root owns cleanup.css, shared chrome, preview asset copying and runtime presentation labels. No showcase layout, new imagery, texture or3D was introduced.

Before editing, original Websites and Lab top views were captured and actually viewed at375 and1280. The original orange/paper Websites colors, Fraunces italic display, local navigation, managed pricing cards, Care and one-off ownership sections, gallery cards and their CTA overlays remain. Lab retains its original three-column adaptive card grid, pale background and dark enquiry strip.

Websites: replaced eleven placeholder preview references (ten gallery cards and one demo showcase) with existing public WebPs. Social preview points to an actual concept. Shortened hero and duplicate demo narration. Removed obsolete DocOps/AI-first definition, unsupported statistics strip and contradictory restaurant comparison that bundled separate products. Retained managed prices69/100/149, minimum terms, included edit budgets, one-off prices and ownership distinctions. Removed duplicate hero process summary; retained the detailed process. Corrected handover copy to distinguish managed and owned source. Replaced real-client claims and LIVE badges with illustrative concepts and DEMO. Removed stale May urgency and deadlines. Static decorative arrow characters were removed from owned markup; runtime scripts were preserved. DM Sans/JetBrains UI declarations now use Inter, preserving Fraunces hierarchy. Mobile CTA rows wrap and hero spacing is compact.

Lab: added matching actual images to all20 existing linked cards. Shortened two long taxonomy paragraphs to one clear introduction. Added the shared STRIP sentinel for root injection. Preserved all sample routes and collection structure. Grid minimum now uses min(100%,280px) to fit320. Image height:auto corrects HTML intrinsic height so previews stay8:5 rather than900px tall. Existing card hover and dark enquiry strip remain; no contrast or wrapping clash was found.

Verification: final normal browser views at320/375/390/768/1280, height640, top/gallery and pricing or Lab footer were captured and actually viewed in six five-case sheets. The final Lab sizing fix was rerun at all five widths. Websites320 was additionally rerun after waiting for and dismissing the consent prompt. All31 preview references loaded at each width, all ten scenarios had zero horizontal overflow, and body typography resolved to Inter. The original scripts were compared with6578619: Websites8blocks and Lab2blocks are identical. No function, handler, form ID, endpoint or provider logic changed. No submissions, commit or publish occurred.

Evidence remains outside Git: C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/original-cleanup/. Before images: before-{websites,lab}-{375,1280}.png. Final images: after-{websites,lab}-{320,375,390,768,1280}-{top,gallery,detail}.png. Reviewed sheets: sheet-{websites,lab}-{top,gallery,detail}.jpg. Results: results.json, lab-final-results.json and website-320-final-results.json. The320 Website sheet initially included a pending consent prompt; the latest standalone320 frames supersede it.

Shared lower Websites fit button still shows a runtime arrow in these captures. Root owns that existing runtime presentation correction. The preserved original Websites local product/section navigation is separate from the shared global Products menu; Lab now has one shared global strip and its local back link.

## Bounded demo layout ports

Reviewed gitdiff6578619..56fc4be and ported only verified responsive CSS plus two local table-scroll wrappers. No brand.css, GN styling, palette, image or function blocks were copied. The original script blocks were asserted equal before/after each lane write.

Changed pure samples:01-minimalism-swiss (implicit mobile grid tracks and wrapping);03-glassmorphism (dashboard button labels wrap);04-brutalism (mobile header logo/CTA sizing and footer logo fit);05-3d-hyperrealism (mobile header wraps);06-vibrant-block (mobile navigation and email CTA fit);10-retro-futurism (focusable local schedule-table scroll).

Changed industry samples:02-solicitor-swiss (headline/header reading fit);04-physio-neumorphism (phone pushes right when hidden nav stops doing so);05-opticians-glassmorphism (mobile navigation wraps);06-trade-pro-dark-oled (contact/email wrapping);08-financial-brutalism-editorial (mobile section head stacks);10-local-services-brutalism (non-expanding hero tracks and focusable local rates-table scroll).

Source frozen after these12files. Root reruns the affected matrix routes. All44demo routes will be visually reviewed from final320/1280 matrix after completion. This section records implementation scope, not a completed new visual pass.

## Initial full demo visual coverage

All 44 routes below were actually viewed at 320 and 1280 using top and footer crops in 30 contact sheets under external original-cleanup/demo-review. This initial matrix predates root's subsequent shared GSAP resource, return control and Vetcare booking-width fixes. It proves body-design coverage, not final shared-control acceptance. Confirmed initial shared defects: return pill overlaps original brand headers; Murphy hero phone is absent; original /js GSAP references are missing. Root owns their correction. Blank full-page tails and transient animated text require normal viewport checks and are not independently treated as product failures.

- /websites/demos/clancys-restaurant-cork/ — viewed at 320 and 1280.
- /websites/demos/curtin-electrical/about/ — viewed at 320 and 1280.
- /websites/demos/curtin-electrical/accessibility/ — viewed at 320 and 1280.
- /websites/demos/curtin-electrical/ — viewed at 320 and 1280.
- /websites/demos/curtin-electrical/privacy/ — viewed at 320 and 1280.
- /websites/demos/curtin-electrical/services/ — viewed at 320 and 1280.
- /websites/demos/murphy-plumbing-cork/ — viewed at 320 and 1280.
- /websites/demos/slaney-dental-wexford/ — viewed at 320 and 1280.
- /websites/demos/strand-road-dental/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/about/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/accessibility/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/book/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/contact/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/privacy/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/consultations/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/dental/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/emergency/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/neutering/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/surgery/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/services/vaccinations/ — viewed at 320 and 1280.
- /websites/demos/vetcare-limerick/team/ — viewed at 320 and 1280.
- /websites/demos/wildflour-bakery-galway/ — viewed at 320 and 1280.
- /websites/samples/01-minimalism-swiss.html — viewed at 320 and 1280.
- /websites/samples/02-neumorphism.html — viewed at 320 and 1280.
- /websites/samples/03-glassmorphism.html — viewed at 320 and 1280.
- /websites/samples/04-brutalism.html — viewed at 320 and 1280.
- /websites/samples/05-3d-hyperrealism.html — viewed at 320 and 1280.
- /websites/samples/06-vibrant-block.html — viewed at 320 and 1280.
- /websites/samples/07-dark-oled.html — viewed at 320 and 1280.
- /websites/samples/08-claymorphism.html — viewed at 320 and 1280.
- /websites/samples/09-aurora-ui.html — viewed at 320 and 1280.
- /websites/samples/10-retro-futurism.html — viewed at 320 and 1280.
- /websites/samples/industries/01-dental-swiss.html — viewed at 320 and 1280.
- /websites/samples/industries/02-solicitor-swiss.html — viewed at 320 and 1280.
- /websites/samples/industries/03-accountant-minimalism.html — viewed at 320 and 1280.
- /websites/samples/industries/04-physio-neumorphism.html — viewed at 320 and 1280.
- /websites/samples/industries/05-opticians-glassmorphism.html — viewed at 320 and 1280.
- /websites/samples/industries/06-trade-pro-dark-oled.html — viewed at 320 and 1280.
- /websites/samples/industries/07-vet-claymorphism.html — viewed at 320 and 1280.
- /websites/samples/industries/08-financial-brutalism-editorial.html — viewed at 320 and 1280.
- /websites/samples/industries/09-architects-3d.html — viewed at 320 and 1280.
- /websites/samples/industries/10-local-services-brutalism.html — viewed at 320 and 1280.

## Additional confirmed normal viewport repairs

Five normal320 viewport checks confirmed real text or content clipping. Scoped CSS repairs: sample04 contact heading font fits its column; sample09 discovery header wraps so its non-shrinking button stays readable; sample10 player title can wrap long words; industry02 headline uses28px below360 to fit the205px column; industry07 contact cards can shrink, contact rows wrap, and decorative card/farm shapes clip locally. All five final normal viewport frames were actually viewed. Contact-heading/button/player/solicitor text now fits; industry07 document overflow29px became0. Retro hero3px scroll excess is its glitch/glow decoration rather than missing readable copy. Final images are clip-final-*.png and metrics clips-normal.json outside Git.

Normal8773 Murphy and Curtin root views were captured and viewed at320/1280 after networkidle plus4seconds. Local GSAP loaded. Murphy phone still had opacity0 and was truly absent; a scoped static hero-phone-fallback opacity1!important restores it. Actual final320 frame confirms the phone. Curtin quote CTA was visible; its12px transform did not hide it. Curtin's40px document overflow was reported to root for separate decorative containment adjudication. No runtime function changed.

Final lane source covers14 sample files plus Murphy root. Initial44-route sheets are reviewed evidence, but final shared resource/control matrix must replace the initial run before overall acceptance. No publish or form submission occurred.

## Final matrix visual review and bounded follow-up

The completed 320-case matrix was reviewed independently. Every one of the 44 demo routes listed above was actually viewed at 320 and 1280 using top, middle and footer crops. Thirty final sheets are outside Git in original-cleanup/demo-review-final. Original demo art and distinct layouts remain. Curtin services panels settle after progressive scrolling and fit. The Vet industry desktop headline has readable text; its small measured excess comes from the wavy underline and dot decoration. Dental Swiss map labels are intentionally translated into position. Hidden honeypots, closed menus, subtle Clancy watermark and full-page transparent tails are not visible content defects.

Four remaining genuine defects received static CSS fixes: Clancy .nav and Strand #site-header start 58 px below the in-flow return control; Slaney .hero__text uses its original surface color so the animated blue background no longer obscures text; Vetcare contact inputs and textarea use border-box sizing and stay inside their card. All eight normal viewport after frames at 320 and 1280 were actually viewed and confirm readable text, separated controls and aligned fields. Before frames are preserved as repair-BEFORE-*; final frames are repair-AFTER-*.

Two additional bounded changes: sample06 fixed .nav starts at 82 px, preserving its original 24 px inset below the 58 px return row. Websites removed its redundant status strip and changed static AI-First Websites labels and sentinel metadata to Websites. Runtime script blocks are unchanged. The final follow-up covers exactly six routes: Websites, Clancy root, Strand root, Slaney root, Vetcare contact and sample06 vibrant. Root owns the four-width matrix rerun and shared injection. No other source changes are planned.

Final normal sample06 frames at 320 and 1280 were viewed after its scoped mobile hero padding adjustment. Return control, brand, navigation and kicker are separate. Websites canonical injection completed with section and label Websites and WhatsApp text Website question. Injector check reports zero drift and zero errors. Final source is frozen; the root agent runs the six-route follow-up matrix.

## Clancy lazy-image flag adjudication

A separate read-only normal browser check inspected all four narrative scene images at widths 320, 390, 768 and 1280. On mobile, .sn__scene-img-mobile is displayed and all four images load at natural width 3840 after scrolling their scenes into view. At 768 and 1280, these mobile duplicate images use display:none with zero dimensions; some hidden lazy duplicates remain incomplete, including scene-table with natural width zero. The active desktop image panel renders the scene photo correctly. Normal mobile and desktop scene frames were actually viewed. No visible broken scene image was found and no source edit was made. This is not a claim that every inactive DOM image loads. Evidence: external clancy-scenes-{320,390,768,1280}.png and websites-clancy-scenes-proof.cjs.
