import { useState, useMemo, useCallback, useEffect, useRef } from "react";

// ─── DATA ─────────────────────────────────────────────────────────────────────
const SECTIONS = [
  {
    id:"easter",label:"Easter & Holy Week",color:"#c9a84c",dark:"#0a0600",icon:"✝",
    crack:"The congregation knows the resurrection happened before the sermon begins. The challenge is not conviction — it is surprise.",
    problem:"You have preached it 5–20 times. The title 'He Is Risen' produces zero narrative tension. The freshness has to come from the angle, not the event.",
    angles:[
      {type:"apologetics",title:"The Most Verified Claim in Ancient History",sub:"The resurrection as the best-attested event in the ancient world",hook:"You cannot dismiss it without engaging it. You cannot engage it without being changed by it."},
      {type:"apologetics",title:"What Five Hundred Witnesses Were Willing to Die For",sub:"People die for what they believe — almost no one dies for what they know is a lie",hook:"The martyrdom of the early church is evidence, not sentiment."},
      {type:"apologetics",title:"The Empty Tomb — A Forensic Analysis",sub:"If the resurrection did not happen, someone has to explain the empty tomb",hook:"Every alternative theory fails. Only one explanation survives the evidence."},
      {type:"apologetics",title:"The Hallucination Theory — Why It Cannot Work",sub:"Mass hallucinations shared by five hundred people simultaneously are psychologically impossible",hook:"Hallucinations are not shared. What the disciples saw was not a shared hallucination."},
      {type:"apologetics",title:"Why the Disciples Could Not Have Stolen the Body",sub:"Traumatized, hiding, afraid — not people who overpower Roman soldiers",hook:"The practical impossibility of the most popular alternative explanation."},
      {type:"apologetics",title:"Two Facts That Demand One Explanation",sub:"The empty tomb and the post-resurrection appearances — only one theory accounts for both",hook:"Every alternative fails on one or the other."},
      {type:"apologetics",title:"N.T. Wright Went Looking for the Body",sub:"The world's leading resurrection scholar who set out to disprove it",hook:"He went looking for the body. He found the argument for the resurrection."},
      {type:"apologetics",title:"Why Women Were the First Witnesses",sub:"No first-century fabricator would choose women as the primary witnesses — their testimony was legally inadmissible",hook:"The detail is embarrassing by ancient standards. Which means it is true."},
      {type:"apologetics",title:"James the Skeptic — Then the Apostle",sub:"Jesus' brother did not believe during the ministry — then led the Jerusalem church",hook:"What turns a skeptical sibling into the head of the movement? He says it was an appearance."},
      {type:"apologetics",title:"The Disciples Were Not Expecting the Resurrection",sub:"They did not manufacture a story to fulfill their expectations — they had none",hook:"You do not make up a story that humiliates your leaders and contradicts your theology."},
      {type:"pastoral",title:"Easter for the Person Who Needs It To Be True",sub:"Preaching the resurrection to the grieving, doubting, and desperate",hook:"If Easter is true, everything changes. If it is not, nothing matters. That is the stakes."},
      {type:"pastoral",title:"The Wound That Thomas Touched",sub:"Not doubting Thomas — the Thomas who asked the question the rest were afraid to ask",hook:"The wounds were not healed. They were glorified. Jesus kept them."},
      {type:"pastoral",title:"The Walk That Took Seven Miles",sub:"Why two disciples left Jerusalem at the worst possible moment",hook:"Grief makes us walk in the wrong direction. Jesus meets us walking."},
      {type:"pastoral",title:"Why Jesus Appeared to Peter Specifically",sub:"The most targeted resurrection appearance in the text",hook:"Jesus did not appear to the person who deserved it first. He appeared to the person who needed it most."},
      {type:"pastoral",title:"Easter for the Parent Who Buried a Child",sub:"The most honest Easter sermon for the most devastating loss",hook:"If Easter is true, death is not the last word about your child."},
      {type:"pastoral",title:"Resurrection in the Middle of Your Winter",sub:"The Easter message for the person whose life does not feel like spring",hook:"The resurrection happened in a cemetery. It does not require favorable conditions."},
      {type:"pastoral",title:"The Grief That Easter Did Not Fix",sub:"When the resurrection is true and the loss is still real",hook:"Mary wept at the empty tomb. The resurrection does not eliminate grief. It reframes it."},
      {type:"pastoral",title:"Easter and the Chronic Illness",sub:"What the resurrection body means for the person whose body has betrayed them",hook:"The resurrection is a promise about your specific body. Paul is not speaking metaphorically."},
      {type:"pastoral",title:"The Eight Days Between the Resurrection and Thomas",sub:"What those days felt like — and what Jesus did when he returned",hook:"He came back for Thomas. He will come back for you."},
      {type:"pastoral",title:"Easter for the Exhausted",sub:"The resurrection for the person who is too tired to feel hopeful",hook:"The disciples were exhausted when Easter arrived. They did not feel like celebrating. The resurrection was true anyway."},
      {type:"narrative",title:"Mary Before She Recognized Him",sub:"The moment between the first sight and the name — she thought he was the gardener",hook:"She had the answer in front of her and did not see it. That is every Easter."},
      {type:"narrative",title:"The Room Where They Were Hiding",sub:"The upper room at Easter evening — he appeared in a locked room",hook:"He did not need the door. He stood among them."},
      {type:"narrative",title:"The Centurion's Easter",sub:"The resurrection from the perspective of the soldier assigned to guard the tomb",hook:"He was paid to make sure the body stayed put. He has some explaining to do on Monday morning."},
      {type:"narrative",title:"The Breakfast Jesus Made",sub:"John 21 — the fire of coals, the fish, the bread — the risen Lord making breakfast",hook:"The risen Lord was cooking breakfast on the beach. That is the kind of resurrection this is."},
      {type:"narrative",title:"The Road to Emmaus — Seven Miles of Explanation",sub:"He explained to them what was said in all the Scriptures about himself",hook:"The best Easter Bible study in history was taught by the risen Christ to people who did not know it was him."},
      {type:"narrative",title:"What Peter Told His Wife That Night",sub:"Imaginative reconstruction of Easter evening in the disciples' homes",hook:"The stories told in Jerusalem that night changed every house that told them."},
      {type:"theological",title:"The Resurrection Is Not a Metaphor",sub:"The costly mistake of spiritualizing the bodily resurrection",hook:"Paul says if there is no bodily resurrection, our faith is worthless. He is not speaking poetically."},
      {type:"theological",title:"Everything Rides on This",sub:"1 Corinthians 15:14 — If Christ has not been raised, our preaching is worthless",hook:"Paul did not say 'it is symbolically important.' He said 'if it did not happen, we have nothing.'"},
      {type:"theological",title:"The First Fruits of the New Creation",sub:"1 Corinthians 15:20 — the most underpreached Easter text",hook:"First fruits means the rest is coming. Easter is the down payment on the whole harvest."},
      {type:"theological",title:"He Showed Them His Hands and His Side",sub:"The resurrection body was scarred — the wounds were glorified, not erased",hook:"The risen Jesus is identifiable by his wounds. This changes everything about suffering."},
      {type:"theological",title:"The Stone Was Not Rolled Away for Jesus",sub:"He had already left — the stone was moved for the witnesses",hook:"Not a barrier for the risen Christ. Evidence for the disciples."},
      {type:"theological",title:"The New Creation Has Already Begun",sub:"Easter is not escape from the world but the beginning of its renewal",hook:"The risen Jesus is the first piece of the new creation. Not the ticket out."},
      {type:"theological",title:"Why the Resurrection Had to Be Bodily",sub:"The philosophical and theological necessity",hook:"A spiritual resurrection would have been easier to believe and useless to depend on."},
      {type:"theological",title:"The Cross Was Not Easter",sub:"Good Friday and Easter Sunday are distinct acts — not one event with different names",hook:"The cross is not enough. The resurrection is not an appendix. Two distinct acts."},
      {type:"theological",title:"The Resurrection as Answer to Gethsemane",sub:"He asked for the cup to be removed — the resurrection is the Father's answer",hook:"He asked for another way. There was not one. The resurrection vindicated the cross."},
      {type:"theological",title:"Resurrection and the Meaning of History",sub:"If Easter happened, history has a direction and a destination",hook:"The resurrection is not just a fact about Jesus. It is a claim about where everything is going."},
      {type:"cultural",title:"Easter and Justice",sub:"What the resurrection of the unjustly executed victim of empire says to every unjust system",hook:"The cross was the empire's final word. The resurrection was God's."},
      {type:"cultural",title:"Easter Is a Political Statement",sub:"Caesar is Lord vs. Jesus is Lord — two claims that cannot coexist",hook:"The earliest Christians were not arrested for piety. They were arrested for treason."},
      {type:"cultural",title:"Easter and the Death of Death",sub:"The last enemy and what the resurrection says about its future",hook:"Death is the last enemy. Easter is the announcement that it has been defeated. The mopping-up operation is underway."},
      {type:"cultural",title:"Easter in a World That Cannot Believe in Progress",sub:"The resurrection as the only credible basis for genuine hope in an age of cynicism",hook:"The world has run out of secular reasons for hope. Easter offers the only remaining basis."},
      {type:"outreach",title:"To the Person Who Came Because Someone Made Them",sub:"The honest Easter sermon for the reluctant attender",hook:"You did not choose to be here today. The question is whether what you hear today changes that."},
      {type:"outreach",title:"If This Is the First Time You Have Heard This",sub:"Preaching the resurrection to the person who has never considered it",hook:"This is either the best news you have ever heard or the most preposterous claim. There is no neutral option."},
      {type:"outreach",title:"What the Skeptic Owes the Evidence",sub:"The sermon for the intellectual who has dismissed the resurrection without examining it",hook:"You have decided on the conclusion. That is not skepticism. That is faith in the wrong direction."},
      {type:"formation",title:"Easter Is the Beginning of the Series",sub:"The sermon that launches what Easter started — not ends it",hook:"Easter Sunday should be the most exciting Sunday of the year to have a small group signup table."},
      {type:"formation",title:"He Is Alive — Now What",sub:"The formation question every Easter sermon should end with but most do not",hook:"The resurrection is not a conclusion. It is a commission."},
      {type:"formation",title:"The Community That Easter Built",sub:"Acts 2 as the formation result of Easter",hook:"The earliest church was not organized around beliefs about the resurrection. It was transformed by the experience of it."},
      {type:"formation",title:"What You Do With Easter Monday",sub:"The specific Monday application of the most significant Sunday",hook:"The resurrection has a Tuesday implication. Name it from the pulpit on Sunday."},
      {type:"formation",title:"The Forty Days Nobody Preaches",sub:"What happened between Easter and Ascension — the formation gap",hook:"Jesus spent forty days with the disciples after the resurrection. He was teaching them something."},
      {type:"lament",title:"Grieving on Easter",sub:"For the congregation that lost someone since last Easter",hook:"You are celebrating something true while grieving something real. The resurrection holds both."},
      {type:"lament",title:"Easter and the Unanswered Prayer",sub:"He raised Jesus from the dead. He did not prevent the crucifixion. Understanding both is the pastoral challenge.",hook:"The resurrection is not evidence that God prevents all suffering. It is evidence that God defeats it."},
    ]
  },
  {
    id:"christmas",label:"Christmas Eve & Advent",color:"#5070a0",dark:"#030508",icon:"✦",
    crack:"The most unchurched room of the year and the most familiar story. The pastor who meets the expectation produces sentiment. The pastor who surprises it produces formation.",
    problem:"The highest percentage of unchurched attenders. The most culturally loaded Sunday. The congregation arrives expecting the familiar story and the familiar feeling.",
    angles:[
      {type:"theological",title:"The Scandal of the Incarnation",sub:"God becoming human was not beautiful at first — it was offensive to first-century sensibility",hook:"We have domesticated what should still disturb us."},
      {type:"theological",title:"John 1 on Christmas Eve",sub:"The most theologically powerful Christmas text is not in Luke 2",hook:"Luke gives you the manger. John gives you the cosmos."},
      {type:"theological",title:"The Inn That Had No Room",sub:"Not a story about innkeepers — a story about what every generation makes room for",hook:"Every generation has to answer the innkeeper's question. Every generation gives the same answer."},
      {type:"theological",title:"Immanuel Is Not Past Tense",sub:"God with us — present tense, active voice, still happening",hook:"Christmas is not a memory. It is a present-tense reality."},
      {type:"theological",title:"Not a Symbol — A Body",sub:"The incarnation is disturbingly physical — he had a heartbeat, got tired, cried",hook:"He had a digestive system. The incarnation is disturbingly physical."},
      {type:"theological",title:"The Theology of a Manger",sub:"What it means that the first cradle was a feeding trough",hook:"He was placed where animals come to be fed. That is the whole gospel in an image."},
      {type:"theological",title:"The Risk of the Incarnation",sub:"What it cost God to become human — vulnerability, limitation, rejection",hook:"The omniscient chose not to know. The omnipotent chose to be helpless. The invulnerable chose to suffer."},
      {type:"theological",title:"The Long Silence Before Bethlehem",sub:"Four hundred years between Malachi and Matthew",hook:"For four centuries, God was silent. Then he cried. In a stable. At night. To shepherds."},
      {type:"theological",title:"The Gift You Cannot Wrap",sub:"God gave himself — not a representative, not a proxy, himself",hook:"Fully. Permanently."},
      {type:"theological",title:"He Became Poor So That We Might Become Rich",sub:"2 Corinthians 8:9 as the best Christmas text",hook:"He did not become poor accidentally. The poverty was the gift."},
      {type:"theological",title:"Fully God and Fully Human — Why Both Matter",sub:"The Council of Chalcedon and the congregation that needs it",hook:"If not fully God, the atonement is insufficient. If not fully human, the identification is not real."},
      {type:"theological",title:"The Pre-Existent Christ at the Manger",sub:"What it means that the one in the manger created the manger",hook:"He made the wood the manger was built from. He made the woman who carried him."},
      {type:"theological",title:"Christmas Without Sentimentality",sub:"The formation sermon for the congregation that has been moved by Christmas and unchanged by it",hook:"If the incarnation is true, sentimentality is the wrong response. Transformation is."},
      {type:"theological",title:"The Second Advent — What Christmas Points Toward",sub:"The Advent sermon about the coming of Christ that has not yet happened",hook:"He came once in humility. He is coming again in glory. Advent prepares us for both."},
      {type:"theological",title:"The Incarnation Is Not Seasonal",sub:"The Christmas sermon that refuses to end with Christmas",hook:"We celebrate the birth annually. We live in the reality of it daily. The difference is formation."},
      {type:"cultural",title:"Christmas as Invasion",sub:"The kingdom of God arrived in occupied territory — a beachhead, not a domestic scene",hook:"The nativity is not peaceful. It is a beachhead."},
      {type:"cultural",title:"What Herod Knew That the Inn Didn't",sub:"The political threat of the incarnation",hook:"Herod tried to kill him because he understood what the innkeeper missed — this changes everything."},
      {type:"cultural",title:"The Magnificat as the Most Dangerous Christmas Song",sub:"Mary's song is not gentle — he has brought down rulers, he has filled the hungry",hook:"This is not a lullaby. It is a revolution."},
      {type:"cultural",title:"The Refugee Family at Christmas",sub:"Joseph, Mary, and the infant Jesus — asylum seekers in Egypt",hook:"The Son of God was a refugee. That is not an argument. It is a text."},
      {type:"cultural",title:"What Christmas Is Not",sub:"Distinguishing the gospel of the incarnation from the cultural festival of Christmas",hook:"The culture has a holiday. The church has an announcement. Those are not the same event."},
      {type:"cultural",title:"Christmas for the Cynic",sub:"The honest Christmas Eve sermon for the person who stopped believing in magic a long time ago",hook:"This is not a fairy tale. It is a historical claim. Fairy tales are not that uncomfortable."},
      {type:"cultural",title:"What December 25 Was Before Christians Claimed It",sub:"The history of the date and what the church was saying by claiming it",hook:"The church did not borrow a pagan holiday. The church announced that the true king had arrived."},
      {type:"pastoral",title:"Christmas for the Person Who Does Not Feel It This Year",sub:"The most honest Christmas Eve sermon",hook:"You came tonight because you were supposed to. What you did not expect was a message for you specifically."},
      {type:"pastoral",title:"Simeon Had Been Waiting His Entire Life",sub:"The old man who held the baby — this is what waiting looks like when what you waited for actually arrives",hook:"He had been told he would not die until he saw the Messiah. He had been waiting."},
      {type:"pastoral",title:"Christmas and the Loneliness Epidemic",sub:"What the incarnation says to the loneliest generation in American history",hook:"God's solution to human isolation was not a message — it was a person. He showed up."},
      {type:"pastoral",title:"Christmas and the People Who Are Missing",sub:"The Christmas Eve sermon for the congregation grieving an empty seat",hook:"The Christmas joy is real. So is the Christmas grief. The incarnation holds both."},
      {type:"pastoral",title:"Christmas and the Person Who Has Lost Everything This Year",sub:"God did not enter human experience at its best — he entered it at its most vulnerable",hook:"He entered the dark. That is why the dark does not have the final word."},
      {type:"pastoral",title:"The Advent Waiting That Was Not Rewarded on Schedule",sub:"The formation of the congregation that has been praying since last Advent",hook:"Four hundred years is a long Advent. Your Advent is shorter. His faithfulness is the same."},
      {type:"pastoral",title:"Christmas and the Unanswered Letter",sub:"God's longest answer to human prayer is the incarnation — he did not write back, he showed up",hook:"He did not send instructions. He did not send a program. He sent himself."},
      {type:"pastoral",title:"What Mary Pondered",sub:"Luke 2:19 — she treasured all these things and pondered them in her heart",hook:"She did not explain it. She did not share it. She kept it. She turned it over. She treasured it."},
      {type:"narrative",title:"What the Shepherds Smelled Like",sub:"The incarnation came first to the people nobody else invited",hook:"God sent the birth announcement to people who worked nights and were not welcome in the synagogue. That is not an accident."},
      {type:"narrative",title:"What Joseph Was Thinking",sub:"The most overlooked character in the nativity — he had a plan. Then an angel appeared.",hook:"His plan was not good enough."},
      {type:"narrative",title:"Anna the Prophetess — The Woman Nobody Preaches",sub:"The eighty-four-year-old widow who recognized the Messiah when the temple missed him",hook:"She had been praying in the temple for decades. She was there when it mattered."},
      {type:"narrative",title:"Elizabeth's Recognition — Before Anyone Else Knew",sub:"The visit of Mary to Elizabeth as the first Christmas testimony",hook:"She recognized the incarnation before there was a manger, a star, or a shepherd."},
      {type:"narrative",title:"What Zechariah Pondered During Nine Months of Silence",sub:"The priest struck mute — his formation through enforced listening",hook:"He could not speak for nine months. He could only listen. That is the first formation move of Advent."},
      {type:"narrative",title:"The Magi Were Not Kings",sub:"They were astronomers from Persia who read Daniel — and followed the evidence",hook:"They were not Jews. They were not religious in the Jewish sense. They followed a star and found a king."},
      {type:"outreach",title:"Christmas Eve for the First-Timer",sub:"The honest Christmas Eve sermon for the person who does not know why they are there",hook:"You are here and you are not sure why. That might be the most important thing about tonight."},
      {type:"outreach",title:"Christmas Eve — Do You Know What Night This Is",sub:"The invitation to stop performing Christmas and actually receive it",hook:"You have prepared for tonight. You dressed up. You came. You sang. Have you received what was given."},
      {type:"outreach",title:"Christmas Eve and the Person Who Has Not Believed in Years",sub:"The gentle re-invitation",hook:"You are here. Something brought you. Consider whether that something might be Someone."},
      {type:"outreach",title:"What Christmas Means If It Is True",sub:"The logical implications of taking the incarnation seriously",hook:"If God became human, nothing about your life is ordinary. Every person is someone God thought worth dying for."},
      {type:"outreach",title:"For Someone Who Was Raised in Church and Left",sub:"The honest conversation with the person who knows the story and stopped caring",hook:"You know the story. You are not sure you believe it anymore. That is the right condition for an honest Advent."},
      {type:"formation",title:"The Cradle and the Cross",sub:"Christmas and Easter as one continuous movement — one story",hook:"They put him in a manger because there was no room. They put him in a tomb because there was no mercy."},
      {type:"formation",title:"What Christmas Asks of You",sub:"The Magi brought something. The shepherds went and told. Mary pondered. What will you do.",hook:"The sermon that closes Christmas Eve with a specific formation response."},
      {type:"formation",title:"Christmas as the Launch of Everything",sub:"The Advent sermon that sets up the formation arc for the next year",hook:"Christmas is not the finish line of Advent. It is the starting line of discipleship."},
      {type:"formation",title:"The Advent Practice That Changed the Year",sub:"The formation discipline of Advent preparation as a yearly rhythm",hook:"The congregation that prepares for Advent arrives at Christmas differently."},
      {type:"formation",title:"The Seven Questions the Incarnation Answers",sub:"Why am I here. Does anyone know me. Is love possible. Can death be defeated.",hook:"The manger addresses the deepest human questions."},
      {type:"lament",title:"The Widower at Christmas",sub:"The first Christmas after the marriage ended by death",hook:"He entered human loneliness so that loneliness is never beyond redemption."},
      {type:"lament",title:"The Year the Christmas Spirit Did Not Arrive",sub:"Preaching to the congregation for whom joy is not accessible this year",hook:"The incarnation does not wait for the right emotional conditions. Neither should we."},
      {type:"theological",title:"God Became Small So We Could Become Large",sub:"The exchange at the heart of the incarnation",hook:"He did not become human to shame us. He became human to elevate us."},
      {type:"theological",title:"First Christmas in John's Prologue",sub:"Eight verses that contain more theology than most entire Christmas sermons",hook:"In the beginning was the Word. Every other Christmas text is a footnote to that sentence."},
    ]
  },
  {
    id:"mothers",label:"Mother's Day",color:"#906060",dark:"#060204",icon:"♡",
    crack:"The most emotionally loaded Sunday for the largest percentage of the congregation. The pastor who names the complexity is the pastor people come back to.",
    problem:"Twenty percent of the room is grieving. Twenty percent has a complicated relationship. Twenty percent is struggling as a mother. The cultural frame owns the day before the pastor opens their mouth.",
    angles:[
      {type:"lament",title:"For the Person for Whom Today Is Complicated",sub:"The sermon that acknowledges every person in the room before it celebrates",hook:"Before we celebrate mothers, we acknowledge that for some of you today is the hardest Sunday of the year."},
      {type:"biblical",title:"Proverbs 31 Was Written By a Man — About His Mother",sub:"A son's tribute, not a woman's job description",hook:"Lemuel wrote this poem about his own mother. It is not a performance standard. It is a love letter."},
      {type:"pastoral",title:"What Hannah Knew That Eli Missed",sub:"The prayer of the barren woman who would not stop praying",hook:"She was praying so intensely the priest thought she was drunk. She was not drunk. She was desperate. God answered."},
      {type:"biblical",title:"The Mothering God — Isaiah 49:15",sub:"Can a mother forget the baby at her breast — Scripture using maternal imagery for God",hook:"Not to make God female — to make God comprehensible to us."},
      {type:"biblical",title:"The Magnificat — What Mary Actually Sang",sub:"The most radical Mother's Day text in the Bible — a revolution, not a lullaby",hook:"She sang about overthrowing the powerful and feeding the hungry. This is the first Christian sermon. It was preached by a teenager."},
      {type:"biblical",title:"Lois and Eunice — The Grandmothers Who Formed an Apostle",sub:"2 Timothy 1:5 — the faith that first lived in his grandmother Lois and his mother Eunice",hook:"Formation is generational."},
      {type:"flagship",title:"The Mother Who Let Go — Mary at the Wedding, Mary at the Cross",sub:"The two moments that define Mary's formation as a mother",hook:"At Cana she released him into his ministry. At Golgotha she released him to his death. Both required everything."},
      {type:"biblical",title:"Deborah — The Mother in Israel",sub:"The military leader whose title was 'a mother in Israel'",hook:"She did not choose the title judge. She was called a mother. The title that mattered was relational."},
      {type:"lament",title:"For the Motherless on Mother's Day",sub:"The honest pastoral sermon for the person whose mother is gone",hook:"Your grief today is not a failure of faith. It is a measure of love."},
      {type:"lament",title:"For the Person Who Is Estranged From Their Mother",sub:"The Mother's Day sermon that names the complicated relationship without fixing it",hook:"Not every mother-child relationship is redemption. The church has to be able to say that."},
      {type:"lament",title:"For the Infertile Woman on Mother's Day",sub:"The most courageous pastoral moment on the church calendar",hook:"If today is the hardest day of the year for you, you are seen. You are not overlooked."},
      {type:"lament",title:"For the Mother Who Is Estranged From Her Child",sub:"The person in the room who is a mother but not to her child today",hook:"You are still a mother. The estrangement did not undo what you gave."},
      {type:"lament",title:"For the Mother of a Prodigal",sub:"The woman who is not celebrating today because her child is not where she hoped",hook:"She has not given up. She has not stopped praying. She is here. That is everything."},
      {type:"lament",title:"Mother's Day and the Baby Who Was Lost",sub:"For the woman grieving a pregnancy or infant loss",hook:"You were a mother. You are still a mother. The church needs to say that."},
      {type:"lament",title:"Mary at the Cross",sub:"What a mother's love looks like when it cannot fix anything",hook:"She could not save him. She could not stop it. She stood there. That is what love does when it cannot do anything else."},
      {type:"pastoral",title:"For the Mother Who Is Failing",sub:"The Mother's Day sermon for the woman who does not feel like a good mother",hook:"The mothers you are comparing yourself to are not real. The mother you are is."},
      {type:"pastoral",title:"For the Single Mother",sub:"The formation in the gap — doing two people's jobs with half the resources",hook:"Strength is not the right word. Neither is sacrifice. Formation is."},
      {type:"pastoral",title:"For the Adoptive Mother",sub:"The mother who chose",hook:"She did not have to. She did. The choice is the point."},
      {type:"pastoral",title:"For the Foster Mother",sub:"The woman who mothers the child who is not hers and may not stay",hook:"The most unrewarded mothering in the culture."},
      {type:"pastoral",title:"For the Stepmother",sub:"The complicated grace of entering a family already formed",hook:"She did not come first. She came willing. That is a different kind of strength."},
      {type:"pastoral",title:"For the Grandmother Raising Her Grandchildren",sub:"The second calling that came when the first was supposed to be finished",hook:"This was not what she planned. It was what was needed. She said yes."},
      {type:"pastoral",title:"For the Mother Who Has Been Doing It Alone",sub:"The sermon that names the invisible labor without romanticizing it",hook:"No one gave her a standing ovation. No one checked in on how she was doing. She just kept going."},
      {type:"flagship",title:"What Your Mother Prayed for You That You Never Heard",sub:"Monica prayed for Augustine for thirty-one years. He did not know.",hook:"Then he became Augustine."},
      {type:"flagship",title:"The Mother Who Released What She Raised",sub:"Hannah giving Samuel to the temple — the hardest act of formation",hook:"She asked for him. She received him. She gave him back. That sequence is the gospel in a family story."},
      {type:"pastoral",title:"Honor Your Mother — Even If It Is Complicated",sub:"The fifth commandment applied pastorally rather than sentimentally",hook:"Honor does not require pretending. It requires a specific kind of respect possible even when the relationship is not whole."},
      {type:"pastoral",title:"What You Would Change If You Could",sub:"The honest Mother's Day sermon about regret and grace",hook:"Every parent wishes they had done something differently. Grace speaks to the specific things."},
      {type:"pastoral",title:"She Was a Mother Before She Was Anything Else",sub:"The identity of the mother as primary formation — and what happens when it is lost",hook:"When the children leave, what remains."},
      {type:"pastoral",title:"The Mother Who Came Alone",sub:"The woman whose family did not come to church with her today",hook:"She came. She has been coming for fifteen years. She has not stopped."},
      {type:"pastoral",title:"The Mother Whose Child Has a Different Faith",sub:"The formation grief of watching a child walk away from what she raised them toward",hook:"She did not fail. She formed. What they do with the formation is not hers to control."},
      {type:"biblical",title:"Ruth Was Not a Mother — Yet",sub:"The formation of faithfulness before the calling is given",hook:"Her faithfulness to Naomi came before the child who would change history. She did not know that."},
      {type:"biblical",title:"Elizabeth — The First Person to Recognize Jesus",sub:"The elderly cousin who recognized what nobody else had seen",hook:"She recognized the incarnation before there was a manger, a star, or a shepherd."},
      {type:"biblical",title:"Jochebed — The Mother Who Saved the Nation",sub:"Exodus 2 — the woman who hid Moses and then received him back",hook:"She did what she could. She trusted what she could not. She received what she gave up."},
      {type:"biblical",title:"Naomi the Theologian",sub:"Who formed Ruth through grief, bitterness, and wisdom",hook:"Naomi told Ruth to go back. Ruth refused. Naomi's formation was stronger than her instruction."},
      {type:"narrative",title:"What Monica Prayed — And for How Long",sub:"The mother of Augustine and the thirty-one years of intercession",hook:"One bishop told her 'the child of those tears cannot be lost.' He was right. But it took thirty-one years."},
      {type:"narrative",title:"What the Prodigal's Mother Was Doing While the Father Ran",sub:"The text does not mention the mother. That silence is not accidental.",hook:"Every family in that culture had a mother. She was present."},
      {type:"narrative",title:"The Last Conversation With My Mother",sub:"The pastoral message for the congregation that has lost a mother",hook:"What would you have said if you had known it was the last time."},
      {type:"flagship",title:"The Blessing That Changes a Child's Life",sub:"What it means to speak a blessing over a child and why most parents never do it",hook:"The blessing was not sentiment. It was formation. It stayed."},
      {type:"formation",title:"The Generational Blessing",sub:"The formation that travels through generations without the middle generation knowing it",hook:"You are not just raising the next generation. You are forming the one after that."},
      {type:"formation",title:"Three Things Every Mother Gives",sub:"Presence, attunement, and blessing — the formation gifts specific to the maternal relationship",hook:"Most mothers give them without knowing they are formation."},
      {type:"formation",title:"The Formation That Happens Before You Can Remember",sub:"What the first three years deposit that the child never consciously receives",hook:"The most formative period of a human life is the period the person cannot recall."},
      {type:"formation",title:"The Prayer Every Mother Should Pray",sub:"Numbers 6:24-26 — the Aaronic blessing as the formation prayer for every child",hook:"The blessing was not metaphor. It was formation. It was the specific words spoken over a specific child."},
      {type:"cultural",title:"What Mothers Do That the Economy Cannot Measure",sub:"The formation work that does not appear in any GDP calculation",hook:"The most important work in the culture is the work that produces people. Nobody pays for it."},
      {type:"cultural",title:"What Hallmark Gets Wrong About Mothers",sub:"The formation the church uniquely offers that Hallmark cannot",hook:"Hallmark sells sentiment. The church offers formation. Different products for different hungers."},
      {type:"cultural",title:"Mothers in Scripture vs. Mothers in the Culture",sub:"The biblical portrait of maternal formation vs. the cultural portrait",hook:"The culture celebrates mothers for what they produce. Scripture celebrates mothers for what they form."},
      {type:"cultural",title:"The Formation Gap — What Happens When Mother's Day Is Not Enough",sub:"The church's responsibility beyond one Sunday per year",hook:"A culture that celebrates mothers one Sunday and devalues mothering every other Sunday is not honoring mothers."},
      {type:"theological",title:"The Church as Mother",sub:"Mater Ecclesia — the ancient concept of the congregation that mothers every believer",hook:"The congregation that forms, feeds, comforts, and disciplines is doing what the best mothers do."},
      {type:"theological",title:"The Woman Who Lost the Coin — A Mother's Day Text",sub:"Luke 15 and the woman who sweeps the house until she finds what she lost",hook:"She does not stop looking. She celebrates when she finds it. She is one of Jesus' images for God."},
      {type:"flagship",title:"The Mother's Day Sermon That Does Not Make Anyone Cry",sub:"The formation alternative to emotional manipulation",hook:"If the only tool in the Mother's Day sermon is sentimentality, the pastor does not trust the text."},
      {type:"flagship",title:"To the Woman Who Wondered If She Mattered",sub:"The sermon that names the invisible formation work",hook:"You mattered. You matter. The formation you gave is still forming the person you gave it to."},
      {type:"pastoral",title:"The Quiet Courage of the Ordinary Mother",sub:"The mother who does not appear in headlines but forms the people who do",hook:"Formation is mostly undramatic. The quiet act repeated ten thousand times is what it looks like."},
      {type:"formation",title:"The Congregation That Mothers the Motherless",sub:"Mater Ecclesia — the church as the mother who forms the person who has no one else",hook:"The church is supposed to do what the best mother does. For everyone."},
    ]
  },
  {
    id:"giving",label:"End-of-Year Giving",color:"#508060",dark:"#030806",icon:"◇",
    crack:"The congregation suspects the sermon is about money before the pastor stands up. The pastor who meets that suspicion has lost. Surprise them with the formation cost of not giving.",
    problem:"The congregation suspects the sermon is about money before the pastor stands up. They have heard the stewardship message annually and are measuring whether this year's version is more or less manipulative.",
    angles:[
      {type:"flagship",title:"What Giving Does to the Giver",sub:"The stewardship sermon entirely about the giver, not the church's need",hook:"The most powerful case for generosity is not the church's budget. It is the soul of the person who gives."},
      {type:"anthropology",title:"The Anthropology of Generosity",sub:"What holding tightly to money does to a person — and what releasing it does",hook:"The hand that gives is open. The hand that holds is closed. You cannot receive with a closed hand."},
      {type:"flagship",title:"The Deceitfulness of Wealth",sub:"Mark 4:19 — Jesus said wealth is deceitful, not dangerous",hook:"Deceitful. It makes promises it cannot keep. That is worse than dangerous."},
      {type:"anthropology",title:"What You Are Becoming While You Are Accumulating",sub:"Every financial decision is also a formation decision",hook:"What you do with money is forming the person you are becoming."},
      {type:"biblical",title:"God Owns It All — Including the Part You Think You Earned",sub:"The stewardship reframe that changes every financial conversation",hook:"You managed someone else's resources. The question is whether you managed them well."},
      {type:"biblical",title:"The Tithe Was Never the Point",sub:"Malachi 3 as a relationship text, not a transaction text",hook:"Bring the whole tithe — and see if I will not open the floodgates. An invitation to an experiment."},
      {type:"flagship",title:"What Jesus Said About Money — All of It",sub:"Thirty-seven parables. Eleven of them about money. Why.",hook:"Jesus talked about money more than any other subject except the kingdom. What was he seeing."},
      {type:"biblical",title:"The Widow's Offering as the Giving Standard",sub:"Not a model for campaigns — a model for the heart",hook:"She held nothing back. Jesus did not celebrate the amount. He celebrated the posture."},
      {type:"flagship",title:"What Your Giving Says About Your Theology",sub:"The budget as a theological statement",hook:"Where your treasure is, your heart will be also. Your bank statement is a theological document."},
      {type:"biblical",title:"The Cheerful Giver — hilaros",sub:"2 Corinthians 9:7 — the Greek word from which we get hilarious",hook:"The giver who gives from that place is laughing."},
      {type:"anthropology",title:"Generosity as the Antidote to Anxiety",sub:"The counterintuitive spiritual therapy for financial worry",hook:"The person most anxious about money usually holds it most tightly. Generosity breaks that pattern."},
      {type:"biblical",title:"The Rich Fool — Updated",sub:"The parable applied to the retirement account, the investment portfolio, the second property",hook:"He built bigger barns. That night his soul was required of him. The barns were full. He was not."},
      {type:"formation",title:"The Formation of the Generous Life — Seven Years In",sub:"What the person who has been tithing for seven years knows that they did not at the start",hook:"The first year of tithing is faith. The seventh year is testimony. The seventeenth year is formation."},
      {type:"biblical",title:"First Fruits as the Ordering Discipline",sub:"The practice that tells your money who is in charge",hook:"When you give first, before anything else is paid, you make a theological statement about who owns the income."},
      {type:"legacy",title:"The Hundred-Year Gift",sub:"The legacy giving sermon that imagines what a hundred-year gift would do",hook:"You will not live to see its full fruit. Neither did the person who gave the gift that formed you."},
      {type:"legacy",title:"The Inheritance Conversation — Before You Have To Have It",sub:"The end-of-year invitation to do estate planning as a family",hook:"The conversation about what you leave behind is not about death. It is about what you value."},
      {type:"formation",title:"Year-End Giving and the Formation of Your Children",sub:"What your children learn by watching what you do with money in December",hook:"You are forming your children's relationship with money right now. Not by what you say about it."},
      {type:"flagship",title:"What Bethlehem Cost God",sub:"The stewardship sermon that begins with incarnation",hook:"God gave the most valuable thing in existence in exchange for the love of people who would mostly reject him."},
      {type:"formation",title:"The Pledge Card as a Prayer",sub:"What happens when the commitment is treated as worship rather than administration",hook:"Write the amount. Sign your name. Pray over it. That changes what you signed."},
      {type:"biblical",title:"What the Early Church Did With Money",sub:"Acts 2:44-45 — they sold property and gave to anyone who had need",hook:"That is not socialism. It is the kingdom."},
      {type:"formation",title:"Contentment Is a Learned Skill",sub:"Philippians 4:11 — I have learned, in whatever state I am, to be content",hook:"Paul does not say he was given contentment. He says he learned it. There is a curriculum."},
      {type:"flagship",title:"The December 31 Decision",sub:"The year-end giving decision as the last formation act of the year",hook:"Before midnight, one more decision. Where does this go. What does this year end with."},
      {type:"formation",title:"The Generosity Formation Arc — Five Years",sub:"What happens to a congregation whose giving formation is tracked over five years",hook:"In year one, the congregation gives to meet a need. In year five, the congregation gives from identity."},
      {type:"cultural",title:"What Amazon Is Doing to Your Soul",sub:"The formation cost of one-click consumption",hook:"Every unplanned purchase is a vote for who is in charge of your money. Generosity is the counter-formation."},
      {type:"cultural",title:"Why Rich People Are Often Miserable",sub:"The research is consistent — above a certain threshold, more money does not produce more happiness",hook:"Something else is required."},
      {type:"biblical",title:"The Matching Gift as a Formation Opportunity",sub:"Not just a financial strategy — a theological invitation",hook:"Every matching gift is a picture of the gospel. Someone else committed first. Your giving joins theirs."},
      {type:"flagship",title:"Generosity and the Great Reversal",sub:"The first will be last — the eschatological giving sermon",hook:"The people who gave most quietly often built the most. The kingdom accounting is different."},
      {type:"formation",title:"The Tithe and the Lie About Affordability",sub:"No one has ever started tithing when they felt they could afford it",hook:"They started before. They found they could."},
      {type:"formation",title:"Year-End Giving and the Formation of Your Marriage",sub:"What happens to a marriage when both partners release their grip on money",hook:"Money is the most common source of marital conflict. Generosity is one of its most reliable antidotes."},
      {type:"formation",title:"The Formation of the Generous Teenager",sub:"The teenager who gives ten percent now is the executive who gives ten percent later",hook:"Formation in small amounts produces character for large ones."},
      {type:"legacy",title:"The Congregation's Endowment — For People Not Yet Born",sub:"The long-arc stewardship sermon about generational giving",hook:"The endowment is not for the congregation that gives it. It is for the congregation that does not yet exist."},
      {type:"flagship",title:"The Last Sermon of the Year Should Be About the First Act of Next Year",sub:"Closing the giving season by opening the formation season",hook:"The best stewardship sermon of the year is not the campaign closer. It is the January formation launcher."},
      {type:"cultural",title:"The Church That the Budget Cannot Capture",sub:"The formation that financial metrics never measure",hook:"The budget tells you what the congregation paid for. It does not tell you what the congregation became."},
      {type:"formation",title:"The Year in Review — What Your Money Did",sub:"The end-of-year accounting as a spiritual discipline",hook:"Where did your money go this year. Not as a guilt exercise. As a formation inventory."},
      {type:"flagship",title:"The Congregation That Could Not Out-Give God",sub:"The annual testimony that keeps the campaign honest",hook:"This is not a sales pitch. This is a report on what we have seen."},
      {type:"anthropology",title:"The Giving That Nobody Saw",sub:"The secret generosity that is the most powerful formation practice",hook:"The gift that is known produces a certain kind of formation. The gift that is unknown produces a deeper kind."},
      {type:"cultural",title:"What the Church Can Offer That GoFundMe Cannot",sub:"The theology of giving as community vs. giving as transaction",hook:"GoFundMe delivers money. The church delivers formation. Different products."},
      {type:"formation",title:"First Fruits of the New Year",sub:"The January 1 giving practice that orders the whole year",hook:"If the first financial act of the new year is a gift, the year is ordered differently from the beginning."},
      {type:"biblical",title:"Zacchaeus and the Formation of Restitution",sub:"Luke 19 — the generosity that goes beyond giving what you have to giving back what you took",hook:"He gave back four times what he had taken. That is not generosity. That is transformation."},
      {type:"flagship",title:"The Stewardship Season vs. The Stewardship Life",sub:"The formation of giving that is not seasonal",hook:"The congregation that only thinks about generosity in October is running a campaign. Not forming generous people."},
      {type:"cultural",title:"Giving in the Age of Subscription",sub:"The formation of intentional generosity in a culture of automatic payment",hook:"You pay your subscriptions automatically. Your giving should require intentionality. That is the difference."},
      {type:"formation",title:"The Percentage That Has Not Changed in Five Years",sub:"The formation audit of the congregation's giving habits",hook:"If your giving percentage has not changed in five years, it is not formation. It is habit."},
      {type:"formation",title:"The Second Gift — Beyond the Tax Deduction",sub:"The giving that is not strategic — purely an act of worship",hook:"The deductible gift is formation. The non-deductible gift is worship."},
      {type:"legacy",title:"What She Left Behind",sub:"The woman who gave ten percent of an ordinary income for forty years and built a school",hook:"She was not wealthy. She was consistent. That is a different kind of wealth."},
      {type:"biblical",title:"The Year-End Gift as Worship",sub:"The December giving decision as a spiritual act, not a financial transaction",hook:"What if the last gift of the year was the most intentional prayer you prayed."},
      {type:"formation",title:"The Generous Church in a Recession",sub:"The formation test of stewardship season in a difficult economic year",hook:"The congregation that gives generously when it is hard has discovered something the comfortable congregation has not."},
      {type:"flagship",title:"The Stewardship Sermon the Budget Committee Wanted — And the Sermon You Need",sub:"The sermon that resists pressure and preaches formation",hook:"The budget committee wants a sermon about the gap. The congregation needs a sermon about the giver."},
    ]
  },
  {
    id:"newyear",label:"New Year Sunday",color:"#7060a0",dark:"#040208",icon:"◉",
    crack:"The gospel does not offer a better resolution. It offers a resurrection. The person who needs a different year does not need a better plan — they need a different identity.",
    problem:"Resolution culture owns January 1. The congregation has already failed their resolutions twice in the last three years. The self-help industry has offered every possible plan. The pastor who offers another plan has nothing new.",
    angles:[
      {type:"theological",title:"Not a Resolution — A Resurrection",sub:"The gospel does not offer a better strategy for change but a different kind of change",hook:"Self-help offers a better version of the person you already are. The gospel offers a different person entirely."},
      {type:"theological",title:"The New Creation Has Already Begun",sub:"2 Corinthians 5:17 as the New Year text",hook:"If anyone is in Christ, there is a new creation. Not coming soon. Already here. Start inhabiting it."},
      {type:"theological",title:"The God Who Makes All Things New",sub:"Revelation 21:5 as the New Year text — all things, not most things",hook:"He did not say 'I am making most things new' or 'I am making new things.' All things."},
      {type:"theological",title:"Beginning in the Middle",sub:"Genesis 1:1 — every beginning is a middle for God. He has been working before you started.",hook:"What looks like your beginning is God's continuation."},
      {type:"theological",title:"The Year Already Redeemed",sub:"The formation theology of giving God the year before you know what it holds",hook:"The year has not happened yet. You can still give it to God before you know what it is."},
      {type:"theological",title:"The Faithfulness That Does Not Need January 1",sub:"God's faithfulness is renewed every morning — not just at the new year",hook:"His mercies are new every morning. Not every January 1. Every morning."},
      {type:"theological",title:"The Second Chance Theology",sub:"The word of the Lord came to Jonah a second time",hook:"God did not give up on the first failure. He never does."},
      {type:"theological",title:"The Promise That Carries the Year",sub:"The specific biblical promise that sustains formation when the January feeling fades",hook:"The formation that carries through December is not built on a January feeling. It is built on a promise."},
      {type:"theological",title:"Epiphany — What the Kings Knew on January 6",sub:"The Magi's arrival as the New Year formation text",hook:"They had traveled for months. They arrived at the right place. They gave what they had. They went home by a different route."},
      {type:"cultural",title:"Why Your Resolutions Have Not Worked",sub:"The formation gap between intention and identity",hook:"You resolve to change your behavior. You do not resolve to change your identity. That is why the behavior change does not last."},
      {type:"cultural",title:"What the Self-Help Industry Cannot Give You",sub:"The specific deficit of every secular New Year approach",hook:"The industry offers you a system. The gospel offers you a new self. Different products."},
      {type:"cultural",title:"The January Gym Effect — And Its Church Equivalent",sub:"Why January formation intentions follow the same curve as fitness resolutions",hook:"By February, the gym is back to normal. Formation requires more than January enthusiasm."},
      {type:"cultural",title:"The New Year Industrial Complex",sub:"The $12 billion self-help industry that arrives every January and leaves by March",hook:"The industry grows because the product does not work. If resolutions worked, the industry would shrink. It keeps growing."},
      {type:"cultural",title:"What New Year Tells Us About Human Nature",sub:"The universal desire for fresh starts — and what it points toward",hook:"Every culture in every century has marked the new year as a beginning. That universal desire is pointing somewhere."},
      {type:"cultural",title:"What January 2 Feels Like",sub:"The formation gap between the New Year intention and the first ordinary workday",hook:"January 2 is the formation test. The sermon that prepares you for January 2 is more useful than the one that celebrates January 1."},
      {type:"cultural",title:"The Self-Help Promise and the Gospel Promise",sub:"What the industry offers vs. what the gospel offers — and why only one can deliver",hook:"The industry offers self-improvement. The gospel offers self-surrender. Those produce different outcomes."},
      {type:"pastoral",title:"The Year That Did Not Go As You Planned",sub:"The New Year sermon for the congregation whose last year was a loss",hook:"You planned one year. You lived a different one. The question is whether what you lived formed you."},
      {type:"pastoral",title:"New Year for the Person Who Has Run Out of Hope",sub:"The congregation that has tried and failed and is not sure it can try again",hook:"The God of new beginnings is not deterred by your history with new beginnings."},
      {type:"pastoral",title:"The New Year After the Worst Year",sub:"For the congregation that cannot imagine the new year being better",hook:"He makes all things new. Including the things that broke. Especially the things that broke."},
      {type:"pastoral",title:"The New Year Grief",sub:"For the congregation for whom the new year marks the anniversary of a loss",hook:"The calendar does not wait for grief to finish. The new year arrives whether or not you are ready."},
      {type:"pastoral",title:"The New Year for the Exhausted",sub:"The formation of rest before the year begins",hook:"You are beginning the year exhausted. That is data, not failure. The formation this year needs may be rest first."},
      {type:"pastoral",title:"The New Year for the Person Who Cannot Afford to Hope",sub:"The person who has been disappointed too many times to risk another expectation",hook:"Hope deferred makes the heart sick. But the hope the gospel offers is not optimism. It is promise."},
      {type:"pastoral",title:"The Person Who Made the Same Resolution Last Year",sub:"The New Year sermon for the person who is back at the same starting line",hook:"The fact that you are back at the starting line means you started. Starting is not the problem. Sustaining is."},
      {type:"pastoral",title:"The Fresh Start That Is Not Earned",sub:"The grace that makes New Year different from performance improvement",hook:"You are not starting with a clean slate because you deserve one. You are starting because someone else paid for it."},
      {type:"pastoral",title:"The New Year Surrender",sub:"Releasing the year to God before you know what it holds",hook:"You cannot control this year. You can only give it. The question is whether you give it to the right person."},
      {type:"biblical",title:"Lamentations 3 — Great Is Your Faithfulness for a New Year",sub:"The New Year text from inside the most hopeless book in the Bible",hook:"His mercies are new every morning. That is not a song lyric. It is a survival theology."},
      {type:"biblical",title:"Joshua 3 — You Have Never Been This Way Before",sub:"Follow the ark into the Jordan — the formation of following into the unknown",hook:"You have never been this way before. Neither had they. They followed anyway."},
      {type:"biblical",title:"Forget the Former Things — Isaiah 43:18",sub:"The New Year command that is also the formation discipline",hook:"Do not dwell on the past. See, I am doing a new thing. The new thing requires releasing the former things."},
      {type:"biblical",title:"Jeremiah 29 — Seek the Peace of This Year",sub:"Build houses. Plant gardens. The formation of settling into the year you are actually in.",hook:"Stop wishing for the year you are not in. Build in the year you are."},
      {type:"biblical",title:"Ecclesiastes 1 and the New Year",sub:"Vanity of vanities — the Preacher's cynicism is the right starting point",hook:"If you begin the year without acknowledging what did not work last year, you are setting up the same failure."},
      {type:"biblical",title:"Paul Pressing On — Philippians 3 for January",sub:"Forgetting what is behind and straining toward what is ahead",hook:"He does not look back to measure the gap. He looks forward to measure the distance."},
      {type:"biblical",title:"The Prodigal's Return as New Year Text",sub:"He came to himself — the formation of waking up in January",hook:"'He came to himself.' He saw his life clearly. He turned. That is the New Year moment."},
      {type:"biblical",title:"Psalm 90 for the New Year — Moses' Prayer",sub:"A thousand years in your sight are like a watch in the night",hook:"Teach us to number our days. Not to be morbid. To be intentional."},
      {type:"biblical",title:"Deuteronomy 8 — Remember the Wilderness Year",sub:"Do not forget what God did in the year you thought was wasted",hook:"He tested you, humbled you, provided for you — in the year you thought was not working."},
      {type:"formation",title:"The Formation That Lasts Past February",sub:"Why spiritual practices succeed where resolutions fail",hook:"A resolution is about behavior. A practice is about formation. Only one produces a new person."},
      {type:"formation",title:"The One Formation Practice Worth Keeping",sub:"The case for a single sustainable formation commitment over multiple resolutions",hook:"You are more likely to keep one practice for twelve months than twelve practices for one month."},
      {type:"formation",title:"The New Year Prayer That Changes the Year",sub:"What it means to surrender the year instead of resolving to improve it",hook:"The most powerful New Year practice is not a plan. It is a surrender."},
      {type:"formation",title:"The Small Faithful Thing — Every Day",sub:"The formation alternative to ambitious New Year declarations",hook:"One small faithful thing, done every day, produces more formation than ten ambitious things done occasionally."},
      {type:"formation",title:"Three Formation Questions for the New Year",sub:"What am I becoming. What am I releasing. What am I beginning.",hook:"Three questions. One year. Different person."},
      {type:"formation",title:"The Word for This Year",sub:"The formation practice of choosing one word for the year",hook:"One word. Twelve months. The formation of sustained intentional attention on a single virtue."},
      {type:"formation",title:"The New Year Small Group Launch",sub:"The most important formation window of the year — and the strategic move",hook:"More people are open to formation in January than at any other time of the year."},
      {type:"formation",title:"The Community That Carries You Through the Year",sub:"The New Year small group launch as the most important formation decision of January",hook:"The formation that lasts through December is not individual. It is communal."},
      {type:"formation",title:"What You Are Reading in January",sub:"The formation of the congregation's reading life at the beginning of the year",hook:"What goes into you in January shapes you in December. Choose intentionally."},
      {type:"formation",title:"The Person You Will Be on December 31",sub:"The formation question that changes January behavior",hook:"Imagine the person you want to be at the end of this year. What does that person do in January."},
      {type:"formation",title:"The Year as a Gift You Have Not Opened Yet",sub:"The New Year as the gift theology of time",hook:"You have been given a year. You have not used it yet. What you do with it is not a resolution. It is a stewardship."},
      {type:"formation",title:"The Formation Rhythm for the Year",sub:"The daily, weekly, monthly, and annual practices that form a person over twelve months",hook:"The year is not a blank slate. It is a formation container. What you put in it determines who comes out."},
      {type:"theological",title:"The Year You Cannot Waste",sub:"Romans 8:28 and the formation theology of redeemed time",hook:"God can work all things together. Including the year you are afraid to give him."},
      {type:"formation",title:"What Generosity in January Produces in December",sub:"The New Year giving decision as a formation investment in the year's ending",hook:"The congregation that begins the year with a generous act is forming the person who ends the year generously."},
      {type:"pastoral",title:"What You Learned From the Year That Broke You",sub:"The New Year sermon for the congregation whose last year was the hardest yet",hook:"The year that broke you was also the year that showed you what you are made of."},
      {type:"theological",title:"The God of Beginnings",sub:"Genesis 1:1 — the first thing Scripture says about God is that he begins",hook:"He is a beginner. He began you. He is not finished."},
    ]
  }
];

