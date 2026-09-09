#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill every empty campaign subtitle across the catalog.
Style-matched to Brett's existing subtitles (short promise lines and questions),
channel-voiced, format-aware, title-keyword aware, and globally unique across all
generated rows. Rewrites data/index.json, data/index.js, and all 23 shards in place
(shards are patched row-by-row by id, preserving their exact shape)."""
import json, re, hashlib, os

SITE = "/home/claude/site"
d = json.load(open(f"{SITE}/data/index.json"))
C = {k: i for i, k in enumerate(d["cols"])}
rows = d["rows"]

# per-channel phrase material: {noun} pools + full-pattern pools ({days} and {kw} available)
CH = [
 (["your calling","the life you were made for","work that matters","your next assignment"],
  ["{days} Days to a Life on Purpose","Finding the Work God Prepared","What You Were Made For","From Drifting to Sent"]),
 (["who you already are","the beloved life","your true name","an unshakable identity"],
  ["{days} Days of Knowing Who You Are","Living Loved, Not Proving Worth","The Verdict Is Already In","From Performing to Beloved"]),
 (["real belonging","life around the table","being fully known","friendship that holds"],
  ["Nobody Was Meant to Do This Alone","{days} Days from Crowd to Family","Building the Circle You've Been Missing","Known, Loved, and Kept Anyway"]),
 (["unhurried prayer","a listening life","honest conversation with God","first-response prayer"],
  ["{days} Days of Learning to Pray Again","When Prayer Becomes a Place","From Emergency Calls to Daily Conversation","Teaching a Church to Listen"]),
 (["an open-handed life","peace with what you have","money in its place","trust over worry"],
  ["{days} Days to Financial Peace of Heart","When Enough Becomes Real","Trusting God with the Numbers","From Anxiety to Open Hands"]),
 (["cheerful giving","the generous life","kingdom investment","open hands"],
  ["{days} Days of Learning to Let Go","The Joy on the Other Side of Giving","Becoming a Generous People","From Leftovers to Firstfruits"]),
 (["a legacy that outlives you","faith handed down","your family's story","the next generation"],
  ["Preparing More Than an Inheritance","{days} Days of Building What Lasts","Telling the Story Before It's Lost","Faith That Reaches Your Grandchildren"]),
 (["your covenant","a marriage that holds","oneness worth tending","love for the long haul"],
  ["{days} Days of Tending the Vows","Strengthening What God Joined","From Roommates Back to One","The Marriage You Still Want"]),
 (["faith at home","the hearts of your kids","parenting with purpose","the family table"],
  ["Raising Kids Who Keep the Faith","{days} Days for the Family Table","Equipping the Home, Not Outsourcing It","Parenting Past the Panic"]),
 (["peace that holds","an unhurried heart","hope with roots","rest for your soul"],
  ["{days} Days Toward a Quiet Heart","When Anxiety Meets Its Match","Finding Rest in a Restless Year","Hope for the Heavy-Hearted"]),
 (["strength for today","wholeness","grace for the long road","care with dignity"],
  ["Grace for Bodies That Wear Out","{days} Days of Strength for Today","Faith Through Diagnosis and Waiting","Whole in the Hands of God"]),
 (["freedom that lasts","the new life","walking in the light","a clean start"],
  ["{days} Days Out of Hiding","Breaking What Has Been Breaking You","Freedom Worth Fighting For","From Secrets to Light"]),
 (["this new chapter","faith for the transition","what comes next","grace for the in-between"],
  ["Faith for the Chapter You Didn't Choose","{days} Days Through the Turn","When Everything Changes but God","Grace for the In-Between"]),
 (["Monday faith","work as worship","integrity under pressure","calling at your desk"],
  ["Taking Sunday Into Monday","{days} Days of Faith That Works","Your Desk as an Altar","Excellence as a Witness"]),
 (["servant leadership","leading from overflow","the towel and the basin","raising up others"],
  ["Leading the Way Jesus Led","{days} Days for the Ones Who Carry Others","From Empty Tank to Overflow","Multiplying More Than Managing"]),
 (["one direction together","the church's next chapter","a shared vision","alignment that moves"],
  ["A Whole Church, One Direction","{days} Days Toward What's Next","Vision Everyone Can Finish","Building What Outlasts Us"]),
 (["the mission you steward","faithful service","people at the margins","kingdom work"],
  ["Serving Until the City Notices","{days} Days of Hands-On Faith","For the Least of These, Together","Fueling the Work That Matters"]),
 (["your neighbor","everyday witness","love with an address","the harvest around you"],
  ["Reaching the Street You Live On","{days} Days of Loving Your Neighbor","Good News Within Walking Distance","From Pew to Front Porch"]),
 (["the holy season","sacred time","the feast ahead","a set-apart week"],
  ["Making the Season Actually Holy","{days} Days to Prepare Your Heart","When the Calendar Turns Sacred","Ready for the Feast"]),
 (["the words of Jesus","the way of the Rabbi","red-letter faith","life with Christ"],
  ["Taking Jesus at His Word","{days} Days in the Red Letters","From Admiring to Following","The Rabbi's Way, Walked Daily"]),
 (["the Word that reads you","Scripture-shaped life","a Book that breathes","truth for today"],
  ["{days} Days in the Word Together","When the Bible Reads You Back","A Church with One Vocabulary","From Owning Bibles to Opening Them"]),
 (["honest questions","faith with room to breathe","belief helped along","seeking that finds"],
  ["Faith Honest Enough for Your Questions","{days} Days for Doubters Too","Wrestling Until the Blessing","Room to Ask Out Loud"]),
 (["reclaimed attention","presence over pixels","a guarded heart","wisdom for the feed"],
  ["Getting Your Attention Back","{days} Days of Looking Up","Discipling the Scroll","Wisdom for a Wired World"]),
]
STOP=set("the a an of and to in for with your our my his her their its on at day days 40 30 21 7".split())
def days_of(f): return 40 if f&8 else 30 if f&4 else 21 if f&2 else 7 if f&1 else 40
def kw(t):
    ws=[w for w in re.findall(r"[A-Za-z']+",t) if w.lower() not in STOP]
    return ws[-1] if ws else ""

seen=set(r[C["s"]] for r in rows if r[C["s"]])
gen=0; per_ch={}
KW_PAT=["Because {kw} Is Worth {days} Days","{days} Days Closer to {kw}","Where {kw} Becomes a Practice","A Whole Church Learning {kw}"]
for r in rows:
    if r[C["s"]]: continue
    ch=r[C["ch"]]; nouns,pats=CH[ch]; dy=days_of(r[C["f"]])
    seed=int(hashlib.md5((r[C["fp"]]+r[C["id"]]).encode()).hexdigest()[:8],16)
    k=kw(r[C["t"]])
    cands=[]
    for b in range(24):
        i=(seed+b)
        if b%3==2 and k and len(k)>3:
            s=KW_PAT[i%len(KW_PAT)].replace("{kw}",k[0].upper()+k[1:]).replace("{days}",str(dy))
        elif i%2:
            s=pats[i//2%len(pats)].replace("{days}",str(dy))
        else:
            n=nouns[i//2%len(nouns)]
            s=["A Churchwide Season of "+n[0].upper()+n[1:],
               str(dy)+" Days Toward "+n[0].upper()+n[1:],
               "Practicing "+n[0].upper()+n[1:]+", Together",
               "The Whole Church, "+n[0].upper()+n[1:]][i//8%4]
        if s not in seen:
            cands.append(s); break
    assert cands, f"subtitle space exhausted at {r[C['id']]}"
    s=cands[0]; seen.add(s); r[C["s"]]=s; gen+=1
    per_ch[ch]=per_ch.get(ch,0)+1

empty=sum(1 for r in rows if not r[C["s"]])
print(f"generated {gen:,} subtitles · remaining empty: {empty} · all unique among generated: True")

# ---- rewrite index.json + index.js ------------------------------------------
json.dump(d, open(f"{SITE}/data/index.json","w"), ensure_ascii=False, separators=(",",":"))
open(f"{SITE}/data/index.js","w").write("window.DATA40="+json.dumps(d,ensure_ascii=False,separators=(",",":"))+";")

# ---- patch shards in place (dict-shaped rows, patched by id) -----------------
by_id={r[C["id"]]: r[C["s"]] for r in rows}
patched=0
for fn in sorted(os.listdir(f"{SITE}/data")):
    if not re.match(r"ch\d\d\.js$", fn): continue
    txt=open(f"{SITE}/data/{fn}").read()
    m=re.match(r"SHARD\((\d+),(.*)\);?\s*$", txt, re.S)
    obj=json.loads(m.group(2))
    for row in obj["rows"]:
        s=by_id.get(row["id"])
        if s and not row.get("s"): row["s"]=s; patched+=1
    open(f"{SITE}/data/{fn}","w").write(f"SHARD({m.group(1)},{json.dumps(obj,ensure_ascii=False,separators=(',',':'))});")
print(f"shards patched: {patched:,} rows")
