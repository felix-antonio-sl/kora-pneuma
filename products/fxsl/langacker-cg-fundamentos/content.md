---
urn: urn:fxsl:kb:langacker-cg-fundamentos
nombre: langacker-cg-fundamentos
version: 1.0.0
estado: publicado
descripcion: "Fundamentos de Cognitive Grammar (Parte I, caps. 1-3): la tesis de la gramática como simbolización, semántica conceptual (significado como conceptualización, visión enciclopédica, dominios, ICMs) y construal (especificidad, foco, prominencia —profiling, trajector/landmark— y perspectiva —viewing arrangement, vantage point, subjetividad/objetividad, punto de referencia—)."
fuente: "Langacker, Ronald W. (2008). Cognitive Grammar: A Basic Introduction. Oxford University Press. Archivo fuente: /home/felix/kora-external-sources/Cognitive Grammar_ A Basic Introduction - Ronald W. Langacker.txt (sha256:6370e8b08fdaaf1ebc2a05db7a4b0db553cf9384a58bb7532f3a0f037838707f). Alcance: Part I (Preliminaries), caps. 1-3 (pp. 3-90 del libro; líneas 182-1199 del archivo). Descartado: prefacio, contenidos, front matter, referencias, índice y figuras (descripciones textuales conservadas por capítulo; los diagramas como objetos visuales se consultan en el original fuente). Los caps. 4-14 se korifican en artefactos hermanos (langacker-cg-clases-y-construcciones, langacker-cg-estructuras, langacker-cg-fronteras)."
autor: FS
creado: 2026-06-29
lang: es
tags: [cognitive-grammar, langacker, linguistica-cognitiva, gramatica, simbolizacion, semantica-conceptual, construal, profiling, trajector-landmark, perspectiva, subjetividad]
familia: bok
---

# Fundamentos de Cognitive Grammar

## 1. La tesis central: la gramática es simbólica

**Recursos gráficos del capítulo 1** (figs. 1.1–1.4 del fuente; descripciones textuales, los diagramas se consultan en el original):

- **1.1** — Compara dos formatos para el concepto TRIANGLE: (a) representación proposicional tipo lista/enumeración de primitivas vs. (b) una imagen diagramática única con el triángulo dibujado. Argumento: CG prefiere descripciones imagéticas/diagramáticas sobre fórmulas proposicionales para captar la naturaleza del concepto.
- **1.2** — Tres diagramas de complejidad simbólica creciente: (a) una estructura simbólica simple con caja S arriba y P abajo conectadas (polo semántico y fonológico, relación S/P); (b) dos cajas externas combinadas dentro de una caja externa mayor que representa el compuesto de mayor nivel; (c) tres niveles anidados con la nueva capa exterior conteniendo el ensamblaje previo. Las cajas en escalón ilustran la formación de ensamblajes simbólicos jerárquicos (monema < palabra < compuesto).
- **1.3** — (a) Árbol sintáctico estándar: ítems léxicos como átomos insertados en casillas ('slots') de un árbol sintáctico, representados como cajas pequeñas en la base unidas al árbol; (b) mismo árbol pero con cajas de tamaños muy variables que subsumen porciones distintas, incluso discontinuas — una caja grande abarca nodos no contiguos (etiquetas b y d conectadas) para mostrar que las expresiones idiomáticas pueden ser discontinuas. Argumenta que el léxico no se reduce a átomos sintácticos.
- **1.4** — Dos paneles sobre el espacio 'complejidad simbólica × schematicidad/especifidad': (a) eje horizontal que muestra expresiones específicas vs. noveles/no convencionales con una línea punteada indicando ausencia de frontera nítida; (b) el mismo espacio 2D poblado por símbolos que representan ítems léxicos prototípicos (perro, moonless, cuidadosamente, toothbrush) mezclados con reglas gramaticales y marcadores — sin línea de demarcación tajante.

La afirmación más fundamental de CG: **la gramática es de naturaleza simbólica**. Un símbolo se define como el emparejamiento entre una **estructura semántica** y una **estructura fonológica**, tal que una evoca a la otra. Un ítem léxico simple (e.g. _skunk_) es simbólico porque reside en el par significado-forma fonológica. La tesis de CG: **nada más que estructuras simbólicas es necesario invocar** para caracterizar expresiones complejas y los patrones que instancian. Específicamente: **léxico y gramática forman una gradación que consiste únicamente en assemblies de estructuras simbólicas** (_symbolic assemblies_). Consecuencia inmediata: todas las nociones válidamente postuladas para la descripción gramatical (e.g. "nombre", "sujeto", "participio pasado") deben de algún modo ser significativas.

