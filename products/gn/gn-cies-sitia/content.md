---
urn: urn:gn:kb:gn-cies-sitia
nombre: gn-cies-sitia
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre KODA/Spec Artifact for Centro Integrado de Emergencia y Seguridad (CIES) de Ñuble con integración SITIA; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml (sha256:044186c02cafaefc284eb26474dbba52a696aed3fa5c80eaf6fc8242df79d213); URN KODA legado urn:gorenuble:gn:cies-sitia:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-10-06
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "cies", "sitia"]
familia: bok
---
# KODA/Spec Artifact for Centro Integrado de Emergencia y Seguridad (CIES) de Ñuble con integración SITIA
# Derived from kb_gn_080_cies_sitia.md

_manifest:
  urn: "urn:gorenuble:gn:cies-sitia:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_080_cies_sitia_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:intro-gores-nuble:1.0.0"
        reason: "Contexto institucional GORE Ñuble"
      - urn: "urn:gorenuble:gn:marco-legal-gores:1.0.0"
        reason: "Marco legal de referencia para protección de datos y seguridad pública"
  provenance:
    created_by: "FS"
    created_at: "2025-10-06"
    last_modified_at: "2025-11-27"
    model_collaborators: ["IA-GEMINI", "Cascade", "KODA-TRANSFORMER"]

ID: CIES-SITIA-MASTER-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator:
  - IA-GEMINI
  - Cascade
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-10-06
Modification-Date: 2025-11-27
Ctx: "Plan de Transformación Digital y IA para GORE Ñuble."
Source:
  Ctx_Required:
    - "staging/gn/kb_gn_080_cies_sitia.md"
    - "CIES SITIA.md"
    - "Ley N° 19.628 sobre Protección de la Vida Privada"
  Ctx_Optional:
    - "knowledge/domains/gn/kb_gn_200_marco_legal_gores_koda.yml"
  Primary-Source: "kb_gn_080_cies_sitia.md"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-CIES-SITIA-01
  Req: "Mandatory block following Metadata."
  Prohib: "Using for artifact creation or translation."
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact in Structured Telegraphic Style (STS).
    Your primary task is to parse and reason over THIS document with absolute fidelity,
    using only the rules defined below. This artifact is a self-contained source of truth.

    1. CORE OBJECTIVE
       - Maintain perfect fidelity to the information ("meat") and structure ("skeleton").
       - Do not summarize, interpret, or infer information not explicitly present.
       - Prohibition: These rules are exclusively for artifact CONSUMPTION, not for creation.

    2. CONCEPTUAL METAPHORS
       - "meat": Essential information, data, and facts. Must be preserved with zero loss.
       - "skeleton": Logical structure (headers, IDs, lists, relationships). Also considered "meat".
       - "fat": Non-essential verbiage (filler, rhetoric, stylistic prose). Ignore for reasoning.

    3. LEXICON MODE & EXPANSION
       This document uses an abbreviated control lexicon. Expand keywords as follows BEFORE processing:
       Act->Action, Cause->Cause, Cpt->Concept, Cond->Condition, Ctx->Context,
       Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
       Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction, Just->Justification,
       Mech->Mechanism, Mssn->Mission, Mdl->Model, Nat->Nature, Obj->Objective,
       Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation,
       Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source,
       Warn->Warning.

    4. REFERENCE POLICY
       - Ref: is used for internal cross-references ONLY.
       - Every Ref: MUST point to an ID: that exists within THIS document.
       - Mentions of external documents are contextual only and appear under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.

    5. LANGUAGE INVARIANCE POLICY
       - Keywords use the fixed control vocabulary in English (and the abbreviated forms listed).
       - All essential content following a Keyword: MUST remain in its original language (es-CL).
       - Never translate content when reasoning over this artifact.
    END_LLM_INSTRUCTIONS

