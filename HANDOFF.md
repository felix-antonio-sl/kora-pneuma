# Handoff vigente — 2026-08-02 — Steipete delega ejecución a Fugaz

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, las instalaciones runtime ni el estado vivo del
> host. Los hashes y resultados siguientes sólo describen el candidato exacto
> evaluado.

## Objetivo y resultado

Se diseñó y realizó el ejecutor al que Steipete puede delegar tareas de código:
`urn:dev:artefacto:fugaz` v2.0.1. Fugaz es un subagente Codex efímero,
minimalista y estricto: recibe una tarea cerrada, implementa el menor cambio
completo dentro de propiedad y autoridad explícitas, verifica hasta cierre y
devuelve un recibo tipado. Steipete v1.2.2 conserva intención, arquitectura,
topología, integración y juicio final.

Cada delegación Codex abre una sesión o `agent thread` nuevo, aislado y
efímero. La sesión principal de Steipete es la central única que crea paquetes,
asigna propiedad, decide secuencia o paralelismo, espera recibos e integra. La
topología es de un nivel: los Fugaz no se coordinan lateralmente ni delegan. El
contrato no nombra, recomienda ni exige modelos o niveles de razonamiento; esa
selección pertenece al runtime.

El resultado está completo en la fuente KORA y en los runtimes declarados. La
proyección actual de Steipete está en paridad en Claude Code, Codex, OpenCode y
OpenClaw. La rama limpia del blueprint OpenClaw fue actualizada y publicada;
no se publicó `openclaw-fleet/main` porque ya contenía historial local no
destinado a esa publicación selectiva.

## Alcance cerrado

Incluido:

- migración `migrar-o-omitir` de la identidad histórica Fugaz a la ontología
  vigente de pneuma;
- contrato observable de entrada, salida, errores, autoridad y cierre;
- adaptador Steipete → Fugaz para Codex;
- sesiones Fugaz nuevas y efímeras gobernadas desde una central Steipete de
  dirección e integración;
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
6. **La central es la sesión principal de Steipete.** Cada paquete abre una
   sesión hija nueva, aislada y efímera. Steipete gobierna su ciclo y realiza
   el join; los Fugaz no se coordinan entre sí ni crean descendencia. Es una
   topología runtime de un nivel, no una reclasificación a arnés orquestador o
   plataforma.
7. **Calidad no se codifica como nombre de modelo.** Se expresa mediante
   propiedad, aceptación, blast radius, autocorrección, evidencia y límites.
   El modelo/esfuerzo efectivo debe verificarse en cada runtime, pero ningún
   nombre específico forma parte del contrato.
8. **Publicación Fleet selectiva.** Se descartó empujar `main`: al iniciar la
   entrega original ya estaba dos commits por delante de `origin/main`. Se
   publicó una rama limpia basada en `origin/main` que contiene sólo el
   blueprint de esta entrega y sus correcciones posteriores.

Alternativas descartadas: una skill sin identidad delegada, un agente
autónomo persistente, delegación recursiva, hardcodear un modelo, aceptar
paquetes incompletos por inferencia, usar una suite verde como sustituto de
integración y forzar la publicación de `main` con historial ajeno.

## Artefactos y propósito

| Ruta | Estado | Propósito |
|---|---|---|
| `artefactos/agentes/dev/fugaz.md` | creado | fuente canónica Fugaz v2.0.1 |
| `artefactos/agentes/dev/steipete.md` | modificado | central de sesiones e integración responsable v1.2.2 |
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
| `/home/felix/.codex/memories/extensions/ad_hoc/notes/20260802T074054+0200-steipete-central-sessions-model-neutral.md` | creado | aprendizaje durable, factual y referenciado |

