---
urn: urn:dev:kb:cierre-operativo
nombre: cierre-operativo
version: 1.0.0
estado: borrador
descripcion: "Contrato de cierre de encargos de software: resultado conseguido y comprobado, correcciones dentro del alcance, estados de evidencia sin reinterpretar, entrega Git integrada en la rama principal con push normal confirmado, continuidad minima y reporte final acotado. Para cualquier agente que cierre trabajo sobre un repositorio."
fuente: "Texto del operador entregado en chat a KORA (perfil hermes) el 2026-08-25; snapshot literal en 10159 bytes, sha256:2f8ffdbb90c8a6597442b974420e84fe98aa31e6bc6372aa48f59d967af6fad9. Busqueda focal en el host sin archivo fuente previo; koraficacion integral. Redensificada el 2026-08-25 tras revision del operador: fusion de duplicados reales (prohibiciones de historia/force-push, condiciones no-PASS vs chequeos post-push, doble declaracion de la autorizacion) con cobertura re-auditada."
creado: 2026-08-25
lang: es
tags: [cierre, entrega-git, disciplina-operativa, estados-de-evidencia, agentes]
cita: [urn:dev:artefacto:ship-discipline]
---

# Cierre operativo

Contrato de cierre para proyectos con **un solo desarrollador, un solo
usuario y un host seguro y controlado**. El cierre forma parte del trabajo:
conseguir y comprobar el resultado, corregir lo corregible dentro del
alcance, completar todo cambio necesario y entregarlo en la rama principal
con push normal confirmado.

## Alcance y autoridad

- La solicitud actual y las instrucciones más recientes gobiernan el alcance.
  Un hallazgo incidental no autoriza nuevas funcionalidades, refactors,
  limpieza general, documentación adicional ni trabajo futuro.
- Prohibido: incorporar cambios ajenos o preexistentes; publicar secretos,
  temporales o material fuera del alcance; reescribir historia publicada;
  force push; eliminar ramas automáticamente.
- La autorización se limita a commit, integración en la rama principal y push
  (§ Acciones externas). No cubre despliegues, migraciones sobre datos reales
  ni otras acciones externas salvo que la solicitud también las incluya.

## Regla principal

Haz únicamente lo necesario para conseguir el resultado, demostrarlo,
corregir un problema real, preservar continuidad necesaria, integrar la
entrega en la rama principal o publicar el trabajo. Omite cualquier acción
que no cumpla una de esas funciones.

## Ejecución

1. Determina el resultado exacto, las restricciones aplicables y la evidencia
   suficiente para declararlo conseguido.
2. Inspecciona solo las superficies capaces de confirmar o invalidar ese
   resultado: una revisión focal basta, no audites todo el repositorio.
3. Corrige directamente los problemas claros, seguros, reversibles y
   comprendidos en el alcance.
4. Verifica el comportamiento modificado con pruebas proporcionales a su
   impacto: nada de suites completas para cambios pequeños si una
   comprobación específica lo demuestra; amplía la verificación solo ante
   riesgo, dependencias afectadas o fallos.
5. Revisa el diff final y elimina únicamente residuos creados por este
   trabajo.
6. Actualiza documentación o continuidad solo si existe información durable
   que no esté ya expresada por el código, las pruebas o la configuración.
7. Integra todos los cambios necesarios en commits coherentes sobre la rama
   principal.
8. Haz push normal de la rama principal y confirma la entrega en su
   referencia remota.
9. Informa el resultado con evidencia mínima y detente. No repitas una
   comprobación válida si nada relevante cambió después.

### Estados de evidencia

Úsalos sin reinterpretarlos; una suposición, `ABSENT` o `NOT_RUN` nunca
equivalen a `PASS`.

| Estado | Criterio |
|---|---|
| `PASS` | comprobado y correcto |
| `FAIL` | comprobado y fallido |
| `PARTIAL` | existe progreso válido, pero falta una condición de cierre |
| `ABSENT` | la capacidad o comprobación no existe |
| `NOT_RUN` | no se ejecutó |

## Correcciones

Corrige sin pedir permiso cuando el problema pertenece al encargo, está
suficientemente comprendido, admite una solución segura y reversible, y no
requiere una decisión de producto, dominio, arquitectura o autoridad. Esto
incluye errores introducidos por el trabajo, comportamiento incompleto,
imports o tipos rotos, residuos propios, depuración accidental, documentación
factual incorrecta y secretos incorporados accidentalmente al diff. Después
de corregir, repite únicamente las comprobaciones afectadas y revisa el diff
resultante.

No fuerces una solución cuando implique una acción destructiva; datos o
sistemas externos no autorizados; una decisión humana irreducible; una
expansión material del alcance; o riesgo de sobrescribir trabajo ajeno. En
ese caso, conserva lo válido e informa solo el bloqueo y la decisión mínima
necesaria.

## Continuidad y documentación

Conserva estado durable, no una narración de la sesión. Actualiza la fuente
canónica existente únicamente cuando quede trabajo material pendiente; una
decisión durable que no viva ya en otra fuente; un requisito operativo
necesario para continuar; o un cambio real en la siguiente acción del
proyecto. Si el proyecto expresa suficientemente el resultado y no queda
continuidad necesaria, no modifiques documentación.

