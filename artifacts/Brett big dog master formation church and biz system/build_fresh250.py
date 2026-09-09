
import html as hlib
def e(s): return hlib.escape(str(s))

CSS = """
:root{
  --navy:#02040a;--gold:#c9a84c;--gold-lt:#e2c97e;--gold-dk:#8a6e30;
  --cream:#f8f5ef;--tl:#d4c9b8;--tm:#8a9ab5;--rule:rgba(201,168,76,0.10);--ink:#0e1520;
  --red:#8a3030;--green:#3a6a4a;--blue:#3a5a8a;--amber:#8a6a1a;--purple:#5a3a6a;
}
*{margin:0;padding:0;box-sizing:border-box;}html{scroll-behavior:smooth;}
body{font-family:'Lato',sans-serif;background:#dedad2;color:var(--ink);}
.page{max-width:1160px;margin:0 auto;background:var(--cream);box-shadow:0 4px 80px rgba(0,0,0,.22);}

/* COVER */
.cover{background:var(--navy);min-height:94vh;display:flex;flex-direction:column;
  justify-content:flex-end;padding:0;position:relative;overflow:hidden;}
.cover-glow{position:absolute;inset:0;background:
  radial-gradient(ellipse at 15% 70%,rgba(201,168,76,.07),transparent 48%),
  radial-gradient(ellipse at 85% 25%,rgba(138,48,48,.05),transparent 48%),
  radial-gradient(ellipse at 50% 50%,rgba(58,90,138,.04),transparent 60%),
  linear-gradient(180deg,#010306,#020408 60%,#030810);}
.cover-top{padding:48px 72px 0;position:relative;z-index:2;
  display:flex;justify-content:space-between;align-items:flex-start;}
.cover-logo{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;
  color:rgba(255,255,255,.38);letter-spacing:2px;}
.cover-tag{font-size:7.5px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  color:var(--gold-dk);border:1px solid rgba(201,168,76,.2);padding:5px 12px;}
.cover-body{padding:64px 72px 80px;position:relative;z-index:2;}
.cover-ey{font-size:8.5px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  color:rgba(90,128,112,.85);display:flex;align-items:center;gap:14px;margin-bottom:22px;}
.cover-ey::before{content:'';width:30px;height:1px;background:rgba(90,128,112,.65);}
.cover-h1{font-family:'Playfair Display',serif;font-size:clamp(44px,6.5vw,104px);
  font-weight:400;line-height:.87;color:#fff;letter-spacing:-2px;margin-bottom:22px;}
.cover-h1 em{font-style:italic;color:var(--gold);}
.cover-h1 .dim{color:rgba(255,255,255,.45);}
.cover-rule{display:flex;align-items:center;gap:14px;margin:24px 0;}
.cover-rule-line{flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);}
.cover-rule-dot{width:6px;height:6px;background:var(--gold);transform:rotate(45deg);flex-shrink:0;}
.cover-sub{font-family:'Playfair Display',serif;font-size:clamp(15px,2vw,21px);
  font-weight:300;font-style:italic;color:var(--tl);max-width:720px;line-height:1.62;margin-bottom:44px;}
.cover-stats{display:grid;grid-template-columns:repeat(5,1fr);
  max-width:820px;border:1px solid rgba(201,168,76,.2);}
.cstat{padding:16px 18px;border-right:1px solid rgba(201,168,76,.14);text-align:center;}
.cstat:last-child{border-right:none;}
.cstat-n{font-family:'Playfair Display',serif;font-size:26px;color:var(--gold);display:block;line-height:1;}
.cstat-l{font-size:7px;letter-spacing:2.5px;text-transform:uppercase;
  color:rgba(255,255,255,.24);font-weight:700;display:block;margin-top:3px;}

/* PROBLEM STATEMENT — TOP 5 */
.prob{background:#030609;padding:52px 72px;border-bottom:3px solid var(--gold);}
.prob-kk{font-size:8px;letter-spacing:5px;text-transform:uppercase;font-weight:700;
  color:rgba(90,128,112,.8);display:flex;align-items:center;gap:12px;margin-bottom:20px;}
.prob-kk::before{content:'';width:18px;height:1px;background:rgba(90,128,112,.65);}
.prob-h2{font-family:'Playfair Display',serif;font-size:clamp(22px,3vw,42px);
  font-weight:400;color:#fff;margin-bottom:12px;}
.prob-h2 em{font-style:italic;color:var(--gold);}
.prob-sub{font-family:'Georgia',serif;font-size:14.5px;color:var(--tl);
  line-height:1.75;max-width:800px;margin-bottom:30px;}
.top5-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.top5-item{padding:20px 22px;border:1px solid var(--rule);background:rgba(255,255,255,.02);}
.top5-item.no1{border-color:rgba(201,168,76,.35);background:rgba(201,168,76,.04);grid-column:1/-1;}
.top5-n{font-family:'Playfair Display',serif;font-size:44px;color:rgba(201,168,76,.12);
  display:block;line-height:1;margin-bottom:5px;float:right;margin-left:16px;}
.top5-item.no1 .top5-n{font-size:64px;color:rgba(201,168,76,.18);}
.top5-title{font-family:'Playfair Display',serif;font-size:18px;font-style:italic;color:#fff;margin-bottom:6px;}
.top5-item.no1 .top5-title{font-size:22px;}
.top5-why{font-family:'Georgia',serif;font-size:12.5px;color:var(--tl);line-height:1.6;}
.top5-crack{font-size:8px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;
  color:var(--gold-dk);display:block;margin-top:10px;padding-top:8px;border-top:1px solid var(--rule);}

/* CATEGORY SECTIONS */
.cat-section{border-top:6px solid;}
.cat-intro{padding:44px 72px 18px;}
.cat-kk{font-size:8px;letter-spacing:4px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.cat-kk::before{content:'';width:18px;height:1px;background:currentColor;}
.cat-h2{font-family:'Playfair Display',serif;font-size:clamp(26px,3.8vw,54px);
  font-weight:400;line-height:.92;color:var(--ink);margin-bottom:10px;}
.cat-h2 em{font-style:italic;}
.cat-sub{font-family:'Georgia',serif;font-size:14.5px;color:#555;line-height:1.75;max-width:800px;margin-bottom:16px;}
.cat-sub p{margin-bottom:12px;}
.cat-sub strong{color:var(--ink);}

/* FRESH ANGLE CARDS */
.angles{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px;padding:0 72px 6px;}
.angle-card{padding:12px 14px;border:1px solid rgba(0,0,0,.06);background:rgba(255,255,255,.55);}
.angle-card.flagship{border-color:rgba(201,168,76,.45);background:linear-gradient(135deg,rgba(201,168,76,.1),rgba(201,168,76,.02));}
.angle-card.pastoral{border-color:rgba(58,90,138,.25);background:rgba(58,90,138,.03);}
.angle-card.apologetics{border-color:rgba(90,58,106,.2);background:rgba(90,58,106,.02);}
.angle-card.cultural{border-color:rgba(58,106,74,.2);background:rgba(58,106,74,.02);}
.angle-card.lament{border-color:rgba(138,80,48,.2);background:rgba(138,80,48,.02);}
.ac-top{display:flex;align-items:flex-start;gap:6px;margin-bottom:2px;}
.ac-num{font-family:'Playfair Display',serif;font-size:10px;color:rgba(138,110,48,.28);flex-shrink:0;padding-top:1px;}
.angle-card.flagship .ac-num{color:var(--gold-dk);font-size:12px;}
.ac-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:var(--ink);line-height:1.3;}
.angle-card.flagship .ac-title{font-size:14.5px;color:#180c00;}
.ac-sub{font-size:9.5px;color:#888;font-family:'Georgia',serif;font-style:italic;
  line-height:1.35;padding-left:20px;margin-bottom:3px;}
.ac-hook{font-size:8.5px;color:#666;font-family:'Georgia',serif;
  padding:4px 8px;border-left:2px solid;margin-left:20px;line-height:1.4;}

/* STRATEGIC NEXT STEPS PANEL */
.nextstep-panel{margin:10px 72px 36px;border:1px solid;overflow:hidden;}
.nsp-header{padding:16px 22px;display:flex;align-items:center;gap:14px;}
.nsp-icon{font-size:22px;}
.nsp-title{font-family:'Playfair Display',serif;font-size:18px;font-style:italic;color:#fff;}
.nsp-sub{font-size:10px;color:rgba(255,255,255,.5);letter-spacing:1px;margin-top:2px;}
.nsp-body{padding:20px 22px;background:rgba(255,255,255,.96);}
.nsp-steps{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px;}
.nsp-step{padding:12px 16px;border-left:3px solid;background:rgba(0,0,0,.02);}
.nsp-step-label{font-size:7px;letter-spacing:2.5px;text-transform:uppercase;
  font-weight:700;display:block;margin-bottom:4px;}
.nsp-step-title{font-family:'Playfair Display',serif;font-size:13.5px;font-style:italic;
  color:var(--ink);display:block;margin-bottom:3px;}
.nsp-step-text{font-family:'Georgia',serif;font-size:11.5px;color:#555;line-height:1.5;}
/* PITCH CARDS */
.pitch-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:6px;}
.pitch-card{padding:14px 16px;border:1px solid;border-radius:0;}
.pitch-card.seven{border-color:rgba(201,168,76,.4);background:rgba(201,168,76,.05);}
.pitch-card.twentyone{border-color:rgba(58,90,138,.3);background:rgba(58,90,138,.04);}
.pitch-card.custom{border-color:rgba(58,106,74,.3);background:rgba(58,106,74,.04);}
.pc-eyebrow{font-size:7px;letter-spacing:3px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:6px;margin-bottom:7px;}
.pitch-card.seven .pc-eyebrow{color:var(--gold-dk);}
.pitch-card.twentyone .pc-eyebrow{color:var(--blue);}
.pitch-card.custom .pc-eyebrow{color:var(--green);}
.pc-title{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;
  color:var(--ink);margin-bottom:5px;}
.pc-desc{font-family:'Georgia',serif;font-size:11px;color:#555;line-height:1.55;margin-bottom:8px;}
.pc-cta{font-size:7.5px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;
  display:flex;align-items:center;gap:5px;}
.pitch-card.seven .pc-cta{color:var(--gold-dk);}
.pitch-card.twentyone .pc-cta{color:var(--blue);}
.pitch-card.custom .pc-cta{color:var(--green);}
.pc-cta::before{content:'→';}

/* WHAT MAKES IT FRESH — THE CRACK */
.crack-box{margin:0 72px 8px;padding:14px 18px;border-left:4px solid var(--gold);
  background:rgba(201,168,76,.04);}
.crack-box p{font-family:'Playfair Display',serif;font-size:14px;font-style:italic;
  color:var(--ink);line-height:1.55;}
.crack-box span{font-size:8px;letter-spacing:2px;text-transform:uppercase;
  font-weight:700;color:var(--gold-dk);display:block;margin-bottom:5px;}

.hdiv{height:3px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.25),transparent);}

/* BACK */
.back{background:#010406;padding:52px 72px;text-align:center;}
.bq{font-family:'Playfair Display',serif;font-size:clamp(14px,2vw,20px);
  font-style:italic;color:var(--cream);max-width:780px;margin:0 auto 18px;line-height:1.55;}
.ba{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:700;}
.bc{margin-top:14px;font-size:12px;color:var(--tm);}
.bc a{color:var(--gold-lt);text-decoration:none;}
.lm{font-family:'Playfair Display',serif;font-size:30px;color:#fff;font-style:italic;margin-top:24px;}

@media(max-width:960px){
  .cover-top,.cover-body,.prob,.cat-intro,.angles,.nextstep-panel,.crack-box,.back{
    padding-left:28px;padding-right:28px;}
  .nextstep-panel{margin-left:28px;margin-right:28px;}
  .crack-box{margin-left:28px;margin-right:28px;}
  .angles{grid-template-columns:1fr 1fr;}
  .top5-grid{grid-template-columns:1fr;}
  .top5-item.no1{grid-column:auto;}
  .nsp-steps{grid-template-columns:1fr;}
  .pitch-row{grid-template-columns:1fr;}
}
@media(max-width:600px){
  .angles{grid-template-columns:1fr;}
  .cover-stats{grid-template-columns:repeat(3,1fr);}
}
"""

