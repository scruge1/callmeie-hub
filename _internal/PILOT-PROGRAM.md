---
id: pilot-program
title: CallMeIE 30-Day Pilot Program
role: internal-operating-doc
temporal_class: data
status: prototype
owner: claude-main
last_verified: 2026-05-22
verified_by: drafted in-session after Adam-authorized Twilio purchase (PN4ecfd7074b2cb1641292956e8738ca23, +35361788870, 2026-05-22 22:16 UTC) confirmed regulatory clearance
refresh_cadence: revise on first 3 pilot completions; freeze after pilot #5 with as-built corrections
gate_class: internal-program-spec (not customer-facing — see /pilot/ for the customer-facing landing page once built)
---

# CallMeIE 30-Day Pilot Program

## Purpose

Convert qualified Irish SMB prospects from cold to paying customers via a 30-day free pilot that ends in a **usage-metered tier recommendation** rather than a flat default.

Adam authorised the program 2026-05-22 after:
- Twilio regulatory clearance confirmed live (IE Local bundle `BUe3a9d5fdaa25fa8065f7dc1607b5551a` purchased number `+35361788870` PN`4ecfd7074b2cb1641292956e8738ca23` 22:16 UTC).
- PRICING-SSOT §2 receptionist tiers stable (Starter €149 / Professional €249 / Growth €397).
- Vapi usage metering already wired (Stripe Meter `mtr_61UbGf0xrOZ6vdadl41CEqG2AuI1zWoq`, event `vapi_minutes`, `usage_records` table).

Pilots are NOT paying customers until day-31 conversion. **Do not count pilots in any LEO / bank / grant / pitch context** — see MEMORY.md `feedback_callmeie-pre-revenue-no-paying-pilots`.

## Pilot economics

| Item | Cost per pilot | Notes |
|---|---|---|
| Twilio IE Local DID | ~€1 setup + €1/mo recurring | Bundle pre-approved |
| Vapi minutes during pilot | ~€0.10/min × est. 100-400 min | Worst case 400 min ≈ €40 |
| Ops/setup time | ~30 min Claude + 0 min Adam (post-build) | Stripe trial automates |
| **Total worst-case burn / pilot** | **~€42** | If pilot churns at day 31 |

3 concurrent pilots = ~€126 worst-case burn. Cap pilot pool at 5 active to bound exposure to ~€210.

## Offer

**30 days. Free. Card on file at signup.**

- Setup fee waived (vs €297 Starter/Pro or €497 Growth).
- All features available immediately — no tier-locked features during pilot.
- Customer's own +353 Limerick local number (or US fallback if inventory empty).
- AI assistant built on the matching vertical template (dental / cafe / salon / solicitor / accounting).
- Vapi assistant pre-loaded with the prospect's hours, services, partner/staff names, calendar.
- Day 28: usage report + tier recommendation emailed to prospect.
- Day 31: auto-converts to recommended tier on the card on file UNLESS prospect picks different OR cancels.

## Day-28 tier recommendation logic

Read from `callmeie-hub/receptionist/scripts/billing/db.py` `usage_records` table for the pilot's `vapi_assistant_id`. Compute:

| Signal | Source |
|---|---|
| total minutes consumed | `SUM(duration_seconds) / 60` over 28-day window |
| routing complexity | `COUNT(DISTINCT route_destination)` from `call_events` |
| after-hours percentage | `% of calls where hour NOT IN 09-17 IE time` |

Tier mapping:

| Recommendation | Trigger |
|---|---|
| **Starter €149/mo** | <300 min/mo AND single-route AND after-hours <20% |
| **Professional €249/mo** | 300-600 min/mo OR after-hours 20-60% OR 2-3 routes |
| **Growth €397/mo** | >600 min/mo OR after-hours >60% OR >3 routes OR explicit 24/7 requirement OR integration request (Calendar/CRM/Stripe) |

Edge cases:
- Pilot used <30 min in 28 days → flag as "low engagement" → email instead asks "still interested?" before any auto-convert.
- Pilot exceeded Growth tier minutes (>1200/mo extrapolated) → recommend Growth + note overage rate (€0.20/min after 1200 min/mo per PRICING-SSOT §2).

## Customer-facing email templates

### Day 0 — Welcome
Subject: Your CallMeIE pilot is live on +353 61 XXX XXXX

Hi {first_name},

Your AI receptionist is live on **+353 61 XXX XXXX** as of today. Try ringing it now — it'll answer in your business voice.

Over the next 30 days, your line will:
- Answer every call 24/7 (no rings to voicemail)
- Book qualified callers straight to your calendar
- Take structured messages for everything else
- Forward urgent items to you via SMS

