
# test-vivo-iterativo-opmkv

## Proposito

Skill operativa para **auditar in-vivo el modelador OPM** del repo
objetivo ejecutando criterios visuales, de UX y funcionales sobre un
navegador real, capturando evidencia y emitiendo un reporte ejecutivo
dentro del mandato del encargo.

Es una skill de **inspeccion en vivo con refinamiento iterativo de la
sonda**: cada hallazgo se clasifica contra evidencia; tantas pasadas como
requiera la evidencia, sin numero supuesto. El cierre se da cuando todos
los criterios estan clasificados con evidencia.

El repo objetivo y su acceso (URL, sesion, credencial esperada) los indica
el operador o vienen inequivocos del contexto vigente. La URL nunca se
inventa ni trae default. Sin objetivo claro no hay ejecucion.

Todo writeback ocurre solo dentro del repo objetivo y del mandato del
encargo (`app/scripts/`, `app/test-results/in-vivo/`,
`docs/REPORTE-EJECUTIVO.md` u otras rutas que el encargo fije); fuera de
ahi, solo lectura. Una referencia a otro proyecto no autoriza modificarlo.

## Cuando Usar

- el operador pide testear in-vivo el modelador contra un objetivo.
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
- ingenieria inversa de OPCloud -> consultar `opm-extracted/` y
  `urn:fxsl:artefacto:opm-specialist` cuando este admitido; mientras
  tanto, lectura directa de `urn:fxsl:kb:opm-es`.
- diseno UX nuevo o auditoria UX exhaustiva -> usar
  `urn:dev:artefacto:ux-research-design-ai`.
- construccion de modelos OPM como artefacto -> usar
  `urn:kora:artefacto:modelamiento-opm`.
- ciclos de cambio que tocan codigo de dominio: combinarla con
  `urn:dev:artefacto:ship-discipline` para blast radius y loop closure.

## Workflow

### `preparar`

0. Fijar objetivo: repo, URL/acceso y alcance, del operador o
   inequivocos del contexto. Lo dudoso se verifica; lo claro no se
   revalida por rutina.

1. Verificar acceso al objetivo (p. ej. `curl` con timeout). Si no hay
   ruta, timeout o conexion rechazada: no hay ejecucion comprobable con
   ese objetivo (no tocar artefactos del repo). El analisis de evidencia
   ya capturada y el reporte honesto del limite, con parciales
   conservados, siguen autorizados dentro del mandato. Una redireccion o autenticacion esperada por el
   contexto no es automaticamente un fallo: seguirla segun el encargo y
   registrarla. Solo abortar si el objetivo efectivo no es verificable.
   Un fallo de acceso bloquea el browser, no todo analisis: la evidencia
   ya capturada admite analisis independiente y el reporte honesto del
   limite sigue siendo entregable.

2. Verificar el toolchain efectivo del repo (leer `package.json`, docs o
   CI: runtime, version, Playwright/Chromium disponible). Sin versiones
   por defecto; lo que falte se reporta.

3. Usar directorios y artefactos existentes del repo objetivo. Solo crear
   o versionar script/directorios cuando el encargo lo requiere; nunca
   por rutina. Si el script de exploracion existe, leerlo antes de
   modificarlo.

### `explorar`

Ejecutar la sonda contra el objetivo con la cobertura proporcional al
cambio que motiva la auditoria: el slice pertinente para cambios
acotados; el workflow ordinal completo (carga, toolbar, demo, visual
SSOT, inspector, enlaces, validacion firma, JSON, persistencia local,
arbol OPD, agregacion, drag, responsive, eliminar) para cortes,
regresiones o estados desconocidos.

La sonda, en lo que cubra:

- abre Chromium headless con viewport declarado (default 1440x900 salvo
  indicacion);
- registra `pageerror`, `console.error/warning`, `requestfailed`;
- aisla estado con contexto de navegador fresco por ejecucion, sin
  borrar almacenamiento persistente fuera del contexto de prueba;
- emite `_resumen.json` identificado por corrida, con conteos y findings.

### `analizar`

