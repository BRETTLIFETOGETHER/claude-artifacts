# -*- coding: utf-8 -*-
# Prefix applier: each key is a unique PREFIX of an English string literal in engine.js.
# The applier locates the literal containing the prefix and replaces its full content.
import subprocess

def apply(P, M):
    s = open(P).read()
    hits = 0
    for pre, tr in sorted(M.items(), key=lambda kv: -len(kv[0])):
        i = s.find(pre)
        while i >= 0:
            a = i
            while a > 0 and not (s[a-1] == '"' and s[a-2] != '\\'): a -= 1
            b = i
            while b < len(s):
                if s[b] == '"' and s[b-1] != '\\': break
                b += 1
            if a > 0 and b < len(s):
                s = s[:a] + tr.replace('"', '\\"') + s[b:]
                hits += 1
                i = s.find(pre)
            else:
                break
    open(P, 'w').write(s)
    return hits

M = {}
# ---- RV1909 verse texts (prefix -> full RV1909) ----
M["Not that I speak in respect of want"] = "No lo digo en raz\u00f3n de indigencia, pues he aprendido a contentarme, cualquiera que sea mi estado."
M["A good man leaveth an inheritance"] = "El bueno dejar\u00e1 herederos a los hijos de sus hijos; y el haber del pecador, para el justo est\u00e1 guardado."
M["He that is faithful in that which is least"] = "El que es fiel en lo muy poco, tambi\u00e9n en lo m\u00e1s es fiel; y el que en lo muy poco es injusto, tambi\u00e9n en lo m\u00e1s es injusto."
M["Every man according as he purposeth in his heart"] = "Cada uno d\u00e9 como propuso en su coraz\u00f3n: no con tristeza, o por necesidad; porque Dios ama el dador alegre."
M["And whatsoever ye do, do it heartily"] = "Y todo lo que hag\u00e1is, hacedlo de \u00e1nimo, como al Se\u00f1or, y no a los hombres."
M["Fear thou not; for I am with thee"] = "No temas, que yo soy contigo; no desmayes, que yo soy tu Dios que te esfuerzo; siempre te ayudar\u00e9, siempre te sustentar\u00e9 con la diestra de mi justicia."
M["Peace I leave with you, my peace I give"] = "La paz os dejo, mi paz os doy: no como el mundo la da, yo os la doy. No se turbe vuestro coraz\u00f3n, ni tenga miedo."
M["Be still, and know that I am God: I will be exalted"] = "Estad quietos, y conoced que yo soy Dios; ensalzado ser\u00e9 entre las gentes, ensalzado ser\u00e9 en la tierra."
M["And if it seem evil unto you to serve the LORD"] = "Y si mal os parece servir a Jehov\u00e1, escogeos hoy a qui\u00e9n sirv\u00e1is; que yo y mi casa serviremos a Jehov\u00e1."
M["His lord said unto him, Well done"] = "Su se\u00f1or le dijo: Bien, buen siervo y fiel; sobre poco has sido fiel, sobre mucho te pondr\u00e9; entra en el gozo de tu se\u00f1or."
M["And let us not be weary in well doing"] = "No nos cansemos, pues, de hacer bien; que a su tiempo segaremos, si no hubi\u00e9remos desmayado."
M["If any of you lack wisdom"] = "Y si alguno de vosotros tiene falta de sabidur\u00eda, dem\u00e1ndela a Dios, el cual da a todos abundantemente, y no zahiere; y le ser\u00e1 dada."
M["Being confident of this very thing"] = "Estando confiado de esto, que el que comenz\u00f3 en vosotros la buena obra, la perfeccionar\u00e1 hasta el d\u00eda de Jesucristo."
M["And we know that all things work together"] = "Y sabemos que a los que a Dios aman, todas las cosas les ayudan a bien, es a saber, a los que conforme al prop\u00f3sito son llamados."
M["Go ye therefore, and teach all nations"] = "Por tanto, id, y doctrinad a todos los gentiles, bautiz\u00e1ndolos en el nombre del Padre, y del Hijo, y del Esp\u00edritu Santo."
M["For we are his workmanship"] = "Porque somos hechura suya, criados en Cristo Jes\u00fas para buenas obras, las cuales Dios prepar\u00f3 para que anduvi\u00e9semos en ellas."
M["I have fought a good fight"] = "He peleado la buena batalla, he acabado la carrera, he guardado la fe."
M["So teach us to number our days"] = "Ens\u00e9\u00f1anos de tal modo a contar nuestros d\u00edas, que traigamos al coraz\u00f3n sabidur\u00eda."
M["I am the vine, ye are the branches"] = "Yo soy la vid, vosotros los p\u00e1mpanos: el que est\u00e1 en m\u00ed, y yo en \u00e9l, \u00e9ste lleva mucho fruto; porque sin m\u00ed nada pod\u00e9is hacer."
M["Bring ye all the tithes into the storehouse"] = "Traed todos los diezmos al alfol\u00ed, y haya alimento en mi casa; y probadme ahora en esto, dice Jehov\u00e1 de los ej\u00e9rcitos, si no os abrir\u00e9 las ventanas de los cielos."
M["But who am I, and what is my people"] = "Porque \u00bfqui\u00e9n soy yo, y qui\u00e9n es mi pueblo, para que pudi\u00e9semos ofrecer voluntariamente cosas semejantes? Pues todo es tuyo, y lo recibido de tu mano te damos."
M["Except the LORD build the house"] = "Si Jehov\u00e1 no edificare la casa, en vano trabajan los que la edifican; si Jehov\u00e1 no guardare la ciudad, en vano vela la guarda."

