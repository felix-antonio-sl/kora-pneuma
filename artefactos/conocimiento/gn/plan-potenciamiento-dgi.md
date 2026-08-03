---
urn: urn:gn:kb:plan-potenciamiento-dgi
nombre: plan-potenciamiento-dgi
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre plan potenciamiento dgi; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_plan_potenciamiento_dgi_koda.yml (sha256:b0d3a4415ef874d8752293744f3107ac42180a53ccd18b94d041e23d58d1eb96); URN KODA legado urn:gorenuble:gn:plan-potenciamiento-dgi:1.0.0; estado KODA original Published; cuerpo original completo preservado; migración KORA 2026-08-02. Conserva referencias KODA legacy a piezas de gestión no migradas en este lote."
autor: "felixsanhueza"
creado: 2026-01-29
lang: es
tags: [gn, gore-os, koda, plan, potenciamiento, dgi]
familia: bok
---
# KODA Artifact: Plan de Potenciamiento DGI
# Source: implementation_plan.md
# Transform: CM-KODA-TRANSFORM (4 fases)

_manifest:
  urn: "urn:gorenuble:gn:plan-potenciamiento-dgi:1.0.0"
  federation:
    visibility: private
    license: UNLICENSED
  resolution:
    canonical_url: "file://knowledge/domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-01-29"
    source_file: "implementation_plan.md"
    last_modified_at: "2026-01-29"
  dependencies:
    requires:
      - urn: "urn:gorenuble:kb:gestion:meyer-org-structure:1.0.0"
      - urn: "urn:gorenuble:kb:gestion:lean6:1.0.1"

ID: PLAN-POTENCIAMIENTO-DGI-KODA-01
Version: 1.0.0
Status: Published
Human-Creator: felixsanhueza
Human-Editor: felixsanhueza
Model-Collaborator: KODA-ARCHITECT
Creation-Date: 2026-01-29
Modification-Date: 2026-01-29
Source: "implementation_plan.md"
Ctx: "Plan de Potenciamiento del DGI: Integración Meyer + Lean Six Sigma + Navegación Social"

XRef_Required:
  - "urn:kora:kb:spec:1.0.0"
  - "urn:gorenuble:kb:gestion:meyer-org-structure:1.0.0"
  - "urn:gorenuble:kb:gestion:lean6:1.0.1"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN.

    LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
    END_LLM_INSTRUCTIONS

Scope:
  Includes:
    - Síntesis de perspectivas Meyer y Lean Six Sigma
    - Modelo de integración estructural y metodológico
    - Navegación social y gestión del cambio
    - Modelos cognitivos para AR Virtual
  Excludes:
    - Plantillas vacías para proyectos específicos

Metrics:
  Source_Chars: 24568
  Artifact_Chars: 18500
  CR: 1.33
  FS: "100%"

# ============================================================================
# SÍNTESIS DE PERSPECTIVAS
# ============================================================================

