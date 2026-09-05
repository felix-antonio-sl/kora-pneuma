---
urn: urn:gn:kb:gestion-rendiciones
nombre: gestion-rendiciones
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre gestion rendiciones; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_020_gestion_rendiciones_koda.yml (sha256:704442885e25c079a494b5f6b0db030e5f22079ec2bdc45943ce9173ae77c5ce); URN KODA legado urn:gorenuble:gn:gestion-rendiciones:1.0.0; estado KODA original published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-27
lang: es
tags: [gn, gore-os, koda, gestion, rendiciones]
familia: bok
---
# Artefacto KODA/Spec – Gestión de Rendiciones de Cuentas en el GORE Ñuble
# Transformado desde: kb_gn_020_gestion_rendiciones.md

_manifest:
  urn: "urn:gorenuble:gn:gestion-rendiciones:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_020_gestion_rendiciones_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "FS"
    created_at: "2025-11-27"
    last_modified_at: "2025-11-27"
    signature: null

ID: GN-REN-GESTION-RENDICIONES-01
Version: 1.0.0
Status: published
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: Cascade
Creation-Date: 2025-11-27
Modification-Date: 2025-11-27
Ctx: "Guía integrada para la gestión de rendiciones de cuentas en el Gobierno Regional de Ñuble (GORE Ñuble)."
Primary-Source: "kb_gn_020_gestion_rendiciones.md"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning, Dln->Deadline.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documentos y fuentes legales se mencionan bajo Ctx: o Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_Rendiciones_GORE_Nuble:
  ID: GN-REN-GLOSARIO-01
  Purp: "Definir conceptos, siglas y normas clave recurrentes en la gestión de rendiciones del GORE Ñuble."
  Ref:
    - GN-REN-GLOS-REN
    - GN-REN-GLOS-GORE
    - GN-REN-GLOS-ENT-EJEC
    - GN-REN-GLOS-SISREC
    - GN-REN-GLOS-SIGFE
    - GN-REN-GLOS-EXPEDIENTE
    - GN-REN-GLOS-DAF
    - GN-REN-GLOS-UCR
    - GN-REN-GLOS-RTF
    - GN-REN-GLOS-FNDR
    - GN-REN-GLOS-FRIL
    - GN-REN-GLOS-FRPD
    - GN-REN-GLOS-SUBV8
    - GN-REN-GLOS-LOCBGAE
    - GN-REN-GLOS-LBPA
    - GN-REN-GLOS-LEY21180
    - GN-REN-GLOS-LEY21719
    - GN-REN-GLOS-RES30
    - GN-REN-GLOS-RES1858
  Terminos:
    - ID: GN-REN-GLOS-REN
      Cpt: "Rendición de Cuentas"
      Def: "Procedimiento administrativo y de control mediante el cual una persona o entidad que administra fondos públicos demuestra y justifica su correcta utilización conforme a la normativa vigente."
    - ID: GN-REN-GLOS-GORE
      Cpt: "GORE"
      Def: "Gobierno Regional; administración superior de la región, con personalidad jurídica y patrimonio propio."
    - ID: GN-REN-GLOS-ENT-EJEC
      Cpt: "Entidad Ejecutora"
      Def: "Municipalidad, servicio público u entidad privada que recibe fondos del GORE para ejecutar un proyecto o programa y debe rendir cuentas de su uso."
    - ID: GN-REN-GLOS-SISREC
      Sigla: "SISREC"
      Cpt: "Sistema de Rendición Electrónica de Cuentas"
      Def: "Plataforma de la Contraloría General de la República para la rendición electrónica de transferencias de Subtítulos 24 y 33."
    - ID: GN-REN-GLOS-SIGFE
      Sigla: "SIGFE"
      Cpt: "Sistema de Información para la Gestión Financiera del Estado"
      Def: "Sistema contable-financiero donde el GORE registra transferencias, devengos, pagos y reintegros asociados a rendiciones."
    - ID: GN-REN-GLOS-EXPEDIENTE
      Cpt: "Expediente de Rendición de Cuentas"
      Def: "Conjunto ordenado de documentos que respaldan la recepción, uso y justificación de fondos públicos, en soporte papel o electrónico."
    - ID: GN-REN-GLOS-DAF
      Sigla: "DAF"
      Cpt: "División de Administración y Finanzas"
      Def: "División del GORE responsable de la gestión financiera y administrativa, incluyendo convenios, pagos, registro y control de rendiciones."
    - ID: GN-REN-GLOS-UCR
      Sigla: "U.C.R."
      Cpt: "Unidad de Control de Rendiciones"
      Def: "Unidad especializada dentro de la DAF que centraliza y ejecuta el control operativo de rendiciones (registro, revisión, contabilización y archivo)."
    - ID: GN-REN-GLOS-RTF
      Sigla: "RTF"
      Cpt: "Referente Técnico-Financiero"
      Def: "Profesional del GORE responsable de la revisión técnica y financiera de rendiciones de una IPR o convenio."
    - ID: GN-REN-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento de proyectos y programas regionales, con exigencias específicas de rendición."
    - ID: GN-REN-GLOS-FRIL
      Sigla: "FRIL"
      Cpt: "Fondo Regional de Iniciativa Local"
      Def: "Fondo FNDR para proyectos de inversión de pequeña escala ejecutados principalmente por municipalidades."
    - ID: GN-REN-GLOS-FRPD
      Sigla: "FRPD"
      Cpt: "Fondo Regional para la Productividad y el Desarrollo"
      Def: "Fondo derivado del Royalty Minero, destinado a iniciativas de innovación, competitividad y desarrollo productivo regional."
    - ID: GN-REN-GLOS-SUBV8
      Cpt: "Subvenciones 8% FNDR"
      Def: "Recursos FNDR destinados a subvencionar actividades acotadas de interés comunitario (cultura, deporte, social, seguridad, medio ambiente), con concurso público y reglas específicas de rendición."
    - ID: GN-REN-GLOS-LOCBGAE
      Cpt: "LOCBGAE"
      Def: "Ley Orgánica Constitucional de Bases Generales de la Administración del Estado; fija principios de responsabilidad, eficiencia, probidad y transparencia que sustentan la rendición."
    - ID: GN-REN-GLOS-LBPA
      Cpt: "LBPA"
      Def: "Ley de Bases de los Procedimientos Administrativos; establece, entre otros, el expediente electrónico y el principio de escrituración electrónica."
    - ID: GN-REN-GLOS-LEY21180
      Cpt: "Ley N°21.180"
      Def: "Ley de Transformación Digital del Estado, que mandata la tramitación electrónica de procedimientos administrativos y expedientes."
    - ID: GN-REN-GLOS-LEY21719
      Cpt: "Ley N°21.719"
      Def: "Ley de Protección de Datos Personales, que regula el tratamiento de datos en expedientes y publicaciones de transparencia."
    - ID: GN-REN-GLOS-RES30
      Cpt: "Resolución N°30/2015 CGR"
      Def: "Norma de procedimiento sobre rendición de cuentas dictada por CGR, de aplicación obligatoria para el GORE y sus entidades ejecutoras."
    - ID: GN-REN-GLOS-RES1858
      Cpt: "Resolución Exenta N°1.858/2023 CGR"
      Def: "Acto que establece la obligatoriedad del uso de SISREC para rendiciones de transferencias de Subtítulos 24 y 33."

