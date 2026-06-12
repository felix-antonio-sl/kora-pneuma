---
urn: urn:fxsl:kb:icas-interaccion
nombre: icas-interaccion
version: 1.0.0
estado: publicado
descripcion: "Pieza 11 del ICAS-BoK: funtores polinomiales, lentes dependientes, comonoides y sistemas dinámicos — APIs como contratos bidireccionales e interacción por interfaces tipadas."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/11-interaccion.md (sha256:e7999114582ee8e0fb5ba06408acf71819c6b24bdc7c478226768da2a93f3b8f) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [polynomial, lente, sistema-dinamico, protocolo, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Interaccion

## El problema de la bidireccionalidad

En todos los documentos anteriores, los morfismos van en una direccion. Un funtor mapea de C a D (documento 02). Una transformacion natural va de F a G (documento 03). Una monada envuelve, una comonada desenvuelve (documento 09). Pero los sistemas reales que construyo son bidireccionales. Un servidor recibe requests y envia responses. Un smart contract lee estado y lo actualiza. Un protocolo tiene turnos: yo envio, tu respondes, yo respondo a tu respuesta.

Necesito una matematica de la interaccion -- no del flujo unidireccional, sino del dialogo. Los polynomial functors de Niu y Spivak son esa matematica. Son la teoria que toma en serio el hecho de que los sistemas tienen interfaces con entradas y salidas, y que la estructura de las entradas puede depender de las salidas observadas.

## Polynomial functors: la definicion

Un polynomial functor p : Set -> Set es una suma de representables:

p = Sigma_{i in p(1)} y^{p[i]}

donde y^A = Set(A, -) es el funtor representable. Evaluado en un conjunto X, da:

p(X) = Sigma_{i in p(1)} X^{p[i]}

Cada sumando es un producto indexado. El conjunto p(1) son las positions del polinomio, y para cada posicion i, el conjunto p[i] son las directions en esa posicion.

La terminologia posiciones/direcciones captura exactamente la nocion de interfaz. Las posiciones son los estados observables -- lo que el sistema muestra al exterior. Las direcciones son las opciones disponibles en cada estado -- lo que el exterior puede enviar al sistema. Un polinomio es un menu dependiente: primero observas la posicion, y segun lo que ves, eliges entre las direcciones disponibles.

El ejemplo mas simple: y^A tiene una posicion y A direcciones. Es una caja negra que siempre muestra la misma cara pero acepta A posibles entradas. El polinomio constante n (= n * y^0) tiene n posiciones y ninguna direccion en ninguna. Es un display: muestra una de n cosas pero no acepta input. El polinomio lineal n*y tiene n posiciones y exactamente una direccion en cada una: recibes un dato sin poder influir en que dato recibes. El polinomio identidad y tiene una posicion y una direccion: es el canal transparente que transmite sin modificar.

## REST APIs como polinomios

Puedo modelar una REST API como un polinomio. Las posiciones son los endpoints -- los recursos que la API expone. Las direcciones en cada posicion son los parametros que ese endpoint acepta.

Un endpoint GET /users/{id} tiene una posicion (el recurso "user detail") y su conjunto de direcciones es el conjunto de IDs validos. Un endpoint GET /users con query params tiene una posicion y sus direcciones son las combinaciones posibles de filtros (page, limit, sort, filter).

La API completa es el coproducto (suma) de los polinomios de cada endpoint:

API = Sigma_{e in Endpoints} y^{Params(e)}

Esto es exactamente un polinomio. Y la evaluacion API(X) me da, para cada endpoint y cada funcion de sus parametros a X, un posible resultado -- la semantica del endpoint como functor.

## Lentes dependientes: morfismos en Poly

Un dependent lens f : p -> q entre polinomios consiste en:

- Una funcion on-positions f_1 : p(1) -> q(1) -- mapea posiciones de p a posiciones de q.
- Para cada posicion i in p(1), una funcion on-directions f^sharp_i : q[f_1(i)] -> p[i] -- mapea direcciones de q de vuelta a direcciones de p.

La bidireccionalidad es esencial: las posiciones van hacia adelante (de p a q) y las direcciones van hacia atras (de q a p). Es como un contrato: "yo te muestro mi posicion traducida, tu me envias tu direccion, y yo la traduzco de vuelta a mi lenguaje."

Esta es la misma estructura que las lenses de la programacion funcional: un getter que va hacia adelante (leer una parte de un todo) y un setter que va hacia atras (actualizar la parte dentro del todo). Pero las lenses polinomiales son dependientes -- la funcion backward depende de la posicion. Es la generalizacion que necesito para modelar sistemas donde la interfaz de entrada depende del estado actual.

Los morfismos en la categoria Poly componen de la manera esperada: las funciones on-positions se componen hacia adelante, y las funciones on-directions se componen hacia atras. La identidad tiene f_1 = id y f^sharp = id. La verificacion de que esto forma una categoria es directa.

## Tres productos monoidales

La categoria Poly tiene una riqueza inusual de estructura monoidal. Tres productos monoidales distintos capturan tres modos fundamentales de combinar sistemas:

**Producto cartesiano (x)**: posiciones se multiplican, direcciones se suman. Para p x q, una posicion es un par (i, j) y las direcciones son p[i] + q[j]. Cada sistema elige independientemente su posicion, y el exterior puede enviar input a cualquiera de los dos. Es la composicion paralela donde ambos sistemas corren independientemente y cualquiera puede recibir input. La unidad es el polinomio constante 1, es decir `y^0`. Con este producto, la categoria de polinomios se comporta como el entorno cartesiano natural para hablar de interfaces independientes.

**Producto Dirichlet (tensor)**: posiciones se multiplican, direcciones se multiplican. Para p tensor q, una posicion es un par (i, j) y las direcciones son p[i] x q[j]. Ambos sistemas operan en paralelo y el exterior debe enviar input a ambos simultaneamente. Es la composicion paralela sincronizada. La unidad es y.

**Producto de composicion (triangleleft)**: es la composicion de polinomios como funtores. Para p triangleleft q, las posiciones son pares de una posicion i de p y una funcion que asigna a cada direccion de p una posicion de q. Las direcciones son productos de direcciones de q. Es la composicion secuencial de protocolos: primero p muestra su posicion, el exterior elige una direccion, eso determina que instancia de q se activa, q muestra su posicion, el exterior elige una direccion de q, y asi. La unidad es y (el canal identidad).

El producto triangleleft captura los protocolos de interaccion. Un protocolo request-response es p triangleleft q donde p es el paso de request (posiciones = tipos de request, direcciones = parametros) y q es el paso de response (posiciones = tipos de response, direcciones = confirmaciones).

## Sistemas dinamicos como lentes

La conexion mas poderosa de Poly con la practica es la modelacion de sistemas dinamicos. Un sistema dinamico con estados S e interfaz p es una lente:

phi : S*y^S -> p

Donde S*y^S es el monomial con S posiciones (los estados posibles) y S direcciones en cada posicion (el proximo estado). La lente tiene:

- phi_1 : S -> p(1) -- el output function: dado el estado actual, que posicion muestra al exterior.
- phi^sharp_s : p[phi_1(s)] -> S -- el update function: dado el estado actual y la direccion elegida por el exterior, cual es el proximo estado.

Es exactamente una Moore machine: el output depende solo del estado, y la transicion depende del estado y el input. Un automata determinista con estados S, alfabeto A, y estados de aceptacion F es una lente S*y^S -> 2*y^A, donde 2 = {accept, reject} y la funcion on-positions indica aceptacion.

En Redux (o cualquier store de estado), el store se deja modelar muy bien con esta lente. El estado S es el state tree. Las posiciones p(1) son los posibles renders (lo que la UI muestra). Las direcciones p[i] son las acciones disponibles en cada estado de la UI. La funcion on-positions es el selector (state -> view). La funcion on-directions es el reducer (state, action) -> state.

## Comonoids en Poly son categorias

El resultado mas profundo de Poly, demostrado por Ahman y Uustalu (2016) y desarrollado extensamente por Niu y Spivak, es que los comonoids en (Poly, y, triangleleft) son exactamente las categorias pequenas.

Un comonoid en Poly respecto al producto de composicion triangleleft es un polinomio p equipado con:

- Counit epsilon : p -> y -- la identidad.
- Comultiplication delta : p -> p triangleleft p -- la composicion.

satisfaciendo coasociatividad y counitalidad.

Cuando decodifico esto, las posiciones de p son los objetos de una categoria, las direcciones p[i] son los morfismos que salen de i, la counit selecciona la identidad en cada posicion, y la comultiplicacion descompone cada morfismo en un par composable.

Este resultado es profundo porque conecta dos mundos que parecian separados: la teoria de polinomios (algebraica, combinatoria) y la teoria de categorias (composicional, abstracta). Bajo la identificacion de Ahman-Uustalu, dar una categoria pequena equivale a dar cierto comonoid polinomial, y viceversa. Los funtores entre categorias corresponden a cierto tipo de morfismos entre comonoids.

Los retrofunctors -- morfismos de comonoids en Poly -- son una generalizacion de los funtores ordinarios. Un retrofunctor F : C -> D tiene una funcion on-objects F_1 que va hacia adelante, y funciones on-morphisms F^sharp que van hacia atras: dado un morfismo en D que sale de F(i), produce un morfismo en C que sale de i. Es un funtor que "levanta" morfismos del codominio al dominio, preservando identidades y composicion.

## Optics: acceso bidireccional generalizado

Las lentes polinomiales se generalizan a optics, que son la familia completa de patrones de acceso bidireccional: lenses (acceso a partes de un producto), prisms (acceso a ramas de un coproducto), traversals (acceso a multiples elementos), isos (acceso por isomorfismo).

Cada tipo de optic corresponde a una eleccion de estructura monoidal en la que se descompone el tipo de datos:

- Lens: descomposicion como producto A = B x C.
- Prism: descomposicion como coproducto A = B + C.
- Affine: descomposicion como B + B x C.
- Traversal: descomposicion via funtores aplicativos.

En la practica, los CRDTs (Conflict-free Replicated Data Types) pueden modelarse como optics: cada replica tiene una lens sobre el estado global, las actualizaciones van hacia atras (merge), y la consistencia eventual se garantiza porque los merges son commutativos e idempotentes -- propiedades que se expresan como condiciones sobre las optics.

Los WebSockets, que son channels bidireccionales con estado, se modelan directamente como dynamical systems en Poly. El estado del servidor es S, la interfaz del WebSocket es un polinomio con posiciones (mensajes que el servidor puede enviar) y direcciones (mensajes que el cliente puede enviar). El protocolo completo -- handshake, intercambio de mensajes, cierre -- es una composicion triangleleft de las fases.

## Smart contracts como lentes

Un smart contract en una blockchain es una lente particularmente limpia. El estado S es el estado del contrato (balances, mappings, variables). La interfaz es un polinomio donde las posiciones son las lecturas publicas (balanceOf, totalSupply) y las direcciones son las transacciones posibles (transfer, approve, mint).

La lente phi : S*y^S -> p dice: dado el estado actual, que puedo leer (phi_1), y dado el estado actual y una transaccion, cual es el nuevo estado (phi^sharp). La composabilidad de lentes significa que puedo componer contratos: el output de uno alimenta el input de otro, y las actualizaciones de estado se propagan hacia atras por la cadena.

La invariante de un contrato (por ejemplo, "la suma de balances es constante") es una condicion sobre la lente: para todo estado s y toda transaccion d, si s satisface el invariante, entonces phi^sharp(s, d) tambien lo satisface.

## Computational tools

Catlab.jl (en Julia) implementa categorias computacionales usando la teoria de polinomios como backend algebraico. AlgebraicJulia proporciona herramientas para definir polinomios, calcular sus productos monoidales, y simular dynamical systems como lentes. En Haskell, la libreria `optics` implementa la jerarquia completa de optics basada en la teoria de profunctors, que es la version enriquecida de la misma idea.

El hecho de que las herramientas computacionales existan y sean usables es importante: la teoria de polinomios no es especulacion matematica. Es una infraestructura para el diseño de sistemas interactivos, con implementaciones funcionales que permiten modelar, componer, y verificar protocolos, interfaces, y maquinas de estado.

## El patron de la interaccion

La leccion central de Poly es que la interaccion no es un accidente que se agrega a la teoria de categorias -- es una estructura que emerge de la composicion de polinomios. Las posiciones son lo que muestras. Las direcciones son lo que aceptas. Las lentes son los contratos entre sistemas. Los tres productos monoidales capturan los tres modos de composicion: independiente (x), sincronizado (tensor), secuencial (triangleleft).

Y el resultado de Ahman-Uustalu cierra el circulo: las categorias mismas -- la estructura fundamental de toda la teoria -- admiten una presentacion como comonoids polinomiales. La composicion de morfismos se refleja como comultiplicacion y la identidad como counidad. La teoria de categorias se refleja dentro de Poly como una estructura algebraica particular. No necesito venderlo como slogan ontologico; me basta con la equivalencia estructural que el resultado establece.

En mi practica diaria, esto cambia como pienso sobre APIs, protocolos, y sistemas de estado. No son entidades ad hoc con contratos informales. Son polinomios con estructura monoidal precisa, y sus composiciones estan garantizadas por la teoria. Cuando compongo dos microservicios, estoy componiendo lentes. Cuando diseño un protocolo multi-fase, estoy construyendo un producto triangleleft. Y cuando verifico que un contrato preserva sus invariantes, estoy probando que una lente respeta la estructura del comonoid subyacente.
