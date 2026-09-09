#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates every page of 40daycampaigns.com in EN (/), ES (/es/), PT (/pt/)."""
import json, os, sys
sys.path.insert(0, "/home/claude/build")
from strings import LANGS, CH_I18N

SITE = "/home/claude/site"
meta = json.load(open(f"{SITE}/data/meta.json"))
N = meta["catalog"]; NC = meta["channels"]; NS = meta["sessions"]
open(f"{SITE}/data/meta.js","w").write("window.META="+json.dumps(meta)+";")

def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def shell(L, rel, page, title, body, extra_scripts="", desc=None, noscriptdata=False):
    ch_names = ""
    if L["lang"] in CH_I18N:
        ch_names = f'<script>window.CH_NAMES={json.dumps(CH_I18N[L["lang"]],ensure_ascii=False)};</script>'
    nav = f"""
<a class="skiplink" href="#main">{L['skip']}</a>
<header class="site"><div class="wrap nav">
 <a class="logo" href="{rel}index.html"><span class="mark">40</span> 40 Day Campaigns</a>
 <button class="hamb" aria-label="Menu">☰</button>
 <nav class="nav-links" aria-label="Primary">
  <a href="{rel}browse.html">{L['nav_browse']}</a>
  <a href="{rel}finder.html">{L['nav_finder']}</a>
  <a href="{rel}builder.html">{L['nav_builder']}</a>
  <a href="{rel}formats.html">{L['nav_formats']}</a>
  <a href="{rel}pricing.html">{L['nav_pricing']}</a>
  <a href="{rel}for-pastors.html">{L['nav_pastors']}</a>
 </nav>
 <div class="nav-cta">
  <a href="{rel}signin.html" class="cartlink">{L['nav_signin']}</a>
  <a href="{rel}cart.html" class="cartlink">{L['nav_cart']}<span class="n" style="display:none">0</span></a>
  <a class="btn primary sm" href="{rel}finder.html">{L['hero_cta1']}</a>
 </div></div></header>"""
    langlinks = {"en": rel, "es": rel + "es/" if rel == "" else ("../" if L["lang"] != "es" else ""), "pt": rel + "pt/" if rel == "" else ("../" if L["lang"] != "pt" else "")}
    # simpler: compute from root
    root = rel  # "" for en pages, "../" for es/pt
    lang_href = {"en": f"{root}index.html", "es": f"{root}es/index.html", "pt": f"{root}pt/index.html"}
    if L["lang"] != "en":
        lang_href = {"en": "../index.html", "es": "../es/index.html", "pt": "../pt/index.html"}
    foot = f"""
<footer class="site"><div class="wrap">
 <div class="footgrid">
  <div><a class="logo" href="{rel}index.html" style="color:#fff"><span class="mark">40</span> 40 Day Campaigns</a>
   <p style="margin-top:14px;max-width:34ch;color:#9aa3b8">{L['foot_tag']}</p></div>
  <div><h4>{L['foot_product']}</h4><a href="{rel}browse.html">{L['nav_browse']}</a><a href="{rel}finder.html">{L['nav_finder']}</a><a href="{rel}builder.html">{L['nav_builder']}</a><a href="{rel}formats.html">{L['nav_formats']}</a><a href="{rel}included.html">{L['foot_included']}</a><a href="{rel}seasonal.html">{L['foot_seasonal']}</a><a href="{rel}pricing.html">{L['nav_pricing']}</a></div>
  <div><h4>{L['foot_company']}</h4><a href="{rel}about.html">{L['foot_about']}</a><a href="{rel}case-studies.html">{L['foot_cases']}</a><a href="{rel}how-it-works.html">{L['foot_how']}</a><a href="{rel}faq.html">{L['foot_faq']}</a><a href="{rel}contact.html">{L['foot_contact']}</a></div>
  <div><h4>{L['foot_tracks']}</h4><a href="{rel}for-pastors.html">{L['foot_pastors']}</a><a href="{rel}for-churches.html">{L['foot_churches']}</a><a href="{rel}browse.html?ch=13">{L['foot_advisors']}</a><a href="{rel}account.html">{L['foot_account']}</a></div>
  <div><h4>{L['foot_lang']}</h4><a href="{lang_href['en']}">English</a><a href="{lang_href['es']}">Español</a><a href="{lang_href['pt']}">Português</a></div>
 </div>
 <div class="footnote"><span>{L['legal']}</span><span>Lifetogether · Purpose Driven lineage · 500+ church partnerships</span></div>
</div></footer>"""
    data_scripts = "" if noscriptdata else f"""
<script>window.REL="{rel}";</script>{ch_names}
<script src="{rel}data/index.js"></script>
<script src="{rel}data/meta.js"></script>
<script src="{rel}data/scripture.js"></script>
<script src="{rel}assets/js/covers.js"></script>
<script src="{rel}assets/js/app.js"></script>"""
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc or L['desc'])}">
<link rel="stylesheet" href="{rel}assets/css/fonts.css">
<link rel="stylesheet" href="{rel}assets/css/site.css">
<link rel="icon" href="data:image/svg+xml,{('%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%23172542%22/%3E%3Ctext x=%2216%22 y=%2222%22 font-family=%22Arial%22 font-weight=%22700%22 font-size=%2214%22 fill=%22%23C9A13B%22 text-anchor=%22middle%22%3E40%3C/text%3E%3C/svg%3E')}">
</head><body>{nav}<main id="main">{body}</main>{foot}{data_scripts}{extra_scripts}
</body></html>"""

TILE_GRADS = ["#172542,#22335A","#101E38,#1d2c50","#22335A,#2b3d68","#15223f,#101E38","#1b2a49,#22335A",
 "#20304f,#101E38","#172542,#101E38","#2b3d68,#172542","#101E38,#22335A","#1d2c50,#15223f",
 "#22335A,#1b2a49","#152036,#22335A","#172542,#20304f","#101E38,#1b2a49","#1b2a49,#101E38",
 "#22335A,#101E38","#15223f,#2b3d68","#1d2c50,#101E38","#B98D3E,#8f6a25","#172542,#0d1830",
 "#101E38,#172542","#C85A28,#8f3d18","#E2703A,#b34e1e"]

def page_index(L, rel):
    lede = L["hero_lede"].replace("{n}", f'{N:,}').replace("{c}", str(NC))
    tiers_html = ""
    for i,(name,sub,amt,feats) in enumerate(L["tiers"]):
        pop = ' pop' if i==1 else ''
        tag = f'<div class="tag">{L["most_pop"]}</div>' if i==1 else ''
        cta = L["tier_cta4"] if i==3 else L["tier_cta"]
        href = "builder.html" if i==3 else "browse.html"
        tiers_html += f'''<div class="price{pop}">{tag}<h3>{name}</h3><p class="muted" style="font-family:var(--ff-ui);font-size:14px">{sub}</p>
        <div class="amt">${amt}<small> {L["per_campaign"]}</small></div><ul>{''.join(f'<li>{f}</li>' for f in feats)}</ul>
        <a class="btn {'gold' if i==1 else 'navy'}" style="margin-top:auto" href="{rel}{href}">{cta}</a></div>'''
    recv_html = "".join(f'<div class="recv"><div class="ic">{i+1}</div><div><b>{t}</b><p>{d}</p></div></div>' for i,(t,d) in enumerate(L["recv"]))
    faqs_html = "".join(f'<details class="faq"><summary>{q}</summary><div><p>{a}</p></div></details>' for q,a in L["faqs"])
    body = f"""
