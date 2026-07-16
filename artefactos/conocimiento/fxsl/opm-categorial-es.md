---
urn: urn:fxsl:kb:opm-categorial-es
nombre: opm-categorial-es
version: 1.2.6
estado: publicado
descripcion: "Puente formal OPM ↔ teoría de categorías: lectura categorial del corpus OPM-ES anclada a las piezas del ICAS-BoK."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-categorial-es.md (sha256:431aa94ce86223e58ceba3faa3731fe9eefd4bba6ea549f22a1621475a9eb60b) el 2026-06-12; cuerpo byte-fiel. Correccion 1.2.5 (2026-06-15): la fuente original /home/felix/projects/deep-opm-pro/docs/capa-categorial.md fue retirada de deep-opm-pro; bajo el regimen pneuma-toma-la-posta de la SSOT OPM (urn:kora:kb:regimen-de-ley), la sintesis viva de la capa categorial es ahora este kb mas la implementacion falsable en deep-opm-pro (app/src/modelo, app/src/leyes). Se corrige la referencia muerta del cuerpo. Correccion 1.2.6 (2026-07-16): retira la derivacion a custodio-kora de la bestia y devuelve las propuestas a la capa propietaria de ley/0..4 con decision del operador."
autor: FS
creado: 2026-06-03
lang: es
tags: [opm, categorial, icas-bok, puente, opforja, eje-horizontal, eje-vertical]
familia: bok
depende: [urn:fxsl:kb:opm-es, urn:fxsl:kb:opd-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:spec-forja-opd-es, urn:fxsl:kb:spec-forja-opl-es, urn:fxsl:kb:metodologia-forja-opm-es, urn:fxsl:kb:reglas-opm-estrictas-es]
cita: [urn:fxsl:kb:icas-sintesis, urn:fxsl:kb:icas-composicion, urn:fxsl:kb:icas-preservacion, urn:fxsl:kb:icas-comparacion, urn:fxsl:kb:icas-efectos, urn:fxsl:kb:icas-universales, urn:fxsl:kb:icas-composicion-estructura, urn:fxsl:kb:icas-higher-categories, urn:fxsl:kb:icas-topoi, urn:fxsl:kb:icas-adjunciones, urn:fxsl:kb:icas-extension, urn:fxsl:kb:icas-enriquecimiento]
---

# OPM <-> teoría de categorías — puente formal (ICAS-BoK)

## 0. Qué es y qué no es este artefacto

Este documento es un **puente** entre dos corpus de la SSOT: la familia OPM (`urn:fxsl:kb:opm-es` y derivadas) y el corpus categorial ICAS-BoK (`urn:fxsl:kb:icas-sintesis` y familia). Lee OPM con **teoría de categorías como piedra de Rosetta** y mapea cada primitiva/mecanismo OPM a la construcción categorial canónica que lo modela.

**Línea roja (rectora).** La lente categorial es **nota al margen formal, nunca principio para el modelador** (`metodologia-forja-es.md §0.2-0.3`). Este artefacto es justamente *esa* nota al margen, aislada en su propio lugar para que el canon-para-humanos (`opm-es`/`opd-es`/`opl-es`) y la familia Forja (`reglas-opm-estrictas-es`, `metodologia-forja-es`, `spec-forja-opd-es`, `spec-forja-opl-es`) permanezcan **limpios de jerga categorial**. Nada aquí redefine OPM ni añade primitiva: OPM ya es categorialmente bien fundado; este puente solo **nombra con precisión** lo que OPM implica estructuralmente. La superficie del modelador (UI, OPD, OPL) **jamás** muestra este vocabulario.

## 1. Mapa OPM <-> teoría de categorías

