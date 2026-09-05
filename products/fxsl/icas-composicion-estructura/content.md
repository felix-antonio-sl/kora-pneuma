---
urn: urn:fxsl:kb:icas-composicion-estructura
nombre: icas-composicion-estructura
version: 1.1.0
estado: publicado
descripcion: "Pieza 07 del ICAS-BoK: categorías monoidales, string diagrams, simetría, categorías cartesianas cerradas y Curry-Howard-Lambek — composición con paralelismo y currying."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/07-composicion-con-estructura.md (sha256:f560157e5a471f36cff6df75dff4019bb32e000b3f4ed848d085467b7fa12944) el 2026-06-12. v1.1.0 (2026-07-18): precisa coherencia, Curry-Howard-Lambek y separa modelos monoidales de React, Kubernetes y redes neuronales."
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

El teorema de coherencia de Mac Lane dice que los diagramas **canonicos** construidos con associators y unitors conmutan. Permite calcular mediante una estrictificacion coherente, sin convertir los objetos originales en literalmente iguales.

El ejemplo prototipico es (Set, x, 1): conjuntos con producto cartesiano y el singleton como unidad. El producto cartesiano es asociativo y unital solo up to isomorphism -- (A x B) x C no es el mismo conjunto que A x (B x C), pero hay una biyeccion canonica ((a,b),c) <-> (a,(b,c)).

El ejemplo no cartesiano mas importante es (Vect, tensor, R): espacios vectoriales con el producto tensorial usual. Aqui V tensor W no es V x W. El producto tensorial captura las funciones bilineales, no los pares. Esta distincion es la razon por la que las categorias monoidales generalizan mas alla de los productos categoricos.

## String diagrams: el lenguaje nativo

Los string diagrams son la notacion que cambia todo. En una categoria monoidal, puedo dibujar morfismos como cajas y objetos como cables. La composicion secuencial es apilar cajas de izquierda a derecha. El producto tensorial es yuxtaponer cables arriba y abajo. La identidad es un cable recto. La unidad monoidal es "no cable."

Perrone los define asi: cada objeto X se representa por un cable etiquetado X. Cada morfismo f : X -> Y es una caja con cable X entrando y cable Y saliendo. El tensor f tensor g se dibuja con f arriba y g abajo. Y la clave: los string diagrams son estrictamente asociativos y unitales -- no distinguen entre (f tensor g) tensor h y f tensor (g tensor h), justificado por el teorema de coherencia.

La interchange law se lee como mover cajas en cables separados. Interpretarla como threads independientes exige que efectos y recursos compartidos esten capturados por la categoria; el paralelismo operacional no se deduce del dibujo.

Los string diagrams forman un calculo riguroso, sound y completo para las ecuaciones generadas por la estructura monoidal apropiada (con las convenciones graficas correspondientes). Una ecuacion adicional del dominio no surge solo por deformacion.

## Simetria, trenzas, y la jerarquia

La jerarquia de categorias monoidales es una escalera que agrega estructura paso a paso:

**Categoria monoidal** -- composicion paralela, asociativa y unital. No puedo intercambiar los factores del tensor.

**Braided monoidal** -- agrego un braiding beta: A tensor B -> B tensor A que satisface las condiciones de hexagono. Puedo cruzar cables, pero los cruces importan -- como trenzas fisicas que no se pueden deshacer.

**Symmetric monoidal** -- el braiding satisface la condicion de involutividad: beta_(B,A) . beta_(A,B) = id. Los cruces se cancelan. Es el caso de (Set, x, 1) donde el swap (a,b) <-> (b,a) compuesto consigo mismo da la identidad.

**Cartesian monoidal** -- el tensor es el producto categorico: el objeto terminal es la unidad, y hay proyecciones universales. En una categoria cartesiana monoidal, cada objeto es canonicamente un comonoid -- puedo copiar datos (comultiplicacion: diagonal A -> A x A) y descartar datos (counidad: A -> 1).

**Compact closed** -- cada objeto tiene un dual, con unidades y counidades (cups y caps) que permiten doblar cables. Aqui viven los circuitos, el algebra lineal como categoria, y el signal flow. Las estructuras de Frobenius suelen aparecer en este vecindario, pero no vienen incluidas por defecto solo por ser compact closed.

**Cartesian closed (CCC)** -- productos finitos + exponenciales; es la estructura semantica del lambda calculo simplemente tipado con producto.

La proposicion de Perrone que mas impacto tiene en mi practica es esta: una categoria symmetric monoidal es cartesiana si y solo si cada objeto tiene una unica estructura de comonoid y cada morfismo es un morfismo de comonoids. Es decir, una categoria es cartesiana exactamente cuando todo se puede copiar y descartar. En un circuito cuantico no puedo copiar qubits (no-cloning theorem) -- eso es porque la categoria de Hilbert spaces con tensor product no es cartesiana.

## Monoids y comonoids internos

Un monoid interno en (C, tensor, I) es un objeto M equipado con una multiplicacion mu: M tensor M -> M y una unidad eta: I -> M que satisfacen asociatividad y unitalidad -- los mismos diagramas del monoide clasico, pero ahora dentro de la categoria.