Parte_1_Marco_Conceptual_y_Normativo:
  ID: STS-KB-GN-RENDICION-MARCO-01
  Purp: "Establecer los fundamentos conceptuales y el marco legal que rigen la rendición de cuentas en el sector público chileno, con aplicabilidad directa al GORE Ñuble."

  Definicion_y_Principios:
    Definicion_Rendicion_Cuentas:
      ID: STS-KB-GN-RENDICION-DEF-01
      Src:
        - "@guia_rendiciones_gores.md"
        - "@generalidades_sistema_rendicion_electronica_cuentas_sisrec.md"
      Ref:
        - GN-REN-GLOS-REN
      Elementos:
        - Def: "Procedimiento administrativo y de control."
        - Resp: "Toda persona o entidad (pública/privada) que custodia, administra, recauda, recibe, invierte o paga fondos públicos."
        - Obj: "Demostrar y justificar la correcta utilización de dichos recursos."
        - Req: "Conforme a los fines para los cuales fueron otorgados."
        - Req: "En cumplimiento de la normativa vigente."
        - Mssn: "Comprobar cómo se realizó el ingreso, egreso o traspaso de los recursos públicos."
        - Cpt: "Deber de informar, explicar y responder por la gestión y resultados."

    Principios_Rectores:
      ID: STS-KB-GN-RENDICION-PRINCIPIOS-01
      Src: "@guia_rendiciones_gores.md (Res. 30/2015 CGR)"
      Ref:
        - GN-REN-GLOS-LOCBGAE
        - GN-REN-GLOS-RES30
      Principios:
        - Cpt: "Legalidad"
          Def: "Gastos amparados por ley y disposiciones reglamentarias."
        - Cpt: "Veracidad-Fidelidad"
          Def: "Información y documentación auténticas, íntegras y que reflejan fielmente las operaciones."
        - Cpt: "Acreditación"
          Def: "Todo ingreso, egreso o traspaso debe estar documentado con comprobantes auténticos."
        - Cpt: "Exactitud"
          Def: "Cálculos y montos deben ser precisos."
        - Cpt: "Oportunidad"
          Def: "Rendiciones presentadas dentro de los plazos establecidos."
        - Cpt: "Transparencia"
          Def: "Proceso y resultados accesibles al control ciudadano y fiscalizador."
        - Cpt: "Eficiencia-Eficacia"
          Def: "Uso de fondos orientado al logro óptimo de objetivos institucionales."
        - Cpt: "Probidad"
          Def: "Actuación recta y leal, con preeminencia del interés general; la rendición es mecanismo de verificación."

  Marco_Normativo_Aplicable:
    ID: STS-KB-GN-RENDICION-MARCO-NORMATIVA-01
    Purp: "Detallar el conjunto de normas, desde la Constitución hasta las resoluciones específicas, que regulan la rendición de cuentas para el GORE Ñuble."
    Ref:
      - GN-REN-GLOS-LOCBGAE
      - GN-REN-GLOS-LBPA
      - GN-REN-GLOS-LEY21180
      - GN-REN-GLOS-LEY21719
      - GN-REN-GLOS-RES30
      - GN-REN-GLOS-RES1858

    Normas:
      - ID: STS-KB-GN-RENDICION-NORMA-CPR-01
        Cpt: "Constitución Política de la República"
        Src: "@guia_rendiciones_gores.md"
        Fnd:
          - "Art-3. Principios de responsabilidad, eficiencia, control, probidad y transparencia como base de la rendición."
          - "Art-8. Principio de probidad como obligación; publicidad de actos como base de transparencia."
          - "Art-98-99. Establecen a CGR como órgano autónomo de control, con facultad para examinar y juzgar cuentas."
          - "Art-111-ss. Regulación de GORE, cuya autonomía se ejerce dentro del marco legal, implicando obligación de rendir cuentas."

      - ID: STS-KB-GN-RENDICION-NORMA-RES30-01
        Cpt: "Resolución N°30 de 2015, CGR"
        Src: "@resolucion_30_2015_cgr_rendicion_cuentas.txt"
        Ref:
          - GN-REN-GLOS-RES30
        Elementos:
          - Def: "Norma de procedimiento sobre rendición de cuentas, de aplicación obligatoria para el GORE Ñuble."
          - Fnd: "Art-1. Ámbito de aplicación incluye al GORE y cualquier entidad (pública/privada) que reciba fondos de éste."
          - Fnd: "Art-2. Define la constitución del expediente de rendición. Ref: STS-KB-GN-RENDICION-PROCESO-EXPEDIENTE-COMPONENTES-01."
          - Fnd: "Art-4. Define 'documentación auténtica' en papel (original)."
          - Fnd: "Art-5-9. Regula documentación electrónica/digital, exige autorización CGR, define autenticidad y validez de firma electrónica."
          - Fnd: "Art-10. Define 'expediente de rendición de cuentas'."
          - Fnd: "Art-13. Regla general de gastos posteriores a total tramitación del acto que autoriza la transferencia."
          - Prohib: "Art-18. Impide entregar nuevos fondos si hay rendiciones exigibles pendientes."
          - Fnd: "Art-26. Regula rendición de transferencias a otros servicios públicos."
          - Fnd: "Art-27. Regula rendición de transferencias a entidades privadas."
          - Fnd: "Art-31. Obliga a restituir fondos no rendidos, observados o no ejecutados."

      - ID: STS-KB-GN-RENDICION-NORMA-LOCBGAE-01
        Cpt: "Ley N°18.575 (LOCBGAE)"
        Src: "@guia_rendiciones_gores.md"
        Ref:
          - GN-REN-GLOS-LOCBGAE
        Elementos:
          - Cpt: "Ley Orgánica Constitucional de Bases Generales de la Administración del Estado."
          - Fnd: "Art-3. Reitera principios de responsabilidad, eficiencia, probidad y transparencia."
          - Fnd: "Art-52-53. Define probidad administrativa como conducta intachable y desempeño honesto y leal; la rendición es un mecanismo de verificación."

      - ID: STS-KB-GN-RENDICION-NORMA-LBPA-01
        Cpt: "Ley N°19.880 (LBPA)"
        Src: "@guia_rendiciones_gores.md"
        Ref:
          - GN-REN-GLOS-LBPA
        Elementos:
          - Cpt: "Ley de Bases de los Procedimientos Administrativos."
          - Fnd: "Art-5, 16bis, 18, 19. Consagran el principio de escrituración electrónica, el expediente electrónico y el uso de plataformas electrónicas; base para digitalización de rendiciones."

      - ID: STS-KB-GN-RENDICION-NORMA-LEYPPTOS-01
        Cpt: "Ley de Presupuestos del Sector Público (Anual)"
        Src: "@guia_rendiciones_gores.md, @kb_021_extractos_legales.md"
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART07"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART23"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART25"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26"
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-08"
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-12"
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-16"
        Elementos:
          - Nat: "Fuente normativa primordial de aplicación directa y anual."
          - Fnd: "Art-23-26 (Ley N°21.796, 2026). Marco estricto para transferencias a privados (concurso, convenio, rendición vía SISREC, garantías, prohibiciones). Obligatorio para el GORE."
          - Cpt: "Glosas Partida 31 (GORE) contienen instrucciones operativas cruciales."
          - Cpt: "Glosa-06. Regula oferta programática GORE (S.24 inversión), evaluación ex ante DIPRES/SES, tope 5% gastos administrativos."
          - Cpt: "Glosa-07. Regula 8% FNDR para subvenciones (cultura, deporte, etc.)."
          - Cpt: "Glosa-12. Regula FRIL."
          - Cpt: "Glosa-13. Regula FRPD."

      - ID: STS-KB-GN-RENDICION-NORMA-LEY21180-01
        Cpt: "Ley N°21.180 (Transformación Digital del Estado)"
        Src: "@guia_rendiciones_gores.md"
        Ref:
          - GN-REN-GLOS-LEY21180
        Elementos:
          - Purp: "Mandata la digitalización de procedimientos administrativos."
          - Res: "Consolida la obligación de tramitar rendiciones por medios electrónicos, usar expedientes electrónicos y firma electrónica."

      - ID: STS-KB-GN-RENDICION-NORMA-LEY21719-01
        Cpt: "Ley N°21.719 (Protección de Datos Personales)"
        Src: "@guia_rendiciones_gores.md, @kb_021_extractos_legales.md"
        Ref:
          - GN-REN-GLOS-LEY21719
        Elementos:
          - Purp: "Establece un marco robusto para el tratamiento de datos personales."
          - Req: "GORE debe tratar datos personales en expedientes y publicaciones de transparencia respetando licitud, finalidad, proporcionalidad y seguridad; especial cuidado con datos sensibles de beneficiarios."

      - ID: STS-KB-GN-RENDICION-NORMA-RES1858-01
        Cpt: "Resolución Exenta N°1.858 de 2023, CGR"
        Src: "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md"
        Ref:
          - GN-REN-GLOS-RES1858
        Elementos:
          - Purp: "Establece el uso obligatorio de SISREC."
          - Ctx: "Para servicios públicos, municipalidades y otros organismos que transfieren recursos de Subtítulos 24 y 33."
          - Req: "Obliga al GORE Ñuble y a sus entidades ejecutoras a utilizar SISREC según cronograma de implementación de CGR."

