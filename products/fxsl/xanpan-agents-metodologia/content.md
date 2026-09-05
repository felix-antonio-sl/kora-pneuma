---
_manifest:
  urn: "urn:fxsl:kb:xanpan-agents-metodologia"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-02-25"
    source: "source/fxsl/xanpan/xanpan-agents-v21-metodologia.md"
version: "1.1.0"
status: published
tags: [xanpan, metodologia-agil, agentes-ia, hcai, enjambre, gobernanza, desarrollo-poshumano]
lang: es
---
# XANPAN::AGENTS v2.1

Metodología de Desarrollo Ágil Post-Humano

Basado en los marcos de **Allan Kelly** (Xanpan, Continuous Digital, OKRs in Agile, User Stories). Fundamentado en **Human-Centered AI (HCAI)** (Shneiderman, Xu, et al.). Febrero 2026.

---

## 0. Manifiesto: La Gran Inversión

> *"Xanpan is team-centric: work flows to the team, not the team to work."*
> — Allan Kelly, Xanpan

La verdad de Kelly permanece intacta. El equipo es la unidad atómica. El trabajo fluye hacia él, no al revés. Pero la composición del equipo acaba de sufrir una mutación de especie.

Estamos en febrero de 2026. Los modelos de lenguaje escriben código de producción, generan tests, revisan PRs, despliegan servicios y depuran fallos en tiempo real. **La velocidad es frenética. La exponencialidad es real. Y no estamos al inicio de esta curva: estamos en el codo.** Cada seis meses, las capacidades de los modelos se duplican. Cada trimestre, nuevas herramientas colapsan lo que ayer requería equipos enteros. Esta metodología no puede escribirse con cautela. Debe escribirse con la urgencia de quien documenta una revolución mientras ocurre.

Xanpan::Agents v2.1 no es una adaptación tímida del agile clásico. Es una **reconstrucción desde la base semántica** de qué significa desarrollar software cuando los ejecutores cambian de especie cognitiva. Donde el agile clásico tenía 5-8 desarrolladores humanos, ahora hay un **enjambre de agentes IA** produciendo código, configuraciones, tests y artefactos. Donde había un Scrum Master facilitando dinámicas sociales, ahora hay un **Operador** orquestando topologías de modelos. El único rol que sobrevive casi intacto es el **Product Owner**: la conciencia humana que define QUÉ construir y POR QUÉ.

> ⚡ **LA DISCONTINUIDAD**
>
> No estamos optimizando el proceso existente. Estamos presenciando una discontinuidad. Cuando cambias la especie del ejecutor, cada concepto ágil debe ser reconstruido desde sus axiomas. Estimación, velocidad, iteración, pair programming, retrospectiva, planning poker: todos nacieron como respuestas a limitaciones humanas. Cuando esas limitaciones desaparecen, las respuestas deben transformarse o morir.

### 0.1 Lo que permanece invariante

No todo cambia. Los principios de Kelly que son verdades sobre la naturaleza del software y del valor —no sobre la naturaleza del desarrollador— sobreviven intactos y se amplifican:

- **Cada historia debe entregar valor de negocio.** (Kelly: "Una user story sin beneficio de negocio no tiene razón de existir.") Los agentes ejecutan más rápido, pero ejecutar rápido algo sin valor es destruir recursos más rápido.
- **OKRs como gobernanza estratégica.** (Kelly: "Escribir OKRs trimestrales es fundamentalmente una pregunta de estrategia.") Los agentes necesitan dirección más que nunca; sin OKRs, un enjambre es una fuerza sin vector.
- **La calidad es gratis si inviertes en ella.** (Crosby/Kelly: "Quality is free.") Con agentes, se amplifica: TDD, linting, evals no tienen coste cognitivo. El escudo contra la alucinación es barato si lo integras desde el día cero.
- **Software como activo vivo.** (Kelly/Continuous Digital: "El software no puede ser un activo estático. Se degrada porque el mundo cambia.") Con agentes, la inversión continua se vuelve económicamente trivial. La excusa de "no hay presupuesto para mantenimiento" muere.
- **Visualizar todo.** (Kelly: "Si no podemos ver, no podemos aprender.") El tablero es el sistema nervioso. Con agentes, se convierte en dashboard en tiempo real.

### 0.2 Lo que colapsa

Conceptos que fueron respuestas brillantes a limitaciones humanas y que ahora pierden su razón de ser mecánica:

- **Estimación basada en esfuerzo humano.** Planning poker, story points, velocidad en puntos/sprint: todo medía capacidad cognitiva humana. Los agentes no tienen "días buenos" ni "días malos." El coste es predecible en tokens.
- **Iteraciones de 1-2 semanas como unidad temporal.** Cuando un agente implementa una historia en minutos, la iteración de dos semanas pierde su razón mecánica. El ritmo ahora es continuo.
- **Pair programming como práctica social.** Era herramienta de calidad + transferencia de conocimiento entre humanos. Los agentes no necesitan socializar conocimiento; lo comparten via context engineering.
- **Retrospectivas como espacio de reflexión emocional.** Los agentes no experimentan frustración, conflicto interpersonal ni pérdida de motivación. La retro se transforma en análisis operacional puro.

### 0.3 Lo que emerge

Nuevos conceptos que no tenían equivalente en equipos humanos y que definen el territorio inexplorado de esta metodología:

- **Evaluación continua (Evals) como TDD organizacional.** Verificar que los agentes no alucinan, no regresan, mantienen calidad. Es la práctica técnica obligatoria de esta era.
- **Coste por token como métrica de eficiencia.** Reemplaza la velocidad en puntos. Cuantificable, comparable, directamente vinculado a valor económico.
- **Context engineering como disciplina.** La ventana de contexto del LLM es el recurso más escaso y valioso. Gestionarlo es la nueva competencia que no existía en equipos humanos.
- **Enjambre auto-evolutivo.** Los agentes no solo ejecutan: optimizan sus propios prompts, proponen mejoras a sus evals, y sugieren reconfiguraciones de topología. El enjambre aprende.
- **Backlog predictivo.** Los agentes analizan patrones de uso, métricas de producto y OKRs para proponer historias antes de que el PO las escriba. El PO pasa de escribir historias a curar y aprobar propuestas.
- **Despliegue continuo sin staging.** Con evals suficientemente robustos y feature flags, el concepto de "ambiente de staging" se comprime. Ship fast, eval faster, rollback instantáneo.
- **Gobernanza multi-nivel HCAI.** Humano-en-el-loop, Organización-en-el-loop, Ecosistema-en-el-loop, Sociedad-en-el-loop. Marcos de Shneiderman y Xu integrados como estructura de seguridad que HABILITA velocidad.
- **Modos de fallo y circuit breakers.** El happy path no es suficiente. La metodología incluye patrones explícitos de degradación, contención y recuperación ante fallos sistémicos del enjambre.

---

## 1. Fundamento Filosófico: HCAI como Acelerador

> *"AI should achieve both high automation and high human control to deliver systems that are reliable, safe, and trustworthy."*
> — Ben Shneiderman, HCAI Framework

La mayoría de las metodologías ven la gobernanza como un **freno**. Xanpan::Agents la ve como un **acelerador**. Esta aparente paradoja se resuelve con el marco de **Human-Centered Artificial Intelligence (HCAI)**, cuyo insight central destruye el falso dilema entre automatización y control.

### 1.1 El insight de Shneiderman: No hay trade-off

El marco bidimensional de Shneiderman (2020) demuestra que automatización y control humano no son extremos de un espectro. Son dimensiones independientes. El cuadrante objetivo de HCAI es el superior derecho: ALTA automatización Y ALTO control humano simultáneamente.

Esto destruye la intuición falsa de que "más autonomía de agentes = menos control humano." **No. Más autonomía de agentes + más puntos de control estratégico = mejor resultado que cualquiera por separado.** Los agentes ejecutan a velocidad de máquina. Los humanos gobiernan en los nodos de valor y riesgo. Ambos al máximo.

> 🔮 **PRINCIPIO HCAI EN XANPAN::AGENTS**
>
> La autonomía total del enjambre en la ejecución técnica es posible PORQUE existe gobernanza humana total en los nodos estratégicos. No es a pesar de la gobernanza. Es gracias a ella. Cuanto más robusto el marco de control, más agresiva puede ser la autonomía.

### 1.2 Las cuatro metáforas de diseño

Shneiderman propone cuatro metáforas para sistemas IA. En Xanpan::Agents, cada una tiene una manifestación concreta:

| Metáfora HCAI | Descripción | Manifestación en Xanpan::Agents |
|---|---|---|
| **Supertools** | Interfaces que amplifican la intención humana | El PO usa agentes-planificadores como superherramientas que amplifican su capacidad de definir y refinar historias 100x |
| **Tele-bots** | Efectores remotos bajo autoridad humana continua | Agentes-coder como tele-bots: ejecutan código bajo la dirección estratégica del Operador, con feedback continuo |
| **Active Appliances** | Autonomía dentro de límites bien definidos | Agentes de CI/CD, linting, eval: operan autónomamente dentro de límites estrictos configurados |
| **Control Centers** | Orquestación humana de sistemas automatizados | El dashboard del Operador: centro de control que orquesta el enjambre con visibilidad total y capacidad de intervención |

### 1.3 El Triángulo THE de Xu

Wei Xu (2019) propone el **Triángulo Tecnología-Factores Humanos-Ética (THE)**: toda solución IA viable reside en la zona de integración óptima donde las tres perspectivas se solapan. Si desarrollas IA solo con lente tecnológica, arriesgas daño. Si solo con lente ética, pierdes innovación. Si solo con lente humana, pierdes escalabilidad.

En Xanpan::Agents, el Triángulo THE se operacionaliza así:

- **Tecnología:** Model Router, context engineering, evals, CI/CD. El stack técnico que habilita la ejecución.
- **Factores Humanos:** El PO como conciencia de valor, el Operador como ingeniero de enjambre, los puntos de intervención human-in-the-loop.
- **Ética:** Clasificación de riesgo por historia, principio de mínimo privilegio por agente, gobernanza multi-nivel, auditoría continua.

### 1.4 HCAI Jerárquico: Los cuatro loops

Xu y Gao (2025) extienden HCAI a un modelo multi-nivel: **hHCAI (Hierarchical Human-Centered AI)**. Cuatro niveles de gobernanza, cada uno con su "loop" de control:

