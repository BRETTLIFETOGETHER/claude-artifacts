#!/usr/bin/env python3
"""
GOD OWNS IT ALL - Student Edition
Verification audit.

Checks every mechanical claim we can check:
  A. Reviewer edits (Russ, Phil) are present in the files
  B. Every video fill-in answer is what is actually said on camera
  C. Ron's weekly texts match the filmed wording
  D. Memory verses are the video anchors
  E. Contents pages agree with body pages
  F. Curriculum reading lists agree with the devotional
  G. Student verses vs the adult devotional
  H. House style rules (no em-dashes, no dollar figures in exercises)
  I. Nothing internal left in a client-facing file

Run:  python3 verify.py
Exit code 0 = all checks pass. Non-zero = something needs attention.

WHAT THIS CANNOT CHECK is listed at the bottom of the report. Those need a human.
"""
import re, sys, os, glob

DEVO = 'devo.md'
CURR = 'curr.md'
LEAD = 'leader_edition.md'
ADULT = 'adult40.txt'
VTT_DIR = 'vtt'          # L1.txt .. L6.txt, plain text of each filmed lesson

fails, warns, passes = [], [], []

def norm(s):
    """Strip pandoc escaping and normalise dashes and whitespace."""
    s = s.replace('\\', '')
    s = re.sub(r'[\u2013\u2014]+|--+', '-', s)
    return re.sub(r'\s+', ' ', s).strip()

def load(p):
    return norm(open(p, encoding='utf8').read()) if os.path.exists(p) else ''

devo, curr, lead = load(DEVO), load(CURR), load(LEAD)
adult = load(ADULT)
vtt = {i: load(f'{VTT_DIR}/L{i}.txt').lower() for i in range(1, 7)}

def check(label, ok, detail=''):
    (passes if ok else fails).append((label, detail))

def warn(label, detail=''):
    warns.append((label, detail))

# ------------------------------------------------------- A. reviewer edits
# Each entry: (reviewer, where, phrase that must be present, file)
EDITS = [
 ('Russ', 'Day 1 question mark',        'your talents, your family, your body?', devo),
 ('Russ', 'Day 1 replacement sentence', 'required a body and brain to earn it and those were handed to you first', devo),
 ('Russ', 'Day 1 scripture colon',      "Today's Scripture:", devo),
 ('Russ', 'Day 1 gift tag kept',        'tiny gift tag on it that read', devo),
 ('Russ', 'Day 2 grip gesture',         'Grip your hands tightly and imagine holding on to it', devo),
 ('Russ', 'Day 3 his wording',          'I worked hard with what was given to me', devo),
 ('Russ', 'Day 5 muddled line fixed',   "isn't right or wrong, it's just honest", devo),
 ('Russ', 'Day 7 weight vs burden',     "It's serious, and it isn't crushing", devo),
 ('Russ', 'Day 5 title',                'Money Reveals Your Master', devo),
 ('Russ', 'Day 6 title',                'Why Money Stresses You Out', devo),
 ('Russ', 'Day 8 title split',          'Enough Is Learned', devo),
 ('Russ', 'Day 14 subtitle',            'Peace through the Storms', devo),
 ('Russ', 'DoorDash removed',           'a food run', devo),
 ('Russ', 'About Ron, grandkids',       'his own kids when they were your age, and now with his grandkids', devo),
 ('Russ', 'About Ron, grandkids',       'his own kids when they were your age, and now with his grandkids', curr),
 ('Russ', 'S1 "sports" not "ball"',     'your talent for art or sports', curr),
 ('Russ', 'S1 "you or your friends"',   'What\u2019s something you or your friends get weirdly protective over', curr),
 ('Russ', 'S1 "lighter load"',          'a lot lighter load than it sounds', curr),
 ('Russ', 'S1 clothes not shoes',       'Your phone, your clothes, whatever', curr),
 ('Russ', 'Grip column',                'Grip (1-10)', curr),
 ('Russ', 'Group agreement prayer',     "pray for each other during the week", curr),
 ('Russ', 'Phone dependence removed',   'first thing every morning', curr),
 ('Phil', 'Day 5 Big Idea',             "whether your stuff has you", devo),
 ('Phil', 'Day 6 Big Idea',             'realizing how big God is and taking one day at a time', devo),
 ('Phil', 'Day 3 title softened',       'The Word That Grows Teeth', devo),
 ('Phil', 'Day 10 short horizon',       'first mile of a very long race', devo),
 ('Phil', 'Day 5 subtitle',             'Where it goes reveals our heart', devo),
 ('Phil', 'Day 13 subtitle',            'Your feed is not your measuring stick', devo),
 ('Phil', 'S3 vague phrase fixed',      'in a way that actually costs you something', curr),
 ('Phil', 'S5 pressure clause',         'not because someone is pressuring you', curr),
]
for who, where, phrase, hay in EDITS:
    check(f'{who} | {where}', norm(phrase) in hay, phrase[:60])

