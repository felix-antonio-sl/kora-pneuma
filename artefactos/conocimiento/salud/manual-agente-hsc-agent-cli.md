---
urn: urn:salud:kb:manual-agente-hsc-agent-cli
nombre: manual-agente-hsc-agent-cli
version: 1.0.15
estado: publicado
descripcion: "Manual operativo para agentes AI que consumen hsc-agent-cli, la vitrina clinica del Hospital de San Carlos: comandos cerrados, contrato JSON beta-3, handles identity-safe, integridad factual, recetas por contexto y limites doctrinales."
fuente: "Autoria de novo 2026-06-22 sobre hsc-agent-cli@bb2a4ec (CLAUDE.md, contrato beta-1, binario v1.0.14) y la ayuda viva del binario. Sin herencia del manual humano previo (capacitacion-agente). No migrado de la bestia; sin sha256 externo. Actualizado 2026-06-23 (v1.0.1): observabilidad aditiva del envelope (cache_status, error_detail.affected_systems/outage_kind, health latency_ms/checked_at, truncated_keys) y receta de epicrisis via hcc:secundaria, tras deliberacion de panel y spike de viabilidad. Actualizado 2026-06-23 (v1.0.2, TIER 2): bundle multi-handle (kind multi_bundle, producto de sub-envelopes aislados, cota 50) y recommended_batch_handle en find para colapsar el N+1 del censo HODOM. Actualizado 2026-06-24 (v1.0.3, Corte 1): find emite recommended_batch_handles[] particionado por COSTO (~3 min/sub-lote) con estimated_cost_seconds/total, ejecutables en serie; el singular queda como alias del primer sub-lote (retrocompat). Resuelve el timeout del censo atomico (auditoria F2/F3); sobre hsc-agent-cli@4d23e85. Actualizado 2026-06-24 (v1.0.4, Corte 2): gap_kind en cada clinical_gap (confirmed_absence / acquisition_failure / identity_failure / unknown) para distinguir ausencia-confirmada de fallo-de-adquisicion sin reclasificar a mano (auditoria F6); y find ... --fresh ahora da mensaje honesto (no cachea, --fresh solo en get/bundle) en vez de mentir con 'requiere argumento' (F1); sobre hsc-agent-cli@d2331c8. Actualizado 2026-06-24 (v1.0.5, Cortes 3+4): forma normal canonica de la evolucion (texto=coalesce(historia,evolucion), plan_indicacion=coalesce(plan,indicacion), data_keys del sub-objeto, preservando los crudos; mata el falso 'sin evolucion' del jq contra el campo equivocado; auditoria F5) y procedencia de la ubicacion en handoff_view (ubicacion_source/diagnostico_admin_source en {estado-actual, unavailable}; un hueco no se lee como dato real; auditoria F4); sobre hsc-agent-cli@3b9f28d. Actualizado 2026-06-26 (v1.0.6, Corte 5): bundle ... --stream entrega el lote como NDJSON (una linea type:bundle por sub-envelope conforme cierra, en orden de completitud, + linea terminal type:summary con streamed:true y sin bundles[]); opt-in, aditivo, retrocompat, requiere >=2 handles; mata F3 (el lote atomico perdia todo en timeout). Cierra la auditoria del censo (Cortes 1-5). Agregado el suite de aceptacion scripts/eval-contrato-agente.sh (5 escenarios exigentes del contrato, casos vivos auto-descubiertos); sobre hsc-agent-cli@1f4e608. Actualizado 2026-06-30 (v1.0.7, Corte 6 + sub-cortes 1 y 2 del frente faithful find): el censo SGH se vuelve FIEL en sus dos niveles ortogonales y lo declara en data. (Corte 6) hospitalizacion:sgh:<id>/estado-actual agrega sweep_complete/rooms_unavailable (barrido de pacientes por sala). (Sub-corte 1) agrega enumeration_complete/services_unavailable (enumeracion de salas por servicio), ortogonal al barrido. (Sub-corte 2 / Caso A) propaga los CUATRO campos a find --hospitalizados (functor distinto FetchHospitalizados; la fidelidad no es transitiva, hubo que reaplicar el patron) y marca censo-parcial en recommended_batch_handles[] con recommended_batch_handles_census_incomplete (+ _detail con las dos dimensiones por separado), solo bajo censo parcial (omitido bajo censo fiel = byte-identico). Cuando estado-actual concluye ausencia bajo censo incompleto, el clinical_gap de dominio ingreso sale con gap_kind=acquisition_failure (no confirmed_absence). Semantica honesta: *_complete=true significa 'sin fallo DURO observado', no 'lista realmente completa'; censo parcial es USABLE (advierte, no bloquea); el agente compone sweep_complete && enumeration_complete. Sobre hsc-agent-cli@a7b28b9. Actualizado 2026-07-07 (v1.0.8, fase 1 HODOM fuentes vivas, encargo DT 2026-07-06): scope hodom: (hodom:libro-mayor/<rut> + hodom:programacion/<rut>, kind sheet, source drive) — las planillas Drive manuales de la unidad entran a la vitrina como handles identity-safe via export CSV sin credenciales, con cache de archivo 10 min; composicion automatica en bundle hospitalizacion (items aislados) cuando el episodio es HODOM o el servicio no resuelve (servicio resuelto no-HODOM = salida byte-identica); summary.discrepancies[] con guard temporal (estado_hodom SIN precedence_hint — SGH es tiempo real y el libro arrastra lag de cierre; la regla de precedencia del DT queda consagrada como doctrina de agente en 6.2) y gap candidato en clinical_gaps cuando un activo SGH no tiene fila en libro sano; tab_found/rows_total/rows_empty/rows_unparseable/estado_normalizado como higiene de planilla manual; --fresh bypassa tambien el cache de archivo drive; error_detail con sistema DRIVE y reason header_mismatch (retryable=false). Sobre hsc-agent-cli@4e5f225 (tag v1.1.0). Actualizado 2026-07-08 (v1.0.9, ciclo feedback urgencia): imaging_narrative_fallback ahora tambien top-level en bundle --minimal cuando scanner cae con upstream_unavailable (en --compact el objeto data.orders.* existe siempre, triggered:true ante cualquier error del scanner — asimetria documentada); summary.urgencia gana indicaciones_alta_presentes (bool incondicional; presencia mecanica de registro de alta, NO conclusion de egreso — sirve para componer 'activo en board + alta indicada = probable lag upstream') y lab_sources_with_data (lista incondicional [lis, textuales], vacia posible, sin fusionar fuentes) y examen_fisico_terms_in_evolucion (solo con evolucion present; barrido de terminos EF, pista no conclusion) + gap moderate examen-fisico con suggested_handle /evolucion cuando el EF estructurado esta ausente; indicaciones-alta entra a los subhandles del bundle minimal (items 18→19); flag --last N (1..50, solo con --compact) overridea los recortes last_n (defaults 2/2/3/1 intactos sin flag); recetas nuevas: --with-rut en board, lote por medico, y manejo del truncado del canal del runtime (el CLI siempre emite JSON completo). Registro del ciclo (desidentificado) en docs/ciclo-feedback-urgencia-2026-07-08.md del repo. Sobre hsc-agent-cli@15f8902 (tag v1.2.0). Actualizado 2026-07-11 (v1.0.10, ciclo feedback v2 — carril doctrinal, cero cambios de binario): triaje verificado de los reportes forenses de turno urgencia 2026-07-10 y sesiones hospitalista 2026-07-06/07 ([hsc-agent-cli] docs/triaje-reportes-feedback-2026-07-11.md). Seis piezas de doctrina de agente: (1) receta canonica censo→briefs via recommended_batch_handles[] + --stream con prohibicion explicita de orquestar subagentes paralelos contra SGH (la via existia y el consumidor no la conocia: 0/30 briefs en produccion); (2) disciplina anti-tormenta bajo upstream_unavailable (UN probe de health, backoff, jamas fan-out — 5 consumidores concurrentes observados reintentado contra upstream caido); (3) error_code+state del envelope como señal primaria de flujo (los pipes destruyen $?; exit code queda para scripts/CI); (4) abrir el turno con health (barato, en vivo, latency_ms por sistema); (5) heuristica canonica de ubicaciones UEH (hospitalizado-en-UEH vs en-atencion, doctrina de agente hasta que upstream exponga campo tipificado); (6) refuerzo del lote para el barrido DAU (no N+1 de gets atomicos). Sobre hsc-agent-cli@61c3c31 (v1.2.0 + triaje 2026-07-11). Actualizado 2026-07-11 (v1.0.11, ciclo feedback v2 SHIPPEADO — tag v1.3.0): el encargo hd-dt 2026-07-11 completo entra a la superficie. (1) find --nombre: el NOMBRE es llave de entrada de primera clase — standalone (barre board DAU + censo SGH en paralelo, fallo aislado por fuente, contrato 0/1/N con match_scope y best_current_context por match, warning explicito de universo incompleto cuando una fuente cae o el censo viene parcial; AMBAS fuentes caidas → upstream_unavailable exit 4, jamas ausencia; tokens sin comillas se unen mecanicamente) y componible como filtro --nombre en --board/--urgencia/--hospitalizados; matching normalizado (mayusculas/tildes/enie plegadas, orden libre de tokens). (2) <comando> --help|-h responde envelope beta-1 (kind:help, error_code:null, exit 0) y todo usage_error de flag desconocido trae error_detail.supported_flags[] con la whitelist real. (3) --fields <k1,k2,...> en listados de find: proyeccion de columnas por entry con fields_projected[] declarado. (4) get --limit N ampliado a paciente:ambulatorias-osiris y paciente:recetas-historicas (truncado declarado + honestidad de orden: primeras N filas upstream, no las mas recientes; con flag no toca cache). (5) bundle --handoff --budget-bytes N (4096..1048576, por sub-bundle en lote/stream): recorte mecanico del envelope ya construido con escalera declarada (fases de data → slim a whitelist nucleo → drop por peso), summary y handoff_view NUNCA recortados, perdida en compaction/_compaction/truncated_keys; el presupuesto se mide con la MISMA serializacion que se emite. (6) scope completado en find: enum cerrado {rut, atencion, nombre, board, urgencia, hospitalizados}. Gate del corte: TDD (~60 tests nuevos), review adversarial multi-agente (19 hallazgos confirmados → 9 defectos corregidos PRE-tag, incl. panic de --fields sin criterio y presupuesto que media compacto pero emitia indentado), eval-contrato-agente 5/5 vivo, verificacion viva completa. Sobre hsc-agent-cli@3fd3f90 (tag v1.3.0). Actualizado 2026-07-15 (v1.0.14, contrato beta-3 — tag v3.0.0): migra el consumo a integridad factual con source_issues[] y bundle_integrity; retira decision_safety, clinical_gaps, usable_clinically, aliases recommended_* y precedence_hint; adopta batch_plan.requests[], agent-autonomy-2, --version local, autocorreccion --fresh sin PII, censo HODOM trivalente, identidad ingreso→RUT verificada, Drive fail-closed y evolucion-ultima con procedencia. Sobre hsc-agent-cli@804bb37 (tag v3.0.0). Actualizado 2026-07-16 (v1.0.15, correccion de verdad): `clinical_warning` deja de documentarse como campo vivo del contrato beta-3; `warnings[]`, `source_issues[]` y `bundle_integrity` concentran advertencias e integridad factual. Epicrisis SGH con form=epicrisis es primera clase; form=epi es invalido y HCC secundaria se consulta como alternativa factual solo si el documento SGH valido resulta vacio."
autor: FS
creado: 2026-06-22
lang: es
tags: [hsc-agent-cli, vitrina-clinica, agentes-ai, contrato-json, handles, identity-safe]
cita: [urn:salud:kb:hodom-direccion-tecnica]
familia: nota
---

