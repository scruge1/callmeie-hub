# Owner screenshot corrections and refreshed voice samples

## Scope and status

Local candidate on top of published original cleanup5f42901.
Published and verified as `d63bf9e`; see the live evidence below.
The owner's screenshot batch was retrieved from Swarm intake and all eight
images were actually viewed. Independent normal WebKit393 views reproduced
the label collisions, split phone number, covered footer and missing logo.
Earlier overflow checks and small contact sheets missed these visual faults.

## Corrections

Restore the exact existing graphical logo in Home and shared parent headers.
Use its burgundy#5a1420 and paper#f5f1e8 with the original Fraunces/Inter
typography and layouts. The logo PNG remains unchanged; CSS frames its existing
padding. The secondary Websites header identifies the page rather than
repeating a conflicting orange badge. Demo bodies keep their own art direction.

Mobile section labels span a full row above their headings and use Inter.
Phone CTAs separate the location from an unbroken number. Dock-bearing pages
reserve64px plus safe-area bottom space. Footer provider and legal links must
remain above the dock at maximum scroll.

## Audio provenance

Three short fictional two-speaker excerpts replace the old Claire sample:
Claire takes a cafe booking; Conor takes a trade callback request; Cillian takes
a professional enquiry. The scripts contain no real customer information.
They illustrate different call types without claiming a booking integration,
legal advice or a universal plan inclusion.

Provider reads confirmed the currently configured approved voices and
eleven_v4_turbo. Only media synthesis and transcription requests were made;
no assistant, telephone route or provider configuration was changed.
Fifteen synthesis segments total965 text characters. Segments were decoded
to mono44100Hz PCM before assembly with250ms gaps, normalized to a-18LUFS
target, and encoded as128kbps MP3. Decoding found no clipped samples.
Scribe_v2 transcripts match the approved dialogue, allowing punctuation and
spelling differences. No human listening assessment is claimed by that check.

- Claire:24.52s; SHA25631a1f1c447e8519cba9c2dd46a463ae82c8c2dc1926560a3e7415ff81cf8f499.
- Conor:21.88s; SHA256da4b4750346828f5ace1cd434bf0bfcd5bee190b94e76f27b8a7a0ecfa982ed4.
- Cillian:20.68s; SHA25616dd0c0a5b8d0005fb06eb4fa8eac48b7ce5e4cb85a3ce59f5f4895c0f50af2f.

The custom player switches voice, title, context and measured waveform.
Changing voice pauses the old sample and resets time without autoplay.
Native controls and direct alternatives remain available without JavaScript.
An explicitly hidden native caption avoids naming Claire under other voices.

## Verification and limits

Initial local playback passed15 actual Chrome/WebKit cases at320/390/1280,
including play, pause, seek, keyboard input,206 media responses, exact waveform
heights and source-switch behavior. Both engines passed native fallback checks.
Final unobscured selected-player and single-frame visuals passed in both engines.
The owner-image states passed at320/393/768/1280 across five routes. Normal
Home/About/Websites/Lab views passed, including aligned Home logo/hero edges.
The80-page/four-context matrix completed320 cases with HTTP200, no page-wide
overflow or page errors. All35 parent pages were repeated against final styles:
140 cases, no label collisions or covered footer bands, and two typefaces.
Existing closed-menu and decorative flags were checked against the prior matrix.
Normal follow-up found actual narrow Financial demo heading/signature clipping;
bounded local responsive corrections retain that demo's own design.
The Vet heading's four-pixel excess remains verified underline decoration.
Chrome audio metadata requests can finish with ERR_ABORTED after successful
206 media loading; actual playback checks passed in both engines.

Private attachments, synthesis receipts, transcripts and browser captures stay
outside Git atC:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/.
GitNexus impact lookups for existing player helpers returned target-not-found;
graph coverage is unavailable. The required staged change check was attempted
and failed because this worktree is unregistered. Direct review verifies108
expected paths,235 browser files, unchanged inline scripts and unchanged legal
main text. Whitespace and injection checks pass. Graph coverage is not claimed.

Push-to-talk remains a proposal. No new live microphone/voice backend or
rig/home/Hetzner service was activated by this media and layout work.

## Verified live release

Published source: `d63bf9e5d66822ddb37d670eb59a7f2fc424a9d3`.
Normal fast-forward publication preserved the original cleanup and later histories.
Cohesion run38101839954 and Pages run38101839806 succeeded. All235 live browser
files match committed Git blob bytes. Independent live checks passed the owner
image states, Home/About/Websites/Lab and three-voice playback. These are bounded
browser checks, not physical iPhone testing or owner design acceptance.

GitHub evidence:
- https://github.com/scruge1/callmeie-hub/actions/runs/38101839954
- https://github.com/scruge1/callmeie-hub/actions/runs/38101839806

Private receipts remain outside Git:
- owner-release-live-bytes.json:235 exact live Git-blob matches.
- owner-release-live/verification.md:11 normal owner-state captures inspected.
- playwright/live-brand-d63bf9e/results.json:8 normal parent cases,4 gallery
  views inspected;11 Website/20 Lab preview nodes decoded at390/1280.
- playwright/three-voice-live-d63bf9e/verification.md:6 actual voice playback
  cases and2 native fallback cases;6 normal selected-player views inspected.

Live controls, waveforms, labels, phone groups, logo and footer clearance pass.
No physical iPhone or owner design acceptance is claimed. No phone calls,
submissions or provider configuration writes. Push-to-talk remains a proposal.
