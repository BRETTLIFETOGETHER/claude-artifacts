# -*- coding: utf-8 -*-
from common import esc, head, cover, category_section, back_cover, outline_of_categories, PALETTE
from data import CATEGORIES as MASTER40
from transform import build_duration_categories, build_catalytic_sundays
from calendar_data import CALENDAR_MAP
import copy

def total_titles(cats):
    return sum(len(c["titles"]) for c in cats)

def add_legacy(cats, roman, entry):
    for c in cats:
        if c["roman"] == roman:
            c["titles"].append(entry)
            return

# ---- Build all five duration sets ----
forty = copy.deepcopy(MASTER40)

seven = build_duration_categories("7 Days", "7-Day", {"Journey": "Challenge"})
add_legacy(seven, "VI", ("7 Days to Peace", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(seven, "XX", ("7 Days of Generosity", "Legacy", "Original founding-library title, carried forward as a bonus entry."))

twentyone = build_duration_categories("21 Days", "21-Day", {"Journey": "Experience"})
add_legacy(twentyone, "VI", ("21 Days to Peace", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XX", ("21 Days of Generosity", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XV", ("21 Days to Better Relationships", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XVI", ("21 Days of Scripture", "Legacy", "Original founding-library title, carried forward as a bonus entry."))

thirty = build_duration_categories("30 Days", "4-Week")
add_legacy(thirty, "IX", ("30 Days of Flourishing", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(thirty, "XII", ("30 Days to Whole-Life Health", "Legacy", "Original founding-library phrasing, kept alongside the converted version."))
add_legacy(thirty, "VI", ("30 Days to Better Balance", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(thirty, "XXVI", ("30 Days to Emotional Resilience", "Legacy", "Original founding-library title, carried forward as a bonus entry."))

sundays = build_catalytic_sundays(limit_per_category=17)

GRAND_TOTAL = total_titles(forty) + total_titles(thirty) + total_titles(twentyone) + total_titles(seven) + total_titles(sundays)

# ============================================================
# Cover — accurate brand copy, matching the established LifeTogether voice
# ============================================================

master_cover = cover(
    "LifeTogether \u00b7 25 Years \u00b7 500+ Churches \u00b7 50M+ Campaigns",
    'The Campaign<br><em>Format System</em>',
    "One theme, five depths &mdash; the complete architecture behind every LifeTogether campaign, from a single Catalytic Sunday to a full 40-day churchwide season, plus the annual calendar map that ties them to the year.",
    [
        (5, "Formats"),
        (GRAND_TOTAL, "Total Titles"),
        (30, "Categories Each"),
        (len(CALENDAR_MAP), "Calendar Sundays"),
    ]
)

# ============================================================
# Ladder section
# ============================================================

ladder_html = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">One Strategy, Five Formats</p>
  <h2>The <em>Campaign Format Ladder</em></h2>
  <p>Every theme in this library can run at five different depths. They aren't five separate libraries &mdash; they're one strategy, so the same theme can meet a church wherever it's ready to start, and grow with it from there.</p>
  <div class="formula-grid">
    <div class="formula-card"><div class="formula-name">Catalytic Sunday</div><div class="formula-pattern">One standalone message</div><div class="formula-note">The anchor. No series required &mdash; launches, closes, or stands alone.</div></div>
    <div class="formula-card"><div class="formula-name">7-Day Challenge</div><div class="formula-pattern">Mon&ndash;Sat + Celebration Sunday</div><div class="formula-note">The on-ramp. Lowest barrier, guest-friendly, no group required.</div></div>
    <div class="formula-card"><div class="formula-name">21-Day Experience</div><div class="formula-pattern">3 weeks, daily habit</div><div class="formula-note">The habit builder. Long enough for a rhythm to stick.</div></div>
    <div class="formula-card"><div class="formula-name">30-Day / 4-Week Journey</div><div class="formula-pattern">4 sermons + 30-day devotional</div><div class="formula-note">The accessible middle. Lighter lift, small-group-first.</div></div>
    <div class="formula-card"><div class="formula-name">40-Day Campaign</div><div class="formula-pattern">6 sessions, full devotional</div><div class="formula-note">The flagship. Full churchwide commitment, all ages.</div></div>
  </div>
  <p style="margin-top:20px;">Use it in either direction: run a Catalytic Sunday or a 7-Day Challenge to test a theme before committing a full 40-day season to it &mdash; or run the 40-day campaign first and harvest a Catalytic Sunday and a 7-Day Challenge from it the following year.</p>
</section>
"""

# ============================================================
# TOC
# ============================================================

def build_toc():
    groups = [("Section I \u00b7 The 40-Day Campaign", forty, "40"), ("Section II \u00b7 The 30-Day / 4-Week Journey", thirty, "30"),
              ("Section III \u00b7 The 21-Day Experience", twentyone, "21"), ("Section IV \u00b7 The 7-Day Challenge", seven, "7"),
              ("Section V \u00b7 Catalytic Sundays", sundays, "SUN")]
    body = ""
    for gi, (label, cats, prefix) in enumerate(groups, 1):
        body += f'<p class="toc-group">{esc(label)}</p>'
        for c in cats:
            body += f'<a class="toc-link" href="#{prefix}-{c["roman"]}"><span class="ix">{c["roman"]}</span>{esc(c["name"])}</a>'
    return f"""
<section class="toc-nav">
  <p class="toc-title">Contents</p>
  <p class="toc-note">5 formats &middot; 30 categories each &middot; {GRAND_TOTAL} titles &middot; the full annual calendar map</p>
  {body}
</section>
"""

# ============================================================
# Strategy / narrative blocks (unchanged copy, new markup)
# ============================================================

def strategy_block(bg, eyebrow_ix, eyebrow_label, heading_html, paragraphs, criteria_label, criteria_items, showcase=None):
    p_html = "".join(f'<p>{p}</p>' for p in paragraphs)
    crit_html = "".join(f'<p><strong>{esc(k)}:</strong> {v}</p>' for k, v in criteria_items)
    showcase_html = ""
    if showcase:
        items = "".join(f'<div class="showcase-item"><span class="showcase-tag">{esc(n)}</span><span class="showcase-title">{esc(ex)}</span></div>' for n, ex in showcase)
        showcase_html = f'<p class="showcase-label" style="margin-top:0;">Same Theme, Different Formula</p><div class="showcase-grid">{items}</div>'
    return f"""
<section class="block bg-{bg} intro">
  <p class="intro-eyebrow"><span class="ix">{esc(eyebrow_ix)}</span>{esc(eyebrow_label)}</p>
  <h2>{heading_html}</h2>
  {p_html}
  {showcase_html}
  <div class="criteria-box">
    <div class="label">{esc(criteria_label)}</div>
    {crit_html}
  </div>
</section>
"""

section_a_intro = strategy_block(
    "navy", "I", "The Flagship Format", 'The 40-Day Campaign<br><em>Vision &amp; Strategy</em>',
    [
        "The 40-day campaign is LifeTogether's flagship format &mdash; the one with the deepest roots, the strongest market precedent, and the clearest path from Sunday sermon to daily devotional to small-group discussion. It's the format the whole library was originally built around, and it remains the highest-commitment, highest-payoff option in the system.",
        "<strong>Why 40 days, specifically:</strong> the number carries its own weight before a single word of content is written &mdash; Moses on the mountain, Israel's spies, Jesus in the wilderness, Nineveh's forty days of repentance. It signals a serious, formative season, not a quick fix.",
        "<strong>The marketing case:</strong> a 40-day campaign gives a church one unifying theme across every touchpoint for six weeks straight &mdash; the weekend sermon, the daily devotional, the small-group discussion guide, and the content ladder's age-appropriate kids' and teens' editions running in parallel. One theme, one set of graphics, one invite message, four audiences.",
        "<strong>Who it's for:</strong> the whole church, every age, every weekend.",
    ],
    "Marketing Assets This Format Anchors",
    [
        ("Sermon series", "6 weekend messages, one per session"),
        ("Daily devotional", "40 daily readings, full depth"),
        ("Small group guide", "6-session discussion guide matching the sermon arc"),
        ("Content ladder", "Parallel kids and teens editions of the same theme"),
        ("Capital/vision pairing", "Strongest format for a building or generosity campaign"),
    ]
)

section_b_intro = strategy_block(
    "forest", "II", "The Accessible Middle", 'The 30-Day Journey<br><em>4-Week Companion Format</em>',
    [
        "If the 40-day campaign is the flagship, the 30-day journey is its more accessible sibling &mdash; the same theme, a shorter runway, and a noticeably lighter lift for both the platform and the pew.",
        "<strong>What makes it unique:</strong> this is not just a trimmed-down 40-day campaign. It runs on a genuinely different outline &mdash; a 4-week sermon arc (four messages instead of six) paired with a 30-day daily devotional companion that's written shorter and simpler than the full 40-day devotional. The small-group guide is built to launch a group off a single month's commitment, not a six-week one.",
        "<strong>Why it earns its own slot in the system:</strong> not every season, and not every congregation, is ready for a full 40-day ask. New churches, smaller churches, a summer series when attendance dips, or a second mid-year campaign layered on top of the main season all fit this format better.",
    ],
    "How It Differs From the 40-Day Format",
    [
        ("Sermon weeks", "4, not 6"),
        ("Devotional depth", "Shorter daily entries, quicker read"),
        ("Small-group entry point", "The easier on-ramp to launch a new group"),
        ("Best timing", "Summer series, second mid-year campaign, or a new church's first series"),
    ]
)

section_c_intro = strategy_block(
    "plum", "III", "The Habit Builder", 'The 21-Day Experience<br><em>Three Weeks to a Rhythm</em>',
    [
        "Twenty-one days is the format built for one job: turning a good intention into an actual habit. It's long enough to move past the initial motivation spike and into repetition, without asking for the full six-week commitment of the 40-day format.",
        "<strong>The structure:</strong> three weeks, each closing on a teaching Sunday that reinforces the habit &mdash; Week 1 (Foundation), Week 2 (Practice), and Week 3 closing on a Commissioning Sunday that sends people into the habit long-term.",
        "<strong>Best-fit themes:</strong> prayer and fasting, generosity and giving rhythms, Bible engagement, gratitude, and the other spiritual disciplines that live or die by repetition.",
    ],
    "Best Uses",
    [
        ("Prayer & fasting emphases", "The single most natural fit for this format"),
        ("Generosity rhythms", "Giving habits, not just an annual ask"),
        ("Bible engagement pushes", "Daily reading plans with a churchwide on-ramp"),
        ("Emotional health & gratitude", "Habits that need three weeks to take root"),
    ]
)

section_d_intro = strategy_block(
    "teal", "IV", "The On-Ramp", 'The 7-Day Challenge<br><em>The Lowest-Barrier Format</em>',
    [
        "The 7-Day Challenge is the easiest yes in the entire system &mdash; a one-week commitment with no small-group homework required, built to bring in people who would never sign up for a 40-day campaign cold.",
        "<strong>The structure:</strong> six short daily readings, Monday through Saturday, then <strong>Celebration Sunday</strong> &mdash; a churchwide gathering that closes the week with worship, testimonies, and one clear next step.",
        "<strong>Where it sits in the strategy:</strong> a stand-alone on-ramp for new guests and dormant attenders, or a preview week the Sunday before launching the full 40-day or 30-day version of the same theme.",
    ],
    "Best Uses",
    [
        ("New-guest on-ramps", "The easiest first commitment a first-time visitor can make"),
        ("Dormant-attender re-engagement", "Low enough barrier to bring people back"),
        ("Series preview week", "Test a theme before committing a full season to it"),
        ("Single hard week", "A seasonal moment the whole church is walking through together"),
    ]
)

# ---- Calendar map ----
calendar_rows = ""
for when, event, cat_name, title, note in CALENDAR_MAP:
    calendar_rows += f"""
      <li>
        <span class="cal-when">{esc(when)}</span>
        <div class="cal-body">
          <span class="cal-title">{esc(event)} &mdash; <em>{esc(title)}</em></span>
          <span class="cal-cat">{esc(cat_name)}</span>
          <span class="cal-note">{esc(note)}</span>
        </div>
      </li>"""

section_e_intro = f"""
<section class="block bg-umber intro">
  <p class="intro-eyebrow"><span class="ix">V</span>The Standalone Anchor</p>
  <h2>Catalytic Sundays &amp; the <em>Annual Calendar Map</em></h2>
  <p>Not every Sunday is part of a series. Some Sundays are given to you by the calendar &mdash; Easter, Mother's Day, Father's Day, Memorial Day, Christmas &mdash; and they need their own big idea, whether or not they fall inside a current campaign.</p>
  <div class="criteria-box">
    <div class="label">A Note on the Original Calendar Map</div>
    <p>You mentioned having built a fuller calendar map previously. I searched and found one direct reference &mdash; "the calendar locks: Easter, Christmas/Advent, Mother's Day, and the annual At the Movies outreach series" &mdash; inside the Preaching Forecast research, but no standalone file with the full set of dates. If it exists elsewhere, it didn't surface in search. The map below is rebuilt fresh and in full.</p>
  </div>
  <p class="showcase-label" style="margin-top:0;">The Annual Catalytic Sunday Map &mdash; {len(CALENDAR_MAP)} Dates</p>
  <ul class="cal-list">{calendar_rows}</ul>
</section>
<div class="divider"></div>
<section class="block bg-navy intro">
  <p class="intro-eyebrow">Beyond the Calendar</p>
  <h2>500+ <em>Big Sundays</em>, Any Week</h2>
  <p>Beyond the calendar-locked dates above, every category in the library has its own standalone Catalytic Sunday &mdash; a single message strong enough to open a series, close a season, or carry a Sunday that isn't tied to any date on the calendar.</p>
</section>
"""

# ============================================================
# Assemble
# ============================================================

def render_categories(cats, prefix):
    parts = []
    for i, cat in enumerate(cats):
        bg = PALETTE[i % len(PALETTE)]
        sec = category_section(cat, bg)
        sec = sec.replace(f'id="cat-{cat["roman"]}"', f'id="{prefix}-{cat["roman"]}"', 1)
        parts.append(sec)
    return "".join(parts)

back_quote = ("What the campaign creates in these days &mdash; the community, the language, the conviction, "
              "the relationships, the stories &mdash; is exactly what the ministry needs to be sustainable from "
              "week one. You are not launching a program. You are releasing a movement the campaign already built.")
back_attribution = "Brett Eastman &middot; Founder, LifeTogether"
back_contact = ('<a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &middot; '
                '<a href="https://lifetogether.com">lifetogether.com</a> &middot; '
                '25 Years &middot; 500+ Churches &middot; 50M+ Campaigns')

doc_parts = [
    head("The LifeTogether Campaign Format System"),
    master_cover,
    ladder_html,
    build_toc(),
    section_a_intro,
    outline_of_categories(forty, "Section I Categories at a Glance"),
    render_categories(forty, "40"),
    section_b_intro,
    outline_of_categories(thirty, "Section II Categories at a Glance"),
    render_categories(thirty, "30"),
    section_c_intro,
    outline_of_categories(twentyone, "Section III Categories at a Glance"),
    render_categories(twentyone, "21"),
    section_d_intro,
    outline_of_categories(seven, "Section IV Categories at a Glance"),
    render_categories(seven, "7"),
    section_e_intro,
    outline_of_categories(sundays, "Section V Categories at a Glance"),
    render_categories(sundays, "SUN"),
    back_cover(back_quote, back_attribution, back_contact, "LifeTogether"),
    "</body></html>"
]

out = "".join(doc_parts)
with open("/mnt/user-data/outputs/lifetogether-campaign-format-system.html", "w") as f:
    f.write(out)

print("Total bytes:", len(out))
print("Grand total titles:", GRAND_TOTAL)