Parte_2_Actores_y_Responsabilidades:
  ID: STS-KB-GN-RENDICION-ACTORES-01
  Purp: "Definir los roles y responsabilidades de cada actor involucrado en el ciclo de rendición de cuentas del GORE Ñuble."
  Src:
    - "@guia_rendiciones_gores.md"
    - "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md"

  Actores_Internos_GORE:
    ID: STS-KB-GN-RENDICION-ACTORES-INTERNOS-01
    Actores:
      - ID: STS-KB-GN-RENDICION-ACTOR-GOBERNADOR-01
        Cpt: "Gobernador/a Regional"
        Rol: "Máxima autoridad ejecutiva; responsable final de la correcta inversión de todos los fondos."
        Funciones:
          - Req: "Aprobar mediante resolución los convenios de transferencia."
          - Req: "Velar por el funcionamiento de un sistema de control interno adecuado para rendiciones."
          - Req: "Representar al GORE ante organismos de control externo."

      - ID: STS-KB-GN-RENDICION-ACTOR-CORE-01
        Cpt: "Consejo Regional (CORE)"
        Rol: "Órgano fiscalizador."
        Funciones:
          - Req: "Fiscalizar actos del GORE, incluyendo ejecución presupuestaria y uso de fondos."
          - Req: "Requerir informes sobre estado de rendiciones."
          - Req: "Considerar historial de rendiciones de ejecutores al aprobar nuevos fondos."

      - ID: STS-KB-GN-RENDICION-ACTOR-ADMREG-01
        Cpt: "Administrador/a Regional"
        Rol: "Coordinador de la gestión administrativa interna."
        Funciones:
          - Req: "Supervisar la eficiencia de los procesos de rendición."
          - Req: "Coordinar acción de divisiones involucradas (DAF, DIPIR, Unidades Técnicas)."

      - ID: STS-KB-GN-RENDICION-ACTOR-DAF-01
        Cpt: "División de Administración y Finanzas (DAF)"
        Rol: "Unidad central en la gestión financiera y administrativa de las rendiciones."
        Ref:
          - GN-REN-GLOS-DAF
        Funciones:
          - Req: "Elaborar convenios y resoluciones de pago."
          - Req: "Recepcionar, registrar y custodiar expedientes de rendición."
          - Req: "Realizar revisión financiera y de legalidad de gastos rendidos."
          - Req: "Contabilizar en SIGFE."
          - Req: "Gestionar SISREC como entidad otorgante (roles Administrador y Encargado Otorgante)."

      - ID: STS-KB-GN-RENDICION-ACTOR-UCR-01
        Cpt: "Unidad de Control de Rendiciones (U.C.R.)"
        Ctx: "Unidad especializada dentro de la DAF; buena práctica según manual de procedimientos."
        Ref:
          - GN-REN-GLOS-UCR
        Rol: "Centraliza y especializa el proceso de control de rendiciones."
        Funciones:
          - Req: "Registrar rendiciones en base de datos de programas."
          - Req: "Derivar a Referentes Técnicos para revisión."
          - Req: "Controlar antecedentes para contabilización."
          - Req: "Contabilizar en SIGFE."
          - Req: "Archivar expedientes."
          - Req: "Supervisar tiempos de revisión de los referentes."

      - ID: STS-KB-GN-RENDICION-ACTOR-DIVISIONES-01
        Cpt: "Divisiones Técnicas (DIPIR, DIDESOH, DIFOI, DIT)"
        Rol: "Albergan a los Referentes Técnicos y Financieros (RTF) de proyectos/programas."
        Funciones:
          - Req: "Definir aspectos técnicos en convenios."
          - Req: "Realizar seguimiento técnico de la ejecución."
          - Req: "Revisar coherencia de gastos rendidos con avance físico."
          - Req: "Emitir informes técnicos de aprobación/observación de rendiciones."

      - ID: STS-KB-GN-RENDICION-ACTOR-RTF-01
        Cpt: "Referente Técnico-Financiero (RTF)"
        Ref:
          - GN-REN-GLOS-RTF
        Rol: "Primera línea de revisión y seguimiento de un proyecto/programa."
        Funciones:
          - Req: "Supervisar cumplimiento del convenio."
          - Req: "Vigilar que la entidad ejecutora rinda mensualmente (o según plazo)."
          - Req: "Revisar detalladamente rendiciones (técnica y financiera)."
          - Req: "Solicitar subsanación de observaciones."
          - Req: "Aprobar técnicamente la rendición y derivar a DAF/U.C.R."
        Rol_SISREC:
          Def: "Corresponde al 'Analista Otorgante' en SISREC."
          Src: "@generalidades_sistema_rendicion_electronica_cuentas_sisrec.md"

      - ID: STS-KB-GN-RENDICION-ACTOR-CONTROLINTERNO-01
        Cpt: "Unidad de Control Interno del GORE"
        Rol: "Control preventivo y posterior de la legalidad."
        Funciones:
          - Req: "Auditar selectivamente procesos de transferencia y rendición."
          - Req: "Asesorar a divisiones en procedimientos de control."
          - Req: "Informar al Gobernador y al CORE sobre hallazgos y recomendaciones."

  Entidades_Ejecutoras:
    ID: STS-KB-GN-RENDICION-ACTORES-EJECUTORES-01
    Rol: "Receptoras de fondos GORE; principales responsables de la correcta ejecución y rendición."
    Deberes:
      - Req: "Usar fondos exclusivamente para fines convenidos."
      - Req: "Administrar con probidad, eficiencia y transparencia."
      - Req: "Llevar registros y documentación de respaldo completa y fidedigna."
      - Req: "Presentar rendiciones en forma y plazos establecidos (vía SISREC)."
      - Req: "Subsanar observaciones oportunamente."
      - Req: "Reintegrar fondos no utilizados o mal rendidos."
    Tipologias:
      - ID: STS-KB-GN-RENDICION-EJECUTOR-MUNI-01
        Cpt: "Municipalidades"
        Ctx: "Receptoras de FNDR, FRIL, 8% FNDR."
        Req:
          - "Obligadas a usar SISREC para rendir al GORE (Res. Ex. 1858/2023 CGR)."
      - ID: STS-KB-GN-RENDICION-EJECUTOR-SSPP-01
        Cpt: "Otros Servicios Públicos Sectoriales"
        Ctx: "SERVIU, Vialidad, etc."
        Req:
          - "Rinden al GORE según convenio."
          - "CGR examina inversión en sede del servicio ejecutor (Res. 30 CGR, Art. 26)."
      - ID: STS-KB-GN-RENDICION-EJECUTOR-PRIVADO-01
        Cpt: "Entidades Privadas (Corporaciones, Fundaciones, ONGs)"
        Ctx: "Receptoras de 8% FNDR, FRPD, etc."
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART23"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26"
        Req:
          - "Sujetos a marco regulatorio estricto (Ley Presupuestos 2026, Art. 23-26)."
          - "Inscripción en Registro de Colaboradores del Estado (Ley 19.862)."
          - "Obligadas a usar SISREC para rendir al GORE."

  Organismos_Control_Externo:
    ID: STS-KB-GN-RENDICION-ACTORES-EXTERNOS-01
    Organismos:
      - ID: STS-KB-GN-RENDICION-EXTERNO-CGR-01
        Cpt: "Contraloría General de la República (CGR)"
        Ref:
          - GN-REN-GLOS-RES30
        Rol: "Principal órgano de control externo."
        Funciones:
          - Req: "Ejercer control de legalidad de actos GORE (Toma de Razón)."
          - Req: "Fiscalizar ingreso e inversión de fondos GORE."
          - Req: "Examinar y juzgar cuentas rendidas."
          - Req: "Realizar auditorías financieras y de cumplimiento."
          - Req: "Formular reparos e iniciar Juicios de Cuentas."
          - Req: "Administrar y establecer uso obligatorio de SISREC."
      - ID: STS-KB-GN-RENDICION-EXTERNO-DIPRES-01
        Cpt: "Dirección de Presupuestos (DIPRES)"
        Rol: "Control y seguimiento de ejecución presupuestaria y programática."
        Funciones:
          - Req: "Monitorear ejecución presupuestaria GORE vía SIGFE."
          - Req: "Evaluar programas públicos regionales (ex ante, durante, ex post)."
          - Req: "Velar por cumplimiento de glosas presupuestarias."

