# -*- coding: utf-8 -*-
import content as C

def esc(s):
    return s if s else ""

def env_rows():
    out = []
    for numeral, name, desc in C.ENVIRONMENTS:
        out.append(f'''
        <div class="env-row reveal">
          <div class="env-num">{numeral}</div>
          <div class="env-body">
            <h3>{name}</h3>
            <p>{desc}</p>
          </div>
        </div>''')
    return "".join(out)

def outcome_cols():
    out = []
    for name, desc in C.OUTCOMES:
        out.append(f'''
        <div class="outcome reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
        </div>''')
    return "".join(out)

def rhythm_blocks():
    out = []
    for i, stage in enumerate(C.RHYTHM, start=1):
        items = "".join(f"<li>{it}</li>" for it in stage["items"])
        lead = f'<p class="rlead">{stage["lead"]}</p>' if stage.get("lead") else ""
        note = f'<p class="rnote">{stage["note"]}</p>' if stage.get("note") else ""
        out.append(f'''
        <div class="stage reveal">
          <div class="stage-mark">{i:02d}</div>
          <h3>{stage["name"]}</h3>
          {lead}
          <ul class="rlist">{items}</ul>
          {note}
          <p class="result"><span>Result</span>{stage["result"]}</p>
        </div>''')
    return "".join(out)

def branch_leaves():
    out = []
    for ed in C.ONE_MESSAGE_EDITIONS:
        out.append(f'<div class="leaf reveal">{ed}</div>')
    return "".join(out)

def edition_entries():
    out = []
    for name, desc, sub in C.EDITIONS:
        sub_html = ""
        if sub:
            sub_html = '<ul class="sub-list">' + "".join(f"<li>{s}</li>" for s in sub) + "</ul>"
        out.append(f'''
        <div class="edition reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
          {sub_html}
        </div>''')
    return "".join(out)

def experience_rungs():
    out = []
    for exp in C.EXPERIENCES:
        fits = "".join(f"<li>{f}</li>" for f in exp["fits"])
        flow_html = ""
        if exp.get("flow"):
            flow_html = '<div class="flow">' + "".join(f'<span>{s}</span>' for s in exp["flow"]) + '</div>'
        flow_note = f'<p class="flow-note">{exp["flow_note"]}</p>' if exp.get("flow_note") else ""
        out.append(f'''
        <div class="rung reveal">
          <div class="rung-length">{exp["length"]}</div>
          <div class="rung-body">
            <h3>{exp["name"]}</h3>
            <p class="tag">{exp["tag"]}</p>
            <ul class="fits">{fits}</ul>
            {flow_html}
            {flow_note}
          </div>
        </div>''')
    return "".join(out)

def product_entries():
    out = []
    for name, desc, items in C.PRODUCTS:
        items_html = '<ul class="sub-list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>" if items else ""
        out.append(f'''
        <div class="product reveal">
          <h4>{name}</h4>
          <p>{desc}</p>
          {items_html}
        </div>''')
    return "".join(out)

def customization_entries():
    out = []
    for i, (name, desc, items) in enumerate(C.CUSTOMIZATION, start=1):
        items_html = '<ul class="sub-list">' + "".join(f"<li>{it}</li>" for it in items) + "</ul>" if items else ""
        out.append(f'''
        <div class="tier reveal">
          <div class="tier-num">{i:02d}</div>
          <div class="tier-body">
            <h4>{name}</h4>
            <p>{desc}</p>
            {items_html}
          </div>
        </div>''')
    return "".join(out)

def pod_items():
    return "".join(f"<li>{i}</li>" for i in C.POD["items"])

def finder_facets():
    return "".join(f'<span class="facet">{f}</span>' for f in C.FINDER["facets"])

def difference_pairs():
    out = []
    for a, b in C.DIFFERENCE_PAIRS:
        out.append(f'<div class="pair reveal"><span class="from">{a}</span><span class="arrow">\u2192</span><span class="to">{b}</span></div>')
    return "".join(out)

