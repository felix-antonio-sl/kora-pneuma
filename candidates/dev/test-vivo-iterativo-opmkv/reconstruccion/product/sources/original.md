---
_manifest:
  urn: urn:dev:artefacto:test-vivo-iterativo-opmkv
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-05-04'
    source: 'Cristalizacion como skill del proceso in-vivo iterativo aplicado al modelador
      OPM en deep-opm-pro: Playwright contra dev server real, criterios DOM medibles
      contra CANON del repo, screenshots fullpage, reporte ejecutivo que reemplaza
      al previo, idempotencia por localStorage clear y refinamiento iterativo cuando
      aparecen falsos positivos.'
version: 0.1.1
status: activo
nombre: test-vivo-iterativo-opmkv
descripcion: 'Skill para auditoria in-vivo iterativa del modelador OPM (deep-opm-pro):
  conduce un navegador headless contra el dev server, ejecuta una bateria de criterios
  visuales/UX/funcionales contra el DOM, captura screenshots y errores de runtime,
  refina iterativamente cuando un FAIL/WARN viene de la sonda, y emite un reporte
  ejecutivo que siempre reemplaza al previo. Para usar cuando el operador pide validar
  in-vivo el modelador, regenerar el reporte tras un cambio o cerrar un loop con evidencia
  visual antes de commitear.'
tags:
- in-vivo
- browser
- playwright
- ux-audit
- visual-ssot
- opm
- modelador
- iterative-probe
- executive-report
- deep-opm-pro
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 1
      - 2
      - 2
      - 1
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:kora:kb:test-strategy
    - urn:kora:kb:canario-spec
    - urn:fxsl:kb:opm-es
    - urn:fxsl:kb:opd-es
    - urn:tde:kb:guia-calidad-web
    componible_con:
    - urn:dev:artefacto:ship-discipline
    - urn:kora:artefacto:cat-thinking
