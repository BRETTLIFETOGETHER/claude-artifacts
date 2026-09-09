import json, re

M = {"es":{},"pt":{}}
def both(en, es, pt):
    M["es"][en]=es; M["pt"][en]=pt

# proper-noun repair (applied after, via direct fix)
# index testimonials + paras + faq
both("We launched a 40-day campaign as our new curriculum. Now people are doing it on their commutes and at work. We are no longer hearing that people feel \u2018not discipled.\u2019",
 "Lanzamos una campa\u00f1a de 40 d\u00edas como nuestro nuevo curr\u00edculo. Ahora la gente la hace en el trayecto al trabajo y en la oficina. Ya no escuchamos que las personas se sientan \u2018sin discipular\u2019.",
 "Lan\u00e7amos uma campanha de 40 dias como nosso novo curr\u00edculo. Agora as pessoas fazem no trajeto e no trabalho. N\u00e3o ouvimos mais que as pessoas se sentem \u2018sem discipulado\u2019.")
both("Because of my role, people come to me for advice on parenting, marriage, and finances. I almost always point them to a campaign that speaks to the season they\u2019re in.",
 "Por mi rol, la gente me pide consejo sobre crianza, matrimonio y finanzas. Casi siempre los dirijo a una campa\u00f1a que habla a la temporada en la que est\u00e1n.",
 "Pelo meu papel, as pessoas me pedem conselho sobre cria\u00e7\u00e3o de filhos, casamento e finan\u00e7as. Quase sempre indico uma campanha que fala \u00e0 temporada em que est\u00e3o.")
both("A campaign gave our whole church shared language for forty days. Celebration Sunday was the most unified our church has felt in years.",
 "Una campa\u00f1a le dio a toda nuestra iglesia un lenguaje com\u00fan por cuarenta d\u00edas. El Domingo de Celebraci\u00f3n fue lo m\u00e1s unida que se ha sentido nuestra iglesia en a\u00f1os.",
 "Uma campanha deu \u00e0 nossa igreja inteira uma linguagem comum por quarenta dias. O Domingo de Celebra\u00e7\u00e3o foi o momento mais unido da nossa igreja em anos.")
both("From the rooms where the Purpose Driven Life campaign was designed to 500+ church partnerships and tens of millions of participants — this platform puts that entire methodology within reach of every church.",
 "Desde las salas donde se dise\u00f1\u00f3 la campa\u00f1a de Una Vida con Prop\u00f3sito hasta m\u00e1s de 500 alianzas con iglesias y decenas de millones de participantes: esta plataforma pone toda esa metodolog\u00eda al alcance de cada iglesia.",
 "Das salas onde a campanha de Uma Vida com Prop\u00f3sitos foi desenhada at\u00e9 mais de 500 parcerias com igrejas e dezenas de milh\u00f5es de participantes: esta plataforma coloca toda essa metodologia ao alcance de cada igreja.")
both("A campaign is a coordinated discipleship experience built around one theme for a defined season — weekend teaching, a daily devotional, small-group curriculum, family editions, and a clear next step, all moving together so the message becomes part of daily life.",
 "Una campa\u00f1a es una experiencia de discipulado coordinada alrededor de un tema por una temporada definida: ense\u00f1anza de fin de semana, devocional diario, curr\u00edculo de grupos, ediciones familiares y un siguiente paso claro, todo movi\u00e9ndose junto para que el mensaje sea parte de la vida diaria.",
 "Uma campanha \u00e9 uma experi\u00eancia de discipulado coordenada em torno de um tema por uma temporada definida: ensino de fim de semana, devocional di\u00e1rio, curr\u00edculo de grupos, edi\u00e7\u00f5es para a fam\u00edlia e um pr\u00f3ximo passo claro, tudo se movendo junto para a mensagem virar parte da vida di\u00e1ria.")
# campaign page
both("The journey at a glance","El recorrido de un vistazo","A jornada em resumo")
both("What tends to happen","Lo que suele suceder","O que costuma acontecer")
both("The heart of this journey","El coraz\u00f3n de este recorrido","O cora\u00e7\u00e3o desta jornada")
both("What your church receives","Lo que recibe tu iglesia","O que sua igreja recebe")
both("Inside this campaign","Dentro de esta campa\u00f1a","Dentro desta campanha")
both("Scripture on more lips — a weekly memory verse the whole church says together",
 "La Escritura en m\u00e1s labios: un vers\u00edculo semanal que toda la iglesia dice junta",
 "A Escritura em mais l\u00e1bios: um vers\u00edculo semanal que a igreja toda diz junta")
both("A pulpit with momentum — six aligned Sundays that build instead of restart",
 "Un p\u00falpito con impulso: seis domingos alineados que construyen en vez de reiniciar",
 "Um p\u00falpito com impulso: seis domingos alinhados que constroem em vez de recome\u00e7ar")
both("New hosts discovered — churches typically launch one group per eight to ten adults",
 "Nuevos anfitriones descubiertos: las iglesias suelen lanzar un grupo por cada ocho a diez adultos",
 "Novos anfitri\u00f5es descobertos: as igrejas costumam lan\u00e7ar um grupo a cada oito a dez adultos")
both("The journey moves at a walking pace — one short reading a day, one honest hour a week, one message that ties the week together. No seminary required, no performance expected: just a congregation reading the same words and letting them work.",
 "El recorrido avanza a paso de caminata: una lectura corta al d\u00eda, una hora honesta a la semana, un mensaje que ata la semana. Sin seminario requerido, sin actuaci\u00f3n esperada: solo una congregaci\u00f3n leyendo las mismas palabras y dej\u00e1ndolas obrar.",
 "A jornada anda em passo de caminhada: uma leitura curta por dia, uma hora honesta por semana, uma mensagem que amarra a semana. Sem semin\u00e1rio exigido, sem performance esperada: s\u00f3 uma congrega\u00e7\u00e3o lendo as mesmas palavras e deixando que trabalhem.")