def angle(num, title, sub, hook, cls=""):
    cls_str = f"angle-card {cls}".strip() if cls else "angle-card"
    return f'''<div class="{cls_str}">
  <div class="ac-top"><span class="ac-num">{e(str(num))}</span><span class="ac-title">{e(title)}</span></div>
  <p class="ac-sub">{e(sub)}</p>
  <div class="ac-hook" style="border-color:rgba(201,168,76,.3);">{e(hook)}</div>
</div>'''

def nsp(label, title, text, acc):
    return f'''<div class="nsp-step" style="border-color:{acc};">
  <span class="nsp-step-label" style="color:{acc};">{e(label)}</span>
  <span class="nsp-step-title">{e(title)}</span>
  <p class="nsp-step-text">{e(text)}</p>
</div>'''

def pitch(kind, eyebrow, title, desc, cta, cls):
    return f'''<div class="pitch-card {cls}">
  <p class="pc-eyebrow">{e(eyebrow)}</p>
  <p class="pc-title">{e(title)}</p>
  <p class="pc-desc">{e(desc)}</p>
  <p class="pc-cta">{e(cta)}</p>
</div>'''

# ═══════════════════════════════════════════════════
# THE FIVE HARDEST SUNDAYS — PROBLEM STATEMENT
# ═══════════════════════════════════════════════════
TOP5 = [
  ("no1","1","Easter","You have preached it 5 to 20 times. The congregation knows how the story ends before you begin. The title 'He Is Risen' produces zero narrative tension. The challenge is not theological — the resurrection is the most defensible claim in the text. The challenge is rhetorical: how do you create surprise on the most unsurprising Sunday of the year. The freshness has to come from the angle, not the event.","The crack: preach to the person who does not believe it yet — the skeptic in the room, the grieving person who desperately wants it to be true, the longtime attender for whom the story has gone stale. The resurrection is always new to someone in the room. Find that person and preach to them."),
  ("","2","Christmas Eve","The highest percentage of unchurched attenders. The most culturally loaded Sunday of the year. The congregation arrives expecting the familiar story and the familiar feeling — and the pastor who gives them exactly that has confirmed the suspicion that church is a nostalgia delivery service. The challenge: preach the most familiar story with the most unexpected angle to the most diverse room of the year.","The crack: the incarnation is actually a scandal. God became human — not a metaphor, not a symbol, a biological fact. The scandal of that is lost in candles and carols. Preach the scandal."),
  ("","3","Mother's Day","The most theologically thin Sunday on the Protestant calendar. The culture owns the frame before the pastor opens their mouth. Twenty percent of the congregation is experiencing Mother's Day as grief — infertility, loss, estrangement, abuse, a mother who is gone. The pastor who preaches sentimentally to that room has failed them. The challenge: honor the occasion, pastor the pain, and find the text that can carry both.","The crack: every great Mother's Day sermon is actually about someone in the room for whom the day is complicated. Preach to that person and the celebration takes care of itself."),
  ("","4","End-of-Year Giving","The congregation suspects the sermon is about money before the pastor stands up. They have heard the stewardship message annually for years and are measuring whether this year's version is more or less manipulative than last year's. The challenge: preach generosity as formation — what giving does to the giver — rather than stewardship as obligation — what the budget requires of the congregation.","The crack: the most powerful stewardship sermon is never about the church's need. It is about the congregation's formation. What does holding tightly to money do to a person's soul? What does releasing it do? Preach the anthropology, not the ask."),
  ("","5","New Year Sunday","Resolution culture owns January 1 so completely that the secular frame makes the pastor's theological frame feel like a competitor. The congregation arrives having already failed their resolutions twice in the last three years and is simultaneously hopeful and skeptical. The challenge: offer something the self-help industry cannot — not a better strategy for change but a different kind of change, rooted in a different kind of power.","The crack: the gospel does not offer a better resolution. It offers a resurrection. The person who needs a different year does not need a better plan — they need a different identity. Preach the new creation, not the new plan."),
]