<section class="hero"><div class="wrap">
 <div><p class="eyebrow">{L['hero_eyebrow']}</p><h1>{L['hero_h1']}</h1>
  <p class="lede">{lede}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:26px">
   <a class="btn primary" href="{rel}finder.html">{L['hero_cta1']}</a>
   <a class="btn ghost" href="{rel}builder.html">{L['hero_cta2']}</a></div></div>
 <div class="hero-cards" id="herocards" aria-hidden="true"></div>
</div></section>
<div class="cred"><div class="wrap">
 <div><b>25</b><span>{L['cred_years']}</span></div>
 <div><b>500+</b><span>{L['cred_churches']}</span></div>
 <div><b>{N:,}</b><span>{L['cred_campaigns']}</span></div>
 <div><b>4</b><span>{L['cred_editions']}</span></div>
</div></div>
<section><div class="wrap">
 <p class="eyebrow">{L['chan_eyebrow']}</p><h2>{L['chan_h2']}</h2>
 <p class="lede" style="max-width:62ch">{L['chan_sub']}</p>
 <div class="grid g4" id="tiles" style="margin-top:30px"></div>
</div></section>
<section class="tight"><div class="wrap">
 <div class="rowhead"><span class="tab-ember gold">{L['flag_tab']}</span><a class="seeall" href="{rel}browse.html?c=1">{L['seeall']} →</a></div>
 <div class="rowline gold"></div>
 <p class="muted" style="max-width:66ch;margin-top:14px;font-family:var(--ff-ui);font-size:15px">{L['flag_sub']}</p>
 <div class="cardrow" id="flagrow"></div>
</div></section>
<section><div class="wrap"><div class="grid g2" style="align-items:center">
 <div><h2>{L['problem_h2']}</h2><div class="prose"><p>{L['problem_p']}</p></div></div>
 <div class="prose"><blockquote>{L['resolve_p']}</blockquote></div>
</div></div></section>
<section class="tight" style="background:#fffdf8;border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
 <p class="eyebrow">{L['fmt_eyebrow']}</p><h2>{L['fmt_h2']}</h2>
 <div class="grid g4" style="margin-top:26px">
  <div class="fmtcard hot"><div class="len">40 <small>{L['days']}</small></div><h4 style="margin:8px 0 4px">40-Day Journey</h4><p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em;text-transform:uppercase">{L['weeks6']}</p><p>{L['fmt40']}</p></div>
  <div class="fmtcard"><div class="len">30 <small>{L['days']}</small></div><h4 style="margin:8px 0 4px">30-Day Spiritual Journey</h4><p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em;text-transform:uppercase">{L['weeks4']}</p><p>{L['fmt30']}</p></div>
  <div class="fmtcard"><div class="len">21 <small>{L['days']}</small></div><h4 style="margin:8px 0 4px">21-Day Challenge</h4><p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em;text-transform:uppercase">{L['weeks3']}</p><p>{L['fmt21']}</p></div>
  <div class="fmtcard"><div class="len">7 <small>{L['days']}</small></div><h4 style="margin:8px 0 4px">7-Day Experience</h4><p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em;text-transform:uppercase">{L['week1']}</p><p>{L['fmt7']}</p></div>
 </div></div></section>
<section><div class="wrap">
 <p class="eyebrow navy">{L['recv_eyebrow']}</p><h2>{L['recv_h2']}</h2>
 <div class="grid g3" style="margin-top:24px">{recv_html}</div>
 <p class="prose" style="margin-top:22px"><i>{L['recv_note']}</i></p>
</div></section>
<section class="tight"><div class="wrap">
 <div class="rowhead"><span class="tab-ember">{L['sea_tab']}</span><a class="seeall" href="{rel}seasonal.html">{L['foot_seasonal']} →</a></div>
 <div class="rowline"></div>
 <p class="muted" style="margin-top:14px;font-family:var(--ff-ui);font-size:15px">{L['sea_sub']}</p>
 <div class="cardrow" id="searow"></div>
</div></section>
<section style="background:#fffdf8;border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
 <p class="eyebrow gold">{L['price_eyebrow']}</p><h2>{L['price_h2']}</h2>
 <div class="grid g4" style="margin-top:34px">{tiers_html}</div>
</div></section>
<section><div class="wrap"><div class="grid g2" style="align-items:center">
 <div><p class="eyebrow gold">{L['herit_eyebrow']}</p><h2>{L['herit_h2']}</h2></div>
 <div class="prose"><p>{L['herit_p']}</p></div>
