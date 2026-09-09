---
name: cover-designer
description: Generate distinct, image-led cover art for curriculum, campaign, and product titles — image-model art direction (Nano Banana / Gemini), original code-built art, or treatment of a supplied image — where the image is built from the title's essence and series covers read as a family. Use whenever Brett supplies a title and subtitle and wants a cover, cover art, thumbnail, packaging, or a visual identity, or whenever a new title, series, or catalog exists without art. Never deliver type sitting on a plain colored background.
---

# Cover Designer

The title is the source. The image is its expression. The composition returns the eye to the words.

## Non-negotiables

- **Image-led.** Full-bleed artwork occupies the entire canvas. A flat or gradient background with a font on it is a failed cover, no matter how nice the font. The bar is a unique, signature, top-designer piece — never something that reads as AI-templated.
- **Derived from the title.** Extract the essence, heart, and theme of the title and subtitle, then choose one central visual metaphor unique to this title. The image is based on the words, not decorated near them.
- **Directional.** The art's energy — light, converging lines, a lit zone — leads the eye to the title block.
- **Distinct.** No two titles in a catalog share a metaphor. On catalog work, keep a running motif ledger and check it before designing each cover; at hundreds or thousands of titles this ledger is the only thing preventing repeats.
- **The removal test.** Hide the words. What remains should still stand as a piece of art about the theme.

## Process

1. **Gather**: title, subtitle, series membership, format (default 2:3 portrait; square thumbnail crop on request), and lane.
2. **Essence brief** (3 lines, before any pixels or prompts): the heart of the title / its emotional register / the one central metaphor. On batch runs, print the brief above each cover.
3. Build in the chosen lane, run a refinement pass, deliver.

## Lane 1 — Image-model art (default)

Claude cannot generate photographs directly, so this lane produces production-grade prompts for an image model — Nano Banana (Gemini) is Brett's tool of choice; Canva Magic Media works as an alternate. Read references/image-model-prompting.md and follow its prompt formula exactly, including:

- One **shared series style block** reused verbatim across every title in a family, plus a **unique subject block** per title — this is how the family resemblance survives generation.
- The hard rule inside every prompt: **no text, letters, numbers, logos, or typography anywhere in the image.** Image models garble type. Generate clean art, then composite the type.
- Composition instruction reserving the lower third as simpler, darker space where light pools — the future type zone.

**The round trip**: deliver the prompts → Brett generates and sends the image(s) back → composite the family type system (Playfair Display title, Cormorant Garamond subtitle and labels, gold rule, brand line) over the returned art in code, and deliver finished PNG covers. Never skip the composite step; a raw generation is not a cover.

## Lane 2 — Original code-built art

For graphic/illustrative covers, instant in-chat results, or when Brett asks for it: read /mnt/skills/examples/canvas-design/SKILL.md and follow it — write a short design philosophy, express it in code, output PNG. Layered fields of color, light, texture, and motion; symbolic, not clip-art; grain and vignette for a printed finish. Be plain that this lane is graphic art, not photography; route photographic ambitions to Lane 1.

## Lane 3 — Supplied image

When Brett supplies a photo or artwork, build the full cover treatment around it under the same composition rules. Never place an unlicensed web image on a cover.

## Series covers are a family

Before designing title one of any series, define the family system and hold it fixed:

- **Shared**: format, type system and placement grid, eyebrow and brand-mark positions, texture treatment, palette logic, one recurring structural motif — and in Lane 1, the shared style block.
- **Unique per title**: the central metaphor, the dominant palette, the composition's energy.

With any series batch, deliver a side-by-side family strip so the resemblance can be checked in one glance.

## Type

Title dominant; subtitle secondary; series eyebrow and brand line small and letterspaced. Earn legibility through the art itself — a halo, a lit zone, a tonal field — never a contrast box slapped over the image. Margins must hold on a phone screen, where Brett reviews first.

## Delivery

PNG at final size to /mnt/user-data/outputs/, presented. For batches: individual covers plus the family strip. Log each title's metaphor to the motif ledger before moving on.

References: references/image-model-prompting.md (Lane 1 formula + worked prompt trio), references/example-family-system.md (Lane 2 worked example).
