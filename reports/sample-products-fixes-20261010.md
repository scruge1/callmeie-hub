# Targeted sample reading fixes

Changed only `websites/samples/industries/02-solicitor-swiss.html`, `06-trade-pro-dark-oled.html` and `08-financial-brutalism-editorial.html`. Added scoped static CSS; no runtime scripts or sample content changed.

- Solicitor: reduced desktop responsive headline size to fit its existing grid column. Mobile practice names now occupy their own line instead of the narrow space beside the practice number.
- Trade: stacked contact labels and values on mobile. The email link was the clipped anchor; it now fits and can wrap if needed.
- Financial: mobile section labels stack above their titles, allowing Introductions to fit the reading area.

Verified loaded local CSS and awaited fonts before measurement. Viewed all 12 final full-page screenshots: WebKit 26.4 at 375/390 and Chrome at 768/1280. Viewed additional targeted viewport detail screenshots. Original headline, practice-name, email and Introductions defects no longer appear in the final metrics. Sample themes are retained.

One shared `_owl-nav` gallery-anchor measurement remains outside this edit scope: scroll65/client61 at375 on Solicitor/Trade; scroll250/client242 at768. Reported to root owner. This is not evidence that the original clipping persists.

Evidence outside Git: `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/sample-products-fixed/results.json`. Same-worktree quiet preview port8771. No publication.
