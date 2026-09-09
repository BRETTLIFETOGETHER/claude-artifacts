import os
from weasyprint import HTML

css = '<link rel="stylesheet" href="style.css">'

cover = """
<div class="page"><div class="hero">
  <div class="brandline"></div>
  <div class="kicker">Lifetogether &middot; Campaign Library</div>
  <h1 class="cover-title">Finances<br>Campaign <span class="it">Catalog</span></h1>
  <hr class="rule">
  <p class="lead">Ten flagship campaigns that help a congregation move from financial fear to faithful peace &mdash; built for churches and workplaces, ready to launch in any season.</p>
  <div style="position:absolute; right:0.8in; top:1.1in; width:3.2in;">
    <div class="panel"><div class="ttl">The Guiding Conviction</div>
      <div class="qt">"The way you handle money is never only a financial matter. It is one of the clearest windows into what you truly believe about God."</div>
    </div>
    <div class="gridcards" style="margin-top:12px;">
      <div class="minicard"><span class="n">1</span><div class="t">Faith &amp; Finances</div><div class="s">Money is a faith issue</div></div>
      <div class="minicard"><span class="n">2</span><div class="t">Money Made Simple</div><div class="s">Clarity for the overwhelmed</div></div>
    </div>
  </div>
  <div class="footer"><span>Finances Campaign Catalog &middot; Top 10 Edition</span><span class="bk">Lifetogether</span></div>
</div></div>
"""

camp = """
<div class="page"><div class="content">
  <div class="kicker gr">Campaign 01 &middot; Flagship</div>
  <h1 style="font-size:30pt; margin:4px 0 6px;">Faith &amp; <span class="it">Finances</span></h1>
  <p class="scrip">"No one can serve two masters... You cannot serve both God and money." &mdash; Matthew 6:24 (NIV)</p>
  <div class="divider"></div>
  <p style="font-size:9.5pt; line-height:1.55;">Most people keep money in one room of their lives and faith in another. This campaign tears down the wall between them, helping every participant discover that how they earn, spend, save, and give is one of the truest expressions of what they believe about God.</p>
  <div style="margin-top:10px;"><span class="tag">Stewardship</span><span class="tag">Trust</span><span class="tag">Surrender</span><span class="tag">Whole-life faith</span></div>
  <div class="two" style="margin-top:12px;">
    <div class="lblbox"><div class="l">The Core Problem</div><p>Faith and money feel disconnected &mdash; Sunday convictions rarely reach the Monday bank account.</p></div>
    <div class="lblbox"><div class="l">The Transformation</div><p>A congregation that handles money as an act of worship, with peace instead of pressure.</p></div>
  </div>
  <div class="divider"></div>
  <div class="kicker gr" style="margin-bottom:8px;">Six-Session Curriculum</div>
  <div class="two">
    <div class="sess"><div class="sn">Session 1</div><div class="st">Who Owns It All?</div><div class="sd">Moving from owner to steward of everything God has entrusted.</div></div>
    <div class="sess"><div class="sn">Session 2</div><div class="st">What Money Reveals</div><div class="sd">Your spending as a spiritual diagnostic of the heart.</div></div>
  </div>
  <div class="lfooter"><span>Faith &amp; Finances &middot; Expanded Campaign</span><span class="bk">Lifetogether</span></div>
</div></div>
"""

daymap = """
<div class="page"><div class="content">
  <div class="hbar"><div class="kicker" style="color:var(--gold2)">Faith &amp; Finances</div>
    <h2>The 40-Day <span class="it">Engagement Map</span></h2>
    <div class="sub">Forty days of formation &mdash; daily title, focus, and Scripture. The architecture for devotionals, not the devotionals themselves.</div>
  </div>
  <div style="height:12px;"></div>
  <div class="daymap">
    <div class="movement">
      <div class="mv-head">I &mdash; The Ownership Question<span class="sub">Who really owns it all?</span></div>
      <div class="day"><span class="dn">DAY 1</span> <span class="dt">The Great Transfer</span><br><span class="ds">Peace begins when "mine" becomes "His."</span><br><span class="dref">Psalm 24:1; 1 Chronicles 29:11&ndash;12</span></div>
      <div class="day"><span class="dn">DAY 2</span> <span class="dt">Every Dollar a Decision</span><br><span class="ds">Money reveals what you trust.</span><br><span class="dref">Matthew 6:21, 24; Proverbs 3:5&ndash;6</span></div>
    </div>
    <div class="movement">
      <div class="mv-head">II &mdash; The Wisdom Question<span class="sub">What does the Bible say about money?</span></div>
      <div class="day"><span class="dn">DAY 8</span> <span class="dt">God's Wisdom on Money</span><br><span class="ds">More verses than you'd expect.</span><br><span class="dref">Proverbs 21:20; Luke 14:28</span></div>
    </div>
  </div>
  <div class="lfooter"><span>Faith &amp; Finances &middot; 40-Day Engagement Map</span><span class="bk">Lifetogether</span></div>
</div></div>
"""

html = f"<html><head><meta charset='utf-8'>{css}</head><body>{cover}{camp}{daymap}</body></html>"
open("test.html","w").write(html)
HTML(string=html, base_url=".").write_pdf("test.pdf")
print("rendered test.pdf")
