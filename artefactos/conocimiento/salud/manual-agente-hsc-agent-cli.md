---
urn: urn:salud:kb:manual-agente-hsc-agent-cli
nombre: manual-agente-hsc-agent-cli
version: 1.0.9
estado: publicado
descripcion: "Manual operativo para agentes AI que consumen hsc-agent-cli, la vitrina clinica del Hospital de San Carlos: comandos cerrados, contrato JSON beta-1, handles identity-safe, recetas por contexto, senales mecanicas y limites doctrinales."
fuente: "Autoria de novo 2026-06-22 sobre hsc-agent-cli@bb2a4ec (CLAUDE.md, contrato beta-1, binario v1.0.14) y la ayuda viva del binario. Sin herencia del manual humano previo (capacitacion-agente). No migrado de la bestia; sin sha256 externo. Actualizado 2026-06-23 (v1.0.1): observabilidad aditiva del envelope (cache_status, error_detail.affected_systems/outage_kind, health latency_ms/checked_at, truncated_keys) y receta de epicrisis via hcc:secundaria, tras deliberacion de panel y spike de viabilidad. Actualizado 2026-06-23 (v1.0.2, TIER 2): bundle multi-handle (kind multi_bundle, producto de sub-envelopes aislados, cota 50) y recommended_batch_handle en find para colapsar el N+1 del censo HODOM. Actualizado 2026-06-24 (v1.0.3, Corte 1): find emite recommended_batch_handles[] particionado por COSTO (~3 min/sub-lote) con estimated_cost_seconds/total, ejecutables en serie; el singular queda como alias del primer sub-lote (retrocompat). Resuelve el timeout del censo atomico (auditoria F2/F3); sobre hsc-agent-cli@4d23e85. Actualizado 2026-06-24 (v1.0.4, Corte 2): gap_kind en cada clinical_gap (confirmed_absence / acquisition_failure / identity_failure / unknown) para distinguir ausencia-confirmada de fallo-de-adquisicion sin reclasificar a mano (auditoria F6); y find ... --fresh ahora da mensaje honesto (no cachea, --fresh solo en get/bundle) en vez de mentir con 'requiere argumento' (F1); sobre hsc-agent-cli@d2331c8. Actualizado 2026-06-24 (v1.0.5, Cortes 3+4): forma normal canonica de la evolucion (texto=coalesce(historia,evolucion), plan_indicacion=coalesce(plan,indicacion), data_keys del sub-objeto, preservando los crudos; mata el falso 'sin evolucion' del jq contra el campo equivocado; auditoria F5) y procedencia de la ubicacion en handoff_view (ubicacion_source/diagnostico_admin_source en {estado-actual, unavailable}; un hueco no se lee como dato real; auditoria F4); sobre hsc-agent-cli@3b9f28d. Actualizado 2026-06-26 (v1.0.6, Corte 5): bundle ... --stream entrega el lote como NDJSON (una linea type:bundle por sub-envelope conforme cierra, en orden de completitud, + linea terminal type:summary con streamed:true y sin bundles[]); opt-in, aditivo, retrocompat, requiere >=2 handles; mata F3 (el lote atomico perdia todo en timeout). Cierra la auditoria del censo (Cortes 1-5). Agregado el suite de aceptacion scripts/eval-contrato-agente.sh (5 escenarios exigentes del contrato, casos vivos auto-descubiertos); sobre hsc-agent-cli@1f4e608. Actualizado 2026-06-30 (v1.0.7, Corte 6 + sub-cortes 1 y 2 del frente faithful find): el censo SGH se vuelve FIEL en sus dos niveles ortogonales y lo declara en data. (Corte 6) hospitalizacion:sgh:<id>/estado-actual agrega sweep_complete/rooms_unavailable (barrido de pacientes por sala). (Sub-corte 1) agrega enumeration_complete/services_unavailable (enumeracion de salas por servicio), ortogonal al barrido. (Sub-corte 2 / Caso A) propaga los CUATRO campos a find --hospitalizados (functor distinto FetchHospitalizados; la fidelidad no es transitiva, hubo que reaplicar el patron) y marca censo-parcial en recommended_batch_handles[] con recommended_batch_handles_census_incomplete (+ _detail con las dos dimensiones por separado), solo bajo censo parcial (omitido bajo censo fiel = byte-identico). Cuando estado-actual concluye ausencia bajo censo incompleto, el clinical_gap de dominio ingreso sale con gap_kind=acquisition_failure (no confirmed_absence). Semantica honesta: *_complete=true significa 'sin fallo DURO observado', no 'lista realmente completa'; censo parcial es USABLE (advierte, no bloquea); el agente compone sweep_complete && enumeration_complete. Sobre hsc-agent-cli@a7b28b9. Actualizado 2026-07-07 (v1.0.8, fase 1 HODOM fuentes vivas, encargo DT 2026-07-06): scope hodom: (hodom:libro-mayor/<rut> + hodom:programacion/<rut>, kind sheet, source drive) — las planillas Drive manuales de la unidad entran a la vitrina como handles identity-safe via export CSV sin credenciales, con cache de archivo 10 min; composicion automatica en bundle hospitalizacion (items aislados) cuando el episodio es HODOM o el servicio no resuelve (servicio resuelto no-HODOM = salida byte-identica); summary.discrepancies[] con guard temporal (estado_hodom SIN precedence_hint — SGH es tiempo real y el libro arrastra lag de cierre; la regla de precedencia del DT queda consagrada como doctrina de agente en 6.2) y gap candidato en clinical_gaps cuando un activo SGH no tiene fila en libro sano; tab_found/rows_total/rows_empty/rows_unparseable/estado_normalizado como higiene de planilla manual; --fresh bypassa tambien el cache de archivo drive; error_detail con sistema DRIVE y reason header_mismatch (retryable=false). Sobre hsc-agent-cli@4e5f225 (tag v1.1.0). Actualizado 2026-07-08 (v1.0.9, ciclo feedback urgencia): imaging_narrative_fallback ahora tambien top-level en bundle --minimal cuando scanner cae con upstream_unavailable (en --compact el objeto data.orders.* existe siempre, triggered:true ante cualquier error del scanner — asimetria documentada); summary.urgencia gana indicaciones_alta_presentes (bool incondicional; presencia mecanica de registro de alta, NO conclusion de egreso — sirve para componer 'activo en board + alta indicada = probable lag upstream') y lab_sources_with_data (lista incondicional [lis, textuales], vacia posible, sin fusionar fuentes) y examen_fisico_terms_in_evolucion (solo con evolucion present; barrido de terminos EF, pista no conclusion) + gap moderate examen-fisico con suggested_handle /evolucion cuando el EF estructurado esta ausente; indicaciones-alta entra a los subhandles del bundle minimal (items 18→19); flag --last N (1..50, solo con --compact) overridea los recortes last_n (defaults 2/2/3/1 intactos sin flag); recetas nuevas: --with-rut en board, lote por medico, y manejo del truncado del canal del runtime (el CLI siempre emite JSON completo). Registro del ciclo (desidentificado) en docs/ciclo-feedback-urgencia-2026-07-08.md del repo. Sobre hsc-agent-cli@15f8902 (tag v1.2.0)."
autor: FS
creado: 2026-06-22
lang: es
tags: [hsc-agent-cli, vitrina-clinica, agentes-ai, contrato-json, handles, identity-safe]
cita: [urn:salud:kb:hodom-direccion-tecnica]
familia: nota
---

