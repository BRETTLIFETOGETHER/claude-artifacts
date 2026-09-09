import re

PAGES = ["page_home.py","page_assessment.py","page_create.py","page_reader.py",
         "page_browse_campaign.py","page_rest.py"]

# ---------- 0. strip all v2 override blocks (they run to </style>) ----------
def strip_v2(s):
    return re.sub(r'/\* ===== v2[^*]*===== \*/.*?(?=</style>)', '', s, flags=re.S)

# ---------- 1. gradient flattening (before single-hex maps) ----------
def flatten_gradients(s):
    s = re.sub(r'linear-gradient\([^)]*#F6A928[^)]*\)', '#E85321', s)   # amber grads → vermilion block
    s = re.sub(r'linear-gradient\([^)]*#0E3A57[^)]*\)', '#2E4C97', s)   # navy grads → royal blue block
    s = re.sub(r'linear-gradient\([^)]*#092B42[^)]*\)', '#243A72', s)
    s = re.sub(r'linear-gradient\([^)]*#FDEFDC[^)]*\)', '#F4F4EF', s)   # cream grads → flat sand
    s = re.sub(r'linear-gradient\([^)]*#F1F6FA[^)]*\)', '#F4F4EF', s)
    return s

# ---------- 2. v2 → v3 hex remap ----------
HEXMAP = {
  "#0E3A57":"#2E4C97", "#155377":"#2E4C97", "#175A85":"#3B5CAD", "#092B42":"#243A72",
  "#12466A":"#2E4C97", "#0F3E5F":"#2E4C97", "#0B3049":"#243A72", "#1A6392":"#3B5CAD",
  "#E8F0F7":"#E8EDF6", "#F4F8FB":"#F6F8FB", "#D4E2ED":"#D6DEEE", "#F1F6FA":"#F4F6F1",
  "#F7FAFC":"#FAFAF6", "#C6D9E8":"#E4EFD8", "#B8CBDA":"#C4CFE8", "#A9C2D6":"#B9C6DE",
  "#7FA0B8":"#9AA9CC", "#8FA9BE":"#9AA9CC", "#7FC0E8":"#E3DF3C", "#6FB6E4":"#E3DF3C",
  "#9CC8E8":"#E9E76A", "#8FB3CC":"#9AA9CC", "#5C86A5":"#5F7BB0", "#3E5468":"#454545",
  "#F6A928":"#E3DF3C", "#EA7A0C":"#D64614", "#E8780C":"#D64614", "#EE8010":"#E85321",
  "#CD6A05":"#C23F10", "#D18410":"#5F8540", "#D6820A":"#C23F10", "#E29A3B":"#7CA457",
  "#FFC97A":"#E3DF3C", "#FFE3B8":"#F2F0B8", "#FFF3E2":"#FBFAE3", "#FFF0DA":"#FBFAE3",
  "#FDEFDC":"#F1F1E2", "#FFF7EA":"#F8F8EC", "#F8DFB8":"#E6ECDA", "#FBE3BE":"#EAF0E2",
  "#7A5310":"#4A5E30", "#4A2E00":"#1C1C1C",
  "rgba(238,128,16":"rgba(232,83,33", "rgba(246,169,40":"rgba(227,223,60",
  "rgba(14,58,87":"rgba(22,22,22", "rgba(21,83,119":"rgba(46,76,151",
}
def remap(s):
    for k,v in HEXMAP.items(): s = s.replace(k,v)
    return s

# ---------- 3. per-page v3 overrides + structural patches ----------

HOME_HERO = '''<!-- ================= HERO ================= -->
<section class="hero">
  <div class="wrap hero-head">
    <span class="eyebrow bare rv">The Lifetogether Formation Platform</span>
    <h1 class="rv">Where do you<br>want to <em>grow</em>?</h1>
    <p class="lede rv">Twenty-five years of churchwide campaigns, now an intelligent platform. Take a ten-minute assessment and receive a path built for where you are — or bring your own teaching and watch it become curriculum your whole church can walk together.</p>
    <div class="hero-ctas rv">
      <a class="btn btn-primary btn-lg" href="assessment.html">Take the 10-Minute Assessment</a>
      <a class="btn btn-outline btn-lg" href="create.html">Bring Your Teaching to Life</a>
    </div>
    <p class="hero-quiet rv">Already know what you need? <a href="browse.html">Browse the campaign library →</a></p>
  </div>
  <div class="wrap"><div class="mosaic hero-mz rv" id="heroMosaic" aria-hidden="true"></div></div>
  <div class="wrap">
    <div class="stats rv">
      <div class="st"><b>25+</b><span>Years of Campaigns</span></div>
      <div class="st"><b>500+</b><span>Church Partnerships</span></div>
      <div class="st"><b>1,000+</b><span>Campaign Titles</span></div>
      <div class="st"><b>4</b><span>Formats — 7·21·30·40</span></div>
    </div>
  </div>
</section>

'''

