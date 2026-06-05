#!/usr/bin/env python3
"""build_location_page.py — assemble a /receptionist/<location>.html landing page.

Long-tail-local SEO (see optimisation-audit/longtail_local.py): callmeie.ie has
VERTICAL pages (dental/salon/...) but no LOCATION pages. A new low-authority domain
wins local long-tail ("AI receptionist Limerick") before head terms. This builds
those pages WITHOUT thin-doorway risk: the chrome (head scaffold, cohesion strip/
footer/chatbot, styles) is cloned byte-identical from a donor receptionist page, and
the BODY is authored, genuinely-unique local content supplied per location in
locations/<slug>.json (>=300 unique words each — Google penalises templated
doorways).

The cohesion blocks are auto-generated DO-NOT-EDIT regions; we copy them verbatim
from the donor and let scripts/inject-cohesion.py re-normalise them afterwards.

USAGE:
  python scripts/build_location_page.py --location limerick
  python scripts/build_location_page.py --location limerick --donor dental.html
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEPTIONIST = HERE.parent
LOCATIONS = RECEPTIONIST / "locations"
SITE = "https://callmeie.ie"


def extract(text: str, start_marker: str, end_marker: str | None) -> str:
    """Slice a verbatim block from the donor page by comment markers (inclusive)."""
    i = text.index(start_marker)
    if end_marker is None:
        return text[i:]
    j = text.index(end_marker, i) + len(end_marker)
    return text[i:j]


def jsonld(loc: dict, faqs: list[dict]) -> str:
    name = loc["name_long"]
    city = loc["city"]
    graph = [
        {
            "@type": "Service",
            "name": f"AI Phone Receptionist in {city}",
            "serviceType": "AI phone receptionist / call answering service",
            "provider": {
                "@type": "LocalBusiness",
                "@id": f"{SITE}/receptionist/#business",
                "name": "CallMeIE",
                "url": f"{SITE}/receptionist/",
                "telephone": "+353-61-788-120",
                "priceRange": "€€",
                "address": {"@type": "PostalAddress", "addressLocality": loc["locality"],
                            "addressRegion": loc["region"], "addressCountry": "IE"},
                "areaServed": [{"@type": "City", "name": a} for a in loc["area_served"]],
            },
            "description": loc["meta_description"],
            "areaServed": {"@type": "City", "name": city},
            "url": f"{SITE}/receptionist/{loc['slug']}.html",
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/receptionist/"},
                {"@type": "ListItem", "position": 2, "name": city,
                 "item": f"{SITE}/receptionist/{loc['slug']}.html"},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": f["q"],
                 "acceptedAnswer": {"@type": "Answer", "text": f["a_plain"]}}
                for f in faqs
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def render_sections(sections: list[dict]) -> str:
    out = []
    for s in sections:
        out.append(f"""  <section class="editorial" id="{s['id']}" aria-labelledby="{s['id']}-title">
    <div class="section-head">
      <div class="section-num">{s['num']}</div>
      <h2 id="{s['id']}-title" class="section-title">{s['title']}</h2>
    </div>
    <p class="section-dek">{s['dek']}</p>
{s['body']}
  </section>""")
    return "\n\n".join(out)


def render_faq(faqs: list[dict]) -> str:
    items = []
    for i, f in enumerate(faqs, 1):
        items.append(f"""      <details>
        <summary>
          <span class="faq-num">{i:02d}</span>
          <span>{f['q']}</span>
          <span class="faq-toggle"></span>
        </summary>
        <div class="faq-body">
{f['a_html']}
        </div>
      </details>""")
    return "\n\n".join(items)


def build(location_slug: str, donor_name: str) -> Path:
    loc = json.loads((LOCATIONS / f"{location_slug}.json").read_text(encoding="utf-8"))
    loc["slug"] = location_slug
    donor = (RECEPTIONIST / donor_name).read_text(encoding="utf-8")

    # Verbatim chrome cloned from the donor (cohesion = auto-generated DO-NOT-EDIT).
    strip = extract(donor, "<!-- COHESION:STRIP-START -->", "<!-- COHESION:STRIP-END -->")
    coh_footer = extract(donor, "<!-- COHESION:FOOTER-START -->", "<!-- COHESION:FOOTER-END -->")
    chatbot = extract(donor, "<!-- COHESION:CHATBOT-START", None)  # to EOF

    url = f"{SITE}/receptionist/{location_slug}.html"
    city = loc["city"]
    # Honesty: only the home base (Limerick) gets a "{city}: 061..." label. Other cities
    # are served remotely on the same real line — neutral framing, never a faked local number.
    is_home = loc.get("is_home", False)
    phone_lbl = f"{city}: +353 61 788 120" if is_home else "Live line · +353 61 788 120"
    line_lbl = f"Live {city} line" if is_home else "Live line"
    footer_line_lbl = f"{city} line" if is_home else "Direct line"
    verticals_nav = " ·\n      ".join(
        f'<a href="{v["href"]}">{v["label"]}</a>' for v in loc["vertical_links"])

    html = f"""<!doctype html>
