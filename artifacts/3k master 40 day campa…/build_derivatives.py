# -*- coding: utf-8 -*-
import copy
from common import esc, head, cover, toc, category_section, colophon, PALETTE
from transform import build_duration_categories, build_catalytic_sundays

def total_titles(cats):
    return sum(len(c["titles"]) for c in cats)

def add_legacy(cats, roman, entry):
    for c in cats:
        if c["roman"] == roman:
            c["titles"].append(entry)
            return
    raise ValueError(f"category {roman} not found")

def render(filename, page_title, eyebrow, cover_title_html, subtitle, stats, footer_note,
           intro_html, categories, colophon_title, colophon_note):
    parts = [head(page_title), cover(eyebrow, cover_title_html, subtitle, stats, footer_note), intro_html, toc(categories)]
    for i, cat in enumerate(categories):
        parts.append(category_section(cat, PALETTE[i % len(PALETTE)]))
    parts.append(colophon(colophon_title, colophon_note))
    parts.append("</body></html>")
    out = "".join(parts)
    with open(f"/mnt/user-data/outputs/{filename}", "w") as f:
        f.write(out)
    print(filename, "->", len(out), "bytes,", total_titles(categories), "titles")

# ============================================================
# FILE 1 — THE 7-DAY CHALLENGE MASTER LIBRARY
# ============================================================
seven = build_duration_categories("7 Days", "7-Day", {"Journey": "Challenge"})
add_legacy(seven, "VI", ("7 Days to Peace", "Legacy", "Original founding-library title, carried forward as a bonus entry alongside \u201c7 Days of Peace.\u201d"))
add_legacy(seven, "XX", ("7 Days of Generosity", "Legacy", "Original founding-library title, carried forward as a bonus entry."))

seven_intro = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">The One-Week On-Ramp</p>
  <h2>Every 40-day campaign, <em>in one week</em></h2>
  <p>This library takes all 600 titles from the Master 40-Day Campaign Library and reframes each one as a 7-Day Challenge &mdash; the shortest, easiest on-ramp in the whole system. Same theme, same category, one-seventh the runtime.</p>
  <p class="showcase-label">The 7-Day Session Map</p>
  <div class="session-map">
    <div class="session-day"><div class="session-day-label">Day 1</div><div class="session-day-name">Mon</div></div>
    <div class="session-day"><div class="session-day-label">Day 2</div><div class="session-day-name">Tue</div></div>
    <div class="session-day"><div class="session-day-label">Day 3</div><div class="session-day-name">Wed</div></div>
    <div class="session-day"><div class="session-day-label">Day 4</div><div class="session-day-name">Thu</div></div>
    <div class="session-day"><div class="session-day-label">Day 5</div><div class="session-day-name">Fri</div></div>
    <div class="session-day"><div class="session-day-label">Day 6</div><div class="session-day-name">Sat</div></div>
    <div class="session-day sunday"><div class="session-day-label">Day 7</div><div class="session-day-name">Celebration<br>Sunday</div></div>
  </div>
  <p>Six short daily readings, Monday through Saturday &mdash; five to ten minutes each, no small-group homework required. Then <strong>Celebration Sunday</strong>: a churchwide gathering that closes the week with worship, a testimony or two from people who did the challenge, and one clear next step (join a group, take a next class, make a decision).</p>
  <div class="criteria-box">
    <div class="label">Best Uses</div>
    <p>New-guest on-ramps &middot; dormant-attender re-engagement &middot; a sermon-series preview before launching the full 40-day version &middot; a low-barrier seasonal moment (New Year, back-to-school, a single hard week the church is walking through together) &middot; testing a theme before committing a full campaign season to it.</p>
  </div>
  <div class="legacy-box">
    <div class="label">Legacy Titles Integrated</div>
    <p>The five original 7-day titles from the founding library are folded in throughout: <strong>7 Days of Prayer</strong>, <strong>7 Days of Rest</strong>, and <strong>7 Days of Gratitude</strong> already appear verbatim as Direct-formula conversions in their categories. <strong>7 Days to Peace</strong> and <strong>7 Days of Generosity</strong> are carried forward as bonus entries in Grace, Peace &amp; Rest and Stewardship, since their exact phrasing differed from the converted set.</p>
  </div>