# ---- audPhrase pool ----
M["your church family"] = "tu familia de la iglesia"
M["your marriage"] = "tu matrimonio"
M["your grandchildren's lives"] = "la vida de tus nietos"
M["this season of your life"] = "esta temporada de tu vida"
M["the families you serve"] = "las familias que sirves"
M["your leadership"] = "tu liderazgo"
M["what you've been entrusted with"] = "lo que te ha sido confiado"

# ---- PREGUNTAS (group discussion questions) ----
M["Where in your life right now is God inviting you to take {c}"] = "\u00bfEn qu\u00e9 parte de tu vida te est\u00e1 invitando Dios, ahora mismo, a tomarte {c} m\u00e1s en serio, y qu\u00e9 lo hace dif\u00edcil?"
M["What would the people closest to you say about how {c}"] = "\u00bfQu\u00e9 dir\u00edan las personas m\u00e1s cercanas a ti sobre c\u00f3mo aparece {c} en tu semana com\u00fan?"
M["If nothing about {ap} changed for a year"] = "Si nada cambiara en {ap} durante un a\u00f1o, \u00bfqu\u00e9 te costar\u00eda? \u00bfY qu\u00e9 har\u00eda posible un cambio peque\u00f1o?"
M["What is one belief about {c} you inherited"] = "\u00bfQu\u00e9 creencia sobre {c} heredaste sin examinarla, y la Escritura est\u00e1 de acuerdo con ella?"
M["When was the last time {c} cost you something real"] = "\u00bfCu\u00e1ndo fue la \u00faltima vez que {c} te cost\u00f3 algo real, y qu\u00e9 aprendiste al pagarlo?"
M["Who in your life models {c} well"] = "\u00bfQui\u00e9n en tu vida modela bien {c}, y qu\u00e9 podr\u00edas tomar prestado de su ejemplo esta semana?"
M["What is the biggest obstacle between you and {c}"] = "\u00bfCu\u00e1l es el mayor obst\u00e1culo entre t\u00fa y {c} ahora: miedo, ocupaci\u00f3n, duda, u otra cosa que puedas nombrar?"
M["If God answered your prayers about {c} today"] = "Si Dios respondiera hoy tus oraciones sobre {c}, \u00bfestar\u00eda tu agenda de ma\u00f1ana lista para la respuesta?"
M["What is one thing you would attempt in {ap}"] = "\u00bfQu\u00e9 intentar\u00edas en {ap} si confiaras plenamente el resultado a Dios?"
M["Where have you settled for managing a problem"] = "\u00bfD\u00f3nde te has conformado con administrar un problema que Dios ofrece transformar?"
M["What does your calendar say you believe about {c}"] = "\u00bfQu\u00e9 dice tu calendario que crees sobre {c}? No tus palabras: tu calendario."
M["What would it look like to give God the first fifteen minutes"] = "\u00bfC\u00f3mo ser\u00eda darle a Dios los primeros quince minutos de ma\u00f1ana en vez de las sobras?"
M["Who needs to hear what you read today"] = "\u00bfQui\u00e9n necesita escuchar lo que le\u00edste hoy, y qu\u00e9 te detiene de dec\u00edrselo?"
M["What is one habit quietly working against {c}"] = "\u00bfQu\u00e9 h\u00e1bito trabaja en silencio contra {c} en tu vida, y c\u00f3mo se ver\u00eda reemplazarlo?"
M["If your kids or closest friends copied your version of {c}"] = "Si tus hijos o tus amigos m\u00e1s cercanos copiaran tu versi\u00f3n de {c}, \u00bfte alegrar\u00eda?"
M["What are you asking God for that He may be waiting"] = "\u00bfQu\u00e9 le est\u00e1s pidiendo a Dios que quiz\u00e1 \u00c9l espera hacer a trav\u00e9s de ti y no solo por ti?"
M["Where does fear vote in your decisions about {ap}"] = "\u00bfD\u00f3nde vota el miedo en tus decisiones sobre {ap}, y qu\u00e9 eligir\u00eda el valor en su lugar?"
M["What would you stop doing this week if you believed rest"] = "\u00bfQu\u00e9 dejar\u00edas de hacer esta semana si creyeras que el descanso es mandato y no solo permiso?"
M["When did God prove Himself faithful to you in the past"] = "\u00bfCu\u00e1ndo se te prob\u00f3 Dios fiel en el pasado, y por qu\u00e9 cuesta recordarlo en el presente?"
M["What part of today's reading did you want to skip"] = "\u00bfQu\u00e9 parte de la lectura quisiste saltarte, y qu\u00e9 podr\u00eda estar enterrado ah\u00ed?"
M["How would this week change if you treated {c} as a relationship"] = "\u00bfC\u00f3mo cambiar\u00eda esta semana si trataras {c} como una relaci\u00f3n para disfrutar y no como un est\u00e1ndar que alcanzar?"
M["What is one honest sentence you have never prayed"] = "\u00bfQu\u00e9 frase honesta nunca has orado en voz alta, y qu\u00e9 tal si la oraras esta noche?"
M["Where are you strong enough to help someone else with {c}"] = "\u00bfD\u00f3nde eres lo bastante fuerte para ayudar a otro con {c}, y qui\u00e9n podr\u00eda ser ese alguien?"
M["What would generous look like today"] = "\u00bfC\u00f3mo se ver\u00eda lo generoso hoy: con dinero, s\u00ed, pero tambi\u00e9n con tiempo, cr\u00e9dito y atenci\u00f3n?"
M["If this journey works, what will be visibly different"] = "Si este recorrido funciona, \u00bfqu\u00e9 ser\u00e1 visiblemente distinto en {ap} dentro de sesenta d\u00edas?"
M["What is God's track record in your life, written down"] = "\u00bfCu\u00e1l es el historial de Dios en tu vida, escrito y no solo recordado? \u00bfAlguna vez lo has escrito?"
M["Which relationship in your life would change first"] = "\u00bfQu\u00e9 relaci\u00f3n de tu vida cambiar\u00eda primero si {c} echara ra\u00edces, y c\u00f3mo?"
M["What are you white-knuckling that today's passage"] = "\u00bfQu\u00e9 est\u00e1s apretando con los nudillos blancos que el pasaje de hoy te invita a entregar?"
M["When you picture God thinking about you"] = "Cuando imaginas a Dios pensando en ti, \u00bfqu\u00e9 expresi\u00f3n tiene su rostro, y qu\u00e9 dice la verdad de hoy sobre esa imagen?"
M["What is one question you would ask Jesus about {c}"] = "\u00bfQu\u00e9 pregunta le har\u00edas a Jes\u00fas sobre {c} si se sentara frente a ti esta noche? Hazla de todos modos. \u00c9l escucha."
M["Where has cynicism crept in wearing the costume"] = "\u00bfD\u00f3nde se col\u00f3 el cinismo disfrazado de sabidur\u00eda, y qu\u00e9 har\u00eda distinto la obediencia esperanzada?"
M["What did you underline today, and more importantly"] = "\u00bfQu\u00e9 subrayaste hoy y, m\u00e1s importante, qu\u00e9 har\u00e1s con eso antes de dormir?"