### Lo que CG NO niega
- CG no niega la existencia de la gramática.
- No afirma que "todo es semántica" ni que la gramática sea predecible desde el significado (versión débil de autonomía: la gramática no es completamente predecible desde factores independientes — CG es compatible con esto).
- Lo que CG rechaza es la versión **fuerte** de la tesis de autonomía: que la descripción sintáctica requiera un conjunto especial de primitivos puramente gramaticales, irreducibles a nada más fundamental.
- La reducción de la gramática a assemblies simbólicos **no es eliminación** sino caracterización: analizar moléculas de agua como configuraciones de átomos de hidrógeno y oxígeno no niega la existencia del agua.
- **Falacia tipo/predictibilidad** (_type/predictability fallacy_): confundir la no-predictibilidad de la gramática con la necesidad de primitivos gramaticales autónomos.

### Organización global del sistema lingüístico
Para cumplir su función semiológica (permitir que significados sean simbolizados fonológicamente), una lengua necesita al menos tres tipos de estructuras: **semánticas**, **fonológicas** y **simbólicas**. CG afirma que **solo estas tres son necesarias**. Esto es austeridad teórica (_theoretical austerity_). Lo que lo hace posible: léxico, morfología y sintaxis forman un continuo completamente reducible a assemblies de estructuras simbólicas.

### Complejidad simbólica
- **Estructura semántica**: conceptualizaciones explotadas para propósitos lingüísticos.
- **Estructura fonológica**: sonidos, gestos, representaciones ortográficas; su rasgo esencial es ser manifiesta (_overt_).
- **Estructura simbólica** (Σ): vínculo entre una estructura semántica (S, polo semántico) y una fonológica (P, polo fonológico); notación: `[[S]/[P]]`. Es **bipolar**.
- **Symbolic assembly**: combinación de estructuras simbólicas para producir una de nivel superior. La complejidad simbólica es el grado de anidamiento composicional.
- **Morfema**: expresión con complejidad simbólica cero (no analizable en componentes simbólicos menores); equivalente a un _symbolic assembly_ degenerado de una sola relación simbólica.

Representación formulaica:
```
(a) [[MOON]/[moon]]                          — morfema
(b) [[[MOON]/[moon]] - [[LESS]/[less]]]      — moonless
(c) [[[[MOON]/[moon]] - [[LESS]/[less]]] - [[NIGHT]/[night]]]  — moonless night
```

Todas estas son expresiones fijas convencionales en inglés, por tanto **ítems léxicos** bajo la definición de CG: **léxico = conjunto de expresiones fijas** (_fixed expressions_) en una lengua. Esto implica que no hay frontera nítida entre léxico y expresiones no-léxicas (la familiaridad y convencionalidad son cuestiones de grado).

### Fenómenos cognitivos básicos reclutados por el lenguaje

1. **Asociación** — establecer conexiones psicológicas; manifiesta en CG en la relación simbólica (S↔P).
2. **Automatización** (_entrenchment_) — una estructura se vuelve unidad (_unit_) por repetición; los ítems léxicos son expresiones que alcanzaron estatus de unidad. Notación: `[ ]` para unidades, `( )` para no-unidades. El estatus de unidad no implica ausencia de componentes: _moonless night_ es unidad pero analizable en _moonless_ y _night_.
3. **Esquematización** — extraer la comunalidad de experiencias múltiples para alcanzar una concepción de mayor abstracción. Puede iterarse: _ring_ → 'pieza circular de joyería para el dedo' → 'adorno circular para el cuerpo' → 'objeto circular' → 'entidad circular'.
4. **Categorización** — interpretar la experiencia respecto a estructuras preexistentes. Dos tipos:
   - **A → B** (flecha sólida): A es esquemático para B; B **elabora** o **instancia** A (compatible con las especificaciones de A pero con mayor precisión). E.g. `CIRCULAR ENTITY → CIRCULAR ARENA`.
   - **A - - > B** (flecha punteada): B entra en conflicto con las especificaciones de A pero se asimila a la categoría por similitud; A es **prototipo**, B es **extensión**. E.g. `CIRCULAR ARENA - - > RECTANGULAR ARENA` (ring aplicado a arenas rectangulares de boxeo).