Parte_3_Proceso_Operativo_Rendicion:
  ID: STS-KB-GN-RENDICION-PROCESO-01
  Purp: "Describir la documentación requerida y los flujos de trabajo para la gestión de rendiciones en el GORE Ñuble, distinguiendo la modalidad legado de la modalidad estándar vía SISREC."

  Documentacion_y_Expediente:
    ID: STS-KB-GN-RENDICION-PROCESO-EXPEDIENTE-01

    Componentes_Esenciales:
      ID: STS-KB-GN-RENDICION-PROCESO-EXPEDIENTE-COMPONENTES-01
      Src: "@resolucion_30_2015_cgr_rendicion_cuentas.txt (Art. 2)"
      Elementos:
        - Cpt: "Informe de Rendición de Cuentas"
          Def: "Documento formal de la entidad ejecutora que resume la gestión; en SISREC corresponde al informe electrónico firmado con FEA."
        - Cpt: "Comprobantes de Ingresos"
          Def: "Documentación que acredita recepción de fondos."
        - Cpt: "Comprobantes de Egresos"
          Def: "Documentación auténtica que respalda cada desembolso."
          Ref:
            - STS-KB-GN-RENDICION-PROCESO-EXPEDIENTE-DOCS-01
        - Cpt: "Comprobantes de Traspasos"
          Def: "Documentos de operaciones contables sin movimiento de efectivo."
        - Cpt: "Registro Ley N°19.862"
          Ctx: "Cuando corresponda (transferencias a privados)."
        - Cpt: "Medios de Verificación"
          Def: "Evidencia de cumplimiento de objetivos (informes técnicos, fotos, listas, etc.)."

    Documentacion_Autentica_y_Respaldo:
      ID: STS-KB-GN-RENDICION-PROCESO-EXPEDIENTE-DOCS-01
      Src: "@resolucion_30_2015_cgr_rendicion_cuentas.txt (Art. 4, 5)"
      Elementos:
        - Cpt: "Soporte Papel"
          Def: "Documento original; copias sólo si son autentificadas por ministro de fe o funcionario autorizado."
        - Cpt: "Soporte Electrónico"
          Def: "Documento electrónico según Ley 19.799, con firma electrónica."
        - Cpt: "Documento Digitalizado"
          Def: "Se considera copia simple, salvo que sea autentificado con firma electrónica; en SISREC el Ministro de Fe del ejecutor cumple esta función."
        - Cpt: "Tipos Comunes"
          Def: "Facturas y boletas electrónicas, contratos, liquidaciones de sueldo, comprobantes de cotizaciones, comprobantes de transferencia bancaria, actas de recepción, etc."

  Flujo_Sin_SISREC_Modalidad_Legado:
    ID: STS-KB-GN-RENDICION-PROCESO-SIN-SISREC-01
    Ctx: "Aplicable a convenios antiguos no migrados a SISREC."
    Src: "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md (Sec. 7.1)"
    Pasos:
      - Step: 1
        Resp: "Entidad Ejecutora (EE)"
        Act: "Prepara y presenta rendición en papel/digital a Oficina de Partes (OP) del GORE."
        Dln: "15 días hábiles del mes siguiente."
      - Step: 2
        Resp: "Oficina de Partes (OP)"
        Act: "Recepciona, registra y deriva a U.C.R./DAF."
        Dln: "2 días hábiles (GORE)."
      - Step: 3
        Resp: "U.C.R./DAF"
        Act: "Registra en base de datos interna y deriva a RTF."
        Dln: "2 días hábiles (GORE)."
      - Step: 4
        Resp: "RTF"
        Act: "Revisa técnica y financieramente la rendición."
        Dln: "7 días hábiles (GORE)."
        Condiciones:
          - Cond: "Si OK"
            Res: "Emite certificado de aprobación y devuelve a U.C.R./DAF."
          - Cond: "Si Observa"
            Res: "Comunica a EE para subsanación; plazo 2 días hábiles (GORE) para comunicar. EE reingresa correcciones."
      - Step: 5
        Resp: "U.C.R./DAF"
        Act: "Recibe rendición aprobada por RTF, realiza control final mediante checklist."
        Dln: "4 días hábiles (GORE)."
      - Step: 6
        Resp: "U.C.R./DAF"
        Act: "Contabiliza en SIGFE."
        Dln: "2 días hábiles (GORE)."
      - Step: 7
        Resp: "U.C.R./DAF"
        Act: "Archiva expediente."
        Dln: "1 día hábil (GORE)."

  Flujo_Con_SISREC_Modalidad_Estandar:
    ID: STS-KB-GN-RENDICION-PROCESO-CON-SISREC-01
    Ctx: "Procedimiento obligatorio para nuevas transferencias S.24 y S.33."
    XRef_Required:
      - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART07"
    Src:
      - "@generalidades_sistema_rendicion_electronica_cuentas_sisrec.md"
      - "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md (Sec. 7.2)"
    Ref:
      - GN-REN-GLOS-SISREC
      - GN-REN-GLOS-SIGFE
      - GN-REN-GLOS-ENT-EJEC

    Flujo_Entidad_Otorgante_GORE:
      ID: STS-KB-GN-RENDICION-SISREC-GORE-01
      Pasos:
        - Step: 1
          Resp: "Analista Otorgante (RTF)"
          Activities:
            - "Crea Programa/Proyecto en SISREC."
            - "Registra y envía transferencia a Ejecutor."
            - "Recibe y revisa rendición del Ejecutor (Dln: 7 días hábiles GORE)."
            - "Aprueba/Observa cada transacción."
            - "Envía a Encargado Otorgante para firma."
        - Step: 2
          Resp: "Encargado Otorgante (Jefe DAF)"
          Activities:
            - "Recibe rendición del Analista."
            - "Revisa propuesta."
          Condiciones:
            - Cond: "Si Observa"
              Res: "Devuelve rendición al Ejecutor con FEA (Dln: 1 día hábil GORE para devolver)."
            - Cond: "Si Aprueba"
              Res: "Firma Informe de Aprobación (total/parcial) con FEA."
        - Step: 3
          Resp: "Analista Otorgante (RTF)"
          Activities:
            - "Descarga Informe de Aprobación firmado."
            - "Deriva a U.C.R./DAF para contabilización."
        - Step: 4
          Resp: "U.C.R./DAF"
          Activities:
            - "Recibe informe."
            - "Contabiliza en SIGFE (Dln: 2 días hábiles GORE)."
            - "Archiva registro (Dln: 2 días hábiles GORE)."

    Flujo_Entidad_Ejecutora:
      ID: STS-KB-GN-RENDICION-SISREC-EJECUTOR-01
      Pasos:
        - Step: 1
          Resp: "Analista Ejecutor"
          Activities:
            - "Recibe y acepta transferencia del GORE en SISREC."
            - "Crea informe de rendición (mensual, regularización, sin movimiento) con Dln: 15 días hábiles mes siguiente."
            - "Ingresa transacciones y adjunta documentos de respaldo digitalizados."
            - "Envía a Ministro de Fe."
        - Step: 2
          Resp: "Ministro de Fe del Ejecutor"
          Activities:
            - "Revisa autenticidad de documentos."
          Condiciones:
            - Cond: "Si OK"
              Res: "Aprueba/certifica y pasa a Encargado Ejecutor."
            - Cond: "Si Observa"
              Res: "Devuelve a Analista Ejecutor."
        - Step: 3
          Resp: "Encargado Ejecutor"
          Activities:
            - "Revisa rendición."
          Condiciones:
            - Cond: "Si OK"
              Res: "Firma Informe de Rendición con FEA y envía al GORE."
            - Cond: "Si Observa"
              Res: "Devuelve a Analista Ejecutor."
        - Step: 4
          Resp: "Analista Ejecutor (si hay devolución del GORE)"
          Activities:
            - "Recibe rendición observada."
            - "Crea informe de 'Regularización'."
            - "Corrige transacciones observadas y reenvía por el mismo flujo."

