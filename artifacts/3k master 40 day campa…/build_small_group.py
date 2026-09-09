# -*- coding: utf-8 -*-
from common import esc, head, cover, category_section, back_cover, outline_of_categories, PALETTE
from transform_sg import build_small_group_categories, EDGE_CATEGORIES

cats = build_small_group_categories()
total = sum(len(c["titles"]) for c in cats)
edge_cats = [c for c in cats if c["is_edge"]]

master_cover = cover(
    "LifeTogether \u00b7 Small Group Finder System",
    'The Small Group<br><em>Master Brochure</em>',
    "Every campaign category, converted into a 6-session small group series &mdash; and a clear read on which ones give a pastor a real edge right now.",
    [
        (30, "Categories"),
        (total, "Series"),
        (6, "Sessions Each"),
        (len(edge_cats), "Edge Categories"),
    ]
)

intro_html = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">How This Works</p>
  <h2>One catalog, <em>every category</em>, six sessions each</h2>
  <p>Every category from the Campaign Format System converts here into a small group series &mdash; the same theme, reshaped as a 6-session discussion guide matching a sermon arc, a stand-alone series, or a Builder starting point. Nothing was left out: all 30 categories, {total} series titles.</p>
  <div class="criteria-box">
    <div class="label">Reading the Tags on Each Series</div>
    <p><strong>Edge:</strong> flagged where a pastor would feel a real competitive advantage running it <em>right now</em> &mdash; live cultural conversations most churches have no ready answer for.</p>
    <p><strong>Video Recommended:</strong> felt-need, cultural-moment topics now carry a video-first market expectation &mdash; people are used to a face and a voice on these. Classic discipleship and formation topics still perform fine print-only.</p>
  </div>
</section>
"""

edge_rows = ""
for roman, note in EDGE_CATEGORIES.items():
    cat = next(c for c in cats if c["roman"] == roman)
    edge_rows += f"""
      <li>
        <span class="cal-when">{esc(cat['roman'])}</span>
        <div class="cal-body">
          <span class="cal-title">{esc(cat['name'])}</span>
          <span class="cal-note">{esc(note)}</span>
        </div>
      </li>"""

edge_html = f"""
<section class="block bg-umber intro">
  <p class="intro-eyebrow">Where You Have an Edge Right Now</p>
  <h2>The <em>Five</em> Categories Worth Leading With</h2>
  <p>These five aren't bigger than the other twenty-five &mdash; they're timelier. Each one addresses a conversation already happening in your congregation, mostly without pastoral input, and running it first is the edge.</p>
  <ul class="cal-list">{edge_rows}</ul>
</section>
<div class="divider"></div>
"""

def build_toc():
    body = ""
    for c in cats:
        badge = " \u2605" if c["is_edge"] else ""
        body += f'<a class="toc-link" href="#sg-{c["roman"]}"><span class="ix">{c["roman"]}</span>{esc(c["name"])}{badge}</a>'
    return f"""
<section class="toc-nav">
  <p class="toc-title">Contents</p>
  <p class="toc-note">30 categories &middot; {total} series &middot; \u2605 marks an Edge category</p>
  {body}
</section>
"""

def render_categories():
    parts = []
    for i, cat in enumerate(cats):
        bg = PALETTE[i % len(PALETTE)]
        sec = category_section(cat, bg)
        sec = sec.replace(f'id="cat-{cat["roman"]}"', f'id="sg-{cat["roman"]}"', 1)
        # Inject Edge / Video badges right after the eyebrow line
        badges = ""
        if cat["is_edge"]:
            badges += ' <span style="font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--navy);background:var(--gold-light);border-radius:9px;padding:2px 9px;margin-left:6px;">Edge \u2605</span>'
        if cat["video_recommended"]:
            badges += ' <span style="font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold-light);border:1px solid rgba(201,168,76,0.4);border-radius:9px;padding:2px 9px;margin-left:6px;">Video Recommended</span>'
        if badges:
            sec = sec.replace(f'Category {cat["roman"]}</p>', f'Category {cat["roman"]}{badges}</p>', 1)
        if cat["is_edge"] and cat["edge_note"]:
            sec = sec.replace(
                '<p class="showcase-label">All',
                f'<div class="legacy-box"><div class="label">Why This Is an Edge Category</div><p>{esc(cat["edge_note"])}</p></div><p class="showcase-label">All',
                1
            )
        parts.append(sec)
    return "".join(parts)

back_quote = ("A small group finds its footing the moment the topic feels like it was written for exactly "
              "what they're carrying this year, not five years ago. That's the whole bet behind this catalog.")
back_attribution = "Brett Eastman &middot; Founder, LifeTogether"
back_contact = ('<a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &middot; '
                '<a href="https://lifetogether.com">lifetogether.com</a> &middot; '
                '25 Years &middot; 500+ Churches &middot; 50M+ Campaigns')

doc_parts = [
    head("The Small Group Master Brochure"),
    master_cover,
    intro_html,
    edge_html,
    build_toc(),
    outline_of_categories(cats, "All 30 Categories at a Glance"),
    render_categories(),
    back_cover(back_quote, back_attribution, back_contact, "LifeTogether"),
    "</body></html>"
]

out = "".join(doc_parts)
with open("/mnt/user-data/outputs/lifetogether-small-group-master-brochure.html", "w") as f:
    f.write(out)

print("Bytes:", len(out), "Total series:", total, "Edge categories:", len(edge_cats))
