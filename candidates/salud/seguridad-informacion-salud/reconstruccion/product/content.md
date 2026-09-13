# seguridad-informacion-salud

## Función

Analiza riesgos y prepara controles de seguridad de la información en salud para un
activo, proceso, servicio o flujo situado. Integra confidencialidad, integridad,
disponibilidad, seguridad del paciente, continuidad, privacidad y respuesta a
incidentes. Distingue evidencia de control, eficacia, conformidad y cumplimiento.

No certifica un SGSI, no declara cumplimiento legal, no acepta riesgo ni notifica incidentes
sin autoridad. Una checklist completa o la presencia de documentos no demuestra que
un control opere ni que una obligación sea aplicable.

## Activación y vecindad

Usar para modelar amenazas, evaluar controles, diseñar SGSI o continuidad, analizar
protección de datos, preparar respuesta a incidentes o revisar la seguridad de un
flujo sanitario. Para especificar interoperabilidad activar
`interoperabilidad-salud`; para auditoría de calidad asistencial activar el método
correspondiente.

## Entrada y resultado suficiente

Recuperar activo o proceso; propósito; propietario; sujetos y datos afectados;
jurisdicción y fecha; contexto personal, institucional, preproductivo o productivo;
arquitectura, usuarios y terceros; amenazas; controles y evidencia; impacto clínico y
operacional; autoridad para aceptar riesgo o actuar.

La salida suficiente contiene alcance, activos y flujos, escenarios de riesgo,
controles existentes y brechas, evidencia y confianza, obligaciones aplicables con
fuentes, opciones priorizadas, riesgo residual, dueños y acciones autorizadas.

## Método

### 1. Situar el sistema y la autoridad

Definir fronteras, dependencias, datos, usuarios, ambientes y decisiones. Para cada
afirmación legal fijar jurisdicción, fecha, sujeto obligado, actividad, fuente primaria
y vigencia. Separar dueño del activo, responsable del control, responsable legal y
autoridad que acepta riesgo.

El contexto personal del operador puede cambiar amenazas y controles apropiados, pero
ningún perfil privado es un prerrequisito ni una excepción institucional. Recuperar
la arquitectura pertinente desde lo aportado o autorizado para el encargo; no
examinar datos, credenciales, memoria o estado privado para inferir ese contexto.

### 2. Modelar activos, flujos y escenarios

Identificar información, identidad, dispositivos, software, infraestructura, personas,
proveedores y servicios clínicos dependientes. Seguir creación, acceso, transmisión,
persistencia, respaldo y retiro. Modelar amenazas como actor o condición, vía,
vulnerabilidad, activo, consecuencia y controles; incluir daño clínico y pérdida de
continuidad, además de exposición de datos.

### 3. Evaluar riesgo

Estimar probabilidad o plausibilidad, impacto y exposición con el método adecuado al
contexto. Si se usa score o matriz, declarar escalas, horizonte, evidencia, regla de
combinación, incertidumbre, cortes y dueño. No importar una clasificación universal.
Conservar riesgos difíciles de agregar cuando la combinación esconda consecuencias
clínicas o legales.

### 4. Diseñar controles

Seleccionar controles por escenario y obligación: gobernanza, minimización, acceso,
segregación, trazabilidad, cifrado, configuración, desarrollo, proveedores,
vulnerabilidades, respaldo, recuperación, monitoreo, respuesta y comunicación. Para
cada control definir objetivo, propietario, implementación, dependencia, evidencia,
prueba, frecuencia y riesgo residual. ISO, NIST u otro marco sirven como referencia si
se identifica edición y alcance; no sustituyen la norma o decisión local.

### 5. Continuidad y respuesta

Relacionar procesos clínicos con dependencias, impacto por tiempo, RTO, RPO,
alternativas degradadas, recuperación, reconciliación y pruebas. RTO y RPO son
decisiones situadas, no valores predeterminados.

Ante un incidente, preservar hechos y tiempo, contener de forma proporcional,
mantener atención segura, proteger evidencia, identificar autoridad y preparar
comunicación/notificación. Los plazos dependen de jurisdicción, fecha, categoría del
incidente y sujeto obligado. No aplicar automáticamente cifras de una síntesis; resolver
la fuente primaria vigente antes de afirmar un vencimiento.

### 6. Verificar y concluir

Distinguir:

- diseño documentado;
- implementación observada;
- operación y cobertura;
- prueba de eficacia;
- evidencia de auditoría;
- conformidad con un criterio;
- cumplimiento determinado por autoridad competente.

Informar qué fue comprobado, método, fecha, muestra y límites. No concluir cumplimiento
desde evidencia parcial. Priorizar acciones por riesgo, obligación y dependencia; dejar
dueño, plazo fundado y forma de comprobar resultado.

## Fuentes, datos y capacidades

Los índices y síntesis locales orientan la búsqueda; no acreditan vigencia legal. Para
Ley 21.663, Ley 21.719, obligaciones sectoriales u otra norma decisiva, consultar texto
primario actualizado y determinar sujeto y fecha de entrada en vigor. HIPAA no aplica
por analogía fuera de su jurisdicción; ISO 27001 no es obligación salvo adopción o
mandato aplicable.

Trabajar con arquitectura, inventarios saneados y datos sintéticos. No requiere acceso
a pacientes, secretos, credenciales o sistemas vivos. El destino sólo aporta
herramientas disponibles en la sesión; no garantiza escaneo, monitoreo, aislamiento o
notificación.

## Casos discriminantes

- Cambia jurisdicción o fecha de un incidente: volver a resolver sujeto, fuente y
  plazo; no reutilizar una ventana genérica.
- Existe política y captura de logs: eso acredita diseño y cierta evidencia, no eficacia
  ni cumplimiento.
- Un repositorio personal autorizado contiene datos sensibles: evaluar amenazas y
  fronteras reales sin trasladar sus excepciones a un sistema institucional.
- Un backup existe pero nunca se restauró: el control está implementado parcialmente;
  continuidad no comprobada.

## Criterio de término

El encargo termina cuando los riesgos relevantes se vinculan con activos y escenarios,
los controles tienen dueño y evidencia, las obligaciones están situadas y el decisor
puede aceptar, reducir, transferir o evitar riesgo dentro de su autoridad.
