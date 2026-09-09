#!/usr/bin/env python3
"""
Builds the Leader Edition as a derivative of the Participant Guide.

The participant text is never retyped here. It is read from curr.md and leader
notes are injected at named anchors. Change curr.md and rerun this script and
the Leader Edition rebuilds to match, so the two can never drift.

Usage:  python3 build_leader.py
Output: leader_edition.md
"""
import re

PARTICIPANT = 'curr.md'
OUT = 'leader_edition.md'

# ---------------------------------------------------------------- front matter

FRONT = r"""## **GOD OWNS IT ALL**

### **Student Edition** · Leader Edition

#### **A Six-Session Journey on Ownership, Contentment, Stewardship, Confidence, Generosity, and Legacy**

*Ron Blue with Brett Eastman*

> **This book contains everything in the student guide, in the same order, plus leader notes.** Your students' pages and your pages match line for line, so you can run the session from this book alone. Leader notes are set apart and are for you, not to be read aloud.

## **Before You Lead Anything**

You don't have to be good with money to lead this.

That isn't a nice thing to say so you'll feel better. It's the actual best-case setup. A leader who admits they're still figuring money out builds more trust with students than one who has it handled, because this whole series is about honesty rather than competence. If a student asks you something financial you can't answer, "I don't know, I'm still working that out myself" is a better answer than a guess.

What you do need to do is read the session before you walk in. Not skim it. Read it, do the exercise yourself, and notice where it gets uncomfortable for you, because that is exactly where it will get uncomfortable for them.

Six things that will make you better at this than any amount of preparation.

**Let silence work.** After you ask a question, count to ten in your head. Ten is much longer than it feels. Students are used to adults rescuing silence, so they have learned to wait it out. Stop rescuing and they start talking. The best follow-up you have is "tell me more about that."

**Answer first when it's hard, not when it's easy.** On the light questions, let students go first. On the real ones, model it. Go first, be honest, keep it short. Your honesty sets the ceiling for the room, and they will never go deeper than you do.

**Don't fix anybody.** When a student says something real, the instinct is to solve it, or find a verse, or tie a bow. Resist all three. Receive it. "That's a lot to carry" is enough. This series touches fear, family money stress, and shame, and a student who gets fixed once will not say the real thing again.

**Never ask for numbers, and don't let the group ask either.** The no-numbers promise is signed in the front of every student's guide, and holding it is on you. If a student volunteers a number, don't repeat it or build on it. Move on gently.

**Watch for the student carrying it at home.** In most groups there is at least one student whose family is genuinely stressed about money right now. They will not tell you. They may go quiet in sessions two and four especially. Follow up privately, don't put them on the spot, and don't build a group moment around them.

**Rotate and share the load.** Healthy groups rotate hosting and leading. Nobody should carry six weeks alone, and rotating develops the students who will lead next.

## **What to Do When It Gets Heavy**

It will, probably in session four.

When a student shares something hard, the group's job is to receive it, not solve it. Don't rush to advice or a verse that closes it down. Sit with it. "Thanks for saying that out loud" is a complete response.

If a student discloses something beyond what a small group can hold, family crisis, real fear about safety, anything about harming themselves, that is not a group moment. Follow up privately, that day, and get your youth pastor involved. You are not the last line of help and you should not try to be.

If the group itself feels off in session two, relax. Groups usually don't gel until three or four. Finish the six weeks before deciding anything.

## **Answer Keys, All Six Sessions**

*Each key also appears beside its own session. Don't read these aloud during the video.*

**Session One** · life · image · created / His · good / very · holding · borrowed / yours

**Session Two** · have · finish line · what is it · day · rotten · store · normal · industries / business model · hitting / trusting

**Session Three** · not looking · holding · could handle · afraid · identical / Faithfulness · fear · fear · safe move / failure

**Session Four** · out there / in here · 2:00 a.m. · real · care · Quiet / still · I am with you · weather / boat · outcome / Person · agreement

**Session Five** · you / you · have · reservoir · stagnant / rot · sack lunch · All of it · holding / released · poorer · amount / heart

**Session Six** · faithful / trend · small stuff · famous / you · are · bowl · identity · wasted · you / up · window / view

"""