both("Sixteen formats from one campaign — possibilities that turn a sermon archive into a scalable ministry platform.",
 "Diecis\u00e9is formatos de una campa\u00f1a: posibilidades que convierten un archivo de sermones en una plataforma de ministerio escalable.",
 "Dezesseis formatos de uma campanha: possibilidades que transformam um arquivo de serm\u00f5es em uma plataforma de minist\u00e9rio escal\u00e1vel.")
both("Every campaign ships in sixteen formats — from a trade-paperback book to a podcast series to a membership course. Preview any of them below; one license covers them all.",
 "Cada campa\u00f1a llega en diecis\u00e9is formatos: de un libro de bolsillo a una serie de p\u00f3dcast a un curso de membres\u00eda. Previsualiza cualquiera abajo; una licencia los cubre todos.",
 "Cada campanha chega em dezesseis formatos: de um livro de bolso a uma s\u00e9rie de podcast a um curso de membresia. Veja qualquer um abaixo; uma licen\u00e7a cobre todos.")
both("The complete daily readings in the campaign\u2019s native length",
 "Las lecturas diarias completas en la duraci\u00f3n nativa de la campa\u00f1a",
 "As leituras di\u00e1rias completas na dura\u00e7\u00e3o nativa da campanha")
both("\u2248 17k words of daily devotional","\u2248 17 mil palabras de devocional diario","\u2248 17 mil palavras de devocional di\u00e1rio")
both("a finished final message, stories to gather","un mensaje final terminado, historias por recoger","uma mensagem final pronta, hist\u00f3rias a colher")
both("shareable art + the offline","arte para compartir + la","arte para compartilhar + a")
# launch strings (unmapped ones)
both("Set the budget and order/print plan","Define el presupuesto y el plan de pedido e impresi\u00f3n","Defina o or\u00e7amento e o plano de pedido e impress\u00e3o")
both("Announce from the pulpit: \u201copen your home for six weeks\u201d","Anuncia desde el p\u00falpito: \u201cabre tu casa por seis semanas\u201d","Anuncie do p\u00falpito: \u201cabra sua casa por seis semanas\u201d")
both("Personally invite 20% more hosts than you need","Invita personalmente 20% m\u00e1s anfitriones de los que necesitas","Convide pessoalmente 20% mais anfitri\u00f5es do que precisa")
both("One-hour host orientation (the kit runs it)","Orientaci\u00f3n de anfitriones de una hora (el kit la ejecuta)","Orienta\u00e7\u00e3o de anfitri\u00f5es de uma hora (o kit conduz)")
both("Preach the \u201cnobody does this alone\u201d invitation","Predica la invitaci\u00f3n de \u201cnadie hace esto solo\u201d","Pregue o convite de \u201cningu\u00e9m faz isso sozinho\u201d")
both("Walk hosts through Session 1 (30 minutes)","Repasa la Sesi\u00f3n 1 con los anfitriones (30 minutos)","Repasse a Sess\u00e3o 1 com os anfitri\u00f5es (30 minutos)")
both("Load Sermon 1 into the plan of service","Carga el Serm\u00f3n 1 en el orden del culto","Carregue o Serm\u00e3o 1 na liturgia")
both("Send the church-wide \u201cwe begin Sunday\u201d message","Env\u00eda el mensaje de \u201cempezamos el domingo\u201d a toda la iglesia","Envie a mensagem de \u201ccome\u00e7amos domingo\u201d para toda a igreja")
both("Open this week\u2019s materials \u2192","Abrir los materiales de esta semana \u2192","Abrir os materiais desta semana \u2192")
both("Point to the next season: finder.html has three matches ready","Se\u00f1ala la pr\u00f3xima temporada: el Buscador tiene tres coincidencias listas","Aponte a pr\u00f3xima temporada: o Localizador tem tr\u00eas combina\u00e7\u00f5es prontas")
both("Choose your kickoff Sunday and the planner builds your church's complete runway — six weeks of preparation, six weeks of campaign, and Celebration Sunday, with every task on a real date.",
 "Elige tu domingo de inicio y el planificador construye la pista completa de tu iglesia: seis semanas de preparaci\u00f3n, seis de campa\u00f1a y el Domingo de Celebraci\u00f3n, con cada tarea en una fecha real.",
 "Escolha seu domingo de abertura e o planejador monta a pista completa da sua igreja: seis semanas de prepara\u00e7\u00e3o, seis de campanha e o Domingo de Celebra\u00e7\u00e3o, com cada tarefa numa data real.")
# groups page paras
both("Every campaign in the library carries a six-session study built for the newest host in the room — and every one of them is available on its own. No sermons required, no churchwide launch: just living rooms, questions, and $99.",
 "Cada campa\u00f1a de la biblioteca lleva un estudio de seis sesiones hecho para el anfitri\u00f3n m\u00e1s nuevo de la sala, y cada uno est\u00e1 disponible por separado. Sin sermones requeridos, sin lanzamiento de toda la iglesia: solo salas de casa, preguntas y $99.",
 "Cada campanha da biblioteca traz um estudo de seis sess\u00f5es feito para o anfitri\u00e3o mais novo da sala, e cada um est\u00e1 dispon\u00edvel avulso. Sem serm\u00f5es exigidos, sem lan\u00e7amento de toda a igreja: s\u00f3 salas de estar, perguntas e $99.")
