# Order Form — CallMeIE Technologies (TEMPLATE v1.0 DRAFT)

**Status:** DRAFT — solicitor review required before first paying customer signs.
**Date drafted:** 2026-05-07.
**Pairs with:** `legal/terms.html` (Master Service Agreement), `legal/dpa.html` (Article 28 DPA), `_internal/ropa-2026.md` (Article 30 ROPA), `websites/care-plans-scope.md` (Care plan inclusions).
**Single source of truth:** ONE template covers all 3 build tiers + all 3 Care tiers + Doc Ops + AI Receptionist via the per-section checkboxes. Reduces drift across templates (round 3 PDR D-LIFE-17).

---

## Section A — Parties

**Service Provider (CallMeIE Technologies):**
Adam Vaughan trading as CallMeIE Technologies
Limerick, Ireland · IE VAT-registered (VAT no. _________________)
Primary contact: adam@callmeie.ie · +353 85 786 3564
Limited-company incorporation in progress; on incorporation, this Order Form
auto-novates to the new Ltd entity per `legal/dpa.html` §8 (no re-papering
required from the Customer).

**Customer:**
Business name: _____________________________
Trading-as / brand: __________________________
Registered address: _________________________________________
Primary contact name: _________________ Role: ______________
Primary contact email: ____________________ Phone: ____________
VAT number (if EU B2B reverse-charge applies): ________________

---

## Section B — Engagement type

Tick exactly one bundle (combinations OK across products if Customer signs once
for both):

### B1. AI-First Websites — Build (one-off)

  [ ] **Quick Page** — €395 + VAT · 3 working days · 1 section, 1 round of revisions, no copy/logo/photography included
  [ ] **Starter** — €695 + VAT · 7 working days · 1 page, 1 round of revisions
  [ ] **Pro** — €1,595 + VAT · 14 working days · 5 pages, 2 rounds of revisions, Decap CMS
  [ ] **Custom** — from €2,950 + VAT · scoped on call · negotiated rounds + tools (Payload CMS / e-commerce / multilingual)

**Payment milestones (Build):**
  - Quick Page / Starter: **100% on signature** (low admin overhead at this band)
  - Pro: **50% on signature, 50% on launch**
  - Custom: **40% on signature, 30% on design-approval milestone, 30% on launch**

**Revision cap:** as stated above. Beyond cap → €60/hour (€55/hour if Customer
also has a Care plan).

**Acceptance:** site is accepted upon either (a) the Customer's written
"approved" reply to the launch-handoff email, OR (b) the lapse of 14 calendar
days following the launch-handoff email without written objection.

### B2. AI-First Websites — Care plan (monthly subscription)

  [ ] **Essential** — €45/mo or €450/yr — 30 min/mo edits · 2 biz-day SLA · €60/hr overage
  [ ] **Growth** — €95/mo or €950/yr — 2 hr/mo edits + 1 new page/quarter · 1 biz-day SLA · €60/hr overage
  [ ] **Concierge** — €195/mo or €1,950/yr — unlimited fair-use (6hr/mo rolling 90-day avg, 8hr/mo single-month ceiling) · same-day SLA · €55/hr overage

Detailed inclusions + scope at: https://callmeie.ie/websites/care-plans-scope

**Billing:** monthly via Stripe on the same day each month, OR annual prepay
(2 months free) on signature day. Cancel any time with 30 days' written notice
to support@callmeie.ie. No auto-renew traps.

### B3. Document Ops — Pilot (one-off)

  [ ] **Entry Pilot** — €500 + VAT · 25 documents · 14 working days
  [ ] **Standard Pilot** — €1,500 + VAT · 100 documents · schema mapping to your accounting tool

### B4. Document Ops — Subscription (monthly)

  [ ] **Auto** — €99/mo · 200 docs/mo cap · self-serve queue · spot-check before paste
  [ ] **Auto Plus** — €249/mo · 600 docs/mo cap · 2 tenant seats included · €40/mo per extra seat
  [ ] **Rescue + Export** — €499/mo · 250 docs/mo · 10 human rescues with 3-biz-day SLA · overflow bounces normally
  [ ] **Bespoke** — from €1,500/mo · scoped on call · custom CSV schema, multi-leg consignment linking, monthly reviewer summary

### B5. AI Receptionist — Subscription (monthly)

  [ ] **Starter** — €149/mo + €297 setup · 300 min/mo · business-hours cover · 1 calendar
  [ ] **Professional** — €249/mo + €297 setup · 600 min/mo · 24/7 + missed-call text-back · 1 calendar
  [ ] **Growth** — €397/mo + €497 setup · 1,200 min/mo · multi-calendar · monthly optimisation call · 3-month minimum

