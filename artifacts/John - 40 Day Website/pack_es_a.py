# -*- coding: utf-8 -*-
import re, sys

P = '/home/claude/site_es/engine.js'
s = open(P).read()

def replace_fn(src, name, code):
    i = src.index('function '+name)
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

# ---------- native generators (Spanish) ----------
G = {}
G['gOpen'] = '''function gOpen(r,m){ return pk(r,[
 "Antes de que el d\\u00eda tome velocidad, detente un momento aqu\\u00ed.",
 "Hay una conversaci\\u00f3n que Dios quiere tener contigo hoy, y empieza en esta p\\u00e1gina.",
 "No llegaste a este d\\u00eda por accidente; algo en tu semana necesita exactamente esta palabra.",
 "El d\\u00eda de hoy trae su propia agenda, pero primero escucha esta.",
 "Respira. Lo que sigue no es informaci\\u00f3n para saber m\\u00e1s, sino una invitaci\\u00f3n para vivir distinto."]); }'''
G['gTension'] = '''function gTension(r,m){ return pk(r,[
 "Porque seamos honestos: en el tema de "+m.c+", la distancia entre lo que creemos y lo que practicamos suele ser grande.",
 "Y aqu\\u00ed est\\u00e1 la tensi\\u00f3n: casi nadie discute esta verdad, y casi nadie la vive sin ayuda.",
 "Lo dif\\u00edcil no es entender esto; lo dif\\u00edcil es que el martes por la tarde lo recuerde nuestro calendario.",
 "El problema nunca fue la falta de informaci\\u00f3n, sino la falta de pr\\u00e1ctica en los d\\u00edas comunes.",
 "Una vida puede ir a la deriva un d\\u00eda sin examinar a la vez; hoy interrumpe esa deriva."]); }'''
G['gHook'] = '''function gHook(r,m){ return pk(r,[
 "Hay una pregunta esperando debajo de este d\\u00eda: \\u00bfqu\\u00e9 pasar\\u00eda si "+m.c+" dejara de ser una palabra y empezara a ser un h\\u00e1bito?",
 "Tarde o temprano llega un d\\u00eda como hoy, cuando la l\\u00ednea subrayada de ayer quiere volverse la huella de hoy.",
 "Hoy el recorrido se vuelve personal: no se trata de lo que otros deber\\u00edan hacer, sino de lo que t\\u00fa puedes empezar.",
 "Algunas verdades se aprenden leyendo; esta se aprende caminando, y hoy toca dar un paso.",
 "Si has le\\u00eddo sobre "+m.c+" antes, hoy deja que el texto te lea a ti."]); }'''
G['gRead'] = '''function gRead(r,m,scr){ return pk(r,[
 "Abre la lectura de hoy, "+scr+", antes de que el d\\u00eda opine. ",
 "La lectura de hoy es "+scr+"; l\\u00e9ela despacio, como quien escucha y no como quien revisa. ",
 "Busca "+scr+" y qu\\u00e9date un minuto m\\u00e1s de lo c\\u00f3modo. ",
 "Hoy el texto es "+scr+", y conviene leerlo dos veces: una para entender, otra para obedecer. ",
 "Antes de seguir, lee "+scr+"; lo que viene abajo supone que el texto ya habl\\u00f3 primero. "]); }'''
G['gTruth'] = '''function gTruth(r,m){ return pk(r,[
 "Lo sorprendente del pasaje es que no pide sentimientos nuevos, sino decisiones peque\\u00f1as y repetidas.",
 "La Escritura no tiene prisa aqu\\u00ed: planta una verdad y espera la cosecha en los d\\u00edas comunes.",
 "N\\u00f3talo bien: el texto asume que esto se vive en casa, en el trabajo y en la mesa, no solo en el templo.",
 "Dios no est\\u00e1 pidiendo perfecci\\u00f3n en esto; est\\u00e1 formando fidelidad, un d\\u00eda a la vez.",
 "El pasaje no decora la vida; la reordena, empezando por lo que parec\\u00eda demasiado peque\\u00f1o para importar."]); }'''
