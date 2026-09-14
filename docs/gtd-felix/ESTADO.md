# GTD de Félix · línea de estado actual

Corte **2026-09-14 UTC**. Este archivo es la única fuente del estado del
proyecto; [GUIA.md](GUIA.md) conserva requisitos y plan. Las decisiones posteriores
no se convierten en implementación por aparecer en la guía. Spec, diseño y runtime
se comprueban por separado. El historial superado queda en el archivo privado;
Git conserva los cortes nuevos. No hay datos personales ni credenciales aquí.

## Veredicto de producto

**Servicio operativo, piloto supervisado; producción personal no aceptada.**
C1 operativo; C2–C6 abiertos. I1 publicado en origen (`9896336` verificado en
remoto). I2 publicado (`65f543e`), instalado sobre datos migrados v3 y reabierto
operativo con reconcile real; runtime y documentación van por separado
(docs `9449e08` y posteriores), aceptación humana NOT_RUN. I3 publicado e
instalado (`7bc1fe8`, bundle de 37 archivos verificado; datos migrados v3→v4
con `migration:i3`, retención que distingue disponibilidad vigente de traza
sintética) y reabierto operativo con reconcile real; Gmail selectivo sigue
degradado preexistente (4 lecturas pendientes, sin éxito completo), calendarios
al día. La dirección
arquitectónica e integración las conserva Codex; Hermes sigue como runtime del
bot. Este encargo se ejecutó en OpenCode según lo asignado, sin llamadas LLM
pagadas ni envíos reales.

El último recorrido real reutilizó un material existente, registró una evaluación
insatisfecha y confirmó la devolución por Telegram en 192,3 s sobre 240 s
reservados. No generó otra ejecución. No terminó el asunto ni acreditó facilidad
de corrección/pausa/regreso. La valoración explícita de utilidad sigue pendiente;
la última crítica del usuario a la calidad y los controles no se da por resuelta.

## Identidad y funcionamiento observados

| Objeto | Evidencia del corte |
|---|---|
| Fuente ejecutable | I3 `7bc1fe8` publicado, instalado (datos v4) y reabierto operativo (bot disponible para recorrido; aceptación pendiente); rama `fxai/gtd-felix-20260911` en sync; base documental `9541abf`/`0fbc18e`, código base `01086a3`; I2 `65f543e` respaldado como conjunto previo |
| Producto instalado | runtime I3 `7bc1fe8` + pin Hermes `5eb99eb` (`28f0a36`; bridge idéntico al bundle) sobre datos migrados v4 con `migration:i3`; `recovery_required` reconciliado antes de arrancar; unidades `gtd-felix` y gateway en marcha, un escritor, receptor Telegram único; conjunto v3 + runtime I2 previos respaldados sin modificar. Incidente 14:09: checkout Hermes compartido avanzó a `5eb99eb` y el gateway entró en bucle por pin (`gmail_bridge_runtime_mismatch` ×92, contenido); reparado actualizando el pin tras verificar el contrato (9 pruebas herméticas), gateway estable sin reinicios. Gmail selectivo degradado preexistente y ajeno al incidente (nunca completó; backoff ~24 h) |
| Salud y cola | HTTP `ok`, cero ejecuciones pendientes en consulta autenticada (recibo de base) |
| Presupuesto | una ejecución global; 7.200 s/día civil America/Santiago; 2.262,4 s comprometidos y 4.937,6 s restantes observados en base y en migrado. No equivalen a cuota de Codex ni factura |
| Runtime del bot | Hermes, `deepseek-v4.1-flash`, `opencode-go`, `max` configurado; aplicación efectiva del esfuerzo por el proveedor no demostrada |
| Construcción | OpenCode con `muse-spark-1.3-contributor` para I1, bajo dirección de Codex; sin inferencias pagadas del bot para invariantes (pruebas locales deterministas) |
| Delegación del producto | cero ejecutores configurados; G7 nativo mínimo no acreditado |
| Esquema | candidato SQLite `user_version=3` (migraciones I1+I2; I1 publicado corresponde a v2); base exportada `user_version=1` verificada por hash `09a38058…ee2424`. Base viva nunca abierta directamente |

Fuente y realización KORA siguen separadas de configuración, credenciales,
memoria, datos y estado nativo de Hermes. Este corte documental no reinstala ni
reinicia servicios. Los directorios sin seguimiento `candidates/` y `versions/`
se preservan; no se agregan masivamente al commit.

