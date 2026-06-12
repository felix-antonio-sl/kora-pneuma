---
urn: urn:fxsl:kb:icas-tiempo
nombre: icas-tiempo
version: 1.0.0
estado: publicado
descripcion: "Pieza 15 del ICAS-BoK: tiempo — behavior types, sheaves temporales, sheaves híbridos, contratos composicionales y delay aditivo; invariantes temporales, SLA, circuit breakers y event sourcing."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/15-tiempo.md (sha256:94f380b1bcfd1c227ac37c65907605a8d2a3c7f2ac480368eeff7324492ed30b) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [sheaf-temporal, event-sourcing, consistencia-temporal, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Tiempo

## Cuando el tiempo importa

Todo lo que construi hasta aqui -- funtores, adjunciones, monadas, polinomios, operads -- vive en una especie de presente eterno. Las categorias que he usado capturan estructura, composicion, interaccion. Pero no capturan que las cosas cambian. Que un servicio esta arriba a las 3am y abajo a las 3:01am. Que un deployment empieza con la version vieja y termina con la nueva. Que un circuit breaker esta cerrado durante minutos y luego, en un instante, se abre.

El tiempo no es un parametro mas que puedo agregar a un sistema. Es una dimension que transforma la naturaleza misma de lo que observo. Un dato no es un valor: es un valor que dura. Una propiedad no es verdadera o falsa: es verdadera durante un intervalo y falsa durante otro. Una especificacion no dice "el sistema hace X" -- dice "el sistema hace X siempre que la condicion Y se haya mantenido durante los ultimos delta segundos."

Schultz y Spivak, en su Temporal Type Theory, construyen un topos entero dedicado a esta idea. No decoran una logica existente con operadores temporales. Construyen un universo donde el tiempo es constitutivo -- donde los objetos mismos son comportamientos que se despliegan en duraciones. Al leer su trabajo, lo que vi fue el cierre de un arco que empezo en el documento 01: la composicion adquiere temporalidad, y con eso, todo lo anterior cobra vida.

## Behavior types como sheaves

La idea fundante es deceptivamente simple. Un tipo de comportamiento B asigna a cada duracion de tiempo l un conjunto B(l) de comportamientos posibles durante esa ventana. Para una duracion de 5 segundos, B(5) contiene todos los posibles trazos de comportamiento de 5 segundos. Para una duracion de 10 segundos, B(10) contiene todos los trazos de 10 segundos.

Y aqui viene la estructura: si tengo un comportamiento de 10 segundos, puedo restringirlo a cualquier subventana de 5 segundos para obtener un comportamiento de 5 segundos. Esto es un restriction map. Y si tengo dos comportamientos en ventanas solapadas que coinciden en el solapamiento, puedo pegarlos para formar un comportamiento sobre la ventana union. Esto es la condicion de sheaf.

Un tipo de comportamiento es un sheaf sobre un site de intervalos. No es un sheaf sobre un espacio topologico arbitrario como en el documento 12 -- es un sheaf sobre el dominio de intervalos IR, el conjunto de intervalos cerrados [a,b] en los reales, ordenados por inclusion reversa. El intervalo [2,7] es "mas grande" que [3,5] porque [3,5] esta contenido en [2,7], y en el orden de IR esto significa que [2,7] <= [3,5]. Esta inversion es natural: un intervalo mas grande impone menos restriccion (hay mas posibles sub-comportamientos), asi que esta mas abajo en la jerarquia de informacion.

La definicion precisa: IR es un posite -- un poset equipado con una coverage que dice que familias de intervalos "cubren" un intervalo. Los objetos del topos Shv(IR) son los (0,1)-sheaves sobre este site. Cada tipo de comportamiento vive en este topos.

Una pelicula es un tipo de comportamiento: para cualquier duracion, hay un conjunto de posibles clips de esa duracion. "Toda la musica posible" es un tipo de comportamiento: a cada duracion le asigna el conjunto de todas las secuencias posibles de 24 cuadros por segundo con overlay de sonido. Las funciones monotonas de R a R forman un tipo de comportamiento: para cada intervalo, el conjunto de funciones monotonas definidas en ese intervalo, con restriccion como el restriction map obvio.

## Invariancia bajo traslacion y el tipo Time

Pero hay un problema sutil. Si defino un comportamiento sobre [2,7] y otro sobre [102,107], ambos duran 5 segundos. ¿Son "el mismo tipo de comportamiento"? En la mayoria de los sistemas que construyo, si. A un servidor no le importa si son las 2am o las 102am -- le importa cuanto dura la request. El comportamiento no depende del tiempo absoluto, solo de la duracion y el orden relativo.

El grupo (R, +) actua sobre IR desplazando intervalos: t envia [a,b] a [a+t, b+t]. Una forma concreta de pasar a comportamientos invariantes por traslacion es tomar el cociente por esta accion y escribir, como en el documento 12, `B = Shv(IR/▷)`. Tambien puede hablarse informalmente de "sheaves modulo traslacion". Ese es el universo donde quiero trabajar: comportamientos que no dependen de un origen temporal absoluto.

Dentro de B existe un objeto notable: el tipo Time. Time es un R-torsor. Representa "momentos en el tiempo" sin un cero privilegiado. Puedo medir la diferencia entre dos tiempos (y obtener un numero real), pero no puedo decir "este momento es el instante cero." Es como un affine space para el tiempo: hay desplazamientos pero no hay origen.

La derivada de Time es 1. Esto significa que el tiempo avanza a ritmo unitario -- una tautologia profunda que sin embargo se puede demostrar formalmente dentro de la logica del topos. Y Time tiene igualdad decidible: dados dos tiempos, o son iguales o no lo son. Pero Time no es constante -- no se puede identificar con ningun numero real fijo. Es la encarnacion de la temporalidad pura.

## Modalidades temporales

Sobre el topos B actuan cuatro modalidades -- endofuntores que transforman proposiciones temporales:

- **up (siempre en el futuro)**: la proposicion P vale para todo tiempo futuro. "La altitud nunca excedera FL410" es una proposicion up.
- **down (siempre en el pasado)**: P valio para todo tiempo pasado. "El servicio nunca estuvo abajo antes" es una proposicion down.
- **@ (en algun punto)**: P vale en algun instante, no importa cuando. "Eventualmente el garbage collector correra" es @.
- **pi (pointwise)**: P vale punto a punto, sin ninguna condicion de continuidad entre instantes. "En cada instante individual, la memoria esta por debajo del limite" es pi.

Estas modalidades forman una red de adjunciones. Las adjunciones pi -| @ y down -| up capturan la tension entre lo puntual y lo global, entre el pasado y el futuro. Y lo crucial: estas no son operadores bolteados sobre una logica existente. Son endofuntores del topos B con semantica precisa dada por la estructura de sheaves.

Cuando escribo un SLA que dice "99.9% uptime medido en ventanas de 30 dias", estoy combinando modalidades. La ventana de 30 dias es una restriccion del sheaf. El porcentaje es una medida sobre las secciones. Y la obligacion contractual es una proposicion up aplicada a la ventana.

## Hybrid sheaves: cuando lo continuo se mezcla con lo discreto

Los sistemas reales no son puramente continuos ni puramente discretos. Un vuelo tiene modos -- taxiing, climbing, cruising, descending, landing -- cada uno con su propia dinamica continua (ecuaciones diferenciales que gobiernan altitud, velocidad, combustible). Las transiciones entre modos son eventos discretos.

Schultz y Spivak formalizan esto con los hybrid sheaves. Un hybrid datum es una tupla (C, D, src, tgt, tau) donde C es un tipo de comportamiento continuo, D es un tipo de transicion discreta, src y tgt asignan a cada transicion el comportamiento continuo de la izquierda y la derecha, y tau : D -> Time marca el instante de la transicion. El tipo hibrido de comportamiento Hyb(C, D) es el tipo de comportamientos que pueden tener finitamente muchas transiciones discretas intercaladas con periodos de dinamica continua.

La definicion es un pushout seguido de sheafificacion -- una construccion que usa los colimites y la topologia del topos B. Y la propiedad clave: una seccion de Hyb(C, D) esta "almost always" en la parte continua C. Las transiciones discretas son instantaneas -- duran exactamente cero tiempo.

Un circuit breaker es un hybrid sheaf. El comportamiento continuo C tiene dos modos: cerrado (el servicio responde normalmente) y abierto (el fallback esta activo). La transicion D ocurre cuando la tasa de errores cruza un umbral -- un evento instantaneo que cambia el modo. El tau marca el instante exacto de la apertura. Y la restriccion de sheaf garantiza que si miro una ventana de tiempo suficientemente pequena alrededor de tau, veo el comportamiento continuo de un lado y del otro con la transicion en el medio.

## Delays: el morfismo que desplaza

Un delay de duracion D es un morfismo en B que desplaza el comportamiento por D unidades de tiempo. Formalmente, un par (a, a') : A x A es D-delayed si, para cada predicado phi sobre A y cada constante c de tipo C, la seccion a satisface phi en el intervalo [d,u] si y solo si a' satisface phi en el intervalo [d+D, u+D].

Esto captura exactamente la latencia de red, el buffering en pipelines, el retraso de propagacion en sistemas distribuidos. Un mensaje publicado en un topic Kafka a tiempo t llega al consumidor a tiempo t+D. El delay D es un morfismo del tipo de comportamiento del productor al tipo de comportamiento del consumidor.

Y dentro de la logica del topos, puedo razonar sobre estos delays composicionalmente. Si el servicio A tiene delay D1 hacia B y B tiene delay D2 hacia C, el delay total de A a C es D1+D2. La composicion de delays es aditiva -- exactamente lo que esperaria, pero ahora con una demostracion formal.

## Systems, components y behavior contracts

Una machine en este framework es un objeto con una interfaz (una coleccion de puertos, cada uno con un tipo de comportamiento) y un tipo total de comportamiento X que mapea a cada puerto via port maps p_i : X -> S_i. Reconozco aqui la estructura de los polynomial functors del documento 11: la interfaz es un polinomio, la machine es un lens del espacio de estados al polinomio.

Pero ahora hay tiempo. El tipo total de comportamiento X no es un conjunto estatico de estados -- es un sheaf temporal. La machine no solo responde a inputs: se comporta a lo largo de duraciones. Y las propiedades que me importan son propiedades temporales: "la temperatura se mantiene entre 18 y 22 grados durante toda la operacion", no "la temperatura es 20 grados ahora."

Un contrato de comportamiento es un predicado temporal sobre los tipos de comportamiento de una interfaz. Es una proposicion en el lenguaje interno del topos B que dice que ciertas relaciones entre las variables del sistema se mantienen a lo largo del tiempo. El contrato se formula en contexto -- un juicio de tipo Gamma, donde Gamma nombra las variables de la interfaz.

Un sistema se compone de componentes, cada uno con su interfaz, su behavior contract, y su cableado (wiring diagram, como en el documento 13). La composicion de componentes produce un sistema cuyo contrato exterior se puede derivar de los contratos individuales y la topologia de conexion. Esto es el teorema de composicionalidad de contratos: si cada componente satisface su contrato, y el cableado es correcto, el sistema compuesto satisface el contrato derivado.

## El National Airspace System

El caso de estudio canonico de Schultz y Spivak es el National Airspace System de la FAA. Aeronaves, sectores del espacio aereo, controladores -- cada uno con sus tipos de comportamiento, contratos y composicion.

Un avion tiene un tipo de comportamiento que incluye altitud, velocidad, rumbo, tasa de combustible -- todos variando continuamente con transiciones discretas (cambio de modo de vuelo). Un sector tiene contratos de separacion: dos aviones en el mismo sector deben mantener al menos 5 millas nauticas de distancia horizontal o 1000 pies de separacion vertical, en todo momento. Un controlador recibe senales de posicion con un delay D (la latencia del radar) y emite instrucciones que se ejecutan con otro delay D' (el tiempo de reaccion del piloto).

La propiedad de safe separation -- que ningun par de aviones viola la distancia minima -- se formula como una proposicion up sobre el tipo de comportamiento del sector completo. Y se puede probar combinando los contratos individuales de aviones y controladores con los delays del sistema de comunicacion y las dinamicas continuas de movimiento.

Este ejemplo muestra algo profundo: el mismo framework que uso para circuit breakers y SLAs se aplica al espacio aereo. La estructura categorica -- sheaves, modalidades, hybrid types, delays -- es suficientemente general para capturar sistemas tan distintos como un cluster de Kubernetes y un sistema de control de trafico aereo.

## Todo converge aqui

Este es el ultimo documento conceptual del corpus, y no es accidental que sea el del tiempo. El tiempo es donde todo converge.

Los sheaves del documento 12 se concretan: en este framework, un tipo de comportamiento se define como un sheaf sobre un site temporal especifico. Los polynomial functors del documento 11 reaparecen: las interfaces de los sistemas son polinomios, las machines son lenses. Las coalgebras del documento 09 adquieren temporalidad: una machine es una coalgebra de un polinomio, pero ahora con un espacio de estados que es un sheaf temporal. La composicion operadica del documento 13 se enriquece: los wiring diagrams componen systems con contratos que se propagan composicionalmente. Y la dualidad pattern/matter del documento 14 se despliega EN el tiempo: el pattern (el arbol finito de decisiones de un agente) corre sobre matter (el stream infinito de comportamiento) a lo largo de duraciones reales.

El event log de un sistema event-sourced se deja modelar de forma natural como un tipo de comportamiento. Para cada ventana temporal, provee los eventos que ocurrieron. El replay es el restriction map: tomar el log de una ventana mas larga y restringirlo a una subventana. La condicion de sheaf dice: si tengo logs parciales de ventanas solapadas que coinciden en el solapamiento, existe un unico log global consistente. Decir "event sourcing es un sheaf" es una buena abreviatura para esa modelizacion, no una identidad sin resto.

Una migracion de base de datos de schema S1 a schema S2 es un morfismo en una categoria temporal de schemas. El schema S1 existe "antes" y S2 existe "despues". La migracion respeta el orden temporal. Y la composicionalidad de migraciones -- que puedo componer M1 : S1 -> S2 y M2 : S2 -> S3 para obtener M2 . M1 : S1 -> S3 -- es composicion de morfismos en esta categoria temporal.

Un blue/green deploy puede modelarse como un morfismo entre tipos de comportamiento: el tipo viejo y el tipo nuevo, conectados por una transicion que es un hybrid sheaf con un solo evento discreto -- el switch. El rate limiting es una restriccion temporal sobre la frecuencia de interacciones: "a lo sumo N requests en cualquier ventana de duracion delta" es un predicado sobre secciones del tipo de comportamiento de requests. Un cron job es la modalidad up aplicada a una accion periodica.

Cuando miro atras al corpus completo, lo que veo es una unica estructura que se repite en dimensiones crecientes: composicion, preservacion, universalidad, interaccion, y ahora temporalidad. Cada nueva dimension no reemplaza las anteriores sino que las enriquece. El tiempo no anula la composicion -- la hace temporal. No destruye los funtores -- les da dinamica. No elimina los contratos -- los hace verificables a lo largo de duraciones. Esta es la promesa de la teoria de categorias para sistemas: no una herramienta puntual para un problema puntual, sino un lenguaje que crece con la complejidad de lo que trato de capturar.
