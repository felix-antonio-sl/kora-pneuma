---
urn: urn:fxsl:kb:icas-comparacion
nombre: icas-comparacion
version: 1.1.0
estado: publicado
descripcion: "Pieza 03 del ICAS-BoK: transformaciones naturales, polimorfismo y equivalencia — cómo comparar implementaciones o traducciones que se afirman equivalentes."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/03-comparacion.md (sha256:b5c9912848ca82e8fdef34e2ae0f84402b52cb309e24a8fa7b2960356ed0f29f) el 2026-06-12. v1.1.0 (2026-07-18): delimita parametricidad, naturalidad, equivalencia y sus analogias con refactor/deploy."
autor: FS
creado: 2026-04-14
lang: es
tags: [transformacion-natural, equivalencia, comparacion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Comparación y equivalencia

## No basta preservar

No basta preservar: necesito comparar dos maneras de preservar. En mi práctica
cotidiana esto aparece con dos implementaciones, versiones o pipelines. Si
ambas se han construido como funtores paralelos, puedo preguntar por una
transformación natural; si no, primero necesito una equivalencia observacional
o un mapping operativo bien tipado.

La composición me enseñó que las cosas se conectan. Los funtores me enseñaron que la estructura se preserva al cruzar mundos. Ahora necesito un tercer nivel: morfismos entre los funtores mismos. Necesito comparar las maneras de preservar.

## Transformaciones naturales: flechas entre funtores

Cuando tengo dos funtores F, G : C → D -- dos maneras de mapear una categoría en otra -- una transformación natural α : F ⇒ G me dice cómo pasar de una a la otra, componente a componente, de manera coherente.

Concretamente: para cada objeto c en C, tengo un morfismo α_c : F(c) → G(c) en D. No uno solo -- una familia entera, uno por cada objeto. Pero no cualquier familia: exijo que estos morfismos sean compatibles con la estructura. Para cada morfismo f : c → c' en C, el siguiente cuadrado debe conmutar:

```
 F(c) ---F(f)--→ F(c')
 | |
 α_c α_c'
 | |
 ↓ ↓
 G(c) ---G(f)--→ G(c')
```

La condición de naturalidad dice exactamente esto: **da igual qué camino tomes alrededor del cuadrado**. Puedo primero transformar y luego mapear, o primero mapear y luego transformar -- el resultado es el mismo:

G(f) ∘ α_c = α_c' ∘ F(f)

Esta condicion puede especificar un refactor uniforme **si** las implementaciones son funtores con dominio y codominio comunes. No todo refactor tiene esa forma ni la naturalidad basta para cubrir seguridad operacional.

## El polimorfismo como naturalidad

El lugar donde esto se hace tangible inmediatamente es en Haskell. Una función polimórfica como `safeHead` es una transformación natural entre el funtor lista y el funtor `Maybe`:

```haskell
safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:xs) = Just x
```

El `a` es libre -- funciona para cualquier tipo. Esa es la clave. La función no mira qué hay dentro de los contenedores, solo los reorganiza. Milewski lo expresa con una imagen memorable: "Una mueve los huevos, la otra los hierve" -- reempacar y transformar contenido son operaciones ortogonales.

La condición de naturalidad se escribe:

```haskell
fmap f . safeHead = safeHead . fmap f
```

Y se verifica directamente. Para la lista vacía:

```haskell
fmap f (safeHead []) = fmap f Nothing = Nothing
safeHead (fmap f []) = safeHead [] = Nothing
```

Para la lista con elementos:

```haskell
fmap f (safeHead (x:xs)) = fmap f (Just x) = Just (f x)
safeHead (fmap f (x:xs)) = safeHead (f x : fmap f xs) = Just (f x)
```

Ambos caminos producen el mismo resultado. Esa es la naturalidad hecha código.

En un calculo parametrico total adecuado, los teoremas de parametricidad pueden inducir naturalidad para terminos polimorficos de esta forma. Haskell real incluye `bottom`, `seq` y efectos que exigen precisar la categoria/semantica; la firma sola no demuestra automaticamente toda afirmacion de naturalidad.

Otros ejemplos que uso diariamente: `length :: [a] -> Const Int a` es natural (la longitud no depende del tipo de los elementos), `reverse :: [a] -> [a]` es natural (invertir el orden no depende de qué son los elementos). En cada caso, la función trata al contenido como opaco y manipula solo la estructura.

## Refactoring, deploys y migraciones

Fuera de Haskell, una transformacion natural es un **modelo candidato** solo cuando ya existen dos funtores paralelos.

**Refactoring.** Dos modulos con la misma interfaz no son por ello funtores. Si se construyen funtores semanticos paralelos, un refactor uniforme puede modelarse como transformacion natural; normalmente basta primero una equivalencia observacional bien especificada.

**A/B testing.** Dos versiones y segmentos producen evidencia comparativa. Solo forman funtores/componentes de una natural si se definen morfismos entre inputs y se prueba la condicion para todos ellos.

**Canary deploys.** Un rollout gradual no es automaticamente una transformacion natural. El modelo requiere categorias, funtores paralelos y cuadrados que conmutan; los checks de trafico aportan evidencia operacional distinta.

**Schema versioning.** Entre dos instancias del **mismo** schema categorial, un homomorfismo es una transformacion natural. Una migracion entre schemas distintos suele requerir primero un funtor de schemas y los funtores de migracion inducidos; no es sin mas una natural entre instancias.

En bases de datos, esto se vuelve aún más preciso. Si mi schema es una categoría C y dos instancias son funtores I, J : C → Set, un homomorfismo de instancias es exactamente una transformación natural α : I ⇒ J. Para cada tabla T, α_T es una función que mapea filas de I(T) a filas de J(T), y la naturalidad dice que las foreign keys se respetan:

```sql
-- Si hay una FK de Orders.customer_id → Customers.id:
-- α_Customers(I(FK)(order)) = J(FK)(α_Orders(order))
-- "migrar el cliente y luego seguir la FK" = "seguir la FK y luego migrar"
```

## La categoría de funtores

Una vez que tengo transformaciones naturales entre funtores, puedo formar una nueva categoría. Para dos categorías C y D, la **categoría de funtores** [C, D] tiene:

- Como objetos: los funtores F : C → D
- Como morfismos: las transformaciones naturales α : F ⇒ G

La composición es componente a componente: dadas α : F ⇒ G y β : G ⇒ H, la composición β ∘ α tiene componentes (β ∘ α)_c = β_c ∘ α_c. La identidad en cada funtor F es la transformación natural con componentes id_{F(c)}.

A esto se le llama **composición vertical** -- apilo transformaciones naturales una encima de otra, siempre entre el mismo par de categorías.

Esto es poderoso. La categoría de funtores [C, Set] -- funtores de C a conjuntos -- es el universo donde habitan las "vistas" de C. Como vi cuando hablé de instancias de bases de datos, cada instancia es un objeto de [Schema, Set]. La categoría de funtores me dice cuáles son todas las instancias posibles y cómo se relacionan entre sí.

## Composición horizontal y whiskering

Pero hay otra forma de componer transformaciones naturales, que surge cuando tengo funtores en cadena:

```
C --F,G-→ D --H-→ E
 ↕α
```

Si α : F ⇒ G es una transformación natural y H : D → E un funtor, puedo formar Hα : HF ⇒ HG, el **whiskering** de α por H a la derecha. En cada componente: (Hα)_c = H(α_c). Aplico H a cada componente de α -- y como H es un funtor y α es natural, el resultado es natural.

Dualmente, si tengo un funtor K : B → C antes de los funtores, puedo formar αK : FK ⇒ GK, el whiskering por la izquierda.

Cuando tengo la situación completa:

```
C --F,G-→ D --H,I-→ E
 ↕α ↕β
```

puedo formar la **composición horizontal** βα : HF ⇒ IG. Se puede construir de dos maneras equivalentes:

βα = (βG) ∘ (Hα) = (Iα) ∘ (βF)

La equivalencia de ambos caminos -- la **ley de intercambio** -- es lo que hace coherente todo el edificio. Perrone lo demuestra limpiamente: la composición vertical de las composiciones horizontales es igual a la composición horizontal de las composiciones verticales. No hay ambigüedad.

## Equivalencia de categorías

El isomorfismo estricto de categorias suele ser mas fuerte que la equivalencia, pero el criterio correcto depende de la pregunta: igualdad, isomorfismo, equivalencia categorial y equivalencia observacional no son intercambiables.

Lo correcto es la **equivalencia de categorías**: dos funtores F : C → D y G : D → C con isomorfismos naturales η : Id_C ≅ GF y ε : FG ≅ Id_D. No pido que la ida-y-vuelta sea la identidad; pido que sea naturalmente isomorfa a la identidad. "Lo mismo, salvo isomorfismo consistente."

El teorema que lo caracteriza es elegante: F define una equivalencia si y solo si es **plenamente fiel** (biyectivo en hom-sets, como ya vi con los funtores) y **esencialmente sobreyectivo** (todo objeto de D es isomorfo a algún F(c)).

El ejemplo que tengo siempre a mano: la categoría **FVect** de espacios vectoriales de dimensión finita es equivalente a la categoría **Mat** de matrices. Los vectores "son" arreglos de números y las transformaciones lineales "son" matrices -- no exactamente lo mismo, pero equivalente en todo sentido operativo. La equivalencia dice: todo lo que puedo hacer con espacios vectoriales abstractos lo puedo hacer igualmente bien con matrices, y viceversa. Perrone lo desarrolla en detalle: el funtor es fiel (matrices distintas dan mapas distintos), pleno (toda transformación lineal se representa con una matriz), y esencialmente sobreyectivo (todo espacio de dimensión finita es isomorfo a algún R^n).

La equivalencia de categorias es el criterio apropiado cuando se comparan categorias como tales. APIs isomorfas no prueban equivalencia conductual de servicios, y traducciones de schemas "sin perdida" deben construirse como funtores plenamente fieles y esencialmente sobreyectivos antes de recibir ese nombre.

## Sin darme cuenta, ya pienso en dos niveles

Al llegar aquí me doy cuenta de algo: estoy trabajando en una estructura con tres capas. Tengo categorías (los mundos), funtores entre ellas (las traducciones), y transformaciones naturales entre los funtores (las comparaciones de traducciones). Esto tiene un nombre: una **2-categoría**.

La categoría **Cat** de todas las categorías (pequeñas) es una 2-categoría:

- **Objetos** (0-células): categorías
- **1-células**: funtores entre categorías
- **2-células**: transformaciones naturales entre funtores

La composición vertical de 2-células (apilar naturales) y la composición horizontal (concatenar a lo largo de funtores) con su ley de intercambio son exactamente la estructura de una 2-categoría.

No necesité aprender "2-categorías" como tema separado. Ya estaba pensando en dos niveles sin darme cuenta: cada vez que comparo dos funtores, cada vez que hago whiskering, cada vez que compongo horizontalmente. Es la estructura que emerge naturalmente cuando tomo en serio la comparación entre preservaciones.

Perrone lo señala con honestidad: la categoría Cat, tal como se define con funtores como morfismos y conjuntos de funtores como hom-sets, no captura toda la riqueza. Los hom-spaces Hom(C, D) no son solo conjuntos -- son categorías, porque entre funtores hay transformaciones naturales, y entre naturales hay composición. Cuando los hom-spaces son categorías en lugar de conjuntos, estamos en una 2-categoría. Eso es lo que Cat realmente es.

Para arquitectura, una 2-categoria puede formalizar traducciones y comparaciones cuando se construyen sus 0-, 1- y 2-celdas y se verifican sus leyes. La mera presencia de componentes, migraciones o estados no demuestra esa estructura.

## Estatuto epistemico

- **Formal:** transformaciones naturales, categorias de funtores,
  equivalencias y la 2-categoria `Cat` bajo las convenciones de tamaño.
- **Modelo:** refactor, deploy o migracion solo con funtores y componentes
  tipados.
- **Heuristica:** tratar dos versiones o dos APIs como funtores equivalentes
  sin construir la semantica.