## Qué existe realmente

| Subsistema | Implementado/observado | Límite relevante |
|---|---|---|
| Dominio y captura | API y comandos versionados; originales, operaciones, autoría y controles sin LLM | Interpretación contextual y UX no acreditadas en recorrido completo |
| Datos | 13 tablas: 12 previas + `source_entries` (esquema v4, candidato I3 sin instalar); WAL, FK por conexión, `BEGIN IMMEDIATE`, originales por hash | `items.document` conserva agregado humano con stubs de referencia; recibos y parches usan la misma forma; ingesta/selección por revisión vive en `source_entries` tras el corte |
| Ejecución | ciclo autorizado separado de intento nativo; admisión inmutable, consumo monotónico, terminalidad/integración separadas, STOP, pausa, reconciliación, presupuesto familiar | Orquestación activa en claves pequeñas; historial global congelado como `*:legacy:v1` sólo para consulta/idempotencia/recuperación |
| Conversación y devolución (I2) | identidad por asunto ante respuestas y precisiones; corrección invalida y versiona; pausa en vuelo con regreso vigente; devolución referencia material y versión; lista/lote paginados; `due_at` como retorno autorizado | Recorrido humano real con el principal pendiente (NOT_RUN); pruebas sintéticas con fixtures, no inferencia LLM |
| Fuentes | agenda conectada; Gmail readonly, ámbito autorizado desde 2026-08-01; fuentes seleccionadas usadas en material real | Cobertura parcial/degradada; selección global e incrementalidad/retención completas aún por acreditar (I3) |
| Resultados | materiales versionados, evaluación separada, entrega automática y deduplicación | Material válido no significa resultado suficiente; nueva regla de prosa no prueba utilidad (I2) |
| Efectos | ledger de propuestas, autorización, despacho y observación existente | No habilita escritura general en Google; reconciliación final pendiente de C5 |
| Recuperación | exportación coherente, migración ensayada en copia aislada, restore con traslado de delta por PK que conserva uuid/versiones (ensayado; el replay por operación conserva contenido con uuid nuevo) | Restore/rollback final sobre la entrega completa se cierra en I5; instalación viva posterior |

Magnitud de la copia: 32 jobs; serialización JSON de `execution:state` 4.734.704
bytes y `execution:orchestration` 3.531.798 bytes en base. Tras I1 en copia
aislada: estado activo 7.663 bytes, orquestación activa 138 bytes; 32 ciclos,
32 runs, 866 observaciones, 118 idempotencias `control:op:*` preservadas.
Lecturas activas (`budget`, `pending`, `get_job`, `validate`) por clave/fila sin
decodificar el historial. Con historia ampliada a 532 runs el presupuesto sigue
en ~22 ms y el estado activo en 7.663 bytes.

## Evidencia y brechas de cierre

| Criterio | Estado | Condición que falta |
|---|---|---|
| C1 continuidad | Operativo | Conservar captura, identidad, presupuesto y recuperación ante cambios (I1 lo preserva en migración; instalación viva posterior) |
| C2 recorrido humano | Parcial | Preparación útil, corrección material, pausa durante trabajo y regreso; variante libre, consultas/lotes y G7 mínimo (I2) |
| C3 fuentes | Parcial | Cobertura pertinente incremental, retención mínima incluidas transcripciones, cursores/revisión/reinicio y cambios dependientes (I3) |
| C4 retorno cotidiano | Parcial | Utilidad y carga humana, acceso a material, oportunidad, silencio y pausa comprobados en canal real (I4) |
| C5 recuperabilidad | Parcial | Restore, rollback, configuración/dependencias y reconciliación de la revisión final (I5; I1 deja migración/rollback ensayados) |
| C6 aceptación | Abierto | Usuario reconoce utilidad en asuntos propios tras el recorrido; no inferirla de entrega ni de silencio |

- Revisión independiente 2026-09-14 (`i1-director-review-20260914`, cinco
  sondas): los cinco casos fallaban en `1f6ebe0` y pasan con la corrección
  (guardia de migración preserva 1 job heredado sin backup; límites del hijo
  50 s / coste 1 / 0 descendientes como la base; causa repetida devuelve
  `duplicate_cause` estructurado sin ciclo parcial; agotado visible tras 64
  históricos; observación rechazada deja 0 filas y plaza `reserved`).
