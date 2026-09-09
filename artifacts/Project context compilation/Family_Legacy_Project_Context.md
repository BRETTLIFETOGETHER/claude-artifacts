# FAMILY LEGACY BY DESIGN — PROJECT CONTEXT

**Prepared for:** Brett Eastman
**Purpose:** Complete working context for the Family Legacy by Design publishing platform. Paste into project instructions, a new project, a collaborator brief, or a handoff document.
**Last assembled:** August 8, 2026

---

## 1. WHO AND WHAT

**Family Legacy by Design** is a publishing platform and certification ecosystem co-founded by **Brett Eastman** and **Tom Conway**, developed through **Lifetogether Ministries** (Rancho Santa Margarita / San Juan Capistrano, CA).

**Core objective:** Scale Tom Conway's intellectual property — built across decades as a CPA, Kingdom Advisor, and multi-generational legacy coach — into a comprehensive curriculum catalog, advisor certification track, and web platform.

**Roles:**
- **Tom Conway** — primary teaching voice and subject matter expert. Background: Ernst & Young, Ronald Blue & Co., National Christian Foundation, Kingdom Advisors. Two co-authored books in the ecosystem.
- **Brett Eastman** — co-author, producer, project director. Leads curriculum and platform development.
- **Hannah** — designer and layout. Receives all markdown files for import into Google Docs.
- **Joel** — videographer. Has conducted shoots with Tom and Brett together.
- **John** — Hannah's brother; involved in working sessions.

**Web presence:** FamilyLegacyByDesign.com
**Imprint:** Lifetogether

---

## 2. AUDIENCES AND COMMERCIAL MODEL

Three audiences:

1. **Legacy Families** — high-capacity, multi-generational households
2. **Christian Advisors** — wealth advisors, estate planners, CPAs, family office professionals
3. **Affinity Groups** — pastors, business owners, attorneys, and others

Two primary revenue objectives:

1. Selling content directly to families
2. Certifying advisors as **Certified Family Legacy Coaches**

---

## 3. CORE FRAMEWORKS

**Five Areas of Legacy:**
Personal · Family · Financial · Business · Charitable

**Three Core Coaching Words:**
Clarity · Alignment · Communication

**The F.A.M.I.L.Y. Review** — the technical framework.

**The Family Legacy Review Questionnaire** — the relational instrument.

> **Disambiguation rule:** Always use the full name "Family Legacy Review Questionnaire" for the relational instrument. Never abbreviate it in a way that collides with the technical F.A.M.I.L.Y. Review.

---

## 4. SOURCE HIERARCHY

All builds follow this precedence order. Higher sources override lower ones on any conflict.

1. **Video transcripts** (highest authority)
2. **Training Manual** and **Workbook Legend**
3. **Coaching Book** and **Family Book**
4. **Workshop Transcripts** (lowest)

**Attribution rule:** Content attributed to Tom vs. Brett must be adjudicated by first-person content analysis and interjection patterns in the VTT files — not assumed.

**Project source files:**
- `FLBD_Workbook_Legend.docx`
- `Training_Manual-bleed-4_27.pdf`
- `Coaching_Book_6x9_4_27.pdf`
- `FLBD_Coaching_BookPaperback427.pdf`
- `Family_Book-6X9_2_5_26.pdf`
- `Family_Book_Cover_6x9_2_5_26.pdf`
- `Workshop_Transcripts_.pdf`

---

## 5. CURRENT STATE OF THE BUILD

### 5.1 Family Foundation Series — six books, largely complete

Three product layers exist for each of six titles:

| Layer | Description | File prefix |
|---|---|---|
| Teleprompter-ready scripts | Camera-ready teaching scripts | `SCRIPT_` |
| 30-day devotionals | Daily reading companion | `DEVO_` (assembled: `_COMPLETE`) |
| Participant guides | Session workbook | `GUIDE_` (client-ready: `_CLIENT`) |

