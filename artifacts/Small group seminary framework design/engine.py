# -*- coding: utf-8 -*-
"""Wire a deterministic course engine into the catalog.

Classifies all 400 courses into six pedagogical archetypes, then replaces the
generic 'course frame' modal with a generated 12-lesson build sheet specific to
that course. Generation happens in the browser from template banks, the same
pattern as the campaign platform's engine.js.
"""
import re, json

SRC = "/mnt/user-data/outputs/smallgroupseminary-framework-and-catalog.html"
s = open(SRC, encoding="utf-8").read()

ROW = re.compile(r'data-code="([^"]+)" data-title="([^"]+)" data-sub="([^"]+)" data-disc="([^"]+)"')
rows = ROW.findall(s)
print("courses found:", len(rows))

BOOKS = ("genesis patriarchs exodus joshua judges kings chronicles torah psalms proverbs "
         "ecclesiastes job isaiah jeremiah lamentations ezekiel daniel twelve hosea malachi "
         "ezra nehemiah esther mark matthew luke john acts romans corinthians galatians "
         "ephesians philippians colossians pastoral hebrews james peter jude revelation "
         "confessions").split()

SKILL_HINTS = ("how to interpreting teaching preaching leading building writing asking praying "
               "listening structuring delivery reading study method toolkit getting developing "
               "coaching facilitat training discipling launching planning").split()

ISSUE_HINTS = ("ethics sexuality race justice politics government war creation care technology "
               "artificial intelligence pornography screens privacy divorce infertility poverty "
               "wealth doubt suffering deconstruction objection abuse addiction trauma "
               "immigration gender").split()

SURVEY_HINTS = ("story of survey whole bible one story why history matters world entered "
                "story of the storyline").split()


def archetype(code, title, sub, disc):
    t = (title + " " + sub).lower()
    d = disc.lower()
    if "practicum" in t or " lab" in t or t.endswith("lab"):
        return "P"
    for h in SURVEY_HINTS:
        if h in t:
            return "V"
    if ("old testament" in d or "new testament" in d):
        for b in BOOKS:
            if b in t:
                return "B"
    if "reading the confessions" in t:
        return "B"
    for h in SKILL_HINTS:
        if h in t:
            return "S"
    if d in ("homiletics and teaching", "hermeneutics and bible study methods",
             "evangelism and personal witness", "discipleship and small group multiplication"):
        return "S"
    for h in ISSUE_HINTS:
        if h in t:
            return "I"
    if d in ("christian ethics and worldview", "culture, technology and digital discernment",
             "world religions and comparative belief", "apologetics",
             "marriage, family and household discipleship", "money, work and vocation",
             "pastoral care and counseling"):
        return "I"
    if d in ("systematic theology", "biblical theology and redemptive history",
             "church history", "christian thought and the great tradition"):
        return "D"
    return "D"


assign = {}
counts = {}
for code, title, sub, disc in rows:
    a = archetype(code, title, sub, disc)
    assign[code] = a
    counts[a] = counts.get(a, 0) + 1
print("archetype spread:", counts)

