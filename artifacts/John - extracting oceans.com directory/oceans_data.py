# -*- coding: utf-8 -*-
# OCEANS.com platform census data
# Compiled from the live public site, August 17, 2026 (oceans.com)
# Units: full-length messages ("Sermons" in platform language, includes podcast
# episodes), plus "Shorts" (sub-3-minute clips) counted separately.

PLATFORM = {
    "name": "OCEANS",
    "url": "oceans.com",
    "tagline": "Messages for whatever you're facing",
    "search_promise": ("Tell OCEANS what you're going through - in your own words. "
                       "We search inside every message: the full teaching, its themes, "
                       "and the moments of life it speaks to. Not just titles."),
    "felt_needs": ["Grief & loss", "Anxiety", "Marriage", "Faith & doubt", "Purpose", "Parenting"],
    "nav": ["Home", "Shorts", "Series", "Contributors", "Podcasts", "Join OCEANS (speaker intake)", "Sign in"],
}

# type: C = church, M = ministry / voice, S = podcast / show
# blurb: exactly as stated on the platform contributor directory (trimmed); "" = no profile text posted
CONTRIBUTORS = [
    (61, "2|42 Community Church", "C", "Non-denominational church with multiple locations, dedicated to helping people take next steps with God."),
    (52, "3Circle Church", "C", ""),
    (42, "Abundant Life", "C", "On a mission to see lives changed by Jesus by being living proof of a loving God to a watching world."),
    (58, "Authentic Church", "C", "Led by Pastor Bobby Chandler; exists so people will have an authentic encounter with God, be set free, and grow in Christ."),
    (39, "Bible Caddie", "S", "Weekly space where Webb Simpson, Ben Crane, and William Kane talk about faith in Jesus, the Bible, and the real pressures of life."),
    (51, "Biltmore Church", "C", "Exists to glorify God by making disciples of Jesus who Reach Up, Reach In, and Reach Out."),
    (67, "Blue Oaks Church", "C", "Non-denominational Christian church located in Pleasanton, CA."),
    (56, "Calvary Chapel Fremont", "C", "Calvary Chapel Fremont Church, since 1998."),
    (30, "Catalyst Church", "C", "Gospel-centered, college-focused, missional, contemporary church in Newport News, VA."),
    (13, "Christians in Sport", "M", "A movement of competitors, coaches and officials; exists to reach the world of sport for Jesus."),
    (3, "Church of the City", "C", "To see the fame and deeds of God renewed and known in our time."),
    (2, "Clayton King Ministries", "M", "Exists to preach the gospel, make disciples, support youth and college leaders, and build community among believers."),
    (74, "Colby Maier", "S", "Channel featuring content that connects viewers with various topics and insights."),
    (76, "Community Bible Church", "C", "Aims to empower individuals to embody the Good News of Jesus in all aspects of life."),
    (36, "Crosspoint City Church", "C", "We exist to relentlessly pursue those far from God to help them know and follow Jesus."),
    (69, "Crossroads Christian Church", "C", "Located in Gray, TN; focused on making following Jesus a way of life through community and mission."),
    (68, "Crossroads Community Church", "C", "Dedicated to helping individuals know Jesus, grow to be like Him, and serve Him."),
    (66, "Desert Vineyard Church", "C", "A community focused on helping individuals find God and understand their purpose."),
    (28, "Eastgate Church", "C", "Eastgate Church in Rocky Mount and Wilson, North Carolina."),
    (55, "Fierce Church", "C", "Online and in-person services Sundays at 10am."),
    (48, "First Baptist Woodstock", "C", "Our vision is to find and follow Jesus from Woodstock to the world."),
    (62, "First McKinney", "C", ""),
    (26, "Gateway Church", "C", ""),
    (79, "Happy and Healthy Podcast", "S", ""),
    (34, "Hope Church LV", "C", ""),
    (31, "Hope Church NC", "C", "Nondenominational church in Burlington, NC, with a vision to do whatever it takes for all people to follow and grow."),
    (59, "Hope Community Church", "C", "Exists to help people far from God find hope in God through giving hope, creating community, and being the church."),
    (63, "HopeCity NC", "C", "Dedicated to partnering with the Presence of God to make a positive impact on everyone for the Kingdom."),
    (5, "Joby Martin", "M", "Founder and lead pastor of The Church of Eleven22 in Jacksonville, Florida."),
    (38, "Joe Gibbs Game Plan for Life", "S", "Game Plan for Life - gameplanforlife.com."),
    (80, "Justin Roethlingshoefer", "S", ""),
    (10, "King's Church London", "C", "A dynamic and diverse Christian church with a vision to serve and reach the communities of London."),
    (11, "Mariners Church", "C", "A thriving community; services Saturday and Sunday plus weekday mornings (Irvine, CA)."),
    (4, "McLean Bible Church", "C", "David Platt serves as Lead Pastor of McLean Bible Church in Washington, D.C., and is the founder of Radical."),
    (45, "Mercy Church", "C", "Trusting God to bring a gospel awakening to Charlotte that is carried to the ends of the earth."),
    (33, "Mercy Hill Church", "C", "Church community in Greensboro, NC."),
    (70, "Mt. Pisgah Baptist Church", "C", ""),
    (78, "Netcast Church", "C", ""),
    (71, "Newsong Church", "C", ""),
    (9, "NewSpring Church", "C", "Passionate about seeing everyone, everywhere in an everyday relationship with Jesus."),
    (47, "Northpointe Las Vegas", "C", "Interdenominational congregation of Jesus followers dedicated to authentic Christianity, serving Las Vegas."),
    (64, "O'Fallon Christian Church", "C", ""),
    (57, "Outreach Church", "C", ""),
    (27, "Port City Church", "C", "We exist to help others encounter Jesus and follow His way."),
    (37, "Proclamation Church", "C", "Church community in Nashville, TN, dedicated to engaging all people and growing as the family of God."),
    (32, "Redeemer Church", "C", "A gospel-centered church in Rocky Mount, NC. Sundays 9:00 and 10:45."),
    (29, "Redemption Church", "C", "We exist to lead a restless culture to the redeeming Savior in Roanoke, VA."),
    (49, "Revolution Church", "C", "Our mission is to love Jesus and grow people (Matthew 22:37-40)."),
    (50, "Risen Church", "C", "A gospel-centered church in Virginia Beach, Virginia."),
    (72, "Royal City Church", "C", "Located in Inglewood, California; services every Sunday at 9am and 11am."),
    (77, "Ryan Miller", "S", "Host of The Jesus People Podcast; dedicated to sharing good news with others."),
    (8, "Southeast Christian Church", "C", "Unleashing the full force of the church to love people - one at a time - is what we're all about."),
    (54, "Sovereign City Church", "C", "A new church launching 02.22.26 in Henderson, NV. His Kingdom. This City."),
    (65, "Sunrise Church", "C", "Located in Chapel Hill, North Carolina, serving the local community."),
    (43, "The Bridge Church", "C", ""),
    (73, "The Impossible Life", "S", "Dedicated to empowering men to embrace their true purpose and rise above mediocrity."),
    (40, "The Kirk Cameron Show", "S", "Kirk Cameron's interview and teaching show."),
    (1, "The Summit Church", "C", "Following the Holy Spirit, we exist to create a movement of disciple-making disciples in RDU and around the world. Led by J.D. Greear."),
    (12, "Tim Tebow", "M", "The Tim Tebow Foundation exists to bring Faith, Hope and Love to those needing a brighter day in their darkest hour of need."),
    (46, "Touching Lives with Dr. James Merritt", "S", "International broadcast ministry of Dr. James Merritt, Senior Pastor of Cross Pointe Church, Duluth, Georgia."),
    (44, "Two Cities Church", "C", "Weekly messages and other content from Two Cities Church."),
    (60, "Tyler Gaulden", "S", ""),
    (41, "Undaunted.Life: A Man's Podcast", "S", "Equipping men to be spiritually, mentally, and physically resilient in the face of life's obstacles."),
    (75, "Walk Worthy Ministry", "S", "The Walk Worthy Podcast, hosted by speaker and pastor Joshua Broome; weekly discussions on biblical truth."),
]

