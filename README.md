# MarkLee-website

Personal website for **Mark T. Lee** — Chief Legal Officer / General Counsel.
Built by Sarreal Consulting. Static, multi-page HTML/CSS — no build step.

## Pages
- `index.html` — Home. Two-column layout: skills (practice areas) + selected experience on the left;
  photo + About Me upper right (per Mark's direction).
- `practice-areas.html` — Full list of practice areas (SEO keyword coverage).
- `experience.html` — Full professional history.
- `licenses.html` — Bar admissions, real estate / insurance / securities licenses, affiliations, education.
- `contact.html` — Email, phone, LinkedIn.

## Structure
- `css/style.css` — single stylesheet (deep navy + muted gold; Outfit/Inter; mobile-first).
- `js/main.js` — footer year + mobile nav toggle.
- `assets/` — images. **Add Mark's headshot at `assets/mark-lee.jpg`**, then replace the placeholder
  `<div class="photo photo-placeholder">` in `index.html` with the commented `<img class="photo">` tag above it.
- `robots.txt`, `sitemap.xml` — SEO. **Replace `https://www.marklee.example/` with the live domain** in
  these files and in the `<link rel="canonical">` / Open Graph tags once the domain is chosen.

## SEO
Each page has a unique `<title>`, `<meta name="description">`, and `<meta name="keywords">` covering
practice areas, licensures, jurisdictions, roles, and industries. `index.html` includes JSON-LD
(`schema.org/Attorney`) with `knowsAbout` (practice areas) and `hasCredential` (licenses).

## Local preview
Open `index.html` in a browser, or: `python3 -m http.server 8000` then visit http://localhost:8000.

## To do before launch
- [ ] Confirm name spelling: "Mark" (résumé) vs "Marc".
- [ ] Add headshot.
- [ ] Choose domain; update canonical URL, Open Graph, `robots.txt`, `sitemap.xml`.
- [ ] Decide hosting/deploy.
