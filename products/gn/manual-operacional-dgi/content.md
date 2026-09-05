---
urn: urn:gn:kb:manual-operacional-dgi
nombre: manual-operacional-dgi
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre manual operacional dgi; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_manual_operacional_dgi_koda.yml (sha256:1d8b7a713a4d026871f82ad691676ca476a1d5da38d06384cbea3d75c2cac494); URN KODA legado urn:gorenuble:gn:manual-operacional-dgi:1.0.0; estado KODA original Published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "felixsanhueza"
creado: 2026-01-29
lang: es
tags: [gn, gore-os, koda, manual, operacional, dgi]
familia: bok
---
# KODA Artifact: Manual Operacional DGI
# Source: manual_operacional_dgi.md
# Transform: CM-KODA-TRANSFORM (4 fases)

_manifest:
  urn: "urn:gorenuble:gn:manual-operacional-dgi:1.0.0"
  federation:
    visibility: private
    license: UNLICENSED
  resolution:
    canonical_url: "file://knowledge/domains/gn/dgi/kb_gn_manual_operacional_dgi_koda.yml"
  provenance:
    created_by: "felixsanhueza"
    created_at: "2026-01-29"
    source_file: "manual_operacional_dgi.md"
    last_modified_at: "2026-01-29"

ID: MANUAL-OPERACIONAL-DGI-KODA-01
Version: 1.0.0
Status: Published
Human-Creator: felixsanhueza
Human-Editor: felixsanhueza
Model-Collaborator: KODA-ARCHITECT
Creation-Date: 2026-01-29
Modification-Date: 2026-01-29
Source: "manual_operacional_dgi.md"
Ctx: "Manual Operacional del Departamento de Gestión Institucional GORE Ñuble"

XRef_Required: "urn:kora:kb:spec:1.0.0"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

    LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
    END_LLM_INSTRUCTIONS

Scope:
  Includes:
    - Marco institucional y normativo del DGI
    - Estructura organizacional y roles
    - Procesos operativos de las 4 áreas
    - Protocolos de coordinación institucional
  Excludes:
    - Plantillas vacías
    - Anexos de formularios

Metrics:
  Source_Chars: 42255
  Artifact_Chars: 28000
  CR: 1.51
  FS: "100%"

# ============================================================================
# TÍTULO I: DISPOSICIONES GENERALES
# ============================================================================

GeneralProvisions:
  - ID: DGI-GEN-01
    Title: "Objeto del Manual"
    Text: |-
      Establece el marco operativo del DGI del GORE Ñuble, definiendo estructura, funciones, procesos y mecanismos de coordinación institucional.

  - ID: DGI-GEN-02
    Title: "Alcance"
    Text: |-
      Aplicable a todo el personal del DGI y a las interacciones con divisiones, unidades y actores externos relacionados con sus funciones.

  - ID: DGI-GEN-03
    Title: "Definiciones Operacionales"
    Definitions:
      - Term: DGI
        Def: "Departamento de Gestión Institucional"
      - Term: AR
        Def: "Administración Regional"
      - Term: TD
        Def: "Transformación Digital"
      - Term: TDE
        Def: "Transformación Digital del Estado (Ley 21.180)"
      - Term: KB
        Def: "Knowledge Base / Base de Conocimiento"
      - Term: BPMN
        Def: "Business Process Model and Notation"
      - Term: KPI
        Def: "Key Performance Indicator"
      - Term: GORE
        Def: "Gobierno Regional"
      - Term: ERD
        Def: "Estrategia Regional de Desarrollo"

  - ID: DGI-GEN-04
    Title: "Marco Normativo"
    Sources:
      - Ley 19.175: "Orgánica Constitucional sobre Gobierno y Administración Regional"
      - Ley 21.180: "Transformación Digital del Estado"
      - DS 14/2014: "Modelo de Gestión de Procesos"
      - Resolución 22/2023: "Normas Técnicas de Interoperabilidad"
      - PMG: "Programa de Mejoramiento de la Gestión"

  - ID: DGI-GEN-05
    Title: "Principios Rectores"
    Principles:
      - ID: PR-01
        Name: "Orientación al servicio"
        Desc: "Foco en necesidades de usuarios internos y finales"
      - ID: PR-02
        Name: "Basado en datos"
        Desc: "Decisiones sustentadas en información verificable"
      - ID: PR-03
        Name: "Mejora continua"
        Desc: "Optimización sistemática de procesos"
      - ID: PR-04
        Name: "Colaboración"
        Desc: "Trabajo conjunto con todas las divisiones"
      - ID: PR-05
        Name: "Transparencia"
        Desc: "Información accesible y trazable"
      - ID: PR-06
        Name: "Innovación"
        Desc: "Adopción de mejores prácticas y tecnologías"

