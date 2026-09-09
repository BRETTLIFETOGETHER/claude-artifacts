# -*- coding: utf-8 -*-
from build_index import *

OPEN = "<font color='#c9a35c'><b>&#9702;</b></font>&nbsp;"

def part_three(story):
    head(story, "PART THREE  \u00b7  AXIS A",
         "The topical index",
         "Thirteen families rather than an alphabet. The alphabet is a finding aid; families "
         "are a planning aid, and you are selling planning.")

    para(story,
      "An A&ndash;Z list is the right structure for someone who already knows the word they "
      "want. It is the wrong structure for a pastor building a year, because it hides the two "
      "things he most needs to see: what sits next to what, and what he has not touched in "
      "eighteen months. These thirteen families are ordered from doctrine outward to culture "
      "and life-stage, and any preaching calendar that never leaves three of them is a "
      "diagnosable problem.",

      "Topics marked <font color='#c9a35c'><b>&#9702;</b></font> do not appear as browse "
      "categories in the public taxonomy. Sixty-two of them across the thirteen families. "
      "Read the clustering rather than the count.")
    story.append(Spacer(1, 4))

    n_open = 0
    for fam, defn, topics in TOPIC_FAMILIES:
        block = []
        block.append(Paragraph(fam.upper(), S["h3"]))
        block.append(Paragraph("<i>%s</i>" % defn, S["note"]))
        cells = []
        for t in topics:
            if t.startswith("*"):
                n_open += 1
                cells.append(Paragraph(OPEN + t[1:], S["topic"]))
            else:
                cells.append(Paragraph(t, S["topic"]))
        # 3 columns
        cols = 3
        rowsn = (len(cells) + cols - 1) // cols
        grid = []
        for r in range(rowsn):
            row = []
            for c in range(cols):
                i = c * rowsn + r
                row.append(cells[i] if i < len(cells) else "")
            grid.append(row)
        t = Table(grid, colWidths=[2.34 * inch] * 3)
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 1.2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
        ]))
        block.append(t)
        block.append(Spacer(1, 5))
        story.append(KeepTogether(block))

    story.append(Spacer(1, 6))
    story.append(Band(
      "<b>Where the openings cluster.</b> Of the sixty-two marked topics, the heaviest "
      "concentrations fall in Money, Work and Stewardship; Family, Marriage and Household; "
      "Seasons of Life; and Culture, Doubt and Contested Questions. Those four families are, "
      "almost exactly, the territory of the Ron Blue work, Family Legacy by Design, the "
      "generosity line and the rising-categories research. The index is telling you the same "
      "thing your client list already tells you, which is a reasonable sign it is built right.",
      S["tb"]))
    story.append(PageBreak())


