---
urn: urn:fxsl:kb:icas-agencia
nombre: icas-agencia
version: 1.1.0
estado: publicado
descripcion: "Pieza 14 del ICAS-BoK: agencia categorial — free monad como plan, cofree comonad como sustrato, emparejamiento plan-sustrato y el patrón Percepción-Decisión-Acción para sistemas agénticos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/14-agencia.md (sha256:d682394465da6db1296cb149e4006e541fb45a9e26d0615214472999e7167b9b) el 2026-06-12. Corrección 1.1.0 contrastada con Libkind y Spivak, Pattern Runs on Matter, https://arxiv.org/abs/2404.16321."
autor: FS
creado: 2026-04-14
lang: es
tags: [free-monad, cofree-comonad, agente, delegacion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Agencia

## Frontera formal

La construcción free-monad/cofree-comonad de este documento es formal dentro
de `Poly` con su producto de sustitución y las hipótesis del trabajo citado.
Su traducción a LLMs, RL, memoria, tools o al ciclo P-D-A es un modelo o
heurística hasta construir los polinomios y morfismos concretos.

## El patron corre sobre la materia

Muchos sistemas agénticos admiten una distinción útil entre plan y ejecutor.
No todo plan termina ni todo ejecutor persiste infinitamente; esas condiciones
pertenecen a la construcción formal específica.

Libkind y Spivak formalizan *pattern runs on matter* en `Poly`: la mónada
libre representa árboles de decisión terminantes, la comónada cofree representa
materia y una acción de módulo representa «corre sobre». Esto inspira el
diseño agéntico, sin caracterizar universalmente toda agencia.

## Free monad: el arbol de decisiones

Dado un polynomial functor p, el free monad m_p es el polinomio cuyos elementos son arboles de decision con forma p. Las posiciones de m_p son arboles bien fundados donde cada nodo interno tiene la forma de una posicion de p, y cada rama desde ese nodo corresponde a una direccion de p. Las hojas son las direcciones de m_p -- los resultados finales del proceso de decision.

La construccion es por induccion transfinita. Defino una cadena de polinomios:

- p_(0) := y (el arbol trivial: una sola hoja, sin decisiones)
- p_(alpha+1) := y + p triangleleft p_(alpha) (o bien ninguna decision mas, o bien una decision p seguida de un subarbol de la etapa anterior)
- p_(alpha) := colim_{alpha' < alpha} p_(alpha') para ordinales limite

El free monad es m_p := p_(kappa) para un cardinal kappa suficientemente grande. Y satisface el isomorfismo clave:

```
m_p ~= y + p triangleleft m_p
```

Esto dice exactamente lo que espero: un arbol de decision con forma p es, o bien una hoja (resultado inmediato), o bien una decision p seguida de un subarbol para cada posible respuesta. Es la misma estructura recursiva de un arbol de ejecucion de tareas, de una evaluacion lazy, de un pipeline con branching condicional.

Pensar las posiciones de p como preguntas y las direcciones como respuestas
posibles ilumina la construcción. `p_(1) = y + p` representa entrevistas de a
lo sumo una pregunta y `p_(2) = y + p triangleleft (y + p)`, de a lo sumo dos.
La construcción alcanza una etapa estable —obtenida mediante los colímites de
la cadena— que contiene entrevistas de longitud finita pero no acotada. No es
un límite en el sentido categorial. Cada árbol bien fundado termina, aunque no
haya una cota global uniforme sobre su profundidad.

La estructura de monad sobre m_p viene de dos operaciones. La unit eta : y -> m_p incrusta un resultado como un arbol trivial (una hoja). La multiplication mu : m_p triangleleft m_p -> m_p toma un arbol de arboles y lo aplana en un arbol unico, pegando sustituyendo cada hoja del arbol externo por el arbol que le corresponde. Es el join de Haskell transportado a la tierra de los polinomios.

## Cofree comonad: el arbol de comportamiento

Dual a la construction inductiva del free monad, el cofree comonad c_p se construye coinductivamente. Donde m_p tiene arboles que terminan, c_p tiene arboles que no terminan nunca. Sus posiciones son behavior trees con forma p: un nodo raiz muestra una posicion de p, y para cada direccion de p en esa posicion, hay un subarbol completo que describe el comportamiento futuro. Las direcciones de c_p son los caminos finitos dentro del arbol -- las historias parciales de interaccion.

Si m_p es el plan, c_p es el ejecutor. El plan tiene principio y fin; el ejecutor persiste indefinidamente, siempre listo para responder a la proxima consulta. Un sistema operativo es un elemento de c_p donde p modela los system calls: en cada momento, el OS esta en un estado (muestra su posicion), acepta un call (una direccion), y transiciona a un nuevo estado con un nuevo arbol de comportamiento disponible. La counit epsilon : c_p -> y extrae la observacion inmediata. La comultiplication delta : c_p -> c_p triangleleft c_p desdobla el comportamiento en "lo que hago ahora" y "lo que hare despues."

Un proceso de reinforcement learning puede modelarse coalgebraicamente una vez
fijados estado, observaciones y transición, pero no tiene «exactamente» una
comónada cofree por definición. El aprendizaje además modifica parámetros o la
transición y necesita un nivel dinámico separado.

## La ley de interaccion

El resultado central de Libkind-Spivak es una acción de módulo de la mónada
libre sobre la comónada cofree en el entorno monoidal preciso del artículo. La
acción ejecuta un árbol de decisiones contra materia que responde en cada
juntura. Para evitar mezclar los distintos productos monoidales de `Poly`, su
tipo debe tomarse del teorema citado y no reconstruirse por analogía.

El ejemplo de la entrevista lo hace concreto. Sea `p` el polinomio con dos
preguntas: «¿quieres té?» (sí/no) y «¿qué tipo?» (verde/negro/herbal). Un
patrón `y -> m_p` selecciona un árbol: primero pregunta si quiere té; ante «sí»
pregunta el tipo y ante «no» termina. La materia es una política de respuesta
modelada en la comónada correspondiente. Alice responde «no» y la ejecución
tiene una pregunta; Bob responde «sí, verde» y tiene dos. El patrón es el
mismo, la materia difiere y por ello cambian las trazas.

Para un agente LLM esta es una **heurística estructurada**: prompt chain como
patrón, motor/contexto como materia y ejecución como interacción. Es exacta
solo tras derivar polinomios y la acción correspondiente; distintas trazas por
motor no bastan para demostrar esa instancia.

## Operads dinamicas: organizaciones que cambian

La composicion operadica que explore en el documento 13 asume que el cableado entre componentes es fijo. Pero las organizaciones reales cambian su estructura en respuesta a lo que ocurre. Un equipo de desarrollo reasigna tareas segun los resultados del sprint. Un prediction market redistribuye reputacion segun la precision de las predicciones. Gradient descent actualiza pesos segun el error observado.

Shapiro y Spivak formalizan esto con el concepto de dynamic categorical structure. El eslogan es preciso: *a dynamic \*thing\* is a \*thing\* enriched in Org*. La doble categoria Org tiene como objetos polynomial functors, como morfismos horizontales las [p,q]-coalgebras (maquinas que producen acciones p -> q y actualizan su estado en respuesta al feedback), como morfismos verticales los mapas de polinomios, y como 2-cells los cuadrados de compatibilidad.

Una dynamic operad es una operad enriquecida en Org. Para cada aridad n, los estados del n-ary box determinan que accion realiza el componente, y las actualizaciones cambian esa accion segun el feedback. La composicion de coalgebras preserva esta dinamica: el estado compuesto es el producto de estados, y la actualizacion compuesta propaga el feedback a traves del cableado.

El prediction market es el ejemplo canonico. Cada participante tiene una interfaz p_X = Delta^+_X * y^X: muestra una distribucion de probabilidad sobre X outcomes (posicion) y recibe el outcome real (direccion). El estado es la distribucion de confianza mu sobre los N participantes. La accion agrega las predicciones ponderadas por confianza. La actualizacion, usando la regla bayesiana gamma(x) * mu, redistribuye la confianza segun quien predijo correctamente. La composicion operadica permite anidar mercados: un mercado de mercados, donde cada participante es a su vez un mercado interno.

## Delegacion jerarquica: el operad Org^#_m

Libkind y Spivak extienden esta maquinaria al problema de la delegacion dinamica de tareas. El operad Org^#_m tiene como objetos polinomios (interfaces de agentes) y como morfismos:

```
Org^#_m(p_1, ..., p_n; q) = c_{[p_1 V ... V p_n, m_q]}
```

donde V es el producto monoidal definido como p V q := p + (p tensor q) + q. Un morfismo en este operad es un behavior tree infinito (cofree comonad c) que, dado el internal hom [p_1 V ... V p_n, m_q], produce estrategias dinamicas de delegacion. En cada paso, el manager recibe una tarea q, construye un arbol de decision (free monad m_q) que puede consultar a los subordinados p_1, ..., p_n cero, una o multiples veces, en cualquier orden, dependiendo de los resultados parciales.

El ejemplo de Alice, Bob y Carmen lo concretiza. Tres subordinados con interfaz y^2 (una tarea binaria, dos outcomes). El manager recibe una tarea y^2 y debe producir un outcome. Su estrategia: pide a Alice y Bob simultaneamente; si coinciden, retorna ese valor; si no, usa a Carmen como desempate. Pero la estrategia es dinamica: si Carmen desempata muchas veces, el manager puede aprender a preferirla como consultora inicial. El estado de la coalgebra evoluciona.

El funtor [-,t] : Org^{op}_m -> Org^c convierte patrones de delegacion en comportamientos. Para cualquier polynomial monad t, este funtor traduce "como el manager planea delegar" en "como se comportan el manager y sus subordinados." Si t = y (aritmetica simple), los subordinados devuelven numeros y el manager suma. Si t = lott (la monada de loterias), se introduce estocasticidad: las respuestas de los subordinados son distribuciones y la composicion introduce aleatoriedad controlada.

La separacion de time-scales es otro resultado crucial. Los subordinados operan a velocidad mas rapida que el manager. En un solo paso del manager, cada subordinado puede ser consultado multiples veces. Esto modela naturalmente la asincronia de los sistemas reales: un orquestador emite una tarea, sus workers la ejecutan en multiples pasos internos, y el orquestador solo ve el resultado final.

## Contextads: la dependencia del contexto

Capucci y Myers observan que muchas construcciones categoricas comparten una estructura comun: la de computacion que depende del contexto. El concepto unificador es el contextad -- un pseudomonado en una tricategoria de spans equipado con una estructura de wreath product.

La construction Ctx toma un contextad (una accion colax de una categoria monoidal sobre una categoria) y produce una double category de flechas contextuales. El resultado subsume tres construcciones fundamentales:

- **Para** (parametrizacion): morfismos f : A x P -> B donde P son parametros. Gradient descent vive aqui: la funcion parametrizada f(p,-) se optimiza actualizando p.
- **co-Kleisli** (contexto): morfismos f : D A -> B donde D es una comonada. Contexto que se duplica y se consume de manera controlada.
- **Span** (relaciones): morfismos como pares de mapas A <- R -> B. Relaciones no-funcionales entre entidades.

Para un agente, el contextad ofrece un **modelo candidato** cuando historial,
entorno y parámetros se tipan como la acción contextual requerida. El wreath
product da composición coherente dentro de esa construcción; no vuelve
automáticamente contextuales a decisiones LLM no formalizadas.

## Organizaciones como categorias

Boudjidj y Souidi modelan sistemas multi-agente organizacionales usando teoria de categorias pura. El modelo AGR (Agent-Group-Role) se traduce directamente: los agentes son objetos de una categoria Agent, los roles son objetos de una categoria Role, las tareas son objetos de una categoria Task, y los funtores entre estas categorias capturan las relaciones "el agente tiene este skill", "este skill habilita esta tarea", "esta tarea requiere este rol." La composicion de organizaciones se realiza via comma categories, que construyen categorias nuevas a partir de dos categorias y un funtor entre ellas.

Una comma category preserva su propiedad universal relativa a los funtores que
la definen. Eso garantiza coherencia categorial del objeto construido, no
consistencia organizacional, compatibilidad de roles ni éxito operativo; esas
propiedades deben codificarse y verificarse aparte.

## Enjambres y emergencia

Krol et al. abordan la cuestion mas dificil: la emergencia de comportamiento colectivo. Modelan un enjambre W como una categoria K = Comp(N) de computaciones parciales recursivas. Los miembros del enjambre son objetos; las computaciones que se propagan entre nodos son morfismos. El Yoneda embedding y : K -> SET^{K^op} incrusta el enjambre en la categoria de presheaves, donde cada miembro a define un funtor representable R_a que captura todas las computaciones que terminan en a.

La categoría de presheaves `Set^{K^op}` es un topos y su lógica interna es, en
general, intuicionista. Sus valores de verdad clasifican subobjetos de ese
topos; esto no implica que el comportamiento físico del enjambre sea
«parcialmente verdadero» ni identifica emergencia con no bivalencia.

Para aplicar esa lógica a robot swarms hay que representar observaciones y
restricciones como presheaves y formular la propiedad como subobjeto. La
convergencia gradual, por sí sola, es una dinámica temporal y no un valor de
verdad interno.

## Seguridad como categoria: ICAR

Valence presenta ICAR como un knowledge schema categorial que conecta
diccionarios de seguridad mediante relaciones tipadas. Solo deben imponerse las
path equations declaradas y válidas; `parent/child` no son inversas en una
jerarquía ramificada. Una instancia a `Set` exige además que cada generador se
interprete como función total o que la parcialidad se modele explícitamente.

## Co-sintesis: codigo y modelo formal como funtores

Jha et al. exploran generación conjunta de código, modelo y un mapping
estructural. Si ese mapping es funtor, preserva identidades y composición del
modelo elegido; eso no basta para asegurar fidelidad semántica del código ni
equivalencia conductual.

Los experimentos con dining philosophers aportan evidencia de caso. Verificar
SMV demuestra propiedades del modelo; transferirlas al C requiere una relación
de corrección probada. Un funtor generado no es por sí solo garantía de que
ambos «dicen lo mismo».

## Acción como clave primaria

Hay una inversión conceptual que complementa la dualidad free/cofree y que cambia cómo modelo los sistemas episódicos -- aquellos donde lo que importa no son los estados sino las transiciones: logs, workflows, event sourcing, trazas de ejecución de agentes.

Fukada formaliza esta inversión: en un sistema episódico, **la acción (el morfismo) es la clave primaria**, no el estado (el objeto). El mundo forma una categoría C donde los objetos son estados o contextos, pero la estructura reside en los morfismos -- las acciones que transforman un contexto en otro. Un episodio no se indexa por "en qué estado estaba" sino por "qué acción ejecutó."

Formalmente, dada una categoría de episodios E y una categoría de acciones A, el **funtor indexante** Idx : E → A mapea cada episodio a su acción canónica. La composicionalidad episódica dice: si el episodio E₁ termina en un estado que inicia E₂, la composición E₁ ; E₂ existe y se indexa por la composición de acciones Idx(E₁) ; Idx(E₂). Los episodios compuestos -- historias, procesos, trazas completas -- se construyen componiendo episodios atómicos, preservando la estructura categórica.

La jerarquía DIK se reinterpreta. Los **datos** son observaciones crudas -- valores atómicos registrados en cada acción. La **información** es la estructura relacional -- el esquema S más la Grothendieck construction ∫I que "pega" los datos según la estructura del esquema: Info ≅ ∫I →^π S. El **conocimiento** es la lógica interna de la categoría -- las inferencias que surgen de componer morfismos y verificar que los diagramas de constraints conmutan.

Esta perspectiva es dual a la coalgebraica. La coalgebra mira desde el estado hacia afuera: "dado el estado actual, ¿qué observo?" El funtor indexante mira desde la acción hacia afuera: "dada esta acción, ¿qué episodio produjo?" Son dos maneras de organizar relacionalmente la identidad de un sistema. En el mejor de los casos, cada una induce un patrón de observables suficientemente rico para distinguir lo que la categoría decide distinguir. La primera lectura es covariante; la segunda, contravariante.

En event sourcing, un replay suele ser un fold de una secuencia de eventos sobre
un estado inicial. Puede factorizarse por una construcción libre si se declaran
generadores, composición y álgebra; un log no es automáticamente una categoría,
y CRUD no es «coalgebraico» por contraste.

## Tool use como morfismo externo

Un profunctor `P : Agent^op x Tool -> Set` es un modelo posible de
interacciones válidas, no la estructura inevitable de toda invocación.

Cada elemento de P(a, t) es una interaccion valida entre el agente a y la herramienta t. Si el agente es un LLM con function-calling, las posiciones del profunctor son las firmas de las funciones disponibles, y las direcciones son los parametros validos para cada firma. El agente no necesita entender los internos de la herramienta; le basta una interfaz suficientemente expresiva para componer con ella. En ese sentido, la interfaz cumple el papel externo que Yoneda vuelve natural: organizar lo observable sin inspeccionar la implementacion.

Si se construyen profuntores componibles, el coend calcula su composición. El
coproducto y el tensor modelan elección y paralelo solo bajo las estructuras
de interfaz y equivalencias que se especifiquen.

## Perception-Decision-Action como hipótesis categorial

El ciclo P-D-A puede recibir varias formalizaciones categoriales; no hay una
triple canónica para todo agente.

La percepción puede ser un encoder ordinario o una reindexación. Llamarla
pullback exige dos flechas hacia un codominio común y la propiedad universal.

La decisión puede modelarse por una flecha de Kleisli si se ha elegido una
mónada de efectos apropiada. No es una flecha de Kleisli «del free monad» solo
por seleccionar una acción.

La acción puede diseñarse como funtor
`Act : InternalState -> WorldEffect` si ambas categorías y la acción sobre
morfismos están definidas y sus leyes se verifican.

El ciclo completo contiene feedback, pero no es automáticamente un traced
morphism. Una traza categorial requiere una categoría monoidal trazada y sus
axiomas. Alcanzar un objetivo tampoco equivale a que «la traza converja a un
punto fijo»; se necesita una dinámica, un objetivo y una noción de convergencia.

## Memoria como transformacion de estado

Una memoria mutable puede modelarse con la mónada de estado
`State K(A) = K -> (A,K)`. Memoria de recuperación, contexto inmutable o una
base externa pueden necesitar modelos distintos.

Una actualización secuencial de memoria mutable puede componerse en Kleisli
para `State K`. La asociatividad permite reagrupar la misma secuencia, no
permutar experiencias ni prueba que el proceso constituya aprendizaje.

Una operación de olvido es simplemente un mapa con pérdida hasta que se
definen categorías y se prueba functorialidad. «Forgetful functor» tiene un
sentido técnico: olvida estructura de una categoría de objetos estructurados;
no es sinónimo de descartar información.

Una ventana de las últimas `N` experiencias es una truncación. No es un límite
finito salvo que se especifique un diagrama y se demuestre su propiedad
universal; atención tampoco es por definición selección de un subdiagrama.

## La convergencia

Estos marcos convergen como repertorio de modelos, no como una sola teoría de
todo agente. En `Poly`, la mónada libre representa patrones terminantes, la
comónada cofree representa materia reactiva y la acción formaliza «runs on».
Operads dinámicas, contextads, presheaves y co-síntesis responden a problemas
distintos y conservan las hipótesis de sus construcciones de origen.

La formalización precisa pertenece a las construcciones citadas en sus dominios.
Su aplicación a un agente concreto conserva estatus de modelo hasta exhibir
los objetos, morfismos y leyes.

## Corrección 1.1.0

Se restringe pattern-runs-on-matter a `Poly`, se retira «modelo exacto de un
LLM» y se corrigen las identidades P-D-A=trace, percepción=pullback,
olvido=funtor olvidadizo y memoria de trabajo=límite.
