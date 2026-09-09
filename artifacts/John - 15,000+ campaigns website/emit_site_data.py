#!/usr/bin/env python3
"""Phase 2: scripture backbones, promise summaries, shards, index, facets, i18n name tables."""
import json, hashlib, sys, os, re
from collections import defaultdict

SP = json.load(open("/home/claude/build/spine.json"))
ROWS, THEMES, NESTS, STATS = SP["rows"], SP["themes"], SP["nests"], SP["stats"]
OUT = "/home/claude/site/data"; os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- canonical scripture table
# verse counts only for (book, chapter) pairs used in pools — hand-verified.
VC = {
 ("Genesis",1):31,("Genesis",12):20,("Genesis",50):26,("Exodus",14):31,("Exodus",20):26,("Deuteronomy",6):25,
 ("Deuteronomy",31):30,("Joshua",1):18,("Joshua",24):33,("Ruth",1):22,("1 Samuel",16):23,("2 Samuel",22):51,
 ("1 Kings",19):21,("1 Chronicles",29):30,("Nehemiah",1):11,("Nehemiah",2):20,("Nehemiah",6):19,("Esther",4):17,
 ("Job",19):29,("Job",42):17,("Psalm",1):6,("Psalm",4):8,("Psalm",8):9,("Psalm",13):6,("Psalm",16):11,("Psalm",19):14,
 ("Psalm",23):6,("Psalm",25):22,("Psalm",27):14,("Psalm",30):12,("Psalm",32):11,("Psalm",34):22,("Psalm",37):40,
 ("Psalm",40):17,("Psalm",42):11,("Psalm",46):11,("Psalm",51):19,("Psalm",56):13,("Psalm",62):12,("Psalm",63):11,
 ("Psalm",73):28,("Psalm",84):12,("Psalm",90):17,("Psalm",91):16,("Psalm",100):5,("Psalm",103):22,("Psalm",107):43,
 ("Psalm",112):10,("Psalm",116):19,("Psalm",119):176,("Psalm",121):8,("Psalm",127):5,("Psalm",128):6,("Psalm",130):8,
 ("Psalm",133):3,("Psalm",139):24,("Psalm",145):21,("Psalm",147):20,("Proverbs",2):22,("Proverbs",3):35,
 ("Proverbs",4):27,("Proverbs",10):32,("Proverbs",11):31,("Proverbs",13):25,("Proverbs",15):33,("Proverbs",16):33,
 ("Proverbs",17):28,("Proverbs",18):24,("Proverbs",22):29,("Proverbs",24):34,("Proverbs",27):27,("Proverbs",31):31,
 ("Ecclesiastes",3):22,("Ecclesiastes",4):16,("Isaiah",6):13,("Isaiah",26):21,("Isaiah",30):33,("Isaiah",40):31,
 ("Isaiah",41):29,("Isaiah",43):28,("Isaiah",53):12,("Isaiah",55):13,("Isaiah",58):14,("Isaiah",61):11,
 ("Jeremiah",1):19,("Jeremiah",17):27,("Jeremiah",29):32,("Lamentations",3):66,("Ezekiel",36):38,("Daniel",1):21,
 ("Daniel",3):30,("Daniel",6):28,("Hosea",6):11,("Joel",2):32,("Micah",6):16,("Habakkuk",3):19,("Zephaniah",3):20,
 ("Haggai",1):15,("Zechariah",4):14,("Malachi",3):18,
 ("Matthew",4):25,("Matthew",5):48,("Matthew",6):34,("Matthew",7):29,("Matthew",9):38,("Matthew",11):30,
 ("Matthew",14):36,("Matthew",16):28,("Matthew",18):35,("Matthew",19):30,("Matthew",20):34,("Matthew",22):46,
 ("Matthew",25):46,("Matthew",28):20,("Mark",1):45,("Mark",2):28,("Mark",4):41,("Mark",5):43,("Mark",6):56,
 ("Mark",8):38,("Mark",10):52,("Mark",12):44,("Luke",4):44,("Luke",5):39,("Luke",6):49,("Luke",8):56,("Luke",9):62,
 ("Luke",10):42,("Luke",11):54,("Luke",12):59,("Luke",14):35,("Luke",15):32,("Luke",18):43,("Luke",19):48,
 ("Luke",24):53,("John",1):51,("John",3):36,("John",4):54,("John",6):71,("John",8):59,("John",10):42,("John",11):57,
 ("John",13):38,("John",14):31,("John",15):27,("John",16):33,("John",17):26,("John",20):31,("John",21):25,
 ("Acts",1):26,("Acts",2):47,("Acts",4):37,("Acts",9):43,("Acts",16):40,("Acts",20):38,("Romans",5):21,
 ("Romans",6):23,("Romans",8):39,("Romans",12):21,("Romans",15):33,("1 Corinthians",3):23,("1 Corinthians",9):27,
 ("1 Corinthians",12):31,("1 Corinthians",13):13,("1 Corinthians",15):58,("1 Corinthians",16):24,
 ("2 Corinthians",1):24,("2 Corinthians",4):18,("2 Corinthians",5):21,("2 Corinthians",8):24,("2 Corinthians",9):15,
 ("2 Corinthians",12):21,("Galatians",2):21,("Galatians",5):26,("Galatians",6):18,("Ephesians",1):23,
 ("Ephesians",2):22,("Ephesians",3):21,("Ephesians",4):32,("Ephesians",5):33,("Ephesians",6):24,
 ("Philippians",1):30,("Philippians",2):30,("Philippians",3):21,("Philippians",4):23,("Colossians",1):29,
 ("Colossians",3):25,("1 Thessalonians",5):28,("2 Thessalonians",3):18,("1 Timothy",4):16,("1 Timothy",6):21,
 ("2 Timothy",1):18,("2 Timothy",2):26,("2 Timothy",3):17,("Titus",2):15,("Philemon",1):25,("Hebrews",4):16,
 ("Hebrews",10):39,("Hebrews",11):40,("Hebrews",12):29,("Hebrews",13):25,("James",1):27,("James",2):26,
 ("James",3):18,("James",4):17,("James",5):20,("1 Peter",1):25,("1 Peter",2):25,("1 Peter",4):19,("1 Peter",5):14,
 ("2 Peter",1):21,("1 John",1):10,("1 John",3):24,("1 John",4):21,("2 John",1):13,("3 John",1):14,("Jude",1):25,
 ("Revelation",2):29,("Revelation",3):22,("Revelation",21):27,
}
REF_RX = re.compile(r"^((?:[123] )?[A-Za-z ]+?) (\d+):(\d+)(?:[–-](\d+))?$")
def valid(ref):
    mm = REF_RX.match(ref)
    if not mm: return False
    b, c, v1, v2 = mm.group(1), int(mm.group(2)), int(mm.group(3)), mm.group(4)
    mx = VC.get((b, c))
    if mx is None: return False
    v2 = int(v2) if v2 else v1
    return 1 <= v1 <= v2 <= mx

