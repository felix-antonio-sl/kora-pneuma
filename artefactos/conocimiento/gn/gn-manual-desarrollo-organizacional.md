---
urn: urn:gn:kb:gn-manual-desarrollo-organizacional
nombre: gn-manual-desarrollo-organizacional
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-desarrollo-organizacional; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_042_manual_desarrollo_organizacional_koda.yml (sha256:7df9ede4a906dc2c5106b0d1ace27133be2269a24e24a4dd80cb766dd3d3e75e); URN KODA legado urn:gorenuble:gn:manual-desarrollo-organizacional:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-desarrollo-organizacional:1.0.0"
  title: "Manual 3.4: Desarrollo Organizacional y Capacitación"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_4_desarrollo_organizacional.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2025-12-16"
    last_modified_at: "2025-12-16"
    signature: null

ID: GN-MANUAL-DESARROLLO-ORGANIZACIONAL-KODA-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "IA-CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Source_ID: MANUAL-DESARROLLO-ORG-01
Primary-Source: staging/brow_speculativo/manual_3_4_desarrollo_organizacional.md
Authoritative-Sources:
  - Path: "staging/temp/brutos ordenados/01_gestion_personas/res_exta_132_designa_encargado_y_referentes_tecnicos_cdc_2025_koda.yml"
    Type: "CDC-Resolution"
    Priority: 1
  - Path: "staging/temp/brutos ordenados/01_gestion_personas/res_exta_817_define_equipos_trabajo_cdc_2025_koda.yml"
    Type: "CDC-Teams-Resolution"
    Priority: 1
Last-Validated: "2025-12-18"
Source-Hierarchy:
  - Level: 1
    Description: "Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*)"
  - Level: 2
    Description: "Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*)"
  - Level: 3
    Description: "Fuentes Especulativas (staging/brow_speculativo/*)"
Ctx: "Manual 3.4: Desarrollo Organizacional y Capacitación (GORE Ñuble)."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.

    REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. Other external mentions use Ctx:, Ctx_Required:, Ctx_Optional:, or Src:.

    LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
    END_LLM_INSTRUCTIONS

