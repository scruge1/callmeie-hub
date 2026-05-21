# Legal Compliance Matrix — CallMeIE Customer Contract Pack

**Prepared:** 2026-05-21
**Prepared by:** in-house research (Claude Opus 4.7), commissioned by Adam Vaughan
**Subject pack:** Order Form (`_internal/order-forms/order-form-template.md`), Master Service Agreement / ToS (`legal/terms.html`), Data Processing Agreement (`legal/dpa.html`), ROPA (`_internal/ropa-2026.md`)
**Contracting entity:** CallMeIE Technologies Limited — CRO 816273, incorporated 21 May 2026, Limerick.

---

## ⚠ READ FIRST — what this document is and is not

This is **legal research, not legal advice.** It was produced in-house to verify, by the book and against primary statutory sources, that the customer-contract pack is compliant and enforceable under Irish and EU law — and to make any eventual solicitor review **fast and cheap** instead of from-scratch.

Every verdict is one of three kinds, and the distinction is load-bearing:

- **VERIFIED** — checked against the primary statute text (quoted, with a cited URL). Defensible to act on in-house.
- **NEEDS-CHANGE** — the contract is wrong or weak against a verified statutory requirement; the fix is mechanical and is given below as drop-in wording.
- **NEEDS-SOLICITOR** — a genuine litigation-exposure judgement call where a wrong answer has real downside and a solicitor's professional-indemnity backing matters. Research narrows it; it does not close it.

§4 gives the explicit two-list split. **Do not treat the VERIFIED column as a substitute for a solicitor on the NEEDS-SOLICITOR items** — specifically the kill fee (b) and the liability cap (c).

---

## §0 — The pivotal finding: customer classification

Every consumer-protection verdict in this matrix turns on one question: **are CallMeIE's customers "consumers"?**

**Answer — VERIFIED.** They are not. Under the **Consumer Rights Act 2022, s.2(1)**, a "consumer" is *"an individual acting for purposes that are wholly or mainly outside that individual's trade, business, craft or profession"*; a "trader" is *"a natural person or legal person … acting for purposes relating to [their] trade, business, craft or profession"* (verified verbatim — irishstatutebook.ie/eli/2022/act/37/section/2). A **sole trader buying an AI receptionist, Document Ops, or a website *for his business* is acting within his trade → he is a trader, not a consumer.** A Ltd company can never be a consumer (the definition is restricted to an individual / natural person). The same test runs through Directive 2011/83/EU Art.2(1) and Directive 93/13/EEC Art.2(b).

Three consequences:

1. **There is no Irish protective tier between "consumer" and "large business."** The unfair-terms regime (Directive 93/13/EEC → CRA 2022 Part 6), the 14-day cooling-off right, and the inertia-selling rules are **consumer-only**. A sole trader gets none of them. This makes the lock-ins and exit fees **more** enforceable against CallMeIE's actual customer base, not less — they are tested only by the common-law penalty doctrine, not the statutory unfair-terms grey list.

2. **The burden of proof is on CallMeIE.** CRA 2022 s.2(3): it is for the *trader* to show that an individual was *not* acting as a consumer. So the matrix still treats the consumer path as a live edge case — a genuine consumer could sign — and the mitigation is cheap (see clause (h)): a one-line **customer warranty** + **onboarding screening**.

3. **The "mixed customer base" in the brief means mixed Ltd / sole-trader — both are traders.** It does *not* mean mixed consumer / business. Consumer law is therefore an edge-case hedge, not a primary exposure. Where a clause is COMPLIANT for a trader but NEEDS-CHANGE for a consumer, the **operative verdict is the trader one**, with the consumer fix listed as low-cost insurance.

---

## §1 — Clause-by-clause matrix (summary)