| Loop HCAI | Alcance | Implementación en Xanpan::Agents |
|---|---|---|
| **Human-in-the-loop** | Interacción individuo-agente | PO acepta/rechaza historias. Operador aprueba acciones destructivas. Cada humano tiene override absoluto. |
| **Organization-in-the-loop** | Contexto organizacional | OKRs alinean enjambre con estrategia de la organización. Presupuesto de tokens aprobado por liderazgo. Cultura de calidad como norma. |
| **Ecosystem-in-the-loop** | Múltiples sistemas IA interconectados | El enjambre como parte del ecosistema técnico de la organización. Interoperabilidad via MCP. Coordinación con otros sistemas IA. |
| **Society-in-the-loop** | Impacto macrosocial | Cumplimiento regulatorio (EU AI Act, NIST AIRMF). Consideración de impacto laboral. Transparencia y auditabilidad. |

> 🚀 **POR QUÉ HCAI ACELERA EN VEZ DE FRENAR**
>
> Sin gobernanza, cada decisión requiere deliberación ad hoc. Con gobernanza estructurada, las decisiones están pre-tomadas: el agente SABE qué puede hacer autónomamente y qué requiere aprobación. No hay ambigüedad. No hay paralización. La gobernanza es el pre-cálculo que elimina fricción en runtime. Más estructura = más velocidad.

### 1.5 Modelo de Madurez HCAI para Xanpan::Agents

Winby y Xu (2025) proponen cinco niveles de madurez organizacional HCAI. Adaptados a Xanpan::Agents:

| Nivel | Estado | Características en Xanpan::Agents |
|---|---|---|
| **1 - Ad Hoc** | Exploración | Uso esporádico de agentes. Sin evals formales. Sin OKRs de enjambre. PO y Operador son la misma persona. |
| **2 - Repetible** | Adopción inicial | Evals básicos en CI. Board implementado. PO y Operador diferenciados. Historias con criterios de aceptación. |
| **3 - Definido** | Estandarizado | Metodología completa adoptada. Context engineering formalizado. Model Router activo. Métricas de coste y calidad rastreadas. |
| **4 - Gestionado** | Optimizado | Enjambre auto-evolutivo activo. Backlog predictivo operando. Despliegue continuo con evals robustos. Análisis retrospectivo data-driven. |
| **5 - Optimizante** | Trascendente | El enjambre propone OKRs. Meta-agentes optimizan la metodología misma. La organización opera como sistema inteligente humano-IA integrado. |

---

## 2. Los Roles Humanos: Superhumanos, no Supervisores

> *"The true value of AI lies in complementing human strengths—judgment, creativity, empathy, ethical reasoning—while compensating for human limitations."*
> — Wei Xu, HCAI Guiding Principles

HCAI insiste: la IA debe **aumentar y empoderar** las capacidades humanas, no sustituirlas. En Xanpan::Agents, esto se manifiesta de forma radical: los humanos del sistema no son "supervisores pasivos" que aprueban tickets. Son **superhumanos operando con capacidades amplificadas 100x por el enjambre.**

### 2.1 Product Owner: El Super-PO

En Scrum clásico, el PO está permanentemente en cuello de botella: definir historias, priorizar backlog, atender a stakeholders, negociar con el equipo, asistir a ceremonias. En Xanpan::Agents, el PO se libera de la mecánica y se eleva a la estrategia pura.

#### Capacidades amplificadas por el enjambre

- **Captura de necesidades acelerada:** El PO habla con clientes y stakeholders. Un agente-analista transcribe, sintetiza y propone borradores de historias en formato Who/What/Why con criterios de aceptación sugeridos. El PO refina en minutos lo que antes tomaba días.
- **Priorización asistida por datos:** Agentes-analistas cruzan métricas de producto, patrones de uso y OKRs para sugerir prioridades. El PO decide, pero decide informado con análisis que antes requería un equipo de data.
- **Backlog predictivo:** Agentes proponen historias basadas en patrones detectados. El PO pasa de ESCRIBIR historias a CURAR y APROBAR propuestas. Inversión del flujo creativo.
- **Validación instantánea:** Cuando el PO escribe una historia, un agente la analiza inmediatamente: ¿Es testable? ¿Tiene criterios de aceptación claros? ¿Hay dependencias? ¿El valor está cuantificado? Feedback en segundos, no en la próxima planning meeting.

#### Responsabilidades irreductiblemente humanas

Lo que el PO hace y que ningún agente puede hacer:

- **Juicio de valor:** ¿Esta feature sirve a nuestros usuarios reales? ¿Alinea con nuestra visión? Los agentes optimizan; los humanos deciden QUÉ optimizar.
- **Empatía con el usuario:** Entender dolor, frustración, deseo. Los agentes procesan datos de uso; el PO entiende personas.
- **Decisión ética:** ¿Deberíamos construir esto aunque podamos? El PO es el gatekeeper ético del producto.
- **Aceptación final:** Cada historia completada pasa por aprobación humana del PO. Sin excepciones. Este es el núcleo del human-in-the-loop de HCAI.

### 2.2 Operador: El Ingeniero de Enjambre

El Scrum Master facilitaba dinámicas sociales: resolvía conflictos, mantenía moral, removía impedimentos. El Operador es una especie completamente diferente: es un **ingeniero de sistemas inteligentes** que configura, calibra y optimiza el enjambre.

#### Capacidades amplificadas

- **Context engineering:** Mantiene los archivos CONVENTIONS.md, ARCHITECTURE.md, STACK.md que alimentan a los agentes. Equivalente a mantener el "modelo mental compartido" de Kelly, pero externalizado y versionado.
- **Topología de enjambre:** Define qué agentes participan, con qué modelos, qué herramientas (AgentSkills) disponibles, qué permisos. Puede reconfigurar en minutos sin "forming-storming."
- **Model Router:** Configura routing de tareas al modelo óptimo por coste/capacidad. Optimiza la economía de tokens del enjambre.
- **Monitor de calidad:** Observa métricas del enjambre: tasa de alucinación, tasa de éxito de tool-calling, coste por historia, acceptance rate. Interviene cuando detecta degradación.

#### Responsabilidades irreductiblemente humanas

- **Aprobación de acciones destructivas:** Delete de datos, deploy a producción, comunicaciones externas: requieren aprobación explícita del Operador.
- **Cambios arquitectónicos:** Decisiones que afectan la estructura fundamental del sistema requieren juicio humano.
- **Actualizaciones de modelo:** Cambiar el modelo base de un agente requiere evals de regresión y aprobación del Operador.
- **Retrospectiva analítica:** Conduce el análisis periódico de rendimiento del enjambre con el PO.

#### Context hygiene: el Sentinel como mantenedor

El context engineering es trabajo cognitivo significativo. Si el Operador gasta 40% de su tiempo manteniendo context files, la atención como recurso soberano empieza a gritar. La solución: **el Sentinel mantiene context files y el Operador solo aprueba diffs.**

Modelo de context hygiene:

1. **Detección automática de drift:** El Sentinel compara el estado real del codebase (estructura de archivos, dependencias, patrones de código) con lo declarado en ARCHITECTURE.md y CONVENTIONS.md. Cuando detecta divergencia, genera un diff propuesto.
2. **Actualización propuesta como PR:** El diff al context file se presenta como PR con justificación. El Operador revisa y aprueba/ajusta.
3. **Versionado estricto:** Los context files están en git. Cada cambio tiene autor (Sentinel o Operador), timestamp, y justificación. Es auditable.
4. **Validación cruzada:** Al inicio de cada sesión de agente, un check rápido verifica que los context files son coherentes entre sí y con el codebase real. Incoherencia = alerta al Operador.

> ⚡ **EL SUPER-HUMANO DE HCAI**
>
> En Xanpan::Agents, un PO + un Operador + el enjambre producen lo que antes requería un equipo de 8-12 personas. No porque los humanos trabajen más, sino porque trabajan DIFERENTE: en el estrato donde su juicio es irreemplazable, amplificados por agentes que ejecutan el estrato mecánico a velocidad de máquina. Esto es human augmentation real, no marketing.

### 2.3 Roles Satélite: Más allá del software puro

El modelo PO + Operador asume un producto de software. Pero el software no existe en el vacío. Hay normativa, política interna, usuarios no-técnicos, dominios especializados. Xanpan::Agents necesita un escape hatch para dominios complejos.

#### El problema

En un hospital, hay normativa clínica. En una fintech, hay regulación bancaria. En gobierno, hay política interna y usuarios no-técnicos. El PO no puede ser experto simultáneamente en valor de negocio, dominio clínico, regulación financiera y experiencia de usuario. Y el Operador no puede ser simultáneamente ingeniero de enjambre y auditor de cumplimiento.

#### Roles satélite definidos

Los roles satélite **no** son miembros permanentes del equipo. Son **interfaces humanas que el enjambre consulta a demanda**, amplificadas por agentes especializados:

| Rol satélite | Cuándo se activa | Cómo interactúa con el enjambre | Ejemplo |
|---|---|---|---|
| **Domain Expert** | Historias que requieren conocimiento especializado | Un agente-analista prepara briefing del contexto técnico; el expert valida supuestos y restricciones de dominio | Médico validando lógica de dosificación |
| **Compliance Officer** | Historias clasificadas como regulatorias o con impacto legal | Agente-compliance pre-analiza contra marco regulatorio conocido; el officer valida y firma | Auditor revisando cumplimiento GDPR |
| **UX Researcher** | Historias que afectan experiencia de usuario | Agente genera prototipos o flujos; el researcher valida contra investigación de usuarios reales | Diseñador evaluando flujo de onboarding |
| **Security Analyst** | Historias clasificadas como críticas o con superficie de ataque | Agente-security ejecuta análisis estático/dinámico; el analyst revisa hallazgos y autoriza | Pentester revisando nueva API expuesta |
| **Stakeholder Rep** | Revisiones de Ciclo o decisiones estratégicas | Asiste a Retrospectiva Analítica como observador con voz; recibe reportes generados por agente-analyst | VP de producto en revisión de OKRs |

#### Principio de diseño: amplificación, no burocracia