def imagine_lines():
    out = []
    for line in C.IMAGINE_CHAIN:
        out.append(f'<p class="imagine-line reveal">{line}</p>')
    return "".join(out)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Whole-Church Formation\u2122 | LifeTogether</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,900;1,500;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>
  :root {{
    --navy-950: #070B15;
    --navy-900: #0D1526;
    --navy-800: #131F38;
    --navy-700: #1A2A48;
    --gold: #C9A24C;
    --gold-soft: #E6CD8C;
    --gold-dim: #8B7538;
    --parchment: #EDE7D6;
    --parchment-dim: #B9B4A2;
    --ink-dim: #8791A8;
    --hairline: rgba(201,162,76,0.28);
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{
    background: var(--navy-950);
    color: var(--parchment);
    font-family: 'Lato', sans-serif;
    font-weight:300;
    line-height:1.7;
    -webkit-font-smoothing:antialiased;
  }}
  .wrap {{ max-width:920px; margin:0 auto; padding:0 32px; }}
  h1,h2,h3,h4 {{ font-family:'Playfair Display', serif; font-weight:600; color:var(--parchment); }}
  .eyebrow {{
    font-family:'Cormorant Garamond', serif;
    font-style:italic;
    font-size:1.15rem;
    color:var(--gold-soft);
    letter-spacing:0.04em;
    margin-bottom:14px;
  }}
  .rule {{ border:none; border-top:1px solid var(--hairline); margin:0; }}
  section {{ padding:96px 0; position:relative; }}
  .reveal {{ opacity:0; transform:translateY(18px); transition:opacity .8s ease, transform .8s ease; }}
  .reveal.in {{ opacity:1; transform:translateY(0); }}

  /* HERO */
  .hero {{
    min-height:100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:80px 32px;
    background:
      radial-gradient(ellipse at 50% -10%, rgba(201,162,76,0.10), transparent 60%),
      var(--navy-950);
    position:relative;
    overflow:hidden;
  }}
  .hero::before {{
    content:"";
    position:absolute; inset:0;
    background-image:
      linear-gradient(var(--hairline) 1px, transparent 1px),
      linear-gradient(90deg, var(--hairline) 1px, transparent 1px);
    background-size:120px 120px;
    opacity:0.12;
    mask-image: radial-gradient(ellipse at center, black, transparent 75%);
  }}
  .hero-eyebrow {{
    font-family:'Cormorant Garamond', serif;
    font-style:italic;
    color:var(--gold-soft);
    font-size:1.3rem;
    letter-spacing:0.08em;
    margin-bottom:28px;
    position:relative;
  }}
  .hero h1 {{
    font-size:clamp(2.8rem, 7vw, 5.6rem);
    line-height:1.05;
    font-weight:700;
    max-width:900px;
    position:relative;
    background:linear-gradient(180deg, var(--parchment) 0%, var(--gold-soft) 100%);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
  }}
  .hero-kicker {{
    margin-top:26px;
    font-family:'Cormorant Garamond', serif;
    font-size:1.6rem;
    font-style:italic;
    color:var(--parchment-dim);
    position:relative;
  }}
  .hero-sub {{
    margin-top:22px;
    font-family:'Lato', sans-serif;
    letter-spacing:0.18em;
    text-transform:uppercase;
    font-size:0.78rem;
    color:var(--gold-dim);
    position:relative;
  }}
  .hero-rule {{
    width:64px; height:1px; background:var(--gold);
    margin:38px auto 0; position:relative;
  }}

  /* OPENING */
  .opening .lead p {{ font-size:1.15rem; color:var(--parchment-dim); max-width:640px; margin-bottom:14px; }}
  .opening .question {{
    font-family:'Playfair Display', serif;
    font-style:italic;
    font-size:clamp(1.5rem,3vw,2.1rem);
    color:var(--gold-soft);
    max-width:760px;
    margin:44px 0;
    line-height:1.4;
  }}
  .frag-list {{
    display:flex; flex-wrap:wrap; gap:10px 14px;
    margin:36px 0;
    padding:28px 0;
    border-top:1px solid var(--hairline);
    border-bottom:1px solid var(--hairline);
  }}
  .frag-list span {{
    font-family:'Cormorant Garamond', serif;
    font-style:italic;
    font-size:1.15rem;
    color:var(--ink-dim);
  }}
  .frag-list span:not(:last-child)::after {{ content:"\\2014"; margin-left:14px; color:var(--gold-dim); }}
  .opening .result p {{ font-size:1.15rem; color:var(--parchment-dim); max-width:640px; margin-bottom:6px; }}
  .opening .result p.punch {{ color:var(--gold-soft); font-family:'Playfair Display', serif; font-style:italic; font-size:1.35rem; margin-top:10px; }}

  /* WHAT IS */
  .what-is h2 {{ font-size:clamp(1.9rem,4vw,2.7rem); margin-bottom:26px; max-width:680px; }}
  .what-is p {{ color:var(--parchment-dim); max-width:640px; margin-bottom:14px; font-size:1.08rem; }}
  .reframe {{ margin-top:40px; display:grid; grid-template-columns:1fr auto 1fr; gap:24px; align-items:center; max-width:760px; }}
  .reframe .box {{ border:1px solid var(--hairline); padding:22px 24px; }}
  .reframe .box.no {{ opacity:0.55; }}
  .reframe .box p {{ font-family:'Cormorant Garamond', serif; font-style:italic; font-size:1.2rem; color:var(--parchment); margin:0; }}
  .reframe .arrow {{ color:var(--gold); font-size:1.4rem; text-align:center; }}
  @media (max-width:640px) {{ .reframe {{ grid-template-columns:1fr; }} .reframe .arrow {{ transform:rotate(90deg); }} }}

  /* SECTION HEAD generic */
  .section-head {{ max-width:680px; margin-bottom:52px; }}
  .section-head h2 {{ font-size:clamp(1.9rem,4vw,2.6rem); margin-bottom:16px; }}
  .section-head p {{ color:var(--parchment-dim); font-size:1.05rem; }}

  /* ENVIRONMENTS directory */
  .env-row {{
    display:grid; grid-template-columns:80px 1fr; gap:28px;
    padding:30px 0; border-top:1px solid var(--hairline);
  }}
  .env-row:last-child {{ border-bottom:1px solid var(--hairline); }}
  .env-num {{
    font-family:'Playfair Display', serif; font-style:italic;
    font-size:2rem; color:var(--gold); line-height:1;
  }}
  .env-body h3 {{ font-size:1.35rem; margin-bottom:8px; }}
  .env-body p {{ color:var(--parchment-dim); font-size:1rem; max-width:560px; }}

  /* OUTCOMES band */
  .outcomes-band {{ display:grid; grid-template-columns:repeat(5,1fr); gap:0; }}
  .outcome {{ padding:0 20px; border-left:1px solid var(--hairline); }}
  .outcome:first-child {{ border-left:none; padding-left:0; }}
  .outcome h4 {{ font-size:1.15rem; color:var(--gold-soft); margin-bottom:10px; }}
  .outcome p {{ font-size:0.92rem; color:var(--parchment-dim); }}
  @media (max-width:800px) {{
    .outcomes-band {{ grid-template-columns:1fr 1fr; gap:28px 24px; }}
    .outcome {{ border-left:none; padding-left:0; border-top:1px solid var(--hairline); padding-top:20px; }}
  }}

  /* RHYTHM — the formation spine */
  .rhythm-title {{ font-size:clamp(2rem,4.5vw,3rem); text-align:center; max-width:820px; margin:0 auto 12px; }}
  .rhythm-sub {{ text-align:center; color:var(--parchment-dim); margin-bottom:80px; }}
  .spine {{ position:relative; padding-left:48px; }}
  .spine::before {{
    content:""; position:absolute; left:11px; top:8px; bottom:8px; width:1px;
    background:linear-gradient(var(--gold-dim), var(--gold), var(--gold-dim));
  }}
  .stage {{ position:relative; margin-bottom:64px; }}
  .stage:last-child {{ margin-bottom:0; }}
  .stage-mark {{
    position:absolute; left:-48px; top:0; width:24px; height:24px;
    border:1px solid var(--gold); border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-family:'Lato'; font-size:0.65rem; color:var(--gold-soft);
    background:var(--navy-950);
  }}
  .stage h3 {{ font-size:1.6rem; margin-bottom:14px; }}
  .rlead {{ color:var(--parchment-dim); margin-bottom:14px; }}
  .rlist {{ list-style:none; display:flex; flex-wrap:wrap; gap:8px 12px; margin-bottom:16px; }}
  .rlist li {{
    font-size:0.88rem; color:var(--parchment); border:1px solid var(--hairline);
    padding:6px 14px; border-radius:2px;
  }}
  .rnote {{ color:var(--parchment-dim); font-style:italic; margin-bottom:14px; }}
  .result {{ font-family:'Playfair Display', serif; font-style:italic; color:var(--gold-soft); font-size:1.1rem; }}
  .result span {{
    display:block; font-family:'Lato'; font-style:normal; text-transform:uppercase;
    letter-spacing:0.14em; font-size:0.7rem; color:var(--gold-dim); margin-bottom:6px;
  }}

  /* ONE MESSAGE branching */
  .one-message .example {{
    font-family:'Playfair Display', serif; font-size:clamp(1.8rem,4vw,2.6rem);
    color:var(--gold-soft); margin-bottom:12px;
  }}
  .one-message .example-label {{ font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--gold-dim); margin-bottom:14px; }}
  .branch {{ position:relative; margin-top:56px; padding-top:40px; }}
  .branch::before {{
    content:""; position:absolute; top:0; left:0; right:0; height:1px; background:var(--hairline);
  }}
  .branch::after {{
    content:""; position:absolute; top:-20px; left:50%; width:1px; height:20px; background:var(--gold-dim);
  }}
  .leaves {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:2px; }}
  .leaf {{
    border:1px solid var(--hairline); padding:18px 16px; font-size:0.92rem;
    color:var(--parchment); position:relative; text-align:center;
  }}
  .leaf::before {{
    content:""; position:absolute; top:-20px; left:50%; width:1px; height:20px; background:var(--hairline);
  }}
  .one-message-close {{ margin-top:44px; text-align:center; }}
  .one-message-close p {{ font-family:'Cormorant Garamond', serif; font-style:italic; font-size:1.3rem; color:var(--parchment-dim); }}
  .one-message-close p:last-child {{ color:var(--gold-soft); }}

  /* MULTI-EDITION */
  .multi-lead p {{ color:var(--parchment-dim); font-size:1.08rem; margin-bottom:8px; max-width:600px; }}
  .multi-lead p:last-child {{ color:var(--gold-soft); font-family:'Playfair Display', serif; font-style:italic; font-size:1.3rem; margin-top:14px; }}
  .editions-grid {{ margin-top:56px; display:grid; grid-template-columns:1fr 1fr; gap:2px; }}
  .edition {{ border-top:1px solid var(--hairline); padding:28px 28px 28px 0; }}
  .edition:nth-child(odd) {{ padding-right:28px; border-right:1px solid var(--hairline); }}
  .edition:nth-child(even) {{ padding-left:28px; }}
  .edition h4 {{ font-size:1.2rem; margin-bottom:8px; color:var(--gold-soft); }}
  .edition p {{ color:var(--parchment-dim); font-size:0.96rem; }}
  .sub-list {{ list-style:none; margin-top:10px; }}
  .sub-list li {{ font-size:0.88rem; color:var(--parchment-dim); padding:3px 0; }}
  .sub-list li::before {{ content:"\\2014  "; color:var(--gold-dim); }}
  @media (max-width:700px) {{
    .editions-grid {{ grid-template-columns:1fr; }}
    .edition:nth-child(odd) {{ border-right:none; padding-right:0; }}
    .edition:nth-child(even) {{ padding-left:0; }}
  }}

  /* EXPERIENCE LADDER */
  .ladder {{ margin-top:20px; }}
  .rung {{ display:grid; grid-template-columns:120px 1fr; gap:32px; padding:36px 0; border-top:1px solid var(--hairline); }}
  .rung:last-child {{ border-bottom:1px solid var(--hairline); }}
  .rung-length {{
    font-family:'Playfair Display', serif; font-style:italic; color:var(--gold);
    font-size:1.3rem; padding-top:4px;
  }}
  .rung h3 {{ font-size:1.5rem; margin-bottom:6px; }}
  .tag {{ color:var(--parchment-dim); font-style:italic; font-family:'Cormorant Garamond', serif; font-size:1.15rem; margin-bottom:16px; }}
  .fits {{ list-style:none; display:flex; flex-wrap:wrap; gap:8px 10px; margin-bottom:14px; }}
  .fits li {{ font-size:0.85rem; color:var(--parchment); border:1px solid var(--hairline); padding:5px 12px; }}
  .flow {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin:14px 0 8px; }}
  .flow span {{ font-size:0.85rem; color:var(--gold-soft); }}
  .flow span:not(:last-child)::after {{ content:"\\2192"; margin-left:10px; color:var(--gold-dim); }}
  .flow-note {{ font-style:italic; color:var(--parchment-dim); font-size:0.92rem; }}
  @media (max-width:640px) {{ .rung {{ grid-template-columns:1fr; gap:10px; }} }}

  /* MORE THAN CURRICULUM */
  .mtc p {{ font-size:1.3rem; color:var(--parchment-dim); font-family:'Cormorant Garamond', serif; font-style:italic; margin-bottom:6px; }}
  .mtc p:last-child {{ color:var(--gold-soft); font-family:'Playfair Display', serif; font-size:1.5rem; margin-top:16px; }}

  /* PRODUCTS */
  .products-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:2px; margin-top:20px; }}
  .product {{ border:1px solid var(--hairline); padding:32px; }}
  .product h4 {{ font-size:1.3rem; margin-bottom:12px; color:var(--gold-soft); }}
  .product p {{ color:var(--parchment-dim); margin-bottom:10px; }}
  .products-note {{ margin-top:28px; font-style:italic; color:var(--parchment-dim); font-family:'Cormorant Garamond', serif; font-size:1.15rem; }}
  @media (max-width:700px) {{ .products-grid {{ grid-template-columns:1fr; }} }}

  /* CUSTOMIZATION TIERS */
  .tier {{ display:grid; grid-template-columns:60px 1fr; gap:24px; padding:30px 0; border-top:1px solid var(--hairline); }}
  .tier:last-child {{ border-bottom:1px solid var(--hairline); }}
  .tier-num {{ font-family:'Playfair Display', serif; font-style:italic; color:var(--gold); font-size:1.6rem; }}
  .tier-body h4 {{ font-size:1.3rem; margin-bottom:8px; }}
  .tier-body p {{ color:var(--parchment-dim); }}

  /* POD */
  .pod-lead {{ color:var(--parchment-dim); font-size:1.1rem; margin-bottom:24px; max-width:600px; }}
  .pod-items {{ list-style:none; margin-bottom:28px; }}
  .pod-items li {{ font-size:1rem; color:var(--parchment); padding:8px 0; border-top:1px solid var(--hairline); }}
  .pod-close {{ display:flex; gap:24px; }}
  .pod-close span {{ font-family:'Playfair Display', serif; font-style:italic; color:var(--gold-soft); font-size:1.2rem; }}

  /* FINDER */
  .finder-lead {{ font-family:'Playfair Display', serif; font-style:italic; font-size:1.4rem; color:var(--gold-soft); margin-bottom:20px; max-width:600px; }}
  .finder-body {{ color:var(--parchment-dim); margin-bottom:24px; }}
  .facets {{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:32px; }}
  .facet {{ border:1px solid var(--gold-dim); color:var(--gold-soft); font-size:0.85rem; padding:8px 18px; }}
  .finder-close {{ display:flex; gap:20px; flex-wrap:wrap; color:var(--parchment-dim); font-style:italic; font-family:'Cormorant Garamond', serif; font-size:1.1rem; }}

  /* DIFFERENCE */
  .difference-lead p {{ color:var(--parchment-dim); font-size:1.1rem; max-width:600px; margin-bottom:8px; }}
  .pairs {{ margin-top:44px; display:grid; grid-template-columns:1fr 1fr; gap:14px 40px; }}
  .pair {{ display:flex; align-items:baseline; gap:14px; padding:14px 0; border-top:1px solid var(--hairline); }}
  .pair .from {{ color:var(--ink-dim); font-size:0.98rem; min-width:150px; }}
  .pair .arrow {{ color:var(--gold-dim); }}
  .pair .to {{ color:var(--gold-soft); font-family:'Playfair Display', serif; font-style:italic; font-size:1.05rem; }}
  @media (max-width:700px) {{ .pairs {{ grid-template-columns:1fr; }} }}

  /* IMAGINE */
  .imagine {{ text-align:center; }}
  .imagine-line {{ font-family:'Playfair Display', serif; font-style:italic; font-size:clamp(1.2rem,3vw,1.7rem); color:var(--parchment-dim); margin-bottom:18px; }}
  .imagine-line:last-child {{ color:var(--gold-soft); font-weight:600; }}
  .imagine-final {{ margin-top:50px; font-family:'Playfair Display', serif; font-size:clamp(1.8rem,4vw,2.6rem); color:var(--gold); }}

  /* FOOTER */
  footer {{ background:var(--navy-900); padding:100px 0 60px; text-align:center; border-top:1px solid var(--hairline); }}
  .foot-block {{ margin-bottom:44px; }}
  .foot-block h3 {{ font-size:1.6rem; color:var(--gold-soft); margin-bottom:8px; }}
  .foot-block p {{ color:var(--parchment-dim); font-size:0.98rem; }}
  .foot-rhythm {{ margin-top:60px; font-family:'Cormorant Garamond', serif; font-style:italic; font-size:1.3rem; color:var(--parchment-dim); }}
  .foot-fine {{ margin-top:40px; font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--ink-dim); }}

  h2.title-lg {{ font-size:clamp(2rem,4.5vw,3rem); }}
