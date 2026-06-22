---
urn: urn:dev:artefacto:design
nombre: design
version: 1.0.0
estado: activo
descripcion: "Disena de extremo a extremo como Claude Design: de brief/imagen/doc a interfaces, identidad, slides, prototipos y collateral, anclando todo a un design system trazable y entregando codigo frontend funcional con handoff a Claude Code. Usar al construir o iterar cualquier salida visual con gusto y trazabilidad."
fuente: "Autorada nueva en KORA pneuma el 2026-06-22. Cristaliza, en formato skill ley/2, la esencia operativa del producto Claude Design de Anthropic Labs (research preview; anuncio 2026-04-17, overhaul 2026-06-17; fuentes anthropic.com/news/claude-design-anthropic-labs, support.claude.com get-started + set-up-design-system, venturebeat/thenewstack/techcrunch/engadget/techrepublic 2026). Sucede CONCEPTUALMENTE a graphic-design (urn:kora:artefacto:graphic-design en la bestia ~/kora, sha256:fe261c35387ab98652f19d2e32b599921a930ac3583425eee973dea72c01cbd5): absorbe sus operadores visuales, los design tokens ejecutables (JSON+CSS+Tailwind), el SVG y el axioma info/simpleza, y los amplia a diseno generativo de UI/identidad/prototipos. NO se declara reemplaza ni refina: graphic-design no encarna en el censo pneuma (referencias-resuelven fallaria), de modo que la sucesion se formalizara recien al migrar el target. Vector [2,0,2,0,1] = disciplina (cuerpo de conocimiento procedural, sin materia propia): Pi2 plan ramificado (brief->system->generar->refinar->verificar->entregar), Mu0 el ejecutor provee todo el soporte (el canvas es materia del runtime anfitrion, no de la skill), Xi2 interaccion bidireccional (round-trip diseno<->codigo con Claude Code), Lambda0 individual, Phi1 instrumental."
autor: FS
creado: 2026-06-22
lang: es
tags: [design, claude-design, design-system, design-tokens, frontend, prototipo, identidad-visual, slides, handoff, trazabilidad, taste, wcag]
vector: [2, 0, 2, 0, 1]
sigma: [1, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Glob, Grep, Bash]
targets: [claude-code, codex, opencode]
alcance: ambos
estados: [enmarcar, anclar-design-system, reunir-contexto, generar, refinar, verificar, entregar]
conocimiento: [urn:dev:kb:steve-jobs-canon-diseno]
componible: [urn:kora:artefacto:cat-thinking]
---
# design

## Proposito

Dota a cualquier agente de la capacidad de **disenar como Claude Design**:
colaborar para producir trabajo visual pulido y funcional — interfaces de UI,
prototipos interactivos, slides/pitch decks, one-pagers, landing pages,
identidad visual y collateral de marketing — donde el output **no es un
wireframe ni un snippet suelto** sino artefactos materializados (codigo
frontend, tokens, SVG, deck) **anclados a un design system trazable** y listos
para handoff a ingenieria.

Tesis operativa (heredada del producto): un lienzo de diseno, no un chat que
escupe markup. El valor no esta en la primera generacion — es solo un punto de
partida — sino en **iterar sobre un canvas** anclado a la marca, verificando
cada salida contra el design system y autocorrigiendo **antes** de mostrarla.

Tres planos inseparables:

| Plano | Funcion | Pregunta madre |
|---|---|---|
| **Sistema** | de donde viene el gusto | cual es el design system que ancla esto y de donde se extrae? |
| **Generacion** | materializar valor | que artefacto funcional resuelve el brief? |
| **Trazabilidad** | sostener coherencia | cada decision visual mapea a un token/componente del sistema? |

Axioma estetico vinculante (heredado de graphic-design):

> **Belleza = max(informacion / simpleza)**

Cada elemento se justifica solo si la informacion que aporta excede la
complejidad que introduce. El sistema optimo es la presentacion mas compacta:
minimos generadores, maxima estructura preservada. El gusto se ancla en
`urn:dev:kb:steve-jobs-canon-diseno` (sustraccion, primeros principios,
preguntas letales): consultarlo cuando la decision es de gusto, no de regla.

## Cuando usar

