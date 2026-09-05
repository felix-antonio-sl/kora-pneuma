---
urn: urn:gn:kb:gn-manual-bienestar
nombre: gn-manual-bienestar
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-bienestar; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_052_manual_bienestar_koda.yml (sha256:8f40ffdfd4bfc5154ed3dc54321029ad89bd8cddd6457e31c6ea185537da221e); URN KODA legado urn:gorenuble:gn:manual-bienestar:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-bienestar:1.0.0"
  title: "Manual 3.5: Bienestar y Calidad de Vida"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_5_bienestar_koda.yml"
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

ID: GN-MANUAL-BIENESTAR-KODA-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "IA-CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Source_ID: MANUAL-BIENESTAR-01
Primary-Source: staging/brow_speculativo/manual_3_5_bienestar.md
Ctx: "Gestionar beneficios y prestaciones sociales para mejorar calidad de vida de funcionarios y cargas familiares."

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

Manual_3_5_Bienestar_y_Calidad_de_Vida:
  ID: GN-MANUAL-BIENESTAR-CONTENT-01
  Title: "Manual 3.5: Bienestar y Calidad de Vida"

  Objetivo:
    ID: GN-MANUAL-BIENESTAR-OBJ-01
    Obj: "Gestionar los beneficios y prestaciones sociales destinados a mejorar la calidad de vida de los funcionarios y sus cargas familiares."

  Seccion_I_Servicio_de_Bienestar:
    ID: GN-MANUAL-BIENESTAR-SEC-I-01
    Title: "Sección I: Servicio de Bienestar"

    1_Afiliacion_y_Aportes:
      ID: GN-MANUAL-BIENESTAR-SEC-I-AFILIACION-01
      Caracter:
        Def: "La afiliación es voluntaria y la desafiliación es libre."
      Socios:
        Req: "Funcionarios de Planta y Contrata (y jubilados que deseen permanecer)."
      Financiamiento:
        - Fuente: "Aporte del Funcionario"
          Def: "Porcentaje de su remuneración imponible (descuento por planilla)."
        - Fuente: "Aporte Institucional"
          Def: "Aporte anual definido en Ley de Presupuestos (Subtítulo 24)."
        - Fuente: "Cuota de Incorporación"
          Def: "Pago único al ingresar."

    2_Administracion:
      ID: GN-MANUAL-BIENESTAR-SEC-I-ADMIN-01
      Organos:
        - Organo: "Consejo Administrativo"
          Def: "Órgano colegiado con representantes de la institución y de los socios (electos). Decide sobre presupuestos y beneficios."
        - Organo: "Unidad de Bienestar"
          Def: "Ejecuta las decisiones del Consejo y administra los fondos."

  Seccion_II_Beneficios_y_Prestaciones:
    ID: GN-MANUAL-BIENESTAR-SEC-II-01
    Title: "Sección II: Beneficios y Prestaciones"

    3_Ayudas_Medicas_y_Dentales:
      ID: GN-MANUAL-BIENESTAR-SEC-II-AYUDA-SALUD-01
      Reembolso:
        Def: "Bonificación de un porcentaje del copago (no cubierto por Isapre/FONASA y seguro complementario) en consultas, exámenes, medicamentos, óptica y prótesis."
      Tope_Anual:
        Req: "Monto máximo de reembolso por socio/carga."

    4_Ayudas_Economicas:
      ID: GN-MANUAL-BIENESTAR-SEC-II-AYUDA-ECO-01
      Subsidios:
        Def: "Asignaciones en dinero por eventos vitales (Nacimiento, Matrimonio/AUC, Fallecimiento)."
      Bonos_Escolares:
        Def: "Aporte anual por escolaridad de hijos (Pre-kinder a Universidad)."
      Becas_de_Excelencia:
        Def: "Premio al rendimiento académico del funcionario o hijos."

    5_Prestamos:
      ID: GN-MANUAL-BIENESTAR-SEC-II-PRESTAMOS-01
      Tipos: ["Médico", "Auxilio (libre disposición)", "Escolar", "Habitacional"]
      Condiciones:
        - "Interés bajo"
        - "Descuento por planilla en cuotas"
        - "Requiere codeudor solidario (otro socio) según monto"

    6_Convenios:
      ID: GN-MANUAL-BIENESTAR-SEC-II-CONVENIOS-01
      Comerciales:
        Def: "Descuentos en farmacias, gimnasios, ópticas, librerías, etc."
      Institucionales:
        Def: "Acuerdos con Cajas de Compensación (CCAF) para créditos sociales y turismo."

  Seccion_III_Calidad_de_Vida:
    ID: GN-MANUAL-BIENESTAR-SEC-III-01
    Title: "Sección III: Calidad de Vida"

    7_Actividades_Recreativas_y_Culturales:
      ID: GN-MANUAL-BIENESTAR-SEC-III-ACTIVIDADES-01
      Act:
        - "Organización de eventos de camaradería (Aniversario GORE, Fiestas Patrias, Navidad)."
        - "Actividades deportivas y talleres."

    8_Prevencion_de_Riesgos:
      ID: GN-MANUAL-BIENESTAR-SEC-III-RIESGOS-01
      Act:
        - "Coordinación con Mutualidad (ACHS/IST) para evaluación de puestos de trabajo y prevención de enfermedades profesionales."

  Nota_de_Cierre:
    ID: GN-MANUAL-BIENESTAR-NOTA-01
    Ctx: "Este manual se rige por el Reglamento General de Servicios de Bienestar y el Reglamento Interno Específico del GORE Ñuble. Los procesos aquí descritos se gestionan operativamente a través del sistema SIGPER."

Referencias_Cruzadas:
  ID: GN-MANUAL-BIENESTAR-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_1_ciclo_vida_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_4_desarrollo_organizacional.yml"
