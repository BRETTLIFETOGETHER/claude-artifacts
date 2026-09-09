import math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops, ImageEnhance
random.seed(9)

FD  = "/mnt/skills/examples/canvas-design/canvas-fonts/"
OUT = "/home/claude/"
def font(n, s): return ImageFont.truetype(FD + n, s)

TEAL=(45,123,121); DEEP=(26,86,85); GOLD=(246,190,100); CREAM=(250,246,238)
INK=(24,36,42); SLATE=(70,84,93)

# ───────── helpers ─────────
def persp(img, dst, out_size):
    w,h = img.size
    src = [(0,0),(w,0),(w,h),(0,h)]
    A=[];B=[]
    for (xd,yd),(xs,ys) in zip(dst,src):
        A.append([xd,yd,1,0,0,0,-xs*xd,-xs*yd]); B.append(xs)
        A.append([0,0,0,xd,yd,1,-ys*xd,-ys*yd]); B.append(ys)
    n=8; M=[A[i][:]+[B[i]] for i in range(n)]
    for i in range(n):
        p=max(range(i,n), key=lambda r: abs(M[r][i])); M[i],M[p]=M[p],M[i]
        pv=M[i][i]
        for j in range(i,n+1): M[i][j]/=pv
        for r in range(n):
            if r!=i and M[r][i]:
                f=M[r][i]
                for j in range(i,n+1): M[r][j]-=f*M[i][j]
    return img.transform(out_size, Image.PERSPECTIVE, [M[i][8] for i in range(n)], Image.BICUBIC)

