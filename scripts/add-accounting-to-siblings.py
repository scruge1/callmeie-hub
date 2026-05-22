"""Add accounting.html link to vertical-switch row + footer 'Other verticals'
list in 9 sibling receptionist vertical pages.

Pattern: every page has solicitor.html in two places. Insert
accounting.html right after solicitor in both. Idempotent — skips if
already added.

Run from callmeie-hub root: python scripts/add-accounting-to-siblings.py
"""
import pathlib
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
RECEPT = ROOT / "receptionist"

# All vertical pages including solicitor itself (so solicitor's own page also
# offers the accounting link as a sibling).
PAGES = [
    "dental.html", "cafe.html", "salon.html", "solicitor.html",
    "motor-factors.html", "electrician.html", "plumber.html",
    "mechanic.html", "restaurant.html",
]

# Vertical-switch row pattern: matches a line containing a link to solicitor.html
# inside the switch nav, followed by ` ·` or end. We insert a new <a> after it.
SWITCH_PATTERN = re.compile(
    r'(<a href="solicitor\.html"[^>]*>\s*<strong>?Solicitors</strong>?\s*</a>|<a href="solicitor\.html">Solicitors</a>)'
)
SWITCH_INSERT = ' ·\n      <a href="accounting.html">Accountants</a>'

# Footer "Other verticals" list item — different shape: <li><a href="solicitor.html">Solicitors</a></li>
FOOTER_PATTERN = re.compile(
    r'<li><a href="solicitor\.html">Solicitors</a></li>'
)
FOOTER_INSERT = '<li><a href="solicitor.html">Solicitors</a></li>\n          <li><a href="accounting.html">Accountants</a></li>'

# Idempotency check — if accounting.html already linked, skip the file.
ALREADY = re.compile(r'href="accounting\.html"')


def process(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    if ALREADY.search(text):
        return ("skip-already", 0, 0)

    new_text = text
    switch_hits = 0
    footer_hits = 0

    # Switch row — simpler pattern, append ` · <a accounting>` after the solicitor anchor.
    # We don't want to double-insert; SWITCH_PATTERN matches only the solicitor anchor.
    def switch_sub(m):
        nonlocal switch_hits
        switch_hits += 1
        # Append the insertion right after the solicitor anchor + the existing separator
        return m.group(0) + SWITCH_INSERT

    new_text = SWITCH_PATTERN.sub(switch_sub, new_text, count=1)

    def footer_sub(m):
        nonlocal footer_hits
        footer_hits += 1
        return FOOTER_INSERT

    new_text = FOOTER_PATTERN.sub(footer_sub, new_text, count=1)

    if switch_hits == 0 and footer_hits == 0:
        return ("no-pattern", 0, 0)

    path.write_text(new_text, encoding="utf-8")
    return ("updated", switch_hits, footer_hits)


def main():
    results = []
    for name in PAGES:
        p = RECEPT / name
        if not p.exists():
            print(f"  MISSING  {name}")
            results.append((name, "missing", 0, 0))
            continue
        status, s, f = process(p)
        results.append((name, status, s, f))
        marker = {
            "updated": "✓",
            "skip-already": "—",
            "no-pattern": "!",
            "missing": "?",
        }.get(status, "?")
        print(f"  {marker} {name:25s} {status:14s} switch={s} footer={f}")

    print()
    updated = sum(1 for r in results if r[1] == "updated")
    skipped = sum(1 for r in results if r[1] == "skip-already")
    print(f"Updated: {updated}  Skipped (already linked): {skipped}  Issues: {len(results) - updated - skipped}")


if __name__ == "__main__":
    main()
