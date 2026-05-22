---
id: pilot-outreach-playbook
title: CallMeIE Pilot Outreach Playbook
role: internal-operating-doc
temporal_class: data
status: prototype
owner: claude-main
last_verified: 2026-05-22
verified_by: composed in-session after PILOT-PROGRAM.md + Stripe pilot endpoint shipped Stage A; routes prospects to the live /admin/api/pilot/signup endpoint and the now-purchased Twilio pool DID +35361788870
refresh_cadence: revise after first 3 pilots — capture response-rate per channel + template, kill templates with <5% reply-rate, double down on what works
gate_class: internal — companion to PILOT-PROGRAM.md (which is the canonical pilot spec); this file is the outreach execution playbook
---

# CallMeIE Pilot Outreach Playbook

## Purpose

How to go from "we have a pilot program" → "3 qualified Irish SMB prospects on day-1 of their 30-day pilot." Companion to `PILOT-PROGRAM.md` (the spec); this is the execution doc.

First 3 verticals: **dental, solicitor, accounting** (per Adam decision 2026-05-22). Limerick + Munster first, broader Ireland after first conversion.

## 1. Lead-source decision

| Source | Pros | Cons | Best for |
|---|---|---|---|
| **LEO Limerick mentor intros** | Pre-trusted; highest close rate; reciprocal goodwill with LEO ecosystem | Limited supply; not on-demand; risks burning mentor relationships if pilots flop | First 1-2 pilots — start strongest |
| **`lead_research.py` deterministic scraper** | Free; scalable; produces ranked summary `_summary.md` HIGH→LOW per night; reuses proven `_blast_industry.py` formula | Cold outreach; lower reply rate (~3-8% typical); requires queue.txt seeding | Sustained pipeline once first 1-2 land |
| **Limerick in-person door-walk** | Highest conversion (face + physical premises trust); local presence reinforced; collect IRL signal on practice size | Slow throughput (5-8 visits/day); Adam time-cost; geographic-limited | Months 2-3 once template proven |

**Recommended sequence:**
1. Week 1: LEO intros → 1 pilot (test the offer with warmest possible prospect)
2. Week 2: `lead_research.py` cold email → 2 pilots (test the email template at low volume)
3. Week 3+: door-walk + cold email scale, based on which converted best

Track every prospect in `pilots` DB table (status=pending until they hit the Stripe Checkout link).

### Existing `leads/` pipeline — DO NOT confuse with receptionist outreach

There is already a `New repos/leads/` cold-pitch pipeline (see `leads/CLAUDE.md`). It is built for the **Websites product** — scrape Golden Pages → build a bespoke site at `{slug}.websites.owlzone.trade` → email "I built you a website" via `email_sender.py`. It has its own `leads.db` SQLite store, scoring, scraper, scheduler.

**Not reused for receptionist pilot today** because: (a) wrong email template (sells a website, not a phone line), (b) `EMAIL_FROM`/`SMTP_*` env vars still unset per `leads/CLAUDE.md` "Known issues", (c) the websites funnel publishes a live site as proof-of-work — pilot funnel does not.

**Stage C consolidation candidate** (Adam decision when receptionist outreach scales >20/week): add a `pitch_track` column to `leads.db` distinguishing `websites` vs `receptionist_pilot` prospects, port `email_sender.py` with the D-01/S-01/A-01 templates from §3 below, share the scoring + scraping + status-tracking infrastructure. Single source of truth for prospect data. Until then: outreach is manual via the `hello@callmeie.ie` Gmail and tracked in the `pilots` DB table per §6.

## 2. Qualification rubric — when is a prospect a pilot fit?

Apply BEFORE sending outreach. Pre-qualifies the pipeline so we don't burn pilot pool capacity (max 5 concurrent per PILOT-PROGRAM.md).