# Captured contributor library counts (as displayed on each contributor page header)
CAPTURED_COUNTS = [
    ("The Summit Church", 137, 61, "full title index in Exhibit A"),
    ("NewSpring Church", 101, 6, "count captured from contributor page"),
    ("McLean Bible Church", 80, 62, "full title index in Exhibit B"),
]

# ---------------------------------------------------------------------------
# EXHIBIT A - The Summit Church (contributor 1): all 137 full-length messages
# Format: duration~title  (blank duration = not displayed on platform)
SUMMIT_SERMONS = """38:38~The Good Life ROI | John Muller
50:46~The Bottom Line to Everything | Bryan Loritts
5:05~What If Your Pain Is Your Mission Field? | Philippians 1 | Bryan Loritts
46:57~The Good Death | Curtis Andrusko
5:35~Even THIS Can Be Used for Good | J.D. Greear
40:33~Holy Spirit: Let Me Upgrade You | Curtis Andrusko
47:09~The Greatest Threat to Your Calling | J.D. Greear
24:11~Being a Member of a Local Church Family | S3E3
41:41~Desert Obedience | John Muller
42:44~Living as Family among Multigenerational Adults | S3E7
34:26~Living with the Local Church as Family | S3E2
47:18~The Devil's Defensive Line of Discouragement | J.D. Greear
30:37~A Conversation about Being Family with Kids and Students | S3E6
51:05~Everybody's Got a Job | J.D. Greear
42:36~Watch Out! | Joby Martin
31:28~A Conversation about Church Membership | S3E4
20:19~A Family from Every Nation, Tribe, and Tongue | S3E8
43:38~Holy Discontent, Part 2 | J.D. Greear
32:59~Living as a Multiethnic Church Family | S3E9
41:07~God, I'm Saying YES! - Guest Pastor Spence Shelton
28:54~Married and Single People Living as Family | S3E10
44:43~Who Is Jesus? How the Resurrected Christ Sets Us Free | Bryan Loritts
44:17~GLP-0 | J.D. Greear
5:57~What If Your Pain Is Actually God's Grace? | Spence Shelton
48:13~The Water Gate Revival | J.D. Greear
27:30~From Generation to Generation | S3E5
48:09~Confession and Renewal | J.D. Greear
43:01~Single and Married People Living as Family | S3E11
45:55~Fade to Black | J.D. Greear
20:42~What It Means to Be Brothers and Sisters in Christ | S3E12
28:19~How to Live as Brothers and Sisters in Christ | S3E13
47:35~The Pain You Didn't See Coming | Bryan Loritts
47:00~Slowly But Surely | Curtis Andrusko
50:43~Holy Discontent, Part 1 | J.D. Greear
45:56~Looking for Help in All the Wrong Places | J.D. Greear
45:18~Embracing Ambition | Curtis Andrusko
44:52~Are You Serious...? | J.D. Greear
42:47~Fundamentals, Not Hype | J.D. Greear
42:57~Glitch or Feature? | J.D. Greear
20:56~God's Gospel Family | S3E1
3:09~Obedience Doesn't Earn God's Love - It Responds to It
47:26~I Am Not Throwing Away My Shot | Curtis Andrusko
43:23~Worth the WAIT | Pastor Curtis Andrusko
7:17~How We Spend Our Days Is How We'll Spend Our Lives
6:27~Exodus: The Melody of Salvation
36:05~Changes | Pastor John Muller
7:33~The Grace of Jesus is Greater Than The Sin in You
48:42~When God Comes Near | Bryan Loritts
4:57~Wait On God and Avoid These 3 Ditches
5:16~When God Confronts Our Idols, He Renders Them Powerless
17:36~Sunday Worship Service | Sunday Morning Live - February 9th 2025
46:37~God, Yes, but Why Jesus? | J.D. Greear
50:54~Udderly Wrong: A Moo-ving Tale of Spiritual Rebellion | J.D. Greear
3:47~From the Red Sea to the Cross: Trusting God's Unseen Presence
4:32~How Jesus Fulfilled The Melody of Salvation
46:22~The Sabbath: Remember and Rest | Curtis Andrusko
33:39~Freedom | Wes Smith
5:45~The Manna Midterm: Trusting God's Daily Provision
44:39~Your God Is Too Small | Pastor Bryan Loritts
47:01~Let's Try This Again | Bryan Loritts
40:32~The Tabernacle: Space for God | J.D. Greear
5:38~Barabbas: The Guilty Set Free
4:04~Sabbath: Our Expression of Trust
15:52~What Is The Gospel | S1E1
4:36~God Isn't Asking to Be First - He's Asking to Be the Only
15:21~Who Is Jesus | S1E3
31:16~What Does It Mean to Live a Jesus Centered Life | S1E4
43:43~The Intoxicated Christian | Bryan Loritts
4:18~You Don't Need More of God - He Needs More of You
24:43~What Does It Mean to Prioritize the Gospel Above All | S1E2
4:49~How to Know You're Really Filled with the Spirit
43:14~The Manifold, Robust Worship of the Lamb | Mitchel Lee
19:24~The Gospel and the FIVE Identities of a Disciple | S1E5
30:47~Growing in the FIVE Identities of a Disciple | S1E6
3:32~True Faith Cannot Stay Silent
31:52~Not So Fast: The Last Thing to Do in 2025
45:58~The Enemy Within: Pergamum & Thyatira | Curtis Andrusko
22:10~Next Steps to Growing as Whole Disciple | S1E7
45:54~The View From Heaven | Curtis Andrusko
37:25~Walking in Truth | Pastor John Muller
3:57~You're Not the Point of the Story (But That's Really Good News)
50:09~Impossible. Difficult. Done. | J.D. Greear
38:41~Stop Playing Around | John Muller
4:13~Perfect Justice, Perfect Love | Revelation Series
5:10~Overcoming the Enemy's Lies | Revelation Series
54:38~The Familiar Stranger | Tyler Staton
4:14~Jesus: Savior or Judge? Revelation 19
48:22~The Summit's Mission and Message | J.D. Greear
24:36~What is the Bible? What Happens When We Read It? | S2E3
26:40~Worshiping God Above All Else (with Jonathan Welch & Joseph Scarfone) | S2E2
21:04~Our Worship and the Gospel | S2E1
33:14~Bible Reading in Real Life - with Eric Stortz & Michal Rudolph | S2E4
~Heaven Will Not Be Boring
~Prayer, the Gospel, and How to Do It
~How to Be a Godly Sinner
~Prayer in Real Life - A Conversation with Chris Gaynor
~You Are Covered by the Blood of Jesus
~What is God's Purpose for your Work?
~Hypocrisy: How to Have Wrong Righteousness
~The Church's Worship Through Song
~You Are Enough
~Why God Lets You Walk Through Pain
~Why We Can't Wait to Share Jesus
~Worship Through Baptism and Communion (Part Two)
~Worship Through Baptism and Communion (Part One)
~Church at the Dome
47:07~Prove Yourself | Curtis Andrusko
3:44~Fantasy Stokes Testimony
3:35~Season 2 Finale
38:13~The Wonder of Jesus | John Muller
47:45~The Love of Christ | Bryan Loritts
1:00:12~The Summit Church | Worship at Home 2025
46:42~Melody | Pastor J.D. Greear
47:56~Meeting the I AM | Pastor J.D. Greear
46:34~Compassion as the Center of Our Calling | J.D. Greear
48:19~When God Is In It And It Still Fails | J.D. Greear
47:45~Red Sea Faith | J.D. Greear
47:12~Wilderness U with J.D. Greear
45:53~Church 101 | J.D. Greear
45:32~Consider the Cross: Eternity's Dividing Line | J.D. Greear
46:08~Why the Big 10 | J.D. Greear
49:18~To the Churches in Ephesus and Smyrna: Beware Small Compromises | J.D. Greear
47:21~Wake Up, Get Ready, and Stop Being Lame | J.D. Greear
45:39~Searching for a Hero | J.D. Greear
44:23~Sweet and Bitter | J.D. Greear
46:21~Beast Games | J.D. Greear
49:36~A Tale of Two Cities | J.D. Greear
47:30~A Party, a Battle, a Kingdom, and a Judgment | J.D. Greear
44:14~The Great Beginning | J.D. Greear
45:49~The Mission of Renewal: 5 Practices | J.D. Greear
55:15~We're All Nervous When We Talk About Money | J.D. Greear
1:54:59~Wise Men Still Seek Him | Pastor J.D. Greear (Christmas service)
51:07~Turn the Cat Around | J.D. Greear
50:08~Plastic Sacks and Gucci Bags | J.D. Greear
45:27~Unveiled | J.D. Greear
49:28~The Why of Your Pain | J.D. Greear
41:50~Wise Men Still Seek Him | J.D. Greear"""

