# -*- coding: utf-8 -*-
import re, subprocess

P = '/home/claude/site_pt/engine.js'
s = open(P).read()

def replace_fn(src, name, code):
    m = re.search(r'function '+name+r'\(', src)
    i = m.start()
    j = src.index('{', i); d=1; k=j+1
    while d:
        if src[k]=='{': d+=1
        if src[k]=='}': d-=1
        k+=1
    return src[:i] + code + src[k:]

def replace_arr(src, name, items):
    i = src.index(name+'=[')
    j = i+len(name)+1; d=0; k=j
    while True:
        if src[k]=='[': d+=1
        if src[k]==']':
            d-=1
            if d==0: break
        k+=1
    lit = '[' + ','.join('"'+x.replace('"','\\"')+'"' for x in items) + ']'
    return src[:i+len(name)+1] + lit + src[k+1:]

G = {}
G['gOpen'] = '''function gOpen(r,m){ return pk(r,[
 "Antes que o dia ganhe velocidade, pare um momento aqui.",
 "H\\u00e1 uma conversa que Deus quer ter com voc\\u00ea hoje, e ela come\\u00e7a nesta p\\u00e1gina.",
 "Voc\\u00ea n\\u00e3o chegou a este dia por acidente; algo na sua semana precisa exatamente desta palavra.",
 "O dia de hoje traz a pr\\u00f3pria agenda, mas primeiro escute esta.",
 "Respire. O que vem a seguir n\\u00e3o \\u00e9 informa\\u00e7\\u00e3o para saber mais, e sim um convite para viver diferente."]); }'''
G['gTension'] = '''function gTension(r,m){ return pk(r,[
 "Porque sejamos honestos: no tema de "+m.c+", a dist\\u00e2ncia entre o que cremos e o que praticamos costuma ser grande.",
 "E aqui est\\u00e1 a tens\\u00e3o: quase ningu\\u00e9m discute essa verdade, e quase ningu\\u00e9m a vive sem ajuda.",
 "O dif\\u00edcil n\\u00e3o \\u00e9 entender isso; o dif\\u00edcil \\u00e9 a ter\\u00e7a-feira \\u00e0 tarde lembrar do que cremos.",
 "O problema nunca foi falta de informa\\u00e7\\u00e3o, e sim falta de pr\\u00e1tica nos dias comuns.",
 "Uma vida pode derivar um dia n\\u00e3o examinado por vez; hoje interrompe essa deriva."]); }'''
G['gHook'] = '''function gHook(r,m){ return pk(r,[
 "H\\u00e1 uma pergunta esperando debaixo deste dia: o que aconteceria se "+m.c+" deixasse de ser uma palavra e come\\u00e7asse a ser um h\\u00e1bito?",
 "Cedo ou tarde chega um dia como hoje, quando a linha sublinhada de ontem quer virar a pegada de hoje.",
 "Hoje a jornada fica pessoal: n\\u00e3o se trata do que os outros deveriam fazer, e sim do que voc\\u00ea pode come\\u00e7ar.",
 "Algumas verdades se aprendem lendo; esta se aprende caminhando, e hoje \\u00e9 dia de dar um passo.",
 "Se voc\\u00ea j\\u00e1 leu sobre "+m.c+" antes, hoje deixe o texto ler voc\\u00ea."]); }'''
G['gRead'] = '''function gRead(r,m,scr){ return pk(r,[
 "Abra a leitura de hoje, "+scr+", antes que o dia d\\u00ea a sua opini\\u00e3o. ",
 "A leitura de hoje \\u00e9 "+scr+"; leia devagar, como quem escuta e n\\u00e3o como quem revisa. ",
 "Procure "+scr+" e fique um minuto a mais do que o confort\\u00e1vel. ",
 "Hoje o texto \\u00e9 "+scr+", e vale a pena ler duas vezes: uma para entender, outra para obedecer. ",
 "Antes de seguir, leia "+scr+"; o que vem abaixo pressup\\u00f5e que o texto j\\u00e1 falou primeiro. "]); }'''
