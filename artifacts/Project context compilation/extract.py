#!/usr/bin/env python3
"""Extract all Family Legacy by Design project sources into clean, paste-ready text."""

import os, re, zipfile, json

SRC = "/mnt/project"
OUT = "/mnt/user-data/outputs/project-sources"
os.makedirs(OUT, exist_ok=True)

# (source filename, output filename, human title, kind)
FILES = [
    ("Workshop_Transcripts_.pdf",            "01_Workshop_Transcripts.md",
     "Workshop Transcripts", "text"),
    ("Training_Manual-bleed-4_27.pdf",       "02_Training_Manual.md",
     "Training Manual", "text"),
    ("FLBD_Workbook_Legend.docx",            "03_Workbook_Legend.md",
     "Workbook Legend", "text"),
    ("Coaching_Book_6x9_4_27.pdf",           "04_Coaching_Book.md",
     "Coaching Book — Family Legacy Coaching by Design", "text"),
    ("Family_Book-6X9_2_5_26.pdf",           "05_Family_Book.md",
     "Family Book — Family Legacy by Design", "text"),
    ("FLBD_Coaching_BookPaperback427.pdf",   "06_Coaching_Book_Cover.md",
     "Coaching Book Cover Copy", "zip"),
    ("Family_Book_Cover_6x9_2_5_26.pdf",     "07_Family_Book_Cover.md",
     "Family Book Cover Copy", "zip"),
]


def clean(text):
    """Normalise line endings and collapse runaway blank lines. No content removed."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")          # non-breaking spaces
    text = re.sub(r"[ \t]+\n", "\n", text)      # trailing whitespace
    text = re.sub(r"\n{4,}", "\n\n\n", text)    # cap blank runs
    return text.strip() + "\n"


def read_text(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8", errors="replace")


def read_zip(path):
    z = zipfile.ZipFile(path)
    manifest = json.loads(z.read("manifest.json").decode("utf-8", "replace"))
    parts = []
    for page in manifest.get("pages", []):
        tp = page.get("text", {}).get("path")
        if tp:
            parts.append(z.read(tp).decode("utf-8", "replace"))
    return "\n\n".join(parts)


report = []
combined = []

combined.append(
    "# FAMILY LEGACY BY DESIGN — COMPLETE SOURCE ARCHIVE\n\n"
    "All project source documents, extracted to plain text.\n"
    "© Tom Conway & Brett Eastman. Family Legacy by Design / Lifetogether.\n\n"
    "**Source hierarchy (highest authority first):** "
    "Video transcripts → Training Manual & Workbook Legend → "
    "Coaching Book & Family Book → Workshop Transcripts\n\n"
    "---\n"
)

for src, dst, title, kind in FILES:
    path = os.path.join(SRC, src)
    raw = read_zip(path) if kind == "zip" else read_text(path)
    body = clean(raw)

    words = len(body.split())
    chars = len(body)

    header = (
        f"# {title}\n\n"
        f"*Source file: `{src}`*\n"
        f"*Approx. {words:,} words*\n\n"
        "---\n\n"
    )

    with open(os.path.join(OUT, dst), "w", encoding="utf-8") as f:
        f.write(header + body)

    combined.append(f"\n\n\n{'=' * 78}\n# {title}\n"
                    f"Source file: {src}\n{'=' * 78}\n\n{body}")

    report.append((title, dst, words, chars))

# Combined master file
with open(os.path.join(OUT, "00_ALL_SOURCES_COMBINED.md"), "w", encoding="utf-8") as f:
    f.write("".join(combined))

# Report
print(f"{'DOCUMENT':<48} {'WORDS':>9} {'CHARS':>10}")
print("-" * 70)
total_w = total_c = 0
for title, dst, w, c in report:
    print(f"{title[:47]:<48} {w:>9,} {c:>10,}")
    total_w += w
    total_c += c
print("-" * 70)
print(f"{'TOTAL':<48} {total_w:>9,} {total_c:>10,}")
print()
print("Files written to", OUT)
for fn in sorted(os.listdir(OUT)):
    size = os.path.getsize(os.path.join(OUT, fn))
    print(f"  {fn:<42} {size/1024:>8.0f} KB")
