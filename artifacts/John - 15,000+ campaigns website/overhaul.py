#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Taxonomy overhaul surgeon — executes Brett's dictated decisions (2026-08-11 sheet, "Go").
Deletions · tool extraction · duplicate collapse (original-subtitle priority) · suffix folds
· renames · display-category assignment with splits and Legacy pulls · manifest of every action."""
import json, re, subprocess, hashlib
from collections import defaultdict

SITE = "/home/claude/site"
d = json.load(open(f"{SITE}/data/index.json"))
C = {k: i for i, k in enumerate(d["cols"])}
rows = d["rows"]
MAN = {"deleted": [], "tools": [], "collapsed": [], "renamed": [], "dc": {}, "notes": []}

# original subtitles (pre-generation) from the first commit
orig = json.loads(subprocess.run(["git","-C",SITE,"show","a43c5eb:data/index.json"],
                                 capture_output=True,text=True).stdout)
OC = {k:i for i,k in enumerate(orig["cols"])}
ORIG_S = {r[OC["id"]]: r[OC["s"]] for r in orig["rows"]}

def by_id(i): return next(r for r in rows if r[C["id"]]==i)
def exists(i): return any(r[C["id"]]==i for r in rows)

# ---------- 1 · deletions ----------
DEL = set()
DEL |= {"M-00658","M-00759","M-00760","M-00761"}                       # Leverage family
DEL.add("M-01406")                                                     # bare "Priorities"
DEL |= {r[C["id"]] for r in rows if "church formation" in r[C["t"]].lower()}
DEL |= {"M-16249","M-09659","M-15679"}                                 # Complete Journey / Resource Rack / Gerasene
DEL |= {"M-10577","M-10869"}                                           # Co-Parenting With Grace ×2
DEL.add("M-10897")                                                     # PTSD and the Family
DEL |= {"M-09676","M-04222","M-04239","M-09582","M-09580","M-00047","M-09685"}  # pastor library set
DEL.add("M-11512")                                                     # superseded by M-11497
DEL.add("M-10671")                                                     # Justice Without Bitterness (parked default)
for probe,label in [("understanding god","Understanding God's Design for Sexuality"),
                    ("non-negotiab","…Are Non-Negotiable")]:
    hits=[r[C["id"]] for r in rows if probe in r[C["t"]].lower()]
    if hits: DEL |= set(hits)
    else: MAN["notes"].append(f"'{label}' not found in catalog — nothing to delete")

# ---------- 2 · tools extraction ----------
TOOL_IDS = ["M-09677","M-09583","M-09579","M-09683","M-08573"]
TOOLS=[]
for tid in TOOL_IDS:
    if exists(tid):
        r=by_id(tid)
        TOOLS.append({"id":tid,"t":r[C["t"]],"s":r[C["s"]] or ""})
        DEL.add(tid)
MAN["tools"]=[t["t"] for t in TOOLS]

# ---------- 3 · duplicate collapse + suffix folds ----------
GR = {"AA":6,"A":5,"B":4,"C":3,"D":2}
def keep_score(r):
    return ((1 if ORIG_S.get(r[C["id"]]) else 0), GR.get(r[C["g"]],0), -int(r[C["id"]][2:]))
groups=defaultdict(list)
for r in rows:
    if r[C["id"]] in DEL: continue
    groups[r[C["t"]].strip().lower()].append(r)
for key,g in groups.items():
    if len(g)<2: continue
    if key=="open hands":
        g.sort(key=lambda r: (("freedom" in (ORIG_S.get(r[C["id"]]) or "").lower()), )+keep_score(r), reverse=True)
    else:
        g.sort(key=keep_score, reverse=True)
    keeper=g[0]
    for r in g[1:]:
        DEL.add(r[C["id"]])
        MAN["collapsed"].append({"cut":r[C["id"]],"kept":keeper[C["id"]],"title":r[C["t"]]})
    if key=="new beginnings":
        keeper[C["s"]]="A Fresh Start in Your Walk with God"
    if key=="caring for aging parents":
        keeper[C["t"]]="Caregiver Burnout"; keeper[C["s"]]="Caring for Aging Parents Without Losing Yourself"
        MAN["renamed"].append({"id":keeper[C["id"]],"to":"Caregiver Burnout"})
# suffix folds: "X — Small Group Curriculum/Series" where base X survives
titles_now={r[C["t"]].strip().lower() for r in rows if r[C["id"]] not in DEL}
sfx=re.compile(r"^(.+?)\s*[-–—:]\s*small group (curriculum|series)$", re.I)
for r in rows:
    if r[C["id"]] in DEL: continue
    m=sfx.match(r[C["t"]].strip())
    if m and m.group(1).strip().lower() in titles_now:
        DEL.add(r[C["id"]])
        MAN["collapsed"].append({"cut":r[C["id"]],"kept":"base: "+m.group(1).strip(),"title":r[C["t"]]})

# ---------- 4 · renames ----------
for rid,newt,news in [("M-15814","In Spirit and Truth",None),
                      ("M-11508","Faith, Family, Future",None)]:
    if exists(rid) and rid not in DEL:
        r=by_id(rid); MAN["renamed"].append({"id":rid,"from":r[C["t"]],"to":newt})
        r[C["t"]]=newt
        if news: r[C["s"]]=news
hits=[r for r in rows if r[C["id"]] not in DEL and re.search(r"every ?day word", r[C["t"]], re.I) and "experience" in r[C["t"]].lower()]
for r in hits:
    MAN["renamed"].append({"id":r[C["id"]],"from":r[C["t"]],"to":"Every Day Word"})
    r[C["t"]]="Every Day Word"
if not hits: MAN["notes"].append("'Every Day Word Experience' not found — no rename needed")

# ---------- 5 · apply deletions ----------
before=len(rows)
rows=[r for r in rows if r[C["id"]] not in DEL]
MAN["deleted"]=sorted(DEL)
d["rows"]=rows

# ---------- 6 · display categories ----------
CALLING=re.compile(r"\bcall(ed|ing)?\b|vocation|assignment|commission|\bsent\b", re.I)
LEGACY =re.compile(r"\blegacy\b|wealth transfer|estate|inherit|heirloom", re.I)
MARRY  =re.compile(r"marri|husband|wife|spouse|wedding|vows|couple|newlywed", re.I)
DCATS=[]
def dc(name,slug,parent): DCATS.append({"id":len(DCATS),"name":name,"slug":slug,"ch":parent}); return len(DCATS)-1
MAP={}
for i,ch in enumerate(d["channels"]):
    n=ch["name"]
    if i==0:
        MAP[(0,"a")]=dc("Purpose","purpose",0); MAP[(0,"b")]=dc("Calling","calling",0)
    elif i==5:
        MAP[(5,"a")]=dc("Generosity","generosity",5); MAP[(5,"b")]=dc("Legacy","legacy",5)
    elif i==7:
        MAP[(7,"a")]=dc("Marriage","marriage",7); MAP[(7,"b")]=dc("Relationships","relationships",7)
    elif i==6:
        MAP[(6,)]=dc("Family Legacy By Design","family-legacy-by-design",6)
    elif i==14:
        MAP[(14,)]=dc("Church Staff & Leadership","church-staff",14)
    else:
        MAP[(i,)]=dc(n, ch["slug"], i)
LEG_DC = MAP[(5,"b")]
counts=defaultdict(int)
for r in rows:
    ch=r[C["ch"]]; t=r[C["t"]]
    if ch==0:  v = MAP[(0,"b")] if CALLING.search(t) else MAP[(0,"a")]
    elif ch==5: v = MAP[(5,"b")] if LEGACY.search(t) else MAP[(5,"a")]
    elif ch==7: v = MAP[(7,"a")] if MARRY.search(t) else MAP[(7,"b")]
    elif ch in (13,15) and LEGACY.search(t): v = LEG_DC        # Legacy pull
    else: v = MAP.get((ch,), MAP.get((ch,"a"), 0))
    r.append(v) if len(r)==len(d["cols"]) else None
if "dc" not in d["cols"]:
    d["cols"].append("dc")
for r in rows:
    if len(r)==len(d["cols"])-0 and len(r)!=len(d["cols"]): pass
# ensure every row has dc (appended above only when length matched pre-append; redo safely)
DCI=d["cols"].index("dc")
for r in rows:
    while len(r)<len(d["cols"]): r.append(None)
    ch=r[C["ch"]]; t=r[C["t"]]
    if ch==0:  v = MAP[(0,"b")] if CALLING.search(t) else MAP[(0,"a")]
    elif ch==5: v = MAP[(5,"b")] if LEGACY.search(t) else MAP[(5,"a")]
    elif ch==7: v = MAP[(7,"a")] if MARRY.search(t) else MAP[(7,"b")]
    elif ch in (13,15) and LEGACY.search(t): v = LEG_DC
    else: v = MAP.get((ch,))
    r[DCI]=v; counts[v]+=1
d["dcats"]=DCATS
MAN["dc"]={DCATS[k]["name"]:v for k,v in sorted(counts.items())}

# ---------- 7 · affinity chip map (from the generator's bit table) ----------
d["affs"]=[{"bit":1,"name":"Men"},{"bit":2,"name":"Women"},{"bit":6,"name":"Couples"},
           {"bit":3,"name":"Young Adults"},{"bit":4,"name":"Students"},{"bit":5,"name":"Kids & Family"},
           {"bit":7,"name":"Seniors"},{"bit":9,"name":"Leaders & Staff"}]
MAN["notes"].append("No 'Singles' tagging exists in the master (no affinity column matches) — add a Singles marker to the master to enable that chip")

# ---------- 8 · write everything ----------
json.dump(d, open(f"{SITE}/data/index.json","w"), ensure_ascii=False, separators=(",",":"))
open(f"{SITE}/data/index.js","w").write("window.DATA40="+json.dumps(d,ensure_ascii=False,separators=(",",":"))+";")
shape=json.loads(re.match(r"SHARD\(\d+,(.*)\);?\s*$",open(f"{SITE}/data/ch00.js").read(),re.S).group(1))
keys=list(shape["rows"][0].keys())
if "dc" not in keys: keys.append("dc")
bych=defaultdict(list)
for r in rows: bych[r[C["ch"]]].append(r)
for chn in range(23):
    out={"ch":chn,"rows":[{k:(r[d["cols"].index(k)] if k in d["cols"] else None) for k in keys} for r in bych.get(chn,[])]}
    open(f"{SITE}/data/ch{chn:02}.js","w").write(f"SHARD({chn},{json.dumps(out,ensure_ascii=False,separators=(',',':'))});")
open(f"{SITE}/data/tools.js","w").write("window.TOOLS40="+json.dumps(TOOLS,ensure_ascii=False)+";")
json.dump(MAN, open(f"{SITE}/data/OVERHAUL-MANIFEST.json","w"), indent=1)
aa=sum(1 for r in rows if r[C["g"]]=="AA")
print(f"rows {before:,} → {len(rows):,}  (deleted {before-len(rows):,}: {len(MAN['collapsed'])} dup/suffix collapses, {len(MAN['deleted'])-len(MAN['collapsed'])} named+tools)")
print(f"AA flagships now: {aa} · display categories: {len(DCATS)} · tools extracted: {len(TOOLS)}")
print("dc counts:", dict(list(MAN["dc"].items())[:8]))