</div></div></section>
<section class="tight"><div class="wrap" style="max-width:860px">
 <h2>{L['faq_h2']}</h2>{faqs_html}
</div></section>
<section class="closing"><div class="wrap">
 <h2>{L['close_h2']}</h2><p class="lede" style="color:#cfd6e4">{L['close_p']}</p>
 <a class="btn gold" style="margin-top:18px" href="{rel}finder.html">{L['close_cta']}</a>
</div></section>"""
    script = f"""
<script>
(function(){{const A=window.App,G={json.dumps(TILE_GRADS)};
const tiles=document.getElementById('tiles');
tiles.innerHTML=A.D.channels.map((c,i)=>{{const n=window.META.per_channel[i]||0;
 const isNew=i>=21;return `<a class="tile" href="{rel}channel.html?c=${{i}}" style="background:linear-gradient(150deg,${{G[i].split(',')[0]}},${{G[i].split(',')[1]}})">${{isNew?`<span class=\\"new\\">{L['new']}</span>`:''}}<h4>${{A.chLabel(i)}}</h4><span class="n">${{n.toLocaleString()}} {L['campaigns_word']}</span></a>`}}).join('');
const flag=A.ROWS.filter(o=>o.co&1&&o.g==='AA').concat(A.ROWS.filter(o=>o.co&1&&o.g!=='AA')).slice(0,14);
document.getElementById('flagrow').innerHTML=flag.map(o=>A.cardHTML(o)).join('');
const hc=document.getElementById('herocards');const hs=flag.slice(0,4);
hc.innerHTML=hs.map((o,i)=>`<div class="hc" style="--rot:${{[-7,4,-3,6][i]}}deg;top:${{[8,30,180,205][i]}}px;left:${{[6,52,14,58][i]}}%">${{window.Covers.svg(o)}}</div>`).join('');
/* seasonal next-90 */
const W={{0:[[10,27],[11,24]],1:[[11,25],[0,5]],2:[[0,1],[0,31]],3:[[1,4],[3,20]],4:[[2,22],[3,25]],5:[[4,10],[5,13]],6:[[4,1],[4,14]],7:[[5,8],[5,21]],8:[[5,1],[7,31]],9:[[7,1],[8,30]],10:[[10,1],[10,30]]}};
function inWin(se){{const t=new Date(),y=t.getFullYear();
 for(const off of [0,1]){{const [[m1,d1],[m2,d2]]=W[se];let a=new Date(y+ (m1>m2?off-0:off),m1,d1),b=new Date(y+off+(m1>m2?1:0)*0 + (m1>m2?0:0),m2,d2);
  if(m1>m2)b=new Date(a.getFullYear()+1,m2,d2);
  const end=new Date(t.getTime()+90*864e5);
  if(a<=end&&b>=t)return true}}return false}}
const sea=A.ROWS.filter(o=>o.se>=0&&inWin(o.se)).slice(0,14);
document.getElementById('searow').innerHTML=(sea.length?sea:A.ROWS.filter(o=>o.co&2).slice(0,14)).map(o=>A.cardHTML(o)).join('');
A.paintCovers(document);}})();
</script>"""
    return shell(L, rel, "index", L["title"], body, script)

def page_browse(L, rel):
    body = f"""
<section class="tight"><div class="wrap">
 <h1 style="font-size:clamp(30px,3.6vw,44px)">{L['br_h1']}</h1>
 <p class="lede">{L['br_sub'].replace('{{n}}', '{n}').replace('{n}', f'{N:,}')}</p>
 <div class="searchbar" style="margin-top:20px">
  <input id="q" type="search" placeholder="{L['br_search']}" aria-label="{L['br_search']}">
  <select id="sort" aria-label="Sort"><option value="rel">{L['sort_rel']}</option><option value="pop">{L['sort_pop']}</option><option value="new">{L['sort_new']}</option><option value="az">{L['sort_az']}</option><option value="len">{L['sort_len']}</option></select>
  <button class="btn ghost sm mobile-filters" id="mfilters">{L['filters']}</button>
 </div>
 <div class="results-meta"><b id="rescount"></b><span id="activef"></span><button class="fchip" id="clearall" style="background:var(--muted)">{L['clear']}</button><span id="perf" class="muted"></span></div>
 <div class="browse-layout">
  <aside class="rail" aria-label="{L['filters']}"><div id="railbody"></div></aside>
  <div>
   <div id="empty" class="hide"><h3>{L['empty_h']}</h3><p class="muted">{L['empty_p']}</p><div class="grid g3" id="nearby"></div></div>
   <div id="vlist" role="list"></div>
  </div>
 </div>
</div></section>"""
    return shell(L, rel, "browse", f"{L['nav_browse']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/browse.js"></script>')

def page_channel(L, rel):
    body = f"""
<section class="tight"><div class="wrap">
 <div class="crumb"><a href="{rel}index.html">40 Day Campaigns</a> / <span id="chname2"></span></div>
 <h1 id="chname" style="font-size:clamp(30px,3.6vw,44px)"></h1>
 <p class="lede" id="chsub"></p>
 <div class="rowhead" style="margin-top:26px"><span class="tab-ember gold">{L['flag_tab']}</span></div><div class="rowline gold"></div>
 <div class="cardrow" id="chflag"></div>
 <h3 style="margin-top:34px">Themes</h3><div id="themes" style="display:flex;gap:10px;flex-wrap:wrap"></div>
 <h3 style="margin-top:34px"><span id="allcount"></span></h3>
 <div class="grid g5" id="chgrid"></div>
 <div class="center" style="margin-top:26px"><button class="btn navy" id="more">More</button></div>
</div></section>"""
    script = f"""