# ============================================================================
# TÍTULO II: ESTRUCTURA ORGANIZACIONAL
# ============================================================================

OrganizationalStructure:
  - ID: DGI-ORG-01
    Title: "Misión DGI"
    Text: |-
      Facilitar la gestión efectiva del GORE Ñuble mediante control de gestión,
      modernización de procesos, transformación digital y gestión del conocimiento,
      apoyando la toma de decisiones de la Administración Regional y la mejora
      continua de los servicios a la ciudadanía.

  - ID: DGI-ORG-02
    Title: "Visión DGI"
    Text: |-
      Ser reconocido como referente de gestión institucional en los Gobiernos
      Regionales de Chile, destacando por la calidad de su asesoría, innovación
      metodológica y uso efectivo de tecnologías para la gestión pública.

  - ID: DGI-ORG-03
    Title: "Áreas Funcionales"
    Domains:
      - ID: DOM-CG
        Name: "Control de Gestión"
        Description: "Monitoreo de indicadores, dashboards, alertas, informes ejecutivos"
      - ID: DOM-MP
        Name: "Modernización de Procesos"
        Description: "Levantamiento BPMN, análisis de mejora, diseño de automatizaciones"
      - ID: DOM-TD
        Name: "Transformación Digital"
        Description: "Cumplimiento TDE, Comité TD, administración funcional de sistemas"
      - ID: DOM-KC
        Name: "Gestión del Conocimiento"
        Description: "Curación KB, administración agentes IA, capacitación y gestión del cambio"

  - ID: DGI-ORG-04
    Title: "Perfiles de Cargo"
    Roles:
      JefeDGI:
        Name: "Jefe(a) Departamento de Gestión Institucional"
        Dependencia: "Administración Regional"
        Functions:
          - "Dirigir y coordinar el equipo DGI"
          - "Asesorar a AR en materias de gestión institucional"
          - "Representar al DGI en instancias colegiadas"
          - "Gestionar recursos del departamento"
          - "Reportar estado de iniciativas a AR"

      EspecialistaProcesos:
        Name: "Especialista en Modernización de Procesos"
        Dependencia: "Jefe DGI"
        Functions:
          - "Levantar y modelar procesos BPMN"
          - "Identificar oportunidades de mejora"
          - "Diseñar automatizaciones"
          - "Acompañar implementación de cambios"
          - "Documentar procedimientos optimizados"

      EspecialistaTD:
        Name: "Especialista en Transformación Digital"
        Dependencia: "Jefe DGI"
        Functions:
          - "Monitorear cumplimiento TDE"
          - "Gestionar secretaría técnica Comité TD"
          - "Curar y mantener base de conocimiento"
          - "Administrar agentes IA institucionales"
          - "Facilitar interoperabilidad de sistemas"

      EspecialistaControl:
        Name: "Especialista en Control de Gestión"
        Dependencia: "Jefe DGI"
        Functions:
          - "Definir y monitorear indicadores"
          - "Elaborar y mantener dashboards"
          - "Detectar y analizar desviaciones"
          - "Generar informes ejecutivos"
          - "Proponer acciones correctivas"

  - ID: DGI-ORG-05
    Title: "Matriz RACI"
    RACI:
      - Activity: "Diseñar indicadores"
        Jefe: C
        Procesos: I
        TD: I
        Control: R
        Division: C
        AR: A
      - Activity: "Levantar procesos"
        Jefe: C
        Procesos: R
        TD: I
        Control: I
        Division: C
        AR: I
      - Activity: "Gestionar KB"
        Jefe: C
        Procesos: I
        TD: R
        Control: I
        Division: I
        AR: I
      - Activity: "Administrar dashboards"
        Jefe: C
        Procesos: I
        TD: I
        Control: R
        Division: I
        AR: I
      - Activity: "Reportar a AR"
        Jefe: R
        Procesos: C
        TD: C
        Control: C
        Division: I
        AR: A
      - Activity: "Coordinar con divisiones"
        Jefe: R
        Procesos: C
        TD: C
        Control: C
        Division: C
        AR: A
    Legend: "R=Responsable, A=Aprueba, C=Consultado, I=Informado"