G['gTruth'] = '''function gTruth(r,m){ return pk(r,[
 "O surpreendente da passagem \\u00e9 que ela n\\u00e3o pede sentimentos novos, e sim decis\\u00f5es pequenas e repetidas.",
 "A Escritura n\\u00e3o tem pressa aqui: planta uma verdade e espera a colheita nos dias comuns.",
 "Note bem: o texto pressup\\u00f5e que isso se vive em casa, no trabalho e \\u00e0 mesa, n\\u00e3o s\\u00f3 no templo.",
 "Deus n\\u00e3o est\\u00e1 pedindo perfei\\u00e7\\u00e3o nisso; est\\u00e1 formando fidelidade, um dia por vez.",
 "A passagem n\\u00e3o decora a vida; ela a reordena, come\\u00e7ando pelo que parecia pequeno demais para importar."]); }'''
G['gGroundWrap'] = '''function gGroundWrap(r,m,core){ return pk(r,[
 "Pare o pensamento aqui: "+core,
 "Esta \\u00e9 a rocha debaixo do dia: "+core,
 "Se voc\\u00ea guardar uma s\\u00f3 ideia hoje, que seja esta: "+core,
 "Os que caminharam antes disseram assim: "+core,
 "Conv\\u00e9m dizer sem enfeite: "+core]); }'''
G['gStory'] = '''function gStory(r){
 var who=pk(r,VX_PEOPLE), where=pk(r,VX_PLACE), span=pk(r,VX_TIMEBOX);
 var prac=pk(r,[
  "guardou uma \\u00fanica palavra da leitura de cada dia num bilhete adesivo",
  "orou uma frase por cada pessoa debaixo do seu teto, pelo nome",
  "escreveu toda noite uma linha sobre onde Deus apareceu",
  "leu a passagem antes de tocar no celular",
  "agradeceu a uma pessoa espec\\u00edfica por algo espec\\u00edfico",
  "deu algo pequeno mas real antes do p\\u00f4r do sol",
  "memorizou um vers\\u00edculo por semana no carro",
  "enviou o vers\\u00edculo do dia a um amigo, sem coment\\u00e1rio"]);
 var pay=pk(r,[
  "As circunst\\u00e2ncias n\\u00e3o mudaram muito, dizem, mas quase todas as suas respostas mudaram.",
  "Ningu\\u00e9m notou na primeira semana; na sexta, todos notavam.",
  "N\\u00e3o foi dram\\u00e1tico, foi acumulativo, e isso acabou sendo melhor.",
  "O que come\\u00e7ou como disciplina terminou parecendo descanso.",
  "A casa n\\u00e3o ficou perfeita, mas ficou mais honesta e mais leve."]);
 return "Conhecemos a hist\\u00f3ria de "+who+" que, "+where+" e "+span+", "+prac+". "+pay; }'''
G['gStoryMoral'] = '''function gStoryMoral(r,m){ return pk(r,[
 "Fa\\u00e7a uma vez e \\u00e9 um ato; fa\\u00e7a todos os dias e vira "+m.c+" com ra\\u00edzes.",
 "\\u00c9 assim que isso cresce na vida real: n\\u00e3o por impulsos grandes, mas por fidelidades pequenas.",
 "A li\\u00e7\\u00e3o n\\u00e3o \\u00e9 copiar a pr\\u00e1tica deles, e sim escolher uma sua e sustent\\u00e1-la.",
 "Hist\\u00f3rias assim n\\u00e3o provam uma f\\u00f3rmula; mostram uma dire\\u00e7\\u00e3o, e a dire\\u00e7\\u00e3o est\\u00e1 aberta hoje.",
 "Deus costuma esconder colheitas grandes dentro de h\\u00e1bitos pequenos."]); }'''
G['gApply'] = '''function gApply(r,m){ return pk(r,[
 "D\\u00ea a isto uma porta concreta: um trajeto, uma refei\\u00e7\\u00e3o, uma soleira, e decida agora como vai responder antes de o momento chegar.",
 "Nomeie a hora do dia em que isto ser\\u00e1 testado e v\\u00e1 ao encontro dela de prop\\u00f3sito; h\\u00e1bitos penduram em ganchos.",
 "Escolha uma a\\u00e7\\u00e3o t\\u00e3o pequena que voc\\u00ea n\\u00e3o possa falhar, e t\\u00e3o real que algu\\u00e9m perceba.",
 "Coloque no calend\\u00e1rio, a caneta; emboscadas perdem para compromissos.",
 "Antes de fechar a p\\u00e1gina, decida o onde e o quando; inten\\u00e7\\u00e3o sem endere\\u00e7o evapora.",
 "Conte a uma pessoa o que voc\\u00ea vai tentar hoje; o dito em voz alta pesa diferente."]); }'''
