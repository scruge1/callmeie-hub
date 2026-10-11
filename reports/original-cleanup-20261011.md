# Original CallMeIE design cleanup

The local candidate restores the layout and character of original `6578619`.
This is the first gradual cleanup requested by Adam. It keeps the Irish AI
receptionist as the main offer and Websites as the secondary offer.

Preview: http://127.0.0.1:8773/. Branch: `review/original-cleanup-20261010`.
Source is saved locally, uncommitted and unpublished. Live `06dcc58` is unchanged.

## Changes

Original paper colours, serif headings, section structure and demo designs
remain. Company pages use Fraunces for display and Inter for supporting text.
Home, About, Receptionist, Websites and Lab have shorter or less repeated copy.
Website and Lab preview windows use real existing thumbnail images. Duplicate
footers and obsolete discovery quiz entry points are removed from the visible
interface. The working custom sample player is retained in the original style.

Scoped fixes address heading rendering, open-menu bounds, enlarged-text
wrapping, buttons, table columns, demo header collisions, gradient contrast,
form field sizing and missing GSAP asset references. Material prices, service
conditions, form handlers, privacy and consent remain.

Legal introductions and metadata now describe Receptionist and Websites.
DocOps is qualified as withdrawn from new sales on 7 June 2026. Existing
agreement references and operative clauses remain. The Legal index replaces
internal Brand canon narration with the verified Service provider identity.
No generated scene, page texture or new 3D asset was added in this phase.

## Verification

The final matrix contains 320 unique cases over 80 content pages: Chrome at
768/1280 and WebKit at 320/390. Every case returns HTTP 200. No page-wide
overflow or JavaScript error remains. Agents actually viewed all 80 pages at
mobile and desktop sizes, then checked the affected normal viewports after
repairs. The 14 aliases are separate redirect inventory entries. Admin coverage
is the unauthenticated gate, with no authenticated operations.

All 11 Website previews were individually viewed and loaded in the normal
WebKit 320 gallery. All 20 Lab preview references load. Lazy images do not
need to load while hidden or before their section is visited. Clancy's visible
scene images were separately confirmed on mobile and desktop.

Home/About normal and doubled-text contexts pass. Open menus fit. Privacy and
other corrected table regions expose their full columns with keyboard scrolling.
The text test doubles computed text sizes; it does not qualify native browser
zoom or physical devices.

Actual audio play, pause, midpoint seek and keyboard advancement pass in
Chrome/WebKit at mobile and desktop sizes, with 206 range responses. Disabled
JavaScript, unavailable audio and reduced-motion checks pass. Two Chrome
metadata requests report ERR_ABORTED after a 206 response. Direct checks in
those exact widths confirm readyState 4, valid duration and no media error.

Raw detectors retain flags for closed native details, empty form fields,
intentional watermarks/map positions, a hidden honeypot and decorative underline
geometry. Normal visual and focus checks distinguish these from real defects.
The report does not claim zero raw detector flags or every dormant image loaded.

All 228 browser source and asset hashes match the reviewed candidate. Original
inline script blocks match after line-ending normalization. Current audio and
enquiry helper scripts match their verified source exactly. Operative Privacy,
Terms and DPA text matches after excluding only the new legacy notice and labels.
Shared injection, local link targets and whitespace checks pass.

No real form submissions, provider writes, phone calls or publication occurred.
The owner's red-marked screenshot remains unavailable because Swarm OAuth
intake failed. These checks qualify the local candidate, not that unseen state
or the owner's design acceptance.

## Evidence and next step

Section reports: original-receptionist-cleanup-20261010.md,
original-websites-lab-cleanup-20261010.md,
original-cleanup-parent-review-20261011.md,
legal-continuity-clarification-20261011.md.

Private browser captures/results and source hashes remain outside Git under
C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/.

Review this cleanup before adding imagery or textures. Any later asset should
serve a specific need in the original design. A future release must integrate
this older-base candidate deliberately with current main; preserve both histories.
