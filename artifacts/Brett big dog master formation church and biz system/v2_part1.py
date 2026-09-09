import html as hlib
def e(s): return hlib.escape(str(s))

STYLES = """
:root{--navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;--cream:#f8f5ef;--ink:#0e1218;--c1:#4a5a8a;--c2:#4a7a50;--c3:#8a4a30;--rule:rgba(201,168,76,0.10);}
*{margin:0;padding:0;box-sizing:border-box;}html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#cac6be;color:var(--ink);}
.page{max-width:1200px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.22);}
.cover{background:var(--navy);min-height:92vh;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:radial-gradient(ellipse at 20% 70%,rgba(74,90,138,.08),transparent 50%),linear-gradient(180deg,#010306,#020510);}
.cover-top{padding:48px 80px 0;position:relative;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;color:rgba(255,255,255,.35);letter-spacing:2px;}
.cover-tag{font-size:7px;letter-spacing:4px;text-transform:uppercase;font-weight:700;color:var(--gold-dk);border:1px solid rgba(201,168,76,.18);padding:4px 11px;}
.cover-body{padding:56px 80px 72px;position:relative;z-index:2;}
.cover-ey{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;color:rgba(201,168,76,.8);display:flex;align-items:center;gap:12px;margin-bottom:18px;}
.cover-ey::before{content:'';width:28px;height:1px;background:rgba(201,168,76,.5);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(36px,5.5vw,80px);font-weight:400;line-height:.9;color:#fff;letter-spacing:-2px;margin-bottom:18px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-rule{display:flex;align-items:center;gap:12px;margin:22px 0;}
.cover-rule-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rule-dot{width:5px;height:5px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(14px,1.8vw,20px);font-weight:300;font-style:italic;color:rgba(212,196,168,.85);max-width:700px;line-height:1.6;margin-bottom:40px;}
.cover-stats{display:grid;grid-template-columns:repeat(6,1fr);max-width:840px;border:1px solid rgba(201,168,76,.18);}
.cstat{padding:14px 15px;border-right:1px solid rgba(201,168,76,.12);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:20px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:6px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.2);font-weight:700;display:block;margin-top:3px;}
.coll-header{padding:48px 80px 20px;border-top:6px solid;}
.coll-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.coll-kk::before{content:'';width:18px;height:1px;background:currentColor;}
.coll-h2{font-family:'Playfair Display',serif;font-size:clamp(26px,3.5vw,52px);font-weight:400;line-height:.92;margin-bottom:10px;}
.coll-h2 em{font-style:italic;}
.coll-sub{font-family:'Georgia',serif;font-size:14px;color:#555;line-height:1.75;max-width:800px;margin-bottom:8px;}
.coll-count{font-size:8px;letter-spacing:3px;text-transform:uppercase;font-weight:700;border:1px solid;display:inline-block;padding:4px 12px;margin-top:6px;}
.cat-block{padding:0 80px 10px;}
.cat-hdr{display:flex;align-items:center;gap:14px;padding:20px 0 12px;border-bottom:2px solid;margin-bottom:10px;}
.cat-num{font-family:'Playfair Display',serif;font-size:28px;color:rgba(0,0,0,.07);flex-shrink:0;line-height:1;}
.cat-name{font-family:'Playfair Display',serif;font-size:clamp(16px,2vw,24px);font-weight:400;font-style:italic;}
.cat-desc{font-size:11px;color:#666;margin-top:2px;line-height:1.4;}
.cat-books{font-size:9px;letter-spacing:1px;color:#888;margin-top:3px;}
.new-cat{background:rgba(201,168,76,.03);border-left:4px solid var(--gold);}
.new-badge{display:inline-block;font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;padding:2px 7px;background:rgba(201,168,76,.12);border:1px solid var(--gold-dk);color:var(--gold-dk);margin-left:8px;vertical-align:middle;}
.series-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;padding-bottom:20px;}
.s-card{padding:12px 14px;border:1px solid rgba(0,0,0,.06);background:rgba(255,255,255,.55);}
.s-card:nth-child(1){grid-column:1/-1;border-width:2px;background:rgba(255,255,255,.8);}
.s-card:nth-child(2),.s-card:nth-child(3){grid-column:span 2;}
.s-num{font-size:8px;letter-spacing:2px;color:#bbb;font-weight:700;display:block;margin-bottom:4px;}
.s-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:var(--ink);line-height:1.25;margin-bottom:3px;}
.s-card:nth-child(1) .s-title{font-size:16px;}
.s-sub{font-size:10px;color:#7a6a5a;line-height:1.35;}
.s-ref{font-size:8px;color:#aaa;margin-top:4px;letter-spacing:.5px;}
.s-badge{display:inline-block;font-size:7px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;padding:2px 6px;border:1px solid;margin-top:4px;}
.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.2),transparent);}
.new-divider{margin:0 80px 0;padding:20px 24px 8px;border-left:4px solid var(--gold);}
.new-divider p{font-family:'Georgia',serif;font-size:13px;font-style:italic;color:#666;}
.back{background:#010406;padding:48px 80px;text-align:center;}
.back-q{font-family:'Playfair Display',serif;font-size:clamp(13px,1.8vw,18px);font-style:italic;color:var(--cream);max-width:740px;margin:0 auto 16px;line-height:1.5;}
.back-a{font-size:8.5px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.back-c{margin-top:12px;font-size:11.5px;color:#5a6a7a;}
.back-c a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:28px;color:#fff;font-style:italic;margin-top:22px;}
@media(max-width:960px){
  .cover-top,.cover-body,.coll-header,.cat-block,.back,.new-divider{padding-left:28px;padding-right:28px;}
  .series-grid{grid-template-columns:1fr 1fr;}
  .s-card:nth-child(1),.s-card:nth-child(2),.s-card:nth-child(3){grid-column:auto;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
}
"""