| Primitiva / mecanismo OPM | Construcción categorial | URN ICAS-BoK |
|---|---|---|
| Objetos, procesos, enlaces | objetos y morfismos de una categoría | `urn:fxsl:kb:icas-composicion` |
| Hecho OPM (denotación atómica del modelo) | elemento del haz de hechos (presheaf) | `urn:fxsl:kb:icas-topoi` |
| Pegado de OPDs (consistencia entre vistas del mismo modelo) | sheaf / gluing sobre el cubrimiento de OPDs | `urn:fxsl:kb:icas-topoi` |
| Refinamiento (in-zoom) <-> abstracción (out-zoom) | adjunción in-zoom ⊣ out-zoom (unit/counit) + fibración de Grothendieck (lift cartesiano de frontera) | `urn:fxsl:kb:icas-adjunciones`, `urn:fxsl:kb:icas-extension` |
| Composición de modelos por interfaz compartida | pushout / structured cospan | `urn:fxsl:kb:icas-universales` |
| Equivalencia de realizaciones (mismo efecto, interior distinto) | 2-célula / equivalencia por firma de frontera | `urn:fxsl:kb:icas-higher-categories`, `urn:fxsl:kb:icas-comparacion` |
| Simulación (desplegar el comportamiento) | anamorfismo (unfold de una coalgebra) | `urn:fxsl:kb:icas-efectos` |
| Razonamiento (derivar lo implícito) | catamorfismo (fold) — dual de la simulación | `urn:fxsl:kb:icas-efectos` |
| Costo / duración / recursos cuantitativos de la traza | categoría enriquecida en Cost `([0,∞],+,0)`: hom-object = costo, `X(x,x)=0`, desigualdad triangular, shortest-path (min,+); `costoDeCamino = foldMap` del monoide libre de pasos | `urn:fxsl:kb:icas-enriquecimiento` |
| Recurso lineal (se consume, no se clona) | categoría monoidal no-cartesiana | `urn:fxsl:kb:icas-composicion-estructura` |
| Preservación de estructura al migrar/proyectar | funtor (faithful / full) | `urn:fxsl:kb:icas-preservacion` |

## 2. El eje horizontal: dónde la lectura categorial aporta

OPM tiene el **eje vertical** (refinamiento <-> abstracción) muy desarrollado en sus capas. La frontera estaba en el **eje horizontal**: **composición**, **equivalencia** y **razonamiento** entre modelos y realizaciones, más la **linealidad** como dimensión designable. La lectura categorial da a ese eje horizontal una semántica precisa y verificable, sin tocar la superficie OPM:

- **Composición** = pushout por interfaz compartida (`icas-universales`): dos modelos se unen identificando entidades comunes, sin duplicar ni dejar referencias colgantes.
- **Equivalencia** = igualdad de firma de frontera (`icas-higher-categories`): dos realizaciones son funcionalmente intercambiables si presentan el mismo efecto observable sobre su contorno, aunque su interior difiera.
- **Linealidad** = monoidalidad no-cartesiana (`icas-composicion-estructura`): un recurso que se consume no se duplica; dos consumidores del mismo recurso lineal son un conflicto.

El **eje vertical**, siempre maduro como *mecanismo*, carecía de un invariante que lo protegiera; ahora también tiene lectura categorial verificada:

- **Adjunción in-zoom ⊣ out-zoom** (`icas-adjunciones`): refinar y luego abstraer preserva exactamente la **frontera** del proceso (la *unit* η es iso sobre la frontera, "módulo detalle añadido"); in-zoom es idempotente. Es la garantía de coherencia del eje más usado de OPM.
- **Fibración de Grothendieck** (`icas-extension`): el árbol de OPDs fibra sobre la jerarquía de refinamiento; cada enlace derivado del hijo es el **lift cartesiano** de un enlace de frontera del padre (existencia + unicidad + cambio de base coherente). "Traer" un enlace entre niveles = cambio de base funtorial.
- **Puente con la bisimulación:** la frontera que la bisimulación de un in-zoom ejerce es la que la adjunción preserva — lo que convierte la coherencia de frontera de hipótesis en teorema verificable.
- **Operador clausura (identidades triangulares):** el round-trip `T = out-zoom ∘ in-zoom` es idempotente sobre la frontera (`T² = T`) y el refinamiento libre es reproducible. El observable vale tanto para `descomposicion` (in-zoom de proceso) como para `despliegue` (unfold de objeto); en unfold la frontera externa se preserva sin redistribuirse (su fibración es parte-todo, no de frontera).