**The six titles:**
1. Clarity
2. Alignment
3. Communication
4. Meetings
5. Next Generation
6. Foundation

### 5.2 Participant Guides — V2 design (rebuilt)

- Questions cut roughly by half
- One marked question per session
- Sessions open with the family's actual question
- Four alternate paths included for non-standard family situations
- Progress page at the back
- All guides client-ready with internal notes stripped

### 5.3 Web prototype — "The Family Legacy Collection"

Built as **nine self-contained HTML pages** plus an **all-in-one single-file bundle** with hash-based routing:

`index` · `campaigns` · `campaign` · `reader` · `assessment` · `intelligence` · `vision` · `pathways` · `about`

**Engine (`engine.js`):** Deterministically composes complete 40-day builds for **100 campaigns across ten domains** — seeded per campaign and per day so output is identical on every visit. **Hand-authored content always takes priority over generated content.**

### 5.4 Strategic documents completed

- **20-page white paper:** *"Create Once. Configure Many Ways."* — articulates the publishing platform strategy
- **Brochure-style HTML/PDF document** for Tom Conway
- **Assessment PDFs:** Heritage edition, Six Pillars edition, Private Client edition
- **Master notes and build map**
- **Multi-email campaign sequence** for the August workshop (built, not yet loaded into Mailchimp)

---

## 6. OPEN ITEMS AND UNRESOLVED DECISIONS

### Content gaps
- [ ] **Family Legacy by Design Assessment** — referenced in guides, not yet built
- [ ] **Family Health Survey** — referenced in guides, not yet built
- [ ] **Statistics attribution** — Williams & Preisser's *Preparing Heirs* for the 60/25 figures
- [ ] **Translation conflict** — NIV vs. NASB between the coaching Overview journey and all 18 family products

### Permissions
- [ ] **Tom's family members** — daughter Pamela; father and the Renault story; granddaughter the songwriter
- [ ] **Brett's own family story** — Clarity Session 4
- [ ] **Rick Warren foreword** — announced on cover; no text and no written permission in any source
- [ ] **Third-party permissions** — Edwin Friedman, Patrick Lencioni, Ron Blue, Dan Cathy

### Business decisions
- [ ] **Certification track** — requirements, sequence, and fees
- [ ] **Canonical price sheet** — pricing currently exists in two conflicting registers
- [ ] **Naming stack** — Christian Advisors Network vs. Family Legacy by Design / Intelligence™
- [ ] **Library vs. Catalog vs. Platform** — final naming resolution
- [ ] **Campaign format standard** — lock 30-day vs. 40-day

### Family edition conversion
Four architecture decisions must be resolved before converting advisor guides to family editions:
1. Target family member audience
2. Facilitator assumption
3. New video plans
4. Replacement for advisor-only Session 2

### Production
- [ ] Lighter ink version of PDF brochures for office printing

---

## 7. ROADMAP

**Documented build order (from strategy document):**

1. Advisor Discipleship Portal MVP
2. Legacy Family Toolkit
3. RIA Custom Edition
4. Generosity Partner Edition
5. Business Owner / Kingdom Capital Track

**Near-term milestone:** August 12–13 Southern California workshop targeting ~25 financial planners.

**In development:** "Next Generation" course, co-authored with Brett, foreword by Rick Warren.

---

## 8. EDITORIAL RULES

These are non-negotiable and apply to every deliverable.

1. **Titles and subtitles must be sourced verbatim from Tom's actual words in transcripts** — not generated from descriptions of his ideas. Grep transcripts for distinctive phrases before writing any title.
2. **Unattributed statistics are excluded, not softened.** The 90% vs. 97% generational wealth transfer failure rate conflict is unresolved; both figures are cut pending verifiable sourcing.
3. **Tom quotes in copy must be ≤15 words.**
4. **Shepherd-not-salesman tone** throughout.
5. **No pricing shown in client-facing materials.**
6. **"Extension not diversion"** is the governing positioning principle for the advisor model — never stated verbatim in client-facing copy.
7. **Scenario responses belong in the appendix**, behind a divider page, so advisors commit to an answer before reading — never embedded in session bodies.
8. **Solo advisor is the primary use case.** Every prompt carries a fork: team/pair discuss vs. solo write it down. Group use is an optional add-on, not the default frame.
9. **The certification spine is structural, not an afterthought.** Requirements, Session Completion Record, and Certificate of Module Completion belong in each module.
10. **Always use the full name "Family Legacy Review Questionnaire"** for the relational instrument.