Manual_3_4_Desarrollo_Organizacional_y_Capacitacion:
  ID: MANUAL-DESARROLLO-ORG-CONTENT-01
  Title: "Manual 3.4: Desarrollo Organizacional y Capacitación"

  Objetivo:
    ID: MANUAL-DESARROLLO-ORG-OBJ-01
    Obj: "Potenciar las competencias de los funcionarios y promover un ambiente laboral positivo, alineado con los objetivos estratégicos del GORE Ñuble."

  Seccion_I_Capacitacion_y_Formacion:
    ID: MANUAL-DESARROLLO-ORG-SEC-I-01
    Title: "Sección I: Capacitación y Formación"

    1_Sistema_de_Capacitacion:
      ID: MANUAL-DESARROLLO-ORG-SEC-I-SISTEMA-01
      Ctx: "Regido por el Estatuto Administrativo y normas del Servicio Civil, busca perfeccionar los conocimientos y habilidades."

    2_Deteccion_de_Necesidades_de_Capacitacion_DNC:
      ID: MANUAL-DESARROLLO-ORG-SEC-I-DNC-01
      Proc:
        - Act: "Proceso Anual"
          Def: "Consulta a jefaturas y funcionarios sobre brechas de competencias."
      Fuentes_de_Informacion:
        - "Evaluación del desempeño."
        - "Nuevas normativas o sistemas (ej. SIGFE, Transformación Digital)."
        - "Objetivos estratégicos regionales (ERD)."

    3_Plan_Anual_de_Capacitacion_PAC:
      ID: MANUAL-DESARROLLO-ORG-SEC-I-PAC-01
      Elaboracion:
        Resp: "Área de Gestión de Personas"
        Act: "Consolida el DNC."
      Comite_Bipartito_de_Capacitacion:
        Def: "Instancia consultiva con representantes de la asociación de funcionarios y la administración. Revisa y sugiere acciones."
      Aprobacion:
        Req: "Resolución Exenta del Gobernador(a)."
      Ejecucion:
        Proc:
          - "Cursos internos"
          - "Cursos externos"
          - "e-learning"
      Compromiso:
        Req:
          - "Funcionario capacitado debe replicar conocimientos o aplicarlos."
          - "Renuncias post-curso pueden implicar devolución de costos (según reglamento)."

      Rec_Prioridad_en_Competencias_Digitales_Estrategia_TDE:
        ID: MANUAL-DESARROLLO-ORG-SEC-I-TIP-DIGITAL-01
        Rec: "Se priorizarán acciones formativas en competencias digitales (uso de plataformas, firma electrónica, seguridad de la información), conforme a la Estrategia de Capacitación de la Transformación Digital del Estado."

  Seccion_II_Gestion_del_Desempeno:
    ID: MANUAL-DESARROLLO-ORG-SEC-II-01
    Title: "Sección II: Gestión del Desempeño"

    4_Sistema_de_Calificaciones:
      ID: MANUAL-DESARROLLO-ORG-SEC-II-CALIFICACIONES-01
      Def: "Instrumento formal para evaluar el desempeño funcionario."
      Periodo:
        Req: "Anual (1 de septiembre al 31 de agosto)."
      Etapas:
        - Etapa: "1. Precalificación"
          Resp: "Jefe Directo"
          Def: "Evalúa factores cualitativos y cuantitativos."
        - Etapa: "2. Junta Calificadora"
          Def: "Comité colegiado que revisa las precalificaciones y asigna la nota final y Lista (1: Distinción, 2: Buena, 3: Condicional, 4: Eliminación)."
        - Etapa: "3. Apelación"
          Proc:
            - "Funcionario puede apelar ante la Junta"
            - "En segunda instancia, ante la Contraloría (por vicios de legalidad)."

    5_Metas_y_Compromisos_PMG:
      ID: MANUAL-DESARROLLO-ORG-SEC-II-PMG-01
      Metas_de_Gestion_Institucional:
        Def: "Definidas anualmente (ej. eficiencia presupuestaria, atención usuarios)."
      Metas_de_Desempeno_Colectivo:
        Def: "Definidas por equipo/división."
      Evaluacion:
        Res: "El cumplimiento determina el pago del Componente de Desempeño de la Asignación de Modernización (pagado trimestralmente)."

  Seccion_III_Desarrollo_Organizacional:
    ID: MANUAL-DESARROLLO-ORG-SEC-III-01
    Title: "Sección III: Desarrollo Organizacional"

    6_Clima_Laboral:
      ID: MANUAL-DESARROLLO-ORG-SEC-III-CLIMA-01
      Medicion:
        Req: "Aplicación bianual de encuestas de clima laboral (ej. ISTAS 21)."
      Intervencion:
        Proc:
          - "Planes de acción para abordar brechas (liderazgo, comunicación, condiciones físicas)."

    7_Conciliacion_Trabajo_Vida:
      ID: MANUAL-DESARROLLO-ORG-SEC-III-CONCILIACION-01
      Politicas:
        Rec:
          - "Promoción de corresponsabilidad parental"
          - "Respeto de horarios"
          - "Derecho a desconexión"
      Teletrabajo:
        Cond: "Modalidad sujeta a factibilidad técnica y normativa específica (Ley de Presupuestos / Reglamento Interno), priorizando tareas que permitan medición por objetivos."

  Nota_Final:
    ID: MANUAL-DESARROLLO-ORG-NOTA-01
    Ctx: "Este manual fomenta la carrera funcionaria y la profesionalización del capital humano regional. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER."

Referencias_Cruzadas:
  ID: GN-MANUAL-DESARROLLO-ORG-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml"
