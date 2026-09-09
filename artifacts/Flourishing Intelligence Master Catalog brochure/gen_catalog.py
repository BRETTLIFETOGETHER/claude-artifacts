# -*- coding: utf-8 -*-
import html

categories = [
    {
        "num": "01",
        "name": "Flourishing Foundations",
        "sub": "Build a Whole Life That Thrives from the Inside Out",
        "items": [
            ("The Flourishing Life", "Move Beyond Surviving and Step Into the Life God Designed You to Live"),
            ("Becoming Fully Alive", "Awaken Your Faith, Renew Your Purpose, and Rediscover the Joy of Living"),
            ("Living Well", "Build a Life of Greater Peace, Health, Meaning, and Connection"),
            ("Whole-Life Flourishing", "Bring Every Area of Your Life into Greater Health and Alignment"),
            ("Created to Flourish", "Discover God's Design for a Life That Is Rooted, Fruitful, and Strong"),
            ("Life in Balance", "Find a Healthier Rhythm for Everything—and Everyone—That Matters"),
            ("Healthy from the Inside Out", "Transform Your Heart, Habits, Relationships, and Everyday Life"),
            ("Flourishing Every Day", "Practice the Small Choices That Lead to a Stronger and More Meaningful Life"),
            ("Living with Margin", "Create the Space You Need for God, People, Rest, and What Matters Most"),
            ("Designed for More", "Stop Settling for Less and Step Into Your God-Given Potential"),
        ]
    },
    {
        "num": "02",
        "name": "Spiritual Flourishing",
        "sub": "Deepen Your Relationship with God and Strengthen Your Soul",
        "items": [
            ("Rooted", "Develop a Faith That Remains Strong Through Every Season"),
            ("Walking with God", "Experience God's Presence and Direction in Everyday Life"),
            ("Abiding", "Remain Connected to Christ and Live from His Strength"),
            ("Soul Care", "Restore Your Inner Life Before the Demands of Life Drain It"),
            ("Hearing God's Voice", "Recognize His Leading and Respond with Greater Confidence"),
            ("Living by Faith", "Move Beyond Fear and Trust God with What Comes Next"),
            ("Spiritual Habits", "Build Daily Practices That Lead to Lifelong Transformation"),
            ("Prayer That Changes You", "Move Beyond Saying Prayers and Experience a Deeper Life with God"),
            ("Worship as a Lifestyle", "Honor God in Every Moment, Decision, Relationship, and Responsibility"),
            ("Flourishing Spiritually", "Cultivate a Faith That Grows Deeper, Stronger, and More Fruitful"),
        ]
    },
    {
        "num": "03",
        "name": "Emotional Flourishing",
        "sub": "Find Greater Peace, Healing, Hope, and Resilience",
        "items": [
            ("Quiet the Noise", "Find Calm, Clarity, and Confidence in an Overwhelming World"),
            ("Emotional Health", "Become Stronger on the Inside So You Can Live Better on the Outside"),
            ("Peace of Mind", "Replace Racing Thoughts and Constant Worry with Lasting Peace"),
            ("Hope Rising", "Find New Strength When Life Feels Heavy or Uncertain"),
            ("Healing the Heart", "Face What Hurt You and Move Forward with Freedom and Hope"),
            ("Freedom from Anxiety", "Break the Cycle of Fear and Build a Life of Greater Trust and Peace"),
            ("Joy Again", "Rediscover Delight, Gratitude, and Hope After a Difficult Season"),
            ("Healthy Emotions", "Understand What You Feel and Respond with Wisdom and Grace"),
            ("Resilient Living", "Develop the Strength to Recover, Adapt, and Keep Moving Forward"),
            ("Flourishing Through Adversity", "Turn Life's Hardest Seasons into Opportunities for Your Deepest Growth"),
        ]
    },
    {
        "num": "04",
        "name": "Relational Flourishing",
        "sub": "Build Stronger, Healthier, and More Life-Giving Relationships",
        "items": [
            ("Better Together", "Experience the Strength and Joy of Authentic Community"),
            ("Healthy Friendships", "Build the Kind of Relationships That Help Everyone Grow"),
            ("Love That Lasts", "Strengthen the Commitments and Practices That Keep Relationships Strong"),
            ("Family Flourishing", "Create a Healthier, Closer, and More Purposeful Family Life"),
            ("Parenting with Purpose", "Raise Children with Faith, Character, Confidence, and Compassion"),
            ("Building Trust", "Create Relationships Where Honesty, Safety, and Connection Can Grow"),
            ("The Freedom of Forgiveness", "Release the Past and Make Room for Healing, Peace, and Restoration"),
            ("Belonging", "Move Beyond Isolation and Find the Community You Were Created For"),
            ("Community That Matters", "Build Relationships That Bring Strength, Support, and Lasting Change"),
            ("Relationships That Thrive", "Practice the Habits That Help Love, Trust, and Connection Grow"),
        ]
    },
    {
        "num": "05",
        "name": "Physical Flourishing",
        "sub": "Care for the Body God Has Entrusted to You",
        "items": [
            ("Whole-Life Health", "Strengthen Your Body, Mind, Soul, and Everyday Life"),
            ("Healthy Habits", "Make Small Changes That Produce Stronger and Lasting Results"),
            ("The Gift of Rest", "Slow Down, Recover Your Strength, and Restore Your Soul"),
            ("Renewed Energy", "Replace Exhaustion with Rhythms That Help You Feel Fully Alive"),
            ("Made to Move", "Strengthen Your Body and Rediscover the Joy of an Active Life"),
            ("Nourished", "Make Healthier Food Choices That Support the Life You Want to Live"),
            ("Stress Less", "Reduce the Pressure and Build Greater Peace into Everyday Life"),
            ("Sabbath Living", "Discover the Restorative Power of Stopping, Trusting, and Delighting in God"),
            ("Healthy Rhythms", "Create Sustainable Patterns for Work, Rest, Health, and Renewal"),
            ("Living Strong", "Build the Strength and Endurance to Fully Live Your God-Given Purpose"),
        ]
    },
    {
        "num": "06",
        "name": "Vocational Flourishing",
        "sub": "Discover Greater Purpose, Peace, and Impact Through Your Work",
        "items": [
            ("Work with Purpose", "Connect What You Do Each Day with Why God Has You There"),
            ("Calling", "Discover the Unique Contribution Your Life Was Designed to Make"),
            ("Meaningful Work", "Turn Your Daily Responsibilities into a Life-Giving Contribution"),
            ("The Excellence Advantage", "Bring Your Best to What Matters Without Losing What Matters Most"),
            ("Everyday Influence", "Use Your Work, Relationships, and Character to Make a Positive Difference"),
            ("Productivity with Peace", "Accomplish What Matters Without Sacrificing Your Health or Relationships"),
            ("Monday Matters", "Bring Your Faith, Values, and Purpose into the Workweek"),
            ("Your Next Chapter", "Navigate Career Transitions with Clarity, Courage, and Confidence"),
            ("Marketplace Impact", "Use Your Work and Influence to Serve People and Advance God's Purposes"),
            ("Flourishing at Work", "Build a Healthier, More Meaningful, and More Sustainable Working Life"),
        ]
    },
    {
        "num": "07",
        "name": "Financial Flourishing",
        "sub": "Build Financial Wisdom, Freedom, Generosity, and Lasting Purpose",
        "items": [
            ("Financial Wisdom", "Make Better Decisions with Everything God Has Entrusted to You"),
            ("Smart Money", "Build Practical Habits That Strengthen Your Financial Future"),
            ("Stewardship for Life", "Manage Your Resources with Faith, Wisdom, and Eternal Purpose"),
            ("Generous Living", "Experience the Freedom and Joy of an Open-Handed Life"),
            ("Wealth with Purpose", "Turn Financial Success into Meaningful and Lasting Impact"),
            ("Enough", "Break Free from Comparison and Discover the Power of Contentment"),
            ("Freedom from Debt", "Create a Practical Path from Financial Pressure to Greater Freedom"),
            ("Planning Your Future", "Prepare Wisely for the Life, Family, and Legacy You Want to Build"),
            ("Family Legacy", "Pass Down Faith, Wisdom, Values, and Resources That Last"),
            ("Financial Peace", "Replace Money Stress with Greater Confidence, Clarity, and Control"),
        ]
    },
    {
        "num": "08",
        "name": "Leadership Flourishing",
        "sub": "Lead Yourself Well, Strengthen Others, and Build What Lasts",
        "items": [
            ("Lead Yourself First", "Develop the Character and Discipline Behind Every Healthy Leader"),
            ("Character That Leads", "Become the Kind of Person Others Can Trust and Follow"),
            ("The Power of Influence", "Make a Greater Difference Without Relying on Position or Authority"),
            ("Servant Leadership", "Lead with Humility, Courage, and a Commitment to Help Others Thrive"),
            ("Leading with Wisdom", "Make Better Decisions in Complex and Changing Situations"),
            ("Courageous Leadership", "Face Difficult Decisions and Lead Forward with Faith and Conviction"),
            ("Healthy Teams", "Build Trust, Alignment, Ownership, and Shared Success"),
            ("Legacy Leadership", "Build People and Organizations That Continue to Flourish Without You"),
            ("Multiplying Leaders", "Stop Doing Everything Yourself and Develop Others to Lead"),
            ("Finish Well", "Stay Faithful, Fruitful, and Focused Through Every Season of Leadership"),
        ]
    },
    {
        "num": "09",
        "name": "Community Flourishing",
        "sub": "Help Your Neighborhood, Church, and Community Become Stronger Together",
        "items": [
            ("Neighboring Well", "Turn Ordinary Proximity into Meaningful Relationships and Local Impact"),
            ("Serving Together", "Unite People Around Practical Acts of Compassion and Care"),
            ("Community Transformation", "Move from Meeting Needs to Creating Lasting Change"),
            ("Justice and Compassion", "Stand for What Is Right While Serving People with Mercy and Love"),
            ("Local Impact", "Make a Measurable Difference Right Where God Has Placed You"),
            ("Hope Without Borders", "Join God's Work of Compassion and Transformation Around the World"),
            ("Living Generously", "Use Your Time, Talents, Relationships, and Resources to Bless Others"),
            ("Open Doors", "Rediscover Hospitality as a Powerful Way to Build Belonging"),
            ("Building Better Communities", "Create Environments Where People, Families, and Neighborhoods Can Thrive"),
            ("Flourishing Together", "Help Everyone Grow by Building a Culture of Shared Well-Being"),
        ]
    },
    {
        "num": "10",
        "name": "Legacy Flourishing",
        "sub": "Live Today in a Way That Continues to Matter Tomorrow",
        "items": [
            ("Your Best Years Ahead", "Approach the Future with Renewed Faith, Energy, and Purpose"),
            ("Dream Again", "Rediscover the Possibilities God Still Has for Your Life"),
            ("A Life of Significance", "Move Beyond Personal Success and Invest in What Matters Forever"),
            ("Living Your Legacy", "Make Your Values Visible Through the Way You Live Today"),
            ("Mentoring Matters", "Invest Your Experience, Wisdom, and Faith in the Next Generation"),
            ("Multiplying Your Life", "Expand Your Impact by Developing and Empowering Others"),
            ("The Second Half", "Turn Your Experience into Your Most Meaningful Season of Contribution"),
            ("Lasting Impact", "Build Something Worth Passing On to the People Who Follow You"),
            ("What Matters Most", "Clarify Your Priorities Before the Urgent Crowds Out the Important"),
            ("A Life Well Lived", "Finish with Faith, Gratitude, Purpose, and No Regrets"),
        ]
    },
]

