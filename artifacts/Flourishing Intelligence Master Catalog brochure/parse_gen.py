# -*- coding: utf-8 -*-
import re, html

text = open('/home/claude/blue17/source.md', encoding='utf-8').read()

def esc(s):
    return html.escape(s, quote=False)

# Split into dimension blocks on "## <roman>. Dimension Name"
dim_pattern = re.compile(r'^##\s+([IVX]+)\.\s+(.+)$', re.MULTILINE)
matches = list(dim_pattern.finditer(text))

dimensions = []
for idx, m in enumerate(matches):
    roman, name = m.group(1), m.group(2).strip()
    start = m.end()
    end = matches[idx+1].start() if idx+1 < len(matches) else len(text)
    block = text[start:end]

    # subtitle: first **bold** line
    sub_m = re.search(r'^\*\*(.+?)\*\*\s*$', block, re.MULTILINE)
    subtitle = sub_m.group(1) if sub_m else ''

    # marketing paragraph: first non-bold, non-empty line after subtitle
    para_m = re.search(r'\*\*.+?\*\*\s*\n\n(.+?)\n\n', block, re.DOTALL)
    paragraph = para_m.group(1).strip() if para_m else ''

    # pathways
    path_m = re.search(r'\*\*Ten Pathways:\*\*\s*(.+)', block)
    pathways = path_m.group(1).strip() if path_m else ''

    # campaigns: **Title** — Subtitle \n 1. ... · 2. ... etc
    campaign_pattern = re.compile(r'\*\*(.+?)\*\*\s+—\s+(.+?)\n(1\..+)')
    campaigns = []
    for cm in campaign_pattern.finditer(block):
        ctitle, csub, sessions_line = cm.group(1), cm.group(2), cm.group(3)
        sessions = re.split(r'\s*·\s*', sessions_line.strip())
        # strip leading "N. "
        clean_sessions = [re.sub(r'^\d+\.\s*', '', s).strip() for s in sessions]
        campaigns.append((ctitle.strip(), csub.strip(), clean_sessions))

    dimensions.append({
        'roman': roman, 'name': name, 'subtitle': subtitle,
        'paragraph': paragraph, 'pathways': pathways, 'campaigns': campaigns
    })

print("Parsed", len(dimensions), "dimensions")
for d in dimensions:
    print(" ", d['roman'], d['name'], "-", len(d['campaigns']), "campaigns")

# ---- Generate HTML ----
out = []
total_campaigns = 0
total_sessions = 0
for d in dimensions:
    out.append(f'''
<div class="dimension">
  <div class="dim-head">
    <span class="dim-roman">{d['roman']}</span>
    <div>
      <h2>{esc(d['name'])}</h2>
      <p class="dim-subtitle">{esc(d['subtitle'])}</p>
    </div>
  </div>
  <p class="dim-para">{esc(d['paragraph'])}</p>
  <div class="pathways"><strong>Ten Pathways:</strong> {esc(d['pathways'])}</div>
  <div class="campaign-grid">''')
    for ctitle, csub, sessions in d['campaigns']:
        total_campaigns += 1
        session_html = "".join(f'<li><span class="sn">{i+1}</span>{esc(s)}</li>' for i, s in enumerate(sessions))
        total_sessions += len(sessions)
        out.append(f'''
    <div class="campaign-card">
      <h4>{esc(ctitle)}</h4>
      <p class="csub">{esc(csub)}</p>
      <ol class="sessions">{session_html}</ol>
    </div>''')
    out.append('''
  </div>
</div>''')

body = "\n".join(out)
open('/home/claude/blue17/dimensions_block.html', 'w', encoding='utf-8').write(body)
print("TOTAL campaigns:", total_campaigns, "TOTAL sessions:", total_sessions)
