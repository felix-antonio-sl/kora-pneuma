# design

## Proposito

Materializa trabajo visual con el sistema de canvas, componentes y estados
heredado de Claude Design:
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

Heuristica estética heredada, útil cuando el brief valora compresión sin pérdida:

> **Belleza = max(informacion / simpleza)**

Cada elemento debe justificar la información, función o carácter que aporta frente a
la complejidad que introduce. La compacidad no puede borrar acceso, contenido,
contexto, estados ni identidad visual. El gusto se ancla en
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

El contexto pertinente mejora el anclaje; acumularlo no garantiza calidad.
Resuelve lo material que falte y usa propuestas explícitas para decisiones
reversibles dentro del brief.

### `generar`

Materializar el artefacto que resuelve el brief, **anclado al sistema**:

- UI/frontend: codigo funcional (componentes, no mockup), usando los tokens y
  componentes del sistema.
- identidad: tokens ejecutables (JSON + CSS custom properties + Tailwind) + SVG
  de marca.
- slides/one-pager/landing: estructura + jerarquia + ritmo visual sobre el
  sistema.

La primera generación se revisa como cualquier otra. Si cumple el brief y
las comprobaciones pertinentes, puede entregarse; iterar requiere un defecto
o una incertidumbre que resolver.

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
  normal, 3:1 texto grande, con las excepciones de SC 1.4.3)? Para tamaño
  de objetivos, WCAG 2.2 SC 2.5.8 AA establece 24×24 CSS px o una excepción
  aplicable, incluido espaciado; SC 2.5.5 AAA usa 44×44 con sus excepciones.
  El contexto puede justificar objetivos mayores; 44px no es un mínimo AA universal.
- **Sustracción fundada.** Cuando una decisión de gusto lo requiera, pasar la salida
  por las preguntas del canon: qué puede retirarse sin perder tarea, acceso, estado,
  seguridad o carácter; si es una cosa coherente; y qué todavía se siente genérico.
  No existe una cuota de tres cortes. Conservar explícitamente un elemento necesario
  es una decisión válida cuando se explica la pérdida que evita.
- **¿las referencias del artefacto resuelven? (estático, sin ejecutar build):** todo
  import/referencia interna del código generado apunta a un símbolo o archivo
  presente, o a una dependencia nombrada; sin componentes fantasma. Es lectura
  (Read/Grep) del propio output, no ejecución: la inspección acredita sólo lo revisado. Si están disponibles las herramientas
  y el encargo incluye materialización, ejecutar build o render del artefacto
  propio cuando permita comprobarlo; dejar pendiente lo no ejecutado.

Si un check falla → volver a `generar`/`refinar` y corregir antes de entregar. La
autocorrección es parte del trabajo, no opcional. Continúa sólo mientras otra iteración pueda resolver un fallo material dentro
del alcance; si falta una capacidad o decisión imprescindible, entrega el
resultado revisable y el impedimento concreto.

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
  que permite al receptor continuar desde las fuentes y los recursos.
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
4. **Revisión antes de entrega.** No exige otra generación si la primera
   ya satisface el propósito y las comprobaciones pertinentes.
5. **Código continuable cuando el artefacto es UI.** El output de UI es frontend que
   ingeniería puede continuar, no una imagen usada como sustituto. La skill verifica estáticamente su
   **continuabilidad** (referencias resueltas, sin componentes fantasma); el funcionamiento exige ejecución. Puede ejecutar build o render autorizados
   sobre su artefacto; ninguna inspección estática garantiza el runtime del receptor.
6. **Handoff por bundle, no por screenshot.** El agente receptor continúa desde el
   trabajo existente; nunca se reconstruye desde una captura.
7. **Cambio de token se propaga.** Un ajuste de sistema se aplica en todo el
   diseno de una vez; no se reescribe elemento por elemento.
8. **Accesibilidad es regla, no gusto.** WCAG AA en contraste y targets es piso,
   no negociable por estetica.
9. **El gusto se ancla y se contrasta.** Consultar el canon cuando una decisión de
   gusto o sustracción lo necesite, aplicarlo al artefacto concreto y registrar la
   pérdida de cada corte o conservación. El canon no reemplaza brief, evidencia o
   restricciones del dominio.
10. **Autoridad según encargo.** Materializa y comprueba la forma, el contenido
    de interfaz y su bundle dentro del alcance autorizado. Puede integrar cambios
    visuales y ejecutar su build cuando el encargo lo incluye. Despliegue, lógica
    interna y decisiones de dominio requieren el alcance y la capacidad pertinentes.

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

## Evidencia y casos discriminantes

Separar forma propuesta, comprobación estática, build, render y experiencia observada.
La generación no acredita corrección; una comprobación real debe nombrar
criterio, método y alcance. Si no se ejecutó el artefacto, declarar
build, interacción, accesibilidad y rendimiento como pendientes. Herramientas o formatos
nombrados son rutas posibles y no APIs instaladas.

- Identidad visual para una pieza estática: resolver tokens, jerarquía y export sin
  exigir frontend o prototipo interactivo.
- Dos elementos necesarios en una UI: conservar ambos y explicar su función; no inventar
  un tercer corte para satisfacer la heurística.
- Dirección ya elegida y repositorio ausente: entregar especificación y bundle
  continuable, sin afirmar build ni runtime.
- Sistema existente con un valor excepcional justificado: registrar la excepción y su
  alcance; no borrar carácter para conseguir uniformidad mecánica.

Fuentes de accesibilidad para los criterios citados, consultadas 2026-09-13:
[SC 2.5.8 AA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html),
[SC 2.5.5 AAA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html) y
[SC 1.4.3 AA](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
