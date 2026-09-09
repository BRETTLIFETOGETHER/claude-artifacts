# Image-Model Prompting for Covers (Lane 1)

How to write prompts for Nano Banana (Gemini) or another image model so a series generates as a family and composites cleanly with type.

## The prompt formula

Every cover prompt has five parts, in this order:

1. **Format line** — "Vertical 2:3 portrait book cover background artwork" (generate at 2:3, e.g. 1024×1536; upscale after if needed).
2. **The hard rule** — "Absolutely no text, no letters, no numbers, no symbols, no logos, no typography anywhere in the image." Repeat it at the end of the prompt too. Image models garble type; the type gets composited afterward.
3. **Series style block** — identical, word for word, across every title in the family. It carries: medium (fine-art cinematic photograph, medium-format film look), light behavior, grain, mood, palette temperament, and the composition law: "one luminous focal subject in the upper two-thirds; the lower third dissolves into darker, simpler, uncluttered space where warm light softly pools." That last clause reserves the type zone.
4. **Title subject block** — unique per title: the central metaphor from the essence brief, rendered concretely (what is seen, what the light does, what moves).
5. **Craft tail** — "masterful, museum-quality, the work of a top editorial photographer; rich detail rewarding a close look."

Change only part 4 between titles. Parts 1, 2, 3, and 5 are the family.

## Worked trio — the "40 Days of ___" family

**Shared style block (paste into all three):**
Fine-art cinematic photograph, medium-format film look, deep saturated color, volumetric light, gentle film grain, vast quiet negative space, reverent mood. One luminous focal subject in the upper two-thirds of the frame; the lower third dissolves into darker, simpler, uncluttered space where warm light softly pools.

**Prayer** — subject block:
A deep midnight-indigo atmosphere. A single shaft of warm golden dawn light breaks downward into the darkness and strikes a still point, sending soft concentric ripples of light outward, while fine particles of dust rise slowly through the beam like incense.

**Generosity** — subject block:
A rich amber and burnt-sienna atmosphere. A pair of open, upturned hands releases hundreds of tiny glowing golden seeds that fountain upward and outward, caught mid-air with soft motion blur, each seed a point of light.

**Courage** — subject block:
A storm-dark teal atmosphere, wind-driven rain streaking diagonally through the frame. A single small candle flame stands unwavering at the center, its warm glow pushing back the storm and lighting the space beneath it.

## After generation — the composite step

Brett sends the generated image(s) back. Then:

1. Load the image at full resolution; extend or crop to exactly 2:3 if the model drifted.
2. Apply the family type system in code (see the type grid in references/example-family-system.md): eyebrow, auto-fit Playfair Display title, gold rule, Cormorant Garamond italic subtitle, brand line with diamonds.
3. If the type zone lacks contrast, deepen it with a soft tonal gradient that matches the image's own palette — never a box.
4. Add the family grain and vignette so generated covers and code-built covers sit together on a shelf.
5. Deliver finished PNGs plus the family strip.

## Consistency rescue

If a generation breaks family resemblance (wrong palette temperature, cluttered lower third, focal subject too low), do not fix it in the composite — regenerate. Add to the prompt whichever constraint failed, stated positively ("the lower third is nearly empty, deep shadow with a soft pool of warm light" beats "don't put things at the bottom").
