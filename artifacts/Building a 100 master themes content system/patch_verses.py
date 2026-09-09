# -*- coding: utf-8 -*-
import json

KV = {
"Ephesians 2:10":("Ephesians 2:10","For we are his workmanship, created in Christ Jesus unto good works, which God hath before ordained that we should walk in them."),
"1 Peter 2:9":("1 Peter 2:9","But ye are a chosen generation, a royal priesthood, an holy nation, a peculiar people; that ye should shew forth the praises of him who hath called you out of darkness into his marvellous light:"),
"Psalm 139:13-14":("Psalm 139:14","I will praise thee; for I am fearfully and wonderfully made: marvellous are thy works; and that my soul knoweth right well."),
"Jeremiah 29:11":("Jeremiah 29:11","For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end."),
"Romans 12:6-8":("Romans 12:6","Having then gifts differing according to the grace that is given to us, whether prophecy, let us prophesy according to the proportion of faith;"),
"John 14:27":("John 14:27","Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled, neither let it be afraid."),
"Psalm 16:8":("Psalm 16:8","I have set the LORD always before me: because he is at my right hand, I shall not be moved."),
"Matthew 11:28-30":("Matthew 11:28","Come unto me, all ye that labour and are heavy laden, and I will give you rest."),
"Isaiah 41:10":("Isaiah 41:10","Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness."),
"Philippians 4:6-7":("Philippians 4:6","Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God."),
"1 Corinthians 13:4-7":("1 Corinthians 13:4","Charity suffereth long, and is kind; charity envieth not; charity vaunteth not itself, is not puffed up,"),
"Ecclesiastes 4:9-12":("Ecclesiastes 4:9","Two are better than one; because they have a good reward for their labour."),
"Malachi 2:14-15":("Malachi 2:15","And did not he make one? Yet had he the residue of the spirit. And wherefore one? That he might seek a godly seed. Therefore take heed to your spirit, and let none deal treacherously against the wife of his youth."),
"Song of Songs 8:6-7":("Song of Songs 8:7","Many waters cannot quench love, neither can the floods drown it: if a man would give all the substance of his house for love, it would utterly be contemned."),
"James 1:19":("James 1:19","Wherefore, my beloved brethren, let every man be swift to hear, slow to speak, slow to wrath:"),
"Psalm 78:4-7":("Psalm 78:4","We will not hide them from their children, shewing to the generation to come the praises of the LORD, and his strength, and his wonderful works that he hath done."),
"Deuteronomy 6:6-7":("Deuteronomy 6:7","And thou shalt teach them diligently unto thy children, and shalt talk of them when thou sittest in thine house, and when thou walkest by the way, and when thou liest down, and when thou risest up."),
"Proverbs 22:6":("Proverbs 22:6","Train up a child in the way he should go: and when he is old, he will not depart from it."),
"Psalm 71:18":("Psalm 71:18","Now also when I am old and grayheaded, O God, forsake me not; until I have shewed thy strength unto this generation, and thy power to every one that is to come."),
"Joshua 24:15":("Joshua 24:15","Choose you this day whom ye will serve\u2026 but as for me and my house, we will serve the LORD."),
"Psalm 24:1":("Psalm 24:1","The earth is the LORD\u2019s, and the fulness thereof; the world, and they that dwell therein."),
"Proverbs 3:9-10":("Proverbs 3:9","Honour the LORD with thy substance, and with the firstfruits of all thine increase:"),
"Proverbs 21:5":("Proverbs 21:5","The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want."),
"Philippians 4:11-13":("Philippians 4:11","Not that I speak in respect of want: for I have learned, in whatsoever state I am, therewith to be content."),
"Matthew 6:33":("Matthew 6:33","But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you."),
"2 Corinthians 9:6-7":("2 Corinthians 9:7","Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver."),
"Acts 20:35":("Acts 20:35","\u2026remember the words of the Lord Jesus, how he said, It is more blessed to give than to receive."),
"Matthew 6:19-21":("Matthew 6:21","For where your treasure is, there will your heart be also."),
"Proverbs 3:9":("Proverbs 3:9","Honour the LORD with thy substance, and with the firstfruits of all thine increase:"),
"Malachi 3:10":("Malachi 3:10","Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts, if I will not open you the windows of heaven, and pour you out a blessing, that there shall not be room enough to receive it."),
"Luke 9:23":("Luke 9:23","And he said to them all, If any man will come after me, let him deny himself, and take up his cross daily, and follow me."),
"Colossians 2:6-7":("Colossians 2:6","As ye have therefore received Christ Jesus the Lord, so walk ye in him:"),
"John 15:4-5":("John 15:5","I am the vine, ye are the branches: He that abideth in me, and I in him, the same bringeth forth much fruit: for without me ye can do nothing."),
"Matthew 11:29":("Matthew 11:29","Take my yoke upon you, and learn of me; for I am meek and lowly in heart: and ye shall find rest unto your souls."),
"1 Timothy 4:7-8":("1 Timothy 4:8","For bodily exercise profiteth little: but godliness is profitable unto all things, having promise of the life that now is, and of that which is to come."),
"Ecclesiastes 4:9-10":("Ecclesiastes 4:10","For if they fall, the one will lift up his fellow: but woe to him that is alone when he falleth; for he hath not another to help him up."),
"Romans 12:5":("Romans 12:5","So we, being many, are one body in Christ, and every one members one of another."),
"Hebrews 10:24-25":("Hebrews 10:24","And let us consider one another to provoke unto love and to good works:"),
"John 13:34-35":("John 13:34","A new commandment I give unto you, That ye love one another; as I have loved you, that ye also love one another."),
"Acts 2:42-47":("Acts 2:42","And they continued stedfastly in the apostles\u2019 doctrine and fellowship, and in breaking of bread, and in prayers."),
"Romans 15:13":("Romans 15:13","Now the God of hope fill you with all joy and peace in believing, that ye may abound in hope, through the power of the Holy Ghost."),
"2 Corinthians 4:8-9":("2 Corinthians 4:8-9","We are troubled on every side, yet not distressed; we are perplexed, but not in despair; persecuted, but not forsaken; cast down, but not destroyed;"),
"Romans 8:28":("Romans 8:28","And we know that all things work together for good to them that love God, to them who are the called according to his purpose."),
"Psalm 34:18":("Psalm 34:18","The LORD is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit."),
"Proverbs 3:5-6":("Proverbs 3:5-6","Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths."),
"John 20:21":("John 20:21","Then said Jesus to them again, Peace be unto you: as my Father hath sent me, even so send I you."),
"Jeremiah 29:7":("Jeremiah 29:7","And seek the peace of the city whither I have caused you to be carried away captives, and pray unto the LORD for it: for in the peace thereof shall ye have peace."),
"Luke 10:27":("Luke 10:27","Thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy strength, and with all thy mind; and thy neighbour as thyself."),
"Matthew 16:26":("Matthew 16:26","For what is a man profited, if he shall gain the whole world, and lose his own soul? or what shall a man give in exchange for his soul?"),
"2 Timothy 4:7":("2 Timothy 4:7","I have fought a good fight, I have finished my course, I have kept the faith:"),
"1 Peter 4:10":("1 Peter 4:10","As every man hath received the gift, even so minister the same one to another, as good stewards of the manifold grace of God."),
"Luke 12:6-7":("Luke 12:7","But even the very hairs of your head are all numbered. Fear not therefore: ye are of more value than many sparrows."),
"Psalm 32:8":("Psalm 32:8","I will instruct thee and teach thee in the way which thou shalt go: I will guide thee with mine eye."),
"Habakkuk 2:2-3":("Habakkuk 2:2","And the LORD answered me, and said, Write the vision, and make it plain upon tables, that he may run that readeth it."),
"Isaiah 43:18-19":("Isaiah 43:19","Behold, I will do a new thing; now it shall spring forth; shall ye not know it? I will even make a way in the wilderness, and rivers in the desert."),
"Nehemiah 8:10":("Nehemiah 8:10","\u2026neither be ye sorry; for the joy of the LORD is your strength."),
"1 Thessalonians 5:18":("1 Thessalonians 5:18","In every thing give thanks: for this is the will of God in Christ Jesus concerning you."),
"Psalm 46:10":("Psalm 46:10","Be still, and know that I am God: I will be exalted among the heathen, I will be exalted in the earth."),
"Psalm 118:5":("Psalm 118:5","I called upon the LORD in distress: the LORD answered me, and set me in a large place."),
"Psalm 147:3":("Psalm 147:3","He healeth the broken in heart, and bindeth up their wounds."),
"Colossians 3:13":("Colossians 3:13","Forbearing one another, and forgiving one another, if any man have a quarrel against any: even as Christ forgave you, so also do ye."),
"Genesis 2:24-25":("Genesis 2:24","Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh."),
"Proverbs 4:23":("Proverbs 4:23","Keep thy heart with all diligence; for out of it are the issues of life."),
"Proverbs 17:17":("Proverbs 17:17","A friend loveth at all times, and a brother is born for adversity."),
"Matthew 5:23-24":("Matthew 5:24","Leave there thy gift before the altar, and go thy way; first be reconciled to thy brother, and then come and offer thy gift."),
"Ephesians 4:2-3":("Ephesians 4:2-3","With all lowliness and meekness, with longsuffering, forbearing one another in love; endeavouring to keep the unity of the Spirit in the bond of peace."),
"Psalm 127:4":("Psalm 127:4","As arrows are in the hand of a mighty man; so are children of the youth."),
"Deuteronomy 11:18-19":("Deuteronomy 11:19","And ye shall teach them your children, speaking of them when thou sittest in thine house, and when thou walkest by the way, when thou liest down, and when thou risest up."),
"Exodus 20:12":("Exodus 20:12","Honour thy father and thy mother: that thy days may be long upon the land which the LORD thy God giveth thee."),
"Ecclesiastes 3:1":("Ecclesiastes 3:1","To every thing there is a season, and a time to every purpose under the heaven:"),
"Proverbs 22:7":("Proverbs 22:7","The rich ruleth over the poor, and the borrower is servant to the lender."),
"Philippians 4:19":("Philippians 4:19","But my God shall supply all your need according to his riches in glory by Christ Jesus."),
"Proverbs 21:20":("Proverbs 21:20","There is treasure to be desired and oil in the dwelling of the wise; but a foolish man spendeth it up."),
"Amos 3:3":("Amos 3:3","Can two walk together, except they be agreed?"),
"2 Samuel 24:24":("2 Samuel 24:24","\u2026Nay; but I will surely buy it of thee at a price: neither will I offer burnt offerings unto the LORD my God of that which doth cost me nothing."),
"Mark 10:45":("Mark 10:45","For even the Son of man came not to be ministered unto, but to minister, and to give his life a ransom for many."),
"Romans 12:13":("Romans 12:13","Distributing to the necessity of saints; given to hospitality."),
"Ephesians 5:15-16":("Ephesians 5:15-16","See then that ye walk circumspectly, not as fools, but as wise, redeeming the time, because the days are evil."),
"1 Thessalonians 5:17":("1 Thessalonians 5:17","Pray without ceasing."),
"Psalm 119:105":("Psalm 119:105","Thy word is a lamp unto my feet, and a light unto my path."),
"Psalm 95:6":("Psalm 95:6","O come, let us worship and bow down: let us kneel before the LORD our maker."),
"John 14:26":("John 14:26","But the Comforter, which is the Holy Ghost, whom the Father will send in my name, he shall teach you all things, and bring all things to your remembrance, whatsoever I have said unto you."),
"John 14:15":("John 14:15","If ye love me, keep my commandments."),
"2 Timothy 2:2":("2 Timothy 2:2","And the things that thou hast heard of me among many witnesses, the same commit thou to faithful men, who shall be able to teach others also."),
"John 17:21":("John 17:21","That they all may be one; as thou, Father, art in me, and I in thee, that they also may be one in us: that the world may believe that thou hast sent me."),
"Luke 24:30-31":("Luke 24:30-31","And it came to pass, as he sat at meat with them, he took bread, and blessed it, and brake, and gave to them. And their eyes were opened, and they knew him;"),
"Hebrews 3:13":("Hebrews 3:13","But exhort one another daily, while it is called To day; lest any of you be hardened through the deceitfulness of sin."),
"James 5:16":("James 5:16","Confess your faults one to another, and pray one for another, that ye may be healed. The effectual fervent prayer of a righteous man availeth much."),
"Psalm 27:14":("Psalm 27:14","Wait on the LORD: be of good courage, and he shall strengthen thine heart: wait, I say, on the LORD."),
"Galatians 6:9":("Galatians 6:9","And let us not be weary in well doing: for in due season we shall reap, if we faint not."),
"2 Corinthians 1:3-4":("2 Corinthians 1:3-4","Blessed be God, even the Father of our Lord Jesus Christ, the Father of mercies, and the God of all comfort; who comforteth us in all our tribulation, that we may be able to comfort them which are in any trouble, by the comfort wherewith we ourselves are comforted of God."),
"Joel 2:25":("Joel 2:25","And I will restore to you the years that the locust hath eaten, the cankerworm, and the caterpiller, and the palmerworm, my great army which I sent among you."),
"Psalm 46:1":("Psalm 46:1","God is our refuge and strength, a very present help in trouble."),
"1 Peter 3:15":("1 Peter 3:15","But sanctify the Lord God in your hearts: and be ready always to give an answer to every man that asketh you a reason of the hope that is in you with meekness and fear:"),
"Micah 6:8":("Micah 6:8","He hath shewed thee, O man, what is good; and what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?"),
"Matthew 9:36":("Matthew 9:36","But when he saw the multitudes, he was moved with compassion on them, because they fainted, and were scattered abroad, as sheep having no shepherd."),
"Revelation 12:11":("Revelation 12:11","And they overcame him by the blood of the Lamb, and by the word of their testimony; and they loved not their lives unto the death."),
"Matthew 28:19-20":("Matthew 28:19","Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost:"),
# universal bank
"Psalm 23:1-6":("Psalm 23:1","The LORD is my shepherd; I shall not want."),
"Psalm 46:1-3":("Psalm 46:1","God is our refuge and strength, a very present help in trouble."),
"Psalm 62:5-8":("Psalm 62:5","My soul, wait thou only upon God; for my expectation is from him."),
"Psalm 103:1-5":("Psalm 103:1","Bless the LORD, O my soul: and all that is within me, bless his holy name."),
"Psalm 121:1-8":("Psalm 121:1-2","I will lift up mine eyes unto the hills, from whence cometh my help. My help cometh from the LORD, which made heaven and earth."),
"Psalm 139:1-10":("Psalm 139:1","O LORD, thou hast searched me, and known me."),
"Isaiah 40:28-31":("Isaiah 40:31","But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint."),
"Lamentations 3:22-24":("Lamentations 3:22-23","It is of the LORD\u2019s mercies that we are not consumed, because his compassions fail not. They are new every morning: great is thy faithfulness."),
"Romans 8:28-32":("Romans 8:28","And we know that all things work together for good to them that love God, to them who are the called according to his purpose."),
"Romans 12:1-2":("Romans 12:2","And be not conformed to this world: but be ye transformed by the renewing of your mind, that ye may prove what is that good, and acceptable, and perfect, will of God."),
"2 Corinthians 12:9-10":("2 Corinthians 12:9","My grace is sufficient for thee: for my strength is made perfect in weakness."),
"Philippians 1:6":("Philippians 1:6","Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ:"),
"Colossians 3:1-4":("Colossians 3:2","Set your affection on things above, not on things on the earth."),
"Hebrews 12:1-3":("Hebrews 12:1","Wherefore seeing we also are compassed about with so great a cloud of witnesses, let us lay aside every weight, and the sin which doth so easily beset us, and let us run with patience the race that is set before us,"),
"James 1:2-5":("James 1:2-3","My brethren, count it all joy when ye fall into divers temptations; knowing this, that the trying of your faith worketh patience."),
"1 Peter 5:6-7":("1 Peter 5:7","Casting all your care upon him; for he careth for you."),
}

