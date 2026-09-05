---
urn: urn:gn:kb:gn-transferencia-ppr
nombre: gn-transferencia-ppr
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Transferencia de Programas Públicos Regionales (PPR) a Entidades Públicas; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_001_transferencia_ppr_koda.yml (sha256:0bfe6fe77bdf1520b152f1b1230847083f52209ac167f6d1eb19375c4029093b); URN KODA legado urn:gorenuble:gn:transferencia-ppr:1.0.0; estado original draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "transferencia"]
familia: bok
---
# Artefacto KODA/Spec – Transferencia de Programas Públicos Regionales (PPR) a Entidades Públicas
# Fuente: kb_gn_001_guia_transferencia_programas_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:transferencia-ppr:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_001_transferencia_ppr_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "FS"
    created_at: "2025-11-28"
    last_modified_at: "2025-12-15"
    signature: null

ID: GN-PPR-TRANSFER-GUIDE-01
Version: 1.0.0
Status: draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-12-15
Ctx: "Guía operativa para la transferencia de Programas Públicos Regionales (PPR) a entidades públicas en el GORE Ñuble."
Primary-Source: kb_gn_001_guia_transferencia_programas_sts.md

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

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content en idioma original (español). Nunca traduzcas el contenido.
    END_LLM_INSTRUCTIONS

Glosario_PPR_Transferencia:
  ID: GN-PPR-GLOSARIO-01
  Purp: "Definir conceptos, siglas y normas clave recurrentes en la guía de transferencia de Programas Públicos Regionales (PPR)."
  Terminos:
    - ID: GN-PPR-GLOS-PPR
      Sigla: "PPR"
      Cpt: "Programa Público Regional"
      Def: "Conjunto integrado y articulado de acciones, prestaciones y beneficios destinados a un propósito específico en una población objetivo, para resolver un problema o necesidad."
    - ID: GN-PPR-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento de proyectos y programas regionales administrada por los Gobiernos Regionales."
    - ID: GN-PPR-GLOS-GORE
      Sigla: "GORE"
      Cpt: "Gobierno Regional"
      Def: "Administración superior de la región, con personalidad jurídica y patrimonio propio, responsable de la inversión y programas regionales."
    - ID: GN-PPR-GLOS-DAE
      Sigla: "DAE"
      Cpt: "Departamento de Análisis y Evaluación"
      Def: "Unidad del GORE responsable de la evaluación técnica de programas y proyectos."
    - ID: GN-PPR-GLOS-DIPIR
      Sigla: "DIPIR"
      Cpt: "División de Presupuesto e Inversión Regional"
      Def: "División encargada del presupuesto de inversión y de la oferta programática regional."
    - ID: GN-PPR-GLOS-DIPRES
      Sigla: "DIPRES"
      Cpt: "Dirección de Presupuestos"
      Def: "Órgano técnico del Ministerio de Hacienda a cargo de la formulación, ejecución y control del Presupuesto del Sector Público."
    - ID: GN-PPR-GLOS-ERD
      Sigla: "ERD"
      Cpt: "Estrategia Regional de Desarrollo"
      Def: "Instrumento estratégico que orienta las prioridades de desarrollo regional y con el que deben alinearse los PPR."
    - ID: GN-PPR-GLOS-SNI
      Sigla: "SNI"
      Cpt: "Sistema Nacional de Inversiones"
      Def: "Marco y plataforma para la evaluación técnico-económica de proyectos de inversión pública (IDI)."
    - ID: GN-PPR-GLOS-IDI
      Sigla: "IDI"
      Cpt: "Iniciativa de Inversión"
      Def: "Proyecto de inversión en obras o activos, sujeto a evaluación en el SNI, distinto de los PPR de gasto corriente o mixto regulados en esta guía."
    - ID: GN-PPR-GLOS-MML
      Sigla: "MML"
      Cpt: "Metodología de Marco Lógico"
      Def: "Metodología obligatoria para el diseño de PPR, basada en diagnóstico, árbol de problemas, objetivos, componentes, actividades e indicadores."
    - ID: GN-PPR-GLOS-ITF
      Sigla: "ITF"
      Cpt: "Informe Técnico Favorable"
      Def: "Informe emitido por la DAE que valida técnicamente una propuesta de PPR para que pueda avanzar a la etapa de financiamiento; no equivale a una Recomendación Satisfactoria (RS) del SNI."
    - ID: GN-PPR-GLOS-GESDOC
      Sigla: "GESDOC"
      Cpt: "Gestor Documental del GORE"
      Def: "Plataforma institucional del GORE Ñuble para el ingreso y gestión de documentación de postulaciones."
    - ID: GN-PPR-GLOS-SISREC
      Sigla: "SISREC"
      Cpt: "Sistema de Rendición Electrónica de Cuentas"
      Def: "Plataforma de la Contraloría General de la República para la rendición de transferencias de Subtítulos 24 y 33."