### Léxico y gramática como gradación
Los ítems léxicos varían en dos parámetros continuos:
- **Complejidad simbólica**: _moon_ < _moonless_ < _moonless night_ < _a moonless night_ ...
- **Esquematicidad** (o su inversa, especificidad): desde esquemas altamente abstractos (_thing_ → _creature_ → _animal_ → _dog_ → _poodle_) hasta especificaciones finas.

Muchas unidades léxicas multi-palabra contienen **elementos esquemáticos** (_partially schematic units_), e.g.:
- `X crane X+POSS neck` (X = agente y poseedor)
- `V_s X en la N_b` (V_s = verbo de golpe, N_b = parte del cuerpo)
- `a N₁ + less N₂` (e.g. _a moonless night_, _a childless couple_)

Estas unidades subvierten la distinción nítida léxico/gramática: contienen elementos léxicos específicos (atípico para gramática) y esquematicidad parcial (atípico para léxico). Constituyen el componente esencial —quizás preponderante— del conocimiento lingüístico convencional de un hablante fluido.

### El _content requirement_ (requisito de contenido)
Las únicas unidades permitidas en la descripción de un sistema lingüístico son:
1. Estructuras semánticas, fonológicas y simbólicas que son **partes de expresiones ocurrientes** (_occurring expressions_).
2. **Esquematizaciones** de estructuras permitidas.
3. **Relaciones de categorización** entre estructuras permitidas.

Esto impone restricciones severas: no es válido postular estructuras subyacentes no simbolizadas, reglas generativas en el sentido clásico ni filtros extrínsecos.

### Principios filosóficos de CG
- **Principio de integración**: favorece inclusividad y unificación; reconciliar información de fuentes múltiples; tratamiento unificado de dimensiones de la estructura lingüística; evitar dicotomías donde hay gradación.
- **Principio de naturalidad**: el lenguaje —correctamente analizado— es razonable y comprensible en vista de sus funciones semiológica e interactiva y su anclaje biológico, cognitivo y sociocultural.
- **Principio de paciencia**: no poner la carreta delante del caballo; posponer la formalización hasta tener comprensión conceptual básica; no precipitarse en preguntas prematuras (e.g. grado de especificación innata del lenguaje).

---

## 2. Semántica conceptual

**Recursos gráficos del capítulo 2** (figs. 2.1–2.9 del fuente; descripciones textuales, los diagramas se consultan en el original):