# ═══════════════════════════════════════════════════
# CATEGORY 1: EASTER — 62 FRESH ANGLES
# ═══════════════════════════════════════════════════
EASTER = [
  # --- SKEPTIC / APOLOGETICS TRACK ---
  ("★","The Most Verified Claim in Ancient History","The resurrection as the best-attested event in the ancient world — and what that demands of you","You cannot dismiss it without engaging it. You cannot engage it without being changed by it.","flagship"),
  ("2","What Five Hundred Witnesses Were Willing to Die For","The martyrdom evidence for the resurrection","People die for what they believe. Almost no one dies for what they know is a lie.","apologetics"),
  ("3","The Empty Tomb — A Forensic Analysis","If the resurrection did not happen, someone has to explain the empty tomb","Every alternative theory fails under examination. Only one explanation survives the evidence.","apologetics"),
  ("4","The Hallucination Theory — Why It Cannot Work","The psychological impossibility of a mass hallucination experienced by five hundred people","Hallucinations are not shared. What the disciples saw was not a shared hallucination.","apologetics"),
  ("5","Why the Disciples Could Not Have Stolen the Body","The practical impossibility of the most popular alternative explanation","Traumatized, hiding, afraid — these are not people who overpower Roman soldiers.","apologetics"),
  ("6","The First Easter Morning — Reconstructed","Treating the resurrection accounts as journalistic testimony","When you read them as journalism rather than liturgy, something new happens.","apologetics"),
  ("7","N.T. Wright Was Right","What the world's leading resurrection scholar discovered when he set out to disprove it","He went looking for the body. He found the argument for the resurrection.","apologetics"),
  # --- FRESH TEXTUAL ANGLES ---
  ("8","The Text You Missed — John 20:8","And he saw and believed — before he understood","Faith precedes comprehension. Always.",""),
  ("9","What the Angels Said That Nobody Quotes","The full angel announcement beyond 'He is not here'","Why are you looking for the living among the dead is the question every generation has to answer.",""),
  ("10","The Smell of the Garden","The sensory details of Easter morning that the paintings always leave out","Resurrection happened in a body, not a symbol. The disciples smelled it before they saw it.",""),
  ("11","Mary's Three Mistakes","She thought he was the gardener — and what that confusion teaches","We look for the risen Christ where we last left the dead Jesus.",""),
  ("12","Why Jesus Appeared to Peter Specifically","The most targeted resurrection appearance in the text","Jesus did not appear to the person who deserved it first. He appeared to the person who needed it most.","flagship"),
  ("13","The Wound That Thomas Touched","Not doubting Thomas — the Thomas who asked the question the rest were afraid to ask","The wounds were not healed. They were glorified. Jesus kept them.","pastoral"),
  ("14","The Walk That Took Seven Miles","Why two disciples left Jerusalem at the worst possible moment","Grief makes us walk in the wrong direction. Jesus meets us walking.","pastoral"),
  ("15","The Two On the Road Did Not Recognize Him","What the Emmaus road teaches about how we encounter the risen Christ","We recognize him in the breaking of the bread. Not before.",""),
  ("16","He Showed Them His Hands and His Side","The resurrection body was not pristine — it was scarred","The risen Jesus is identifiable by his wounds. This changes everything about suffering.","flagship"),
  # --- PASTORAL / FELT NEED TRACK ---
  ("17","Easter for the Person Who Needs It To Be True","Preaching the resurrection to the grieving, the doubting, and the desperate","If Easter is true, everything changes. If it is not, nothing matters. The stakes are that high.","pastoral"),
  ("18","What the Resurrection Says to Your Greatest Fear","The specific fear that Easter is designed to address","Every fear, at its root, is a fear of death. Easter speaks to the root.","pastoral"),
  ("19","Resurrection in the Middle of Your Winter","The Easter message for the person whose life does not currently feel like spring","The resurrection happened in a cemetery. It does not require favorable conditions.","pastoral"),
  ("20","The Grief That Easter Did Not Fix","When the resurrection is true and the loss is still real","Mary wept at the empty tomb. The resurrection does not eliminate grief. It reframes it.","lament"),
  ("21","Easter and the Chronic Illness","What the resurrection body means for the person whose body has betrayed them","The resurrection is a promise about your specific body. Paul is not speaking metaphorically.","pastoral"),
  ("22","Easter for the Parent Who Buried a Child","The most honest Easter sermon for the most devastating loss","If Easter is true, death is not the last word about your child. That is either the most important thing you have ever heard or the most insulting. It depends entirely on whether it is true.","lament"),
  ("23","The Day After Easter","The Sunday that most churches ignore and should not","What the disciples did Monday is the formation question Easter always leaves open.",""),
  # --- THEOLOGICAL DEPTH TRACK ---
  ("24","The Resurrection Is Not a Metaphor","The costly mistake of spiritualizing the bodily resurrection","Paul says if there is no bodily resurrection, our faith is worthless. He is not speaking poetically.","flagship"),
  ("25","The New Creation Has Already Begun","N.T. Wright's insight: Easter is not escape from the world but the beginning of its renewal","The risen Jesus is the first piece of the new creation. Not the ticket out.",""),
  ("26","What the Resurrection Means for Monday","The vocational and ethical implications of a bodily resurrection","If bodies matter enough to be raised, what you do in a body matters eternally.",""),
  ("27","Easter and Justice","What the resurrection of the unjustly executed victim of empire says to every unjust system","The cross was the empire's final word. The resurrection was God's.","cultural"),
  ("28","Easter Is a Political Statement","The Roman empire said 'Caesar is Lord.' Easter said 'Jesus is Lord.' Those two claims cannot coexist.","The earliest Christians were not arrested for piety. They were arrested for treason.","cultural"),
  ("29","Why Easter Keeps Happening","The congregation that treats Easter as annual instead of daily has misread the text","The resurrection is not a calendar event. It is a present-tense reality.",""),
  ("30","The First Fruits of the New Creation","1 Corinthians 15:20 as the most underpreached Easter text","First fruits means the rest is coming. Easter is the down payment on the whole harvest.",""),
  ("31","Resurrection Before Restoration","The order of events in the new creation — and what it means that Jesus went first","He did not restore himself to the old creation. He inaugurated the new one.",""),
  # --- OUTREACH / UNCHURCHED TRACK ---
  ("32","To the Person Who Came Because Someone Made Them","The honest Easter sermon for the reluctant attender","You did not choose to be here today. The question is whether what you hear today changes that.","outreach"),
  ("33","If This Is the First Time You Have Heard This","Preaching the resurrection to the person who has never considered it","This is either the best news you have ever heard or the most preposterous claim you have ever encountered. It is not possible to be neutral about it.","outreach"),
  ("34","One Reason Intelligent People Believe the Resurrection","The condensed apologetic for the skeptic in the Easter service","Not faith instead of evidence. Faith because of it.","apologetics"),
  ("35","What the Resurrection Asks You To Do With It","The response Easter invites that is different from the response Christmas invites","Christmas asks you to receive. Easter asks you to respond.","outreach"),
  # --- CREATIVE / NARRATIVE ---
  ("36","The Centurion's Easter","The resurrection from the perspective of the soldier assigned to guard the tomb","He was paid to make sure the body stayed put. He has some explaining to do on Monday morning.","narrative"),
  ("37","Mary Before She Recognized Him","The moment between the first sight and the name","She thought he was the gardener. He asked her one question. Her name.","narrative"),
  ("38","What Peter Told His Wife That Night","Imaginative reconstruction of Easter evening in the disciples' homes","The stories told in every house in Jerusalem that night changed every house that told them.","narrative"),
  ("39","The Other Mary — The One at the Tomb","The overlooked witness who stayed when the disciples left","Mary Magdalene stayed when everyone else left. She got there first.","narrative"),
  ("40","The Grave Clothes as Evidence","The specific forensic detail John noticed that convinced him","The linen strips. The burial cloth folded separately. Not a body that was moved — a body that left.",""),
  ("41","The Room Where They Were Hiding","The upper room at Easter evening — what happened in the fear","He appeared in a locked room. He did not need the door. He stood among them.",""),
  ("42","What Peter Said at Pentecost About Easter","Acts 2 as the earliest Easter sermon — how the first preacher preached it","This man, handed over to you, raised by God. The eyewitness account.",""),
  ("43","The Forty Days Nobody Preaches","What happened between Easter and Ascension — the formation gap","Jesus spent forty days with the disciples after the resurrection. He was teaching them something.",""),
  ("44","Paul's Conversion as an Easter Sermon","The Damascus Road as a resurrection appearance","Paul's testimony: I persecuted Christians until the risen Jesus appeared to me. That is Easter.","apologetics"),
  ("45","The Resurrection Appearances in Order","Walking through every post-resurrection appearance and what each one reveals","He appeared to Mary, then Peter, then the twelve, then five hundred. The appearances have a logic.",""),
  # --- SERIES STARTERS ---
  ("46","Easter Is the Beginning of the Series","The sermon that launches what Easter started — not ends it","Easter Sunday should be the most exciting Sunday of the year to have a small group signup table.","flagship"),
  ("47","The Risen Life — A 7-Day Journey Begins Today","Launching the post-Easter formation arc from the Easter sermon itself","The seven days after Easter are the most important formation window of the year. Start them today.","flagship"),
  ("48","What You Do With Easter Monday","The specific Monday application of the most significant Sunday","The resurrection has a Tuesday implication. Name it from the pulpit on Sunday.",""),
  ("49","The Easter Series — Six Weeks of Resurrection Living","What the congregation does in the weeks after Easter when the formation system is ready","Easter is the launch of the best series of the year — not the conclusion of Lent.","flagship"),
  ("50","He Is Alive — Now What","The formation question every Easter sermon should end with but most do not","The resurrection is not a conclusion. It is a commission.",""),
  ("51","Easter and the 21-Day Resurrection Challenge","The post-Easter formation arc that takes the congregation through the resurrection appearances","Twenty-one days. One resurrection appearance per day. The congregation arrives at the ascension.","flagship"),
  ("52","The Fresh Angle Your Congregation Has Never Heard","Compiling the eight least-preached Easter texts and why they matter","Eight texts. Eight angles. Choose the one your congregation most needs this year.","flagship"),
  ("53","The Stone Was Not Rolled Away For Jesus","The stone was rolled away for the disciples — he had already left","The stone was not a barrier for the risen Christ. It was rolled away as evidence for the witnesses.",""),
  ("54","Two Facts That Demand an Explanation","The empty tomb and the post-resurrection appearances — and the only explanation that accounts for both","Two facts. One explanation that works. Every alternative fails on one or the other.","apologetics"),
  ("55","Easter in Gethsemane","The prayer that preceded the cross and the resurrection that answered it","He asked the Father to take the cup if possible. The resurrection is the Father's answer to that prayer.",""),
  ("56","The Disciples Recognized the Risen Jesus by His Wounds","The identification that changed everything","The wounds were not evidence of what he suffered. They were proof of who he was.",""),
  ("57","Everything Rides on This","1 Corinthians 15:14 — If Christ has not been raised, our preaching is worthless","Paul did not say 'it is symbolically important.' He said 'if it did not happen, we have nothing.'","flagship"),
  ("58","The Resurrection Body Is the Template for Yours","What Paul says the resurrection means for every believer's body","Your body will be raised. Not your soul. Your body. Paul is quite specific.",""),
  ("59","What Changed Between Thursday Night and Sunday Morning","The disciples who hid on Friday were preaching in public on Sunday — something happened","The transformation of the disciples is itself evidence. Defeated people do not start world religions.","apologetics"),
  ("60","The Cross Was Not Easter — The Cross Was Friday","The sermon that refuses to let the congregation collapse the two events","Good Friday and Easter Sunday are not the same event with different names. They are two distinct acts.",""),
  ("61","Easter and the Empty Promises the World Has Made You","What the resurrection offers that no self-improvement program can","The world offers a better version of your old self. Easter offers a new creation.","outreach"),
  ("62","The Congregation That Lives Easter — Not Just Preaches It","Vision for the congregation whose life embodies resurrection","What would this congregation look like if its daily culture was shaped by the fact that Jesus rose.","flagship"),
]