# ---- WELCOMES ----
M["Welcome to Session {n}. Before anything else, take a breath"] = "Bienvenidos a la Sesi\u00f3n {n}. Antes que nada, respiren. Esta hora no es una actuaci\u00f3n; es una mesa. Toda respuesta honesta es bienvenida aqu\u00ed."
M["Good to be together for Session {n}"] = "Qu\u00e9 bueno estar juntos para la Sesi\u00f3n {n}. Esta noche es simple: un pasaje, cuatro conversaciones cortas y una pr\u00e1ctica que vale la pena llevarse a casa."
M["Welcome to Session {n} of {t}. Tonight builds"] = "Bienvenidos a la Sesi\u00f3n {n} de {t}. Esta noche se construye sobre todo lo anterior, as\u00ed que empecemos poni\u00e9ndonos al d\u00eda antes de entrar."
M["Welcome back. Session {n} is not about having the right answers"] = "Bienvenidos de nuevo. La Sesi\u00f3n {n} no se trata de tener las respuestas correctas, sino de traer tu semana real a la sala. Empieza ah\u00ed y la noche se cuidar\u00e1 sola."
M["Glad you're here for Session {n}"] = "Qu\u00e9 alegr\u00eda tenerlos en la Sesi\u00f3n {n}. Regla de la casa, como siempre: escuchen con generosidad, compartan con honestidad y dejen que el silencio haga parte del trabajo."
M["Session {n}, friends. Phones down"] = "Sesi\u00f3n {n}, amigos. Tel\u00e9fonos abajo si pueden, caf\u00e9 arriba, y d\u00e9mosle a Dios la pr\u00f3xima hora sin prisa."
M["Welcome to Session {n}. Somebody in this circle"] = "Bienvenidos a la Sesi\u00f3n {n}. Alguien en este c\u00edrculo necesitaba esta noche m\u00e1s de lo que dir\u00e1 en voz alta. Seamos el tipo de grupo donde no tenga que decirlo."
M["Here we are at Session {n}. Quick reminder"] = "Aqu\u00ed estamos en la Sesi\u00f3n {n}. Recordatorio r\u00e1pido: nada de lo compartido en esta sala sale de ella. Las salas seguras hacen crecer gente honesta."
M["Welcome to Session {n} of {t}. If the week ran you over"] = "Bienvenidos a la Sesi\u00f3n {n} de {t}. Si la semana te pas\u00f3 por encima, est\u00e1s exactamente en el lugar correcto. Ven como est\u00e1s; vete un poco m\u00e1s liviano."
M["Session {n} tonight. The goal is not to finish"] = "Sesi\u00f3n {n} esta noche. La meta no es terminar las preguntas. La meta es encontrarnos de verdad unos con otros, y con Dios, dentro de ellas."

