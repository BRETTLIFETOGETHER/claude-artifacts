#!/usr/bin/env python3
"""Inline styles.css, data.js and app.js into every page → self-contained files."""
import re, pathlib

src = pathlib.Path('/home/claude/flc')
out = pathlib.Path('/home/claude/flc/dist')
out.mkdir(exist_ok=True)

css  = (src/'styles.css').read_text(encoding='utf-8')
data = (src/'data.js').read_text(encoding='utf-8')
app  = (src/'app.js').read_text(encoding='utf-8')

pages = ['index.html','vision.html','reader.html','campaigns.html',
         'campaign.html','assessment.html','pathways.html','about.html']

jsflag = '<script>document.documentElement.classList.add("js")</script>'

for p in pages:
    html = (src/p).read_text(encoding='utf-8')
    # confirm-JS flag immediately so .rv hiding only applies when scripts run
    html = html.replace('<head>', '<head>\n'+jsflag, 1)
    # inline stylesheet
    html = html.replace('<link rel="stylesheet" href="styles.css">',
                        '<style>\n'+css+'\n</style>', 1)
    # inline data + app
    html = html.replace('<script src="data.js"></script>',
                        '<script>\n'+data+'\n</script>', 1)
    html = html.replace('<script src="app.js"></script>',
                        '<script>\n'+app+'\n</script>', 1)
    assert 'styles.css' not in html, p+': stylesheet ref remains'
    assert 'src="data.js"' not in html and 'src="app.js"' not in html, p+': js ref remains'
    (out/p).write_text(html, encoding='utf-8')
    print(f'{p:18s} {len(html)/1024:6.1f} KB  self-contained')

print('done')