# Manual operativo para agentes AI — hsc-agent-cli

Edición `1.0.15`, sincronizada el 2026-07-16 con la fuente viva de
`hsc-agent-cli` (contrato `beta-3`; base publicada `v3.0.0`) y su guía inline
`agent-autonomy-2`. El flujo estándar es autoritativo en
`<comando> --help`; este manual conserva inventario exhaustivo, caveats de
fuente y doctrina excepcional.

Manual para un **agente AI** (no un humano) que opera `hsc-agent-cli` para
reconstruir la historia contextual de un caso clínico del Hospital de San Carlos.
Estructura recuperable: ve a la sección que necesitas, no lo leas en orden.

## 0. Qué es y qué NO es

`hsc-agent-cli` es una **vitrina**: lee los sistemas clínicos del hospital (DAU
urgencia, SGH hospitalización, LIS laboratorio, HCC APS) y los expone como
**handles direccionables** en **JSON puro por stdout**. Tú recorres la vitrina,
eliges items y compones tu lectura del caso.

| Es | No es |
|---|---|
| Selecciona y presenta datos crudos parseados | No interpreta, resume ni prioriza clínicamente |
| Se hace cargo de infra (login, sesiones, cookies, HTTP, parseo HTML/PDF) | No es una base de datos (stateless + caché) |
| CLI de comandos cerrados, salida JSON estable | No es daemon, servidor ni endpoint de escritura |
| Identity-safe por construcción | No adivina: si un fetcher no existe → `not_implemented_yet` |

**Regla madre:** el sistema **selecciona, presenta y garantiza la
infraestructura**. **La proyección, el resumen, la priorización y la
interpretación clínica son tuyas.** Si esperas que el CLI "te diga qué es
importante", estás usándolo mal.