# things that must be GONE
REMOVED = [
 ('Russ', 'answer keys out of participant guide', 'Answers:', curr),
 ('Russ', 'DoorDash gone',                        'Door Dash', devo),
 ('Phil', 'old Day 3 title gone',                 'Most Dangerous Word', devo + curr),
 ('house', 'old day count gone',                  '40-Day', devo),
 ('house', 'internal names gone',                 'Russ Gunsalus', devo + curr),
 ('house', 'internal names gone',                 'Keri Wyatt', devo + curr),
 ('house', 'placeholder text gone',               'Copy to be supplied', devo + curr),
]
for who, where, phrase, hay in REMOVED:
    check(f'{who} | {where}', norm(phrase) not in hay, f'found: {phrase}')

# ------------------------------------------------ B. fill-in answers vs film
FILL = {
 1: ['life','image','created','His','good','very','holding','borrowed','yours'],
 2: ['have','finish','line','what','is','it','day','rotten','store','normal',
     'industries','business','model','hitting','trusting'],
 3: ['not','looking','holding','could','handle','afraid','identical','Faithfulness',
     'fear','fear','safe','move','failure'],
 4: ['out','there','in','here','2:00 a.m.','real','care','Quiet','still',
     'I','am','with','you','weather','boat','outcome','Person','agreement'],
 5: ['you','you','have','reservoir','stagnant','rot','sack','lunch','All','of','it',
     'holding','released','poorer','amount','heart'],
 6: ['faithful','trend','small','stuff','famous','you','are','bowl','identity',
     'wasted','you','up','window','view'],
}
STOPWORDS = {'you','is','it','in','of','not','i','am','with','up','have','and','the'}
for s, answers in FILL.items():
    t = vtt.get(s, '')
    if not t:
        warn(f'transcript L{s} missing', 'cannot verify fill-ins for this session')
        continue
    missing = [a for a in answers
               if a.lower() not in STOPWORDS and a.lower() not in t]
    check(f'video | S{s} fill-in answers on camera',
          not missing, f'missing: {missing}')

# --------------------------------------------------- C. Ron's texts vs film
RON = {
 2: "Enough was never a number to hit",
 3: "How you handle what isn't yours is who you actually are",
 4: "Fear says what if, but faith says even if",
 5: "Be a pipeline, not a reservoir",
 6: "You don't leave a legacy. You live one, starting now",
}
for s, phrase in RON.items():
    t = vtt.get(s, '')
    if not t: continue
    check(f'video | S{s} Ron text matches film',
          norm(phrase).lower() in t, phrase[:50])
    check(f'devotional | S{s} Ron text present',
          norm(phrase) in devo, phrase[:50])
# Session 1's Ron text comes from the script, not the film
check('devotional | S1 Ron text (script-sourced)',
      "It was His before it was yours" in devo, 'Day 7')

# career length must be forty-five everywhere in the books
for name, hay in (('devotional', devo), ('curriculum', curr)):
    bad = re.findall(r'(fifty years|50 years|five decades)', hay, re.I)
    check(f'house | {name} career length is forty-five', not bad, f'found: {bad}')

# ------------------------------------------------------- D. memory verses
MV = {1:'Psalm 24:1', 2:'Hebrews 13:5', 3:'Matthew 25:21',
      4:'Isaiah 41:10', 5:'2 Corinthians 9:7', 6:'Matthew 5:16'}
for s, v in MV.items():
    check(f'curriculum | S{s} memory verse present', v in curr, v)
# note which are spoken on camera vs script only
for s, v in MV.items():
    t = vtt.get(s, '')
    if t and v.split(':')[0].lower() not in t:
        warn(f'S{s} memory verse {v} not spoken on camera', 'script-sourced, acceptable')

# ------------------------------------------- E. contents vs body, devotional
toc_t = dict(re.findall(r'\*\*Day (\d+) - ([^*]+?)\*\*', devo))
hdr_t = dict(re.findall(r'DAY (\d+) -\*?\*? ?\*?\*?([^*]+?)\*\*', devo))
bad = [d for d in toc_t
       if re.sub(r'[^a-z0-9]', '', toc_t[d].lower())
       != re.sub(r'[^a-z0-9]', '', hdr_t.get(d, '').lower())]
check('structure | 42 day titles match contents', not bad, f'mismatched days: {bad}')

toc_s = dict(re.findall(r'\*\*Day (\d+) - [^*]+\*\* ([^\u00b7\n]+?) \u00b7', devo))
bad = []
for d, sub in toc_s.items():
    m = re.search(r'DAY ' + d + r' -[^\n]*\n\n\*([^*]+)\*', devo)
    if m and re.sub(r'[^a-z0-9]', '', sub.lower()) != re.sub(r'[^a-z0-9]', '', m.group(1).lower()):
        bad.append(d)
