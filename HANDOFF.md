# Continuidad de desarrollo de GTD-Félix

Preparado el **2026-09-20**. Puente temporal para otra sesión; retirar cuando se
haya absorbido lo pendiente en el estado propietario. No constituye otra guía.

## Propósito y fuentes

Terminar la puesta en producción personal de GTD-Félix: que Félix pueda dejar
una intención, recibir preparación útil, corregir, pausar y volver con contexto
vigente desde Telegram. Un usuario, un host personal y un desarrollador.
El resultado suficiente es ayuda cotidiana utilizable y recuperable.

Lee `AGENTS.md`, [ESTADO](docs/gtd-felix/ESTADO.md) y las partes pertinentes de
[GUIA](docs/gtd-felix/GUIA.md), especialmente §10–12. GUIA conserva el contrato;
ESTADO conserva hechos, brechas y próximo paso. No reconstruyas los 69 encargos
ni conviertas su numeración en el método de desarrollo.

## Punto de partida comprobado al preparar esta transición

- Checkout: `/home/felix/lab/kora-gtd-felix`, rama
  `fxai/gtd-felix-20260911`. HEAD y referencia local de upstream coinciden en
  `e528313ec521fae566407bee6c5bedd7c31af326`; no se consultó el remoto por red.
  Antes de editar este handoff, tracked limpio. Preservar `candidates/` y
  `versions/` sin seguimiento.
- ESTADO contiene un corte del **2026-09-15**, anterior al último recorrido.
  Sus PID, salud, saldo y pausa no son observaciones actuales del 20 de septiembre.
  No se consultó el servicio vivo durante esta transición.
- Última instalación documentada: datos v4; E66 corrige el reconocimiento del
  progreso de una evaluación usando stubs de filas canónicas. Conserva la
  guarda de versiones. Entrada de skill abreviada con obligaciones en referencias,
  herramientas con errores legibles y generación auxiliar de títulos desactivada.
- Modelo principal documentado: DeepSeek v4.1 Flash vía OpenCode Go, razonamiento
  max. Una ejecución global y presupuesto de 7200 s/día, America/Santiago.
  Auxiliar instalado pero SUSPENDED; utilidad real de delegación pendiente.
  Muse Spark Contributor está autorizado como alternativa, incluso para datos
  reales; esa autorización no equivale a tenerlo instalado ni a una orden de cambio.
- Producción personal **no aceptada**. Ensayos sintéticos y restauración tienen
  evidencia; uso humano, utilidad y recorrido completo todavía requieren cierre.

## Novedad decisiva: recuperar E69 antes de cualquier nueva ejecución

Félix respondió expresamente **«autorizo»** a reanudar el mismo asunto para el
tramo de Telemedicina de E67. Esa autorización supera la espera de E68 en ese
alcance; no volver a solicitarla. Una instrucción humana posterior incompatible
sí prevalece.

Se inspeccionó la tarea ejecutora y las salidas de su último turno:

- Tarea `01a09df2-0dcb-7e30-92fd-59e5a8355a0c`: idle; turno E69
  `01a0a358-8a5c-7d91-ba58-1159fd7361c9`: **interrupted**.
- La operación de reapertura respondió `applied`; el asunto pasó de pausado v32
  a activo v33. Un sondeo posterior mostró una ejecución activa.
- El último sondeo guardado mostró active 0, asunto activo v35, **9 materiales y
  13 evaluaciones**, frente a 8 y 12 al inicio. Apareció una minuta de Telemedicina
  con autor principal. Son salidas históricas de E69, no lecturas actuales.
- No se encontró el reporte de cierre E69. El sondeo no acredita por sí solo
  contenido útil, terminal nativo, integración, entrega por Telegram ni aceptación.
  Tampoco permite adjudicar todos los cambios sin revisar su causalidad.

La orden privada exacta conserva asunto, alcance, operación idempotente y límites:
`/home/felix/.local/state/gtd-felix/direccion-20260914/encargo-69-telemedicina-autorizada.md`.
El despacho está junto a ella en `despacho-encargo-69.json`.
**No reenviar esta orden ni iniciar otro run porque falte el informe.**

## Siguiente trabajo, en orden suficiente

Al comenzar la nueva sesión, recuperar contexto y comprobar el punto de partida
mediante lecturas. **Avisar a Félix cuando esté lista para partir**, antes de
modificar el producto o iniciar nuevas ejecuciones. El aviso debe indicar
brevemente qué se recuperó de E69, qué sigue pendiente y cuál será la primera
acción concreta. No confundir este aviso de preparación con aceptación del
producto ni convertirlo en una nueva solicitud de permisos ya concedidos.

1. Recuperar E69 mediante lecturas soportadas: asunto y procedencia, causa/job,
   terminal e integración, material completo, evaluación y delivery. Comprobar
   salud, trabajo activo y presupuesto actuales. Reconciliar el mismo run si
   corresponde; no recrearlo, reabrir otra vez ni sumar `request_review`.
2. Juzgar el material existente: fuentes y cobertura, responsabilidades
   respaldadas, pendientes y próximos pasos propuestos. Distinguir un corte
   parcial útil del cierre del compromiso completo. Verificar devolución normal;
   no escribir una minuta como operador para fingir éxito del agente.
3. Actualizar ESTADO con ese resultado y el próximo obstáculo concreto. Si ya
   hay entrega útil, pasar al recorrido humano de corrección, pausa y regreso.
   Si falla algo, reparar la causa demostrada con el menor cambio completo;
   una nueva inferencia necesita un propósito y una envolvente justificados,
   sin reintentos automáticos de la orden E69 agotada.