G['gClose'] = '''function gClose(r,m,d){ return pk(r,[
 "Deixe o dia terminar mais quieto do que come\\u00e7ou: trinta segundos sem pressa com o vers\\u00edculo, e permiss\\u00e3o para deixar o resto nas m\\u00e3os de Deus.",
 "N\\u00e3o confunda o silencioso com o in\\u00fatil; a colheita nunca pergunta como foi o plantio do Dia "+d+".",
 "Um pensamento antes de fechar o Dia "+d+": se voc\\u00ea chegou sem for\\u00e7as, chegou \\u00e0 p\\u00e1gina certa; Deus faz muito com pouco.",
 "Hoje nada foi avaliado; algo foi plantado. Durma sobre isso.",
 "Seja o que for que o dia conseguiu ou n\\u00e3o, voc\\u00ea se apresentou para ouvir a Deus, e isso j\\u00e1 mudou a dire\\u00e7\\u00e3o."]); }'''
G['gDeeper'] = '''function gDeeper(r,m,d){ return pk(r,[
 "Se quiser ir mais fundo hoje, volte \\u00e0 passagem e pare em cada verbo; os verbos s\\u00e3o onde a Escritura pede as m\\u00e3os.",
 "Uma pergunta extra para a margem do dia: quem voc\\u00ea conhece que vive bem isso, e o que poderia imitar esta semana?",
 "Para quem quer mais: escreva numa linha o que Deus est\\u00e1 pedindo de voc\\u00ea no tema de "+m.c+", e marque uma data.",
 "Antes de dormir, repasse o dia procurando uma \\u00fanica pegada de Deus; escrever leva um minuto e ancora a mem\\u00f3ria.",
 "Se o dia deixou uma pergunta sem resposta, guarde-a para o seu grupo esta semana; perguntas honestas s\\u00e3o combust\\u00edvel."]); }'''
G['gPrayer'] = '''function gPrayer(r,m){ return pk(r,[
 "Pai, obrigado por me encontrar hoje nestas palavras. D\\u00e1-me uma chance clara de praticar "+m.c+" antes que o dia termine, e a coragem de aproveit\\u00e1-la. Am\\u00e9m.",
 "Senhor Jesus, tens sido mais paciente comigo do que eu mesmo. Interrompe-me na hora certa hoje, e ensina-me a responder como tu. Am\\u00e9m.",
 "Deus, n\\u00e3o pe\\u00e7o um dia f\\u00e1cil, e sim um cora\\u00e7\\u00e3o atento. Que o que li de manh\\u00e3 tenha a \\u00faltima palavra \\u00e0 noite. Am\\u00e9m.",
 "Esp\\u00edrito Santo, tu conheces a hora exata em que isto ser\\u00e1 dif\\u00edcil hoje. Chega antes de mim. Am\\u00e9m.",
 "Pai, diminui a minha pressa e aumenta a tua voz. Hoje quero obedecer em algo concreto, mesmo que pequeno. Am\\u00e9m."]); }'''
G['gQuestion'] = '''function gQuestion(r,m){ return pk(r,[
 "Se nada na sua vida mudasse em um ano, o que voc\\u00ea gostaria de ter come\\u00e7ado hoje?",
 "Em que parte da sua vida Deus est\\u00e1 convidando voc\\u00ea, agora mesmo, a levar "+m.c+" mais a s\\u00e9rio?",
 "Quem na sua vida modela bem isso, e o que voc\\u00ea poderia come\\u00e7ar a imitar esta semana?",
 "Quando foi a \\u00faltima vez que Deus se provou fiel a voc\\u00ea, e o que voc\\u00ea aprendeu na espera?",
 "O que essa verdade tornaria poss\\u00edvel que na segunda-feira parecia imposs\\u00edvel?"]); }'''
