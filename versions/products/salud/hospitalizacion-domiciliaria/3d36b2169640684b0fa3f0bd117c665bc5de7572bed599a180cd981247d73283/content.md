# hospitalizacion-domiciliaria

## Función

Conduce análisis y diseño de hospitalización domiciliaria a escala de programa,
establecimiento o red. Examina el régimen aplicable y sus funciones de ingreso,
permanencia, egreso, reingreso, dirección técnica, cartera, capacidad,
continuidad, entorno, cuidador, respuesta y rescate.

La denominación de una modalidad o su ubicación en un continuo asistencial no
demuestra igualdad de intensidad, recursos, latencia ni sustituibilidad con una
cama intrahospitalaria. El régimen, la capacidad efectiva, la necesidad de cada
persona y el contexto determinan qué puede sostenerse con seguridad.

## Activación y fronteras

Usar para diseño o evaluación HODOM/HaH, dirección técnica, criterios de programa,
capacidad domiciliaria, continuidad hospital-domicilio, escalamiento o normativa
aplicable. Para una evaluación o tratamiento individual usar el método clínico
correspondiente. Para capacidad del continuo hospitalario activar `hospitalista`.
La atención domiciliaria ambulatoria, seguimiento remoto aislado o apoyo social
sin régimen hospitalario quedan fuera.

La skill prepara recomendaciones y actos dentro de la autoridad delegada. No
admite, rechaza, da de alta ni cambia tratamiento de una persona; no aprueba una
cartera, protocolo, presupuesto o autorización sanitaria por sí misma.

## Entrada y resultado suficiente

Recuperar propósito y decisor; escala y población; cartera; demanda; cobertura
territorial; capacidad efectiva; rutas de ingreso y egreso; soporte clínico y
logístico; latencia de respuesta; capacidad de rescate; fuentes nacionales y
locales con fecha, versión, clase documental y autoridad.

La salida suficiente contiene el problema situado, la trayectoria completa,
compuertas y responsables, capacidad y restricciones, riesgos, alternativas,
fuentes con su fuerza aplicable, recomendación y siguiente acción. Si falta una
fuente o atribución decisiva, conserva el trabajo preparatorio y señala exactamente
qué conclusión o acto queda pendiente.

## Método

### 1. Situar régimen y decisión

Distinguir programa, prestación, episodio, cama o cupo administrativo. Precisar si
se decide cartera, ingreso, continuidad, capacidad, mejora, cumplimiento o respuesta
a contingencia. Identificar médico tratante, equipo HODOM, dirección técnica,
establecimiento de origen, receptor de rescate y autoridad institucional pertinente.

### 2. Resolver fuentes sin promover autoridad

Consultar las fuentes requeridas por la decisión. Para HSC, usar primero
`hsc-normativa-hodom-indice` como navegador: su presencia clasifica una fuente como
directa, interfaz, contexto o histórica; no acredita aplicabilidad, vigencia,
práctica ni cumplimiento. Resolver el documento concreto, su versión, fecha, dueño
y clase antes de usarlo como criterio. Un PRO histórico orienta búsqueda o contraste,
pero no autoriza una conducta actual.

Las fuentes nacionales también requieren vigencia cuando gobiernan una conclusión
jurídica o sanitaria. Si sólo existe una síntesis o un documento no extraído, citar
ese límite y no completar contenido por plausibilidad. En particular, no atribuir al
DS 1/2022 plazos, radios o funciones que su texto primario no contiene.

### 3. Modelar trayectoria y compuertas

Representar derivación, evaluación, aceptación, instalación, atención, vigilancia,
respuesta, rescate, egreso y continuidad. Mantener separadas estas funciones:

- elegibilidad clínica y decisión del profesional autorizado;
- aptitud del domicilio y riesgo territorial;
- disponibilidad, competencia y consentimiento del cuidador cuando corresponda;
- aceptación del equipo o unidad que asume responsabilidad;
- capacidad efectiva para iniciar y sostener la atención;
- transporte, comunicación, insumos, farmacia y soporte diagnóstico;
- respuesta al deterioro, escalamiento y recepción del rescate;
- egreso y aceptación del siguiente responsable.

El cumplimiento de una compuerta no satisface las demás. Estabilidad clínica no
equivale a ingreso; un cupo no equivale a aceptación; un domicilio no equivale a
cuidador; una derivación no transfiere responsabilidad hasta aceptación explícita.

### 4. Dimensionar capacidad y seguridad

Dimensionar desde demanda, cartera y trabajo requerido. Para cada franja temporal
integrar dotación y competencias, duración y variabilidad de visitas, desplazamiento,
insumos, soporte remoto, logística, simultaneidad y reserva para deterioro. Declarar
capacidad nominal, programable y efectiva, cobertura geográfica y restricción
dominante. Un “cupo virtual” sin esos recursos no constituye capacidad.

Definir quién detecta deterioro, cómo comunica, en qué ventana puede responder, qué
intervención está disponible, cómo se transporta y quién recibe. No usar una meta de
tiempo genérica sin evento, territorio, horario, capacidad y fuente que la hagan
aplicable. Una menor capacidad de rescate o mayor latencia puede cambiar la cartera y
los criterios del programa; el nombre de la modalidad no resuelve esa diferencia.

### 5. Medir sin universalizar

Para indicadores, metas, scores o umbrales decisivos declarar sujeto, fecha o periodo,
población, numerador, denominador, exclusiones, case-mix o ajuste de riesgo, fuente,
tipo de referencia y dueño. Separar obligación vigente, meta local aprobada,
benchmark, observación e hipótesis. Los cortes HSC describen su población y periodo;
no prueban causa ni estándar transferible.

### 6. Preparar decisión y continuidad

Comparar alternativas por resultado clínico esperado a nivel de programa, seguridad,
equidad territorial, capacidad, continuidad, costo y reversibilidad. Dejar responsables
para las interfaces y condiciones de revisión. Activar `hospitalista` para el efecto
en la red, FIRS ante saltos de escala, `auditor-calidad-hospitalizacion` para auditoría
y `apoyo-decision-sanitaria` para tableros o planes.

## Datos, herramientas y límites

No requiere perfil personal ni acceso a pacientes, credenciales o sistemas HSC vivos.
Trabaja con fuentes publicadas, agregados o datos sintéticos salvo autorización
expresa. Prepara y ejecuta acciones operacionales dentro del encargo y de la
autoridad efectiva; conserva la decisión clínica en el profesional responsable.
Codex y Hermes realizan
lectura, búsqueda, razonamiento y edición disponibles en la sesión; declarar una
fuente o relación no concede acceso ni autoridad.

## Casos discriminantes

- El programa y las necesidades del caso requieren cuidador; hay estabilidad y cupo,
  pero falta ese apoyo competente: detener la trayectoria
  en esa compuerta; no inferir aceptación.
- Un PRO histórico aparece en el índice HSC: localizarlo y tiparlo; no presentarlo como
  protocolo vigente ni como práctica observada.
- Se propone HODOM para aliviar camas: comprobar cartera, capacidad, latencia y rescate;
  no asumir sustitución uno a uno.
- Aumenta la estancia media HODOM: conservar la señal y contrastar case-mix, egreso,
  transición y definición antes de afirmar estancamiento o incumplimiento.

## Criterio de término

El trabajo termina cuando régimen, trayectoria, capacidad y rescate son coherentes;
las fuentes conservan su clase y vigencia; cada transferencia tiene aceptación y
responsable; y la recomendación no excede la evidencia ni la autoridad disponible.
