---
urn: urn:dev:kb:steve-jobs-principios-salud
nombre: steve-jobs-principios-salud
version: 1.0.0
estado: publicado
descripcion: "Extension del canon de diseno de Steve Jobs a la superficie de los sistemas institucionales de salud (EHR/HIS/LIS, flujos clinicos, alertas, portales de paciente): el residente agotado de las 2 AM como benchmark, la estetica como herramienta cognitiva en alto riesgo, offline como caso base, y los principios INTEGROS de seguridad del paciente (ganar el derecho a interrumpir, el error silencioso, dignidad en cada pixel, la clinica gana sobre el diseno). Especializa el canon; aqui solo el delta de superficie."
fuente: "Sintesis nueva (NO migracion byte-fiel), 2026-06-14, desde la bestia (~/kora @ 017dc1b9) jobs-healthcare-ux AGENT.md (sha256:f56d28841a91555044410bef1a43025c2f7b07deff61b214db2e686413e50666) + su kb principios-constitucionales (sha256:5f44a22ef2563f8fa4b4b7babce932ae6ddd8647a6069c03f900851d04b8d99b). Especializa el canon urn:dev:kb:steve-jobs-canon-diseno (relacion depende+refina): contiene SOLO lo especifico de UX clinica; los principios compartidos viven en el canon, citados por nombre. Decision de namespace: dev (no salud) por cohesion del corpus de diseno steve-jobs — es conocimiento de DISENO sobre superficies clinicas, no practica clinica (que vive en artefactos/conocimiento/salud/). Los principios de seguridad del paciente se conservan integros y con teeth, jamas diluidos al canon: una interrupcion mal calibrada en salud no molesta, mata."
autor: FS
creado: 2026-06-14
lang: es
tags: [steve-jobs, ux-clinica, salud, seguridad-del-paciente, ehr, diseno-clinico, alertas, carga-cognitiva]
familia: bok
depende: [urn:dev:kb:steve-jobs-canon-diseno]
refina: [urn:dev:kb:steve-jobs-canon-diseno]
---
# Steve Jobs aplicado a la UX de sistemas institucionales de salud

Este kb especializa el canon urn:dev:kb:steve-jobs-canon-diseno a la superficie
clínica: hospitales públicos latinoamericanos, donde el usuario final es un
residente con dieciocho horas de guardia y el costo de un error de diseño no se
mide en frustración sino en eventos adversos. Depende de él por relación; aquí
solo el delta de superficie, nunca re-enunciado. Cuando un principio clínico
lleva la marca **[SEGURIDAD]**, no se diluye ni se negocia: en salud la
diferencia entre interrumpir bien y mal no es elegancia, es la línea entre
prevenir un daño y provocarlo.

## Anclajes al canon

Los invariantes del canon rigen aquí sin reescribirse; este documento solo los
invoca por nombre cuando un principio clínico los afila. Tres anclajes, con el
delta que la superficie clínica añade y el canon no dice:

- Especializa **Cero entrenamiento o no existe** del canon
  (urn:dev:kb:steve-jobs-canon-diseno): el benchmark honesto no es abstracto sino
  el tiempo-reloj real por flujo, el primer día de un servicio en marcha, con el
  residente que recién rota y nadie le explicó nada. El **curso de capacitación
  obligatorio** es la encarnación clínica de **La Montaña de Tutorial**: en salud
  el teeth es que ese curso suele ser la coartada de un sistema que no se ganó su
  primera interacción, y el "lo enseñamos en la inducción" sustituye al diseño que
  faltó.

- Especializa **Default brutal: criterio, no configuración** del canon: prohibido
  pedirle al clínico exhausto que diseñe su propia interfaz —sin dashboards
  personalizables, sin layouts drag-and-drop, sin sliders de configuración de
  vista—. La adaptación contextual automática sí es legítima y es el camino: la
  vista se reordena sola por dispositivo (tablet de pasillo vs. estación fija),
  por rol y por contexto físico, sin que el usuario toque un ajuste. Lo ilegítimo
  es trasladar la carga de configuración al usuario; cada slider que le pasamos al
  clínico es complejidad que no tuvimos el coraje de resolver nosotros. Los
  **dashboards personalizables / layouts drag-and-drop** son la encarnación
  clínica de **El Configurador** del canon: misma cobardía, bata blanca.

- Especializa **Lo bello no es decoración, es función cognitiva** del canon: el
  delta clínico es que el contexto es de alto riesgo y la estética se vuelve
  triaje cognitivo. Una jerarquía tipográfica resuelve, en la práctica, qué dosis
  se lee a las 2 AM y cuál se confunde; el espaciado separa lo crítico de lo
  accesorio en una pantalla densa de paciente; el contraste decide si una alerta
  se ve bajo luz fluorescente. La pregunta funcional aquí es clínica: qué hay que
  ver primero y qué puede pasar desapercibido con consecuencias graves.

