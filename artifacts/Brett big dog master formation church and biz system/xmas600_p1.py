#!/usr/bin/env python3
"""
600 Christmas/Advent/Epiphany campaigns across 12 NEW categories
(none repeat the 20 existing categories)
Each category has 50 campaigns split: ~25 coming INTO, ~25 coming OUT OF
Title · Subtitle · Hook · Duration · Scripture
"""

import html as hlib
def e(s): return hlib.escape(str(s))

STYLES = """
:root{
  --navy:#020408;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f7f3ea;--ink:#0d1018;--muted:#6a6a7a;
  --into:#2a4060;--out:#603020;--new:#2a5040;
  --rule:rgba(201,168,76,0.09);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#c4c0b8;color:var(--ink);}
.page{max-width:1280px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.25);}

/* COVER */
.cover{background:var(--navy);min-height:96vh;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden;}
.cover-bg{position:absolute;inset:0;background:
  radial-gradient(ellipse at 15% 80%,rgba(42,64,96,.15),transparent 50%),
  radial-gradient(ellipse at 85% 20%,rgba(96,48,32,.1),transparent 50%),
  radial-gradient(ellipse at 50% 50%,rgba(42,80,64,.06),transparent 70%),
  linear-gradient(180deg,#010204,#020308);}
.cover-top{padding:48px 80px 0;position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:rgba(255,255,255,.3);letter-spacing:2px;}
.cover-vol{font-size:7px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:var(--gold-dk);border:1px solid rgba(201,168,76,.18);padding:4px 12px;}
.cover-body{padding:60px 80px 72px;position:relative;z-index:2;}
.cover-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;color:rgba(201,168,76,.75);display:flex;align-items:center;gap:14px;margin-bottom:20px;}
.cover-kk::before{content:'';width:30px;height:1px;background:rgba(201,168,76,.5);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(42px,6vw,96px);font-weight:400;line-height:.86;color:#fff;letter-spacing:-3px;margin-bottom:22px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-rule{display:flex;align-items:center;gap:14px;margin:24px 0;}
.cover-rl{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rd{width:6px;height:6px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(15px,1.9vw,22px);font-weight:300;font-style:italic;color:rgba(210,195,165,.82);max-width:720px;line-height:1.58;margin-bottom:44px;}
.cover-stats{display:grid;grid-template-columns:repeat(6,1fr);max-width:900px;border:1px solid rgba(201,168,76,.16);}
.cs{padding:16px 18px;border-right:1px solid rgba(201,168,76,.1);text-align:center;}
.cs:last-child{border-right:none;}
.cs-n{font-family:'Playfair Display',serif;font-size:26px;color:var(--gold);display:block;line-height:1;}
.cs-l{font-size:6px;letter-spacing:2.5px;text-transform:uppercase;color:rgba(255,255,255,.18);font-weight:700;display:block;margin-top:4px;}

/* SECTION BANNERS */
.sec-banner{padding:42px 80px 22px;border-top:5px solid;}
.sec-banner.into{background:linear-gradient(135deg,#020508,#040810);border-color:var(--into);}
.sec-banner.out{background:linear-gradient(135deg,#060402,#0a0604);border-color:var(--out);}
.sec-banner.new{background:linear-gradient(135deg,#020605,#040a07);border-color:var(--new);}
.sb-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.sb-kk::before{content:'';width:16px;height:1px;background:currentColor;}
.into .sb-kk{color:#6a8aba;}
.out .sb-kk{color:#c09870;}
.new .sb-kk{color:#6aaa88;}
.sb-h2{font-family:'Playfair Display',serif;font-size:clamp(24px,3.5vw,56px);font-weight:400;line-height:.9;color:#fff;margin-bottom:10px;}
.sb-h2 em{font-style:italic;}
.sb-sub{font-family:'Georgia',serif;font-size:14px;line-height:1.72;max-width:820px;margin-bottom:8px;}
.into .sb-sub{color:rgba(170,195,220,.65);}
.out .sb-sub{color:rgba(220,185,155,.65);}
.new .sb-sub{color:rgba(160,210,185,.65);}
.sb-count{font-size:8px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border:1px solid;display:inline-block;padding:4px 13px;margin-top:6px;}
.into .sb-count{border-color:rgba(80,130,180,.3);color:#6a8aba;}
.out .sb-count{border-color:rgba(180,130,80,.3);color:#c09870;}
.new .sb-count{border-color:rgba(80,160,120,.3);color:#6aaa88;}

/* CATEGORY HEADER */
.cat-hdr{display:flex;align-items:flex-start;gap:22px;padding:28px 80px 14px;border-bottom:2px solid var(--rule);}
.cat-num-big{font-family:'Playfair Display',serif;font-size:52px;font-weight:400;color:rgba(201,168,76,.12);line-height:1;flex-shrink:0;margin-top:-8px;}
.cat-hdr-text{}
.cat-name{font-family:'Playfair Display',serif;font-size:clamp(20px,2.8vw,36px);font-weight:400;font-style:italic;}
.cat-name.into{color:var(--into);}
.cat-name.out{color:#905030;}
.cat-name.new{color:var(--new);}
.cat-desc{font-size:12px;color:#888;margin-top:4px;line-height:1.5;max-width:860px;}
.cat-badge{display:inline-block;font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:2px 8px;border:1px solid;margin-top:6px;}
.cat-badge.into{color:var(--into);border-color:rgba(42,64,96,.3);}
.cat-badge.out{color:#905030;border-color:rgba(144,80,48,.3);}
.cat-badge.new{color:var(--new);border-color:rgba(42,80,64,.3);}

/* CAMPAIGN GRID — 5 column for 50 per category */
.camp-wrap{padding:0 80px 20px;}
.camp-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;margin-top:10px;}
/* Hero — first card spans full width */
.camp-grid .c-hero{grid-column:1/-1;}
/* Large cards — positions 2,3 */
.camp-grid .c-lg{grid-column:span 2;}

/* BASE CARD */
.cc{padding:13px 15px;border:1px solid rgba(0,0,0,.065);background:rgba(255,255,255,.5);position:relative;}
.cc.c-hero{background:rgba(255,255,255,.85);border-width:2px;padding:18px 22px;}
.cc.c-lg{background:rgba(255,255,255,.65);}
.cc.into{border-top:3px solid var(--into);}
.cc.out{border-top:3px solid #905030;}
.cc.new{border-top:3px solid var(--new);}
.cc.c-hero.into{border-color:rgba(42,64,96,.4);}
.cc.c-hero.out{border-color:rgba(144,80,48,.4);}
.cc.c-hero.new{border-color:rgba(42,80,64,.4);}

/* CARD INTERNALS */
.cc-n{font-size:7.5px;letter-spacing:2px;color:#ccc;font-weight:700;display:block;margin-bottom:4px;}
.cc-arc{font-size:6.5px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:2px 6px;border:1px solid;display:inline-block;margin-bottom:6px;}
.cc.into .cc-arc{color:var(--into);border-color:rgba(42,64,96,.25);background:rgba(42,64,96,.04);}
.cc.out .cc-arc{color:#905030;border-color:rgba(144,80,48,.25);background:rgba(144,80,48,.04);}
.cc.new .cc-arc{color:var(--new);border-color:rgba(42,80,64,.25);background:rgba(42,80,64,.04);}
.cc-title{font-family:'Playfair Display',serif;font-style:italic;color:var(--ink);line-height:1.22;margin-bottom:4px;}
.cc-title{font-size:13.5px;}
.cc.c-hero .cc-title{font-size:19px;margin-bottom:7px;}
.cc.c-lg .cc-title{font-size:14.5px;}
.cc-sub{font-size:9.5px;color:#7a6a58;line-height:1.38;font-family:'Georgia',serif;font-style:italic;margin-bottom:5px;}
.cc.c-hero .cc-sub{font-size:12px;margin-bottom:8px;}
.cc.c-lg .cc-sub{font-size:10.5px;}
.cc-hook{font-size:8.5px;color:#4a4a5a;line-height:1.42;padding:5px 9px;border-left:2px solid;background:rgba(0,0,0,.025);}
.cc.into .cc-hook{border-color:rgba(42,64,96,.25);}
.cc.out .cc-hook{border-color:rgba(144,80,48,.25);}
.cc.new .cc-hook{border-color:rgba(42,80,64,.25);}
.cc.c-hero .cc-hook{font-size:11px;padding:9px 13px;margin-bottom:8px;}
.cc-meta{display:flex;gap:8px;align-items:center;margin-top:5px;flex-wrap:wrap;}
.cc-dur{font-size:7.5px;letter-spacing:1px;text-transform:uppercase;font-weight:700;color:var(--gold-dk);}
.cc-ref{font-size:7.5px;color:#bbb;font-style:italic;}

/* DIVIDERS */
.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.22),transparent);}
.sdiv{height:1px;background:var(--rule);margin:0 80px;}
.cat-sdiv{height:1px;background:var(--rule);}
.bridge{padding:28px 80px;background:linear-gradient(90deg,#030508,#060a0e,#030508);text-align:center;}
.bridge-inner{max-width:680px;margin:0 auto;}
.bridge p{font-family:'Playfair Display',serif;font-size:clamp(14px,2vw,20px);font-style:italic;color:rgba(201,168,76,.6);line-height:1.55;}
.bridge-rule{display:flex;align-items:center;gap:14px;max-width:680px;margin:12px auto 0;}
.bridge-rl{flex:1;height:1px;background:rgba(201,168,76,.15);}
.bridge-sym{font-size:18px;color:rgba(201,168,76,.3);}

/* BACK */
.back{background:#010305;padding:52px 80px;text-align:center;}
.back-q{font-family:'Playfair Display',serif;font-size:clamp(14px,2vw,20px);font-style:italic;color:var(--cream);max-width:760px;margin:0 auto 16px;line-height:1.55;}
.back-a{font-size:8.5px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.back-c{margin-top:12px;font-size:12px;color:#4a5a6a;}
.back-c a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:30px;color:#fff;font-style:italic;margin-top:22px;}

@media(max-width:1000px){
  .cover-top,.cover-body,.sec-banner,.cat-hdr,.camp-wrap,.bridge,.back{padding-left:28px;padding-right:28px;}
  .camp-grid{grid-template-columns:1fr 1fr;}
  .camp-grid .c-hero,.camp-grid .c-lg{grid-column:auto;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
}
"""