def grain(size, amt=6):
    w,h=size
    n=Image.new("L",(w//2,h//2)); n.putdata([random.gauss(128,amt) for _ in range((w//2)*(h//2))])
    n=n.resize(size, Image.BILINEAR); return Image.merge("RGB",(n,n,n))

def tracked(d, xy, text, f, fill, track, cx=None):
    x,y=xy
    if cx is not None:
        tot=sum(d.textlength(c,font=f)+track for c in text)-track; x=cx-tot/2
    for c in text:
        d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+track

# ───────── 1 · the devotional cover art ─────────
CW,CH = 1100, 1700
cov = Image.new("RGB",(CW,CH),TEAL)
g=Image.new("L",(1,CH)); gp=g.load()
for y in range(CH):
    t=y/(CH-1); gp[0,y]=int(255*(0.30+0.55*t))
g=g.resize((CW,CH),Image.BILINEAR)
cov=Image.composite(Image.new("RGB",(CW,CH),DEEP), cov, g)
arc=Image.new("RGB",(CW,CH),(0,0,0))
ImageDraw.Draw(arc).ellipse([CW*0.42,-CH*0.10,CW*1.32,CH*0.50], fill=(92,70,32))
cov=ImageChops.add(cov, arc.filter(ImageFilter.GaussianBlur(2)))
d=ImageDraw.Draw(cov)
tracked(d,(0,190),"THE SIGNATRY",font("CrimsonPro-Regular.ttf",34),GOLD,15,cx=CW//2)
tracked(d,(0,470),"40 DAYS OF",font("CrimsonPro-Regular.ttf",56),(196,222,219),13,cx=CW//2)
tracked(d,(0,570),"IRRATIONAL",font("YoungSerif-Regular.ttf",126),CREAM,3,cx=CW//2)
tracked(d,(0,720),"OBEDIENCE",font("YoungSerif-Regular.ttf",126),CREAM,3,cx=CW//2)
d.rectangle([CW//2-90,900,CW//2+90,906],fill=GOLD)
sub=font("CrimsonPro-Italic.ttf",42)
d.text((CW//2,950),"Saying yes to God before",font=sub,fill=(206,228,226),anchor="ma")
d.text((CW//2,1006),"the reasons arrive",font=sub,fill=(206,228,226),anchor="ma")
tracked(d,(0,1470),"STEVE FRENCH",font("CrimsonPro-Regular.ttf",40),GOLD,11,cx=CW//2)
cov=ImageChops.add(cov, grain((CW,CH),5), scale=1, offset=-128)

# ───────── the book, standing on a surface ─────────
W,H = 1900, 2100; SS=2
W2,H2 = W*SS, H*SS
scene=Image.new("RGB",(W2,H2))
g=Image.new("L",(1,H2)); gp=g.load()
for y in range(H2):
    t=y/(H2-1); gp[0,y]=int(232 - 74*max(0.0,(t-0.62)/0.38) + 10*math.sin(min(t,0.62)/0.62*3.1))
g=g.resize((W2,H2),Image.BILINEAR)
scene=Image.merge("RGB",(g.point(lambda v:int(v*1.0)),g.point(lambda v:int(v*0.995)),g.point(lambda v:int(v*0.97))))

cx,cy=int(W2*0.50),int(H2*0.50); fw,fh=int(W2*0.40),int(H2*0.60)
FTL=(cx-fw*0.44, cy-fh*0.50); FTR=(cx+fw*0.56, cy-fh*0.455)
FBR=(cx+fw*0.56, cy+fh*0.515); FBL=(cx-fw*0.44, cy+fh*0.47)
dep=fw*0.115
STL=(FTL[0]-dep, FTL[1]+fh*0.05); SBL=(FBL[0]-dep, FBL[1]+fh*0.05)

cast=Image.new("L",(W2,H2),0)
ImageDraw.Draw(cast).polygon([(STL[0]-40,SBL[1]-16),(FBR[0]+20,FBR[1]-26),
    (FBR[0]+int(fw*0.85),FBR[1]+int(fh*0.26)),(STL[0]+int(fw*0.30),SBL[1]+int(fh*0.30))],fill=126)
cast=cast.filter(ImageFilter.GaussianBlur(110*SS))
scene=Image.composite(Image.new("RGB",(W2,H2),(126,120,110)), scene, cast)
occ=Image.new("L",(W2,H2),0)
ImageDraw.Draw(occ).polygon([(STL[0]-8,SBL[1]-12),(FBR[0]+8,FBR[1]-20),
    (FBR[0]+8,FBR[1]+30),(STL[0]-8,SBL[1]+36)],fill=190)
occ=occ.filter(ImageFilter.GaussianBlur(14*SS))
scene=Image.composite(Image.new("RGB",(W2,H2),(88,82,74)), scene, occ)

spw=260; spine=Image.new("RGB",(spw,CH),DEEP)
spine=ImageChops.add(spine, grain((spw,CH),7), scale=1, offset=-128)
tmp=Image.new("RGB",(CH,spw),(0,0,0)); td=ImageDraw.Draw(tmp)
td.text((CH*0.26,spw*0.5),"40 DAYS OF IRRATIONAL OBEDIENCE",font=font("YoungSerif-Regular.ttf",56),fill=CREAM,anchor="lm")
td.text((CH*0.88,spw*0.5),"FRENCH",font("CrimsonPro-Regular.ttf",34),fill=GOLD,anchor="lm")
spine=ImageChops.add(spine,tmp.rotate(90,expand=True))

sl=persp(spine,[STL,FTL,FBL,SBL],(W2,H2)); sm=persp(Image.new("L",spine.size,255),[STL,FTL,FBL,SBL],(W2,H2))
scene.paste(ImageEnhance.Brightness(sl).enhance(0.60),(0,0),sm)

sheen=Image.new("L",cov.size,0)
ImageDraw.Draw(sheen).polygon([(0,0),(cov.width*0.60,0),(0,cov.height*0.70)],fill=34)
covx=ImageChops.add(cov, Image.merge("RGB",tuple([sheen.filter(ImageFilter.GaussianBlur(110))]*3)))
fl=persp(covx,[FTL,FTR,FBR,FBL],(W2,H2)); fm=persp(Image.new("L",cov.size,255),[FTL,FTR,FBR,FBL],(W2,H2))
scene.paste(fl,(0,0),fm)

pb=Image.new("RGB",(34,CH),(230,224,210)); pd=ImageDraw.Draw(pb)
for i in range(0,34,2): pd.line([i,0,i,CH],fill=(208+((i*3)%20),202+((i*3)%20),188+((i*3)%20)))
PTR=(FTR[0]+fw*0.026,FTR[1]+fh*0.011); PBR=(FBR[0]+fw*0.026,FBR[1]+fh*0.011)
pl=persp(pb,[FTR,PTR,PBR,FBR],(W2,H2)); pm=persp(Image.new("L",pb.size,255),[FTR,PTR,PBR,FBR],(W2,H2))
scene.paste(ImageEnhance.Brightness(pl).enhance(0.90),(0,0),pm)

scene=ImageChops.add(scene, grain((W2,H2),4), scale=1, offset=-128)
vm=Image.new("L",(W2//4,H2//4),0)
ImageDraw.Draw(vm).ellipse([-W2//12,-H2//13,W2//4+W2//12,H2//4+H2//13],fill=255)
vm=vm.resize((W2,H2),Image.BICUBIC).filter(ImageFilter.GaussianBlur(180*SS//2))
scene=Image.composite(scene, Image.blend(scene, Image.new("RGB",(W2,H2),(0,0,0)),0.26), vm)
scene.resize((W,H),Image.LANCZOS).save(OUT+"mockup-book.png","PNG")
print("book done")

# ───────── 2 · the platform on a laptop ─────────
SW,SH = 1760, 1100
scr=Image.new("RGB",(SW,SH),(255,255,255))
sd=ImageDraw.Draw(scr)
sd.rectangle([0,0,SW,74],fill=(238,243,244)); sd.line([0,74,SW,74],fill=(219,228,229),width=2)
for i,c in enumerate([(224,231,232)]*3):
    sd.ellipse([28+i*30,30,44+i*30,46],fill=c)
sd.rounded_rectangle([150,24,SW-40,52],14,fill=(255,255,255))
sd.text((172,30),"thesignatry.com / living-legacy-profile",font=font("CrimsonPro-Regular.ttf",22),fill=(150,163,168))
sd.rectangle([0,74,392,SH],fill=(244,249,248)); sd.line([392,74,392,SH],fill=(226,234,233),width=2)
sd.text((34,120),"The Signatry",font=font("YoungSerif-Regular.ttf",34),fill=TEAL)
for i,(t,on) in enumerate([("Overview",0),("Our profile",1),("Our journey",0),("Family conversation",0),("The pledge",0),("Tools",0)]):
    y=196+i*46
    if on: sd.rounded_rectangle([22,y-10,370,y+32],8,fill=(255,255,255))
    sd.text((36,y),t,font=font("CrimsonPro-Regular.ttf",26),fill=INK if on else (128,142,148))
sd.text((36,520),"THE WHITFIELD FAMILY",font=font("CrimsonPro-Regular.ttf",19),fill=(160,174,180))
sd.text((444,124),"LIVING LEGACY PROFILE  ·  COMPLETED 12 MARCH",font=font("CrimsonPro-Regular.ttf",19),fill=(176,139,63))
sd.text((444,160),"Where your family stands",font=font("YoungSerif-Regular.ttf",50),fill=INK)
dims=[("Faith","Strong",.88,0),("Purpose","Strong",.81,0),("Family","Developing",.54,1),
      ("Generosity","Strong",.84,0),("Legacy","Vulnerable",.31,1),("Impact","Developing",.62,1),
      ("Next generation","Vulnerable",.27,1)]
y=246
for nm,st,v,warn in dims:
    sd.text((444,y),nm,font=font("CrimsonPro-Regular.ttf",24),fill=SLATE)
    sd.text((SW-70,y),st,font=font("CrimsonPro-Regular.ttf",22),fill=(150,163,168),anchor="ra")
    sd.rounded_rectangle([444,y+34,SW-70,y+50],8,fill=(234,240,239))
    sd.rounded_rectangle([444,y+34,444+int((SW-514)*v),y+50],8,fill=GOLD if warn else TEAL)
    y+=86
sd.line([444,y+6,SW-70,y+6],fill=(226,234,233),width=2)
sd.text((444,y+28),"WHERE THE GENERATIONS DISAGREE",font=font("CrimsonPro-Regular.ttf",19),fill=(150,163,168))
for i,(t,s2) in enumerate([("Nobody under forty has decided where real money went","Recommended next  ·  The 21-Day Family Journey"),
                           ("Legacy intentions are held by one person, undocumented","Recommended next  ·  The Family Conversation, then the Pledge")]):
    yy=y+64+i*94
    sd.rounded_rectangle([444,yy,SW-70,yy+76],8,outline=(226,234,233),width=2)
    sd.text((468,yy+16),t,font=font("YoungSerif-Regular.ttf",25),fill=INK)
    sd.text((468,yy+48),s2,font=font("CrimsonPro-Regular.ttf",21),fill=(150,163,168))

LW,LH = 2100, 1500
lap=Image.new("RGB",(LW,LH),(233,231,226))
lg=Image.new("L",(1,LH)); lp=lg.load()
for yy in range(LH):
    t=yy/(LH-1); lp[0,yy]=int(236-56*max(0.0,(t-0.58)/0.42))
lg=lg.resize((LW,LH),Image.BILINEAR)
lap=Image.merge("RGB",(lg,lg,lg.point(lambda v:int(v*0.97))))
ld=ImageDraw.Draw(lap)
bx0,by0,bx1,by1 = 210,120,LW-210,1150
sh=Image.new("L",(LW,LH),0)
ImageDraw.Draw(sh).rounded_rectangle([bx0-30,by0+40,bx1+30,by1+150],44,fill=150)
lap=Image.composite(Image.new("RGB",(LW,LH),(140,136,128)), lap, sh.filter(ImageFilter.GaussianBlur(60)))
ld=ImageDraw.Draw(lap)
ld.rounded_rectangle([bx0,by0,bx1,by1],26,fill=(46,52,56))
ld.rounded_rectangle([bx0+6,by0+6,bx1-6,by1-6],22,fill=(30,35,38))
sx0,sy0 = bx0+38, by0+42
sw_,sh_ = (bx1-38)-sx0, (by1-58)-sy0
lap.paste(scr.resize((sw_,sh_),Image.LANCZOS),(sx0,sy0))
ld.ellipse([LW//2-7,by0+18,LW//2+7,by0+32],fill=(70,78,82))
ld.polygon([(bx0-118,by1),(bx1+118,by1),(bx1+188,by1+82),(bx0-188,by1+82)],fill=(206,210,214))
ld.polygon([(bx0-118,by1),(bx1+118,by1),(bx1+120,by1+12),(bx0-120,by1+12)],fill=(178,184,189))
ld.rounded_rectangle([LW//2-130,by1+58,LW//2+130,by1+70],6,fill=(188,194,199))
lap=ImageChops.add(lap, grain((LW,LH),4), scale=1, offset=-128)
lap.save(OUT+"mockup-laptop.png","PNG")
print("laptop done")