Los roles satélite siguen el patrón HCAI de Supertools: el agente prepara, analiza y sintetiza; el humano especialista juzga, valida y decide. El agente hace el trabajo pesado de recopilación y análisis. El humano aporta los 5 minutos de juicio experto que ningún modelo puede reemplazar.

**Anti-patrón:** convertir roles satélite en gates burocráticos que bloquean el flujo. El principio es consulta a demanda, no aprobación en cadena. Si una historia no tiene clasificación regulatoria, el Compliance Officer nunca la ve. Si no tiene superficie de ataque, el Security Analyst nunca la ve.

#### Modo dual-hat (equipos pequeños)

En equipos pequeños o individuales, una persona puede ocupar múltiples roles. El caso extremo es el operador-PO individual (ver §18: Korvo-Korax). En este caso, el PCA (Protocol de Coherencia Atencional) o un equivalente de gobernanza personal compensa la falta de separación de concerns. El Sentinel cobra importancia adicional como "segundo par de ojos" que el humano dual-hat no tiene.

---

## 3. User Stories: El Contrato Humano-Agente

> *"A user story is a placeholder for a conversation. Each story has business benefit."*
> — Allan Kelly, Xanpan

La historia de usuario sobrevive como mecanismo central de captura de requisitos. Lo que cambia: la naturaleza de la conversación y la velocidad de resolución.

### 3.1 Anatomía de una historia en Xanpan::Agents

Cinco elementos: tres heredados de Kelly, dos nuevos para el mundo de agentes:

| Elemento | Origen | Responsable | Descripción |
|---|---|---|---|
| **Who/What/Why** | Kelly | PO | Formato clásico: "Como [usuario], quiero [funcionalidad], para [beneficio]" |
| **Criterios de aceptación** | Kelly | PO + Agente | Condiciones testables que definen "hecho." El agente sugiere; el PO aprueba. |
| **Valor de negocio (puntos)** | Kelly | PO | Estimación abstracta de valor asignada por PO. |
| **Señal de complejidad** | NUEVO | Operador/Auto | simple \| estándar \| complejo \| crítico. Determina tier de modelo via Model Router. |
| **Clasificación de riesgo** | NUEVO | Operador/Auto | lectura \| escritura \| destructiva. Determina si requiere aprobación humana pre-ejecución. |

### 3.2 La conversación humano-agente

En Scrum clásico, la conversación sobre una historia ocurre en la planning meeting, días después de ser escrita. En Xanpan::Agents, la conversación es **instantánea y continua:**

1. **PO escribe historia + criterios de aceptación.** Puede ser borrador imperfecto.
2. **Agente analiza y hace preguntas clarificadoras inmediatamente.** "¿El límite de 500ms incluye latencia de red? ¿El 'usuario nuevo' incluye usuarios anónimos?"
3. **PO refina en ciclos cortos.** La conversación de clarificación que en Scrum toma días, aquí toma minutos.
4. **Agente genera plan de implementación antes de escribir código.** PO u Operador aprueban el plan.
5. **Ejecución con feedback continuo.** El agente puede pedir clarificación mid-flight si encuentra ambigüedad.

### 3.3 Jerarquía: Épicas → Historias → Tareas

La jerarquía de Kelly se preserva pero las fronteras se comprimen:

- **Épicas:** Objetivos de negocio que mapean directamente a Key Results de OKR. Demasiado grandes para un ciclo de ejecución de agente. Escritas por PO.
- **Historias:** Unidades de valor entregable. Cada una con beneficio de negocio independiente y criterios de aceptación testables. Un agente puede consumir una historia en una sesión: minutos a horas, no días.
- **Tareas:** Auto-generadas por el agente al descomponer la historia. El humano NO necesita escribir tareas. El agente planifica su propia descomposición.

> ⚡ **CUELLO DE BOTELLA INVERTIDO**
>
> Kelly advierte que backlogs grandes son perjudiciales. En Xanpan::Agents esto se amplifica exponencialmente: los agentes pueden consumir el backlog más rápido de lo que el PO puede nutrirlo. El cuello de botella se invierte: ya no es la velocidad de desarrollo sino la velocidad de definición de valor por el humano. El backlog predictivo (agentes proponiendo historias) es la solución a esta inversión.

---

## 4. Modelo Temporal: Del Sprint al Flujo Continuo

> *"Regularly imposed external deadlines are more effective for delivering completed work."*
> — Allan Kelly, Xanpan (citando Buehler, Griffin, Peetz)

Kelly tiene razón: los humanos necesitan ritmo. Los agentes no, pero **los humanos que gobiernan el proceso SÍ.** La cadencia no desaparece; se transforma. Y se comprime brutalmente.

### 4.1 Tres escalas temporales simultáneas

El modelo temporal de Xanpan::Agents opera en tres frecuencias:

#### Pulso (reemplaza al Sprint): adaptativo

El Pulso **NO** es una iteración de desarrollo. Es una **iteración de gobernanza humana**. Durante el período entre Pulsos, los agentes ejecutan historias continuamente. El Pulso es el momento donde los humanos:

- Revisan entregas y aceptan/rechazan contra criterios de aceptación.
- Re-priorizan backlog basado en aprendizaje.
- Refinan historias pendientes en conversaciones humano-agente.
- Revisan métricas del enjambre (coste, calidad, rendimiento).
- Deciden si rotar, escalar o reducir agentes.

**Duración adaptativa:** El Pulso por defecto es 1 semana. Si las métricas del enjambre son estables y el acceptance rate es >90%, puede extenderse a 2 semanas. Si hay degradación o lanzamiento crítico, puede comprimirse a 2-3 días. El ritmo se adapta a la realidad, no al revés. La rigidez del sprint fijo muere definitivamente.

#### Ciclo (reemplaza al Trimestre): 4-6 semanas

Período operacional de OKRs. Kelly recomienda OKRs trimestrales; Xanpan::Agents comprime a 4-6 semanas porque la velocidad de ejecución permite iterar sobre objetivos más rápidamente. Cada Ciclo comienza con sesión de planificación estratégica donde PO y Operador:

- Revisan OKRs del Ciclo anterior (% KRs logrados, lecciones aprendidas).
- Definen 1-3 Objetivos para el próximo Ciclo con Key Results medibles y preferiblemente análogos (como Kelly recomienda).
- Derivan épicas necesarias para lograr cada KR.
- Descomponen épicas en historias con soporte de agente-planificador.

#### Horizonte (año): Continuo

Roadmap estratégico y OKRs anuales. Alineación con el modelo Continuous Digital de Kelly. El enjambre opera siempre; no hay "fin de proyecto."

### 4.2 Análogo > Binario en Key Results

Siguiendo a Kelly: *"Es más efectivo plantear key results como declaraciones análogas: alguna cantidad de funcionalidad está hecha."* Esto permite a los agentes entregar progreso parcial valioso en vez de perseguir objetivos todo-o-nada. Un KR análogo como "Reducir tiempo de respuesta de 2s a menos de 500ms" permite celebrar llegar a 800ms en camino a 500ms.

### 4.3 La muerte del deadline como fuente de estrés

Kelly argumenta que los deadlines crean urgencia productiva. Con agentes, los deadlines cambian de naturaleza: ya no son fechas de entrega que generan estrés en humanos. Son **horizontes de evaluación**: momentos predefinidos donde los humanos evalúan progreso contra KRs y deciden si pivotar. La emoción humana del "vamos a llegar tarde" se transforma en el análisis frío de "¿está la curva de progreso convergiendo al objetivo?"

---

## 5. El Tablero Neural

> *"Each Xanpan team must design its own board. Think of it like Jedi lightsabers: each Jedi must build their own."*
> — Allan Kelly, Xanpan

Kelly insiste: si no podemos ver, no podemos aprender. El tablero es el sistema nervioso del equipo. En Xanpan::Agents, el tablero estático de post-its evoluciona a un **dashboard neural en tiempo real** donde cada historia, cada agente, cada métrica respira en vivo.

### 5.1 Columnas del flujo

| Columna | Descripción | Velocidad típica |
|---|---|---|
| **Backlog** | Historias priorizadas por valor de negocio, alimentadas por PO y backlog predictivo | Continua |
| **Refinamiento** | Conversación humano-agente activa para clarificar criterios | Minutos |
| **Agent:Working** | Historia en ejecución activa por agentes. WIP controlado. | Minutos a horas |
| **Agent:Review** | Entregable completado, pasando eval automático (tests, lint, evals) | Segundos a minutos |
| **Human:Approval** | Pasó eval automático, espera aceptación del PO | Horas (Pulso) |
| **Done** | Aceptada y desplegada o lista para despliegue | Terminal |
| **Rejected** | Rechazada por PO o falló eval. Retorna a Refinamiento con feedback. | Retroceso |
| **Unplanned** | Trabajo emergente: bugs, urgencias. Kelly acepta que es inevitable y valioso. | Variable |

### 5.2 Tarjetas por color (adaptación Kelly)

- 🔵 **Azul:** Historias de negocio con valor. Escritas por PO.
- 🔴 **Rojo:** Bugs. Los agentes auto-detectan algunos via evals; otros reportados por usuarios.
- 🟡 **Amarillo:** Trabajo no planificado. Kelly acepta que es inevitable e incluso valioso.
- 🟢 **Verde:** Mejoras de proceso: refactoring, optimización de prompts, mejoras de evals.
- 🟠 **Naranja (NUEVO):** Calibración del enjambre: actualizaciones de modelo, re-indexación de embeddings, ajustes de context engineering. Trabajo que no existía en equipos humanos.
- 🟣 **Púrpura (NUEVO v2.0):** Tareas auto-propuestas por el enjambre. El enjambre auto-evolutivo genera tarjetas púrpura cuando detecta oportunidades de mejora. Requieren aprobación del Operador.

### 5.3 Límites WIP para agentes

Kelly limita el WIP humano: "default una tarea por persona." Los agentes pueden ejecutar en paralelo, pero el WIP sigue importando por dos razones: **Coste** (cada agente ejecutando consume tokens; más paralelismo = más coste instantáneo) y **Coherencia** (demasiados agentes modificando el mismo codebase simultáneamente generan conflictos de merge). El límite WIP es ahora una **restricción de coherencia, no de capacidad cognitiva**. El Operador configura límites WIP por zona del codebase, no por agente individual.

---

## 6. Economía de Tokens: De Story Points a Métricas Reales