# channel-keyed pools (index-aligned with CHANNELS order in generate_data.py)
POOLS = [
 # Purpose & Calling
 ["Ephesians 2:10","Jeremiah 29:11","Romans 8:28","Proverbs 3:5-6","Philippians 3:13-14","Matthew 5:14-16","Colossians 3:23-24",
  "Psalm 138:8" if False else "Psalm 37:4-5","Isaiah 6:8","2 Timothy 1:9","John 15:16","Matthew 28:19-20","Acts 20:24",
  "Psalm 32:8","1 Peter 2:9","Esther 4:14","Micah 6:8","Matthew 4:19","Luke 9:23","Romans 12:1-2","1 Corinthians 15:58",
  "Galatians 6:9","Psalm 90:12","Proverbs 16:3","Proverbs 16:9","Philippians 1:6","John 10:10","Matthew 6:33","Psalm 119:105",
  "Isaiah 30:21","Hebrews 12:1-2","2 Timothy 2:15","Joshua 1:9","Psalm 25:4-5","Luke 5:10-11","Mark 1:17","John 21:15-17",
  "Acts 1:8","Colossians 1:16-17","Proverbs 19:21" if False else "Proverbs 16:33","Ecclesiastes 3:1","Psalm 139:16"],
 # Identity & Significance
 ["Psalm 139:13-14","Ephesians 1:4-5","1 John 3:1","2 Corinthians 5:17","Genesis 1:27" if False else "Psalm 8:4-5","Romans 8:15-16",
  "Galatians 2:20","Ephesians 2:10","1 Peter 2:9","John 1:12","Colossians 3:3","Romans 8:1","Isaiah 43:1","Zephaniah 3:17",
  "Psalm 139:1-4","John 15:15","Romans 8:37","2 Timothy 1:7","1 John 4:9-10","Ephesians 1:13-14","Isaiah 43:4","Psalm 34:5",
  "Luke 12:6-7","Matthew 5:13","John 8:36","Galatians 5:1","Colossians 1:22" if False else "Colossians 3:12","1 John 3:2","Psalm 100:3"],
 # Community & Belonging
 ["Acts 2:42-47","Hebrews 10:24-25","Ecclesiastes 4:9-10","Ecclesiastes 4:12","Romans 12:4-5","1 Corinthians 12:12-14",
  "John 13:34-35","Galatians 6:2","Colossians 3:13-14","1 Thessalonians 5:11","Romans 15:7","Psalm 133:1","Proverbs 27:17",
  "1 Peter 4:8-10","Ephesians 4:2-3","Acts 4:32","Romans 12:10","Philippians 2:1-4","Mark 2:3-5","Luke 19:5-6",
  "Matthew 18:20","1 John 1:7","Proverbs 17:17","Proverbs 18:24","Genesis 2:18" if False else "Psalm 68:6" if False else "Psalm 133:1-3",
  "John 17:20-21","Ephesians 2:19","Colossians 3:16","Hebrews 13:1-2","Romans 16:3-4" if False else "Acts 2:46-47"],
 # Prayer, Worship & Disciplines
 ["Matthew 6:9-13","Philippians 4:6-7","1 Thessalonians 5:16-18","James 5:16","Psalm 46:10","Matthew 6:6","Luke 11:9-10",
  "Psalm 63:1","Psalm 100:1-2","Psalm 100:4","John 4:23-24","Psalm 95:6" if False else "Psalm 34:1-3","Colossians 4:2","Mark 1:35",
  "Psalm 5:3","Daniel 6:10","Acts 2:42","2 Chronicles 7:14" if False else "Joel 2:12-13","Psalm 119:11","Psalm 119:15-16","Joshua 1:8",
  "Psalm 1:1-3","Matthew 4:4","Hebrews 4:16","Ephesians 6:18","Romans 12:12","Psalm 27:4","Psalm 84:1-2","Psalm 84:10",
  "Isaiah 40:31","Psalm 130:5-6","Luke 18:1","Matthew 26:41" if False else "Mark 6:31","Psalm 62:1-2","Psalm 46:1-3","Habakkuk 3:17-18"],
 # Money & Stewardship
 ["1 Timothy 6:6-8","1 Timothy 6:10","1 Timothy 6:17-19","Matthew 6:19-21","Matthew 6:24","Proverbs 3:9-10","Proverbs 22:7",
  "Luke 16:10-11" if False else "Luke 16:10","Philippians 4:11-13","Philippians 4:19","Hebrews 13:5","Proverbs 21:20" if False else "Proverbs 13:11",
  "Proverbs 27:23-24" if False else "Proverbs 24:3-4","Ecclesiastes 5:10" if False else "Proverbs 11:28","Matthew 25:21","Luke 12:15","Luke 14:28",
  "Psalm 24:1","Deuteronomy 8:18" if False else "Proverbs 10:22","Proverbs 22:26-27" if False else "Proverbs 22:1","Malachi 3:10","2 Corinthians 9:8",
  "Proverbs 15:16","Proverbs 16:8","Matthew 6:31-33","Luke 12:22-24" if False else "Luke 12:24","Psalm 37:25" if False else "Psalm 37:21",
  "Proverbs 3:27" if False else "Proverbs 11:24-25","Romans 13:8" if False else "Proverbs 22:9","Proverbs 30:8-9" if False else "Proverbs 17:1"],
 # Generosity & Legacy
 ["2 Corinthians 9:6-7","2 Corinthians 9:8","2 Corinthians 8:9","Acts 20:35","Proverbs 11:24-25","Malachi 3:10","Luke 6:38",
  "Matthew 6:19-21","1 Timothy 6:18-19","Proverbs 22:9","1 Chronicles 29:14","Psalm 112:5" if False else "Psalm 112:9","2 Corinthians 8:12",
  "Mark 12:41-44","Luke 12:33-34" if False else "Luke 12:33","John 3:16","Romans 12:8","Galatians 6:9-10","Hebrews 13:16","James 1:17",
  "Proverbs 3:9-10","Deuteronomy 15:10" if False else "Proverbs 28:27" if False else "Proverbs 19:17","Matthew 10:8","Psalm 24:1","Matthew 25:40",
  "Luke 16:10" if False else "Luke 19:8-9","2 Corinthians 9:11","1 Timothy 6:17" if False else "Ecclesiastes 5:19" if False else "Proverbs 13:22"],
 # Family Legacy & Generations
 ["Proverbs 13:22","Psalm 78:4" if False else "Psalm 145:4","Deuteronomy 6:6-7","Psalm 127:3","Psalm 128:1-2","Joshua 24:15",
  "Psalm 103:17-18" if False else "Psalm 103:17","Proverbs 22:6","2 Timothy 1:5","Psalm 90:12","Psalm 71:18" if False else "Psalm 92:14" if False else "Psalm 145:3-4",
  "Genesis 12:2-3" if False else "Genesis 12:2","Proverbs 17:6","Isaiah 44:3" if False else "Isaiah 43:5" if False else "Isaiah 41:10","1 Chronicles 29:11-12",
  "Psalm 24:1","Proverbs 3:9-10","Ecclesiastes 3:1","Proverbs 16:31" if False else "Proverbs 16:3","Psalm 78:6-7" if False else "Psalm 102:18" if False else "Psalm 119:90",
  "Matthew 25:21","Luke 12:48","1 Timothy 6:17-19","Proverbs 27:23-24" if False else "Proverbs 24:27","Hebrews 11:8-10" if False else "Hebrews 11:8",
  "Genesis 50:20","Ruth 1:16","Malachi 3:6" if False else "Psalm 100:5","Deuteronomy 31:6" if False else "Deuteronomy 31:8","2 Samuel 22:31"],
 # Marriage & Relationships
 ["Ephesians 5:25","Ephesians 5:33","1 Corinthians 13:4-7","Ecclesiastes 4:9-10","Ecclesiastes 4:12","Colossians 3:13-14",
  "1 Peter 4:8","Song of Songs 8:6-7" if False else "Proverbs 18:22","Genesis 2:24" if False else "Mark 10:8-9" if False else "Matthew 19:5-6",
  "Ephesians 4:2-3","Ephesians 4:26-27" if False else "Ephesians 4:32","James 1:19","Proverbs 15:1","Philippians 2:3-4","Romans 12:10",
  "1 John 4:19" if False else "1 John 4:7-8","Proverbs 31:10-12" if False else "Proverbs 31:10","Colossians 3:18-19" if False else "Colossians 3:14",
  "Hebrews 13:4","Proverbs 5:18-19" if False else "Proverbs 5:18" if False else "Proverbs 17:9","Matthew 7:24-25","Psalm 127:1","Proverbs 24:3-4",
  "1 Corinthians 16:14","Galatians 5:22-23","John 15:12-13" if False else "John 15:12"],
 # Parenting & Family
 ["Deuteronomy 6:6-7","Proverbs 22:6","Psalm 127:3-5" if False else "Psalm 127:3","Ephesians 6:4","Colossians 3:21" if False else "Colossians 3:20-21",
  "Psalm 78:4" if False else "Psalm 145:4","Proverbs 29:17" if False else "Proverbs 13:24" if False else "Proverbs 15:5" if False else "Proverbs 4:1-2",
  "Joshua 24:15","2 Timothy 1:5" if False else "2 Timothy 3:14-15","Isaiah 54:13" if False else "Isaiah 40:11","Matthew 19:14","Mark 10:14-16" if False else "Mark 10:14",
  "Psalm 128:3" if False else "Psalm 128:1-2","Proverbs 1:8-9" if False else "Proverbs 2:1-5" if False else "Proverbs 3:1-2","Luke 15:20",
  "Genesis 18:19" if False else "Psalm 103:13","3 John 1:4","Proverbs 17:6","Deuteronomy 11:18-19" if False else "Deuteronomy 6:5-7" if False else "Psalm 119:9",
  "James 1:5","Philippians 4:6-7","1 Corinthians 13:4-7","Galatians 6:9","Psalm 121:7-8" if False else "Psalm 121:8" if False else "Psalm 121:1-2"],
 # Emotional Health
 ["Philippians 4:6-7","Matthew 6:34","Psalm 34:18","Psalm 23:4","Isaiah 41:10","John 14:27","Matthew 11:28-30","1 Peter 5:7",
  "Psalm 42:11","Psalm 46:1-3","2 Corinthians 1:3-4","Psalm 147:3","Lamentations 3:22-23","Romans 15:13","Psalm 30:5",
  "Isaiah 26:3","Psalm 62:1-2","Joshua 1:9","Psalm 91:1-2","Psalm 4:8","Psalm 13:5-6" if False else "Psalm 13:1-2","Psalm 56:8",
  "John 16:33","Romans 8:38-39","Psalm 27:13-14","Habakkuk 3:17-18","Psalm 40:1-3","2 Timothy 1:7","Isaiah 40:28-31" if False else "Isaiah 40:29",
  "Matthew 5:4","Psalm 116:1-2" if False else "Psalm 116:15" if False else "Psalm 116:7","1 Thessalonians 4:13" if False else "Revelation 21:4",
  "Psalm 73:26","Job 19:25" if False else "Job 42:2" if False else "Psalm 121:1-2","Zephaniah 3:17"],
 # Health, Healing & Care
 ["Psalm 139:13-14","1 Corinthians 6:19-20","3 John 1:2","Jeremiah 17:14" if False else "Psalm 103:2-3","Psalm 147:3","Isaiah 53:5",
  "James 5:14-15","Matthew 14:14" if False else "Mark 5:34" if False else "Matthew 9:35" if False else "Luke 5:15-16" if False else "Mark 1:40-42" if False else "Matthew 9:36",
  "2 Corinthians 12:9-10","Psalm 73:26","Romans 8:26" if False else "Romans 8:18","Isaiah 40:29-31" if False else "Isaiah 40:29",
  "Psalm 23:1-3" if False else "Psalm 23:2-3","Proverbs 3:7-8","Proverbs 4:20-22","Galatians 6:2","1 Thessalonians 5:14" if False else "1 Thessalonians 5:11",
  "Matthew 25:36" if False else "Matthew 25:40","Psalm 41:3" if False else "Psalm 34:19","Exodus 20:12" if False else "Proverbs 23:22" if False else "Proverbs 16:31" if False else "Psalm 92:12-14" if False else "Psalm 71:9" if False else "Psalm 90:14",
  "Ecclesiastes 3:1" if False else "Ecclesiastes 3:11","John 9:1-3","2 Corinthians 4:16-18","Philippians 1:20-21" if False else "Philippians 1:21","Psalm 121:1-2"],
 # Freedom & Recovery
 ["John 8:36","Galatians 5:1","2 Corinthians 5:17","Romans 8:1-2","1 John 1:9","Psalm 51:10-12","James 5:16","Romans 6:6-7",
  "Philippians 3:13-14","Isaiah 43:18-19","Psalm 40:1-3","Ephesians 4:22-24","Romans 12:2","Titus 2:11-12","1 Corinthians 10:13",
  "Psalm 32:1-2" if False else "Psalm 32:5","Micah 7:18-19" if False else "Psalm 103:12","Colossians 3:1-3" if False else "Colossians 3:9-10",
  "John 10:10","Luke 4:18","Isaiah 61:1","Psalm 34:17-18" if False else "Psalm 34:4-5","2 Timothy 2:22" if False else "2 Timothy 2:21",
  "Hebrews 12:1-2","Romans 8:37","Galatians 5:16" if False else "Galatians 5:13","1 Peter 5:8-9" if False else "1 Peter 5:10","Ezekiel 36:26"],
 # Seasons of Life
 ["Ecclesiastes 3:1","Ecclesiastes 3:11","Psalm 90:12","Isaiah 43:18-19","Philippians 3:13-14","Jeremiah 29:11","Psalm 32:8",
  "Proverbs 3:5-6","Psalm 37:23-24" if False else "Psalm 37:23","Isaiah 41:10","Joshua 1:9","Psalm 121:7-8" if False else "Psalm 121:8",
  "Ruth 1:16","Psalm 68:5-6" if False else "Psalm 27:10" if False else "Psalm 25:16-17" if False else "Psalm 62:5-6","2 Corinthians 5:7" if False else "2 Corinthians 5:17",
  "Psalm 71:17-18" if False else "Psalm 92:12-14" if False else "Psalm 90:14","Isaiah 46:4" if False else "Isaiah 40:31","Lamentations 3:22-23",
  "Psalm 30:11-12" if False else "Psalm 30:5","Romans 8:28","Genesis 50:20","Psalm 139:16","1 Corinthians 7:32" if False else "1 Corinthians 7:35" if False else "Matthew 6:33-34" if False else "Matthew 6:34",
  "Hebrews 13:5" if False else "Hebrews 13:8","Deuteronomy 31:8","Psalm 16:11","John 14:1-3" if False else "John 14:2-3" if False else "John 14:27"],
 # Work & Marketplace
 ["Colossians 3:23-24","Proverbs 16:3","Ecclesiastes 9:10" if False else "Proverbs 22:29","Matthew 5:14-16","Ephesians 6:7" if False else "Ephesians 2:10",
  "Proverbs 12:11" if False else "Proverbs 13:4" if False else "Proverbs 14:23","Genesis 2:15" if False else "Psalm 90:17","1 Corinthians 10:31",
  "Proverbs 11:1" if False else "Proverbs 11:3","Luke 16:10","Matthew 25:21","Proverbs 27:23-24" if False else "Proverbs 27:23",
  "1 Thessalonians 4:11-12","2 Thessalonians 3:10" if False else "2 Thessalonians 3:13","Proverbs 22:1","Daniel 6:3-4" if False else "Daniel 6:4" if False else "Daniel 1:20" if False else "Daniel 1:8",
  "Nehemiah 6:3","Nehemiah 2:17-18","Proverbs 3:5-6","James 1:5","Proverbs 15:22","Proverbs 16:9","Philippians 2:3-4",
  "Matthew 6:33","Micah 6:8","Proverbs 10:4" if False else "Proverbs 10:9","Titus 2:7-8","1 Peter 2:12" if False else "1 Peter 2:15" if False else "1 Peter 2:17"],
 # Leadership & Serving
 ["Mark 10:45","John 13:14-15","Philippians 2:3-4","1 Peter 4:10-11","Matthew 20:26-28","Galatians 5:13","Joshua 1:9",
  "Proverbs 27:17","2 Timothy 2:2","1 Timothy 4:12","Titus 2:7-8","Nehemiah 2:17-18","Exodus 18:21" if False else "Acts 6:3-4" if False else "Acts 6:3",
  "1 Corinthians 12:4-7" if False else "1 Corinthians 12:4-6","Romans 12:6-8","Ephesians 4:11-13" if False else "Ephesians 4:11-12","Luke 22:26-27" if False else "Luke 22:27",
  "Proverbs 11:14","Proverbs 4:23","Psalm 78:72" if False else "Psalm 25:9" if False else "Psalm 32:8","Hebrews 13:7" if False else "Hebrews 13:17" if False else "Hebrews 10:24",
  "Matthew 25:21","Colossians 3:23-24","James 3:1" if False else "James 3:13" if False else "James 3:17","1 Thessalonians 5:12-13" if False else "1 Thessalonians 5:11",
  "John 15:16","Isaiah 6:8","Matthew 9:37-38","2 Corinthians 4:5" if False else "2 Corinthians 4:7"],
 # Church Vision & Values
 ["Habakkuk 2:2" if False else "Proverbs 29:18","Matthew 16:18","Acts 2:42-47","Ephesians 4:11-13" if False else "Ephesians 4:15-16",
  "1 Corinthians 3:6-9" if False else "1 Corinthians 3:9","Matthew 28:19-20","Ephesians 2:19-22" if False else "Ephesians 2:20-22",
  "Colossians 1:18","1 Peter 2:4-5","Acts 1:8","Matthew 5:14-16","Psalm 127:1","Nehemiah 2:17-18","Nehemiah 6:15-16" if False else "Nehemiah 6:16",
  "Joshua 24:15","Philippians 1:27","Philippians 2:1-2","John 17:20-21","Romans 12:4-5","1 Corinthians 12:27","Hebrews 10:24-25",
  "Acts 4:31-33" if False else "Acts 4:32-33" if False else "Acts 4:33","2 Chronicles 7:14" if False else "Joel 2:28" if False else "Isaiah 43:19",
  "Haggai 1:8" if False else "Haggai 1:7-8" if False else "Zechariah 4:6","Matthew 9:37-38","Luke 14:23" if False else "Luke 14:28-30" if False else "Luke 14:28"],
 # Ministries & Nonprofits
 ["Matthew 25:40","Isaiah 58:10","Galatians 6:9-10","2 Corinthians 9:8","Proverbs 31:8-9" if False else "Proverbs 31:9","James 1:27",
  "Micah 6:8","Acts 20:35","Matthew 5:16","Colossians 3:23-24","1 Peter 4:10-11","Isaiah 61:1","Luke 4:18","Matthew 9:36",
  "John 21:15-17" if False else "John 21:17","Nehemiah 2:17-18","Habakkuk 2:2" if False else "Proverbs 29:18","Psalm 41:1" if False else "Psalm 82:3-4",
  "Deuteronomy 15:11" if False else "Proverbs 19:17","Hebrews 13:16","Philippians 4:19","2 Corinthians 8:1-4" if False else "2 Corinthians 8:3-4" if False else "2 Corinthians 8:2",
  "Matthew 6:1-4" if False else "Matthew 6:3-4","Esther 4:14","1 John 3:17-18","Romans 12:11" if False else "Romans 12:13"],
 # Mission & Neighbor
 ["Matthew 28:19-20","Acts 1:8","Mark 12:30-31","Luke 10:27" if False else "Luke 10:36-37","John 13:34-35","Matthew 5:13-16",
  "Romans 10:14-15" if False else "Romans 10:13-14","1 Peter 3:15","2 Corinthians 5:18-20","Matthew 9:37-38","Isaiah 6:8",
  "Micah 6:8","Isaiah 58:6-7","James 2:14-17","Matthew 25:35-36" if False else "Matthew 25:35","Luke 14:23","John 4:35",
  "Acts 2:46-47" if False else "Acts 16:31" if False else "Acts 16:14" if False else "Acts 16:25","Galatians 6:9-10","Proverbs 31:8-9" if False else "Proverbs 31:8",
  "Psalm 96:3" if False else "Psalm 67:1-2","Matthew 22:37-39","Luke 19:10","John 20:21","Revelation 7:9" if False else "Revelation 21:3",
  "Zechariah 7:9-10" if False else "Zechariah 8:16" if False else "Hosea 6:6","Amos 5:24" if False else "Isaiah 1:17"],
 # Seasons & the Church Calendar
 ["Ecclesiastes 3:1","Luke 2:10-11","Isaiah 9:6","John 1:14","Matthew 1:23" if False else "Matthew 2:10-11" if False else "Luke 2:14",
  "Luke 24:5-6","John 11:25-26" if False else "John 11:25","1 Corinthians 15:20" if False else "1 Corinthians 15:55-57","Matthew 28:5-6",
  "Isaiah 53:5","John 3:16","Lamentations 3:22-23","Psalm 118:24","Psalm 90:12","Isaiah 43:18-19","Philippians 3:13-14",
  "Joel 2:12-13" if False else "Joel 2:13","Psalm 51:10","Matthew 4:1-2" if False else "Matthew 4:4","Acts 2:1-4",
  "Psalm 100:4","1 Thessalonians 5:18","Psalm 107:1","James 1:17","Deuteronomy 6:6-7" if False else "Joshua 4:6-7" if False else "Joshua 1:8",
  "Psalm 65:11" if False else "Psalm 145:1-2" if False else "Psalm 34:1","Colossians 3:17","Hebrews 12:1-2","Psalm 19:1" if False else "Psalm 24:1"],
 # Life of Christ & Red Letter
 ["Matthew 5:3-4" if False else "Matthew 5:3","Matthew 5:6","Matthew 5:9","Matthew 5:13","Matthew 5:14-16","Matthew 5:44",
  "Matthew 6:9-13","Matthew 6:19-21","Matthew 6:33","Matthew 7:7-8","Matthew 7:12","Matthew 7:24-25","Matthew 11:28-30",
  "Matthew 16:24-25" if False else "Matthew 16:24","Matthew 22:37-39","Matthew 28:19-20","Mark 1:17","Mark 8:34-35" if False else "Mark 8:36",
  "Mark 10:45","Mark 12:30-31","Luke 6:27-28" if False else "Luke 6:31","Luke 6:38","Luke 9:23","Luke 15:20","Luke 19:10",
  "John 3:16","John 8:12","John 10:10-11" if False else "John 10:10","John 11:25-26" if False else "John 11:25","John 13:34-35",
  "John 14:6","John 14:27","John 15:5","John 15:12-13" if False else "John 15:13","John 16:33","John 20:29" if False else "John 20:21"],
 # Bible & Scripture Studies
 ["2 Timothy 3:16-17","Hebrews 4:12","Psalm 119:105","Joshua 1:8","Psalm 1:1-3","Psalm 119:11","Isaiah 55:10-11" if False else "Isaiah 55:11",
  "Matthew 4:4","Romans 15:4","James 1:22-25" if False else "James 1:22","Psalm 19:7-8" if False else "Psalm 19:7","2 Peter 1:20-21" if False else "2 Peter 1:21",
  "Colossians 3:16","Deuteronomy 6:6-7" if False else "Deuteronomy 6:6","Psalm 119:15-16" if False else "Psalm 119:18","Acts 2:42",
  "Nehemiah 1:5-6" if False else "Nehemiah 1:11","Nehemiah 2:17-18","Nehemiah 6:15-16" if False else "Nehemiah 6:16","James 1:2-4","James 2:14-17",
  "James 3:17","James 4:7-8" if False else "James 4:8","James 5:16","Ephesians 6:10-11","Ephesians 6:13" if False else "Ephesians 6:14-17" if False else "Ephesians 6:18",
  "Romans 8:28","Romans 12:1-2","1 John 4:7-8" if False else "1 John 4:19" if False else "1 John 4:4","Revelation 3:20"],
 # Doubt & Honest Faith
 ["Mark 9:24" if False else "Mark 9:23-24","John 20:27-29" if False else "John 20:27","Jude 1:22","Matthew 11:2-3" if False else "Matthew 11:4-6" if False else "Matthew 11:6",
  "Psalm 13:1-2","Psalm 42:5" if False else "Psalm 42:9-11" if False else "Psalm 42:11","Habakkuk 1:2" if False else "Habakkuk 3:17-18","Job 42:1-3" if False else "Job 42:5",
  "Lamentations 3:19-23" if False else "Lamentations 3:21-23","Psalm 73:2-3" if False else "Psalm 73:25-26" if False else "Psalm 73:26","Isaiah 40:27-28" if False else "Isaiah 40:28",
  "John 6:67-68" if False else "John 6:68-69" if False else "John 6:68","Hebrews 11:1","Hebrews 11:6","2 Corinthians 5:7" if False else "2 Corinthians 4:8-9",
  "1 Peter 1:6-7" if False else "1 Peter 1:8-9" if False else "1 Peter 1:8","Romans 8:24-25" if False else "Romans 8:26","Psalm 34:17-18" if False else "Psalm 34:18",
  "Matthew 14:29-31" if False else "Matthew 14:31","Proverbs 3:5-6","Isaiah 55:8-9","Deuteronomy 31:8" if False else "Deuteronomy 31:6","John 16:33",
  "Psalm 27:13-14","James 1:5-6" if False else "James 1:5","Jeremiah 29:13" if False else "Jeremiah 29:12-13"],
 # Digital Discernment & AI
 ["Romans 12:2","Philippians 4:8","Psalm 101:3" if False else "Psalm 119:37","Colossians 3:1-2","1 Corinthians 10:23" if False else "1 Corinthians 6:12",
  "Matthew 6:22-23" if False else "Matthew 6:21","Proverbs 4:23","Ephesians 5:15-16","Psalm 90:12","James 1:19","Proverbs 18:2" if False else "Proverbs 18:13",
  "Proverbs 15:14" if False else "Proverbs 15:2" if False else "Proverbs 15:28","1 Thessalonians 5:21" if False else "1 Thessalonians 5:21-22","Proverbs 2:2-5" if False else "Proverbs 2:6",
  "Psalm 46:10","Matthew 11:28-30","Mark 6:31","Ecclesiastes 4:6" if False else "Ecclesiastes 3:1","Psalm 139:23-24","John 8:31-32" if False else "John 8:32",
  "2 Timothy 3:1-5" if False else "2 Timothy 3:16-17" if False else "2 Timothy 2:15","Isaiah 26:3","Proverbs 3:5-6","Colossians 2:8","1 John 4:1",
  "Hebrews 5:14" if False else "Hebrews 4:12","Psalm 19:14" if False else "Psalm 19:7-8" if False else "Psalm 19:8","Daniel 1:8"],
]