| ID | Clause (where) | Governing law | Verdict | Action |
|----|----------------|---------------|---------|--------|
| **a** | Minimum-term lock-ins 12/12/18-mo + accelerated remaining-term fee (Order Form §B1b, §B5) | Common-law penalty doctrine; CRA 2022 Sch.5 (consumer only); *Launceston Property Finance v Burke* [2017] IESC 62 | **COMPLIANT (trader)** / NEEDS-CHANGE (consumer edge case) | ✅ **POLISH APPLIED 2026-05-21** — §B1b now offers instalment-or-lump-sum on early exit + a "specifically drawn to attention" confirmation |
| **b** | "Kill fee" — flat 30% of remaining balance (Order Form §H2) | Common-law penalty doctrine — *Dunlop* genuine-pre-estimate test; *Sheehan v Breccia* [2018] IECA | **NEEDS-CHANGE → NEEDS-SOLICITOR** | Recast flat % as actual-work-done + a reasoned, capped slot-loss estimate |
| **c** | Liability cap = fees paid in prior 12 months (Order Form §I, ToS §8, DPA §7) | Sale of Goods and Supply of Services Act 1980 ss.39–40; GDPR Art.82; CRA 2022 Part 4 (consumer) | **NEEDS-CHANGE → NEEDS-SOLICITOR** (final figures) | Name the non-excludable heads explicitly; for one-off Builds switch to 100% of Build fee for 24 months |
| **d** | Deemed acceptance — 14-day deliverable sign-off (Order Form §B1) & "continued use = acceptance" of term changes (ToS §11) | Contract formation (*Felthouse v Bindley*); CRA 2022 Sch.5 items 10–11 (consumer) | §B1(b): **COMPLIANT** · §11: **NEEDS-CHANGE** | §B1(b) fine. Redraft §11 with advance notice + a penalty-free exit right |
| **e** | Late-payment auto-terms (Order Form §D4) | European Communities (Late Payment in Commercial Transactions) Regulations 2012 (S.I. 580/2012, as amended); Directive 2011/7/EU | **NEEDS-CHANGE** | ✅ **FIXED THIS SESSION** — correct instrument, rate wording, tiered €40/€70/€100, consumer carve-out |
| **f** | IP transfer-on-payment + portfolio carve-out + Managed source-retention (Order Form §F, §C2, §B1b) | Copyright and Related Rights Act 2000 ss.116, 118, 120, 121 | **NEEDS-CHANGE** | ✅ **APPLIED 2026-05-21** — §F2 recast as self-executing s.121 assignment + new §F5 moral-rights waiver; assignor-signature requirement + cross-refs already fixed (§3) |
| **g** | DPA — Article 28(3) completeness + sub-processor transfer adequacy (`legal/dpa.html`) | GDPR Arts 28, 32–36, 44–49; Implementing Decision (EU) 2021/914 (SCCs); Implementing Decision (EU) 2023/1795 (EU-US DPF) | **NEEDS-CHANGE → NEEDS-SOLICITOR** | 4 mandatory Art.28(3) clauses confirmed missing; DPF over-claimed (Vapi/Anthropic/xAI); no signed master DPA exists — needs a complete Art 28 DPA + SCCs |
| **h** | Consumer / distance-selling / cooling-off exposure (whole pack) | CRA 2022 s.2, Part 4 Ch.3, s.125; Directive 2011/83/EU; Electronic Commerce Act 2000; eIDAS Reg. (EU) 910/2014 | **COMPLIANT (classification)** / NEEDS-CHANGE (conditional cooling-off module) | ✅ **WARRANTY APPLIED 2026-05-21** (Order Form §D6); onboarding screening / consumer cooling-off module still recommended |

---

## §2 — Per-clause detail and recommended wording

### Clause (a) — Minimum-term lock-ins + accelerated exit fee

**What the pack says.** Order Form §B1b "Managed" website plans: Launch €69/mo (12-month minimum), Business €100/mo (12-month minimum), Premium €149/mo (18-month minimum); on early cancellation "the remaining minimum-term monthly fees become payable as one final invoice." Order Form §B5 AI Receptionist "Growth": 3-month minimum.

