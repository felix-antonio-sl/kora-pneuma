---
urn: urn:gn:kb:gn-instructivo-subvencion-8-2025-sts
nombre: gn-instructivo-subvencion-8-2025-sts
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Instructivo Concurso Vinculación con la Comunidad 8% 2025 GORE Ñuble; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_028_instructivo_subvencion_8_koda.yml (sha256:ea7db77fd2a9a2f70e431d2e119731e689672589478265540924deaee3fa4a80); URN KODA legado urn:gorenuble:gn:instructivo-subvencion-8-2025-sts:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "instructivo"]
familia: bok
---
# Artefacto KODA/Spec – Instructivo Concurso Vinculación con la Comunidad 8% 2025 GORE Ñuble
# Fuente principal: kb_gn_028_instructivo_subvencion_8_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:instructivo-subvencion-8-2025-sts:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_028_instructivo_subvencion_8_koda.yml"
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

ID: GN-CONC-8-STS-2025-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Instructivo general del Concurso de Vinculación con la Comunidad 8% 2025 del
  Gobierno Regional de Ñuble, dirigido a instituciones privadas sin fines de
  lucro y municipalidades. Establece objetivos, marco legal, reglas
  transversales, fondos y áreas de postulación, requisitos de admisibilidad,
  procedimientos de evaluación, seguimiento, ejecución y rendición de cuentas,
  junto con anexos de formularios tipo.

Source:
  Primary-Source: "staging/gn/kodeando/kb_gn_028_instructivo_subvencion_8_sts.md"
  Ctx_Required:
    - "Ley N° 21.796 – Ley de Presupuestos del Sector Público 2026 (Glosa 07, Subtítulo 24, subvenciones GORE)."
    - "Ley N° 19.175 – Ley Orgánica Constitucional sobre Gobierno y Administración Regional (LOC GORE)."
    - "Ley N° 19.880 – Bases de los Procedimientos Administrativos."
    - "Ley N° 18.575 – Bases Generales de la Administración del Estado."
    - "Ley N° 19.862 – Registro de Colaboradores del Estado."
    - "Ley N° 19.886 – Ley de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios."
    - "Ley N° 19.418 – Sobre Juntas de Vecinos y demás organizaciones comunitarias."
    - "Ley N° 19.253 – Ley Indígena."
    - "Ley N° 19.712 – Ley del Deporte."
    - "Ley N° 21.015 – Inclusión Laboral."
    - "Ley N° 19.300 – Bases Generales del Medio Ambiente."
    - "Ley N° 21.302 – Crea el Servicio Nacional de Protección Especializada a la Niñez y Adolescencia (Mejor Niñez)."
    - "Estrategia Regional de Desarrollo Región de Ñuble 2024–2030."
    - "Estrategia Quinquenal Regional del Ministerio de las Culturas 2024–2025."
    - "Plan Nacional de Seguridad 2022–2024."
  Ctx_Optional:
    - "Política Nacional de Actividad Física y Deporte 2016–2025."
    - "Documentos operativos internos del GORE Ñuble sobre subvenciones concursables 8%."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-CONC-8-STS-2025-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure:
    headers, IDs, listas, tablas) with zero loss. Ignore fat (filler words,
    retórica, redundancias).

    LEXICON (expand before processing):
      Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dep->Dependency, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID,
      Just->Justification, Mech->Mechanism, Mssn->Mission,
      Nat->Nature, Obj->Objective, Proc->Process,
      Prohib->Prohibition, Purp->Purpose, Ref->Reference,
      Req->Requirement, Res->Result, Resp->Responsible,
      Src->Source, Warn->Warning, Dst->Destination.

    REFERENCE POLICY:
      - Ref: is internal only—must point to an existing ID defined within THIS
        document.
      - External leyes, resoluciones, circulares, políticas y estrategias se
        mencionan bajo Ctx:, Src:, Ctx_Required: o Ctx_Optional:.

    LANGUAGE POLICY:
      - Keywords in English (and abbreviated forms as listed).
      - Content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_Concurso8_Conceptos_Clave:
  ID: GN-CONC8-GLOSARIO-01
  Purp: "Definir conceptos, siglas, actores y fondos clave del Concurso 8% Vinculación con la Comunidad."
  Terminos:
    - ID: GN-CONC8-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento regional administrada por los Gobiernos Regionales; permite asignar recursos a inversión y subvenciones especiales como el Concurso 8%."
    - ID: GN-CONC8-GLOS-GORE
      Sigla: "GORE"
      Cpt: "Gobierno Regional"
      Def: "Institución descentralizada, con personalidad jurídica y patrimonio propio, responsable de la administración superior de la Región de Ñuble y de la gestión del FNDR."
    - ID: GN-CONC8-GLOS-CONCURSO8
      Cpt: "Concurso Vinculación con la Comunidad 8%"
      Def: "Concurso anual de subvenciones FNDR hasta por el 8% de los recursos de inversión regional, destinado a financiar iniciativas de vinculación con la comunidad en diversos fondos temáticos."
    - ID: GN-CONC8-GLOS-SUBVENCION8
      Cpt: "Subvenciones FNDR 8%"
      Def: "Subvenciones financiadas con cargo a hasta un 8% de los recursos de inversión regional, orientadas a actividades específicas de interés comunitario en áreas como cultura, deporte, seguridad, medio ambiente, entre otras."
    - ID: GN-CONC8-GLOS-ORG-PRIV-SFL
      Cpt: "Instituciones privadas sin fines de lucro"
      Def: "Corporaciones, fundaciones, ONG, organizaciones comunitarias y otras entidades privadas sin fines de lucro habilitadas para postular al Concurso 8% bajo las reglas del instructivo."
    - ID: GN-CONC8-GLOS-ORG-COMUNITARIAS
      Cpt: "Organizaciones comunitarias"
      Def: "Organizaciones territoriales, funcionales o de base (ej. juntas de vecinos, centros de padres, clubes, comités) reguladas principalmente por Ley N° 19.418 y normativa municipal."
    - ID: GN-CONC8-GLOS-CIES
      Sigla: "CIES"
      Cpt: "Centro Integral de Emergencia y Seguridad"
      Def: "Unidad del GORE Ñuble responsable de la gestión del Fondo de Seguridad Ciudadana del Concurso 8% y de la coordinación técnica asociada."
    - ID: GN-CONC8-GLOS-SISREC
      Sigla: "SISREC"
      Cpt: "Sistema de Rendición de Cuentas"
      Def: "Plataforma utilizada para la rendición de cuentas de subvenciones públicas; de uso obligatorio para municipalidades y, según casos, para instituciones privadas."
    - ID: GN-CONC8-GLOS-MEJORNINEZ
      Cpt: "Residencias Mejor Niñez"
      Def: "Residencias de protección del Servicio Nacional de Protección Especializada a la Niñez y Adolescencia, con línea de financiamiento específica dentro del Fondo Social."
    - ID: GN-CONC8-GLOS-FONDO-CULTURA
      Cpt: "Fondo de Cultura"
      Def: "Fondo del Concurso 8% orientado a iniciativas culturales, patrimoniales, artísticas y de cultura tradicional."
    - ID: GN-CONC8-GLOS-FONDO-SOCIAL
      Cpt: "Fondo Social e Inclusión"
      Def: "Fondo que financia iniciativas sociales, de inclusión y prevención psicosocial, incluyendo residencias Mejor Niñez."
    - ID: GN-CONC8-GLOS-FONDO-GENERO
      Cpt: "Fondo Equidad de Género"
      Def: "Fondo destinado a iniciativas que disminuyan brechas y violencias de género y promuevan la autonomía y liderazgo de mujeres y población LGBTIQA+."
    - ID: GN-CONC8-GLOS-FONDO-DEPORTE
      Cpt: "Fondo de Deporte"
      Def: "Fondo destinado a iniciativas deportivas formativas, recreativas, inclusivas y de competición, incluyendo representación de deportistas."
    - ID: GN-CONC8-GLOS-FONDO-AM
      Cpt: "Fondo Personas Mayores"
      Def: "Fondo exclusivo para organizaciones de personas mayores, orientado a envejecimiento activo, inclusión y bienestar integral."
    - ID: GN-CONC8-GLOS-FONDO-MEDIOAMB
      Cpt: "Fondo Medio Ambiente"
      Def: "Fondo destinado a iniciativas de protección ambiental, educación ambiental, eficiencia hídrica y energética, limpieza de focos de basura y tenencia responsable de mascotas."
    - ID: GN-CONC8-GLOS-FONDO-SEG
      Cpt: "Fondo Seguridad Ciudadana"
      Def: "Fondo destinado a iniciativas que mejoren la seguridad humana mediante prevención situacional, prevención de riesgos de desastres y equipamiento comunitario de seguridad."

Normativa_Concurso8_Clave:
  ID: GN-CONC8-NORMATIVA-01
  Purp: "Registrar las principales normas legales y administrativas que sustentan el Concurso 8% Vinculación con la Comunidad."
  Normas:
    - ID: GN-CONC8-NORM-LEY-21796-01
      Cpt: "Ley N° 21.796 – Ley de Presupuestos del Sector Público 2026"
      Def: "Incluye glosas presupuestarias que autorizan a los Gobiernos Regionales a destinar hasta un 8% de sus recursos de inversión a subvenciones para actividades específicas."
    - ID: GN-CONC8-NORM-LEY-19175-01
      Cpt: "Ley N° 19.175 – LOC GORE"
      Def: "Ley Orgánica Constitucional sobre Gobierno y Administración Regional que establece competencias, atribuciones y organización de los GORE."
    - ID: GN-CONC8-NORM-LEY-18880-01
      Cpt: "Ley N° 19.880"
      Def: "Establece Bases de los Procedimientos Administrativos aplicables a los actos de la Administración del Estado."
    - ID: GN-CONC8-NORM-LEY-18575-01
      Cpt: "Ley N° 18.575"
      Def: "Ley Orgánica Constitucional de Bases Generales de la Administración del Estado, que fija principios de probidad, eficiencia y responsabilidad."
    - ID: GN-CONC8-NORM-LEY-19862-01
      Cpt: "Ley N° 19.862"
      Def: "Regula el Registro de Colaboradores del Estado y Municipalidades, exigido para instituciones receptoras de fondos públicos."
    - ID: GN-CONC8-NORM-LEY-19886-01
      Cpt: "Ley N° 19.886"
      Def: "Establece Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios, aplicable a la contratación asociada a subvenciones."
    - ID: GN-CONC8-NORM-LEY-19418-01
      Cpt: "Ley N° 19.418"
      Def: "Regula Juntas de Vecinos y demás organizaciones comunitarias."
    - ID: GN-CONC8-NORM-LEY-19253-01
      Cpt: "Ley N° 19.253 – Ley Indígena"
      Def: "Regula comunidades y asociaciones indígenas; relevante para proyectos en territorios y comunidades indígenas."
    - ID: GN-CONC8-NORM-LEY-19712-01
      Cpt: "Ley N° 19.712 – Ley del Deporte"
      Def: "Norma el desarrollo de la actividad física y el deporte en Chile, marco para proyectos deportivos."
    - ID: GN-CONC8-NORM-LEY-21015-01
      Cpt: "Ley N° 21.015 – Inclusión Laboral"
      Def: "Establece obligaciones de inclusión laboral de personas con discapacidad, relevante para enfoque inclusivo de proyectos."
    - ID: GN-CONC8-NORM-LEY-19300-01
      Cpt: "Ley N° 19.300 – Bases Generales del Medio Ambiente"
      Def: "Marco general para la gestión ambiental y la protección del medio ambiente."
    - ID: GN-CONC8-NORM-LEY-21302-01
      Cpt: "Ley N° 21.302 – Servicio Nacional de Protección Especializada a la Niñez y Adolescencia"
      Def: "Crea el Servicio Mejor Niñez y regula residencias familiares que pueden ser beneficiarias en líneas específicas."