---

## Section C — Deliverables

**For Build engagements**, the Customer will receive on completion:
1. The live site at the agreed URL (Customer's domain or `{slug}.callmeie.ie`)
2. Full source code in a GitHub repository, ownership transferred to Customer (collaborator + can be promoted to repo owner)
3. CMS admin credentials (Decap GitHub OAuth for Pro; Payload account for Custom; n/a for Quick Page / Starter)
4. The "Stack Sheet" — single-page PDF listing every service, account holder, registered email, renewal date, monthly cost
5. One Loom training video (5–8 minutes) covering Customer-self-edit workflows
6. Day-of-launch welcome email per `OPERATOR-RUNBOOK.md` handoff package
7. 30-day post-launch check-in (calendar invite already sent)

**For Document Ops engagements**, the Customer will receive:
1. A magic-link to the tenant portal at `https://portal.callmeie.ie/{slug}/`
2. A dedicated email-in inbox: `inbox-{slug}@callmeie.ie`
3. CSV exports formatted for Xero supplier-bill import (auto-paste); Sage IE Quick-Entry purchases (auto-paste, with companion crib for RCT manual posting); BrightBooks via Surf Accounts engine (auto-paste); QuickBooks UK/IE via SaasAnt bridge (Customer's SaasAnt account required)
4. Bounce-back queue with one-line reason per uncertain document
5. Stripe customer portal access for self-serve cancel / upgrade / billing

**For AI Receptionist engagements**, the Customer will receive:
1. A dedicated Twilio phone number (we never own the Customer's existing line; Customer keeps it)
2. Vapi assistant configured to Customer's voice/persona/hours/services from the Day-1 welcome call
3. Google Calendar write access via service-account share (Customer keeps OAuth control)
4. Weekly Monday email report: calls handled, bookings made, escalations
5. Stripe customer portal access for self-serve cancel / upgrade / billing

---

## Section D — Customer responsibilities

The Customer agrees to:

1. Provide brand assets (logo in vector form, brand colours, fonts owned/licensed, photography rights) within 3 business days of signature.
2. Warrant that all content supplied to CallMeIE Technologies (text, images, logos, customer-data extracts) is owned by the Customer or licensed to the Customer for the purpose. Customer indemnifies CallMeIE Technologies against third-party copyright claims arising from supplied content.
3. Maintain the accuracy of their own knowledge base (services, prices, hours, FAQs) for AI Receptionist engagements. Customer is the data controller; the AI is decision-support to the Customer's instruction.
4. Pay invoices within 14 days of issue. Late payment terms per the Late Payment in Commercial Transactions Regulations 2002 (8% above ECB rate + €40 fixed fee on overdue invoices) auto-apply.
5. Respond to revision requests within 5 business days. After 14 days of unresponsiveness ("ghosting"): project is paused; deposit retained; work-to-date delivered as-is; restart billed at €60/hr from the pause point.

---

## Section E — Service Provider responsibilities

CallMeIE Technologies agrees to:

1. Deliver each engagement to the timeline + scope above. Acceptance criteria per Section B.
2. Maintain professional indemnity + cyber liability insurance (carrier + cover details published at `legal/terms.html` §8).
3. Monitor uptime via Uptime Kuma. For Care customers: any unplanned outage >30 minutes triggers proactive incident email and a 1-day Care credit.
4. Process Customer personal data per the DPA (`legal/dpa.html`) and the ROPA (`_internal/ropa-2026.md`).
5. Deliver complete data export within 7 calendar days of any Customer cancellation, then permanently delete from our systems within 30 calendar days (per DPA Article 17 commitment + `scripts/permanent_delete.py` execution path).
6. Respond to support emails within the SLA tier above. Silence beyond SLA on a confirmed-received email entitles the Customer to a refund of one tier-month at no questions asked.

---

## Section F — IP ownership

1. **Customer-supplied content** (text, images, logos, brand) remains the Customer's property.
2. **CallMeIE-developed deliverables** (code, design, configuration, AI prompts) transfer to the Customer upon full payment of all milestone invoices for that engagement.
3. **Portfolio licence (carve-out):** CallMeIE Technologies retains a non-exclusive, royalty-free licence to display the work in our portfolio (including case studies, before/after screenshots, traffic + uptime metrics in aggregate) UNLESS the Customer opts out in writing within 14 days of the launch-handoff email.
4. **Pre-existing CallMeIE IP** (templates, internal tooling, the Doc Ops extraction pipeline itself, the AI Receptionist Vapi configuration system, scripts under `scripts/`, the Decap CMS / Payload CMS configurations as a reusable system) is licensed to the Customer for the duration of their engagement. On engagement termination, the Customer keeps the configured instance (their site, their tenant, their Vapi assistant) but does not retain a licence to redistribute the underlying tooling.

---

## Section G — Hosting transfer-of-control

1. **Day 1 through engagement:** site / tenant / assistant runs on CallMeIE Technologies infrastructure (Cloudflare Pages, Hetzner Coolify, Render, Vapi). CallMeIE-controlled accounts, Customer never sees credentials.
2. **Cancellation, week 1 (Days 1–7):** CallMeIE Technologies delivers complete export — for Websites: GitHub repo + content backup + Stack Sheet; for Doc Ops: zip of every original document + master CSV; for AI Receptionist: PDF export of last 6 months of summaries + booking history + recordings download link.
3. **Cancellation, weeks 1–4 (Days 1–30):** Customer may request migration to their own infrastructure at no fee. CallMeIE Technologies provides DB dumps, hosting-config docs, DNS-transfer instructions within 14 working days of the request.
4. **Day 30 onward:** all Customer data permanently deleted from CallMeIE Technologies systems per `scripts/permanent_delete.py`. Customer relationship terminated.
5. **Re-activation within 3 months:** CallMeIE Technologies retains the Customer's Vapi assistant in `archived` state for 90 days. Customer can re-activate within 3 months via reply to final invoice; configuration restored within 24 hours, no re-build fee.

---

## Section H — Cancellation + kill fee

1. **Subscription engagements (Care, Doc Ops sub, AI Receptionist):** cancel any time with 30 days' written notice to `support@callmeie.ie` OR via Stripe Customer Portal one-click. Final pro-rated invoice for the 30-day notice period.
2. **Build engagements, mid-build:** Customer may cancel before launch with a kill fee of **30% of remaining contracted balance** (industry-standard 25–40% band). Work-to-date delivered as-is + GitHub repo transferred. CallMeIE Technologies retains the deposit + the kill fee in lieu of remaining work.
3. **Service Provider termination (rare):** if CallMeIE Technologies must terminate (Customer breach of acceptable use, non-payment, or fraud), 30 days' notice + complete data export per Section G applies.

---

## Section I — Liability cap (refer to MSA)

Liability terms per `legal/terms.html` §8. Subscription tier liability capped at fees paid in the prior 12 months for any claim. Bespoke (Custom build, Doc Ops Bespoke) liability negotiated per engagement; cap stated below if differs from default.

**Custom liability cap (if applicable):** € __________ aggregate.

Nothing limits liability for: death or personal injury caused by negligence; fraud or fraudulent misrepresentation; any liability that cannot be excluded under Irish law.

---

## Section J — Governing law + signatures

This Order Form, the MSA (`legal/terms.html`), and the DPA (`legal/dpa.html`) together form the binding agreement. Governed by the laws of Ireland; jurisdiction of the Irish courts.

**Customer signature:**

  Name (print): _______________________
  Title: _____________________________
  Signature: _________________________ Date: __________

**CallMeIE Technologies signature:**

  Name (print): Adam Vaughan
  Title: Sole Trader (until Ltd incorporation per DPA §8)
  Signature: _________________________ Date: __________

---

## Internal notes (NOT customer-facing)

- This template lives at `_internal/order-forms/order-form-template.md`. Customer-facing PDF is generated from this on demand (export to PDF or use Documenso when D-LIFE-16 lifts and Documenso lands at customer #5).
- Solicitor review still pending as of v1.0 draft. The 10 clauses called out in `_research/2026-05-06-websites-lifecycle.md` Part 3 are all addressed in this template (see deliverable enumeration / milestone schedule / revision cap / scope-creep boundary / IP+portfolio carve-out / hosting transfer schedule / acceptance criteria / kill fee / late-payment per Irish law / customer-content warranty).
- For first paying customer (rounds 1–4): Adam fills in Section A + B as a print-PDF, emails to customer, customer replies "I agree" with a signed PDF attachment. That's legally binding under Irish e-commerce law and avoids the Documenso install at this scale.
- When Documenso lands (customer #5+): import this template as a Documenso template; the per-tier checkboxes become Documenso form fields; signature + 50% deposit collected in one click.