Para cada finding, hipotesis desde evidencia: tipo de criterio, trazas
capturadas, reproduccion, codigo a la vista. Un WARN o un FAIL puede ser
defecto de app, defecto de sonda, efecto de entorno o indeterminado con
lo capturado; ninguna etiqueta decide la causa. Distinguir siempre
**defecto de sonda demostrado** (evidencia positiva: valor contra CANON
vivo, orden contra UX observada, prueba de timing) de **oraculo sin
procedencia** (valor esperado sin fuente o insuficiente para atribuir):
lo segundo cierra como **indeterminado**, nunca como error de sonda. La
ausencia de codigo, CANON o traza no acredita error de app ni de sonda.
Separar siempre **resultado informado por la fuente** (fixture, resumen,
traza ajena) de **observado por el agente**: lo informado se reporta
como defecto informado por fixture con confianza acotada, sin afirmar
comprobacion propia. Todo indeterminado declara el dato minimo que lo
resolveria. Vias validas para
confirmar un bug o refutar un falso positivo: lectura de codigo,
reproduccion del caso, evidencia decisiva ya capturada. Hallazgos en
criterios bloqueantes (firma OPM, SSOT, persistencia, pageerror) son
potencialmente graves y exigen evidencia explicita para reclasificarse;
la etiqueta no acredita por si sola un defecto real.

- OK: registrar y continuar.
- INFO: revisar si revela algo que merezca observacion.
- WARN/FAIL: verificar por la via mas decisiva y barata primero:
  `CANON` vivo del repo para aserciones visuales, handlers y store para
  orden UX y comportamiento, reproduccion para intermitencias. Si la
  sonda esta mal: ir a `refinar-sonda`.

### `refinar-sonda`

Corregir asercion, orden UX o respeto a comportamientos por diseno.
Documentar el cambio. Reejecutar `explorar` solo si cambio
comportamiento, selectores, flujos o datos; si la correccion es solo del
oraculo y la evidencia capturada basta, reclasificar con reevaluacion
documentada. Terminar cuando el conjunto refleja la app real.

### `redactar-reporte`

Escribir el reporte dentro del mandato: reemplaza unicamente el reporte
previo propio y prescindible (verificado por marcador y mandato). Un
informe ajeno no se toca jamas (el marcador propio no autoriza sobre lo
ajeno), salvo autorizacion especifica sobre ese informe; capturas historicas necesarias se conservan. Cada corrida
conserva su evidencia identificada; solo lo propio prescindible se
reemplaza con mandato. Si la ruta esta ocupada por otro, proponer
alternativa. El reporte incluye veredicto con conteos, cobertura,
detalle desde `_resumen.json`, runtime, artefactos, hallazgos UX,
riesgos, proximos pasos y como reproducir.

### `cierre`

Resumen breve al operador: conteos, rutas, hallazgos principales,
siguiente paso. Commits solo dentro de la autoridad ya concedida; si el
encargo no la incluye, pedirla.

## Plantilla del script (ejemplo de origen, adaptar a la estructura efectiva)

El script vive en el repo objetivo (no en esta skill). Ejemplo minimo;
adaptar imports, rutas y comandos al repo efectivo:

```js
import { chromium } from "@playwright/test";
import { mkdirSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const URL_OBJETIVO = process.argv[2];
if (!URL_OBJETIVO) throw new Error("Falta la URL indicada por el operador o el contexto");
const RAIZ_REPO = resolve(import.meta.dirname, "..", "..");
const DIR_SHOTS = resolve(RAIZ_REPO, "app/test-results/in-vivo");
// ... findings, listeners, bloques ordinales segun cobertura ...
let fallo = null;
try {
  await page.goto(URL_OBJETIVO, { waitUntil: "networkidle", timeout: 20000 });
  // ... bloques ...
} catch (e) {
  fallo = String(e?.message ?? e);
} finally {
  await browser.close().catch(() => {});
}
writeFileSync(resolve(DIR_SHOTS, "_resumen.json"), JSON.stringify({
  fecha: new Date().toISOString(),
  url: URL_OBJETIVO,
  fallo,
  // ... conteos y findings, incluidos los capturados antes de la excepcion ...
}, null, 2));
```

El resumen se escribe siempre, incluso ante excepcion: el fallo y la
evidencia parcial se conservan, nunca se pierden en el `finally`.

## Heuristicas para construir criterios

Valores de referencia heredados del repo de origen (NO norma vigente):
orientan que medir, nunca deciden conformidad. Cada ciclo relee el
`CANON` vivo del repo objetivo. El `CANON` describe la implementacion
vigente; la norma OPM/ISO vive en la SSOT (`urn:fxsl:kb:opm-es`). Cuando
tensionan, se registra cual rige cada juicio: conformidad visual contra
el `CANON`, validez formal contra la SSOT.

