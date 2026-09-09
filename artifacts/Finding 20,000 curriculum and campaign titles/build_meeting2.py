# -*- coding: utf-8 -*-
import json
from sm1 import PART1
from sm2 import PART2
from sm3 import PART3
from sm4 import PART4
import meeting_meta as M

ALL = PART1 + PART2 + PART3 + PART4
NC = len(ALL); NS = sum(len(c[7]) for c in ALL)

payload = {
 "cats":[{"n":c[0],"s":c[1],"w":c[2],"ice":c[3],"close":c[4],"deep":c[5],"notes":c[6],
          "ss":[{"t":s[0],"sub":s[1],"pas":s[2],"pts":s[3],"pr":s[4],"ns":s[5]} for s in c[7]]} for c in ALL],
 "thesis":M.THESIS,"why":M.WHY,"struct":M.STRUCTURE,"structnote":M.STRUCTURE_NOTE,
 "lq":M.LEADER_Q,"lb":M.LEADER_BANDS,"survey":M.STAFF_SURVEY,
 "cal":M.CAL52,"calrules":M.CAL_RULES,"retreat":M.RETREAT,
 "toolbox":M.TOOLBOX,"journeys":M.JOURNEYS,"nc":NC,"ns":NS,
}

CSS = open("meeting_css.txt", encoding="utf-8").read()
BODY = open("meeting_body.txt", encoding="utf-8").read()
JS = open("meeting_js.txt", encoding="utf-8").read()

SHELL = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Church Staff Meeting Finder &amp; Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body>__BODY__<script>__JS__</script></body></html>"""

out = SHELL.replace("__CSS__", CSS).replace("__BODY__", BODY)
out = out.replace("__JS__", JS.replace("__DATA__", json.dumps(payload, separators=(",", ":"))))
open("/mnt/user-data/outputs/staff-meeting-builder.html", "w", encoding="utf-8").write(out)
print("categories:", NC, "| sessions:", NS, "| KB:", round(len(out)/1024, 1))
