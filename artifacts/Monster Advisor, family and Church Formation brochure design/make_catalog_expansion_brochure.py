PAGES = []
def add(html): PAGES.append(html)

def folio(chapter, num):
    return f'''<div class="folio"><div class="thread">{chapter}</div><div>{num:02d}</div></div>'''

# =================================================================
# PAGE 1 — COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:flex-end;">
    <div style="font-family:'Archivo'; font-weight:600; font-size:9pt; letter-spacing:0.22em; color:#D9B876; margin-bottom:2.1in;">40 DAY CAMPAIGNS &middot; CATALOG EXPANSION</div>
    <h1 class="display" style="font-size:30pt; color:#FBF8F1;">2,528 New Titles</h1>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Playfair'; font-style:italic; font-weight:600; font-size:14pt; color:#D9B876;">Part J: Forty Felt-Need Categories &middot; Part K: All Sixty-Six Books of the Bible</div>
    <div style="height:0.26in;"></div>
    <p class="lede" style="font-size:10.3pt; color:rgba(251,248,241,0.8); max-width:5.6in;">
      Built around the gap already identified in your own research &mdash; the pastor&rsquo;s felt
      need and the congregation&rsquo;s felt need are related, but not identical. The strongest
      campaigns serve both at once.
    </p>
  </div>
</div>
''')

# =================================================================
# PAGE 2 — THE BIG IDEA
# =================================================================
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">THE BIG IDEA</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:20pt; color:var(--navy);">Two felt needs, not one.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      Your congregation&rsquo;s felt needs already cluster around purpose, relationships,
      anxiety, money, belonging, parenting, and doubt. What&rsquo;s thinner is the <b>pastor&rsquo;s
      own felt need</b> &mdash; leadership loneliness, the tension between institutional
      maintenance and prophetic calling, and the exhaustion of shepherding everyone
      without having a shepherd of his own.
    </p>
    <div style="height:0.14in;"></div>
    <p class="lede">
      A pastor who feels personally understood by a category brings it to his church far
      more readily than one he is only licensing.
    </p>
    <div style="height:0.22in;"></div>
    <div class="takeaway">
      <span class="label">Two gaps named explicitly in prior research</span>
      Suffering &amp; Lament &mdash; the series pastors are most afraid to preach and report as most transformational when they do. Doubt &amp; Deconstruction &mdash; the fastest-growing opportunity with younger and unchurched-adjacent audiences.
    </div>
  </div>
  {folio("The Big Idea", 2)}
</div>
''')

# =================================================================
# PAGE 3 — BY THE NUMBERS
# =================================================================
stats = [("2,528", "New Titles, Total"), ("2,000", "Part J — Felt-Need Titles"), ("40", "New Categories"), ("528", "Part K — Bible-Book Titles"), ("66", "Books Covered"), ("0", "Duplicate Titles")]
stats_html = "".join([f'<div style="text-align:center; width:33%; margin-bottom:0.3in;"><div style="font-family:\'Playfair\'; font-weight:700; font-size:24pt; color:var(--navy);">{n}</div><div style="font-family:\'Archivo\'; font-weight:600; font-size:8pt; letter-spacing:0.06em; color:var(--gray); margin-top:0.04in;">{l}</div></div>' for n, l in stats])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">BY THE NUMBERS</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Honest math, checked programmatically.</h1>
    <div style="height:0.24in;"></div>
    <div style="display:flex; flex-wrap:wrap;">{stats_html}</div>
    <div style="height:0.1in;"></div>
    <div class="takeaway">
      <span class="label">On merging</span>
      This is a standalone new batch, internally deduplicated. It has not yet been checked against your live master catalog &mdash; send that file over for a clean merge and renumber.
    </div>
  </div>
  {folio("By the Numbers", 3)}
