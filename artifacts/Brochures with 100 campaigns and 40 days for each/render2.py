# -*- coding: utf-8 -*-
"""Build Volume II (Campaigns 11-20) PDF, reusing Volume I page components."""
import data2
import render as R          # reuse camp_detail, camp_map, closing components
from weasyprint import HTML

C2 = data2.CATEGORY2
CAMPS = data2.CAMPAIGNS2
BRAND = "Lifetogether"

# ---- Volume II cover ----
def cover():
    return f"""
<div class="page">
  <div class="hero">
    <div class="brandline"></div>
    <div class="kicker">{C2['kicker']}</div>
    <h1 class="cover-title" style="margin-top:.30in;">{C2['title_html']}</h1>
    <hr class="rule">
    <div class="eyebrow" style="color:var(--gold2); margin:-.02in 0 .14in;">{C2['volline']}</div>
    <p class="lead" style="max-width:4.7in;">{C2['positioning']}</p>

    <div style="position:absolute; left:0.8in; right:0.8in; bottom:1.95in;">
      <div class="covpanel">
        <div class="ql">The Conviction</div>
        <div class="qt">{C2['conviction']}</div>
      </div>
    </div>

    <div style="position:absolute; left:0.8in; right:0.8in; bottom:0.95in;">
      <div class="statstrip">
        <div class="st"><div class="sv">10</div><div class="sl">New Campaigns</div></div>
        <div class="st"><div class="sv">400</div><div class="sl">Devotional Days</div></div>
        <div class="st"><div class="sv">60</div><div class="sl">Group Sessions</div></div>
        <div class="st"><div class="sv">11&ndash;20</div><div class="sl">In the Library</div></div>
      </div>
    </div>

    <div class="footer">
      <span>Brett Eastman &middot; Founder &middot; brett@lifetogether.com</span>
      <span class="bk">{BRAND}</span>
    </div>
  </div>
</div>"""

# ---- Volume II overview table ----
def overview():
    rows = ""
    for c in CAMPS:
        rows += f"""
      <tr>
        <td class="rk">{int(c['num'])}</td>
        <td style="width:2.1in;">
          <div class="nm">{c['title_plain']}</div>
          <div class="pos">{c['positioning']}</div>
          <div class="meta">{c['tier']} &middot; {c['audience']}</div>
        </td>
        <td class="sum">{c['description']}</td>
      </tr>"""
    return f"""
<div class="page">
  <div class="content">
    <div class="kicker gr">The Library Continues</div>
    <h1 class="mtitle" style="margin:6px 0 2px;">Ten More <span class="it">Finances Campaigns</span></h1>
    <p class="scrip" style="margin:1px 0 5px;">Campaigns eleven through twenty &mdash; each a complete series with its own biblical backbone, from firstfruits giving to starting over after loss.</p>
    <div class="divider" style="margin:8px 0;"></div>
    <table class="ovtable">{rows}</table>
    <div class="lfooter">
      <span>Finances Campaign Catalog &middot; Volume II &middot; Overview</span>
      <span class="bk">{BRAND}</span>
    </div>
  </div>
</div>"""

# ---- Volume II closing index ----
def closing():
    rows = ""
    for c in CAMPS:
        rows += (f'<div class="idxrow"><div class="in">{int(c["num"])}</div>'
                 f'<div class="it2">{c["title_plain"]}</div>'
                 f'<div class="ip">{c["positioning"]}</div>'
                 f'<div class="im">{c["tier"]}</div></div>')
    return f"""
<div class="page">
  <div class="hero">
    <div class="brandline"></div>
    <div class="kicker">Volume II &middot; The Library Continues</div>
    <h1 style="color:#fff; font-size:27pt; margin:7px 0 4px;">Twenty Campaigns. <span class="it">And Growing.</span></h1>
    <p class="lead" style="max-width:5in; margin-bottom:.16in;">With Volume II the Finances library reaches twenty flagship campaigns &mdash; a full calendar of formation for every season and stage a congregation walks through.</p>
    <div>{rows}</div>

    <div style="position:absolute; left:0.8in; right:0.8in; bottom:1.5in;">
      <div class="covpanel">
        <div class="ql">Next Step</div>
        <div class="qt" style="font-size:12.5pt;">Choose your next campaign and season &mdash; and we will keep building the library toward the full one hundred.</div>
      </div>
    </div>

    <div class="footer">
      <span>Brett Eastman &middot; brett@lifetogether.com &middot; Finances Campaign Catalog, Vol. II</span>
      <span class="bk">{BRAND}</span>
    </div>
  </div>
</div>"""

def build():
    parts = [cover(), overview()]
    for c in CAMPS:
        parts.append(R.camp_detail(c))
        parts.append(R.camp_map(c))
    parts.append(closing())
    body = "\n".join(parts)
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="style.css"></head><body>{body}</body></html>"""
    with open("catalog2.html", "w") as f:
        f.write(html)
    HTML(string=html, base_url=".").write_pdf("Finances_Campaign_Catalog_Vol2.pdf")
    print("Pages:", len(parts), "PDF written.")

if __name__ == "__main__":
    build()
