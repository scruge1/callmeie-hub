# Independent document visual review

Date: 2026-10-10. Local preview http://127.0.0.1:8769/. Source was frozen; no source edits made.

Reviewed `/legal/`, `/legal/privacy.html`, `/legal/terms.html`, `/legal/dpa.html`, `/websites/managed-plans-scope.html`, and `/websites/care-plans-scope.html` in Chromium at 1280px, 375px and 768px. All 18 full-page screenshots were visually viewed. Four additional mobile/tablet viewport screenshots inspected the privacy and managed-scope table regions.

Sequential navigation waited for network idle, fonts and accessible loaded brand.css rules. Every page had loaded local styles and Inter body text. All 18 captures measured zero page-level horizontal overflow. This does not establish readable tables by itself.

## Issues sent to root

- Both website scope pages have two consecutive full footers: the retained old AI-staff/AI-First Websites footer and the new canonical footer. Visible at all three widths. Remove the old wrapper only; preserve substantive contract copy.
- Managed-scope four-column table compresses to 335px at mobile width. Cells split ordinary words into many fragments. Existing `.table-scroll` needs a table minimum width around 640px so the table scrolls locally. Desktop and tablet tables are readable.
- Privacy provider table compresses to 335px at mobile width. Provider names split mid-word, including Google, Resend and GitHub. Give the existing local scrolling table a minimum width around 480px, or give its first column sufficient width. Tablet and desktop are readable.

Other checked headers, document contents, text and footer objects align. Legal index cards stack correctly at mobile and remain readable at tablet. Long legal documents remain long by design. This is a visual review; legal accuracy was not re-certified or rewritten.

Evidence stays outside Git: `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/document-review/`. Metrics: `results.json`. Root owns fixes and final revalidation.

## Authorized fixes and final verification

Root authorized the three layout fixes after review. Removed only the old duplicate footer on Managed Scope and Care Scope. Added inline minimum widths of 480px to Privacy's provider table and 640px to Managed Scope's four-column table. Substantive terms, table cell text and scripts remain unchanged.

The original server on 8769 stopped. Final verification used a quiet server for the same worktree on 8771. All three changed routes were recaptured and visually viewed at 1280px, 375px and 768px: nine full-page images, plus four table viewport images and two right-scrolled mobile table images. All nine checks report loaded styles and zero page overflow. Both scope pages now show one canonical footer. At 375px, tables are 480/640px inside 335px scroll regions; horizontal scrolling reaches the rightmost columns (145/305px). Tablet and desktop remain readable.

Final evidence: `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/document-review-fixed/`, including `results.json`. All flagged fixes are resolved in the local preview. No deployment or legal-copy rewrite performed.