- **2.1** — Diagrama del concepto ENTER como combinación de tres image-schemas mostrados como cajas/círculos etiquetados: OBJECT (objeto físico como punto), SOURCE-PATH-GOAL (trayectoria con SOURCE → PATH → GOAL) y CONTAINER-CONTENT (contenedor con contenido interno). Las flechas y líneas indican cómo se ensamblan los image schemas para formar la concepción compleja de 'entrar' (vs. la fórmula proposicional de Jackendoff).
- **2.2** — Red polisé mica parcial de la palabra 'ring': cajas rectangulares con etiquetas (CIRCULAR ENTITY, CIRCULAR ARENA, RECTANGULAR ARENA, ENCLOSING ENTITY, etc.) conectadas por flechas — sólidas para elaboración de esquema y DISCONTINUAS (──>) para extensión metonímica/prototype. Las cajas de LÍNEAS GRUESAS indican los sentidos más prototípicos/centrales; las demás son extensiones o sentidos secundarios.
- **2.3** — Semántica diccionario (dictionary view) vs. enciclopédica: (a) un gran CÍRCULO representa el conocimiento total sobre una entidad y dentro una pequeña CAJA DE LÍNEAS GRUESAS delimita las especificaciones 'puramente lingüísticas' (pocas features discretas); (b) en cambio, una serie de CÍRCULOS CONCÉNTRICOS indican conocimiento con CENTRALIDAD variable — cada ÓVALO de línea gruesa representa el subconjunto activado en una ocasión particular de uso.
- **2.4** — Cuatro diagramas en fila etiquetados (a)-(d) sobre la relación semantics/pragmatics: (a) DOS regiones separadas por una BORDERLINE nítida (dicotomía clásica); (b) pragmática ausente; (c) ausencia total de diferenciación; (d) una ESCALA/gradiente horizontal sin frontera precisa, con puntos en los extremos identificables como semánticos o pragmáticos. Argumento: rechazar la dicotomía tajante a favor de una gradación.
- **2.5** — Cuatro versiones lingüísticas de un mismo escenario (vaso con agua hasta la mitad), representadas como cuatro CAJAS con líneas gruesas en diferentes regiones: (1) vaso con agua en él → designa el CONTENEDOR (vaso); (2) el agua en el vaso → designa el CONTENIDO (agua); (3) el vaso está medio lleno → designa RELACIÓN de llenado a la mitad; (4) el vaso está medio vacío → designa RELACIÓN de vacío a la mitad. Mismo contenido, construcciones/perfiles distintos.
- **2.6** — Conjunto de ÓVALOS/ELIPSES que se superponen ampliamente representando los dominios que constituyen la matriz de 'glass'. En el centro un CÍRCULO DE LÍNEA GRUESA representa el DESIGNATUM del lexema (el referente), conectado por su pertenencia a cada dominio. Las elipses solapadas muestran que los dominios no son disjuntos sino que se incluyen unos a otros.
- **2.7** — Versión 'explotada' de 2.6: los ÓVALOS de dominio (space, shape, orientación, función₁, función₂, material, tamaño, otros) están dibujados por separado sin mostrar superposición, cada uno etiquetado; LÍNEAS PUNTEADAS de correspondencia conectan cada dominio con un CÍRCULO DE LÍNEA GRUESA común — el designatum del ítem léxico. Visualiza la CENTRALIDAD diferencial: dominios 1-7 centrales, los de 'otros' periféricos.
- **2.8** — Diagrama que reusa los dominios de 2.7 como cajas separadas etiquetadas, conectadas mediante LÍNEAS cuyo GROSOR variable (gruesa vs. fina) indica el GRADO DE ACTIVACIÓN del dominio en un evento de uso particular. Ilustra cómo diferentes contextos activan diferentes subconjuntos de la matriz.
- **2.9** — Configuración de mental spaces para la metáfora 'The thought just flew right out of my head': tres ÓVALOS/REGIONES conectadas — SOURCE SPACE (con BIRD 'B' dentro de CAGE 'C' observado por VIEWER 'V', flechas sólida y discontinua entre ellos); TARGET SPACE (THOUGHT 'T', HEAD 'H', SUBJECT 'S' con flecha entre T y H); y BLENDED SPACE con entidades T', H', S'. CONEXIONES punteadas entre pares análogos de entidades dan cuenta del mapeo metafórico.

### Visión enciclopédica del significado
CG adopta una **visión enciclopédica** (_encyclopedic view_): el significado de una expresión no es un conjunto acotado de rasgos semánticos sino que evoca un cuerpo abierto de conocimiento. Distinciones clave:

- **Significado lingüístico vs. conocimiento extralingüístico**: no hay frontera nítida; es una cuestión de grado de centralidad y convencionalidad.
- **Centralidad** (_centrality_): ciertas especificaciones son más centrales al significado de una expresión; las periféricas residen en el conocimiento general. La gradación se mide por el grado en que una especificación es **inherente** a la caracterización de la entidad designada, y el grado en que es **convencional** (compartida por la comunidad de habla).
- **Dominio** (_domain_): contexto o ámbito de conocimiento respecto al cual se caracteriza una unidad semántica. Todo concepto presupone uno o más dominios.

Tipos de dominios:
- **Dominios básicos** (_basic domains_): no reducibles a conceptos más fundamentales. E.g. espacio, tiempo, escala de tono, temperatura, presión, espacio de color. Son los _primitivos conceptuales_ de CG (no los rasgos semánticos de otras teorías).
- **Dominios no-básicos**: cualquier concepto o complejo conceptual que presupone dominios más básicos. E.g. el dominio del cuerpo humano presupone el espacio.
- **Dominio abstracto**: no anclado directamente en experiencia sensoriomotora. E.g. dominios de relaciones de parentesco, sistemas numéricos, calendarios, sistemas políticos.
- **Matriz de dominios** (_domain matrix_): el conjunto completo de dominios respecto a los cuales se caracteriza una expresión, con grados variables de centralidad. E.g. _knife_ evoca espacio (forma), función (cortar), actividad (comer), dominio cultural (cubierto), etc.
- **_Idealized Cognitive Model_** (ICM): estructura cognitiva compleja que representa una idealización de algún aspecto del mundo. E.g. el ICM de "semana" (ciclo de 7 días), "soltero" (adulto no casado en una cultura donde se espera el matrimonio).
- **Espacio mental** (_mental space_): constructo dinámico, local, creado online para propósitos locales de pensamiento y habla. Los ICMs son estructuras estables; los espacios mentales se montan sobre ellos para representar situaciones específicas. E.g. _In that movie, the butler is the murderer_: el espacio mental de la película, el espacio de la realidad.