<html lang="en-IE">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{loc['title']}</title>
<meta name="description" content="{loc['meta_description']}" />
<link rel="canonical" href="{url}" />
<link rel="icon" type="image/png" sizes="512x512" href="/favicon.png" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="apple-touch-icon" href="/favicon.png" />
<!-- Geo / Local SEO -->
<meta name="geo.region" content="{loc.get('geo_region', 'IE-LK')}" />
<meta name="geo.placename" content="{city}, Ireland" />
<meta name="geo.position" content="{loc['lat']};{loc['lng']}" />
<meta name="ICBM" content="{loc['lat']}, {loc['lng']}" />

<!-- Open Graph / Social -->
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:title" content="{loc['og_title']}" />
<meta property="og:description" content="{loc['og_description']}" />
<meta property="og:locale" content="en_IE" />
<meta property="og:site_name" content="CallMeIE" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{loc['og_title']}" />
<meta name="twitter:description" content="{loc['og_description']}" />

<!-- Structured Data -->
<script type="application/ld+json">
{jsonld(loc, loc['faq'])}
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/receptionist/styles.css">
  <link rel="stylesheet" href="/_partials/cohesion.css">
  <meta property="fb:pages" content="1105012356028968">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"CallMeIE Technologies","url":"https://callmeie.ie/","image":"https://callmeie.ie/og-image.png","telephone":"+353-61-788-120","priceRange":"€€","address":{{"@type":"PostalAddress","addressLocality":"{loc['locality']}","addressRegion":"{loc['region']}","addressCountry":"IE"}},"geo":{{"@type":"GeoCoordinates","latitude":{loc['lat']},"longitude":{loc['lng']}}},"areaServed":{{"@type":"City","name":"{city}"}}}}</script>
</head>
<body>

<a class="cmt-skip-link" href="#main">Skip to main content</a>

{strip}

<!-- COHESION:BREADCRUMB-START section="AI Receptionist" section_url="/receptionist/" page="{city}" -->
<!-- (auto-generated by scripts/inject-cohesion.py — DO NOT EDIT) -->
<nav class="callmeie-breadcrumb" aria-label="breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/receptionist/">AI Receptionist</a></li>
    <li aria-current="page">{city}</li>
  </ol>
</nav>
<!-- COHESION:BREADCRUMB-END -->