No crees por rutina handoffs, memorias, changelogs, reportes, tickets,
matrices, dashboards ni archivos de estado; no dupliques el diff, la
conversación ni información que Git ya conserva. No escribas memoria salvo
autorización explícita.

## Entrega Git

La rama principal es el único destino final de la entrega; toda rama de
trabajo es transitoria. Determínala mediante el contrato local del
repositorio o la referencia por defecto del remoto: no presupongas que se
llama `main` o `master` cuando pueda comprobarse directamente.

**Antes de commitear o integrar:** identifica la raíz del repositorio, la
rama principal, el remoto y su upstream; revisa el estado del working tree,
las ramas involucradas y el diff; separa los cambios necesarios de los
preexistentes, ajenos, temporales o accidentales; comprueba que lo publicable
no contenga secretos ni información sensible; preserva cualquier cambio ajeno
o fuera de alcance; ejecuta la verificación necesaria sobre el candidato real
a entrega. Incluye todo lo necesario para que el resultado funcione
—implementación, pruebas, configuración, esquemas, migraciones, documentación
canónica, continuidad durable y eliminaciones requeridas—; no excluyas una
pieza necesaria para reducir artificialmente el commit.

**Si el trabajo está en otra rama:**

1. Confirma qué cambios y commits pertenecen al encargo.
2. Actualiza la información del remoto.
3. Sincroniza la rama principal local con su upstream mediante el
   procedimiento normal del repositorio.
4. Integra en la rama principal todos y solo los cambios necesarios.
5. Resuelve únicamente conflictos claros, seguros y comprendidos en el
   alcance.
6. Repite las comprobaciones invalidadas por la integración.
7. Revisa el diff y la historia resultantes antes de publicar.

Elige el método de integración más simple permitido por el repositorio;
conserva commits coherentes que expresen unidades reales de valor y no
reduzcas todo a un único commit salvo que la política local o la solicitud lo
exijan. Ante un conflicto ambiguo, historia inesperada, protección de rama o
riesgo de sobrescribir trabajo: conserva lo válido, declara `PARTIAL` con el
bloqueo exacto y no publiques la rama de trabajo como sustituto de la
principal.

**Antes del push:** confirma que publicas la rama principal, comprueba su
relación con el upstream, verifica que contiene todos y solo los commits
necesarios y que ningún cambio ajeno o fuera de alcance será publicado. Haz
push normal exclusivamente desde la rama principal hacia su rama principal
remota.

**Después del push:** confirma que el comando terminó correctamente; verifica
que la rama principal remota contiene todos los commits esperados; comprueba
la paridad entre la rama principal local, su upstream y la referencia remota;
confirma que no quedó ningún cambio necesario fuera de la rama principal, sin
commit, ni ningún commit necesario solo en local.

El working tree puede permanecer sucio únicamente por cambios preexistentes
o ajenos preservados deliberadamente: no los borres, integres ni presentes
como parte de la entrega. Si un workspace no usa Git, indícalo sin inventar
un cierre Git.

No declares `PASS` si falla cualquiera de las condiciones anteriores, si
falta un cambio necesario o si existe un archivo requerido sin seguimiento.

## Acciones externas

Para despliegues, migraciones reales, publicaciones, mensajes, APIs u otras
acciones externas: actúa solo cuando estén autorizadas; confirma el resultado
en el destino; una solicitud enviada no es una acción completada; no repitas
una acción únicamente para obtener una confirmación más cómoda. Commit,
integración en la rama principal y push están autorizados por este contrato;
las demás acciones externas no.

## Criterio de cierre

Detente cuando el resultado solicitado esté conseguido con evidencia
proporcional suficiente; los problemas corregibles dentro del alcance estén
resueltos; todos los cambios y commits necesarios estén integrados en la rama
principal; la rama principal esté publicada y la remota contenga exactamente
la entrega esperada; la continuidad imprescindible esté preservada; y el
trabajo ajeno permanezca intacto. No prolongues el cierre con mejoras
laterales, abstracciones preventivas, comprobaciones duplicadas,
documentación ornamental, recomendaciones genéricas ni preparación para
escenarios hipotéticos.

## Respuesta final

Entrega solo:

```text
Cierre — PASS | PARTIAL | FAIL

Outcome:
- resultado conseguido y valor entregado.

Comprobaciones:
- evidencia decisiva — estado.

Correcciones:
- solo si hubo correcciones relevantes.

Continuidad:
- UPDATED: <ruta y estado durable> | NO_CHANGE | NOT_RUN.

Git:
- repositorio y rama principal;
- commits publicados: hash y mensaje;
- integración en rama principal: PASS | FAIL;
- remoto y rama principal de destino;
- push: PASS | FAIL;
- paridad principal local/remota: PASS | FAIL;
- cambios preexistentes preservados, si existen.

Otras acciones externas:
- resultado confirmado o NOT_RUN.

Límites o pendientes:
- solo lo que impida un PASS; omitir si no existe.

Siguiente acción:
- una sola acción concreta, únicamente si todavía es necesaria.
```