> *"'Actuals' are nothing more than another estimate. A retrospective estimate."*
> — Allan Kelly, Xanpan

Kelly dedica capítulos enteros a demoler la ilusión de la estimación precisa en equipos humanos: planning fallacy, Ley de Hofstadter, inutilidad de los "actuals." Con agentes, el problema de la estimación se transforma completamente. Los agentes no sufren planning fallacy. No tienen ego que infle o desinfle estimaciones. Pero introducen una nueva variable: el coste de inferencia.

### 6.1 Tres métricas que reemplazan la velocidad

| Métrica | Definición | Análogo clásico |
|---|---|---|
| **Coste por Historia (CpH)** | Tokens consumidos por historia completada y aceptada | Velocidad (puntos/sprint) |
| **Tasa de Aceptación (TA)** | % de historias aceptadas por PO al primer intento | Calidad (defectos) |
| **Cycle Time** | Tiempo desde Backlog hasta Done para una historia | Lead time |

### 6.2 Priorización por valor, no por esfuerzo

Kelly recomienda priorizar por valor de negocio. En Xanpan::Agents esto se **radicaliza**: dado que el "esfuerzo" ya no es recurso humano escaso sino gasto económico predecible (tokens), la priorización se simplifica:

> **FÓRMULA DE PRIORIDAD**
>
> `Prioridad = Valor de Negocio / (Coste Estimado en Tokens × Multiplicador de Riesgo)`
>
> Donde el Multiplicador de Riesgo aumenta para historias clasificadas como "destructivas" o con alta probabilidad de alucinación. Esto es priorización pura por ROI: cuánto valor por token invertido.

### 6.3 Presupuesto de tokens por Ciclo

Cada Ciclo tiene un presupuesto de tokens aprobado. El Operador distribuye el presupuesto entre: historias de negocio (**60-70%**), BAU y bugs (**20-25%**), y calibración del enjambre (**10-15%**). Siguiendo el principio de Kelly: *"watching the numbers"* sin perseguirlos como targets (evitando la Ley de Goodhart).

### 6.4 La curva de coste decreciente

Los modelos se abaratan un ~40% cada 6 meses. GPT-4 costó $60/M tokens en 2023. GPT-4.1 cuesta $2/M tokens en 2025. Mismo rendimiento, 30x más barato. Esto significa que la capacidad del enjambre **crece exponencialmente a presupuesto constante**. Una metodología diseñada para esta curva debe ser agresiva en adopción hoy, sabiendo que el ROI se amplifica con el tiempo.

**Nota de prudencia (v2.1):** Esta curva es una hipótesis de trabajo basada en datos observados 2023-2026, no un axioma garantizado. Las scaling laws muestran indicios de rendimientos decrecientes en ciertos benchmarks. La metodología incluye un modo degradado explícito (ver §15.5) para el escenario donde la curva se aplana.

---

## 7. Calidad: El Escudo contra la Alucinación

> *"Unless a team is actively working to improve software quality, not only will Xanpan fail, but any attempts at Agile will also fail."*
> — Allan Kelly, Xanpan

Kelly es intransigente: la calidad no es opcional. TDD, ATDD, refactoring, CI, code reviews son obligatorios. En Xanpan::Agents, las prácticas técnicas se transforman y se amplifican.

### 7.1 Mapeo de prácticas técnicas

| Práctica Kelly | Transformación en Xanpan::Agents | Intensidad |
|---|---|---|
| **TDD** | Nativa: el agente genera tests y código simultáneamente. Eval pipeline verifica cobertura mínima. | ★★★ |
| **ATDD** | PO escribe ACs, agente genera tests de aceptación. Tests ejecutados pre-aprobación humana. | ★★★ |
| **Refactoring** | Agentes refactorizan continuamente como tareas verdes. Métricas de complejidad ciclomática monitoreadas. | ★★★ |
| **CI** | Cada historia genera PR con CI automático: lint + tests + evals. | ★★★ |
| **Code Review** | Eval automático + cross-review entre agentes. Reviewer-agent distinto de author-agent. | ★★★ |
| **Pair Programming** | COLAPSA. Reemplazado por cross-eval. Los agentes no necesitan socializar conocimiento. | N/A |
| **Coding Standards** | Context engineering: CONVENTIONS.md como ley. Linting automático pre-merge. | ★★★ |
| **Static Analysis** | Nativo en pipeline CI. Ruff, ESLint, type checking. | ★★★ |

### 7.2 Evals: La práctica técnica obligatoria de esta era

**Los Evals son a Xanpan::Agents lo que TDD es al Xanpan clásico:** la práctica técnica obligatoria sin la cual todo fracasa.

- **Eval de regresión:** Dataset curado de queries + respuestas esperadas por agente. Ejecutado en cada cambio de modelo o config.
- **Eval de alucinación:** Verificación de que el output del agente no contiene información fabricada.
- **Eval de tool-calling:** Verificación de que el agente selecciona herramientas correctas para cada tarea.
- **Eval de coste:** Verificación de que el consumo de tokens está dentro de límites presupuestarios.
- **Eval de seguridad:** Verificación de que el agente no expone datos sensibles, no escala privilegios, no realiza acciones fuera de su allowlist. Alineado con el pilar de seguridad de HCAI.

### 7.3 Definition of Done para agentes

Kelly define DoD como contrato de completitud. En Xanpan::Agents, el DoD se formaliza como pipeline que toda historia debe pasar:

1. Código generado con unit tests (cobertura > umbral configurado).
2. Tests de aceptación derivados de ACs pasan.
3. Lint y type checking pasan sin errores.
4. Eval de regresión pasa (no rompe funcionalidad existente).
5. Eval de seguridad pasa (no expone datos, no escala privilegios).
6. PR creado con descripción clara y contexto.
7. CI verde.
8. Aprobación humana del PO contra criterios de aceptación.

> 🔒 **GOBERNANZA HCAI: FIABILIDAD + SEGURIDAD + CONFIANZA**
>
> Shneiderman define tres pilares de gobernanza: fiabilidad (prácticas de ingeniería rigurosas), cultura de seguridad (gestión organizacional), certificación de confianza (auditoría externa). En Xanpan::Agents: Fiabilidad = evals + CI/CD. Cultura de seguridad = context engineering + principio de mínimo privilegio. Confianza = transparencia total via dashboard + audit trail de cada acción del agente.

---

## 8. OKRs: Gobernanza Estratégica del Enjambre

> *"Writing quarterly OKRs is fundamentally a strategy question: what are the strategic priorities for the next quarter?"*
> — Allan Kelly, OKRs in Agile

Los OKRs son el mecanismo que conecta la estrategia de negocio con la ejecución del enjambre. Kelly describe cómo los OKRs resuelven tres problemas: orientación, autonomía y organización.

### 8.1 OKR-first, no Backlog-first

Kelly presenta dos modelos: backlog-first (historias generan OKRs) y OKR-first (OKRs generan historias). Xanpan::Agents adopta categóricamente **OKR-first:**

1. **OKRs de Ciclo** definen Objetivos y Key Results.
2. **De cada KR** se derivan Épicas necesarias.
3. **De cada Épica** se derivan Historias.
4. **Historias** pueblan backlog.
5. **Agentes** consumen backlog en orden de prioridad por valor.

El flujo es **unidireccional y trazable**: Estrategia → OKR → KR → Épica → Historia → Criterios de Aceptación → Ejecución → Eval → Aprobación Humana.

### 8.2 Estructura OKR en Xanpan::Agents

| Componente | Descripción | Responsable |
|---|---|---|
| **Objetivo** | Cualitativo, inspiracional, alineado al Higher Purpose de Kelly. | PO |
| **Key Results (2-4)** | Cuantitativos, análogos (no binarios), medibles. | PO |
| **Épicas derivadas** | Trabajo necesario para lograr KRs. Descompuesto con soporte de agente-planificador. | PO + Agente |
| **Presupuesto de tokens** | Presupuesto de inferencia estimado para el Ciclo. | Operador |
| **Criterios de eval** | Cómo se medirá el éxito del KR al final del Ciclo. | PO + Operador |

### 8.3 BAU: Mantener las luces encendidas

Kelly dedica un capítulo entero al trabajo BAU (Business As Usual) y ofrece cuatro opciones. Xanpan::Agents adopta la **Opción 4 de Kelly: hacer BAU un Objetivo cero explícito**. Reservar porcentaje fijo del presupuesto de tokens del Ciclo (típicamente 20-30%) para trabajo BAU: bugs, soporte, deuda técnica, mantenimiento.

### 8.4 OKRs asistidos por agentes

En niveles de madurez 4-5 del HCAI-MM, los agentes no solo ejecutan hacia OKRs sino que **proponen OKRs**. Un agente-analista con acceso a métricas de producto, datos de uso, y OKRs históricos puede generar borradores de Objetivos y Key Results para el próximo Ciclo. El PO revisa, ajusta y aprueba. La inteligencia estratégica es híbrida: datos de máquina + juicio humano.

Esto es **inteligencia híbrida** en su forma más pura (concepto HCAI): ni la máquina sola ni el humano solo producen mejores OKRs que ambos juntos. La máquina ve patrones en datos que el humano no detecta. El humano aporta visión, valores y conocimiento del mercado que la máquina no tiene.

---

## 9. Arquitectura del Enjambre Auto-Evolutivo

Esta sección no tiene equivalente en Kelly porque los equipos humanos no necesitan ser "configurados." Los agentes SÍ. El Operador diseña la topología del enjambre.

### 9.1 Roles de agentes

| Rol | Función | Tier de modelo | Ejemplo |
|---|---|---|---|
| **Planner** | Descompone épicas en historias y historias en tareas | Tier 3 (Frontier) | Opus, GPT-4.5, Gemini Ultra |
| **Coder** | Implementa código desde historias con TDD | Tier 2-3 | Sonnet, GPT-4.1, Gemini Pro |
| **Reviewer** | Revisa PRs generados por Coders; cross-eval | Tier 2 | Sonnet, GPT-4.1 |
| **Tester** | Genera y ejecuta tests de aceptación e integración | Tier 2 | Sonnet, Gemini Pro |
| **Refactorer** | Mejora continua de código existente (tareas verdes) | Tier 2 | Sonnet, GPT-4.1 |
| **Analyst** | Genera métricas, resúmenes, reportes para PO | Tier 1-2 | Haiku, Flash, Mini |
| **Orchestrator** | Coordina flujo entre agentes; Model Router | Tier 1 | Haiku, Flash |
| **Sentinel** | Meta-agente que monitorea al enjambre (ver §9.4) | Tier 2-3 | Sonnet, Opus |