// ─── TYPE CONFIG ──────────────────────────────────────────────────────────────
const TYPE_CONFIG = {
  flagship:    {label:"Flagship",       color:"#c9a84c", bg:"rgba(201,168,76,.1)"},
  apologetics: {label:"Apologetics",    color:"#7060b0", bg:"rgba(112,96,176,.08)"},
  pastoral:    {label:"Pastoral",       color:"#4a7aaa", bg:"rgba(74,122,170,.08)"},
  narrative:   {label:"Narrative",      color:"#8a6040", bg:"rgba(138,96,64,.08)"},
  theological: {label:"Theological",    color:"#3a7a5a", bg:"rgba(58,122,90,.08)"},
  cultural:    {label:"Cultural",       color:"#6a4a8a", bg:"rgba(106,74,138,.08)"},
  outreach:    {label:"Outreach",       color:"#5a9060", bg:"rgba(90,144,96,.08)"},
  formation:   {label:"Formation",      color:"#8a7030", bg:"rgba(138,112,48,.08)"},
  lament:      {label:"Lament",         color:"#9a4040", bg:"rgba(154,64,64,.08)"},
  biblical:    {label:"Biblical",       color:"#3a6a8a", bg:"rgba(58,106,138,.08)"},
  anthropology:{label:"Anthropology",   color:"#7a5050", bg:"rgba(122,80,80,.08)"},
  legacy:      {label:"Legacy",         color:"#506870", bg:"rgba(80,104,112,.08)"},
};
const ALL_TYPES = Object.keys(TYPE_CONFIG);

