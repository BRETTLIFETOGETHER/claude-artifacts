#!/usr/bin/env python3
"""
NEXT GENERATION — cover art in the Auric Record philosophy.
Composed vector drawing: two ring-records (the standing tree, the sapling)
joined by one continuous bright gold line. Rendered at 2x and downsampled.
"""
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(11)
np.random.seed(11)

# ---------- canvas ----------
W, H = 3600, 5400          # working resolution (2x)
FW, FH = 1800, 2700        # final resolution
NAVY = (11, 21, 35)
GOLD = (201, 162, 39)
GOLD_BRIGHT = (232, 196, 104)
IVORY = (234, 227, 210)
SLATE = (150, 163, 182)

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"

img = Image.new("RGB", (W, H), NAVY)

# very subtle vertical ground gradient (darker at foot)
grad = np.zeros((H, W, 3), dtype=np.float64)
base = np.array(NAVY, dtype=np.float64)
for y in range(H):
    t = y / H
    k = 1.06 - 0.12 * t            # slightly lighter at head, darker at foot
    grad[y, :, :] = np.clip(base * k, 0, 255)
img = Image.fromarray(grad.astype(np.uint8), "RGB")

layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(layer)

# ---------- ring machinery ----------
def ring_points(cx, cy, r, wobble_amp, phases, n=560):
    pts = []
    for i in range(n + 1):
        th = 2 * math.pi * i / n
        w = (math.sin(3 * th + phases[0]) * 0.45
             + math.sin(5 * th + phases[1]) * 0.33
             + math.sin(8 * th + phases[2]) * 0.22)
        rr = r + wobble_amp * w
        pts.append((cx + rr * math.cos(th), cy + rr * math.sin(th)))
    return pts

def draw_ring(cx, cy, r, color, alpha, width, wobble_frac=0.010):
    phases = [random.uniform(0, 6.283) for _ in range(3)]
    amp = max(1.5, r * wobble_frac)
    pts = ring_points(cx, cy, r, amp, phases)
    d.line(pts, fill=color + (alpha,), width=width, joint="curve")

def build_radii(r0, rmax):
    """Irregular tree-ring spacing: tight clusters and open years."""
    radii, r = [], r0
    while r < rmax:
        radii.append(r)
        if random.random() < 0.30:              # a run of tight rings
            for _ in range(random.randint(2, 4)):
                r += random.uniform(16, 26)
                if r < rmax:
                    radii.append(r)
        r += random.uniform(30, 62)
    return radii

# ---------- the standing record (I) ----------
C1 = (1500, 1560)
R1 = 1030
radii1 = build_radii(56, R1 - 30)
accents1 = set(random.sample(range(3, len(radii1) - 1), 4))
for i, r in enumerate(radii1):
    if i in accents1:
        draw_ring(*C1, r, GOLD, 195, 5)
    else:
        a = random.randint(72, 132)
        draw_ring(*C1, r, GOLD, a, 3)
# heartwood point
d.ellipse([C1[0] - 7, C1[1] - 7, C1[0] + 7, C1[1] + 7], fill=GOLD + (210,))

# survey ticks around the standing record
for k in range(72):
    th = 2 * math.pi * k / 72
    r_in = R1 + 26
    r_out = R1 + (86 if k % 6 == 0 else 54)
    a = 78 if k % 6 == 0 else 52
    d.line([(C1[0] + r_in * math.cos(th), C1[1] + r_in * math.sin(th)),
            (C1[0] + r_out * math.cos(th), C1[1] + r_out * math.sin(th))],
           fill=GOLD + (a,), width=2)

# ---------- the young record (II) ----------
C2 = (2560, 3140)
R2 = 300
radii2 = build_radii(24, R2 - 26)
for r in radii2:
    a = random.randint(85, 140)
    draw_ring(*C2, r, GOLD, a, 3)
d.ellipse([C2[0] - 5, C2[1] - 5, C2[0] + 5, C2[1] + 5], fill=GOLD + (210,))

# ---------- the one continuous line ----------
def bezier(p0, p1, p2, p3, n=240):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = (mt**3 * p0[0] + 3 * mt**2 * t * p1[0]
             + 3 * mt * t**2 * p2[0] + t**3 * p3[0])
        y = (mt**3 * p0[1] + 3 * mt**2 * t * p1[1]
             + 3 * mt * t**2 * p2[1] + t**3 * p3[1])
        pts.append((x, y))
    return pts