| Signal | Score | Source |
|---|---|---|
| Irish-based (.ie or IE address) | +2 | Website / Google Business |
| Phone-led business (no online booking) | +3 | `lead_research.py` HIGH rating |
| Visible call volume (multiple lines / "call us" CTAs) | +2 | Homepage scan |
| Solo operator or 2-5 staff | +2 | About page / LinkedIn |
| After-hours / weekend hours mentioned | +1 | Hours page |
| Existing answering service or VoIP system | -2 | If found, harder to displace |
| Already lists "AI receptionist" / "virtual assistant" | -3 | Already considered + chose other vendor |
| Vertical-fit (dental/solicitor/accounting) | +2 | Schema.org or about copy |
| Limerick / Munster locality (founder reach) | +1 | Address |

**Pursue threshold: total ≥ 6.** Below that, skip — too much churn risk on a 5-pilot cap.

Concrete examples:
- Dental practice, Limerick, 3 dentists, no online booking, "call us to book" → `+2+3+2+2+2+1 = 12` → **strong pursue**
- Solo solicitor, Dublin, online appointment system, AI chatbot on site → `+2-2-3+2 = -1` → **skip**
- 5-partner accounting firm, Cork, phone-led, no AI mentions → `+2+3+2+2+2 = 11` → **strong pursue**

## 3. Cold email templates

