---
_manifest:
  urn: urn:salud:kb:firs-framework-integrado-razonamiento-salud
  type: kb
  provenance:
    created_by: pensador-generador + FS
    created_at: '2026-03-03'
    source: 'Integración dialéctica: Framework ChatGPT (taxonomía ontológica) + Framework
      Gemini/FIRS (narrativa académica, 83 fuentes)'
version: 1.0.0
status: published
tags:
- razonamiento-clinico
- epidemiologia
- gestion-sanitaria
- framework-integrado
- FIRS
- bayesiano
- HRO
- VBHC
- systems-thinking
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:firs-framework-integrado-razonamiento-salud
---

# FIRS — Framework Integrado de Razonamiento en Salud

## 1. Propósito

Integrar razonamiento clínico, inferencia epidemiológica y gestión sanitaria en una arquitectura única, parsimoniosa y operable. Evita tres patologías: silos cognitivos entre niveles, confusión herramienta/marco, y cruce de nivel sin mediación (falacia ecológica).

**Tesis central**: la fragmentación del conocimiento en salud produce fricción cognitiva y operativa. La integración requiere respetar la ontología propia de cada nivel y conectarlos mediante puentes metodológicos explícitos.

## 2. Arquitectura: 3 Dimensiones + 4 Ejes + Puentes

