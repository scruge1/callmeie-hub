# PRD — ZBook as the Doc Ops OCR / Document-Understanding Backend

Status: `REVISED 2026-05-29 — ready to dispatch (pending the hardening + acceptance gates as Phase 0/1). Adam decision RESOLVED (Option B); Codex review findings 1-17 incorporated. Body aligned to the resolved cascade (ZBook → Mistral EU → STOP, xAI removed) + revised positioning. NOT yet executed.`

### Codex pre-review verdict (2026-05-29, different-substrate touch gate — INCORPORATED)
Codex (GPT-5.4) reviewed this PRD via `codex exec --dangerously-bypass-approvals-and-sandbox < promptfile` (the MCP + arg-passing paths are broken on this Windows box — stdin-pipe + sandbox-bypass is the working invocation). Full output: `_codex-docops-review.md`. **Go/no-go: DO NOT IMPLEMENT YET** — revise around three explicit decisions first:
1. **Absolute privacy claim vs fallback availability — choose one, or make fallback opt-in per tenant.** THE killer finding: a cloud-AI fallback when the ZBook is down RE-INTRODUCES the third-party/US AI processor the product claims to avoid → the "no third-party AI processor" claim is still false on the fallback path. (Ties to the top integrity risk: no-overclaim.) Mistral-EU fallback may preserve EEA residency *only if* the account/region/DPA actually guarantee it; xAI does not.
2. **OCR ownership on ZBook-down:** retain Hetzner-CPU OCR as the fallback (no bytes leave the EU), OR accept that a cloud fallback sees document bytes. Don't leave it implicit.
3. **ZBook production-hardening baseline (before any client doc):** disk encryption (LUKS — the rig was installed UNENCRYPTED), temp-file wipe, Tailscale ACL + bearer not "enough" alone, **sandbox `docops-ocr` as untrusted-PDF processing** (parser attack surface — containerize, non-root, no write outside temp, resource limits), monitoring (health/queue-depth/fallback-rate/GPU-temp/node-offline alerts), incident runbooks.

Other findings to fold in (medium): model accuracy is overclaimed — a bake-off on invoices ≠ proven on bank statements/RCT/Gaeilge/handwritten/multi-page → build a real acceptance set with field-level precision/recall + VAT reconciliation gates BEFORE trusting it; NUM_PARALLEL=1 = serial → quantify sec/page, 8-page worst case, daily capacity, queue-depth alerts; observability/ops + a more honest rollback plan; raw-document retention + joining the prod Hetzner host to the tailnet + repositioning on "runs in Ireland on owned hardware" are hard-to-reverse → explicit owner approval, not just impl gates.

**∴ §13 decisions are SUPERSEDED by the above 3 + the medium items.**

### Adam decision RESOLVED 2026-05-29 — Option B
- **Fallback = Mistral Small (EU/France), NOT a US/cloud-AI and NOT OCR-only.** Cascade: **ZBook qwen3.5:9b (own hardware) → Mistral Small EU → [no further AI fallback].** **xAI removed entirely** from the pipeline + DPA.
- **Positioning claim revised** to the honest, defensible form: *"AI runs on hardware we own in Ireland, with an EU-sovereign fallback (Mistral, France) — no data ever leaves the EU, no US/third-country processors."* Drop the absolute "no third-party AI processor" phrasing (Mistral is an EU third-party). Update live site / POSITIONING / DPA Schedule B+C accordingly.
- **Codex hardening baseline is MANDATORY before any client doc:** LUKS disk encryption on the ZBook (it was installed UNENCRYPTED — this is now a blocker), temp-file wipe, sandbox `docops-ocr` as untrusted-PDF processing (containerized, non-root, no write outside temp, resource limits), Mistral DPA confirming EU-only processing, monitoring (health/queue-depth/fallback-rate/GPU-temp/node-offline), incident runbooks.
- **Model trust gate:** build a real acceptance set (bank statements / RCT / Gaeilge / handwritten / multi-page) with field-level precision/recall + VAT reconciliation BEFORE trusting qwen3.5:9b for financial extraction — a bake-off on invoices is insufficient.
- **Status → REVISE per above, then ready-to-dispatch.** A revision worker is rewriting the cascade (§2/§4), positioning, and adding hardening/acceptance/observability/honest-rollback sections.
Date: 2026-05-29
Author: Claude Opus 4.8 (1M ctx) — research-then-PRD pass per behavior-contract.md.
Path note: written to `callmeie-hub/PRD-DOCOPS-ZBOOK-OCR-BACKEND-2026-05-29.md` (the callmeie-hub dir exists; this is the right home — it is the CallMeIE product hub, and the OCR backend is a Doc Ops product concern, not an Image-Ledger concern).

> **Scope boundary (read first):** This PRD owns the **Doc Ops application pipeline** — how Doc Ops USES the ZBook OCR/VL node. It does **NOT** specify infrastructure (Tailscale reachability for `cax21`, Docker placement, shared mounts, process offload). Infra is owned by **`C:\Users\a33_s\Desktop\claude MCPs\New repos\PRD-ZBOOK-CONSOLIDATION-2026-05-29.md`** (authored in parallel). Where this PRD describes the cax21↔ZBook Tailscale bridge (§5/§6 Phase 1), treat it as the *application's reachability requirement*; defer the canonical infra mechanism to the consolidation PRD.
>
> **Shared-node note (consistency with the Image Ledger):** the ZBook OCR/VL node this PRD calls — **RapidOCR (CPU) + qwen3.5:9b (GPU), which run in parallel with zero contention** (16 idle cores + 8GB GPU per the runbook) — is the **same physical node** the Image Ledger vision pipeline uses (`Image Intelligence Ledger\PRD-VISION-REARCH-2026-05-29.md`). Doc Ops fronts it with its own auth wrapper (`docops-ocr`), but the model picks, the moondream ban, and the CPU/GPU-parallel discipline are shared across both application PRDs. Both depend on the consolidation PRD for infra.

Companion / parent docs (read these before executing — they are the ground truth this PRD sits on top of):

- **Rig runbook (canonical node card):** `C:\Users\a33_s\Desktop\claude MCPs\New repos\ZBOOK-LAB-RIG-RUNBOOK.md` — pop-os @ `100.78.148.106` (Tailscale, user `firstlast`), Ollama `:11434` (tailscale0-only), vision default `qwen3.5:9b`, moondream BANNED, `MAX_LOADED_MODELS=1`, small parser `qwen2.5:3b`. The single source for how to reach + drive the node.
- **Infra owner (Tailscale/Docker/mounts/offload):** `C:\Users\a33_s\Desktop\claude MCPs\New repos\PRD-ZBOOK-CONSOLIDATION-2026-05-29.md` — owns cax21 tailnet join, Docker placement, shared mounts, process offload. This PRD references it; it does not re-specify infra.
- **Sibling application PRD (same node):** `C:\Users\a33_s\Desktop\Image Intelligence Ledger\PRD-VISION-REARCH-2026-05-29.md` — the Image Ledger's use of the same RapidOCR-CPU + qwen3.5:9b-GPU node. Keep model picks + moondream ban consistent with it.
- **Bake-off verdict:** `C:\Users\a33_s\Desktop\Image Intelligence Ledger\indexes\VISION-BAKEOFF-2026-05-29.md` — config D (qwen3.5:9b solo) won; moondream fabricates.
- **ZBook rig PRD (the machine this builds on):** `C:\Users\a33_s\Desktop\Image Intelligence Ledger\PRD-ZBOOK-LAB-RIG-2026-05-29.md` — deployed 2026-05-29, G2+G5+G6 passed, remote GPU inference live. Optimization report sibling: `ZBOOK-LAB-RIG-OPTIMIZATION-2026-05-29.md` (same folder).
- **What Doc Ops actually is + sells:** `C:\Users\a33_s\Desktop\claude MCPs\New repos\DOC-OPS-AUDIT-2026-05-20\01-STATED-OFFERING.md`
- **What Doc Ops actually IS, in code:** `DOC-OPS-AUDIT-2026-05-20\02-ACTUAL-IMPLEMENTATION.md` (the load-bearing reality doc — pipeline diagram + 14 loss-risk points)
- **Prior architecture intent / pivots:** `DOC-OPS-AUDIT-2026-05-20\03-CLAUDE-MEM-INTENT-VS-REALITY.md`
- **Stack freshness (what NOT to change):** `DOC-OPS-AUDIT-2026-05-20\11-STACK-FRESHNESS-AUDIT.md`
- **Infra source of truth:** `C:\Users\a33_s\Desktop\claude MCPs\New repos\owl-studio-website-directions\INFRA.md` §14 (Doc Ops), and the callmeie-fix mirror `C:\Users\a33_s\Desktop\callmeie-fix\INFRA.md`.
- **Pricing / fulfilment:** `owl-studio-website-directions\PRICING-SSOT.md` §3 + `PDR-CLIENT-FULFILLMENT.md`.
- **Remote-control wrapper for the ZBook:** `C:\Users\a33_s\.claude\scripts\zbook.ps1` (functions `Invoke-Zbook`, `Start-ZbookJob`, `Get-ZbookJob`).

---

## 0. Last-discussion claude-mem citations (explicit prior intent vs inference)

Searched `~/.claude-mem/claude-mem.db` (FTS5, 22,737 obs, window to 2026-05-17) on 2026-05-29. **The intent to run Doc Ops OCR/verification on the ZBook is EXPLICIT prior intent, not my invention.** Citations:

| Obs | Date | What was explicitly said | Confidence this is real intent |
|---|---|---|---|
| **18507** | 2026-05-03 | "OCR Tool Stack Architecture Decision … final agentic image recognition layer will be powered by either the cheapest available frontier model **or a locally-hosted model on the zbook** … local deployment for maximum capability and data privacy." | EXPLICIT |
| **18509** | 2026-05-03 | OSS ensemble + "verification layer will use either cheap frontier API models … **or a local model on the ZBook**." | EXPLICIT |
| **18520** | 2026-05-03 | OSS ensemble OCR (PaddleOCR-VL + PP-StructureV3 + Tesseract 5) + Mistral Pixtral EU verifier. **"Eliminate all paid OCR sub-processors."** 10-30× cost cut, 39%→75% margin. "Production deployment on Hetzner AX52 dedicated CPU; **GPU upgrade path deferred until volume exceeds 8,000 docs/month.**" | EXPLICIT (note the deferral) |
| **18524** | 2026-05-03 | ZBook 8GB RTX "can comfortably run the entire proposed stack locally": PaddleOCR-VL FP16 (~2GB), **Qwen2.5-VL-7B Q4 (~4-5GB, primary agentic verifier candidate)**, Tesseract 5, PP-StructureV3. BUT: **"Production architecture remains Hetzner AX52 dedicated CPU for 24/7 serving; ZBook role clarified as development workstation, NOT production server."** | EXPLICIT — and the explicit constraint this PRD must consciously override |
| **18585** | 2026-05-03 | D15/D16 LOCKED: "free local **Qwen2.5-VL-7B Q4** as primary in dev/eval phase, falling back to paid **Mistral Small 3.1** (~€0.001/doc, FR/EU sovereignty) when local quality drops below threshold," optional Gemini Flash cross-check. "Cheapest tier meeting per-doc accuracy threshold wins." | EXPLICIT routing rule |
| **20362 / 20366** | 2026-05-08 | DPA Schedule B: "xAI LLM provider **may be replaced by self-hosted Ollama for clients requiring no-third-country processing.**" Only post-OCR extracted text (not original PDF) currently routed to xAI. | EXPLICIT — the legal hook for self-hosting |
| **22240 / 22209** | 2026-05-15 | Two-box local-AI workstation PDR: heavy reasoning incl. Document Ops on a future Mac-Studio-class box; **gated to 8-12 paying customers / Priming Grant.** "Validate OSS stack on existing hardware as parallel test line" until then. | EXPLICIT — the ZBook is the "existing hardware parallel test line" |

### The one honest tension this PRD must resolve up-front (READ THIS)

Prior intent (18524, 18520, 22240) said **ZBook = dev/eval workstation, NOT production server**; production OCR stays on Hetzner CPU until 8,000 docs/mo or 8-12 customers. **This PRD is asked to make the ZBook the _main_ OCR backend NOW.** That is a genuine status change driven by two facts that did not hold when those decisions were made:

1. The ZBook is now **deployed 24/7, headless, Tailscale-reachable, GPU-tuned** (2026-05-29) — it was a not-yet-deployed laptop in May. The "dev workstation" framing assumed it was Adam's daily-driver laptop, not a 24/7 rig.
2. Doc Ops is **pre-revenue, zero paying customers** (obs 21466). There is no production SLA to protect yet. The cost of "single home laptop is fragile" is near-zero today and rises with each customer.

**∴ The honest synthesis:** make the ZBook the **primary OCR/VL compute** for Doc Ops _now_, behind an **EU-sovereign fallback (Mistral Small, France)** (so a ZBook outage degrades, never drops), and treat this as the "validate OSS stack on existing hardware" line from 22240 — promoted from dev to primary-with-fallback because deployment + zero-SLA make it safe. This does NOT contradict the Mac-Studio two-box plan; it _is_ the parallel test line, now load-bearing. When volume crosses the 22240 threshold, the Mac Studio replaces the ZBook as primary and the ZBook reverts to dev/eval. This PRD's architecture is forward-compatible with that swap (the backend talks to an OCR _endpoint_, not to "the ZBook" specifically).