OVR_HOME = """
/* ===== v3 catalog overrides ===== */
.hero{background:#fff;padding:72px 0 64px}
.hero-head{max-width:840px;margin:0 auto;text-align:center;display:flex;flex-direction:column;align-items:center}
.hero-head h1{margin:20px 0 22px}
.hero-head .lede{margin:0 auto 32px}
.hero-ctas{display:flex;gap:14px;flex-wrap:wrap;justify-content:center}
.hero-quiet{margin-top:20px;font-size:14.5px;color:var(--mute)}
.hero-quiet a{color:var(--lt-orange);font-weight:700;border-bottom:2px solid rgba(232,83,33,.3)}
.hero-mz{grid-template-columns:repeat(6,1fr);grid-auto-rows:104px;margin-top:48px}
.hero-mz .big{grid-column:span 2;grid-row:span 2}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:50px;border-top:2px dotted #C9C9BE;padding-top:32px;text-align:center}
.stats b{font-family:var(--display);font-size:42px;font-weight:600;color:var(--ink);display:block;line-height:1}
.stats span{font-family:var(--display);font-size:11.5px;font-weight:500;letter-spacing:.2em;text-transform:uppercase;color:var(--mute)}
.stats .st{display:flex;flex-direction:column;gap:8px}
.partners{background:#F4F4EF;border:0;padding:44px 0 48px}
.logo-row span{font-family:var(--display);text-transform:uppercase;letter-spacing:.1em;font-size:16px;color:#8F8F87}
.door{border-radius:3px;padding:34px 30px;min-height:360px;box-shadow:none;border:1px solid var(--line)}
.door .dart{display:none}
.door .dtag{display:inline-block;align-self:flex-start;font-family:var(--ui);font-weight:700;font-size:14px;letter-spacing:.02em;padding:8px 15px;margin-bottom:6px}
.door-find{background:#fff}
.door-find .dtag{background:var(--lt-green);color:#fff}
.door-find h3{color:var(--ink)}.door-find p{color:var(--body)}.door-find .dlink{color:var(--lt-orange)}
.door-path{background:var(--lt-blue);border:0}
.door-path .dtag{background:var(--lt-lime);color:#1C1C1C}
.door-path h3{color:#fff}.door-path p{color:#C4CFE8}.door-path .dlink{color:var(--lt-lime)}
.door-create{background:var(--lt-orange);border:0}
.door-create .dtag{background:#1C1C1C;color:#fff}
.door-create h3{color:#fff}.door-create p{color:#FBD9CB}.door-create .dlink{color:#fff}
.scale button.sel{background:var(--lt-blue);border-color:var(--lt-blue);color:#fff;box-shadow:none}
.sampler{border-radius:3px;box-shadow:var(--shadow-lg)}
.sampler .sdone{background:#EAF0E2;color:#44622C;border-radius:3px}
.sampler .sdone a{color:#5F8540!important}
.stp .num{border-radius:2px;background:#EAF0E2;color:#5F8540}
.mock{border-radius:3px}
.mock-head{background:#F4F4EF}
.mline i{background:var(--lt-green);border-radius:1px}
.yw{background:#EAF0E2;color:#5F8540;border-radius:2px}
.shelf-head .eyebrow{color:var(--lt-green-deep)}
.fmt-card{border-radius:3px;background:rgba(255,255,255,.14);border:0}
.fmt-card .fname{color:var(--lt-lime)}
.fmt-card p{color:#E4EFD8}
.her .dots40{color:var(--lt-lime)}
.hn{border-radius:3px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14)}
.tsti-feature{border-radius:3px;padding:46px 52px}
.tsti-feature .avatar{background:var(--lt-blue);border-radius:50%}
.tsti-feature blockquote{font-family:var(--wordmark);font-style:italic;font-weight:500;text-transform:none;letter-spacing:0;font-size:clamp(19px,2vw,24px)}
.tcard{border-radius:3px}
.tcard .avatar{border-radius:50%}
.spanel{border-radius:3px;padding:52px 42px 44px}
.sp-you{background:var(--lt-blue);border:0}
.sp-you h3{color:#fff}.sp-you p{color:#C4CFE8}
.sp-church{background:var(--lt-orange);border:0}
.sp-church h3{color:#fff}.sp-church p{color:#FBD9CB}
.sp-church .btn{background:#1C1C1C;color:#fff}
"""

HOME_SCRIPT_ADD = '''
  // catalog hero mosaic — photos + brand color tiles
  const mzEl=document.getElementById('heroMosaic');
  if(mzEl){mzEl.innerHTML=mosaicHTML([
    ['img','p01'],['img','p03'],['big','p04'],['tile','var(--lt-green)'],['img','p05'],
    ['img','p08'],['tile','var(--lt-lime)'],['img','p15'],['img','p02'],
    ['img','p14'],['img','p13'],['tile','var(--lt-gray)'],['img','p22']
  ]);}
'''

