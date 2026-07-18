---
urn: urn:fxsl:kb:icas-efectos
nombre: icas-efectos
version: 1.1.0
estado: publicado
descripcion: "Pieza 09 del ICAS-BoK: efectos — mónadas, Kleisli, Eilenberg-Moore, comónadas, coálgebras, bisimulación y leyes distributivas; componer computación con efectos y observar comportamiento."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/09-efectos.md (sha256:67dd42843b739c2db94b89c00b5321fe0d43b634c3fcd46a9ac0fe7fd53f46fb) el 2026-06-12. v1.1.0 (2026-07-18): corrige coalgébras de automatas, existencia final, event sourcing, bisimulacion, transformers y extrapolaciones a servicios."
autor: FS
creado: 2026-04-14
lang: es
tags: [monada, kleisli, coalgebra, bisimulacion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Efectos

## El problema de las funciones que mienten

Una funcion `f : A -> B` promete que dado un valor de tipo A produce un valor de tipo B. Pero en la practica, las funciones que escribo todos los dias hacen mucho mas que eso. Leen configuracion. Escriben logs. Fallan con excepciones. Producen multiples resultados. Modifican estado. Lanzan operaciones asincronas. La firma de tipos dice una cosa; el comportamiento dice otra.

Una solución importante es hacer los efectos explícitos en el sistema de tipos.
Las mónadas modelan muchas composiciones efectivas; no son la única estructura
posible ni todo efecto determina una mónada canónica.

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

La monada aporta una composicion Kleisli coherente; distintos modelos usan esa
estructura para efectos. No todo efecto ni toda secuenciacion viene dado por
una monada.

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

-- IO a: modelo operacional de interacciones externas en Haskell
```

Promises admiten una lectura monadica sobre una semantica y equivalencia
adecuadas. La asimilacion de *thenables*, excepciones y detalles del runtime
impiden inferir las leyes solo de la API de TypeScript.

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

`duplicate` produce las colas sucesivas y `extend` calcula con ese contexto
derecho. Automatas celulares como Game of Life suelen modelarse con una
comonada de store/grid que expone vecindad bidireccional; este `Stream` no la
realiza por si solo.

En React, los hooks exhiben una estructura analogica a las comonadas. Un componente `(props, state) -> JSX` tiene la forma de un co-Kleisli arrow. `useContext`, `useState`, `useEffect` proporcionan el contexto extendido. El componente extrae su render del contexto completo. El re-render se asemeja a extend: "re-computa el output para cada posible estado." La analogia es estructural, no una instancia formal de Comonad -- React no implementa las leyes comonadicas -- pero ilumina por que la composicion de hooks sigue los mismos patrones.

## Coalgebras: la mirada desde afuera

Mientras las algebras deconstruyen (evaluan estructura), las coalgebras construyen (generan comportamiento). Una F-coalgebra es un par (U, alpha) donde alpha : U -> F(U) -- un estado produce una observacion estructurada.

Barbosa lo dice con precision: "coalgebra invierte la flecha del algebra. En lugar de especificar como ensamblar un valor a partir de sus componentes, especifica como descomponer un estado en sus observables."

El funtor F es la forma de la observacion -- el interface functor. Determina que puedo ver del sistema:

- F(X) = A x X: un sistema sin input que produce un output A y transiciona; su
  coalgebra final, cuando se toma en `Set`, son streams.
- F(X) = 1 + A x X: parcialidad -- la observacion puede terminar o seguir. Es una lista posiblemente finita.
- F(X) = P(X): no-determinismo -- multiples estados sucesores. Es un sistema de transiciones.
- F(X) = B x X^A: output B dependiente del estado y sucesor por input A; es
  una maquina de Moore.
- F(X) = (B x X)^A: por cada input A produce output B y sucesor; es una
  maquina de Mealy.

## Coalgebra final y anamorfismos

**Si existe**, una coalgebra final `nu(F)` recibe un unico morfismo desde cada
F-coalgebra y puede representar comportamientos observables. El lema de Lambek
implica que su estructura es un isomorfismo `nu(F) ≅ F(nu(F))`; el converso no
vale: un punto fijo cualquiera no es final.

El anamorfismo coiterativo es ese unico morfismo cuando la coalgebra final
existe. El siguiente `Fix` de Haskell es una codificacion operacional bajo
hipotesis de productividad/laziness, no una prueba general de finality:

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

La **generacion** de un stream de eventos puede modelarse coalgebraicamente si
hay una funcion `State -> Event × State`. En event sourcing real, la
reconstruccion de estado desde un log finito es normalmente un fold; no todo el
patron es un anamorfismo.

## Bisimulacion: equivalencia observacional

Cuando existe una coalgebra final, la igualdad de las imagenes por los
morfismos conductuales define equivalencia observacional.

Una bisimulacion relacional requiere un lifting de relaciones adecuado para F
y las hipotesis bajo las cuales coincide con equivalencia conductual. Con
efectos/no determinismo hay varias semanticas posibles.

Para automatas deterministas, bisimulacion dice: dos estados son bisimilares si producen el mismo output y sus sucesores siguen siendo bisimilares. Para sistemas con no-determinismo, la definicion se adapta al funtor correspondiente.

Dos microservicios pueden llamarse bisimilares solo tras especificar sus
coalgebras, observaciones, transiciones y relacion. Aun entonces la
intercambiabilidad operacional puede exigir latencia, disponibilidad y efectos
que el funtor no observa.

Blue-green e integration tests aportan evidencia de equivalencia sobre casos
observados; no construyen por si solos una relacion coinductiva cerrada para
todos los estados.

## Leyes distributivas: cuando los efectos componen

No todas las monadas componen. Dadas dos monadas S y T en la misma categoria, la composicion S . T no necesariamente es una monada. Para que lo sea, necesito una ley distributiva lambda : S . T => T . S -- una transformacion natural que "intercambia" las capas de efecto de manera coherente con las unidades y multiplicaciones de ambas monadas.

Cuando existe la ley distributiva, puedo construir la monada compuesta T . S con unit eta_T . eta_S y una multiplicacion que usa lambda para mover las capas.

Stacks State/Either o State/List tienen ordenes y semanticas distintas. Que
exista un transformer util no demuestra una ley distributiva entre las monadas
subyacentes en ambas direcciones.

Los monad transformers de Haskell son una solucion pragmatica al problema: en lugar de buscar leyes distributivas, apilan monadas con una interfaz estandarizada:

```haskell
-- StateT s (Either e) a = s -> Either e (a, s)
-- El transformer fija una semantica; no certifica por si solo una ley
-- distributiva entre las monadas originales.

type App = ReaderT Config (StateT AppState (ExceptT AppError IO))
-- Composicion de cuatro efectos: configuracion, estado, errores, IO
```

El orden importa y algunos transformers tienen restricciones o leyes propias.
Una ley distributiva demostrada explica una composicion monadica; no toda
implementacion de transformer proviene de una.

## La dualidad que organiza todo

Hay una simetria profunda que organiza este documento entero:

| Concepto | Construccion | Destruccion |
|----------|-------------|-------------|
| Estructura | Algebra: F(A) -> A | Coalgebra: A -> F(A) |
| Efecto | Monada: anade estructura | Comonada: consume contexto |
| Recursion | Catamorfismo: fold | Anamorfismo: unfold |
| Objeto canonico | Algebra inicial mu(F) | Coalgebra final nu(F) |
| Razonamiento | Induccion | Coinduccion |

Los catamorfismos consumen algebras iniciales y los anamorfismos generan
estructuras coinductivas bajo las hipotesis pertinentes. Un query puede
implementarse como fold, pero asociatividad no da independencia del orden de
evaluacion: para eso suelen requerirse conmutatividad u otras leyes.

Servicios pueden recibir modelos algebraicos, coalgebraicos, monadicos o
comonadicos una vez definidos sus funtores y leyes. Metricas/logs no convierten
automaticamente al servicio en coalgebra ni un handler en algebra.

Toda monada admite adjunciones canonicas (Kleisli y Eilenberg-Moore), y una
adjuncion genera una monada y una comonada en lados opuestos. Esta es una
relacion formal; no implica que toda ingenieria de efectos use ese modelo.

## Estatuto epistemico

- **Formal:** monadas/comonadas, categorias de Kleisli/EM, coalgebras,
  finality y bisimulacion bajo hipotesis explicitas.
- **Modelo:** maquinas, streams y efectos tipados cuando se declara el funtor.
- **Heuristica:** servicios, deployments, React o event sourcing promovidos a
  esas estructuras por semejanza superficial.