<div class="page">

  <header class="topbar" role="banner">
    <a class="wordmark" href="/" aria-label="CallMeIE — home">
      <span class="wordmark__dot" aria-hidden="true"></span>CallMeIE
    </a>
    <div class="topbar__right">
      <span class="topbar__meta">{loc['topbar_meta']}</span>
      <a class="topbar__cta" href="tel:+35361788120">{phone_lbl}</a>
    </div>
  </header>

  <div class="masthead-strip" aria-hidden="true">
    <span>{city} Edition</span>
    <span>Vol. I — MMXXVI</span>
    <span>24/7 · Irish accent · From €149/mo</span>
    <span>{city} · Ireland</span>
  </div>

  <div class="vertical-switch" aria-label="Switch vertical">
    <span>{city} by trade</span>
    <span>
      {verticals_nav} ·
      <a href="/">All verticals →</a>
    </span>
  </div>

  <!-- HERO -->
  <section class="hero" id="top" aria-labelledby="hero-title">
    <div class="hero__kicker">{loc['hero']['kicker']}</div>
    <h1 id="hero-title" class="hero__headline">{loc['hero']['headline']}</h1>
    <p class="hero__sub">{loc['hero']['sub']}</p>

    <span class="demo-number__label">{line_lbl} · Answers 24 hours</span>
    <a class="demo-number" href="tel:+35361788120" aria-label="Ring the live line">+353 61 788 120</a>
    <span class="demo-number__caption">Ring it now — hear exactly what your callers would hear.</span>

    <div class="hero__actions">
      <a class="btn-primary" href="tel:+35361788120">Hear it live · sign up</a>
      <a class="btn-secondary" href="/onboard.html?location={location_slug}">Start onboarding →</a>
    </div>
  </section>

{render_sections(loc['sections'])}

  <!-- FAQ -->
  <section class="editorial" id="faq" aria-labelledby="faq-title">
    <div class="section-head">
      <div class="section-num">§ FAQ</div>
      <h2 id="faq-title" class="section-title">{city} questions we actually get</h2>
    </div>
    <p class="section-dek">{loc['faq_dek']}</p>

    <div class="faq-list">
{render_faq(loc['faq'])}
    </div>
  </section>

</div><!-- /.page -->

<!-- FINAL CTA -->
<section class="final-cta" aria-labelledby="final-cta-title">
  <div class="page">
    <div class="final-cta__kicker">{loc['final_cta']['kicker']}</div>
    <h2 id="final-cta-title" class="final-cta__headline">{loc['final_cta']['headline']}</h2>
    <a class="final-cta__number" href="tel:+35361788120">{phone_lbl}</a>
    <p class="final-cta__sub">{loc['final_cta']['sub']}</p>
    <a class="final-cta__secondary" href="/onboard.html?location={location_slug}">Start onboarding →</a>
  </div>
</section>

<footer role="contentinfo">
  <div class="page">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>CallMeIE · {city}</h4>
        <p>AI phone receptionist for {city} businesses. Built &amp; operated from {loc['locality']}, {loc['region']}, Ireland.</p>
        <p>Stack: Vapi · Twilio · Google Calendar · FastAPI.</p>
        <p>Email: <a href="mailto:hello@callmeie.ie" class="mono-val">hello@callmeie.ie</a></p>
        <p>{footer_line_lbl}: <span class="mono-val">+353 61 788 120</span></p>
      </div>
      <div class="footer-col">
        <h4>By trade in {city}</h4>
        <ul>
          {''.join(f'<li><a href="{v["href"]}">{v["label"]}</a></li>' for v in loc['vertical_links'])}
          <li><a href="/">All verticals</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul>
          <li><a href="#handles">Capabilities</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="/onboard.html?location={location_slug}">Onboarding</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="privacy.html">Privacy notice</a></li>
          <li><a href="terms.html">Terms of service</a></li>
          <li><a href="about.html">About CallMeIE</a></li>
          <li><a href="/receptionist/blog/">Blog</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <span class="footer-legal__wordmark">CALLMEIE &mdash; {city.upper()}</span>
      <span>© 2026 CallMeIE. All rights reserved.</span>
      <span>Built in Limerick &nbsp;·&nbsp; {phone_lbl}</span>
    </div>
  </div>
</footer>

{coh_footer}

{chatbot}"""

    out = RECEPTIONIST / f"{location_slug}.html"
    out.write_text(html, encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--location", required=True, help="slug; reads locations/<slug>.json")
    ap.add_argument("--donor", default="dental.html", help="receptionist page to clone chrome from")
    a = ap.parse_args()
    out = build(a.location, a.donor)
    words = len(re.sub(r"<[^>]+>", " ", out.read_text(encoding="utf-8")).split())
    print(f"built {out.name}  (~{words} words total incl. chrome)")
    print(f"  next: validate render, then run scripts/inject-cohesion.py + add to sitemap.xml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