both("No. The Small-Group Edition stands entirely on its own — sessions, leader notes, and print rights. If your church later runs it churchwide, the study you already own is the same one inside the full license.",
 "No. La edici\u00f3n para grupos se sostiene completamente sola: sesiones, notas de l\u00edder y derechos de impresi\u00f3n. Si tu iglesia luego la ejecuta completa, el estudio que ya tienes es el mismo de la licencia total.",
 "N\u00e3o. A edi\u00e7\u00e3o para grupos se sustenta totalmente sozinha: sess\u00f5es, notas de l\u00edder e direitos de impress\u00e3o. Se sua igreja depois rodar por completo, o estudo que voc\u00ea j\u00e1 tem \u00e9 o mesmo da licen\u00e7a completa.")
both("Seventy to ninety minutes at a natural pace: ten of welcome, four movements of Scripture and discussion, one practice, and prayer. Groups that run long run long on the conversation — which is the point.",
 "De setenta a noventa minutos a paso natural: diez de bienvenida, cuatro movimientos de Escritura y conversaci\u00f3n, una pr\u00e1ctica y oraci\u00f3n. Los grupos que se alargan, se alargan en la conversaci\u00f3n, que es el punto.",
 "De setenta a noventa minutos em ritmo natural: dez de boas-vindas, quatro movimentos de Escritura e conversa, uma pr\u00e1tica e ora\u00e7\u00e3o. Os grupos que passam do tempo, passam na conversa, que \u00e9 o ponto.")
both("Early on, people mostly answer the host's questions rather than talking to each other. By week two or three, that usually starts to loosen up — people start responding to one another instead of just the host, and the group starts feeling less like an obligation.",
 "Al principio, la gente responde m\u00e1s al anfitri\u00f3n que entre s\u00ed. Para la semana dos o tres, eso suele soltarse: las personas empiezan a responderse unas a otras y el grupo deja de sentirse como una obligaci\u00f3n.",
 "No come\u00e7o, as pessoas respondem mais ao anfitri\u00e3o do que umas \u00e0s outras. L\u00e1 pela semana dois ou tr\u00eas, isso costuma soltar: as pessoas come\u00e7am a responder umas \u00e0s outras e o grupo deixa de parecer obriga\u00e7\u00e3o.")
both("By the midpoint, groups are often willing to get more specific and honest with each other. It's common for the weekly practice to actually get done and talked about, without anyone having to bring it up first.",
 "Hacia la mitad, los grupos suelen estar dispuestos a ser m\u00e1s espec\u00edficos y honestos. Es com\u00fan que la pr\u00e1ctica semanal de verdad se haga y se converse, sin que nadie tenga que sacarla primero.",
 "No meio do caminho, os grupos costumam estar dispostos a ser mais espec\u00edficos e honestos. \u00c9 comum a pr\u00e1tica semanal ser feita e conversada de verdade, sem ningu\u00e9m precisar puxar o assunto.")
both("\u2026three more movements, a weekly practice, and prayer complete the session.",
 "\u2026tres movimientos m\u00e1s, una pr\u00e1ctica semanal y la oraci\u00f3n completan la sesi\u00f3n.",
 "\u2026mais tr\u00eas movimentos, uma pr\u00e1tica semanal e a ora\u00e7\u00e3o completam a sess\u00e3o.")
# account signed-out + empty states
both("Your journey, launches, and library — right where you left them.","Tu recorrido, tus lanzamientos y tu biblioteca, justo donde los dejaste.","Sua jornada, seus lan\u00e7amentos e sua biblioteca, exatamente onde voc\u00ea deixou.")
both("Sign in \u2192","Iniciar sesi\u00f3n \u2192","Entrar \u2192")
both("New here? Create your account","\u00bfNuevo aqu\u00ed? Crea tu cuenta","Novo por aqui? Crie sua conta")
both("\u2190 Back to 40daycampaigns.com","\u2190 Volver a 40daycampaigns.com","\u2190 Voltar para 40daycampaigns.com")
both("Nothing in progress yet — open any campaign and tap","A\u00fan nada en progreso: abre cualquier campa\u00f1a y toca","Nada em andamento ainda: abra qualquer campanha e toque")
both("No campaign licenses yet.","A\u00fan no hay licencias de campa\u00f1a.","Nenhuma licen\u00e7a de campanha ainda.")
# churches paras
both("You preach your heart out. People nod, some take notes, a few tell you it was exactly what they needed. And by Tuesday the week has swallowed it — not because they didn't mean it, but because nothing carried the message past the parking lot.",
 "Predicas con todo el coraz\u00f3n. La gente asiente, algunos toman notas, unos pocos te dicen que era justo lo que necesitaban. Y para el martes la semana se lo trag\u00f3, no porque no fueran sinceros, sino porque nada llev\u00f3 el mensaje m\u00e1s all\u00e1 del estacionamiento.",
 "Voc\u00ea prega com o cora\u00e7\u00e3o inteiro. As pessoas assentem, algumas anotam, umas poucas dizem que era exatamente o que precisavam. E na ter\u00e7a a semana engoliu tudo, n\u00e3o porque n\u00e3o fossem sinceras, mas porque nada levou a mensagem para al\u00e9m do estacionamento.")