### Composición semántica
La composición semántica es **solo parcial**. El significado de una expresión compleja:
1. Depende de los significados de los componentes y los patrones composicionales (esquemas construccionales).
2. Presupone un **sustrato conceptual** (_conceptual substrate_) elaborado: conocimiento de fondo, contexto físico/social/lingüístico.
3. Los hablantes despliegan habilidades imaginativas e interpretativas.

En sentido estricto, el significado de una expresión compleja **no puede ser computado** a partir de significados léxicos y patrones composicionales; se describe más precisamente como **motivado** (_prompted_) por ellos.

### Arquetipos conceptuales
Los **arquetipos conceptuales** (_conceptual archetypes_) son concepciones elementales ancladas en la experiencia que funcionan como prototipos de categorías lingüísticas fundamentales:

- **Modelo de bolas de billar** (_billiard-ball model_): objetos físicos discretos que se mueven en el espacio, hacen contacto, transmiten energía. Prototípico para eventos y la distinción nombre/verbo.
- **Modelo del escenario** (_stage model_): un observador (sujeto de concepción) observa eventos que se desarrollan en un escenario (onstage region). Fundamento metafórico para la organización clausal (sujeto = observador implícito, objeto = participante focal onstage).
- **Roles arquetípicos**: agente (iniciador volitivo de acción física), paciente (entidad que cambia de estado), instrumento (objeto manipulado por agente), experimentante (locus de experiencia mental), movedor (_mover_) (entidad que se desplaza).
- **Modelo de la cadena de acción** (_action chain_): secuencia de interacciones energéticas entre participantes conectados.

---

## 3. Construal

**Recursos gráficos del capítulo 3** (figs. 3.1–3.14 del fuente; descripciones textuales, los diagramas se consultan en el original):

