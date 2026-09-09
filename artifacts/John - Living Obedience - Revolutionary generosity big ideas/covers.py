import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

W, H = 1600, 2400
F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
OUT = "/mnt/user-data/outputs/"
random.seed(7)

INK   = (9, 18, 34)
NAVY  = (18, 37, 63)
INDIGO= (32, 56, 92)
UMBER = (92, 68, 44)
GOLD  = (196, 152, 74)
WARM  = (233, 199, 138)
CREAM = (246, 241, 231)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def vgrad(size, stops):
    """stops: list of (pos 0-1, color). Smooth vertical field."""
    w, h = size
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]; p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                u = (t - p0) / max(p1 - p0, 1e-6)
                u = u * u * (3 - 2 * u)          # smoothstep
                px[0, y] = lerp(c0, c1, u)
                break
        else:
            px[0, y] = stops[-1][1]
    return img.resize((w, h), Image.BILINEAR)

def radial(size, cx, cy, r, color, strength=1.0, falloff=2.2):
    """Additive glow, rendered at low res then upsampled for a soft, seamless falloff."""
    w, h = size
    sw, sh = w // 4, h // 4
    lay = Image.new("RGB", (sw, sh), (0, 0, 0))
    px = lay.load()
    cxs, cys, rs = cx / 4, cy / 4, r / 4
    for y in range(sh):
        for x in range(sw):
            d = math.hypot((x - cxs), (y - cys) * 1.0) / rs
            if d < 1.6:
                a = max(0.0, 1.0 - d) ** falloff * strength
                px[x, y] = (int(color[0]*a), int(color[1]*a), int(color[2]*a))
    return lay.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(28))