Parte_1_Marco_General_y_Objeto:
  ID: STS-KB-GN-PPR-MARCO-01

  Proposito_y_Alcance_Guia:
    ID: STS-KB-GN-PPR-MARCO-PURP-01
    Purp: "Estandarizar el procedimiento de postulación, evaluación y transferencia de fondos FNDR para la ejecución de Programas Públicos Regionales (PPR) por parte de entidades públicas."
    Fnd:
      - "Glosa 06, Partida 31, Ley de Presupuestos 2026 (Ley N°21.796)."
      - "Oficio Circular N°22 DIPRES."
    Ctx: "La guía regula específicamente los PPR (gasto corriente o mixto para la entrega de servicios) que, por ser ejecutados por un tercero público, están exentos de la evaluación ex-ante de DIPRES/SES. En consecuencia, la evaluación de mérito y diseño de estas iniciativas es competencia del Gobierno Regional de Ñuble."
    Warn:
      - "Ámbito de aplicación estricto: este documento no aplica para proyectos de inversión (IDI) ni programas de ejecución directa del GORE."
    Exclusiones_Ambito:
      ID: STS-KB-GN-PPR-MARCO-EXCLUSIONES-01
      Casos:
        - Cpt: "Proyectos de Inversión (IDI)"
          Def: "Iniciativas de gasto de capital (obras, activos) regidas por el Sistema Nacional de Inversiones (SNI). Su transferencia sigue otros procedimientos."
        - Cpt: "Programas de Ejecución Directa GORE"
          Def: "Programas ejecutados directamente por el GORE que sí requieren el ciclo de evaluación ex-ante de DIPRES/SES."
    Ref:
      - GN-PPR-GLOS-FNDR
      - GN-PPR-GLOS-GORE

  Entidades_Postulantes_Habilitadas:
    ID: STS-KB-GN-PPR-ENTIDADES-01
    Dest:
      - "Municipalidades de la Región de Ñuble."
      - "Otros servicios públicos y entidades del Estado con competencia para ejecutar programas sociales, culturales o de fomento."
    Ejemplos:
      - Ex: "Universidades Estatales."
    Fnd:
      - "Decreto Ley 1.263 de 1975 (Ley de Administración Financiera del Estado)."
      - 'Glosa 06 de Inversión Regional ("transferencias a otras entidades públicas y al gobierno central").'

  Definicion_PPR_Transferible:
    ID: STS-KB-GN-PPR-DEF-PPR-01
    Def: "Conjunto integrado y articulado de acciones, prestaciones y beneficios (componentes) destinados a lograr un propósito específico en una población objetivo, de modo de resolver un problema o atender una necesidad que la afecte."
    Req:
      - "Duración definida y finita."
    Prohib:
      - "No debe constituir acciones permanentes de la entidad receptora, las cuales deben ser financiadas con su presupuesto regular."

  Criterios_Focalizacion_Inversion:
    ID: STS-KB-GN-PPR-FOCALIZACION-01
    Fnd:
      - "Art. 74 del DFL 1-19.175 de 2005."
    Ctx: "El FNDR opera como programa de inversiones públicas para el desarrollo regional y la compensación territorial."
    Ref:
      - GN-PPR-GLOS-FNDR
      - GN-PPR-GLOS-ERD
    Req:
      - "El propósito del programa debe solucionar un problema regional definido, que permita su identificación, demostración y tenga indicadores de cumplimiento."
      - "La formulación debe focalizarse en la disminución de brechas de un problema claramente definido."
      - "La cobertura debe considerar el aspecto regional del FNDR y la dimensión del problema."
      - "Debe existir coherencia con la Estrategia Regional de Desarrollo (ERD) Ñuble 2022-2030, el Plan de Gobierno Regional y/o la Estrategia Regional de CTCI."
      - "Se debe poner énfasis en equidad de acceso y pertinencia de beneficiarios, con mecanismos de selección transparentes y probos."
      - "Debe considerarse una capacidad de gestión óptima con máxima optimización de recursos, cumpliendo principios de eficiencia y eficacia."

  Plazos_Postulacion:
    ID: STS-KB-GN-PPR-PLAZOS-01
    Dln: "La postulación de programas para financiamiento con cargo al presupuesto del año 2026 se recibirá hasta el 30 de septiembre de 2026."
    Cond:
      - "Propuestas ingresadas post-fecha, si son recomendadas favorablemente, podrían ser consideradas para el siguiente ejercicio presupuestario, sujeto a la normativa vigente."

