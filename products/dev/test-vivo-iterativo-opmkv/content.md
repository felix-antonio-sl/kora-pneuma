
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

const URL_OBJETIVO = process.argv[2];
if (!URL_OBJETIVO) throw new Error("Falta la URL de desarrollo indicada por el operador");
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

## Disponibilidad de referencias anteriores

`jobs-healthcare-ux` permanece archivado y desactivado. Para el recorrido UX
se conserva disponible `ux-research-design-ai`, ya indicado en el cuerpo.
