import re

PAGES = ["page_home.py","page_assessment.py","page_create.py","page_reader.py",
         "page_browse_campaign.py","page_rest.py"]

# ---------- generic hex remap (old palette → navy/orange) ----------
HEXMAP = {
  # violets → navy family
  "#6A63CF":"#155377", "#5A53B8":"#155377", "#4A44A8":"#0E3A57", "#403A9E":"#0E3A57",
  "#EAE8F8":"#E8F0F7", "#F8F7FD":"#F4F8FB", "#DBD8F0":"#D4E2ED", "#7A75C4":"#5C86A5",
  "#4A4B6E":"#3E5468", "#F1EFFB":"#E8F0F7", "#EFEDFA":"#E8F0F7", "#B7A9E0":"#8FB3CC",
  "#DDD9F1":"#D4E2ED", "#FBFAFE":"#F7FAFC",
  # greens → navy family (structural art) / light tints
  "#237A52":"#155377", "#2E8A5F":"#1A6392", "#1B5C3F":"#0E3A57",
  "#EDF4EA":"#F1F6FA", "#F8F3E3":"#FDEFDC", "#DDE7D6":"#D4E2ED", "#D7E6D4":"#D4E2ED",
  "#D6E5D3":"#D4E2ED", "#E7F1E6":"#E8F0F7", "#F7FBF4":"#F7FAFC", "#FAFCF6":"#F7FAFC",
  "#5F8F6C":"#5C86A5", "#3E5A48":"#3E5468", "#BFE3C6":"#9CC8E8", "#DCEBDD":"#C6D9E8",
  # golds → orange family
  "#C4933C":"#F6A928", "#9C7228":"#D18410", "#E3C88A":"#FFC97A", "#C9A45A":"#F6A928",
  "#E8D9AE":"#FFC97A", "#B5852F":"#D6820A", "#B08A45":"#E29A3B", "#EBDDBE":"#F8DFB8",
  "#F5EBD4":"#FDEFDC", "#FBF5E6":"#FFF7EA", "#EFDDB2":"#FBE3BE", "#F7ECD8":"#FDEFDC",
  "#FCF8EE":"#FFF7EA", "#5E4E2E":"#7A5310", "#5E4A22":"#7A5310",
  # terracotta / misc
  "#B45A38":"#CD6A05", "#FBEAE4":"#FDEFDC", "#B5502F":"#CD6A05",
  # old ink green-black → navy
  "#14352A":"#0E3A57", "#2B2008":"#4A2E00",
  # old greens in rgba shadows
  "rgba(35,122,82":"rgba(238,128,16", "rgba(106,99,207":"rgba(21,83,119",
  "rgba(90,83,184":"rgba(238,128,16", "rgba(196,147,60":"rgba(238,128,16",
  "rgba(156,114,40":"rgba(216,132,16",
}

def generic(s):
  # arch radii → rounded
  s = re.sub(r'border-radius:\d+px \d+px \d+px \d+px', 'border-radius:14px', s)
  s = re.sub(r'border-radius:50% 50% \d+px \d+px', 'border-radius:50%', s)
  # italic display voice → normal (Archivo has no italic)
  s = s.replace("font-style:italic", "font-style:normal")
  # Fraunces variation settings are meaningless for Archivo
  s = re.sub(r"font-variation-settings:'SOFT' 40,'WONK' 0,'opsz' \d+;", "", s)
  for k, v in HEXMAP.items():
    s = s.replace(k, v)
  return s

# ---------- targeted patches (run BEFORE generic where colors must diverge) ----------
def patch_home(s):
  # door-path art strokes/fills → light blue on navy card
  s = s.replace('stroke="#6A63CF"', 'stroke="#6FB6E4"').replace('fill="#6A63CF"', 'fill="#6FB6E4"')
  # door-create art → white on orange card
  s = s.replace('stroke="#C4933C"', 'stroke="#FFFFFF"').replace('fill="#C4933C"', 'fill="#FFFFFF"')
  # split panel buttons: strip inline violet style; navy button on orange panel
  s = s.replace('class="btn btn-primary btn-lg" style="background:#5A53B8;box-shadow:0 8px 22px rgba(90,83,184,.3)"',
                'class="btn btn-primary btn-lg"')
  s = s.replace('<a class="btn btn-primary btn-lg" href="create.html">Transform a sermon</a>',
                '<a class="btn btn-ink btn-lg" style="background:#0E3A57" href="create.html">Transform a sermon</a>')
  # v2 overrides appended to the page style block
  s = s.replace("</style>\n\"\"\"", OVR_HOME + "</style>\n\"\"\"", 1)
  return s