- I1 migración (repetida tras corregir): PASS semántico (0 diferencias en IDs,
  nativas, versiones, períodos, 866/866 observaciones; tablas dominio intactas
  261/325/396/1/298; presupuesto migrado 2.262,4 s y período
  `daily:...:2026-09-13` idénticos al recibo; 118/118 idempotencias preservadas).
- I1 lecturas acotadas y completas: PASS (estado 7.663 B vs 4.734.704 B;
  orquestación 138 B vs 3.531.798 B; `get_job` 0,4 ms, `pending` 0,1 ms,
  `budget` ~20 ms; con 532 runs el presupuesto sigue ~29 ms y el estado en
  7.663 B; recorridos por asunto/actor/integración paginados sin tope).
- `test_control` 70/70 PASS (64 + 6 regresiones que fallan sin su fix: 5 de la
  primera revisión más identidad de facetas nativas); `test_daily_budget` 17/17
  PASS; `test_spent_continuation` 7/7 PASS; `test_orchestration` 62/62 PASS;
  `test_core`+`test_gtd`+`test_source_evaluation` 76/76 PASS (las 6 fallidas de
  fuentes citadas en el corte anterior ya no reproducen en este candidato;
  su capa completa se resuelve en I3). Paquete anterior: 274/274 PASS con claim
  HTTP (94 control/diaria/gasto + 42 Hermes + 138 orquestación/núcleo/fuentes).
- Cierre de integración I1 (revisión 2026-09-14, paquete 2): la plaza nativa se
  reclama durable y atómicamente (`control.claim_dispatch`) ANTES del efecto
  remoto, con la red fuera de la transacción; el segundo despacho no crea otro
  run remoto (`uncertain`/`native_slot_busy`, 1 POST); concurrencia resuelta por
  el índice único; la incertidumbre conserva la plaza y se reconcilia antes de
  reintentar (misma `Idempotency-Key`, sin duplicar runs); el hijo corre tras la
  terminalidad del padre con su asignación (60 s / coste 2, un activo local);
  STOP sólo llega a identidades nativas admitidas exactas. `max_active=2` sigue
  admitido: acota reservas, no ejecuciones; la plaza nativa sigue única global.
  El fallo Hermes heredado era regresión de I1 mal clasificada, ahora corregida:
  el test espera padre e hijo secuenciales y pasa.
- Suite del adaptador Hermes 46/46 PASS (10 pruebas nuevas + test heredado
  adaptado al contrato secuencial; 8 fallan sobre `b3cc45b` por estante y 3
  guardas pasan en ambos). Durable nunca-enviado se recupera por
  reconciliación tras liberar la plaza (HTTP y Kanban, con reinicio y STOP);
  el envío incierto nunca se recrea a ciegas (inventario Kanban o misma
  `Idempotency-Key` HTTP).
- Compatibilidad de adaptadores cerrada: `test_adapters` 7/7 PASS. Los 2 casos
  eran regresiones de I1, no deuda externa: la proyección a tablas perdía
  facetas de identidad nativa (`thread_id` de Codex) y `observe` rechazaba la
  terminalidad con `native_identity_changed`; el recorrido del ejecutor quedaba
  sin terminal y el descarte por corrección humana estrellaba un `KeyError`
  latente. Corregido con identidad completa en `detail_json.native` (columnas
  mandan en la cuaterna) más una regresión directa; ambos fallan sin el fix.
  `test_mcp` y `test_application` pasan con ellos.
- Total integrado actual: 338/338 PASS (102 control/diaria/gasto/adaptadores +
  236   Hermes/orquestación/núcleo/fuentes/mcp/aplicación, medidos por módulo:
  71+17+7+7 y 46+62+17+47+12+23+29). KORA `check` revalidado aquí con
  `--knowledge-root /home/felix/kora-knowledge`: ok (523/18).
