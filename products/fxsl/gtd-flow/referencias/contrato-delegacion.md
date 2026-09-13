# Delegación con contexto y retorno suficientes

Una delegación necesita que quien la recibe entienda el resultado, su responsabilidad,
el contexto, las decisiones que puede tomar y cómo devolver progreso o resultado. La
cantidad de detalle depende de complejidad, riesgo, dependencias y posibilidad de fallo.
No se devuelve automáticamente una tarea pequeña porque falte un campo formal.

Para trabajo complejo puede usarse esta pauta:

```text
Resultado esperado:
Responsable y participantes:
Contexto y recursos pertinentes:
Alcance y decisiones autorizadas:
Criterio de aceptación:
Fecha o condición de retorno:
Qué hacer si aparece un impedimento:
```

Un responsable de integración evita ambigüedad cuando participan varias personas o
agentes. Puede haber varios ejecutores con propiedad disjunta; no confundir propiedad
compartida con ausencia de responsabilidad. Conservar dependencias y reunir las partes.

En delegación humana distinguir propuesta, solicitud enviada, aceptación y compromiso.
No inventar aceptación ni enviar recordatorios sin autoridad. El seguimiento puede
ocurrir en una fecha o al cumplirse una condición; no necesita día y hora universales.

En delegación a agentes comprobar capacidad efectiva, alcance, propiedad de archivos,
evidencia esperada y retorno. Usar aislamiento, pruebas, revisión independiente o
recuperación cuando resuelvan un riesgo concreto; no exigir logs especiales, rollback
o evaluación automatizada a toda lectura o redacción. Una acción irreversible puede
necesitar otra prevención o autoridad; no prometer que todo se revierte.

Si aparece un vacío menor, resolverlo con un supuesto visible. Si puede cambiar el
resultado, señalar la decisión pendiente y continuar la parte independiente. Al
recibir la entrega, comprobar lo necesario contra el criterio, integrar y dar por
cerrado sólo el trabajo efectivamente cumplido. Guardar el estado en el asunto
propietario; no abrir un registro paralelo por cada delegación.
