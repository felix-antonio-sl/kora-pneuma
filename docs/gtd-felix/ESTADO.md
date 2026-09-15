# GTD de Félix · estado actual

Corte **2026-09-15 04:30 UTC** (06:30 CEST). Estado vigente; el historial queda
en Git y en recibos privados (`/home/felix/.local/state/gtd-felix/`).
Sin datos personales ni credenciales. `candidates/` y `versions/` sin
seguimiento se preservan.

## Veredicto

**Servicio operativo, piloto supervisado; producción personal no aceptada.**
Rama `fxai/gtd-felix-20260911`; código publicado hasta `fd048d7`; documentación según HEAD.
C1 operativo; C2–C6 abiertos. Aceptación humana: NOT_RUN.

## Instalado y verificado (observado 2026-09-15 04:29 UTC)

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
- Vivo: salud `ok`, PID de servicio posterior al reinicio E67 sin reinicios,
  budget diario 2026-09-15 active 0 / remaining 7200.0 s / committed 0.0 USD
  (imputación, no coste de proveedor medido), TM `5869a0bb` v32 **pausado por
  botón Telegram del dueño** (se respeta; recorrido pendiente de reapertura).
  Datos v4: 262 asuntos / 335 operaciones / 40 runs / 8 materiales /
  12 evaluaciones / 56 entregas.
- Recuperación (ensayo E68 sobre export-pre67 con composición instalada):
  restore propietario + reconcile (`reconciled`, `recovery_required` false) +
  replay por identidad (263/9/337 en copia, segunda aplicación sin duplicados);
  pausa v32 conservada; rollback a `gtd.py` previo arranca y lee sano (con el
  defecto de confirmación de assess ya conocido, no versión aceptada);
  focales assess+progreso 3/3 sobre composición instalada. Recibo
  `enc68-recuperacion/`.

## Qué puede usar Félix ahora

Captura y conversación por Telegram con identidad por asunto, corrección que
versiona, pausa/regreso, materiales y devoluciones; agenda de calendarios
principal + feriados. Presupuesto y plaza visibles para dirección.

## Qué NO está acreditado

- Minuta TM (`5869a0bb` v32, pausado por el dueño): 8 materiales en
  inventario del asunto, sin minuta del principal; E27/E32 sin entrega.
  M64 (sintético) acredita material + relectura por el agente; M65 añade
  evaluación persistida con fallo de confirmación, reparado offline e
  instalado (E66/E67). Sin autoría global comprobada. C2 NOT_RUN.
- Gmail: cobertura no acreditada (sin recorrido reciente; no se declara sana,
  caída ni ausente). Fallback de lectura instalado; 4 pendientes históricos.
- Inferencia útil del proveedor: M64/M65 muestran generación real con frenos
  de envolvente y guarda; sin recorrido vivo que la acredite como útil.
- Coste monetario del proveedor: desconocido (telemetría NULL).
- G7: instalado-suspendido, útil en vivo no probado. El botón de pausa
  observado no acredita UX ni aceptación.

## Recorrido humano mínimo (listo, sin ejecutar)

Si Félix quiere continuar: Félix autoriza reapertura o usa Retomar
(botón verificado de ficha pausada, `telegram.py`); dirección confirma estado
y coordina UNA causa de trabajo para tramo E67, evitando duplicación →
primera minuta TM por el bot → corrección con palabras propias →
pausa/reingreso con los mismos controles. `/reanudar` sólo reanuda avisos,
no reabre el asunto ni admite trabajo solo. Controles reales verificados en
código: `pause`/`reopen` del dueño, `apply_human_instruction` con cita,
`request_review` del principal, guarda STOP 240 s + sondeo, aviso único E49.
Antes de la reapertura, ninguna inferencia de este frente. Sin preguntas
nuevas al usuario desde el sistema.

## Referencias de evidencia vigente

Recibos E62/E64/E66/E67/E68, reportes `direccion-20260914/`, composición
instalada arriba. El resto es historia en Git; no otra crónica aquí.