4. Cerrar lo pendiente de fuentes pertinentes y una delegación mínima útil
   según GUIA, aprovechando lo existente. No activar el auxiliar por rutina.
   Verificar recuperación sobre la composición final y dejar a Félix validar
   utilidad y aceptar el uso. Un fallo o una decisión humana bloquean sólo
   el trabajo que dependa de ellos.

## Disciplina de ejecución: cuatro límites

- **Antiburocracia:** medir avance por lo que Félix puede hacer y recibir.
  Una decisión, cambio o prueba debe resolver una necesidad identificable.
  Actualizar GUIA sólo si cambia el contrato y ESTADO cuando cambia un hecho.
  Evidencia privada mínima y localizable; no otra serie de matrices, puertas,
  planes, reportes numerados o revisiones ceremoniales para poder avanzar.
- **Anti sobreingeniería:** conservar la aplicación, SQLite propietaria, API,
  runtime nativo de Hermes y outbox existentes. Un escritor y una autoridad de
  integración. No plataformas genéricas, flotas, multiusuario, alta disponibilidad
  ni reescritura por anticipación. Reutilizar mecanismos nativos antes de crear
  proxies, harnesses o capas de coordinación. Delegar sólo si ahorra trabajo real.
- **Anti deriva circunstancial:** trabajar sobre el siguiente impedimento del
  recorrido de usuario. Incidencias adyacentes quedan fuera salvo que lo impidan
  o comprometan datos/autoridad. Tras pruebas pertinentes verdes, avanzar al uso;
  no otra campaña de canarios, modelos o sondas sin una hipótesis decisiva nueva.
  No repetir la restauración histórica entera para cada edición documental.
- **Anti sobresimplificación:** reducir pasos y texto conservando autoridad,
  identidad, versiones, dependencias, fallo y recuperación. Mantener separados
  intención y propuesta; material, entrega y aceptación; fin nativo e integración;
  acceso a fuentes y cobertura; STOP pedido y detención; coste observado e
  imputación. No quitar guardas para lograr verde, ocultar incertidumbre, inventar
  cobertura ni recortar instrucciones hasta perder condiciones necesarias.

## Límites y operación

- La autoridad de desarrollo, instalación y publicación ya fue delegada;
  no pedir permisos ceremoniales. Eso no autoriza efectos institucionales,
  mensajes a terceros ni atribuir decisiones o aceptación a Félix.
- Conservar alcances privados autorizados de fuentes y asuntos. No mover plazos
  vencidos silenciosamente ni ampliar Gmail. Preparar un frente no cierra todos.
  Respetar pausas posteriores. `Retomar` reabre un asunto; `/reanudar` sólo avisos.
- No usar `gtd-flow` para desarrollar. Usar habilidades pertinentes de ingeniería
  o pensamiento cuando resuelvan el problema, sin imponer su ceremonia.
- Mantener privacidad y consumo: secretos y estado personal fuera de Git;
  no imprimir configuración con credenciales. Coste NULL no significa cero y
  reserva monetaria no acredita coste facturado. No cambiar modelo/esfuerzo o
  subir límites para esconder un fallo.
- No abrir SQLite viva con herramientas auxiliares. Consultar la API propietaria;
  exportar de forma consistente para ensayos en copias. Instalar desde fuentes
  con respaldo y comparación; evitar sobrescribir la composición con una base vieja.
- La ejecutora anterior puede reutilizarse si resulta útil. Consultar su estado
  antes de encargarle cambios; asignar propiedad sin escritores concurrentes.
  También se puede continuar directamente. No hace falta perpetuar dos sesiones
  ni crear agentes nuevos para cada paso.

## Rutas y comprobaciones suficientes

- Código: `products/fxsl/gtd-operations/runtime/gtd_felix/`.
  Instrucciones: `products/fxsl/gtd-operations/content.md` y `references/`.
  Pruebas: `tests/gtd_felix/`.
- Instalaciones: `/home/felix/.hermes/profiles/gtd-felix/` y
  `/home/felix/.hermes/profiles/gtd-private-helper/`.
  API local: `127.0.0.1:35017`; gateways principal 51111, auxiliar 51112.
  Verificar configuración efectiva antes de depender de estos valores históricos.
- Evidencia privada: `/home/felix/.local/state/gtd-felix/`.
  Recuperación E68: `enc68-recuperacion/recibo.md`.
  Consultar reportes E66–E68 sólo cuando el detalle haga falta; E69 es la
  continuación pendiente. No copiar datos privados a documentación versionada.
- Ejecutar regresión del defecto y vecinas afectadas; ampliar sólo si la evidencia
  lo pide. Para KORA en este checkout:
  `python3 -B kora_cli.py --knowledge-root /home/felix/kora-knowledge check`.
  `git diff --check` y commits semánticos por intención, staging de rutas exactas.
  No confundir pruebas offline con conducta instalada o aceptación humana.

## Qué permite declarar producción

Aplicar C1–C6 y G1–G10 de GUIA, sin añadir otro contrato de aceptación:
captura durable; continuidad y preparación útil; fuentes con cobertura honesta;
corrección/pausa/regreso; devolución accesible sin duplicados; una delegación
acotada útil; autoridad y gasto controlados; entrega recuperable; uso real y
aceptación explícita de Félix. Resolver incidentes materiales del alcance ofrecido.
No exigir completar todas sus obligaciones personales ni un número arbitrario
de días de piloto. No declarar aceptación por silencio ni por suites verdes.