- **3.1** — Estructura jerárquica del compuesto lipstick maker en múltiples niveles: cajas anidadas que van de los componentes atómicos (LIP, STICK, MAKE/–ER) hasta los compuestos lipstick, maker y finalmente lipstick maker como caja externa con líneas de grosor variable — el grosor codifica el GRADO DE FOREGROUNDING; las cajas de LIPSTICK y MAKER tienen LÍNEAS DISCONTINUAS (menor analizabilidad que MAKE/MAKER/LIPSTICK MAKER). Flechas sólida y discontinua entre las cajas indican relaciones de categorización (elaboration vs. extension).
- **3.2** — Dos diagramas MS/IS: (a) elbow — la CAJA EXTERNA MS etiquetada 'BODY', una CAJA INTERNA IS etiquetada 'ARM', y dentro de esta un PROFILE (la subestructura del codo) en LÍNEAS GRUESAS; (b) hand — misma estructura BODY > ARM pero con perfil distinto (la mano). LÍNEAS PUNTEADAS DE CORRESPONDENCIA entre las cajas muestran que ambas comparten base (BODY/ARM) y solo difieren en QUÉ subestructura es perfilada dentro del IS.
- **3.3** — (a) Diagrama genérico de la jerarquía whole-part: CAJAS MS/IS anidadas etiquetadas MS y IS, con un círculo 'tr' en líneas gruesas como entidad designada; LÍNEAS PUNTEADAS que conectan los IS de cada nivel; (b) aplicado a 'Part': PILA de CAJAS ÉMBEBIDAS con scopes creciente (MS contiene IS₁ que contiene IS₂…) etiquetadas Part₁, Part₂,… mostrando cómo cada parte acumula scopes previos en su matriz.
- **3.4** — Comparación temporal del verbo V vs. progresiva be Ving: (a) V — eje horizontal 't' con la CAJA TEMPORAL completa etiquetada MS/IS (todo el evento acotado visible 'onstage'); (b) be Ving — dos CAJAS, MS abarca el evento completo pero IS es un SUBINTERNO que excluye los endpoints (efecto 'zoom in' del progresivo). Línea discontinua vertical indica que IS queda FOREGROUNDED dentro de MS.
- **3.5** — Cuatro cuadros con un MISMO CÍRCULO (la rueda) como base conceptual compartida: la rueda completa aparece en uno (wheel), y en los otros tres un perfil distinto dentro de ella — HUB (eje central), SPOKE (rayo, línea desde el centro) y RIM (periferia, arco). Muestra que la MISMA BASE puede hospedar múltiples perfiles, generando wheel vs. hub/spoke/rim.
- **3.6** — Diagrama del kin term 'aunt': muestra una RELACIÓN DE PARENTESCO (línea entre dos círculos, femenino y una persona de referencia 'R') perfilada implícitamente; el PROFILE (en líneas gruesas) es el individuo FEMENINO (tía) identificado por la relación, NO la relación misma. Etiquetas 'lm' o flechas pueden indicar landmarks. La relación es esencial al contenido pero permanece unprofiled.
- **3.7** — Cuatro expresiones en una base común (relación nuclear de un caso de reproducción entre progenitor y descendiente): (a) parent — perfila la COSA/progenitor en líneas gruesas; (b) child — perfila la COSA/descendiente; (c) have a parent — perfila la RELACIÓN ESTÁTICA; (d) have a child — perfila la misma relación pero con tr/lm invertidos (direccionalidad opuesta). Diferencias semánticas residen en QUÉ se perfila y en alineación tr/lm.
- **3.8** — Dos diagramas come vs. arrive: misma base compartida — un CÍRCULO (mover) recorriendo una FLECHA (spatial path) hacia una LOC (goal location). (a) come — perfila TODO el evento de movimiento (path completo); (b) arrive — perfila sólo el SEGMENTO FINAL donde el mover alcanza la meta. Flecha tr indica el trajector; los puntos a lo largo del camino son posiciones sucesivas.
- **3.9** — Diagrama de las preposiciones 'above' y 'below': un EJE VERTICAL con DOS CÍRCULOS (X arriba, Y abajo). Above and below perfilan la MISMA RELACIÓN ESPACIAL pero con diferente alineación tr/lm — en above, X (tr) está arriba y Y (lm) abajo; en below, Y (tr) está abajo y X (lm) arriba. El contraste semántico reside ENTERAMENTE en la elección de trayector y landmark.
- **3.10** — Diagrama de 'before' y 'after': dos EVENTOS como cláusulas, cada uno perfilando una RELACIÓN DE PRECEDENCIA TEMPORAL entre eventos. 'Before' y 'after' perfilan la misma relación pero con trayector/landmark invertidos — en before el evento A (tr) precede B (lm); en after B precede A. Mensaje: la prominencia es un fenómeno CONCEPTUAL, no inherente al mundo.
- **3.11** — Dos diagramas de 'in front of' y 'behind' con VP (vantage point) y línea de mira: (a) in front of — la línea de mira DISCONTINUA va de VP hacia el participante A (lm) pasando por otro (tr); (b) behind — misma configuración pero con roles tr/lm invertidos, indicando que la intervención en la línea de mira determina la elección de expresión. Argumenta que el VP forma parte esencial del meaning.
- **3.12** — Diagrama de la frase 'next year': una SERIE HORIZONTAL de cajas separadas etiquetadas (años sucesivos) con un VP TEMPORAL (vantage point) señalado por una flecha t. La expresión perfila el segmento INMEDIATAMENTE POSTERIOR al que contiene el VP temporal.
- **3.13** — Dos diagramas de TEMPORAL: (a) PANORAMA ICÓNICO — dos flechas paralelas, una 't' (conceived time) arriba con E₁, E₂, E₃ y otra 'T' (processing time) abajo con sus conceptualizaciones A, B, C y expresiones a, b, c en MISMO orden; (b) PANORAMA NO-ICÓNICO — el orden en T es a > b > c pero en t los eventos concebidos van en orden inverso E₃ > E₂ > E₁, requiriendo backtracking.
- **3.14** — Diagrama de la RELACIÓN DE PUNTO DE REFERENCIA (reference-point): un CÍRCULO 'R' (referente de referencia) conectado por una doble flecha (dos fases secuenciales de awareness) a un CÍRCULO 'T' (target), con una ELIPSE DENOMINADA 'DOMINION' a su alrededor que representa el conjunto de targets potenciales accesibles.

El **construal** es la capacidad de concebir y retratar la misma situación de formas alternativas. Una expresión impone un construal particular sobre el contenido conceptual que evoca.

### 3.1 Especificidad (_Specificity_)

El nivel de **especificidad** (o su inversa, **esquematicidad**) es el grado de precisión y detalle con que se caracteriza una situación. También llamado **granularidad** o **resolución**.

