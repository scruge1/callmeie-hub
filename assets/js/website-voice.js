/* Website UI only. The transport owns media; the backend owns calls and records. */
(() => {
  'use strict';
  const isLocal = () => ['localhost', '127.0.0.1', '[::1]'].includes(location.hostname);
  const microphone = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10v2a7 7 0 0 0 14 0v-2M12 19v3M8 22h8"/></svg>';

  function createController(root, config, dependencies = {}) {
    const request = dependencies.fetch || window.fetch.bind(window);
    const factory = dependencies.transportFactory || (options => window.CallMeIEVoiceTransport.create(options));
    const api = new URL(config.api_base, location.href);
    if (api.protocol !== 'https:' && !(isLocal() && api.protocol === 'http:' && ['localhost', '127.0.0.1'].includes(api.hostname))) throw new Error('Invalid voice API');
    let generation = 0, state = 'idle', transport = null, session = null, connected = false, held = false;
    let mode = 'hold', pointer = null, activeKey = null, speaking = false, endPromise = null;
    const listeners = [];
    const endRequests = new Map();
    root.innerHTML = `<div class="website-voice__row"><div class="website-voice__intro"><p class="website-voice__label">Live conversation</p><h3 class="website-voice__title">Talk to Claire.</h3><p class="website-voice__description">Ask about CallMeIE, in your own words.</p></div><div class="website-voice__actions"><button class="website-voice__talk" type="button">${microphone}<span>Start conversation</span></button><button class="website-voice__end" type="button" hidden>End</button></div></div><div class="website-voice__meta"><p class="website-voice__status" role="status" aria-live="polite"><span class="website-voice__indicator" aria-hidden="true"></span><span>Ready when you are</span></p><button class="website-voice__mode" type="button" hidden>Use tap to talk</button></div><p class="website-voice__notice">AI voice demonstration. Start, then hold to speak. <a href="/privacy.html">Privacy</a></p><details class="website-voice__captions" hidden><summary>Show captions</summary><ol aria-live="polite" aria-label="Conversation captions"></ol></details>`;
    root.hidden = false;
    const talk = root.querySelector('.website-voice__talk'), label = talk.querySelector('span');
    const end = root.querySelector('.website-voice__end'), modeButton = root.querySelector('.website-voice__mode');
    const status = root.querySelector('.website-voice__status > span:last-child');
    const captions = root.querySelector('details'), lines = captions.querySelector('ol');
    const listen = (target, type, handler, options) => { target.addEventListener(type, handler, options); listeners.push(() => target.removeEventListener(type, handler, options)); };
    const render = (next, message) => {
      state = next; root.dataset.state = next; status.textContent = message;
      talk.disabled = ['connecting', 'ending'].includes(next);
      label.textContent = next === 'connecting' ? 'Connecting…' : next === 'ending' ? 'Ending…' : connected ? held ? 'Listening' : mode === 'hold' ? 'Hold to talk' : 'Tap to talk' : 'Start conversation';
      talk.setAttribute('aria-label', connected ? held ? 'Microphone open. Release to stop talking' : mode === 'hold' ? 'Hold to talk to Claire' : 'Tap to open microphone' : 'Start conversation with Claire');
      if (connected && mode === 'toggle') talk.setAttribute('aria-pressed', String(held)); else talk.removeAttribute('aria-pressed');
      end.hidden = !connected && next !== 'connecting'; modeButton.hidden = !connected;
      modeButton.textContent = mode === 'hold' ? 'Use tap to talk' : 'Use hold to talk';
    };
    const closeInput = () => {
      held = false; pointer = null; activeKey = null;
      try { transport?.setInput(false); } catch { /* Cleanup continues even after a transport error. */ }
    };
    const release = () => {
      const wasHeld = held; closeInput();
      if (connected && wasHeld) render(speaking ? 'speaking' : 'ready', speaking ? 'Claire is replying · microphone off' : 'Microphone off · hold for your next question');
    };
    const openInput = () => {
      if (!connected || held || ['ending', 'error'].includes(state)) return false;
      try {
        if (!transport.setInput(true)) return false;
        held = true; render('listening', 'Listening · microphone on'); return true;
      } catch { void finish('Voice is unavailable. You can still call or hear the examples.'); return false; }
    };
    const remoteEnd = saved => {
      if (!saved) return Promise.resolve();
      if (endRequests.has(saved.session_id)) return endRequests.get(saved.session_id);
      const operation = (async () => {
        const response = await request(`${api.href.replace(/\/$/, '')}/sessions/${encodeURIComponent(saved.session_id)}/end`, {
          method:'POST', headers:{'Content-Type':'application/json', Authorization:`Bearer ${saved.capability}`},
          body:JSON.stringify({operation_id:crypto.randomUUID()}), keepalive:true, signal:AbortSignal.timeout(8000)
        });
        if (!response.ok) throw new Error('termination-pending');
        const result = await response.json();
        if (!['ended', 'cancelled'].includes(result.connection_state)) throw new Error('termination-pending');
        return result;
      })();
      operation.catch(() => {}); endRequests.set(saved.session_id, operation);
      return operation;
    };
    async function finish(message = 'Microphone off · connection closed') {
      if (endPromise) return endPromise;
      generation++; closeInput();
      const oldTransport = transport, oldSession = session;
      transport = null; session = null; connected = false; speaking = false;
      render('ending', 'Microphone off · ending conversation');
      // end() closes capture synchronously before its async provider cleanup.
      let cleanup;
      try { cleanup = oldTransport?.end(); } catch { cleanup = Promise.resolve(); }
      endPromise = Promise.allSettled([cleanup, remoteEnd(oldSession)]).then(results => {
        endPromise = null;
        render('idle', results[1].status === 'rejected' ? `${message}. Server end is not yet confirmed.` : message);
      });
      return endPromise;
    }
    const addCaption = event => {
      if (!['user', 'assistant'].includes(event.role) || typeof event.text !== 'string' || !event.text.trim()) return;
      let line = lines.lastElementChild;
      if (!line || line.dataset.final === 'true' || line.dataset.role !== event.role) {
        line = document.createElement('li'); line.dataset.role = event.role;
        const who = document.createElement('strong'); who.textContent = event.role === 'user' ? 'You' : 'Claire';
        line.append(who, document.createElement('span')); lines.append(line);
      }
      line.lastElementChild.textContent = event.text.slice(0, 2000); line.dataset.final = String(event.final === true);
      while (lines.children.length > 12) lines.firstElementChild.remove();
      captions.hidden = false;
    };
    async function start() {
      if (connected || state === 'connecting' || state === 'ending') return;
      const attempt = ++generation;
      lines.replaceChildren(); captions.hidden = true;
      render('connecting', 'Connecting · microphone off');
      document.querySelectorAll('audio').forEach(audio => audio.pause());
      let admitted = null, nextTransport = null;
      try {
        if (!dependencies.transportFactory && !window.CallMeIEVoiceTransport) throw new Error('Voice unavailable');
        const prepareSession = async () => {
          const response = await request(`${api.href.replace(/\/$/, '')}/sessions`, {
            method:'POST', headers:{'Content-Type':'application/json'}, signal:AbortSignal.timeout(15000),
            body:JSON.stringify({page:root.dataset.page, operation_id:crypto.randomUUID(), notice_revision:config.notice_revision})
          });
          if (!response.ok) throw new Error('Voice unavailable');
          admitted = await response.json();
          if (typeof admitted.session_id !== 'string' || typeof admitted.capability !== 'string' || admitted.capability.length < 16 || typeof admitted.assistant_id !== 'string') throw new Error('Invalid voice session');
          if (attempt !== generation) { await remoteEnd(admitted); throw new DOMException('Connection cancelled', 'AbortError'); }
          session = admitted;
          return {capability:admitted.capability, sessionId:admitted.session_id, assistantId:admitted.assistant_id};
        };
        // connect() opens/resumes the closed audio graph in this user activation.
        // Admission runs inside it after permission, before any provider creation.
        nextTransport = factory({apiBase:api.href.replace(/\/$/, ''), prepareSession, endSession:() => remoteEnd(admitted), onEvent:event => {
          if (attempt !== generation) return;
          if (event.type === 'transcript') addCaption(event);
          else if (event.type === 'speech-start') { speaking = true; if (connected && !held) render('speaking', 'Claire is replying · microphone off'); }
          else if (event.type === 'speech-end') { speaking = false; if (connected && !held) render('ready', 'Microphone off · ready for your next question'); }
          else if (event.type === 'ended') void finish();
          else if (event.type === 'error') void finish(event.error === 'permission-denied' || event.error?.name === 'NotAllowedError' ? 'Microphone permission was denied. You can still call or hear the examples.' : 'Voice is unavailable. You can still call or hear the examples.');
        }});
        transport = nextTransport;
        await nextTransport.connect();
        if (attempt !== generation) { await nextTransport.end(); await remoteEnd(admitted); return; }
        closeInput(); connected = true; render('ready', 'Microphone off · hold to ask Claire');
      } catch (error) {
        if (attempt !== generation) return;
        const text = error.name === 'NotAllowedError' ? 'Microphone permission was denied. You can still call or hear the examples.' : error.name === 'NotFoundError' ? 'No microphone was found. You can still call or hear the examples.' : 'Voice is unavailable. You can still call or hear the examples.';
        await finish(text);
      }
    }
    listen(talk, 'click', () => { if (!connected) void start(); else if (mode === 'toggle') { if (held) release(); else openInput(); } });
    listen(talk, 'pointerdown', event => {
      if (!connected || mode !== 'hold' || !event.isPrimary || event.button !== 0 || held) return;
      event.preventDefault();
      if (openInput()) { pointer = event.pointerId; talk.setPointerCapture(event.pointerId); }
    });
    listen(talk, 'pointerup', event => { if (pointer === event.pointerId) release(); });
    listen(talk, 'pointercancel', release); listen(talk, 'lostpointercapture', release);
    listen(talk, 'keydown', event => {
      if (!connected || mode !== 'hold' || ![' ', 'Enter'].includes(event.key)) return;
      event.preventDefault(); if (event.repeat || activeKey) return;
      if (openInput()) activeKey = event.key;
    });
    listen(talk, 'keyup', event => { if (activeKey === event.key) { event.preventDefault(); release(); } });
    listen(talk, 'blur', release);
    listen(end, 'click', () => { void finish(); });
    listen(modeButton, 'click', () => { release(); mode = mode === 'hold' ? 'toggle' : 'hold'; render(speaking ? 'speaking' : 'ready', 'Microphone off'); });
    listen(window, 'blur', () => { release(); if (state === 'connecting') void finish(); });
    listen(document, 'visibilitychange', () => { if (document.hidden && (connected || state === 'connecting')) void finish(); });
    listen(window, 'pagehide', () => { if (connected || state === 'connecting') void finish(); });
    listen(document, 'keydown', event => { if (event.key === 'Escape' && (connected || state === 'connecting')) void finish(); });
    listen(document, 'play', event => { if (event.target instanceof HTMLMediaElement && event.target.matches('audio[data-voice-player]') && (connected || state === 'connecting')) void finish(); }, true);
    render('idle', 'Ready when you are');
    return {start, end:finish, getState:() => ({state, connected, held, mode}), dispose:async () => { listeners.forEach(remove => remove()); await finish(); root.hidden = true; }};
  }
  window.CallMeIEWebsiteVoice = {createController};
  async function boot() {
    const mounts = document.querySelectorAll('[data-website-voice]');
    if (!mounts.length) return;
    try {
      const response = await fetch('/assets/website-voice-config.json', {cache:'no-store'});
      if (!response.ok) return;
      const config = await response.json();
      if (isLocal() && new URLSearchParams(location.search).get('voice-preview') === '1') {
        config.enabled = true; config.api_base = 'http://127.0.0.1:8817/api/website-voice';
      }
      if (config.enabled !== true) return;
      mounts.forEach(root => createController(root, config));
    } catch { /* Disabled or unavailable configuration preserves the existing demo. */ }
  }
  void boot();
})();