both("The fix isn't a better sermon. It's a structure that lets one message travel: into living rooms on Wednesday, into a reading on Thursday morning, into a question a child asks at Friday's dinner table. That structure is a campaign — and building one from scratch takes a staff you don't have and a month you can't spare.",
 "La soluci\u00f3n no es un mejor serm\u00f3n. Es una estructura que deja viajar un mensaje: a las salas de casa el mi\u00e9rcoles, a una lectura el jueves por la ma\u00f1ana, a una pregunta que un ni\u00f1o hace en la cena del viernes. Esa estructura es una campa\u00f1a, y construirla desde cero requiere un equipo que no tienes y un mes que no te sobra.",
 "A solu\u00e7\u00e3o n\u00e3o \u00e9 um serm\u00e3o melhor. \u00c9 uma estrutura que deixa uma mensagem viajar: para as salas de estar na quarta, para uma leitura na quinta de manh\u00e3, para uma pergunta que uma crian\u00e7a faz no jantar de sexta. Essa estrutura \u00e9 uma campanha, e constru\u00ed-la do zero exige uma equipe que voc\u00ea n\u00e3o tem e um m\u00eas que n\u00e3o sobra.")
# business paras
both("Complete team campaigns for the workplace: short daily reads, one weekly team conversation, and a practical challenge that shows up in how people lead, serve, and treat each other. Built for real companies, mixed-faith teams, and calendars that don't have room for one more program that fizzles.",
 "Campa\u00f1as de equipo completas para el trabajo: lecturas diarias cortas, una conversaci\u00f3n semanal y un reto pr\u00e1ctico que se nota en c\u00f3mo la gente lidera, sirve y se trata. Hechas para empresas reales, equipos de fe mixta y calendarios sin espacio para un programa m\u00e1s que se apaga.",
 "Campanhas de equipe completas para o trabalho: leituras di\u00e1rias curtas, uma conversa semanal e um desafio pr\u00e1tico que aparece em como as pessoas lideram, servem e se tratam. Feitas para empresas reais, equipes de f\u00e9 mista e calend\u00e1rios sem espa\u00e7o para mais um programa que morre.")
both("A first shelf from our workplace catalog — the dedicated Purpose Built Business library is being added now, campaign by campaign.",
 "Un primer estante de nuestro cat\u00e1logo laboral: la biblioteca dedicada de Purpose Built Business se est\u00e1 a\u00f1adiendo ahora, campa\u00f1a por campa\u00f1a.",
 "Uma primeira estante do nosso cat\u00e1logo corporativo: a biblioteca dedicada Purpose Built Business est\u00e1 sendo adicionada agora, campanha por campanha.")
both("Purpose Built Business grows out of Lifetogether's twenty-five years of purpose-driven campaigns. The workplace editions lead with character, trust, and meaning in language any team can use, and the underlying conviction is no secret: work matters because people matter, and people matter because they were made on purpose. Teams that want to go deeper into the faith roots can; teams that don't, won't be cornered.",
 "Purpose Built Business nace de los veinticinco a\u00f1os de campa\u00f1as con prop\u00f3sito de Lifetogether. Las ediciones laborales lideran con car\u00e1cter, confianza y sentido en un lenguaje que cualquier equipo puede usar, y la convicci\u00f3n de fondo no es secreta: el trabajo importa porque las personas importan, y las personas importan porque fueron hechas con prop\u00f3sito. Los equipos que quieran profundizar en las ra\u00edces de fe pueden; los que no, no ser\u00e1n acorralados.",
 "A Purpose Built Business nasce dos vinte e cinco anos de campanhas com prop\u00f3sito da Lifetogether. As edi\u00e7\u00f5es corporativas lideram com car\u00e1ter, confian\u00e7a e sentido numa linguagem que qualquer equipe pode usar, e a convic\u00e7\u00e3o de fundo n\u00e3o \u00e9 segredo: o trabalho importa porque as pessoas importam, e as pessoas importam porque foram feitas com prop\u00f3sito. Equipes que quiserem aprofundar nas ra\u00edzes da f\u00e9 podem; as que n\u00e3o quiserem, n\u00e3o ser\u00e3o encurraladas.")
# about paras
both("Before Lifetogether was a company, it was a question inside the small-groups movement at Saddleback Church: what happens when a congregation doesn't just attend a message, but walks it — together, daily, in homes? The campaign era answered loudly. When churches aligned the pulpit, the group, and the daily reading around one journey, something happened that sermons alone never produced: whole congregations changed direction at once.",
 "Antes de ser una empresa, Lifetogether fue una pregunta dentro del movimiento de grupos peque\u00f1os de la iglesia de Saddleback: \u00bfqu\u00e9 pasa cuando una congregaci\u00f3n no solo asiste a un mensaje, sino que lo camina, junta, a diario, en los hogares? La era de las campa\u00f1as respondi\u00f3 con fuerza. Cuando las iglesias alinearon el p\u00falpito, el grupo y la lectura diaria alrededor de un recorrido, pas\u00f3 algo que los sermones solos nunca produjeron: congregaciones enteras cambiaron de direcci\u00f3n a la vez.",
 "Antes de ser uma empresa, a Lifetogether foi uma pergunta dentro do movimento de pequenos grupos da igreja de Saddleback: o que acontece quando uma congrega\u00e7\u00e3o n\u00e3o s\u00f3 assiste a uma mensagem, mas caminha nela, junta, diariamente, nos lares? A era das campanhas respondeu alto. Quando as igrejas alinharam o p\u00falpito, o grupo e a leitura di\u00e1ria em torno de uma jornada, aconteceu algo que serm\u00f5es sozinhos nunca produziram: congrega\u00e7\u00f5es inteiras mudaram de dire\u00e7\u00e3o de uma vez.")
