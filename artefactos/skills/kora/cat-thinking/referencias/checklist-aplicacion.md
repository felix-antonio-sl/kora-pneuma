# Checklist de aplicacion — verificar que la lectura categorial es correcta

Usar despues de aplicar un patron del corpus, antes de entregar al agente invocador. Marca con tres niveles: **CRITICO** (debe pasar), **MEDIO** (debe pasar o declararse explicitamente), **BAJO** (recomendable).

## Bloque 0 — Estatuto epistemico

- [ ] **CRITICO** cada afirmacion categorial se etiqueta como **formal**, **modelo**, **heuristica** o **metafora**.
- [ ] **CRITICO** toda afirmacion formal incluye una demostracion suficiente o una fuente primaria que pruebe exactamente la afirmacion.
- [ ] **CRITICO** la lectura elegida es la mas debil que resuelve el problema; una heuristica no fabrica categorias ni leyes que no necesita.

## Bloque 1 — Identificacion

- [ ] **CRITICO** para toda lectura **formal**, la categoria base esta identificada explicitamente (Set, Cat, Vect, Cost, Bool, topos T, etc.).
- [ ] **CRITICO** sus **objetos** estan tipificados (servicios, tablas, tipos, valores efectados, configuraciones, ...).
- [ ] **CRITICO** sus **morfismos** estan tipificados (calls, FKs, funciones, queries, transitions, ...).
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

- [ ] **CRITICO** todo limite/colimite declarado se justifica con su **propiedad universal**: existe un unico morfismo mediador compatible. El objeto universal queda determinado salvo isomorfismo.
- [ ] **CRITICO** los pullbacks no se confunden con simples intersecciones; los pushouts no se confunden con simples uniones.
- [ ] **MEDIO** se identifican los morfismos universales que la propiedad induce.

## Bloque 6 — Adjunciones

- [ ] **CRITICO** toda adjuncion declarada exhibe el **iso natural** `Hom(F(X), Y) ≅ Hom(X, G(Y))`, o equivalentemente unidad y counit con identidades triangulares.
- [ ] **CRITICO** si se usa la segunda presentacion, se identifican **unit** `η: Id → G ∘ F`, **counit** `ε: F ∘ G → Id` y sus identidades triangulares.
- [ ] **BAJO** se declara explicitamente que `F ⊣ G` no implica que `F` y `G` sean inversos.

## Bloque 7 — Yoneda y representabilidad

- [ ] **CRITICO** cualquier afirmacion "X queda determinado por sus relaciones" cita Yoneda y la categoria sobre la que aplica.
- [ ] **MEDIO** se distingue isomorfismo de hom-funtores de igualdad de objetos.

## Bloque 8 — Efectos

- [ ] **CRITICO** toda monada declarada exhibe `η`, `μ` y satisface las **tres leyes** (unidad izquierda, unidad derecha, asociatividad).
- [ ] **CRITICO** la composicion Kleisli `>=>` se distingue de la composicion ordinaria.
- [ ] **CRITICO** toda coalgebra declarada exhibe la funcion `α: A → F(A)` y el funtor `F`.
- [ ] **MEDIO** las bisimulaciones declaradas exhiben la relacion `R`, el lifting relacional o hipotesis del funtor y la prueba de preservacion bajo `α` y `β`; con efectos, se declara ademas la semantica elegida.

## Bloque 8b — Ingeniería agéntica

- [ ] **CRITICO** se separan artefacto fuente, modelo matematico y conducta
  runtime; igualdad de archivos no se usa como equivalencia conductual.
- [ ] **CRITICO** todo agente llamado coalgebra exhibe `I`, `O`, `U`, la
  monada `M` y `step : U × I -> M(O × U)`.
- [ ] **CRITICO** toda composicion de agentes exhibe interfaces/puertos
  tipados, wiring, semantica del wiring y compatibilidad de efectos.
- [ ] **CRITICO** `componible` se trata como arista candidata, no como prueba
  de composicion; `estados` no se trata como FSM sin aristas/eventos.
- [ ] **CRITICO** toda afirmacion de least-privilege compara capacidades
  efectivas del runtime con la declaracion, incluidos overrides dentro del
  alcance.
- [ ] **CRITICO** toda afirmacion de safety exhibe un invariante cerrado bajo
  la transicion modelada; allowlist y safety no se confunden.
- [ ] **MEDIO** feedback, recursion o delegacion declaran su semantica de
  delay/terminacion, protocolo, errores y autoridad.

## Bloque 9 — Logica interna

- [ ] **CRITICO** todo topos elemental declarado exhibe limites finitos, exponenciales (clausura cartesiana) y clasificador de subobjetos `Ω`.
- [ ] **MEDIO** se distingue logica clasica (boolean) de intuicionista (clasificador no-2).
- [ ] **BAJO** los sheaves declarados verifican explicitamente la condicion de pegado.

## Bloque 10 — Trazabilidad y citas

- [ ] **CRITICO** cada conclusion sustantiva cita la **URN interna** que permite rastrear el artefacto del corpus.
- [ ] **CRITICO** toda conclusion formal cita ademas una fuente primaria o aporta la prueba; una URN no confiere autoridad matematica.
- [ ] **CRITICO** se distingue entre formal, modelo, heuristica y metafora.
- [ ] **MEDIO** se cita la seccion o pasaje preciso. Si el corpus contradice la matematica, se corrige o se declara la discrepancia: la fuente/proof manda.

## Bloque 11 — Anti-sobreingenieria

- [ ] **CRITICO** se eligio la lectura categorial **mas debil** que cumple el trabajo.
- [ ] **MEDIO** se justifica por que se necesita ir mas alla de Set / monada simple / categoria 1.
- [ ] **BAJO** si la lectura es heuristica, se ofrece una alternativa operacional.
- [ ] **BAJO** una lectura heuristica puede cerrar sin categoria construida, siempre que no use vocabulario formal como si estuviera demostrado.

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
