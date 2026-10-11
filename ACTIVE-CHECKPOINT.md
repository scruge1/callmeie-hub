# CallMeIE original design cleanup

## Current truth — 11 October 2026

Adam asked to return carefully to the good original design and make gradual
changes to typography, thumbnails, copy and alignment. This supersedes the
replacement art direction. Irish AI phone reception is the main offer;
websites are the secondary offer. New generated imagery, textures and assets
come after review of this cleanup.

Candidate: original `6578619` on branch `review/original-cleanup-20261010`.
Local preview: http://127.0.0.1:8773/.
Adam authorised publication on 11 October 2026. The reviewed browser files
are integrated on top of current main `56fc4be` in the isolated publication
worktree `callmeie-hub-publish-20261011`, branch
`publish/original-cleanup-20261011`. All 228 pinned browser source and asset
files match the reviewed candidate exactly. Preserve both histories.
Publication is pending the commit check, push, deployment and live verification.
The previous rejected visual release is `06dcc58`.
See reports/original-cleanup-publication-20261011.md for release evidence.

The original paper colours, Fraunces headings, section structure and demo
designs remain. Supporting text uses Inter consistently. Website and Lab
previews use real existing thumbnail images. Home and selected service copy
are shorter. Repeated footers and unsupported product claims are removed.
Responsive corrections address menus, controls, headings and local table
scrolling. The working custom audio player is retained with styling that fits
the original design. The obsolete discovery quiz entry points are hidden;
direct contact links remain.

## Completed first-pass verification

The final browser matrix covers 80 content pages at four browser/width
combinations: Chrome 768/1280 and WebKit 320/390. All 320 cases return HTTP 200,
with no page-wide overflow or JavaScript errors. The 14 redirects are listed
separately in the inventory. Agents actually reviewed all 80 content pages at
320/1280, with bounded normal-viewport follow-ups for each confirmed defect.
The admin review covers its unauthenticated gate only.

Actual Website gallery views confirm all 11 previews render. Lab has 20 working
preview references. Clancy's visible mobile and desktop scene images render;
hidden desktop copies can remain lazy and unloaded. Raw detector flags remain
for closed native menus, empty form fields, intentional decoration and a
honeypot. These were inspected rather than treated as automatic failures.
The Vet industry heading's four-pixel excess is underline decoration.

Home/About normal and doubled-text checks pass. This is text enlargement,
not native browser zoom. Open menus fit. The Privacy table and other corrected
tables scroll locally with keyboard focus, with readable columns. Sample audio
passes actual play, pause, seek and keyboard checks in Chrome/WebKit. Disabled
JavaScript and unavailable-audio fallbacks pass. Chrome's metadata fetch can
report ERR_ABORTED after a successful 206 response; direct checks confirm
readyState 4, valid duration and no media error in both affected contexts.

All 228 pinned browser source/asset files match the reviewed bytes. Shared
injection has zero drift; local links have zero missing targets; whitespace
checks pass. See reports/original-cleanup-20261011.md and section reports.
Private screenshots and browser data stay outside Git under
C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/.

Original inline JavaScript blocks are preserved after line-ending normalization.
Audio and sample enquiry helpers are exact copies of verified current versions.
Operative Privacy, Terms and DPA text is unchanged, excluding only the added
legacy DocOps notice and label suffixes. Introductions and metadata describe
current products; the Legal index uses the verified Service provider identity.
No provider writes, phone
calls, real submissions or authenticated admin checks are included.

## Next steps

Review this first cleanup against the original before adding any new assets.
Use one identified need at a time for later imagery or textures. Preserve
the receptionist-first positioning and the original character.

Adam proposed a custom push-to-talk button on11October. Record it as the next
improvement for separate review: press and hold to speak, release to send,
clear listening/reply states and text fallback. It needs a live voice connection
and microphone consent. It is not included in this publication; no new live
voice connection or provider configuration has been authorised by that question.

Publish through a normal fast-forward commit on current main. Verify the
served bytes, real gallery images and audio controls before claiming success.
The reviewed candidate remains recoverable in its original worktree.

The owner's red-marked screenshot remains unread: Swarm Gmail OAuth intake
returned invalid_grant. Browser verification does not prove that specific
owner-reported visual state or establish design acceptance.