# ---- MOVE_EX ----
M["Read the passage aloud together, then let it breathe"] = "Lean el pasaje en voz alta juntos y d\u00e9jenlo respirar un momento antes de conversar. Noten lo que dice de Dios antes de notar lo que nos pide."
M["Have two people read the passage in turn"] = "Que dos personas lean el pasaje por turnos. Pregunta al grupo: \u00bfqu\u00e9 palabra o frase resalta, y por qu\u00e9 podr\u00eda Dios estar subray\u00e1ndola para ti esta semana?"
M["Read the passage, then retell it in your own words"] = "Lean el pasaje y luego cu\u00e9ntenlo con sus propias palabras como grupo. El lenguaje llano suele descubrir lo que el lenguaje familiar esconde."
M["Read slowly, twice. First time for the room"] = "Lean despacio, dos veces. La primera para la sala, la segunda para ti. Luego compartan una primera reacci\u00f3n honesta; sin pulir est\u00e1 bien."
M["Before discussing, sit with thirty seconds of quiet"] = "Antes de conversar, guarden treinta segundos de silencio despu\u00e9s de la lectura. Que el lector m\u00e1s joven empiece esta noche."
M["Read the passage and ask the oldest saint"] = "Lean el pasaje y pregunten al santo de m\u00e1s edad en la sala qu\u00e9 ha significado este vers\u00edculo a lo largo de sus a\u00f1os. La experiencia es un comentario que el dinero no compra."
M["Read the text, then have each person finish this sentence"] = "Lean el texto y que cada persona complete esta frase: si este vers\u00edculo es verdad, entonces mi semana..."
M["Read it once in full, then a second time stopping at every verb"] = "L\u00e9anlo una vez completo y una segunda vez deteni\u00e9ndose en cada verbo. Los verbos son donde la Escritura pide nuestras manos, no solo nuestras cabezas."
M["Read the passage and name together what it says about God's character"] = "Lean el pasaje y nombren juntos lo que dice del car\u00e1cter de Dios antes que nada. Qui\u00e9n es \u00c9l siempre va antes de lo que hacemos."
M["Read aloud, then ask: what would it look like if our group actually believed"] = "Lean en voz alta y pregunten: \u00bfc\u00f3mo se ver\u00eda que nuestro grupo de verdad creyera esto para el pr\u00f3ximo jueves?"
M["Read the passage, then let each person share where their eyes snagged"] = "Lean el pasaje y que cada persona comparta d\u00f3nde se le engancharon los ojos. Los enganches suelen ser invitaciones."
M["Read the text and ask the room: what does this make possible"] = "Lean el texto y pregunten a la sala: \u00bfqu\u00e9 hace posible esto que el lunes parec\u00eda imposible?"