G['gGroundWrap'] = '''function gGroundWrap(r,m,core){ return pk(r,[
 "Det\\u00e9n aqu\\u00ed el pensamiento: "+core,
 "Esta es la roca debajo del d\\u00eda: "+core,
 "Si hoy guardas una sola idea, que sea esta: "+core,
 "Los que caminaron antes lo dijeron as\\u00ed: "+core,
 "Conviene decirlo sin adorno: "+core]); }'''
G['gStory'] = '''function gStory(r){
 var who=pk(r,VX_PEOPLE), where=pk(r,VX_PLACE), span=pk(r,VX_TIMEBOX);
 var prac=pk(r,[
  "guard\\u00f3 una sola palabra de la lectura de cada d\\u00eda en una nota adhesiva",
  "or\\u00f3 una oraci\\u00f3n de una l\\u00ednea por cada persona bajo su techo, por nombre",
  "escribi\\u00f3 cada noche una l\\u00ednea sobre d\\u00f3nde apareci\\u00f3 Dios",
  "ley\\u00f3 el pasaje antes de tocar el tel\\u00e9fono",
  "agradeci\\u00f3 a una persona espec\\u00edfica por algo espec\\u00edfico",
  "regal\\u00f3 algo peque\\u00f1o pero real antes del atardecer",
  "memoriz\\u00f3 un vers\\u00edculo por semana en el auto",
  "le envi\\u00f3 el vers\\u00edculo del d\\u00eda a un amigo, sin comentario"]);
 var pay=pk(r,[
  "Las circunstancias no cambiaron mucho, dicen, pero casi todas sus respuestas s\\u00ed.",
  "Nadie lo not\\u00f3 la primera semana; para la sexta, todos lo notaban.",
  "No fue dram\\u00e1tico, fue acumulativo, y eso result\\u00f3 ser mejor.",
  "Lo que empez\\u00f3 como disciplina termin\\u00f3 pareciendo descanso.",
  "Su casa no se volvi\\u00f3 perfecta, pero s\\u00ed m\\u00e1s honesta y m\\u00e1s liviana."]);
 return "Conocemos la historia de "+who+" que, "+where+" y "+span+", "+prac+". "+pay; }'''
G['gStoryMoral'] = '''function gStoryMoral(r,m){ return pk(r,[
 "Hazlo una vez y es un acto; hazlo a diario y se vuelve "+m.c+" con ra\\u00edces.",
 "As\\u00ed crece esto en la vida real: no por impulsos grandes, sino por fidelidades peque\\u00f1as.",
 "La lecci\\u00f3n no es copiar su pr\\u00e1ctica, sino elegir una propia y sostenerla.",
 "Historias as\\u00ed no prueban una f\\u00f3rmula; muestran una direcci\\u00f3n, y la direcci\\u00f3n est\\u00e1 abierta hoy.",
 "Dios suele esconder cosechas grandes dentro de h\\u00e1bitos peque\\u00f1os."]); }'''
G['gApply'] = '''function gApply(r,m){ return pk(r,[
 "Ponle a esto una puerta concreta: un trayecto, una comida, un umbral, y decide ahora c\\u00f3mo responder\\u00e1s antes de que llegue el momento.",
 "Nombra la hora del d\\u00eda donde esto ser\\u00e1 probado y sal a su encuentro a prop\\u00f3sito; los h\\u00e1bitos cuelgan de ganchos.",
 "Escoge una acci\\u00f3n tan peque\\u00f1a que no puedas fallar, y tan real que alguien la note.",
 "Ponlo en el calendario, con tinta; las emboscadas pierden contra las citas.",
 "Antes de cerrar la p\\u00e1gina, decide el d\\u00f3nde y el cu\\u00e1ndo; la intenci\\u00f3n sin direcci\\u00f3n se eval\\u00fapora.",
 "Cu\\u00e9ntale a una persona lo que intentar\\u00e1s hoy; lo dicho en voz alta pesa distinto."]); }'''