# ============================================================================
# TÍTULO III: CONTROL DE GESTIÓN
# ============================================================================

ControlGestion:
  - ID: DGI-CG-01
    Title: "Monitoreo de Indicadores Institucionales"
    Obj: "Mantener visibilidad permanente sobre el estado de gestión del GORE"
    Process:
      - Step: "Definición de indicadores"
        Actions:
          - "Identificar objetivos estratégicos (ERD, Ñuble 250)"
          - "Definir indicadores SMART para cada objetivo"
          - "Establecer metas y umbrales de alerta"
          - "Documentar ficha de cada indicador"
      - Step: "Recolección de datos"
        Actions:
          - "Identificar fuentes de datos por indicador"
          - "Establecer frecuencia de actualización"
          - "Definir responsable de provisión de datos"
          - "Validar calidad de datos recibidos"
      - Step: "Cálculo y análisis"
        Actions:
          - "Aplicar fórmulas definidas"
          - "Comparar con metas y períodos anteriores"
          - "Identificar tendencias y desviaciones"
          - "Documentar hallazgos"
      - Step: "Comunicación"
        Actions:
          - "Actualizar dashboard"
          - "Generar alertas si corresponde"
          - "Informar a responsables"

  - ID: DGI-CG-02
    Title: "Tipos de Dashboard"
    Dashboards:
      - Type: "Ejecutivo"
        Audience: "AR, Gobernador"
        Content: "KPIs agregados, alertas críticas"
        Frequency: "Actualización diaria"
      - Type: "División"
        Audience: "Jefe División"
        Content: "Indicadores de la división"
        Frequency: "Semanal"
      - Type: "Operativo"
        Audience: "Equipos"
        Content: "Detalle de tareas y estados"
        Frequency: "Diario"
      - Type: "Temático"
        Audience: "Comités"
        Content: "Foco específico (IPR, TD, etc.)"
        Frequency: "Según comité"

  - ID: DGI-CG-03
    Title: "Detección de Cuellos de Botella"
    Obj: "Identificar proactivamente puntos de fricción en la operación"
    AlertSignals:
      - "Indicadores bajo umbral por más de 2 períodos"
      - "Acumulación de trabajo pendiente"
      - "Incremento en tiempos de ciclo"
      - "Reclamos o consultas recurrentes sobre mismo tema"
      - "Desviaciones presupuestarias significativas"
    InvestigationProcess:
      - "Detección: Sistema de alertas o reporte de división"
      - "Verificación: Confirmar que el problema es real y significativo"
      - "Análisis: Identificar causa raíz (5 porqués, Ishikawa)"
      - "Propuesta: Formular recomendación de solución"
      - "Comunicación: Informar a responsable y AR"
      - "Seguimiento: Verificar implementación y efectividad"

  - ID: DGI-CG-04
    Title: "Estructura Informe Estado Situacional"
    Sections:
      - "1. RESUMEN EJECUTIVO: Estado general (semáforo), principales logros, alertas activas"
      - "2. INDICADORES CLAVE: Tabla resumen con tendencia, gráficos de evolución"
      - "3. ALERTAS Y RIESGOS: Problemas detectados, acciones en curso, riesgos emergentes"
      - "4. AVANCE DE INICIATIVAS: Estado de proyectos DGI, hitos cumplidos/pendientes"
      - "5. RECOMENDACIONES: Decisiones requeridas, acciones sugeridas"
      - "6. PRÓXIMO PERÍODO: Prioridades, hitos esperados"
    Frequency: "Semanal (resumen) / Mensual (completo)"