# ---------------------------------------------------------------- archetypes
ARCH = {
"V": {"name": "Survey", "desc": "A whole corpus read as one shape before any part is studied closely.",
 "L": [
 ("Why the Whole Matters", "You cannot understand a part until you have seen the shape of the whole."),
 ("Beginnings", "Where a story starts determines what it is able to mean."),
 ("The Break", "Something goes wrong, and everything after is a response to it."),
 ("The Promise", "A commitment made early that the rest of the story is measured against."),
 ("The Long Middle", "What happens to a people while a promise is delayed."),
 ("The Turning", "The hinge the whole account swings on."),
 ("The Center", "The moment everything before was building toward."),
 ("The Community Formed", "What the turning produces in the people who witness it."),
 ("Outward", "The story stops being about one people and becomes about all of them."),
 ("The End Already Begun", "How it resolves, and the sense in which it has not yet."),
 ("Placing Any Passage on the Map", "Reading a single text inside the shape you now know."),
 ("Handing On the Shape", "Teaching the whole to somebody who has only ever seen pieces."),
 ]},
"B": {"name": "Single book", "desc": "One biblical book worked through from occasion to theology to teaching it.",
 "L": [
 ("Meeting the Book", "Who wrote it, to whom, and what occasion called it into existence."),
 ("The World Behind the Text", "The setting and the first hearers, before any application."),
 ("The Shape of the Argument", "Structure at a glance, so no passage is read orphaned."),
 ("Opening Movement", "Where the book begins, and what that beginning announces."),
 ("Second Movement", "The argument or the narrative gathers weight."),
 ("Third Movement", "Where the pressure builds and the stakes become clear."),
 ("The Hinge", "The passage the whole book turns on."),
 ("Fourth Movement", "Consequence and application worked out inside the book itself."),
 ("Closing Movement", "How it ends, and why it could not have ended otherwise."),
 ("The Passage People Stumble Over", "The hard text, addressed rather than avoided."),
 ("What This Book Alone Contributes", "The theology no other book supplies in the same way."),
 ("Teaching It", "Leading a group or a congregation through the whole book."),
 ]},
"D": {"name": "Doctrine", "desc": "A teaching traced from the question it answers to the pastoral use it serves.",
 "L": [
 ("Why This Matters on a Tuesday", "What changes in an ordinary life if this is true."),
 ("The Question Underneath", "The problem this teaching came into existence to answer."),
 ("Gathering the Texts", "Collecting the biblical data before drawing any conclusion."),
 ("The Texts That Complicate It", "Passages that resist the tidy version, held rather than resolved."),
 ("How the Church Said It", "Councils, confessions, and the language that was fought for."),
 ("The Classic Errors", "What was tried and rejected, and why each was attractive at the time."),
 ("Stating It Carefully", "Putting the affirmation into your own words without losing it."),
 ("Where Christians Disagree", "The live debate, each position in the words its holders would use."),
 ("What It Is Not", "Clearing away the distortions that attach themselves to this teaching."),
 ("At the Bedside", "How this doctrine functions in crisis, decision, and grief."),
 ("Living Inside It", "The practices that follow from believing it."),
 ("Handing It On", "Teaching this doctrine to one person who has never considered it."),
 ]},
"S": {"name": "Skill", "desc": "A competence built by practice, with two supervised attempts inside the twelve weeks.",
 "L": [
 ("What Becomes Possible", "Why this skill is worth twelve weeks of your life."),
 ("Watching It Done Well", "A worked example before any theory, taken apart together."),
 ("The First Move", "The step almost everybody skips, and what skipping it costs."),
 ("The Second Move", "Building on a foundation that is now actually there."),
 ("The Third Move", "Where most people plateau, and what carries you past it."),
 ("First Attempt", "Practising in front of the room, with a small assignment."),
 ("The Five Common Failures", "The mistakes that account for most poor work in this discipline."),
 ("Receiving Critique", "How to hear feedback without either collapsing or dismissing it."),
 ("Harder Material", "Applying the skill where it does not come naturally."),
 ("Doing It as Yourself", "Finding your own voice rather than imitating a model."),
 ("Second Attempt", "A full assignment, with everything from the first eleven weeks."),
 ("Teaching the Skill", "Reproduction is the real test of whether you have it."),
 ]},
"I": {"name": "Applied question", "desc": "A contested or practical question worked from the question itself to a posture.",
 "L": [
 ("Naming the Question", "What is actually being asked, underneath the argument people are having."),
 ("Why It Is Genuinely Hard", "The real difficulty rather than the caricature of the other side."),
 ("How We Got Here", "The history that produced the conversation we are now inside."),
 ("What Scripture Says Directly", "The texts that address this head on, read carefully."),
 ("What Scripture Assumes", "The larger convictions that bear on it without naming it."),
 ("The Positions, Fairly Stated", "Each view in the words its own holders would recognise."),
 ("Weighing Them", "Testing each position against the text, the tradition, and the fruit."),
 ("The Hard Cases", "Where every position, including yours, becomes uncomfortable."),
 ("Who This Costs", "The actual people affected by how the church answers this."),
 ("Conviction Without Contempt", "Holding a position while respecting the person who does not."),
 ("What Changes on Monday", "The practice that follows, in a real week."),
 ("Having the Conversation", "Talking about this with somebody who disagrees, and staying in the room."),
 ]},
"P": {"name": "Practicum", "desc": "Supervised practice with structured observation, attempts, and assessed evaluation.",
 "L": [
 ("The Framework", "What competent practice looks like, before anybody attempts it."),
 ("Structured Observation", "Watching a practitioner with a defined lens rather than an impression."),
 ("Debrief", "What you saw, what you missed, and what that reveals about your lens."),
 ("Preparation", "Planning a first attempt in writing, submitted before you do it."),
 ("First Attempt", "Doing it, with a supervisor present and taking notes."),
 ("First Feedback", "Structured critique from the supervisor, then from the room."),
 ("One Adjustment", "Naming a single thing to change, and changing only that."),
 ("Second Attempt", "The same work under harder circumstances."),
 ("Peer Review", "Critique from people carrying the same assignment as you."),
 ("Edge Cases", "The situations the framework does not cleanly cover."),
 ("Final Attempt", "Assessed work, evaluated by the supervisor and the ministry mentor."),
 ("Supervising Someone Else", "Running the first attempt for a person coming behind you."),
 ]},
}

