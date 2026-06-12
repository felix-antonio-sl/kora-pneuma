---
urn: urn:fxsl:kb:icas-preservacion
nombre: icas-preservacion
version: 1.0.0
estado: publicado
descripcion: "Pieza 02 del ICAS-BoK: funtores y preservación de estructura — faithful/full, schema→instancia y migraciones; qué se preserva o se pierde al traducir entre sistemas."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/02-preservacion.md (sha256:9b4d56be662f49eaef894708d4673b50277b76e11f78088a5b2b0902940ee5dd) el 2026-06-12; cuerpo byte-fiel. Fuente original: ICAS-BoK corpus — Fong/Spivak, Mac Lane, Barbosa, Awodey, Riehl"
autor: FS
creado: 2026-04-14
lang: es
tags: [funtor, faithfulness, fullness, traduccion, ICAS-BoK, teoria-categorias, corpus-categorico]
familia: bok
---

# Preservacion

Si la composicion es lo que veo primero, la preservacion es lo segundo: que se mantiene cuando paso de un mundo a otro. Cuando migro un schema de base de datos, cuando compilo codigo a bytecode, cuando serializo un objeto a JSON, cuando construyo una vista SQL sobre tablas base --- en cada caso estoy mapeando de un mundo a otro. La pregunta que me obsesiona es: que se preservo en la traduccion? Que se perdio? Y lo que se perdio, se perdio intencionalmente o por accidente?

Esa pregunta tiene una respuesta precisa. Se llama functor.

## El patron que aparece en todas partes

Tengo dos categorias --- dos mundos con sus objetos, sus morfismos, su composicion. Un **functor** F: C -> D es un mapeo que respeta la estructura. Concretamente:

- A cada objeto A en C le asigna un objeto F(A) en D.
- A cada morfismo f: A -> B en C le asigna un morfismo F(f): F(A) -> F(B) en D.

Pero no cualquier mapeo sirve. El functor debe satisfacer dos leyes --- las mismas que vi en la composicion, pero ahora como condiciones de preservacion:

**Preservacion de composicion:** F(g . f) = F(g) . F(f). Si compongo primero y luego mapeo, obtengo lo mismo que si mapeo primero y luego compongo.

**Preservacion de identidad:** F(id_A) = id_{F(A)}. La identidad en el mundo de origen se mapea a la identidad en el mundo de destino.

Estas dos leyes son un TEST. Cuando construyo un mapeo entre dos sistemas y quiero saber si "se porta bien", le aplico estas leyes. Si las satisface, es un functor. Si no, es un mapeo ad hoc que puede romper invariantes sin que me de cuenta.

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

En bases de datos: una consulta SELECT es un functor covariante (produce filas), pero un predicado WHERE es contravariante (consume filas para producir un booleano). Si cambio el schema agregando una columna, las queries que producen datos se adaptan covariantemente, pero los filtros que consumen datos se adaptan contravariantemente.

## Cuanta estructura preserva un functor

No todos los functores preservan la misma cantidad de informacion. Hay un espectro:

**Faithful (fiel).** Un functor es faithful si la funcion sobre morfismos es inyectiva: morfismos distintos en C se mapean a morfismos distintos en D. No se colapsan flechas. Puedo distinguir relaciones del mundo de origen mirando el mundo de destino.

**Full (pleno).** Un functor es full si la funcion sobre morfismos es sobreyectiva: todo morfismo entre F(A) y F(B) en D proviene de algun morfismo entre A y B en C. No hay relaciones en el destino que no existieran en el origen.

**Essentially surjective (esencialmente sobreyectivo).** Todo objeto en D es isomorfo a la imagen de algun objeto en C. No hay objetos "nuevos" en el destino (salvo renombramientos).

Un functor que es faithful, full, y essentially surjective es una equivalencia de categorias --- la nocion de "son la misma cosa, salvo detalles inesenciales" en matematica categorica.

En la practica, la mayoria de los functores que encuentro son fieles pero no plenos. Un ORM que mapea un schema relacional a clases de objetos es tipicamente faithful (relaciones distintas se mapean a metodos distintos) pero no full (hay operaciones sobre objetos que no corresponden a ninguna relacion en el schema). Y eso esta bien: el punto no es preservar todo, sino saber exactamente que se preserva y que no.

## Functores que olvidan y functores que crean

Dos patrones aparecen una y otra vez en mi practica:

**Forgetful functors** (functores de olvido). Toman una estructura rica y olvidan parte de ella. El ejemplo clasico: tomo un grupo (conjunto con operacion, inversos, identidad) y olvido la operacion, quedandome solo con el conjunto subyacente. En bases de datos, una vista que selecciona solo algunas columnas es un functor de olvido: preserva las filas y sus relaciones, pero olvida columnas.

```sql
-- Functor de olvido: Employee tiene (id, name, email, dept_id, salary)
-- La vista olvida salary y email
CREATE VIEW employee_directory AS
 SELECT id, name, dept_id FROM employee;
```

La vista preserva la composicion de foreign keys (puedo seguir haciendo JOINs a traves de dept_id) pero olvido informacion. Es un functor honesto: cumple las leyes.

**Free functors** (functores libres). Van en la direccion opuesta: toman una estructura simple y la completan libremente con la minima cantidad de estructura necesaria para satisfacer las leyes. Un grafo dirigido genera una categoria libre: los objetos son los vertices, los morfismos son los caminos (secuencias de flechas), y la composicion es la concatenacion de caminos. No se impone ninguna ecuacion --- es la categoria mas libre posible compatible con el grafo.