</div>
''')

# =================================================================
# PAGE 4 — PART J: THE SEVEN GROUPS
# =================================================================
groups = [
    ("Mental &amp; Emotional Health", ["Anxiety &amp; Worry", "Suffering &amp; Lament", "Depression &amp; the Dark Night", "Burnout &amp; Exhaustion", "Loneliness &amp; Isolation", "Comparison &amp; Social Media", "Grief &amp; Loss", "Shame &amp; Self-Worth"]),
    ("Faith &amp; Doubt", ["Doubt &amp; Deconstruction", "Wrestling with God", "Deconversion &amp; Prodigal Children", "Church Hurt &amp; Disillusionment", "Faith After Trauma"]),
    ("Relationships &amp; Family", ["Blended &amp; Step-Families", "Singleness &amp; Waiting Seasons", "Infertility &amp; Pregnancy Loss", "Divorce Recovery", "Widowhood", "Empty Nest", "Caregiving for Aging Parents", "Adoption &amp; Foster Care", "Special Needs Parenting", "Parenting Teens in the Digital Age"]),
    ("Life Transitions", ["Career Transition &amp; Unemployment", "Financial Anxiety", "Chronic Illness &amp; Disability", "Addiction Recovery", "Midlife Crisis &amp; Reinvention", "Retirement &amp; Purpose After Work"]),
    ("Culture &amp; Identity", ["Racial Reconciliation &amp; Unity", "Political Division in the Church", "Identity &amp; Belonging for Young Adults", "Singleness in a Couples&rsquo; Culture"]),
    ("Pastor &amp; Leader-Specific", ["The Lonely Leader", "Prophetic Calling vs. Institutional Demands", "Pastor&rsquo;s Family Under the Spotlight", "Ministry Burnout &amp; Sabbatical", "Succession &amp; Passing the Baton"]),
    ("Belonging &amp; Rhythm", ["Hospitality &amp; Belonging for Newcomers", "Rest, Sabbath &amp; Margin"]),
]
groups_html = ""
for gname, cats in groups:
    chips = "".join([f'<span class="chip">{c}</span>' for c in cats])
    groups_html += f'<div style="margin-bottom:0.18in;"><div style="font-family:\'Archivo\'; font-weight:700; font-size:8.5pt; letter-spacing:0.08em; color:var(--gold); margin-bottom:0.06in;">{gname.upper()}</div><div style="display:flex; flex-wrap:wrap; gap:0.06in;">{chips}</div></div>'
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PART J &mdash; THE SEVEN GROUPS</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:18pt; color:var(--navy);">Forty categories, organized so the shape is visible at a glance.</h1>
    <div style="height:0.14in;"></div>
    {groups_html}
  </div>
  {folio("Part J — The Seven Groups", 4)}
</div>
''')

# =================================================================
# PAGE 5 — PART J: SAMPLE TITLES SHOWCASE
# =================================================================
samples = [
    ("Anxiety &amp; Worry", "40 Days of the Weight You Carry"),
    ("Suffering &amp; Lament", "40 Days of the Silence of God"),
    ("Doubt &amp; Deconstruction", "40 Days of Questions You&rsquo;ve Been Afraid to Ask"),
    ("The Lonely Leader", "40 Days of Who Shepherds the Shepherd"),
    ("Prophetic Calling vs. Institutional Demands", "40 Days of the Pull Between Calling and Calendar"),
    ("Empty Nest", "40 Days of Who Am I After the Kids Leave"),
    ("Widowhood", "40 Days of the Empty Side of the Bed"),
    ("Church Hurt &amp; Disillusionment", "40 Days of the Wounded Belonging Again"),
    ("Rest, Sabbath &amp; Margin", "40 Days of the Unhurried Life"),
    ("Deconversion &amp; Prodigal Children", "40 Days of the Empty Seat at Church"),
]
samples_html = "".join([f'''
    <div style="border-top:1px solid var(--line); padding:0.13in 0;">
      <div style="font-family:'Archivo'; font-weight:600; font-size:7.6pt; letter-spacing:0.06em; color:var(--gold); margin-bottom:0.03in;">{cat}</div>
      <div style="font-family:'Playfair'; font-weight:700; font-size:12pt; color:var(--navy);">{title}</div>
    </div>''' for cat, title in samples])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PART J &mdash; A SAMPLE OF THE 2,000</div>
    <div style="height:0.16in;"></div>
    <h1 class="display" style="font-size:19pt; color:var(--navy);">Ten titles, out of two thousand.</h1>
    <div style="height:0.1in;"></div>
    {samples_html}
    <div style="height:0.16in;"></div>
    <p style="font-family:'Inter'; font-size:9pt; color:var(--gray); font-style:italic;">Each category carries fifty titles at this depth &mdash; the full list lives in the companion spreadsheet.</p>
  </div>
  {folio("Part J — Sample Titles", 5)}
