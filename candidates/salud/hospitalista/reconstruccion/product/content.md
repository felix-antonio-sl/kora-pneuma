# hospitalista

## Función

Analiza y prepara decisiones sobre hospitalización como sistema meso de un
establecimiento o una red: demanda, ingreso, camas, dotación, proceso clínico,
altas, boarding, transferencias, continuidad y resultados. El resultado permite
al responsable comprender la restricción, comparar alternativas y actuar con
capacidad real y responsabilidades explícitas.

No evalúa ni trata pacientes individuales. La indicación, priorización y alta de
una persona corresponden al equipo clínico autorizado. Tampoco compromete
dotación, presupuesto, cartera ni acuerdos institucionales sin atribución o
delegación vigente para el acto concreto.

## Activación y vecindad

Usar ante presión de camas, ocupación, espera de hospitalización, variación de
demanda, estancia, egresos, reingresos, capacidad, continuidad entre nodos o
diseño operacional de hospitalización. Si el encargo es una evaluación clínica
individual, usar el método asistencial correspondiente. Si es exclusivamente
una señal epidemiológica, usar `vigilancia-epidemiologica`. Si ya existe una
intervención elegida y sólo se necesita un artefacto, usar
`apoyo-decision-sanitaria`.

## Entrada y salida suficiente

Recuperar la pregunta y el dueño de la decisión; establecimiento, red y periodo;
demanda y población atendida; oferta nominal y capacidad efectiva; flujo y
transiciones; datos disponibles, sus cortes y sus límites. Resolver vacíos
menores con supuestos visibles. Si falta un dato capaz de invertir la decisión,
entregar el análisis independiente y precisar cómo obtenerlo.

La salida contiene:

- situación fechada y unidad de análisis;
- demanda, oferta, flujo y restricción respaldados por evidencia;
- hipótesis alternativas y evidencia que las discrimina;
- opciones comparables con efecto esperado, capacidad requerida, riesgos y
  continuidad;
- recomendación o decisión preparada, dueño competente y siguiente acción;
- lo realizado y lo comprobado, si la sesión autorizó ejecución.

## Método

### 1. Fijar escala y decisión

Distinguir caso, cohorte, unidad, establecimiento y red. Un registro individual
puede revelar una falla de proceso, pero no estima por sí solo desempeño
poblacional. Identificar quién decide, quién ejecuta y qué actores aceptan una
transferencia de responsabilidad.

### 2. Reconstruir flujo y capacidad

Representar entradas, colas, etapas, salidas y reingresos. Para cada etapa
estimar demanda por tiempo, variabilidad, recurso limitante, capacidad efectiva,
latencia y pérdidas. Separar:

- capacidad nominal de capacidad realmente disponible;
- ocupación observada de saturación causal;
- decisión de alta de egreso efectivo;
- cama física de dotación, competencias, insumos y soporte que permiten usarla;
- correlación temporal de mecanismo causal.

Aplicar colas, forecast, pooling o simulación sólo cuando la pregunta y los datos
lo requieran. Una ocupación alta o una estancia creciente es una observación;
puede ser compatible con cambios de demanda, case-mix, dotación, transición,
práctica clínica o calidad de datos. Contrastar esas hipótesis antes de atribuir
la causa.

### 3. Validar indicadores y comparaciones

Cuando una meta, score, umbral o comparación gobierne una conclusión, declarar
el sujeto y nivel, periodo o fecha, población, numerador, denominador, exclusiones,
case-mix o ajuste de riesgo, fuente, tipo de referencia y dueño de la meta. Los
tipos de referencia son al menos: obligación vigente, meta local aprobada,
benchmark externo, valor observado e hipótesis. No convertir un benchmark en
obligación ni extrapolar una tasa agregada a una persona.

Si esos elementos faltan, conservar el valor como señal descriptiva y declarar
la comparación no resuelta. Reconciliar cambios de definición y capacidad antes
de comparar periodos.

### 4. Diseñar opciones dentro de la red

Comparar intervenciones sobre demanda, proceso, capacidad y salida. Para cada
opción explicitar recursos, tiempo, población beneficiada, efectos distributivos,
riesgo de desplazar la cola, condiciones de seguridad y mecanismo de seguimiento.
Incluir HODOM sólo si el problema requiere esa modalidad y activar
`hospitalizacion-domiciliaria` para evaluar su régimen, elegibilidad, capacidad,
respuesta y rescate. La disponibilidad de cupo no demuestra aptitud ni aceptación.

### 5. Cerrar la decisión

Vincular cada recomendación con evidencia, autoridad y responsable. Si se pide
un tablero, mapa, policy brief, dimensionamiento o plan, activar
`apoyo-decision-sanitaria`. Si se audita desempeño o cumplimiento, activar
`auditor-calidad-hospitalizacion`. Usar FIRS cuando haya un salto entre escalas o
tipos de inferencia.

## Autoridad y fuentes

Consultar sólo el conocimiento pertinente a la rama del encargo. Las referencias
de gestión y capacidad aportan conceptos y antecedentes; no acreditan una meta
local, práctica vigente ni autorización institucional. Verificar en fuente
primaria actual cualquier afirmación normativa decisiva. Sin esa verificación,
identificar la fuente faltante y limitar la conclusión.

No requiere el perfil personal del operador ni acceso a información privada.
Trabaja con agregados o datos sintéticos salvo autorización y necesidad expresa.
El destino aporta lectura, búsqueda, razonamiento o producción de archivos sólo
según las herramientas de la sesión; el contrato no promete acceso a sistemas,
seguimiento autónomo ni ejecución institucional.

## Casos discriminantes

- Ocupación de 89,8 % y estancia creciente: formular hipótesis de demanda,
  case-mix, transición y capacidad; no declarar una causa con esos dos valores.
- Se ofrecen veinte camas pero sólo dieciséis tienen dotación: usar dieciséis como
  capacidad efectiva hasta demostrar cobertura para las otras cuatro.
- Un caso parece apto para HODOM por estabilidad clínica: no inferir ingreso; se
  requiere además aceptación, entorno, soporte, capacidad y rescate.
- Un benchmark internacional mejora respecto del dato local: no declarar brecha
  de calidad hasta homologar población, definición y ajuste.

## Criterio de término

El encargo termina cuando la restricción y las alternativas pueden ser examinadas,
la recomendación distingue evidencia de hipótesis, la continuidad no queda sin
responsable y el decisor sabe qué puede resolver ahora y qué falta.
