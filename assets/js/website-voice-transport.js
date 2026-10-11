/* CallMeIE website voice transport. No provider call occurs before connect().
 * A closed Web Audio gain and disabled capture track protect the input before
 * SDK join. This candidate still needs real transmitted-audio qualification.
 */
(function (global) {
  'use strict';
  const vendorPath = '/assets/vendor/website-voice/vapi-2.7.1-ptt.js';
  let vendorLoad;

  function loadSDK() {
    if (global.CallMeIEVapi?.default) return Promise.resolve(global.CallMeIEVapi.default);
    if (!vendorLoad) vendorLoad = new Promise((resolve, reject) => {
      const script = global.document.createElement('script');
      script.src = vendorPath;
      script.onload = () => global.CallMeIEVapi?.default
        ? resolve(global.CallMeIEVapi.default) : reject(new Error('sdk-unavailable'));
      script.onerror = () => { vendorLoad = null; reject(new Error('sdk-unavailable')); };
      global.document.head.appendChild(script);
    });
    return vendorLoad;
  }

  function create(options) {
    const opts = { ...(options || {}) };
    const deps = opts.dependencies || {};
    const media = deps.mediaDevices || global.navigator?.mediaDevices;
    const Context = deps.AudioContext || global.AudioContext || global.webkitAudioContext;
    const sdkLoader = deps.loadSDK || loadSDK;
    const fetcher = deps.fetch || global.fetch?.bind(global);
    let sdk, context, capture, source, gain, destination, output;
    let generation = 0, pending = null, ready = false, disposed = false;
    let inputOpen = false, terminal = false, endedEmitted = false, callId = null;
    let backendEnd = null, localCleanup = null;
    const removers = [];
    const players = new Set();

    function emit(event) {
      try { opts.onEvent?.(event); } catch (_) { /* Consumer errors cannot open capture. */ }
    }
    function aborted() {
      const error = new Error('Connection cancelled.');
      error.name = 'AbortError';
      return error;
    }
    function current(attempt) { return generation === attempt && !terminal && !disposed; }
    function closeGate() {
      inputOpen = false;
      capture?.getAudioTracks().forEach(track => { track.enabled = false; });
      if (gain) {
        gain.gain.cancelScheduledValues(context.currentTime);
        gain.gain.setValueAtTime(0, context.currentTime);
      }
      if (output) output.enabled = false;
      try { sdk?.setMuted(true); } catch (_) { /* The source gate is independent. */ }
    }
    function stopCapture() {
      closeGate();
      capture?.getTracks().forEach(track => track.stop());
      destination?.stream.getTracks().forEach(track => track.stop());
      source?.disconnect();
      gain?.disconnect();
      players.forEach(player => {
        try { player.pause(); player.srcObject = null; player.remove(); } catch (_) {}
      });
      players.clear();
      if (context && context.state !== 'closed') {
        Promise.resolve(context.close()).catch(() => {});
      }
    }
    function bounded(promise) {
      if (!global.setTimeout) return promise;
      let timer;
      const deadline = new Promise((_, reject) => {
        timer = global.setTimeout(() => reject(new Error('cleanup-pending')), 5000);
      });
      return Promise.race([promise, deadline]).finally(() => global.clearTimeout(timer));
    }
    function notifyBackendEnd() {
      if (backendEnd) return backendEnd;
      // A cancelled pending admission can still return a session later.
      // Do not memoize a no-op before that session identity exists.
      if (!opts.sessionId) return Promise.resolve();
      backendEnd = bounded(Promise.resolve().then(async () => {
        if (opts.endSession) return opts.endSession({ sessionId: opts.sessionId, callId });
        if (!opts.apiBase || !opts.capability || !opts.sessionId || !fetcher) return;
        const response = await fetcher(opts.apiBase.replace(/\/$/, '') + '/sessions/'
          + encodeURIComponent(opts.sessionId) + '/end', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + opts.capability },
          body: JSON.stringify({ operationId: opts.operationId || opts.sessionId }),
          keepalive: true
        });
        if (!response.ok) throw new Error('termination-pending');
      })).catch(() => {
        emit({ type: 'error', error: 'termination-pending', message: 'Connection closed. Server termination is not yet confirmed.' });
      });
      return backendEnd;
    }
    function stopSDK(instance) {
      if (!instance) return Promise.resolve();
      try { instance.send?.({ type: 'end-call' }); } catch (_) {}
      try { return bounded(Promise.resolve(instance.stop())).catch(() => {}); } catch (_) { return Promise.resolve(); }
    }
    function end() {
      terminal = true;
      ready = false;
      generation += 1;
      stopCapture();
      if (!localCleanup) localCleanup = stopSDK(sdk);
      if (!endedEmitted) { endedEmitted = true; emit({ type: 'ended' }); }
      return Promise.all([localCleanup, notifyBackendEnd()]).then(() => undefined);
    }
    function fail(code, message) {
      closeGate();
      emit({ type: 'error', error: code, message });
      void end();
    }
    function observe(instance, attempt) {
      const on = (name, fn) => {
        instance.on(name, fn);
        removers.push(() => instance.removeListener?.(name, fn));
      };
      on('call-start', () => {
        if (!current(attempt)) { void stopSDK(instance); return; }
        closeGate();
      });
      on('call-end', () => { if (current(attempt)) void end(); });
      on('speech-start', () => { if (current(attempt)) emit({ type: 'speech-start' }); });
      on('speech-end', () => { if (current(attempt)) emit({ type: 'speech-end' }); });
      on('message', message => {
        if (!current(attempt) || message?.type !== 'transcript') return;
        emit({ type: 'transcript', text: String(message.transcript || ''),
          role: message.role, final: message.transcriptType === 'final' });
      });
      on('audio', player => {
        if (!current(attempt)) { player.pause?.(); player.remove?.(); return; }
        players.add(player);
      });
      on('error', event => {
        if (!current(attempt)) return;
        if (event?.type === 'audio-start-failed') {
          closeGate();
          emit({ type: 'error', error: 'audio-blocked', message: 'Audio could not start. End and reconnect using the button.' });
          return;
        }
        fail('transport-error', 'The voice connection stopped. Try again.');
      });
    }
    function setInput(open) {
      if (!open) { closeGate(); return true; }
      if (!ready || terminal || disposed || context?.state !== 'running'
          || output?.readyState !== 'live' || !capture?.getAudioTracks().length) return false;
      try {
        sdk.setMuted(false);
        output.enabled = true;
        capture.getAudioTracks().forEach(track => { track.enabled = true; });
        gain.gain.setValueAtTime(1, context.currentTime);
        inputOpen = true;
        return true;
      } catch (_) {
        fail('input-unavailable', 'The microphone is unavailable.');
        return false;
      }
    }
    function connect() {
      if (disposed || terminal) return Promise.reject(aborted());
      if (pending) return pending;
      if (!opts.apiBase || (!opts.prepareSession && (!opts.capability || !opts.sessionId || !opts.assistantId))) {
        return Promise.reject(new Error('Voice session configuration is incomplete.'));
      }
      if (!media?.getUserMedia || !Context) return Promise.reject(new Error('Microphone access is unavailable.'));
      const attempt = ++generation;
      // Create/resume in the user's activation, before awaiting microphone permission.
      context = new Context();
      const resume = Promise.resolve(context.resume());
      pending = (async () => {
        try {
          const stream = await media.getUserMedia({ audio: { echoCancellation: true }, video: false });
          if (!current(attempt)) { stream.getTracks().forEach(track => track.stop()); throw aborted(); }
          capture = stream;
          capture.getAudioTracks().forEach(track => { track.enabled = false; });
          await resume;
          if (!current(attempt)) throw aborted();
          source = context.createMediaStreamSource(capture);
          gain = context.createGain();
          gain.gain.setValueAtTime(0, context.currentTime);
          destination = context.createMediaStreamDestination();
          source.connect(gain); gain.connect(destination);
          output = destination.stream.getAudioTracks()[0];
          if (!output || context.state !== 'running') throw new Error('input-gate-unavailable');
          output.enabled = false;
          capture.getAudioTracks().forEach(track => track.addEventListener('ended', () => {
            if (current(attempt)) fail('device-lost', 'The microphone disconnected.');
          }));
          context.onstatechange = () => {
            if (current(attempt) && context.state !== 'running') fail('input-gate-stopped', 'The microphone connection paused.');
          };
          const SDK = await sdkLoader();
          if (!current(attempt)) throw aborted();
          if (opts.prepareSession) {
            const session = await opts.prepareSession();
            if (!session?.capability || !session?.sessionId || !session?.assistantId) {
              throw new Error('session-unavailable');
            }
            opts.capability = session.capability;
            opts.sessionId = session.sessionId;
            opts.assistantId = session.assistantId;
            if (!current(attempt)) { await notifyBackendEnd(); throw aborted(); }
          }
          sdk = new SDK(opts.capability, opts.apiBase.replace(/\/$/, ''),
            { avoidEval: true }, { audioSource: output, startAudioOff: true });
          observe(sdk, attempt);
          const instance = sdk;
          const call = await instance.start(opts.assistantId, undefined, undefined, undefined,
            undefined, { roomDeleteOnUserLeaveEnabled: true });
          if (!current(attempt)) { await stopSDK(instance); throw aborted(); }
          if (!call?.id) throw new Error('call-unavailable');
          callId = call.id;
          closeGate();
          ready = true;
          emit({ type: 'ready' });
          return { callId };
        } catch (error) {
          if (current(attempt)) {
            const permission = error?.name === 'NotAllowedError';
            fail(permission ? 'permission-denied' : 'connection-failed',
              permission ? 'Microphone permission was not granted.' : 'The voice connection could not start.');
          } else stopCapture();
          throw error;
        }
      })();
      // A delayed resume rejection must not become an unhandled promise while permission is pending.
      resume.catch(() => {});
      return pending;
    }
    const closeOnHide = () => { if (global.document?.hidden) closeGate(); };
    const closeOnBlur = () => closeGate();
    global.addEventListener?.('blur', closeOnBlur);
    global.document?.addEventListener('visibilitychange', closeOnHide);
    function dispose() {
      disposed = true;
      global.removeEventListener?.('blur', closeOnBlur);
      global.document?.removeEventListener('visibilitychange', closeOnHide);
      removers.splice(0).forEach(remove => remove());
      return end();
    }
    return { connect, setInput, end, dispose };
  }
  global.CallMeIEVoiceTransport = Object.freeze({ create });
})(window);
