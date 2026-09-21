# GTD de Félix · estado actual

Corte de continuidad **2026-09-21**. Lecturas por API y exportación consistente;
SQLite consultada sólo en copia privada. Sin instalación ni envíos GTD provocados por este corte.
La evaluación Jev posterior hizo 24 peticiones sintéticas y, tras la siguiente
instrucción de continuar, 22 con texto de correos reales revisado y con datos
innecesarios eliminados. No se enviaron adjuntos ni el mensaje clínico excluido. `candidates/` y `versions/` se preservan sin seguimiento.

## Veredicto

**Producción personal no aceptada. Gateway principal con reinicios repetidos.**
C2–C6 abiertos; aceptación humana NOT_RUN. La observación sana del 15 de septiembre
no describe la disponibilidad actual.

## Observado ahora

- Servicio GTD: systemd active/running, PID 3048478, NRestarts 0. Lecturas de asunto,
  presupuesto, pendientes, cobertura y material respondieron; exportación obtenida.
  `/health` agotó 15 s: no se declara salud integral acreditada.
- Gateway principal: activating/auto-restart, MainPID 0; contador 28427 y aumento
  a 28429 en el journal durante la inspección. Causa no diagnosticada en este corte.
  Es impedimento para un recorrido vivo; no se cambió el pin ni la instalación.
- Presupuesto del 21 de septiembre: active 0, pending vacío, remaining 7200 s,
  committed 0 s. No permite inferir coste histórico de proveedor.
- Asunto del recorrido E69: activo v35; 9 materiales y 13 evaluaciones.
- Cobertura declarada por el servicio: ambos calendarios complete; Gmail degraded,
  4 pendientes de lectura, último código `cycle_not_active`. No se ejecutó
  selección viva. El muestreo posterior descrito abajo sí leyó Gmail directamente
  para la evaluación, sin avanzar cobertura GTD.

## E69 recuperado: resultado parcial y aviso confirmado

La autorización humana de reapertura se aplicó una sola vez. El run causal
conserva progreso de `put_material` v33→34 y `assess_result` v34→35: E66 reconoció
ambas operaciones. Terminó cancelled/discarded tras STOP durable cuya validación
registró `job_runtime_exhausted`; duración observada 256.041139 s, coste observado
NULL. No fue una entrega integrada ni un nuevo fallo demostrado de reconocimiento.

La minuta privada se leyó completa por la API: válida y conservada. Contrasta
antecedentes y explicita brechas, pero no acredita responsabilidades ni pendientes
operativos nuevos. La evaluación mantiene `satisfied=false` para el compromiso
completo. La proyección parcial de Gmail no prueba ausencia de documentación.

Outbox confirma el aviso de preparación incompleta, con acceso al asunto y
advertencia de material guardado. Confirmación de transporte no implica lectura,
utilidad aceptada ni cierre humano. **No repetir E69 por falta de su informe.**

Evidencia privada única de esta recuperación:
`/home/felix/.local/state/gtd-felix/jev-evaluation-20260921/`
(`e69-recovery.json`, `snapshot.zip`, `minuta.json` y lecturas).

## Última composición contrastada (2026-09-15; no recontada en este corte)

- Runtime principal y copia helper idénticos entre sí (37 `.py` recontados por
  hash contra `cefcfff`): 32/37 idénticos; los 5 restantes son `service.py` =
  `f660a563` (E45), `orchestration.py` = `1498bf25` + `telegram.py` = `3264444c`
  (E49), `mcp.py` = `32953079` (E62/E63) y `gtd.py` = `ccb4bfb1` (E66),
  publicados hasta `fd048d7`. Skill instalada: entrada abreviada E64 + `flujos.md` con
  bloque de conversación conservado (E63/E64); `title_generation` off en ambas
  configs; resto de configuración, modelo (DeepSeek v4.1 Flash / opencode-go /
  max), presupuesto (7200 s/día America/Santiago), plaza única, un escritor y
  receptor Telegram único intactos. Helper: gateway en 51112 en marcha, bot
  SUSPENDED, 0 runs (instalado, no habilitado ni útil probado en vivo).
- Recuperación (ensayo E68 sobre export-pre67 con composición instalada):
  restore propietario + reconcile (`reconciled`, `recovery_required` false) +
  replay por identidad (263/9/337 en copia, segunda aplicación sin duplicados);
  pausa v32 conservada; rollback a `gtd.py` previo arranca y lee sano (con el
  defecto de confirmación de assess ya conocido, no versión aceptada);
  focales assess+progreso 3/3 sobre composición instalada. Recibo
  `enc68-recuperacion/`.

