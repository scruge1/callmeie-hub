"""add-wa-sentinels.py — one-shot inserter for COHESION:WHATSAPP sentinels.

Walks the conversion-oriented pages that already participate in cohesion
(detected via COHESION:FOOTER-END marker) and inserts a WhatsApp sentinel
pair right after the footer sentinel, picking a per-page-slug prefill so
every wa.me link arrives with vertical-specific context.

Skips:
  - any page already containing COHESION:WHATSAPP-START (idempotent)
  - /websites/samples/*  and  /websites/demos/*  (bespoke samples, no FAB)
  - /legal/*  and any *terms.html / *privacy.html  (formal pages)
  - test-inject-dummy.html

Run once. Then run scripts/inject-cohesion.py to render the partials.
"""
from __future__ import annotations
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Slug -> (utm_content, raw prefill text). Script URL-encodes at write time.
PREFILL_BY_SLUG: dict[str, tuple[str, str]] = {
    "about":            ("about",            "Hi CallMeIE — quick question about your team/setup"),
    "demo":             ("demo",             "Hi CallMeIE — I just tried the demo, want to chat"),
    "dental":           ("dental",           "Hi CallMeIE — I'm a dental practice in [town], interested in your AI Receptionist"),
    "motor-factors":    ("motor-factors",    "Hi CallMeIE — I'm a motor factors business, interested in your AI Receptionist"),
    "salon":            ("salon",            "Hi CallMeIE — I'm a salon, interested in your AI Receptionist"),
    "solicitor":        ("solicitor",        "Hi CallMeIE — I'm a solicitor's firm, interested in your AI Receptionist"),
    "onboard":          ("onboard",          "Hi CallMeIE — quick question while filling in your onboarding form"),
    "onboard-details":  ("onboard-details",  "Hi CallMeIE — quick question about an onboarding detail"),
}

# Pages that opt out by path fragment.
SKIP_PATH_FRAGMENTS = (
    "/_partials/",
    "/scripts/",
    "/node_modules/",
    "/.git/",
    "/qa-screenshots/",
    "/legal/",
    "/websites/samples/",
    "/websites/demos/",
    "test-inject-dummy.html",
    "privacy.html",
    "terms.html",
    "/blog/",
)

FOOTER_END_MARKER = "<!-- COHESION:FOOTER-END -->"
WA_START_MARKER   = "<!-- COHESION:WHATSAPP-START"


def url_encode(text: str) -> str:
    """Match the exact encoding used in the four already-shipped pages.
    We use urllib.parse.quote with safe='' to encode every reserved char,
    then handcraft the em-dash + apostrophe to match prior commits."""
    from urllib.parse import quote
    return quote(text, safe="")


def slug_for(page: Path) -> str | None:
    """Return slug key from PREFILL_BY_SLUG matching this page's filename, else None."""
    stem = page.stem  # 'dental' for dental.html
    return stem if stem in PREFILL_BY_SLUG else None


def should_skip(page: Path) -> bool:
    posix = page.as_posix()
    return any(frag in posix for frag in SKIP_PATH_FRAGMENTS)


def insert_sentinel(text: str, prefill_encoded: str, utm_content: str) -> str | None:
    """Insert WHATSAPP sentinel pair after the FIRST FOOTER-END marker.
    Returns new text or None if marker not found / already has WA sentinel."""
    if WA_START_MARKER in text:
        return None  # already done
    idx = text.find(FOOTER_END_MARKER)
    if idx == -1:
        return None
    end_idx = idx + len(FOOTER_END_MARKER)
    block = (
        f'\n\n<!-- COHESION:WHATSAPP-START prefill="{prefill_encoded}" '
        f'utm_content="{utm_content}" -->\n'
        f'<!-- COHESION:WHATSAPP-END -->'
    )
    return text[:end_idx] + block + text[end_idx:]


def main() -> int:
    touched = 0
    skipped = 0
    no_slug = 0

    for page in REPO_ROOT.rglob("*.html"):
        if should_skip(page):
            continue
        slug = slug_for(page)
        if slug is None:
            no_slug += 1
            continue
        utm_content, raw_prefill = PREFILL_BY_SLUG[slug]
        text = page.read_text(encoding="utf-8")
        new_text = insert_sentinel(text, url_encode(raw_prefill), utm_content)
        rel = page.relative_to(REPO_ROOT).as_posix()
        if new_text is None:
            skipped += 1
            print(f"  SKIP   {rel}  (already has WA sentinel or no FOOTER-END)")
            continue
        page.write_text(new_text, encoding="utf-8", newline="\n")
        touched += 1
        print(f"  WROTE  {rel}  (slug={slug})")

    print(f"\nSummary: {touched} pages got WA sentinel, "
          f"{skipped} skipped, {no_slug} not in slug map")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