O='/home/claude/site/out/'
kvjs={k:{'v':v[0],'t':v[1]} for k,v in KV.items()}

# ---- patch engine.js ----
e=open(O+'engine.js').read()
e=e.replace("/* ---------- public API ---------- */",
"/* ---------- verse text: KJV (public domain) key verses; swaps to NIV under Biblica license at launch ---------- */\nconst KV="+json.dumps(kvjs,ensure_ascii=False)+";\nfunction memFor(c,m,ph){ // weekly memory verse: week 1 = theme anchor, weeks 2-6 rotate the universal set\n  if(ph===0 && KV[m.scr]) return KV[m.scr];\n  const keys=Object.keys(KV).slice(-16);\n  return KV[keys[(seedFrom(c[9])+ph*3)%16]];\n}\n\n/* ---------- public API ---------- */")

# devotional days get mem
e=e.replace("days.push({ph, n:d, dn:'Day '+String(d).padStart(2,'0'),",
"const mem=memFor(c,m,ph);\n    days.push({ph, n:d, mem, dn:'Day '+String(d).padStart(2,'0'),")

# group sessions get mem
e=e.replace("return {n:i+1, title:'Session '+(i+1)+': '+a.t, focus:'This session is about '+a.f+'.',",
"return {n:i+1, mem:memFor(c,m,i), title:'Session '+(i+1)+': '+a.t, focus:'This session is about '+a.f+'.',")
open(O+'engine.js','w').write(e)