**Jerarquía de verdad** (si algo aquí contradice la realidad): manda el binario
y sus tests; luego el `CLAUDE.md` del repo (`~/projects/hsc-agent-cli/CLAUDE.md`,
doctrina y contrato público); este manual es la guía de operación subordinada.
Detalle técnico de endpoints upstream: `~/projects/hsc-agent-cli/docs/reference/`.

## 1. Contrato de invocación

```
hsc-agent-cli <comando> [args]
```

Cinco comandos, **conjunto cerrado** (no hay otros; no inventes `init`, `login`,
`session`):

| Comando | Costo | Para qué |
|---|---|---|
| `catalog <rut>` | barato | Listar la vitrina del paciente: qué handles hay |
| `get <handle> [--fresh]` | caro | Materializar el contenido de un handle |
| `bundle <handle> --minimal\|--compact\|--handoff\|--longitudinal` | caro | Componer varios handles de un encuentro en un paquete |
| `bundle <h1> <h2> ... --handoff\|--minimal` | caro | LOTE: producto de bundles en una invocación (colapsa el N+1 del censo); máx. 50. `find` lo particiona por costo en `batch_plan.requests[]` |
| `find <criterio>` | medio | Ubicar paciente/episodio activo antes de pedir handles |
| `health` | barato | Verificar conectividad upstream + versión del binario; reporta por sistema `ok`, `latency_ms` y `checked_at` de esa invocación |

`hsc-agent-cli --version` es un flag raíz local, no un sexto comando. Devuelve
versión, commit, contrato y estado `modified` sin tocar upstream.

**Salida:** SIEMPRE JSON en stdout (incluso los errores). stderr queda
silencioso por defecto. El logging estructurado es opt-in con
`HSC_AGENT_CLI_LOG_LEVEL=debug|info|warn|error` y no incluye identificadores;
**parsea solo stdout**.

**Ayuda embebida:** `hsc-agent-cli <comando> --help` (o `-h` como
primer arg) responde un envelope beta-3 (`kind:"help"`, `error_code:null`,
exit 0) con uso, versión local, flags por scope y puntero a este manual. Y todo `usage_error` de flag
o criterio desconocido trae `error_detail.supported_flags[]` con la whitelist
real del subcomando: **si tanteas un flag, el error te dice cuáles existen**
— no insistas probando variantes.

**Autonomía inline:** cada help agrega `data.agent_guide` versión
`agent-autonomy-2`, con flujo completo, selección de primitive, protocolo por
`state/error_code`, hard stops y playbook del comando (`use_when`, `inspect`,
`next`, `avoid`, `examples`). La ayuda declara
`manual_required_for_standard_flow:false`: úsala como autoridad operacional
del flujo normal. Vuelve a este manual solo para inventario exhaustivo de
handles, caveats de fuente o un caso que `command_playbook.next`,
`error_detail` y `batch_plan` no cubran.

**Exit codes** (contrato para scripts/CI que invocan sin pipe):

| Exit | Significado |
|---|---|
| 0 | ok |
| 2 | `usage_error` (input mal formado) |
| 3 | `patient_not_found` / `identity_mismatch` |
| 4 | `upstream_unavailable` / `not_implemented_yet` |
| 5 | `internal_error` (bug del CLI) |

**Tu señal primaria de flujo es el ENVELOPE, no el exit code.** En el patrón
real de invocación de un agente (pipes: `2>&1 | head`, `| jq`, `| python3 -c`)
`$?` se destruye y el exit code es inobservable. Decide flujo por `error_code` +
`state` (+ `data_keys`) del JSON, que viajan SIEMPRE en stdout, incluso en
error. El exit code sigue siendo contrato estable — pero para scripts que
invocan directo, no para ti.

**Credenciales:** vienen del entorno (`H_DAU_*`, `H_SGH_*`, `H_LAB_*`,
`H_SGH_HOSPITAL_ID`, `H_PROXY_HOST`; para las planillas HODOM,
`H_DRIVE_INGRESOS_ID`/`H_DRIVE_PROGRAMACION_ID` con defaults compilados — no son
secretos y rotan por año) o de `~/.config/hsc-agent-cli/credentials.env`.
No es tu trabajo gestionarlas; si faltan, `health` lo reporta.

## 2. Modelo mental: handles

Un **handle** es la dirección tipada de un item de la vitrina. Lleva la
**identidad del paciente embebida** y es **identity-safe**: toda respuesta
upstream se verifica contra la identidad esperada o se rechaza con
`identity_mismatch`. Tú **compones** handles; no negocias con un envelope
monolítico.

Gramática por scope (subconjunto operativo — universo cerrado completo en el
`CLAUDE.md` del repo, §Universo de handles):

| Scope | Forma | Eje |
|---|---|---|
| `paciente:` | `paciente:identidad:<rut>`, `paciente:timeline/<rut>`, `paciente:lis/<rut>/examenes`, `paciente:dau-previas/<rut>`, `paciente:hospitalizaciones-previas/<rut>`, ... | transversal, longitudinal por RUT |
| `urgencia:dau:` | `urgencia:dau:<atencion_id>` y subhandles `/triage`, `/vitales`, `/anamnesis`, `/hipotesis`, `/diagnosticos`, `/evolucion`, `/observaciones`, `/ordenes/{lab,rayos,scanner,interconsultas}`, `/medicacion`, `/indicaciones-alta`, `/print/pdf`, ... | episodio de urgencia activo |
| `hospitalizacion:sgh:` | `hospitalizacion:sgh:<ingreso_id>` y subhandles `/estado-actual`, `/cabecera`, `/ingreso-servicio`, `/evoluciones`, `/evolucion-ultima`, `/indicaciones-vigentes`, `/recetas`, `/doc/{ingreso,solicitud,epicrisis,consentimiento}`, ... | episodio de hospitalización (`<ingreso_id>`, **nunca** `cp`) |
| `hcc:` | `hcc:{primaria,secundaria}:<rut>/resumen`, `/detalle/<id>`, `/search/<query>` | APS/especialidades vía ESB |

**`catalog` es barato, `get` es caro.** Pide `catalog` para saber qué existe;
pide `get` solo de lo que vas a consumir.

## 3. El sobre JSON `beta-3`

Todos los comandos exponen una base común. Estos son los campos que **debes
leer**:

| Campo | Uso para el agente |
|---|---|
| `ok` | éxito booleano de la operación |
| `handle` | la dirección tipada del item devuelto — confirma sobre qué pediste |
| `contract_version` | versión del contrato (`beta-3`); detecta cambios de shape |
| `state` | `present` (hay dato) · `ausente` (no hay, pero la fuente respondió) · `error` · `no_implementado` |
| `kind` | tipo del item (encounter, timeseries, triage, narrative, document, ...) |
| `source` | sistema fuente (dau, sgh, lab, hcc) |
| `data` | el payload real |
| `data_keys` | **lista ordenada de claves top-level de `data`** — úsala para descubrir el shape sin adivinar |
| `warnings` | avisos mecánicos no fatales; léelos cuando la lista no esté vacía |
| `error_code` / `error_detail` | ver §4 |
| `fetched_at` | timestamp de materialización |
| `cache_status` / `cache_ttl_remaining_seconds` | en `get` y en cada sub-item de `bundle`: `hit`\|`miss` (no existe `stale`) + segundos de TTL restante. Decide `--fresh` con criterio en vez de actuar a ciegas sobre dato viejo. `catalog`/`find`/`health` no cachean en disco → omiten estos campos (siempre en vivo) |

**Descubrimiento de shape:** nunca asumas la forma de `data`. Lee `data_keys` y
navega. Shapes conocidos están en el `CLAUDE.md` del repo (§Shape hints).

## 4. Errores: qué hacer con cada uno

`error_code` es el contrato estable. `error_detail` lo enriquece con
`reason`, `source_system`, `affected_systems[]` (sistemas involucrados en
materializar el handle: HCC es bridge → `[HCC, DAU, SGH]`; compuestos DAU→LIS →
`[DAU, LIS]`; el resto, su fuente única), `retryable`, y a veces
`upstream_status`, `outage_kind` (`transient`|`down`|`unknown` en
`upstream_unavailable`; conservador, default `unknown` para no inducir a
ignorarlo por sobre-reporte), `alternative_handles[]` y `source_limitation`.
Las alternativas son consultas relacionadas sin equivalencia ni orden. No hay
`downtime_estimated` (sería predicción, no hecho).

| `error_code` | Qué significa | Tu acción |
|---|---|---|
| `usage_error` | input mal formado (handle, RUT, flag) | corrige la invocación; no reintentes igual |
| `patient_not_found` | upstream no encuentra al paciente, o atención DAU cerrada | verifica el id/RUT; si la atención cerró, busca vía `find` o handles `paciente:*` |
| `identity_mismatch` | el handle dice RUT R, upstream devolvió R' | **DETENTE.** No uses el dato. Es una falla categorial, no un dato degradado |
| `upstream_unavailable` | red/proxy/login/5xx | mira `outage_kind`: `transient` → reintenta acotado; `down` → no insistas y reporta caída; `unknown` → un reintento acotado y evalúa. `affected_systems[]` indica los sistemas implicados; `alternative_handles[]`, si existe, no elige por ti |
| `not_implemented_yet` | handle válido, fetcher pendiente | no insistas; revisa `error_detail` y el catálogo sin inventar una ruta |
| `internal_error` | bug del CLI | reporta; no es problema de tus datos |

Cuando un handle de scanner/LIS/HCC falla, lee
`error_detail.alternative_handles[]` y `source_limitation`. Son rutas
direccionables independientes del catálogo cerrado, no una recomendación ni
prueba de contenido equivalente.

**Disciplina anti-tormenta bajo `upstream_unavailable` (obligatoria):**

1. **UN solo probe de `health`** para confirmar qué sistema cayó (usa
   `affected_systems[]` del error para saber cuál mirar).
2. **Backoff**: si reintentas (`outage_kind: transient`), espera creciente entre
   intentos, máximo 2 reintentos por handle.
3. **JAMÁS fan-out**: no lances N consumidores/subagentes concurrentes a
   reintentar contra un upstream caído. Cinco consumidores decidiendo solos
   convierten una caída de minutos en una tormenta de reintentos contra el
   proxy (observado en producción 2026-07-06: 5 subagentes × ~5 min contra SGH
   caído). `retryable: true` significa "reintentable", NO "reintenta ya y en
   paralelo".
4. Si la caída persiste, **reporta la caída y sigue con las fuentes vivas**
   (`alternative_handles[]`, handles de otros sistemas): límite declarado
   vale más que reintento infinito.

## 5. Cómo empezar: navega antes de pedir

**Abre el turno/sesión con `health`.** Es barato, siempre en vivo, y reporta por
sistema `ok`, `latency_ms` y `checked_at`: sabes desde el minuto cero qué
fuentes están vivas y cuáles evitar, en vez de descubrir una caída a mitad de
una síntesis con el médico esperando. Si un sistema está caído al abrir, planea
la sesión alrededor (fallbacks del §4) en lugar de tropezar con él N veces.
Lee `beta_ready` para el núcleo requerido y `all_capabilities_ready` para toda
la superficie. Una capacidad opcional degradada mantiene `ok:true`,
`state:present` y exit 0, con `health_status:degraded`; una requerida caída
emite `ok:false`, `state:error`, `health_status:unavailable` y exit 4. HCC
figura en `partially_probed_systems` porque su prueba es configuracional.

No empieces pidiendo handles a ciegas. **Ubica primero** con `find`, que además
te entrega `best_current_context`: un puntero mecánico que enumera rutas
direccionables para el contexto observado, sin orden de preferencia.

```
find --rut <rut>           localiza al paciente y su contexto activo
find --atencion <atencion_id>      localiza por atención DAU
find --nombre "<nombre>"   localiza por NOMBRE: barre board DAU + censo SGH (v1.3.0)
find --board [--with-rut] [--nombre <txt>]
find --urgencia [--categoria C1..C5] [--unidad <txt>] [--especialidad <txt>] [--medico <txt>] [--box <txt>] [--nombre <txt>] [--with-rut]
find --hospitalizados [--establecimiento <id>] [--servicio <alias|id>] [--sala <alias|id>] [--hodom] [--desde YYYY-MM-DD] [--hasta YYYY-MM-DD] [--nombre <txt>]
find ... --fields atencion_id,nombre,rut,categoria   proyección de columnas por entry (solo listados)
```

**El nombre es llave de entrada de primera clase (v1.3.0).** Cuando el médico
te entrega un nombre (el caso más frecuente en turno), NO interrogues por el
RUT ni barras el board con N gets: `find --nombre "<nombre y/o apellidos>"`.
Matching normalizado (mayúsculas/tildes/ñ plegadas, orden libre de tokens:
"perez juan" ≡ "juan perez"); los tokens sin comillas se unen solos. Contrato
0/1/N: 0 matches → `state:ausente` (con warning explícito si una fuente cayó
o el censo vino parcial: **0 matches bajo universo incompleto NO es ausencia
confirmada**); N matches → lista con `match_scope` (`urgencia`|
`hospitalizados`) y `best_current_context` POR match — la elección entre
homónimos es tuya, nunca del CLI. Ambas fuentes caídas → `upstream_unavailable`
(exit 4), no ausencia. Como filtro (`--urgencia --nombre <txt>`) restringe el
listado del scope.