**The law.** For a **trader** customer (CallMeIE's whole base — see §0) there is **no statutory unfair-terms control**; the only live control is the common-law penalty doctrine, which bites only on sums payable *on breach*. The Supreme Court in *Launceston Property Finance Ltd v Burke* [2017] IESC 62 confirmed that sums forming **part of the contractual price, payable regardless of breach,** fall outside the penalty doctrine entirely. The §B1b framing — "the minimum term is solely how the build cost is recovered" for a €0-upfront build — deliberately and correctly characterises the lock-in as **deferred price**, not a breach charge.

**Verdict — COMPLIANT (trader).** Edge case: against a *consumer*, immediate acceleration of the entire remaining term as a day-one lump sum risks CRA 2022 Schedule 5 item 5 (presumed-unfair "disproportionately high sum in compensation") and the s.134 transparency duty.

**Recommended polish (low-cost insurance, not required for traders):**
> *Early termination of a Managed plan within the minimum term: because the website was built and delivered with no upfront charge, the minimum-term fees are deferred payment for that build. On early cancellation the Customer may either (a) continue paying the remaining minimum-term monthly fees on the normal monthly schedule, or (b) settle the remaining balance in one payment. This minimum-term commitment is stated in bold on the first page of the Order Form and the Customer confirms it has been specifically drawn to their attention.*

Adding the instalment option and the bold first-page flag removes the consumer-path exposure cheaply.

**✅ APPLIED 2026-05-21.** The §B1b minimum-term paragraph now offers the instalment-or-lump-sum choice, states the term is "deferred payment … not a penalty," and carries the "important term … specifically drawn to their attention" confirmation.

---

### Clause (b) — "Kill fee" (flat 30% of remaining balance) — ⚠ NEEDS-SOLICITOR

**What the pack says.** Order Form §H2: "Build engagements, mid-build: Customer may cancel before launch with a kill fee of **30% of remaining contracted balance** (industry-standard 25–40% band). … CallMeIE retains the deposit + the kill fee in lieu of remaining work."

**The law — VERIFIED.** Ireland still applies the ***Dunlop* "genuine pre-estimate of loss" test, not the English *Cavendish*/Makdessi "legitimate interest" test.** The Court of Appeal in *Sheehan v Breccia / Flynn v Breccia* (30 July 2018) expressly **declined to adopt** *Cavendish*, holding itself bound by existing Irish law, and confirmed: a clause is enforceable liquidated damages only if it is "a genuine attempt by the parties to estimate in advance the loss which will result from the breach" — otherwise it is an unenforceable penalty (verified — mccannfitzgerald.com knowledge note on the case). **The penalty doctrine applies to business customers, not just consumers.**

**Why the current clause is exposed.** A **flat 30%** applied uniformly is the textbook penalty vulnerability: it is the same percentage whether the customer cancels at 5% or 95% of the build. A single sum applicable to events of widely differing gravity is exactly what *Dunlop* condemns. "Industry-standard 25–40% band" has **no legal weight** — market practice does not convert a penalty into liquidated damages. The CoA in *Breccia* struck down a surcharge precisely because it "applied broadly without case-by-case tailoring."

**Verdict — NEEDS-CHANGE; final wording NEEDS-SOLICITOR.** A cancellation charge is legitimate in principle (CallMeIE does suffer real loss — allocated developer time, a lost and unfillable slot) but it must be drafted as a genuine pre-estimate, not a flat percentage.

**Recommended wording (draft — solicitor to confirm before first use):**
> *If the Customer cancels a Build engagement before launch, CallMeIE will invoice for: (i) all work actually completed to the cancellation date, charged at the rates in this Order Form or, where none is stated, at €60/hour; plus (ii) a cancellation charge representing CallMeIE's genuine pre-estimate of the loss caused by the cancelled booking — the cost of the development slot reserved and not re-fillable at short notice — being the lesser of 30% of the remaining contracted balance or €[X]. The deposit is credited against these amounts. Work completed to date is delivered as-is and the GitHub repository transferred on payment.*

Tying the charge to **actual work done + a stated, reasoned, capped slot-loss estimate** reframes it as a genuine pre-estimate and removes the flat-rate penalty risk. **The cap figure €[X] and the final wording should be settled with a solicitor** — this is the single clause in the pack with the clearest litigation exposure.

*Reference (Irish market):* Web Design Ireland uses "deposit returned minus costs for works completed" (webdesignireland.ie) — the cleanest *Dunlop*-aligned model. Designwest's "full quoted cost on late cancellation" (designwest.ie) is *more* aggressive than CallMeIE's and more exposed.

---

### Clause (c) — Liability cap — ⚠ NEEDS-SOLICITOR (final figures)

**What the pack says.** Order Form §I + ToS §8 + DPA §7: aggregate liability for any claim capped at "the fees you paid us in the 12 months prior to the claim" (self-serve subscription); Bespoke caps negotiated per Order Form. Carve-out: nothing limits liability for death/personal injury by negligence, fraud/fraudulent misrepresentation, or "any liability that cannot be excluded under Irish law."

**The law — VERIFIED.** The **Sale of Goods and Supply of Services Act 1980 s.39** implies into every business-supplied service contract that the service will be supplied "with due skill, care and diligence." **s.40** allows those implied terms to be negatived or varied by an express term — but "where the recipient of the service deals as consumer it must be shown that the express term is **fair and reasonable and has been specifically brought to his attention**" (verified verbatim — irishstatutebook.ie/eli/1980/act/16/section/40). For a **business** recipient the cap can be varied by an express term without satisfying that statutory test (ordinary common-law controls still apply). **GDPR Art.82**: a data subject's right to compensation cannot be capped by a B2B contract — but Art.82(5) controller↔processor *apportionment* can be.

**Verdict — NEEDS-CHANGE.** The 12-month-fees structure is market-standard and enforceable for traders (the Irish SaaS Workvivo Ltd uses the identical "twelve (12) months preceding" wording — workvivo.com/terms; Intercom likewise). Two gaps:
1. The carve-out relies on a catch-all ("any liability that cannot be excluded under Irish law") rather than naming the heads. Better practice names them: SGSSA s.39 implied terms, CRA 2022 Part 4 (for any consumer), GDPR Art.82.
2. **For a one-off website Build, a trailing 12-month window is the wrong shape** — if a defect surfaces 13+ months after launch the cap could read as €0. Switch Builds to a fixed reference.

**Recommended wording (draft — solicitor to confirm the figures):**
> *Subject to the carve-outs below, our total aggregate liability for all claims arising out of or in connection with this Agreement (in contract, tort including negligence, breach of statutory duty or otherwise) is limited to: (a) for self-serve subscription Services — the greater of the fees paid under the relevant Order Form in the 12 months before the event giving rise to the claim, or €[X]; (b) for one-off Build engagements — 100% of the total fees paid for that Build, for claims made within 24 months of launch-handoff; (c) for Bespoke engagements — the amount stated in the Order Form.*
> *Nothing limits liability for: (i) death or personal injury caused by negligence; (ii) fraud or fraudulent misrepresentation; (iii) breach of the terms implied by section 39 of the Sale of Goods and Supply of Services Act 1980; (iv) where the Customer is a consumer, any liability under Part 4 of the Consumer Rights Act 2022 or any term that may not lawfully be excluded against a consumer; (v) a controller's or processor's liability to a data subject under Article 82 GDPR; or (vi) any other liability that cannot lawfully be limited.*

The €[X] floor and the Bespoke caps are commercial-risk judgement calls → **solicitor.**

---

### Clause (d) — Deemed acceptance by silence

**§B1(b) — 14-day deliverable sign-off — VERDICT: COMPLIANT.** *Felthouse v Bindley* (silence is not acceptance) prohibits imposing a *new* contract on a stranger by silence. §B1(b) is different: it is an agreed mechanism *inside an already-signed contract* defining when a deliverable is deemed accepted. A clear, reasonable, clearly-triggered 14-day sign-off window is standard, enforceable B2B practice. No change needed. (Optional: state the 14-day window in bold in the launch-handoff email.)

**ToS §11 — "continued use after the notice period is acceptance" of *changed* terms — VERDICT: NEEDS-CHANGE.** Changing the bargain itself by inferring consent from inaction is weaker. For a *consumer* it engages CRA 2022 Schedule 5 items 10 (binding the consumer to terms they had no real opportunity to see) and 11 (unilateral variation without a specified valid reason). Even B2B it is the pack's weakest formation point. The robust fix is advance notice + a genuine penalty-free exit:

**Recommended wording for ToS §11:**
> *We may amend these Terms only for a valid reason — to comply with a change in law or regulation; to reflect a change in our sub-processors or the technical operation of the Service; or for documented security reasons. We will give 30 days' written notice to your Order Form contact email. If you do not accept a material change you may cancel the affected Service before the change takes effect with no early-termination charge, and we will refund any pre-paid fees for the unused period. Continued use of the Service after the change takes effect constitutes acceptance.*

---

### Clause (e) — Late payment — ✅ FIXED THIS SESSION

**What the pack said.** Order Form §D4: "Late payment terms per the **Late Payment in Commercial Transactions Regulations 2002** (8% above ECB rate + €40 fixed fee) auto-apply."

**The law — VERIFIED.** The 2002 instrument (S.I. 388/2002) is **superseded.** The instrument in force is **S.I. No. 580 of 2012 — European Communities (Late Payment in Commercial Transactions) Regulations 2012**, transposing **Directive 2011/7/EU**, itself amended by S.I. 74/2013, 196/2014 and 281/2016 (title verified — irishstatutebook.ie/eli/2012/si/580). Three corrections were needed:
- **Citation** — wrong; now corrected to "S.I. No. 580 of 2012, as amended."
- **Interest rate** — "8% above ECB rate" is right in substance but should read "**8 percentage points above the ECB main refinancing reference rate**" (the reference rate is fixed each 1 January and 1 July).
- **Fixed compensation** — "€40" is only the floor. The Irish Regulations set a **tiered scale: €40** (debt ≤ €1,000), **€70** (€1,000–€10,000), **€100** (over €10,000), plus reasonable additional recovery costs.
- **Scope** — the regime is **B2B only**; it does not apply to a consumer. The fixed §D4 wording now carves this out.

**Verdict — NEEDS-CHANGE → done.** See §3 for the wording applied.

---

### Clause (f) — IP ownership / assignment

**What the pack says.** Order Form §F2: CallMeIE-developed deliverables "transfer to the Customer upon full payment of all milestone invoices." §C2: "Full source code … ownership transferred to Customer." §B1b Managed override: CallMeIE retains the source code. §F3: portfolio licence with 14-day opt-out.

**The law — VERIFIED.**
- **Copyright and Related Rights Act 2000 s.120(3):** a copyright assignment "is not effective unless it is in writing and signed by or on behalf of the assignor."
- **s.121:** an agreement on *future copyright* "signed by or on behalf of the prospective owner" makes the copyright **vest automatically in the assignee** when it comes into existence — no further deed needed (verified — irishstatutebook.ie/eli/2000/act/28/section/121).
- **s.118:** moral rights (paternity, integrity) are **incapable of assignment**. **s.116:** they *can* be **waived**, in writing signed by the person waiving them.

**Verdict — NEEDS-CHANGE (drafting precision).**
1. "Transfer upon full payment" reads as an *agreement to assign*, not a self-executing assignment. Recast it in operative s.121 language so copyright vests automatically on payment.
2. **The Order Form must be signed by CallMeIE** (the assignor) for the assignment to satisfy s.120(3). The internal note's "customer replies 'I agree'" flow gets only the *assignee's* signature — insufficient. The flow must capture CallMeIE's counter-signature. (Defect #8 below — fixed.)
3. **No moral-rights clause exists.** A customer will modify, rebrand and not credit CallMeIE — that needs an express s.116 waiver. Currently missing — add one.
4. §F2/§C2 ("ownership transferred") flatly contradict §B1b's Managed override. The override should hold (it is explicit) but each of §F2/§C2 should carry an inline cross-reference. (Defect #9 below — fixed.)

**Recommended wording (assignment + moral rights):**
> *Assignment. With effect from CallMeIE's receipt of payment in full of all milestone invoices for an engagement, CallMeIE hereby assigns to the Customer, by way of present assignment of future copyright under section 121 of the Copyright and Related Rights Act 2000, all copyright and other intellectual property rights in the CallMeIE-developed deliverables for that engagement (code, design, configuration and AI prompts), to vest in the Customer automatically on their coming into existence and on payment, with no further document required. This clause does not apply to Managed engagements (see §B1b) or to pre-existing CallMeIE IP (§F4).*
> *Moral rights. To the fullest extent permitted by sections 116 and 118 of the Copyright and Related Rights Act 2000, CallMeIE unconditionally and irrevocably waives all moral rights in the deliverables, including the paternity and integrity rights, in favour of the Customer and its successors and licensees.*

The portfolio licence (§F3) and the Managed source-retention model are enforceable as drafted — no IP-law defect, only the cross-reference clean-up.

**✅ APPLIED 2026-05-21.** Order Form §F2 recast as a self-executing present assignment of future copyright under CRRA 2000 s.121; a new §F5 moral-rights waiver added (s.116). The assignor-signature requirement was already added (§3 defect 8) and the §B1b/§C2/§F2 cross-references de-conflicted (§3 defect 9).

---

### Clause (g) — DPA: Article 28(3) completeness + sub-processor transfers — ⚠ NEEDS-SOLICITOR

> **Scope note (updated 2026-05-21).** `legal/dpa.html` is the public summary. It claims a "full signed v1.0 PDF" is sent on request — but **no such document exists**: a repo-wide search found no DPA PDF and Adam confirms he holds none. `legal/dpa.html` is therefore the *only* DPA text. The "MISSING" findings below are **confirmed missing**, not "maybe in an unseen PDF" — so the DPA is **non-compliant with GDPR Article 28 on its face**. The live page's "full v1.0 PDF on request" claim is itself a defect: either a complete DPA must be produced or that claim removed.

**Article 28(3) completeness — VERIFIED against GDPR Art.28.** Of the nine mandatory stipulations a processor contract must contain, the public summary shows:

| Art.28(3) item | Status in public summary |
|---|---|
| (a) process only on documented instructions | PRESENT (§1) |
| (b) confidentiality commitment of authorised staff | **MISSING** |
| (c) Art.32 security measures | PRESENT (§6) |
| (d) sub-processor conditions + flow-down + full liability | WEAK — 30-day notice present; **no flow-down / full-liability wording** |
| (e) assist controller with data-subject-rights requests | **MISSING** |
| (f) assist with Arts 32–36 — incl. **personal-data-breach notification** | **MISSING — most serious gap** |
| (g) delete/return data at end of service | PRESENT (§4) |
| (h) make available compliance info + allow audits | WEAK / effectively absent |
| final para — "immediately inform" controller of an infringing instruction | **MISSING** |

**Verdict — NEEDS-CHANGE; the breach-notification clause NEEDS-SOLICITOR** for the precise timeline/content. A processor contract for a service that **records phone calls** with no breach-notification clause is the headline defect.

**Sub-processor third-country transfers — VERIFIED (partial).**
- The **EU-US Data Privacy Framework is in force in 2026** — the General Court dismissed the *Latombe* challenge (T-553/23) on 3 Sept 2025; a CJEU appeal is pending. DPF is a valid mechanism but carries annulment risk — **do not rely on it alone.**
- **The DPA over-claims DPF coverage — register-confirmed 2026-05-21.** The official EU-US DPF register (`dataprivacyframework.gov`, snapshot dated 2026-05-21, queried via its data API — 3,612 active + 3,891 inactive entities) shows: **Twilio Inc.** (OrganizationId 5394) and **Google LLC** (OrganizationId 5780) are **ACTIVE** participants across EU-US DPF + UK Extension + Swiss-US — the DPA's DPF reliance for these two is correct. **Vapi, Anthropic and xAI do NOT appear on the register** under any name variant — none is DPF-certified (Anthropic's own privacy policy independently confirms SCC reliance). Labelling Vapi / Anthropic / xAI "under DPF" in DPA Schedule A/B is a **confirmed defect** — a transfer relying on DPF to a non-certified importer is unlawful; all three must move to SCCs.
- The DPA **asserts** "DPF + SCCs" but never **incorporates** the SCCs. "Covered by SCCs" is legally empty — the SCCs (Commission Implementing Decision (EU) 2021/914), **Module Three** for processor-to-processor onward transfers, must actually be signed with each US sub-processor and the Annexes completed.

