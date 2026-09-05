---
urn: urn:fxsl:kb:icas-calidad-riesgo
nombre: icas-calidad-riesgo
version: 1.1.0
estado: publicado
descripcion: "Pieza 18 del ICAS-BoK: calidad y riesgo — quality attributes, RAM, resiliencia y garantías formuladas con métricas enriquecidas y vocabulario formal."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/18-calidad-riesgo.md (sha256:033be897e2b071186bee582adff6df17f8068398ab38af49192aea17b57690b9) el 2026-06-12. Corrección de rigor 1.1.0 (2026-07-18): se retira la identificación genérica verificación=end y test=coend."
autor: FS
creado: 2026-04-14
lang: es
tags: [quality-attributes, riesgo, metricas-enriched, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Calidad y riesgo

## Las propiedades que no se ven en el diagrama de arquitectura

Cuando dibujo un sistema --- cajas, flechas, puertos --- lo que dibujo es la estructura funcional. Que componentes existen, como se conectan, que datos fluyen. Pero las propiedades que hacen que un sistema sea confiable, seguro, rapido y mantenible no viven en las cajas ni en las flechas. Viven en otra dimension. La latencia no es un componente; es una medida sobre los morfismos. La confiabilidad no es una conexion; es una probabilidad sobre las trayectorias. La seguridad no es un dato; es la imposibilidad de ciertos caminos.

Estas propiedades requieren una formalización distinta a la estructura
funcional. **Pueden modelarse** mediante funtores desde una categoría del
sistema hacia categorías de medición si se definen los objetos, morfismos y la
acción sobre ambos. No todo atributo o dashboard es ya uno de esos funtores.

## Quality attributes como funtores de medicion

En ese modelo, un quality attribute `Q : SystemCat -> MeasurementCat` toma
componentes y transformaciones a mediciones compatibles. La categoría de
medición depende del atributo; las leyes de composición deben verificarse y no
se obtienen por escoger una escala numérica.

Munoz et al. formalizan exactamente esta idea para Software Product Lines. En su framework, las variability models (VMs) forman una categoria NVM cuyos objetos son arboles de features con nodos numericos y booleanos, y cuyos morfismos son las relaciones jerarquicas (Parent/Child, cardinality) y cross-tree constraints entre features. Los quality attributes forman una segunda categoria QAM cuyos objetos son Measured metrics sets M_S --- conjuntos de metricas con formato name-domain-metric como "Performance < 10 Seconds" o "EnergyConsumption in Joules" --- y cuyos morfismos son los non-functional requirements (NFRs) que restringen las metricas. El puente entre ambas categorias es un isomorphic functor F : M_NVM -> QAM que establece una correspondencia bijective entre los Complete Solution objects CS de NVM (los productos satisfactorios de la variability model) y los Measurement Sets objects MS de QAM (sus mediciones de calidad).

La intuicion que captura este framework es que un quality attribute no es un numero aislado. Es una funcion que depende de la configuracion del sistema. La performance de un sistema IoT con WiFi es distinta de la performance del mismo sistema con Bluetooth. La energia consumida depende de si los datos se comprimen o no, del tamano del batch, del chipset especifico. Munoz valida esto con la herramienta HADAS transformada en una categoria CQL: 30 features NVM, 2 QAs (performance en Seconds y energy rate en milliWatts), 162 soluciones validas con 324 mediciones, procesadas en 0.1 segundos. El funtor Q : System -> Measurement captura esta dependencia: para cada configuracion (un objeto en NVM), Q produce un perfil de calidad (un objeto en QAM).

Engel lo ilustra con los Key Performance Attributes del Battery Electric Vehicle. Cada KPA --- autonomia de 380 km, velocidad maxima de 225 km/h, aceleracion 0-100 en 6.1 s, potencia de 239 kW, torque de 420 Nm, bateria de 57 kWh, eficiencia de 150 Wh/km, vida util de 15 anos --- es una componente del funtor de quality. Los KPAs no son propiedades de un componente individual sino del sistema compuesto. La potencia total depende de la interaccion composicional entre motor electrico, power converter y bateria. El punto no es escribir esos subsistemas como si fueran morfismos aislados, sino afirmar que Q sobre el sistema compuesto debe poder derivarse de manera coherente a partir de los subsistemas y de sus interfaces. La Dependency Structure Matrix (DSM) del BEV captura esas interfaces --- 10 tipos distintos, desde Force/position hasta Material/energy --- y cada celda de la DSM puede leerse como una relacion estructural cuya calidad se mide de forma composicional.

## La categoria de quality attributes

Los quality attributes no son independientes. Mejorar performance puede
degradar consumo energético; redundancia puede mejorar reliability y aumentar
costo. Estas tensiones aportan datos para un modelo ordenado o enriquecido,
pero no forman una categoría por sí mismas.

Puede construirse una categoría `QA` si los objetos son perfiles de atributos
y los morfismos son transformaciones de diseño componibles. Tratar los
atributos aislados como objetos y los trade-offs como flechas exige tipar la
composición: una curva empírica `performance -> cost` no tiene necesariamente
inversa ni compone con cualquier otra curva.

Un orden de prioridades puede formar un preorder y servir como base de
enriquecimiento. Los trade-offs empíricos entre seguridad y usabilidad no
forman por ello adjunciones locales: harían falta mapas monótonos y la
equivalencia de orden que define la adjunción.

Un SLA es primero un contrato con una función de medición, una ventana y una
cota. Puede incorporarse a un funtor de calidad si se construyen las categorías
y la acción sobre morfismos. «99.9% uptime en 30 días» se evalúa directamente
como `availability(System,[t,t+30d]) >= 0.999`; el cruce del umbral es una
violación contractual, haya o no formalización funtorial.

Un performance budget puede modelarse en una categoría enriquecida en costes
si la composición de latencias usa la operación monoidal elegida. Para tres
componentes estrictamente seriales, `80+100+20 <= 200 ms` es una cota aditiva.
Paralelismo, colas y distribuciones de cola requieren otra operación o un
enriquecimiento más rico; el presupuesto por sí solo no construye la
categoría.

## RAM categoricamente

Reliability, Availability y Maintainability --- la triada RAM --- tienen formalizaciones categoricas precisas que conectan con la nocion de comportamiento temporal y con la nocion coalgebraica de estado.

**Reliability** puede modelarse como probabilidad de permanecer en un
subconjunto operacional durante `[0,t]`. Ese subconjunto es una
subcoálgebra solo si está cerrado bajo la transición y existe la estructura
coalgebraica restringida; una partición de estados no basta.

SIL y DAL pueden organizarse en órdenes de criticidad con cuidado de no mezclar
estándares ni métricas. Las metodologías de safety forman un proceso, no una
cadena functorial hasta definir categorías y preservación. Fault trees, event
trees y Markov chains son formalismos distintos; solo son modelos de una misma
subcoálgebra si se construyen traducciones semánticas entre ellos.

**Availability** es una medición temporal. Bajo independencia y topologías
serie/paralelo ideales aparecen las fórmulas `A1*A2` y
`1-(1-A1)(1-A2)`. Puede buscarse un funtor monoidal/lax que las organice, pero
las fórmulas por sí solas no construyen su categoría ni cubren common-cause
failures.

**Maintainability** puede medirse por el costo mínimo o esperado de caminos de
restauración en una categoría enriquecida o un sistema estocástico. Una función
`FailedStates -> N` no es automáticamente funtor y un estado puede tener varios
caminos o ninguno. MTTR exige además una distribución y un proceso temporal.

En un proceso reparable estacionario bajo hipótesis usuales,
`A ≈ MTBF/(MTBF+MTTR)`. Es una fórmula probabilística/temporal; no se vuelve
composición enriquecida solo porque sus magnitudes estén en `[0,∞]`.

## Riesgo como morfismo en la categoria de Kleisli

Un comportamiento incierto puede modelarse como flecha de Kleisli para una
mónada de distribuciones. «Riesgo» incluye además impacto, exposición y
criterios de decisión, y no se identifica con esa flecha sin codificarlos.

Formalmente, un morfismo con riesgo es una flecha de Kleisli k : A -> P(B + Error) donde P es la monada de probabilidad y B + Error es el coproducto de resultados exitosos y fallidos. Con probabilidad p, el morfismo produce un error; con probabilidad 1-p, produce el resultado correcto. La composicion de riesgos en la categoria de Kleisli propaga las probabilidades: si k_1 falla con probabilidad p_1 y k_2 falla con probabilidad p_2, la composicion k_2 .kl k_1 falla con probabilidad 1 - (1-p_1)(1-p_2) (asumiendo independencia). Myers formaliza los stochastic systems como morfismos en la categoria de Kleisli de la monada de distribuciones de probabilidad, y demuestra que esta construccion es functorial y composicional: el comportamiento del sistema compuesto se puede calcular a partir de los comportamientos de las partes.

La gestión de riesgos puede transformar kernels estocásticos y sus cotas. Con
intentos independientes y probabilidad de falla constante `p`, `n` intentos
fallan con `p^n`; correlación, backoff y fallas permanentes invalidan esa
fórmula. Fallback, risk register y threat modeling solo son flechas/órdenes de
Kleisli después de codificar resultados, impacto y composición.

## Resiliencia como recovery functor

En un modelo de transición enriquecido, la resiliencia puede exigir que cada
estado fallido considerado tenga un camino de recuperación hacia el dominio
operacional con costo temporal acotado. Esto no es un «recovery functor» hasta
definir una selección coherente de caminos y su acción.

Un circuit breaker tiene estados y transiciones operacionales que pueden
incluir `trip`, `half-open` y `reset`. Puede integrarse en un modelo híbrido o
coalgebraico, pero su implementación no garantiza recuperación: `reset` puede
fallar o reabrir, y el timeout solo habilita un intento.

En un álgebra específica de contracts, reglas de composición pueden transferir
garantías bajo assumptions compatibles. La resiliencia global no se reduce en
general a que cada componente tenga recuperación: dependencias, fallas comunes
y composición de tiempos deben formar parte del teorema.

Resilience testing y chaos engineering observan recuperación bajo fallas
inyectadas. Cada experimento aporta un caso y una cota medida; no es por ello
un coend. La verificación formal requeriría demostrar la propiedad para el
modelo completo de fallas considerado. Un end podría representar familias
naturales concretas, pero solo después de definir el profuntor correspondiente.

## Seguridad como ICAR

Valence construye ICAR --- Integrated CAtegorical Resource --- como una categoria de seguridad informatica cuyos objetos son los diccionarios de conocimiento: CPE (activos, con mas de 20,000 entradas), CVE (vulnerabilidades, 176,000 entradas), CWE (debilidades, 668 entradas), CAPEC (patrones de ataque, 559 entradas), ATT&CK Techniques (193 entradas) y Tactics (14 entradas). Los morfismos son las relaciones entre diccionarios: Has (un CVE tiene un CWE, un CWE tiene CAPECs), isChildOf/isParentOf (jerarquia dentro de CWE y CAPEC), isSubTechniqueOf (jerarquia de techniques), y accomplishesTactic (una Technique implementa una Tactic).

Lo que hace categorial a un knowledge schema es declarar objetos, morfismos,
identidades, composición y, cuando proceda, ecuaciones tipadas entre caminos.
Las relaciones parent/child de una jerarquía con ramificación no son inversas:
`child ; parent = id` y `parent ; child = id` solo valdrían en una
correspondencia biyectiva. Una instancia a `Set` respeta únicamente las
ecuaciones que el schema realmente presenta.

Los attack paths pueden ser composiciones en el schema. Una defensa cambia la
instancia o la semántica de alcanzabilidad —elimina, restringe o invalida una
ruta efectiva—; «hacer no conmutativo» un diagrama no es en general la
condición correcta de seguridad.

En el schema de Valence, algunas queries se expresan por pullbacks,
composición y proyección. Esa consistencia es relativa a la instancia, mappings
y equations del modelo; no garantiza actualidad ni corrección de los
diccionarios de seguridad.

Bakirtzis complementa esta perspectiva con su algebra de security tests. Un test de seguridad verifica que un ataque no logra componer morfismos para producir un comportamiento peligroso. El razonamiento en clave Yoneda da una forma util de modelar el aprendizaje del atacante: la exploracion se parece a la construccion progresiva del representable functor Hom(-, System), y la explotacion a la composicion exitosa de un attack path. La security posture del sistema es inversamente proporcional a la cantidad de informacion que el atacante puede extraer observando respuestas.

## Verificacion formal vs validacion empirica

Hay una distinción fundamental: la verificación formal demuestra una
propiedad sobre todos los casos cubiertos por un modelo; la validación
empírica observa casos elegidos. Property-based testing amplía la muestra y
model checking puede agotar un modelo finito, pero ninguno se identifica
genéricamente con un end o un coend.

Un end de `Hom(F-,G-)` representa transformaciones naturales porque incorpora
una condición de compatibilidad específica. Un coend es un cociente de un
coproducto por relaciones de dinaturalidad; no «existe trivialmente porque
puedo probar un input». Usar estas construcciones para V&V exige definir el
profuntor y demostrar que su propiedad universal coincide con la afirmación
verificada.

Las coálgebras aportan técnicas de bisimulación y semántica final cuando el
funtor y la coálgebra final existen y satisfacen las hipótesis pertinentes.
Esas técnicas no convierten toda verificación universal en un end ni toda
consistencia parcial en un coend.

## La convergencia

Los quality attributes, riesgos, resiliencia y seguridad pueden integrarse en
una misma estructura categorial cuando sus representaciones se tipan y sus
leyes se demuestran; fuera de ese caso son modelos parciales complementarios,
no automáticamente funtores o flechas de Kleisli.

En modelos concretos, reliability puede representarse con medidas temporales
sobre trayectorias, el riesgo mediante flechas de Kleisli probabilísticas y la
resiliencia mediante caminos de recuperación acotados. Cada elección exige sus
propias hipótesis. La naturalidad de una transformación
`eta : Spec => Reality` sería una formulación fuerte de coherencia solo si
`Spec` y `Reality` son funtores con componentes bien definidos.

## Corrección 1.1.0

Se elimina el falso «end-coend gap»: tests, chaos experiments y diccionarios
parciales no son coends por ser existenciales, ni la verificación es un end por
cuantificar universalmente. La notación queda reservada a profuntores y
propiedades universales explícitas.
