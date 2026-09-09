# -*- coding: utf-8 -*-

CAPACITY = {
 "headline":"How many standalone sermons are actually in here",
 "intro":("Two different numbers matter, and conflating them is how catalogue claims stop being believed. "
  "One is how many standalone sermons the library can produce. The other is how many genuinely distinct "
  "ideas sit underneath them. Both are worth saying out loud."),
 "rows":[
  ["Sermon titles already standalone","5,155","Every message in the sermon library is written to stand alone. These need no conversion &mdash; they are already the product."],
  ["Campaigns that can produce an overview sermon","16,379","Every campaign in the platform compresses to one message. The engine already writes the build deterministically."],
  ["Total standalone sermons available","21,534","The honest ceiling, and every one of them can carry six days, a group guide and a ladder."],
  ["Distinct underlying ideas","1,742","The campaign platform's own theme count. This is the number that matters for a preaching calendar."],
  ["Verified Scripture backbones","461","Every reference checked against a canonical verse-count table at build time."],
 ],
 "honest":("Twenty-one thousand is real but it is not twenty-one thousand different ideas. Seventeen thousand campaigns "
  "run on 1,742 themes, which means the same idea appears at different lengths, for different audiences and in "
  "different seasons. That is a feature rather than a defect &mdash; a pastor does not need twenty-one thousand "
  "distinct thoughts, he needs the right one for the Sunday in front of him, at the length he can actually run. "
  "But say 1,742 when someone asks how many ideas, and 21,534 when someone asks how many sermons, and never blur them."),
 "math":[
  ["Every sermon becomes six days","5,155 x 6","30,930 daily devotionals from the sermon library alone"],
  ["Every campaign overview becomes six days","16,379 x 6","98,274 more"],
  ["Total daily devotional slots","","129,204 &mdash; which is why these are generated from the message rather than written by hand"],
 ],
}

SIX_WHY = {
 "line":"Six days, not seven. Sunday is the sermon.",
 "body":("Monday through Saturday belong to the message that was preached, and Sunday is when it comes back. "
  "A seven-day devotional starting on Sunday competes with the sermon it came from. Six days finishes the week "
  "on Saturday and hands the congregation back to the room."),
 "rules":[
  ["Recorded on or before Sunday","One sitting, six videos or six written pieces. If the pastor has to produce something on Tuesday, it will not survive March."],
  ["From the pastor, not from the church","It arrives as him. Same voice they heard Sunday, same face, in their inbox at six in the morning."],
  ["Under two minutes, or under 200 words","Whichever format. The constraint is what makes it repeatable."],
  ["One idea, six angles","Never six new ideas. The message is the idea; the week is the angles."],
  ["Every day ends with the same question","Different wording, same job &mdash; get a story back."],
  ["The reply goes to a human","Not a form, not a no-reply address. Somebody reads them, and that somebody is named."],
 ],
}

TWO_SCRIPTS = [
 ["Sliced","The sermon cut into six",
  "The message itself, divided at its natural seams and re-recorded as six short pieces. His words, his examples, his phrasing &mdash; a congregation hears Sunday again in miniature.",
  ["Highest recognition &mdash; they know they heard this","Zero additional writing; it is already written",
   "Reinforces the exact language of the message","Best when the sermon had strong distinct movements"],
  "Just-in-time. Only usable the week of that sermon."],
 ["Summary","Six clean standalone pieces",
  "Six short devotionals that carry the message's idea without depending on having heard it. Anyone can start on Wednesday and it still works.",
  ["Works for people who missed Sunday","Reusable in a year, or on another campus, or in a rerun",
   "Easier for a guest teacher to record","Best when the sermon was one idea rather than four points"],
  "Evergreen. Recordable months ahead and stockpiled."],
]

SIX_ARC = [
 ["Monday","The hook, again","Reopen the thing that opened the message. Not a recap &mdash; the same door, one day later.",
  "What did Sunday put a finger on for you?"],
 ["Tuesday","The text","Slow down on the passage itself. Read it, then say one thing about what it actually says.",
  "What do you notice in the passage that you missed on Sunday?"],
 ["Wednesday","The honest part","The line in the message that was uncomfortable. Say it again, more personally.",
  "Where is this true about you right now?"],
 ["Thursday","The practice","One concrete thing, today, small enough that it actually happens.",
  "What did you do, and what happened?"],
 ["Friday","The person","Somebody else in it. The idea leaves the head and reaches a name.",
  "Who came to mind, and did you reach out?"],
 ["Saturday","Bring it back","Point at tomorrow. What are we walking into, and what are you carrying in?",
  "What is one sentence you would say out loud about this week?"],
]