El skill Fugaz legado quedó fuera de la superficie activa en
`/home/felix/_archive/codex-skills/fugaz-legacy-20260801T204112Z`. Los respaldos
preoperación y precorrección viven bajo `/home/felix/backups/kora-runtime/`; el
respaldo previo a materializar OpenClaw está en
`/home/felix/backups/openclaw-managed/steipete-managed-pre-1.2.1-20260801T215133Z.tar.gz`.
Antes de instalar Steipete v1.2.2 se crearon además los respaldos privados
`kora-runtime-steipete-1.2.1-20260802T072850+0200.tar.gz`
(`sha256:50c3080c5fcb3c3eef96cfc69a0d8987f920a58bce4a123178e0f66660f7f817`)
y `openclaw-blueprint-steipete-1.2.1-20260802T072850+0200.tar.gz`
(`sha256:73f73f3fdf11abc8616a3292b47f316b03d3af49f85ef54e0f16245c435e0ec8`)
en `/home/felix/backups/kora-runtime/`, ambos modo
`0600`.
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
scan de nombres/configuración de modelos                 PASS; 0 coincidencias
```

`verify-repo.sh --live` de OpenClaw terminó con 43 `PASS`, 5 `FAIL` y 2
`WARN`. Pasaron la materialización, la búsqueda vectorial, la memoria activa y
la paridad KORA. Fallaron `live-drift`, `plugin-supply-chain`,
`openclaw-health`, `memory-runtime` y `docs-upstream-live`; hubo avisos de
frescura e2e de memoria. No se atribuyen a Fugaz ni se presentan como
preexistentes en todos los casos: sólo se confirma que pertenecen al estado
global vivo y quedan fuera del cambio acotado. Reescribir configuración viva,
retirar paquetes, borrar colas, reindexar agentes o sincronizar docs sin un
diagnóstico separado habría ampliado alcance y riesgo.

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
- aclaración de topología y neutralidad de modelo:
  `9238c84e6401124a1e10f353dd5f9089747a8453`
  (`fix(agent): centralize Steipete Fugaz sessions`);
- este handoff se confirma como unidad documental separada; su hash se obtiene
  del `git log` vivo para evitar una referencia circular dentro del propio
  commit;
- `AGENTS.md`, el subárbol `artefactos/skills/dev/scaffold-repo/` y los
  conocimientos no trackeados observados permanecen fuera de staging por ser
  trabajo ajeno o concurrente.

OpenClaw Fleet:

- commit local sobre `main`: `6cb7e97ea2e5ffeb830ed7c5fdbdba3e10e63fc3`;
- commit limpio publicado: `5faa01ab4166326ddac8bc8081cd1c5a2f521418`
  (`chore(blueprint): update Steipete delegation contract`);
- aclaración local sobre `main`:
  `57b77cd89dc3e58f60b98d2f0b3f06ef50d2bb79`;
- aclaración limpia publicada:
  `38273b72429dca340d4332a38d14c7c76950ec0f`
  (`chore(blueprint): centralize Steipete Fugaz sessions`);
- rama remota: `origin/codex/steipete-fugaz-20260801`, paridad local↔tracking
  `0/0` confirmada;
- `main` local queda cuatro commits por delante de `origin/main` y no fue
  empujada;
- `AGENTS.md` y los cambios de tipo en `docs/fleet-canon-policy.md` y
  `docs/handoff-policy.md` permanecen excluidos por ser trabajo ajeno.

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
arrastrar ni perder el historial local pendiente. Después, en una tarea
separada y con diagnóstico propio, resolver los cinco fallos live globales y
evaluar si el materializador debe normalizar modos desde Git o declarar una
política de permisos reproducible. Para evolucionar Fugaz, la siguiente mejora
de valor es una matriz pequeña de evals representativos ligada a costo,
latencia, scope compliance y calidad integrada; no ampliar primero su prompt.

---

## Cierre de auditoría de fuentes del host — 2026-08-03

Esta sección registra el frente de auditoría y consolidación documental. Se
añade sin absorber los cambios concurrentes de skills descritos arriba.

### Objetivo, alcance y resultado

Se revisaron fuentes candidatas del host para decidir entre koraficar,
conservar externamente, archivar o descartar. El criterio confirmado quedó
publicado como `urn:kora:kb:frontera-fuentes-tecnicas`: KORA es la fuente única
del conocimiento curado; los formatos cuya semántica depende de OWL/SKOS, XML,
schemas o datos raw permanecen externos; un consumidor real usa symlink; y la
ausencia de referencias no autoriza borrar.

Resultado material:

- 96 conocimientos incorporados a `artefactos/conocimiento/`: 11 publicados,
  84 GN en borrador y el tutorial OPCloud en borrador;
- nueve archivos externos reversibles con manifiestos SHA-256 completos para
  210 archivos de contenido;
- siete symlinks consumidores vivos y resolubles: cinco en OpenClaw Fleet, uno
  en Ñuble AI y el directorio sanitario ya existente de `hd-dt`;
- Fleet valida symlinks de fuente restringidos a archivos regulares bajo
  `KORA/artefactos` y los materializa como archivos runtime regulares;
- KORA y Ñuble fueron publicados en sus ramas principales; Fleet se publicó
  selectivamente desde una rama limpia.

No se eliminó ninguna fuente. No hubo despliegue ni materialización sobre
runtime vivo. La validez formal no se presenta como aprobación semántica,
institucional, clínica o productiva.

### Decisiones y alternativas descartadas

1. **Una fuente KORA por conocimiento curado.** Se descartaron copias activas
   iguales en varios repositorios.
2. **Conservar semántica técnica externa.** No se convirtieron
   indiscriminadamente ontologías, catálogos, schemas ni datos raw a Markdown.
3. **Archivar antes que borrar.** `DESCARTAR` exige redundancia u obsolescencia
   completa y autoridad explícita; no se ejerció en este trabajo.
4. **Symlink sólo para un consumidor físico.** Los enlaces OPM se hicieron
   relativos. Fleet rechaza enlaces rotos, directorios y destinos fuera de
   KORA, y el runtime recibe archivos regulares.
5. **Ingestión no equivale a aceptación semántica.** Los 84 documentos GN no
   se promovieron en bloque; OPCloud sigue siendo evidencia pedagógica, no
   canon OPM.
6. **Publicar primero la fuente.** KORA se publicó antes de sus consumidores.
7. **No empujar Fleet `main`.** Esa rama contenía cinco commits anteriores al
   cambio y acumuló modificaciones concurrentes; se publicó sólo el delta
   propio desde `origin/main`.

### Artefactos y propósito

| Ruta | Propósito |
|---|---|
| `artefactos/conocimiento/dev/nuble-plan-ia-2026.md` | fuente KORA del plan regional |
| `artefactos/conocimiento/fxsl/information-system-usage-theory-alter.md` | koraficación acotada de ISUT |
| `artefactos/conocimiento/fxsl/{metodologia-modelamiento-opm,opm-iso-19450,opm-opl-es}.md` | fuentes OPM consumidas por Mente Omega |
| `artefactos/conocimiento/fxsl/opcloud-tutorial-videos.md` | evidencia tutorial en borrador |
| `artefactos/conocimiento/kora/frontera-fuentes-tecnicas.md` | criterio curatorial publicado |
| `artefactos/conocimiento/openclaw-fleet/{fleet-canon-policy,handoff-policy}.md` | políticas Fleet canónicas |
| `artefactos/conocimiento/salud/{hsc-cartera-servicios-2024,minsal-decreto-exento-74-2024-mcc,minsal-rem-2026}.md` | fuentes sanitarias trazables |
| `artefactos/conocimiento/gn/*.md` | 84 fuentes GN migradas como borrador |
| `/home/felix/openclaw-fleet/blueprints/mente-omega/{AGENTS,SOUL}.md` | declara la capacidad KORA consumida |
| `/home/felix/openclaw-fleet/blueprints/mente-omega/skills/opm-modeler/references/*.md` | tres consumidores OPM relativos |
| `/home/felix/openclaw-fleet/docs/{fleet-canon-policy,handoff-policy}.md` | dos consumidores de políticas KORA |
| `/home/felix/openclaw-fleet/scripts/{materialize-workspace,verify-repo}.sh` | aplica y verifica la frontera KORA |
| `/home/felix/openclaw-fleet/tests/{test-materialize-workspace,test-verify-repo}.sh` | regresiones de symlinks KORA |
| `/home/felix/projects/nuble_ai_oc/PLAN_IA_NUBLE_2026.md` | consumidor del plan KORA |
| `/home/felix/kora-external-sources/_archivo/*/sha256-manifest.txt` | nueve recibos de contenido archivado |
| `/home/felix/.codex/memories/extensions/ad_hoc/notes/20260803T022819Z-kora-host-audit-closeout.md` | aprendizajes durables y pendientes |
| `HANDOFF.md` | continuidad única; no se creó un handoff paralelo |

El inventario Salubrista registra seis fuentes perdidas desde un working tree
no versionado antes de esta auditoría. No fueron recuperadas y no se afirma que
estén archivadas o sean restaurables.

### Comprobaciones

```text
KORA velar --estricto                                    13/13 PASS
KORA unittest en `origin/master` limpio                  322/322 PASS
KORA unittest en working tree concurrente                338/338 PASS informativo
GN: fuente, SHA declarado y cuerpo normalizado            84/84 PASS
archivos externos: sha256sum --check           9/9; 210 entradas PASS
scan de claves privadas/tokens de proveedor              0 hallazgos
Fleet test-materialize-workspace.sh                      28/28 PASS
Fleet test-verify-repo.sh                                74/74 PASS
Fleet materialización + check en destino temporal        PASS
Fleet symlinks de fuente KORA                              3/3 PASS
Ñuble blob d404f81 vs cuerpo KORA             SHA-256 idéntico PASS
symlinks consumidores del host                             7/7 PASS
git diff --check en cambios propios                        PASS
```

El último `verify-repo.sh --live` del candidato Fleet limpio terminó
`40 PASS / 10 FAIL / 0 WARN / 0 SKIP`. Fallaron `live-drift`,
`runtime-materialization`, `openclaw-health`, `memory-runtime`,
`memory-search`, `active-memory-e2e`, `docs-upstream-live`, `docs-web-live`,
`kora-velar` y `kora-parity`. Los dos últimos observaron una ventana de cambios
concurrentes; el `velar` directo posterior pasó. No se mutó runtime para forzar
verde.

### Git y publicación

KORA `master`:

- `dda9b132f9667b5e75e3845effb41667557fa098`
  `feat(knowledge): consolidate canonical host sources`;
- `f29d9b68ef491439a1557844834f2ad94062e2e4`
  `feat(knowledge): stage audited GN corpus`;
- `46a4d137c26408a4ce5f0e4af4d77b38910386f2`
  `docs(knowledge): publish technical source boundary`;
- el hash del commit documental se obtiene del `git log` vivo para evitar una
  referencia circular.

OpenClaw Fleet:

- commits equivalentes locales sobre `main`:
  `f264a3d54c94e144d3fe8aecebdd135f0edc5d87` y
  `6dce01b76e5465c54095284ed2d4bf81c7c860cc`;
- commits limpios publicados:
  `768b9f64ed9d5e146b4ea997d37039df33b84410` y
  `1e39b451d1860c1835aa4282b829409d14e91608`;
- rama remota `origin/codex/kora-consumers-20260803`, paridad confirmada;
- `main` no fue empujada y conserva historial/cambios concurrentes ajenos.

Ñuble AI `master`:

- `9d7f152bd0b7b3c242d8824c3ddb693f901e8ba8`
  `docs: consume canonical KORA plan`, confirmado en `origin/master`.

### Riesgos, pendientes y siguiente acción

- Permanecen 85 conocimientos en borrador: 84 GN y OPCloud. Su forma es válida;
  su promoción semántica no está demostrada en bloque.
- Las seis fuentes Salubrista perdidas requieren otra copia verificable.
- Los archivos externos y manifiestos son locales y no están publicados en
  Git; dependen de conservar esa zona del host.
- La rama Fleet publicada no fue integrada ni desplegada; el runtime vivo
  conserva drift y fallos de memoria, salud y documentación.
- KORA y Fleet mantienen modificaciones concurrentes no incluidas en estos
  commits. La limpieza se afirma sólo para los commits y ramas exactos.

Siguiente acción recomendada: revisar e integrar
`codex/kora-consumers-20260803` sobre un Fleet `main` limpio; después,
materializar en una operación runtime autorizada y repetir el gate live. En un
frente documental separado, revisar los 84 borradores GN por lotes pequeños y
promover únicamente los que demuestren fuente, vigencia y fidelidad.