# 5 context badges applied to every series (Church, Group, Family, Personal, Ministry)
badges = ["Church", "Group", "Family", "Personal", "Ministry"]
badge_svgs = {
    "Church": "M12 2 L4 7 V10 H20 V7 Z M6 10 V21 H10 V15 H14 V21 H18 V10",
    "Group": "M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM2 20c0-3 3-5 6-5s6 2 6 5M10 20c0-2.5 2.5-4.5 6-4.5s6 2 6 4.5",
    "Family": "M12 3 3 10h2v10h5v-6h4v6h5V10h2Z",
    "Personal": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm-7 9c0-4 3-7 7-7s7 3 7 7",
    "Ministry": "M5 21V9l7-4 7 4v12M9 21v-6h6v6",
}

def esc(s):
    return html.escape(s, quote=False)

out = []
counter = 1
for cat in categories:
    out.append(f'''
    <div class="category" id="cat-{cat['num']}">
      <div class="cat-header">
        <span class="cat-numeral">{cat['num']}</span>
        <div class="cat-title-block">
          <h3>{esc(cat['name'])}</h3>
          <p class="cat-sub">{esc(cat['sub'])}</p>
        </div>
      </div>
      <div class="specimen-grid">''')
    for title, subtitle in cat['items']:
        badge_html = "".join(
            f'<span class="badge" title="{b}"><svg viewBox="0 0 24 24"><path d="{badge_svgs[b]}"/></svg></span>'
            for b in badges
        )
        out.append(f'''
        <div class="specimen">
          <span class="spec-num">{counter:03d}</span>
          <div class="spec-body">
            <div class="spec-title">{esc(title)}</div>
            <div class="spec-sub">{esc(subtitle)}</div>
          </div>
          <div class="spec-badges">{badge_html}</div>
        </div>''')
        counter += 1
    out.append('''
      </div>
    </div>''')

with open('/home/claude/ff/catalog_block.html', 'w') as f:
    f.write("\n".join(out))

print("Generated", counter - 1, "entries")