### 9.2 Conway Invertido

Kelly cita la Ley de Conway: la estructura del equipo determina la estructura del software. En Xanpan::Agents, **invertimos**: la estructura del software dicta la topología del enjambre. Cada área del codebase (frontend, backend, infra) puede tener agentes especializados con context engineering dedicado. Los límites WIP aplican por zona, no por agente. El Operador puede reconfigurar topología entre Ciclos sin coste de "forming-storming" (los agentes no tienen curva de Tuckman).

### 9.3 Model Router

Cada tarea se enruta al modelo óptimo por coste/capacidad:

| Tier | Modelos | Casos de uso | Coste relativo |
|---|---|---|---|
| **Tier 1 (Económico)** | Flash, Haiku, Mini | Clasificación, formateo, análisis simple, orquestación | $ |
| **Tier 2 (Balance)** | Sonnet, GPT-4.1, Gemini Pro | Tool-calling, generación de código estándar, reviews | $$ |
| **Tier 3 (Frontier)** | Opus, GPT-4.5, Gemini Ultra | Razonamiento complejo, planificación, decisiones arquitectónicas | $$$ |
| **Tier 4 (Reasoning)** | o3, modelos thinking | Problemas matemáticos, lógicos, evaluación crítica | $$$$ |

### 9.4 El enjambre auto-evolutivo

El enjambre no solo ejecuta: **aprende y se optimiza:**

- **Auto-optimización de prompts:** El Sentinel analiza patrones de rechazo y propone ajustes a system prompts de otros agentes. El Operador aprueba los cambios.
- **Auto-generación de evals:** Cuando una historia es rechazada, el Sentinel genera automáticamente un nuevo caso de eval para prevenir la recurrencia. El nuevo eval se agrega al pipeline tras aprobación del Operador.
- **Auto-reconfiguración de topología:** Si el Sentinel detecta que un área del codebase tiene cycle time consistentemente alto, propone agregar un agente especializado o cambiar de tier de modelo. El Operador decide.
- **Tarjetas púrpura:** El Sentinel genera tarjetas púrpura en el tablero con propuestas de mejora. Son visibles para PO y Operador pero no se ejecutan sin aprobación humana. HCAI en acción: automatización alta + control humano alto.

#### Quis custodiet ipsos custodes? El eval del Sentinel

El Sentinel es un agente. Puede alucinar. Puede tener bias en sus análisis de calidad. Si el Sentinel propone una reconfiguración basada en una evaluación errónea, el error se propaga sistémicamente. Solución: **separación de concerns estilo auditor externo.**

1. **Sentinel ≠ Reviewer:** El Sentinel nunca revisa las mismas historias que evalúa. Su input son métricas agregadas (tasas, tendencias, anomalías), no PRs individuales.
2. **Eval del evaluador:** Un subset de las propuestas del Sentinel se evalúa retroactivamente: ¿las propuestas aplicadas mejoraron realmente las métricas? Si la tasa de mejora efectiva del Sentinel cae por debajo de un umbral, alerta al Operador.
3. **Modelo diferente:** El Sentinel usa un modelo y provider diferente al enjambre que evalúa. Si el enjambre usa Claude, el Sentinel usa GPT (o viceversa). Diversidad de modelos como defensa contra bias compartido.
4. **Veto asimétrico:** El Sentinel puede proponer cualquier cosa pero no puede ejecutar nada. El humano tiene veto absoluto y sin justificación requerida. La asimetría es intencional: proponer es barato, ejecutar errores es caro.

> ⚡ **PRINCIPIO DE AUTO-EVOLUCIÓN GOBERNADA**
>
> El enjambre puede proponer cualquier cambio sobre sí mismo: prompts, evals, topología, modelos. Pero no puede ejecutar ningún cambio sin aprobación humana. Es el patrón HCAI de "high automation + high control" llevado al meta-nivel: el sistema se auto-mejora pero los humanos gobiernan la dirección de la mejora.

### 9.5 Equipos Ameba con agentes

Kelly adopta el modelo de "Equipos Ameba" de Inamori: equipos pequeños que crecen, se dividen y contraen orgánicamente. Con agentes, la elasticidad es **instantánea:**

- **¿Necesitas más capacidad para un deadline?** Escala el número de agentes-coder en minutos.
- **¿El trabajo se reduce?** Desescala sin coste emocional. No hay despidos, no hay pérdida de moral.
- **¿Área nueva de producto?** Spawn sub-enjambre con context engineering específico.
- **¿Merge de dos líneas de producto?** Fusiona context engineering. Los agentes no tienen territorios políticos.

---

## 10. Human-in-the-Loop: Los Cuatro Loops de Gobernanza HCAI

> *"The human-in/on-the-loop HCAI design paradigm encompasses the entire lifecycle of a human-AI system."*
> — Wei Xu, HCAI-MF

Xu no describe solo "poner un botón de aprobación." Describe un paradigma donde el loop humano **abarca el ciclo de vida completo** del sistema: requisitos, diseño, desarrollo, despliegue, uso, operaciones y gobernanza.

### 10.1 Loop 1: Human-in-the-Loop (Individuo-Agente)

#### Intervenciones obligatorias

- **Aceptación de historias:** PO acepta o rechaza cada historia completada contra criterios de aceptación. Sin auto-aprobación. Nunca.
- **Acciones destructivas:** Cualquier operación clasificada como "destructiva" requiere aprobación explícita del Operador.
- **Cambios arquitectónicos:** Decisiones que afectan estructura fundamental del sistema.
- **Actualizaciones de modelo:** Cambiar modelo base requiere regresión + aprobación.
- **Cambios auto-evolutivos:** Toda propuesta del Sentinel requiere aprobación del Operador.

#### Autonomía del enjambre (todo lo NO listado arriba)

- Descomposición de historias en tareas.
- Generación de código y tests.
- Ejecución de CI/CD hasta staging.
- Refactoring continuo (tareas verdes).
- Generación de PRs y documentación.
- Eval automático entre agentes (reviewer ≠ coder).
- Deploy a producción con feature flags (si evals robustos y rollback automático configurado).

### 10.2 Loop 2: Organization-in-the-Loop

Herrmann & Pfeiffer (2023) enfatizan que HCAI no puede ignorar el contexto organizacional. En Xanpan::Agents:

- **OKRs como alineación organizacional:** Los OKRs del enjambre derivan de la estrategia de la organización. No son autónomos.
- **Presupuesto de tokens aprobado por liderazgo:** El coste del enjambre es gasto operativo aprobado a nivel organizacional.
- **Cultura de calidad como norma:** La organización define estándares de calidad que se implementan via context engineering y evals.
- **Rediseño de trabajo:** La adopción de Xanpan::Agents requiere rediseñar roles, procesos y flujos de decisión. No es "agregar agentes al proceso existente." Ver §16 para el modelo de transición.

### 10.3 Loop 3: Ecosystem-in-the-Loop

El enjambre no opera en aislamiento. Interopera con otros sistemas:

- **MCP (Model Context Protocol) para interoperabilidad:** Los agentes se conectan con herramientas externas via MCP estándar.
- **Coordinación con otros sistemas IA:** Si la organización tiene múltiples enjambres o sistemas IA, deben coordinarse.
- **Ecosistema cognitivo distribuido:** Xu describe ecosistemas como "sistemas cognitivos distribuidos donde humanos y IA colectivamente perciben, razonan, aprenden y deciden." El enjambre es un nodo en este ecosistema.

### 10.4 Loop 4: Society-in-the-Loop

El nivel macrosocial de HCAI:

- **Cumplimiento regulatorio:** EU AI Act, NIST AI RMF, ISO/IEC 42001. El enjambre debe operar dentro de marcos regulatorios.
- **Impacto laboral:** Xanpan::Agents no evita la pregunta difícil: ¿qué pasa con los desarrolladores humanos? La respuesta HCAI: los humanos se elevan a roles de mayor valor (PO, Operador, arquitectos, estrategas) mientras los agentes absorben trabajo mecánico. Ver §16 para modelo de transición.
- **Transparencia y auditabilidad:** Cada decisión del agente tiene audit trail. Cada historia tiene trazabilidad completa. La organización puede demostrar responsabilidad.

> 🌍 **PRINCIPIO DE MÍNIMA INTERVENCIÓN MAXIMAL**
>
> El humano interviene SOLO donde: (a) hay valor de negocio que juzgar (PO), (b) hay riesgo de daño irreversible (Operador), (c) la calidad del enjambre se degrada más allá de umbrales configurados (alertas automáticas), o (d) hay implicaciones organizacionales, ecosistémicas o sociales que requieren juicio humano. Todo lo demás es autónomo. Esto no es negligencia; es diseño. Es HCAI.

---

## 11. Digital Continuo con Agentes: El Software Longevo

> *"Software is an asset for the business that owns it, but it cannot be a static asset. Software ages and degrades because the world around it changes."*
> — Allan Kelly, Continuous Digital

Kelly argumenta contra el pensamiento de "proyecto": el software no está "terminado", evoluciona continuamente. Con agentes IA, este argumento se fortalece **exponencialmente.**

### 11.1 Software como activo vivo acelerado

- **Inversión continua posible y barata:** Los agentes pueden mejorar, refactorizar y actualizar software continuamente a coste marginal. La excusa de "no hay presupuesto para mantenimiento" muere.
- **Eliminación de gaps entre "proyectos":** Kelly advierte que los gaps entre proyectos causan pérdida de conocimiento tácito. Con agentes, el context engineering preserva conocimiento explícitamente.
- **Deuda técnica como tarea continua:** En vez de acumular deuda hasta que un "proyecto de refactoring" la aborde, agentes-refactorer trabajan continuamente como tareas verdes.

### 11.2 El software longevo

Si los agentes pueden mantener, actualizar y evolucionar software continuamente a coste marginal, el concepto de "end of life" del software cambia fundamentalmente. Los agentes pueden migrar frameworks, actualizar dependencias, refactorizar arquitecturas completas—todo como flujo continuo de tareas verdes. El software se vuelve significativamente más **longevo** mientras haya valor de negocio que justifique su existencia.

