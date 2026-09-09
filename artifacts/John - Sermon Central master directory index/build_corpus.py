# -*- coding: utf-8 -*-
from build_index import *
from data_corpus1 import CORPUS_1
from data_corpus2 import CORPUS_2, BOOK_SERIES

CORPUS = CORPUS_1 + CORPUS_2
NPAIRS = sum(len(v) for _, v in CORPUS) + len(BOOK_SERIES)


def front(story):
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph("LIFETOGETHER MINISTRIES", S["cover_e"]))
    story.append(Spacer(1, 3))
    story.append(Paragraph("THE SERMON LIBRARY  \u00b7  THE MASTER TITLE LIBRARY", S["cover_m"]))
    story.append(Spacer(1, 2.35 * inch))
    story.append(Paragraph("Title and<br/>Subtitle", S["cover_t"]))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "%d original title and subtitle pairs, each carrying an anchor passage and a "
        "formation outcome &mdash; plus the arithmetic on what a 160,000-title library "
        "would actually cost you." % NPAIRS, S["cover_s"]))
    story.append(Spacer(1, 1.45 * inch))
    story.append(Paragraph(
        "13 topic families &nbsp;&middot;&nbsp; 312 message titles &nbsp;&middot;&nbsp; "
        "66 book series &nbsp;&middot;&nbsp; every pair coordinated to Axis A, C and F",
        S["cover_m"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "Working corpus, version 1 &nbsp;&middot;&nbsp; August 2026 &nbsp;&middot;&nbsp; "
        "Companion to The Master Preaching Index", S["cover_m"]))
    story.append(NextPageTemplate("inner"))
    story.append(PageBreak())

    # ---- the argument
    head(story, "BEFORE THE LIST",
         "The 160,000 you cannot have, and the number you should want instead",
         "Their 160,000 and your 21,214 are not the same unit. Everything below turns on "
         "that.")

    para(story,
      "Their 160,000 are finished sermons. Manuscripts, submitted by named pastors, each one "
      "a complete piece of work. Your 21,214 are title records. Comparing the two counts is "
      "comparing a warehouse to a catalog, and if you put a 160,000-row title list next to "
      "their 160,000 finished sermons in front of a pastor, the comparison does not flatter "
      "you &mdash; it invites him to open one of yours.",

      "The same rights problem applies to their list at 160,000 as at 300,000. Those titles "
      "are the property of the contributors who wrote them, and building your catalog on top "
      "of theirs is the one move that would hand the incumbent a legitimate grievance in the "
      "exact area &mdash; plagiarism &mdash; where they publish a policy and you have a "
      "positioning claim to protect. So this document contains none of their titles. Every "
      "line in it is original.")

    story.append(Spacer(1, 3))
    story.append(Paragraph("WHAT YOUR LIBRARY ACTUALLY HOLDS RIGHT NOW", S["h3"]))
    rows = [[Paragraph("v20 MASTER LIBRARY", S["th"]), Paragraph("ROWS", S["th"]),
             Paragraph("WHAT IT MEANS FOR A 160,000 TARGET", S["th"])]]
    for a, b, c in [
      ("Total title records", "21,214",
       "The honest headline number, after sixteen sources and three rounds of pruning."),
      ("Rated A &mdash; strong / ready", "1,393",
       "The only rows you could print today without a caveat. Under 7 per cent."),
      ("Rated B", "11,671", "Real, unverified, and mostly without a passage or an outcome."),
      ("Rated C and F", "7,062", "Weak or filler. Adding volume adds to this pile fastest."),
      ("Seen four or more times", "643",
       "The genuinely corroborated spine: How Much Is Enough?, God Owns It All, "
       "The Legacy Conversation, Kingdom Legacy."),
      ("Single mention, ungraded", "13,270",
       "Already greyed as unverified. This is 63 per cent of the library."),
      ("Collapsed as exact duplicates", "10,087",
       "Removed in v16 &mdash; roughly a third of everything ingested was the same title twice."),
    ]:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]),
                     Paragraph(b, S["tbb"]), Paragraph(c, S["tbi"])])
    story.append(tbl(rows, [1.85 * inch, 0.72 * inch, 4.45 * inch]))
    story.append(Spacer(1, 10))

    para(story,
      "Read those seven rows together and the case against a 160,000-row target makes itself. "
      "One row in three that came into the library was a word-for-word duplicate. Two rows in "
      "three that survived have been seen exactly once and carry no grade. You spent yesterday "
      "removing 10,087 duplicates, moving 4,054 session rows off the master, and pulling 323 "
      "rows that were never titles at all. Generating another 138,786 would manufacture, at "
      "scale and on purpose, precisely the mess you have been cleaning.")

    story.append(Spacer(1, 3))
    story.append(Band(
      "<b>The arithmetic nobody runs.</b> &nbsp;At thirty seconds per title for a human to read, "
      "grade and accept or reject it, 160,000 titles is 1,333 hours &mdash; eight months of "
      "full-time work before a single one is built. At the current build ratio in the Sermon "
      "Library (8 built against 5,155 titled), a 160,000-title catalog would ship with roughly "
      "248 finished messages behind it. The number would be impressive in a deck and indefensible "
      "in a demo.", S["tb"]))
    story.append(PageBreak())

    head(story, "THE BETTER ANSWER",
         "Three tiers instead of one number",
         "You do not need one count. You need three, each with a different job and a "
         "different audience.")

    rows = [[Paragraph("TIER", S["th"]), Paragraph("SIZE", S["th"]),
             Paragraph("WHAT IT IS FOR", S["th"]), Paragraph("WHO SEES IT", S["th"])]]
    for a, b, c, d in [
      ("<b>1. The Verified Spine</b>", "~1,400",
       "Every row A-rated, with a subtitle, an anchor passage and a formation outcome. "
       "Printed, bound, handed to a pastor. This is the artifact.",
       "Founders, partners, conferences"),
      ("<b>2. The Working Catalog</b>", "~21,000",
       "The full master library. Searchable, internal, honest about its own grades. Never "
       "printed and never claimed as a public number.",
       "You and Hannah"),
      ("<b>3. The Generative Surface</b>", "Unbounded",
       "Titles composed on demand from index coordinates at the moment a pastor asks. "
       "Never stored, never counted, never deduplicated because nothing accumulates.",
       "Every pastor, every query"),
    ]:
        rows.append([Paragraph(a, S["tb"]), Paragraph(b, S["tbb"]),
                     Paragraph(c, S["tb"]), Paragraph(d, S["tbi"])])
    story.append(tbl(rows, [1.3 * inch, 0.72 * inch, 3.4 * inch, 1.6 * inch]))
    story.append(Spacer(1, 10))

    para(story,
      "Tier 3 is the part worth arguing about, because it is where the scale claim actually "
      "lives and it is the one thing the incumbent cannot copy. Their 160,000 is a warehouse. "
      "It grows by 300 a week because three hundred pastors upload something, and every item "
      "in it has to be stored, moderated and searched forever. Yours would be a press. The "
      "index you already have &mdash; 353 topics, 66 books, 149 anchor passages, 56 occasions, "
      "7 outcomes, 4 hinges &mdash; multiplies out past 160,000 combinations before you add a "
      "single format variant, and none of it needs to exist until somebody asks for it.",

      "That changes what you are able to say in a founders conversation, and the honest version "
      "is stronger than the inflated one. Not <i>we have 160,000 sermons</i>, which invites the "
      "comparison you lose. Instead: <i>we can produce a coordinated title, subtitle, message, "
      "week of devotionals, group session and household edition for any of 353 topics across 66 "
      "books, 56 occasions and 7 formation outcomes &mdash; and here are fourteen hundred we "
      "have already verified.</i> The second claim is bigger, it is true, and it survives being "
      "checked.")

    story.append(Spacer(1, 6))
    story.append(Paragraph("THE TITLE GRAMMAR THAT MAKES TIER 3 REAL", S["h3"]))
    para(story,
      "Generation only works if it is governed. Every pair in this document was built on six "
      "title forms and four subtitle jobs, and the constraint is what keeps the output from "
      "reading like a machine wrote it.")

    rows = [[Paragraph("TITLE FORM", S["th"]), Paragraph("EXAMPLE FROM THIS CORPUS", S["th"]),
             Paragraph("WHEN TO USE IT", S["th"])]]
    for a, b, c in [
      ("Declarative", "God Owns It All", "A doctrinal claim the whole series rests on."),
      ("Interrogative", "How Much Is Enough?", "A felt need the listener already carries as a question."),
      ("Imperative", "Say the Hard Thing", "A message whose outcome is <i>do it</i>."),
      ("Single word", "Anxious &nbsp;\u00b7&nbsp; Holy &nbsp;\u00b7&nbsp; Wet",
       "Maximum weight, minimum explanation. Use sparingly or it becomes a tic."),
      ("Reversal", "The Rich Fool Had a Retirement Plan",
       "When the point is that the listener is the one being described."),
      ("Relational", "The Legacy Conversation",
       "When the product is a conversation rather than a concept."),
    ]:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tbi"]),
                     Paragraph(c, S["tb"])])
    story.append(tbl(rows, [1.05 * inch, 2.4 * inch, 3.57 * inch]))
    story.append(Spacer(1, 8))

    para(story,
      "The subtitle does one of four jobs and never restates the title: it names the "
      "<b>promise</b> (what changes), the <b>mechanism</b> (how), the <b>audience</b> (who this "
      "is for), or the <b>scope</b> (how long, how many). A subtitle that merely rephrases the "
      "title is the single most reliable sign a catalog was generated rather than written, and "
      "it is what makes eleven thousand B-rated rows read as filler.")
    story.append(PageBreak())

    head(story, "HOW TO READ THE CORPUS",
         "%d pairs, and what each one carries" % NPAIRS)
    para(story,
      "What follows is written, not generated: 312 message titles across the thirteen families "
      "of Axis A, then 66 series titles, one for every book of the Bible. Each message row "
      "carries its anchor passage and its formation outcome, so every line arrives already "
      "coordinated and can be dropped straight into the master workbook against the seven axis "
      "columns.",

      "Treat these as candidates for the Verified Spine rather than as finished catalog. They "
      "are original, they are A-standard, and none of them duplicates a title already carrying "
      "a strong signal in the master library &mdash; <i>God Owns It All</i>, <i>How Much Is "
      "Enough?</i> and <i>The Legacy Conversation</i> appear deliberately, because those four "
      "corroborated titles are the spine everything else hangs off and the corpus should show "
      "where it connects.",

      "Outcome tags use your seven steps. Expect the distribution to look uneven when you count "
      "it, and expect the unevenness to be instructive: <i>bring it back</i> appears twice in "
      "312 titles, which is roughly its share in most preaching and exactly the imbalance the "
      "outcome column exists to expose.")
    story.append(Spacer(1, 6))
    story.append(Band(
      "<b>What I need to give you the actual thing you asked for.</b> &nbsp;Upload the v20 "
      "master workbook and I will produce this same document from your real 21,214 rows &mdash; "
      "Verified Spine first, then the working catalog by family, with the ungraded single-mention "
      "rows separated rather than hidden. That is a print job, not a research job, and it is the "
      "title-and-subtitle PDF you probably actually want.",
      S["tb"], bg=colors.HexColor("#f4f0e4"), bar=NAVY2))
    story.append(PageBreak())