def grain(size, amt=9):
    w, h = size
    n = Image.new("L", (w // 2, h // 2))
    n.putdata([random.gauss(128, amt) for _ in range((w // 2) * (h // 2))])
    n = n.resize((w, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.4))
    return Image.merge("RGB", (n, n, n))

def vignette(img, strength=0.55):
    w, h = img.size
    m = Image.new("L", (w // 4, h // 4), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([-w//9, -h//11, w//4 + w//9, h//4 + h//11], fill=255)
    m = m.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(200))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    return Image.composite(img, Image.blend(img, dark, strength), m)

def finish(img):
    img = ImageChops.add(img, grain(img.size, 8), scale=1, offset=-128)
    return vignette(img)

# ---------- type ----------
def font(name, size):
    return ImageFont.truetype(F + name, size)

def tracked(draw, xy, text, f, fill, track=0, anchor_center=None):
    x, y = xy
    if anchor_center is not None:
        total = sum(draw.textlength(c, font=f) + track for c in text) - track
        x = anchor_center - total / 2
    for c in text:
        draw.text((x, y), c, font=f, fill=fill)
        x += draw.textlength(c, font=f) + track

def typeset(img, title_lines, tone="dark"):
    """Family type system. Identical placement across all three covers."""
    d = ImageDraw.Draw(img)
    cx = W // 2
    ttl = font("LibreBaskerville-Regular.ttf", 132)
    sub = font("CrimsonPro-Italic.ttf", 50)
    lab = font("CrimsonPro-Regular.ttf", 30)
    aut = font("CrimsonPro-Regular.ttf", 38)

    tracked(d, (0, 1512), "THE SIGNATRY", lab, GOLD, track=13, anchor_center=cx)

    y = 1610
    for line in title_lines:
        tracked(d, (0, y), line, ttl, CREAM, track=5, anchor_center=cx)
        y += 168

    ry = y + 34
    d.rectangle([cx - 62, ry, cx + 62, ry + 3], fill=GOLD)

    st = "Saying yes to God with your life, your family,"
    st2 = "your business, your wealth."
    d.text((cx, ry + 62), st, font=sub, fill=(205, 197, 182), anchor="ma")
    d.text((cx, ry + 128), st2, font=sub, fill=(205, 197, 182), anchor="ma")

    tracked(d, (0, 2178), "STEVE FRENCH", aut, WARM, track=9, anchor_center=cx)
    tracked(d, (0, 2238), "WITH DALE ARMSTRONG", lab, (150, 146, 136), track=11, anchor_center=cx)
    return img

# ---------- COVER A · THE THRESHOLD ----------
def cover_a():
    img = vgrad((W, H), [(0.0, INK), (0.34, NAVY), (0.62, (26, 46, 76)), (1.0, (11, 21, 38))])
    # the opening: a tall aperture, high and centred, light widening as it descends
    ap = Image.new("RGB", (W, H), (0, 0, 0))
    ad = ImageDraw.Draw(ap)
    top_w, bot_w = 148, 430
    y0, y1 = 300, 1560
    for i in range(340):
        t = i / 339
        yy0 = y0 + (y1 - y0) * t
        wdt = top_w + (bot_w - top_w) * (t ** 1.55)
        a = (1 - t) ** 1.25
        c = lerp(WARM, UMBER, min(1.0, t * 1.15))
        ad.rectangle([W/2 - wdt/2, yy0, W/2 + wdt/2, yy0 + 8],
                     fill=(int(c[0]*a), int(c[1]*a), int(c[2]*a)))
    ap = ap.filter(ImageFilter.GaussianBlur(46))
    img = ImageChops.add(img, ap)
    img = ImageChops.add(img, radial((W, H), W/2, 340, 620, (150, 116, 62), 0.95))
    img = ImageChops.add(img, radial((W, H), W/2, 1560, 900, (58, 44, 26), 0.85, 2.6))
    return finish(img)

# ---------- COVER B · FIRST LIGHT ----------
def cover_b():
    hz = int(H * 0.605)
    img = vgrad((W, H), [(0.0, INK), (0.22, (16, 32, 56)), (0.44, INDIGO),
                         (0.575, (118, 92, 62)), (0.605, (208, 168, 106)),
                         (0.615, (28, 36, 50)), (0.80, (14, 24, 40)), (1.0, (8, 16, 30))])
    img = ImageChops.add(img, radial((W, H), W/2, hz - 10, 760, (128, 96, 52), 0.9, 2.0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, hz - 2, W, hz], fill=(226, 190, 128))
    # atmospheric striations above the horizon — patient, hand-tuned bands
    st = Image.new("RGB", (W, H), (0, 0, 0))
    sd = ImageDraw.Draw(st)
    for i in range(46):
        yy = hz - 40 - i * (17 + (i * 0.85))
        if yy < 120: break
        a = max(0.0, (1 - i / 46)) ** 2.1 * 0.5
        h2 = 3 + i * 0.35
        sd.rectangle([0, yy, W, yy + h2], fill=(int(150*a), int(116*a), int(64*a)))
    st = st.filter(ImageFilter.GaussianBlur(11))
    img = ImageChops.add(img, st)
    return finish(img)

# ---------- COVER C · THE BENDING LINE ----------
def cover_c():
    img = vgrad((W, H), [(0.0, (11, 22, 40)), (0.4, NAVY), (0.72, (24, 44, 72)), (1.0, (9, 18, 34))])
    ln = Image.new("RGB", (W, H), (0, 0, 0))
    ld = ImageDraw.Draw(ln)
    pts = []
    for i in range(1400):
        t = i / 1399
        # enters upper right, descends, bends — a knee — and continues low-left
        x = W * (0.90 - 0.86 * t) + 150 * math.sin(t * math.pi) * (1 - t) * 0.55
        y = 190 + (1330 * (t ** 1.9)) + 210 * math.sin(t * math.pi * 0.92)
        pts.append((x, y))
    for w_, a_ in ((26, 0.16), (14, 0.34), (7, 0.62), (3, 1.0)):
        c = (int(226*a_), int(186*a_), int(120*a_))
        ld.line(pts, fill=c, width=w_, joint="curve")
    ln = ln.filter(ImageFilter.GaussianBlur(3))
    glow = ln.filter(ImageFilter.GaussianBlur(52))
    img = ImageChops.add(img, glow)
    img = ImageChops.add(img, ln)
    img = ImageChops.add(img, radial((W, H), W*0.30, 1500, 780, (54, 42, 26), 0.9, 2.4))
    return finish(img)

specs = [("A", cover_a, ["LIVING", "OBEDIENCE"]),
         ("B", cover_b, ["LIVING", "OBEDIENCE"]),
         ("C", cover_c, ["LIVING", "OBEDIENCE"])]

made = []
for tag, fn, lines in specs:
    im = typeset(fn(), lines)
    p = OUT + "Living-Obedience-Cover-%s.png" % tag
    im.save(p, "PNG")
    made.append(p)
    print("saved", p)

# family strip
sw, sh = 640, 960
strip = Image.new("RGB", (sw*3 + 4*40, sh + 80), (233, 228, 216))
for i, p in enumerate(made):
    strip.paste(Image.open(p).resize((sw, sh), Image.LANCZOS), (40 + i*(sw+40), 40))
strip.save(OUT + "Living-Obedience-Cover-Family.png", "PNG")
print("strip done")