# ---- patch sample.html & curriculum.html day render: add memory-verse block with actual text ----
MEMBLOCK='''<div class="dscr" style="background:#F2F6FB;border-left-color:#4F86E0;color:#26417F;text-transform:none;letter-spacing:0;font-weight:400;font-family:Georgia,serif;font-size:14.5px;font-style:italic;">\u201C${d.mem.t}\u201D<div style="font-family:'Hanken Grotesk';font-style:normal;font-weight:800;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;">This week\u2019s memory verse \u00b7 ${d.mem.v} (KJV)</div></div>
 '''
for f in ('sample.html','curriculum.html'):
    h=open(O+f).read()
    h=h.replace('<div class="dscr">Today\\u2019s reading: ${d.scr}</div>',
                MEMBLOCK+'<div class="dscr">Today\\u2019s reading: ${d.scr}</div>')
    # session memory verse (curriculum only; harmless if absent)
    h=h.replace("<div class=\"dlbl\">Read together</div><p>${s.refs.join(' · ')}</p>",
      "<div class=\"dscr\" style=\"background:#F2F6FB;border-left-color:#4F86E0;color:#26417F;text-transform:none;letter-spacing:0;font-weight:400;font-family:Georgia,serif;font-size:14.5px;font-style:italic;\">\\u201C${s.mem.t}\\u201D<div style=\"font-family:'Hanken Grotesk';font-style:normal;font-weight:800;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;margin-top:6px;\">This week\\u2019s memory verse \\u00b7 ${s.mem.v} (KJV)</div></div><div class=\"dlbl\">Read together</div><p>${s.refs.join(' · ')}</p>")
    # attribution footer note
    h=h.replace('SCRIPTURE REFERENCES NIV','MEMORY VERSES KJV (PUBLIC DOMAIN) \u00b7 DAILY READING REFERENCES NIV \u2014 NIV TEXT SHIPS UNDER THE BIBLICA LICENSE AT LAUNCH')
    h=h.replace('40DAYCAMPAIGNS.COM</div>','40DAYCAMPAIGNS.COM<br>MEMORY VERSES SHOWN IN THE KING JAMES VERSION (PUBLIC DOMAIN); DAILY READING REFERENCES NIV \u2014 FULL NIV TEXT SHIPS UNDER THE BIBLICA LICENSE AT LAUNCH</div>') if f=='sample.html' else h
    open(O+f,'w').write(h)

# ---- campaign.html preview: show actual memory verse text ----
h=open(O+'campaign.html').read()
h=h.replace("v:'Read today\\u2019s passage slowly, twice.',r:d.scr,",
            "v:'\\u201C'+d.mem.t+'\\u201D',r:'Memory verse \\u00b7 '+d.mem.v+' (KJV) \\u00b7 Today\\u2019s reading: '+d.scr,")
open(O+'campaign.html','w').write(h)

# ---- index stats: exactly as requested ----
h=open(O+'index.html').read()
h=h.replace('10,000+ campaigns \u00b7 100 themes \u00b7 10 categories','10,000 campaigns \u00b7 100 categories \u00b7 10 themes')
h=h.replace('10,000+ campaigns · 100 themes · 10 categories','10,000 campaigns · 100 categories · 10 themes')
open(O+'index.html','w').write(h)

# ---- browse: drop One-Year option ----
h=open(O+'browse.html').read()
h=h.replace(",['One-Year','One-Year']","")
open(O+'browse.html','w').write(h)
print('patched: engine KV(%d refs), sample, curriculum, campaign preview, index stats, browse One-Year removed'%len(KV))
