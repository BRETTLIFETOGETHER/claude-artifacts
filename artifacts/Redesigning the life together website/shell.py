# Shared shell for all Lifetogether platform pages
import os
OUT = "/home/claude/site/lifetogether-platform"

def header(active=""):
    def a(k): return ' active' if k == active else ''
    return f"""
<div class="util">
  <div class="wrap">
    <span class="util-left">25+ Years &nbsp;·&nbsp; 500+ Church Partnerships &nbsp;·&nbsp; <b>Purpose Driven Heritage</b></span>
    <span class="util-right">
      <a href="mailto:contact@lifetogether.com">contact@lifetogether.com</a>
      <span class="pipe">|</span><a href="about.html#contact">Request a Sample</a>
      <span class="pipe">|</span><a href="browse.html">Search</a>
    </span>
  </div>
</div>
<header class="site">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Lifetogether home">
      <span class="ring">life</span><span class="rest">together</span><span class="tm">™</span>
    </a>
    <nav class="primary" aria-label="Primary">
      <div class="nav-item">
        <a class="nav-link{a('campaigns')}" href="browse.html">Campaigns <span class="chev"></span></a>
        <div class="mega" role="menu">
          <div class="mega-cols">
            <div>
              <h5>The Library</h5>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--green)"></span>Browse by Channel</a>
              <a class="mlink" href="browse.html#flagships"><span class="chdot" style="background:var(--gold)"></span>Editors&rsquo; Flagships</a>
              <a class="mlink" href="browse.html#seasonal"><span class="chdot" style="background:var(--c-calendar)"></span>Seasonal Collections</a>
              <a class="mlink" href="assessment.html"><span class="chdot" style="background:var(--c-prayer)"></span>Campaign Finder</a>
              <a class="mlink" href="campaign.html"><span class="chdot" style="background:var(--c-community)"></span>See a Sample Campaign</a>
            </div>
            <div>
              <h5>Popular Channels</h5>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--c-purpose)"></span>Purpose &amp; Calling</a>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--c-prayer)"></span>Prayer &amp; Worship</a>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--c-emotional)"></span>Peace &amp; Emotional Health</a>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--c-family)"></span>Family Legacy</a>
              <a class="mlink" href="browse.html"><span class="chdot" style="background:var(--c-money)"></span>Money &amp; Stewardship</a>
            </div>
            <div class="mega-feature">
              <span class="chip gold" style="align-self:flex-start">★ Flagship</span>
              <b>40 Days of Life Together</b>
              <span>The groups launch campaign that gives the platform its name.</span>
              <a href="campaign.html">Explore the campaign →</a>
            </div>
          </div>
        </div>
      </div>
      <a class="nav-link{a('path')}" href="assessment.html">Find My Path</a>
      <a class="nav-link{a('pastors')}" href="create.html">For Pastors &amp; Leaders</a>
      <a class="nav-link{a('how')}" href="how-it-works.html">How It Works</a>
      <a class="nav-link{a('pricing')}" href="pricing.html">Pricing</a>
      <a class="nav-link{a('about')}" href="about.html">About</a>
      <a class="btn btn-primary btn-sm nav-cta" href="assessment.html">Take the Assessment</a>
    </nav>
    <button class="nav-burger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
<nav class="mobile-menu" aria-label="Mobile">
  <a href="browse.html">Campaigns</a>
  <a href="assessment.html">Find My Path</a>
  <a href="create.html">For Pastors &amp; Leaders</a>
  <a href="how-it-works.html">How It Works</a>
  <a href="pricing.html">Pricing</a>
  <a href="about.html">About</a>
  <a class="msmall" href="campaign.html">See a Sample Campaign</a>
  <a class="msmall" href="mailto:contact@lifetogether.com">contact@lifetogether.com</a>
</nav>
"""

FOOTER = """
<footer class="site">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <a class="brand" href="index.html"><span class="ring">life</span><span class="rest">together</span></a>
        <p class="foot-mission">Sermons into curriculum. Curriculum into community. Community into movements.</p>
        <p class="small">27132A Paseo Espada, Suite 423<br>San Juan Capistrano, CA 92675<br>949-769-0777 · contact@lifetogether.com</p>
      </div>
      <div>
        <h5>The Library</h5>
        <div class="fl">
          <a href="browse.html">Browse by Channel</a>
          <a href="browse.html#flagships">Editors&rsquo; Flagships</a>
          <a href="browse.html#seasonal">Seasonal Collections</a>
          <a href="assessment.html">Campaign Finder</a>
          <a href="campaign.html">Sample Campaign</a>
        </div>
      </div>
      <div>
        <h5>The Platform</h5>
        <div class="fl">
          <a href="assessment.html">Find My Path</a>
          <a href="create.html">For Pastors &amp; Leaders</a>
          <a href="how-it-works.html">How It Works</a>
          <a href="pricing.html">Pricing</a>
        </div>
      </div>
      <div>
        <h5>Company</h5>
        <div class="fl">
          <a href="about.html">Our Story &amp; Heritage</a>
          <a href="about.html#stories">Church Stories</a>
          <a href="about.html#contact">Schedule a Call</a>
          <a href="mailto:contact@lifetogether.com">Contact</a>
        </div>
      </div>
    </div>
    <div class="foot-bot">
      <span>© 2026 Lifetogether · lifetogether.com · Purpose Driven lineage · 500+ church partnerships</span>
      <span>Scripture standard: NIV · Used by permission of Biblica, Inc.</span>
    </div>
  </div>
</footer>
"""

def write(fname, title, body, active="", head="", scripts=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="Lifetogether — the intelligent Christian formation platform. 25 years of churchwide campaigns, personalized paths, and pastor content transformation.">
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/site.css">
{head}
</head>
<body>
{header(active)}
<main>
{body}
</main>
{FOOTER}
<script src="assets/app.js"></script>
{scripts}
</body>
</html>"""
    path = os.path.join(OUT, fname)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", fname, f"{os.path.getsize(path)//1024}KB")