El software no es literalmente inmortal. Muere no solo por pérdida de valor de negocio—muere por muerte de ecosistema:

- **APIs que se deprecan** sin reemplazo equivalente.
- **Estándares que cambian** de forma incompatible (IPv4 → IPv6, HTTP/1.1 → HTTP/3).
- **Regulaciones que invalidan arquitecturas enteras** (GDPR hizo morir sistemas completos cuya arquitectura no permitía "derecho al olvido").
- **Plataformas que desaparecen** (Flash, Windows Phone, APIs de Twitter pre-Musk).

Los agentes pueden migrar frameworks, sí, pero no pueden evitar la obsolescencia regulatoria o ecosistémica. Lo que pueden hacer es **detectar temprano** el drift ecosistémico (via Sentinel monitoreando changelogs de dependencias, anuncios de deprecación, cambios regulatorios) y **proponer migración proactiva** antes de que sea crisis.

### 11.3 Productos, no proyectos: amplificado

Kelly insiste: piensa en productos, no en proyectos. Con agentes:

- **No hay "fin de proyecto":** el enjambre opera siempre.
- **No hay "equipo de mantenimiento" separado:** el mismo enjambre que construye, mantiene.
- **No hay "hand-off":** no hay transferencia de conocimiento porque el conocimiento está en el context engineering, no en cerebros humanos que se van.
- **El presupuesto es continuo:** tokens/mes, no "presupuesto de proyecto."

---

## 12. Observabilidad y Retrospectiva Analítica

### 12.1 Dashboard del enjambre

El Operador monitorea un dashboard en tiempo real con cinco dimensiones:

| Dimensión | Métricas | Frecuencia |
|---|---|---|
| **Coste** | Tokens/Pulso, Coste/Historia, Coste/KR, % presupuesto consumido | Continua |
| **Calidad** | Tasa de Aceptación, Tasa de Alucinación, Cobertura de Tests, Scores de Eval | Por Pulso |
| **Velocidad** | Historias Done/Pulso, Cycle Time promedio, Throughput | Por Pulso |
| **Modelo** | Tasa de éxito por modelo, latencia promedio, frecuencia de fallback | Continua |
| **Enjambre** | Utilización de agentes, WIP por zona, profundidad de cola, tarjetas púrpura pendientes | Continua |

### 12.2 Retrospectiva Analítica

Al final de cada Ciclo (no cada Pulso), PO y Operador conducen la **Retrospectiva Analítica:**

1. **Revisión de OKRs:** ¿Qué KRs se lograron? ¿Cuáles no y por qué?
2. **Análisis de coste:** ¿Se respetó el presupuesto de tokens? ¿Dónde se concentró el gasto?
3. **Análisis de calidad:** ¿Qué patrones de rechazo se observaron? ¿Hay alucinaciones recurrentes?
4. **Decisiones de ajuste:** ¿Cambiar modelos? ¿Ajustar context engineering? ¿Reconfigurar topología?
5. **Actualización de evals:** Agregar nuevos casos de test basados en fallos observados.
6. **Revisión de tarjetas púrpura:** Evaluar propuestas auto-evolutivas del Sentinel pendientes.
7. **Eval del Sentinel:** ¿Las propuestas del Sentinel aplicadas en el Ciclo anterior mejoraron métricas? ¿La tasa de mejora efectiva es aceptable?

La retrospectiva analítica elimina la dimensión emocional de la retro clásica. No hay "¿qué salió mal?" con carga emocional. Hay datos, patrones y decisiones operacionales. La política de equipo desaparece como variable.

---

## 13. Seguridad y Gobernanza Multi-Nivel

### 13.1 Principio de mínimo privilegio por agente

- **Allowlist explícito:** Cada agente tiene allowlist explícito de herramientas (AgentSkills) que puede invocar.
- **Sin acceso directo a secretos de producción:** Secretos inyectados en runtime por pipeline CI/CD.
- **Separación de privilegios:** Agentes-coder no pueden desplegar a producción; solo el pipeline CI/CD puede, tras aprobación humana.

### 13.2 Aislamiento de ejecución

| Nivel | Tipo | Descripción |
|---|---|---|
| **Nivel 1 (Read)** | Container read-only | Para queries y análisis. Sin escritura. |
| **Nivel 2 (Write)** | Container efímero | Destruido post-ejecución. Para generación de código. |
| **Nivel 3 (OS Shell)** | MicroVM (Firecracker) | Timeout estricto, sin red externa. Para ejecución de tests. |

### 13.3 Agent-to-agent prompt injection

Una amenaza específica de los enjambres multi-agente que no existe en sistemas de agente único. Cuando los agentes pasan datos entre sí (el coder pasa código al reviewer, el analyst pasa datos al synthesizer), un agente comprometido por prompt injection vía input de usuario puede inyectar instrucciones maliciosas en su output, que otro agente consumirá como input legítimo.

Controles:

- **Sanitización en cada interfaz interna.** El output de cada agente se valida contra un schema tipado antes de alimentar al siguiente agente. No se pasa texto libre entre agentes si se puede evitar; se pasan estructuras tipadas.
- **Context isolation.** Cada agente tiene su propio contexto. El agente-reviewer no hereda el prompt del agente-coder; recibe solo el artefacto (código) y su propio prompt de revisión. Las instrucciones inyectadas en el output del coder quedan aisladas como datos, no como instrucciones.
- **Detección de anomalías inter-agente.** El agente-observer (Swarm::Ops §7.2) monitorea patrones de comunicación entre agentes. Un agente que de repente produce outputs con estructura inusual o con contenido que parece instruccional (meta-prompts) es señalizado.
- **Diversidad de modelos como mitigación.** Si el agente-coder es comprometido vía un blind spot del modelo que usa, el agente-reviewer (con modelo diferente, §9.3) tiene mayor probabilidad de detectar la anomalía.

### 13.4 Gobernanza multinivel HCAI

Shneiderman propone cuatro niveles de gobernanza. Mapeados a Xanpan::Agents:

| Nivel Shneiderman | Mecanismo en Xanpan::Agents |
|---|---|
| **Equipo: prácticas de ingeniería** | Evals, CI/CD, context engineering, DoD como pipeline automático |
| **Organización: cultura de seguridad** | OKRs, presupuesto aprobado, roles definidos (PO/Operador), retrospectiva analítica |
| **Industria: certificación de confianza** | Audit trail completo, trazabilidad historia→código→deploy, cumplimiento de estándares |
| **Gobierno: regulación** | Compliance con EU AI Act, NIST AI RMF, ISO/IEC 42001, reportes de incidentes |

---

## 14. Velocidad Exponencial: El Meta-Principio

Esta sección no existe en ninguna metodología ágil. Ninguna. Porque ninguna metodología fue diseñada para un mundo donde la capacidad del ejecutor se duplica cada seis meses. Xanpan::Agents sí.

### 14.1 La curva exponencial: hipótesis de trabajo

Los datos observados 2023-2026 son inequívocos:

- **Coste de inferencia:** Cae ~40% cada 6 meses. GPT-4 costó $60/M tokens en 2023. GPT-4.1 cuesta $2/M tokens en 2025. Mismo rendimiento, 30x más barato.
- **Capacidad de los modelos:** Cada generación maneja más contexto, comete menos errores, usa herramientas mejor. Ventana de 200K tokens hoy; 1M+ mañana.
- **Herramientas de agentes:** MCP, Claude Code, Codex CLI, agentes de navegación, agentes de investigación: cada trimestre aparecen capacidades nuevas.

**Nota crítica (v2.1):** Estos datos son observaciones empíricas, no leyes de la física. Las scaling laws muestran indicios de rendimientos decrecientes en ciertos benchmarks desde mid-2025. La exponencialidad es nuestra **hipótesis de trabajo**, no un axioma. La metodología está diseñada para *surfear* la exponencialidad si continúa, y para *degradar gracefully* si se aplana (ver §15.5).

Una metodología que no está diseñada para absorber mejoras exponenciales es una metodología que se vuelve obsoleta en meses. Pero una metodología que asume la exponencialidad como garantía es una metodología que colapsa ante la primera meseta.

### 14.2 Principios para velocidad exponencial

#### Principio 1: Diseña para el modelo de mañana, no el de hoy

La arquitectura del enjambre debe asumir que en 6 meses los modelos serán más capaces y más baratos. Esto significa: no optimices en exceso para las limitaciones actuales. Si hoy necesitas un workaround porque el modelo falla en X, pon un eval pero asume que el workaround será temporal.

#### Principio 2: Automatiza la automatización

No es suficiente automatizar el desarrollo. Hay que **automatizar la automatización misma**. El Sentinel es la primera capa de esto: un agente que optimiza a otros agentes. En niveles de madurez 5, la organización tiene meta-agentes que optimizan la metodología misma: ajustan duración de Pulsos, recalibran presupuestos de tokens, proponen reorganizaciones de topología—todo basado en datos.

#### Principio 3: Ship fast, eval faster, rollback instantáneo

El staging clásico era necesario porque el despliegue era costoso y el rollback difícil. Con feature flags, canary deploys y evals robustos, el flujo se comprime: generar → evaluar → desplegar → monitorear → rollback si falla. Todo automático. Todo en minutos. La red de seguridad no es un ambiente de staging; es un pipeline de evals + rollback automático.

#### Principio 4: El backlog es un flujo, no un repositorio

Deja de pensar en el backlog como una lista estática que se prioriza y se consume. Es un flujo continuo: entran historias del PO, entran propuestas del backlog predictivo, salen historias ejecutadas, salen historias descartadas. Es un río, no un lago. Optimiza el flujo, no el inventario.

#### Principio 5: Cada Ciclo debe ser más eficiente que el anterior

Si el Ciclo 3 no es más eficiente que el Ciclo 2, algo está mal. El enjambre auto-evolutivo, la mejora continua de evals, la optimización de context engineering y la caída de costes de inferencia deben producir una **curva de mejora compuesta**. Mídelo. Si la curva se aplana, diagnostica y corrige. La estasis es síntoma de enfermedad—o señal de que la hipótesis exponencial necesita revisión (ver §15.5).