G['gStep'] = '''function gStep(r,m){ return "Passo de hoje: "+gStepCore(r,m,false)+"."; }'''
G['gStepCore'] = '''function gStepCore(r,m,weekly){ return pk(r,weekly?[
 "escolha um momento comum de cada dia, um trajeto, uma refei\\u00e7\\u00e3o, uma soleira, e deixe o vers\\u00edculo da semana acompanh\\u00e1-lo",
 "pe\\u00e7a perd\\u00e3o por uma coisa, limpamente, sem v\\u00edrgula e sem desculpa, esta semana",
 "d\\u00ea algo pequeno mas real todos os dias antes do p\\u00f4r do sol",
 "caminhe uma volta lenta e ore pelo que realmente vir, todo dia at\\u00e9 domingo",
 "escreva toda noite uma linha sobre onde Deus apareceu no seu dia"]:[
 "diga o vers\\u00edculo em voz alta tr\\u00eas vezes: manh\\u00e3, meio-dia e noite",
 "envie o vers\\u00edculo de hoje a um amigo, sem coment\\u00e1rio",
 "agrade\\u00e7a a uma pessoa espec\\u00edfica por algo espec\\u00edfico antes do jantar",
 "fa\\u00e7a uma pausa de sessenta segundos antes da sua hora mais dif\\u00edcil e entregue-a a Deus",
 "deixe o celular fora da primeira meia hora da manh\\u00e3 e d\\u00ea esse espa\\u00e7o \\u00e0 leitura"]); }'''
G['gPractice'] = '''function gPractice(r,m){ return "A pr\\u00e1tica desta semana: "+gStepCore(r,m,true)+". Fa\\u00e7a uma vez e \\u00e9 um ato; fa\\u00e7a todos os dias e vira um caminho."; }'''
G['gCarry'] = '''function gCarry(r,d){
 var lead=pk(r,["leve o vers\\u00edculo desta semana para ","caminhe com o vers\\u00edculo desta semana at\\u00e9 ","deixe o vers\\u00edculo da semana acompanhar voc\\u00ea em "]);
 var where=pk(r,["um momento espec\\u00edfico "+pk(r,VX_SOON),"a hora que voc\\u00ea menos quer viver hoje","uma tarefa comum de hoje","a pr\\u00f3xima conversa dif\\u00edcil","os \\u00faltimos minutos antes de dormir"]);
 var how=pk(r,[" e deixe que ele tenha ali a \\u00faltima palavra."," e diga-o uma vez em voz alta se puder."," e deixe que interrompa o que normalmente manda ali."]);
 return lead+where+how; }'''
G['gTomorrow'] = '''function gTomorrow(r,d,n,nextPart){
 if(d>=n) return pk(r,[
  "Amanh\\u00e3 voc\\u00ea vai olhar todo o caminho percorrido; termine hoje com gratid\\u00e3o pelo quanto Deus o trouxe.",
  "A \\u00faltima p\\u00e1gina est\\u00e1 perto. Termine hoje agradecido e venha pronto para lembrar de tudo.",
  "Mais um amanhecer e a jornada vira celebra\\u00e7\\u00e3o. Caminhe bem o passo de hoje."]);
 var lead=pk(r,["Amanh\\u00e3 a jornada continua","O caminho segue amanh\\u00e3","O Dia "+(d+1)+" j\\u00e1 espera","A pr\\u00f3xima p\\u00e1gina se abre pela manh\\u00e3"]);
 var mid=nextPart?pk(r,[", cruzando para \\u00ab"+nextPart+"\\u00bb",", e com ele um trecho novo chamado \\u00ab"+nextPart+"\\u00bb"]):"";
 var tail=pk(r,["; hoje basta o passo de hoje.","; n\\u00e3o carregue amanh\\u00e3 antes da hora.","; durma e volte."]);
 return lead+mid+tail; }'''
G['gProvision'] = '''function gProvision(r,occ){
 var a=pk(r,["E porque esta jornada foi pensada com "+occ+" em mente,","Esta jornada foi formada para "+occ+", ent\\u00e3o","Constru\\u00edda como foi para "+occ+","]);
 var b=pk(r,[" n\\u00e3o se surpreenda se o passo de hoje cair perto de casa; isso \\u00e9 desenho, n\\u00e3o acidente."," se hoje parecer estranhamente oportuno, \\u00e9 porque \\u00e9: a provis\\u00e3o de perto parece coincid\\u00eancia."," o desafio de hoje pode caber desconfortavelmente bem na sua semana; receba isso como uma bondade."]);
 return a+b; }'''