BACK = r"""
## **Leading After Session Six**

The six weeks were the easy part. There was a rhythm, a video, a page, and a room. All of that stops now, and what is left is whatever actually got built.

Three things worth doing in the two weeks after.

**Follow up individually, once.** One message to each student, naming the one thing you noticed in them. Not a group text. This is the highest-return thing you will do in the whole series and it takes about twenty minutes.

**Ask what they kept.** Not what they learned. What they kept. If the answer is nothing, that's useful information and it isn't a failure, since most people keep nothing from most things.

**Do something together that isn't a study.** A meal, a service thing, anything. Groups that meet once more without curriculum usually stay groups.

And keep the student who went quiet in session four on your radar. That one matters more than the rest of this page.
"""

# ------------------------------------------------------------------ the notes
# Injected BEFORE the section header named in the key.
# 'SETUP' goes immediately after the session title block.

NOTES = {
1: {
 'SETUP': ("This session sets the tone for all six. Budget more time for Come Together than you think you need, "
   "because the group agreement is the foundation for everything after it. Read it aloud rather than summarizing, "
   "then have students sign it. It feels formal. Do it anyway. Signing something makes it real in a way that "
   "agreeing to it doesn't.\n\nBring pens. Every week. Students will not have them.\n\n"
   "**The one thing to get right this week:** the no-numbers promise. Say it plainly and say it early. Half the "
   "room walked in braced for a money study that is going to expose them.\n\n"
   "**Answer key** · life · image · created / His · good / very · holding · borrowed / yours"),
 'Come together': ("Pray first, then read the no-numbers paragraph word for word rather than paraphrasing. Then the "
   "agreement, then signatures. The opening question about being protective is meant to be light. Let it be light. "
   "Don't push anybody deeper here."),
 'Watch the video': ("Hand out the pens now. Don't read answers aloud, and don't stop the video to catch anybody up.\n\n"
   "**Pause and reflect is sixty seconds, timed and silent.** Say \"we're going to sit here for a minute, that's on "
   "purpose\" so nobody thinks something went wrong."),
 "Let's talk about it": ("The board question is your easiest entry. Most students can name something they're carrying "
   "that belongs to somebody else. If the room is slow, go first with a small real one of your own.\n\n"
   "**The third question is the honest one.** Somebody on the show said that if they stopped holding it all together, "
   "they don't know what would be left of them. If a student agrees with that out loud, don't move on quickly. Sit in "
   "it. That sentence is the emotional center of the episode.\n\n"
   "**If you're short on time, keep the fourth question.**"),
 'Open hands': ("Say clearly that nobody reads this out loud. Then be quiet and let them write for four to five "
   "minutes. Watch for the student who fills it in fast and shallow, and don't call it out."),
 'Before you go': ("Read the prayer or pray your own. Then point them to the devotional, days one through seven, and "
   "tell them you'll ask next week who read any of it. Then actually ask.\n\n"
   "**Your prayer, if you want one:** God, thank you for these students and for six weeks together. Nobody here has "
   "this figured out, including me. Quiet the part of us that wants to look fine. Show us where we have been carrying "
   "weight you never asked us to carry. Amen."),
},
2: {
 'SETUP': ("This is the session where the quiet student gets quiet. Wanting things is embarrassing to admit out loud "
   "at this age, and half your room is carrying a comparison problem they have never named. Your job is to make "
   "wanting things normal instead of shameful. Go first on the opening question and pick something a little "
   "embarrassing.\n\n**The one thing to get right this week:** nobody compares anything. If two students start "
   "measuring what they have against each other, stop it kindly and immediately. This is the session where that does "
   "the most damage.\n\n**Answer key** · have · finish line · what is it · day · rotten · store · normal · "
   "industries / business model · hitting / trusting"),
 'Come together': ("The opening question asks how long the buzz lasted on something they saved for. Most students will "
   "underestimate it and then correct themselves. Let them correct themselves. Don't do it for them."),
 'Watch the video': ("Watch for the moment near the end of the game when sleep comes out last and Caroline has already "
   "committed her top spots. Students laugh, then go quiet. If your group reacts to that, it's your best entry into "
   "discussion, better than any question on the page.\n\n**Sixty seconds of silence after.** Some students will name "
   "something small and real, like sleep. Take that as seriously as the big answers."),
 "Let's talk about it": ("Asking what their feed tells them they are missing works better than asking about money "
   "directly, and it gets to the same place. Most students have never said this out loud.\n\n"
   "**The fourth question is the peak.** It asks whether any amount would actually let them exhale. Let the silence "
   "sit. If the honest answer in the room is no, that is exactly right, and it is the whole point of the session."),
 'Draw your finish line': ("Say plainly there are no amounts anywhere on this page. Students who hear \"finish line\" "
   "think you want a salary number. The last prompt, what they would do with what's left over, is the one that "
   "matters. Give them time for it."),
 'Before you go': ("Days eight through fourteen. Day fourteen is the hardest and best one in the week. Mention it.\n\n"
   "**Your prayer, if you want one:** God, we are all chasing something and most of us could not name it if you asked. "
   "Thank you that you sent enough every morning to people who could not store it, and that you have not changed. "
   "Amen."),
},
3: {
 'SETUP': ("This one is funnier than the others for about ten minutes and then it turns, and the turn catches people "
   "off guard. The game is a confession game, and Jerry's ratings on screen give your students permission to be honest "
   "about their own borrowed-stuff record.\n\nThe real content is not the hoodie. It's the buried thing. Watch for the "
   "student who goes still during the pause.\n\n**The one thing to get right this week:** do not let the buried-thing "
   "conversation become about talent or performance. It is about fear. When a student names something they have not "
   "done, ask what they were afraid of, not what is stopping them.\n\n**Answer key** · not looking · holding · "
   "could handle · afraid · identical / Faithfulness · fear · fear · safe move / failure"),
 'Come together': ("The opening question about something they are holding that belongs to somebody else is a laugh "
   "line. Use it. The lighter this opening is, the further the group will go later."),
 'Watch the video': ("The pause afterward asks \"what's your buried thing.\" Say out loud that they do not have to "
   "share it. Some will anyway, and that's the session working."),
 "Let's talk about it": ("Widening from a hoodie to time, talent, and trust is the hinge of the session. If the group "
   "stays on objects, name a bigger one yourself and let them follow.\n\n**The third question is the honest one.** "
   "Somebody on the show said burying it feels safer than failing at it. If a student says yes, ask what the smallest "
   "version of digging it up would be, and then stop talking."),
 'Live, Give, Owe, Grow': ("Percentages only, never amounts. The point of the exercise is the two questions after the "
   "four buckets, not the buckets themselves. Most students will discover Live got everything and Give has never "
   "existed. Let that land without commentary."),
 'Before you go': ("Days fifteen through twenty-one. Day twenty is the four questions before you borrow, which is the "
   "single most useful page in the book for the next ten years of their lives.\n\n**Your prayer, if you want one:** "
   "God, we are holding a lot of things we did not make and calling them ours. Help these students dig up the thing "
   "they have been sitting on. Amen."),
},
4: {
 'SETUP': ("This is the heavy one. Read \"What to Do When It Gets Heavy\" before you walk in, even if you read it in "
   "week one.\n\nThe game is funny, six fears sorted into three piles, and then two cards land that are not funny at "
   "all: being ordinary, and being found out. Both of those live at 2:00 a.m. in most of your students. Expect the "
   "room to change temperature.\n\n**The one thing to get right this week:** do not fix anybody. This session asks "
   "students to name their 2:00 a.m. fear, and the instinct to reassure is strong. Reassurance ends the conversation. "
   "Presence continues it.\n\nIf a student discloses something serious, follow up privately that same day and involve "
   "your youth pastor.\n\n**Answer key** · out there / in here · 2:00 a.m. · real · care · Quiet / still · "
   "I am with you · weather / boat · outcome / Person · agreement"),
 'Come together': ("Start with the silly fear. Genuinely start there. The order matters, and a room that has laughed "
   "together will go further than a room that hasn't."),
 'Watch the video': ("The pause afterward asks for their 2:00 a.m. question, \"not the presentable version.\" Say that "
   "phrase out loud. It gives students permission they will not take otherwise."),
 "Let's talk about it": ("Asking whether they have stopped believing God is paying attention is the most spiritually "
   "honest question in the series. Answer it first yourself if the room stalls, and answer it truthfully.\n\n"
   "**On the third question**, somebody on the show describes a prayer that felt like it hit the ceiling. Some student "
   "in your room has been there this month. The point to land is that the people literally in the boat with Jesus also "
   "thought He did not care, so that feeling is not evidence of failure.\n\n**The fourth question is where it lands.** "
   "Ask students to finish the \"even if\" out loud if they are willing. Do not force it, and do not correct anybody's "
   "answer."),
 'The five habits': ("This is a relief valve after a heavy conversation, and it is meant to be. Move to something "
   "concrete on purpose. The last prompt, the smallest possible version of their weakest habit, is the whole exercise."),
 'Before you go': ("Days twenty-two through twenty-eight. Day twenty-six is the one to mention, since it hands them "
   "something to do when they are panicking.\n\n**Your prayer, if you want one:** God, some of us in this room are "
   "genuinely afraid, and most of us have not said so. You never told us not to be afraid because things would go our "
   "way. You said it because you are here. Be here. Amen."),
},
5: {
 'SETUP': ("Students expect this week to be the ask. They are braced for a guilt trip about giving, and the session is "
   "not that. Say so at the top, out loud, in the first two minutes.\n\nThe game builds to a point most groups miss "
   "until it is named: the two hardest things to share are not things at all. Credit and feelings. Those are self.\n\n"
   "**The one thing to get right this week:** nobody says what they give. Not a number, not a percentage, not a story "
   "that implies one. Generosity stops being generosity the moment it becomes a scoreboard, and in a student group it "
   "becomes one fast.\n\n**Answer key** · you / you · have · reservoir · stagnant / rot · sack lunch · All of it · "
   "holding / released · poorer · amount / heart"),
 'Come together': ("Start with what is easy to share. Every student has an easy one, and starting there makes the hard "
   "one sayable twenty minutes later."),
 'Watch the video': ("The pause afterward asks what they are white-knuckling. Expect answers that are not money. That "
   "is the session working, not drifting."),
 "Let's talk about it": ("Somebody on the show says that if he gave the credit away too, he is scared there would be "
   "nothing left that proves he mattered. That is the realest line in the episode. If a student agrees, stay there.\n\n"
   "**The fourth question asks for the actual cost**, \"not the noble version.\" That is deliberate. Students will "
   "reach for the impressive answer. Push once, gently, for the true one."),
 'The quiet gift': ("This exercise only works if nobody finds out, which means you do not ask about it next week in "
   "front of the group. Say that when you assign it. The last prompt asks whether they are less interested in doing it "
   "if nobody will know. Do not soften that question."),
 'Before you go': ("Days twenty-nine through thirty-five. Day thirty-four is for the student who thinks they have "
   "nothing to give.\n\n**Your prayer, if you want one:** God, we have been holding on tightly and calling it being "
   "careful, and it has been making us empty. Help these students open their hands around something small this week. "
   "Amen."),
},
6: {
 'SETUP': ("Last one. Leave room, because last sessions are where people finally say the thing.\n\nTwo things are "
   "different this week. The exercise gets shared, which breaks the pattern of the other five, so tell students that "
   "before they start writing rather than after. And there is a closing beat after the prayer about what happens next "
   "Tuesday, when the videos stop.\n\n**The one thing to get right this week:** get every student to name one thing "
   "they are keeping and one person who is allowed to ask them about it. That single move is what makes six weeks "
   "stick instead of fade.\n\n**Answer key** · faithful / trend · small stuff · famous / you · are · bowl · identity · "
   "wasted · you / up · window / view"),
 'Come together': ("The yearbook quote question, \"not the one you'd actually submit, the real one,\" is a good laugh "
   "and a quiet setup for everything after it."),
 'Watch the video': ("The pause afterward asks about ten years of the week they just had. Some students will find this "
   "genuinely unsettling. Do not rescue it."),
 "Let's talk about it": ("Naming an un-famous person who changed them is the warmest moment in the whole series. Give "
   "it room, and go first.\n\n**On the third question**, somebody on the show says they have been seen by a lot of "
   "people and known by almost none. Some student in your room lives there. Do not rush past it."),
 'Your legacy letter': ("Three lines, not a book. Say clearly that they will be asked to read these to one real person "
   "this week, and that person can be someone in this room. Line two, why it holds when things get hard, takes the "
   "longest. Give it real time.\n\nIf your group is willing, have students read line three aloud to each other. That is "
   "the closing moment of the series if you want one."),
 'Before you go': ("Days thirty-six through forty-two. Day forty-two asks what they hope God does with their life. Tell "
   "them to date it and come back in a year.\n\n**Your prayer, if you want one:** God, six weeks ago this started with "
   "a sentence about everything belonging to you, including us. You called these students light before they did "
   "anything to earn it. Let it be on, and pointed at you. Amen."),
},
}