<script>
(function(){{const A=window.App;const ci=+(new URLSearchParams(location.search).get('c')||0);
const name=A.chLabel(ci);document.title=name+' — 40 Day Campaigns';
document.getElementById('chname').textContent=name;document.getElementById('chname2').textContent=name;
document.getElementById('chsub').textContent=(window.META.per_channel[ci]||0).toLocaleString()+' {L['campaigns_word']} · '+'{L['chan_sub']}'.split('.')[0]+'.';
const rows=A.ROWS.filter(o=>o.ch===ci);
document.getElementById('chflag').innerHTML=rows.filter(o=>o.co&1).slice(0,14).map(o=>A.cardHTML(o)).join('')||'<p class="muted" style="padding:16px">—</p>';
const tset=new Map();rows.forEach(o=>tset.set(o.th,(tset.get(o.th)||0)+1));
const themes=[...tset.entries()].sort((a,b)=>b[1]-a[1]);
document.getElementById('themes').innerHTML=themes.slice(0,40).map(([t,n])=>`<a class="chip" style="font-size:12.5px;padding:7px 12px" href="{rel}theme.html?t=${{t}}">${{A.escapeH(A.themeLabel(t))}} · ${{n}}</a>`).join('');
document.getElementById('allcount').textContent=rows.length.toLocaleString()+' {L['campaigns_word']}';
let shown=0;const grid=document.getElementById('chgrid');
function more(){{const chunk=rows.slice(shown,shown+40);shown+=chunk.length;
 grid.insertAdjacentHTML('beforeend',chunk.map(o=>A.cardHTML(o)).join(''));A.paintCovers(grid);
 if(shown>=rows.length)document.getElementById('more').classList.add('hide')}}
document.getElementById('more').addEventListener('click',more);more();A.paintCovers(document);}})();
</script>"""
    return shell(L, rel, "channel", "Channel — 40 Day Campaigns", body, script)

def page_theme(L, rel):
    body = f"""
<section class="tight"><div class="wrap">
 <div class="crumb" id="crumb"></div>
 <h1 id="thname" style="font-size:clamp(30px,3.6vw,44px)"></h1>
 <p class="lede" id="thsub"></p>
 <div class="grid g5" id="grid" style="margin-top:26px"></div>
 <div class="center" style="margin-top:26px"><button class="btn navy" id="more">More</button></div>
</div></section>"""
    script = f"""
<script>
(function(){{const A=window.App;const ti=+(new URLSearchParams(location.search).get('t')||0);
const th=A.D.themes[ti]||[0,'—'];const ci=th[0];const name=th[1];
document.title=name+' — 40 Day Campaigns';
document.getElementById('crumb').innerHTML=`<a href="{rel}index.html">40 Day Campaigns</a> / <a href="{rel}channel.html?c=${{ci}}">${{A.escapeH(A.chLabel(ci))}}</a>`;
document.getElementById('thname').textContent=name;
const rows=A.ROWS.filter(o=>o.th===ti);
document.getElementById('thsub').textContent=rows.length.toLocaleString()+' {L['campaigns_word']} · '+A.chLabel(ci);
let shown=0;const grid=document.getElementById('grid');
function more(){{const chunk=rows.slice(shown,shown+40);shown+=chunk.length;
 grid.insertAdjacentHTML('beforeend',chunk.map(o=>A.cardHTML(o)).join(''));A.paintCovers(grid);
 if(shown>=rows.length)document.getElementById('more').classList.add('hide')}}
document.getElementById('more').addEventListener('click',more);more();}})();
</script>"""
    return shell(L, rel, "theme", "Theme — 40 Day Campaigns", body, script)

def page_campaign(L, rel):
    ed = lambda k: f'<div class="edbox"><h4>{L[k][0]}</h4><ul>{"".join(f"<li>{x}</li>" for x in L[k][1])}</ul></div>'
    body = f"""
<section class="tight"><div class="wrap">
 <div class="crumb" id="crumb"></div>
 <div class="detail-top">
  <div><div class="coverbig" id="cover"></div></div>
  <div>
   <span id="flag" class="chip hide" style="background:var(--gold);color:var(--navy-900);font-size:11px">★ {L['flag_tab'].split(' ')[0].upper()}</span>
   <h1 id="title" style="font-size:clamp(30px,3.4vw,42px);margin-top:8px"></h1>
   <p class="lede" id="subtitle"></p>
   <p id="promise" style="font-style:italic;color:var(--navy-700)"></p>
   <p class="muted" style="font-family:var(--ff-label);font-size:12px;letter-spacing:.05em;text-transform:uppercase">Scripture backbone · <span id="ref" style="color:var(--gold-deep)"></span></p>
   <p id="aud" style="font-family:var(--ff-ui);font-size:14.5px"></p>
   <p id="felt" style="font-family:var(--ff-ui);font-size:14.5px"></p>
   <div class="fmt-select" id="fmts"></div>
   <div class="pricebig" id="price"></div>
   <div style="display:flex;gap:12px;flex-wrap:wrap">
    <button class="btn primary" id="addbig" data-add="">{L['add_cart']}</button>
    <button class="btn ghost" id="preview">{L['preview']}</button>
   </div>
  </div>
 </div>
 <div class="dsec" id="nest" ><div class="inner"></div></div>
 <div class="dsec"><h2 id="archead">{L['arc_h']}</h2><div class="arc" id="arc"></div></div>
 <div class="dsec"><h2>{L['sermons_h']}</h2><p class="muted" style="font-family:var(--ff-ui)">{L['sermons_sub']}</p><div id="sermons"></div></div>
 <div class="dsec"><h2>{L['sess_h']}</h2><div class="grid g2" id="sess"></div></div>
 <div class="dsec"><h2>{L['editions_h']}</h2><div class="grid g2" style="margin-top:8px">{ed('ed_adult')}{ed('ed_youth')}{ed('ed_kids')}{ed('ed_leader')}</div></div>
 <div class="dsec"><div class="twocol">
  <div class="edbox" style="border-left:4px solid var(--gold)"><h4>{L['celebrate_h']}</h4><p style="margin:0">{L['celebrate_p']}</p></div>
  <div class="edbox" style="border-left:4px solid var(--ember)"><h4>{L['partner_h']}</h4><p style="margin:0">{L['partner_p']}</p></div>
 </div></div>
 <div class="dsec"><div class="rowhead"><span class="tab-ember">{L['related_h']}</span></div><div class="rowline"></div><div class="cardrow" id="relrow"></div></div>
