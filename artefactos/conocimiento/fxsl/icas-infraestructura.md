---
urn: urn:fxsl:kb:icas-infraestructura
nombre: icas-infraestructura
version: 1.1.0
estado: publicado
descripcion: "Pieza 20 del ICAS-BoK: modelos categoriales condicionales para infraestructura autónoma — tool use, self-improvement, IaC, reconciliación, self-healing y sistemas de sistemas."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/20-infraestructura-autonoma.md (sha256:b29c97fc95a73d9c2b11d52f0beedf38963d028dbe19f2d35f8aae7482214743) el 2026-06-12. Corrección 1.1.0 contrastada con Rutten, Universal Coalgebra, https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf."
autor: FS
creado: 2026-04-14
lang: es
tags: [IaC, reconciliation, self-healing, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Infraestructura autonoma

## Estatus

Las construcciones siguientes son modelos condicionales. Tool use no es
profunctor, un loop no es trace y una jerarquía no es 2-categoría solo por su
forma; cada lectura formal requiere categorías, acciones y leyes explícitas.

## La frontera donde el sistema se toca a si mismo

Hay un momento en la vida de todo sistema donde deja de ser operado y empieza a operarse a si mismo. Un reconciliation loop de Kubernetes que ajusta el estado real para igualar el estado deseado. Un agente que invoca una herramienta externa para resolver un sub-problema. Un enjambre de robots que redistribuye tareas cuando uno falla. Un pipeline de ML que reentrena su propio modelo cuando la distribucion de datos drifta.

Estos casos exigen modelar estado y reglas que también pueden cambiar. A veces
conviene usar categorías superiores; la auto-modificación operacional no obliga
a «subir de nivel categorial» ni queda libre de paradojas por adoptar ese
vocabulario.

## Tool use como morfismo externo

El uso de herramientas **puede modelarse** por un profunctor
`P : A^op x B -> Set` después de construir categorías de agentes y tools y
verificar las acciones contravariante/covariante. Una invocación ordinaria no
determina ese profunctor.

Un elemento de P(a, b) es una interaccion valida entre el agente a y la herramienta b. El profunctor captura todas las interacciones posibles -- todos los pares (agente, herramienta) que pueden conectarse, junto con las formas especificas en que pueden hacerlo. Si P(a, b) es vacio, el agente a no puede usar la herramienta b. Si P(a, b) tiene multiples elementos, hay multiples maneras de invocar la herramienta -- distintos modos de uso, distintos parametros, distintas interpretaciones del resultado.

Dentro de ese modelo, profuntores componibles se componen por el coend
`∫^b P(a,b) × Q(b,c)`. La fórmula identifica interacciones por la acción de
`B`; no demuestra que una cadena real de autorización o efectos sea transitiva.

El lema de Yoneda inspira directamente esta lectura: la herramienta puede tratarse externamente a traves de su interfaz. El agente no necesita entender los internos de la herramienta -- solo necesita conocer una interfaz suficientemente expresiva para componer con ella. Esta es la formalizacion de la opacidad que observo en la practica: un agente LLM que invoca una tool function no sabe como esta implementada, solo conoce su firma y su descripcion.

Elección, secuencia y paralelismo multi-tool requieren respectivamente
coproductos, composición y tensor **si** el modelo de interfaces los realiza.
Una jerarquía de delegación no es automáticamente una operad dinámica.

## Sistemas que se mejoran a si mismos

Un sistema auto-mejorante puede cambiar su espacio de capacidades o sus reglas.
Puede modelarse con una dinámica sobre presentaciones/categorías, pero no es por
ello un endo-2-funtor: habría que definir una 2-categoría y su acción sobre
0-, 1- y 2-celdas.

La distincion es sutil pero crucial. Un endofunctor ordinario actúa dentro de
una categoría fija y preserva identidades y composición. Puede identificar
morfismos distintos y no tiene por qué ser pleno, de modo que «no crea ni
destruye morfismos» es una lectura incorrecta. Un sistema auto-mejorante, en
cambio, puede cambiar la presentación, los objetos admitidos o la propia ley de
composición; entonces una sola categoría fija quizá ya no sea el dominio
adecuado.

Aguado, Rossi y Sanz capturan esta idea en su framework Sys-Self para robots autonomos: el robot usa un modelo formal de si mismo -- una representacion categorica de sus componentes, relaciones y capacidades -- y lo modifica en runtime cuando encuentra contingencias. La auto-conciencia del robot es la capacidad de razonar sobre su propio modelo categorico. La auto-mejora es la modificacion de ese modelo basada en la experiencia.

La convergencia de la auto-mejora es una pregunta dinámica. Un punto fijo
`E(C*) ≅ C*` no es automáticamente una coálgebra final. La finality exige una
propiedad universal: una única flecha coalgebraica desde toda `E`-coálgebra.
Tampoco significa «modelo óptimo»; optimalidad requiere un objetivo y un orden
o métrica separados.

La ausencia de punto fijo impide esa forma de estabilidad, pero la
convergencia de iteraciones depende además del espacio y de la dinámica. Un
argumento por contracción requiere una métrica completa y las hipótesis del
teorema de punto fijo correspondiente; es independiente de la finality
coalgebraica.

## Sistemas distribuidos como funtores sheaf-valued

Un sistema distribuido **puede modelarse** mediante un presheaf de estados
locales sobre un site que represente regiones y solapamientos. Los nodos y su
conectividad no constituyen automáticamente una topología ni una categoría de
abiertos.

En el modelo elegido, sea `Open` una categoría de regiones con inclusiones. Un
presheaf `F : Open^op -> C` asigna estados locales y mapas de restricción. Para
hablar de sheaf hace falta además una cobertura y una noción de familias
compatibles.

La condición de sheaf expresa existencia y unicidad de pegado para toda
cobertura del site. Puede representar una noción específica de consistencia
global cuando los estados y restricciones fueron diseñados para ello. No es
equivalente, sin esa semántica, a linearizability, serializability ni a
«consistencia fuerte» en general.

La consistencia eventual puede estudiarse con datos locales temporales, pero
sheafification es un reflector estático de presheaves a sheaves, no el límite
automático de Raft, Paxos o CRDTs. Modelar la convergencia exige una categoría
temporal y un diagrama concretos.

CAP es un resultado operacional sobre ejecuciones durante particiones. Un
equalizer, un objeto terminal o un site desconectado pueden aparecer en una
formalización concreta, pero asignarles respectivamente C, A y P no demuestra
CAP ni preserva por sí solo sus cuantificadores temporales. Aquí esa asociación
es, como máximo, una heurística para buscar un modelo posterior.

## Systems of Systems como 2-categorias

Un System of Systems (SoS) **puede** recibir un modelo 2-categorial si cada
constituyente se presenta como categoría, cada interfaz como funtor y cada
adaptación como transformación natural con los tipos y coherencias requeridos.
En ese modelo, los constituyentes son 0-celdas, las interfaces son 1-celdas y
las adaptaciones son 2-celdas. La composición horizontal y vertical tiene
entonces el significado impuesto por la 2-categoría; una adaptación operativa
arbitraria no hereda esas composiciones por el nombre.

Un colímite puede construir un sistema compuesto a partir de constituyentes e
interfaces. Que una propiedad emergente sea propiedad de ese colímite requiere
un observable o semántica adicional. La inexistencia del colímite en un modelo
elegido no demuestra que la emergencia física no ocurra.

La taxonomía Acknowledged/Collaborative/Virtual describe gobernanza y autonomía,
no determina una construcción 2-categorial. Composición estricta o lax y
coproductos son opciones de modelado solo después de definir interfaces,
2-celdas y sus leyes.

## Infraestructura autonoma: codigo declarativo y reconciliacion

Infrastructure-as-code **puede modelarse** mediante un funtor
`Deploy : Spec -> Runtime` si se definen ambas categorías y se demuestra
preservación de identidades y composición.

Un reconciliation loop tiene feedback operacional. Para llamarlo traced
morphism hay que definir una categoría monoidal trazada y demostrar sus axiomas;
el cable que vuelve atrás solo motiva el modelo.

Si `Observe . Deploy` y `Desired` son funtores paralelos bien definidos, una
transformación natural puede comparar sus imágenes. Un isomorfismo natural
expresa equivalencia dentro de esa semántica; no es sinónimo de convergencia
temporal ni de fidelidad física. El drift operativo debe medirse sobre estados
y tiempos concretos, aunque un cuadrado no conmutativo pueda representar una
clase de drift en el modelo.

El self-healing puede modelarse como transición recurrente. Que la supervisión
sea indefinida no la vuelve coinducción: coinducción es un principio de prueba
basado en una coálgebra/bisimulación concreta.

## Composition machines: auto-organizacion categorica

Arellanes propone las composition machines como un paradigma donde el software no se programa monoliticamente sino que emerge de la composicion auto-organizada de computones -- unidades atomicas de computacion. Una composition machine M = (D, F, Q, mu, S, N, delta) tiene un conjunto de tipos de datos D, un conjunto de computones F (funciones atomicas), un quiver Q que define la topologia de interaccion, funciones de asignacion mu, un conjunto de estados S, una estructura de vecindad N, y funciones de transicion local delta.

Lo notable de las composition machines es que el espacio de programas no se define a priori sino que emerge de las reglas locales de transicion. Cada computon tiene un estado (vivo o muerto). En cada paso temporal, los estados se actualizan segun las reglas delta que dependen de la vecindad. El espacio de programas en el tiempo t es la path category del quiver de computones vivos -- todas las composiciones secuenciales posibles en ese instante.

La evolucion temporal de la composition machine se describe por la iteración
de una función de actualización global `G` sobre configuraciones. Llamarla
funtor exige primero una categoría de configuraciones y comprobar su acción
sobre morfismos. La órbita `c, G(c), G(G(c)), ...` puede estabilizarse o hacerse
periódica; los ejemplos de Arellanes muestran, dentro de su formalismo, que
reglas locales simples pueden generar composiciones secuenciales no triviales.

Composition machines y operads dinámicas son formalismos distintos. Puede
buscarse un puente entre el quiver/categoría de caminos de Arellanes y la
estructura polynomial/coalgebraica de Shapiro-Spivak, pero identificar uno con
el otro requiere construir un funtor o una equivalencia que aquí no existe.

## La coherencia en todos los niveles

Estas manifestaciones sugieren una observación recursiva: algunos cambios que
afectan la propia estructura requieren un modelo de nivel superior. El grado
de autonomía no determina por sí solo una altura categorial.

Un sistema de transición puede generar una categoría de caminos; no «vive en
una categoría» solo por tener estados y pasos.

Un sistema que se opera a sí mismo puede admitir un modelo
especificación-ejecución; llamarlo funtor exige definir su acción y leyes.

Un sistema que modifica su lenguaje de capacidades puede modelarse mediante
una dinámica entre categorías o presentaciones. Un 2-funtor es una opción solo
si se define la 2-categoría pertinente y se preservan sus composiciones e
identidades; cambiar reglas no basta para producirlo.

Un System of Systems puede estudiarse en clave 2-categorial si sus
constituyentes, interfaces y adaptaciones realizan esos tipos. Un 2-colímite
compone un diagrama; no es por definición «la emergencia».

Y una composition machine vive en la frontera: su estructura de composicion
cambia en cada paso temporal, pero las reglas de cambio son fijas. La
diferencia entre auto-organización y auto-mejora puede modelarse, según el
caso, como dinámica dentro de una estructura fija frente a dinámica que
también cambia esa estructura. «Endofuntor frente a nivel superior» es una
hipótesis que todavía debe tiparse.

En la práctica, esta jerarquía ofrece hipótesis de modelado: funtores para
pipelines, traces para controladores, profuntores para interfaces de tools y
2-categorías para sistemas que cambian su arquitectura. Cada hipótesis debe
ganarse por tipado y leyes; la autonomía no eleva por sí sola el «nivel
categorial».

## Corrección 1.1.0

Se separan punto fijo, coálgebra final y óptimo; se retira la identificación de
consenso dinámico con sheafification y se condicionan las lecturas
IaC=funtor, reconciliation=trace y bucle infinito=coinducción.