G['gPromise'] = '''function gPromise(r,t,sub,c){
 var s2=sub?String(sub).replace(/\\.$/,''):null;
 var pool=[
  "Lembre para onde tudo isto vai: "+t+" n\\u00e3o \\u00e9 um curso para passar, e sim um caminho para caminhar.",
  "No meio da caminhada conv\\u00e9m levantar os olhos: Deus est\\u00e1 formando "+c+" em voc\\u00ea, e n\\u00e3o tem pressa nem d\\u00favida.",
  "Esta jornada fez uma promessa ao come\\u00e7ar, e cada dia como hoje a vai cumprindo em sil\\u00eancio."];
 if(s2){ pool.push("\\u00ab"+s2+"\\u00bb. Essa continua sendo a frase sobre toda a viagem, e hoje ela deu mais um passo para ser verdade."); }
 return pk(r,pool); }'''
G['gAnchorLabel'] = '''function gAnchorLabel(r){ return pk(r,["\\u00c2ncora para hoje","Leve isto hoje","A \\u00e2ncora de hoje","Uma linha para guardar","Segure esta linha hoje"]); }'''
G['gScrFirst'] = '''function gScrFirst(r,m,scr){ return pk(r,[
 "Comece hoje pelo texto: "+scr+". Leia antes de ler qualquer coisa minha, porque o dia inteiro se ap\\u00f3ia ali.",
 "Hoje a Escritura vai primeiro: "+scr+". O resto desta p\\u00e1gina s\\u00f3 ajuda a carreg\\u00e1-la.",
 "Abra "+scr+" agora, devagar; o resto do dia de hoje \\u00e9 coment\\u00e1rio."]); }'''

# replace gStep before gStepCore is irrelevant now (regex-anchored); do gStepCore first anyway
order = ['gStepCore','gStep'] + [k for k in G if k not in ('gStep','gStepCore')]
for name in order:
    s = replace_fn(s, name, G[name])

s = replace_arr(s,'VX_PEOPLE',["uma m\u00e3e jovem","um enfermeiro do turno da noite","um professor aposentado","uma dona de neg\u00f3cio","um pai solteiro","uma estudante universit\u00e1ria","um av\u00f4 rec\u00e9m-estreado","um casal de agenda cheia"])
s = replace_arr(s,'VX_PLACE',["na mesa da cozinha","no carro antes de entrar","na sala, com a casa dormindo","na pausa do meio-dia","no \u00f4nibus de cada manh\u00e3","junto \u00e0 cafeteira, logo cedo"])
s = replace_arr(s,'VX_TIMEBOX',["durante um m\u00eas","por seis semanas","durante uma temporada inteira","quarenta dias seguidos","semana ap\u00f3s semana"])
s = replace_arr(s,'VX_SOON',["antes do jantar","antes do meio-dia","a caminho do trabalho","antes de anoitecer","na pr\u00f3xima hora livre"])
s = replace_arr(s,'DAY_TITLES',[
 "O primeiro passo rumo a {C}","Quando {C} parece longe","{C} nas coisas pequenas","A obra lenta de {C}","{C} come\u00e7a hoje",
 "Onde {C} cria ra\u00edzes","{C} sem medo","Praticando {C}","Um cora\u00e7\u00e3o formado por {C}","{C} para o longo caminho",
 "Escolhendo {C} de novo","A for\u00e7a quieta de {C}","{C} na vida real","Quando Deus faz crescer {C}","{C} sob press\u00e3o",
 "O que {C} torna poss\u00edvel","{C} um passo por vez","Por que {C} importa a Deus","O dia em que {C} fica pessoal","{C} quando ningu\u00e9m v\u00ea",
 "O que Jesus disse sobre {C}","{C} em casa","{C} no trabalho","A promessa dentro de {C}","{C} num dia dif\u00edcil",
 "Como Deus constr\u00f3i {C}","{C} que vale herdar","O h\u00e1bito de {C}","{C} antes do p\u00f4r do sol","{C} e as pessoas que voc\u00ea ama",
 "A prova de {C}","{C} na espera"])
