# Checklist de aplicacion — verificar que la lectura categorial es correcta

Usar despues de aplicar un patron del corpus, antes de entregar al agente invocador. Marca con tres niveles: **CRITICO** (debe pasar), **MEDIO** (debe pasar o declararse explicitamente), **BAJO** (recomendable).

## Bloque 1 — Identificacion

- [ ] **CRITICO** la **categoria base** del problema esta identificada explicitamente (Set, Cat, Vect, Cost, Bool, topos T, etc.).
- [ ] **CRITICO** los **objetos** del problema estan tipificados (servicios, tablas, tipos, valores efectados, configuraciones, ...).
- [ ] **CRITICO** los **morfismos** estan tipificados (calls, FKs, funciones, queries, transitions, ...).
- [ ] **MEDIO** se declara si la categoria es enriquecida y sobre que base.
- [ ] **MEDIO** se declara si la categoria es 1-cat / 2-cat / (∞,1)-cat.

## Bloque 2 — Composicion

- [ ] **CRITICO** las composiciones del problema satisfacen **asociatividad**.
- [ ] **CRITICO** existe un morfismo identidad `id_A` para cada objeto y se comporta como tal en composiciones.
- [ ] **MEDIO** se identifica si la categoria es **monoidal** (paralelismo, currying) y con que producto.

## Bloque 3 — Funtores y traduccion

- [ ] **CRITICO** todo funtor declarado preserva **composicion** (`F(g ∘ f) = F(g) ∘ F(f)`).
- [ ] **CRITICO** todo funtor declarado preserva **identidad** (`F(id_A) = id_F(A)`).
- [ ] **MEDIO** se declara si el funtor es **faithful** (inyectivo en hom-sets) y si **full** (sobreyectivo en hom-sets).
- [ ] **MEDIO** se declara explicitamente lo que el funtor pierde.

## Bloque 4 — Naturalidad

- [ ] **CRITICO** toda transformacion natural declarada cumple el cuadrado de naturalidad para todos los morfismos del dominio.
- [ ] **MEDIO** se distingue componentes individuales (familia de morfismos) de transformacion natural completa.
- [ ] **BAJO** se declara si la transformacion natural es invertible (isomorfismo natural).

## Bloque 5 — Universalidad

- [ ] **CRITICO** todo limite/colimite declarado se justifica con su **propiedad universal** (existencia + unicidad salvo isomorfismo).
- [ ] **CRITICO** los pullbacks no se confunden con simples intersecciones; los pushouts no se confunden con simples uniones.
- [ ] **MEDIO** se identifican los morfismos universales que la propiedad induce.

## Bloque 6 — Adjunciones

- [ ] **CRITICO** toda adjuncion declarada exhibe el **iso natural** `Hom(F(X), Y) ≅ Hom(X, G(Y))`.
- [ ] **CRITICO** se identifican **unit** `η: Id → G ∘ F` y **counit** `ε: F ∘ G → Id`.
- [ ] **MEDIO** se verifican las **identidades triangulares**.
- [ ] **BAJO** se declara explicitamente que `F ⊣ G` no implica que `F` y `G` sean inversos.

## Bloque 7 — Yoneda y representabilidad

- [ ] **CRITICO** cualquier afirmacion "X queda determinado por sus relaciones" cita Yoneda y la categoria sobre la que aplica.
- [ ] **MEDIO** se distingue isomorfismo de hom-funtores de igualdad de objetos.

## Bloque 8 — Efectos

- [ ] **CRITICO** toda monada declarada exhibe `η`, `μ` y satisface las **tres leyes** (unidad izquierda, unidad derecha, asociatividad).
- [ ] **CRITICO** la composicion Kleisli `>=>` se distingue de la composicion ordinaria.
- [ ] **CRITICO** toda coalgebra declarada exhibe la funcion `α: A → F(A)` y el funtor `F`.
- [ ] **MEDIO** las bisimulaciones declaradas se justifican exhibiendo la relacion `R` y mostrando que se preserva bajo `α` y `β`.

## Bloque 9 — Logica interna

- [ ] **CRITICO** todo topos declarado exhibe limites finitos, exponenciales y clasificador de subobjetos `Ω`.
- [ ] **MEDIO** se distingue logica clasica (boolean) de intuicionista (clasificador no-2).
- [ ] **BAJO** los sheaves declarados verifican explicitamente la condicion de pegado.

## Bloque 10 — Trazabilidad y citas

- [ ] **CRITICO** cada conclusion sustantiva cita la **URN especifica** del ICAS-BoK que la apoya.
- [ ] **CRITICO** se distingue formal (teorema/lema del corpus) de heuristica (analogia util pero no prueba).
- [ ] **MEDIO** se cita la seccion o pasaje del corpus, no solo la URN, cuando hay precision adicional.

## Bloque 11 — Anti-sobreingenieria

- [ ] **CRITICO** se eligio la lectura categorial **mas debil** que cumple el trabajo.
- [ ] **MEDIO** se justifica por que se necesita ir mas alla de Set / monada simple / categoria 1.
- [ ] **BAJO** si la lectura es heuristica, se ofrece una alternativa operacional.

## Bloque 12 — Cierre

- [ ] **CRITICO** el agente invocador recibe diagnostico + patron + checklist + (cuando aplica) alternativas.
- [ ] **CRITICO** si el corpus no cubre el caso, se declara explicitamente y se propone como tratarlo afuera.
- [ ] **MEDIO** se identifica si el problema necesita tambien `modelamiento-opm` u otra skill complementaria.

## Severidad y entrega

| Resultado | Accion |
|-----------|--------|
| 0 fallos CRITICO | listo para `entregar` |
| 1+ fallo CRITICO | volver a `aplicar-patron` (refinar mapeo) o `reformular-categorialmente` (max 2 iter) |
| solo fallos MEDIO/BAJO | entregar con anotacion explicita de lo que queda fuera |

**No silenciar fallos**. La transparencia exige declarar todo lo que la aplicacion deja sin demostrar.