// ─── STYLES ───────────────────────────────────────────────────────────────────
const S = `
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Lato:wght@300;400;700&family=Inter:wght@400;500;600&display=swap');
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Lato',sans-serif;background:#18141e;color:#1a1412;}
.app{min-height:100vh;display:flex;flex-direction:column;}

/* HEADER */
.hdr{background:#0a0810;border-bottom:1px solid rgba(201,168,76,.12);padding:13px 24px;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.hdr-brand{font-family:'Playfair Display',serif;font-size:15px;font-style:italic;color:rgba(255,255,255,.5);letter-spacing:1px;}
.hdr-tag{font-size:7.5px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:#8a6e30;border:1px solid rgba(201,168,76,.2);padding:3px 10px;}
.hdr-stats{display:flex;align-items:center;gap:16px;}
.hdr-stat{text-align:center;}
.hdr-stat-n{font-family:'Playfair Display',serif;font-size:18px;color:#c9a84c;display:block;line-height:1;}
.hdr-stat-l{font-size:7px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.2);font-weight:700;}

/* TABS */
.tabs{background:#0e0c14;border-bottom:1px solid rgba(255,255,255,.06);display:flex;padding:0 18px;overflow-x:auto;flex-shrink:0;}
.tabs::-webkit-scrollbar{height:2px;background:transparent;}
.tabs::-webkit-scrollbar-thumb{background:rgba(201,168,76,.2);}
.tab{display:flex;align-items:center;gap:8px;padding:12px 16px;font-size:12px;font-weight:600;color:rgba(255,255,255,.35);cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:all .12s;flex-shrink:0;user-select:none;}
.tab:hover{color:rgba(255,255,255,.6);}
.tab.on{border-bottom-color:var(--c);color:var(--c);}
.tab-icon{font-size:14px;}
.tab-count{font-size:9px;padding:1px 5px;border-radius:10px;font-weight:700;background:rgba(255,255,255,.06);}
.tab.on .tab-count{background:rgba(255,255,255,.12);}

/* BODY LAYOUT */
.body{display:flex;flex:1;overflow:hidden;height:calc(100vh - 100px);}
.sidebar{width:240px;background:#0e0c14;border-right:1px solid rgba(255,255,255,.06);flex-shrink:0;overflow-y:auto;display:flex;flex-direction:column;}
.main{flex:1;overflow-y:auto;background:#f4f0e8;}

/* SIDEBAR */
.sb-section{padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.05);}
.sb-label{font-size:7.5px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:rgba(255,255,255,.22);display:block;margin-bottom:10px;}
.search-wrap{position:relative;}
.search-input{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:#f4f0e8;padding:8px 10px 8px 30px;font-size:12px;width:100%;font-family:'Lato',sans-serif;outline:none;}
.search-input::placeholder{color:rgba(255,255,255,.25);}
.search-input:focus{border-color:rgba(201,168,76,.35);}
.search-icon{position:absolute;left:9px;top:50%;transform:translateY(-50%);font-size:12px;color:rgba(255,255,255,.3);}
.type-filter{display:flex;flex-direction:column;gap:2px;}
.type-btn{display:flex;align-items:center;justify-content:space-between;padding:5px 10px;cursor:pointer;transition:all .1s;border:none;background:transparent;width:100%;text-align:left;border-left:2px solid transparent;}
.type-btn:hover{background:rgba(255,255,255,.03);}
.type-btn.on{border-left-color:var(--tc);background:rgba(255,255,255,.05);}
.type-btn-left{display:flex;align-items:center;gap:6px;}
.type-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;}
.type-btn-label{font-size:11px;color:rgba(255,255,255,.4);font-weight:500;}
.type-btn.on .type-btn-label{color:var(--tc);font-weight:600;}
.type-count{font-size:9px;color:rgba(255,255,255,.2);font-weight:600;}
.type-btn.on .type-count{color:var(--tc);opacity:.7;}
.clear-btn{font-size:9px;color:#c9a84c;cursor:pointer;display:block;padding:8px 10px;letter-spacing:1px;text-transform:uppercase;font-weight:700;}
.clear-btn:hover{color:#e2c97e;}

/* CRACK BOX */
.crack-section{padding:16px 22px;border-bottom:1px solid rgba(201,168,76,.15);background:rgba(201,168,76,.03);}
.crack-label{font-size:7px;letter-spacing:3px;text-transform:uppercase;font-weight:700;color:#8a6e30;display:block;margin-bottom:5px;}
.crack-text{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:#2a2010;line-height:1.5;}

/* ANGLE GRID */
.grid-section{padding:18px 22px;}
.grid-header{display:flex;align-items:baseline;gap:10px;margin-bottom:14px;}
.grid-title{font-family:'Playfair Display',serif;font-size:20px;font-style:italic;color:#1a1412;}
.grid-count{font-size:11px;color:#888;}
.angles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;}
.angle-card{padding:12px 14px;border:1px solid rgba(0,0,0,.07);background:#fff;cursor:pointer;transition:all .1s;position:relative;border-top:3px solid transparent;}
.angle-card:hover{box-shadow:0 3px 14px rgba(0,0,0,.12);transform:translateY(-1px);}
.angle-card.featured{border:2px solid rgba(201,168,76,.5);background:linear-gradient(135deg,rgba(201,168,76,.06),rgba(201,168,76,.01));}
.angle-card.selected{box-shadow:0 0 0 2px var(--c);background:rgba(255,255,255,.98);}
.ac-type{font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;display:block;margin-bottom:4px;}
.ac-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;line-height:1.25;margin-bottom:4px;color:#1a1412;}
.ac-sub{font-size:9.5px;color:#777;font-family:'Georgia',serif;font-style:italic;line-height:1.35;margin-bottom:4px;}
.ac-hook{font-size:8.5px;color:#555;font-family:'Georgia',serif;padding:4px 8px;border-left:2px solid rgba(201,168,76,.35);background:rgba(201,168,76,.03);line-height:1.4;}

/* AI PANEL */
.ai-panel{background:#0e0c14;border-top:1px solid rgba(255,255,255,.06);}
.ai-toggle{display:flex;align-items:center;gap:10px;padding:10px 22px;cursor:pointer;user-select:none;}
.ai-toggle-label{font-size:11.5px;font-weight:600;color:rgba(255,255,255,.5);letter-spacing:.5px;}
.ai-toggle-badge{font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#c9a84c;border:1px solid rgba(201,168,76,.25);padding:2px 7px;}
.ai-panel-body{padding:16px 22px;border-top:1px solid rgba(255,255,255,.06);}
.ai-prompt-row{display:flex;gap:8px;margin-bottom:10px;}
.ai-input{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);color:#f4f0e8;padding:9px 12px;font-size:12px;flex:1;font-family:'Lato',sans-serif;outline:none;}
.ai-input::placeholder{color:rgba(255,255,255,.25);}
.ai-input:focus{border-color:rgba(201,168,76,.4);}
.ai-btn{background:#c9a84c;color:#000;border:none;padding:9px 18px;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;cursor:pointer;font-family:'Lato',sans-serif;white-space:nowrap;transition:background .12s;}
.ai-btn:hover{background:#e2c97e;}
.ai-btn:disabled{opacity:.4;cursor:not-allowed;}
.ai-options{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px;}
.ai-opt{font-size:9.5px;padding:4px 10px;border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.35);cursor:pointer;transition:all .1s;background:transparent;font-family:'Lato',sans-serif;}
.ai-opt:hover,.ai-opt.on{border-color:rgba(201,168,76,.5);color:#c9a84c;background:rgba(201,168,76,.08);}
.ai-thinking{display:flex;align-items:center;gap:10px;padding:12px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);margin-bottom:10px;}
.ai-pulse{width:8px;height:8px;border-radius:50%;background:#c9a84c;animation:pulse 1.2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.2;}}
.ai-thinking-txt{font-size:12px;color:rgba(255,255,255,.45);}
.ai-results{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;}
.ai-card{background:rgba(255,255,255,.06);border:1px solid rgba(201,168,76,.2);padding:12px 14px;}
.ai-card-badge{font-size:7px;letter-spacing:2px;text-transform:uppercase;font-weight:700;color:#c9a84c;display:block;margin-bottom:5px;}
.ai-card-title{font-family:'Playfair Display',serif;font-size:13px;font-style:italic;color:#f4f0e8;line-height:1.3;margin-bottom:4px;}
.ai-card-hook{font-size:9.5px;color:rgba(255,255,255,.5);font-family:'Georgia',serif;font-style:italic;line-height:1.4;border-left:2px solid rgba(201,168,76,.3);padding-left:8px;}
.ai-error{font-size:11px;color:#e08080;padding:10px;background:rgba(180,50,50,.1);border:1px solid rgba(180,50,50,.2);}
.ai-hint{font-size:10px;color:rgba(255,255,255,.25);font-style:italic;}

/* DETAIL PANEL */
.detail-panel{background:#fff;border-top:3px solid var(--c,#c9a84c);padding:20px 22px;}
.dp-close{position:absolute;top:12px;right:14px;font-size:16px;cursor:pointer;color:#bbb;}
.dp-type{font-size:7.5px;letter-spacing:3px;text-transform:uppercase;font-weight:700;display:block;margin-bottom:6px;}
.dp-title{font-family:'Playfair Display',serif;font-size:20px;font-style:italic;line-height:1.2;margin-bottom:6px;color:#1a1412;}
.dp-sub{font-family:'Georgia',serif;font-size:13px;color:#666;font-style:italic;margin-bottom:12px;line-height:1.5;}
.dp-hook{font-family:'Georgia',serif;font-size:13px;color:#333;padding:10px 14px;border-left:3px solid var(--c,#c9a84c);background:rgba(201,168,76,.04);line-height:1.55;margin-bottom:12px;}
.dp-actions{display:flex;gap:8px;}
.dp-action{font-size:9px;letter-spacing:1.5px;text-transform:uppercase;font-weight:700;padding:7px 14px;border:1px solid;cursor:pointer;background:transparent;font-family:'Lato',sans-serif;transition:all .1s;}

/* EMPTY */
.empty{text-align:center;padding:60px 20px;color:#aaa;}
.empty-icon{font-size:32px;display:block;margin-bottom:10px;}
.empty-text{font-family:'Playfair Display',serif;font-size:18px;font-style:italic;color:#bbb;margin-bottom:5px;}

@media(max-width:900px){
  .angles-grid,.ai-results{grid-template-columns:1fr 1fr;}
  .sidebar{width:200px;}
}
@media(max-width:640px){
  .angles-grid,.ai-results{grid-template-columns:1fr;}
  .sidebar{display:none;}
}
`;