**DPF register check — DONE 2026-05-21** (Opus agent, via the register's data API at `dpfapi.azurewebsites.net`): Twilio + Google certified; Vapi, Anthropic, xAI absent from the register → must use SCCs. See the bullet above.

**Recommended DPA changes:** add the four missing Art.28(3) clauses (the wording is standard — see any EDPB-aligned DPA template); add a per-sub-processor transfer-mechanism table (importer / role / DPF-or-SCC-Module-Three / verified-date); add a DPF-annulment SCC-fallback clause; correct Schedule A/B so Vapi, Anthropic and xAI are not labelled "under DPF" (register-confirmed non-certified 2026-05-21) and are moved to SCCs; carve the public **demo line** out of the DPA — for `+353 61 788 120` CallMeIE is a **controller**, not a processor, so that data belongs in the Privacy Policy, not the processor DPA.

---

### Clause (h) — Consumer protection, distance selling, cooling-off

**Customer classification — VERIFIED COMPLIANT.** Covered in §0: traders, not consumers; no middle tier.

**Recommended addition — customer warranty (Order Form).** Because the s.2(3) burden is on CallMeIE:
> *The Customer warrants that it is entering this Agreement wholly for purposes relating to its trade, business, craft or profession and not as a consumer, and acknowledges that consumer-protection law, including the Consumer Rights Act 2022, does not apply to this Agreement.*
This does not override the law (a court still applies the substance test) but it is strong evidence and standard practice. **✅ APPLIED 2026-05-21** — added to the Order Form as §D6.

**Cooling-off / 14-day right of withdrawal — NEEDS-CHANGE (conditional).** The 14-day right under the Consumer Rights Act 2022 Part 4 Ch.3 (which replaced S.I. 484/2013) applies **only to consumer distance contracts** — so it does not apply to the trader base. *But* if a genuine consumer ever signed, the pack has **no cooling-off notice**, and failure to inform extends the withdrawal window to up to 12 months (Directive 2011/83/EU Art.10). Two ways to close this:
- **Cheapest — onboarding screening:** confirm at sign-up that every customer is a business; never issue the pack to a consumer. Combined with the §0 warranty, this is sufficient for a pure-B2B operation.
- **Belt-and-braces — a conditional consumer cooling-off module:** a clause that activates only for consumer customers, with the statutory Model Cancellation Form, an express-start-of-service acknowledgement, and (for website builds) a "clearly personalised goods" acknowledgement.

**Inertia selling — VERIFIED.** CRA 2022 s.125: a consumer's silence is *not* consent (also blacklisted under Directive 2005/29/EC Annex I). This is consumer-only — it does not bite the trader base — but it reinforces the clause (d) §11 redraft.

**E-signature — VERIFIED COMPLIANT.** Under the Electronic Commerce Act 2000 (ss.9, 13, 19, 22) and eIDAS Regulation (EU) 910/2014 Art.25, an "I agree" email + signed PDF validly forms and signs a B2B services contract and a copyright assignment — neither is an ECA 2000 s.10 excluded document. **One caveat (see clause (f)):** the IP assignment needs the **assignor's** signature, so the Order Form must be **counter-signed by CallMeIE**, not signed by the customer alone.

---

## §3 — Internal contradictions: defects found and fixed this session

Nine internal defects were found in the pack — clauses that contradict each other or each other's facts. These are not statute-compliance issues, but a self-contradicting pack is itself an enforceability and transparency risk. All nine were **fixed this session** (per Adam's instruction "Matrix + fix defects now"):

