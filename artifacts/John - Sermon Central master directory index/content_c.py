# -*- coding: utf-8 -*-
from build_index import *
from content_a import front_matter, part_one, part_two
from content_b import part_three, part_four, part_five, part_six, part_seven


def part_eight(story):
    head(story, "PART EIGHT",
         "The join",
         "A list becomes a system at the moment every item carries coordinates on every axis.")

    para(story,
      "Everything to this point is a set of registers. Registers are useful and inert. What "
      "makes them a product is the join &mdash; a single table in which one row is one message "
      "and seven columns are its coordinates. Below is what that looks like using material you "
      "have already built or already named, so the pattern is concrete rather than "
      "hypothetical.")
    story.append(Spacer(1, 4))

    hdr = ["MESSAGE", "A TOPIC", "B BOOK", "C PASSAGE", "D OCCASION", "E PERSON",
           "F OUTCOME", "G HINGE"]
    rows = [[Paragraph(h, S["th"]) for h in hdr]]
    for r in [
      ("God Owns It All", "Stewardship", "1 Chronicles", "29:10&ndash;18",
       "Thanksgiving &rarr; year-end", "David", "Own it", "Giving"),
      ("He&rsquo;s Not Where You Left Him", "Resurrection", "John", "20:24&ndash;31",
       "Easter", "Thomas", "See it", "Gospel"),
      ("The Legacy Conversation", "Legacy &amp; Generations", "Deuteronomy", "6:4&ndash;9",
       "All Saints / Father&rsquo;s Day", "Moses", "Share it", "Rolls into"),
      ("How Much Is Enough?", "Contentment", "1 Timothy", "6:6&ndash;19",
       "New Year", "The Rich Fool", "Sit with it", "Call to action"),
      ("Two Are Better", "Small Groups", "Ecclesiastes", "4:9&ndash;12",
       "Group launch", "Jonathan", "Do it", "Rolls into"),
      ("Nothing Can Separate", "Assurance", "Romans", "8:31&ndash;39",
       "Funeral / crisis", "Paul", "Sit with it", "Gospel"),
    ]:
        rows.append([Paragraph("<b>%s</b>" % r[0], S["tb"])] +
                    [Paragraph(x, S["tb"]) for x in r[1:]])
    t = Table(rows, colWidths=[1.42 * inch, 0.86 * inch, 0.76 * inch, 0.78 * inch,
                               1.12 * inch, 0.72 * inch, 0.72 * inch, 0.64 * inch])
    cmds = [("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4.5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
            ("LINEAFTER", (0, 0), (0, -1), 0.4, RULE)]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), CREAM2))
    t.setStyle(TableStyle(cmds))
    story.append(t)
    story.append(Spacer(1, 12))

    story.append(Paragraph("WHAT THE JOIN LETS YOU DO THAT A BROWSE INDEX CANNOT", S["h3"]))
    para(story,
      "<b>Reverse lookup.</b> A pastor tells you he is preaching Ephesians 2 in October. A "
      "browse index returns other sermons on Ephesians 2. The join returns the season he is "
      "walking into, the formation outcome that text is best suited to produce, the campaign it "
      "rolls into, the children&rsquo;s and student versions of the same big idea, and the two "
      "messages that should follow it. That is the difference between a search result and a "
      "plan, and it is the entire product claim reduced to one query.",

      "<b>Gap detection.</b> Once every row is coordinated you can ask questions of the library "
      "that no one can currently answer. Which of the seventy-three categories has no Old "
      "Testament anchor? Which quarter of the calendar has nothing built against it? Which "
      "formation outcome is over-served? My expectation is that the second and third quarters "
      "are thin, that the outcome distribution is badly front-loaded, and that a dozen "
      "categories are running entirely on New Testament epistles. Each of those is a build "
      "queue that writes itself, which matters a great deal when the honest ratio is eight "
      "built against five thousand titled.",

      "<b>Edition generation.</b> The same coordinates drive the derivative editions. A message "
      "carrying <i>Person: Zacchaeus</i> and <i>Outcome: own it</i> has most of what a "
      "children&rsquo;s version needs specified before anyone writes a word. This is where the "
      "index stops being documentation and becomes production infrastructure, and it is the "
      "argument for coordinating the library before building more of it.",

      "<b>Honest inventory.</b> The least comfortable use, and the most valuable. A coordinated "
      "library tells you the truth about itself &mdash; how many titles are real, how many are "
      "the same idea under four names, how many carry no passage at all. The master workbook "
      "already carries a corroboration signal and a duplicate-merge history for exactly this "
      "reason. The seven axes extend that discipline from the title to the substance.")
    story.append(PageBreak())