</style>
</head>
<body>

<section class="hero">
  <div class="hero-eyebrow">LifeTogether Church Formation System\u2122</div>
  <h1>{C.TITLE}</h1>
  <p class="hero-kicker">{C.KICKER}</p>
  <div class="hero-rule"></div>
  <p class="hero-sub">{C.SUBHEAD}</p>
</section>

<hr class="rule">

<section class="opening">
  <div class="wrap">
    <div class="eyebrow">Every Church Has a Mission</div>
    <h2 style="font-size:clamp(1.9rem,4vw,2.6rem); max-width:700px; margin-bottom:30px;">Few Have a Comprehensive Formation Strategy.</h2>
    <div class="lead">
      {"".join(f"<p>{p}</p>" for p in C.OPENING_LEAD)}
    </div>
    <p class="question">{C.OPENING_QUESTION}</p>
    <div class="frag-list">
      {"".join(f"<span>{m}</span>" for m in C.FRAGMENTED_MINISTRIES)}
    </div>
    <div class="result">
      {"".join(f'<p class="punch">{p}</p>' if i == len(C.OPENING_RESULT)-1 else f"<p>{p}</p>" for i,p in enumerate(C.OPENING_RESULT))}
    </div>
  </div>
</section>

<hr class="rule">

<section class="what-is">
  <div class="wrap">
    <div class="eyebrow">{C.WHAT_IS['eyebrow']}</div>
    <h2>{C.WHAT_IS['title']}</h2>
    {"".join(f"<p>{p}</p>" for p in C.WHAT_IS['body'])}
    <div class="reframe">
      <div class="box no"><p>{C.WHAT_IS['reframe_from']}</p></div>
      <div class="arrow">\u2192</div>
      <div class="box"><p>{C.WHAT_IS['reframe_to']}</p></div>
    </div>
  </div>