OVR_HOME = """
/* ===== v2 navy/orange overrides ===== */
.hero{background:linear-gradient(150deg,#092B42 0%,#0E3A57 52%,#175A85 100%);padding:92px 0 86px;color:#B8CBDA;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;right:-220px;top:-220px;width:640px;height:640px;border-radius:50%;
  border:2px solid rgba(255,255,255,.06);box-shadow:0 0 0 80px rgba(255,255,255,.03),0 0 0 170px rgba(255,255,255,.02)}
.hero h1{color:#fff}
.hero .lede{color:#C6D9E8}
.hero .eyebrow{color:#F6A928}
.hero-quiet{color:#8FA9BE}.hero-quiet a{color:#F6A928;border-color:rgba(246,169,40,.45)}
.hero .btn-outline{border-color:rgba(255,255,255,.42);color:#fff}
.hero .btn-outline:hover{border-color:#fff;background:rgba(255,255,255,.07);color:#fff}
.stats{border-top:1px solid rgba(255,255,255,.16)}
.stats b{color:#fff}.stats span{color:#7FA0B8}
.fan .halo{background:radial-gradient(closest-side,rgba(246,169,40,.22),transparent 70%)}
.fan .fc{box-shadow:0 32px 70px rgba(0,0,0,.4);border-radius:16px;border-width:4px}
.partners{background:#fff;border:0;padding:48px 0 52px}
.door{border-radius:18px;min-height:400px}
.door-find{background:#fff;border:1px solid var(--line-soft)}
.door-find h3{color:var(--ink)}.door-find .dlink{color:var(--green-deep)}.door-find .dtag{color:var(--mute)}.door-find p{color:var(--body)}
.door-path{background:linear-gradient(160deg,#0E3A57,#155377);border:0}
.door-path h3{color:#fff}.door-path .dtag{color:#7FC0E8}.door-path p{color:#B8CBDA}.door-path .dlink{color:#F6A928}
.door-create{background:linear-gradient(135deg,#F6A928,#E8780C);border:0}
.door-create h3,.door-create .dlink{color:#fff}.door-create .dtag{color:#FFE3B8}.door-create p{color:#FFF3E2}
.scale button.sel{background:var(--grad);border-color:transparent;color:#fff;box-shadow:var(--shadow-o)}
.sampler .sdone{background:#FDEFDC;color:#7A5310}
.sampler .sdone a{color:#CD6A05!important}
.spanel{border-radius:18px;padding:56px 42px 46px}
.sp-you{background:linear-gradient(160deg,#0E3A57,#155377);border:0}
.sp-you h3{color:#fff}.sp-you p{color:#B8CBDA}
.sp-church{background:linear-gradient(135deg,#F6A928,#E8780C);border:0}
.sp-church h3{color:#fff}.sp-church p{color:#FFF3E2}
.mock-head{background:linear-gradient(120deg,#FDEFDC,#FFF7EA)}
.tsti-feature .avatar{background:linear-gradient(140deg,#0E3A57,#1A6392);border-radius:50%}
.her .dots40{color:#F6A928}
.fmt-card .fname{color:#FFC97A}
.stp .num{border-radius:12px}
.door .dart{opacity:.85}
"""

def patch_assessment(s):
  s = s.replace("</style>\n\"\"\"", OVR_ASSESS + "</style>\n\"\"\"", 1)
  return s

OVR_ASSESS = """
/* ===== v2 overrides ===== */
.prog i{border-radius:8px;width:26px;height:12px}
.prog i.done{background:var(--grad);border-color:transparent}
.prog i.cur{background:var(--green-tint);border-color:var(--green)}
.ig i{border-radius:10px}
.proc .parch{width:110px;height:110px}
.proc .parch::before,.proc .parch::after{border-radius:22px}
.area{border-radius:16px}
.path-cta{border-radius:18px}
"""

def patch_create(s):
  s = s.replace("</style>\n\"\"\"", OVR_CREATE + "</style>\n\"\"\"", 1)
  return s

OVR_CREATE = """
/* ===== v2 overrides ===== */
.pull{border-radius:20px}
.pull .sun{border-radius:14px}
.proc .ring{border-radius:50%;border-width:4px}
.stab{border-radius:12px}
.exp .ei{border-radius:14px}
.doc{border-radius:18px}
"""