# the bright line rides the standing record's outer edge as a long crescent,
# peels off at the lower right, and coils clockwise into the young record
th_start, th_leave = math.radians(-80), math.radians(50)
arc = []
for i in range(220):
    th = th_start + (th_leave - th_start) * i / 219
    arc.append((C1[0] + R1 * math.cos(th), C1[1] + R1 * math.sin(th)))

P0 = arc[-1]
P1 = (P0[0] + 300, P0[1] + 460)               # leave moving down and right
P3 = (C2[0] - R2, C2[1])                       # enter at the young ring's left
P2 = (P3[0], P3[1] - 320)                      # arrive moving straight down
bridge = bezier(P0, P1, P2, P3)

young_outer = []                               # clockwise from the left point
for i in range(561):
    th = math.radians(180) - 2 * math.pi * i / 560
    young_outer.append((C2[0] + R2 * math.cos(th), C2[1] + R2 * math.sin(th)))

for seg in (arc, bridge, young_outer):
    d.line(seg, fill=GOLD_BRIGHT + (235,), width=6, joint="curve")

# ---------- clinical index numerals ----------
mono = ImageFont.truetype(f"{FONTS}/DMMono-Regular.ttf", 44)
d.text((C1[0] - R1 - 210, C1[1] + 60), "i.", font=mono, fill=GOLD + (120,))
d.text((C2[0] + R2 + 96, C2[1] - 18), "ii.", font=mono, fill=GOLD + (120,))

img = Image.alpha_composite(img.convert("RGBA"), layer)

# ---------- typography ----------
t = ImageDraw.Draw(img)

def tracked(draw, xy_center, text, font, fill, tracking):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = xy_center[0] - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, xy_center[1]), ch, font=font, fill=fill, anchor="lm")
        x += w + tracking

def fit_font(path, text, target_w, start=340):
    size = start
    while size > 40:
        f = ImageFont.truetype(path, size)
        if t.textlength(text, font=f) <= target_w:
            return f
        size -= 4
    return ImageFont.truetype(path, 40)

CX = W // 2

# thin rule
t.line([(CX - 130, 3985), (CX + 130, 3985)], fill=GOLD + (200,), width=3)

series_f = ImageFont.truetype(f"{FONTS}/CrimsonPro-Regular.ttf", 62)
tracked(t, (CX, 4095), "LEGACY BY DESIGN  ·  COACHING SERIES",
        series_f, GOLD + (255,), 20)

title_f = fit_font(f"{FONTS}/Gloock-Regular.ttf", "Next Generation", 2660)
t.text((CX, 4330), "Next Generation", font=title_f, fill=IVORY, anchor="mm")

authors_f = ImageFont.truetype(f"{FONTS}/CrimsonPro-Regular.ttf", 68)
tracked(t, (CX, 4625), "TOM CONWAY  &  BRETT EASTMAN",
        authors_f, IVORY + (225,), 16)

fore_f = ImageFont.truetype(f"{FONTS}/CrimsonPro-Italic.ttf", 60)
t.text((CX, 4775), "Foreword by Rick Warren", font=fore_f,
       fill=(168, 179, 194, 240), anchor="mm")

# hairline frame
t.rectangle([120, 120, W - 120, H - 120], outline=GOLD + (58,), width=2)

# ---------- finish: downsample, grain, vignette ----------
img = img.convert("RGB").resize((FW, FH), Image.LANCZOS)

arr = np.asarray(img).astype(np.int16)
grain = np.random.randint(-3, 4, size=(FH, FW, 1), dtype=np.int16)
arr = np.clip(arr + grain, 0, 255).astype(np.uint8)
img = Image.fromarray(arr, "RGB")

# gentle vignette
yy, xx = np.mgrid[0:FH, 0:FW]
cx, cy = FW / 2, FH / 2
r = np.sqrt(((xx - cx) / (FW / 2)) ** 2 + ((yy - cy) / (FH / 2)) ** 2)
vig = np.clip(1.0 - 0.10 * np.clip(r - 0.55, 0, None) / 0.9, 0.90, 1.0)
arr = np.asarray(img).astype(np.float64) * vig[:, :, None]
img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

img.save("/home/claude/next_generation_cover.png")
print("done", img.size)