def part_nine(story):
    head(story, "PART NINE",
         "Vision, Phase 1, next action",
         "The index is worth nothing unread and nothing uncoordinated. Here is the smallest "
         "credible first move.")

    story.append(Paragraph("VISION", S["h3"]))
    para(story,
      "Every record in the master library carries coordinates on all seven axes, and the index "
      "becomes the routing layer beneath the Sermon Library, the campaign platform and the "
      "custom build. A pastor tells the system three things &mdash; his text, his date, his "
      "church&rsquo;s season &mdash; and the system returns a message, a service, a week of "
      "devotionals, a group session, the household edition and the next step, because every one "
      "of those assets is addressable by the same coordinates. That is not a catalog with better "
      "search. It is the intelligence layer you have been circling and have not yet named.")

    story.append(Paragraph("PHASE 1", S["h3"]))
    para(story,
      "Do not coordinate twenty thousand rows. Coordinate the A-grade rows and nothing else "
      "&mdash; the roughly fourteen hundred titles already rated strong and ready. Add seven "
      "columns to the master workbook, one per axis. Two of them are close to populated "
      "already: topic exists in some form on most rows, and format is effectively a proxy for "
      "hinge on the campaign rows. The four that need real work are book, passage, occasion and "
      "outcome, and outcome is the one that cannot be automated because it requires a judgment "
      "about what the message is <i>for</i>. Budget that as human work and treat the other three "
      "as tractable.")

    story.append(Paragraph("NEXT ACTION", S["h3"]))
    rows = [[Paragraph("#", S["th"]), Paragraph("ACTION", S["th"]),
             Paragraph("WHY THIS ONE FIRST", S["th"])]]
    for a, b, c in [
      ("1", "Add the seven axis columns to the master workbook and coordinate the eight "
       "built messages by hand.",
       "Eight rows establishes the pattern, exposes the ambiguities, and takes an afternoon. "
       "Everything downstream is a copy of this decision."),
      ("2", "Run the seventy-three categories against the thirteen families in Part Three.",
       "This is a one-session exercise that will show which families you are over-indexed in "
       "and which of the sixty-two openings you can already serve from existing material."),
      ("3", "Correct the 300,000 figure to 160,000 wherever the comparison table carries it.",
       "It is in a document you will put in front of founders. Their number, verified, is "
       "stronger than an inflated one."),
    ]:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tb"]),
                     Paragraph(c, S["tbi"])])
    story.append(tbl(rows, [0.3 * inch, 3.1 * inch, 3.62 * inch]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("THE TWO EXTENSIONS WITH THE MOST LEVERAGE", S["h3"]))
    para(story,
      "<b>Finish Axis B and the illustration library in one pass.</b> The illustration library "
      "stands at ten books of sixty-six and four passages. Part Four of this document is the "
      "missing scaffolding for the other fifty-six. Building illustration sets book by book "
      "against this axis, rather than by theme, means one effort produces both the completed "
      "illustration resource and the coordinated book column. Doing them separately costs "
      "roughly twice as much for the same result, and the book axis is the one a pastor already "
      "thinks in.",

      "<b>Sell the calendar before you sell the library.</b> Registers 1 through 3 in Part Six, "
      "laid over fifty-two weeks and designed properly, are a standalone product with no sermon "
      "content in it at all. It is cheap to produce, it demonstrates the strategy claim in a "
      "form a pastor can hold, and it is the natural artifact to put in the hands of the five "
      "hundred churches already in the network &mdash; who are a relationship, not yet a "
      "channel, and who need a small first transaction to become one. A calendar is also the "
      "most natural thing in the world to give away at a conference in February.")

    story.append(Spacer(1, 8))
    story.append(Band(
      "<b>One conflict to name.</b> Part Nine argues for coordinating before building, and the "
      "earlier recommendation on the ratio problem argued for building roughly 120 flagship "
      "kits &mdash; the top five per category &mdash; rather than all 5,155. Those are "
      "compatible but ordered: coordinate first, because the coordinates are what tell you "
      "<i>which</i> five per category deserve to be flagships. Building the 120 without the "
      "index means choosing them by intuition, and you will end up with 120 messages that are "
      "all <i>see it</i> and all New Testament.",
      S["tb"], bg=colors.HexColor("#f4f0e4"), bar=NAVY2))

    story.append(Spacer(1, 14))
    story.append(HRule(thick=1.4, space=4))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
      "Sources: SermonCentral&rsquo;s public browse taxonomy and library statistics, read "
      "August 2026. Scripture references follow the NIV versification. No sermon text, title or "
      "manuscript from any third-party library is reproduced in this document. Everything in "
      "Parts Two through Nine is original LifeTogether architecture.", S["note"]))


# ------------------------------------------------------------------ build
def build(path):
    doc = BaseDocTemplate(path, pagesize=letter,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=0.85 * inch,
                          title="The Master Preaching Index",
                          author="LifeTogether Ministries",
                          subject="Five-axis reference architecture for the Sermon Library")
    fr = Frame(MARGIN, 0.85 * inch, PW - 2 * MARGIN, PH - MARGIN - 0.85 * inch,
               id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[fr], onPage=cover_page),
        PageTemplate(id="inner", frames=[fr], onPage=inner_page),
    ])
    story = []
    front_matter(story)
    part_one(story)
    part_two(story)
    part_three(story)
    part_four(story)
    part_five(story)
    part_six(story)
    part_seven(story)
    part_eight(story)
    part_nine(story)
    doc.build(story)
    return path


if __name__ == "__main__":
    out = "/home/claude/Master-Preaching-Index.pdf"
    build(out)
    print("built", out, os.path.getsize(out), "bytes")