- I2 verificado en aislamiento: `test_i2_journey` 12/12 (identidad de tres
  frentes con plazo y precisiones, mensaje ajeno separado, corrección que
  invalida y devolución versionada, pausa que bloquea y regreso vigente,
  `due_at` como retorno, material largo completo por segmentos, lote 15 con
  4 hechos + 2 pospuestos + 9 restantes, paginación sin crear asuntos,
  idempotencia y no-repost de envíos, migración unitaria con rechazo en vivo).
  Módulos I2 y vecinos en verde: control/diaria/gasto/adaptadores/gtd/núcleo
  166/166; Hermes/orquestación/fuentes/mcp/aplicación/telegram/pausa 278/278;
  agenda/efectos/materiales/índice/producto/recuperación/adjuntos/fuentes 129/129;
  codex probes 50/50 y remoto 14/14 (un probe de Codex falló una vez por tiempo
  y pasó al repetir; ruta no tocada por I2).
- Conjuntos con fallos previos a I2, idénticos antes y después (listas
  comparadas línea a línea contra la base publicada): 26 en
  atención/codex-local/recorridos/instrucción y 19 en gmail/google/nativo;
  fuera del contrato I2 y sin regresiones nuevas. Fuentes (I3) y Codex en
  producción (no activado) quedan pendientes.
- Realización preparada 2026-09-14 (sin instalar): export actual
  `b298c3…7a24f3` con manifiesto propio (esquema v1, 261/396); migración
  reensayada sobre ese origen con 0 diferencias (32/32/866/118 y 8/11/50/0);
  restore/rollback reensayado con captura posterior preservada por identidad
  mediante traslado de delta por PK (uuid/versiones/autoría/relaciones
  idénticos, replay idempotente, sin envíos nuevos); el replay por operación
  solo conserva contenido con uuid nuevo, por eso el corte exige quiescencia.
  Comparación semántica integral de la migración con 0 diferencias (contenido
  y basis de 8 materiales, criterio y contexto de 11 evaluaciones, derivación
  exacta de 50 entregas, consumo de 866 observaciones, identidad nativa
  cuádruple de 32 runs). Rechazo `newer_schema` del código instalado ante v3;
  release `release-65f543e.tgz` (42 entradas: 5 dirs + 37 archivos, bytes
  idénticos al candidato) y plan de corte ejecutable con migración offline
  explícita y arranque por etapas vía `recovery_required`+`reconcile`.
  Instalación viva observada ese día: salud ok, cero pendientes, período
  fresco con 7.200 s; `service.json` efectivo ya declara DeepSeek/opencode-go
  (el borrador preparado con otro modelo está superado, sin cambios).
  Recorrido humano y producción siguen NOT_RUN.
- Migración I2 ensayada sobre la exportación privada (hash verificado
  `09a38058…ee2424`): 8 materiales, 11 evaluaciones, 50 envíos, 0 omitidos;
  0 diferencias semánticas (filas contra arreglos históricos, IDs nativas,
  versiones, presupuesto); recibo `migration:i2` en metadatos. Rollback
  ensayado: snapshot v2 + replay por identidad (1 asunto, 4 operaciones,
  4 eventos, 2 originales, 1 envío; 50 envíos previos verificados
  byte a byte); el runtime v2 publicado abre y lee lo revertido; el runtime
  v2 rechaza el esquema v3 (`newer_schema`). Rollover diario comprobado de
  paso: período 2026-09-14 amanece con 7.200 s intactos.
- Invariantes I1: PASS en suite (causa duplicada/idempotencia, agotamiento sin
  autorrenovación, presupuesto familiar sin doble cómputo, exclusión global con
  incertidumbre y delegación, STOP/corrección/invalidación, reinicio y
  reconciliación de identidades, compatibilidad de comandos/versiones/recibos).
  Prueba sintética no acredita proveedor ni aceptación humana.
- Código viejo rechaza esquema nuevo (`newer_schema`); rollback ensayado con una
  captura posterior preservada por traslado de filas (262 vs 261 asuntos, mismo
  uuid y versión) sin repetir efectos externos; el replay por operación da
  contenido idéntico con uuid nuevo.
- KORA `check` revalidado en este checkout: `python3 kora_cli.py
  --knowledge-root /home/felix/kora-knowledge check` (CPython 3.12.3 del
  sistema, sin venv) devuelve `ok:true`, 523 activos, 18 archivados, 0
  incidencias, 463 verificaciones de referencia. Sin el flag falla con
  `Biblioteca de conocimiento ausente` (exit 1) porque el enlace `knowledge`
  apunta a `../kora-knowledge`, ausente junto a esta raíz; no es un fallo del
  candidato. No sustituye validación del producto.