</div></section>
<div id="modal" class="hide" style="position:fixed;inset:0;background:rgba(16,30,56,.55);z-index:90;display:grid;place-items:center;padding:20px">
 <div style="background:var(--paper);border-radius:20px;max-width:720px;width:100%;max-height:86vh;overflow:auto;padding:30px;position:relative">
  <button class="mclose btn sm ghost" style="position:absolute;top:14px;right:14px">✕</button>
  <p class="eyebrow gold">{L['sample_h']}</p>
  <div class="inner"></div>
  <div class="no-print" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:20px">
   <button class="btn navy sm" id="printday">{L['print_pdf']}</button>
   <button class="btn ghost sm" id="worddoc">{L['word_doc']}</button>
   <button class="btn ghost sm" id="canva">{L['canva']}</button>
  </div></div></div>"""
    return shell(L, rel, "campaign", "Campaign — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/campaign.js"></script>')

def page_finder(L, rel):
    body = f"""
<section><div class="wrap">
 <div class="center" style="max-width:720px;margin:0 auto 34px">
  <p class="eyebrow">{L['nav_finder']}</p><h1>{L['fin_h1']}</h1><p class="lede">{L['fin_sub']}</p></div>
 <div id="finder"><div class="qcard" id="qwrap"><div class="progress"><i style="width:0"></i></div><div id="qbody"></div></div>
 <div id="results" class="hide">
  <h2 class="center">{L['fin_results']}</h2>
  <div class="grid g3" id="picks" style="margin-top:22px"></div>
  <h3 style="margin-top:36px">{L['fin_wild']}</h3><div id="wild" class="grid g2" style="align-items:start"></div>
  <div class="center" style="margin-top:30px"><button class="btn ghost" id="again">{L['fin_again']}</button></div>
 </div></div>
</div></section>"""
    return shell(L, rel, "finder", f"{L['nav_finder']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_builder(L, rel):
    body = f"""
<section><div class="wrap">
 <div class="center" style="max-width:760px;margin:0 auto 34px">
  <p class="eyebrow">{L['nav_builder']}</p><h1>{L['bld_h1']}</h1><p class="lede">{L['bld_sub']}</p></div>
 <div id="builder"><div class="qcard" style="max-width:900px"><div class="grid g3" id="bsteps"></div></div>
 <div id="brief" class="hide"><div class="qcard" style="max-width:900px"><div class="inner"></div></div></div></div>
</div></section>"""
    return shell(L, rel, "builder", f"{L['nav_builder']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_formats(L, rel):
    rows = [("40-Day Journey", L["weeks6"], "$849", L["fmt40"]),("30-Day Spiritual Journey", L["weeks4"], "$649", L["fmt30"]),
            ("21-Day Challenge", L["weeks3"], "$449", L["fmt21"]),("7-Day Experience", L["week1"], "$249", L["fmt7"])]
    cards = "".join(f'<div class="fmtcard{" hot" if i==0 else ""}"><div class="len">{t.split("-")[0]} <small>{L["days"] if i<4 else ""}</small></div><h3 style="margin:8px 0 2px">{t}</h3><p class="muted" style="font-family:var(--ff-label);font-size:11px;letter-spacing:.05em;text-transform:uppercase">{w} · {p} {L["per_campaign"]}</p><p>{d}</p><a class="btn navy sm" style="margin-top:auto" href="{rel}browse.html?f={[8,4,2,1][i]}">{L["tier_cta"]}</a></div>' for i,(t,w,p,d) in enumerate(rows))
    body = f"""
<section><div class="wrap">
 <p class="eyebrow">{L['nav_formats']}</p><h1>{L['fp_h1']}</h1><p class="lede" style="max-width:64ch">{L['fp_sub']}</p>
 <div class="grid g4" style="margin-top:30px">{cards}</div>
 <div class="prose" style="margin-top:44px"><blockquote>{L['resolve_p']}</blockquote></div>
</div></section>"""
    return shell(L, rel, "formats", f"{L['nav_formats']} — 40 Day Campaigns", body)

def page_included(L, rel):
    recv_html = "".join(f'<div class="recv"><div class="ic">{i+1}</div><div><b>{t}</b><p>{d}</p></div></div>' for i,(t,d) in enumerate(L["recv"]))
    ed = lambda k: f'<div class="edbox"><h4>{L[k][0]}</h4><ul>{"".join(f"<li>{x}</li>" for x in L[k][1])}</ul></div>'
    body = f"""
<section><div class="wrap">
 <p class="eyebrow navy">{L['recv_eyebrow']}</p><h1>{L['inc_h1']}</h1><p class="lede">{L['inc_sub']}</p>
 <div class="grid g3" style="margin-top:28px">{recv_html}</div>
 <h2 style="margin-top:48px">{L['editions_h']}</h2>
 <div class="grid g2">{ed('ed_adult')}{ed('ed_youth')}{ed('ed_kids')}{ed('ed_leader')}</div>
 <p class="prose" style="margin-top:24px"><i>{L['recv_note']}</i></p>
 <a class="btn primary" href="{rel}browse.html">{L['tier_cta']}</a>