- construir UI/frontend funcional desde texto, imagen o documento (DOCX, PPTX, XLSX).
- crear o iterar identidad visual: paleta, tipografia, grilla, espaciado, marca.
- generar design tokens ejecutables (JSON + CSS custom properties + Tailwind).
- prototipos interactivos (incluida voz/video/3D/IA integrada conceptualmente).
- slides, pitch decks, one-pagers, landing pages, assets de redes/campana.
- extraer un design system de un codebase, repo React, archivos de diseno, PPT/PDF.
- preparar handoff de un diseno a Claude Code (bundle continuable, no screenshot).
- auditar coherencia de un sistema visual existente contra su design system.

## Cuando NO usar

- **evaluacion de experiencia de uso** — flujos de tarea, heuristicas Nielsen,
  accesibilidad sistemica, arquitectura de informacion: es trabajo de UX, no de
  forma visual; esta skill da forma, no evalua usabilidad.
- **modelado de interaccion** formal (IFML, multiscreen, view containers): es
  modelado, no diseno visual.
- razonamiento de **arquitectura/composicion** de sistemas (no visual) → usar
  `urn:kora:artefacto:cat-thinking`.
- escribir/integrar la **logica de aplicacion, backend, build, tests** del
  frontend generado: es trabajo de implementacion; esta skill entrega el bundle,
  no lo despliega ni lo cablea.
- decisiones de **negocio/contenido** (que decir): la skill da forma, no copy
  estrategico.

## Workflow — el loop de siete movimientos

No siempre secuencial. El router (abajo) elige el movimiento lider segun lo
detectado. El ciclo `generar -> refinar -> verificar` itera; `entregar` cierra.

### `enmarcar`

Capturar el brief antes de tocar pixeles:

- **que** se construye (UI / identidad / slides / prototipo / collateral).
- **soportes destino** (web, mobile, print, presentacion) y restricciones
  (contraste, tamano, color).
- **audiencia y tono**.
- **insumos disponibles**: brief textual, imagenes, documentos, codebase, repo,
  URL de referencia.

Si el brief es ambiguo en el **que** o el soporte, preguntar antes de generar —
generar sobre barro quema iteraciones. **Una pregunta a la vez.**

### `anclar-design-system`

**Todo proyecto hereda o construye un design system.** Resolver su origen, en
este orden de preferencia:

| Fuente | Como | Resultado |
|---|---|---|
| Codebase / repo React local | `Glob`+`Read` de tokens, theme, componentes; arrancar desde lo existente | reutiliza elementos del frontend real |
| Archivos de diseno / repo de marca | importar paleta, tipografia, componentes | construye con los componentes de la org |
| PPT/PDF/imagen bien hecha | extraer color, tipografia, ritmo visual | semilla de sistema desde un referente |
| Sin fuente | construir un sistema minimo desde el brief | tokens base + escala + componentes nucleo |

Si no hay sistema heredable, **construir uno** (no improvisar estilos por
elemento): definir tokens (color, tipografia, espaciado, radios, sombra),
escala tipografica y los componentes nucleo (boton, card, navegacion, input).
El sistema es el contrato que `verificar` hace cumplir.

### `reunir-contexto`

Antes de generar, sumar el contexto que ancla el resultado al producto real:

- screenshots o assets existentes del producto.
- captura de elementos de un sitio de referencia (web capture conceptual).
- documentos de origen (brief, contenido, datos para slides/tablas).
- restricciones tecnicas del target (framework, tokens disponibles, breakpoints).

Mas contexto = menos alucinacion visual. Sin contexto, la primera generacion es
mas debil; declararlo y proponer reunirlo antes de quemar iteraciones.

### `generar`

Materializar el artefacto que resuelve el brief, **anclado al sistema**:

- UI/frontend: codigo funcional (componentes, no mockup), usando los tokens y
  componentes del sistema.
- identidad: tokens ejecutables (JSON + CSS custom properties + Tailwind) + SVG
  de marca.
- slides/one-pager/landing: estructura + jerarquia + ritmo visual sobre el
  sistema.

La primera generacion es **punto de partida**, no entrega. Nombrarlo asi al
operador: el valor esta en iterar.

### `refinar`

Tres vias de cambio, segun el nivel:

| Via | Alcance | Cuando |
|---|---|---|
| **chat** | estructural amplio | reorganizar layout, cambiar enfoque, otra direccion |
| **comentario inline** | a nivel componente | ajustar un elemento especifico sin tocar el resto |
| **edicion directa** | micro-ajuste (mover/redimensionar/alinear) | refinamiento fino que no merece un turno de modelo |

Un cambio de token o componente se **propaga a todo el diseno** (cambiar una vez,
aplicar en todas partes). No reescribir elemento por elemento lo que el sistema
puede gobernar de una vez.

### `verificar`

**Autocorregir contra el design system ANTES de mostrar.** Checks:

- ¿cada color/tipografia/espaciado mapea a un token del sistema (no valores
  magicos sueltos)?
- ¿los componentes usados son los del sistema (no reinventados)?
- ¿la jerarquia visual respeta la escala definida?
- ¿contraste y tamanos cumplen accesibilidad (WCAG AA: contraste >= 4.5:1 texto
  normal, 3:1 texto grande; targets tactiles >= 44px)?
- ¿el axioma se sostiene — cada elemento aporta mas informacion que complejidad?

Si un check falla → volver a `generar`/`refinar` y corregir antes de entregar.
La autocorreccion es parte del trabajo, no un paso opcional.

### `entregar`

Cerrar con uno de:

- **handoff a Claude Code**: empaquetar un bundle continuable (codigo + tokens +
  estructura), no un screenshot — Claude Code continua desde el diseno existente.
- **export**: a HTML standalone, PPTX, PDF, .zip, o el formato que pida el target.
- **resumen al invocador**: que se construyo, contra que sistema, que quedo como
  deuda o supuesto, y la siguiente decision pendiente.

## Decision router

| Situacion detectada | Movimiento lider |
|---|---|
| Brief ambiguo en que/soporte | `enmarcar` |
| Hay codebase/repo/PPT pero no sistema resuelto | `anclar-design-system` |
| Falta material de origen o contexto del producto | `reunir-contexto` |
| Sistema y brief claros, sin artefacto aun | `generar` |
| Hay artefacto, requiere cambio | `refinar` |
| Artefacto listo, sin chequear contra sistema | `verificar` |
| Verificado, toca cerrar | `entregar` |

## Reglas duras

1. **El sistema antes que el pixel.** Ningun artefacto se genera sin un design
   system resuelto (heredado o construido). Estilos por elemento = drift.
2. **Trazabilidad de tokens.** Todo color, tipografia y espaciado mapea a un
   token. Valor magico suelto = deuda que `verificar` rechaza.
3. **Autocorregir antes de mostrar.** Verificar contra el sistema es parte de
   generar, no un paso posterior opcional.
4. **La primera generacion es borrador.** Declararlo: el valor esta en iterar,
   no en el primer disparo.
5. **Codigo funcional, no mockup.** El output de UI es frontend que ingenieria
   puede continuar, no una imagen.
6. **Handoff por bundle, no por screenshot.** Claude Code continua desde el
   trabajo existente; nunca se reconstruye desde una captura.
7. **Cambio de token se propaga.** Un ajuste de sistema se aplica en todo el
   diseno de una vez; no se reescribe elemento por elemento.
8. **Accesibilidad es regla, no gusto.** WCAG AA en contraste y targets es piso,
   no negociable por estetica.
9. **El gusto se ancla, no se improvisa.** Las decisiones de gusto (sustraccion,
   primeros principios) se consultan en `urn:dev:kb:steve-jobs-canon-diseno`, no
   de memoria.
10. **No invadir implementacion ni dominio.** La skill entrega forma y bundle; no
    despliega, no cablea backend, no decide copy estrategico.

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:cat-thinking` | la decision es de arquitectura/composicion del sistema visual (que compone con que) mas que de forma; cat-thinking da la critica estructural. |

## Salida esperada

- design system resuelto (origen + tokens + componentes nucleo).
- artefacto materializado (codigo frontend / tokens ejecutables / SVG / deck)
  anclado al sistema.
- reporte de verificacion contra el sistema (tokens, componentes, accesibilidad).
- cierre: handoff a Claude Code (bundle), export, o resumen con deuda y siguiente
  decision.