---
urn: urn:gn:kb:gn-guia-frpd-nuble
nombre: gn-guia-frpd-nuble
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Guía Operativa FRPD Ñuble 2025; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_027_guia_frpd_koda.yml (sha256:955f7ff1a1e8be7249e6d7115280929e0bfd7df7d54318345ea5316dffa43c28); URN KODA legado urn:gorenuble:gn:guia-frpd-nuble:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "guia"]
familia: bok
---
# Artefacto KODA/Spec – Guía Operativa FRPD Ñuble 2025
# Fuente principal: kb_gn_027_guia_frpd_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:guia-frpd-nuble:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_027_guia_frpd_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:selector-ipr:1.0.0"
        reason: "Marco legal detallado y selector de vías de financiamiento (incluye FRPD)."
      - urn: "urn:gorenuble:gn:guia-programas-directos-gore:1.0.0"
        reason: "Guía complementaria para formulación de programas (caso 2)."
  provenance:
    created_by: "FS"
    created_at: "2025-11-28"
    last_modified_at: "2025-11-28"
    signature: null

ID: GN-FRPD-GUIA-OPERATIVA-2025-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Guía operativa para el concurso FRPD 2025 del Gobierno Regional de Ñuble.
  Regula requisitos, procesos, actores y restricciones para la asignación del
  Fondo Regional para la Productividad y el Desarrollo (FRPD) en la región.

Source:
  Primary-Source: "kb_gn_027_guia_frpd_sts.md"
  Ctx_Required:
    - "Marco legal de Royalty Minero y FRPD (FIN-GORE-NORMATIVA-LEY-ROYALTY-01, FIN-GORE-NORMATIVA-GLOSA-13-01, FIN-GORE-NORMATIVA-FRPD-REGULACION-OPERATIVA-01)."
    - "Glosa 06 de la Ley de Presupuestos y Circular N°22 de DIPRES."
    - "Resolución Exenta N°33 de la SUBCTCI (31-Ene-2024) sobre instituciones habilitadas."
    - "Guía de Proyectos SNI (kb_gn_024_guia_idi_sni_sts.md)."
    - "Guía de Programas Públicos Regionales (kb_gn_025_guia_programas_sts.md)."
    - "Guía Operativa del Departamento de Análisis y Evaluación del GORE Ñuble para obtención de RS."
  Ctx_Optional:
    - "Estrategia Regional de Desarrollo (ERD) Ñuble 2023-2030."
    - "Estrategia Regional de Ciencia, Tecnología, Conocimiento e Innovación (ER-CTCI) 2022-2030."
    - "Planes regionales y sectoriales de fomento productivo pertinentes."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-FRPD-ÑUBLE-2025-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY:
      - Preserve all meat (essential information) and skeleton (estructura:
        secciones, listas, tablas, jerarquías, relaciones) con cero pérdida.
      - Ignora fat (retórica, redundancias, frases de estilo).

    LEXICON (expand before processing):
      Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dest->Destination, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
      Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
      Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
      Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
      Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY:
      - Ref: es interno al documento; sólo puede apuntar a IDs definidos
        dentro de este mismo artefacto.
      - Documentos externos (leyes, resoluciones, oficios, formularios,
        guías complementarias, sitios web) se mencionan bajo Ctx:,
        Src:, Ctx_Required: o Ctx_Optional:, nunca bajo Ref:.

    LANGUAGE POLICY:
      - Keywords en inglés (y abreviaturas como en este bloque).
      - Contenido descriptivo en español (es-CL). Nunca traduzcas el contenido.
    END_LLM_INSTRUCTIONS

Glosario_FRPD:
  ID: GN-FRPD-GLOSARIO-01
  Purp: "Definir conceptos, siglas y normas clave recurrentes en la Guía Operativa FRPD Ñuble 2025."
  Terminos:
    - ID: GN-FRPD-GLOS-FRPD
      Sigla: "FRPD"
      Cpt: "Fondo Regional para la Productividad y el Desarrollo"
      Def: "Fondo regional asociado al Royalty Minero para financiar iniciativas de fomento productivo, innovación, ciencia, tecnología y desarrollo regional."
    - ID: GN-FRPD-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento de proyectos y programas regionales, incluyendo recursos complementarios al FRPD."
    - ID: GN-FRPD-GLOS-GORE
      Sigla: "GORE"
      Cpt: "Gobierno Regional"
      Def: "Administración superior de la región, responsable del concurso FRPD y de la ejecución de iniciativas financiadas."
    - ID: GN-FRPD-GLOS-CTCI
      Sigla: "CTCI"
      Cpt: "Ciencia, Tecnología, Conocimiento e Innovación"
      Def: "Conjunto de actividades de generación y aplicación de conocimiento que el FRPD prioriza como motor de transformación y desarrollo regional."
    - ID: GN-FRPD-GLOS-SISREC
      Sigla: "SISREC"
      Cpt: "Sistema de Rendición de Cuentas"
      Def: "Plataforma electrónica obligatoria para la rendición de recursos FNDR/FRPD (Art. 24 Ley N° 21.796)."
    - ID: GN-FRPD-GLOS-RATE
      Sigla: "RATE"
      Cpt: "Resultado de la Evaluación Técnica"
      Def: "Clasificaciones RS, FI, OT y NV que resumen el resultado de la evaluación técnica de una iniciativa."
    - ID: GN-FRPD-GLOS-RS
      Sigla: "RS"
      Cpt: "Recomendado Favorablemente"
      Def: "Calificación que indica aprobación técnica y habilita la obtención de RS para financiamiento."