Parte_4_Rendicion_por_Tipologia_de_Fondos:
  ID: STS-KB-GN-RENDICION-FONDOS-01
  Purp: "Detallar las particularidades de la rendición de cuentas para los principales fondos y programas gestionados por el GORE Ñuble."
  Src:
    - "@guia_rendiciones_gores.md"
    - "kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"
    - "kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml"

  Fondos_Principales:
    - ID: STS-KB-GN-RENDICION-FONDOS-FNDR-01
      Cpt: "Fondo Nacional de Desarrollo Regional (FNDR)"
      Ref:
        - GN-REN-GLOS-FNDR
        - GN-REN-GLOS-FRIL
        - GN-REN-GLOS-FRPD
      Subtipos:
        - ID: STS-KB-GN-RENDICION-FNDR-S31-01
          Cpt: "Iniciativas de Inversión (Subtítulo 31 - Ejecución Directa GORE)"
          Ctx:
            - "Obras, adquisición de activos, estudios de preinversión ejecutados directamente por el GORE."
            - "@kb_024_guia_idi_sni.md"
          Ref:
            - GN-REN-GLOS-FNDR
            - GN-REN-GLOS-SIGFE
          Elementos:
            - Cpt: "Rendición"
              Def: "Rendición interna de gastos y cumplimiento de etapas."
            - Cpt: "Respaldo Clave"
              Ex: "Contratos, estados de pago visados por ITO, facturas, resoluciones de adjudicación, boletas de garantía."
            - Cpt: "Sistema"
              Req: "Gastos se imputan al código BIP en SIGFE; se actualiza avance físico-financiero en BIP."
            - Cpt: "Contabilización"
              Proc: "DAF verifica disponibilidad y correcta imputación en S.31."
            - Cpt: "Cierre"
              Req: "Completar Carpeta Digital Ex Post en BIP al finalizar el proyecto."

        - ID: STS-KB-GN-RENDICION-FNDR-S33-01
          Cpt: "Transferencias de Capital (Subtítulo 33 - Ejecución por Terceros)"
          Ctx:
            - "Modalidad más común; GORE transfiere a Municipalidades, Servicios Públicos o privados."
            - "@kb_024_guia_idi_sni.md"
          Ref:
            - GN-REN-GLOS-FNDR
            - GN-REN-GLOS-SISREC
            - GN-REN-GLOS-ENT-EJEC
          Elementos:
            - Fnd: "Convenio de Transferencia detalla proyecto, monto, plazos y obligaciones."
            - Cpt: "Rendición Ejecutor"
              Req: "Obligatoria vía SISREC, con informe, comprobantes de gasto, informes de avance y actas de recepción."
            - Cpt: "Revisión GORE"
              Proc: "RTF revisa coherencia técnica-financiera; DAF/U.C.R. revisan legalidad y documentación."

        - ID: STS-KB-GN-RENDICION-FONDOS-FRIL-01
          Cpt: "Fondo Regional de Iniciativa Local (FRIL)"
          XRef_Required:
            - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-12"
          Ctx:
            - "Asignación FNDR para proyectos de inversión de pequeña escala municipal."
            - "@kb_026_guia_fril.md"
          Ref:
            - GN-REN-GLOS-FNDR
            - GN-REN-GLOS-FRIL
            - GN-REN-GLOS-SISREC
          Elementos:
            - Cpt: "Informe favorable MDSF"
              Req: "Proyectos FRIL deben contar con informe favorable del Ministerio de Desarrollo Social y Familia, salvo excepción bajo 5000 UTM."
            - Cpt: "Excepción <5000 UTM"
              Req: "Los proyectos cuyo costo total por proyecto sea inferior a 5000 UTM, valorizadas al 1 de enero del ejercicio presupuestario vigente, no requerirán informe favorable del MDSF. Sin perjuicio de lo anterior, deberá ser ingresada al Sistema Nacional de Inversiones la información necesaria, según lo dispuesto en el Oficio Ordinario N°2 del 26 de enero de 2024, e instructivo asociado, del Ministerio de Hacienda y del Ministerio de Desarrollo Social y Familia."
            - Prohib: "Financiar proyectos por etapas o fraccionados."
            - Cpt: "Rendición"
              Proc: "Municipalidades rinden al GORE vía SISREC, acreditando gastos y avance de obras."
            - Cpt: "Supervisión GORE"
              Proc: "Verifica cumplimiento de guía operativa y aplicación correcta de los requisitos MDSF/excepción <5000 UTM y del registro en SNI."

        - ID: STS-KB-GN-RENDICION-FONDOS-FRPD-01
          Cpt: "Fondo Regional para la Productividad y el Desarrollo (FRPD)"
          Ctx:
            - "Fondos de Royalty Minero para innovación, competitividad y CTI."
            - "@kb_027_guia_frpd.md"
          Ref:
            - GN-REN-GLOS-FRPD
            - GN-REN-GLOS-SISREC
          Elementos:
            - Resp: "Universidades, centros de investigación, corporaciones, empresas."
            - Cpt: "Rendición"
              Req: "Vía SISREC, acreditando gasto financiero y logro de hitos, productos y resultados de I+D+i."
            - Cpt: "Supervisión GORE"
              Proc: "DIFOI y DIPIR siguen cumplimiento de metas."

        - ID: STS-KB-GN-RENDICION-FONDOS-SUBV8-01
          Cpt: "Subvenciones de Vinculación con la Comunidad (8% FNDR)"
          Ctx:
            - "@kb_028_guia_subv8.md"
          Ref:
            - GN-REN-GLOS-SUBV8
            - GN-REN-GLOS-FNDR
            - GN-REN-GLOS-SISREC
          Elementos:
            - Ctx: "Fondos concursables para cultura, deporte, seguridad, medio ambiente, destinados a municipalidades y entidades privadas sin fines de lucro."
            - Fnd: "Glosa 07 Ley de Presupuestos, bases del concurso, instructivo regional."
            - Cpt: "Rendición"
              Req: "Vía SISREC, con énfasis en coherencia del gasto con el proyecto adjudicado."
            - Cpt: "Respaldo Clave"
              Ex: "Boletas de honorarios con cotizaciones, facturas específicas de la actividad."
            - Cpt: "Medios de Verificación"
              Req: "Listas de asistencia, fotos, material de difusión."
            - Cpt: "Restricciones"
              Req: "Bases definen gastos prohibidos (operativos, premios en dinero, alcohol, etc.) que deben fiscalizarse."

        - ID: STS-KB-GN-RENDICION-FONDOS-PROG-GLOSA06-01
          Cpt: "Programas FNDR (Subtítulo 24 Inversión - Ejecución Directa GORE)"
          Ctx:
            - "@kb_gn_025_guia_programas.md"
          Ref:
            - GN-REN-GLOS-FNDR
            - GN-REN-GLOS-DAF
          Elementos:
            - Ctx: "Programas ejecutados directamente por el GORE."
            - Fnd: "Glosa 06 Ley de Presupuestos, evaluación ex ante DIPRES/SES."
            - Cpt: "Gasto Administrativo"
              Req: "Hasta 5% del programa puede destinarse a gastos de administración del GORE, imputados al presupuesto del programa."
            - Cpt: "Rendición Interna"
              Proc: "DAF controla tope del 5% y correcta imputación."
            - Cpt: "Rendición Externa"
              Proc: "Se rinde cumplimiento de componentes y metas, coherente con diseño aprobado ex ante."

        - ID: STS-KB-GN-RENDICION-FONDOS-C33-01
          Cpt: "Conservación de Infraestructura (Circular 33)"
          Ctx:
            - "@kb_gn_029_guia_circ33.md"
          Elementos:
            - Ctx: "Iniciativas de mantención/reparación de infraestructura que no afectan capacidad original."
            - Fnd: "Oficio Circular N°33/2009 MINHAC, NIP 2025."
            - Proc: "Uso del BIP para obtener RATE 'AD (Admisible para Financiamiento)' del MDSF."
            - Prohib: "Costo de reparación > 30% del costo de reposición del activo (si ocurre, debe ir a SNI estándar)."
            - Cpt: "Rendición"
              Proc: "Sigue flujo estándar de proyecto de inversión, acreditando partidas de conservación."