| # | Defect | File | Fix applied |
|---|--------|------|-------------|
| 1 | Order Form signature block named "Adam Vaughan / Sole Trader (until Ltd incorporation)" — entity-correction commit `a87dcbf` missed it | order-form-template.md §J | Changed to CallMeIE Technologies Limited; signatory title → "Director" |
| 2 | ROPA "Controller of record: Adam Vaughan trading as CallMeIE Technologies" — sole-trader framing contradicts DPA §8 (Ltd) | ropa-2026.md | Controller → CallMeIE Technologies Limited (CRO 816273); section headings updated; v1.1 change-log entry appended |
| 3 | ROPA breach contact `adam@callmeie.ie` — that mailbox does not exist | ropa-2026.md | Changed to `hello@callmeie.ie` |
| 4 | ToS §4 "no minimum term, no lock-in" — directly contradicts Order Form §B1b/§B5 lock-ins | terms.html §4 | Reworded to state Doc Ops + Care subscriptions are month-to-month while Managed website plans and the Receptionist Growth tier carry minimum terms per the Order Form |
| 5 | ToS §9 "we do not pay SLA credits" — contradicts Order Form §E3 "1-day Care credit" | terms.html §9 | Carved out that Care/Managed customers receive the service credit stated in their plan / Order Form |
| 6 | ToS §7 "no pro-rata refunds" / "effective at end of billing period" — contradicts Order Form §H1 "30 days' notice + final pro-rated invoice" | terms.html §7 | Reworded so subscription cancellation notice + pro-rata follow the Order Form §H |
| 7 | Order Form §D4 cited the superseded "Late Payment … Regulations 2002" | order-form-template.md §D4 | Corrected to S.I. 580/2012 (as amended); rate wording; tiered €40/€70/€100; consumer carve-out |
| 8 | Order Form internal note: "customer replies 'I agree'" flow gets only the customer's signature — insufficient for the IP assignment (CRRA s.120(3) needs the assignor's signature) | order-form-template.md internal notes | Note corrected to require CallMeIE's counter-signature |
| 9 | Order Form §C2 / §F2 "ownership transferred" contradict §B1b Managed source-retention with no cross-reference | order-form-template.md §C, §F | Inline cross-references to §B1b added |

