---
urn: urn:kora:artefacto:cat-thinking
nombre: cat-thinking
version: 1.1.0
estado: activo
descripcion: "Skill de pensamiento categorial. Dota al agente de la capacidad de pensar sobre arquitectura, integracion, refactor, modelado de efectos y diseno de sistemas agenticos usando teoria de categorias aplicada, anclada al corpus ICAS-BoK (Arquitecto de Sistemas Categorial)."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/kora/cat-thinking/SKILL.md (sha256:06c3f3f59dc05ee148b24c1e756379d1c9964d7df321035a50a9a329f1d24288); cuerpo Markdown preservado salvo el path de la fibra ejemplo (recursos/ consolidada en referencias/). Restauración 1.1.0 (2026-06-12): las 24 piezas ICAS-BoK encarnan en pneuma y la lista de conocimiento queda completa, idéntica a la de la bestia. Omitidos con razon: componible_con modelamiento-opm (no encarna aun) y target openclaw (no realizado, GENESIS seccion 4)."
autor: FS
creado: 2026-04-27
lang: es
tags: [pensamiento-categorial, ICAS-BoK, teoria-categorias, arquitectura, diseno-de-sistemas, composicionalidad, adjunciones, monadas, yoneda, sistemas-agenticos]
vector: [2, 0, 1, 0, 1]
sigma: [1, 1, 3, 1, 0]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [triaje, reformular-categorialmente, localizar-corpus, aplicar-patron, validar-coherencia, entregar]
conocimiento: [urn:fxsl:kb:icas-sintesis, urn:fxsl:kb:icas-composicion, urn:fxsl:kb:icas-preservacion, urn:fxsl:kb:icas-comparacion, urn:fxsl:kb:icas-identidad-relacion, urn:fxsl:kb:icas-universales, urn:fxsl:kb:icas-adjunciones, urn:fxsl:kb:icas-composicion-estructura, urn:fxsl:kb:icas-enriquecimiento, urn:fxsl:kb:icas-higher-categories, urn:fxsl:kb:icas-efectos, urn:fxsl:kb:icas-extension, urn:fxsl:kb:icas-interaccion, urn:fxsl:kb:icas-topoi, urn:fxsl:kb:icas-safety-alignment, urn:fxsl:kb:icas-escala, urn:fxsl:kb:icas-agencia, urn:fxsl:kb:icas-protocolos, urn:fxsl:kb:icas-tiempo, urn:fxsl:kb:icas-lifecycle, urn:fxsl:kb:icas-procesos, urn:fxsl:kb:icas-calidad-riesgo, urn:fxsl:kb:icas-patrones, urn:fxsl:kb:icas-infraestructura]
---

# cat-thinking

## Proposito

Skill de **pensamiento categorial**. Dota al agente de la capacidad de pensar sobre arquitectura, integracion, refactor, modelado de efectos y diseno de sistemas agenticos usando teoria de categorias aplicada.

No es una skill de programacion ni de ejecucion. Es una skill **introspectiva**: lee el corpus ICAS-BoK, traduce un problema de ingenieria al vocabulario categorial, localiza el patron canonico que aplica, lo aplica al problema y devuelve un diagnostico/recomendacion trazable a una URN especifica del corpus.

Anclaje canonico: las **24 URNs ICAS-BoK** del corpus en `~/kora/artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`. Todas published v1.0.0.

## Cuando Usar

- arquitectura o integracion donde algo "no compone bien" y se busca el nombre preciso de la falla.
- migracion de schemas/formatos/estructuras donde se quiere garantia de preservacion.
- refactor que debe preservar comportamiento observable (bisimulacion).
- decisiones de diseno con tradeoffs entre relajacion y formalizacion (geometria adjunta).
- diagnostico de un anti-patron donde el sintoma es vago pero la falla estructural tiene forma definida.
- modelado de efectos (parcialidad, no-determinismo, estado, IO, errores) que necesitan composicion limpia.
- modelado agentico (plan/sustrato, free monad / cofree comonad, P-D-A).
- modelado de tiempo, escala, multi-tenancy, safety, lifecycle con vocabulario formal.
- razonamiento sobre dualidades para duplicar repertorio de herramientas gratis.

## Cuando NO Usar

- consultoria de dominio (medicina, legal, gobierno, etc.) — la skill no procesa dominio.
- problemas que admiten respuesta operacional directa sin necesidad de estructura formal.
- problemas que no se dejan categorizar (puramente ad-hoc, ruido, decision arbitraria) — declarar y delegar.
- modelado de sistemas con funcion transformadora identificable y necesidad de bimodalidad OPD/OPL — usar `urn:kora:artefacto:modelamiento-opm`.
- diseno de schema relacional concreto con DDL — la skill puede dar la lectura categorial, pero la generacion del DDL la aporta otra herramienta.