**`--fields` (v1.4.0):** en listados, proyecta cada entry a las columnas que
pides (`fields_projected[]` lo declara). `item_path` dice dónde iterar;
`fields_coverage` cuenta presencia por columna y
`fields_missing_all_entries` denuncia typos/campos globalmente ausentes. Si
el listado está vacío, `fields_coverage_status:not_observable_empty_list`
impide inventar un schema ausente. Úsalo cuando tu canal trunca: el
board completo pesa ~90 KB; proyectado a `aid,nombre,rut,categoria,box` cabe
en cualquier contexto.

- `best_current_context` aparece en `find --rut`, `--atencion`, `--urgencia`,
  `--board` y por entry en `--hospitalizados`. Si hay DAU activo **e** ingreso
  activo a la vez, expone ambos + `conflict_note`.
- `find --urgencia --with-rut` enriquece cada entry con `rut` canónico
  (FetchAtencion paralelo, más lento); default off por latencia.
- `tiempo_minutos` es un int siempre presente (parseo de "18h10m"→1090).
- `find --hospitalizados --hodom` es alias mecánico de `--servicio hodom`.

## 6. Recetas por contexto

### 6.1 Paciente en urgencia (DAU activo)

```
find --nombre "<nombre que te dio el médico>"   # ← ABRE POR AQUÍ si te dan nombre
find --urgencia --categoria C2
find --board --with-rut                        # board CON rut por entry (evita el doble viaje al bundle longitudinal)
get urgencia:dau:<atencion_id>/estado-actual --fresh
bundle urgencia:dau:<atencion_id> --minimal           # paquete operacional, sin resumen
bundle urgencia:dau:<atencion_id> --minimal --compact  # snapshot compacto para turno conversacional
bundle urgencia:dau:<atencion_id> --minimal --compact --last 8   # compact con más profundidad (recortes last_n a 8)
bundle paciente:<rut> --longitudinal           # historia contextual mecánica
```

Para reconstruir el episodio: lee `urgencia:dau:<atencion_id>/anamnesis`, `/hipotesis`
(narrativa) vs `/diagnosticos` (CIE-10 codificado), `/vitales`, `/evolucion`,
`/observaciones` (canónico para informes TAC copiados y resultados pegados),
`/ordenes/*`, `/medicacion`, `/indicaciones-alta`, `/print/pdf`.

**`--with-rut` existe y evita el doble viaje**: `find --board --with-rut` y
`find --urgencia --with-rut` enriquecen cada entry con el RUT canónico (default
off por latencia). Úsalo cuando vayas a pedir bundles longitudinales del board.

**Turno del médico (lote mecánico, NO pidas un "resumen de turno")**: el CLI no
resume ni prioriza — pero el lote compone todo lo que necesitas:
`find --urgencia --medico "<nombre>" --with-rut` → ejecuta
`batch_plan.requests[].command_args` en el orden secuencial declarado
(sub-lotes `--minimal --compact`, agregables con `--last N` para más
profundidad). Cada sub-envelope trae vitales, disposición
documental y pendientes mecánicos; la síntesis del turno es tuya.

**Barrido del board completo = lote, NUNCA N+1 de gets.** Si necesitas
reconstruir contexto de muchos episodios del board (p. ej. armar un índice
nombre→RUT, revisar todos los C2), ejecuta todas las requests de `batch_plan`
que `find --urgencia`/`--board` ya emite. NO hagas un `get` atómico por
episodio (`/triage`, `/estado-actual` × N): es el mismo anti-patrón N+1 que el
lote existe para matar (observado en producción: 28×2 gets para reconstruir un
índice que el board ya traía).

**«Hospitalizados en UEH» vs «en atención» (heurística canónica de agente).**
El board DAU no tipifica ese estado. Hasta que upstream exponga un campo
tipificado, la heurística compartida es por la ubicación de la entry:
`Cama`, `Camilla`, `Pasillo`, `Cuidados Básicos` ≈ hospitalizado en UEH
esperando destino; `Rea`/box de atención ≈ atención activa. Es **heurística de
agente, no contrato del CLI**: decláralo como tal al reportar, y usa SIEMPRE
esta (no inventes la tuya) — que todos los agentes filtren igual vale más que
la precisión marginal de una variante propia.

**Señales factuales de `summary.urgencia`:** estados de cada subhandle,
`indicaciones_alta_presentes`, `lab_sources_with_data` y
`medicacion_non_medication_count`. Son índices de adquisición: una lista vacía
o un booleano no autorizan una conclusión clínica. Las fuentes LIS y textuales
mantienen su procedencia; el agente decide cómo integrarlas.

### 6.2 Paciente hospitalizado / HODOM (ingreso SGH activo)

```
find --hospitalizados --establecimiento 2 --servicio medicina
find --hospitalizados --hodom                  # censo HODOM HSC
get hospitalizacion:sgh:<ingreso_id>/estado-actual --fresh
bundle hospitalizacion:sgh:<ingreso_id> --minimal
bundle hospitalizacion:sgh:<ingreso_id> --handoff   # vista compacta para handoff/turno
bundle hospitalizacion:sgh:<ingreso_id> --handoff --budget-bytes 16384
                                       # presupuesto best-effort del envelope:
                                       # lee compaction.budget_satisfied/over_budget_bytes
bundle paciente:<rut> --longitudinal
```

HODOM **no es un comando nuevo**: se expresa con `find --hospitalizados --hodom`,
los handles SGH existentes, el bundle `--handoff` y el timeline longitudinal.
Los handles `hospitalizacion:sgh:*` usan SIEMPRE `ingreso_id`, **no `cp`**
(`find --hospitalizados` trae `id_semantics` con `next_handle_pattern`).
La presencia censal HODOM es trivalente: `observed_present`,
`observed_absent` o `unavailable`. `/evolucion-ultima` consulta el listing de
evoluciones si el puntero censal falla, proviene de censo parcial o es inválido;
declara `fallback_source` como procedencia técnica y conserva los errores
tipados. Solo una consulta exitosa sin contenido se vuelve `ausente`.

**«Censo + brief de cada paciente» (el pedido más frecuente del operador): esta
ES la vía de primera clase. No la compongas a mano, no orquestes subagentes.**
El intento de paralelizar bundles SGH con subagentes fracasó en producción
2026-07-06/07 (0/30 briefs entregados: desborde de contexto de los consumidores
+ tormenta contra SGH caído). El flujo correcto es: `find` → ejecutar sus
`batch_plan.requests[].command_args` en serie, con `--stream` para ir componiendo el
brief de cada paciente apenas su bundle cierra. El brief HODOM por paciente
sale de cada sub-envelope, que ya compone SGH + `hodom:libro-mayor` +
`hodom:programacion` (§fuentes vivas, abajo).

