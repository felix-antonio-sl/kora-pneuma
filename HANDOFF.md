# Handoff vigente — 2026-08-01 — Steipete delega ejecución a Fugaz

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, las instalaciones runtime ni el estado vivo del
> host. Los hashes y resultados siguientes sólo describen el candidato exacto
> evaluado.

## Objetivo y resultado

Se diseñó y realizó el ejecutor al que Steipete puede delegar tareas de código:
`urn:dev:artefacto:fugaz` v2.0.1. Fugaz es un subagente Codex efímero,
minimalista y estricto: recibe una tarea cerrada, implementa el menor cambio
completo dentro de propiedad y autoridad explícitas, verifica hasta cierre y
devuelve un recibo tipado. Steipete v1.2.1 conserva intención, arquitectura,
topología, integración y juicio final.

El resultado está completo en la fuente KORA y en el runtime Codex. La
proyección actual de Steipete también está en paridad en Claude Code, Codex,
OpenCode y OpenClaw. La rama limpia del blueprint OpenClaw fue publicada; no se
publicó `openclaw-fleet/main` porque contenía dos commits locales anteriores a
esta sesión.

## Alcance cerrado

Incluido:

- migración `migrar-o-omitir` de la identidad histórica Fugaz a la ontología
  vigente de pneuma;
- contrato observable de entrada, salida, errores, autoridad y cierre;
- adaptador Steipete → Fugaz para Codex;
- pruebas canónicas, emisión, instalación, paridad y canarios in vivo;
- actualización y materialización controlada del blueprint Steipete de
  OpenClaw;
- documentación, memoria durable, commits y publicación selectiva.

Excluido deliberadamente:

- fijar un modelo comercial o nivel de razonamiento dentro de la identidad;
  esa selección pertenece al runtime y no amplía autoridad;
- realizar Fugaz en targets distintos de Codex;
- convertir Fugaz en coordinador, integrador o suborquestador recursivo;
- resolver degradaciones globales de OpenClaw, colas, índices de memoria o
  sincronización documental ajenas al contrato Steipete–Fugaz;
- incorporar o publicar modificaciones concurrentes en `AGENTS.md`.

## Decisiones consolidadas

1. **Fugaz es `forma=subagente`, `arnes=delegado`, target Codex.** Su unidad de
   vida es una invocación efímera. La alternativa de conservar el agente
   orquestador legado contradecía el cuerpo que se quería construir. Tras la
   refutación adversarial, el operador autorizó conservar la URN con major
   `2.0.0`: se trató como corrección durante la primera migración a pneuma, no
   como democión de una fuente pneuma ya encarnada. Se descartó la alternativa
   estricta de crear otra URN y retirar la identidad histórica; la procedencia
   y este límite interpretativo permanecen explícitos en la fuente canónica.
2. **Una tarea es un paquete tipado.** `objective`, `workspace`, `candidate`,
   `owned_scope`, `acceptance` y `authority` son obligatorios. El recibo liga
   cambios y evidencia al candidato final y distingue `COMPLETE`, `PARTIAL` y
   `BLOCKED`.
3. **La autoridad sólo se estrecha.** Es la intersección entre paquete,
   autorización del principal y frontera efectiva del runtime. Fugaz no hace
   commit, push, despliegue, destrucción ni acciones externas salvo concesión
   explícita y exacta.
4. **Steipete sigue siendo el integrador.** No se delegan intención borrosa,
   arquitectura, dependencias, schema, boundaries, producto, taste ni cierre
   integrado.
5. **El adaptador Codex usa aislamiento.** `agent_type=fugaz` debe combinarse
   con `fork_turns="none"` o aislamiento equivalente. La herencia completa
   conserva el tipo padre y hace que Codex rechace el custom agent antes de
   crear el hijo.
6. **Calidad no se codifica como nombre de modelo.** Se expresa mediante
   propiedad, aceptación, blast radius, autocorrección, evidencia y límites.
   El modelo/esfuerzo efectivo debe verificarse en cada runtime.
7. **Publicación Fleet selectiva.** Se descartó empujar `main`: estaba dos
   commits por delante de `origin/main` antes del cambio. Se publicó una rama
   limpia basada en `origin/main` que contiene sólo el blueprint de esta
   entrega.

Alternativas descartadas: una skill sin identidad delegada, un agente
autónomo persistente, delegación recursiva, hardcodear un modelo, aceptar
paquetes incompletos por inferencia, usar una suite verde como sustituto de
integración y forzar la publicación de `main` con historial ajeno.

## Artefactos y propósito

| Ruta | Estado | Propósito |
|---|---|---|
| `artefactos/agentes/dev/fugaz.md` | creado | fuente canónica Fugaz v2.0.1 |
| `artefactos/agentes/dev/steipete.md` | modificado | adaptador e integración responsable v1.2.1 |
| `tests/test_fugaz.py` | creado | contrato estructural y semántico mínimo de ambos agentes |
| `HANDOFF.md` | reemplazado | continuidad única de esta entrega |
| `_archivo/HANDOFF-2026-07-31-revision-sintetica-hodom-hsc.md` | archivado, gitignored | continuidad anterior preservada |
| `/home/felix/.codex/agents/fugaz.toml` | instalado | realización Codex de Fugaz |
| `/home/felix/.codex/agents/steipete.toml` | actualizado | realización Codex de Steipete |
| `/home/felix/.agents/skills/steipete/SKILL.md` | actualizado | proyección skill Codex declarada por KORA |
| `/home/felix/.claude/agents/steipete.md` | actualizado | proyección Claude Code |
| `/home/felix/.config/opencode/agents/steipete.md` | actualizado | proyección OpenCode |
| `/home/felix/openclaw-fleet/blueprints/steipete/{AGENTS,SOUL}.md` | actualizado | blueprint OpenClaw |
| `/home/felix/.openclaw/workspaces/steipete/` | materializado | runtime gestionado de Steipete |

