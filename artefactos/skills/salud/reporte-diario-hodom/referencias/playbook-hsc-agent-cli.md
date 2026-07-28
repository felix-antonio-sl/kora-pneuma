# Playbook de adquisición con `hsc-agent-cli`

## Veredicto y frontera

La superficie `beta-3` actual es suficiente para el reporte diario HODOM. La
ejecución fallida del 2026-07-28 fue una brecha de orquestación del consumidor:
se materializaron censos completos de servicios candidatos y no se conservó un
ledger paciente × fuente × tiempo × estado.

No agregar comandos al CLI. Mantener dos recorridos distintos:

- **HODOM:** censo completo; ejecutar todo el `batch_plan`.
- **Candidatos:** censo liviano; no ejecutar el `batch_plan` masivo; seleccionar
  y profundizar solo handles justificados.

El CLI selecciona y presenta. La skill sintetiza. El médico o responsable
competente decide.

## 1. Recorrido completo HODOM

### 1.1 Preflight

Ejecutar desde la misma frontera runtime:

```text
hsc-agent-cli health
```

Registrar `fetched_at`, `data.health_status`, `data.systems`,
`data.beta_ready`, `data.all_capabilities_ready`,
`data.degraded_capabilities` y `data.partially_probed_systems`. Continuar solo
con los sistemas utilizables. Ante `upstream_unavailable`, realizar como máximo
un probe adicional y no iniciar fan-out.

### 1.2 Censo

```text
hsc-agent-cli find --hospitalizados --hodom \
  --fields ingreso_id,handle,handle_status,nombre,rut,diagnostico,dias_hospitalizacion,fecha_ingreso,service_name,room_name
```

Inspeccionar:

- `.state`, `.error_code`, `.fetched_at`;
- `.data.sweep_complete`, `.data.enumeration_complete`;
- `.data.rooms_unavailable[]`, `.data.services_unavailable[]`;
- `.data.total_pacientes`, `.data.ready_count`,
  `.data.missing_handle_count`;
- `.fields_coverage[]`, `.fields_missing_all_entries[]`;
- `.batch_plan.requests[]`, `.batch_plan.covered_handle_count`,
  `.batch_plan.total_estimated_cost_seconds`,
  `.batch_plan.execution_order`;
- `.batch_plan.census_incomplete` cuando exista.

Detener el cierre si el censo no es fiel. Conservar las entries positivas
observadas, pero no declarar que el universo está completo.

### 1.3 Materialización

Para cada `batch_plan.requests[].command_args`, en el orden declarado, invocar
el mismo argv y agregar:

```text
--fresh --stream --budget-bytes 16384
```

No alterar handles ni modo. No ejecutar dos requests del plan en paralelo. El
presupuesto es best-effort y se aplica por sub-bundle; revisar
`compaction.budget_satisfied`, `over_budget_bytes` y `truncated_keys[]`.

Si hay un solo handle listo, `batch_plan` se omite por contrato:

```text
hsc-agent-cli bundle hospitalizacion:sgh:<ingreso_id> \
  --handoff --fresh --budget-bytes 16384
```

No usar `--stream` con un solo handle.

### 1.4 Consumo del stream

Para cada línea `type:"bundle"`:

1. leer `envelope.state` y `envelope.error_code`;
2. registrar `handle`, `index`, `fetched_at`, estado y error;
3. inspeccionar `envelope.summary` solo si existe;
4. comprobar `envelope.items[]`;
5. producir el ledger y el brief de ese paciente;
6. liberar el envelope crudo antes de procesar el siguiente.

La línea `type:"summary"` es terminal, pero no sustituye los envelopes ya
emitidos. Reconciliar por `index` y por handle, no por orden de llegada.

### 1.5 Fuentes mínimas y prueba de composición

Cada bundle HODOM direccionable debe contener:

- episodio `hospitalizacion:sgh:<ingreso_id>`;
- items SGH de estado actual, ingreso, evoluciones, evolución última e
  indicaciones vigentes según el bundle;
- `hodom:libro-mayor/<rut>`;
- `hodom:programacion/<rut>`.

Probar la composición Drive mediante `items[]` del sub-envelope:

```text
items[].handle == hodom:libro-mayor/<rut>
items[].handle == hodom:programacion/<rut>
items[].payload.source == drive
items[].payload.kind == sheet
```