artefacto:
  perfil:
    dominio:
    - auditoria-in-vivo-de-aplicacion-web
    - validacion-visual-contra-ssot-del-repo
    - exploracion-funcional-end-to-end-en-navegador
    - reporteria-ejecutiva-idempotente
    - probe-engineering-iterativo
    disparadores:
    - el operador pide testear in-vivo el modelador OPM contra una URL del dev server
    - se necesita regenerar el reporte ejecutivo despues de un cambio en `app/`
    - antes de cerrar un loop de cambios visuales o de UX, se requiere evidencia browser
    - una sesion empieza con cambios sin commitear y se quiere validar comportamiento
      previo a commit
    - se requiere medir conformidad con `app/src/modelo/constantes.ts:CANON` directamente
      sobre el DOM renderizado
    salidas:
    - script de exploracion en `app/scripts/in-vivo-test.mjs` (idempotente, recibe
      URL como argumento)
    - screenshots fullpage en `app/test-results/in-vivo/` con nombres ordinales por
      escenario
    - '`app/test-results/in-vivo/_resumen.json` con findings estructurados por seccion/criterio/estado/detalle'
    - '`docs/REPORTE-EJECUTIVO.md` que SIEMPRE reemplaza al previo (no fechado, no
      versionado en filename)'
    - lista de hallazgos UX accionables y riesgos detectados, alineados con HANDOFF
      y mvp-alpha-coverage
    narrativa: Esta skill no escribe codigo de dominio del modelador. Conduce un navegador
      real contra el dev server, mide criterios objetivos contra el DOM renderizado,
      distingue defectos de la app de errores de la propia sonda (refinando en loop),
      y emite un reporte ejecutivo que siempre reemplaza al anterior para evitar deriva
      entre versiones.
  plan:
    estado_inicial: preparar
    estado_terminal: cierre
    estados:
    - id: preparar
      accion: verificar dev server, herramientas y directorios de salida
    - id: explorar
      accion: ejecutar navegador headless y capturar evidencia
    - id: analizar
      accion: clasificar findings y distinguir defecto de app vs sonda
    - id: refinar-sonda
      accion: corregir aserciones o secuencia UX y repetir exploracion
    - id: redactar-reporte
      accion: escribir reporte ejecutivo idempotente
    - id: cierre
      accion: resumir resultados y deuda residual
    - id: abortar
      accion: detener sin tocar artefactos cuando el preflight falla
    fsm:
      inicial: preparar
      terminales:
      - cierre
      - abortar
      transiciones:
        preparar:
        - explorar
        - abortar
        explorar:
        - analizar
        - abortar
        analizar:
        - refinar-sonda
        - redactar-reporte
        refinar-sonda:
        - explorar
        redactar-reporte:
        - cierre
        cierre: []
        abortar: []
  interfaz:
    herramientas:
    - Bash
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    permisos: Lectura/escritura sobre el repo deep-opm-pro (`app/scripts/`, `app/test-results/in-vivo/`,
      `docs/REPORTE-EJECUTIVO.md`). Ejecucion de Node + Playwright via Bash contra
      una URL HTTP del dev server especificada por el operador. No requiere auth.
      No commitea ni hace push automaticamente.
    protocolos:
      entrada: 'URL del dev server del modelador OPM (default `http://138.201.53.205:5173/`
        segun HANDOFF), opcional: lista de areas a profundizar.'
      salida: Resumen textual al operador con conteo OK/FAIL/WARN/INFO + ruta de screenshots
        + ruta del reporte ejecutivo + hallazgos UX accionables priorizados.
    api_observable:
      entradas:
      - nombre: url_objetivo
        tipo: url-http
        obligatorio: false
      - nombre: areas_a_profundizar
        tipo: lista-de-secciones
        obligatorio: false
      salidas:
      - nombre: resumen_findings
        tipo: texto-estructurado
      - nombre: ruta_screenshots
        tipo: ruta
      - nombre: ruta_reporte_ejecutivo
        tipo: ruta
      invariantes_io:
      - Si el dev server no responde 200, abortar antes de tocar artefactos.
      - Cero `pageerror` y cero `console.error` son criterios duros de salud.
      - Toda WARN/FAIL debe atribuirse a defecto de app o defecto de sonda; no quedan
        en limbo.
      - El reporte ejecutivo siempre reemplaza al previo en la misma ruta `docs/REPORTE-EJECUTIVO.md`.
  contexto:
    qa_budget:
      umbrales_minimos:
        ok_ratio: 0.9
        page_errors: 0
        console_errors: 0
        request_failures: 0
      criterios_bloqueantes:
      - FAIL en validacion de firma OPM (firma ilegal NO debe crear enlace)
      - FAIL en visual SSOT (fill, stroke, dimensiones contra CANON)
      - FAIL en persistencia (export/import o Guardar/Cargar)
      - pageerror > 0
    risk_register:
    - risk_id: tvi-falsos-positivos-de-sonda
      category: validez-de-medicion
      source: probe-engineering
      trigger: la sonda asume valores SSOT incorrectos o flujos UX en orden incorrecto
        y reporta FAIL/WARN espurios
      likelihood: 0.5
      impact: 0.4
      mitigation: antes de declarar defecto, leer `app/src/modelo/constantes.ts:CANON`
        y los handlers del store; refinar la sonda y reejecutar
      status: mitigated
    - risk_id: tvi-mensajes-status-acumulados
      category: ux-noise
      source: barra-de-status-toolbar
      trigger: la barra de status del Toolbar acumula mensajes entre escenarios y
        la sonda los lee como del escenario actual
      likelihood: 0.4
      impact: 0.2
      mitigation: limpiar localStorage + reload entre bloques; verificar mensaje en
        el momento de su accion, no diferido
      status: mitigated
    - risk_id: tvi-deriva-canon
      category: drift-de-spec
      source: app-evolves
      trigger: el repo cambia colores, dimensiones o tags SVG sin actualizar la sonda
      likelihood: 0.3
      impact: 0.5
      mitigation: leer `CANON` del repo en cada ciclo; nunca hardcodear valores en
        la sonda salvo cuando se verifica conformidad cromatica explicita y declarada
      status: monitored
    - risk_id: tvi-screenshot-stale
      category: artefacto-no-regenerado
      source: workdir-state
      trigger: el operador lee un screenshot viejo creyendo que refleja el commit
        actual
      likelihood: 0.2
      impact: 0.3
      mitigation: el script reescribe siempre todos los PNG del directorio; usar `mtime`
        reciente como heuristica de validez
      status: mitigated
    - risk_id: tvi-commit-no-autorizado
      category: accountability
      source: agente-invocador
      trigger: el agente confunde 'cierre del loop' con 'commitear el reporte'
      likelihood: 0.2
      impact: 0.5
      mitigation: 'default: no commitea. Solo entrega el patch listo y la ruta del
        reporte; commit requiere autorizacion explicita del operador'
      status: mitigated
  invariantes:
    reglas_duras:
    - El reporte ejecutivo en `docs/REPORTE-EJECUTIVO.md` siempre reemplaza al previo.
      No se versionan reportes con fecha o sufijo.
    - Antes de declarar un FAIL como defecto de la app, agotar la hipotesis de defecto
      de la sonda (orden UX, asuncion SSOT, timing). Documentar el descarte.
    - Los criterios visuales se miden contra `app/src/modelo/constantes.ts:CANON`
      leido en vivo, no contra valores externos.
    - Captura siempre `pageerror`, `console.error/warning` y `requestfailed`. Cero
      es criterio duro.
    - 'Idempotencia obligatoria: `localStorage.clear()` + `reload` entre bloques que
      mutan estado, para que la siguiente ejecucion no dependa del estado anterior.'
    - Screenshots fullpage en `app/test-results/in-vivo/` con nombres ordinales (`NN-descripcion.png`)
      que reflejan el orden del workflow.
    - El script vive en `app/scripts/in-vivo-test.mjs`, recibe la URL como `process.argv[2]`,
      default `http://138.201.53.205:5173/`.
    - Esta skill NO commitea, NO hace push y NO altera codigo de dominio del modelador.
      Su unico writeback son `app/scripts/in-vivo-test.mjs`, `app/test-results/in-vivo/`
      y `docs/REPORTE-EJECUTIVO.md`.
    - Si el dev server no responde 200, abortar y reportar ANTES de tocar artefactos.
    - Cuando un cambio del repo invalide la sonda (drift de CANON, nueva firma de
      enlace, nuevo selector), refinar la sonda en el mismo ciclo y dejarlo escrito
      en el reporte como deuda de calibracion.