Parte_5_Control_Fiscalizacion_y_Transparencia:
  ID: STS-KB-GN-RENDICION-CONTROL-01
  Purp: "Describir mecanismos de control, rol de la fiscalización externa y obligaciones de transparencia asociadas a las rendiciones."
  Src: "@guia_rendiciones_gores.md"

  Control_Interno_GORE:
    ID: STS-KB-GN-RENDICION-CONTROL-INTERNO-01
    Mecanismos:
      - Purp: "Asegurar la correcta administración y rendición desde dentro de la institución."
      - Mech: "Unidad de Control Interno"
        Proc: "Realiza revisión preventiva y auditorías selectivas sobre el proceso de rendición; informa al Gobernador y al CORE."
      - Mech: "Listas de Chequeo"
        Proc: "Aplicación de checklists estandarizadas para revisión formal, documental, financiera y técnica de cada rendición."
        Src: "Anexo 10.3 del manual de procedimientos."
      - Mech: "Seguimiento Físico-Financiero"
        Proc: "Verificar que el gasto se traduzca en avances concretos; requiere análisis integrado de informes y visitas a terreno por parte de los RTF."

  Fiscalizacion_Externa:
    ID: STS-KB-GN-RENDICION-CONTROL-EXTERNO-01
    Elementos:
      - Purp: "Control ejercido por organismos externos al GORE."
      - Resp: "Contraloría General de la República (CGR)"
        Act:
          - "Examen y juzgamiento de cuentas para verificar legalidad, fidelidad y exactitud de rendiciones."
          - "Auditorías financieras y de cumplimiento al GORE."
          - "Formulación de observaciones y reparos."
          - "Juicios de Cuentas para responsabilidades pecuniarias."
      - Resp: "Dirección de Presupuestos (DIPRES)"
        Act:
          - "Monitoreo de ejecución presupuestaria y programática del GORE."
          - "Evaluación de programas regionales para medir eficacia."

  Transparencia_y_Acceso_a_Informacion:
    ID: STS-KB-GN-RENDICION-CONTROL-TRANSPARENCIA-01
    Src: "Ley N°20.285 (Transparencia)"
    Elementos:
      - Purp: "Deber del GORE de transparentar el uso de fondos públicos."
      - Req: "Transparencia Activa"
        Cpt: "Publicación proactiva y mensual de convenios de transferencia, detalle de transferencias, nóminas de beneficiarios, presupuesto y ejecución, resultados de auditorías."
      - Req: "Transparencia Pasiva"
        Cpt: "Respuesta a solicitudes de acceso a la información dentro de plazos legales, resguardando datos personales sensibles."
    Obligaciones_Presupuesto_2026_Partida_31:
      ID: STS-KB-GN-RENDICION-TRANSP-PPTO-2026-P31-01
      XRef_Required:
        - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-08"
        - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-16"
      Corporaciones_y_Fundaciones:
        ID: STS-KB-GN-RENDICION-TRANSP-PPTO-2026-P31-GLO08-01
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-08"
        Req:
          - "Informar a DIPRES y publicar en las páginas web de la corporación y del Gobierno Regional información institucional (misión, objetivos, directorio, financiamiento, planificación anual) a más tardar al término del primer trimestre."
          - "Informar y publicar trimestralmente, dentro de los 30 días siguientes al término de cada trimestre, información de ejecución y gestión (dotación, remuneraciones, concursos, recursos transferidos/ejecutados, indicadores)."
          - "Exigir cuenta pública anual, estados financieros publicados y cumplimiento de Ley N°20.285 cuando corresponda."
      Requerimientos_Informacion_y_Publicacion:
        ID: STS-KB-GN-RENDICION-TRANSP-PPTO-2026-P31-GLO16-01
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-16"
        Req:
          - "Publicar mensualmente la cartera de proyectos financiada con cargo a presupuestos de inversión regional y publicar acuerdos CORE dentro de 5 días hábiles desde su adopción."
          - "Informar trimestralmente el uso de recursos (beneficiarios, comuna, instituciones receptoras, montos, productos del convenio y su aplicación regional) a las instancias definidas en la glosa, y publicar la información en los mismos plazos cuando corresponda."
          - "Publicar trimestralmente e informar a senadores y diputados de la región los proyectos adjudicados/contratados con cargo a Subtítulos 24, 31 y 33, incluyendo identificación de proyecto, montos, postulantes, pauta de evaluación, seleccionado, presupuesto aprobado y votaciones CORE."

