---
urn: urn:gn:kb:gn-erd-nuble-2024-2030
nombre: gn-erd-nuble-2024-2030
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Estrategia Regional de Desarrollo Ñuble 2024 - 2030; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/02_estrategia/estrategia/kb_gn_006_erd_nuble_2024_2030_koda.yml (sha256:2ab1b80a2d9acd28ff034c8087da217e7dbe2fe5d78f9b95a19387b3c37bb871); URN KODA legado urn:gorenuble:gn:erd-nuble-2024-2030:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "02-estrategia", "estrategia", "erd", "nuble"]
familia: bok
---
# Artefacto KODA/Spec – Estrategia Regional de Desarrollo Ñuble 2024 - 2030
# Fuente: kb_gn_006_erd.md
---
_manifest:
  urn: "urn:gorenuble:gn:erd-nuble-2024-2030:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_006_erd_nuble_2024_2030_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "FS"
    created_at: "2025-12-14"
    last_modified_at: "2025-12-14"
    signature: null

ID: KB-GN-006-ERD-NUBLE-2024-2030-KODA-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
Creation-Date: 2025-12-14
Modification-Date: 2025-12-14
Ctx: "Estrategia Regional de Desarrollo de Ñuble 2024-2030: ejes, lineamientos estratégicos, objetivos estratégicos y actividades estratégicas."
Primary-Source: kb_gn_006_erd.md

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

