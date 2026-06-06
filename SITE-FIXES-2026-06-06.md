# CallMeIE site fixes — 2026-06-06

Source of live callmeie.ie = this `callmeie-hub` (live `<head>` matches; CF-served). Box folder `Claude/Callmeie` (7 phone screenshots, uploaded today) = Adam's evidence of the stale legal copy below.

Company is NOW incorporated: **CallMeIE Technologies Ltd, CRO 816273, incorporated 21 May 2026** (terms.html:79 + dpa.html:156/157 already say this correctly). The pages below LAG and still say sole-trader / pending / "trading as" / "until incorporation".

## Fix 1 — stale "sole trader / pending incorporation" copy (6 spots, OURS only)

| File:line | Current (stale) | Fix to |
|---|---|---|
| privacy.html:83 | "Until CallMeIE Technologies Ltd is incorporated and CRO-listed, the data Controller… is **Adam Vaughan**, an Irish VAT-registered **sole trader**… Upon incorporation, Adam Vaughan may assign and novate…" | Controller IS **CallMeIE Technologies Ltd** (CRO 816273, incorporated 21 May 2026), VAT-registered, Limerick. Drop the assignment-pending paragraph (assignment is done). |
| privacy.html:199 | "the legal entity is **CallMeIE Technologies (Adam Vaughan trading as)**" | "the legal entity is **CallMeIE Technologies Ltd** (CRO 816273)" |
| privacy.html:253 | "**Until Ltd incorporation**, the data-protection contact is Adam Vaughan… a DPO will be appointed **if and when CallMeIE Technologies Ltd reaches a scale**…" | "The data-protection contact is **Adam Vaughan, Director of CallMeIE Technologies Ltd**, at hello@callmeie.ie. No DPO appointment under Art 37 (threshold not crossed); one will be appointed if scale requires." (drop "Until Ltd incorporation") |
| index.html:72 | "**Sole-trader → Ltd assignment-on-incorporation** clause." | drop / reword — incorporation complete |
| index.html:84 | "CallMeIE Technologies — formal entity name (**Adam Vaughan trading as until Ltd incorporation**; assignment-on-incorporation clause…)" | "**CallMeIE Technologies Ltd** (CRO 816273, incorporated 21 May 2026)" |
| about.html:314 | "Limited company **registration pending**." | "**CallMeIE Technologies Ltd — CRO 816273** (incorporated 21 May 2026)." |

**NOT ours — leave:** plumber.html/electrician.html "sole trader" (client demo copy about THEIR customers); accountant/dental/salon "depending" fee lines; admin.html "pending" (queue status code).

## Fix 2 — favicon (no favicon in Google results)

Live state verified: `favicon.png` (32×32) + `favicon.svg` + `og-image.png` (1200×630, good) all 200. BUT:
- `/favicon.ico` → **404**, `/apple-touch-icon.png` → **404**
- favicon declared `sizes="32x32"` — **Google requires ≥48×48** → shows default globe
- `<link href="favicon.svg">` is **relative** → breaks on sub-paths

Fix (source mark = existing `favicon.svg`, navy #1d3557 doc glyph — fine to reuse, or swap if Adam has a better logo):
- Generate `favicon.ico` (16+32+48 multi-res), `favicon-96.png`, `favicon-192.png`, `apple-touch-icon.png` (180×180) from favicon.svg (rig/Pillow/ImageMagick).
- In every page `<head>`: absolute paths; add `<link rel="icon" href="/favicon.ico" sizes="any">`, `<link rel="icon" type="image/png" sizes="48x48" href="/favicon-96.png">`, `<link rel="apple-touch-icon" href="/apple-touch-icon.png">`, keep svg.
- **FAVICON SOURCE FOUND (Adam was right):** `callmeie-hub/receptionist/assets/callmeie-icon.png` = **1254×1254**, the real brand mark (maroon "C" + phone handset on cream). Use THIS for favicon.ico/96/192/apple-touch + schema logo — not the weak 32px doc-glyph svg currently live.
- og-image: **no change** (already correct + good design).

## Fix 4 — Google visibility: result thumbnail + Knowledge Panel (Adam asks)

**Result thumbnail (image right of the link):** cannot be forced — Google chooses. Make ELIGIBLE: og-image (have), schema `ImageObject` + logo upgraded to the 1254 PNG, strong crawlable hero image. Shows mostly on mobile / image-rich results.

**Knowledge Panel ("celebrity wiki box at top"):** earned over weeks, levers (all route to OWNED infra):
1. **Google Business Profile** — primary. Verified GBP = the brand info box. Use swarm.agent.2026 Google account + SEO control plane → claim/verify "CallMeIE Technologies, Limerick."
2. **Organization schema + `sameAs`** — index.html already has founder/foundingDate/sameAs; enrich sameAs with real social URLs + upgrade `logo` to `https://callmeie.ie/callmeie-icon.png` (1254 mark, ≥112px Google min).
3. **Wikidata item** for the company (no Wikipedia notability bar) — feeds entity graph.
4. **`jake-van-clief-icm/.../shared/citation_pack.py`** — already built; run for CallMeIE → consistent NAP authority.
NOT instant, NOT guaranteed; GBP is the fastest concrete step.

## Fix 3 — deploy

Confirm callmeie-hub → callmeie.ie deploy path (Cloudflare Pages git-push? Astro build?) BEFORE pushing, so fixes go live + favicon files land at site root. Re-verify live: `/favicon.ico` 200, privacy page copy updated.
