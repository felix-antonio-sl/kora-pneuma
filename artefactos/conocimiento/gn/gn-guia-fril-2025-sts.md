---
urn: urn:gn:kb:gn-guia-fril-2025-sts
nombre: gn-guia-fril-2025-sts
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Instructivo FRIL 2025 GORE Ñuble; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_026_guia_fril_koda.yml (sha256:5da71b7468f24640b8b651538e15b019357134edebfad0e0d0f3f884165c1f0b); URN KODA legado urn:gorenuble:gn:guia-fril-2025-sts:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "guia"]
familia: bok
---
# Artefacto KODA/Spec – Instructivo FRIL 2025 GORE Ñuble
# Fuente principal: kb_gn_026_guia_fril_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:guia-fril-2025-sts:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_026_guia_fril_koda.yml"
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
    last_modified_at: "2025-11-28"
    signature: null

ID: GN-GUIA-FRIL-STS-2025-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Guía técnico-operativa para la formulación, evaluación, adjudicación, ejecución
  y rendición de iniciativas de inversión FRIL 2025 en la Región de Ñuble, basada
  en la Resolución Exenta que aprueba el instructivo regional y en la Guía
  Operativa FRIL de SUBDERE.

Source:
  Primary-Source: "staging/gn/kodeando/kb_gn_026_guia_fril_sts.md"
  Ctx_Required:
    - "Guía Operativa FRIL – Resolución Exenta N° 15.051/2023 SUBDERE"
    - "Ley N° 21.796 – Ley de Presupuestos del Sector Público 2026 (Glosa 12, Programa 02, Subtítulo 33)"
    - "DFL 1-19.175 – Ley Orgánica Constitucional de Gobierno y Administración Regional (LOC GORE)"
    - "Ley N° 18.575 – Bases Generales de la Administración del Estado"
    - "Ley N° 19.880 – Bases de los Procedimientos Administrativos"
    - "Ley N° 21.074 – Fortalecimiento de la Regionalización"
    - "Circular N° 11/2025 del Ministerio de Hacienda (Glosas GORE)"
    - "Resolución N° 36/2024 de la Contraloría General de la República (Exención Toma de Razón)"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-GUIA-FRIL-STS-2025-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers,
    IDs, listas, tablas) with zero loss. Ignore fat (filler words, retórica,
    redundancias).

    LEXICON (expand before processing):
      Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dep->Dependency, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID,
      Just->Justification, Mech->Mechanism, Mssn->Mission,
      Nat->Nature, Obj->Objective, Proc->Process,
      Prohib->Prohibition, Purp->Purpose, Ref->Reference,
      Req->Requirement, Res->Result, Resp->Responsible,
      Src->Source, Warn->Warning, Conting->Contingency, Dest->Destination.

    REFERENCE POLICY:
      - Ref: is internal only—must point to an existing ID defined within THIS document.
      - External laws, resoluciones, circulares y guías (SUBDERE, DIPRES, CGR)
        se mencionan bajo Ctx:, Src:, Ctx_Required: o Ctx_Optional:.

    LANGUAGE POLICY:
      - Keywords in English (and abbreviated forms as listed).
      - Content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_FRIL_Conceptos_Clave:
  ID: GN-FRIL-GLOSARIO-01
  Purp: "Definir conceptos, siglas y actores clave utilizados en el instructivo FRIL 2025."
  Terminos:
    - ID: GN-FRIL-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento de la inversión regional administrada por los Gobiernos Regionales."
    - ID: GN-FRIL-GLOS-FRIL
      Sigla: "FRIL"
      Cpt: "Fondo Regional de Iniciativa Local"
      Def: "Fondo FNDR destinado a proyectos de infraestructura comunal de menor escala, ejecutados principalmente por municipalidades."
    - ID: GN-FRIL-GLOS-GORE
      Sigla: "GORE"
      Cpt: "Gobierno Regional"
      Def: "Institución descentralizada, con personalidad jurídica y patrimonio propio, a cargo de la administración superior de la región."
    - ID: GN-FRIL-GLOS-CORE
      Sigla: "CORE"
      Cpt: "Consejo Regional"
      Def: "Órgano colegiado del GORE con facultades normativas, resolutivas y fiscalizadoras; aprueba instructivos y marcos de asignación FRIL."
    - ID: GN-FRIL-GLOS-SUBDERE
      Sigla: "SUBDERE"
      Cpt: "Subsecretaría de Desarrollo Regional y Administrativo"
      Def: "Organismo del Ministerio del Interior que emite la Guía Operativa FRIL y visa metodologías regionales de evaluación."
    - ID: GN-FRIL-GLOS-MDSF
      Sigla: "MDSF"
      Cpt: "Ministerio de Desarrollo Social y Familia"
      Def: "Responsable de la evaluación técnico-económica de iniciativas de inversión en el SNI."
    - ID: GN-FRIL-GLOS-BIP
      Sigla: "BIP"
      Cpt: "Banco Integrado de Proyectos"
      Def: "Plataforma del SNI para registro, evaluación y seguimiento de iniciativas de inversión, incluyendo proyectos FRIL."
    - ID: GN-FRIL-GLOS-GESDOC
      Sigla: "GESDOC"
      Cpt: "Sistema de Gestión Documental del GORE"
      Def: "Plataforma electrónica para el registro de oficios, resoluciones y anexos asociados a proyectos FRIL."
    - ID: GN-FRIL-GLOS-RS
      Sigla: "RS"
      Cpt: "Recomendado Satisfactoriamente"
      Def: "Resultado de evaluación técnica-económica que acredita que la iniciativa cumple requisitos normativos y de admisibilidad."
    - ID: GN-FRIL-GLOS-IDI
      Sigla: "IDI"
      Cpt: "Iniciativa de Inversión"
      Def: "Unidad de análisis del SNI que agrupa estudios, proyectos y programas de inversión pública."
    - ID: GN-FRIL-GLOS-BNUP
      Sigla: "BNUP"
      Cpt: "Bien Nacional de Uso Público"
      Def: "Terreno o espacio de dominio público destinado al uso de toda la comunidad (calles, plazas, áreas verdes, etc.)."
    - ID: GN-FRIL-GLOS-ITO
      Sigla: "ITO"
      Cpt: "Inspector Técnico de Obra"
      Def: "Profesional responsable de supervisar técnicamente la ejecución de la obra financiada con FRIL."

Normativa_FRIL_Clave:
  ID: GN-FRIL-NORMATIVA-01
  Purp: "Registrar las normas principales usadas como fundamento del instructivo FRIL 2025."
  Normas:
    - ID: GN-FRIL-NORM-CPR-01
      Cpt: "Constitución Política de la República"
      Def: "Norma suprema del ordenamiento jurídico chileno; establece organización del Estado y principios de probidad, responsabilidad y control."
    - ID: GN-FRIL-NORM-LOC-GORE-01
      Cpt: "Ley N° 19.175 (LOC GORE)"
      Def: "Ley Orgánica Constitucional sobre Gobierno y Administración Regional, texto refundido en DFL 1-19.175."
    - ID: GN-FRIL-NORM-LEY-18575-01
      Cpt: "Ley N° 18.575"
      Def: "Ley Orgánica Constitucional de Bases Generales de la Administración del Estado."
    - ID: GN-FRIL-NORM-LEY-19880-01
      Cpt: "Ley N° 19.880"
      Def: "Establece Bases de los Procedimientos Administrativos."
    - ID: GN-FRIL-NORM-LEY-21796-01
      Cpt: "Ley N° 21.796 – Presupuesto 2026"
      Def: "Ley de Presupuestos del Sector Público para el año 2026; incluye Glosa 12 de FNDR para FRIL."
    - ID: GN-FRIL-NORM-LEY-21074-01
      Cpt: "Ley N° 21.074"
      Def: "Ley de Fortalecimiento de la Regionalización del País."
    - ID: GN-FRIL-NORM-DL575-01
      Cpt: "Decreto Ley N° 575 – Regionalización del País"
      Def: "Norma que establece principios y reglas de regionalización y FNDR."
    - ID: GN-FRIL-NORM-RES36-CGR-2024-01
      Cpt: "Resolución N° 36/2024 CGR"
      Def: "Fija normas sobre exención del trámite de Toma de Razón para ciertos actos administrativos."
    - ID: GN-FRIL-NORM-CIRC11-HACIENDA-2025-01
      Cpt: "Circular N° 11/2025 Ministerio de Hacienda"
      Def: "Imparte instrucciones sobre aplicación de glosas presupuestarias de Gobiernos Regionales."
    - ID: GN-FRIL-NORM-RES15051-SUBDERE-2023-01
      Cpt: "Resolución Exenta N° 15.051/2023 SUBDERE"
      Def: "Fija Guía Operativa FRIL a nivel nacional."