MOVES = {
"V": ["Orient the room to {T} as a single shape rather than a collection",
      "Trace where the material in this session sits inside {D}",
      "Name what {S} contributes at this point in the arc"],
"B": ["Work the passage in front of the group rather than summarising it",
      "Show how this section serves the book's larger argument",
      "Connect it outward: what {D} does with this material"],
"D": ["State the claim plainly, then test it against the text",
      "Show where this teaching sits within {D} as a whole",
      "Trace one practical consequence of holding it, or of not"],
"S": ["Demonstrate the move before explaining it",
      "Break it into steps the group can attempt this week",
      "Name the failure mode this step is designed to prevent"],
"I": ["Establish what is genuinely at stake before taking any position",
      "Set the strongest form of each view side by side",
      "Bring it back to {D} and to a decision somebody has to make"],
"P": ["Review the framework against what actually happened",
      "Work one real case supplied by a participant",
      "Assign and prepare the next supervised attempt"],
}

QS = {
"V": ["Where did you previously think this material began, and what changes if it begins where the text puts it?",
      "What part of {T} have you never seen connected to the rest of it?"],
"B": ["What did the first hearers of this passage need that you do not, and the reverse?",
      "Where in this section were you tempted to skip ahead, and why?"],
"D": ["Where have you seen this doctrine held badly, and what did the bad version cost somebody?",
      "What would change in your week if you actually believed this rather than affirmed it?"],
"S": ["What is the specific thing about this skill that you are most afraid of getting wrong?",
      "Whose example are you unconsciously copying, and is it serving you?"],
"I": ["State the strongest version of the position you disagree with. Can you do it without sneering?",
      "Where does your own position become uncomfortable, and what do you do with that?"],
"P": ["What did you notice this week that you would not have noticed in week one?",
      "What is the one thing you are still avoiding in this practice?"],
}

EXS = {
"V": "Map this session's material onto a single page timeline you keep and add to for twelve weeks.",
"B": "Read the assigned section twice this week, once in a different translation, and note every question it raises.",
"D": "Write this doctrine in one paragraph, in your own words, for a fifteen-year-old. Bring it.",
"S": "Practise the move once this week on real material and bring what you produced, finished or not.",
"I": "Find someone who holds a different position and ask them to explain it. Listen only. Write half a page.",
"P": "Complete the assigned attempt or observation and submit your written reflection before the next session.",
}

# ---------------------------------------------------------------- JS payload
payload = {
  "assign": assign,
  "arch": {k: {"name": v["name"], "desc": v["desc"], "L": v["L"]} for k, v in ARCH.items()},
  "moves": MOVES, "qs": QS, "exs": EXS,
}