def patch_reader(s):
  s = s.replace("</style>\n\"\"\"", OVR_READER + "</style>\n\"\"\"", 1)
  return s

OVR_READER = """
/* ===== v2 overrides ===== */
.dayarch{border-radius:10px}
.dayarch.done{background:var(--grad);border-color:transparent}
.rd-camp .mini{border-radius:9px}
.verse{border-left-width:4px}
.rq{border-radius:16px}
"""

def patch_browse_campaign(s):
  s = s.replace("</style>\n\"\"\"", OVR_BROWSE + "</style>\n\"\"\"", 1)          # browse head
  s = s.replace("</style>\n\"\"\"", OVR_CAMPAIGN + "</style>\n\"\"\"", 1)        # campaign head (second occurrence)
  return s

OVR_BROWSE = """
/* ===== v2 overrides ===== */
.chtile{border-radius:14px}
.chtile .swash{height:4px}
.search input{border-radius:999px}
"""

OVR_CAMPAIGN = """
/* ===== v2 overrides ===== */
.cd-cover{border-radius:20px;border-width:5px}
.ph .pnum{border-radius:12px;color:#fff}
.ed-card{border-radius:16px}
.frame{border-radius:18px}
"""

def patch_rest(s):
  # pricing tier rework: navy cards, orange featured
  s = s.replace("</style>\n\"\"\"", OVR_HOW + "</style>\n\"\"\"", 1)     # how-it-works head
  s = s.replace("</style>\n\"\"\"", OVR_PRICING + "</style>\n\"\"\"", 1) # pricing head
  s = s.replace("</style>\n\"\"\"", OVR_ABOUT + "</style>\n\"\"\"", 1)   # about head
  return s

OVR_HOW = """
/* ===== v2 overrides ===== */
.an-card .ai{border-radius:12px}
.ph .pnum{border-radius:12px;background:var(--grad);color:#fff}
.lw .wk{border-radius:12px}
.ft{border-radius:16px}
.fq{border-radius:14px}
"""

OVR_PRICING = """
/* ===== v2 overrides ===== */
.tier{background:linear-gradient(165deg,#0F3E5F,#0B3049);border:0;color:#B8CBDA;border-radius:18px}
.tier .tname{color:#fff}.tier .tfor{color:#7FA0B8}
.tier .price{color:#fff}.tier .per{color:#7FA0B8}
.tier li{color:#C6D9E8}.tier li::before{color:#F6A928}
.tier li.plus::before{color:#FFC97A}
.tier .btn-outline{border-color:rgba(255,255,255,.42);color:#fff}
.tier .btn-outline:hover{border-color:#fff;color:#fff;background:rgba(255,255,255,.07)}
.tier.hot{background:linear-gradient(150deg,#F6A928,#E8780C);box-shadow:0 26px 60px rgba(238,128,16,.35);border:0}
.tier.hot .tname,.tier.hot .price{color:#fff}
.tier.hot .tfor,.tier.hot .per{color:#FFE3B8}
.tier.hot li{color:#FFF3E2}.tier.hot li::before{color:#fff}
.tier.hot .btn{background:#0E3A57;color:#fff;box-shadow:none}
.tier.hot .btn:hover{background:#092B42}
.tier .pop{background:#0E3A57;color:#FFC97A}
.alt-card{border-radius:18px}
.guarantee{border-radius:18px}
.guarantee .gi{border-radius:14px;background:var(--grad)}
"""

OVR_ABOUT = """
/* ===== v2 overrides ===== */
.tl-item::before{border-radius:5px}
.tsti-feature .avatar{background:linear-gradient(140deg,#0E3A57,#1A6392);border-radius:50%}
.tcard .avatar{border-radius:50%}
.contact{border-radius:20px}
.contact .cline i{border-radius:12px}
.tc{border-radius:16px}
"""

for f in PAGES:
  s = open(f).read()
  if f == "page_home.py": s = patch_home(s)
  if f == "page_assessment.py": s = patch_assessment(s)
  if f == "page_create.py": s = patch_create(s)
  if f == "page_reader.py": s = patch_reader(s)
  if f == "page_browse_campaign.py": s = patch_browse_campaign(s)
  if f == "page_rest.py": s = patch_rest(s)
  s = generic(s)
  open(f, "w").write(s)
  print("restyled", f)
print("done")