</div></section>"""
    return shell(L, rel, "included", f"{L['foot_included']} — 40 Day Campaigns", body)

def page_pricing(L, rel):
    tiers_html = ""
    for i,(name,sub,amt,feats) in enumerate(L["tiers"]):
        pop = ' pop' if i==1 else ''
        tag = f'<div class="tag">{L["most_pop"]}</div>' if i==1 else ''
        cta = L["tier_cta4"] if i==3 else L["tier_cta"]
        href = "builder.html" if i==3 else "browse.html"
        tiers_html += f'''<div class="price{pop}">{tag}<h3>{name}</h3><p class="muted" style="font-family:var(--ff-ui);font-size:14px">{sub}</p>
        <div class="amt">${amt}<small> {L["per_campaign"]}</small></div><ul>{''.join(f'<li>{f}</li>' for f in feats)}</ul>
        <a class="btn {'gold' if i==1 else 'navy'}" style="margin-top:auto" href="{rel}{href}">{cta}</a></div>'''
    alacarte = [("6-Session Study","$549"),("Catalytic Sunday kit","$149"),("Additional campus license","$99"),("Spanish or Portuguese edition of a flagship","$199")]
    tbl = "".join(f"<tr><td>{a}</td><td style='text-align:right'><b>{b}</b></td></tr>" for a,b in alacarte)
    body = f"""
<section><div class="wrap">
 <p class="eyebrow gold">{L['price_eyebrow']}</p><h1>{L['pr_h1']}</h1><p class="lede">{L['pr_sub']}</p>
 <div class="grid g4" style="margin-top:36px">{tiers_html}</div>
 <p class="muted" style="margin-top:18px;font-family:var(--ff-ui);font-size:14px">{L['pr_grade']}</p>
 <h3 style="margin-top:40px">À la carte</h3>
 <table class="simple" style="max-width:560px"><tbody>{tbl}</tbody></table>
 <div style="margin-top:34px"><a class="btn primary" href="{rel}browse.html">{L['tier_cta']}</a></div>
</div></section>"""
    return shell(L, rel, "pricing", f"{L['nav_pricing']} — 40 Day Campaigns", body)

def page_how(L, rel):
    steps = "".join(f'<div class="intel"><div class="num">{i+1}</div><h3>{t}</h3><p style="margin:0;font-size:15.5px">{d}</p></div>' for i,(t,d) in enumerate(L["how"]))
    body = f"""
<section><div class="wrap">
 <p class="eyebrow">{L['foot_how']}</p><h1>{L['how_h1']}</h1><p class="lede">{L['how_sub']}</p>
 <div class="grid g3" style="margin-top:30px">{steps}</div>
 <div style="margin-top:34px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn primary" href="{rel}finder.html">{L['hero_cta1']}</a><a class="btn ghost" href="{rel}for-churches.html">{L['foot_churches']}</a></div>
</div></section>"""
    return shell(L, rel, "how-it-works", f"{L['foot_how']} — 40 Day Campaigns", body)

def page_track(L, rel, which):
    if which=="pastors":
        h1,p1,p2 = L["fps_h1"],L["fps_p1"],L["fps_p2"]; rowsel="o.co&8"; tab="The Pastor's Shelf · Grade AA"
    else:
        h1,p1,p2 = L["fch_h1"],L["fch_p1"],L["fch_p2"]; rowsel="o.f&16"; tab=L["sess_h"]
    body = f"""
<section><div class="wrap">
 <h1>{h1}</h1>
 <div class="grid g2" style="align-items:start;margin-top:16px">
  <div class="prose"><p>{p1}</p></div><div class="prose"><p>{p2}</p></div></div>
 <div class="rowhead" style="margin-top:34px"><span class="tab-ember gold">{tab}</span></div><div class="rowline gold"></div>
 <div class="cardrow" id="trackrow"></div>
 <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn primary" href="{rel}finder.html">{L['hero_cta1']}</a><a class="btn ghost" href="{rel}builder.html">{L['hero_cta2']}</a></div>
</div></section>"""
    script=f"""<script>(function(){{const A=window.App;
const rows=A.ROWS.filter(o=>{rowsel}).slice(0,16);
document.getElementById('trackrow').innerHTML=rows.map(o=>A.cardHTML(o)).join('');A.paintCovers(document)}})();</script>"""
    return shell(L, rel, "track", f"{h1} — 40 Day Campaigns", body, script)

def page_seasonal(L, rel):
    body = f"""
<section><div class="wrap">
 <p class="eyebrow">{L['foot_seasonal']}</p><h1>{L['se_h1']}</h1><p class="lede">{L['se_sub']}</p>
 <div id="seasons" class="grid g2" style="margin-top:28px"></div>
</div></section>"""
    script = f"""
<script>(function(){{const A=window.App;const SEA=A.D.seasons;
const W={{0:[10,27,11,24],1:[11,25,0,5],2:[0,1,0,31],3:[1,4,3,20],4:[2,22,3,25],5:[4,10,5,13],6:[4,1,4,14],7:[5,8,5,21],8:[5,1,7,31],9:[7,1,8,30],10:[10,1,10,30]}};
const t=new Date(),end=new Date(t.getTime()+90*864e5);
function win(se,yoff){{const[m1,d1,m2,d2]=W[se];const y=t.getFullYear()+yoff;
 const a=new Date(y,m1,d1),b=new Date(m1>m2?y+1:y,m2,d2);return[a,b]}}
const list=[];for(let se=0;se<11;se++)for(const off of[0,1]){{const[a,b]=win(se,off);
 if(b<t||a>new Date(t.getTime()+300*864e5))continue;list.push([se,a,b,a<=end&&b>=t]);break}}
list.sort((x,y)=>x[1]-y[1]);
const fmt=d=>d.toLocaleDateString('{ "en-US" if L["lang"]=="en" else ("es-ES" if L["lang"]=="es" else "pt-BR") }',{{month:'short',day:'numeric'}});
document.getElementById('seasons').innerHTML=list.map(([se,a,b,now])=>{{
 const rows=A.ROWS.filter(o=>o.se===se).slice(0,4);
 return `<div class="season${{now?' now':''}}"><span class="when">${{now?'{L['se_now']} · ':''}}${{fmt(a)}} – ${{fmt(b)}}</span><h3 style="margin:6px 0 12px">${{SEA[se]}}</h3>
 <div class="grid g4" style="gap:12px">${{rows.map(o=>A.cardHTML(o)).join('')}}</div>
 <a class="seeall" style="display:inline-block;margin-top:12px" href="{rel}browse.html?se=${{se}}">{L['seeall']} →</a></div>`}}).join('');
A.paintCovers(document)}})();</script>"""
    return shell(L, rel, "seasonal", f"{L['foot_seasonal']} — 40 Day Campaigns", body, script)

def page_about(L, rel):
    body = f"""
