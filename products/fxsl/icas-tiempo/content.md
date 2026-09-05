---
urn: urn:fxsl:kb:icas-tiempo
nombre: icas-tiempo
version: 1.1.0
estado: publicado
descripcion: "Pieza 15 del ICAS-BoK: tiempo — behavior types, sheaves temporales, sheaves híbridos, contratos composicionales y delay aditivo; invariantes temporales, SLA, circuit breakers y event sourcing."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/15-tiempo.md (sha256:94f380b1bcfd1c227ac37c65907605a8d2a3c7f2ac480368eeff7324492ed30b) el 2026-06-12. Revisado contra Schultz-Spivak, Temporal Type Theory, arXiv:1710.10258. v1.1.0 (2026-07-18): delimita el framework y corrige SLA, circuit breaker, delays, event sourcing, deploys y cron."
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

Un SLA de uptime puede modelarse con ventanas, una medida sobre secciones y
operadores temporales. Identificar la obligacion con una modalidad concreta
requiere formalizar porcentaje, ventana movil y horizonte; `up` por si sola no
expresa 99.9%.

## Hybrid sheaves: cuando lo continuo se mezcla con lo discreto

Los sistemas reales no son puramente continuos ni puramente discretos. Un vuelo tiene modos -- taxiing, climbing, cruising, descending, landing -- cada uno con su propia dinamica continua (ecuaciones diferenciales que gobiernan altitud, velocidad, combustible). Las transiciones entre modos son eventos discretos.

Schultz y Spivak formalizan esto con los hybrid sheaves. Un hybrid datum es una tupla (C, D, src, tgt, tau) donde C es un tipo de comportamiento continuo, D es un tipo de transicion discreta, src y tgt asignan a cada transicion el comportamiento continuo de la izquierda y la derecha, y tau : D -> Time marca el instante de la transicion. El tipo hibrido de comportamiento Hyb(C, D) es el tipo de comportamientos que pueden tener finitamente muchas transiciones discretas intercaladas con periodos de dinamica continua.

La definicion es un pushout seguido de sheafificacion -- una construccion que usa los colimites y la topologia del topos B. Y la propiedad clave: una seccion de Hyb(C, D) esta "almost always" en la parte continua C. Las transiciones discretas son instantaneas -- duran exactamente cero tiempo.

Un circuit breaker puede **modelarse** como tipo hibrido tras especificar sus
conductas continuas/discretas y el dato hibrido. Tener estados open/closed y un
timeout no demuestra por si solo la construccion de pushout/sheafification.

## Delays: el morfismo que desplaza

Un delay de duracion D es un morfismo en B que desplaza el comportamiento por D unidades de tiempo. Formalmente, un par (a, a') : A x A es D-delayed si, para cada predicado phi sobre A y cada constante c de tipo C, la seccion a satisface phi en el intervalo [d,u] si y solo si a' satisface phi en el intervalo [d+D, u+D].

La definicion captura un delay constante idealizado. Latencia de red/Kafka es
variable, puede reordenar o perder mensajes y requiere un tipo probabilistico o
acotado mas rico.

Para delays puros constantes compuestos secuencialmente, el desplazamiento es
`D1+D2`. Esta ley no cubre concurrencia, colas o distribuciones de latencia.

## Systems, components y behavior contracts

En el framework, una machine relaciona un comportamiento total con puertos
tipados. Vincular esta definicion con polinomios/lentes exige un funtor o
equivalencia adicional; no se sigue solo de tener interfaz.

Pero ahora hay tiempo. El tipo total de comportamiento X no es un conjunto estatico de estados -- es un sheaf temporal. La machine no solo responde a inputs: se comporta a lo largo de duraciones. Y las propiedades que me importan son propiedades temporales: "la temperatura se mantiene entre 18 y 22 grados durante toda la operacion", no "la temperatura es 20 grados ahora."

Un contrato de comportamiento es un predicado temporal sobre los tipos de comportamiento de una interfaz. Es una proposicion en el lenguaje interno del topos B que dice que ciertas relaciones entre las variables del sistema se mantienen a lo largo del tiempo. El contrato se formula en contexto -- un juicio de tipo Gamma, donde Gamma nombra las variables de la interfaz.

Los resultados de composicionalidad del framework permiten derivar contratos
exteriores bajo hipotesis de tipado, totality/determinism y wiring. No basta que
cada componente satisfaga aisladamente un contrato informal.

## El National Airspace System

El caso de estudio canonico de Schultz y Spivak es el National Airspace System de la FAA. Aeronaves, sectores del espacio aereo, controladores -- cada uno con sus tipos de comportamiento, contratos y composicion.

Un avion tiene un tipo de comportamiento que incluye altitud, velocidad, rumbo, tasa de combustible -- todos variando continuamente con transiciones discretas (cambio de modo de vuelo). Un sector tiene contratos de separacion: dos aviones en el mismo sector deben mantener al menos 5 millas nauticas de distancia horizontal o 1000 pies de separacion vertical, en todo momento. Un controlador recibe senales de posicion con un delay D (la latencia del radar) y emite instrucciones que se ejecutan con otro delay D' (el tiempo de reaccion del piloto).

La propiedad de safe separation -- que ningun par de aviones viola la distancia minima -- se formula como una proposicion up sobre el tipo de comportamiento del sector completo. Y se puede probar combinando los contratos individuales de aviones y controladores con los delays del sistema de comunicacion y las dinamicas continuas de movimiento.

El caso NAS demuestra expresividad dentro del modelo de Temporal Type Theory.
Circuit breakers, SLAs o Kubernetes son aplicaciones candidatas que deben
formalizarse por separado.

## Todo converge aqui

Este es el ultimo documento conceptual del corpus, y no es accidental que sea el del tiempo. El tiempo es donde todo converge.

En Temporal Type Theory, un tipo de comportamiento es un sheaf sobre el site
temporal especificado por esa teoría. Polinomios, lenses, coálgebras, wiring
diagrams y pattern/matter pertenecen a otros formalismos citados: pueden
conectarse mediante construcciones explícitas, pero no convergen
automáticamente por compartir vocabulario de interfaces o tiempo.

Un event log puede modelarse como sheaf/presheaf de eventos por ventana si
restricciones y pegado se verifican. Restringir una ventana es el restriction
map; **replay** es un fold que reconstruye estado y no debe confundirse con
restriccion.

Migraciones secuenciales generan una categoria de caminos si se declaran
identidades/equivalencias. El hecho de que ocurran antes/despues no construye
un sheaf o categoria temporal mas rica.

Un blue/green deploy puede recibir un modelo hibrido si el switch y ambos
regimenes forman el dato requerido. Rate limiting si admite naturalmente un
predicado por ventanas. Periodicidad de cron requiere una condicion de
recurrencia/fase; no es solo aplicar `up`.

Temporal Type Theory aporta un modelo formal de comportamientos durativos. Su
uso fuera de los casos construidos conserva el estatuto de modelo hasta que se
definan site, sheaves, morphisms y contratos.

## Estatuto epistemico

- **Formal:** el framework de Schultz-Spivak dentro de su topos y axiomas.
- **Modelo:** NAS y cualquier sistema cuya traduccion al framework se
  construya.
- **Heuristica:** SLA, circuit breaker, Kafka, deploy o cron identificados con
  modalidades/sheaves sin esa traduccion.