El skill Fugaz legado quedó fuera de la superficie activa en
`/home/felix/_archive/codex-skills/fugaz-legacy-20260801T204112Z`. Los respaldos
preoperación y precorrección viven bajo `/home/felix/backups/kora-runtime/`; el
respaldo previo a materializar OpenClaw está en
`/home/felix/backups/openclaw-managed/steipete-managed-pre-1.2.1-20260801T215133Z.tar.gz`.
No se guardaron secretos ni datos personales en los artefactos canónicos.

## Evidencia de comportamiento

Canario positivo Codex:

- cadena observada `root → steipete → fugaz`;
- una única instancia Fugaz;
- cierre `COMPLETE` con aceptación `PASS`;
- un único archivo dentro de `owned_scope` modificado;
- `HEAD` preservado y cero rechazos de invocación.

Canarios negativos Codex:

- paquete sin `authority` → `BLOCKED / malformed-packet`, sin escritura;
- `candidate` falso → `BLOCKED / candidate-mismatch`, sin escritura;
- ambos corrieron como custom agents aislados y el árbol quedó byte-idéntico.

Estos canarios prueban observables puntuales del adaptador; no prueban
determinismo universal, least privilege de herramientas built-in, safety
general, calidad humana, taste ni rendimiento del modelo. El harness negativo
consumió 914.912 tokens de entrada, 853.760 cacheados: es costo end-to-end del
harness y no una medición aislada de eficiencia de Fugaz.

## Comprobaciones ejecutadas

```text
python3 kora.py velar --estricto                         13/13 PASS
python3 -m unittest discover -s tests                   322/322 PASS
paridad urn:dev:artefacto:fugaz                         1 fiel; 0 drift
paridad urn:dev:artefacto:steipete                      5 fiel; 0 drift
git diff --check                                        PASS
OpenClaw verify-repo.sh estático                        28 PASS; 1 SKIP
materialize-workspace.sh steipete                       PASS
materialize-workspace.sh --check steipete               PASS
rama Fleet limpia: materialización + check en destino   PASS
```

`verify-repo.sh --live` de OpenClaw terminó con 44 `PASS`, 4 `FAIL` y 2
`WARN`. La materialización y paridad KORA pasaron. Fallaron salud global,
runtime de memoria, búsqueda de memoria y docs upstream; además hubo avisos de
frescura/e2e de memoria. No se atribuyen a Fugaz ni se presentan como
preexistentes en todos los casos: sólo se confirma que son globales y quedan
fuera del cambio acotado. Borrar colas, reindexar agentes o sincronizar docs
sin diagnóstico habría ampliado alcance y riesgo.

Una comprobación de la rama Fleet limpia contra el runtime vivo produjo un
falso drift de manifiesto: el materializador incluye modos POSIX del checkout,
y el worktree limpio nació `0600` mientras el checkout operativo usa `0664`
salvo una referencia `0600`. El contenido Git y la lista de archivos eran
idénticos. Materializar y verificar esa rama en un destino temporal propio
pasó; el temporal fue enviado a la papelera. Esta dependencia de permisos del
checkout queda como limitación conocida del materializador.

## Git y publicación

KORA `master`:

- implementación: `7a9ac32a77c60e63ab358d6d05b9e67662440c23`
  (`feat(agent): add delegated Fugaz executor`);
- este handoff se confirma como unidad documental separada; su hash se obtiene
  del `git log` vivo para evitar una referencia circular dentro del propio
  commit;
- `AGENTS.md` permanece modificado y fuera de staging por ser trabajo ajeno.

OpenClaw Fleet:

- commit local sobre `main`: `6cb7e97ea2e5ffeb830ed7c5fdbdba3e10e63fc3`;
- commit limpio publicado: `5faa01ab4166326ddac8bc8081cd1c5a2f521418`
  (`chore(blueprint): update Steipete delegation contract`);
- rama remota: `origin/codex/steipete-fugaz-20260801`, paridad local↔tracking
  `0/0` confirmada;
- `main` local conserva dos commits anteriores más el commit local de esta
  sesión y no fue empujada;
- `AGENTS.md` permanece modificado y excluido por ser trabajo ajeno.

## Riesgos y límites vigentes

- La paridad material demuestra correspondencia de fuente, emisión e
  instalación; no demuestra conducta, composición formal ni autoridad
  efectiva.
- Codex no ofrece una allowlist exacta de herramientas built-in para este
  custom agent. El task packet es un control contractual, no un sandbox nuevo.
- La selección del modelo y esfuerzo no está fijada por el artefacto. Debe
  observarse al invocar; no se afirma que un nombre de modelo solicitado esté
  disponible o activo.
- El canario es evidencia localizada, no una evaluación estadística de calidad,
  latencia, costo o regresión sobre tareas diversas.
- Los fallos globales de Fleet y la sensibilidad del manifiesto a modos POSIX
  siguen abiertos.

## Siguiente acción recomendada

Integrar mediante revisión la rama
`codex/steipete-fugaz-20260801` sobre un `openclaw-fleet/main` limpio, sin
arrastrar ni perder los dos commits locales anteriores. Después, en una tarea
separada y con diagnóstico propio, resolver los cuatro fallos live globales y
evaluar si el materializador debe normalizar modos desde Git o declarar una
política de permisos reproducible. Para evolucionar Fugaz, la siguiente mejora
de valor es una matriz pequeña de evals representativos ligada a costo,
latencia, scope compliance y calidad integrada; no ampliar primero su prompt.