OVR_ASSESS = """
/* ===== v3 catalog overrides ===== */
.prog i{border-radius:2px;width:26px;height:10px;border:0;background:#E3E3DA}
.prog i.done{background:var(--lt-green)}
.prog i.cur{background:var(--lt-lime)}
.q{border-radius:3px}
.scale button{border-radius:2px}
.scale button.sel{background:var(--lt-blue);border-color:var(--lt-blue);color:#fff;box-shadow:none}
.ig{border-radius:3px}
.ig i{border-radius:2px}
.proc .parch{width:104px;height:104px}
.proc .parch::before,.proc .parch::after{border-radius:3px;border-color:#E3E3DA}
.proc .parch::after{border-color:var(--lt-green)}
.pf-sum{border-radius:3px}
.track{border-radius:0;height:12px}
.fill{border-radius:0}
.area{border-radius:3px}
.area .sg{border-radius:0}
.path-cta{border-radius:3px;background:#F4F4EF;border:1px solid var(--line)}
.match .why{color:var(--lt-green-deep)}
"""

OVR_CREATE = """
/* ===== v3 catalog overrides ===== */
.pull{border-radius:3px}
.pull .sun{border-radius:2px;background:var(--lt-lime);color:#1C1C1C}
.pull blockquote{font-family:var(--wordmark);font-style:italic;text-transform:none;letter-spacing:0}
.up{border-radius:3px;border-color:#C9C9BE}
.proc .ring{border-radius:50%;border-color:#EAF0E2;border-top-color:var(--lt-green)}
.an-card{border-radius:3px}
.an-card .vchip{background:var(--lt-blue);color:#fff;border-radius:0}
.an-note{border-radius:3px;background:#F4F4EF;color:#4A4A45}
.out{border-radius:3px}
.out .otag{border-radius:0}
.stab{border-radius:3px}
.stab.sel{border-color:var(--lt-green);background:#F7FAF2;box-shadow:none}
.stab .sn{color:var(--lt-green-deep)}
.doc{border-radius:3px}
.doc-head{background:#F4F4EF}
.regen{border-radius:2px;background:#EAF0E2;color:#5F8540}
.regen:hover{background:#DCE8CE}
.yw{background:#EAF0E2;color:#5F8540;border-radius:2px}
.crumbs b{color:var(--lt-orange)}
.exp{border-radius:3px}
.exp .ei{border-radius:2px}
"""

OVR_READER = """
/* ===== v3 catalog overrides ===== */
.dayarch{border-radius:2px}
.dayarch.cur{border-color:var(--lt-green);background:#EAF0E2;color:#5F8540}
.dayarch.done{background:var(--lt-green);border-color:var(--lt-green)}
.rd-camp .mini{border-radius:2px}
.verse{border-radius:3px;border-left:5px solid var(--lt-green)}
.verse p{font-family:var(--wordmark);font-style:italic;text-transform:none;letter-spacing:0}
.verse cite{color:var(--lt-green-deep)}
.rq{border-radius:3px;background:#F4F4EF}
.done-msg{border-radius:3px}
.sun-note{border-radius:3px;background:#FBFAE3;color:#5A5A20}
"""

OVR_BROWSE = """
/* ===== v3 catalog overrides ===== */
.search input{border-radius:3px;box-shadow:none;border-width:2px}
.chtile{border-radius:3px}
.chtile .swash{height:5px}
.chtile .cnew{background:var(--lt-lime);color:#1C1C1C;border-radius:0}
"""

OVR_CAMPAIGN = """
/* ===== v3 catalog overrides ===== */
.cd-cover{border-radius:3px;border:5px solid #fff;box-shadow:var(--shadow-lg)}
.cd-cover .cover{aspect-ratio:4/4.4}
.ph .pnum{border-radius:2px;color:#fff}
.ed-card{border-radius:3px;border-top-width:6px}
.frame{border-radius:3px}
"""

OVR_HOW = """
/* ===== v3 catalog overrides ===== */
.an-card{border-radius:3px}
.an-card .ai{border-radius:2px}
.ft{border-radius:3px}
.ft .fname{color:var(--lt-green-deep)}
.ph .pnum{border-radius:2px;background:var(--lt-lime);color:#1C1C1C}
.lw .wk{border-radius:2px;background:#EAF0E2;color:#5F8540}
.fq{border-radius:3px}
.fq summary::after{color:var(--lt-orange)}
"""

