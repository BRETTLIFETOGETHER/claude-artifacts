# -*- coding: utf-8 -*-
import io, json
import data as v1
import calendar_data as v2
import vol4_data as v4
import vol5_data as v5
import preview_data as pv
from master_content import DRAFTS, DELIVERY
from build_index2 import VOLUMES as IDX

# ---- explainer + experience lookup, keyed by category name ----
LOOK = {}
for vname, vfile, cats in IDX:
    for cn, anc, cc, note, expl, exper in cats:
        key = cn.replace("&amp;", "and").replace("&mdash;", "-").replace("&rsquo;", "'")
        LOOK[key] = (expl, exper, note)

def look(name):
    k = name.replace("&", "and").replace("'", "'")
    for kk in LOOK:
        if kk.lower().replace("'", "'") == k.lower():
            return LOOK[kk]
    # tolerant match on first word cluster
    for kk in LOOK:
        if kk.lower()[:14] == name.lower()[:14]:
            return LOOK[kk]
    return ("", "", "")

CATS = []

def add(name, vol, blurb, tracks, hinge=None, expl=None, exper=None):
    e, x, note = look(name)
    CATS.append({
        "n": name, "v": vol,
        "e": expl or e or blurb,
        "x": exper or x,
        "h": hinge,
        "t": [{"n": tn, "i": [[a, b] for a, b in items]} for tn, items in tracks],
    })

for name, blurb, items in v1.EASTER + v1.CHRISTMAS:
    add(name, "Easter and Christmas", blurb, [(None, items)])

for name, blurb, hinge, tracks in v2.LOCKS:
    add(name, "Calendar Locks", blurb, tracks, hinge)
for name, blurb, hinge, items in v2.STRATEGIC:
    add(name, "Strategic Weekends", blurb, [(None, items)], hinge)

for name, blurb, hinge, tracks in v4.CATS:
    add(name, "The Working Calendar", blurb, tracks, hinge)

for name, expl, exper, hinge, tracks in v5.CATS:
    add(name, "The Challenge Library", expl, tracks, hinge, expl, exper)

# new categories from this turn
add("10-Day Jumpstart", "New Formats",
    "Ten weekdays. Monday through Friday, twice, with the weekends left alone.",
    [("The John Edition, day by day", [(str(d) + ". " + t, r + " &mdash; " + s) for d, t, r, s in pv.JOHN10]),
     ("Twenty jumpstart editions", pv.JUMPSTART)],
    {"roll":"A two-week runway between a launch Sunday and a Celebration Sunday.",
     "give":"Journals and the printed jumpstart guide.",
     "gospel":"Short enough that a not-yet-believing spouse will do it alongside someone.",
     "act":"Take the journal, start Monday morning."},
    "Ten weekdays rather than fourteen days, because every daily plan dies on the weekend. Saturday scatters people and Sunday already carries a spiritual obligation, so a seven-consecutive-day plan is quietly asking for two acts of obedience it never named. Ten weekdays asks for the commute, the lunch break, or the ten minutes before the house wakes up.",
    "Hand out the printed journal on the launch Sunday with a tracker grid on page three. Then run the Celebration Sunday exactly fourteen days later, while the momentum is still live.")

add("Friends Day", "New Formats",
    "Two categories, not one: the messages preached on the day, and the messages that motivate the ask beforehand.",
    [("On the day &mdash; guest-facing", pv.FRIENDS_DAY),
     ("Before the day &mdash; motivating the ask", pv.FRIENDS_MOTIVATE)],
    {"roll":"A three-week runway, then the day itself, then the series that follows it.",
     "give":"Invite cards, bulletin inserts, and outreach production.",
     "gospel":"The highest invite density of the year. Preach for the guest who has not arrived yet.",
     "act":"Map your circles, write one name, send the text during the service."},
    "Most churches build the guest-facing message and skip the four weeks of congregational motivation that fill the room, then wonder why attendance looks the same. Friends Day is a runway, not a Sunday.",
    "Three weeks out, map the circles with the bulletin insert. Two weeks out, pray for the name. One week out, phones out during the service and send the text. Then preach to the person who came because somebody asked.")

SERMONS = []
for s in pv.SERMONS:
    d = dict(s)
    d["draft"] = DRAFTS.get(s["t"], [])
    SERMONS.append(d)

NTIT = sum(sum(len(t["i"]) for t in c["t"]) for c in CATS)
print("categories:", len(CATS), "titles:", NTIT, "sermons with drafts:",
      len([s for s in SERMONS if s["draft"]]))

DATA = {"cats": CATS, "sermons": SERMONS, "delivery": DELIVERY}
with io.open('/home/claude/work/master_payload.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(DATA))
print("payload bytes:", len(json.dumps(DATA)))