**Day 28** I'll send you a usage report showing exactly how much your line handled — and recommend the tier that matches what you actually used.

**Day 31** that tier activates on the card you put on file. You can override the recommendation or cancel anytime before then, no questions.

Any tweaks needed — answering script, hours, calendar link — just reply.

— Adam, CallMeIE

### Day 14 — Mid-pilot check
Subject: 14 days in — your CallMeIE line so far

Quick midway look at your line:
- {minutes} min answered
- {bookings} appointments booked
- {leads} new-enquiry messages captured
- {after_hours_pct}% of calls were outside business hours

Anything not working how you'd like? Reply and I'll adjust before the second half kicks in.

— Adam

### Day 28 — Tier recommendation
Subject: Your pilot wraps up Friday — here's what fits

Your AI receptionist handled **{minutes} min** across **{calls} calls** over the last 28 days, with **{after_hours_pct}%** outside business hours.

Based on your actual usage, the tier that fits is:

**{recommended_tier}** — {recommended_price}/mo

({rationale})

This activates Friday {day_31_date} on the card on file. You can:
- **Stay on the recommended tier** — do nothing
- **Pick a different tier** — reply with which one
- **Cancel** — reply "cancel" and we'll wind it down. No charge.

Pricing reference:
- Starter €149/mo — 300 min, business-hours
- Professional €249/mo — 600 min, after-hours included
- Growth €397/mo — 1,200 min, 24/7 + integrations (3-month minimum)

— Adam

### Day 31 — Conversion confirmation OR cancel
Sent automatically based on prospect action / inaction.

## Acceptance criteria — pilot offer is "done" when

- [ ] `/pilot/signup` endpoint live on api.callmeie.ie (Stripe Checkout subscription, `trial_period_days=30`, `payment_method_collection=always`)
- [ ] Day-28 usage-report cron in `server.py` queries `usage_records` + emails recommendation
- [ ] Day-31 auto-convert webhook handles Stripe `customer.subscription.trial_will_end` → upgrades to recommended tier price ID OR cancels if customer replied "cancel"
- [ ] `accounting.html` vertical page live (in parallel build)
- [ ] First pilot prospect rings their new +353 number and gets answered correctly
- [ ] Pilot tracker `_internal/PILOT-TRACKER.md` exists with row per pilot (start date, vertical, prospect, assistant ID, DID, day-28 recommendation, day-31 outcome)

## Anti-patterns — explicitly rejected

| Rejected | Why |
|---|---|
| 14-day pilot like VoiceFleet | Insufficient signal for tier-fit; first 7 days are setup-bias |
| Auto-convert to Starter regardless of usage | Under-tiers accountants/solicitors with >600 min/mo — Adam press-back 2026-05-22 |
| Free pilot with no card | Tire-kicker filter absent; high false-pilot rate per saas-trial conversion data |
| Free pilot with Stripe Checkout but no trial flag | Charges card day-1; not actually free |
| Sell as "free trial" | Adam's frame: "first month free" / "pilot", not "trial" (claude-mem 11587) |
| Count any pilot as "customer" before day-31 conversion | LEO/bank/grant integrity risk (MEMORY.md callmeie-pre-revenue-no-paying-pilots) |
| Promise "callers can't tell it's AI" | Humans clock it ~90%; sell answered+booked not disguise (MEMORY.md no-undetectable-ai-overclaim) |
| Run >5 concurrent pilots | Worst-case burn cap; shallow attention risk; pre-revenue economic discipline |

## Outreach (separate doc — to be written after infra ships)

`_internal/PILOT-OUTREACH-PLAYBOOK.md` will cover:
- Lead source (LEO mentor intros / lead_research.py output / Limerick door-walk)
- Cold email templates per vertical (dental / cafe / salon / solicitor / accounting)
- Qualification criteria (call volume threshold, IE-based, vertical match)
- Onboarding call script (15 min — confirm hours, partner names, calendar share, vertical template tuning)

## Compliance + GDPR

- All pilot data handled under same DPA as paid customers — point at `/legal/dpa.html`
- Call recording disclosure mandatory in AI assistant first sentence (built into vertical templates)
- Pilot data retained 90 days post-cancellation then purged (per existing retention policy in `legal/privacy.html`)
- Pilot prospect's card-on-file PCI-DSS handled entirely by Stripe (we never see PAN)

## Change log

- 2026-05-22 — initial draft after Twilio purchase press-back; pilot economics computed from PRICING-SSOT §2 + Vapi €0.10/min reference
