# Website voice local build and layout corrections — 11 October 2026

The local browser control and backend session bridge are implemented. Public
`assets/website-voice-config.json` remains `enabled:false`. This is an integration
candidate, not an accepted live voice service. No provider calls were made.

## Website changes

Home and Receptionist mount a compact control inside their existing layouts.
Start requests microphone access from an explicit user action. Input begins
closed. Hold, keyboard release, pointer cancellation, focus loss and ending
close input. An accessible tap mode and captions are available. Late permission,
admission and join results cannot reopen a cancelled attempt. Prerecorded sample
playback closes the conversation; the assistant's own audio does not.

The pinned Vapi2.7.1/Daily0.87.0 adapter receives only a controlled audio track.
The raw track, gain and output track close before SDK mute. Processor recovery
ends the attempt instead of enabling raw capture. The pinned same-origin bundle
loads only after connection is requested. Build pins, hashes and licences are
retained under `scripts/website-voice/` and `assets/vendor/website-voice/`.

The header now uses the authentic `/callmeie-icon.png`, with its separate dot
above/right, instead of the different wide Receptionist mark. Shared headers
fit at320px. The original layout, paper, burgundy, Fraunces and Inter remain.
Home main content has six size roles: desktop12/14/16/24/36/64px and mobile
12/14/16/24/32/40px. The gap from hero actions to the call demo is56px, down
from about206px in the measured390px view.

Home navigation, footer, signature and consent text now share the same supporting
roles instead of extra11/13/15/17/20px values. The custom voice sample player
remains on Receptionist; no extra player or section is added to Home.
Final visible-text scans at390/1280 confirm exactly six sizes, not only the main
content. Normal top/consent/footer views pass. Home legal links clear WhatsApp
with80px plus safe-area bottom scroll space.

The owner's follow-up exposed a missed thumbnail surface: the ten compact
"Working website concepts" tiles still used one generic placeholder although
the11 large gallery images worked. Those ten tiles and seven Lab teaser tiles
now use their corresponding existing captures. Both groups were actually
viewed at390/1280; modal opening/closing and20 Lab page previews are verified.
No gallery JavaScript or demo design is changed. This supersedes earlier claims
that large-gallery image decoding covered all thumbnail surfaces.

## Backend owner

The isolated backend worktree is
`callmeie-system/development/website-voice-20261011`, branch
`codex/website-voice-20261011`, based on retained source981daca. Its
`WEBSITE-VOICE-CONTRACT.md` and `ACTIVE-CHECKPOINT.md` own exact API and gates.
Local backend commit: `23b97fcb035610c5da439dd40aa044b92e73a7e5`.
It is preserved locally and has not been pushed, merged or deployed.

It implements origin-scoped admission, expiring capabilities, atomic call/time
reservations, server-owned provider association, authenticated end/status and
committed report readback through existing `call_events`. Website demo expense
is internal; customer billable units are zero. The existing phone audit and
notification engines retain their guards. The provider router is inert until
the dedicated published website assistant/version and callback are configured.
No backend deployment, assistant mutation, recording activation or phone change.

## Verification

- 20 browser/UI cases pass, including release, keyboard, accessible mode, safe
 captions, late cancellation, assistant playback and unconfirmed server end.
- 11 injected transport cases pass. An actual browser synthetic audio graph has
 zero output before hold and after release, and active output during hold.
- 19 new HTTP/SQLite cases plus12 existing status and17 final-report cases pass.
 Existing server functions/classes are unchanged. Legacy auth tests have20
 setup errors from installed Starlette/httpx incompatibility; async HTTP tests
 independently exercise the new auth boundary.
- The actual browser, controller, transport and HTTP fixture are joined using
 Chromium's fake microphone and a fake provider. A fictional final report is
 committed and read back through the existing store. End state is confirmed;
 there are no browser errors. No physical microphone or provider media proof.
- Real-wire CORS preflight returns an empty204. This test caught a body-length
 bug missed by the initial ASGI tests; the response and regression are fixed.
- 27 changed pages pass108 Chrome/WebKit contexts at320/390/768/1280: no page
 overflow, clipping or browser errors. Raw flags match previously closed menu
 elements. Normal Home390/1280 and header/control captures were visually reviewed.
- 12 bounded Chrome/WebKit cases pass on Home/Receptionist/Websites at390/1280,
 including all17 compact backgrounds,11 gallery previews, modal open/close,
 correct icon, gap56px and public voice disabled with no vendor request.

Private scripts, captures and detailed results stay outside Git in
`C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/`, notably
`output/website-voice/`, `output/playwright/website-voice-header-20261011/`,
`website-voice-backend-candidate/` and the transport test receipts.

GitNexus impact could not resolve the relevant symbols/index. Staged detection
was attempted and failed because this worktree is unregistered. Graph coverage
is unavailable; direct scope, syntax, layout and integration checks were used.

## Remaining voice acceptance

Qualify the dedicated saved assistant/version, callback credential and knowledge
revision; deployed origin/CORS/HTTPS and PostgreSQL migration; actual provider
association/media; physical iPhone/Android microphone release and cancellation;
business answers, interruption, latency, idle termination and spending ceiling;
explicit webCall usage/dashboard path and any requested enquiry/notification.
Rig/home/Hetzner realtime fallback and optional3D phone remain unqualified.
The local fixture listener is stopped after testing. Public voice remains off.