# ============================================================================
# TÍTULO IV: MODERNIZACIÓN DE PROCESOS
# ============================================================================

ModernizacionProcesos:
  - ID: DGI-MP-01
    Title: "Levantamiento y Modelado BPMN"
    Obj: "Documentar los procesos institucionales de manera estandarizada"
    Phases:
      Preparacion:
        - "Identificar proceso a levantar"
        - "Definir alcance (inicio, fin, actores)"
        - "Programar sesiones con participantes"
        - "Preparar materiales"
      Recoleccion:
        - "Realizar entrevistas con ejecutores"
        - "Observar proceso en terreno si es posible"
        - "Revisar documentación existente"
        - "Identificar variantes y excepciones"
      Modelado:
        - "Crear diagrama BPMN del proceso AS-IS"
        - "Identificar roles y sistemas involucrados"
        - "Documentar reglas de negocio"
        - "Validar con participantes"
      Documentacion:
        - "Completar ficha de proceso"
        - "Registrar métricas actuales (tiempos, volúmenes)"
        - "Identificar puntos de dolor"
        - "Almacenar en repositorio institucional"
    MinBPMNElements:
      - "Eventos de inicio y fin"
      - "Actividades con responsable"
      - "Flujos de secuencia"
      - "Compuertas de decisión"
      - "Pools/lanes por actor"
      - "Anotaciones explicativas"

  - ID: DGI-MP-02
    Title: "Análisis de Oportunidades de Mejora"
    Obj: "Identificar y priorizar mejoras a los procesos levantados"
    AnalysisDimensions:
      - Dimension: "Valor"
        Question: "¿Cada actividad agrega valor al resultado?"
      - Dimension: "Duplicación"
        Question: "¿Hay actividades redundantes?"
      - Dimension: "Esperas"
        Question: "¿Dónde se acumula trabajo sin procesar?"
      - Dimension: "Movimientos"
        Question: "¿Hay traslados innecesarios de información?"
      - Dimension: "Errores"
        Question: "¿Dónde ocurren más errores o reprocesos?"
      - Dimension: "Automatización"
        Question: "¿Qué actividades son repetitivas y basadas en reglas?"
    PrioritizationProcess:
      - "Listar todas las oportunidades identificadas"
      - "Evaluar cada una por: Impacto (alto/medio/bajo), Esfuerzo (alto/medio/bajo), Urgencia"
      - "Priorizar: Alto impacto + Bajo esfuerzo primero"
      - "Validar priorización con División responsable"
      - "Incorporar al plan de trabajo"

  - ID: DGI-MP-03
    Title: "Tipos de Automatización"
    Types:
      - Type: "RPA"
        Desc: "Automatización de tareas repetitivas"
        Ex: "Carga de datos entre sistemas"
      - Type: "Flujos de trabajo"
        Desc: "Orquestación de aprobaciones"
        Ex: "Circuito de visación"
      - Type: "Notificaciones"
        Desc: "Alertas automáticas"
        Ex: "Vencimiento de convenio"
      - Type: "Reportes"
        Desc: "Generación programada"
        Ex: "Informe semanal"
      - Type: "Integraciones"
        Desc: "Conexión entre sistemas"
        Ex: "SIGFE - Dashboard"

  - ID: DGI-MP-04
    Title: "Proceso de Implementación"
    Phases:
      - Phase: "Preparación"
        Actions:
          - "Confirmar recursos disponibles"
          - "Comunicar cambio a afectados"
          - "Preparar materiales de capacitación"
          - "Configurar ambiente"
      - Phase: "Piloto"
        Actions:
          - "Implementar en alcance reducido"
          - "Monitorear intensivamente"
          - "Recoger feedback"
          - "Ajustar si es necesario"
      - Phase: "Despliegue"
        Actions:
          - "Extender a alcance completo"
          - "Capacitar usuarios"
          - "Documentar procedimiento actualizado"
          - "Comunicar nuevo proceso"
      - Phase: "Estabilización"
        Actions:
          - "Monitorear indicadores"
          - "Atender incidentes"
          - "Refinar configuración"
          - "Cerrar proyecto formal"
      - Phase: "Mejora continua"
        Actions:
          - "Medir resultados vs. línea base"
          - "Identificar nuevas oportunidades"
          - "Documentar lecciones aprendidas"