**Standing QA checks (run after each major stage):**
- Em-dash check
- Fill-in-the-blank check
- Banned header check
- Source attribution check
- Cross-book title collision check (shared titles dictionary built by iterating all `DEVO_*.md` files; flag any title appearing in more than one book)

---

## 9. WORKFLOW PREFERENCES

**Pre-build audit before any writing.**
Read and cross-reference all source files, then deliver a structured report covering:
- Session verification
- Template mismatches
- Story inventory
- Framework mapping
- Scripture sourcing gaps
- Open decisions

Build only after Brett confirms the go signal.

**Autonomous operation once parameters are set.**
Brett gives a go signal and expects full delivery without approval gates between stages. Default decisions are made and flagged inline in one line. Questions are not held for Brett to answer.

**Rich drafting for Brett to cut, not expand.**
Deliver complete, full-length content. No placeholders. No stubs. No stopping for confirmation.

**Markdown as primary delivery format** — for pasting into Google Docs via Hannah. `.docx` as secondary.

**Sequential, volume-oriented workflow.**
Brett advances through the build order with short approvals ("next book") without extensive deliberation between items.

**Corrections applied immediately and tersely.**
Brett catches errors; acknowledge and apply without extended discussion.

**Outstanding items tracked explicitly** with a consistent open-items list surfaced at the end of each deliverable.

---

## 10. DESIGN SYSTEM AND TECHNICAL STANDARDS

### Brand palette and type
- Deep forest green brand palette with gold accent
- **Poppins** — base64-embedded via `fonts.css`
- **Inter** — Google Fonts
- **Playfair Display** and **Cormorant Garamond** — editorial and brochure pieces

### Web platform
- Source: `/home/claude/flc/`
- Build pipeline: `build.py`
- Output: `/mnt/user-data/outputs/family-legacy-collection/`
- **Multi-file HTML navigation only works when all files sit together.** The all-in-one bundle with hash-based routing resolves preview/sandbox breakage.

### PDF generation best practices
- `print_background=True`
- `prefer_css_page_size=True`
- `scale=0.85`
- Dedicated `@media print` block, separate from responsive queries
- `break-before: page` applied to individual semantic class names
- Fonts installed locally via `~/.fonts` + `fc-cache -f` **before** launching Playwright
- Visual QA via `pdftoppm -png` contact sheets
- Glyph-level content verification via `pdfplumber`

### File naming conventions
| Prefix / suffix | Meaning |
|---|---|
| `SCRIPT_` | Prompter-ready script |
| `DEVO_` | Devotional |
| `GUIDE_` | Participant guide |
| `_CLIENT` | Client-ready, internal notes stripped |
| `_COMPLETE` | Assembled devotional |

### Transcript processing
- VTT files extracted via bash tooling
- Python loops for targeted multi-file edits, with per-file hit counts reported
- Regex splits on session headers for per-session word counts

---

## 11. QUICK REFERENCE — WHAT TO ASK BEFORE STARTING ANY NEW BUILD

1. Which source tier governs this piece? (Transcripts win.)
2. Is the title sourced verbatim from Tom's words?
3. Are all statistics attributed? If not, cut them.
4. Solo advisor fork present on every prompt?
5. Certification spine included?
6. Scenario responses moved to appendix behind a divider?
7. Tom quotes under 15 words?
8. Any pricing accidentally left in client-facing copy?
9. Open-items list appended to the deliverable?

---

*End of context document.*
