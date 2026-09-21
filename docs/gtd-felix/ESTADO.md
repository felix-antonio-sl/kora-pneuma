# GTD de Félix · estado actual

Corte de continuidad **2026-09-21**. Lecturas por API y exportación consistente;
SQLite consultada sólo en copia privada. Sin instalación, inferencia ni envíos
provocados por este corte. `candidates/` y `versions/` se preservan sin seguimiento.

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
  4 pendientes de lectura, último código `cycle_not_active`. No se volvió a
  consultar Google ni a ejecutar selección desde este encargo.

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

## Experimento Jev: preparación offline, sin incorporación

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
- Cinco pruebas offline del instrumento PASS. No son pruebas de calidad de Jev.
  Requests preparados en la carpeta privada; inferencia real NOT_RUN.

Uso (salidas nuevas; se rechaza sobrescribir evidencia):

```sh
python3 -B scripts/gtd_jev_mail_eval.py prepare --split dev --output /ruta/privada/requests.jsonl
python3 -B scripts/gtd_jev_mail_eval.py score --split dev --results /ruta/privada/responses.jsonl --output /ruta/privada/score.json
```

Cada registro de respuesta lleva `id`, `request_sha256`, `response` HTTP y
`elapsed_ms`; en fallo, `error`. Probar ajuste antes de fijar pregunta/política
para comprobación. No ajustar contra comprobación y seguir llamándola independiente.

## Próximo paso y criterio de decisión

Confirmar acceso/cuenta TypeSafe y ámbito de datos; realizar una comparación
acotada cuando corresponda, empezando por los ficticios. No se presume autorización
para trasladar correo privado a otro proveedor por la autorización previa de Muse.
Revisar errores por clase, en especial relevante→ruido, y coste/latencia completos.
Una muestra pequeña sirve para descartar problemas y decidir continuar; no prueba
fiabilidad universal. No admitir umbrales por intuición ni adoptar Jev sólo por
JSON válido. Si aporta, sustituir el evaluador conservando autoridad, vigencia,
consumo y cobertura; retirar mecanismo desplazado. Si no aporta, cerrar prueba.

El gateway requiere recuperación antes de cualquier recorrido vivo. No bloquea
la evaluación offline. Sigue pendiente validación humana sobre ayuda real,
corrección/pausa/regreso, fuentes pertinentes y G7 útil. `Retomar` actúa sobre el
asunto; `/reanudar` sólo sobre avisos. C5 debe cerrarse sobre la entrega final.
Contrato de aceptación y límites: GUIA §10–12.
