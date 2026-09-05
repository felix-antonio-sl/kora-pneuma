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
- preparar handoff de un diseno a un agente de codigo receptor (bundle
  continuable, no screenshot).
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
- **Sustracción (binaria).** Antes de mostrar, pasar la propia salida por las
  preguntas letales del canon anclado (`urn:dev:kb:steve-jobs-canon-diseno`): ¿qué
  tres elementos cortarías?, ¿es una cosa o varias fingiendo ser una?, ¿inevitable o
  solo competente? Si no podés nombrar tres para cortar, no miraste lo suficiente —
  volvé a `refinar`. Corte o no-corte, no ensayo.
- **¿las referencias del artefacto resuelven? (estático, sin ejecutar build):** todo
  import/referencia interna del código generado apunta a un símbolo o archivo
  presente, o a una dependencia nombrada; sin componentes fantasma. Es lectura
  (Read/Grep) del propio output, no ejecución: la skill garantiza continuabilidad
  estática; el build ejecutable y el render son del receptor (regla 10).

Si un check falla → volver a `generar`/`refinar` y corregir antes de entregar. La
autocorrección es parte del trabajo, no opcional. Techo de seguridad: si tras 3
ciclos completos `generar→refinar→verificar` un check sigue en rojo, detener y
reportar el bloqueo al operador con el último error en vez de seguir iterando — un
bucle que no converge es deuda, no diligencia (única excepción reglada a
"autocorregir antes de mostrar").

### `entregar`

Cerrar con uno de:

- **handoff a agente de codigo — bundle continuable con contrato** (no screenshot). El
  bundle fija roles, no rutas literales: **artefacto** (código frontend / tokens /
  deck), **tokens** (JSON + CSS custom properties + Tailwind) y **`HANDOFF.md`**
  (manifiesto: qué se construyó, contra qué design system, punto de entrada, comando
  de build/preview declarado como `verificado-por: receptor`, deuda/supuestos, y la
  siguiente decisión pendiente). Antes del handoff, validar que el bundle está bien
  formado: existen entrypoint, tokens y manifiesto, y su árbol coincide con lo que
  `HANDOFF.md` declara. Se escribe en staging aislado (el que indique el operador),
  nunca in-place sobre el frontend vivo salvo instrucción explícita. Es el contrato
  que deja a Codex, Claude Code u OpenCode continuar sin reconstruir (regla 6).
- **export**: a HTML standalone, PPTX, PDF, .zip, o el formato que pida el target.
- **resumen al invocador**: el mismo cierre que recoge `HANDOFF.md` — qué se
  construyó, contra qué sistema, qué quedó como deuda o supuesto, y la siguiente
  decisión pendiente — cuando la salida no es un bundle de handoff.

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
5. **Código funcional, no mockup.** El output de UI es frontend que ingeniería
   puede continuar, no una imagen. La skill verifica estáticamente su
   **continuabilidad** (referencias resueltas, sin componentes fantasma); que el
   código **funcione en runtime** lo prueba el receptor al montarlo (la skill no
   ejecuta el build — regla 10). Continuable ≠ funcional-probado: la skill garantiza
   lo primero, el receptor lo segundo.
6. **Handoff por bundle, no por screenshot.** El agente receptor continúa desde el
   trabajo existente; nunca se reconstruye desde una captura.
7. **Cambio de token se propaga.** Un ajuste de sistema se aplica en todo el
   diseno de una vez; no se reescribe elemento por elemento.
8. **Accesibilidad es regla, no gusto.** WCAG AA en contraste y targets es piso,
   no negociable por estetica.
9. **El gusto se ancla y se ejecuta, no se improvisa ni se decora.** Las decisiones
   de gusto se consultan en `urn:dev:kb:steve-jobs-canon-diseno`; además,
   `verificar` pasa la propia salida por sus preguntas letales como guardia binaria
   de sustracción. Anclar sin ejecutar es import muerto.
10. **No invadir implementación ni dominio.** La skill entrega forma y bundle; no
    despliega, no cablea backend, no integra al codebase vivo, no decide copy. Pero
    verificar estáticamente la continuabilidad del propio output y empaquetar el
    contrato de handoff SÍ es de la skill: validar lo que uno produjo y definir qué
    se entrega es deber del emisor; ejecutar el build y montarlo en producción es del
    receptor.

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:cat-thinking` | la decision es de arquitectura/composicion del sistema visual (que compone con que) mas que de forma; cat-thinking da la critica estructural. |

## Salida esperada

- design system resuelto (origen + tokens + componentes nucleo).
- artefacto materializado (codigo frontend / tokens ejecutables / SVG / deck)
  anclado al sistema.
- reporte de verificacion contra el sistema (tokens, componentes, accesibilidad).
- cierre: handoff al agente de código (bundle), export, o resumen con deuda y siguiente
  decision.