# ═══════════════════════════════════════════════════
# CATEGORY 2: CHRISTMAS EVE — 62 FRESH ANGLES
# ═══════════════════════════════════════════════════
CHRISTMAS = [
  ("★","The Scandal of the Incarnation","God becoming human was not beautiful at first — it was offensive","The first disciples did not find the incarnation comforting. They found it scandalous. We have domesticated what should still disturb us.","flagship"),
  ("2","John 1 on Christmas Eve","The most theologically powerful Christmas text is not in Luke 2","The Word was with God and the Word was God. And the Word became flesh. Luke gives you the manger. John gives you the cosmos.","flagship"),
  ("3","What the Shepherds Smelled Like","The incarnation came first to the people nobody else invited","God sent the birth announcement to people who worked nights and were not welcome in the synagogue. That is not an accident.",""),
  ("4","Christmas as Invasion","The kingdom of God did not arrive peacefully — it invaded","The nativity is not a domestic scene. It is a beachhead. The kingdom arrived in occupied territory.","cultural"),
  ("5","What Herod Knew That the Inn Didn't","The political threat of the incarnation","Herod tried to kill him because he understood what the innkeeper missed — this changes everything.","cultural"),
  ("6","The Inn That Had No Room","Not a story about innkeepers — a story about what we make room for","Every generation has to answer the innkeeper's question. Every generation gives the same answer.","flagship"),
  ("7","The Word Became Flesh and Moved Into the Neighborhood","Eugene Peterson's translation as the Christmas sermon","The Word did not drop in for a visit. The Word moved in. Permanently.",""),
  ("8","Christmas for the Person Who Does Not Feel It This Year","The most honest Christmas Eve sermon","You came tonight because you were supposed to. What you did not expect was a message for you specifically.","pastoral"),
  ("9","What the Angels Were Actually Saying","The full content of the Christmas announcement beyond 'Glory to God'","Good news for all people. That is not a musical cue. That is a declaration.",""),
  ("10","Simeon Had Been Waiting His Entire Life","The old man who held the baby and what he saw","He had been told he would not die until he saw the Messiah. He had been waiting. This is what waiting for something that actually arrives looks like.","pastoral"),
  ("11","The God Who Chose Poverty","The incarnation began in the most economically vulnerable circumstances possible","He was not born into poverty accidentally. The Son of God chose the manger. That choice is theological.",""),
  ("12","Anna the Prophetess — The Woman Nobody Preaches","The eighty-four-year-old widow who recognized the Messiah when the temple missed him","She had been praying in the temple for decades. She was there when it mattered.","women"),
  ("13","The Magnificat as the Most Dangerous Christmas Song","Mary's song is not gentle — it is revolutionary","He has brought down rulers from their thrones. He has filled the hungry. This is not a lullaby.","cultural"),
  ("14","What Bethlehem Was Actually Like","The archaeology and history of a first-century village at census time","Nothing about it was romantic. Which is precisely the point.",""),
  ("15","Christmas and the Loneliness Epidemic","What the incarnation says to the loneliest generation in American history","God's solution to human isolation was not a message — it was a person. He showed up.","pastoral"),
  ("16","Immanuel Is Not Past Tense","God with us — present tense, active voice, still happening","Christmas is not a memory. It is a present-tense reality.",""),
  ("17","The Christmas the Prophets Saw Coming","Preaching Isaiah 9, Isaiah 53, and Micah 5 as the setup to Luke 2","The birth of Jesus is not a surprise to the Old Testament. The Old Testament is the longest advent.",""),
  ("18","What Joseph Was Thinking","The most overlooked character in the nativity","He was going to divorce her quietly. He had a plan. Then an angel appeared. His plan was not good enough.","narrative"),
  ("19","The Risk of the Incarnation","What it cost God to become human — vulnerability, limitation, rejection","The omniscient chose not to know. The omnipotent chose to be helpless. The invulnerable chose to suffer.",""),
  ("20","Christmas Eve and the God Who Shows Up","The incarnation as the pattern — God always shows up in person","When God had a message, he sent prophets. When God wanted to save, he came himself.","flagship"),
  ("21","Not a Symbol — A Body","The incarnation is not a metaphor for spiritual connection","He had a heartbeat. He had a digestive system. He got tired. The incarnation is disturbingly physical.",""),
  ("22","The Refugee Family at Christmas","Joseph, Mary, and the infant Jesus — asylum seekers in Egypt","The Son of God was a refugee. That is not an argument. It is a text.","cultural"),
  ("23","Christmas and the Person Who Has Lost Everything This Year","The incarnation for the congregation navigating devastation at Christmas","God did not enter human experience at its best. He entered it at one of its most vulnerable moments.","lament"),
  ("24","Christmas Eve for the First-Timer","The honest Christmas Eve sermon for the person who does not know why they are there","You are here and you are not sure why. That might be the most important thing about tonight.","outreach"),
  ("25","The Light That the Darkness Could Not Overcome","John 1:5 as the Christmas text for the congregation living in real darkness","The darkness did not understand it. The darkness did not win. Those are different claims.","pastoral"),
  ("26","What God Sounds Like as a Newborn","The silence of the nativity — before the words","For thirty years after the nativity, God mostly said nothing. He was observing. Learning. Growing.",""),
  ("27","The Name He Was Given and Why","What Jesus means and why the angel specified it","He was given the name before he did anything to deserve it. The name was not earned — it was announced.",""),
  ("28","Christmas and the Person Who Prayed for Something Else","When the year's biggest prayer was not answered the way you asked","Mary did not ask to be the mother of the Messiah. Elizabeth did not ask to be barren for decades. God arrives on his own schedule.","pastoral"),
  ("29","The Three Gifts and What They Meant","The Magi's gifts as theological statements, not tourist purchases","Gold for a king. Frankincense for a priest. Myrrh for a burial. They knew more than the shepherds did.",""),
  ("30","Christmas and the City That Does Not Notice","Bethlehem was full of people who missed the biggest event in human history","The census was happening. The inn was full. Two people were having a baby in a stable. Nobody looked twice.",""),
  ("31","The Theology of a Manger","What it means that the first cradle was a feeding trough","He was placed in the place where animals come to be fed. That is the whole gospel in an image.","flagship"),
  ("32","What Christmas Means If It Is True","The logical implications of taking the incarnation seriously","If God became human, nothing about your life is ordinary. Every person is someone God thought worth dying for.","outreach"),
  ("33","Christmas Eve Communion — Body and Blood","The most theologically coherent Christmas Eve service","We celebrate the body that was born tonight. We remember the body that was broken. We are fed by the body that rose.","eucharist"),
  ("34","The Star That Was Visible Only to Those Who Were Looking","The Magi and the congregation that is looking for signs","The star was not secret. It was there for anyone who looked. The Magi were looking.",""),
  ("35","God Became Small So We Could Become Large","The exchange at the heart of the incarnation","He did not become human to shame us. He became human to elevate us.",""),
  ("36","What Did the Animals Know","The stable as a formation image — the created world at the incarnation","He who made the animals was placed among them on his first night. Creation received what the city refused.",""),
  ("37","The Long Silence Before Bethlehem","Four hundred years between Malachi and Matthew","For four centuries, God was silent. Then he cried. In a stable. At night. To shepherds.","flagship"),
  ("38","Elizabeth's Recognition — Before Anyone Else Knew","The visit of Mary to Elizabeth as the first Christmas testimony","She recognized the incarnation before there was a manger, a star, or a shepherd.",""),
  ("39","Christmas in the Psalms","Preaching the Christmas text from Psalm 2, Psalm 22, Psalm 110","The Psalms told the story centuries before the story happened.",""),
  ("40","The First Christmas in John's Prologue","Eight verses that contain more theology than most entire Christmas sermons","In the beginning was the Word. Every other Christmas text is a footnote to that sentence.","flagship"),
  ("41","Christmas and the Unanswered Letter","Writing to God and wondering why the answer has not come","God's longest answer to human prayer is the incarnation. He did not write back. He showed up.","pastoral"),
  ("42","What the Shepherds Told Mary","Luke 2:19 — Mary treasured all these things and pondered them","She heard what the shepherds said. She kept it. She turned it over. She did not explain it. She treasured it.",""),
  ("43","Christmas Eve and the Person Who Has Not Believed in Years","The gentle re-invitation","You are here. That is not nothing. Something brought you. Consider whether that something might be Someone.","outreach"),
  ("44","The Baby Who Would Say I Am the Way","The infant Jesus and the adult Jesus — what did Mary know","She was holding the baby who would later say I am the resurrection. She did not know that yet.",""),
  ("45","The Cradle and the Cross","Christmas and Easter as one continuous movement","They put him in a manger because there was no room. They put him in a tomb because there was no mercy. The two events are one story.","flagship"),
  ("46","Christmas and the Theology of Smallness","God chose the smallest — smallest nation, smallest town, smallest family, smallest space","He who is everywhere chose to be somewhere. He who is everything chose to need something.",""),
  ("47","What the Inn Offered That the Stable Did Not","The sermon that finds the stable superior to the inn","The inn had warmth and noise and people and normalcy. The stable had stars and silence and God.",""),
  ("48","Christmas Without Sentimentality","The formation sermon for the congregation that has been moved by Christmas and unchanged by it","If the incarnation is true, sentimentality is the wrong response. Transformation is.","flagship"),
  ("49","The Child Who Would Not Stay a Child","The nativity as the beginning of everything, not the center of everything","We celebrate the birth. The angels celebrated the birth. But the birth was not the point. It was the beginning.",""),
  ("50","Christmas and the New Covenant","The incarnation as the fulfillment of every covenant promise","Every covenant God made pointed here. This is the yes to every promise.",""),
  ("51","Silent Night — What Was Actually Silent","Dissecting the carol that tells the theological truth accidentally","Silent night. Holy night. All is calm. None of that was literally true. The silence that matters was cosmic.",""),
  ("52","The God Who Did Not Stay Distant","The incarnation as God's answer to his own absence","He did not send instructions. He did not send a program. He sent himself.","flagship"),
  ("53","Christmas for the Cynic","The honest Christmas Eve sermon for the person who stopped believing in magic a long time ago","This is not a fairy tale. It is a historical claim. Which makes it either the most important thing that ever happened or a lie. Fairy tales are not that uncomfortable.","apologetics"),
  ("54","What the Star Was — And What It Was Not","The astronomical, historical, and theological discussion of the star of Bethlehem","Whatever it was, the Magi saw it, interpreted it correctly, and made a journey that changed history.",""),
  ("55","The First Christmas Morning","What Christmas Day felt like for Mary — exhausted, bewildered, holding God","She was a teenager. She was not in her home. She had just given birth. She was holding the incarnation.","pastoral"),
  ("56","Christmas and the People Who Are Missing","The Christmas Eve sermon for the congregation grieving an empty seat","The Christmas joy is real. So is the Christmas grief. The incarnation is the only thing that holds both.","lament"),
  ("57","The Generation That Did Not See It","The prophets who wrote about it and died before it happened","Isaiah did not live to see the child born of a virgin. He wrote about it centuries before.",""),
  ("58","The Gift You Cannot Wrap","The Christmas sermon about what God actually gave","He gave himself. Not a representative. Not a proxy. Himself. Fully. Permanently.","flagship"),
  ("59","On This Night Everything Changed","The historical marker — the world before and after December 25","Before this night, the fullest revelation of God available was a burning bush. After this night, it was a face.",""),
  ("60","Christmas Eve — Do You Know What Night This Is","The invitation to the congregation to stop performing Christmas and receive it","You have prepared for tonight. You dressed up. You came. You sang. Have you received what was given.","outreach"),
  ("61","The Incarnation Is Not Seasonal","The Christmas sermon that refuses to end with Christmas","We celebrate the birth annually. We live in the reality of it daily. The difference between those two things is formation.","flagship"),
  ("62","What Christmas Asks of You","The sermon that closes Christmas Eve with a specific formation response","The Magi brought something. The shepherds went and told. Mary pondered. What will you do with what you received tonight.","outreach"),
]