La ausencia de esos items solo es admisible si
`summary.hodom_identity_resolution` o `warnings[]` explican por qué no existió
evidencia de identidad suficiente para direccionarlos. Inspeccionar siempre:

- `summary.hodom_identity_resolution`;
- `summary.source_issues[]`;
- `summary.bundle_integrity`;
- `summary.discrepancies[]`, si existe.

`discrepancies` omitido significa “no se detectó una discrepancia mecánica”,
no “ambas fuentes fueron adquiridas”. Probar primero los dos items Drive y sus
estados.

### 1.6 Condición de recorrido completo

Cerrar `G2-census` solo si:

```text
handles_ready_del_censo
  = union(handles hospitalizacion:sgh:* posicionales en command_args)
  = handles_de_envelopes_terminales_recibidos
```

y además:

- `covered_handle_count == ready_count`;
- cada request del plan produjo su summary terminal o un fallo tipado;
- cada entry no direccionable permanece visible con
  `handle_status=missing_ingreso_id`;
- `briefs_verificables + briefs_no_verificables == total_pacientes`;
- no existe `identity_mismatch` usado como evidencia.

## 2. Embudo canónico de candidatos

### 2.1 Censo liviano

Urgencia:

```text
hsc-agent-cli find --urgencia \
  --fields atencion_id,handle,nombre,motivo,edad,categoria,box,especialidad,tiempo,tiempo_minutos
```

No usar `--with-rut` sobre el board completo salvo necesidad explícita: obliga
a enriquecer cada entry. Obtener identidad detallada solo para los casos
seleccionados.

Hospitalizados, una consulta por servicio:

```text
hsc-agent-cli find --hospitalizados --establecimiento 2 --servicio medicina \
  --fields ingreso_id,handle,handle_status,nombre,rut,diagnostico,dias_hospitalizacion,fecha_ingreso,service_name,room_name

hsc-agent-cli find --hospitalizados --establecimiento 2 --servicio traumatologia \
  --fields ingreso_id,handle,handle_status,nombre,rut,diagnostico,dias_hospitalizacion,fecha_ingreso,service_name,room_name

hsc-agent-cli find --hospitalizados --establecimiento 2 --servicio cirugia \
  --fields ingreso_id,handle,handle_status,nombre,rut,diagnostico,dias_hospitalizacion,fecha_ingreso,service_name,room_name
```

Usar `service_name` y `room_name` observados para reconocer Área Quirúrgica.
No congelar IDs de servicio o sala. Si la fuente la presenta como servicio
separado, repetir el patrón con el nombre o ID exacto enumerado.

En esta etapa:

- no ejecutar `batch_plan.requests[]`;
- no conservar el censo crudo en el DOCX;
- registrar por entry solo los campos proyectados y la razón de selección;
- decidir `profundizar`, `no profundizar por criterio observado` o
  `indeterminado por censo`.

Un campo ausente no autoriza `no-candidato-en-este-corte`.

### 2.2 Profundización selectiva

Para handles SGH seleccionados, lotes de hasta tres:

```text
hsc-agent-cli bundle hospitalizacion:sgh:<id1> hospitalizacion:sgh:<id2> \
  --handoff --fresh --stream --budget-bytes 16384
```

Para handles DAU seleccionados, lotes de hasta nueve:

```text
hsc-agent-cli bundle urgencia:dau:<id1> urgencia:dau:<id2> \
  --minimal --compact --last 3 --fresh --stream
```

Con un solo handle, omitir `--stream`. Los límites reproducen el presupuesto
de aproximadamente tres minutos del CLI: 62 segundos por SGH y 20 segundos por
DAU. Son estimaciones, no SLA.

La condición de cierre del embudo es:

```text
handles_materializados = handles_seleccionados
```

Todo handle materializado debe tener `selection_reason`. Todo handle no
seleccionado queda fuera del reporte nominal. Conservar solo conteos agregados
por servicio y los bloques de candidatos profundizados.

## 3. Ledger mínimo de proveniencia

Registrar por paciente y adquisición:

```text
subject_key_local
requested_handle
scope
source
requested_at
fetched_at
fresh_requested
cache_status
state
error_code
census_sweep_complete
census_enumeration_complete
identity_status
hodom_identity_provenance
source_issues
discrepancies
evidence_path
evidence_class
selection_reason
```

`subject_key_local` puede ser un identificador interno del manifiesto. La
política externa decide si el producto autorizado porta identidad clínica.

Interpretación:

- `fetched_at` prueba cuándo el CLI emitió la observación;
- `--fresh` prueba que el consumidor pidió bypass de caché;
- `cache_status` prueba hit/miss en materializaciones cacheables;
- `source`, `handle` y `evidence_path` prueban procedencia direccionable;
- `bundle_integrity` prueba solo integridad de identidad y adquisición;
- nada de lo anterior prueba actualidad del registro manual, suficiencia
  clínica, adopción humana ni autorización de ingreso/alta.

Cada frase factual del brief debe apuntar a un `evidence_path`. Las inferencias
deben listar los hechos que las sustentan. Lo no observado se registra como
pendiente o no verificable.

## 4. Tabla de decisión

| Evidencia | Conducta |
|---|---|
| `state=present`, sin mismatch | Usar solo los campos presentes y conservar proveniencia. |
| `state=ausente`, censo/fuente fiel | Registrar ausencia documental de esa fuente; no convertirla en ausencia clínica. |
| `state=error`, `upstream_unavailable` | No concluir ausencia; marcar fuente no observable y evitar fan-out. |
| `identity_mismatch` | Detener y descartar el contenido afectado. |
| `bundle_integrity.acquisition.status=partial` | Usar hechos de items presentes; prohibir afirmaciones que requieran completitud. |
| `bundle_integrity.identity.status=mismatch_detected` | Bloquear el item o bundle afectado. |
| `hospitalization_observed=true`, `hospitalization_handle_ready=false` | Mantener paciente visible; no fabricar handle; brief clínico no verificable por episodio. |
| Item Drive omitido por identidad insuficiente | No construir `hodom:*`; registrar limitación de `hodom_identity_resolution`. |
| Discrepancia SGH–Drive | Rotular `Observación`; citar ambos valores y su temporalidad; no resolver por precedencia implícita. |
| Resultado técnicamente válido pero sin evidencia para una frase | Omitir la frase o marcarla `pendiente`/`no verificable`. |

## 5. Presupuesto de contexto y tiempo

- Sintetizar un paciente por vez.
- Usar 16 KiB best-effort por bundle SGH; escalar a 32 KiB o abrir un handle
  exacto solo si `truncated_keys[]` afecta una afirmación necesaria.
- No acumular envelopes crudos; conservar ledger, brief y hash local del bloque.
- Usar el costo emitido por `batch_plan` como estimación primaria.
- Modelo de referencia: `62 s × HODOM direccionables` y
  `20 s × candidatos DAU profundizados`.
- Para 29 HODOM direccionables, el modelo estima 1.798 segundos, cerca de
  30 minutos, más censo, render y variación upstream.

Límites editoriales:

- resumen ejecutivo: hasta 700 palabras;
- brief HODOM: hasta 350 palabras;
- bloque de candidato: hasta 180 palabras;
- mover incidencias técnicas sin impacto decisional al ledger, no repetirlas
  como observación narrativa.

## 6. EVAL de referencia

### 6.1 Fixture sintético versionable

Construir envelopes desidentificados con:

- cuatro entries HODOM: tres direccionables y una sin `ingreso_id`;
- dos requests de plan cuya unión cubre exactamente los tres handles;
- un bundle completo, uno parcial y uno con `identity_mismatch`;
- items Drive presentes, ausentes y omitidos por identidad insuficiente;
- censos de candidatos con al menos diez entries y solo dos seleccionadas.

Asserts:

1. el recorrido reconcilia 4 pacientes y 3 bundles;
2. el mismatch nunca produce afirmaciones;
3. cada hecho conserva handle y ruta;
4. los candidatos materializados son exactamente los dos seleccionados;
5. ninguna salida usa “requiere evaluación formal” para un no candidato;
6. los gates de utilidad fallan ante volcado crudo o falta de proveniencia.

### 6.2 Canario vivo sin PHI versionada

Ejecutar el playbook en la frontera autorizada y persistir fuera de Git solo:

- conteos agregados;
- hashes de conjuntos de handles calculados en memoria;
- estados/error codes por fuente sin contenido clínico;
- cantidad seleccionada y materializada por servicio;
- resultado de gates.

El canario pasa técnicamente cuando los conjuntos del censo HODOM reconcilian,
la composición Drive queda probada o limitada explícitamente, y el embudo no
materializa handles no seleccionados. El gate de utilidad requiere además
revisión humana de una muestra de briefs y candidatos; el canario técnico no
la sustituye.