def corpus_section(story):
    head(story, "THE CORPUS  \u00b7  PART ONE",
         "312 message titles",
         "Thirteen families, twenty-four each. Title, subtitle, anchor, outcome.")
    story.append(Spacer(1, 2))

    for i, (fam, items) in enumerate(CORPUS):
        block = [Paragraph(fam.upper(), S["h3"])]
        rows = [[Paragraph("TITLE", S["th"]), Paragraph("SUBTITLE", S["th"]),
                 Paragraph("ANCHOR", S["th"]), Paragraph("OUTCOME", S["th"])]]
        for t, sub, anc, out in items:
            rows.append([Paragraph("<b>%s</b>" % t, S["tb"]), Paragraph(sub, S["tb"]),
                         Paragraph(anc, S["tbi"]), Paragraph(out, S["tbi"])])
        block.append(tbl(rows, [1.72 * inch, 3.32 * inch, 1.06 * inch, 0.92 * inch]))
        block.append(Spacer(1, 8))
        story.append(KeepTogether(block) if len(items) <= 12 else block[0])
        if len(items) > 12:
            story.append(block[1]); story.append(block[2])
    story.append(PageBreak())

    head(story, "THE CORPUS  \u00b7  PART TWO",
         "66 series titles, one per book",
         "The book axis, converted from a canonical list into a bookable preaching year.")
    para(story,
      "Length is a recommendation, not a rule, and it assumes a congregation that will stay "
      "with a book rather than a topic. Added end to end these sixty-six run to roughly 350 "
      "weeks, which is a little under seven years of preaching &mdash; a useful thing to be "
      "able to say to a pastor who thinks he is out of material.")
    story.append(Spacer(1, 3))

    for label, span in [("OLD TESTAMENT", (0, 39)), ("NEW TESTAMENT", (39, 66))]:
        story.append(Paragraph(label, S["h3"]))
        rows = [[Paragraph("BOOK", S["th"]), Paragraph("SERIES TITLE", S["th"]),
                 Paragraph("SUBTITLE", S["th"]), Paragraph("LENGTH", S["th"])]]
        for bk, t, sub, ln in BOOK_SERIES[span[0]:span[1]]:
            rows.append([Paragraph(bk, S["tbi"]), Paragraph("<b>%s</b>" % t, S["tb"]),
                         Paragraph(sub, S["tb"]), Paragraph(ln, S["tbi"])])
        story.append(tbl(rows, [1.0 * inch, 1.72 * inch, 3.5 * inch, 0.8 * inch]))
        story.append(Spacer(1, 9))

    story.append(Spacer(1, 4))
    story.append(Band(
      "<b>Next action.</b> &nbsp;Drop these %d rows into the v20 workbook as source seventeen, "
      "graded A and flagged LifeTogether-original so they never read as ingested from anywhere "
      "else. Then upload the workbook and I will build the Verified Spine edition of this "
      "document from your real library. The count that wins is 1,400 you can defend, not "
      "160,000 you cannot." % NPAIRS, S["tb"], bg=colors.HexColor("#f4f0e4"), bar=NAVY2))


def build(path):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=0.85 * inch,
                          title="Title and Subtitle - LifeTogether Working Corpus",
                          author="LifeTogether Ministries",
                          subject="378 original title and subtitle pairs")
    fr = Frame(MARGIN, 0.85 * inch, PW - 2 * MARGIN, PH - MARGIN - 0.85 * inch,
               id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[fr], onPage=cover_page),
        PageTemplate(id="inner", frames=[fr], onPage=inner_page),
    ])
    story = []
    front(story)
    corpus_section(story)
    doc.build(story)
    return path


if __name__ == "__main__":
    out = "/home/claude/Title-and-Subtitle-Corpus.pdf"
    build(out)
    print("built", out, os.path.getsize(out), "bytes", "| pairs:", NPAIRS)
