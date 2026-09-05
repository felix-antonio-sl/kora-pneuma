---
urn: urn:gn:kb:gn-manual-tiempo-ausentismo
nombre: gn-manual-tiempo-ausentismo
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-tiempo-ausentismo; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_051_manual_asistencia_koda.yml (sha256:647431ca047ddbf135e2e930f309e3da03168d6faabea3efaa5b6e3886429a0a); URN KODA legado urn:gorenuble:gn:manual-tiempo-ausentismo:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-tiempo-ausentismo:1.0.0"
  title: "Manual 3.3: Gestión del Tiempo y Ausentismo"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml"
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

ID: GN-MANUAL-TIEMPO-AUSENTISMO-KODA-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "IA-CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Source_ID: MANUAL-TIEMPO-AUSENTISMO-01
Primary-Source: staging/brow_speculativo/manual_3_3_tiempo_ausentismo.md
Authoritative-Source:
  Path: "staging/temp/brutos ordenados/01_gestion_personas/MANUAL GENERAL DE PROCEDIMIENTOS INTERNOS DE GDP.md"
  Priority: 1
  Type: "Official-Manual-GDP"
  Section: "Autorización Trabajo Extraordinario, Descanso Compensatorio"
  Last-Validated: "2025-12-18"
Source-Hierarchy:
  - Level: 1
    Description: "Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*)"
  - Level: 2
    Description: "Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*)"
  - Level: 3
    Description: "Fuentes Especulativas (staging/brow_speculativo/*)"
