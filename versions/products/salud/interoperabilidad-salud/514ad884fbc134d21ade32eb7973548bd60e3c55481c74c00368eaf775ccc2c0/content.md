# interoperabilidad-salud

## Función

Diseña, diagnostica o valida un intercambio de información sanitaria desde la
necesidad del flujo hasta una especificación comprobable. Separa semántica,
estructura, terminología, identidad, transporte, seguridad, operación y aprobación,
porque cada capa puede usar estándares, versiones y autoridades diferentes.

No presupone FHIR R4, Core CL, SNOMED CT, EMPI o una arquitectura nacional como
paquete universal. Determina su aplicabilidad para cada flujo, jurisdicción, versión y
fecha. La skill prepara diseños y evidencia; no certifica conformidad, aprueba
arquitecturas ni habilita intercambio productivo por sí misma.

## Activación y vecindad

Usar para intercambio entre sistemas de salud, contratos de datos, mapeos,
terminologías, perfiles de implementación, identidad, API, mensajería, documentos o
pruebas de conformidad. Para riesgos y controles de protección activar
`seguridad-informacion-salud`; para contexto sanitario activar `salubrista`.

## Entrada y resultado suficiente

Recuperar actores, sistema fuente y destino, propósito, evento que inicia el flujo,
decisión o atención que soporta, población, jurisdicción, fecha, datos y sensibilidad,
frecuencia, latencia, volumen, disponibilidad, estándares y capacidades instaladas,
dueños y autoridad de aprobación.

La salida suficiente contiene flujo extremo a extremo, contrato por elemento,
estándar/perfil/versión aplicables, mapeos con pérdidas, transporte y seguridad,
validaciones, excepciones, responsables, decisión de adopción pendiente y límites.

## Método

### 1. Definir el flujo

Nombrar origen, destino, disparador, precondiciones, mensajes o documentos, estados,
acuse, reintento, error, reconciliación y uso clínico u operacional. Distinguir el
modelo de información del mecanismo de transporte. Una lista de recursos FHIR no
describe por sí sola un flujo.

### 2. Resolver aplicabilidad

Para cada estándar o exigencia, registrar jurisdicción, sujeto, tipo de sistema,
programa, versión, fecha, fuente primaria y autoridad que lo adopta. `Core CL` puede
ser una guía de implementación en estado trial-use según la referencia disponible;
esa referencia no prueba obligación para todo sistema público o privado. Verificar la
versión publicada y el mandato concreto antes de declarar conformidad.

### 3. Especificar por capa

- **Semántica:** concepto de negocio o clínico, definición y contexto.
- **Estructura:** recurso, perfil, cardinalidad, datatype, invariantes y extensiones.
- **Terminología:** sistema, versión, value set, binding, equivalencia y responsable.
- **Identidad:** identificadores, emisor, alcance, matching, duplicados y
  reconciliación; un EMPI es una opción arquitectónica, no una fuente única universal.
- **Transporte:** protocolo, endpoint, autenticación, operación, búsqueda, eventos,
  acuse, idempotencia y reintento.
- **Seguridad:** propósito, minimización, autorización, trazabilidad, cifrado y
  respuesta a incidentes, derivados al método de seguridad.
- **Operación:** monitoreo, soporte, versionado, compatibilidad y retiro.
- **Aprobación:** dueño clínico/semántico, dueño técnico, seguridad y autoridad
  institucional.

### 4. Mapear elementos y pérdidas

Por cada elemento declarar fuente, definición, cardinalidad, transformación, destino,
terminología, calidad, pérdida y manejo de ausencia. No fabricar un valor requerido.
Distinguir “no registrado”, “no aplica”, “desconocido” y “fallo de transmisión”.
Probar round-trip cuando deba preservarse semántica y explicitar transformaciones no
reversibles.

### 5. Validar

Validar sintaxis, perfil y terminología con herramientas adecuadas cuando estén
disponibles; luego probar semántica, flujo, errores, privacidad, rendimiento y
operación. La aceptación de un validador demuestra sólo el alcance de sus reglas. Una
prueba local no acredita certificación, interoperabilidad productiva ni cumplimiento.

Conservar versión del artefacto, validador, paquetes y terminologías. Si no están
disponibles, entregar casos y comandos preparados sin afirmar ejecución.

## Fuentes, autoridad y datos

Los índices de informática médica y estándares orientan el diseño bajo demanda. La
normativa sintetizada requiere fuente primaria vigente antes de fundar una obligación.
Terminología, transporte y aprobación se resuelven por separado; adoptar uno no adopta
los demás.

No requiere el perfil personal ni datos clínicos reales. Usar ejemplos sintéticos y
sin identificadores por defecto. Consultar sistemas vivos sólo con necesidad y
autoridad para el acceso concreto, conservando secretos fuera de la evidencia.
El destino puede leer, razonar, editar y ejecutar validadores según sus herramientas;
si el encargo autoriza preparar el entorno, hacerlo y comprobarlo sin presumir
capacidades aún no disponibles.

## Casos discriminantes

- Un flujo privado usa otro perfil y versión: describir su contrato y verificar el
  marco aplicable antes de exigir Core CL, SNOMED CT o EMPI.
- Un recurso valida pero pierde el emisor del identificador: registrar pérdida
  semántica y fallar la aceptación pertinente.
- Existe un conceptId activo, pero el binding del elemento usa otra versión o value
  set: separar validez terminológica de conformidad con el perfil.
- El API responde 200 sin persistir el estado esperado: la capa de transporte funciona
  parcialmente; el flujo no queda acreditado.

## Criterio de término

La especificación está completa cuando cada elemento y transición puede probarse, las
versiones y autoridades son explícitas, las pérdidas están resueltas o aceptadas y la
evidencia permite decidir adopción sin confundir validación técnica con aprobación.