G['gClose'] = '''function gClose(r,m,d){ return pk(r,[
 "Deja que el d\\u00eda termine m\\u00e1s callado de lo que empez\\u00f3: treinta segundos sin prisa con el vers\\u00edculo, y permiso para dejar el resto en manos de Dios.",
 "No confundas lo silencioso con lo in\\u00fatil; la cosecha nunca pregunta c\\u00f3mo se sinti\\u00f3 la siembra del D\\u00eda "+d+".",
 "Un pensamiento antes de cerrar el D\\u00eda "+d+": si llegaste sin fuerzas, llegaste a la p\\u00e1gina correcta; Dios hace mucho con poco.",
 "Hoy no se calific\\u00f3 nada; se plant\\u00f3 algo. Duerme sobre eso.",
 "Sea lo que sea que el d\\u00eda logr\\u00f3 o no logr\\u00f3, te presentaste a escuchar a Dios, y eso ya cambi\\u00f3 la direcci\\u00f3n."]); }'''
G['gDeeper'] = '''function gDeeper(r,m,d){ return pk(r,[
 "Si quieres ir m\\u00e1s hondo hoy, vuelve al pasaje y det\\u00e9nte en cada verbo; los verbos son donde la Escritura pide manos.",
 "Una pregunta extra para el margen del d\\u00eda: \\u00bfa qui\\u00e9n conoces que vive bien esto, y qu\\u00e9 podr\\u00edas imitar esta semana?",
 "Para los que quieren m\\u00e1s: escribe en una l\\u00ednea qu\\u00e9 te est\\u00e1 pidiendo Dios en el tema de "+m.c+", y ponle fecha.",
 "Antes de dormir, repasa el d\\u00eda buscando una sola huella de Dios; escribirla toma un minuto y ancla la memoria.",
 "Si el d\\u00eda te dej\\u00f3 una pregunta sin responder, gu\\u00e1rdala para tu grupo esta semana; las preguntas honestas son combustible."]); }'''
G['gPrayer'] = '''function gPrayer(r,m){ return pk(r,[
 "Padre, gracias por encontrarme hoy en estas palabras. Dame una oportunidad clara de practicar "+m.c+" antes de que termine el d\\u00eda, y el valor de tomarla. Am\\u00e9n.",
 "Se\\u00f1or Jes\\u00fas, has sido m\\u00e1s paciente conmigo que yo mismo. Interr\\u00fampeme en el momento justo hoy, y ens\\u00e9\\u00f1ame a responder como t\\u00fa. Am\\u00e9n.",
 "Dios, no te pido un d\\u00eda f\\u00e1cil sino un coraz\\u00f3n atento. Que lo que le\\u00ed esta ma\\u00f1ana tenga la \\u00faltima palabra esta noche. Am\\u00e9n.",
 "Esp\\u00edritu Santo, t\\u00fa conoces la hora exacta en que esto ser\\u00e1 dif\\u00edcil hoy. Ll\\u00e9game primero. Am\\u00e9n.",
 "Padre, haz peque\\u00f1a mi prisa y grande tu voz. Hoy quiero obedecer en algo concreto, aunque sea peque\\u00f1o. Am\\u00e9n."]); }'''
G['gQuestion'] = '''function gQuestion(r,m){ return pk(r,[
 "Si nada de tu vida cambiara en un a\\u00f1o, \\u00bfqu\\u00e9 desear\\u00edas haber empezado hoy?",
 "\\u00bfEn qu\\u00e9 parte de tu vida te est\\u00e1 invitando Dios, ahora mismo, a tomarte "+m.c+" m\\u00e1s en serio?",
 "\\u00bfQui\\u00e9n en tu vida modela bien esto, y qu\\u00e9 podr\\u00edas empezar a imitar esta semana?",
 "\\u00bfCu\\u00e1ndo fue la \\u00faltima vez que Dios te prob\\u00f3 fiel, y qu\\u00e9 aprendiste en la espera?",
 "\\u00bfQu\\u00e9 har\\u00eda posible esta verdad que el lunes parec\\u00eda imposible?"]); }'''