check('structure | 42 day subtitles match contents', not bad, f'mismatched days: {bad}')

# ------------------------------- F. curriculum reading lists vs devotional
BOOKS = (r'(?:Genesis|Exodus|Deuteronomy|Psalm|Proverbs|Ecclesiastes|Isaiah|Lamentations|'
         r'Daniel|Habakkuk|Zechariah|Amos|Matthew|Mark|Luke|John|Acts|Romans|1 Corinthians|'
         r'2 Corinthians|Galatians|Ephesians|Philippians|Colossians|1 Thessalonians|'
         r'1 Timothy|Hebrews|James|1 Peter)')
devo_v = {}
for m in re.finditer(r'\*\*Day (\d+) - [^*]+\*\*[^\u00b7\n]+\u00b7 ([^\u00b7\n]+) \u00b7 ([^\n]+)', devo):
    devo_v[m.group(1)] = {norm(m.group(2)).rstrip('.'), norm(m.group(3)).rstrip('.')}
bad = []
for m in re.finditer(r'\u2610 \*\*Day (\d+) - [^*]+\*\* ([^\n\u2610]+)', curr):
    vs = {norm(v) for v in re.findall(BOOKS + r'\s\d+:[\d,\-]+', m.group(2))}
    if vs != devo_v.get(m.group(1), set()):
        bad.append(m.group(1))
check('structure | curriculum reading lists match devotional', not bad, f'days: {bad}')

# ------------------------------------------- G. student verses vs adult
if adult:
    adult_v = {}
    for line in adult.split('\n'):
        m = re.match(r'\s*Day (\d+) - (.*)', line)
        if m:
            vs = re.findall(BOOKS + r'\s\d+:[\d,\-]+', m.group(2))
            if vs: adult_v[m.group(1)] = {norm(v) for v in vs}
    HELD = {'7', '26', '30', '41'}   # deliberate, documented divergences
    unexpected = [d for d in devo_v
                  if d in adult_v and devo_v[d] != adult_v[d] and d not in HELD]
    check('alignment | student verses match adult (except 4 held)',
          not unexpected, f'unexpected divergences: {unexpected}')
    for d in sorted(HELD, key=int):
        if d in adult_v and devo_v.get(d) == adult_v[d]:
            warn(f'Day {d} now matches adult', 'was a documented divergence, confirm intended')
else:
    warn('adult devotional not found', 'skipped adult verse comparison')

# ------------------------------------------------------- H. house style
for name, hay in (('devotional', devo), ('curriculum', curr), ('leader edition', lead)):
    if not hay: continue
    check(f'style | {name} has no em-dashes', '\u2014' not in open(
        {'devotional': DEVO, 'curriculum': CURR, 'leader edition': LEAD}[name],
        encoding='utf8').read(), 'em-dash found')
# no dollar figures inside exercises
for label, section in (('Open hands', 'Open hands'), ('finish line', 'Draw your finish line'),
                       ('buckets', 'Live, Give, Owe, Grow'), ('quiet gift', 'The quiet gift')):
    m = re.search(r'## \*\*' + re.escape(section) + r'\*\*(.{0,2500}?)## \*\*', curr, re.S | re.I)
    if m:
        check(f'dignity | no dollar figures in {label} exercise',
              not re.search(r'\$\d', m.group(1)), 'dollar amount found')

# ---------------------------------------------------------------- report
print('=' * 68)
print('GOD OWNS IT ALL - STUDENT EDITION - VERIFICATION AUDIT')
print('=' * 68)
print(f'\nPASS {len(passes)}   FAIL {len(fails)}   REVIEW {len(warns)}\n')
if fails:
    print('-- FAILED ' + '-' * 56)
    for l, d in fails: print(f'  X  {l}\n       {d}')
    print()
if warns:
    print('-- NEEDS A LOOK ' + '-' * 50)
    for l, d in warns: print(f'  ?  {l}\n       {d}')
    print()
print('-- PASSED ' + '-' * 56)
for l, _ in passes: print(f'  ok {l}')

print('\n' + '=' * 68)
print('WHAT THIS CANNOT CHECK - needs a person')
print('=' * 68)
print("""
  1. Whether a reviewer's intent landed, only that their words are present.
     Phil's note that teens think in months not lifetimes drove a rewrite of
     Day 10. The phrase is there. Whether it works on a fifteen-year-old is
     a judgment call.
  2. Any comment made after the last export. This checks the edits we logged,
     not ones nobody has sent yet.
  3. Whether the filmed Lesson 1 ending got fixed. The books do not depend on
     it, but the tease still points at the wrong week.
  4. Theology, tone, and whether the voice still sounds like a person.
  5. Scripture wording against a licensed NIV text. Verify at layout.
""")
sys.exit(1 if fails else 0)