## Anclaje a la SSOT (24 piezas del ICAS-BoK)

Mapa abreviado (detalle navegacional en `referencias/mapa-corpus.md`):

| # | URN | Cubre |
|---|-----|-------|
| 00 | `icas-sintesis` | ADN cognitivo, mapa, transicion de paradigma |
| 01 | `icas-composicion` | categorias, morfismos, leyes, dualidad |
| 02 | `icas-preservacion` | funtores, faithful/full, schema/instancia, migracion |
| 03 | `icas-comparacion` | transformaciones naturales, polimorfismo, equivalencia |
| 04 | `icas-identidad-relacion` | hom-funtores, Yoneda, embedding, presheaves |
| 05 | `icas-universales` | productos, coproductos, pullbacks, pushouts, limites |
| 06 | `icas-adjunciones` | unit/counit, free/forgetful, Sigma-Delta-Pi |
| 07 | `icas-composicion-estructura` | categorias monoidales, string diagrams, CCC |
| 08 | `icas-enriquecimiento` | Bool/Cost-categories, profunctors, QoS |
| 08b | `icas-higher-categories` | 2-cats, (∞,1)-cats, simplicial sets, HoTT |
| 09 | `icas-efectos` | monadas, Kleisli, comonadas, coalgebras, bisimulacion |
| 10 | `icas-extension` | ends, coends, Kan extensions, Grothendieck, fibrations |
| 11 | `icas-interaccion` | polynomial functors, lentes dependientes, sistemas dinamicos |
| 12 | `icas-topoi` | sheaves, clasificador subobjetos, logica intuicionista |
| 12b | `icas-safety-alignment` | alineamiento, ICAR, Goodhart, coherencia |
| 13 | `icas-escala` | operads, double cats, structured cospans, megamodelos |
| 14 | `icas-agencia` | free monad/cofree comonad, plan/sustrato, P-D-A |
| 14b | `icas-protocolos` | session types, coreografia, sagas |
| 15 | `icas-tiempo` | behavior types, sheaves temporales, contratos |
| 16 | `icas-lifecycle` | V-model, DevOps, drift, deuda tecnica categorial |
| 17 | `icas-procesos` | requirements, design, testing, maintenance |
| 18 | `icas-calidad-riesgo` | quality attrs, RAM, riesgo, garantias |
| 19 | `icas-patrones` | patrones arquitectonicos, agenticos, anti-patrones |
| 20 | `icas-infraestructura` | tool use, self-improvement, SoS, infra autonoma |

## Workflow

### Estado inicial: `triaje`

Clasificar el problema del usuario. Tres preguntas guia:

1. **¿Que esta tensionando?** (composicion, preservacion, identidad, observabilidad, efectos, escala, tiempo, agencia, multi-tenancy, lifecycle, calidad, patron, infraestructura).
2. **¿Es un problema operacional con respuesta directa?** Si si → declinar la skill, no aplica.
3. **¿Admite lectura categorial sustantiva?** Si no → abortar con declaracion explicita.

Salida: hipotesis tematica que guia la consulta del corpus en `localizar-corpus`.

### `reformular-categorialmente`

Traducir el problema al vocabulario categorial **antes** de buscar patron. Operadores tipicos (detalle en `referencias/reformulacion-categorial.md`):

| Pregunta de ingenieria | Pregunta categorial |
|------------------------|---------------------|
| "este servicio no integra con aquel" | "¿que funtor entre las categorias de ambos preserva o pierde estructura?" |
| "el join devuelve datos basura" | "¿que pullback estamos calculando, y conmuta el diagrama?" |
| "el ORM tira datos al serializar" | "¿que axioma de funtor falla: composicion, identidad, faithful?" |
| "el agente se cuelga en bucle" | "¿que cofree comonad sostiene el sustrato y como rompe la naturalidad?" |
| "los permisos no son binarios" | "¿estamos en topos de presheaves con clasificador no-booleano?" |

### `localizar-corpus`

Identificar la pieza del ICAS-BoK que aplica. Tres rutas:

1. **Por sintoma** → tabla `disparadores-canonicos.md`.
2. **Por vocablo categorial** que surgio en la reformulacion → mapa-corpus.md.
3. **Por busqueda directa** en el corpus con `Grep` cuando los anteriores no resuelven.