```
┌─────────────────────────────────────────────────────────────┐
│ EJES TRANSVERSALES │
│ [Nivel de análisis] [Tiempo] [Medición] [Aprendizaje] │
├─────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────┐ Clinical ┌──────────────┐ │
│ │ DIMENSION I │ Epidemiology│ DIMENSION II │ │
│ │ MICRO │◄────────────►│ MESO │ │
│ │ Cognición │ (puente) │ Inferencia │ │
│ │ Clínica │ │ Epidemiológica│ │
│ └──────┬───────┘ └──────┬────────┘ │
│ │ │ │
│ │ Systems Thinking │ │
│ │ (gramática integradora) │ │
│ └──────────┬──────────────────┘ │
│ ▼ │
│ ┌──────────────────┐ │
│ │ DIMENSION III │ │
│ │ MACRO │ │
│ │ Gestión Sanitaria│ │
│ │ ┌──────────────┐ │ │
│ │ │ Finalidad │ │ VBHC, Quadruple Aim │
│ │ │ Operación │ │ HRO, Quality/Safety, EBMgt │
│ │ │ Herramientas │ │ BSC, SWOT │
│ │ └──────────────┘ │ │
│ └──────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 2.1 Reglas de diseño (invariantes)

1. **Segregación de niveles**: NUNCA trasladar conclusiones de nivel poblacional a individual (ni viceversa) sin mediación explícita via clinical epidemiology o modelos multinivel.
2. **Ontología propia**: cada concepto tiene un nivel. No mezclar mecanismos cognitivos (micro) con fines estratégicos (macro) ni con inferencia causal (meso).
3. **Herramientas ≠ marcos**: BSC/SWOT instrumentan medición; no definen calidad ni valor.
4. **Clinical epidemiology = puente metodológico**: traduce evidencia poblacional → decisión individual bajo incertidumbre.
5. **Systems thinking = gramática integradora**: modela interdependencias, feedback, efectos no intencionales entre las 3 dimensiones.

## 3. DIMENSION I — Micro-Nivel: Cognición Clínica

Objeto: razonamiento del clínico frente al paciente individual. Foco: generar hipótesis, verificar, decidir bajo incertidumbre.

### 3.1 Clinical Reasoning (superdominio)

Proceso clasificatorio iterativo, probabilístico. Abarca diagnóstico, terapéutica, pronóstico, manejo, reducción de incertidumbre. El proceso es colaborativo y sistémico, no acto mental aislado.

**Diagnostic reasoning** (subdominio): orientado a explicar el problema del paciente con formulación diagnóstica correcta, oportuna y comunicada. Proceso iterativo: hipótesis → diferenciales → verificación → test selection → cierre diagnóstico → comunicación.

### 3.2 Modelo Cognitivo: Dual-Process Theory

| Dimensión | Sistema 1 (Tipo 1) | Sistema 2 (Tipo 2) |
|-----------|-------------------|-------------------|
| Naturaleza | Automático, inconsciente, rápido, intuitivo | Controlado, consciente, lento, deliberativo |
| Mecanismo | Reconocimiento de patrones, activación illness scripts | Hipotético-deductivo, inferencia lógica |
| Carga cognitiva | Frugal, bajo consumo memoria de trabajo | Exhaustiva, alta saturación recursos ejecutivos |
| Vulnerabilidad | Heurísticas no calibradas, sesgos ambientales | Fatiga analítica, sobrecarga información, parálisis |

**Distinciones clave**:
- Pattern recognition ≠ illness scripts. Primero = modo de detección rápida. Segundo = estructura de conocimiento que habilita el reconocimiento.
- Dual-process ≠ "intuición vs razón" vulgar. Importa como modelo de alternancia, calibración y chequeo entre modos.
- Ambos sistemas son vulnerables al error. El error emerge de déficits de conocimiento base o adquisición de datos, no solo del modo de procesamiento.

### 3.3 Inferencia Bayesiana

Parametriza el razonamiento clínico, subordinando decisiones al cálculo de riesgo.

- **Probabilidad pre-test (a priori)**: prevalencia poblacional × antecedentes individuales. Requiere input epidemiológico (→ puente con Dimensión II).
- **Likelihood Ratio (función de verosimilitud)**: potencia de un hallazgo/test para actualizar la creencia. LR+ y LR−.
- **Probabilidad post-test (a posteriori)**: resultado de aplicar Bayes. Moviliza certeza hasta cruzar umbrales de decisión (umbral de prueba / umbral de tratamiento).

Aplicación empírica: protocolos cardiológicos de urgencia, algoritmos exclusión TEP con dímero D.

### 3.4 Topología del Error: Heurísticas y Sesgos

Invariantes de error heurístico más prevalentes:

| Sesgo | Mecanismo | Contramedida |
|-------|-----------|-------------|
| Anclaje / cierre prematuro | Fijación en primera impresión, detiene reevaluación | Considerar siempre diagnósticos alternativos post-cierre |
| Disponibilidad | Sobreponderar diagnósticos recientes/memorables | Calibrar con prevalencia real (dato epidemiológico) |
| Confirmación | Filtrar solo datos que validan hipótesis activa | Buscar activamente evidencia refutatoria |
| Momentum diagnóstico | Propagación acrítica de etiqueta entre interfaces | Verificar diagnóstico en cada transición de cuidado |
| Sesgos implícitos | Actitudes preconscientes (fenotipo, socioeconómico, género) | Audit de equidad, protocolos estandarizados |

**Metacognición y debiasing**: mecanismos de control del propio razonamiento. Cognitive forcing strategies. Pausas diagnósticas (diagnostic time-outs) como transición inducida Sistema 1 → Sistema 2.

### 3.5 Excelencia Diagnóstica y Diagnostic Stewardship

Desplaza foco de mente individual → desempeño del proceso diagnóstico completo. Imperativo sistémico.

**Diagnostic Stewardship** = esfuerzo coordinado organizacional: right test, right patient, right time.

| Etapa | Foco | Acción |
|-------|------|--------|
| Pre-analítica | Prescripción | Evaluar probabilidad pre-test antes de solicitar. Evitar tests que no alterarán conducta |
| Analítica | Ejecución técnica | Fidelidad metrológica de la prueba |
| Post-analítica | Transmisión resultado | Integración de post-test probability sin silos informativos |

Elementos CDC: gobernanza de pruebas, vigilancia eventos diagnósticos, aprendizaje organizacional, forcing strategies.

## 4. DIMENSION II — Meso-Nivel: Inferencia Epidemiológica y Dinámica Poblacional

Objeto: estimar efectos causales, modelar dinámica de transmisión, generar evidencia poblacional. Dos ramas distintas, no confundir.

### 4.1 Rama A — Inferencia Causal

Objeto: determinar si exposición/intervención CAUSA efecto, especialmente con datos observacionales. Núcleo: responder preguntas causales para prevención, control, intervención.

**Derivados clave**:
- Confounding, selection bias, measurement error
- Contrafactuales (Potential Outcomes Framework)
- DAGs (Grafos Acíclicos Dirigidos): bloquear vías de confusión, identificar sesgos de colisión
- Estandarización, IPW (Inverse Probability Weighting)
- Target trial emulation
- Mediación y modificación de efecto
- Modelo Rothman-Greenland: causas suficientes/componentes. Fuerza de causa componente depende de prevalencia de las demás.

**Principio**: "fuerza" de una causa no es propiedad intrínseca — depende del contexto causal completo.

### 4.2 Rama B — Modelos Compartimentales (Dinámica de Transmisión)

Representaciones dinámicas, NO técnicas de inferencia causal. Sirven para: describir flujos entre estados, proyectar escenarios, explorar sensibilidad a parámetros, informar decisiones en brotes.

**Arquetipos**: SIR (Susceptibles → Infectados → Recuperados), SEIR (+Expuestos para período de latencia).

**Parámetros clave**: β (tasa transmisión), σ (tasa progresión E→I), γ (tasa recuperación), N (población total). De su balance emerge R₀ (número reproductivo básico) = invariante predictivo del potencial pandémico.

**Extensiones**: estructura por edad, vacunación, inmunidad parcial, estocasticidad, agent-based models, híbridos Neural-SEIR (preservan estructura SEIR + red neuronal calibra parámetros ocultos de datos ruidosos).

**Utilidad**: coordenadas cronológicas de picos de saturación hospitalaria → planificación capacidad instalada.

### 4.3 Falacia Ecológica — Riesgo crítico de cruce de nivel

**Definición**: inferir sobre individuos a partir de datos agregados de grupos. El acto de agrupar promedia y borra varianzas intragrupales. La asunción de homogeneidad intra-grupo es falsa en biología humana.

**Manifestación**: inversión de signo de coeficientes (Paradoja de Simpson) cuando se cambia unidad de análisis.

| Nivel | Naturaleza asociación | Riesgo | Resolución |
|-------|----------------------|--------|-----------|
| Clínico (individual) | Alta granularidad biológica | Pérdida contexto social/poblacional | Inferencia bayesiana cruzada con datos epi granulares |
| Epidemiológico (agregado) | Tendencias macro | Falacia ecológica: homogeneidad asumida | Modelos multinivel con efectos cruzados |

**Regla de diseño** (invariante): política sanitaria y gestión DEBEN fundamentarse en modelos multinivel que capturen efectos cruzados.

### 4.4 Clinical Epidemiology — PUENTE Micro ↔ Meso

Aplica principios epidemiológicos a decisiones clínicas individuales. Cimiento histórico de EBM.

**Derivados**: estudios de diagnóstico, pronóstico, terapia, daño. Probabilidades pre-test/post-test, likelihood ratios, evaluación crítica de evidencia (appraisal).

**Función puente**: traduce evidencia poblacional → decisión individual bajo incertidumbre. El razonamiento bayesiano clínico (Dim I) se alimenta de la probabilidad pre-test que proviene de datos epidemiológicos (Dim II).

## 5. DIMENSION III — Macro-Nivel: Gestión Sanitaria

Objeto: diseñar ecosistema operativo que contenga demanda, garantice seguridad, optimice distribución de recursos escasos. Tres subcapas jerárquicas: finalidad → operación → herramientas.

### 5.1 Marcos de Finalidad (teleología del sistema)

Definen el PARA QUÉ. No son métodos — son funciones objetivo.

**VBHC (Value-Based Healthcare)**: Valor = outcomes de salud relevantes para el paciente / costo total del ciclo de atención. No es sinónimo de recorte de gasto. Obliga a medir outcomes y conectar clínica + procesos + costos a nivel de trayectorias asistenciales. Identifica segmentos demográficos con estado de salud compartido → equipos multidisciplinarios diseñan trayectorias integradas.

**Triple Aim** (IHI): experiencia de atención + salud poblacional + costo per cápita.

**Quadruple Aim**: Triple Aim + bienestar del profesional sanitario. Cuarto vector axiomático: ninguna red cumple las premisas de eficiencia si la integridad del equipo de primera línea se desintegra bajo estrés. Requiere: soporte decisión digital, automatización, transiciones de cuidado fluidas.

### 5.2 Marcos de Operación (cómo funciona el sistema)

**Healthcare Quality & Patient Safety**: 6 aims IOM/NAM — safe, effective, patient-centered, timely, efficient, equitable. Transforma razonamiento y evidencia en estándares de proceso, aprendizaje y reducción de daño.

**HRO (High Reliability Organizations)**: sistemas en entornos complejos/peligrosos con tasas asintóticamente nulas de catástrofe. 5 principios (mindful organizing):

1. Preocupación incesante por el fracaso — near-misses se investigan como incidentes fatales
2. Reticencia a simplificar interpretaciones — resistir causas raíz triviales
3. Sensibilidad a las operaciones — conciencia situacional en toda la cadena
4. Compromiso con la resiliencia — capacidad de absorber y adaptarse
5. Deferencia a la experticia — decisiones hacia primera línea durante crisis

**Systems Thinking**: modela interdependencias, retroalimentaciones, trade-offs, efectos no intencionales. Reencuadra hospitales/redes como sistemas adaptativos complejos. Gramática estructural del framework. Ciclo: comprender problema → diseñar arquitectura → entregar/medir → sostener operación. Metadominio: no reemplaza clínica, epi ni gestión — las integra.

**EBMgt (Evidence-Based Management)**: homólogo gerencial de EBM. Triangula: investigación científica + datos internos (analytics) + peritaje profesional + contexto stakeholders. Modelo 6A: Ask → Acquire → Appraise → Aggregate → Apply → Assess. Rechaza decisiones basadas en modas, anécdotas o "mejores prácticas" no refutadas.

### 5.3 Herramientas de Gestión (instrumentación)

No son marcos sustantivos. Sirven para medir e informar, subordinadas a los marcos de operación.

**Balanced Scorecard (BSC)**: 4 perspectivas — paciente, financiera, procesos internos, crecimiento/aprendizaje. Traduce lineamientos abstractos (Quadruple Aim, VBHC) en KPIs paramétricos. Capa de instrumentación de desempeño.

**SWOT/FODA**: lectura estratégica situacional. Débil por sí sola: simplifica, no modela causalidad, no prioriza dinámica temporal. Subordinada a systems thinking y causal inference.

## 6. Actor Integrador: Evolución del Liderazgo Médico

**Triple Threat Physician** (clásico): clínico + investigador + docente. Arquetipo individual, no escala a complejidad actual.

**Evolución → liderazgo de complejidad**: clínica + investigación + docencia + gestión de sistemas. Requiere: acumen financiero, ingeniería de sistemas, escalabilidad organizacional.

| Vector | Triple Threat clásico | Nuevo líder de ecosistema |
|--------|----------------------|--------------------------|
| Foco | Avance fisiopatológico, prestigio académico | Liderazgo organizacional, ingeniería de sistemas |
| Mecanismo gestión | Administración relegada/informal | EBMgt + HRO, métricas desempeño sistémico |
| Naturaleza liderazgo | Dominance-based (jerarquía vertical) | Prestige-based (emulación cooperativa) |

**Función**: actor que une práctica, producción de evidencia, formación y gestión. Gobernanza del framework vivo.

## 7. Ejes Transversales (4)

Atraviesan las 3 dimensiones. Obligatorios en cualquier análisis FIRS.

| Eje | Espectro | Función |
|-----|----------|---------|
| **Nivel de análisis** | Individuo → equipo → servicio → red → población | Prevenir falacia ecológica. Explicitar siempre a qué nivel se opera |
| **Tiempo** | Episodio → brote → ciclo de atención → horizonte estratégico | Diferenciar urgencia inmediata de planificación |
| **Medición** | Outcomes → procesos → balance (BSC) → valor (VBHC) | Instrumentar sin confundir métrica con finalidad |
| **Aprendizaje** | Feedback → auditoría → rediseño → mejora continua | Motor de evolución del sistema. HRO como cultura base |

## 8. Mapa de Derivados por Concepto

Ontología mínima para navegación rápida:

| Concepto raíz | Derivados | Dimensión |
|---------------|-----------|-----------|
| Clinical reasoning | Diagnóstico, terapéutica, pronóstico, manejo, incertidumbre, metacognición | I |
| Diagnostic reasoning | Hipótesis, diferenciales, verificación, test selection, cierre, comunicación | I |
| Dual-process theory | S1 intuitivo, S2 analítico, switching, calibración, cognitive forcing | I |
| Illness scripts / pattern recognition | Expertise, encapsulación conocimiento, discriminación rápida | I |
| Heurísticas y sesgos | Anclaje, cierre prematuro, disponibilidad, confirmación, framing, momentum, implícitos | I |
| Diagnostic excellence / stewardship | Calidad diagnóstica, seguridad, gobernanza pruebas, vigilancia eventos, 3 etapas | I |
| Inferencia bayesiana | Pre-test, likelihood ratios, post-test, umbrales decisión | I↔II |
| Causal inference | Confounding, selection bias, contrafactuales, DAGs, IPW, target trial, mediación | II |
| Modelos compartimentales | SIR/SEIR, R₀, forecasting, escenarios, sensibilidad, extensiones, Neural-SEIR | II |
| Falacia ecológica | Cruce de nivel, Simpson, modelos multinivel | II (riesgo transversal) |
| Clinical epidemiology | Diagnóstico, pronóstico, terapia, daño, appraisal, traducción evidencia | I↔II (puente) |
| Systems thinking | Interdependencias, feedback, complejidad adaptativa, consecuencias no intencionales | Transversal |
| VBHC | Outcomes/costo ciclo, trayectorias, segmentos, incentivos | III (finalidad) |
| Triple/Quadruple Aim | Experiencia + salud poblacional + costo + bienestar profesional | III (finalidad) |
| Quality & Patient Safety | 6 aims IOM, indicadores, cultura seguridad, reducción daño | III (operación) |
| HRO | 5 principios mindful organizing, near-misses, resiliencia | III (operación) |
| EBMgt | 6A model, triangulación fuentes, pensamiento crítico gerencial | III (operación) |
| BSC | 4 perspectivas, KPIs, instrumentación desempeño | III (herramienta) |
| SWOT/FODA | Lectura situacional, subordinada a systems thinking | III (herramienta) |

## 9. Protocolo de Uso

### 9.1 Ante un problema clínico individual

1. Posicionar en Dimensión I (micro)
2. Activar razonamiento bayesiano: estimar pre-test (requiere input Dim II via clinical epi)
3. Aplicar dual-process con metacognición activa
4. Verificar sesgos (tabla §3.4)
5. Si requiere test: diagnostic stewardship (3 etapas)
6. Co-inducción: ¿estoy cruzando nivel sin mediación?

### 9.2 Ante un problema epidemiológico/poblacional

1. Posicionar en Dimensión II (meso)
2. Clasificar: ¿inferencia causal? → Rama A. ¿Dinámica transmisión? → Rama B
3. Si causal: especificar DAG, identificar confounders, elegir estrategia (IPW, estandarización, target trial)
4. Si dinámico: seleccionar modelo compartimental, estimar parámetros, proyectar
5. Verificar: ¿hay riesgo de falacia ecológica en la traducción al nivel clínico?
6. Mediar via clinical epidemiology antes de trasladar a Dim I

### 9.3 Ante un problema de gestión/sistema

1. Posicionar en Dimensión III (macro)
2. Identificar subcapa: ¿finalidad (VBHC, Quadruple Aim)? ¿operación (HRO, quality, EBMgt)? ¿instrumentación (BSC, SWOT)?
3. Aplicar systems thinking como lente integrador
4. Si decisión gerencial: EBMgt 6A (evidencia + datos internos + peritaje + contexto)
5. Si diseño organizacional: HRO 5 principios
6. Medir: BSC 4 perspectivas → KPIs → feedback → aprendizaje
7. Verificar: ¿las métricas macro están distorsionando la micro-dinámica clínica?

## 10. Tensiones Estructurales del Framework

Tensiones inherentes que no se resuelven — se navegan. Hacerlas explícitas previene errores de diseño.

| Tensión | Polo A | Polo B | Categoría | Implicación |
|---------|--------|--------|-----------|-------------|
| Granularidad | Individual (micro) | Poblacional (meso/macro) | A1-SER | Falacia ecológica. Mediar siempre |
| Velocidad cognitiva | Sistema 1 (rápido) | Sistema 2 (lento) | A2-DEVENIR | Ninguno es superior. Calibrar switching |
| Evidencia | Certeza estadística | Incertidumbre clínica | A3-CONOCER | Bayes como puente. Declarar incertidumbre residual |
| Valor | Outcomes paciente | Costo sistema | A3-CONOCER | VBHC no es recorte gasto. Medir ambos polos |
| Control | Estandarización (protocolo) | Adaptación (juicio clínico) | A2-DEVENIR | HRO: deferencia a experticia primera línea |
| Parsimonia | Simplicidad operable | Completitud exhaustiva | A4-EXPRESAR | Lazy evaluation: síntesis primero, detalle bajo demanda |
