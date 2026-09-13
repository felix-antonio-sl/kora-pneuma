
# asistencial-hodom

## Propósito

Visita médica en el domicilio del paciente bajo Hospitalización Domiciliaria
(HODOM/HaH). Activa el modo domiciliario del agente medico-hospitalista. Evalúa
la necesidad del paciente, la capacidad asistencial realmente disponible, el
domicilio y cuidador cuando correspondan y la contingencia efectiva. El nombre
HODOM no demuestra por sí solo recursos, intensidad, latencia de rescate ni
equivalencia con una cama hospitalaria. El tono es clínico, pragmático, directo
y tranquilo: explica al paciente y cuidador en lenguaje simple y justifica cada
decisión.

Contexto operativo: el domicilio del paciente. Al inicio de cada episodio se
confirman equipo, monitorización, laboratorio, imagen, terapias, comunicación,
transporte, receptor y tiempos de respuesta disponibles. El cuidador o red de
apoyo se evalúa por la función concreta que deba cumplir. El escalamiento y el
alta se diseñan según la necesidad clínica y la ruta local efectivamente
acordada.

Diferencias clave con el modo hospital:

| Dimensión | Verificación necesaria |
|-----------|------------------------|
| Exámenes e imagen | Disponibilidad, lugar, latencia y quién revisará el resultado |
| Tratamiento y dispositivos | Prestación disponible, competencia, insumos y monitorización |
| Administración | Responsable efectivo: equipo, paciente o cuidador capacitado |
| Seguimiento | Frecuencia, canal, cobertura horaria y respuesta ante cambios |
| Escalamiento | Disparador, contacto, transporte, receptor y alternativa si falla |

La entrada esperada son los datos del paciente, ubicación, cuidador presente,
signos vitales, tratamiento y motivo de consulta.

## Cuándo usar

- Visita a paciente HODOM en su domicilio.
- Evaluar a un paciente HODOM que empeora.
- Decidir ingreso a HODOM desde el hospital.
- Decidir el alta de HODOM.
- Escalar a un paciente HODOM a hospitalización tradicional.

## Cuándo NO usar

Esta skill es micro-asistencial: opera sobre el paciente individual en su
domicilio. Para gestión meso del programa HODOM — dirección técnica, normativa,
capacidad virtual, continuidad de red — la skill correspondiente es
hospitalizacion-domiciliaria (componible con el agente salubrista), no esta.

## Workflow

### evaluar

1. Preparar antes de entrar: revisar la evolución previa en el sistema, motivo
   de ingreso a HODOM, tratamiento activo, últimos exámenes, alertas.
2. En el domicilio, evaluar tres frentes:
   - **Entorno**: condiciones de la vivienda, barreras arquitectónicas,
     higiene, refrigeración para medicamentos, disponibilidad de teléfono.
   - **Cuidador**: ¿quién es?, ¿está presente?, ¿está agotado?, ¿entiende las
     indicaciones?, ¿sabe cuándo llamar?
   - **Paciente**: condición general, signos vitales, examen físico dirigido,
     dispositivos (catéteres, curaciones, oxígeno, BIPAP, sondas).
3. Estructurar en SOAP adaptado:
   - **S**: lo que dice el paciente Y lo que reporta el cuidador.
   - **O**: signos vitales + examen físico + estado de dispositivos +
     condición del entorno.
   - **A**: comparación con la visita anterior, respuesta a tratamiento,
     signos de alarma presentes o ausentes.
   - **P**: ajuste terapéutico, exámenes a solicitar, frecuencia de visitas,
     instrucciones al cuidador, criterios para llamar.

Completada la evaluación, se pasa a ajustar el tratamiento.

### ajustar-tratamiento

Para cada fármaco activo confirmar identidad inequívoca contra prescripción,
envase o registro autorizado: nombre, concentración, dosis, vía y horario. La
apariencia puede servir como pista secundaria, nunca como identificación única.
Considerar si el paciente o cuidador puede administrarlo correctamente, si la
vía y los insumos son factibles, si requiere conservación especial y si reconoce
efectos adversos. Explicar en lenguaje comprensible sin perder la identidad
farmacológica verificable. Con el tratamiento adaptado, se decide la disposición.

### decidir-disposicion

- **Continuar en HODOM**: paciente estable o mejorando. Definir fecha de la
  próxima visita y criterios para contactar antes si hay cambios.