PerspectiveSynthesis:
  - ID: POT-SYN-01
    Title: "Perspectiva Meyer: Estructura como Ciencia"
    XRef: "urn:gorenuble:kb:gestion:meyer-org-structure:1.0.0"
    Principles:
      - ID: MEYER-P1
        Name: "Regla de Oro"
        Application: "Autoridad y responsabilidad deben coincidir. El DGI asesora pero NO decide por las divisiones."
      - ID: MEYER-P2
        Name: "Especialización + Trabajo en Equipo"
        Application: "Cada rol del DGI debe ser experto de clase mundial en su dominio, colaborando con pares especializados."
      - ID: MEYER-P3
        Name: "Dominios Precisos"
        Application: "Límites claros entre Control de Gestión, Procesos y TD sin superposiciones ni brechas."
      - ID: MEYER-P4
        Name: "Base para Subestructura"
        Application: "Subdividir por especialidad técnica (qué producen), no por cliente o proceso interno."
      - ID: MEYER-P5
        Name: "Evitar Conflictos de Interés"
        Application: "No mezclar funciones de auditoría con servicios; no mezclar estabilidad con innovación."
      - ID: MEYER-P6
        Name: "Agrupar por Sinergias Profesionales"
        Application: "Mantener especialistas similares juntos para intercambio profesional y economías de escala."
      - ID: MEYER-P7
        Name: "Negocio Dentro del Negocio"
        Application: "Cada rol del DGI es un 'emprendedor interno' que vende productos/servicios a clientes internos."

  - ID: POT-SYN-02
    Title: "Perspectiva Lean Six Sigma: Mejora Sistemática"
    XRef: "urn:gorenuble:kb:gestion:lean6:1.0.1"
    Concepts:
      - ID: LEAN-C1
        Name: "5S"
        Application: "Organización visual del conocimiento institucional y flujos de trabajo."
      - ID: LEAN-C2
        Name: "DMAIC"
        Application: "Ciclo sistemático para proyectos de mejora: Definir → Medir → Analizar → Mejorar → Controlar."
      - ID: LEAN-C3
        Name: "Eliminación de Desperdicios"
        Application: "Identificar y reducir actividades que no agregan valor en procesos del GORE."
      - ID: LEAN-C4
        Name: "Control Estadístico"
        Application: "Uso de datos para detectar desviaciones antes de que escalen."
      - ID: LEAN-C5
        Name: "Kaizen"
        Application: "Cultura de mejora continua pequeña y constante vs. grandes revoluciones."

# ============================================================================
# MODELO DE INTEGRACIÓN: ARQUITECTURA
# ============================================================================

IntegrationArchitecture:
  - ID: POT-ARQ-01
    Title: "Arquitectura de Building Blocks (Meyer)"
    Description: |-
      Organización del DGI según los principios de especialización y dominios precisos,
      donde cada rol opera como un 'negocio dentro del negocio'.
    BuildingBlocks:
      - Block: "Engineers (Base)"
        Roles: ["Especialista Procesos", "Especialista TD"]
        Products:
          - "Modelos BPMN, diseños de automatización, especificaciones técnicas"
          - "Configuraciones KB, agentes IA, arquitecturas de integración"
      - Block: "Service Providers (Asset-based)"
        Roles: ["Especialista Control"]
        Products:
          - "Dashboards, informes periódicos, alertas operativas"
      - Block: "Coordinators"
        Roles: ["Jefe DGI"]
        Products:
          - "Planificación estratégica, facilitación de consensos, gestión de prioridades"
      - Block: "Sales & Marketing (Internal)"
        Roles: ["Navegador Institucional"]
        Products:
          - "Mapeo stakeholders, estrategia de influencia, acompañamiento en transiciones"

  - ID: POT-ARQ-02
    Title: "Catálogo de Productos DGI"
    Catalog:
      EngineersProcesos:
        - "Modelo BPMN proceso AS-IS"
        - "Diseño proceso TO-BE"
        - "Especificación de automatización"
        - "Análisis de causa raíz"
      EngineersTD:
        - "Artefacto conocimiento estructurado"
        - "Agente IA configurado"
        - "Integración entre sistemas"
        - "Capacitación técnica"
      ServiceProvidersControl:
        - "Dashboard ejecutivo (diario)"
        - "Informe estado situacional (semanal)"
        - "Alerta de desviación (continuo)"
        - "Métrica calculada y verificada"
      CoordinatorsJefatura:
        - "Plan de trabajo consensuado"
        - "Priorización de iniciativas"
        - "Resolución de conflictos"
        - "Comunicación con AR"

  - ID: POT-ARQ-03
    Title: "Relaciones Cliente-Proveedor"
    Paradigm: "Business Within a Business"
    InternalClients:
      - "Administración Regional: estrategia, prioridades"
      - "Divisiones: mejoras operativas, cumplimiento TDE"
      - "Comité TD: secretaría técnica"
    InteractionModel:
      - "Catálogo de servicios publicado"
      - "Solicitudes canalizadas formalmente"
      - "SLAs definidos por tipo de producto"
      - "Feedback estructurado post-entrega"
    KeyPrinciple: |-
      El DGI PROPONE y FACILITA; las divisiones DECIDEN y EJECUTAN.
      Autoridad para decidir = Responsabilidad por resultados.