**Censo completo en una operación (lotes por costo).** Para pasar la visita a todo
el censo sin invocar el bundle N veces (un proceso/login por paciente), `find` te
entrega el censo **ya particionado por costo** en `batch_plan.requests[]`: una
lista de sub-lotes, cada uno con `command_args[]` como argv estructurado exacto,
su `count` y su
`estimated_cost_seconds`. No memorices reglas — `find` ya
eligió el modo de cada scope (hospitalizados → `--handoff`, urgencia → `--minimal
--compact`) y el tamaño de cada sub-lote (apunta a ~3 min para no time-outear).

```
find --hospitalizados --hodom                  # mira batch_plan.requests[]
# ejecuta CADA sub-lote EN SERIE; p. ej. el primero:
bundle hospitalizacion:sgh:<id1> hospitalizacion:sgh:<id2> hospitalizacion:sgh:<id3> --handoff
```

**Ejecútalos en serie, no todos de golpe.** `batch_plan.total_estimated_cost_seconds`
te dice el costo del censo completo (p. ej. ~2100 s para 35 pacientes): es lo que
costaría en total, no de una vez. Cada sub-lote es ~3 min y devuelve su propio
`kind: multi_bundle`. No subas la concurrencia para "acelerar": SGH legacy serializa
(~62 s/paciente fresh), más paralelismo de cliente lo satura, no lo acelera.

No existen aliases singulares o plurales `recommended_*`: `batch_plan` es la
única autoridad del lote. Cada sub-lote es `kind: multi_bundle`, un **producto**
con un sub-envelope por ingreso en `bundles[]`; cada componente cierra su
identidad. `summary.identity_mismatch_handles[]` nombra solo los componentes con
mismatch y no convierte el resto en clínicamente seguro.

**Entrega incremental con `--stream` (NDJSON).** Agrega `--stream` a cualquier
sub-lote (`bundle <h1> <h2> ... --handoff --stream`) para recibir cada bundle
**apenas cierra**, en vez de esperar a que todos terminen. La salida deja de ser un
único objeto y pasa a ser **una línea JSON por sub-envelope**, en orden de
**completitud** (no de petición):

```
{"type":"bundle","index":1,"handle":"hospitalizacion:sgh:<id>","envelope":{…}}
{"type":"bundle","index":0,"handle":"hospitalizacion:sgh:<id>","envelope":{…}}
{"type":"summary","streamed":true,"summary":{…}}   ← línea terminal, SIEMPRE la última
```

Cada línea `type:bundle` lleva el sub-envelope **intacto** en `envelope` (idéntico al
bundle single) y su `index` (el orden de petición, para que reordenes si lo
necesitas). La línea final `type:summary` trae el mismo `summary` mecánico del lote,
**sin** `bundles[]` (ya los recibiste). Es opt-in, retrocompat y requiere ≥2 handles
(con 1 → `usage_error`). Úsalo cuando un sub-lote es lento (SGH legacy ~62 s/paciente)
y quieras ir trabajando cada paciente conforme llega, sin que un timeout del último te
haga perder los ya computados. Desde v1.4.0 la primera emisión tampoco espera
que terminen N-3 componentes cuando el lote supera tres handles. Procesa cada
línea NDJSON por separado.

**Fidelidad del censo (`sweep_complete` + `enumeration_complete`).** El censo SGH se
materializa en **dos niveles ortogonales**: (1) **enumerar** las salas del establecimiento
y (2) **barrer** los pacientes de cada sala. Cualquiera de los dos puede fallar en
silencio y hacer que un ingreso ausente del censo parezca **ausencia confirmada** cuando
en realidad es **censo truncado**. Tanto `get hospitalizacion:sgh:<id>/estado-actual`
como `find --hospitalizados` exponen en `data` cuatro campos que declaran esa fidelidad:

| Campo | Tipo | Qué te dice |
|---|---|---|
| `sweep_complete` | bool (siempre) | `true` = todas las salas **conocidas** respondieron el barrido; `false` = al menos una no respondió |
| `rooms_unavailable` | []string (omitempty) | salas que no respondieron el barrido (solo si `sweep_complete=false`) |
| `enumeration_complete` | bool (siempre) | `true` = sin fallo DURO al enumerar salas; `false` = al menos un servicio no pudo listar las suyas |
| `services_unavailable` | []string (omitempty) | servicios que no enumeraron (solo si `enumeration_complete=false`) |

**Compón los dos bits; no mires uno solo.** El censo es fiel sólo si
`sweep_complete && enumeration_complete`. Semántica honesta: `*_complete=true` significa
"sin fallo DURO observado", **nunca** "la lista de salas es realmente completa" (un 200 con
lista corta-silenciosa no es detectable). Un **censo parcial sigue siendo
enumerable**: el listado se entrega con su alcance incompleto. Lo que NO puedes hacer es
concluir "el paciente no está hospitalizado" desde un censo con `sweep_complete=false` **o**
`enumeration_complete=false`: ahí la ausencia es **fallo de adquisición**, no ausencia
confirmada.

En `find --hospitalizados`, cuando el censo es parcial y hay lote,
`batch_plan.census_incomplete=true` y `census_incomplete_detail` separa ambas
dimensiones con las salas/servicios nominales caídos. En bundle, la misma
limitación aparece como `source_issues[].issue_kind=source_scope_incomplete`;
nunca como ausencia confirmada.

**Fuentes vivas de la unidad (scope `hodom:`, fase 1 — encargo DT 2026-07-06).**
Para el caso HODOM la vitrina expone además dos planillas Drive **manuales** de la
unidad como handles identity-safe (kind `sheet`, `source: drive`):

| Handle | Qué trae |
|---|---|
| `hodom:libro-mayor/<rut>` | fila(s) del paciente en el libro mayor anual: `ESTADO` (con lag de cierre), Barthel, categorización, O2, servicio de origen, CESFAM, motivo de egreso |
| `hodom:programacion/<rut>` | prestaciones programadas por día del paciente en la pestaña del mes en curso |

En `bundle hospitalizacion:sgh:<id> --handoff|--minimal` se **componen solos** como
items del bundle cuando el episodio es HODOM (o el servicio no resolvió); un
servicio resuelto no-HODOM los omite (salida byte-idéntica). En el flujo de censo
ya vienen dentro de cada sub-envelope del lote: no los pidas aparte. La
identidad documental solo habilita Drive si `identity_check.match=true` e
`ingreso_id_verified=true`; el ingreso exacto debe estar probado por censo
activo o por membresía en la ficha SGH del mismo CP. Un match solo de RUT no
basta ni demuestra servicio, ubicación o presencia censal.

Reglas de lectura (doctrina de agente, pactada con el DT):

- **Fuente MANUAL**: planilla de la unidad, no sistema institucional. Reconócela
  por `kind:sheet` + `source:drive` y conserva sus `warnings[]`. SGH y Drive
  tienen temporalidad y gobernanza distintas; el CLI expone procedencia y no
  elige cuál prevalece.
