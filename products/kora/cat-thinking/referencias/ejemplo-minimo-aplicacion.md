# Ejemplo minimo — "El ORM perdio joins en la migracion"

Caso ilustrativo del workflow completo. Su proposito es mostrar como **no
confundir un modelo candidato con un diagnostico demostrado**.

## Pregunta del usuario

> "Migramos del schema A (Postgres) al schema B (DynamoDB) usando un ORM.
> Las queries que antes hacian JOINs entre `orders` y `customers` ahora
> devuelven datos parciales o duplicados. ¿Que esta pasando estructuralmente?"

## `triaje`

Sintomas:

- hubo traduccion de schema y datos;
- cambio la implementacion de una consulta con JOIN;
- aparecen faltantes o duplicados.

Antes de categorizar, hay que obtener evidencia:

1. DDL, claves, unicidad, nulabilidad y cardinalidades del origen;
2. claves, indices, denormalizacion y modo de consistencia del destino;
3. mapping exacto del ORM y codigo de lectura/escritura;
4. filas/documentos concretos que reproducen faltantes y duplicados.

Sin esos datos, "el ORM no preserva pullbacks" es una **hipotesis**, no una
conclusion.

## `reformular-categorialmente`

### Construccion formal minima

En `Set`, si existen funciones

```text
customer_id : Orders    -> CustomerId
id          : Customers -> CustomerId
```

el conjunto de pares compatibles es el pullback:

```text
Orders x_CustomerId Customers
```

Su propiedad universal dice que cualquier conjunto `X` con mapas compatibles
a `Orders` y `Customers` factoriza por un unico mapa hacia ese conjunto de
pares.

Esta construccion modela un inner join sencillo bajo supuestos explicitos:
tablas como conjuntos, igualdad ordinaria de claves y sin semantica adicional
de `NULL`, multiplicidades (*bags*) u outer joins. SQL real puede exigir una
categoria/modelo distinto.

### Pregunta reformulada

> "¿La implementacion destino conserva la relacion de compatibilidad y las
> restricciones de unicidad/referencia que necesita la consulta?"

Solo despues de definir categorias de schemas/instancias y la accion de la
migracion sobre objetos **y morfismos** corresponde preguntar si existe un
funtor y si preserva ese pullback.

## `localizar-corpus`

- `urn:fxsl:kb:icas-preservacion`: propiedades que una traduccion puede
  preservar o perder.
- `urn:fxsl:kb:icas-universales`: definicion y prueba de pullback.
- `urn:fxsl:kb:icas-adjunciones`: migracion funtorial de datos
  `Sigma-Delta-Pi`, si se han construido los schemas categoriales.

Las URNs permiten navegar el corpus; no prueban el diagnostico.

## `aplicar-patron`

### Diagnostico operacional primero

Comparar el contraejemplo concreto con estas causas independientes:

- falta una restriccion de unicidad equivalente a `Customers.id`;
- se perdieron o duplicaron referencias durante la escritura;
- la consulta hace varias lecturas con una ventana de consistencia distinta;
- la denormalizacion produce copias no sincronizadas;
- el ORM cambio semantica de nulos, cardinalidad o multiplicidad.

Encontrar una de estas causas basta para intervenir. No hace falta promover el
mapping a funtor.

### Lectura categorial, si los datos la soportan

Si se construyen categorias `S_A`, `S_B` y un funtor de schemas `F`, su accion
sobre instancias debe especificarse con direccion y tipos exactos. Entonces
puede formularse y probarse una afirmacion de preservacion de limites para el
funtor de instancias pertinente. No se deduce de que exista un ORM ni de que
ambos sistemas almacenen datos.

Un contraejemplo suficiente seria un diagrama cuyo pullback en el modelo de
origen, al migrarse, no satisfaga la propiedad universal en el modelo destino.
Faltantes o duplicados observados son evidencia inicial, pero no sustituyen
esa prueba.

## `validar-coherencia`

- [x] **formal**: el pullback en `Set` y su propiedad universal estan
  tipificados.
- [x] **modelo**: el inner join se representa por ese pullback solo bajo los
  supuestos declarados.
- [ ] **formal pendiente**: categorias exactas de origen/destino y funtor de
  migracion.
- [ ] **formal pendiente**: prueba o contraejemplo de preservacion.
- [x] **operacional**: existe un plan de evidencia que puede localizar la causa
  sin sobre-formalizar.

## `entregar`

### Diagnostico responsable

La señal apunta a una restriccion o relacion de compatibilidad que la
migracion/consulta destino no reproduce. El pullback es un buen **modelo
candidato** para el inner join simple, pero aun no se ha demostrado que el ORM
induzca un funtor ni que su falla sea "no preservar pullbacks".

### Intervencion

1. reproducir un faltante y un duplicado con sus claves;
2. comprobar unicidad, referencia y consistencia en cada etapa;
3. restaurar la restriccion o cambiar la estrategia de lectura/escritura;
4. solo si se necesita una garantia reusable, formalizar los schemas y probar
   la preservacion pertinente.

### Estatuto epistemico

| Afirmacion | Estatuto |
|------------|----------|
| el conjunto de pares compatibles es un pullback en `Set` | formal |
| ese pullback modela el inner join descrito | modelo, bajo supuestos |
| el ORM concreto no preserva pullbacks | hipotesis no demostrada |
| falta una constraint, hay lag o copias divergentes | hipotesis operacional a contrastar |

### Fuente primaria

Para pullbacks y propiedades universales: Emily Riehl, *Category Theory in
Context*, capitulos 3–4,
<https://emilyriehl.github.io/files/context.pdf>.

---

El ejemplo enseña el orden correcto: evidencia concreta, construccion tipada,
estatuto epistemico y recien entonces lenguaje categorial fuerte.