both("Brett Eastman founded Lifetogether in 2001 to put that discovery within reach of every church — not just the ones with writing teams. Through the Purpose Driven years and the decades since, the pattern held across more than five hundred churches: alignment beats intensity. Forty shared days outwork forty scattered sermons.",
 "Brett Eastman fund\u00f3 Lifetogether en 2001 para poner ese descubrimiento al alcance de cada iglesia, no solo de las que tienen equipos de redacci\u00f3n. A trav\u00e9s de los a\u00f1os de Una Vida con Prop\u00f3sito y las d\u00e9cadas siguientes, el patr\u00f3n se sostuvo en m\u00e1s de quinientas iglesias: la alineaci\u00f3n vence a la intensidad. Cuarenta d\u00edas compartidos rinden m\u00e1s que cuarenta sermones dispersos.",
 "Brett Eastman fundou a Lifetogether em 2001 para colocar essa descoberta ao alcance de cada igreja, n\u00e3o s\u00f3 das que t\u00eam equipes de reda\u00e7\u00e3o. Pelos anos de Uma Vida com Prop\u00f3sitos e as d\u00e9cadas seguintes, o padr\u00e3o se manteve em mais de quinhentas igrejas: alinhamento vence intensidade. Quarenta dias compartilhados rendem mais que quarenta serm\u00f5es dispersos.")
both("The library is the latest chapter of that same conviction. Churches face hundreds of seasons — grief and generosity, marriages and money, planting and finishing well — and every one of them used to require a custom build. So we built them all: five hundred thirty-three complete campaigns, hand-curated, each with its own angle and backbone, all finished before you arrive.",
 "La biblioteca es el cap\u00edtulo m\u00e1s reciente de esa misma convicci\u00f3n. Las iglesias enfrentan cientos de temporadas \u2014 duelo y generosidad, matrimonios y dinero, plantar y terminar bien \u2014 y cada una sol\u00eda requerir una construcci\u00f3n a medida. As\u00ed que las construimos todas: 1.252 campa\u00f1as completas, cada una con su propio \u00e1ngulo y columna, todas terminadas antes de que llegues.",
 "A biblioteca \u00e9 o cap\u00edtulo mais recente dessa mesma convic\u00e7\u00e3o. As igrejas enfrentam centenas de temporadas \u2014 luto e generosidade, casamentos e dinheiro, plantar e terminar bem \u2014 e cada uma exigia uma constru\u00e7\u00e3o sob medida. Ent\u00e3o constru\u00edmos todas: 1.252 campanhas completas, cada uma com seu \u00e2ngulo e sua espinha, todas prontas antes de voc\u00ea chegar.")
both("After years of producing church video content, we've found that a well-shot phone video often works better than an over-produced one. We can train your team to shoot it themselves, then handle editing and finishing so it looks polished. Four formats we typically recommend:",
 "Tras a\u00f1os produciendo video para iglesias, hemos visto que un video de tel\u00e9fono bien grabado suele funcionar mejor que uno sobreproducido. Podemos entrenar a tu equipo para grabarlo, y luego encargarnos de la edici\u00f3n y el acabado para que quede pulido. Cuatro formatos que solemos recomendar:",
 "Depois de anos produzindo v\u00eddeo para igrejas, vimos que um v\u00eddeo de celular bem gravado costuma funcionar melhor que um superproduzido. Podemos treinar sua equipe para gravar, e depois cuidar da edi\u00e7\u00e3o e do acabamento para ficar polido. Quatro formatos que costumamos recomendar:")
# hiw para
both("A campaign is not a sermon series with homework. It is a whole church reading the same words, praying the same prayers, and carrying one question into every room of the week — until Sunday stops ending on Sunday. Here is exactly how it runs.",
 "Una campa\u00f1a no es una serie de sermones con tarea. Es una iglesia entera leyendo las mismas palabras, orando las mismas oraciones y llevando una pregunta a cada sala de la semana, hasta que el domingo deja de terminar el domingo. As\u00ed es exactamente c\u00f3mo funciona.",
 "Uma campanha n\u00e3o \u00e9 uma s\u00e9rie de serm\u00f5es com dever de casa. \u00c9 uma igreja inteira lendo as mesmas palavras, orando as mesmas ora\u00e7\u00f5es e levando uma pergunta a cada sala da semana, at\u00e9 o domingo parar de terminar no domingo. \u00c9 exatamente assim que funciona.")
# finder
both("Our ministry\u2019s donors","Los donantes de nuestro ministerio","Os doadores do nosso minist\u00e9rio")
both("QUESTION","PREGUNTA","PERGUNTA")
both(" OF 7"," DE 7"," DE 7")
both(" OF "," DE "," DE ")
both("CAMPAIGNS'","CAMPA\u00d1AS'","CAMPANHAS'")
# reader/sample/curriculum labels
both("THIS WEEK'S MEMORY VERSE","VERS\u00cdCULO DE MEMORIA DE ESTA SEMANA","VERS\u00cdCULO DESTA SEMANA")
both("THIS WEEK\u2019S MEMORY VERSE","VERS\u00cdCULO DE MEMORIA DE ESTA SEMANA","VERS\u00cdCULO DESTA SEMANA")
both("Day ${","D\u00eda ${","Dia ${")
both("of ${C[5]}","de ${C[5]}","de ${C[5]}")
both("Days 1\u20133 of the daily devotional \u00b7 Session 1 of the small-group study \u00b7 Anchored in",
 "D\u00edas 1\u20133 del devocional diario \u00b7 Sesi\u00f3n 1 del estudio de grupos \u00b7 Anclado en",
 "Dias 1\u20133 do devocional di\u00e1rio \u00b7 Sess\u00e3o 1 do estudo de grupos \u00b7 Ancorado em")