Ctx: "Manual: Gestión del Tiempo y Ausentismo (GORE Ñuble)."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Dln->Deadline, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.

    REFERENCE POLICY: Ref: internal only—must point to existing ID within THIS document. XRef/XRef_Required: external only—must point to a URN (optionally with #ID fragment) in another artifact. Other external mentions use Ctx:, Ctx_Required:, Ctx_Optional:, or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Manual_3_3_Gestion_del_Tiempo_y_Ausentismo:
  ID: MANUAL-TIEMPO-AUSENTISMO-CONTENT-01

  Obj: "Regular el control de asistencia, el cumplimiento de la jornada laboral y la gestión de permisos y licencias del personal, garantizando la continuidad operativa del GORE."

  Seccion_I_Jornada_y_Asistencia:
    ID: MANUAL-TIEMPO-SEC-I-01

    1_Jornada_Laboral:
      ID: MANUAL-TIEMPO-SEC-I-JORNADA-01
      Src: "Estatuto Administrativo (Ley 18.834)"
      Componentes:
        - Jornada_Ordinaria: "44 horas semanales, distribuidas de lunes a viernes."
        - Horarios: "Fijos o flexibles (según reglamento interno), garantizando presencia en horario núcleo (ej. 09:30 - 16:00)."
        - Colacion: "Mínimo 30 minutos, no imputables a la jornada de trabajo."

    2_Control_de_Asistencia:
      ID: MANUAL-TIEMPO-SEC-I-ASISTENCIA-01

      Sistema:
        Ctx: "Registro biométrico (huella/facial) o tarjeta magnética."

      Obligatoriedad:
        Req: "Todo funcionario debe registrar entrada y salida."

      Excepciones:
        Ctx: "Cargos directivos y Jefes de División (art. 22 del Código del Trabajo por analogía/exención de marcar)."

      Atrasos_y_Tiempos_Menores:
        ID: MANUAL-TIEMPO-SEC-I-ATRASOS-01
        Regla:
          Cond: "Suma de atrasos y tiempos menores de jornada en el periodo mensual."
          Req: "Si el total acumulado supera los 59 minutos, genera descuento proporcional en las remuneraciones del funcionario (PR-DAF-0004)."

  Seccion_II_Gestion_de_Derechos_Estatutarios_Ausencias_Planificadas:
    ID: MANUAL-TIEMPO-SEC-II-01
    Title: "Sección II: Gestión de Derechos Estatutarios"

    3_Feriado_Legal_Vacaciones:
      ID: MANUAL-TIEMPO-SEC-II-FERIADO-01
      Derecho:
        Ctx: "15 días hábiles con goce de sueldo tras 1 año de servicio (aumenta a 20 y 25 días según antigüedad)."
      Solicitud:
        Proc:
          - Act: "Vía sistema interno (workflow SIGPER)."
          - Req: "Aprobada por Jefatura Directa."
      Acumulacion:
        Req:
          - "Posible acumular hasta 2 períodos (requiere resolución fundada)."
        Warn: "Días no utilizados fuera de los períodos autorizados caducan automáticamente."

    4_Permisos_Administrativos:
      ID: MANUAL-TIEMPO-SEC-II-PERMISOS-01
      Dias_Administrativos:
        Ctx: "6 días anuales con goce de sueldo para fines particulares."
      Fraccionamiento:
        Req: "Pueden tomarse por días completos o medios días (mañana/tarde)."

    5_Compensacion_de_Horas:
      ID: MANUAL-TIEMPO-SEC-II-COMPENSACION-01
      Ctx: "Devolución de tiempo por trabajos extraordinarios realizados en horario nocturno, festivo o fines de semana, autorizada previamente por Resolución."

  Seccion_III_Licencias_Medicas_Ausencias_No_Planificadas:
    ID: MANUAL-TIEMPO-SEC-III-01
    Title: "Sección III: Gestión de Licencias Médicas (LME)"

    6_Flujo_de_Tramitacion_LME:
      ID: MANUAL-TIEMPO-SEC-III-LME-01
      Proc:
        - Paso: "1. Recepción y Validación"
          Act: "El funcionario presenta LME (electrónica vía portal I-MED o manual en papel)."
          Dln: "Max 3 días hábiles desde inicio del reposo."
        - Paso: "2. Registro y Certificación"
          Act: "GDP registra en SIGPER y emite Certificado de Remuneraciones (últimos 3 meses)."
        - Paso: "3. Tramitación Externa"
          Proc:
            - Cond: "Afiliado FONASA con Caja Compensación (CCAF)."
              Act: "Envío a CCAF dentro de 3 días hábiles."
            - Cond: "Afiliado FONASA sin CCAF."
              Act: "Envío a COMPIN dentro de 3 días hábiles."
            - Cond: "Afiliado ISAPRE."
              Act: "Envío a la Isapre respectiva dentro de 3 días hábiles."
        - Paso: "4. Resolución y Ajuste"
          Proc:
            - "Recepción de Resolución (Aprobad/Rechazada/Reducida)."
            - "Cálculo de SIL (Subsidio por Incapacidad Laboral) para recuperación."
            - "En caso de Rechazo/Reducción: Generar descuento o reintegro inmediato tras notificación (Manual 3.2)."

    7_Mantencion_de_Ingresos:
      ID: MANUAL-TIEMPO-SEC-III-REMUNERACIONES-01
      Req: "El GORE garantiza el pago íntegro de la remuneración líquida mientras el funcionario mantenga el vínculo."
      Recuperacion: "GDP tramita ante el ente pagador (Caja/Compin/Isapre) la devolución del subsidio correspondiente al empleador."

  Seccion_IV_Responsabilidades:
    ID: MANUAL-TIEMPO-SEC-IV-01
    Title: "Sección IV: Responsabilidades"

    Funcionario:
      Req: "Cuidar su asistencia, registrar marcas biométricas, solicitar permisos a tiempo y justificar ausencias en plataforma de control."

    Jefatura_Directa:
      Req:
        - "Autorizar permisos garantizando cobertura de funciones críticas del servicio."
        - "Validar cumplimiento de turnos y evitar acumulación excesiva de compensatorios."

    Gestion_de_Personas (GDP):
      Req:
        - "Administración técnica del sistema de control y SIGPER."
        - "Reportar semanalmente atrasos a Remuneraciones para corte mensual."
        - "Liderar la recuperación de subsidios por licencias médicas."

  Nota_de_Cierre:
    ID: GN-MANUAL-TIEMPO-NOTA-01
    Ctx: "Este manual se complementa con el Reglamento Interno de Higiene y Seguridad del GORE Ñuble. Los procesos de LME se rigen por el D.S. N° 3 de 1984 del Minsal."

Referencias_Cruzadas:
  ID: GN-MANUAL-TIEMPO-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml"