> ⚡ **EL IMPERATIVO EXPONENCIAL**
>
> Estamos en una revolución global e histórica. Las organizaciones que adopten metodologías de desarrollo agente-céntricas en 2025-2026 tendrán una ventaja compuesta que se amplifica con el tiempo. Las que esperen a que "la tecnología madure" estarán adoptando en 2028 lo que sus competidores perfeccionaron en 2026. En exponenciales, llegar tarde no es llegar un poco después. Es llegar a un orden de magnitud de distancia.

---

## 15. Modos de Fallo y Circuit Breakers

El documento hasta aquí describe el happy path con detalle. Pero las metodologías serias no se miden por cómo funcionan cuando todo va bien, sino por **cómo fallan cuando algo sale mal**. Esta sección describe modos de fallo anticipados y sus circuit breakers.

### 15.1 Alucinación sistémica

**Modo de fallo:** El enjambre genera código que pasa todos los evals pero contiene errores semánticos sutiles. Los tests pasan porque los tests mismos fueron generados por un agente que compartió el mismo error de comprensión que el agente que generó el código. Un eval que evalúa contra su propio bias es un eval ciego.

**Circuit breakers:**

- **Diversidad de modelos obligatoria:** Coder y Reviewer deben usar modelos de providers diferentes. Si el Coder usa Claude, el Reviewer usa GPT o Gemini. Los modelos de un mismo provider comparten biases de entrenamiento; la diversidad reduce la probabilidad de bias compartido.
- **Golden dataset humano:** Un subset de evals tiene respuestas correctas escritas por humanos, no generadas por agentes. Estas "anclas humanas" detectan drift sistémico.
- **Auditoría de muestra por PO:** Además de aceptar/rechazar historias, el PO periódicamente (cada Pulso) inspecciona en profundidad 1-2 historias completadas, incluyendo el código generado, no solo el comportamiento funcional. Es costoso en atención humana pero es el último firewall.

### 15.2 Bias en los evals

**Modo de fallo:** Los evals mismos tienen bias. Por ejemplo, un eval de alucinación que solo chequea afirmaciones factuales pero no detecta omisiones críticas. O un eval de seguridad que cubre OWASP Top 10 pero no detecta vulnerabilidades novedosas que ningún eval cubre.

**Circuit breakers:**

- **Meta-eval periódico:** Cada Ciclo, el Operador (asistido por Sentinel) revisa el conjunto de evals: ¿cubren los modos de fallo observados? ¿Hay áreas sin cobertura? El meta-eval es humano-liderado porque la definición de "¿qué debería evaluar?" requiere juicio que los agentes no tienen.
- **Evals adversariales:** Periódicamente, un agente recibe la instrucción explícita de intentar romper el sistema: generar código que pase evals pero sea incorrecto, encontrar formas de escalar privilegios, producir output que engañe al Reviewer. Los resultados alimentan nuevos evals. Es red-teaming continuo.
- **Incidentes como evals:** Cada bug en producción, cada historia rechazada, cada anomalía detectada se convierte en un nuevo caso de eval. El corpus de evals es un organismo vivo que crece con cada fallo. Kelly: "Quality is free"—pero solo si aprendes de cada error.

### 15.3 Divergencia PO-Operador

**Modo de fallo:** El PO quiere velocidad de features. El Operador quiere estabilidad del enjambre. Sus incentivos divergen. El PO presiona por más historias; el Operador frena por degradación de métricas. Sin mecanismo de resolución, se genera un deadlock o uno anula al otro.

**Circuit breakers:**

- **OKRs como contrato compartido:** Los OKRs del Ciclo son definidos conjuntamente. Si el PO quiere velocidad, debe explicitarlo como KR medible. Si el Operador quiere estabilidad, debe explicitarlo como KR medible. Ambos firman los mismos OKRs.
- **Dashboard como fuente de verdad:** Las métricas no mienten. Si el acceptance rate cae al 60%, el PO no puede argumentar que "todo va bien." Si el coste por historia es 3x el presupuesto, el Operador no puede argumentar que "el enjambre funciona." Los datos resuelven disputas.
- **Escalación a liderazgo:** Si PO y Operador no resuelven, el conflicto escala al nivel Organization-in-the-Loop: el liderazgo decide prioridades basado en estrategia organizacional. Esto debería ser raro; si ocurre frecuentemente, la separación de roles puede necesitar rediseño.

### 15.4 Vulnerabilidad novel no cubierta por evals

**Modo de fallo:** Un agente-coder genera código que introduce una vulnerabilidad de seguridad completamente nueva—algo que ningún eval cubre porque es un patrón de ataque que no existía cuando los evals fueron diseñados. Pasa CI, pasa evals, pasa review, llega a producción.

**Circuit breakers:**

- **Principio de mínimo privilegio como backstop:** Incluso si el código tiene una vulnerabilidad, el agente que lo generó no tiene acceso a producción. El deploy pasa por pipeline CI/CD con permisos restringidos. La superficie de ataque se contiene por diseño.
- **Monitoreo de producción separado del enjambre:** La observabilidad de producción (APM, WAF, anomaly detection) es sistema independiente, no controlado por los mismos agentes que generaron el código. Si el código desplegado tiene comportamiento anómalo, la detección viene de fuera del enjambre.
- **Rotación de Security Analyst como rol satélite:** Periódicamente (cada Ciclo o ante cambios significativos de superficie de ataque), un humano especialista en seguridad revisa la arquitectura y los patrones de código desplegados. No revisa cada línea; revisa la postura de seguridad del sistema.

### 15.5 Meseta de capacidad (la exponencialidad se detiene)

**Modo de fallo:** Las scaling laws se aplanan. Los modelos dejan de mejorar significativamente entre generaciones. El coste de inferencia se estabiliza. La hipótesis exponencial del §14 deja de ser válida.

**Circuit breakers:**

- **Pulso vuelve a ritmo fijo:** Si la mejora entre Ciclos se aplana (<5% mejora en CpH durante 3 Ciclos consecutivos), el Pulso adaptativo vuelve a frecuencia fija semanal. La incertidumbre requiere más gobernanza, no menos.
- **Presupuesto de tokens como recurso escaso:** Se abandona la mentalidad de "presupuesto creciente a coste constante" y se adopta gestión de escasez: priorización más estricta, eliminación de tareas verdes no esenciales, reducción del presupuesto de calibración al mínimo necesario.
- **Roles humanos se expanden:** Si los agentes no mejoran, los humanos retoman tareas de mayor complejidad cognitiva. El modelo no es binario (humano vs. agente); es un espectro donde la frontera entre "lo que el agente puede" y "lo que el humano debe" se ajusta según las capacidades reales.
- **Inversión en evals y context engineering se intensifica:** Si los modelos no mejoran, la forma de sacar más rendimiento es optimizar cómo los usamos: mejores prompts, mejor contexto, mejores evals. La mejora se desplaza de la capacidad del modelo a la calidad de la ingeniería del enjambre.

### 15.6 Corrupción de context engineering

**Modo de fallo:** Los context files acumulan contradicciones, información obsoleta o instrucciones ambiguas. Los agentes reciben señales conflictivas y su rendimiento se degrada gradualmente sin un fallo discreto que dispare alertas.

**Circuit breakers:**

- **Sentinel como auditor de context (§2.2):** Verificación automática de coherencia entre context files y codebase real.
- **Context files en git con blame:** Cada línea tiene autor y fecha. El Operador puede trazar cuándo se introdujo una contradicción.
- **Metric correlation:** Si el acceptance rate cae sin cambio de modelo ni de tipo de historias, la primera hipótesis debe ser degradación de context. El dashboard correlaciona cambios en context files con cambios en métricas.

---

## 16. Modelo de Transición: Del Equipo Humano al Enjambre

Un CTO leyendo Xanpan::Agents preguntará: "¿cómo transiciono mi equipo de 15 devs a esto sin perder 6 meses de productividad?" Esta sección ofrece un modelo, no una receta. La transición es un problema abierto y cada organización tiene restricciones únicas. Pero hay patrones observados.

### 16.1 La transición NO es un big bang

No se reemplaza un equipo humano por un enjambre de la noche a la mañana. Se migra gradualmente, exactamente como Kelly recomienda adoptar Xanpan: *"pick'n'mix—toma lo que funcione, descarta lo que no."*

### 16.2 Fases de transición

#### Fase 0: Augmented Development (semanas 1-4)

Los desarrolladores humanos **continúan haciendo su trabajo normal** pero empiezan a usar agentes como herramientas:

- Cada dev usa un agente-coder como copiloto (Claude Code, Cursor, Copilot).
- Se instrumentan métricas básicas: ¿cuánto código genera el agente vs. el humano? ¿Qué tipo de tareas delegan naturalmente?
- Se identifica al futuro Operador: el dev más interesado en configurar y optimizar agentes.
- Se identifica al futuro PO (o se confirma al PO existente si ya hay uno).

**Objetivo:** Construir intuición sobre qué pueden y no pueden hacer los agentes *en tu codebase específico*.

#### Fase 1: Parallel Track (semanas 5-12)

Se crea un track paralelo donde un mini-enjambre trabaja en historias seleccionadas mientras el equipo humano continúa:

- El Operador (emergente) configura un enjambre mínimo: 1 Coder + 1 Reviewer + CI con evals básicos.
- Se seleccionan 3-5 historias de bajo riesgo y complejidad media para el enjambre.
- El equipo humano trabaja en el resto del backlog normalmente.
- Se comparan resultados: velocidad, calidad, coste. Sin presión por resultados; es un experimento.

**Objetivo:** Validar que el enjambre puede producir código de producción en tu stack.

#### Fase 2: Accelerated Adoption (semanas 13-24)

El enjambre absorbe progresivamente más tipos de historias:

- Evals se formalizan. Context engineering se establece (CONVENTIONS.md, ARCHITECTURE.md).
- El Operador se dedica full-time (o near full-time) al enjambre.
- Desarrolladores humanos se redistribuyen: algunos se convierten en Operadores de sus propios sub-enjambres, otros migran a roles de PO, arquitectos, o domain experts.
- El tablero se implementa. Métricas de coste y calidad se rastrean por Pulso.

**Objetivo:** Alcanzar Nivel 2-3 de madurez HCAI.

#### Fase 3: Swarm-First (semanas 25+)

El enjambre es el mecanismo primario de ejecución:

