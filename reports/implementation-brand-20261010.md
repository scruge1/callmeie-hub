# Home and About preview changes

Local review worktree only. No commit or publication.

- Home now routes to two clearly scoped services, with current starting prices, a useful phone demo, brief studio introduction and contact.
- About identifies Adam, explains direct setup/support, links service choices and provider details.
- Removed founding/product counters, roadmap teaser, repeated labour-task story, long italic headlines and blanket claims about receptionist inclusion or all-plan coverage.
- Both pages use one navigation sentinel, one existing footer sentinel, the marketing body marker and brand.css last. Root supplies canonical shared navigation/footer and styles.
- Preserved canonical URLs, seller detail links, demo recording notice and 30-day deletion wording. All existing consent, widget and JavaScript functions remain unchanged.

Static review confirms one h1 and one strip/footer sentinel pair per page.

## Render verification

Visually viewed local preview `http://127.0.0.1:8765/` and `/about.html`: full pages at 1280×720 and 375×844; additional 390×844 viewport checks. Captures remain outside Git in `C:/Users/a33_s/AppData/Local/Temp/callmeie-preview-*.png`.

Home headings, service rows, phone demo and footer fit. About has one header, legible body copy and complete footer. Mobile menu was opened and visually inspected: all links fit in its panel. Consent was inspected visible on Home, then declined using No, thanks. Declined choice persisted on navigation to About. Internal service/provider/privacy links use local root-relative URLs; external contact links were not activated. About at 390 px reports document scrollWidth 390 px.

Sent two shared-style findings to root: remove inherited uppercase/letterspacing from product labels and enlarge/normalize demo recording disclosure; root brand.css now contains disclosure correction. Mobile floating WhatsApp button can overlap About body after consent decline; recommend hiding the floating control on mobile and retaining footer/contact links. No own HTML layout correction required.

No 3D asset is needed for this version. The visible demo number already explains and starts the interaction. A phone object would add weight without solving an observed comprehension problem; reconsider only if a future demonstrated interaction needs it.

## Tablet follow-up

Inspected About full-page Chromium render at 768×1024 after a matrix alert (`a` left595/right798). Current anchor bounds query returns no anchors beyond the viewport; header, main and two-column footer visually fit. Capture: `C:/Users/a33_s/AppData/Local/Temp/callmeie-about-tablet.png`.

The earlier matrix entry lists old font tokens (JetBrains Mono and Fraunces/Bodoni), whereas the adjacent375 entry lists the final two-font system. This suggests a mixed pre/post shared-style render or style-load timing; it does not identify a proven overflowing footer link. Requested a fresh frozen-source768 check from root. No speculative layout patch or overflow masking was applied.

## Final compact-footer verification

After the final shared footer update, captured and visually viewed all20 full-page Chromium screenshots: Home, About, Care Plans, Legal index and the admin gate, each at375,390,768,1280px. Capture script waits for every same-origin stylesheet to expose nonempty CSS rules and waits for document fonts. All20 document scroll widths equal viewport widths. Marketing/document body computed font is the final Inter token. Screenshots and metric results are outside Git at `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/brand-final/`.

Compact mobile footer passes: brand full-width, Products/Company side-by-side, Legal links in one full-width row, single provider line. Tablet and desktop remain aligned. About body is no longer covered by floating WhatsApp. Care hero gutters, pricing controls and FAQ labels fit. Legal index cards and provider details fit; its retained legal references were not rewritten.

Admin route `/receptionist/scripts/admin.html` shows a separate dark/cyan token gate with readable title, token input and Enter control. Gate fits all four widths. No token was entered, no controls were activated and no requests were submitted. Authenticated admin behavior is outside this visual check. No site source changes were made during final verification.

## Bounded sample repairs and Safari gallery check

Subsequent user-requested full-page checks identified two sample issues. Changed only `websites/samples/03-glassmorphism.html` and `websites/samples/10-retro-futurism.html` for these repairs. No JavaScript edits.

Glassmorphism dashboard actions now wrap and keep their labels readable. At widths480px and below, portfolio metadata stacks into a single column, removing the confirmed label/value collisions. Retro schedule now sits in a named, keyboard-focusable local horizontal scroll region with a visible focus outline; the table keeps readable columns. Both samples retain their own colors and typography.

Visually viewed targeted actions/metadata and schedule screenshots in WebKit375/390 and Chromium768/1280. All eight check document widths equal viewports, and no button has scrollWidth greater than clientWidth+3. WebKit schedule region widths345/359 contain560px of table content. Chromium table fits768/1280 without scrolling. Evidence: `output/playwright/sample-bounded-fixes/` under the external review directory.

Websites gallery was separately tested in WebKit375/390 by scrolling each of ten thumbnail images into view and waiting for actual image decode. All20 image loads completed with positive natural widths. All20 image screenshots were visually viewed. First seven previews show distinct business designs. Last three rendered previews show oversized numeral/bar or neon-object overlap. Follow-up source inspection confirms these are gallery pseudo-element overlays, not defects established in the image assets: `.card-stage.t-01`, `.card-stage.t-sol` and `.card-stage.t-07` retain decorative `::before`/`::after` rules. Only `.demo-thumb` pseudo-elements were disabled. Image-locator screenshots include the overlapping pseudo-elements within the image rectangle. Root received exact screenshots375-08/09/10 and matching390 paths plus the precise CSS fix: disable pseudo-elements on actual-image card stages. No lazy-loading repair is indicated. Gallery evidence: external `output/playwright/gallery-webkit/`.

Root disabled gallery card-stage pseudo-elements. Visually rechecked all six last-three thumbnails in WebKit375/390: clean previews, computed pseudo display none. Shared Solicitor sample bar fits375/390/768; Opticians header wraps cleanly at768. All six current checks have document width equal viewport. Evidence: external `output/playwright/brand-last/`.

Vetcare root and About menus were checked in WebKit375/390, closed and open. Closed links are not focusable and are visually absent. Open drawer failed: link bounds331..599 at375 and346..614 at390. Source drawer combines `inset-inline:0`, explicit right0 and fixed width, so its left edge anchors beside the toggle instead of aligning its right edge. Root received exact bounds, open screenshots and a shared CSS recommendation to set inline-start auto and inline-end0. No site source edits made during these checks. Evidence: external `output/playwright/brand-vetcare/`.

Final root correction now targets the actual native-details class `.nav-mobile-toggle`, aligns the open drawer to its right edge and explicitly sets the closed drawer display:none. Reran all four cases in WebKit: root/About at375/390, initial closed followed by menu clicks only. Visually viewed eight accepted screenshots. Initial closed display:none and all links are not focusable; no hidden attribute is expected for native details. Open links are visible/focusable and within viewport:75..343 at375 and90..358 at390. Open panel itself fits59..359 and74..374 respectively. Updated evidence in `brand-vetcare/` replaces the earlier failed captures. No forms submitted or site source edited during final recheck.