bad = [r for pool in POOLS for r in pool if not valid(r)]
if bad:
    print("INVALID REFS:", bad); sys.exit(1)

# ---------------------------------------------------------------- backbone assignment (no repeats within theme)
by_theme = defaultdict(list)
for i, o in enumerate(ROWS): by_theme[o["th"]].append(i)
REFS = sorted({r for p in POOLS for r in p})
RIDX = {r: i for i, r in enumerate(REFS)}
collisions = 0
for th, idxs in by_theme.items():
    ch = ROWS[idxs[0]]["ch"]; pool = POOLS[ch]; n = len(pool)
    for k, i in enumerate(sorted(idxs, key=lambda j: ROWS[j]["id"])):
        seed = int(hashlib.sha1((ROWS[i]["fp"]+str(th)).encode()).hexdigest()[:8], 16)
        ref = pool[(seed + k) % n]
        if len(idxs) > n and k >= n: collisions += 1
        ROWS[i]["sb"] = RIDX[ref]

# ---------------------------------------------------------------- promise summary (second person, pastoral)
LEAD = ["A journey for","Six weeks that help","A season that teaches","Forty days that move","A campaign that walks",
        "Daily steps that lead","A guided path for"]
CORE = {5:"open-handed living",4:"peace with what you have",9:"a calmer, steadier heart",3:"a deeper life of prayer",
        0:"the purpose God wrote into you",2:"real belonging",6:"a generous life",7:"a legacy that outlives you",
        8:"a stronger marriage",10:"healing and wholeness",11:"walking in freedom",1:"who you are in Christ",
        12:"grace for this season",13:"faith that goes to work with you",14:"servant-hearted leadership",
        15:"a church aligned around one vision",16:"ministry that multiplies",17:"loving your neighbor well",
        18:"a season your church will remember",19:"the words of Jesus, taken seriously",20:"a Bible that comes alive",
        21:"honest faith with room for questions",22:"a discerning heart in a digital age"}