s = replace_arr(s,'mvTitles',[
 "O que Deus diz primeiro","O cora\u00e7\u00e3o da quest\u00e3o","A verdade debaixo da superf\u00edcie","Contando o custo","Dando o passo",
 "O car\u00e1ter de Deus","O nosso chamado","O obst\u00e1culo comum","A pr\u00e1tica concreta","Olhar para cima: quem Deus \u00e9",
 "Olhar para dentro: onde estamos","Olhar ao redor: quem precisa disto","Olhar adiante: o que faremos","A promessa","O problema",
 "A pr\u00e1tica","A pessoa ao seu lado","Enraizado no texto","Real na nossa hist\u00f3ria","Liberado para a semana",
 "A grande ideia","O meio honesto","O custo do sim","O primeiro passo"])

P1_NEW = '''var P1=[
          "\\u00ab"+C[1]+"\\u00bb. Essa \\u00e9 a promessa sobre toda esta jornada, e ela come\\u00e7a aqui. ",
          "Toda jornada faz uma promessa. Esta faz sem rodeios: "+C[1].replace(/\\.$/,'')+". O Dia Um come\\u00e7a a cumpri-la. ",
          "\\u00ab"+C[1]+"\\u00bb. Segure essa frase. As pr\\u00f3ximas semanas existem para torn\\u00e1-la verdade na sua vida real, come\\u00e7ando agora. ",
          "\\u00c9 para l\\u00e1 que "+t+" vai: "+C[1].replace(/\\.$/,'')+". Hoje se d\\u00e1 o primeiro passo. ",
          "Se esta jornada pudesse dizer uma s\\u00f3 frase, seria esta: "+C[1].replace(/\\.$/,'')+". Tudo o que vem desempacota isso. "
        ];'''
i = s.index('var P1=['); j = s.index('];', i)+2
s = s[:i] + P1_NEW + s[j:]

s = s.replace('" (NIV)"','" (ARC)"').replace("' (NIV)'","' (ARC)'").replace('(NIV)','(ARC)')
s = s.replace('"Days "','"Dias "').replace('" Devotional"','" \\u2014 Devocional"')

i = s.index('CARE_NOTE='); j = s.index('";', i)+2
s = s[:i] + 'CARE_NOTE="E uma palavra suave antes de come\\u00e7ar: se esta temporada parece pesada, voc\\u00ea n\\u00e3o precisa carreg\\u00e1-la sozinho. Compartilhe com seu pastor, um amigo de confian\\u00e7a ou um conselheiro profissional; pedir ajuda tamb\\u00e9m \\u00e9 um ato de f\\u00e9.";' + s[j:]
i = s.index('MONEY_NOTE='); j = s.index('";', i)+2
s = s[:i] + 'MONEY_NOTE="Uma palavra suave ao come\\u00e7ar: esta jornada compartilha princ\\u00edpios b\\u00edblicos e espirituais, n\\u00e3o assessoria financeira, jur\\u00eddica ou fiscal profissional; para decis\\u00f5es nessas \\u00e1reas, caminhe com um profissional qualificado.";' + s[j:]

