---
urn: urn:fxsl:kb:icas-preservacion
nombre: icas-preservacion
version: 1.1.0
estado: publicado
descripcion: "Pieza 02 del ICAS-BoK: funtores y preservación de estructura — faithful/full, schema→instancia y migraciones; qué se preserva o se pierde al traducir entre sistemas."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/02-preservacion.md (sha256:9b4d56be662f49eaef894708d4673b50277b76e11f78088a5b2b0902940ee5dd) el 2026-06-12. v1.1.0 (2026-07-18): corrige la promocion automatica de ORM, compilador, serializador, SQL y Docker a funtores y delimita faithful/full."
autor: FS
creado: 2026-04-14
lang: es
tags: [funtor, faithfulness, fullness, traduccion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Preservacion

Si la composicion es lo que veo primero, la preservacion es lo segundo: que se mantiene cuando paso de un mundo a otro. Cuando migro un schema de base de datos, cuando compilo codigo a bytecode, cuando serializo un objeto a JSON, cuando construyo una vista SQL sobre tablas base --- en cada caso estoy mapeando de un mundo a otro. La pregunta que me obsesiona es: que se preservo en la traduccion? Que se perdio? Y lo que se perdio, se perdio intencionalmente o por accidente?

Una respuesta estructural posible es construir un funtor y preguntar que
propiedades adicionales preserva. No toda traduccion cotidiana induce uno.

## El patron que aparece en todas partes

Tengo dos categorias --- dos mundos con sus objetos, sus morfismos, su composicion. Un **functor** F: C -> D es un mapeo que respeta la estructura. Concretamente:

- A cada objeto A en C le asigna un objeto F(A) en D.
- A cada morfismo f: A -> B en C le asigna un morfismo F(f): F(A) -> F(B) en D.

Pero no cualquier mapeo sirve. El functor debe satisfacer dos leyes --- las mismas que vi en la composicion, pero ahora como condiciones de preservacion:

**Preservacion de composicion:** F(g . f) = F(g) . F(f). Si compongo primero y luego mapeo, obtengo lo mismo que si mapeo primero y luego compongo.

**Preservacion de identidad:** F(id_A) = id_{F(A)}. La identidad en el mundo de origen se mapea a la identidad en el mundo de destino.

Estas dos leyes son el test de **functorialidad**, no de correccion general. Si
se satisfacen, hay un funtor; si no, debe usarse un tipo de transformacion mas
debil y verificar sus invariantes por otros medios.

En Haskell, esta idea se materializa en la typeclass `Functor`:

```haskell
class Functor f where
 fmap :: (a -> b) -> f a -> f b

-- Las leyes del functor:
-- fmap id == id -- preserva identidad
-- fmap (g . f) == fmap g . fmap f -- preserva composicion
```

El `fmap` ES la accion del functor sobre los morfismos. Dado un type constructor `f` (la accion sobre objetos) y un `fmap` (la accion sobre morfismos) que satisfaga las dos leyes, tengo un functor. El compilador de Haskell no verifica las leyes --- esa es responsabilidad del programador. Pero las leyes estan ahi como garantia: si `fmap` las cumple, puedo razonar ecuacionalmente sobre mi codigo con total confianza.

El ejemplo mas claro es `Maybe`:

```haskell
instance Functor Maybe where
 fmap _ Nothing = Nothing
 fmap f (Just x) = Just (f x)
```

Si tengo una funcion `f :: a -> b`, `fmap f` la levanta al mundo de los valores opcionales: `Maybe a -> Maybe b`. Si el valor existe, aplico `f`; si no existe, propago la ausencia. Las leyes se verifican por razonamiento ecuacional --- Milewski lo demuestra caso por caso, y la prueba es casi trivial, lo cual es la senal de que la abstraccion es correcta.

La lista es otro functor:

```haskell
instance Functor [] where
 fmap _ [] = []
 fmap f (x:xs) = f x : fmap f xs
```

Aplicar `fmap f` a una lista aplica `f` a cada elemento. La composicion se preserva: aplicar `fmap (g . f)` es lo mismo que aplicar `fmap f` y luego `fmap g`. Esto no es un accidente --- es la ley del functor actuando.

## Covarianza y contravarianza

No todos los functores preservan la direccion de las flechas. Un **functor covariante** (el caso comun, el que acabo de describir) mapea f: A -> B a F(f): F(A) -> F(B) --- misma direccion. Pero un **functor contravariante** invierte las flechas: mapea f: A -> B a F(f): F(B) -> F(A).

Formalmente, un functor contravariante F: C -> D es lo mismo que un functor covariante F: C^op -> D. Esto conecta directamente con la dualidad que vi en la composicion: la contravarianza es un functor que ve el mundo de origen a traves de la categoria opuesta.

En la practica, la contravarianza aparece constantemente:

```haskell
-- Functor covariante: produce valores de tipo a
newtype Producer a = Producer (IO a)
-- Si tengo f :: a -> b, puedo mapear: Producer a -> Producer b

-- Functor contravariante: consume valores de tipo a
newtype Consumer a = Consumer (a -> IO )
-- Si tengo f :: a -> b, mapeo al reves: Consumer b -> Consumer a
```

Un `Consumer` de `String` se convierte en un `Consumer` de `Int` si tengo una funcion `show :: Int -> String`. La flecha se invierte: la funcion va de `Int` a `String`, pero el consumer va de `Consumer String` a `Consumer Int`. Esto es contravarianza pura.

En bases de datos, covarianza o contravarianza solo se afirma despues de definir una categoria de schemas/consultas y la accion sobre morfismos. `SELECT` y `WHERE` por si solos no son funtores ni determinan su varianza.

## Cuanta estructura preserva un functor

No todos los functores preservan la misma cantidad de informacion. Hay un espectro:

**Faithful (fiel).** Un functor es faithful si la funcion sobre morfismos es inyectiva: morfismos distintos en C se mapean a morfismos distintos en D. No se colapsan flechas. Puedo distinguir relaciones del mundo de origen mirando el mundo de destino.

**Full (pleno).** Un functor es full si la funcion sobre morfismos es sobreyectiva: todo morfismo entre F(A) y F(B) en D proviene de algun morfismo entre A y B en C. No hay relaciones en el destino que no existieran en el origen.

**Essentially surjective (esencialmente sobreyectivo).** Todo objeto en D es isomorfo a la imagen de algun objeto en C. No hay objetos "nuevos" en el destino (salvo renombramientos).

Un functor que es faithful, full, y essentially surjective es una equivalencia de categorias --- la nocion de "son la misma cosa, salvo detalles inesenciales" en matematica categorica.

No debe inferirse fidelidad o plenitud de una intuicion de "perdida". Ambas propiedades se calculan por hom-set para un funtor ya construido. Un ORM concreto puede no inducir siquiera las categorias o la accion funtorial supuestas.

## Functores que olvidan y functores que crean

Dos patrones aparecen una y otra vez en mi practica:

**Forgetful functors** (functores de olvido). Toman una estructura rica y olvidan parte de ella. El ejemplo clasico: tomo un grupo y olvido su operacion, quedandome con el conjunto subyacente. Una proyeccion de schema/instancias puede modelarse de este modo si se especifican sus categorias y accion; una vista SQL aislada no basta.

```sql
-- Functor de olvido: Employee tiene (id, name, email, dept_id, salary)
-- La vista olvida salary y email
CREATE VIEW employee_directory AS
 SELECT id, name, dept_id FROM employee;
```

En un modelo concreto debe comprobarse si la vista preserva las claves y composiciones relevantes. El ejemplo no demuestra por si solo las leyes.

**Free functors** (functores libres). Van en la direccion opuesta: toman una estructura simple y la completan libremente con la minima cantidad de estructura necesaria para satisfacer las leyes. Un grafo dirigido genera una categoria libre: los objetos son los vertices, los morfismos son los caminos (secuencias de flechas), y la composicion es la concatenacion de caminos. No se impone ninguna ecuacion --- es la categoria mas libre posible compatible con el grafo.

Milewski describe esto con claridad: dado cualquier grafo dirigido, agrego una identidad en cada nodo y luego, para cada par de flechas componibles, agrego la flecha de composicion. "You usually end up with infinitely many arrows, but that's okay." La categoria libre generada por un grafo captura toda la informacion composicional del grafo sin imponer restricciones adicionales.

Muchas construcciones libres son adjuntas izquierdas a funtores de olvido, pero no todo acto informal de "generar" u "olvidar" define esa adjuncion.

## El patron schema/instancia

El ejemplo mas importante de functor en mi practica cotidiana no viene de Haskell ni de tipos abstractos. Viene de bases de datos. Y lo debo a David Spivak.

Un **database schema** en forma normal categorica es una categoria finitamente presentada. Las tablas son objetos. Las columnas (foreign keys) son morfismos. Los path equivalences son ecuaciones. Spivak proporciona un diccionario preciso:

| Concepto DB | Concepto CT |
|---|---|
| Database schema | Categoria C (finitamente presentada) |
| Tabla | Objeto en C |
| Columna / Foreign key | Morfismo en C |
| Path equivalence | Ecuacion de composicion |
| Database instance | Functor I: C -> Set |
| Fila en tabla T | Elemento de I(T) |
| Valor en columna c | Aplicacion de I(c) a un elemento |

La linea clave: una **database instance** es un functor I: C -> Set. A cada tabla T le asigna un conjunto I(T) --- el conjunto de filas. A cada foreign key f: T -> U le asigna una funcion I(f): I(T) -> I(U) --- la funcion que, dada una fila de T, devuelve la fila referenciada en U.

Las leyes del funtor garantizan que las ecuaciones de caminos declaradas se respeten en la instancia y que cada flecha se interprete como funcion total. Esto cubre una nocion precisa de integridad en el modelo categorial; no engloba automaticamente toda constraint o semantica SQL.

Consideremos un schema concreto:

```sql
CREATE TABLE department (
 id SERIAL PRIMARY KEY,
 name TEXT NOT NULL
);

CREATE TABLE employee (
 id SERIAL PRIMARY KEY,
 first_name TEXT,
 last_name TEXT,
 dept_id INTEGER REFERENCES department(id),
 manager_id INTEGER REFERENCES employee(id)
);
```

Este DDL no define directamente esa categoría a `Set`: `dept_id`,
`manager_id`, `first_name` y `last_name` admiten `NULL`, luego se interpretan
como relaciones parciales u opciones, no como funciones totales. Tras declarar
columnas `NOT NULL` o modelar explícitamente la parcialidad, puede presentarse
un schema con esos generadores. Si además se agrega
`manager ; dept = dept`, las instancias categoriales deben satisfacer esa
ecuación; SQL solo la hará cumplir si se materializa el constraint adecuado.

En Julia/Catlab, el schema se declara como una categoria presentada:

```julia
@present CompanySchema(FreeSchema) begin
 Employee::Ob
 Department::Ob

 dept::Hom(Employee, Department)
 manager::Hom(Employee, Employee)
 name::Hom(Department, StringType)

 compose(manager, dept) == dept -- path equivalence
end
```

Y una instancia es un functor de esta categoria a FinSet. Los datos SE CONVIERTEN en un functor. No es una metafora --- es la definicion.

## Migracion de datos como composicion de functores

En las categorías de instancias usadas por el modelo, un funtor de schemas
`F:C->D` induce `Delta_F` por precomposición y, cuando existen las extensiones
de Kan relevantes, sus adjuntos `Sigma_F` y `Pi_F`:

- **Delta_F (precomposicion):** tira instancias de D hacia C mediante `I ↦ I ∘ F`. Si F envia dos objetos a uno, ambos reciben el mismo conjunto subyacente bajo la precomposicion; eso no "separa" datos por si solo.
- **Sigma_F (left pushforward):** extensión de Kan izquierda; en la
  presentación CQL del ejemplo produce uniones y labelled nulls.
- **Pi_F (right pushforward):** extensión de Kan derecha; en ese ejemplo
  produce el join indicado.

Cuando existen, estas construcciones quedan determinadas hasta isomorfismo por
su universalidad. Unit y counit dan leyes de round-trip, pero no son
isomorfismos ni garantizan migración lossless sin hipótesis adicionales.

## Candidatos en la ingenieria cotidiana

ORMs, compiladores, serializadores y builders de imagen pueden admitir modelos
funtoriales, pero el sustantivo no aporta la prueba. Para cada caso hay que
declarar:

1. categorias origen y destino;
2. accion sobre objetos y morfismos;
3. preservacion de identidad y composicion;
4. propiedad semantica adicional requerida.

Las dos leyes funtoriales no garantizan por si solas que un compilador preserve
la semantica, que una serializacion sea reversible o que un ORM evite N+1.
Esas son propiedades adicionales (correccion semantica, inversa/embedding,
coste operacional, etc.).

**`fmap` en la practica.** Cuando escribo `map` sobre una lista en cualquier lenguaje, estoy aplicando un functor. Cuando uso `Promise.then` o `async/await`, estoy dentro de un functor (de hecho, dentro de algo mas fuerte --- pero la parte functorial es lo que preserva la composicion de transformaciones asincronas). Cada vez que "levanto" una funcion ordinaria para que opere sobre valores envueltos en un contexto (Maybe, List, Promise, Result, Stream), estoy usando `fmap`.

```haskell
-- Levantar una funcion pura al mundo de IO
fmap (+1) (readLn :: IO Int) -- lee un entero y le suma 1

-- Levantar al mundo de listas
fmap (*2) [1,2,3] -- [2,4,6]

-- Levantar al mundo de Maybe
fmap show (Just 42) -- Just "42"
fmap show Nothing -- Nothing
```

Cada una de estas lineas es la misma idea: un functor que preserva composicion e identidad, aplicado a un contexto particular.

## Lo que me dice la preservacion

El functor es mi herramienta de diagnostico. Cuando construyo un mapeo entre dos sistemas --- entre un schema y su ORM, entre un DSL y su compilacion, entre un modelo de dominio y su serializacion --- me pregunto: es esto un functor? Si lo es, tengo garantias de coherencia automatica. Si no lo es, necesito entender que ley se violo y por que.

Las leyes del funtor preservan identidades y composicion. Ser fiel solo impide colapsar morfismos dentro de cada hom-set; no permite reconstruir objetos ni un schema completo. De igual modo, la functorialidad de un compilador no basta para concluir equivalencia semantica entre fuente y ejecutable.

La functorialidad es una garantia estructural precisa, no una certificacion general de confiabilidad. Una traduccion puede perder informacion siendo un funtor perfectamente legal, y *faithful/full* solo se preguntan despues de construirlo. El diagnostico responsable identifica primero la propiedad concreta que se perdio y luego comprueba si el vocabulario categorial aplica.

## Estatuto epistemico

- **Formal:** definicion de funtor, fidelidad/plenitud, instancias `C -> Set`
  y la triple de migracion bajo sus hipotesis.
- **Modelo:** ORM, compilador, serializador, vista o layer solo tras construir
  categorias y acciones.
- **Heuristica:** atribuir cualquier perdida a una "ley de funtor rota".