JS_ENGINE = """
<script>
var ENGINE = """ + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + """;

function fill(str, T, S, D){
  return str.replace(/\\{T\\}/g, T).replace(/\\{S\\}/g, S).replace(/\\{D\\}/g, D);
}

function buildSheet(code, title, sub, disc, status){
  var a = ENGINE.assign[code] || "D";
  var A = ENGINE.arch[a];
  var h = '<div class="mcode">'+code+' &nbsp;&middot;&nbsp; Generated build sheet</div>'+
    '<h3 id="mtitle">'+title+'</h3><p class="msub">'+sub+'</p>'+
    '<div class="genwarn"><b>Generated draft, not curriculum</b>'+
    'This twelve-lesson map was produced by the course engine from the title, subtitle, discipline '+
    'and course archetype. The structure is right and the specifics are thin, because specifics are '+
    'what the author pass and the faculty review supply. Treat it as the outline a writer starts '+
    'from, never as a course. ST 101 shows what the same sheet looks like after that work.</div>'+
    '<h5>Course profile</h5><p><b>Archetype:</b> '+A.name+'. '+A.desc+'<br>'+
    '<b>Discipline:</b> '+disc+' &nbsp;&middot;&nbsp; <b>Status:</b> '+status+'<br>'+
    '<b>Shape:</b> 12 sessions, 90 minutes, six stages each &mdash; open, three movements, discuss, close.</p>'+
    '<h5>The twelve lessons</h5>';
  for(var k=0;k<A.L.length;k++){
    var n = (k+1)<10 ? '0'+(k+1) : ''+(k+1);
    h += '<div class="lrow"><b>'+n+'</b><span>'+fill(A.L[k][0],title,sub,disc)+
         '<i>'+fill(A.L[k][1],title,sub,disc)+'</i></span></div>';
  }
  h += '<h5>Session pattern applied to every lesson</h5><p><b>Three movements</b></p><ul>';
  var mv = ENGINE.moves[a];
  for(var m=0;m<mv.length;m++){ h += '<li>'+fill(mv[m],title,sub,disc)+'</li>'; }
  h += '</ul><p><b>Two discussion questions, never three</b></p><ul>';
  var qq = ENGINE.qs[a];
  for(var q=0;q<qq.length;q++){ h += '<li>'+fill(qq[q],title,sub,disc)+'</li>'; }
  h += '</ul><p><b>Weekly exercise</b></p><p>'+fill(ENGINE.exs[a],title,sub,disc)+'</p>';
  h += '<h5>What the author pass adds</h5><ul>'+
    '<li>The actual key text for each of the twelve sessions</li>'+
    '<li>Movements written to this material rather than to the archetype</li>'+
    '<li>Questions that could only be asked about this course</li>'+
    '<li>The reading list, and the primary source for the depth track</li>'+
    '<li>A full teaching script per session, roughly 1,200 words each</li></ul>'+
    '<p style="font-family:Lato,sans-serif;font-size:13px;color:var(--muted);'+
    'border-top:1px solid var(--rule);padding-top:14px;margin-top:24px">Engine output is '+
    'deterministic: this sheet renders identically every time. Regenerating is not editing.</p>';
  return h;
}
</script>
"""

GENCSS = """
.genwarn{border:1px solid var(--gold);background:#fffdf8;padding:16px 18px;margin:18px 0 6px;
 font-family:"Lato",sans-serif;font-size:12.5px;line-height:1.7;color:var(--body)}
.genwarn b{display:block;color:var(--gold);letter-spacing:.12em;text-transform:uppercase;
 font-size:9.5px;margin-bottom:7px}
"""

# swap the modal dispatcher to call the engine
old_call = "mbody.innerHTML = (c === 'ST 101') ? fullST101(c,t,u) : frame(c,t,u,d,st);"
new_call = "mbody.innerHTML = (c === 'ST 101') ? fullST101(c,t,u) : buildSheet(c,t,u,d,st);"
assert old_call in s, "dispatcher not found"
s = s.replace(old_call, new_call, 1)

# button label: the frame is now a real draft
s = s.replace(">See the course frame &nbsp;&rarr;<", ">Open 12-lesson build sheet &nbsp;&rarr;<")

s = s.replace("</style>", GENCSS + "\n</style>", 1)
s = s.replace("<script>", JS_ENGINE + "\n<script>", 1)

open(SRC, "w", encoding="utf-8").write(s)
print("engine wired. bytes:", len(s))
print("build sheet buttons:", s.count("Open 12-lesson build sheet"))