## 3. La dualidad central: simulación y razonamiento

La pieza unificadora (`urn:fxsl:kb:icas-efectos`): **simulación (anamorfismo / unfold) y razonamiento (catamorfismo / fold) son duales sobre el mismo sustrato** — el haz de hechos del modelo. La simulación despliega el comportamiento paso a paso; el razonamiento colapsa la estructura a inferencias. Recorren **el mismo grafo de transición de estados**, en sentidos opuestos: lo que la simulación abre, el razonamiento puede cerrar. La consulta de alcanzabilidad de estados es el dual estático del recorrido dinámico.

El grafo de transición que la simulación recorre se **enriquece en Cost** (`urn:fxsl:kb:icas-enriquecimiento`): cada traza es el monoide libre de pasos, y `costoDeCamino = foldMap(duración)` es su homomorfismo canónico al monoide de costos `([0,∞], +, 0)`. La categoría enriquecida resultante da, vía cerradura (min,+), el costo mínimo entre estados con `X(x,x)=0` y desigualdad triangular — base para QoS, caminos críticos y co-design por profunctors. Es estructura cuantitativa, no agregación estadística.

## 4. Dónde se encarna (capas opforja + implementación)

Este puente es conocimiento; las **reglas normativas** correspondientes viven en las capas prescriptivas de opforja, y la **verdad ejecutable** en las leyes del modelador:

- `urn:fxsl:kb:reglas-opm-estrictas-es §Anexo C` — reglas `R-CAT-LIN` (linealidad), `R-CAT-EQ` (equivalencia por frontera), `R-CAT-COMP` (composición).
- `urn:fxsl:kb:metodologia-forja-opm-es §A0.4` — equivalencia funcional de realizaciones como cierre del método A0; comparación de realizaciones hermanas por firma de frontera y criterio vertical in-zoom <-> out-zoom como caso complementario.
- `urn:fxsl:kb:spec-forja-opd-es` — realización visual/OPD de las reglas cuando una ley categorial se proyecta a canvas, validación visual o export.
- `urn:fxsl:kb:spec-forja-opl-es §24` — composición por interfaz en OPL (unión deduplicada de párrafos).
- Implementación verificada en `deep-opm-pro`: `app/src/modelo/{hechos,composicion,equivalencia,razonamiento,simulacion}/` y leyes falsificables en `app/src/leyes/` (`law-composicion-*`, `law-derivacion-no-contradice`, integración S⊑F0 / dualidad S->F3 / F1<->S / F2<->S, condiciones/loops por invocación). El **eje vertical** se verifica en `app/src/modelo/equivalencia/verticalidad.ts` (`firmaFronteraEntidad`, `verificarLiftCartesianoFrontera`) y `app/src/leyes/refinamiento-adjuncion.test.ts` (F-V1 adjunción incl. despliegue e identidades triangulares, F-V2 fibración, puente F-V1<->F-D2). El **enriquecimiento en Cost** (F-D3) en `app/src/modelo/simulacion/costoCategoria.ts` (`costoDeCamino`, `categoriaDeCosto`) y `app/src/leyes/enriquecimiento-cost.test.ts`. Cada ley con control de no-tautología. Síntesis viva: este kb (`urn:fxsl:kb:opm-categorial-es`) + la implementacion falsable en `deep-opm-pro` (`app/src/modelo`, `app/src/leyes`).

## 5. Regla de uso

- Para **modelar** (humano): usar OPM/OPD/OPL en lenguaje de dominio; este artefacto NO se cita al modelador.
- Para **diseñar o auditar** la capa formal de opforja (agente/arquitecto): este puente da el vocabulario y la trazabilidad a ICAS-BoK; cada afirmación categorial DEBE poder anclarse a una URN ICAS específica y, donde se vuelve regla, a su capa propietaria opforja y a una ley ejecutable.
- Cambios a este puente o a las capas que referencia = **propuestas** en la capa propietaria bajo `ley/0..4`, con decisión del operador; nunca contaminar las capas ISO (`opm-es`/`opd-es`/`opl-es`).