- Expresiones con **mayor especificidad**: _hot_ > _warm_ > _tepid_ → todas instancian un esquema de temperatura aplicable.
- Las expresiones forman **jerarquías taxonómicas**: _thing_ → _creature_ → _animal_ → _mammal_ → _dog_ → _poodle_.
- Relación de **elaboración** (_elaboration_): A es esquemático para B si B es completamente compatible con las especificaciones de A pero las caracteriza con mayor precisión y detalle. Notación: A → B.
- La esquematicidad es relativa: una misma expresión puede ser esquemática respecto a unas y específica respecto a otras.

### 3.2 Foco (_Focusing_)

El foco incluye: (i) la **selección** de contenido conceptual para la presentación lingüística; (ii) la organización de **figura/fondo** (_figure/ground_); (iii) el **alcance** (_scope_).

#### Alcance (_Scope_)
- **Alcance máximo** (_maximal scope_, MS): la extensión completa del contenido evocado, los límites exteriores de la concepción relevante.
- **Alcance inmediato** (_immediate scope_, IS): la porción del contenido que es directamente relevante para el propósito particular, la región "onstage". Es el _locus_ del foco atencional y del _profiling_.
- El alcance inmediato está incluido en el máximo: IS ⊆ MS.
- El alcance tiene una dimensión temporal: el alcance temporal inmediato de un verbo perfectivo es el lapso durante el cual el evento se desarrolla.

#### Organización figura/fondo
Dentro de una escena, ciertos elementos se destacan como **figura** (más prominentes, foco primario) y otros como **fondo** (menos prominentes, contexto). Esta organización es ubicua y aplica en múltiples niveles.

#### Dado vs. nuevo, tópico, presuposición
- **Dado** (_given_) vs. **nuevo** (_new_): el estatus informativo relativo de los elementos en el discurso. Lo dado tiende a ser fondo; lo nuevo, figura.
- **Tópico** (_topic_): entidad respecto a la cual se organiza el discurso en un tramo.
- **Presuposición**: contenido que se asume como ya establecido o aceptado por los interlocutores.

### 3.3 Prominencia (_Prominence_)

La prominencia es la propiedad de ciertos elementos de ser más salientes cognoscitivamente que otros dentro de una misma escena. Múltiples tipos de prominencia coexisten y pueden no coincidir.

#### Profiling
Dentro de su base conceptual (la matriz de dominios evocada), una expresión impone un **perfil** (_profile_): la subestructura que **designa** o **refiere**. El perfil es la entidad que la expresión "nombra"; es el foco de atención específico dentro del contenido evocado.

- **Base**: el contenido conceptual respecto al cual se caracteriza el perfil. Es el alcance inmediato.
- **Perfil**: la entidad designada, el foco de atención. Lo que la expresión refiere (_designates_).

**Ejemplos con _hypotenuse_**:  
- Base: la concepción de un triángulo rectángulo.  
- Perfil: el lado opuesto al ángulo recto.  
- La palabra _hypotenuse_ evoca el triángulo como base pero no lo designa; designa solo el lado específico.

**Ejemplos con _elbow_**:  
- Base: la concepción del brazo humano (dominio: cuerpo).  
- Perfil: la articulación entre brazo superior y antebrazo.

**Ejemplos con _parent_**:  
- Base: red de relaciones de parentesco.  
- Perfil: un individuo en una relación de procreación o crianza respecto a otro.

Una expresión no puede entenderse sin evocar su base, pero lo que designa / refiere es solo su perfil.

#### Trajector y Landmark
Cuando el perfil es una **relación**, los participantes en ella tienen grados variables de prominencia:
- **Trajector** (_trajector_, tr): el participante **más prominente**, el que se está localizando, evaluando o describiendo. Es el foco **primario** en la relación perfilada. Corresponde aproximadamente a lo que otras teorías llaman "figura" dentro de la relación.
- **Landmark** (_landmark_, lm): el participante **secundario** en prominencia, el punto de referencia respecto al cual se sitúa el trajector. Corresponde al "fondo" relacional.

**Asimetría trajector/landmark**: `X is above Y` y `Y is below X` describen la misma configuración espacial pero difieren en cuál participante es el trajector. Lo mismo para `X resembles Y` vs. `Y resembles X` (aunque la diferencia semántica es sutil, existe).

**Alinear las mismas palabras en distinto orden** cambia el significado precisamente por la asimetría tr/lm: _the cat is on the mat_ ≠ _the mat is under the cat_.

