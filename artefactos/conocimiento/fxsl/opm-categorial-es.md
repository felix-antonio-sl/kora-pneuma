---
urn: urn:fxsl:kb:opm-categorial-es
nombre: opm-categorial-es
version: 1.3.0
estado: publicado
descripcion: "Puente formal OPM ↔ teoría de categorías: lectura categorial del corpus OPM-ES anclada a las piezas del ICAS-BoK."
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/fxsl/opm/opm-ssot-es/opm-categorial-es.md (sha256:431aa94ce86223e58ceba3faa3731fe9eefd4bba6ea549f22a1621475a9eb60b) el 2026-06-12; cuerpo byte-fiel. Correccion 1.2.5 (2026-06-15): la fuente original /home/felix/projects/deep-opm-pro/docs/capa-categorial.md fue retirada de deep-opm-pro; bajo el regimen pneuma-toma-la-posta de la SSOT OPM (urn:kora:kb:regimen-de-ley), la sintesis viva de la capa categorial es ahora este kb mas la implementacion falsable en deep-opm-pro (app/src/modelo, app/src/leyes). Correccion 1.2.6 (2026-07-16): retira la derivacion a custodio-kora. Correccion 1.3.0 (2026-07-18): separa correspondencias formales, modelos candidatos y analogias; la firma de frontera queda como equivalencia observacional relativa, no equivalencia categorial ni sustituibilidad universal."
autor: FS
creado: 2026-06-03
lang: es
tags: [opm, categorial, icas-bok, puente, opforja, eje-horizontal, eje-vertical]
familia: bok
depende: [urn:fxsl:kb:opm-es, urn:fxsl:kb:opd-es, urn:fxsl:kb:opl-es, urn:fxsl:kb:spec-forja-opd-es, urn:fxsl:kb:spec-forja-opl-es, urn:fxsl:kb:metodologia-forja-opm-es, urn:fxsl:kb:reglas-opm-estrictas-es]
cita: [urn:fxsl:kb:icas-sintesis, urn:fxsl:kb:icas-composicion, urn:fxsl:kb:icas-preservacion, urn:fxsl:kb:icas-comparacion, urn:fxsl:kb:icas-efectos, urn:fxsl:kb:icas-universales, urn:fxsl:kb:icas-composicion-estructura, urn:fxsl:kb:icas-higher-categories, urn:fxsl:kb:icas-topoi, urn:fxsl:kb:icas-adjunciones, urn:fxsl:kb:icas-extension, urn:fxsl:kb:icas-enriquecimiento]
---

# OPM <-> teoría de categorías — puente epistémicamente tipado (ICAS-BoK)

## 0. Qué es y qué no es este artefacto

Este documento es un **puente de modelado** entre dos corpus de la SSOT: la
familia OPM y el ICAS-BoK. Una correspondencia es formal solo cuando declara
categorías, funtores/objetos universales y leyes; las demás filas son modelos
candidatos o analogías controladas. Compartir forma o vocabulario no basta.

**Línea roja (rectora).** La lente categorial es **nota al margen, nunca
principio para el modelador**. Nada aquí redefine OPM ni añade primitivas.
OPM no se vuelve categorial por decreto: este puente propone formalizaciones
falsables para aspectos seleccionados. La superficie del modelador no necesita
mostrar este vocabulario.

## 1. Mapa OPM <-> teoría de categorías

| Primitiva / mecanismo OPM | Construcción categorial | URN ICAS-BoK |
|---|---|---|
| Objetos, procesos, enlaces | candidato: categoría presentada de hechos/caminos; no identificar «proceso» con morfismo sin semántica | `urn:fxsl:kb:icas-composicion` |
| Hecho OPM (denotación atómica del modelo) | candidato: sección de un presheaf explícito | `urn:fxsl:kb:icas-topoi` |
| Pegado de OPDs (consistencia entre vistas del mismo modelo) | candidato: sheaf si se define site, cobertura, restricciones y gluing único | `urn:fxsl:kb:icas-topoi` |
| Refinamiento (in-zoom) <-> abstracción (out-zoom) | modelo local: adjunción/fibración solo si se prueban hom-isomorfismo y lifts cartesianos | `urn:fxsl:kb:icas-adjunciones`, `urn:fxsl:kb:icas-extension` |
| Composición de modelos por interfaz compartida | pushout / structured cospan si satisface la propiedad universal | `urn:fxsl:kb:icas-universales` |
| Realizaciones con igual firma declarada | equivalencia observacional relativa a esa firma; no equivalencia categorial automática | `urn:fxsl:kb:icas-higher-categories`, `urn:fxsl:kb:icas-comparacion` |
| Simulación | anamorfismo solo para una coálgebra y funtor concretos | `urn:fxsl:kb:icas-efectos` |
| Razonamiento | catamorfismo solo para un álgebra inicial concreta; no dual automático de la simulación | `urn:fxsl:kb:icas-efectos` |
| Costo / duración / recursos cuantitativos de la traza | categoría enriquecida en Cost si unidad, composición y desigualdad enriquecida cierran | `urn:fxsl:kb:icas-enriquecimiento` |
| Recurso lineal (se consume, no se clona) | candidato: categoría monoidal no-cartesiana con semántica de uso | `urn:fxsl:kb:icas-composicion-estructura` |
| Preservación de estructura al migrar/proyectar | funtor si se define acción sobre morfismos y se prueban leyes; faithful/full son propiedades adicionales | `urn:fxsl:kb:icas-preservacion` |