G['gStepCore'] = '''function gStepCore(r,m,weekly){ return pk(r,weekly?[
 "elige un momento ordinario cada d\\u00eda, un trayecto, una comida, un umbral, y deja que el vers\\u00edculo de la semana lo acompa\\u00f1e",
 "pide perd\\u00f3n por una cosa, limpiamente, sin coma y sin excusa, esta semana",
 "da algo peque\\u00f1o pero real cada d\\u00eda antes del atardecer",
 "camina una vuelta lenta y ora por lo que realmente veas, cada d\\u00eda hasta el domingo",
 "escribe cada noche una l\\u00ednea sobre d\\u00f3nde apareci\\u00f3 Dios en tu d\\u00eda"]:[
 "di el vers\\u00edculo en voz alta tres veces: ma\\u00f1ana, mediod\\u00eda y noche",
 "env\\u00eda el vers\\u00edculo de hoy a un amigo, sin comentario",
 "agradece a una persona espec\\u00edfica por algo espec\\u00edfico antes de la cena",
 "haz una pausa de sesenta segundos antes de tu hora m\\u00e1s dif\\u00edcil y entr\\u00e9gasela a Dios",
 "deja el tel\\u00e9fono fuera de la primera media hora de la ma\\u00f1ana y dale ese espacio a la lectura"]); }'''
G['gStep'] = '''function gStep(r,m){ return "Paso de hoy: "+gStepCore(r,m,false)+"."; }'''
G['gPractice'] = '''function gPractice(r,m){ return "La pr\\u00e1ctica de esta semana: "+gStepCore(r,m,true)+". Hazlo una vez y es un acto; hazlo a diario y se vuelve un camino."; }'''
G['gCarry'] = '''function gCarry(r,d){
 var lead=pk(r,["lleva el vers\\u00edculo de esta semana a ","camina el vers\\u00edculo de esta semana hacia ","deja que el vers\\u00edculo de la semana te acompa\\u00f1e en "]);
 var where=pk(r,["un momento espec\\u00edfico "+pk(r,VX_SOON),"la hora que menos ganas tienes de vivir hoy","un mandado ordinario de hoy","la pr\\u00f3xima conversaci\\u00f3n dif\\u00edcil","los \\u00faltimos minutos antes de dormir"]);
 var how=pk(r,[" y deja que tenga all\\u00ed la \\u00faltima palabra."," y dilo una vez en voz alta si puedes."," y deja que interrumpa lo que normalmente manda ah\\u00ed."]);
 return lead+where+how; }'''
G['gTomorrow'] = '''function gTomorrow(r,d,n,nextPart){
 if(d>=n) return pk(r,[
  "Ma\\u00f1ana mirar\\u00e1s todo el camino recorrido; termina hoy con gratitud por lo lejos que Dios te ha tra\\u00eddo.",
  "La \\u00faltima p\\u00e1gina est\\u00e1 cerca. Termina hoy agradecido y ven listo para recordarlo todo.",
  "Un amanecer m\\u00e1s y el recorrido se vuelve celebraci\\u00f3n. Camina bien el paso de hoy."]);
 var lead=pk(r,["Ma\\u00f1ana el recorrido contin\\u00faa","El camino sigue ma\\u00f1ana","El D\\u00eda "+(d+1)+" ya espera","La p\\u00e1gina siguiente se abre por la ma\\u00f1ana"]);
 var mid=nextPart?pk(r,[", cruzando hacia \\u00ab"+nextPart+"\\u00bb",", y con \\u00e9l un tramo nuevo llamado \\u00ab"+nextPart+"\\u00bb"]):"";
 var tail=pk(r,["; hoy basta con el paso de hoy.","; no cargues ma\\u00f1ana antes de tiempo.","; duerme y vuelve."]);
 return lead+mid+tail; }'''
G['gProvision'] = '''function gProvision(r,occ){
 var a=pk(r,["Y porque este recorrido fue pensado con "+occ+" en mente,","Este recorrido fue formado para "+occ+", as\\u00ed que","Construido como fue para "+occ+","]);
 var b=pk(r,[" no te sorprendas si el paso de hoy cae cerca de casa; eso es dise\\u00f1o, no accidente."," si hoy se siente extra\\u00f1amente oportuno, lo es: la provisi\\u00f3n de cerca parece coincidencia."," el reto de hoy puede calzar inc\\u00f3modamente bien con tu semana; t\\u00f3malo como una bondad."]);
 return a+b; }'''