### Rules for all templates
- **Subject ≤ 50 chars**, no clickbait, business-specific not generic
- **Body ≤ 120 words** — anything longer gets archived unread per cold-email best practice
- **One ask**, one link, one P.S. with the demo number
- From `hello@callmeie.ie` (canonical per MEMORY.md)
- **Never** claim "callers can't tell it's AI" (humans clock it ~90% per MEMORY rule)
- **Never** claim existing accounting/solicitor/dental customers (pre-revenue)
- Always say "pilot" not "free trial" (Adam's frame)
- Sign as **Adam Vaughan, Founder, CallMeIE** (not a fake sales persona)
- Pricing reference: **from €149/mo** never flat (PRICING-SSOT rule)

### Template D-01 — Dental practice

```
Subject: 30-day pilot — [PRACTICE_NAME] missed-call cover

Hi [FIRST_NAME],

Saw [PRACTICE_NAME] on [WHERE_FOUND — e.g. "the Limerick dentists list"]. Quick question: how many appointment calls do you reckon go to voicemail after 6pm or during a busy clinic?

We built an Irish AI phone receptionist that answers every call, books straight into your existing Google or Outlook calendar, and SMSes you anything urgent. From €149/mo after a 30-day free pilot — no card charged until day 31, no setup fee during the pilot.

Worth a 10-min call to see if it's a fit? If yes, ring our demo line +353 61 788 120 (talk to our test assistant, it's the same product) — or reply and I'll send a calendar link.

— Adam Vaughan
   Founder, CallMeIE
   hello@callmeie.ie

P.S. We're piloting with 3 dental practices this month and prioritising Limerick/Munster.
```

### Template S-01 — Solicitor / legal practice

```
Subject: 30-day pilot — [FIRM_NAME] first-contact intake

Hi [FIRST_NAME],

How much partner time does [FIRM_NAME] lose to first-contact calls that don't qualify? Conflict-check questions, "what's your hourly rate", "do you handle [matter type]" — calls that need a receptionist, not a solicitor.

We built an Irish AI receptionist designed for legal practices: never gives legal advice, never asks for PPS/PRSI/bank data, runs a conflict-name prompt on first contact, routes by matter type, takes a structured intake message for the right partner. From €149/mo after a 30-day free pilot — card on file at signup, no charge until day 31.

Worth a 15-min call? Or ring our demo line +353 61 788 120 — same product, test assistant.

— Adam Vaughan
   Founder, CallMeIE
   hello@callmeie.ie

P.S. Three solicitor pilots this month, Limerick/Munster priority.
```

### Template A-01 — Accounting practice

```
Subject: 30-day pilot — [FIRM_NAME] tax-season calls

Hi [FIRST_NAME],

Deadline week question: how many calls does [FIRM_NAME] route between partners before the right person picks up? VAT3 panic, ROS password resets, "is my CT1 due Friday" — the kind of call that interrupts the audit POD for the tax POD.

We built an Irish AI receptionist designed for accountancy practices: never gives tax/audit/payroll advice (regulatory + PI), routes by partner OR by query type (tax / audit / payroll / advisory), takes structured messages for callbacks, covers after-hours through deadline week. From €149/mo after a 30-day free pilot — card on file at signup, no charge until day 31.

Worth a 15-min call? Or ring +353 61 788 120 — demo line, test assistant, same product.

— Adam Vaughan
   Founder, CallMeIE
   hello@callmeie.ie

P.S. Three accounting pilots this month — Limerick/Munster first.
```

### Follow-up 1 (day +4 if no reply)

```
Subject: Re: 30-day pilot — [FIRM/PRACTICE_NAME]

Hi [FIRST_NAME] — Adam from CallMeIE. Bumping the note in case it got buried.

Short version: 30 days free, your own +353 number, your calendar, your hours. Day 28 I send you a usage report and recommend the tier (Starter / Pro / Growth) based on what you actually used. Day 31 it activates on the card you put on file — or cancel by reply, no charge.

10-min call to see if it fits?

— Adam
```

### Follow-up 2 (day +10 if still no reply)

```
Subject: Last note — [PRACTICE_NAME] pilot

Hi [FIRST_NAME] — I won't keep bumping. Quick yes / no / not-now would close the loop. Pilot details: callmeie.ie/receptionist/[VERTICAL].html.

— Adam
```

After follow-up 2 → mark prospect `not_now` in tracker, revisit in 90 days.

## 4. 15-min onboarding call script

Run AFTER prospect replies positive. Goal: lock signup + confirm operational details before provisioning.

```
1. (1 min) Adam intro + thank for time. Confirm 15 min slot.

2. (3 min) Ask THEM first:
   - "Walk me through what happens when a caller rings now."
   - "Roughly how many calls a day? Peak times?"
   - "What kinds of calls do you wish you didn't have to take personally?"
   - LISTEN — their words go straight into the assistant prompt.

3. (3 min) Confirm the offer:
   - 30 days free, own +353 Limerick number
   - Card on file at signup (Stripe, GDPR-safe)
   - Day 28: usage report + tier recommendation
   - Day 31: auto-converts to recommended tier OR cancel anytime by reply
   - Setup fee waived (vs €297/€497 standard)
   - "It's your call answering — you're not locked in"

4. (4 min) Operational collect (write into NOTES field of /admin/api/pilot/signup):
   - Business hours (open / close days)
   - Existing booking calendar (Google / Outlook / pen and paper)
   - Partner / staff names + roles (for routing)
   - 1-2 frequent caller queries we should handle vs route
   - Hard-no's: anything they explicitly don't want the AI saying

5. (2 min) Logistics:
   - Confirm contact email (Stripe link goes here)
   - Confirm card-on-file is acceptable (most say yes; minority pushback → offer "I can set you up without the card and we'll talk again day 28" — half the friction-removal but the tire-kicker filter is gone)
   - Set day-1 expectation: number live within 24h, will text them when ready

6. (1 min) Close:
   - Send Stripe link by end of day
   - Schedule day-7 check-in call (15 min)
   - Their question slot — any open?

7. (1 min buffer)
```

Outcome states:
- **YES + card** → run provisioning checklist §5
- **YES + no card** → run §5 but skip card; set Stripe Checkout to invoice-mode (not built yet — Stage A only supports card-required; defer no-card flow to Stage C)
- **NOT NOW** → record reason in tracker; calendar follow-up 90 days
- **NO** → record reason; do not re-contact

## 5. Per-prospect provisioning checklist

Run AFTER successful onboarding call. ~15 min Claude work per pilot.

```bash
# Set per-prospect vars
PROSPECT_BUSINESS="O'Brien Dental Clinic"
PROSPECT_EMAIL="info@obriendental.ie"
PROSPECT_PHONE="+35361234567"
PROSPECT_VERTICAL="dental"   # one of: dental, solicitor, accounting, salon, cafe, ...
PROSPECT_HOURS="Mon-Fri 09:00-17:30, Sat 09:00-13:00"
PROSPECT_NOTES="3 dentists: Mary O'Brien (principal), Tom Murphy (associate), Aoife Daly (hygienist). New-patient enquiries route to Mary. Treatment-callback routes to whoever the patient saw last."

# 1. Buy a dedicated +353 number for this pilot
cd C:/Users/a33_s/Desktop/callmeie-fix
python scripts/buy-pilot-did.py --search-only      # confirm inventory
python scripts/buy-pilot-did.py --buy              # buys +35361 first match
# → record returned PN_SID + phone number

# 2. Clone the vertical Vapi assistant template, customise prompt with prospect notes
#    (manual via Vapi console for now — automate as a /admin/api/pilot/provision endpoint
#    in Stage B once the manual flow is proven on first 3 pilots)
#    Template assistant IDs (callmeie-hub/receptionist/CLAUDE.md §Key IDs):
#      Dental: 0b37deb5-2fc2-4e7b-81b1-e61e97103506
#      Solicitor: 7774b535-95fe-4e75-b571-dde098e2f8fb
#      Accounting: (use solicitor as base, swap prompt — see PROSPECT_NOTES → prompt mapping below)
#
#    Bind the new Vapi assistant to the bought Twilio DID via Vapi console
#    (Phone Numbers → import Twilio → assign to assistant).

# 3. Issue a per-tenant client_token (NEVER ADMIN_TOKEN — per
#    feedback_client-token-not-admin-token.md privilege-escalation lesson)
cd C:/Users/a33_s/Desktop/callmeie-fix
python scripts/issue-client-token.py --slug "$(echo $PROSPECT_BUSINESS | tr ' ' '-' | tr '[:upper:]' '[:lower:]')" --assistant-id "<vapi_assistant_id_from_step_2>"
# → record returned ct_<slug>_<24_random> token

# 4. Create the Stripe Checkout link via the pilot endpoint
curl -X POST https://api.callmeie.ie/admin/api/pilot/signup \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"business_name\": \"$PROSPECT_BUSINESS\",
    \"contact_email\": \"$PROSPECT_EMAIL\",
    \"contact_phone\": \"$PROSPECT_PHONE\",
    \"vertical\": \"$PROSPECT_VERTICAL\",
    \"notes\": \"$PROSPECT_NOTES\"
  }"
# → returns {pilot_id, checkout_url, day_28_due, day_31_due}

# 5. UPDATE pilots row with the Twilio + Vapi IDs (manual SQL until Stage B endpoint)
#    sqlite3 /tmp/callmeie.db
#      UPDATE pilots SET vapi_assistant_id='<id>', twilio_phone_sid='<PN_SID>', twilio_phone_number='+35361xxxxxx' WHERE id=<pilot_id>;

# 6. Send the checkout_url to prospect (email + SMS for redundancy)
#    Subject: "CallMeIE pilot — your link"
#    Body: "Hi [name], here's your card-on-file link to start your 30-day pilot:
#           [checkout_url]
#           Your dedicated number goes live within 24 hours of card capture. — Adam"

# 7. After prospect completes Stripe Checkout (you'll see it via webhook
#    customer.subscription.created with trial_end set), confirm the
#    Vapi assistant is responding by ringing the new +353 number yourself.

# 8. Day 1: SMS prospect "Your CallMeIE line +35361XXXXXX is live. Try ringing it."
# 9. Day 7: scheduled 15-min check-in call. Tweak prompt/hours/routing as needed.
# 10. Day 28: PILOT-PROGRAM.md §"Day-28 tier recommendation logic" — manually for now;
#     Stage B cron handles this once built (NEXT-STEPS step 7).
# 11. Day 31: Stripe webhook `customer.subscription.updated` (trial_end transition).
#     Manually PATCH subscription items to swap price if recommended_tier != starter.
#     Stage B webhook handles this once built.
```

## 6. Tracking

Single source of truth = `pilots` DB table in `/tmp/callmeie.db`. Read via `GET /admin/api/pilots`.

Per-pilot lifecycle states (`status` column):
| state | meaning |
|---|---|
| `pending` | Signup endpoint called, checkout_url created, prospect has NOT yet clicked |
| `card_captured` | Prospect completed Stripe Checkout, trial running |
| `provisioned` | Vapi assistant live, Twilio DID bound, day-1 confirmation SMS sent |
| `day_28_recommended` | Usage report sent, tier recommended |
| `converted` | Day 31 → tier active, billing started, customer (not pilot) |
| `cancelled` | Prospect replied "cancel" OR Stripe missing-payment auto-cancel fired |
| `not_now` | Prospect declined onboarding call OR no reply after 2 follow-ups |

Outreach attempts (one row per cold-email send) — separate `outreach_attempts` table NOT yet built; manual `_internal/OUTREACH-LOG.md` markdown ledger until volume warrants the schema (build threshold: >20 attempts/week).

## 7. Anti-patterns — rejected approaches

| Rejected | Why |
|---|---|
| Mass cold-email blast (>50/day) | Reputation risk on `hello@callmeie.ie` SPF/DKIM; deliverability tanks; conversion floor stays low. Quality > volume at this stage. |
| Sales-y subject lines ("REVOLUTIONIZE your phone system") | Adam's anti-AI-tells rule + IE-SME tone; "30-day pilot — [name]" beats every hype variant in B2B IE cold email benchmarks. |
| Hiding the price | "From €149/mo" upfront filters tire-kickers and qualifies budget; hidden price = "you can't afford it" perception. |
| Demo-call before email | Wastes Adam's 15 min on uncommitted prospects. Email-then-call funnel filters to interested-only. |
| Using the same +353 61 788 120 demo line for all pilots | Cross-pollutes data; need per-tenant DID for per-pilot usage metering accuracy. |
| Provisioning Vapi assistant BEFORE Stripe card capture | If prospect ghosts after onboarding call, we've burnt setup time. Card-capture-first = commitment proof. |
| Reusing ADMIN_TOKEN for prospect access | NEVER — privilege escalation, per `feedback_client-token-not-admin-token.md`. Always issue per-tenant `client_token` via `scripts/issue-client-token.py`. |
| Counting card-captured prospects as customers | They are still pilots until day-31 conversion. LEO/bank/grant integrity rule. |
| Auto-following-up indefinitely | 2 follow-ups MAX → `not_now`. Annoying repeat outreach burns brand. |

## 8. Success metrics (track weekly)

| Metric | Target by month 1 | Target by month 3 |
|---|---|---|
| Outreach attempts | 30 | 80 |
| Reply rate | ≥10% | ≥15% |
| Onboarding call rate | ≥50% of replies | ≥60% |
| Pilot signup rate (Stripe link clicked + card captured) | ≥40% of calls | ≥50% |
| Pilot conversion rate (day 31 → paying) | ≥40% of signups | ≥60% |
| Average tier on conversion | Starter | Professional (signals upmarket fit) |
| Cancellation reason captured | 100% | 100% (this is the gold) |

Below target on any metric for 2 consecutive weeks → revise the relevant section (template / call script / qualification rubric) and log the change here.

## 9. Composing rules

- This playbook routes prospects to the **live `/admin/api/pilot/signup` endpoint** in `callmeie-fix/scripts/server.py` (Stage A shipped 2026-05-22).
- It depends on the **`+35361788870` Twilio pool DID** and the **Limerick address SID `ADa6af451f3c25f1e5ff44f5b587c62fe7`** being valid — both confirmed 2026-05-22.
- It assumes Vapi vertical assistant templates in `callmeie-hub/receptionist/CLAUDE.md §Key IDs` are stable.
- It depends on **`STRIPE_RECEPTIONIST_STARTER_MONTHLY` env var** being set on Render (NEXT-STEPS step 1).
- If any of those drift, this playbook drifts. Re-verify before each fresh outreach campaign.

## Change log

- 2026-05-22 — initial draft after PILOT-PROGRAM.md + Stage A endpoint shipped same day.