- Guarda de agotamiento: comprobada en pruebas aisladas. El job real de 192 s
  terminó antes del límite y **no ejercitó esa rama**.
- Contrato de devolución de `01086a3`: instalado; efecto sobre calidad **NOT_RUN**.
- Producción aceptada: **NOT_RUN**. I1 no declara producción aceptada.

## Línea de base reproducible y evidencia privada

En este host: `/home/felix/.local/state/gtd-felix/rebaseline-20260913/` contiene
`baseline-receipt.json` y `baseline-export.zip` (4.805.602 bytes; SHA-256
`09a38058d5c4e4651e288057bc5f1c2698a3eacde3409da9cdd3398566ee2424`). El recibo
registra momento, salud, saldo, identidad y conteos. Exportar no demuestra restore.
No publicar estos archivos: contienen estado privado.

Los recibos anteriores permanecen en
`/home/felix/.local/state/gtd-felix/production-c2-dnx2m7zw/`, especialmente
`dir-review-v8-receipt.json`, `instalacion-return-receipt.json`,
`tramo-cierre-revisado-receipt.json` y `suite102-{base,candidata}.log`.
La guía y el estado anteriores se conservaron en
`/home/felix/lab/gtd-agentico-2026-09-10/archivo/2026-09-13/antes-linea-base/`.
Las rutas históricas de GUIA/ESTADO apuntan a estos dos archivos versionados,
sin otra copia activa. El estado personal detallado sigue en el servicio.

## Diseño y próximo incremento

I1 implementado, publicado e instalado (v2 y luego v3/v4 por I2/I3):
`store` con `work_cycles`/`runs`/`run_observations`, `control` y `orchestration`
sobre tablas con lecturas acotadas, migración con comparación semántica y
rollback ensayado. Detalle y decisiones en GUIA §§6–7 y en este archivo.

Límites de I1: materiales, evaluaciones, entregas y fuentes se migran en sus
incrementos; `items.document`/`field_versions` conservan el agregado humano.
Doble escritura permanente eliminada: tablas + blobs activos pequeños son la
única autoridad tras el corte; `*:legacy:v1` queda congelado para consulta,
idempotencia y recuperación. Directorios `candidates/` y `versions/` preservados.
Límites reales medidos: el conjunto activo vive del protocolo (plaza nativa
única, `max_active`, familias pequeñas) y se recorre completo sin topes;
`duplicate_cause` es el rechazo de dominio para causa repetida tras cierre
(`purpose_already_active` si el asunto sigue abierto); `_own_event` cubre el
asunto más sus antecesores (cadena `parent_id` ≤16); `pending()` de dueño
devuelve el activo completo sin paginar por ser pequeño por protocolo.

I2 implementado, publicado e instalado: tablas
`materials`/`assessments`/`deliveries` como autoridad única con stubs de
referencia en documento, recibos y parches; `due_at` como retorno autorizado;
outbox de Telegram sobre `deliveries`; resumen breve con acceso completo a
pedido; undo con archivo y restauración exacta. Recorrido cubierto con
fixtures y verificado en vivo tras reapertura (trabajo legítimo
completed+integrated con budget exacto). Recorrido humano/LLM: NOT_RUN.