</section>
"""

render(
    "lifetogether-7-day-challenge-library.html",
    "The 7-Day Challenge Master Library",
    "LifeTogether Ministries \u00b7 Campaign & Curriculum Library",
    'The 7-Day Challenge<br><em>Master Library</em>',
    "Every 40-day campaign, reframed as a one-week on-ramp \u2014 six sessions and a Celebration Sunday.",
    [(30, "Categories"), (total_titles(seven), "Titles"), ("6+1", "Session Map"), ("All", "Ages")],
    "Derived from the Master 40-Day Campaign Library",
    seven_intro,
    seven,
    "The 7-Day Challenge Master Library",
    "600+ titles, six daily sessions and a Celebration Sunday, derived from every category in the Master 40-Day Campaign Library."
)

# ============================================================
# FILE 2 — THE 21-DAY EXPERIENCE MASTER LIBRARY
# ============================================================
twentyone = build_duration_categories("21 Days", "21-Day", {"Journey": "Experience"})
add_legacy(twentyone, "VI", ("21 Days to Peace", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XX", ("21 Days of Generosity", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XV", ("21 Days to Better Relationships", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(twentyone, "XVI", ("21 Days of Scripture", "Legacy", "Original founding-library title, carried forward as a bonus entry \u2014 daily Bible engagement."))

twentyone_intro = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">The Habit Builder</p>
  <h2>Three weeks, <em>one real habit</em></h2>
  <p>Twenty-one days is long enough to move past a good idea and into an actual rhythm &mdash; the format built specifically for habit formation: prayer, fasting, generosity, Bible engagement, emotional health, and the other spiritual disciplines that need repetition to stick.</p>
  <p class="showcase-label">The 21-Day Structure</p>
  <div class="session-map" style="grid-template-columns:repeat(4,1fr);">
    <div class="session-day"><div class="session-day-label">Week 1</div><div class="session-day-name">Foundation</div></div>
    <div class="session-day"><div class="session-day-label">Week 2</div><div class="session-day-name">Practice</div></div>
    <div class="session-day sunday"><div class="session-day-label">Week 3</div><div class="session-day-name">Commission<br>Sunday</div></div>
    <div class="session-day"><div class="session-day-label">Daily</div><div class="session-day-name">Habit<br>Tracker</div></div>
  </div>
  <p>Each week closes on a teaching Sunday that reinforces the daily habit rather than introducing new content &mdash; Week 3 closes with a Commissioning Sunday, sending people into the habit long-term with a simple tracking tool to keep it going past day 21.</p>
  <div class="criteria-box">
    <div class="label">Best Uses</div>
    <p>Prayer and fasting emphases &middot; generosity and giving seasons &middot; Bible engagement pushes &middot; emotional-health and gratitude rhythms &middot; any spiritual discipline the church wants to move from event to habit.</p>
  </div>
  <div class="legacy-box">
    <div class="label">Legacy Titles Integrated</div>
    <p><strong>21 Days of Prayer</strong> already appears verbatim as a Direct-formula conversion. <strong>21 Days to Peace</strong>, <strong>21 Days of Generosity</strong>, <strong>21 Days to Better Relationships</strong>, and <strong>21 Days of Scripture</strong> are carried forward as bonus entries in their nearest-fit categories, since their exact phrasing differed from the converted set.</p>
  </div>
</section>
"""

render(
    "lifetogether-21-day-experience-library.html",
    "The 21-Day Experience Master Library",
    "LifeTogether Ministries \u00b7 Campaign & Curriculum Library",
    'The 21-Day Experience<br><em>Master Library</em>',
    "Every 40-day theme, built for habit formation \u2014 three weeks to a rhythm that sticks.",
    [(30, "Categories"), (total_titles(twentyone), "Titles"), ("3", "Weeks"), ("All", "Ages")],
    "Derived from the Master 40-Day Campaign Library",
    twentyone_intro,
    twentyone,
    "The 21-Day Experience Master Library",
    "600+ titles built for habit formation \u2014 prayer, fasting, generosity, and Scripture engagement across three weeks."
)

