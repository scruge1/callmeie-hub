# CallMeIE brand restoration — 10 October 2026

## Result and authority

The first consolidation reduced copy but moved away from Adam's established
identity. This correction uses the Great National v1 proposal renderer and
rendered pages: warm paper, deep ink, burgundy, Archivo Black and IBM Plex Sans,
with the original icon/wordmark. The proposal's editorial notes preserve that
identity while cutting repeated and internal narration.

Recovered design history is in design-history-20261010.md. Business demos remain
distinct from the experimental Lab gallery. No forced heading breaks, decorative
final-word colours or emoji are added. Existing demo motion is retained.

Generated paper and handset WebP assets add material and a service-related visual.
assets/brand/README.md records the prompts and generation/export method. The
handset is a still, not an interactive 3D implementation. Actual continuous 3D
remains conditional on usefulness, with the accepted Oceanic workflow available.

The shared header/footer and Lab now follow the same brand. Product copy removes
repeated sales narration and unsupported claims while retaining approved pricing,
coverage and legal/form boundaries. Product implementation has its own report.
Demo return controls no longer cover the three affected fixed headers; sample06
mobile links use their own row; the bottom gallery dock now follows page content.
The sample05 mobile logo/action, sample04 footer wordmark and sample06 contact
address now fit. All10 industry samples use a clear house-style CallMeIE enquiry
form without the old24-hour promise or internal admin narration.

## Fresh verification

Local preview: http://127.0.0.1:8769/.
External evidence: C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/.
Base release: 4cac3375b91b75b119fdb49e3bb3c70947f52f38.

- 94 public HTML entries:80 content pages and14 redirect stubs.
- 320 runtime scenarios:Chromium154 at768/1280; WebKit26.4 at375/390.
- Final Home/Websites heading changes separately rechecked in all8 scenarios.
- Final shared header checked across35 pages at320/375/390:105 WebKit scenarios,
  including open dropdowns, control overlap and44px contact targets; zero failures.
- Follow-up demo/form scenarios cover every affected sample after its final edit.
- Zero page overflow, runtime errors or failed resources in accepted results.
- 179 source/asset hashes pinned, no drift at acceptance.
- Known raw gate findings remain recorded:local table scroll, offscreen
  honeypots, empty native form controls and intentional sample artwork. The raw
  gate is not represented as zero findings.
- Shared partial check:91 pages, zero drift. Local links:zero missing targets.
- All80 content pages visually viewed at375/1280 by the section agents. Settled
  demo viewports and separate normal footer/form captures resolve screenshot
  animation artefacts. Final10 enquiry forms viewed at both widths.

Current full-page screenshots can restart demo ScrollTrigger/SplitText animation.
Dedicated settled viewport images are captured before full-page images and are
used to review the actual hero. Earlier malformed-stylesheet and mid-animation
captures are retained as rejected evidence, not used to certify the final design.

Final visual coverage and publication status are recorded in ACTIVE-CHECKPOINT.md.
Technical verification does not imply Adam's visual acceptance or physical-device
performance. Authenticated administration and live form submission are outside
this public-site review; no customer messages were sent.

## Change analysis

JavaScript changes are limited to demo-form presentation strings. Submission,
routing and state handlers remain unchanged. The shared helper is loaded by all10
industry sample pages; the manual callsite search establishes its actual scope.
GitNexus impact was attempted for the anonymous helper against the parent index:
target not found, risk unknown, FTS extension unavailable. This is a lookup limit,
not a clean impact result. GitNexus detect-changes ran against
the existing parent repository:low risk, zero affected processes, with an FTS
extension warning. That index covers unrelated parent changes and is not a
candidate-specific impact proof for this isolated worktree. The public-site
runtime, source diff and shared-partial checks are the relevant verification.

## Published verification

Source release:adc21bc5b8cb04b6ab4294b9362700d92c522a1c. Pages run38085385084 and cohesion38085385236
succeeded. Actual live WebKit390/1280 verification passed on Home, Websites,
Lab, Receptionist and Privacy. Correct Archivo/Plex fonts and original wordmark
are present; the handset and all gallery previews load; no page overflow or
browser errors. Ten actual served files match Git release bytes exactly.
Evidence:external output/live-restoration-verification.json,
live-restoration-hashes.json and output/playwright/live-restoration-* captures.
Main visually viewed the actual live Home/mobile and Lab/desktop captures.
This final receipt changes documentation only; site source remains identical.
GitNexus detect-changes was also attempted against the exact worktree before
the receipt commit; it is not registered in that index. Manual Git diff confirms
the receipt is limited to ACTIVE-CHECKPOINT.md, README.md and this report.