# ---- MOVE_APP ----
M["Application: name one specific place this truth touches your week"] = "Aplicaci\u00f3n: nombra un lugar espec\u00edfico donde esta verdad toca tu semana, una decisi\u00f3n, una relaci\u00f3n, un h\u00e1bito, y dilo en voz alta al grupo."
M["Application: pair up for three minutes"] = "Aplicaci\u00f3n: en parejas por tres minutos. Cada persona responde: \u00bfc\u00f3mo se ver\u00eda obedecer esto para m\u00ed antes de volver a reunirnos?"
M["Application: write one sentence, privately"] = "Aplicaci\u00f3n: escribe una frase, en privado, que empiece con \u00abEsta semana voy a...\u00bb. Comparte solo si quieres. Las intenciones escritas sobreviven a las habladas."
M["Application: pick the smallest real step"] = "Aplicaci\u00f3n: elige el paso real m\u00e1s peque\u00f1o que sugiere este pasaje y recl\u00e1malo frente al grupo. Peque\u00f1o y declarado vence a grande y vago."
M["Application: identify one person outside this room"] = "Aplicaci\u00f3n: identifica a una persona fuera de esta sala que necesita esta verdad, y decidan juntos c\u00f3mo podr\u00eda llegarle esta semana."
M["Application: look at your own calendar for the next three days"] = "Aplicaci\u00f3n: mira tu calendario de los pr\u00f3ximos tres d\u00edas. \u00bfD\u00f3nde ser\u00e1 probado primero este pasaje? Nombra el momento ahora."
M["Application: choose a group-wide experiment"] = "Aplicaci\u00f3n: elijan un experimento de todo el grupo a partir de la verdad de esta noche, una pr\u00e1ctica compartida, la misma semana, y comparen notas en la pr\u00f3xima sesi\u00f3n."
M["Application: finish this sentence honestly"] = "Aplicaci\u00f3n: completa esta frase con honestidad: la raz\u00f3n por la que esto me cuesta es... Luego que el grupo ore exactamente por eso."
M["Application: turn tonight's big idea into a question"] = "Aplicaci\u00f3n: convierte la gran idea de esta noche en una pregunta que har\u00e1s en tu propia mesa esta semana, y vuelve contando qu\u00e9 dijo la mesa."
M["Application: pick one habit that quietly fights this truth"] = "Aplicaci\u00f3n: elige un h\u00e1bito que pelea en silencio contra esta verdad y nombra su reemplazo. Los h\u00e1bitos no se van; los desaloja un mejor inquilino."
M["Application: agree on one text message"] = "Aplicaci\u00f3n: acuerden un mensaje de texto que el grupo se enviar\u00e1 a mitad de semana, de cinco palabras o menos, atado a la idea de esta noche."
M["Application: decide what 'done' looks like by Sunday"] = "Aplicaci\u00f3n: decidan c\u00f3mo se ve \u00abhecho\u00bb para el domingo. La obediencia vaga se evapora; la obediencia definida se presenta."

