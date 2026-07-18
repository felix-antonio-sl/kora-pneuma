---
urn: urn:fxsl:kb:icas-enriquecimiento
nombre: icas-enriquecimiento
version: 1.1.0
estado: publicado
descripcion: "Pieza 08 del ICAS-BoK: categorías enriquecidas — Bool/Cost-categories, espacios métricos de Lawvere, profunctors y cambio de base; relaciones cuantitativas (latencia, fiabilidad, costo, QoS)."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/08-enriquecimiento.md (sha256:3c514ef1407c0112d3bb0a1bdf29e578391b86b61e591e994e6f191ad5b8bd00) el 2026-06-12. Corrección 1.1.0 contrastada con Lawvere, Metric Spaces, Generalized Logic, and Closed Categories, https://www.math.buffalo.edu/~sww/0papers/lawveres-metric-space-paper.pdf."
autor: FS
creado: 2026-04-14
lang: es
tags: [enriched-category, cost, metricas-cuantitativas, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Enriquecimiento

## Mas alla de si o no

Hasta ahora cada hom-set ha sido un conjunto plano: los morfismos de A a B forman un set, y la unica pregunta que puedo hacer es "existe un morfismo?" o "cuantos hay?" Eso me basta para muchas cosas, pero no captura una dimension que aparece constantemente en sistemas reales: la dimension cuantitativa. ¿Cuanto cuesta llegar de A a B? ¿Con que probabilidad? ¿Con que latencia? ¿Con que nivel de acceso?

Cuando modelo la topologia de red de un cluster, no me basta saber que el servicio A puede hablar con el servicio B. Necesito saber cuanto tarda -- 2ms, 50ms, 200ms. Cuando modelo permisos, no me basta un grafo de "puede o no puede." Necesito niveles: lectura, escritura, administracion. Cuando modelo calidad de servicio, necesito un numero real entre 0 y 1 que me diga la fiabilidad del canal.

La solucion categorica es reemplazar los hom-sets (objetos en Set) por hom-objects en otra categoria V. Eso es una V-category, una categoria enriquecida sobre V. La idea es simple pero tiene consecuencias profundas: al cambiar la "moneda" con la que mido las relaciones entre objetos, cambio todo el caracter del universo matematico.

## V-categorias: la definicion

Sea V = (V, tensor, I) una categoria monoidal -- ya la conozco del documento 07. Una V-category X consiste en:

- Un conjunto de objetos Ob(X).
- Para cada par de objetos x, y, un hom-object X(x, y) que es un objeto de V (no un conjunto).
- Composicion como morfismo en V: X(y, z) tensor X(x, y) -> X(x, z).
- Identidad como morfismo en V: I -> X(x, x), donde I es la unidad monoidal.

Sujeto a asociatividad y unitalidad, expresadas como diagramas en V que conmutan usando los associators y unitors.

La clave conceptual: ya no puedo "elegir un morfismo" individual, porque los hom-objects no son conjuntos. La composicion no toma un par de flechas y produce otra flecha; toma el tensor de dos hom-objects y produce un hom-object. Todo se expresa globalmente, sin nombrar elementos.

Fong y Spivak lo formulan de manera elegante en el caso preordinal. Como los preordenes son categorias monoidales simples, la definicion de V-category se reduce a condiciones que se leen directamente.

## Bool-enrichment: los preordenes recuperados

El primer ejemplo canónico es V = Bool = ({true, false}, <=, true, AND). Aqui la unidad monoidal es true y el tensor es la conjuncion.

Una Bool-category X asigna a cada par (x, y) un valor booleano X(x, y) in {true, false}. Las condiciones de V-category se reducen a:

- Identidad: true <= X(x, x), que fuerza X(x, x) = true. Esto es reflexividad.
- Composicion: X(x, y) AND X(y, z) <= X(x, z). Si x <= y y y <= z, entonces x <= z. Esto es transitividad.

El resultado es un preorden. Los preordenes son exactamente las Bool-categories. Fong y Spivak demuestran este isomorfismo con una construccion explicita en ambas direcciones.

Esto permite modelar como preorden la **herencia monotónica** de permisos: si
un rol hereda de otro y este accede a un recurso, el acceso se propaga. Un
sistema real con denegaciones explícitas, contexto, separación de funciones o
prioridades puede no ser preorden y necesita otra base.

## Cost-enrichment: espacios metricos de Lawvere

El segundo ejemplo canonico, y el que mas impacto tiene en mi practica, es V = Cost = ([0, infinito], >=, 0, +). Los objetos de Cost son numeros reales no negativos (incluyendo infinito). El orden esta invertido: x >= y significa que hay un morfismo de x a y. La unidad monoidal es 0 y el tensor es la suma.

Una Cost-category X es un conjunto de objetos donde X(x, y) in [0, infinito] asigna una "distancia" o "costo" a cada par. Las condiciones dan:

- Identidad: 0 >= X(x, x), que fuerza X(x, x) = 0. La distancia de un punto a si mismo es cero.
- Composicion: X(x, y) + X(y, z) >= X(x, z). La desigualdad triangular.

Lawvere observo que esto es exactamente un espacio metrico generalizado -- sin exigir simetria ni separacion. Un espacio metrico de Lawvere permite distancias asimetricas (cuesta mas subir que bajar) y distancias infinitas (no hay camino).

Una red pesada genera una métrica de Lawvere al tomar el costo mínimo de
caminos. Las mediciones crudas de latencia, variables en el tiempo y afectadas
por congestión, no satisfacen automáticamente la desigualdad triangular. La
asimetría sí puede representarse.

La `Cost`-categoría libre generada por un grafo pesado dirigido toma shortest
paths. Para aristas `A->B:3`, `B->C:2`, `A->C:10`, resulta
`X(A,C)=min(10,3+2)=5`; el cierre matricial en `(min,+)` computa esos
hom-values. El grafo inicial y su cierre enriquecido no son el mismo objeto.

## [0,1]-enrichment: calidad de servicio

Un caso que uso frecuentemente es V = ([0,1], <=, 1, *), donde el tensor es la multiplicacion y la unidad es 1. Aqui el hom-object X(x, y) in [0,1] mide la fiabilidad o probabilidad de exito del canal de x a y.

La composicion dice que la fiabilidad del camino compuesto es al menos el producto de las fiabilidades individuales: X(x, y) * X(y, z) <= X(x, z). La identidad dice que la fiabilidad del canal de un nodo a si mismo es 1.

Este enriquecimiento modela una cota multiplicativa bajo hipótesis como
independencia y probabilidades estables. Sin ellas, multiplicar `0.99` y
`0.95` no determina la fiabilidad compuesta; tampoco el sistema «elige» el
camino más fiable salvo que exista una política de routing que lo haga.

## Cambio de base de enriquecimiento

Hay una operacion que conecta todos estos mundos: el cambio de base. Si tengo un monoidal monotone f : V -> W (un funtor monoidal lax entre categorias monoidales vistas como preordenes), puedo convertir cualquier V-category en una W-category preservando los objetos y aplicando f a los hom-objects.

Fong y Spivak lo definen formalmente: dada una V-category C, la W-category C_f tiene los mismos objetos y hom-objects C_f(c, d) = f(C(c, d)). Las condiciones de V-category se transfieren automaticamente gracias a las propiedades del monoidal monotone.

Un contraejemplo importante: para `epsilon > 0`, la función
`t_epsilon(x) = true` si `x <= epsilon` **no** es en general monoidal lax de
`Cost` a `Bool`. La condición exigiría que de `x <= epsilon` e
`y <= epsilon` se siguiera `x+y <= epsilon`, lo que falla. En un espacio
métrico, tres puntos con distancias `0.75 epsilon`, `0.75 epsilon` y
`1.5 epsilon` muestran que «estar a distancia <= epsilon» no es transitivo.
Por tanto el umbral produce un **grafo de proximidad**, no automáticamente una
Bool-category/preorden.

Hay dos reparaciones distintas: `epsilon = 0` sí respeta la composición, o se
toma el cierre reflexivo-transitivo del grafo de proximidad. Este último
produce un preorden de alcanzabilidad, pero cambia la semántica: relaciona
puntos conectados por una cadena de saltos cortos aunque su distancia directa
supere el umbral.

En la otra direccion, la inclusion Bool -> Cost que envía true a 0 y false a infinito convierte preordenes en espacios metricos discretos: o estas a distancia 0 o estas a distancia infinita.

## V-functors y V-natural transformations

Un V-functor F : X -> Y entre V-categories preserva la estructura enriquecida. No mapea morfismos individuales -- mapea hom-objects completos. Para cada par de objetos, da un morfismo en V:

F_{a,b} : X(a, b) -> Y(Fa, Fb)

compatible con composicion e identidad.

Un Bool-functor es exactamente un monotone map entre preordenes. Un Cost-functor es una funcion 1-Lipschitz: d_X(x, y) >= d_Y(Fx, Fy). La estructura enriquecida impone condiciones mas fuertes que un funtor ordinario.

Las V-natural transformations generalizan las transformaciones naturales al contexto enriquecido, reemplazando la condicion de naturalidad puntual por una condicion global expresada con hom-objects. En el caso Bool, una Bool-natural transformation es simplemente la condicion de que la relacion se preserva. En el caso Cost, es una condicion de no-expansividad.

## Enriquecimiento en Cat: las 2-categorias

El caso V = Cat (la categoria de categorias pequenas, con producto cartesiano como tensor) produce las 2-categorias. Una categoria enriquecida en Cat tiene objetos, y entre cada par de objetos no un conjunto de morfismos sino una categoria de morfismos. Los objetos de esa categoria interna son los 1-morfismos (las flechas originales) y los morfismos son los 2-morfismos (las flechas entre flechas).

La composicion en una 2-categoria tiene dos dimensiones. La composicion vertical compone 2-morfismos dentro de una misma hom-categoria: si alpha : f => g y beta : g => h son 2-morfismos entre los mismos objetos, beta . alpha : f => h es su composicion vertical. La composicion horizontal compone 2-morfismos en hom-categorias adyacentes: si alpha : f => g : A -> B y beta : h => k : B -> C, entonces beta * alpha : h.f => k.g : A -> C es su composicion horizontal.

La interchange law dice que las dos composiciones son compatibles: (beta . beta') * (alpha . alpha') = (beta * alpha) . (beta' * alpha'), cuando las composiciones estan definidas. En string diagrams es la condicion de que cajas en cables independientes se pueden mover libremente.

El ejemplo que mas uso: la arquitectura de microservicios como 2-categoria. Los objetos son los servicios. Los 1-morfismos son las llamadas (endpoints). Los 2-morfismos son las transformaciones entre llamadas -- refactorings de API, wrappers, adaptadores. La composicion vertical es encadenar adaptadores. La composicion horizontal es componer llamadas de servicio a servicio con sus adaptadores.

Otro ejemplo: Cat misma es una 2-categoria. Las categorias son 0-celdas, los funtores son 1-celdas, las transformaciones naturales son 2-celdas. Cuando en el documento 03 defini transformaciones naturales, ya estaba trabajando dentro de una 2-categoria sin saberlo.

## Categorias internas

Hay una nocion relacionada pero distinta: una categoria interna a una categoria C con pullbacks. Mientras que una V-category reemplaza los hom-sets por hom-objects, una categoria interna a C reemplaza la coleccion de objetos y la coleccion de morfismos por objetos de C. Una categoria interna tiene un objeto de objetos Ob, un objeto de morfismos Mor, morfismos source y target s, t : Mor -> Ob, identidad i : Ob -> Mor, y composicion c : Mor x_Ob Mor -> Mor (donde el pullback asegura que el target de uno coincide con el source del otro).

Un grupo interno en Set es un grupo ordinario. Un grupo interno en Top es un grupo topologico. Un grupo interno en Diff es un grupo de Lie. La misma definicion categorica, cambiando el ambiente, produce estructuras clasicas distintas.

## Profunctors: relaciones enriquecidas

Los profunctors generalizan las relaciones al mundo enriquecido. Un V-profunctor Phi : X -> Y entre V-categories es un V-functor Phi : X^op tensor Y -> V. En el caso Bool, un profunctor es una relacion de feasibility. En el caso Cost, un profunctor asigna costos a pares (x, y) con x in X e y in Y, respetando la estructura metrica.

La composicion de profunctors en un quantale V (una categoria monoidal preordinal con todos los joins y tensor distribuyendo sobre joins) se define con una formula que es esencialmente una multiplicacion matricial generalizada:

(Phi . Psi)(x, z) = join_{y in Y} Phi(x, y) tensor Psi(y, z)

En Cost, esto es min_{y} (Phi(x,y) + Psi(y,z)) -- el shortest path a traves de un waypoint. En Bool, es exists y . Phi(x,y) AND Psi(y,z) -- "hay un camino pasando por algun y."

Los profunctors son la herramienta para co-design: descomponer un problema de ingenieria en componentes con interfaces cuantitativas y calcular la factibilidad global por composicion.

## El patron recurrente

El enriquecimiento parametriza los hom-objects y su composición por una base
monoidal. `Bool` da preórdenes, `Cost` métricas de Lawvere y `Cat`
2-categorías. `[0,1]` da una estructura de cotas multiplicativas; llamarla red
de fiabilidad requiere justificar la semántica probabilística.

En la práctica, primero identifico una base monoidal y compruebo sus leyes
contra el dominio. Entonces una categoría y un funtor enriquecidos proporcionan
composición y preservación de las cotas **codificadas**; no garantizan que la
métrica elegida sea una medición correcta del sistema real.

## Corrección 1.1.0

Se retira el falso cambio de base por umbral positivo. El threshold ordinario
da un grafo de proximidad; solo una construcción compatible con el tensor o un
cierre explícito produce el preorden.