# Manual operativo para agentes AI — hsc-agent-cli

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
| `bundle <h1> <h2> ... --handoff\|--minimal` | caro | LOTE: producto de bundles en una invocación (colapsa el N+1 del censo); máx. 50. `find` lo lotea por costo en `recommended_batch_handles[]` |
| `find <criterio>` | medio | Ubicar paciente/episodio activo antes de pedir handles |
| `health` | barato | Verificar conectividad upstream + versión del binario; reporta por sistema `ok`, `latency_ms` y `checked_at` de esa invocación |

**Salida:** SIEMPRE JSON en stdout (incluso los errores). Un log estructurado
puede ir a stderr; **parsea solo stdout**.

**Exit codes** (úsalos para decidir flujo sin parsear texto):

| Exit | Significado |
|---|---|
| 0 | ok |
| 2 | `usage_error` (input mal formado) |
| 3 | `patient_not_found` / `identity_mismatch` |
| 4 | `upstream_unavailable` / `not_implemented_yet` |
| 5 | `internal_error` (bug del CLI) |

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
| `urgencia:dau:` | `urgencia:dau:<aid>` y subhandles `/triage`, `/vitales`, `/anamnesis`, `/hipotesis`, `/diagnosticos`, `/evolucion`, `/observaciones`, `/ordenes/{lab,rayos,scanner,interconsultas}`, `/medicacion`, `/indicaciones-alta`, `/print/pdf`, ... | episodio de urgencia activo (`<aid>` = atencion_id) |
| `hospitalizacion:sgh:` | `hospitalizacion:sgh:<ingreso_id>` y subhandles `/estado-actual`, `/cabecera`, `/ingreso-servicio`, `/evoluciones`, `/evolucion-ultima`, `/indicaciones-vigentes`, `/recetas`, `/doc/{ingreso,solicitud,epicrisis,consentimiento}`, ... | episodio de hospitalización (`<ingreso_id>`, **nunca** `cp`) |
| `hcc:` | `hcc:{primaria,secundaria}:<rut>/resumen`, `/detalle/<id>`, `/search/<query>` | APS/especialidades vía ESB |

