# -*- coding: utf-8 -*-
import copy
from data import CATEGORIES as MASTER40
from transform import extract_theme

# Categories flagged as giving a pastor a competitive "edge right now" —
# addressing live cultural conversations most churches have no ready answer for.
EDGE_CATEGORIES = {
    "XXIX": "AI is the single most-discussed topic in American life with almost no pastoral guidance attached to it. A church running this series first, in its city, owns the conversation.",
    "XXVIII": "The deconstruction/doubt conversation is already happening in your congregation, mostly in private or on someone else's podcast. Naming it from the stage first is the edge.",
    "XXVI": "Anxiety is the most commonly named felt need in American church life right now, and most churches still only address it pastorally, not practically. This series does both.",
    "XXVII": "Grief support is usually a ministry, not a series. Making it a small group curriculum signals the church will go there with people, not just refer them out.",
    "XXV": "Identity confusion, driven by social comparison, is arguably the defining discipleship problem for under-40s right now. Most churches are still running 2015-era self-esteem content.",
}

# Video-companion recommendation logic — grounded in the earlier Small Group
# Finder/Builder strategy conversation: felt-need, cultural-moment topics now
# carry a video-first market expectation; classic discipleship formation topics
# perform fine print-only.
VIDEO_RECOMMENDED_CATEGORIES = {
    "XXV", "XXVI", "XXVII", "XXVIII", "XXIX",  # the 5 edge categories
    "IV", "XII", "XIII",  # Freedom/Breakthrough, Healing, Family — high felt-need, video expected
}

def sg_title_from_forty(title, formula):
    """Convert a 40-day title into a 6-session small group series title."""
    hook, outcome = extract_theme(title)
    if formula in ("Promise", "Single-Word"):
        if outcome:
            return f"{hook}: A 6-Session Series to {outcome}"
        return f"{hook}: A 6-Session Small Group Series"
    else:
        return f"{hook}: A 6-Session Small Group Series"

def build_small_group_categories():
    out = []
    for cat in MASTER40:
        new_cat = {
            "roman": cat["roman"], "name": cat["name"], "tag": cat["tag"],
            "tagline": cat["tagline"], "description": cat["description"],
            "is_edge": cat["roman"] in EDGE_CATEGORIES,
            "edge_note": EDGE_CATEGORIES.get(cat["roman"]),
            "video_recommended": cat["roman"] in VIDEO_RECOMMENDED_CATEGORIES,
            "titles": []
        }
        seen = set()
        for (title, formula, desc) in cat["titles"]:
            sg_title = sg_title_from_forty(title, formula)
            key = sg_title.lower()
            if key in seen:
                continue
            seen.add(key)
            new_cat["titles"].append((sg_title, "6-Session Series", desc))
        out.append(new_cat)
    return out

if __name__ == "__main__":
    cats = build_small_group_categories()
    total = sum(len(c["titles"]) for c in cats)
    print("Categories:", len(cats), "Total series:", total)
    edge = [c for c in cats if c["is_edge"]]
    print("Edge categories:", [c["name"] for c in edge])
    print("Sample:", cats[0]["titles"][:3])
    print("Sample edge:", [c for c in cats if c["roman"]=="XXIX"][0]["titles"][:3])
