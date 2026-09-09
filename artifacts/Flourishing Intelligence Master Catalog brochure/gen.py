# -*- coding: utf-8 -*-
import html

domains = [
{"num":"01","name":"Whole-Life Foundations","sub":"Parallel to Flourishing Foundations","items":[
("The Whole Employee","Bring Your Whole Self to Work, Not Just Your Task List"),
("Thriving, Not Just Getting Through the Week","Move From Survival Mode to Genuine Engagement"),
("A Job That Fits Your Life","Align Your Work With What Actually Matters to You"),
("Building Margin Into a Demanding Role","Create Space Before You Hit Empty"),
("The Small Choices That Change Your Workday","Build Habits That Make Every Day Better"),
("Redefining What a Good Workday Looks Like","Move Past Busy Toward Genuinely Well-Spent"),
("The Employee's Mindset Reset","Renew the Beliefs That Shape How You Experience Work"),
("Starting Fresh in a New Role","Build Good Patterns From Day One Instead of Drifting Into Bad Ones"),
("Finding Meaning in the Ordinary Workday","Discover Significance in Tasks That Don't Feel Significant"),
("A Whole-Life Approach to Your Career","See Your Job as One Part of a Bigger, Well-Lived Life"),
]},
{"num":"02","name":"Inner Life & Focus","sub":"Parallel to Spiritual Flourishing","items":[
("A Quiet Mind in a Loud Workplace","Build Stillness Into a Distracting Environment"),
("The Practice of Presence at Work","Be Fully Where You Are Instead of Mentally Elsewhere"),
("Building Personal Habits That Actually Stick","Create Routines That Support Your Best Work"),
("Values-Driven Decision-Making","Make Daily Choices That Reflect What You Actually Believe"),
("The Inner Life Behind the Job Title","Strengthen What No Coworker Ever Sees"),
("Trusting Yourself Under Pressure","Build Confidence in Your Own Judgment"),
("A Personal Code for How You Work","Define the Principles That Guide Your Decisions"),
("Finding Stillness Before a Big Decision","Slow Down Enough to Choose Well"),
("The Practice of Reflection at Work","Learn From Experience Instead of Just Moving to the Next Thing"),
("Renewing Your Sense of Purpose Mid-Career","Reconnect With Why This Work Matters to You"),
]},
{"num":"03","name":"Emotional Wellbeing","sub":"Parallel to Emotional Flourishing","items":[
("Quieting Workplace Anxiety","Find Calm and Clarity in a High-Pressure Job"),
("Emotional Health on the Job","Build Inner Strength That Carries Into How You Work"),
("Handling Criticism Without Spiraling","Receive Feedback Without Losing Your Footing"),
("Recovering From a Bad Day at Work","Process Setbacks Without Carrying Them Into Tomorrow"),
("The Anxious Employee, Renewed","Retrain Anxious Thought Patterns Specific to Work Stress"),
("Building Resilience After a Difficult Project","Bounce Back Stronger After Things Didn't Go Well"),
("Managing Frustration With a Coworker","Process Irritation in Healthy, Constructive Ways"),
("Finding Joy in Work Again","Rediscover Engagement After a Draining Season"),
("The Weight of Workplace Comparison","Free Yourself From Constantly Measuring Against Colleagues"),
("Emotionally Whole at Work","Integrate What You Feel Into How You Show Up Professionally"),
]},
{"num":"04","name":"Workplace Relationships","sub":"Parallel to Relational Flourishing","items":[
("Working Well With Difficult People","Build Professional Relationships That Don't Drain You"),
("The Art of Giving and Receiving Feedback","Build Trust Through Honest, Respectful Communication"),
("Healthy Conflict With Coworkers","Disagree Without Damaging the Working Relationship"),
("Building Genuine Friendship at Work","Move Past Surface Politeness Into Real Connection"),
("Trusting a New Team","Build Confidence in Colleagues You Don't Know Well Yet"),
("The Coworker Who's Become a Real Friend","Navigate Friendship and Professionalism Together"),
("Repairing a Damaged Work Relationship","Rebuild Trust After a Conflict or Misunderstanding"),
("Belonging on a Team You Just Joined","Move From Outsider to Genuine Member"),
("Setting Boundaries With Demanding Colleagues","Protect Your Time Without Damaging the Relationship"),
("Relationships That Make Work Worth Showing Up For","Build Connection That Sustains You Through Hard Weeks"),
]},
{"num":"05","name":"Physical & Practical Wellbeing","sub":"Parallel to Physical Flourishing","items":[
("Energy Management for a Demanding Job","Build Rhythms That Keep You Sustainably Productive"),
("Building Healthy Habits Around a Busy Schedule","Make Small Changes That Fit a Real Work Life"),
("The Rested Employee","Protect Sleep From a Job That Wants More of Your Time"),
("Movement Breaks That Actually Happen","Build Physical Activity Into a Desk-Bound Day"),
("Eating Well on a Work Schedule","Make Healthier Choices Despite Limited Time"),
("Reducing Stress-Related Physical Tension","Address What Chronic Work Stress Does to Your Body"),
("The Sustainable Workday Rhythm","Build Patterns for Focus, Break, and Recovery"),
("Recovering From Burnout","Rebuild Energy After Running on Empty for Too Long"),
("Building Physical Boundaries at Work","Protect Rest Time From a Job That Never Fully Stops"),
("A Healthier Relationship With Your Workday","Structure Time in Ways That Support Your Whole Wellbeing"),
]},
{"num":"06","name":"Career & Contribution","sub":"Parallel to Vocational Flourishing","items":[
("Finding Purpose in Your Current Role","Connect What You Do Daily to Why It Matters"),
("Discovering What You're Actually Good At","Clarify Strengths You Can Build a Career Around"),
("Making Your Work Feel Meaningful Again","Reconnect Daily Tasks to a Larger Sense of Contribution"),
("Navigating a Career Crossroads","Find Clarity When Your Next Step Isn't Obvious"),
("Excellence Without Burning Out","Do Great Work Sustainably, Not at Any Cost"),
("Making the Most of a Job You Didn't Choose","Find Real Value in a Role You Fell Into"),
("The Side Project That Might Become Something More","Explore Ambition Alongside Your Current Job"),
("Recovering From Being Passed Over","Find Direction After a Disappointing Career Setback"),
("Bringing Your Full Effort to Work That Matters","Give Genuine Excellence Without Losing Perspective"),
("Building a Career You're Actually Proud Of","Define Success on Terms That Fit You"),
]},
{"num":"07","name":"Financial Wellbeing","sub":"Parallel to Financial Flourishing","items":[
("Making the Most of Your Paycheck","Build Practical Financial Habits Around Your Actual Income"),
("The Benefits You're Not Using","Understand and Maximize What Your Employer Already Offers"),
("Financial Stress and Focus at Work","Address How Money Worries Affect Your Job Performance"),
("Negotiating Pay With Confidence","Advocate for Fair Compensation Without Anxiety"),
("Building an Emergency Fund on a Regular Salary","Create Real Financial Margin Over Time"),
("The Retirement Contribution You Keep Meaning to Increase","Build Long-Term Financial Wisdom Into Today's Choices"),
("Understanding Your Total Compensation","See the Full Value of Pay, Benefits, and Perks Together"),
("Financial Goals Beyond the Next Paycheck","Build a Longer View of Your Financial Life"),
("The Side Income Conversation","Navigate Extra Work Without Jeopardizing Your Primary Job"),
("Contentment With What You Earn","Find Peace With Your Financial Situation While Still Growing"),
]},
{"num":"08","name":"Everyday Leadership","sub":"Parallel to Leadership Flourishing","items":[
("Leading Without a Title","Influence Your Team Even Without Formal Authority"),
("The Employee Who Leads From Where They Sit","Bring Genuine Influence to Any Role"),
("Building Trust With Colleagues and Managers Alike","Earn Credibility Through Consistency"),
("Speaking Up in a Meeting","Contribute Your Voice With Confidence and Clarity"),
("The Reluctant Project Lead","Step Into Informal Leadership You Didn't Seek"),
("Giving Feedback to a Peer","Offer Honest Input Without Overstepping or Underdelivering"),
("Handling Being Asked to Do More Than Your Role","Navigate Scope Creep With Clarity and Boundaries"),
("Mentoring a Newer Colleague","Invest in Someone Else's Growth Alongside Your Own Work"),
("The Employee Who Notices What's Not Working","Raise Concerns Constructively Instead of Just Complaining"),
("Everyday Integrity at Work","Build a Reputation for Doing the Right Thing Consistently"),
]},
{"num":"09","name":"Team & Community","sub":"Parallel to Community Flourishing","items":[
("Being a Good Teammate","Contribute to a Healthy Team Culture, Not Just Your Own Output"),
("Welcoming New Colleagues Well","Help Someone Else Feel They Belong on the Team"),
("Contributing to a Team You Didn't Choose","Find Your Place in a Group You Were Simply Assigned To"),
("The Employee Volunteer Opportunity","Use Company-Sponsored Service to Build Genuine Community Impact"),
("Building Community Across Departments","Connect With Colleagues Beyond Your Own Immediate Team"),
("Showing Up for a Coworker Going Through Something Hard","Offer Real Support Within Professional Boundaries"),
("The Employee Resource Group Worth Joining","Find Belonging Through Shared Identity or Interest at Work"),
("Contributing to a Positive Team Culture","Be Part of the Solution, Not Just a Participant in the Problem"),
("Building Relationships With Remote Colleagues","Create Real Connection Across Distance"),
("Being Known for How You Treat People","Build a Reputation for Genuine Care Toward Coworkers"),
]},
{"num":"10","name":"Growth & Legacy","sub":"Parallel to Legacy Flourishing","items":[
("Your Best Years at Work May Still Be Ahead","Approach Your Career With Renewed Energy and Possibility"),
("What You Want to Be Known For at Work","Define the Reputation You're Actually Building"),
("Making Your Time Here Count","Invest Fully in the Season You're Actually In"),
("The Legacy of How You Treated People","Consider What Colleagues Will Remember About Working With You"),
("Multiplying Your Impact Through Others","Extend Your Contribution by Developing Those Around You"),
("Preparing for Your Next Chapter","Build Skills and Relationships That Serve Wherever You Go Next"),
("Finishing a Project Well","Bring the Same Care to the End of Work as the Beginning"),
("What Matters Most in Your Career","Clarify Priorities Before the Urgent Crowds Out the Important"),
("Leaving a Role Well","Depart a Job With Integrity and Genuine Gratitude"),
("A Career Well Spent","Build a Working Life You'll Look Back on Without Regret"),
]},
]

def esc(s):
    return html.escape(s, quote=False)

out = []
for d in domains:
    out.append(f'''
    <div class="library" id="dom-{d['num']}">
      <div class="lib-head">
        <span class="lib-numeral">{d['num']}</span>
        <div class="lib-title-block">
          <h3>{esc(d['name'])}</h3>
          <div class="audience">{esc(d['sub'])}</div>
        </div>
      </div>
      <div class="specimen-grid">''')
    for i, (title, subtitle) in enumerate(d['items'], start=1):
        n = (int(d['num'])-1)*10 + i
        out.append(f'''
        <div class="specimen">
          <span class="spec-num">{n:03d}</span>
          <div class="spec-body">
            <div class="spec-title">{esc(title)}</div>
            <div class="spec-sub">{esc(subtitle)}</div>
          </div>
        </div>''')
    out.append('''
      </div>
    </div>''')

with open('/home/claude/emp/catalog_block.html', 'w') as f:
    f.write("\n".join(out))
print("done, domains:", len(domains))