**`catalog` es barato, `get` es caro.** Pide `catalog` para saber qué existe;
pide `get` solo de lo que vas a consumir.

## 3. El sobre JSON `beta-1`

Todos los comandos exponen una base común. Estos son los campos que **debes
leer**:

| Campo | Uso para el agente |
|---|---|
| `ok` | éxito booleano de la operación |
| `handle` | la dirección tipada del item devuelto — confirma sobre qué pediste |
| `contract_version` | versión del contrato (`beta-1`); detecta cambios de shape |
| `state` | `present` (hay dato) · `ausente` (no hay, pero la fuente respondió) · `error` · `no_implementado` |
| `kind` | tipo del item (encounter, timeseries, triage, narrative, document, ...) |
| `source` | sistema fuente (dau, sgh, lab, hcc) |
| `data` | el payload real |
| `data_keys` | **lista ordenada de claves top-level de `data`** — úsala para descubrir el shape sin adivinar |
| `warnings` | avisos mecánicos no fatales |
| `error_code` / `error_detail` | ver §4 |
| `clinical_warning` | string de advertencia mecánica; **léelo siempre que no esté vacío** |
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
ignorarlo por sobre-reporte), `clinical_meaning`, `canonical_fallback_handle`,
`fallback_strategy`, `next_steps[]`, `doctrinal_note`. No hay
`downtime_estimated` (sería predicción, no hecho).

| `error_code` | Qué significa | Tu acción |
|---|---|---|
| `usage_error` | input mal formado (handle, RUT, flag) | corrige la invocación; no reintentes igual |
| `patient_not_found` | upstream no encuentra al paciente, o atención DAU cerrada | verifica el id/RUT; si la atención cerró, busca vía `find` o handles `paciente:*` |
| `identity_mismatch` | el handle dice RUT R, upstream devolvió R' | **DETENTE.** No uses el dato. Es una falla categorial, no un dato degradado |
| `upstream_unavailable` | red/proxy/login/5xx | mira `outage_kind`: `transient` → reintenta acotado; `down` → no insistas, reporta caída y usa `canonical_fallback_handle` si lo hay; `unknown` → un reintento acotado y evalúa. `affected_systems[]` te dice qué sistema(s) revisar |
| `not_implemented_yet` | handle válido, fetcher pendiente | no insistas; usa la fuente alternativa que sugiere `error_detail` |
| `internal_error` | bug del CLI | reporta; no es problema de tus datos |