G['gPromise'] = '''function gPromise(r,t,sub,c){
 var s2=sub?String(sub).replace(/\\.$/,''):null;
 var pool=[
  "Recuerda hacia d\\u00f3nde va todo esto: "+t+" no es un curso que aprobar, sino un camino que caminar.",
  "A mitad de la marcha conviene levantar la vista: Dios est\\u00e1 formando "+c+" en ti, y no tiene prisa ni duda.",
  "Este recorrido hizo una promesa al empezar, y cada d\\u00eda como hoy la va cumpliendo en silencio."];
 if(s2){ pool.push("\\u00ab"+s2+"\\u00bb. Esa sigue siendo la frase sobre todo el viaje, y hoy dio un paso m\\u00e1s hacia ser verdad."); }
 return pk(r,pool); }'''
G['gAnchorLabel'] = '''function gAnchorLabel(r){ return pk(r,["Ancla para hoy","Lleva esto hoy","El ancla de hoy","Una l\\u00ednea para guardar","Sost\\u00e9n esta l\\u00ednea hoy"]); }'''
G['gScrFirst'] = '''function gScrFirst(r,m,scr){ return pk(r,[
 "Empieza hoy por el texto: "+scr+". L\\u00e9elo antes de leer nada m\\u00edo, porque el d\\u00eda entero se apoya ah\\u00ed.",
 "Hoy la Escritura va primero: "+scr+". Lo dem\\u00e1s de esta p\\u00e1gina solo ayuda a cargarla.",
 "Abre "+scr+" ahora, despacio; el resto del d\\u00eda de hoy es comentario."]); }'''

for name, code in G.items():
    s = replace_fn(s, name, code)

# ---------- pools ----------
s = replace_arr(s,'VX_PEOPLE',["una mam\u00e1 joven","un enfermero de turno nocturno","un maestro jubilado","una due\u00f1a de negocio","un padre soltero","una estudiante universitaria","un abuelo reci\u00e9n estrenado","una pareja con la agenda llena"])
s = replace_arr(s,'VX_PLACE',["en la mesa de la cocina","en el auto antes de entrar","en la sala, con la casa dormida","en el descanso del mediod\u00eda","en el autob\u00fas de cada ma\u00f1ana","junto a la cafetera, a primera hora"])
s = replace_arr(s,'VX_TIMEBOX',["durante un mes","por seis semanas","durante toda una temporada","cuarenta d\u00edas seguidos","semana tras semana"])
s = replace_arr(s,'VX_MOMENT',["En esta temporada","Justo en estos d\u00edas","En medio de una semana llena","En el punto medio del a\u00f1o","En d\u00edas como estos"])
s = replace_arr(s,'VX_SOON',["antes de la cena","antes del mediod\u00eda","camino al trabajo","antes de que anochezca","en la pr\u00f3xima hora libre"])
s = replace_arr(s,'DAY_TITLES',[
 "El primer paso hacia {C}","Cuando {C} parece lejos","{C} en las cosas peque\u00f1as","La obra lenta de {C}","{C} empieza hoy",
 "Donde {C} echa ra\u00edces","{C} sin miedo","Practicando {C}","Un coraz\u00f3n formado por {C}","{C} para el largo camino",
 "Eligiendo {C} otra vez","La fuerza callada de {C}","{C} en la vida real","Cuando Dios hace crecer {C}","{C} bajo presi\u00f3n",
 "Lo que {C} hace posible","{C} un paso a la vez","Por qu\u00e9 {C} le importa a Dios","El d\u00eda en que {C} se vuelve personal","{C} cuando nadie mira",
 "Lo que Jes\u00fas dijo sobre {C}","{C} en casa","{C} en el trabajo","La promesa dentro de {C}","{C} en un d\u00eda dif\u00edcil",
 "C\u00f3mo Dios construye {C}","{C} que vale la pena heredar","El h\u00e1bito de {C}","{C} antes del atardecer","{C} y la gente que amas",
 "La prueba de {C}","{C} en la espera"])
s = replace_arr(s,'mvTitles',[
 "Lo que Dios dice primero","El coraz\u00f3n del asunto","La verdad debajo de la superficie","Contando el costo","Dando el paso",
 "El car\u00e1cter de Dios","Nuestro llamado","El obst\u00e1culo com\u00fan","La pr\u00e1ctica concreta","Mirar arriba: qui\u00e9n es Dios",
 "Mirar adentro: d\u00f3nde estamos","Mirar alrededor: qui\u00e9n necesita esto","Mirar adelante: qu\u00e9 haremos","La promesa","El problema",
 "La pr\u00e1ctica","La persona a tu lado","Arraigado en el texto","Real en nuestra historia","Liberado hacia la semana",
 "La gran idea","El medio honesto","El costo del s\u00ed","El primer paso"])

