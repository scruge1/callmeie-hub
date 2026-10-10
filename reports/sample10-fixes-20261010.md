# Local-services sample responsiveness fix

Changed only `websites/samples/industries/10-local-services-brutalism.html`. Static CSS uses zero-minimum grid tracks and hero children, narrower mobile padding and bounded wrapping buttons/headline. Preserved the sample colours, desktop composition, content and scripts.

Wrapped the rates table in a labelled `role=region` container with `tabindex=0`, horizontal local scrolling and visible focus outline. The table has a 720px minimum width for readable cells.

Verified loaded local styles and fonts. Viewed all four final full-page captures: WebKit 26.4 at 375/390px and Chrome at 768/1280px, plus mobile hero and right-scrolled table detail views. Actual element bounds were checked, not only document overflow. At375, hero left/right end350px and cards332px. At390, hero left/right end365px and cards347px. The rates region stays within those page bounds. Its final column is reachable at scroll395/380px on mobile. The scroll region is focusable and has an accessible label. Desktop/tablet objects remain within their viewport.

The only detected internal overflow on mobile is the intentional rates scroll region; original concealed hero/table clipping is resolved. No JavaScript changes or publication.

Evidence outside Git: `C:/Users/a33_s/AppData/Local/callmeie-site-review-20261010/output/playwright/sample10-fixed/results.json` and `bounds.json`. Quiet local server8771 serves the same worktree.