Instructivo_Concurso_Vinculacion_Comunidad_8_2025:
  ID: GN-CONC8-INSTRUCTIVO-01
  Titulo: "Instructivo Concurso de Vinculación con la Comunidad 8% 2025 – Región de Ñuble"
  Purp: |
    Establecer reglas, requisitos, procesos, fondos, áreas de postulación y
    documentación para la formulación, evaluación, adjudicación, ejecución y
    rendición de iniciativas financiadas con subvenciones FNDR 8% del Gobierno
    Regional de Ñuble durante el año 2025, tanto para instituciones privadas
    sin fines de lucro como para municipalidades.
  Destinatarios:
    - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y organizaciones comunitarias de la Región de Ñuble."
    - "Municipalidades de la Región de Ñuble y sus equipos técnicos."
  Alcance:
    - "Aplica a todas las líneas y fondos del Concurso de Vinculación con la Comunidad 8% 2025 administrado por el GORE Ñuble."
    - "Complementa la normativa presupuestaria nacional y las políticas regionales vigentes (ERD, planes sectoriales)."

  Estructura_Secciones:
    - ID: GN-CONC8-SEC-1-DESCRIPCION-GRAL
      Cpt: "Descripción general del concurso (instituciones privadas)."
    - ID: GN-CONC8-SEC-2-REGLAS-TRANSVERSALES
      Cpt: "Reglas transversales del concurso (instituciones privadas)."
    - ID: GN-CONC8-SEC-3-FONDO-CULTURA
      Cpt: "Fondo de Cultura."
    - ID: GN-CONC8-SEC-4-FONDO-SOCIAL
      Cpt: "Fondo Social e Inclusión."
    - ID: GN-CONC8-SEC-5-FONDO-GENERO
      Cpt: "Fondo Equidad de Género."
    - ID: GN-CONC8-SEC-6-FONDO-DEPORTE
      Cpt: "Fondo de Deporte."
    - ID: GN-CONC8-SEC-7-FONDO-PERSONAS-MAYORES
      Cpt: "Fondo para Personas Mayores."
    - ID: GN-CONC8-SEC-8-FONDO-MEDIO-AMBIENTE
      Cpt: "Fondo de Medio Ambiente."
    - ID: GN-CONC8-SEC-9-FONDO-SEGURIDAD
      Cpt: "Fondo de Seguridad Ciudadana."
    - ID: GN-CONC8-SEC-10-MUNICIPIOS
      Cpt: "Reglas especiales para organismos públicos (municipalidades)."
    - ID: GN-CONC8-SEC-11-SEGUIMIENTO-RENDICION
      Cpt: "Procedimiento general de seguimiento, ejecución y rendición."
    - ID: GN-CONC8-SEC-12-ANEXOS
      Cpt: "Anexos: formularios y documentos tipo."

  Sec_1_Descripcion_General_Privados:
    ID: GN-CONC8-SEC-1-DESCRIPCION-GRAL
    Introduccion_Concurso_8:
      ID: GN-CONC8-INTRO-01
      Cpt: "Introducción general del Concurso 8%."
      Ctx:
        - "La administración de la Región de Ñuble recae en el Gobierno Regional."
      Obj:
        - "Alcanzar el desarrollo social, cultural y económico de la región."
      Resp:
        - "El Gobierno Regional diseña, elabora y aprueba políticas, planes, programas y proyectos de desarrollo regional."
      Fnd:
        - "Las políticas deben ajustarse al presupuesto de la Nación, la Estrategia Regional de Desarrollo y los instrumentos de planificación comunal."
      Req:
        - "Las acciones deben ser coherentes con las políticas públicas nacionales, evitando duplicidad de funciones."
      Mech:
        - "El FNDR permite financiar acciones en beneficio de la comunidad de manera participativa, directa y transparente."
      Purp:
        - "Permitir que instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y organizaciones comunitarias accedan a financiamiento para actividades que generen integración e inclusión de los habitantes de la Región de Ñuble."

    Objetivos_Concurso_Privados:
      ID: GN-CONC8-OBJ-PRIV-01
      Cpt: "Objetivos del concurso para instituciones privadas."
      Objetivo_General:
        ID: GN-CONC8-OBJ-PRIV-GRAL-01
        Obj: "Desarrollar y promover iniciativas y actividades sociales dirigidas a los habitantes de la Región de Ñuble para mejorar su calidad de vida y fomentar el desarrollo integral de la región, con enfoque en propuestas inclusivas y con perspectiva de género."
      Objetivos_Especificos:
        ID: GN-CONC8-OBJ-PRIV-ESP-01
        Obj:
          - "Potenciar la interrelación de la cultura, el patrimonio y su entorno mediante la promoción y rescate de tradiciones."
          - "Fomentar espacios de integración e inclusión social a través de acciones que generen vínculos entre organizaciones y la comunidad."
          - "Fomentar la actividad física, la vida saludable e inclusiva para mejorar la calidad de vida."
          - "Fomentar iniciativas que incrementen el empoderamiento y liderazgo femenino."
          - "Promover iniciativas de tenencia responsable de mascotas."
          - "Promover iniciativas de cuidado y protección del medio ambiente."
          - "Potenciar iniciativas que mejoren las condiciones biopsicosociales de los adultos mayores para un envejecimiento activo."
          - "Promover estilos de vida saludable y la protección de derechos de niños, niñas y adolescentes."
          - "Potenciar iniciativas de prevención y seguridad ciudadana."

    Marco_Legal_Concurso:
      ID: GN-CONC8-MARCO-LEGAL-01
      Cpt: "Marco legal específico del concurso y actividades subvencionables."
      Fnd:
        - Cpt: "Ley de Presupuesto del Sector Público N° 21.796, año 2026, glosa 07, subtítulo 24."
        - "La oferta programática de los gobiernos regionales está sujeta al Sistema de Evaluación y Monitoreo del MDSF y de DIPRES, con excepción de programas en ejecución como las subvenciones del Concurso 8%."
        - "Los gobiernos regionales pueden destinar hasta un 8% de sus recursos de inversión para subvencionar actividades específicas."
        - "Asignación directa excepcional: se podrá asignar hasta un 10% del 8% para casos emblemáticos, excepcionales y emergentes, previo acuerdo del Consejo Regional, sujeto a lo dispuesto en Resolución DIPRES N°72/08.01.2025 y sus modificaciones."
      Actividades_Subvencionables:
        ID: GN-CONC8-ACT-SUBVENCIONABLES-01
        Cpt: "Listado de actividades subvencionables con cargo al 8%."
        Act:
          - "Actividades deportivas y del programa Elige Vivir Sano."
          - "Actividades de participación de niños, niñas, adolescentes y jóvenes (Ley N° 21.302, art. 6 letra p)."
          - "Actividades de carácter social, incluyendo atención a personas con discapacidad y dependencia severa y prevención y rehabilitación de drogas."
          - "Actividades de atención de adultos mayores e integración y promoción del envejecimiento activo."
          - "Actividades de protección del medioambiente y educación ambiental."
          - "Actividades asociadas con animales (adopción, rescate, tratamiento veterinario, gestión de residuos)."
          - "Actividades de funcionamiento de establecimientos de larga estadía para adultos mayores y residencias del Servicio Mejor Niñez."
          - "Actividades de funcionamiento de teatros municipales/regionales y/o monumentos históricos."
          - "Actividades culturales y patrimoniales."
          - "Actividades de seguridad ciudadana."

    Normativa_Aplicable_Detallada:
      ID: GN-CONC8-NORM-APLICABLE-DET-01
      Cpt: "Normativa aplicable citada explícitamente en el instructivo."
      Fnd:
        - "Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional."
        - "Ley N° 19.880, de Procedimientos Administrativos."
        - "Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado."
        - "Ley N° 21.796, del Presupuesto del Sector Público del año 2026."
        - "Certificado del Consejo Regional de Ñuble N° 1124/2024."
        - "Resoluciones N° 30/2015 y N° 07/2019 de la Contraloría General de la República."
        - "Circular 20/2023 del Ministerio de Hacienda."
        - "Ley N° 19.862, Registro de Colaboradores del Estado."
        - "Ley N° 19.886, Ley de Bases Sobre Contratos Administrativos."
        - "Ley N° 19.418, Sobre Juntas de Vecinos."
        - "Ley N° 19.253, Sobre Protección Indígena."
        - "Ley N° 19.712, de Deporte."
        - "Ley N° 21.015, Inclusión Laboral."
        - "Ley N° 19.300, de Bases Generales del Medio Ambiente."
        - "Ley N° 21.302, Crea el Servicio Mejor Niñez."
        - "Estrategia Regional de Desarrollo Región de Ñuble 2024–2030."
        - "Política Nacional de Actividad Física y Deporte 2016–2025."
        - "Plan Nacional de Seguridad 2022–2024."
        - "Estrategia Quinquenal Regional del Ministerio de las Culturas 2024–2025."

    Participacion_y_Postulacion_Privados:
      ID: GN-CONC8-PARTICIPACION-POST-PRIV-01
      Requisitos_Postulantes:
        ID: GN-CONC8-REQ-POSTULANTES-PRIV-01
        Cpt: "Requisitos generales para instituciones privadas."
        Req:
          - "Ser institución privada sin fines de lucro, organización de la sociedad civil u organización comunitaria."
          - "Tener antigüedad mínima de 2 años desde su constitución."
          - "Tener domicilio en la Región de Ñuble."
          - "Demostrar experiencia en el área de postulación del proyecto."
          - "No tener rendiciones pendientes con el Gobierno Regional de Ñuble."
      Regla_General_Postulacion:
        ID: GN-CONC8-REG-GRAL-POST-01
        Prohib:
          - "Las organizaciones privadas sin fines de lucro podrán postular solo a una iniciativa del concurso."
      Excepciones_Regla_General:
        ID: GN-CONC8-EXCEPCIONES-POST-01
        Cond:
          - "Organismos colaboradores del Servicio Mejor Niñez pueden presentar más de una iniciativa, exclusivamente en el área 'Residencias Mejor Niñez' del Fondo Social."
          - "Instituciones privadas sin fines de lucro de Deporte o Cultura con representación regional, interregional, nacional o internacional pueden presentar hasta dos iniciativas."
        Req:
          - "En el caso de instituciones de Deporte o Cultura con representación, una de las iniciativas debe ser obligatoriamente para participación en un evento de carácter interregional, regional, nacional o internacional."

    Recursos_Disponibles_y_Distribucion_Privados:
      ID: GN-CONC8-RECURSOS-PRIV-01
      Monto_Total_Disponible:
        ID: GN-CONC8-MONTO-TOTAL-PRIV-01
        Cpt: "Monto total disponible para instituciones privadas."
        Def: "M$ 4.850.000 (cuatro mil ochocientos cincuenta millones de pesos)."
      Distribucion_Fondos_Privados:
        ID: GN-CONC8-DIST-FONDOS-PRIV-01
        Cpt: "Distribución del monto total entre fondos y concursos especiales."
        Tabla:
          Ctx: |
            |Fondo|Concurso Privados - Organizaciones de Base|Concurso Especial (Cultura y Deporte)|
            |-|-|-|
            |Medio Ambiente|M$ 400.000|N/A|
            |Adulto Mayor|M$ 400.000|N/A|
            |Social e Inclusión|M$ 500.000|N/A|
            |Cultura|M$ 330.000|M$ 270.000|
            |Equidad de Género|M$ 400.000|N/A|
            |Deporte|M$ 800.000|M$ 200.000|
            |Seguridad Ciudadana|M$ 1.550.000|N/A|
            |**TOTAL**|**M$ 4.380.000**|**M$ 470.000**|
      Criterio_Adjudicacion_Privados:
        ID: GN-CONC8-CRIT-ADJ-PRIV-01
        Mech:
          - "Los recursos se distribuirán entre las iniciativas que superen la admisibilidad y obtengan el puntaje de corte mínimo en la revisión técnica, sujeto a disponibilidad presupuestaria."
          - "Si las iniciativas recomendadas superan el presupuesto, el GORE puede aumentar el puntaje de corte."

    Descripcion_Fondos_Disponibles:
      ID: GN-CONC8-DESC-FONDOS-01
      Fondos:
        - ID: GN-CONC8-FONDO-CULT-01
          Cpt: "Fondo de Cultura"
          Purp:
            - "Financiar actividades culturales que aborden el desarrollo de la identidad local, comunal, provincial y regional."
        - ID: GN-CONC8-FONDO-SOCIAL-01
          Cpt: "Fondo Social e Inclusión"
          Purp:
            - "Financiar actividades de carácter social que promuevan la vinculación activa, inclusión, intervención y desarrollo de las personas."
        - ID: GN-CONC8-FONDO-GENERO-01
          Cpt: "Fondo Equidad de Género"
          Purp:
            - "Financiar iniciativas para disminuir brechas y violencia de género."
            - "Financiar iniciativas que contribuyan a la autonomía de la mujer (social, laboral, económica)."
            - "Financiar iniciativas que promuevan asociatividad, liderazgo femenino, corresponsabilidad y empoderamiento."
            - "Financiar iniciativas para disminuir la discriminación hacia personas LGBTI+."
        - ID: GN-CONC8-FONDO-DEPORTE-01
          Cpt: "Fondo de Deporte"
          Purp:
            - "Financiar iniciativas deportivas, formativas, recreativas e inclusivas."
            - "Apoyar competencias a nivel provincial, regional, nacional e internacional."
        - ID: GN-CONC8-FONDO-AM-01
          Cpt: "Fondo para Personas Mayores"
          Purp:
            - "Fomentar la participación de adultos mayores en actividades sociales, deportivas y culturales para un envejecimiento activo."
            - "Apoyar la vida diaria de adultos mayores con dependencia moderada o severa, resguardando su autonomía y dignidad."
        - ID: GN-CONC8-FONDO-MEDIOAMB-01
          Cpt: "Fondo de Medio Ambiente"
          Purp:
            - "Financiar iniciativas que protejan el medioambiente y promuevan la educación ambiental."
            - "Financiar mantenimiento de parques, áreas verdes y jardines botánicos."
            - "Financiar operación de instalaciones para tratamiento de residuos sólidos, reciclaje y valorización."
            - "Financiar actividades relacionadas con adopción, rescate, atención veterinaria y gestión de residuos de animales."
        - ID: GN-CONC8-FONDO-SEG-01
          Cpt: "Fondo Seguridad Ciudadana"
          Purp:
            - "Financiar iniciativas para la prevención de delitos y emergencias, incluyendo equipamiento y recuperación de espacios públicos."

    Requisitos_Admisibilidad_Documental_Privados:
      ID: GN-CONC8-REQ-ADMIS-PRIV-01
      Req:
        - "Toda iniciativa debe presentar obligatoriamente la documentación exigida en el instructivo."
        - "Los documentos deben ser ingresados en la plataforma de postulación en formato PDF o JPG."
      Lista_Documentos_Obligatorios:
        ID: GN-CONC8-DOC-OBLIG-PRIV-01
        Ctx: "Instituciones Privadas sin Fines de Lucro."
        Req:
          - "Carta de solicitud de recursos dirigida al Gobernador Regional."
          - "Carta de aceptación de términos y condiciones del Concurso."
          - "Fotocopia del RUT de la Institución (legible)."
          - "Fotocopia de la Cédula de Identidad del Representante Legal (ambos lados)."
          - "Carta de presentación y experiencia de la organización."
          - "Certificado de Directorio Vigente (emitido por Registro Civil u otra entidad competente, con antigüedad máxima de 30 días)."
          - "Para Corporaciones, Fundaciones y ONG: copia autorizada de escritura de constitución, extracto de publicación del Decreto de personalidad jurídica y certificado de vigencia del Ministerio de Justicia."
          - "Certificado de Inscripción en el Registro Único de Personas Jurídicas Receptoras de Fondos Públicos (www.registros19862.cl), actualizado con directorio vigente."
          - "Fotocopia o pantallazo de libreta de ahorro, cartola o certificado bancario que indique número y tipo de cuenta de la Institución (legible)."
          - "Carta de apoyo a la iniciativa y autorización de uso de espacio público (si aplica)."
          - "Carta de compromiso de prevención de la violencia, consumo de drogas y alcohol."
          - "Declaración jurada sobre restricciones (letras b y c)."
          - "Declaración jurada sobre restricciones (letra m)."
          - "Cotizaciones (una por ítem: Equipamiento; Gestión y producción; Difusión)."
          - "Formulario de presentación de la iniciativa (incluyendo nombre, correo y vínculo del formulador)."
          - "Planilla de Presupuesto de la Iniciativa."
        Warn:
          - "El monto solicitado debe coincidir en el formulario, la carta de solicitud y la planilla de presupuesto; inconsistencias resultan en inadmisibilidad."
      Anexos_Descargables_Web:
        ID: GN-CONC8-ANEXOS-WEB-01
        Ctx:
          - "Los formatos de anexos editables están disponibles en la web del Gobierno Regional."

  Sec_2_Reglas_Transversales_Privados:
    ID: GN-CONC8-SEC-2-REGLAS-TRANSVERSALES
    Aspectos_Generales:
      ID: GN-CONC8-REGLAS-GRALES-01
      Documentos_Oficiales:
        ID: GN-CONC8-DOC-OFICIALES-01
        Def: "El Instructivo, la planilla presupuestaria y sus anexos son los documentos oficiales del concurso."
        Req:
          - "Las instituciones deben ceñirse fielmente a lo solicitado en dichos documentos."
        Ctx:
          - "La participación implica la aceptación de todas las disposiciones del Instructivo."
      Gratuidad_Actividades:
        ID: GN-CONC8-GRATUIDAD-01
        Req:
          - "Se exigirá gratuidad en las actividades financiadas por el GORE cuando este financie el 100% del proyecto."
      Entrega_Material_Editado:
        ID: GN-CONC8-MATERIAL-EDITADO-01
        Cond:
          - "Aplica a iniciativas cuya finalidad sea la edición de libros, revistas, discos y videos."
        Req:
          - "Se deberá entregar el 10% del tiraje al Gobierno Regional (División de Desarrollo Social y Humano)."
      Coordinacion_Eventos:
        ID: GN-CONC8-COORD-EVENTOS-01
        Req:
          - "Toda invitación a actos de inicio y/o cierre de proyectos debe ser coordinada con la División de Desarrollo Social y Humano."
        Dln:
          - "La coordinación debe realizarse con 10 días de anticipación."
        Instr:
          - "Enviar invitaciones a oficinapartes@goredenuble.cl y secretarioejecutivo@goredenuble.cl."
      Redistribucion_Excedentes:
        ID: GN-CONC8-REDIST-EXCED-01
        Cond:
          - "En caso de existir disponibilidad presupuestaria en algún fondo, el GORE puede redistribuir los excedentes a otros fondos."
      Renuncia_Recursos:
        ID: GN-CONC8-RENUNCIA-REC-01
        Cond:
          - "Aplica a organizaciones beneficiarias que no puedan ejecutar sus iniciativas por fuerza mayor."
        Proc:
          - "Deben ingresar un oficio al Gobernador Regional renunciando a los recursos, indicando motivos y adjuntando voucher de reintegro."
        Ctx:
          - "Una vez formalizada la renuncia, el GORE queda facultado para redistribuir los recursos."
      Plazo_Ejecucion_General:
        ID: GN-CONC8-PLAZO-EJEC-GRAL-01
        Dln:
          - "8 meses una vez transferidos los recursos (incluye el ingreso de la rendición de cuentas)."

    Plazos_y_Modalidad_Postulacion_Privados:
      ID: GN-CONC8-PLAZOS-MODALIDAD-PRIV-01
      Aceptacion_Terminos:
        ID: GN-CONC8-ACEPT-TERM-01
        Req:
          - "Cada institución postulante declara conocer y aceptar el contenido íntegro del Instructivo General y sus Anexos."
      Modalidad_Postulacion:
        ID: GN-CONC8-MODALIDAD-POST-01
        Mech:
          - "Las organizaciones deben ingresar a www.goredenuble.cl y subir los antecedentes al link habilitado."
      Contenido_Postulacion:
        ID: GN-CONC8-CONTENIDO-POST-01
        Req:
          - "El proyecto debe ser descrito detalladamente con estricto apego al instructivo."
      Cotizaciones:
        ID: GN-CONC8-COTIZACIONES-01
        Resp:
          - "Es responsabilidad de la organización presentar una cotización por cada ítem presupuestario (equipamiento, gestión y producción, difusión)."
        Ctx:
          - "Se consideran válidos los pantallazos de productos cotizados por internet."
      Apoyo_Postulante:
        ID: GN-CONC8-APOYO-POST-01
        Act:
          - "Se generarán jornadas de capacitación por comuna, coordinadas a través de los municipios."
      Cierre_Proceso:
        ID: GN-CONC8-CIERRE-PROCESO-01
        Dln:
          - "El cierre será automático el último día de postulación a las 23:59 horas."
        Warn:
          - "Se sugiere ingresar la información con anticipación debido a la capacidad limitada de las redes de internet."

    Guia_Practica_Formulario_En_Linea_Privados:
      ID: GN-CONC8-GUIA-FORM-ONLINE-PRIV-01
      Purp: "Detallar paso a paso el proceso de postulación en la plataforma en línea para instituciones privadas."
      Req:
        - "Tener todos los documentos requeridos digitalizados (PDF, JPG, PNG) antes de iniciar."
      Secciones:
        - ID: GN-CONC8-GUIA-PRIV-S1-CARGA-DOC-01
          Cpt: "Sección 1 – Carga de documentos"
          Purp: "Adjuntar toda la documentación obligatoria."
        - ID: GN-CONC8-GUIA-PRIV-S2-DATOS-01
          Cpt: "Sección 2 – Datos de institución e iniciativa"
        - ID: GN-CONC8-GUIA-PRIV-S3-DATOS-ESPEC-01
          Cpt: "Sección 3 – Datos específicos"
        - ID: GN-CONC8-GUIA-PRIV-S4-FORMULACION-01
          Cpt: "Sección 4 – Formulación del proyecto"
        - ID: GN-CONC8-GUIA-PRIV-S5-PRESUPUESTO-01
          Cpt: "Sección 5 – Presupuesto"
        - ID: GN-CONC8-GUIA-PRIV-S6-FORMULADOR-01
          Cpt: "Sección 6 – Datos del formulador"
        - ID: GN-CONC8-GUIA-PRIV-S7-ENVIO-01
          Cpt: "Sección 7 – Enviar formulario"

  Sec_3_Fondo_Cultura:
    ID: GN-CONC8-SEC-3-FONDO-CULTURA
    Objetivo_y_Participantes:
      ID: GN-CONC8-FC-OBJ-PART-01
      Obj:
        - "Fortalecer y promover la identidad de la Región de Ñuble como eje de desarrollo, poniendo en valor sus elementos constitutivos."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales de antigüedad (2 años), domicilio en Ñuble y ausencia de rendiciones pendientes."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto_y_Montos:
      ID: GN-CONC8-FC-PRESUP-01
      Monto_Total_Fondo:
        Def: "$600.000.000."
      Distribucion_Especial:
        Ctx:
          - "$50.000.000 para representación artística y cultural (regional, interregional, nacional, internacional) y literatura."
          - "$120.000.000 para producción de películas (artes audiovisuales)."
          - "$50.000.000 para producción de festivales de cine, música o teatro."
          - "$50.000.000 para creación y elaboración de libros."
      Plazo_Especial_Postulacion:
        Ctx:
          - "Para el área de representación y creación de libros, la postulación está abierta hasta el 15 de octubre de 2025 o hasta agotar presupuesto."
      Requisito_Especial_Representacion:
        Req:
          - "Para iniciativas de representación, adjuntar certificado de la organización respectiva que acredite el derecho a representar."
      Excepcion_Postulacion:
        Ctx:
          - "Instituciones pueden presentar hasta dos iniciativas si una es para representación (regional, nacional o internacional)."
    Gastos_Financiables:
      ID: GN-CONC8-FC-GASTOS-01
      Warn:
        - "Si la iniciativa sobrepasa los montos establecidos, el GORE queda facultado para ajustar el presupuesto."
      Tabla_Gastos_Especificos:
        ID: GN-CONC8-FC-GASTOS-TABLA-01
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que permanecen post-proyecto.|- Req: Todo lo adquirido debe llevar logo del GORE, año y fondo. - Ctx: El costo de la gráfica debe incluirse en la iniciativa.|
            |Gestión y Producción|- Def: Gastos en actividades directas del proyecto; materiales fungibles.|- Cpt: Gastos-Permitidos   - Act: Arriendo de servicios.   - Prohib: Arriendo/traslado de animales.   - Act: Alimentación/colaciones saludables (máx. $10.000 por persona).   - Act: Materiales e insumos para talleres.   - Act: Servicios de producción de eventos (pago artistas, ficha técnica, etc.).   - Req: Si es servicio integral, debe adjuntar contrato.|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Cpt: Medios   - Ctx: Medios escritos, radio, TV; pasacalles, palomas. - Req: Debe incluir logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (profesionales, técnicos, talleristas, monitores).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos/Talleristas: $23.000.   - Monitores: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados (título, capacitaciones), cert. antecedentes, cert. inhabilidades (si aplica), informe de actividades, lista de beneficiarios.|
      Consideraciones_Adicionales:
        ID: GN-CONC8-FC-CONSID-ADIC-01
        Gestion_Produccion:
          Req:
            - "Productoras de eventos deben tener giro acorde y se debe firmar un contrato que detalle los servicios."
        Gastos_Iniciativa:
          Warn:
            - "Modificaciones al presupuesto requieren autorización formal previa del GORE."
        Plazo_Ejecucion:
          Dln:
            - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FC-AREAS-MONTOS-01
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Artes escénicas|Purp: Financiar presentaciones/eventos de danza, teatro, arte circense, montajes, itinerancia, seminarios, festivales y talleres de capacitación.|
            |Artes audiovisuales|Purp: Financiar iniciativas de ciclos de cine, producción de videos y documentales con énfasis en patrimonio, identidad y diversidad cultural regional.|
            |Artes visuales|Purp: Financiar creación, formación y difusión de obras (pintura, grabado, fotografía, escultura, murales), exposiciones y talleres.|
            |Artes musicales y teatrales|Purp: Financiar iniciativas de producciones, talleres, presentaciones, itinerancias, grupos musicales (incluida música ranchera), edición de obras, y festivales de cine, música y teatro con impacto regional.|
            |Artes literatura|Purp: Fomentar la lectura, publicaciones de obras, eventos literarios, revistas culturales, concursos de creación literaria, talleres y seminarios.|
            |Cultura tradicional|Purp: Financiar capacitaciones, talleres, ferias (campesinas, artesanales, culturales) y eventos de música/danza que promuevan el patrimonio cultural y rural.|
            |Cultura y ciencias|Purp: Apoyar iniciativas de divulgación científica y tecnológica (charlas, talleres, ferias científicas, exposiciones interactivas, material didáctico).|
            |Patrimonio cultural|Purp: Financiar actividades de rescate del patrimonio material e inmaterial.|
            |Representación (Regional/Interregional/Nacional/Internacional)|Purp: Apoyar a organizaciones culturales para participar en eventos, proyectando la diversidad cultural de Ñuble.|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Artes (escénicas, audiovisuales, visuales, musicales, literatura), Cultura tradicional, Patrimonio cultural|Instituciones Privadas (Universidades, Corporaciones, Asociaciones de Municipalidades)|$ 5.000.000|
            |Artes (escénicas, audiovisuales, visuales, musicales, literatura), Cultura tradicional, Patrimonio cultural|Agrupaciones Culturales (Conjuntos Folclóricos, Fundaciones, Centros Culturales, Bandas, etc.)|$ 3.500.000|
            |Artes (escénicas, audiovisuales, visuales, musicales, literatura), Cultura tradicional, Patrimonio cultural|Otras Organizaciones (Juntas de Vecinos, Comités de Adelanto, Centros de Padres, Organizaciones Juveniles, etc.)|$ 2.500.000|
            |Cultura y Ciencias|Universidades, Corporaciones, Asociaciones de Municipalidades, Centros de Padres, Organizaciones Juveniles, etc.|$ 5.000.000|
            |Producción de Películas|Instituciones Privadas (Agrupaciones, Fundaciones, Corporaciones, ONG Culturales)|Hasta $ 60.000.000|
            |Festivales (Cine, Música, Teatro)|Instituciones Privadas (Agrupaciones, Fundaciones, Corporaciones, ONG Culturales)|Hasta $ 20.000.000|
            |Creación y elaboración de libros|Instituciones Privadas (Agrupaciones, Fundaciones, Centros Culturales, Grupos Literarios, Juntas de Vecinos)|Hasta $ 10.000.000|
            |Representación (Regional/Interregional/Nacional/Internacional)|Instituciones Privadas (Agrupaciones Culturales, Conjuntos Folclóricos, Fundaciones, etc.)|Hasta $ 5.000.000|

  Sec_4_Fondo_Social_e_Inclusion:
    ID: GN-CONC8-SEC-4-FONDO-SOCIAL
    Objetivo_y_Participantes:
      ID: GN-CONC8-FS-OBJ-PART-01
      Obj:
        - "Contribuir al fortalecimiento del tejido social y a la mejora de la calidad de vida comunitaria."
      Mech:
        - "Ejecución de iniciativas participativas que promuevan la inclusión, cohesión social y desarrollo de capacidades en organizaciones territoriales y sociales."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales de antigüedad (2 años), domicilio en Ñuble y sin rendiciones pendientes."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto:
      ID: GN-CONC8-FS-PRESUP-01
      Monto_Total_Fondo:
        Def: "$500.000.000."
    Gastos_Financiables:
      ID: GN-CONC8-FS-GASTOS-01
      Warn:
        - "Si la iniciativa sobrepasa los montos establecidos, el GORE queda facultado para ajustar el presupuesto."
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que permanecen post-proyecto.|- Req: Todo lo adquirido debe llevar logo del GORE, año y fondo. - Ctx: El costo de la gráfica debe incluirse en la iniciativa.|
            |Gestión y Producción|- Def: Gastos en actividades directas del proyecto; materiales fungibles.|- Cpt: Gastos-Permitidos   - Act: Arriendo de servicios.   - Act: Alimentación/colaciones saludables (máx. $10.000 por persona).   - Act: Materiales e insumos para talleres.   - Act: Servicios de producción de eventos.   - Req: Si es servicio integral, debe adjuntar contrato.|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Cpt: Medios   - Ctx: Medios escritos, radio, TV, artículos de difusión (lápices, bolsas de tela, etc.). - Req: Debe incluir logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (profesionales, técnicos, monitores).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos: $23.000.   - Monitores/Talleristas: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados (título, capacitaciones), cert. antecedentes, cert. inhabilidades (si aplica), informe de actividades, lista de beneficiarios.|
      Consideraciones_Adicionales:
        ID: GN-CONC8-FS-CONSID-ADIC-01
        Gestion_Produccion:
          Req:
            - "Productoras de eventos deben tener giro acorde y se debe firmar un contrato que detalle los servicios."
        Gastos_Iniciativa:
          Warn:
            - "Modificaciones al presupuesto requieren autorización formal previa del GORE."
        Plazo_Ejecucion:
          Dln:
            - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FS-AREAS-MONTOS-01
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Social|Prioriza el fortalecimiento de organizaciones a través de encuentros y talleres sobre participación, autonomía, liderazgo y comunicación.|
            |Inclusión Social|Financia iniciativas (talleres, charlas, material informativo) para mejorar la calidad de vida y acceso a derechos de grupos prioritarios (pueblos originarios, personas mayores, migrantes, personas con discapacidad, NNA, población LGBTQ+, mujeres).|
            |Prevención Psicosocial|Financia proyectos para disminuir factores de riesgo y potenciar factores protectores (prevención consumo de sustancias, rehabilitación de adicciones, prevención comunitaria, prevención terciaria y secundaria).|
            |Residencias Mejor Niñez|Apoya organismos colaboradores de Mejor Niñez para fortalecimiento de residencias familiares (equipamiento y vestuario).|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Residencias Mejor Niñez|Organismos Colaboradores Mejor Niñez (Exclusivo para residencias)|$ 10.000.000 (por residencia)|
            |Social, Inclusión, Prevención Psicosocial|Instituciones Privadas (Universidades, Corporaciones, Asoc. de Municipalidades)|$ 5.500.000|
            |Social, Inclusión, Prevención Psicosocial|Organizaciones Territoriales, Funcionales y/o de Base|$ 3.500.000|

  Sec_5_Fondo_Equidad_de_Genero:
    ID: GN-CONC8-SEC-5-FONDO-GENERO
    Objetivo_y_Participantes:
      ID: GN-CONC8-FG-OBJ-PART-01
      Objetivos_Concurso:
        Obj:
          - "Promover iniciativas que disminuyan brechas y violencias de género, fomentando formación, asociatividad, empoderamiento, liderazgo y autonomía de las mujeres."
          - "Promover iniciativas que disminuyan brechas y discriminaciones que afecten a la comunidad LGBTIQA+."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales de antigüedad (2 años), domicilio en Ñuble y sin rendiciones pendientes."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto:
      ID: GN-CONC8-FG-PRESUP-01
      Monto_Total_Fondo:
        Def: "$400.000.000."
    Gastos_Financiables:
      ID: GN-CONC8-FG-GASTOS-01
      Warn:
        - "Si la iniciativa sobrepasa los montos establecidos, el GORE queda facultado para ajustar el presupuesto."
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que permanecen post-proyecto.|- Req: Todo lo adquirido debe llevar logo del GORE, año y fondo.|
            |Gestión y Producción|- Def: Gastos en actividades directas del proyecto; materiales fungibles.|- Cpt: Gastos-Permitidos   - Act: Arriendo de servicios.   - Act: Alimentación/colaciones saludables (máx. $10.000 por persona).   - Act: Materiales e insumos para talleres.   - Act: Servicios de producción de eventos.   - Req: Si es servicio integral, debe adjuntar contrato.|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Cpt: Medios.   - Ctx: Medios escritos, radio, TV. - Req: Debe incluir logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (profesionales, técnicos, monitores).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos: $23.000.   - Monitores/Talleristas: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados, cert. antecedentes, cert. inhabilidades (si aplica), informe de actividades, lista de beneficiarios.|
      Consideraciones_Adicionales:
        ID: GN-CONC8-FG-CONSID-ADIC-01
        Gestion_Produccion:
          Req:
            - "Productoras de eventos deben tener giro acorde y se debe firmar un contrato que detalle los servicios."
        Gastos_Iniciativa:
          Warn:
            - "Modificaciones al presupuesto requieren autorización formal previa del GORE."
        Plazo_Ejecucion:
          Dln:
            - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FG-AREAS-MONTOS-01
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Prevención y sensibilización|Financia acciones de sensibilización y prevención de la violencia contra las mujeres y niñas, y actividades para bienestar e inserción de mujeres.|
            |Formación y autonomía financiera de la mujer|Financia iniciativas (talleres, ferias, capacitaciones) que contribuyan a asociatividad, formación y/o autonomía económica de las mujeres.|
            |Mujer rural|Potencia el trabajo y crecimiento de mujeres rurales, apoyando emprendimientos agrícolas, iniciativas comunitarias, asesorías técnicas o capacitación.|
            |Diversidad sexual y de género|Financia actividades que permitan erradicar violencia, prejuicios y discriminación por orientación sexual, identidad y expresión de género o características sexuales.|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Prevención y sensibilización; Mujer Rural; Diversidad sexual y de género|Organizaciones Territoriales, Funcionales y/o de Base|$3.500.000|
            |Formación y autonomía financiera de la mujer|Instituciones Privadas (Universidades, Corporaciones, Fundaciones, Asoc. de Municipalidades)|$6.500.000|
            |Formación y autonomía financiera de la mujer|Organizaciones Territoriales, Funcionales y/o de Base|$3.500.000|

  Sec_6_Fondo_Deporte:
    ID: GN-CONC8-SEC-6-FONDO-DEPORTE
    Objetivo_y_Participantes:
      ID: GN-CONC8-FD-OBJ-PART-01
      Objetivos_Concurso:
        Obj:
          - "Promover y potenciar iniciativas de carácter deportivo, formativo, recreativo e inclusivo."
          - "Apoyar competencias a nivel comunal, provincial, regional, interregional, nacional e internacional."
          - "Fortalecer la representación de deportistas a nivel regional, interregional, nacional e internacional."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales de antigüedad (2 años), domicilio en Ñuble y sin rendiciones pendientes."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto_y_Montos:
      ID: GN-CONC8-FD-PRESUP-01
      Monto_Total_Fondo:
        Def: "$1.000.000.000."
      Distribucion_Especial:
        Ctx:
          - "$100.000.000 para el área de representación de deportistas (regional, interregional, nacional e internacional)."
          - "$100.000.000 para el área de organización y promoción de actividades deportivas."
      Plazo_Especial_Postulacion:
        Ctx:
          - "Para el área de representación, la postulación está abierta hasta el 15 de octubre de 2025 o hasta agotar presupuesto."
      Requisito_Especial_Representacion:
        Req:
          - "Para iniciativas de representación, adjuntar certificado emitido por la asociación, federación, IND, Comité Olímpico/Paralímpico u otra entidad que acredite el derecho a representar."
      Excepcion_Postulacion:
        Ctx:
          - "Instituciones pueden presentar hasta dos iniciativas si una de ellas está dirigida a las áreas de representación (regional, nacional o internacional)."
    Gastos_Financiables:
      ID: GN-CONC8-FD-GASTOS-01
      Warn:
        - "Si la iniciativa sobrepasa los montos establecidos, el GORE queda facultado para ajustar el presupuesto."
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que subsistan después del proyecto (tableros, arcos, vestuario, etc.).|- Req: Todo lo adquirido debe llevar logo del GORE y año de financiamiento.|
            |Gestión y Producción|- Def: Gastos en actividades directas del proyecto (arriendo, traslados, vestuario deportivo, balones, trofeos, alimentación, alojamiento).|- Cpt: Gastos-Permitidos   - Act: Colaciones saludables (máx. $10.000 por persona). - Prohib: No se financian planes de internet ni servicios básicos.|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Cpt: Medios   - Ctx: Medios escritos, radiales, TV. - Req: Debe incluir logo GORE, nombre proyecto, monto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (Profesionales, Educadores, Monitores, Talleristas, Árbitros, Cronometristas, Planilleros).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos Nivel Superior: $23.000.   - Monitores/Talleristas/Árbitros: $18.000.   - Cronometristas/Planilleros: $12.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados (título, inhabilidades, antecedentes), informe de actividades.|
      Consideraciones_Adicionales:
        ID: GN-CONC8-FD-CONSID-ADIC-01
        Gestion_Produccion:
          Req:
            - "Productoras de eventos deben tener giro acorde y se debe firmar un contrato que detalle los servicios."
        Gastos_Iniciativa:
          Warn:
            - "Modificaciones al presupuesto requieren autorización formal previa del GORE."
        Plazo_Ejecucion:
          Dln:
            - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FD-AREAS-MONTOS-01
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Formación para el Deporte|Financia escuelas deportivas y cursos formativos para árbitros, entrenadores, etc. (70% del financiamiento en honorarios).|
            |Deporte Recreativo|Financia iniciativas para práctica de actividad física y deportiva (talleres, eventos, yoga, zumba, cuadrangulares).|
            |Deporte de Competición|Financia organización, participación y preparación para actividades competitivas.|
            |Deporte Inclusivo|Financia iniciativas que aborden temáticas de inclusión en todos sus ámbitos.|
            |Organización y Promoción de Actividades Deportivas|Fomenta el deporte y la integración comunitaria mediante eventos deportivos regionales, nacionales e internacionales.|
            |Representación de Deportistas (Regional/Interregional)|Financia iniciativas dirigidas a representación y fortalecimiento integral de deportistas a nivel regional e interregional.|
            |Representación de Deportistas (Nacional/Internacional)|Financia iniciativas dirigidas a representación y fortalecimiento integral de deportistas a nivel nacional e internacional.|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Deporte Recreativo, Inclusivo, Competición y Formación|Asociaciones Deportivas Regionales.|$ 10.000.000|
            |Deporte Recreativo, Inclusivo, Competición y Formación|Uniones comunales deportivas, Asociaciones deportivas comunales, Federaciones Deportivas.|$ 6.000.000|
            |Deporte Recreativo e Inclusivo|Universidades, Corporaciones, Asoc. de Municipalidades.|$ 4.000.000|
            |Deporte Recreativo e Inclusivo|Juntas de Vecinos, Agrupaciones de Discapacitados, Fundaciones, etc.|$ 1.800.000|
            |Deporte de Competición|Organizaciones deportivas, Clubes Deportivos, Clubes de Huasos.|$ 1.800.000|
            |Organización y Promoción de Actividades Deportivas|Organizaciones deportivas, Clubes, Uniones, Asociaciones, Federaciones.|Hasta $30.000.000|
            |Formación para el Deporte|Organizaciones deportivas, Clubes, Uniones, Asociaciones, Federaciones, JJVV, etc.|$ 6.000.000|
            |Representación (Regional/Interregional)|Organizaciones deportivas, Clubes, Uniones, Asociaciones, Federaciones.|$ 3.000.000|
            |Representación (Nacional/Internacional)|Organizaciones deportivas, Clubes, Uniones, Asociaciones, Federaciones.|$ 5.000.000|

  Sec_7_Fondo_Personas_Mayores:
    ID: GN-CONC8-SEC-7-FONDO-PERSONAS-MAYORES
    Objetivo_y_Participantes:
      ID: GN-CONC8-FAM-OBJ-PART-01
      Objetivos_Concurso:
        Obj:
          - "Potenciar actividades de cuidado y autocuidado para mejorar el bienestar físico y cognitivo de las personas mayores."
          - "Fortalecer habilidades sociales e instancias de inclusión social de personas mayores."
          - "Incentivar proyectos que mejoren la condición de bienestar de personas mayores en situación de dependencia y/o discapacidad."
      Participantes:
        Req:
          - "Postulación exclusiva para Organizaciones de Adulto Mayor (clubes, uniones comunales, federaciones, confederaciones)."
        Ctx:
          - "Deben tener al menos 2 años de antigüedad, domicilio en la Región de Ñuble, demostrar experiencia y no tener rendiciones pendientes."
    Presupuesto:
      ID: GN-CONC8-FAM-PRESUP-01
      Monto_Total_Fondo:
        Def: "$400.000.000."
    Gastos_Financiables:
      ID: GN-CONC8-FAM-GASTOS-01
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes para desarrollar las actividades (audífonos, colchón antiescaras, lentes, silla de ruedas, ayudas técnicas, instrumentos musicales, etc.).|- Ctx: Compra de PC, notebook, televisores, etc., será analizada según pertinencia y debe ser justificada. - Req: Debe llevar logo del GORE.|
            |Gestión y Producción|- Def: Gasto necesario para la ejecución que no perdura post-actividad.|- Ex: Arriendo, traslados, sábanas, kits de aseo, pañales, botiquines, materiales para talleres, vestimenta deportiva. - Cpt: Gastos-Permitidos   - Act: Colaciones saludables (máx. $10.000 por persona). - Prohib: No se financian planes de internet ni servicios básicos.|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Cpt: Medios   - Ctx: Medios escritos, radio, TV. - Req: Debe incluir logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano para actividades en beneficio integral de las personas mayores.|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos Nivel Superior: $23.000.   - Monitores/Talleristas/Facilitadores: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados (título, inhabilidades, antecedentes), informe de actividades.|
      Consideraciones_Adicionales:
        ID: GN-CONC8-FAM-CONSID-ADIC-01
        Gestion_Produccion:
          Req:
            - "Productoras deben tener giro acorde y plan de trabajo detallado."
        Plazo_Ejecucion:
          Dln:
            - "8 meses desde la transferencia de recursos."
    Areas_y_Montos:
      ID: GN-CONC8-FAM-AREAS-MONTOS-01
      Postulantes_Exclusivos:
        Def: "Clubes de adulto mayor, Uniones Comunales, Federaciones y Confederaciones de Adulto Mayor."
      Monto_Maximo_General:
        Def: "$2.500.000 para todas las áreas."
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Social Adulto Mayor|Desarrolla talleres y actividades de cuidado, autocuidado o autovalencia para la prevención del deterioro físico-cognitivo (operativos de salud, talleres de estimulación cognitiva, terapias alternativas, viajes terapéuticos, etc.).|
            |Deporte Adulto Mayor|Desarrolla talleres para envejecimiento activo y actividades al aire libre (yoga, baile entretenido, caminatas, gimnasia, olimpiadas, acondicionamiento físico).|
            |Cultura Adulto Mayor|Desarrolla actividades de recreación, esparcimiento o educación cultural (viajes patrimoniales, talleres de música/danza, manualidades, artesanías, ferias y exposiciones).|
      Restriccion_Postulacion_Otros_Fondos:
        Warn:
          - "Las organizaciones de adulto mayor no podrán postular a otros fondos del concurso."

  Sec_8_Fondo_Medio_Ambiente:
    ID: GN-CONC8-SEC-8-FONDO-MEDIO-AMBIENTE
    Objetivo_y_Participantes:
      ID: GN-CONC8-FMA-OBJ-PART-01
      Obj:
        - "Promover e incentivar iniciativas para el cuidado y protección del medio ambiente, fomentando la educación ambiental, el desarrollo sustentable y la tenencia responsable de mascotas."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto_y_Asignacion:
      ID: GN-CONC8-FMA-PRESUP-01
      Monto_Total_Fondo:
        Def: "$400.000.000."
      Asignacion_Especial:
        Ctx:
          - "$25.000.000 se destinarán a 'Habilitación de senderos comunitarios sostenibles' dentro del área de Biodiversidad y Desarrollo Sustentable."
    Gastos_Financiables:
      ID: GN-CONC8-FMA-GASTOS-01
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que permanecen post-proyecto.|- Req: Todo lo adquirido debe llevar logo del GORE, año y fondo.|
            |Gestión y Producción|- Def: Material fungible que se consume durante la actividad.|- Ex: Arriendo de equipos, traslados, insumos (semillas, árboles), alimentación (tope $10.000/persona). - Cond: Para ferias medioambientales, se financia producción (iluminación, amplificación, stands).|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Ex: Medios escritos, radio, TV, artículos como lápices, bolsas, etc. - Req: Deben ser de material reciclable y llevar logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (Profesionales, Educadores, Monitores).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos: $23.000.   - Monitores/Talleristas: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados, cert. antecedentes, cert. inhabilidades (si aplica), informe de actividades.|
      Plazo_Ejecucion:
        Dln:
          - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FMA-AREAS-MONTOS-01
      Tabla_Areas:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Biodiversidad y Desarrollo Sustentable|Financia talleres de protección y conservación; material educativo; habilitación de senderos comunitarios sostenibles; iniciativas de adaptación al cambio climático y uso eficiente de recursos.|
            |Educación Ambiental, Eficiencia Hídrica y Energética|Financia talleres sobre manejo de residuos (compostaje, lombricultura); seminarios sobre cambio climático; huertos orgánicos; iniciativas de ahorro de agua (recolección de aguas lluvias, reutilización de aguas grises); iniciativas de eficiencia energética (paneles fotovoltaicos, termo paneles, turbinas eólicas).|
            |Limpieza De Focos De Basura|Financia proyectos de recuperación de áreas verdes o sitios abandonados; limpieza de borde costero y playas, con trabajo comunitario.|
            |Tenencia responsable de mascotas, esterilización e implante de chip|Financia operativos de esterilización con chip; desparasitación; charlas de tenencia responsable; compra de alimentos e insumos para organizaciones de cuidado y rescate; charlas sobre prevención de enfermedades zoonóticas (procedimientos realizados por médico veterinario).|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Todas las áreas|Instituciones Privadas y Organizaciones Territoriales/Funcionales|- General: $6.500.000. - Base: $3.500.000.|
            |Eficiencia Hídrica y Energética (paneles fotovoltaicos)|Comités de Agua Potable Rural (APR)|$ 6.000.000|
            |Biodiversidad y Desarrollo Sustentable (senderos)|Organizaciones con objetivos de conservación y protección del medio ambiente|$ 25.000.000|

  Sec_9_Fondo_Seguridad_Ciudadana:
    ID: GN-CONC8-SEC-9-FONDO-SEGURIDAD
    Objetivo_y_Participantes:
      ID: GN-CONC8-FSEG-OBJ-PART-01
      Obj:
        - "Mejorar la seguridad humana financiando proyectos que disminuyan factores de riesgo mediante acciones comunitarias y equipamiento para prevenir delitos y/o emergencias."
      Participantes:
        Req:
          - "Instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y comunitarias."
        Ctx:
          - "Aplican requisitos generales."
        Prohib:
          - "Las organizaciones de adulto mayor no pueden acceder a este fondo."
    Presupuesto:
      ID: GN-CONC8-FSEG-PRESUP-01
      Monto_Total_Fondo:
        Def: "$1.550.000.000."
      Monto_Tope_Postulacion:
        Def: "$5.500.000 por cada organización social."
      Criterio_Adjudicacion:
        Def: "Se financiarán las iniciativas que obtengan el mayor puntaje de prelación en la evaluación técnico-financiera."
    Gastos_Financiables:
      ID: GN-CONC8-FSEG-GASTOS-01
      Tabla_Gastos_Especificos:
        Tabla:
          Ctx: |
            |Ítem|Tipo de Gasto|Consideraciones Específicas|
            |-|-|-|
            |Equipamiento|- Def: Adquisición de bienes indispensables que permanecen post-proyecto.|- Req: Todo lo adquirido debe llevar logo del GORE, año y fondo.|
            |Gestión y Producción|- Def: Material fungible que se consume durante la actividad.|N/A|
            |Difusión|- Req: Obligatorio, 3-10% del presupuesto.|- Req: Debe incluir logo GORE, nombre proyecto y fuente de financiamiento.|
            |Honorarios|- Def: Recurso humano (Profesionales, Educadores, Monitores).|- Cpt: Valores-Hora   - Ctx: Profesionales: $25.000.   - Técnicos: $23.000.   - Monitores/Talleristas: $18.000. - Cpt: Requisitos-Rendición   - Req: CV, certificados, cert. antecedentes, cert. inhabilidades (si aplica), informe de actividades.|
      Plazo_Ejecucion:
        Dln:
          - "8 meses desde la transferencia de recursos."
    Areas_y_Montos_Tope:
      ID: GN-CONC8-FSEG-AREAS-MONTOS-01
      Responsable_Tecnico:
        Resp:
          - "El proceso de este fondo es de responsabilidad de la Unidad CIES del GORE Ñuble."
      Tabla_Areas_y_Tipologias:
        Tabla:
          Ctx: |
            |Área de Postulación|Tipología de Proyecto y Especificaciones Técnicas Mínimas|
            |-|-|
            |Prevención Situacional|Incluye cámaras de televigilancia, iluminación peatonal, sistemas de alerta comunitaria, con especificaciones de potencia, estándares y requisitos organizativos.|
            |Prevención de Riesgos de Desastres|Incluye recuperación de espacios públicos, kits de prevención de incendios y apoyo a la escasez hídrica (contenedores de agua, generadores para APR).|
      Tabla_Montos_Tope:
        Tabla:
          Ctx: |
            |Área(s)|Tipo de Institución|Monto Tope por Proyecto|
            |-|-|-|
            |Prevención Situacional / Prevención de Riesgos de Desastres|Organizaciones Territoriales, Funcionales y/o de Base|$ 5.500.000|

  Sec_10_Reglas_Municipalidades:
    ID: GN-CONC8-SEC-10-MUNICIPIOS
    Objetivos_Concurso_Municipios:
      ID: GN-CONC8-MUN-OBJ-01
      Purp: "Entregar orientaciones para la postulación de los municipios al Concurso 8% 2025."
      Objetivo_General:
        Obj: "Fomentar iniciativas municipales para fortalecer la identidad cultural y la seguridad comunitaria, promoviendo la participación ciudadana y acciones preventivas."
      Objetivos_Especificos:
        Obj:
          - "Impulsar iniciativas de participación comunitaria en torno a expresiones artísticas, culturales y patrimoniales en las 21 comunas."
          - "Promover iniciativas de recuperación de espacio público y prevención del delito y emergencias."
    Presupuesto_y_Participacion:
      ID: GN-CONC8-MUN-PRESUP-01
      Lineas_Financiamiento:
        - Cpt: "Fondo de Fomento a la Cultura"
          Ctx:
            - "Monto Total: $480.000.000."
            - "Monto Tope por municipio: $22.857.142."
        - Cpt: "Fondo de Seguridad Ciudadana"
          Ctx:
            - "Monto Total: $250.000.000."
            - "Monto Tope por municipio: $25.000.000."
            - "Se financiarán solo las 10 iniciativas con mayor puntaje de prelación en evaluación técnica."
      Reglas_Participacion:
        Req:
          - "Podrán participar solo las Municipalidades de la Región de Ñuble."
          - "Cada municipalidad podrá postular a una iniciativa del Fondo de Fomento a la Cultura y a una iniciativa del Fondo de Seguridad."
    Areas_Postulacion_Municipios:
      ID: GN-CONC8-MUN-AREAS-01
      Fondo_Cultura:
        Tabla:
          Ctx: |
            |Área|Definición|
            |-|-|
            |Actividades Artísticas, Culturales y Patrimoniales|Financia programas y redes para itinerancia de obras y espectáculos, festivales, muestras artísticas, ferias literarias, exposiciones y otros eventos públicos que fortalezcan la identidad cultural.|
      Fondo_Seguridad:
        Tabla:
          Ctx: |
            |Área de Postulación|Tipología de Proyecto y Especificaciones Mínimas|
            |-|-|
            |Prevención Situacional|Incluye cámaras de televigilancia, iluminación peatonal, recuperación de espacios públicos.|
            |Equipamiento de Protección Personal|Equipamiento para inspectores/patrulleros municipales (chalecos, cascos, cámaras corporales, radios).|
            |Prevención de Riesgos de Desastres|Sistema de radiocomunicación y sistema de respaldo de suministro eléctrico.|
        Ctx:
          - "Municipios pueden postular a una sola tipología de Prevención Situacional, pero pueden combinar tipologías de equipamiento y prevención de riesgos sin sobrepasar el monto máximo."
    Gastos_Plafzos_Admisibilidad_Municipios:
      ID: GN-CONC8-MUN-GASTOS-PLAZOS-01
      Gastos_Financiables:
        Cpt: "Estructura de gastos (Equipamiento, Gestión y Producción, Difusión, Honorarios) y valores idénticos a fondos para instituciones privadas."
      Plazos_Proceso:
        Ctx: |
          Plazo de postulación: del 16 de junio de 2025 al 16 de julio de 2025.

          |Fase|Actividad|Duración|
          |-|-|-|
          |Postulación|Proceso de postulación para municipalidades (se extiende 3 días hábiles si el link presenta problemas).|15 días hábiles|
          |Admisibilidad y Apelación|Revisión de admisibilidad y plazo para subsanar errores.|5 días hábiles + 5 días hábiles|
          |Evaluación Técnica|Evaluación técnica de las iniciativas.|15 días hábiles|
          |Inicio Transferencia|Publicación de resultados y envío de nóminas.|15 días hábiles|
      Plazo_Ejecucion_Iniciativa:
        Dln:
          - "9 meses una vez transferidos los recursos."
      Documentacion_Admisibilidad:
        Req:
          - "Carta dirigida al Gobernador Regional solicitando los recursos."
          - "Carta de aceptación de términos y condiciones."
          - "Fotocopia del RUT de la Institución (SII)."
          - "Fotocopia de la Cédula de Identidad del Representante Legal (Alcalde/sa)."
          - "Decreto de Nombramiento del Alcalde o Alcaldesa."
          - "Comprobante de cuenta bancaria."
          - "Carta de compromiso de prevención de la violencia, consumo de drogas y alcohol."
          - "Cotizaciones (una por cada ítem: Equipamiento, Gestión y producción, Difusión)."
    Reglas_Restricciones_Evaluacion_Municipios:
      ID: GN-CONC8-MUN-REGLAS-01
      Aspectos_Generales:
        Req:
          - "Gratuidad en actividades si el GORE financia el 100%."
          - "Para edición de libros/revistas/etc., entregar 10% del tiraje al GORE."
          - "Coordinar actos de inicio/cierre con el referente técnico del GORE con 10 días de anticipación."
      Restricciones_y_Gastos_No_Financiables:
        Prohib:
          - "Pago de honorarios a personal del GORE, directores de servicios públicos, autoridades regionales y comunales."
          - "Proyectos que sean exclusivamente adquisición de equipamiento."
          - "Iniciar ejecución o rendir gastos anteriores a la firma del convenio."
          - "Otorgar financiamiento si existen rendiciones pendientes al momento de la transferencia."
          - "Proyectos con formulación copiada."
          - "Gastos en ceremonias de orden social (cócteles, cenas, bebidas alcohólicas), salvo aprobación expresa."
          - "Premios en dinero, compra de animales para premios, gastos de trámites propios de la institución."
      Pauta_Evaluacion_Municipios:
        Ctx: |
          La pauta de evaluación contempla criterios de identificación y formulación,
          cobertura, difusión, coherencia entre proyecto y presupuesto, entre otros,
          con puntaje máximo de 100 puntos. Se considera proyecto recomendado aquel
          con puntaje entre 60 y 100 puntos.

  Sec_11_Seguimiento_Ejecucion_y_Rendicion:
    ID: GN-CONC8-SEC-11-SEGUIMIENTO-RENDICION
    Aprobacion_y_Transferencia:
      ID: GN-CONC8-SEG-APROB-TRANS-01
      Articulo_1:
        Proc:
          - "Unidad de Análisis y Evaluación informa iniciativas recomendadas a la División de Desarrollo Social y Humano o a la Unidad CIES."
          - "Dichas unidades elaboran planillas de beneficiarios y remiten a la División de Presupuesto e Inversión Regional para dictar resolución de transferencia."
        Req:
          - "Para la transferencia se requiere firma de convenio y presentación de documentación complementaria (CI representante legal si cambió, certificado de directorio vigente, pagaré para instituciones privadas, certificado de receptores de fondos actualizado si cambió directiva)."
      Articulo_2:
        Resp:
          - "El representante legal de la institución es el responsable financiero, técnico, administrativo y judicial del proyecto."
        Req:
          - "Si hay cambio de representante legal, se debe informar al GORE con nuevo certificado de directorio y cédula de identidad."
      Articulo_3:
        Req:
          - "La ejecución de gastos puede comenzar solo desde la fecha de transferencia de los recursos."
        Warn:
          - "Gastos anteriores a la transferencia o posteriores al término del proyecto no serán aceptados, salvo aprobación escrita del GORE."
    Garantias_y_Obligaciones:
      ID: GN-CONC8-SEG-GARANTIAS-01
      Articulo_5_7:
        Req:
          - "Instituciones privadas deben presentar un pagaré suscrito ante notario para caucionar el correcto uso de los recursos (no aplica a municipios)."
          - "El pagaré debe tener vigencia de 18 meses desde la firma del convenio y mantenerse vigente durante todo el proyecto, ampliándolo si hay extensión de plazos."
        Proc:
          - "La devolución de la garantía se solicita mediante carta a la Jefatura de la División de Administración y Finanzas, una vez que el proyecto esté completamente ejecutado, rendido, aprobado y con certificados de cierre técnico y financiero."
      Obligaciones_Institucion_Ejecutante:
        ID: GN-CONC8-SEG-OBLIG-01
        Req:
          - "Asistir a reuniones, ceremonias y capacitaciones convocadas por el GORE."
          - "Mantener comunicación constante con la contraparte técnica del GORE."
          - "Recibir a profesionales del GORE para supervisiones en terreno."
          - "Cumplir los objetivos, actividades y gastos definidos en el proyecto."
    Proceso_Rendicion_Cuentas:
      ID: GN-CONC8-SEG-RENDICION-01
      Def:
        - "La rendición de cuentas es el procedimiento por el cual la entidad demuestra que los fondos públicos fueron invertidos correctamente según la normativa."
      Reglas_Generales:
        ID: GN-CONC8-SEG-REND-REGLAS-01
        Cond:
          - "Para proyectos ≤ 500 UTM, el GORE puede autorizar que la rendición se efectúe fuera de la plataforma SISREC."
        Mech:
          - "Instituciones privadas exceptuadas de SISREC rinden en papel con documentación original."
          - "Municipios rinden mensualmente vía SISREC."
        Req:
          - "Todo gasto debe respaldarse con FACTURA (pago al contado) a nombre de la institución ejecutante."
          - "La fecha de la documentación de gasto debe ser posterior a la recepción de recursos y anterior al cierre del proyecto."
          - "El gasto debe ajustarse estrictamente al presupuesto aprobado; modificaciones requieren autorización previa por escrito del referente técnico."
          - "Implementos adquiridos deben permanecer en custodia de la institución; si se ceden a terceros debe existir constancia de recepción conforme."
          - "Actividades como cursos y talleres deben respaldarse con listas de asistencia firmadas."
      Documentacion_Obligatoria_Rendicion:
        ID: GN-CONC8-SEG-REND-DOC-01
        Req:
          - "Oficio conductor."
          - "Informe ejecutivo (Anexo 1)."
          - "Informe financiero (Anexo 2)."
          - "Voucher de recursos recibidos."
          - "Facturas y boletas de honorarios."
          - "Formulario 29 (si aplica)."
          - "Comprobante de reintegro (si aplica)."
          - "Medios de verificación (Anexo 3)."
          - "Informe de actividades de honorarios (Anexo 4)."
          - "Otros anexos según corresponda."
      Formalidades_Documentos_Tributarios:
        ID: GN-CONC8-SEG-REND-TRIB-01
        Facturas:
          Req:
            - "Emitidas a nombre de la institución (no del representante legal)."
            - "Fecha dentro del período de convenio."
            - "Condición de pago 'CONTADO'."
            - "Giro comercial correspondiente."
            - "Detalle del proyecto en la glosa."
        Boletas_Honorarios:
          Req:
            - "Emitidas por el prestador."
            - "Fecha coincidente con las actividades."
            - "Giro correspondiente."
            - "Detalle del proyecto en la glosa."
      Externalizacion_Servicios:
        ID: GN-CONC8-SEG-REND-EXTERN-01
        Def: "Proceso por el cual la institución contrata a un tercero para realizar actividades contempladas en el proyecto."
        Req:
          - "Para obras menores (instalación de cámaras, luminarias, etc.), se debe presentar contrato de prestación de servicios suscrito ante notario y acta de recepción conforme."
          - "Si la ejecución es por una productora, se debe adjuntar contrato de prestación de servicios suscrito ante notario detallando el servicio."
    Analisis_Sanciones_y_Cierre:
      ID: GN-CONC8-SEG-SANCIONES-01
      Analisis_Rendicion:
        Warn:
          - "Si se comprueba adulteración o falsedad en documentos de rendición, el GORE denunciará al Ministerio Público, rechazará el gasto y exigirá la devolución del monto."
      Incumplimientos_y_Inhabilitacion:
        Proc:
          - "A instituciones que no rindan en los plazos se les remitirá oficio de cobro y no podrán ser beneficiarias de nuevos recursos para el siguiente concurso."
          - "Observaciones a la rendición serán informadas por correo; la organización tiene 5 días hábiles para subsanar; de no hacerlo, el gasto será rechazado y se deberá reintegrar el monto."
        Inhabilitacion:
          Def: "El incumplimiento puede configurar causal de inhabilitación para futuras postulaciones."
          Ctx:
            - "2 años por primera vez, 5 años por reincidencia."
        Warn:
          - "Gastos rechazados o no ejecutados deben ser restituidos al GORE."

  Sec_12_Anexos:
    ID: GN-CONC8-SEC-12-ANEXOS
    Purp: "Proporcionar los formularios y documentos estandarizados requeridos para el proceso de postulación y rendición."
    Anexos_Principales:
      - ID: GN-CONC8-ANEXO-1-FORM-POST-PRIVADOS-01
        Cpt: "Formulario de Postulación – Instituciones Privadas"
        Ctx: "Estructura completa del formulario, con secciones de identificación, iniciativa, descripción, plan de trabajo y presupuesto, incluida lógica de validación interna."
      - ID: GN-CONC8-ANEXO-2-FORM-POST-MUNICIPIOS-01
        Cpt: "Formulario de Postulación – Municipalidades"
        Ctx: "Formulario alineado con las líneas de financiamiento de Cultura y Seguridad Ciudadana para municipios, con identificación, iniciativa y presupuesto."
      - ID: GN-CONC8-ANEXO-3-CARTA-SOLICITUD-01
        Cpt: "Carta Solicitud de Recursos"
        Purp: "Formalizar la solicitud de financiamiento al Gobernador Regional."
      - ID: GN-CONC8-ANEXO-4-CARTA-ACEPTACION-01
        Cpt: "Carta de Aceptación de Términos y Condiciones"
        Purp: "Declarar conocimiento y aceptación del instructivo y normativa del concurso."
      - ID: GN-CONC8-ANEXO-5-CARTA-PRESENTACION-01
        Cpt: "Carta de Presentación y Experiencia de la Organización"
      - ID: GN-CONC8-ANEXO-6-DJ-A-RESTRICCIONES-01
        Cpt: "Declaración Jurada Simple A (Restricciones B y C)"
      - ID: GN-CONC8-ANEXO-7-DJ-B-RESTRICCION-M-01
        Cpt: "Declaración Jurada Simple B (Restricción M)"
      - ID: GN-CONC8-ANEXO-8-CARTA-COMPROMISO-PREVENCION-01
        Cpt: "Carta de Compromiso de Prevención (violencia, drogas y alcohol)"

    Anexo_1_Formulario_Postulacion_Privados:
      ID: GN-CONC8-ANEXO-1-FORM-POST-PRIVADOS-01
      Version: "1.0.0"
      Status: "Published"
      Ref_Guide: "GUIDE-SFD-STS-MASTER-01"
      Purp: "Recopilar toda la información requerida de la organización y la iniciativa para postular a los fondos concursables."
      Secciones:
        - ID: GN-CONC8-ANX1-SEC1-ORG
          Titulo: "Sección 1: Identificación de la Organización"
          Campos:
            - ID: GN-CONC8-ANX1-S1-NOMBRE-ORG
              Field-Label: "Nombre de la Organización"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S1-RUT-ORG
              Field-Label: "RUT de la Organización"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: XX.XXX.XXX-X."
            - ID: GN-CONC8-ANX1-S1-DOMICILIO
              Field-Label: "Domicilio (Calle, N°, Villa, Población)"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S1-COMUNA
              Field-Label: "Comuna"
              Field-Type: Select
              Field-Constraint: "Req: mandatory."
              Field-Options:
                - "Bulnes"
                - "Chillán"
                - "Chillán Viejo"
                - "Cobquecura"
                - "Coelemu"
                - "Coihueco"
                - "El Carmen"
                - "Ninhue"
                - "Ñiquén"
                - "Pemuco"
                - "Pinto"
                - "Portezuelo"
                - "Quillón"
                - "Quirihue"
                - "Ránquil"
                - "San Carlos"
                - "San Fabián"
                - "San Ignacio"
                - "San Nicolás"
                - "Treguaco"
                - "Yungay"
            - ID: GN-CONC8-ANX1-S1-TEL-CONTACTO
              Field-Label: "Teléfono de Contacto"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S1-CORREO-ORG
              Field-Label: "Correo Electrónico"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: email."
            - ID: GN-CONC8-ANX1-S1-REP-LEGAL
              Field-Label: "Nombre del Representante Legal"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S1-RUT-REP-LEGAL
              Field-Label: "RUT del Representante Legal"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: XX.XXX.XXX-X."
            - ID: GN-CONC8-ANX1-S1-TEL-REP-LEGAL
              Field-Label: "Teléfono del Representante Legal"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S1-CORREO-REP-LEGAL
              Field-Label: "Correo Electrónico del Representante Legal"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: email."

        - ID: GN-CONC8-ANX1-SEC2-INICIATIVA
          Titulo: "Sección 2: Identificación de la Iniciativa"
          Campos:
            - ID: GN-CONC8-ANX1-S2-NOMBRE-INI
              Field-Label: "Nombre de la Iniciativa"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX1-S2-FONDO
              Field-Label: "Fondo al que Postula"
              Field-Type: Select
              Field-Constraint: "Req: mandatory."
              Field-Options:
                - "Cultura"
                - "Deporte"
                - "Social e Inclusión"
                - "Seguridad Ciudadana"
                - "Medio Ambiente"
                - "Adulto Mayor"
                - "Equidad de Género"
            - ID: GN-CONC8-ANX1-S2-AREA
              Field-Label: "Área de Postulación"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Debe corresponder a una de las áreas definidas para el fondo seleccionado en el instructivo."
            - ID: GN-CONC8-ANX1-S2-MONTO-SOL
              Field-Label: "Monto Solicitado al Gobierno Regional de Ñuble"
              Field-Type: Number
              Field-Constraint: "Req: mandatory. Min-Val: 0."
            - ID: GN-CONC8-ANX1-S2-APORTE-TERCEROS
              Field-Label: "Aporte de Terceros"
              Field-Type: Number
              Field-Constraint: "Req: optional. Min-Val: 0."
            - ID: GN-CONC8-ANX1-S2-APORTE-PROPIO
              Field-Label: "Aporte Propio"
              Field-Type: Number
              Field-Constraint: "Req: optional. Min-Val: 0."
            - ID: GN-CONC8-ANX1-S2-COSTO-TOTAL
              Field-Label: "Costo Total de la Iniciativa"
              Field-Type: Number
              Field-Constraint: "Req: mandatory. Min-Val: 0."
              Field-Logic: "Debe ser igual a Monto Solicitado + Aporte de Terceros + Aporte Propio."

        - ID: GN-CONC8-ANX1-SEC3-DESCRIPCION
          Titulo: "Sección 3: Descripción de la Iniciativa"
          Campos:
            - ID: GN-CONC8-ANX1-S3-FUNDAMENTACION
              Field-Label: "Fundamentación de la Iniciativa"
              Field-Type: TextArea
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Diagnóstico de la situación o problema que se quiere solucionar. Indicar cómo la iniciativa se vincula con los objetivos del fondo."
            - ID: GN-CONC8-ANX1-S3-DESCRIPCION
              Field-Label: "Descripción de la Iniciativa"
              Field-Type: TextArea
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Detalle de las principales acciones, si es un evento, taller, etc. Explicar en qué consiste."
            - ID: GN-CONC8-ANX1-S3-OBJ-GENERAL
              Field-Label: "Objetivo General"
              Field-Type: TextArea
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Propósito central del proyecto. Debe ser coherente con la fundamentación."
            - ID: GN-CONC8-ANX1-S3-OBJ-ESPECIFICOS
              Field-Label: "Objetivos Específicos"
              Field-Type: TextArea
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Resultados medibles y cuantificables que permitirán alcanzar el objetivo general."
            - ID: GN-CONC8-ANX1-S3-N-BENEF-DIR
              Field-Label: "N° de Beneficiarios Directos"
              Field-Type: Number
              Field-Constraint: "Req: mandatory. Min-Val: 1."
            - ID: GN-CONC8-ANX1-S3-N-BENEF-IND
              Field-Label: "N° de Beneficiarios Indirectos"
              Field-Type: Number
              Field-Constraint: "Req: optional. Min-Val: 0."
            - ID: GN-CONC8-ANX1-S3-DESC-BENEF
              Field-Label: "Descripción de la Población Beneficiaria"
              Field-Type: TextArea
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Detallar el perfil de los beneficiarios (grupo etario, género, territorio, etc.)."

        - ID: GN-CONC8-ANX1-SEC4-PLAN-TRABAJO
          Titulo: "Sección 4: Plan de Trabajo"
          Campos:
            - ID: GN-CONC8-ANX1-S4-PLAN
              Field-Label: "Plan de Trabajo"
              Field-Type: Repeater
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Detallar las actividades a realizar y el cronograma de ejecución en meses (máx. 8 meses)."
              Field-Group:
                Group-Label: "Fila de Actividad"
                Fields:
                  - Field-Label: "Actividad"
                    Field-Type: Text
                  - Field-Label: "Mes 1"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 2"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 3"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 4"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 5"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 6"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 7"
                    Field-Type: Checkbox
                  - Field-Label: "Mes 8"
                    Field-Type: Checkbox

        - ID: GN-CONC8-ANX1-SEC5-PRESUPUESTO
          Titulo: "Sección 5: Presupuesto Detallado"
          Campos:
            - ID: GN-CONC8-ANX1-S5-INSTR
              Field-Label: "Instrucciones de Presupuesto"
              Field-Type: Static-Text
              Field-Instr: "Detallar todos los gastos en los ítems correspondientes. Los montos deben coincidir con lo solicitado."
            - ID: GN-CONC8-ANX1-S5-ITEM-HONORARIOS
              Field-Label: "Ítem 1: Honorarios"
              Field-Type: Repeater
              Field-Group:
                Group-Label: "Fila de Gasto Honorario"
                Fields:
                  - Field-Label: "Detalle del Gasto"
                    Field-Type: Text
                    Field-Instr: "Ej: Monitor de taller, Profesional de apoyo."
                  - Field-Label: "Monto Solicitado"
                    Field-Type: Number
            - ID: GN-CONC8-ANX1-S5-ITEM-EQUIPAMIENTO
              Field-Label: "Ítem 2: Equipamiento"
              Field-Type: Repeater
              Field-Group:
                Group-Label: "Fila de Gasto Equipamiento"
                Fields:
                  - Field-Label: "Detalle del Gasto"
                    Field-Type: Text
                    Field-Instr: "Ej: Data show, notebook, indumentaria."
                  - Field-Label: "Monto Solicitado"
                    Field-Type: Number
            - ID: GN-CONC8-ANX1-S5-ITEM-GESTION
              Field-Label: "Ítem 3: Gastos de Gestión y Producción"
              Field-Type: Repeater
              Field-Group:
                Group-Label: "Fila de Gasto Gestión"
                Fields:
                  - Field-Label: "Detalle del Gasto"
                    Field-Type: Text
                    Field-Instr: "Ej: Arriendo de local, alimentación, materiales."
                  - Field-Label: "Monto Solicitado"
                    Field-Type: Number
            - ID: GN-CONC8-ANX1-S5-ITEM-DIFUSION
              Field-Label: "Ítem 4: Gastos de Difusión"
              Field-Type: Repeater
              Field-Group:
                Group-Label: "Fila de Gasto Difusión"
                Fields:
                  - Field-Label: "Detalle del Gasto"
                    Field-Type: Text
                    Field-Instr: "Ej: Pendón, volantes, spot radial."
                  - Field-Label: "Monto Solicitado"
                    Field-Type: Number

    Anexo_2_Formulario_Postulacion_Municipalidades:
      ID: GN-CONC8-ANEXO-2-FORM-POST-MUNICIPIOS-01
      Version: "1.0.0"
      Status: "Published"
      Ref_Guide: "GUIDE-SFD-STS-MASTER-01"
      Purp: "Recopilar la información requerida de las municipalidades para postular a los fondos concursables de Cultura y Seguridad Ciudadana."
      Secciones:
        - ID: GN-CONC8-ANX2-SEC1-MUNI
          Titulo: "Sección 1: Identificación del Municipio"
          Campos:
            - ID: GN-CONC8-ANX2-S1-NOMBRE-MUNI
              Field-Label: "Nombre del Municipio"
              Field-Type: Select
              Field-Constraint: "Req: mandatory."
              Field-Options:
                - "Bulnes"
                - "Chillán"
                - "Chillán Viejo"
                - "Cobquecura"
                - "Coelemu"
                - "Coihueco"
                - "El Carmen"
                - "Ninhue"
                - "Ñiquén"
                - "Pemuco"
                - "Pinto"
                - "Portezuelo"
                - "Quillón"
                - "Quirihue"
                - "Ránquil"
                - "San Carlos"
                - "San Fabián"
                - "San Ignacio"
                - "San Nicolás"
                - "Treguaco"
                - "Yungay"
            - ID: GN-CONC8-ANX2-S1-RUT-MUNI
              Field-Label: "RUT del Municipio"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: XX.XXX.XXX-X."
            - ID: GN-CONC8-ANX2-S1-DOMICILIO
              Field-Label: "Domicilio"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX2-S1-NOMBRE-ALCALDE
              Field-Label: "Nombre del Alcalde/sa"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX2-S1-RUT-ALCALDE
              Field-Label: "RUT del Alcalde/sa"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: XX.XXX.XXX-X."
            - ID: GN-CONC8-ANX2-S1-PROF-RESP
              Field-Label: "Nombre del Profesional Responsable"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX2-S1-CORREO-PROF
              Field-Label: "Correo Electrónico del Profesional Responsable"
              Field-Type: Text
              Field-Constraint: "Req: mandatory. Format: email."
            - ID: GN-CONC8-ANX2-S1-TELEFONO-PROF
              Field-Label: "Teléfono del Profesional Responsable"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."

        - ID: GN-CONC8-ANX2-SEC2-INICIATIVA
          Titulo: "Sección 2: Identificación de la Iniciativa"
          Campos:
            - ID: GN-CONC8-ANX2-S2-NOMBRE-INI
              Field-Label: "Nombre de la Iniciativa"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - ID: GN-CONC8-ANX2-S2-FONDO
              Field-Label: "Fondo al que Postula"
              Field-Type: Select
              Field-Constraint: "Req: mandatory."
              Field-Options:
                - "Fomento a la Cultura"
                - "Seguridad Ciudadana"
            - ID: GN-CONC8-ANX2-S2-AREA
              Field-Label: "Área de Postulación"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
              Field-Instr: "Debe corresponder a una de las áreas y tipologías definidas para el fondo seleccionado en el instructivo."
            - ID: GN-CONC8-ANX2-S2-MONTO-SOL
              Field-Label: "Monto Solicitado al Gobierno Regional"
              Field-Type: Number
              Field-Constraint: "Req: mandatory. Min-Val: 0."
            - ID: GN-CONC8-ANX2-S2-COSTO-TOTAL
              Field-Label: "Costo Total de la Iniciativa"
              Field-Type: Number
              Field-Constraint: "Req: mandatory. Min-Val: 0."

        - ID: GN-CONC8-ANX2-SEC3-DESC-PRESUP
          Titulo: "Sección 3: Descripción y Presupuesto"
          Ctx:
            - "Esta sección es idéntica en estructura a las secciones 3, 4 y 5 del formulario para instituciones privadas."
            - "Se utiliza el mismo conjunto de campos de descripción, plan de trabajo y presupuesto detallado, con la diferencia de que el plazo máximo de ejecución es de 9 meses."

    Anexo_3_Carta_Solicitud_Recursos:
      ID: GN-CONC8-ANEXO-3-CARTA-SOLICITUD-01
      Version: "1.0.0"
      Status: "Published"
      Ref_Guide: "GUIDE-SFD-STS-MASTER-01"
      Purp: "Formalizar la solicitud de financiamiento al Gobernador Regional."
      Secciones:
        - ID: GN-CONC8-ANX3-SEC1-ENCABEZADO
          Titulo: "Sección 1: Encabezado"
          Campos:
            - Field-Label: "Comuna"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Fecha"
              Field-Type: Date
              Field-Constraint: "Req: mandatory. Format: DD/MM/YYYY."
        - ID: GN-CONC8-ANX3-SEC2-CUERPO
          Titulo: "Sección 2: Cuerpo de la Solicitud"
          Campos:
            - Field-Label: "Yo,"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
              Field-Placeholder: "Nombre completo del presidente(a)"
            - Field-Label: "presidente(a) de Organización o Institución"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Domiciliado en"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "comuna de"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Texto fijo de solicitud"
              Field-Type: Static-Text
              Field-Value: "Solicito al Sr. Óscar Crisóstomo Llanos, Gobernador de la Región de Ñuble, financiamiento para el proyecto denominado"
            - Field-Label: "Nombre del Proyecto"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Monto Solicitado"
              Field-Type: Number
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Fondo Postulado"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Lineamiento"
              Field-Type: Text
              Field-Constraint: "Req: optional."
            - Field-Label: "Texto fijo Concurso"
              Field-Type: Static-Text
              Field-Value: "del \"CONCURSO DE VINCULACIÓN CON LA COMUNIDAD 8% 2025\"."
        - ID: GN-CONC8-ANX3-SEC3-CIERRE
          Titulo: "Sección 3: Cierre y Firma"
          Campos:
            - Field-Label: "FIRMA Y TIMBRE DEL REPRESENTANTE LEGAL"
              Field-Type: Static-Text
              Field-Instr: "Se debe firmar y timbrar por el representante legal."

    Anexo_4_Carta_Aceptacion_Terminos:
      ID: GN-CONC8-ANEXO-4-CARTA-ACEPTACION-01
      Version: "1.0.0"
      Status: "Published"
      Ref_Guide: "GUIDE-SFD-STS-MASTER-01"
      Purp: "Declarar conocimiento y aceptación del instructivo y normativa del concurso."
      Secciones:
        - ID: GN-CONC8-ANX4-SEC1-IDENTIFICACION
          Titulo: "Sección 1: Identificación"
          Campos:
            - Field-Label: "Yo,"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Rut.:"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
            - Field-Label: "Representante legal de la organización o institución"
              Field-Type: Text
              Field-Constraint: "Req: mandatory."
        - ID: GN-CONC8-ANX4-SEC2-DECLARACION
          Titulo: "Sección 2: Declaración"
          Campos:
            - Field-Label: "Texto Declaración"
              Field-Type: Static-Text
              Field-Value: "Declaro, conocer y aceptar el contenido íntegro del presente instructivo general y sus anexos, además de aceptar la normativa legal y reglamentaria vigente."

    Anexo_5_Carta_Presentacion_Experiencia:
      ID: GN-CONC8-ANEXO-5-CARTA-PRESENTACION-01
      Version: "1.0.0"
      Status: "Published"
      Ref_Guide: "GUIDE-SFD-STS-MASTER-01"
      Purp: "Acreditar la identidad, objetivos y experiencia de la organización postulante."
      Campos:
        - Field-Label: "Nombre de la organización"
          Field-Type: Text
          Field-Constraint: "Req: mandatory."
        - Field-Label: "Rut de la Organización"
          Field-Type: Text
          Field-Constraint: "Req: mandatory."
        - Field-Label: "Dirección de la organización"
          Field-Type: Text
          Field-Constraint: "Req: mandatory."
        - Field-Label: "Objetivos de la organización (Según lo que indican sus respectivos estatutos)"
          Field-Type: TextArea
          Field-Constraint: "Req: mandatory."
        - Field-Label: "Experiencia de la organización en el área que postula (indicar ejecución de otras iniciativas ejecutadas, actividades, talleres, etc.)"
          Field-Type: TextArea
          Field-Constraint: "Req: mandatory."
        - Field-Label: "Declaración de Experiencia"
          Field-Type: Static-Text
          Field-Value: "El o la representante legal declara tener experiencia en el ámbito de postulación y ejecución del proyecto a presentar al Concurso de Vinculación con la Comunidad 8%."
        - Field-Label: "NOMBRE: (Representante Legal Organización o Institución)"
          Field-Type: Text
          Field-Constraint: "Req: mandatory."
        - Field-Label: "RUT"
          Field-Type: Text
          Field-Constraint: "Req: mandatory."

    Anexo_6_Declaracion_Jurada_A:
      ID: GN-CONC8-ANEXO-6-DJ-A-RESTRICCIONES-01
      Purp: "Declarar el cumplimiento de las restricciones de las letras B y C del instructivo (Restricciones del Fondo y Gastos No Financiables)."
      Contenido:
        Field-Label: "Texto Declaración"
        Field-Type: Static-Text
        Field-Value: "Declaro; Que la Institución cumple con lo establecido en las letras B y C \"DE LAS RESTRICCIONES DEL FONDO Y LOS GASTOS NO FINANCIABLES\". Acepto la anulación absoluta de mi postulación en el evento de comprobarse la falsedad de alguno de los antecedentes presentados."
        Field-Instr: "Requiere identificación de la comuna, fecha, nombre y RUT del representante legal, y firma/timbre."

    Anexo_7_Declaracion_Jurada_B:
      ID: GN-CONC8-ANEXO-7-DJ-B-RESTRICCION-M-01
      Purp: "Declarar el cumplimiento de la restricción de la letra m) del instructivo (Restricciones del Fondo y Gastos No Financiables)."
      Contenido:
        Field-Label: "Texto Declaración"
        Field-Type: Static-Text
        Field-Value: "Declaro; Que la Institución cumple con lo establecido en la letra m) \"DE LAS RESTRICCIONES DEL FONDO Y LOS GASTOS NO FINANCIABLES\". Acepto la anulación absoluta de mi postulación en el evento de comprobarse la falsedad de alguno de los antecedentes presentados."
        Field-Instr: "Requiere identificación de la comuna, fecha, nombre y RUT del representante legal, y firma/timbre."

    Anexo_8_Carta_Compromiso_Prevencion:
      ID: GN-CONC8-ANEXO-8-CARTA-COMPROMISO-PREVENCION-01
      Purp: "Comprometer a la organización a prevenir actos de violencia y consumo de alcohol/drogas en actividades financiadas por el concurso."
      Contenido:
        Field-Label: "Texto Declaración"
        Field-Type: Static-Text
        Field-Value: "Declaro que la organización que represento se compromete a generar todas las acciones que sean necesarias para prevenir actos de violencia, consumo de alcohol y drogas en recintos que se ejecuten actividades con recursos obtenidos por la subvención del \"CONCURSO DE VINCULACIÓN CON LA COMUNIDAD 8% 2025\"."
        Field-Instr: "Requiere identificación de la comuna, fecha, nombre y RUT del representante legal, y firma/timbre."
