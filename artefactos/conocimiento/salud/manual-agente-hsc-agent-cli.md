---
urn: urn:salud:kb:manual-agente-hsc-agent-cli
nombre: manual-agente-hsc-agent-cli
version: 1.0.1
estado: publicado
descripcion: "Manual operativo para agentes AI que consumen hsc-agent-cli, la vitrina clinica del Hospital de San Carlos: comandos cerrados, contrato JSON beta-1, handles identity-safe, recetas por contexto, senales mecanicas y limites doctrinales."
fuente: "Autoria de novo 2026-06-22 sobre hsc-agent-cli@bb2a4ec (CLAUDE.md, contrato beta-1, binario v1.0.14) y la ayuda viva del binario. Sin herencia del manual humano previo (capacitacion-agente). No migrado de la bestia; sin sha256 externo. Actualizado 2026-06-23 (v1.0.1): observabilidad aditiva del envelope (cache_status, error_detail.affected_systems/outage_kind, health latency_ms/checked_at, truncated_keys) y receta de epicrisis via hcc:secundaria, tras deliberacion de panel y spike de viabilidad."
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
`H_SGH_HOSPITAL_ID`, `H_PROXY_HOST`) o de `~/.config/hsc-agent-cli/credentials.env`.
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
get urgencia:dau:<aid>/estado-actual --fresh
bundle urgencia:dau:<aid> --minimal           # paquete operacional, sin resumen
bundle urgencia:dau:<aid> --minimal --compact  # snapshot compacto para turno conversacional
bundle paciente:<rut> --longitudinal           # historia contextual mecánica
```

Para reconstruir el episodio: lee `urgencia:dau:<aid>/anamnesis`, `/hipotesis`
(narrativa) vs `/diagnosticos` (CIE-10 codificado), `/vitales`, `/evolucion`,
`/observaciones` (canónico para informes TAC copiados y resultados pegados),
`/ordenes/*`, `/medicacion`, `/indicaciones-alta`, `/print/pdf`.

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
| `clinical_gaps[]` | summary de bundles urgencia/hosp | `{severity, domain, message, suggested_handle}`: brecha + handle para cerrarla |
| `usable_clinically` | por item de bundle | `false` + `reason_not_usable` cuando el item no sirve (mismatch, PDF vacío, texto inútil) |
| `summary.urgencia.*` | bundles DAU | flags de scanner/lab copiados, `possible_copied_report_in_observaciones`, etc. |
| `status_normalized` | órdenes/indicaciones | índice de estado operacional (`requested`/`executed`/`resulted`/`reviewed`/...); conserva siempre `estado` original |
| `compaction` / `_compaction` / `truncated_keys[]` | salidas `--compact` | hubo pérdida mecánica (truncado, `last_n`); `truncated_keys[]` lista las claves exactas truncadas en ese item — pide el handle fuente con `--fresh` para su texto completo |
| `id_semantics` | `find --hospitalizados` | `next_handle_pattern` para construir handles correctos |

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
60s; triage/narrative/diagnosis 5min; lab_history 10min; document 24h; history 12h).
Usa `--fresh` cuando necesites el estado **ahora** (paciente activo, turno en
curso) y quieras bypassar la lectura de caché. `--fresh` igual reescribe la
entrada nueva.

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

## 12. Referencias

- Doctrina y contrato público (SSOT de implementación): `~/projects/hsc-agent-cli/CLAUDE.md`.
- Referencia técnica de endpoints upstream: `~/projects/hsc-agent-cli/docs/reference/`.
- Estado operacional vigente: `~/projects/hsc-agent-cli/MEMORY.md` y el handoff vigente del repo.