Siguiente: **I4/G7** sobre I3 instalado (primera sincronía o retorno
legítimo aún por observar; sin actividad sintética para probarlo), con recorrido
humano listo para coordinar por dirección. I4 en curso: instalados los 5
archivos revisados `bf43b9f` (control, google_sources, source_monitor,
source_evaluation + hoja nueva source_error_codes; resto de la composición
previa intacta); ciclo huérfano sanado con re-STOP `i4-tm-stop:3` (sin gasto);
worker recuperado de verdad (evento requested_review→run `b025d38f`, 53
observaciones en 272.65 s, fin nativo cancelled→integración descartada, slot
libre, servicios sin reinicios). Causa PROBADA: límite por trabajo agotado
(`job_runtime_exhausted`: admitido 240 s, primera marca 260.4 s, STOP técnico
14:32:54Z, recibo `hermes:stop` durable con `validation.job_runtime_exhausted`; iniciador local probado, proveedor con actividad monotona hasta el STOP; latencias o fallos internos como causa de la lentitud no excluidos; defecto de producto no demostrado). El run previo util 05eba618 integro con 244.77 s en la misma envolvente de 240 s: el limite se aplica en sondeos de guarda y trabajos de este tamano caen a uno u otro lado por ritmo de sondeo; el total necesario sigue desconocido. Pase de seleccion con guardas superadas y 0 clasificaciones (nada nuevo que clasificar; backlog actual son obligaciones de lectura previas al run). Siguiente accion ejecutada 2026-09-14: plan owner v28 con paso acotado TM + admision por continuacion pendiente (sin request_review) como job 5dbd12c7; 51 obs en 252.87 s, integration integrated con assess-mapa-v28 (satisfied False, brechas explicitas) pero SIN la minuta material encargada: entrega TM no cumplida; respuesta final enviada confirmada (notificacion done con native_reply por diseno; sin aceptacion humana); asistencia fuera de foco; secuenciacion nuestra con tres frentes primero y TM cuarto; Gmail incompleto no prueba que falten documentos: causa residual determinada por sonda real — mensajes gigantes (raw > topes 8/6 MiB; cuenta/auth sanas); contención instalada 3 archivos 0bf7ca1 (TransportError por mensaje + degrade cerrado), resto pendiente sin bloquear. Admisión autónoma 2069f077 documentada (periodic_return legítimo, 258.1 s, descartado). Resto 6429.71 exacto, coste desconocido. C2/aceptacion NOT_RUN. Coste observado desconocido (53 obs. con cost NULL;
$1 es imputación conservadora, no cobro medido); resto 6682.58 = 6955.23 −
272.65. Un pase de selección con 0 clasificaciones y 0 llamadas bridge; Gmail
degradado preexistente intacto, sin material nuevo. Fuentes selectivas ya
autorizadas en ámbito; cobertura incremental y retención en este incremento.

Validación del diseño: **24/24 comprobaciones PASS** del DDL sobre el esquema
actual en SQLite 3.45.1 en memoria, con datos sintéticos. Incluye FK, identidad de
fuentes, material/evaluación del mismo asunto, causa única, plaza nativa retenida
ante incertidumbre y deduplicación de entregas. Recibo y script reproducible en
la carpeta privada de este corte: `design-validation.json`, `validate-design.py`.
DDL SHA-256 `77b1a446bdc9a1f5824cc67c0d3070b9fb6001118ef2141f33a57a01782a8edc`.

Esto **no acredita** conducta LLM ni aceptación. Cada incremento requiere sus pruebas y
ensayo de realización según GUIA. La comprobación KORA se revalidó en este
checkout con `python3 kora_cli.py --knowledge-root /home/felix/kora-knowledge
check` (ok, 523 activos, 18 archivados, sin incidencias); no sustituye
validación del producto.

## E26 · realizado fallback Gmail `6b97caf` (2026-09-14)

Candidato vs instalado: idénticos 4/4 hashes (`google_sources`,
`google_transport`, `source_attachments`, `application` desde `6b97caf`;
remoto en sync tras push normal). Sin migración de datos. Config DeepSeek,
gateway, perfil y límites intactos. Corte mínimo con un escritor; reapertura
con salud ok, receptor único (1 proceso), gateway estable NRestarts 92,
presupuesto idéntico antes/después (active 0, committed 1028.4 s / 4.0 USD,
remaining 6171.6 s, período 2026-09-14), pendientes [], Gmail degraded con 4
pendientes gigantes conocidos, calendarios complete.

Lectura real con código instalado (sólo lectura, 1 raw+1 full por mensaje,
sin modelo ni escrituras): `1a07ca…f6e` raw rehusado `response_too_large`,
full 52 540 B plain con texto 6 373 y 4 adjuntos referenciados;
`1a07ca…966` raw 7 791 323 B (supera tope parser 4 MiB ⇒ `message_too_large`
en la ruta instalada) y full 34 670 B plain con texto 2 179 y 1 adjunto
referenciado. Ambos con identidad, missing_text 0 y manifiesto coherente.
Lectura ≠ selección/clasificación: ninguna evaluación, asunto ni material
creado; adjuntos sólo referenciados, no leídos.

TM `5869a0bb` v29: payload plan preparado y validado offline (5 pasos,
selección de fuentes TM primera, resto del encargo preservado, procedencia
de dirección, sin frase humana nueva), NO escrito; sin `request_review`.
Siguiente trabajo legítimo pendiente de decisión. KORA reproducible con 1
hallazgo preexistente ajeno (`source_error_codes.py` de E17 sin declarar en
resources); nada de los 4 realizados. C2/aceptación humana: NOT_RUN.

