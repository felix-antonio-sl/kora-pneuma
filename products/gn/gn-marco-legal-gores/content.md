---
urn: urn:gn:kb:gn-marco-legal-gores
nombre: gn-marco-legal-gores
version: "0.1.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Compendio Jurídico para Gobiernos Regionales; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/01_fundamentos/legal/kb_gn_200_marco_legal_gores_koda.yml (sha256:1162ece95a989f4e7dda3387d606ce53c79e2ae56fe159a600c9250934c5120e); URN KODA legado urn:gorenuble:gn:marco-legal-gores:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2025-11-27
lang: es
tags: ["gn", "gore-os", "koda", "domains", "01-fundamentos", "legal", "marco", "gores"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:marco-legal-gores:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use Only"
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2026-02-19"
    last_modified_at: "2026-02-19"

# Compendio Jurídico para Gobiernos Regionales
# Transformación KODA/Spec desde: kb_gn_200_marco_legal_gores.md
# Estado: BORRADOR INICIAL
---
ID: KB-GN-200-MARCO-LEGAL-GORES-KODA
Version: 0.1.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: Cascade
Creation-Date: 2025-11-27
Modification-Date: 2025-11-27
Ctx: "Transformación KODA/Spec del 'Compendio Jurídico para Gobiernos Regionales' usado por el Goreólogo."
Primary-Source: "kb_gn_200_marco_legal_gores.md"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-KB-GN-200
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, relationships) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents use Ctx:, Ctx_Required:, or Ctx_Optional:.

    LANGUAGE POLICY: Keywords in English, content in original language (es-CL). Never translate content.
    END_LLM_INSTRUCTIONS

Purp: "Concentrar en un solo artefacto KODA/Spec el marco legal clave que afecta a los Gobiernos Regionales (GORE), como base del Goreólogo."

# ============================================================================
# 1. MARCO CONCEPTUAL JURÍDICO TRANSVERSAL
# ============================================================================

Marco_Conceptual_Juridico_Transversal:
  ID: MCJT-01
  Purp: "Establecer una SSoT de conceptos jurídicos transversales usados en el compendio, evitando redundancia y asegurando coherencia."

  Conceptos_Fundamentales:
    ID: MCJT-CONCEPTOS-FUNDAMENTALES-01
    Cpt: "Conceptos de Probidad, Transparencia y Procedimiento Administrativo."

    Probidad_Administrativa:
      ID: DEF-PROBIDAD-ADMINISTRATIVA-01
      Def: "Observar una conducta funcionaria intachable y un desempeño honesto y leal de la función o cargo, con preeminencia del interés general sobre el particular."
      Fnd: "Art. 52, Ley N° 18.575 (texto original incorporado por Ley N° 19.653)."

    Conflicto_de_Intereses:
      ID: DEF-CONFLICTO-DE-INTERESES-01
      Def: "Concurrencia del interés general propio del ejercicio de las funciones con un interés particular, sea o no económico, del que ejerce dichas funciones o de terceros vinculados a él."
      Fnd: "Art. 1, Ley N° 20.880."

    Transparencia_Administrativa:
      ID: DEF-TRANSPARENCIA-ADMINISTRATIVA-01
      Def: "Principio que promueve el conocimiento de procedimientos, contenidos y fundamentos de las decisiones adoptadas en ejercicio de la función pública. Implica publicidad de actos, fundamentos e información de sustento."
      Fnd: "Art. 3 y 13, Ley N° 18.575 (texto incorporado por Ley N° 19.653); Art. 3 y 5, Ley N° 20.285."

    Acto_Administrativo:
      ID: DEF-ACTO-ADMINISTRATIVO-01
      Def: "Decisión formal y escrita que adopta la Administración en ejercicio de una potestad pública. Goza de presunción de legalidad y es exigible desde su entrada en vigencia."
      Fnd: "Art. 3, Ley N° 19.880."

    Licitacion_Publica:
      ID: DEF-LICITACION-PUBLICA-01
      Def: "Procedimiento administrativo concursal mediante el cual la Administración convoca públicamente a interesados para formular propuestas conforme a bases fijadas, seleccionando y aceptando la más conveniente."
      Fnd: "Art. 7, Ley N° 19.886."

# ============================================================================
# 2. LEYES CLAVE PARA LOS GORE
# ============================================================================

