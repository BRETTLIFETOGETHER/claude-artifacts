import re, json

# ---------- lexicon ----------
# entry: surface EN -> (es, pt, flags) flags: n=noun m/f gender tag after, a=adjective (postpose+agree), g=gerund head, p=preposition/function, k=keep
L = {
 # function words
 "of":("de","de","p"),"the":("el","o","art"),"The":("El","O","art"),"for":("para","para","p"),"with":("con","com","p"),
 "and":("y","e","p"),"to":("para","para","p"),"in":("en","em","p"),"at":("en","em","p"),"on":("sobre","sobre","p"),
 "from":("desde","desde","p"),"by":("por","por","p"),"into":("hacia","para","p"),"as":("como","como","p"),
 "that":("que","que","p"),"That":("que","que","p"),"Through":("a trav\u00e9s de","atrav\u00e9s de","p"),"through":("a trav\u00e9s de","atrav\u00e9s de","p"),
 "Beyond":("m\u00e1s all\u00e1 de","al\u00e9m de","p"),"Before":("antes de","antes de","p"),"After":("despu\u00e9s de","depois de","p"),
 "Without":("sin","sem","p"),"Together":("juntos","juntos","x"),"Every":("cada","cada","p"),"every":("cada","cada","p"),
 "More":("m\u00e1s","mais","x"),"Than":("que","que","p"),"than":("que","que","p"),"Most":("m\u00e1s","mais","x"),
 "Your":("tu","sua","p"),"your":("tu","sua","p"),"Our":("nuestra","nossa","p"),"You":("t\u00fa","voc\u00ea","x"),
 "What":("lo que","o que","p"),"What's":("lo que","o que","p"),"Who":("quien","quem","p"),"Why":("por qu\u00e9","por que","p"),
 "How":("c\u00f3mo","como","p"),"When":("cuando","quando","p"),"Where":("donde","onde","p"),"While":("mientras","enquanto","p"),
 "Is":("es","\u00e9","x"),"is":("es","\u00e9","x"),"Are":("son","s\u00e3o","x"),"Not":("no","n\u00e3o","x"),"Never":("nunca","nunca","x"),
 "One":("uno","um","x"),"one":("un","um","x"),"Us":("nosotros","n\u00f3s","x"),"We":("nosotros","n\u00f3s","x"),
 "It":("","","drop"),"This":("este","este","p"),"Has":("tiene","tem","x"),"Do":("","","drop"),"Be":("ser","ser","x"),
 "All":("todo","tudo","x"),"Just":("solo","s\u00f3","x"),"Here":("aqu\u00ed","aqui","x"),"Out":("","","drop"),
 "an":("un","um","p"),"A":("Un","Um","art"),"a":("un","um","p"),"Over":("sobre","sobre","p"),"Under":("bajo","sob","p"),
 "Their":("su","seu","p"),"His":("su","seu","p"),"Them":("ellos","eles","x"),"Else":("m\u00e1s","mais","x"),
 "Down":("","","drop"),"Go":("ir","ir","x"),"Well":("bien","bem","x"),"Much":("mucho","muito","x"),
 "Enough":("suficiente","suficiente","x"),"Other":("otra","outra","x"),"Ahead":("por delante","adiante","x"),
 "Back":("de vuelta","de volta","x"),"Alone":("solos","sozinhos","x"),"Toward":("hacia","rumo a","p"),
 "Today":("hoy","hoje","x"),"Today's":("de hoy","de hoje","pos"),"Tomorrow":("ma\u00f1ana","amanh\u00e3","x"),
 "Tomorrow's":("del ma\u00f1ana","do amanh\u00e3","pos"),"Forever":("para siempre","para sempre","x"),
 # possessives handled by rule: "God's" etc via 's detection with these lemmas:
 # core nouns (gender: es;pt often same)
 "Family":("familia","fam\u00edlia","nf"),"Families":("familias","fam\u00edlias","nf"),"Days":("d\u00edas","dias","nm"),"Day":("d\u00eda","dia","nm"),
 "Legacy":("legado","legado","nm"),"Life":("vida","vida","nf"),"Faith":("fe","f\u00e9","nf"),"God":("Dios","Deus","nm"),
 "Purpose":("prop\u00f3sito","prop\u00f3sito","nm"),"Wisdom":("sabidur\u00eda","sabedoria","nf"),"Stewardship":("mayordom\u00eda","mordomia","nf"),
 "Wealth":("riqueza","riqueza","nf"),"Kingdom":("Reino","Reino","nm"),"Journey":("recorrido","jornada","nm;f"),
 "Christ":("Cristo","Cristo","nm"),"Jesus":("Jes\u00fas","Jesus","nm"),"Seven":("siete","sete","x"),
 "Generations":("generaciones","gera\u00e7\u00f5es","nf"),"Generation":("generaci\u00f3n","gera\u00e7\u00e3o","nf"),
 "Influence":("influencia","influ\u00eancia","nf"),"Work":("trabajo","trabalho","nm"),"Generosity":("generosidad","generosidade","nf"),
 "Mission":("misi\u00f3n","miss\u00e3o","nf"),"Future":("futuro","futuro","nm"),"Impact":("impacto","impacto","nm"),
 "Joy":("gozo","alegria","nm;f"),"Business":("negocio","neg\u00f3cio","nm"),"Peace":("paz","paz","nf"),"Trust":("confianza","confian\u00e7a","nf"),
 "Leadership":("liderazgo","lideran\u00e7a","nm;f"),"Love":("amor","amor","nm"),"Money":("dinero","dinheiro","nm"),
 "Calling":("llamado","chamado","nm"),"Hope":("esperanza","esperan\u00e7a","nf"),"Home":("hogar","lar","nm"),
 "Marriage":("matrimonio","casamento","nm"),"Season":("temporada","temporada","nf"),"Vision":("visi\u00f3n","vis\u00e3o","nf"),
 "Children":("hijos","filhos","nm"),"Grace":("gracia","gra\u00e7a","nf"),"Heart":("coraz\u00f3n","cora\u00e7\u00e3o","nm"),
 "Hearts":("corazones","cora\u00e7\u00f5es","nm"),"Blessing":("bendici\u00f3n","b\u00ean\u00e7\u00e3o","nf"),"Blessings":("bendiciones","b\u00ean\u00e7\u00e3os","nf"),
 "Conversations":("conversaciones","conversas","nf"),"Conversation":("conversaci\u00f3n","conversa","nf"),
 "Resources":("recursos","recursos","nm"),"Resource":("recurso","recurso","nm"),"Success":("\u00e9xito","sucesso","nm"),
 "Values":("valores","valores","nm"),"Character":("car\u00e1cter","car\u00e1ter","nm"),"Way":("camino","caminho","nm"),
 "Decisions":("decisiones","decis\u00f5es","nf"),"Decision":("decisi\u00f3n","decis\u00e3o","nf"),"Story":("historia","hist\u00f3ria","nf"),
 "Stories":("historias","hist\u00f3rias","nf"),"Unity":("unidad","unidade","nf"),"Relationships":("relaciones","relacionamentos","nf;m"),
 "Relationship":("relaci\u00f3n","relacionamento","nf;m"),"Time":("tiempo","tempo","nm"),"Estate":("patrimonio","patrim\u00f4nio","nm"),
 "Inheritance":("herencia","heran\u00e7a","nf"),"Courage":("valent\u00eda","coragem","nf"),"Prayer":("oraci\u00f3n","ora\u00e7\u00e3o","nf"),
 "Fear":("miedo","medo","nm"),"Habits":("h\u00e1bitos","h\u00e1bitos","nm"),"Freedom":("libertad","liberdade","nf"),
 "Culture":("cultura","cultura","nf"),"Lifetime":("vida","vida","nf"),"Heirs":("herederos","herdeiros","nm"),
 "Gifts":("dones","dons","nm"),"Gift":("don","dom","nm"),"Responsibility":("responsabilidad","responsabilidade","nf"),
 "Confidence":("confianza","confian\u00e7a","nf"),"Plan":("plan","plano","nm"),"Compassion":("compasi\u00f3n","compaix\u00e3o","nf"),
 "Assets":("bienes","bens","nm"),"Commission":("comisi\u00f3n","comiss\u00e3o","nf"),"Community":("comunidad","comunidade","nf"),
 "Leaders":("l\u00edderes","l\u00edderes","nm"),"Leader":("l\u00edder","l\u00edder","nm"),"Conflict":("conflicto","conflito","nm"),
 "Years":("a\u00f1os","anos","nm"),"Year":("a\u00f1o","ano","nm"),"Foundations":("fundamentos","fundamentos","nm"),
 "Foundation":("fundamento","fundamento","nm"),"Transition":("transici\u00f3n","transi\u00e7\u00e3o","nf"),"Second":("segunda","segunda","a"),
 "Faithfulness":("fidelidad","fidelidade","nf"),"Strength":("fortaleza","for\u00e7a","nf"),"Ownership":("pertenencia a Dios","pertencimento a Deus","nm"),
 "Soul":("alma","alma","nf"),"Hands":("manos","m\u00e3os","nf"),"Abundance":("abundancia","abund\u00e2ncia","nf"),
 "Finances":("finanzas","finan\u00e7as","nf"),"Health":("salud","sa\u00fade","nf"),"Covenant":("pacto","alian\u00e7a","nm;f"),
 "Church":("iglesia","igreja","nf"),"Will":("voluntad","vontade","nf"),"Ministry":("ministerio","minist\u00e9rio","nm"),
 "Step":("paso","passo","nm"),"Growth":("crecimiento","crescimento","nm"),"Marketplace":("mundo laboral","mercado","nm"),
 "Truth":("verdad","verdade","nf"),"People":("personas","pessoas","nf"),"Body":("cuerpo","corpo","nm"),
 "Contentment":("contentamiento","contentamento","nm"),"World":("mundo","mundo","nm"),"Steward":("mayordomo","mordomo","nm"),
 "Stewards":("mayordomos","mordomos","nm"),"Table":("mesa","mesa","nf"),"Heritage":("herencia","heran\u00e7a","nf"),
 "Path":("camino","caminho","nm"),"Circumstances":("circunstancias","circunst\u00e2ncias","nf"),"Chapter":("cap\u00edtulo","cap\u00edtulo","nm"),
 "Change":("cambio","mudan\u00e7a","nm;f"),"Obedience":("obediencia","obedi\u00eancia","nf"),"Clarity":("claridad","clareza","nf"),
 "Humility":("humildad","humildade","nf"),"Treasure":("tesoro","tesouro","nm"),"Honor":("honra","honra","nf"),
 "Mind":("mente","mente","nf"),"Pressure":("presi\u00f3n","press\u00e3o","nf"),"Gratitude":("gratitud","gratid\u00e3o","nf"),
 "Eternity":("eternidad","eternidade","nf"),"Household":("hogar","lar","nm"),"Discipleship":("discipulado","discipulado","nm"),
 "End":("final","fim","nm"),"Career":("carrera","carreira","nf"),"Identity":("identidad","identidade","nf"),
 "Kids":("ni\u00f1os","crian\u00e7as","nm;f"),"Profit":("ganancia","lucro","nf;m"),"Line":("l\u00ednea","linha","nf"),
 "Servant":("siervo","servo","nm"),"House":("casa","casa","nf"),"Half":("mitad","metade","nf"),
 "Women":("mujeres","mulheres","nf"),"Men":("hombres","homens","nm"),"Parents":("padres","pais","nm"),
 "Firm":("firma","firma","nf"),"Discernment":("discernimiento","discernimento","nm"),"Roots":("ra\u00edces","ra\u00edzes","nf"),
 "Transformation":("transformaci\u00f3n","transforma\u00e7\u00e3o","nf"),"Integrity":("integridad","integridade","nf"),
 "Disciple":("disc\u00edpulo","disc\u00edpulo","nm"),"Disciples":("disc\u00edpulos","disc\u00edpulos","nm"),"Principles":("principios","princ\u00edpios","nm"),
 "Managers":("administradores","administradores","nm"),"Reward":("recompensa","recompensa","nf"),
 "Eyes":("ojos","olhos","nm"),"Things":("cosas","coisas","nf"),"Voice":("voz","voz","nf"),"Room":("espacio","espa\u00e7o","nm"),
 "Gospel":("evangelio","evangelho","nm"),"Simplicity":("sencillez","simplicidade","nf"),"Heaven":("cielo","c\u00e9u","nm"),
 "Purposes":("prop\u00f3sitos","prop\u00f3sitos","nm"),"Philanthropy":("filantrop\u00eda","filantropia","nf"),
 "Council":("consejo","conselho","nm"),"Builders":("constructores","construtores","nm"),"Action":("acci\u00f3n","a\u00e7\u00e3o","nf"),
 "Needs":("necesidades","necessidades","nf"),"Documents":("documentos","documentos","nm"),"Governance":("gobernanza","governan\u00e7a","nf"),
 "Enterprise":("empresa","empresa","nf"),"College":("universidad","faculdade","nf"),"Meetings":("reuniones","reuni\u00f5es","nf"),
 "Grandparents":("abuelos","av\u00f3s","nm"),"Grandparenting":("ser abuelos","ser av\u00f3s","g"),"Bottom":("fondo","fundo","nm"),
 "Company":("empresa","empresa","nf"),"Exit":("salida","sa\u00edda","nf"),"Significance":("trascendencia","signific\u00e2ncia","nf"),
 "Power":("poder","poder","nm"),"Book":("libro","livro","nm"),"Place":("lugar","lugar","nm"),
 "Testament":("testamento","testamento","nm"),"Beginning":("comienzo","come\u00e7o","nm"),"Storm":("tormenta","tempestade","nf"),
 "Rest":("descanso","descanso","nm"),"Connection":("conexi\u00f3n","conex\u00e3o","nf"),"Belonging":("pertenencia","pertencimento","nf;m"),
 "Letters":("cartas","cartas","nf"),"Practice":("pr\u00e1ctica","pr\u00e1tica","nf"),"Neighbor":("pr\u00f3jimo","pr\u00f3ximo","nm"),
 "Fasting":("ayuno","jejum","nm"),"Spirit":("Esp\u00edritu","Esp\u00edrito","nm"),"Lord":("Se\u00f1or","Senhor","nm"),
 "Service":("servicio","servi\u00e7o","nm"),"Grandchildren":("nietos","netos","nm"),"Communication":("comunicaci\u00f3n","comunica\u00e7\u00e3o","nf"),
 "Center":("centro","centro","nm"),"Example":("ejemplo","exemplo","nm"),"Presence":("presencia","presen\u00e7a","nf"),
 "Management":("administraci\u00f3n","administra\u00e7\u00e3o","nf"),"Perspective":("perspectiva","perspectiva","nf"),
 "Master":("Maestro","Mestre","nm"),"Playbook":("manual","manual","nm"),"Guide":("gu\u00eda","guia","nm"),
 "Numbers":("n\u00fameros","n\u00fameros","nm"),"Taxes":("impuestos","impostos","nm"),"Tax":("fiscal","fiscal","a"),
 "Margin":("margen","margem","nm;f"),"Proverbs":("Proverbios","Prov\u00e9rbios","nm"),"Review":("revisi\u00f3n","revis\u00e3o","nf"),
 "Area":("\u00e1rea","\u00e1rea","nf"),"Questions":("preguntas","perguntas","nf"),"Capital":("capital","capital","nm"),
 "Transfer":("transferencia","transfer\u00eancia","nf"),"Monday":("lunes","segunda-feira","nm;f"),"SHAPE":("SHAPE","SHAPE","k"),
 # adjectives (postpose + agree)
 "Financial":("financiero","financeiro","a"),"Spiritual":("espiritual","espiritual","a1"),"Biblical":("b\u00edblico","b\u00edblico","a"),
 "Eternal":("eterno","eterno","a"),"Faithful":("fiel","fiel","a1"),"Wise":("sabio","s\u00e1bio","a"),
 "Generous":("generoso","generoso","a"),"Strong":("fuerte","forte","a1"),"New":("nuevo","novo","a"),
 "Everyday":("cotidiano","cotidiano","a"),"Open":("abierto","aberto","a"),"First":("primero","primeiro","a"),
 "Great":("grande","grande","a1"),"Greatest":("m\u00e1s grande","maior","a1"),"Healthy":("sano","saud\u00e1vel","a;a1"),
 "Better":("mejor","melhor","a1"),"Last":("\u00faltimo","\u00faltimo","a"),"Next":("pr\u00f3ximo","pr\u00f3ximo","a"),
 "Young":("joven","jovem","a1"),"Adult":("adulto","adulto","a"),"Intentional":("intencional","intencional","a1"),
 "Deep":("profundo","profundo","a"),"Whole":("entero","inteiro","a"),"Free":("libre","livre","a1"),
 "Courageous":("valiente","corajoso","a1;a"),"Christian":("cristiano","crist\u00e3o","a"),"Rich":("rico","rico","a"),
 "Real":("real","real","a1"),"Honest":("honesto","honesto","a"),"Practical":("pr\u00e1ctico","pr\u00e1tico","a"),
 "Joyful":("gozoso","alegre","a;a1"),"Responsible":("responsable","respons\u00e1vel","a1"),"Good":("bueno","bom","a"),
 "Hard":("dif\u00edcil","dif\u00edcil","a1"),"Final":("final","final","a1"),"Timeless":("atemporal","atemporal","a1"),
 "Broken":("quebrantado","quebrantado","a"),"Blessed":("bendecido","aben\u00e7oado","a"),"Generational":("generacional","geracional","a1"),
 "Lasting":("duradero","duradouro","a"),"Shared":("compartido","compartilhado","a"),"Centered":("centrado","centrado","a"),
 "Rooted":("arraigado","enraizado","a"),"Daily":("diario","di\u00e1rio","a"),"Trusted":("de confianza","de confian\u00e7a","a1"),
 "Gifted":("dotado","dotado","a"),"Anchored":("anclado","ancorado","a"),"Surrendered":("rendido","rendido","a"),
 "Given":("dado","dado","a"),"Fully":("plenamente","plenamente","x"),"Annual":("anual","anual","a1"),
 "Grandparent":("de abuelos","de av\u00f3s","a1"),"Changed":("transformado","transformado","a"),"Entrusted":("confiado","confiado","a"),
 "Built":("edificado","edificado","a"),"Called":("llamado","chamado","a"),"Made":("hecho","feito","a"),"Ready":("listo","pronto","a"),
 "Designed":("dise\u00f1ado","desenhado","a"),"Created":("creado","criado","a"),"Connected":("conectado","conectado","a"),
 "Flourishing":("floreciente","florescente","a1"),
 # gerund heads
 "Living":("viviendo","vivendo","g"),"Building":("edificando","edificando","g"),"Growing":("creciendo","crescendo","g"),
 "Preparing":("preparando","preparando","g"),"Giving":("dando","doando","g"),"Creating":("creando","criando","g"),
 "Leading":("liderando","liderando","g"),"Passing":("transmitiendo","transmitindo","g"),"Discovering":("descubriendo","descobrindo","g"),
 "Finding":("encontrando","encontrando","g"),"Helping":("ayudando","ajudando","g"),"Making":("haciendo","fazendo","g"),
 "Using":("usando","usando","g"),"Following":("siguiendo","seguindo","g"),"Walking":("caminando","caminhando","g"),
 "Raising":("criando","criando","g"),"Trusting":("confiando en","confiando em","g"),"Aligning":("alineando","alinhando","g"),
 "Planning":("planificando","planejando","g"),"Serving":("sirviendo","servindo","g"),"Stewarding":("administrando","administrando","g"),
 "Managing":("administrando","administrando","g"),"Choosing":("eligiendo","escolhendo","g"),"Learning":("aprendiendo","aprendendo","g"),
 "Investing":("invirtiendo","investindo","g"),"Becoming":("llegando a ser","tornando-se","g"),"Turning":("convirtiendo","transformando","g"),
 "Honoring":("honrando","honrando","g"),"Parenting":("criando hijos","criando filhos","g"),"Talking":("hablando","conversando","g"),
 "Leaving":("dejando","deixando","g"),"Knowing":("conociendo","conhecendo","g"),"Starting":("comenzando","come\u00e7ando","g"),
 "Understanding":("entendiendo","entendendo","g"),"Applying":("aplicando","aplicando","g"),"Developing":("desarrollando","desenvolvendo","g"),
 "Strengthening":("fortaleciendo","fortalecendo","g"),"Seeing":("viendo","vendo","g"),"Losing":("perdiendo","perdendo","g"),
 "Influencing":("influyendo en","influenciando","g"),"Protecting":("protegiendo","protegendo","g"),"Remembering":("recordando","lembrando","g"),
 "Restoring":("restaurando","restaurando","g"),"Doing":("haciendo","fazendo","g"),"Moving":("pasando","passando","g"),
 "Putting":("poniendo","colocando","g"),"Redefining":("redefiniendo","redefinindo","g"),"Seeking":("buscando","buscando","g"),
 "Multiplying":("multiplicando","multiplicando","g"),"Continuing":("continuando","continuando","g"),"Speaking":("hablando","falando","g"),
 "Preserving":("preservando","preservando","g"),"Sharing":("compartiendo","compartilhando","g"),"Breaking":("rompiendo","quebrando","g"),
 "Standing":("permaneciendo","permanecendo","g"),"Healing":("sanidad","cura","nf"),"Loving":("amando","amando","g"),
 "Blessing2":("bendiciendo","aben\u00e7oando","g"),
 # verbs (imperative-ish heads)
 "Build":("edifica","edifique","x"),"Give":("da","d\u00ea","x"),"Serve":("sirve","sirva","x"),"Live":("vive","viva","x"),
 "Lead":("lidera","lidere","x"),"Follow":("sigue","siga","x"),"Bless":("bendice","aben\u00e7oe","x"),"Discover":("descubre","descubra","x"),
 "Become":("llega a ser","torne-se","x"),"Ask":("pregunta","pergunte","x"),"Finish":("termina","termine","x"),
 "Grows":("crece","cresce","x"),"Gives":("da","d\u00e1","x"),"Owns":("es due\u00f1o de","\u00e9 dono de","x"),
 "Matters":("importa","importa","x"),"Lasts":("permanece","permanece","x"),"Changes":("cambia","muda","x"),
 "Begins":("comienza","come\u00e7a","x"),"Honors":("honra","honra","x"),"Outlive":("sobrevivir a","sobreviver a","x"),
 "Manages":("administra","administra","x"),"Were":("fuiste","voc\u00ea foi","x"),"Flourish":("florecer","florescer","x"),
 "Handed":("entregado","entregue","a"),"Advance":("avanzar","avan\u00e7ar","x"),"Do2":("hacer","fazer","x"),
}