SUMMIT_SHORTS_COUNT = 61
SUMMIT_SHORTS_SAMPLE = [
    "Jesus Isn't Deceived - But He Is Ready to Restore (2:56)",
    "Where Does Your Life Fit in God's Story? (0:46)",
    "The Power You're Looking For Isn't in You (1:44)",
    "Hope isn't just about what you're waiting for - it's about who you're waiting with (0:46)",
    "Generosity is not something God wants from you; it's something he wants for you (1:43)",
    "Condemnation says 'Hide it.' Conviction says 'Bring it to light and find freedom.' (1:17)",
    "The Bill Was Paid (1:52)",
    "You Were Never Meant to Carry That Weight (2:23)",
]

# ---------------------------------------------------------------------------
# EXHIBIT B - McLean Bible Church (contributor 4): all 80 full-length messages
MCLEAN_SERMONS = """50:12~Graduation Sunday 2026: Who Are You Becoming? (Romans 12:1-2) | Mike Kelsey
39:21~The Road of Repentance (1 Samuel 7:3-17) | Kingmaker | Eric Saunders
49:38~Healing Over Hiding (Luke 8:43-48) | Seen | Mike Kelsey
55:45~Impact 20 Million (Matthew 28:16-20) | Vision 2030 | David Platt
46:05~Disciple 10K (Ephesians 4:11-16) | Vision 2030 | Mike Kelsey
39:36~Seen In Suffering, Seen In Service (Mark 9:14-29) | Seen | David Platt
43:04~He Loves You, and Not Just You (John 4:1-42) | Seen | David Platt
49:44~Impossible People (Luke 19:1-10) | Seen | Mike Kelsey
38:25~Baptism: Celebration Of Grace (Acts 2:36-42) | David Platt
48:40~What Kind Of God Do You Believe In? (1 Samuel 2:1-11) | Kingmaker | David Platt
52:04~God, What Are You Doing (1 Samuel 1:1-28) | Kingmaker | Mike Kelsey
46:55~Are You Available God? (1 Samuel 3:1-4:1) | Kingmaker | Mike Kelsey
43:36~When Leaders Fall (1 Samuel 2:11-36) | Kingmaker | David Platt
52:25~Religion God Rejects (1 Samuel 4:2-7:2) | Kingmaker | Mike Kelsey
34:53~The King Who Rose to Serve You (John 21) | Easter | David Platt
55:20~Reach One (Luke 15:1-7) | Vision 2030 | Mike Kelsey
49:10~Looking Back, Looking Forward (Psalm 33) | Nate Reed
48:38~Don't Settle for Bare Minimum Spirituality (Ephesians 3:14-17) | Mike Kelsey
49:21~Start 5 New Congregations (Acts 1-14) | Vision 2030 | David Platt
48:43~Prayer That Amazes Jesus (Ephesians 3:20-21) | David Platt
49:21~Let Down Your Nets (Luke 5:1-11) | Vision 2030 | Mike Kelsey
37:32~Grasping The Limitless Love Of God (Ephesians 3:14-19) | Eric Saunders
5:15~When Our World Changed (story)
3:31~Week Three Encouragement | 21 Days of Prayer
46:53~The Story Of Scripture (Genesis 1-2) | The Word Of God | Mike Kelsey
52:46~Is The Bible Reliable? (2 Timothy 3:16) | The Word Of God | David Platt
53:15~Authority Not Advice | The Word Of God | Mike Kelsey
49:38~The Goodness Of God In Scripture (Psalm 23) | The Word Of God | David Platt
48:16~Praying For Other People (Colossians 1:1-14) | Image Of The Invisible | Mike Kelsey
56:09~Christ In You, The Hope Of Glory (Colossians 1:24-2:5) | Image Of The Invisible | David Platt
42:31~Jesus Over Everything Else (Colossians 2:6-23) | Image Of The Invisible | Mike Kelsey
36:40~Captured By The Image Of The Invisible (Colossians 1:15) | Image Of The Invisible | Eric Saunders
48:11~Becoming The New You (Colossians 3:1-4) | Image Of The Invisible | Mike Kelsey
42:39~Life In Response To The Beauty Of Christ (Colossians 3:5-11) | Image Of The Invisible | Eric Saunders
53:09~Relearning Relationships (Colossians 3:12-17) | Image Of The Invisible | Mike Kelsey
51:51~The Difference Jesus Makes In Marriage (Colossians 3:18-19) | Image Of The Invisible | David Platt
57:40~The Difference Jesus Makes In Children And Parents (Colossians 3:20-21) | David Platt
51:41~You Have A New Boss (Colossians 3:22-4:1) | Image Of The Invisible | Mike Kelsey
38:24~The Resurrection And Real Life (John 11:17-44) | Easter 2025 | Mike Kelsey
48:40~Prayer: Our Wartime Walkie-Talkie (Colossians 4:2-18) | Image Of The Invisible | David Platt
47:56~Everything You Need To Know About Christians (Titus 3:3-8) | Walk With Jesus | Mike Kelsey
48:31~An Invitation To Memorize God's Word... And Live (Psalm 119) | Walk With Jesus | David Platt
39:20~The God Who Is Worthy Of Our Waiting (Psalm 130) | Walk With Jesus | David Platt
53:34~I Am With You (Matthew 28:18-20) | Walk With Jesus | Mike Kelsey
33:31~Rest For Your Restless Soul (Psalm 131) | Walk With Jesus | David Platt
36:17~A Prayer In Times Of Sorrow (Psalm 13) | Walk With Jesus | Nate Reed
54:23~Helping Each Other Hold Onto Hope (Hebrews 10:23) | In This Together | David Platt
56:40~In A Cave With God (1 Samuel 22:1-2) | Walk With Jesus | Mike Kelsey
41:19~The Pathway To See God's Glory (John 15:7-8) | Walk With Jesus | Nirup Alphonse
39:52~A Confident Community (Hebrews 10:19-22) | In This Together | Eric Saunders
54:35~A Call To Community (Hebrews 10:24-25) | In This Together | Mike Kelsey
46:05~The Belt Of Truth (Ephesians 6:14) | How To Fight In The Dark | David Platt
45:25~Six Foundations for Spiritual Battle (Ephesians 6:10-13) | How To Fight In The Dark | David Platt
52:01~The Breastplate of Righteousness (Ephesians 6:14) | How To Fight In The Dark | Mike Kelsey
51:26~The Shield of Faith (Ephesians 6:16) | How To Fight In The Dark | Mike Kelsey
52:32~The Gospel of Peace (Ephesians 6:15) | How To Fight In The Dark | Mike Kelsey
46:54~The Sword Of The Spirit (Ephesians 6:17) | How To Fight In The Dark | David Platt
54:50~How to (Really) Pray in the Dark (Ephesians 6:18-20) | How To Fight In The Dark | Nate Reed
39:48~Helmet Of Salvation (Ephesians 6:10-17) | How To Fight In The Dark | Eric Saunders
49:54~God's Good Design For Humanity, Part 1 (Genesis 1-2) | David Platt
51:11~God's Good Design in Creation, Part 1 (Genesis 1:1-25) | Mike Kelsey
50:34~God's Good Design in Creation, Part 2 (Genesis 1-2) | David Platt
55:45~God's Good Design For Humanity, Part 2 (Genesis 1:26) | Mike Kelsey
54:44~God's Good Design for Gender and Sexuality, Part 1 (Genesis 1:27) | Mike Kelsey
46:58~God's Good Design For Rest, Part 1 (Genesis 2:1-3) | David Platt
55:26~God's Good Design for Gender and Sexuality, Part 2 (Genesis 1-2) | Mike Kelsey
39:58~God's Good Design For Rest, Part 2 (Genesis 2:1-3) | Eric Saunders
50:05~God's Good Design for Work, Part 1 (Genesis 2:5-15) | Mike Kelsey
1:00:19~God's Good Design for Work, Part 2 (Genesis 2:15) | Mike Kelsey
47:54~God's Good Design For Marriage and Singleness, Part 1 (Genesis 2:18-25) | David Platt
43:33~God's Good Design For Marriage And Singleness, Part 2 (Genesis 2:18-25) | David Platt
42:05~Wonderful Counselor (Isaiah 9:6) | Christmas In Chaos | Mike Kelsey
48:35~What Loving One Another Looks Like (1 Corinthians 13:1-7) | Nate Reed
5:16~10:20 at Culpepper Garden (story)
48:47~Everlasting Father (Isaiah 9:6) | Christmas In Chaos | Mike Kelsey
34:15~Prince Of Peace (Isaiah 9:6) | Christmas In Chaos | David Platt
5:47~Tiwa (story)
5:39~car(e)pool (story)
51:19~Why You Need God's Word (Psalm 19) | Nate Reed
39:59~Jesus: Mighty God (Isaiah 9:6) | Christmas In Chaos | David Platt"""

