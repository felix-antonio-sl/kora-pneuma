---
urn: urn:fxsl:kb:icas-adjunciones
nombre: icas-adjunciones
version: 1.1.0
estado: publicado
descripcion: "Pieza 06 del ICAS-BoK: adjunciones — unit/counit, free/forgetful, Sigma-Delta-Pi y conexiones de Galois; tradeoffs relajación/formalización y migración con preservación de constraints."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/06-adjunciones.md (sha256:53c5c8fa0c1e3ede1b13e35526862e9b3ee4e5b5f3256f6300f25758207c194c) el 2026-06-12. v1.1.0 (2026-07-18): corrige unit/counit, round-trips, preservacion de constraints y retorica de optimalidad."
autor: FS
creado: 2026-04-14
lang: es
tags: [adjuncion, sigma-delta-pi, free-forgetful, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Adjunciones

## Una correspondencia universal entre traducciones

Llevo cinco documentos construyendo un vocabulario: composición, preservación, comparación, identidad relacional, y ahora construcciones universales. Y hay un hilo que reaparece en cada una. Cuando traduzco entre mundos con funtores, hay traducciones que están "perfectamente emparejadas" -- una va en un sentido y la otra en el sentido contrario, y juntas forman algo mejor que un simple par de funtores. No son inversas (eso sería una equivalencia), pero están coordinadas de una manera que genera estructura nueva.

Esa coordinacion se llama **adjuncion**. Muchos pares importantes la realizan,
pero un viaje de ida y vuelta no basta: se necesita la biyeccion natural de
hom-sets o, equivalentemente, unidad/counidad con identidades triangulares.

## La definición: unit y counit

Dados dos funtores L : D → C y R : C → D, digo que L es **left adjoint** de R (notado L ⊣ R) cuando existen dos transformaciones naturales:

```
η : Id_D → R ∘ L (unit)
ε : L ∘ R → Id_C (counit)
```

que satisfacen las **identidades triangulares**:

```
ε_{L d} ∘ L(η_d) = id_{L d}
R(ε_c) ∘ η_{R c} = id_{R c}
```

La unit η aporta un morfismo canonico `η_d : d → R(L(d))`. No tiene por que ser
inyectivo/monomorfismo.

La counit ε aporta `ε_c : L(R(c)) → c`; tampoco tiene por que ser una
proyeccion o epimorfismo.

Las identidades triangulares dicen que dos compuestos especificos sobre `L` y
`R` son identidades. No dicen que cualquier objeto sobreviva sin perdida al
viaje redondo: `R ∘ L` y `L ∘ R` no son necesariamente identidades.

## La definición equivalente: isomorfismo de hom-sets

Hay una formulación alternativa que revela el significado profundo. L ⊣ R si y solo si hay un isomorfismo natural:

```
C(L d, c) ≅ D(d, R c)
```

para todo d en D y c en C. Es decir: los morfismos desde L(d) hacia c en C están en correspondencia biyectiva con los morfismos desde d hacia R(c) en D, y esta correspondencia es natural en ambas variables.

Esto dice algo extraordinario: **preguntar en C después de traducir con L equivale a preguntar en D antes de traducir con R**. Los dos funtores dan "vistas" del mismo fenómeno desde mundos distintos, y las vistas son perfectamente compatibles.

La conexión entre las dos definiciones es directa. De la isomorfía de hom-sets, tomando c = L(d), obtengo id_{L d} ∈ C(L d, L d) que corresponde a η_d ∈ D(d, R(L d)): eso es la unit. Tomando d = R(c), obtengo id_{R c} ∈ D(R c, R c) que corresponde a ε_c ∈ C(L(R c), c): eso es la counit.

## Conexiones de Galois: la adjunción más simple

La forma más elemental de adjunción ocurre entre preórdenes. Una **conexión de Galois** entre posets P y Q es un par de funciones monótonas f : P → Q y g : Q → P tales que:

```
f(p) ≤ q si y solo si p ≤ g(q)
```

Esto es exactamente la definición de adjunción con hom-sets reemplazados por la relación de orden (en un poset, el hom-set tiene a lo sumo un elemento). Fong y Spivak lo desarrollan en detalle: f es el left adjoint, g el right adjoint, y la composición g ∘ f : P → P es un **operador clausura** -- idempotente y extensivo.

Un ejemplo concreto: la función techo ⌈·⌉ : R → Z y la inclusión i : Z → R forman una conexión de Galois:

```
⌈x⌉ ≤ n si y solo si x ≤ i(n) = n
```

El left adjoint (techo) es la mejor aproximación entera por arriba compatible con el orden. El right adjoint (inclusión) preserva la estructura exacta. Dualmente, la inclusión es left adjoint de la función piso. Este patrón aparece en cada par de niveles de abstracción que manejo: un lado aproxima, el otro retiene estructura.

Para reticulos completos, un mapa monotono que preserva todos los meets
(incluido el vacio) es adjunto derecho. Fuera de esas hipotesis no se infiere
una adjuncion de que una operacion "parezca preservar".

## Free/forgetful: el arquetipo

El ejemplo más importante de adjunción en la práctica es el par **free/forgetful**. El funtor olvidadizo U : Mon → Set toma un monoide y devuelve su conjunto subyacente, olvidando la operación y la unidad. El funtor libre F : Set → Mon toma un conjunto de generadores y construye el monoide libre sobre él (todas las listas finitas con concatenación).

La adjunción F ⊣ U dice:

```
Mon(F(X), M) ≅ Set(X, U(M))
```

Un homomorfismo desde el monoide libre F(X) al monoide M está determinado por una función del conjunto generador X al conjunto subyacente de M. Es decir: para definir un homomorfismo desde algo libre, basta decir a dónde van los generadores. Todo lo demás se deduce de la estructura.

En Haskell, esto es concreto: `[a]` (listas finitas) es el monoide libre sobre `a`. Un homomorfismo de monoides `[a] → m` está determinado por una función `a → m` -- que es exactamente `foldMap`:

```haskell
foldMap :: (Monoid m) => (a -> m) -> [a] -> m
foldMap f = mconcat . map f
```

En la práctica, el patrón free/forgetful reaparece muchas veces. En algunos casos es una adjunción exacta; en otros, una lectura estructural útil pero no literal:

- **ORM / SQL**: suele haber una tensión de tipo free/forgetful entre el modelo de dominio y la representación tabular, pero rara vez una adjunción exacta. El **ORM drift** nombra precisamente la distancia entre ambos niveles cuando el viaje de ida y vuelta no preserva bien la estructura relevante.
- **AST / Source**: parser y pretty-printer exhiben un patrón ida-y-vuelta muy cercano al libre/olvido, aunque con detalles concretos de sintaxis, formato y comentarios que no siempre encajan en una adjunción limpia.
- **Docker image / Dockerfile**: el Dockerfile especifica un proceso generativo y la imagen es su resultado materializado; la analogía con libre/forgetful es útil para pensar la relación, pero no debe tomarse como identificación automática.

El patrón es: uno crea estructura libremente (sin imponer relaciones más allá de las leyes algebraicas mínimas), el otro olvida con gracia (retiene solo lo esencial). Cada vez que digo "X se genera a partir de Y", probablemente estoy mirando un left adjoint libre.

## Las adjunciones generan límites

Hay un resultado que conecta este documento con el anterior de manera profunda: **los right adjoints preservan límites y los left adjoints preservan colímites**.

Esto no es solo un teorema elegante -- tiene consecuencias prácticas inmediatas. Si sé que un funtor R es right adjoint, entonces automáticamente preserva productos, pullbacks, ecualizadores, y todo tipo de límite. No necesito verificar cada caso: la adjunción me lo da gratis.

Y el converso es casi cierto: el Adjoint Functor Theorem (que ya vimos para preórdenes) se generaliza. Si una categoría es completa y un funtor preserva todos los límites, bajo ciertas condiciones de tamaño, ese funtor es right adjoint. La preservación de estructura delata la adjunción.

En la práctica esto significa: si un funtor preserva sistemáticamente los límites relevantes y además se cumplen las hipótesis del teorema del adjunto, suele haber una pareja óptima esperándolo. La preservación de estructura es una señal fuerte; no un certificado automático por sí sola.

## Las adjunciones generan monads

Y hay otro resultado que anticipo aquí para el documento 09. Dada una adjunción L ⊣ R con unit η y counit ε, la composición T = R ∘ L es una monad:

```
T = R ∘ L : D → D
η : Id → T (unit de la monad)
μ = R ε L : T² → T (multiplication)
```

La monad codifica el "efecto" del viaje de ida y vuelta. Si L traduce "hacia abajo" y R traduce "de vuelta," T es la huella que deja el viaje redondo en el mundo original. No profundizo más aquí, pero esto explica por qué las monads aparecen en tantos lugares: cada adjunción genera una, y las adjunciones son ubicuas.

## La triple adjunción: Sigma ⊣ Delta ⊣ Pi

Y ahora la aplicación que considero la más importante para un arquitecto de sistemas: la **triple adjunción para migración funcional de datos**. Spivak demuestra que un funtor entre esquemas de bases de datos F : C → D induce tres funtores de migración:

```
Σ_F ⊣ Δ_F ⊣ Π_F
```

donde:

- **Δ_F** (pullback migration): tira datos de D-instancias a C-instancias por composición con F. Produce **proyecciones** automáticamente.
- **Σ_F** (left pushforward): empuja datos de C-instancias a D-instancias. Produce **uniones** y **Skolemiza** valores desconocidos.
- **Π_F** (right pushforward): empuja datos de C-instancias a D-instancias. Produce **joins** automáticamente.

El paper de Spivak lo ilustra con un ejemplo concreto. Si tengo un esquema C con dos tablas T1 (SSN, First, Last) y T2 (First, Last, Salary), y un esquema D con una sola tabla T que unifica ambas, entonces:

- Δ_F(J) reindexa/proyecta la instancia unificada sobre las entidades y
  atributos que F asigna a T1 y T2.
- Σ_F(I) toma la unión de T1 y T2 en una sola tabla, inventando variables Skolem para los campos que faltan (T1 no tiene Salary, T2 no tiene SSN).
- Π_F(I) hace el join de T1 y T2, quedándose solo con los registros que matchean en First y Last.

Una sutileza de Σ_F que merece atención: las variables Skolem que introduce no son los NULLs de SQL. Un NULL de SQL es ambiguo -- puede significar "no existe," "no lo sé," o "no aplica" -- y dos NULLs no son iguales entre sí (NULL ≠ NULL). Los **labelled nulls** de CQL son diferentes: cada uno es un valor fresco, tipado y distinguible (sk_1, sk_2, ...) que se comporta como una variable libre. Si más tarde aparece la información faltante, el labelled null puede unificarse con el valor real. La diferencia es operacional: los NULLs de SQL destruyen joins (NULL ≠ NULL rompe el equi-join); los labelled nulls los preservan (sk_1 = sk_1 funciona). La categoría distingue entre "no lo sé" y "no existe" con la precisión que SQL no tiene.

Brown, Spivak y Wisnesky implementan esto en CQL (Categorical Query Language), donde un script real de migración se ve así:

```
schema S = literal : empty {
 entities
 Employee Department
 foreign_keys
 worksIn : Employee -> Department
 attributes
 name : Employee -> Varchar
 dept_name : Department -> Varchar
}

mapping F = literal : S -> T { ... }

-- Δ_F produce la vista automáticamente
-- Σ_F produce la unión con nulls tipados
-- Π_F produce el join
```

Las adjunciones proporcionan unidades, counidades e identidades triangulares
para esos viajes. Son leyes de coherencia, no garantias de round-trip
lossless: unidad o counidad solo son isomorfismos bajo hipotesis adicionales.

## Qué preserva cada adjunto

La triple adjunción no solo migra datos -- transporta (o destruye) las constraints del esquema fuente. Y saber qué preserva cada operador antes de elegirlo es la diferencia entre una migración segura y una que introduce deuda técnica silenciosa.

Una constraint en el esquema fuente puede ser una path equation (dos caminos producen el mismo resultado), un monomorfismo (inyectividad, como UNIQUE), una condición de existencia formulada por límites, o una condición más extensional como la sobreyectividad. La pregunta es: si la constraint vale en el esquema fuente, ¿sigue valiendo después de migrar con Δ, Σ o Π? Aquí conviene ser cuidadoso: no todas las constraints se preservan por los mismos argumentos.

Lo garantizado al nivel de categorias de instancias es:

| Funtor | Garantia estructural |
|--------|-----------------------|
| `Δ_F` (precomposicion) | preserva limites y colimites calculados punto a punto |
| `Σ_F` (adjunto izquierdo) | preserva colimites |
| `Π_F` (adjunto derecho) | preserva limites |

Traducir `UNIQUE`, existencia, ecuaciones, nulabilidad o sobreyectividad a esas
formas requiere especificar la constraint y comprobar que cae bajo la
garantia. No existe una regla general "Δ/Π = integridad fuerte, Σ = perdida":
la eleccion depende del tipo de migracion y de la propiedad expresada.

## La doble categoría de los datos

La triple adjunción Σ ⊣ Δ ⊣ Π ya es poderosa. Pero hay una estructura más rica que contiene a los tres operadores como casos particulares, y que además integra las queries como ciudadanos de primera clase: la **doble categoría Data**.

Schultz, Spivak, Vasilakopoulou y Wisnesky demuestran que schemas, mappings y queries forman no una categoría sino una doble categoría -- una estructura con dos dimensiones de composición:

- **Objetos**: esquemas de bases de datos (categorías finitamente presentadas, posiblemente con teorías algebraicas).
- **Morfismos verticales**: mappings entre esquemas (funtores F : S → T). Son los que inducen la triple adjunción.
- **Morfismos horizontales**: bimodules (profuntores) M : S ⇸ T. Son las queries.
- **2-celdas**: transformaciones entre queries respetando los mappings.

La composición vertical es composición de funtores -- como siempre. Pero la composición horizontal es composición de profuntores vía coend:

```
(M ⊗ N)(s, t) = ∫^{r ∈ R} M(s, r) × N(r, t)
```

Esto dice: para componer dos queries M : S ⇸ R y N : R ⇸ T, integro sobre todos los objetos intermedios r de R, tomando los pares compatibles de M y N. Es el análogo categórico del JOIN transitivo -- si M selecciona empleados por departamento y N selecciona departamentos por región, M ⊗ N selecciona empleados por región, componiendo las relaciones.

La evaluación de una query M : R ⇸ S sobre una instancia I : S → Set es:

```
Γ_M(I) = ∫^{s ∈ S} M(-, s) × I(s)
```

Otro coend. Lo que conecta directamente con la maquinaria del documento 10 sobre ends y coends -- la evaluación de queries ES un coend, no por analogía sino por identidad. Cada uber-query (bimodule general que puede retornar múltiples tablas y referenciar otras queries) se evalúa con la misma fórmula.

El marco se llama **proarrow equipment** (o framed bicategory): Data es una doble categoría donde el funtor frame (L, R) : Data_1 → Data_0 × Data_0 es una fibración. Esto significa que cada mapping de esquemas F : S → T determina un bimodule canónico U_F : S ⇸ T (la unidad del equipment), y la composición de bimodules es compatible con la composición de mappings.

¿Por qué me importa esto como arquitecto? Porque el proarrow equipment unifica tres cosas que en la práctica manejo por separado:

1. **Migraciones** (funtores verticales) → transformaciones de esquema.
2. **Queries** (bimodules horizontales) → consultas composicionales.
3. **Vistas** (2-celdas) → queries parametrizadas por mappings.

En el equipment `Data` citado, mappings, bimodules y 2-celdas interactúan por
leyes precisas. Traducir DDL/DQL/vistas reales a esa estructura es trabajo
semántico adicional; solo las queries representadas por el modelo heredan la
transformación coherente.

## Adjunciones en la práctica cotidiana

Más allá de la migración de datos, las adjunciones organizan pares de operaciones que encuentro cada día:

**Compilar / Interpretar.** Muchas veces este par se deja leer con la geometría de una adjunción: un lado traduce a una forma más ejecutable o comprimida, el otro preserva semántica observable al reintroducir contexto. Pero la identificación exacta exige fijar con mucho cuidado las categorías implicadas.

**Normalizar / Desnormalizar.** Aquí también hay una tensión típica de ida y vuelta: un movimiento elimina redundancia y el otro la reintroduce por razones operativas. La analogía con una adjunción es fértil, aunque no debe leerse como teorema sin más.

**Comprimir / Expandir.** Compresión y expansión suelen comportarse como una pareja direccional muy asimétrica, útil para pensar en términos adjuntos, pero no toda pareja codec forma una adjunción categórica literal.

**Abstraer / Concretar.** Subir un nivel de abstracción y bajar a una implementación concreta es otro patrón que a menudo se deja leer como adjunto: un lado minimiza estructura, el otro la rellena. De nuevo, lo valioso aquí es la disciplina de diseño que la analogía revela.

**Currying como adjunción.** Anticipo aquí una estructura que el documento 07 formalizará como categoría cartesiana cerrada (CCC). Es quizás la adjunción más limpia:

```
C(A × B, C) ≅ C(A, C^B)
```

El funtor − × B (tomar producto con B) es left adjoint del funtor (−)^B (exponencial, o función desde B). Dar una función de dos argumentos es lo mismo que dar una función de un argumento que devuelve otra función. Esto es `curry`/`uncurry` en Haskell:

```haskell
curry :: ((a, b) -> c) -> a -> b -> c
uncurry :: (a -> b -> c) -> (a, b) -> c
```

Y la counit de esta adjunción es la función `eval`:

```haskell
eval :: (b -> c, b) -> c
eval (f, x) = f x
```

que toma un par (función, argumento) y produce el resultado. Es la eliminación del exponencial, exactamente como la counit elimina L ∘ R.

## El principio unificador

Una adjuncion caracteriza una correspondencia natural entre hom-sets. Puede
interpretarse como aproximacion universal en casos concretos, pero "optima" no
significa mejor rendimiento, fidelidad o menor perdida.

Algunos adjuntos izquierdos son libres/reflexiones y algunos derechos son
inclusiones/cofree; no todos admiten las lecturas "compacta", "fiel" o "pierde
menos". La afirmacion segura es la biyeccion natural y sus consecuencias
universales.

Cuando se demuestra una adjuncion, se que: (1) existe la biyeccion natural, (2)
el adjunto derecho preserva limites existentes, (3) `R ∘ L` induce una monada y
(4) unidad, counidad e identidades triangulares gobiernan el round-trip. No se
deduce que este sea invertible ni lossless.

Construcciones universales y adjunciones dan garantias precisas dentro de
categorias tipadas. Su traduccion a una decision de ingenieria conserva siempre
las hipotesis y metricas del dominio.

## Estatuto epistemico

- **Formal:** equivalencia entre hom-biyeccion y unidad/counidad, preservacion
  de limites/colimites y `Sigma ⊣ Delta ⊣ Pi` bajo sus hipotesis.
- **Modelo:** pares cotidianos, constraints de datos y "round-trips" solo tras
  construir categorias y probar las propiedades adicionales.
- **Metafora:** llamar adjuncion a cualquier ida/vuelta o atribuirle optimalidad
  operacional.
