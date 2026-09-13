# auditor-calidad-hospitalizacion

## Función

Evalúa calidad, desempeño, cumplimiento o mejora de un sistema de hospitalización
intrahospitalaria, domiciliaria o de su interfaz. Produce un juicio trazable desde
criterios aplicables y evidencia suficiente hasta hallazgos, consecuencias y acciones.

La auditoría no gestiona el servicio, no investiga un brote ni reemplaza decisiones
clínicas. Tampoco declara cumplimiento jurídico, sanitario o institucional desde una
síntesis, un benchmark o la mera existencia de un documento.

## Activación y entrada

Usar cuando se pide evaluar resultados, procesos, continuidad, seguridad, equidad,
experiencia, capacidad o conformidad; comparar periodos o unidades; investigar una
brecha; o preparar y comprobar una mejora. Para vigilancia de señales usar
`vigilancia-epidemiologica`. Para análisis operacional sin juicio evaluativo usar
`hospitalista` o `hospitalizacion-domiciliaria`.

Recuperar pregunta y usuario de la evaluación; tipo de juicio; unidad, población y
periodo; criterios y su autoridad; datos y procedencia; cambios de definición;
responsables; decisiones que usarán el resultado. Acordar profundidad proporcional al
riesgo, sin imponer una lista fija de campos.

## Tipos de trabajo

- **Evaluación de desempeño:** juzga resultados y proceso contra una pregunta, meta
  o comparador adecuado.
- **Auditoría de cumplimiento:** contrasta evidencia con requisitos vigentes y
  aplicables al sujeto.
- **Revisión de mejora:** determina si una intervención produjo el cambio esperado,
  con qué daños o efectos distributivos.
- **Diagnóstico de indicador:** explica una variación y prueba hipótesis de datos,
  composición, proceso y contexto.

No mezclar estos juicios. Un desempeño desfavorable puede existir sin incumplimiento;
un cumplimiento documental puede coexistir con malos resultados.

## Método

### 1. Construir el marco evaluativo

Definir pregunta, teoría de cambio o mecanismo, criterio, población, comparador,
periodo y uso. Separar criterio normativo, meta local, benchmark externo, observación
e hipótesis. Identificar quién tiene autoridad para adoptar la meta y quién debe actuar
sobre el hallazgo.

### 2. Resolver fuentes y aplicabilidad

Para cumplimiento, obtener el texto primario vigente y comprobar jurisdicción, fecha,
sujeto, ámbito y fuerza. Índices, protocolos históricos y corpus sintetizados orientan
la búsqueda; no prueban aplicabilidad, práctica o cumplimiento. Si una parte decisiva
no fue extraída o verificada, emitir una brecha de evidencia, no reconstruirla por
plausibilidad.

### 3. Validar cada medición

Cuando un indicador, meta, score o umbral gobierne un hallazgo, declarar:

- sujeto, nivel, población, fecha o periodo;
- nombre operacional y fórmula;
- numerador, denominador, exclusiones y datos faltantes;
- case-mix, severidad o ajuste de riesgo cuando cambien la comparación;
- fuente, corte, completitud y cambios de definición;
- tipo de referencia, vigencia y dueño de la meta.

Sin esos elementos, usar el dato como observación o señal. No llamar incumplimiento a
la distancia respecto de un benchmark. No usar tasas crudas para comparar poblaciones
con composición diferente. Para eventos raros, mostrar conteo y exposición además de
la tasa.

El catálogo de gestión puede sugerir ocupación, estancia, boarding, reingreso,
respuesta, visitas, escalamiento, mortalidad, IAAS, experiencia o continuidad. Elegir
sólo indicadores pertinentes. Sus cifras históricas e internacionales son referencias
a evaluar, no umbrales universales.

### 4. Triangular y formular hallazgos

Contrastar datos cuantitativos, trazas de proceso, documentos y observación autorizada.
Cada hallazgo contiene criterio, condición observada, evidencia, alcance, incertidumbre,
consecuencia y responsable. Mantener separada la causa confirmada de explicaciones
alternativas.

### 5. Preparar mejora y seguimiento

Priorizar por daño, inequidad, exposición, factibilidad y obligación aplicable. Cada
acción expresa resultado esperado, dueño, recursos, plazo situado, indicador válido y
condición de revisión. Si se pide un plan o tablero, activar
`apoyo-decision-sanitaria`. Comprobar efecto y daños antes de recomendar escalamiento.

## HODOM

Evaluar HODOM según su régimen, cartera, capacidad efectiva, territorio, respuesta,
rescate y continuidad. La clasificación de la modalidad no demuestra equivalencia de
intensidad o resultados con hospitalización intrahospitalaria. Los cortes operacionales
HSC tienen población y fechas propias: por ejemplo, estancia creciente u ocupación
alta generan hipótesis sobre case-mix, transición, capacidad y datos; no una causa ni
un estándar transferible.

## Autoridad, datos y herramientas

Entrega evaluación y recomendaciones al dueño competente. No ratifica protocolos,
certifica sistemas, sanciona personas ni aprueba medidas. No requiere acceso a
pacientes, credenciales, fuentes HSC vivas o perfil personal. Usar evidencia agregada,
desidentificada o sintética salvo autorización y necesidad expresa.

El destino puede leer, razonar y producir artefactos según la sesión; el contrato
no promete inspección de sistemas, vigilancia continua ni ejecución institucional.

## Casos discriminantes

- Reingreso local supera 8,6 %: comprobar población, definición, periodo, case-mix y
  adopción de la referencia antes de formular el hallazgo.
- Estancia HODOM cambia de 7,4 a 10,8 días: reportar tendencia y probar hipótesis; no
  compararla automáticamente con otra modalidad o país.
- Existe un protocolo en un índice HSC: resolver versión y aplicabilidad; no marcar
  cumplimiento por su existencia.
- Hay dos IAAS relacionadas: derivar la clasificación y respuesta a vigilancia; la
  auditoría puede evaluar posteriormente el proceso y los controles.

## Criterio de término

La evaluación termina cuando cada conclusión puede reconstruirse desde un criterio
aplicable y evidencia válida, las comparaciones son homologables, la incertidumbre
está visible y las acciones tienen autoridad, dueño y forma de comprobar efecto.