# ---- MV verse texts -> Almeida Revista e Corrigida ----
MV_PT = {
 "The earth is the LORD's, and the fulness thereof; the world, and they that dwell therein.":"Do Senhor \u00e9 a terra e a sua plenitude, o mundo e aqueles que nele habitam.",
 "Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.":"Confia no Senhor de todo o teu cora\u00e7\u00e3o e n\u00e3o te estribes no teu pr\u00f3prio entendimento. Reconhece-o em todos os teus caminhos, e ele endireitar\u00e1 as tuas veredas.",
 "For where your treasure is, there will your heart be also.":"Porque onde estiver o vosso tesouro, a\u00ed estar\u00e1 tamb\u00e9m o vosso cora\u00e7\u00e3o.",
 "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.":"Mas buscai primeiro o Reino de Deus, e a sua justi\u00e7a, e todas essas coisas vos ser\u00e3o acrescentadas.",
 "He that is faithful in that which is least is faithful also in much.":"Quem \u00e9 fiel no m\u00ednimo tamb\u00e9m \u00e9 fiel no muito.",
 "I have learned, in whatsoever state I am, therewith to be content.":"Aprendi a contentar-me com o que tenho.",
 "God loveth a cheerful giver.":"Porque Deus ama ao que d\u00e1 com alegria.",
 "A good man leaveth an inheritance to his children's children.":"O homem de bem deixa uma heran\u00e7a aos filhos de seus filhos.",
 "It is more blessed to give than to receive.":"Mais bem-aventurada coisa \u00e9 dar do que receber.",
 "Godliness with contentment is great gain.":"Grande fonte de lucro \u00e9 a piedade com o contentamento.",
 "Commit thy works unto the LORD, and thy thoughts shall be established.":"Confia ao Senhor as tuas obras, e teus pensamentos ser\u00e3o estabelecidos.",
 "The blessing of the LORD, it maketh rich, and he addeth no sorrow with it.":"A b\u00ean\u00e7\u00e3o do Senhor \u00e9 que enriquece, e n\u00e3o acrescenta dores.",
 "Be strong and of a good courage; be not afraid, neither be thou dismayed: for the LORD thy God is with thee whithersoever thou goest.":"Esfor\u00e7a-te e tem bom \u00e2nimo; n\u00e3o pasmes, nem te espantes, porque o Senhor, teu Deus, \u00e9 contigo por onde quer que andares.",
 "I can do all things through Christ which strengtheneth me.":"Posso todas as coisas naquele que me fortalece.",
 "Casting all your care upon him; for he careth for you.":"Lan\u00e7ando sobre ele toda a vossa ansiedade, porque ele tem cuidado de v\u00f3s.",
 "This is the day which the LORD hath made; we will rejoice and be glad in it.":"Este \u00e9 o dia que fez o Senhor; regozijemo-nos e alegremo-nos nele.",
 "Thy word is a lamp unto my feet, and a light unto my path.":"L\u00e2mpada para os meus p\u00e9s \u00e9 a tua palavra e luz, para o meu caminho.",
 "Draw nigh to God, and he will draw nigh to you.":"Chegai-vos a Deus, e ele se chegar\u00e1 a v\u00f3s.",
 "Love one another; as I have loved you.":"Que vos ameis uns aos outros; como eu vos amei.",
 "As for me and my house, we will serve the LORD.":"Eu e a minha casa serviremos ao Senhor.",
 "Train up a child in the way he should go: and when he is old, he will not depart from it.":"Instrui o menino no caminho em que deve andar, e, at\u00e9 quando envelhecer, n\u00e3o se desviar\u00e1 dele.",
 "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.":"Assim resplande\u00e7a a vossa luz diante dos homens, para que vejam as vossas boas obras e glorifiquem o vosso Pai, que est\u00e1 nos c\u00e9us.",
 "Be ye doers of the word, and not hearers only.":"Sede cumpridores da palavra e n\u00e3o somente ouvintes.",
 "The LORD is my shepherd; I shall not want.":"O Senhor \u00e9 o meu pastor; nada me faltar\u00e1.",
 "Come unto me, all ye that labour and are heavy laden, and I will give you rest.":"Vinde a mim, todos os que estais cansados e oprimidos, e eu vos aliviarei.",
 "Be still, and know that I am God.":"Aquietai-vos e sabei que eu sou Deus.",
 "And we know that all things work together for good to them that love God.":"E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus.",
 "In every thing give thanks: for this is the will of God in Christ Jesus concerning you.":"Em tudo dai gra\u00e7as, porque esta \u00e9 a vontade de Deus em Cristo Jesus para convosco.",
 "Wait on the LORD: be of good courage, and he shall strengthen thine heart.":"Espera no Senhor, anima-te, e ele fortalecer\u00e1 o teu cora\u00e7\u00e3o; espera, pois, no Senhor.",
 "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.":"Porque eu bem sei os pensamentos que penso de v\u00f3s, diz o Senhor; pensamentos de paz e n\u00e3o de mal, para vos dar o fim que esperais.",
 "Behold, I make all things new.":"Eis que fa\u00e7o novas todas as coisas.",
 "Now faith is the substance of things hoped for, the evidence of things not seen.":"Ora, a f\u00e9 \u00e9 o firme fundamento das coisas que se esperam e a prova das coisas que se n\u00e3o veem.",
}
hit=0
for a,b in MV_PT.items():
    if a in s: s=s.replace(a,b); hit+=1
print("PT MV verses swapped:", hit)

open(P,'w').write(s)
r=subprocess.run(['node','--check',P],capture_output=True,text=True)
print("PT pack A applied | syntax:", "OK" if r.returncode==0 else r.stderr[:300])