Guia_Operativa_FRPD_Ñuble_2025:
  ID: GN-FRPD-GUIA-OPERATIVA-2025-01
  Titulo: "Guía Operativa FRPD Ñuble 2025"
  Purp: |
    Regular el concurso FRPD 2025 para la asignación de recursos del Fondo
    Regional para la Productividad y el Desarrollo en la Región de Ñuble,
    definiendo reglas, criterios, plazos y responsabilidades para las
    instituciones habilitadas.
  Destinatarios:
    - "Instituciones públicas y entidades habilitadas por SUBCTCI para ejecutar programas y proyectos FRPD."
    - "Equipos técnicos del GORE Ñuble (DIPIR, Departamentos de Análisis y Evaluación, Presupuesto, etc.)."
    - "Autoridades regionales y actores que participan en evaluación, seguimiento y supervisión de iniciativas FRPD."
  Alcance:
    - "Aplica al concurso FRPD 2025 del GORE Ñuble."
    - "Cubre desde antecedentes generales, admisibilidad, evaluación técnica, ejecución, garantías y obligaciones de rendición."
  Estructura_Secciones:
    - ID: GN-FRPD-SEC-1-ANTECEDENTES
      Cpt: "Antecedentes Generales del FRPD y propósito de la guía."
    - ID: GN-FRPD-SEC-2-INTRO
      Cpt: "Introducción, contexto regional y bifurcación del proceso de evaluación."
    - ID: GN-FRPD-SEC-3-PILARES
      Cpt: "Pilares estratégicos, sectores y focos prioritarios del concurso."
    - ID: GN-FRPD-SEC-4-POSTULANTES
      Cpt: "Instituciones habilitadas y prohibiciones para postular."
    - ID: GN-FRPD-SEC-5-PRESENTACION
      Cpt: "Presentación de postulaciones, plazos y mecanismos de consultas."
    - ID: GN-FRPD-SEC-6-ADM-ADMIN
      Cpt: "Admisibilidad administrativa y criterios obligatorios."
    - ID: GN-FRPD-SEC-7-ADM-TEC
      Cpt: "Admisibilidad técnica, variables de evaluación y ponderaciones."
    - ID: GN-FRPD-SEC-8-EVAL-TEC
      Cpt: "Evaluación técnica detallada, prioridades 2025, restricciones y antecedentes requeridos."
    - ID: GN-FRPD-SEC-9-COMUNICACION
      Cpt: "Comunicación oficial de resultados."
    - ID: GN-FRPD-SEC-10-EJECUCION
      Cpt: "Ejecución de iniciativas aprobadas, convenios, transferencias, seguimiento y reevaluaciones."
    - ID: GN-FRPD-SEC-11-PROPIEDAD
      Cpt: "Propiedad intelectual e industrial de los resultados."
    - ID: GN-FRPD-SEC-12-COMPROMISO-GORE
      Cpt: "Compromisos y condiciones suspensivas del GORE."
    - ID: GN-FRPD-SEC-13-GARANTIAS
      Cpt: "Garantías exigidas a instituciones privadas."
    - ID: GN-FRPD-SEC-14-OTROS
      Cpt: "Transparencia, rendiciones, SISREC, contrapartes, objeto social, supervisión y protección de datos."
    - ID: GN-FRPD-FORM-APPLICATION-2025-01
      Cpt: "Formulario de postulación FRPD 2025 (campos obligatorios y especificaciones)."

  Sec_1_Antecedentes_Generales:
    ID: GN-FRPD-SEC-1-ANTECEDENTES
    Instrumento_FRPD:
      ID: GN-FRPD-ANT-INSTRUMENTO-01
      Cpt: "Fondo Regional para la Productividad y el Desarrollo (FRPD)."
      Def: "Fondo regional de inversión productiva asociado al Royalty Minero."
      Purp:
        - "Financiar inversión productiva a través de proyectos, planes o programas."
      Req:
        - "Considerar regulación operativa anual del FRPD en la Ley de Presupuestos (p.ej. provisión sin distribuir en Ítem 33.03 y transferencias directas cuando aplique)."
      Ctx:
        - "Marco legal detallado en el Selector IPR (FIN-GORE-NORMATIVA-LEY-ROYALTY-01, FIN-GORE-NORMATIVA-GLOSA-13-01)."
        - "kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13"
    Tipos_Iniciativa:
      ID: GN-FRPD-ANT-TIPOS-01
      Tipos:
        - ID: GN-FRPD-TIPO-PROYECTO
          Cpt: "Proyectos de inversión."
          Def: "Iniciativas de inversión de capital."
          Req:
            - "Formulación según la guía del Sistema Nacional de Inversiones (SNI)."
          Ctx_Required:
            - "kb_gn_024_guia_idi_sni_sts.md."
        - ID: GN-FRPD-TIPO-PROGRAMA
          Cpt: "Programas."
          Def: "Iniciativas de gasto corriente para entrega de servicios."
          Req:
            - "Formulación según la Guía de Programas Públicos Regionales."
          Ctx_Required:
            - "kb_gn_025_guia_programas_sts.md."
    Ambitos_Principales:
      ID: GN-FRPD-ANT-AMBITOS-01
      Ambitos:
        - "Fomento de actividades productivas."
        - "Desarrollo regional."
        - "Promoción de investigación científica, tecnológica, conocimiento e innovación (CTCI)."
    Alineacion_Estrategica_Obligatoria:
      ID: GN-FRPD-ANT-ALINEACION-01
      Req:
        - "Estrategia Regional de Desarrollo (ERD)."
        - "Estrategia Regional de CTCI."
        - "Otras prioridades estratégicas regionales de fomento productivo."
    Rol_CTCI:
      ID: GN-FRPD-ANT-ROL-CTCI-01
      Def: "Los actores de CTCI son garantes de la transformación y el desarrollo regional."
    Resultado_Esperado:
      ID: GN-FRPD-ANT-RES-ESPERADO-01
      Res:
        - "Generar condiciones para apertura de empresas de base tecnológica con mayores y mejores empleos."
    Proposito_Guia_Operativa:
      ID: GN-FRPD-ANT-PROP-GUIA-01
      Purp:
        - "Regular el concurso FRPD 2025 en Ñuble, dirigido a instituciones habilitadas."
      Src:
        - "Resolución Exenta N°33 de SUBCTCI (31-Ene-2024) con base de instituciones habilitadas."

  Sec_2_Introduccion:
    ID: GN-FRPD-SEC-2-INTRO
    FRPD_Como_Herramienta:
      ID: GN-FRPD-INTRO-FRPD-01
      Cpt:
        - "FRPD como desafío y aporte al desarrollo económico, productivo y social regional."
        - "Ciencia y tecnología como herramienta clave para transformar y fortalecer la región."
      Purp:
        - "Promover e incentivar la asociatividad interinstitucional para la cooperación."
      Res:
        - "Contribuir a diversificar la matriz productiva y aumentar la competitividad regional."
    Alineacion_Estrategica:
      ID: GN-FRPD-INTRO-ALINEACION-01
      Req:
        - "Alinearse con pilares y prioridades de la ERD."
        - "Alinearse con la Estrategia Regional de CTCI 2022-2030."
      Consideraciones_Adicionales:
        - "Responder a demandas sociales."
        - "Abordar necesidades territoriales de productividad y desarrollo."
    Concurso_2025:
      ID: GN-FRPD-INTRO-CONCURSO-01
      Proc:
        - "Concurso FRPD año 2025 organizado por el GORE Ñuble."
      Obj:
        - "Resolver brechas en fomento y productividad regional."
      Req_Iniciativas:
        - "Las iniciativas deben resolver problemáticas en sectores y focos prioritarios definidos en la guía."
      Mecanismo_Postulacion:
        Mech: "Postulación mediante formulario online."
        Act_Postulante:
          - "Completar todos los campos del formulario."
          - "Subir todos los anexos solicitados."
      Alcance_Bases:
        Cpt: "Las bases determinan las iniciativas preseleccionadas para financiamiento."
    Bifurcacion_Post_Seleccion:
      ID: GN-FRPD-INTRO-BIFURCACION-01
      Warn:
        - "Según Glosa 06 y Circular N°22 DIPRES, el camino posterior a la selección depende de la naturaleza de la iniciativa."
      Casos:
        - ID: GN-FRPD-CASO-1-CTCI
          Cpt: "Caso 1 – Innovación, CTCI."
          Def: "Iniciativas estrictamente enmarcadas en CTCI."
          Ctx:
            - "Exentas del proceso de evaluación ex ante DIPRES/SES."
            - "La evaluación del concurso se considera final."
        - ID: GN-FRPD-CASO-2-FOMENTO
          Cpt: "Caso 2 – Fomento Productivo General."
          Def: "Iniciativas de fomento productivo que no califican como CTCI."
          Req:
            - "DEBEN ingresar al proceso de evaluación ex ante correspondiente."
            - "Si son proyectos de inversión, seguir Guía SNI (kb_gn_024_guia_idi_sni_sts.md)."
            - "Si son programas de servicios, seguir Guía de Programas Públicos (kb_gn_025_guia_programas_sts.md)."

  Sec_3_Pilares_Estrategicos_Concurso_2025:
    ID: GN-FRPD-SEC-3-PILARES
    Referencias_Legales_Clave:
      ID: GN-FRPD-PILARES-REF-01
      Ctx:
        - "Ley de Royalty Minero (FIN-GORE-NORMATIVA-LEY-ROYALTY-01)."
        - "Regulación operativa FRPD (FIN-GORE-NORMATIVA-FRPD-REGULACION-OPERATIVA-01)."
    Ambitos_Accion:
      ID: GN-FRPD-PILARES-AMBITOS-01
      Ambitos:
        Investigacion:
          Cpt: "Investigación."
          Subtipos:
            - "Básica: esencial para formación de talento, innovación y solución de problemas."
            - "Aplicada: resuelve problemas relevantes específicos."
            - "Desarrollo experimental: crea o ensaya nuevas metodologías o tecnologías."
        Innovacion:
          Cpt: "Innovación."
          Subtipos:
            - "Base científico-tecnológica: clave para diversificación productiva."
            - "Productiva: introduce nuevos productos/servicios al mercado."
            - "Social: nuevos productos/servicios que satisfacen necesidades sociales."
            - "Pública: nuevas soluciones con valor público implementadas en el sector público."
        Emprendimiento:
          Cpt: "Emprendimiento (empresa)."
          Def: "Actividades para solucionar problemas complejos y globales con potencial de crecimiento regional."
        Difusion_y_Transferencia:
          Cpt: "Divulgación, difusión y transferencia tecnológica."
          Def: "Programas que diseminan conocimiento, ciencia y tecnología hacia sociedad, industria y sector público."
    Sectores_Prioritarios:
      ID: GN-FRPD-PILARES-SECTORES-01
      Lista_Sectores:
        - "Atracción de Inversiones para el Desarrollo Regional."
        - "Desarrollo Empresarial, Fomento Productivo e Inversión Productiva."
        - "Turismo y/o Medioambiente."
        - "Energía y/o Conectividad Digital."
    Focos_Prioritarios:
      ID: GN-FRPD-PILARES-FOCOS-01
      Req:
        - "Las iniciativas deben alinearse a los sectores prioritarios definidos para el concurso."
      Ctx:
        - "Marco estratégico validado por el Comité Regional de Ciencia."
      Instrumentos_Planificacion:
        - "Estrategia de Desarrollo Regional al 2030."
        - "Estrategia Regional de CTCI."
      Focos_Principales:
        - "Conocimiento, Ciencia, Tecnología e Innovación."
        - "Gestión, Competitividad, Capacitación Laboral e Innovación."
        - "Agroindustrial, Silvoagropecuario y/o Pesca."
        - "Emprendimiento, Turismo y Medioambiente."

  Sec_4_Postulantes_Habilitados:
    ID: GN-FRPD-SEC-4-POSTULANTES
    Criterio_General:
      ID: GN-FRPD-POST-CRITERIO-01
      Cpt: "Cumplir con Resolución Exenta N°33 de SUBCTCI (31-Ene-2024) sobre instituciones habilitadas."
    Lista_Instituciones_Habilitadas:
      ID: GN-FRPD-POST-LISTA-01
      Cpt: "Listado de instituciones habilitadas para postular al FRPD 2025."
      Instituciones:
        - "Agencia Nacional de Investigación y Desarrollo (ANID)."
        - "CORFO (incluyendo Comité Innova Chile)."
        - "Fundación para la Innovación Agraria (FIA)."
        - "Servicio de Cooperación Técnica (SERCOTEC)."
        - "Instituto de Desarrollo Agropecuario (INDAP)."
        - "Subsecretaría de Economía y Empresas de Menor Tamaño (programas Desarrollo Productivo Sostenible)."
        - "Subsecretaría de Ciencia, Tecnología, Conocimiento e Innovación."
        - "Servicio de Evaluación Ambiental."
        - "Servicio de Biodiversidad y Áreas Protegidas (SBAP)."
        - "Servicio Nacional de Pesca y Acuicultura."
        - "Servicio Nacional de Turismo."
        - "Agencia de Promoción de la Inversión Extranjera (InvestChile)."
        - "Instituto Nacional de Propiedad Industrial (INAPI)."
        - "Servicio Nacional de Aduanas."
        - "Dirección General de Aguas (DGA)."
        - "Comisión Nacional de Riego (CNR)."
        - "Corporación Nacional Forestal (CONAF)."
        - "Agencia de Sostenibilidad Energética (ASE)."
        - "Servicio Agrícola y Ganadero (SAG)."
        - "Instituto Nacional de Desarrollo Sustentable de la Pesca Artesanal y de la Acuicultura de Pequeña Escala (INDESPA)."
        - "Agencia de Sustentabilidad y Cambio Climático (ASCC)."
        - "Dirección General de Promoción de Exportaciones (PROCHILE)."
        - "Centro de Información de Recursos Naturales (CIREN)."
        - "Instituto Forestal (INFOR)."
        - "Instituto de Fomento Pesquero (IFOP)."
        - "Fundación Chile."
        - "Instituto para la Resiliencia ante Desastres (ITREND)."
        - "Fundación Conecta Logística."
        - "Comités de Desarrollo Productivo Regional de CORFO."
        - "Centros Regionales de Desarrollo Científico y Tecnológico (Programa Regional ANID)."
        - "Centros de Investigación en Áreas Prioritarias (FONDAP)."
        - "Centros Tecnológicos de I+D de la ANID."
        - "Centros Científicos y Tecnológicos de Excelencia y Centros de Investigación Avanzada en Educación (PIA)."
        - "Centros del Programa Iniciativa Científica Milenio."
        - "Centros Tecnológicos (Programa Fortalecimiento y Creación de Capacidades Tecnológicas Habilitantes)."
        - "Centros e Institutos (Programa Fortalecimiento de Institutos Públicos)."
        - "Entidades de Programas Tecnológicos y Consorcios Tecnológicos para la Innovación; Programas Estratégicos (Transforma)."
        - "Centros de Excelencia Internacional."
        - "Centros de investigación y entidades I+D registradas en CORFO (Ley N° 20.241)."
        - "Instituciones de educación superior (literales a, b, c art. 52 DFL N°2/2010 Mineduc), con acreditación institucional vigente Ley N° 20.129."
        - "Corporaciones regionales con participación del GORE (glosa 04, Partida 31, Capítulo 01, Programa 02, Ley de Presupuestos 2025)."
    Prohibiciones_Postulacion:
      ID: GN-FRPD-POST-PROHIB-01
      Prohib:
        - "Instituciones cuyo objeto social no se relacione o sin experiencia comprobable en materias pertinentes."
        - "Instituciones con directivos o representantes con parentesco hasta 4° consanguinidad o 3° afinidad, o vínculo de cónyuge/conviviente civil/hijo en común, con Gobernador Regional, Consejeros Regionales, Jefes de División o funcionarios del GORE (incluyendo honorarios)."
        - "Instituciones con directivos/representantes que hayan trabajado o prestado servicios (remunerados o no) en el GORE."
        - "Instituciones privadas con directivos/representantes que hayan sido autoridades o funcionarios del GORE en los 2 años previos al ejercicio de su cargo público actual."

  Sec_5_Presentacion_Postulaciones:
    ID: GN-FRPD-SEC-5-PRESENTACION
    Mecanismo:
      ID: GN-FRPD-PRES-MECANISMO-01
      Mech: "Postulación en línea mediante página web del GORE Ñuble."
      Act:
        - "Completar formulario de postulación."
    Plazos_Claves_2025:
      ID: GN-FRPD-PRES-PLAZOS-01
      Cpt: "Plazos clave del concurso 2025 (valores específicos se completan en cada convocatoria)."
      Fechas_Placeholders:
        - "Fecha-Publicacion"
        - "Fecha-Inicio-Preguntas"
        - "Fecha-Final-Preguntas"
        - "Fecha-Publicacion-Respuestas"
        - "Fecha-Cierre-Formulario"
        - "Fecha-Revision-Adm"
        - "Fecha-Resultados-Adm-Adm"
        - "Fecha-Resultados-Adm-Tec"
        - "Plazo-Max-Ingreso-Eval-Tec"
        - "Plazo-Max-Obtener-RS"
    Consultas_y_Respuestas:
      ID: GN-FRPD-PRES-CONSULTAS-01
      Proc_Consultas:
        Mech: "Correo electrónico."
        Req:
          - "Plazo de formulación: primeros 7 días corridos desde el día hábil siguiente a la publicación."
        Dest: "Página web del GORE Ñuble (publicación de preguntas)."
      Proc_Respuestas:
        Mech: "Mismo correo electrónico utilizado para consultas."
        Req:
          - "Plazo de respuesta máximo: 5 días hábiles, salvo complejidad."
        Res:
          - "Respuestas compiladas y publicadas en la web del GORE en los plazos establecidos."

  Sec_6_Admisibilidad_Administrativa:
    ID: GN-FRPD-SEC-6-ADM-ADMIN
    Evaluacion:
      ID: GN-FRPD-ADM-ADMIN-EVAL-01
      Resp:
        - "Comisión de profesionales del GORE Ñuble."
      Res:
        - "Clasificación de iniciativas como 'admisibles' o 'inadmisibles'."
      Proximo_Paso:
        - "Iniciativas admisibles pasan a admisibilidad técnica."
    Criterios_Obligatorios:
      ID: GN-FRPD-ADM-ADMIN-CRITERIOS-01
      Cpt: "Criterios A–L de admisibilidad administrativa."
      Req:
        - "A. Registro en línea completo."
        - "B. Vinculación en el registro con pilar estratégico, sector y focos prioritarios (GUIDE-GN-FRPD-STRATEGIC-PILLARS-01, GUIDE-GN-FRPD-PRIORITY-SECTORS-01, GUIDE-GN-FRPD-PRIORITY-FOCUSES-01)."
        - "C. Formulario de admisibilidad completo."
        - "D. Postulante perteneciente a categorías habilitadas (GUIDE-GN-FRPD-ELIGIBLE-APPLICANTS-01)."
        - "E. Personalidad jurídica acreditada."
        - "F. Máximo 2 iniciativas por postulante (se consideran las 2 primeras ingresadas cronológicamente)."
        - "G. Carta de patrocinio firmada por Rector, Director o Jefe de Servicio."
        - "H. Máximo 30% del monto total a remuneraciones con cargo al fondo regional."
        - "I. Plazo máximo de ejecución de 30 meses."
        - "J. Alcance regional (21 comunas) o justificación suficiente para un territorio particular (p.ej. Valle del Itata)."
        - "K. Mínimo 1 profesional residente en Ñuble contratado (adjuntar certificado)."
        - "L. Certificado que acredite que viáticos, alimentación, pasajes, peajes y estacionamiento son asumidos por la institución ejecutora."
      Consecuencia_Incumplimiento:
        Res:
          - "La iniciativa se declara inadmisible."

  Sec_7_Admisibilidad_Tecnica:
    ID: GN-FRPD-SEC-7-ADM-TEC
    Proposito:
      ID: GN-FRPD-ADM-TEC-PROP-01
      Purp:
        - "Tomar la mejor decisión de inversión basada en la información presentada."
      Obj:
        - "Evaluar aplicación de las bases, pertinencia local y factibilidad técnica."
    Comision_Evaluadora:
      ID: GN-FRPD-ADM-TEC-COMISION-01
      Composicion:
        - "Máximo 11 representantes del territorio vinculados a fomento e innovación."
      Quorum_Minimo: 6
      Facultades:
        - "Realizar observaciones a las iniciativas."
    Variables_Evaluacion:
      ID: GN-FRPD-ADM-TEC-VARIABLES-01
      Variables:
        - "A. Coherencia global de la iniciativa."
        - "B. Coherencia con objetivos de desarrollo regional."
        - "C. Coherencia entre componentes, propósito y actividades."
        - "D. Mérito innovador."
    Criterios_Puntuacion:
      ID: GN-FRPD-ADM-TEC-PUNTAJE-01
      Escala:
        - "1 – Interés: Nulo."
        - "3 – Interés: Bajo."
        - "5 – Interés: Medio."
        - "7 – Interés: Alto."
      Ponderacion_Variables:
        Tabla:
          - "Coherencia global – 10%."
          - "Coherencia con objetivos de desarrollo regional – 30%."
          - "Coherencia componentes/propósito/actividades – 20%."
          - "Mérito innovador – 40%."
      Calculo_Puntaje_Final:
        Cpt: "Promedio ponderado de todos los evaluadores."
        Puntaje_Minimo_Elegibilidad: 5
        Res:
          - "Se construye un ranking de iniciativas 'Elegibles' de mayor a menor puntuación."
          - "Iniciativas 'Elegibles' pasan a Evaluación Técnica."

  Sec_8_Evaluacion_Tecnica_y_Antecedentes:
    ID: GN-FRPD-SEC-8-EVAL-TEC
    Alcance:
      ID: GN-FRPD-EVAL-ALCANCE-01
      Obj:
        - "Aplicar evaluación técnica a iniciativas declaradas 'Elegibles' en etapas anteriores."
      Criterios:
        - "Antecedentes presentados."
        - "Pertinencia."
        - "Ejecutabilidad."
        - "Uso eficiente de recursos fiscales."
      Resp:
        - "Unidad de Proyectos y Programas del Departamento de Análisis y Evaluación del GORE Ñuble."
    Lineamientos_y_Prioridades_2025:
      ID: GN-FRPD-EVAL-LINEAMIENTOS-01
      Req:
        - "Considerar prioridades regionales año 2025 fijadas por Resolución Exenta."
      Lista_Prioridades_2025:
        - "SOCIAL."
        - "ASISTENCIA TÉCNICA A MUNICIPALIDADES."
        - "CULTURA."
        - "SALUD."
        - "INFANCIA."
        - "ENERGÍA, TRANSPORTES Y TELECOMUNICACIONES."
        - "MEDIOAMBIENTE Y GESTIÓN DE RESIDUOS."
        - "GESTIÓN DE RECURSOS HÍDRICOS."
        - "DEPORTES."
        - "MOVILIDAD URBANA."
        - "CUIDADOS DE ADULTO MAYOR."
        - "CONECTIVIDAD DIGITAL."
        - "EMERGENCIA."
        - "FOMENTO PRODUCTIVO, EMPRENDIMIENTO E INNOVACIÓN."
        - "SEGURIDAD PÚBLICA."
        - "ATRACCIÓN DE INVERSIONES."
      Focalizacion_Inversion:
        Cpt: "Reglas de foco y coherencia de la inversión."
        Req:
          - "Propósito: solucionar un problema regional definido, identificable, demostrable y con indicadores."
          - "Formulación: enfocada en disminuir brechas de un problema claramente definido."
          - "Cobertura: considerar dimensión regional del FNDR y magnitud del problema."
          - "Coherencia estratégica con ERD Ñuble 2023-2030, Plan de Gobierno Regional y/o Estrategia Regional de CTCI."
          - "Equidad: énfasis en equidad de acceso y pertinencia, con mecanismos de selección transparentes y probos."
          - "Gestión: capacidad óptima de gestión, maximizando eficiencia y eficacia."

    Restricciones_Postulacion:
      ID: GN-FRPD-EVAL-RESTRICCIONES-01
      Instituciones_Publicas:
        Cpt: "Restricciones para instituciones públicas."
        Req:
          - "No postular a programas con objetivos distintos a su ley o decreto de creación."
          - "Acreditar objeto social coherente."
      Convenios_Vigentes:
        Req:
          - "Si existen convenios vigentes con el GORE, adjuntar clarificación de saldos por rendir y cumplir con Res. N°30 de 2015 CGR."
      Uso_Prohibido_Recursos_FNDR:
        Prohib:
          - "Otorgar préstamos."
          - "Financiar gastos de personal de entidades receptoras (salvo glosas específicas)."
          - "Financiar gastos de bienes y servicios de consumo de entidades receptoras (salvo habilitación expresa)."
          - "Constituir, aportar o comprar sociedades o empresas."
        Limite_Gastos_Administrativos:
          Req:
            - "Máximo 5% del total postulado (Art. 25 Ley N° 21.796)."
      Rendicion_Cuentas:
        Req:
          - "Rendir cuentas obligatoriamente vía SISREC (Art. 24 Ley N° 21.796)."
      Subcontratacion:
        Cpt: "Reglas sobre subcontratación."
        Req:
          - "Permitida sólo para actividades que no son objeto principal del proyecto."
          - "Precisar en formulario, presupuesto y convenio."
        Prohib:
          - "No subcontratar con personas relacionadas (Art. 100 Ley N° 18.045), incluyendo matrices, coligantes, filiales, directores, gerentes y parientes hasta 2° consanguinidad vinculados al Gobernador, Consejeros o directivos del GORE."
      Contratacion_Personas:
        Prohib:
          - "Contratar cónyuges, parejas, hijos o parientes hasta 3° consanguinidad del Gobernador, Consejeros, personal directivo GORE o Jefe de Servicio/directivos de la institución postulante."

    Antecedentes_Requeridos_Postulacion:
      ID: GN-FRPD-EVAL-ANTECEDENTES-01
      Mech_Ingreso:
        Cpt: "Mecanismos de ingreso de antecedentes."
        Instituciones_Privadas:
          Mech: "Oficio al Gobernador Regional por Oficina de Partes."
        Instituciones_Publicas:
          Mech: "DOC Digital del Estado de Chile."
        Req:
          - "Todos los antecedentes descritos deben estar cargados en el Banco Integrado de Proyectos (BIP) al momento de la postulación."
      Lista_Antecedentes:
        - ID: GN-FRPD-ANT-OFICIO-CONDUCTOR
          Cpt: "Oficio Conductor."
          Req:
            - "Dirigido al Gobernador Regional, firmado y timbrado."
            - "Debe indicar nombre de la iniciativa, código BIP y Eje/Lineamiento/Objetivo ERD asociado."
          Cond:
            - "Si no se cumple, la iniciativa es INADMISIBLE."
        - ID: GN-FRPD-ANT-FICHA-IDI
          Cpt: "Ficha IDI (año presupuestario 2025)."
          Src:
            - "Se descarga desde BIP con código de proyecto."
          Ctx:
            - "Etapa de ejecución."
          Req:
            - "Cargar asignación presupuestaria completa."
            - "Registrar cofinanciamiento y fuentes."
            - "Monto total coherente con presupuesto y oficio."
            - "Es el único antecedente impreso, pero también debe estar cargado en BIP."
        - ID: GN-FRPD-ANT-ANEXO-1-FORM
          Cpt: "Anexo 1 – Formulario de Postulación FRPD."
          Purp:
            - "Documento metodológico que fundamenta la iniciativa."
          Src:
            - "Disponible en página web del GORE Ñuble."
          Rec:
            - "Se sugiere usar Metodología de Marco Lógico."
          Ctx:
            - "Debe ubicarse en carpeta 'Estudio Preinversional' en BIP."
        - ID: GN-FRPD-ANT-ANEXO-2-PRESUPUESTO
          Cpt: "Anexo 2 – Presupuesto."
          Req:
            - "Formato PDF y Excel en BIP."
            - "Desglose máximo coherente con MML, IVA incluido, sin gastos generales ni utilidades."
          Facultades_GORE:
            - "El GORE puede solicitar análisis de precios unitarios (APU)."
          Cond:
            - "Cofinanciamiento requiere V°B° de Unidad Financiera."
          Clasificador_Presupuestario:
            - "Contratación de programa: actividades principales (RRHH, materiales, etc.), sugerido entre 70–95% del total."
            - "Consultoras: externalización de servicios, no puede ser mayor a 'Contratación de Programas'."
            - "Gastos administrativos: hasta 5% del total; incluye combustible, materiales de oficina y garantías (privados)."
          Prohib:
            - "Cargar viáticos, alimentación, pasajes, peajes o estacionamiento al FRPD."
          Clasificacion_SISREC:
            - "Inversión: adquisición de activos y otros sin contraprestación directa (asociado a contratación de programa)."
            - "Operación: gastos de bienes de consumo y otros para funcionamiento (asociados a gastos administrativos)."
            - "Recursos Humanos: remuneraciones (asociadas a consultorías)."
          Imputacion_Transferencia:
            - "Corriente: si gasto asimilable a subtítulos 21, 22, 24 > 50% del total."
            - "De Capital: si gasto asimilable a subtítulos 29, 31, 33 > 50% del total."
        - ID: GN-FRPD-ANT-ANEXO-3-PERFILES
          Cpt: "Anexo 3 – Perfiles y descripción de cargo."
          Req:
            - "Describir perfiles, funciones, número de horas y formato de contratación."
            - "Universidades estatales deben adjuntar declaración jurada simple del Rector con horas disponibles de académicos."
            - "Adjuntar certificado de que personas a contratar no pertenecen a la institución (cuando corresponda)."
        - ID: GN-FRPD-ANT-ANEXO-4-COTIZ-TDR
          Cpt: "Anexo 4 – Cotizaciones y/o Términos de Referencia (TDR)."
          Req:
            - "Al menos 1 cotización por activo, con antigüedad ≤ 60 días, fecha, RUT del proveedor y precio."
            - "TDR detallados para licitaciones (fechas, dimensiones, especificaciones técnicas)."
          Ctx:
            - "Ubicación en BIP: carpeta 'Especificaciones Técnicas'."
        - ID: GN-FRPD-ANT-ANEXO-5-DECL-SIN-REND
          Cpt: "Anexo 5 – Declaración jurada simple (sin rendiciones pendientes)."
          Src:
            - "Disponible en página web del GORE Ñuble."
          Req:
            - "Firma del representante legal."
        - ID: GN-FRPD-ANT-ANEXO-6-ESTATUTOS
          Cpt: "Anexo 6 – Decreto o Estatutos de creación del servicio."
          Purp:
            - "Acreditar que el objeto social se relaciona con el programa."
          Rec:
            - "Adjuntar aprobación técnica de SES o DIPRES si existe."
        - ID: GN-FRPD-ANT-ANEXO-7-PERSONERIA
          Cpt: "Anexo 7 – Personería del representante legal."
          Purp:
            - "Acreditar quién firmará el convenio."
        - ID: GN-FRPD-ANT-ANEXO-8-RESUMEN-EJEC
          Cpt: "Anexo 8 – Resumen Ejecutivo."
          Src:
            - "Disponible en página web del GORE Ñuble."
          Req:
            - "Apéndice con objetivos, descripción y montos."
          Ctx:
            - "Ubicación en BIP: carpeta 'Anexos'."
        - ID: GN-FRPD-ANT-OTROS-ANEXOS
          Cpt: "Otros anexos."
          Cond:
            - "Compromiso de financiamiento compartido: certificado de Dirección de Finanzas."
            - "Postulación de Universidad Estatal: certificado de acreditación de la CNA."
            - "Derechos de Autor: declaración jurada sobre plagio, si aplica."

    Procedimiento_Evaluacion_Tecnica_y_RATE:
      ID: GN-FRPD-EVAL-PROCEDIMIENTO-01
      Resp:
        - "Unidad de Proyectos y Programas de la DIPIR-GORE Ñuble."
      Func:
        - "Revisión técnica y recomendación de iniciativas."
      Res:
        - "Acta de evaluación con asignación de RATE."
      Tipos_RATE:
        RS:
          ID: GN-FRPD-RATE-RS-01
          Cpt: "RS – Recomendado Favorablemente."
          Res:
            - "Otorga aprobación técnica."
          Req:
            - "Certificado RS, acta de evaluación, presupuesto final, ficha IDI y oficio conductor."
          Contenido_Certificado_RS:
            - "Listado de beneficiarios."
            - "Comuna o territorio."
            - "Monto FNDR y otros aportes."
            - "Antecedentes de la institución postulante."
            - "Producto esperado."
            - "Objetivo esperado."
            - "Coherencia con carácter regional del FNDR."
          Vigencia:
            - "Año de obtención + 2 años calendario siguientes, si no hay cambios sustantivos."
        FI:
          ID: GN-FRPD-RATE-FI-01
          Cpt: "FI – Falta de Información."
          Def:
            - "Antecedentes insuficientes, errores o necesidad de actualización."
        OT:
          ID: GN-FRPD-RATE-OT-01
          Cpt: "OT – Objetado técnicamente."
          Def:
            - "Iniciativa mal formulada o con problemas técnicos/administrativos/normativos insalvables."
        NV:
          ID: GN-FRPD-RATE-NV-01
          Cpt: "NV – No Vigente."
          Causa:
            - "Incumplimiento de plazos para subsanar observaciones."
            - "Financiamiento por otra fuente."
            - "Desistimiento."
            - "Incompatibilidades normativas."
          Res:
            - "Término del proceso de evaluación para el año presupuestario."

  Sec_9_Comunicacion_Resultados:
    ID: GN-FRPD-SEC-9-COMUNICACION
    Canales:
      ID: GN-FRPD-COMUNICACION-CANALES-01
      Medio_Principal:
        - "Publicación en página web del GORE Ñuble ([www.goredenuble.cl](www.goredenuble.cl))."
      Medio_Secundario:
        - "Comunicación vía correo electrónico a coordinadores de iniciativas desde difoi.nuble@goredenuble.cl."

  Sec_10_Ejecucion_Iniciativas:
    ID: GN-FRPD-SEC-10-EJECUCION
    Solicitud_Financiamiento:
      ID: GN-FRPD-EJEC-SOLICITUD-01
      Act:
        - "Departamento de Análisis y Evaluación emite reporte semanal al Gobernador y Jefe de División de Presupuesto con iniciativas aprobadas."
      Proc_Aprobacion:
        - "> 7.000 UTM: aprobación del Consejo Regional."
        - "<= 7.000 UTM: toma de conocimiento del Consejo Regional."
      Proc_Post_Aprobacion:
        - "Departamento de Presupuesto elabora resolución y solicita creación presupuestaria a DIPRES."
    Elaboracion_Convenio:
      ID: GN-FRPD-EJEC-CONVENIO-01
      Ctx:
        - "Inicia una vez emitida la resolución de DIPRES."
      Resp:
        - "Departamento de Presupuestos del GORE."
      Req:
        - "Firma del representante legal del servicio beneficiado."
    Transferencia_Recursos:
      ID: GN-FRPD-EJEC-TRANSFERENCIAS-01
      Cond:
        - "Según Ley de Presupuestos, programación financiera y avance efectivo del programa."
      Req:
        - "Cuenta corriente exclusiva para recursos FNDR."
    Seguimiento_Iniciativa:
      ID: GN-FRPD-EJEC-SEGUIMIENTO-01
      Resp:
        - "División Patrocinante del GORE."
      Obj:
        - "Seguimiento técnico y financiero."
    Reevaluaciones:
      ID: GN-FRPD-EJEC-REEVAL-01
      Def:
        - "Nuevo análisis frente a cambios significativos."
      Ctx:
        - "Aplica sólo a iniciativas con obras civiles."
      Prohib:
        - "No aplica a estudios ni programas."
      Proc:
        - "Modificaciones requieren ingreso de oficio al Gobernador para evaluación."

  Sec_11_Propiedad_Intelectual:
    ID: GN-FRPD-SEC-11-PROPIEDAD
    Reconocimiento:
      ID: GN-FRPD-PROPIEDAD-RECONOC-01
      Cpt:
        - "Propiedad intelectual de inventos e innovaciones según Ley 17.336 y 19.039."
      Entidad_Encargante:
        - "El GORE Ñuble se considera quien encarga el servicio."
      Compromiso_GORE:
        - "No perseguirá fines lucrativos con los resultados."
        - "No entregará información a terceros sin autorización expresa de la institución."
      Propiedad_Industrial:
        - "Aplica el mismo régimen que para propiedad intelectual."

  Sec_12_Compromiso_Gobierno_Regional:
    ID: GN-FRPD-SEC-12-COMPROMISO-GORE
    Compromiso:
      ID: GN-FRPD-COMPROMISO-01
      Cpt:
        - "Transferir recursos asignados según proyecto aprobado y programación financiera."
    Condiciones_Suspensivas:
      ID: GN-FRPD-COND-SUSPENSIVAS-01
      Cond:
        - "Existencia y disponibilidad de recursos en el presupuesto del GORE."
        - "No existencia de rebajas presupuestarias del Gobierno Central; en caso contrario, plazos y montos podrán modificarse."

  Sec_13_Garantias:
    ID: GN-FRPD-SEC-13-GARANTIAS
    Ambito:
      ID: GN-FRPD-GARANTIAS-AMBITO-01
      Ctx:
        - "Aplica sólo a instituciones privadas."
      Fnd:
        - "Res. 30 CGR; Oficio Circular N°20 Ministerio de Hacienda; Dictamen N°15.978/10 CGR."
    Reglas_Garantias:
      ID: GN-FRPD-GARANTIAS-REGLAS-01
      Req:
        - "Obligatoria para transferencias > 1.000 UTM."
      Purp:
        - "Velar por el cumplimiento de obligaciones del convenio."
      Instrumentos:
        - "Boletas de garantía."
        - "Vales vista."
        - "Otros instrumentos de cobro inmediato."
      Monto_Minimo:
        - "5% del total transferido (Art. 25 Ley N° 21.796)."
      Financiamiento_Garantia:
        - "Puede cargarse al ítem de 'Gastos Administrativos'."
      Vigencia:
        - "Mínimo 90 días posteriores al término de la iniciativa; se extiende si hay ampliación de plazo."

  Sec_14_Otros_Aspectos:
    ID: GN-FRPD-SEC-14-OTROS
    Transparencia_y_Comunicaciones:
      ID: GN-FRPD-OTROS-TRANSP-01
      Cpt:
        - "Normas gráficas de la Unidad de Comunicaciones del GORE aplican a todas las iniciativas."
      Act:
        - "Publicación mensual en la web del GORE de la cartera de proyectos ingresados y con convenio."
      Req_Instituciones_Privadas:
        - "Al postular: sitio web con información de la institución, directorio y representante legal; publicar estados financieros, balance y memoria anual (especialmente si adjudica > 2.000 UTM)."
        - "Durante ejecución: banner en web institucional con información de la iniciativa, convenio, avances, etc."
    Rendiciones_de_Cuenta:
      ID: GN-FRPD-OTROS-RENDICIONES-01
      Req:
        - "Documentos originales para rendición."
        - "Listados de participación con firmas en fresco o digitales."
    Uso_SISREC:
      ID: GN-FRPD-OTROS-SISREC-01
      Req:
        - "Rendir cuentas vía SISREC (Art. 24 Ley N° 21.796)."
      Resp:
        - "Órgano público que transfiere los fondos es responsable del uso de SISREC."
    Obligacion_Restituir_Fondos:
      ID: GN-FRPD-OTROS-RESTITUCION-01
      Causa:
        - "Uso de recursos en finalidad distinta a la autorizada."
        - "Fondos no utilizados."
        - "Fondos observados por contraparte GORE o Unidad de Control."
      Ctx:
        - "La obligación de restituir es distinta de la garantía de fiel cumplimiento."
    Contrapartes_Tecnicas:
      ID: GN-FRPD-OTROS-CONTRAPARTES-01
      Cpt:
        - "Contraparte postulante: persona responsable de la iniciativa informada antes del convenio; si no existe, se debe presupuestar su contratación."
        - "Contraparte GORE: nombrada según Resolución Exenta N°162 del 15/02/2023."
      Proc_Coordinacion:
        - "Se busca un flujo ágil; las instituciones deben canalizar la información mediante una contraparte."
        - "Para difusión, coordinar con Depto. de Comunicaciones o Gabinete del GORE."
    Acreditar_Objeto_Social:
      ID: GN-FRPD-OTROS-OBJETO-SOCIAL-01
      Req:
        - "Los convenios deben mencionar expresamente el objeto social de la institución privada."
        - "Acreditar objeto social pertinente a la actividad mediante documentación adjunta."
    Facultades_Supervision:
      ID: GN-FRPD-OTROS-SUPERVISION-01
      Cpt:
        - "GORE y Consejo Regional pueden supervisar iniciativas en ejecución y ex post (Ley N°19.175)."
      Proc:
        - "Dudas o interpretaciones sobre la guía serán resueltas por el GORE."
    Contratacion_Funcionarios_Universidades:
      ID: GN-FRPD-OTROS-UNIVERSIDADES-01
      Req:
        - "Universidades deben adjuntar declaración jurada simple del Rector con detalle de horas disponibles de académicos/investigadores para I+D."
      Cond:
        - "Las horas no deben traslaparse con actividades y horarios regulares de la universidad."
    Norma_Supletoria:
      ID: GN-FRPD-OTROS-NORMA-SUPLETORIA-01
      Cpt:
        - "Aspectos no cubiertos en esta guía se rigen por Guía Base FNDR (Res. Ex. N°83/2024), Normas de Inversión Pública y normativa legal vigente."
    Proteccion_Datos_Personales:
      ID: GN-FRPD-OTROS-DATOS-01
      Fnd:
        - "Ley N° 19.628 y sus modificaciones."
      Req:
        - "El postulante debe adoptar medidas técnicas y organizativas para asegurar confidencialidad, integridad y disponibilidad de datos personales."
      Derechos_Titulares:
        - "Acceso, rectificación, supresión, oposición y portabilidad."
    Normativa_Especifica_FRPD:
      ID: GN-FRPD-OTROS-NORMATIVA-ESPECIFICA-01
      Cpt:
        - "Regulación adicional podrá establecerse por decretos supremos del Ministerio de Hacienda (Ley N° 21.591)."
      Ctx:
        - "Estas bases se entienden complementadas por dicha normativa una vez publicada."

