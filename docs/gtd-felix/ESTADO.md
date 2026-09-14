# GTD de Félix · estado actual

Corte **2026-09-14 ~21:20 UTC**. Este archivo describe el estado vigente;
el historial queda en Git y en recibos privados
(`/home/felix/.local/state/gtd-felix/`). Sin datos personales ni credenciales.
`candidates/` y `versions/` sin seguimiento se preservan.

## Veredicto

**Servicio operativo, piloto supervisado; producción personal no aceptada.**
Rama `fxai/gtd-felix-20260911` en sync con remoto. C1 operativo; C2–C6
abiertos. I1/I2 publicados e instalados en su momento; I3 publicado
(`7bc1fe8`) e instalado con datos v4 y `migration:i3`. Encima van los
parches revisados E17 (control/fronteras de error), E26 (fallback Gmail) y
E28–E31 (vigilancia temporal del run). Aceptación humana: NOT_RUN.

## Instalado y verificado

- Runtime: 37/37 `.py` instalados idénticos a HEAD `cefcfff`, sin diferencias
  ni archivos sin origen git. Pin Hermes `5eb99eb`, gateway estable,
  DeepSeek v4.1 Flash / opencode-go / max, 7200 s/día America/Santiago,
  plaza única, un escritor, receptor Telegram único.
- Vivo (sólo lectura, ~21:15 UTC): salud `ok`, `pending` 0, committed
  1881.06 s con imputación contable 6.0 USD (**no** es coste de proveedor
  medido), remaining 5318.94 s, `cost_control` false.
- Datos (export `enc39-recuperacion/export-e39.zip`, 7 626 918 B,
  `55e17bf8…66b7`): esquema v4, 261 asuntos / 332 operaciones / 405 eventos /
  300 originales / 8 materiales / 12 evaluaciones / 52 entregas confirmadas /
  39 runs / 1232 observaciones / 39 ciclos / 258 decisiones de fuente
  (+3 standalone en el marcador); 38 registros `hermes:state:*` (solo 1 con `first_send_at`/`native_admitted_at`; el ensayo prueba conservación de estados, no recuperación de plazo incierto — esa conducta la cubren las suites temporales 156/156); outbox vacío;
  `recovery_required` false.
- Recuperación de esta composición, ensayada en aislamiento (E39,
  `enc39-recuperacion/rehearse-e39.py`, runtime instalado): restore real
  marca `recovery_required`; comando no-owner rechazado; delta exacto por PK
  (17 filas) con originales/bytes/decisiones/marcador/entregas/anclas
  idénticos; segunda aplicación mueve 0; replay `already_applied`;
  `reconcile` owner real deja `reconciled`. PASS sin desvíos.
- Guardas vigentes: suites focales 156/156 (Hermes/control/diaria/gasto) y
  91/91 (fuentes/selección/monitor/evaluación) sobre este código.
- Paquete repetible: `enc39-recuperacion/paquete-composicion-actual.md`
  (instalación, recuperación, rollback coherente, límites del operador).

## Qué puede usar Félix ahora

Captura y conversación por Telegram con identidad por asunto, corrección que
versiona, pausa/regreso, materiales y devoluciones; agenda de calendarios
principal + feriados al día. Presupuesto y plaza visibles para dirección.

## Qué NO está acreditado

- Minuta TM (`5869a0bb` v31): sin material del principal; recorridos E27/E32
  terminaron sin herramientas ni entrega (protección temporal sí funcionó:
  STOP medido, slot libre).
- Gmail: 4 lecturas pendientes (`selection_unavailable`, degradado
  preexistente). El fallback de lectura funciona para los 2 gigantes
  probados (texto + manifiesto, adjuntos sólo referenciados); la cobertura
  global sigue incompleta y la selección real por el principal no ocurrió.
- Inferencia útil del proveedor: bloqueada en la práctica. E38 (200 con
  headers ~1.1 s, primer byte 14 B a ~13 s, ningún evento hasta deadline
  80 s) sitúa el síntoma en fase cuerpo/eventos incluso con prompt mínimo;
  causa interna no determinada; fin de la campaña de sondas.
- Coste monetario del proveedor: desconocido (telemetría NULL; las cifras en
  USD son imputación conservadora). Mantenimiento E34 (~1 s ×2) + E37 (~1 s)
  + E38 (~80 s) va por recibo separado, fuera del contador de jobs.

## Afirmaciones retiradas (sustituidas con referencia)

- «Stalls específicos de payload 12–18k» (E34): refutada como específica;
  E38 muestra silencio también con prompt mínimo. Queda: fase lenta en
  cuerpo/eventos, causa sin determinar.
- «400 determinista / 0 tokens» (E34): el 400 de E37 fue `MissingSessionID`
  de la sonda sin cabecera de sesión; E38 con sesión propia obtuvo 200.
  Tokens nunca medidos: se declara desconocido, no cero.
- «400 no es auth» (E35): la inferencia desde el 401 del código cliente no
  universaliza; la causa del 400 de E34 sigue desconocida.

## Criterios y trabajo pendiente (I4/G7)

| Criterio | Estado | Evidencia / siguiente paso |
|---|---|---|
| C1 continuidad | Operativo | Captura/identidad/presupuesto/recuperación conservados; ensayo E39 PASS |
| C2 recorrido humano | Parcial | Principal real aún sin entrega útil; controles listos, inferencia bloqueada |
| C3 fuentes | Parcial | I3 + fallback instalados; 4 pendientes Gmail; sin selección real del principal |
| C4 retorno cotidiano | Parcial | Pendiente de un recorrido real con salida útil |
| C5 recuperabilidad | Parcial (técnica) | Restore+reconcile ensayados sobre la composición actual; rollback coherente documentado, no ejecutado |
| C6 aceptación | Abierto | Requiere reconocimiento explícito de Félix; nada lo sustituye |
| G7 delegar | Paquete E42 ensayado (36/36), listo para decision, NO instalado | Auxiliar distinto probado (E41); aplicar/revertir endurecidos y ensayados sobre copias (idempotencia, parciales, auth MCP, suspendido, adaptador); perfil efectivo en destino aislado con discover compatible; `local_work` minimo por contrato. Propuesta: instalar perfil+config+bot SUSPENDED sin LLM; habilitar recorrido bajo orden aparte. E41 dry-run no era validacion completa. Falta orden e inferencia disponible |

I4 = primer encargo útil del principal con fuentes y retorno sostenido;
bloqueado hoy por inferencia sin salida; sin defecto determinista adicional demostrado que lo explique (no exclusión universal del runtime). I5 = este paquete +
aceptación. Próximo recorrido humano (sólo cuando la inferencia vuelva a
producir salida; no solicitarlo ahora): pedir al bot el estado de un asunto
propio y una preparación acotada; dirección observará material, cobertura y
devolución sin reintentos automáticos.
