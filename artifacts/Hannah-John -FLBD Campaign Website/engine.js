/* ════════════════════════════════════════════════════════════════
   THE CAMPAIGN ENGINE · composes complete 40-day builds for every
   campaign in the library. Deterministic (seeded per campaign+day):
   the same visitor sees the same words every time. Hand-authored
   content (Faith Worth Passing On, Family Legacy, The Wisdom-Driven
   Life) is never overwritten — the engine only fills what is empty.
   Loads after data.js + intel.js.
   ════════════════════════════════════════════════════════════════ */
(function(){
'use strict';
window.FLengine=true;

/* ---------- deterministic randomness ---------- */
function hash(s){var h=1779033703,i;for(i=0;i<s.length;i++){h=Math.imul(h^s.charCodeAt(i),3432918353);h=h<<13|h>>>19;}return function(){h=Math.imul(h^h>>>16,2246822507);h=Math.imul(h^h>>>13,3266489909);return (h^=h>>>16)>>>0;};}
function rng(seed){var a=hash(seed)();return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function pk(R,arr){return arr[Math.floor(R()*arr.length)];}
function pkn(R,arr,n){var c=arr.slice(),o=[];while(o.length<n&&c.length)o.push(c.splice(Math.floor(R()*c.length),1)[0]);return o;}
function lc(s){return s.charAt(0).toLowerCase()+s.slice(1);}
function slug(s){return s.toLowerCase().replace(/[’']/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');}

/* gerund → infinitive (for turning catalog one-liners into questions) */
var GER={Discovering:'discover',Building:'build',Preserving:'preserve',Understanding:'understand',Redeeming:'redeem',Honoring:'honor',Remembering:'remember',Living:'live',Recognizing:'recognize',Creating:'create',Clarifying:'clarify',Strengthening:'strengthen',Sharing:'share',Helping:'help',Using:'use',Restoring:'restore',Defining:'define',Naming:'name',Aligning:'align',Turning:'turn',Developing:'develop',Moving:'move',Learning:'learn',Confronting:'confront',Releasing:'release',Navigating:'navigate',Replacing:'replace',Combining:'combine',Giving:'give',Showing:'show',Addressing:'address',Redefining:'redefine',Preparing:'prepare',Teaching:'teach',Evaluating:'evaluate',Passing:'pass',Capturing:'capture',Becoming:'become',Making:'make',Ensuring:'ensure',Connecting:'connect',Engaging:'engage',Designing:'design',Redirecting:'redirect',Integrating:'integrate',Planning:'plan',Adjusting:'adjust'};
function infin(desc){var w=desc.split(' ')[0],rest=desc.slice(w.length).replace(/\.$/,'');return (GER[w]||w.toLowerCase().replace(/ing$/,''))+rest;}

/* ---------- the verse bank · KJV, public domain ---------- */
var V=[
/*0*/["Psalm 145:4","One generation shall praise thy works to another, and shall declare thy mighty acts."],
["Deuteronomy 32:7","Remember the days of old, consider the years of many generations: ask thy father, and he will shew thee; thy elders, and they will tell thee."],
["Joel 1:3","Tell ye your children of it, and let your children tell their children, and their children another generation."],
["Proverbs 13:22","A good man leaveth an inheritance to his children's children."],
["Psalm 16:6","The lines are fallen unto me in pleasant places; yea, I have a goodly heritage."],
/*5*/["Psalm 127:1","Except the LORD build the house, they labour in vain that build it."],
["Psalm 127:3","Lo, children are an heritage of the LORD."],
["Joshua 24:15","Choose you this day whom ye will serve; but as for me and my house, we will serve the LORD."],
["Deuteronomy 6:6\u20137","And these words, which I command thee this day, shall be in thine heart: and thou shalt teach them diligently unto thy children."],
["2 Timothy 1:5","When I call to remembrance the unfeigned faith that is in thee, which dwelt first in thy grandmother Lois, and thy mother Eunice."],
/*10*/["Psalm 103:2","Bless the LORD, O my soul, and forget not all his benefits."],
["Psalm 90:12","So teach us to number our days, that we may apply our hearts unto wisdom."],
["Proverbs 4:7","Wisdom is the principal thing; therefore get wisdom: and with all thy getting get understanding."],
["Proverbs 22:6","Train up a child in the way he should go: and when he is old, he will not depart from it."],
["Proverbs 17:6","Children's children are the crown of old men; and the glory of children are their fathers."],
/*15*/["Ephesians 4:32","And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you."],
["Matthew 5:9","Blessed are the peacemakers: for they shall be called the children of God."],
["Psalm 133:1","Behold, how good and how pleasant it is for brethren to dwell together in unity!"],
["Romans 12:10","Be kindly affectioned one to another with brotherly love; in honour preferring one another."],
["Romans 12:18","If it be possible, as much as lieth in you, live peaceably with all men."],
/*20*/["Ecclesiastes 4:9","Two are better than one; because they have a good reward for their labour."],
["Ecclesiastes 4:12","And a threefold cord is not quickly broken."],
["Matthew 19:6","What therefore God hath joined together, let not man put asunder."],
["1 Peter 4:8","And above all things have fervent charity among yourselves: for charity shall cover the multitude of sins."],
["Proverbs 31:28","Her children arise up, and call her blessed; her husband also, and he praiseth her."],
/*25*/["Proverbs 24:3\u20134","Through wisdom is an house builded; and by understanding it is established: and by knowledge shall the chambers be filled with all precious and pleasant riches."],
["Luke 12:48","For unto whomsoever much is given, of him shall be much required."],
["Luke 16:10","He that is faithful in that which is least is faithful also in much."],
["Matthew 6:21","For where your treasure is, there will your heart be also."],
["Matthew 6:33","But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you."],
/*30*/["1 Timothy 6:18","That they do good, that they be rich in good works, ready to distribute, willing to communicate."],
["1 Timothy 6:7","For we brought nothing into this world, and it is certain we can carry nothing out."],
["Proverbs 11:25","The liberal soul shall be made fat: and he that watereth shall be watered also himself."],
["2 Corinthians 9:7","Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver."],
["Acts 20:35","It is more blessed to give than to receive."],
/*35*/["Psalm 24:1","The earth is the LORD's, and the fulness thereof; the world, and they that dwell therein."],
["1 Chronicles 29:14","For all things come of thee, and of thine own have we given thee."],
["Deuteronomy 8:18","But thou shalt remember the LORD thy God: for it is he that giveth thee power to get wealth."],
["Proverbs 22:1","A good name is rather to be chosen than great riches, and loving favour rather than silver and gold."],
["Proverbs 16:3","Commit thy works unto the LORD, and thy thoughts shall be established."],
/*40*/["Colossians 3:23","And whatsoever ye do, do it heartily, as to the Lord, and not unto men."],
["Psalm 37:5","Commit thy way unto the LORD; trust also in him; and he shall bring it to pass."],
["Isaiah 46:4","And even to your old age I am he; and even to hoar hairs will I carry you."],
["Psalm 71:18","Now also when I am old and grayheaded, O God, forsake me not; until I have shewed thy strength unto this generation."],
["Psalm 92:14","They shall still bring forth fruit in old age; they shall be fat and flourishing."],
/*45*/["Proverbs 20:7","The just man walketh in his integrity: his children are blessed after him."],
["Psalm 112:2","His seed shall be mighty upon earth: the generation of the upright shall be blessed."],
["Psalm 100:5","For the LORD is good; his mercy is everlasting; and his truth endureth to all generations."],
["Lamentations 3:22\u201323","His compassions fail not. They are new every morning: great is thy faithfulness."],
["Philippians 1:6","He which hath begun a good work in you will perform it until the day of Jesus Christ."],
/*50*/["Hebrews 13:8","Jesus Christ the same yesterday, and to day, and for ever."],
["James 1:5","If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him."],
["James 1:19","Let every man be swift to hear, slow to speak, slow to wrath."],
["Proverbs 15:1","A soft answer turneth away wrath: but grievous words stir up anger."],
["Proverbs 12:18","There is that speaketh like the piercings of a sword: but the tongue of the wise is health."],
/*55*/["Proverbs 18:21","Death and life are in the power of the tongue: and they that love it shall eat the fruit thereof."],
["Ephesians 4:29","Let no corrupt communication proceed out of your mouth, but that which is good to the use of edifying, that it may minister grace unto the hearers."],
["Ephesians 4:15","But speaking the truth in love, may grow up into him in all things."],
["Numbers 6:24\u201325","The LORD bless thee, and keep thee: the LORD make his face shine upon thee, and be gracious unto thee."],
["Genesis 12:2","And I will bless thee, and make thy name great; and thou shalt be a blessing."],
/*60*/["Proverbs 4:23","Keep thy heart with all diligence; for out of it are the issues of life."],
["Micah 6:8","And what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?"],
["Galatians 6:9","And let us not be weary in well doing: for in due season we shall reap, if we faint not."],
["Galatians 6:2","Bear ye one another's burdens, and so fulfil the law of Christ."],
["Psalm 46:10","Be still, and know that I am God."],
/*65*/["Habakkuk 2:2","Write the vision, and make it plain upon tables, that he may run that readeth it."],
["1 Corinthians 4:2","Moreover it is required in stewards, that a man be found faithful."],
["Matthew 25:21","Well done, thou good and faithful servant: thou hast been faithful over a few things, I will make thee ruler over many things."],
["Psalm 78:6","That the generation to come might know them, even the children which should be born; who should arise and declare them to their children."],
["Isaiah 58:12","And thou shalt be called, The repairer of the breach, The restorer of paths to dwell in."],
/*70*/["Ruth 1:16","Whither thou goest, I will go; and where thou lodgest, I will lodge: thy people shall be my people, and thy God my God."],
["1 Samuel 7:12","Hitherto hath the LORD helped us."],
["Psalm 34:8","O taste and see that the LORD is good: blessed is the man that trusteth in him."],
["Proverbs 27:17","Iron sharpeneth iron; so a man sharpeneth the countenance of his friend."],
["Ecclesiastes 3:1","To every thing there is a season, and a time to every purpose under the heaven."],
/*75*/["2 Timothy 2:2","And the things that thou hast heard of me among many witnesses, the same commit thou to faithful men, who shall be able to teach others also."],
["Psalm 119:105","Thy word is a lamp unto my feet, and a light unto my path."],
["Psalm 25:4","Shew me thy ways, O LORD; teach me thy paths."],
["1 Chronicles 28:9","And thou, Solomon my son, know thou the God of thy father, and serve him with a perfect heart and with a willing mind."],
["1 Chronicles 28:20","Be strong and of good courage, and do it: fear not, nor be dismayed: for the LORD God, even my God, will be with thee."],
/*80*/["Esther 4:14","And who knoweth whether thou art come to the kingdom for such a time as this?"],
["Psalm 102:18","This shall be written for the generation to come: and the people which shall be created shall praise the LORD."],
["Deuteronomy 30:19","I have set before you life and death, blessing and cursing: therefore choose life, that both thou and thy seed may live."],
["Proverbs 14:26","In the fear of the LORD is strong confidence: and his children shall have a place of refuge."],
["Malachi 4:6","And he shall turn the heart of the fathers to the children, and the heart of the children to their fathers."],
/*85*/["Genesis 50:20","But as for you, ye thought evil against me; but God meant it unto good."],
["Romans 5:3\u20134","We glory in tribulations also: knowing that tribulation worketh patience; and patience, experience; and experience, hope."],
["Psalm 30:5","Weeping may endure for a night, but joy cometh in the morning."],
["James 1:17","Every good gift and every perfect gift is from above, and cometh down from the Father of lights."],
["Hebrews 10:24","And let us consider one another to provoke unto love and to good works."],
/*90*/["Philippians 2:3","In lowliness of mind let each esteem other better than themselves."],
["Proverbs 29:18","Where there is no vision, the people perish: but he that keepeth the law, happy is he."],
["Proverbs 16:9","A man's heart deviseth his way: but the LORD directeth his steps."],
["Psalm 37:25","I have been young, and now am old; yet have I not seen the righteous forsaken, nor his seed begging bread."],
["Job 12:12","With the ancient is wisdom; and in length of days understanding."],
/*95*/["Proverbs 13:20","He that walketh with wise men shall be wise: but a companion of fools shall be destroyed."],
["Deuteronomy 11:19","And ye shall teach them your children, speaking of them when thou sittest in thine house, and when thou walkest by the way."],
["Psalm 71:17","O God, thou hast taught me from my youth: and hitherto have I declared thy wondrous works."],
["Proverbs 6:20","My son, keep thy father's commandment, and forsake not the law of thy mother."],
["3 John 1:4","I have no greater joy than to hear that my children walk in truth."],
/*100*/["Isaiah 54:13","And all thy children shall be taught of the LORD; and great shall be the peace of thy children."],
["Genesis 18:19","For I know him, that he will command his children and his household after him, and they shall keep the way of the LORD."],
["Joshua 4:6","That this may be a sign among you, that when your children ask their fathers in time to come, saying, What mean ye by these stones?"],
["Psalm 44:1","We have heard with our ears, O God, our fathers have told us, what work thou didst in their days, in the times of old."],
["Isaiah 38:19","The father to the children shall make known thy truth."],
/*105*/["Jeremiah 6:16","Ask for the old paths, where is the good way, and walk therein, and ye shall find rest for your souls."],
["Proverbs 25:11","A word fitly spoken is like apples of gold in pictures of silver."],
["Proverbs 15:22","Without counsel purposes are disappointed: but in the multitude of counsellors they are established."],
["Proverbs 11:14","Where no counsel is, the people fall: but in the multitude of counsellors there is safety."],
["Psalm 78:72","So he fed them according to the integrity of his heart; and guided them by the skilfulness of his hands."],
/*110*/["Matthew 20:26","Whosoever will be great among you, let him be your minister."],
["1 John 3:18","My little children, let us not love in word, neither in tongue; but in deed and in truth."],
["Matthew 5:16","Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven."],
["2 Corinthians 4:18","For the things which are seen are temporal; but the things which are not seen are eternal."],
["Matthew 6:20","But lay up for yourselves treasures in heaven, where neither moth nor rust doth corrupt."],
/*115*/["Colossians 3:2","Set your affection on things above, not on things on the earth."],
["1 Corinthians 15:58","Your labour is not in vain in the Lord."],
["Proverbs 19:21","There are many devices in a man's heart; nevertheless the counsel of the LORD, that shall stand."],
["Psalm 33:11","The counsel of the LORD standeth for ever, the thoughts of his heart to all generations."],
["Proverbs 3:9","Honour the LORD with thy substance, and with the firstfruits of all thine increase."],
/*120*/["Luke 6:38","Give, and it shall be given unto you; good measure, pressed down, and shaken together, and running over."],
["Proverbs 3:27","Withhold not good from them to whom it is due, when it is in the power of thine hand to do it."],
["Hebrews 13:16","But to do good and to communicate forget not: for with such sacrifices God is well pleased."],
["Ecclesiastes 5:19","Every man also to whom God hath given riches and wealth, and hath given him power to eat thereof; this is the gift of God."],
["Philippians 4:11","For I have learned, in whatsoever state I am, therewith to be content."],
/*125*/["1 Timothy 6:6","But godliness with contentment is great gain."],
["Hebrews 13:5","Be content with such things as ye have: for he hath said, I will never leave thee, nor forsake thee."],
["Proverbs 30:8","Give me neither poverty nor riches; feed me with food convenient for me."],
["Psalm 62:10","If riches increase, set not your heart upon them."],
["Matthew 16:26","For what is a man profited, if he shall gain the whole world, and lose his own soul?"],
/*130*/["Ephesians 6:4","And, ye fathers, provoke not your children to wrath: but bring them up in the nurture and admonition of the Lord."],
["Proverbs 29:17","Correct thy son, and he shall give thee rest; yea, he shall give delight unto thy soul."],
["Lamentations 3:27","It is good for a man that he bear the yoke in his youth."],
["Proverbs 20:11","Even a child is known by his doings, whether his work be pure, and whether it be right."],
["1 Timothy 4:12","Let no man despise thy youth; but be thou an example of the believers, in word, in conversation, in charity, in spirit, in faith, in purity."],
/*135*/["Psalm 144:12","That our sons may be as plants grown up in their youth; that our daughters may be as corner stones, polished after the similitude of a palace."],
["Isaiah 44:3","I will pour my spirit upon thy seed, and my blessing upon thine offspring."],
["Deuteronomy 7:9","The faithful God, which keepeth covenant and mercy with them that love him and keep his commandments to a thousand generations."],
["Genesis 17:7","To be a God unto thee, and to thy seed after thee."],
["Psalm 89:1","I will sing of the mercies of the LORD for ever: with my mouth will I make known thy faithfulness to all generations."],
/*140*/["Psalm 119:90","Thy faithfulness is unto all generations: thou hast established the earth, and it abideth."],
["Isaiah 51:1","Look unto the rock whence ye are hewn, and to the hole of the pit whence ye are digged."],
["Zechariah 4:10","For who hath despised the day of small things?"],
["Isaiah 43:19","Behold, I will do a new thing; now it shall spring forth; shall ye not know it?"],
["2 Corinthians 5:17","Old things are passed away; behold, all things are become new."],
/*145*/["Philippians 3:13","Forgetting those things which are behind, and reaching forth unto those things which are before."],
["Psalm 90:17","And let the beauty of the LORD our God be upon us: and establish thou the work of our hands upon us."],
["Numbers 6:26","The LORD lift up his countenance upon thee, and give thee peace."],
["Psalm 121:8","The LORD shall preserve thy going out and thy coming in from this time forth, and even for evermore."],
["Psalm 23:6","Surely goodness and mercy shall follow me all the days of my life: and I will dwell in the house of the LORD for ever."],
/*150*/["Matthew 7:24","Whosoever heareth these sayings of mine, and doeth them, I will liken him unto a wise man, which built his house upon a rock."],
["Luke 15:20","But when he was yet a great way off, his father saw him, and had compassion, and ran, and fell on his neck, and kissed him."],
["2 Corinthians 1:4","Who comforteth us in all our tribulation, that we may be able to comfort them which are in any trouble."],
["1 Thessalonians 5:11","Wherefore comfort yourselves together, and edify one another, even as also ye do."],
["Isaiah 32:8","But the liberal deviseth liberal things; and by liberal things shall he stand."]
];

/* ---------- domain lexicons ---------- */
var DL={
1:{vs:[1,2,4,0,141,71,103,102,68,81,85,38,104,97],season:"Anniversaries, reunions, and the season after a loss \u2014 whenever the family is already remembering",
 motifs:["the family story","the people who came before","the turning points","the old photographs","the places that shaped us","the name we carry"],
 insights:["A family that cannot tell its story will eventually be told a story about itself \u2014 by culture, by circumstance, or by silence.","The past is not behind a family; it is underneath one, the way roots are underneath a tree.","Most families lose their stories not through tragedy but through busyness \u2014 nobody wrote the evening down."],
 practices:["Pull out one old photograph and tell the story behind it out loud","Write down one family story exactly as you heard it told","Call the oldest living relative and ask one question from today","Name one place that shaped your family and why","Add one date and one sentence to a family timeline","Ask a child to retell a family story in their own words"],
 qs:["that shaped the family you have become","behind the story we tell about ourselves","that the next generation has never heard","we would lose if this generation stayed silent"],
 exT:["The Family Timeline","The Story Archive","The Table of Names"],
 mtitles:["The Photograph That Talks","The Places That Made Us","The Name On The Door","What The Old House Knew","The First Telling","Stones Of Remembrance"]},
2:{vs:[7,8,9,0,2,47,139,137,101,96,100,50,72,89],season:"Advent, Lent, a baptism season \u2014 or any stretch when the family wants faith at the center",
 motifs:["the faith we received","the God who has led us","prayer at the table","the family's spiritual story","belief becoming personal","God's faithfulness"],
 insights:["Faith rarely leaps a generation on its own; it is carried \u2014 by hands, by habits, by stories told at the right moment.","A family altar is not furniture. It is any place where a household regularly tells the truth to God together.","The next generation does not need a perfect spiritual example. It needs an honest one that keeps showing up."],
 practices:["Pray one sentence of thanks out loud before tonight's meal","Tell one story of answered prayer from your family's history","Read tomorrow's Scripture with one other person","Write down one conviction you hope outlives you","Bless one family member by name before bed","Ask someone older where they first met God"],
 qs:["about where God has been in our family's story","that your faith owes to someone else's faithfulness","the next generation should hear you say about God","that prayer has changed in this family"],
 exT:["The Faith Timeline","The Answered-Prayer List","The Household Blessing"],
 mtitles:["Where God Showed Up","The Praying Grandmother","The Table Grace","A Faith With Fingerprints","The God Of Our House","Hitherto"]},
3:{vs:[7,60,111,112,91,38,82,61,45,29,117,118,150,39],season:"New Year, a milestone birthday, or the month before a big family decision",
 motifs:["what we stand for","the family compass","values you can watch","our nonnegotiables","the life we want to build","the legacy we choose"],
 insights:["A value that never inconveniences a family is a slogan, not a value.","Children learn a family's real priorities by watching its calendar and its checkbook, not its wall art.","Vision is simply memory pointed forward: deciding on purpose what the story should say next."],
 practices:["Name one family value and one behavior that proves it","Ask each person at the table: what do we stand for?","Write a one-sentence family mission draft \u2014 rough is fine","Identify one decision this month your values should shape","Choose one word you want guests to feel in your home","Retire one habit that contradicts what you say you value"],
 qs:["that our family should be known for","our decisions actually reveal about our priorities","worth being inconvenient for","the next generation should never have to guess"],
 exT:["The Visible Values Exercise","The Family Compass","One Sentence Of Mission"],
 mtitles:["Values You Can Watch","The Compass In The Drawer","What The Calendar Confesses","The Unwritten Rules","Choosing On Purpose","The Family Creed"]},
4:{vs:[15,16,17,18,19,23,53,52,84,151,63,69,73,89],season:"Before the holidays gather everyone \u2014 or the season after a hard conversation",
 motifs:["the bridge between us","the conversation we avoid","forgiveness with a face","trust rebuilt slowly","hearing one another","peace at the table"],
 insights:["Unspoken things do not stay still in a family; they compound, quietly, like interest.","Reconciliation is rarely one dramatic scene. It is usually a series of small, brave, ordinary moments.","A family strong enough to disagree without dividing has given its children a rare inheritance."],
 practices:["Say one sentence of appreciation to the person hardest to say it to","Ask one question tonight and only listen to the answer","Write \u2014 without sending \u2014 the honest letter, then pray over it","Name one conversation the family keeps postponing","Apologize for one small thing without adding an explanation","Invite one relative back toward the table, gently"],
 qs:["that needs to be said with more grace than volume","we keep circling but never landing","that forgiveness would change in this family","the family is stronger for having survived"],
 exT:["The Bridge List","One Honest Hour","The Repair Kit"],
 mtitles:["The Chair Left Empty","The Long Way Back","What Silence Costs","The Soft Answer","Mending The Net","The First Move"]},
5:{vs:[22,24,20,21,23,18,5,25,150,39,64,74,148,146],season:"An anniversary month, a marriage retreat, or the year the nest empties",
 motifs:["the marriage beneath it all","leading together","a united front","love that keeps its promises","the long yes","two becoming a team"],
 insights:["The marriage at the center of a family is teaching, every day, whether anyone means it to or not.","Couples do not drift into unity; they build it \u2014 decision by decision, apology by apology.","What children remember about their parents' marriage becomes the floor or the ceiling of their own."],
 practices:["Tell your spouse one thing their faithfulness has built","Take one decision you have been making separately and make it together","Retell the story of how you met \u2014 with the kids listening","Name one pressure you will face as a team this month","Write one sentence of vision for your next season together","Thank your spouse for one unseen sacrifice"],
 qs:["your marriage has quietly taught the family","that the two of you should decide together, not separately","that commitment has cost \u2014 and given","the next generation should learn from your covenant"],
 exT:["The Shared-Vision Page","The Team Decision","The Covenant Retelling"],
 mtitles:["The Two-Person Foundation","When The Nest Empties","The Long Yes","One Front, One Table","The Vows At Work","Love, Weathered"]},
6:{vs:[13,130,131,132,133,26,27,134,135,98,45,6,150,29],season:"Back-to-school, a launch year, or the season before a first inheritance conversation",
 motifs:["preparing, not protecting","character before capital","the launch","raising contributors","responsibility in small doses","the baton"],
 insights:["Children rise to responsibility the way muscles rise to weight \u2014 gradually, with resistance, and with someone spotting them.","An inheritance can fund a life; only preparation can build one.","The goal is not children who need the family forever, but children the family will one day gladly follow."],
 practices:["Hand one real responsibility to a young person this week","Tell a child the story of a failure that taught you","Let a young person sit in on one family decision \u2014 and ask their view","Name one thing you are protecting a child from that might be preparing them","Assign one meaningful task and resist rescuing it","Celebrate one act of contribution louder than any achievement"],
 qs:["a young person in this family is ready to carry","that preparation should come before inheritance here","childhood responsibility taught you that comfort never could","the next generation needs to practice while the stakes are small"],
 exT:["The Readiness Map","One Real Responsibility","The Launch Checklist"],
 mtitles:["Training Wheels Off","The Weight That Builds","First Shift","The Allowance And The Lesson","Passing The Baton Slowly","Roots, Then Wings"]},
7:{vs:[11,12,51,94,93,95,75,97,73,105,1,77,106,88],season:"A retirement year, a milestone birthday, or any season with a long car ride in it",
 motifs:["the wisdom transfer","lessons from the journey","what I wish I had known","the stories behind the lessons","questions worth asking","a lifetime of lessons"],
 insights:["Experience is not wisdom until it is reflected on, written down, and handed over.","The most valuable things an elder knows are usually the things nobody has ever asked them.","A lesson without its story is advice; with its story, it becomes unforgettable."],
 practices:["Write down one lesson you paid full price to learn","Ask an elder one question and record the answer","Tell the story behind one piece of advice you always give","Start a running list titled: what I want them to know","Share one mistake and what it taught \u2014 without the varnish","Pass on one skill with your hands, not just your words"],
 qs:["you wish someone had told you at twenty","an elder in this family knows that nobody has asked","that failure taught you more gently than success ever did","worth writing down before it is forgotten"],
 exT:["The Wisdom Letter","Ten Questions For An Elder","The Lessons Ledger"],
 mtitles:["Paid In Full","The Long Way Around","Ask The Ancient Paths","The Notebook","What The Scars Say","Iron On Iron"]},
8:{vs:[35,36,37,27,26,28,66,119,123,124,125,126,127,128],season:"Tax season, an estate-planning year, or the month a windfall arrives",
 motifs:["wealth with purpose","the owner and the steward","money and meaning","enough as a decision","the purpose behind the plan","open books, open hearts"],
 insights:["Money is the most honest member of the family; it always tells the truth about what everyone believes.","Wealth without a why becomes a weight; the same wealth, given a purpose, becomes a tool.","The question is never only what a family owns \u2014 it is what the owning is for."],
 practices:["Finish this sentence together: our resources exist so that\u2026","Tell the story of one lean season and what it taught","Explain to a younger person the why behind one financial decision","Name one possession that owns more of you than it should","Review one line of the budget through the lens of your values","Define, in one sentence, what enough would look like"],
 qs:["your money would say about you if it could talk","that this family believes about ownership and stewardship","a lean season taught that abundance never has","the resources are actually for"],
 exT:["The Purpose Statement","One Honest Budget Line","The Enough Exercise"],
 mtitles:["What The Ledger Believes","The Steward's Morning","Enough, Decided","The Why Behind The Wealth","Open Books","Treasure, Located"]},
9:{vs:[30,32,33,34,120,121,122,154,59,29,62,112,88,63],season:"Year-end giving season, a family foundation cycle, or the month after abundance",
 motifs:["the open hand","giving together","serving side by side","the family that gives","joy in the giving","impact beyond us"],
 insights:["Generosity taught is easily forgotten; generosity practiced together becomes part of a family's name.","The first gift a giving family gives is to itself: children who know that everything is not for them.","A family's giving tells its money where its heart already lives."],
 practices:["Let the youngest person at the table pick this month's gift","Serve two hours somewhere, side by side, this week","Tell the story of a gift someone once gave your family","Write one thank-you note to someone who serves unseen","Set aside one jar, envelope, or line \u2014 and name its purpose","Ask each person: where should our family show up this year?"],
 qs:["that giving together would teach that giving alone cannot","your family's generosity should be known for","a gift once changed in your own story","that open hands make possible"],
 exT:["The Family Giving Plan","Two Hours, Side By Side","The Gratitude Round"],
 mtitles:["The Open Hand","The Youngest Chooses","Side By Side","The Jar On The Counter","Rivers, Not Reservoirs","Where We Show Up"]},
10:{vs:[78,79,3,65,81,82,74,80,42,43,113,114,118,149],season:"A succession year, an estate review, or the decade everyone can see coming",
 motifs:["the handoff","the family meeting","written down and passed on","finishing well","the ethical will","what will outlive us"],
 insights:["A succession that transfers assets but not understanding has moved the money and lost the meaning.","The family meeting is where a legacy stops being one person's intention and becomes everyone's inheritance.","What is written survives; what is assumed evaporates \u2014 usually at the worst possible moment."],
 practices:["Put the next family meeting on the calendar \u2014 tonight","Write the first paragraph of an ethical will","Tell one heir the reason behind one plan","Name the one document that says what you own but not why","List three things that must not die with you","Ask the next generation what they hope will continue"],
 qs:["that should be written down before it is needed","the next generation deserves to understand, not just receive","that finishing well would look like for you","must outlive every account and every deed"],
 exT:["The First Family Meeting","One Page That Outlives You","The Continuity List"],
 mtitles:["The Empty Chair At The Head","Write It Plain","The Meeting That Changed Things","While There Is Time","The Second Signature","What The Will Cannot Say"]}
};

/* ---------- movement lexicons (the six-session frame) ---------- */
var ML=[
{key:"remembering",noun:"the story",act:"remember",focus:"the people, places, blessings, and turning points that shaped this family",
 teach:["Nothing in a family's future makes sense until someone honors its past out loud.","Memory is the first act of stewardship: you cannot pass forward what you have never picked up.","Every family is standing on ground somebody else cleared. This week is for learning their names."],
 outs:["Name the people and moments that shaped the family","Tell at least one family story out loud","Notice where God was present in the family's past","Begin a simple record the family can add to"],
 open:["What is the oldest family story you know by heart?","Who is one person from the family's past you wish you could ask a question?","What object in your home holds the most family history?"],
 mvT:["The Ground We Stand On","Learning The Old Names","Where The Story Started"],
 qs:["What has shaped our family more than we usually admit?","Which family story do you find yourself retelling \u2014 and why that one?","Where can you already see God's hand in the family's past?"],
 steps:["Tell one family story at the table tonight \u2014 the whole thing, unhurried.","Write down three names from the family's past and one sentence about each.","Ask an elder one question about the early years and simply listen."],
 prays:["God, thank You for the hands that carried this family before we knew to be grateful.","Lord, open our memories gently, and help us honor what You were doing all along.","Father, teach us the story You have been writing through this family."]},
{key:"clarifying",noun:"what matters",act:"clarify",focus:"the beliefs, values, and convictions this family wants to stand for",
 teach:["A family that never names its values will still have them \u2014 it just won't get to choose them.","Clarity is a gift to the next generation: they should never have to guess what the family stands for.","Values are proven in collisions \u2014 when two good things compete, what a family chooses reveals what it believes."],
 outs:["Name the values the family wants to be known for","Test each value against actual behavior","Draft language the whole family can own","Choose one value to make more visible this month"],
 open:["If a guest lived with your family for a week, what would they say you value?","What is one conviction you hope your grandchildren still hold?","When has this family chosen the harder right over the easier wrong?"],
 mvT:["Naming What We Believe","Values With Fingerprints","The Compass, Held Up To The Light"],
 qs:["What do we want this family to stand for \u2014 in five words or fewer?","Where do our decisions already match our values, and where is the gap?","What conviction would we defend even if it cost us?"],
 steps:["Write five words this family should stand for \u2014 argue about them lovingly.","Pick one stated value and name one behavior that would prove it this week.","Finish this sentence together: in our family, we believe\u2026"],
 prays:["Lord, give us convictions worth keeping and the courage to live them where the children can see.","God, make our values true in the kitchen, not just true on paper.","Father, help us stand for what You stand for, together."]},
{key:"strengthening",noun:"the relationships",act:"strengthen",focus:"the trust, communication, forgiveness, and belonging this legacy will travel on",
 teach:["A legacy travels on relationships the way current travels on wire; where the connection is broken, nothing gets through.","Grace is not the absence of truth in a family \u2014 it is the way truth learns to knock instead of kick.","The strongest families are not the ones without wounds; they are the ones that learned to tend them."],
 outs:["Name what the family's relationships carry well","Identify one connection that needs care","Practice speaking truth with more love than volume","Take one concrete step toward repair or gratitude"],
 open:["Who in this family made you feel most heard growing up \u2014 and how?","What is one thing this family does well when things get hard?","When did a hard conversation in this family end better than you feared?"],
 mvT:["Tending The Wire","The Grammar Of Grace","Stronger At The Joints"],
 qs:["Which relationship in this family deserves more deliberate care right now?","What do we do when we disagree \u2014 and what do we want to do instead?","Where has forgiveness already made this family stronger?"],
 steps:["Say one specific, out-loud thank-you to a family member today.","Ask one person a real question tonight and let silence do some of the work.","Take the smallest honest step toward one strained connection."],
 prays:["God, soften what has hardened between us, and strengthen what holds.","Lord, give us ears before opinions and grace before verdicts.","Father, make our home a safe place to tell the truth."]},
{key:"preparing",noun:"the generations",act:"prepare",focus:"the character, competence, and calling the next generation will need",
 teach:["The next generation is not prepared by being told about weight; it is prepared by being handed some.","Every skill the family hopes to pass on needs a first, small, survivable rep \u2014 soon.","Preparation is love with a long horizon: it accepts short-term mess for long-term strength."],
 outs:["Assess honestly where the next generation is ready","Identify one capacity to develop on purpose","Hand over one real, right-sized responsibility","Tell one story that turns experience into instruction"],
 open:["What responsibility, given to you young, grew you the most?","Who believed in you before you were ready \u2014 and what did that do?","What does the next generation of this family do better than ours did?"],
 mvT:["Weight, Rightly Sized","The Apprenticeship Of Home","Ready Before Needed"],
 qs:["What is one responsibility a younger person here is ready to carry now?","Where are we protecting when we should be preparing?","What must the next generation understand before it inherits anything?"],
 steps:["Hand one real task to a young person this week \u2014 and do not take it back.","Tell a younger family member the story of one instructive failure.","Invite the next generation's opinion into one real decision."],
 prays:["Lord, grow the ones coming after us \u2014 and grow our willingness to make room.","God, give us the patience to prepare people, not just plans.","Father, may the next generation surpass us, and may we cheer when they do."]},
{key:"aligning",noun:"the resources",act:"align",focus:"the time, wealth, influence, and opportunity that should serve what this family believes",
 teach:["Resources are indifferent servants; they will faithfully fund whatever the family actually worships.","Alignment is the discipline of making the calendar and the accounts tell the same story as the prayers.","A family's influence is a resource too \u2014 and it is the one most often spent by accident."],
 outs:["Connect one resource decision to one stated value","Explain the why behind the what to someone younger","Find one misalignment and adjust it","Practice generosity as a family, not a transaction"],
 open:["What is one purchase or gift your family made that you are still proud of?","If our budget could talk, what would it say we love?","Where has this family's influence quietly done good?"],
 mvT:["The Ledger And The Creed","Making The Money Mean","Influence, On Purpose"],
 qs:["Where do our resources already serve our values \u2014 and where do they wander?","What is the why behind one financial decision the next generation should hear?","What would change if we believed everything here was entrusted, not owned?"],
 steps:["Pick one line of the budget and ask together: what is this for?","Explain the purpose behind one asset or plan to someone younger.","Make one act of giving a family decision this week, not a private one."],
 prays:["God, You own it all \u2014 teach our hands to hold accordingly.","Lord, align what we have with what You love.","Father, make our resources servants of Your purposes in this family."]},
{key:"choosing",noun:"the legacy",act:"choose",focus:"what this family will deliberately preserve, bless, and pass forward",
 teach:["Legacy stops being weather and becomes architecture the day a family starts choosing it on purpose.","What is spoken can be treasured; what is written can be inherited; what is assumed will be lost.","The last movement of legacy is release: preparing something excellent, then handing it over with open hands."],
 outs:["Name what must not be lost with this generation","Put one piece of the legacy in writing","Speak one deliberate blessing out loud","Set the next milestone on the family calendar"],
 open:["If future generations remember three things about this family, what do you hope they are?","What is one thing you received that you are determined to pass on?","What should the family feel free to change after us?"],
 mvT:["From Weather To Architecture","Written, Spoken, Handed Over","The Open-Handed Finish"],
 qs:["What are we choosing, on purpose, to pass forward?","What must be written down before this season ends?","What blessing does each person at this table need to hear?"],
 steps:["Write the first paragraph of a legacy letter \u2014 just the first.","Speak one deliberate blessing to one family member, by name.","Put the next family gathering on the calendar before you sleep."],
 prays:["Lord, help us choose our legacy while the choosing is still ours.","God, give us words worth inheriting and the courage to say them now.","Father, let what we pass forward point every generation to You."]}
];

/* ---------- the seven day-archetypes ---------- */
/* ctx: {c,D,M,R,vref,vtext,w(week idx),n(day),first,last} */
function tie(ctx){var d=ctx.c._eng;return d.tie;}
var ARCH=[
{ /* 0 · open the week's theme */
 t:function(x){return pk(x.R,["The Week Of "+cap(x.M.noun),"Begin With "+cap(x.M.noun),cap(x.M.act)+" First",pk(x.R,x.M.mvT)]);},
 b:function(x){return [
   pk(x.R,x.M.teach)+" This week, "+x.c.title+" turns its attention to "+x.M.focus+".",
   pk(x.R,x.D.insights)+" "+cap(tie(x))+" is where that truth gets personal for your family."
 ];},
 q:function(x){return "As this week begins, what comes to mind first when you think about "+pk(x.R,x.D.motifs)+"?";},
 s:function(x){return pk(x.R,x.M.steps);},
 p:function(x){return pk(x.R,x.M.prays);}},
{ /* 1 · the people angle */
 t:function(x){return pk(x.R,["The People In The "+cap(x.M.noun),"Faces Around "+cap(pk(x.R,x.D.motifs)),"Who Taught Us To "+cap(x.M.act)]);},
 b:function(x){return [
   "Every family learns to "+x.M.act+" from somebody. A parent, a grandparent, a neighbor, a friend of the family whose example lodged deeper than any lecture \u2014 someone showed you what "+pk(x.R,x.D.motifs)+" looks like when it has a face.",
   pk(x.R,x.M.teach)+" Naming those people is not nostalgia; it is inventory. You are counting what you have been given so you can give it deliberately."
 ];},
 q:function(x){return "Who first showed you something true about "+pk(x.R,x.D.motifs)+" \u2014 and what exactly did you see?";},
 s:function(x){return "Name that person out loud at the table tonight, and tell one thing you watched them do.";},
 p:function(x){return "Thank You, God, for the people who carried this before us \u2014 let us carry it as well as they did.";}},
{ /* 2 · the honest difficulty */
 t:function(x){return pk(x.R,["The Hard Part Of "+cap(x.M.noun),"When "+cap(x.M.act)+"ing Costs Something","The Honest Chapter"]);},
 b:function(x){return [
   "Let's tell the truth: "+lc(tie(x))+" is not always comfortable work. Families postpone it for good-sounding reasons \u2014 the timing, the feelings, the fear of opening what might not close neatly.",
   pk(x.R,x.M.teach)+" The families who get there are not the ones who found it easy. They are the ones who decided the discomfort of the conversation was smaller than the cost of the silence."
 ];},
 q:function(x){return "What makes "+lc(tie(x))+" feel difficult in our family \u2014 and what would make it feel possible?";},
 s:function(x){return "Name the difficulty out loud today \u2014 to yourself, on paper, or to one trusted person. Naming it shrinks it.";},
 p:function(x){return "Lord, give us courage for the part we keep postponing, and gentleness for one another when we begin.";}},
{ /* 3 · the Scripture deep-dive */
 t:function(x){return pk(x.R,["Sitting With "+x.vref.split(":")[0],"What The Verse Knows","An Old Word For This House"]);},
 b:function(x){return [
   "Read today's verse once more, slowly. Scripture like this has sat at ten thousand family tables before yours \u2014 through harvests and famines, weddings and funerals, fortunes made and lost \u2014 and it has not worn out yet.",
   "Hold it against "+pk(x.R,x.D.motifs)+" in your own household. "+pk(x.R,x.D.insights)+" The verse is not decoration for that truth; it is the foundation under it."
 ];},
 q:function(x){return "If this verse were framed on the kitchen wall, what would it quietly correct \u2014 or confirm \u2014 about our family?";},
 s:function(x){return "Write today's verse somewhere the family will see it this week \u2014 the fridge, a mirror, the group chat.";},
 p:function(x){return "Father, let this word do its slow, deep work in our house.";}},
{ /* 4 · the practice day */
 t:function(x){return pk(x.R,["Practice, Not Theory","The Small Rep","Hands On "+cap(x.M.noun)]);},
 b:function(x){return [
   cap(x.M.act)+"ing is a skill before it is a sentiment \u2014 and skills are built the unglamorous way, in small repetitions nobody applauds.",
   "So today is a doing day. "+pk(x.R,x.D.insights)+" One small rep, taken today, outweighs a month of good intentions about "+pk(x.R,x.D.motifs)+"."
 ];},
 q:function(x){return "What is the smallest concrete step our family could take on "+pk(x.R,x.D.motifs)+" \u2014 something finishable before bedtime?";},
 s:function(x){return pk(x.R,x.D.practices)+".";},
 p:function(x){return "God, bless the small obediences \u2014 make them add up to something worthy of You.";}},
{ /* 5 · the family conversation day */
 t:function(x){return pk(x.R,[pk(x.R,x.D.mtitles),"The Question That Opens Things","Around The Table, Honestly"]);},
 b:function(x){return [
   "Some days the reading is short on purpose, because the point of today is not the page \u2014 it is the people across from you.",
   "Tonight's question asks about something "+pk(x.R,x.D.qs)+". Ask it plainly. Then do the hard, loving thing: stop talking, and let the answers take as long as they take."
 ];},
 q:function(x){return "What is one thing "+pk(x.R,x.D.qs)+"?";},
 s:function(x){return "Ask tonight's question to every person at the table \u2014 youngest first \u2014 and receive every answer without correcting it.";},
 p:function(x){return "Lord, be the unseen guest at our table tonight; give us honest words and unhurried ears.";}},
{ /* 6 · rest & remember (week close) */
 t:function(x){return pk(x.R,["Rest And Remember","Sabbath For The "+cap(x.M.noun),"The Week, Gathered Up"]);},
 b:function(x){return [
   "A week of "+lc(x.M.noun)+" deserves a quiet ending. Before the next movement begins, gather this one up: what was said this week that surprised you? What was almost said?",
   pk(x.R,x.M.teach)+" Rest is part of the work \u2014 the part where what you planted gets to root."
 ];},
 q:function(x){return "Looking back on this week, what is one moment \u2014 a sentence, a story, a silence \u2014 you want to keep?";},
 s:function(x){return "Write two sentences in the margin of this page: what this week taught, and what it started.";},
 p:function(x){return "Father, seal what You began in us this week, and ready us for what comes next.";}}
];
function cap(s){return s.charAt(0).toUpperCase()+s.slice(1);}

/* ---------- per-campaign engine metadata ---------- */
function engMeta(c){
  if(c._eng) return c._eng;
  var R=rng("meta:"+c.id);
  var D=DL[c.domNo||1], desc=(c._srcDesc||c.desc||"").replace(/\s+A complete campaign[\s\S]*$/,"");
  var inf=infin(desc||("building "+lc(c.title)));
  c._eng={
    R:R, D:D,
    inf:inf,
    tie:inf.charAt(0).toUpperCase()+inf.slice(1),
    dq:"What would it mean for our family to "+inf+"?",
    verses:pkn(rng("vs:"+c.id), D.vs, D.vs.length)
  };
  return c._eng;
}

/* ---------- generators ---------- */
function genWeeks(c){
  var e=engMeta(c), counts=[7,7,7,7,6,6], acc=0, used={};
  var weeks=ML.map(function(M,i){
    var R=rng("wk:"+c.id+":"+i);
    var slots=(counts[i]===7)?[0,1,2,3,4,5,6]:[0,1,2,3,4,6];
    var days=slots.map(function(sl,j){
      var n=acc+j+1;
      var vi=e.verses[(acc+j)%e.verses.length];
      var v=V[vi], x={c:c,D:e.D,M:M,R:rng("d:"+c.id+":"+n),vref:v[0],vtext:v[1],w:i,n:n};
      var t=ARCH[sl].t(x); var guard=0;
      while(used[t]&&guard++<4){t=ARCH[sl].t(x);}
      used[t]=1;
      return [t, v[0], "", sl, vi];
    });
    acc+=days.length;
    return {t:pk(R,M.mvT), d:cap(M.act)+" "+M.focus+".", days:days};
  });
  return weeks;
}
function genReading(c,n){
  var e=engMeta(c), acc=0, w=null, j=0, wi=0;
  for(var i=0;i<c.weeks.length;i++){
    if(n<=acc+c.weeks[i].days.length){w=c.weeks[i];wi=i;j=n-acc-1;break;}
    acc+=c.weeks[i].days.length;
  }
  if(!w) return null;
  var d=w.days[j], M=ML[Math.min(wi,ML.length-1)];
  var sl=(typeof d[3]==="number")?d[3]:(j%7);
  var vi=(typeof d[4]==="number")?d[4]:e.verses[(n-1)%e.verses.length];
  var v=V[vi]||[d[1],""];
  var x={c:c,D:e.D,M:M,R:rng("d:"+c.id+":"+n),vref:d[1]||v[0],vtext:v[1],w:wi,n:n};
  var A=ARCH[sl];
  return {
    title:d[0], verse:x.vtext||v[1], verseLabel:(d[1]||v[0])+" \u00B7 KJV",
    body:A.b(x), table:A.q(x), step:A.s(x), pray:A.p(x)
  };
}
function genSessions(c){
  var e=engMeta(c);
  return ML.map(function(M,i){
    var R=rng("s:"+c.id+":"+i), F=FLI.frame6[i];
    var vi=e.verses[i%e.verses.length];
    return {
      t:F.t, scr:V[vi][0],
      sq:F.q+" "+pk(R,M.teach),
      outcomes:pkn(R,M.outs,3).concat([cap(e.inf).split(" ").slice(0,3).join(" ")==="" ? F.d : "Connect this movement to "+lc(e.tie)]),
      opening:pk(R,M.open),
      moves:[
        {t:pk(R,M.mvT), p:pk(R,M.teach), list:pkn(R,e.D.motifs,4).map(cap)},
        {t:cap(M.act)+"ing In This Campaign", p:pk(R,e.D.insights)+" In "+c.title+", this movement asks the family to "+lc(F.d).replace(/^families /,"")}
      ],
      qs:[F.q, pk(R,M.qs), "What is one thing "+pk(R,e.D.qs)+"?", pk(R,M.qs.filter(function(q){return true;})), e.dq].filter(function(q,k,a){return a.indexOf(q)===k;}).slice(0,5),
      exercise:{t:pk(R,e.D.exT), p:"Around the table or on one shared page:", list:pkn(R,e.D.practices,4)},
      step:pk(R,M.steps)
    };
  });
}
function ensureFull(c){
  if(c.id==="faith-worth-passing-on") { c.open=c.days||21; return c; }
  c._srcDesc=c._srcDesc||c.big||c.desc||"";
  if(!c.weeks) c.weeks=genWeeks(c);
  c.days=c.weeks.reduce(function(a,w){return a+w.days.length;},0);
  if(!c.sessions) c.sessions=genSessions(c);
  c.open=c.days;
  delete c.status;
  var e=engMeta(c);
  if(!c.sub) c.sub=c._srcDesc.replace(/\.$/,"");
  if(!c.kicker) c.kicker="A "+c.days+"-Day Family Legacy Campaign";
  if(!c.quote) c.quote=e.dq;
  if(!c.big||c.big===c._srcDesc) c.big=c._srcDesc;
  c.desc="Over "+(c.days===40?"forty":c.days)+" mornings, this campaign walks a family through "+lc(e.inf)+" \u2014 one short reading, one honest question at the table, and one small step at a time. "+pk(rng("dd:"+c.id),e.D.insights)+" Built on the standard six-session frame, with a family edition and a facilitated edition for advisors and churches.";
  if(!c.scrRef){var v0=V[e.verses[0]]; c.scrRef=v0[0]; c.scrKJV=v0[1]; c.kjv=true;}
  if(!c.audience) c.audience="Households, couples, small groups of families \u2014 with or without a facilitator";
  if(!c.season) c.season=e.D.season;
  return c;
}

/* hue synthesis per domain, varied per campaign */
var DHUE={1:[8,52],2:[152,38],3:[42,58],4:[318,24],5:[22,42],6:[208,34],7:[82,32],8:[164,40],9:[16,48],10:[36,44]};
function hslhex(h,s,l){s/=100;l/=100;var a=s*Math.min(l,1-l);var f=function(k){var x=(k+h/30)%12;var c=l-a*Math.max(-1,Math.min(x-3,Math.min(9-x,1)));return Math.round(255*c).toString(16).padStart(2,"0");};return "#"+f(0)+f(8)+f(4);}
function genHue(c){
  var R=rng("hue:"+c.id), b=DHUE[c.domNo]||[152,30];
  var h=(b[0]+Math.floor(R()*24)-12+360)%360, s=b[1]+Math.floor(R()*10)-4;
  return [hslhex(h,s,34+Math.floor(R()*8)), hslhex(h,Math.min(60,s+6),15+Math.floor(R()*5))];
}
var DAREAS={1:["family"],2:["personal","family"],3:["personal","family"],4:["family"],5:["family","personal"],6:["family","financial"],7:["personal","family"],8:["financial","charitable"],9:["charitable","family"],10:["business","financial"]};

/* ---------- registry: every campaign in the library, complete ---------- */
if(window.FLC && window.FLI){
  FLI.catalog=[];
  FLI.domains.forEach(function(d,di){
    d.c.forEach(function(row,j){
      var id=slug(row[0]), n=di*10+j+1;
      var c=FLget(id);
      if(!c){
        c={id:id, title:row[0], _srcDesc:row[1], big:row[1],
           areas:DAREAS[di+1].slice(), hue:genHue({id:id,domNo:di+1}),
           domNo:di+1, domName:d.n};
        FLC.campaigns.push(c);
      } else { c._srcDesc=c._srcDesc||row[1]; c.domNo=c.domNo||di+1; c.domName=c.domName||d.n; }
      ensureFull(c);
      FLI.catalog.push({n:n,id:id,title:row[0],desc:row[1],dom:di+1});
    });
  });
  /* the two original demonstration builds: open everything, fill gaps */
  ["family-legacy","wisdom-driven-life"].forEach(function(id){
    var c=FLget(id); if(!c) return;
    c.domNo=c.domNo||3; c.domName=c.domName||FLI.domains[2].n; c._srcDesc=c._srcDesc||c.big||c.sub||"";
    if(!c.sessions) c.sessions=genSessions(c);
    c.days=c.weeks?c.weeks.reduce(function(a,w){return a+w.days.length;},0):40;
    c.open=c.days;
  });
  var fw=FLget("faith-worth-passing-on"); if(fw){ fw.ribbon="The Flagship \u00B7 21 Days"; }

  /* reading resolver: authored first, engine second */
  window.FLreading=function(c,n){
    FLC.readings=FLC.readings||{};
    var bank=FLC.readings[c.id];
    if(bank && bank[n]) return bank[n];
    var r=genReading(c,n);
    if(r){ if(!bank){bank=FLC.readings[c.id]={};} bank[n]=r; }
    return r;
  };
  window.FLrelated=function(c,count){
    var sibs=FLI.catalog.filter(function(k){return k.dom===c.domNo && k.id!==c.id;});
    var R=rng("rel:"+c.id);
    return pkn(R,sibs,count||6).map(function(k){return FLget(k.id);});
  };
  window.FLdomShort=["Identity & Story","Faith & Heritage","Values & Vision","Relationships","Marriage & Leadership","Parenting & Next Gen","Wisdom & Mentoring","Wealth & Stewardship","Generosity & Impact","Succession & Governance"];
}
})();
