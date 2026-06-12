---
urn: urn:fxsl:kb:icas-efectos
nombre: icas-efectos
version: 1.0.0
estado: publicado
descripcion: "Pieza 09 del ICAS-BoK: efectos — mónadas, Kleisli, Eilenberg-Moore, comónadas, coálgebras, bisimulación y leyes distributivas; componer computación con efectos y observar comportamiento."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/09-efectos.md (sha256:67dd42843b739c2db94b89c00b5321fe0d43b634c3fcd46a9ac0fe7fd53f46fb) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [monada, kleisli, coalgebra, bisimulacion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Efectos

## El problema de las funciones que mienten

Una funcion `f : A -> B` promete que dado un valor de tipo A produce un valor de tipo B. Pero en la practica, las funciones que escribo todos los dias hacen mucho mas que eso. Leen configuracion. Escriben logs. Fallan con excepciones. Producen multiples resultados. Modifican estado. Lanzan operaciones asincronas. La firma de tipos dice una cosa; el comportamiento dice otra.

La solucion no es eliminar los efectos -- un programa sin efectos no puede ni imprimir "hola mundo." La solucion es hacerlos explicitos en el sistema de tipos. Y la estructura matematica que hace posible componer funciones con efectos explicitos es la monada.

## Monada: un monoid en la categoria de endofuntores

Ya vi en el documento 07 que la categoria de endofuntores [C, C] tiene una estructura monoidal estricta: el tensor es la composicion de funtores y la unidad es el funtor identidad Id. Una monada es exactamente un monoid interno en esa categoria.

Concretamente, una monada sobre C es un endofuntor T : C -> C junto con dos transformaciones naturales:

- **unit** eta : Id => T (meter un valor en el contexto monadico)
- **multiplication** mu : T . T => T (aplanar dos capas de efecto en una)

sujetas a tres leyes:

```
mu . T(mu) = mu . mu_T -- asociatividad
mu . T(eta) = id -- unidad derecha
mu . eta_T = id -- unidad izquierda
```

Perrone lo ilustra con el power set monad P en Set. El unit sigma_X : X -> PX envuelve cada elemento en su singleton: x |-> {x}. La multiplicacion union_X : PPX -> PX aplana un conjunto de conjuntos tomando la union. Las leyes de monada son las leyes de la union: union de uniones es asociativa, y la union de singletons da el conjunto original.

La conexion con adjunciones, que ya explore en el documento 06, es directa: toda adjuncion F ⊣ G genera una monada T = G . F con unit eta y multiplication G(epsilon_F), donde epsilon es la counit de la adjuncion. La adjuncion producto-exponencial (- x A) ⊣ [A, -] genera la state monad S -> (-, S). La pregunta inversa -- ¿toda monada proviene de una adjuncion? -- tiene respuesta positiva, y las dos adjunciones canonicas son la de Kleisli y la de Eilenberg-Moore.

## La categoria de Kleisli: componer funciones con efectos

Dada una monada T en C, la categoria de Kleisli Kl(T) tiene los mismos objetos que C pero sus morfismos son "Kleisli arrows": un morfismo de A a B en Kl(T) es un morfismo A -> TB en C. La composicion de Kleisli de k : A -> TB y h : B -> TC es:

```
h .kl k = mu_C . T(h) . k : A -> TC
```

Primero aplico k para obtener un TB, luego levanto h con T para obtener T(TC), y finalmente aplano con mu. La identidad de Kleisli en A es eta_A : A -> TA.

En Haskell, la composicion Kleisli es el fish operator:

```haskell
(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> (a -> m c)
f >=> g = \a -> f a >>= g

-- equivalentemente, con bind:
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

Las leyes de la monada se vuelven las leyes de una categoria:

```haskell
return >=> f = f -- identidad izquierda
f >=> return = f -- identidad derecha
(f >=> g) >=> h = f >=> (g >=> h) -- asociatividad
```

Esto es lo fundamental: la monada no es sobre efectos. La monada es sobre composicion. Los efectos son lo que permite componer.

## Catalogo de monadas concretas

Cada monada captura un patron de efecto distinto. Los reconozco porque los uso todos los dias:

```haskell
-- Parcialidad: el computo puede fallar
-- Maybe a = Nothing | Just a
instance Monad Maybe where
 Nothing >>= f = Nothing
 Just x >>= f = f x

-- No-determinismo: multiples resultados
-- [a] = [] | a : [a]
instance Monad [] where
 xs >>= f = concatMap f xs

-- Estado mutable: lectura y escritura
-- State s a = s -> (a, s)
instance Monad (State s) where
 m >>= f = \s -> let (a, s') = m s in f a s'

-- Configuracion: lectura de entorno
-- Reader r a = r -> a
instance Monad (Reader r) where
 m >>= f = \r -> f (m r) r

-- Logging: acumular un monoide
-- Writer w a = (a, w)
instance Monad (Writer w) where
 (a, w) >>= f = let (b, w') = f a in (b, w <> w')

-- Errores tipados: fallo con informacion
-- Either e a = Left e | Right a
instance Monad (Either e) where
 Left e >>= f = Left e
 Right a >>= f = f a

-- Efectos del mundo real
-- IO a: la monada que encapsula todo side effect
```

En TypeScript, las Promises son una monada. `Promise.resolve(x)` es return. `.then(f)` es bind. La asincronia es el efecto. La composicion `.then(f).then(g)` es composicion Kleisli.

## Algebras de Eilenberg-Moore: los objetos que absorben efectos

La otra adjuncion canonica genera la categoria de Eilenberg-Moore C^T. Un T-algebra es un par (A, alg) donde alg : TA -> A es un "evaluador" que satisface:

```
alg . eta_A = id_A -- evaluar un valor trivial da el valor
alg . mu_A = alg . T(alg) -- evaluar un efecto anidado da lo mismo
 -- que evaluar el efecto interno y luego el externo
```

Milewski lo ilustra con la monada lista. Una algebra para la lista es un tipo A con una funcion `[A] -> A` que es asociativa y tiene unidad -- un fold. Las algebras de la monada lista son exactamente los monoids. Mas generalmente, las algebras de la monada libre sobre una signatura algebrica son exactamente los modelos de esa signatura.

La diferencia entre Kleisli y Eilenberg-Moore es la diferencia entre construir expresiones y evaluarlas. Los Kleisli arrows construyen expresiones con efectos. Las algebras las evaluan.

## Comonadas: computacion en contexto

Dualmente, una comonada W en C tiene:

- **counit** epsilon : W => Id (extraer el valor actual)
- **comultiplication** delta : W => W . W (expandir el contexto)

con las leyes duales. Si la monada dice "puedo meter un valor en un contexto pero no sacarlo," la comonada dice "puedo extraer un valor del contexto pero no meterlo." Una monada produce valores envueltos en estructura. Una comonada consume estructura para producir valores.

```haskell
class Functor w => Comonad w where
 extract :: w a -> a
 duplicate :: w a -> w (w a)
 extend :: (w a -> b) -> w a -> w b
 extend f = fmap f . duplicate
```

El producto comonad `Product e a = (e, a)` es el dual del reader monad. Un co-Kleisli arrow `(e, a) -> b` es una funcion que computa en un entorno. Extract ignora el entorno. Duplicate duplica el entorno para sub-computaciones.

El stream comonad es el ejemplo que mas ilumina:

```haskell
data Stream a = Cons a (Stream a)

instance Comonad Stream where
 extract (Cons a _) = a -- el valor actual
 duplicate (Cons a as) = Cons (Cons a as) (duplicate as) -- todos los shifts
```

Duplicate produce un stream de streams, cada uno enfocado en una posicion distinta. Extend aplica una funcion a cada posicion con todo su contexto. Es exactamente el patron de Conway's Game of Life: cada celda computa su proximo estado mirando sus vecinos.

En React, los hooks exhiben una estructura analogica a las comonadas. Un componente `(props, state) -> JSX` tiene la forma de un co-Kleisli arrow. `useContext`, `useState`, `useEffect` proporcionan el contexto extendido. El componente extrae su render del contexto completo. El re-render se asemeja a extend: "re-computa el output para cada posible estado." La analogia es estructural, no una instancia formal de Comonad -- React no implementa las leyes comonadicas -- pero ilumina por que la composicion de hooks sigue los mismos patrones.

## Coalgebras: la mirada desde afuera

Mientras las algebras deconstruyen (evaluan estructura), las coalgebras construyen (generan comportamiento). Una F-coalgebra es un par (U, alpha) donde alpha : U -> F(U) -- un estado produce una observacion estructurada.

Barbosa lo dice con precision: "coalgebra invierte la flecha del algebra. En lugar de especificar como ensamblar un valor a partir de sus componentes, especifica como descomponer un estado en sus observables."

El funtor F es la forma de la observacion -- el interface functor. Determina que puedo ver del sistema:

- F(X) = A x X: un sistema que produce un output A y transiciona a un nuevo estado. Es un stream, un automata de Moore.
- F(X) = 1 + A x X: parcialidad -- la observacion puede terminar o seguir. Es una lista posiblemente finita.
- F(X) = P(X): no-determinismo -- multiples estados sucesores. Es un sistema de transiciones.
- F(X) = (X)^A x B: recibo input A, produzco output B, cambio estado. Es un automata de Mealy.

## Coalgebra final y anamorfismos

La coalgebra final nu(F) para un funtor F es el espacio de todos los posibles comportamientos F-observables. Lambek's lemma dice que la coalgebra final es un fixed point: nu(F) es isomorfo a F(nu(F)).

El anamorphismo (unfold) es el unico morfismo de cualquier coalgebra a la coalgebra final:

```haskell
ana :: Functor f => (a -> f a) -> a -> Fix f
ana coalg = Fix . fmap (ana coalg) . coalg
```

Es el dual del catamorfismo (fold). Un catamorfismo consume una estructura inductiva; un anamorfismo genera una estructura coinductiva.

La criba de Eratostenes es un anamorphismo canonico:

```haskell
era :: [Int] -> StreamF Int [Int]
era (p : ns) = StreamF p (filter (\n -> n `mod` p /= 0) ns)

primes = ana era [2..] -- stream infinito de primos
```

Event sourcing es anamorfismo. Dado un estado inicial y una funcion de transicion `State -> Event x State`, el unfold genera la secuencia infinita de eventos. El estado es el carrier de la coalgebra. Los eventos son las observaciones. La funcion de transicion es la estructura coalgebraica.

## Bisimulacion: equivalencia observacional

Barbosa define la equivalencia observacional de dos estados u en U y v en V como la igualdad de sus comportamientos en la coalgebra final: u equiv v si y solo si [p](u) = [q](v), donde [p] y [q] son los unicos morfismos a la coalgebra final.

Pero la bisimulacion ofrece un criterio mas constructivo. Una bisimulacion entre dos coalgebras p : U -> F(U) y q : V -> F(V) es una relacion R en U x V que se levanta a traves de F: si (u, v) esta en R, entonces (pu, qv) esta en F-bar(R), el lifting de la relacion a traves del funtor.

Para automatas deterministas, bisimulacion dice: dos estados son bisimilares si producen el mismo output y sus sucesores siguen siendo bisimilares. Para sistemas con no-determinismo, la definicion se adapta al funtor correspondiente.

La aplicacion directa en mi practica: dos microservicios son intercambiables si son bisimilares. No me importa su implementacion interna -- solo que ante las mismas observaciones (requests) producen las mismas respuestas y transicionan a estados que siguen siendo bisimilares. Una bisimulacion es un contrato de equivalencia comportamental.

Cuando hago blue-green deployment, estoy afirmando una bisimulacion: el servicio nuevo y el viejo son observacionalmente equivalentes para el load balancer. Cuando escribo tests de integracion que comparan las respuestas de dos implementaciones, estoy construyendo la bisimulacion explicitamente.

## Leyes distributivas: cuando los efectos componen

No todas las monadas componen. Dadas dos monadas S y T en la misma categoria, la composicion S . T no necesariamente es una monada. Para que lo sea, necesito una ley distributiva lambda : S . T => T . S -- una transformacion natural que "intercambia" las capas de efecto de manera coherente con las unidades y multiplicaciones de ambas monadas.

Cuando existe la ley distributiva, puedo construir la monada compuesta T . S con unit eta_T . eta_S y una multiplicacion que usa lambda para mover las capas.

En la practica: State + Either compone bien (puedo tener estado con errores). State + List es mas sutil -- ¿cada rama del no-determinismo tiene su propia copia del estado, o comparten estado? Las dos opciones corresponden a dos ordenes de composicion, y no siempre hay una ley distributiva en ambas direcciones.

Los monad transformers de Haskell son una solucion pragmatica al problema: en lugar de buscar leyes distributivas, apilan monadas con una interfaz estandarizada:

```haskell
-- StateT s (Either e) a = s -> Either e (a, s)
-- La ley distributiva esta codificada en la implementacion del transformer

type App = ReaderT Config (StateT AppState (ExceptT AppError IO))
-- Composicion de cuatro efectos: configuracion, estado, errores, IO
```

Pero no todo stack de transformers es coherente. El orden importa. `StateT s (ListT m)` y `ListT (StateT s m)` tienen semanticas distintas. La teoria de leyes distributivas me dice exactamente cuando y por que.

## La dualidad que organiza todo

Hay una simetria profunda que organiza este documento entero:

| Concepto | Construccion | Destruccion |
|----------|-------------|-------------|
| Estructura | Algebra: F(A) -> A | Coalgebra: A -> F(A) |
| Efecto | Monada: anade estructura | Comonada: consume contexto |
| Recursion | Catamorfismo: fold | Anamorfismo: unfold |
| Objeto canonico | Algebra inicial mu(F) | Coalgebra final nu(F) |
| Razonamiento | Induccion | Coinduccion |

Las algebras viven en el mundo de la construccion: tomo piezas y las ensamblo. Las coalgebras viven en el mundo de la observacion: tomo un sistema y lo sondeo. Las monadas aaden estructura a los valores. Las comonadas extraen valores de la estructura. Los catamorfismos colapsan datos finitos -- y cuando esos datos son instancias de una base de datos, el catamorfismo es un motor de queries: un fold sobre la estructura de los registros que evalúa, filtra y agrega en una sola pasada composicional. MultiCategory implementa exactamente esto en Haskell: cada query es una función fold tipada, las instancias son datos foldables, y la composición de queries es la composición de folds -- con la garantía de que el resultado es independiente del orden de evaluación por la asociatividad del catamorfismo. Los anamorfismos generan datos potencialmente infinitos.

Cada sistema que construyo tiene ambas caras. Un servicio es una coalgebra cuando lo observo desde afuera (metricas, logs, traces = observaciones estructuradas por un interface functor). Es una algebra cuando lo implemento por dentro (fold sobre los requests entrantes, evaluacion de expresiones, reduccion de estado). Monadas modelan los efectos de mi codigo. Comonadas modelan el contexto en el que corre.

Y el puente entre ambos mundos lo da la adjuncion. Toda monada surge de una adjuncion. Toda adjuncion genera una monada y una comonada, una en cada lado. La monada y la comonada son dos caras de la misma conexion entre dos niveles de abstraccion. Es la dualidad que sostiene toda la ingenieria de efectos.