MCLEAN_SHORTS_COUNT = 62
MCLEAN_SHORTS_SAMPLE = [
    "Week One Encouragement | 21 Days of Prayer 2026 (2:41)",
    "'What could God do through you if you were willing to give him your yes?' | Mike Kelsey (2:49)",
    "'No limit to what we can bother God with' | David Platt (2:48)",
    "21 Days of Prayer | Day 01 (1:45)",
    "Is the Bible worth prioritizing? | David Platt (0:59)",
    "Should Christians be afraid of science? | David Platt (1:48)",
    "Why does God create boundaries? | Mike Kelsey (2:55)",
    "A cure for church hurt | Eric Saunders (2:04)",
]

# ---------------------------------------------------------------------------
# Series captured from the public Series index (first render batch of the
# infinite-scroll list; the platform holds more)
SERIES = [
    ("God Is", 5, "King's Church London"),
    ("21 Days of Prayer and Fasting 2025", 21, "Crosspoint City Church"),
    ("Luke Part I: Jesus, Friend of Sinners", 18, "Redeemer Church"),
    ("More Than Enough", 6, "Port City Church"),
    ("The Road to Emmaus: Wanderings", 5, "Redeemer Church"),
    ("The Road to Emmaus: Conquests & Kings", 11, "Redeemer Church"),
    ("Genesis Part III: The Son Who Saves", 7, "Redeemer Church"),
    ("Acts Part II: Onward", 14, "Redeemer Church"),
    ("Songs of the Season", 4, "Port City Church"),
    ("Matthew Part I: King & Kingdom", 11, "Redeemer Church"),
    ("The Book of Psalms", 11, "Port City Church"),
    ("Exodus: The Deliverer", 13, "Redeemer Church"),
    ("Exiles", 11, "King's Church London"),
    ("Matthew Part II: The Words of the King", 12, "Redeemer Church"),
    ("Revelation Part II: The Return of the King", 10, "Redeemer Church"),
    ("Technology", 4, "King's Church London"),
    ("The Road to Emmaus: Q4", 9, "Redeemer Church"),
    ("1 + 2 Samuel: The Shadow King", 12, "Redeemer Church"),
    ("Christmas 2022: Faith, Hope, Joy, Peace", 4, "Redeemer Church"),
    ("Cross Series", 5, "King's Church London"),
]