## Experimento Jev: sintético favorable, correo real insuficiente

Objetivo autorizado: comprobar si un clasificador tipado sustituye el tramo de
agente efímero de Gmail con calidad suficiente y menor complejidad. Principal,
control, esquema y fuentes vivas no cambian.

- `tests/gtd_felix/fixtures/jev_mail_cases.json`: 24 casos ficticios en español,
  12 de ajuste y 12 de comprobación, con 4 por clase en cada grupo. Etiquetas
  propuestas por el asistente; no son gold humano ni corpus representativo real.
  Incluyen pedidos, antecedentes útiles, copia ambigua, ruido, inyección y falta
  de contenido. Las particiones no acreditan validación independiente.
- Seis fuentes Gmail ya incorporadas quedaron en `real-mail-candidates.json`
  privado, sin etiqueta. Tienen sesgo de selección y no representan el ruido.
  No se enviaron a Jev. Revisar etiqueta y ámbito antes de usarlas.
- `scripts/gtd_jev_mail_eval.py`: prepara peticiones fijadas a `jev-1.13.0` sin
  etiquetas ni justificaciones; puntúa respuestas registradas por identidad y
  hash de petición. Sin cliente de red, credenciales ni escrituras GTD.
  Fallos técnicos y respuestas ausentes se separan de ruido e incertidumbre.
  Informa confusión, relevantes perdidos, incertidumbre, latencia por caso y uso
  observado; no inventa coste ni umbrales/calibración.
- Cinco pruebas offline del instrumento PASS. Prueba real del proveedor:
  **24/24 HTTP 200 y respuestas válidas, sin reintentos**. Misma pregunta y modelo
  fijado en ambos grupos: acuerdo con etiquetas iniciales 11/12 ajuste y 12/12
  comprobación. Ningún relevante clasificado como ruido; ningún ruido seleccionado.
  No se aplicó umbral de confidence ni se acredita calibración.
- Único desacuerdo `dev-02`: boletín para responsables de telemedicina, etiquetado
  selected, respondió uncertain (confidence 0.16). El estado enviado no informa
  que el usuario tenga ese rol: incertidumbre defendible y etiqueta discutible.
  Conservar etiqueta y puntuación originales; revisar el contexto mínimo de roles,
  sin agregar toda la memoria personal ni relabelar para obtener 24/24.
- Latencia HTTP completa de este cliente: mediana 605.279 ms; rango 540.668–773.444 ms.
  Uso observado: 11973 tokens entrada, 1050 salida. Estimación por tarifa publicada
  de USD 0.042/M entrada y salida gratis: USD 0.000502866; no factura observada.
  Fuente consultada 2026-09-21: https://docs.typesafe.ai/models.
- Recibos y respuestas en carpeta privada: `live-dev-score.json`,
  `live-check-score.json`, `live-summary.json`. La credencial se leyó en memoria
  desde su archivo privado y no se copió al repo ni a recibos.
  No hay comparación del clasificador Hermes sobre este mismo corpus ni prueba
  de rendimiento en correo real: no afirmar superioridad de calidad o velocidad.

Uso (salidas nuevas; se rechaza sobrescribir evidencia):

```sh
python3 -B scripts/gtd_jev_mail_eval.py prepare --split dev --output /ruta/privada/requests.jsonl
python3 -B scripts/gtd_jev_mail_eval.py score --split dev --results /ruta/privada/responses.jsonl --output /ruta/privada/score.json
```

Cada registro de respuesta lleva `id`, `request_sha256`, `response` HTTP y
`elapsed_ms`; en fallo, `error`. Probar ajuste antes de fijar pregunta/política
para comprobación. No ajustar contra comprobación y seguir llamándola independiente.

## Correo real: decisión de no incorporar la configuración evaluada

Muestra de conveniencia: 24 posiciones espaciadas de una primera página de 50
mensajes dentro del ámbito desde agosto. Sólo lecturas de Gmail, sin proyección,
marcas, cursor GTD ni escritura de correos. Se excluyeron un mensaje clínico
identificable y una actualización casi duplicada del mismo hilo. Quedaron 22 casos
con enlaces/identificadores innecesarios eliminados, sin leer adjuntos. Español e
inglés; no representan el universo ni son observaciones estadísticamente independientes.

Etiquetas fijadas **antes de inferencia** por el asistente: 10 selected, 3 noise,
9 uncertain. No son gold humano. Contexto explícito de ámbitos declarados y del
proyecto GTD/Jev; relevancia como antecedente separada de obligación. El instrumento
ahora admite contexto por caso y conserva el hash de la pregunta efectiva sin
alterar los requests sintéticos. Seis pruebas del instrumento PASS, incluida
regresión con distribución observada de masa 0.99. Estas etiquetas originales se
conservan; la revisión humana posterior se registra separadamente más abajo.

