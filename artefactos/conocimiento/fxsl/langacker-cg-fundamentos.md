---
urn: urn:fxsl:kb:langacker-cg-fundamentos
nombre: langacker-cg-fundamentos
version: 1.0.0
estado: publicado
descripcion: "Fundamentos de Cognitive Grammar (Parte I, caps. 1-3): la tesis de la gramática como simbolización, semántica conceptual (significado como conceptualización, visión enciclopédica, dominios, ICMs) y construal (especificidad, foco, prominencia —profiling, trajector/landmark— y perspectiva —viewing arrangement, vantage point, subjetividad/objetividad, punto de referencia—)."
fuente: "Langacker, Ronald W. (2008). Cognitive Grammar: A Basic Introduction. Oxford University Press. Archivo fuente: /home/felix/kora-external-sources/Cognitive Grammar_ A Basic Introduction - Ronald W. Langacker.txt (sha256:6370e8b08fdaaf1ebc2a05db7a4b0db553cf9384a58bb7532f3a0f037838707f). Alcance: Part I (Preliminaries), caps. 1-3 (pp. 3-90 del libro; líneas 182-1199 del archivo). Descartado: prefacio, contenidos, front matter, referencias e índice. Los caps. 4-14 se korifican en artefactos hermanos (langacker-cg-clases-y-construcciones, langacker-cg-estructuras, langacker-cg-fronteras)."
autor: FS
creado: 2026-06-29
lang: es
tags: [cognitive-grammar, langacker, linguistica-cognitiva, gramatica, simbolizacion, semantica-conceptual, construal, profiling, trajector-landmark, perspectiva, subjetividad]
familia: bok
---

# Fundamentos de Cognitive Grammar

## 1. La tesis central: la gramática es simbólica

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

En **semántica cognitiva**, el significado se identifica con la **conceptualización** asociada a las expresiones lingüísticas. Esto es contraintuitivo para la doctrina estándar (que lo rechaza como insular o no-empírico), pero la conceptualización está anclada en la realidad física (actividad cerebral, cuerpo, mundo) y en la interacción social (negociada entre interlocutores).

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

El **construal** es la capacidad de concebir y retratar la misma situación de formas alternativas. Una expresión impone un construal particular sobre el contenido conceptual que evoca. Es la dimensión central de la organización semántica: dos expresiones pueden evocar el mismo contenido pero diferir en significado por cómo lo construyen.

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