# ═══════════════════════════════════════════════════
# CATEGORY 3: MOTHER'S DAY — 63 FRESH ANGLES
# ═══════════════════════════════════════════════════
MOTHERS = [
  ("★","For the Person for Whom Today Is Complicated","The sermon that acknowledges every person in the Mother's Day room","Before we celebrate mothers, we acknowledge that for some of you today is the hardest Sunday of the year. That is the room we are in.","lament"),
  ("2","The Mother Who Changed the World — Before Anyone Knew Her Name","The anonymous mothers of Scripture who formed the people who changed history","Jochebed put Moses in a basket. History does not remember her name. Moses does.","flagship"),
  ("3","Proverbs 31 Was Written By a Man — About His Mother","The text as a son's tribute, not a woman's job description","Lemuel wrote this poem about his own mother. It is not a performance standard. It is a love letter.",""),
  ("4","What Hannah Knew That Eli Missed","The prayer of the barren woman who would not stop praying","She was praying so intensely that the priest thought she was drunk. She was not drunk. She was desperate. God answered.","pastoral"),
  ("5","The Mothering God — Isaiah 49:15","Can a mother forget the baby at her breast? The text that uses mothering to describe God","Scripture uses maternal imagery for God. Not to make God female — to make God comprehensible to us.","flagship"),
  ("6","Ruth Was Not a Mother — Yet","The formation of faithfulness before the calling was given","Her faithfulness to Naomi came before the child who would change history. She did not know that.",""),
  ("7","The Magnificat — What Mary Actually Sang","The most radical Mother's Day text in the Bible","She sang about overthrowing the powerful and feeding the hungry. This is the first Christian sermon. It was preached by a teenager.","cultural"),
  ("8","Elizabeth — The First Person to Recognize Jesus","The elderly cousin who recognized what nobody else had seen","She was six months pregnant. Mary was days pregnant. Elizabeth recognized the incarnation before it was visible.",""),
  ("9","Lois and Eunice — The Grandmothers Who Formed an Apostle","2 Timothy 1:5 — the formation that traveled through generations","Paul said Timothy's sincere faith first lived in his grandmother Lois and his mother Eunice. Formation is generational.",""),
  ("10","The Mother Who Let Go — Mary at the Wedding, Mary at the Cross","The two moments that define Mary's formation as a mother","At Cana she released him into his ministry. At Golgotha she released him to his death. Both required everything.","flagship"),
  ("11","The Woman at the Well Was Someone's Daughter","Reframing the Samaritan woman through the lens of what her mother wanted for her","Every adult with a complicated story was once a child whose mother had hopes for them.","pastoral"),
  ("12","Deborah — The Mother in Israel","The military leader and judge whose title was 'a mother in Israel'","She did not choose the title judge. She was called a mother. The title that mattered was relational.","women"),
  ("13","What Your Mother's Hands Taught You","The embodied formation that words cannot replicate","What a mother forms in a child is not primarily verbal. It is gestural, habitual, physical.","pastoral"),
  ("14","For the Motherless on Mother's Day","The honest pastoral sermon for the person whose mother is gone","Your grief today is not a failure of faith. It is a measure of love.","lament"),
  ("15","For the Person Who Is Estranged From Their Mother","The Mother's Day sermon that names the complicated relationship without fixing it","Not every mother-child relationship is redemption. The church has to be able to say that.","lament"),
  ("16","For the Mother Who Is Estranged From Her Child","The person in the room who is a mother but not to her child today","You are still a mother. The estrangement did not undo what you gave.","lament"),
  ("17","For the Infertile Woman on Mother's Day","The most courageous pastoral moment on the church calendar","If today is the hardest day of the year for you, you are seen. You are not overlooked. You are specifically invited into this sermon.","lament"),
  ("18","For the Mother Who Is Failing","The Mother's Day sermon for the woman who does not feel like a good mother","The mothers you are comparing yourself to are not real. The mother you are is.","pastoral"),
  ("19","For the Mother Who Did Not Get It Right","The grace that covers the gaps in every mother's story","The person God uses is never the person who got everything right. It is always the person who did not give up.","pastoral"),
  ("20","For the Adoptive Mother","The mother who chose","She did not have to. She did. The choice is the point.",""),
  ("21","For the Foster Mother","The woman who mothers the child who is not hers and may not stay","The most unrewarded mothering in the culture is the fostering that forms a child who may never come back.",""),
  ("22","For the Single Mother","The formation in the gap","She was doing two people's jobs with half the resources. Strength is not the right word. Neither is sacrifice. Formation is.","pastoral"),
  ("23","For the Stepmother","The complicated grace of entering a family already formed","She did not come first. She came willing. That is a different kind of strength.","pastoral"),
  ("24","For the Grandmother Raising Her Grandchildren","The second calling that came when the first was supposed to be finished","This was not what she planned. It was what was needed. She said yes.",""),
  ("25","What a Mother Knows That Nobody Taught Her","The formation knowledge that is not instinct and not education","She knows things about her child that are not in a book and not in her training. They are in relationship.","flagship"),
  ("26","The Last Conversation With My Mother","The pastoral message for the congregation that has lost a mother","What would you have said if you had known it was the last time.","lament"),
  ("27","The Formation That Happens Before You Can Remember","What the first three years deposit that the child never consciously receives","The most formative period of a human life is the period the person cannot recall.",""),
  ("28","What Your Mother Prayed for You That You Never Heard","The intercessory prayer that happened before you were old enough to understand","Monica prayed for Augustine for thirty-one years. He did not know. Then he became Augustine.","flagship"),
  ("29","The Mother Who Kept Going","The formation of perseverance in the parent who did not quit","She did not feel capable. She did not feel adequate. She kept going. That is the formation.","pastoral"),
  ("30","What Mothers Know About Waiting","The specific patience that parenthood forms","She waited for the first word, the first step, the first faith confession. Mothers know how to wait.",""),
  ("31","The Mother Who Released What She Raised","Hannah giving Samuel to the temple — the hardest act of formation","She asked for him. She received him. She gave him back. That sequence is the gospel in a family story.","flagship"),
  ("32","The Father Who Mothered","The men who did the mothering that mothers typically do — Joseph, Barnabas, Paul","I became your mother among you — Paul's image of himself as a nursing mother in 1 Thessalonians.","men"),
  ("33","The Church as Mother","The ancient concept of Mater Ecclesia — the church that mothers every believer","The congregation that forms, feeds, comforts, and disciplines is doing what the best mothers do.",""),
  ("34","What the Prodigal's Mother Was Doing While the Father Ran","The text does not mention the mother. That silence is not accidental.","Every family in that culture had a mother. She was present. The text just did not record what she felt.",""),
  ("35","Honor Your Mother — Even If It Is Complicated","The fifth commandment applied pastorally rather than sentimentally","Honor does not require pretending. It requires a specific kind of respect that is possible even when the relationship is not whole.","pastoral"),
  ("36","The Woman Who Lost the Coin — A Mother's Day Text","Luke 15 and the woman who sweeps the house until she finds what she lost","She does not stop looking. She celebrates when she finds it. She is one of the images Jesus uses for God.",""),
  ("37","The Best Mother's Day Sermon Is About Someone Else's Mother","The formation that comes from honoring a specific mother in the congregation","Every sermon that says 'mothers are wonderful' is generic. The sermon that honors one specific mother in this congregation is formation.",""),
  ("38","To the Mother Who Is Here Alone","The woman whose family did not come to church with her today","She came. She is here. She brought them when they were children. She comes now. She has not stopped.","pastoral"),
  ("39","What Mothers Do That the Economy Cannot Measure","The formation work that does not show up in any GDP calculation","The most important work in the culture is the work that produces people. Nobody pays for it.","cultural"),
  ("40","The Blessing That Changes a Child's Life","What it means to speak a blessing over a child and why most parents never do it","Isaac blessed Jacob. Jacob blessed his sons. The blessing was not sentiment. It was formation. It stayed.","flagship"),
  ("41","When the Mother Is the Child","The sandwich generation Sunday — caring for aging parents while raising children","She is the generation between. She is caring for her mother while her children watch how it is done.","pastoral"),
  ("42","The Quiet Courage of the Ordinary Mother","The mother who does not appear in headlines or testimony services but who is forming the people who do","Formation is mostly undramatic. The quiet act repeated ten thousand times is what it looks like.",""),
  ("43","Mary at the Cross","What a mother's love looks like when it cannot fix anything","She could not save him. She could not stop it. She stood there. That is what love does when it cannot do anything else.","lament"),
  ("44","The Formation Gap — What Happens When Mother's Day Is Not Enough","The church's responsibility beyond one Sunday per year","A culture that celebrates mothers one Sunday per year and devalues mothering every other Sunday is not actually honoring mothers.","cultural"),
  ("45","What Comes After Mother's Day","The pastoral care the church owes the people this Sunday surfaces","The 20% of the congregation for whom today was painful will be back next Sunday. Will the church be ready for them.","pastoral"),
  ("46","The Mother Who Did Not Live to See It","Raising children who became something the mother prayed for but did not see","She planted. Someone else watered. God gave the growth. She was gone by harvest.","lament"),
  ("47","A Letter to My Mother","The pastoral sermon format that opens with a specific and honest letter","Reading a real letter to a real mother — full of gratitude and complication — creates the formation space for the whole congregation.","narrative"),
  ("48","What You Would Change If You Could","The honest Mother's Day sermon about regret and grace","Every parent wishes they had done something differently. Grace speaks to the specific things, not just the general sentiment.","pastoral"),
  ("49","The Mothers Who Kept the Faith When the Culture Did Not","The church mothers in every generation who were the formation infrastructure","There is a woman in every congregation who has been the spiritual mother of the congregation for fifty years. She is probably not the senior pastor.","flagship"),
  ("50","The Hardest Mother's Day in Congregational History","When the congregation itself has been through something that makes Mother's Day complicated","After a loss, a crisis, or a trauma — Mother's Day is the occasion that surfaces everything.","pastoral"),
  ("51","The Generational Blessing — What You Give Your Children's Children","The formation that travels through generations","What you form in your children they will pass to their children without knowing it. You are not just raising the next generation. You are forming the one after that.","flagship"),
  ("52","The 7-Day Mother's Day Journey — Begins Today","Launching the post-Mother's Day formation arc from the pulpit","The formation conversation Mother's Day begins does not have to end with the bulletin.","flagship"),
  ("53","The Custom Mother's Day Devotional — An Announcement","Pitching the congregation-specific devotional that follows today's message","What if your church had a devotional that continued this conversation in the specific language of your congregation.","flagship"),
  ("54","For the Mother of a Prodigal","The woman who is not celebrating today because her child is not where she hoped","She has not given up. She has not stopped praying. She is here. That is everything.","lament"),
  ("55","What the Culture Gets Wrong About Mothers","The formation that the church uniquely can offer that Hallmark cannot","Hallmark sells sentiment. The church offers formation. Those are different products for different hungers.","cultural"),
  ("56","The Three Things Every Mother Gives","The formation gifts that are specific to the maternal relationship","Presence, attunement, and blessing. Three things. Most mothers give them without knowing they are formation.",""),
  ("57","She Was a Mother Before She Was Anything Else","The identity of the mother as primary formation — and what happens when it is lost","When the children leave, what remains. The mother who formed herself around her children has work to do.","pastoral"),
  ("58","The Mother in the Room Who Does Not Feel Seen","Every Mother's Day sermon should include this person specifically","She is there. She has been coming for fifteen years. She has never been mentioned from the pulpit.","pastoral"),
  ("59","The Mother's Day Sermon That Does Not Make Anyone Cry","The formation alternative to the emotional manipulation that most Mother's Day sermons rely on","If the only tool in the Mother's Day sermon is sentimentality, the pastor does not trust the text.","flagship"),
  ("60","Formation Before the Words Were There","What the pre-verbal child receives from the mother that shapes everything","The most important formation in a human life happens before language. Before the child can receive teaching, the mother is forming.",""),
  ("61","The Church That Mothers the Motherless","The congregation as formation community for the person without a mother","The church is supposed to be Mater Ecclesia — the mother who forms the people who have no one else.",""),
  ("62","What You Did Not Know Your Mother Was Doing","The unseen formation that only becomes visible decades later","You did not know what she was forming. You are living it now.","flagship"),
  ("63","To the Woman Who Wondered If She Mattered","The final Mother's Day sermon that names the invisible formation work","You mattered. You matter. The formation you gave is still forming the person you gave it to.","flagship"),
]