> **OCR-ownership on ZBook-down (Codex #2 — RESOLVED).** The ZBook owns BOTH deterministic OCR (RapidOCR) AND VL understanding (qwen3.5:9b). When the ZBook is unreachable, **the Hetzner-CPU OCR ladder (`extractor.py`: pdfplumber → pypdfium2 → Tesseract + RapidOCR) is retained as the local OCR fallback** — it never left the box. The cloud fallback (Mistral EU) then receives **post-OCR text only**, never original document bytes. This closes Codex's "if ZBook owns OCR, who OCRs on fallback?" gap: OCR is always available locally (ZBook primary, Hetzner-CPU local fallback); only the *understanding/normalisation* layer escalates to Mistral EU, and only as text. No original PDF bytes are ever sent to any cloud processor.

This tension belongs in `New repos/TENSION-LEDGER.md` — see §13 decision 1.

---

## 1. Real Goal (not the literal ask)

Literal ask: "stand up the ZBook as the main OCR backend for Doc Ops."

Real goal: **Doc Ops processes client documents on hardware Adam physically owns, in Ireland, with an EU-sovereign fallback (Mistral, France) when that hardware is down — so no data ever leaves the EU and no US/third-country processor touches client documents — while staying reliable enough that a home-laptop outage never loses a customer document or drops the service.**

The wedge that makes Doc Ops worth more than Klippa/Dext (per `POSITIONING.md` + live site) is **"open-source you can audit, EU-resident, primary processing on owned Irish hardware."** Today the code half-honours this: OCR (Tesseract+RapidOCR) runs on Hetzner CPU, but field-normalisation routes post-OCR _text_ to **xAI Grok (US, under DPF)** — a third-country, third-party AI processor (obs 20315: "DPA Schedules B and C omit xAI despite production use"). The ZBook closes that gap: **both OCR and VL/LLM understanding run on Adam's GPU in Ireland**, with the only fallback being an EU-sovereign processor (Mistral, France) — **xAI is removed entirely from the pipeline.** So no client-document data ever leaves the EU. That is the real goal — the privacy claim becomes honestly defensible, the margin goes to ~100% on compute, and the "you can audit it" wedge gets a physical answer ("it runs on a GPU in Ireland you can come look at").

> **Positioning claim — canonical wording (use this verbatim everywhere; Codex #1/#10).** *"AI runs on hardware we own in Ireland, with an EU-sovereign fallback (Mistral, France) — no data leaves the EU, no US/third-country processors."* **Do NOT use the absolute "no third-party AI processor" phrasing** — Mistral is an EU third-party processor, so the absolute is false. The honest, defensible claim names the EU third-party fallback explicitly. **Dependency (not in-scope here — flag for the sibling/owner track):** the live site, `POSITIONING.md`, and DPA Schedule B+C must all be updated to this exact wording and to remove xAI; see §4.3 + Phase 4 + §9.

Secondary real goal: add the **VL document-understanding layer** that the current pipeline lacks. Today's pipeline is OCR→regex/LLM-JSON. The ZBook bake-off (2026-05-29) proved **qwen3.5:9b** gives accurate layout + semantic understanding that RapidOCR alone cannot (RapidOCR = deterministic exact text; VL = "what kind of doc is this, which number is the VAT total, is this an RCT invoice"). 60/30/10: deterministic OCR first, VL only where judgement is needed.

---

## 2. Reference-Adapt-Render Anchors

| What we do | Reference (proven, citable) | What we adapt |
|---|---|---|
| Two-machine OCR topology (Hetzner backend ↔ home GPU) | The ZBook rig PRD already proved the exact pattern: primary issues commands, ZBook serves models over Tailscale, ports firewalled to `tailscale0`. `Invoke-Zbook` + remote `/api/generate` round-trip PASSED 2026-05-29 (G5). | Swap "primary workstation" for "Hetzner `document-ops-portal` container" as the client. Same Tailscale mesh, same HTTP-to-Ollama call, different caller. |
| OCR engine ladder | Already shipped + proven in `document-ops-portal/app/services/extractor.py` (pdfplumber → pypdfium2 render → Tesseract + RapidOCR voter). RapidOCR 0.97-0.98 conf confirmed on ZBook bake-off. | Keep the deterministic text layer **unchanged**. Add a VL understanding call (qwen3.5:9b on ZBook) as a new stage, not a replacement. Per stack-freshness audit: "ADD, do not replace." |
| VL model choice | ZBook controlled bake-off 2026-05-29: **moondream:1.8b HALLUCINATES — banned.** **qwen3.5:9b accurate + richest.** Aligns with prior intent obs 18585 (Qwen2.5-VL-7B Q4 primary). | Use `qwen3.5:9b` (already pulled on ZBook) as the VL/understanding model. `qwen2.5vl:7b` is the documented-intent fallback if 9b is too slow under load (also already pulled). |
| Fallback when ZBook down | Existing `llm_extractor.py` already has a provider cascade (xAI → Anthropic → Ollama → static). The pattern exists; we re-order it AND strip xAI. | Re-order + prune cascade to **ZBook-Ollama primary → Hetzner-CPU OCR (local, bytes never leave) → Mistral Small EU on post-OCR text (obs 18585 fallback) → STOP. xAI REMOVED entirely** (Adam Option B). EU-only cascade keeps every byte and every escalation in-EEA; there is no US/third-country leg. |
| Async queue (don't OCR in the request thread) | Loss-risk #2 in the actual-implementation audit: OCR runs synchronously in the uvicorn worker → timeout → 502 → lost doc. Standard fix = a job queue. | Smallest viable: a DB-backed work table + a poller, OR `arq` (Redis-less option exists). Avoid Celery (audit says no Celery/RQ/Arq in-process today — keep it light). See §6 Phase 3. |
| Authenticated ZBook OCR endpoint | The ZBook already exposes Ollama on `0.0.0.0:11434` firewalled to `tailscale0`. | Put a thin **FastAPI OCR service** (`docops-ocr`) in front of Ollama+RapidOCR on the ZBook, bearer-token auth, so the Hetzner box calls one stable contract, not raw Ollama. |

---

## 3. Ground-truth facts the executing instance must treat as given (do not re-derive)

### 3.1 ZBook (the OCR rig) — deployed 2026-05-29

- HP ZBook Studio G8, **NVIDIA RTX 3070 Laptop GPU, 8GB VRAM, Ampere CC 8.6**, 32GB RAM, 1TB SSD. **Pop!_OS 24.04, headless, 24/7, always plugged in.**
- Reachable from the main Windows workstation over **Tailscale**: host `pop-os` @ **`100.78.148.106`**, SSH user **`firstlast`** (NOPASSWD sudo), Tailscale SSH enabled. NoMachine remote desktop on `:4000`.
- **Ollama** running, bound `0.0.0.0:11434`, **firewalled to `tailscale0` ONLY (ufw)**. Models present: `moondream:1.8b` (BANNED — hallucinates), `qwen2.5:3b`, `llama3.1:8b`, **`qwen2.5vl:7b`**, **`qwen3.5:9b`** (multimodal, primary VL pick). GPU persistence via systemd. llama.cpp (Vulkan) at `~/lab-rig/llama-cpp`.
- Ollama 8GB-tuned: `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`, `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_MAX_LOADED_MODELS=1`. **NUM_PARALLEL=1 + MAX_LOADED=1 means the ZBook serves one model, one request at a time** — this is a hard concurrency constraint the queue design must respect (§6 Phase 3).
- Remote-control wrapper: `C:\Users\a33_s\.claude\scripts\zbook.ps1`.
- **Bake-off finding (load-bearing):** moondream hallucinates → never use for any assessment/OCR. qwen3.5:9b solo, one call = accurate + richest. RapidOCR = deterministic exact text (0.97-0.98). VL adds layout/semantic understanding. 60/30/10: deterministic first, VL where judgement is needed.

### 3.2 Doc Ops backend (the OCR client) — per audit 02 + INFRA §14

- Runs as Docker service **`document-ops-portal`** (uuid `rs0jyp5cj24hutaxijacye6r`) on **Hetzner Cloud `cax21`, Nuremberg DE, `178.104.205.255`, Coolify-managed.** **This box is NOT currently on the Tailscale tailnet** — solving that reachability is the core architectural decision (§5).
- FastAPI 0.115+ / Python 3.13 / single uvicorn process / Jinja2 + HTMX / Postgres 16 (Coolify-managed, DB `document_ops_portal`, alembic head `0009`).
- OCR today: **`app/services/extractor.py`** — pdfplumber → pypdfium2 render → **Tesseract + RapidOCR ensemble**, all **synchronous in the request thread**. Field normalisation: **`app/services/llm_extractor.py`** — xAI Grok primary → Anthropic → Ollama → static fallback.
- The customer upload route is **`POST /portal/{slug}/extract`** (`app/routes/tenant.py:272`). **Original PDF bytes are dropped after OCR** (`source_path="memory-only"`); nothing is uploaded to the `callmeie-corpus` Hetzner Object Storage bucket (loss-risk #3, CRITICAL).
- **Known gaps the executing instance must NOT assume are fixed** (audit 02/03): no email-inbox ingest, no HTML upload widget, CSV-export object never written, `boto3` missing from `pyproject.toml` (lazy-imported, 503s silently), Stripe billing-meter not wired. **These are out of scope for THIS PRD** (they are the sibling fix-track) — but the executing instance must not break them and must not claim them done.
- Vault creds: `~/.claude/routes/.env` (SMTP, Stripe, `SESSION_SIGNING_KEY`, Hetzner Object Storage, Label Studio). The new ZBook bearer token goes here too (§6 Phase 2).

### 3.3 Document types Doc Ops handles (per `01-STATED-OFFERING.md` + obs 18712)

Invoices, credit notes, supplier statements, delivery dockets, BOL/CMR, customs declarations, receipts, quotes, handwritten docs, mixed-VAT invoices, **RCT reverse-charge invoices**, utility bills, bank statements. **IE-specific quirks the VL layer must handle:** RCT principal-contractor stamp, per-letter supermarket VAT (Tesco/Dunnes/SuperValu A/B/Z codes), medical-exempt, FX intra-community, Gaeilge headers. Limits stated on site: **≤10 MB, ≤8 pages** (code says `MAX_PAGES=50` / 25 MB on the paid route — a contradiction to note, not fix here).

---

## 4. Current vs target architecture

### 4.1 Current (as built, 2026-05-29)

```
[Customer browser] --POST /portal/{slug}/extract (multipart PDF)--> [Hetzner cax21 uvicorn worker]
                                                                       │ (synchronous, in request thread)
                                                                       ├─ pdfplumber / pypdfium2 + Tesseract + RapidOCR   (Hetzner CPU)
                                                                       ├─ llm_extractor: xAI Grok (US, DPF)  ◄── third-country AI processor
                                                                       └─ INSERT Extraction(payload, source_path="memory-only")  ← bytes dropped
```

Privacy reality: post-OCR text leaves the EU to xAI. Reliability reality: long OCR blocks the worker → 502 → lost doc. Original-bytes reality: gone, no replay, fails VATCA s.84(3) provenance claim.

### 4.2 Target (this PRD)

```
[Customer upload] --> [Hetzner cax21]
                         ├─ enqueue job in Postgres `ocr_jobs` (status=queued)   ← returns fast, no worker block
                         └─ store original PDF to Hetzner Object Storage callmeie-corpus/{tenant}/raw/  ← closes loss-risk #3
                                          │
        [poller / arq worker on cax21] --pull queued job--> calls OCR endpoint over Tailscale:
                                          │
   Tailscale mesh (cax21 joined) ── HTTPS bearer-auth ──► [ZBook pop-os 100.78.148.106]
                                          │                   docops-ocr FastAPI (:8088, tailscale0 only)
                                          │                     ├─ RapidOCR  (deterministic exact text, conf 0.97-0.98)
                                          │                     └─ qwen3.5:9b via Ollama (layout + semantic understanding)
                                          │                   returns {ocr_text, fields, confidences, doc_type, vl_notes}
                                          ▼
   IF ZBook unreachable / timeout / job retried N× ─► OCR FALLBACK: Hetzner-CPU ladder (pdfplumber→Tesseract+RapidOCR, bytes stay on cax21/EU)
                                          │            then UNDERSTANDING FALLBACK: Mistral Small 3.1 (EU, France, La Plateforme) on post-OCR TEXT ONLY
                                          │            then STOP (no further AI fallback — xAI REMOVED). Permanent fail → status=failed, bytes retained for replay.
                                          │
                         └─ write Extraction row + gate + (optional) corrections-queue
```

Privacy: with ZBook primary, **nothing leaves Adam's house**. The entire fallback cascade is EU-only — OCR falls back to Hetzner CPU (EU, original bytes never leave), and the understanding layer falls back to Mistral (France, EEA) on **post-OCR text only**. **xAI is removed entirely** — there is no US/third-country leg anywhere in the pipeline (Adam Option B; Codex #1/#2). Reliability: queue + retry + EU fallback means a ZBook outage degrades latency, never drops a doc and never breaks the EU-residency claim.

### 4.3 Positioning / legal dependency (out-of-scope here — flag, do not do)

This architecture change makes the canonical positioning claim (§1) true. The matching copy/legal updates are a **dependency, not in-scope for this PRD's executing instance to author**:
- **Live site + `POSITIONING.md`** → replace any "no third-party AI processor" absolute with the §1 canonical wording.
- **DPA Schedule B + Schedule C** → remove xAI as a (sub)processor entirely; name the processors as: self-hosted OCR/VL on owned hardware in Ireland (primary), Hetzner-CPU OCR (EU local fallback), Mistral SAS / La Plateforme (France, EU — understanding fallback, post-OCR text only). See Phase 4 + §9. **Adam/solicitor must review + approve before any legal/marketing publish (G4).**

---

## 5. THE core architectural decision — how Hetzner reaches the home ZBook securely

Three viable options. **This PRD recommends Option A.** The executing instance must confirm Adam's choice (§13 decision 2) before Phase 1.

| Option | How | Pros | Cons | Verdict |
|---|---|---|---|---|
| **A. Tailscale on the Hetzner box (RECOMMENDED)** | Install Tailscale on `cax21`, join the same tailnet as `pop-os`. cax21 calls `http://100.78.148.106:8088` (or MagicDNS `pop-os`). ZBook `docops-ocr` stays firewalled to `tailscale0`. | Zero public exposure of the ZBook. Reuses the exact proven mesh from the rig PRD. No inbound ports opened on the home router. Encrypted by WireGuard. ~1h setup. | cax21 now has a tailnet identity (ACL it tightly — see §6 Phase 1). Tailscale must run inside/alongside the Coolify host (host-level install, not in the app container). | **CHOSEN** — least public surface, proven pattern, cheapest. |
| **B. Outbound-pull queue (no inbound at all)** | ZBook **polls** Hetzner for queued jobs over Tailscale or HTTPS, pulls the PDF, processes, posts result back. Hetzner never initiates a connection to the home network. | Most defensive — home network never accepts inbound, even on tailnet. Survives home-IP changes trivially. | More moving parts (a poller on the ZBook + a job-claim protocol + auth both directions). Higher latency. | **STRONG ALTERNATIVE** if Adam wants zero inbound to home. Compose with A: run the poller _over_ Tailscale. |
| **C. Public authenticated API on ZBook** | Expose `docops-ocr` on a public port / via Cloudflare Tunnel, bearer + mTLS. | Works without Tailscale on cax21. | Puts a home GPU box on the public internet — directly against the rig PRD non-goal "Not exposing inference ports to the public internet." Largest attack surface for client documents. | **REJECTED** — violates the privacy real-goal and the rig PRD's explicit non-goal. |

**Recommended composite:** Option A (Tailscale on cax21) as transport + Option B's pull-discipline for the _job_ flow (the cax21 worker pulls jobs from its own Postgres and pushes to the ZBook; the ZBook never reaches back into Hetzner except to return the HTTP response). This keeps the data-flow direction one-way (Hetzner → ZBook → response) and the home box inbound-only on the tailnet.

---

## 5A. Hardening baseline — HARD GATE before ANY client document (Codex #3/#5/#8/#9/#17)

> **This entire section is a blocking precondition.** No client (or real-client) document may flow through the ZBook path until every item here is verified by runtime/filesystem evidence, not assumption. Codex's #3 ("a residential laptop is not automatically a better regulated processing environment") is the load-bearing correction: moving client financial PII into a home environment introduces physical-security, endpoint-hardening, retention, and incident-response obligations that Hetzner-managed infra provided by default. These are NOT optional polish — they are the cost of the privacy win.

### 5A.1 Disk encryption — LUKS (HARD BLOCKER, Codex #3)

The ZBook was **installed UNENCRYPTED** (Pop!_OS, no LUKS — confirmed against the rig PRD). A residential, headless, always-on box holding client financial documents on an unencrypted disk is unacceptable: theft, service, repair, resale, or seizure exposes every cached byte. **This requires an explicit reinstall-or-encrypt decision and is a Phase 0 blocker:**
- **Option 1 — reinstall with LUKS full-disk encryption** (cleanest; requires re-running the rig setup; the only option that encrypts the existing system partition + swap).
- **Option 2 — in-place encrypt** the data/working partition the OCR service uses (LUKS on a dedicated volume) if a full reinstall is too costly — but the root partition, swap, and any temp location the OCR pipeline touches MUST be on encrypted volumes.
- Either way: **swap must be encrypted** (document bytes can page out), and the working/temp directory `docops-ocr` uses must be on a LUKS volume.
- **Verify:** `lsblk -o NAME,FSTYPE,MOUNTPOINT && cryptsetup status <device>` shows the root + swap + working dir on `crypto_LUKS`. Owner-approval required for the reinstall path (it is hard-to-reverse — see §11A).

### 5A.2 Temp-file wipe after each doc (Codex #3/#17)

§7's "process in memory" is insufficient on its own — PDF render / OCR libraries (pypdfium2, RapidOCR onnxruntime, any pdf→image step) routinely spill temp images, model scratch, and caches to disk. Required:
- A per-doc temp dir under the LUKS working volume, created per job, **shredded (`shred`/secure-unlink) on completion AND on failure** (try/finally).
- Explicitly disable/redirect library temp spill into that dir (`TMPDIR`, library cache env).
- No browser downloads, no crash dumps, no core dumps retaining bytes (`ulimit -c 0`, disable systemd-coredump for the service).
- Confirm Ollama, systemd-journal, and the `docops-ocr` app logs retain **no** document text/bytes (Codex #3 enumerated list: temp files, OCR caches, swap, crash dumps, journal logs, Ollama logs).
- **Tested wipe procedure** for both normal completion and failed jobs — a documented, runnable script, verified by `find <workdir> -type f` returning empty after a test run.

### 5A.3 Sandbox `docops-ocr` as UNTRUSTED-PDF processing (Codex #17 — the parser attack surface)

`docops-ocr` accepts hostile PDFs/images from a production web app over the network. PDF/image/OCR parser stacks have a large, repeatedly-CVE'd attack surface. Treat it as an untrusted-document sandbox, NOT a trusted internal microservice:
- **Containerize** the service (Docker/podman on the ZBook); run as a **non-root service user** with minimal filesystem permissions.
- **No write access outside the per-doc temp dir** (read-only root FS; tmpfs or LUKS-backed scratch only).
- **seccomp / AppArmor profile** where practical; drop all unneeded capabilities.
- **Resource limits** (memory, CPU, PIDs) so a malicious doc cannot OOM/fork-bomb the box; **strict request timeouts** per doc.
- **No shelling out with unsanitized paths**; content-type + magic-byte validation on input; **request size + page-count limits enforced at the ZBook endpoint** (≤10 MB / ≤8 pages per the stated product limit — reject oversized before parsing).
- Per-request `doc_id` validation; **rate limiting** at the endpoint.
- GPU access is the one capability the container must retain (Ollama call); everything else is denied.

### 5A.4 Network/auth hardening — Tailscale ACL + bearer is NOT "enough" alone (Codex #8/#9)

The §5/§7 ACL + bearer is directionally right but under-specified. Required additions before client docs:
- **Default-deny tailnet policy confirmed** (not just an allow rule added on top of an implicit-allow base).
- **Source = a locked tagged node** (`tag:docops-backend` with `tagOwners` restricted), NOT a user-owned mutable device identity; **destination = a tagged service identity** where possible, not only a hard-coded `100.78.148.106`.
- **Key expiry, device approval, and a node-offboarding runbook** for cax21's tailnet key.
- **Tailscale SSH on the ZBook disabled or separately constrained** (it currently allows broad access); confirm **no subnet routing** lets cax21 reach the home LAN.
- **Confirm no other tailnet device can reach `:8088`**, and that cax21 **cannot** reach raw Ollama `:11434`, SSH, or NoMachine `:4000` (test from cax21).
- **The ZBook's `NOPASSWD sudo` + 0.0.0.0-bound Ollama is a broad local attack surface** for a box receiving client financial docs — review and tighten (bind Ollama to the tailscale IP, not 0.0.0.0; reconsider NOPASSWD for the service user).
- **Bearer-token = one factor, treat as compromisable.** A token leaked via Coolify env / logs / shell history / `.env` / compromised cax21 lets an attacker submit arbitrary PDFs. Mitigate with the ACL + size/page/content-type limits + parser sandbox (5A.3) so a stolen token alone cannot exfiltrate or exploit. Document a **token rotation + revocation runbook**; consider mTLS or Tailscale-identity checks if available.

### 5A.5 Mistral DPA — confirm EU-only processing (Codex #1/#10)

Before Mistral is wired as the understanding fallback, **obtain/confirm the Mistral (La Plateforme) DPA + region settings guarantee EU-only (France/EEA) processing** of the post-OCR text — EU residency is only real if the account/region/contract actually guarantee it. Record Mistral SAS as a named EU subprocessor in the RoPA/DPA (Phase 4). If the DPA cannot guarantee EU-only, the fallback decision returns to Adam (EU-only-refuse vs accept).

### 5A.6 RoPA / processing-location disclosure (Codex #3)

The ZBook becomes a **production processing location** and must be treated as one:
- List the ZBook (owned hardware, Ireland) as a processing environment in the RoPA/DPA; disclose the processing **country/region** (Ireland) — not necessarily the home address, but at minimum the jurisdiction.
- Document the answers to: stolen/serviced/sold/repaired laptop procedure (ties to 5A.1 LUKS + 5A.2 wipe); who has physical + logical access; patching cadence for the headless box.

**Press-back gate G-HARD (runtime + Adam):** 5A.1 LUKS verified by `lsblk`/`cryptsetup`; 5A.2 wipe procedure runs + `find` shows empty; 5A.3 service runs containerized non-root with limits (inspect runtime); 5A.4 ACL + reachability negatives proven from cax21; 5A.5 Mistral DPA confirmed; 5A.6 RoPA entry drafted + Adam-approved. **No real client document touches the ZBook until G-HARD passes.**

---

## 5B. Model trust / acceptance set — GATE before trusting qwen3.5:9b for financial extraction (Codex #12)

> **A bake-off on sample invoices is NOT sufficient to trust a model for financial extraction.** The 2026-05-29 bake-off proved qwen3.5:9b > moondream on a narrow invoice sample. It did NOT prove production accuracy across the full document spread Doc Ops handles (§3.3). Wrong VAT totals or misread IBANs on a customer's books is a trust-ending failure. Before qwen3.5:9b is trusted for live financial extraction, build a **labelled acceptance set with measurable gates.**

### 5B.1 The labelled acceptance set (must span the real spread)

Assemble a labelled (ground-truth) set covering, at minimum, each hard case:
- **Bank statements** (table extraction — rows, balances, running totals).
- **RCT reverse-charge invoices** (principal-contractor stamp, reverse-charge VAT handling).
- **Gaeilge headers** (Irish-language field labels).
- **Per-letter supermarket VAT** (Tesco/Dunnes/SuperValu A/B/Z code → rate mapping).
- **Handwritten docs** (expected failure mode — must be *detected* as low-confidence, not silently fabricated).
- **Multi-page PDFs** (8-page worst case; cross-page totals).
- Plus the common path: standard invoices, credit notes, receipts, mixed-VAT invoices.

Use sanitized/synthetic or public-domain fixtures for the labelled set — **never real client docs without opt-in** (ties to §5A privacy + Codex #11 shadow-mode).

### 5B.2 Field-level acceptance gates (must pass to declare qwen3.5:9b trusted)

- **Field-level precision/recall** per extracted field (vendor, vat_no, total, vat_breakdown, date, iban, rct_principal_contractor) — set a numeric threshold per field before go-live; financial fields (total, vat_breakdown, iban) get the strictest gate.
- **Totals/VAT reconciliation gate** — extracted line items + VAT must reconcile to the stated total within tolerance; a doc that fails reconciliation is auto-flagged for review, never auto-accepted.
- **Confidence calibration** — low model confidence must correlate with actual error (so the review queue catches the right docs); handwritten docs must route to review, not fabricate.
- **Reviewer-override flow** — a human can correct any extracted field, and the correction is captured (feeds the existing corrections queue).

### 5B.3 Regression set before ANY model swap

Freeze the acceptance set as a **regression suite.** Any model change — qwen3.5:9b → qwen2.5vl:7b in-rig fallback swap, a future model upgrade, or the Mac-Studio cutover (22240) — must re-pass the regression gates before it goes live. A config-flag model swap (§6 Phase 2) does NOT bypass this.

**Press-back gate G-ACCEPT (runtime metrics):** acceptance set built + labelled; precision/recall + reconciliation gates computed and meeting thresholds on the full spread (not just invoices); handwritten/low-conf docs proven to route to review; regression suite frozen. **qwen3.5:9b is not trusted for live financial extraction until G-ACCEPT passes** (it may still run in shadow against sanitized fixtures before then). This gate sits in Phase 5 before primary cutover.

---

## 6. Method: phased deployment

```
P0  →  Discovery + HARDENING BASELINE (§5A) verify: LUKS, temp-wipe, sandbox, ACL, Mistral DPA, RoPA   (autonomous probe + Adam decisions; G-HARD)
P1  →  Tailnet bridge: Tailscale on cax21, ACL-locked to the ZBook OCR port  (Adam-keyboard auth, ~45 min)
P2  →  docops-ocr service on the ZBook (RapidOCR + qwen3.5:9b, containerized non-root, bearer auth)   (autonomous, ~90 min)
P3  →  Async queue + retry + EU-only fallback (Hetzner-CPU OCR → Mistral EU text, NO xAI) + async UX   (autonomous, ~3-4h)
P4  →  Original-bytes persistence + retention/DSAR policy + DPA/RoPA truth-up + positioning copy dep    (autonomous + Adam legal review)
P5  →  Model-trust ACCEPTANCE SET (§5B) + shadow (sanitized) + cutover + observability + handoff        (autonomous + Adam gate)
```

> **Phase ordering note:** §5A hardening (G-HARD) and §5B acceptance-set (G-ACCEPT) are **gates, not optional polish** — they bound when client docs may flow, not when code may be written. Build P1-P3 against fixtures freely; do not point real client traffic at the ZBook path until both gates pass.

### Phase 0 — Discovery (autonomous; do this FIRST, do not skip)

Doc Ops' exact current OCR wiring may have drifted since the 2026-05-20 audit. **Verify before changing.** Steps:

1. `git -C "C:\Users\a33_s\Desktop\claude MCPs\New repos\document-ops-portal" log --oneline -20` and read `app/services/extractor.py` + `app/services/llm_extractor.py` + `app/routes/tenant.py` (the `tenant_extract` handler). Confirm: is OCR still synchronous? Is the provider cascade still xAI-first? Is `source_path` still `"memory-only"`?
2. `ssh firstlast@100.78.148.106 'ollama list && nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu --format=csv'` — confirm models + free VRAM headroom for `docops-ocr`.
3. Confirm whether `cax21` is on the tailnet: `tailscale status` (from workstation) — does `cax21` / `178.104.205.255` appear? (Audit says NO; verify.)
4. Read `owl-studio-website-directions/INFRA.md` §14 cover-to-cover for the live Doc Ops infra contract; note the fqdn-cascade bug #6281 workaround and the rescue-daemon/corrections containers already on cax21.
5. Confirm the OCR bake-off result file exists and re-read the qwen3.5:9b-vs-moondream finding: `Image Intelligence Ledger\ZBOOK-LAB-RIG-OPTIMIZATION-2026-05-29.md`.

**Press-back gate G0:** Discovery findings written into this PRD as a `### Phase 0 findings` block (state any drift from the audit). If OCR is no longer synchronous, or cax21 is already on the tailnet, adjust later phases accordingly. Runtime is the second thing here.

### Phase 1 — Tailnet bridge (Adam-keyboard for auth)

> **Infra ownership:** the canonical mechanism for joining `cax21` to the tailnet + host-level Docker/Tailscale placement is owned by `PRD-ZBOOK-CONSOLIDATION-2026-05-29.md`. The steps below are the **Doc Ops reachability requirement** (cax21 must reach the ZBook OCR port, least-privilege ACL). If the consolidation PRD has already landed cax21 on the tailnet, skip the install and just confirm + apply the OCR-port ACL. Do not duplicate the infra build.

**Outputs:** `cax21` joined to the tailnet; ACL restricts cax21 to ONLY the ZBook OCR port; ZBook reachable from cax21.

1. On `cax21` (Coolify host, NOT inside the app container):
   ```bash
   curl -fsSL https://tailscale.com/install.sh | sh
   sudo tailscale up --ssh --hostname=cax21-docops    # Adam authenticates in browser (G1)
   tailscale status                                    # confirm cax21 + pop-os both online
   ```
2. Tailnet ACL (Tailscale admin console) — least privilege. cax21 may reach ONLY the ZBook OCR port, nothing else:
   ```jsonc
   // tailnet policy — add, do not replace existing
   "acls": [
     { "action": "accept", "src": ["tag:docops-backend"], "dst": ["100.78.148.106:8088"] }
   ],
   "tagOwners": { "tag:docops-backend": ["autogroup:admin"] }
   // tag cax21 with tag:docops-backend; it cannot reach :11434, :4000, or SSH on pop-os
   ```
   Note: the ZBook's raw Ollama `:11434` is NOT exposed to cax21 — only the `docops-ocr` wrapper `:8088` is. This means even a compromised cax21 cannot pull arbitrary models or hit Ollama directly.
3. From cax21, smoke-test reachability (after P2 ships the endpoint): `curl -sS http://100.78.148.106:8088/healthz`.

**Press-back gate G1:** Adam confirms the Tailscale auth completed + the ACL is applied (Adam review + `tailscale status` runtime output). Do not proceed to wiring the backend until cax21↔ZBook reachability is proven by a runtime `curl`.

### Phase 2 — `docops-ocr` service on the ZBook (autonomous)

**Outputs:** A small FastAPI service on the ZBook at `:8088` (bound to `tailscale0` only, ufw-denied elsewhere), bearer-token auth, that wraps RapidOCR + qwen3.5:9b behind one stable contract.

Deploy under `~/lab-rig/docops-ocr/`. Endpoint contract:

```
POST /ocr   (Authorization: Bearer <DOCOPS_OCR_TOKEN>)
  body: { "doc_id": str, "pdf_b64": str OR "image_b64": str, "hint_doc_type": str|null }
  →  {
       "doc_id": str,
       "ocr_text": str,              // RapidOCR deterministic exact text
       "ocr_confidence": float,      // 0.97-0.98 typical
       "doc_type": str,              // qwen3.5:9b classification (invoice/receipt/rct-invoice/bank-statement/...)
       "fields": { ... },            // VL-extracted candidate fields (vendor, vat_no, total, vat_breakdown, date, iban, rct_principal_contractor)
       "field_confidences": { ... },
       "vl_notes": str,              // qwen3.5:9b layout/semantic notes for the review queue
       "engine": "zbook-rapidocr+qwen3.5:9b",
       "elapsed_ms": int
     }
GET /healthz  → { "ok": true, "models": [...], "gpu_free_mb": int }
```

Implementation rules (per ground truth + 60/30/10):

- **RapidOCR runs first, always** — deterministic text layer. Already proven 0.97-0.98 conf. (RapidOCR is pip-installable on Pop; `rapidocr-onnxruntime`.)
- **qwen3.5:9b runs second**, ONE call, solo (respect `OLLAMA_NUM_PARALLEL=1` / `MAX_LOADED_MODELS=1`). It does classification + field-candidate extraction + layout notes — the judgement layer.
- **moondream is BANNED.** Do not import, call, or fall back to it. (Hallucinates — bake-off finding.)
- **qwen2.5vl:7b is the in-rig fallback** if 9b is too slow under sustained load (also already pulled). Swap is a config flag, not a code change.
- Bearer token `DOCOPS_OCR_TOKEN` (32-byte urlsafe) generated on the ZBook, stored on the ZBook env + mirrored into Hetzner `~/.claude/routes/.env` / Coolify env. **No client document text is logged** — log doc_id + elapsed + confidence only (privacy).
- ufw: `sudo ufw allow in on tailscale0 to any port 8088; sudo ufw deny in 8088` (deny on every other iface). Bind uvicorn to `100.78.148.106` (the tailscale IP), not `0.0.0.0`.
- **Containerize + run non-root with the §5A.3 sandbox** (untrusted-PDF processing): read-only root FS, LUKS-backed per-doc temp dir, seccomp/AppArmor, dropped caps (GPU retained), memory/CPU/PID + timeout limits, **size/page/content-type validation rejecting >10 MB / >8 pages / non-PDF before parsing**, rate limiting. This is mandatory, not optional — it is the parser-attack-surface control (Codex #17). The `systemd` unit supervises the container (auto-restart); GPU-persistence already on.
- **Temp-file wipe per §5A.2** — shred the per-doc temp dir on completion AND failure (try/finally); `TMPDIR` redirected into the LUKS scratch; core dumps disabled.

**Press-back gate G2 (runtime):** From the workstation over Tailscale: `Invoke-Zbook` is for SSH; for HTTP do `curl -sS -H "Authorization: Bearer <tok>" -d '{"doc_id":"t1","image_b64":"<base64 of a sample IE invoice>"}' http://100.78.148.106:8088/ocr` and verify a valid JSON with non-empty `ocr_text` + a `doc_type`. Use a **real sample invoice** from `document-ops-portal/proof-fixtures/` (or the public-domain corpus referenced in obs 18585). Runtime is the second thing. If `ocr_text` empty or `doc_type` missing → do NOT proceed.

### Phase 3 — Async queue + retry + EU-only fallback + async UX (autonomous; the reliability core)

**Outputs:** Doc Ops upload no longer OCRs in the request thread; a worker processes jobs against the ZBook with retry + EU-only fallback; the customer-facing async UX is redesigned (not just the backend).

Design (keep it light, but a real worker — see step 3 / Codex #6):

1. New alembic migration `0010_ocr_jobs`: table `ocr_jobs(id, tenant_id, doc_id, file_sha256, object_key, status[queued|processing|done|failed|fallback], attempts, engine_used, error, claimed_by, claimed_at, heartbeat_at, created_at, updated_at)`. (`claimed_by`/`heartbeat_at` support timeout-recovery + dead-letter; Codex #6.)
2. `POST /portal/{slug}/extract` change: **stop OCRing inline.** Instead — store the original PDF to `callmeie-corpus/{tenant_id}/raw/{sha256}.pdf` (this ALSO closes loss-risk #3), INSERT an `ocr_jobs` row `status=queued`, return `202 Accepted` fast. (This is the single biggest reliability win — the worker timeout class of failure disappears.)
3. **Worker = a SEPARATE process/container, NOT an in-app asyncio poller (Codex #6 — RESOLVED).** Codex flagged the in-app poller as fragile for customer-facing work: app restarts interrupt jobs, deploys kill in-flight work, double-processing risk, weak observability, long OCR calls interfere with serving. **Use a separate worker process/container** that claims jobs with Postgres **`SELECT ... FOR UPDATE SKIP LOCKED`** (not a naive `UPDATE ... RETURNING`), with a **heartbeat + timeout-recovery (re-queue stale `processing` jobs), a dead-letter state, and an admin replay path.** `arq` + a tiny Coolify Redis is acceptable if the alternative is invisible stuck jobs; a bespoke Postgres-`SKIP LOCKED` worker process is the Redis-less option — but it MUST be a separate process, not a background task inside uvicorn. (§13 #3 default updated accordingly.) The worker:
   - claims a job (`FOR UPDATE SKIP LOCKED`), sets `claimed_by` + `heartbeat_at`,
   - downloads the PDF from object storage,
   - calls `http://100.78.148.106:8088/ocr` (ZBook, primary),
   - on success → write `Extraction` row + gate + `engine_used='zbook'`,
   - on ZBook timeout/5xx/unreachable, retry up to N=3 with backoff; if still failing → **EU-ONLY fallback cascade**: (a) **Hetzner-CPU OCR** (pdfplumber → Tesseract + RapidOCR, bytes stay on cax21/EU) to recover the text, then (b) **Mistral Small 3.1 (La Plateforme, France/EU)** for understanding on **post-OCR text only** → mark `status=fallback`, flag for review. **xAI is REMOVED — there is no further AI fallback** (Adam Option B; Codex #1/#2),
   - never drops: a permanently-failing job (ZBook + Mistral both unavailable) ends `status=failed` WITH the original bytes still in object storage for replay, doc flagged.
4. Concurrency: because the ZBook serves **one request at a time** (`NUM_PARALLEL=1`), the worker processes serially or with a semaphore of 1 against the ZBook. Batch/overnight runs are fine (Doc Ops is batch-oriented per obs 18712 non-scope: "no real-time sub-second p99"). Capacity numbers in §8A.
5. Re-order + **prune** `llm_extractor.py` provider cascade to: **ZBook-Ollama (via docops-ocr) → Hetzner-CPU OCR (local) → Mistral EU (post-OCR text) → static.** **Delete the xAI provider leg** (Adam Option B) — grep to confirm no xAI code path remains reachable from the extract route.
6. **Async customer UX redesign (Codex #7 — was missing).** Changing `/extract` from synchronous-result to `202 Accepted` breaks the current portal workflow, which expects an immediate extraction result. This PRD now owns the matching UX:
   - **Job-status polling endpoint** (`GET /portal/{slug}/extract/{job_id}` → status + result when done) the HTMX UI polls.
   - **Job-status UI states** in the existing Jinja2/HTMX templates: queued / processing / done / failed / fallback(in-review) — with retry messaging and a review-state surface.
   - **Idempotency on repeated uploads** (same `file_sha256` + tenant → return existing job, don't double-enqueue).
   - **Customer notification** on completion/failure (reuse the existing SMTP path if cheap; otherwise in-portal status only).
   - Document how the existing synchronous template path is retained behind a feature flag for rollback (§11A).

**Press-back gate G3 (runtime + filesystem):** Upload a test doc through the real `/portal/{slug}/extract` route on a staging tenant; confirm (a) a `202` returns immediately + the HTMX UI shows a queued→done transition via the polling endpoint, (b) the original PDF appears in `callmeie-corpus/.../raw/`, (c) an `Extraction` row lands with `engine_used='zbook'`, (d) kill the `docops-ocr` service and re-run → confirm the job recovers text via Hetzner-CPU OCR + understanding via Mistral, writes a row (`engine_used='mistral'`), never a 502, and **never touches xAI** (grep the code path), (e) kill the worker mid-job → confirm the stale `processing` job is re-queued by timeout-recovery and completes (Codex #6). Filesystem + DB are the second thing.

### Phase 4 — Original-bytes persistence + retention policy + DPA/RoPA truth-up (autonomous + Adam legal review)

**Outputs:** loss-risk #3 closed (already done in P3 step 2 — verify); a documented retention/deletion policy for the newly-stored raw documents; DPA Schedule B + Schedule C + RoPA updated; positioning copy dependency flagged.

1. Verify P3 step 2 actually persists originals (don't assume). This is also what makes the "originals kept for Revenue audit" + VATCA s.84(3) provenance claims true.
2. **Raw-document retention policy (Codex #8 — was missing; storing raw PDFs is a major privacy design decision, not just a reliability fix).** Define + implement:
   - **Retention period** by tenant/product tier; **deletion policy** (auto-expire after the audit window) — bank statements vs invoices may differ.
   - **DSAR / right-to-erasure handling** — a tenant delete request must purge raw bytes + extractions + object-storage keys.
   - **Encryption at rest** for the `callmeie-corpus` object storage bucket; **object-key access controls** + **audit logs for reads**; **backup/replication policy** (EU-region only).
   - **Tenant-isolation tests** on the object-key namespace (`{tenant_id}/raw/...`).
   - **Confirm raw documents are NEVER sent to any fallback processor** — only post-OCR text escalates (ties to §0 OCR-ownership resolution + the Codex #2/#8 answer).
3. Update **DPA Schedule B + Schedule C + the RoPA** (`document-ops-portal` legal docs / `callmeie-hub/_internal/`): the **primary** OCR + VL processor is now **self-hosted on owned hardware in Ireland (no third party, no third country)**; EU fallback = Hetzner-CPU OCR (EU) then **Mistral SAS / La Plateforme (France, EU)** on post-OCR text only; **xAI is REMOVED as a (sub)processor entirely**; the ZBook (Ireland) is listed as a processing location (§5A.6). This is the obs 20362/20366 hook made real. **Adam/solicitor must review legal copy — do not auto-publish DPA/RoPA changes.**
4. **Positioning copy dependency (out-of-scope to author here — flag).** The live site + `POSITIONING.md` must be updated to the §1 canonical wording (drop the "no third-party AI processor" absolute; name the EU fallback). This is a dependency on the sibling/owner track, gated behind G4. The executing instance flags it; it does not rewrite marketing copy.

**Press-back gate G4 (Adam):** Adam reviews + approves the DPA Schedule B+C, the RoPA entry, the retention/DSAR policy, AND the revised positioning wording before any legal/marketing doc is committed/published. Human review is mandatory for legal + positioning text.

### Phase 5 — Model-trust acceptance, shadow→primary cutover, observability, handoff

**Acceptance set FIRST (§5B / G-ACCEPT):** the labelled acceptance set across the full document spread (bank statements / RCT / Gaeilge / supermarket-VAT / handwritten / multi-page) with field-level precision/recall + totals/VAT reconciliation gates must pass before primary cutover. **qwen3.5:9b is not trusted for live financial extraction until G-ACCEPT passes.**

**Cutover discipline + shadow-mode privacy (Codex #11):** run **shadow mode first** — each doc through BOTH the old inline path AND the new ZBook path, diff the extracted fields, before flipping the ZBook to primary. **CRITICAL privacy constraint:** the old path includes xAI, so shadow mode against **real client docs would silently re-send them to xAI** — exactly the contradiction this PRD eliminates. Therefore **shadow mode MUST use sanitized/synthetic fixtures, OR explicit per-tenant opt-in** before any real client doc is double-sent through the old (xAI) path. Default = sanitized fixtures. (Even better, once xAI is pruned in P3, shadow the new EU-only path against the labelled set instead of the live old path.)

**Observability + ops (Codex #14).** Required before cutover: health checks cax21 → ZBook + Tailscale node-offline alert for pop-os; alerts on queue-depth (§8A), failed-job, fallback-rate (rising = the privacy/owned-hardware promise silently degrading), GPU memory/temperature, disk-space (LUKS volume), service-restart; a per-document engine-path audit trail (which engine handled each doc — zbook / hetzner-cpu / mistral — without logging document content); and runbooks for "ZBook offline", "token leaked / rotate", "bad extraction / replay", "Mistral fallback down" (→ jobs hold as `failed` with bytes retained; no xAI escape hatch — Adam Option B).

**Acceptance criteria (ALL must be true to declare done):**

- [ ] **G-HARD passed** (§5A): LUKS verified, temp-wipe tested, `docops-ocr` containerized non-root with limits, ACL + reachability-negatives proven, Mistral DPA confirmed EU-only, RoPA entry Adam-approved
- [ ] **G-ACCEPT passed** (§5B): labelled acceptance set across the full spread meets precision/recall + reconciliation gates; handwritten/low-conf → review; regression suite frozen
- [ ] `cax21` on tailnet; ACL default-deny, restricts it to `100.78.148.106:8088` only; cax21 proven UNABLE to reach `:11434`/SSH/`:4000` (G1)
- [ ] `docops-ocr` `/healthz` returns 200 from cax21 over Tailscale; `/ocr` returns valid JSON on a real sample invoice (G2)
- [ ] Upload route returns `202` fast + async UX (polling endpoint + status UI + idempotency) works; original PDF persisted to object storage; `Extraction` row written with `engine_used='zbook'` (G3)
- [ ] ZBook-down test → Hetzner-CPU OCR recovers text, Mistral EU does understanding, row still written, no 502, doc never lost, **xAI never touched** (G3)
- [ ] Worker-crash test → stale `processing` job re-queued + completed (Codex #6)
- [ ] moondream referenced NOWHERE in the OCR path; **xAI removed from `llm_extractor.py` and unreachable from the extract route** (grep both)
- [ ] Raw-document retention/DSAR policy implemented + object-storage encryption-at-rest + tenant-isolation test passing (Codex #8)
- [ ] Shadow-mode used sanitized fixtures or explicit opt-in (no silent real-doc xAI re-send); field diff reviewed; accuracy parity or better
- [ ] Observability live: health/queue/fallback-rate/GPU/disk/node-offline alerts + per-doc engine audit trail + 4 runbooks (Codex #14)
- [ ] DPA Schedule B+C + RoPA updated, xAI removed, + revised positioning wording — all Adam-approved (G4)
- [ ] `INFRA.md` §14 updated (ZBook OCR backend entry: host, port, auth, EU-only fallback order, tailnet ACL, retention) + callmeie-fix mirror
- [ ] `NEW-REPOS-RUNNING-CONTEXT.md` appended; `NEW-REPOS-NEXT-STEPS.md` updated; `TENSION-LEDGER.md` entry for the dev-vs-prod-ZBook tension (§13 #1); Anamnesis architecture-decision stored; Hermes pattern published
- [ ] Touch gate: a different substrate pressed back per phase (runtime G2/G3/G-ACCEPT, Adam G1/G4/G5/G-HARD). Codex-peer review of THIS PRD already done (`_codex-docops-review.md`, findings 1-17 incorporated).

---

## 7. Security — client documents are the #1 reason this exists

Client documents are the most sensitive data Doc Ops touches (invoices = financial PII, VAT numbers, IBANs, supplier relationships). Self-hosting OCR is the privacy win — but the home box + the tailnet bridge are new surfaces. Required:

- **No public exposure of the ZBook.** `docops-ocr` bound to the tailscale IP only, ufw-denied on every other interface. Option C (public API) is rejected.
- **Tailnet least-privilege ACL.** cax21 reaches ONLY `100.78.148.106:8088`. Not Ollama `:11434`, not SSH, not NoMachine `:4000`.
- **Tailnet ACL + bearer is NOT sufficient alone (Codex #8/#9)** — see §5A.4 for the full hardening: default-deny policy, tagged source/service identity, key expiry, Tailscale-SSH constraint, no-subnet-routing, token rotation/revocation runbook, and the size/page/content-type limits + parser sandbox (§5A.3) so a stolen token alone cannot exfiltrate or exploit.
- **Bearer auth on `docops-ocr`** — 32-byte token, stored in vault `~/.claude/routes/.env` + Coolify env, never in code/git. Treat as compromisable (one factor); rotation/revocation runbook per §5A.4.
- **No client document content in logs** — on either box. Log doc_id, sha256, elapsed, confidence, engine. Never ocr_text / fields / images. (The ZBook is headless 24/7; a leaky log is a standing exposure.)
- **Encryption in transit:** Tailscale/WireGuard end-to-end. (If Option C ever revived: mTLS mandatory — but it's rejected.)
- **Encryption at rest — HARD BLOCKER (§5A.1, Codex #3):** the ZBook was installed **UNENCRYPTED.** LUKS full-disk encryption (root + swap + working dir) is a Phase 0 blocker requiring a reinstall-or-encrypt decision — NOT "confirm LUKS." Temp-file wipe per §5A.2 (memory-only is insufficient; PDF/OCR libs spill temp). Original-bytes retention is on Hetzner Object Storage (EU, encrypted at rest per Phase 4), not the ZBook.
- **EU-ONLY fallback** keeps even degraded mode in-EEA: Hetzner-CPU OCR (EU, bytes never leave) then Mistral (France) on post-OCR text. **xAI is removed entirely — there is no US/third-country leg** (Adam Option B; Codex #1). EU residency is preserved on every path.
- **DPA must name the real processors + remove xAI** (Phase 4). Stating "no third party" while xAI was primary was the honesty gap (obs 20315) — this PRD closes it by removing xAI and naming the EU processors (self-hosted Ireland primary; Hetzner-CPU EU local fallback; Mistral SAS France EU on text). Use the §1 canonical positioning wording, not the absolute.
- **§5A hardening is part of security here, not separate** — LUKS at rest (5A.1), temp-wipe (5A.2), untrusted-PDF sandbox (5A.3), the full ACL/auth hardening (5A.4), Mistral EU-DPA (5A.5), RoPA (5A.6). The bullets above are the application-layer controls; §5A is the gate that must pass before client docs flow.
- **Multi-tenant isolation unchanged** — the OCR backend is tenant-agnostic; tenant scoping stays in the Hetzner app layer (`require_tenant_user`). Do not pass tenant secrets to the ZBook; pass only doc bytes + doc_id.

---

## 8. Reliability — single home laptop is the central risk

The ZBook is one consumer laptop in Adam's house: ISP outage, power cut, lid event, Pop update, GPU OOM, thermal throttle, Ollama hang. **The architecture must degrade, never drop.**

| Failure | Detection | Behaviour | Why safe |
|---|---|---|---|
| ZBook unreachable (ISP/power/Tailscale down) | `docops-ocr` `/healthz` fails / `/ocr` connection refused | Job retries N×, then **EU-only fallback**: Hetzner-CPU OCR (EU) for text, Mistral (France) for understanding | Doc processed in-EEA, just not on home GPU; never lost; **no US leg** |
| ZBook up but Ollama hung / GPU OOM | `/ocr` 5xx or timeout | Same retry → EU-only fallback | RapidOCR/Hetzner-CPU text still available; understanding falls back to Mistral EU |
| Slow under load (NUM_PARALLEL=1) | queue depth grows past threshold (§8A) | serial processing; batch is acceptable (obs 18712: batch-oriented, no sub-second p99 promise) | latency degrades, nothing drops |
| Original bytes needed for replay | — | persisted to object storage at upload (P3 step 2) before OCR even runs | any failed job is fully replayable |
| Both ZBook AND Mistral down | both fail | job ends `status=failed` with bytes retained + doc flagged (**no xAI escape hatch** — Adam Option B) | operator replays later; customer doc never silently lost; EU-residency never broken |
| Worker process crash mid-job | stale `processing` row (heartbeat timeout) | timeout-recovery re-queues the stale job (§6 P3, Codex #6) | no job stuck invisibly |
| Cutover regression | shadow-mode field diff (sanitized fixtures) | flip back to old inline path (feature flag, §11A) | reversible |

**Reliability is bounded by being pre-revenue (zero SLA today).** As customers sign, the fallback carries more weight — and the 22240 Mac Studio (8-12 customers) becomes the primary, ZBook reverts to dev. Until then: ZBook primary + EU-only fallback is the right risk posture.

## 8A. Capacity — quantify the serial constraint (Codex #13)

`OLLAMA_NUM_PARALLEL=1` + `MAX_LOADED_MODELS=1` means the ZBook is **strictly serial** — "batch-oriented" was hand-wavy; quantify it during Phase 0/G2 with the real sample set and record here:

- **Seconds/page** — measure qwen3.5:9b on a representative page on the actual 8GB RTX (RapidOCR is fast/CPU-parallel; the VL call is the serial bottleneck).
- **8-page worst case** — the stated product limit (≤8 pages); = per-page × 8 + overhead. This is the single-doc latency ceiling.
- **Daily document capacity** — `86400 s / mean-doc-seconds` at NUM_PARALLEL=1; the realistic ceiling before the queue backs up.
- **Queue-depth alert threshold** — set so a backlog that would exceed the customer latency target pages the operator (wired in §6 P5 observability).
- **Customer-facing latency target** — define it (async UX makes this "time-to-result-in-portal", not request latency); set expectation in the UI.
- **Thermal-throttle behavior** — a headless laptop under sustained load throttles; measure whether seconds/page degrades over a sustained batch and at what duty cycle, and whether `qwen2.5vl:7b` (lighter) holds throughput better under thermal pressure.
- **Concurrent uploads** — multiple customer uploads enqueue fine (202 fast-return); they serialize at the ZBook. Confirm the queue + semaphore-of-1 handles a burst without dropping.

These numbers gate whether qwen3.5:9b stays primary or `qwen2.5vl:7b` (config-flag swap) is needed for throughput, and they set the alert thresholds. Capture them at G2.

---

## 9. Non-goals (consider don'ts — privacy / cost / fragility / scope-creep / fabrication)

- **NOT** building the missing email-inbox ingest, HTML upload widget, CSV-export writer, or Stripe billing-meter. Those are the **sibling fix-track** (audit 02 loss-risks #1/#9, stack-audit upgrade #1). This PRD only changes WHERE OCR/VL compute happens + makes it reliable. Do not scope-creep into them; do not claim them done.
- **NOT** exposing the ZBook to the public internet (Option C rejected — privacy + rig-PRD non-goal).
- **NOT** running raw Ollama `:11434` to cax21 — only the `docops-ocr` wrapper `:8088` (least surface).
- **NOT** using moondream anywhere (hallucination ban).
- **REMOVE xAI entirely** (Adam Option B — reversed from the draft's "keep xAI last"). xAI is deleted from the pipeline, `llm_extractor.py`, and the DPA Schedules B/C. On a dual ZBook+Mistral outage the job holds as `failed` with bytes retained for replay — it does NOT escape to a US processor. EU-residency is never broken to preserve uptime.
- **NOT** claiming the absolute "no third-party AI processor" — Mistral is an EU third-party. Use the §1 canonical wording: *"AI runs on hardware we own in Ireland, with an EU-sovereign fallback (Mistral, France) — no data leaves the EU, no US/third-country processors."* Do not fabricate an absolute; the EU fallback must be named.
- **NOT** buying the Mac Studio (22240) — that's gated to 8-12 customers / Priming Grant; the ZBook is the bridge.
- **NOT** running other CallMeIE production traffic (receptionist voice, etc.) through this OCR path — out of scope.
- **NOT** building per-customer LoRA fine-tunes or the active-learning flywheel here (obs 18712 v0.4.2/0.4.3 — separate track; the rig CAN do it later but this PRD is OCR-serving only).

---

## 10. Cost

- **Money:** ~€0 incremental on the primary path. ZBook owned + already deployed + always-on (power is sunk cost from the rig PRD). Tailscale free tier covers cax21 + pop-os. RapidOCR + qwen3.5:9b are free/local. **Mistral Small fallback ≈ €0.001/doc** (obs 18585), incurred only on ZBook-outage docs (EU-only; xAI removed). Hetzner-CPU OCR fallback is also ~€0 (existing box).
- **Margin impact:** primary-path per-doc compute cost goes to **~€0** (vs xAI-per-call today). This is the 39%→75%+ margin move from obs 18520, now realised on Adam-owned hardware.
- **Time:** ~7-10h autonomous (the draft's 5-7h did NOT include the §5A hardening, §5B acceptance set, async UX redesign, retention policy, or observability — all now in scope) + ~2h Adam-keyboard (Tailscale auth, LUKS reinstall decision, legal/positioning review). G-HARD + G-ACCEPT are the bulk of the new time.
- **Power:** ZBook ~80-150W under load; negligible at single-box scale.

---

## 11. Risks + rollback

| Risk | Likelihood | Impact | Mitigation | Rollback |
|---|---|---|---|---|
| Tailscale on cax21 conflicts with Coolify networking | Low | Phase blocks | Install at host level, not in container; test `tailscale status` before wiring | Remove Tailscale; revert to Option B pull-model or keep OCR on Hetzner CPU |
| qwen3.5:9b too slow under real doc load (NUM_PARALLEL=1) | Medium | latency | Swap to `qwen2.5vl:7b` (config flag); batch overnight | Fall back to Mistral for live, ZBook for batch |
| Home ISP/power instability | Medium | degraded | EU-only fallback (§8) | n/a — fallback IS the mitigation |
| Accuracy regression vs current path | Medium | customer trust | G-ACCEPT acceptance set (§5B) + shadow-mode diff before cutover (Phase 5) | Feature-flag back to inline path (§11A) |
| Client doc leaked via logs / temp / swap | Low | CRITICAL/legal | No-content-logging (§7); temp-wipe + LUKS swap (§5A.2) | Purge logs; rotate token |
| Stolen / serviced / sold ZBook exposes disk | Low | CRITICAL/legal | LUKS full-disk (§5A.1, HARD BLOCKER) | Remote-wipe key; the disk is unreadable without the LUKS key |
| Malicious PDF exploits parser on ZBook | Medium | data exposure / RCE | Untrusted-PDF sandbox: containerized non-root, seccomp, size/page/content-type limits (§5A.3, Codex #17) | Kill container; rotate token; the sandbox contains blast radius |
| cax21 compromised → reaches ZBook | Low | data exposure | §5A.4 hardening: default-deny ACL to `:8088` only, no Ollama/SSH/NoMachine reach, bearer + parser limits | Revoke cax21 tailnet key + rotate token |
| DPA/positioning overclaims | Low | legal/integrity | §1 canonical wording (no absolute); Phase 4 names EU fallback + removes xAI; Adam/solicitor review (G4) | Re-edit before publish |
| Scope-creep into the inbox/CSV/billing fix-track | Medium | timeline | §9 non-goals; the executing instance must refuse | Drop the extra work |

### Honest rollback (Codex #15 — "feature-flag back" was too optimistic)

The async route + object persistence + schema + UI changes mean rollback is not a single flag. Specify before cutover:
- **Exact feature flags:** `DOCOPS_OCR_BACKEND={zbook|inline}` (routes upload to async-ZBook vs old synchronous inline) and `DOCOPS_PERSIST_RAW={on|off}`.
- **Old synchronous path RETAINED, not removed**, behind the flag, for the whole cutover window (do not delete `extractor.py` inline call). xAI is pruned regardless — so the *inline* rollback path uses Hetzner-CPU OCR + Mistral EU, NOT the old xAI path (rolling back must not re-introduce the legal-copy violation).
- **DB compatibility:** `ocr_jobs` + the new `Extraction` columns are additive (migration `0010`); rollback leaves the table in place, just stops enqueuing.
- **In-flight jobs on rollback:** drain `queued`/`processing` jobs first (or mark them for replay); do not orphan customer docs mid-flight.
- **Partially-processed replay:** any `failed`/`fallback` job replays from the retained original bytes in object storage.

## 11A. Hard-to-reverse decisions — explicit owner approval required (Codex #16)

These are one-way doors; implementation gates are NOT enough — Adam must approve each explicitly (most are answered by the RESOLVED Option B decision, recorded here for the record):
- **Home hardware becomes part of the production processing record** (RoPA/DPA lists the ZBook, Ireland) — APPROVED via Option B; G-HARD/§5A.6 implements it.
- **`/extract` semantics change to async (`202`)** — changes the customer API/UX contract; the async UX (§6 P3 step 6) is the matching redesign.
- **Raw-document retention introduced** (originals stored in object storage) — a standing privacy/retention obligation (§Phase 4 retention/DSAR policy); APPROVED as the loss-risk-#3 fix.
- **Joining the production Hetzner host (cax21) to the tailnet** — expands cax21's identity/attack surface; locked down per §5A.4.
- **Legal/positioning change** — DPA Schedules B/C rewritten + xAI removed + live-site copy changed to the §1 wording; APPROVED via Option B, but the *published* wording still needs solicitor sign-off at G4.
- **LUKS reinstall** (if Option 1 in §5A.1 is chosen) — wipes/rebuilds the ZBook system partition; explicit go before reinstall.

---

## 12. Press-back gates summary (Quaternity Cycle, second-thing protocol)

| Gate | Press-back (different substrate) | Required-by |
|---|---|---|
| G0 | Discovery findings vs audit confirmed by runtime (`git log`, `ollama list`, `tailscale status`) | before Phase 1 |
| **G-HARD** | Hardening baseline (§5A): LUKS verified (`lsblk`/`cryptsetup`), temp-wipe tested, container non-root + limits, ACL/reachability-negatives proven, Mistral DPA confirmed EU-only, RoPA Adam-approved | **before ANY client doc** |
| G1 | Adam confirms Tailscale auth + ACL; `tailscale status` runtime shows cax21+pop-os | before backend wiring |
| G2 | Runtime: `docops-ocr /ocr` returns valid JSON on a real sample invoice; capacity numbers captured (§8A) | before Phase 3 |
| G3 | Runtime+FS: 202 fast-return + async UX, original persisted, Extraction row, ZBook-down→Hetzner-CPU+Mistral EU fallback proven (no xAI), worker-crash recovery | before cutover |
| **G-ACCEPT** | Runtime metrics (§5B): labelled acceptance set across full spread meets precision/recall + reconciliation gates; regression suite frozen | **before primary cutover** |
| G4 | Adam reviews + approves DPA Schedule B+C + RoPA + retention/DSAR + revised positioning wording (xAI removed) | before any legal/marketing publish |
| G5 | Adam reviews shadow-mode field diff (sanitized fixtures) + approves ZBook-as-primary cutover | before flipping primary |

Touch gate: each G requires a different substrate (runtime G0/G2/G3/G-HARD/G-ACCEPT, Adam G1/G4/G5/G-HARD). NOT Claude self-review. **Codex-peer review of THIS PRD is DONE** (`_codex-docops-review.md`, findings 1-17 — incorporated into §5A/§5B/§8A/§6/§11/§11A + the positioning change; the review pressed back and was incorporated, not overruled). This is the different-substrate touch on the PRD itself.

---

## 13. Decisions — RESOLVED (header block + Codex review); recorded here for the executing instance

> The draft asked Adam to decide 1-6. **They are now resolved** (Adam Option B + Codex findings). The executing instance treats these as GIVEN, not open. Two new gating decisions (queue substrate, EU-only-vs-keep-xAI) were resolved by the Codex review + Option B.

1. **ZBook = primary OCR/VL backend (with EU-only fallback) — RESOLVED YES (Option B).** Promoted from dev/eval to primary-with-fallback; safe now (24/7 deployed + zero paying customers + EU fallback). Log the chosen pole in `TENSION-LEDGER.md` (dev-vs-prod-ZBook).

2. **Reachability — RESOLVED: Option A (Tailscale on cax21) + Option B's one-way data-flow discipline.** Hardened per §5A.4. Codex #9 noted Option B (outbound-pull) is the cleaner long-term security model; if Adam later prefers it, the §5/§6 transport swaps without changing the app contract — but Option A is the chosen bridge, locked down hard.

3. **Queue substrate — RESOLVED: a SEPARATE worker process/container with Postgres `FOR UPDATE SKIP LOCKED` + heartbeat + dead-letter (NOT an in-app asyncio poller).** Codex #6 flagged the in-app poller as fragile for customer-facing work (restart-interruption, double-processing, weak observability). `arq`+tiny-Redis is an acceptable equivalent. The draft's "in-app asyncio poller" default is REVERSED.

4. **VL model — RESOLVED: `qwen3.5:9b` primary, `qwen2.5vl:7b` config-flag fallback** — BUT trust is gated by the §5B acceptance set (G-ACCEPT), not the invoice bake-off (Codex #12). Throughput may force the `qwen2.5vl:7b` swap per §8A capacity numbers.

5. **Fallback order — RESOLVED: ZBook → Hetzner-CPU OCR (EU) → Mistral Small (France/EU) → STOP. xAI REMOVED (Option B).** EU-only; on dual outage the job holds as `failed` with bytes retained, never escaping to a US processor. The draft's "→ xAI (last)" is REMOVED.

6. **Codex-peer pre-review — RESOLVED: DONE.** `_codex-docops-review.md` (findings 1-17) returned "DO NOT IMPLEMENT YET"; incorporated into this revision (§5A hardening, §5B acceptance, §8A capacity, §6 P3 worker+UX, §11 honest rollback, §11A hard-to-reverse register, the positioning change). The review pressed back and was incorporated — the touch gate on the PRD is satisfied.

**Status: ready to dispatch.** Open dependencies before client docs flow: G-HARD (§5A) + G-ACCEPT (§5B) as Phase 0/1 gates; the positioning/legal copy update (§4.3 / Phase 4, out-of-scope to author here, gated at G4); Mistral EU-DPA confirmation (§5A.5).