- **`summary.discrepancies[]`**: comparación mecánica con **guard temporal** (solo
  filas cuyo rango solapa el episodio SGH actual; episodios previos del año son
  contexto, no conflicto). Cada entry contiene `{campo, valor_sgh,
  valor_drive, regla}` y nunca `precedence_hint`.
- Una fila no encontrada solo es ausencia de esa fuente si el probe declara
  `negative_lookup_conclusive=true`. Planilla caída o identidad de fila no
  parseable produce `source_issues[].issue_kind=acquisition_error`, no una
  ausencia ni una brecha clínica fabricada.
- **Higiene de planilla**: `data.rows_total`/`rows_empty`/`rows_unparseable`
  cuentan la realidad del CSV (filas de relleno, RUT mal tipeados);
  `estado_normalizado` ∈ {`activo`,`egresado`,`unknown`} absorbe typos
  (`EGRESADC`) preservando el crudo. Un header no identificable, una pestaña
  mensual inexistente o cero matches junto con filas de identidad no
  parseable producen `upstream_unavailable`: **universo trunco, NO ausencia**.
  No infieras una columna RUT por posición. El parser acepta
  `N,NNN,NNN-DV` solo como patrón completo con dígito verificador válido y no
  cuenta filas plantilla sin identidad ni contenido bajo headers reales.
- Multi-fila con el mismo RUT = rehospitalizaciones del año;
  `filas_orden_cronologico[]` da el orden mecánico.

**Epicrisis — SGH primero; HCC solo ante documento SGH válido sin contenido
útil.** La epicrisis SGH es un PDF de primera clase: usa
`get hospitalizacion:sgh:<id>/doc/epicrisis` para un ingreso activo o
`get paciente:hosp/<ingreso_id>/doc/epicrisis` para uno histórico. Ambos
materializan el parámetro upstream completo `form=epicrisis`. No uses el
abreviado `form=epi`: es inválido y fue el que produjo el TCPDF vacío observado.

Lee `state`, `error_code` y los metadatos del documento: `upstream_form`,
`text_useful`, `empty_pdf_like` e `identity_check`. Si el documento SGH válido
trae texto útil e identidad cerrada, esa es la fuente disponible. Solo si ese
documento válido responde sin contenido útil, HCC secundaria es una alternativa
factual: `get hcc:secundaria:<rut>/resumen` para ubicar la atención y luego
`get hcc:secundaria:<rut>/detalle/<id>` para comprobar si expone
`discharge_report`. No presupongas equivalencia, precedencia ni presencia: cita
qué fuente respondió. Las evoluciones (`/evoluciones`) reconstruyen el curso del
ingreso, pero no son la epicrisis formal de egreso.

### 6.3 Paciente sin atención activa (longitudinal)

```
get paciente:identidad:<rut> --fresh
bundle paciente:<rut> --longitudinal
get paciente:timeline/<rut> --since 2025-01-01 --limit 50 --fresh
get paciente:ambulatorias-osiris/<rut> --limit 20   # (v1.3.0) truncado declarado
get paciente:recetas-historicas/<rut> --limit 20    # OJO: primeras N filas upstream,
                                                    # NO garantizadas las más recientes
catalog <rut>
```

`paciente:timeline/<rut>` compone ~10 fuentes longitudinales en orden
cronológico desc; cada entry trae `source_handle` direccionable para profundizar.

## 7. Señales mecánicas que DEBES leer

El CLI no interpreta, pero **indexa señales mecánicas trazables**. Ignorarlas es
usar el CLI a medias.

| Señal | Dónde | Qué te dice |
|---|---|---|
| `warnings[]` | todo sobre | avisos mecánicos no fatales; conserva su procedencia y no los conviertas en decisiones clínicas |
| `summary.source_issues[]` | bundles | hecho por fuente: `source_returned_no_content`, `acquisition_error`, `identity_mismatch`, `source_scope_incomplete` o `unknown`; `alternative_handles[]` no expresa equivalencia, severidad ni orden |
| `summary.bundle_integrity` | bundles | identidad y adquisición solamente. Lee `identity.status`, `acquisition.status` y `does_not_assess_clinical_safety:true`; nunca lo conviertas en autorización terapéutica o suficiencia clínica |
| `texto` / `plan_indicacion` / `data_keys` | sub-objeto evolución (`/evolucion/<eid>`, `/evolucion-ultima`, entries de `/evoluciones`) | forma normal canónica: `texto` = coalesce(`historia`,`evolucion`), `plan_indicacion` = coalesce(`plan`,`indicacion`/`indicaciones`); los crudos se preservan. `data_keys` lista las claves de contenido pobladas. LEE `texto` en vez de adivinar `.historia` vs `.evolucion` — evita el falso "sin evolución" |
| `ubicacion_source` / `diagnostico_admin_source` | `handoff_view` (`bundle … --handoff`) | procedencia ∈ {`estado-actual`, `unavailable`}: `unavailable` = la fuente no pobló (no es "sin ubicación", es hueco); `estado-actual` con campo vacío = ausencia confirmada. No leas `ubicacion={}` como dato real |
| `summary.urgencia.*` | bundles DAU | estados de subhandles y conteos/flags factuales; no son síntesis clínica |
| `status_normalized` | órdenes/indicaciones | índice de estado operacional (`requested`/`executed`/`resulted`/`reviewed`/...); conserva siempre `estado` original |
| `compaction` / `_compaction` / `truncated_keys[]` | salidas `--compact`/`--budget-bytes` | hubo pérdida mecánica; `budget_satisfied` declara si se alcanzó la cota best-effort y `over_budget_bytes` el exceso; `truncated_keys[]` lista las claves exactas truncadas — pide el handle fuente con `--fresh` para texto completo |
| `id_semantics` | `find --hospitalizados` | `next_handle_pattern` para construir handles correctos |
| `batch_plan.requests[]` | `find --urgencia`/`--board`/`--hospitalizados` (≥2 items) | partición factual por costo (`command_args`, `count`, `estimated_cost_seconds`); ejecuta todas las requests en el `execution_order` declarado |
| `item_path` / `fields_coverage*` | listados de `find --fields` | ruta de entries, cobertura observable por campo y campos ausentes en todo el listado; lista vacía = `not_observable_empty_list`, no schema ausente |
| `sweep_complete` / `enumeration_complete` (+ `rooms_unavailable` / `services_unavailable`) | `data` de `estado-actual` y `find --hospitalizados` | alcance del censo SGH en dos niveles. Censo fiel ⟺ ambos `true`; si cualquiera es `false`, no concluyas ausencia |
| `batch_plan.census_incomplete` (+ `_detail`) | `find --hospitalizados` | el plan cubre solo los handles enumerados por un censo parcial; el detalle separa barrido y enumeración |
| `summary.identity_mismatch_handles[]` | `bundle multi_bundle` | componentes exactos con mismatch; inspecciona cada sub-envelope y no extrapoles seguridad al resto |
| `summary.discrepancies[]` | bundles de hospitalización con items `hodom:` | comparación factual SGH–Drive con guard temporal y procedencia; no incluye `precedence_hint` |
| `header_row_index` / `rows_total` / `rows_empty` / `rows_unparseable` / `estado_normalizado` | `data` de handles `hodom:*` | higiene de planilla manual. Header/pestaña inválidos o identidad no parseable que impide una ausencia fiel → `upstream_unavailable`, no `ausente` |
| `negative_lookup_conclusive` / `remediation_code` | `health.systems.drive` | si una búsqueda negativa puede leerse como ausencia de esa planilla y qué reparación de fuente corresponde |
| `best_current_context.navigation_targets[]` | `find --rut` | rutas disponibles para contextos observados sin recomendación ni orden de preferencia |

