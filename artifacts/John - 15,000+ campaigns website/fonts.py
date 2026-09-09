#!/usr/bin/env python3
import urllib.request, base64, os, subprocess, sys
from fontTools import ttLib
from fontTools.varLib.instancer import instantiateVariableFont

RAW = "https://raw.githubusercontent.com/google/fonts/main/ofl"
TMP = "/home/claude/build/fonts"; os.makedirs(TMP, exist_ok=True)
UNI = "U+0000-00FF,U+0100-017F,U+2013-2014,U+2018-201F,U+2022,U+2026,U+00B7,U+2192"

def fetch(url, out):
    if not os.path.exists(out):
        urllib.request.urlretrieve(url, out)
    return out

def subset_woff2(src, out):
    subprocess.run([sys.executable,"-m","fontTools.subset",src,f"--unicodes={UNI}",
        "--flavor=woff2","--layout-features=kern,liga","--drop-tables+=DSIG",
        f"--output-file={out}","--no-hinting","--desubroutinize"], check=True, capture_output=True)
    return out

faces = []
# Hanken Grotesk variable -> 400/500/600/700
hg = fetch(f"{RAW}/hankengrotesk/HankenGrotesk%5Bwght%5D.ttf", f"{TMP}/hg.ttf")
for w in (400,500,600,700):
    f = ttLib.TTFont(hg); instantiateVariableFont(f, {"wght": w}, inplace=True)
    inst = f"{TMP}/hg{w}.ttf"; f.save(inst)
    faces.append(("Hanken Grotesk", w, "normal", subset_woff2(inst, f"{TMP}/hg{w}.woff2")))
# Archivo variable -> 600 (labels)
ar = fetch(f"{RAW}/archivo/Archivo%5Bwdth%2Cwght%5D.ttf", f"{TMP}/ar.ttf")
f = ttLib.TTFont(ar); instantiateVariableFont(f, {"wght": 600, "wdth": 100}, inplace=True)
f.save(f"{TMP}/ar600.ttf")
faces.append(("Archivo", 600, "normal", subset_woff2(f"{TMP}/ar600.ttf", f"{TMP}/ar600.woff2")))
# Spectral statics
for fam, wt, style, fn in (("Spectral",400,"normal","Spectral-Regular.ttf"),
                           ("Spectral",400,"italic","Spectral-Italic.ttf"),
                           ("Spectral",500,"normal","Spectral-Medium.ttf"),
                           ("Spectral",600,"normal","Spectral-SemiBold.ttf")):
    p = fetch(f"{RAW}/spectral/{fn}", f"{TMP}/{fn}")
    faces.append((fam, wt, style, subset_woff2(p, f"{TMP}/{fn}.woff2")))

css = ["/* Fonts embedded base64 — zero external requests (Google CDN unreachable at build; fetched from google/fonts GitHub). */"]
total = 0
for fam, wt, style, path in faces:
    b = open(path,"rb").read(); total += len(b)
    css.append(f"@font-face{{font-family:'{fam}';font-weight:{wt};font-style:{style};font-display:swap;"
               f"src:url(data:font/woff2;base64,{base64.b64encode(b).decode()}) format('woff2')}}")
open("/home/claude/site/assets/css/fonts.css","w").write("\n".join(css))
print(f"{len(faces)} faces, {total//1024}KB woff2, css {os.path.getsize('/home/claude/site/assets/css/fonts.css')//1024}KB")