</div>
''')

# =================================================================
# PAGE 6 — PART K: ALL 66 BOOKS
# =================================================================
OT = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"]
NT = ["Matthew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"]
ot_html = "".join([f'<div class="book-cell">{b}</div>' for b in OT])
nt_html = "".join([f'<div class="book-cell">{b}</div>' for b in NT])
add(f'''
<div class="page">
  <div class="frame">
    <div class="eyebrow">PART K &mdash; ALL SIXTY-SIX BOOKS</div>
    <div style="height:0.14in;"></div>
    <h1 class="display" style="font-size:17pt; color:var(--navy);">Eight titles per book, four formats, one complete library.</h1>
    <div style="height:0.1in;"></div>
    <p style="font-family:'Inter'; font-size:8.8pt; color:var(--gray); margin-bottom:0.14in;">Each book carries straight-through studies, Christ-centered readings, and thematic overviews, at 40, 30, 21, and 7 days.</p>
    <div style="font-family:'Archivo'; font-weight:700; font-size:7.5pt; letter-spacing:0.08em; color:var(--gold); margin-bottom:0.06in;">OLD TESTAMENT &mdash; 39 BOOKS</div>
    <div class="book-grid">{ot_html}</div>
    <div style="height:0.14in;"></div>
    <div style="font-family:'Archivo'; font-weight:700; font-size:7.5pt; letter-spacing:0.08em; color:var(--gold); margin-bottom:0.06in;">NEW TESTAMENT &mdash; 27 BOOKS</div>
    <div class="book-grid">{nt_html}</div>
  </div>
  {folio("Part K — All Sixty-Six Books", 6)}
</div>
''')

# =================================================================
# PAGE 7 — WHAT MAKES THESE DIFFERENT
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame">
    <div class="eyebrow">WHAT MAKES THESE DIFFERENT</div>
    <div style="height:0.2in;"></div>
    <h1 class="display" style="font-size:19pt; color:#FBF8F1;">Every title still follows the same architecture.</h1>
    <div style="height:0.16in;"></div>
    <p class="lede">
      The title names a specific audience&rsquo;s deepest felt need or most powerful aspiration.
      The arc builds theological conviction around that need over the length of the
      campaign. The Celebration Sunday produces stories that prove the journey was worth
      it. And the ministry launch invitation is not a program pitch &mdash; it is the natural,
      fully prepared next step the campaign has been building toward from day one.
    </p>
    <div style="height:0.2in;"></div>
    <div class="pull-quote">The campaign is not separate from the ministry launch. <span class="mark">The campaign IS the ministry launch.</span></div>
  </div>
  {folio("What Makes These Different", 7)}
</div>
''')

# =================================================================
# PAGE 8 — BACK COVER
# =================================================================
add(f'''
<div class="page navy">
  <div class="frame" style="display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center;">
    <div></div>
    <div>
      <div style="font-family:'Archivo'; font-weight:600; font-size:9.5pt; letter-spacing:0.28em; color:#D9B876;">LIFETOGETHER</div>
      <div style="height:0.26in;"></div>
      <h1 class="display" style="font-size:20pt; color:#FBF8F1;">2,528 titles. Zero duplicates. Ready to merge.</h1>
      <div style="height:0.18in;"></div>
      <p class="lede" style="max-width:4.4in; margin:0 auto;">
        Send the live master catalog and this becomes Part J and Part K, cleanly numbered
        and deduplicated against everything that already exists.
      </p>
      <div style="height:0.3in;"></div>
      <div style="width:30px; height:2px; background:#B98D3E; margin:0 auto;"></div>
    </div>
    <div style="font-family:'Archivo'; font-weight:500; font-size:7.6pt; letter-spacing:0.12em; color:rgba(251,248,241,0.4);">40 DAY CAMPAIGNS &middot; CATALOG EXPANSION &middot; PART J &amp; K</div>
  </div>
</div>
''')

# =================================================================
# ASSEMBLE
# =================================================================
with open("/home/claude/build/portrait_style.css") as f:
    base_css = f.read()

extra_css = '''
.chip{ font-family:'Archivo'; font-weight:600; font-size:7.6pt; letter-spacing:0.02em; color:var(--navy); background:var(--cream); border:1px solid var(--line); padding:0.045in 0.1in; border-radius:11px; }
.book-grid{ display:grid; grid-template-columns:repeat(6, 1fr); gap:0.05in 0.08in; }
.book-cell{ font-family:'Inter'; font-size:7.3pt; color:var(--ink); padding:0.035in 0; border-bottom:1px solid var(--line); }
'''

html = f'''<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{base_css}{extra_css}</style></head>
<body>{"".join(PAGES)}</body></html>'''

with open("/home/claude/build/catalog_expansion_brochure.html", "w") as f:
    f.write(html)
print("Pages:", len(PAGES))