# ============================================================================
# MODELO DE INTEGRACIÓN: METODOLOGÍA DMAIC
# ============================================================================

DMAICFramework:
  - ID: POT-DMAIC-01
    Title: "Marco Operativo DMAIC para DGI"
    Description: "Cada proyecto de mejora del DGI sigue el ciclo DMAIC"
    Phases:
      Define:
        - "Identificar problema/oportunidad"
        - "Establecer alcance y objetivos SMART"
        - "Definir stakeholders y sponsor"
        - "Documentar caso de negocio"
      Measure:
        - "Establecer línea base con métricas actuales"
        - "Recopilar datos del proceso AS-IS"
        - "Validar sistema de medición"
        - "Crear Value Stream Map si aplica"
      Analyze:
        - "Análisis de causa raíz (5 Porqués, Ishikawa)"
        - "Identificar cuellos de botella"
        - "Cuantificar oportunidades de mejora"
        - "Priorizar causas según impacto"
      Improve:
        - "Diseñar solución TO-BE"
        - "Prototipar y pilotear"
        - "Implementar cambios"
        - "Capacitar usuarios"
      Control:
        - "Establecer controles estadísticos"
        - "Documentar nuevo estándar"
        - "Crear alertas automáticas"
        - "Transferir a operación normal"

  - ID: POT-DMAIC-02
    Title: "Sistema 5S para Gestión del Conocimiento"
    Application: "Aplicar 5S japonés al ecosistema de conocimiento institucional"
    S5Mapping:
      - S: "Seiri (Clasificar)"
        Application: "Auditar artefactos, deprecar obsoletos, categorizar por utilidad"
      - S: "Seiton (Ordenar)"
        Application: "URNs consistentes, catálogo maestro, taxonomía clara"
      - S: "Seiso (Limpiar)"
        Application: "Revisión periódica de vigencia, corrección de errores"
      - S: "Seiketsu (Estandarizar)"
        Application: "Plantillas KODA, procesos de curación, naming conventions"
      - S: "Shitsuke (Disciplina)"
        Application: "Cultura de actualización, governance de KB, capacitación continua"

  - ID: POT-DMAIC-03
    Title: "Proyecto Piloto DMAIC Sugerido"
    Candidate: "Flujo de Visación de Actos Administrativos"
    Phases:
      Define:
        Output: "Charter del proyecto con objetivo de reducir tiempo de visación en 30%"
      Measure:
        Output: "VSM actual, tiempos de ciclo por etapa, volumen mensual"
      Analyze:
        Output: "Identificación de esperas, reprocesos, cuellos de botella"
      Improve:
        Output: "Automatización de notificaciones, checklist digital, flujo en paralelo"
      Control:
        Output: "Dashboard de seguimiento, alertas de SLA, revisión mensual"

  - ID: POT-DMAIC-04
    Title: "Tablero Kanban para Gestión de Iniciativas"
    Columns:
      - "BACKLOG"
      - "EN DISEÑO (DMAIC D-M-A)"
      - "EN IMPLEMENTACIÓN (DMAIC I)"
      - "EN VERIFICACIÓN (DMAIC C)"
      - "COMPLETADO"
    WIPLimits:
      Diseño: 2
      Implementación: 3
      Verificación: 2

# ============================================================================
# NAVEGACIÓN SOCIAL Y GESTIÓN DEL CAMBIO
# ============================================================================