// ─── MAIN APP ─────────────────────────────────────────────────────────────────
export default function FreshSermonAngles() {
  const [activeId, setActiveId] = useState("easter");
  const [search, setSearch] = useState("");
  const [selTypes, setSelTypes] = useState([]);
  const [selectedAngle, setSelectedAngle] = useState(null);
  const [aiOpen, setAiOpen] = useState(false);
  const [aiPrompt, setAiPrompt] = useState("");
  const [aiType, setAiType] = useState("");
  const [aiResults, setAiResults] = useState([]);
  const [generating, setGenerating] = useState(false);
  const [aiError, setAiError] = useState("");

  const section = SECTIONS.find(s => s.id === activeId);

  // Compute type counts for current section
  const typeCounts = useMemo(() => {
    const counts = {};
    section.angles.forEach(a => { counts[a.type] = (counts[a.type]||0)+1; });
    return counts;
  }, [section]);

  // Filter angles
  const filtered = useMemo(() => {
    let res = section.angles;
    if (selTypes.length) res = res.filter(a => selTypes.includes(a.type));
    if (search) {
      const q = search.toLowerCase();
      res = res.filter(a =>
        a.title.toLowerCase().includes(q) ||
        a.sub.toLowerCase().includes(q) ||
        a.hook.toLowerCase().includes(q)
      );
    }
    return res;
  }, [section, selTypes, search]);

  // Toggle type
  const toggleType = useCallback(t => {
    setSelTypes(prev => prev.includes(t) ? prev.filter(x=>x!==t) : [...prev, t]);
  }, []);

  // AI Generate
  async function generateAngles() {
    if (!aiPrompt.trim() && !aiType) return;
    setGenerating(true); setAiError(""); setAiResults([]);
    const ctx = `Sunday: ${section.label}. The pastoral crack: ${section.crack}`;
    const typeFilter = aiType ? `Focus on the rhetorical angle: ${aiType}.` : "";
    const prompt = `You are a master preaching consultant for senior pastors. Generate 6 fresh, original sermon angles for ${section.label}.

Context: ${ctx}
${typeFilter}
Pastor's specific need: ${aiPrompt || "Fresh angles that avoid clichés"}

Rules:
- Every angle must be genuinely surprising — not the obvious approach
- Each must have a specific hook sentence that would stop a tired pastor mid-scroll
- The sub-description must make the theological move clear in one sentence
- Avoid: "He Is Risen," "the true meaning," generic encouragement, anything that sounds like it could be in any sermon library
- Type must be one of: apologetics, pastoral, narrative, theological, cultural, outreach, formation, lament, biblical

Respond ONLY with valid JSON array, no other text:
[{"title":"...","sub":"...","hook":"...","type":"..."},{"title":"...","sub":"...","hook":"...","type":"..."},{"title":"...","sub":"...","hook":"...","type":"..."},{"title":"...","sub":"...","hook":"...","type":"..."},{"title":"...","sub":"...","hook":"...","type":"..."},{"title":"...","sub":"...","hook":"...","type":"..."}]`;

    try {
      const r = await fetch("https://api.anthropic.com/v1/messages", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({model:"claude-sonnet-4-6",max_tokens:1000,messages:[{role:"user",content:prompt}]})
      });
      const d = await r.json();
      const txt = d.content?.find(b=>b.type==="text")?.text||"";
      const clean = txt.replace(/```json|```/g,"").trim();
      setAiResults(JSON.parse(clean));
    } catch(err) {
      setAiError("Generation failed — try a more specific prompt.");
    } finally { setGenerating(false); }
  }

  const c = section.color;

  return (
    <>
      <style>{S}</style>
      <div className="app">
        {/* HEADER */}
        <div className="hdr">
          <div className="hdr-brand">Lifetogether · Fresh Sermon Intelligence™</div>
          <div className="hdr-stats">
            <div className="hdr-stat"><span className="hdr-stat-n">5</span><span className="hdr-stat-l">Hard Sundays</span></div>
            <div className="hdr-stat"><span className="hdr-stat-n">{SECTIONS.reduce((a,s)=>a+s.angles.length,0)}</span><span className="hdr-stat-l">Fresh Angles</span></div>
            <div className="hdr-stat"><span className="hdr-stat-n">AI</span><span className="hdr-stat-l">Generator</span></div>
          </div>
          <span className="hdr-tag">2026 Edition</span>
        </div>

        {/* SECTION TABS */}
        <div className="tabs">
          {SECTIONS.map(s => (
            <div key={s.id} className={`tab ${activeId===s.id?"on":""}`}
              style={{"--c":s.color}} onClick={()=>{setActiveId(s.id);setSelectedAngle(null);setSearch("");setSelTypes([]);setAiResults([]);}}>
              <span className="tab-icon">{s.icon}</span>
              {s.label}
              <span className="tab-count">{s.angles.length}</span>
            </div>
          ))}
        </div>

        {/* BODY */}
        <div className="body">
          {/* SIDEBAR */}
          <div className="sidebar">
            <div className="sb-section">
              <span className="sb-label">Search</span>
              <div className="search-wrap">
                <span className="search-icon">🔍</span>
                <input className="search-input" value={search} onChange={e=>setSearch(e.target.value)} placeholder="Title, topic, hook…"/>
              </div>
            </div>
            <div className="sb-section" style={{flex:1,overflow:"auto"}}>
              <span className="sb-label">Filter by Angle Type</span>
              <div className="type-filter">
                {ALL_TYPES.filter(t => typeCounts[t]).map(t => {
                  const cfg = TYPE_CONFIG[t];
                  const on = selTypes.includes(t);
                  return (
                    <button key={t} className={`type-btn ${on?"on":""}`}
                      style={{"--tc":cfg.color}} onClick={()=>toggleType(t)}>
                      <div className="type-btn-left">
                        <div className="type-dot" style={{background:cfg.color}}/>
                        <span className="type-btn-label">{cfg.label}</span>
                      </div>
                      <span className="type-count">{typeCounts[t]||0}</span>
                    </button>
                  );
                })}
              </div>
              {selTypes.length>0 && <span className="clear-btn" onClick={()=>setSelTypes([])}>✕ Clear filters</span>}
            </div>
          </div>

          {/* MAIN */}
          <div className="main">
            {/* CRACK */}
            <div className="crack-section" style={{borderBottomColor:`${c}30`}}>
              <span className="crack-label">The Crack — The Fresh Angle for {section.label}</span>
              <p className="crack-text">{section.crack}</p>
            </div>

            {/* SELECTED DETAIL */}
            {selectedAngle && (() => {
              const cfg = TYPE_CONFIG[selectedAngle.type] || TYPE_CONFIG.theological;
              return (
                <div className="detail-panel" style={{"--c":cfg.color,position:"relative"}}>
                  <span className="dp-close" onClick={()=>setSelectedAngle(null)}>✕</span>
                  <span className="dp-type" style={{color:cfg.color}}>{cfg.label} Angle</span>
                  <h2 className="dp-title">{selectedAngle.title}</h2>
                  <p className="dp-sub">{selectedAngle.sub}</p>
                  <div className="dp-hook">{selectedAngle.hook}</div>
                  <div className="dp-actions">
                    <button className="dp-action" style={{borderColor:cfg.color,color:cfg.color}}
                      onClick={()=>{setAiPrompt(`Develop more angles like: "${selectedAngle.title}"`);setAiOpen(true);}}>
                      → Generate Similar with AI
                    </button>
                    <button className="dp-action" style={{borderColor:"#aaa",color:"#888"}}
                      onClick={()=>setSelectedAngle(null)}>
                      Close
                    </button>
                  </div>
                </div>
              );
            })()}

            {/* ANGLES GRID */}
            <div className="grid-section">
              <div className="grid-header">
                <h2 className="grid-title">{section.label} · Fresh Angles</h2>
                <span className="grid-count">{filtered.length} of {section.angles.length}</span>
              </div>
              {filtered.length===0 ? (
                <div className="empty">
                  <span className="empty-icon">🔍</span>
                  <p className="empty-text">No angles match</p>
                  <p>Try different search terms or clear filters</p>
                </div>
              ) : (
                <div className="angles-grid">
                  {filtered.map((a,i) => {
                    const cfg = TYPE_CONFIG[a.type] || TYPE_CONFIG.theological;
                    const isSel = selectedAngle===a;
                    return (
                      <div key={i}
                        className={`angle-card ${a.type==="flagship"?"featured":""} ${isSel?"selected":""}`}
                        style={{borderTopColor:cfg.color,"--c":cfg.color}}
                        onClick={()=>setSelectedAngle(isSel?null:a)}>
                        <span className="ac-type" style={{color:cfg.color}}>{cfg.label}</span>
                        <h3 className="ac-title">{a.title}</h3>
                        <p className="ac-sub">{a.sub}</p>
                        {isSel && <div className="ac-hook" style={{borderLeftColor:cfg.color}}>{a.hook}</div>}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            {/* AI GENERATOR */}
            <div className="ai-panel">
              <div className="ai-toggle" onClick={()=>setAiOpen(o=>!o)}>
                <span style={{fontSize:16,color:"#c9a84c"}}>✦</span>
                <span className="ai-toggle-label">AI Sermon Angle Generator</span>
                <span className="ai-toggle-badge">Claude Sonnet · Live</span>
                <span style={{marginLeft:"auto",color:"rgba(255,255,255,.3)",fontSize:12}}>{aiOpen?"▲":"▼"}</span>
              </div>

              {aiOpen && (
                <div className="ai-panel-body">
                  <p className="ai-hint" style={{marginBottom:10}}>Describe your specific need — congregation, series theme, felt need, or approach you want to avoid — and Claude will generate 6 original angles not in the library above.</p>
                  <div className="ai-prompt-row">
                    <input className="ai-input" value={aiPrompt} onChange={e=>setAiPrompt(e.target.value)}
                      placeholder={`Fresh angle for ${section.label} — describe your congregation or felt need…`}
                      onKeyDown={e=>e.key==="Enter"&&generateAngles()}/>
                    <button className="ai-btn" disabled={generating||(!aiPrompt.trim()&&!aiType)} onClick={generateAngles}>
                      {generating?"Generating…":"Generate →"}
                    </button>
                  </div>
                  <div className="ai-options">
                    <span className="ai-hint" style={{alignSelf:"center",marginRight:4}}>Focus:</span>
                    {["apologetics","pastoral","narrative","theological","cultural","outreach","formation","lament"].map(t=>(
                      <button key={t} className={`ai-opt ${aiType===t?"on":""}`}
                        onClick={()=>setAiType(aiType===t?"":t)}>
                        {TYPE_CONFIG[t]?.label||t}
                      </button>
                    ))}
                  </div>
                  {generating && (
                    <div className="ai-thinking">
                      <div className="ai-pulse"/>
                      <span className="ai-thinking-txt">Generating 6 original angles for {section.label}…</span>
                    </div>
                  )}
                  {aiError && <div className="ai-error">{aiError}</div>}
                  {aiResults.length>0 && (
                    <div className="ai-results">
                      {aiResults.map((r,i)=>{
                        const cfg = TYPE_CONFIG[r.type]||TYPE_CONFIG.theological;
                        return (
                          <div key={i} className="ai-card" style={{borderColor:`${cfg.color}40`}}>
                            <span className="ai-card-badge" style={{color:cfg.color}}>AI · {cfg.label}</span>
                            <p className="ai-card-title">{r.title}</p>
                            <p className="ai-card-hook">{r.hook}</p>
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              )}
            </div>

          </div>
        </div>
      </div>
    </>
  );
}
