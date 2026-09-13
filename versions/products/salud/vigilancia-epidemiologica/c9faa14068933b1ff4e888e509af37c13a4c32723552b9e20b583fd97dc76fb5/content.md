# vigilancia-epidemiologica

## Función

Conduce el recorrido desde una señal hasta una decisión de investigación,
notificación o respuesta epidemiológica. Caracteriza tiempo, lugar, persona o
población, evento, exposición, severidad y fuente; clasifica con la definición
aplicable; estima riesgo; prepara acciones y conserva incertidumbre.

Una señal no es un caso confirmado ni un brote. Un agrupamiento no acredita nexo y
un umbral genérico no sustituye la definición del evento. La skill no realiza manejo
clínico individual, certifica diagnósticos, declara emergencias ni envía
notificaciones sin autoridad y canal habilitado.

## Activación y vecindad

Usar para eventos de notificación obligatoria, IAAS, RAM, conglomerados, brotes,
alertas, cambios sobre línea de base o evaluación de una señal. Para evaluar un
programa o auditar calidad usar `auditor-calidad-hospitalizacion`; para analizar la
operación afectada usar `hospitalista`; para tratar a una persona usar el método
clínico correspondiente.

## Entrada y salida suficiente

Recuperar evento o síndrome; fuente y fecha de detección; definición de caso y
versión; población y territorio; periodo; conteos, denominadores y exposición;
relaciones posibles; severidad; calidad y cobertura de datos; autoridad, receptor,
canal y plazo aplicables.

La salida contiene caracterización, estado de clasificación, evidencia a favor y en
contra, riesgo y grupos expuestos, acciones inmediatas proporcionales, requerimientos
de notificación, dueño, plazo fundado y brechas que deben resolverse.

## Método

### 1. Caracterizar la señal

Verificar identidad del evento, deduplicación, tiempo, lugar, población, fuente y
calidad. Construir numerador y denominador coherentes; si no existe denominador,
reportar conteo y cobertura sin inventar una tasa. Comparar con línea de base sólo
tras homologar definición, vigilancia, población y periodo.

### 2. Resolver definición y fuente

Identificar país y jurisdicción, evento concreto, fecha, sujeto obligado y fuente
primaria vigente. Las definiciones de sospechoso, probable, confirmado, brote y los
plazos pueden variar por evento y circular. `notificacion-eno-iaas` orienta hacia las
fuentes conocidas, pero declara partes no extraídas; no completar campos, listas ni
plazos desde memoria o analogía.

Si no puede recuperarse la definición aplicable, mantener “señal en evaluación”,
marcar el dato exacto pendiente y escalar al responsable epidemiológico cuando el
riesgo o una obligación potencial no admita demora.

### 3. Clasificar sin sobreafirmar

Aplicar los criterios encontrados al evento y periodo. Distinguir:

- registro o alerta técnica;
- señal validada;
- caso en clasificación;
- conglomerado o exceso observado;
- brote según definición aplicable;
- evento descartado o no clasificable con la evidencia actual.

Conservar fecha, autor y fuente de cada cambio de estado. Una relación temporal o
espacial es evidencia para investigar, no prueba causal.

### 4. Estimar riesgo y responder

Evaluar probabilidad o plausibilidad de propagación, magnitud, severidad,
vulnerabilidad, exposición, capacidad de detección y posibilidad de control. Adaptar
la respuesta: verificar datos, ampliar búsqueda, muestrear, controlar una exposición,
proteger grupos, coordinar clínica y operación, comunicar o escalar. No usar una matriz
o score fijo salvo que el encargo adopte su definición y dueño.

Las medidas clínicas o restrictivas requieren autoridad y fundamento propios. Preparar
alternativas y consecuencias; identificar quién decide y ejecuta.

### 5. Preparar notificación

Resolver modalidad, receptor, canal y plazo desde la fuente aplicable al evento. Usar
sólo los campos efectivamente exigidos y disponibles. Diferenciar borrador preparado,
validación epidemiológica, autorización y envío. No introducir datos personales en
Git, pruebas o evidencia compartida. Si el envío no está autorizado, entregar la
notificación lista para el responsable y conservar el vencimiento.

### 6. Mantener y cerrar

Actualizar línea de casos y decisiones con cortes fechados, sin confundir ausencia de
registro con ausencia de evento. Definir condiciones de escalamiento, desclasificación
y cierre. Transferir seguimiento sólo cuando el receptor acepta responsabilidad.

## Fuentes, autoridad y herramientas

Las referencias sobre ENO e IAAS son conocimiento de consulta. Una cita de Decreto
7/2019, Decreto Exento 60/2022 o NT 225 no acredita por sí misma vigencia ni
aplicabilidad al evento en la fecha actual. Verificar la fuente primaria si el plazo,
la definición o la obligación gobiernan la conducta. Si un documento o formulario no
fue extraído, declarar esa pérdida.

No requiere perfil personal ni acceso a sistemas vivos. Trabaja con datos sintéticos
o agregados salvo autorización y necesidad expresa. El destino no aporta por sí solo
canales oficiales ni seguimiento autónomo.

## Casos discriminantes

- Dos casos relacionados: validar nexo, definición y línea de base; pueden constituir
  señal o brote según el evento, pero el número dos no decide universalmente.
- Dos casos aislados: no declararlos brote por cantidad; mantener vigilancia y aplicar
  la definición específica.
- Falta la circular por enfermedad: no inventar definición ni plazo; identificarla y
  escalar si existe riesgo de notificación tardía.
- La tasa aumenta tras ampliar la búsqueda: considerar cambio de detección y
  denominador antes de inferir propagación.

## Criterio de término

El trabajo termina cuando la señal tiene estado trazable, la definición y el plazo
provienen de una fuente aplicable o su ausencia está escalada, la respuesta es
proporcional y cada acción o notificación tiene responsable y seguimiento.
