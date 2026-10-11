// Rebuild with an isolated npm ci directory supplied as the sole argument.
// Do not run a development server or install dependencies into the website root.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const buildRoot = path.resolve(process.argv[2] || '.');
const modules = path.join(buildRoot, 'node_modules');
const siteRoot = path.resolve(__dirname, '../..');
const output = path.join(siteRoot, 'assets/vendor/website-voice');
const sdkPath = path.join(modules, '@vapi-ai/web/dist/vapi.js');
const original = fs.readFileSync(sdkPath, 'utf8');
const hash = text => crypto.createHash('sha256').update(text).digest('hex');
assert.equal(hash(original), '0123bc2a327bcab91f3f37c373521e41031a8e1d3829645c4e667c35dbc4ab3b');
let patched = original;
function replace(pattern, replacement, expected) {
  const matches = [...patched.matchAll(pattern)].length;
  assert.equal(matches, expected, 'Upstream patch shape changed');
  patched = patched.replace(pattern, replacement);
}
// The CallMeIE transport supplies only its controlled destination track.
replace(/this\.dailyCallObject = \(0, daily_guards_1\.createSafeDailyFactoryOptions\)\(dailyCallObject\);/g,
  '$&\n        if (this.dailyCallObject.audioSource?.kind !== "audio") throw new Error("Controlled audio track required");', 1);
replace(/audioSource: this\.dailyCallObject\.audioSource \?\? true,/g,
  '$&\n                    startAudioOff: true,', 4);
replace(/videoSource: this\.dailyCallObject\.videoSource \?\? isVideoRecordingEnabled,/g,
  'videoSource: false,', 4);
replace(/type: 'noise-cancellation'/g, "type: 'none'", 2);
replace(/if \(e\?\.type === 'audio-processor-error'\) \{[\s\S]*?this\.emitAudioProcessingError\('audio-processor-recovery', error\);[\s\S]*?\}\);\s*\}/g,
  'if (e?.type === "audio-processor-error") {\n                    this.emit("error", { type: "ptt-unsafe-audio-recovery" });\n                    void this.stop();\n                }', 2);
const work = path.join(buildRoot, 'work');
fs.mkdirSync(work, { recursive: true });
fs.mkdirSync(output, { recursive: true });
// Preserve SDK relative api/client/guard modules from the published package.
for (const name of fs.readdirSync(path.dirname(sdkPath))) {
  if (name.endsWith('.js')) fs.copyFileSync(path.join(path.dirname(sdkPath), name), path.join(work, name));
}
fs.writeFileSync(path.join(work, 'vapi.js'), patched);
fs.writeFileSync(path.join(work, 'entry.js'), 'module.exports = { default: require("./vapi").default };\n');
require(path.join(modules, 'esbuild')).buildSync({
  entryPoints: [path.join(work, 'entry.js')], bundle: true, platform: 'browser',
  format: 'iife', globalName: 'CallMeIEVapi', target: ['es2020'],
  minify: true, legalComments: 'eof',
  outfile: path.join(output, 'vapi-2.7.1-ptt.js')
});
const lock = JSON.parse(fs.readFileSync(path.join(buildRoot, 'package-lock.json'), 'utf8'));
const pins = Object.entries(lock.packages).filter(([name]) => name.startsWith('node_modules/'))
  .map(([name, pkg]) => ({ name: name.slice(13), version: pkg.version, integrity: pkg.integrity }));
const manifest = {
  purpose: 'Controlled-source PTT candidate; real media/privacy qualification remains open.',
  sdk: '@vapi-ai/web@2.7.1', daily: '@daily-co/daily-js@0.87.0', build: 'esbuild@0.28.2',
  originalSDKHash: hash(original), patchedSDKHash: hash(patched),
  bundleHash: hash(fs.readFileSync(path.join(output, 'vapi-2.7.1-ptt.js'))),
  patches: ['Require supplied controlled audio track', 'Start Daily input closed and camera disabled',
    'Disable processor replacement', 'End on processor recovery rather than unmute'],
  sources: ['https://registry.npmjs.org/@vapi-ai/web/2.7.1',
    'https://github.com/VapiAI/client-sdk-web', 'https://docs.daily.co/reference/daily-js/types/daily-call-options'],
  pins
};
fs.writeFileSync(path.join(output, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
fs.copyFileSync(path.join(modules, '@daily-co/daily-js/LICENSE'), path.join(output, 'LICENSE-Daily.txt'));
fs.copyFileSync(path.join(modules, 'events/LICENSE'), path.join(output, 'LICENSE-events.txt'));
const readme = fs.readFileSync(path.join(modules, '@vapi-ai/web/README.md'), 'utf8');
const licenseStart = readme.indexOf('MIT License');
assert(licenseStart >= 0);
fs.writeFileSync(path.join(output, 'LICENSE-Vapi.txt'), readme.slice(licenseStart).replace(/```/g, '').trim() + '\n');
const dependencyLicenses = [];
for (const pin of pins) {
  const dir = path.join(modules, pin.name);
  if (!fs.existsSync(dir)) continue;
  const name = fs.readdirSync(dir).find(file => /^licen[sc]e(?:\.|$)/i.test(file));
  if (name && fs.statSync(path.join(dir, name)).isFile()) {
    dependencyLicenses.push(pin.name + '@' + pin.version + '\n' + fs.readFileSync(path.join(dir, name), 'utf8'));
  }
}
fs.writeFileSync(path.join(output, 'LICENSE-dependencies.txt'), dependencyLicenses.join('\n\n---\n\n').trimEnd() + '\n');
console.log(JSON.stringify({ bundleHash: manifest.bundleHash, pins: pins.length }));
