"""audit-no-cookies.py — verify ZERO analytics/pixels/cookies/storage/widgets across the site.
   Per SITE-COHESION-DESIGN-RECIPE §17.6: cookie-banner deferral is defensible
   ONLY if every served HTML page carries no analytics or tracking surface.
   Exit 0 = clean (no banner needed). Exit 1 = at least one match (banner mandatory same commit).
   USAGE:
     python scripts/audit-no-cookies.py            # walk repo HTML, exit 1 on hit
     python scripts/audit-no-cookies.py --verbose  # show per-page status

   P2-1 STATUS (2026-05-09):
   ------------------------
   Operator-visibility task to add web analytics is BLOCKED by the rules
   below. callmeie.ie ships with no analytics and no cookie banner on
   purpose — the brand promise is "no cookies, no tracking." Three
   options for getting analytics without breaking that:

     A) Move callmeie.ie onto a Cloudflare-proxied A record (currently
        GitHub Pages, proxied:false in DNS). Cloudflare Web Analytics
        (server-side, no JS, no cookies) becomes available + the audit
        rules below remain green.
     B) Add Umami via analytics.owlzone.trade on a "no localStorage"
        config + add the consent banner. Loses the no-banner promise.
     C) Keep zero analytics. Accept the operator-visibility blind spot
        as the price of the brand promise.

   Defer to Adam. Until decided, P2-1 stays deferred and this comment
   is the audit trail.
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"_partials", "scripts", "node_modules", ".git", ".github", ".githooks"}

# Patterns that REQUIRE a cookie banner under Irish DPC + GDPR.
# Each tuple = (pattern, severity, why)
PATTERNS = [
    (r"google-analytics\.com",                "CRITICAL", "Google Analytics — non-essential cookies"),
    (r"googletagmanager\.com",                "CRITICAL", "Google Tag Manager — wraps any tracker"),
    (r"\banalytics\.js\b",                    "CRITICAL", "GA legacy library"),
    (r"\bgtag\s*\(",                          "CRITICAL", "Google Tag function call"),
    (r"\bfbq\s*\(",                           "CRITICAL", "Facebook Pixel"),
    (r"\bdataLayer\.push",                    "CRITICAL", "GTM dataLayer"),
    (r"plausible\.io",                        "HIGH",     "Plausible Analytics — cookieless but still triggers DPC consent rules in some interpretations"),
    (r"\bumami\.is\b",                        "HIGH",     "Umami Analytics"),
    (r"fathom\.com",                          "HIGH",     "Fathom Analytics"),
    (r"\bmixpanel\b",                         "CRITICAL", "Mixpanel"),
    (r"\bsegment\.io\b",                      "CRITICAL", "Segment"),
    (r"\bhotjar\b",                           "CRITICAL", "Hotjar session recording"),
    (r"\bfullstory\b",                        "CRITICAL", "FullStory session recording"),
    (r"\bclarity\.ms\b",                      "CRITICAL", "Microsoft Clarity"),
    (r"localStorage\.setItem\s*\(",           "HIGH",     "localStorage write — needs consent if non-essential"),
    (r"sessionStorage\.setItem\s*\(",         "MEDIUM",   "sessionStorage write — same-tab only, lower risk"),
    (r"document\.cookie\s*=",                 "HIGH",     "Direct cookie write"),
    (r"linkedin\.com/insight",                "HIGH",     "LinkedIn Insight Tag"),
    (r"twitter\.com/i/adsct",                 "HIGH",     "Twitter Ads conversion"),
    (r"<iframe\s+[^>]*src\s*=\s*[\"']https?://(?!fonts\.googleapis|fonts\.gstatic|stripe\.com|www\.youtube-nocookie|www\.openstreetmap\.org/export)", "MEDIUM", "Third-party iframe (excluding allow-listed)"),
]

# Build a single combined regex for fast scan
COMBINED_RE = re.compile("|".join(f"(?P<p{i}>{p[0]})" for i, p in enumerate(PATTERNS)), re.IGNORECASE)


def find_pages():
    pages = []
    for path in REPO_ROOT.rglob("*.html"):
        if any(part in EXCLUDE_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        pages.append(path)
    return pages


def scan_page(path: Path) -> list[tuple[str, str, str, int]]:
    """Returns list of (pattern, severity, why, line_no) for hits."""
    hits = []
    text = path.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        for j, (pattern, severity, why) in enumerate(PATTERNS):
            if re.search(pattern, line, re.IGNORECASE):
                hits.append((pattern, severity, why, i))
    return hits


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--verbose", "-v", action="store_true", help="show per-page status")
    args = parser.parse_args()

    pages = find_pages()
    total_hits = 0
    pages_with_hits = 0
    by_severity = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0}

    for page in pages:
        rel = page.relative_to(REPO_ROOT).as_posix()
        hits = scan_page(page)
        if hits:
            pages_with_hits += 1
            total_hits += len(hits)
            print(f"\n  {rel}", file=sys.stderr)
            for pat, sev, why, line_no in hits:
                by_severity[sev] = by_severity.get(sev, 0) + 1
                print(f"    L{line_no} [{sev}] {why}", file=sys.stderr)
        elif args.verbose:
            print(f"  OK {rel}")

    print(f"\nAUDIT summary: {len(pages)} pages scanned, {pages_with_hits} with hits, {total_hits} total hits",
          file=sys.stderr if total_hits else sys.stdout)
    print(f"  CRITICAL: {by_severity.get('CRITICAL', 0)}, HIGH: {by_severity.get('HIGH', 0)}, MEDIUM: {by_severity.get('MEDIUM', 0)}",
          file=sys.stderr if total_hits else sys.stdout)

    if total_hits:
        print("\n[FAIL] Cookie banner is MANDATORY before Phase 3 final commit.", file=sys.stderr)
        print("       See SITE-COHESION-DESIGN-RECIPE.md §17.6 + Codex Q5 enforcement.", file=sys.stderr)
        return 1
    print("\n[PASS] Zero analytics/pixels/cookies/widgets detected. Cookie banner deferral defensible.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
