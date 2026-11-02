/* Progressive enhancement: the original media element remains the playback source. */
(() => {
  'use strict';
  const icon = playing => playing ? '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zm8 0h4v16h-4z"/></svg>' : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m8 4 12 8-12 8z"/></svg>';
  const format = seconds => Number.isFinite(seconds) ? `${Math.floor(seconds / 60)}:${String(Math.floor(seconds % 60)).padStart(2, '0')}` : '0:00';
  document.querySelectorAll('audio[data-voice-player]').forEach(audio => {
    const panel = document.createElement('section');
    panel.className = 'voice-player';
    panel.setAttribute('aria-label', 'Sample call audio player');
    panel.innerHTML = `<p class="voice-player__label">Listen to a sample call</p><h2 class="voice-player__title">Claire takes a café booking.</h2><p class="voice-player__context">Hear the receptionist confirm the caller’s booking details.</p><div class="voice-player__transport"><button class="voice-player__toggle" type="button" aria-label="Play sample call">${icon(false)}</button><div class="voice-player__track"><svg class="voice-player__wave" viewBox="0 0 600 48" preserveAspectRatio="none" aria-hidden="true"></svg><input class="voice-player__seek" type="range" min="0" max="100" step="0.1" value="0" disabled aria-label="Seek within sample call"></div></div><div class="voice-player__meta"><p class="voice-player__status" role="status">Ready to listen</p><span class="voice-player__time">0:00 / 0:00</span></div>`;
    const toggle = panel.querySelector('button');
    const seek = panel.querySelector('input');
    const status = panel.querySelector('[role="status"]');
    const time = panel.querySelector('.voice-player__time');
    const wave = panel.querySelector('svg.voice-player__wave');
    const update = () => {
      const duration = audio.duration;
      seek.disabled = !Number.isFinite(duration) || duration <= 0;
      if (!seek.disabled) seek.value = String(audio.currentTime / duration * 100);
      seek.setAttribute('aria-valuetext', `${format(audio.currentTime)} of ${format(duration)}`);
      time.textContent = `${format(audio.currentTime)} / ${format(duration)}`;
    };
    const state = () => {
      toggle.innerHTML = icon(!audio.paused);
      toggle.setAttribute('aria-label', audio.paused ? 'Play sample call' : 'Pause sample call');
      status.textContent = audio.ended ? 'Sample finished' : audio.paused ? 'Paused' : 'Playing';
      update();
    };
    toggle.addEventListener('click', async () => {
      if (!audio.paused) { audio.pause(); return; }
      status.textContent = 'Loading sample…';
      try { await audio.play(); } catch { status.textContent = 'Unable to play. Try again or call the demo line.'; }
    });
    seek.addEventListener('input', () => { if (Number.isFinite(audio.duration)) audio.currentTime = Number(seek.value) / 100 * audio.duration; update(); });
    ['loadedmetadata', 'durationchange', 'timeupdate'].forEach(event => audio.addEventListener(event, update));
    ['play', 'pause', 'ended', 'playing'].forEach(event => audio.addEventListener(event, state));
    audio.addEventListener('waiting', () => { status.textContent = 'Loading sample…'; });
    const failure = () => { status.textContent = 'Sample unavailable. Call the demo line instead.'; toggle.disabled = true; seek.disabled = true; };
    audio.addEventListener('error', failure);
    audio.after(panel);
    audio.hidden = true;
    update();
    if (audio.error) failure();
    fetch('/assets/audio/claire-cafe-booking-waveform.json').then(response => { if (!response.ok) throw new Error('Waveform unavailable'); return response.json(); }).then(peaks => {
      wave.innerHTML = peaks.map((peak, index) => { const height = Math.max(2, peak * 44); return `<rect x="${index * 5}" y="${(48 - height) / 2}" width="2.5" height="${height}" fill="currentColor"/>`; }).join('');
    }).catch(() => { wave.hidden = true; });
  });
})();