# ============================================================================
# TÍTULO V: TRANSFORMACIÓN DIGITAL
# ============================================================================

TransformacionDigital:
  - ID: DGI-TD-01
    Title: "Coordinación Cumplimiento Ley 21.180"
    Obj: "Asegurar que el GORE avance hacia el cumplimiento de la TDE"
    Responsibilities:
      Monitoreo:
        - "Mantener inventario de procesos y su nivel de digitalización"
        - "Identificar brechas respecto a requisitos TDE"
        - "Reportar estado al Comité de TD"
      Planificacion:
        - "Proponer roadmap de cumplimiento"
        - "Priorizar procesos a digitalizar"
        - "Estimar recursos requeridos"
      Facilitacion:
        - "Apoyar a divisiones en digitalización de sus procesos"
        - "Coordinar con Unidad de Operaciones aspectos técnicos"
        - "Gestionar dependencias entre iniciativas"
      Verificacion:
        - "Validar que implementaciones cumplan normas técnicas"
        - "Documentar evidencia de cumplimiento"
        - "Preparar información para auditorías"
    ComplianceChecklist:
      - "Procedimiento documentado"
      - "Firma electrónica implementada"
      - "Notificaciones electrónicas habilitadas"
      - "Expediente electrónico configurado"
      - "Interoperabilidad especificada"
      - "Autenticación con ClaveÚnica (si aplica)"

  - ID: DGI-TD-02
    Title: "Gestión del Comité de TD"
    Obj: "Proveer soporte técnico al Comité de TD institucional"
    Functions:
      SecretariaTecnica:
        - "Preparar tabla y materiales para sesiones"
        - "Elaborar actas"
        - "Dar seguimiento a acuerdos"
      AnalisisPropuestas:
        - "Presentar estado de avance TDE"
        - "Proponer iniciativas para decisión"
        - "Evaluar factibilidad de solicitudes"
      Coordinacion:
        - "Articular a las divisiones en temas transversales"
        - "Gestionar dependencias entre proyectos"
        - "Escalar impedimentos"
    Frequency: "Mínimo mensual, o con mayor frecuencia según agenda"

  - ID: DGI-TD-03
    Title: "Administración Funcional de Sistemas"
    Obj: "Asegurar que los sistemas de gestión de trabajo operen correctamente"
    ResponsibilityMatrix:
      - Function: "Definir requisitos funcionales"
        DGI: R
        TI: C
      - Function: "Configurar reglas de negocio"
        DGI: R
        TI: I
      - Function: "Definir perfiles y roles"
        DGI: R
        TI: C
      - Function: "Habilitar cuentas y accesos"
        DGI: I
        TI: R
      - Function: "Mantener infraestructura/seguridad"
        DGI: I
        TI: R
      - Function: "Resolver incidentes de negocio"
        DGI: R
        TI: I
      - Function: "Resolver incidentes técnicos"
        DGI: C
        TI: R
      - Function: "Evolucionar plataforma"
        DGI: R
        TI: C

  - ID: DGI-TD-04
    Title: "Interoperabilidad y Datos"
    Obj: "Avanzar hacia un ecosistema de datos integrado"
    Principles:
      - "Datos como activo: Los datos institucionales son un activo estratégico"
      - "Fuente única de verdad: Cada dato tiene una fuente autoritativa definida"
      - "Interoperabilidad por diseño: Los sistemas deben poder intercambiar datos"
    DataManagementProcess:
      Inventario:
        - "Identificar conjuntos de datos críticos"
        - "Documentar ubicación y formato"
        - "Identificar dueño de datos"
      Calidad:
        - "Definir estándares de calidad por conjunto"
        - "Monitorear cumplimiento"
        - "Gestionar correcciones"
      Integracion:
        - "Especificar necesidades de intercambio"
        - "Diseñar interfaces (APIs, archivos)"
        - "Implementar y monitorear"