- **Visual SSOT**: medir `tag`, `fill`, `stroke`, `stroke-width`,
  `stroke-dasharray` y dimensiones via `evaluateAll` contra el `CANON`
  vivo (los valores de origen son historia, no objetivo).
- **UX de creacion de enlace**: verificar el orden efectivo en el repo
  (origen: entidad antes que tipo en el picker); la sonda refleja el
  orden real, no el supuesto.
- **Undo despues de Demo**: verificar el comportamiento efectivo
  (origen: `cargarDemo` reseteaba historial); probar undo real creando
  manualmente.
- **Validacion firma**: intentar consumo objeto->objeto y verificar que
  NO se crea enlace y aparece mensaje en la barra de status.
- **Import corrupto**: enviar JSON con `opds["opd-1"] = null` y
  verificar mensaje de error sin mutar el modelo.
- **Persistencia local**: ciclo Guardar -> mutar -> Cargar, verificando
  estados dirty/guardado efectivos.
- **Arbol OPD**: importar JSON multi-OPD; verificar OPD activo y
  filtrado tras click en hijo.
- **Agregacion**: verificar forma triangular y herramientas de vertices
  segun implementacion efectiva.
- **Responsive**: viewports pertinentes al repo; medir
  `body.scrollWidth === body.clientWidth` donde aplique.

## Composicion con otras skills

- `urn:dev:artefacto:ship-discipline`: para que el ciclo de cambio que
  motiva la auditoria respete blast radius y cierre el loop antes del
  commit.
- `urn:kora:artefacto:cat-thinking`: solo cuando la auditoria revela una
  tension arquitectural que exige lectura categorial antes de proponer
  fix. Nunca como capa obligatoria ante cualquier tension.
- `urn:kora:artefacto:modelamiento-opm`: solo si la auditoria detecta
  deriva semantica respecto a SSOT OPM/ISO 19450, delegar el dictamen
  normativo. No es capa obligatoria del recorrido.

## Antipatrones

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| sonda hardcoded contra valores externos | mide contra OPCloud, no contra el repo | leer `CANON` vivo en cada ciclo; valores de origen son historia |
| FAIL declarado sin evidencia decisiva | reporta bugs inexistentes | confirmar por codigo, reproduccion o evidencia capturada |
| presuncion por etiqueta | WARN siempre sonda, FAIL siempre app | ambos pueden ser app, sonda, entorno o indeterminado |
| reporte versionado con fecha en filename | acumula reportes obsoletos | identificar por corrida; reemplazar solo lo propio prescindible con mandato |
| reemplazar informe ajeno | pisa trabajo de otros | jamas tocarlo; el marcador propio no autoriza sobre lo ajeno |
| borrar capturas necesarias | destruye evidencia | conservar por corrida lo necesario; reevaluar antes de reemplazar |
| commit fuera de autoridad | accountability rota | commitear solo dentro de la autoridad concedida |
| screenshots no regenerados | operador lee evidencia stale | cada corrida conserva su evidencia identificada |
| asercion de orden UX equivocada | falsos negativos en flujos correctos | leer el store antes de escribir asserts |
| umbrales magicos | fallan en sesiones reales | `qa_budget` con valores del operador o del repo; sin valores, no inventar |
| borrar estado persistente para aislar | destruye datos del operador | contexto fresco por ejecucion; sin borrado fuera del contexto |
| asumir URL o entorno | objetivo equivocado | operador o contexto inequivoco; preflight verifica lo dudoso |
| crear script/dirs por rutina | versiona basura | usar artefactos existentes; crear solo requerido y autorizado |
| resumen perdido en excepcion | se pierde el fallo | escribir resumen siempre, con fallo y evidencia parcial |
| CANON heredado como norma | juzga con historia | norma = SSOT; CANON = implementacion vigente leida en vivo |

## Recursos

- `scripts/`: el script de exploracion vive en el repo objetivo (no en
  esta skill). La skill describe su contrato; el script es artefacto del
  proyecto.
- `referencias/`: ninguna por defecto. Documentacion de criterios o
  catalogo de selectores reusables, solo si surge y sirve.

## Disponibilidad de referencias anteriores

`jobs-healthcare-ux` permanece archivado y desactivado; no usarlo como
alternativa. Para el recorrido UX se conserva disponible
`urn:dev:artefacto:ux-research-design-ai`, ya indicado en el cuerpo.