## E27 · selección real TM: plan v30 admitido, nativo fallado en proveedor (2026-09-14)

Plan owner `dir27-tm-focus-select:5869a0bb:v29` aplicado sobre TM v29 → v30
(5 pasos, selección de fuentes TM primera, global preservado; validado antes
en copia aislada con red/submit neutralizados: `applied`, intent con primer
paso, y `_continue_work` espejo abrió continuación pendiente + reserva sin
`request_review`). Una única admisión: job `ca99acbc` (prepare_private,
native `run_06ff2d56`). Sin reintento tras el fallo, por contrato.

Resultado: nativo `failed` tras ~600 s de pared sin ningún chunk del modelo
(contexto ~16.5k tokens, 2 mensajes; Hermes mató la conexión por stall 600 s
y el reintento devolvió Broken pipe, proveedor opencode-go). Cero llamadas a
herramientas (sin `source_evaluation`, sin selección, sin material);
integración `discarded`, slot/ciclo limpios (active 0), sin entregas
duplicadas. La guarda local 240 s nunca disparó (observado ~0 s; resolución
None, sin STOP). Gmail intacto: 4 pendientes gigantes, calendarios complete.
Presupuesto (corrección E28, historia conservada): consumo del trabajo 600.36 s
(committed 1028.38→1628.74, remaining 6171.62→5571.26); el +360.3 del reporte
comparaba contra la reserva abierta 1268.38 que ya incluía 240. Imputación
conservadora 1 USD, no cobro acreditado; coste de proveedor observado
desconocido (117/117 obs. con cost NULL). TM v30 active, sin material nuevo.
KORA `ok:true` tras declarar `source_error_codes.py` en resources de
gtd-operations (1 línea, sin cambio de conducta ni reinstalación).
C2/aceptación humana y mapa global: NOT_RUN.

## E28 · candidato: vigilancia temporal ante proveedor en silencio (sin instalar)

Hipótesis de dirección confirmada por evidencia durable del run `ca99acbc`:
116 polls running con `updated_at` congelado mantuvieron observed ~0.0065 s
y `validate` nunca alcanzó `job_runtime_exhausted` (límite 240); el fallo
terminal registró 600.36 s. Fallo de proveedor y defecto de protección
coexistieron; el reporte E27 sólo probaba lo primero.

Candidato E28 (hermes.py, sin instalar; CORREGIDO en E29: el valor era el instante de
recuperación y renovaba el plazo ante envío incierto — ver E29): ancla durable `native_admitted_at` al
acknowledge del dispatch (sólo con run nativo probado; nunca en
never_sent/incierto); piso local para estado `running` en `_observe_api`
(`max(telemetría nativa, ahora - ancla)`), con separación
`native_runtime_seconds` vs `runtime_seconds`; backfill único documentado
para runs admitidos pre-guardia; queued/waiting sin cambios; STOP
idempotente post-límite por recibo durable (una llamada remota). Controles
sin cambios: el call site real (`_advance`→`validate`→`gtd-invalid-stop`+stop)
ya existía. Límites: kanban sin piso; reloj local salta-adelante falla en
seguro; coste sigue NULL (sin invención monetaria). Regresiones: 3 en
`test_hermes` (stall+STOP durable, supervivencia a reinicio, sano+never_sent);
fallan en base, pasan en candidato. Focales: hermes+control+daily 144 OK,
spent+codex_probe 22 OK. C2/minuta/aceptación: NOT_RUN.

## E29 · candidato: plazo ante recuperación + política de espera (sin instalar)

