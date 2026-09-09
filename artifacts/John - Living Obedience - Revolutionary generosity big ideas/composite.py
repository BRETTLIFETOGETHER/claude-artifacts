import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
random.seed(5)

W, H = 1600, 2400
F = "/mnt/skills/examples/canvas-design/canvas-fonts/"
def font(n, s): return ImageFont.truetype(F + n, s)

src = Image.open("/mnt/user-data/uploads/Screenshot_2026-08-18_at_4_37_19_PM.png").convert("RGB")
art = src.crop((758, 352, 1418, 1010))
tail = src.crop((758, 1006, 1418, 1330))

# --- build the 2:3 canvas: art on top, wheat extended below ---
canvas = Image.new("RGB", (W, H))
aw, ah = art.size
art_r = art.resize((W, int(ah * W / aw)), Image.LANCZOS)
canvas.paste(art_r, (0, 0))
y = art_r.height

tail_r = tail.resize((W, int(tail.height * W / tail.width)), Image.LANCZOS)
while y < H:
    canvas.paste(tail_r, (0, y))
    y += tail_r.height
    tail_r = tail_r.transpose(Image.FLIP_TOP_BOTTOM)

# --- deepen the lower third into a warm shadow so type reads (tonal, never a box) ---
grad = Image.new("L", (1, H), 0)
gp = grad.load()
for yy in range(H):
    t = (yy - 1180) / (H - 1180)
    gp[0, yy] = 0 if t < 0 else int(255 * min(1.0, (t ** 1.35) * 1.02))
grad = grad.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(60))
shadow = Image.new("RGB", (W, H), (18, 16, 14))
canvas = Image.composite(shadow, canvas, grad)
# recover a breath of warmth in the type zone so it isn't dead black
warm = Image.new("RGB", (W, H), (0, 0, 0))
wd = ImageDraw.Draw(warm)
wd.ellipse([W*0.10, 1500, W*0.90, 2260], fill=(34, 26, 16))
canvas = ImageChops.add(canvas, warm.filter(ImageFilter.GaussianBlur(190)))

# --- family grain + vignette ---
n = Image.new("L", (W//2, H//2))
n.putdata([random.gauss(128, 8) for _ in range((W//2)*(H//2))])
n = n.resize((W, H), Image.BILINEAR)
canvas = ImageChops.add(canvas, Image.merge("RGB", (n, n, n)), scale=1, offset=-128)
m = Image.new("L", (W//4, H//4), 0)
ImageDraw.Draw(m).ellipse([-W//9, -H//10, W//4 + W//9, H//4 + H//10], fill=255)
m = m.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(180))
canvas = Image.composite(canvas, Image.blend(canvas, Image.new("RGB", (W, H), (0,0,0)), 0.40), m)

# --- the family type system, bound last ---
d = ImageDraw.Draw(canvas)
CREAM = (247, 242, 232); GOLD = (206, 164, 88); MUTE = (168, 160, 146)
cx = W // 2

def tracked(y, text, f, fill, track):
    tot = sum(d.textlength(c, font=f) + track for c in text) - track
    x = cx - tot / 2
    for c in text:
        d.text((x, y), c, font=f, fill=fill); x += d.textlength(c, font=f) + track

tracked(1512, "THE SIGNATRY", font("CrimsonPro-Regular.ttf", 30), GOLD, 15)
tracked(1610, "LIVING", font("LibreBaskerville-Regular.ttf", 128), CREAM, 6)
tracked(1772, "OBEDIENCE", font("LibreBaskerville-Regular.ttf", 128), CREAM, 6)
d.rectangle([cx - 78, 1986, cx + 78, 1990], fill=GOLD)
sub = font("CrimsonPro-Italic.ttf", 46)
d.text((cx, 2030), "Saying yes to God with your life, your family,", font=sub, fill=(206, 198, 184), anchor="ma")
d.text((cx, 2090), "your business, your wealth.", font=sub, fill=(206, 198, 184), anchor="ma")
tracked(2200, "STEVE FRENCH", font("CrimsonPro-Regular.ttf", 36), (233, 199, 138), 10)
tracked(2262, "WITH DALE ARMSTRONG", font("CrimsonPro-Regular.ttf", 29), MUTE, 12)

canvas.save("/mnt/user-data/outputs/Living-Obedience-Cover-KneelingField-MOCKUP.png", "PNG")
print("composited")
