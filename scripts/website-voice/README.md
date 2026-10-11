# Website voice transport

This is a disabled-by-default integration candidate. No real provider call or physical microphone privacy test was performed for this change.

## Browser contract

Load `assets/js/website-voice-transport.js`. Create a new instance for each connection attempt with `CallMeIEVoiceTransport.create(options)`. Call `connect()` directly from the user's start action. It starts AudioContext resume and microphone permission before any awaited admission request.

Options require `apiBase` and `onEvent`. Supply either existing `capability`, `sessionId`, `assistantId`, or an async `prepareSession()` callback that returns those three fields. The callback runs after the closed media graph and SDK are available. It cannot override provider settings. A session that arrives after cancellation is sent to the backend end route without SDK start.

`connect()` resolves `{callId}` after join with the input closed. `setInput(true)` returns false before readiness. `setInput(false)`, `end()` and `dispose()` close input immediately. End stops captured and controlled tracks before network cleanup. Each instance has one connection attempt.

Events have `type` equal to `ready`, `speech-start`, `speech-end`, `transcript`, `error` or `ended`. Transcript events include `text`, `role`, and `final`. Errors include safe `error` and `message` fields. `ended` confirms local closure, not server termination. An unconfirmed backend end produces `termination-pending`.

The default end request is POST `{apiBase}/sessions/{sessionId}/end`, Bearer capability, JSON `{operationId}`. Supply `endSession({sessionId,callId})` if the integration needs a different approved backend contract. The browser receives no private provider key.

## Controlled input and limits

The captured microphone track, Web Audio gain and controlled destination track start closed. Only the controlled track reaches Daily. Release disables capture, zeros gain and disables output before SDK mute. SDK recovery cannot restore the captured raw stream. Blur and document hiding close the gate. The controller must also close on pointer cancellation, keyboard release and lost focus.

Release gates input. It does not commit a provider turn, cancel an assistant response, or guarantee half-duplex behavior. Real Chromium, Safari and mobile capture, transmitted-audio silence, permission, autoplay, device loss, end reconciliation and provider latency still need acceptance before enablement.

## Reproducible vendor build

The lock pins `@vapi-ai/web` 2.7.1, Daily 0.87.0 and esbuild 0.28.2. Copy package.json and package-lock.json to an external build directory. Run `npm ci --prefix <build-directory> --ignore-scripts`, then `node scripts/website-voice/build.cjs <build-directory>`. No node_modules belongs in the site repository.

The build rejects a changed upstream SDK hash. Its small patch requires a supplied audio track, sets startAudioOff, disables camera and audio processor replacement, and ends on processor recovery instead of unmuting. It keeps the upstream API/client and Daily implementation. The resulting same-origin bundle, hashes, exact patches and dependency integrity values are recorded in `assets/vendor/website-voice/manifest.json`; license files accompany it. No runtime CDN import is used.

## Verification evidence

External evidence is under `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/`:

- `website-voice-transport-tests.cjs`: 11 injected lifecycle and cancellation tests.
- `website-voice-transport-test-results.json`: test receipt.
- `website-voice-audio-graph.cjs`: Chromium synthetic oscillator through the actual transport graph, with an injected SDK and no provider requests.
- `website-voice-audio-graph-results.json`: closed RMS 0, held RMS approximately 0.70, released RMS 0 even after controlled-track unmute; capture stopped on end.

These tests prove the tested local graph and lifecycle paths. They do not prove physical microphone or provider transport behavior.
