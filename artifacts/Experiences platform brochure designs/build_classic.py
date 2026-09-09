# -*- coding: utf-8 -*-
import content as C
from components import (env_rows, outcome_cols, rhythm_blocks, branch_leaves,
    edition_entries, experience_rungs, product_entries, customization_entries,
    pod_items, finder_facets, difference_pairs, imagine_lines)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Whole-Church Formation\u2122 | LifeTogether</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --paper: #F4F1E7;
    --paper-deep: #EAE5D3;
    --moss-deep: #2F5B3E;
    --moss-900: #1F3C29;
    --moss-tint: #E4E8DD;
    --brass: #A8853C;
    --brass-light: #C7A45E;
    --ink: #23281F;
    --ink-dim: #5B6155;
    --hairline: rgba(47,91,62,0.22);
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{
    background: var(--paper);
    color: var(--ink);
    font-family:'Inter', sans-serif;
    font-weight:300;
    line-height:1.7;
    -webkit-font-smoothing:antialiased;
  }}
  .wrap {{ max-width:920px; margin:0 auto; padding:0 32px; }}
  h1,h2,h3,h4 {{ font-family:'Fraunces', serif; font-weight:600; color:var(--moss-900); }}
  .eyebrow {{
    font-family:'Fraunces', serif;
    font-style:italic;
    font-weight:500;
    font-size:1.1rem;
    color:var(--brass);
    letter-spacing:0.02em;
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
      radial-gradient(ellipse at 50% -10%, rgba(168,133,60,0.10), transparent 60%),
      var(--paper);
    position:relative;
    overflow:hidden;
    border-bottom:1px solid var(--hairline);
  }}
  .hero::before {{
    content:"";
    position:absolute; inset:36px;
    border:1px solid var(--hairline);
    pointer-events:none;
  }}
  .hero-eyebrow {{
    font-family:'Fraunces', serif;
    font-style:italic;
    font-weight:500;
    color:var(--brass);
    font-size:1.25rem;
    letter-spacing:0.03em;
    margin-bottom:28px;
  }}
  .hero h1 {{
    font-size:clamp(2.6rem, 6.6vw, 5.2rem);
    line-height:1.08;
    font-weight:600;
    max-width:900px;
    color:var(--moss-900);
  }}
  .hero-kicker {{
    margin-top:26px;
    font-family:'Fraunces', serif;
    font-style:italic;
    font-weight:500;
    font-size:1.5rem;
    color:var(--moss-deep);
  }}
  .hero-sub {{
    margin-top:22px;
    letter-spacing:0.16em;
    text-transform:uppercase;
    font-size:0.75rem;
    color:var(--brass);
    font-weight:600;
  }}
  .hero-rule {{ width:56px; height:2px; background:var(--brass); margin:38px auto 0; }}

  /* OPENING */
  .opening .lead p {{ font-size:1.15rem; color:var(--ink-dim); max-width:640px; margin-bottom:14px; }}
  .opening .question {{
    font-family:'Fraunces', serif;
    font-style:italic;
    font-weight:500;
    font-size:clamp(1.5rem,3vw,2.1rem);
    color:var(--moss-deep);
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
  .frag-list span {{ font-family:'Fraunces', serif; font-style:italic; font-size:1.1rem; color:var(--ink-dim); }}
  .frag-list span:not(:last-child)::after {{ content:"\\2014"; margin-left:14px; color:var(--brass); }}
  .opening .result p {{ font-size:1.15rem; color:var(--ink-dim); max-width:640px; margin-bottom:6px; }}
  .opening .result p.punch {{ color:var(--moss-deep); font-family:'Fraunces', serif; font-style:italic; font-size:1.35rem; margin-top:10px; }}

  /* WHAT IS */
  .what-is h2 {{ font-size:clamp(1.9rem,4vw,2.7rem); margin-bottom:26px; max-width:680px; }}
  .what-is p {{ color:var(--ink-dim); max-width:640px; margin-bottom:14px; font-size:1.08rem; }}
  .reframe {{ margin-top:40px; display:grid; grid-template-columns:1fr auto 1fr; gap:24px; align-items:center; max-width:760px; }}
  .reframe .box {{ border:1px solid var(--hairline); padding:22px 24px; background:var(--paper-deep); }}
  .reframe .box.no {{ opacity:0.6; background:transparent; }}
  .reframe .box p {{ font-family:'Fraunces', serif; font-style:italic; font-size:1.15rem; color:var(--ink); margin:0; }}
  .reframe .arrow {{ color:var(--brass); font-size:1.4rem; text-align:center; }}
  @media (max-width:640px) {{ .reframe {{ grid-template-columns:1fr; }} .reframe .arrow {{ transform:rotate(90deg); }} }}

  .section-head {{ max-width:680px; margin-bottom:52px; }}
  .section-head h2 {{ font-size:clamp(1.9rem,4vw,2.6rem); margin-bottom:16px; }}
  .section-head p {{ color:var(--ink-dim); font-size:1.05rem; }}

  /* ENVIRONMENTS directory */
  .env-row {{ display:grid; grid-template-columns:80px 1fr; gap:28px; padding:30px 0; border-top:1px solid var(--hairline); }}
  .env-row:last-child {{ border-bottom:1px solid var(--hairline); }}
  .env-num {{ font-family:'Fraunces', serif; font-style:italic; font-size:1.9rem; color:var(--brass); line-height:1; }}
  .env-body h3 {{ font-size:1.35rem; margin-bottom:8px; }}
  .env-body p {{ color:var(--ink-dim); font-size:1rem; max-width:560px; }}

  /* OUTCOMES */
  .outcomes-band {{ display:grid; grid-template-columns:repeat(5,1fr); gap:0; }}
  .outcome {{ padding:0 20px; border-left:1px solid var(--hairline); }}
  .outcome:first-child {{ border-left:none; padding-left:0; }}
  .outcome h4 {{ font-size:1.1rem; color:var(--moss-deep); margin-bottom:10px; }}
  .outcome p {{ font-size:0.92rem; color:var(--ink-dim); }}
  @media (max-width:800px) {{
    .outcomes-band {{ grid-template-columns:1fr 1fr; gap:28px 24px; }}
    .outcome {{ border-left:none; padding-left:0; border-top:1px solid var(--hairline); padding-top:20px; }}
  }}

  /* RHYTHM spine */
  .rhythm-title {{ font-size:clamp(2rem,4.5vw,3rem); text-align:center; max-width:820px; margin:0 auto 12px; }}
  .rhythm-sub {{ text-align:center; color:var(--ink-dim); margin-bottom:80px; }}
  .spine {{ position:relative; padding-left:48px; }}
  .spine::before {{ content:""; position:absolute; left:11px; top:8px; bottom:8px; width:1px; background:linear-gradient(var(--brass-light), var(--moss-deep), var(--brass-light)); }}
  .stage {{ position:relative; margin-bottom:64px; }}
  .stage:last-child {{ margin-bottom:0; }}
  .stage-mark {{
    position:absolute; left:-48px; top:0; width:24px; height:24px;
    border:1px solid var(--brass); border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-family:'Inter'; font-size:0.65rem; color:var(--moss-deep);
    background:var(--paper);
  }}
  .stage h3 {{ font-size:1.6rem; margin-bottom:14px; }}
  .rlead {{ color:var(--ink-dim); margin-bottom:14px; }}
  .rlist {{ list-style:none; display:flex; flex-wrap:wrap; gap:8px 12px; margin-bottom:16px; }}
  .rlist li {{ font-size:0.88rem; color:var(--ink); border:1px solid var(--hairline); padding:6px 14px; border-radius:2px; background:var(--paper-deep); }}
  .rnote {{ color:var(--ink-dim); font-style:italic; margin-bottom:14px; }}
  .result {{ font-family:'Fraunces', serif; font-style:italic; color:var(--moss-deep); font-size:1.1rem; }}
  .result span {{ display:block; font-family:'Inter'; font-style:normal; text-transform:uppercase; letter-spacing:0.14em; font-size:0.7rem; color:var(--brass); margin-bottom:6px; }}

  /* ONE MESSAGE branching */
  .one-message .example {{ font-family:'Fraunces', serif; font-size:clamp(1.8rem,4vw,2.6rem); color:var(--moss-deep); margin-bottom:12px; }}
  .one-message .example-label {{ font-size:0.78rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--brass); margin-bottom:14px; font-weight:600; }}
  .branch {{ position:relative; margin-top:56px; padding-top:40px; }}
  .branch::before {{ content:""; position:absolute; top:0; left:0; right:0; height:1px; background:var(--hairline); }}
  .branch::after {{ content:""; position:absolute; top:-20px; left:50%; width:1px; height:20px; background:var(--brass); }}
  .leaves {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:2px; }}
  .leaf {{ border:1px solid var(--hairline); padding:18px 16px; font-size:0.92rem; color:var(--ink); position:relative; text-align:center; background:var(--paper-deep); }}
  .leaf::before {{ content:""; position:absolute; top:-20px; left:50%; width:1px; height:20px; background:var(--hairline); }}
  .one-message-close {{ margin-top:44px; text-align:center; }}
  .one-message-close p {{ font-family:'Fraunces', serif; font-style:italic; font-size:1.3rem; color:var(--ink-dim); }}
  .one-message-close p:last-child {{ color:var(--moss-deep); }}

  /* MULTI-EDITION */
  .multi-lead p {{ color:var(--ink-dim); font-size:1.08rem; margin-bottom:8px; max-width:600px; }}
  .multi-lead p:last-child {{ color:var(--moss-deep); font-family:'Fraunces', serif; font-style:italic; font-size:1.3rem; margin-top:14px; }}
  .editions-grid {{ margin-top:56px; display:grid; grid-template-columns:1fr 1fr; gap:2px; }}
  .edition {{ border-top:1px solid var(--hairline); padding:28px 28px 28px 0; }}
  .edition:nth-child(odd) {{ padding-right:28px; border-right:1px solid var(--hairline); }}
  .edition:nth-child(even) {{ padding-left:28px; }}
  .edition h4 {{ font-size:1.2rem; margin-bottom:8px; color:var(--moss-deep); }}
  .edition p {{ color:var(--ink-dim); font-size:0.96rem; }}
  .sub-list {{ list-style:none; margin-top:10px; }}
  .sub-list li {{ font-size:0.88rem; color:var(--ink-dim); padding:3px 0; }}
  .sub-list li::before {{ content:"\\2014  "; color:var(--brass); }}
  @media (max-width:700px) {{
    .editions-grid {{ grid-template-columns:1fr; }}
    .edition:nth-child(odd) {{ border-right:none; padding-right:0; }}
    .edition:nth-child(even) {{ padding-left:0; }}
  }}

  /* EXPERIENCE LADDER */
  .ladder {{ margin-top:20px; }}
  .rung {{ display:grid; grid-template-columns:120px 1fr; gap:32px; padding:36px 0; border-top:1px solid var(--hairline); }}
  .rung:last-child {{ border-bottom:1px solid var(--hairline); }}
  .rung-length {{ font-family:'Fraunces', serif; font-style:italic; color:var(--brass); font-size:1.25rem; padding-top:4px; }}
  .rung h3 {{ font-size:1.5rem; margin-bottom:6px; }}
  .tag {{ color:var(--ink-dim); font-style:italic; font-family:'Fraunces', serif; font-size:1.1rem; margin-bottom:16px; }}
  .fits {{ list-style:none; display:flex; flex-wrap:wrap; gap:8px 10px; margin-bottom:14px; }}
  .fits li {{ font-size:0.85rem; color:var(--ink); border:1px solid var(--hairline); padding:5px 12px; background:var(--paper-deep); }}
  .flow {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin:14px 0 8px; }}
  .flow span {{ font-size:0.85rem; color:var(--moss-deep); font-weight:500; }}
  .flow span:not(:last-child)::after {{ content:"\\2192"; margin-left:10px; color:var(--brass); }}
  .flow-note {{ font-style:italic; color:var(--ink-dim); font-size:0.92rem; }}
  @media (max-width:640px) {{ .rung {{ grid-template-columns:1fr; gap:10px; }} }}

  /* MORE THAN CURRICULUM */
  .mtc p {{ font-size:1.3rem; color:var(--ink-dim); font-family:'Fraunces', serif; font-style:italic; margin-bottom:6px; }}
  .mtc p:last-child {{ color:var(--moss-deep); font-family:'Fraunces', serif; font-size:1.5rem; margin-top:16px; font-style:normal; font-weight:600; }}

  /* PRODUCTS */
  .products-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:2px; margin-top:20px; }}
  .product {{ border:1px solid var(--hairline); padding:32px; background:var(--paper-deep); }}
  .product h4 {{ font-size:1.3rem; margin-bottom:12px; color:var(--moss-deep); }}
  .product p {{ color:var(--ink-dim); margin-bottom:10px; }}
  .products-note {{ margin-top:28px; font-style:italic; color:var(--ink-dim); font-family:'Fraunces', serif; font-size:1.15rem; }}
  @media (max-width:700px) {{ .products-grid {{ grid-template-columns:1fr; }} }}

  /* CUSTOMIZATION TIERS */
  .tier {{ display:grid; grid-template-columns:60px 1fr; gap:24px; padding:30px 0; border-top:1px solid var(--hairline); }}
  .tier:last-child {{ border-bottom:1px solid var(--hairline); }}
  .tier-num {{ font-family:'Fraunces', serif; font-style:italic; color:var(--brass); font-size:1.5rem; }}
  .tier-body h4 {{ font-size:1.3rem; margin-bottom:8px; }}
  .tier-body p {{ color:var(--ink-dim); }}

  /* POD */
  .pod-lead {{ color:var(--ink-dim); font-size:1.1rem; margin-bottom:24px; max-width:600px; }}
  .pod-items {{ list-style:none; margin-bottom:28px; }}
  .pod-items li {{ font-size:1rem; color:var(--ink); padding:8px 0; border-top:1px solid var(--hairline); }}
  .pod-close {{ display:flex; gap:24px; }}
  .pod-close span {{ font-family:'Fraunces', serif; font-style:italic; color:var(--moss-deep); font-size:1.2rem; }}

  /* FINDER */
  .finder-lead {{ font-family:'Fraunces', serif; font-style:italic; font-size:1.35rem; color:var(--moss-deep); margin-bottom:20px; max-width:600px; }}
  .finder-body {{ color:var(--ink-dim); margin-bottom:24px; }}
  .facets {{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:32px; }}
  .facet {{ border:1px solid var(--brass); color:var(--moss-deep); font-size:0.85rem; padding:8px 18px; font-weight:500; }}
  .finder-close {{ display:flex; gap:20px; flex-wrap:wrap; color:var(--ink-dim); font-style:italic; font-family:'Fraunces', serif; font-size:1.1rem; }}

  /* DIFFERENCE */
  .difference-lead p {{ color:var(--ink-dim); font-size:1.1rem; max-width:600px; margin-bottom:8px; }}
  .pairs {{ margin-top:44px; display:grid; grid-template-columns:1fr 1fr; gap:14px 40px; }}
  .pair {{ display:flex; align-items:baseline; gap:14px; padding:14px 0; border-top:1px solid var(--hairline); }}
  .pair .from {{ color:var(--ink-dim); font-size:0.98rem; min-width:150px; }}
  .pair .arrow {{ color:var(--brass); }}
  .pair .to {{ color:var(--moss-deep); font-family:'Fraunces', serif; font-style:italic; font-size:1.05rem; }}
  @media (max-width:700px) {{ .pairs {{ grid-template-columns:1fr; }} }}

  /* IMAGINE */
  .imagine {{ text-align:center; }}
  .imagine-line {{ font-family:'Fraunces', serif; font-style:italic; font-size:clamp(1.2rem,3vw,1.7rem); color:var(--ink-dim); margin-bottom:18px; }}
  .imagine-line:last-child {{ color:var(--moss-deep); font-weight:600; }}
  .imagine-final {{ margin-top:50px; font-family:'Fraunces', serif; font-size:clamp(1.8rem,4vw,2.6rem); color:var(--brass); font-weight:600; }}

  /* FOOTER */
  footer {{ background:var(--moss-900); padding:100px 0 60px; text-align:center; }}
  footer h3, footer .foot-fine {{ color:var(--paper); }}
  .foot-block {{ margin-bottom:44px; }}
  .foot-block h3 {{ font-size:1.6rem; color:var(--brass-light); margin-bottom:8px; }}
  .foot-block p {{ color:var(--paper-deep); font-size:0.98rem; opacity:0.85; }}
  .foot-rhythm {{ margin-top:60px; font-family:'Fraunces', serif; font-style:italic; font-size:1.3rem; color:var(--paper-deep); }}
  .foot-fine {{ margin-top:40px; font-size:0.75rem; letter-spacing:0.12em; text-transform:uppercase; opacity:0.6; }}

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
    <p style="color:var(--ink-dim);">Available automatically as:</p>
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
    <p class="foot-fine">LifeTogether Ministries \u2014 Classic Edition Brochure</p>
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

with open("/mnt/user-data/outputs/whole-church-formation-classic-edition.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("done", len(HTML))