# ============================================================================
# TÍTULO VI: GESTIÓN DEL CONOCIMIENTO
# ============================================================================

GestionConocimiento:
  - ID: DGI-KC-01
    Title: "Curación y Actualización de KB"
    Obj: "Mantener la base de conocimiento institucional actualizada y útil"
    CurationProcess:
      - Phase: "Identificación"
        Actions:
          - "Detectar conocimiento nuevo o actualizado"
          - "Evaluar relevancia institucional"
          - "Priorizar incorporación"
      - Phase: "Estructuración"
        Actions:
          - "Formatear según estándares KODA"
          - "Asignar metadatos (URN, categorías)"
          - "Vincular con artefactos relacionados"
      - Phase: "Validación"
        Actions:
          - "Verificar exactitud del contenido"
          - "Validar con expertos de dominio"
          - "Aprobar publicación"
      - Phase: "Publicación"
        Actions:
          - "Incorporar al catálogo"
          - "Actualizar índices y referencias"
          - "Comunicar disponibilidad"
      - Phase: "Mantenimiento"
        Actions:
          - "Revisar vigencia periódicamente"
          - "Actualizar cuando hay cambios normativos"
          - "Deprecar contenido obsoleto"
    PrioritizationCriteria:
      - "Frecuencia de consulta esperada"
      - "Criticidad para operación"
      - "Riesgo de información desactualizada"
      - "Demanda explícita de usuarios"

  - ID: DGI-KC-02
    Title: "Administración de Agentes IA"
    Obj: "Gestionar el ciclo de vida de los agentes de IA institucionales"
    Lifecycle:
      Diseno:
        - "Definir propósito y alcance del agente"
        - "Especificar fuentes de conocimiento"
        - "Diseñar flujos de interacción"
        - "Establecer límites de actuación"
      Desarrollo:
        - "Configurar agente según especificación"
        - "Entrenar con conocimiento relevante"
        - "Probar funcionamiento"
      Despliegue:
        - "Habilitar acceso a usuarios"
        - "Capacitar en uso"
        - "Monitorear adopción"
      Operacion:
        - "Monitorear interacciones"
        - "Detectar respuestas inadecuadas"
        - "Refinar entrenamiento"
        - "Actualizar conocimiento"
      Evolucion:
        - "Evaluar efectividad"
        - "Identificar mejoras"
        - "Implementar versiones mejoradas"
    AIGovernance:
      - "Todo agente debe tener un dueño funcional"
      - "Las respuestas deben ser auditables"
      - "El conocimiento base debe estar documentado"
      - "Los usuarios deben saber que interactúan con IA"

  - ID: DGI-KC-03
    Title: "Capacitación y Gestión del Cambio"
    Obj: "Facilitar la adopción de nuevas prácticas y herramientas"
    Principles:
      - "Cambio centrado en personas: La tecnología es medio, no fin"
      - "Comunicación permanente: Informar el porqué antes del qué"
      - "Participación: Involucrar a afectados en diseño de soluciones"
      - "Gradualidad: Cambios incrementales sobre revoluciones"
    ChangeManagementProcess:
      - Phase: "Preparación"
        Actions:
          - "Identificar stakeholders"
          - "Evaluar impacto del cambio"
          - "Diseñar estrategia de comunicación"
          - "Identificar resistencias potenciales"
      - Phase: "Comunicación"
        Actions:
          - "Explicar el porqué del cambio"
          - "Mostrar beneficios concretos"
          - "Responder dudas y preocupaciones"
          - "Mantener comunicación constante"
      - Phase: "Capacitación"
        Actions:
          - "Diseñar programa según audiencia"
          - "Ejecutar capacitaciones prácticas"
          - "Proveer materiales de apoyo"
          - "Evaluar aprendizaje"
      - Phase: "Acompañamiento"
        Actions:
          - "Proveer soporte durante transición"
          - "Resolver problemas emergentes"
          - "Celebrar éxitos tempranos"
          - "Ajustar según feedback"
      - Phase: "Consolidación"
        Actions:
          - "Verificar adopción"
          - "Reforzar nuevas prácticas"
          - "Documentar lecciones aprendidas"

