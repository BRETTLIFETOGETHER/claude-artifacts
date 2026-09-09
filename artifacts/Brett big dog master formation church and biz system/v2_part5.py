def build(cat_list, is_new=False):
    return "".join(cat_sec(i+1,n,d,b,c,entries,is_new) for i,(n,d,b,c,entries) in enumerate(cat_list))

def build_chars_deep():
    out = ""
    for i,(name,color,entries) in enumerate(zip(CHAR_DEEP_NAMES, CHAR_DEEP_COLORS, CHAR_DEEP_ENTRIES)):
        desc = f"10 additional formation angles going deeper into {name.lower()}"
        out += cat_sec(i+1, name+" — Additional", desc, "", color, entries)
    return out

total = (
    sum(len(e) for _,_,_,_,e in BIBLE_DEEP) +
    sum(len(e) for _,_,_,_,e in BIBLE_NEW) +
    sum(len(e) for e in CHAR_DEEP_ENTRIES) +
    sum(len(e) for _,_,_,_,e in CHAR_NEW) +
    sum(len(e) for _,_,_,_,e in STORIES_DEEP) +
    sum(len(e) for _,_,_,_,e in STORIES_NEW)
)

COVER = f"""<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-top">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">Campaign Library · Volume II · Deep Expansion</span>
  </div>
  <div class="cover-body">
    <p class="cover-ey">Bible Campaigns · Biblical Characters · Bible Stories &amp; Themes</p>
    <h1 class="cover-h1">{total:,}<br>New<br><em>Series.</em></h1>
    <div class="cover-rule"><div class="cover-rule-dot"></div><div class="cover-rule-line"></div></div>
    <p class="cover-sub">Volume II of the Lifetogether Campaign Library — doubling every existing category with additional series going deeper into the same formation territory, plus 30 brand-new categories not previously covered. Every title designed for the senior pastor ready for the formation underneath the obvious series.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">{total:,}</span><span class="cstat-l">New Series Titles</span></div>
      <div class="cstat"><span class="cstat-n">30</span><span class="cstat-l">New Categories</span></div>
      <div class="cstat"><span class="cstat-n">60+</span><span class="cstat-l">Categories Deepened</span></div>
      <div class="cstat"><span class="cstat-n">66</span><span class="cstat-l">Books Covered</span></div>
      <div class="cstat"><span class="cstat-n">Vol I+II</span><span class="cstat-l">Combined Library</span></div>
      <div class="cstat"><span class="cstat-n">1,650+</span><span class="cstat-l">Total Series Titles</span></div>
    </div>
  </div>
</section>"""

BODY = (
    coll_hdr("var(--c1)","Collection One — 500 New Bible Campaign Series",
             "<em>Deeper and Broader</em><br>Bible Campaigns",
             "250 additional series across 10 existing categories — going deeper into the same canon with fresh formation angles. Plus 250 across 10 brand-new categories not previously covered.",
             "500 Series · 10 Deepened · 10 New Categories") +
    build(BIBLE_DEEP) +
    new_divider("10 New Bible Campaign Categories — formation angles not previously covered in Volume I") +
    build(BIBLE_NEW, is_new=True) +

    coll_hdr("var(--c2)","Collection Two — 300 New Character Series",
             "<em>Deeper and Broader</em><br>Biblical Character Series",
             "10 additional series for each of the 20 existing character categories. Plus 10 brand-new character categories.",
             "300 Series · 20 Deepened · 10 New Categories") +
    build_chars_deep() +
    new_divider("10 New Biblical Character Categories — not previously covered in Volume I") +
    build(CHAR_NEW, is_new=True) +

    coll_hdr("var(--c3)","Collection Three — 200 New Stories and Themes Series",
             "<em>Deeper and Broader</em><br>Bible Stories, Themes &amp; Passages",
             "10 additional series for each of the 10 existing story/theme categories. Plus 10 brand-new categories built around specific texts not previously addressed.",
             "200 Series · 10 Deepened · 10 New Categories") +
    build(STORIES_DEEP) +
    new_divider("10 New Bible Story, Theme and Passage Categories — not previously covered in Volume I") +
    build(STORIES_NEW, is_new=True)
)

BACK = """<div class="hdiv"></div>
<section class="back">
  <p class="back-q">"The congregation that has done the same ten series for twenty years has not exhausted Scripture. It has not even begun. Volume II exists for the pastor who wants to take their congregation somewhere it has never been — not just a new text, but a new angle on a familiar one, a character they have never preached, a theme they have never named."</p>
  <p class="back-a">Brett Eastman · Founder, Lifetogether</p>
  <p class="back-c"><a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp; <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp; 25 Years · 500+ Church Relationships · 50M+ Campaigns</p>
  <div class="lm">Lifetogether</div>
</section>"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lifetogether · Campaign Library Vol II · {total:,} New Series</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{STYLES}</style>
</head>
<body>
<div class="page">
{COVER}
{BODY}
{BACK}
</div>
</body>
</html>"""

with open('/mnt/user-data/outputs/lifetogether-bible-campaigns-vol2.html','w') as f:
    f.write(HTML)

print(f"Done — {total:,} new series — {len(HTML):,} chars")