SocialNavigation:
  - ID: POT-SOC-01
    Title: "El Rol del Navegador Institucional"
    BuildingBlock: "Sales & Marketing (Internal)"
    AlternateName: "Gestor de Relaciones y Cambio"
    Definition: |-
      Profesional que cultiva relaciones estratégicas con stakeholders clave,
      facilita la adopción de cambios, y "vende" internamente el valor del DGI
      sin imponer ni auditar.
    GuidingPrinciple: |-
      "No vendemos productos; ayudamos a las divisiones a descubrir cómo
      nuestros servicios pueden resolver sus dolores operativos."
    Products:
      - "Mapeo de stakeholders actualizado"
      - "Diagnóstico de clima organizacional por división"
      - "Estrategia de influencia por iniciativa"
      - "Acompañamiento en transiciones"
      - "Comunicación de éxitos y valor generado"
      - "Feedback estructurado desde divisiones"

  - ID: POT-SOC-02
    Title: "Mapa de Stakeholders GORE"
    Levels:
      Estrategico:
        - Actor: "Gobernador Regional"
          Power: Alto
          DGIInterest: "Variable (depende de agenda política)"
          Strategy: "Demostrar impacto en ERD y ciudadanía"
        - Actor: "Administrador/a Regional"
          Power: Alto
          DGIInterest: "Alto (sponsor natural)"
          Strategy: "Mantener informado, visibilizar quick wins"
      Tactico:
        - Actor: "Jefes de División"
          Power: "Medio-Alto"
          DGIInterest: "Variable (algunos resistentes)"
          Strategy: "Identificar campeones, resolver dolores primero, no amenazar autonomía"
        - Actor: "Comité de Transformación Digital"
          Power: Medio
          DGIInterest: Alto
          Strategy: "Proveer secretaría técnica impecable"
      Operativo:
        - Actor: "Profesionales de divisiones"
          Power: "Bajo individual, Alto colectivo"
          DGIInterest: Variable
          Strategy: "Capacitación como servicio, celebrar adopciones, crear red de embajadores"

  - ID: POT-SOC-03
    Title: "Modelo ADKAR para Gestión del Cambio"
    Phases:
      - Phase: "Awareness"
        Question: "¿Por qué cambiar?"
        Action: "Comunicar el problema claramente, usar datos"
      - Phase: "Desire"
        Question: "¿Qué gano yo?"
        Action: "Mostrar beneficios concretos para cada stakeholder"
      - Phase: "Knowledge"
        Question: "¿Cómo lo hago?"
        Action: "Capacitar, proveer materiales, acompañar"
      - Phase: "Ability"
        Question: "¿Puedo hacerlo?"
        Action: "Pilotear, ajustar, dar tiempo de práctica"
      - Phase: "Reinforcement"
        Question: "¿Seguirá funcionando?"
        Action: "Celebrar éxitos, medir, reconocer"

  - ID: POT-SOC-04
    Title: "Tácticas de Influencia Ética"
    Note: "El Navegador Institucional utiliza influencia, NO manipulación"
    Tactics:
      - Name: "Reciprocidad"
        Description: "Dar antes de pedir"
        Example: "Resolver un dolor pequeño de una división antes de proponer proyecto mayor"
      - Name: "Prueba Social"
        Description: "Mostrar que otros ya adoptaron"
        Example: "La División X ya usa el dashboard y redujo 30% sus consultas"
      - Name: "Autoridad"
        Description: "Citar fuentes creíbles"
        Example: "Según la normativa TDE, esto debe implementarse para 2026"
      - Name: "Escasez"
        Description: "Crear urgencia legítima"
        Example: "Si no priorizamos esto ahora, no cumpliremos el plazo del PMG"
      - Name: "Consistencia"
        Description: "Anclar a compromisos previos"
        Example: "En la última reunión de Comité, se acordó avanzar en esta línea"
      - Name: "Simpatía"
        Description: "Construir relación genuina"
        Example: "Reuniones periódicas informales, conocer las personas"

  - ID: POT-SOC-05
    Title: "Detección y Manejo de Resistencias"
    Types:
      - Type: "Racional"
        Symptoms: "Objeciones técnicas, preguntas sobre viabilidad"
        Response: "Escuchar, incorporar feedback, ajustar propuesta"
      - Type: "Emocional"
        Symptoms: "Frustración, comentarios sobre 'otra moda más'"
        Response: "Empatizar, reconocer fatiga de cambios, ir gradual"
      - Type: "Política"
        Symptoms: "Sabotaje pasivo, demoras, 'no es mi prioridad'"
        Response: "Identificar intereses, buscar win-win, escalar si es necesario"
    Protocol:
      - "Paso 1: Escuchar genuinamente la objeción"
      - "Paso 2: Validar la preocupación legítima"
      - "Paso 3: Explorar intereses subyacentes"
      - "Paso 4: Buscar alternativa que satisfaga ambas partes"
      - "Paso 5: Documentar y ajustar enfoque"
      - "Paso 6: Si persiste: escalar a AR con propuesta de solución"

  - ID: POT-SOC-06
    Title: "Métricas de Éxito Social"
    Metrics:
      - Indicator: "NPS interno del DGI"
        Target: "> 50"
        Measurement: "Encuesta trimestral a divisiones"
      - Indicator: "Tasa de adopción voluntaria"
        Target: "> 70%"
        Measurement: "% de divisiones que solicitan servicios"
      - Indicator: "Tiempo de respuesta a solicitudes"
        Target: "< 48h"
        Measurement: "Registro en sistema"
      - Indicator: "Proyectos completados sin escalamiento"
        Target: "> 80%"
        Measurement: "Conteo de escalamientos a AR"
      - Indicator: "Red de embajadores"
        Target: "1 por división"
        Measurement: "Conteo de personas identificadas"

