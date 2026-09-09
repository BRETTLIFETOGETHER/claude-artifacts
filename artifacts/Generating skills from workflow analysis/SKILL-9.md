---
name: blue-template-builder
description: Build Brett's blue interactive HTML template — the working/product-prototype system with segmentation → assessment → result → pricing → catalog flow. Use whenever Brett pastes copy or content with no other instruction (this is his stated default), or asks for an interactive tool, prototype, working build, product page draft, clickable experience, or "put this in the template." NOT for pastor/partner/buyer-facing polish — that's the navy/gold brochure-builder skill.
---

# Blue Template Builder

## When this fires

Brett pasting copy with no instruction = build it into this template, not plain text. This is the **working/prototype system**; anything a pastor, partner, or buyer will see goes to the navy/gold system (brochure-builder skill) instead. If audience is ambiguous, ask which system — one question maximum.

## The design system (fixed)

- Font: **Inter**. Accent: **`--blue: #1d4ed8`**. White cards on a light ground, **12px radius**, **no emoji anywhere**.
- Clean, product-grade, generous spacing. No decorative flourish — this system's job is to make an idea feel like software.

## The canonical flow (adapt, don't abandon)

**Segmentation → Assessment → Result → Pricing → Catalog.**

1. **Segmentation** — who are you? (e.g., senior pastor / executive pastor / ministry leader; or advisor / family / church). Selection personalizes everything downstream.
2. **Assessment** — short rating-scale questions (a diagnostic, not a quiz). An assessment leads to a pathway, not just a score. Crawl → Walk → Run staging is the house pattern for results banding.
3. **Result** — the score band with customized next steps per segment.
4. **Pricing** — tiers per the pricing-packager rules (attendance bands for church products; ladder integrity; free tier real).
5. **Catalog** — the browsable library/product grid relevant to their segment and result.

Not every build needs all five — a directory may be catalog-first, an offer page pricing-first — but keep the spine recognizable and wire segmentation through whatever exists.

## Engineering rules (hard requirements)

- **Single self-contained HTML file.** No frameworks, no external dependencies, no CDN calls.
- **No template literals in JS — string concatenation only.** Verify brace balance before delivering.
- **Mobile-first.** Brett reviews on his phone; the build must be excellent at ~380px before it's good at desktop.
- Include a simple self-test count where state logic exists (Brett's builds report "N/N tests pass"); actually run the logic mentally or in code before claiming it.
- No localStorage/sessionStorage in claude.ai artifacts — state lives in JS memory.

## Content rules

Publication-ready copy inside the build — finished names, real subtitles, working numbers carried exactly from established sources (never invented stats or testimonials; verified field evidence only). Status labels apply to product claims inside the UI too: don't render a concept as a shipping product without a draft label.

## Delivery

Save to outputs and present the file. Note in one line which parts are wired vs. stubbed, if any.