# ═══════════════════════════════════════════════════
# CATEGORY 4: END-OF-YEAR GIVING — 63 FRESH ANGLES
# ═══════════════════════════════════════════════════
GIVING = [
  ("★","What Giving Does to the Giver","The stewardship sermon that is entirely about the giver, not the church's need","The most powerful case for generosity is not the church's budget. It is the soul of the person who gives.","flagship"),
  ("2","The Anthropology of Generosity","What holding tightly to money does to a person — and what releasing it does","The hand that gives is open. The hand that holds is closed. You cannot receive with a closed hand.","flagship"),
  ("3","Why Rich People Are Often Miserable","The uncomfortable correlation between wealth accumulation and life satisfaction","The research is consistent. Above a certain income threshold, more money does not produce more happiness. Something else is required.","cultural"),
  ("4","The Deceitfulness of Wealth — Jesus' Most Neglected Warning","Mark 4:19 — the thorns that choke the word","Jesus said wealth is deceitful. Not dangerous. Deceitful. It makes promises it cannot keep.","flagship"),
  ("5","What You Are Becoming While You Are Accumulating","The formation cost of holding tightly to money","Every financial decision is also a formation decision. What you do with money is forming the person you are becoming.",""),
  ("6","The Rich Fool — Updated","The parable of the barns applied to the retirement account, the investment portfolio, the second property","He built bigger barns. That night his soul was required of him. The barns were full. He was not.","flagship"),
  ("7","God Owns It All — Including the Part You Think You Earned","The stewardship reframe that changes every financial conversation","You did not generate your income in isolation. The intelligence, the opportunity, the health, the economy — none of that is yours. You managed someone else's resources.",""),
  ("8","The Tithe Was Never the Point","Malachi 3 as a relationship text, not a transaction text","Bring the whole tithe — and see if I will not open the floodgates. It is an invitation to an experiment, not a demand for a payment.",""),
  ("9","What Jesus Said About Money — All of It","Thirty-seven parables. Eleven of them about money. Why.","Jesus talked about money more than any other subject except the kingdom of God. What was he seeing that we are not seeing.","flagship"),
  ("10","The Widow's Offering as the Giving Standard","Not a model for campaigns — a model for the heart","She gave everything she had. Jesus did not celebrate the amount. He celebrated the posture. She held nothing back.","flagship"),
  ("11","The Year-End Gift as Worship","The December giving decision as a spiritual act, not a financial transaction","What if the last gift of the year was the most intentional prayer you prayed.",""),
  ("12","What Your Giving Says About Your Theology","The budget as a theological statement","Where your treasure is, your heart will be also. Your bank statement is a theological document.","flagship"),
  ("13","The Cheerful Giver — What Cheerful Actually Means","2 Corinthians 9:7 — the Greek word hilaros","The word Paul uses is not 'willing.' It is hilaros — from which we get hilarious. The giver who gives from that place is laughing.",""),
  ("14","The Financial Audit as Spiritual Discipline","What it means to review your year-end giving statement as a formation practice","Before you sign the pledge card, review the year's giving. Does it tell the story you want to tell.",""),
  ("15","Contentment Is a Learned Skill","Philippians 4:11 — I have learned, in whatever state I am, to be content","Paul does not say he was given contentment. He says he learned it. There is a curriculum.",""),
  ("16","The Formation of the Generous Life — Seven Years In","What the person who has been tithing for seven years knows that they did not know when they started","The first year of tithing is faith. The seventh year is testimony. The seventeenth year is formation.","flagship"),
  ("17","First Fruits as the Ordering Discipline","The practice that tells your money who is in charge","When you give first, before anything else is paid, you are making a theological statement about who owns the income.",""),
  ("18","The Year God Outdid Your Generosity","The testimony sermon for the end-of-year giving campaign","We do not share testimonies to manipulate. We share them because the congregation needs to hear what God does when his people give.","testimony"),
  ("19","The Legacy Gift That Started With a Decision","The estate planning sermon that begins with a specific story","She was not wealthy. She gave ten percent of an ordinary income for forty years. Her estate gift built a school.","flagship"),
  ("20","Year-End Giving and the Formation of Your Children","What your children are learning by watching what you do with money in December","You are forming your children's relationship with money right now. Not by what you say about money. By what you do with it.",""),
  ("21","The Matching Gift as a Formation Opportunity","Not just a financial strategy — a theological invitation","Every matching gift is a picture of the gospel. Someone else committed first. Your giving joins theirs.",""),
  ("22","What the Early Church Did With Money","Acts 2:44–45 — and what it cost them and what it produced","They sold property and possessions and gave to anyone who had need. That is not socialism. It is the kingdom.",""),
  ("23","The Tax Deduction That God Does Not Need","The sermon that refuses to make a financial argument for a formation decision","God does not need your year-end tax deduction strategy. He needs your heart. The deduction is a bonus.",""),
  ("24","The Pledge Card as a Prayer","What happens when the commitment is treated as worship rather than administration","Write the amount. Sign your name. Pray over it. That changes what you signed.",""),
  ("25","The Congregation That Could Not Out-Give God","The annual testimony that keeps the campaign honest","This is not a sales pitch. This is a report on what we have seen. God has been giving back more than we gave.","flagship"),
  ("26","Generosity as the Antidote to Anxiety","The counterintuitive spiritual therapy for financial worry","The person who is most anxious about money usually holds it most tightly. Generosity is the formation that breaks that pattern.",""),
  ("27","The Tithe and the Lie About Affordability","The theological response to 'I cannot afford to tithe'","No one in the history of tithing started when they felt like they could afford it. They started before.",""),
  ("28","What the Capital Campaign Built That Is Not the Building","The formation the campaign produced in the congregation","The building is the visible product. The congregation that gave to build it is the formation product.","seasonal"),
  ("29","Giving in the Recession — The Formation Test","What the congregation does with generosity when the economy contracts","The congregation's giving behavior in a recession reveals more about its formation than its giving behavior in prosperity.",""),
  ("30","The Year-End Financial Review as a Formation Practice","The invitation to review the year's spending and giving before next year's decisions","Before you plan next year's budget, review this year's. What did you invest in. What did you consume. What did you give.",""),
  ("31","The Hundred-Year Gift","The legacy giving sermon that imagines what a hundred-year gift would do","You will not live to see its full fruit. Neither did the person who gave the gift that formed you.","flagship"),
  ("32","Loose Grip — The Physical Discipline of Generosity","The embodied practice of releasing what you hold","The generous life is practiced before it is felt. Act generously before you feel generous.",""),
  ("33","The Pledge and the Practice","The difference between the year-end commitment and the formation that follows it","The pledge is the beginning. The practice is the formation. Most churches celebrate the pledge and forget the practice.",""),
  ("34","What Amazon Is Doing to Your Soul","The formation cost of one-click consumption","Every purchase you did not plan is a vote for who is in charge of your money. Generosity is the counter-formation.","cultural"),
  ("35","The Sermon the Budget Committee Wanted — And the Sermon You Need","The stewardship message that resists pressure and preaches formation","The budget committee wants a sermon about the gap. The congregation needs a sermon about the giver.","flagship"),
  ("36","The Stewardship of Time — The Other Giving Campaign","The end of year review that includes more than money","You gave a certain percentage of your money this year. What percentage of your time went to the kingdom.",""),
  ("37","The Formation of the Generous Marriage","What happens to a marriage when both partners release their grip on money","Money is the most common source of marital conflict. Generosity is one of its most reliable antidotes.",""),
  ("38","The Inheritance Conversation — Before You Have To Have It","The end-of-year invitation to do estate planning as a family","The conversation about what you leave behind is not about death. It is about what you value.","flagship"),
  ("39","The Second Gift — What Happens After the Tax Deduction","The giving that is not strategic — the gift that is purely an act of worship","The deductible gift is formation. The non-deductible gift is worship.",""),
  ("40","What Bethlehem Cost God","The stewardship sermon that begins with incarnation","God gave the most valuable thing in existence in exchange for the love of people who would mostly reject him. That is the generosity we are called to reflect.","flagship"),
  ("41","The Formation of the Generous Teenager","The year-end giving conversation for the families in the congregation","The teenager who gives ten percent of their babysitting income is the adult who gives ten percent of their executive salary.",""),
  ("42","Year-End Giving and the Five Purposes","How generosity connects to every purpose of the church","Generosity forms worshippers, builds community, disciplizes the giver, mobilizes service, and funds evangelism. It is not a department. It is the whole thing.",""),
  ("43","The Church That Gave More Than It Planned","The testimony of the congregation that exceeded its campaign goal","We set a goal. You exceeded it. That does not happen because of good fundraising. It happens because of formation.","testimony"),
  ("44","What the Endowment Is For","The long-arc stewardship sermon about generational giving","The endowment is not for the congregation that gives it. It is for the congregation that does not yet exist.","flagship"),
  ("45","The Debt That Was Paid Off — And What Comes After","The stewardship sermon for the mortgage-burning congregation","You built it. You paid it off. Now what. The question of what the freed money does is a formation question.","seasonal"),
  ("46","The Christmas Fund and the Kingdom Fund","The year-end invitation to make December giving missional as well as operational","You gave to the building, the programs, the staff. What did you give to the kingdom work that goes beyond your zip code.",""),
  ("47","Generosity and the Great Reversal","The eschatological giving sermon — the first will be last","The people who gave most quietly are often the people who built the most. The kingdom accounting is different.","flagship"),
  ("48","The Percentage That Changed a Family's History","The specific family whose giving percentage changed everything","Every congregation has a family whose giving story is worth telling. Tell it with permission.","testimony"),
  ("49","What End-of-Year Giving Is Actually For","The formation sermon that refuses to treat year-end giving as a tax strategy","You are not giving to reduce your taxes. You are giving to form your soul. The tax reduction is a bonus.","flagship"),
  ("50","The Giving That Nobody Saw","The secret generosity that is the most powerful formation practice","The gift that is known produces a certain kind of formation. The gift that is unknown produces a deeper kind.",""),
  ("51","The Congregation That Takes Stewardship Season Seriously","What a formation-oriented stewardship season looks like","The church that runs a campaign is running a campaign. The church that runs a formation season is forming people.","flagship"),
  ("52","The Year in Review — What Your Money Did","The end-of-year accounting as a spiritual discipline","Where did your money go this year. Not as a guilt exercise. As a formation inventory.",""),
  ("53","The December 31 Decision","The year-end giving decision as the last formation act of the year","Before midnight, one more decision. Where does this go. To whom is this given. What does this year end with.","flagship"),
  ("54","The 21-Day Generosity Challenge — Beginning January 1","The year-end giving campaign that launches a January formation arc","The pledge card is not the end of the campaign. It is the beginning of the formation.","flagship"),
  ("55","The Custom Year-End Devotional","The pitch for the congregation-specific giving devotional","What if your congregation had its own devotional for the weeks of stewardship season — in your voice, about your context, with your stories.","flagship"),
  ("56","The Formation of the Generous Retiree","The year-end giving sermon for the congregation's most financially flexible members","The retiree with financial capacity and a formed generous identity is the most powerful giving force in any congregation.",""),
  ("57","What Happened When the Church Gave It All Away","The radical generosity testimony that changes the formation culture","Some congregations have given what they could not afford and discovered they were more than adequate.","testimony"),
  ("58","The First Fruits of the New Year","The January 1 giving practice that changes the year","If the first financial act of the new year is a gift, the year is ordered differently from the beginning.",""),
  ("59","The Generous Church in a Recession","The formation test of stewardship season in a difficult economic year","The congregation that gives generously when it is hard has discovered something the comfortable congregation has not.",""),
  ("60","Year-End Giving and the Five-Year Formation Arc","What happens to a congregation whose giving formation is tracked over five years","In year one, the congregation gives to meet a need. In year five, the congregation gives from identity.","flagship"),
  ("61","The Tax-Year Giving Deadline as a Spiritual Invitation","The one day in the year when financial urgency and formation opportunity converge","December 31 is a deadline. It is also an invitation. The question is which frame you bring to it.",""),
  ("62","What the Next Ten Years of Your Generosity Will Build","The long-arc giving sermon that invites a decade-level commitment","Do not think about what you are giving this year. Think about what you are building over the next ten years.","flagship"),
  ("63","The Last Sermon of the Year Should Be About the First Act of Next Year","Closing the giving season by opening the formation season","The best stewardship sermon of the year is not the campaign closer. It is the January formation launcher.","flagship"),
]

