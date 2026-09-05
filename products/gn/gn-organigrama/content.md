---
urn: urn:gn:kb:gn-organigrama
nombre: gn-organigrama
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-organigrama; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml (sha256:dae085948421d892cdffdf69a07014767cb75c5805bedd4d7aed97e6f64bd81f); URN KODA legado urn:gorenuble:gn:organigrama:1.0.0; estado original Published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2026-01-26
lang: es
tags: ["gn", "gore-os", "koda", "domains", "01-fundamentos", "intro", "organigrama"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:organigrama:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2026-01-27"
    last_modified_at: "2026-01-27"
    signature: null

ID: KB-GN-002-ORGANIGRAMA-01
Version: 1.0.0
Status: Published
Human-Creator: FSA
Human-Editor: FSA
Model-Collaborator: GPT-5.2
Creation-Date: 2026-01-26
Modification-Date: 2026-01-26
Primary-Source: "staging/organigrama_gore_2026.md"
Ctx: "Organigrama institucional del Gobierno Regional de Ñuble (versión 2026)."

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

Organigrama_Institucional_GORE_Nuble:
  ID: GN-ORG-2026-01
  Purp: "Describir estructura organizacional y funciones generales por unidad."
  Ctx:
    - "Contenido redactado como descripciones funcionales (no incluye dotación/cargos específicos)."
    - "Orden de unidades preserva el orden del documento fuente."

  Maxima_Autoridad:
    Gobernador_Regional:
      ID: GN-ORG-GOBERNADOR-01
      Def: "Máxima autoridad ejecutiva del Gobierno Regional; dirige la administración del Gobierno Regional."
      Src:
        - "Ley Orgánica Constitucional de Gobierno y Administración Regional (LOCGAR), Ley N°19.175."
        - "Constitución Política de la República."
      Act:
        - "Gestionar administración del Gobierno Regional."
        - "Ejecutar funciones propias del servicio."
        - "Coordinar trabajo de las divisiones del Gobierno Regional."
        - "Presidir el Consejo Regional."
      Req:
        - "Ejercer funciones con estricto apego a la Constitución Política de la República."

  Unidades_y_Organos:
    Unidad_de_Gabinete_y_Participacion_Social:
      ID: GN-ORG-GABINETE-01
      Purp: "Asesoría al Gobernador Regional y al equipo directivo; coordinación institucional."
      Act:
        - "Asesorar al Gobernador Regional y equipo directivo en materias específicas (principalmente administrativas y de gestión)."
        - "Coordinar agenda institucional, despliegue territorial y audiencias."
        - "Preparar información de respaldo para actividades institucionales."
        - "Contribuir a articulación con actores del sector público y privado."

    Departamento_de_Comunicaciones:
      ID: GN-ORG-COMUNICACIONES-01
      Purp: "Comunicación externa e interna del Gobierno Regional."
      Act:
        - "Diseñar, planificar y ejecutar estrategias de comunicación para mantener a la ciudadanía informada del quehacer, planes y objetivos del Gobierno Regional y su Consejo."
        - "Gestionar vinculación con actores relacionados con la institución."
        - "Gestionar relación formal con medios de comunicación e imagen institucional."
        - "Fortalecer confianza en la información entregada y transparencia de acciones."
        - "Promover comunicación clara y cercana a la ciudadanía."
        - "Fortalecer flujos de información interna para alinear equipos, fomentar cultura organizacional y mejorar compromiso con objetivos estratégicos."

    Unidad_de_Control:
      ID: GN-ORG-CONTROL-01
      Purp: "Auditoría operativa interna; control de legalidad y ejecución financiera/presupuestaria."
      Dependencia: "Gobernador Regional."
      Relacion:
        - "Colabora directamente con el Consejo Regional en su función de fiscalización."
      Act:
        - "Realizar auditoría operativa interna institucional."
        - "Fiscalizar legalidad de actos del Gobierno Regional."
        - "Controlar ejecución financiera y presupuestaria."
        - "Emitir informes trimestrales al Consejo Regional."
        - "Responder consultas del Consejo Regional."
        - "Informar sobre reclamaciones."
        - "Representar al Gobernador Regional actos que se estimen ilegales."
        - "Asesoría técnica permanente al Gobernador Regional y al Consejo Regional en cumplimiento normativo, auditoría interna y control de gestión."
        - "Identificar, evaluar y mitigar riesgos institucionales."
        - "Resguardar uso eficiente, eficaz y conforme a derecho de recursos públicos regionales."
        - "Seguimiento sistemático de ejecución presupuestaria."
        - "Informar trimestralmente al Consejo Regional sobre avance financiero, procesos de contratación pública, licitaciones y materias relevantes para toma de decisiones."

    Consejo_de_la_Sociedad_Civil_COSOC:
      ID: GN-ORG-COSOC-01
      Def: "Órgano colegiado y autónomo."
      Obj:
        - "Promover y fortalecer participación ciudadana en gestión del Gobierno Regional."
        - "Fiscalizar cumplimiento de normas de participación civil."
      Ctx:
        - "Con representación de organizaciones de la sociedad civil de la Región de Ñuble vinculadas a competencias del Gobierno Regional."
      Res:
        - "Contribuye a transparencia, eficacia y legitimidad de la acción gubernamental a nivel regional."

    Consejo_Regional_de_Nuble_CORE:
      ID: GN-ORG-CORE-01
      Def: "Órgano normativo, fiscalizador y decisorio del Gobierno Regional."
      Purp: "Hacer efectiva la participación de la comunidad regional en el gobierno regional."
      Ctx:
        - "Compuesto por 16 Consejeras y Consejeros Regionales."
        - "Elegidos democráticamente para representar provincias: Diguillín, Punilla e Itata."
        - "Presidido por el Gobernador Regional."
      Src:
        - "Ley 19.175 Orgánica Constitucional sobre Gobierno y Administración Regional."

    Secretaria_Ejecutiva_del_Consejo_Regional:
      ID: GN-ORG-SEC-CORE-01
      Def: "Unidad administrativa, técnica y operativa que facilita y coordina funcionamiento del CORE."
      Act:
        - "Asegurar cumplimiento de acuerdos y resoluciones del Consejo."
        - "Servir de enlace entre CORE, Gobernador Regional, unidades del Gobierno Regional y comunidad."
        - "Coordinar, colaborar y asesorar desempeño de funciones del Consejo Regional."
        - "Apoyar planificación anual."
        - "Registrar acuerdos."
        - "Elaborar actas de cada sesión."

    Administracion_Regional:
      ID: GN-ORG-ADMIN-REGIONAL-01
      Purp: "Gestión administrativa integral y coordinación del accionar de jefaturas de divisiones."
      Act:
        - "Coordinar accionar de jefes/as de cada una de las divisiones."
        - "Ejecutar materias propias del servicio."
        - "Ejercer subrogancia del Gobernador Regional en caso de ausencia."
      Ctx:
        - "Desempeño del cargo bajo exclusiva confianza del Gobernador Regional."

    Corporacion_Regional_de_Desarrollo:
      ID: GN-ORG-CORP-DESARROLLO-01
      Mssn: "Entidad asesora del Gobierno Regional de Ñuble en planificación, gestión y desarrollo de políticas públicas."
      Obj: "Promover desarrollo integral y articulado público-privado en áreas de interés de la región."
      Act:
        - "Contribuir a promoción, posicionamiento y avance de la región a nivel nacional e internacional."
        - "Implementar iniciativas para disminuir desigualdades socio-territoriales."
      Ctx:
        - "Núcleo de intervención: provincias y comunas de la región."

    Auditoria_Interna:
      ID: GN-ORG-AUD-INTERNA-01
      Def: "Unidad de monitoreo independiente y objetivo del sistema de control interno del Gobierno Regional."
      Act:
        - "Evaluación objetiva e independiente de gestión y desempeño del Gobierno Regional."
        - "Examinar y analizar procesos administrativos, financieros y operativos para asegurar conformidad normativa y uso eficiente de recursos."
        - "Realizar auditoría operativa interna del GORE."
        - "Velar por transparencia activa según ley de acceso a la información pública."
        - "Asesorar al Gobernador Regional y jefaturas en asuntos de funcionamiento (excepto procesos disciplinarios)."
        - "Coordinar seguimiento de recomendaciones de la Contraloría General de la República."

    Departamento_Juridico:
      ID: GN-ORG-JURIDICO-01
      Purp: "Asesoría legal interna; resguardo de legalidad institucional."
      Act:
        - "Asesorar en materias legales a distintas áreas del servicio."
        - "Elaborar y supervisar actos administrativos."
        - "Representación judicial y extrajudicial del Gobierno Regional."
        - "Entregar lineamientos legales a la autoridad y unidades."
        - "Mantener informados estamentos sobre normas legales y reglamentarias pertinentes."

    Departamento_de_Gestion_Institucional:
      ID: GN-ORG-GESTION-INST-01
      Purp: "Planificación institucional y control de gestión para toma de decisiones."
      Act:
        - "Desarrollar sistema de planificación y control de gestión."
        - "Formular, monitorear y dar seguimiento a indicadores de desempeño institucional."
        - "Planificar, organizar y controlar procesos administrativos y estratégicos para asegurar cumplimiento de objetivos."
        - "Optimizar recursos y lograr objetivos de calidad y eficiencia."
        - "Implementar políticas y mejora continua para asegurar buen funcionamiento administrativo y organizacional."
      Unidades_Dependientes:
        Oficina_OIRS:
          ID: GN-ORG-OIRS-01
          Def: "Oficina de Informaciones, Reclamos y Sugerencias (OIRS)."
          Purp: "Facilitar vínculo ciudadanía–Gobierno Regional."
          Act:
            - "Generar espacios de atención y participación ciudadana."
            - "Facilitar interacción con la ciudadanía."
            - "Garantizar derecho de acceso a la información pública."
            - "Gestionar y canalizar reclamos, sugerencias y felicitaciones recibidos en la institución."
            - "Asegurar atención oportuna."
            - "Retroalimentar administración con base en necesidades y sugerencias de la comunidad."

    Departamento_Nuble_250:
      ID: GN-ORG-NUBLE-250-01
      Purp: "Articulación técnica y seguimiento de proyectos estratégicos priorizados (Agenda Ñuble 250)."
      Ctx:
        - "Agenda Ñuble 250: hoja de ruta regional hacia 2028; concordante con el primer decenio de creación de la Región de Ñuble."
      Act:
        - "Articular técnicamente, coordinar, controlar y dar seguimiento a la gestión de proyectos estratégicos de la cartera de inversión priorizada."
        - "Favorecer trabajo coordinado entre reparticiones públicas y divisiones del Gobierno Regional."
        - "Fortalecer gobernanza territorial y coherencia de acción estatal en la región."
      Req:
        - "Alineación con objetivos de la Estrategia de Desarrollo Regional."

    Unidad_Regional_de_Asuntos_Internacionales_URAI:
      ID: GN-ORG-URAI-01
      Purp: "Gestión de internacionalización de la región."
      Act:
        - "Propiciar cooperación internacional."
        - "Impulsar paradiplomacia."
        - "Coordinar con entidades nacionales e internacionales."
        - "Promover desarrollo regional y participación comunitaria en ámbito exterior."
        - "Complementar funciones del gobierno central."
      Res:
        - "Contribuye a participación activa de la Región de Ñuble en escena internacional."

    Departamento_Coordinacion_Integral_de_Emergencia_y_Seguridad:
      ID: GN-ORG-EMERG-SEG-01
      Purp: "Mejorar respuesta oportuna y coordinada ante emergencias y seguridad pública."
      Mech:
        - "Integración de sistemas de comunicaciones, información, televigilancia y medios logísticos."
        - "Colaboración entre distintas instituciones."
      Act:
        - "Formular, diseñar y evaluar políticas y estrategias en seguridad pública y gestión de riesgo de desastres."
        - "Gestionar cartera de proyectos GORE en seguridad y gestión de riesgo de desastres."
        - "Mantener coordinación permanente con municipalidades e instituciones de la región en estas materias."

  Divisiones:
    Division_de_Planificacion_y_Desarrollo_Regional:
      ID: GN-ORG-DIV-PLAN-01
      Purp: "Planificación territorial y apoyo a evaluación de políticas regionales."
      Act:
        - "Elaborar y proponer estrategias, políticas, planes, programas y proyectos para desarrollo armónico del territorio (incluye Plan Regional de Ordenamiento Territorial)."
        - "Basar procesos en insumos técnicos y participativos, conforme a prioridades definidas por el gobierno regional."
        - "Apoyar al Gobernador Regional en evaluación de cumplimiento de políticas, planes, programas, proyectos y presupuestos de carácter regional."
        - "Prestar asistencia técnica a municipalidades y otros organismos de la administración que lo requieran."
      Componentes:
        Comite_de_Pertinencia_y_Vinculacion_Estrategica:
          ID: GN-ORG-COMITE-PERTINENCIA-01
          Def: "Instancia formal de asesoría y análisis de proyectos."
          Integrantes:
            - "Administrador(a) Regional."
            - "Jefaturas de Divisiones: Planificación y Desarrollo Regional (Presidente del Comité), Presupuesto e Inversión Regional, Fomento e Industria, Desarrollo Social y Humano, Infraestructura y Transporte."
          Act:
            - "Asesorar integralmente a la autoridad."
            - "Analizar admisibilidad de proyectos postulados."
            - "Analizar pertinencia regional con base en instrumentos de planificación regional y competencias determinadas en la Ley Orgánica de Gobierno y Administración Regional."

        Departamento_de_Planificacion_Estrategica_y_Ordenamiento_Territorial:
          ID: GN-ORG-DEP-PEOT-01
          Purp: "Planificación estratégica y ordenamiento territorial regional."
          Mssn: "Impulsar desarrollo armónico y sostenible."
          Act:
            - "Elaborar y proponer planes de desarrollo local que integren necesidades de la comunidad con análisis de restricciones ambientales y particularidades geofísicas del territorio."
            - "Considerar vocación productiva distintiva de cada comuna, infraestructura existente y proyecciones de crecimiento futuro."
            - "Coordinar formulación y seguimiento del Anteproyecto Regional de Inversión (ARI)."
            - "Coordinar formulación y seguimiento del Programa Público de Inversión Regional (PROPIR)."

        Departamento_de_Desarrollo_de_Proyectos_Estrategicos:
          ID: GN-ORG-DEP-DPE-01
          Purp: "Gestión de iniciativas de alto impacto alineadas con visión regional."
          Act:
            - "Seleccionar, planificar y supervisar iniciativas de alto impacto."
            - "Alinear operación diaria con visión de largo plazo del Gobierno Regional."
            - "Facilitar vínculo entre visión de la autoridad regional, su Consejo y directivos."
            - "Asegurar contribución de proyectos a competitividad, innovación y crecimiento territorial."
          Req:
            - "Alineación con Estrategia Regional de Desarrollo."

        Departamento_Zonas_en_Desarrollo:
          ID: GN-ORG-DEP-ZED-01
          Purp: "Acceso equitativo al desarrollo y fortalecimiento de descentralización."
          Ctx:
            - "Enfoque de derechos."
          Act:
            - "Promover inversión pública focalizada."
            - "Fortalecer descentralización."
            - "Promover participación de actores de la sociedad."
            - "Promover desarrollo territorial integral y equilibrado con base en especificidades regionales."

    Division_de_Presupuesto_e_Inversion_Regional:
      ID: GN-ORG-DIV-PRESUPUESTO-INVERSION-01
      Purp: "Presupuesto de inversión regional; ejecución, control y asesoría al Gobernador."
      Act:
        - "Elaborar proyectos de presupuestos de inversión del gobierno regional."
        - "Ejecutar y controlar presupuesto de inversión y programas administrados por el gobierno regional."
        - "Asesorar al Gobernador Regional en definición de proyectos de inversión a desarrollar o financiar según lineamientos y prioridades de instrumentos de planificación regional."
      Componentes:
        Departamento_de_Analisis_y_Evaluacion:
          ID: GN-ORG-DEP-AE-01
          Purp: "Revisión y evaluación técnica de proyectos/programas postulados."
          Ctx:
            - "Postulación a financiamiento FNDR."
          Act:
            - "Evaluar pertinencia con lineamientos regionales."
            - "Asesorar en determinación de proyectos a desarrollar."
            - "Proporcionar proyectos con RS coordinando el Comité de Pertinencia y Vinculación Estratégica para análisis y priorización."
            - "Establecer metodologías y analizar normativa técnica y presupuestaria para postulación a financiamiento."
            - "Controlar solicitudes de financiamiento de inversión regional."
            - "Apoyar formulación de proyectos y programas regionales."
            - "Coordinar asesoría técnica a municipalidades y otros servicios para cumplimiento del desarrollo regional."
          Unidades_Dependientes:
            Unidad_de_Municipalidades_y_Conservaciones:
              ID: GN-ORG-UNID-MUNIC-CONS-01
              Def: "Unidad dependiente del Departamento de Análisis y Evaluación."
              Purp: "Evaluación de proyectos de inversión local."
              Ctx:
                - "Tipos: FRIL, Circular 33, PMU-PMB."
              Act:
                - "Evaluar técnica y administrativamente proyectos de inversión local."
                - "Asegurar viabilidad normativa y financiera."
                - "Fortalecer gestión comunal mediante asesoría directa y capacitación externa para optimizar formulación de iniciativas territoriales."
                - "Tramitar convenios, resoluciones y registro en plataformas oficiales del Estado."

            Unidad_de_Proyectos_y_Programas:
              ID: GN-ORG-UNID-PP-01
              Purp: "Evaluación de iniciativas FNDR, programas y concursos asociados al programa de inversión regional."
              Ctx:
                - "Concursos: 8%, FRPD, otros; activos no financieros."
              Act:
                - "Evaluar técnica y administrativamente iniciativas FNDR, programas públicos y concursos."
                - "Gestionar admisibilidad y visación ante el Ministerio de Desarrollo Social cuando corresponda."
                - "Asesorar a divisiones regionales, servicios, universidades y organizaciones privadas para correcta formulación de proyectos."
                - "Ejecutar planes de capacitación externa."

        Departamento_de_Presupuesto:
          ID: GN-ORG-DEP-PRESUPUESTO-01
          Purp: "Gestión integral del presupuesto de inversión."
          Act:
            - "Gestionar presupuesto desde identificación presupuestaria hasta control y seguimiento."
            - "Elaborar resoluciones."
            - "Gestionar caja."
            - "Coordinar internamente con divisiones del Gobierno Regional."
            - "Coordinar externamente con Dirección de Presupuestos (DIPRES), SUBDERE y Contraloría Regional."

    Division_de_Desarrollo_Social_y_Humano:
      ID: GN-ORG-DIV-DSH-01
      Def: "Eje de la inversión social del Gobierno Regional de Ñuble."
      Purp: "Fortalecer desarrollo humano y reducir brechas estructurales."
      Act:
        - "Definir e implementar lineamientos estratégicos de inversión social."
        - "Diseñar, ejecutar y dar seguimiento a políticas regionales, programas y proyectos sociales."
      Ctx:
        - "Ámbitos: pobreza, educación, salud, género, neurodiversidad, vivienda, entre otros."
      Obj:
        - "Promover equidad territorial."
        - "Promover inclusión social."
        - "Resguardar dignidad humana."
      Res:
        - "Complementa y fortalece acción del Estado en la región."
      Componentes:
        Departamento_de_Fondos_Concursables_y_Programas_Sociales:
          ID: GN-ORG-DEP-FCPS-01
          Purp: "Gestión de fondos concursables y programas sociales."
          Act:
            - "Planificar, coordinar, gestionar y supervisar inversión social mediante fondos concursables y programas sociales."
            - "Asegurar asignación eficiente, transparente y pertinente de recursos públicos."
            - "Promover iniciativas con impacto social, pertinencia territorial y enfoque de derechos."
            - "Articular trabajo con municipios, servicios públicos, organizaciones de la sociedad civil y otras entidades ejecutoras."
            - "Velar por ciclo de vida de iniciativas: diseño, evaluación, ejecución, seguimiento y cierre."
          Req:
            - "Coherencia con Estrategia Regional de Desarrollo, políticas públicas vigentes y prioridades definidas por el Gobierno Regional."

        Departamento_de_Gestion_Territorial:
          ID: GN-ORG-DEP-GT-01
          Purp: "Operativización y despliegue territorial de oferta programática."
          Act:
            - "Actuar como nexo de vinculación estratégica entre el Gobierno Regional de Ñuble y las personas de la región."
            - "Fortalecer desarrollo social y comunitario."
            - "Asegurar pertinencia territorial de actividades."
            - "Contribuir a priorización de inversión regional."
            - "Realizar seguimiento técnico de cartera de inversión social de la división."

    Division_de_Fomento_e_Industria:
      ID: GN-ORG-DIV-FOMENTO-01
      Purp: "Fomento productivo, ciencia, tecnología e innovación."
      Act:
        - "Proponer, promover y ejecutar planes y programas regionales para estimular desarrollo de ciencia, tecnología e innovación y nuevas capacidades empresariales."
        - "Facilitar incorporación de nuevas tecnologías de la información para favorecer crecimiento sostenido, integrado y sustentable."
        - "Proponer y promover instrumentos de fomento productivo."
      Componentes:
        Departamento_de_Fomento_y_Desarrollo_Productivo:
          ID: GN-ORG-DEP-FDP-01
          Purp: "Impulso a economía regional y emprendimiento."
          Act:
            - "Promover emprendimiento."
            - "Diseñar políticas regionales de fomento y desarrollo productivo."
            - "Ejecutar planes, programas e instrumentos de fomento productivo."
            - "Lograr crecimiento sostenible, integrado y articulado con actores relevantes de la región."

        Departamento_de_Ciencia_Tecnologia_e_Innovacion:
          ID: GN-ORG-DEP-CTI-01
          Purp: "Fomento del conocimiento, investigación y desarrollo tecnológico regional."
          Obj: "Sostenibilidad y crecimiento económico."
          Act:
            - "Planificar, diseñar e implementar estrategias de CTI."
            - "Coordinar y articular actores relevantes: sector público, academia y ámbito privado."
            - "Contribuir a creación de políticas públicas."
            - "Fortalecer ecosistema regional."

    Division_de_Infraestructura_y_Transportes:
      ID: GN-ORG-DIV-INFRA-TRANS-01
      Purp: "Obras de infraestructura y equipamiento regional; gestión en transportes."
      Act:
        - "Proponer, promover y ejecutar planes y programas regionales en infraestructura, equipamiento regional y transportes."
      Componentes:
        Departamento_de_Infraestructura_y_Conectividad:
          ID: GN-ORG-DEP-INFRA-CONECT-01
          Purp: "Infraestructura, transporte, movilidad y conectividad (vial y digital)."
          Act:
            - "Proponer y promover planes, estudios y programas regionales en coordinación con servicios públicos regionales."
            - "Analizar e identificar brechas existentes en infraestructura, transporte, movilidad y conectividad en distintas escalas territoriales."
            - "Entregar directrices para oferta de programas y servicios de conectividad."
            - "Promover y coordinar iniciativas para ampliar cobertura y calidad del transporte colectivo."
            - "Proponer iniciativas para intermovilidad segura mediante programas y obras."
            - "Evaluar y coordinar con otras instituciones planes de inversiones en movilidad."
            - "Estudiar y proponer sistemas de Transporte Inteligente."

        Departamento_de_Ejecucion_y_Supervision_de_Proyectos_de_Inversion:
          ID: GN-ORG-DEP-ESP-01
          Purp: "Supervisión de ejecución de proyectos de inversión regional."
          Act:
            - "Supervisar gestión eficiente de inversión regional mediante control riguroso de ejecución de proyectos asignados."
            - "Fiscalización técnica (física) y presupuestaria (financiera) para resguardar integridad del proceso."
            - "Coordinar con Contrapartes Técnicas para asegurar cumplimiento de objetivos institucionales."
            - "Ejecutar de manera directa iniciativas de inversión que le sean encomendadas (responsabilidad técnica y administrativa)."

    Division_de_Administracion_y_Finanzas:
      ID: GN-ORG-DIV-ADAF-01
      Purp: "Gestión administrativa y financiera; presupuesto de funcionamiento; servicios generales; personal."
      Src:
        - "Ley N.º 19.175."
        - "Ley N.º 18.834."
      Res: "Sustenta funcionamiento eficiente y transparente del Gobierno Regional."
      Componentes:
        Oficina_de_Partes:
          ID: GN-ORG-OF-PARTES-01
          Purp: "Gestión documental institucional."
          Act:
            - "Recepción, distribución, archivo, registro y despacho de documentación de entrada y salida de servicios administrativos del Gobierno Regional de Ñuble."
            - "Gestión de otras materias propias de su naturaleza y/o encomendadas o delegadas."

        Departamento_de_Gestion_y_Desarrollo_de_Personas:
          ID: GN-ORG-DEP-GDP-01
          Purp: "Estrategias, políticas y procesos del ciclo de vida laboral del personal."
          Act:
            - "Definir, elaborar e implementar estrategias, políticas y procesos institucionales de gestión de personas."
            - "Asegurar equipo humano competente, motivado y alineado con objetivos de desarrollo regional."
          Req:
            - "Concordancia con lineamientos de la autoridad regional."
            - "Concordancia con normativa vigente aplicable al sector público."
            - "Concordancia con instrumentos de gestión de personas del Estado."

        Departamento_de_Finanzas:
          ID: GN-ORG-DEP-FINANZAS-01
          Purp: "Revisión y control de información presupuestaria, contable y financiera."
          Act:
            - "Supervisar elaboración y ejecución del presupuesto."
            - "Gestionar registro contable y elaboración de estados financieros."
            - "Analizar situación económica para toma de decisiones."
            - "Implementar políticas de control para seguridad de activos."
            - "Optimizar uso de recursos."
          Res: "Garante de salud financiera y transparencia institucional."
          Unidades_Dependientes:
            Unidad_de_Tesoreria:
              ID: GN-ORG-UNID-TESORERIA-01
              Purp: "Administración y custodia de ingresos y egresos; pagos y flujo de caja."
              Act:
                - "Administrar, controlar y custodiar ingresos y egresos del Gobierno Regional."
                - "Gestionar fondos institucionales, pagos y flujo de caja."
                - "Velar por liquidez y estabilidad financiera."
              Res:
                - "Asegura cumplimiento de obligaciones financieras."
                - "Asegura eficiencia en ejecución presupuestaria."

            Unidad_de_Contabilidad_y_Finanzas:
              ID: GN-ORG-UNID-CONTAB-FIN-01
              Purp: "Registro, control y análisis de información contable y presupuestaria."
              Act:
                - "Registrar, controlar y analizar información contable y presupuestaria."
                - "Resguardar integridad de datos financieros y contables."
              Res:
                - "Permite gestión alineada con normativas vigentes y buenas prácticas del sector público."

            Unidad_de_Control_de_Rendiciones:
              ID: GN-ORG-UNID-RENDICIONES-01
              Purp: "Seguimiento y control de rendiciones de cuentas."
              Act:
                - "Seguimiento, monitoreo, control y contabilización de rendiciones de cuentas ingresadas al Gobierno Regional."
                - "Asegurar uso de recursos conforme a normativa vigente, de forma eficiente, transparente y oportuna."
              Res:
                - "Resguarda correcta administración de fondos públicos."

            Unidad_de_Adquisiciones:
              ID: GN-ORG-UNID-ADQ-01
              Purp: "Procesos de compras de bienes y servicios."
              Req:
                - "Apego a Ley de Compras Públicas y su reglamento."
              Act:
                - "Ejecutar procesos de adquisiciones de bienes y servicios necesarios para funcionamiento institucional."
                - "Publicar y monitorear contrataciones especialmente encomendadas provenientes del programa de inversiones, junto a unidad técnica designada."
              Obj:
                - "Eficiencia."
                - "Transparencia."
                - "Probidad."

            Unidad_de_Operaciones:
              ID: GN-ORG-UNID-OPERACIONES-01
              Purp: "Infraestructura física, flota vehicular y tecnologías de la información."
              Act:
                - "Gestionar infraestructura física (edificios e instalaciones) y flota de vehículos institucionales."
                - "Coordinar mantenimiento preventivo, correctivo y respuesta a emergencias."
                - "Asegurar operatividad, funcionalidad y seguridad de recursos físicos institucionales."
                - "Gestionar y mantener infraestructura TI: red, servidores, hardware, software, sistemas de información."
                - "Gestionar políticas de seguridad informática y protección de datos institucionales."
                - "Desarrollar soluciones tecnológicas alineadas con objetivos estratégicos del Gobierno Regional."
              Src:
                - "Ley de Transformación Digital."