Milewski describe esto con claridad: dado cualquier grafo dirigido, agrego una identidad en cada nodo y luego, para cada par de flechas componibles, agrego la flecha de composicion. "You usually end up with infinitely many arrows, but that's okay." La categoria libre generada por un grafo captura toda la informacion composicional del grafo sin imponer restricciones adicionales.

Los functores de olvido y los functores libres viven en tension creativa. El functor libre construye; el functor de olvido deconstruye. Esa tension es uno de los motores mas profundos de la teoria --- las adjunciones entre functores libres y de olvido --- pero ese tema viene despues. Por ahora basta con reconocer el patron: cada vez que "genero algo libremente" o "olvido estructura," estoy trabajando con un functor.

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

Las leyes del functor garantizan automaticamente la integridad referencial. Si tengo dos caminos en el schema que son declarados equivalentes (path equivalence), el functor asegura que las funciones correspondientes tambien son iguales. Esta es la idea central de Spivak: la integridad referencial no es un conjunto de checks ad hoc, sino una consecuencia automatica de la functorialidad.

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

Este DDL define una categoria con objetos {Employee, Department, String, Integer} y morfismos {first_name, last_name, dept_id, manager_id, name}. Una instancia --- los datos concretos --- es un functor a Set. Si agrego la path equivalence `manager.dept = dept` (el manager de un empleado esta en el mismo departamento), toda instancia valida debe satisfacer esa ecuacion functorialmente: la funcion compuesta I(manager) seguida de I(dept) debe ser igual a I(dept).

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

Cuando tengo un mapeo entre dos schemas --- una traduccion F: C -> D que envia tablas a tablas y columnas a columnas, preservando las ecuaciones --- Spivak demuestra que se inducen automaticamente tres functores de migracion de datos:

- **Delta_F (pullback):** tira instancias de D hacia C. Automaticamente produce proyecciones. Si F fusiona dos tablas T1 y T2 en una sola tabla T, Delta_F separa los datos de T de vuelta en T1 y T2.
- **Sigma_F (left pushforward):** empuja instancias de C hacia D. Automaticamente produce uniones, y Skolemiza valores desconocidos.
- **Pi_F (right pushforward):** empuja instancias de C hacia D. Automaticamente produce joins.

La belleza de esto es que los tres functores de migracion son *determinados* por la traduccion de schemas F. No necesito escribir queries de migracion ad hoc. La migracion emerge del mapeo entre categorias. Y las propiedades de "round-trip" (composiciones Delta-Pi y Delta-Sigma) se demuestran como consecuencias de adjunciones entre los functores.

## Functores en la ingenieria cotidiana

**ORMs como functores.** Un ORM mapea el schema relacional (una categoria) a clases y metodos en un lenguaje orientado a objetos (otra categoria). Las tablas se mapean a clases. Las foreign keys se mapean a propiedades de navegacion. La composicion se preserva: si `employee.department.company` es un camino en el schema, el ORM produce `employee.getDepartment.getCompany` en el mundo de objetos. Cuando un ORM "pierde" informacion (no expone ciertas relaciones, o introduce N+1 queries), es porque el functor no es faithful o porque la implementacion viola las leyes.

**Compiladores como functores.** Un compilador mapea la categoria de tipos y funciones del lenguaje fuente a la categoria de tipos y operaciones del bytecode. La composicion debe preservarse: compilar `g . f` debe producir lo mismo que compilar `f`, compilar `g`, y componer los resultados. La preservacion de identidad asegura que las funciones identidad se compilan a no-ops. Un compilador que viola estas leyes genera codigo incorrecto.

**Serializacion como functor.** `JSON.stringify` en JavaScript es (idealmente) un functor de la categoria de valores JS a la categoria de strings JSON. Si serializo un objeto compuesto, el resultado debe ser compatible con serializar las partes y componer. Cuando la serializacion falla en tipos ciclicos o pierde informacion de tipo, el functor deja de cumplir las leyes.

**Docker image layers.** Cada instruccion en un Dockerfile transforma un filesystem en otro. El mapeo de un Dockerfile multi-stage a su imagen final es un functor: preserva la composicion de layers (la composicion de transformaciones de filesystem es la transformacion total) y preserva las identidades (una instruccion que no modifica nada produce un layer vacio).

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

Las leyes del functor dicen exactamente lo que vi en la composicion: preserva identidades y preserva la composicion asociativa. Eso es todo. Y ese "todo" es extraordinariamente poderoso, porque me permite razonar sobre el mapeo sin inspeccionar cada caso particular. Si se que mi ORM es un functor faithful, se que puedo reconstruir el schema a partir de las clases. Si se que mi compilador es un functor que preserva composicion, se que puedo razonar sobre el programa fuente y confiar en que el ejecutable se comporta igual.

La preservacion no es un lujo teorico. Es la condicion minima para que una traduccion entre mundos sea confiable. Y cuando la traduccion no es un functor --- cuando el ORM pierde joins, cuando el serializador descarta campos, cuando la migracion de datos introduce inconsistencias --- ahora tengo el vocabulario para diagnosticar exactamente que fallo: la ley de composicion, la ley de identidad, la faithfulness, la fullness. Cada falla tiene un nombre y un remedio.
