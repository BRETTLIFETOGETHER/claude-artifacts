---
name: LifeTogether Brochure Builder
description: Build or extend a LifeTogether ministry brochure as single-file HTML in the canonical navy/gold editorial system. Use whenever asked to create, redesign, restyle, or add to a LifeTogether brochure, catalog, or marketing one-pager.
---

# LifeTogether Brochure Builder

Use this any time the request is to build, redesign, or extend a brochure, catalog page, or marketing one-pager for LifeTogether Ministries or any of its product lines (Pastor's Library, Small Group Ministry Platform, Generosity Ministry, Adult Bible Fellowship, Flourishing Intelligence, LifeTogether Experiences, or any new line).

## Canonical Design Tokens (default palette: Navy & Gold)

Use these exact values unless the person explicitly asks for a different named palette (Ivory/Jewel-Tone, Moss/Brass, Heritage/Parchment, Classic Blue, Blueprint/Construction, Near-Black/Ember). Do not invent new hex values for "navy/gold" — this exact set is canonical:

```css
:root{
  --navy:#101a33; --navy-2:#16223f;
  --gold:#b8934e; --gold-light:#d9bc82;
  --cream:#f7f3ea; --hair:rgba(184,147,78,.35);
  --muted:rgba(247,243,234,.82); --muted2:rgba(247,243,234,.6);
  --ink-bright:#fbf7ee;
}
body{ background:var(--navy); color:var(--cream); font-family:'Cormorant Garamond',serif; }
h1,h2,h3{ font-family:'Playfair Display',serif; font-weight:600; color:var(--ink-bright); }
```

Typography: Playfair Display (headers), Cormorant Garamond (body), Lato (eyebrows/labels/small caps). Import from Google Fonts.

## Layout Conventions (non-negotiable house style)

- **Editorial directory style, never card grids.** Sections read like a designed magazine/annual report — numbered or roman-numeral entries, hairline dividers, pull quotes — not boxed feature cards.
- Container max-width ~960–980px, generous padding, hairline rule dividers between sections (`rgba(184,147,78,.35)`).
- Eyebrow labels in Lato, uppercase, letter-spaced, small.
- Stat bars (credibility numbers like years/church count/titles) belong near the top, right under the hero.
- Always run `view /mnt/skills/public/frontend-design/SKILL.md` before writing code, per house process — this skill supplements it, not replaces it.

## Standard Section Pattern

Most brochures follow this shape, adapted per product:
1. Hero — eyebrow, headline, one-line subtitle, deck paragraph
2. Stat bar — 3 credibility numbers
3. The problem/hook — reframes what the person already has as an asset
4. Differentiation — why this beats the generic alternative (prose or editorial comparison, not a card grid)
5. Deliverables — numbered list of concrete things the buyer walks away with
6. Process — 3–4 real steps, in order
7. Tiers/ways to begin — if it's a sellable offer
8. CTA — one clear next step

## After Building: Log It

Every time this skill produces a new brochure, output a short catalog entry at the end of the response, in this exact format, so it can be pasted into the Brochure Library index:

```
<div class="item"><div class="name">[FILE NAME]</div><div class="meta">Palette: [PALETTE] · [DATE]</div><div class="desc">[ONE-LINE DESCRIPTION]</div></div>
```

This is the fix for brochures getting built and then lost — the entry always gets produced, whether or not the person remembers to ask for it.