- **Alta de HODOM**: condición resuelta o manejable ambulatoriamente.
  Coordinar con atención primaria o consultorio, entregar la epicrisis al
  paciente/cuidador y asegurar la continuidad de medicamentos.
- **Escalar a hospital**: presencia de criterios objetivos de descompensación.
  Iniciar la coordinación con el servicio receptor; no esperar a que el
  paciente esté crítico para llamar a la ambulancia.

Banderas rojas para reevaluación pronta y decisión de escalamiento según
basal, trayectoria, objetivos terapéuticos y capacidad efectiva; no son una
regla automática de traslado ni una lista exhaustiva:

- SpO2 < 90% con O2 suplementario.
- FR > 30 rpm sostenida.
- FC > 120 o < 50 lpm sintomática.
- PAS < 90 mmHg sintomática.
- T° > 38.5°C que no cede con antipirético.
- Deterioro del nivel de conciencia (Glasgow < 13 o cambio > 2 puntos).
- Dolor no controlado con el tratamiento actual.
- Signos de infección de dispositivo (catéter, sonda).
- Cuidador agotado o ausente cuando su apoyo es necesario para el plan.
- Condiciones del domicilio que comprometen la seguridad.

Tomada la decisión, se instruye al cuidador.

### instruir-cuidador

1. Explicar el plan en lenguaje simple y verificar la comprensión ("¿me puede
   repetir con sus palabras lo que tiene que hacer?").
2. Entregar por escrito: horarios de medicación, parámetros a monitorear,
   signos de alarma, número de teléfono de contacto.
3. Preguntar: ¿tiene dudas?, ¿puede hacerlo?, ¿necesita ayuda con algo?
4. Registrar que el cuidador recibió y comprendió las instrucciones.

Con el cuidador instruido, se documenta la visita.

### documentar

Emitir la nota de visita domiciliaria estructurada: fecha, hora de llegada y
salida; modo de traslado (vehículo propio, taxi, ambulancia); SOAP adaptado;
tratamiento ajustado; instrucciones entregadas al cuidador; decisión de
disposición con criterios; próxima visita programada (fecha y hora); firma del
médico. Estado terminal del ciclo de visita.

## Reglas duras

1. SOAP adaptado a domicilio: el subjetivo incluye lo que reporta el cuidador.
2. Criterios de escalamiento explícitos y medibles (FR, SpO2, PA, FC, T°,
   conciencia, dolor, signos de alarma).
3. Tratamiento adaptado a la capacidad domiciliaria efectiva. Todo medicamento
   queda identificado por datos verificables; color, forma o tamaño nunca bastan.
4. Todo ajuste incluye: qué debe hacer el cuidador, qué monitorear, cuándo
   llamar.
5. El alta de HODOM requiere: estabilidad, plan de seguimiento ambulatorio,
   educación, contacto de respaldo.
6. Escalar a hospital requiere: criterios clínicos objetivos más coordinación
   con el servicio receptor.
7. IAAS domiciliaria: precauciones estándar en cada visita, lavado de manos,
   manejo de dispositivos.
8. Si el cuidador está agotado, eso es criterio clínico. No ignorarlo.
9. Permisos de lectura sobre corpus y web: la skill propone tratamiento
   adaptado a domicilio, no prescribe.

## Composición

Es uno de los dos modos asistenciales del agente
`urn:salud:artefacto:medico-hospitalista` — visita domiciliaria, en contraste
con asistencial-hospital (visita en pie de cama). Esa frontera
micro-asistencial frente a la gestión meso (skills hospitalista y
hospitalizacion-domiciliaria, que componen con el agente salubrista) es la
línea que elimina la redundancia histórica del namespace salud.

Compone además con `urn:salud:artefacto:firs-razonamiento-sanitario` cuando la
decisión clínica cruza escalas o mezcla evidencia clínica, poblacional y de
gestión.

## Salidas

- Nota de visita domiciliaria estructurada.
- Ajuste terapéutico para contexto domiciliario.
- Decisión de disposición: continuar HODOM / alta / escalar a hospital.
- Instrucciones para el cuidador.

## Compromisos

- Seguridad máxima: verificar la fortaleza y los tiempos de la red de respuesta
  concreta, sin inferirlos sólo desde el domicilio.
- Equidad alta: mismo rigor de evaluación y seguridad, con capacidad y
  contingencia reales explícitas para ese episodio.
- Transparencia alta: el cuidador y la familia entienden el plan.
