import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance
random.seed(3)

OUT = "/mnt/user-data/outputs/"
SCENE_W, SCENE_H = 2000, 2500          # 4:5 presentation crop
SS = 2                                  # supersample for clean edges

def grain(size, amt=6):
    w, h = size
    n = Image.new("L", (w//2, h//2))
    n.putdata([random.gauss(128, amt) for _ in range((w//2)*(h//2))])
    return Image.merge("RGB", tuple([n.resize(size, Image.BILINEAR)]*3))

def persp_quad(img, dst, out_size):
    """Map the image's four corners onto dst using PIL's perspective transform."""
    w, h = img.size
    src = [(0,0),(w,0),(w,h),(0,h)]
    # solve for the 8 coefficients (dst -> src, as PIL wants the inverse map)
    A = []; B = []
    for (xd, yd), (xs, ys) in zip(dst, src):
        A.append([xd, yd, 1, 0, 0, 0, -xs*xd, -xs*yd]); B.append(xs)
        A.append([0, 0, 0, xd, yd, 1, -ys*xd, -ys*yd]); B.append(ys)
    # gaussian elimination
    n = 8
    M = [A[i][:] + [B[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        pv = M[i][i]
        for j in range(i, n+1): M[i][j] /= pv
        for r in range(n):
            if r != i and M[r][i]:
                f = M[r][i]
                for j in range(i, n+1): M[r][j] -= f*M[i][j]
    coeffs = [M[i][8] for i in range(n)]
    return img.transform(out_size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)

# ---------- the surface ----------
W, H = SCENE_W*SS, SCENE_H*SS
scene = Image.new("RGB", (W, H), (30, 27, 24))
# a warm wall falling to a darker table
g = Image.new("L", (1, H))
gp = g.load()
for y in range(H):
    t = y/(H-1)
    gp[0,y] = int(56 + 40*math.sin(min(t,0.62)/0.62*math.pi*0.5) - 62*max(0.0,(t-0.62)/0.38))
g = g.resize((W, H), Image.BILINEAR)
scene = Image.merge("RGB", (
    g.point(lambda v: int(v*1.02)), g.point(lambda v: int(v*0.94)), g.point(lambda v: int(v*0.82))))
# a soft key light from upper left
kl = Image.new("RGB", (W//4, H//4), (0,0,0))
ImageDraw.Draw(kl).ellipse([-W//14, -H//16, W//4-W//12, H//4-H//7], fill=(70, 62, 48))
scene = ImageChops.add(scene, kl.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(240*SS//2)))

# ---------- geometry ----------
front = Image.open(OUT + "Living-Obedience-Cover-F.png").convert("RGB")
# subtle cover sheen so the board reads as a physical object
sheen = Image.new("L", front.size, 0)
sd = ImageDraw.Draw(sheen)
sd.polygon([(0,0),(front.width*0.62,0),(0,front.height*0.74)], fill=46)
sheen = sheen.filter(ImageFilter.GaussianBlur(120))
front = ImageChops.add(front, Image.merge("RGB",(sheen,sheen,sheen)))

# spine art: same cloth, gold rule, vertical title
SPW, SPH = 300, front.height
spine = Image.new("RGB", (SPW, SPH), (23, 33, 48))
spine = ImageChops.add(spine, grain((SPW, SPH), 9), scale=1, offset=-128)
sp = ImageDraw.Draw(spine)
sp.rectangle([0, 0, 10, SPH], fill=(15, 22, 33))
sp.rectangle([SPW-10, 0, SPW, SPH], fill=(15, 22, 33))
from PIL import ImageFont
FD = "/mnt/skills/examples/canvas-design/canvas-fonts/"
sf = ImageFont.truetype(FD + "YoungSerif-Regular.ttf", 74)
lab = ImageFont.truetype(FD + "CrimsonPro-Regular.ttf", 34)
tmp = Image.new("RGB", (SPH, SPW), (0,0,0))
td = ImageDraw.Draw(tmp)
td.text((SPH*0.30, SPW*0.5), "LIVING OBEDIENCE", font=sf, fill=(232, 204, 146), anchor="lm")
td.text((SPH*0.86, SPW*0.5), "FRENCH", font=lab, fill=(200, 206, 216), anchor="lm")
spine = ImageChops.add(spine, tmp.rotate(90, expand=True))

# corner targets — a book standing, turned slightly, seen a little from above
cx, cy = int(W*0.50), int(H*0.50)
fw, fh = int(W*0.415), int(H*0.585)
FTL = (cx - fw*0.42, cy - fh*0.50)
FTR = (cx + fw*0.58, cy - fh*0.455)
FBR = (cx + fw*0.58, cy + fh*0.515)
FBL = (cx - fw*0.42, cy + fh*0.47)
depth = fw*0.155
STL = (FTL[0] - depth, FTL[1] + fh*0.055)
SBL = (FBL[0] - depth, FBL[1] + fh*0.055)

# ---------- contact shadow ----------
sh = Image.new("L", (W, H), 0)
ImageDraw.Draw(sh).polygon([ (STL[0]-40, SBL[1]-10), (FBR[0]+30, FBR[1]-14),
                             (FBR[0]+250, FBR[1]+120), (STL[0]-150, SBL[1]+130) ], fill=185)
sh = sh.filter(ImageFilter.GaussianBlur(70*SS))
scene = Image.composite(Image.new("RGB",(W,H),(12,10,9)), scene, sh)

# ---------- place spine then front ----------
sp_layer = persp_quad(spine, [STL, FTL, FBL, SBL], (W, H))
sp_mask = persp_quad(Image.new("L", spine.size, 255), [STL, FTL, FBL, SBL], (W, H))
sp_layer = ImageEnhance.Brightness(sp_layer).enhance(0.62)
scene.paste(sp_layer, (0,0), sp_mask)

fr_layer = persp_quad(front, [FTL, FTR, FBR, FBL], (W, H))
fr_mask  = persp_quad(Image.new("L", front.size, 255), [FTL, FTR, FBR, FBL], (W, H))
scene.paste(fr_layer, (0,0), fr_mask)

# ---------- page block along the right edge ----------
pb = Image.new("RGB", (40, front.height), (226, 220, 206))
pd = ImageDraw.Draw(pb)
for i in range(0, 40, 2): pd.line([i,0,i,front.height], fill=(206+((i*3)%22), 200+((i*3)%22), 186+((i*3)%22)))
PTR = (FTR[0] + fw*0.030, FTR[1] + fh*0.012)
PBR = (FBR[0] + fw*0.030, FBR[1] + fh*0.012)
pb_layer = persp_quad(pb, [FTR, PTR, PBR, FBR], (W, H))
pb_mask  = persp_quad(Image.new("L", pb.size, 255), [FTR, PTR, PBR, FBR], (W, H))
scene.paste(ImageEnhance.Brightness(pb_layer).enhance(0.86), (0,0), pb_mask)

# ---------- finish ----------
scene = ImageChops.add(scene, grain((W, H), 5), scale=1, offset=-128)
vm = Image.new("L", (W//4, H//4), 0)
ImageDraw.Draw(vm).ellipse([-W//11, -H//12, W//4+W//11, H//4+H//12], fill=255)
vm = vm.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(200*SS//2))
scene = Image.composite(scene, Image.blend(scene, Image.new("RGB",(W,H),(0,0,0)), 0.42), vm)

scene = scene.resize((SCENE_W, SCENE_H), Image.LANCZOS)
scene.save(OUT + "Living-Obedience-Hardcover-Mockup.png", "PNG")
print("mockup rendered")
