# Continuar KORA: maquinaria primero

Fecha de corte: 2026-09-13. El encargo vigente es dejar la maquinaria a punto
antes de renovar productos. Este es el único relevo activo; se retira cuando
su trabajo pendiente termine.

## Estado comprobado

La serie integrada en `master` conserva la implementación de `669fec2`,
reorganizada en commits por intención. No incorpora el commit de productos
`52a539d`. Incluye:

- Restricciones de revisión conservadas al resolver alias y cadenas de alias.
- Adopción de archivos existentes con recuperación de estado físico y propiedad.
- Candidatas compatibles sin bloqueos causados por caché regenerable; los
  residuos privados y las candidatas históricas siguen protegidos.
- Rechazo de raíces inexistentes y alcance explícito de `check`.
- Sondas que distinguen lectura, materialización y marcadores de carga efectiva.
- Parser YAML seguro nativo con alternativa Python y rechazo de claves duplicadas.
- Una realización conjunta por destino en el recorrido válido de `check`, con
  diagnóstico individual cuando falla y conservación de colisiones y revalidación.

Sobre el árbol preparado para integración: 236 pruebas aprobadas en 89,430 s;
pruebas focales de cada commit aprobadas; 10 pruebas de catálogo aprobadas con
la alternativa Python. `check`, usando la biblioteca explícita, informa 521
objetos activos, 18 archivados y ninguna incidencia. El diff de implementación
coincide con `669fec2`; solo este relevo añade contenido al resultado anterior.

La evidencia de este cierre está en
`/home/felix/lab/cierre-kora-maquinaria-2026-09-13/`: `suite.log`, `check.json`,
`commits.json` y registros de preservación/publicación. Son comprobaciones
locales. El historial Git y la referencia remota identifican los commits finales;
verifica su estado al retomar en vez de asumir que no avanzaron.

La lectura actual del instalador no muestra recuperación pendiente. Registra un
bytecode modificado de `koraficacion-integral`, ya conocido y conservado; no se
actualizaron instalaciones personales durante este cierre.

## Qué falta para cerrar la aceptación de maquinaria

1. **Actualización nativa discriminante.** El ensayo de actualización existente
   observa lectura de la nueva fuente y marcadores; no distingue por sí solo que
   el rol haya sido cargado como instrucciones. Contrasta dos versiones de un
   canario sintético en sesiones nuevas, con la misma tarea y una diferencia de
   conducta observable. No reveles la respuesta esperada ni ordenes leer el
   archivo del rol para producirla. Comprueba cada runtime según su mecanismo
   efectivo y conserva cualquier limitación observada.
2. **Integridad histórica bajo demanda.** `check` verifica las referencias del
   catálogo; `at_revision` verifica una revisión consultada. No existe una
   comprobación explícita de toda la historia conservada. Cierra esa capacidad
   usando los verificadores existentes y una invocación deliberada, sin escanear
   toda la historia en cada consulta. Prueba versiones previas intactas y
   corrompidas, conocimiento y fuentes de productos, incluidas identidades
   retiradas. Usa fixtures; no repares ni reescribas el corpus real.
3. **Integración final sobre el candidato resultante.** Ejecuta los recorridos
   pertinentes y el ensayo de independencia/traslado en raíces y homes temporales.
   La evidencia nativa e independiente conservada del 2026-09-10 corresponde a
   un candidato anterior; no acredita automáticamente el nuevo. Repite solo lo
   que los cambios y estas brechas requieren.

El cierre suficiente exige recorridos mecánicos sin defectos materiales abiertos,
evidencia nativa que discrimine lo que afirma y límites precisos. No requiere
renovar el corpus, hacer instalaciones personales ni demostrar utilidad diferencial
de productos. Esa evaluación pertenece a la etapa siguiente.

## Trabajo que se conserva fuera de este alcance

- En el checkout principal permanecen ediciones previas en
  `products/salud/medico-hospitalista/content.md` y
  `products/salud/urgenciologo/content.md`, y `.hermes/` no seguido. No los
  incluyas en commits de maquinaria ni los restaures por rutina.
- `fxai/kora-funcion-sin-ceremonia-20260911` conserva la propuesta sobre 18
  artefactos; `fxai/kora-maquinaria-20260911` conserva la serie previa al cierre.
  El trabajo independiente `fxai/gtd-felix-20260911` también se conserva.
- Los cuatro borradores de conocimiento preparados anteriormente siguen sin
  publicar. No se retoma su aprobación durante esta etapa.
- `/home/felix/kora-knowledge` conserva cambios ajenos de retiro histórico y
  conocimiento privado. Es una biblioteca independiente, no una carpeta para
  incluir en este cierre Git.

## Goal para la próxima sesión

Dejar a punto la maquinaria de KORA en `/home/felix/kora-pneuma`, con el menor
trabajo completo y evidencia suficiente para iniciar después la renovación de
productos. Retoma `master`, lee `AGENTS.md`, `README.md`, `docs/operacion.md` y
este `HANDOFF.md`, y verifica Git y los cambios locales antes de actuar.

Cierra las brechas de comprobación pendientes: un canario de actualización que
distinga carga efectiva de instrucciones de lectura de archivos, y una
comprobación explícita de integridad histórica bajo demanda, reutilizando los
mecanismos existentes. Usa fuentes, revisiones y homes temporales para probar
éxito, corrupción, incompatibilidad y recuperación sin modificar productos,
conocimiento ni instalaciones personales. Comprueba la integración e independencia
del candidato final y corrige los defectos materiales que aparezcan.

Conserva las garantías de concurrencia, propiedad, revisiones y recuperación.
Evita nuevas capas, registros o controles sin una función demostrada. Separa
archivos válidos, integridad, carga nativa, conducta y utilidad. No reabras la
auditoría completa ni repitas pruebas sin una causa nueva.

Integra los cambios autorizados en `master` mediante commits atómicos y
semánticos, verifica la publicación normal y la paridad con `origin/master`,
y conserva el trabajo ajeno. Termina con un dictamen preciso de maquinaria
lista o pendientes materiales concretos. La renovación de agentes, skills y
conocimientos queda para el encargo posterior.