def fmt(note):
    """Render a leader note as an indented block quote."""
    lines = []
    for para in note.split('\n\n'):
        lines.append('> ' + para.replace('\n', '\n> '))
    return '**LEADER NOTE**\n\n' + '\n>\n'.join(lines) + '\n'

def main():
    src = open(PARTICIPANT).read()
    start = src.find('## **SESSION ONE')
    sessions = re.split(r'(?=## \*\*SESSION (?:ONE|TWO|THREE|FOUR|FIVE|SIX))', src[start:])
    sessions = [s for s in sessions if s.strip()]

    # session six carries the participant back matter; split it off
    back_start = sessions[-1].find('## **Four Questions Before You Borrow**')
    participant_back = ''
    if back_start > 0:
        participant_back = sessions[-1][back_start:]
        sessions[-1] = sessions[-1][:back_start]

    out = [FRONT]
    injected = 0
    for n, sess in enumerate(sessions, 1):
        notes = NOTES.get(n, {})
        # SETUP goes after the session title block, before the memory verse
        mv = sess.find('**MEMORY VERSE**')
        if 'SETUP' in notes and mv > 0:
            sess = sess[:mv] + fmt(notes['SETUP']) + '\n' + sess[mv:]
            injected += 1
        # remaining notes go before their named section header
        for header, note in notes.items():
            if header == 'SETUP':
                continue
            pat = re.compile(r'^(## \*\*' + re.escape(header).replace(r'\'', r"(?:\\)?'") + r'\*\*)$', re.M)
            m = pat.search(sess)
            if m:
                sess = sess[:m.start()] + fmt(note) + '\n' + sess[m.start():]
                injected += 1
            else:
                print(f'  WARNING session {n}: anchor not found -> {header}')
        out.append(sess)

    out.append(participant_back)
    out.append(BACK)
    open(OUT, 'w').write('\n'.join(out))
    print(f'notes injected: {injected}')
    print(f'wrote {OUT}: {len(open(OUT).read().split())} words')

if __name__ == '__main__':
    main()