Parte_2_Proceso_Postulacion_y_Evaluacion_GORE:
  ID: STS-KB-GN-PPR-PROCESO-01
  Purp: "Describir el flujo que debe seguir una entidad pública para postular un PPR a financiamiento GORE y el proceso de evaluación interna que este último realizará para asegurar la pertinencia y calidad de la propuesta."

  Metodologia_Formulacion_Obligatoria_MML:
    ID: STS-KB-GN-PPR-MML-01
    Req:
      - "Las propuestas de PPR deben ser formuladas utilizando la Metodología de Marco Lógico (MML)."
    Warn:
      - "No se debe utilizar la Ficha IDI, el código BIP ni la metodología de evaluación de proyectos de inversión para este tipo de iniciativas. La postulación no se realiza en el Banco Integrado de Proyectos (BIP)."
    Src:
      - "kb_gn_025_guia-programas_sts.md"
    Rec:
      - "Se sugiere fuertemente a las entidades formuladoras capacitarse en MML para asegurar la calidad de sus propuestas."

  Documentacion_Requerida_Postulacion:
    ID: STS-KB-GN-PPR-DOCS-01
    Req:
      - "La postulación debe realizarse mediante la plataforma GESDOC del GORE, adjuntando la documentación mínima definida a continuación."
    Plataforma:
      Cpt: "Plataforma GESDOC del GORE Ñuble."
      Ref:
        - GN-PPR-GLOS-GESDOC
    Documentos_Clave:
      - N: 1
        ID: STS-KB-GN-PPR-DOC-01-OFICIO-CONDUCTOR
        Nombre: "Oficio Conductor del Representante Legal"
        Ref-SFD: "N/A"
      - N: 2
        ID: STS-KB-GN-PPR-DOC-02-FORM-PPR
        Nombre: "Formulario de Diseño de Programa Público (PPR)"
        Ref-SFD: "FORM-PPR-TRANSFER-PUBLIC-2026-V1"
      - N: 3
        ID: STS-KB-GN-PPR-DOC-03-PRESUPUESTO
        Nombre: "Presupuesto Detallado (Excel y PDF)"
        Ref-SFD: "N/A"
      - N: 4
        ID: STS-KB-GN-PPR-DOC-04-COTIZACIONES
        Nombre: "Cotizaciones de Respaldo"
        Ref-SFD: "N/A"
      - N: 5
        ID: STS-KB-GN-PPR-DOC-05-PERFILES
        Nombre: "Perfil y Descripción de Cargos"
        Ref-SFD: "FORM-ANEXO1-PERFIL-CARGOS-V1"
      - N: 6
        ID: STS-KB-GN-PPR-DOC-06-PATROCINIO
        Nombre: "Certificado de Pertinencia y Patrocinio GORE"
        Ref-SFD: "FORM-PPR-PATROCINIO-GORE-V1"
      - N: 7
        ID: STS-KB-GN-PPR-DOC-07-DJ-RENDICIONES
        Nombre: "Declaración Jurada de Rendiciones y SISREC"
        Ref-SFD: "FORM-PPR-RENDICIONES-DJ-V1"
      - N: 8
        ID: STS-KB-GN-PPR-DOC-08-DJ-NO-FRACCION
        Nombre: "Certificado de No Fraccionamiento de Programas"
        Ref-SFD: "FORM-PPR-NO-FRACCION-DJ-V1"
      - N: 9
        ID: STS-KB-GN-PPR-DOC-09-COMPROMISO-FINANCIERO
        Nombre: "Certificado de Compromiso Financiero"
        Ref-SFD: "FORM-PPR-FINANZAS-COMP-V1"
      - N: 10
        ID: STS-KB-GN-PPR-DOC-10-DOCS-LEGALES
        Nombre: "Documentos Legales de la Entidad (Estatutos, Personería)"
        Ref-SFD: "N/A"
      - N: 11
        ID: STS-KB-GN-PPR-DOC-11-OTROS-ANEXOS
        Nombre: "Otros Anexos (si aplica)"
        Ref-SFD: "N/A"

  Proceso_Evaluacion_Interna_GORE:
    ID: STS-KB-GN-PPR-EVAL-01
    Ctx: "Dado que estos programas están exentos de evaluación central, el GORE realiza un proceso de evaluación de admisibilidad, pertinencia y mérito técnico, para resguardar el correcto uso de los fondos públicos."
    Pasos:
      - Step: 1
        Nombre: "Admisibilidad Documental"
        Resp: "Departamento de Análisis y Evaluación (DAE)."
        Act: "Verificar que la postulación contiene toda la documentación requerida en la sección 2.2 y que ha sido ingresada correctamente. Las postulaciones incompletas serán devueltas para subsanación en un plazo acotado."
      - Step: 2
        Nombre: "Evaluación de Pertinencia Estratégica"
        Resp: "Comité de Pertinencia Regional (o instancia que lo reemplace)."
        Act: "Evaluar la alineación del programa con la Estrategia Regional de Desarrollo (ERD), el Plan de Gobierno Regional y las prioridades políticas definidas para el año."
      - Step: 3
        Nombre: "Evaluación Técnica de Diseño"
        Resp: "Departamento de Análisis y Evaluación (DAE)."
        Act: "Revisión de fondo de la propuesta."
        Criterios_Clave:
          - "Calidad y suficiencia del diagnóstico."
          - "Coherencia y robustez de la Matriz de Marco Lógico (causa-problema-propósito-componentes-actividades)."
          - "Pertinencia y realismo de los indicadores propuestos."
          - "Factibilidad técnica y operativa del modelo de gestión."
          - "Racionalidad y eficiencia del presupuesto solicitado."
    Resultado_Evaluacion:
      ID: STS-KB-GN-PPR-EVAL-RESULTADO-01
      Def: "La evaluación culmina con un Informe Técnico Favorable (ITF) emitido por la DAE."
      Warn:
        - "Este informe NO es un RATE RS. Es un documento interno del GORE que valida técnicamente la propuesta para que pueda avanzar a la etapa de financiamiento."
      Calificaciones_Posibles:
        - "Recomendado Favorablemente: La propuesta es sólida y se recomienda para su aprobación presupuestaria."
        - "Recomendado con Observaciones: La propuesta es pertinente pero requiere ajustes para ser financiada. La entidad postulante deberá subsanar las observaciones en un plazo definido."
        - "No Recomendado: La propuesta presenta debilidades técnicas o de pertinencia insalvables que no la hacen elegible para financiamiento."