OVR_PRICING = """
/* ===== v3 catalog overrides ===== */
.tiers{align-items:stretch}
.tier{background:#fff;border:1.5px solid var(--line);border-radius:3px;color:var(--body);padding:0 32px 36px;overflow:hidden}
.tier::before{content:'';display:block;height:9px;background:var(--lt-gray);margin:0 -32px 28px}
.tier:nth-child(1)::before{background:var(--lt-green)}
.tier.hot::before{background:var(--lt-orange)}
.tier:nth-child(3)::before{background:var(--lt-blue)}
.tier .tname{color:var(--ink)}.tier .tfor{color:var(--mute)}
.tier .price{color:var(--ink)}.tier .per{color:var(--mute)}
.tier li{color:var(--body)}.tier li::before{color:var(--lt-green)}
.tier li.plus::before{color:var(--lt-orange)}
.tier .btn-outline{border-color:#1C1C1C;color:#1C1C1C}
.tier .btn-outline:hover{background:#1C1C1C;color:#fff}
.tier.hot{background:#fff;border:2px solid var(--lt-orange);box-shadow:var(--shadow-lg)}
.tier.hot .tname,.tier.hot .price{color:var(--ink)}
.tier.hot .tfor,.tier.hot .per{color:var(--mute)}
.tier.hot li{color:var(--body)}.tier.hot li::before{color:var(--lt-orange)}
.tier.hot .btn{background:var(--lt-orange);color:#fff}
.tier.hot .btn:hover{background:var(--lt-orange-deep)}
.tier .pop{background:var(--lt-orange);color:#fff;border-radius:0}
.alt-card{border-radius:3px}
.guarantee{border-radius:3px;background:#F4F4EF;border:1px solid var(--line)}
.guarantee .gi{border-radius:2px;background:var(--lt-green)}
"""

OVR_ABOUT = """
/* ===== v3 catalog overrides ===== */
.tl::before{background:#DEDED6}
.tl-item::before{border-radius:1px;background:var(--lt-green)}
.tl-item.gold::before{background:var(--lt-orange)}
.tsti-feature{border-radius:3px}
.tsti-feature .avatar{background:var(--lt-blue);border-radius:50%}
.tsti-feature blockquote{font-family:var(--wordmark);font-style:italic;text-transform:none;letter-spacing:0;font-weight:500}
.tcard{border-radius:3px}
.tcard .avatar{border-radius:50%}
.three .tc{border-radius:3px}
.contact{border-radius:3px}
.contact .cline i{border-radius:2px;background:#EAF0E2;color:#5F8540}
.logo-row span{font-family:var(--display);text-transform:uppercase;letter-spacing:.1em;font-size:16px;color:#8F8F87}
"""

def append_ovr(s, head_var, block):
    hm = re.search(head_var + r' = """(.*?)</style>', s, re.S)
    if not hm:
        # single-head pages use HEAD = """..."""
        hm = re.search(head_var + r'="""(.*?)</style>', s, re.S)
    seg = hm.group(0)
    return s.replace(seg, seg.replace('</style>', block + '\n</style>'), 1)

for f in PAGES:
    s = open(f).read()
    s = strip_v2(s)
    s = flatten_gradients(s)
    s = remap(s)
    if f == "page_home.py":
        # swap hero block for the catalog mosaic hero
        a = s.find('<!-- ================= HERO ================= -->')
        b = s.find('<!-- ================= PARTNERS ================= -->')
        s = s[:a] + HOME_HERO + s[b:]
        s = append_ovr(s, "HEAD", OVR_HOME)
        # inject mosaic fill into the DOMContentLoaded script
        s = s.replace("  // featured shelf", HOME_SCRIPT_ADD + "  // featured shelf")
        # remove old fan JS (data-cover fill) — no fan markup remains, guard is querySelectorAll so harmless; keep
    if f == "page_assessment.py":
        s = append_ovr(s, "HEAD", OVR_ASSESS)
        s = re.sub(r"const BANDS=\[.*?\];",
          "const BANDS=[{max:2.5,l:'Emerging',c:'#C6552E'},{max:3.5,l:'Growing',c:'#C98F2E'},{max:4.3,l:'Steady',c:'#4E86B8'},{max:9,l:'Strong',c:'#5F8540'}];", s)
    if f == "page_create.py":
        s = append_ovr(s, "HEAD", OVR_CREATE)
    if f == "page_reader.py":
        s = append_ovr(s, "HEAD", OVR_READER)
    if f == "page_browse_campaign.py":
        s = append_ovr(s, "B_HEAD", OVR_BROWSE)
        s = append_ovr(s, "C_HEAD", OVR_CAMPAIGN)
    if f == "page_rest.py":
        s = append_ovr(s, "H_HEAD", OVR_HOW)
        s = append_ovr(s, "P_HEAD", OVR_PRICING)
        s = append_ovr(s, "A_HEAD", OVR_ABOUT)
    open(f,'w').write(s)
    print("v3 restyled", f)
print("done")