def cc(n, arc, title, sub, hook, dur, ref, cls="", hero=False, lg=False):
    sz = "c-hero" if hero else ("c-lg" if lg else "")
    classes = f"cc {cls} {sz}".strip()
    return f"""<div class="{classes}">
  <span class="cc-n">{n:03d}</span>
  <span class="cc-arc">{e(arc)}</span>
  <h3 class="cc-title">{e(title)}</h3>
  <p class="cc-sub">{e(sub)}</p>
  <p class="cc-hook">{e(hook)}</p>
  <div class="cc-meta"><span class="cc-dur">{e(dur)}</span><span class="cc-ref">{e(ref)}</span></div>
</div>"""

def build_cat(cat_n, name, desc, badge, side, entries, global_start):
    cards = ""
    for i, entry in enumerate(entries):
        arc, title, sub, hook, dur, ref = entry
        is_hero = (i == 0)
        is_lg = (i in (1, 2))
        n = global_start + i
        cards += cc(n, arc, title, sub, hook, dur, ref, side, is_hero, is_lg)
    return f"""<div class="cat-hdr">
  <div class="cat-num-big">{cat_n:02d}</div>
  <div class="cat-hdr-text">
    <h2 class="cat-name {side}">{e(name)}</h2>
    <p class="cat-desc">{e(desc)}</p>
    <span class="cat-badge {side}">{e(badge)}</span>
  </div>
</div>
<div class="camp-wrap"><div class="camp-grid">{cards}</div></div>"""

def sec_banner(cls, kk, h2, sub, count):
    return f"""<div class="hdiv"></div><div class="sec-banner {cls}">
  <p class="sb-kk">{e(kk)}</p>
  <h2 class="sb-h2">{h2}</h2>
  <p class="sb-sub">{e(sub)}</p>
  <span class="sb-count">{e(count)}</span>
</div>"""