P1: la recuperación de un envío incierto sin recibo renovaba el ancla
(repro E29: timeout post-creación + reconcile a t0+125 ⇒ observed 2,
límite intacto). Causa: sólo never_sent prueba ausencia de envío; incierto
no. Fix E29 (parcial): el ancla conserva el primer intento — pero E30
precisa que `intent.created_at` NO equivale a primer envío (la intención
nace antes, incluso sin envío): el dato es `first_send_at`, escrito
pre-red en el claim y conservado al reconciliar.
cuando ya hubo envío posible, y usa ahora sólo tras marca never_sent; un
ancla existente jamás se sobrescribe. never_sent sigue sin ancla/cargo.
P2 (política autorizada): la cota cuenta vida admitida incluida espera
post-admisión; queued/waiting reportan telemetría pura (transición probada:
queued 120 s ⇒ 2, running ⇒ ~121 + exhausted). El contador diario consume la
misma cota (declarado, no inferencia medida). P3: `_advance` real llega solo
al STOP durable post-límite (margen declarado: un poll; 1 POST stop, sin
re-admisión al mismo propósito, plaza conservada sin terminalidad
fabricada). Regresiones E29: P1 falla en e731c26 y pasa; P2/P3 fijan conducta.
Focales vecinas: hermes+control+daily+spent 154 OK. C2/minuta: NOT_RUN.

## E30 · candidato: primer envío efectivo como origen del plazo (sin instalar)

Cruce never_sent→envío incierto: `_dispatch` borraba never_sent al pasar a
sending sin conservar cuándo fue ESE primer intento; perder el ack caía en
`intent.created_at` (120 s previos sin envío ⇒ falso agotamiento).
Fix: `first_send_at` durable escrito en el claim antes de la red (una vez);
el ancla = ancla existente ?? `first_send_at` ?? ahora. never_sent sin
efecto sigue con observed 0; la recuperación no renueva; el backfill legacy
queda sólo para datos antiguos. Política de vida admitida intacta (sin
segmentar, sin ampliar queued/waiting). Regresión E30: falla en fae79e3
(observed 124.93) y pasa (observed ~5 + STOP automático vía `_advance`
real). Vecinas: hermes+control+daily+spent+codex_probe 170 OK.
Paquete acumulado: un archivo `gtd_felix/hermes.py`. C2/minuta: NOT_RUN.

## E31 · instalado hermes.py E28–E31 (ancla de primer intento + backfill)

Composición instalada: `gtd_felix/hermes.py` hash
`8327d3f6…c84242e` (= cbb3850 + reemplazo exacto revisado en
`_admitted_elapsed`: el backfill prefiere `first_send_at` durable antes que
ahora). Cierra la ventana de interrupción entre writes: ack perdido con
identidad + primer envío persistidos ya no rejuvenece el plazo.
Margen declarado: la denuncia exige el siguiente poll tras el cruce (STOP en
el advance posterior). Lo contado es cota de vida admitida (incluye espera
post-admisión), NO telemetría de inferencia medida; el diario consume la
misma cota. Coste proveedor desconocido (NULL, imputación conservadora).
Backfill `ahora` queda sólo para datos antiguos sin `first_send_at`;
queued/waiting/kanban sin piso (honesto). C2/minuta/aceptación: NOT_RUN.

## E32 · protección verificada en vivo, sin minuta TM (2026-09-14)

Plan v31 (foco TM primero, global como antecedente) admitió UN job `520f13`
(native `run_8824`). La guarda E28–E31 midió cota local desde el primer poll
(6.7 s) y pidió STOP al superar 240 (observado final 252.3 = 240 + margen de
sondeo declarado); nativo canceló dócil, integración `discarded`, slot libre,
sin material/assessment nuevo (v31 intacta, 8/12), Gmail igual (4 pendientes),
sin entregas duplicadas. Consumo 252.4 s (committed 1628.7→1881.1, remaining
5571.3→5318.9, íntegro atribuido a este job; coste NULL, imputación 1 USD).
Tramo del fallo: primera respuesta del proveedor ausente 252 s (0 chunks, 0
herramientas incl. `source_evaluation`; misma firma que ca99 a 600 s). La
guarda NO falló; no hubo reintento. C2/minuta/aceptación: NOT_RUN.

## E34 · transporte medido: relay vivo, stalls específicos de payload (2026-09-14)

Sonda mínima (POST relay, DeepSeek, effort max, 23 chars, cero tools):
traza completa <1 s y 400 determinista de validación (sin header de sesión
del agente). Conectividad/protocolo/capa vivos ESE momento; stalls de
252/600 s con 0 eventos fueron específicos de payloads 12–18k + tools, no
caída general. Exceso declarado: 2 peticiones en vez de 1 (2ª por relectura),
<1 s c/u, 0 tokens, fuera del contador GTD. Sin defecto repo ⇒ sin
candidato. E33 precisado (no reescrito). C2 NOT_RUN.