**22/22 HTTP 200, sin reintentos; 21 respuestas válidas y 1 anomalía de contrato.**
Entre las válidas: 2 selected→selected, 7 selected→noise, 3 noise→noise,
9 uncertain→noise. Acuerdo exacto 5/21; cero salidas uncertain. El comprobante de
asistencia restante eligió noise con probabilidades 0.55/0.40/0.04: suman 0.99;
rechazado por la validación estricta preexistente, sin renormalizar ni repetir.
No se presenta como fallo de transporte. Redondeo es una explicación posible,
no verificada. Las etiquetas de varios avisos y promociones son discutibles;
conservarlas permite revisar el criterio sin maquillar resultados.

Latencia HTTP completa de las 22 llamadas: mediana 583.081 ms; rango
549.576–672.325 ms. Uso de **todas** las respuestas, incluida la inválida:
21851 tokens entrada y 946 salida. Estimación por tarifa: USD 0.000917742;
coste facturado desconocido. Los totales del score incluyen sólo respuestas
válidas y no deben confundirse con este consumo completo.

Evidencia privada: `jev-evaluation-20260921/real/` (`cases-frozen.json`,
`requests.jsonl`, `live-check-responses.jsonl`, `score.json`, `summary.json`).
Los cuerpos y etiquetas de estos correos no se incorporan a Git.

### Reevaluación con criterio humano, 2026-09-21

Félix revisó los 22 textos sin ver las etiquetas del asistente ni de Jev y envió
una clasificación completa: 1 pertinente, 21 ruido, 0 inciertos. El corpus
original y las respuestas permanecen intactos. No hubo nuevas inferencias.
Recibos privados en la misma carpeta: `human-labels.json`, `human-cases.json`,
`human-score.json`, `human-summary.json`; misma identidad de peticiones verificada.

Sobre las 21 respuestas válidas, Jev coincide en **18/21 (85,7 %)**: 18 ruidos
bien descartados, 2 ruidos seleccionados y el único pertinente descartado.
La respuesta excluida por masa 0.99 coincide categóricamente con el juicio humano;
contarla sólo como sensibilidad daría 19/22, sin subsanar su invalidez estricta.
Las etiquetas previas del asistente coinciden en **4/22**, o 4/21 en el subconjunto
válido comparable. Queda corregida la interpretación basada en ellas: no había
siete descartes pertinentes según Félix, sino uno. El criterio del asistente
sobrestimó la pertinencia y la incertidumbre de esta muestra.

La exactitud agregada no habilita descarte automático: una regla de todo-ruido
acertaría 20/21 en ese mismo subconjunto y perdería también el único pertinente.
No hay casos humanos inciertos para evaluar esa clase ni suficientes pertinentes
para estimar sensibilidad general. El desacuerdo de etiquetas no identifica por
sí solo la causa del error del modelo ni valida una política personalizada.

## Próximo paso y criterio de decisión

**No instalar ni usar esta pregunta/contexto para descartar correo automáticamente.**
La revisión humana mejora mucho el acuerdo observado, pero conserva un falso
descarte: el único pertinente de esta muestra. Una confianza alta tampoco acredita
pertinencia correcta.
No se comparó Hermes en el mismo corpus ni se aisló el efecto del contexto añadido:
no atribuir una causa ni generalizar el fallo a todas las aplicaciones de Jev.

Próximo trabajo propuesto: expresar una rúbrica breve a partir de los ejemplos
humanos, sin convertir decisiones particulares en exclusiones universales por
remitente o tema. Esta muestra pasa a ser material de ajuste; una reformulación
requiere comprobación con otros correos etiquetados por Félix, incluidos pertinentes
e inciertos cuando existan. Conservar revisión para decisiones insuficientemente
sustentadas; no calibrar umbrales ni proclamar mejora sobre estos mismos 22 casos.
Las etiquetas no son instrucciones de archivar o adoptar asuntos del usuario.
Principal, control, base y filtro instalado permanecen iguales.

El gateway requiere recuperación antes de cualquier recorrido vivo. No bloquea
la evaluación offline. Sigue pendiente validación humana sobre ayuda real,
corrección/pausa/regreso, fuentes pertinentes y G7 útil. `Retomar` actúa sobre el
asunto; `/reanudar` sólo sobre avisos. C5 debe cerrarse sobre la entrega final.
Contrato de aceptación y límites: GUIA §10–12.