A 10th minor item — ToS §1 defines "Customer" as "the legal entity that signs an Order Form," but a sole trader is a natural person, not a legal entity — was also corrected to "the legal entity or individual that signs an Order Form."

---

## §4 — The honest split: verified ourselves vs genuinely needs a solicitor

### ✅ VERIFIED IN-HOUSE — defensible on cited statute (no solicitor required to rely on these)

- **Customer classification** — traders, not consumers (CRA 2022 s.2(1), verified verbatim). The "not a consumer" warranty is standard, low-risk to add — **applied this session (Order Form §D6).**
- **Late-payment correction (e)** — pure citation/figure fix; S.I. 580/2012 verified. **Fixed this session.**
- **E-signature validity (h)** — ECA 2000 + eIDAS Art.25 verified.
- **IP assignment mechanism (f)** — CRRA ss.116/118/120/121 verified; the self-executing s.121 wording and the moral-rights waiver are mechanical statutory fixes. **Applied this session** (Order Form §F2 recast + new §F5).
- **The nine internal contradictions (§3)** — factual corrections, zero legal judgement. **Fixed this session.**
- **Lock-in characterisation (a)** as deferred price — defensible for traders on *Launceston v Burke*. Transparency polish **applied this session** (Order Form §B1b).
- **DPA Art.28(3) missing-clause list (g)** — the four missing clauses are *mandatory verbatim* GDPR requirements; identifying them is statute-compliance, not judgement.

