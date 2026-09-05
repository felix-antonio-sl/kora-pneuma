---
urn: urn:gn:kb:gn-manual-remuneraciones
nombre: gn-manual-remuneraciones
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-remuneraciones; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_049_manual_remuneraciones_koda.yml (sha256:f42e5eac8b66e485c7b847e6bfe005468fd00134d837589bb24ed1a1972e76f4); URN KODA legado urn:gorenuble:gn:manual-remuneraciones:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-remuneraciones:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2025-12-14"
    last_modified_at: "2025-12-16"
    signature: null

ID: GN-MANUAL-REMUNERACIONES-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "IA-CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Ctx: "Manual 3.2: Remuneraciones y Compensaciones."
Primary-Source: "staging/brow_speculativo/manual_3_2_remuneraciones.md"
Authoritative-Source:
  Path: "staging/temp/brutos ordenados/01_gestion_personas/PROCEDIMIENTO DE SOLICITUD, CÁLCULO Y PAGO DE REMUNERACIONES.md"
  Priority: 1
  Type: "Official-Procedure-GDP"
  Last-Validated: "2025-12-18"
Source-Hierarchy:
  - Level: 1
    Description: "Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*)"
  - Level: 2
    Description: "Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*)"
  - Level: 3
    Description: "Fuentes Especulativas (staging/brow_speculativo/*)"

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

Manual_3_2_Remuneraciones_y_Compensaciones:
  ID: GN-MANUAL-REM-ROOT-01
  Obj: "Regular el proceso de cálculo, validación y pago de las remuneraciones del personal del GORE Ñuble, asegurando exactitud, oportunidad y cumplimiento legal."

  Seccion_I_Estructura_de_Remuneraciones:
    ID: GN-MANUAL-REM-S1-01

    Escala_de_Sueldos_y_Haberes:
      ID: GN-MANUAL-REM-S1-EUS-01
      Req: "Estructura rige por EUS y leyes especiales de reajuste Sector Público."
      Componentes:
        Sueldo_Base:
          ID: GN-MANUAL-REM-S1-SB-01
          Def: "Asignado según grado EUS."
        Asignaciones_Permanentes:
          ID: GN-MANUAL-REM-S1-AP-01
          Items:
            - "Antigüedad (Bienios)."
            - "Profesional / Directiva / Jefatura."
            - "Zona (según localidad)."
            - "Modernización (Ley 19.553): Componente Base y por Desempeño Institucional/Colectivo."
        Asignaciones_Transitorias:
          ID: GN-MANUAL-REM-S1-AT-01
          Items:
            - "Viáticos (Comisiones de Servicio)."
            - "Horas Extraordinarias (Trabajo fuera de jornada)."

    Honorarios:
      ID: GN-MANUAL-REM-S1-HON-01
      Condiciones:
        - Req: "Monto definido en contrato a Suma Alzada."
        - Req: "No perciben asignaciones de escala EUS (zona, antigüedad, etc.)."
        - Req: "Sujeto a boleta de honorarios mensual (electrónica)."

  Seccion_II_Proceso_de_Calculo_y_Pago:
    ID: GN-MANUAL-REM-S2-01

    Ciclo_Mensual_de_Remuneraciones:
      ID: GN-MANUAL-REM-S2-CICLO-01
      Proc:
        - Paso: "1. Recopilación y Apertura (Días 01 - 14)"
          Act: "Cierre de recepción de novedades (licencias, horas extra visadas, nuevos contratos)."
          Input: "Formularios GDP firmados y Decretos tramitados."
        - Paso: "2. Proceso y Cálculo (Días 15 - 17)"
          Act: "Ingreso al sistema, cálculo de brutos, descuentos y líquidos."
        - Paso: "3. Validación y VB (Día 18)"
          Act: "Revisión de nóminas preliminares por Jefatura GDP y Control."
        - Paso: "4. Pago (Fecha Legal)"
          Req: "Día 19 del mes (o hábil anterior). Transferencia efectiva a cuentas funcionarios."
        - Paso: "5. Reliquidaciones y Planilla Suplementaria (Días 19 - 25)"
          Act: "Pagos rechazados o ajustes de última hora."
        - Paso: "6. Pago Cotizaciones (Día 20-30)"
          Act: "Declaración y pago PREVIRED."

    Horas_Extraordinarias_y_Viaticos:
      ID: GN-MANUAL-REM-S2-HEV-01
      Horas_Extras:
        ID: GN-MANUAL-REM-S2-HE-01
        Topes_Institucionales_Ref_PR_DAF_0005:
          - "Diurnas: Máximo 20 horas mensuales."
          - "Nocturnas/Festivas: Máximo 16 horas mensuales."
          - "Total Máximo: 40 horas (solo casos criticos excepcionales autorizados por Gobernador)."
        Req:
          - "Resolución previa."
          - "Sistema de control horario biométrico debe respaldar la solicitud."
      Viaticos:
        ID: GN-MANUAL-REM-S2-VIAT-01
        Cond:
          - "Pago anticipado o devengado."
        Reglas:
          - "Escala según grado y destino (nacional/internacional)."
          - "Rendición de cometido requerida para cierre administrativo."

  Seccion_III_Obligaciones_y_Control:
    ID: GN-MANUAL-REM-S3-01

    Descuentos_Legales_y_Voluntarios:
      ID: GN-MANUAL-REM-S3-DESC-01
      Obligatorios:
        Def: "Impuesto Único de Segunda Categoría, AFP/IPS, FONASA/Isapre, Seguro de Cesantía (Código del Trabajo)."
      Voluntarios:
        Def: "Ahorro previsional, asociaciones de funcionarios, convenios de bienestar (hasta tope legal del 15% o 25% de remuneración líquida)."

    Obligaciones_de_Informacion_Ley_de_Presupuestos:
      ID: GN-MANUAL-REM-S3-INF-01
      Src: "Art. 14 N°10 Ley Presupuestos 2026."
      Req: "Remitir semestralmente a Comisión de Hacienda de la Cámara de Diputados:"
      Entregables:
        - "Gastos asociados a remuneraciones."
        - "Calidad jurídica de contratos."
        - "Porcentajes por estamento y género."
        - "Duración media de contratos y re-contrataciones."

    Transparencia_Activa:
      ID: GN-MANUAL-REM-S3-TA-01
      Src: "Ley 20.285."
      Req: "Publicación mensual en sitio web de dotación de planta, contrata y honorarios con remuneraciones brutas y líquidas."

  Complementos_y_Sistema_Operativo:
    ID: GN-MANUAL-REM-CTX-01
    Ctx: "Este manual se complementa con el Manual 3.1 (Ciclo de Vida) para la fuente del dato (personas) y Manual 1.3 (Tesorería) para la ejecución del gasto. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER."

Referencias_Cruzadas:
  ID: GN-MANUAL-REM-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_3_tiempo_ausentismo_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml"