# ============================================================
# FILE 3 — THE 30-DAY / 4-WEEK COMPANION JOURNEYS
# ============================================================
thirty = build_duration_categories("30 Days", "4-Week")
add_legacy(thirty, "IX", ("30 Days of Flourishing", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(thirty, "XII", ("30 Days to Whole-Life Health", "Legacy", "Original founding-library phrasing, kept alongside the converted \u201c30 Days of Whole Life Health.\u201d"))
add_legacy(thirty, "VI", ("30 Days to Better Balance", "Legacy", "Original founding-library title, carried forward as a bonus entry."))
add_legacy(thirty, "XXVI", ("30 Days to Emotional Resilience", "Legacy", "Original founding-library title, carried forward as a bonus entry."))

thirty_intro = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">The 4-Week Companion Format</p>
  <h2>A shorter arc, <em>a lighter lift</em></h2>
  <p>Not every series needs the full six-week, 40-day commitment. This library reframes most of the same themes as a <strong>4-week Sunday sermon arc</strong> &mdash; four messages instead of six &mdash; paired with a 30-day daily devotional companion that runs a little longer than the sermon series itself, so the daily habit outlasts the last Sunday.</p>
  <div class="criteria-box">
    <div class="label">How This Differs From the 40-Day Format</div>
    <p><strong>Fewer sermon weeks:</strong> four Sunday messages, not six.</p>
    <p><strong>A lighter devotional:</strong> shorter daily entries built for a quicker read, not the fuller 40-day devotional structure.</p>
    <p><strong>Small-group-first:</strong> designed to launch a group off a shorter series commitment &mdash; a good on-ramp for groups not ready for a full 40-day round.</p>
    <p><strong>Different outline:</strong> weekly big-idea plus daily application, rather than the 40-day format's six-session curriculum plus full daily devotional arc.</p>
  </div>
  <p class="showcase-label">Format Note</p>
  <p>Titles below carry two conventions: <strong>&ldquo;30 Days of X&rdquo;</strong> for the daily-devotional framing, and <strong>&ldquo;The 4-Week X Journey&rdquo;</strong> for the Sunday-sermon-arc framing &mdash; use whichever matches how you're marketing the series that season.</p>
  <div class="legacy-box">
    <div class="label">Legacy Titles Integrated</div>
    <p><strong>30 Days of Rest</strong> already appears verbatim as a Direct-formula conversion. <strong>30 Days of Flourishing</strong>, <strong>30 Days to Whole-Life Health</strong>, <strong>30 Days to Better Balance</strong>, and <strong>30 Days to Emotional Resilience</strong> are carried forward as bonus entries in their nearest-fit categories.</p>
  </div>
</section>
"""

render(
    "lifetogether-30-day-4-week-journeys.html",
    "The 30-Day / 4-Week Companion Journeys",
    "LifeTogether Ministries \u00b7 Campaign & Curriculum Library",
    'The 30-Day Journeys<br><em>4-Week Companion Format</em>',
    "Most 40-day themes, reframed as a 4-week sermon arc with a lighter 30-day devotional companion.",
    [(30, "Categories"), (total_titles(thirty), "Titles"), ("4", "Sermon Weeks"), ("30", "Devotional Days")],
    "Derived from the Master 40-Day Campaign Library",
    thirty_intro,
    thirty,
    "The 30-Day / 4-Week Companion Journeys",
    "600+ titles built for a shorter sermon arc and lighter devotional companion \u2014 a small-group-first on-ramp to the full 40-day format."
)

# ============================================================
# FILE 4 — CATALYTIC SUNDAYS (500 Big Sundays)
# ============================================================
sundays = build_catalytic_sundays(limit_per_category=17)

sundays_intro = f"""
<section class="block bg-navy intro">
  <p class="intro-eyebrow">Not a Series \u2014 a Single Sunday</p>
  <h2>500 Sundays that <em>carry their own weight</em></h2>
  <p>Every title in this library stands alone. No six-week arc, no daily devotional, no small-group guide required &mdash; just one Sunday built to hit hard on its own: a launch Sunday that opens a season, a vision Sunday, a standalone message strong enough to be the whole point.</p>
  <div class="criteria-box">
    <div class="label">How to Use a Catalytic Sunday</div>
    <p><strong>As a launch:</strong> open a full campaign season with the single biggest idea from that theme, then let the 40-day, 30-day, 21-day, or 7-day version carry the follow-through.</p>
    <p><strong>As a capstone:</strong> close a season or teaching year with the theme's most concentrated statement.</p>
    <p><strong>On its own:</strong> a fifth-Sunday, holiday-adjacent, or between-series week that still needs to matter.</p>
  </div>
  <p>Titles are drawn from all 30 categories in the Master 40-Day Campaign Library, distilled to their single strongest idea &mdash; roughly 17 per category, 500+ in total.</p>
</section>
"""

render(
    "lifetogether-catalytic-sundays.html",
    "Catalytic Sundays",
    "LifeTogether Ministries \u00b7 Campaign & Curriculum Library",
    'Catalytic Sundays',
    "500 standalone, single-message Sundays \u2014 no series required.",
    [(30, "Categories"), (total_titles(sundays), "Big Sundays"), ("1", "Sunday Each"), ("New", "Library")],
    "Distilled from the Master 40-Day Campaign Library \u2014 no prior file found under this name",
    sundays_intro,
    sundays,
    "Catalytic Sundays",
    "500+ standalone single-Sunday titles, distilled from every category in the Master 40-Day Campaign Library."
)
