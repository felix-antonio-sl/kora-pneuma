---
urn: urn:fxsl:kb:icas-identidad-relacion
nombre: icas-identidad-relacion
version: 1.1.0
estado: publicado
descripcion: "Pieza 04 del ICAS-BoK: hom-funtores, lema de Yoneda, embedding y presheaves — entender un componente desde afuera por su patrón de relaciones (API, queries, interacción)."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/04-identidad-es-relacion.md (sha256:ae994f1606b5bc1bc3e0e403f1c767bd2706d5e4163ef22c24c9099778d8a66a) el 2026-06-12. v1.1.0 (2026-07-18): restringe Yoneda a la estructura visible en la categoria y corrige sus extrapolaciones a APIs, usuarios, containers y presheaves de datos."
autor: FS
creado: 2026-04-14
lang: es
tags: [yoneda, representabilidad, API, interfaz, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Identidad es relación

## El momento en que todo cambia

Hay un momento en el que todo cambia. Dejo de preguntar "¿qué es esto por dentro?" y empiezo a ver que, para fines de observación y composición, una cosa queda determinada por un patrón suficientemente rico de relaciones con todo lo demás. Un servicio se deja estudiar por su API. Una tabla, por las operaciones que admite. Un agente, por sus interacciones. Un container, por sus puertos y volúmenes expuestos.

Este giro -- de mirar adentro a mirar afuera -- es central para mi formación
como arquitecto. La red de relaciones dice todo lo que la categoría elegida
puede observar; no necesariamente agota la implementación, el contexto físico
ni la identidad humana de aquello que modela.

En el libro sobre pensamiento relacional lo dicen con una frase que se me quedó grabada: *relational thinking seeks to understand an object by taking it as a point from which to look outwards, asking how the object interacts, rather than inwards, asking what the object is made of.* Eso es exactamente lo que voy a formalizar aquí.

## Mirar desde afuera: el hom-funtor

Todo empieza con una pregunta simple. Dado un objeto A en una categoría C, ¿qué puedo aprender sobre A observando sus relaciones con los demás?

Para cada objeto X de C, puedo considerar el conjunto de todos los morfismos de A a X: el hom-set Hom(A, X). Este conjunto me dice "de cuántas maneras A puede hablar con X." Si el conjunto es vacío, A no tiene conexión con X. Si tiene un solo elemento, hay exactamente una forma. Si tiene muchos, A se relaciona con X de múltiples maneras.

Lo crucial es que esta asignación X ↦ Hom(A, X) es un funtor. Si tengo un morfismo f : X → Y en C, puedo transformar cualquier morfismo h : A → X en un morfismo f ∘ h : A → Y por post-composición:

```
Hom(A, X) ——f∘—→ Hom(A, Y)
 h ↦——————→ f ∘ h
```

Este funtor Hom(A, −) : C → Set es el **hom-funtor covariante** fijando A. Es un funtor porque preserva identidades (id_X ∘ h = h) y composición ((g ∘ f) ∘ h = g ∘ (f ∘ h) por asociatividad -- una ley que ya conozco desde que empecé a componer).

Lo que hace Hom(A, −) es, literalmente, ver el mundo entero desde el punto de vista de A. Para cada objeto del universo, recopila todas las flechas que salen de A hacia él. Es la perspectiva de A sobre todo lo demás.

Dualmente, Hom(−, A) : C^op → Set captura todos los morfismos que llegan a A. Este es el hom-funtor contravariante: ve a A como destino. Si f : X → Y, induce Hom(Y, A) → Hom(X, A) por pre-composición: g ↦ g ∘ f. Nota la inversión de dirección -- la contravarianza que ya vi con los funtores.

## Funtores representables: cuando un funtor "es" secretamente un objeto

A veces me encuentro con un funtor F : C → Set que, para mi sorpresa, resulta ser isomorfo al hom-funtor de algún objeto. Es decir, existe un objeto A en C y un isomorfismo natural F ≅ Hom(A, −). Cuando esto pasa, digo que F es **representable**, y que A lo representa.

En Haskell, Milewski lo explica con una imagen que me resultó iluminadora: un funtor representable es como una tabla de memoización. El tipo A es la clave, los valores de F(X) son los resultados tabulados. Puedo "tabular" una función (a → x) → F x o "indexar" F x → (a → x), y ambas operaciones son inversas:

```haskell
class Representable f where
 type Rep f :: *
 tabulate :: (Rep f -> x) -> f x
 index :: f x -> Rep f -> x
```

Un `Stream` unilateral infinito es representable por los numeros naturales: equivale a una funcion `Natural -> x`.

```haskell
data Stream x = Cons x (Stream x)

instance Representable Stream where
 type Rep Stream = Natural
 tabulate f = Cons (f 0) (tabulate (f . (+1)))
 index (Cons b bs) n = if n == 0 then b else index bs (n - 1)
```

No toda estructura de datos es representable. La lista finita no lo es, porque puede estar vacía -- no hay manera de recuperar un valor de una lista vacía dada una clave arbitraria. La representabilidad exige que para cada clave haya un valor.

Lo que importa aquí para mi práctica: si un funtor es representable, tiene un "objeto secreto" que lo determina completamente. Y las dos representaciones -- la funcional y la de datos -- contienen exactamente la misma información, aunque una puede ser más eficiente que la otra.

## El lema de Yoneda

Y ahora el golpe. No solo los funtores representables se relacionan con los hom-funtores. **Todo** funtor Set-valorado tiene una relación precisa con cada hom-funtor. Esa relación es el lema de Yoneda.

Sea C una categoría, A un objeto de C, y F : C → Set un funtor cualquiera. El lema de Yoneda afirma:

**Nat(Hom(A, −), F) ≅ F(A)**

El conjunto de todas las transformaciones naturales del hom-funtor Hom(A, −) al funtor F está en biyección con los elementos del conjunto F(A).

Detengo aquí un momento, porque la primera vez que leí esto no medí su alcance. Dice: todo lo que puedo hacer "naturalmente" con las sondas que salen de A -- toda manera coherente de convertir "morfismos desde A" en "datos de F" -- está codificado en un solo punto: un elemento de F(A). Toda la transformación natural, una familia infinita de funciones indexada por todos los objetos de C, cristaliza a partir de un solo valor.

¿Cómo funciona? Sea α : Hom(A, −) ⇒ F una transformación natural. Considero su componente en A mismo: α_A : Hom(A, A) → F(A). Existe al menos un morfismo de A a A -- la identidad id_A. Evalúo: q = α_A(id_A) ∈ F(A). Ese punto q es el "germen" que determina toda la transformación.

Para cualquier otro objeto Y y cualquier morfismo f : A → Y, la naturalidad me obliga:

α_Y(f) = α_Y(f ∘ id_A) = (Ff)(α_A(id_A)) = (Ff)(q)

Toda la transformación natural se reconstruye a partir de q aplicando el funtor F a los morfismos que salen de A. El resto "simplemente sigue de la condición de naturalidad", como dice Milewski. El valor se propaga desde id_A siguiendo las flechas del funtor.

Conversamente, dado cualquier q ∈ F(A), puedo definir una transformación natural α^q por:

α^q_Y(f) = (Ff)(q) para todo f : A → Y

Es inmediato verificar que esto es natural. Así que la correspondencia es biyectiva.

En Haskell, el lema toma una forma que uso regularmente:

```haskell
-- El lema de Yoneda dice:
-- forall x. (a -> x) -> F x ≅ F a

-- De izquierda a derecha: aplicar a id
toData :: (forall x. (a -> x) -> f x) -> f a
toData alpha = alpha id

-- De derecha a izquierda: fmap
fromData :: Functor f => f a -> (forall x. (a -> x) -> f x)
fromData fa h = fmap h fa
```

En una semantica parametrica total, el caso identidad da `forall r. (a -> r) -> r ≅ a`. Es la codificacion por continuaciones de un valor; relacionarla con callbacks, asincronia o promesas exige modelar ademas sus efectos.

## El embedding de Yoneda: ninguna información se pierde

Ahora llevo esto un paso más allá. No fijo solo un objeto A -- considero el mapeo que a cada A le asigna su hom-funtor:

y : C → [C^op, Set]
A ↦ Hom(−, A)

Este mapeo envía cada objeto A al funtor contravariante que recopila todas las flechas que llegan a A. El **embedding de Yoneda** dice que este mapeo es un funtor, y que es **plenamente fiel**.

Plenamente fiel significa: el mapeo entre morfismos

Hom_C(A, B) → Nat(Hom(−, A), Hom(−, B))

es una biyección. Cada transformación natural entre los hom-funtores contravariantes corresponde exactamente a un morfismo en la categoría original. No se pierde nada y no se inventa nada.

Esto dice que la categoria C se embebe plenamente fiel en su categoria de presheaves: se preservan exactamente sus hom-sets. No afirma que el modelo categorico capture toda propiedad extramatematica del sistema representado.

La versión covariante usa Hom(A, −) y embebe C^op en [C, Set], llegando a la misma conclusión por dualidad.

## Presheaves: vistas generalizadas

La categoría [C^op, Set] se llama la **categoría de presheaves** sobre C. Sus objetos son funtores C^op → Set -- asignaciones que a cada objeto de C le asocian un conjunto, de manera contravariante.

No todos los presheaves vienen de objetos de C vía el embedding de Yoneda. Los que sí vienen -- los de la forma Hom(−, A) -- se llaman **presheaves representables**. Son los puntos de vista de los "ciudadanos nativos" de C. Pero la categoría de presheaves contiene mucho más: contiene "vistas generalizadas" que no corresponden a ningún objeto concreto.

Con la convencion usual del corpus, una instancia de un schema C es un funtor covariante `C -> Set`. Un presheaf `C^op -> Set` es una construccion distinta (o una instancia del schema opuesto); las instancias ordinarias no son, en general, presheaves representables.

Perrone muestra un ejemplo limpio: si C = Par (la categoría con dos objetos V, E y dos flechas paralelas s, t : V → E), un presheaf sobre Par^op consiste en dos conjuntos FV y FE con dos funciones Fs, Ft : FE → FV. Esto es exactamente un multigrafo dirigido. Los grafos emergen como presheaves sobre un schema simple.

## Lo que Yoneda cambia en mi práctica

### Un servicio se deja estudiar por su API

Si un servicio es realmente un objeto de una categoria de observables, su presheaf representable captura los morfismos que esa categoria distingue. Una signatura de API usual es solo una aproximacion parcial: APIs isomorfas no garantizan igual conducta, latencia, efectos ni protocolo.

### Una tabla se deja estudiar por sus queries

En bases de datos, una tabla queda muy bien caracterizada por el repertorio de consultas y relaciones que soporta dentro de un esquema fijo. El `SELECT * FROM t WHERE ...` para cada condición posible, los `JOIN` con cada otra tabla, las agregaciones y restricciones forman una familia de observables muy cercana al espíritu de Yoneda. En ese marco, si dos tablas inducen exactamente las mismas observaciones relacionales, puedo tratarlas como equivalentes para ese propósito de modelado.

### Un container se deja estudiar por sus puertos

Puertos, volumenes y variables describen parte de la interfaz observable de un container. Igual signatura no demuestra intercambiabilidad: protocolos, semantica, salud, recursos y efectos tambien pueden ser observables.

### Un usuario se deja estudiar por su comportamiento

Los motores de recomendacion pueden modelar usuarios por trazas observadas. Eso es una eleccion estadistica y etica, no una consecuencia de Yoneda; las interacciones no agotan la identidad de una persona ni garantizan recomendaciones iguales.

### Un agente se deja estudiar por sus interacciones

En sistemas multi-agente, un agente puede modelarse externamente por lo que hace en todos los contextos que la categoría de observación decide distinguir. No por su arquitectura interna (¿usa un LLM? ¿un árbol de decisión? ¿reglas hardcodeadas?) sino por su respuesta a cada posible input en cada posible estado observable. El hom-funtor del agente captura todas las maneras en que el agente puede responder al mundo dentro de ese marco, y eso suele ser suficiente para componer agentes en un sistema.

## Robots que se conocen a sí mismos

El proyecto Sys-Self de Aguado, Rossi y Sanz en la Universidad Politécnica de Madrid lleva esta idea a un territorio fascinante: robots autónomos que se entienden a sí mismos no abriendo su propia carcasa, sino modelando sus interacciones. La premisa es que un robot puede mejorar su dependabilidad si tiene un modelo formal de sí mismo -- de sus capacidades, su misión, su entorno.

Una categoria de sistemas y sus observaciones puede servir como modelo formal de auto-representacion. Llamarlo "Yoneda operativo" es una lectura de diseño: el teorema no implementa introspeccion, deteccion de fallas ni re-planificacion.

## Enjambres en la categoría de presheaves

Krol, Schumann y Bielas llevan el embedding de Yoneda a otro terreno: computación de enjambres (swarms). Modelan un enjambre W como una categoría K de nodos computacionales con funciones recursivas parciales como morfismos. El embedding de Yoneda

y : K → SET^{K^op}

embebe el enjambre en su categoría de presheaves. Los presheaves representables R_a = Hom(−, a) capturan todas las computaciones que pueden llegar a un nodo a. Las regiones excitadas del enjambre -- las zonas donde la computación se activa en respuesta a estímulos externos -- se modelan como sub-presheaves.

Para K pequena, la categoria de presheaves `Set^{K^op}` es un topos y posee logica interna intuicionista. Que un comportamiento de enjambre quede adecuadamente representado en ella depende del modelo del estudio; la existencia del topos no explica por si sola la emergencia.

El lema de Yoneda, en este contexto, establece la biyección entre las transformaciones naturales de un presheaf representable R_a a cualquier presheaf F, y el conjunto F(a):

Nat(R_a, F) ≅ F(a)

Esto permite razonar sobre el comportamiento global del enjambre a partir de observaciones locales en nodos individuales.

## La metáfora Neo

Antes de Yoneda, miro los objetos por dentro para entenderlos. Abro la caja, saco las piezas, etiqueto los mecanismos. Es el enfoque reduccionista que me enseñaron: para entender algo, descomponerlo.

Después de Yoneda, entiendo que descomponer no es necesario -- y a veces no es posible. Lo que determina completamente un objeto, en el sentido del embedding de Yoneda, es la totalidad de sus relaciones categóricas. Ninguna información se pierde cuando paso de un objeto a su presheaf representable. La red de relaciones no reemplaza mágicamente toda descripción concreta del objeto, pero sí captura de manera plena y fiel la estructura que la categoría sabe distinguir.

Yoneda garantiza suficiencia respecto de **todos los morfismos de la categoria elegida**. Una API o conjunto finito de observaciones solo hereda esa garantia si se demuestra que realiza ese patron completo.

El co-Yoneda -- la versión contravariante -- me da lo mismo por el otro lado. Si fijo el target en lugar del source, obtengo:

Nat(Hom(−, A), F) ≅ F(A)

para funtores contravariantes F : C^op → Set. La analogia entre endpoints ofrecidos y dependencias requeridas puede orientar un modelo, pero cada perspectiva parcial no determina por si sola al servicio.

Cuando este entendimiento se asienta, la forma de diseñar sistemas cambia. Ya no parto de "qué es este componente por dentro" sino de "cómo se relaciona este componente con todo lo demás." La parte teoremática es Yoneda: el embedding pleno y fiel en la categoría de presheaves. Las lecturas sobre APIs, queries e interfaces son aplicaciones de modelado de ese resultado, no sustitutos literales de su formulación.

## Estatuto epistemico

- **Formal:** lema y embedding de Yoneda, representabilidad y topos de
  presheaves para una categoria pequena.
- **Modelo:** servicios, schemas, agentes o enjambres solo dentro de una
  categoria de observacion construida.
- **Metafora:** reducir identidad humana, conducta operacional o
  auto-conocimiento al eslogan "un objeto es sus relaciones".
