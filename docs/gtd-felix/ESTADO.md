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
14:32:54Z, recibo `hermes:stop` durable; sin fallo de proveedor ni defecto de
producto demostrado). Coste observado desconocido (53 obs. con cost NULL;
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
