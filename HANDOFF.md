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

## Punto de partida

Checkout `/home/felix/lab/kora-gtd-felix`, rama `fxai/gtd-felix-20260911`.
La transición inicial quedó en `87f60ee`, sobre `e528313`; consultar Git para
cambios posteriores. Preservar `candidates/` y `versions/` sin seguimiento.
El corte vigente de hechos está en ESTADO; no usar salud, saldo o pausa del
15 de septiembre como observación actual.

## Continuación actualizada el 2026-09-21

E69 ya fue recuperado por API y exportación consistente. El estado propietario
ESTADO describe el resultado: minuta parcial válida, evaluación negativa,
run cancelled/discarded por límite y aviso Telegram confirmado. No repetirlo.
También registra la incidencia actual del gateway y la preparación offline de Jev.
Las cifras y salud del apartado anterior son la base histórica de esta transición.

Félix autorizó explorar Jev comenzando por Gmail y facilitó la ruta de credencial.
Tras 24 peticiones sintéticas favorables se evaluaron 22 correos reales con datos
innecesarios eliminados. Félix completó después una revisión ciega: 1 pertinente,
21 ruido. Jev coincide en 18/21 respuestas válidas, pero descarta el único pertinente
y selecciona 2 ruidos; una anomalía de distribución sigue separada. Las etiquetas
previas del asistente sólo coinciden en 4/22: quedan como evidencia histórica, no
criterio humano. ESTADO y los recibos privados `real/human-*.json` conservan la
reevaluación sin nuevas inferencias. La configuración NO se incorpora para descarte
automático. Siguiente propuesta: rúbrica breve basada en las decisiones y posterior
comprobación en otros correos; no llamar validación independiente al ajuste contra
estos 22. Sin instalación ni cambios en correo o asuntos GTD.
Al iniciar otra sesión, recuperar contexto mediante lecturas y **avisar a Félix
cuando esté lista para partir**, indicando estado y primera acción concreta antes
de modificar el producto o iniciar inferencias. Conservar autorizaciones vigentes;
el aviso no es una solicitud ceremonial de permisos.

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
  Consultar reportes E66–E68 sólo cuando el detalle haga falta; la recuperación
  E69 se encuentra en `jev-evaluation-20260921/e69-recovery.json`. No copiar datos privados a documentación versionada.
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