Instructivo_FRIL_2025:
  ID: GN-GUIA-FRIL-STS-2025-01
  Titulo: "Instructivo FRIL 2025 – Región de Ñuble"
  Purp: |
    Establecer reglas, requisitos, procesos y documentación para la formulación,
    evaluación, adjudicación, ejecución y rendición de proyectos FRIL financiados
    con recursos FNDR del GORE Ñuble durante el año presupuestario 2025.
  Destinatarios:
    - "Municipalidades de la Región de Ñuble."
    - "Equipos técnicos de SECPLA y DOM comunales."
    - "Equipos de la División de Presupuesto e Inversión Regional (DIPIR)."
    - "Equipos de la División de Desarrollo Social y Humano, Infraestructura y otras divisiones del GORE vinculadas a FRIL."
  Alcance:
    - "Aplica a iniciativas FRIL 2025 financiadas con cargo a Subtítulo 33 FNDR."
    - "Complementa y particulariza la Guía Operativa FRIL emitida por SUBDERE."
    - "Vigente mientras no existan modificaciones relevantes en Ley de Presupuestos o normativa relacionada."
  Estructura_Secciones:
    - ID: GN-FRIL-SEC-1-RESOLUCION
      Cpt: "Resolución Exenta que aprueba el instructivo FRIL 2025."
    - ID: GN-FRIL-SEC-2-INTRO
      Cpt: "Introducción, objetivos del programa y marco legal."
    - ID: GN-FRIL-SEC-3-MONTO-MARCO
      Cpt: "Montos máximos/mínimos, marco por comuna y prioridades."
    - ID: GN-FRIL-SEC-4-LINEAMIENTOS
      Cpt: "Lineamientos de postulación, categorías y reglas especiales."
    - ID: GN-FRIL-SEC-5-PROHIBICIONES
      Cpt: "Prohibiciones y restricciones a la postulación."
    - ID: GN-FRIL-SEC-6-TERRENOS
      Cpt: "Situaciones especiales de terrenos y documentación legal."
    - ID: GN-FRIL-SEC-7-PLAZOS
      Cpt: "Períodos y plazos de difusión, postulación, evaluación y asesoría."
    - ID: GN-FRIL-SEC-8-PROCESO
      Cpt: "Etapas y procesos: ingreso, admisibilidad, revisión y resultados."
    - ID: GN-FRIL-SEC-9-DOC-POSTULACION
      Cpt: "Documentación requerida para la postulación (checklist)."
    - ID: GN-FRIL-SEC-10-OTRAS-CONSID
      Cpt: "Otras consideraciones de postulación y autorizaciones."
    - ID: GN-FRIL-SEC-11-REEVALUACIONES
      Cpt: "Reglas para reevaluaciones de proyectos FRIL."
    - ID: GN-FRIL-SEC-12-TRANSFERENCIAS
      Cpt: "Transferencia de recursos, convenios y flujos de pago."
    - ID: GN-FRIL-SEC-13-EJECUCION
      Cpt: "Ejecución, licitación, adjudicación, contratación y garantías."
    - ID: GN-FRIL-SEC-14-RENDICIONES-INFORMES
      Cpt: "Rendiciones, informes y proyectos sin adjudicación."
    - ID: GN-FRIL-SEC-15-MODIFICACIONES-TERMINO
      Cpt: "Modificaciones de contrato, término de proyecto y vigencia del instructivo."
    - ID: GN-FRIL-SEC-16-ANEXOS
      Cpt: "Anexos operativos: checklist, planillas tipo y certificados."

  Sec_1_Resolucion_Exenta:
    ID: GN-FRIL-SEC-1-RESOLUCION
    Encabezado:
      ID: GN-FRIL-RES-ENCABEZADO-01
      Cpt: "Resolución Exenta que aprueba instructivo FRIL 2025."
      Numero: "4A/00894/16.05.2025"
      Purp: "Aprobar instructivo para formulación y evaluación de iniciativas FRIL, año presupuestario 2025."
    Vistos:
      ID: GN-FRIL-RES-VISTOS-01
      Cpt: "Marco normativo que sustenta la resolución."
      Fnd:
        - Ref: GN-FRIL-NORM-CPR-01
          Detalle: "Constitución Política de la República, Artículo 111°."
        - Ref: GN-FRIL-NORM-LOC-GORE-01
          Cpt: "Atribuciones del Gobernador Regional."
          Act:
            - "Dictar resoluciones e instrucciones necesarias para la administración regional."
          Ref_Normativa:
            - "Art. 24, letra ñ, LOC GORE."
        - Ref: GN-FRIL-NORM-LEY-21074-01
        - Ref: GN-FRIL-NORM-LEY-18575-01
        - Ref: GN-FRIL-NORM-LEY-21796-01
          Ctx: "Partida 31 Gobiernos Regionales, Glosas Comunes programa 02 Inversión Regional."
        - Ref: GN-FRIL-NORM-LEY-19880-01
        - Ref: GN-FRIL-NORM-DL575-01
          Cpt: "FNDR como instrumento financiero de inversión pública de decisión regional y fuente flexible para los GORE."
        - Ref: GN-FRIL-NORM-RES36-CGR-2024-01
          Ctx: "Normas sobre exención del trámite de Toma de Razón."
        - Ref: GN-FRIL-NORM-CIRC11-HACIENDA-2025-01
        - Ref: GN-FRIL-NORM-RES15051-SUBDERE-2023-01
          Ctx: "Fija Guía Operativa FRIL nacional."
        - Cpt: "Resoluciones internas del GORE Ñuble sobre estructura organizacional y procedimientos."
        - Cpt: "Documentos de proclamación y nombramiento del Gobernador Regional para el período 2025-2029."
    Considerandos:
      ID: GN-FRIL-RES-CONSIDERANDOS-01
      Cpt: "Razones que justifican la emisión del instructivo FRIL 2025."
      Just:
        - "El presupuesto de Inversión Regional es instrumento fundamental para el desarrollo social, cultural y económico regional."
        - "Acuerdo del CORE para aprobar el Instructivo del Fondo Regional de Iniciativa Local (FRIL) 2025 (Sesión N°158, 09/04/2025, Certificado N°1177/2025)."
        - "Visación de la metodología de evaluación FRIL por parte de SUBDERE (Oficio N°1667/2025)."
        - "Acuerdo del CORE para modificar el plazo de postulación de proyectos FRIL 2025 (Sesión N°86, 14/05/2025, Certificado N°1198/2025)."
        - "Necesidad de orientaciones técnicas y administrativas para optimizar el trabajo con eficiencia y eficacia."
        - "Necesidad de unificar normas vigentes para el buen uso de los recursos públicos."
      Vigencia_Instructivo:
        Nat: "Indefinida hasta modificación por nueva resolución exenta."
    Resuelvo:
      ID: GN-FRIL-RES-RESUELVO-01
      Act:
        - "Aprobar el texto del Instructivo Concurso Postulación FRIL 2025 para financiamiento FNDR."
        - "Adjuntar certificados del CORE y oficio de visación de SUBDERE como parte integrante de la resolución."
        - "Ordenar la publicación de la resolución e instructivo en el sitio web del GORE Ñuble y en el portal de transparencia activa."

  Sec_2_Introduccion_y_Marco_Programa:
    ID: GN-FRIL-SEC-2-INTRO
    Introduccion_Programa_FRIL:
      ID: GN-FRIL-INTRO-01
      Cpt: "Programa FRIL."
      Def: "Mecanismo de financiamiento para proyectos de inversión en infraestructura comunal de menor escala."
      Obj:
        - "Elevar la calidad de vida de los habitantes de las comunas de la Región de Ñuble (urbano y rural)."
      Mech:
        - "Transferencia de recursos FNDR a municipalidades para ejecución de proyectos."
      Fnd:
        - Ref: GN-FRIL-NORM-LEY-21796-01
          Ctx: "Asignación presupuestaria anual en Ley de Presupuestos."
      Proc:
        - Act: "Municipios formulan y presentan iniciativas."
        - Act: "GORE evalúa iniciativas según Guía Operativa SUBDERE y lineamientos del instructivo regional."
        - Resp: "GORE regula la distribución de recursos, con validación del CORE."
    Objetivo_Fondo_FRIL:
      ID: GN-FRIL-OBJ-FONDO-01
      Obj: |
        Financiar proyectos de infraestructura comunal de menor tamaño que mejoren la calidad de vida de la población, tanto en zonas urbanas
        como rurales, priorizando iniciativas con alto impacto social y territorial.
      Acciones_Financiables:
        - "Ejecución de infraestructura pública."
        - "Mantenimiento de infraestructura pública."
        - "Conservación de infraestructura pública."
        - Ctx: "Incluye infraestructura social y deportiva."
      Fnd:
        - Ref: GN-FRIL-NORM-LEY-21796-01
          Ctx: "Glosa 12, Subtítulo 33, Programa 02."
    Marco_Legal_Programa:
      ID: GN-FRIL-MARCO-LEGAL-01
      Cpt: "Normativa que rige el programa FRIL 2025."
      Fnd:
        - Ref: GN-FRIL-NORM-LOC-GORE-01
        - Ref: GN-FRIL-NORM-LEY-18575-01
        - Ref: GN-FRIL-NORM-LEY-21796-01
        - Ref: GN-FRIL-NORM-RES15051-SUBDERE-2023-01
        - Ref: GN-FRIL-NORM-CIRC11-HACIENDA-2025-01

  Sec_3_Monto_y_Marco_a_Postular:
    ID: GN-FRIL-SEC-3-MONTO-MARCO
    Monto_Maximo_Proyecto:
      ID: GN-FRIL-MONTO-MAX-01
      Req:
        - "Monto máximo por proyecto: igual o inferior a 4.545 UTM (valorizada al 01.01.2025)."
        - "Equivalente aproximado: $306.464.805 CLP."
      Just:
        - "Se descuenta un 10% del máximo normativo de 5.000 UTM para cubrir posibles aumentos de obra."
    Monto_Minimo_Proyecto:
      ID: GN-FRIL-MONTO-MIN-01
      Req:
        - "Monto mínimo por proyecto: $100.000.000 CLP."
    Marco_Por_Comuna:
      ID: GN-FRIL-MARCO-COMUNA-01
      Req:
        - "Postulación habilitada para las 21 comunas de la Región de Ñuble."
        - "Cada comuna puede postular hasta 5 iniciativas en el período regular."
        - "Monto total máximo a postular por comuna en período regular: M$1.000.000."
    Llamados_Extraordinarios:
      ID: GN-FRIL-LLAMADOS-EXTRA-01
      Cond:
        - "El GORE podrá desarrollar llamados extraordinarios por áreas temáticas o por emergencias."
      Mech:
        - "Los llamados se informan a las municipalidades por oficio."
        - "Requieren resolución exenta previa que defina marco, montos, justificación y plazos."
    Prioridades_GORE:
      ID: GN-FRIL-PRIORIDADES-01
      Rec:
        - "Priorizar proyectos con alto impacto social y territorial."
        - "Priorizar proyectos integrados con otras soluciones presentes en el territorio."

  Sec_4_Lineamientos_de_Postulacion:
    ID: GN-FRIL-SEC-4-LINEAMIENTOS
    Acciones_Financiables:
      ID: GN-FRIL-ACC-FINANCIABLES-01
      Cpt: "Obras civiles FRIL."
      Act:
        - "Construcción."
        - "Reposición."
        - "Mejoramiento."
        - "Habilitación."
        - "Normalización."
        - "Ampliación."
    Categorias_Proyecto:
      ID: GN-FRIL-CATEGORIAS-01
      Req:
        - "Cada proyecto debe definirse en una sola categoría (la más relevante)."
        - "Cada comuna debe presentar al menos un proyecto asociado a los ejes regionales de Salud, Seguridad o Reactivación Económica."
      Tabla_Categorias:
        ID: GN-FRIL-CATEGORIAS-TABLA-01
        Ctx: "Resumen estructurado de categorías y subcategorías del instructivo."
        Grupos:
          - Cpt: "A - Desarrollo Territorial"
            Subcategorias:
              - ID: GN-FRIL-CAT-A1
                Cpt: "Integración Rural"
                Def: "Infraestructura de servicios básicos y conectividad para zonas alejadas."
              - ID: GN-FRIL-CAT-A2
                Cpt: "Acceso al Agua"
                Ex: "Sistemas APR, sistemas de impulsión/tratamiento/distribución, alcantarillado comunitario y pluvial."
              - ID: GN-FRIL-CAT-A3
                Cpt: "Vial"
                Ex: "Aceras, baches, calles, caminos, cunetas, veredas, supresor de polvo, barreras de contención."
          - Cpt: "B - Servicios"
            Subcategorias:
              - ID: GN-FRIL-CAT-B1
                Cpt: "Edificación Pública"
                Ex: "Postas, centros de salud, escuelas, patios cubiertos, cuarteles de bomberos."
              - ID: GN-FRIL-CAT-B2
                Cpt: "Gestión de Riesgos"
                Ex: "Muros de contención, drenajes, cortafuegos, desbroce."
              - ID: GN-FRIL-CAT-B3
                Cpt: "Seguridad"
                Ex: "Luminarias, televigilancia, cierres perimetrales, refugios peatonales, fibra óptica."
          - Cpt: "C - Desarrollo Social y Económico"
            Subcategorias:
              - ID: GN-FRIL-CAT-C1
                Cpt: "Inclusión"
                Ex: "Infraestructura inclusiva, centros de terapia, centros de adulto mayor."
              - ID: GN-FRIL-CAT-C2
                Cpt: "Género"
                Ex: "Centros de acogida para víctimas de violencia, casas de protección."
              - ID: GN-FRIL-CAT-C3
                Cpt: "Turismo"
                Ex: "Pórticos, senderos turísticos, bordes costeros, miradores, señalética."
          - Cpt: "D - Medio Ambiente"
            Subcategorias:
              - ID: GN-FRIL-CAT-D1
                Cpt: "Deportes"
                Ex: "Canchas, multicanchas, estadios, piscinas, pistas de trote, plazas activas."
              - ID: GN-FRIL-CAT-D2
                Cpt: "Áreas Verdes"
                Ex: "Paseos peatonales, plazas, parques, juegos de agua."
              - ID: GN-FRIL-CAT-D3
                Cpt: "Sustentabilidad"
                Ex: "Paneles solares, energía eólica, riego eficiente, áreas verdes con reciclaje y compostaje."
    Reglas_Especiales_Postulacion:
      ID: GN-FRIL-REGLAS-ESPECIALES-01
      Excepcion_Conteo_Proyectos:
        Cpt: "Excepción al máximo de 5 iniciativas por comuna."
        Cond:
          - "Proyectos en categorías A2 (Acceso al Agua) y A3 (Vial) no se contabilizan dentro del máximo de 5 proyectos."
        Just:
          - "El acceso al agua y el mejoramiento de caminos son fundamentales para el desarrollo regional."
        Dep:
          - "Aplicación sujeta a disponibilidad de revisión por parte de la unidad revisora FRIL del GORE."
      Proyectos_Multiubicacion:
        ID: GN-FRIL-MULTIUBICACION-01
        Cond:
          - "Un proyecto puede considerar múltiples ubicaciones dentro de la comuna."
        Req:
          - "Las ubicaciones deben compartir naturaleza, alcance y objetivo."
          - "Debe existir un solo presupuesto y una sola licitación para el conjunto."

  Sec_5_Prohibiciones_Postulacion:
    ID: GN-FRIL-SEC-5-PROHIBICIONES
    Prohibiciones_Generales:
      ID: GN-FRIL-PROHIB-GRALES-01
      Prohib:
        - "Financiar gastos en personal, bienes y servicios de consumo de municipalidades."
        - "Adquirir o reponer activos no financieros que no formen parte de un proyecto de obras civiles."
        - "Financiar proyectos de servicios básicos que incluyan instalaciones domiciliarias privadas."
        - "Financiar proyectos con fines de lucro."
        - "Financiar proyectos por etapas (fraccionamiento de obras)."
        - "Financiar dos o más proyectos en un mismo terreno o mismo tramo de BNUP en el mismo año presupuestario."
        - "Financiar dos o más proyectos para la misma actividad/uso en un mismo terreno en años distintos, si el primero no está ejecutado totalmente."
      Criterios_Terreno_y_Tramo:
        Cpt: "Definición administrativa de terreno y tramo."
        Ctx:
          - "El terreno se identifica por el mismo rol de avalúo."
          - "El tramo vial se verifica con coordenadas y archivos KMZ, a criterio del GORE."
      Vinculo_ERD:
        ID: GN-FRIL-PROHIB-ERD-01
        Prohib:
          - "Postular proyectos que no indiquen su relación con la Estrategia Regional de Desarrollo de Ñuble 2020–2028 en el oficio conductor."

  Sec_6_Situaciones_Especiales_de_Terrenos:
    ID: GN-FRIL-SEC-6-TERRENOS
    Proyectos_en_Terrenos_Privados:
      ID: GN-FRIL-TERRENOS-PRIVADOS-01
      Cond:
        - "Se permiten proyectos en terrenos privados bajo condiciones específicas que resguarden el uso público y la vida útil de las obras."
    Proyectos_Ley_Indigena:
      ID: GN-FRIL-TERRENOS-LEY-INDIGENA-01
      Cond:
        - "Proyectos de infraestructura social o deportiva en inmuebles que son bienes comunes de comunidades conformadas según Ley N° 19.253."
      Req:
        - "Certificación de tenencia/posesión emitida por el Alcalde."
        - "Certificado de CONADI que acredite la condición de comunidad indígena."
    Personas_Juridicas_Sin_Fines_de_Lucro:
      ID: GN-FRIL-TERRENOS-PJ-SFL-01
      Req:
        - "Acreditar calidad de persona jurídica sin fines de lucro, con documento municipal que indique directiva vigente."
        - "Acreditar que el privado otorga a la municipalidad el uso y goce de la propiedad por un período no inferior a la vida útil de las obras (usufructo o comodato)."
        - "Presentar escritura pública inscrita en el Conservador de Bienes Raíces, incorporando la prohibición de enajenar por al menos 20 años."
        - "Adjuntar certificado simple de la unidad jurídica municipal que respalde la información legal de la propiedad."
      Control_GORE:
        Cpt: "Control jurídico adicional del GORE."
        Mech:
          - "El departamento jurídico del GORE podrá realizar análisis adicionales y solicitar más antecedentes si existen dudas."

  Sec_7_Periodos_y_Plazos:
    ID: GN-FRIL-SEC-7-PLAZOS
    Difusion:
      ID: GN-FRIL-PLAZOS-DIFUSION-01
      Dln:
        - "Desde la aprobación del marco presupuestario y durante todo el año 2025."
    Postulacion:
      ID: GN-FRIL-PLAZOS-POSTULACION-01
      Llamados:
        - Cpt: "1er Llamado"
          Dln: "Desde la aprobación administrativa del instructivo hasta 30 días corridos posteriores."
        - Cpt: "2do Llamado"
          Dln: "Desde el 01 de septiembre al 30 de septiembre de 2025."
    Evaluacion:
      ID: GN-FRIL-PLAZOS-EVAL-01
      Dln:
        - "Desde el 01 de marzo de 2025 al 12 de diciembre de 2025."
      Warn:
        - "Iniciativas sin aprobación técnica a esa fecha serán calificadas como NO VIGENTE."
    Asesoria_Tecnica:
      ID: GN-FRIL-PLAZOS-ASESORIA-01
      Mech:
        - "Acompañamiento metodológico durante todo el año por parte de profesionales del Depto. de Análisis y Evaluación."
        - "Para colaboración adicional, los municipios deben enviar correo al coordinador del Depto. (dato de contacto en instructivo)."
    Otras_Convocatorias:
      ID: GN-FRIL-PLAZOS-OTRAS-CONVOC-01
      Cond:
        - "Pueden desarrollarse convocatorias adicionales asociadas a Provisiones FNDR u otras materias específicas."
      Mech:
        - "Se elaborará resolución exenta del Gobernador Regional con lineamientos, montos y plazos específicos."

  Sec_8_Etapas_y_Procesos_FRIL:
    ID: GN-FRIL-SEC-8-PROCESO
    Ingreso_Iniciativas:
      ID: GN-FRIL-PROC-INGRESO-01
      Mech:
        - "Ingreso de iniciativas vía banner 'FRIL' en la página web del GORE Ñuble, utilizando las credenciales de GESDOC."
      Req:
        - "Usuarios deben estar habilitados con clave única y autorizados por su institución ante el administrador de GESDOC."
        - "Al presentar oficio y ficha IDI, todos los archivos requeridos para admisibilidad deben estar cargados en el BIP."
      Res:
        - "El incumplimiento de estos requisitos implica INADMISIBLE."
    Admisibilidad:
      ID: GN-FRIL-PROC-ADMISIBILIDAD-01
      Def: "Revisión formal de completitud de antecedentes y cumplimiento de requisitos mínimos del instructivo y la Guía Operativa."
      Cond:
        - "Serán inadmisibles las postulaciones fuera de plazo o que incluyan prohibiciones expresas del instructivo FRIL."
    Etapa_Revision_y_RATE:
      ID: GN-FRIL-PROC-REVISION-01
      Dln:
        - "El GORE dispondrá de un máximo de 60 días hábiles para emitir el primer Resultado de Análisis Técnico-Económico (RATE) desde el ingreso de antecedentes completos."
      Res:
        - "El análisis genera un acta de evaluación con resultados posibles: Recomendado (RS) o No Recomendado (FI, OT, NV, IN)."
      Resultado_RS:
        ID: GN-FRIL-PROC-RS-01
        Def: "Recomendado Satisfactoriamente."
        Cond:
          - "Se otorga cuando la iniciativa cumple con todos los antecedentes administrativos, técnicos y normativa vigente."
        Res:
          - "Emisión de certificado RS, acta de evaluación, presupuesto final y ficha IDI aprobada."
          - "Habilita la iniciativa para ser presentada a aprobación de financiamiento, sujeta a disponibilidad presupuestaria."
        Vigencia_RS:
          Dln:
            - "Vigente para el año en que se obtiene."
            - "El municipio dispone de 90 días desde la firma del convenio para presentar licitación; de lo contrario, se pierde vigencia de la aprobación técnica."
      Resultado_No_Recomendado:
        ID: GN-FRIL-PROC-NR-01
        Tipos:
          - Cpt: "FI (Falta Información)"
            Cond: "Faltan antecedentes, existen errores de cálculo o se requieren ajustes subsanables."
          - Cpt: "OT (Objetado Técnicamente)"
            Cond: "Iniciativa mal formulada o con problemas técnicos/normativos insubsanables."
          - Cpt: "NV (No Vigente)"
            Cond:
              - "No se cumplen plazos de subsanación."
              - "El municipio informa que el proyecto ya no es de interés o se financió por otra vía."
          - Cpt: "IN (Incumplimiento de Normativa)"
            Cond:
              - "Se asignan recursos, adjudica, ejecuta gasto o se modifican archivos en BIP después de la aprobación técnica sin informe favorable del GORE."
            Warn:
              - "Esta situación será considerada falta en futuras postulaciones."
        Dln:
          - "Plazo para subsanar observaciones FI/OT: máximo 30 días hábiles, prorrogables a criterio del analista."

  Sec_9_Documentacion_para_Postulacion:
    ID: GN-FRIL-SEC-9-DOC-POSTULACION
    Ref_Checklist:
      Src: "DOC-GORE-NUBLE-FRIL-2025-ANEXO-01-CHECKLIST"
      Ctx: "El instructivo detalla un checklist exhaustivo de documentos obligatorios. Este artefacto sintetiza sus requisitos clave."
    Oficio_Conductor:
      ID: GN-FRIL-DOC-OFICIO-01
      Req:
        - "Oficio del Alcalde(sa) al Gobernador Regional, firmado y registrado en GESDOC y BIP."
        - "Incluir nombre del proyecto concordante con ficha IDI y código BIP."
        - "Indicar relación con Estrategia Regional de Desarrollo (Ejes, Lineamientos)."
        - "Indicar relación con PLADECO Comunal (Eje, Lineamiento, Acción)."
        - "Especificar tipología (FRIL) y año presupuestario."
    Ficha_IDI:
      ID: GN-FRIL-DOC-IDI-01
      Req:
        - "Ficha IDI descargada desde BIP del año presupuestario en ejercicio (2025)."
        - "Indicar Subtítulo 33 e inversión menor a 5.000 UTM."
        - "Toda la información debe ser coherente con el proyecto postulado."
    Fotografias_y_Localizacion:
      ID: GN-FRIL-DOC-FOTOS-01
      Req:
        - "Mínimo 4 fotografías de la situación actual y su entorno, con descripción y antigüedad menor a 6 meses."
        - "Para proyectos viales, al menos 3 fotos de tramos representativos."
        - "Incluir localización con coordenadas UTM (Huso 18 Sur, Datum WGS84)."
        - "Adjuntar archivo digital de ubicación en formato KML o KMZ."
    Especificaciones_Tecnicas:
      ID: GN-FRIL-DOC-EETT-01
      Req:
        - "Especificaciones detalladas (materialidad, dimensiones, métodos de ejecución)."
        - "Itemizado de partidas coherente con presupuesto."
        - "Firmadas por profesional competente y Director(a) SECPLA."
    Presupuesto_Obras:
      ID: GN-FRIL-DOC-PPTO-01
      Req:
        - "Presupuesto ingresado en BIP y GESDOC en formato PDF y Excel."
        - "Desglose por partidas (cantidad, precio unitario), gastos generales, utilidades e IVA."
        - "Planilla de cubicaciones por partida."
        - "Firmado por profesional competente y Alcalde(sa)."
        - "El analista del GORE puede solicitar análisis de precio unitario (APU) cuando corresponda."
    Certificacion_Propiedad:
      ID: GN-FRIL-DOC-PROPIEDAD-01
      Casuistica:
        - Cpt: "Caso A – Terreno Municipal"
          Req:
            - "Escritura de la propiedad."
            - "Certificado de Dominio Vigente con Hipotecas y Gravámenes (vigencia máxima 60 días)."
        - Cpt: "Caso B – BNUP administrado por municipio"
          Req:
            - "Certificado DOM que acredite condición de BNUP (parques, plazas, calles)."
        - Cpt: "Caso C – BNUP no administrado por municipio"
          Req:
            - "Concesión, autorización de uso o proyecto aprobado por la entidad responsable del BNUP."
        - Cpt: "Caso D – Caminos Vecinales"
          Req:
            - "Documentos que acrediten cumplimiento del Decreto 293/2008 del MOP."
        - Cpt: "Caso E – Terreno Privado (Comodato/Usufructo)"
          Req:
            - "Escritura de usufructo o contrato de comodato inscrito en CBR, con prohibición de enajenar por período no inferior a vida útil de obras."
    Otros_Documentos_Claves:
      ID: GN-FRIL-DOC-OTROS-01
      Incluye:
        - "Certificado Compromiso Operación y Mantención (con costos mensuales/anuales y vida útil)."
        - "Certificados de Factibilidad Eléctrica/Sanitaria."
        - "Permiso o Anteproyecto de Edificación o Informe Técnico OGUC, según corresponda."
        - "Títulos profesionales o patentes de responsables técnicos."
        - "Render o imágenes objetivo de obras."
        - "Planimetría completa (ubicación, emplazamiento, arquitectura, especialidades, topografía)."
        - "Proyecto de Ingeniería si normativa lo exige."
        - "Certificados de Participación Ciudadana."
        - "Certificados de Pertinencia Técnica según tipo de proyecto."
      Tabla_Pertinencia_Tecnica:
        ID: GN-FRIL-TABLA-PERT-01
        Purp: "Tabla referencial de qué servicio o municipalidad emite el certificado de pertinencia técnica según tipo de proyecto."
        Src:
          - "kb_gn_026_guia_fril_sts.md – Sección 2.10.15."
        Filas:
          - Tipo_Proyecto: "Proyectos deportivos de uso formativo o competitivo"
            Servicio_Responsable: "Instituto Nacional de Deportes"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos deportivos de uso recreativo"
            Servicio_Responsable: "Municipalidad"
            Tipo_Pertinencia: "Pertinencia Municipal"
          - Tipo_Proyecto: "Obras de infraestructura educacional"
            Servicio_Responsable: "SEREMI de Educación"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Obras de infraestructura de salud"
            Servicio_Responsable: "SEREMI de Salud"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural"
            Servicio_Responsable: "Dirección de Obras Hidráulicas"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural"
            Servicio_Responsable: "Empresa sanitaria"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de obras viales urbanos"
            Servicio_Responsable: "Servicio de Vivienda y Urbanismo"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de obras viales rurales"
            Servicio_Responsable: "Dirección de Vialidad"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Obras en cauces de ríos"
            Servicio_Responsable: "Dirección de Obras Hidráulicas"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Obras en cauces de ríos"
            Servicio_Responsable: "Asociación de Canalistas"
            Tipo_Pertinencia: "Pertinencia de institución"
          - Tipo_Proyecto: "Proyectos de señalética vial en área urbana"
            Servicio_Responsable: "SEREMI de Transporte y Telecomunicaciones"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de señalética turística vial área urbana y rural"
            Servicio_Responsable: "SERNATUR"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Proyectos de alumbrado público"
            Servicio_Responsable: "Seremi de Energía"
            Tipo_Pertinencia: "Pertinencia Servicio"
          - Tipo_Proyecto: "Áreas verdes municipales"
            Servicio_Responsable: "Municipalidad"
            Tipo_Pertinencia: "Pertinencia Municipal"
      Tabla_Visacion_Servicios:
        ID: GN-FRIL-TABLA-VISACION-01
        Purp: "Tabla referencial de qué servicio debe visar qué tipo de obra FRIL."
        Src:
          - "kb_gn_026_guia_fril_sts.md – Sección 2.10.16."
        Filas:
          - Tipo_Proyecto: "Proyectos deportivos de uso formativo o competitivo"
            Servicio_Responsable: "Instituto Nacional de Deportes"
            Proyectos_Que_Contemplan_Visacion: "Construcción o reposición de: Gimnasios, Multicanchas, Piscinas, Estadios, Canchas de tenis, Camarines, Graderías, Techos, Multicanchas, Medialunas, Entre otros."
          - Tipo_Proyecto: "Obras de infraestructura educacional"
            Servicio_Responsable: "SEREMI de Educación"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición: Salas de clases, Laboratorios, Entre otros."
          - Tipo_Proyecto: "Obras de infraestructura de salud"
            Servicio_Responsable: "Servicio de Salud de Ñuble"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Establecimientos de salud, Entre otros."
          - Tipo_Proyecto: "Obras de infraestructura de salud"
            Servicio_Responsable: "SEREMI de Salud"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Alcantarillado, Agua potable área urbana, Agua potable área rural, Entre otros."
          - Tipo_Proyecto: "Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural"
            Servicio_Responsable: "Dirección de Obras Hidráulicas"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Agua potable área rural, Entre otros."
          - Tipo_Proyecto: "Proyectos de construcción o extensión de redes de alcantarillado y/o agua potable área urbana o rural"
            Servicio_Responsable: "Empresa sanitaria"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Agua potable área urbana, Entre otros."
          - Tipo_Proyecto: "Proyectos de obras viales urbanos"
            Servicio_Responsable: "Servicio de Vivienda y Urbanismo"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Pavimentos, Aceras, Evacuación de aguas lluvias, Aceras, Muros de contención, Puentes, etc."
          - Tipo_Proyecto: "Proyectos de obras viales rurales"
            Servicio_Responsable: "Dirección de Vialidad"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Pavimentos, Evacuación de aguas lluvias, Aceras, Muros de contención, Puentes, Refugios peatonales, etc."
          - Tipo_Proyecto: "Pronunciamiento sobre instalaciones u obras cuyo emplazamiento requiera ocupar los terrenos de faja vial de un camino público rural"
            Servicio_Responsable: "Dirección de Vialidad (paralelismos)"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Alumbrado público."
          - Tipo_Proyecto: "Obras en cauces de ríos"
            Servicio_Responsable: "Dirección General de Aguas"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros."
          - Tipo_Proyecto: "Obras en cauces de ríos"
            Servicio_Responsable: "Dirección de Obras Hidráulicas"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros."
          - Tipo_Proyecto: "Obras en cauces de ríos"
            Servicio_Responsable: "Asociación de Canalistas"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Obras de cauces de ríos, Entre otros."
          - Tipo_Proyecto: "Proyectos de señalética vial en área urbana"
            Servicio_Responsable: "SEREMI de Transporte y Telecomunicaciones"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación (siempre que exista modificación de lo señalado en Manual de Señalética Vial): Semáforos, Demarcaciones viales, Señalética, Entre otros."
          - Tipo_Proyecto: "Proyectos de señalética vial en área urbana"
            Servicio_Responsable: "Dirección de Tránsito Municipal"
            Proyectos_Que_Contemplan_Visacion: "Construcción, reposición, mejoramiento, habilitación, normalización, ampliación: Semáforos, Demarcaciones viales, Señalética, Entre otros."
          - Tipo_Proyecto: "Proyectos de alumbrado público (cuando corresponda)"
            Servicio_Responsable: "Seremi de Energía"
            Proyectos_Que_Contemplan_Visacion: "Reposición, mejoramiento, habilitación, normalización, ampliación (masivo): Alumbrado público (calles urbanas, rutas de vialidad, etc.), Alumbrado en plazas y áreas verdes."
          - Tipo_Proyecto: "Proyectos que requieran declaraciones o estudios de impacto ambiental"
            Servicio_Responsable: "Servicio de Evaluación Ambiental"
            Proyectos_Que_Contemplan_Visacion: "Consulta de Pertinencia, considerando lo indicado en artículo 26 del D.S. 40 de 2012 del Ministerio del Medio Ambiente (Reglamento del SEIA)."

  Sec_10_Otras_Consideraciones:
    ID: GN-FRIL-SEC-10-OTRAS-CONSID
    Activos_No_Financieros:
      ID: GN-FRIL-OTRAS-ACTIVOS-NF-01
      Cond:
        - "Se puede financiar mobiliario, equipamiento y equipos informáticos como parte de un proyecto de infraestructura FRIL."
      Req:
        - "Solo unidades necesarias para la puesta en funcionamiento del recinto."
        - "Costo acumulado no debe superar el 10% del costo total del proyecto (salvo casos especiales de alumbrado público o infraestructura deportiva, evaluados caso a caso)."
        - "Costo se imputa a obras civiles y se incluye como partida en presupuesto."
        - "Detalle de activos con al menos tres cotizaciones formales y cuadro comparativo técnico."
      Prohib:
        - "No se pueden adquirir activos no financieros que no sean parte del proyecto de obras civiles."
    Tramitacion_Autorizaciones:
      ID: GN-FRIL-OTRAS-AUTORIZACIONES-01
      Resp:
        - "Municipio es responsable de tramitar todas las autorizaciones de servicios competentes."
      Req:
        - "Autorizaciones deben presentarse junto con el expediente para obtener recomendación técnica."
        - "Proyectos APR deben incluir memoria de cálculo de agua potable y torre de agua."
        - "Proyectos de ampliación/remodelación requieren que edificación existente cuente con permiso de edificación y recepción final."
        - "Todos los proyectos deben incorporar Accesibilidad Universal conforme OGUC y DS50."
    De_la_Revision:
      ID: GN-FRIL-OTRAS-REVISION-01
      Purp: "Precisar facultades de revisión del analista del GORE durante todo el proceso y el uso de visitas a terreno como parte del análisis."
      Mech:
        - "El profesional analista del GORE puede formular nuevas observaciones durante todo el proceso de revisión, incluso después de subsanaciones anteriores."
      Req:
        - "El analista debe, cuando la disponibilidad presupuestaria y de recursos lo permita, realizar visitas a terreno para revisar la integralidad del proyecto."
      Resp:
        - "La División de Desarrollo Regional, a través de sus analistas, entregará asesoría técnica permanente a las municipalidades en la etapa de revisión."

  Sec_11_Reevaluaciones:
    ID: GN-FRIL-SEC-11-REEVALUACIONES
    Solicitud_Reevaluacion:
      ID: GN-FRIL-REEVAL-SOLICITUD-01
      Dln:
        - "Puede solicitarse desde 60 días después de la aprobación técnica y hasta 30 días corridos antes del término del plazo contractual de ejecución."
      Req:
        - "Solicitud dirigida al GORE con resumen ejecutivo, informe ITO GORE (si obra en ejecución) y respaldos (presupuestos, cotizaciones, Carta Gantt)."
      Resp:
        - "Unidad responsable depende de la etapa: Depto. de Presupuesto (desde creación presupuestaria hasta adjudicación) y Depto. de Inversiones (desde adjudicación hasta recepción definitiva)."
      Dln_Subsanar:
        - "Plazo para subsanar observaciones de reevaluación: máximo 30 días corridos."
    Casos_No_Acepta_Reevaluacion:
      ID: GN-FRIL-REEVAL-NO-ACEPTA-01
      Prohib:
        - "Modificaciones menores que pueden registrarse en libro de obras."
        - "Cambios significativos del objetivo del proyecto (alcances, finalidad)."
        - "Cambios de materialidad no justificados por habitabilidad o correcta ejecución."
        - "Aumento de obras sobre el 10% del monto original o sobre 5.000 UTM."
        - "Cambios de ubicación que impliquen cambio de rol, salvo que mantengan objetivo y se presenten todos los antecedentes del nuevo emplazamiento para nueva recomendación técnica."
    Evaluacion_Segun_Instructivo_Vigente:
      ID: GN-FRIL-REEVAL-VIGENCIA-01
      Mech:
        - "Las reevaluaciones se analizan respecto al instructivo vigente."
        - "Si un punto no está en instructivo vigente, se aplica el del año en que se aprobó la iniciativa."

  Sec_12_Transferencia_de_Recursos:
    ID: GN-FRIL-SEC-12-TRANSFERENCIAS
    Solicitud_Financiamiento:
      ID: GN-FRIL-TRANSF-SOL-01
      Proc:
        - "Una vez que la iniciativa cuenta con RS, se elabora resolución que incorpora el proyecto al marco presupuestario."
        - "El Gobernador Regional aprueba el financiamiento e instruye a DIPIR a continuar con el proceso."
    Convenio_Transferencia:
      ID: GN-FRIL-TRANSF-CONVENIO-01
      Resp:
        - "Depto. de Presupuestos gestiona la creación presupuestaria y suscripción del convenio GORE-Municipio."
      Contenido_Minimo:
        - "Detalle de ítems de gasto."
        - "Modalidad de ejecución."
        - "Requisitos para modificaciones y transferencias de recursos."
        - "Derechos y obligaciones de las partes."
        - "Reglas de administración financiera y restricciones."
        - "Forma y oportunidad de rendiciones."
        - "Reglas de devolución de recursos."
        - "Especificaciones para señaléticas y placas."
        - "Proceso de cierre administrativo."
        - "Anexo con presupuesto detallado aprobado."
    Transferencia_a_Municipios:
      ID: GN-FRIL-TRANSF-MUNICIPIOS-01
      Mech:
        - "Transferencia se realiza según programación financiera presentada por el municipio y avance efectivo de obras, avalado por ITO GORE."
      Req:
        - "Recursos se depositan en cuenta corriente exclusiva para fondos FNDR."
        - "Primera transferencia se efectúa tras la entrega de antecedentes establecidos en el convenio."
        - "Transferencias posteriores se condicionan a rendiciones mensuales y avance de obra."

  Sec_13_Ejecucion_Proyecto_FRIL:
    ID: GN-FRIL-SEC-13-EJECUCION
    Modelos_Ejecucion:
      ID: GN-FRIL-EJEC-MOD-01
      Cpt: "La ejecución se rige por normativa de Municipalidades y Ley de Compras Públicas."
      Mdl:
        - "Ejecución Directa: la municipalidad ejecuta con sus propios procedimientos."
        - "Administración Delegada: la municipalidad supervisa técnica, administrativa y financieramente todo el proyecto ejecutado por terceros."
        - "Licitación Pública: modalidad principal para ejecución de obras FRIL."
      Licitacion_Publica:
        ID: GN-FRIL-EJEC-LICITACION-01
        Dln:
          - "Municipio debe llamar a propuesta en un plazo máximo de 45 días corridos desde la resolución que aprueba el convenio."
        Warn:
          - "El incumplimiento puede significar la reasignación de fondos."
          - "Si a los 90 días corridos desde el convenio no se ha licitado, la iniciativa pierde su recomendación técnica."
        Req:
          - "Municipio debe nombrar Inspector Técnico de Obra (ITO) competente (ingeniero civil, ingeniero constructor, constructor civil, arquitecto)."
      Adjudicacion:
        ID: GN-FRIL-EJEC-ADJUDICACION-01
        Cond:
          - "Municipio puede adjudicar si la oferta no supera el monto aprobado por el GORE."
        Proc:
          - "Si la mejor oferta supera el monto aprobado, tras al menos 3 llamados a licitación, el municipio puede solicitar aumento de presupuesto al GORE."
        Cond_Adicional:
          - "Aumento debe estar dentro del 10% del monto original y ajustarse a reglas de reevaluación FRIL."
      Contratacion:
        ID: GN-FRIL-EJEC-CONTRATACION-01
        Dln:
          - "La contratación debe decretarse en un máximo de 20 días desde el acto que aprueba la adjudicación."
        Warn:
          - "El incumplimiento faculta al GORE para reasignar los fondos."
        Req:
          - "Contratación bajo modalidad de suma alzada, sin reajustes ni intereses."
          - "Municipio debe remitir al GORE todos los antecedentes de adjudicación en un plazo no mayor a 15 días desde la entrega de terreno."
      Garantias:
        ID: GN-FRIL-EJEC-GARANTIAS-01
        Mech:
          - "Municipio puede exigir garantías por seriedad de la oferta, fiel cumplimiento de contrato y correcta ejecución."
        Mdl:
          - "Boletas de garantía bancaria, vale vista u otras modalidades permitidas por ley."
        Req:
          - "Garantía de fiel cumplimiento: mínimo 10% del monto del contrato, con vigencia plazo contractual + 90 días."
          - "Garantía de correcta ejecución: mínimo 5%, con vigencia de 365 días desde la recepción provisoria sin observaciones."
        Resp:
          - "Es responsabilidad exclusiva de la Municipalidad mantener vigentes las garantías."

  Sec_14_Rendiciones_e_Informes:
    ID: GN-FRIL-SEC-14-RENDICIONES-INFORMES
    Rendiciones:
      ID: GN-FRIL-RENDICIONES-01
      Cpt: "Rendición de recursos FRIL transferidos a municipalidades."
      Req:
        - "Los recursos FRIL no se incorporan al presupuesto municipal; se rinden a CGR y al GORE."
        - "Rendición conforme Resolución N° 30/2015 de CGR y normativa complementaria."
        - "Municipios deben enviar al GORE comprobante de ingreso, decretos de pago e informes mensuales de inversión."
      Prohib:
        - "Los recursos solo pueden utilizarse para ejecución del mismo proyecto FRIL."
    Informes:
      ID: GN-FRIL-INFORMES-01
      Req:
        - "Informe mensual debe remitirse dentro de los primeros 15 días hábiles administrativos del mes siguiente."
        - "Incluso sin movimiento, debe enviarse informe declarando 'sin movimiento'."
    Proyectos_sin_Adjudicacion:
      ID: GN-FRIL-PROY-SIN-ADJ-01
      Cond:
        - "Obras no adjudicadas 90 días corridos después de la tramitación total del convenio podrán ser reevaluadas."
      Req:
        - "Para solicitar la reevaluación por no adjudicación se debe haber cumplido con el número de llamados a licitación establecidos en la Ley N° 19.886 de Compras Públicas."
      Ctx:
        - "El instructivo establece consecuencias y tratamiento de proyectos sin adjudicación; se recomienda coordinar con DIPIR y DAF para ajustes presupuestarios y eventuales reasignaciones."

  Sec_15_Modificaciones_y_Termino:
    ID: GN-FRIL-SEC-15-MODIFICACIONES-TERMINO
    Modificaciones_Contrato:
      ID: GN-FRIL-MOD-CONTRATO-01
      Req:
        - "Toda modificación de contrato (salvo aquellas que solo ajustan plazo) debe ser autorizada por el GORE antes de su ejecución y a costo cero."
        - "ITO debe informar obligatoriamente al GORE sobre eventos relevantes (ejecución deficiente, incumplimientos, hechos sobrevinientes)."
        - "Municipio debe informar por oficio al GORE modificaciones de plazos y/o paralizaciones."
        - "Cambios cualitativos y cuantitativos significativos requieren solicitar reevaluación al GORE."
        - "Solicitudes de modificación deben presentarse con al menos 30 días antes del término del plazo contractual."
      Warn:
        - "Solicitudes fuera de plazo pueden ser rechazadas."
    Termino_Proyecto:
      ID: GN-FRIL-TERMINO-PROY-01
      Req:
        - "Al finalizar la obra, la Unidad Técnica municipal debe remitir recepción provisoria y ficha de cierre al GORE."
        - "DOM fiscaliza cumplimiento de Ley General de Urbanismo y Construcciones hasta la recepción."
        - "Acta de recepción debe consignar fecha de entrega de terreno y eventuales atrasos imputables al contratista."
      Proc:
        - "La recepción definitiva se realiza según plazos de bases de licitación y precede a la liquidación del contrato."
    Vigencia_Instructivo:
      ID: GN-FRIL-VIGENCIA-INSTRUCTIVO-01
      Cpt: "Vigencia y aplicabilidad territorial."
      Ctx:
        - "Aplica a comunas de la Región de Ñuble."
      Dln:
        - "Entra en vigencia a contar de la total tramitación del acto administrativo que lo aprueba."
        - "Permanece vigente mientras no existan cambios relevantes en Ley de Presupuestos y normas relacionadas."
    Operatividad_GESDOC:
      ID: GN-FRIL-GESDOC-CONTINGENCIA-01
      Conting:
        - "Si el sistema GESDOC no está completamente operativo, la División de Planificación y Desarrollo Regional adoptará medidas para asegurar la postulación y resguardo de la información."
      Act:
        - "Dichas medidas deberán ser informadas oportunamente a cada municipalidad."

  Sec_16_Firmas_y_Anexos:
    ID: GN-FRIL-SEC-16-ANEXOS
    Firmas_y_Distribucion:
      ID: GN-FRIL-FIRMAS-01
      Act:
        - "Se adjuntan certificados de acuerdo del CORE y oficio de visación de SUBDERE como anexos de la resolución."
        - "La resolución es firmada por el Gobernador Regional de Ñuble."
      Dest:
        - "Administración Regional – GORE Ñuble."
        - "División de Presupuesto e Inversión Regional – GORE Ñuble."
        - "División de Planificación y Desarrollo Regional – GORE Ñuble."
        - "División de Desarrollo Social y Humano – GORE Ñuble."
        - "División de Infraestructura y Transporte – GORE Ñuble."
        - "División de Fomento e Industria – GORE Ñuble."
        - "Departamento de Análisis y Evaluación DIPIR – GORE Ñuble."
        - "Departamento de Presupuesto de Inversión Regional – GORE Ñuble."
        - "Oficina de Partes."
    Anexos_Operativos:
      ID: GN-FRIL-ANEXOS-OPERATIVOS-01
      Purp: "Resumir anexos críticos (checklist, planillas y certificados) y remitir a plantillas detalladas en documentos fuente."
      Anexo_1_Checklist_Postulacion:
        ID: GN-FRIL-ANEXO-1-CHECKLIST-01
        Purp: "Listar la totalidad de archivos requeridos para la evaluación de una iniciativa FRIL 2025."
        Req:
          - "Oficio conductor firmado e ingresado en GESDOC y BIP."
          - "Ficha IDI 2025."
          - "Fotografías y localización (coordenadas + KML/KMZ)."
          - "Especificaciones técnicas y presupuesto por partida."
          - "Certificación de propiedad según tipología de terreno."
          - "Certificados de operación y mantención, factibilidad, permisos, participación ciudadana, pertinencia técnica y otros según tipo de proyecto."
        Warn:
          - "Al momento de la presentación del oficio, todos los archivos del checklist deben estar cargados en BIP y GESDOC."
      Anexo_2_Especificaciones_Tecnicas:
        ID: GN-FRIL-ANEXO-2-EETT-01
        Purp: "Establecer el formato y contenido mandatorio para el documento de Especificaciones Técnicas (EE.TT.) de proyectos FRIL."
        Bloque_Identificacion_Proyecto:
          Cpt: "Ficha de identificación."
          Req:
            - "Codigo BIP."
            - "Ubicación."
            - "Superficie (m², ml, unidades, etc.)."
            - "Arquitecto."
            - "Unidad Técnica (municipalidad)."
            - "Mandante (municipalidad)."
            - "Unidad Financiera: Gobierno Regional de Ñuble."
        Generalidades:
          ID: GN-FRIL-ANEXO-2-GENERALIDADES-01
          Req:
            - "Las obras deben ejecutarse considerando planos, EE.TT., reglamentos, normas y legislación vigente."
          Concordancias:
            Cpt: "Relación entre planos y EE.TT."
            Def: "Los planos y las EE.TT. son complementarios."
            Resp: "Contratista."
            Act:
              - "Conocer y compatibilizar todos los documentos del proyecto."
              - "Informar diferencias antes de iniciar la construcción."
            Orden_Prelacion_Documentos:
              Cpt: "Orden de prelación en caso de divergencias."
              Orden:
                - "Consultas y aclaraciones en portal Mercado Público."
                - "Instrucciones y criterios de la Inspección Técnica de Obra (ITO)."
                - "Planos de detalles (escalas mayores sobre generales)."
                - "Especificaciones Técnicas Generales y de especialidad."
                - "Proyecto de Arquitectura y Detalles."
                - "Especificaciones Técnicas."
                - "Planos de Estructuras."
              Cond:
                - "Ante divergencias entre profesionales, prevalece el arquitecto autor del proyecto."
        Administracion_y_Control_Obra:
          ID: GN-FRIL-ANEXO-2-ADM-OBRA-01
          Calidad_Materiales:
            Req:
              - "Todos los materiales deben ser de primera calidad dentro de su especie."
            Auth:
              - "La ITO rechazará materiales que no cumplan lo especificado."
              - "La ITO puede solicitar ensayos o certificaciones técnicas en cualquier etapa."
            Cond:
              - "Si se especifica una marca, es referencial; se pueden proponer alternativas de calidad igual o superior, sujetas a aprobación de la ITO."
          Archivos_Obra:
            Req:
              - "Mantener en obra un juego completo de planos actualizados y ordenados."
              - "Solo tendrán validez planos firmados y timbrados en original."
          Permisos:
            Resp:
              - "El Contratista es responsable de cancelar todos los permisos y derechos asociados a la construcción (rotura de vías, empalmes, etc.)."
          Inspeccion_Tecnica_Obra:
            Resp:
              - "El control de la obra estará a cargo de la ITO, nombrada por el mandante."
            Req:
              - "El contratista debe cumplir estrictamente todas las instrucciones de la ITO, registradas en el Libro de Obra."
            Prohib:
              - "La ITO no puede efectuar cambios al proyecto sin V°B° del arquitecto proyectista y del Mandante."
          Libro_Obras:
            Req:
              - "Mantener un Libro de Obra tipo MANIFOLD triplicado en obra."
              - "Registrar entrega de terreno, control de trabajos, aclaraciones, marcha de faenas, recepción de materiales, atrasos, observaciones y recepción de obras."
          Normas_Seguridad:
            Resp:
              - "El contratista asume responsabilidad completa por daños a personas o propiedad."
            Req:
              - "Tomar todas las medidas de seguridad para evitar accidentes."
              - "Asegurar uso de Elementos de Protección Personal (EPP) adecuados por parte de todo el personal."
        Obras_Civiles_y_Provisionales:
          ID: GN-FRIL-ANEXO-2-OBRAS-01
          Gastos_Adicionales:
            Cpt: "Certificados de ensayos de materiales."
            Resp:
              - "El contratista debe realizar y costear ensayos en laboratorios autorizados."
            Req:
              - "Entregar informe de ensayo a la ITO y registrarlo en Libro de Obra."
          Limpieza_y_Cuidado:
            Resp:
              - "El contratista debe mantener la obra aseada, ordenada y con vigilancia hasta la recepción final."
          Obras_Provisionales:
            Instalaciones_Provisorias:
              Req:
                - "Ejecutar empalmes provisorios a redes de electricidad, agua potable y alcantarillado."
                - "Dar de baja todas las conexiones provisorias al finalizar la obra."
                - "Instalar señalética preventiva y protecciones."
            Construcciones_Provisorias:
              Req:
                - "Construir bodega de herramientas y materiales, con recintos separados para materiales delicados."
                - "Construir o habilitar oficina para ITO y Profesional Residente (con equipamiento básico)."
                - "Construir servicios higiénicos para el personal (WC, lavamanos, urinario, ducha)."
                - "Desarmar y retirar todas las construcciones provisorias al finalizar la obra."
          Trabajos_Previos:
            Req:
              - "Despeje de terreno según descripción del proyecto."
              - "Escarpe y nivelación de terreno según especificaciones."
              - "Escarpe, relleno y compactación con espesores y materiales definidos."
              - "Trazado, niveles y replanteo conforme a dimensiones y métodos establecidos."
        Letrero_y_Placa:
          ID: GN-FRIL-ANEXO-2-LETRERO-PLACA-01
          Letrero_Obras:
            Req:
              - "Construir letrero de obras según Normas Gráficas del GORE Ñuble."
            Spec:
              - "Tamaño tipo 00: 5,00 m (ancho) x 2,00 m (alto)."
              - "Impresión en vinilo PVC o autoadhesivo de alta calidad, resistente al agua, con tintas con filtro UV (garantía 3 años)."
              - "Tipografía obligatoria: Museo Sans."
            Prohib:
              - "No se puede añadir logotipo de la constructora; solo su nombre en sección 'Contratista'."
            Contenido:
              - "Nombre del proyecto (según Ficha IDI)."
              - "Financia: Gobierno Regional de Ñuble."
              - "Inversión: monto total en M$."
              - "Fecha de inicio (según acta entrega de terreno)."
              - "Plazo de ejecución (según oferta adjudicada)."
              - "Unidad técnica."
              - "Contratista."
            Estructura_Valla:
              Spec:
                - "Pilares: 3 unidades, perfil rectangular 100x100x3 mm."
                - "Vientos: diagonales, perfil 50x50x3 mm."
                - "Fundación: hormigón, profundidad mínima 0,75 m."
                - "Marco: perfil 20x20x2 mm, 5,0x2,0 m."
                - "Soporte gráfica: plancha de zinc 0,5 mm."
              Warn:
                - "Especificaciones estructurales son mínimas y deben corroborarse con memoria de cálculo."
          Placa_Informativa:
            Req:
              - "Instalar al menos una placa informativa."
            Spec:
              - "Material: acero fotograbado bajo relieve."
              - "Medidas mínimas: 80 cm (ancho) x 60 cm (alto)."
              - "Debe usar marco oficial del GORE descargable desde sitio web."
            Contenido:
              - "Nombre del proyecto y logos (GORE y organización) del mismo tamaño."
              - "Frase: 'Iniciativa realizada con apoyo del Gobierno Regional de Ñuble, siendo Gobernador (nombre del Gobernador Regional)'."
        Obra_Gruesa_y_Firmas:
          ID: GN-FRIL-ANEXO-2-OBRA-GRUESA-01
          Obra_Gruesa:
            Req:
              - "Describir todas las partidas de la obra en concordancia con el presupuesto oficial."
            Ex:
              - "Fundaciones: hormigón premezclado con parámetros de dosificación, docilidad y control de calidad."
            Auth:
              - "Se debe solicitar autorización a la ITO antes de llenar fundaciones."
            Warn:
              - "La ITO puede ordenar demolición de estructuras con segregaciones o desniveles."
            Prohib:
              - "No se aceptan demoliciones posteriores para pasar instalaciones; deben dejarse espacios previstos."
          Firmas:
            Req:
              - "El documento debe ser firmado por Profesional Responsable y Director(a) de SECPLA, indicando nombre, RUT y profesión."

      Anexo_3_Presupuesto_Oficial:
        ID: GN-FRIL-ANEXO-3-PPTO-01
        Purp: "Definir la estructura y desglose de partidas mandatorio para el presupuesto de proyectos FRIL."
        Formato:
          Frmt:
            - "Presupuesto en formatos Excel y PDF, según secciones de documentación del instructivo."
          Encabezado:
            Req:
              - "Nombre del Proyecto (según Ficha IDI)."
              - "Código BIP."
              - "Comuna."
              - "Mandante."
              - "Fecha."
        Columnas_Obligatorias:
          ID: GN-FRIL-ANEXO-3-COLUMNAS-01
          Req:
            - "ITEM"
            - "DESCRIPCION"
            - "UNIDAD"
            - "CANTIDAD"
            - "PRECIO UNITARIO"
            - "PRECIO TOTAL"
        Estructura_Partidas:
          ID: GN-FRIL-ANEXO-3-PARTIDAS-01
          Cpt: "Estructura jerárquica de ítems y sub-ítems del presupuesto."
          Tabla_Resumen:
            Ctx:
              - "La planilla debe contemplar, al menos, los siguientes grupos de partidas, siguiendo el detalle del instructivo:"
            Grupos:
              - "1 GASTOS GENERALES (letrero de obra, ensayos de laboratorio, fletes, permisos y derechos, utilidades)."
              - "2 OBRAS PROVISIONALES (instalaciones y construcciones provisorias)."
              - "3 TRABAJOS PREVIOS (limpieza, escarpe, nivelación, demoliciones)."
              - "4 OBRA GRUESA (excavaciones, hormigones, moldajes, enfierraduras, estructuras, albañilería, tabiquería, techumbre)."
              - "5 TERMINACIONES (revestimientos, puertas, ventanas, pinturas)."
              - "6 INSTALACIONES (alcantarillado, agua potable, electricidad, gas, climatización)."
              - "7 OBRAS EXTERIORES (cierros, pavimentos exteriores, áreas verdes, iluminación exterior)."
              - "8 EQUIPAMIENTO Y EQUIPOS."
              - "9 OTROS (ítems específicos adicionales)."
        Resumen_Costos:
          ID: GN-FRIL-ANEXO-3-RESUMEN-01
          Req:
            - "Presentar COSTO NETO como suma de todos los precios totales."
            - "Calcular IVA 19% sobre costo neto."
            - "Calcular COSTO TOTAL PROYECTO como suma de costo neto + IVA."
        Firmas:
          Req:
            - "Presupuesto debe ser firmado por Profesional Responsable (nombre, RUT, firma)."
            - "Presupuesto debe ser firmado por Alcalde(sa) (nombre, RUT, firma)."

      Anexo_4_Certificado_Costos_Operacion_Mantencion:
        ID: GN-FRIL-ANEXO-4-COSTOS-OM-01
        Purp: "Definir el formato y contenido mandatorio del certificado que garantiza financiamiento de costos de operación y mantención del proyecto."
        Entidad_Emisora:
          Cpt: "Quién puede emitir el certificado."
          Req:
            - "Honorable Concejo Municipal de la municipalidad correspondiente."
            - "Organización usuaria del proyecto (indicando su RUT)."
        Contenido_Mandatorio:
          ID: GN-FRIL-ANEXO-4-CONTENIDO-01
          Req:
            - "Identificación de la aprobación (tipo de sesión, número y fecha del acuerdo)."
            - "Identificación del proyecto (nombre completo y código BIP)."
            - "Declaración expresa de compromiso de financiar costos de operación y mantención."
            - "Periodo del compromiso (toda la vida útil estimada del proyecto, en años)."
            - "Desglose de costos de operación y mantención (montos mensuales y anuales por separado)."
            - "Cláusula de cierre que indique que el certificado se extiende para ser presentado al GORE Ñuble."
          Mdl:
            - "Texto tipo incluye fórmulas del estilo: 'en sesión N°..., de fecha ...', 'respecto al proyecto denominado...', 'durante toda su vida útil, estimada en ... años', y detalle de costos mensuales/anuales de operación y mantención."
        Firmas_Requeridas:
          Req:
            - "Firma 1: Alcalde(sa) o Presidente(a) de la organización (nombre, cargo, firma)."
            - "Firma 2: Secretario(a) Municipal o Secretario(a) de la organización (nombre, cargo, firma)."

      Anexo_5_Permiso_Anteproyecto_o_Informe_Tecnico:
        ID: GN-FRIL-ANEXO-5-PERMISO-01
        Purp: "Definir documentación obligatoria para acreditar aprobación normativa de las obras a ejecutar según su tipología."
        Req:
          - "Se debe adjuntar uno de los tres documentos siguientes, según características del proyecto."
        Opcion_1_Permiso_Edificacion:
          Cond:
            - "Obligatorio para proyectos que contemplen construcción de obras nuevas, ampliaciones o reposiciones que legalmente requieran permiso."
        Opcion_2_Anteproyecto_Edificacion:
          Cond:
            - "Puede presentarse cuando el proyecto requiere Permiso de Edificación pero este aún no está disponible al momento de postular."
          Req:
            - "Debe ser emitido por la Dirección de Obras Municipales (DOM) correspondiente."
        Opcion_3_Informe_Tecnico_Profesional:
          Ctx:
            - "Aplicable a proyectos que no requieren Permiso de Edificación (por ejemplo, mejoramiento, habilitación, normalización)."
          Req:
            - "Indicar explícitamente el cumplimiento del proyecto con la Ordenanza General de Urbanismo y Construcción (OGUC)."
            - "Estar firmado por profesional competente y por Director(a) SECPLA o Director(a) de Obras Municipales."

      Anexo_6_Certificado_Pertinencia_Tecnica:
        ID: GN-FRIL-ANEXO-6-PERTINENCIA-01
        Purp: "Establecer documentación obligatoria para certificar pertinencia técnica de la iniciativa y ausencia de duplicidad de financiamiento."
        Req:
          - "Se debe presentar uno de los dos tipos de certificados, según la naturaleza del proyecto."
        Opcion_1_Certificado_Alcalde:
          Ctx:
            - "Formato definido en Anexo 6 para proyectos donde el municipio tiene competencia técnica principal (ej. proyectos deportivos recreativos, áreas verdes municipales)."
          Req:
            - "Declarar que el terreno no se encuentra asociado a otra iniciativa de inversión con ninguna otra fuente de financiamiento."
            - "Declarar que la iniciativa postulada no se encuentra asociada a otra fuente de financiamiento (sectoriales, fondos propios, etc.)."
        Opcion_2_Certificado_Servicio_Competente:
          Cond:
            - "Aplicable a proyectos que por su naturaleza involucran la competencia de otros servicios del Estado."
          Req:
            - "Certificado emitido por el servicio al cual le compete la visación de la iniciativa (ej. SEREMI de Educación para infraestructura educacional, SERVIU para obras viales urbanas, SEREMI de Energía para alumbrado público)."
        Src:
          - "kb_gn_026_guia_fril_sts.md – Sección 4.2 a 4.6 (Anexos 2–6)."