# ═══════════════════════════════════════════════════
# STRATEGIC NEXT STEP SYSTEMS
# ═══════════════════════════════════════════════════
SYSTEMS = {
  "Easter": {
    "color":"#4a2a08","acc":"#c9a84c","bg":"#030b04",
    "icon":"✝",
    "crack":"Easter is the most preached Sunday in the church year — and the one most likely to produce no formation change in the congregation because the sermon ends without a next step. The congregation that hears the best resurrection sermon of the year and leaves with nothing specific to do next has been inspired. Inspiration is not formation.",
    "steps":[
      ("Immediate · During the Service","The Response Card","Every Easter sermon should end with a response card that has exactly one question: What do you do with this? The person who writes an answer is three times more likely to act on it than the person who only hears it.","#c9a84c"),
      ("Day 1 · Monday","The 7-Day Resurrection Journey","The seven days after Easter are the most underused formation window in the church year. Launch the 7-Day Resurrection Journey on Sunday evening with a text message to the congregation. Day 1 begins Monday. The journey follows one resurrection appearance per day.","#c9a84c"),
      ("Week 1 · Thursday","Small Group Launch","Easter Sunday is the highest small group signup opportunity of the year. The communication card should include a small group signup. The first small group meeting the Thursday after Easter reviews the first three days of the 7-Day Journey.","#4a7fa8"),
      ("Weeks 2–4","The 21-Day Resurrection Challenge","Three weeks. One resurrection appearance per day. The congregation arrives at the Ascension having walked through every post-Easter appearance in order. This is the formation arc that most Easter sermons leave on the table.","#4a7fa8"),
      ("Month 2","The Post-Easter Series","Easter Sunday launches a 6-week series on resurrection living. The campaign does not end with the sermon — it begins with it. The 7-Day Challenge is the on-ramp to the 6-week small group series.","#5a8070"),
      ("End of Season","Testimony Sunday","Three to four weeks after Easter, three congregation members share what happened in them during the 7-Day Journey or the post-Easter series. The most powerful formation produced by Easter is the story the congregation member tells about what Easter did to them.","#5a8070"),
    ],
    "pitches":[
      ("seven","7-Day","The 7-Day Resurrection Journey","Mon–Sat resurrection appearances + Celebration Sunday recap. One appearance per day. Six days of formation closing with a Celebration Sunday where the congregation shares what happened.","Download the free guide at lifetogether.com/easter-7day","flagship"),
      ("twentyone","21-Day","The 21-Day Resurrection Challenge","Three weeks following every post-resurrection appearance in order. The congregation arrives at Pentecost having walked every moment between Easter and the Ascension.","Full study guide available at lifetogether.com/resurrection-21","flagship"),
      ("custom","Custom Devotional","Your Church's Easter Devotional","A custom devotional written in your pastoral voice, referencing your congregation's specific context, for distribution from the Easter Sunday bulletin. 7 days. Print-ready. Available at lifetogether.com/custom","Learn more at lifetogether.com/custom-easter","flagship"),
    ]
  },
  "Christmas": {
    "color":"#08103a","acc":"#c9a84c","bg":"#030508",
    "icon":"✦",
    "crack":"Christmas Eve is the only Sunday of the year when the congregation is at maximum size and minimum expectation of being changed. The unchurched attender comes for the experience, not the formation. The pastor's challenge: produce the experience while offering the formation step that goes home with them.",
    "steps":[
      ("Immediate · At the Door","The Take-Home Card","Every person leaving the Christmas Eve service should receive one card. On one side: the key verse. On the other: one formation question to discuss at the table on Christmas Day. This is the only next step the unchurched attender will take.","#c9a84c"),
      ("Christmas Day","The Family Table Conversation","The sermon that includes a specific conversation question for the Christmas Day dinner table is the sermon that forms the family that came back. 'What is one thing from tonight that you want to carry into next year?' That question, asked at the table, produces formation.","#c9a84c"),
      ("December 26–31","The Advent Reflection Week","The seven days between Christmas and New Year are the best formation window of the year for the congregation that is not in programming. The 7-Day Christmas-to-New-Year Journey takes the congregation from incarnation to new year formation in one continuous arc.","#4a7fa8"),
      ("January 1","The New Year Formation Launch","Every Christmas Eve sermon should name what January 1 will launch. The congregation that leaves Christmas Eve knowing that the formation arc continues in January is the congregation that comes back.","#4a7fa8"),
      ("January Series","The Advent-to-January Bridge Series","The 4-week Advent series that flows seamlessly into a 4-week January series on incarnation living. The December formation arc and the January formation arc are one continuous arc.","#5a8070"),
      ("Annual Rhythm","The Christmas Devotional Tradition","The congregation that receives the same devotional format every Advent season develops a formation tradition. The custom Advent devotional becomes the thing the congregation looks forward to as much as any program.","#5a8070"),
    ],
    "pitches":[
      ("seven","7-Day","Christmas to New Year — The 7-Day Bridge","December 25 to December 31. One reflection per day on the incarnation. The congregation arrives at New Year's Eve having sat with Christmas for seven days.","Available at lifetogether.com/christmas-7day","flagship"),
      ("twentyone","21-Day","The 21-Day Advent Journey","Beginning December 1. Three weeks of Advent formation closing with Christmas Day. Hope, Peace, Joy, Love — the Advent arc in daily formation bites.","Full Advent guide at lifetogether.com/advent-21","flagship"),
      ("custom","Custom Devotional","Your Church's Custom Advent Devotional","An Advent devotional written in your pastoral voice, referencing your congregation's specific tradition and language. Available in print-ready and digital formats for every family in the congregation.","Learn more at lifetogether.com/custom-advent","flagship"),
    ]
  },
  "Mothers": {
    "color":"#3a0808","acc":"#c9a84c","bg":"#06030a",
    "icon":"♡",
    "crack":"Mother's Day generates the most pastoral complexity of any Sunday on the calendar. Twenty percent of the room is grieving. Another twenty percent has a complicated relationship. Another twenty percent is struggling as a mother. The formation step on Mother's Day has to be tender enough for all of them.",
    "steps":[
      ("Immediate · During the Service","The Write-a-Mother Card","At the end of the Mother's Day service, every person writes one sentence to a mother in their life — present or absent, living or deceased — and reads it aloud to the person next to them or keeps it as a private prayer. This is the most powerful Mother's Day formation moment available and it costs nothing.","#c9a84c"),
      ("Day 1 · Monday","The 7-Day Mother's Blessing Journey","Seven days of formation around the specific things a mother forms in a child. Not sentimental. Theological. Each day names one formation gift and invites the participant to receive it, express gratitude for it, or grieve its absence.","#c9a84c"),
      ("Week 1","The Grief Group for Those for Whom Today Was Hard","Every Mother's Day should be followed by a pastoral care pathway for the people for whom it surfaced grief. A mid-week gathering, a small group, or a pastoral conversation offered to the 20% of the congregation for whom the day was painful.","#4a7fa8"),
      ("Month 2","The Mothering Series","The 6-week formation series on what mothers form and how the congregation embodies maternal formation for those who do not have it. The congregation that follows Mother's Day with a formation series has done more than the congregation that follows it with nothing.","#4a7fa8"),
      ("Season","The Custom Mother's Day Devotional","A custom 7-day devotional written for your congregation — in your pastoral voice, referencing the specific formation challenges of mothering in your context. Given to every mother in the congregation at the end of the service.","#5a8070"),
      ("Ongoing","The Mater Ecclesia Initiative","The congregation formally commits to being the mother to the motherless. The maternal formation work of the congregation becomes a named ministry with a specific formation arc.","#5a8070"),
    ],
    "pitches":[
      ("seven","7-Day","The 7-Day Mother's Formation Journey","Seven days of formation around the specific gifts mothers give — presence, attunement, blessing, resilience, release, prayer, and legacy. Works for every person regardless of their relationship with their mother.","Available at lifetogether.com/mothers-7day","flagship"),
      ("twentyone","21-Day","The 21-Day Family Formation Challenge","Three weeks of formation on what families form and how to receive or pass on what was received. For mothers, children, and everyone navigating the complicated territory of family.","Full guide at lifetogether.com/family-21","flagship"),
      ("custom","Custom Devotional","Your Church's Custom Mother's Day Devotional","A 7-day devotional written in your pastoral voice for every person in your congregation — tender enough for grief, honest enough for complication, celebratory enough for joy.","Learn more at lifetogether.com/custom-mothers","flagship"),
    ]
  },
  "Giving": {
    "color":"#0a1a08","acc":"#c9a84c","bg":"#040808",
    "icon":"◇",
    "crack":"The stewardship sermon is the most feared Sunday on the pastoral calendar. The congregation expects to be asked for money. The pastor who meets that expectation has confirmed the suspicion that the church is primarily a financial institution. The pastor who surprises the congregation with formation — with what generosity does to the giver's soul — has the room's attention.",
    "steps":[
      ("Immediate · The Pledge Card","The Formation Pledge","The pledge card should ask one formation question alongside the financial commitment: What do you believe about generosity that this commitment expresses? The person who answers that question is not writing a check. They are declaring a theology.","#c9a84c"),
      ("Week 1","The 7-Day Generosity Practice","Seven days of one specific generosity action per day — not all financial. Day 1: give a compliment you have been withholding. Day 4: give money to someone outside the church budget. Day 7: give time. The formation of the generous life is not only about the pledge card.","#c9a84c"),
      ("Month 2","The 21-Day Generosity Challenge","January generosity formation arc. Three weeks of daily generosity practice. The congregation that does the 21-Day Generosity Challenge in January is the congregation whose year-end giving next December reflects formation, not obligation.","#4a7fa8"),
      ("Ongoing","The Generosity Tracker","The annual review of giving patterns alongside formation patterns. The congregation member who tracks both their giving percentage and their formation growth over five years is the congregation member who becomes a generous person, not just a generous giver.","#4a7fa8"),
      ("Annual","The Legacy Giving Initiative","The year-end giving campaign that includes a legacy giving conversation. Every year-end stewardship season should include one message on estate planning as formation. The congregation that thinks about its estate annually is the congregation that gives strategically.","#5a8070"),
      ("Custom","The Stewardship Season Devotional","A custom devotional for the weeks of stewardship season — in your pastoral voice, referencing your congregation's specific formation challenges around money. Distributed at the start of stewardship season rather than during the campaign.","#5a8070"),
    ],
    "pitches":[
      ("seven","7-Day","The 7-Day Generosity Practice","Seven days. One generosity action per day — some financial, some relational, some time-based. The congregation that does this discovers that generosity is a posture, not a transaction.","Available at lifetogether.com/giving-7day","flagship"),
      ("twentyone","21-Day","The 21-Day Generosity Challenge","Three weeks of formation on the generous life — the theology, the practice, and the transformation. The person who completes this challenge is the person who changes their year-end giving amount next year.","Full guide at lifetogether.com/generosity-21","flagship"),
      ("custom","Custom Devotional","Your Church's Custom Stewardship Devotional","A 5-week devotional written in your pastoral voice for your congregation's stewardship season — before the campaign begins, so the formation precedes the ask.","Learn more at lifetogether.com/custom-stewardship","flagship"),
    ]
  },
}