En bundles de hospitalización, `summary.hospitalizacion` declara estados,
conteos y procedencia de adquisición. El bundle mínimo incluye
`/ingreso-servicio`, no `/doc/ingreso`; el segundo sigue direccionable por
`get`. Los PDFs exponen metadata mínima (`pdf_size_bytes`, `text_len`,
`pages_estimated`, `pdftotext_ok`, `text_useful`, `empty_pdf_like`,
`upstream_form`) para distinguir adquisición útil de TCPDF vacío.

## 8. Identity-safety (innegociable)

El handle lleva la identidad esperada; el CLI verifica
`rut(handle) == extractRUT(upstream)`. Si no conmuta → `identity_mismatch` y se
rechaza el dato. **Para ti:** si ves `identity_mismatch`, NUNCA uses ese
contenido y NUNCA lo atribuyas al paciente. No es un dato "casi bueno"; es un
dato de otra persona.

En bundle, `summary.bundle_integrity.identity.mismatch_handles[]` nombra los
items afectados. En lote, usa `summary.identity_mismatch_handles[]`. Descarta
esos contenidos; los estados no certifican seguridad clínica del resto.

## 9. Límites doctrinales (lo que NO debes esperar ni pedir)

- **No interpretación clínica.** El CLI no resume, no prioriza, no ranquea, no
  filtra por relevancia. `bundle --minimal` solo **compone** handles para reducir
  round-trips; no genera resumen. La síntesis clínica es tuya.
- **No escritura.** No hay endpoints de escritura. No intentes registrar,
  modificar ni dar de alta.
- **`state=ausente` ≠ ausencia clínica.** Puede ser brecha documental upstream.
  Obliga a verificar con fuente directa o equipo; no concluyas "el paciente no
  tiene X" desde un `ausente`.
- **`resultados/lab` con `current_encounter_match:false`:** son paneles LIS
  validados recientes por RUT, no prueba de que sean de la atención actual.
- **`imagenes/narrativas`** expone **menciones** de estudios (TAC/eco/RX) en la
  narrativa; NO concluye que el estudio se realizó. Informes TAC reales copiados
  viven en `urgencia:dau:<atencion_id>/observaciones`.
- **PDFs pueden venir vacíos** (TCPDF). Mira `empty_pdf_like`/`text_useful` antes
  de citar contenido de un PDF.
- **No pidas comandos fuera del set cerrado.** Si algo no está, el CLI dice
  `not_implemented_yet`; ese es el contrato, no un bug que debas sortear.

## 10. Caché y `--fresh`

Stateless con caché en disco, TTL por kind (encounter/timeseries/orders/medications
60s; triage/narrative/diagnosis 5min; lab_history 10min; document 24h; history 12h;
sheet 10min). Los handles `hodom:*` tienen además un **caché de archivo** (el CSV
crudo de la planilla, 10 min, una descarga por planilla por lote); `--fresh`
bypassa **ambos** niveles.
Usa `--fresh` cuando necesites el estado **ahora** (paciente activo, turno en
curso) y quieras bypassar la lectura de caché. `--fresh` igual reescribe la
entrada nueva.

`--fresh` **solo existe en `get` y `bundle`** (los que cachean en disco). `find`,
`catalog` y `health` son siempre en vivo (no cachean). Si pasas `--fresh` a `find`
recibes `usage_error` con el mensaje honesto `"find no cachea; --fresh no aplica
(siempre en vivo). --fresh solo existe en get/bundle."` — no es un flag que falte
un argumento, es que no aplica por diseño. `error_detail.remove_flag="--fresh"`
expone el delta mínimo de autocorrección sin repetir el RUT, nombre o atención
del argv; no esperes `suggested_command_args`.

## 11. Disciplina del agente

- **PHI:** no pegues datos identificables (nombre, RUT, texto clínico completo)
  en documentos de ingeniería, logs ni repos. Reporta agregados, conteos o
  brechas desidentificadas.
- **Compón, no negocies:** toma el subconjunto de handles que tu caso requiere;
  el CLI no decide cuáles son "relevantes".
- **Verifica el `ausente`:** una brecha documental obliga a confirmar con fuente
  directa antes de afirmar.
- **Confía en el contrato, no en el texto:** decide flujo por `error_code`,
  `state` y `data_keys` del envelope, no por strings humanos. El exit code solo
  si invocas sin pipes (§1: los pipes destruyen `$?`).
- **Truncado del canal (NO es del CLI):** el binario SIEMPRE emite el JSON
  completo por stdout; si tu runtime trunca el output de herramienta (~2-4k
  chars), redirige a archivo y consulta selectivo:
  `hsc-agent-cli bundle ... > /tmp/b.json && jq '.summary' /tmp/b.json`.
  Para snapshots conversacionales usa `--compact` (y `--last N` si necesitas
  más profundidad) en vez de pelear con el truncado. Desde v1.3.0 tienes
  además knobs de presupuesto del lado del emisor: `--fields` en listados de
  `find`, `--limit` en fuentes históricas, `--budget-bytes` en el handoff —
  prefiérelos antes de redirigir a archivo.

## 12. Referencias

- Doctrina y contrato público (SSOT de implementación): `~/projects/hsc-agent-cli/CLAUDE.md`.
- Referencia técnica de endpoints upstream: `~/projects/hsc-agent-cli/docs/reference/`.
- Estado operacional vigente: `~/projects/hsc-agent-cli/MEMORY.md` y el handoff vigente del repo.
- **Suite de aceptación del contrato** (5 escenarios exigentes, casos vivos
  auto-descubiertos; corre el binario y verifica el contrato de extremo a extremo):
  `~/projects/hsc-agent-cli/scripts/eval-contrato-agente.sh`. Córrelo para confiar en
  que el CLI honra lo que este manual promete antes de apoyarte en él.
