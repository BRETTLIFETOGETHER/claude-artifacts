# -*- coding: utf-8 -*-
from build_index import *

def front_matter(story):
    # ---- COVER
    story.append(Spacer(1, 0.55 * inch))
    story.append(Paragraph("LIFETOGETHER MINISTRIES", S["cover_e"]))
    story.append(Spacer(1, 3))
    story.append(Paragraph("THE SERMON LIBRARY  \u00b7  THE PASTOR'S LIBRARY", S["cover_m"]))
    story.append(Spacer(1, 2.35 * inch))
    story.append(Paragraph("The Master<br/>Preaching Index", S["cover_t"]))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "A five-axis directory of topics, books, passages, occasions and people &mdash; "
        "with the public sermon-research taxonomy read as a benchmark, and the "
        "openings it leaves marked.", S["cover_s"]))
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph(
        "13 topic families &nbsp;&middot;&nbsp; 330 topics &nbsp;&middot;&nbsp; "
        "66 books &nbsp;&middot;&nbsp; 150 anchor passages<br/>"
        "60 occasions &nbsp;&middot;&nbsp; 70 people of Scripture &nbsp;&middot;&nbsp; "
        "7 formation outcomes &nbsp;&middot;&nbsp; 4 campaign hinges", S["cover_m"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "Reference architecture, version 1 &nbsp;&middot;&nbsp; August 2026 &nbsp;&middot;&nbsp; "
        "Internal working document", S["cover_m"]))
    story.append(NextPageTemplate("inner"))
    story.append(PageBreak())

    # ---- SOURCING NOTE
    head(story, "BEFORE YOU USE THIS",
         "What you asked for, and what actually exists",
         "Two corrections that matter before any of the rest of this is useful.")

    para(story,
      "You asked for SermonCentral&rsquo;s master directory &mdash; the file behind the index, with every "
      "category, title, theme, book and passage across three hundred thousand sermons. There is no such "
      "file to send. There is a browse interface, and behind it a proprietary database, and the gap "
      "between those two things is where this document lives.",

      "Start with the number, because it is the kind of figure that gets repeated in a founders "
      "conversation and then gets checked. SermonCentral&rsquo;s own pages say the library holds "
      "<b>over 160,000</b> pastor-contributed sermons, and that roughly <b>300 new sermons and "
      "illustrations arrive each week</b>. The 300,000 almost certainly comes from collapsing that "
      "weekly number into the total. The scale is still formidable and none of the strategy changes, "
      "but the number you use should be theirs. Where the comparison table in the master file carries "
      "300,000, it needs correcting.",

      "Then the corpus itself. Those sermons are the copyrighted work of the pastors who wrote them, "
      "licensed by Outreach, Inc., and their titles and manuscripts are not public metadata. I am not "
      "going to scrape them or hand you a directory of them, and on reflection you would not want one. "
      "Your entire positioning rests on the claim that a pastor should be preaching his own material "
      "and mining his own archive. A spreadsheet of someone else&rsquo;s titles sitting on your server "
      "contradicts the pitch and creates exposure in the one area &mdash; plagiarism &mdash; where the "
      "incumbent publishes a formal policy and would enjoy the fight.",

      "What <i>is</i> public, and genuinely instructive, is the shape of their index: which axes they "
      "sort by, what vocabulary they use, where they go deep, and where they simply stop. I read that "
      "structure directly. It is the benchmark this document is built against, and it turns out to be "
      "more useful than the corpus would have been, because an index is a statement of what a business "
      "is <i>for</i>.")

    story.append(Spacer(1, 4))
    story.append(Band(
      "<b>So this is not their directory. It is yours.</b> &nbsp;The five-axis reference architecture "
      "for the Sermon Library and the Pastor&rsquo;s Library, built out to the depth where it can "
      "actually be used &mdash; with the incumbent&rsquo;s structure named where it instructs, and the "
      "gaps marked where they exist.", S["tb"]))
    story.append(Spacer(1, 10))

    para(story,
      "One convention runs through the whole document. Where a topic in these pages does <b>not</b> "
      "appear as a browse category in the public taxonomy, it carries an open marker: "
      "<font color='#c9a35c'><b>&#9702;</b></font>. Read those marks as the map of what the incumbent "
      "does not index. There are 62 of them in Part Three alone, and they cluster in exactly the places "
      "you already build: money, household, legacy, formation practice, and the contested cultural "
      "questions that have arrived faster than a browse taxonomy can absorb them.")

    story.append(Spacer(1, 6))
    story.append(Band(
      "<b>Status.</b> Reference architecture, v1. Not a published asset, not approved copy, not a "
      "product. It is the spine a catalog hangs on, and it is only worth what gets coordinated against "
      "it &mdash; see Part Nine.", S["note"], bg=colors.HexColor("#f4f0e4"), bar=NAVY2))
    story.append(PageBreak())

    # ---- CONTENTS
    head(story, "CONTENTS", "What is in here")
    rows = [[Paragraph(a, S["th"]), Paragraph(b, S["th"]), Paragraph(c, S["th"])]
            for a, b, c in [("PART", "SECTION", "WHAT IT GIVES YOU")]]
    toc = [
     ("One", "The index you are being compared to",
      "The four public browse axes, the numbers, and the strategic read"),
     ("Two", "The five-axis architecture",
      "The seven axes, their units, and the two the incumbent cannot add"),
     ("Three", "Axis A &mdash; The topical index",
      "13 families, 330 topics, 62 openings marked"),
     ("Four", "Axis B &mdash; The books of the Bible",
      "All 66 with themes, anchor passages and series potential"),
     ("Five", "Axis C &mdash; The anchor passage index",
      "150 passages grouped by preaching function, not canonical order"),
     ("Six", "Axis D &mdash; Occasion and season",
      "The Christian year, the civil calendar, church life and pastoral moments"),
     ("Seven", "Axis E &mdash; The people of Scripture",
      "70 figures with the angle each one carries"),
     ("Eight", "The join",
      "How the axes cross-reference, with worked coordinates"),
     ("Nine", "Vision, Phase 1, next action",
      "What to do with this on Monday"),
    ]
    for a, b, c in toc:
        rows.append([Paragraph(a, S["tbb"]), Paragraph(b, S["tbb"]),
                     Paragraph(c, S["tb"])])
    story.append(tbl(rows, [0.62 * inch, 2.5 * inch, 3.9 * inch]))
    story.append(PageBreak())


