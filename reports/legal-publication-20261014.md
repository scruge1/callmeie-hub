# Legal publication - 14 October 2026

Adam authorised deployment after reviewing the v02 insurance/legal package.
The reviewed branch starts at current remote main
`948fc2e33d8938a0be56bb96b9278d24bb252997`. A fresh fetch and remote check confirm
that main has not advanced. Publication uses a normal fast-forward push.

## Scope

- `legal/terms.html`, `legal/privacy.html`, `legal/dpa.html`, `legal/index.html`:
  v1.3, scoped future technical services and the operative sole-trader supplier.
- `_internal/order-forms/order-form-template.md`: v2.0, current modular Order.
- `README.md`, `ACTIVE-CHECKPOINT.md`, this report: source/status routing.

Payment routes are generic; Stripe is optional. IP grants require verified rights.
Future processing uses an agreed Order and applicable DPA Schedule, including
Schedule D for software, AI, automation, integrations and consultancy. Article 28
duties remain. Listing a service category does not establish a live deployment.

The old Order is preserved in Git history and in a clearly superseded local
archive. The archive is not staged or added to the public site. It is excluded
from the current reference PDF and active legal source ZIP. This publication
does not retrospectively replace the June website customer's agreement.

## Validation

The reviewed v02 source hashes match the publication files. No styles or
executable scripts changed. Local browser checks passed for four legal pages
at desktop/mobile widths. All 27 v02 PDF pages were visually reviewed. Normal
site checks pass: 88 cohesion pages, zero drift/errors; 93 cookie-audit pages,
zero hits. `git diff --check` passes.

GitNexus CLI 1.6.12 detection was invoked for this worktree. It reports repository
not found. Graph coverage is unavailable, not a passing result. Direct staged
scope, source hashes and executable-script comparison bound this prose-only
change. No tool installation or runtime configuration change was required.

## Deployment

Published source release: `1e20ed6c0515c677e345ef313a3803d7791f474f`.
The normal fast-forward push preserved all previous main history. GitHub Pages
run [38609229267](https://github.com/scruge1/callmeie-hub/actions/runs/38609229267)
and cohesion run [38609232728](https://github.com/scruge1/callmeie-hub/actions/runs/38609232728)
both succeeded. Pages reports this source built at 17:45:41 UTC.

Live verification at 17:49 UTC confirms HTTP 200 and exact reviewed hashes for
all four legal HTML files and the current Order Markdown. All eight live
desktop/mobile cases pass scope, identity, version, viewport and internal-anchor
checks. Schedule D navigation passes at both sizes. There are no page errors.
The desktop/mobile screenshots were inspected. The unchanged homepage exactly
matches its Git blob; a raw worktree comparison differed only in CRLF endings.
The local superseded-archive URL returns 404. The initial probe during the Pages
build saw old files; it is retained separately and was not counted as acceptance.

These source files match the reviewed v02 bytes:

| Path | SHA256 |
| --- | --- |
| `legal/terms.html` | `4c4ad78e110299dc2bb1740a71d6971c002e8e30a300844b75fd5e82738c184f` |
| `legal/privacy.html` | `6e5634f6482a06b001ba752c61a12a6b370b355a068ffa58ebeed3bb402257e9` |
| `legal/dpa.html` | `8b144709f7bd9701fb2aac8af1c6dc27b3c74f1339ebcc9ebd31e145848794f6` |
| `legal/index.html` | `d7303ac6c5161e418bb02b31223f30f3c9b5c82f8b25c7fa2b17f5d038eddc1b` |
| `_internal/order-forms/order-form-template.md` | `c94dc2fce04642fd04aa166b7027f3347560321ce5b6fcf1612afcf6fb8060f7` |

Raw live receipts, final unsigned insurance package and delivery receipts remain
outside Git under
`C:/Users/a33_s/Downloads/CallMeIE-PI-draft-20261014/`.

Recovery preserves the base commit and reviewed branch. A recovery, if needed,
must revert only these legal changes on current main and recheck live files;
do not reset unrelated newer work. No signature, broker send, cover binding,
voice activation or client/payment/provider configuration change is included.