Glosario_Conceptos_Clave:
  ID: CIES-SITIA-GLOSARIO-01
  Purp: "Definir y referenciar conceptos estructurales del CIES y de la integración SITIA."
  Terminos:
    - ID: CIES-SITIA-GLOS-CIES
      Ref: CIES-SITIA-DESC-CIES-NUBLE-01
      Cpt: "CIES-NUBLE"
    - ID: CIES-SITIA-GLOS-SITIA-PATENTES
      Ref: CIES-SITIA-CAP-SITIA-PATENTES-01
      Cpt: "SITIA-Patentes"
    - ID: CIES-SITIA-GLOS-SITIA-EVIDENCIA
      Ref: CIES-SITIA-CAP-SITIA-EVIDENCIA-01
      Cpt: "SITIA-Evidencia"
    - ID: CIES-SITIA-GLOS-SITIA-ARMAS
      Ref: CIES-SITIA-CAP-SITIA-ARMAS-01
      Cpt: "SITIA-Armas"
    - ID: CIES-SITIA-GLOS-SITIA-UNIF-VID
      Ref: CIES-SITIA-CAP-SITIA-UNIF-VID-01
      Cpt: "SITIA-Unificacion-Videos"
    - ID: CIES-SITIA-GLOS-GOB-DATOS
      Ref: CIES-SITIA-DESC-GOB-DATOS-01
      Cpt: "Gobernanza-Datos"
    - ID: CIES-SITIA-GLOS-SPD
      Cpt: "Subsecretaría de Prevención del Delito (SPD)"
      Src:
        - "KB-GN-200-MARCO-LEGAL-GORES-KODA / LMSP-SPD-01"
    - ID: CIES-SITIA-GLOS-CADENA-CUSTODIA
      Ref: CIES-SITIA-PROC-CADENA-CUST-01
      Cpt: "Cadena-Custodia-Digital"

Descripcion_General:
  ID: CIES-SITIA-DESC-01
  Conceptos:
    - ID: CIES-SITIA-DESC-CIES-NUBLE-01
      Cpt: CIES-NUBLE
      Def: "Centro Integrado de Emergencia y Seguridad de Ñuble."
      Nat: "Iniciativa estratégica del Gobierno Regional."
      Purp: "Fortalecer la seguridad pública y la gestión integral de riesgos."
      Ctx: "Aplicado a las 21 comunas de la región de Ñuble."
    - ID: CIES-SITIA-DESC-FUNC-PRINC-01
      Cpt: Funcionalidad-Principal
      Nat: "Núcleo para vigilancia, coordinación y respuesta ante emergencias y delitos."
      Mech: "Utiliza tecnología de punta y colaboración interinstitucional."
    - ID: CIES-SITIA-DESC-ALIANZA-01
      Cpt: Alianza-Estrategica
      Def: "Colaboración con el Sistema Integrado de Teleprotección con Inteligencia Artificial (SITIA)."
      Resp: "Subsecretaría de Prevención del Delito."
      Ref: CIES-SITIA-GLOS-SPD
      Purp: "Potenciar capacidades del CIES."
      Mech: "Integrar capacidades locales del CIES con plataformas de analítica avanzada a nivel nacional."
    - ID: CIES-SITIA-DESC-CAP-POT-01
      Cpt: Capacidades-Potenciadas
      Obj:
        - "Reforzar la detección de prófugos."
        - "Reforzar la búsqueda de personas desaparecidas."
        - "Reforzar la localización de vehículos con encargo de búsqueda."
    - ID: CIES-SITIA-DESC-GOB-DATOS-01
      Cpt: Gobernanza-Datos
      Req: "Gobernanza de datos transparente."
      Fnd: "Pleno respeto de la Ley N° 19.628."

Objetivos:
  ID: CIES-SITIA-OBJ-01
  Obj:
    - Obj: "Mejorar capacidad de prevención y respuesta ante emergencias y delitos en la región."
    - Obj: "Fortalecer coordinación interinstitucional para gestión efectiva de seguridad pública."
    - Obj: "Potenciar análisis de video con herramientas de IA de nivel nacional."
      Purp:
        - "Anticipar riesgos."
        - "Optimizar gestión de emergencias."
    - Obj: "Facilitar intercambio de evidencia digital con Ministerio Público y policías."
      Mech: "A través de plataformas unificadas."
    - Obj: "Contribuir al desarrollo social, económico y territorial de Ñuble."
      Mech: "Mediante la reducción de riesgos y amenazas."