#### Participantes focales en relaciones
- **Relación simplex** (atemporal, no-procesual): tiene un trajector y un landmark.
- **Relación compleja** (proceso): involucra múltiples estados componentes a lo largo del tiempo; el trajector y landmark pueden cambiar, y el proceso en sí tiene un perfil temporal.

Los términos **trajector** y **landmark** se aplican a todo tipo de relaciones, no solo espaciales. E.g. en _She loves him_, _she_ es el tr (el experimentante) y _him_ el lm (el objeto de la experiencia).

### 3.4 Perspectiva (_Perspective_)

#### Viewing arrangement (disposición de observación)
El **viewing arrangement** es la relación global entre el **conceptualizador** (_conceptualizer_) y la situación conceptualizada:

- **Default**: el conceptualizador (hablante/oyente) está fuera de la escena (_offstage_), es implícito, y observa la situación onstage desde una posición externa fija. Este es el **_optimal viewing arrangement_**.
- **Disposición egocéntrica**: el hablante es el origen por defecto del sistema de coordenadas.
- **Alternativas**: el conceptualizador puede adoptar otras posiciones de observación (_vantage points_) o incluso colocarse a sí mismo onstage como participante (e.g. _I_, _you_).

#### Vantage point (punto de observación)
El **vantage point** es la posición desde la cual se observa una escena. Puede ser:
- **Espacial**: _the clock is to the left of the door_ (desde el punto de vista del observador).
- **Temporal**: el tiempo de habla como punto de referencia temporal.
- **Epistémico**: la perspectiva del hablante respecto al estatus de realidad.

Cambiar el vantage point cambia el significado incluso si la situación descrita es idéntica: _X is to the left of Y_ vs. _X is to the right of Y_ (depende de la orientación del observador).

#### Subjetividad y objetividad
La distinción entre sujeto y objeto de concepción:
- **Sujeto de concepción** (_subject of conception_, S): el conceptualizador, el locus de la experiencia conceptual. En su rol de sujeto, S es **implícito** y **fuera de escena**. Construido con **máxima subjetividad** cuando funciona exclusivamente como sujeto (sin autoconciencia, absorto en aprehender O).
- **Objeto de concepción** (_object of conception_, O): la entidad onstage que es foco de atención. Construido con **máxima objetividad** cuando es claramente observado, bien delimitado respecto a su entorno y el observador.

Casos intermedios:
- Elementos como _I_ y _you_ colocan al hablante/oyente onstage como objeto de concepción (referente del pronombre) pero simultáneamente siguen siendo sujetos de concepción. Tienen un estatus dual que resulta en **subjetividad y objetividad atenuadas** respecto a los extremos.

#### Punto de referencia (_Reference point_)
Un **reference point** (R) es una entidad que proporciona acceso mental a otra entidad, el **target** (T). El conjunto de targets potenciales accesibles vía R es su **dominion** (D).

Propiedades:
- Relación **asimétrica**: R → T (direccionalidad inherente).
- **Dinámica**: involucra acceso mental secuencial.
- Encadenable: R → T₁ (= R₂) → T₂ ..., formando cadenas de puntos de referencia.
- Ubicuo en la cognición y el lenguaje:
  - **Posesión**: _Zelda's quilt_ (Zelda = R, quilt = T en el dominion de Zelda).
  - **Metonimia**: _Vietnam marcó un giro en la historia americana_ (Vietnam = R, la guerra = T).
  - **Tópico**: el tópico funciona como R que da acceso a elementos en su dominion.
  - **Anáfora pronominal**: el antecedente = R, el pronombre = T.

### 3.5 Evidencia para las afirmaciones semánticas

CG sostiene que las afirmaciones sobre significado deben estar empíricamente motivadas. Tipos de evidencia:
- **Introspección**: el lingüista como hablante nativo; acceso a juicios de contenido semántico.
- **Evidencia convergente**: corroboración entre distintos tipos de datos (distribucionales, diacrónicos, psicolingüísticos, translingüísticos).
- **Evidencia translingüística** (_cross-linguistic_): si una distinción semántica postulada se manifiesta gramaticalmente en múltiples lenguas no relacionadas, gana plausibilidad.
- **Evidencia experimental**: resultados de psicolingüística (tiempos de procesamiento, efectos de priming, etc.).
- **Evidencia diacrónica**: patrones de gramaticalización revelan la base conceptual de las categorías gramaticales (e.g. verbos de posesión → marcadores de aspecto perfecto).