# ---------- devotional inline strings ----------
P1_NEW = '''var P1=[
          "\\u00ab"+C[1]+"\\u00bb. Esa es la promesa sobre todo este recorrido, y empieza aqu\\u00ed. ",
          "Todo recorrido hace una promesa. Este la hace sin rodeos: "+C[1].replace(/\\.$/,'')+". El D\\u00eda Uno empieza a cumplirla. ",
          "\\u00ab"+C[1]+"\\u00bb. Sost\\u00e9n esa frase. Las pr\\u00f3ximas semanas existen para hacerla verdad en tu vida real, empezando ahora. ",
          "Hacia all\\u00e1 va "+t+": "+C[1].replace(/\\.$/,'')+". Hoy se da el primer paso. ",
          "Si este recorrido pudiera decir una sola frase, ser\\u00eda esta: "+C[1].replace(/\\.$/,'')+". Todo lo que sigue la desempaca. "
        ];'''
i = s.index('var P1=['); j = s.index('];', i)+2
s = s[:i] + P1_NEW + s[j:]

s = s.replace('" (NIV)"','" (RV 1909)"').replace("' (NIV)'","' (RV 1909)'").replace('(NIV)','(RV 1909)')
s = s.replace('"Days "','"D\\u00edas "').replace('" Devotional"','" \\u2014 Devocional"')

# CARE / MONEY notes
i = s.index('CARE_NOTE='); j = s.index('";', i)+2
s = s[:i] + 'CARE_NOTE="Y una palabra suave antes de empezar: si esta temporada se siente pesada, no tienes que cargarla solo. Comp\\u00e1rtela con tu pastor, un amigo de confianza o un consejero profesional; pedir ayuda tambi\\u00e9n es un acto de fe.";' + s[j:]
i = s.index('MONEY_NOTE='); j = s.index('";', i)+2
s = s[:i] + 'MONEY_NOTE="Una palabra suave al empezar: este recorrido comparte principios b\\u00edblicos y espirituales, no asesor\\u00eda financiera, legal ni fiscal profesional; para decisiones en esas \\u00e1reas, camina con un profesional calificado.";' + s[j:]

