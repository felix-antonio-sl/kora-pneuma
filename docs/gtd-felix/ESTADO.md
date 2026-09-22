# GTD-Félix · estado 2026-09-22

**Instalación coherente realizada; producción personal todavía no aceptada.**
[GUIA.md](GUIA.md) gobierna alcance y aceptación. Corte de continuidad
`gtd-felix/corte-2026-09-22` (`13bc6e8`), Jev en `af0a023`, corrección operativa
en `f71837e`; composición fuente instalada en `2e0e6e0`.

## Instalado y observado

Observación final del **2026-09-22, 19:22–19:24 UTC**. Checkout
`/home/felix/lab/kora-gtd-felix`, rama `fxai/gtd-felix-20260911`.
`candidates/` y `versions/` preservados. Sin migración de esquema.

| Parte | Estado y límite |
|---|---|
| Servicio GTD | Running, API propietaria disponible, cero trabajos en vuelo. Captura/consulta/controles ofrecidos por la misma instalación; no se envió captura sintética |
| Principal Hermes | Running, admisión `ready` sin errores, bot `available`. DeepSeek v4.1 Flash / OpenCode Go / max conservado |
| Causa del reinicio | El wrapper `gmail_bridge.py` rechazaba el checkout compartido: pin `5eb99eb…`, instalado `1a1f4a59e252e1dc0137e7b2e7bcc8b0381d19c4`. Log `gmail_bridge_runtime_mismatch`, antes de contactar proveedor |
| Corrección de arranque | Gateway usa CLI nativa Hermes `0.21.3`; no se modificó ni actualizó el checkout compartido. Gmail del servicio pasa directamente por Jev |
| Jev | Cliente, Gmail, API, MCP, guard, instrucciones y allowlists instalados como conjunto. `gtd_decide` incluido entre las cuatro herramientas admitidas; no se llamó al proveedor |
| Credencial | `LoadCredential=typesafe.env` sólo en la unidad GTD; `decisions.env_file` apunta a la copia privada de systemd. Formato/lectura local disponibles; clave ausente del entorno del proceso, perfiles y Git |
| Telegram | `getMe` confirma `@korax_kv_bot`; `getWebhookInfo`: sin webhook, cero updates pendientes, sin último error. Receptor ejecutándose; no se envió mensaje de prueba ni se consumieron updates desde otra herramienta |
| Helper G7 | Gateway running, bot sigue `suspended`, sin habilitación ni trabajo nuevo. Perfil actualizado y mandato acotado conservado; utilidad delegada sigue pendiente |
| Presupuesto | 7.200 s disponibles, cero consumo/reserva actual, una plaza, día America/Santiago. El reinicio no cambió la política |
| Fuentes | Selección Gmail preparada en Jev; cobertura útil nueva no observada. No se provocó revisión de dominio ni se reactivaron asuntos |
| Recuperación | Exports consistentes y dos paquetes privados: composición anterior e instalada. Creación/validación del empaquetador existente realizada; no ensayo de restore. El venv Hermes sigue como dependencia identificada del host |

La comparación de instalación informa **38 módulos iguales a la fuente en cada
perfil**, sin cambios nativos administrados ni recuperación KORA pendiente.
Los recibos anteriores estaban atrasados: 18 ediciones locales del principal ya
incorporadas en la fuente se conservaron en respaldo antes de reponer los bytes
registrados y aplicar el instalador. Tres recursos del principal y 41 del helper
se adoptaron con hashes y procedencia revisados. No hubo copia indiscriminada.
El SOUL privado del helper explicita `gtd_decide` sin permitir subdelegación.

## Incidente de disponibilidad resuelto en este incremento

Al recuperar el gateway, una consulta de estado tardó **19,26 s** y el servicio
consumía cerca de un núcleo. `_source_review_blocker` llamaba a `SourceSync.inspect`
por cada evento: hidrataba todos los objetos de la colección repetidamente para
253 revisiones bloqueadas por selección de fuentes.

`f71837e` limita la lectura al objeto y sus dos índices de identidad, preservando
partición, procedencia y rechazo por inconsistencia. Tras instalarlo, la consulta
operativa de salud respondió en **1,181 s** y las de bots, presupuesto, pendientes
y capacidades en aproximadamente **0,001 s**. Son observaciones puntuales del
servicio, no benchmark ni garantía de latencia. Las tres unidades permanecían
running y con cero reinicios desde el arranque final.

## Preservación y evidencia

- Los exports anterior/posterior conservan los **263 documentos de asuntos
  idénticos**, 43 intentos históricos y cero recibos Jev. No se cambiaron plazos,
  pausas, mandatos ni compromisos por este encargo de desarrollo.
- No se abrió SQLite viva con herramientas auxiliares. Inspección de datos sólo
  mediante API o copias extraídas de sus exports consistentes.
- No se ejecutaron tests, benchmarks, canarios ni solicitudes de inferencia.
  El arranque usó su descubrimiento operativo nativo, incluida la enumeración
  MCP; no ejecutó herramientas de dominio. `git diff --check` sin incidencias.
- Evidencia privada: `/home/felix/.local/state/gtd-felix/installation-20260922/`.
  `receipt.json`, `operational-final.json`, `installed-modules.json`,
  `domain-preservation.json`, recibos KORA y estados Telegram precisan el alcance.
  `RECUPERACION.md` explica uso y límites de los respaldos.
- `before-recovery.zip` conserva la instalación anterior; `installed-recovery.zip`
  conserva la composición instalada y su export. La anterior reintroduce el pin
  incompatible si se restaura literalmente: no es un fallback sano automático.
- El corte y la evaluación histórica de Jev siguen en Git y evidencia privada
  referida en `13bc6e8`. No constituyen una nueva cola de pruebas o decisiones.

## Incremento activo y siguiente acción

**Instalación disponible para comenzar un asunto útil completo.** Responsable:
la misma sesión integradora. Se invitó a Félix a enviar una intención real por
Telegram; se espera esa intención o su decisión de dejar el sistema listo.
No elegir un asunto antiguo ni crear un encargo para demostrar funcionamiento.

A partir de esa intención: observar preparación, primera llamada legítima a Jev,
material, integración y devolución; resolver corrección, pausa y regreso dentro
del mismo asunto, sin atribuir aceptación al silencio. Los procesos activos,
hashes e inventarios no acreditan ese recorrido.

C1–C6 y G1–G10 **siguen abiertos** hasta su evidencia aplicable. C2/C6 necesitan
uso y aceptación de Félix; C3 cobertura útil; C4 devolución efectiva; G7 un aporte
acotado útil. C5 tiene ahora paquetes identificados, pero no recuperación observada
de la entrega final ni reconstrucción completa del entorno Hermes. No se reabre
una campaña de tests para cerrar estos límites.