Parte_3_Restricciones_Normativas_y_Financieras:
  ID: STS-KB-GN-PPR-RESTRICCIONES-01

  Restricciones_Generales:
    ID: STS-KB-GN-PPR-RESTR-GEN-01
    Prohib:
      - "Postular programas cuyo objetivo o naturaleza sea distinto al descrito en la ley o decreto de creación de la institución."
    Cond:
      - "Instituciones con convenios vigentes con el GORE deben acreditar su estado de rendiciones de cuentas."
    Fnd:
      - "Resolución N°30 de 2015 de la Contraloría General de la República (CGR)."

  Restricciones_de_Gasto:
    ID: STS-KB-GN-PPR-RESTR-GASTO-01
    Ctx: "Los recursos FNDR transferidos para programas tienen las siguientes restricciones de gasto:"
    Prohib:
      - "Otorgar préstamos o constituir/comprar sociedades con cargo a los recursos transferidos."
    Cond:
      - "Gastos en Personal: la entidad receptora puede usar hasta un 5% del total de la transferencia para contratar personal a honorarios para la gestión del programa."
      - "Gastos de Administración: el GORE puede destinar hasta un 5% del monto total a gastos de administración propios para la gestión y seguimiento. Este monto no forma parte de la transferencia."
    Fnd:
      - "Glosa 06, Partida 31, Ley de Presupuestos 2026 (Ley N°21.796)."
    Ref:
      - GN-PPR-GLOS-FNDR

  Restricciones_de_Probidad:
    ID: STS-KB-GN-PPR-RESTR-PROBIDAD-01
    Cond:
      - "La subcontratación es permitida solo para actividades que no constituyen el objeto principal del programa, debe estar justificada y detallada en el convenio."
    Prohib:
      - "Subcontratar con personas jurídicas relacionadas (matriz, filial, etc. según Ley 18.046) o con personas naturales que tengan conflictos de interés por parentesco con autoridades regionales o directivos de la institución postulante."
      - "Contratar para la ejecución del programa a cónyuges, convivientes civiles, o parientes hasta el tercer grado de consanguinidad y segundo de afinidad de autoridades y funcionarios directivos del GORE o de la institución postulante."
    Ref:
      - GN-PPR-GLOS-GORE