Parte_6_Responsabilidades_y_Sanciones:
  ID: STS-KB-GN-RENDICION-RESPONSABILIDAD-01
  Purp: "Detallar el régimen de responsabilidades y las posibles sanciones derivadas de irregularidades en el proceso de rendición."
  Src:
    - "@guia_rendiciones_gores.md"
    - "@kb_021_extractos_legales.md"

  Tipos_Responsabilidad:
    - Cpt: "Responsabilidad Administrativa"
      Cause: "Infracción a deberes de cuidado, supervisión o probidad por parte de funcionarios del GORE."
      Proc: "Sumario administrativo."
      Src: "Estatuto Administrativo, Art. 119."
      Res: "Censura, multa, suspensión o destitución (Ley 18.834)."
    - Cpt: "Responsabilidad Civil"
      Cause: "Perjuicio patrimonial al Fisco por acción negligente o dolosa."
      Proc: "Juicio de Cuentas ante CGR o demanda civil ante tribunales."
      Res: "Orden de restituir los fondos."
    - Cpt: "Responsabilidad Penal"
      Cause: "Hechos constitutivos de delito (malversación, fraude al fisco, cohecho, etc.)."
      Proc: "Investigación del Ministerio Público y juicio penal."
      Res: "Multas, inhabilitación, penas privativas de libertad."

  Consecuencias_Directas_por_Rendiciones_Pendientes_o_Observadas:
    - Cpt: "Obligación de Restituir Fondos"
      Cause: "Rendición no presentada, no aprobada u observada por CGR."
      Res: "Genera obligación de reintegro (Res. 30 CGR, Art. 31)."
    - Cpt: "Suspensión de Nuevas Transferencias"
      Cause: "Existencia de rendiciones exigibles pendientes."
      Res: "GORE no debe entregar nuevos fondos (Res. 30 CGR, Art. 18)."

