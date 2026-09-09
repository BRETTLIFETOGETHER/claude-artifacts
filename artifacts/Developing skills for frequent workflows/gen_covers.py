#!/usr/bin/env python3
"""Luminous Passage — 40 Days of ___ family. Three covers + family strip."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

SS = 2
W, H = 1200 * SS, 1800 * SS
FONTS = "/home/claude/fonts"
OUT = "/home/claude/covers"

def font(path, size, weight=None, italic=False):
    f = ImageFont.truetype(path, size)
    if weight is not None:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f

def lingrad(w, h, stops):
    """Vertical gradient. stops = [(pos0-1, (r,g,b)), ...]"""
    ys = np.linspace(0, 1, h)
    arr = np.zeros((h, w, 3), dtype=np.float64)
    for i in range(len(stops) - 1):
        p0, c0 = stops[i]; p1, c1 = stops[i + 1]
        mask = (ys >= p0) & (ys <= p1)
        t = np.zeros(h)
        t[mask] = (ys[mask] - p0) / max(p1 - p0, 1e-6)
        for ch in range(3):
            col = c0[ch] + (c1[ch] - c0[ch]) * t
            arr[mask, :, ch] = col[mask, None]
    return arr

def add_glow(arr, cx, cy, radius, color, strength=1.0, falloff=2.2):
    h, w, _ = arr.shape
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / radius
    g = np.clip(1 - d, 0, 1) ** falloff * strength
    for ch in range(3):
        arr[:, :, ch] += g * color[ch]
    return arr

def to_img(arr):
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

def screen_paste(base, overlay):
    return ImageChops.screen(base, overlay)

def grain_vignette(img, grain=9, vig=0.55):
    w, h = img.size
    arr = np.asarray(img).astype(np.float64)
    rng = np.random.default_rng(7)
    noise = rng.normal(0, grain, (h, w, 1))
    arr = arr + noise
    yy, xx = np.mgrid[0:h, 0:w]
    cx, cy = w / 2, h / 2
    d = np.sqrt(((xx - cx) / (w * 0.72)) ** 2 + ((yy - cy) / (h * 0.72)) ** 2)
    v = 1 - np.clip(d - 0.55, 0, 1) * vig
    arr = arr * v[:, :, None]
    return to_img(arr)

def tracked(draw, xy, text, fnt, fill, tracking, anchor="center"):
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor == "center":
        x -= total / 2
    for ch, cw in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += cw + tracking
    return total

def tracked_len(draw, text, fnt, tracking):
    return sum(draw.textlength(ch, font=fnt) for ch in text) + tracking * (len(text) - 1)

IVORY = (243, 233, 210)
GOLD = (212, 175, 96)

def type_system(img, word, subtitle, glow_color):
    """Fixed family grid: eyebrow, big word, rule, subtitle, brand line."""
    w, h = img.size
    layer = Image.new("RGB", img.size, (0, 0, 0))
    d = ImageDraw.Draw(layer)

    eyebrow_f = font(f"{FONTS}/CormorantGaramond.ttf", int(46 * SS), 600)
    brand_f = font(f"{FONTS}/CormorantGaramond.ttf", int(34 * SS), 600)
    sub_f = font(f"{FONTS}/CormorantGaramond-Italic.ttf", int(52 * SS), 500)

    # auto-fit title word to 78% width
    lo, hi = 40 * SS, 260 * SS
    target = 0.78 * w
    while lo < hi:
        mid = (lo + hi + 1) // 2
        f = font(f"{FONTS}/PlayfairDisplay.ttf", mid, 800)
        tr = mid * 0.06
        if tracked_len(d, word, f, tr) <= target:
            lo = mid
        else:
            hi = mid - 1
    title_f = font(f"{FONTS}/PlayfairDisplay.ttf", lo, 800)
    title_tr = lo * 0.06

    ey_y = int(0.575 * h)
    tracked(d, (w / 2, ey_y), "F O R T Y   D A Y S   O F", eyebrow_f, IVORY, 6 * SS)

    asc, desc = title_f.getmetrics()
    ti_y = int(0.618 * h)
    tracked(d, (w / 2, ti_y), word, title_f, IVORY, title_tr)
    base_y = ti_y + asc + desc

    rule_y = base_y + int(26 * SS)
    d.line([(w / 2 - 45 * SS, rule_y), (w / 2 + 45 * SS, rule_y)], fill=GOLD, width=int(3 * SS))

    sub_y = rule_y + int(26 * SS)
    sw = d.textlength(subtitle, font=sub_f)
    d.text((w / 2 - sw / 2, sub_y), subtitle, font=sub_f, fill=IVORY)

    br_y = int(0.935 * h)
    bw = tracked(d, (w / 2, br_y), "L I F E T O G E T H E R", brand_f, (*GOLD,), 4 * SS)
    dy = br_y + int(22 * SS)
    for dx in (-bw / 2 - 34 * SS, bw / 2 + 34 * SS):
        cx = w / 2 + dx
        d.polygon([(cx, dy - 7 * SS), (cx + 7 * SS, dy), (cx, dy + 7 * SS), (cx - 7 * SS, dy)], fill=GOLD)

    # warm glow beneath type, then crisp type on top
    glow = layer.filter(ImageFilter.GaussianBlur(14 * SS))
    glow_np = np.asarray(glow).astype(np.float64)
    tint = np.array(glow_color) / 255.0
    glow = to_img(glow_np * tint[None, None, :] * 0.9)
    out = screen_paste(img, glow)
    out = screen_paste(out, layer)
    return out

# ---------------------------------------------------------------- PRAYER
def art_prayer():
    arr = lingrad(W, H, [(0.0, (10, 13, 34)), (0.45, (22, 28, 66)), (0.75, (34, 41, 92)), (1.0, (13, 16, 40))])
    cx, cy = W / 2, 0.355 * H
    add_glow(arr, cx, cy, 0.52 * W, (96, 74, 30), 1.0)          # broad dawn aura
    add_glow(arr, cx, cy, 0.17 * W, (168, 128, 52), 1.0)        # core
    add_glow(arr, cx, 0.66 * H, 0.44 * W, (46, 38, 22), 1.0)    # light descending to title
    img = to_img(arr)

    ov = Image.new("RGB", img.size, (0, 0, 0))
    d = ImageDraw.Draw(ov)
    # concentric rings — the struck point of contact
    for i, r in enumerate(np.linspace(0.045 * W, 0.62 * W, 11)):
        a = max(10, int(120 * (1 - i / 11) ** 1.4))
        col = (int(212 * a / 255), int(175 * a / 255), int(96 * a / 255))
        d.ellipse([cx - r, cy - r * 0.72, cx + r, cy + r * 0.72], outline=col, width=max(int(2.2 * SS - i * 0.14), 1))
    ov = ov.filter(ImageFilter.GaussianBlur(1.1 * SS))
    img = screen_paste(img, ov)

    # ascending particle streams converging into the light
    pv = Image.new("RGB", img.size, (0, 0, 0))
    pd = ImageDraw.Draw(pv)
    rng = random.Random(11)
    for sx in np.linspace(0.06 * W, 0.94 * W, 22):
        for t in np.linspace(0, 1, 46):
            x = sx + (cx - sx) * (t ** 1.55) + rng.uniform(-1, 1) * 11 * SS
            y = H * 1.02 - (H * 1.02 - cy) * t + rng.uniform(-1, 1) * 8 * SS
            if y < cy - 6 * SS:
                continue
            s = (0.7 + 2.3 * t) * SS
            a = 0.16 + 0.66 * (t ** 1.6)
            col = (int(224 * a), int(190 * a), int(120 * a))
            pd.ellipse([x - s, y - s, x + s, y + s], fill=col)
    pv = pv.filter(ImageFilter.GaussianBlur(0.9 * SS))
    img = screen_paste(img, pv)
    return type_system(img, "P R A Y E R".replace(" ", ""), "Learning to Live in Conversation with God", (150, 120, 60))

# ------------------------------------------------------------ GENEROSITY
def art_generosity():
    arr = lingrad(W, H, [(0.0, (66, 20, 14)), (0.42, (112, 38, 22)), (0.72, (150, 62, 30)), (1.0, (70, 24, 15))])
    cx, cy = W / 2, 0.435 * H
    add_glow(arr, cx, cy, 0.42 * W, (120, 66, 22), 1.0)
    add_glow(arr, cx, cy, 0.15 * W, (190, 120, 40), 1.0)
    add_glow(arr, cx, 0.68 * H, 0.40 * W, (56, 30, 12), 1.0)
    img = to_img(arr)

    # the open vessel — two concentric bowl arcs beneath the burst
    ov = Image.new("RGB", img.size, (0, 0, 0))
    d = ImageDraw.Draw(ov)
    box = [cx - 0.185 * W, cy - 0.155 * W, cx + 0.185 * W, cy + 0.095 * W]
    d.arc(box, start=14, end=166, fill=(230, 182, 110), width=int(8 * SS))
    d.arc([box[0] + 13 * SS, box[1] + 13 * SS, box[2] - 13 * SS, box[3] - 13 * SS],
          start=20, end=160, fill=(158, 110, 54), width=int(3.6 * SS))
    ov = ov.filter(ImageFilter.GaussianBlur(1.2 * SS))
    img = screen_paste(img, ov)

    # seed fountain — parabolic arcs of gold seeds
    pv = Image.new("RGB", img.size, (0, 0, 0))
    pd = ImageDraw.Draw(pv)
    rng = random.Random(23)
    for k in range(120):
        ang = rng.uniform(math.pi * 0.16, math.pi * 0.84)
        vel = rng.uniform(0.16, 0.62)
        n = rng.randint(9, 16)
        for i in range(n):
            t = i / (n - 1)
            x = cx + math.cos(ang) * vel * W * t * 0.85
            y = cy - 0.045 * H - (math.sin(ang) * vel * H * t * 0.62 - 0.34 * H * (t * vel) ** 2)
            if y > 0.585 * H or y < 0.04 * H or x < 0.04 * W or x > 0.96 * W:
                continue
            s = (2.6 - 1.7 * t) * SS * rng.uniform(0.7, 1.15)
            a = 0.9 - 0.55 * t
            col = (int(232 * a), int(186 * a), int(104 * a))
            pd.ellipse([x - s, y - s, x + s, y + s], fill=col)
    pv = pv.filter(ImageFilter.GaussianBlur(0.8 * SS))
    img = screen_paste(img, pv)
    return type_system(img, "GENEROSITY", "Open Hands, Overflowing Life", (170, 100, 40))

# --------------------------------------------------------------- COURAGE
def art_courage():
    arr = lingrad(W, H, [(0.0, (9, 22, 26)), (0.45, (17, 38, 44)), (0.78, (24, 50, 56)), (1.0, (10, 24, 28))])
    cx, cy = W / 2, 0.40 * H
    add_glow(arr, cx, cy, 0.40 * W, (96, 44, 14), 1.0)
    add_glow(arr, cx, cy, 0.13 * W, (200, 96, 26), 1.0)
    add_glow(arr, cx, 0.665 * H, 0.42 * W, (54, 26, 10), 1.0)
    img = to_img(arr)

    # diagonal wind streaks parting around the flame
    ov = Image.new("RGB", img.size, (0, 0, 0))
    d = ImageDraw.Draw(ov)
    rng = random.Random(31)
    for _ in range(230):
        x0 = rng.uniform(-0.1 * W, 1.1 * W)
        y0 = rng.uniform(0.02 * H, 0.56 * H)
        dist = abs(x0 - cx) / (0.5 * W) + abs(y0 - cy) / (0.5 * H)
        if dist < 0.44:
            continue
        ln = rng.uniform(0.07, 0.22) * W
        a = rng.uniform(0.16, 0.50) * min(dist, 1.4)
        col = (int(140 * a), int(190 * a), int(200 * a))
        d.line([(x0, y0), (x0 - ln, y0 + ln * 0.42)], fill=col, width=max(int(1.8 * SS), 1))
    ov = ov.filter(ImageFilter.GaussianBlur(1.0 * SS))
    img = screen_paste(img, ov)
    # baseline — the ground the flame stands on
    bl = Image.new("RGB", img.size, (0, 0, 0))
    bd = ImageDraw.Draw(bl)
    by = cy + 0.205 * H * 0.55 + 8 * SS
    bd.line([(cx - 0.15 * W, by), (cx + 0.15 * W, by)], fill=(196, 138, 62), width=int(3 * SS))
    bl = bl.filter(ImageFilter.GaussianBlur(2.6 * SS))
    img = screen_paste(img, bl)

    # the standing flame — three nested parametric teardrops
    fv = Image.new("RGB", img.size, (0, 0, 0))
    fd = ImageDraw.Draw(fv)
    layers = [(1.00, (150, 52, 14)), (0.66, (222, 116, 30)), (0.36, (250, 206, 120))]
    fh, fw = 0.205 * H, 0.115 * W
    for scale, col in layers:
        pts = []
        for i in range(120):
            t = i / 119.0
            yy = cy + fh * 0.55 * scale - fh * scale * t
            wob = 1 + 0.10 * math.sin(t * 9.0 + scale * 5)
            ww = fw * scale * math.sin(math.pi * min(t * 1.12, 1.0)) ** 1.25 * wob * (1 - 0.55 * t)
            pts.append((cx + ww, yy))
        for i in range(120):
            t = 1 - i / 119.0
            yy = cy + fh * 0.55 * scale - fh * scale * t
            wob = 1 + 0.10 * math.sin(t * 9.0 + scale * 5)
            ww = fw * scale * math.sin(math.pi * min(t * 1.12, 1.0)) ** 1.25 * wob * (1 - 0.55 * t)
            pts.append((cx - ww, yy))
        fd.polygon(pts, fill=col)
    fv = fv.filter(ImageFilter.GaussianBlur(2.2 * SS))
    img = screen_paste(img, fv)

    # drifting sparks
    sv = Image.new("RGB", img.size, (0, 0, 0))
    sd = ImageDraw.Draw(sv)
    rng = random.Random(37)
    for _ in range(40):
        t = rng.uniform(0, 1)
        x = cx + rng.uniform(-0.03, 0.05) * W + 0.02 * W * t
        y = cy - fh * 0.55 - t * 0.16 * H + rng.uniform(-0.01, 0.01) * H
        s = (2.0 - 1.4 * t) * SS
        a = 0.85 - 0.6 * t
        sd.ellipse([x - s, y - s, x + s, y + s], fill=(int(250 * a), int(180 * a), int(90 * a)))
    sv = sv.filter(ImageFilter.GaussianBlur(0.7 * SS))
    img = screen_paste(img, sv)
    return type_system(img, "COURAGE", "Faith That Stands When Everything Shakes", (150, 78, 30))

def finish(img, name):
    img = grain_vignette(img)
    img = img.resize((1200, 1800), Image.LANCZOS)
    img.save(f"{OUT}/{name}.png")
    return img

if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    covers = [
        finish(art_prayer(), "40-days-of-prayer"),
        finish(art_generosity(), "40-days-of-generosity"),
        finish(art_courage(), "40-days-of-courage"),
    ]
    gap, pad = 60, 80
    strip = Image.new("RGB", (1200 * 3 + gap * 2 + pad * 2, 1800 + pad * 2), (16, 14, 18))
    for i, c in enumerate(covers):
        strip.paste(c, (pad + i * (1200 + gap), pad))
    strip.save(f"{OUT}/series-family-strip.png")
    print("done")