# ---- REV ----
M["Exactly what our launch needed"] = "Exactamente lo que nuestro lanzamiento necesitaba"
M["Our groups actually finished this one"] = "Nuestros grupos de verdad terminaron este"
M["The daily rhythm is the secret"] = "El ritmo diario es el secreto"
M["Complete out of the box"] = "Completo desde el primer d\u00eda"
M["Best on-ramp to groups we've used"] = "La mejor rampa hacia los grupos que hemos usado"
M["We ran {t} across our whole church and the {fmt} rhythm"] = "Corrimos {t} en toda nuestra iglesia y el ritmo de {fmt} mantuvo a la gente m\u00e1s all\u00e1 de la segunda semana, algo que honestamente nunca nos hab\u00eda pasado. Los grupos siguen reuni\u00e9ndose."
M["What sold me was how complete it is"] = "Lo que me convenci\u00f3 fue lo completo que es. Devocional, estudio de grupo, bosquejos de sermones y la edici\u00f3n de ni\u00f1os alineados semana a semana, as\u00ed que las familias iban en una sola historia."
M["I've launched a lot of series that ended on Sunday"] = "He lanzado muchas series que terminaban el domingo. Esta no. La gente me citaba las lecturas diarias a mitad de semana, y tres de nuestros grupos siguen reuni\u00e9ndose por su cuenta."
M["As a {role}, I was watching for whether the {th} theme"] = "Como {role}, estaba atento a si el tema de {th} se sostendr\u00eda a lo largo de todo el recorrido. Se sostuvo: cada semana construy\u00f3 sobre la anterior, y el reto semanal lo hizo pr\u00e1ctico."
M["Our hosts are volunteers, not teachers"] = "Nuestros anfitriones son voluntarios, no maestros, y el formato de cuatro movimientos los llev\u00f3 por completo. Solo el consejo del texto de mitad de semana en el kit de l\u00edderes ya val\u00eda la pena."
M["Honest review: week one felt like any other study"] = "Rese\u00f1a honesta: la primera semana se sinti\u00f3 como cualquier estudio. Para la tercera, el ritmo diario hab\u00eda hecho algo que una serie de sermones nunca hace. Correremos otro."
M["I recommend campaigns to the families I serve"] = "Recomiendo campa\u00f1as a las familias que sirvo, y {t} es la que pongo en manos de quienes navegan exactamente esta temporada. B\u00edblicamente s\u00f3lida y pr\u00e1ctica."
M["Senior Pastor"] = "Pastor principal"
M["Executive Pastor"] = "Pastor ejecutivo"
M["Small Groups Pastor"] = "Pastor de grupos peque\u00f1os"
M["Discipleship Pastor"] = "Pastor de discipulado"
M["Lead Pastor"] = "Pastor l\u00edder"
M["Campus Pastor"] = "Pastor de campus"
M["Family Ministry Director"] = "Director de ministerio familiar"
M["Church Planter"] = "Plantador de iglesias"
M["Worship Pastor"] = "Pastor de adoraci\u00f3n"
M["Missions Director"] = "Director de misiones"
M["Financial Advisor"] = "Asesor financiero"
M["Estate Attorney"] = "Abogado de sucesiones"
M["Family Office Director"] = "Director de family office"
M["Wealth Manager"] = "Gestor de patrimonio"
M["Ministry Development Officer"] = "Oficial de desarrollo ministerial"
M["January 2026"] = "Enero de 2026"
M["February 2026"] = "Febrero de 2026"
M["March 2026"] = "Marzo de 2026"
M["April 2026"] = "Abril de 2026"
M["May 2026"] = "Mayo de 2026"
M["June 2026"] = "Junio de 2026"
M["November 2025"] = "Noviembre de 2025"
M["December 2025"] = "Diciembre de 2025"
M["October 2025"] = "Octubre de 2025"
M["September 2025"] = "Septiembre de 2025"

if __name__ == '__main__':
    P = '/home/claude/site_es/engine.js'
    h = apply(P, M)
    print('map1 applied:', h, 'literals')
    r = subprocess.run(['node', '--check', P], capture_output=True, text=True)
    print('syntax:', 'OK' if r.returncode == 0 else r.stderr[:200])