</section>

<hr class="rule">

<section class="environments">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">A Churchwide Formation Strategy</div>
      <h2>Every Major Environment of Church Life</h2>
      <p>Whole-Church Formation\u2122 connects seven environments into a single, shared discipleship process.</p>
    </div>
    <div class="env-list">
      {env_rows()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="outcomes">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Five Desired Outcomes</div>
      <h2>What Everything Is Designed to Cultivate</h2>
    </div>
    <div class="outcomes-band">
      {outcome_cols()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="rhythm">
  <div class="wrap">
    <h2 class="rhythm-title">{C.RHYTHM_INTRO}</h2>
    <p class="rhythm-sub">{C.RHYTHM_SUB}</p>
    <div class="spine">
      {rhythm_blocks()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="one-message">
  <div class="wrap">
    <div class="eyebrow">One Message. Multiple Experiences.</div>
    <h2 style="max-width:700px; margin-bottom:36px;">Every biblical theme can become a complete family of synchronized experiences.</h2>
    <p class="example-label">For Example</p>
    <p class="example">{C.ONE_MESSAGE_EXAMPLE}</p>
    <p style="color:var(--parchment-dim);">Available automatically as:</p>
    <div class="branch">
      <div class="leaves">
        {branch_leaves()}
      </div>
    </div>
    <div class="one-message-close">
      {"".join(f"<p>{p}</p>" for p in C.ONE_MESSAGE_CLOSE)}
    </div>
  </div>
</section>

<hr class="rule">

<section class="multi-edition">
  <div class="wrap">
    <div class="eyebrow">The Multi-Edition Difference</div>
    <h2 class="title-lg" style="max-width:640px;">This Is What Makes LifeTogether Fundamentally Different</h2>
    <div class="multi-lead" style="margin-top:26px;">
      {"".join(f"<p>{p}</p>" for p in C.MULTI_EDITION_LEAD)}
    </div>
    <div class="editions-grid">
      {edition_entries()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="experiences">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Choose the Right Experience</div>
      <h2>Not Every Church Needs the Same Level of Engagement</h2>
      <p>LifeTogether offers experiences designed for every season\u2014from a single Sunday to a full forty-day churchwide journey.</p>
    </div>
    <div class="ladder">
      {experience_rungs()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="mtc">
  <div class="wrap">
    {"".join(f"<p>{p}</p>" for p in C.MORE_THAN_CURRICULUM)}
  </div>
</section>

<hr class="rule">

<section class="products">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Two Products. One Unified Experience.</div>
      <h2>Every Experience Can Include</h2>
    </div>
    <div class="products-grid">
      {product_entries()}
    </div>
    <p class="products-note">{C.PRODUCTS_NOTE}</p>
  </div>
</section>

<hr class="rule">

<section class="customization">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Built Around Your Church</div>
      <h2>Choose from Multiple Customization Levels</h2>
    </div>
    {customization_entries()}
  </div>
</section>

<hr class="rule">

<section class="pod">
  <div class="wrap">
    <div class="eyebrow">Print-on-Demand Publishing</div>
    <h2 style="margin-bottom:20px;">{C.POD['title']}</h2>
    <p class="pod-lead">{C.POD['lead']}</p>
    <ul class="pod-items">
      {pod_items()}
    </ul>
    <div class="pod-close">
      {"".join(f"<span>{p}</span>" for p in C.POD['close'])}
    </div>
  </div>
</section>

<hr class="rule">

<section class="finder">
  <div class="wrap">
    <div class="eyebrow">{C.FINDER['title']}</div>
    <p class="finder-lead">{C.FINDER['lead']}</p>
    <p class="finder-body">{C.FINDER['body']}</p>
    <div class="facets">
      {finder_facets()}
    </div>
    <div class="finder-close">
      {"".join(f"<span>{c}</span>" for c in C.FINDER['close'])}
    </div>
  </div>
</section>

<hr class="rule">

<section class="difference">
  <div class="wrap">
    <div class="eyebrow">The LifeTogether Difference</div>
    <div class="difference-lead">
      {"".join(f"<p>{p}</p>" for p in C.DIFFERENCE_LEAD)}
    </div>
    <div class="pairs">
      {difference_pairs()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="imagine">
  <div class="wrap">
    <div class="eyebrow" style="text-align:center;">Imagine What's Possible</div>
    {imagine_lines()}
    <p class="imagine-final">That\u2019s Whole-Church Formation\u2122.</p>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-block">
      <h3>{C.FOOTER['system']}</h3>
      <p>{C.FOOTER['system_sub']}</p>
    </div>
    <div class="foot-block">
      <h3>{C.FOOTER['wcf']}</h3>
      <p>{C.FOOTER['wcf_sub']}</p>
    </div>
    <div class="foot-block">
      <h3>{C.FOOTER['experiences']}</h3>
      <p>{C.FOOTER['experiences_sub']}</p>
    </div>
    <p class="foot-rhythm">{C.FOOTER['rhythm']}</p>
    <p class="foot-fine">LifeTogether Ministries \u2014 New Edition Brochure</p>
  </div>
</footer>

<script>
  const els = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {{
    entries.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }});
  }}, {{ threshold: 0.08 }});
  els.forEach(el => io.observe(el));
</script>

</body>
</html>
"""

with open("/mnt/user-data/outputs/whole-church-formation-new-edition.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("done", len(HTML))
