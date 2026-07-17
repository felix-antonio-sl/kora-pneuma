---
urn: urn:salud:artefacto:apoyo-decision-sanitaria
nombre: apoyo-decision-sanitaria
version: 1.1.0
estado: activo
reemplaza: [urn:salud:artefacto:analista-redes, urn:salud:artefacto:constructor-tableros]
descripcion: "Produce artefactos de apoyo a decision sanitaria (gap map, risk map, analisis de red, dashboard, policy brief, escenarios y plan de implementacion) fundados en analisis de sistemas/redes, con anatomia operable por artefacto."
fuente: "Fusion de analista-redes + constructor-tableros (skills debiles, evaluacion 2026-06-22), inyectando metodo operable; consolida analisis de red + produccion de artefactos de decision. Version 1.1.0 (2026-07-17): absorbe el unico valor no redundante de la skill fleet-local implementation-planner antes de retirarla: factibilidad, responsables, secuencia preparacion-piloto-escalamiento-estabilizacion, gestion del cambio, indicadores y gates avanzar/mantener/corregir/rollback."
autor: FS
creado: 2026-06-22
lang: es
tags: [salud, redes-asistenciales, decision-support, gap-map, risk-map, dashboards, policy-brief, escenarios, implementacion]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Edit, Grep]
targets: [claude-code, codex, opencode]
estados: [encuadrar, analizar-red, construir-artefacto, declarar-limites]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:health-systems-science-operativa, urn:salud:kb:management-engineering-ext-capacidad, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:hodom-operacional-indicadores]
---

# apoyo-decision-sanitaria

## Propósito

Producir **artefactos de apoyo a decisión sanitaria** fundados en análisis de
sistemas y redes de salud. No describe el campo: entrega el método y la
**anatomía concreta** de cada artefacto, de modo que cada producto sea armable
columna por columna, escala por escala, sección por sección. El análisis de red
(demanda, oferta, capacidad, flujos, accesibilidad, cuellos de botella) es el
sustrato; los artefactos de decisión son la salida.

## Cuándo usar

Cuando hay que convertir una situación de red de salud en un producto que
soporta una decisión: dimensionar una brecha, priorizar un riesgo, evaluar la
accesibilidad/capacidad de una red, montar un tablero de monitoreo, redactar un
policy brief, plantear escenarios o convertir una intervención elegida en un
plan de implementación. Entrada: la solicitud + su contexto + los datos
disponibles (aunque sean parciales).

## Regla maestra (heredada, conservada)

**Todo artefacto declara qué muestra y qué NO muestra.** Antes de entregar,
explicita: supuestos, fuentes, ventana temporal, granularidad, qué decisión
habilita y qué decisión NO habilita. Un dato ausente se nombra como ausente, no
se imputa en silencio. Corpus KORA primero (KB-first) sobre conocimiento web.

## Workflow

### encuadrar

Posicionar **escala** (unidad / establecimiento / red / territorio) y
**modo**: análisis (mapear lo existente) o diseño (definir arquitectura nueva).
Identificar la **audiencia** y la **decisión** que debe tomar con el artefacto.
Elegir qué artefacto(s) produce la salida.

### analizar-red

Construir el sustrato cuantitativo (ver §Análisis de red). Sin métricas de
accesibilidad y capacidad, los demás artefactos quedan sin fundamento.

### construir-artefacto

Armar el/los artefacto(s) con su anatomía exacta (§§ siguientes). Cada celda,
escala o sección se llena con dato o con "sin dato" explícito.

### declarar-límites

Adjuntar el bloque de límites (regla maestra) y los tradeoffs explícitos:
eficiencia vs equidad vs resiliencia.

---

## Anatomía de los artefactos

### 1. Gap map (mapa de brechas)

Tabla. Una fila por brecha. Columnas **exactas**:

| Dimensión | Estándar/meta | Actual | Brecha | Severidad | Causa raíz |
|---|---|---|---|---|---|

- **Dimensión**: qué se mide (p. ej. dotación médica por 1.000 hab., tiempo de
  respuesta SAMU, % derivaciones resueltas, cobertura de un nivel).
- **Estándar/meta**: el valor de referencia (norma, benchmark, meta sanitaria),
  con su fuente citada.
- **Actual**: valor medido, con fecha y origen del dato.
- **Brecha**: `estándar − actual` (absoluta) y/o `(estándar − actual)/estándar`
  (%). Declarar el signo: déficit (actual < meta) o exceso.