# ============================================================================
# TÍTULO VII: FUNCIONES HABILITADORAS (NUEVO)
# ============================================================================

EnablementFunctions:
  - ID: DGI-EF-01
    Title: "Gestión Arquitectural"
    Purpose: "Diseñar estructura organizacional saludable (Meyer)"
    KeyConcepts:
      - "Golden Rule: Autoridad = Responsabilidad"
      - "Dominios Precisos: Sin superposiciones"
      - "Sinergias: Agrupación de especialistas"

  - ID: DGI-EF-02
    Title: "Dinámica de Producción"
    Purpose: "Gestionar flujo de trabajo (Lean/Kanban)"
    KeyConcepts:
      - "Visualización de flujo (Tableros)"
      - "Límites WIP"
      - "Métricas: Throughput, Lead Time"

  - ID: DGI-EF-03
    Title: "Navegación Social"
    Purpose: "Gestión del cambio y relaciones (ADKAR)"
    KeyConcepts:
      - "Lobbista Interno: Facilitar, no imponer"
      - "Modelo ADKAR: Awareness, Desire, Knowledge, Ability, Reinforcement"
      - "Influencia Ética: Reciprocidad, prueba social"

# ============================================================================
# TÍTULO VIII: COORDINACIÓN INSTITUCIONAL
# ============================================================================

CoordinacionInstitucional:
  - ID: DGI-CI-01
    Title: "Relación con Administración Regional"
    Canal: "Reunión semanal de coordinación"
    Content:
      - "Estado de iniciativas DGI"
      - "Alertas y escalamientos"
      - "Decisiones requeridas"
      - "Prioridades para próximo período"
    Escalamiento: "Temas que requieren decisión de AR se escalan mediante Informe Ejecutivo con opciones y recomendación"

  - ID: DGI-CI-02
    Title: "Matriz de Interacción con Divisiones"
    Interactions:
      - Division: "Gabinete"
        InteractionType: "Agenda estratégica, comunicación política"
        Frequency: "Según necesidad"
      - Division: "DAF"
        InteractionType: "Indicadores presupuestarios, rendiciones"
        Frequency: "Semanal"
      - Division: "DIPIR"
        InteractionType: "Cartera IPR, estados de avance"
        Frequency: "Semanal"
      - Division: "Jurídica"
        InteractionType: "Convenios, resoluciones, cumplimiento"
        Frequency: "Quincenal"
      - Division: "DIPLADE"
        InteractionType: "Indicadores ERD, planificación"
        Frequency: "Mensual"
      - Division: "Unidad Operaciones"
        InteractionType: "Sistemas, interoperabilidad, infraestructura"
        Frequency: "Mensual (Mesa Técnica)"
      - Division: "Auditoría Interna"
        InteractionType: "Cumplimiento, control interno"
        Frequency: "Trimestral"

  - ID: DGI-CI-03
    Title: "Protocolo de Escalamiento"
    Levels:
      - Level: 1
        Situation: "Incidente operativo"
        EscalateTo: "Jefe DGI"
        Deadline: "4 horas"
      - Level: 2
        Situation: "Bloqueo de proyecto"
        EscalateTo: "Administración Regional"
        Deadline: "24 horas"
      - Level: 3
        Situation: "Conflicto entre divisiones"
        EscalateTo: "Administración Regional"
        Deadline: "48 horas"
      - Level: 4
        Situation: "Decisión estratégica"
        EscalateTo: "Gobernador (vía AR)"
        Deadline: "Según urgencia"
    RequiredInfo:
      - "Descripción del problema"
      - "Impacto si no se resuelve"
      - "Opciones de solución"
      - "Recomendación"
      - "Plazo requerido para decisión"
      - "Firma responsable del escalamiento"

  - ID: DGI-CI-04
    Title: "Participación en Comités"
    Committees:
      - Name: "Comité de Transformación Digital"
        Role: "Secretaría técnica"
        Frequency: "Mensual"
      - Name: "Comité de Coordinación Regional"
        Role: "Informante"
        Frequency: "Según convocatoria"
      - Name: "Mesas de trabajo temáticas"
        Role: "Facilitador técnico"
        Frequency: "Según necesidad"
