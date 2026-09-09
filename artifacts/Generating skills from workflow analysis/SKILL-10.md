---
name: print-pdf-producer
description: Produce designed, print-ready PDFs — proposals, offers, prospectuses, print editions of HTML deliverables — using Brett's verified WeasyPrint page-discipline system. Use whenever Brett asks for a PDF, a printable version, a print edition, "make this printable," or a designed document to send or hand to someone. Encodes hard-won technical rules; never build a designed PDF from scratch without this skill.
---

# Print PDF Producer

## Page discipline — author pages, don't flow them

Author **one `.pg` div per sheet** and fill each deliberately. The container that works (do not improvise):

```css
@page{size:8.5in 11in;margin:0}
.pg{width:8.5in;height:11in;padding:0.72in 0.92in 1.15in;position:relative;
    overflow:hidden;display:block;page-break-after:always;break-after:page}
.foot{position:absolute;left:.92in;right:.92in;bottom:.52in;border-top:1px solid /*line color*/}
```

**Never use flex for the page container** — flex + fixed height lets the body overflow and drags footers onto the next sheet, cascading. Screen-only `margin-bottom` on `.pg` is fine with `@media print{.pg{margin:0}}`.

## Verification loop — run every render

1. Count `.pg` divs in source; render; **assert PDF page count matches.** Mismatch = an overflowing page.
2. Rasterize at 50dpi (`pdftoppm -png -r 50`); per page, measure the gap from footer rule up to last inked row. Over ~0.85in of bottom whitespace → add copy (~250 characters of prose per inch at 11pt/1.62); page-count growth → cut copy.
3. Extract text per page with pypdf; a page under ~650 characters is a spillover orphan — tighten the source page above it. Remove any global `break-inside:avoid`.
4. Deliberately centered pages (covers, closers) get balanced top padding so the gap reads intentional.

## Design rules

- **Every page gets a ground** — never black type on bare white sheets; run a color rhythm across the spread.
- **Never introduce a color outside the client's palette** (an invented cream reads generic instantly). **Never nest a filled panel on a colored ground** — use rules, space, and a left accent bar instead.
- "Looks like a template" = a visible repeating system: one header pattern every page (eyebrow, accent rule, headline with second half in accent, large pale section numeral top-right), one grid, one footer, one type scale.
- Default identity for pastor/partner/buyer documents is the **navy/gold system** (tokens live in the brochure-builder skill / lifetogether site source of record).
- Photography of people: full color, no filter.
- **Never end a document on the invoice** — price second-to-last, the ask and the vision last.
- Fill every [NAME]/[EMAIL]-style placeholder before a PDF travels, or flag it loudly.

## WeasyPrint technicals

- Install: `pip install --default-timeout=120 weasyprint --break-system-packages`. Don't use wkhtmltopdf (old WebKit breaks flex/grid).
- **Fonts:** Google Fonts CSS host is unreachable from the sandbox, but the real variable TTFs are: fetch `raw.githubusercontent.com/google/fonts/main/ofl/<family>/<Family>%5Bwght%5D.ttf` (plus `-Italic`) for Playfair Display and Cormorant Garamond; register via `@font-face` with `font-weight:100 900`. Fallbacks installed: Lora, Carlito.
- **Full-bleed covers:** body background paints over every page and silently hides a named `@page cover` background — keep body transparent, paper color on `@page`, cover div its own 8.5×11in background with `@page cover{margin:0}`.
- WeasyPrint treats flex containers as atomic (whole block jumps pages); flowed content needs `display:block` all the way down.
- Merge multiple designed documents at the file level with `pypdf.PdfWriter` — never splice HTML.
- Crashes on `::first-letter{float:left}` in flex — use an inline span drop initial. Absolutely-positioned progress fills don't render in flex — block fill inside `overflow:hidden` track. QR-style graphics as **inline SVG**, not CSS gradients. Two-column lists: `flex-wrap` with 50% items, not `column-count`.

## Delivery

Render, run the full verification loop, report page count and per-page whitespace check results in one line, save to outputs, present the file.