Lo que viene es lo que el canon **no** alcanza: el delta donde el cuerpo del
paciente, el turno de noche y la conectividad inestable cambian las reglas.

## Principios específicos de UX clínica

**I. La mirada pertenece al paciente.** Especializa la **Empatía
trascendental** del canon —diseñar desde el job humano— y la lleva a su forma
más radical en esta superficie: la interfaz ideal es la que no necesita ser
mirada, porque robarle la mirada al clínico es robarle la relación terapéutica, y
eso no se compensa con un dato más en la ficha. El delta concreto: ambient
listening sobre formularios, voz sobre teclado, inferencia sobre entrada manual,
resumen post-consulta sobre documentación en tiempo real. Y ojo con la métrica:
no es "tiempo de pantalla mejorado", es tiempo de pantalla **eliminado**. Si tu
indicador celebra que el clínico mira la pantalla de forma más eficiente, estás
midiendo la derrota.

**III. Ganar el derecho a interrumpir. [SEGURIDAD]** Cada alerta pasa una prueba,
y es literal: si esta alerta fuera una persona que te toca el hombro mientras
atendés a un paciente, ¿merecería interrumpirte? La mayoría no lo merece. Por eso
se mide con un NNT equivalente —cuántas alertas hay que disparar para que UNA
prevenga un evento adverso real— y las de baja especificidad bajan a un canal
secundario donde se acumulan en silencio, no en la cara del clínico. Hay eco aquí
del agéntico "no interrogar", pero no es lo mismo y no se generaliza: en un agente
una interrupción mal calibrada molesta; en salud mata, porque entrena al clínico a
descartar todo y entonces la alerta que sí importaba se pierde con las demás. Por
eso el descarte sistemático nunca es negligencia del clínico: es señal de diseño,
y el dueño del problema es quien diseñó.

**IV. La complejidad es nuestra, la claridad es del usuario.** Especializa la
**Jerarquía absoluta** del canon con un delta que justifica enunciarlo aparte: detrás
de la superficie limpia hay un motor de inferencia, normalización, cruce de datos
y lógica clínica trabajando. No es solo ocultar profundidad bajo demanda; es que
el sistema *hace el trabajo clínico pesado* para que la superficie pueda ser
radicalmente simple. Esconder un campo no es absorción de complejidad si detrás no
hay nadie pensando.

**V. El tiempo del clínico se mide en vidas.** Cada minuto que el sistema le roba a
un clínico es un minuto que no le da a un paciente. Y esto escala brutal: treinta
segundos ahorrados por consulta en un hospital con quinientas consultas diarias son
más de cuatro horas de atención recuperada cada día. La métrica es tiempo-reloj
real por flujo, medido el primer día **sin** entrenamiento —porque medir con
entrenamiento es hacerse trampa al solitario.

**VI. La narrativa primero, la estructura después.** El pensamiento clínico es
narrativo, y los formularios estructurados lo matan. El sistema acepta lenguaje
natural y **extrae** la estructura, no la impone: el clínico habla o escribe como
piensa, el sistema organiza el SOAP, el clínico revisa y corrige. Invertir esto
—exigir que el humano piense en celdas para que la máquina no tenga que pensar— es
el pecado de origen del EHR moderno.

**VII. Diseñar para el equipo, no para el rol.** La unidad de cuidado no es el
médico: es el equipo —médico, enfermero, técnico, farmacéutico, trabajador social,
familiar. Los sistemas que diseñan vistas por rol crean silos de información, y un
silo en salud es un lugar donde la información que salva se queda atascada. Cada
miembro ve lo que necesita para la tarea que está haciendo ahora, no lo que su
cargo "tiene permitido" ver.

**VIII. La transición no existe.** Para el paciente el cuidado es continuo: no hay
"alta de urgencias" e "ingreso a piso", hay una persona que sigue enferma y se
mueve de lugar. La transición es una ficción administrativa nuestra, no una
realidad clínica suya. Por eso: cero re-entrada de datos en transiciones, el
contexto viaja con el paciente y no con el episodio. Cada vez que un sistema obliga
a re-tipear lo que ya sabe porque "cambió el episodio", está sirviéndose a sí mismo
y traicionando la continuidad del cuidado.

**IX. Dignidad en cada pixel. [SEGURIDAD/ÉTICA]** Especializa **El copy es
interfaz** del canon —cada palabra carga peso— y le suma la carga de la dignidad.
El paciente es una persona, no un registro: nombre antes que número de ficha,
contexto de vida antes que lista de diagnósticos, preferencias antes que alergias
codificadas. El anti-lenguaje es concreto y no negociable: no "el diabético de la
cama 4", sino "María González, 67 años, vive con su hija, diabetes desde 2015". El
lenguaje que cosifica al paciente no es un detalle de tono: es la forma en que un
sistema enseña a un equipo a dejar de ver personas.

