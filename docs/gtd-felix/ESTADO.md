# GTD de Félix · línea de estado actual

Corte **2026-09-13 21:27 UTC**. Este archivo es la única fuente del estado del
proyecto; [GUIA.md](GUIA.md) conserva requisitos y plan. Las decisiones posteriores
no se convierten en implementación por aparecer en la guía. Spec, diseño y runtime
se comprueban por separado. El historial superado queda en el archivo privado;
Git conserva los cortes nuevos. No hay datos personales ni credenciales aquí.

## Veredicto de producto

**Servicio operativo, piloto supervisado; producción personal no aceptada.**
C1 operativo; C2–C6 abiertos. El goal no está completado. La petición vigente es
fijar esta base y repensar datos, UX, control y camino de cierre para un usuario,
un host y un desarrollador. La dirección arquitectónica queda en la sesión
actual de Codex; no se inicia implementación del rediseño por documentarlo.

El último recorrido real reutilizó un material existente, registró una evaluación
insatisfecha y confirmó la devolución por Telegram en 192,3 s sobre 240 s
reservados. No generó otra ejecución. No terminó el asunto ni acreditó facilidad
de corrección/pausa/regreso. La valoración explícita de utilidad sigue pendiente;
la última crítica del usuario a la calidad y los controles no se da por resuelta.

## Identidad y funcionamiento observados

| Objeto | Evidencia del corte |
|---|---|
| Fuente ejecutable | commit `01086a3b9fb72e2c2aae228732ea53946d8fa6fe`, rama `fxai/gtd-felix-20260911`, publicado en origin |
| Producto instalado | revisión `fc1e17d849e0b9daba3e086b01d1c3ea00315d8b2361866a4289015649917994`, transacción `a005abcd79f24683832b41d81e6ec0be` |
| Archivo focal | `orchestration.py`: SHA-256 `27f17a17e4c751046863d946875f87ffc431ea11385b8a6472016ad1c18be7b1`, fuente e instalado coinciden |
| Salud y cola | HTTP `ok`, cero ejecuciones pendientes en consulta autenticada |
| Presupuesto | una ejecución global; 7.200 s/día civil America/Santiago; 2.262,4 s comprometidos y 4.937,6 s restantes observados. No equivalen a cuota de Codex ni factura |
| Runtime del bot | Hermes, `deepseek-v4.1-flash`, `opencode-go`, `max` configurado; aplicación efectiva del esfuerzo por el proveedor no demostrada |
| Construcción | sesión Hermes existente con `muse-spark-1.3-contributor`, bajo dirección/revisión de Codex; xhigh solicitado, no demostrado por este corte |
| Delegación del producto | cero ejecutores configurados; G7 nativo mínimo no acreditado |
| Esquema | SQLite `user_version=1`, inspeccionado en copia aislada de la exportación del servicio, nunca abriendo la base viva |

Fuente y realización KORA siguen separadas de configuración, credenciales,
memoria, datos y estado nativo de Hermes. Este corte documental no reinstala ni
reinicia servicios. Los directorios sin seguimiento `candidates/` y `versions/`
se preservan; no se agregan masivamente al commit.

## Qué existe realmente

| Subsistema | Implementado/observado | Límite relevante |
|---|---|---|
| Dominio y captura | API y comandos versionados; originales, operaciones, autoría y controles sin LLM | Interpretación contextual y UX no acreditadas en recorrido completo |
| Datos | 6 tablas: `items`, `operations`, `events`, `cursors`, `originals`, `metadata`; WAL, transacciones y originales por hash | Items documentales y varios controles durables en JSON; integridad semántica depende del servicio |
| Ejecución | admisión, presupuesto, identidad nativa, observación, integración, stop y reconciliación | Control y orquestación mantienen estados JSON globales; cronología de agotamientos no explícita en jobs históricos |
| Fuentes | agenda conectada; Gmail readonly, ámbito autorizado desde 2026-08-01; fuentes seleccionadas usadas en material real | Cobertura parcial/degradada; selección global e incrementalidad/retención completas aún por acreditar |
| Resultados | materiales versionados, evaluación separada, entrega automática y deduplicación | Material válido no significa resultado suficiente; nueva regla de prosa no prueba utilidad |
| Efectos | ledger de propuestas, autorización, despacho y observación existente | No habilita escritura general en Google; reconciliación final pendiente de C5 |
| Recuperación | exportaciones coherentes, reinicios y restauraciones aisladas históricas | Restore y rollback de la entrega final completa aún no cerrados |

Magnitud de la copia: 32 jobs; serialización JSON de `execution:state` ≈4,94 MB y
`execution:orchestration` ≈3,71 MB (medida con `json.dumps`, no tamaño en disco).
`control._load/_save` y `orchestration._state/_save` leen/escriben esos agregados.
**Inferencia:** esta representación acopla historial y trabajo activo y dificulta
consultas acotadas. No se atribuye causalmente toda latencia a ese factor sin medir.

## Evidencia y brechas de cierre

| Criterio | Estado | Condición que falta |
|---|---|---|
| C1 continuidad | Operativo | Conservar captura, identidad, presupuesto y recuperación ante cambios |
| C2 recorrido humano | Parcial | Preparación útil, corrección material, pausa durante trabajo y regreso; variante libre, consultas/lotes y G7 mínimo |
| C3 fuentes | Parcial | Cobertura pertinente incremental, retención mínima incluidas transcripciones, cursores/revisión/reinicio y cambios dependientes |
| C4 retorno cotidiano | Parcial | Utilidad y carga humana, acceso a material, oportunidad, silencio y pausa comprobados en canal real |
| C5 recuperabilidad | Parcial | Restore, rollback, configuración/dependencias y reconciliación de la revisión final |
| C6 aceptación | Abierto | Usuario reconoce utilidad en asuntos propios tras el recorrido; no inferirla de entrega ni de silencio |

- `test_spent_continuation`: 7/7 en candidata; base anterior 5 fallos + 2 skips.
- `test_orchestration`: 62/62 en el cambio funcional anterior y 62/62 en la
  primera candidata de devolución. El último ajuste de texto tuvo validación de
  sintaxis/revisión; **no una campaña conductual nueva**.
- Suite focal de 102: 5 fallos + 1 error iguales en base y candidata de la guarda.
  Todos en `test_source_evaluation`: pausa durante evaluación (`reason` ausente),
  uso desconocido frente a cero en dos fallos de helper/bridge, y tres casos de
  evaluación/proyección/cached retry. Su clasificación como problema de fixture
  es una hipótesis pendiente de resolución; no están excusados por ser anteriores.
- Guarda de agotamiento: comprobada en pruebas aisladas. El job real de 192 s
  terminó antes del límite y **no ejercitó esa rama**.
- Contrato de devolución de `01086a3`: instalado; efecto sobre calidad **NOT_RUN**.
- Recuperación de la entrega final y aceptación humana: **NOT_RUN/pendientes**.

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

## Siguiente trabajo autorizado

Tras publicar esta línea de base: decidir estructura de datos, contratos de UX y
control, comparar alternativas y definir una secuencia de incrementos verificables
hasta C6 en GUIA.md. No empezar otra campaña de parches de síntomas ni nuevas
inferencias del bot para este trabajo de diseño. No se ha cambiado el alcance
original ni diferido G7 por omisión.