La observacion clave de Perrone: "una monada es exactamente un monoid en la categoria monoidal de endofuntores ([C, C], compose, Id)." La unidad eta: Id -> T y la multiplicacion mu: T compose T -> T satisfacen las leyes de monoid. Esta es la famosa frase de Mac Lane: "a monad is just a monoid in the category of endofunctors." Guardo esta conexion para el documento 09, pero la raiz esta aqui.

Dualmente, un comonoid tiene comultiplicacion delta: W -> W tensor W (copiar) y counidad epsilon: W -> I (descartar). En una categoria cartesiana, cada objeto porta canonicamente esa estructura. En semanticas lineales/monoidales no cartesianas, copiar y descartar deben representarse explicitamente; esto es relevante, entre otros dominios, para informacion cuantica.

## Categorias cartesianas cerradas y el trinity

Una CCC tiene tres ingredientes: objeto terminal, productos de cualquier par de objetos, y para cada par (A, B) un exponencial B^A (el internal hom [A, B]) con un morfismo de evaluacion:

```
eval : [A, B] x A -> B
```

y la propiedad universal de que para todo f : C x A -> B existe un unico curry(f) : C -> [A, B] tal que eval . (curry(f) x id_A) = f. Currying ES la adjuncion (- x A) ⊣ [A, -].

El lambda calculo simplemente tipado total con productos tiene una categoria sintactica CCC, y las CCC le dan semantica. Lenguajes reales con recursion, `bottom` y efectos requieren estructura adicional; `Hask` no debe usarse sin esas salvedades como ejemplo matematico estricto.

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

Existe una correspondencia formal, bajo nociones apropiadas de equivalencia, entre CCC y lambda calculo simplemente tipado con producto/funcion. Para incluir disyuncion y falso se necesita estructura bicartesiana cerrada (coproductos finitos), y la logica intuicionista completa exige declarar el fragmento y la semantica exactos.

## Funtores monoidales: preservar la estructura paralela

Un functor lax-monoidal F : (C, tensor_C, I_C) -> (D, tensor_D, I_D) viene equipado con un mapa de unidad e : I_D -> F(I_C) y un mapa de multiplicacion nabla : F(A) tensor_D F(B) -> F(A tensor_C B), satisfaciendo condiciones de asociatividad y unitalidad. Es lax porque los mapas van en una direccion; colax va en la otra; strong cuando son isomorfismos.

La intuicion de Perrone es que un functor lax-monoidal captura "una nocion general de complejidad": combinar imagenes de partes puede ser mas complejo que la imagen del todo. El functor de probabilidad P es lax-monoidal: la distribucion producto P(X) x P(Y) -> P(X x Y) mapea un par de marginales a su distribucion conjunta independiente. La inversa no existe en general -- una distribucion conjunta tiene mas informacion que el par de marginales.

## En la practica

React puede leerse provechosamente con intuición monoidal. Un componente `<Header />` y un componente `<Sidebar />` se renderizan lado a lado bajo una operación de composición de vistas; el nesting de `children` funciona como composición secuencial. `<Fragment />` es un buen análogo informal de unidad. Lo que me interesa aquí no es afirmar que React venga ya dado como categoría monoidal estrictamente formalizada, sino que su semántica composicional se beneficia de ese lenguaje.

Kubernetes puede recibir un modelo monoidal de composicion paralela, pero debe definirse el tensor, su unidad (normalmente una configuracion vacia, no un pod singleton) y la semantica de recursos compartidos. Init containers aportan orden operacional, no prueban por si solos la estructura.

Las redes neuronales admiten formalizaciones por string diagrams cuando se elige una categoria de espacios/mapas y una operacion monoidal. Dibujar capas y cabezas como cajas/cables es una notacion candidata; "paralelo" no identifica automaticamente el tensor matematico.

Signal flow graphs, como los formalizan Fong y Spivak, son morfismos en una categoria compact closed. Las matrices de n x m son morfismos de R^n a R^m. La composicion es multiplicacion de matrices. El tensor product es la suma directa. La compactness permite hacer feedback loops -- cables que van "hacia atras" -- que en una categoria meramente monoidal serian ilegales.

La jerarquia monoidal es, en el fondo, la jerarquia de cuanta libertad tengo para mover cables. En una categoria monoidal pura, los cables son rigidos. Con braiding puedo cruzarlos. Con simetria, los cruces se cancelan. Con compactness, los cables se doblan. Con cartesianidad, los cables se copian y se descartan. Cada nivel agrega una capacidad que desbloquea un nuevo dominio de ingenieria.

## Estatuto epistemico

- **Formal:** categorias/funtores monoidales, coherencia, CCC y
  Curry-Howard-Lambek con sus hipotesis.
- **Modelo:** signal flow y calculos de redes cuando se declara la categoria.
- **Heuristica:** React, Kubernetes o "paralelismo = tensor" sin construccion
  ni leyes.