STORY_ENGINE = {
 "line":"The question at the bottom is the whole product.",
 "intro":("Every daily devotional ends with one question and a reply box. Those replies are not feedback. "
  "They are the raw material of a story culture, and within about eight weeks a church that has never had "
  "usable testimony has more than it can use."),
 "flow":[
  ["01","The question goes out","Six questions a week, one per devotional, each written to produce a specific kind of answer rather than a general one."],
  ["02","People reply to a human","A named staff member or volunteer, not a form. Replies land in one inbox and nowhere else."],
  ["03","One person curates on Thursday","Fifteen minutes. Read, tag, and move anything usable into the library. Most of it will not be usable and that is fine."],
  ["04","Permission is asked separately","Never assume a reply is publishable. A short, specific, easy-to-decline ask, and a no costs nothing."],
  ["05","Three are used on Sunday","Read from the platform, shown on screen, or told by the person. The congregation hears itself."],
  ["06","The rest goes in the library","Tagged by theme, passage and campaign. Next year's Sunday on the same text already has stories attached to it."],
 ],
 "two_questions":[
  ["Looking back","How did you live out last week's message?","Produces application stories &mdash; what somebody actually did. These are the ones that move a congregation, because they are recent and specific."],
  ["Looking forward","Have you ever lived this out before?","Produces history stories &mdash; something from years ago that fits the message coming Sunday. These can be gathered in advance and are the reason a pastor never has to hunt for an illustration again."],
 ],
 "forward_note":("The forward-looking question is the innovation. Ask it three weeks before the message and the "
  "congregation supplies the illustrations for a sermon that has not been preached yet. The pastor opens Sunday "
  "with a story from row twelve about the exact thing he is about to teach, and nobody in the building can "
  "work out how he did it."),
}

Q_BANK = [
 ["Application","What did you actually do this week because of Sunday?","The workhorse question. Specific verb, recent timeframe."],
 ["Application","What was hard about this one?","Produces honest answers rather than victory reports, and honest answers are more usable."],
 ["Application","Who did you talk to about this?","Surfaces the relational ripple, which is invisible otherwise."],
 ["History","Have you ever been through something like this?","The forward-looking gather. Ask three weeks ahead."],
 ["History","When has God done this in your life before?","Produces testimony rather than anecdote."],
 ["History","What would you tell somebody sitting where you were five years ago?","Produces the most quotable single sentences of any question in the bank."],
 ["Diagnostic","Where are you stuck on this?","Not for publication. This one tells the pastor what to preach next."],
 ["Diagnostic","What did you not understand?","The most valuable and least-asked question in preaching."],
 ["Invitation","Who should hear this?","Turns a reply into an invitation without a campaign."],
]

PERMISSION = {
 "rule":"Never publish a reply without asking, and never make the ask hard to decline.",
 "script":("Thank you for sending that &mdash; it stayed with me. Would you be willing for me to share it on Sunday? "
  "I can use your name, use your first name only, or tell it without any name at all. And if you would rather I "
  "did not, just say so and it changes nothing."),
 "rules":[
  ["Three options, always","Full name, first name only, or anonymous. Offering all three roughly doubles the yes rate."],
  ["Explicit permission to decline","The sentence that makes it safe is the one that says no costs nothing."],
  ["Ask once","A second ask is pressure, regardless of how it is worded."],
  ["Show them the version you will use","Especially if you have shortened it. People say yes to their story and then hear a different one."],
  ["Never use a reply from someone in crisis","Not for a year, and not without a separate conversation. The devotional inbox is not a source."],
  ["Written permission for anything published online","Verbal is fine for a Sunday mention. Social and video need it in writing."],
 ],
}

LIBRARY_SPEC = [
 ["Tagged by theme","Matches the campaign platform's 1,742 themes, so a story attaches to every future message on that idea."],
 ["Tagged by passage","Search by text. Next year's sermon on Luke 15 already has four stories waiting."],
 ["Tagged by campaign","Every campaign accumulates its own stories, which makes the second run of it far stronger than the first."],
 ["Tagged by permission level","Full name, first name, anonymous, or do-not-use. Never guess this."],
 ["Tagged by date","Stories age. A two-year-old story about a job loss may be a very different story now."],
 ["Tagged by usability","Most replies are not stories. Marking the ten percent that are is the whole curation job."],
]

CULTURE = {
 "line":"Eight weeks in, the church changes shape.",
 "stages":[
  ["Weeks 1-2","Almost nobody replies","Expect a handful. This is normal and it is not a failure of the idea. Read one aloud anyway."],
  ["Weeks 3-4","The first real story arrives","Usually from someone nobody expected. Use it. That single use produces the next twenty replies."],
  ["Weeks 5-8","People start writing before they are asked","The congregation works out that somebody is actually reading, and the volume changes."],
  ["Months 3-6","The library becomes usable","Enough tagged stories that the pastor stops hunting and starts choosing."],
  ["Year 2","The culture is self-sustaining","People arrive at church expecting to be asked what happened, which is a different congregation than the one you started with."],
 ],
 "warning":("The single failure mode is nobody reading the replies. If a person writes something real and hears "
  "nothing back, they will not write again and they will tell their group. Reading the inbox is not optional, "
  "and it should be assigned to a named person with fifteen minutes a week rather than to whoever gets to it."),
}