**XI. Offline es el caso base.** En Latinoamérica la conectividad no es garantía
—zonas rurales, urgencias, cortes. El caso base de diseño es offline; la
conectividad es enhancement, no premisa. Sistema completo en modo local, sincroniza
cuando puede, y en conflicto gana la versión más reciente del dato clínico. Diseñar
asumiendo red estable es diseñar para un hospital que no existe; es la versión de
infraestructura de *diseñar para las 2 AM*.

**XII. La privacidad es experiencia, no checkbox.** La privacidad no se resuelve
con un formulario de consentimiento firmado y olvidado: se resuelve con diseño
—qué información se muestra a quién, cuándo, cómo. Awareness contextual: el sistema
sabe si el dispositivo está en consultorio, pasillo o sala de espera, y ajusta la
exposición de datos sensibles. Un checkbox de "acepto los términos" no protege a
nadie en un pasillo lleno de gente.

**XIII. Medir lo que importa.** Las métricas no son clicks, page views ni adoption
rate. Son tiempo-a-decisión-clínica, eventos adversos prevenidos, readmisiones
evitadas, burnout clínico reducido, continuidad de cuidado. La regla es seca: si
una métrica no conecta con un outcome de salud, no es una métrica, es vanidad. Un
dashboard que celebra "usuarios activos" en un EHR mide cuánto sufre la gente, no
cuánto mejora el cuidado.

**XV. Diseñar para las 2 AM.** El usuario de diseño no es el médico descansado de
las 10 AM. Es el residente con dieciocho horas de guardia, tres pacientes críticos,
un celular con la pantalla rota y luz fluorescente. Por default: contraste alto,
tamaños de fuente generosos, targets de toque grandes, flujos que perdonan errores,
undo omnipresente. Esto realiza la **Reversibilidad universal** del canon en su
contexto más exigente: el delta es que cuando el error lo comete alguien al borde
del colapso, el undo no es cortesía, es red de seguridad clínica. El residente
agotado de las 2 AM es el benchmark, no un caso límite; un sistema que solo
funciona con la atención fresca falla exactamente cuando más se lo necesita.

**XVI. El error más peligroso es el silencioso. [SEGURIDAD]** Un error ruidoso —un
mensaje en pantalla— es preferible a uno silencioso: un dato guardado mal, una
alerta que no se disparó, una orden duplicada sin aviso. El error silencioso es el
peor porque nadie lo ve hasta que ya hizo daño. Por eso: audit trail clínico
completo, reconciliación activa de datos, detección de anomalías en órdenes. Un
sistema que falla en silencio para "no molestar" está eligiendo la comodidad de la
interfaz sobre la vida del paciente.

**XVII. Heredar con humildad, reemplazar con paciencia.** Los sistemas de salud
existentes tienen décadas de datos, flujos arraigados y personal que aprendió a
trabajar con sus limitaciones. No se llega con arrogancia a "disrumpir" un
hospital: migración progresiva, coexistencia con legacy, importación fidedigna de
datos históricos. El que llega prometiendo barrer con todo de un golpe no entendió
que esos flujos viejos, por torpes que sean, hoy sostienen pacientes vivos.

**XVIII. Esto no se termina nunca.** El diseño de sistemas de salud no tiene
versión final: la medicina evoluciona, las guías cambian, los patrones de
enfermedad se transforman. Arquitectura modular, configuración sin redespliegue,
feedback loops continuos y humildad epistemológica. El delta sobre **Default
brutal** del canon: seguimos hard-codeando la decisión correcta de hoy —esto no es
una excusa para volver a los dashboards configurables—, pero la decisión correcta
de hoy va a cambiar, y el sistema tiene que poder cambiar con ella sin romper el
cuidado. La evolución la absorbe la arquitectura, no la traslada al usuario en
forma de settings.

**Regla de seguridad. [SEGURIDAD]** Una recomendación de diseño que comprometa la
seguridad clínica se mitiga sin discusión, porque la seguridad clínica prevalece
sobre cualquier principio de diseño. La clínica gana sobre el diseño. Si un paso de
flujo previene un error médico, se queda aunque sea feo, aunque agregue fricción,
aunque viole la sustracción. Y ante la duda, se consulta al operador: no se
optimiza la pantalla a costa del paciente. Este es el Norte del agente, el techo
sobre todos los demás principios, y no admite excepción elegante.

## Preguntas letales clínicas

Estas son las preguntas que se hacen cuando ya pasaste las preguntas letales del
canon y estás parado frente a una pantalla clínica:

- Si esta alerta fuera una persona que te toca el hombro mientras atendés a un
  paciente, ¿merecería la interrupción? (el derecho a interrumpir, **III**).
- ¿Cuántas alertas hay que mostrar para que UNA prevenga un evento adverso real?
  Si no sabés el número, no diseñaste el sistema de alertas: lo apilaste.
- ¿Esta métrica conecta con un outcome de salud? Si no, es vanidad, no métrica
  —y un dashboard de vanidad en un hospital es ruido caro.
- ¿Qué necesita ver primero el clínico, y qué puede pasar desapercibido con
  consecuencias graves? Esta pregunta gobierna cada decisión visual; aquí la
  jerarquía no es estética, es triaje cognitivo.
- ¿Estás diseñando para el clínico ideal de las 10 AM en vez del residente agotado
  de las 2 AM? Si lo hacés, estás derivando, y tu sistema va a fallar exactamente
  cuando más se lo necesita.
- Si esta decisión de diseño estuviera entre un paciente y su cuidado, ¿la
  eliminarías? Si la respuesta es sí, ya sabés qué hacer. Ese es el Norte.

## Anti-patrones clínicos

Cada uno de estos viola principios concretos. No son malas prácticas genéricas:
son las formas específicas en que un sistema de salud traiciona a su gente.
Cuando un anti-patrón clínico es la encarnación de uno universal del canon, se
cita el canónico y se deja solo el teeth clínico.

- **Alert Fatigue** — tantas alertas que el clínico las descarta todas y la crítica
  se pierde en el ruido. Es el fracaso prototípico de salud: viola **III** y
  **XVI**. Cada alerta que no se ganó el derecho a interrumpir le quita
  credibilidad a la que sí lo merecía.
- **Form Hell** — documentación clínica reducida a 47 campos en 12 pestañas; la
  narrativa clínica muere ahí dentro. Viola **VI** y **V**: mata el pensamiento
  narrativo y roba el tiempo que pertenece al paciente.
- **Tab Soup** — información del paciente repartida en 15 pestañas que el clínico
  navega como mapa del tesoro. Viola **IV** y **VII**: la complejidad que debía
  absorber el sistema se la comió el usuario, y la fragmentación rompe la vista de
  equipo.
- **Handoff Gap** — información que se pierde en las transiciones, cada episodio
  tratado como independiente. Viola **VIII** y **VII**: la transición no existía
  para el paciente, pero el sistema la inventó y dejó caer el contexto en la grieta.
- **Screen-Time Theft** — el sistema demanda tanta interacción que el clínico mira
  más la pantalla que al paciente. Viola **I** y **V**: roba la mirada y roba el
  tiempo, las dos cosas que más caro cuestan en una consulta.
- **Click Liturgy** — acciones que exigen 7 clicks cuando deberían exigir 0;
  ceremonias de interfaz sin valor clínico. Viola **V** y **X**: cada click de
  liturgia es tiempo robado a un paciente y una barrera de entrenamiento que no
  debió existir.
- **Copy-Paste Medicine** — el sistema incentiva copiar y pegar, y las notas se
  llenan de información obsoleta. Viola **VI** y **IX**: degrada la narrativa real
  y, peor, convierte al paciente en un bloque de texto reciclado en vez de una
  persona con una historia que cambió desde ayer.
- **Checkbox Compliance** — la ilusión de que un checkbox equivale a un proceso
  clínico significativo. Viola **XIII** y **XVI**: mide cumplimiento de formulario
  en vez de outcome, y esconde en silencio que el proceso real nunca ocurrió.
- **Dashboard de autor** — pedirle al clínico que arme su propia vista con widgets
  arrastrables y paneles configurables. Es la encarnación clínica de **El
  Configurador** del canon: el teeth de salud es que delega el diseño de la
  interfaz en el usuario más agotado del hospital, justo el que no tiene un
  segundo para configurarla, y disfraza de "flexibilidad" la decisión que el
  diseñador no tomó. Viola **II** (default brutal clínico).
- **Curso obligatorio** — la inducción de N horas que el personal debe atravesar
  antes de poder usar el sistema. Es la encarnación clínica de **La Montaña de
  Tutorial** del canon: el teeth de salud es que el curso se vuelve la coartada del
  diseño que no se ganó la primera interacción, y la rotación constante de
  residentes garantiza que siempre haya alguien usándolo sin haberlo tomado.
  Viola el anclaje a **Cero entrenamiento o no existe**.
- **Role Silo** — información visible solo para un rol cuando el equipo completo la
  necesita; el cuidado se fragmenta. Viola **VII** y **VIII**: rompe la unidad de
  cuidado y corta la continuidad justo donde el paciente más necesita que el
  contexto viaje con él.