Formulario_FRPD_Application_2025:
  ID: GN-FRPD-FORM-APPLICATION-2025-01
  Purp: "Definir los campos obligatorios y estructura del formulario de postulación FRPD 2025."
  Ctx:
    - "Deriva directamente del bloque FORM-GN-FRPD-APPLICATION-2025-01 del documento fuente."
  Seccion_1_Identificacion_Iniciativa:
    ID: GN-FRPD-FORM-SEC1-IDENT
    Campos:
      - ID: GN-FRPD-FORM-COD-BIP
        Field-Label: "Código BIP"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-NOMBRE-PROGRAMA
        Field-Label: "Nombre del Programa"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-MONTO-FNDR
        Field-Label: "Monto solicitado FNDR"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 0."
      - ID: GN-FRPD-FORM-MONTO-TOTAL
        Field-Label: "Monto total del Programa"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 0."
      - ID: GN-FRPD-FORM-PLAZO-MESES
        Field-Label: "Plazo de ejecución (meses)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 1. Max-Val: 30."
      - ID: GN-FRPD-FORM-EJE-ERD
        Field-Label: "Eje ERD"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-LINEAMIENTO-ERD
        Field-Label: "Lineamiento ERD"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-OBJETIVO-ERD
        Field-Label: "Objetivo ERD"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-LINEAMIENTO-POSTULA
        Field-Label: "Lineamiento al que postula"
        Field-Type: Checkbox-Group
        Field-Instr: "Marcar con X el lineamiento al que postula."
        Field-Options:
          - "Social"
          - "Asistencia técnica a municipalidades"
          - "Cultural"
          - "Salud"
          - "Infancia"
          - "Energía, transportes y telecomunicaciones"
          - "Medioambiente y gestión de residuos"
          - "Gestión de recursos hídricos"
          - "Deportes"
          - "Movilidad urbana"
          - "Cuidados de adulto mayor"
          - "Conectividad digital"
          - "Emergencia"
          - "Fomento productivo, emprendimiento, innovación"
          - "Seguridad pública"
          - "Atracción de inversiones"

  Seccion_2_Institucion_Postulante:
    ID: GN-FRPD-FORM-SEC2-INSTITUCION
    Campos:
      - ID: GN-FRPD-FORM-INSTITUCION
        Field-Label: "Institución o Servicio Postulante"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-REP-LEGAL
        Field-Label: "Representante Legal"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-RESP-FORMULACION
        Field-Label: "Responsable de la formulación"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-CONTACTO-FORMULADOR
        Field-Label: "Correo y teléfono formulador"
        Field-Type: Text
        Field-Constraint: "Req: mandatory. Format: email."
      - ID: GN-FRPD-FORM-ANTECEDENTES-MISION
        Field-Label: "Antecedentes y Misión Institucional"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-NOMBRE-INSTRUMENTO
        Field-Label: "Nombre del instrumento o programa a utilizar"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-DESC-INSTRUMENTO
        Field-Label: "Descripción del instrumento o programa a utilizar"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-MARCO-LEGAL-PROGRAMA
        Field-Label: "Marco Legal para operar y realizar el programa"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-FUNDAMENTO-TRANSFERENCIA
        Field-Label: "Fundamento de la solicitud de transferencia a la institución"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-N-PROGRAMAS-EJEC
        Field-Label: "N° de programas en ejecución con Gobierno Regional"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 0."
      - ID: GN-FRPD-FORM-SALDO-POR-RENDIR
        Field-Label: "Saldo por rendir programas en ejecución (a la fecha de postulación)"
        Field-Type: Number
        Field-Constraint: "Req: mandatory. Min-Val: 0."

  Seccion_3_Diagnostico:
    ID: GN-FRPD-FORM-SEC3-DIAGNOSTICO
    Campos:
      - ID: GN-FRPD-FORM-ANALISIS-INVOLUCRADOS
        Field-Label: "Análisis de los involucrados"
        Field-Type: Static-Text
      - ID: GN-FRPD-FORM-DESC-GRUPO-OBJETIVO
        Field-Label: "Descripción del grupo objetivo"
        Field-Type: TextArea
        Field-Instr: "Identificar beneficiarios directos e indirectos en todos los niveles."
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-TERRITORIO-INTERVENIR
        Field-Label: "Territorio a intervenir"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-PROY-ANTERIORES
        Field-Label: "Identificación de proyectos o programas anteriores destinados al grupo objetivo (FNDR o Sectorial)."
        Field-Type: TextArea
      - ID: GN-FRPD-FORM-ANALISIS-BENEFICIARIOS
        Field-Label: "Análisis de los beneficiarios"
        Field-Type: Static-Text
      - ID: GN-FRPD-FORM-REQ-BENEFICIARIO
        Field-Label: "Requisitos específicos para calificar como beneficiario"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-PROC-SELECCION-BENEF
        Field-Label: "Descripción del procedimiento de selección de beneficiarios"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-BENEFICIOS-INDIVIDUALES
        Field-Label: "Beneficios a recibir por beneficiario individual"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-N-ESTIMADO-BENEF
        Field-Label: "Numero estimado de beneficiarios (por grupo objetivo y género)"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-ANALISIS-PROBLEMA
        Field-Label: "Análisis del Problema"
        Field-Type: Static-Text
      - ID: GN-FRPD-FORM-IDENTIFICACION-PROBLEMA
        Field-Label: "Identificación del problema (problemas principales de la situación)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-DEFINICION-PROBLEMA-CENTRAL
        Field-Label: "Definición del problema central (aplicando prioridad y selectividad)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-EFECTOS-PROBLEMA
        Field-Label: "Efectos del problema (definir los más importantes)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-CAUSAS-PROBLEMA
        Field-Label: "Causas del problema (elementos que lo provocan)"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-ARBOL-PROBLEMAS
        Field-Label: "Árbol de problemas (diagrama Causa-Efecto)"
        Field-Type: File
        Field-Instr: "Construir y presentar árbol de problemas. El árbol debe dar una imagen completa de la situación negativa. Verificar validez e integridad."
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-ARBOL-OBJETIVOS
        Field-Label: "Diagrama de árbol de soluciones (medios y fines)"
        Field-Type: File
        Field-Instr: "Convertir condiciones negativas a positivas. Examinar relación medio-fin. Añadir nuevos objetivos si es necesario."
        Field-Constraint: "Req: mandatory."

  Seccion_4_Identificacion_Programa:
    ID: GN-FRPD-FORM-SEC4-IDENT-PROGRAMA
    Campos:
      - ID: GN-FRPD-FORM-ESTRUCTURA-ANALITICA
        Field-Label: "Estructura Analítica del Programa"
        Field-Type: TextArea
      - ID: GN-FRPD-FORM-ARBOL-OBJETIVOS-SEL
        Field-Label: "Árbol de objetivos (seleccionados)"
        Field-Type: File
      - ID: GN-FRPD-FORM-ESTRUCTURA-PROGRAMA
        Field-Label: "Estructura del Programa"
        Field-Type: TextArea
      - ID: GN-FRPD-FORM-OBJ-GENERAL
        Field-Label: "Objetivo general del programa"
        Field-Type: TextArea
      - ID: GN-FRPD-FORM-PRODUCTOS-ENTREGAR
        Field-Label: "Productos que se entregarán"
        Field-Type: TextArea
      - ID: GN-FRPD-FORM-RESULTADOS-ESPERADOS
        Field-Label: "Resultados esperados"
        Field-Type: TextArea

  Seccion_5_Matriz_Marco_Logico:
    ID: GN-FRPD-FORM-SEC5-MML
    Campos:
      - ID: GN-FRPD-FORM-MATRIZ-MML
        Field-Label: "Matriz de Marco Lógico"
        Field-Type: Repeater
        Field-Instr: "Completar la matriz para cada nivel: Fin, Propósito, Componentes y Actividades."

  Seccion_6_Operatividad_Programa:
    ID: GN-FRPD-FORM-SEC6-OPERATIVIDAD
    Campos:
      - ID: GN-FRPD-FORM-ETAPA-PLANIFICACION-CONTROL
        Field-Label: "Etapa de Planificación y Control"
        Field-Type: File
        Field-Instr: "Incorporar carta Gantt de actividades y financiera."
        Field-Constraint: "Req: mandatory."

  Seccion_7_Presupuesto:
    ID: GN-FRPD-FORM-SEC7-PRESUPUESTO
    Campos:
      - ID: GN-FRPD-FORM-PRESUPUESTO-TITULO
        Field-Label: "Presupuesto"
        Field-Type: Static-Text
      - ID: GN-FRPD-FORM-PRESUPUESTO-DETALLADO
        Field-Label: "Presupuesto Detallado"
        Field-Type: Repeater
        Field-Instr: "Añadir una fila por cada ítem del presupuesto."
      - ID: GN-FRPD-FORM-RESUMEN-PRESUP-CLASIF-PRESUP
        Field-Label: "Resumen Presupuesto (por Clasificación Presupuestaria)"
        Field-Type: Repeater
      - ID: GN-FRPD-FORM-RESUMEN-PRESUP-CLASIF-SISREC
        Field-Label: "Resumen Presupuesto (por Clasificación SISREC)"
        Field-Type: Repeater
      - ID: GN-FRPD-FORM-DETALLE-CONTRATACION-PERSONAS
        Field-Label: "Detalle Contratación de Personas"
        Field-Type: Repeater
      - ID: GN-FRPD-FORM-DETALLE-DIFUSION-HITOS
        Field-Label: "Detalle actividades difusión e hitos comunicacionales"
        Field-Type: Repeater

  Seccion_8_Resumen_Programa:
    ID: GN-FRPD-FORM-SEC8-RESUMEN
    Campos:
      - ID: GN-FRPD-FORM-RESUMEN-PROGRAMA
        Field-Label: "Resumen del Programa"
        Field-Type: TextArea
        Field-Constraint: "Req: mandatory. Max-Len: 3000."
        Field-Instr: "¾ de hoja máximo."
      - ID: GN-FRPD-FORM-FIRMA-FORMULADOR
        Field-Label: "Nombre, firma y timbre del Formulador"
        Field-Type: Signature
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-FIRMA-REPRESENTANTE
        Field-Label: "Nombre, firma y timbre del jefe de Servicio o Representante"
        Field-Type: Signature
        Field-Constraint: "Req: mandatory."
      - ID: GN-FRPD-FORM-CONTACTO-FORMULADOR-FINAL
        Field-Label: "Fono y Mail del formulador"
        Field-Type: Text
        Field-Constraint: "Req: mandatory."