Componentes_Clave:
  ID: CIES-SITIA-COMP-01

  Infraestructura_Tecnologica_y_Fisica:
    ID: CIES-SITIA-COMP-INFRA-01

    Sala_Monitoreo_Central:
      ID: CIES-SITIA-COMP-INFRA-SALA-01
      Ctx: "Ubicada en GORE Ñuble."
      Caracteristicas:
        - Cpt: Diseño-Ergonomia
          Def: "Sala de 77,03 m²."
          Fnd: "Diseñada según norma ISO 11064."
          Ctx: "Incluye zonas operativas, técnicas, de supervisión y de descanso."
          Purp: "Garantizar rendimiento óptimo y bienestar del personal."
        - Cpt: Visualizacion-Centralizada
          Def: "Video Wall de 6x2 metros."
          Ctx: "Pantallas LED modulares 4K."
          Mech: "Capaz de mostrar hasta 16 vistas simultáneas."
          Purp: "Permitir monitoreo global y detallado de puntos críticos."
        - Cpt: Estaciones-Trabajo
          Def: "7 estaciones de trabajo (6 operadores, 1 supervisor)."
          Ctx:
            - "3 estaciones adicionales para Unidad Operativa de Control de Tránsito (UOCT)."
            - "Cada estación equipada con monitor Full HD 32\", teclado ergonómico, joystick."
          Purp: "Control preciso de cámaras PTZ."
        - Cpt: Centro-Datos
          Def: "Infraestructura robusta."
          Ctx:
            - "Racks APC NetShelter SX."
            - "Servidores redundantes Dell PowerEdge R740."
            - "Sistemas de Alimentación Ininterrumpida (UPS)."
          Purp: "Garantizar operación continua 24/7."

    Sistema_Integrado_Camaras_y_Red:
      ID: CIES-SITIA-COMP-INFRA-CAMNET-01
      Elementos:
        - Cpt: Cobertura-Regional
          Def: "209 puntos de vigilancia en 21 comunas."
          Ctx: "140 cámaras PTZ 4K y 69 cámaras multisensor/panorámicas."
        - Cpt: Conectividad
          Def: "Red híbrida de alta velocidad con 316 nodos."
          Ctx: "80% fibra óptica (100Mbps) y 20% enlaces inalámbricos (50Mbps)."
        - Cpt: Arquitectura-Federacion
          Def: "Modelo federado para gestión centralizada con autonomía local."
          Res: "Garantiza resiliencia, robustez y escalabilidad."
        - Cpt: Software-Gestion-VMS
          Def: "Plataforma HikCentral."
          Mech: "Permite gestión centralizada, acceso a video grabado, notificaciones."
          Ctx: "Compatibilidad con estándar ONVIF."
        - Cpt: Almacenamiento-Seguro
          Def: "Capacidad para 60 días de grabaciones a máxima resolución."
          Mech: "Redundancia (RAID, ANR) y cifrado para proteger integridad de datos."

    Capacidades_Analitica_Avanzada_CIES_SITIA:
      ID: CIES-SITIA-COMP-INFRA-ANALITICA-01
      Fnd: "El sistema CIES cuenta con analítica de video (VCA) para funciones base (detección de movimiento, seguimiento, conteo, intrusión)."
      Cpt: "La capacidad es potenciada por la integración con plataformas especializadas de SITIA."
      Capacidades:
        - ID: CIES-SITIA-CAP-SITIA-PATENTES-01
          Cpt: SITIA-Patentes
          Purp: "Complementar la lectura de placas local con una red integrada nacional (pórticos públicos y privados)."
          Mech: "Datos contrastados en tiempo real con registro oficial de vehículos con encargo de búsqueda."
          Res: "Genera dashboards dinámicos sobre zonas críticas de robo y rutas probables."
        - ID: CIES-SITIA-CAP-SITIA-EVIDENCIA-01
          Cpt: SITIA-Evidencia
          Def: "Plataforma digital para la gestión de evidencias."
          Fnd: "Basada en Genetec Clearance."
          Purp: "Facilitar solicitud, almacenamiento y compartición segura de pruebas audiovisuales."
          Dest:
            - "Municipios."
            - "Policías."
            - "Fiscalía."
          Res: "Asegura cadena de custodia digital y reduce tiempos de investigación."
        - ID: CIES-SITIA-CAP-SITIA-ARMAS-01
          Cpt: SITIA-Armas
          Mech: "Implementa modelos de IA (basados en YOLOv11) en la red de cámaras."
          Purp: "Generar alertas automáticas en tiempo real al detectar un arma de fuego en la vía pública."
          Res: "Apoya labores de fiscalización y control."
        - ID: CIES-SITIA-CAP-SITIA-UNIF-VID-01
          Cpt: SITIA-Unificacion-Videos
          Purp: "Centralizar las señales de las cámaras del CIES en una interfaz única a nivel nacional."
          Mech: "Permite acceso a Carabineros de Chile."
          Res: "Refuerza la coordinación y la capacidad de respuesta ante emergencias."

  Personal_y_Estructura_Operativa:
    ID: CIES-SITIA-COMP-OPER-01
    Componentes:
      - Cpt: Equipo-Humano
        Def: "3 operadores y 1 supervisor por turno en la sala."
        Ctx: "Se integra personal de la UOCT."
      - Cpt: Turnos-Operacion
        Def: "Cobertura inicial de 16 horas diarias (08:00 a 00:00)."
        Ctx: "Dos turnos rotativos."
        Obj: "Proyección de extenderse a 24/7."
      - Cpt: Roles-Capacitacion
        Fnd: "Personal capacitado conforme al Manual de Operaciones."
        Subroles:
          - Cpt: Operadores
            Resp: "Detección temprana, clasificación de incidentes, seguimiento en tiempo real."
          - Cpt: Supervisores
            Resp: "Gestión de incidentes críticos, articulación de recursos, enlace interinstitucional."
          - Cpt: Soporte-Tecnico
            Resp: "Mantenimiento preventivo y correctivo de la plataforma."
      - Cpt: Enlaces-Interinstitucionales
        Def: "Personal que actúa como facilitador de comunicación directa."
        Dest:
          - "Carabineros."
          - "PDI."
          - "Bomberos."
          - "SAMU."
          - "21 municipios."

  Procesos_y_Protocolos_Marco_Operativo_Legal:
    ID: CIES-SITIA-COMP-PROC-01
    Fnd: "Todas las actuaciones se rigen por un estricto Manual de Operaciones."
    Req: "Garantizar el cumplimiento de la Ley N° 19.628 sobre Protección de la Vida Privada."
    Procesos:
      - Cpt: Protocolos-Vigilancia-Respuesta
        Def: "Procedimientos estandarizados para monitoreo, detección, clasificación y escalamiento de incidentes."
        Ctx: "Clasificación por prioridad (alta, media, baja)."
      - ID: CIES-SITIA-PROC-CADENA-CUST-01
        Cpt: Cadena-Custodia-Digital
        Def: "Las grabaciones son consideradas evidencia legal."
        Proc: "Su entrega se realiza únicamente bajo requerimiento formal (orden judicial o del Ministerio Público)."
        Req: "Utilizar medios seguros y controlados para garantizar validez."
      - Cpt: Gestion-Privacidad
        Proc: "Grabaciones se almacenan por un máximo de 30 días."
        Act: "Eliminación segura e irreversible posterior al plazo."
        Mech: "Ciudadanos pueden solicitar cautela de una grabación por hasta 6 meses."
        Cond: "Si son víctimas o testigos de un delito."
      - Cpt: Plan-Contingencia
        Def: "Análisis de riesgos y plan de acción."
        Purp: "Enfrentar fallos técnicos, cortes de energía o desastres naturales."
        Res: "Asegurar la continuidad operativa."
      - Cpt: Coordinacion-Interinstitucional
        Def: "Canales de comunicación directos y protocolos de acción conjunta."
        Ctx: "Con todas las entidades de seguridad y emergencia."