# Additional series visible on the home page "Popular series" rail (overlapping + extra)
SERIES_EXTRA = ["Genesis Part II (Redeemer)", "Luke Part II: Jesus, Friend of Sinners (Redeemer)",
                "Walking in Wisdom (Port City)", "I Will; Be Clean (Hope NC)",
                "When We Demand A King (Hope NC)", "The Way (King's Church London)",
                "21 Days of Prayer", "The Promised Messiah", "Set Apart (Proclamation)"]

# Top 10 this week (home page, week of Aug 17, 2026)
TOP10 = [
    "From MrBeast Fame to Finding Jesus | The Chandler Hallow Story | The Jesus People Podcast Ep 46",
    "A Tale of Two Cities | J.D. Greear - The Summit Church",
    "You Are Covered by the Blood of Jesus - The Summit Church",
    "I Am Not Throwing Away My Shot | Curtis Andrusko - The Summit Church",
    "Heaven Will Not Be Boring - The Summit Church",
    "Where Does My Help Come? | 21 Days of Prayer | Tex Chettiar - King's Church",
    "What Changed Sam Burns' View of God Forever - Bible Caddie",
    "Pastor Joby Martin | Act Like Men Conference 2025 - Crosspoint City Church",
    "Missional Formation | Disciple the Deficits - Suzy Silk - Church of the City",
    "Jesus: Mighty God (Isaiah 9:6) | David Platt - McLean Bible Church",
]

SCALE_EVIDENCE = [
    "Content IDs observed on the live site run from 3 to 22,318; IDs are non-sequential, so the ID range is an upper bound on catalog size, not a count.",
    "The two largest church libraries captured hold 137 (The Summit Church) and 80 (McLean Bible Church) full-length messages, plus 61 and 62 shorts respectively; NewSpring holds 101.",
    "Podcast shows publish on weekly-or-faster cadence (12 of the 12 most recent podcast episodes belong to a single show, Own It / Justin Roethlingshoefer).",
    "New releases are current to June-August 2026; the platform is actively ingesting, so any census is a snapshot.",
]