# ─── BUILD HTML ────────────────────────────────────────

def angle_card(num, title, sub, hook, cls=""):
    cls_str = f"angle-card {cls}".strip() if cls else "angle-card"
    return f'''<div class="{cls_str}">
  <div class="ac-top"><span class="ac-num">{e(str(num))}</span><span class="ac-title">{e(title)}</span></div>
  <p class="ac-sub">{e(sub)}</p>
  <div class="ac-hook" style="border-color:rgba(201,168,76,.3);">{e(hook)}</div>
</div>'''

def build_system(key, label, titles, col, crack_text):
    sys = SYSTEMS[key]
    # angles
    cards = "\n".join(angle_card(t[0],t[1],t[2],t[3],t[4] if len(t)>4 else "") for t in titles)
    # crack box
    crack = f'<div class="crack-box" id="crack-{key.lower()}"><span>The Crack — The Fresh Angle</span><p>{e(crack_text)}</p></div>'
    # steps
    steps_html = "\n".join(f'''<div class="nsp-step" style="border-color:{s[3]};">
  <span class="nsp-step-label" style="color:{s[3]};">{e(s[0])}</span>
  <span class="nsp-step-title">{e(s[1])}</span>
  <p class="nsp-step-text">{e(s[2])}</p>
</div>''' for s in sys["steps"])
    # pitches
    pitch_map = {"seven":("pitch-card seven","7-Day Journey →"),"twentyone":("pitch-card twentyone","21-Day Challenge →"),"custom":("pitch-card custom","Custom Devotional →")}
    pitches_html = "\n".join(f'''<div class="{pitch_map[p[0]][0]}">
  <p class="pc-eyebrow">{e(p[1])}</p>
  <p class="pc-title">{e(p[2])}</p>
  <p class="pc-desc">{e(p[3])}</p>
  <p class="pc-cta">{e(p[4])}</p>
</div>''' for p in sys["pitches"])
    panel = f'''<div class="nextstep-panel" id="next-{key.lower()}" style="border-color:rgba(201,168,76,.25);">
  <div class="nsp-header" style="background:{sys['bg']};">
    <span class="nsp-icon">{sys['icon']}</span>
    <div><p class="nsp-title">Strategic Next Steps — {label}</p>
    <p class="nsp-sub">The formation system that extends the sermon beyond Sunday</p></div>
  </div>
  <div class="nsp-body">
    <div class="nsp-steps">{steps_html}</div>
    <p style="font-family:Georgia,serif;font-size:11px;color:#888;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">Launch These Three Formation Products</p>
    <div class="pitch-row">{pitches_html}</div>
  </div>
</div>'''
    return f'''<section class="cat-section" id="{key.lower()}" style="border-color:{col};">
  <div class="cat-intro" style="background:rgba(0,0,0,.01);">
    <p class="cat-kk" style="color:{col};">{e(label)}</p>
    <h2 class="cat-h2" style="">{e(label.split("—")[0].strip())} <em>Fresh Angles</em></h2>
    <div class="cat-sub"><p>{e(SYSTEMS[key]["crack"])}</p></div>
  </div>
  {crack}
  <div class="angles">{cards}</div>
  {panel}
  <div class="hdiv"></div>
</section>'''

# ── THE 5 HARDEST PROBLEM STATEMENT ──
top5_html = "\n".join(f'''<div class="top5-item {t[0]}">
  <span class="top5-n">{e(t[1])}</span>
  <h3 class="top5-title">{e(t[2])}</h3>
  <p class="top5-why">{e(t[3])}</p>
  <span class="top5-crack">{e(t[4])}</span>
</div>''' for t in TOP5)

total = len(EASTER) + len(CHRISTMAS) + len(MOTHERS) + len(GIVING)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Fresh Sermon Angles — The 5 Hardest Sundays · Lifetogether</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="page">

<section class="cover">
  <div class="cover-glow"></div>
  <div class="cover-top">
    <span class="cover-logo">Lifetogether</span>
    <span class="cover-tag">Sermon Intelligence · Fresh Angles · 2026</span>
  </div>
  <div class="cover-body">
    <p class="cover-ey">The Five Hardest Sundays to Preach Fresh — And {total} New Angles For Them</p>
    <h1 class="cover-h1">The <em>Fresh</em><br>Sermon<br><span class="dim">System.</span></h1>
    <div class="cover-rule"><div class="cover-rule-dot"></div><div class="cover-rule-line"></div></div>
    <p class="cover-sub">{total} fresh sermon titles and angles for the five most preached — and most exhausted — Sundays on the pastoral calendar, plus the strategic formation system that connects each sermon to a 7-day journey, a 21-day challenge, and a custom devotional for your congregation.</p>
    <div class="cover-stats">
      <div class="cstat"><span class="cstat-n">5</span><span class="cstat-l">Hardest Sundays</span></div>
      <div class="cstat"><span class="cstat-n">{total}</span><span class="cstat-l">Fresh Angles</span></div>
      <div class="cstat"><span class="cstat-n">4</span><span class="cstat-l">Formation Systems</span></div>
      <div class="cstat"><span class="cstat-n">12</span><span class="cstat-l">Product Pitches</span></div>
      <div class="cstat"><span class="cstat-n">∞</span><span class="cstat-l">Formation Arcs</span></div>
    </div>
  </div>
</section>

<section class="prob">
  <p class="prob-kk">The Problem · Why These Five</p>
  <h2 class="prob-h2">The <em>Five Hardest</em> Sundays<br>to Find a Fresh Sermon Idea</h2>
  <p class="prob-sub">Every pastor has a list of Sundays that produce dread rather than anticipation. Not because the theology is unclear. Because the angle has been exhausted. Because the congregation has heard every version of the sermon that comes to mind first. Because the cultural frame is so strong that the biblical frame has to fight to be heard. These five are the ones almost every pastor names.</p>
  <div class="top5-grid">{top5_html}</div>
</section>
<div class="hdiv"></div>

{build_system("Easter","Easter & Holy Week — 62 Fresh Angles",EASTER,"#c9a84c","The congregation knows the resurrection happened before the sermon begins. The pastoral challenge is not to convince them — it is to surprise them with what they already know.")}

{build_system("Christmas","Christmas Eve & Advent — 62 Fresh Angles",CHRISTMAS,"#5070a0","The most unchurched room of the year and the most familiar story of the year. The congregation that knows the story arrives expecting to be moved. The pastor who meets that expectation has produced sentiment. The pastor who surprises it has produced formation.")}

{build_system("Mothers","Mother's Day — 63 Fresh Angles",MOTHERS,"#806060","The most emotionally loaded Sunday for the largest percentage of the congregation. The pastor who ignores the complexity confirms that the church is not a safe place to bring the complicated story. The pastor who names it is the pastor people come back to.")}

{build_system("Giving","End-of-Year Giving — 63 Fresh Angles",GIVING,"#508060","The congregation suspects the sermon is about money before the pastor stands up. The pastor who meets that suspicion has lost. The pastor who surprises the congregation with the formation cost of not giving has the room's full attention.")}

<section class="back">
  <p class="bq">"The freshness in a sermon never comes from a better illustration or a more creative title. It comes from a different angle on the text — one that the congregation has not heard, that the pastor has not preached, that the occasion has never before offered. These 250 angles exist to give every pastor a starting point that is not the one they would have reached for without help."</p>
  <p class="ba">Brett Eastman · Founder, Lifetogether</p>
  <p class="bc">
    <a href="mailto:brett@lifetogether.com">brett@lifetogether.com</a> &nbsp;·&nbsp;
    <a href="https://lifetogether.com">lifetogether.com</a> &nbsp;·&nbsp;
    25 Years · 500+ Church Relationships · 50M+ Campaigns
  </p>
  <div class="lm">Lifetogether</div>
</section>

</div>
</body>
</html>"""

with open('/mnt/user-data/outputs/lifetogether-fresh-sermon-angles.html','w') as f:
    f.write(HTML)
print(f"Done — {len(HTML):,} chars · {total} titles")