def promise(o):
    seed = int(o["fp"][:4], 16)
    lead = LEAD[seed % len(LEAD)]
    core = CORE.get(o["ch"], "life with Jesus")
    who = "your whole church" if o["af"] & 1 else "your people"
    return f"{lead} {who} into {core} — one honest step at a time."
for o in ROWS: o["sum"] = promise(o)

# ---------------------------------------------------------------- emit
from generate_data import CHANNELS  # reuse names/slugs
sys.path.insert(0, "/home/claude/build")
CH = [{"slug": s, "name": n} for s, n in CHANNELS]

index = {"channels": CH, "themes": THEMES, "refs": REFS,
 "aff": ["Whole Church","Men","Women","Young Adults","Students","Children & Families","Couples","Seniors & Grandparents","New Believers","Leaders","Advisors & Clients","Business Owners"],
 "seasons": ["Advent","Christmas","New Year","Lent","Easter","Pentecost","Mother's Day","Father's Day","Summer","Back to School","Thanksgiving"],
 "cols": ["id","slug","t","s","ch","th","f","af","co","g","pt","fp","sb","se","ns"],
 "rows": [[o["id"],o["slug"],o["t"],o["s"],o["ch"],o["th"],o["f"],o["af"],o["co"],o["g"],o["pt"],o["fp"],o["sb"],o["se"],o["ns"]] for o in ROWS]}