Content:
  Src: kb_gn_006_erd.md
  Format: "Markdown"
  Body: |
    # Estrategia Regional de Desarrollo Ñuble 2024 - 2030

    LE: Lineamiento Estratégico
    OE: Objetivo Estratégico
    AE: Actividad Estratégica

    1. EJE TERRITORIO Y MEDIO AMBIENTE
       - LE 1.1. Desarrollo territorial planificado, integrado, equitativo, resiliente y sostenible
         - OE 1.1.1. Planificar el territorio de manera equilibrada e integrada
           - AE 1.1.1.1. Elaborar o actualizar los instrumentos de planificación territorial regional
           - AE 1.1.1.2. Asesorar en la elaboración de instrumentos de planificación comunal
           - AE 1.1.1.3. Identificar, diseñar e implementar de acciones para territorios especiales de la región
         - OE 1.1.2. Mejorar la infraestructura y la conectividad intraregional física y digital
           - AE 1.1.2.1. Implementar un programa prioritario de mejoramiento de la infraestructura pública de conectividad, con énfasis en caminos secundarios y conectividad digital
           - AE 1.1.2.2. Configurar una red vial, ferroviaria, marítima y aérea estructural regional e interregional
           - AE 1.1.2.3. Aumentar la disponibilidad y accesibilidad segura de espacios públicos multifuncionales con énfasis en la educación y recreación
         - OE 1.1.3. Fortalecer las capacidades resilientes regionales ante riesgos de desastres y cambio climático
           - AE 1.1.3.1. Modernizar la infraestructura y el equipamiento local para dar respuesta frente a desastres y emergencias
           - AE 1.1.3.2. Implementar medidas contenidas en el Plan Regional de Reducción de Riesgo de Desastre
           - AE 1.1.3.3. Apoyar la elaboración y ejecución del plan regional y los planes locales asociados a la ley marco de Cambio Climático
         - OE 1.1.4. Avanzar hacia la seguridad hídrica mediante el uso racional, eficiente y sostenible de los recursos hídricos regionales
           - AE 1.1.4.1. Mejorar la articulación institucional para aumentar el acceso al agua potable para consumo humano
           - AE 1.1.4.2. Desarrollar y modernizar la infraestructura de agua para riego
           - AE 1.1.4.3. Fortalecer la organización, participación y capacitación de los usuarios integrados bajo criterio territorial de cuencas hidrográficas para el uso del recurso hídrico
       - LE 1.2. Habitabilidad y servicios para el bienestar territorial
         - OE 1.2.1. Impulsar programas de mejoramiento de la habitabilidad
           - AE 1.2.1.1. Apoyar la ejecución de medidas del plan habitacional regional
           - AE 1.2.1.2. Incentivar el uso de tecnologías y fuentes de energía renovables no convencionales (ERNC) que sean más eficientes y menos contaminantes para calefacción y enfriamiento
           - AE 1.2.1.3. Fomentar el mejoramiento de aislación térmica en edificaciones y la construcción con materiales sustentables
         - OE 1.2.2. Impulsar programas de mejoramiento del acceso a servicios
           - AE 1.2.2.1. Elaborar, ejecutar y difundir plan regional de movilidad y accesibilidad sostenible
           - AE 1.2.2.2. Avanzar en el mejoramiento sanitario de los asentamientos humanos rurales de la región
         - OE 1.2.3. Avanzar en la implementación de un sistema integral de gestión de residuos sólidos domiciliario
           - AE 1.2.3.1. Formular un plan regional de gestión integral de Residuos Sólidos Domiciliarios
           - AE 1.2.3.2. Apoyar las iniciativas de economía circular en la región
       - LE 1.3. Valores ambientales del territorio promovidos, protegidos y restaurados
         - OE 1.3.1. Elevar el nivel de educación sobre valores ambientales del territorio
           - AE 1.3.1.1. Un plan de creación de conciencia sobre los valores ambientales del territorio que incluya la educación formal y actividades comunitarias
           - AE 1.3.1.2. Evaluar los programas de certificación ambiental municipal (SCAM) y de establecimientos educacionales (SCAE) para mejorar el conocimiento sobre los valores ambientales del territorio
         - OE 1.3.2. Proteger y recuperar los valores ambientales del territorio
           - AE 1.3.2.1. Conservar el estado de los valores ambientales del territorio, incluyendo programas de promoción, protección y recuperación
           - AE 1.3.2.2. Promover el desarrollo de actividades de visita y turismo de bajo impacto en áreas representativas de los valores ambientales del territorio
    2. EJE ECONOMÍA INNOVACIÓN Y CAPITAL HUMANO
       - LE 2.1. Formación, retención y atracción de capital humano especializado
         - OE 2.1.1. Promover la instalación de una cultura de innovación y creatividad
           - AE 2.1.1.1. Desarrollar la capacidad innovadora, creadora y emprendedora de la formación escolar
           - AE 2.1.1.2. Elaborar e implementar un programa de apoyo al desarrollo de talentos regionales
           - AE 2.1.1.3. Fortalecer el distrito de innovación mediante la vinculación educación superior, empresa y sector público para la inserción en la economía nacional y global
           - AE 2.1.1.4. Promover el intercambio y alianzas internacionales en materia de relevancia regional para Ñuble
         - OE 2.1.2. Retener y atraer el capital humano
           - AE 2.1.2.1. Formular un programas de incentivo para la atracción y retención de profesionales
           - AE 2.1.2.2. Generar programas de capacitación en oficios y/o certificación de competencias con criterios territoriales
           - AE 2.1.2.3. Diseñar e implementar iniciativas para la incorporación de mujeres al mercado laboral con criterios de equidad
       - LE 2.2. Economía territorial, innovadora, dinámica con producción diversificada y soporte energético, logístico y científico
         - OE 2.2.1. Diversificar territorialmente la matriz productiva
           - AE 2.2.1.1. Implementar un plan de fortalecimiento, recambio e introducción de nuevas variedades y especies agrícolas, y hortofrutícolas
           - AE 2.2.1.2. Elaborar y difundir información apropiada para incorporar adaptación, innovación y diversificación a la actividad agrícola
           - AE 2.2.1.3. Diseñar y ejecutar un programa de fortalecimiento de la producción y comercialización de alimentos saludables y plantas medicinales bajo criterios agroecológicos, orgánicos y otras certificaciones especiales
           - AE 2.2.1.4. Apoyar la diversificación y mejoramiento de la oferta de los pequeños productores agrícolas y emprendimientos rurales
           - AE 2.2.1.5. Diseñar e implementar un programa de desarrollo productivo integral de caletas pesqueras
           - AE 2.2.1.6. Diseñar e implementar un programa de apoyo al desarrollo de las industrias creativas
           - AE 2.2.1.7. Impulsar programas de Transferencia Tecnológica para mejorar la competitividad de emprendimientos creativos
         - OE 2.2.2. Desarrollar la ciencia, tecnología, innovación y conocimiento para potenciar la economía y el bienestar social
           - AE 2.2.2.1. Elaborar y ejecutar un programa regional para la incorporación de valor agregado en segmentos críticos de las cadenas productivas, especialmente en el sector silvoagropecuario y agroindustrial
           - AE 2.2.2.2. Impulsar un plan de transformación digital con aplicaciones en distintos ámbitos de la economía y sociedad regionales
           - AE 2.2.2.3. Establecer incentivos y programas de financiamiento para fomentar la inversión en actividades de investigación aplicada, desarrollo e innovación que promuevan el bienestar social
           - AE 2.2.2.4. Diseñar e implementar un programa de servicios globales de exportación
         - OE 2.2.3. Incrementar el turismo regional fomentando nuevos productos y articulando la oferta existente con énfasis en Turismo de Intereses Especiales
           - AE 2.2.3.1. Diseñar y ejecutar una estrategia de promoción de la oferta turística formalizada
           - AE 2.2.3.2. Identificar nuevos atractivos turísticos, facilitar el acceso e integrarlos en las cadenas de valor del turismo
           - AE 2.2.3.3. Ejecutar la política regional de turismo con énfasis en la formalización de servicios y experiencia del visitante
           - AE 2.2.3.4. Capacitar y transferir buenas prácticas que promuevan el turismo sostenible en la región
           - AE 2.2.3.5. Implementar soluciones tecnológicas inteligentes para optimizar la gestión de destinos turísticos
           - AE 2.2.3.6. Elaborar un programa de formación de capital humano para el desarrollo del turismo regional con Identidad territorial
         - OE 2.2.4. Fortalecer el capital social para la innovación y la creación de valor
           - AE 2.2.4.1. Impulsar la articulación y asociatividad de los productores, en particular de la Agricultura Familiar Campesina (AFC), para su vinculación con cadenas de valor regionales y/o globales
           - AE 2.2.4.2. Fomentar que la Agricultura Familiar Campesina sea reconocida a través de un sello de certificación de calidad
           - AE 2.2.4.3. Impulsar el emprendimiento de jóvenes con atención a la superación de barreras de entrada a la participación en la actividad productiva
           - AE 2.2.4.4. Elaborar un programa de mejoramiento de las condiciones de producción y empleo rural
         - OE 2.2.5. Propender a una matriz energética sostenible y diversificada, segura, eficiente y carbono neutral que cubre las necesidades presentes y futuras
           - AE 2.2.5.1. Diagnosticar las necesidades de suministro de energía y elaborar programa para mejorar la seguridad y estabilidad del suministro
           - AE 2.2.5.2. Promover y desarrollar iniciativas que permitan avanzar en la reducción de costos de consumo y en la incorporación de energías renovables no convencionales (ERNC), especialmente en lugares apartados
           - AE 2.2.5.3. Generar programas de eficiencia energética en la industria
           - AE 2.2.5.4. Fomentar la descarbonización en la generación de energía en la región
         - OE 2.2.6. Poner en valor la región como centro logístico macro regional
           - AE 2.2.6.1. Formular plan estratégico para el desarrollo de la logística regional
           - AE 2.2.6.2. Diseñar e implementar programa de fomento a la generación de ofertas de servicios logísticos con incorporación de fuentes de energías limpias autónomas
           - AE 2.2.6.3. Ejecutar programa para la atracción de nuevas inversiones y capacitación asociada a la industria logística
           - AE 2.2.6.4. Fortalecer los servicios logísticos de Ñuble asociados a la industria vitivinícola de la macroregión
    3. EJE DESARROLLO SOCIAL INCLUSIVO
       - LE 3.1. Bienestar, seguridad y calidad de vida para las personas de Ñuble
         - OE 3.1.1. Reducir la pobreza y la vulnerabilidad de la población regional
           - AE 3.1.1.1. Determinar y caracterizar las variables que más inciden en la situación de pobreza regional, para priorizar estrategias de intervención con pertinencia territorial
           - AE 3.1.1.2. Elaborar programa para la educación, prevención, promoción y protección de los derechos de la infancia y la adolescencia, con énfasis en la atención del grupo cuyos derechos han sido vulnerados
           - AE 3.1.1.3. Diseño e implementación de plan regional de seguridad pública, con especial consideración en la atención de territorios priorizados
           - AE 3.1.1.4. Promover iniciativas de recuperación de espacios públicos para la revitalización de la convivencia en los territorios más vulnerables
           - AE 3.1.1.5. Programa de apoyo integral a familias que viven en campamentos para la obtención de la vivienda definitiva
           - AE 3.1.1.6. Diseñar y ejecutar programas orientados al incremento del ingreso autónomo de las personas en situación de pobreza
           - AE 3.1.1.7. Diseñar y ejecutar programas de acompañamiento a cuidadores de personas en estado de vulnerabilidad y/o dependencia
           - AE 3.1.1.8. Facilitar la integración social, económica y cultural de población inmigrante
         - OE 3.1.2. Fortalecer el acceso a la salud de calidad y promover estilos de vida saludable
           - AE 3.1.2.1. Diseñar y ejecutar los componentes del Polo de Salud de Ñuble
           - AE 3.1.2.2. Elaborar, fortalecer o potenciar programas de acceso para prevenir el cáncer y enfermedades no transmisibles más comunes en la región
           - AE 3.1.2.3. Apoyar un programa de fortalecimiento actual de la red de salud pública con énfasis en ampliación de cobertura, mejoramiento de infraestructura, equipamiento y aumento de especialidades médicas
           - AE 3.1.2.4. Ampliar cobertura del programa de educación, prevención, tratamiento y rehabilitación del consumo de alcohol y drogas, con pertinencia territorial
           - AE 3.1.2.5. Implementar estudio de sedentarismo por comunas
           - AE 3.1.2.6. Impulsar programa para ampliar la cobertura de atención en salud mental para los habitantes de la región
           - AE 3.1.2.7. Mejorar la calidad atención de los usuarios de la red de salud pública
           - AE 3.1.2.8. Avanzar en la implementación de un sistema regional integrad de información de salud orientado a lograr la trazabilidad de la historia clínica de los beneficiarios
         - OE 3.1.3. Incentivar la educación integral para el desarrollo de habilidades personales y la convivencia social
           - AE 3.1.3.1. Introducir la formación cívica en la educación pública regional
           - AE 3.1.3.2. Innovar en técnicas pedagógicas y contenidos para el proceso enseñanza-aprendizaje en la aula
           - AE 3.1.3.3. Desarrollar iniciativas que apunten al mejoramiento de la convivencia social, fortaleciendo habilidades y destrezas personales e interpersonales
           - AE 3.1.3.4. Elaborar programa para facilitar el acceso a la educación superior
         - OE 3.1.4. Promover políticas, programas y acciones para disminuir la violencia de género
           - AE 3.1.4.1. Fortalecer programas y campañas de sensibilización, prevención y denuncia de situaciones de violencia de género
           - AE 3.1.4.2. Aumentar cobertura territorial y acompañamiento continuo de programas que estimulen la autonomía económica de las mujeres
           - AE 3.1.4.3. Fortalecer los espacios de convivencia y formación de redes de apoyo mutuo entre mujeres
           - AE 3.1.4.4. Diseñar e implementar un observatorio regional para el estudio y seguimiento de políticas de género y diversidad sexual
       - LE 3.2. Inclusión Social
         - OE 3.2.1. Promover el bienestar integral de las personas mayores
           - AE 3.2.1.1. Diseñar e implementar programas de mejoramiento de infraestructura, del entorno y movilidad de personas mayores con incorporación de tecnologías apropiadas
           - AE 3.2.1.2. Desarrollar programas de vivienda con condiciones especiales de habitabilidad para personas mayores, a nivel urbano y rural
           - AE 3.2.1.3. Implementar acciones de acompañamiento en espacios públicos adecuados a las carencias de redes de apoyo, con énfasis en aquellos que se encuentran con algún nivel de situación de dependencia
           - AE 3.2.1.1. Diseñar e implementar programas de mejoramiento de infraestructura, del entorno y movilidad de personas mayores con incorporación de tecnologías apropiadas. (Repetido)
         - OE 3.2.2. Contribuir a la generación de igualdad para personas con discapacidad y neurodivergentes
           - AE 3.2.2.1. Generar programas y campañas de sensibilización para abordar las particularidades de las personas en situación de discapacidad y/o neurodivergencias
           - AE 3.2.2.2. Desarrollar iniciativas para el mejoramiento de la accesibilidad universal en servicio público y privados
           - AE 3.2.2.3. Impulsar adaptación y construcción de espacios públicos adecuados a la diversidad de personas con discapacidad y neurodivergencia
           - AE 3.2.2.4. Apoyar la integración laboral de las personas con discapacidad y neurodivergencia
    4. EJE PATRIMONIO, CULTURAL E IDENTIDAD
       - LE 4.1. Desarrollo del ambiente creativo, artístico, cultural e identitario
         - OE 4.1.1. Fortalecer la gestión cultural de la región de Ñuble
           - AE 4.1.1.1. Potenciar la gestión cultural regional a través de la vinculación entre actores públicos y privados
           - AE 4.1.1.2. Elaborar programa de apoyo para el mejoramiento y creación de nuevos espacios culturales sociales, virtuales e infraestructura con pertinencia territorial
           - AE 4.1.1.3. Desarrollar iniciativas de fortalecimiento a la programación cultural y formación de audiencias
           - AE 4.1.1.4. Elaborar un programa de desarrollo equitativo de actividades culturales y artísticas, con énfasis en la coherencia territorial y diversificación de temáticas
           - AE 4.1.1.5. Desarrollar la Política Regional de Cultura que ponga en valor las identidades de la región, especialmente lo rural y campesino, y otras como la de los pueblos originarios
           - AE 4.1.1.6. Crear el complejo Archivo-Museo-Depósito y Biblioteca Regional que resguarde y haga pública información básica del patrimonio cultural y natural, y de las economías creativas
         - OE 4.1.2. Contribuir al desarrollo de las economías creativas
           - AE 4.1.2.1. Potenciar la vinculación entre los diferentes actores regionales, nacionales e internacionales pertenecientes a los ciclos culturales
           - AE 4.1.2.2. Promover y difundir las diferentes áreas creativas de la región
         - OE 4.1.3. Contribuir a la identificación y visibilización de las identidades de la región
           - AE 4.1.3.1. Elaborar estudio de las identidades regionales, con énfasis en rescate de memorias colectivas, tradiciones locales y creación de relatos regionales
           - AE 4.1.3.2. Elaborar programa de gestión y difusión de las identidades locales, que promueva el uso de elementos identitarios contribuyente a una identidad regional, en municipios, servicios públicos, instituciones de educación, entre otros
           - AE 4.1.3.3. Visibilizar la herencia y la presencia de personas y organizaciones pertenecientes a pueblos originarios y atender necesidades de sus integrantes con pertinencia cultural
       - LE 4.2. Sustentabilidad del patrimonio cultural y natural de la región de Ñuble
         - OE 4.2.1. Fomentar la investigación y puesta en valor del patrimonio cultural, material e inmaterial y natural
           - AE 4.2.1.1. Poner en valor las diferentes expresiones de patrimonio cultural inmaterial, ampliando planes de salvaguarda
           - AE 4.2.1.2. Preparar y acompañar a las comunidades locales para el desarrollo turístico cultural y natural
           - AE 4.2.1.3. Elaborar programa de puesta en valor del patrimonio alimentario de la región de Ñuble
           - AE 4.2.1.4. Investigar y difundir el patrimonio regional, cultural —material e inmaterial—, y natural, tanto a nivel local, como nacional. Con énfasis en el patrimonio arqueológico
           - AE 4.2.1.5. Programa de conservación y mejoramiento del patrimonio arquitectónico urbano y rural, incluyendo vivienda, zonas de conservación y zonas típicas
           - AE 4.2.1.6. Valorizar el patrimonio tangible e intangible de la región, a través de la educación y el turismo
           - AE 4.2.1.7. Implementar programas formativos en el sistema educativo nacional y regional, que permitan fortalecer habilidades, oficios, artes y culturas
    5. EJE INSTITUCIONALIDAD Y GOBERNANZA REGIONAL
       - LE 5.1. Institucionalidad pública descentralizada y desconcentrada que destaca por su probidad y transparencia
         - OE 5.1.1. Consolidar la institucionalidad pública integrada y en coherencia con los instrumentos de desarrollo y planificación
           - AE 5.1.1.1. Caracterizar las necesidades presupuestarias, de infraestructura para la eficiencia de la gestión pública
           - AE 5.1.1.2. Implementar la presencia de la institucionalidad pública en la región en coherencia con las necesidades territoriales
           - AE 5.1.1.3. Fomentar la colaboración y articulación pública privada para impulsar proyectos emblemáticos regionales
         - OE 5.1.2. Formar gestores públicos con perspectiva multinivel para la descentralización y la desconcentración
           - AE 5.1.2.1. Impulsar una oferta programática de capacitaciones, dirigida a directivos y funcionarios públicos, y otros actores del territorio para fortalecer la descentralización
           - AE 5.1.2.2. Potenciar redes formativas entre servicios públicos, Gobierno Regional, municipios, academia y sociedad civil orientado a la cualificación del capital humano
         - OE 5.1.3. Potenciar innovaciones tecnológicas para favorecer una gestión de calidad
           - AE 5.1.3.1. Potenciar la alfabetización digital, con amplios criterios de inclusión ciudadana
         - OE 5.1.4. Fortalecer mecanismos de control que aseguren un ejercicio de gestión pública con transparencia y probidad
           - AE 5.1.4.1. Asegurar el acceso a la información a la ciudadanía, con mecanismos definidos y seguimiento
           - AE 5.1.4.2. Evaluar de forma continua las acciones implementadas por el sistema de integridad pública regional
       - LE 5.2. Participación y gobernanza multinivel con equidad territorial
         - OE 5.2.1. Formalizar y promover mecanismos y niveles de participación para las políticas públicas regionales
           - AE 5.2.1.1. Formalizar los niveles de participación en el marco de la política regional de participación ciudadana
           - AE 5.2.1.2. Potenciar la participación ciudadana para apoyar la formulación e implementación de políticas públicas inclusivas con pertinencia territorial
         - OE 5.2.2. Impulsar una gestión pública integrada, a nivel subregional, con criterios de equidad territorial
           - AE 5.2.2.1. Promover la planificación estratégica, por territorios subregionales, considerando criterios sociales, culturales, económicos y ambientales
           - AE 5.2.2.2. Reforzar la integración entre instrumentos de planificación estratégica a nivel comunal y regional
           - AE 5.2.2.3. Gestionar la transferencia de nuevas competencias detonantes del desarrollo regional
