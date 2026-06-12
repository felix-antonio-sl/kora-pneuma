# Ejemplo minimo — "El ORM perdio joins en la migracion"

Caso ilustrativo del workflow completo de la skill. **No es SSOT, solo ilustracion didactica.**

## Pregunta del usuario

> "Migramos del schema A (Postgres) al schema B (DynamoDB) usando un ORM. Las queries que antes hacian JOINs entre `orders` y `customers` ahora devuelven datos parciales o duplicados. ¿Que esta pasando estructuralmente?"

## `triaje`

Sintomas detectados:
- migracion entre schemas → composicion + preservacion.
- queries con JOIN → universales (pullback).
- "datos parciales o duplicados" → falla de preservacion de limites.

Hipotesis tematica: **preservacion de pullbacks bajo migracion**.

## `reformular-categorialmente`

Traduccion al vocabulario categorial:

- **Categoria origen** `S_A`: schema relacional A. Objetos = tablas; morfismos = foreign keys.
- **Categoria destino** `S_B`: schema documental B. Objetos = colecciones; morfismos = referencias entre documentos.
- **Funtor de migracion** `M: S_A → S_B`: induce el ORM al traducir tablas a colecciones.
- **JOIN** entre `orders` y `customers` sobre `customer_id` = pullback en la categoria de instancias `Inst(S_A) ≅ Set^S_A`.

Pregunta categorial reformulada:
> "¿Preserva `M` los pullbacks? ¿O sea, `M` es **continuo** sobre la categoria de instancias?"

## `localizar-corpus`

Por sintoma "migracion entre schemas pierde algo" → `urn:fxsl:kb:icas-preservacion`.
Por vocablo "pullback" → `urn:fxsl:kb:icas-universales`.
Por vocablo "migracion entre schemas como funtor" → `urn:fxsl:kb:icas-adjunciones` (Sigma-Delta-Pi).

Tres piezas relevantes; consultar las tres.

## `aplicar-patron`

### Patron 1: funtor que falla preservacion (`urn:fxsl:kb:icas-preservacion`)

El ORM induce un funtor `M: S_A → S_B` en la **presentacion** de los schemas. Pero la pregunta importante es si el funtor inducido `M*: Inst(S_A) → Inst(S_B)` sobre las instancias preserva limites finitos.

- Postgres con FKs y constraints corresponde a una categoria finitamente presentada con ecuaciones; las instancias son funtores a `Set` y forman una categoria con todos los limites.
- DynamoDB no tiene equivalente nativo de FK; las "referencias" no son morfismos de la presentacion sino convenciones de aplicacion. La categoria destino es mas pobre en estructura.
- El funtor `M*` colapsa la **path equivalence** que en `S_A` garantizaba que `customer_id` en `orders` apunta exactamente a un `customer`.

### Patron 2: pullback no se preserva (`urn:fxsl:kb:icas-universales`)

El JOIN `orders ⨝_{customer_id} customers` es el pullback del diagrama:

```
orders ──[customer_id]──> customers <──[id]── customers
```

En `S_B` (DynamoDB), los morfismos del diagrama no existen como tales (no hay FK). El "pullback computado por el ORM" es una **simulacion en aplicacion**: filtrar `orders` por algun atributo y juntar con consultas separadas a `customers`.

Esa simulacion no es el pullback universal. No tiene la propiedad de unicidad: si dos `customers` distintos tienen el mismo valor de `id` (o si la consulta es eventual), aparecen duplicados o faltantes.

### Patron 3: adjuncion rota (`urn:fxsl:kb:icas-adjunciones`)

La triple adjuncion `Σ ⊣ Δ ⊣ Π` exige que la migracion entre schemas sea funtorial sobre presentaciones cuyas instancias respeten limites.

- `Δ` (proyeccion / pullback de instancias) preserva todos los limites — pero requiere que el destino tenga la estructura.
- `Σ` (Skolem / coproducto) preserva colimites pero introduce *labelled nulls* cuando la informacion no se puede determinar.
- `Π` (push con join) preserva productos pero requiere computar pullbacks, lo que en `S_B` no es posible nativamente.