# attributes
for en,es,pt in [
 ("Accepted payment methods","M\u00e9todos de pago aceptados","Formas de pagamento aceitas"),
 ("Average weekend attendance","Asistencia promedio de fin de semana","Frequ\u00eancia m\u00e9dia de fim de semana"),
 ("Back to campaign","Volver a la campa\u00f1a","Voltar \u00e0 campanha"),
 ("Candlelight (t)","Luz de vela (t)","Luz de vela (t)"),
 ("Change who this is for","Cambiar para qui\u00e9n es","Mudar para quem \u00e9"),
 ("Choose a week","Elige una semana","Escolha uma semana"),
 ("Church name","Nombre de la iglesia","Nome da igreja"),
 ("Close","Cerrar","Fechar"),
 ("Day navigation","Navegaci\u00f3n de d\u00edas","Navega\u00e7\u00e3o de dias"),
 ("Download this week's verse card","Descargar la tarjeta del vers\u00edculo de esta semana","Baixar o cart\u00e3o do vers\u00edculo desta semana"),
 ("Exactly as printed","Exactamente como aparece impreso","Exatamente como impresso"),
 ("Filter by audience","Filtrar por audiencia","Filtrar por p\u00fablico"),
 ("Filter by channel","Filtrar por canal","Filtrar por canal"),
 ("Filter by life event","Filtrar por momento de vida","Filtrar por momento de vida"),
 ("Filter by theme","Filtrar por tema","Filtrar por tema"),
 ("First and last name","Nombre y apellido","Nome e sobrenome"),
 ("First and last","Nombre y apellido","Nome e sobrenome"),
 ("Jump to a category","Saltar a una categor\u00eda","Ir para uma categoria"),
 ("Jump to a topic","Saltar a un tema","Ir para um t\u00f3pico"),
 ("Larger text","Texto m\u00e1s grande","Texto maior"),
 ("Launch summary","Resumen del lanzamiento","Resumo do lan\u00e7amento"),
 ("Listen to today's reading","Escuchar la lectura de hoy","Ouvir a leitura de hoje"),
 ("Listen","Escuchar","Ouvir"),
 ("Monthly tiers by weekend attendance","Niveles mensuales por asistencia de fin de semana","N\u00edveis mensais pela frequ\u00eancia de fim de semana"),
 ("Next day","D\u00eda siguiente","Pr\u00f3ximo dia"),
 ("Optional","Opcional","Opcional"),
 ("Pay with Apple Pay","Pagar con Apple Pay","Pagar com Apple Pay"),
 ("Pay with PayPal","Pagar con PayPal","Pagar com PayPal"),
 ("Previous day","D\u00eda anterior","Dia anterior"),
 ("Previous","Anterior","Anterior"),
 ("Progress","Progreso","Progresso"),
 ("Quick search","B\u00fasqueda r\u00e1pida","Busca r\u00e1pida"),
 ("Scroll left","Desplazar a la izquierda","Rolar para a esquerda"),
 ("Scroll right","Desplazar a la derecha","Rolar para a direita"),
 ("Search 1252 campaigns","Buscar entre 1252 campa\u00f1as","Buscar em 1252 campanhas"),
 ("Search campaigns, pages, actions\u2026","Buscar campa\u00f1as, p\u00e1ginas, acciones\u2026","Buscar campanhas, p\u00e1ginas, a\u00e7\u00f5es\u2026"),
 ("Search campaigns\u2026","Buscar campa\u00f1as\u2026","Buscar campanhas\u2026"),
 ("Search the site","Buscar en el sitio","Buscar no site"),
 ("Smaller text","Texto m\u00e1s peque\u00f1o","Texto menor"),
 ("Social channels launch soon \u2014 say hello","Las redes sociales llegan pronto: escr\u00edbenos","As redes sociais chegam em breve: fale conosco"),
 ("Toggle candlelight mode","Alternar modo de luz de vela","Alternar modo luz de vela"),
 ("Two sentences is plenty.","Con dos oraciones basta.","Duas frases bastam."),
 ("Verse card","Tarjeta de vers\u00edculo","Cart\u00e3o de vers\u00edculo"),
 ("ZIP / postal","C\u00f3digo postal","CEP"),
 ("e.g. First Baptist Alexandria","p. ej. Primera Bautista Alejandr\u00eda","ex.: Primeira Batista Alexandria"),
 ("e.g. PLANT40","p. ej. PLANT40","ex.: PLANT40"),
 ("you@church.org","tu@iglesia.org","voce@igreja.org"),
 ("you@example.com","tu@ejemplo.com","voce@exemplo.com"),
]: both(en,es,pt)

json.dump(M["es"], open("/home/claude/tr_es_5.json","w"), ensure_ascii=False)
json.dump(M["pt"], open("/home/claude/tr_pt_5.json","w"), ensure_ascii=False)
print("chrome close-out maps:", len(M["es"]), "pairs each")

