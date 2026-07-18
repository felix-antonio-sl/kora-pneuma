---
urn: urn:fxsl:kb:icas-interaccion
nombre: icas-interaccion
version: 1.1.0
estado: publicado
descripcion: "Pieza 11 del ICAS-BoK: funtores polinomiales, lentes dependientes, comonoides y sistemas dinámicos — APIs como contratos bidireccionales e interacción por interfaces tipadas."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/11-interaccion.md (sha256:e7999114582ee8e0fb5ba06408acf71819c6b24bdc7c478226768da2a93f3b8f) el 2026-06-12. v1.1.0 (2026-07-18): conserva el nucleo formal de Poly y degrada REST, Redux, CRDT, WebSocket y smart contracts a modelos bajo hipotesis."
autor: FS
creado: 2026-04-14
lang: es
tags: [polynomial, lente, sistema-dinamico, protocolo, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Interaccion

## El problema de la bidireccionalidad

En todos los documentos anteriores, los morfismos van en una direccion. Un funtor mapea de C a D (documento 02). Una transformacion natural va de F a G (documento 03). Una monada envuelve, una comonada desenvuelve (documento 09). Pero los sistemas reales que construyo son bidireccionales. Un servidor recibe requests y envia responses. Un smart contract lee estado y lo actualiza. Un protocolo tiene turnos: yo envio, tu respondes, yo respondo a tu respuesta.

Los funtores polinomiales y lentes dependientes proporcionan **una** matematica
de interfaces interactivas; no son la unica ni todo protocolo real cabe en
`Poly`.

## Polynomial functors: la definicion

Un polynomial functor p : Set -> Set es una suma de representables:

p = Sigma_{i in p(1)} y^{p[i]}

donde y^A = Set(A, -) es el funtor representable. Evaluado en un conjunto X, da:

p(X) = Sigma_{i in p(1)} X^{p[i]}

Cada sumando es un producto indexado. El conjunto p(1) son las positions del polinomio, y para cada posicion i, el conjunto p[i] son las directions en esa posicion.

Posiciones/direcciones admiten la lectura de output/input dependiente. Es una
interpretacion formal del polinomio, pero demostrar que captura una interfaz
real exige especificar sus estados, errores, efectos y temporalidad.

El ejemplo mas simple: y^A tiene una posicion y A direcciones. Es una caja negra que siempre muestra la misma cara pero acepta A posibles entradas. El polinomio constante n (= n * y^0) tiene n posiciones y ninguna direccion en ninguna. Es un display: muestra una de n cosas pero no acepta input. El polinomio lineal n*y tiene n posiciones y exactamente una direccion en cada una: recibes un dato sin poder influir en que dato recibes. El polinomio identidad y tiene una posicion y una direccion: es el canal transparente que transmite sin modificar.

## REST APIs como polinomios

Puedo modelar una REST API como un polinomio. Las posiciones son los endpoints -- los recursos que la API expone. Las direcciones en cada posicion son los parametros que ese endpoint acepta.

Un endpoint GET /users/{id} tiene una posicion (el recurso "user detail") y su conjunto de direcciones es el conjunto de IDs validos. Un endpoint GET /users con query params tiene una posicion y sus direcciones son las combinaciones posibles de filtros (page, limit, sort, filter).

La API completa es el coproducto (suma) de los polinomios de cada endpoint:

API = Sigma_{e in Endpoints} y^{Params(e)}

La signatura `Σ_e y^{Params(e)}` es un polinomio y `API(X)` parametriza una
eleccion de endpoint junto con una funcion de sus parametros a X. Modela
**handlers posibles**, no aporta por si sola la semantica HTTP, responses,
errores, autenticacion o efectos.

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

Redux puede modelarse con una lente dinamica si se tipan vistas, acciones
dependientes y reducer total. Efectos, middleware y acciones asincronas
requieren ampliar el modelo.

## Comonoids en Poly son categorias

El resultado mas profundo de Poly, demostrado por Ahman y Uustalu (2016) y desarrollado extensamente por Niu y Spivak, es que los comonoids en (Poly, y, triangleleft) son exactamente las categorias pequenas.

Un comonoid en Poly respecto al producto de composicion triangleleft es un polinomio p equipado con:

- Counit epsilon : p -> y -- la identidad.
- Comultiplication delta : p -> p triangleleft p -- la composicion.

satisfaciendo coasociatividad y counitalidad.

Cuando decodifico esto, las posiciones de p son los objetos de una categoria, las direcciones p[i] son los morfismos que salen de i, la counit selecciona la identidad en cada posicion, y la comultiplicacion descompone cada morfismo en un par composable.

Este resultado es profundo porque conecta dos mundos que parecian separados: la teoria de polinomios (algebraica, combinatoria) y la teoria de categorias (composicional, abstracta). Bajo la identificacion de Ahman-Uustalu, dar una categoria pequena equivale a dar cierto comonoid polinomial, y viceversa. Los funtores entre categorias corresponden a cierto tipo de morfismos entre comonoids.

Los retrofunctors —ciertos morfismos de comonoids en `Poly`— tienen mapa de
objetos hacia adelante y levantamiento de flechas salientes hacia atrás,
preservando las leyes correspondientes. No son funtores ordinarios: la
dirección de su acción sobre flechas es parte esencial de la estructura.

## Optics: acceso bidireccional generalizado

Las lentes polinomiales se generalizan a optics, que son la familia completa de patrones de acceso bidireccional: lenses (acceso a partes de un producto), prisms (acceso a ramas de un coproducto), traversals (acceso a multiples elementos), isos (acceso por isomorfismo).

Cada tipo de optic corresponde a una eleccion de estructura monoidal en la que se descompone el tipo de datos:

- Lens: descomposicion como producto A = B x C.
- Prism: descomposicion como coproducto A = B + C.
- Affine: descomposicion como B + B x C.
- Traversal: descomposicion via funtores aplicativos.

Algunos CRDTs pueden integrarse en modelos de optics, pero consistencia
eventual proviene de las leyes algebraicas y supuestos de entrega del CRDT
(por ejemplo, join-semilattice/merge), no de ser una optic.

Un WebSocket puede recibir un modelo dinamico en `Poly` si mensajes, estados y
fases forman los polinomios/lentes declarados. Handshake, errores,
concurrencia y cierre no quedan formalizados automaticamente.

## Smart contracts como lentes

Un smart contract determinista puede modelarse como lente sobre estado e
interfaz. Reverts, gas, llamadas externas, concurrencia de transacciones y
semantica de cadena deben entrar al tipo para obtener garantias.

La lente describe output y update dentro del modelo. Componer contratos reales
requiere ademas que sus interfaces tengan los tipos compatibles y que efectos
de ejecucion/reentrada esten representados.

La invariante de un contrato (por ejemplo, "la suma de balances es constante") es una condicion sobre la lente: para todo estado s y toda transaccion d, si s satisface el invariante, entonces phi^sharp(s, d) tambien lo satisface.

## Computational tools

El ecosistema AlgebraicJulia/Catlab implementa numerosas construcciones
categoriales y existen librerias especificas para dinamica/polinomios; no debe
inferirse que Poly sea el backend de todo Catlab. Las optics de Haskell por
profunctores estan relacionadas, pero no son simplemente "la version
enriquecida" de lentes polinomiales.

La teoria de polinomios es matematica formal con implementaciones
computacionales. Que una herramienta calcule composiciones no verifica
automaticamente que un protocolo real corresponda al modelo ni que sus
invariantes se conserven.

## El patron de la interaccion

La leccion central de Poly es que la interaccion no es un accidente que se agrega a la teoria de categorias -- es una estructura que emerge de la composicion de polinomios. Las posiciones son lo que muestras. Las direcciones son lo que aceptas. Las lentes son los contratos entre sistemas. Los tres productos monoidales capturan los tres modos de composicion: independiente (x), sincronizado (tensor), secuencial (triangleleft).

Y el resultado de Ahman-Uustalu cierra el circulo: las categorias mismas -- la estructura fundamental de toda la teoria -- admiten una presentacion como comonoids polinomiales. La composicion de morfismos se refleja como comultiplicacion y la identidad como counidad. La teoria de categorias se refleja dentro de Poly como una estructura algebraica particular. No necesito venderlo como slogan ontologico; me basta con la equivalencia estructural que el resultado establece.

APIs, protocolos y sistemas de estado **pueden** formalizarse en `Poly`. Solo
despues de construir los polinomios/lentes y comprobar los tipos, componer
microservicios corresponde a componer lentes o un protocolo a
`triangleleft`. La preservacion de invariantes sigue necesitando prueba.

## Estatuto epistemico

- **Formal:** polinomios, lentes cartesianas/dependientes, productos
  monoidales y comonoides en `Poly`.
- **Modelo:** maquinas de Moore y los casos de software cuando se tipan.
- **Heuristica:** identificar directamente APIs, CRDTs, WebSockets o contratos
  con lentes sin representar sus efectos y leyes.