### ⚠ GENUINELY NEEDS A SOLICITOR — litigation exposure; a wrong call has real downside

- **(b) Kill fee** — the final liquidated-damages wording and the cap figure. Penalty-vs-liquidated-damages is a judgement call; the current flat 30% is a live penalty risk; a solicitor's PI backing matters here. **Highest priority.**
- **(c) Liability cap** — the final cap figures, the Bespoke caps, and the consumer-floor interaction with CRA 2022 Part 4.
- **(g) DPA** — the precise breach-notification timeline/content; **reconciling the public summary against the full signed v1.0 PDF**; the actual incorporation of SCCs (signing Module Three SCCs with each US sub-processor and completing the Annexes) is a real legal task, not a wording tweak.
- **(h) cooling-off** — whether a bespoke website build qualifies for the "clearly personalised goods" exclusion, if a consumer ever buys one (fact-specific).
- **(d) §11** — the final change-of-terms wording (the pack's weakest formation point).

### 👤 ADAM-ACTION — human steps, not solicitor

- ~~Confirm each US sub-processor on `https://www.dataprivacyframework.gov/list`.~~ **DONE 2026-05-21** — register-confirmed via the DPF data API: Twilio Inc. (OrgId 5394) + Google LLC (OrgId 5780) ACTIVE; Vapi, Anthropic, xAI NOT on the register → SCCs required for those three.
- Reconcile the public `legal/dpa.html` summary against the full signed v1.0 DPA PDF.
- ~~Fill the registered-office address and VAT-number blanks in Order Form §A.~~ **DONE 2026-05-21** — §A carries the registered office (40 Gouldavoher Estate, Limerick, V94 HWH7, Ireland) and VAT no. IE8490023T.

---

## §5 — Sources (primary statutory sources cited)

**Verified directly this session (URL opened, content confirmed):**
- Consumer Rights Act 2022 s.2 (consumer/trader definitions) — https://www.irishstatutebook.ie/eli/2022/act/37/section/2/enacted/en/html
- Sale of Goods and Supply of Services Act 1980 s.40 — https://www.irishstatutebook.ie/eli/1980/act/16/section/40/enacted/en/html
- Copyright and Related Rights Act 2000 s.121 — https://www.irishstatutebook.ie/eli/2000/act/28/section/121/enacted/en/html
- S.I. No. 580/2012 Late Payment in Commercial Transactions Regulations — https://www.irishstatutebook.ie/eli/2012/si/580
- McCann FitzGerald — Court of Appeal restates the law on penalty clauses (*Sheehan v Breccia*) — https://www.mccannfitzgerald.com/knowledge/aviation-and-asset-finance/court-of-appeal-restates-law-on-penalty-clauses-and-enforcement-costs

**Cited by the research streams (Irish Statute Book ELI-pattern URLs — same verified URL scheme):**
- Consumer Rights Act 2022 (full text) — https://www.irishstatutebook.ie/eli/2022/act/37/enacted/en/html
- CRA 2022 ss.111–125 (cancellation, inertia selling) — https://www.irishstatutebook.ie/eli/2022/act/37/section/{111…125}/enacted/en/html
- CRA 2022 ss.132–134, Schedule 5 (unfair terms) — .../section/{132,133,134}/... and .../schedule/5/...
- Sale of Goods and Supply of Services Act 1980 s.39 — https://www.irishstatutebook.ie/eli/1980/act/16/section/39/enacted/en/html
- Copyright and Related Rights Act 2000 ss.116, 118, 120 — https://www.irishstatutebook.ie/eli/2000/act/28/section/{116,118,120}/enacted/en/html
- Electronic Commerce Act 2000 — https://www.irishstatutebook.ie/eli/2000/act/27/enacted/en/print
- GDPR Art.28 — https://gdpr-info.eu/art-28-gdpr/ ; Art.82 — https://gdpr-info.eu/art-82-gdpr/
- *Launceston Property Finance v Burke* [2017] IESC 62 — https://www.casemine.com/judgement/uk/5da02bf64653d058440f9942
- CCPC unfair contract terms — https://www.ccpc.ie/consumers/contracts-and-services/contract-terms-that-may-be-unfair/
- Citizens Information — unfair contract terms — https://www.citizensinformation.ie/en/consumer/consumer_laws/unfair_contract_terms.html

**Market comparators (Irish/established SaaS — practice, not authority):**
- Workvivo Ltd (Irish SaaS — 12-month-fees liability cap) — https://www.workvivo.com/terms/
- Web Design Ireland (deposit-minus-work cancellation) — https://www.webdesignireland.ie/website-design-development-terms
- Ireland Website Design (IP-on-payment) — https://www.irelandwebsitedesign.com/terms-and-conditions/

---

## §6 — Honest limitations of this research

1. **Not legal advice.** Produced by an AI research process. It verifies statutory text and flags mismatches; it does not replace a solicitor on the NEEDS-SOLICITOR items (§4).
2. **The DPA (clause g) — there is no separate signed master DPA.** A repo-wide search found no DPA PDF and Adam confirms none exists; `legal/dpa.html` is the only DPA text. The Article 28 gaps are therefore confirmed, not provisional — a complete Article 28 DPA still needs to be produced.
3. **DPF register check — RESOLVED 2026-05-21.** The register UI is a JavaScript SPA, but its backing data API was queried directly (snapshot dated 2026-05-21): Twilio Inc. (OrgId 5394) + Google LLC (OrgId 5780) confirmed ACTIVE DPF participants; Vapi, Anthropic and xAI confirmed absent from the register. No longer a limitation.
4. **Secondary sources** (law-firm notes, Citizens Information, CCPC) corroborate the primary statutes but are not themselves authority. The five most load-bearing URLs were independently re-verified this session; the remaining Irish Statute Book URLs follow the same verified ELI scheme.
5. **Case-law currency** — the penalty-doctrine position rests on *Sheehan v Breccia* [2018] IECA. The Court of Appeal noted Irish law *may* later move toward *Cavendish*; the Supreme Court had not done so as of this research. Re-check before any litigation reliance.

---

*End of matrix. Pairs with the contract pack edits applied 2026-05-21 (see §3) and `handoffs/HANDOFF-2026-05-21-04.md`.*