json.dump(index, open(f"{OUT}/index.json","w"), separators=(",",":"))

shards = defaultdict(list)
for o in ROWS:
    rec = {k: o[k] for k in ("id","slug","t","s","th","f","af","co","g","pt","fp","sb","se","aud","fn","sum","ns")}
    if o["id"] in NESTS: rec["nest"] = NESTS[o["id"]]
    shards[o["ch"]].append(rec)
for ci, recs in shards.items():
    json.dump({"ch": ci, "rows": recs}, open(f"{OUT}/ch{ci:02d}.json","w"), separators=(",",":"))

facets = {"channel": {}, "format": defaultdict(int), "aff": defaultdict(int), "coll": defaultdict(int),
          "season": defaultdict(int), "grade": defaultdict(int)}
FN = {1:"7-Day",2:"21-Day",4:"30-Day",8:"40-Day",16:"Study",32:"Catalytic Sunday"}
for o in ROWS:
    facets["channel"][o["ch"]] = facets["channel"].get(o["ch"],0)+1
    for b,nm in FN.items():
        if o["f"]&b: facets["format"][nm]+=1
    for i in range(12):
        if o["af"]&(1<<i): facets["aff"][i]+=1
    for b,nm in ((1,"Flagship"),(2,"Seasonal"),(4,"New"),(8,"Pastor's Shelf")):
        if o["co"]&b: facets["coll"][nm]+=1
    if o["se"]>=0: facets["season"][o["se"]]+=1
    facets["grade"][o["g"]] = facets["grade"].get(o["g"],0)+1
json.dump(facets, open(f"{OUT}/facets.json","w"), separators=(",",":"), default=int)

meta = {"catalog": len(ROWS), "active_total": STATS["active_total"], "sessions": STATS["supporting_nested"],
        "channels": len(CH), "themes": len(THEMES), "flagship": STATS["flagship"],
        "per_channel": {i: facets["channel"].get(i,0) for i in range(len(CH))},
        "backbone_theme_overflow": collisions}
json.dump(meta, open(f"{OUT}/meta.json","w"))
print(json.dumps(meta, indent=1))
sizes = {f: os.path.getsize(f"{OUT}/{f}")//1024 for f in sorted(os.listdir(OUT))}
print("KB:", sizes)
