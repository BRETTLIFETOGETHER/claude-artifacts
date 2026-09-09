import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageEnhance

W, H = 1600, 2400
F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
OUT = "/mnt/user-data/outputs/"
random.seed(21)

def font(n, s): return ImageFont.truetype(F + n, s)

def paper(size, base=(238, 231, 216), fibre=16):
    """Heavy cold-press stock: fibre, mottle, and a soft crumple."""
    w, h = size
    img = Image.new("RGB", size, base)
    n = Image.new("L", (w // 3, h // 3))
    n.putdata([random.gauss(128, fibre) for _ in range((w // 3) * (h // 3))])
    n = n.resize(size, Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.6))
    img = ImageChops.add(img, Image.merge("RGB", (n, n, n)), scale=1, offset=-128)
    # broad mottle
    m = Image.new("L", (w // 26, h // 26))
    m.putdata([random.gauss(128, 34) for _ in range((w // 26) * (h // 26))])
    m = m.resize(size, Image.BICUBIC).filter(ImageFilter.GaussianBlur(26))
    img = ImageChops.add(img, Image.merge("RGB", (m, m, m)), scale=1, offset=-128)
    # crease light
    cr = Image.new("L", size, 128)
    d = ImageDraw.Draw(cr)
    for _ in range(9):
        x0, y0 = random.randint(-200, w), random.randint(-200, h)
        x1, y1 = x0 + random.randint(-900, 900), y0 + random.randint(-1400, 1400)
        d.line([x0, y0, x1, y1], fill=random.choice([112, 146]), width=random.randint(2, 6))
    cr = cr.filter(ImageFilter.GaussianBlur(9))
    img = ImageChops.add(img, Image.merge("RGB", (cr, cr, cr)), scale=1, offset=-128)
    return img

def grain(size, amt=8):
    w, h = size
    n = Image.new("L", (w // 2, h // 2))
    n.putdata([random.gauss(128, amt) for _ in range((w // 2) * (h // 2))])
    n = n.resize(size, Image.BILINEAR)
    return Image.merge("RGB", (n, n, n))

def vignette(img, strength=0.34):
    w, h = img.size
    m = Image.new("L", (w // 4, h // 4), 0)
    ImageDraw.Draw(m).ellipse([-w//9, -h//10, w//4 + w//9, h//4 + h//10], fill=255)
    m = m.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(180))
    return Image.composite(img, Image.blend(img, Image.new("RGB", (w, h), (0, 0, 0)), strength), m)

def brushstroke(draw, pts, width, color, jitter=3):
    """A stroke with a living edge — not a vector line."""
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        w_ = max(2, int(width * (0.72 + 0.28 * math.sin(i / 7.0))))
        draw.line([x0 + random.uniform(-jitter, jitter), y0 + random.uniform(-jitter, jitter),
                   x1 + random.uniform(-jitter, jitter), y1 + random.uniform(-jitter, jitter)],
                  fill=color, width=w_)

def tracked(d, xy, text, f, fill, track=0, cx=None):
    x, y = xy
    if cx is not None:
        tot = sum(d.textlength(c, font=f) + track for c in text) - track
        x = cx - tot / 2
    for c in text:
        d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + track

# ---------------- D · THE PAPER (texture-led, DRIVEN / Born For This lane) --------------
def cover_d():
    img = paper((W, H))
    d = ImageDraw.Draw(img)
    INKY = (26, 34, 46); GOLD = (176, 132, 54); MUTE = (120, 116, 106)

    # a single ochre brush field behind the title — hand-laid, not a rectangle
    band = Image.new("RGB", (W, H), (0, 0, 0))
    bd = ImageDraw.Draw(band)
    for i in range(210):
        yy = 1180 + i * 3.1
        x0 = 150 + 40 * math.sin(i / 26.0) + random.uniform(-9, 9)
        x1 = W - 150 + 44 * math.sin(i / 21.0 + 1.4) + random.uniform(-9, 9)
        a = 0.30 * (1 - abs(i - 105) / 118.0)
        bd.line([x0, yy, x1, yy], fill=(int(196*a), int(150*a), int(70*a)), width=5)
    band = band.filter(ImageFilter.GaussianBlur(13))
    img = ImageChops.add(img, band)

    tracked(d, (0, 300), "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 31), GOLD, track=15, cx=W//2)
    d.rectangle([W//2 - 46, 372, W//2 + 46, 375], fill=GOLD)

    ttl = font("YoungSerif-Regular.ttf", 196)
    d.text((W//2, 1180), "LIVING", font=ttl, fill=INKY, anchor="ma")
    d.text((W//2, 1380), "OBEDIENCE", font=font("YoungSerif-Regular.ttf", 152), fill=INKY, anchor="ma")

    # underline, drawn as a stroke
    brushstroke(d, [(360 + i*14, 1620 + 5*math.sin(i/5.0)) for i in range(63)], 9, GOLD, jitter=2)

    sub = font("CrimsonPro-Italic.ttf", 50)
    d.text((W//2, 1700), "Saying yes to God with your life, your family,", font=sub, fill=(96, 92, 84), anchor="ma")
    d.text((W//2, 1764), "your business, your wealth.", font=sub, fill=(96, 92, 84), anchor="ma")

    tracked(d, (0, 2166), "STEVE FRENCH", font("CrimsonPro-Regular.ttf", 39), INKY, track=11, cx=W//2)
    tracked(d, (0, 2228), "WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 29), MUTE, track=12, cx=W//2)

    img = ImageChops.add(img, grain((W, H), 7), scale=1, offset=-128)
    return vignette(img, 0.30)

# ---------------- E · THE PAINTED FIELD (ONE / brush lane) --------------
def cover_e():
    img = Image.new("RGB", (W, H), (14, 24, 40))
    # layered brush field, warm over cool, built stroke by stroke
    fld = Image.new("RGB", (W, H), (0, 0, 0))
    fd = ImageDraw.Draw(fld)
    palette = [(58, 92, 140), (34, 62, 104), (168, 120, 52), (206, 158, 78), (92, 70, 44)]
    for k in range(240):
        c = palette[k % len(palette)]
        a = random.uniform(0.10, 0.30)
        col = (int(c[0]*a), int(c[1]*a), int(c[2]*a))
        y0 = random.uniform(60, 1360)
        amp = random.uniform(20, 90)
        pts = [(x, y0 + amp * math.sin(x / random.uniform(160, 420) + k)) for x in range(-80, W + 80, 26)]
        brushstroke(fd, pts, random.randint(14, 54), col, jitter=5)
    fld = fld.filter(ImageFilter.GaussianBlur(7))
    img = ImageChops.add(img, fld)
    # a warm core the eye lands on
    gl = Image.new("RGB", (W//4, H//4), (0, 0, 0))
    gd = ImageDraw.Draw(gl)
    gd.ellipse([W//16, H//22, W//4 - W//16, H//4 - H//5], fill=(64, 46, 22))
    img = ImageChops.add(img, gl.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(150)))
    # settle the lower third
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).rectangle([0, 1340, W, H], fill=255)
    sh = sh.filter(ImageFilter.GaussianBlur(190))
    img = Image.composite(Image.blend(img, Image.new("RGB", (W, H), (8, 15, 27)), 0.80), img, sh)

    d = ImageDraw.Draw(img)
    CREAM = (245, 240, 230); GOLD = (206, 164, 88)
    tracked(d, (0, 1560), "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 30), GOLD, track=15, cx=W//2)
    ttl = font("YoungSerif-Regular.ttf", 178)
    d.text((W//2, 1650), "LIVING", font=ttl, fill=CREAM, anchor="ma")
    d.text((W//2, 1830), "OBEDIENCE", font=font("YoungSerif-Regular.ttf", 138), fill=CREAM, anchor="ma")
    d.rectangle([W//2 - 74, 2030, W//2 + 74, 2034], fill=GOLD)
    sub = font("CrimsonPro-Italic.ttf", 45)
    d.text((W//2, 2072), "Saying yes to God with your life, your family,", font=sub, fill=(198, 190, 176), anchor="ma")
    d.text((W//2, 2130), "your business, your wealth.", font=sub, fill=(198, 190, 176), anchor="ma")
    tracked(d, (0, 2250), "STEVE FRENCH  ·  WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 30), (156, 150, 138), track=9, cx=W//2)

    img = ImageChops.add(img, grain((W, H), 9), scale=1, offset=-128)
    return vignette(img, 0.42)

for tag, fn in (("D", cover_d), ("E", cover_e)):
    p = OUT + "Living-Obedience-Cover-%s.png" % tag
    fn().save(p, "PNG"); print("saved", p)

sw, sh = 620, 930
files = ["Living-Obedience-Cover-D.png", "Living-Obedience-Cover-E.png",
         "Living-Obedience-Cover-A.png", "Living-Obedience-Cover-B.png"]
strip = Image.new("RGB", (sw*4 + 5*34, sh + 68), (233, 228, 216))
for i, f in enumerate(files):
    strip.paste(Image.open(OUT + f).resize((sw, sh), Image.LANCZOS), (34 + i*(sw+34), 34))
strip.save(OUT + "Living-Obedience-Cover-Family-v2.png", "PNG")
print("strip v2 done")