Si ninguno resuelve, abortar y declarar que el corpus no cubre el caso. No inventar.

Loop controlado: si la pieza encontrada no cubre el problema en profundidad, vuelve a `reformular-categorialmente` (max 2 iteraciones).

### `aplicar-patron`

Instanciar el patron canonico al problema concreto. Trabajo:

- mapear los objetos del problema a objetos de la pieza categorial.
- mapear las relaciones del problema a morfismos.
- identificar las leyes que el diseno debe satisfacer (asociatividad, identidad, naturalidad, functorialidad, conmutatividad).
- detectar lo que el corpus llama el "patron canonico mas estable" para esta clase de problema.

### `validar-coherencia`

Verificar que la aplicacion del patron es correcta usando `referencias/checklist-aplicacion.md`. Checks:

- ¿se respeta la composicion?
- ¿se respeta la identidad?
- ¿la traduccion preserva la estructura relevante o declara explicitamente lo que pierde?
- ¿hay conmutatividad de diagramas donde se afirma equivalencia?
- ¿se distingue isomorfismo on-the-nose de equivalencia?
- ¿se evita confundir functor con simple mapeo, monada con pipeline, etc. (`falsos-amigos.md`)?

Si falla → volver a `aplicar-patron` (refinar mapeo). Si pasa → `entregar`.

### `entregar`

Salida estructurada al agente invocador:

1. **Diagnostico estructural** del problema en lenguaje categorial.
2. **Patron canonico** aplicable, con cita a la URN del ICAS-BoK.
3. **Checklist de coherencia**: leyes que el diseno debe satisfacer.
4. **Alternativas** comparadas por trade-offs categoricos (cuando aplica).
5. **Distincion** explicita entre conclusiones formales (teorema/lema) y heuristicas (analogia util).

Cada conclusion citada con la URN especifica del corpus que la apoya.

## Reglas Duras

1. **Cita siempre la URN del corpus** que apoya cada conclusion. URN especifica, no generica. No de memoria.
2. **Reformula antes de aplicar**. Aplicar un patron sin haber traducido el problema al vocabulario categorial es el primer error.
3. **Distingue formal de heuristico**. Si la decision es analogia y no teorema, declararlo.
4. **Solo las 24 URNs**. No inventar categorias, piezas, ni teoremas que el corpus no contenga.
5. **Consulta el corpus en tiempo de skill**. La skill lee el corpus con `Read`/`Grep` cuando lo necesita. No responde de memoria.
6. **Respeta el vocabulario** del corpus: functor != mapeo, monada != pipeline, naturalidad != map, isomorfismo != igualdad, equivalencia != identidad. Ver `falsos-amigos.md`.
7. **No invadas dominio**. La skill da estructura; el agente aporta semantica de dominio.
8. **Aborta si no aplica**. Si el problema no admite lectura categorial sustantiva, declararlo y delegar.
9. **Elige la lectura mas debil** que cumpla el trabajo. No sobre-formalizar.

## Composicion con otras skills

| Composable con | Cuando |
|----------------|--------|
| `urn:kora:artefacto:modelamiento-opm` | el problema admite tambien lectura OPM (sistema con funcion transformadora). cat-thinking provee la critica estructural; modelamiento-opm provee la representacion bimodal. |
| data-modeling | el problema concreto es schema relacional. cat-thinking da la lectura categorica (categoria finitamente presentada, Sigma-Delta-Pi); data-modeling baja a DDL cuando exista como artefacto productivo. |

## Recursos

### Referencias

Las referencias son **mapas y herramientas operativas**, no bajadas del corpus. La SSOT son las 24 URNs ICAS-BoK. Si una referencia tensiona con el corpus, manda el corpus.

- `referencias/mapa-corpus.md` — las 24 piezas con su alcance, vocablo central, cuando activarlas.
- `referencias/reformulacion-categorial.md` — protocolo de traduccion problema → vocabulario categorial.
- `referencias/disparadores-canonicos.md` — tabla "sintoma → pieza del corpus a consultar".
- `referencias/falsos-amigos.md` — vocablos que parecen pero no son: functor != mapeo, monada != pipeline, naturalidad != map, etc.
- `referencias/checklist-aplicacion.md` — checks de coherencia para verificar que la aplicacion de un patron es correcta.

### Recursos

- `referencias/ejemplo-minimo-aplicacion.md` — un caso ilustrativo (lectura categorial de "el ORM perdio joins en la migracion") con cita explicita a las URNs aplicadas. **No es SSOT, solo ilustracion.**