PHRASES = [
 ("40 Days of","40 D\u00edas de","40 Dias de"),
 ("Seven Days of","Siete D\u00edas de","Sete Dias de"),
 ("30 Days of","30 D\u00edas de","30 Dias de"),
 ("21 Days of","21 D\u00edas de","21 Dias de"),
 ("God Owns It All","Dios es due\u00f1o de todo","Deus \u00e9 dono de tudo"),
 ("More Than Money","M\u00e1s que dinero","Mais que dinheiro"),
 ("Finishing Well","Terminar bien","Terminar bem"),
 ("Finish Well","Termina bien","Termine bem"),
 ("Well Done","Bien hecho","Bem feito"),
 ("Next Generation","siguiente generaci\u00f3n","pr\u00f3xima gera\u00e7\u00e3o"),
 ("Empty Nest","nido vac\u00edo","ninho vazio"),
 ("Each One, Ask One","Cada uno invita a uno","Cada um convida um"),
 ("Faithful with Little","Fiel en lo poco","Fiel no pouco"),
 ("Faithful with Much","Fiel en lo mucho","Fiel no muito"),
 ("Wise with Much","Sabio en lo mucho","S\u00e1bio no muito"),
 ("Open Hands","Manos abiertas","M\u00e3os abertas"),
 ("The Good Life","La buena vida","A boa vida"),
 ("Second Half","segunda mitad","segunda metade"),
 ("Bottom Line","resultado final","resultado final"),
 ("Year-End","de fin de a\u00f1o","de fim de ano"),
 ("Family Office","family office","family office"),
 ("Family Offices","family offices","family offices"),
 ("Whole-Life","de vida entera","de vida inteira"),
 ("What God Has Done","Lo que Dios ha hecho","O que Deus tem feito"),
 ("Counting My Blessings","Contando mis bendiciones","Contando minhas b\u00ean\u00e7\u00e3os"),
 ("The Thankful Life","La vida agradecida","A vida grata"),
 ("It All","todo","tudo"),
]

