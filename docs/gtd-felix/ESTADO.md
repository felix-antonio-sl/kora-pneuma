# GTD-Félix · estado desde el corte 2026-09-22

**Base de desarrollo conservada:** `af0a0239b1579d9794791365b70b63060fe0eabf`.
**Referencia de corte:** `gtd-felix/corte-2026-09-22`, sobre el commit de esta
reorganización. **Producción personal todavía no aceptada.**
[GUIA.md](GUIA.md) gobierna alcance, arquitectura, recorrido y aceptación.

## Posición verificable

- Checkout `/home/felix/lab/kora-gtd-felix`, rama `fxai/gtd-felix-20260911`.
  Base previa al commit de corte: ocho commits sobre la referencia local
  `origin/fxai/gtd-felix-20260911`; no se consultó el remoto para este corte.
- `candidates/` y `versions/` sin seguimiento, preservados. Sin migración, borrado,
  reinicio, escritura de dominio ni llamada de inferencia durante la reorganización.
- Esquema fuente v4, 13 tablas, leído en `store.py`. Este dato describe el código;
  no se abrió la DB viva para verificarla en este corte.
- No se ejecutaron tests, experimentos, canarios ni comparaciones de proveedor.
  Revisión de fuentes/documentos y estado systemd; no acredita el recorrido humano.

## Declarado, implementado y observado

| Parte | Código/contrato | Instalación y evidencia disponible |
|---|---|---|
| Registro, control y resultados | Servicio único, ciclos/intentos, materiales/evaluaciones/deliveries, esquema v4 | Instalados según recibos anteriores; unidad GTD running el 22. No se recontaron hashes ni se acredita salud integral por systemd |
| Principal Hermes | Preparación, herramientas, integración y devolución | **Gateway en auto-restart el 22; impedimento actual**. Causa no diagnosticada en este corte |
| Jev | Decisor tipado por defecto elegido por Félix; cliente, Gmail, `gtd_decide`, API/MCP/guard e instrucciones en `af0a023` | **No instalado.** Sólo revisión estática previa; no afirmar conducta observada de la nueva integración |
| Google | Adquisición selectiva, identidad/revisión, cobertura e invalidación en código | Última lectura API del 21: calendarios completos, Gmail degradado con 4 pendientes y `cycle_not_active`; no reconsultado el 22 |
| Material útil | Existe preparación parcial y conservación de material en recorridos previos | No hay todavía un recorrido completo aceptado por Félix; material guardado no equivale a entrega integrada |
| Helper G7 | Incorporación y mandato acotados implementados | Gateway running el 22; bot SUSPENDED y 0 runs según último recibo, no revalidados hoy. Utilidad delegada no acreditada |
| Recuperación | Export/restore, replay y reconciliación existentes | Evidencia histórica en copias; debe corresponder a la composición final para cerrar C5 |

Observación de unidades el **2026-09-22, 18:38:57 UTC** (hora exacta en
recibo privado): GTD PID 3048478, 0 reinicios; gateway principal MainPID 0,
auto-restart, contador 43824; helper PID 3868393, running, 1 reinicio.
No hubo consulta nueva a `/health`, presupuesto o pausas: los saldos y posiciones
del 21 no se presentan como actuales. No se cambiaron unidades ni configuración.

## Evidencia que se conserva sin convertirla en plan

- E69: recuperado por API/export el 21. Minuta parcial válida; evaluación negativa
  del objetivo completo; run cancelado/descartado por límite y aviso Telegram
  confirmado. No repetirlo por faltar un reporte ni reabrir su asunto por este corte.
- Jev: 24 peticiones sintéticas y 22 correos reales anteriores. Félix etiquetó
  1 pertinente y 21 ruido; acuerdo 18/21 respuestas válidas, único pertinente
  descartado, 2 falsos seleccionados y 1 distribución inválida. Mis etiquetas
  iniciales coincidieron sólo 4/22. Resultados intactos, sin nueva inferencia.
  **La decisión posterior de adoptar Jev prevalece; no reabrir su elección.**
- Última composición contrastada del 15: 37 módulos principal/helper; 32 iguales
  a `cefcfff`, cinco sustituciones documentadas, más instrucciones. No equivale al
  HEAD actual; no copiar el repositorio entero encima sin identificar el conjunto.
  Detalle recuperable en `git show af0a023:docs/gtd-felix/ESTADO.md`.
- Evidencia privada: `/home/felix/.local/state/gtd-felix/corte-20260922/receipt.json`
  para este corte; `jev-evaluation-20260921/` para E69 y clasificación humana;
  `direccion-20260914/` para reportes y referencias a recuperación histórica E68.
  Consultar el detalle sólo cuando una decisión dependa de él; cuerpos y secretos
  permanecen fuera de Git.

## Trabajo activo: instalación coherente

**Resultado:** dejar accesible el bot con la composición que incorpora Jev,
captura/controles y recuperación conservados. Dueño: la sesión que tome el desarrollo;
un solo escritor/integrador. El corte actual prepara el encargo, no lo ejecuta.

1. Leer error efectivo y configuración del gateway principal y resolver su causa
   concreta. No atribuir al proveedor lo que sea un pin, entorno o dependencia;
   no actualizar a ciegas el checkout Hermes compartido ni tocar instalaciones ajenas.
2. Revisar el conjunto `af0a023` contra la composición realmente instalada:
   cliente Jev, selección Gmail, API, MCP, guard, instrucciones, exposición efectiva
   de herramientas y credencial del servicio. Conservar tipos, errores y autoridad
   al conectar las piezas. No nuevo diseño general ni campaña de evaluación.
3. Usar exportación, respaldo, corte y recuperación existentes; realizar el conjunto
   identificado respetando pausas y trabajos en vuelo. Sin reabrir asuntos ni
   provocar inferencia para fabricar una evidencia de instalación.
4. Dejar versión/configuración identificadas, controles/canal disponibles y límites
   explícitos. La primera inferencia posterior pertenece a un encargo real vigente.
   Actualizar aquí lo instalado y lo observado, sin prometer éxito del modelo.

Después: un asunto útil completo en Telegram; luego uso sostenido, G7 útil y
recuperación final. C1–C6 permanecen abiertos hasta su evidencia aplicable; C2/C6
necesitan uso/aceptación de Félix, C3 cobertura útil, C4 retorno, C5 composición final.
No pedirle al dueño acciones de validación hasta que ese recorrido esté disponible.
