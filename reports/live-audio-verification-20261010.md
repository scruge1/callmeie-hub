# Live audio verification — 10 October 2026

Published revision: `06dcc58b2f7e30b040030cda2b03d2699682d3f8`.

Target: https://callmeie.ie/receptionist/. The parent confirmed successful Pages and cohesion runs before this check.

| Browser | Width | Playback and pause | 50% seek | Keyboard seek | Range response | Result |
| --- | ---: | --- | ---: | --- | ---: | --- |
| Chrome | 390 | Passed | 15.973 s | Passed | 206 | Passed |
| Chrome | 1280 | Passed | 15.973 s | Passed | 206 | Passed |
| WebKit | 390 | Passed | 16.000 s | Passed | 206 | Passed |
| WebKit | 1280 | Passed | 16.000 s | Passed | 206 | Passed |

These checks used the actual public audio endpoint without request interception. Playback advanced the media clock. Pause stopped playback. The range control changed the actual media position; ArrowRight advanced it again. All cases rendered 120 waveform bars and an accessible time label. No horizontal overflow or browser errors were recorded.

All four normal viewport screenshots were opened and visually reviewed. The receiver image and player form one composition. Desktop controls remain within the initial viewport. Mobile controls are readable, aligned, and unclipped. The enhanced player has no native audio chrome.

Private evidence remains outside Git under `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/live-audio-final/`: `results.json`, `chrome-390-top.png`, `chrome-1280-top.png`, `webkit-390-top.png`, and `webkit-1280-top.png`. The external verification script is `check-live-audio-final.cjs` in the same task output root.

No site source changed during live verification. No forms, provider actions, phone calls, payments, or authenticated administration were exercised. The parent owns the separate live asset-hash and five-page visual checks.