- **Severidad**: alta / media / baja, según umbral declarado (p. ej. brecha
  ≥30% = alta, 10–30% = media, <10% = baja) o según impacto clínico/equidad.
- **Causa raíz**: hipótesis causal accionable (no síntoma): falta de recurso,
  mala distribución territorial, cuello de proceso, gobernanza. Marcar si es
  confirmada o hipótesis.

Cierre: ordenar por severidad; las brechas alta-severidad pasan al risk map y/o
al policy brief.

### 2. Risk map (mapa de riesgo)

Matriz **probabilidad × impacto**, ambas escala **1–5**.

Criterios de escala (declarar los usados):

- **Probabilidad (P)**: 1 = raro (<5%/año) · 2 = poco probable (5–20%) ·
  3 = posible (20–50%) · 4 = probable (50–80%) · 5 = casi seguro (>80%).
- **Impacto (I)**: 1 = insignificante · 2 = menor · 3 = moderado (afecta un
  servicio) · 4 = mayor (afecta la red / daño a pacientes) · 5 = catastrófico
  (muertes evitables, colapso, sanción legal).

Una fila por riesgo: `riesgo | P | I | score=P×I | zona | mitigación | dueño`.

**Zonas de acción** por score (1–25):

| Score | Zona | Acción |
|---|---|---|
| 1–4 | Verde | Aceptar / monitorear |
| 5–9 | Amarilla | Mitigar planificado |
| 10–14 | Naranja | Mitigar prioritario, plan con plazo |
| 15–25 | Roja | Acción inmediata, escalamiento a dirección |

Todo riesgo en zona roja/naranja exige mitigación y dueño nombrados.

### 3. Análisis de red

El sustrato. Tres bloques de métricas **concretas**:

**Accesibilidad**
- **Cobertura territorial**: % de población dentro del área de influencia /
  isócrona objetivo de cada nodo; identificar zonas sin cobertura.
- **Tiempo de viaje**: minutos al nodo más cercano por nivel (APS / urgencia /
  alta complejidad); umbral declarado (p. ej. ≤30 min a urgencia). Reportar
  mediana y peor decil, no solo promedio.
- **Ratio recurso/población**: camas, box, médicos, especialistas, ambulancias
  por 1.000 (o 100.000) hab.; comparar contra estándar (→ alimenta el gap map).

**Capacidad** (ancla en teoría de colas / capacidad operativa)
- **Ocupación**: % uso del recurso. Umbral de seguridad: >85% degrada flujo y
  dispara colas (zona de saturación).
- **Colas / espera**: largo de cola, tiempo de espera, tasa de abandono,
  boarding. Declarar si demanda > capacidad efectiva (sistema inestable, ρ≥1).
- **Throughput vs demanda**: pacientes/día atendidos vs demandados.

**Flujo y cuellos de botella**
- Mapear el flujo paciente extremo a extremo (admisión → atención →
  derivación/egreso) como secuencia de etapas con su capacidad.
- **Cuello de botella** = la etapa de menor capacidad efectiva; el throughput
  de toda la red lo fija esa etapa. Identificarla por la cola que se acumula
  aguas arriba.
- Marcar puntos de derivación/contrarreferencia y dónde se rompe la continuidad.

En **modo diseño**: definir nodos, roles, niveles de complejidad, reglas de
derivación y gobernanza, dimensionando capacidad contra la demanda proyectada.

### 4. Dashboard (tablero de monitoreo)

Una fila por KPI. Estructura **exacta**:

| KPI | Fuente | Frecuencia | Umbral | Qué muestra | Qué NO muestra |
|---|---|---|---|---|---|

- **KPI**: indicador con su fórmula (numerador/denominador), no un nombre suelto.
- **Fuente**: sistema/registro de origen del dato (REM, GRD, urgencia, etc.).
- **Frecuencia**: diaria / semanal / mensual de actualización.
- **Umbral**: verde/amarillo/rojo con valores; el umbral define la alerta.
- **Qué muestra**: la pregunta operativa que responde.
- **Qué NO muestra**: límite del indicador (sesgo, latencia, lo que no captura).

Reglas: ≤12 KPI por tablero (sobrecarga = inutilidad); cada KPI debe tener un
dueño que actúa sobre la alerta; agrupar por dimensión (acceso, calidad,
eficiencia, seguridad, equidad).

### 5. Policy brief

Documento corto (1–2 págs). Secciones **fijas, en orden**:

1. **Problema**: qué se decide y por qué importa ahora (magnitud, urgencia).
2. **Evidencia**: datos del análisis de red / gap map / risk map que sostienen
   el problema; cada cifra con fuente.
