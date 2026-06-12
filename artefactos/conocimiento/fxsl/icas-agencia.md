---
urn: urn:fxsl:kb:icas-agencia
nombre: icas-agencia
version: 1.0.0
estado: publicado
descripcion: "Pieza 14 del ICAS-BoK: agencia categorial — free monad como plan, cofree comonad como sustrato, emparejamiento plan-sustrato y el patrón Percepción-Decisión-Acción para sistemas agénticos."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/14-agencia.md (sha256:d682394465da6db1296cb149e4006e541fb45a9e26d0615214472999e7167b9b) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl."
autor: FS
creado: 2026-04-14
lang: es
tags: [free-monad, cofree-comonad, agente, delegacion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Agencia

## El patron corre sobre la materia

Todo sistema agentico que he construido tiene la misma estructura secreta: hay un plan y hay algo que ejecuta el plan. Un prompt chain que corre sobre un motor de inferencia. Un DAG de tareas que corre sobre un cluster de workers. Un protocolo de votacion que corre sobre electores. Un juego que corre sobre jugadores. En cada caso, el plan tiene forma de arbol de decisiones finito -- ramifica, elige, termina. El ejecutor tiene forma de arbol de comportamiento infinito -- responde, persiste, nunca se destruye.

Libkind y Spivak cristalizan esta intuicion en una frase que se ha vuelto para mi un axioma de diseno: *pattern runs on matter*. Los patrones empiezan y terminan; la materia nunca se destruye. Los programas corren sobre sistemas operativos. Las entrevistas corren sobre personas. Los esquemas de votacion corren sobre votantes. Los juegos corren sobre jugadores. La estructura matematica que captura esta dualidad vive en Poly, la categoria de polynomial functors que ya explore en documentos anteriores. Pero ahora Poly revela su cara mas profunda: la de un universo donde monadas y comonadas interactuan para producir agencia.

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

Pensar las posiciones de p como preguntas y las direcciones como respuestas posibles ilumina la construccion. El polinomio p_(1) = y + p representa entrevistas de a lo sumo una pregunta. El polinomio p_(2) = y + p triangleleft (y + p) representa entrevistas de a lo sumo dos preguntas. Y m_p es el limite: entrevistas de longitud finita pero no acotada. Cada arbol en m_p termina eventualmente -- es well-founded -- pero no hay cota global sobre cuantas preguntas puede hacer.

La estructura de monad sobre m_p viene de dos operaciones. La unit eta : y -> m_p incrusta un resultado como un arbol trivial (una hoja). La multiplication mu : m_p triangleleft m_p -> m_p toma un arbol de arboles y lo aplana en un arbol unico, pegando sustituyendo cada hoja del arbol externo por el arbol que le corresponde. Es el join de Haskell transportado a la tierra de los polinomios.

## Cofree comonad: el arbol de comportamiento

Dual a la construction inductiva del free monad, el cofree comonad c_p se construye coinductivamente. Donde m_p tiene arboles que terminan, c_p tiene arboles que no terminan nunca. Sus posiciones son behavior trees con forma p: un nodo raiz muestra una posicion de p, y para cada direccion de p en esa posicion, hay un subarbol completo que describe el comportamiento futuro. Las direcciones de c_p son los caminos finitos dentro del arbol -- las historias parciales de interaccion.

Si m_p es el plan, c_p es el ejecutor. El plan tiene principio y fin; el ejecutor persiste indefinidamente, siempre listo para responder a la proxima consulta. Un sistema operativo es un elemento de c_p donde p modela los system calls: en cada momento, el OS esta en un estado (muestra su posicion), acepta un call (una direccion), y transiciona a un nuevo estado con un nuevo arbol de comportamiento disponible. La counit epsilon : c_p -> y extrae la observacion inmediata. La comultiplication delta : c_p -> c_p triangleleft c_p desdobla el comportamiento en "lo que hago ahora" y "lo que hare despues."

En reinforcement learning, el agente que aprende tiene exactamente esta estructura comonadica. Su estado es un behavior tree: dado el estado actual, elige una accion (posicion), recibe un reward y una observacion (direccion), y transiciona a un nuevo behavior tree. El aprendizaje es la actualizacion de la coalgebra -- el mismo polinomio p, pero una funcion de transicion distinta que refleja la experiencia acumulada.

## La ley de interaccion

El resultado central de Libkind-Spivak es que m_p es un modulo sobre c_p. La ley de interaccion es una transformacion natural:

```
Xi_{p,q} : m_p tensor c_q -> m_{p tensor q}
```

Dado un patron (un arbol de decision en m_p) y materia (un arbol de comportamiento en c_q), la interaccion produce un arbol de decision en m_{p tensor q}. El patron consume la materia: en cada nodo de decision del patron, el patron consulta a la materia, la materia responde con una direccion, y el patron usa esa respuesta para elegir su siguiente rama. El arbol resultante tiene la forma combinada de patron y materia.

El ejemplo de la entrevista lo hace concreto. Sea p el polinomio con dos preguntas: "quieres te?" (si/no) y "que tipo?" (verde/negro/herbal). Un patron y -> m_p selecciona un arbol de entrevista especifico: primero pregunta "quieres te?", si la respuesta es "si" entonces pregunta "que tipo?", si es "no" termina. La materia es una persona -- un elemento de c_{[p,y]}, un behavior tree que para cada pregunta tiene una respuesta. Alice, que no quiere te, genera una ejecucion de dos preguntas. Bob, que primero dice que no pero luego cambia de opinion, genera una ejecucion de tres preguntas. El patron es el mismo; la materia es diferente; las ejecuciones difieren.

Este es el modelo exacto de un agente LLM: el prompt chain es el patron m_p, el motor de inferencia es la materia c_q, y la interaccion Xi produce la traza de ejecucion. Dos instancias del mismo chain sobre motores diferentes (GPT-4, Claude, Llama) producen trazas diferentes porque la materia es diferente. El patron estructura; la materia responde.

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

Para un agente, la relevancia es directa. Toda decision agentica depende del contexto: el historial de interacciones, el estado del entorno, los parametros aprendidos. Un contextad captura esta dependencia como estructura de primera clase, no como un hack ad hoc. La composicion de decisiones contextuales es automaticamente contextual -- el wreath product asegura que los contextos se componen coherentemente.

## Organizaciones como categorias

Boudjidj y Souidi modelan sistemas multi-agente organizacionales usando teoria de categorias pura. El modelo AGR (Agent-Group-Role) se traduce directamente: los agentes son objetos de una categoria Agent, los roles son objetos de una categoria Role, las tareas son objetos de una categoria Task, y los funtores entre estas categorias capturan las relaciones "el agente tiene este skill", "este skill habilita esta tarea", "esta tarea requiere este rol." La composicion de organizaciones se realiza via comma categories, que construyen categorias nuevas a partir de dos categorias y un funtor entre ellas.

Lo que este enfoque revela es que la composicion organizacional preserva estructura por construccion. Si dos organizaciones se integran via un funtor comun (un mapeo de roles compartidos, por ejemplo), la comma category resultante hereda las propiedades composicionales de las categorias originales. No necesito verificar post hoc que la integracion es consistente; la construccion categorica lo garantiza.

## Enjambres y emergencia

Krol et al. abordan la cuestion mas dificil: la emergencia de comportamiento colectivo. Modelan un enjambre W como una categoria K = Comp(N) de computaciones parciales recursivas. Los miembros del enjambre son objetos; las computaciones que se propagan entre nodos son morfismos. El Yoneda embedding y : K -> SET^{K^op} incrusta el enjambre en la categoria de presheaves, donde cada miembro a define un funtor representable R_a que captura todas las computaciones que terminan en a.

El punto fundamental es que la categoria de presheaves SET^{K^op} es un topos. Y la logica interna de un topos es intuicionistica, no clasica. Esto significa que el comportamiento emergente del enjambre -- las propiedades que existen en el presheaf category pero no en la categoria base -- obedece una logica donde el tercero excluido no vale. Un enjambre puede exhibir un comportamiento que no es ni definitivamente presente ni definitivamente ausente. La emergencia vive en el espacio entre verdadero y falso, en el subobject classifier de Heyting que reemplaza al booleano clasico.

Para robot swarms, esta logica no-clasica captura la realidad operativa: el enjambre converge gradualmente, las propiedades emergentes se estabilizan progresivamente, y hay un periodo donde una propiedad esta "parcialmente presente" -- exactamente el valor de verdad de un subpresheaf que no es ni el total ni el vacio.

## Seguridad como categoria: ICAR

Valence muestra que los silos de la ciberseguridad -- vulnerabilidades (CVE), debilidades (CWE), patrones de ataque (CAPEC), tecnicas (ATT&CK), activos (CPE) -- se integran como un knowledge schema categorico. ICAR (Integrated CAtegorical Resource) es una categoria cuyos objetos son los diccionarios de seguridad, cuyos morfismos son las relaciones entre ellos (Has, isChildOf, isParentOf, accomplishesTactic), y cuyos path equivalences capturan las restricciones semanticas (isChildOf.isParentOf = id). Una instancia de ICAR es un funtor F : S -> Set que asigna a cada diccionario su conjunto de entradas y a cada relacion las funciones correspondientes. El documento 18 desarrolla ICAR con queries operativas, conteos concretos y su conexion con el analisis de riesgo.

## Co-sintesis: codigo y modelo formal como funtores

Jha et al. cierran el circulo con un resultado que me parece profundamente practico: un LLM puede generar simultaneamente codigo ejecutable, un modelo formal verificable, y un funtor entre ambos. El funtor mapea objetos del codigo (threads, mutexes, funciones) a objetos del modelo (procesos, variables booleanas, transiciones), y la propiedad de preservar composicion asegura que la estructura del codigo se refleja fielmente en la estructura del modelo.

Los experimentos con el dining philosophers problem son ilustrativos. Los LLMs mas capaces generan en una sola iteracion el codigo C, el modelo SMV, y el funtor asociativo que permite verificar propiedades temporales del codigo a traves del modelo. Modelos menos capaces requieren multiples iteraciones o no convergen sin intervencion humana significativa. El funtor es el puente que falta en la verificacion formal tradicional: no solo genero codigo y especificacion por separado, sino que genero la garantia estructural de que ambos dicen lo mismo.

## Acción como clave primaria

Hay una inversión conceptual que complementa la dualidad free/cofree y que cambia cómo modelo los sistemas episódicos -- aquellos donde lo que importa no son los estados sino las transiciones: logs, workflows, event sourcing, trazas de ejecución de agentes.

Fukada formaliza esta inversión: en un sistema episódico, **la acción (el morfismo) es la clave primaria**, no el estado (el objeto). El mundo forma una categoría C donde los objetos son estados o contextos, pero la estructura reside en los morfismos -- las acciones que transforman un contexto en otro. Un episodio no se indexa por "en qué estado estaba" sino por "qué acción ejecutó."

Formalmente, dada una categoría de episodios E y una categoría de acciones A, el **funtor indexante** Idx : E → A mapea cada episodio a su acción canónica. La composicionalidad episódica dice: si el episodio E₁ termina en un estado que inicia E₂, la composición E₁ ; E₂ existe y se indexa por la composición de acciones Idx(E₁) ; Idx(E₂). Los episodios compuestos -- historias, procesos, trazas completas -- se construyen componiendo episodios atómicos, preservando la estructura categórica.

La jerarquía DIK se reinterpreta. Los **datos** son observaciones crudas -- valores atómicos registrados en cada acción. La **información** es la estructura relacional -- el esquema S más la Grothendieck construction ∫I que "pega" los datos según la estructura del esquema: Info ≅ ∫I →^π S. El **conocimiento** es la lógica interna de la categoría -- las inferencias que surgen de componer morfismos y verificar que los diagramas de constraints conmutan.

Esta perspectiva es dual a la coalgebraica. La coalgebra mira desde el estado hacia afuera: "dado el estado actual, ¿qué observo?" El funtor indexante mira desde la acción hacia afuera: "dada esta acción, ¿qué episodio produjo?" Son dos maneras de organizar relacionalmente la identidad de un sistema. En el mejor de los casos, cada una induce un patrón de observables suficientemente rico para distinguir lo que la categoría decide distinguir. La primera lectura es covariante; la segunda, contravariante.

En la práctica, event sourcing es action-primary-key. Cada evento en el log es un morfismo, no un estado. El estado actual se reconstruye componiendo todos los morfismos desde el estado inicial -- es un fold (catamorfismo) sobre la secuencia de acciones. El append-only log es la categoría libre sobre el grafo de eventos, y la reconstrucción del estado es el único homomorfismo desde esa categoría libre al álgebra de estados. Cuando diseño un sistema con event sourcing, estoy eligiendo la perspectiva action-primary; cuando diseño con CRUD, estoy eligiendo la perspectiva state-primary (coalgebraica). Ambas son válidas; la elección depende de qué dimensión del sistema necesito que sea composicional.

## Tool use como morfismo externo

Cuando un agente usa una herramienta, compone un morfismo en su propia categoria con un morfismo en la categoria de la herramienta. Pero esta composicion no ocurre dentro de ninguna de las dos categorias -- ocurre en una estructura que las conecta: un profunctor P : Agent^op x Tool -> Set.

Cada elemento de P(a, t) es una interaccion valida entre el agente a y la herramienta t. Si el agente es un LLM con function-calling, las posiciones del profunctor son las firmas de las funciones disponibles, y las direcciones son los parametros validos para cada firma. El agente no necesita entender los internos de la herramienta; le basta una interfaz suficientemente expresiva para componer con ella. En ese sentido, la interfaz cumple el papel externo que Yoneda vuelve natural: organizar lo observable sin inspeccionar la implementacion.

La composicion de uso de herramientas es composicion de profunctores. Si P conecta agentes con herramientas de busqueda y Q conecta herramientas de busqueda con bases de datos, la composicion Q . P conecta agentes con bases de datos. La formula es la convolucion coend: (Q . P)(a, d) = integral^t Q(t, d) x P(a, t). Un agente multi-herramienta tiene un profunctor sobre el coproducto de categorias de herramientas: P : Agent^op x (Tool_1 + ... + Tool_n) -> Set. La eleccion de herramienta es la eleccion de componente del coproducto. La composicion de herramientas en secuencia es composicion de profunctores. La invocacion en paralelo es su producto monoidal.

## Perception-Decision-Action como triple categorico

El ciclo Perception-Decision-Action que estructura todo agente tiene una formulacion categorica precisa como composicion de tres estructuras distintas.

La percepcion se parece mas a una operacion de reindexacion o pullback de observaciones que a un funtor ordinario hacia adelante. Dado el estado del mundo W y la interfaz de observacion del agente, la percepcion "tira hacia atras" los datos relevantes del entorno al espacio interno del agente. En la practica, es el encoder que transforma inputs crudos (pixeles, tokens, sensores) en representaciones internas.

La decision es seleccion interna de morfismos. Dentro del free monad del agente, la decision elige una rama del arbol de decisiones. Dado el estado percibido, el agente selecciona un morfismo en su categoria interna -- una accion entre las disponibles. Esta seleccion es un morfismo en la categoria de Kleisli del free monad: toma el estado actual y produce un estado+accion envuelto en la monada.

La accion es un funtor -- empuja efectos hacia adelante. El funtor Act : InternalState -> WorldEffect traduce la decision interna del agente en un cambio en el mundo. La functorialidad garantiza que componer dos decisiones internas y luego actuar es lo mismo que actuar sobre cada decision y componer los efectos: Act(d2 . d1) = Act(d2) . Act(d1).

El ciclo completo P-D-A es un traced morphism. La accion modifica el mundo, la percepcion observa el mundo modificado, la decision elige la siguiente accion -- y el ciclo se repite. El cable de feedback que conecta la salida de Action con la entrada de Perception es la traza en una categoria compact closed. La convergencia del ciclo -- que el agente alcance su objetivo -- es la condicion de que la traza converja a un punto fijo.

## Memoria como transformacion de estado

La memoria de un agente es una monada de estado donde el espacio de estados es la base de conocimiento del agente. Formalmente, la monada State K asigna a cada tipo A el tipo K -> (A, K): una computacion que lee la base de conocimiento, produce un resultado, y devuelve una base de conocimiento posiblemente modificada.

El aprendizaje es composicion Kleisli en la monada State K. Cada experiencia nueva es un morfismo Kleisli e : Observation -> State K (Updated_Knowledge). La composicion de experiencias -- aprender de una secuencia de observaciones -- es la composicion Kleisli e_n >=> e_{n-1} >=> ... >=> e_1. La asociatividad de la composicion Kleisli garantiza que el orden de agrupamiento no importa: aprender (a luego b) luego c es lo mismo que aprender a luego (b luego c).

El olvido es un funtor olvidadizo sobre el espacio de estados. El funtor U : Full_Knowledge -> Working_Knowledge descarta informacion, preservando solo lo relevante para la tarea actual. La composicion de aprendizaje seguida de olvido es una proyeccion: se retiene solo la traza de la experiencia en el espacio de trabajo.

La memoria de trabajo es un limite finito del estado completo. Si el estado completo K es un limite de la cadena de experiencias, la memoria de trabajo es una aproximacion finita -- un cono finito que captura las ultimas N experiencias. La atencion es la seleccion del sub-diagrama sobre el que se calcula el limite: elegir a que prestar atencion es elegir que partes de la experiencia contribuyen a la memoria de trabajo actual.

## La convergencia

Todos estos marcos convergen en una vision unificada de la agencia. El free monad es el plan -- finito, ramificante, terminante. El cofree comonad es el ejecutor -- infinito, persistente, reactivo. La ley de interaccion es la ejecucion -- el patron consume materia. Las operads dinamicas son la organizacion -- jerarquica, adaptiva, con accounting. Los contextads son la dependencia contextual -- parametros, efectos, relaciones, todos unificados por wreath products. El embedding de Yoneda y el paso al topos de presheaves proporcionan un buen marco para estudiar emergencia relacional. Y los funtores de co-sintesis son la verificacion -- el intento de mantener alineados artefacto ejecutable y modelo formal.

Lo que antes era intuicion artesanal -- "el prompt chain es como un arbol de decisiones," "los agentes necesitan contexto," "la organizacion debe adaptarse" -- ahora tiene una formulacion precisa en la interaccion entre monadas libres y comonadas cofree, modulada por operads dinamicas y contextads. No pierdo la intuicion; la gano en composabilidad.