Parte_4_Formalizacion_Ejecucion_y_Seguimiento:
  ID: STS-KB-GN-PPR-FORMALIZACION-01

  Aprobacion_Presupuestaria_y_Convenio:
    ID: STS-KB-GN-PPR-FORMAL-APROB-CONV-01
    Proc:
      - Step: 1
        Nombre: "Priorización y Aprobación de Recursos"
        Act: "Los PPR con Informe Técnico Favorable (ITF) son presentados por la DIPIR al Gobernador(a) y, si corresponde por normativa presupuestaria, al Consejo Regional para la aprobación de los fondos."
      - Step: 2
        Nombre: "Elaboración de Convenio de Transferencia"
        Act: "El Departamento de Presupuesto del GORE elabora un convenio que formaliza la transferencia, el cual debe ser suscrito por los representantes legales de ambas instituciones."
      - Step: 3
        Nombre: "Contenido Mínimo del Convenio"
        Req:
          - "Partes, objeto del programa, monto total, calendario de transferencias, plazos, metas e indicadores de la MML, obligaciones de las partes, y cláusulas de rendición de cuentas y restitución de fondos."
          - "Incorporar las cláusulas de probidad y restricciones de gasto señaladas en la sección 3 de esta guía."

  Transferencia_Recursos_y_Ejecucion:
    ID: STS-KB-GN-PPR-FORMAL-TRANSFER-EJEC-01
    Mech:
      - "La transferencia de fondos se realiza según lo estipulado en el convenio, usualmente contra la presentación de estados de avance o cumplimiento de hitos."
    Resp:
      - "La entidad pública receptora es la responsable de la ejecución técnica y financiera del programa, cumpliendo la normativa de compras públicas que le aplique."
      - "El GORE, a través de su división patrocinante, supervisa el avance y cumplimiento del convenio."

  Seguimiento_y_Rendicion:
    ID: STS-KB-GN-PPR-FORMAL-SEGUIMIENTO-01
    Resp:
      - "La entidad ejecutora debe rendir cuenta de los fondos al GORE en los plazos y formatos estipulados en el convenio."
    Fnd:
      - "La rendición se rige por la Resolución N°30 de 2015 de la CGR y sus modificaciones."
    Mech:
      - "El GORE podrá exigir la rendición vía plataforma SISREC o en formato físico, según se defina en el convenio."
    Src:
      - "urn:gorenuble:gn:gestion-rendiciones:1.0.0"
    Ref:
      - GN-PPR-GLOS-SISREC