<section><div class="wrap">
 <p class="eyebrow gold">{L['herit_eyebrow']}</p><h1>{L['ab_h1']}</h1>
 <div class="prose"><p>{L['ab_p1']}</p><p>{L['ab_p2']}</p><p>{L['ab_p3']}</p></div>
 <div class="cred" style="margin-top:36px;border-radius:16px"><div class="wrap" style="padding-left:0;padding-right:0">
  <div><b>25</b><span>{L['cred_years']}</span></div><div><b>500+</b><span>{L['cred_churches']}</span></div>
  <div><b>{N:,}</b><span>{L['cred_campaigns']}</span></div><div><b>{NS}</b><span>{L['sessions_word']}</span></div></div></div>
 <div style="margin-top:34px"><a class="btn primary" href="{rel}case-studies.html">{L['foot_cases']}</a></div>
</div></section>"""
    return shell(L, rel, "about", f"{L['foot_about']} — 40 Day Campaigns", body)

def page_cases(L, rel):
    cs = "".join(f'<div class="edbox" style="border-top:4px solid var(--gold)"><h3>{t}</h3><p style="margin:0">{d}</p></div>' for t,d in L["cases"])
    body = f"""
<section><div class="wrap">
 <h1>{L['cs_h1']}</h1><p class="muted" style="font-family:var(--ff-ui);max-width:64ch">{L['cs_note']}</p>
 <div class="grid g3" style="margin-top:26px">{cs}</div>
 <div style="margin-top:34px"><a class="btn primary" href="{rel}finder.html">{L['hero_cta1']}</a></div>
</div></section>"""
    return shell(L, rel, "case-studies", f"{L['foot_cases']} — 40 Day Campaigns", body)

def page_faq(L, rel):
    faqs_html = "".join(f'<details class="faq"><summary>{q}</summary><div><p>{a}</p></div></details>' for q,a in L["faqs"])
    body = f"""
<section><div class="wrap" style="max-width:860px">
 <h1>{L['faq_h2']}</h1>{faqs_html}
 <div style="margin-top:30px"><a class="btn ghost" href="{rel}contact.html">{L['foot_contact']}</a></div>
</div></section>"""
    return shell(L, rel, "faq", f"{L['foot_faq']} — 40 Day Campaigns", body)

def page_cart(L, rel):
    body = f"""<section><div class="wrap" style="max-width:860px"><h1>{L['cart_h1']}</h1><div id="cartpage" style="margin-top:20px"></div></div></section>"""
    return shell(L, rel, "cart", f"{L['cart_h1']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_checkout(L, rel):
    body = f"""
<section><div class="wrap"><h1>{L['ck_h1']}</h1>
 <div class="grid g2" style="align-items:start;margin-top:20px" id="checkout">
  <div class="qcard" style="max-width:none">
   <div class="field"><label for="co-church">{L['ck_church']}</label><input id="co-church"><div class="err">Required</div></div>
   <div class="grid g2">
    <div class="field"><label for="co-name">{L['ck_name']}</label><input id="co-name"><div class="err">Required</div></div>
    <div class="field"><label for="co-email">{L['ck_email']}</label><input id="co-email" type="email"><div class="err">Valid email required</div></div></div>
   <div class="paytabs">
    <button class="paytab on" data-m="card">{L['ck_card']}</button>
    <button class="paytab" data-m="paypal">{L['ck_paypal']}</button>
    <button class="paytab" data-m="invoice">{L['ck_invoice']}</button></div>
   <div class="payform" id="pf-card">
    <div class="field"><label for="cc-num">Card number</label><input id="cc-num" inputmode="numeric" placeholder="4242 4242 4242 4242"><div class="err">Card number</div></div>
    <div class="grid g2">
     <div class="field"><label for="cc-exp">MM/YY</label><input id="cc-exp" placeholder="08/27"><div class="err">MM/YY</div></div>
     <div class="field"><label for="cc-cvc">CVC</label><input id="cc-cvc" inputmode="numeric" placeholder="123"><div class="err">CVC</div></div></div></div>
   <div class="payform hide" id="pf-paypal"><p class="muted" style="font-family:var(--ff-ui)">You will be redirected to PayPal to approve this payment when the live gateway is connected.</p></div>
   <div class="payform hide" id="pf-invoice">
    <div class="field"><label for="po-num">PO number</label><input id="po-num" placeholder="PO-2026-001"><div class="err">PO number</div></div>
    <p class="muted" style="font-family:var(--ff-ui);font-size:14px">Net-30 church invoice. Downloads unlock immediately; the invoice follows by email.</p></div>
   <button class="btn primary" id="place" style="width:100%;justify-content:center">{L['ck_place']}</button>
   <p class="muted" style="font-family:var(--ff-ui);font-size:13px;margin-top:12px">{L['ck_secure']}</p>
  </div>
  <div class="summary" id="osum"></div>
 </div></div></section>"""
    return shell(L, rel, "checkout", f"{L['ck_h1']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_confirm(L, rel):
    body = f"""
<section><div class="wrap" style="max-width:860px" id="confirm">
 <p class="eyebrow gold">Order <span id="ordno"></span></p>
 <h1>{L['cf_h1']}</h1><p class="lede">{L['cf_p']} <b id="ordch"></b>.</p>
 <div class="summary" id="ordsum" style="margin:22px 0"></div>
 <h3>{L['cf_dl']}</h3><div id="dls"></div>
 <p class="prose" style="margin-top:18px">{L['cf_next']}</p>
 <div style="display:flex;gap:12px;margin-top:20px"><a class="btn navy" href="{rel}account.html">{L['ac_h1']}</a><a class="btn ghost" href="{rel}browse.html">{L['nav_browse']}</a></div>
