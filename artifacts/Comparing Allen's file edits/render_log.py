import json, re
from collections import OrderedDict

recs = json.load(open('records.json'))

ORDER = ['Leader Guide — Front Matter'] + ['Leader Guide — Session %d' % i for i in range(1, 7)] \
      + ['Participant Guide — Front Matter'] + ['Participant Guide — Session %d' % i for i in range(1, 7)]

def flags_for(rec):
    f = []
    new = rec['new']
    old = rec['old']
    if 'Plan spending on' in new:
        f.append('FIX')
    if 'first grade,.' in new:
        f.append('FIX')
    if ' -- ' in new and ' -- ' not in old:
        f.append('FIX')
    if 'start sharing -- the business model' in new:
        f.append('FIX')
    if 'I have had the honest money conversations' in new:
        f.append('FIX')
    if re.search(r'who owns it\*\*\.', new):
        f.append('FIX')
    if 'In this session' in new or 'the session' in new or 'meeting' in new or 'Save question 10 for a strong meeting' in new:
        if re.search(r'\bnight\b|\bTonight\b|\btonight\b', old):
            f.append('EVE')
    return sorted(set(f))

def ctx(c, width=5):
    pre = ' '.join(c['pre'].split()[-width:])
    post = ' '.join(c['post'].split()[:width])
    frm = c['from']
    to = c['to']
    if c['tag'] == 'insert':
        was = ('%s %s' % (pre, post)).strip()
        now = ('%s %s %s' % (pre, to, post)).strip()
    elif c['tag'] == 'delete':
        was = ('%s %s %s' % (pre, frm, post)).strip()
        now = ('%s %s' % (pre, post)).strip()
    else:
        was = ('%s %s %s' % (pre, frm, post)).strip()
        now = ('%s %s %s' % (pre, to, post)).strip()
    return was, now

def locator(rec):
    n = rec['new']
    if n.startswith('> LEADER'):
        return 'Leader cue'
    m = re.match(r'^(\d+)\.\s', n.replace('\\', ''))
    if m:
        return 'Item %s' % m.group(1)
    if n.startswith('**Day'):
        mm = re.match(r'\*\*Day (\d+)', n)
        return 'Day %s' % mm.group(1)
    if n.startswith('**Time guide'):
        return 'Time guide'
    if n.startswith('**What'):
        return re.sub(r'\*', '', n.split(':')[0])
    if n.startswith('**On '):
        return re.sub(r'\*', '', n.split(':')[0])
    if n.startswith('**Big Idea'):
        return 'Big Idea'
    if n.startswith('**Icebreaker'):
        return 'Icebreaker'
    if n.startswith('\\"Father'):
        return 'Prayer'
    if n.startswith('\\"Welcome'):
        return 'Welcome script'
    if 'Read one aloud to open your time' in n:
        return 'Opening Story intro'
    return 'Paragraph'

groups = OrderedDict((k, []) for k in ORDER)
for r in recs:
    groups.setdefault(r['section'], []).append(r)

out = []
W = out.append

W('# Generous Living — Adult Curriculum')
W('## Allen\'s Edit Log: July 21 snapshot → current Shared file')
W('')
W('Compared `july_21_-_Copy_of_Shared_-_Generous_Living_-_Adult_Curriculum_-_July_21_1_39_PM.docx` '
  '(older) against `Shared_-_Generous_Living_-_Adult_Curriculum_.docx` (current). Neither file carries '
  'tracked changes or comments, so this list was reconstructed by text comparison.')
W('')
W('**127 paragraphs changed. No paragraph added, deleted, or moved. No heading, title, subtitle, '
  'fill-in blank, assessment item, or Day listing was restructured.** Everything below is line editing.')
W('')
W('Page numbers are from the current file rendered at 84 pages. Word repaginates slightly against '
  'other renderers, so treat these as accurate to within a page.')
W('')
W('Flags: **[FIX]** = introduces an error, revert or correct. **[EVE]** = part of the evening-neutral '
  'pass, keep but finish it.')
W('')
W('---')
W('')

total = 0
for sec in ORDER:
    rows = groups.get(sec) or []
    if not rows:
        continue
    W('## %s' % sec)
    W('')
    for r in rows:
        fl = flags_for(r)
        tag = (' **[%s]**' % ']** **['.join(fl)) if fl else ''
        W('**p. %d — %s**%s' % (r['page'], locator(r), tag))
        W('')
        for c in r['changes']:
            was, now = ctx(c)
            W('- was: %s' % was)
            W('- now: %s' % now)
            W('')
            total += 1
    W('---')
    W('')

W('')
W('Total discrete word-level changes: %d across 127 paragraphs.' % total)

open('/mnt/user-data/outputs/Allen_Edit_Log_Generous_Living_Adult.md', 'w').write('\n'.join(out))
print('changes:', total)