Parte_7_Gestion_Estrategica_y_Contingencias:
  ID: STS-KB-GN-RENDICION-GESTION-01
  Purp: "Ofrecer recomendaciones para una gestión de excelencia y planes para contingencias operativas."
  Src:
    - "@guia_rendiciones_gores.md"
    - "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md"

  Buenas_Practicas:
    ID: STS-KB-GN-RENDICION-GESTION-BPR-01
    Ref:
      - GN-REN-GLOS-DAF
      - GN-REN-GLOS-ENT-EJEC
      - GN-REN-GLOS-SISREC
      - GN-REN-GLOS-SIGFE
    Recomendaciones:
      - Rec: "Planificación anual de rendiciones y programación de revisiones internas."
      - Rec: "Coordinación interdivisional entre DAF, DIPIR y unidades técnicas con roles claros."
      - Rec: "Capacitación continua a funcionarios del GORE y entidades ejecutoras, especialmente en uso de SISREC."
      - Rec: "Uso óptimo de tecnología (SIGFE, BIP, SISREC)."
      - Rec: "Desarrollo y actualización de manuales internos de procedimientos."
      - Rec: "Gestión de riesgos (fraude, errores, demoras) con medidas preventivas y de control."
      - Rec: "Fomento de cultura de probidad y transparencia."
      - Rec: "Enfoque en resultados, articulando rendición financiera con medición de impacto."

  Contingencias_y_Planes_Accion:
    ID: STS-KB-GN-RENDICION-GESTION-CONTINGENCIAS-01
    Src: "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md (Sec. 7.3)"
    Casos:
      - Cpt: "Pérdida de Rendición al Interior del GORE"
        Proc: "Mantener registros digitales o libros de correspondencia en cada unidad (OP, U.C.R., RTF) para trazabilidad; como último recurso, solicitar copia a entidad ejecutora; SISREC minimiza este riesgo."
      - Cpt: "Entidad Privada solicita cuota siguiente sin haber rendido la anterior"
        Proc: "Aplicar Art. 18 Res. 30 CGR; si convenio lo permite, autorizar adelanto solo contra garantía (vale vista, póliza) por monto no rendido, fijando plazo perentorio para rendir o ejecutar garantía."
      - Cpt: "Demoras en revisión interna por alta carga de trabajo"
        Proc: "Usar planificación anual para anticipar peaks, reasignar revisores y priorizar rendiciones que habilitan transferencias críticas."

Parte_8_Procedimientos_Contables_Clave:
  ID: STS-KB-GN-RENDICION-CONTABILIDAD-01
  Purp: "Detallar los procedimientos contables en SIGFE para registrar transferencias y rendiciones vinculadas a transferencias condicionadas."
  Src: "@manual_procedimientos_rendicion_cuentas_st24_st33_gore_ñuble.md (Sec. 8)"
  Ref:
    - GN-REN-GLOS-SIGFE
    - GN-REN-GLOS-FNDR
    - GN-REN-GLOS-FRIL
    - GN-REN-GLOS-FRPD
    - GN-REN-GLOS-SUBV8
    - GN-REN-GLOS-ENT-EJEC
    - GN-REN-GLOS-DAF
  Warn: "Los números de cuenta corresponden al Plan de Cuentas del Sector Público."

  F07_Transferencias_Condicionadas_Sector_Privado:
    ID: STS-KB-GN-RENDICION-CONTABILIDAD-F07-01
    Ctx: "Aplicación en Subvenciones 8% FNDR y programas con ONGs."
    Ref:
      - GN-REN-GLOS-SUBV8
      - GN-REN-GLOS-SIGFE
      - GN-REN-GLOS-ENT-EJEC
    Fases:
      - Cpt: "Fase 1 - Entrega de Fondos"
        Proc:
          - "Devengo de obligación: Debe 12106 Deudores por Transferencias Reintegrables / Haber 21524 Cuentas por Pagar - Transf. Corrientes o 21533 Cuentas por Pagar - Transf. de Capital."
          - "Pago: Debe 21524/21533 / Haber 11102/11103 Banco."
      - Cpt: "Fase 2 - Aprobación Rendición"
        Proc:
          - "Reconocimiento del gasto: Debe 54101 Transf. Corr. Sector Privado o 54201 Transf. Cap. Sector Privado / Haber 12106 Deudores por Transferencias Reintegrables."
      - Cpt: "Fase 3 - Reintegro"
        Proc:
          - "Devengo del cobro: Debe 11508 Cuentas por Cobrar / Haber 12106 Deudores por Transferencias Reintegrables."
          - "Recepción del pago: Debe 11102/11103 Banco / Haber 11508 Cuentas por Cobrar."

  F08_Transferencias_Condicionadas_Sector_Publico:
    ID: STS-KB-GN-RENDICION-CONTABILIDAD-F08-01
    Ctx: "Aplicación en FNDR a Municipalidades (FRIL, proyectos) y transferencias a otros Servicios Públicos."
    Warn: "Para transferencias a otros Servicios Públicos (no Municipalidades), el devengo del gasto se realiza al aprobar la rendición; para Municipalidades, al momento de la transferencia."
    Ref:
      - GN-REN-GLOS-FNDR
      - GN-REN-GLOS-FRIL
      - GN-REN-GLOS-SIGFE
      - GN-REN-GLOS-ENT-EJEC
    Fases:
      - Cpt: "Fase 1 - Entrega de Fondos"
        Proc:
          - "Devengo de obligación: Debe 12106 Deudores por Transferencias Reintegrables / Haber 21524/21533."
          - "Pago: Debe 21524/21533 / Haber 11102/11103 Banco."
      - Cpt: "Fase 2 - Aprobación Rendición"
        Proc:
          - "Reconocimiento del gasto: Debe 54103 Transf. Corr. Otras Ent. Públicas o 54203 Transf. Cap. Otras Ent. Públicas / Haber 12106 Deudores por Transferencias Reintegrables."
      - Cpt: "Fase 3 - Reintegro"
        Proc:
          - "Devengo del cobro: Debe 11508 Cuentas por Cobrar / Haber 12106 Deudores por Transferencias Reintegrables."
          - "Recepción del pago: Debe 11102/11103 Banco / Haber 11508 Cuentas por Cobrar."
