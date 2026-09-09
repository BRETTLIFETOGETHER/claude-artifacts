# -*- coding: utf-8 -*-
"""Course summaries for the catalog drop-downs.

FLAGSHIP: hand-written summaries for the twenty 101 courses (the Year One row).
compose():  honest, varied placeholder summaries for the remaining 380.
"""

FLAGSHIP = {
"ST 101": "Most Christians have absorbed a great deal of doctrine without ever being taught how "
  "doctrine works, where it came from, how it was tested, or which parts are worth dividing over. "
  "This course does not teach the doctrines; the eleven after it do that. It teaches a person how "
  "to hold one, and it ends with the student teaching one to somebody else.",
"OT 101": "Thirty-nine books read as a single narrative rather than a pile of episodes. The course "
  "walks Eden to exile to return in twelve sessions, giving a student the map before any later "
  "course hands them a magnifying glass. Most people who have read the Old Testament for years "
  "have never once seen its shape.",
"NT 101": "From the manger to the last vision of Revelation, in one arc. Twelve sessions across the "
  "gospels, the spread of the church, the letters, and the ending, so a student knows where any "
  "passage sits before studying it closely. Pairs with OT 101, and most churches run them back to back.",
"CH 101": "Twenty centuries of Christians have already faced most of what your congregation is "
  "facing. This course introduces the church's memory as a discipleship resource rather than an "
  "academic subject, working through moments where the church got it right and several where it "
  "badly did not, asking each time what a believer today inherits.",
"HERM 101": "The single most useful course in the catalog, and the one most churches should teach "
  "first. Observation, interpretation, application, worked slowly on real passages until a student "
  "can walk into any text and know what to do next. Every other discipline assumes this skill. "
  "Almost no church teaches it.",
"APOL 101": "Not a course in winning arguments. It is for the member who freezes when a coworker "
  "asks about suffering, or when their own child asks whether the resurrection actually happened. "
  "Twelve sessions on giving a reason with gentleness and respect, including what to do when the "
  "honest answer is that you do not know.",
"HOM 101": "Written for the volunteer who has been asked to teach and is quietly terrified. The "
  "course separates calling from competence, then treats competence as a craft that can be learned: "
  "finding what the text says, building a lesson around it, and standing up to deliver it. Students "
  "teach twice during the twelve weeks.",
"PC 101": "Most failures in pastoral care are not failures of knowledge, they are failures of nerve. "
  "This course trains a member to show up in a hospital room, a kitchen, or a crisis without needing "
  "an answer first, and to know the difference between the care they can offer and the care that "
  "requires a licensed professional.",
"ETH 101": "Everyone is already living inside a story about what is real, what is good, and what a "
  "person is for. This course surfaces the story the student absorbed, sets it beside the Christian "
  "one, and introduces how Christians actually reason toward a decision when Scripture does not "
  "address the question directly.",
"LEAD 101": "The New Testament spends far more attention on what a leader is like than on what a "
  "leader does, which is inconvenient for anyone hoping for a management course. Twelve sessions on "
  "character, authority, and the particular temptations of ministry leadership, taken by elders, "
  "deacons, directors, and group leaders together.",
"BT 101": "Creation, fall, redemption, restoration, and the way every book takes its meaning from "
  "its place in that arc. Where OT 101 and NT 101 give the historical shape, this course gives the "
  "theological one. It is the course that most often makes a long-time reader say they had never "
  "seen the Bible whole before.",
"SF 101": "Christians are told to grow without often being told how growth happens. This course "
  "introduces formation as a lifetime of ordinary practices rather than a series of decisions, "
  "surveys what Scripture and the historic traditions have said about change, and has every student "
  "begin one practice and keep it for the full twelve weeks.",
"WOR 101": "Why the church gathers, who it gathers for, and why the order of a service is a "
  "theological statement whether anyone intended it or not. Useful for worship teams, but written "
  "for the member in the seats who has never been told what is supposed to be happening on a Sunday "
  "morning.",
"DIS 101": "Jesus defined the word disciple, and his definition is more demanding and more concrete "
  "than the one most churches operate with. This course works through that definition, then asks "
  "what a church would have to change if it took the definition seriously. The natural first course "
  "for anyone in group leadership.",
"EV 101": "Before technique, motive. A course on why Christians speak at all, written for members "
  "who have either stopped telling anyone or who only know how to do it badly. Twelve sessions on "
  "the theology underneath evangelism and the ordinary settings where it actually happens.",
"FAM 101": "Covenant rather than contract, and what follows from that difference in an ordinary "
  "week. Taken by married couples, by singles thinking about marriage, and by anyone who will one "
  "day sit with a couple in trouble. Sessions are built so spouses can take it in the same room "
  "without either one feeling exposed.",
"STW 101": "The one conviction that reorganizes everything else about money: none of it is yours. "
  "Twelve sessions on ownership and stewardship, and on what changes in a household when the "
  "question shifts from how much to give to how much to keep. Built on financial teaching "
  "LifeTogether has carried for two decades.",
"WR 101": "Christians frequently describe other faiths in terms their adherents would not recognize, "
  "which is both unkind and ineffective. This course teaches a member to represent a belief "
  "accurately before evaluating it, and to hold deep conviction and genuine fairness at the same "
  "time.",
"CT 101": "The command to love God with your mind has been quietly optional in a lot of churches. "
  "This course makes the case that it is not, introduces the habits of clear thinking, and gives "
  "students their first experience of reading something difficult slowly and in company rather "
  "than alone.",
"CULT 101": "Discernment used to be a churchy word. It is now closer to a survival skill. Twelve "
  "sessions on seeing the assumptions inside what you watch, scroll, and buy, and on teaching a "
  "household to do the same. The entry point to the disciplines newest to this catalog and most "
  "urgent in most churches.",
}

_FOUND = [
 "An entry point into {d}, with no prerequisite and no assumed background beyond a willingness to read. {s}.",
 "Foundation tier, written for the member who has never studied {d} formally. {s}.",
 "The kind of course a church can put a brand-new student into on week one. {s}. No prerequisite.",
]
_CORE = [
 "Core tier in {d}, assuming the Foundation row or equivalent grounding. {s}.",
 "The working middle of {d}, where most of the actual substance of the discipline sits. {s}.",
 "A core course. Heavier reading than the Foundation row, and the point at which depth-track students begin primary sources. {s}.",
]
_ADV = [
 "Advanced tier, with primary-source reading and a supervised assignment for students on the depth track. {s}.",
 "The far end of {d}, taken after the core row and expecting substantial reading. {s}.",
 "An advanced course, and one of the places this discipline earns the word seminary. {s}.",
]


def compose(discipline, tier, subtitle, index):
    """Honest placeholder summary for a course whose syllabus is not yet drafted."""
    bank = {"Foundation": _FOUND, "Core": _CORE, "Advanced": _ADV}[tier]
    d = discipline.replace("&amp;", "and")
    s = subtitle.rstrip(".")
    return bank[index % 3].format(d=d, s=s)
