# Migration runbook — GitHub Pages → Cloudflare Pages (P2-1 path A)

**Goal:** keep brand promise ("no cookies, no tracking, no banner") AND get operator visibility via Cloudflare Web Analytics (server-side, zero JS injection, zero cookies, zero localStorage).

**State today (2026-05-09 verified):**
- `callmeie.ie` apex → A records `185.199.108.153 / 109.153 / 110.153 / 111.153` = GitHub Pages
- Cloudflare DNS managed in zone `0ed441de9cda4746aa4bbc3c46532c81`, proxied=false
- Static site built from `callmeie-hub` GitHub repo, no build step (plain HTML)
- Resume PRD line 100 ("Cloudflare Pages, GitHub-backed") was stale — corrected here

---

## Step 1 — Create Cloudflare Pages project (Adam-keyboard, ~5 min)

1. Cloudflare dash → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
2. Select GitHub account `scruge`, repo `callmeie-hub`
3. Project name: `callmeie-hub` (becomes `callmeie-hub.pages.dev`)
4. Production branch: `main`
5. Build settings — leave empty:
   - Framework preset: **None**
   - Build command: *(empty)*
   - Build output directory: `/`
6. Environment variables: none needed
7. **Save and Deploy**

First deploy takes ~30 sec. Verify `https://callmeie-hub.pages.dev` serves the live site identical to `https://callmeie.ie`.

## Step 2 — Add custom domain to CF Pages project (Adam-keyboard, ~2 min)

1. In the CF Pages project → **Custom domains** tab → **Set up a custom domain**
2. Enter `callmeie.ie` → Continue → CF auto-creates the DNS record
3. Repeat for `www.callmeie.ie` (CNAME → `callmeie-hub.pages.dev`)

CF DNS apex switches from the four GitHub Pages A records to a CNAME-flattened record pointing to the CF Pages target. SSL via CF's universal cert (LE-backed).

## Step 3 — Verify

```powershell
nslookup callmeie.ie 1.1.1.1     # expect Cloudflare IPs (104.x / 172.x), NOT 185.199.x
curl -I https://callmeie.ie       # expect server: cloudflare, cf-ray header
```

Browse `/`, `/receptionist/`, `/docs/`, `/legal/privacy`, `/lab/`, `/local-seo/` — all 200.

## Step 4 — Enable Cloudflare Web Analytics (Adam-keyboard, ~1 min)

1. CF dash → **Analytics & Logs** → **Web Analytics**
2. **Add a site** → enter `callmeie.ie`
3. Choose **Server-side analytics** (NOT the JS beacon — that one sets cookies)
4. CF binds aggregate counts to the Pages project automatically

That's it. No JS, no `<script>`, no consent banner, no cookies. Audit script `audit-no-cookies.py` stays green.

## Step 5 — Update DPA + privacy.html

DPA Schedule B sub-processors list already includes Cloudflare (DNS + CDN). Add a single line under §6 of `legal/privacy.html`:

> "We use Cloudflare's free Web Analytics to count anonymous, aggregate page visits. It runs server-side at the Cloudflare edge — no JavaScript, no cookies, no device storage. We do not see individual visitors."

Same line, same wording, into DPA §1.6 description.

## Step 6 — Decommission GitHub Pages (no rush)

1. `callmeie-hub` repo → **Settings** → **Pages** → set source to **None** (or leave; both serve)
2. CNAME file in repo root: leave as-is (CF Pages ignores; GH Pages stops serving)

## Rollback (if anything breaks)

CF DNS still managed by us. To rollback:
1. Delete the CF Pages custom domain binding (returns A records to whatever was there)
2. Re-add the four GitHub Pages A records:
   ```
   callmeie.ie A → 185.199.108.153 (proxied:false)
   callmeie.ie A → 185.199.109.153 (proxied:false)
   callmeie.ie A → 185.199.110.153 (proxied:false)
   callmeie.ie A → 185.199.111.153 (proxied:false)
   ```
3. GitHub Pages resumes within DNS TTL (5 min)

Total rollback time: < 10 min.

---

## What this DOES NOT do

- Does NOT add JavaScript to any page
- Does NOT set cookies
- Does NOT use localStorage / sessionStorage
- Does NOT require a consent banner
- Does NOT identify individual visitors
- Does NOT replace `audit-no-cookies.py` — that script still runs in CI/local and still must exit 0

## What we GAIN

- Page-view counts per URL (last 30 days, 6 months, 12 months)
- Top referrers (without identifying users)
- Device class breakdown (mobile/tablet/desktop)
- Country breakdown
- 100% sampling on free tier up to 100K requests/day
- Edge cache stats (CF Pages free tier)

Aggregate-only, no per-visitor data, GDPR-clean by design.

---

## Connection to other infra

- DNS records `api.callmeie.ie` and `status.callmeie.ie` (added today, both pointing to Hetzner `178.104.205.255`) are unaffected — those stay as A records, proxied:false, on the same CF zone
- CF Pages uses a separate egress/SSL pipeline from Hetzner Coolify — nothing changes for `https://api.callmeie.ie` (FastAPI on Coolify) or `https://portal.callmeie.ie`
- Stripe webhook `we_1TVCAzCEqG2AuI1zI2qB6OM5` continues to hit `https://api.callmeie.ie/owl/stripe/webhook` regardless of the static-site host change