---

# test-vivo-iterativo-opmkv

## Proposito

Skill operativa para **auditar in-vivo el modelador OPM** del repo
`deep-opm-pro` ejecutando una bateria iterativa de criterios visuales,
de UX y funcionales sobre un navegador real, capturando evidencia y
emitiendo un reporte ejecutivo que siempre reemplaza al anterior.

No es una skill de testing unitario; existe `bun run test` y
`bun run browser:smoke` para eso. Es una skill de **inspeccion en vivo
con refinamiento iterativo de la sonda**: la primera pasada casi siempre
genera FAIL/WARN espurios por asunciones de la sonda; la segunda pasada
los confirma como defectos reales de la app o los descarta tras leer el
codigo del repo. El cierre se da cuando todos los criterios estan
clasificados con evidencia.

## Cuando Usar

- el operador pide testear in-vivo el modelador contra una URL.
- se acaba de hacer un cambio en `app/` y se necesita evidencia browser
  antes de declarar el loop cerrado.
- se requiere validar conformidad visual contra `CANON` despues de
  tocar `proyeccion.ts` o `JointCanvas.tsx`.
- se quiere regenerar el `docs/REPORTE-EJECUTIVO.md` para reflejar el
  estado actual del corte.
- se quiere clasificar hallazgos UX accionables (no bloqueantes pero
  capitalizables) antes del proximo bloque de trabajo.

## Cuando No Usar

- testing unitario del kernel OPM -> `bun run test` en `app/`.
- smoke tests reproducibles checked-in -> `app/e2e/opm-smoke.spec.ts`
  con `bun run browser:smoke`.
- ingenieria inversa de OPCloud -> consultar `opm-extracted/` y delegar
  al subagente `opm-specialist`.
- diseno UX nuevo o auditoria UX exhaustiva -> usar
  `ux-research-design-ai` o `jobs-healthcare-ux`.
- construccion de modelos OPM como artefacto -> usar
  `urn:kora:artefacto:modelamiento-opm`.
- ciclos de cambio que tocan codigo de dominio: combinarla con
  `urn:dev:artefacto:ship-discipline` para blast radius y loop closure.

## Workflow

### `preparar`

1. Verificar que el dev server responde:

   ```bash
   curl -s -o /dev/null -w "%{http_code}" {URL} --max-time 5
   ```

   Si no es 200, abortar y reportar al operador. No tocar artefactos.

2. Verificar herramientas disponibles:

   - Node 24+ (o Bun) en PATH.
   - Playwright + Chromium instalado (`ls ~/.cache/ms-playwright/`).
   - Repo deep-opm-pro en `~/projects/deep-opm-pro/` con `app/` accesible.

3. Crear directorios si no existen:

   ```bash
   mkdir -p app/scripts app/test-results/in-vivo
   ```

4. Si el script `app/scripts/in-vivo-test.mjs` no existe, crearlo desde
   plantilla minima (ver `## Plantilla del script` mas abajo). Si existe,
   leerlo para entender que cubre antes de modificarlo.

### `explorar`

Ejecutar el script con la URL del operador:

```bash
cd app
node scripts/in-vivo-test.mjs {URL}
```

