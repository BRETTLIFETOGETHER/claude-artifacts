#!/usr/bin/env python3
import re, sys, os, glob

TS = re.compile(r'^(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->')

def strip(path, out):
    lines = open(path, encoding='utf-8-sig').read().splitlines()
    text = []
    last_marker = -1
    cur_ts = None
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith('WEBVTT') or s.startswith('NOTE'):
            continue
        m = TS.match(s)
        if m:
            h, mi, se = int(m.group(1)), int(m.group(2)), int(m.group(3))
            cur_ts = h * 60 + mi
            continue
        if re.fullmatch(r'\d+', s):
            continue
        if cur_ts is not None and cur_ts != last_marker and cur_ts % 2 == 0:
            text.append(f"\n[{cur_ts:02d}:00]")
            last_marker = cur_ts
        text.append(s)
    body = ' '.join(text)
    body = re.sub(r'\s+\[', '\n\n[', body)
    body = re.sub(r'\]\s+', ']\n', body)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(body.strip() + '\n')
    return len(body.split())

for p in sorted(glob.glob('/mnt/user-data/uploads/*.vtt')):
    base = os.path.basename(p).replace('.vtt', '.txt')
    n = strip(p, os.path.join('/home/claude/tx', base))
    print(f"{base}: {n} words")