def pos(entry): return entry[2] if len(entry)>2 else "x"

def agree_es(adj, noun_entry):
    g = "f" if (noun_entry and "f" in noun_entry[2].split(";")[0]) else "m"
    if adj.endswith("o") and g=="f": return adj[:-1]+"a"
    return adj
def agree_pt(adj, noun_entry):
    gtag = noun_entry[2].split(";")[-1] if noun_entry else "m"
    g = "f" if "f" in gtag else "m"
    if adj.endswith("o") and g=="f": return adj[:-1]+"a"
    if adj=="crist\u00e3o" and g=="f": return "crist\u00e3"
    return adj

def translate(text, lang):
    t = text
    # phrases first
    for en,es,pt in PHRASES:
        t = t.replace(en, "\u0001"+(es if lang=="es" else pt)+"\u0001")
    tokens = re.findall(r"\u0001[^\u0001]+\u0001|[A-Za-z']+|[^A-Za-z'\s]+|\s+", t)
    out=[]
    i=0
    idx=lang=="es" and 0 or 1
    while i < len(tokens):
        tk = tokens[i]
        if tk.startswith("\u0001"): out.append(tk.strip("\u0001")); i+=1; continue
        if not re.match(r"[A-Za-z']+$", tk): out.append(tk); i+=1; continue
        # possessive X's Y -> Y de X
        if tk.endswith("'s") and tk[:-2] in L:
            owner = L[tk[:-2]][idx]
            # find following NP tokens (up to next non-word/preposition)
            j=i+1; np=[]
            while j < len(tokens):
                w=tokens[j]
                if re.match(r"\s+$", w): j+=1; continue
                if re.match(r"[A-Za-z']+$", w) and w in L and pos(L[w]) in ("nf","nm","nm;f","nf;m","a","a1","a;a1","a1;a"):
                    np.append(w); j+=1
                    if pos(L[w]).startswith("n"): break
                else: break
            if np:
                sub = translate(" ".join(np), lang)
                out.append(sub + " de " + owner); i=j; continue
            out.append("de "+owner); i+=1; continue
        e = L.get(tk)
        if not e:
            out.append(tk); i+=1; continue
        p = pos(e)
        if p=="drop": i+=1; continue
        # adjective + noun reorder
        if p.startswith("a"):
            j=i+1
            while j<len(tokens) and re.match(r"\s+$",tokens[j]): j+=1
            if j<len(tokens) and tokens[j] in L and pos(L[tokens[j]]).startswith("n"):
                noun_e = L[tokens[j]]
                adj = e[idx]
                if lang=="es": adj = agree_es(adj, noun_e) if p in("a","a;a1") else adj
                else:
                    ppt = p.split(";")[-1] if ";" in p else p
                    adj = agree_pt(adj, noun_e) if ppt=="a" else adj
                out.append(noun_e[idx]+" "+adj); i=j+1; continue
            out.append(e[idx]); i+=1; continue
        if p=="art":
            j=i+1
            while j<len(tokens) and re.match(r"\s+$",tokens[j]): j+=1
            nxt = tokens[j] if j<len(tokens) else ""
            fem=False
            if nxt in L and pos(L[nxt]).startswith("n"):
                gt=pos(L[nxt]); fem = gt.split(";")[0]=="nf" if lang=="es" else (gt.split(";")[-1] in("nf","f") or gt=="nf")
            if lang=="es": out.append("La" if fem and tk[0]=="T" else ("la" if fem else e[0]))
            else: out.append("A" if fem and tk[0]=="T" else ("a" if fem else e[1]))
            i+=1; continue
        out.append(e[idx]); i+=1
    s="".join(out)
    s=re.sub(r"\s+"," ",s).strip()
    # sentence case: first letter cap, keep proper nouns
    if s: s = s[0].upper()+s[1:]
    # cleanup artifacts
    s = s.replace(" de de "," de ").replace("de el ","del ").replace("De el ","Del ")
    if lang=="pt": s = s.replace("de o ","do ").replace("De o ","Do ").replace("de a ","da ").replace("De a ","Da ").replace("em o ","no ").replace("em a ","na ")
    if lang=="es": s = s.replace("a el ","al ")
    return s

