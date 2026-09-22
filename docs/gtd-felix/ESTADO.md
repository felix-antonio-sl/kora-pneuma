# GTD-Félix · estado 2026-09-22

**Instalación coherente realizada; producción personal todavía no aceptada.**
[GUIA.md](GUIA.md) gobierna alcance y aceptación. Corte de continuidad
`gtd-felix/corte-2026-09-22` (`13bc6e8`), Jev en `af0a023`, corrección operativa
en `f71837e`; composición inicial `2e0e6e0`, seguida de la corrección
de credencial `a563304` observada durante el primer recorrido real.

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

## Primer recorrido real y corrección de instalación

Félix envió una intención real por Telegram el 22, a las 19:52 UTC. Captura durable
y acuse observados; el principal preparó un material privado en un asunto derivado
y la devolución sustantiva fue confirmada por Telegram. El primer intento terminó
y quedó integrado tras 228,67 s. Esto acredita preparación y transporte, no aceptación.

La primera selección real de Gmail y el posterior juicio tipado quedaron
indisponibles: `LoadCredential` entrega la clave en **0400**, pero `read_private`
exigía exactamente **0600**. La observación anterior de archivo montado y formato
presente no acreditaba que el cliente pudiera leerlo. `a563304` admite 0400/0600
sólo para la credencial Jev y conserva dueño, archivo regular, ausencia de enlaces
y privacidad. Los demás lectores conservan 0600. Instalado en ambos perfiles;
servicio reiniciado después de confirmar cero trabajos en vuelo. Sin inferencia
artificial para probarlo: éxito de proveedor todavía no observado.

La continuación automática de evaluación agotó su reserva: 245,53 s observados,
STOP confirmado e integración descartada; el límite nativo es cooperativo.
Conservó el material anterior y envió un aviso de revisión incompleta. No se
amplió presupuesto ni se lanzó otro intento por la reparación. La secuencia de
«material listo» y aviso de preparación incompleta puede resultar confusa: el
material existe, pero no quedó evaluado como suficiente.

Límites del primer material: regla de colación aún no confirmada; un límite
horario descrito ambiguamente; `source_versions` vacío pese a citar correos;
revisión nueva de Gmail fallida, que no demuestra ausencia de antecedentes.
No cerrar C3/C4 ni declarar utilidad aceptada sobre esa base.
Evidencia privada y exports propietarios del recorrido en
`/home/felix/.local/state/gtd-felix/weekly-hours-20260922/`. El paquete de instalación
anterior sigue conservado; los exports nuevos preservan material y entregas,
sin acreditar recuperación de esta nueva composición completa.

## Incremento activo y siguiente acción

**Un asunto útil completo sigue activo.** Responsable: la misma sesión integradora.
Félix ya precisó la colación incluida, presencia diaria en ambos servicios y
preferencia por HODOM al inicio/final y telemedicina al centro. La captura quedó
separada y agotó 248,25 s sin material: leyó antecedentes e intentó una edición
lateral al final; el servicio rechazó por presupuesto agotado. No atribuir el
fallo a falta de información del usuario.

El botón «Revisar ahora» sí registró la solicitud. Su recibo aplicado no contiene
`item`, y el presentador lo trataba como rechazo: aviso corregido en `8663e05`.
Ese cambio también prioriza en las instrucciones la ruta existente de captura
a asunto, y guardar material útil con límites antes de ampliar fuentes. Instalado
en ambos perfiles, 38 módulos coincidentes; servicio reiniciado sin jobs pendientes.
Sin tests ni inferencias artificiales; la conducta futura de la instrucción no
queda acreditada por su instalación.

La sesión integradora recuperó la precisión mediante `clarify` autenticado como
dueño, con cita literal y destino original: conserva la captura como ruteada,
sin compromiso duplicado. El servicio admitió revisión del destino con esa fuente
en su reserva. Esta recuperación asistida no acredita todavía la vinculación
autónoma de futuras correcciones.

Durante la revisión real anterior sí hubo selección Gmail válida de Jev tras
la reparación de la credencial (respuestas con fuentes seleccionadas y uso del
proveedor). Esto supera el límite anterior de cero respuestas válidas, pero no
acredita cobertura completa del correo ni resultado útil de toda la ejecución.

La revisión ruteada terminó e integró material v2 en 221,55 s; Telegram confirmó
su entrega. La continuación automática guardó v3 con cuatro dependencias de
correo, obtuvo juicio Jev favorable y cerró la preparación en 193,57 s. Esto
acredita ejecución/registro del juicio, no su suficiencia epistemológica ni
aceptación humana. Se preservan versiones anteriores y recibos privados.

Dos límites observados en esa salida requieren conservar el juicio crítico:

- Al guardar v2, el modelo confundió `item.version=2` con `source_revision=1`
  de la precisión ruteada y, tras el rechazo, omitió esa dependencia. V3 conserva
  cuatro correos pero tampoco la fuente humana en `material.source_versions`;
  la fuente sigue vinculada al asunto y a los jobs. `7c26a08` aclara esa unidad
  en schema e instrucciones y exige corregir el número, no retirar la fuente.
- V3 infiere actividad sincrónica al mediodía a partir de horas de interconsulta.
  Ese dato no lo demuestra. El resumen enviado a Jev omitió esa inferencia y el
  juicio favorable no la contrastó. `c5f24a0` exige contrastar las afirmaciones
  con pasajes de fuente y conservar posibles refutaciones. No hay nueva
  inferencia artificial que acredite la conducta posterior.

La sesión preparó un material privado revisado, con la aritmética y el horario
útiles, imputación de colación explícita y sin esas inferencias:
`weekly-hours-20260922/recomendacion-horario-revisada.md` bajo el directorio privado
de evidencia indicado arriba. Está fuera de Git y aún fuera del registro de
materiales GTD: no presentarlo como v4 ni como una entrega del bot. El asunto
figura `done` por su evaluación automática, no por aceptación de Félix.

Siguiente trabajo: integrar correcciones de fundamento y dependencia en la
continuidad del material, sin confundir juicio favorable con verificación de
fuentes; después observar pausa/regreso cuando Félix los use. No reiniciar
tentativas agotadas ni reabrir asuntos ajenos. La recuperación asistida de esta
entrada no acredita todavía el recorrido autónomo de futuras correcciones.

C1–C6 y G1–G10 **siguen abiertos** hasta su evidencia aplicable. C2/C6 necesitan
uso y aceptación de Félix; C3 cobertura útil; C4 devolución efectiva; G7 un aporte
acotado útil. C5 tiene ahora paquetes identificados, pero no recuperación observada
de la entrega final ni reconstrucción completa del entorno Hermes. No se reabre
una campaña de tests para cerrar estos límites.
