# CallMeIE website consolidation

## Scope and source

Adam rejected the first 10 October consolidation as too basic and off-brand.
The Great National pilot proposal v1 is the explicit reference for this correction.
Its v09 editorial notes preserve logos, paper/burgundy colours and existing fonts
while cutting repeated and internal narration. v1 keeps that visual system.
The old dark/Geist ai-agency spec and May per-product themes are historical.
Simplifying copy does not authorise changing CallMeIE's visual identity.
Keep the 7/8 October seller, privacy, coverage-hours and form corrections.

## Visual thesis

Warm paper, deep ink, burgundy rules and strong sans-serif type. Use the actual
CallMeIE icon and wordmark. Preserve confident hierarchy and generous space.

Reference: GN output/proposal/build-proposal-pack.py and rendered v1 pages,
existing receptionist/assets/callmeie-logo.png, and installed design-hub section
templates for layout. Generic references must not override this selected identity.

## Shared system

- Paper #f5f1e8, alternate #ece7d9, ink #0b0a08, muted #545454, line #c8c1b3.
- One action accent: burgundy #5a1420. Product photos and demo artwork can vary.
- Archivo Black for display. IBM Plex Sans for body, navigation, prices and forms.
- Self-host the existing proposal font files with their OFL licences. Two common
  font families; use Plex and tabular figures for labels/data.
- No decorative emoji, forced heading line breaks or decorative final-word colour accents.
- No replacement text logo, generic serif theme or new palette.
- Square minimal controls, 2px corners, hairlines and restrained inset depth.
  No glowing filled pills or capsule-shaped category/status controls.
- Large headings carry identity; card headings remain smaller and aligned.
- Do not flatten headings, prices, labels and sections into one visual weight.
- Body minimum 16px. Text width about 65 characters. Mobile gutters at least20px.
- One global header. Local section links can remain as a compact in-flow row.
- One shared footer. Remove repeated product identity/footer blocks.
- Main navigation: AI Receptionist, Websites, About, Contact. Lab is under Websites.
- Native details/summary for secondary offer and FAQ detail. Keep material terms visible.
- Keep essential prices, minimum commitments and ownership clear. Do not invent approved promises.
- Use direct natural language. Remove hype, internal process language, generic
  sales narration and repeated explanations. Do not add statistics merely as proof.

## Page responsibilities

- Home: two clear services, a useful demo, short studio explanation and contact.
- Receptionist: hear the demo, understand plan-dependent coverage, compare plans, enquire.
- Websites: view actual demos, compare three managed plans, enquire. Secondary ownership and care detail.
- Lab: optional visual design gallery. Brief intro, actual previews, obvious return to Websites.
- Local SEO and Care: concise secondary services, existing approved prices/terms, contact.
- Industry/location pages: retain useful unique content and route visitors to the demo/plan details.
- Legal/scope pages: consistent readable layout. Preserve substantive terms.
- Demo/sample pages: preserve the demonstrated design; use unobtrusive consistent return controls.

## Implementation contract

Root owner adds `/brand.css` and canonical navigation/footer partial changes.
Agents do not edit shared partials, shared CSS or the injector. Root reinjects once.
Marketing pages use `body data-callmeie-page="marketing"`; legal/scope use
`data-callmeie-page="document"`. Do not set these markers on distinct demo/sample pages.
Link `/brand.css` last in head. Do not hide overflow to make a broken layout pass.
Existing form IDs, action routes, consent handling and billing URLs remain functional.

## Motion and 3D

Use restrained button/gallery transitions and a short entrance that leaves content
visible without JavaScript and with reduced motion. A 3D phone is optional only
if it helps the receptionist demonstration. No mandatory WebGL or long scroll scene.

## Verification

Inventory every tracked public HTML route. Check actual renders at375/390px mobile,
768px tablet and1280px desktop. Reuse site-qa mobile overflow, invisible-content,
stuck-transform and layout-push checks; use WebKit as well as Chromium. Inspect
screenshots for every route; distinguish redirect/system files from content pages.
Check tables, headings, nav, modal and form alignment. Keep captures outside Git.
ACTIVE-CHECKPOINT.md owns current local versus published status. A technical pass
alone is not design acceptance.