# ---------- apply to both builds ----------
CATS_T = {
 "es":{"1":"Mayordom\u00eda y sabidur\u00eda financiera"},
 "pt":{"1":"Mordomia e sabedoria financeira"}
}
for lang in ["es","pt"]:
    p=f"/home/claude/site_{lang}/data.js"
    src=open(p).read()
    m=re.search(r"window\.CAMPAIGNS=(\[.*?\]);\n",src,re.S)
    C=json.loads(m.group(1))
    unknown={}
    for r in C:
        r[0]=translate(r[0],lang)
        if r[1]: r[1]=translate(r[1],lang)
        for w in re.findall(r"[A-Za-z']+", r[0]+" "+(r[1] or "")):
            if re.match(r"^[A-Z]?[a-z]+$",w) and w.lower() not in ("de","la","el","los","las","del","al","que","con","para","y","en","un","una","o","a","os","as","do","da","dos","das","e","em","um","uma","no","na","com","por","sem","mais","m\u00e1s") and w in {k for k in []}:
                pass
    # translate CATS + THEMEMETA labels + audience/occasion fields via translate()
    m2=re.search(r"window\.CATS=(\{.*?\});",src,re.S)
    CATS=json.loads(m2.group(1))
    for k in CATS: CATS[k]=translate(CATS[k],lang)
    m3=re.search(r"window\.THEMEMETA=(\{.*?\});",src,re.S)
    TM=json.loads(m3.group(1))
    TM2={}
    for k,v in TM.items():
        nk=translate(k,lang); v=list(v); v[3]=nk if len(v)>3 else nk
        TM2[nk]=v
    # theme keys are referenced by r[10] — translate those too
    for r in C:
        r[10]=translate(r[10],lang)
        if r[11]: r[11]=translate(r[11],lang)
        if r[12]: r[12]=translate(r[12],lang)
    out=src[:m.start()]+"window.CAMPAIGNS="+json.dumps(C,ensure_ascii=False)+";\n"+src[m.end():]
    m2=re.search(r"window\.CATS=(\{.*?\});",out,re.S)
    out=out[:m2.start()]+"window.CATS="+json.dumps(CATS,ensure_ascii=False)+";"+out[m2.end():]
    m3=re.search(r"window\.THEMEMETA=(\{.*?\});",out,re.S)
    out=out[:m3.start()]+"window.THEMEMETA="+json.dumps(TM2,ensure_ascii=False)+";"+out[m3.end():]
    open(p,"w").write(out)
    print(lang,"catalog translated:",len(C),"campaigns")
    # QA: untranslated-token scan
    left={}
    ENGLISH_HINTS=set("the of and for with your that from into what who how when this our you their his".split())
    for r in C[:1252]:
        for w in re.findall(r"[A-Za-z']+", r[0]+" "+(r[1] or "")):
            if w.lower() in ENGLISH_HINTS: left[w]=left.get(w,0)+1
    print(lang,"suspicious English function words remaining:",dict(sorted(left.items(),key=lambda x:-x[1])[:10]))
    print(lang,"samples:", " | ".join(r[0] for r in C[:6]))
    print(lang,"sub sample:", C[0][1])
