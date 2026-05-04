# PDR — Callmeie Multi-Product Legal Pages

**Date:** 2026-05-04
**Author:** Claude (collaborator-mode draft for Adam approval)
**Status:** DRAFT — awaiting Adam decisions D-LEGAL-01..09 before code

---

## Why this PDR

Current state:
- `receptionist/privacy.html` (680 lines) + `receptionist/terms.html` (631 lines) only cover the AI Receptionist product (Vapi + Twilio + Google Calendar + SMS)
- 3 products live now: AI Receptionist · Document Ops · AI-First Websites — only 1 covered
- Brand-string drift: "CallMeIE" + "callme.ie" + "Callmeie" + "Callmeie Technologies" all present
- Service-account email `callmeie-receptionist@callme-ie.iam.gserviceaccount.com` uses `callme-ie` (Google quirk — not the brand) but customers may parse as canonical
- Visual palette: receptionist legal pages use Archivo Black + Fraunces + burgundy accent; hub /docs/ uses Inter + Fraunces + navy. Pick one for legal.

Per Product Design Preflight: PDR before code. Build ONE prototype, review, batch.

---

## Architecture decisions to make (D-LEGAL-01..05)

### D-LEGAL-01 · Page architecture

**A. Consolidated** — ONE `/legal/privacy.html` + ONE `/legal/terms.html` cover all 3 products. Per-product addenda inline (sections § Privacy by product). Single source of truth.

**B. Per-product** — Keep `receptionist/privacy.html` + add `docs/privacy.html` + `websites/privacy.html`. Each can deep-link to product-specific data flows.

**C. Hybrid** — Consolidated `/legal/privacy.html` master + product sub-pages that are abstract-and-link-up (`/docs/privacy.html` says "see /legal/privacy.html § Document Ops").

**Recommendation: A (consolidated).** Cleaner for a small team, easier to maintain when sub-processors change, single GDPR Article 13/14 disclosure point. Per-product data-flow tables embedded inside.

### D-LEGAL-02 · Brand-string canon

| String | When to use |
|---|---|
| **Callmeie Technologies** | Formal entity name (footer, copyright, header on legal docs, contracts) |
| **Callmeie** | Short brand (in-prose, navigation, button labels, casual mentions) |
| **callmeie.ie** | Domain only (URL contexts, email addresses) |
| **callme-ie** | RESERVED for Google service-account technical identifier ONLY (`callmeie-receptionist@callme-ie.iam.gserviceaccount.com`) — explained as a Google project-id quirk in legal text. Never used as brand prose. |

Kill: `CallMeIE`, `Call Me IE`, `Call.Me`, `callme.ie` (in any prose context).

### D-LEGAL-03 · Visual palette for legal

**A. Hub-aligned** (Inter + Fraunces + navy + cream) — matches `callmeie.ie/` parent and `/docs/` hub. Reads as "Callmeie Technologies parent" neutral.

**B. Receptionist-aligned** (Archivo Black + Fraunces + burgundy + paper cream) — matches existing `receptionist/privacy.html` aesthetic. Heavy editorial. Looks like a legal document.

**C. New legal-only palette** — Bespoke "Legal" visual identity (formal serif + thin rules, like a print solicitor letter). Highest signal but extra design work.

**Recommendation: A (hub-aligned).** Consolidates brand system. Avoids implying legal is owned by Receptionist.

### D-LEGAL-04 · Data-flow disclosure depth

**A. Surface-level** — "We process: contact details, call recordings, documents, analytics. Lawful basis: contract." (~5 lines per product)

**B. Article-13/14 full** — Per-product table: data category × purpose × lawful basis × retention × sub-processor × transfer (if any) × your rights × DPO contact. (~30 lines per product, GDPR best-practice)

**Recommendation: B (full Article-13/14).** SMB customers WILL ask before paying €500. The DPA already commits to this depth — privacy page should match.

### D-LEGAL-05 · DPA cross-reference architecture

DPA already exists at `docs/dpa.html` (Document Ops only, customer-facing summary).

**A. Single DPA covering all 3 products** — Refactor `docs/dpa.html` to `legal/dpa.html`, add Receptionist + Websites sections.

**B. Per-product DPA** — Keep `docs/dpa.html` + add `receptionist/dpa.html` + `websites/dpa.html`. Each links from its product's privacy page.

**C. DPA only required for Document Ops** — Receptionist + Websites sub at the MSA level (no separate DPA), Doc Ops gets its own DPA because the data-processing volume warrants it.

**Recommendation: A (consolidated DPA).** GDPR Article 28 contract obligations apply to all 3 products that process customer personal data. One DPA = one signature = one negotiation. Doc Ops gets a richer Schedule (sub-processor list specific to its pipeline) within the same DPA.

---

## Per-product data flow (input to PDR)

### Receptionist

| Data category | Source | Purpose | Retention | Sub-processors |
|---|---|---|---|---|
| Caller phone number | Inbound call (Twilio) | Lead capture · routing · SMS reply | 12 months from last call | Twilio · Vapi · Render |
| Call recording + transcript | Inbound call (Vapi) | Quality assurance · client review | 90 days then auto-delete | Vapi |
| Caller name + intent | Spoken in call | Lead routing · captureLead webhook | 12 months | Vapi · Render |
| Calendar event (for booking) | Vapi → Google Calendar API | Appointment booking on behalf of client | Per client's calendar retention (Google) | Google Workspace · Vapi |
| SMS to caller | Vapi → Twilio | Confirm booking · follow-up | 12 months | Twilio |
| Anomaly diagnosis (Claude API) | Webhook | Detect failed calls + recommend action | 90 days | Anthropic |

### Document Ops