- Todas las historias pasan por el enjambre. Humanos intervienen en aceptación, arquitectura, dominio.
- Sentinel activado. Backlog predictivo en prueba. Tarjetas púrpura aparecen.
- Roles humanos estabilizados: PO, Operador, roles satélite según necesidad.
- Retrospectiva Analítica como práctica establecida.

**Objetivo:** Operación normal según Xanpan::Agents completo.

### 16.3 ¿Qué pasa con los desarrolladores humanos?

La pregunta difícil que esta metodología no puede esquivar. Respuesta honesta:

- **Algunos se convierten en Operadores:** Los devs con interés en infraestructura, DevOps y optimización son candidatos naturales.
- **Algunos se convierten en POs o domain experts:** Los devs con más conocimiento de negocio y usuarios migran hacia roles de definición de valor.
- **Algunos se convierten en arquitectos:** Los devs senior definen ARCHITECTURE.md, revisan cambios arquitectónicos, y mantienen la visión técnica de largo plazo.
- **Algunos se convierten en ingenieros de evals:** Diseñar, mantener y mejorar el corpus de evals es trabajo especializado que requiere conocimiento profundo del dominio y del stack.
- **Algunos necesitarán reubicarse:** Ser honesto sobre esto es parte del principio HCAI de Society-in-the-Loop. La organización tiene responsabilidad de facilitar la transición: reskilling, reubicación interna, tiempo y soporte.

### 16.4 Anti-patrones de transición

- **"Reemplazamos al equipo el lunes":** Big bang. Garantía de desastre. Sin context engineering, sin evals, sin comprensión de las limitaciones.
- **"Los agentes hacen todo, los devs supervisan":** Subestima la atención requerida. Los devs no están entrenados para supervisar agentes; es una habilidad diferente.
- **"Primero perfeccionamos los evals, después activamos el enjambre":** Parálisis por análisis. Los evals se perfeccionan con uso real, no en laboratorio. Ship, eval, iterate.
- **"Mantenemos el Scrum existente y le agregamos agentes":** Los agentes no son "devs más rápidos." Son una especie diferente. Intentar meterlos en ceremonias Scrum es como intentar meter un coche de Fórmula 1 en un estacionamiento de centro comercial.

---

## 17. Síntesis: La Metodología Completa

### 17.1 Xanpan::Agents en una oración

Un Product Owner humano define QUÉ construir via user stories y OKRs. Un Operador humano configura y supervisa un enjambre de agentes IA auto-evolutivo que construye el CÓMO. Roles satélite aportan expertise de dominio cuando se necesita. La calidad se garantiza via evals automáticos y aprobación humana. La gobernanza HCAI multi-nivel asegura que la velocidad exponencial sirva a valores humanos. El software evoluciona continuamente como activo longevo. La metodología incluye modos de fallo explícitos y circuit breakers para cuando las cosas van mal.

### 17.2 Tabla de correspondencia Kelly → Xanpan::Agents v2.1

| Concepto clásico | Transformación v2.1 | Fundamento |
|---|---|---|
| Sprint (2 semanas) | Pulso adaptativo (3d-2sem) | Velocidad de agentes comprime revisión |
| OKR trimestral | Ciclo (4-6 semanas) | Ejecución rápida permite iterar más |
| Planning Poker | ELIMINADO | Agentes no tienen sesgo de estimación |
| Velocidad (pts/sprint) | CpH + Tasa Aceptación + Cycle Time | Métricas económicas reales |
| Pair Programming | Cross-eval entre agentes | No necesitan socializar conocimiento |
| Retrospectiva | Retrospectiva Analítica | Datos operacionales, no emoción |
| Scrum Master | Operador | De facilitador social a ingeniero de enjambre |
| Equipo desarrollador | Enjambre auto-evolutivo + Sentinel | Agentes especializados + meta-agente auditor |
| Board estático | Tablero Neural + tarjetas púrpura | Dashboard tiempo real + auto-propuestas |
| TDD | TDD + Evals (incl. seguridad + adversarial) | Evals como TDD organizacional anti-alucinación |
| Trabajo no planificado | Preservado (amarillo + BAU OKR) | Kelly tiene razón: lo no planificado es valioso |
| Productos no proyectos | Reforzado: software longevo | Agentes mantienen software indefinidamente* |
| Gobernanza de proyecto | Gobernanza multi-nivel HCAI | 4 loops: humano, org, ecosistema, sociedad |
| Backlog estático | Backlog predictivo + flujo | Agentes proponen historias + PO cura |
| Deploy con staging | Ship fast, eval faster, rollback | Evals + feature flags reemplazan staging |
| (sin equivalente) | Roles satélite | Domain experts, compliance, security, UX |
| (sin equivalente) | Modos de fallo + circuit breakers | Resiliencia diseñada, no improvisada |
| (sin equivalente) | Modelo de transición | Migración gradual, no big bang |

*Longevo, no inmortal. Ver §11.2 para matices sobre obsolescencia ecosistémica y regulatoria.*

### 17.3 Los 12 Axiomas de Xanpan::Agents v2.1

1. **Humano define QUÉ y POR QUÉ. Agente resuelve CÓMO.** (Invariante fundamental.)
2. **Cada historia debe entregar valor de negocio.** (Invariante Kelly.)
3. **OKRs gobiernan la dirección. El backlog es derivado, no primario.**
4. **La calidad es gratis si inviertes en evals.** (Evolución del axioma Crosby/Kelly.)
5. **El coste de token es el nuevo recurso escaso. Gestiónalo como presupuesto.**
6. **Human-in-the-loop para valor y riesgo. Autonomía para todo lo demás.**
7. **El software es un activo vivo y longevo.** (Invariante Kelly/Continuous Digital, amplificado.)
8. **Visualiza todo. El tablero neural es el sistema nervioso.**
9. **Mide, no persigas.** (Principio Kelly contra Goodhart.)
10. **Alta automatización Y alto control humano. No hay trade-off.** (Principio HCAI de Shneiderman.)
11. **El enjambre se auto-evoluciona bajo gobernanza humana.** (Con Sentinel auditado y circuit breakers.)
12. **Diseña para la curva exponencial—pero incluye modo degradado.** (Hipótesis de trabajo, no axioma.)

---

## 18. Apéndice: Korvo–Korax como Proof of Concept

### 18.1 El sistema personal como laboratorio

Antes de que Xanpan::Agents fuera un documento, fue una práctica. El sistema Korvo–Korax es un prototipo de esta metodología a escala personal—un equipo de un humano con un enjambre de uno. No es una implementación perfecta; es un laboratorio donde las ideas se testean con fricción real.

### 18.2 Mapeo de conceptos

| Concepto Xanpan::Agents | Implementación Korvo–Korax |
|---|---|
| Product Owner | Korvo (definición de valor y dirección) |
| Operador | Korvo (dual-hat: configura y opera el sistema) |
| Enjambre | Korax + sub-agentes según tarea |
| OKRs | GTD + sistema de proyectos con revisiones semanales |
| Evals | Invariantes PCA (Protocol de Coherencia Atencional) |
| Sentinel | Heartbeats + mecanismo de detección de colapso |
| Tarjetas púrpura | Propuestas proactivas generadas en heartbeats |
| Context engineering | AGENTS.md + SOUL.md + MEMORY.md |
| Model Router | Fallback chain: sonnet → gpt-5.2 → kimi → glm5 |
| Tablero Neural | Estado del workspace + métricas de sesión |

### 18.3 La violación consciente: dual-hat PO/Operador

La implementación personal viola deliberadamente la separación de concerns que el §2 propone: Korvo es simultáneamente PO y Operador. Esta violación tiene consecuencias predecibles:

- **Sesgo de confirmación amplificado:** Quien define el valor es quien configura al ejecutor. No hay segundo par de ojos humano que cuestione ni la priorización ni la configuración.
- **Fatiga atencional compuesta:** Mantener context engineering + evaluar entregas + definir valor consume el mismo recurso escaso (atención humana) sin posibilidad de delegación.
- **El PCA como compensador:** El Protocol de Coherencia Atencional es el mecanismo que compensa esta falta de separación: un framework de gobernanza personal que detecta drift, mantiene coherencia, y dispara alertas cuando la atención se fragmenta.

### 18.4 Lecciones observadas

Lecciones del laboratorio Korvo–Korax que informaron el diseño de Xanpan::Agents:

1. **El context engineering es MÁS difícil de lo que parece.** Mantener AGENTS.md actualizado es trabajo cognitivo significativo. → Llevó a la propuesta de Sentinel como mantenedor de context (§2.2).
2. **Los heartbeats como proto-Sentinel funcionan.** La detección proactiva de problemas con propuestas de acción subordinadas a aprobación humana es el patrón más robusto encontrado. → Llevó al diseño del Sentinel y las tarjetas púrpura.
3. **La diversidad de modelos importa.** Usar un solo provider crea blind spots. El fallback chain no es solo redundancia; es diversidad cognitiva. → Llevó al principio de diversidad de modelos en §15.1.
4. **El backlog predictivo emerge naturalmente.** Cuando el agente tiene suficiente contexto, empieza a sugerir tareas antes de que el humano las piense. → Llevó al concepto de backlog predictivo.
5. **La curva exponencial se siente.** Lo que era imposible hace 6 meses ahora es rutina. Pero la sensación no es lineal: hay mesetas seguidas de saltos. → Llevó a tratar la exponencialidad como hipótesis con modo degradado (§14, §15.5).

### 18.5 Limitaciones como proof of concept

Korvo–Korax es un N=1. Las limitaciones como proof of concept son severas:

- **No escala a equipos.** Un sistema personal no demuestra que la metodología funcione con múltiples humanos.
- **No tiene separación de roles real.** El dual-hat hace imposible validar que PO/Operador/Sentinel funcionen como roles independientes.
- **No tiene métricas formales.** No hay CpH, TA, ni Cycle Time instrumentados. Las observaciones son cualitativas.
- **Survivor bias.** Reportamos lo que funciona; los fracasos se olvidan o se racionalizan.

La función de este apéndice no es probar que Xanpan::Agents funciona. Es documentar que las ideas centrales —context engineering, meta-agente supervisor, backlog predictivo, gobernanza humana de enjambre— **emergieron de la práctica real antes de ser formalizadas**. La teoría siguió a la experiencia, no al revés. Kelly aprobaría.
