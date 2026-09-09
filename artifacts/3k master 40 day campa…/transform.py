# -*- coding: utf-8 -*-
import re, copy
from data import CATEGORIES as MASTER

STRIP_SUFFIXES = [
    " Journey", " Challenge", " Experience", " Adventure", " Plan", " Project",
    " Reset", " Path", " Companion", " Primer", " Conversation"
]

def extract_theme(title):
    """Pull the core theme phrase out of a 40-day title, stripping day-scaffolding."""
    t = title
    # Colon-based titles: "Hook: A 40-Day Journey to Outcome" -> return hook (and outcome separately)
    if ":" in t:
        hook, rest = t.split(":", 1)
        rest = rest.strip()
        m = re.search(r"to (.+)$", rest, re.IGNORECASE)
        outcome = m.group(1).strip().rstrip(".") if m else None
        return hook.strip(), outcome
    # "The 40-Day X Journey/Challenge/..."
    m = re.match(r"The 40-Day (.+)", t)
    if m:
        rest = m.group(1)
        for suf in STRIP_SUFFIXES:
            if rest.endswith(suf):
                rest = rest[: -len(suf)]
                break
        return rest.strip(), None
    # "40 Days of X" / "40 Days to X"
    m = re.match(r"40 Days (?:of|to) (.+)", t)
    if m:
        return m.group(1).strip(), None
    return t, None

def convert_direct(title, day_word):
    """Straightforward day-count swap for Direct-formula titles."""
    t = title
    t = t.replace("40 Days of", f"{day_word} of")
    t = t.replace("40 Days to", f"{day_word} to")
    t = t.replace("40 Days", day_word)
    return t

def convert_journey(title, day_label, journey_word):
    t = title.replace("The 40-Day", f"The {day_label}")
    # normalize trailing journey-word if requested (e.g., Challenge for 7-day file)
    return t

def convert_promise(title, day_label):
    t = title.replace("A 40-Day Journey", f"A {day_label} Journey")
    return t

def build_duration_categories(day_word, day_label, formula_overrides=None):
    """
    day_word: e.g. '7 Days' (for Direct titles: '40 Days of X' -> '7 Days of X')
    day_label: e.g. '7-Day' (for Journey/Promise titles: 'A 40-Day Journey' -> 'A 7-Day Journey')
    formula_overrides: optional dict mapping formula name -> replacement word for "Journey"
    """
    out = []
    for cat in MASTER:
        new_cat = {
            "roman": cat["roman"], "name": cat["name"], "tag": cat["tag"],
            "tagline": cat["tagline"], "description": cat["description"],
            "titles": []
        }
        for (title, formula, desc) in cat["titles"]:
            t = title
            t = t.replace("40 Days of", f"{day_word} of")
            t = t.replace("40 Days to", f"{day_word} to")
            t = t.replace("The 40-Day", f"The {day_label}")
            t = t.replace("A 40-Day Journey", f"A {day_label} Journey")
            t = t.replace("40-Day", day_label)
            t = t.replace("40 Days", day_word)
            if formula_overrides:
                for old, new in formula_overrides.items():
                    t = t.replace(old, new)
            new_cat["titles"].append((t, formula, desc))
        out.append(new_cat)
    return out

def build_catalytic_sundays(limit_per_category=17):
    """Standalone single-Sunday titles derived from the 40-day master themes.
    Dedupes within each category (Direct/Journey formulas often share a theme word),
    pulling further into the category's list as needed to reach the target count."""
    out = []
    for cat in MASTER:
        new_cat = {
            "roman": cat["roman"], "name": cat["name"], "tag": cat["tag"],
            "tagline": cat["tagline"], "description": cat["description"],
            "titles": []
        }
        seen = set()
        for (title, formula, desc) in cat["titles"]:
            if len(new_cat["titles"]) >= limit_per_category:
                break
            hook, outcome = extract_theme(title)
            if formula in ("Promise", "Single-Word"):
                sunday_title = hook
                blurb = f"One catalytic Sunday on {outcome}" if outcome else desc
            else:
                sunday_title = f"The {hook} Sunday"
                blurb = desc
            key = sunday_title.lower()
            if key in seen:
                continue
            seen.add(key)
            new_cat["titles"].append((sunday_title, "Big Sunday", blurb))
        out.append(new_cat)
    return out

if __name__ == "__main__":
    seven = build_duration_categories("7 Days", "7-Day", {"Journey":"Challenge"})
    print("7-day sample:", seven[0]["titles"][:4])
    twentyone = build_duration_categories("21 Days", "21-Day", {"Journey":"Experience"})
    print("21-day sample:", twentyone[0]["titles"][:4])
    thirty = build_duration_categories("30 Days", "4-Week")
    print("30-day sample:", thirty[0]["titles"][:4])
    sundays = build_catalytic_sundays()
    print("sunday sample:", sundays[0]["titles"][:6])
    print("sunday total:", sum(len(c["titles"]) for c in sundays))