def sc(n, title, sub, ref, badge=None, color="#4a5a8a"):
    b = f'<span class="s-badge" style="border-color:{color};color:{color};">{e(badge)}</span>' if badge else ""
    return f'<div class="s-card"><span class="s-num">{n:02d}</span><p class="s-title">{e(title)}</p><p class="s-sub">{e(sub)}</p><p class="s-ref">{e(ref)}</p>{b}</div>'

def cat_sec(num, name, desc, books, color, entries, is_new=False):
    cards = "".join(sc(i+1,t,s,r,b,color) for i,(t,s,r,b) in enumerate(entries))
    bk = f'<p class="cat-books">{e(books)}</p>' if books else ""
    nb = '<span class="new-badge">New Category</span>' if is_new else ""
    nc = " new-cat" if is_new else ""
    return f'<div class="cat-block{nc}"><div class="cat-hdr" style="border-color:{color};"><span class="cat-num">{num:02d}</span><div><h3 class="cat-name" style="color:{color};">{e(name)}{nb}</h3><p class="cat-desc">{e(desc)}</p>{bk}</div></div><div class="series-grid">{cards}</div></div>'

def coll_hdr(color, kk, h2_html, sub, count):
    return f'<div class="hdiv"></div><section class="coll-header" style="border-color:{color};"><p class="coll-kk" style="color:{color};">{e(kk)}</p><h2 class="coll-h2">{h2_html}</h2><p class="coll-sub">{e(sub)}</p><span class="coll-count" style="border-color:{color};color:{color};">{e(count)}</span></section>'

def new_divider(txt):
    return f'<div class="hdiv"></div><div class="new-divider"><p>{e(txt)}</p></div>'

def build(cat_list, is_new=False):
    return "".join(cat_sec(i+1,n,d,b,c,entries,is_new) for i,(n,d,b,c,entries) in enumerate(cat_list))
