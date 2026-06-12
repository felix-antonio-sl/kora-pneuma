---
urn: urn:fxsl:kb:icas-identidad-relacion
nombre: icas-identidad-relacion
version: 1.0.0
estado: publicado
descripcion: "Pieza 04 del ICAS-BoK: hom-funtores, lema de Yoneda, embedding y presheaves — entender un componente desde afuera por su patrón de relaciones (API, queries, interacción)."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/04-identidad-es-relacion.md (sha256:ae994f1606b5bc1bc3e0e403f1c767bd2706d5e4163ef22c24c9099778d8a66a) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [yoneda, representabilidad, API, interfaz, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Identidad es relación

## El momento en que todo cambia

Hay un momento en el que todo cambia. Dejo de preguntar "¿qué es esto por dentro?" y empiezo a ver que, para fines de observación y composición, una cosa queda determinada por un patrón suficientemente rico de relaciones con todo lo demás. Un servicio se deja estudiar por su API. Una tabla, por las operaciones que admite. Un agente, por sus interacciones. Un container, por sus puertos y volúmenes expuestos.

Este giro -- de mirar adentro a mirar afuera -- es el paso más profundo que he dado en mi formación como arquitecto. Antes de este punto, entendía las cosas descomponiéndolas: abría la caja, estudiaba los mecanismos internos, clasificaba las partes. Después de este punto, entiendo las cosas situándolas: observo cómo se relacionan con todo lo demás, y esa red de relaciones me dice todo lo que necesito saber.

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

Un Stream infinito, por ejemplo, es representable por Integer: es exactamente una función de Integer a valores, empaquetada como estructura de datos.

```haskell
data Stream x = Cons x (Stream x)

instance Representable Stream where
 type Rep Stream = Integer
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

La aplicación más simple es cuando F es la identidad: `forall r. (a -> r) -> r ≅ a`. Esto es la **transformación de paso de continuaciones** (CPS). Cualquier valor de tipo `a` puede reemplazarse por una función que toma un "handler" y le pasa el valor. Es la base de los callbacks, la programación asíncrona, las promesas. Y es un caso particular del lema de Yoneda.

## El embedding de Yoneda: ninguna información se pierde

Ahora llevo esto un paso más allá. No fijo solo un objeto A -- considero el mapeo que a cada A le asigna su hom-funtor:

y : C → [C^op, Set]
A ↦ Hom(−, A)

Este mapeo envía cada objeto A al funtor contravariante que recopila todas las flechas que llegan a A. El **embedding de Yoneda** dice que este mapeo es un funtor, y que es **plenamente fiel**.

Plenamente fiel significa: el mapeo entre morfismos

Hom_C(A, B) → Nat(Hom(−, A), Hom(−, B))

es una biyección. Cada transformación natural entre los hom-funtores contravariantes corresponde exactamente a un morfismo en la categoría original. No se pierde nada y no se inventa nada.

Esto es extraordinario. Dice que la categoría C vive fielmente dentro de su categoría de presheaves [C^op, Set], sin perder ningún detalle de su estructura interna. Cada objeto queda completamente determinado por su patrón de relaciones con todos los demás.

La versión covariante usa Hom(A, −) y embebe C^op en [C, Set], llegando a la misma conclusión por dualidad.

## Presheaves: vistas generalizadas

La categoría [C^op, Set] se llama la **categoría de presheaves** sobre C. Sus objetos son funtores C^op → Set -- asignaciones que a cada objeto de C le asocian un conjunto, de manera contravariante.

No todos los presheaves vienen de objetos de C vía el embedding de Yoneda. Los que sí vienen -- los de la forma Hom(−, A) -- se llaman **presheaves representables**. Son los puntos de vista de los "ciudadanos nativos" de C. Pero la categoría de presheaves contiene mucho más: contiene "vistas generalizadas" que no corresponden a ningún objeto concreto.

Un ejemplo que me acompaña siempre: si C es el schema de una base de datos (objetos = tablas, morfismos = foreign keys), un presheaf es una asignación de datos a cada tabla que respeta las FKs en dirección opuesta. Pero además de las instancias "normales" (que corresponden a presheaves representables en cierto sentido), existen presheaves que representan "consultas parciales" o "vistas materializadas" que no son instancias completas de ningún objeto del schema.

Perrone muestra un ejemplo limpio: si C = Par (la categoría con dos objetos V, E y dos flechas paralelas s, t : V → E), un presheaf sobre Par^op consiste en dos conjuntos FV y FE con dos funciones Fs, Ft : FE → FV. Esto es exactamente un multigrafo dirigido. Los grafos emergen como presheaves sobre un schema simple.

## Lo que Yoneda cambia en mi práctica

### Un servicio se deja estudiar por su API

Cuando diseño microservicios, el lema de Yoneda formaliza algo más preciso y más modesto que el eslogan "un servicio es su API": si fijo una categoría de observables adecuada, el patrón de morfismos hacia y desde el servicio captura exactamente la información relevante para ese modo de observación. En práctica, la API suele ser la mejor aproximación externa a ese patrón. Dos servicios con APIs isomorfas son indistinguibles para cualquier cliente que solo observe a través de esa interfaz, aunque todavía pueden diferir internamente en dimensiones que la API no expone.

### Una tabla se deja estudiar por sus queries

En bases de datos, una tabla queda muy bien caracterizada por el repertorio de consultas y relaciones que soporta dentro de un esquema fijo. El `SELECT * FROM t WHERE ...` para cada condición posible, los `JOIN` con cada otra tabla, las agregaciones y restricciones forman una familia de observables muy cercana al espíritu de Yoneda. En ese marco, si dos tablas inducen exactamente las mismas observaciones relacionales, puedo tratarlas como equivalentes para ese propósito de modelado.

### Un container se deja estudiar por sus puertos

Un container Docker está fuertemente determinado, para el orquestador, por su interfaz expuesta: puertos publicados, volúmenes montados, variables de entorno que acepta. Dos containers con la misma signatura de puertos y volúmenes son intercambiables desde ese punto de vista operativo. La implementación interna -- el sistema operativo base, el lenguaje de la aplicación, la estructura de archivos -- puede seguir importando para otros fines, pero no para la observación que hace el orquestador.

### Un usuario se deja estudiar por su comportamiento

Los motores de recomendación funcionan porque Yoneda es verdadero. No necesitan saber quién "es" un usuario por dentro -- su edad, sus pensamientos, su identidad. Lo que necesitan es el patrón de interacciones: qué compró, qué vio, qué calificó, con qué frecuencia. La identidad del usuario, para el sistema, ES la totalidad de sus interacciones. Dos usuarios con comportamiento isomorfo recibirán las mismas recomendaciones.

### Un agente se deja estudiar por sus interacciones

En sistemas multi-agente, un agente puede modelarse externamente por lo que hace en todos los contextos que la categoría de observación decide distinguir. No por su arquitectura interna (¿usa un LLM? ¿un árbol de decisión? ¿reglas hardcodeadas?) sino por su respuesta a cada posible input en cada posible estado observable. El hom-funtor del agente captura todas las maneras en que el agente puede responder al mundo dentro de ese marco, y eso suele ser suficiente para componer agentes en un sistema.

## Robots que se conocen a sí mismos

El proyecto Sys-Self de Aguado, Rossi y Sanz en la Universidad Politécnica de Madrid lleva esta idea a un territorio fascinante: robots autónomos que se entienden a sí mismos no abriendo su propia carcasa, sino modelando sus interacciones. La premisa es que un robot puede mejorar su dependabilidad si tiene un modelo formal de sí mismo -- de sus capacidades, su misión, su entorno.

La teoría de categorías les proporciona el marco: el robot se modela como un objeto en una categoría de sistemas. Su auto-conocimiento no viene de introspección de su código, sino de su hom-funtor -- la totalidad de cómo puede interactuar con su entorno, con sus componentes, con otros robots. Cuando algo cambia (un sensor falla, el entorno se modifica), el robot actualiza su modelo relacional y re-planifica. Es Yoneda operativo: el sistema SE CONOCE a través de sus relaciones, no de su estructura interna.

## Enjambres en la categoría de presheaves

Krol, Schumann y Bielas llevan el embedding de Yoneda a otro terreno: computación de enjambres (swarms). Modelan un enjambre W como una categoría K de nodos computacionales con funciones recursivas parciales como morfismos. El embedding de Yoneda

y : K → SET^{K^op}

embebe el enjambre en su categoría de presheaves. Los presheaves representables R_a = Hom(−, a) capturan todas las computaciones que pueden llegar a un nodo a. Las regiones excitadas del enjambre -- las zonas donde la computación se activa en respuesta a estímulos externos -- se modelan como sub-presheaves.

Lo notable es que la categoría de presheaves SET^{K^op} tiene propiedades extraordinariamente ricas -- limites, colimites, exponenciales, un clasificador de subobjetos -- que le dan una logica interna intuicionista (el documento 12 desarrolla esta estructura bajo el nombre de topos). Krol y colegas encuentran que el comportamiento colectivo emergente del enjambre vive naturalmente en esa lógica: no es necesariamente clásico (tercero excluido), sino intuicionista. La emergencia no es mística; es la lógica interna del topos de presheaves.

El lema de Yoneda, en este contexto, establece la biyección entre las transformaciones naturales de un presheaf representable R_a a cualquier presheaf F, y el conjunto F(a):

Nat(R_a, F) ≅ F(a)

Esto permite razonar sobre el comportamiento global del enjambre a partir de observaciones locales en nodos individuales.

## La metáfora Neo

Antes de Yoneda, miro los objetos por dentro para entenderlos. Abro la caja, saco las piezas, etiqueto los mecanismos. Es el enfoque reduccionista que me enseñaron: para entender algo, descomponerlo.

Después de Yoneda, entiendo que descomponer no es necesario -- y a veces no es posible. Lo que determina completamente un objeto, en el sentido del embedding de Yoneda, es la totalidad de sus relaciones categóricas. Ninguna información se pierde cuando paso de un objeto a su presheaf representable. La red de relaciones no reemplaza mágicamente toda descripción concreta del objeto, pero sí captura de manera plena y fiel la estructura que la categoría sabe distinguir.

Este es el paso del reduccionismo al pensamiento relacional. No abandono la capacidad de mirar adentro cuando es útil, pero ya no la necesito como fundamento epistémico. Lo primero que miro ahora es la interfaz, el API, el contrato, el patrón de interacciones. Y sé, con la garantía del lema, que eso es suficiente.

El co-Yoneda -- la versión contravariante -- me da lo mismo por el otro lado. Si fijo el target en lugar del source, obtengo:

Nat(Hom(−, A), F) ≅ F(A)

para funtores contravariantes F : C^op → Set. Los morfismos que llegan a A son tan informativos como los que salen. En la práctica, esto es la dualidad entre "lo que un servicio ofrece" (endpoints que expone) y "lo que un servicio requiere" (dependencias que consume). Ambas perspectivas determinan al servicio completamente.

Cuando este entendimiento se asienta, la forma de diseñar sistemas cambia. Ya no parto de "qué es este componente por dentro" sino de "cómo se relaciona este componente con todo lo demás." La parte teoremática es Yoneda: el embedding pleno y fiel en la categoría de presheaves. Las lecturas sobre APIs, queries e interfaces son aplicaciones de modelado de ese resultado, no sustitutos literales de su formulación.