def part_one(story):
    head(story, "PART ONE",
         "The index you are being compared to",
         "Their taxonomy is a retrieval system. That is not a criticism &mdash; it is the "
         "whole tell.")

    para(story,
      "The public browse structure sorts the library four ways, and it is worth being precise about "
      "them, because precision here is what makes the comparison credible rather than dismissive.")

    rows = [[Paragraph("AXIS", S["th"]), Paragraph("HOW IT IS BUILT", S["th"]),
             Paragraph("DEPTH", S["th"])]]
    for a, b, c in [
      ("Topic", "An A&ndash;Z browser with a featured shortlist per letter and a full list "
       "behind a <i>View All</i>. Vocabulary is single-concept and mostly noun-form: Faith, "
       "Grace, Marriage, Stewardship, Suffering.", "Broad; several hundred entries"),
      ("Bible Characters", "A separate alphabetical register of figures, from Abraham and "
       "Adam and Eve through to Zacchaeus, including paired entries such as Mary and Martha.",
       "Roughly 30 headline figures"),
      ("Holidays &amp; Seasonal", "A flat list mixing the Christian year with the American "
       "civil calendar &mdash; Advent and Ash Wednesday sitting alongside Labor Day, Halloween "
       "and September 11.", "About 21 entries"),
      ("Books of the Bible", "All 66, Old and New Testament, each linking to sermons keyed "
       "to that book. This is the most complete axis they have.", "66 of 66"),
    ]:
        rows.append([Paragraph(a, S["tbb"]), Paragraph(b, S["tb"]), Paragraph(c, S["tbi"])])
    story.append(tbl(rows, [1.05 * inch, 4.35 * inch, 1.62 * inch]))
    story.append(Spacer(1, 9))

    para(story,
      "Behind those four sit secondary filters rather than axes: contributor, denomination, "
      "sermon type (which is where Youth and PRO material is segregated), language, and a "
      "lectionary and liturgical calendar for the traditions that preach the readings. Around "
      "them orbit sibling catalogs &mdash; sermon series, series kits, premium kits, "
      "illustrations, collections, preaching articles, and a substantial media library of "
      "video illustrations, countdowns, motion backgrounds, preaching slides and social "
      "graphics.",

      "Concede what deserves conceding. The book axis is complete, the character axis is a "
      "genuinely good idea most catalogs skip, and the topical vocabulary is broad enough that "
      "a pastor looking for something on forgiveness at nine o&rsquo;clock on a Thursday will "
      "find it in under a minute. That is a well-built retrieval system, and the AI tooling "
      "layered on top of it &mdash; outline generation, a research assistant, a funeral-sermon "
      "helper &mdash; means the phrase <i>&ldquo;custom, with AI&rdquo;</i> is not, on its own, "
      "a differentiator you can claim.")

    story.append(Spacer(1, 3))
    story.append(Band(
      "Here is the read, and it is structural rather than competitive: <b>every axis they have is "
      "a retrieval axis.</b> Topic, character, holiday and book all answer one question &mdash; "
      "<i>help me find a message.</i> Not one of them answers what happens after it. There is no "
      "column for the outcome the message is supposed to produce, no column for the church&rsquo;s "
      "own season as distinct from the calendar&rsquo;s, and no column for what the message rolls "
      "into. The index is built for a pastor at a desk on Thursday, and it stops when he stands up.",
      S["tb"]))
    story.append(Spacer(1, 10))

    para(story,
      "That is the literal, structural version of the line you already use: <i>they have proven "
      "sermons, we have proven strategy.</i> An index is a confession of purpose. Theirs confesses "
      "that the message is the product. Yours has to confess that the week is.",

      "Three narrower observations are worth carrying into the build. The first is that their "
      "seasonal axis fuses the Christian year and the civil calendar into one undifferentiated "
      "list, which is fine for browsing and useless for planning &mdash; a pastor building next "
      "year cannot see that Advent and Lent are campaign-shaped and Labor Day is a single "
      "message. The second is that the character axis stops at roughly thirty figures, which "
      "leaves most of the narrative Old Testament unindexed as story even though narrative is "
      "how the majority of congregations actually receive teaching. The third is the one with "
      "the shortest shelf life: their topical vocabulary lags the culture. It carries "
      "Homosexuality but not deconstruction, not loneliness, not attention, not artificial "
      "intelligence, and not men and purpose. A community-contributed taxonomy grows by "
      "accretion, and accretion is slow. That lag is a real and temporary opening, and it "
      "closes the moment someone there decides to curate rather than accumulate.")
    story.append(PageBreak())


