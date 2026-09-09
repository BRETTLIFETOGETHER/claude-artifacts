---
name: brochure-builder
description: Build professionally designed HTML brochures, sales pages, and clickable catalog editions in LifeTogether's established navy/gold editorial design system. Use whenever Brett asks for a brochure, one-pager, sales page, subscription page, directory, "clickable edition," or any polished HTML deliverable for a product line.
---

# Brochure Builder

Every LifeTogether brochure follows one established design system. Consistency across product lines is the point — a new brochure should look like a sibling of the last one.

## Design system

- Palette: dark navy base with gold accents
- Typography: Playfair Display for display and headlines, Cormorant Garamond for serif body and accents
- Layout: editorial, directory-style — a well-set print catalog, not a SaaS landing page. No card grids.
- Generous whitespace, ruled section dividers, small-caps labels, numbered directory entries

## Technical rules (hard requirements)

- Single self-contained HTML file; no frameworks
- No template literals in JavaScript — use string concatenation
- Verify bracket and brace balance before delivering
- Save to /mnt/user-data/outputs/ and present the file
- Must read well on mobile first — Brett reviews on his phone

## Write it as a sales page, not a list

A brochure has a named buyer making a decision (a Christian business leader deciding whether to bring marketplace training to a 10–1,000 person company; an advisor deciding whether to join a pilot). Open with the decision, position the offer, then present the library as evidence. Real scale numbers (categories, titles, formats) are part of the pitch — use the honest counts.

## Clickable editions

When Brett asks for a "clickable edition," build drill-down navigation:
campaign title/subtitle → series sessions → daily devotional titles → full campaign kit (student/youth edition, sermon series, women's edition, leader training, and the rest).

Keep all data in JavaScript structures inside the single file, render views by concatenation, and provide a back path at every level.

## Master-directory pattern

For large catalogs, lead with a Top 10 highlight section (top categories × top titles), then the full directory with anchors into every part. Displayed counts must match the true catalog math.