Leyes_Clave_GORE:
  ID: LEYES-GORE-01
  Purp: "Sintetizar el marco legal principal que regula a los GORE, su inserción institucional y su coordinación con otros actores del Estado."

  Ley_21730_Ministerio_Seguridad_Publica:
    ID: LMSP-01
    Purp: "Describir la nueva institucionalidad de seguridad pública y su vínculo con los GORE."
    Fnd: "Ley 21.730, publicada el 06-Oct-2023."

    Institucionalidad_General:
      ID: LMSP-INSTITUCIONALIDAD-01
      Cpt: "Institucionalidad general y funciones del Ministerio de Seguridad Pública."
      Funciones_Ministerio:
        ID: LMSP-FUNCIONES-MINISTERIO-01
        Ctx: "Art. 5 Ley 21.730."
        Cpt: "Atribuciones relevantes para GORE."
        Act:
          - "Colaborar con autoridades regionales y comunales y prestarles asesoría para que identifiquen prioridades y proyectos coherentes con la Política Nacional de Seguridad Pública (letra s))."

      Funciones_Ministro:
        ID: LMSP-FUNCIONES-MINISTRO-01
        Ctx: "Art. 6 Ley 21.730."
        Cpt: "Atribuciones del Ministro/a respecto de Fuerzas de Orden."
        Certificado_Pertinencia:
          ID: LMSP-FUNCIONES-MINISTRO-CERT-01
          Cpt: "Certificado de pertinencia para operaciones relevantes de las policías."
          Req:
            - "Contrataciones, donaciones o transferencias > 1.000 UTM de las policías, incluidos convenios con GORE, deben contar con certificado de pertinencia del Ministerio de Seguridad Pública."

      SPD_Subsecretaria_Prevencion_Delito:
        ID: LMSP-SPD-01
        Ctx: "Art. 21 Ley 21.730."
        Cpt: "Atribuciones relevantes de la SPD para coordinación con GORE."
        Act:
          - "Colaborar y asesorar a autoridades regionales y municipales para alinear sus proyectos con la Política Nacional de Seguridad Pública (letra l))."
          - "Dictar lineamientos y orientaciones técnicas para diseño, aprobación y ejecución de planes y proyectos regionales/comunales de prevención."
          - "Celebrar convenios con GORE y municipalidades (letra m))."

    Sistema_y_Consejos_Regional_Seguridad:
      ID: LMSP-SISTEMA-SEGURIDAD-01
      Sistema_Seguridad_Publica:
        ID: LMSP-SISTEMA-DEF-01
        Ctx: "Art. 8 Ley 21.730."
        Def: "Conjunto de instituciones públicas y privadas que colaboran para asegurar el orden público y prevenir el delito."
        Resp: "Ministerio de Seguridad Pública está a cargo del Sistema."

      Consejos_Regionales:
        ID: LMSP-CONSEJOS-REGIONALES-01
        Ctx: "Art. 10 Ley 21.730."
        Def: "Consejos Regionales de Seguridad Pública y de Prevención del Delito como instancias de coordinación y colaboración del Sistema a nivel regional."
        Composicion:
          Resp:
            - "Presididos por el Delegado Presidencial Regional."
            - "Secretaría Ejecutiva a cargo del SEREMI de Seguridad Pública."
          Integrantes_Relevantes:
            - "Gobernador Regional."
            - "Representante del Consejo Regional."
        Delimitacion_Funcional:
          Fnd:
            - "Refuerza separación de funciones: GORE coopera en prevención; Delegado Presidencial gestiona seguridad operativa."
          Warn:
            - "Participación del Gobernador como miembro colaborador no implica control ni subordinación de las fuerzas de seguridad."
          Req:
            - "Cualquier plan de seguridad del GORE debe canalizarse a través de estos Consejos."

    Desconcentracion_y_SEREMI_Seguridad:
      ID: LMSP-ESTRUCTURA-TERRITORIAL-01
      SEREMI_Seguridad:
        ID: LMSP-SEREMI-SEGURIDAD-01
        Ctx: "Art. 14 y 23 Ley 21.730."
        Def: "Secretarías Regionales Ministeriales de Seguridad Pública como mecanismo de desconcentración territorial del Ministerio."
        Dep: "SEREMI de Seguridad Pública depende directamente del Ministro, no del GORE."
        Fnd: "Refuerza que la función de seguridad pública es desconcentrada, no descentralizada."
        Atribuciones_Relevantes:
          - "Coordinar ejecución de políticas, planes y programas del Ministerio en la región."
          - "Prestar asistencia y colaborar con Gobernador Regional y CORE para alinear proyectos con la Política Nacional."
        Warn:
          - "No existe subordinación del SEREMI al GORE; la relación debe ser de cooperación."

    Implicancias_Para_GORE:
      ID: LMSP-IMPLICANCIAS-LEGALES-01
      Coordinacion_Inversion_Seguridad:
        ID: LMSP-COORDINACION-INVERSION-01
        Cpt: "Coordinación de inversiones y políticas de seguridad."
        Req:
          - "GORE debe alinear sus inversiones en seguridad (incluyendo FNDR) con orientaciones del Ministerio de Seguridad Pública."
        Mech:
          - "Directrices sobre políticas locales de seguridad emanan ahora del nuevo Ministerio, no de Interior."

      Regla_Reemplazo_Normativo:
        ID: LMSP-REGLA-REEMPLAZO-01
        Cpt: "Donde leyes antiguas (ej. Ley 20.502) hablen del Ministerio del Interior en materias de prevención del delito, debe leerse 'Ministerio de Seguridad Pública'."
        Res:
          - "Ley 21.730, como norma posterior, deroga o modifica tácitamente las referencias anteriores en lo pertinente."

      Resolucion_Contiendas_Competencia:
        ID: LMSP-RESOLUCION-CONFLICTOS-01
        Cpt: "Resolución de contiendas de competencia entre Gobernador Regional y Delegado Presidencial Regional/SEREMI de Seguridad."
        Resp: "Contraloría General de la República (CGR)."
        Rec:
          - "Se espera que, en materias de orden público operativo, la CGR resuelva a favor del Delegado/SEREMI."

  Ley_18575_Bases_Generales_Admin_Estado:
    ID: LEY-18575-MASTER-01
    Purp: "Fijar principios y organización básica de la Administración del Estado, incluyendo el lugar institucional de los GORE."

    Disposiciones_Generales:
      ID: LEY-18575-TIT0-01
      Art_1_Administracion_Estado:
        ID: LEY-18575-ART1-01
        Def:
          - "Presidente de la República ejerce el gobierno y la administración del Estado con colaboración de órganos establecidos en la Constitución y la ley."
          - "La Administración del Estado está constituida por Ministerios, Gobiernos Regionales, Municipalidades, servicios públicos y otros órganos para el ejercicio de la función administrativa."
        Incl:
          - "Contraloría General de la República, Banco Central, Fuerzas Armadas, Fuerzas de Orden y Seguridad Pública, Gobiernos Regionales, Municipalidades, empresas públicas creadas por ley, entre otros."

      Art_2_Legalidad_y_Competencia:
        ID: LEY-18575-ART2-01
        Req:
          - "Órganos de la Administración del Estado deben someter su acción a la Constitución y las leyes."
          - "Deben actuar dentro de su competencia; no tienen más atribuciones que las que el ordenamiento les confiere expresamente."
        Res:
          - "Abuso o exceso en el ejercicio de potestades da lugar a acciones y recursos correspondientes."

      Art_3_Bien_Comun_y_Principios:
        ID: LEY-18575-ART3-01
        Purp:
          - "Administración del Estado al servicio de la persona humana; promover el bien común y atender necesidades públicas de forma continua y permanente."
        Mech:
          - "Ejercicio de atribuciones conferidas por la Constitución y la ley; aprobación, ejecución y control de políticas, planes y programas de alcance nacional, regional y comunal."
        Principios:
          - "Responsabilidad, eficiencia, eficacia, coordinación, impulsión de oficio del procedimiento, impugnabilidad de actos administrativos, control, probidad, transparencia, publicidad y participación ciudadana."

      Art_4_Responsabilidad_Estatal:
        ID: LEY-18575-ART4-01
        Resp:
          - "Estado responde por daños causados por órganos de la Administración en el ejercicio de sus funciones, sin perjuicio de responsabilidades personales de los funcionarios."

      Art_5_Coord_Administrativa:
        ID: LEY-18575-ART5-01
        Req:
          - "Autoridades y funcionarios deben velar por una administración eficiente e idónea de los medios públicos."
          - "Órganos deben cumplir sus cometidos coordinadamente, propender a unidad de acción y evitar duplicidad o interferencia de funciones."

      Probidad_y_Acoso:
        ID: LEY-18575-PROBIDAD-ACOSO-01
        Art_13_Probidad:
          ID: LEY-18575-ART13-01
          Req:
            - "Funcionarios deben observar el principio de probidad administrativa y las normas que lo regulan."
            - "Función pública debe ejercerse con transparencia."
            - "Debe propenderse al respeto del derecho de toda persona a un espacio libre de violencia y acoso laboral o sexual."
        Art_14_Protocolos:
          ID: LEY-18575-ART14-01
          Req:
            - "Órganos de la Administración deben contar con protocolos de prevención de violencia en el trabajo, acoso laboral y sexual."
            - "Protocolos incluyen acciones de difusión, formación, medidas de resguardo y aplicación de normas del Estatuto Administrativo en investigaciones."

    Organizacion_y_Servicios:
      ID: LEY-18575-TIT1-ORG-01
      Cpt: "Regula estructura de Ministerios, Subsecretarías, SEREMI y servicios públicos."
      Notas_Clave_Para_GORE:
        - "Define a los Gobiernos Regionales como parte de la Administración del Estado, pero con reglas específicas en su LOCGORE."
        - "Establece la figura de las Secretarías Regionales Ministeriales como órganos desconcentrados, que coordinan políticas sectoriales en el territorio, en relación de cooperación (no subordinación) con el GORE."

  Ley_19175_LOCGORE:
    ID: LEY-19175-MASTER-01
    Purp: "Regular el Gobierno Interior de la Región y la Administración de la Región a través de los Gobiernos Regionales (LOCGORE)."
    Ctx: "Transformación conceptual de los Títulos Primero y Segundo y del Párrafo 2° sobre transferencia de competencias."

    Gobierno_Interior_y_Delegados:
      ID: LEY-19175-GOB-INTERIOR-01
      Delegado_Presidencial_Regional:
        ID: LEY-19175-DPR-01
        Fnd: "Art. 1 y 2 LOCGORE."
        Def:
          - "Representante natural e inmediato del Presidente de la República en cada región."
          - "Titular del gobierno interior de la región."
        Nombramiento:
          - "Es nombrado y removido libremente por el Presidente; permanece mientras cuente con su confianza."
        Dependencia:
          - "Ejerce funciones conforme a las leyes y a instrucciones del Presidente, directamente o a través del Ministerio del Interior y Seguridad Pública."
        Rol_Coordinacion_Regional:
          Act:
            - "Coordinar la acción de gobierno interior a nivel regional."
            - "Velar por adecuada gestión de servicios públicos y de planes/programas en ejecución en la región."
            - "Requerir informes a SEREMI sobre cumplimiento de funciones e instrucciones técnicas/administrativas de los ministerios."
        Subrogacion:
          Mech:
            - "Es subrogado por el Delegado Presidencial Provincial que designe el Presidente."
            - "El Presidente puede designar suplente sin restricciones de tiempo del Estatuto Administrativo."
        Funciones_Principales:
          Act:
            - "Dirigir tareas de gobierno interior en la región, según orientaciones del Presidente."
            - "Velar por la tranquilidad y protección de personas y bienes."
            - "Instruir auxilio de la fuerza pública a través del SEREMI de Seguridad Pública."
            - "Mantener informado al Presidente sobre gobierno interior y desempeño de delegados provinciales y jefes regionales de servicios."
            - "Conocer y resolver recursos administrativos contra resoluciones de delegados presidenciales provinciales."
            - "Aplicar Ley de Extranjería, incluida la expulsión de extranjeros conforme a la ley."
            - "Efectuar denuncias y requerimientos ante tribunales de justicia."
            - "Representar extrajudicialmente al Estado en la región en actos y contratos dentro de su competencia."
            - "Coordinar, fiscalizar o supervigilar servicios públicos regionales/provinciales que dependan o se relacionen con el Presidente; informar semestralmente al Ministerio del Interior."
            - "Proponer ternas para nombramiento de SEREMI y proponer remoción de SEREMI y jefes regionales de servicios."
            - "Hacer presentes al nivel central, en conjunto con el Gobernador Regional, las necesidades de la región."
            - "Administrar complejos fronterizos de la región en coordinación con servicios nacionales."
            - "Adoptar medidas para prevenir y enfrentar emergencias o catástrofes."
            - "Dictar resoluciones e instrucciones necesarias para el ejercicio de sus atribuciones."
            - "Otorgar personalidad jurídica a corporaciones y fundaciones regionales cuando el Presidente delega esa atribución."
            - "Coordinar prevención y respuesta frente a conflictos sociales sin riesgo para la seguridad pública."
            - "Ejercer funciones que la ley entrega al Ministerio del Interior en la región, según instrucciones ministeriales."
          Principios_Ejercicio:
            Req:
              - "Debe desempeñar el cargo dialogando con autoridades locales."
              - "Debe respetar irrestrictamente planes de desarrollo comunales y regionales."

      Delegado_Presidencial_Provincial:
        ID: LEY-19175-DPP-01
        Fnd: "Art. 3, 4 y 5 LOCGORE."
        Def:
          - "Órgano territorialmente desconcentrado del Delegado Presidencial Regional en cada provincia."
        Nombramiento:
          - "Es nombrado y removido libremente por el Presidente."
        Rol:
          - "Ejercer, conforme a instrucciones del Delegado Presidencial Regional, la supervigilancia de servicios públicos existentes en la provincia que dependan o se relacionen con el Presidente."
        Funciones_Principales:
          Act:
            - "Ejercer tareas de gobierno interior en la provincia."
            - "Aplicar disposiciones sobre extranjería en la provincia."
            - "Autorizar reuniones en espacios públicos, informando a Carabineros."
            - "Requerir auxilio de la fuerza pública a través del Director Provincial de Seguridad Pública."
            - "Adoptar medidas para prevenir y enfrentar emergencias o catástrofes."
            - "Velar por buen uso de la Bandera Nacional y autorizar uso de pabellones extranjeros según la ley."
            - "Autorizar circulación de vehículos fiscales fuera de horas de trabajo y excepciones de uso de disco fiscal."
            - "Vigilar bienes del Estado, especialmente nacionales de uso público; impedir ocupación ilegal y exigir restitución."
            - "Dictar resoluciones e instrucciones para ejercicio de sus atribuciones."
            - "Supervisar programas y proyectos de desarrollo de servicios públicos en la provincia."
            - "Coordinar el desarrollo provincial."
            - "Informar al Delegado Presidencial Regional y a SEREMI sobre necesidades observadas."
            - "Ejercer, en la provincia, funciones que la ley entrega al Ministerio del Interior."
        Encargados_Localidades_Aisladas:
          Act:
            - "Con autorización del Delegado Presidencial Regional, puede designar encargados con atribuciones específicas para localidades aisladas."
            - "Determina facultades, plazo y ámbito territorial del encargado."
          Requisitos:
            - "Encargado debe ser ciudadano con derecho a sufragio y cumplir requisitos de ingreso a la Administración Pública."
          Regimen:
            - "Si es funcionario público, actúa en comisión de servicio; si es externo, se desempeña ad honorem."
            - "Queda sujeto a responsabilidades administrativas, civiles y penales de los funcionarios públicos."
            - "Designación se publica en Diario Oficial y diario de mayor circulación en la provincia (extracto)."

      Disposiciones_Comunes_Delegados:
        ID: LEY-19175-DEL-COMUNES-01
        Fnd: "Art. 6 a 12 LOCGORE."
        Requisitos_Cargo:
          Req:
            - "Ser ciudadano con derecho a sufragio."
            - "Tener al menos 21 años."
            - "Cumplir requisitos generales de ingreso a la Administración."
            - "No estar inhabilitado para ejercer funciones públicas."
            - "No estar condenado por crimen o simple delito."
            - "Residir en la región respectiva al menos 2 años previos a la designación."
          Inhabilidad_Drogas:
            Req:
              - "No tener dependencia de drogas estupefacientes/sicotrópicas ilegales, salvo tratamiento médico acreditado."
              - "Declaración jurada al asumir."
        Incompatibilidades_y_Cese:
          Incompatibilidades:
            - "Cargos de Gobernador Regional, Delegado Presidencial Regional, Delegado Presidencial Provincial, Consejero Regional, Alcalde, Concejal y Consejero Comunal de Organizaciones de la Sociedad Civil son incompatibles entre sí."
          Causales_Cese:
            - "Pérdida de requisitos habilitantes."
            - "Aceptación de cargo incompatible."
            - "Inscripción como candidato a elección popular."
            - "Renuncia aceptada."
            - "Remoción por el Presidente."
            - "Destitución por acuerdo del Senado (art. 53 N° 1 CPR)."
        Otras_Reglas_Comunes:
          - "Delegados ejercen funciones principalmente en capital regional/provincial, pudiendo hacerlo transitoriamente en otras localidades."
          - "Pueden requerir información a jefes de organismos sujetos a su fiscalización; éstos deben responder oportunamente."
          - "Deben informar a Contraloría y tribunales hechos que puedan implicar responsabilidad de funcionarios de instituciones fiscalizadas."
          - "Servicio de Gobierno Interior apoya sus funciones y las de SEREMI y Departamentos Provinciales de Seguridad Pública."

    Gobierno_Regional_y_Administracion_Region:
      ID: LEY-19175-GORE-ORG-01
      Naturaleza_y_Objeto:
        ID: LEY-19175-ART13-15-RESUMEN
        Fnd: "Art. 13 a 15 LOCGORE."
        Def:
          - "La administración superior de cada región está radicada en un Gobierno Regional (GORE)."
          - "GORE tiene personalidad jurídica de derecho público y patrimonio propio."
        Objeto:
          - "Desarrollo social, cultural y económico de la región."
        Ejercicio_Competencias:
          - "Puede ejercer funciones directamente o con colaboración de otros órganos de la Administración del Estado."
        Regimen_Financiero:
          - "Se rige por D.L. N° 1.263/1975 y normas de administración financiera del Estado."
          - "Nuevas funciones deben señalar fuente de financiamiento y contemplar recursos para su ejercicio."
        Principios_Desarrollo:
          - "Debe promover desarrollo armónico y equitativo de territorios en dimensiones económica, social y cultural."
          - "Debe inspirarse en equidad, eficiencia, eficacia, participación regional y protección del medio ambiente, en coherencia con Ley N° 18.575."
        Sede:
          - "Tiene su sede en la capital regional, pudiendo ejercer funciones transitoriamente en otras localidades."

      Funciones_y_Competencias_Generales:
        ID: LEY-19175-FUNC-GENERALES-01
        Fnd: "Art. 16, 18, 19 y 20 LOCGORE."
        Desarrollo_y_Planificacion:
          - "Diseñar, elaborar, aprobar y aplicar políticas, planes, programas y proyectos de desarrollo regional, coherentes con presupuesto, Estrategia Regional de Desarrollo e instrumentos comunales."
          - "Realizar estudios, análisis y proposiciones sobre desarrollo regional."
          - "Orientar desarrollo territorial en coordinación con servicios públicos y municipalidades."
          - "Elaborar y aprobar el proyecto de presupuesto regional, conforme orientaciones de Ley de Presupuestos y atribuciones del Gobernador Regional."
        Gestion_Recursos_y_Inversion:
          - "Administrar fondos y programas de aplicación regional."
          - "Decidir inversión de recursos del FNDR y otros que procedan, según normativa."
          - "Decidir destinación a proyectos específicos de programas de inversión sectorial de asignación regional."
          - "Convenir programas anuales/plurianuales de inversión con ministerios, servicios, municipalidades u otros GORE."
        Normacion_y_Coordinacion:
          - "Dictar normas generales para materias de su competencia, sujetas a toma de razón de Contraloría y publicación en Diario Oficial."
          - "Aplicar políticas definidas en la Estrategia Regional de Desarrollo."
          - "Aprobar instrumentos de planificación territorial (planes regionales de ordenamiento, reguladores metropolitanos/intercomunales, comunales y seccionales) y planes de inversiones en movilidad y espacio público."
          - "Mantener relación permanente con el gobierno nacional y sus organismos para armonizar funciones."
        Fomento_Productivo_y_Social:
          - "Formular políticas regionales de fomento productivo, innovación, ciencia y tecnología aplicada."
          - "Establecer prioridades en fomento productivo e innovación para la competitividad."
          - "Aprobar plan regional de desarrollo turístico."
          - "Promover investigación científica, educación superior y media técnico-profesional."
          - "Establecer prioridades para erradicación de la pobreza y coordinar acciones de acceso a programas sociales."
          - "Distribuir recursos a municipalidades para programas sociales."
          - "Fomentar cultura, patrimonio, etnias originarias y deporte, promoviendo identidad regional."
        Obras_y_Servicios:
          - "Construir, reponer, conservar y administrar pavimentación de aceras y calzadas urbanas con recursos asignados, pudiendo celebrar convenios con municipalidades u otros órganos."
          - "Elaborar y aprobar planes de inversiones en infraestructura de movilidad y espacio público asociados a planes reguladores metropolitanos/intercomunales."
          - "Adoptar medidas frente a emergencias o catástrofes y desarrollar programas de prevención y protección ante desastres."
        Cambio_Climatico:
          - "Coparticipar con el Comité Regional para el Cambio Climático en instrumentos regionales de gestión del cambio climático."
        Coherencia_Politicas_Nacionales:
          - "Funciones generales, de ordenamiento territorial, fomento y desarrollo social/cultural (incluidas transferidas) deben ser coherentes con políticas públicas nacionales, actuando coordinadamente y evitando duplicidades (art. 20 bis)."

      Ordenamiento_Territorial:
        ID: LEY-19175-ORD-TERR-01
        Fnd: "Art. 17 LOCGORE."
        Plan_Regional_Ordenamiento_Territorial:
          ID: LEY-19175-PROT-01
          Def: "Instrumento que orienta el uso del territorio regional para el desarrollo sustentable mediante lineamientos estratégicos y macrozonificación."
          Req:
            - "Coherencia con Estrategia Regional de Desarrollo, política nacional de ordenamiento territorial, estrategia climática de largo plazo y plan de acción regional de cambio climático."
            - "Establece condiciones vinculantes de localización para disposición de residuos y para infraestructura y actividades productivas en zonas no urbanizadas, incluyendo áreas de localización preferente."
            - "Reconoce áreas bajo protección oficial según legislación especial."
            - "Es obligatorio para ministerios y servicios públicos que operen en la región."
            - "No puede regular materias que excedan territorio regional ni áreas sometidas a planificación urbanística."
          Proc_Elaboracion:
            Steps:
              - "Diagnóstico de características, tendencias, restricciones y potencialidades del territorio regional."
              - "Consulta pública mínima de 60 días sobre imagen objetivo y elementos de estructuración territorial, con consulta paralela a municipalidades y organismos del GORE."
              - "Convocatoria difundida al menos en un medio nacional y uno regional."
              - "Ajuste a Párrafo 1° bis del Título II de la Ley N° 19.300 (Medio Ambiente)."
              - "Evaluación y eventual actualización en ciclos no superiores a 10 años."
          Rol_Comision_Interministerial:
            Def: "Comisión Interministerial de Ciudad, Vivienda y Territorio propone políticas nacionales de ordenamiento territorial y reglamentos de procedimientos aplicables al PROT."
            Ctx: "Conformada por Ministros de Vivienda y Urbanismo (preside), Interior y Seguridad Pública, Segpres, Economía, Desarrollo Social, Obras Públicas, Agricultura, Minería, Transportes y Telecomunicaciones, Bienes Nacionales, Energía y Medio Ambiente."
            Tareas:
              - "Proponer políticas nacionales de ordenamiento territorial y desarrollo rural/urbano."
              - "Proponer reglamentos sobre contenidos mínimos, procedimientos, consulta pública e indicadores."
          Zonificacion_Borde_Costero:
            Act:
              - "GORE propone zonificación del borde costero y sus modificaciones, coherente con política nacional existente."
              - "Zonificación se aprueba por decreto supremo del Ministerio de Defensa Nacional y se reconoce en el PROT."

    Transferencia_de_Competencias:
      ID: LEY-19175-TRANSF-COMP-01
      Fnd: "Art. 21 bis a 21 octies LOCGORE."
      Def:
        - "El Presidente puede transferir, temporal o definitivamente, competencias de ministerios y servicios públicos a uno o más GORE en materias de ordenamiento territorial, fomento productivo y desarrollo social/cultural."
      Principios:
        - "Transferencias se priorizan cuando la decisión regional mejora calidad y oportunidad de decisiones y adecua mejor la política nacional al territorio, sin perjudicar a otras regiones."
        - "Toda transferencia debe considerar recursos económicos y de personal suficientes, evitar duplicidad de funciones y respetar plazos mínimos (al menos 1 año si es temporal)."
      Procedimientos:
        - "Puede iniciarse a solicitud del GORE (con mayorías del Consejo Regional y rol del Gobernador) o de oficio por el Presidente."
        - "Intervienen un Comité Interministerial de Descentralización y Comisiones de Estudio paritarias (administración central–GORE)."
        - "Se establece un decreto de transferencia que detalla competencias, recursos, condiciones, gradualidad, mecanismos de seguimiento y evaluación."
        - "Plazo máximo del procedimiento: 6 meses desde la solicitud o instrucción presidencial."
      Evaluacion:
        - "Un Consejo de Evaluación de Competencias (paritario) evalúa el ejercicio de competencias transferidas (al término del período temporal o a los 3 años si son definitivas), con indicadores cualitativos y cuantitativos y recomendaciones."
        - "Puede proponer áreas de capacitación y asistencia técnica; indicadores se pueden integrar a programas de mejoramiento de la gestión (Ley N° 19.553)."
      Revocacion:
        - "Competencias transferidas definitivamente sólo pueden revocarse por ley."
        - "Transferencias temporales pueden revocarse de oficio o a solicitud del GORE por incumplimiento de condiciones, deficiente prestación del servicio o incompatibilidad con nuevas políticas nacionales (tras un plazo de adecuación)."
        - "La revocación se resuelve por decreto supremo del Ministerio del Interior y Seguridad Pública, suscrito además por Hacienda, Segpres y ministro sectorial, con vigencia a contar del 1 de enero del año siguiente."

  Ley_18834_Estatuto_Administrativo:
    ID: LEY-18834-MASTER-01
    Purp: "Regular las relaciones entre el Estado y el personal de las instituciones regidas por el Estatuto Administrativo, incluyendo a los funcionarios de los GORE."

    Alcance:
      ID: LEY-18834-ALCANCE-01
      Def:
        - "Aplica a las relaciones entre el Estado y el personal de los órganos e instituciones señalados en el artículo 1º de la ley (Administración Central y servicios públicos)."
        - "GORE y sus funcionarios quedan sometidos a este régimen general, salvo estatutos especiales que se les apliquen."

    Conceptos_Claves_Titulo_I:
      ID: LEY-18834-T1-CONCEPTOS-01
      Def:
        - "Cargo Público: Empleo contemplado en las plantas o empleos a contrata de las instituciones del artículo 1º."
        - "Planta de Personal: Conjunto de cargos permanentes asignados por ley a una institución."
        - "Empleo a Contrata: Cargo de carácter transitorio dentro de la dotación de una institución."
        - "Sueldo: Retribución fija asignada a un empleo según su clasificación."
        - "Remuneración: Contraprestación en dinero por el empleo (sueldo más asignaciones)."
        - "Carrera Funcionaria: Sistema integral que regula el empleo público, basado en igualdad de oportunidades, dignidad de la función, capacitación, ascenso, estabilidad y objetividad en calificaciones."

      Normas_Generales_Relevantes:
        ID: LEY-18834-T1-NORMAS-GENERALES-01
        Fnd: "Art. 1 a 3 Ley 18.834."
        Req:
          - "Personal se rige por el Estatuto Administrativo, salvo excepciones establecidas en el artículo 21 de la Ley N° 18.575."
          - "Los cargos de planta y a contrata sólo pueden destinarse al cumplimiento de funciones propias de las instituciones del artículo 1º."
          - "Se prohíbe utilizar cargos públicos para actividades ajenas a la función pública o en beneficio del sector privado."
        Just:
          - "Establece la base estatutaria común para funcionarios de Ministerios, servicios y Gobiernos Regionales, articulando la carrera funcionaria y la regulación de deberes, derechos y responsabilidades."

      Plantas_Cargos_y_Contratas:
        ID: LEY-18834-PLANTAS-01
        Fnd: "Art. 4 a 11 Ley 18.834."
        Def:
          - "Las plantas de personal se estructuran en estamentos (Directivos, Profesionales, Técnicos, Administrativos, Auxiliares), con cargos de planta (titulares), suplentes, subrogantes y empleos a contrata."
        Cpt:
          - "Titulares: Funcionarios nombrados en cargos vacantes de planta."
          - "Suplentes: Designados para reemplazar cargos vacantes o ausencias prolongadas del titular, con derecho a remuneración, dentro de límites de duración y presupuesto."
          - "Subrogantes: Funcionarios que ocupan temporalmente el cargo por mandato legal (reglas de subrogación interna)."
          - "Empleos a contrata: Cargos transitorios que duran hasta el 31 de diciembre de cada año, renovables, con tope porcentual respecto de la planta (20%) y reglas sobre grado, jornada y remuneración."
          - "Honorarios: Profesionales o técnicos contratados para labores accidentales, regidos por contrato civil y no por el Estatuto Administrativo."

      Ingreso_y_Carrera_Funcionaria:
        ID: LEY-18834-CARRERA-01
        Fnd: "Art. 12 a 29 Ley 18.834 (Título II de la Carrera Funcionaria)."
        Requisitos_Ingreso:
          - "Cumplir requisitos generales: nacionalidad o residencia, salud compatible, nivel educacional/título exigido, no haber sido cesado por calificación deficiente o medida disciplinaria dentro de plazos legales, no estar inhabilitado ni condenado por crimen o delito grave (con reglas especiales para estamentos auxiliares/administrativos)."
          - "Acreditar requisitos mediante documentos oficiales, certificaciones de salud y declaraciones juradas, con sanciones penales en caso de falsedad."
        Ingreso_Por_Concurso:
          - "Ingreso a la carrera funcionaria se realiza, en general, por concurso público al último grado de la planta, salvo que existan vacantes superiores no provistas por promoción."
          - "Concurso: procedimiento técnico y objetivo que evalúa estudios, experiencia y aptitudes, con reglas sobre ponderación, puntajes mínimos y actas de resultados."
          - "Avisos de concurso deben publicarse en el Diario Oficial, con plazos mínimos de postulación y especificación detallada de requisitos y antecedentes."
          - "Comités de selección proponen ternas (u otros listados acotados) a la autoridad nombrante; se regulan causales de desierto y duración de listas de elegibles."
        Empleo_a_Prueba:
          - "La ley contempla un sistema de empleo a prueba, optativo para el jefe superior del servicio, con duración acotada (3 a 6 meses), evaluación obligatoria y posibilidad de cese si el desempeño es deficiente."
          - "Finalizado satisfactoriamente el período de prueba, el funcionario puede ser designado titular en el cargo."
        Capacitacion:
          - "Se define la capacitación como actividad permanente y sistemática de desarrollo de conocimientos y destrezas para un desempeño eficiente."
          - "Se distinguen tipos de capacitación: para promoción (habilita para cargos superiores), de perfeccionamiento (mejora desempeño en el cargo) y voluntaria (interés institucional, sin vínculo directo con ascenso)."
          - "Los programas de capacitación y la asignación de recursos deben responder a necesidades institucionales, priorizando tipos de capacitación y fomentando esquemas desconcentrados y convenios con organismos públicos o privados."
        Calificaciones:
          - "Sistema de calificación anual que evalúa desempeño y aptitudes de todos los funcionarios (incluidos a contrata), clasificándolos en listas de distinción, buena, condicional y eliminación; estas listas son base para promociones, estímulos y eventuales retiros."
          - "Las Juntas Calificadoras (regionales o central, según número de funcionarios) son responsables de la calificación, utilizando precalificaciones del jefe directo, hojas de vida y anotaciones de mérito y demérito."
          - "Existen reglas precisas sobre períodos evaluados, plazos del proceso, prohibiciones de calificar a ciertos altos cargos, recursos de apelación, confección del escalafón y efectos de permanecer en listas de desempeño deficiente (lista 4 o permanencia reiterada en lista 3)."
        Promociones:
          - "La promoción se efectúa, según estamento, mediante concursos internos (directivos, profesionales, fiscalizadores, técnicos) o ascensos automáticos basados en escalafón (administrativos y auxiliares)."
          - "Los concursos de promoción ponderan factores como capacitación, evaluación de desempeño, experiencia y aptitudes, y requieren que los candidatos estén bien calificados (listas de distinción o buena) y sin sanciones recientes."
          - "Se reconoce el derecho al ascenso respetando el orden del escalafón, con preferencias para funcionarios de grado inmediatamente inferior y reglas de inhabilidad para quienes no cumplan estándares de probidad o desempeño."

      Obligaciones_Funcionarias:
        ID: LEY-18834-T3-OBLIGACIONES-01
        Fnd: "Art. 61 a 88 Ley 18.834 (Título III de las Obligaciones Funcionarias)."
        Obligaciones_Generales:
          - "Desempeñar las funciones de manera regular, orientando el trabajo al cumplimiento de los objetivos institucionales, con esmero y eficiencia."
          - "Cumplir la jornada de trabajo y los trabajos extraordinarios que se ordenen legítimamente, salvo causas justificadas."
          - "Obedecer las órdenes de los superiores jerárquicos; si se estiman ilegales, representarlas por escrito y sólo cumplirlas si son reiteradas, quedando la responsabilidad en el superior."
          - "Observar en todo momento el principio de probidad administrativa, guardar secreto respecto de asuntos reservados y mantener una conducta pública y privada acorde con la dignidad del cargo."
          - "Denunciar a la autoridad competente los delitos y faltas administrativas de que tomen conocimiento en el ejercicio de sus funciones y rendir cuenta de los fondos o bienes públicos a su cargo."

        Jornada_y_Trabajo_Extraordinario:
          - "La jornada ordinaria de trabajo es, en general, de 44 horas semanales distribuidas de lunes a viernes, con un máximo diario de 9 horas, permitiéndose jornadas parciales con remuneración proporcional."
          - "El trabajo extraordinario debe ser expresamente ordenado para la atención de tareas impostergables y se compensa, preferentemente, con descanso complementario; si ello no es posible, se pagan recargos sobre la remuneración."
          - "Se definen reglas sobre trabajo nocturno y en fines de semana, con porcentajes de descanso o recargo diferenciados, y prohibiciones específicas de trabajo en ciertas tardes (17 de septiembre, 24 y 31 de diciembre), salvo situaciones de excepción."

        Destinaciones_Comisiones_y_Subrogacion:
          - "Las destinaciones permiten cambiar al funcionario de localidad o unidad dentro de la misma institución, respetando jerarquía y con reglas especiales cuando ambos cónyuges son funcionarios."
          - "Las comisiones de servicio autorizan el desempeño temporal de funciones distintas o en otros órganos, dentro o fuera del país, con límites de duración, exigencia de interés público y requisitos formales (decreto o resolución)."
          - "Los cometidos funcionarios regulan desplazamientos específicos para cumplir tareas puntuales, generando derecho a viáticos y pasajes cuando corresponda."
          - "La subrogación opera cuando el cargo no es desempeñado por su titular o suplente, pasando a ser ejercido por el funcionario que le sigue en el orden jerárquico, con reglas sobre derecho al sueldo del cargo subrogado cuando la subrogación es prolongada."

        Prohibiciones_e_Incompatibilidades:
          - "Se prohíbe ejercer facultades que no hayan sido delegadas, intervenir en asuntos en que el funcionario o sus parientes cercanos tengan interés directo o litigar contra el Estado, salvo defensa de derechos propios o de dichos parientes."
          - "Existe incompatibilidad para que cónyuges o parientes cercanos se encuentren en relación de subordinación directa dentro de un mismo servicio, debiendo destinarse al subalterno a otras funciones cuando esto ocurra."
          - "Regla general de incompatibilidad entre empleos afectos al Estatuto Administrativo y otros cargos públicos o de elección popular, con excepciones limitadas (docencia con tope de horas, funciones a honorarios fuera de la jornada, participación en ciertos consejos de organismos públicos, suplencias y contratas, y cargos directivos en educación superior estatal)."
          - "La compatibilidad de remuneraciones no exime el cumplimiento integro de la jornada ni de las demás obligaciones funcionarias, y determinadas combinaciones obligan a optar por una sola remuneración."

      Derechos_Funcionarios:
        ID: LEY-18834-T4-DERECHOS-01
        Fnd: "Art. 89 a 118 Ley 18.834 (Título IV de los Derechos Funcionarios)."
        Derechos_Generales:
          - "Derecho a la estabilidad en el empleo, al ascenso en el escalafón (salvo cargos de exclusiva confianza), a participar en concursos, a feriados, permisos y licencias, a la capacitación y a acceder a prestaciones de previsión y bienestar social, incluyendo protección a la maternidad."
        Defensa_y_Proteccion:
          - "Derecho a que la institución ejerza acciones civiles y penales cuando, en razón de sus funciones, se atente contra la vida o integridad del funcionario, o se le injurie o calumnie, previa solicitud."
          - "Régimen especial de protección para funcionarios que denuncian irregularidades de probidad, que prohíbe suspensiones, destituciones o traslados arbitrarios durante el proceso y permite anotar méritos cuando sus denuncias resguardan el patrimonio fiscal."
          - "Reglas formales sobre cómo presentar denuncias internas (requisitos mínimos, reserva de identidad, plazos de tramitación y remisión a la autoridad competente)."
        Vivienda_y_Movilidad:
          - "Derecho a vivienda fiscal gratuita cuando la naturaleza del cargo exige permanencia en el lugar de trabajo; si el funcionario opta por residir allí sin obligación, puede hacerlo pagando una renta reducida, sujeto a requisitos jerárquicos y de propiedad en la localidad."
          - "Posibilidad de permutar cargos entre funcionarios de igual grado y que cumplan requisitos, con efectos transitorios en su posición dentro del escalafón."
        Remuneraciones_y_Asignaciones:
          - "Derecho a percibir remuneraciones y asignaciones establecidas por ley mientras se desempeñe efectivamente el cargo, con reglas sobre inicio del devengo, embargos limitados y deducciones autorizadas."
          - "Tipología de asignaciones: pérdida de caja, movilización, horas extraordinarias no compensadas, cambio de residencia, viáticos y pasajes en comisiones de servicio, entre otras que señalen leyes especiales."
          - "Reconocimiento de ciertos efectos remuneracionales asociados al servicio militar u obligaciones similares, y obligación de reintegrar valores en caso de uso indebido de derechos."
        Feriados_Permisos_y_Licencias:
          - "Feriados anuales con duración creciente según años de servicio, reglas sobre acumulación y fraccionamiento, y beneficios adicionales para funcionarios que sirven en zonas extremas o apartadas."
          - "Permisos particulares con y sin goce de remuneraciones para asuntos personales, con topes anuales y facultad discrecional de la jefatura para concederlos según necesidades del servicio."
          - "Licencias médicas como derecho a ausentarse o reducir jornada por motivos de salud, con goce de remuneraciones y especial protección en licencias maternales y postnatales, más efectos de la declaración de irrecuperabilidad para el vínculo funcionarial."
        Prestaciones_Sociales:
          - "Prestaciones en caso de fallecimiento del funcionario (pago de remuneraciones hasta fin de mes y beneficios a familiares prioritarios)."
          - "Asistencia médica integral y pensiones especiales en casos de accidentes en acto de servicio o enfermedades profesionales, incluyendo gastos de traslado y apoyo a la familia."
          - "Derecho a afiliarse a servicios de bienestar y a percibir asignaciones familiares y maternales conforme a la legislación general."

      Responsabilidad_Administrativa:
        ID: LEY-18834-T5-RESP-ADM-01
        Fnd: "Art. 119 a 145 Ley 18.834 (Título V de la Responsabilidad Administrativa)."
        Concepto_y_Ambito:
          - "La responsabilidad administrativa se configura cuando el funcionario infringe sus obligaciones funcionarias, lo que puede dar lugar a anotaciones de demérito y a la aplicación de sanciones disciplinarias, sin perjuicio de la responsabilidad civil o penal que proceda."
          - "La tramitación disciplinaria se rige por los principios de confidencialidad, imparcialidad, celeridad y, en los casos de acoso y violencia, por un enfoque con perspectiva de género y protección a las víctimas y denunciantes."
        Sanciones_Disciplinarias:
          - "Las sanciones principales son: censura escrita, multa (porcentaje de la remuneración), suspensión del empleo con reducción de remuneraciones y destitución del cargo."
          - "La determinación de la sanción debe considerar la gravedad de la falta, los antecedentes del funcionario y la existencia de atenuantes o agravantes, entre las que se incluye la cooperación eficaz para esclarecer los hechos e identificar a otros responsables."
          - "Para ciertos hechos de probidad particularmente graves, la destitución es obligatoria y no proceden determinadas atenuantes; la sanción puede generar inhabilidades para reingresar a la Administración."
        Investigacion_Sumaria_y_Sumario:
          - "Frente a presuntos hechos sancionables, la autoridad puede ordenar una investigación sumaria para verificar con rapidez la existencia de la infracción y los responsables, con plazos breves para informes, descargos y resolución, y recursos de reposición y apelación."
          - "Cuando la gravedad de los hechos lo amerita, o la investigación sumaria lo revela, debe instruirse un sumario administrativo formal, designando un fiscal de grado igual o superior al inculpado y un actuario que actúa como ministro de fe."
          - "El sumario comprende etapas de formulación de cargos, recepción de descargos y prueba, dictamen del fiscal proponiendo absolución o sanción y resolución de la autoridad; rigen reglas estrictas de notificación, foliación de actuaciones y custodia del expediente."
          - "Durante el sumario pueden adoptarse medidas cautelares, como la suspensión o destinación transitoria del funcionario inculpado, especialmente en casos de acoso, violencia o riesgos para la seguridad de la víctima, sin perjuicio de la posterior restitución de remuneraciones si resulta absuelto."
        Garantias_y_Recursos:
          - "El procedimiento disciplinario asegura el derecho del inculpado a ser notificado de los cargos, a presentar descargos y prueba, a contar con patrocinio letrado y a impugnar sanciones mediante recursos administrativos."
          - "Los recursos típicos son la reposición ante la misma autoridad que dictó la resolución y la apelación subsidiaria ante el superior jerárquico, los que deben interponerse fundadamente dentro de plazos breves y ser resueltos en un término igualmente acotado."
          - "Los vicios formales del procedimiento sólo afectan la validez de la sanción cuando influyen decisivamente en el resultado del sumario; en caso contrario, se consideran inofensivos."
        Coordinacion_con_Otras_Responsabilidades:
          - "La responsabilidad administrativa es independiente de las responsabilidades civil y penal: la existencia de archivo, suspensión condicional, acuerdos reparatorios, prescripción o incluso condena o absolución penal no impiden la adopción de medidas disciplinarias, salvo los efectos restitutivos que la ley expresamente reconoce."
          - "En los casos más graves, el fiscal debe proponer remitir los antecedentes al Ministerio Público o a los tribunales competentes para la persecución penal de los hechos."
          - "Determinadas resoluciones relacionadas con denuncias de hechos de probidad (especialmente las que absuelven o aplican medidas disciplinarias en órganos de primer nivel) requieren toma de razón de la Contraloría General de la República y sólo pueden ejecutarse vencidos los plazos legales de reclamación."

  Ley_19880_Procedimiento_Administrativo:
    ID: LEY-19880-MASTER-01
    Purp: "Establecer las bases del procedimiento administrativo común aplicable a los órganos de la Administración del Estado, incluidos los Gobiernos Regionales."
    Fnd: "Ley N° 19.880."

    Alcance_y_Conceptos_Claves:
      ID: LEY-19880-ALCANCE-01
      Def:
        - "Se aplica a los procedimientos administrativos de los órganos y organismos enumerados en su artículo 2° (Ministerios, Gobiernos Regionales, municipalidades, servicios públicos, Contraloría, FF.AA. y de Orden, entre otros)."
        - "Opera como régimen supletorio frente a procedimientos especiales establecidos en leyes sectoriales, salvo que éstos dispongan algo distinto de forma expresa."
      Acto_Administrativo:
        ID: LEY-19880-ACTO-ADM-01
        Ref: DEF-ACTO-ADMINISTRATIVO-01
        Def:
          - "Precisa que el acto administrativo se formaliza, principalmente, mediante decretos supremos y resoluciones, y que goza de presunción de legalidad, imperio y exigibilidad desde su entrada en vigencia, salvo suspensión por autoridad administrativa o judicial."

    Principios_Del_Procedimiento:
      ID: LEY-19880-PRINCIPIOS-01
      Fnd: "Art. 4 a 17 Ley 19.880."
      Principios_Generales:
        - "Escrituracion: todo procedimiento y acto administrativo debe constar por escrito, preferentemente mediante medios electrónicos, salvo excepciones legales."
        - "Gratuidad: las actuaciones y documentos del procedimiento son gratuitos para los interesados, sin cobros entre órganos salvo autorización legal."
        - "Celeridad y Economia Procedimental: la Administración debe impulsar de oficio el procedimiento, remover obstáculos, evitar trámites dilatorios y decidir en un solo acto las cuestiones que puedan resolverse conjuntamente."
        - "Conclusividad e Inexcusabilidad: los procedimientos deben concluir con un acto decisorio fundado; la Administración no puede excusarse de resolver."
        - "Contradictoriedad e Imparcialidad: los interesados pueden formular alegaciones y aportar pruebas; el órgano debe asegurar igualdad de armas, objetividad y probidad."
        - "Abstencion y No Formalizacion: autoridades y funcionarios deben abstenerse cuando exista conflicto de interés; sólo se exigen formalidades indispensables y los vicios formales solo invalidan si afectan requisitos esenciales y causan perjuicio."
        - "Impugnabilidad y Transparencia/Publicidad: los actos son, en general, impugnables y públicos, salvo excepciones de ley de transparencia u otras normas de quórum calificado."
      Principios_Medios_Electronicos_y_Derechos:
        - "Principios relativos a medios electrónicos: neutralidad tecnológica, actualización de plataformas, equivalencia funcional entre firma electrónica y manuscrita, fidelidad del expediente electrónico, interoperabilidad y cooperación entre órganos."
        - "Derechos de las personas frente a la Administración: conocer el estado de tramitación, obtener copias, identificar autoridades, no presentar documentos que obren en poder de la Administración, formular alegaciones, exigir responsabilidades y recibir un trato respetuoso y facilitador."

    Procedimiento_Administrativo_General:
      ID: LEY-19880-PROC-GENERAL-01
      Expediente_y_Soporte_Electronico:
        Def:
          - "El procedimiento se documenta en un expediente (preferentemente electrónico) donde se incorporan cronológicamente escritos, documentos, actos, notificaciones y resoluciones, con registro de fecha y hora de ingreso y envío."
          - "Los órganos deben disponer de plataformas electrónicas que aseguren integridad, disponibilidad, autenticidad y conservación de los expedientes, con reglas especiales para digitalización de documentos en papel y para personas sin acceso a medios tecnológicos."
      Sujetos_y_Representacion:
        Def:
          - "Pueden intervenir quienes tengan capacidad conforme a las normas generales; se reconoce la figura del interesado (quien promueve el procedimiento o puede ver afectados sus derechos o intereses)."
          - "Los interesados pueden actuar por medio de apoderados con poderes suficientes, otorgados incluso mediante firma electrónica, con mayores exigencias para actos solemnes."
      Plazos_y_Interoperabilidad:
        Def:
          - "Todos los intervinientes (autoridades, personal e interesados) deben respetar los plazos legales; se regulan plazos específicos para enviar antecedentes, emitir informes, dictar providencias de mero trámite y resolver definitivamente, con responsabilidad por prolongaciones injustificadas."
          - "Los plazos se computan en días hábiles, con reglas sobre cómputo, prórroga, ampliación justificada y un límite máximo general de 6 meses entre iniciación y decisión, salvo caso fortuito o fuerza mayor."
          - "Se fomenta la interoperabilidad entre órganos para remitir electrónicamente antecedentes y evitar exigir documentos que ya obran en poder de la Administración, respetando la protección de datos personales."
      Inicio_Instruccion_y_Terminacion:
        Def:
          - "El procedimiento puede iniciarse de oficio (iniciativa propia, orden superior, petición de otros órganos, denuncia) o a solicitud de parte, la que debe contener requisitos mínimos (identificación, hechos, peticiones, medio electrónico de contacto, etc.)."
          - "Si la solicitud es incompleta, la Administración debe requerir su subsanación dentro de un breve plazo, bajo apercibimiento de tenerla por no presentada si no se corrige."
          - "Durante la instrucción se pueden adoptar medidas provisionales para asegurar la eficacia de la resolución final, practicar actos de instrucción, recibir y valorar prueba, solicitar informes y abrir períodos de información pública cuando la naturaleza del asunto lo requiera."
          - "El procedimiento termina, en general, mediante resolución final fundada que decide todas las cuestiones planteadas, o bien por desistimiento, renuncia, abandono o imposibilidad material sobrevenida, debidamente declarados."

    Publicidad_Ejecutoriedad_y_Revisiones:
      ID: LEY-19880-PUBLICIDAD-REVISION-01
      Notificacion_y_Publicacion:
        Def:
          - "Los actos administrativos individuales deben notificarse íntegramente a los interesados dentro de plazos breves, preferentemente mediante medios electrónicos asociados a domicilios digitales; se prevén mecanismos supletorios (carta certificada, comparecencia en oficinas) y reglas sobre notificación tácita."
          - "Determinados actos (normas generales, actos de interés general o dirigidos a un número indeterminado de personas, y aquellos cuyos destinatarios tienen paradero ignorado) deben publicarse en el Diario Oficial, adquiriendo plena autenticidad y obligatoriedad desde su publicación."
      Ejecutoriedad_Retroactividad_y_Titulo_Ejecutorio:
        Def:
          - "Como regla general, los actos administrativos son inmediatamente ejecutorios una vez notificados o publicados, sin necesidad de declaración adicional, salvo que la ley exija aprobación o que se disponga lo contrario."
          - "Se prohíbe la retroactividad de los actos administrativos, salvo cuando produzcan efectos favorables para los interesados y no lesionen derechos de terceros."
          - "No pueden ejecutarse materialmente medidas que limiten derechos sin una resolución previa que las autorice expresamente (título ejecutorio)."
      Invalidacion_y_Revisiones_Oficiosas:
        Def:
          - "La Administración puede invalidar de oficio o a petición de parte los actos contrarios a derecho dentro de un plazo general de 2 años desde su notificación o publicación, previa audiencia de los interesados y con posibilidad de control judicial posterior."
          - "La revocación de actos válidos está permitida en ciertos casos, pero no procede respecto de actos declarativos de derechos o cuando la ley establece formas específicas de extinción."
          - "Los órganos pueden aclarar en cualquier momento puntos dudosos o errores materiales de sus actos, sin alterar el fondo de lo decidido."

    Recursos_y_Silencio_Administrativo:
      ID: LEY-19880-RECURSOS-SILENCIO-01
      Recursos_Ordinarios_y_Extraordinarios:
        Def:
          - "Los principales recursos administrativos son la reposición (ante el mismo órgano) y el jerárquico (ante el superior), que deben interponerse dentro de plazos breves y permiten modificar, reemplazar o dejar sin efecto el acto impugnado, con reglas sobre suspensión excepcional de sus efectos."
          - "En ciertos casos existe un recurso extraordinario de revisión frente a resoluciones firmes cuando concurren causales graves (falta de emplazamiento, error de hecho manifiesto, prevaricación, falsedad de documentos, etc.), dentro de plazos acotados."
          - "Mientras haya una reclamación administrativa pendiente, se suspende el ejercicio de acciones jurisdiccionales sobre el mismo asunto, y la interposición de la acción judicial impide continuar con la vía administrativa por la misma causa."
      Procedimiento_de_Urgencia:
        Def:
          - "El procedimiento de urgencia permite reducir a la mitad la mayoría de los plazos cuando el interés público lo exige, sin admitir recursos contra la decisión que lo declare."
      Silencio_Administrativo:
        Def:
          - "La ley regula tanto el silencio positivo (en ciertos casos, la falta de resolución en plazo produce la aceptación de la solicitud del interesado, con certificación correspondiente) como el silencio negativo (en otras materias, la falta de respuesta equivale a rechazo, habilitando la interposición de recursos)."
          - "Los efectos del silencio se equiparan, en lo sustancial, a los de una resolución expresa desde la fecha en que se entiende configurado, debiendo dejar constancia formal mediante certificados o anotaciones en el expediente."

  Ley_20880_Probidad_y_Conflictos_de_Interes:
    ID: LEY-20880-MASTER-01
    Purp: "Reforzar el régimen de probidad, transparencia y prevención de conflictos de interés mediante la regulación de la Declaración de Intereses y Patrimonio (DIP), mandatos especiales de administración y enajenación obligatoria de ciertos bienes."
    Fnd: "Ley N° 20.880, publicada el 5 de enero de 2016."

    Normas_y_Principios_Generales:
      ID: LEY-20880-GENERAL-01
      Ref:
        - DEF-PROBIDAD-ADMINISTRATIVA-01
        - DEF-CONFLICTO-DE-INTERESES-01
      Def:
        - "La ley complementa y actualiza el régimen general de probidad de la Ley 18.575 y del Estatuto Administrativo, sin reemplazarlos, detallando obligaciones específicas de transparencia patrimonial y gestión de intereses."
        - "Focaliza sus exigencias en autoridades políticas y directivas (incluidos Gobernadores Regionales, Consejeros Regionales y jefaturas del GORE), así como en funcionarios de fiscalización y profesionales de alto nivel, donde el riesgo de conflicto de interés es mayor."

    Declaracion_Intereses_y_Patrimonio_DIP:
      ID: LEY-20880-DIP-01
      Sujetos_Obligados_GORE:
        Def:
          - "Deben presentar DIP, al menos: Gobernadores Regionales, Consejeros Regionales, jefes superiores de servicio y directivos del GORE hasta el tercer nivel jerárquico, funcionarios de fiscalización directa y profesionales/técnicos de planta o a contrata hasta ese mismo nivel."
          - "También deben declarar las personas a honorarios que ejerzan funciones directivas en el GORE con remuneración igual o superior a la de un funcionario del tercer nivel jerárquico."
      Plazos_DIP:
        Def:
          - "Dentro de los 30 días siguientes a la asunción del cargo."
          - "Actualización anual durante el mes de marzo."
          - "Dentro de los 30 días siguientes a la cesación en funciones."
      Forma_y_Publicidad:
        Def:
          - "La DIP se presenta en formato electrónico ante la Contraloría General de la República (CGR) y tiene carácter de declaración jurada."
          - "Es, en principio, pública: se publica en el sitio web de la institución y en la plataforma que disponga el órgano garante de transparencia, resguardando datos personales sensibles (domicilio particular, RUT, etc.)."
          - "La publicidad de las DIP permite el escrutinio ciudadano y mediático respecto de eventuales conflictos de interés de las autoridades regionales."
      Contenido_y_Extension_Familiar:
        Def:
          - "Debe incluir, al menos: actividades profesionales y económicas recientes, bienes inmuebles, derechos de aguas y concesiones, bienes muebles registrables, acciones y otros valores, mandatos de administración de cartera y pasivos significativos."
          - "La declaración comprende obligatoriamente los bienes del cónyuge en régimen de sociedad conyugal y, en general, los bienes de los hijos sujetos a patria potestad, con ciertas restricciones de publicidad según el tipo de autoridad."

    Fiscalizacion_y_Sanciones_DIP:
      ID: LEY-20880-DIP-SANCIONES-01
      Rol_CGR_y_Autoridades_GORE:
        Def:
          - "El Gobernador Regional y las jefaturas superiores deben verificar que sus dependientes obligados presenten y mantengan actualizadas sus DIP, informando los incumplimientos a la CGR."
          - "La CGR fiscaliza oportunidad, integridad y veracidad de las DIP, pudiendo requerir antecedentes adicionales y cruzar información con otros registros públicos."
      Procedimiento_Sancionatorio:
        Def:
          - "Ante incumplimientos en la presentación o actualización de la DIP, la CGR apercibe al infractor para que subsane en un plazo breve; si persiste el incumplimiento, formula cargos y puede proponer la aplicación de multa (p.ej. entre 5 y 50 UTM)."
          - "El incumplimiento grave y prolongado (que se extiende varios meses pese a las sanciones) se califica como falta grave a la probidad, pudiendo conducir a la destitución del funcionario o autoridad."
          - "Las sanciones aplicadas por la CGR en esta materia son reclamables ante la Corte de Apelaciones competente."

    Mandato_Especial_y_Enajenacion:
      ID: LEY-20880-MANDATO-ENAJENACION-01
      Mandato_Especial_Administracion_Cartera:
        Def:
          - "Cuando Gobernadores Regionales o Consejeros Regionales son titulares de acciones, bonos u otros valores por sobre un umbral relevante (por ejemplo, 25.000 UF), deben optar entre constituir un mandato especial de administración de cartera (fideicomiso ciego) o enajenar la parte excedente."
          - "El mandato especial se otorga a un administrador independiente, que gestiona la cartera sin informar decisiones de inversión al mandante, reduciendo el riesgo de que decisiones públicas se vean influidas por intereses privados."
          - "El plazo para cumplir esta obligación corre, en general, desde la asunción del cargo o desde la actualización de la DIP que revela la superación del umbral."
      Enajenacion_Obligatoria_Activos_Conflictivos:
        Def:
          - "Determinadas autoridades regionales (Gobernadores, Consejeros y jefes de servicio del GORE) deben enajenar o renunciar a su participación en empresas que contratan con el Estado, tienen tarifas reguladas o explotan concesiones estatales cuando tales empresas se vinculan directamente con el ámbito de su competencia o fiscalización."
          - "La enajenación debe efectuarse dentro de plazos perentorios (por ejemplo, 120 días desde la asunción o desde que surge la incompatibilidad), de manera que se elimine el conflicto de interés estructural."
          - "Las unidades jurídicas del GORE deben revisar las DIP de las autoridades y directivos para detectar y gestionar estas incompatibilidades patrimoniales."

    Fiscalizacion_y_Sanciones_Mandato_Enajenacion:
      ID: LEY-20880-MANDATO-ENAJENACION-SANCIONES-01
      Rol_CGR:
        Def:
          - "La CGR es competente para fiscalizar el cumplimiento de las obligaciones de constituir mandatos especiales y de enajenar participaciones incompatibles, aplicando un procedimiento sancionatorio análogo al de la DIP."
          - "Las infracciones a estas obligaciones pueden ser sancionadas con multas que, según la gravedad, pueden alcanzar montos muy significativos (p.ej. entre 10 y 1.000 UTM), además de calificarse como faltas graves al principio de probidad."

    Jurisprudencia_y_Superposicion_Normativa:
      ID: LEY-20880-JURISPRUDENCIA-01
      Def:
        - "La jurisprudencia de la CGR ha precisado que las obligaciones de DIP, mandatos y enajenación alcanzan plenamente a los Consejeros Regionales, aun cuando su dedicación sea parcial, reforzando el estándar de probidad en los GORE."
        - "Esta ley se entiende complementaria de la Ley 18.575 y del Estatuto Administrativo: no elimina otros deberes de probidad ni las sanciones disciplinarias existentes, sino que los refuerza y detalla para situaciones patrimoniales y de conflicto de interés."

  Ley_21180_Transformacion_Digital_Estado:
    ID: LEY-21180-MASTER-01
    Purp: "Modernizar y digitalizar los procedimientos administrativos del Estado, estableciendo el uso obligatorio de medios electrónicos, con especial impacto en la operación de los GORE."
    Fnd: "Ley N° 21.180 sobre Transformación Digital del Estado."

    Resumen_Ejecutivo:
      ID: LEY-21180-RESUMEN-01
      Def:
        - "Establece las bases para la digitalización de los procedimientos administrativos, eliminando el papel como soporte por defecto y privilegiando el expediente electrónico."
        - "Modifica y complementa principalmente la Ley N° 19.880, incorporando obligaciones de tramitación electrónica, firma electrónica y gestión documental digital."
        - "Para los GORE, implica una transformación profunda en la forma de tramitar, resolver y archivar actos administrativos."
      Componentes_Claves:
        Def:
          - "Procedimientos electrónicos, expedientes digitales, firma electrónica, notificaciones digitales, interoperabilidad entre sistemas y archivo electrónico de documentos."
      Implicancias_Para_GORE:
        Def:
          - "Los GORE deben implementar y utilizar sistemas electrónicos en todas las fases del procedimiento administrativo (inicio, instrucción, decisión y archivo)."
          - "La validez jurídica de los actos del GORE pasa a descansar en documentos electrónicos con firma electrónica conforme a la Ley N° 19.799, no en soportes físicos."

    Principios_y_Derechos_Digitales:
      ID: LEY-21180-PRINCIPIOS-DERECHOS-01
      Principios_Procedimiento_Electronico:
        Ref: LEY-19880-PRINCIPIOS-01
        Def:
          - "Refuerza los principios específicos del procedimiento electrónico: neutralidad tecnológica, actualización continua de plataformas, equivalencia funcional del soporte electrónico frente al papel, fidelidad de la información, interoperabilidad entre sistemas y cooperación efectiva entre órganos del Estado."
      Derechos_Digitales_Interesados:
        Def:
          - "Consolida el derecho de las personas a no presentar nuevamente documentos que ya obran en poder de la Administración, obligando al GORE a obtenerlos por interoperabilidad con otros órganos."
          - "Exige que la digitalización no genere exclusión: los GORE deben ofrecer canales alternativos y apoyo a quienes carezcan de medios tecnológicos, sin menoscabar su derecho de petición."

    Obligaciones_Claves_Para_GORE:
      ID: LEY-21180-OBLIGACIONES-01
      Obligatoriedad_y_Escrituracion_Electronica:
        Def:
          - "Tramitar electrónicamente pasa de ser una opción a una obligación: la regla general es que el procedimiento y los actos administrativos del GORE se documenten y gestionen en formato electrónico."
          - "Redefine el principio de escrituración: se satisface por medios electrónicos por defecto, reservando el soporte papel para situaciones excepcionales debidamente justificadas."
      Comunicaciones_y_Expediente_Electronico:
        Def:
          - "Las comunicaciones oficiales entre el GORE y otros órganos de la Administración deben realizarse por medios electrónicos, utilizando plataformas interoperables."
          - "Las solicitudes, escritos y documentos ingresan al GORE en formato electrónico, conformando un expediente electrónico único por procedimiento, con registro cronológico de todas las actuaciones."
          - "Cuando las personas no disponen de medios tecnológicos, pueden presentar documentos en papel, los que deben ser digitalizados e incorporados inmediatamente al expediente electrónico por el funcionario a cargo."
      Plataformas_Gestion_y_Archivo:
        Def:
          - "Los GORE deben contar con plataformas electrónicas que aseguren integridad, disponibilidad, autenticidad y conservación de expedientes y documentos digitales."
          - "La gestión de archivos se desplaza al formato electrónico, incluyendo la obligación de preparar la transferencia en formato digital de documentos con valor histórico al Archivo Nacional."
      Firma_Electronica_y_Poderes:
        Def:
          - "Todos los actos y documentos administrativos del GORE deben ajustarse a la Ley N° 19.799 sobre firma electrónica; las resoluciones del Gobernador deben suscribirse con firma electrónica avanzada."
          - "Los poderes para actuar en procedimientos administrativos pueden constar en documentos electrónicos con firma simple o avanzada, según la naturaleza y solemnidad del acto."
      Notificaciones_Digitales:
        Def:
          - "Las notificaciones a los interesados se realizan, como regla general, por medios electrónicos, utilizando domicilios digitales o direcciones de correo electrónico declaradas para tal efecto."
          - "El uso de canales físicos (carta certificada, comparecencia en dependencias) se reserva para casos excepcionales o cuando el interesado lo requiera o no cuente con medios electrónicos."

    Implementacion_y_Fiscalizacion:
      ID: LEY-21180-IMPLEMENTACION-01
      Plazos_Implementacion:
        Def:
          - "La implementación del sistema de tramitación electrónica es gradual, pero no puede extenderse más allá del 31 de diciembre de 2027, salvo prórrogas o ajustes muy específicos."
      Roles_Claves:
        Def:
          - "La División de Gobierno Digital de la SEGPRES asiste y coordina, a nivel nacional, la implementación de la transformación digital, incluyendo a los GORE."
          - "La Contraloría General de la República guía y fiscaliza el cumplimiento de las obligaciones digitales, pudiendo formular cargos por rezagos injustificados o incumplimientos graves."

    Superposicion_y_Complementariedad_Normativa:
      ID: LEY-21180-OVERLAP-01
      Def:
        - "Actúa en estrecha complementariedad con la Ley N° 19.799 (Firma Electrónica), que entrega la base técnica y jurídica para la validez de los documentos y firmas electrónicas usados por el GORE."
        - "Opera como una capa de actualización tecnológica sobre la Ley N° 19.880 (Bases de Procedimientos Administrativos), cuyas disposiciones sobre procedimientos, plazos, recursos y principios deben ahora interpretarse y aplicarse en clave digital."
        - "Obliga a revisar y depurar reglamentos internos y manuales de procedimiento del GORE para eliminar referencias obsoletas a trámites en papel e incorporar la lógica de expediente y archivo electrónicos."

  Ley_20730_Lobby_y_Gestion_de_Intereses:
    ID: LEY-20730-MASTER-01
    Purp: "Regular y transparentar la interacción entre autoridades/funcionarios del GORE y particulares que buscan influir en sus decisiones, mediante reglas sobre lobby, gestión de intereses y publicidad de agendas."
    Fnd: "Ley N° 20.730 sobre Lobby y Gestión de Intereses."

    Conceptos_Fundamentales:
      ID: LEY-20730-DEFINICIONES-01
      Def:
        - "Lobby: Actividad remunerada cuyo objeto es promover, defender o representar un interés particular para influir en decisiones de las autoridades o funcionarios sujetos a la ley."
        - "Gestion_de_Interes_Particular: Actividad no remunerada que persigue el mismo fin que el lobby (influir en decisiones públicas), realizada por personas o entidades en nombre propio o de terceros."
        - "Sujetos_Pasivos: Autoridades y funcionarios del GORE y otros órganos que, por su cargo, son objeto de actividades de lobby o gestión de intereses y deben cumplir obligaciones de transparencia reforzada."
      Notas_Contexto_GORE:
        Def:
          - "La regulación de lobby se conecta con el régimen de probidad (Ley 18.575 y Ley 20.880), complementándolo con obligaciones específicas de publicidad de reuniones, viajes y donativos que pueden generar conflictos de interés o capturas indebidas."

    Sujetos_Pasivos_en_el_GORE:
      ID: LEY-20730-SUJETOS-GORE-01
      Lista_Principal:
        Def:
          - "Se consideran sujetos pasivos, al menos: Gobernadores Regionales, Consejeros Regionales, Secretarios Ejecutivos de los CORE y jefes de gabinete de estas autoridades."
          - "También son sujetos pasivos otros funcionarios que el Gobernador designe anualmente mediante resolución, cuando por su cargo tengan influencia decisiva en la toma de decisiones (por ejemplo, Jefes de División)."
      Sujetos_Externos_Relevantes:
        Def:
          - "Secretarios Regionales Ministeriales (SEREMI) y otras autoridades sectoriales en la región son sujetos pasivos bajo esta ley, aunque no formen parte orgánica del GORE, siendo contraparte frecuente en procesos de lobby vinculados a decisiones regionales."

    Actividades_Reguladas_y_Excepciones:
      ID: LEY-20730-ACTIVIDADES-01
      Actividades_Reguladas:
        Def:
          - "Se regula toda gestión destinada a influir en: la elaboración, dictación, modificación o rechazo de actos administrativos del GORE (resoluciones, reglamentos); la celebración, modificación o terminación de contratos que involucren al GORE; y el diseño, implementación o evaluación de políticas, planes y programas regionales."
      Actividades_No_Consideradas_Lobby:
        Def:
          - "No constituyen lobby: los planteamientos realizados en reuniones convocadas formalmente por la propia autoridad del GORE; las peticiones que solo buscan conocer el estado de un procedimiento; y la información proporcionada a solicitud expresa de la autoridad."

    Obligaciones_de_Transparencia_del_GORE:
      ID: LEY-20730-OBLIGACIONES-GORE-01
      Registros_y_Plataforma:
        Def:
          - "Las autoridades y funcionarios sujetos pasivos del GORE deben mantener y publicar registros actualizados de sus audiencias, reuniones, viajes y donativos vinculados a lobby o gestión de intereses."
          - "Esta información se publica y actualiza, como regla general, en la plataforma oficial `www.leylobby.gob.cl` u otros medios electrónicos que disponga la autoridad competente."
      Contenido_Minimo_Registro:
        Def:
          - "Audiencias y reuniones: identificación de quien solicita la reunión, a nombre de quién actúa, lista de asistentes, carácter remunerado o no de la gestión, lugar, fecha y materia tratada."
          - "Viajes: destino, objeto del viaje, costo total y fuente de financiamiento (especialmente si no fue con fondos públicos)."
          - "Donativos: descripción del bien recibido, valor estimado, fecha, ocasión y origen del donativo."
      Principios_Transparencia_e_Igualdad:
        Def:
          - "Las autoridades del GORE deben otorgar trato igualitario a quienes soliciten audiencias sobre una misma materia, evitando discriminaciones arbitrarias en el acceso a la decisión pública."

    Obligaciones_de_Lobbistas_y_Gestores:
      ID: LEY-20730-OBLIGACIONES-LOBBYISTAS-01
      Def:
        - "Quienes realizan lobby o gestión de intereses ante autoridades del GORE deben proporcionar información veraz y completa al solicitar audiencias, indicando a qué persona o entidad representan y si la gestión es o no remunerada."
        - "La falta de transparencia o la entrega de información falsa por parte de lobbistas o gestores puede gatillar responsabilidades y sanciones específicas, además de afectar la relación con la autoridad regional."

    Fiscalizacion_y_Sanciones:
      ID: LEY-20730-FISCALIZACION-SANCIONES-01
      Rol_de_CGR:
        Def:
          - "La Contraloría General de la República (CGR) supervisa el cumplimiento de la ley en los GORE, investigando omisiones o registros falsos en las agendas de lobby y proponiendo la aplicación de sanciones."
      Causales_Tipicas:
        Def:
          - "No informar o no registrar oportunamente audiencias, viajes o donativos exigidos por la ley."
          - "Registrar información falsa o incompleta que impida la adecuada transparencia de la actividad de lobby."
      Procedimiento_y_Tipos_de_Multa:
        Def:
          - "Tras investigación, la CGR puede proponer al Gobernador Regional (como jefe de servicio) la aplicación de multas que varían, por ejemplo, desde 10 a 30 UTM para omisiones simples y desde 20 a 50 UTM para omisiones inexcusables o registros falsos."
          - "Las sanciones suelen conllevar anotaciones de demérito en la hoja de vida del funcionario y la publicación de la identidad de los sancionados en el sitio web institucional."
      Reincidencia_y_Vinculo_con_Probidad:
        Def:
          - "La reincidencia en conductas infractoras (omitir registros, entregar información falsa) se considera una falta grave a la probidad administrativa, pudiendo abrir la puerta a sanciones más severas en el marco del Estatuto Administrativo."

  Ley_20530_Ministerio_Desarrollo_Social_y_Familia:
    ID: LEY-20530-MASTER-01
    Purp: "Establecer al Ministerio de Desarrollo Social y Familia como órgano rector del sistema de protección social y de la evaluación social de inversiones públicas, condicionando el uso del FNDR y otros fondos regionales."
    Fnd: "Ley N° 20.530 que crea el Ministerio de Desarrollo Social y Familia y modifica diversos cuerpos legales."

    Resumen_Ejecutivo:
      ID: LEY-20530-RESUMEN-01
      Def:
        - "Reorganiza la institucionalidad social del Estado, asignando al MDSF la coordinación de políticas, planes y programas sociales, así como la rectoría técnica del Sistema Nacional de Inversiones (SNI)."
        - "Para los GORE, fija la obligación práctica de someter sus iniciativas de inversión a evaluación de rentabilidad social (RS) favorable como condición previa para su financiamiento y ejecución con cargo al FNDR u otros fondos públicos."

    Eje_Central_Evaluacion:
      ID: LEY-20530-EJE-EVALUACION-01
      Evaluacion_de_Programas_Sociales:
        ID: LEY-20530-EVAL-PROGRAMAS-01
        Def:
          - "El MDSF debe evaluar y emitir informes de recomendación sobre todos los programas sociales nuevos o reformulados de la Administración, incluyendo aquellos diseñados o implementados por los GORE."
          - "Administra un banco integrado de programas sociales que actúa como registro único de la oferta programática del Estado, sobre el cual los GORE deben alinear y justificar sus iniciativas."
      Evaluacion_de_Iniciativas_de_Inversion_RS:
        ID: LEY-20530-EVAL-INVERSIONES-01
        Def:
          - "Ningún proyecto de inversión financiado con recursos públicos –incluido el FNDR– debe ejecutarse sin una recomendación favorable de rentabilidad social (RS favorable) emitida por el MDSF."
          - "La evaluación de RS, canalizada a través de las SEREMI de Desarrollo Social y Familia, determina si los beneficios sociales de un proyecto superan sus costos, condicionando su viabilidad técnica y presupuestaria."
          - "Un pronunciamiento negativo de RS implica que el GORE no debiera financiar ni ejecutar el proyecto, salvo reformas que permitan obtener una nueva evaluación favorable."
          - "La jurisprudencia de la CGR ha declarado inadmisible la aprobación de proyectos FNDR sin RS favorable y ha observado casos en que los GORE iniciaron obras sin el código BIP asignado por el SNI."

    Articulacion_Institucional_y_Roles:
      ID: LEY-20530-ARTICULACION-01
      Rol_de_la_SEREMI_de_Desarrollo_Social_y_Familia:
        ID: LEY-20530-SEREMI-ROL-01
        Def:
          - "Ejecuta a nivel regional la función de evaluación de rentabilidad social de iniciativas de inversión, emitiendo los informes técnicos que habilitan o desaconsejan el uso de recursos FNDR y otros fondos de inversión."
          - "Analiza la coherencia de las iniciativas de inversión con la Estrategia Regional de Desarrollo y otros instrumentos de planificación regional, coordinando con el GORE ajustes de diseño cuando sea necesario."
          - "Colabora con GORE y municipalidades en la capacitación para la correcta formulación de proyectos y programas, fortaleciendo las capacidades técnicas de la red territorial."
          - "Aporta insumos diagnósticos al nivel central del MDSF sobre la situación social de la región, influyendo en la priorización de políticas sociales nacionales y regionales."
      Mecanismos_de_Coordinacion_MDSF_GORE:
        ID: LEY-20530-COORDINACION-01
        Def:
          - "El MDSF coordina a los órganos con competencia social, incluidos los GORE, mediante instancias formales como comités y mesas regionales de protección social."
          - "Los GORE participan en instancias colegiadas lideradas por el MDSF para identificar brechas y priorizar intervenciones sociales, incluyendo la definición de zonas de rezago sujetas a validación técnica del Ministerio."
          - "La ley habilita la celebración de convenios entre MDSF y GORE para cofinanciar y expandir programas sociales, articulando recursos sectoriales, FNDR y otros instrumentos regionales."

    Rol_y_Autonomia_del_GORE_en_el_Marco_de_la_Ley:
      ID: LEY-20530-GORE-ROL-01
      Def:
        - "El GORE mantiene la responsabilidad de liderar la planificación del desarrollo regional mediante la formulación de políticas, planes, programas e iniciativas de inversión propias."
        - "Dicha planificación debe ejercerse dentro del marco de las políticas sociales nacionales, los lineamientos del MDSF y las restricciones del presupuesto de la Nación."
        - "En la práctica, la autonomía del GORE para priorizar proyectos de inversión se ve modulada por el requisito de RS favorable del MDSF y por la necesaria coherencia con las estrategias sociales y de desarrollo definidas a nivel nacional."

  Ley_21722_Presupuestos_Sector_Publico_2025:
    ID: LEY-21722-MASTER-01
    Purp: "Aprobar los ingresos y gastos del Sector Público para el año 2025 y fijar el marco normativo anual que regula la programación y ejecución presupuestaria de los GORE."
    Fnd: "Ley N° 21.722 de Presupuestos del Sector Público para el año 2025."

    Resumen_Ejecutivo:
      ID: LEY-21722-RESUMEN-01
      Def:
        - "Es una ley de vigencia anual que aprueba los montos máximos de ingresos y gastos del Sector Público, incluyendo la Partida 31 correspondiente a los Gobiernos Regionales."
        - "Además de asignar recursos, establece reglas, condiciones, prohibiciones y obligaciones específicas de ejecución que condicionan la gestión financiera de los GORE."
        - "Opera en conjunto con la Norma de Clasificaciones Presupuestarias, que define cómo se registran y categorizan las transacciones presupuestarias."

    Estructura_Presupuesto_GORE:
      ID: LEY-21722-ESTRUCTURA-01
      Partida_y_Programas:
        Def:
          - 'La Partida 31 "Gobiernos Regionales" agrupa un capítulo por cada uno de los 16 GORE, permitiendo identificar su presupuesto individual.'
          - 'Cada capítulo se subdivide en Programas Presupuestarios, destacando el Programa 01 "Funcionamiento" (gastos operativos) y el Programa 02 "Inversión Regional" (FNDR y otros programas de inversión).'
      Subtitulos_de_Gasto_Claves:
        Def:
          - "Subtítulo 21: Gastos en Personal (remuneraciones y obligaciones asociadas del personal del GORE)."
          - "Subtítulo 22: Bienes y Servicios de Consumo (gastos operativos y de funcionamiento)."
          - "Subtítulo 24: Transferencias Corrientes (aportes a terceros para financiar gastos corrientes sin contraprestación directa)."
          - "Subtítulo 29: Adquisición de Activos no Financieros (bienes de capital para uso del GORE)."
          - "Subtítulo 31: Iniciativas de Inversión (gastos ejecutados directamente por el GORE en estudios, proyectos y programas con código BIP)."
          - "Subtítulo 33: Transferencias de Capital (recursos transferidos a otras entidades, públicas o privadas, para que ejecuten inversión, especialmente relevante para la ejecución del FNDR)."

    Reglas_Generales_de_Ejecucion:
      ID: LEY-21722-REGLAS-EJECUCION-01
      Adquisiciones_e_Inversiones:
        ID: LEY-21722-REGLAS-ADQUISICIONES-01
        Def:
          - "Refuerza la obligatoriedad de licitación o propuesta pública para proyectos o programas de inversión sobre ciertos umbrales de monto (por ejemplo, > 1.000 UTM), limitando el uso de trato directo a causales excepcionales."
          - "Exige que los pagos a proveedores de bienes y servicios se realicen mediante transferencia electrónica, incrementando la trazabilidad de las operaciones del GORE."
          - "Sujeta las inversiones en Tecnologías de la Información y Comunicaciones (TIC) a autorización previa de la Dirección de Presupuestos (DIPRES) cuando se trate de proyectos nuevos o de arrastre relevantes."
          - "Dispone que la identificación formal de los proyectos de inversión se efectúa mediante resolución de DIPRES, vinculando el presupuesto a iniciativas de inversión específicas."
          - "Prohíbe en general adquirir, construir o arrendar inmuebles para casas habitación de personal, salvo excepciones acotadas (por ejemplo, viviendas para personal de educación o salud en zonas apartadas)."
      Transferencias_a_Terceros:
        ID: LEY-21722-REGLAS-TRANSFERENCIAS-01
        Def:
          - "Establece un marco estricto para las transferencias a instituciones públicas y privadas con recursos de los subtítulos 24 y 33, fijando condiciones sobre su uso, reintegros y rendiciones de cuentas."
          - "Como regla general, las transferencias corrientes no pueden destinarse a financiar gastos en personal ni bienes y servicios de consumo, salvo que exista autorización expresa en la propia ley o en sus glosas."
          - "Las transferencias a entidades privadas deben realizarse, en principio, mediante concurso público, exigiendo inscripción en el Registro de Colaboradores del Estado y experiencia previa en el ámbito de la política pública financiada."
          - "Los convenios de transferencia deben contener metas, indicadores, obligaciones de información, cláusulas de restitución de fondos y restricciones claras a la subcontratación, especialmente respecto de personas relacionadas."
          - "Autoriza transferencias plurianuales en ciertos casos, pero sujetas a requisitos y autorizaciones adicionales de DIPRES para no comprometer indebidamente presupuestos futuros."

    Obligaciones_de_Transparencia_e_Informacion:
      ID: LEY-21722-TRANSPARENCIA-01
      Def:
        - "Obliga a informar al Congreso Nacional sobre los proyectos de inversión identificados y su estado, dentro de plazos acotados una vez tramitados los decretos respectivos."
        - "Exige la publicación y actualización periódica en el sitio web institucional de la nómina de proyectos de inversión del GORE, con sus montos y avances de ejecución."
        - "Obliga a publicar información detallada sobre las transferencias realizadas (beneficiarios, montos, fundamentos, criterios de asignación), reforzando la transparencia activa."
        - "Dispone que el Ministerio de Hacienda mantenga una plataforma informática de seguimiento de la ejecución presupuestaria, desagregada por región, que refleja la ejecución del presupuesto de los GORE."

    Gastos_Operativos_y_Reglas_Especiales:
      ID: LEY-21722-GASTOS-ESPECIALES-01
      Def:
        - "Reconoce a las personas contratadas a honorarios en programas presupuestarios como agentes públicos sujetos al deber de probidad y a responsabilidad administrativa y penal en el ejercicio de sus funciones."
        - "Establece restricciones severas al gasto en publicidad y difusión institucional, prohibiendo el uso de recursos públicos para la promoción personal de autoridades del GORE."
        - "Restringe y racionaliza las comisiones de servicio y viajes, exigiendo su planificación y justificación, y en algunos casos la presentación de planes anuales ante DIPRES."
        - "Fija normas especiales para el destino de parte del producto de la venta de inmuebles fiscales ubicados en la región, asignando un porcentaje relevante al programa de inversión del GORE respectivo."
        - "Contempla reglas excepcionales para asignaciones destinadas a emergencias, desastres o catástrofes, permitiendo flexibilizar ciertas exigencias de las normas de transferencias para responder con oportunidad."
        - "Hace obligatorios para los GORE los instructivos presidenciales o del Ministerio de Hacienda sobre buen uso de los recursos fiscales."

    Ciclo_y_Etapas_del_Gasto:
      ID: LEY-21722-CICLO-GASTO-01
      Def:
        - "Reconoce y utiliza las etapas del gasto público –preafectación, afectación o compromiso, devengo y pago– como secuencia obligatoria para la ejecución presupuestaria del GORE."
        - "La preafectación corresponde a la reserva inicial de recursos; la afectación, al compromiso formal del gasto; el devengo, al reconocimiento de la obligación de pago por un bien recibido o servicio efectivamente prestado; y el pago, a la salida de fondos."
        - "Exige que el GORE respete rigurosamente estas etapas, evitando prácticas irregulares como devengar recursos por servicios no prestados solo para mejorar indicadores de ejecución."
        - "La jurisprudencia de la Contraloría General ha objetado reiteradamente devengos anticipados o sin respaldo suficiente, considerándolos contrarios a la legalidad presupuestaria y a la probidad administrativa."

  Norma_Clasificaciones_Presupuestarias:
    ID: NORM-CLASIF-MASTER-01
    Purp: "Establecer una estructura y nomenclatura uniforme para registrar todos los ingresos y gastos del Sector Público, sirviendo como columna vertebral del presupuesto y la contabilidad de los GORE."
    Fnd: "Decreto Supremo N° 854 de 2004 del Ministerio de Hacienda y jurisprudencia administrativa asociada de la Contraloría General de la República."

    Resumen_Ejecutivo:
      ID: NORM-CLASIF-RESUMEN-01
      Def:
        - "Es un instrumento normativo que define las clasificaciones presupuestarias que deben utilizar todos los órganos del Estado, incluyendo los Gobiernos Regionales."
        - "Complementa a la Ley de Presupuestos anual: mientras la ley asigna montos por partida, capítulo y programa, el clasificador define cómo se descomponen y registran las transacciones específicas (ingresos y gastos)."
        - "Para los GORE, permite distinguir con precisión qué parte del presupuesto va a funcionamiento, a inversión ejecutada directamente y a inversión ejecutada vía transferencias (FNDR)."

    Estructura_Clasificacion_Presupuestaria:
      ID: NORM-CLASIF-ESTRUCTURA-01
      Clasificacion_Institucional:
        Def:
          - "Ordena el presupuesto por organismo, utilizando niveles jerárquicos: Partida, Capítulo y Programa."
          - 'Partida: nivel superior de agrupación (por ejemplo, Partida 31 "Gobiernos Regionales").'
          - "Capítulo: subdivisión de una Partida que identifica al GORE específico (un capítulo por cada región)."
          - 'Programa: división funcional dentro de un Capítulo (por ejemplo, Programa 01 "Funcionamiento" y Programa 02 "Inversión Regional").'
      Clasificacion_por_Objeto_o_Naturaleza:
        Def:
          - "Ordena las transacciones según su origen (ingresos) o destino (gastos) mediante una jerarquía: Subtítulo, Ítem, Asignación y Sub-asignación."
          - 'Subtítulo: categoría amplia y homogénea (por ejemplo, 21 "Gastos en Personal", 31 "Iniciativas de Inversión", 33 "Transferencias de Capital").'
          - 'Ítem: motivo significativo del gasto o ingreso dentro de un subtítulo (por ejemplo, 01 "Personal de Planta" dentro del subtítulo 21).'
          - 'Asignación: descripción más específica del motivo (por ejemplo, 001 "Sueldos y Sobresueldos").'
          - "Sub-asignación: máximo nivel de detalle, utilizado cuando se requiere una desagregación adicional para control o gestión."
      Clasificacion_por_Iniciativas_de_Inversion:
        Def:
          - "Identifica los recursos asociados a estudios, proyectos y programas de inversión que forman parte del Sistema Nacional de Inversiones (SNI)."
          - "Cada iniciativa se vincula a un código único en el Banco Integrado de Proyectos (BIP), lo que permite seguir el rastro completo de la inversión financiada con FNDR u otros fondos."

    Clasificadores_Clave_Para_GORE_y_FNDR:
      ID: NORM-CLASIF-GORE-CLAVE-01
      Ingresos_Clave:
        ID: NORM-CLASIF-GORE-INGRESOS-01
        Def:
          - 'Subtítulo 05: Transferencias Corrientes – Ítem 02 "Del Gobierno Central": principal fuente de ingresos para el funcionamiento corriente del GORE.'
          - "Subtítulo 08: Otros Ingresos Corrientes – incluye, entre otros, cuentas para registrar saldos no utilizados de transferencias que deben devolverse o reprogramarse."
          - 'Subtítulo 13: Transferencias para Gastos de Capital – Ítem 02 "Del Gobierno Central": recursos destinados a financiar el FNDR y otros programas de inversión regional.'
          - "Subtítulo 15: Saldo Inicial de Caja – registra las disponibilidades netas al 1° de enero, relevantes para medir la holgura financiera inicial del GORE."
      Gastos_Clave:
        ID: NORM-CLASIF-GORE-GASTOS-01
        Def:
          - "Subtítulo 21: Gastos en Personal – agrupa todas las remuneraciones, cotizaciones y otros gastos asociados al personal del GORE (planta, contrata y honorarios)."
          - "Subtítulo 22: Bienes y Servicios de Consumo – cubre los gastos de operación y mantenimiento, tales como arriendos, servicios básicos, viáticos, pasajes, mantención de vehículos y materiales de oficina."
          - "Subtítulo 24: Transferencias Corrientes – recursos entregados a terceros para financiar gastos corrientes sin contraprestación directa (por ejemplo, subvenciones del 8% FNDR a organizaciones privadas sin fines de lucro)."
          - "Subtítulo 29: Adquisición de Activos No Financieros – compra de bienes de capital para uso del propio GORE que no forman parte de un proyecto de inversión con código BIP."
          - "Subtítulo 31: Iniciativas de Inversión – gastos ejecutados directamente por el GORE en estudios, proyectos y programas que cuentan con código BIP; clave para la inversión regional ejecutada por administración directa."
          - "Subtítulo 33: Transferencias de Capital – recursos transferidos a otras entidades públicas o privadas para que ejecuten proyectos de inversión; es el clasificador central para la ejecución indirecta del FNDR mediante municipalidades u otros organismos."

    Relevancia_Para_Control_y_Transparencia:
      ID: NORM-CLASIF-CONTROL-01
      Def:
        - "El clasificador no es solo una herramienta contable, sino un mecanismo de control fiscal: la legalidad del gasto depende, en parte, de su correcta imputación a los subtítulos, ítems y asignaciones correspondientes."
        - "La combinación Ley de Presupuestos + Clasificador fija techos y reglas para mover recursos entre subtítulos, limitando la posibilidad de reorientar fondos sin autorización legal."
        - "Permite generar informes financieros estandarizados que muestran con claridad cuánto del presupuesto del GORE se destina a personal, operación, inversión directa y transferencias de capital (FNDR)."
        - "La jurisprudencia de la Contraloría General ha exigido consistentemente la aplicación correcta del clasificador, declarando improcedente imputar recursos FNDR a subtítulos de gasto corriente cuando en realidad financian inversión (por ejemplo, usar subtítulo 22 en vez de 33)."
        - "Errores de clasificación pueden derivar en reparos, observaciones y eventuales responsabilidades administrativas o de juicio de cuentas para las autoridades y funcionarios responsables."

  Ley_Organica_Contraloria_General:
    ID: LEY-CGR-MASTER-01
    Purp: "Consolidar las atribuciones de la Contraloría General de la República (CGR) y su aplicación directa sobre la gestión administrativa y financiera de los Gobiernos Regionales."
    Fnd: "DFL N° 1/1964 que fija el texto refundido de la Ley N° 10.336, Artículo 98 de la Constitución Política de la República y jurisprudencia administrativa de la propia CGR."

    Resumen_Ejecutivo:
      ID: LEY-CGR-RESUMEN-01
      Def:
        - "La CGR es el órgano superior de control externo del Estado, autónomo e independiente de los ministerios y autoridades políticas."
        - "Sus funciones esenciales sobre los GORE incluyen: control preventivo de legalidad (toma de razón), fiscalización y auditoría de fondos, emisión de dictámenes vinculantes y establecimiento de responsabilidades (juicio de cuentas y sumarios)."
        - "La autonomía de los GORE no los exime del control de la CGR; al contrario, los somete plenamente a su escrutinio en materia de legalidad, probidad y buen uso de recursos."

    Atribuciones_Principales_de_Control:
      ID: LEY-CGR-ATRIBUCIONES-01
      Toma_de_Razon:
        ID: LEY-CGR-TOMA-RAZON-01
        Def:
          - "Mecanismo de control previo por el cual la CGR examina la constitucionalidad y legalidad de decretos y resoluciones del GORE antes de que entren en vigencia."
          - "Deben someterse a toma de razón los actos que crean, modifican o extinguen derechos, así como aquellos que implican gasto público por sobre ciertos umbrales."
          - "Si el acto es legal, la CGR toma razón y el acto puede producir efectos; si es ilegal o inconstitucional, la CGR lo representa, impidiendo su entrada en vigencia."
          - "La CGR puede eximir determinados actos de este trámite para facilitar la gestión, pero esa exención no libera al GORE del deber de respetar la legalidad presupuestaria y administrativa."
      Fiscalizacion_y_Auditoria:
        ID: LEY-CGR-FISCALIZACION-01
        Def:
          - "Fiscaliza la totalidad del ingreso e inversión de los fondos de los GORE, cualquiera sea su origen (incluidos FNDR y otros fondos especiales)."
          - "Puede requerir cualquier tipo de información y antecedentes al GORE; ningún funcionario puede oponer secreto o reserva frente a la CGR para fines de fiscalización."
          - "Imparte instrucciones sobre la forma de llevar la contabilidad, ejecutar el presupuesto y rendir cuentas, que son obligatorias para las unidades de control interno y asesorías jurídicas del GORE."
          - "Las unidades de control interno y asesores jurídicos del GORE dependen técnicamente de la CGR y deben ajustar sus criterios a su jurisprudencia administrativa."
      Funcion_Dictaminante:
        ID: LEY-CGR-DICTAMENES-01
        Def:
          - "Emite dictámenes que interpretan la legislación aplicable a la Administración del Estado, incluyendo a los GORE."
          - "Los dictámenes son vinculantes y de cumplimiento obligatorio para las autoridades y funcionarios del GORE, aun cuando no compartan el criterio jurídico."
          - "Actúan como jurisprudencia administrativa oficial, llenando vacíos legales y unificando criterios de aplicación normativa en todo el país."
      Contiendas_de_Competencia:
        ID: LEY-CGR-COMPETENCIAS-01
        Def:
          - "Resuelve disputas sobre quién tiene la atribución para realizar un determinado acto administrativo (contiendas de competencia)."
          - "Puede dirimir conflictos entre el Gobernador Regional y otros órganos presentes en la región (por ejemplo, SEREMI o Delegado Presidencial)."
          - "La resolución de la CGR en una contienda de competencia es obligatoria para todas las partes involucradas."

    Establecimiento_de_Responsabilidades:
      ID: LEY-CGR-RESPONSABILIDADES-01
      Rendicion_y_Juicio_de_Cuentas:
        ID: LEY-CGR-JUICIO-CUENTAS-01
        Def:
          - "Todo funcionario del GORE que administre o custodie fondos o bienes públicos tiene la obligación de rendir cuentas comprobadas a la CGR en los plazos y formas que esta fije."
          - "Cuando en una rendición existen reparos (observaciones, falta de respaldo, uso indebido de fondos), la CGR puede iniciar un Juicio de Cuentas para determinar si hay responsabilidad pecuniaria."
          - "El Juicio de Cuentas puede concluir con la declaración de deuda a cargo del funcionario responsable, obligándolo a restituir los montos observados."
      Responsabilidad_Administrativa_y_Financiera_del_Funcionario:
        ID: LEY-CGR-RESP-FUNCIONARIO-01
        Def:
          - "Los funcionarios del GORE son responsables por el uso, abuso, pérdida o deterioro de los fondos y bienes públicos a su cargo cuando ello ocurre por dolo, culpa o negligencia."
          - "La orden de un superior jerárquico no exime de responsabilidad si el funcionario no representó por escrito la ilegalidad o improcedencia de dicha orden."
          - "Las responsabilidades pueden ser concurrentes: administrativa, civil y eventualmente penal, según la gravedad de la infracción."
      Potestad_Disciplinaria_Sumarios:
        ID: LEY-CGR-SUMARIOS-01
        Def:
          - "Frente a irregularidades graves en un GORE, la CGR puede ordenar la instrucción de un sumario administrativo por parte del propio servicio."
          - "En casos calificados, la CGR puede asumir directamente la investigación, designando fiscales propios para llevar adelante el sumario."
          - "Los resultados de los sumarios pueden derivar en sanciones disciplinarias (amonestaciones, suspensiones, destituciones) y en antecedentes para eventuales juicios de cuentas o acciones penales."

    Relevancia_Para_los_GORE:
      ID: LEY-CGR-GORE-RELEVANCIA-01
      Def:
        - "La CGR es el principal garante externo de la legalidad y probidad en la gestión de los GORE; sus decisiones condicionan directamente la validez de actos administrativos y el uso del presupuesto regional."
        - "El diseño de procesos internos, sistemas de control y procedimientos de rendición en el GORE debe alinearse con las instrucciones y jurisprudencia de la CGR para evitar reparos y responsabilidades."
        - "Existe una relación estrecha con otras normas del compendio: la CGR aplica y fiscaliza el cumplimiento de la Ley de Presupuestos, la Norma de Clasificaciones Presupuestarias, la Ley 18.575, la Ley 19.653 de Probidad y la Ley 20.285 de Acceso a la Información, entre otras."
        - "Un entendimiento profundo del rol de la CGR es crítico para cualquier diseño de gobernanza, gestión financiera o modernización del GORE, incluyendo iniciativas de Transformación Digital y de fortalecimiento de control interno."

  Ley_19653_Probidad_Administrativa:
    ID: LEY-19653-MASTER-01
    Purp: "Robustecer la integridad en el servicio público mediante la incorporación explícita de la probidad administrativa en la Ley 18.575 y la LOC GORE, fijando estándares exigibles para autoridades y funcionarios regionales."
    Fnd: "Ley N° 19.653 sobre Probidad Administrativa Aplicable a los Organismos de la Administración del Estado."

    Resumen_Ejecutivo:
      ID: LEY-19653-RESUMEN-01
      Def:
        - "Sistematiza y refuerza las normas de probidad en la Ley 18.575 (LOCBGAE) y modifica la Ley 19.175 (LOCGORE) para incorporar expresamente a los Gobiernos Regionales en el régimen de probidad."
        - "Define el principio de probidad administrativa como estándar jurídico vinculante y establece inhabilidades, deber de declaración de intereses y un catálogo de conductas prohibidas."
        - "Introduce ajustes en la LOCGORE que refuerzan el rol del Consejo Regional en el control de la probidad y establecen causales de inhabilidad y cesación de cargo para los CORES."

    Modificaciones_a_Ley_18575_LOCBGAE:
      ID: LEY-19653-MOD-18575-01
      Alcance_General:
        ID: LEY-19653-MOD-18575-ALCANCE-01
        Def:
          - "Incorpora explícitamente a los Gobiernos Regionales dentro del ámbito de la Administración del Estado sujeta a la Ley 18.575, asegurando que todas sus autoridades y funcionarios queden cubiertos por el régimen general de probidad."
          - "Reformula el artículo 3 de la Ley 18.575, precisando la finalidad de la Administración (servicio a la persona humana, bien común) y los principios de responsabilidad, eficiencia, eficacia, coordinación, control, probidad, transparencia e impugnabilidad de actos."
      Contratos_Administrativos_Art9:
        ID: LEY-19653-MOD-18575-ART9-01
        Def:
          - "Establece que los contratos administrativos deben, como regla general, celebrarse previa propuesta pública, de conformidad a la ley."
          - "La licitación privada o el trato directo solo proceden por resolución fundada y en los casos expresamente previstos en la normativa, reduciendo la discrecionalidad en compras y contrataciones del GORE."
      Probidad_y_Transparencia_Art13:
        ID: LEY-19653-MOD-18575-ART13-01
        Def:
          - "Consagra el deber de los funcionarios de observar el principio de probidad administrativa y ejercer la función pública con transparencia."
          - "Establece que los actos administrativos y los documentos que les sirven de sustento o complemento directo y esencial son, por regla general, públicos, conectándose posteriormente con el régimen de acceso a la información de la Ley 20.285."

    Titulo_III_Probidad_Administrativa_en_LOC_18575:
      ID: LEY-19653-TITULO-III-01
      Principio_de_Probidad_Art52:
        ID: LEY-19653-ART52-PROBIDAD-01
        Def:
          - "Impone a autoridades y funcionarios el deber de observar una conducta funcionaria intachable y un desempeño honesto y leal, con preeminencia del interés general sobre el particular."
          - "Constituye el pilar ético-jurídico que debe guiar el actuar de todos los servidores del GORE; su vulneración puede generar responsabilidades administrativas y penales."
      Inhabilidades_de_Ingreso_Art54:
        ID: LEY-19653-ART54-INHABILIDADES-01
        Def:
          - "Establece inhabilidades para ingresar a cargos en la Administración del Estado, incluyendo el GORE, tales como tener contratos o cauciones vigentes de cuantía relevante con el organismo o mantener litigios pendientes con la institución."
          - "Prohíbe el ingreso de cónyuges, hijos, adoptados y parientes cercanos de autoridades y directivos del organismo (hasta jefe de departamento), configurando la base legal del principio antinepotismo."
          - "Inhabilita a personas condenadas por crimen o simple delito para acceder a cargos públicos."
      Declaracion_de_Intereses_Art57:
        ID: LEY-19653-ART57-INTERESES-01
        Def:
          - "Obliga a altas autoridades (incluyendo Gobernadores Regionales y Consejeros Regionales) y a directivos y funcionarios con capacidad decisoria o fiscalizadora a presentar una Declaración de Intereses dentro de un plazo acotado desde la asunción del cargo."
          - "La declaración debe detallar participaciones, vínculos y actividades que puedan generar conflictos de interés, constituyendo el antecedente directo del régimen más robusto establecido luego por la Ley 20.880."
      Catalogo_de_Conductas_Prohibidas_Art62:
        ID: LEY-19653-ART62-CATALOGO-01
        Def:
          - "Enumera conductas contrarias al principio de probidad, tales como utilizar información reservada o privilegiada en beneficio propio o de terceros, influir indebidamente sobre otras personas y emplear recursos institucionales en provecho propio."
          - "Proscribe ejecutar actividades o usar tiempo de jornada para fines ajenos a los institucionales, solicitar o aceptar donativos o ventajas indebidas y participar en asuntos en que exista interés personal o de parientes cercanos, imponiendo un deber expreso de abstención e información al superior."
          - "Califica como falta a la probidad omitir la propuesta pública cuando la ley la exige y contravenir gravemente los deberes de eficiencia, eficacia y legalidad, generando un catálogo operativo para la fiscalización de la conducta funcionaria en el GORE."

    Modificaciones_a_LOCGORE_Ley_19175:
      ID: LEY-19653-MOD-19175-01
      Rol_del_Consejo_Regional_en_Probidad:
        ID: LEY-19653-MOD-19175-CORE-01
        Def:
          - "Incorpora en la LOCGORE una atribución expresa del Consejo Regional de velar por el cumplimiento de las normas sobre probidad administrativa contenidas en la Ley 18.575, reforzando su rol de órgano de control político interno."
      Inhabilidades_y_Cesacion_de_CORES:
        ID: LEY-19653-MOD-19175-INHABILIDADES-01
        Def:
          - "Precisa inhabilidades para ser Consejero Regional, alineadas con las reglas generales de la LOCBGAE (contratos, cauciones, litigios con el GORE, vínculos societarios significativos y condenas penales)."
          - "Establece que la configuración sobreviniente de una inhabilidad es causal de cesación en el cargo de CORE, activando mecanismos de control y de intervención del Tribunal Electoral Regional (TER)."
          - "Introduce expresamente la contravención grave al principio de probidad administrativa como causal de requerimiento de cesación ante el TER, elevando la probidad a parámetro de permanencia en el cargo."

    Probidad_en_la_Gestion_Regional_y_Jurisprudencia:
      ID: LEY-19653-ANALISIS-GORE-01
      Probidad_como_Estandar_Juridico:
        ID: LEY-19653-ANALISIS-PROBIDAD-01
        Def:
          - "La probidad administrativa opera como un estándar jurídico exigible, no solo como recomendación ética; exige a las autoridades y funcionarios del GORE un nivel de diligencia y cuidado superior al del ciudadano común."
          - "Cada acto del GORE debe poder justificarse en función del interés general, siendo evaluable a la luz de este estándar en eventuales procedimientos disciplinarios, de cuentas o penales."
      Inhabilidades_y_Nepotismo:
        ID: LEY-19653-ANALISIS-NEPOTISMO-01
        Def:
          - "Las inhabilidades de ingreso y ejercicio buscan prevenir conflictos de interés estructurales, especialmente vinculados a parentesco y vínculos económicos con el GORE."
          - "La jurisprudencia de la CGR ha invalidado nombramientos y contrataciones que vulneran las prohibiciones de parentesco, incluyendo contrataciones a honorarios que encubren vínculos familiares con autoridades del GORE."
          - "La responsabilidad de verificar la ausencia de inhabilidades recae en las autoridades que efectúan el nombramiento o contratación en el GORE."
      Deber_de_Abstencion_y_Conflictos_de_Interes:
        ID: LEY-19653-ANALISIS-ABSTENCION-01
        Def:
          - "El deber de abstención es la herramienta central para gestionar conflictos de interés circunstanciales: obliga a autoridades y funcionarios a inhibirse de intervenir en asuntos donde tengan interés personal o lo tengan sus parientes cercanos."
          - "En la práctica del GORE, implica que un CORE no debe votar proyectos que beneficien directamente a empresas con las que tiene vínculos, ni un jefe de división debe intervenir en evaluaciones donde exista interés personal."
          - "La CGR y los tribunales han establecido que la sola participación de un inhabilitado en la decisión, aunque el resultado no sea injusto, configura infracción al deber de abstención y puede llevar a la invalidación de acuerdos."
      Catalogo_y_Sanciones:
        ID: LEY-19653-ANALISIS-SANCIONES-01
        Def:
          - "El catálogo de conductas prohibidas sirve de referencia directa para los sumarios administrativos instruidos en el GORE, permitiendo calificar faltas leves, graves y gravísimas al principio de probidad."
          - "Las infracciones pueden derivar en responsabilidad administrativa (amonestación, suspensión, destitución), civil mediante Juicio de Cuentas para reparar perjuicios patrimoniales y, en casos graves, responsabilidad penal (cohecho, malversación, fraude al Fisco)."

    Recomendaciones_Para_los_GORE:
      ID: LEY-19653-RECOMENDACIONES-01
      Def:
        - "Instalar una cultura de probidad preventiva, basada en capacitación continua y en la identificación temprana de riesgos en procesos críticos (compras, contratación de personal, evaluación de proyectos, transferencias a terceros)."
        - "Utilizar el formalismo administrativo (procedimientos claros, fundamentación suficiente de actos, correcta imputación presupuestaria) como barrera de protección frente a acusaciones de falta a la probidad."
        - "Supervisar activa y sistemáticamente las declaraciones de intereses y patrimonio de autoridades y funcionarios, articulándolas con el régimen más detallado de la Ley 20.880."
        - "Fortalecer la coordinación entre la Unidad de Control Interno, la Asesoría Jurídica y las divisiones operativas del GORE para identificar y tratar casos de potencial conflicto de interés antes de que se materialicen en infracciones."

  Ley_20285_Acceso_Informacion_Publica:
    ID: LEY-20285-MASTER-01
    Purp: "Garantizar el derecho de toda persona a solicitar y recibir información de los órganos de la Administración del Estado, estableciendo un régimen de transparencia activa y pasiva plenamente aplicable a los GORE."
    Fnd: "Ley N° 20.285 sobre Acceso a la Información Pública y su reglamento."

    Resumen_General_y_Principios:
      ID: LEY-20285-RESUMEN-01
      Def:
        - "Declara que la transparencia es la regla general en la función pública y el secreto la excepción, obligando a los GORE a operar como una 'casa de cristal'."
        - "Crea el Consejo para la Transparencia (CPLT) como ente fiscalizador y resolutor de amparos frente a denegaciones o incumplimientos, cuyas decisiones son obligatorias para el GORE."
      Sujetos_Obligados:
        ID: LEY-20285-SUJETOS-01
        Def:
          - "Incluye expresamente a los Gobiernos Regionales dentro del listado de órganos sujetos a sus disposiciones, junto a ministerios, municipalidades, Fuerzas Armadas y otros servicios públicos."
      Principio_de_Transparencia_y_Publicidad:
        ID: LEY-20285-PRINCIPIOS-01
        Def:
          - "La función pública se ejerce con transparencia, permitiendo el conocimiento de procedimientos, contenidos y fundamentos de las decisiones del GORE."
          - "Los actos de la Administración, la información elaborada con presupuesto público y toda otra información que obre en poder del GORE son públicos, salvo las excepciones legales de secreto o reserva."
      Derecho_de_Acceso:
        ID: LEY-20285-DERECHO-01
        Def:
          - "Reconoce a toda persona el derecho a solicitar y recibir información del GORE sin necesidad de invocar un interés especial ni justificar la solicitud."
          - "El derecho de acceso se extiende a actos, resoluciones, actas, expedientes, contratos, acuerdos y a toda información elaborada con presupuesto público, en cualquier formato o soporte, salvo las excepciones legales."

    Transparencia_Activa:
      ID: LEY-20285-TRANSP-ACTIVA-01
      Obligaciones_de_Publicacion:
        ID: LEY-20285-TRANSP-ACTIVA-OBLIG-01
        Def:
          - "Obliga al GORE a mantener permanentemente disponible en sus sitios electrónicos, actualizada al menos mensualmente, información sobre su estructura orgánica, facultades y marco normativo aplicable."
          - "Exige publicar información detallada sobre planta, contrata y honorarios, incluyendo remuneraciones, así como las contrataciones de bienes, servicios, estudios y asesorías con identificación de contratistas e intervinientes."
          - "Ordena publicar todas las transferencias de fondos públicos, los actos y resoluciones que tengan efectos sobre terceros, los trámites y requisitos para acceder a servicios, los mecanismos de participación ciudadana y la información sobre presupuesto y ejecución."
          - "Incorpora la obligación de publicar resultados de auditorías y todos los convenios de colaboración o asociatividad que celebre el GORE con organismos públicos o privados, nacionales o extranjeros."
      Notas_Especificas_GORE:
        ID: LEY-20285-TRANSP-ACTIVA-GORE-01
        Def:
          - "Un reglamento complementario precisa la información adicional específica que los GORE deben publicar, reforzando la transparencia de su gestión presupuestaria y de inversión regional."
          - "La Unidad de Control Interno del GORE tiene un rol relevante en la verificación del cumplimiento de estas obligaciones y en la coordinación con las divisiones operativas para mantener la información actualizada."

    Transparencia_Pasiva_y_Procedimiento_de_Acceso:
      ID: LEY-20285-TRANSP-PASIVA-01
      Procedimiento_de_Solicitud:
        ID: LEY-20285-SOLICITUD-01
        Def:
          - "El procedimiento se inicia mediante solicitud escrita o electrónica dirigida al GORE, sin necesidad de invocar causa o motivo."
          - "La solicitud debe contener, al menos, identificación del solicitante, dirección de contacto e identificación clara de la información requerida; la falta de fundamentos no puede utilizarse para rechazarla."
      Plazos_y_Respuesta:
        ID: LEY-20285-PLAZOS-01
        Def:
          - "El GORE dispone, como regla general, de 20 días hábiles para pronunciarse sobre la solicitud, entregando o negando fundadamente la información."
          - "Excepcionalmente puede prorrogar el plazo por 10 días hábiles adicionales cuando existan dificultades fundadas para reunir la información, debiendo comunicar la prórroga al solicitante antes del vencimiento del plazo original."
          - "La falta de respuesta en plazo se considera denegación tácita y habilita al solicitante para recurrir de amparo ante el CPLT, pudiendo generar sanciones para los responsables."
      Denegacion_y_Causales_de_Reserva:
        ID: LEY-20285-RESERVA-01
        Def:
          - "La denegación de información debe ser siempre por escrito y fundada, basada exclusivamente en las causales de secreto o reserva previstas en la ley."
          - "Considera causales como la afectación del debido cumplimiento de funciones del órgano, de la seguridad nacional, de la defensa jurídica del Estado o de los derechos de las personas (vida privada, seguridad, intereses económicos o comerciales, datos personales sensibles)."
          - "Las excepciones deben interpretarse restrictivamente; en caso de duda razonable, se debe favorecer la entrega de información, aplicando el principio de máxima divulgación."

    Amparo_y_Sanciones:
      ID: LEY-20285-AMPARO-SANCIONES-01
      Reclamacion_de_Amparo_ante_CPLT:
        ID: LEY-20285-AMPARO-01
        Def:
          - "El requirente puede interponer un reclamo de amparo ante el Consejo para la Transparencia si el GORE deniega la información, responde fuera de plazo o no responde (denegación tácita)."
          - "El plazo para reclamar es acotado y se cuenta desde la notificación de la denegación o desde la expiración del plazo legal de respuesta; el CPLT analiza el caso, puede requerir antecedentes al GORE y resolver ordenando la entrega total o parcial de la información."
      Infracciones_y_Sanciones:
        ID: LEY-20285-SANCIONES-01
        Def:
          - "Prevé multas proporcionales (porcentaje relevante de la remuneración) para autoridades y funcionarios del GORE que denieguen infundadamente el acceso o no respondan dentro de plazo."
          - "Sanciona el incumplimiento injustificado de obligaciones de transparencia activa, así como la falta de colaboración con el CPLT al no entregar la información requerida oportunamente."
          - "En los casos más graves, contempla la combinación de multas y sanciones disciplinarias (como suspensión en el cargo), articulándose con los mecanismos de responsabilidad administrativa bajo el Estatuto Administrativo y la Ley 18.575."

    Reglamento_Ley_Acceso_Informacion_Publica:
      ID: LEY-20285-REGLAMENTO-01
      Aspectos_Claves:
        ID: LEY-20285-REGLAMENTO-CLAVES-01
        Def:
          - "Detalla principios operativos como apertura, máxima divulgación, divisibilidad, facilitación, no discriminación, oportunidad, control, responsabilidad y gratuidad, que deben guiar la implementación del derecho de acceso en el GORE."
          - "Regula el procedimiento administrativo de solicitud: requisitos formales, subsanación de solicitudes incompletas, derivación a otros órganos cuando el GORE no es competente y plazos de tramitación, reforzando los 20 días hábiles prorrogables por 10."
          - "Establece el tratamiento de terceros cuyos derechos puedan verse afectados por la entrega de información, obligando al GORE a notificarles y gestionar sus eventuales oposiciones, que pueden ser resueltas en última instancia por el CPLT."
          - "Define con mayor precisión los deberes de transparencia activa, el contenido mínimo a publicar en los sitios web del GORE y la obligación de mantener la información fácilmente accesible y actualizada, con supervisión de la Unidad de Control Interno."
          - "Articula los mecanismos de reclamación y sanciones reglamentarias por incumplimiento, reforzando el rol del CPLT y conectando el régimen de transparencia con el de probidad y responsabilidad administrativa."

  Ley_19886_Contratos_Suministro_y_Servicios:
    ID: LEY-19886-MASTER-01
    Purp: "Regular los contratos administrativos de suministro de bienes y prestación de servicios en la Administración del Estado, estableciendo principios, procedimientos y controles para las compras públicas que realizan los GORE."
    Fnd: "Ley N° 19.886 de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios y su reglamentación asociada."

    Alcance_y_Definiciones_Clave:
      ID: LEY-19886-ALCANCE-01
      Ambito_de_Aplicacion:
        ID: LEY-19886-AMBITO-01
        Def:
          - "Se aplica a los contratos onerosos de bienes muebles y servicios celebrados por los órganos de la Administración del Estado definidos en la Ley 18.575, incluyendo a los Gobiernos Regionales."
          - "Alcanza también a corporaciones, fundaciones y asociaciones con participación municipal o regional cuando se vinculan a recursos públicos, así como a ciertas empresas públicas en materias específicas."
      Definicion_Contrato_de_Suministro:
        ID: LEY-19886-DEFINICION-SUMINISTRO-01
        Def:
          - "Contrato que tiene por objeto la compra o arrendamiento de productos o bienes muebles, incluyendo equipos y sistemas de tratamiento de información, licencias de software y fabricación conforme a especificaciones del órgano público."
      Contratacion_Publica_y_Principios:
        ID: LEY-19886-PRINCIPIOS-01
        Def:
          - "Define la contratación pública como el conjunto de procedimientos destinados a satisfacer oportuna y eficientemente las necesidades de las instituciones públicas y la ciudadanía."
          - "Consagra principios rectores: libre acceso a las licitaciones, competencia, publicidad, transparencia, igualdad de trato, no discriminación arbitraria, probidad y obtención de valor por dinero (eficiencia, eficacia, economía y mejor costo-beneficio)."
          - "Incorpora la promoción de la participación de empresas de menor tamaño y la incorporación transversal de criterios de sustentabilidad económica, social y ambiental en las compras públicas."

    Procedimientos_de_Contratacion:
      ID: LEY-19886-PROCEDIMIENTOS-01
      Regla_General_Licitacion_Publica:
        ID: LEY-19886-LIC-PUBLICA-01
        Def:
          - "Establece que los organismos del Estado, incluidos los GORE, deben adjudicar sus contratos, como regla general, mediante licitación o propuesta pública."
          - "La licitación pública es un procedimiento concursal abierto en el que cualquier interesado puede formular ofertas ajustadas a bases previamente aprobadas, adjudicándose la propuesta más conveniente para el interés público."
      Licitacion_Privada_y_Trato_Directo:
        ID: LEY-19886-LIC-OTROS-01
        Def:
          - "Permite, de manera excepcional y mediante resolución fundada, recurrir a licitación privada (invitando a oferentes determinados) o a trato directo o contratación excepcional directa con publicidad, en casos taxativamente regulados."
          - "Causales típicas de trato directo: proveedor único sin alternativas razonables, ausencia de oferentes o ofertas inadmisibles en licitaciones previas, emergencias o urgencias graves, servicios confidenciales o que afectan la seguridad o interés nacional, o situaciones técnicas muy específicas que requieren un proveedor determinado."
          - "La utilización indebida de estas causales puede acarrear multas relevantes para la jefatura del servicio y otras responsabilidades disciplinarias, reforzando el vínculo con la probidad administrativa."
      Procedimientos_Especiales_de_Contratacion:
        ID: LEY-19886-PROCED-ESPECIALES-01
        Def:
          - "Incorpora procedimientos especiales para distintos tipos de compras, como la Compra Ágil, la Compra por Cotización, los Convenios Marco, los Contratos para la Innovación, el Diálogo Competitivo de Innovación y la Subasta Inversa Electrónica."
          - "Estos procedimientos buscan simplificar y dinamizar compras de menor monto, habilitar soluciones innovadoras, aprovechar economías de escala y facilitar la participación de empresas de menor tamaño y proveedores locales."
      Bases_de_Licitacion_y_Evaluacion:
        ID: LEY-19886-BASES-EVAL-01
        Def:
          - "Las bases de licitación deben definir con claridad las condiciones para determinar la oferta más ventajosa, considerando no solo el precio, sino también la calidad, el ciclo de vida del bien o servicio y otros factores objetivos."
          - "Se exige incorporar criterios que favorezcan mejores condiciones laborales y remuneracionales de los trabajadores de empresas contratistas, así como criterios de sustentabilidad y de promoción de la economía social, sin desvirtuar la evaluación técnica y económica."

    Requisitos_de_Proveedores_y_Registro:
      ID: LEY-19886-PROVEEDORES-01
      Requisitos_Generales:
        ID: LEY-19886-REQUISITOS-01
        Def:
          - "Para contratar con organismos del Estado, los proveedores deben acreditar situación financiera e idoneidad técnica suficientes, encontrarse debidamente inscritos y actualizados en el Registro de Proveedores y cumplir los requisitos del derecho común."
          - "Se excluye a quienes han sido condenados recientemente por prácticas antisindicales, infracciones graves a derechos fundamentales de los trabajadores o ciertos delitos económicos, reforzando el vínculo entre compras públicas y estándares laborales."
      Garantias_y_Seriedad_de_Ofertas:
        ID: LEY-19886-GARANTIAS-01
        Def:
          - "Prevé la exigencia de garantías de seriedad de la oferta y de fiel y oportuno cumplimiento del contrato, especialmente en contrataciones de mayor monto, con porcentajes máximos respecto del valor del contrato."
          - "Permite eximir de garantías en ciertos casos (por ejemplo, suministros consumibles o servicios sociales) cuando existan mecanismos alternativos que resguarden adecuadamente el cumplimiento."
      Inhabilidades_y_Registro_de_Proveedores:
        ID: LEY-19886-INHABILIDADES-01
        Def:
          - "Establece causales de inhabilidad para inscribirse o mantenerse en el Registro de Proveedores, tales como condenas por delitos concursales, incumplimientos contractuales graves con organismos públicos, cohecho, lavado de activos, financiamiento del terrorismo o la entrega maliciosa de antecedentes falsos."
          - "Prevé la extensión de inhabilidades a sociedades donde los condenados tienen participación o control significativo, afectando así la posibilidad de que grupos empresariales eludan las sanciones mediante nuevas razones sociales."

    Sistema_Electronico_y_Transparencia_en_Compras:
      ID: LEY-19886-SISTEMA-ELECTRONICO-01
      Sistema_de_Informacion_y_Gestion:
        ID: LEY-19886-SISTEMA-INFO-01
        Def:
          - "Obliga a los organismos de la Administración, incluidos los GORE, a utilizar sistemas electrónicos de información y gestión de compras provistos por la Dirección de Compras, para cotizar, licitar, adjudicar y administrar sus contratos."
          - "Crea un Sistema de Información y Gestión de Compras y Contrataciones del Estado, de acceso público y gratuito, donde deben publicarse los llamados, aclaraciones, modificaciones de bases, adjudicaciones, órdenes de compra y la ejecución contractual."
          - "Exige que la información se publique en formatos abiertos y reutilizables, salvo en los casos de información sujeta a secreto o reserva legal."
      Excepciones_al_Uso_del_Sistema:
        ID: LEY-19886-EXCEPCIONES-SISTEMA-01
        Def:
          - "Solo de manera excepcional pueden desarrollarse procesos fuera del sistema electrónico, en casos como falta de acceso tecnológico de proveedores, fuerza mayor, indisponibilidad técnica certificada del sistema, materias secretas o compras a proveedores extranjeros en condiciones especiales."
          - "Aun en esos casos, el GORE debe publicar posteriormente en el sistema los antecedentes esenciales del procedimiento y del contrato, manteniendo un estándar de transparencia."

    Tribunal_de_Contratacion_Publica:
      ID: LEY-19886-TRIBUNAL-01
      Naturaleza_y_Composicion:
        ID: LEY-19886-TRIBUNAL-ESTRUCTURA-01
        Def:
          - "Crea el Tribunal de Contratación Pública, órgano jurisdiccional especial con asiento en Santiago, sometido a la superintendencia de la Corte Suprema."
          - "Está integrado por jueces especializados en contratación pública y derecho administrativo, designados mediante un procedimiento que involucra al Consejo de Alta Dirección Pública y a la Corte Suprema."
      Funcion_y_Rol_Para_GORE:
        ID: LEY-19886-TRIBUNAL-FUNCION-01
        Def:
          - "Conoce de reclamaciones relacionadas con la legalidad de los procedimientos de contratación pública, incluyendo aquellos en los que participan los GORE."
          - "Sus decisiones pueden anular licitaciones o adjudicaciones cuando se vulneran las normas de la ley, afectando directamente la ejecución de programas y proyectos regionales."

    Direccion_de_Compras_y_Contratacion_Publica:
      ID: LEY-19886-DIRECCION-COMPRAS-01
      Creacion_y_Funciones:
        ID: LEY-19886-DIRECCION-FUNCIONES-01
        Def:
          - "Crea la Dirección de Compras y Contratación Pública (ChileCompra) como servicio público descentralizado bajo la supervigilancia del Ministerio de Hacienda."
          - "Tiene funciones de asesoría a los organismos, operación y administración de los sistemas electrónicos de compras, licitación y gestión del Registro de Proveedores, diseño y administración de Convenios Marco y emisión de instrucciones obligatorias para la Administración del Estado."
          - "Debe promover la competencia, la probidad, la transparencia, la eficiencia y la sustentabilidad de las compras públicas, así como la participación de empresas de menor tamaño y proveedores locales."
      Relacion_con_los_GORE:
        ID: LEY-19886-DIRECCION-GORE-01
        Def:
          - "Los GORE deben ajustar sus procesos de compra a las instrucciones y sistemas definidos por la Dirección de Compras, salvo cuando una ley especial disponga otra cosa."
          - "La Dirección puede monitorear los procedimientos de contratación de los GORE, recibir reclamos de la ciudadanía y remitir antecedentes a la Contraloría o al Ministerio Público en caso de ilícitos o faltas de probidad."

    Probidad_y_Transparencia_en_la_Contratacion:
      ID: LEY-19886-PROBIDAD-01
      Reglas_Especificas_de_Probidad:
        ID: LEY-19886-PROBIDAD-REGLAS-01
        Def:
          - "El Capítulo VII refuerza el principio de probidad y transparencia en contratación pública, complementando la Ley 18.575 y la Ley 19.653."
          - "Prohíbe, en términos generales, las comunicaciones directas fuera del sistema entre oferentes y funcionarios que participan en la adjudicación durante el desarrollo del procedimiento, garantizando igualdad de información."
          - "Prohíbe contratar con funcionarios del propio organismo, sus cónyuges, convivientes y parientes cercanos, así como con sociedades en que estos tengan participación relevante, salvo excepciones muy restringidas y debidamente fundadas."
          - "Obliga a autoridades y funcionarios a abstenerse de intervenir en procedimientos de contratación y en la ejecución de contratos cuando tengan interés personal o vínculos que afecten su imparcialidad, detallando un catálogo de causales de abstención."
          - "Declara la nulidad de los contratos celebrados infringiendo estas reglas y califica estas infracciones como contravenciones graves al principio de probidad, con posibles responsabilidades administrativas, civiles y penales."

    Promocion_de_Empresas_de_Menor_Tamano_y_Proveedores_Locales:
      ID: LEY-19886-MIPYME-01
      Medidas_de_Promocion:
        ID: LEY-19886-MIPYME-MEDIDAS-01
        Def:
          - "El Capítulo IX establece un marco especial para promover la participación de empresas de menor tamaño y cooperativas en el sistema de compras públicas, incluyendo criterios de evaluación y mecanismos específicos en los procedimientos de compra."
          - "Define la figura de proveedores locales y de uniones temporales de proveedores, permitiendo que empresas pequeñas se asocien para competir en licitaciones y convenios marco."
          - "Obliga a la Dirección de Compras y a los organismos compradores, incluidos los GORE, a generar condiciones que faciliten el acceso de MIPYME y proveedores locales, evitando requisitos desproporcionados que limiten su concurrencia."

    Relevancia_Para_los_GORE:
      ID: LEY-19886-GORE-RELEVANCIA-01
      Def:
        - "Conecta directamente el sistema de compras del GORE con estándares nacionales de probidad, transparencia y eficiencia, estructurando cómo se licitan y contratan bienes y servicios necesarios para la gestión regional."
        - "Obliga al GORE a utilizar plataformas electrónicas y procedimientos formales que dejan trazabilidad completa de las decisiones de compra, lo que facilita el control por parte de la Contraloría, el Tribunal de Contratación Pública y la ciudadanía."
        - "La correcta aplicación de la Ley 19.886 es fundamental para evitar observaciones por uso indebido del trato directo, fragmentación artificiosa de compras, favoritismos en la selección de proveedores o vulneraciones al principio de probidad."
        - "Resulta clave para el diseño de manuales internos de adquisiciones del GORE, para la planificación de compras estratégicas y para la articulación con políticas de desarrollo productivo regional que busquen favorecer a empresas de menor tamaño y proveedores locales."

  Ley_18695_Municipalidades_Desde_Perspectiva_GORE:
    ID: LEY-18695-GORE-MUNI-MASTER-01
    Purp: "Analizar la Ley Orgánica Constitucional de Municipalidades desde la óptica del Gobierno Regional, identificando áreas de coordinación, jerarquía normativa, financiamiento e instrumentos de planificación clave para la relación GORE–municipios."
    Fnd: "Ley N° 18.695 Orgánica Constitucional de Municipalidades y normativa complementaria."

    Coordinacion_Interinstitucional_y_Jerarquia_Normativa:
      ID: LEY-18695-COORDINACION-01
      Rol_del_Gobernador_Regional:
        ID: LEY-18695-COORD-GOBERNADOR-01
        Def:
          - "La LOCM reconoce al Gobernador Regional una potestad de supervigilancia sobre la gestión municipal en cuanto a su coherencia con los instrumentos de planificación regional (ERD, PROT, instrumentos territoriales regionales)."
          - "Esta supervigilancia no implica jerarquía administrativa sobre los alcaldes, pero habilita al Gobernador para representar ante la Contraloría General o los tribunales los actos municipales que contradigan planes regionales."
          - "Otorga además un rol dirimente en conflictos de coordinación entre municipalidades y servicios que dependen o se relacionan con el GORE, permitiendo destrabar proyectos o políticas regionales a escala comunal."
      Rol_del_Delegado_Presidencial_Regional:
        ID: LEY-18695-COORD-DPR-01
        Def:
          - "El Delegado Presidencial Regional y sus delegados provinciales aseguran la coherencia de la acción municipal con las políticas del gobierno central y el gobierno interior."
          - "Para el GORE, la LOCM delimita campos de acción: mientras el GORE se coordina con municipios en materias de desarrollo regional, el DPR lo hace en materias sectoriales y de orden público, generando potenciales puntos de fricción que requieren coordinación política y técnica."
      Marco_de_Actuacion_Municipal:
        ID: LEY-18695-MARCO-MUNICIPAL-01
        Def:
          - "Los municipios deben actuar dentro de los planes nacionales y regionales de desarrollo: el Delegado Presidencial Regional fiscaliza la adecuación a planes nacionales y el Gobernador Regional la adecuación a los planes regionales."
          - "La coordinación interinstitucional se apoya en acuerdos directos entre municipalidades y servicios relacionados con el GORE; a falta de acuerdo, el Gobernador puede disponer medidas a solicitud del alcalde, sin alterar las atribuciones legales de cada órgano."

    Instrumentos_de_Planificacion_Municipal_y_Vinculo_Regional:
      ID: LEY-18695-PLANIFICACION-01
      PLADECO_y_Estrategia_Regional_de_Desarrollo:
        ID: LEY-18695-PLAN-PLADECO-ERD-01
        Def:
          - "El Plan Comunal de Desarrollo (PLADECO) es el instrumento rector del desarrollo comunal, pero debe armonizarse con la Estrategia Regional de Desarrollo (ERD) y otros planes regionales y nacionales."
          - "El GORE, a través de su División de Planificación y Desarrollo Regional (DIPLADE), tiene la responsabilidad técnica de revisar los PLADECO de las comunas y verificar su coherencia con la visión y objetivos regionales."
          - "En la práctica, la coherencia PLADECO–ERD se vuelve criterio de evaluación para la priorización y financiamiento de proyectos municipales con fondos regionales (FNDR, FRIL, otros)."
      Plan_Regulador_Comunal_y_Planificacion_Territorial_Regional:
        ID: LEY-18695-PLAN-PRC-REGIONAL-01
        Def:
          - "La planificación urbana comunal, a través del Plan Regulador Comunal (PRC), está subordinada a los instrumentos de planificación territorial de escala superior, como los Planes Reguladores Intercomunales o Metropolitanos y el PROT."
          - "Los PRC deben respetar límites de extensión urbana, áreas de riesgo y vialidad estructurante definidos a nivel regional; el CORE, al aprobar instrumentos regionales, condiciona el marco dentro del cual se mueve la planificación comunal."
          - "Para el GORE, esta jerarquía es fundamental al evaluar la localización y viabilidad de proyectos de inversión municipales y regionales en el territorio."

    Inversion_Publica_y_Mecanismos_de_Colaboracion:
      ID: LEY-18695-INVERSION-01
      Convenios_de_Programacion_GORE_Municipalidades:
        ID: LEY-18695-CONV-PROGRAMACION-01
        Def:
          - "La LOCM reconoce los convenios de programación entre el GORE y las municipalidades como herramientas centrales para coordinar inversión sectorial, regional y municipal en proyectos estratégicos, de carácter anual o plurianual."
          - "Estos convenios son jurídicamente obligatorios: las partes deben incorporar en sus presupuestos los compromisos de gasto asumidos, dando estabilidad a la cartera de proyectos acordada."
          - "Deben identificar proyectos específicos, responsabilidades y obligaciones de cada parte, metas, procedimientos de evaluación, normas de revocación y reglas de reasignación de recursos, pudiendo incorporar otras entidades públicas o privadas."
      Convenios_de_Programacion_Territorial:
        ID: LEY-18695-CONV-TERRITORIAL-01
        Def:
          - "Los convenios de programación territorial permiten que el GORE y una o más municipalidades acuerden la ejecución conjunta de proyectos de impacto comunal o intercomunal, definiendo plazos y aportes financieros de cada parte mediante resolución regional."
          - "Son una herramienta flexible para abordar problemas y oportunidades a escala subregional, facilitando la coordinación de inversiones que trascienden los límites de una sola comuna."
      Transferencias_y_Financiamiento_Municipal_Desde_GORE:
        ID: LEY-18695-INVERSION-TRANSFERENCIAS-01
        Def:
          - "El aporte del GORE forma parte del patrimonio municipal y es una fuente crucial de financiamiento para proyectos de inversión local; gran parte de la inversión ejecutada por municipios proviene de fondos regionales."
          - "Las divisiones técnicas del GORE (como DIPIR y DIPLADE) deben evaluar la pertinencia, factibilidad y rentabilidad social de los proyectos municipales que se financian con FNDR u otros fondos regionales."
          - "Aunque la ejecución material la realiza el municipio, la responsabilidad política y técnica por el buen uso de los recursos regionales recae en el GORE, que debe establecer mecanismos robustos de seguimiento, control y rendición de cuentas."

    Competencias_Concurrentes_y_Seguridad_Publica:
      ID: LEY-18695-COMPETENCIAS-01
      Seguridad_Publica_y_Prevencion_del_Delito:
        ID: LEY-18695-SEGURIDAD-01
        Def:
          - "Tanto los municipios como el GORE tienen funciones en prevención del delito y seguridad pública, aunque el control del orden público sigue siendo competencia del Ministerio del Interior y las Fuerzas de Orden."
          - "La LOCM establece el Plan Comunal de Seguridad Pública como instrumento comunal que debe ser coherente con las políticas nacionales de seguridad y con las políticas y planes regionales relevantes en la materia."
          - "La Subsecretaría de Prevención del Delito entrega información y orientaciones al Consejo Regional de Seguridad, al GORE y al Delegado Presidencial Regional, y las municipalidades pueden solicitar asesoría al GORE para formular o implementar sus planes de seguridad."

    Asociativismo_Municipal_y_Rol_del_GORE:
      ID: LEY-18695-ASOCIATIVISMO-01
      Asociaciones_y_Convenios_Entre_Municipalidades:
        ID: LEY-18695-ASOCIACIONES-01
        Def:
          - "La LOCM permite que dos o más municipalidades constituyan asociaciones con personalidad jurídica (de derecho privado) o celebren convenios de asociación sin personalidad jurídica para proveer servicios comunes, ejecutar obras de desarrollo local y fortalecer su gestión."
          - "Estas asociaciones pueden abarcar comunas de distintas provincias o regiones y orientarse a ámbitos diversos como medio ambiente, seguridad, turismo o capacitación de personal municipal."
          - "Para el GORE, el asociativismo municipal representa una oportunidad estratégica para abordar problemas de escala subregional mediante convenios de colaboración y transferencias de recursos o asistencia técnica a asociaciones municipales."

    Relevancia_Para_los_GORE:
      ID: LEY-18695-GORE-RELEVANCIA-01
      Def:
        - "La LOCM configura el espacio de interacción permanente entre el GORE y los municipios, definiendo cómo se coordinan en planificación, inversión, seguridad y servicios, sin alterar la autonomía municipal pero exigiendo coherencia con los instrumentos regionales."
        - "Entrega al GORE herramientas formales –como la supervigilancia respecto de la adecuación a planes regionales y los convenios de programación y territoriales– para alinear la acción municipal con la estrategia regional de desarrollo."
        - "Hace explícito que una parte esencial de la inversión municipal depende de decisiones de financiamiento regional, lo que refuerza la necesidad de capacidades técnicas en el GORE para evaluar, priorizar y supervisar proyectos municipales."
        - "El GORE debe comprender y utilizar el marco de la LOCM para diseñar una política de relacionamiento municipal clara, que combine cooperación técnica y financiera con exigencias de coherencia estratégica y probidad en el uso de recursos regionales."

  Ley_17336_Propiedad_Intelectual_Para_GORE:
    ID: LEY-17336-GORE-MASTER-01
    Purp: "Sintetizar la Ley 17.336 de Propiedad Intelectual desde la perspectiva de los Gobiernos Regionales, abarcando su rol como creadores, usuarios y fomentadores de obras protegidas."
    Fnd: "Ley N° 17.336 sobre Propiedad Intelectual y normativa complementaria; en diálogo con la Ley 19.175 y la Ley 20.285."

    Marco_General_y_Ambito:
      ID: LEY-17336-MARCO-01
      Def:
        - "Protege los derechos de autores sobre obras de la inteligencia (literarias, artísticas, científicas), incluyendo documentos técnicos, audiovisuales, mapas, programas computacionales y compilaciones de datos relevantes para la gestión regional."
        - "Distingue entre derechos patrimoniales (explotación económica) y derechos morales (paternidad e integridad de la obra), que subsisten siempre en el autor personas natural."
        - "Establece actos exclusivos del titular: publicar, reproducir, adaptar, transformar, traducir, ejecutar públicamente y distribuir las obras, salvo excepciones legales."
        - "Define que nadie puede utilizar públicamente una obra de dominio privado sin autorización expresa del titular (Art. 19), regla central para el funcionamiento del GORE como usuario de contenidos."

    Titularidad_en_el_Sector_Publico_y_Software:
      ID: LEY-17336-TITULARIDAD-01
      Obras_de_Funcionarios_Publicos:
        ID: LEY-17336-FUNCIONARIOS-01
        Def:
          - "El Art. 88 establece que el Estado, los municipios y corporaciones públicas, incluyendo los GORE, son titulares de las obras producidas por sus funcionarios en el ejercicio de sus funciones, sin perjuicio de los derechos morales de los creadores."
          - "El titular institucional puede, mediante resolución, liberar determinadas obras al patrimonio cultural común, lo que permite su uso libre por terceros, respetando siempre la paternidad e integridad de la obra."
      Programas_Computacionales_y_Trabajos_Encargados:
        ID: LEY-17336-SOFTWARE-ENCARGOS-01
        Def:
          - "Para programas computacionales y obras realizadas por dependientes en cumplimiento de su contrato de trabajo, se presume que el empleador (incluido un GORE) es titular patrimonial, salvo pacto escrito en contrario."
          - "En obras realizadas por encargo a consultores o terceros independientes, la regla general es que el autor externo conserva la titularidad, a menos que exista cesión expresa en el contrato."
          - "Si no se pacta cesión, el GORE podría pagar por el informe, software o campaña, pero no por el derecho a reproducirlo, modificarlo o relicenciarlo ampliamente, generando riesgos jurídicos y de gestión."

    GORE_Como_Creador_y_Comitente_de_Obras:
      ID: LEY-17336-GORE-CREADOR-01
      Obras_Institucionales_y_Instrumentos_de_Gestion:
        ID: LEY-17336-GORE-OBRAS-01
        Def:
          - "Instrumentos como la Estrategia Regional de Desarrollo, el PROT, planes, estudios y manuales internos constituyen obras protegidas; en muchos casos, son obras colectivas cuya titularidad patrimonial corresponde al GORE."
          - "Al publicar estos instrumentos, se recomienda explicitar la titularidad institucional y el año de publicación, por ejemplo: '© Gobierno Regional de [Región], [Año]. Todos los derechos reservados'."
      Contratos_y_Bases_que_Encargan_Obras:
        ID: LEY-17336-GORE-CONTRATOS-01
        Def:
          - "Las bases de licitación, convenios y contratos mediante los cuales el GORE encarga estudios, contenidos audiovisuales, diseños, software u otras obras deben incluir cláusulas de cesión de derechos patrimoniales amplias y perpetuas a favor del GORE."
          - "Estas cláusulas deben precisar derechos cedidos, plazo, territorio y modalidades de explotación, de acuerdo al Art. 20, evitando ambigüedades que limiten el uso público de las obras financiadas con recursos regionales."
          - "Es recomendable que la cesión permita al GORE licenciar obras con fines de difusión pública sin fines de lucro, manteniendo la autoría moral del creador."

    GORE_Como_Usuario_de_Obras_Protegidas:
      ID: LEY-17336-GORE-USUARIO-01
      Uso_de_Software_y_Contenidos:
        ID: LEY-17336-USO-SOFTWARE-CONTENIDOS-01
        Def:
          - "El uso de software por parte del GORE exige contar con licencias válidas; el empleo de programas no licenciados expone a responsabilidad civil y penal, además de observaciones de control externo."
          - "La utilización de fotografías, videos, música, textos y otros contenidos de terceros en campañas, sitios web o eventos del GORE requiere autorización expresa del titular o de las entidades de gestión colectiva, salvo que se trate de obras en dominio público o con licencias abiertas (por ejemplo, Creative Commons adecuadamente revisadas)."
          - "En proyectos de arquitectura y diseño urbano, debe respetarse el derecho moral a la integridad de la obra; modificaciones sustantivas sobre proyectos de terceros pueden vulnerar este derecho si no están autorizadas."
      Licencias_y_Gestion_Colectiva:
        ID: LEY-17336-LICENCIAS-GESTION-01
        Def:
          - "La ley contempla la licencia a través de entidades de gestión colectiva para el uso de repertorios amplios (música, obras escénicas, etc.), exigiendo el pago de remuneraciones conforme a tarifas generales publicadas en el Diario Oficial."
          - "Para actividades del GORE que incluyan espectáculos públicos, transmisiones o difusión en medios, es más eficiente contratar licencias con entidades de gestión colectiva que negociar autorización caso a caso con cada titular."

    Obras_Huerfanas_y_Fuera_de_Comercio:
      ID: LEY-17336-OBRAS-HUERFANAS-01
      Def:
        - "La ley regula el uso de obras huérfanas o fuera de comercio por entidades culturales, educativas, archivos y bibliotecas sin fines de lucro, previa tramitación ante la Subdirección de Derechos Intelectuales y registro de la obra."
        - "Este mecanismo permite que instituciones financiadas por el GORE utilicen obras de difícil licenciamiento, con la obligación de pagar una tarifa si el titular aparece con posterioridad."

    Limitaciones_y_Excepciones_Relevantes_para_GORE:
      ID: LEY-17336-EXCEPCIONES-01
      Citas_y_Uso_Educativo:
        ID: LEY-17336-EXC-CITA-EDUCACION-01
        Def:
          - "Permite la cita de fragmentos breves de obras protegidas sin autorización ni pago, para fines de crítica, ilustración, enseñanza o investigación, siempre que se indique fuente y autor."
          - "Autoriza la reproducción y traducción de pequeños fragmentos de obras con fines educacionales en el sistema formal o autorizado, excluyendo específicamente textos escolares y manuales universitarios, y exigiendo mención de autor y fuente."
      Discapacidad_y_Acceso_Universal:
        ID: LEY-17336-EXC-DISCAPACIDAD-01
        Def:
          - "Habilita la reproducción, adaptación, distribución y comunicación de obras en formatos accesibles para personas con discapacidad, sin fines de lucro y siempre que ya hayan sido lícitamente publicadas."
      Bibliotecas_Archivos_y_Preservacion:
        ID: LEY-17336-EXC-BIBLIOTECAS-01
        Def:
          - "Permite la reprografía de artículos o extractos breves para uso exclusivo de usuarios de bibliotecas o archivos sin fines de lucro, sin constitutir infracción."
          - "Autoriza la reproducción de obras no disponibles en el mercado por bibliotecas y archivos sin fines de lucro para preservar ejemplares o reemplazar pérdidas o deterioros."
          - "Faculta la consulta electrónica de obras de la colección en terminales internos, sin posibilidad de copia digital, en entidades sin fines de lucro."
      Establecimientos_Sin_Fines_de_Lucro_y_Actuaciones_Publicas:
        ID: LEY-17336-EXC-ESTABLECIMIENTOS-01
        Def:
          - "Declarar que ciertos usos en establecimientos educacionales, de beneficencia, bibliotecas y otros no constituyen comunicación o ejecución pública, siempre que no exista fin de lucro, eximiendo de autorización y pago."
          - "Permite el uso de discursos públicos y actuaciones judiciales, administrativas o legislativas sin autorización ni pago, para fines de información y documentación institucional."
      Software_y_Excepcion_de_Usuario_Legitimo:
        ID: LEY-17336-EXC-SOFTWARE-01
        Def:
          - "El tenedor legítimo de un programa computacional puede realizar copias o adaptaciones esenciales para su uso y para archivo o respaldo, pero no para otros fines ni para distribuir a terceros."

    Registro_y_Formalidades:
      ID: LEY-17336-REGISTRO-01
      Def:
        - "La ley establece el Registro de la Propiedad Intelectual, donde pueden inscribirse derechos de autor y conexos, con depósito de un ejemplar de la obra, generando un fuerte medio de prueba sobre la titularidad y la fecha."
        - "Las transferencias totales o parciales de derechos deben constar en instrumento público o privado autorizado ante notario e inscribirse en el Registro dentro de un plazo determinado, lo que es relevante para cesiones a favor del GORE."

    Tension_con_Ley_de_Transparencia:
      ID: LEY-17336-TRANSPARENCIA-01
      Def:
        - "En caso de solicitudes de acceso a estudios, informes u obras financiadas por el GORE pero titularizadas por terceros, la jurisprudencia ha establecido que el derecho de acceso a la información pública prevalece sobre el derecho de autor."
        - "El GORE está obligado a entregar la información solicitada cuando se trata de documentos elaborados con recursos públicos, aunque el solicitante no adquiere por ello una licencia para explotar comercialmente la obra."
        - "Se recomienda advertir explícitamente al momento de la entrega que el contenido está protegido y que su entrega responde a fines de control social y transparencia, no de explotación económica."
        - "La forma más robusta de evitar tensiones es pactar desde el inicio la cesión de derechos patrimoniales al GORE en contratos y convenios que financian la generación de estas obras."

    Plan_de_Accion_Interno_Para_GORE:
      ID: LEY-17336-PLAN-ACCION-01
      Def:
        - "Revisar y estandarizar cláusulas contractuales y bases de licitación para incluir cesión de derechos patrimoniales a favor del GORE, particularmente en estudios, software, campañas comunicacionales y contenidos culturales."
        - "Desarrollar un protocolo interno sobre uso lícito de contenidos de terceros (software, imágenes, música, textos), incluyendo lineamientos para el uso de licencias abiertas y dominio público."
        - "Estandarizar las bases y convenios de fondos culturales FNDR para reservar al GORE una licencia no exclusiva, gratuita y a perpetuidad para difundir las obras financiadas con fines culturales y sin fines de lucro."
        - "Capacitar a equipos jurídicos, de adquisiciones, comunicaciones, cultura y transparencia en nociones básicas de propiedad intelectual y en los riesgos de uso no autorizado de obras."
        - "Instruir a la unidad de transparencia sobre el manejo de solicitudes que involucren obras protegidas, asegurando el cumplimiento simultáneo de la Ley 20.285 y de la Ley 17.336."

    Relevancia_Para_los_GORE:
      ID: LEY-17336-GORE-RELEVANCIA-01
      Def:
        - "La adecuada gestión de la propiedad intelectual permite al GORE maximizar el valor público de las obras que financia y crea, evitando a la vez riesgos legales por uso no autorizado de contenidos de terceros."
        - "La Ley 17.336 obliga al GORE a integrar criterios de titularidad y licenciamiento en sus contratos, fondos concursables y políticas de publicación, en coherencia con los principios de transparencia, probidad y eficiencia en el uso de recursos regionales."
        - "Comprender el régimen de excepciones y limitaciones facilita que el GORE utilice de manera legítima obras de terceros en actividades educacionales, culturales y de gestión interna, sin caer en infracciones."
        - "El reconocimiento expreso del GORE como titular de las obras creadas por sus funcionarios sienta la base para desarrollar un patrimonio intelectual público que puede ser utilizado estratégica y responsablemente en beneficio de la región."

  Ley_21659_Seguridad_Privada_y_GORE:
    ID: LEY-21659-GORE-MASTER-01
    Purp: "Sintetizar la Ley 21.659 sobre Seguridad Privada, enfocando sus implicancias para los Gobiernos Regionales como propietarios de inmuebles, promotores de eventos y actores de coordinación en seguridad."
    Fnd: "Ley N° 21.659 que regula los servicios y sistemas de seguridad privada, derogando el DL 3.607 y la Ley 19.303."

    Marco_General_e_Institucionalidad:
      ID: LEY-21659-MARCO-01
      Def:
        - "Define la seguridad privada como actividades preventivas, coadyuvantes y complementarias de la seguridad pública, realizadas por entidades privadas o por ciertas entidades obligadas bajo regulación específica."
        - "Establece a la Subsecretaría de Prevención del Delito (SPD) como órgano rector del sistema de seguridad privada, responsable de autorizar, regular y supervigilar estas actividades, manteniendo registros oficiales."
        - "Reconoce a Carabineros de Chile (y autoridades militares/marítimas/aeronáuticas según el caso) como autoridad fiscalizadora a cargo de supervisar el cumplimiento y emitir informes técnicos."
        - "Prohíbe en general que el personal de la Administración del Estado, incluido el GORE, realice directamente actividades de seguridad privada, salvo cuando la ley lo autorice expresamente en su calidad de entidad obligada."

    GORE_como_Entidad_Obligada:
      ID: LEY-21659-ENTIDAD-OBLIGADA-01
      Def:
        - "La ley crea la figura de 'entidad obligada': personas naturales o jurídicas, públicas o privadas, cuya actividad genera riesgos relevantes para la seguridad pública, declaradas como tales por resolución de la SPD."
        - "Los criterios de riesgo incluyen, entre otros, alta concurrencia de público, valor de los bienes protegidos, carácter estratégico de las funciones y prestación de servicios de utilidad pública; varios inmuebles GORE (edificio central, centros culturales, museos, recintos deportivos) pueden calzar en estos criterios."
        - "El GORE puede ser declarado entidad obligada de oficio por la SPD o incluso solicitar voluntariamente dicha declaración cuando el riesgo lo aconseje, lo que gatilla obligaciones específicas de seguridad privada."
      Estudio_de_Seguridad_y_Obligaciones_Asociadas:
        ID: LEY-21659-ENTIDAD-ESTUDIO-01
        Def:
          - "Una vez notificado como entidad obligada, el GORE debe elaborar y presentar a la SPD un 'estudio de seguridad' en un plazo de 60 días hábiles, el cual debe considerar las medidas físicas, tecnológicas y de personal requeridas."
          - "El estudio de seguridad requiere informe técnico de la autoridad fiscalizadora (Carabineros u otra competente) y su aprobación por la SPD; si incluye sistemas de vigilancia armada, la vigencia y requisitos son más estrictos."
          - "La vigencia del estudio aprobado es de varios años (con plazos diferenciados si contempla sistemas de vigilancia privada), siendo obligatorio su cumplimiento y actualización periódica; los antecedentes del estudio se consideran reservados por razones de seguridad."
          - "La categoría de entidad obligada implica para el GORE la incorporación de jefaturas de seguridad, contratación de vigilantes privados y la implementación de recursos tecnológicos (cámaras, controles de acceso, etc.), cuyos costos deben ser internalizados en el presupuesto de funcionamiento."

    GORE_y_Eventos_Masivos:
      ID: LEY-21659-EVENTOS-01
      Def:
        - "La ley regula los 'eventos masivos', definidos como sucesos programados con concurrencia estimada superior a un umbral de público, o de menor tamaño cuando por sus características generen riesgos relevantes; los GORE suelen promover o cofinanciar este tipo de actividades culturales, deportivas o turísticas."
        - "La noción de 'organizador' es funcional: es organizador quien dispone y coordina los medios necesarios para la realización del evento, aunque formalmente se trate de un tercero; esto es clave para determinar cuándo el GORE asume responsabilidades directas."
      Deberes_del_Organizador_y_Procedimiento_de_Autorizacion:
        ID: LEY-21659-EVENTOS-ORGANIZADOR-01
        Def:
          - "El organizador de un evento masivo debe elaborar e implementar un plan de seguridad que considere la evaluación de riesgos, el dimensionamiento de los servicios de vigilancia, los flujos de acceso/evacuación y la coordinación con autoridades."
          - "Tiene la obligación de denunciar delitos que ocurran durante el evento, entregar información a las autoridades, designar un responsable de seguridad plenamente identificado y contratar un seguro de responsabilidad civil adecuado al riesgo."
          - "Debe contratar servicios de guardias de seguridad privada y disponer de recursos tecnológicos (por ejemplo, circuitos cerrados de televisión, sistemas de control de acceso) conforme a los estándares que fije la SPD."
          - "La realización de eventos masivos requiere autorización previa de la Delegación Presidencial Regional (DPR), quien decide mediante resolución fundada luego de recabar antecedentes de SPD, Carabineros, municipalidad y otros organismos competentes."
      Responsabilidad_Solidaria_y_Riesgos_para_GORE:
        ID: LEY-21659-EVENTOS-RESPONSABILIDAD-01
        Def:
          - "La ley establece responsabilidad solidaria de los organizadores por los daños que se produzcan en el marco del evento, lo que expone al GORE a demandas civiles cuando actúa como organizador o coorganizador, incluso si la ejecución operativa recae en un tercero."
          - "El mayor riesgo jurídico se produce cuando el GORE financia o cofinancia eventos y su rol como organizador no está claramente delimitado en los convenios o contratos, ya que la definición funcional puede llevar a considerarlo corresponsable."
          - "Para mitigar estos riesgos, los convenios y bases deben asignar de forma explícita el rol de organizador a la contraparte, exigir la contratación de todos los seguros obligatorios y establecer cláusulas de indemnidad a favor del GORE frente a reclamaciones de terceros."

    Coordinacion_y_Flujos_de_Informacion:
      ID: LEY-21659-COORDINACION-01
      Def:
        - "La ley refuerza un deber general de coordinación y colaboración entre las entidades de seguridad privada, las entidades obligadas y las policías, incluyendo la obligación de denunciar delitos y poner a disposición antecedentes relevantes para la persecución penal."
        - "El GORE, como potencial entidad obligada y como actor que puede operar sistemas de vigilancia y registrar datos personales (por ejemplo, placas patentes, imágenes de cámaras), debe garantizar que el tratamiento de estos datos se ajuste a la normativa de protección de datos personales."
        - "Es recomendable que exista en el GORE una unidad o función claramente identificada (por ejemplo, una división de seguridad o prevención del delito) como nexo con SPD, DPR y Carabineros, con protocolos formales para el intercambio y resguardo de la información."

    Plan_de_Accion_Interno_Para_GORE:
      ID: LEY-21659-PLAN-ACCION-01
      Def:
        - "Realizar una auditoría de riesgos de sus inmuebles y actividades para identificar aquellos que podrían ser declarados entidad obligada y anticipar los requerimientos de estudios de seguridad y medidas asociadas."
        - "Revisar y ajustar convenios, bases de concursos y contratos vinculados a eventos culturales, deportivos o masivos financiados por el GORE, clarificando el rol de organizador, las obligaciones de seguridad y la distribución de responsabilidades civiles."
        - "Diseñar protocolos internos para la elaboración, tramitación y actualización de estudios de seguridad en caso de declaración como entidad obligada, asegurando coordinación entre División Jurídica, DAF y unidades operativas."
        - "Formalizar canales de coordinación con la Delegación Presidencial Regional y la SPD para la planificación de eventos masivos y la gestión de información de seguridad, incorporando criterios de protección de datos personales."
        - "Capacitar a equipos clave del GORE (jurídico, finanzas, divisiones sectoriales, cultura y deporte) en los contenidos básicos de la Ley 21.659 y en los riesgos asociados a la seguridad privada y los eventos masivos."

    Relevancia_Para_los_GORE:
      ID: LEY-21659-GORE-RELEVANCIA-01
      Def:
        - "La Ley 21.659 integra al GORE en un nuevo ecosistema de seguridad, en el que puede ser sujeto de obligaciones directas como entidad obligada y asumir responsabilidades relevantes al promover o coorganizar eventos masivos."
        - "Obliga al GORE a considerar la seguridad privada como una dimensión estructural de su gestión de inmuebles, programas culturales, deportivos y de fomento, incorporando costos de seguridad y seguros en la planificación presupuestaria."
        - "Refuerza la necesidad de una coordinación fluida con la SPD, la Delegación Presidencial Regional, Carabineros y otros actores de seguridad pública, distinguiendo claramente las funciones de fomento regional del GORE de las de orden público del nivel central."
        - "Gestionada proactivamente, esta normativa permite al GORE reducir riesgos de responsabilidad civil, mejorar la seguridad en eventos y espacios que financia o administra, y fortalecer la confianza ciudadana en la acción pública regional."

  Ley_21364_SINAPRED_y_GORE:
    ID: LEY-21364-GORE-MASTER-01
    Purp: "Sintetizar la Ley 21.364 que crea el Sistema Nacional de Prevención y Respuesta ante Desastres (SINAPRED) y sus reglamentos, destacando el rol del GORE en la gestión del riesgo de desastres."
    Fnd: "Ley N° 21.364 sobre SINAPRED; DS N° 234/2022 (Reglamento SINAPRED) y Reglamento N° 86/2023 sobre Organismos Técnicos para la GRD."

    Sistema_Nacional_GRD_y_Posicion_del_GORE:
      ID: LEY-21364-SISTEMA-ROL-GORE-01
      Def:
        - "La ley reemplaza el modelo reactivo centrado en ONEMI por un sistema integral de Gestión del Riesgo de Desastres (GRD), que cubre todas las fases del ciclo: mitigación, preparación, respuesta y recuperación."
        - "Organiza el sistema en niveles nacional, regional, provincial y comunal, con comités en cada nivel y una nueva institucionalidad encabezada por SENAPRED como servicio público descentralizado dependiente del Presidente vía Ministerio del Interior."
        - "El GORE pasa de tener una función genérica en emergencias (Ley 19.175, art. 16 letra k) a ser un componente orgánico de un sistema nacional jerarquizado, con responsabilidades formales en planificación, ejecución y financiamiento de medidas de GRD."
        - "Se configura una tensión estructural entre la descentralización política del GORE y la centralización funcional de la gestión del riesgo bajo el Ministerio del Interior y SENAPRED."

    Comite_Regional_de_Gestion_del_Riesgo:
      ID: LEY-21364-COMITE-REGIONAL-01
      Marco_y_Composicion:
        ID: LEY-21364-COMITE-MARCO-01
        Def:
          - "El Comité Regional para la Gestión del Riesgo de Desastres es la instancia clave a nivel regional; su presidencia recae en el Delegado Presidencial Regional (DPR), mientras que el Gobernador Regional es miembro permanente."
          - "El Director Regional de SENAPRED actúa como Secretaría Técnica y Ejecutiva del Comité, concentrando la preparación técnica, la información y la propuesta de instrumentos."
          - "El reglamento DS 234/2022 reafirma esta estructura y precisa que, en las fases de mitigación y preparación, el DPR debe actuar en coordinación con el Gobernador Regional, sin llegar a configurar una co-presidencia formal."
      Funciones_Clave:
        ID: LEY-21364-COMITE-FUNCIONES-01
        Def:
          - "El Comité Regional aprueba el Plan Regional para la Reducción del Riesgo de Desastres, el Plan Regional de Emergencia y otros instrumentos de gestión del riesgo a nivel regional."
          - "En fases de mitigación y preparación, el Comité coordina la planificación y priorización de medidas preventivas; en respuesta y recuperación, coordina la dirección de la emergencia, convocado por el DPR."
          - "El Comité recomienda proyectos para ser financiados con el Programa de Gestión del Riesgo de Desastres de SENAPRED, influyendo en la asignación de recursos nacionales a iniciativas regionales."

    Instrumentos_de_Gestion_del_Riesgo_a_Nivel_Regional:
      ID: LEY-21364-INSTRUMENTOS-REGIONALES-01
      Plan_Regional_para_la_Reduccion_del_Riesgo:
        ID: LEY-21364-PLAN-RRD-01
        Def:
          - "El Plan Regional para la Reducción del Riesgo de Desastres es elaborado técnicamente por la Dirección Regional de SENAPRED y aprobado por el Comité Regional, siendo luego sancionado por resolución del DPR."
          - "Fija objetivos, acciones y prioridades de mitigación y preparación a mediano y largo plazo, condicionando la asignación de recursos y la priorización de proyectos en la región."
          - "Debe articularse con los instrumentos propios del GORE, particularmente la Estrategia Regional de Desarrollo (ERD) y el Plan Regional de Ordenamiento Territorial (PROT), para evitar agendas paralelas y contradicciones territoriales."
      Plan_Regional_de_Emergencia:
        ID: LEY-21364-PLAN-EMERGENCIA-01
        Def:
          - "El Plan Regional de Emergencia define la organización y procedimientos para la respuesta ante eventos adversos, siguiendo un proceso de elaboración, aprobación y sanción similar al del Plan de Reducción del Riesgo."
          - "Establece roles, cadenas de mando, protocolos de activación, coordinación interinstitucional y mecanismos de comunicación con la población, integrando la participación del GORE en la fase de respuesta."
      Mapas_de_Riesgo_y_Obligacion_de_Informacion:
        ID: LEY-21364-MAPAS-RIESGO-01
        Def:
          - "La ley ordena la elaboración de Mapas de Riesgo a nivel regional por SENAPRED en coordinación con GORE, municipalidades, SEREMI MINVU y organismos técnicos especializados."
          - "El GORE está obligado a proveer la información territorial, de infraestructura y de proyectos que posea para la confección y actualización de estos mapas."
          - "Los Mapas de Riesgo deben incorporarse a los planes de gestión del riesgo y articularse con el PROT y otros instrumentos territoriales regionales, para que la localización de inversiones públicas considere explícitamente los riesgos identificados."

    Reglamentos_y_Plataformas_de_Colaboracion:
      ID: LEY-21364-REGLAMENTOS-PLATAFORMAS-01
      Reglamento_General_DS_234_2022:
        ID: LEY-21364-REGL-234-01
        Def:
          - "El DS 234/2022 detalla el funcionamiento de los Comités de GRD, confirmando su actuación en todas las fases del ciclo de riesgo y la composición del Comité Regional."
          - "Introduce las 'Plataformas para la Reducción del Riesgo de Desastres' como instancias de colaboración intersectorial a nivel nacional y regional, coordinadas por SENAPRED, en las que participan sector público (incluido el GORE), sociedad civil, academia y sector privado."
          - "Las Plataformas ejecutan acciones que los Comités Regionales les encarguen en mitigación y preparación, sirviendo como espacio para integrar la agenda de GRD en políticas sectoriales y de planificación regional."
      Reglamento_86_2023_sobre_Organismos_Tecnicos:
        ID: LEY-21364-REGL-86-01
        Def:
          - "Regula la participación de organismos técnicos en la elaboración de instrumentos de GRD, estableciendo procedimientos de consulta para la Política Nacional y los planes regionales de reducción de riesgo y de emergencia."
          - "Obliga a SENAPRED a solicitar información al GORE en la preparación de estos instrumentos y a considerar los aportes de entidades públicas, privadas y de la comunidad vía consultas públicas."
          - "Reitera la jerarquía de planes (Nacional > Regional > Provincial > Comunal) y exige consonancia entre ellos, al tiempo que reconoce la necesidad de considerar la realidad territorial local."
          - "Confirma la obligación del GORE de proporcionar información y coordinarse con SENAPRED en la elaboración de Mapas de Riesgo y en la supervisión de la ejecución de los instrumentos de GRD a nivel regional."

    Articulacion_con_Instrumentos_Propios_del_GORE:
      ID: LEY-21364-ARTICULACION-GORE-01
      Def:
        - "La existencia de nuevos instrumentos específicos de GRD (Plan Regional de Reducción de Riesgo, Plan Regional de Emergencia, Mapas de Riesgo) genera un potencial solapamiento con la ERD y el PROT del GORE si no se coordinan explícitamente."
        - "Es imprescindible que DIPLADE y las divisiones técnicas del GORE participen activamente en las consultas y procesos de elaboración de los instrumentos de GRD para incorporar la visión estratégica regional."
        - "Los objetivos y medidas de los planes de GRD deben integrarse como criterios de priorización en la cartera de inversión regional (FNDR, FRIL, otros), especialmente para obras de infraestructura crítica, equipamientos y proyectos urbanos."
        - "El PROT y los Mapas de Riesgo deben retroalimentarse mutuamente, de modo que áreas de riesgo identificadas condicionen la expansión urbana y la localización de asentamientos y servicios."

    Gobernanza_y_Tension_Descentralizacion_vs_Centralizacion:
      ID: LEY-21364-GOBERNANZA-TENSION-01
      Def:
        - "La presidencia del Comité Regional por el DPR, junto con la iniciativa técnica radicada en el Director Regional de SENAPRED, limita el liderazgo formal del Gobernador Regional en GRD, pese a ser la máxima autoridad electa de la región."
        - "La cláusula legal que indica que en mitigación y preparación el DPR actúa 'en conjunto con' el Gobernador es jurídicamente ambigua y requiere desarrollo práctico mediante protocolos y acuerdos políticos."
        - "La influencia del GORE en la agenda de GRD depende de su capacidad para construir consensos en el Comité, aportar información estratégica y vincular la planificación de riesgos con la planificación regional y la inversión FNDR."
        - "Este marco refuerza la subordinación funcional del GORE en materia de GRD a un sistema nacional centralizado, al tiempo que lo reconoce como actor clave en la implementación territorial de las políticas de riesgo."

    Financiamiento_y_Rol_Ejecutor_del_GORE:
      ID: LEY-21364-FINANCIAMIENTO-GORE-01
      Def:
        - "El Programa de Gestión del Riesgo de Desastres de SENAPRED financia instrumentos y proyectos de GRD, pero el GORE sigue siendo una fuente crítica de financiamiento a través de su presupuesto de inversión (FNDR y otros fondos)."
        - "El Comité Regional recomienda proyectos a ser financiados por el Programa de GRD, mientras que el GORE puede apalancar esos recursos con inversión regional propia para maximizar impacto."
        - "La transferencia de recursos del GORE a municipios (FRIL, Circular 33 y otros mecanismos) es un vehículo clave para implementar acciones de mitigación y preparación a nivel comunal, siempre que estén alineadas con los planes de GRD."
        - "La articulación financiera exige que los criterios de priorización del FNDR incorporen explícitamente objetivos de reducción del riesgo y resiliencia territorial definidos en los instrumentos de GRD."

    Recomendaciones_Estrategicas_para_el_GORE:
      ID: LEY-21364-RECOMENDACIONES-GORE-01
      Def:
        - "Desarrollar, junto con SENAPRED y el DPR, protocolos claros de funcionamiento del Comité Regional que den contenido a la colaboración 'en conjunto con' el Gobernador en las fases de mitigación y preparación."
        - "Asegurar la participación temprana de DIPLADE y otras divisiones técnicas del GORE en la elaboración de planes y mapas de riesgo, para que reflejen la visión estratégica y las prioridades regionales de largo plazo."
        - "Integrar los objetivos y medidas de los instrumentos de GRD en la ERD, el PROT y otros instrumentos propios del GORE, evitando duplicidades y contradicciones entre agendas."
        - "Ajustar los manuales y criterios de evaluación de proyectos de inversión regional para incluir explícitamente la contribución a la reducción del riesgo de desastres como criterio clave de priorización."
        - "Fortalecer las capacidades internas del GORE (equipos técnicos y de planificación) en materia de GRD, para poder dialogar en pie de igualdad con SENAPRED y otros organismos técnicos nacionales."

    Relevancia_Para_los_GORE:
      ID: LEY-21364-GORE-RELEVANCIA-01
      Def:
        - "La Ley 21.364 y sus reglamentos redefinen el rol del GORE en la gestión del riesgo de desastres, integrándolo en un sistema nacional que exige coordinación permanente con el nivel central y con los municipios."
        - "Obliga al GORE a incorporar la dimensión de riesgo y resiliencia en su planificación estratégica, territorial y de inversión, condicionando dónde y cómo se localizan las obras y proyectos financiados regionalmente."
        - "Refuerza la necesidad de una gobernanza regional robusta capaz de articular la agenda de GRD con la agenda de desarrollo regional, evitando que la política de desastres se convierta en un subsistema desconectado de las prioridades productivas, sociales y urbanas."
        - "Bien utilizado, este marco permite al GORE orientar sus inversiones hacia una región más resiliente, reduciendo la exposición de la población y de la infraestructura a amenazas naturales y antrópicas."

  Res_30_CGR_Rendicion_y_Control_Transferencias:
    ID: RES30-CGR-GORE-MASTER-01
    Purp: "Sintetizar la Resolución N° 30 de 2015 de la CGR sobre rendición de cuentas y control de transferencias, destacando sus exigencias y riesgos para los Gobiernos Regionales."
    Fnd: "Resolución N° 30/2015 de la Contraloría General de la República sobre procedimientos de rendición de cuentas y control interno, en el marco de la Ley 10.336 y la normativa de responsabilidad funcionaria."

    Normas_Generales_de_Rendicion:
      ID: RES30-CGR-NORMAS-GENERALES-01
      Documentacion_Minima_y_Expediente:
        ID: RES30-CGR-DOC-EXPEDIENTE-01
        Def:
          - "Establece la documentación mínima que debe contener una rendición de cuentas: informe de rendición, comprobantes de ingresos y egresos, traspasos, registros de Ley 19.862 y demás documentos de respaldo."
          - "Exige que el expediente de rendición esté completo, ordenado y disponible para la CGR, precisando que los actos de transferencia pueden complementar, pero no alterar, estas exigencias mínimas."
          - "Distingue entre expedientes en soporte papel y electrónicos, imponiendo requisitos de autenticidad, integridad y disponibilidad; los sistemas electrónicos deben ser expresamente autorizados por CGR."
      Aceptacion_de_Desembolsos_y_Continuidad_de_Servicio:
        ID: RES30-CGR-DESEMBOLSOS-01
        Def:
          - "Regla general: solo se aceptan como rendición desembolsos efectuados con posterioridad a la total tramitación del acto administrativo que autoriza el gasto o la transferencia."
          - "Como excepción, admite ciertos gastos anteriores por continuidad o buen servicio, pero exige que estas situaciones sean fundadas y consten explícitamente en el acto, evitando su uso expansivo."

    Plazos_Reintegros_y_Suspension_de_Fondos:
      ID: RES30-CGR-PLAZOS-SUSPENSION-01
      Plazo_para_Rendir_y_Reintegro_de_Saldos:
        ID: RES30-CGR-PLAZOS-REINTEGRO-01
        Def:
          - "Los plazos para rendir deben fijarse en el acto que concede los fondos y no pueden exceder en más de 30 días el plazo de ejecución de la iniciativa financiada."
          - "Los saldos no invertidos ni comprometidos al término del convenio deben ser reintegrados al GORE en un plazo acotado, normalmente 30 días desde el término del convenio."
          - "Las rendiciones no presentadas o no aprobadas generan obligación de restitución de fondos y pueden dar origen a reparos y juicios de cuentas."
      Suspension_de_Nuevas_Transferencias:
        ID: RES30-CGR-SUSPENSION-FONDOS-01
        Def:
          - "Prohíbe al GORE entregar nuevos fondos a rendir a un receptor que mantiene rendiciones exigibles pendientes, salvo casos calificados y fundados en que se otorguen garantías suficientes."
          - "Esta suspensión opera como una obligación, no como una mera facultad; su inobservancia puede constituir una falta administrativa grave para los funcionarios que autoricen nuevas remesas."
          - "Se recomienda reflejar esta regla en los convenios de transferencia, estableciendo cláusulas de suspensión automática por mora en la rendición."

    Transferencias_a_Servicios_Publicos_y_Privados:
      ID: RES30-CGR-TRANSFERENCIAS-01
      Transferencias_a_Servicios_Publicos:
        ID: RES30-CGR-TRANSF-SERVICIOS-01
        Def:
          - "En transferencias a otros servicios públicos, el GORE puede rendir ante CGR con el comprobante de ingreso emitido por el servicio receptor, pero debe exigir informes mensuales y finales sobre la inversión de los recursos."
          - "La responsabilidad por la rendición ante la CGR se desplaza principalmente al servicio receptor, sin liberar al GORE de su deber de seguimiento y control interno sobre la ejecución de los proyectos financiados."
      Transferencias_a_Privados:
        ID: RES30-CGR-TRANSF-PRIVADOS-01
        Def:
          - "En transferencias a entidades privadas, la responsabilidad del GORE es máxima: actúa como primer fiscalizador de la correcta inversión y del cumplimiento de los objetivos del convenio."
          - "El GORE debe revisar sustantivamente las rendiciones presentadas por privados, no limitarse a recibir documentos; una revisión meramente formal no lo exime de responsabilidad si la CGR objeta posteriormente la rendición."
          - "Solo en casos excepcionales y con autorización de CGR se permite que los expedientes de respaldo permanezcan en poder de la entidad privada, debiendo garantizarse el acceso irrestricto de la CGR y del GORE a estos antecedentes."

    Concepto_de_Cuentadante_y_Responsabilidad_Extendida:
      ID: RES30-CGR-CUENTADANTE-RESP-01
      Def:
        - "Define un ámbito de aplicación amplio: toda entidad que administra fondos públicos está sujeta a la resolución, y el concepto de 'cuentadante' abarca a todo funcionario que participe en la cadena de custodia, administración, inversión o pago de recursos, no solo a las autoridades superiores."
        - "Para el GORE, esto incluye a jefes de proyecto, inspectores técnicos de obras, profesionales que validan informes y gastos, así como a funcionarios de unidades financieras y de control."
        - "Refuerza el principio de responsabilidad indelegable sobre el destino final de fondos públicos: la aprobación de rendiciones por parte de funcionarios del GORE puede generar responsabilidad solidaria si CGR objeta gastos indebidos."

    Analisis_Juridico_y_Recomendaciones_Clave_Para_GORE:
      ID: RES30-CGR-ANALISIS-RECS-GORE-01
      Fortalecimiento_de_Instrumentos_y_Protocolos:
        ID: RES30-CGR-ANALISIS-INSTRUMENTOS-01
        Def:
          - "La resolución es considerada por la propia CGR como piedra angular del sistema de control financiero y probidad, por lo que el GORE debe traducirla en manuales internos, protocolos y cláusulas tipo para convenios de transferencia."
          - "Los convenios con municipios, servicios y privados deben detallar con precisión: documentación exigida, plazos perentorios de rendición, causales de suspensión de fondos, obligación de restitución y consecuencias de incumplimiento."
          - "Es crítico contar con protocolos internos claros para la revisión técnica y financiera de rendiciones, involucrando tanto a las divisiones sectoriales como a DAF y a la Unidad de Control."
      Gestion_de_Riesgos_y_Alertas_Temporales:
        ID: RES30-CGR-ANALISIS-RIESGOS-01
        Def:
          - "La Res. 30 exige que el GORE disponga de sistemas de alerta temprana para detectar rendiciones atrasadas, observadas o no aprobadas, a fin de activar oportunamente exigencias de restitución y evitar nuevos desembolsos indebidos."
          - "Una gestión proactiva de estos riesgos protege tanto el patrimonio fiscal como la responsabilidad personal de autoridades y funcionarios, reduciendo la probabilidad de reparos y juicios de cuentas."
      Rol_Preventivo_del_Equipo_Juridico_y_Unidad_de_Control:
        ID: RES30-CGR-ANALISIS-ROL-JURIDICO-01
        Def:
          - "El rol del equipo jurídico del GORE debe ser principalmente preventivo: asegurar que todos los actos administrativos y convenios vinculados a transferencias se ajusten ex ante a la Res. 30, más que limitarse a defender ex post en juicios de cuentas."
          - "La Unidad de Control y el equipo jurídico deben trabajar coordinadamente: Control audita la operación y monitorea el cumplimiento de plazos y requisitos; Jurídica proporciona el marco normativo y contractual para que la operación sea ajustada a derecho desde su origen."

    Relevancia_Para_los_GORE:
      ID: RES30-CGR-GORE-RELEVANCIA-01
      Def:
        - "La Resolución 30 es el manual operativo de la CGR para la correcta rendición y control de fondos públicos, y por tanto el marco de referencia ineludible para la gestión financiera y de transferencias del GORE."
        - "Del grado en que el GORE internalice y operacionalice estas reglas dependerán la solidez de su sistema de control interno, la calidad de sus relaciones con municipios y beneficiarios, y el nivel de exposición a reparos y juicios de cuentas."
        - "Aplicada rigurosamente, permite al GORE utilizar los instrumentos de transferencia (FNDR, FRIL, 8% y otros) como herramientas de desarrollo territorial sin comprometer la probidad ni la responsabilidad patrimonial de sus autoridades y funcionarios."