| Data category | Source | Purpose | Retention | Sub-processors |
|---|---|---|---|---|
| Original-form document (PDF/JPG) | Upload | OCR + extraction | Per Order Form retention window (default 7 years VATCA s.84(3)) | Hetzner (storage) · self-hosted Label Studio (review) |
| Extracted fields (vendor/total/VAT/date) | Pipeline | Customer's accounting input | Per Order Form | Hetzner (Postgres) |
| Reviewer corrections (Label Studio) | Human review | Improve extraction quality | Per Order Form | Self-hosted (no third-party) |
| Tenant config + auth identifiers | Magic-link auth | Account access | Account lifetime | Hetzner |
| Stripe customer ID | Subscription | Billing | Billing lifetime | Stripe |

### AI-First Websites

| Data category | Source | Purpose | Retention | Sub-processors |
|---|---|---|---|---|
| Site visitor IP (anonymised) | Umami self-hosted | Privacy-friendly analytics | 12 months aggregated; no per-visitor profile | Self-hosted on Hetzner |
| Form submission (contact / lead) | Site forms | Forward to client owner | 90 days then auto-delete | Hetzner (Postgres) · Resend (email forward) |
| Cloudflare DNS + CDN | All requests | Routing · DDoS protection | Per Cloudflare retention | Cloudflare |
| Hosted assets (images, JS, CSS) | Build pipeline | Site delivery | Per asset lifetime | Hetzner · Cloudflare CDN |
| Stripe checkout iframe (if commerce wired) | Site embed | Payment | Per Stripe retention | Stripe |

---

## Sub-processor master list

| Sub-processor | Used by | Location | Function |
|---|---|---|---|
| Hetzner Online GmbH | Doc Ops · Websites · Receptionist DB-mirror | Nuremberg, DE | Hosting · object storage |
| Vapi.ai | Receptionist | US (with EU routing where available) | Voice agent runtime · call recording |
| Twilio Inc. | Receptionist | US/IE (number-dependent) | Telephony · SMS |
| Google LLC (Workspace) | Receptionist | EU residency where set | Calendar API |
| Anthropic PBC | Receptionist (anomaly diagnosis) | US | LLM API for failed-call diagnosis |
| Stripe Payments Europe Ltd | All 3 (billing) | Dublin, IE | Payment processing |
| Cloudflare Inc. | All 3 (DNS/CDN) | Global with EU routing | DNS · CDN · DDoS |
| HumanSignal Inc. (Label Studio) | Doc Ops | Self-hosted on Hetzner DE | Reviewer tool — no data egress |
| Resend (Resend.com Inc.) | Websites · Receptionist (transactional email) | EU | Transactional email |
| Render Inc. | Receptionist server | Frankfurt, DE | FastAPI hosting |

---

## Build order (after Adam approves D-LEGAL-01..05)

| Step | Action | Adam-keyboard |
|---|---|---|
| 1 | Decisions D-LEGAL-01..05 ratified | YES (this doc) |
| 2 | Build `/legal/privacy.html` ONE prototype: hub-aligned palette, consolidated 3-product Article-13/14 tables, sub-processor master list, brand canon applied. ~400-500 lines. | NO (Claude builds) |
| 3 | Adam eyeballs prototype via localhost | YES (visual review) |
| 4 | Apply same pattern to `/legal/terms.html` (consolidated MSA-style ToS for all 3 products) | NO (Claude builds) |
| 5 | Refactor `docs/dpa.html` → `legal/dpa.html` with Receptionist + Websites sections added (per D-LEGAL-05A) | NO (Claude builds) |
| 6 | Update `_partials/cohesion-footer.html` Legal column to point to `/legal/*` not `/receptionist/*` | NO (Claude builds) |
| 7 | Re-run `inject-cohesion.py` to propagate footer to all 16 hub pages | NO (Claude builds) |
| 8 | Add redirects: `receptionist/privacy.html` + `receptionist/terms.html` → `/legal/*` | NO (Claude builds) |
| 9 | Adam approves final via localhost preview | YES |
| 10 | Push hub repo (Coolify auto-deploys) | NO |

Estimated cost: 3-5 chat-exchanges if D-LEGAL-01..05 are accepted as recommended. Each prototype iteration = 1 exchange.

---

## Risks (3 to flag)

**R1. AI-substitute legal review only.** Like the DPA v0.3, this PDR + the resulting pages are written without a licensed Irish solicitor's review. Acceptable risk for the pre-revenue stage; MUST be reviewed before first paying customer signs an Order Form. Disclosure included in page footer per existing DPA convention.

**R2. Visual-palette consolidation breaks receptionist-page brand cohesion.** Existing `receptionist/privacy.html` has its own Archivo Black + burgundy aesthetic that some prospects may have already seen. Mitigation: receptionist-product LANDING pages stay with their existing palette; only `/legal/*` pages adopt the hub-aligned palette. Legal is a different surface, expected to look different.

**R3. Sub-processor list may be incomplete or stale.** Master list above is built from current INFRA.md + receptionist/CLAUDE.md. Any sub-processor change (e.g. switching from Resend to Postmark) requires updating this single list and re-deploying. Add a "version + last-updated" stamp at top of each legal page.

---

## Decisions table (Adam approves/overrides)

| ID | Decision | Recommendation | Adam |
|---|---|---|---|
| D-LEGAL-01 | Page architecture | A (consolidated) | _____ |
| D-LEGAL-02 | Brand-string canon | Callmeie Technologies / Callmeie / callmeie.ie | _____ |
| D-LEGAL-03 | Visual palette | A (hub-aligned) | _____ |
| D-LEGAL-04 | Data-flow disclosure depth | B (full Article-13/14) | _____ |
| D-LEGAL-05 | DPA cross-reference architecture | A (consolidated DPA) | _____ |