Sostenibilidad_y_Modelo_Gestion:
  ID: CIES-SITIA-SOST-01
  Componentes:
    - Cpt: Financiamiento-Operativo
      Mech: "Continuidad garantizada a través de presupuesto anual."
      Purp: "Cubrir gastos recurrentes (RR.HH., mantenimiento, servicios)."
    - Cpt: Mantenimiento-Garantia
      Def: "Garantía técnica de 22 meses."
      Ctx: "Incluye mantenimiento preventivo trimestral."
    - Cpt: Convenio-Colaboracion
      Mech: "La relación con SITIA se formaliza a través de un convenio marco de colaboración."
      Resp: "Subsecretaría de Prevención del Delito y Gobierno Regional."
      Ref: CIES-SITIA-GLOS-SPD
      Purp: "Establecer los ejes de cooperación en integración tecnológica, intercambio de datos y capacitación."

Beneficios_Para_Region:
  ID: CIES-SITIA-BENEF-01
  Res:
    - "Mayor seguridad y protección (disuasión y respuesta rápida)."
    - "Mejora en los tiempos de respuesta ante emergencias, minimizando daños."
    - "Fortalecimiento de la coordinación interinstitucional, optimizando uso de recursos."
    - "Generación de evidencia de alta calidad y estandarizada para apoyar procesos judiciales."
    - "Acceso a una red de inteligencia nacional, mejorando capacidad de análisis y prevención."
    - "Creación de un entorno más seguro para la inversión y la vida en comunidad en Ñuble."