# ---------- MV verse texts -> Reina-Valera 1909 ----------
MV_ES = {
 "The earth is the LORD's, and the fulness thereof; the world, and they that dwell therein.":"De Jehov\u00e1 es la tierra y su plenitud; el mundo, y los que en \u00e9l habitan.",
 "Trust in the LORD with all thine heart; and lean not unto thine own understanding. In all thy ways acknowledge him, and he shall direct thy paths.":"F\u00edate de Jehov\u00e1 de todo tu coraz\u00f3n, y no estribes en tu prudencia. Recon\u00f3celo en todos tus caminos, y \u00e9l enderezar\u00e1 tus veredas.",
 "For where your treasure is, there will your heart be also.":"Porque donde estuviere vuestro tesoro, all\u00ed estar\u00e1 vuestro coraz\u00f3n.",
 "But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.":"Mas buscad primeramente el reino de Dios y su justicia, y todas estas cosas os ser\u00e1n a\u00f1adidas.",
 "He that is faithful in that which is least is faithful also in much.":"El que es fiel en lo muy poco, tambi\u00e9n en lo m\u00e1s es fiel.",
 "I have learned, in whatsoever state I am, therewith to be content.":"He aprendido a contentarme, cualquiera que sea mi estado.",
 "God loveth a cheerful giver.":"Porque Dios ama el dador alegre.",
 "A good man leaveth an inheritance to his children's children.":"El bueno dejar\u00e1 herederos a los hijos de sus hijos.",
 "It is more blessed to give than to receive.":"M\u00e1s bienaventurada cosa es dar que recibir.",
 "Godliness with contentment is great gain.":"Empero grande granjer\u00eda es la piedad con contentamiento.",
 "Commit thy works unto the LORD, and thy thoughts shall be established.":"Encomienda a Jehov\u00e1 tus obras, y tus pensamientos ser\u00e1n afirmados.",
 "The blessing of the LORD, it maketh rich, and he addeth no sorrow with it.":"La bendici\u00f3n de Jehov\u00e1 es la que enriquece, y no a\u00f1ade tristeza con ella.",
 "Be strong and of a good courage; be not afraid, neither be thou dismayed: for the LORD thy God is with thee whithersoever thou goest.":"Esfu\u00e9rzate y s\u00e9 valiente; no temas ni desmayes, porque Jehov\u00e1 tu Dios ser\u00e1 contigo en donde quiera que fueres.",
 "I can do all things through Christ which strengtheneth me.":"Todo lo puedo en Cristo que me fortalece.",
 "Casting all your care upon him; for he careth for you.":"Echando toda vuestra solicitud en \u00e9l, porque \u00e9l tiene cuidado de nosotros.",
 "This is the day which the LORD hath made; we will rejoice and be glad in it.":"Este es el d\u00eda que hizo Jehov\u00e1; nos gozaremos y alegraremos en \u00e9l.",
 "Thy word is a lamp unto my feet, and a light unto my path.":"L\u00e1mpara es a mis pies tu palabra, y lumbrera a mi camino.",
 "Draw nigh to God, and he will draw nigh to you.":"Allegaos a Dios, y \u00e9l se allegar\u00e1 a vosotros.",
 "Love one another; as I have loved you.":"Que os am\u00e9is unos a otros; como os he amado.",
 "As for me and my house, we will serve the LORD.":"Yo y mi casa serviremos a Jehov\u00e1.",
 "Train up a child in the way he should go: and when he is old, he will not depart from it.":"Instruye al ni\u00f1o en su carrera; aun cuando fuere viejo no se apartar\u00e1 de ella.",
 "Let your light so shine before men, that they may see your good works, and glorify your Father which is in heaven.":"As\u00ed alumbre vuestra luz delante de los hombres, para que vean vuestras obras buenas, y glorifiquen a vuestro Padre que est\u00e1 en los cielos.",
 "Be ye doers of the word, and not hearers only.":"Sed hacedores de la palabra, y no tan solamente oidores.",
 "The LORD is my shepherd; I shall not want.":"Jehov\u00e1 es mi pastor; nada me faltar\u00e1.",
 "Come unto me, all ye that labour and are heavy laden, and I will give you rest.":"Venid a m\u00ed todos los que est\u00e1is trabajados y cargados, que yo os har\u00e9 descansar.",
 "Be still, and know that I am God.":"Estad quietos, y conoced que yo soy Dios.",
 "And we know that all things work together for good to them that love God.":"Y sabemos que a los que a Dios aman, todas las cosas les ayudan a bien.",
 "In every thing give thanks: for this is the will of God in Christ Jesus concerning you.":"Dad gracias en todo; porque esta es la voluntad de Dios para con vosotros en Cristo Jes\u00fas.",
 "Wait on the LORD: be of good courage, and he shall strengthen thine heart.":"Aguarda a Jehov\u00e1; esfu\u00e9rzate, y aliente \u00e9l tu coraz\u00f3n; s\u00ed, espera a Jehov\u00e1.",
 "For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.":"Porque yo s\u00e9 los pensamientos que tengo acerca de vosotros, dice Jehov\u00e1, pensamientos de paz, y no de mal, para daros el fin que esper\u00e1is.",
 "Behold, I make all things new.":"He aqu\u00ed, yo hago nuevas todas las cosas.",
 "Now faith is the substance of things hoped for, the evidence of things not seen.":"Es pues la fe la sustancia de las cosas que se esperan, la demostraci\u00f3n de las cosas que no se ven.",
}
hit=0
for a,b in MV_ES.items():
    if a in s: s=s.replace(a,b); hit+=1
print("MV verses swapped:", hit, "of", len(MV_ES))

open(P,'w').write(s)
import subprocess
r=subprocess.run(['node','--check',P],capture_output=True,text=True)
print("pack A applied | syntax:", "OK" if r.returncode==0 else r.stderr[:300])