# ---- DEEP flagship data translation (applied to localized data.js AFTER catalog run) ----
DEEP_TR = {"es":{
 "The Ownership Question":"La pregunta de la pertenencia","The Stewardship Question":"La pregunta de la mayordom\u00eda",
 "The Confidence Question":"La pregunta de la confianza","The Contentment Question":"La pregunta del contentamiento",
 "The Generosity Question":"La pregunta de la generosidad","The Legacy Question":"La pregunta del legado",
 "Days 1\u20137":"D\u00edas 1\u20137","Days 8\u201314":"D\u00edas 8\u201314","Days 15\u201321":"D\u00edas 15\u201321","Days 22\u201328":"D\u00edas 22\u201328","Days 29\u201335":"D\u00edas 29\u201335","Days 36\u201340":"D\u00edas 36\u201340","Days 29\u201334":"D\u00edas 29\u201334","Days 35\u201340":"D\u00edas 35\u201340",
 "Who Really Owns What I Have?":"\u00bfQui\u00e9n es realmente due\u00f1o de lo que tengo?",
 "When ownership changes hands, everything changes.":"Cuando la propiedad cambia de manos, todo cambia.",
 "The Transfer":"La transferencia",
 "When Does Stewardship Become Contentment?":"\u00bfCu\u00e1ndo la mayordom\u00eda se vuelve contentamiento?",
 "Stewardship is worship in motion.":"La mayordom\u00eda es adoraci\u00f3n en movimiento.",
 "The Enough Budget":"El presupuesto del suficiente",
 "Will I Be Okay?":"\u00bfVoy a estar bien?",
 "Peace replaces fear when you trust the Provider, not the provision.":"La paz reemplaza al miedo cuando conf\u00edas en el Proveedor, no en la provisi\u00f3n.",
 "The Margin Plan":"El plan de margen",
 "How Much Is Enough?":"\u00bfCu\u00e1nto es suficiente?",
 "Enough is learned, not earned.":"El suficiente se aprende, no se gana.",
 "Finish Lines":"L\u00edneas de meta",
 "Why Does Giving Change Everything?":"\u00bfPor qu\u00e9 dar lo cambia todo?",
 "You're never more like God than when you give.":"Nunca te pareces m\u00e1s a Dios que cuando das.",
 "First-and-Best Giving Plan":"El plan de dar primero y lo mejor",
 "What Will I Leave Behind?":"\u00bfQu\u00e9 dejar\u00e9 atr\u00e1s?",
 "Legacy is about what outlives you.":"El legado se trata de lo que te sobrevive.",
 "The Legacy Letter":"La carta de legado",
 "Ownership":"Pertenencia","Stewardship":"Mayordom\u00eda","Confidence":"Confianza","Contentment":"Contentamiento","Generosity":"Generosidad","Legacy":"Legado",
 "Ownership Changes the Pressure":"La pertenencia cambia la presi\u00f3n",
 "When ownership changes hands, the weight shifts too":"Cuando la propiedad cambia de manos, el peso tambi\u00e9n se mueve",
 "The complete day-by-day 40-day devotional manuscript ships with this campaign.":"El manuscrito devocional completo de 40 d\u00edas, d\u00eda por d\u00eda, llega con esta campa\u00f1a.",
 "Who Really Owns Our Family's Resources?":"\u00bfQui\u00e9n es realmente due\u00f1o de los recursos de nuestra familia?",
 "Everything changes when a family agrees that God owns it all.":"Todo cambia cuando una familia acuerda que Dios es due\u00f1o de todo.",
 "The God Owns It All Family Inventory":"El inventario familiar de Dios es due\u00f1o de todo",
 "What Is Our Family Here to Build?":"\u00bfQu\u00e9 vino a construir nuestra familia?",
 "The Family Mission Statement":"La declaraci\u00f3n de misi\u00f3n familiar",
 "How Do We Make Decisions Together?":"\u00bfC\u00f3mo tomamos decisiones juntos?",
 "Shared values produce wise financial decisions.":"Los valores compartidos producen decisiones financieras sabias.",
 "Five Family Stewardship Principles":"Cinco principios de mayordom\u00eda familiar",
 "How Do We Raise Faithful Stewards?":"\u00bfC\u00f3mo criamos mayordomos fieles?",
 "Children learn stewardship by participating.":"Los hijos aprenden mayordom\u00eda participando.",
 "Age-Appropriate Stewardship Plan":"Plan de mayordom\u00eda por edades",
 "What Does Generosity Look Like for Our Family?":"\u00bfC\u00f3mo se ve la generosidad en nuestra familia?",
 "Generosity becomes a family culture before it becomes a financial decision.":"La generosidad se vuelve cultura familiar antes que decisi\u00f3n financiera.",
 "The Family Giving Plan":"El plan familiar de dar",
 "What Legacy Will We Leave?":"\u00bfQu\u00e9 legado dejaremos?",
 "The greatest inheritance is a life of faithful stewardship.":"La mayor herencia es una vida de mayordom\u00eda fiel.",
 "The Family Legacy Letter":"La carta de legado familiar",
 "The Awakening of Generosity":"El despertar de la generosidad",
 "What Happens When God Opens Your Heart":"Lo que pasa cuando Dios abre tu coraz\u00f3n",
 "The Ownership Shift":"El cambio de due\u00f1o",
 "Why Open Hands Begin with God Owns It All":"Por qu\u00e9 las manos abiertas empiezan con Dios es due\u00f1o de todo",
 "The Enough Question":"La pregunta del suficiente",
 "Finding Freedom from the Endless Pursuit of More":"Encontrando libertad de la b\u00fasqueda interminable de m\u00e1s",
 "The Practice of Generosity":"La pr\u00e1ctica de la generosidad",
 "Turning Good Intentions into Open-Handed Habits":"Convirtiendo buenas intenciones en h\u00e1bitos de manos abiertas",
 "The Generous Family":"La familia generosa",
 "Passing Down Joy, Gratitude, and Stewardship":"Transmitiendo gozo, gratitud y mayordom\u00eda",
 "The Legacy of Generosity":"El legado de la generosidad",
 "Living and Giving for What Outlives You":"Viviendo y dando por lo que te sobrevive",
},"pt":{
 "The Ownership Question":"A pergunta do dono","The Stewardship Question":"A pergunta da mordomia",
 "The Confidence Question":"A pergunta da confian\u00e7a","The Contentment Question":"A pergunta do contentamento",
 "The Generosity Question":"A pergunta da generosidade","The Legacy Question":"A pergunta do legado",
 "Days 1\u20137":"Dias 1\u20137","Days 8\u201314":"Dias 8\u201314","Days 15\u201321":"Dias 15\u201321","Days 22\u201328":"Dias 22\u201328","Days 29\u201335":"Dias 29\u201335","Days 36\u201340":"Dias 36\u201340","Days 29\u201334":"Dias 29\u201334","Days 35\u201340":"Dias 35\u201340",
 "Who Really Owns What I Have?":"Quem \u00e9 realmente dono do que eu tenho?",
 "When ownership changes hands, everything changes.":"Quando a propriedade muda de m\u00e3os, tudo muda.",
 "The Transfer":"A transfer\u00eancia",
 "When Does Stewardship Become Contentment?":"Quando a mordomia vira contentamento?",
 "Stewardship is worship in motion.":"Mordomia \u00e9 adora\u00e7\u00e3o em movimento.",
 "The Enough Budget":"O or\u00e7amento do suficiente",
 "Will I Be Okay?":"Eu vou ficar bem?",
 "Peace replaces fear when you trust the Provider, not the provision.":"A paz substitui o medo quando voc\u00ea confia no Provedor, n\u00e3o na provis\u00e3o.",
 "The Margin Plan":"O plano de margem",
 "How Much Is Enough?":"Quanto \u00e9 suficiente?",
 "Enough is learned, not earned.":"O suficiente se aprende, n\u00e3o se ganha.",
 "Finish Lines":"Linhas de chegada",
 "Why Does Giving Change Everything?":"Por que doar muda tudo?",
 "You're never more like God than when you give.":"Voc\u00ea nunca se parece tanto com Deus quanto ao doar.",
 "First-and-Best Giving Plan":"O plano de dar primeiro e o melhor",
 "What Will I Leave Behind?":"O que vou deixar para tr\u00e1s?",
 "Legacy is about what outlives you.":"Legado \u00e9 o que sobrevive a voc\u00ea.",
 "The Legacy Letter":"A carta de legado",
 "Ownership":"Propriedade","Stewardship":"Mordomia","Confidence":"Confian\u00e7a","Contentment":"Contentamento","Generosity":"Generosidade","Legacy":"Legado",
 "Ownership Changes the Pressure":"Saber quem \u00e9 o dono muda a press\u00e3o",
 "When ownership changes hands, the weight shifts too":"Quando a propriedade muda de m\u00e3os, o peso tamb\u00e9m muda",
 "The complete day-by-day 40-day devotional manuscript ships with this campaign.":"O manuscrito devocional completo de 40 dias, dia a dia, acompanha esta campanha.",
 "Who Really Owns Our Family's Resources?":"Quem \u00e9 realmente dono dos recursos da nossa fam\u00edlia?",
 "Everything changes when a family agrees that God owns it all.":"Tudo muda quando uma fam\u00edlia concorda que Deus \u00e9 dono de tudo.",
 "The God Owns It All Family Inventory":"O invent\u00e1rio familiar do Deus \u00e9 dono de tudo",
 "What Is Our Family Here to Build?":"O que a nossa fam\u00edlia veio construir?",
 "The Family Mission Statement":"A declara\u00e7\u00e3o de miss\u00e3o da fam\u00edlia",
 "How Do We Make Decisions Together?":"Como tomamos decis\u00f5es juntos?",
 "Shared values produce wise financial decisions.":"Valores compartilhados produzem decis\u00f5es financeiras s\u00e1bias.",
 "Five Family Stewardship Principles":"Cinco princ\u00edpios de mordomia familiar",
 "How Do We Raise Faithful Stewards?":"Como criamos mordomos fi\u00e9is?",
 "Children learn stewardship by participating.":"Os filhos aprendem mordomia participando.",
 "Age-Appropriate Stewardship Plan":"Plano de mordomia por idades",
 "What Does Generosity Look Like for Our Family?":"Como \u00e9 a generosidade na nossa fam\u00edlia?",
 "Generosity becomes a family culture before it becomes a financial decision.":"A generosidade vira cultura familiar antes de virar decis\u00e3o financeira.",
 "The Family Giving Plan":"O plano familiar de doar",
 "What Legacy Will We Leave?":"Que legado vamos deixar?",
 "The greatest inheritance is a life of faithful stewardship.":"A maior heran\u00e7a \u00e9 uma vida de mordomia fiel.",
 "The Family Legacy Letter":"A carta de legado da fam\u00edlia",
 "The Awakening of Generosity":"O despertar da generosidade",
 "What Happens When God Opens Your Heart":"O que acontece quando Deus abre o seu cora\u00e7\u00e3o",
 "The Ownership Shift":"A mudan\u00e7a de dono",
 "Why Open Hands Begin with God Owns It All":"Por que m\u00e3os abertas come\u00e7am com Deus \u00e9 dono de tudo",
 "The Enough Question":"A pergunta do suficiente",
 "Finding Freedom from the Endless Pursuit of More":"Encontrando liberdade da busca sem fim por mais",
 "The Practice of Generosity":"A pr\u00e1tica da generosidade",
 "Turning Good Intentions into Open-Handed Habits":"Transformando boas inten\u00e7\u00f5es em h\u00e1bitos de m\u00e3os abertas",
 "The Generous Family":"A fam\u00edlia generosa",
 "Passing Down Joy, Gratitude, and Stewardship":"Transmitindo alegria, gratid\u00e3o e mordomia",
 "The Legacy of Generosity":"O legado da generosidade",
 "Living and Giving for What Outlives You":"Vivendo e doando pelo que sobrevive a voc\u00ea",
}}
json.dump(DEEP_TR["es"], open("/home/claude/tr_es_deep.json","w"), ensure_ascii=False)
json.dump(DEEP_TR["pt"], open("/home/claude/tr_pt_deep.json","w"), ensure_ascii=False)
print("DEEP maps:", len(DEEP_TR["es"]), "pairs each")