def part_four(story):
    head(story, "PART FOUR  \u00b7  AXIS B",
         "The books of the Bible",
         "All sixty-six, with what each one preaches, what it anchors on, and whether it wants "
         "to be a series.")

    para(story,
      "This is the axis where the incumbent is strongest and where your own illustration "
      "library currently sits at ten books out of sixty-six. Completing it is not a separate "
      "project from coordinating the index &mdash; it is the same job, and doing it once "
      "serves both. The series-potential column is the part that does not exist anywhere else: "
      "it converts a canonical list into a planning instrument, and roughly a third of these "
      "entries are the seed of a campaign you have not built.")
    story.append(Spacer(1, 4))

    for division, books in BOOKS:
        story.append(Paragraph(division.upper(), S["h3"]))
        rows = [[Paragraph("BOOK", S["th"]), Paragraph("CH", S["th"]),
                 Paragraph("DOMINANT PREACHING THEMES", S["th"]),
                 Paragraph("ANCHOR PASSAGES", S["th"])]]
        for name, ch, genre, themes, anchors, series in books:
            rows.append([
                Paragraph("<b>%s</b><br/><font size=7 color='#6b7484'>%s</font>" % (name, genre), S["tb"]),
                Paragraph(str(ch), S["tb"]),
                Paragraph(themes, S["tb"]),
                Paragraph(anchors, S["tbi"])])
            rows.append(["", "",
                Paragraph("<font color='#8a6d2f'><b>Series &rarr;</b></font> " + series, S["tb"]),
                ""])
        t = Table(rows, colWidths=[1.12 * inch, 0.3 * inch, 3.15 * inch, 2.45 * inch],
                  repeatRows=1)
        cmds = [("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("ALIGN", (1, 1), (1, -1), "CENTER")]
        for i in range(1, len(rows)):
            if i % 2 == 1:  # data row
                cmds.append(("BOTTOMPADDING", (0, i), (-1, i), 1.5))
                cmds.append(("SPAN", (0, i), (0, i + 1)))
                cmds.append(("SPAN", (1, i), (1, i + 1)))
                cmds.append(("SPAN", (3, i), (3, i + 1)))
            else:  # series row
                cmds.append(("TOPPADDING", (0, i), (-1, i), 0))
                cmds.append(("LINEBELOW", (0, i), (-1, i), 0.4, RULE))
                if (i // 2) % 2 == 1:
                    cmds.append(("BACKGROUND", (0, i - 1), (-1, i), CREAM2))
        t.setStyle(TableStyle(cmds))
        story.append(t)
        story.append(Spacer(1, 9))
    story.append(PageBreak())


def part_five(story):
    head(story, "PART FIVE  \u00b7  AXIS C",
         "The anchor passage index",
         "One hundred and fifty passages, grouped by what they do rather than where they sit.")

    para(story,
      "Canonical order is how you find a passage you already have in mind. Functional grouping "
      "is how you find the passage a situation requires, which is the actual question in a "
      "pastor&rsquo;s head at the moment of need &mdash; a family has lost a child, a couple is "
      "separating, a congregation is frightened, a young leader is being sent. No public sermon "
      "index sorts this way, and it is the single most useful reorganisation in this document.",

      "The one-line note on each entry names the function, not the content. A pastor scanning "
      "for a funeral text does not need to be told what Romans 8 says.")
    story.append(Spacer(1, 4))

    for group, items in PASSAGE_GROUPS:
        block = [Paragraph(group.upper(), S["h3"])]
        rows = []
        for ref, fn in items:
            rows.append([Paragraph("<b>%s</b>" % ref, S["tb"]), Paragraph(fn, S["tbi"])])
        t = Table(rows, colWidths=[1.55 * inch, 5.47 * inch])
        cmds = [("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 2.6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
                ("LINEBELOW", (0, 0), (-1, -1), 0.35, RULE)]
        for i in range(len(rows)):
            if i % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), CREAM2))
        t.setStyle(TableStyle(cmds))
        block.append(t)
        block.append(Spacer(1, 4))
        story.append(KeepTogether(block))
    story.append(PageBreak())


def part_six(story):
    head(story, "PART SIX  \u00b7  AXIS D",
         "Occasion and season",
         "Four registers, deliberately kept apart. Fusing them is the mistake the public "
         "taxonomy makes.")

    para(story,
      "The Christian year is campaign-shaped: Advent and Lent already carry a four-week and a "
      "forty-day frame that the culture has done the work of establishing. The civil calendar "
      "is message-shaped, mostly single Sundays with sharp attendance consequences. Church-life "
      "occasions are strategy-shaped, and they are where the real product lives &mdash; nobody "
      "else is helping a pastor run a baptism Sunday or a group launch. Pastoral occasions are "
      "care-shaped and largely unplannable, which is exactly why the resources for them have to "
      "be ready in advance.")
    story.append(Spacer(1, 4))

    story.append(Paragraph("REGISTER 1 &mdash; THE CHRISTIAN YEAR", S["h3"]))
    rows = [[Paragraph("SEASON", S["th"]), Paragraph("WHEN", S["th"]),
             Paragraph("THEMES", S["th"]), Paragraph("PLANNING NOTE", S["th"])]]
    for a, b, c, d in CHRISTIAN_YEAR:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tbi"]),
                     Paragraph(c, S["tb"]), Paragraph(d, S["tb"])])
    story.append(tbl(rows, [0.95 * inch, 1.2 * inch, 1.85 * inch, 3.02 * inch]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("REGISTER 2 &mdash; THE CIVIL AND CULTURAL CALENDAR", S["h3"]))
    rows = [[Paragraph("DATE", S["th"]), Paragraph("THEMES", S["th"]),
             Paragraph("PLANNING NOTE", S["th"])]]
    for a, b, c in CIVIL_CALENDAR:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tb"]),
                     Paragraph(c, S["tbi"])])
    story.append(tbl(rows, [1.5 * inch, 2.2 * inch, 3.32 * inch]))
    story.append(PageBreak())

    story.append(Paragraph("REGISTER 3 &mdash; CHURCH-LIFE OCCASIONS", S["h3"]))
    story.append(Paragraph(
      "<i>The register nobody else indexes, and the one your product is actually built "
      "for.</i>", S["note"]))
    rows = [[Paragraph("OCCASION", S["th"]), Paragraph("THE DESIGN NOTE", S["th"])]]
    for a, b in CHURCH_OCCASIONS:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tb"])])
    story.append(tbl(rows, [1.85 * inch, 5.17 * inch]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("REGISTER 4 &mdash; PASTORAL OCCASIONS", S["h3"]))
    rows = [[Paragraph("OCCASION", S["th"]), Paragraph("APPROACH AND ANCHOR TEXTS", S["th"])]]
    for a, b in PASTORAL_OCCASIONS:
        rows.append([Paragraph("<b>%s</b>" % a, S["tb"]), Paragraph(b, S["tb"])])
    story.append(tbl(rows, [1.85 * inch, 5.17 * inch]))
    story.append(Spacer(1, 10))

    story.append(Band(
      "<b>The product hiding in this part.</b> Register 1 and Register 2, laid over fifty-two "
      "weeks with the church-life occasions slotted in, is a preaching calendar. It requires no "
      "sermon content, competes with nothing else in your line, and is the cheapest possible "
      "proof that the strategy claim is real &mdash; a pastor can hold it, see his whole year, "
      "and understand in thirty seconds what you mean by <i>they come for a sermon and leave "
      "with a strategy.</i> See Part Nine.", S["tb"]))
    story.append(PageBreak())


def part_seven(story):
    head(story, "PART SEVEN  \u00b7  AXIS E",
         "The people of Scripture",
         "Seventy figures, each with the angle it carries. The incumbent stops at about thirty.")

    para(story,
      "Narrative is how most congregations actually receive teaching, and character is the "
      "handle a listener remembers when the outline has gone. This axis also happens to be the "
      "one that converts most cleanly into children&rsquo;s and student editions of the same "
      "big idea, which is the piece of your product ladder nobody else attempts.")
    story.append(Spacer(1, 4))

    for label, tag in [("OLD TESTAMENT", "OT"), ("NEW TESTAMENT", "NT")]:
        story.append(Paragraph(label, S["h3"]))
        rows = []
        for name, t, angle in PEOPLE:
            if t != tag:
                continue
            rows.append([Paragraph("<b>%s</b>" % name, S["tb"]), Paragraph(angle, S["tbi"])])
        t2 = Table(rows, colWidths=[1.55 * inch, 5.47 * inch])
        cmds = [("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 2.6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
                ("LINEBELOW", (0, 0), (-1, -1), 0.35, RULE)]
        for i in range(len(rows)):
            if i % 2 == 1:
                cmds.append(("BACKGROUND", (0, i), (-1, i), CREAM2))
        t2.setStyle(TableStyle(cmds))
        story.append(t2)
        story.append(Spacer(1, 8))
    story.append(PageBreak())