El script DEBE:

- abrir Chromium headless 1440x900,
- registrar `pageerror`, `console.error/warning`, `requestfailed`,
- recorrer un workflow ordinal (carga, toolbar, demo, visual SSOT,
  inspector, enlaces, validacion firma, JSON, persistencia local, arbol
  OPD, agregacion, drag, responsive, eliminar),
- limpiar `localStorage` entre bloques que mutan estado,
- emitir `_resumen.json` con conteos por estado y findings ordenados.

### `analizar`

Para cada finding:

1. Si es OK -> registrar y continuar.
2. Si es INFO -> es dato; revisar si revela algo que merezca observacion.
3. Si es WARN -> hipotesis primaria: defecto de sonda. Verificar:
   - Lee `app/src/modelo/constantes.ts:CANON` y compara con la asercion.
   - Lee el handler relevante en `app/src/store.ts` y `app/src/render/jointjs/`.
   - Lee la UX del flujo en `app/src/ui/Toolbar.tsx`.
   - Si la sonda esta mal: ir a `refinar-sonda`.
4. Si es FAIL -> hipotesis primaria: defecto de app. Pero igualmente
   confirmar contra el codigo antes de declarar bug en el reporte.

Sin embargo, criterios bloqueantes (firma OPM, SSOT, persistencia,
pageerror) son siempre defectos serios y no se pueden reclasificar como
falsos positivos sin evidencia explicita en el codigo del repo.

### `refinar-sonda`

Cuando un FAIL/WARN es defecto de sonda, editar
`app/scripts/in-vivo-test.mjs` para:

1. corregir la asercion (e.g. `fill=#fdffff` no `fill=#70E483`),
2. corregir el orden de UX (e.g. seleccionar entidad ANTES de elegir tipo
   de enlace),
3. respetar comportamientos por diseno (e.g. `cargarDemo` resetea undo).

Documentar el cambio y reejecutar `explorar`. La iteracion termina cuando
el conjunto OK/FAIL/WARN refleja la app real, no las asunciones de la
sonda.

### `redactar-reporte`

Escribir `docs/REPORTE-EJECUTIVO.md` reemplazando el archivo previo. El
reporte DEBE incluir:

1. **Veredicto** con tabla de conteos (Criterios, OK, FAIL, WARN, INFO,
   pageerror, console errors, request failures) y una linea de juicio.
2. **Cobertura por seccion** (carga, toolbar, demo, visual SSOT,
   inspector, enlaces, etc.) con conteos.
3. **Detalle de criterios** desde `_resumen.json`, idealmente generado
   por el mismo script para evitar deriva entre `_resumen.json` y el
   reporte.
4. **Runtime** (`pageerror`, `console.error/warning`, `requestfailed`).
5. **Artefactos generados** (lista de PNG).
6. **Hallazgos UX accionables** (no bloqueantes pero capitalizables).
7. **Riesgos detectados**.
8. **Proximos pasos** alineados con `docs/HANDOFF.md` y
   `docs/roadmap/mvp-alpha-coverage.md`.
9. **Como reproducir** (comando exacto).

### `cierre`

Resumir al operador en menos de 200 palabras:

- conteo OK/FAIL/WARN/INFO,
- ruta del reporte y de los screenshots,
- 2-3 hallazgos UX accionables principales,
- propuesta de siguiente paso (no commitear sin autorizacion).

## Plantilla del script

El script vive en `app/scripts/in-vivo-test.mjs` y sigue este shape
minimo (no copiar literal; adaptar a la version vigente del repo):

