# MarkLee-website

Personal website for **Mark T. Lee** — Chief Legal Officer / General Counsel.
Built by Sarreal Consulting. Static, multi-page HTML/CSS — no build step.

## Pages
- `index.html` — Home. Two-column layout: skills (practice areas) + selected experience on the left;
  photo + About Me upper right (per Mark's direction).
- `practice-areas/` — Practice-areas section with a **left-hand menu** and one SEO-optimized page per
  area (`index.html` overview + 11 area pages). Designed so each area ranks for its category and can
  grow its own content.
- `experience.html` — Full professional history.
- `licenses.html` — Bar admissions, real estate / insurance / securities licenses, affiliations, education.
- `contact.html` — Email, phone, LinkedIn.

## Structure
- `css/style.css` — single stylesheet (deep navy + muted gold; Outfit/Inter; mobile-first).
- `js/main.js` — footer year + mobile nav toggle.
- `assets/` — images (headshot at `assets/MarkLee.jpeg`).
- `scripts/generate_practice_areas.py` — **generator** for the practice-area pages. Edit the `AREAS`
  data (titles, keywords, content) in that file and re-run `python3 scripts/generate_practice_areas.py`
  to regenerate `practice-areas/`. Output is plain static HTML — no build step is needed to serve the site.
- `robots.txt`, `sitemap.xml` — SEO. **Replace `https://www.marklee.example/` with the live domain** in
  these files and in the `<link rel="canonical">` / Open Graph tags once the domain is chosen.

## SEO
Every page has a unique `<title>`, `<meta name="description">`, and `<meta name="keywords">`. The
practice-area pages each target one category (capital markets, consumer lending, SEC reporting, etc.)
with category-specific keywords to capture the maximum search coverage. `index.html` includes JSON-LD
(`schema.org/Attorney`) with `knowsAbout` (practice areas) and `hasCredential` (licenses).
**Note:** `sitemap.xml` currently lists the top-level pages — add the new `practice-areas/*` URLs when
the domain is finalized.

## Local preview
Open `index.html` in a browser, or: `python3 -m http.server 8000` then visit http://localhost:8000.

## Deployment
Hosted on **GitHub Pages** from the `main` branch (root). Any push to `main` auto-deploys.
Live: https://jsarreal.github.io/MarkLee-website/

To attach a custom domain later: add a `CNAME` file (containing the domain) at the repo root, set the
custom domain in repo **Settings → Pages**, point DNS at GitHub Pages, then update the canonical/OG tags,
`robots.txt`, and `sitemap.xml` from the `www.marklee.example` placeholder to the real domain.

## To do before launch
- [ ] Choose domain; update canonical URL, Open Graph, `robots.txt`, `sitemap.xml` (incl. practice-area URLs).
- [ ] Expand practice-area content as desired (edit `scripts/generate_practice_areas.py`, re-run).
- [ ] Decide hosting/deploy.
