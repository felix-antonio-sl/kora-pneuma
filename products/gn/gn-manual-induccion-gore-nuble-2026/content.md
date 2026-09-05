---
urn: urn:gn:kb:gn-manual-induccion-gore-nuble-2026
nombre: gn-manual-induccion-gore-nuble-2026
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-induccion-gore-nuble-2026; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/kb_gn_017_manual_induccion_gore_nuble_2025_koda.yml (sha256:7af17924f696f84e94748f03474d11a99dd3beff9c3a40df39ae5dcb369bd90b); URN KODA legado urn:gorenuble:gn:manual-induccion-gore-nuble-2026:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manual", "induccion"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-induccion-gore-nuble-2026:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_017_manual_induccion_gore_nuble_2025_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2025-12-14"
    last_modified_at: "2025-12-15"
    signature: null

ID: KB-GN-017-MANUAL-INDUCCION-GORE-NUBLE-2026-01
Version: 1.0.0
Status: Draft
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "CASCADE"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-15"
Primary-Source: "staging/gn/kodeando/manual_induccion_gore_ñuble_2024.md"
Ctx: "Manual de Inducción del Gobierno Regional de Ñuble 2026."

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

Manual_de_Induccion_Gobierno_Regional_de_Nuble_2026:
  ID: GN-MANUAL-INDUCCION-2026-01
  Titulo:
    Def: "Manual de Inducción del Gobierno Regional de Ñuble 2026"

  Seccion_1_Introduccion:
    ID: GN-MANUAL-INDUCCION-S01

    Que_es_la_induccion:
      Def:
        - >-
          La inducción es una herramienta de gestión que apunta a integrar de manera planificada a las personas que ingresan a la organización o cambian de funciones, a través de un proceso de acompañamiento tendiente a ofrecer la información necesaria para desempeñarse en forma cómoda y eficaz. Permite conocer y comprender los aspectos específicos del trabajo y los procedimientos de la institución, promoviendo la adaptación a las características organizacionales (Servicio Civil, 2016).
        - >-
          Dicho de otro modo, la inducción busca contribuir a un ajuste entre persona/puesto/organización a través de acciones deliberadas tendientes a apoyar a las nuevas personas en su integración a la cultura organizacional (Servicio Civil, 2016). Es un proceso que, además de entregar una visión global de la organización, sus proyectos y dar calidez al ingreso, involucra el inicio de la interiorización en los valores institucionales, conocer las prácticas predominantes y los comportamientos acordes a las expectativas de un sistema social estable. Implica el desafío de incorporar e integrar a un nuevo colaborador a una cultura colectiva que determina la manera de actuar (Servicio Civil, 2016).

    Objetivos_del_proceso_de_induccion:
      Ctx: "En sus orientaciones para el proceso de inducción, el Servicio Civil considera esta como un proceso estratégico para la institución, cuyos objetivos son:"
      Obj:
        - Socializar:
            Def: "Proceso a través del cual el funcionario/a empieza a conocer e integrarse con las personas que forman parte de la institución, y particularmente, con su equipo de trabajo."
        - Orientar:
            Def: "Proceso a través del cual se apoya al funcionario/a para que comience a comprender y aceptar los valores, normas, derechos, deberes y convicciones de la organización y su contexto."
        - Entrenar:
            Def: "Proceso que facilita el aprendizaje inicial del funcionario/a en las funciones propias, y cómo estas se vinculan con las funciones de su equipo y con la misión y objetivos institucionales."
        - Alinear_respecto_al_rol:
            Def: "Proceso de vinculación del desempeño esperado del funcionario/a con las definiciones y productos estratégicos de la institución, y sus propias expectativas al respecto."
        - Fidelizar:
            Def: "Proceso de fortalecimiento de la identificación del funcionario/a con la función pública en general y con su servicio en particular, y la generación y/o profundización de un compromiso individual con sus funciones."

    Beneficios:
      Ctx: "El Servicio Civil en sus orientaciones reconoce como principales beneficios de contar con un programa de inducción los siguientes:"
      Res:
        - "Atender adecuadamente la forma en la que se insertan y se adaptan las personas en una organización."
        - "Incorporar de manera más efectiva a las personas a sus nuevas funciones, contexto y grupo humano de trabajo."
        - "Favorecer el contrato psicológico entre las personas y la institución, es decir, entre las expectativas del servicio y las que las personas tienen respecto a su desarrollo en el mismo."
        - "Contribuir al logro de los resultados de desempeño del nuevo funcionario/a."
        - "Posibilitar que las personas se sientan parte y se identifiquen con la institución."
        - "Facilitar y direccionar las potencialidades de las personas hacia los objetivos institucionales."
        - "Facilitar que la persona demuestre en el corto plazo resultados en su propio desempeño y en su aporte a la consecución de los resultados de la institución."

    Induccion_y_ciclo_de_vida_laboral:
      Ctx: >-
        La inducción constituye un proceso crítico en el ciclo de vida laboral de las personas en cualquier organización. Una buena recepción e incorporación no sólo resulta relevante en tanto acogida, sino que también puede contribuir al sentido de compromiso del funcionario con su desempeño, equipo de trabajo, institución y con la función pública. La organización define e implementa programas que apuntan a integrar de manera planificada a las personas, a través de un proceso de acompañamiento y actividades que permitan transmitir a los nuevos funcionarios actitudes, estándares, valores y patrones de conducta prevalecientes que espera la organización para alcanzar mejores estándares de desempeño en el menor tiempo posible (Servicio Civil, 2016).

    Fases_generales_del_proceso:
      Ctx: "Desde la perspectiva de proceso, un programa de inducción debe considerar al menos:"
      Proc:
        - Fase_de_bienvenida:
            Purp: "Orientada a la recepción e integración que contempla actividades de acogida, presentación del equipo, de las instalaciones e interacción con las autoridades."
        - Fase_informativa:
            Purp: "Actividades para entregar información clave sobre la institución respecto a estructura, estrategias y procesos."
        - Fase_orientada_al_cargo:
            Purp: "Actividades para clarificar tareas, responsabilidades, funciones y metas esperadas (Servicio Civil, 2016)."

    Adaptacion_y_flexibilidad_del_proceso_en_la_organizacion:
      Ctx: >-
        El proceso de inducción en el Gobierno Regional de Ñuble se concibe como una instancia flexible y adaptable a contingencias y recursos existentes al momento del ingreso del nuevo funcionario. Existirán actividades que son estándar, pero otras deberán ser adecuadas considerando el desempeño que se espera alcanzar según las funciones que se asumen, la procedencia de la persona (Sector Público o Sector Privado) y el nivel de experiencia en la función pública del nuevo funcionario.

  Seccion_2_Objetivos:
    ID: GN-MANUAL-INDUCCION-S02

    General:
      Obj: >-
        Socializar, orientar, entrenar, alinear y fidelizar al funcionario o funcionaria que ingrese a desempeñar funciones al Gobierno Regional de Ñuble de una manera sistematizada y formal, que contribuya a que éste asimile con rapidez la cultura de la organización, se reduzca el tiempo de adaptación al puesto de trabajo y facilite el proceso de integración a la institución, logrando una adecuada satisfacción laboral y un mejor desempeño para la organización.

    Especificos:
      Obj:
        - "Presentar a la persona que se integra a los miembros de la institución, informando quiénes son sus superiores y compañeros de trabajo."
        - "Entregar información sobre las funciones y responsabilidades en el marco de la estructura y metas organizacionales."
        - "Facilitar el aprendizaje de las metas de la organización, cómo lograrlas, sus tareas y responsabilidades, y los comportamientos de trabajo aceptados y no aceptados."
        - "Apoyar al funcionario en el conocimiento de las políticas y reglas necesarias para el desempeño en el lugar de trabajo."
        - "Facilitar el conocimiento de la cultura organizacional y su adaptación a ésta, familiarizándose con los valores institucionales, la historia organizacional, las prestaciones que ofrece y las características relevantes."
        - "Contemplar los tiempos necesarios que demanda la incorporación de un nuevo funcionario, su adaptación y aprendizaje de los objetivos y funciones del cargo, niveles de exigencia de las tareas, normativas existentes, contexto institucional, integración al equipo de trabajo y adaptación a la cultura organizacional."

  Seccion_3_Alcance_o_Cobertura:
    ID: GN-MANUAL-INDUCCION-S03
    Ctx: "Aplica a todos los nuevos funcionarios y funcionarias que ingresen a desempeñar funciones al Gobierno Regional de Ñuble, independiente de su situación contractual."

  Seccion_4_Marco_Normativo:
    ID: GN-MANUAL-INDUCCION-S04
    Ctx: "El funcionamiento del Gobierno Regional de Ñuble y la labor de sus funcionarios se rigen por un conjunto de normativas fundamentales, entre las que destacan:"
    Src:
      - "Constitución Política de la República de Chile."
      - "Ley N°18.575: Ley Orgánica Constitucional de Bases Generales de la Administración del Estado (texto refundido por DFL N°1/19.653 de 2000)."
      - "Ley N°18.834: Estatuto Administrativo (texto refundido por DFL N°29 de 2004)."
      - "Ley N°19.175: Orgánica Constitucional Sobre Gobierno y Administración Regional (texto refundido por DFL N°1-19.175 de 2005, y sus modificaciones posteriores, especialmente las Leyes N°21.073 y N°21.074)."
      - "Ley N°21.033: Crea la XVI Región de Ñuble y las Provincias de Diguillín, Punilla e Itata."
      - "Ley N°21.074: Fortalecimiento de la Regionalización del País."
      - "Ley N°21.073: Regula la Elección de Gobernadores Regionales y Realiza Adecuaciones a Diversos Cuerpos Legales."
      - "Decreto Ley N°1.263 de 1975: Ley Orgánica de Administración Financiera del Estado."
      - "Ley de Presupuestos del Sector Público para el año 2026 (Ley N°21.796) y sus respectivas glosas aplicables a Gobiernos Regionales."
      - "Ley N°19.628: Sobre Protección de la Vida Privada (modificada significativamente por la Ley N°21.719 sobre Protección de Datos Personales)."
      - "Ley N°19.880: Establece Bases de los Procedimientos Administrativos que Rigen los Actos de la Administración del Estado (modificada por la Ley N°21.180 sobre Transformación Digital)."
      - "Ley N°20.035: Introduce Modificaciones en la Ley N°19.175, Orgánica Constitucional Sobre Gobierno y Administración Regional, en lo Relativo a la Estructura y Funciones de los Gobiernos Regionales."
      - "Ley N°20.285: Sobre Acceso a la Información Pública y su Reglamento (DS N°13/2009 SEGPRES)."
      - "Ley N°20.730: Regula el Lobby y las Gestiones que Representen Intereses Particulares Ante las Autoridades y Funcionarios."
      - "Ley N°20.880: Sobre Probidad en la Función Pública y Prevención de los Conflictos de Intereses."
      - "Ley N°21.180: Sobre Transformación Digital del Estado y sus normas técnicas asociadas (DS N°7, N°8, N°9, N°10, N°11, N°12 de 2023)."
      - "Ley N°21.364: Establece el Sistema Nacional de Prevención y Respuesta ante Desastres (SINAPRED) y sus reglamentos (DS N°234/2022 MININTER)."
      - "Ley N°21.659: Sobre Seguridad Privada."
      - "Ley N°21.719: Modifica la Ley N°19.628, sobre Protección de Datos Personales."
      - "Ley N°21.730: Crea el Ministerio de Seguridad Pública."
      - "Decreto N°2.421 de 1964: Fija el Texto Refundido de la Ley de Organización de la Contraloría General de la República (Ley N°10.336)."
      - "Resolución N°30 de 2015 de la Contraloría General de la República: Fija Normas de Procedimiento sobre Rendición de Cuentas (y sus modificaciones)."
      - "Instructivos y Circulares de la Dirección de Presupuestos (DIPRES) y de la Contraloría General de la República (CGR) aplicables a la gestión presupuestaria y administrativa."
    Req: "Este marco normativo está en constante evolución, por lo que es deber de cada funcionario mantenerse actualizado respecto a las leyes y reglamentos que rigen su actuar."

  Seccion_5_Principios_Orientadores:
    ID: GN-MANUAL-INDUCCION-S05
    Principios:
      - Compromiso:
          Def: "Nos identificamos con la institución, somos parte de ella y somos conscientes de nuestra responsabilidad con la comunidad, por lo que asumimos la función pública con responsabilidad y profesionalismo, brindando un servicio de excelencia a las personas que viven en nuestra Región. Asimismo, la institución reconoce la labor realizada por los(as) funcionarios(as) y les brinda un ambiente laboral con adecuadas condiciones, resguardando su dignidad y derechos y dándoles oportunidades de desarrollo."
      - Eficiencia:
          Def: "Realizamos nuestro trabajo enfocándonos en las personas y en contribuir a mejorar su calidad de vida y satisfacer las necesidades que presentan las comunidades en el territorio de nuestra Región, usando de manera eficiente los recursos públicos disponibles y necesarios para cumplir nuestros objetivos institucionales con excelencia."
      - Profesionalismo:
          Def: "Reconocemos que el ingreso a la Administración, su permanencia en ella y el desarrollo profesional de una carrera funcionaria dependen de nuestras capacidades y del correcto desempeño de nuestro cargo o función, por lo que velamos por la rectitud, probidad, idoneidad, honestidad e irrestricto apego a la normativa en el desempeño de nuestras funciones."
      - Transparencia:
          Def: "Garantizamos y resguardamos el derecho a la ciudadanía de conocer y acceder a toda la información acerca de las actuaciones y decisiones de nuestra institución, posibilitando y facilitando que los ciudadanos conozcan y vigilen la función pública."
      - Probidad:
          Def: "Mantenemos una conducta honesta e íntegra. Esto implica que el interés común prima sobre el particular, de modo que no utilizaremos ni el cargo ni los recursos públicos para obtener beneficios o privilegios personales y seremos imparciales en el ejercicio de nuestras funciones."
      - Respeto:
          Def: "Realizaremos nuestras labores funcionarias en un marco de cordialidad, igualdad, respeto y libertades, dignidad e individualidad de cada persona."
      - Inclusion:
          Def: "No realizaremos discriminación de ningún tipo entre funcionario(a), usuario(a) o beneficiario(a) alguno(a) y reconocemos los mismos derechos y oportunidades, garantizando las condiciones necesarias para practicar este principio. De esta manera pretendemos eliminar cualquier distinción, exclusión o preferencia fundada en razones arbitrarias y/o personales, como el sexo, la orientación sexual, la religión, la raza, la etnia, la nacionalidad, la adherencia política, entre otras."
      - Sostenibilidad:
          Def: "Integramos la dimensión ambiental y la adaptación al cambio climático en nuestras políticas y proyectos, buscando un desarrollo regional que satisfaga las necesidades del presente sin comprometer la capacidad de las futuras generaciones para satisfacer las suyas."
      - Coherencia_y_Coordinacion:
          Def: "Actuamos en armonía con las políticas nacionales y en coordinación con otros órganos del Estado y los gobiernos locales, para optimizar el uso de los recursos y potenciar el impacto de la acción pública en el territorio."

  Seccion_6_Definiciones_Relevantes_Glosario:
    ID: GN-MANUAL-INDUCCION-S06
    Glosario:
      - Termino: "Inducción"
        Def: "Proceso mediante el cual se integra a un nuevo empleado en la organización, proporcionándole la información y herramientas necesarias para que pueda desempeñar su trabajo de manera eficiente y adaptarse a la cultura organizacional."
      - Termino: "Cultura Organizacional"
        Def: "Conjunto de valores, creencias, normas y prácticas compartidas que caracterizan a una organización y guían el comportamiento de sus miembros."
      - Termino: "Política del Servicio o Institución"
        Def: "Conjunto de directrices y normas que rigen las acciones y decisiones dentro de la organización. Incluye políticas de recursos humanos, de seguridad, de conducta, entre otras."
      - Termino: "Procedimiento"
        Def: "Serie de pasos secuenciales y detallados que deben seguirse para completar una tarea específica de manera eficiente y conforme a las normas establecidas."
      - Termino: "Manual de Inducción"
        Def: "Documento que recopila toda la información relevante para la incorporación de nuevos empleados, incluyendo la misión, visión, valores de la empresa, políticas, procedimientos, derechos y responsabilidades del empleado."
      - Termino: "Misión"
        Def: "Propósito fundamental de la organización, lo que busca lograr a largo plazo."
      - Termino: "Visión"
        Def: "Declaración que describe lo que la organización aspira ser o lograr en el futuro."
      - Termino: "Valores"
        Def: "Principios y creencias fundamentales que guían el comportamiento y la toma de decisiones en la organización."
      - Termino: "Descripción de Puesto"
        Def: "Documento que detalla las responsabilidades, deberes y requisitos de un puesto específico dentro de la organización."
      - Termino: "Evaluación de Desempeño"
        Def: "Proceso sistemático para evaluar el rendimiento de los empleados en relación con sus responsabilidades laborales, metas y objetivos."
      - Termino: "Plan de Capacitación"
        Def: "Programa diseñado para mejorar las habilidades y conocimientos de los empleados, permitiéndoles desempeñar sus funciones de manera más efectiva y avanzar en su carrera profesional."
      - Termino: "Derechos del Empleado"
        Def: "Beneficios y protecciones legales que un empleado tiene en su relación laboral, incluyendo salario justo, condiciones de trabajo seguras y no discriminación."
      - Termino: "Responsabilidades del Empleado"
        Def: "Deberes y obligaciones que un empleado tiene hacia su empleador, incluyendo la realización de tareas asignadas, cumplimiento de políticas de la empresa y mantenimiento de la confidencialidad."
      - Termino: "Código de Conducta"
        Def: "Conjunto de normas y principios que regulan el comportamiento de los empleados dentro de la organización, promoviendo un ambiente de trabajo ético y respetuoso."
      - Termino: "Integración"
        Def: "Proceso mediante el cual un nuevo empleado se familiariza y se adapta a su nuevo entorno laboral, colegas y tareas."
      - Termino: "Bienestar Laboral"
        Def: "Estado de satisfacción y salud física y mental de los empleados, influenciado por las condiciones de trabajo, relaciones interpersonales y políticas de la institución."
      - Termino: "Comunicación Interna"
        Def: "Intercambio de información entre los miembros de la organización a través de diversos canales y métodos, con el objetivo de coordinar actividades y mantener a todos informados."
      - Termino: "Feedback"
        Def: "Retroalimentación constructiva sobre el desempeño laboral, que puede ser tanto positiva como negativa, y que busca mejorar la eficacia y satisfacción en el trabajo."
      - Termino: "Mentoría"
        Def: "Relación de apoyo y orientación entre un empleado con experiencia y uno nuevo, destinada a facilitar la adaptación y el desarrollo profesional del nuevo empleado."
      - Termino: "Seguridad y Salud Ocupacional"
        Def: "Conjunto de prácticas y normativas destinadas a garantizar un entorno de trabajo seguro y saludable para todos los empleados."
      - Termino: "Transformación Digital"
        Def: "Proceso de modernización de la gestión pública mediante el uso estratégico de tecnologías digitales, incluyendo la digitalización de procedimientos, el uso de firma electrónica, la interoperabilidad y la gestión de datos."
      - Termino: "Ley N°21.180"
        Def: "Ley sobre Transformación Digital del Estado, que mandata la tramitación electrónica de los procedimientos administrativos."
      - Termino: "Protección de Datos Personales (Ley N°21.719)"
        Def: "Marco normativo que regula el tratamiento de datos personales por parte de organismos públicos y privados, estableciendo principios, derechos y obligaciones."
      - Termino: "Gobernanza de Datos"
        Def: "Conjunto de políticas, roles, responsabilidades y procesos para gestionar los datos como un activo estratégico, asegurando su calidad, seguridad y uso ético."
      - Termino: "Interoperabilidad"
        Def: "Capacidad de los sistemas de información de diferentes organizaciones para intercambiar datos y operar conjuntamente de manera eficiente."
      - Termino: "SIGFE (Sistema de Información para la Gestión Financiera del Estado)"
        Def: "Plataforma oficial para el registro y control de la ejecución presupuestaria del sector público."
      - Termino: "BIP (Banco Integrado de Proyectos)"
        Def: "Sistema donde se registran y evalúan las iniciativas de inversión pública."
      - Termino: "FNDR (Fondo Nacional de Desarrollo Regional)"
        Def: "Principal fuente de financiamiento para la inversión de los Gobiernos Regionales."
      - Termino: "FRPD (Fondo Regional para la Productividad y el Desarrollo)"
        Def: "Fondo destinado a iniciativas de innovación, competitividad, ciencia y tecnología regional."
      - Termino: "Glosas Presupuestarias"
        Def: "Disposiciones específicas en la Ley de Presupuestos que regulan el uso de ciertos fondos o establecen condiciones para su ejecución."
    Res: "Estas definiciones ayudarán a los nuevos empleados a entender mejor los conceptos clave y a adaptarse más rápidamente a la organización."

  Seccion_7_Roles_y_Responsabilidades:
    ID: GN-MANUAL-INDUCCION-S07
    Roles:
      - Rol: "GOBERNADOR REGIONAL"
        Def: "Su rol es brindar el respaldo al Área de Gestión de Personas para que la inducción sea relevada al interior de la organización. Esto incluye la asignación de los recursos humanos, financieros y materiales necesarios para su realización, y su propia participación en aquellas actividades que así lo consignen."
      - Rol: "JEFATURA DIRECTA"
        Def: "Es responsable de garantizar los tiempos y generar las condiciones necesarias para que el nuevo funcionario participe del proceso de inducción. Debe escoger un agente inductor que asegure una adecuada supervisión, seguimiento y orientación del nuevo funcionario. La jefatura directa es la responsable de entregar al nuevo funcionario una descripción clara de las tareas que debe desempeñar, clarificar sus funciones y contextualizar con la estrategia institucional, suministrando toda la información técnica acerca de cómo realizarlas, y será la responsable de retroalimentar al inducido al final del proceso."
      - Rol: "ÁREA DE GESTIÓN DE PERSONAS"
        Def: "Responsable del proceso general de inducción. Debe coordinar y monitorear el proceso de inducción y sus actividades. Asimismo, debe controlar la efectiva participación de las personas e introducir los ajustes que determinadas coyunturas pueden demandar. Adicionalmente, debe coordinar una evaluación periódica del proceso de inducción institucional y realizar las acciones de inducción específica que le correspondan en cada caso. Entre las acciones específicas está informar cuáles son las políticas de la organización en gestión de personas, deberes y derechos que le corresponden como funcionario, y familiarizarse con la estructura de la organización (áreas, unidades, infraestructura, entre otros)."
      - Rol: "AGENTE INDUCTOR, MENTOR O TUTOR"
        Def: "Par de la persona inducida o un miembro de la organización reconocido por ser confiable y experimentado, que pueda responder preguntas sobre la organización y mantenerse cerca durante el periodo inicial. Su rol fundamental es facilitar la interrelación de la persona con su equipo de trabajo directo y con las otras áreas."

  Seccion_8_Aspectos_Generales_Organizacion_Administracion_Publica:
    ID: GN-MANUAL-INDUCCION-S08
    Ctx: "La organización de la administración pública en Chile se estructura de manera que permite una gestión eficiente y ordenada del Estado, asegurando el cumplimiento de sus funciones y la prestación de servicios a los ciudadanos. A continuación, se describen los aspectos generales de esta organización:"

    Division_de_Poderes:
      Ctx: "La administración pública se organiza bajo el principio de la separación de poderes, dividiéndose en tres poderes principales:"
      Poderes:
        - "Poder Ejecutivo: Encabezado por el Presidente de la República, quien es responsable de la administración general del país."
        - "Poder Legislativo: Compuesto por el Congreso Nacional, que incluye la Cámara de Diputados y el Senado. Su función es la creación de leyes y la fiscalización de las actividades del Ejecutivo."
        - "Poder Judicial: Encargado de la administración de justicia, independiente del Ejecutivo y Legislativo."

    Presidencia_de_la_Republica:
      Ctx: "El Presidente de la República es la máxima autoridad del Poder Ejecutivo y tiene la facultad de nombrar ministros, subsecretarios y jefes de servicios públicos. Además, es responsable de la administración del Estado y la conducción de la política gubernamental."

    Ministerios:
      Ctx:
        - "Cada ministerio está encabezado por un ministro y se encarga de áreas específicas de la política pública. Los ministerios pueden tener una o más subsecretarías y en regiones son representados por sus respectivos secretarios regionales ministeriales (SEREMIs)."
        - "Con la creación del Ministerio de Seguridad Pública (Ley N°21.730), esta cartera asume las funciones específicas de seguridad ciudadana y orden público, antes radicadas principalmente en el Ministerio del Interior."
      Items:
        - "Ministerio del Interior"
        - "Ministerio de Seguridad Pública."
        - "Ministerio de Relaciones Exteriores."
        - "Ministerio de Defensa Nacional."
        - "Ministerio de Hacienda."
        - "Ministerio de Economía, Fomento y Turismo."
        - "Ministerio de Desarrollo Social y Familia."
        - "Ministerio Secretaría General de la Presidencia."
        - "Ministerio Secretaría General de Gobierno."
        - "Ministerio de Educación."
        - "Ministerio de Justicia y Derechos Humanos."
        - "Ministerio de Trabajo y Previsión Social."
        - "Ministerio de Obras Públicas."
        - "Ministerio de Salud."
        - "Ministerio de Vivienda y Urbanismo."
        - "Ministerio de Agricultura."
        - "Ministerio de Minería."
        - "Ministerio de Transporte y Telecomunicaciones."
        - "Ministerio de Bienes Nacionales."
        - "Ministerio de Energía."
        - "Ministerio del Medio Ambiente."
        - "Ministerio del Deporte."
        - "Ministerio de las Culturas, las Artes y el Patrimonio."
        - "Ministerio de Ciencia, Tecnología, Conocimiento e Innovación."
        - "Ministerio de la Mujer y la Equidad de Género."

    Subsecretarias:
      Ctx: "Son órganos dependientes de los ministerios, encargados de áreas específicas dentro de la competencia del ministerio. Las subsecretarías tienen funciones de planificación, coordinación y supervisión de políticas públicas. La Subsecretaría de Desarrollo Regional y Administrativo (SUBDERE), dependiente del Ministerio del Interior, juega un rol clave en la coordinación y apoyo a los Gobiernos Regionales."

    Servicios_Publicos_Descentralizados_y_Desconcentrados:
      Items:
        - "Descentralizados: Organismos con personalidad jurídica y patrimonio propio que ejecutan políticas específicas y prestan servicios directos a la ciudadanía (Ej. Servicio de Impuestos Internos - SII, Instituto Nacional de Estadísticas - INE, Superintendencias). Los Gobiernos Regionales son entidades descentralizadas."
        - "Desconcentrados: Unidades de ministerios o servicios nacionales que operan a nivel regional o provincial para acercar la gestión a los territorios (Ej. Direcciones Regionales de SERVIU, SAG, CONAF; Secretarías Regionales Ministeriales - SEREMI)."

    Gobiernos_Regionales_y_Locales:
      Items:
        - "Gobiernos Regionales (GORE): Encargados de la administración superior de la región, con foco en el desarrollo social, cultural y económico. Están constituidos por un Gobernador Regional (electo) y un Consejo Regional (electo). (Ley N°19.175 y sus modificaciones)."
        - "Gobiernos Locales (Municipalidades): Encabezados por alcaldes y concejos municipales (electos), responsables de la administración local y la prestación de servicios municipales."

    Organos_Autonomos:
      Ctx: "Existen varios órganos autónomos que operan independientemente del Poder Ejecutivo para garantizar la imparcialidad y el control en diferentes áreas:"
      Items:
        - "Contraloría General de la República: Supervisa la legalidad de los actos de la administración pública y el correcto uso de los fondos públicos."
        - "Banco Central de Chile: Encargado de la política monetaria y financiera."
        - "Tribunal Constitucional: Vigila la constitucionalidad de las leyes."
        - "Ministerio Público (Fiscalía): Investiga y persigue delitos."
        - "Servicio Electoral (SERVEL): Organiza y fiscaliza los procesos eleccionarios."
        - "Agencia de Protección de Datos Personales (creada por Ley N°21.719)."
        - "Agencia Nacional de Ciberseguridad (ANCI) (creada por Ley N°21.663)."
      Res: "Estos aspectos generales describen cómo se estructura y funciona la administración pública en Chile, asegurando que el Estado pueda cumplir sus responsabilidades de manera eficiente y efectiva."

  Seccion_9_Gobiernos_Regionales:
    ID: GN-MANUAL-INDUCCION-S09

    Descentralizacion_y_Desconcentracion:
      Ctx:
        - "La Constitución Política de la República señala en su artículo 3° que:"
        - "\"El Estado de Chile es unitario\"."
        - "\"La administración del Estado será funcional y territorialmente descentralizada, o desconcentrada en su caso, de conformidad a la ley\"."
        - "\"Los órganos del Estado promoverán el fortalecimiento de la regionalización del país y el desarrollo equitativo y solidario entre las regiones, provincias y comunas del territorio nacional\"."
        - "Esto relaciona los conceptos de descentralización y desconcentración con la capacidad de accionar de los órganos del Estado que describe el citado artículo. (Servicio Civil, 2017)"
        - >-
          Mientras que la descentralización es la transferencia de parte del poder y recursos del Estado Central a las instancias del nivel regional o local, en donde la toma de decisiones se radica en el nivel regional o local, respondiendo y dando cuenta ante ese mismo nivel; la desconcentración consiste en transferir algunas funciones administrativas y/o técnicas a niveles más bajos de administración, pero manteniendo el poder de decisión a nivel central. Es decir, aunque el decisor se radique en el nivel regional o local, sigue respondiendo ante el nivel central por el resultado de sus decisiones (Servicio Civil, 2017).
        - "La Ley N°21.074 de Fortalecimiento de la Regionalización estableció mecanismos para la transferencia de competencias desde ministerios y servicios públicos nacionales hacia los GORE, profundizando el proceso de descentralización funcional."

    Funciones_Atribuciones_y_Competencias:
      Ctx: "La Ley Orgánica Constitucional sobre Gobierno y Administración Regional (LOCGAR, DFL N°1-19.175 y sus modificaciones) establece la estructura de los Gobiernos Regionales, sus funciones, atribuciones y competencias. Como principales funciones de estos se distinguen:"
      Items:
        - "La elaboración y aprobación de las políticas, planes y programas de desarrollo de la región, así como su proyecto de presupuesto, ajustados a la Política Nacional de Desarrollo y al Presupuesto de la Nación."
        - "Resolver la inversión de los recursos que a la región correspondan en la distribución del Fondo Nacional de Desarrollo Regional (FNDR) y de aquellos que procedan de acuerdo con la normativa aplicable."
        - "Dictar normas de carácter general para regular las materias de su competencia, con sujeción a las disposiciones legales y a los decretos supremos reglamentarios, todas las cuales están sujetas al trámite de toma de razón por parte de la Contraloría General de la República y se publicarán en el Diario Oficial."

    Funciones_Generales_Art_16_Ley_19175:
      Ctx: "FUNCIONES GENERALES DE LOS GOBIERNOS REGIONALES (Art. 16, Ley N°19.175)"
      Items:
        - Item: "a)"
          Def: "Diseñar, elaborar, aprobar y aplicar las políticas, planes, programas y proyectos de desarrollo de la región en el ámbito de sus competencias, ajustándose al presupuesto de la Nación; a la estrategia regional de desarrollo y a los instrumentos de planificación comunal. El Gobierno Regional podrá convocar a los directores regionales de los servicios públicos que dependan o se relacionen con el Presidente de la República o a los secretarios regionales ministeriales para abordar la contribución sectorial en el cumplimiento de los planes, programas y proyectos de desarrollo de la región, según corresponda."
        - Item: "b)"
          Def: "Efectuar estudios, análisis y proposiciones relativos al desarrollo regional."
        - Item: "c)"
          Def: "Orientar el desarrollo territorial de la región en coordinación con los servicios públicos y municipalidades localizados en ella."
        - Item: "d)"
          Def: "Elaborar y aprobar su proyecto de presupuesto, ajustándose a las orientaciones que se emitan para la formulación del proyecto de Ley de Presupuestos del Sector Público."
        - Item: "e)"
          Def: "Administrar fondos y programas de aplicación regional."
        - Item: "f)"
          Def: "Resolver la inversión de los recursos que a la región correspondan en la distribución del Fondo Nacional de Desarrollo Regional (FNDR) y de aquellos que procedan de acuerdo al artículo 74 de esta ley, en conformidad con la normativa aplicable."
        - Item: "g)"
          Def: "Decidir la destinación a proyectos específicos de los recursos de los programas de inversión sectorial de asignación regional, que contemple anualmente la Ley de Presupuestos de la Nación."
        - Item: "h)"
          Def: "Dictar normas de carácter general para regular las materias de su competencia, con sujeción a las disposiciones legales y a los decretos supremos reglamentarios."
        - Item: "i)"
          Def: "Diseñar, aprobar, ejecutar y aplicar políticas, planes, programas y proyectos regionales en materia de prevención social, situacional y comunitaria del delito, así como en materias de atención y asistencia a víctimas, en coordinación con los organismos públicos competentes y el ministerio encargado de la seguridad pública (incorporado por Ley N°21.730)."
        - Item: "j)"
          Def: "Asesorar a las municipalidades, cuando éstas lo soliciten, especialmente en la formulación de sus planes y programas de desarrollo, así como en la formulación e implementación de sus planes comunales de seguridad pública."
        - Item: "k)"
          Def: "Adoptar las medidas necesarias para enfrentar situaciones de emergencia o catástrofe (SINAPRED, Ley N°21.364), y desarrollar programas de prevención y protección ante situaciones de desastre."
        - Item: "l)"
          Def: "Participar en acciones de cooperación internacional en la región."
        - Item: "m)"
          Def: "Ejercer las competencias que le sean transferidas."
        - Item: "n)"
          Def: "Mantener relación permanente con el gobierno nacional y sus distintos organismos."
        - Item: "ñ)"
          Def: "Construir, reponer, conservar y administrar obras de pavimentación de aceras y calzadas."
        - Item: "o)"
          Def: "Elaborar y aprobar los planes de inversiones en infraestructura de movilidad y espacio público asociados a planes reguladores metropolitanos o intercomunales."
        - Item: "p)"
          Def: "Coparticipar con el Comité Regional para el cambio climático en la elaboración y aprobación de los instrumentos para la gestión del cambio climático a nivel regional."

    Funciones_Ordenamiento_Territorial_Art_17:
      Ctx: "Principales funciones del Gobierno Regional en materia de Ordenamiento Territorial (Art. 17)"
      Items:
        - Item: "a)"
          Def: "Elaborar y aprobar el plan regional de ordenamiento territorial (PROT)."
        - Item: "b)"
          Def: "Establecer políticas y objetivos para el desarrollo integral y armónico del sistema de asentamientos humanos de la región."
        - Item: "c)"
          Def: "Participar en programas y proyectos de dotación y mantenimiento de obras de infraestructura y de equipamiento en la región."
        - Item: "d)"
          Def: "Fomentar y velar por la protección, conservación y mejoramiento del medio ambiente."
        - Item: "e)"
          Def: "Fomentar y velar por el buen funcionamiento de la prestación de los servicios en materia de transporte intercomunal, interprovincial e internacional fronterizo en la región."
        - Item: "f)"
          Def: "Fomentar y propender al desarrollo de áreas rurales y localidades aisladas en la región."
        - Item: "g)"
          Def: "Proponer a la autoridad competente la localidad en que deberán radicarse las secretarías regionales ministeriales y las direcciones regionales de los servicios públicos."
        - Item: "h)"
          Def: "Financiar estudios que definan las condiciones de localización para la disposición de los distintos tipos de residuos."
        - Item: "i)"
          Def: "Proponer territorios como zonas rezagadas en materia social y su respectivo plan de desarrollo."

    Funciones_Fomento_Actividades_Productivas_Art_18:
      Ctx: "Principales funciones del Gobierno Regional en materia de fomento de las actividades productivas (Art. 18)"
      Items:
        - Item: "a)"
          Def: "Formular políticas regionales de fomento de las actividades productivas, apoyo al emprendimiento, innovación, capacitación laboral, ciencia y tecnología."
        - Item: "b)"
          Def: "Establecer las prioridades estratégicas regionales en materia de fomento productivo e innovación para la competitividad."
        - Item: "c)"
          Def: "Aprobar el plan regional de desarrollo turístico (PLADETUR)."
        - Item: "d)"
          Def: "Promover y diseñar programas y proyectos de fomento productivo."
        - Item: "e)"
          Def: "Promover y apoyar oficinas comunales de fomento productivo."
        - Item: "f)"
          Def: "Promover la investigación científica y tecnológica y el desarrollo de la educación superior y técnico profesional."
        - Item: "g)"
          Def: "Elaborar y aprobar la Política Regional de Ciencia, Tecnología, Conocimiento e Innovación para el Desarrollo."

    Funciones_Desarrollo_Social_y_Cultural_Art_19:
      Ctx: "Principales funciones del Gobierno Regional en materia de desarrollo social y cultural (Art. 19)"
      Items:
        - Item: "a)"
          Def: "Establecer prioridades regionales para la erradicación de la pobreza."
        - Item: "b)"
          Def: "Participar en acciones para facilitar el acceso de la población de escasos recursos a salud, educación, cultura, vivienda, seguridad social, deportes, recreación y asistencia judicial."
        - Item: "c)"
          Def: "Proponer programas y proyectos con énfasis en grupos vulnerables."
        - Item: "d)"
          Def: "Distribuir recursos para financiamiento de beneficios y programas sociales administrados por municipalidades."
        - Item: "e)"
          Def: "Realizar estudios sobre condiciones, nivel y calidad de vida de los habitantes."
        - Item: "f)"
          Def: "Fomentar expresiones culturales, cautelar el patrimonio, y velar por la protección y desarrollo de etnias originarias."
        - Item: "g)"
          Def: "Proponer programas y proyectos que fomenten la formación deportiva y la práctica del deporte."
        - Item: "h)"
          Def: "Mantener información actualizada sobre la situación socioeconómica regional."

    Atribuciones_Art_20:
      Ctx: "ATRIBUCIONES DE LOS GOBIERNOS REGIONALES (Art. 20)"
      Items:
        - Item: "a)"
          Def: "Aprobar y modificar normas reglamentarias regionales."
        - Item: "b)"
          Def: "Adquirir, administrar y disponer de sus bienes y recursos."
        - Item: "c)"
          Def: "Convenir programas anuales o plurianuales de inversiones con impacto regional."
        - Item: "d)"
          Def: "Disponer, supervisar y fiscalizar iniciativas con cargo a su presupuesto."
        - Item: "e)"
          Def: "Aplicar políticas definidas en la estrategia regional de desarrollo."
        - Item: "f)"
          Def: "Aprobar planes regionales de ordenamiento territorial, planes reguladores metropolitanos, intercomunales, comunales, seccionales y planes de inversiones en infraestructura de movilidad y espacio público."
        - Item: "g)"
          Def: "Formular y priorizar proyectos de infraestructura social básica y evaluar programas."
        - Item: "h)"
          Def: "Proponer criterios para la distribución de subvenciones a programas sociales."
        - Item: "i)"
          Def: "Aplicar tributos regionales para financiar obras de desarrollo regional (según ley)."
        - Item: "j)"
          Def: "Aprobar banderas, escudos e himnos regionales."
        - Item: "k)"
          Def: "Diseñar, elaborar, aprobar y ejecutar políticas, planes, programas y proyectos dentro de su territorio."
        - Item: "l)"
          Def: "Ejercer demás atribuciones necesarias para el ejercicio de sus funciones."
        - Item: "m)"
          Def: "Coparticipar con el Comité Regional para el cambio climático en la elaboración y aprobación de los instrumentos para la gestión del cambio climático a nivel regional."

    Marco_Juridico_Regulatorio:
      Ctx: "Se reitera el marco normativo general presentado en la Sección 4, enfatizando la Ley N°19.175 y sus modificaciones como el cuerpo legal central para los GORE, junto con las leyes de presupuesto anuales y normativas específicas sobre probidad, transparencia, lobby, transformación digital, protección de datos, y las referidas a nuevas competencias como seguridad y gestión de desastres."

  Seccion_10_Gobierno_Regional_de_Nuble:
    ID: GN-MANUAL-INDUCCION-S10
    Ctx: >-
      El Gobierno Regional de Ñuble se estableció el 6 de septiembre de 2018, tras la creación de la Región de Ñuble, la cual se separó de la Región del Biobío. Este cambio significativo en la división política-administrativa de Chile fue el resultado de un largo proceso de descentralización y regionalización del país. El Gobierno Regional de Ñuble tiene como objetivo principal promover el desarrollo económico, social y cultural de la región, así como gestionar de manera eficiente los recursos públicos para satisfacer las necesidades de la población local. Desde su creación, ha trabajado en estrecha colaboración con los municipios de la región y la comunidad para impulsar el progreso y el bienestar de las 21 comunas que componen la Región de Ñuble.

    Mision_y_Vision_Actualizado_2025_2026:
      Mssn: "Liderar e impulsar el desarrollo sustentable de la Región de Ñuble, mediante la gestión eficiente de la inversión pública, la responsabilidad presupuestaria, y la coordinación entre la institucionalidad pública y privada para contribuir al desarrollo territorial armónico, de cordillera a mar."
      Vision:
        Def: "Que Ñuble sea un territorio reconocido por su calidad de vida, su aporte cultural y su fortalecimiento del capital humano, con una matriz productiva diversificada y una mejora especial en la calidad de vida de adultos mayores y población rural."
        Ctx: "Contexto ERD 2024-2030"

    Objetivos_Estrategicos_Institucionales_2025_2026:
      Table:
        Columns: [Prioridad, Tipo_de_Objetivo, Descripcion, Enfoque_de_Genero, Cambio_Climatico]
        Rows:
          - Prioridad: "1"
            Tipo_de_Objetivo: "Estratégico"
            Descripcion: "Desarrollar estrategias, políticas e instrumentos con enfoque de género para la Planificación Regional, la gestión de la Información territorial regional, y la gestión de los distintos actores del territorio, contribuyendo al desarrollo regional participativo y territorialmente integrado."
            Enfoque_de_Genero: "Sí"
            Cambio_Climatico: "Sí"
          - Prioridad: "2"
            Tipo_de_Objetivo: "Estratégico"
            Descripcion: "Financiar una cartera anual de iniciativas de Inversión Pública Regional en las áreas de fomento productivo e innovación, que considere la perspectiva de género, y sea desarrollada en conjunto con los actores estratégicos público-privado del territorio, contribuyendo a mejorar las condiciones económicas y sociales de la región."
            Enfoque_de_Genero: "Sí"
            Cambio_Climatico: "Sí"
          - Prioridad: "3"
            Tipo_de_Objetivo: "Estratégico"
            Descripcion: "Implementar instancias de participación, actualización, fortalecimiento de capacidades y articulación de los actores estratégicos público-privado del territorio y con perspectiva de género, en materia de formulación, evaluación y/o ejecución de iniciativas de inversión regional con financiamiento público del Fondo Regional de Desarrollo Regional, contribuyendo a una gestión eficaz, eficiente y oportuna del FNDR."
            Enfoque_de_Genero: "Sí"
            Cambio_Climatico: "No"

    Alineacion_con_ERD_Nuble_2024_2030:
      Ctx: "Estos objetivos se alinean con los ejes de la Estrategia Regional de Desarrollo Ñuble 2024-2030, que son:"
      Items:
        - "Territorio y Medio Ambiente."
        - "Economía, Innovación y Capital Humano."
        - "Desarrollo Social Inclusivo."
        - "Patrimonio, Cultura e Identidad."
        - "Institucionalidad y Gobernanza Regional."

    Bienes_y_Servicios_que_Entrega_el_Gobierno_Regional_de_Nuble:
      Items:
        - "Políticas, planes, programas y proyectos de alcance regional: PROT, ERD, Política Regional de CTiD, ARI, PROPIR, entre otros."
        - "Financiamiento de Iniciativas de Inversión y Gasto público regional."
        - "Financiamiento de proyectos de infraestructura, equipamiento y gestión de alcance regional."
        - "Financiamiento de Proyectos a organizaciones y entidades públicas y privadas."
        - "Financiamiento de subvenciones en áreas de cultura, deporte, seguridad, género, social, medio ambiente, etc. (Ej. Concurso 8% FNDR)."
        - "Financiamiento de proyectos de conservación, activos no financieros, FRIL, entre otros."
        - "Financiamiento del Fondo Regional para la Productividad y el Desarrollo (FRPD)."
        - "Coordinación y articulación de actores públicos y privados para el desarrollo regional."
        - "Asesoría y asistencia técnica a municipalidades en materias de competencia regional."
        - "Promoción de la participación ciudadana en la gestión regional."
      Src: "(Ejemplos concretos de la gestión 2023 incluyen: Mejoras en salud (CESFAM, hospitales), Agua Potable Rural, Espacios Públicos, Maquinaria municipal, programas de apoyo a PYMES, seguridad (infraestructura policial, prevención), apoyo a la agricultura y riego, proyectos de innovación, programas para zonas de rezago, y respuesta a emergencias. Fuente: Cuenta Pública GORE Ñuble 2023)."

    Estructura_Organizacional_del_Gobierno_Regional_de_Nuble:
      Ctx: "La estructura organizacional del Gobierno Regional de Ñuble fue aprobada por el Consejo Regional, según Certificado CORE 579 del 22 de diciembre de 2022, y posteriormente por Resolución Exenta N° 00056 del 16 de enero de 2023. Esta consta de acuerdo al DFL 1-19175, como base de:"
      Items:
        - "Un Gobernador/a Regional."
        - "Un Consejo Regional."
        - "Un Administrador/a Regional."
        - "Una Unidad de Control."
        - "Seis Divisiones:"
      Divisiones_Base:
        - "División de Planificación y Desarrollo Regional."
        - "División de Presupuesto e Inversión Regional."
        - "División de Administración y Finanzas."
        - "División de Desarrollo Social y Humano."
        - "División de Infraestructura y Transportes."
        - "División de Fomento e Industria."
      Ctx_Optional:
        - "Adicionalmente, la Ley N°19.175 (Art. 68) permite al Gobernador Regional, con acuerdo del CORE, crear una División de Prevención del Delito, encargada de las tareas de coordinación y gestión de las funciones del GORE en materia de seguridad y prevención."
        - "Además, se conjugan una serie de otros departamentos y unidades, dependientes de las primeras, que apoyan y complementan la gestión tanto administrativa como financiera de la organización."

    Organigrama_en_detalle:
      Ctx: "(El organigrama detallado presentado en el manual 2024 sigue vigente en sus líneas generales. Se debe consultar la última resolución oficial del GORE Ñuble para cualquier actualización específica de departamentos o unidades internas)."

      Nivel_Superior:
        - Gobernador_Region_de_Nuble:
            Items:
              - "Comunicaciones"
              - "Gabinete Gobernador"
              - "Centro Integral de Emergencia y Seguridad (CIES)"
              - "Administradora Regional"
              - "Corporación Regional de Desarrollo de Ñuble (u otras entidades asociativas)"
              - "Asesoría Jurídica"
        - Consejo_Region_de_Nuble:
            Items:
              - "Secretaría Ejecutiva CORE"
              - "Unidad de Control"

      Nivel_de_Asesoria:
        Items:
          - "Comité de Ciencia, Tecnología, Conocimiento e Innovación para el Desarrollo (CCTID)"
          - "Consejo de la Sociedad Civil (COSOC)"
          - "Auditoría (puede ser parte de Unidad de Control o externa según necesidad)"
          - "Unidad de Calidad y Gestión Institucional"
          - "Oficina de Partes (y Archivo)"

      Divisiones:
        - Jefe_Division_de_Planificacion_y_Desarrollo_Regional_DIPLADE:
            Items:
              - "Comité Pertinencia y Vinculación Estratégica"
              - "Departamento de Planificación Estratégica y Ordenamiento Territorial"
              - "Departamento de Desarrollo de Proyectos Estratégicos"
              - "Departamento de Desarrollo Urbano (y/o Área Metropolitana, si aplica)"
              - "Departamento de Puesta en Valor del Patrimonio"
        - Jefe_Division_de_Presupuesto_e_Inversion_Regional_DIPIR:
            Items:
              - "Departamento de Análisis y Evaluación de Inversiones (SNI)"
              - "Departamento de Presupuesto Regional"
              - "Departamento de Gestión de Inversiones y Convenios"
        - Jefe_Division_de_Desarrollo_Social_y_Humano:
            Departamentos:
              - Departamento_Fondos_Concursables_y_Programas_Sociales:
                  Items:
                    - "Unidad Subvenciones (Ej. 8% FNDR)"
                    - "Unidad Programas Sociales Regionales"
              - Departamento_Analisis_y_Gestion_Territorial:
                  Items:
                    - "Unidad Participación Ciudadana"
                    - "Unidad Territorial Provincial (si aplica)"
                    - "Unidad de Seguimiento de Políticas, Planes y Programas Sociales"
        - Jefe_Division_de_Fomento_e_Industria:
            Items:
              - "Departamento Zonas en Desarrollo (Territorios Rezagados, Zonas Extremas)"
              - "Departamento Desarrollo Económico Local y PYMES"
              - "Departamento Ciencia, Tecnología e Innovación para la Competitividad (gestión FRPD)"
              - "Departamento de Desarrollo Empresarial y Atracción de Inversiones"
              - "Departamento de Riego y Medio Ambiente (o unidad específica de Medio Ambiente y Cambio Climático)"
        - Jefe_Division_de_Infraestructura_y_Transporte:
            Departamentos:
              - Departamento_de_Infraestructura_y_Equipamiento_Regional:
                  Items:
                    - "Unidad Saneamiento Básico (APR, alcantarillado)"
              - Departamento_Gestion_en_Transporte_y_Telecomunicaciones:
                  Items:
                    - "Unidad Conectividad (digital y física)"
        - Jefe_Division_de_Administracion_y_Finanzas_DAF:
            Departamentos:
              - Departamento_de_Gestion_y_Desarrollo_de_Personas:
                  Items:
                    - "Unidad Gestión de Personas"
                    - "Unidad Desarrollo de Personas (Capacitación)"
              - Departamento_de_Finanzas_y_Contabilidad
              - Unidad_de_Gestion_Operativa_Interna:
                  Items:
                    - "Servicios Generales, Adquisiciones"
              - Unidad_de_Abastecimiento
              - Unidad_de_Tecnologias_de_la_Informacion_y_Comunicaciones_TIC_y_Transformacion_Digital
        - Opcional_Jefe_Division_de_Prevencion_del_Delito:
            Ctx: "Departamentos o unidades según las necesidades de la estrategia regional de prevención."

    Funciones_de_las_Unidades_Base_Segun_DFL_1_19175:
      Items:
        - Unidad: "Gobernador Regional"
          Def: "Órgano ejecutivo del gobierno regional, preside el consejo regional. Ejerce funciones con arreglo a la Constitución y leyes. (Revisar en profundidad Art. 24 de la Ley N°19.175 para detalle de funciones)."
        - Unidad: "Consejo Regional (CORE)"
          Def: "Órgano normativo, resolutivo y fiscalizador, que busca hacer efectiva la participación de la comunidad regional. Integrado por consejeros elegidos por sufragio universal. (Revisar en profundidad Art. 36 de la Ley N°19.175 para detalle de funciones)."
        - Unidad: "Administrador/a Regional"
          Def: "Colaborador directo del gobernador regional, encargado de la gestión administrativa del gobierno regional y la coordinación de los jefes de división."
        - Unidad: "Unidad de Control"
          Def: "Responsable de la auditoría operativa interna, fiscalización de legalidad y control de ejecución financiera y presupuestaria. Colabora con el CORE en su función fiscalizadora. Emite informes trimestrales y representa actos ilegales al Gobernador."
        - Unidad: "DIVISIÓN DE PLANIFICACIÓN Y DESARROLLO REGIONAL (DIPLADE)"
          Def: "Elabora y propone estrategias, políticas, planes (incluido PROT), programas y proyectos para el desarrollo armónico del territorio, conforme a prioridades del GORE. Apoya al gobernador en evaluación y presta asistencia técnica."
        - Unidad: "DIVISIÓN DE PRESUPUESTO E INVERSIÓN REGIONAL (DIPIR)"
          Def: "Elabora proyectos de presupuesto de inversión, ejecuta y controla dicho presupuesto y programas, asesorando al gobernador en proyectos de inversión según planificación regional."
        - Unidad: "DIVISIÓN DE ADMINISTRACIÓN Y FINANZAS (DAF)"
          Def: "Gestión administrativa interna y provisión de servicios generales del GORE."
        - Unidad: "DIVISIÓN DE FOMENTO E INDUSTRIA"
          Def: "Propone, promueve y ejecuta planes y programas regionales para estimular ciencia, tecnología, conocimiento, innovación, desarrollo empresarial y competitividad, facilitando la incorporación de TICs y proponiendo instrumentos de fomento."
        - Unidad: "DIVISIÓN DE INFRAESTRUCTURA Y TRANSPORTES"
          Def: "Propone, promueve y ejecuta planes y programas regionales en materia de obras de infraestructura, equipamiento regional y gestión de transporte."
        - Unidad: "DIVISIÓN DE DESARROLLO SOCIAL Y HUMANO"
          Def: "Propone, promueve y ejecuta planes y programas regionales conducentes a la igualdad de derechos, oportunidades y cohesión social."
        - Unidad: "DIVISIÓN DE PREVENCIÓN DEL DELITO (si se crea)"
          Def: "Encargada de tareas de coordinación y gestión de funciones del GORE en materia de prevención del delito y atención a víctimas, en coordinación con la institucionalidad de seguridad pública."
      Req: "Las divisiones de Fomento e Industria, Infraestructura y Transportes, y Desarrollo Social y Humano (y Prevención del Delito, si existe) deben coordinar el accionar de los servicios públicos regionales que dependan o se relacionen con el gobierno regional."

  Seccion_11_Derechos_y_Deberes_Funcionarios:
    ID: GN-MANUAL-INDUCCION-S11

    Requisitos_de_Ingreso:
      Ctx: "Requisitos Generales: Los postulantes deberán cumplir con los siguientes requisitos generales señalados en el Artículo 12 del Estatuto Administrativo, el cual señala que para ingresar a la Administración del Estado será necesario:"
      Req:
        - Item: "a)"
          Def: "Ser ciudadano."
        - Item: "b)"
          Def: "Haber cumplido con la ley de reclutamiento y movilización, cuando fuere procedente."
        - Item: "c)"
          Def: "Tener salud compatible con el desempeño del cargo."
        - Item: "d)"
          Def: "Haber aprobado la educación básica y poseer el nivel educacional o título profesional o técnico que por la naturaleza del empleo exija la ley."
        - Item: "e)"
          Def: "No haber cesado en un cargo público como consecuencia de haber obtenido una calificación deficiente, o por medida disciplinaria, salvo que hayan transcurrido más de cinco años desde la fecha de expiración de funciones."
        - Item: "f)"
          Def: "No estar inhabilitado para el ejercicio de funciones o cargos públicos, ni hallarse condenado por crimen o simple delito."

    Prohibiciones_Inhabilidades_e_Incompatibilidades_Funcionarias:
      Ctx: "Sin perjuicio de lo anterior, los postulantes no deberán estar afectados a las inhabilidades e incompatibilidades contenidas en los artículos 54 y 56 del DFL N° 1/19653 de 2000 del Ministerio Secretaría General de la Presidencia, que fija el texto refundido, coordinado y sistematizado de la Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado. Estas inhabilidades e incompatibilidades son:"
      Prohib:
        - Item: "a)"
          Def: "Tener vigentes o suscribir, por sí o por terceros, contratos o cauciones ascendientes a 200 UTM o más, con el Servicio."
        - Item: "b)"
          Def: "Tener litigios pendientes con el Servicio, a menos que se refieran al ejercicio de derechos propios, de su cónyuge, hijos, adoptados o parientes hasta el tercer grado de consanguinidad y segundo de afinidad inclusive."
        - Item: "c)"
          Def: "Ser director, administrador, representante o socio titular del 10% o más de los derechos de cualquier clase de sociedad, cuando ésta tenga contratos o cauciones vigentes ascendientes a 200 UTM o más, o litigios pendientes con el Servicio."
        - Item: "d)"
          Def: "Ser cónyuge, hijo, adoptado o pariente hasta el tercer grado de consanguinidad o segundo por afinidad inclusive de las autoridades y de los funcionarios directivos del Servicio hasta el nivel de Jefe de Departamento inclusive."
        - Item: "e)"
          Def: "Desarrollar actividades particulares en los mismos horarios de labores dentro del Servicio, o que interfieran con su desempeño funcionario, salvo actividades de tipo docente, con un máximo de 12 horas semanales."

    Derechos_Funcionarios:
      Res:
        - Item: "1."
          Def: "Hacer uso de los feriados, permisos, licencias y participar en las acciones de capacitación."
        - Item: "2."
          Def: "Gozar de todas las prestaciones y beneficios que contemplen los sistemas de previsión y bienestar social."
        - Item: "3."
          Def: "Ser defendidos y exigir que la institución a que pertenezcan persiga la responsabilidad civil y criminal de las personas que atenten contra su vida o su integridad corporal, con motivo del desempeño de sus funciones, o que, por dicho motivo, los injurien o calumnien en cualquier forma."
        - Item: "4."
          Def: "Percibir por sus servicios las remuneraciones y demás asignaciones adicionales."
        - Item: "5."
          Def: "Percibir las siguientes asignaciones:"
          Items:
            - "Horas extraordinarias."
            - "Viático, pasajes u otros análogos."
        - Item: "6."
          Def: "Derecho a afiliarse a los Servicios de Bienestar (Depende si está creado)."
        - Item: "7."
          Def: "Derecho a Asignaciones Familiares."
        - Item: "8."
          Def: "Derecho a formar y a afiliarse a Asociaciones de funcionarios."
        - Item: "9."
          Def: "Gozar de estabilidad en el empleo."
        - Item: "10."
          Def: "Ascender en el respectivo escalafón."
        - Item: "11."
          Def: "Participar en concursos."
        - Item: "12."
          Def: "Recibir asistencia en caso de accidente de trabajo o enfermedad profesional."
        - Item: "13."
          Def: "Todos los funcionarios de planta o contrata que sufran un accidente de trabajo o un accidente de trayecto tienen el derecho a atenderse en los Servicios Médicos de la Mutual de Seguridad de la Cámara Chilena de la Construcción."

    Licencias_Medicas:
      Ctx: >-
        Los y las funcionarias(os) que presenten una licencia médica deben asegurarse de que esta sea remitida por el médico o centro de salud al empleador por los medios electrónicos correspondientes dentro de los tres días desde la emisión de la licencia (es el plazo que tiene el trabajador para presentar la licencia médica al empleador). En el caso de que la licencia sea emitida en papel, el funcionario tendrá tres días para hacerla llegar al Gobierno Regional entregándola por oficina de partes (o digitalizándola según los procedimientos de transformación digital). Por último, el funcionario(a) deberá estar atento(a) a la resolución de la ISAPRE o COMPIN, la cual autorizará, rechazará o reducirá los días de licencia otorgados. Para lo cual, en los casos que corresponda, deberá presentar mayores antecedentes para apelar al dictamen.

    Remuneraciones_Asignaciones_e_Incentivos:
      Ctx:
        - "Las remuneraciones del sector público están regidas por diversas escalas, siendo la Escala Única de Sueldos la norma general. Las remuneraciones de la Escala Única de Sueldos (EUS) se conforman por el sueldo base y por un conjunto de asignaciones que dependen de las responsabilidades y características del cargo, de los títulos académicos del trabajador y de la institución en la que trabajan."
        - "Los funcionarios del Gobierno Regional se rigen por el Estatuto Administrativo, Ley 18.834 de 1989. La remuneración constituye la sumatoria de los siguientes estipendios según corresponda:"
      Items:
        - Item: "1."
          Def: "Sueldo Base: El sueldo base de los trabajadores del Gobierno Central está regido en el artículo 1º de la EUS del Decreto Ley Nº 249, donde se establecen los grados y la renta mensual."
        - Item: "2."
          Def: "Bonificación Art. 18 DL 19185: Además del sueldo base, existen un conjunto de asignaciones reguladas por el artículo 18 de la Ley 19.185, las cuales siguen la clasificación de grados establecida en el DL Nº 1."
        - Item: "3."
          Def: "Asignación Profesional: Los profesionales regidos por la EUS tienen derecho a una Asignación Profesional, según lo establecido en el artículo 19 de la Ley 19.185."
        - Item: "4."
          Def: "Asignación de Dirección Superior: En el artículo 1º de la Ley 19.863 se establece la Asignación de Dirección Superior."
        - Item: "5."
          Def: "Bonificación de Salud y Bonificación Compensatoria Previsional: Los funcionarios regidos por la EUS tienen derecho a una bonificación de salud según lo establecido en el artículo 3° de la Ley 18.566. Además, existe la bonificación compensatoria previsional, regida por los artículos 10 y 1 de la Ley 18.675."
        - Item: "6."
          Def: "Asignación de Responsabilidad Superior: Los funcionarios directivos entre los grados 1-A y 5 reciben una asignación de responsabilidad superior al 40% del sueldo base."
        - Item: "7."
          Def: "Asignación Modernización: Dentro de los componentes comunes de la EUS, existe la Asignación de Modernización, regida por la Ley 19.553."
      Ctx_Optional: "Nota sobre personal a contrata GORE (Ley de Presupuestos 2026): La Glosa 01, Partida 31 de la Ley N°21.796 (Presupuestos 2026) establece que para el personal a contrata de los GORE no regirá la limitación de antigüedad del Estatuto Administrativo. Asimismo, hasta un 20% del personal a contrata podrá desempeñar funciones directivas por encargo del Gobernador Regional. El personal a honorarios podrá tener calidad de Agente Público para efectos de responsabilidad."

    Permisos_con_Goce_de_Remuneraciones:
      Ctx: >-
        Estos permisos, comúnmente llamados permisos administrativos, corresponden a 6 días asignados a todo funcionario público en el período de un año, y se pueden fraccionar en medios días, sean estos AM o PM. Si el funcionario no hace uso de estos días durante el período de un año calendario, se pierden sin que se tenga derecho a utilizarlos en un próximo período. Para solicitar este permiso, se debe hacer una solicitud a la jefatura directa a través de un formulario destinado para tal efecto (preferentemente electrónico).

    Permisos_sin_Goce_de_Remuneraciones:
      Ctx: "Estos permisos deben ser autorizados por la jefatura directa. Un funcionario podrá solicitar este permiso por:"
      Items:
        - "Motivos particulares, hasta seis meses en cada año calendario."
        - "Permanecer en el extranjero, hasta por dos años."

    Feriado_Legal:
      Ctx: "Comúnmente conocidos como vacaciones, se utilizan para el descanso de los funcionarios durante un año calendario. Los días de feriado legal varían según la antigüedad laboral:"
      Items:
        - "De 1 a 15 años: 15 días hábiles"
        - "De 15 a 20 años: 20 días hábiles"
        - "Más de 20 años laborales: 25 días hábiles"
      Ctx_Optional:
        - "Para justificar los años trabajados, se debe presentar un Certificado de Vacaciones Progresivas otorgado por la AFP."
        - "Los feriados legales pueden o no ser utilizados durante el año. Si no se utilizan, pueden ser traspasados según la normativa vigente."
        - "Para solicitar este permiso, se debe hacer una solicitud a la jefatura directa a través de un formulario destinado para tal efecto (preferentemente electrónico)."

    Destinaciones_Comisiones_de_Servicio_y_Cometidos:
      Ctx:
        - "Toda actividad laboral desarrollada por los funcionarios fuera de las dependencias físicas del Gobierno Regional se considera un cometido funcional. Este debe ser respaldado por un formulario creado para tal efecto (preferentemente electrónico), que debe detallar la actividad a realizar, el tiempo que se utilizará y la fecha en la cual se llevará a cabo. El formulario consta de dos partes:"
        - "Todo funcionario que incurra en un cometido deberá llenar la primera parte del formulario, y una vez realizado el cometido, deberá completar la segunda parte, que debe ser firmada por la jefatura directa, quien indicará si existe derecho a viático y a qué porcentaje. Finalmente, el formulario debe ser entregado al Departamento de Gestión y Desarrollo de Personas."
      Proc:
        - "Planificación de la actividad y detalles"
        - "Características reales del cometido, respaldadas por correo, invitación, planificación, etc."
      Ctx_Optional: "La Ley de Presupuestos 2026 (Artículo 22) instruye reducir las comisiones de servicio, especialmente al extranjero, a las imprescindibles."

    Jornada_Horaria_y_Mecanismo_de_Control_de_Jornada:
      Req:
        - "Todo funcionario en Calidad Jurídica Planta, Contrata o Código del Trabajo deberá registrar su ingreso y salida de la jornada laboral en el sistema de control dispuesto para tal efecto."
        - "Para ello, deberá ponerse en contacto con el Departamento de Gestión y Desarrollo de Personas para registrar sus datos."
      Ctx: "La jornada laboral corresponde a 44 horas semanales, distribuidas de la siguiente manera:"
      Items:
        - "Lunes a Jueves: 9 horas"
        - "Viernes: 8 horas"
      Ctx_Optional:
        - "La hora de ingreso podrá ser entre las 8:00 y las 9:00 horas, y la hora de salida dependerá de la hora en que se cumplen las 9 horas (de lunes a jueves) y las 8 horas (los viernes)."
        - "Cuando por distintas razones el funcionario olvide marcar, deberá justificarse con la jefatura directa a través de correo electrónico con copia al GDP."

    Jornada_Extraordinaria:
      Ctx: >-
        Para trabajar jornadas extraordinarias, el funcionario deberá presentar el formulario N°1 correspondiente a Planificación de Trabajo Extraordinario, el cual debe ser autorizado por la jefatura. Una vez transcurrido el período autorizado para el trabajo extraordinario, se procederá a calcular el tiempo acumulado que exceda el período laboral, el cual será reconocido a través de una resolución que contempla un Formulario N°2 y los respaldos del sistema de control. Una vez reconocido el tiempo de trabajo extraordinario, se registrará en una cuenta a nombre del funcionario, quien podrá utilizarlo como tiempo compensado durante dos años. Posteriormente, se extinguirá. Para solicitar este permiso, se deberá tener claridad de cuánto tiempo posee el funcionario y hacer una solicitud a la jefatura directa a través de un formulario destinado para tal efecto (preferentemente electrónico).

    Formacion_y_Capacitacion_Funcionaria:
      Ctx: >-
        Todos los años, se aprueba un Plan Anual de Capacitación, el cual establece las actividades de capacitación que se desarrollará el Gobierno Regional durante el año, y a quienes irán dirigidas. Por otro lado, existen diversas posibilidades de optar a actividades de capacitación, como Cursos de la Contraloría, Campus del Servicio Civil, Diplomados y Cursos de la SUBDERE, entre otros. Cada vez que un funcionario(a) quiera optar a estas actividades de perfeccionamiento, deberá presentar al Encargado de Capacitación del GORE un formulario firmado por su jefatura directa. Finalmente, al obtener su certificado de aprobación, deberá remitirlo al Encargado de Capacitación para su correspondiente registro.

    Proceso_de_Calificaciones_Funcionarias:
      Proc:
        - Item: "1."
          Def: "El sistema de calificación tendrá por objeto evaluar el desempeño y las aptitudes de cada funcionario, atendidas las exigencias y características de su cargo, y servirá de base para el ascenso, los estímulos y la eliminación del servicio."
        - Item: "2."
          Req: "Todos los funcionarios, incluido el personal a contrata, deben ser calificados anualmente, en alguna de las siguientes listas:"
          Items:
            - "Lista N° 1: Distinción"
            - "Lista N° 2: Buena"
            - "Lista N° 3: Condicional"
            - "Lista N° 4: Eliminación"
        - Item: "3."
          Resp: "El Jefe Superior de la institución"
          Req: "Será personalmente responsable del cumplimiento de este deber."
        - Item: "4."
          Cond: "No serán calificados el Jefe Superior de la institución, su subrogante legal, los miembros de la Junta Calificadora Central y los delegados del personal, quienes conservarán la calificación del año anterior, cuando corresponda. Con todo, si el delegado del personal lo pidiere, será calificado por su Jefe Directo."
        - Item: "5."
          Req: "La calificación se hará por la Junta Calificadora."
        - Item: "6."
          Req: "Las Juntas Calificadoras se integrarán según normativa."
        - Item: "7."
          Req: "Los funcionarios elegirán un representante titular y un suplente. La Asociación de Funcionarios con mayor representación tendrá derecho a designar un delegado con voz."
        - Item: "8."
          Req: "La Junta Calificadora será presidida por el funcionario de más alto nivel jerárquico."
        - Item: "9."
          Ctx: "Las normas de este párrafo sirven de base para el reglamento de calificaciones."
        - Item: "10."
          Ctx: "La calificación evaluará los doce meses de desempeño entre el 1° de septiembre y el 31 de agosto."
        - Item: "11."
          Req: "El proceso de calificaciones deberá iniciarse el 1° de septiembre y terminarse a más tardar el 30 de noviembre."
        - Item: "12."
          Prohib: "No serán calificados funcionarios con menos de seis meses de desempeño efectivo."
        - Item: "13."
          Req: "La Junta Calificadora considerará la precalificación del Jefe Directo y anotaciones de mérito o demérito."
        - Item: "14."
          Resp: "Los jefes"
          Req: "Son responsables de las precalificaciones."
        - Item: "15."
          Ctx: "Elementos básicos: hoja de vida y hoja de calificación."
        - Item: "16."
          Ctx: "Infracción establecida en sumario se considera una vez."
        - Item: "17."
          Ctx: "Anotaciones de mérito: por conducta o desempeño destacado."

    Prevencion_de_Riesgos_Higiene_y_Seguridad:
      Ctx: "El Gobierno Regional de Ñuble se encuentra adherido a la Mutual de Seguridad de la Cámara Chilena de la Construcción desde el año 2018 a la fecha. <www.mutual.cl>"

    Definiciones_Importantes_Accidentes_y_Enfermedades:
      Def:
        - Item: "a)"
          Termino: "Accidentes del Trabajo"
          Def: "Toda lesión que una persona sufra a causa o con ocasión del trabajo, y que le produzca incapacidad o muerte."
        - Item: "b)"
          Termino: "Enfermedad Profesional"
          Def: "Causada directamente por el ejercicio de una profesión o trabajo, que produzca incapacidad o muerte."
        - Item: "c)"
          Termino: "Accidente de Trayecto"
          Def: "Ocurrido en el trayecto \"directo\" de ida o regreso, entre la habitación y el lugar de trabajo."

    Documentacion_Exigida_para_Notificar:
      Req:
        - Caso: "Accidentes del Trabajo"
          Items:
            - "Denuncia Individual de Accidente del Trabajo (DIAT), Cédula de Identidad."
        - Caso: "Accidente de Trayecto"
          Items:
            - "DIAT, Cédula de Identidad."
        - Caso: "Enfermedad Profesional"
          Items:
            - "Denuncia Individual de Enfermedad Profesional (DIEP), Cédula de Identidad."

    Responsabilidad_del_Funcionario_frente_a_un_Accidente:
      Req:
        - "El funcionario debe informar a su Jefe directo y al Departamento de Gestión de Personas de cualquier accidente laboral. El reporte debe ser a la brevedad."
        - "Tras ser atendido, debe entregar el \"Informe de atención\" y, si hay reposo, el \"Alta Médica\" antes de reintegrarse."
        - "El funcionario que retorne de reposo por Accidente del Trabajo deberá tener una entrevista con el Comité Paritario de Higiene y Seguridad."

  Seccion_12_Comites_Paritarios_de_Higiene_y_Seguridad:
    ID: GN-MANUAL-INDUCCION-S12
    Def: "El Comité Paritario de Higiene y Seguridad (CPHS) es una unidad técnica de trabajo conjunto entre la empresa y los trabajadores, para detectar y evaluar riesgos de accidentes y enfermedades profesionales, y buscar estrategias de prevención."
    Integracion:
      Def: "Está integrado por tres representantes titulares designados por la administración y tres representantes titulares elegidos por los funcionarios, más sus respectivos suplentes."
    Contacto:
      Ctx: "Para contactar al Comité Paritario de Higiene y Seguridad del Gobierno Regional, puedes escribir a: comité<.paritario@goredenuble.cl>"
    Principales_Funciones:
      Act:
        - "Asesorar e instruir a los trabajadores para la correcta utilización de los instrumentos de protección."
        - "Vigilar el cumplimiento de las medidas de prevención, higiene y seguridad."
        - "Investigar las causas de los accidentes del trabajo y enfermedades profesionales."
        - "Decidir si el accidente o la enfermedad profesional se debió a negligencia inexcusable del trabajador."
        - "Indicar la adopción de todas las medidas de higiene y seguridad."
        - "Promover la realización de cursos de capacitación profesional."

  Seccion_13_Probidad_y_Transparencia:
    ID: GN-MANUAL-INDUCCION-S13
    Ctx: "Concepto de probidad y su aplicación al funcionario público (Ley 19.653 y Ley 18.575)"
    Def: "El principio de probidad en la función pública consiste en observar una conducta funcionaria intachable, un desempeño honesto y leal de la función o cargo con preeminencia del interés general sobre el particular."
    Componentes:
      - Item: "a)"
        Req: "Observar una conducta funcionaria intachable."
      - Item: "b)"
        Req: "Desempeñar honesta y lealmente la función o cargo."
      - Item: "c)"
        Req: "Darle preeminencia al interés general sobre el particular."
    Alcance:
      Ctx: "Están sujetos al principio de probidad todas las personas que prestan servicios en o para la Administración Central del Estado y los Gobiernos Regionales, ya sea en cargos de planta, empleos a contrata, contratos a honorarios y contratos regidos por las normas del Código del Trabajo."

  Seccion_14_Declaraciones_de_Intereses_y_Patrimonios_DIP_Ley_20880:
    ID: GN-MANUAL-INDUCCION-S14
    Ctx:
      - "Para el debido cumplimiento del principio de probidad, esta ley determina las autoridades y funcionarios que deberán declarar sus intereses y patrimonio en forma pública. Para el GORE Ñuble, esto incluye al Gobernador Regional, Consejeros Regionales, Administrador Regional, Jefes de División y otros funcionarios hasta el tercer nivel jerárquico o con funciones de fiscalización, así como ciertos contratados a honorarios."
      - "Gestión de Personas debe ingresar al nuevo funcionario (si corresponde) a la plataforma <www.declaracionjurada.cl>, administrada por la Contraloría General de la República. Esta declaración debe confeccionarse dentro de los primeros 30 días corridos desde el ingreso, actualizarse cada mes de marzo (plazo máximo 31 de marzo), y realizarse una declaración de cese de funciones dentro de los 30 días posteriores al término del vínculo."

  Seccion_15_Consejo_para_la_Transparencia_y_Ley_20285:
    ID: GN-MANUAL-INDUCCION-S15
    Def: "El Consejo para la Transparencia (CPLT) es una corporación autónoma de derecho público, con personalidad jurídica y patrimonio propio, creado por la Ley de Transparencia de la Función Pública y de Acceso a la Información de la Administración del Estado."
    Obj:
      - "Garantizar el principio de transparencia y el derecho de acceso a la información pública. Velar por el adecuado cumplimiento de la Ley de Protección de Datos Personales."
      - "Fiscalizar el cumplimiento de las normas de transparencia y acceso a la información, aplicando sanciones."
      - "Promover y difundir el principio de transparencia y el derecho de acceso a la información."

  Seccion_16_Ley_de_Acceso_a_la_Informacion_Transparencia_Activa_y_Pasiva_Lobby:
    ID: GN-MANUAL-INDUCCION-S16

    Transparencia:
      Def: "La Ley de Acceso a la Información (Ley 20.285) establece dos modalidades de transparencia: activa y pasiva."

      Transparencia_Activa:
        Req:
          - "Los servicios públicos, incluyendo el GORE Ñuble, deben mantener actualizados sus sitios web (ej. <www.goredenuble.cl> sección Transparencia Activa), permitiendo el acceso a información relevante."
          - "El CPLT dispone el portal web [www.portaltransparencia.cl](http://www.portaltransparencia.cl), donde los servicios públicos deben ingresar mensualmente información como:"
        Items:
          - "Actos y documentos publicados en Diario Oficial."
          - "Potestades y Marco Normativo."
          - "Estructura orgánica y facultades, funciones y atribuciones."
          - "Personal y remuneraciones."
          - "Adquisiciones y contrataciones."
          - "Transferencias de fondos y aportes económicos entregados."
          - "Actos y resoluciones con efectos sobre terceras personas."
          - "Subsidios y beneficios."
          - "Mecanismos de participación ciudadana."
          - "Información Presupuestaria."
          - "Auditorías al ejercicio presupuestario."
          - "Participación en otras entidades."
          - "Antecedentes preparatorios de normas."
          - "Lobby y gestión de intereses (Ley N°20.730)."
          - "Declaración de patrimonio e intereses (Ley N°20.880)."
          - "Sanciones por incumplimiento Ley de Transparencia."
          - "Acceso a Información Pública."
          - "Transparencia proactiva."
        Warn: "La falta, omisión o alteración de esta información conlleva multas."

      Transparencia_Pasiva:
        Def:
          - "Consiste en la entrega de información a las personas que la soliciten al GORE Ñuble a través de los mecanismos dispuestos (link en web, formulario del portal de transparencia, formato físico en Oficina de Partes)."
          - "Las solicitudes deben ser respondidas mediante oficio y la información proporcionada en el formato solicitado, dentro del plazo legal, para evitar multas."

    Lobby:
      Def: "La Ley N°20.730 regula el Lobby y las gestiones que representen intereses particulares ante las autoridades y funcionarios. Su objetivo es regular la publicidad en estas actividades para fortalecer la transparencia y probidad."
      Sujetos_Pasivos_en_el_GORE:
        Def: "Gobernador Regional, Consejeros Regionales, Secretario Ejecutivo del CORE, jefes de gabinete, y funcionarios con atribuciones decisorias relevantes o que influyan en ellas, designados por resolución."
      Sujetos_Activos:
        Def: "Quienes realizan lobby o gestión de interés particular."
      Deberes_de_Sujetos_Pasivos:
        Req:
          - "Registro de agenda pública (audiencias, reuniones, viajes, donativos)."
          - "Publicidad de los registros (en <www.leylobby.gob.cl>)."
          - "Deber de Igualdad de trato."
      Resp: "El GORE Ñuble es responsable de nombrar a los funcionarios que cumplen rol de sujeto pasivo."

  Seccion_17_Asignacion_de_Equipos_Institucionales_y_Seguridad_de_la_Informacion:
    ID: GN-MANUAL-INDUCCION-S17
    Asignacion_de_Equipos:
      Ctx:
        - "Asignación de Equipos: La DAF proporciona equipos necesarios (computadoras, teléfonos, etc.)."
        - "Entrega de Equipos: Documentada y firmada."
        - "Solicitud de Equipos Móviles: Justificada y aprobada por jefatura y DAF, según disponibilidad."
        - "Registro de Equipos: Detalla equipos asignados."

    Tratamiento_y_Seguridad_de_la_Informacion:
      Ctx: "Tratamiento y Seguridad de la Información (Ley N°21.719 y Ley N°21.663): Conjunto de políticas y procedimientos para proteger la información contra accesos no autorizados, alteraciones, pérdida o destrucción, en cumplimiento con la Ley de Protección de Datos Personales y la Ley Marco de Ciberseguridad."
      Req:
        - "Políticas de Seguridad de la Información: Normas y directrices sobre uso de contraseñas, acceso a sistemas, manejo de datos sensibles, etc."
        - "Confidencialidad: Proteger información sensible y privada."
        - "Integridad de la Información: Mantener datos precisos y completos."
        - "Disponibilidad de la Información: Asegurar acceso a funcionarios autorizados."
        - "Backup y Recuperación de Datos: Realizar copias de seguridad."
        - "Uso Adecuado de Equipos: Normas de uso responsable y prevención de daños."
        - "Devolución de Equipos: Al finalizar relación laboral o cuando no sean necesarios."
        - "Capacitación en Seguridad y Protección de Datos: Programas de formación sobre mejores prácticas, reconocimiento de amenazas, protección de datos y ciberseguridad."
        - "Acceso a Sistemas y Redes: Políticas de acceso y autorización. Asignación de correo electrónico y acceso a intranet y plataformas electrónicas."
        - "Incidentes de Seguridad y Brechas de Datos: Procedimientos para identificar, reportar y manejar incidentes de seguridad y violaciones de datos personales (notificación a la Agencia de Protección de Datos Personales y a la Agencia Nacional de Ciberseguridad, según corresponda)."
        - "Responsabilidad del Usuario: Cumplir políticas de seguridad, notificar incidentes, y proteger equipos e información."
        - "Protección de Datos por Diseño y por Defecto: Aplicar medidas para proteger datos desde la concepción de sistemas y procesos."
        - "Evaluación de Impacto en Protección de Datos (EIPD): Realizarla previo a tratamientos de alto riesgo."
        - "Delegado de Protección de Datos (DPD): Considerar su designación para velar por el cumplimiento de la Ley N°21.719."

    Procedimientos_Especificos:
      Proc:
        - "Asignación y Entrega de Equipos: Solicitud del jefe de departamento, aprobación DAF, registro, entrega con firma de recepción."
        - "Solicitud de Equipos Móviles: Justificación a supervisor, revisión, aprobación DAF, entrega y registro."
        - "Tratamiento y Seguridad de la Información:"
      Steps:
        - Item: "1."
          Act: "Capacitación Inicial: Inducción sobre políticas de seguridad, protección de datos y ciberseguridad."
        - Item: "2."
          Act: "Uso de Contraseñas Seguras y doble factor de autenticación cuando proceda."
        - Item: "3."
          Act: "Acceso a Sistemas según rol."
        - Item: "4."
          Act: "Backup Regular."
        - Item: "5."
          Act: "Reporte de Incidentes al encargado de ciberseguridad y Dpto. de Informática."

  Seccion_18_Transformacion_Digital_del_Estado_Ley_21180:
    ID: GN-MANUAL-INDUCCION-S18
    Ctx: "La Ley N°21.180 de Transformación Digital del Estado, publicada en 2019 y con implementación gradual hasta 2027, mandata a todos los órganos de la Administración del Estado, incluyendo el Gobierno Regional de Ñuble, a realizar sus procedimientos administrativos por medios electrónicos."

    Principios_y_Objetivos:
      Req:
        - "Procedimientos Electrónicos: La regla general es la tramitación electrónica, utilizando expedientes digitales."
        - "Cero Papel: Eliminar progresivamente el uso del papel en la gestión administrativa."
        - "Firma Electrónica: Uso de firma electrónica (simple o avanzada según el acto) para dar validez a documentos digitales."
        - "Notificaciones Electrónicas: Las comunicaciones a los interesados se realizan por medios electrónicos, preferentemente a través de un Domicilio Digital Único."
        - "Interoperabilidad: Los sistemas del GORE deben poder intercambiar información con otros órganos del Estado de forma segura y estandarizada, utilizando la Plataforma de Interoperabilidad del Estado (PISEE)."
        - "Seguridad y Protección de Datos: La transformación digital debe realizarse resguardando la seguridad de la información y cumpliendo con la normativa de protección de datos personales (Ley N°21.719) y ciberseguridad (Ley N°21.663)."

    Plataformas_Transversales_y_su_Aplicacion_en_el_GORE_Nuble:
      Ctx: "El Estado ha desarrollado plataformas para apoyar esta transformación, que el GORE Ñuble debe utilizar o integrar:"
      Items:
        - "ClaveÚnica: Sistema de autenticación centralizado para que ciudadanos y funcionarios accedan a servicios digitales. El GORE debe integrar ClaveÚnica en sus trámites en línea."
        - "FirmaGob: Plataforma para la firma electrónica avanzada de documentos por parte de funcionarios públicos. Facilita la firma de resoluciones, oficios, etc."
        - "DocDigital: Sistema para el envío y recepción de comunicaciones oficiales electrónicas entre organismos públicos, reemplazando el oficio en papel. Su uso es obligatorio."
        - "CPAT (Catálogo de Procedimientos Administrativos y Tramitaciones): Herramienta para registrar y diagnosticar el estado de digitalización de todos los trámites del GORE. Es de uso obligatorio y alimenta el portal de trámites del Estado."
        - "SIMPLE: Plataforma para crear trámites digitales de baja complejidad sin necesidad de programación. El GORE puede usarla para digitalizar rápidamente formularios y flujos de trabajo."
        - "PISEE (Plataforma de Integración de Servicios Electrónicos del Estado): Infraestructura para el intercambio seguro de datos entre instituciones, fundamental para el principio de \"no pedir al ciudadano información que el Estado ya posee\"."
        - "Portal de Datos Abiertos (datos.gob.cl): Para la publicación de datos públicos del GORE en formatos reutilizables."

    Implementacion_en_el_GORE_Nuble:
      Items:
        - "Plan de Transformación Digital: El GORE debe contar con un plan estratégico para abordar la digitalización, identificando trámites prioritarios, necesidades de infraestructura, capacitación y adecuación normativa interna."
        - "Gobernanza Digital: Se recomienda designar un Coordinador de Transformación Digital y un Delegado de Protección de Datos."
        - "Gestión Documental Electrónica: Implementar o adoptar un sistema de gestión de expedientes electrónicos que cumpla con las normas técnicas."
        - "Capacitación y Gestión del Cambio: Es fundamental capacitar al personal y gestionar el cambio cultural asociado a la digitalización."
        - "Registro en Plataformas: El nuevo funcionario, según su rol, será registrado y capacitado en el uso de DocDigital, FirmaGob (si corresponde), y otras plataformas institucionales."
      Res: "La transformación digital es un proceso continuo que busca modernizar la gestión regional, hacerla más eficiente, transparente y cercana a las necesidades de los habitantes de Ñuble. El GORE Ñuble está comprometido con este proceso, avanzando hacia la digitalización completa de sus servicios y procedimientos para el año 2027."

  Seccion_19_Evaluacion_de_Induccion:
    ID: GN-MANUAL-INDUCCION-S19
    Ctx: "Como cierre del proceso de inducción, se debe contar con una fase de evaluación dirigida por el equipo de gestión de personas al funcionario que haya desarrollado este proceso formal de inducción, en la lógica de mejora continua, para obtener información significativa, monitorear si los objetivos se están logrando y realizar las adecuaciones pertinentes."
    Ctx_Optional: "Esta evaluación considera los siguientes ámbitos:"

    Actividad_de_Bienvenida:
      Table:
        Columns: [Actividad, SI_NO, Comentarios_u_Observaciones, Check_GDP]
        Rows:
          - Actividad: "Fue recibido por su jefatura directa"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Tuvo la oportunidad de conocer los compañeros de trabajo"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "El lugar físico de desempeño"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Recibió algún set con material que contenga la información relevante de la organización"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Contó al momento de ingreso con un puesto de trabajo."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Contó al momento de ingreso con un PC."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Contó al momento de ingreso con un teléfono."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""

    Relacionadas_con_el_Cargo:
      Table:
        Columns: [Actividad, SI_NO, Comentarios_u_Observaciones, Check_GDP]
        Rows:
          - Actividad: "Se logró claridad sobre los objetivos del cargo."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre las metas y los medios para alcanzarlas"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre el rol que desempeñará"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre con quiénes debe interactuar"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Recibió la información necesaria para iniciar sus tareas."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""

    Relacionadas_con_la_Institucion:
      Table:
        Columns: [Actividad, SI_NO, Comentarios_u_Observaciones, Check_GDP]
        Rows:
          - Actividad: "Se logró claridad sobre la misión de la organización."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre los objetivos estratégicos, de la organización."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre el organigrama de la organización"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre los deberes y obligaciones como funcionario de la organización."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre los valores de la organización."
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
          - Actividad: "Se logró claridad sobre las normas de la organización"
            SI_NO: ""
            Comentarios_u_Observaciones: ""
            Check_GDP: ""
