---
urn: urn:gn:kb:gestion-ipr
nombre: gestion-ipr
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre gestion ipr; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_019_gestion_ipr_koda.yml (sha256:9f286370f39b5bc386341160c67b150cf50bbacb75bdb0a6ec1caddadfac43f9); URN KODA legado urn:gorenuble:gn:gestion-ipr:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-27
lang: es
tags: [gn, gore-os, koda, gestion, ipr]
familia: bok
---
# Artefacto KODA/Spec – Gestión Operacional de Intervenciones Públicas Regionales (IPR)
# Fuente: kb_gn_019_gestion_ipr.md

_manifest:
  urn: "urn:gorenuble:gn:gestion-ipr:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_019_gestion_ipr_koda.yml"
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
    last_modified_at: "2025-12-15"
    signature: null

ID: GN-IPR-GESTION-OPERACIONAL-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
Creation-Date: 2025-11-27
Modification-Date: 2025-12-15
Ctx: "Guía operacional completa para la gestión de Intervenciones Públicas Regionales (IPR) en el GORE Ñuble, desde el ingreso hasta el cierre y evaluación ex-post."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx: or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_IPR_Gestion:
  ID: GN-IPR-GLOSARIO-01
  Purp: "Definir conceptos y siglas operativas recurrentes en la gestión de IPR."
  Terminos:
    - ID: GN-IPR-GLOS-IPR
      Sigla: "IPR"
      Nombre: "Intervención Pública Regional"
      Def: "Término paraguas para cualquier acción (proyecto, programa, estudio) financiada por el GORE para objetivos de desarrollo."
    - ID: GN-IPR-GLOS-IDI
      Sigla: "IDI"
      Nombre: "Iniciativa de Inversión"
      Def: "Tipo de IPR asociada a proyectos de capital (obras, activos)."
    - ID: GN-IPR-GLOS-PPR
      Sigla: "PPR"
      Nombre: "Programa Público Regional"
      Def: "Tipo de IPR de gasto corriente o mixto (servicios, subvenciones)."
    - ID: GN-IPR-GLOS-POSTULACION
      Sigla: "Postulación"
      Nombre: "Postulación de IPR"
      Def: "IPR presentada para evaluación, antes de clasificación o aprobación."
    - ID: GN-IPR-GLOS-RS
      Sigla: "RS"
      Nombre: "Recomendación Satisfactoria"
      Def: "Resultado favorable de evaluación SNI/MDSF para IDI de mayor envergadura."
    - ID: GN-IPR-GLOS-RF
      Sigla: "RF"
      Nombre: "Recomendación Favorable"
      Def: "Resultado favorable de evaluación de programas en Glosa 06 u otros mecanismos."
    - ID: GN-IPR-GLOS-AD
      Sigla: "AD"
      Nombre: "Admisible para financiamiento (Conservación)"
      Def: "Resultado favorable de evaluación MDSF para proyectos de conservación; habilita financiamiento sin ser RS."
    - ID: GN-IPR-GLOS-CDP
      Sigla: "CDP"
      Nombre: "Certificado de Disponibilidad Presupuestaria"
      Def: "Documento del Depto. Presupuesto que acredita fondos para financiar una IPR."
    - ID: GN-IPR-GLOS-BIP
      Sigla: "BIP"
      Nombre: "Banco Integrado de Proyectos"
      Def: "Sistema para registro y seguimiento de IDI."
    - ID: GN-IPR-GLOS-SIGFE
      Sigla: "SIGFE"
      Nombre: "Sistema de Información para la Gestión Financiera del Estado"
      Def: "Sistema contable-financiero donde se registra ejecución presupuestaria."
    - ID: GN-IPR-GLOS-SISREC
      Sigla: "SISREC"
      Nombre: "Sistema de Rendición Electrónica de Cuentas"
      Def: "Plataforma de la Contraloría General de la República para rendiciones de cuentas de transferencias."
    - ID: GN-IPR-GLOS-DIPIR
      Sigla: "DIPIR"
      Nombre: "División de Presupuesto e Inversión Regional"
      Def: "División GORE responsable de presupuesto de inversión y gestión de IPR."
    - ID: GN-IPR-GLOS-DIPLADE
      Sigla: "DIPLADE"
      Nombre: "División de Planificación y Desarrollo Regional"
      Def: "División que lidera planificación y presidencia del Comité Directivo Regional."
    - ID: GN-IPR-GLOS-CORE
      Sigla: "CORE"
      Nombre: "Consejo Regional"
      Def: "Órgano colegiado que aprueba o rechaza financiamiento de IPR según normativa y acuerdos regionales."
    - ID: GN-IPR-GLOS-CDR
      Sigla: "CDR"
      Nombre: "Comité Directivo Regional"
      Def: "Instancia técnico-política interna para filtro de pertinencia estratégica de IPR."
    - ID: GN-IPR-GLOS-MDSF
      Sigla: "MDSF"
      Nombre: "Ministerio de Desarrollo Social y Familia"
      Def: "Organismo responsable de evaluación técnico-económica de IDI en el SNI."
    - ID: GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
      Nombre: "Estados de admisibilidad IPR"
      Def: "Categorías clave: PRE-ADMISIBLE CDR, NO PRE-ADMISIBLE CDR, ADMISIBLE, ADMISIBLE CON OBSERVACIONES, INADMISIBLE."
    - ID: GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
      Nombre: "Estados de financiamiento IPR"
      Def: "Categorías clave: PARA REVISIÓN TÉCNICA, EN CARTERA PRE-ADMISIBLE, ENVIADO A MDSF, APROBADO TÉCNICAMENTE (RS/RF/AD/Exento RS), CARTERA ENVIADA A CORE, CERTIFICADO CORE OK, ENVIADO A FINANCIAMIENTO, TRANSFERENCIA PROGRAMADA, CONVENIO FORMALIZADO."

