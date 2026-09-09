import json, sys, re, difflib
sys.path.insert(0, '.')
from findc import norm, CTEXT, pagemap
from loadp import load_paras
from rapidfuzz import fuzz

A = load_paras('A_base.md')
B = load_paras('B_pg.md')
ATEXT = ' '.join(norm(x) for x in A)
BTEXT = ' '.join(norm(x) for x in B)


def best_sub(q, TEXT):
    q = norm(q)
    if len(q) < 12:
        return (0.0, '')
    al = fuzz.partial_ratio_alignment(q, TEXT, score_cutoff=0)
    if al is None:
        return (0.0, '')
    sub = TEXT[al.dest_start:al.dest_end]
    return (fuzz.ratio(q, sub) / 100.0, sub)


# probe pairs: (label, B wording, C wording) -- pulled from the substantive scan
probes = [
    ("p19 practices Q",
     "Which of these four practices is most absent from how you handle money right now",
     "Which of these four practices is most challenging for how you handle money right now"),
    ("p51 Grow",
     "Grow. Saving and margin, the room that turns a fragile budget into a steady one",
     "Grow. Saving and investing to create margin now and in the future. Margin becomes the space that turns a fragile budget into a stable one"),
    ("p60 whisper",
     "It's the question people whisper in the dark, and Ron says it's the one he hears more than any other",
     "It's the question people whisper just to themselves, and Ron says it's the one he hears more than any other"),
    ("p60 two answers",
     "This week gives it two. The first is practical",
     "This week gives two answers. The first is practical"),
    ("p60 fragile",
     "confidence that depends on a number will always be fragile, because the number can move. Confidence anchored in the Provider holds when the number doesn't",
     "confidence that depends on a number will always feel vulnerable, because the number can move. Confidence anchored in the Provider holds when the provision feels fragile"),
    ("p98 meaning",
     "What's the difference between handing down resources and handing down meaning",
     "What's the difference between handing down resources and handing down purpose"),
    ("p109 safe env",
     "a place where people can be heard and feel loved, especially on a subject as tender as money",
     "a place where people can be heard and feel loved and supported, especially on a subject as sensitive as money"),
    ("p109 no numbers",
     "To never ask each other what we make, owe, give, or have saved. Money is personal, and dignity matters more than disclosure",
     "To never ask each other what we make, owe, give, or have saved. You and God know your numbers and that's what counts"),
    ("p109 encouragement",
     "To be givers, not takers. We want to grow, and to help each other take one faithful next step",
     "To give encouragement not just receive it. We want to grow, and to help each other make one faithful next step"),
    ("p118 split",
     "You can always split into two circles after the video and come back together to pray",
     "You can always split into two circles after the video and come back together to pray"),
    ("p122 thirty-day",
     "Do the thirty-day tracking exercise together",
     "Do the thirty-day spending plan together"),
    ("p122 forty",
     "The forty-two days end, but the ten seconds each morning",
     "The forty days end, but the ten seconds each morning"),
    ("p125 expert",
     "You are not the teacher, and you are not the financial advisor",
     "You are not the teacher, and you don't have to be a financial expert"),
    ("p128 alone",
     "Remember you're not alone. God is with you, and so is your church. You're not carrying this by yourself",
     "Remember you're not alone. God is with you, and so is your church. And hopefully a co-leader as well.You're not carrying this by yourself"),
    ("p128 curriculum",
     "Trust the flow of each session, the questions, the exercise, the story",
     "Trust the flow of the curriculum, the questions, the exercise, the story"),
    ("p116 verse cards",
     "SESSION ONE The Ownership Question",
     "SESSION ONE The Ownership Question"),
]

print(f"{'label':22} {'inA':>6} {'inB':>6}  verdict")
print('-' * 90)
for label, bw, cw in probes:
    aB, _ = best_sub(bw, ATEXT)
    aC, _ = best_sub(cw, ATEXT)
    bB, _ = best_sub(bw, BTEXT)
    bC, _ = best_sub(cw, BTEXT)
    # which wording does A support?
    if aB - aC > 0.03:
        av = 'A=B'
    elif aC - aB > 0.03:
        av = 'A=C'
    else:
        av = 'A=?'
    verdict = {'A=B': 'C changed it (team/layout edit)',
               'A=C': 'B changed it (ALLEN EDIT)',
               'A=?': 'A absent/ambiguous'}[av]
    print(f"{label:22} B:{aB:.2f} C:{aC:.2f}  {av}  -> {verdict}")