# ============================================================================
# MODELOS COGNITIVOS PARA AR VIRTUAL
# ============================================================================

CognitiveModels:
  - ID: POT-CM-01
    Title: "CM-LEAN-THINKING"
    Purpose: "Evaluar situaciones desde la perspectiva de mejora continua"
    Dimensions:
      - "Identificar desperdicios (7+1 mudas): sobreproducción, esperas, transporte, sobreproceso, inventario, movimiento, defectos, talento subutilizado"
      - "Aplicar ciclo PDCA: Plan-Do-Check-Act"
      - "Priorizar por impacto/esfuerzo"
      - "Buscar causa raíz antes de solucionar"
      - "Preferir mejoras pequeñas y constantes"

  - ID: POT-CM-02
    Title: "CM-STRUCTURE-PRINCIPLES"
    Purpose: "Evaluar propuestas organizacionales según ciencia de Meyer"
    Dimensions:
      - "Verificar coincidencia autoridad-responsabilidad"
      - "Confirmar dominios precisos sin superposición"
      - "Evaluar especialización vs. generalización"
      - "Detectar conflictos de interés potenciales"
      - "Validar agrupación por sinergias profesionales"
      - "Aplicar paradigma 'negocio dentro del negocio'"

  - ID: POT-CM-03
    Title: "CM-SOCIAL-NAVIGATION"
    Purpose: "Evaluar dimensión social de cambios organizacionales"
    Dimensions:
      - "Mapear stakeholders y sus intereses"
      - "Aplicar ADKAR: ¿Tiene awareness, desire, knowledge, ability, reinforcement?"
      - "Seleccionar táctica de influencia apropiada"
      - "Detectar tipo de resistencia (racional, emocional, política)"
      - "Planificar comunicación y acompañamiento"

  - ID: POT-CM-04
    Title: "CM-DMAIC-EVALUATOR"
    Purpose: "Evaluar proyectos de mejora según metodología DMAIC"
    Dimensions:
      - "DEFINE: ¿Problema claro? ¿Alcance definido? ¿Sponsor identificado?"
      - "MEASURE: ¿Línea base establecida? ¿Datos confiables?"
      - "ANALYZE: ¿Causa raíz identificada? ¿Priorización por impacto?"
      - "IMPROVE: ¿Solución diseñada? ¿Pilotaje realizado?"
      - "CONTROL: ¿Controles establecidos? ¿Transferencia a operación?"