El ORM al migrar elige implicitamente uno de estos tres pero no el correcto para preservar JOINs.

## `validar-coherencia`

Aplicacion de `checklist-aplicacion.md`:

- [x] **CRITICO** categoria base identificada: `Set^{S_A}` y `Set^{S_B}` o equivalente para DynamoDB.
- [x] **CRITICO** objetos y morfismos tipificados (tablas/colecciones, FKs/refs).
- [x] **CRITICO** funtor `M` declarado preserva composicion e identidad **a nivel de presentacion**.
- [x] **CRITICO** se identifica que `M*` **no preserva pullbacks** (axioma de funtor de instancias roto).
- [x] **CRITICO** la propiedad universal del pullback se exhibe y se muestra que no se mantiene.
- [x] **CRITICO** cita explicita: `urn:fxsl:kb:icas-preservacion`, `urn:fxsl:kb:icas-universales`, `urn:fxsl:kb:icas-adjunciones`.
- [x] **CRITICO** lectura mas debil: el problema admite la lectura simple "funtor que pierde limites" sin necesidad de topos ni higher cats.

## `entregar`

### Diagnostico estructural

El ORM induce un funtor `M: S_A → S_B` que parece preservar la estructura del schema, pero el funtor inducido `M*: Inst(S_A) → Inst(S_B)` **no preserva pullbacks**. El JOIN computado en `S_B` es una simulacion en aplicacion, no el pullback universal de la categoria destino. La perdida de unicidad da datos parciales (cuando la simulacion no encuentra la referencia) o duplicados (cuando encuentra mas de una).

### Patron canonico aplicable

**`urn:fxsl:kb:icas-preservacion`**: el ORM tiene un funtor sin la propiedad de preservacion de limites. Si quieres preservar JOINs, necesitas un destino con suficiente estructura (categoria con pullbacks) o explicitar la perdida.

### Checklist de coherencia que el sistema debe satisfacer

1. Si el destino no tiene pullbacks nativos, **explicitar** que los JOINs se simulan y no son universales.
2. Si la simulacion de JOIN debe ser determinista, garantizar **unicidad** de las referencias (constraint a nivel de aplicacion que reemplaza el FK).
3. Si la consistencia se relaja a *eventual*, modelar el destino como **topos** con clasificador no-booleano (`urn:fxsl:kb:icas-topoi`) — la verdad de "este order tiene este customer" es ahora un grado, no booleana.

### Alternativas comparadas

| Alternativa | Tradeoff categorial |
|-------------|---------------------|
| mantener Postgres | preserva pullbacks; pierde escalabilidad horizontal |
| migrar a DynamoDB con denormalizacion | pierde pullbacks; gana coproductos eficientes |
| migrar a DynamoDB + capa de adjuncion en aplicacion | reintroduce pullbacks via aplicacion; complica el `Σ-Δ-Π`; pierde garantia formal |
| usar base de datos categorial (CQL, AlgebraicJulia) | preserva todo Sigma-Delta-Pi; coste de adopcion alto |

### Distincion formal vs heuristica

- **Formal**: que el ORM no preserva pullbacks bajo `M*` es teorema (depende de la presentacion exacta de `S_B`).
- **Heuristica**: que "denormalizar" sea la respuesta correcta depende del dominio y del trade-off latencia/consistencia.

### Citas

- `urn:fxsl:kb:icas-preservacion` — funtores que pierden estructura; cuando declarar la perdida.
- `urn:fxsl:kb:icas-universales` — propiedad universal de pullback; cuando se pierde universalidad.
- `urn:fxsl:kb:icas-adjunciones` — triple `Σ-Δ-Π` y migracion entre schemas como adjuncion.

---

**Nota**: este es un ejemplo didactico. En un caso real, `cat-thinking` consultaria con `Read` los archivos de las URNs citadas para confirmar los detalles antes de afirmar el diagnostico.