Proceso_Gestion_Operacional_IPR:
  ID: GN-IPR-PROCESO-END-TO-END
  Purp: "Estandarizar el flujo completo de gestión de IPR en GORE Ñuble: desde el ingreso hasta el cierre."
  Ref:
    - GN-IPR-GLOS-IPR
    - GN-IPR-GLOS-IDI
    - GN-IPR-GLOS-PPR
  Res:
    - "Secuencia clara de fases, actores, decisiones y documentos clave."
    - "Trazabilidad normativa y documental de cada hito."
  Fnd:
    - "LOC GORE (Art. 16, 24, 36, 78)."
    - "DL N°1.263/1975 (Art. 19 bis)."
    - "Ley 20.530 (Crea MDSF)."
    - "Glosas 01, 06, 07 Ley de Presupuestos 2026 (Partida 31)."
    - "Normas Generales Ley de Presupuestos 2026 (Art. 23-26)."
    - "Res. 30/2015 CGR (Rendiciones)."
    - "Normativa DIPRES/MDSF sobre SNI, BIP, procedimientos especiales."
  Src:
    - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31"
    - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-NORMAS-GENERALES"

  Fases:
    - Ref: GN-IPR-FASE1-INGRESO
    - Ref: GN-IPR-FASE2-EVAL
    - Ref: GN-IPR-FASE3-FINANC
    - Ref: GN-IPR-FASE4-GESTION-PPT
    - Ref: GN-IPR-FASE5-EJECUCION
    - Ref: GN-IPR-FASE6-MODIFICACIONES
    - Ref: GN-IPR-FASE7-CIERRE

  Fase_1_Ingreso_Pertinencia_Admisibilidad:
    ID: GN-IPR-FASE1-INGRESO
    Purp: "Recepcionar, registrar y filtrar postulaciones de IPR para decidir cuáles avanzan a evaluación técnica."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-POSTULACION
    Res:
      - "Lista de IPR con registro formal y trazabilidad."
      - "Clasificación estratégica inicial y decisión de admisibilidad formal."
    Fnd:
      - "LOC GORE Art. 16 y 24."
    Secciones:
      - ID: GN-IPR-F1-RECEPCION-REGISTRO
        Titulo: "2.1 Recepción y Registro"
        Purp: "Formalizar ingreso de postulaciones y derivarlas a DIPIR."
        Ref:
          - GN-IPR-GLOS-POSTULACION
          - GN-IPR-GLOS-DIPIR
        Tabla_Pasos:
          - Step: 1
            Resp: "Unidad Formuladora (Externa)"
            Ref:
              - GN-IPR-GLOS-IPR
              - GN-IPR-GLOS-POSTULACION
            Activities:
              - "Preparar y presentar IPR según guías del mecanismo de financiamiento."
            Req:
              - "Ingresar oficio conductor firmado por máxima autoridad de la entidad postulante."
            Warn:
              - "La calidad de la formulación inicial es crítica para el resto del ciclo."
            Output: "Oficio y antecedentes completos presentados al GORE."
          - Step: 2
            Resp: "Oficina de Partes GORE"
            Activities:
              - "Recepcionar oficio y documentación física/digital."
              - "Asignar número de ingreso único en sistema de gestión documental (ej. SGDOC)."
              - "Derivar antecedentes completos a Jefatura DIPIR."
            Ref:
              - GN-IPR-GLOS-DIPIR
            Output: "Postulación registrada y derivada formalmente a DIPIR."
          - Step: 3
            Resp: "Jefatura DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-CDR
            Activities:
              - "Registrar datos básicos de la IPR en sistema de seguimiento interno."
              - "Poner la postulación a disposición del Comité Directivo Regional (CDR)."
            Output: "Postulación disponible para revisión del CDR."
      - ID: GN-IPR-F1-PERTINENCIA-CDR
        Titulo: "2.2 Análisis de Pertinencia Estratégica (Filtro Político-Técnico)"
        Purp: "Evaluar alineación de la IPR con prioridades estratégicas antes de invertir en evaluación técnica."
        Resp_Principal: "Comité Directivo Regional (CDR)."
        Ref:
          - GN-IPR-GLOS-CDR
          - GN-IPR-GLOS-DIPLADE
          - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
        Tabla_Pasos:
          - Step: 1
            Resp: "Jefatura DIPLADE"
            Ref:
              - GN-IPR-GLOS-DIPLADE
            Activities:
              - "Recibir listado de postulaciones ingresadas."
              - "Convocar a sesión del CDR como presidente de la instancia."
            Cpt: "Composición del CDR: Jefaturas de División, Jefatura de Rezago, Administrador/a Regional."
            Output: "CDR convocado con cartera de IPR a revisar."
          - Step: 2
            Resp: "CDR"
            Ref:
              - GN-IPR-GLOS-CDR
              - GN-IPR-GLOS-IPR
            Activities:
              - "Analizar cada IPR desde perspectiva técnico-política."
              - "Evaluar coherencia con ERD y prioridades estratégicas del GORE."
              - "Evaluar viabilidad preliminar y pertinencia."
              - "Generar acta de sesión con categorización y observaciones por IPR."
            Output:
              - "`PRE-ADMISIBLE CDR`"
              - "`NO PRE-ADMISIBLE CDR`"
          - Step: 3
            Resp: "Jefatura DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Recibir acta del CDR."
              - "Para IPR PRE-ADMISIBLES, evaluar marco presupuestario disponible y cartera de inversiones vigente."
              - "Priorizar IPR para revisión técnica según relevancia y factibilidad de financiamiento."
            Output:
              - "`PARA REVISIÓN TÉCNICA`"
              - "`EN CARTERA PRE-ADMISIBLE`"
      - ID: GN-IPR-F1-ADMISIBILIDAD-FORMAL
        Titulo: "2.3 Revisión de Admisibilidad Formal (Filtro Documental)"
        Purp: "Verificar requisitos formales y documentales exigidos por el mecanismo de financiamiento."
        Ctx: "Revisión realizada por analista asignado; resultado condiciona el paso a evaluación técnica."
        Ref:
          - GN-IPR-GLOS-DIPIR
          - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
        Tabla_Pasos:
          - Step: 1
            Resp: "Jefatura de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
            Activities:
              - "Recibir instrucción de Jefatura DIPIR para iniciar revisión."
              - "Asignar la IPR a analista competente según tipología."
              - "Formalizar apoyos interdivisionales si se requieren."
            Output: "IPR derivada formalmente a analista."
          - Step: 2
            Resp: "Analista de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
            Activities:
              - "Realizar revisión documental exhaustiva."
              - "Verificar cumplimiento de requisitos de la guía operativa del mecanismo."
              - "Comprobar correcta carga en Carpeta Digital del BIP cuando aplique."
            Output:
              - "`ADMISIBLE`"
              - "`ADMISIBLE CON OBSERVACIONES`"
              - "`INADMISIBLE`"
          - Step: 3
            Resp: "Unidad Formuladora (Externa)"
            Cond: "Solo si estado = ADMISIBLE CON OBSERVACIONES."
            Ref:
              - GN-IPR-GLOS-IPR
              - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
            Activities:
              - "Corregir antecedentes dentro del plazo definido por el GORE."
            Warn:
              - "No subsanar en plazo puede derivar en estado INADMISIBLE."
            Output: "Documentación subsanada."
          - Step: 4
            Resp: "Jefatura de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Si estado final es INADMISIBLE, elaborar y despachar oficio de inadmisibilidad."
              - "Si es ADMISIBLE o subsanada, declarar estado PARA EVALUACIÓN TÉCNICA."
            Output:
              - "`INADMISIBLE INFORMADO`"
              - "`LISTA PARA FASE 2`"

  Fase_2_Evaluacion_Tecnica_Economica:
    ID: GN-IPR-FASE2-EVAL
    Purp: "Analizar en profundidad la IPR para determinar calidad, viabilidad y conveniencia, aplicando principio de proporcionalidad."
    Fnd:
      - "Art. 19 bis DL N°1.263/1975."
      - "Ley 20.530 (Crea MDSF)."
    Warn:
      - "Proceso y criterios varían según nivel de proporcionalidad y mecanismo de financiamiento."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-IDI
      - GN-IPR-GLOS-PPR
      - GN-IPR-GLOS-MDSF
      - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
    Tracks:
      - ID: GN-IPR-F2-TRACK-A-SNI
        Titulo: "3.1 Track A – SNI (Análisis Estándar y Enriquecido, Nivel 2 y 3)"
        Purp: "Evaluar IDI de mayor envergadura que requieren RS de MDSF."
        Ref:
          - GN-IPR-GLOS-IDI
          - GN-IPR-GLOS-MDSF
          - GN-IPR-GLOS-RS
          - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
        Tabla_Pasos:
          - Step: 1
            Resp: "Analista GORE (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-IDI
              - GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD
            Activities:
              - "Revisión de fondo considerando antecedentes de Fase 1."
              - "Verificar cumplimiento de RIS y metodologías SNI aplicables."
              - "Asegurar calidad de estudios preinversionales (Perfil, Prefactibilidad, etc.)."
              - "Elaborar Acta de Admisibilidad interna GORE."
            Output:
              - "`ADMISIBLE PARA ENVÍO A MDSF`"
              - "`INADMISIBLE`"
          - Step: 2
            Resp: "Jefatura DIPIR / Gobernador/a"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-MDSF
            Activities:
              - "Elaborar y visar oficio solicitando evaluación ex ante al SEREMI MDSF."
              - "Gestionar cadena de V°B° interno y firma del Gobernador/a."
            Output: "Oficio despachado a MDSF."
          - Step: 3
            Resp: "Jefatura de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-BIP
              - GN-IPR-GLOS-MDSF
            Activities:
              - "Registrar formalmente la 'Informar Postulación' en el BIP."
            Output: "Iniciativa `ENVIADO A MDSF` en BIP."
          - Step: 4
            Resp: "Analista MDSF"
            Ref:
              - GN-IPR-GLOS-MDSF
              - GN-IPR-GLOS-RS
            Activities:
              - "Realizar evaluación de admisibilidad (plazo orientativo: 5 días)."
              - "Realizar análisis técnico-económico (ATE) (plazo orientativo: 10 días)."
            Output:
              - "RATE: `RS`, `FI`, u `OT`."
          - Step: 5
            Resp: "Unidad Formuladora / Analista GORE"
            Ref:
              - GN-IPR-GLOS-IPR
              - GN-IPR-GLOS-RS
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Si RS: registrar aprobación técnica y preparar paso a financiamiento."
              - "Si FI u OT: apoyar a la Unidad Formuladora en subsanar observaciones (plazo máx. 60 días hábiles)."
            Output:
              - "`APROBADO TÉCNICAMENTE (RS)`"
              - "`OBSERVACIONES SUBSANADAS`"
          - Step: 6
            Resp: "Jefatura de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-BIP
              - GN-IPR-GLOS-RS
            Activities:
              - "Monitorear BIP para obtener resultado de MDSF."
              - "Informar cartera con RS a Jefatura DIPIR para preparación de presentación al Gobernador/a."
            Output: "Cartera RS disponible para priorización."
      - ID: GN-IPR-F2-TRACK-B-PPR
        Titulo: "3.2 Track B – Programas Públicos Regionales (Glosa 06)"
        Purp: "Evaluar programas de gasto corriente/mixto ejecutados por el GORE según proceso bifásico DIPRES/SES."
        Ref:
          - GN-IPR-GLOS-PPR
          - GN-IPR-GLOS-RF
          - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
        Ctx:
          - "Programas en continuidad."
          - "Subvenciones 8% FNDR."
          - "Transferencias a entidades públicas."
          - "Ayudas tempranas por emergencia."
          - "Programas FRPD bajo Res. 33 (Innovación)."
        Req:
          - "Se podrá destinar hasta un 5% del monto total de la transferencia a gastos de administración de las iniciativas en el Gobierno Regional, según glosa aplicable."
          - "Con cargo a esta transferencia se podrá contratar en la entidad pública receptora a personal a honorarios cuyo vínculo cesará una vez finalizado el convenio, dentro del límite establecido por la glosa aplicable."
          - "Cuando corresponda, considerar la calidad de agente público para honorarios según glosa aplicable."
        Src:
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-06"
        Tabla_Pasos:
          - Step: 1
            Resp: "División Proponente GORE / DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-PPR
            Activities:
              - "Elaborar Formulario de Perfil de Programa Público GORE."
            Req:
              - "Visión concisa y fundamentada."
              - "Definir contraparte única GORE frente a DIPRES/SES."
            Output: "Formulario de Perfil enviado a DIPRES/SES."
          - Step: 2
            Resp: "DIPRES / SES"
            Activities:
              - "Evaluar si iniciativa corresponde a programa y si es pertinente."
            Output:
              - "Aprobado: solicitud formal a GORE para elaborar Diseño."
              - "Rechazado: proceso se detiene."
          - Step: 3
            Resp: "División Proponente GORE / DIPIR"
            Cond: "Solo si DIPRES/SES solicita Diseño."
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-PPR
            Activities:
              - "Elaborar Formulario de Diseño con Metodología de Marco Lógico."
            Output: "Formulario de Diseño enviado."
          - Step: 4
            Resp: "DIPRES / SES"
            Activities:
              - "Revisión iterativa de diseño."
              - "Emisión de observaciones y recepción de subsanaciones."
            Output:
              - "Calificación final: `RF`, `OT` o `FI`."
          - Step: 5
            Resp: "División Proponente GORE / DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-RF
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Subsanar observaciones hasta lograr RF."
            Warn:
              - "Solo RF habilita programa para solicitar financiamiento."
            Output: "`APROBADO TÉCNICAMENTE (RF)`"
      - ID: GN-IPR-F2-TRACK-C-ESPECIALES
        Titulo: "3.3 Track C – Vías Simplificadas y Procedimientos Especiales"
        Purp: "Detallar procesos de evaluación para mecanismos agilizados."
        Ref:
          - GN-IPR-GLOS-IDI
          - GN-IPR-GLOS-MDSF
          - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
        Subtracks:
          - ID: GN-IPR-F2-C-5000UTM
            Titulo: "Proyectos < 5.000 UTM (Exención de RS)"
            Ref:
              - GN-IPR-GLOS-IDI
              - GN-IPR-GLOS-RS
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Tabla_Pasos:
              - Step: 1
                Resp: "Unidad Formuladora"
                Ref:
                  - GN-IPR-GLOS-IDI
                Activities:
                  - "Postular proyecto en BIP a etapa Ejecución o Diseño."
                Req:
                  - "Usar descriptor 'Proyecto menor a 5.000 UTM'."
                  - "Verificar que no existan causales de exclusión (fraccionamiento, EIA/CMN, problemas de terreno, etc.)."
                Output: "IDI postulada con descriptor específico."
              - Step: 2
                Resp: "Unidad Formuladora"
                Ref:
                  - GN-IPR-GLOS-IDI
                  - GN-IPR-GLOS-BIP
                Activities:
                  - "Cargar en BIP estudio preinversional simplificado y demás antecedentes exigidos."
                Output: "Carpeta digital completa."
              - Step: 3
                Resp: "Institución Financiera (GORE)"
                Ref:
                  - GN-IPR-GLOS-MDSF
                Activities:
                  - "Enviar carta de responsabilidad a MDSF declarando ausencia de impedimentos y fraccionamiento."
                Output: "Carta enviada a MDSF."
              - Step: 4
                Resp: "DIPIR GORE"
                Ref:
                  - GN-IPR-GLOS-DIPIR
                  - GN-IPR-GLOS-IDI
                Activities:
                  - "Verificar cumplimiento del procedimiento y antecedentes."
                Ctx: "La aprobación técnica la otorga el propio GORE."
                Output: "`APROBADO TÉCNICAMENTE (Exento RS)`"
          - ID: GN-IPR-F2-C-CONSERVACION
            Titulo: "Proyectos de Conservación"
            Ref:
              - GN-IPR-GLOS-IDI
              - GN-IPR-GLOS-AD
              - GN-IPR-GLOS-MDSF
            Tabla_Pasos:
              - Step: 1
                Resp: "Unidad Formuladora"
                Ref:
                  - GN-IPR-GLOS-IDI
                Activities:
                  - "Postular IDI en BIP con proceso 'Conservación'."
                Req:
                  - "Costo total <= 30% del costo de reposición del activo."
                  - "Cargar antecedentes: Memoria, Certificado de Conservación, etc."
                Output: "IDI postulada correctamente."
              - Step: 2
                Resp: "Analista GORE (DIPIR)"
                Ref:
                  - GN-IPR-GLOS-DIPIR
                Activities:
                  - "Revisar coherencia de postulación con instructivo de conservación."
                Output: "V°B° para envío a MDSF."
              - Step: 3
                Resp: "Jefatura DIPIR / GORE"
                Ref:
                  - GN-IPR-GLOS-DIPIR
                  - GN-IPR-GLOS-MDSF
                Activities:
                  - "Enviar oficio a MDSF solicitando evaluación de admisibilidad."
                Output: "IDI `ENVIADA A MDSF` en BIP."
              - Step: 4
                Resp: "Analista MDSF"
                Ref:
                  - GN-IPR-GLOS-MDSF
                  - GN-IPR-GLOS-AD
                  - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
                Activities:
                  - "Verificar que IDI clasifique como conservación."
                  - "Emitir RATE AD."
                Output: "`APROBADO TÉCNICAMENTE (AD)`"
          - ID: GN-IPR-F2-C-FRIL-8FNDR-FRPD-CIRC33
            Titulo: "FRIL, 8% FNDR, FRPD y Circular 33"
            Ctx: "Mecanismos con lógicas de evaluación propias detalladas en sus guías específicas."
            Src:
              - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-07"
              - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-12"
            Elementos:
              - Cpt: "FRIL."
                Def: "Evaluación de mérito realizada por el GORE según instructivo. Aprobación técnica interna. Considerar informe favorable del MDSF cuando aplique financiamiento vía transferencias de capital (FRIL), según glosa aplicable."
              - Cpt: "8% FNDR."
                Def: "Concurso público con bases y pautas específicas; evalúa y puntúa iniciativas."
                Warn:
                  - "No financia programas públicos complejos, sino actividades acotadas."
                Req:
                  - "Exigir garantías (pagaré) a instituciones privadas adjudicatarias."
                  - "Asignaciones directas excepcionales: aplicar límites y condiciones de la glosa vigente, previo acuerdo del CORE cuando corresponda."
              - Cpt: "FRPD (Royalty)."
                Def: "Fondo evaluado según bases del concurso FRPD."
                Ctx:
                  - "Tipología Innovación."
                  - "Exenta de evaluación ex ante Glosa 06 (Res. 33/2024 MCTCI)."
              - Cpt: "Circular 33 (ANF, Estudios)."
                Def: "Tramitación vía DIPRES y V°B° DIPRES como aprobación técnica GORE."

  Fase_3_Financiamiento_y_Aprobacion_Presupuestaria:
    ID: GN-IPR-FASE3-FINANC
    Purp: "Gestionar asignación de recursos presupuestarios para IPR con aprobación técnica, incluyendo aprobación CORE cuando aplique."
    Fnd:
      - "LOC GORE Art. 36 y 78."
      - "Glosa 01, Partida 31, Ley Presupuestos 2026."
    Src:
      - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-01"
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-CORE
      - GN-IPR-GLOS-CDP
      - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
    Secciones:
      - ID: GN-IPR-F3-SIN-CORE
        Titulo: "4.1 Modificaciones Presupuestarias sin Acuerdo Obligatorio CORE"
        Ref:
          - GN-IPR-GLOS-CDP
          - GN-IPR-GLOS-DIPIR
        Tabla_Pasos:
          - Step: 1
            Resp: "Jefatura DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-CDP
            Activities:
              - "Analizar cartera de IPR con aprobación técnica."
              - "Solicitar al Depto. Presupuesto la emisión del CDP."
            Output: "Solicitud de CDP enviada."
          - Step: 2
            Resp: "Jefatura Depto. Presupuesto (DAF)"
            Ref:
              - GN-IPR-GLOS-CDP
            Activities:
              - "Verificar disponibilidad de fondos."
              - "Elaborar y enviar CDP a unidad solicitante."
            Output: "CDP emitido."
          - Step: 3
            Resp: "Jefatura de Preinversión / Unidad Patrocinante"
            Ref:
              - GN-IPR-GLOS-IPR
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Recibir CDP."
              - "Enviar memo al Depto. Presupuesto instruyendo iniciar tramitación de modificación presupuestaria."
            Output: "`ENVIADO A FINANCIAMIENTO`"
      - ID: GN-IPR-F3-CON-CORE
        Titulo: "4.2 Iniciativas con Aprobación Obligatoria del CORE"
        Ctx: "Aplica a mayoría de proyectos de inversión (>7.000 UTM) y a otras IPR que se definan políticamente."
        Ref:
          - GN-IPR-GLOS-CORE
          - GN-IPR-GLOS-DIPIR
          - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
        Tabla_Pasos:
          - Step: 1
            Resp: "Jefatura DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-IPR
            Activities:
              - "Analizar cartera de IPR con aprobación técnica."
              - "Solicitar preparación de documentación para CORE."
            Output: "`INSTRUCCIÓN PARA PREPARAR ENVÍO A CORE`"
          - Step: 2
            Resp: "Jefatura de Preinversión (DIPIR)"
            Ref:
              - GN-IPR-GLOS-DIPIR
            Activities:
              - "Elaborar carpeta CORE (oficios, fichas IDI, antecedentes de respaldo)."
            Output: "`CARTERA DISPONIBLE PARA ENVÍO A CORE`"
          - Step: 3
            Resp: "Jefatura DIPIR / Gobernador/a"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-CORE
            Activities:
              - "Presentar cartera al Gobernador/a para V°B° final."
              - "Firmar oficio y enviar formalmente cartera al CORE."
            Output: "`CARTERA ENVIADA A CORE`"
          - Step: 4
            Resp: "CORE"
            Ref:
              - GN-IPR-GLOS-CORE
              - GN-IPR-GLOS-IPR
            Activities:
              - "Analizar cartera en comisiones y sesión plenaria."
              - "Votar aprobación o rechazo del financiamiento."
            Output: "`IPR APROBADAS/RECHAZADAS`"
          - Step: 5
            Resp: "Secretario/a Ejecutivo CORE"
            Ref:
              - GN-IPR-GLOS-CORE
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Activities:
              - "Comunicar resultados y emitir Certificado de Acuerdo CORE."
              - "Usar formato estandarizado de certificado indicado por DIPRES para el año presupuestario vigente."
            Output: "`CERTIFICADO CORE OK`"
          - Step: 6
            Resp: "Jefatura DIPIR / Jefatura Preinversión"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-IPR
            Activities:
              - "Con certificado CORE, solicitar al Depto. Presupuesto la creación de asignación presupuestaria."
            Output: "`ENVIADA A CREACIÓN PPT.`"

  Fase_4_Gestion_Presupuestaria_y_Formalizacion:
    ID: GN-IPR-FASE4-GESTION-PPT
    Purp: "Traducir aprobación de financiamiento en actos administrativos y convenios que permitan ejecutar y transferir recursos."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
    Secciones:
      - ID: GN-IPR-F4-ACTOS-ADMIN
        Titulo: "5.1 Tramitación de Actos Administrativos (Decretos y Resoluciones)"
        Ctx: "Tipo de acto según si modificación afecta solo presupuesto interno o Partida 31 nacional."
        Tabla_Pasos:
          - Step: 1
            Resp: "Profesional Depto. Presupuesto"
            Activities:
              - "Elaborar borrador de Resolución (modificación interna) o solicitud a DIPRES para Decreto (afecta Partida 31)."
            Output: "Borrador de Resolución / Solicitud de Decreto."
          - Step: 2
            Resp: "DAF / DIPIR / Unidad de Control"
            Ref:
              - GN-IPR-GLOS-DIPIR
            Req:
              - "Acto debe obtener V°B° internos (Jurídico, Jefatura Presupuesto, Jefatura DIPIR, Administrador/a Regional)."
            Output: "Acto visado internamente."
          - Step: 3
            Resp: "Gobernador/a"
            Activities:
              - "Firmar resolución interna o oficio a DIPRES para tramitación del Decreto."
            Output: "Acto firmado."
          - Step: 4
            Resp: "GORE / DIPRES / CGR"
            Activities:
              - "Si Resolución GORE: enviar a DIPRES para visación y a CGR para Toma de Razón."
              - "Si Decreto DIPRES: DIPRES elabora, envía a CGR para Toma de Razón y publica."
            Output: "`RESOLUCIÓN/DECRETO CON TOMA DE RAZÓN`"
      - ID: GN-IPR-F4-CONVENIO
        Titulo: "5.2 Elaboración y Firma de Convenio"
        Warn:
          - "La transferencia de recursos solo puede materializarse después de la total tramitación del convenio."
        Src:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART23"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART25"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26"
        Tabla_Pasos:
          - Step: 1
            Resp: "Profesional Depto. Presupuesto"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Con asignación presupuestaria asegurada, elaborar borrador de Convenio de Transferencia."
            Req:
              - "Contenido mínimo: partes, objeto, monto, plazos, productos, obligaciones, rendición de cuentas, restitución."
              - "Cuando la transferencia corresponda a institución privada: verificar régimen de concurso y convenio, y condiciones de asignación directa excepcional, según normas vigentes."
              - "Acreditar objeto social/fines pertinentes de la institución receptora y condicionar la suscripción al cumplimiento íntegro de obligaciones aplicables."
              - "Incluir cláusulas de rendición de cuentas vía SISREC CGR, restitución y prohibición de financiar gastos no permitidos, según glosa aplicable."
              - "Si aplica a ejecutoras de políticas públicas y el monto supera el umbral correspondiente: exigir garantías y requisitos adicionales según normas vigentes."
            Output: "Borrador de Convenio."
          - Step: 2
            Resp: "DIPIR / Jurídico / Unidad Técnica Receptora"
            Ref:
              - GN-IPR-GLOS-DIPIR
            Activities:
              - "Revisar y visar borrador del convenio."
            Output: "Convenio visado internamente."
          - Step: 3
            Resp: "Gabinete / Oficina de Partes"
            Activities:
              - "Coordinar firma de convenio entre Gobernador/a y representante legal de entidad receptora."
            Output: "`CONVENIO FIRMADO`"
      - ID: GN-IPR-F4-FORMALIZACION-DEVENGO
        Titulo: "5.3 Formalización Final y Devengo Presupuestario"
        Purp: "Tramitar actos que aprueban convenio y aplicar reglas de devengo."
        Ref:
          - GN-IPR-GLOS-SIGFE
          - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
        Tabla_Pasos:
          - Step: 1
            Resp: "Profesional Depto. Presupuesto"
            Activities:
              - "Elaborar Resolución que aprueba convenio y lo deja formalmente vigente."
            Output: "Borrador de Resolución de aprobación."
          - Step: 2
            Resp: "GORE / CGR"
            Activities:
              - "Firmar resolución."
              - "Si corresponde según normativa CGR aplicable, enviar a CGR para Toma de Razón."
            Output: "`CONVENIO FORMALIZADO (TRAMITADO)`"
          - Step: 3
            Resp: "Profesional DAF / DIPIR"
            Ctx:
              - "Con convenio tramitado, obligación se vuelve exigible."
              - "Regla de devengo varía según tipo de receptor."
            Ref:
              - GN-IPR-GLOS-SIGFE
              - GN-IPR-GLOS-SISREC
            Activities:
              - "Programar transferencias considerando:"
            Detalle_Devengo:
              - "Transferencias a privados y municipios: devengo cuando obligación es exigible (convenio tramitado)."
              - "Transferencias a otros servicios públicos no consolidables: devengo cuando se aprueba la rendición de cuentas."
            Src:
              - "Normativa CGR y DIPRES sobre devengo y procedimientos internos del GORE."
            Output: "`TRANSFERENCIA PROGRAMADA`"

  Fase_5_Ejecucion_y_Seguimiento:
    ID: GN-IPR-FASE5-EJECUCION
    Purp: "Monitorear desarrollo de la IPR, asegurando cumplimiento técnico y uso correcto de recursos."
    Fnd:
      - "Ley 19.886 (Compras Públicas)."
      - "Res. 30/2015 CGR (Rendiciones)."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-BIP
      - GN-IPR-GLOS-SIGFE
      - GN-IPR-GLOS-SISREC
    Secciones:
      - ID: GN-IPR-F5-INICIO-COORDINACION
        Titulo: "6.1 Inicio del Proyecto y Reuniones de Coordinación"
        Tabla_Pasos:
          - Step: 1
            Resp: "División Patrocinante / Depto. Inversiones"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Antes del inicio, chequear documentación técnica aprobada (EE.TT., planos, etc.)."
            Output: "Revisión conforme de antecedentes."
          - Step: 2
            Resp: "División Patrocinante / Depto. Presupuesto / Unidad Técnica Receptora"
            Activities:
              - "Convocar reunión formal GORE–UT receptora."
              - "Aclarar roles, responsabilidades, plazos, hitos de control y procedimientos de rendición."
            Output: "Acta de reunión con acuerdos."
          - Step: 3
            Resp: "Supervisor/a del Proyecto (GORE)"
            Activities:
              - "Crear carpeta de seguimiento (digital/física) con todos los antecedentes del proyecto."
            Output: "Carpeta de seguimiento creada."
      - ID: GN-IPR-F5-LICITACION
        Titulo: "6.2 Licitación y Adjudicación (cuando aplica)"
        Ctx: "Cuando corresponda, aplicar exigencias de licitación pública obligatoria y sus excepciones según normativa vigente."
        Req:
          - "Proyectos y programas de inversión: licitación pública obligatoria cuando el monto sea superior a 1.000 UTM, salvo excepciones por emergencia según normativa aplicable."
          - "Estudios básicos: licitación pública obligatoria cuando el monto sea superior a 500 UTM, salvo excepciones por emergencia según normativa aplicable."
        Src:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART06"
        Tabla_Pasos:
          - Step: 1
            Resp: "Unidad Técnica Receptora"
            Activities:
              - "Elaborar bases de licitación y publicar en Mercado Público."
              - "Gestionar proceso de licitación para contratar ejecución."
            Output: "Licitación adjudicada."
          - Step: 2
            Resp: "Unidad Técnica Receptora"
            Activities:
              - "Firmar contrato con adjudicatario."
            Output: "Contrato firmado."
          - Step: 3
            Resp: "Unidad Técnica Receptora"
            Activities:
              - "Formalizar inicio de ejecución física (Entrega de Terreno u Orden de Inicio)."
            Output: "Acta de Entrega de Terreno u Orden de Inicio."
      - ID: GN-IPR-F5-SEGUIMIENTO
        Titulo: "6.3 Seguimiento y Supervisión"
        Tabla_Pasos:
          - Step: 1
            Resp: "Supervisor/a del Proyecto (GORE)"
            Ref:
              - GN-IPR-GLOS-BIP
            Activities:
              - "Realizar visitas a terreno periódicas."
              - "Revisar informes de avance de la UT."
              - "Gestionar Estados de Pago cuando aplique."
              - "Actualizar BIP con % de avance físico."
            Output: "Informes de visita y supervisión, avance en BIP."
          - Step: 2
            Resp: "Analista Financiero (DAF/DIPIR)"
            Ref:
              - GN-IPR-GLOS-SIGFE
              - GN-IPR-GLOS-SISREC
            Activities:
              - "Monitorear ejecución presupuestaria en SIGFE."
              - "Revisar rendiciones de cuentas en SISREC."
              - "Alertar sobre sub-ejecución o desviaciones."
            Src:
              - "Normativa CGR sobre rendiciones y lineamientos internos del GORE."
            Output: "Informes de ejecución financiera."
          - Step: 3
            Resp: "Comité de Seguimiento (si aplica)"
            Activities:
              - "Realizar reuniones periódicas GORE–UT para revisar estado integral de la IPR."
            Output: "Actas de reunión con acuerdos y planes de acción."

  Fase_6_Gestion_de_Modificaciones_IPR:
    ID: GN-IPR-FASE6-MODIFICACIONES
    Purp: "Gestionar formalmente cambios durante la ejecución, asegurando viabilidad y legalidad."
    Fnd:
      - "LOC GORE Art. 36."
      - "Glosa 01 Ley de Presupuestos 2026 (Partida 31)."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-DIPIR
      - GN-IPR-GLOS-CORE
      - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
    Secciones:
      - ID: GN-IPR-F6-SOLICITUD
        Titulo: "7.1 Solicitud de Modificación"
        Tabla_Pasos:
          - Step: 1
            Resp: "Unidad Técnica Receptora"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Detectar necesidad de modificación (sobrecosto, obra adicional, imprevisto, etc.)."
              - "Preparar informe técnico y financiero que justifique la modificación."
            Output: "Informe de solicitud de modificación."
          - Step: 2
            Resp: "Unidad Técnica Receptora"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Enviar oficio al Gobernador/a solicitando formalmente la modificación, adjuntando informe y antecedentes (nuevos presupuestos, planos, etc.)."
            Output: "Solicitud formal ingresada al GORE."
      - ID: GN-IPR-F6-REEVALUACION
        Titulo: "7.2 Evaluación de la Modificación (Reevaluación)"
        Tabla_Pasos:
          - Step: 1
            Resp: "Supervisor/a GORE / Analista DIPIR"
            Ref:
              - GN-IPR-GLOS-DIPIR
            Activities:
              - "Analizar pertinencia y justificación técnica de la modificación."
              - "Verificar que no altere sustancialmente el objetivo del proyecto."
            Output: "Informe técnico GORE sobre modificación."
          - Step: 2
            Resp: "DIPIR / DIPLADE"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-DIPLADE
            Activities:
              - "Si cambio es significativo, reevaluar conveniencia de la IPR."
              - "Verificar si nuevo costo total supera umbrales que exigen nuevo pronunciamiento CORE o SNI."
            Src:
              - "Normativa e instructivos internos del GORE sobre umbrales de reingreso al CORE y SNI."
            Output: "Pronunciamiento técnico sobre viabilidad de modificación."
          - Step: 3
            Resp: "Jefatura DIPIR / GORE"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-CORE
            Activities:
              - "Con base en informes técnicos, aprobar o rechazar la modificación."
            Output: "Decisión formal sobre modificación."
      - ID: GN-IPR-F6-TRAMITACION
        Titulo: "7.3 Tramitación de la Modificación"
        Ctx: "Proceso similar a Fases 3 y 4, aplicado a una modificación."
        Tabla_Pasos:
          - Step: 1
            Resp: "DIPIR / CORE"
            Ref:
              - GN-IPR-GLOS-DIPIR
              - GN-IPR-GLOS-CORE
              - GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO
            Cond: "Solo si modificación implica aumento de presupuesto."
            Activities:
              - "Repetir proceso de solicitud de financiamiento y, si aplica, paso por CORE."
            Output: "Fondos adicionales aprobados."
          - Step: 2
            Resp: "DAF / Depto. Presupuesto"
            Activities:
              - "Tramitar modificación presupuestaria (Resolución/Decreto)."
              - "Modificar convenio de transferencia según corresponda."
            Output: "Convenio y presupuesto modificados y tramitados."

  Fase_7_Cierre_y_Evaluacion_ExPost:
    ID: GN-IPR-FASE7-CIERRE
    Purp: "Formalizar finalización de la IPR y generar lecciones aprendidas mediante evaluación ex-post cuando corresponda."
    Fnd:
      - "Res. 30/2015 CGR."
    Ref:
      - GN-IPR-GLOS-IPR
      - GN-IPR-GLOS-CORE
      - GN-IPR-GLOS-SISREC
    Secciones:
      - ID: GN-IPR-F7-CIERRE-TECNICO
        Titulo: "8.1 Cierre Técnico"
        Tabla_Pasos:
          - Step: 1
            Resp: "Unidad Técnica Receptora"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Realizar recepción provisoria y definitiva de obras al contratista."
              - "Tras período de garantía, formalizar recepción definitiva."
            Output: "Acta de Recepción Definitiva de Obras."
          - Step: 2
            Resp: "Unidad Técnica / Supervisor GORE"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Elaborar informe final de ejecución (productos, metas, resultados)."
              - "Validar informe por parte del Supervisor GORE."
            Output: "Informe final técnico aprobado."
      - ID: GN-IPR-F7-CIERRE-FINANCIERO
        Titulo: "8.2 Cierre Financiero y Administrativo"
        Src:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24"
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26"
        Tabla_Pasos:
          - Step: 1
            Resp: "Unidad Técnica Receptora"
            Ref:
              - GN-IPR-GLOS-SISREC
            Activities:
              - "Presentar rendición final de cuentas en SISREC CGR, sin saldos por rendir."
            Src:
              - "Normativa CGR de rendiciones y manual interno de gestión de rendiciones del GORE."
            Output: "Rendición final presentada."
          - Step: 2
            Resp: "Analista Financiero GORE (DAF)"
            Ref:
              - GN-IPR-GLOS-SISREC
            Activities:
              - "Revisar y aprobar rendición final según guía específica."
              - "Solicitar reintegro de saldos no utilizados o gastos rechazados."
              - "Pronunciarse de manera fundada sobre la rendición dentro del plazo máximo aplicable, salvo que el convenio establezca un plazo diferente."
            Src:
              - "Procedimientos internos y normativa CGR vigente."
            Output: "Rendición final aprobada y saldos reintegrados."
          - Step: 3
            Resp: "Profesional Depto. Presupuesto"
            Ref:
              - GN-IPR-GLOS-IPR
            Activities:
              - "Elaborar resolución que aprueba la rendición de cuentas y declara cierre del convenio."
            Output: "Resolución de Cierre de Convenio."
          - Step: 4
            Resp: "DAF / Entidad Receptora"
            Activities:
              - "Una vez cerrado el convenio, gestionar devolución de garantías."
            Output: "Garantías devueltas."
      - ID: GN-IPR-F7-EVAL-EXPOST
        Titulo: "8.3 Evaluación Ex-Post"
        Tabla_Pasos:
          - Step: 1
            Resp: "MDSF / GORE"
            Ref:
              - GN-IPR-GLOS-MDSF
              - GN-IPR-GLOS-IPR
            Activities:
              - "Seleccionar IPR relevantes para evaluación ex-post."
            Output: "Muestra de IPR a evaluar."
          - Step: 2
            Resp: "Equipo Evaluador Externo/Interno"
            Activities:
              - "Realizar estudio comparando situación 'con proyecto' vs. 'sin proyecto'."
            Output: "Informe de Evaluación Ex-Post."
          - Step: 3
            Resp: "GORE / SNI"
            Activities:
              - "Utilizar conclusiones y lecciones aprendidas para mejorar formulación y evaluación de futuras IPR."
            Output: "Lecciones aprendidas incorporadas al ciclo de inversión."
