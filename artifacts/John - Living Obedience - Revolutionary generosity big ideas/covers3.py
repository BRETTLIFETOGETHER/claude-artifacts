import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
random.seed(11)

W, H = 1600, 2400
FD = "/mnt/skills/examples/canvas-design/canvas-fonts/"
OUT = "/mnt/user-data/outputs/"
def font(n, s): return ImageFont.truetype(FD + n, s)

def grain(size, amt=8):
    w, h = size
    n = Image.new("L", (w//2, h//2))
    n.putdata([random.gauss(128, amt) for _ in range((w//2)*(h//2))])
    return Image.merge("RGB", tuple([n.resize(size, Image.BILINEAR)]*3))

def vignette(img, s=0.38):
    w, h = img.size
    m = Image.new("L", (w//4, h//4), 0)
    ImageDraw.Draw(m).ellipse([-w//9, -h//10, w//4+w//9, h//4+h//10], fill=255)
    m = m.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(180))
    return Image.composite(img, Image.blend(img, Image.new("RGB",(w,h),(0,0,0)), s), m)

def cloth(size, base, warp=13):
    """A woven, book-cloth surface — the tooth of a bound board."""
    w, h = size
    img = Image.new("RGB", size, base)
    n = Image.new("L", (w//2, h//2))
    n.putdata([random.gauss(128, warp) for _ in range((w//2)*(h//2))])
    n = n.resize(size, Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.5))
    img = ImageChops.add(img, Image.merge("RGB",(n,n,n)), scale=1, offset=-128)
    weave = Image.new("L", size, 128)
    wd = ImageDraw.Draw(weave)
    for y in range(0, h, 3): wd.line([0,y,w,y], fill=134)
    for x in range(0, w, 3): wd.line([x,0,x,h], fill=122)
    weave = weave.filter(ImageFilter.GaussianBlur(0.7))
    return ImageChops.add(img, Image.merge("RGB",(weave,weave,weave)), scale=1, offset=-128)

def tracked(d, y, text, f, fill, track, cx=W//2):
    tot = sum(d.textlength(c, font=f) + track for c in text) - track
    x = cx - tot/2
    for c in text:
        d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + track

# ---------------- F · THE IMPRINT ----------------
# Type as the whole cover. Foil-stamped on book cloth. An ideas book, not a devotional.
def cover_f():
    img = cloth((W, H), (23, 33, 48), warp=11)
    # a faint blind-deboss rectangle: the printer's frame
    fr = Image.new("L", (W, H), 128)
    fd = ImageDraw.Draw(fr)
    fd.rectangle([120, 120, W-120, H-120], outline=118, width=5)
    fd.rectangle([126, 126, W-126, H-126], outline=138, width=3)
    fr = fr.filter(ImageFilter.GaussianBlur(3))
    img = ImageChops.add(img, Image.merge("RGB",(fr,fr,fr)), scale=1, offset=-128)

    img = ImageChops.add(img, grain((W,H), 7), scale=1, offset=-128)
    img = vignette(img, 0.34)
    d = ImageDraw.Draw(img)
    GOLD=(198,158,84); FOIL=(232,204,146); CREAM=(240,235,224); MUTE=(139,148,162)

    tracked(d, 300, "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 30), MUTE, 16)

    big = font("YoungSerif-Regular.ttf", 214)
    # foil: a warm ghost offset behind, then the strike
    tracked(d, 906, "LIVING", big, (86,66,32), 4)
    tracked(d, 900, "LIVING", big, FOIL, 4)
    small = font("YoungSerif-Regular.ttf", 150)
    tracked(d, 1156, "OBEDIENCE", small, (86,66,32), 4)
    tracked(d, 1150, "OBEDIENCE", small, FOIL, 4)

    d.rectangle([W//2-120, 1410, W//2+120, 1414], fill=GOLD)

    sub = font("CrimsonPro-Italic.ttf", 52)
    d.text((W//2, 1480), "Saying yes to God with your life,", font=sub, fill=(196,202,212), anchor="ma")
    d.text((W//2, 1546), "your family, your business, your wealth.", font=sub, fill=(196,202,212), anchor="ma")

    tracked(d, 2130, "STEVE FRENCH", font("CrimsonPro-Regular.ttf", 42), CREAM, 12)
    tracked(d, 2198, "WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 30), MUTE, 13)
    return img

# ---------------- G · THE SIGNATURE ----------------
# The Signatry means the one who signs. The mark is the cover.
def cover_g():
    img = cloth((W, H), (238, 233, 222), warp=9)
    # ink signature — one continuous confident stroke, drawn not typeset
    ink = Image.new("RGB", (W, H), (0,0,0))
    idr = ImageDraw.Draw(ink)
    pts=[]
    for i in range(1200):
        t=i/1199
        x = 300 + 1000*t
        y = (1250 + 150*math.sin(t*7.4) - 260*math.sin(t*2.1)
             + 90*math.sin(t*15.0)*(1-t))
        pts.append((x,y))
    for wdt,a in ((17,0.30),(11,0.62),(6,1.0)):
        c=(int(26*a),int(32*a),int(44*a))
        for i in range(len(pts)-1):
            jx,jy = random.uniform(-1.6,1.6), random.uniform(-1.6,1.6)
            idr.line([pts[i][0]+jx,pts[i][1]+jy,pts[i+1][0]+jx,pts[i+1][1]+jy], fill=c, width=wdt)
    # the underscore of a signed line
    idr.line([300,1470,1300,1470], fill=(150,150,150), width=3)
    ink = ink.filter(ImageFilter.GaussianBlur(1.6))
    img = ImageChops.subtract(img, ink)

    img = ImageChops.add(img, grain((W,H), 6), scale=1, offset=-128)
    img = vignette(img, 0.22)
    d = ImageDraw.Draw(img)
    INK=(24,32,46); GOLD=(158,118,44); MUTE=(120,116,106)

    tracked(d, 250, "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 30), GOLD, 16)
    tracked(d, 470, "LIVING", font("YoungSerif-Regular.ttf", 190), INK, 4)
    tracked(d, 690, "OBEDIENCE", font("YoungSerif-Regular.ttf", 132), INK, 4)
    d.rectangle([W//2-110, 890, W//2+110, 894], fill=GOLD)
    sub = font("CrimsonPro-Italic.ttf", 48)
    d.text((W//2, 940), "Saying yes to God with your life,", font=sub, fill=(92,90,84), anchor="ma")
    d.text((W//2, 1002), "your family, your business, your wealth.", font=sub, fill=(92,90,84), anchor="ma")
    tracked(d, 1660, "SIGNED", font("CrimsonPro-Regular.ttf", 26), MUTE, 14)
    tracked(d, 2140, "STEVE FRENCH", font("CrimsonPro-Regular.ttf", 40), INK, 12)
    tracked(d, 2206, "WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 29), MUTE, 13)
    return img

# ---------------- H · THE TURN ----------------
# The typography performs the idea: LIVING light and open, OBEDIENCE set immovable.
def cover_h():
    img = cloth((W, H), (14, 22, 34), warp=10)
    # one shaft of light, tight and architectural — a suggestion, not a landscape
    beam = Image.new("RGB", (W, H), (0,0,0))
    bd = ImageDraw.Draw(beam)
    for i in range(300):
        t=i/299
        x0 = 470 + 210*t; x1 = 700 + 500*t
        y  = 60 + 2200*t
        a  = (1-t)**1.7 * 0.42
        bd.polygon([(x0,y),(x1,y),(x1,y+9),(x0,y+9)], fill=(int(210*a),int(176*a),int(112*a)))
    beam = beam.filter(ImageFilter.GaussianBlur(60))
    img = ImageChops.add(img, beam)

    img = ImageChops.add(img, grain((W,H), 8), scale=1, offset=-128)
    img = vignette(img, 0.44)
    d = ImageDraw.Draw(img)
    CREAM=(244,239,229); GOLD=(206,164,88); MUTE=(150,158,172)

    tracked(d, 262, "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 29), GOLD, 16)
    # LIVING — open, letterspaced, weightless
    tracked(d, 1490, "L I V I N G", font("CrimsonPro-Regular.ttf", 122), CREAM, 16)
    # OBEDIENCE — set heavy, immovable, filling the measure
    tracked(d, 1650, "OBEDIENCE", font("YoungSerif-Regular.ttf", 168), CREAM, 2)
    d.rectangle([W//2-110, 1900, W//2+110, 1904], fill=GOLD)
    sub = font("CrimsonPro-Italic.ttf", 46)
    d.text((W//2, 1950), "Saying yes to God with your life,", font=sub, fill=(190,196,206), anchor="ma")
    d.text((W//2, 2010), "your family, your business, your wealth.", font=sub, fill=(190,196,206), anchor="ma")
    tracked(d, 2150, "STEVE FRENCH", font("CrimsonPro-Regular.ttf", 38), CREAM, 11)
    tracked(d, 2214, "WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 28), MUTE, 12)
    return img

for tag, fn in (("F", cover_f), ("G", cover_g), ("H", cover_h)):
    p = OUT + "Living-Obedience-Cover-%s.png" % tag
    fn().save(p, "PNG"); print("saved", p)

sw, sh = 660, 990
strip = Image.new("RGB", (sw*3 + 4*38, sh + 76), (231, 226, 214))
for i, t in enumerate("FGH"):
    strip.paste(Image.open(OUT+"Living-Obedience-Cover-%s.png"%t).resize((sw,sh), Image.LANCZOS), (38+i*(sw+38), 38))
strip.save(OUT + "Living-Obedience-Cover-Family-v3.png", "PNG")
print("strip v3")