## 2. El eje horizontal: dónde la lectura categorial aporta

OPM tiene el **eje vertical** (refinamiento <-> abstracción) muy desarrollado en sus capas. La frontera estaba en el **eje horizontal**: **composición**, **equivalencia** y **razonamiento** entre modelos y realizaciones, más la **linealidad** como dimensión designable. La lectura categorial da a ese eje horizontal una semántica precisa y verificable, sin tocar la superficie OPM:

- **Composición:** puede especificarse por pushout si la operación implementada
  satisface su universalidad.
- **Equivalencia observacional:** igual firma de frontera hace indistinguibles
  dos realizaciones **solo para los observables incluidos**. Sustituibilidad
  exige incluir efectos, protocolos y atributos relevantes.
- **Linealidad:** una semántica monoidal no-cartesiana puede impedir
  contracción; el conflicto de recursos debe representarse en ella.

El **eje vertical** dispone de una formalización ejecutable local. Sus nombres
categoriales valen respecto de las categorías y observables que esa
implementación declara; los tests no convierten el mecanismo OPM general en
teorema:

- **Adjunción candidata:** requiere categorías de refinamientos/abstracciones y
  el isomorfismo natural de hom-sets; preservar una firma en round-trip no basta.
- **Fibración candidata:** requiere lifts cartesianos con existencia y
  universalidad, no solo propagación de enlaces.
- **Bisimulación candidata:** requiere una relación conductual estable bajo las
  transiciones elegidas; igualdad de frontera estática no la prueba.
- **Operador idempotente:** `T²=T` es comprobable para el operador local; llamarlo
  clausura exige además extensividad (o interior, si es descendente) y monotonía.

## 3. La dualidad central: simulación y razonamiento

Simulación y razonamiento pueden realizar respectivamente unfolds y folds
cuando se construyen una coálgebra y un álgebra apropiadas. No son duales por
usar el mismo grafo, ni alcanzabilidad es el dual categorial automático de una
ejecución.

El grafo de transición que la simulación recorre se **enriquece en Cost** (`urn:fxsl:kb:icas-enriquecimiento`): cada traza es el monoide libre de pasos, y `costoDeCamino = foldMap(duración)` es su homomorfismo canónico al monoide de costos `([0,∞], +, 0)`. La categoría enriquecida resultante da, vía cerradura (min,+), el costo mínimo entre estados con `X(x,x)=0` y desigualdad triangular — base para QoS, caminos críticos y co-design por profunctors. Es estructura cuantitativa, no agregación estadística.

## 4. Dónde se encarna (capas opforja + implementación)

Este puente es conocimiento; las **reglas normativas** correspondientes viven en las capas prescriptivas de opforja, y la **verdad ejecutable** en las leyes del modelador:

- `urn:fxsl:kb:reglas-opm-estrictas-es §Anexo C` — reglas `R-CAT-LIN` (linealidad), `R-CAT-EQ` (equivalencia por frontera), `R-CAT-COMP` (composición).
- `urn:fxsl:kb:metodologia-forja-opm-es §A0.4` — equivalencia funcional de realizaciones como cierre del método A0; comparación de realizaciones hermanas por firma de frontera y criterio vertical in-zoom <-> out-zoom como caso complementario.
- `urn:fxsl:kb:spec-forja-opd-es` — realización visual/OPD de las reglas cuando una ley categorial se proyecta a canvas, validación visual o export.
- `urn:fxsl:kb:spec-forja-opl-es §24` — composición por interfaz en OPL (unión deduplicada de párrafos).
- Realización ejecutable en `deep-opm-pro`: los módulos y tests citados
  falsan invariantes del **modelo local**. Los nombres históricos
  `adjunción`, `fibración` y `bisimulación` no sustituyen las propiedades
  universales descritas arriba. La síntesis viva es este KB más esa
  implementación falsable.

## 5. Regla de uso

- Para **modelar** (humano): usar OPM/OPD/OPL en lenguaje de dominio; este artefacto NO se cita al modelador.
- Para **diseñar o auditar** la capa formal de opforja: cada afirmación debe
  declarar estatus, tipos, ley/prueba o fuente primaria. La URN aporta
  trazabilidad, no autoridad matemática.
- Cambios a este puente o a las capas que referencia = **propuestas** en la capa propietaria bajo `ley/0..4`, con decisión del operador; nunca contaminar las capas ISO (`opm-es`/`opd-es`/`opl-es`).