Parte_5_Formularios_Estandarizados_PPR:
  ID: STS-KB-GN-PPR-FORMULARIOS-01
  Ctx: "Los formatos estandarizados para la postulación se encontrarán disponibles en la página web del Gobierno Regional de Ñuble. A continuación se define su estructura detallada."

  Formulario_Diseno_Programa_Publico_PPR:
    ID: FORM-PPR-TRANSFER-PUBLIC-2026-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-PPR-TRANSFER-S1-NOMBRE-PROGRAMA
        Seccion: "Sección 1: Identificación del Programa"
        Field-Label: "Nombre del Programa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S1-MONTO-FNDR
        Seccion: "Sección 1: Identificación del Programa"
        Field-Label: "Monto total solicitado FNDR (M$)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S1-APORTE-PROPIO
        Seccion: "Sección 1: Identificación del Programa"
        Field-Label: "Aporte Propio / Otros Aportes (M$)"
        Field-Type: Number
        Field-Constraint: "Req: optional."
      - ID: FORM-PPR-TRANSFER-S1-PLAZO-EJECUCION
        Seccion: "Sección 1: Identificación del Programa"
        Field-Label: "Plazo de ejecución (meses)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 1."
      - ID: FORM-PPR-TRANSFER-S1-ALINEACION-ERD
        Seccion: "Sección 1: Identificación del Programa"
        Field-Label: "Alineación con ERD (Indicar Eje, Lineamiento, Objetivo)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."

      - ID: FORM-PPR-TRANSFER-S2-INSTITUCION
        Seccion: "Sección 2: Institución Postulante"
        Field-Label: "Institución o Servicio Postulante"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S2-OBJETO-SOCIAL
        Seccion: "Sección 2: Institución Postulante"
        Field-Label: "Objeto social de la institución (Resumen según estatuto/ley)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S2-FUNDAMENTO-TRANSFERENCIA
        Seccion: "Sección 2: Institución Postulante"
        Field-Label: "Fundamento de la solicitud de transferencia (Justificar por qué su institución es la idónea para ejecutar el programa)."
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."

      - ID: FORM-PPR-TRANSFER-S3-PROBLEMA-CENTRAL
        Seccion: "Sección 3: Diagnóstico y Problema (MML)"
        Field-Label: "Definición del problema central que afecta a la comunidad."
        Field-Type: TextArea
        Field-Instr: "Redactar como estado negativo, claro y preciso. Debe estar respaldado por datos."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S3-ANALISIS-CAUSAL
        Seccion: "Sección 3: Diagnóstico y Problema (MML)"
        Field-Label: "Análisis Causal: Causas y Efectos del Problema"
        Field-Type: TextArea
        Field-Instr: "Describir las causas directas e indirectas que explican el problema, y los efectos que este genera. Adjuntar diagrama de árbol de problemas si es necesario."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S3-POBLACION
        Seccion: "Sección 3: Diagnóstico y Problema (MML)"
        Field-Label: "Caracterización y Cuantificación de la Población"
        Field-Type: TextArea
        Field-Instr: "Describir y cuantificar la población potencial, la población objetivo y los beneficiarios anuales, indicando fuentes de datos."
        Field-Constraint: "Req: mandatory."

      - ID: FORM-PPR-TRANSFER-S4-PROPOSITO
        Seccion: "Sección 4: Diseño de la Intervención (MML)"
        Field-Label: "Propósito del programa (Objetivo General)"
        Field-Type: TextArea
        Field-Instr: "Debe ser la reversión en positivo del problema central. Único, medible y orientado a la población objetivo."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S4-COMPONENTES
        Seccion: "Sección 4: Diseño de la Intervención (MML)"
        Field-Label: "Componentes del Programa"
        Field-Type: Repeater
        Field-Instr: "Añada una fila por cada Componente (producto o servicio) que entregará el programa."
        Field-SubLabels:
          - "Nombre del Componente"
          - "Descripción del bien/servicio"
          - "Causa del problema que aborda"
          - "Unidad de medida y meta de producción anual"
      - ID: FORM-PPR-TRANSFER-S4-MATRIZ-MML
        Seccion: "Sección 4: Diseño de la Intervención (MML)"
        Field-Label: "Matriz de Marco Lógico"
        Field-Type: File
        Field-Instr: "Adjuntar la Matriz de Marco Lógico completa (Fin, Propósito, Componentes, Actividades) con sus respectivos Indicadores, Medios de Verificación y Supuestos."
        Field-Constraint: "Req: mandatory."

      - ID: FORM-PPR-TRANSFER-S5-MODELO-GESTION
        Seccion: "Sección 5: Operatividad y Presupuesto"
        Field-Label: "Modelo de Gestión y Carta Gantt"
        Field-Type: TextArea
        Field-Instr: "Describir cómo se implementará el programa, el flujo del beneficiario, y adjuntar una Carta Gantt detallada de actividades y financiera."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S5-PRESUPUESTO
        Seccion: "Sección 5: Operatividad y Presupuesto"
        Field-Label: "Detalle del Presupuesto por Componente y Actividad"
        Field-Type: File
        Field-Instr: "Adjuntar planilla Excel con el desglose del presupuesto, justificando cada ítem de gasto y su coherencia con las actividades de la MML."
        Field-Constraint: "Req: mandatory."

      - ID: FORM-PPR-TRANSFER-S6-FIRMA-FORMULADOR
        Seccion: "Sección 6: Firmas"
        Field-Label: "Nombre, firma y timbre del Formulador"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para firma."
      - ID: FORM-PPR-TRANSFER-S6-CONTACTO-FORMULADOR
        Seccion: "Sección 6: Firmas"
        Field-Label: "Fono y Mail contacto formulador"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-TRANSFER-S6-FIRMA-REPRESENTANTE
        Seccion: "Sección 6: Firmas"
        Field-Label: "Nombre firma y timbre del jefe de Servicio o Representante de la Institución"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para firma."
      - ID: FORM-PPR-TRANSFER-S6-CONTACTO-REPRESENTANTE
        Seccion: "Sección 6: Firmas"
        Field-Label: "Fono y Mail contacto representante"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."

  Anexo_Perfil_y_Descripcion_de_Cargos:
    ID: FORM-ANEXO1-PERFIL-CARGOS-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-ANEXO1-S1-PERFILES-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Perfiles Requeridos para la Iniciativa"
        Field-Type: Repeater
        Field-Instr: "Añada una entrada por cada tipo de cargo requerido."
      - ID: FORM-ANEXO1-S1-NOMBRE-CARGO-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Nombre del cargo"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S1-NUMERO-CARGOS-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "N° de Cargos"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 1."
      - ID: FORM-ANEXO1-S1-DEPTO-SUPERVISOR-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Departamento supervisor"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S1-PERFIL-CARGO-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Perfil del Cargo"
        Field-Type: TextArea
        Field-Instr: "Detallar la formación, experiencia y competencias requeridas."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S1-PERIODO-CONTRATACION-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Periodo de contratación"
        Field-Type: Text
        Field-Instr: "Ej: 12 meses, media jornada."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S1-OBJETIVO-CARGO-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Objetivo del cargo"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S1-PRODUCTOS-ASOCIADOS-01
        Seccion: "Sección 1: Perfiles de Cargo"
        Field-Label: "Productos asociados a la contratación"
        Field-Type: TextArea
        Field-Instr: "Listar los entregables o productos verificables."
        Field-Constraint: "Req: mandatory."
      - ID: FORM-ANEXO1-S2-FIRMA-REP-LEGAL-01
        Seccion: "Sección 2: Firma"
        Field-Label: "Nombre, firma y timbre del representante legal"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para la firma manuscrita."

  Certificado_Pertinencia_y_Patrocinio_GORE:
    ID: FORM-PPR-PATROCINIO-GORE-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-PPR-PATROCINIO-S1-NOMBRE-PROGRAMA
        Seccion: "Sección 1: Información del Programa"
        Field-Label: "NOMBRE DEL PROGRAMA"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S1-INSTITUCION
        Seccion: "Sección 1: Información del Programa"
        Field-Label: "INSTITUCIÓN POSTULANTE"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S1-PROPOSITO
        Seccion: "Sección 1: Información del Programa"
        Field-Label: "PROPÓSITO DEL PROGRAMA"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S1-MONTO-FNDR
        Seccion: "Sección 1: Información del Programa"
        Field-Label: "MONTO TOTAL SOLICITADO FNDR (M$)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S2-DIVISION-GORE
        Seccion: "Sección 2: Evaluación de Pertinencia de la División GORE"
        Field-Instr: "A ser completado por el/la Jefe/a de la División GORE correspondiente."
        Field-Label: "División GORE Patrocinante"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S2-JUSTIFICACION-PERTINENCIA
        Seccion: "Sección 2: Evaluación de Pertinencia de la División GORE"
        Field-Label: "Justificar la ejecución del programa, describiendo su pertinencia y alineación con los objetivos estratégicos de la División y la Estrategia Regional de Desarrollo."
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S2-SINERGIA-DUPLICIDAD
        Seccion: "Sección 2: Evaluación de Pertinencia de la División GORE"
        Field-Label: "¿Se identifica sinergia o duplicidad con otras iniciativas GORE en curso? Detallar."
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-PATROCINIO-S3-FIRMA-JEFE-DIVISION
        Seccion: "Sección 3: Firma"
        Field-Label: "Nombre, firma y timbre del Jefe de División patrocinante GORE"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para la firma manuscrita."

  Declaracion_Jurada_Rendiciones:
    ID: FORM-PPR-RENDICIONES-DJ-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-PPR-REN-S1-INSTR
        Seccion: "Sección 1: Identificación"
        Field-Instr: "En el marco de la iniciativa..."
      - ID: FORM-PPR-REN-S1-NOMBRE-PROGRAMA
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Programa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_______NOMBRE DEL PROGRAMA _______________"
      - ID: FORM-PPR-REN-S1-NOMBRE-REPRESENTANTE
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Representante Legal"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_NOMBRE DEL REPRESENTANTE LEGAL ________________"
      - ID: FORM-PPR-REN-S1-INSTITUCION
        Seccion: "Sección 1: Identificación"
        Field-Label: "Institución a la que representa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_INSTITUCIÓN A LA QUE REPRESENTA_________________________"
      - ID: FORM-PPR-REN-S2-ESTADO-RENDICIONES
        Seccion: "Sección 2: Declaración"
        Field-Label: "La institución que represento actualmente, mantiene rendiciones de cuenta pendiente con el Gobierno Regional de Ñuble."
        Field-Type: Radio
        Field-Constraint: "Req: mandatory."
        Field-Options:
          - "SI"
          - "NO"
      - ID: FORM-PPR-REN-S2-AVISO-CAUCION
        Seccion: "Sección 2: Declaración"
        Field-Label: "Aviso sobre Caución"
        Field-Type: Static-Text
        Field-Instr: "En caso de tener rendiciones pendientes, al momento de celebrar convenio con el Gobierno Regional, esta institución deberá rendir caución de los montos pendientes, con el fin de garantizar el buen uso de los recursos públicos."
      - ID: FORM-PPR-REN-S2-COMPROMISO-RES30
        Seccion: "Sección 2: Declaración"
        Field-Label: "Declaro estar en conocimiento de los alcances y responsabilidades establecidas en la Resolución N°30 de 2015 de la Contraloría General de la República."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-REN-S2-COMPROMISO-SISREC
        Seccion: "Sección 2: Declaración"
        Field-Label: "Declaro que, en caso de ser aprobada, las rendiciones del programa deben realizarse por medio de plataforma SISREC de la Contraloría General de la República."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-REN-S3-FIRMA-REP-LEGAL
        Seccion: "Sección 3: Firma"
        Field-Label: "Nombre, firma y timbre del representante legal"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para la firma manuscrita."

  Declaracion_Jurada_No_Fraccionamiento:
    ID: FORM-PPR-NO-FRACCION-DJ-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-PPR-NOFRACC-S1-INSTR
        Seccion: "Sección 1: Identificación"
        Field-Instr: "En el marco de la iniciativa..."
      - ID: FORM-PPR-NOFRACC-S1-NOMBRE-PROGRAMA
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Programa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_______NOMBRE DEL PROGRAMA _______________"
      - ID: FORM-PPR-NOFRACC-S1-NOMBRE-REPRESENTANTE
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Representante Legal"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_NOMBRE DEL REPRESENTANTE LEGAL ________________"
      - ID: FORM-PPR-NOFRACC-S1-INSTITUCION
        Seccion: "Sección 1: Identificación"
        Field-Label: "Institución a la que representa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
        Field-Placeholder: "_INSTITUCIÓN A LA QUE REPRESENTA_________________________"
      - ID: FORM-PPR-NOFRACC-S2-DECLARACION-NOFRACC
        Seccion: "Sección 2: Declaración"
        Field-Label: "Declaro QUE EL PROGRAMA POSTULADO ABORDA UN OBJETIVO Y PROBLEMA ÚNICO, Y NO CONSTITUYE UN FRACCIONAMIENTO DE UNA INICIATIVA MAYOR."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-NOFRACC-S2-ACLARACION
        Seccion: "Sección 2: Declaración"
        Field-Label: "Aclaración sobre propósito único"
        Field-Type: Static-Text
        Field-Instr: "Esto es que el programa considera un propósito integral, no existiendo para estos efectos otros programas complementarios que busquen el mismo fin y que hayan sido presentados por separado para eludir controles de monto o evaluación."
      - ID: FORM-PPR-NOFRACC-S3-FIRMA-REP-LEGAL
        Seccion: "Sección 3: Firma"
        Field-Label: "Nombre, firma y timbre del representante legal"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para la firma manuscrita."

  Certificado_Compromiso_Presupuesto_y_Finanzas:
    ID: FORM-PPR-FINANZAS-COMP-V1
    Version: 1.0.0
    Status: Published
    Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01
    Campos:
      - ID: FORM-PPR-FIN-S1-INSTR
        Seccion: "Sección 1: Identificación"
        Field-Instr: "En el marco de la iniciativa..."
      - ID: FORM-PPR-FIN-S1-NOMBRE-PROGRAMA
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Programa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S1-NOMBRE-ENCARGADO-FINANZAS
        Seccion: "Sección 1: Identificación"
        Field-Label: "Nombre del Encargado de Presupuesto o Finanzas"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S1-CARGO-ENCARGADO
        Seccion: "Sección 1: Identificación"
        Field-Label: "Cargo"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S1-INSTITUCION
        Seccion: "Sección 1: Identificación"
        Field-Label: "Institución a la que representa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S2-INTENCION-CAPACIDAD
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Declaro que el servicio tiene la intención y capacidad administrativa para recibir la transferencia desde el Gobierno Regional de Ñuble y administrarla en una cuenta o centro de costo separado."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S2-MONTO-FNDR
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Monto FNDR solicitado (M$)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory."
        Field-Instr: "Debe ser igual al formulario principal."
      - ID: FORM-PPR-FIN-S2-MONTO-APORTE-PROPIO
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Monto Aporte Propio (M$)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory."
        Field-Instr: "Si no tiene aporte, poner M$0."
      - ID: FORM-PPR-FIN-S2-AUTORIZACION-APORTE-PROPIO
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Declaro que el aporte propio se encuentra autorizado y estará disponible según la programación financiera presentada."
        Field-Type: Checkbox
        Field-Constraint: "Req: conditional. Visible si Monto Aporte Propio > 0."
      - ID: FORM-PPR-FIN-S2-NO-RESP-GORE
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Declaro que, en caso de ejecutar el programa, no será responsabilidad del Gobierno Regional el financiamiento posterior al término del mismo."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S2-CONTINUIDAD-GASTO-CORRIENTE
        Seccion: "Sección 2: Declaración de Compromiso"
        Field-Label: "Declaro que, en caso de que la entidad decida continuar la iniciativa post-convenio, los costos serán cargados al presupuesto regular del servicio."
        Field-Type: Checkbox
        Field-Constraint: "Req: mandatory."
      - ID: FORM-PPR-FIN-S3-FIRMA-JEFE-ADMON-FIN
        Seccion: "Sección 3: Firma"
        Field-Label: "Nombre, firma y timbre del Jefe de División o Departamento de Administración y Finanzas"
        Field-Type: Static-Text
        Field-Instr: "Espacio reservado para la firma manuscrita."