```js
import { chromium } from "@playwright/test";
import { mkdirSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const URL_OBJETIVO = process.argv[2] ?? "http://138.201.53.205:5173/";
const RAIZ_REPO = resolve(import.meta.dirname, "..", "..");
const DIR_SHOTS = resolve(RAIZ_REPO, "app/test-results/in-vivo");

mkdirSync(DIR_SHOTS, { recursive: true });

const findings = [];
const pageErrors = [];
const consoleMessages = [];
const requestFailures = [];

function record(seccion, criterio, estado, detalle) {
  findings.push({ seccion, criterio, estado, detalle });
}
async function shot(page, nombre) {
  await page.screenshot({ path: resolve(DIR_SHOTS, nombre), fullPage: true });
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
const page = await context.newPage();
page.on("pageerror", (e) => pageErrors.push(e.message));
page.on("console", (m) => {
  if (m.type() === "error" || m.type() === "warning") consoleMessages.push({ type: m.type(), text: m.text() });
});
page.on("requestfailed", (r) => requestFailures.push({ url: r.url(), reason: r.failure()?.errorText }));

try {
  await page.goto(URL_OBJETIVO, { waitUntil: "networkidle", timeout: 20000 });
  // ... bloques ordinales: carga, toolbar, demo, visual SSOT, inspector,
  //     crear-enlace, validacion-firma, JSON, persistencia local,
  //     arbol OPD, agregacion, drag, responsive, eliminar.
  //     Cada bloque hace screenshots y record() de criterios.
} finally {
  await browser.close();
}

writeFileSync(resolve(DIR_SHOTS, "_resumen.json"), JSON.stringify({
  fecha: new Date().toISOString(),
  url: URL_OBJETIVO,
  totalCriterios: findings.length,
  ok: findings.filter((f) => f.estado === "OK").length,
  fail: findings.filter((f) => f.estado === "FAIL").length,
  warn: findings.filter((f) => f.estado === "WARN").length,
  info: findings.filter((f) => f.estado === "INFO").length,
  pageErrors, consoleMessages, requestFailures, findings,
}, null, 2));
```

## Heuristicas para construir criterios

- **Visual SSOT**: medir `tag`, `fill`, `stroke`, `stroke-width`,
  `stroke-dasharray`, dimensiones via `evaluateAll` y comparar contra
  los valores observados (no asumidos). Para el modelador OPM hoy: rect
  para objeto, ellipse para proceso, fill `#fdffff`, stroke `#70E483`
  o `#3BC3FF` segun tipo, dims 135x60, dasharray `8 4` para ambiental.
- **UX de creacion de enlace**: la app exige seleccionar entidad origen
  ANTES de elegir tipo en el picker. La sonda debe reflejar ese orden.
- **Undo despues de Demo**: `cargarDemo` resetea historial por diseno;
  Ctrl+Z no debe reducir elementos. Para probar undo real, crear
  manualmente y luego deshacer.
- **Validacion firma**: intentar consumo objeto->objeto y verificar que
  NO se crea enlace y aparece mensaje en la barra de status.
- **Import corrupto**: enviar JSON con `opds["opd-1"] = null` y
  verificar mensaje de error sin mutar el modelo.
- **Persistencia local**: ciclo Guardar (limpia dirty) -> mutar (reaparece
  '(No guardado)') -> Cargar (regresa a guardado, sin dirty).
- **Arbol OPD**: importar JSON multi-OPD; verificar que click en hijo
  cambia OPD activo y filtra canvas + OPL.
- **Agregacion**: verificar `polygon` triangular y que NO expone tools
  de vertices.
- **Responsive**: probar 1024x700 y 1920x1080; medir `body.scrollWidth
  === body.clientWidth`.

## Composicion con otras skills

- `urn:dev:artefacto:ship-discipline`: para que el ciclo de cambio que
  motiva la auditoria respete blast radius y cierre el loop antes del
  commit.
- `urn:kora:artefacto:cat-thinking`: cuando la auditoria revela tension
  arquitectural (por ejemplo, agregacion estructural vs procedimental,
  CANON como spec dual de fill/stroke), hacer lectura categorial minima
  antes de proponer fix.
- `urn:kora:artefacto:modelamiento-opm`: si la auditoria detecta deriva
  semantica respecto a SSOT OPM/ISO 19450, delegar el dictamen normativo.

## Antipatrones

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| sonda hardcoded contra valores externos | mide contra OPCloud, no contra el repo | leer `CANON` del repo en cada ciclo |
| FAIL declarado sin verificar codigo | reporta bugs inexistentes | agotar hipotesis de defecto de sonda primero |
| reporte versionado con fecha en filename | acumula reportes obsoletos | `docs/REPORTE-EJECUTIVO.md` siempre reemplaza |
| commit automatico tras correr la skill | accountability rota | default no commitea; pedir autorizacion |
| screenshots no regenerados | operador lee evidencia stale | el script reescribe todos los PNG en cada run |
| asercion de orden UX equivocada | falsos negativos en flujos correctos | leer el store antes de escribir asserts |
| umbrales magicos | umbrales sin justificacion fallan en sesiones reales | declarar `qa_budget` y citarlo en el reporte |

## Recursos

- `scripts/`: el script de exploracion vive en
  `app/scripts/in-vivo-test.mjs` (en el repo deep-opm-pro, no en esta
  skill). La skill describe su contrato; el script es artefacto del
  proyecto.
- `referencias/`: ninguna por defecto. Si surge documentacion
  detallada de criterios o catalogo de selectores reusables, moverla
  aqui.
