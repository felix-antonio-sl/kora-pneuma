---
urn: urn:fxsl:kb:icas-composicion-estructura
nombre: icas-composicion-estructura
version: 1.0.0
estado: publicado
descripcion: "Pieza 07 del ICAS-BoK: categorías monoidales, string diagrams, simetría, categorías cartesianas cerradas y Curry-Howard-Lambek — composición con paralelismo y currying."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/07-composicion-con-estructura.md (sha256:f560157e5a471f36cff6df75dff4019bb32e000b3f4ed848d085467b7fa12944) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [monoidal, string-diagram, tensor, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Composicion con estructura

## Cuando componer no basta

Hasta ahora tengo composicion secuencial: f despues de g, un morfismo tras otro. Eso basta para modelar pipelines lineales, pero la realidad que construyo todos los dias tiene otra dimension. Los pods de un deployment corren en paralelo. Los componentes de un frontend se renderizan lado a lado. Las capas de una red neuronal procesan tensores simultaneamente. El mundo real no es una linea -- es una red con flujo vertical y horizontal a la vez.

Necesito una categoria que sepa no solo componer en serie sino tambien en paralelo. Eso es exactamente lo que da una categoria monoidal: composicion con una nocion de "al lado de."

## Categorias monoidales: la estructura minima del paralelismo

Una categoria monoidal (C, tensor, I) equipa a una categoria C con un producto tensorial tensor : C x C -> C y un objeto unidad I, junto con isomorfismos naturales -- el associator alpha: (A tensor B) tensor C -> A tensor (B tensor C) y los unitors lambda: I tensor A -> A, rho: A tensor I -> A -- sujetos a la condicion de pentagono y la condicion de triangulo.

Perrone lo explica con una idea que captura la esencia: "una categoria monoidal es una categoria cuyos objetos y morfismos se pueden multiplicar de manera asociativa y unital, como en un monoide, pero solo up to isomorphism." Es un monoide categorificado.

El teorema de coherencia de Mac Lane es la razon por la que puedo ignorar los parentesis sin culpa. Dice que en una categoria monoidal, todo diagrama formal construido a partir de productos tensoriales, la unidad, associators y unitors conmuta automaticamente. En la practica esto significa que puedo trabajar como si la categoria fuera estricta -- como si (A tensor B) tensor C fuera literalmente igual a A tensor (B tensor C). Es la misma libertad que tengo cuando escribo `a + b + c` sin parentesis en cualquier lenguaje de programacion.

El ejemplo prototipico es (Set, x, 1): conjuntos con producto cartesiano y el singleton como unidad. El producto cartesiano es asociativo y unital solo up to isomorphism -- (A x B) x C no es el mismo conjunto que A x (B x C), pero hay una biyeccion canonica ((a,b),c) <-> (a,(b,c)).

El ejemplo no cartesiano mas importante es (Vect, tensor, R): espacios vectoriales con el producto tensorial usual. Aqui V tensor W no es V x W. El producto tensorial captura las funciones bilineales, no los pares. Esta distincion es la razon por la que las categorias monoidales generalizan mas alla de los productos categoricos.

## String diagrams: el lenguaje nativo

Los string diagrams son la notacion que cambia todo. En una categoria monoidal, puedo dibujar morfismos como cajas y objetos como cables. La composicion secuencial es apilar cajas de izquierda a derecha. El producto tensorial es yuxtaponer cables arriba y abajo. La identidad es un cable recto. La unidad monoidal es "no cable."

Perrone los define asi: cada objeto X se representa por un cable etiquetado X. Cada morfismo f : X -> Y es una caja con cable X entrando y cable Y saliendo. El tensor f tensor g se dibuja con f arriba y g abajo. Y la clave: los string diagrams son estrictamente asociativos y unitales -- no distinguen entre (f tensor g) tensor h y f tensor (g tensor h), justificado por el teorema de coherencia.

La interchange law -- (id_Y tensor g) . (f tensor id_A) = (f tensor id_B) . (id_X tensor g) = f tensor g -- se lee en string diagrams como una obviedad topologica: si dos cajas estan en cables distintos, no importa si las ejecuto primero una y despues la otra, o al reves. Son independientes. Es la misma intuicion que "f y g corren en threads distintos, el orden no importa."

Esto no es decorativo. Los string diagrams son un calculo riguroso. Toda ecuacion entre morfismos en una categoria monoidal corresponde a una deformacion continua de string diagrams. Es un lenguaje visual tan formal como el algebraico, pero que hace evidentes simetrias que las ecuaciones ocultan.

## Simetria, trenzas, y la jerarquia

La jerarquia de categorias monoidales es una escalera que agrega estructura paso a paso:

**Categoria monoidal** -- composicion paralela, asociativa y unital. No puedo intercambiar los factores del tensor.

**Braided monoidal** -- agrego un braiding beta: A tensor B -> B tensor A que satisface las condiciones de hexagono. Puedo cruzar cables, pero los cruces importan -- como trenzas fisicas que no se pueden deshacer.

**Symmetric monoidal** -- el braiding satisface la condicion de involutividad: beta_(B,A) . beta_(A,B) = id. Los cruces se cancelan. Es el caso de (Set, x, 1) donde el swap (a,b) <-> (b,a) compuesto consigo mismo da la identidad.

**Cartesian monoidal** -- el tensor es el producto categorico: el objeto terminal es la unidad, y hay proyecciones universales. En una categoria cartesiana monoidal, cada objeto es canonicamente un comonoid -- puedo copiar datos (comultiplicacion: diagonal A -> A x A) y descartar datos (counidad: A -> 1).

**Compact closed** -- cada objeto tiene un dual, con unidades y counidades (cups y caps) que permiten doblar cables. Aqui viven los circuitos, el algebra lineal como categoria, y el signal flow. Las estructuras de Frobenius suelen aparecer en este vecindario, pero no vienen incluidas por defecto solo por ser compact closed.

**Cartesian closed (CCC)** -- productos + exponenciales. Es la cumbre para la computacion funcional.

La proposicion de Perrone que mas impacto tiene en mi practica es esta: una categoria symmetric monoidal es cartesiana si y solo si cada objeto tiene una unica estructura de comonoid y cada morfismo es un morfismo de comonoids. Es decir, una categoria es cartesiana exactamente cuando todo se puede copiar y descartar. En un circuito cuantico no puedo copiar qubits (no-cloning theorem) -- eso es porque la categoria de Hilbert spaces con tensor product no es cartesiana.

## Monoids y comonoids internos

Un monoid interno en (C, tensor, I) es un objeto M equipado con una multiplicacion mu: M tensor M -> M y una unidad eta: I -> M que satisfacen asociatividad y unitalidad -- los mismos diagramas del monoide clasico, pero ahora dentro de la categoria.

La observacion clave de Perrone: "una monada es exactamente un monoid en la categoria monoidal de endofuntores ([C, C], compose, Id)." La unidad eta: Id -> T y la multiplicacion mu: T compose T -> T satisfacen las leyes de monoid. Esta es la famosa frase de Mac Lane: "a monad is just a monoid in the category of endofunctors." Guardo esta conexion para el documento 09, pero la raiz esta aqui.

Dualmente, un comonoid tiene comultiplicacion delta: W -> W tensor W (copiar) y counidad epsilon: W -> I (descartar). En una categoria cartesiana, cada objeto es un comonoid de manera unica -- la diagonal y la proyeccion terminal dan la estructura. Esto es lo que hace posible usar una variable mas de una vez en un lambda calculus: copiar es gratis. En una categoria monoidal general (como la de espacios vectoriales con tensor product), copiar no es gratis -- y esa restriccion genera la fisica cuantica y la criptografia.

## Categorias cartesianas cerradas y el trinity

Una CCC tiene tres ingredientes: objeto terminal, productos de cualquier par de objetos, y para cada par (A, B) un exponencial B^A (el internal hom [A, B]) con un morfismo de evaluacion:

```
eval : [A, B] x A -> B
```

y la propiedad universal de que para todo f : C x A -> B existe un unico curry(f) : C -> [A, B] tal que eval . (curry(f) x id_A) = f. Currying ES la adjuncion (- x A) ⊣ [A, -].

Cada lenguaje funcional tipado es el lenguaje interno de una CCC. Los tipos son objetos. Las funciones son morfismos. Las funciones de orden superior son exponenciales. Currying es la adjuncion CCC. Apply es eval.

```haskell
-- La CCC de Haskell
-- Objetos: tipos (Int, String, Bool, ...)
-- Morfismos: funciones (a -> b)
-- Producto: (a, b) con fst, snd
-- Exponencial: a -> b (el tipo funcion)
-- Evaluacion:
eval :: (a -> b, a) -> b
eval (f, x) = f x

-- Currying IS la adjuncion CCC:
curry :: ((a, b) -> c) -> a -> b -> c
uncurry :: (a -> b -> c) -> (a, b) -> c
```

El Curry-Howard-Lambek correspondence cierra el triangulo:

| Logica | Tipos | Categorias |
|--------|-------|------------|
| Proposicion | Tipo | Objeto |
| Prueba | Programa | Morfismo |
| Implicacion A => B | Funcion A -> B | Exponencial B^A |
| Conjuncion A and B | Par (A, B) | Producto A x B |
| Disjuncion A or B | Either A B | Coproducto A + B |
| Verdadero | | Objeto terminal 1 |
| Falso | Void | Objeto inicial 0 |
| Modus ponens | Aplicacion de funcion | eval |

Esto no es una analogia. Es una equivalencia formal. Toda CCC tiene un lambda calculus como lenguaje interno. Todo lambda calculus tipado simple determina una CCC. Toda logica proposicional intuicionista es el sistema de tipos de un lambda calculus, que es el lenguaje interno de una CCC. Tres mundos, un objeto matematico.

## Funtores monoidales: preservar la estructura paralela

Un functor lax-monoidal F : (C, tensor_C, I_C) -> (D, tensor_D, I_D) viene equipado con un mapa de unidad e : I_D -> F(I_C) y un mapa de multiplicacion nabla : F(A) tensor_D F(B) -> F(A tensor_C B), satisfaciendo condiciones de asociatividad y unitalidad. Es lax porque los mapas van en una direccion; colax va en la otra; strong cuando son isomorfismos.

La intuicion de Perrone es que un functor lax-monoidal captura "una nocion general de complejidad": combinar imagenes de partes puede ser mas complejo que la imagen del todo. El functor de probabilidad P es lax-monoidal: la distribucion producto P(X) x P(Y) -> P(X x Y) mapea un par de marginales a su distribucion conjunta independiente. La inversa no existe en general -- una distribucion conjunta tiene mas informacion que el par de marginales.

## En la practica

React puede leerse provechosamente con intuición monoidal. Un componente `<Header />` y un componente `<Sidebar />` se renderizan lado a lado bajo una operación de composición de vistas; el nesting de `children` funciona como composición secuencial. `<Fragment />` es un buen análogo informal de unidad. Lo que me interesa aquí no es afirmar que React venga ya dado como categoría monoidal estrictamente formalizada, sino que su semántica composicional se beneficia de ese lenguaje.

Kubernetes pods componen monoidalmente: multiples containers en un pod corren en paralelo compartiendo red y volumenes. El pod singleton es la unidad. La composicion secuencial es el pipeline de init containers seguido del container principal.

En redes neuronales, los string diagrams son la notacion natural. Cada capa es una caja. Los datos fluyen como cables. Una capa densa `Dense(784, 256)` seguida de `Dense(256, 10)` es composicion secuencial. Dos cabezas de atencion procesando en paralelo es tensor product. La concatenacion o suma de sus outputs es un morfismo de merge. Todo el diagrama de una arquitectura transformer es un string diagram en una categoria monoidal.

Signal flow graphs, como los formalizan Fong y Spivak, son morfismos en una categoria compact closed. Las matrices de n x m son morfismos de R^n a R^m. La composicion es multiplicacion de matrices. El tensor product es la suma directa. La compactness permite hacer feedback loops -- cables que van "hacia atras" -- que en una categoria meramente monoidal serian ilegales.

La jerarquia monoidal es, en el fondo, la jerarquia de cuanta libertad tengo para mover cables. En una categoria monoidal pura, los cables son rigidos. Con braiding puedo cruzarlos. Con simetria, los cruces se cancelan. Con compactness, los cables se doblan. Con cartesianidad, los cables se copian y se descartan. Cada nivel agrega una capacidad que desbloquea un nuevo dominio de ingenieria.