Cuando un handle de scanner/LIS/HCC falla, **lee `error_detail.next_steps` y
`canonical_fallback_handle`**: el CLI te ofrece un camino alternativo dentro del
universo cerrado para que no quedes sin ruta.

## 5. Cómo empezar: navega antes de pedir

No empieces pidiendo handles a ciegas. **Ubica primero** con `find`, que además
te entrega `best_current_context`: un puntero mecánico que indica qué
handle/bundle abrir primero dado el estado activo del paciente.

```
find --rut <rut>           localiza al paciente y su contexto activo
find --atencion <aid>      localiza por atencion_id DAU
find --board               board completo de urgencia
find --urgencia [--categoria C1..C5] [--unidad <txt>] [--especialidad <txt>] [--medico <txt>] [--box <txt>] [--with-rut]
find --hospitalizados [--establecimiento <id>] [--servicio <alias|id>] [--sala <alias|id>] [--hodom] [--desde YYYY-MM-DD] [--hasta YYYY-MM-DD]
```

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
find --urgencia --categoria C2
find --board --with-rut                        # board CON rut por entry (evita el doble viaje al bundle longitudinal)
get urgencia:dau:<aid>/estado-actual --fresh
bundle urgencia:dau:<aid> --minimal           # paquete operacional, sin resumen
bundle urgencia:dau:<aid> --minimal --compact  # snapshot compacto para turno conversacional
bundle urgencia:dau:<aid> --minimal --compact --last 8   # compact con más profundidad (recortes last_n a 8)
bundle paciente:<rut> --longitudinal           # historia contextual mecánica
```

Para reconstruir el episodio: lee `urgencia:dau:<aid>/anamnesis`, `/hipotesis`
(narrativa) vs `/diagnosticos` (CIE-10 codificado), `/vitales`, `/evolucion`,
`/observaciones` (canónico para informes TAC copiados y resultados pegados),
`/ordenes/*`, `/medicacion`, `/indicaciones-alta`, `/print/pdf`.

**`--with-rut` existe y evita el doble viaje**: `find --board --with-rut` y
`find --urgencia --with-rut` enriquecen cada entry con el RUT canónico (default
off por latencia). Úsalo cuando vayas a pedir bundles longitudinales del board.

**Turno del médico (lote mecánico, NO pidas un "resumen de turno")**: el CLI no
resume ni prioriza — pero el lote compone todo lo que necesitas:
`find --urgencia --medico "<nombre>" --with-rut` → ejecuta los
`recommended_batch_handles[]` (sub-lotes `--minimal --compact`, agregables con
`--last N` para más profundidad). Cada sub-envelope trae vitales, disposición
documental y pendientes mecánicos; la síntesis del turno es tuya.

**Señales nuevas del `summary.urgencia`** (ciclo 2026-07-08): 
`indicaciones_alta_presentes` (bool incondicional: hay registro de indicaciones
de alta — compón "activo en board + alta indicada = probable lag del board");
`lab_sources_with_data` (lista incondicional `[lis, textuales]`, vacía = sin
labs en NINGUNA fuente; revisa las que liste, la procedencia importa: LIS es
validado, textuales es copia narrativa); `examen_fisico_terms_in_evolucion`
(solo si evolución present: pista mecánica de EF narrado — el gap de dominio
`examen-fisico` te apunta a `/evolucion` cuando el EF estructurado falta).
`imaging_narrative_fallback` ahora aparece **top-level también en `--minimal`**
cuando `/ordenes/scanner` cae con `upstream_unavailable` (en `--compact` el
objeto vive en `data.orders.*` y existe siempre, `triggered:false` con scanner
sano).

### 6.2 Paciente hospitalizado / HODOM (ingreso SGH activo)

```
find --hospitalizados --establecimiento 2 --servicio medicina
find --hospitalizados --hodom                  # censo HODOM HSC
get hospitalizacion:sgh:<ingreso_id>/estado-actual --fresh
bundle hospitalizacion:sgh:<ingreso_id> --minimal
bundle hospitalizacion:sgh:<ingreso_id> --handoff   # vista compacta para handoff/turno
bundle paciente:<rut> --longitudinal
```

HODOM **no es un comando nuevo**: se expresa con `find --hospitalizados --hodom`,
los handles SGH existentes, el bundle `--handoff` y el timeline longitudinal.
Los handles `hospitalizacion:sgh:*` usan SIEMPRE `ingreso_id`, **no `cp`**
(`find --hospitalizados` trae `id_semantics` con `next_handle_pattern`).

**Censo completo en una operación (lotes por costo).** Para pasar la visita a todo
el censo sin invocar el bundle N veces (un proceso/login por paciente), `find` te
entrega el censo **ya particionado por costo** en `recommended_batch_handles[]`
(plural): una lista de sub-lotes, cada uno con su comando `bundle ... --modo` ya
armado, su `count` y su `estimated_cost_seconds`. No memorices reglas — `find` ya
eligió el modo de cada scope (hospitalizados → `--handoff`, urgencia → `--minimal
--compact`) y el tamaño de cada sub-lote (apunta a ~3 min para no time-outear).

```
find --hospitalizados --hodom                  # mira recommended_batch_handles[]
# ejecuta CADA sub-lote EN SERIE; p. ej. el primero:
bundle hospitalizacion:sgh:<id1> hospitalizacion:sgh:<id2> hospitalizacion:sgh:<id3> --handoff
```

**Ejecútalos en serie, no todos de golpe.** `recommended_batch_handles_total_estimated_cost_seconds`
te dice el costo del censo completo (p. ej. ~2100 s para 35 pacientes): es lo que
costaría en total, no de una vez. Cada sub-lote es ~3 min y devuelve su propio
`kind: multi_bundle`. No subas la concurrencia para "acelerar": SGH legacy serializa
(~62 s/paciente fresh), más paralelismo de cliente lo satura, no lo acelera.

El singular `recommended_batch_handle` se conserva como **alias del primer sub-lote**
(retrocompat); para el censo completo usa el plural. Cada sub-lote es `kind:
multi_bundle`: un **producto** con un sub-envelope por ingreso en `bundles[]`, cada
uno idéntico al bundle single (lee cada uno y compón; el sistema no resume). Cada
componente cierra su propia identidad: un `identity_mismatch` marca SOLO ese handle
en `summary.unsafe_handles`, no contamina al resto.

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
haga perder los ya computados. Procesa cada línea NDJSON por separado.

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
lista corta-silenciosa no es detectable). Un **censo parcial es USABLE**: el listado/censo
se sigue entregando; estos campos **advierten**, no bloquean. Lo que NO puedes hacer es
concluir "el paciente no está hospitalizado" desde un censo con `sweep_complete=false` **o**
`enumeration_complete=false`: ahí la ausencia es **fallo de adquisición**, no ausencia
confirmada.

En `find --hospitalizados`, cuando el censo es parcial **y** hay lote, el bloque
`recommended_batch_handles[]` agrega `recommended_batch_handles_census_incomplete:true`
(+ `..._detail` con las dos dimensiones por separado y las salas/servicios nominales caídos).
Bajo censo fiel ese marcador **se omite** (salida byte-idéntica). En
`bundle … --handoff/--minimal`, si `estado-actual` concluye ausencia del ingreso pero el
censo fue parcial, el `clinical_gap` de dominio `ingreso` sale con
`gap_kind=acquisition_failure` (no `confirmed_absence`): la misma señal, propagada al
lenguaje de brechas (§7).

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
ya vienen dentro de cada sub-envelope del lote: no los pidas aparte.

Reglas de lectura (doctrina de agente, pactada con el DT):

- **Fuente MANUAL con `clinical_warning` permanente**: planilla de la unidad, no
  sistema institucional. Para el **estado del HOY manda SGH** (tiempo real); el
  libro mayor es censo manual **con lag de cierre**; `PROGRAMACIÓN` da la mayor
  granularidad del proceso activo.
- **Regla de precedencia (encargo DT 2026-07-06)**: ante conflicto entre SGH y
  fuentes vivas **en lo relativo al proceso de hospitalización domiciliaria
  actual**, pesan más las fuentes vivas — SALVO el campo `ESTADO`, donde SGH es
  tiempo real y el libro arrastra lag: ahí la vitrina expone ambos valores y la
  resolución es **tuya**, caso a caso.
- **`summary.discrepancies[]`**: comparación mecánica con **guard temporal** (solo
  filas cuyo rango solapa el episodio SGH actual; episodios previos del año son
  contexto, no conflicto). Cada entry: `{campo, valor_sgh, valor_drive,
  precedence_hint, regla}` — `estado_hodom` viene SIN `precedence_hint` (la
  salvedad de arriba); `fecha_egreso_hodom` con `precedence_hint: "drive"`.
- **Gap candidato**: activo en censo SGH + libro mayor **sano** sin fila → entra a
  `clinical_gaps[]` (`domain: hodom`, `gap_kind: confirmed_absence`): anomalía o
  retraso de registro de la unidad — repórtalo, no lo silencies. Planilla caída
  produce en cambio `acquisition_failure` del propio item.
- **Higiene de planilla**: `data.rows_total`/`rows_empty`/`rows_unparseable`
  cuentan la realidad del CSV (filas de relleno, RUT mal tipeados);
  `estado_normalizado` ∈ {`activo`,`egresado`,`unknown`} absorbe typos
  (`EGRESADC`) preservando el crudo. En `hodom:programacion`, `tab_found:false` =
  la pestaña del mes no existe → **universo trunco: NO concluyas ausencia**.
- Multi-fila con el mismo RUT = rehospitalizaciones del año;
  `filas_orden_cronologico[]` da el orden mecánico.

**Epicrisis — pídela por HCC, no por el PDF SGH.** La epicrisis SGH
(`hospitalizacion:sgh:<id>/doc/epicrisis`) **nace como TCPDF vacío** (caveat
4.4.1): es un cascarón, el contenido nunca entró al PDF, así que **OCR no
recupera nada**. La epicrisis **real** viaja por el ESB Salud En Red y es
direccionable: `get hcc:secundaria:<rut>/detalle/<id>` (`discharge_report`).
Flujo: `get hcc:secundaria:<rut>/resumen` para ubicar el `id` de la atención de
egreso → `get hcc:secundaria:<rut>/detalle/<id>`. Cuando `/doc/epicrisis` viene
vacío, el CLI **ya te redirige** allí vía `clinical_warning` /
`nota_doctrinal_si_vacio`: síguela. Las evoluciones (`/evoluciones`) reconstruyen
el curso del ingreso pero **no son** la epicrisis formal de egreso.

### 6.3 Paciente sin atención activa (longitudinal)

```
get paciente:identidad:<rut> --fresh
bundle paciente:<rut> --longitudinal
get paciente:timeline/<rut> --since 2025-01-01 --limit 50 --fresh
catalog <rut>
```

`paciente:timeline/<rut>` compone ~10 fuentes longitudinales en orden
cronológico desc; cada entry trae `source_handle` direccionable para profundizar.

## 7. Señales mecánicas que DEBES leer

El CLI no interpreta, pero **indexa señales mecánicas trazables**. Ignorarlas es
usar el CLI a medias.

| Señal | Dónde | Qué te dice |
|---|---|---|
| `clinical_warning` | todo sobre | advertencia mecánica; léela siempre |
| `decision_safety` | summary de bundles | `safe_to_act_on_bundle` + `blocking_conditions[]` + `cautionary_conditions[]` |
| `clinical_gaps[]` | summary de bundles urgencia/hosp | `{severity, domain, message, gap_kind, suggested_handle}`: brecha + handle para cerrarla. **`gap_kind`** distingue la naturaleza de la falta (eje ortogonal a `severity`): `confirmed_absence` = la fuente respondió y el dato no existe → PUEDES concluir ausencia; `acquisition_failure` = la fuente cayó (`upstream_unavailable`) **o el censo de hospitalización vino incompleto** (`sweep_complete`/`enumeration_complete` en `false`) → NO concluyas ausencia, reintenta o reporta caída; `identity_failure` = `identity_mismatch` (dato de otro paciente); `unknown` = error sin causa clasificable. No reclasifiques con regex: el campo ya lo hace |
| `usable_clinically` | por item de bundle | `false` + `reason_not_usable` cuando el item no sirve (mismatch, PDF vacío, texto inútil) |
| `texto` / `plan_indicacion` / `data_keys` | sub-objeto evolución (`/evolucion/<eid>`, `/evolucion-ultima`, entries de `/evoluciones`) | forma normal canónica: `texto` = coalesce(`historia`,`evolucion`), `plan_indicacion` = coalesce(`plan`,`indicacion`/`indicaciones`); los crudos se preservan. `data_keys` lista las claves de contenido pobladas. LEE `texto` en vez de adivinar `.historia` vs `.evolucion` — evita el falso "sin evolución" |
| `ubicacion_source` / `diagnostico_admin_source` | `handoff_view` (`bundle … --handoff`) | procedencia ∈ {`estado-actual`, `unavailable`}: `unavailable` = la fuente no pobló (no es "sin ubicación", es hueco); `estado-actual` con campo vacío = ausencia confirmada. No leas `ubicacion={}` como dato real |
| `summary.urgencia.*` | bundles DAU | flags de scanner/lab copiados, `possible_copied_report_in_observaciones`, etc. |
| `status_normalized` | órdenes/indicaciones | índice de estado operacional (`requested`/`executed`/`resulted`/`reviewed`/...); conserva siempre `estado` original |
| `compaction` / `_compaction` / `truncated_keys[]` | salidas `--compact` | hubo pérdida mecánica (truncado, `last_n`); `truncated_keys[]` lista las claves exactas truncadas en ese item — pide el handle fuente con `--fresh` para su texto completo |
| `id_semantics` | `find --hospitalizados` | `next_handle_pattern` para construir handles correctos |
| `recommended_batch_handles[]` | `find --urgencia`/`--board`/`--hospitalizados` (≥2 items) | censo particionado por COSTO en sub-lotes (`handle`, `count`, `estimated_cost_seconds`); ejecuta cada uno EN SERIE. `_total_estimated_cost_seconds` = costo del censo completo. El singular `recommended_batch_handle` es alias del primer sub-lote (retrocompat) |
| `sweep_complete` / `enumeration_complete` (+ `rooms_unavailable` / `services_unavailable`) | `data` de `estado-actual` y `find --hospitalizados` | fidelidad del censo SGH en dos niveles ORTOGONALES (barrido de pacientes + enumeración de salas). Censo fiel ⟺ **ambos** `true`; si cualquiera es `false`, la ausencia del censo es **fallo de adquisición**, no ausencia confirmada (compón los dos bits). `*_complete=true` = "sin fallo DURO observado", no "lista realmente completa". Censo parcial es USABLE (advierte, no bloquea) |
| `recommended_batch_handles_census_incomplete` (+ `_detail`) | bloque batch de `find --hospitalizados` | presente SOLO bajo censo parcial; `_detail` separa las dos dimensiones (barrido/enumeración) + listas nominales. Omitido bajo censo fiel (byte-idéntico) |
| `summary.unsafe_handles` / `has_unsafe_handles` | `bundle multi_bundle` | qué componentes del lote tienen `identity_mismatch` (no usar SOLO esos; el resto sigue válido) |
| `summary.discrepancies[]` | bundles de hospitalización con items `hodom:` | conflicto mecánico SGH vs fuentes vivas con guard temporal; `estado_hodom` SIN `precedence_hint` (SGH tiempo real vs libro con lag: resuelves tú); `fecha_egreso_hodom` con hint `drive`. Solo presente si hay discrepancias |
| `tab_found` / `rows_total`/`rows_empty`/`rows_unparseable` / `estado_normalizado` | `data` de handles `hodom:*` | higiene de planilla manual: `tab_found:false` = universo trunco (no concluir ausencia); conteos de filas de relleno y RUT no parseables; estado normalizado (typos absorbidos, crudo preservado) |

En bundles de hospitalización, revisa `summary.hospitalizacion`: `critical_gaps`,
`technical_findings`, `fallbacks`, `doc_ingreso_pdf`, `ingreso_servicio_pdf`. Los
PDFs exponen metadata mínima (`pdf_size_bytes`, `text_len`, `pages_estimated`,
`pdftotext_ok`, `text_useful`, `empty_pdf_like`, `upstream_form`) para distinguir
documento útil de TCPDF vacío.

## 8. Identity-safety (innegociable)

El handle lleva la identidad esperada; el CLI verifica
`rut(handle) == extractRUT(upstream)`. Si no conmuta → `identity_mismatch` y se
rechaza el dato. **Para ti:** si ves `identity_mismatch`, NUNCA uses ese
contenido y NUNCA lo atribuyas al paciente. No es un dato "casi bueno"; es un
dato de otra persona.

`unsafe_to_use` / `blocking_error` en `summary` de un bundle indican que apareció
`identity_mismatch` dentro del paquete: no actúes sobre ese bundle.

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
  viven en `urgencia:dau:<aid>/observaciones`.
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
un argumento, es que no aplica por diseño.

## 11. Disciplina del agente

- **PHI:** no pegues datos identificables (nombre, RUT, texto clínico completo)
  en documentos de ingeniería, logs ni repos. Reporta agregados, conteos o
  brechas desidentificadas.
- **Compón, no negocies:** toma el subconjunto de handles que tu caso requiere;
  el CLI no decide cuáles son "relevantes".
- **Verifica el `ausente`:** una brecha documental obliga a confirmar con fuente
  directa antes de afirmar.
- **Confía en el contrato, no en el texto:** decide flujo por `exit code`,
  `state`, `error_code` y `data_keys`, no por strings humanos.
- **Truncado del canal (NO es del CLI):** el binario SIEMPRE emite el JSON
  completo por stdout; si tu runtime trunca el output de herramienta (~2-4k
  chars), redirige a archivo y consulta selectivo:
  `hsc-agent-cli bundle ... > /tmp/b.json && jq '.summary' /tmp/b.json`.
  Para snapshots conversacionales usa `--compact` (y `--last N` si necesitas
  más profundidad) en vez de pelear con el truncado.

## 12. Referencias

- Doctrina y contrato público (SSOT de implementación): `~/projects/hsc-agent-cli/CLAUDE.md`.
- Referencia técnica de endpoints upstream: `~/projects/hsc-agent-cli/docs/reference/`.
- Estado operacional vigente: `~/projects/hsc-agent-cli/MEMORY.md` y el handoff vigente del repo.
- **Suite de aceptación del contrato** (5 escenarios exigentes, casos vivos
  auto-descubiertos; corre el binario y verifica el contrato de extremo a extremo):
  `~/projects/hsc-agent-cli/scripts/eval-contrato-agente.sh`. Córrelo para confiar en
  que el CLI honra lo que este manual promete antes de apoyarte en él.
