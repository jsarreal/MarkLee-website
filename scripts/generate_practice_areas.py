#!/usr/bin/env python3
"""Generate the practice-area pages with a shared left-hand menu.

Each practice area is its own SEO-optimized static page so it can rank for that
category and grow its own content. Edit AREAS below and re-run:

    python3 scripts/generate_practice_areas.py

Output: practice-areas/index.html + practice-areas/<slug>.html (static; no build step to serve).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "practice-areas")

# Each area: slug, name (menu/short), title, description, keywords, lead, body (HTML).
AREAS = [
    {
        "slug": "capital-markets",
        "name": "Capital Markets",
        "title": "Capital Markets Counsel — Mark Lee | Credit Facilities & Securitization",
        "description": "Capital markets legal experience: negotiating and documenting financing, secondary-market, and credit transactions — multi-billion-dollar credit facilities, master repurchase agreements, and mortgage securitization.",
        "keywords": "capital markets attorney, credit facility counsel, master repurchase agreement, loan and security agreement, secondary market, mortgage securitization, warehouse lending, structured finance, fintech capital markets",
        "lead": "Negotiating and documenting financing, secondary-market, and credit transactions for lenders and high-growth platforms.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Negotiated and drafted multi-billion-dollar credit facilities, lease, financing, and corporate agreements.</li>
          <li>Documented stock purchase agreements, loan &amp; security agreements, and master repurchase agreements.</li>
          <li>Drafted whole-loan sale and servicing agreements, mortgage securitization documents, and commercial-paper conduit agreements for the sale and securitization of over $20 billion in mortgages.</li>
        </ul>""",
    },
    {
        "slug": "consumer-lending",
        "name": "Consumer Lending",
        "title": "Consumer Lending Counsel — Mark Lee | Mortgage & Fintech Compliance",
        "description": "Consumer lending legal experience representing lenders in loan origination, servicing, and compliance — Reg Z, FCRA, TCPA, ECOA, UDAAP, HMDA, and AML/KYC across multi-state operations.",
        "keywords": "consumer lending attorney, mortgage compliance counsel, Regulation Z, FCRA, TCPA, ECOA, fair lending, UDAAP, HMDA, AML, KYC, loan origination, loan servicing, multi-state lending licensing, fintech lending",
        "lead": "Representing lenders in loan origination, servicing, and compliance across regulated, multi-state mortgage and consumer-lending businesses.",
        "body": """
        <h2>Regulatory coverage</h2>
        <ul>
          <li>Regulation Z (TILA), FCRA, TCPA, ECOA (fair lending), UDAAP, and HMDA.</li>
          <li>USA PATRIOT Act, anti-money-laundering, and know-your-customer requirements.</li>
          <li>Treasury regulations governing foreign assets.</li>
        </ul>
        <h2>Experience</h2>
        <ul>
          <li>Led legal and compliance for regulated mortgage, down-payment-assistance, and fintech lending platforms.</li>
          <li>Oversaw origination, servicing, and marketing-compliance functions across multiple states.</li>
        </ul>""",
    },
    {
        "slug": "corporate-governance",
        "name": "Corporate Governance",
        "title": "Corporate Governance &amp; Corporate Secretary — Mark Lee",
        "description": "Corporate governance counsel: advising boards and management on governance, corporate-secretary duties, equity and ERISA plans, fundraising, and ethical best practices.",
        "keywords": "corporate governance attorney, corporate secretary, board advisory, ERISA plan administration, equity incentive plans, fundraising counsel, ethics and compliance, startup governance, board of directors counsel",
        "lead": "Advising boards and management on governance, corporate-secretary duties, and ethical best practices.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Advised boards of directors on launching new ventures, governance, fundraising, and corporate transactions.</li>
          <li>Served as Corporate Secretary across multiple companies.</li>
          <li>Administered equity-incentive, stock-option, and ERISA plans.</li>
        </ul>""",
    },
    {
        "slug": "regulatory-compliance",
        "name": "Regulatory &amp; Compliance",
        "title": "Regulatory &amp; Compliance Counsel — Mark Lee | Multi-State",
        "description": "Regulatory and compliance counsel on federal, state, and local laws for regulated lending, real estate, and fintech businesses — including government affairs and marketing-compliance review.",
        "keywords": "regulatory compliance attorney, financial services compliance, multi-state compliance, government affairs, legislative tracking, marketing compliance review, fintech regulation, lending compliance counsel",
        "lead": "Building and running compliance programs that satisfy federal, state, and local requirements across multi-state operations.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Provided legal support for all regulatory and compliance functions of regulated lending businesses.</li>
          <li>Conducted government-affairs outreach, tracked legislative developments, and oversaw lobbying activity.</li>
          <li>Performed marketing and sales-collateral reviews to ensure compliance with applicable laws.</li>
        </ul>""",
    },
    {
        "slug": "data-protection-privacy",
        "name": "Data Protection &amp; Privacy",
        "title": "Data Privacy Counsel — Mark Lee | CCPA, CPRA &amp; Data Security",
        "description": "Data protection and privacy counsel: building privacy programs, policies, and terms of use to implement CCPA, CPRA, and federal data-security requirements for e-commerce and fintech platforms.",
        "keywords": "data privacy attorney, CCPA compliance, CPRA, privacy policy, terms of use, data security, e-commerce privacy, consumer data protection, fintech privacy counsel",
        "lead": "Developing privacy programs, policies, and terms of use that implement state and federal data-protection requirements.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Implemented and maintained multiple privacy policies and terms of use.</li>
          <li>Ensured compliance with applicable data-security and privacy laws, including the CCPA and CPRA.</li>
          <li>Supported e-commerce initiatives and AI product launches with privacy-by-design review.</li>
        </ul>""",
    },
    {
        "slug": "employment-hr",
        "name": "Employment &amp; HR",
        "title": "Employment &amp; HR Counsel — Mark Lee | Employment Law Compliance",
        "description": "Employment and HR legal experience: drafting compensation plans, offer and separation agreements, advising on employment-law compliance, and overseeing HR investigations.",
        "keywords": "employment law attorney, HR counsel, compensation plans, offer letters, separation agreements, employment compliance, workplace investigations, in-house employment counsel",
        "lead": "Advising on employment-law compliance and drafting the HR documents that growing companies depend on.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Drafted compensation plans, offer letters, and separation agreements.</li>
          <li>Rendered employment-law advice and oversaw investigations initiated by HR teams.</li>
        </ul>""",
    },
    {
        "slug": "insurance",
        "name": "Insurance",
        "title": "Insurance Counsel — Mark Lee | Coverage &amp; Claims",
        "description": "Insurance experience evaluating and binding traditional coverages and administering claims; licensed California insurance professional.",
        "keywords": "insurance counsel, coverage evaluation, claims administration, California insurance license, corporate insurance attorney, risk management",
        "lead": "Evaluating and binding traditional coverages and administering claims.",
        "body": """
        <h2>Credential</h2>
        <p>California Insurance License #0I21214. See <a href="../licenses.html">Licenses &amp; admissions</a>.</p>""",
    },
    {
        "slug": "intellectual-property",
        "name": "Intellectual Property",
        "title": "Intellectual Property Counsel — Mark Lee | Trademarks, Patents &amp; Copyright",
        "description": "Intellectual property experience prosecuting and administering patents, trademarks, and copyrights, including software copyright and trademark portfolio management.",
        "keywords": "intellectual property attorney, trademark prosecution, patent prosecution, copyright, software copyright, IP portfolio management, technology IP counsel",
        "lead": "Prosecuting and administering patents, trademarks, and copyrights — including software copyright and trademark portfolios.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Responsible for prosecution of company trademark portfolios and copyrighted software.</li>
          <li>Administered intellectual-property portfolios across multiple companies.</li>
        </ul>""",
    },
    {
        "slug": "investment-funds",
        "name": "Investment Fund Formation",
        "title": "Investment Fund Formation &amp; Compliance — Mark Lee | ERA &amp; RIA",
        "description": "Investment fund formation and compliance counsel for ERA and RIA entities, including structuring alternative asset funds with over $1 billion in assets.",
        "keywords": "investment fund formation attorney, ERA counsel, RIA compliance, alternative asset funds, fund structuring, private funds, life settlements, premium finance, investment adviser compliance",
        "lead": "Counseling exempt reporting advisers (ERA) and registered investment advisers (RIA), and structuring alternative asset funds.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Counseled both ERA and RIA entities on formation and compliance.</li>
          <li>Established alternative asset funds in Ireland and Luxembourg with over $1 billion in assets.</li>
          <li>Advised on alternative asset classes including life settlements, premium finance, installment loans, credit-card portfolios, and medical receivables.</li>
        </ul>""",
    },
    {
        "slug": "mergers-acquisitions",
        "name": "Mergers &amp; Acquisitions",
        "title": "Mergers &amp; Acquisitions Counsel — Mark Lee | Public &amp; Private M&amp;A",
        "description": "Mergers and acquisitions experience representing public and private companies, including a ~$340 million public-REIT acquisition in a cash-and-stock transaction.",
        "keywords": "mergers and acquisitions attorney, M&A counsel, public company acquisition, private company M&A, REIT acquisition, cash and stock transaction, deal counsel, corporate transactions",
        "lead": "Representing public and private companies in mergers and acquisitions, from diligence through close.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Negotiated and closed the acquisition of Aames Investment Corporation, a publicly traded REIT, in a cash-and-stock transaction valued at approximately $340 million.</li>
          <li>Advised on corporate transactions and new business ventures for venture-backed and public companies.</li>
        </ul>""",
    },
    {
        "slug": "sec-reporting",
        "name": "SEC Reporting",
        "title": "SEC Reporting &amp; Securities Counsel — Mark Lee | '33 &amp; '34 Act",
        "description": "SEC reporting and securities-law experience: preparing and filing registration statements under the Securities Act of 1933 and periodic reports under the Securities Exchange Act of 1934.",
        "keywords": "SEC reporting attorney, securities counsel, registration statements, Securities Act of 1933, Securities Exchange Act of 1934, periodic reports, public company reporting, securities compliance, Regulation D offerings",
        "lead": "Preparing registration statements and periodic reports and monitoring securities-law compliance.",
        "body": """
        <h2>Experience</h2>
        <ul>
          <li>Prepared registration statements under the Securities Act of 1933 and periodic reports under the Securities Exchange Act of 1934.</li>
          <li>Monitored compliance with federal and state securities laws.</li>
          <li>Represented issuers in Regulation D offerings, venture financings, and private placements.</li>
        </ul>""",
    },
]

NAV_ITEMS = [
    ("../index.html", "Home", ""),
    ("index.html", "Practice Areas", "active"),
    ("../experience.html", "Experience", ""),
    ("../licenses.html", "Licenses", ""),
    ("../contact.html", "Contact", ""),
]


def _cls_attr(cls):
    return ' class="' + cls + '"' if cls else ""


def site_header():
    links = "\n".join(
        '        <li><a href="' + href + '"' + _cls_attr(cls) + '>' + label + '</a></li>'
        for href, label, cls in NAV_ITEMS
    )
    return f"""  <header class="site-header">
    <nav class="nav">
      <a class="brand" href="../index.html">Mark Lee<span>.</span></a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>
      <ul class="nav-links">
{links}
      </ul>
    </nav>
  </header>"""


def side_menu(active_slug):
    overview_cls = _cls_attr("active" if active_slug is None else "")
    items = ['        <li><a href="index.html"' + overview_cls + '>Overview</a></li>']
    for a in AREAS:
        cls = _cls_attr("active" if a["slug"] == active_slug else "")
        items.append('        <li><a href="' + a["slug"] + '.html"' + cls + '>' + a["name"] + '</a></li>')
    inner = "\n".join(items)
    return f"""      <nav class="pa-nav" aria-label="Practice areas">
        <h2>Practice areas</h2>
        <ul>
{inner}
        </ul>
      </nav>"""


SITE_FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div>&copy; <span id="year"></span> Mark Lee &middot; Chief Legal Officer &amp; General Counsel</div>
      <div>
        <a href="mailto:markleesfo@gmail.com">markleesfo@gmail.com</a> &middot;
        <a href="https://www.linkedin.com/in/markleeSFO">LinkedIn</a>
      </div>
    </div>
  </footer>
  <script src="../js/main.js"></script>"""


def page(title, description, keywords, active_slug, content_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>
{site_header()}

  <main class="container">
    <div class="pa-layout">
{side_menu(active_slug)}
      <div class="pa-content">
{content_html}
      </div>
    </div>
  </main>

{SITE_FOOTER}
</body>
</html>
"""


def overview_content():
    cards = "\n".join(
        f'          <div class="card"><h3><a href="{a["slug"]}.html">{a["name"]}</a></h3><p>{a["lead"]}</p></div>'
        for a in AREAS
    )
    return f"""        <p class="eyebrow">Capabilities</p>
        <h1>Practice areas</h1>
        <p class="lead">Two decades of in-house and advisory legal leadership across regulated mortgage,
          consumer lending, fintech, and proptech businesses &mdash; spanning the full corporate, transactional,
          and compliance lifecycle. Select an area to learn more.</p>
        <div class="cards">
{cards}
        </div>
        <div class="pa-cta">
          <a class="btn btn-primary" href="../contact.html">Discuss an engagement</a>
        </div>"""


def area_content(a):
    return f"""        <p class="eyebrow">Practice area</p>
        <h1>{a["name"]}</h1>
        <p class="lead">{a["lead"]}</p>
{a["body"]}
        <div class="pa-cta">
          <a class="btn btn-primary" href="../contact.html">Discuss a {a["name"].replace("&amp;", "and")} engagement</a>
          <a class="btn btn-ghost" href="index.html">All practice areas</a>
        </div>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    # Overview
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(page(
            "Practice Areas — Mark Lee | General Counsel &amp; Compliance",
            "Mark Lee's practice areas: capital markets, consumer lending, corporate governance, "
            "regulatory and compliance, data privacy, employment, insurance, intellectual property, "
            "investment fund formation, mergers and acquisitions, and SEC reporting.",
            "general counsel practice areas, capital markets, consumer lending, corporate governance, "
            "regulatory compliance, data privacy, employment law, insurance, intellectual property, "
            "investment funds, mergers and acquisitions, SEC reporting, fractional general counsel",
            None,
            overview_content(),
        ))
    # Each area
    for a in AREAS:
        with open(os.path.join(OUT, a["slug"] + ".html"), "w") as f:
            f.write(page(a["title"], a["description"], a["keywords"], a["slug"], area_content(a)))
    print(f"Generated {len(AREAS) + 1} pages in {OUT}")


if __name__ == "__main__":
    main()