def part_two(story):
    head(story, "PART TWO",
         "The five-axis architecture",
         "Five axes match or exceed what exists publicly. Two more are yours, and they are the "
         "reason the index becomes a routing engine rather than a catalog.")

    para(story,
      "The seven columns below are the whole proposal. Any message, session, campaign or "
      "devotional in your library can be located on all seven, and once it is, the library "
      "stops being a list and starts being a system that can answer questions nobody has "
      "asked it yet.")

    rows = [[Paragraph("AXIS", S["th"]), Paragraph("UNIT", S["th"]),
             Paragraph("IN THIS DOCUMENT", S["th"]),
             Paragraph("THE QUESTION IT ANSWERS", S["th"])]]
    for a, b, c, d in [
      ("A &nbsp;Topic", "Topic within a family", "13 families, 330 topics",
       "What is this about?"),
      ("B &nbsp;Book", "Book of the Bible", "66 of 66, with profiles",
       "Where does it live in Scripture?"),
      ("C &nbsp;Passage", "Anchor passage", "150, grouped by function",
       "What text carries it?"),
      ("D &nbsp;Occasion", "Season or occasion", "4 registers, ~60 entries",
       "When does it land hardest?"),
      ("E &nbsp;People", "Figure of Scripture", "70, with angles",
       "Whose story tells it?"),
      ("F &nbsp;Outcome", "Formation outcome", "7 &mdash; the transformation process",
       "What is different by Tuesday?"),
      ("G &nbsp;Hinge", "Campaign hinge", "4 &mdash; rolls into, giving, gospel, call to action",
       "What does it roll into?"),
    ]:
        rows.append([Paragraph(a, S["tbb"]), Paragraph(b, S["tb"]),
                     Paragraph(c, S["tb"]), Paragraph(d, S["tbi"])])
    story.append(tbl(rows, [1.05 * inch, 1.35 * inch, 1.85 * inch, 2.77 * inch]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("THE TWO AXES THAT ARE NOT THEIRS TO ADD", S["h3"]))
    para(story,
      "Axis F carries the seven steps you already named and refuse to call an arc: <b>see it, "
      "sit with it, own it, do it, share it, deepen it, bring it back.</b> Tagging a message "
      "with the step it is designed to produce is a small act of discipline with an outsized "
      "consequence, because the moment the column exists you can see the imbalance. My "
      "expectation, and it is worth testing against the eight built messages before you trust "
      "it, is that the library will run heavy on <i>see it</i> and <i>sit with it</i> and go "
      "nearly empty on <i>share it</i> and <i>bring it back</i> &mdash; which is the same "
      "diagnosis you would give most preaching in America, now visible as a count rather than "
      "an opinion.",

      "Axis G carries the campaign hinge: rolls into, giving, gospel, call to action. It is the "
      "column that turns a standalone message into a component. Your own standing rule &mdash; "
      "<i>always ask for the next step in the current step</i> &mdash; is unenforceable without "
      "it, because you cannot audit a rule you have not stored.",

      "Neither of these is an axis the incumbent can bolt on, and that is worth saying plainly "
      "rather than triumphantly. Their content is contributed by thousands of pastors who have "
      "no shared formation framework and no reason to adopt one. An outcome column requires a "
      "point of view about what preaching is for, applied consistently across every item in the "
      "catalog. Community contribution and editorial consistency pull in opposite directions. "
      "They chose scale, which is a legitimate choice and the reason they have 160,000 sermons "
      "and you have 8 built ones. You are choosing coherence, which is the only trade that "
      "makes the ratio survivable.")
    story.append(PageBreak())