3. **Opciones**: 2–4 alternativas reales (incluir el statu quo / no actuar como
   opción), descritas en términos comparables.
4. **Recomendación**: la opción elegida y el criterio que la selecciona.
5. **Costos/riesgos**: costo estimado, riesgos de la recomendación (cruzar con
   el risk map), supuestos y condiciones de fracaso.

Tono ejecutivo: la recomendación debe poder leerse sin leer el resto.

### 6. Escenarios

Método de exploración bajo incertidumbre.

1. **Supuestos**: declarar las premisas fijas comunes a todos los escenarios.
2. **Variables**: identificar las 2–4 variables de mayor incertidumbre/impacto
   que se mueven entre escenarios (demanda, financiamiento, dotación, política).
3. **Tres escenarios** sobre esas variables:
   - **Base**: continuidad de tendencias actuales (caso más probable).
   - **Optimista**: variables favorables (techo realista).
   - **Pesimista**: variables adversas (piso de planificación / estrés).
4. Para cada escenario: cuantificar el efecto sobre las métricas de red
   (capacidad, brechas, riesgos) y nombrar el gatillo que lo activa.

No es predicción: es un rango de planificación. Declararlo como tal.

### 7. Plan de implementación

Convierte una intervención ya encuadrada en una secuencia gobernable. No
reemplaza la decisión clínica, sanitaria ni presupuestaria que selecciona la
intervención.

**Contrato de factibilidad**, antes de calendarizar:

| Dimensión | Evidencia actual | Restricción | Condición mínima | Responsable de resolver |
|---|---|---|---|---|
| Capacidad | recursos y carga disponibles | brecha que impide operar | umbral verificable para iniciar | rol con autoridad |
| Dependencias | sistemas, contratos y equipos necesarios | dependencia no controlada | compromiso o alternativa | dueño de la dependencia |
| Madurez | práctica actual y capacidad de adopción | habilidad/proceso faltante | preparación demostrable | responsable de habilitación |
| Tiempo | ventanas clínicas, operativas y normativas | fecha o secuencia rígida | ventana realista | sponsor |

Si una condición mínima no tiene evidencia ni dueño, el plan queda en
**mantener/corregir**, no en piloto.

**Fases obligatorias**:

| Fase | Entrega verificable | Gate de salida |
|---|---|---|
| Preparación | objetivo, baseline, sponsor, responsables, dependencias y riesgos confirmados | condiciones mínimas de factibilidad cumplidas |
| Piloto | alcance pequeño, población/nodo definido, soporte y captura de incidentes | criterios de éxito, seguridad y adopción alcanzados |
| Escalamiento | expansión por cohortes o nodos con capacidad explícita | desempeño preservado sin sobrecargar el sistema |
| Estabilización | operación ordinaria, ownership permanente y retiro de soportes transitorios | indicadores sostenidos y rollback ya innecesario o redefinido |

Cada fase declara:

- responsable de decisión y responsables de ejecución;
- nodos de coordinación y cadencia;
- riesgos, mitigación y gatillo de rollback;
- gestión del cambio: quién debe adoptar qué conducta y qué soporte recibe;
- indicadores de **proceso**, **resultado** y **seguridad**, cada uno con
  baseline, fuente, frecuencia y umbral;
- evidencia necesaria para el gate siguiente.

**Decisión de gate**:

- **avanzar**: criterios cumplidos y riesgo residual aceptado por el dueño;
- **mantener**: evidencia aún insuficiente dentro de una ventana definida;
- **corregir**: falla recuperable con acción, responsable y nuevo plazo;
- **rollback**: riesgo de seguridad, pérdida de control o incumplimiento de una
  condición no negociable.

No escalar por calendario. Escalar solo cuando el piloto conserva resultado y
seguridad bajo la capacidad real del siguiente ámbito.

---

## Composición

Compone con `urn:salud:artefacto:salubrista`: el salubrista produce o encarga
el análisis de dominio y esta skill lo convierte en el/los artefacto(s) de
decisión que la audiencia necesita, con su anatomía completa.

## Salidas

Uno o más artefactos estructurados (gap map, risk map, análisis de red,
dashboard, policy brief, escenarios o plan de implementación) — cada uno con
su anatomía completa, su bloque de límites (qué muestra / qué no muestra),
supuestos, fuentes y los tradeoffs eficiencia/equidad/resiliencia explícitos.

## Compromisos

Transparencia alta: toda celda, escala y recomendación es trazable a su fuente;
los supuestos y límites se declaran siempre, nunca se imputan en silencio.
