---
id: a2p-10dlc-submission
title: A2P 10DLC Brand + Campaign Submission — Paste-Ready Values
role: internal-operating-doc
temporal_class: data
status: prototype
owner: claude-main
last_verified: 2026-05-29
verified_by: drafted after Twilio Business Profile approval (Anna 2026-05-29 12:50 UTC, ticket #27189947); field list pulled from canonical Twilio docs `https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/collect-business-info`
refresh_cadence: revise on Twilio rejection feedback or when monthly SMS volume grows past Low-Volume threshold (<6000 msg/day)
---

# A2P 10DLC Brand + Campaign Submission

Paste-ready value block for the two Twilio Trust Hub forms now unblocked by the Customer Profile approval (Anna 2026-05-29).

**Order of operations:**
1. **Trust Hub → Trust Products → CallMeIE (`BU1a8950fb31ba1d7e99cadfcec74ce8de`) → Edit and resubmit** = the Brand registration (Section 1 below)
2. After Brand approves (~1-3 days based on this week's SLA) → **Messaging → Services → CallMeIE Ireland Outbound (`MG5773dd9d6b3b577d9517361ebcb758d0`) → Compliance → Register A2P 10DLC Campaign** (Section 2 below)

---

## Section 1 — Brand registration (Trust Product re-submission)

Most of these auto-fill from the approved Customer Profile `BU58d684c9...`. Only the brand-specific fields below need manual entry:

| Field | Value |
|---|---|
| Business name | `CallMeIE Technologies Limited` |
| Business type | `Private Corporation` |
| Business industry | **`TECHNOLOGY`** |
| Business registration ID type | (whatever was used on the approved Customer Profile — likely `Other` or `RegistrationNumber`) |
| Business registration number | `816273` (CRO) |
| Website URL | `https://www.callmeie.ie` |
| Business identity | `ISV Reseller or Partner` |
| Business regions of operation | `Europe` only |
| Stock exchange | `None` |
| Stock ticker | blank |
| Company type | `Private` |
| Vertical (US carrier classification) | `TECHNOLOGY` (matches industry) |

**Brand contact email:** `hello@callmeie.ie` (matches website domain — Anna's 2026-05-26 rule)

**Authorized Representative #1:** (already on Customer Profile, will auto-link)
- First name: `Adam`
- Last name: `Vaughan`
- Job title: `Director`
- Job position: `Director`
- Phone: `+353857863564`
- Email: `hello@callmeie.ie`

**Social media profiles** (Twilio asks for at least one; if blank may trigger manual review):
- LinkedIn: [Adam to supply or leave blank]
- Facebook: `https://www.facebook.com/[CallMeIE page if exists, else blank]`
- Twitter: blank
- Instagram: blank

> **Skip-automatic-SEC-vet:** leave default (`false`). Low-Volume tier (under 6000 msg/day) doesn't need SEC vetting anyway; we comfortably fit there (5-20 msg/day projected).

---

## Section 2 — Campaign registration (after Brand approval)

Console → Messaging → Services → CallMeIE Ireland Outbound → Compliance → Register A2P 10DLC Campaign.

### Use case
`Customer Care` (transactional pilot prospect + end-caller callbacks; **not** Marketing, not 2FA, not Mixed)

### Volume tier
`Low Volume` (under 6000 msg/day; we project 5-20/day during pilot phase)

### `description` (40-4096 chars) — who sends, who receives, why

```
CallMeIE Technologies Limited is an Irish AI phone receptionist provider serving small businesses in Ireland (dental clinics, solicitor firms, accountancy practices, salons, cafes, trades). Outbound SMS is sent from a US +1 long code (TWILIO_FROM = +16624397271) to two recipient groups:

(a) Irish SMB owners during a 30-day product pilot — pre-onboarding confirmations, Stripe Checkout signup links, day-14 mid-pilot check-in summaries, day-28 usage reports, day-31 conversion confirmations.

(b) Irish consumer end-callers who request a callback through the deployed AI receptionist — appointment confirmations, missed-call follow-ups, requested information dispatches.

All recipients have either explicitly contracted for the service (pilot SMBs) or opted in via a recorded call disclosure (end-callers). Recorded disclosure includes (1) the line is automated, (2) the call may be recorded, (3) callbacks via SMS will be sent if requested. Volume is projected at 5-20 messages per day during pilot phase, growing to under 200 per day at full operation across all deployed customer lines.
```

### `message_flow` (40-2049 chars) — opt-in mechanism

```
Pilot prospects opt in by completing CallMeIE's Stripe Checkout signup link (sent by direct email from hello@callmeie.ie after a recorded 15-minute onboarding call where they verbally consent to the trial and explicitly authorise SMS communications about their pilot). The signup link is generated server-side at POST https://api.callmeie.ie/admin/api/pilot/signup; no public web form drives this — it is admin-mediated per prospect.

End-callers opt in by ringing the prospect's dedicated +353 number — the AI receptionist's first sentence discloses (1) the line is automated, (2) the call may be recorded, (3) any callback or appointment confirmation will be sent via SMS if requested. Consent is per-recipient, captured at the point of contact, and retained in the callmeie-receptionist Postgres database for 90 days per the published Data Processing Agreement at https://callmeie.ie/legal/dpa.html.

Privacy policy: https://callmeie.ie/legal/privacy.html
Terms of service: https://callmeie.ie/legal/terms.html
```

### `message_samples` (2-5 samples, 20-1024 chars each, brand-named, `[]` for variables)

**Sample 1 — Pilot signup link:**
```
CallMeIE: tap to complete your 30-day pilot signup for [BUSINESS_NAME]. Card on file, no charge until day 31. [LINK]. Reply STOP to opt out.
```

**Sample 2 — Day-0 line-live notification:**
```
CallMeIE: your dedicated line +[NUMBER] is live for [BUSINESS_NAME]. Try ringing it now. Reply STOP to opt out.
```

**Sample 3 — Day-28 usage report:**
```
CallMeIE: 28-day pilot report for [BUSINESS_NAME] — your line answered [N] calls and booked [M] appointments. Recommended tier: [TIER]. Day 31 auto-activates unless you reply. STOP to opt out.
```

**Sample 4 — End-caller callback confirmation:**
```
CallMeIE: [CALLER_NAME] booked your callback with [BUSINESS_NAME] for [TIME]. Reply 'reschedule' to change, STOP to opt out.
```

### `opt_in_message` (20-320 chars, includes brand + opt-out info)
```
CallMeIE: thanks for confirming your pilot signup. We'll text at day 0, day 14, day 28 and day 31 only — and only about your CallMeIE line. Reply STOP to opt out, HELP for support.
```

### `opt_out_message` (20-320 chars, confirms no further messages)
```
CallMeIE: you've been unsubscribed. No further messages will be sent. Email hello@callmeie.ie if this was a mistake or for support.
```

### `help_message` (20-320 chars, support contact)
```
CallMeIE: support at hello@callmeie.ie or +353 85 786 3564 (Adam, founder). Reply STOP to unsubscribe at any time.
```

### Keywords

| Field | Value |
|---|---|
| `opt_in_keywords` | `START,YES,UNSTOP` |
| `opt_out_keywords` | `STOP,UNSUBSCRIBE,CANCEL,END,QUIT` |
| `help_keywords` | `HELP,INFO,SUPPORT` |

### Flags

| Field | Value |
|---|---|
| `has_embedded_links` | **`true`** (Stripe Checkout links in samples 1) |
| `has_embedded_phone` | **`true`** (callback confirmations include numbers) |
| `has_embedded_phone` (numbers in body) | true — sample 2 + sample 4 |
| `subscriber_opt_in` | true (recorded verbal consent on call OR signed Stripe checkout) |
| `age_gated` | false (no adult content) |
| `direct_lending` | false |

---

## Anti-patterns — do not say these on the form

| Avoid | Use instead |
|---|---|
| "Marketing" / "Promotional" | "Customer Care" / "Account Notification" |
| "We send to anyone who calls" | "Recipients opt in via recorded verbal disclosure at first contact" |
| "Bulk SMS" / "mass send" | "Transactional, low-volume (5-20/day projected)" |
| Vague recipient definition | "Irish SMB pilot prospects" + "End-callers who ring deployed AI receptionist lines" |
| Missing opt-out language in samples | EVERY sample includes "Reply STOP to opt out" |
| Generic brand identifier | "CallMeIE:" prefix in every sample |

---

## Rejection-then-resubmit timeline

Per Anna's 2026-05-26 feedback on the Customer Profile and the 2026-05-29 approval one calendar day after evidence upload:
- Initial submission expected response: 1-3 business days
- If rejected: typically asks for additional documentation (DUNS-equivalent, more specific opt-in proof, video walkthrough of the AI receptionist disclosure)
- Maximum 2-3 review cycles to approval in practice

Plan: submit Brand by end of business day, follow up if no response after 72 hours via the existing ticket thread.

---

## What to do if Twilio asks for additional opt-in proof

Adam can supply on request:
- Recording of a sample onboarding call where the prospect verbally consents to the trial + SMS communications (held in Vapi cloud per existing receptionist setup)
- Screenshot of the Stripe Checkout consent step (Stripe shows "By providing your card information, you authorise CallMeIE to charge your card per the subscription terms")
- The PILOT-PROGRAM.md spec (`_internal/PILOT-PROGRAM.md` Day 0 / Day 14 / Day 28 / Day 31 email templates as proof of the pre-disclosed cadence)
- The AI receptionist first-sentence disclosure script (`callmeie-hub/receptionist/scripts/CLAIRE-PROMPT-RESTRUCTURE-PROPOSAL-2026-05-11.md` or equivalent — confirms automated + recorded + SMS-on-request)

---

## Change log

- 2026-05-29 — initial draft after Customer Profile approval same day; field list pulled from canonical Twilio A2P 10DLC docs; tailored to CallMeIE Ireland pilot stage (Low-Volume tier).