</div></section>"""
    return shell(L, rel, "confirmation", f"{L['cf_h1']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_account(L, rel):
    body = f"""
<section><div class="wrap" id="account"><h1>{L['ac_h1']}</h1>
 <h3 style="margin-top:24px">{L['ac_orders']}</h3>
 <table class="simple"><thead><tr><th>#</th><th>Date</th><th>Items</th><th>Total</th><th></th></tr></thead><tbody id="orders"></tbody></table>
 <h3 style="margin-top:34px">{L['ac_library']}</h3><div class="grid g5" id="library"></div>
</div></section>"""
    return shell(L, rel, "account", f"{L['ac_h1']} — 40 Day Campaigns", body,
                 f'<script src="{rel}assets/js/flows.js"></script>')

def page_auth(L, rel, up):
    h = L["su_h1"] if up else L["si_h1"]; btn = L["su_btn"] if up else L["si_btn"]
    other = f'<a href="{rel}signin.html">{L["si_h1"]}</a>' if up else f'<a href="{rel}signup.html">{L["su_h1"]}</a>'
    church = f'<div class="field"><label for="a-church">{L["ck_church"]}</label><input id="a-church"></div>' if up else ""
    body = f"""
<section><div class="wrap"><div class="qcard" style="max-width:460px">
 <h1 style="font-size:30px">{h}</h1>
 {church}
 <div class="field"><label for="a-email">{L['ck_email']}</label><input id="a-email" type="email"><div class="err">Valid email required</div></div>
 <div class="field"><label for="a-pass">Password</label><input id="a-pass" type="password"><div class="err">8+ characters</div></div>
 <button class="btn primary" id="a-go" style="width:100%;justify-content:center">{btn}</button>
 <p class="muted" style="font-family:var(--ff-ui);font-size:13.5px;margin-top:14px">{L['si_note']}</p>
 <p style="font-family:var(--ff-ui);font-size:14px">{other}</p>
</div></div></section>"""
    script = f"""<script>(function(){{const A=window.App;
document.getElementById('a-go').addEventListener('click',()=>{{
 const e=document.getElementById('a-email'),p=document.getElementById('a-pass');
 const eok=/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(e.value);const pok=p.value.length>=8;
 e.closest('.field').classList.toggle('bad',!eok);p.closest('.field').classList.toggle('bad',!pok);
 if(!eok||!pok)return;A.store.set('auth40',{{email:e.value,when:Date.now()}});
 A.toast('{ "Welcome back" if not up else "Account created" }');setTimeout(()=>location.href='{rel}account.html',600)}})}})();</script>"""
    return shell(L, rel, "auth", f"{h} — 40 Day Campaigns", body, script)

def page_contact(L, rel):
    body = f"""
<section><div class="wrap"><div class="grid g2" style="align-items:start">
 <div><h1>{L['co_h1']}</h1><div class="prose"><p>{L['co_p']}</p></div>
  <p style="font-family:var(--ff-ui)"><b>hello@40daycampaigns.com</b><br>Lifetogether · Rancho Santa Margarita, CA</p></div>
 <div class="qcard" style="max-width:none">
  <div class="field"><label for="c-name">{L['ck_name']}</label><input id="c-name"><div class="err">Required</div></div>
  <div class="field"><label for="c-email">{L['ck_email']}</label><input id="c-email" type="email"><div class="err">Valid email required</div></div>
  <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" rows="6"></textarea><div class="err">Required</div></div>
  <button class="btn primary" id="c-send">{L['co_send']}</button>
  <p id="c-ok" class="hide" style="color:#1C3A2D;font-family:var(--ff-ui);font-weight:600;margin-top:12px"></p>
 </div></div></div></section>"""
    script = f"""<script>(function(){{
document.getElementById('c-send').addEventListener('click',()=>{{
 const f=id=>document.getElementById(id);const ok=(id,t)=>{{const v=t(f(id).value.trim());f(id).closest('.field').classList.toggle('bad',!v);return v}};
 const good=ok('c-name',v=>v.length>1)&ok('c-email',v=>/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v))&ok('c-msg',v=>v.length>3);
 if(!good)return;const el=f('c-ok');el.textContent='{L["co_sent"]}'.replace('{{email}}',f('c-email').value.trim());
 el.classList.remove('hide');window.App.toast('✓')}})}})();</script>"""
    return shell(L, rel, "contact", f"{L['foot_contact']} — 40 Day Campaigns", body, script)

PAGES = {
 "index.html": page_index, "browse.html": page_browse, "channel.html": page_channel,
 "theme.html": page_theme, "campaign.html": page_campaign, "finder.html": page_finder,
 "builder.html": page_builder, "formats.html": page_formats, "included.html": page_included,
 "pricing.html": page_pricing, "how-it-works.html": page_how,
 "for-pastors.html": lambda L,r: page_track(L,r,"pastors"),
 "for-churches.html": lambda L,r: page_track(L,r,"churches"),
 "seasonal.html": page_seasonal, "about.html": page_about, "case-studies.html": page_cases,
 "faq.html": page_faq, "cart.html": page_cart, "checkout.html": page_checkout,
 "confirmation.html": page_confirm, "account.html": page_account,
 "signin.html": lambda L,r: page_auth(L,r,False), "signup.html": lambda L,r: page_auth(L,r,True),
 "contact.html": page_contact,
}

def build():
    os.makedirs(f"{SITE}/i18n", exist_ok=True)
    for code, L in LANGS.items():
        rel = "" if code=="en" else "../"
        outdir = SITE if code=="en" else f"{SITE}/{code}"
        os.makedirs(outdir, exist_ok=True)
        for fn, fpage in PAGES.items():
            open(f"{outdir}/{fn}", "w").write(fpage(L, rel))
        json.dump(L, open(f"{SITE}/i18n/{code}.json","w"), ensure_ascii=False, indent=1)
    print(f"pages: {len(PAGES)} × {len(LANGS)} langs = {len(PAGES)*len(LANGS)} files")

if __name__ == "__main__":
    build()
