# CallMeIE website consolidation

## Scope and source

Local preview requested by Adam on 10 October 2026. Base is published commit
657861961e8297853a2c6e62c6c453c56488f159. No publication is authorised in this task.
Keep the 7/8 October seller, privacy, coverage-hours and form corrections.

## Visual thesis

Warm paper, clear ink and quiet indigo. One coherent Irish business site with
generous space, short headings and useful product examples.

Reference: existing `_partials/cohesion.css` identity, installed Apple design
reference for restraint, and design-hub section templates for layout and CTA.
This task supersedes older per-product burgundy/orange themes and mono labels.

## Shared system

- Paper #f8f5f0, alternate #efe9de, ink #1c1f24, muted #615d55, line #d8cfc1.
- One action accent: indigo #1d3557. Product photos and demo artwork can vary.
- Fraunces for short headings. Inter for body, navigation, prices and forms.
- No third marketing font, all-caps hero, long italic heading or numbered narration.
- Body minimum 16px. Text width about 65 characters. Mobile gutters at least20px.
- One global header. Local section links can remain as a compact in-flow row.
- One shared footer. Remove repeated product identity/footer blocks.
- Main navigation: AI Receptionist, Websites, About, Contact. Lab is under Websites.
- Native details/summary for secondary offer and FAQ detail. Keep material terms visible.
- Keep essential prices, minimum commitments and ownership clear. Do not invent approved promises.

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
