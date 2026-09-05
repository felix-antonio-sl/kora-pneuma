---
urn: urn:gn:kb:gn-estrategia-gestion
nombre: gn-estrategia-gestion
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Estrategia y Gestión del GORE en Chile; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/kb_gn_035_estrategia_gestion_koda.yml (sha256:8a2d2764a3ca7363a0abb4fd6666ec65b93402c16f959afd671642cc3ca75f8f); URN KODA legado urn:gorenuble:gn:estrategia-gestion:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2024-06-30
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "estrategia"]
familia: bok
---
# Artefacto KODA/Spec – Estrategia y Gestión del GORE en Chile
# Fuente principal: kb_gn_035_estrategia_gestion.md

_manifest:
  urn: "urn:gorenuble:gn:estrategia-gestion:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_035_estrategia_gestion_koda.yml"
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

ID: KB-GN-035-ESTRATEGIA-GESTION-STS
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FSA
Human-Editor: IA-GEMINI
Model-Collaborator: IA-GEMINI
AI-Remediator: KODA-TRANSFORMER
Creation-Date: "2024-06-30"
Modification-Date: "2024-07-31"
Primary-Source: "kb_gn_035_estrategia_gestion_gn.md"
Ref-STS-Guide: "GUIDE-STS-MASTER-01"
Ctx: "Guía integral de estrategia, gestión pública y modernización institucional aplicada a Gobiernos Regionales (GORE) de Chile, con foco aplicable al GORE de Ñuble."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning, Just->Justification, Rec->Recommendation, Dest->Destination.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx: or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_Conceptos_Clave:
  ID: GORE-ESTRATEGIA-GESTION-GLOSARIO-01
  Purp: "Sintetizar conceptos y siglas clave utilizados en la guía de estrategia y gestión del GORE."
  Terminos:
    - ID: GORE-GLOS-GORE
      Sigla: "GORE"
      Nombre: "Gobierno Regional"
      Def: "Entidad pública autónoma de nivel regional, con personalidad jurídica y patrimonio propio, encargada de la administración superior de la región."
    - ID: GORE-GLOS-CORE
      Sigla: "CORE"
      Nombre: "Consejo Regional"
      Def: "Órgano colegiado del GORE, con facultades normativas, resolutivas y fiscalizadoras."
    - ID: GORE-GLOS-ERD
      Sigla: "ERD"
      Nombre: "Estrategia Regional de Desarrollo"
      Def: "Instrumento rector de largo plazo que define visión, ejes y objetivos estratégicos del desarrollo regional."
    - ID: GORE-GLOS-PROT
      Sigla: "PROT"
      Nombre: "Plan Regional de Ordenamiento Territorial"
      Def: "Instrumento que orienta el uso del territorio y la localización de inversiones."
    - ID: GORE-GLOS-FNDR
      Sigla: "FNDR"
      Nombre: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fondo de inversión de los GORE para proyectos de desarrollo regional."
    - ID: GORE-GLOS-FRIL
      Sigla: "FRIL"
      Nombre: "Fondo Regional de Iniciativa Local"
      Def: "Fondo orientado a proyectos de infraestructura local de menor escala, ejecutados principalmente por municipalidades."
    - ID: GORE-GLOS-FRPD
      Sigla: "FRPD"
      Nombre: "Fondo Regional para la Productividad y el Desarrollo"
      Def: "Fondo financiado por Royalty Minero para iniciativas de productividad, innovación y desarrollo regional."
    - ID: GORE-GLOS-SNI
      Sigla: "SNI"
      Nombre: "Sistema Nacional de Inversiones"
      Def: "Marco y plataforma para evaluación técnico-económica de inversiones públicas."
    - ID: GORE-GLOS-VALOR-PUBLICO
      Nombre: "Valor Público"
      Def: "Mejora concreta y sostenible en la calidad de vida de las personas y el desarrollo de la región, derivada de la acción del Estado."
    - ID: GORE-GLOS-IPR
      Sigla: "IPR"
      Nombre: "Intervención Pública Regional"
      Def: "Término paraguas para proyectos, programas y otras iniciativas financiadas por el GORE."

    - ID: GORE-GLOS-DPR
      Sigla: "DPR"
      Nombre: "Delegado Presidencial Regional"
      Def: "Representante del Presidente de la República que ejerce el gobierno interior de la región y coordina servicios públicos nacionales."
    - ID: GORE-GLOS-SEREMI
      Sigla: "SEREMI"
      Nombre: "Secretaría Regional Ministerial"
      Def: "Representante regional de un ministerio, responsable de implementar políticas sectoriales en la región."
    - ID: GORE-GLOS-DIPIR
      Sigla: "DIPIR"
      Nombre: "División de Presupuesto e Inversión Regional"
      Def: "División del GORE encargada de elaborar, ejecutar y controlar el presupuesto de inversión regional."
    - ID: GORE-GLOS-DIPLADE
      Sigla: "DIPLADE"
      Nombre: "División de Planificación y Desarrollo Regional"
      Def: "División responsable de formular instrumentos de planificación y coordinar la estrategia de desarrollo regional."
    - ID: GORE-GLOS-DAF
      Sigla: "DAF"
      Nombre: "División de Administración y Finanzas"
      Def: "División encargada de la gestión administrativa interna, finanzas, recursos humanos y abastecimiento del GORE."
    - ID: GORE-GLOS-DIDESOH
      Sigla: "DIDESOH"
      Nombre: "División de Desarrollo Social y Humano"
      Def: "División encargada de programas e iniciativas orientadas a cohesión social, inclusión y acceso a servicios."
    - ID: GORE-GLOS-UCI
      Sigla: "UCI"
      Nombre: "Unidad de Control Interno"
      Def: "Unidad asesora del GORE que impulsa gestión de riesgos, control interno y mejora de procesos, y actúa como contraparte técnica de la Contraloría."
    - ID: GORE-GLOS-COSOC
      Sigla: "COSOC"
      Nombre: "Consejo de la Sociedad Civil Regional"
      Def: "Órgano consultivo de participación ciudadana del GORE, regulado por la Ley N°20.500 y la Ley N°21.074."
    - ID: GORE-GLOS-CCTID
      Sigla: "CCTID"
      Nombre: "Comité Regional de Ciencia, Tecnología e Innovación para el Desarrollo"
      Def: "Órgano asesor del GORE en materias de ciencia, tecnología e innovación para el desarrollo regional."
    - ID: GORE-GLOS-SIGFE
      Sigla: "SIGFE"
      Nombre: "Sistema de Información para la Gestión Financiera del Estado"
      Def: "Sistema contable-financiero oficial donde se registran los movimientos presupuestarios del GORE."
    - ID: GORE-GLOS-RF
      Sigla: "RF"
      Nombre: "Recomendación Favorable"
      Def: "Resultado favorable de evaluación de programas en Glosa 06 u otros mecanismos de programas públicos."
    - ID: GORE-GLOS-MML
      Sigla: "MML"
      Nombre: "Metodología Marco Lógico"
      Def: "Herramienta de planificación y gestión de proyectos y programas orientada a resultados."
    - ID: GORE-GLOS-PMO
      Sigla: "PMO"
      Nombre: "Oficina de Gestión de Proyectos"
      Def: "Unidad responsable de estandarizar y profesionalizar la gestión de cartera de proyectos y programas del GORE."
    - ID: GORE-GLOS-SINAPRED
      Sigla: "SINAPRED"
      Nombre: "Sistema Nacional de Prevención y Respuesta ante Desastres"
      Def: "Sistema que organiza la gestión del riesgo de desastres en Chile, asignando roles específicos a los gobiernos regionales."

Parte_I_Fundamentos_Gestion_Publica_Regional:
  ID: GORE-FUNDAMENTOS-01
  Titulo: "Parte I: Fundamentos de la Gestión Pública Regional en Chile"
  Purp: "Establecer fundamentos conceptuales y contextuales de la gestión pública regional y del rol de los GORE en Chile."
  Ref:
    - GORE-GLOS-GORE
    - GORE-GLOS-CORE

  Desafio_Gestion_Publica_Regional:
    ID: GORE-FUNDAMENTOS-DESAFIO-01
    Purp: "Caracterizar los desafíos y singularidades de la gestión pública en los Gobiernos Regionales chilenos."
    Ctx: "Nivel de análisis: GORE, en el marco de Estado unitario y descentralización en curso."

    Singularidad_Gestion_GORE:
      ID: GORE-FUNDAMENTOS-GESTION-SINGULARIDAD-01
      Conceptos:
        - Cpt: "Principio-Actuacion-Directivo-Publico"
          Ctx: "Comparación Gerente Privado vs Directivo Público Regional."
          Nat:
            - "Gerente privado puede hacer todo lo que la ley no prohíbe."
            - "Directivo público solo puede hacer lo que la ley permite expresamente."
          Fnd: "Característica central del Estado de Derecho."
          Purp: "Limitar la arbitrariedad y asegurar ejercicio del poder público dentro de cauces normativos."

        - Cpt: "Marco-Juridico-GORE"
          ID: GORE-MARCO-JURIDICO-01
          Def: "Conjunto de normativas que rigen creación, organización y funcionamiento de los GORE."
          Componentes:
            - "Constitución Política de la República."
            - "Ley 19.175: Ley Orgánica Constitucional sobre Gobierno y Administración Regional (DFL N°1-19.175/2005)."
            - "Ley 21.074: Fortalecimiento de la Regionalización, que modifica sustantivamente la Ley 19.175."

        - Cpt: "Autonomia-GORE"
          ID: GORE-AUTONOMIA-01
          Src: "Normativa del marco jurídico GORE."
          Nat:
            - "Personas jurídicas de derecho público."
            - "Patrimonio propio."
            - "Autonomía para administrar asuntos de su competencia."
          Cond: "La autonomía se ejerce en un Estado unitario, requiriendo coordinación con políticas y directrices nacionales."

        - Cpt: "Ecosistema-Stakeholders-GORE"
          ID: GORE-STAKEHOLDERS-01
          Nat: "Complejidad de actores y relaciones."
          Stakeholders:
            - "Consejo Regional (CORE)."
            - "Delegado Presidencial Regional (DPR)."
            - "SEREMIs y servicios públicos desconcentrados."
            - "Municipios de la región."
            - "Organizaciones de la sociedad civil."
            - "Sector privado regional."
            - "Órganos de control (CGR, otros)."
          Req: "El directivo GORE requiere alta capacidad de articulación y liderazgo político-técnico."

  Proposito_y_Valor_Publico_Regional:
    ID: GORE-FUNDAMENTOS-VALOR-PUBLICO-01
    Purp: "Definir el propósito fundamental del GORE y su rol en la creación de valor público regional."

    Proposito_Fundamental_GORE:
      ID: GORE-PROPOSITO-FUNDAMENTAL-01
      Src: "Ley 19.175."
      Def: "Impulsar el desarrollo social, cultural y económico de la región."
      Res: "Creación de valor público para sus habitantes."

    Definicion_Valor_Publico_Regional:
      ID: GORE-VALOR-PUBLICO-REGIONAL-01
      Ctx: "Aplicado a la acción del GORE."
      Res: "Mejora concreta y sostenible de la calidad de vida en el territorio regional."
      Ref:
        - GORE-GLOS-VALOR-PUBLICO
        - GORE-GLOS-ERD
        - GORE-GLOS-PROT
      Instrumentos_Clave:
        - Cpt: "Estrategia Regional de Desarrollo (ERD)."
          ID: GORE-INSTRUMENTO-ERD-01
        - Cpt: "Plan Regional de Ordenamiento Territorial (PROT)."
          ID: GORE-INSTRUMENTO-PROT-01

    Actuaciones_Creacion_Valor:
      ID: GORE-ACTUACIONES-VALOR-01
      Ref:
        - GORE-FUNDAMENTOS-MOTOR-VALOR-01
      Act:
        - "Identificar y responder a necesidades y prioridades de la población regional."
        - "Diseñar e implementar políticas, planes, programas y proyectos de inversión pertinentes, eficaces y eficientes (ej. FNDR, FRPD, FRIL)."
        - "Fomentar participación ciudadana en la toma de decisiones."
        - "Abordar fallas de valor público que el mercado y otros niveles del Estado no cubren."

    Motor_Valor_Cinco_Procesos:
      ID: GORE-FUNDAMENTOS-MOTOR-VALOR-01
      Purp: "Adaptar la lógica de modelo de negocio para identificar cinco procesos esenciales del GORE."
      Cpt: "Falla en uno de los procesos compromete el sistema completo."
      Procesos:
        - Cpt: "Creacion-Valor-Publico"
          Def: "Descubrir necesidades y diseñar soluciones (políticas, programas, proyectos)."
        - Cpt: "Comunicacion-Estrategica-y-Legitimidad"
          Def: "Comunicar valor creado y construir apoyo y legitimidad."
        - Cpt: "Adopcion-y-Participacion-Ciudadana"
          Def: "Convertir el interés en acción concreta de ciudadanía y socios."
        - Cpt: "Provision-y-Entrega-de-Valor"
          Def: "Ejecutar eficaz y eficientemente lo prometido."
        - Cpt: "Sostenibilidad-Financiera-y-Presupuestaria"
          Def: "Gestionar recursos para mantener continuidad operacional y de inversión."

  Aprendizajes_Gestion_Publica_Latinoamericana:
    ID: GORE-FUNDAMENTOS-APRENDIZAJES-LATAM-01
    Purp: "Extraer aprendizajes de la experiencia latinoamericana en gestión pública e implementación."
    Conceptos:
      - Cpt: "Desafio-Implementacion"
        Def: "No basta formular buenas estrategias; sin capacidad de gestión, procesos adecuados y voluntad política, los resultados no se materializan."
      - Cpt: "Foco-en-Gestion-sobre-Politica-Contingente"
        Req: "La gestión técnica orientada a resultados no debe supeditarse a clientelismo, cálculos electorales de corto plazo ni capturas institucionales."
      - Cpt: "Construccion-Capacidades-Institucionales"
        Act:
          - "Invertir en desarrollo de equipos humanos."
          - "Modernizar sistemas de gestión."
          - "Adoptar buenas prácticas de gestión."
      - Cpt: "Rendicion-Cuentas-y-Transparencia"
        Act: "Fortalecer transparencia (activa y pasiva) y comunicar impacto de la gestión del GORE."

  GORE_y_Entorno:
    ID: GORE-ENTORNO-MARCO-ACTUACION-01
    Purp: "Comprender la posición del GORE en el Estado unitario descentralizado, tensiones intergubernamentales y herramientas de intervención."
    Ref:
      - GORE-GLOS-GORE
      - GORE-GLOS-CORE

    GORE_en_Estado_Unitario:
      ID: GORE-ENTORNO-ESTADO-UNITARIO-01
      Ctx: "Marco constitucional y legal que define posición del GORE."
      Conceptos:
        - Cpt: "Estado-Chile"
          Nat:
            - "Estado unitario."
          Principios:
            - "Administración del Estado funcional y territorialmente descentralizada o desconcentrada."
        - Cpt: "GORE-en-Estado"
          Def: "Principal expresión de administración descentralizada a nivel regional."
          Regulacion:
            - "Ley 19.175 (LOC GORE)."
            - "Ley 21.074 (Fortalecimiento de la Regionalización)."
          Cambios_Clave_Ley_21074:
            - "Elección directa de Gobernadores Regionales."
            - "Rediseño de estructura interna del GORE."
            - "Ampliación de competencias y mecanismo formal de transferencia."

    Tensiones_Politicas_Intergubernamentales:
      ID: GORE-ENTORNO-TENSIONES-01
      Purp:
        - "Entender el conflicto intergubernamental como rasgo inherente de sistemas descentralizados."
        - "Identificar impulsores y tipos de fricción para diseñar estrategias del GORE."
      Impulsores:
        - "Descentralización: devolución de poder a niveles subnacionales con electorados propios."
        - "Democratización: doble legitimidad democrática entre autoridades nacionales y subnacionales."
        - "Liberalización: reformas de mercado con ganadores y perdedores territoriales."
      Tipos_Friccion:
        - "Vertical: GORE vs Gobierno Central (recursos, competencias, autonomía)."
        - "Horizontal: GORE vs Municipios u otras regiones (competencia por recursos e influencia)."
      Estrategia_GORE:
        Act:
          - "Construir coaliciones horizontales y verticales para superar vulnerabilidad e aislamiento."

    Principios_Descentralizacion_Fiscal:
      ID: GORE-ENTORNO-PRINCIPIOS-FISCALES-01
      Purp: "Sintetizar principios económicos de diseño fiscal para GORE."
      Asignacion_Gasto:
        ID: GORE-PRINCIPIOS-GASTO-01
        Fnd: "Finance must follow function."
        Principios:
          - "Correspondencia: jurisdicción coincide con área beneficiaria del servicio."
          - "Subsidiariedad: responsabilidad al nivel más bajo compatible con área de beneficio."
          - "Rendición de cuentas: mayor eficiencia cuando gasto se financia con recursos de sus propios votantes."
      Asignacion_Ingresos:
        ID: GORE-PRINCIPIOS-INGRESO-01
        Principios:
          - "Impuestos sobre bases móviles deben ser centrales para evitar competencia fiscal dañina."
          - "Impuestos sobre bases inmóviles son adecuados para SNG."
          - "Impuestos redistributivos deben ser nacionales."
          - "Impuestos subnacionales deben ser visibles a votantes."
      Transferencias_Intergubernamentales:
        ID: GORE-PRINCIPIOS-TRANSFERENCIAS-01
        Obj:
          - "Cerrar desequilibrios fiscales verticales."
          - "Corregir desequilibrios fiscales horizontales (ecualización)."
          - "Compensar externalidades."
          - "Asegurar estándares mínimos en bienes preferentes."
          - "Alinear prioridades subnacionales con objetivos nacionales."

    Formas_Intervencion_GORE:
      ID: GORE-ENTORNO-INTERVENCION-01
      Purp: "Detallar herramientas de intervención: sermones, zanahorias y garrotes."
      Sermones:
        Cpt: "Informacion-Planificacion-Coordinacion"
        Act:
          - "Planificación estratégica (ERD, PROT, otros planes regionales)."
          - "Coordinación interinstitucional."
          - "Promoción y difusión (identidad regional, turismo, oportunidades)."
      Zanahorias:
        Cpt: "Inversion-Fomento-Programas"
        Act:
          - "Inversión pública con FNDR y otros fondos."
          - "Fomento productivo vía FRPD."
          - "Programas sociales y de desarrollo, subvenciones 8% FNDR."
          - "Apoyo a municipios mediante transferencias y asistencia técnica."
      Garrotes:
        Cpt: "Potestad-Normativa-y-Fiscalizacion"
        Nat: "Poder coercitivo directo limitado, pero con herramientas normativas y regulatorias."
        Act:
          - "Ordenanzas y reglamentos regionales dentro de competencias."
          - "Fiscalización del CORE."
          - "Rol en ordenamiento territorial (PRI, incidencia en PRC)."

    Ciclo_Politicas_Publicas_en_GORE:
      ID: GORE-ENTORNO-CICLO-POLITICAS-01
      Purp: "Describir ciclo completo desde definición estratégica hasta evaluación y retroalimentación."
      Fases:
        - "Fase 1: Definición de la política pública regional (ERD, PROT, participación)."
        - "Fase 2: Gestión y asignación de recursos (DIPLADE, DIPIR, DAF; presupuesto regional y fondos)."
        - "Fase 3: Implementación (ejecución directa del GORE y vía convenios)."
        - "Fase 4: Resultados (outputs y outcomes, comunicación centrada en impacto)."
        - "Fase 5: Evaluación (control interno, control externo, evaluación de inversiones y programas)."
        - "Fase 6: Retroalimentación (actualización ERD, planes, reasignación de recursos)."

    GORE_y_Problemas_Wicked:
      ID: GORE-ENTORNO-WICKED-PROBLEMS-01
      Cpt: "Problemas complejos, interdependientes y sin soluciones únicas (pobreza multidimensional, seguridad, cambio climático, equidad territorial)."
      Req: "Adoptar pensamiento sistémico, colaboración y co-creación de soluciones; la suma de acciones aisladas no basta."

    GORE_en_Red:
      ID: GORE-ENTORNO-RED-01
      Cpt: "Transición de modelo burocrático tradicional a 'Estado en red' ciudadano-céntrico, colaborativo e interoperable."
      Ejes:
        - "Gestion ciudadano-céntrica (diseño de servicios desde el usuario)."
        - "Colaboración interinstitucional (nivel central, municipios, sociedad civil y sector privado)."
        - "Interoperabilidad y transformación digital (Ley 21.180, plataformas SIGFE, BIP, ChileIndica)."

  Directivo_Publico_Regional_y_Liderazgo:
    ID: GORE-DIRECTIVO-01
    Purp: "Analizar rol, desafíos y competencias del directivo público regional en el GORE."

    Perfiles_Clave_Direccion_GORE:
      ID: GORE-DIRECTIVO-PERFILES-01
      Perfiles:
        - Cpt: "Gobernador/a Regional"
          ID: GORE-ROL-GOBERNADOR-01
          Nat: "Máxima autoridad ejecutiva regional, elegida democráticamente."
          Resp:
            - "Liderar formulación ERD."
            - "Proponer presupuesto regional."
            - "Coordinar acción integral del GORE."
        - Cpt: "Administrador/a Regional"
          ID: GORE-ROL-ADMINISTRADOR-01
          Nat: "Funcionario de exclusiva confianza del Gobernador/a."
          Resp:
            - "Gestión administrativa y coordinación de divisiones."
            - "Subrogante legal del Gobernador/a."
        - Cpt: "Jefes/as de División"
          ID: GORE-ROL-JEFE-DIVISION-01
          Resp: "Liderar divisiones especializadas (DAF, DIPLADE, DIPIR, Fomento, Infraestructura, DIDESOH, Prevención Delito)."
      Desafio_Comun: "Equilibrar demandas técnicas y políticas, presiones externas y recursos limitados, visión de largo plazo y urgencias."

    Triangulo_Estrategico_Moore:
      ID: GORE-DIRECTIVO-TRIANGULO-MOORE-01
      Purp: "Aplicar el triángulo de Moore a la gestión regional."
      Dimensiones:
        - ID: GORE-TRIANGULO-VALOR-PUBLICO-01
          Cpt: "Creación de valor público regional"
          Ctx: "Qué valor significativo se genera para habitantes; cómo contribuyen acciones al desarrollo."
        - ID: GORE-TRIANGULO-VIABILIDAD-POLITICA-01
          Cpt: "Viabilidad política y legal"
          Ctx: "Apoyo político, legitimidad y respaldo normativo; coordinación con CORE, nivel central y municipios."
        - ID: GORE-TRIANGULO-CAPACIDAD-OPERATIVA-01
          Cpt: "Capacidad operativa y administrativa"
          Ctx: "Estructura, procesos, recursos y sistemas para implementar eficazmente."
      Res: "El directivo GORE exitoso alinea simultáneamente las tres dimensiones."

    BATNA_en_Negociacion_Regional:
      ID: GORE-TRIANGULO-BATNA-01
      Purp: "Usar la Mejor Alternativa a un Acuerdo (BATNA) como herramienta de poder en negociaciones con nivel central y otros actores."

    Competencias_Clave_Directivos_GORE:
      ID: GORE-DIRECTIVO-COMPETENCIAS-01
      Competencias:
        - "Visión estratégica territorial."
        - "Gestión de proyectos y programas regionales."
        - "Liderazgo externo y articulación de redes."
        - "Manejo de crisis regionales."
        - "Liderazgo interno y gestión de personas."
        - "Innovación y flexibilidad."
        - "Conocimientos normativos y experiencia en gestión pública regional."

    Intraemprendimiento_Publico:
      ID: GORE-DIRECTIVO-INTRAEMPRENDIMIENTO-01
      Cpt: "Intraemprendedor del Estado como agente de cambio que impulsa ideas, desafía statu quo y moderniza la gestión."
      Purp:
        - "Modernizar procesos y tecnologías."
        - "Responder a nuevos desafíos (cambio climático, reconversión productiva)."
        - "Aprovechar nuevas competencias transferidas."
        - "Fomentar cultura de mejora continua."

Parte_II_Modernizacion_y_Herramientas_Gestion_GORE:
  ID: GORE-MODERNIZACION-01
  Titulo: "Parte II: Modernización y Herramientas para la Gestión Estratégica y Operativa del GORE"
  Purp: "Traducir fundamentos y diagnósticos en una hoja de ruta de modernización, fortalecimiento institucional y mejora continua."

  Hoja_Ruta_Modernizacion:
    ID: GORE-MODERNIZACION-HOJA-RUTA-01
    Purp: "Adaptar un 'mapa rutero' de transformación institucional al contexto GORE."
    Etapas:
      Preparacion_Previa:
        ID: GORE-HOJA-RUTA-ETAPA-A-01
        Purp: "Cimentar liderazgo, diagnóstico y diseño estratégico antes de cambios profundos."
        Componentes:
          - "Liderazgo y equipo directivo consolidado."
          - "Diagnóstico institucional y territorial profundo."
          - "(Re)definición ERD y PROT sobre base del diagnóstico."
          - "Diseño de arquitectura organizacional y tecnológica."
      Carretera_Operacional:
        ID: GORE-HOJA-RUTA-ETAPA-B-01
        Purp: "Asegurar capacidades operacionales básicas (UCI, DAF, DIPIR, DIPLADE, jurídica, innovación, PMO)."
      Ruta_Excelencia:
        ID: GORE-HOJA-RUTA-ETAPA-C-01
        Purp: "Implementar cambios estratégicos: proyectos, programas, nuevas competencias, transformación digital, gestión de personas, participación."
      Liderazgo_y_Gestion_Cambio:
        ID: GORE-HOJA-RUTA-ETAPA-D-01
        Purp: "Acompañar la modernización técnica con un proyecto robusto de gestión del cambio."

  Diagnostico_Institucional:
    ID: GORE-MODERNIZACION-DIAGNOSTICO-01
    Purp: "Realizar diagnóstico profundo del GORE y su entorno como base de la modernización."
    Metodologia:
      ID: GORE-DIAGNOSTICO-METODOLOGIA-01
      Proc:
        - "Definir propósito y alcance del diagnóstico."
        - "Organizar trabajo y levantar información secundaria (marco legal, documentos estratégicos, informes, datos de desempeño, información pública)."
        - "Construir modelo de agregación de valor público (canvas público)."
        - "Levantamiento de percepciones (entrevistas y encuestas a actores internos y externos)."
        - "Análisis integrado con herramientas como Ishikawa y árboles de problemas."
        - "Discusión, validación y priorización de hallazgos."
      Pauta_Priorizacion:
        ID: GORE-DIAGNOSTICO-PRIORIZACION-01
        Purp: "Evaluar problemas/iniciativas con criterios cuantificados (urgencia, tamaño, costo-beneficio, etc.)."

  Modelo_Agregacion_Valor_Publico:
    ID: GORE-DIAGNOSTICO-MODELO-VALOR-01
    Purp: "Mapear cómo el GORE crea, entrega y captura valor público en la práctica actual."
    Componentes:
      - "Propuesta de valor público."
      - "Segmentos de ciudadanos/usuarios/clientes."
      - "Relaciones con usuarios y canales de entrega."
      - "Actividades clave (planificación, inversión, programas, coordinación, fomento)."
      - "Recursos clave (capital humano, financiero, sistemas, legitimidad, redes)."
      - "Alianzas clave (nivel central, municipios, CORE, CGR, universidades, sector privado, OSC)."
      - "Estructura de costos y fuentes de financiamiento (FNDR, FRIL, FRPD, ISAR, ingresos propios, fondos especiales)."

  Gestion_Estrategica_GORE:
    ID: GORE-MODERNIZACION-ESTRATEGIA-01
    Purp: "Orientar la toma de decisiones y asignación de recursos para crear valor público."
    Ref:
      - GORE-VALOR-PUBLICO-REGIONAL-01
      - GORE-INSTRUMENTO-ERD-01
      - GORE-INSTRUMENTO-PROT-01
    ERD_como_Instrumento_Rector:
      ID: GORE-ESTRATEGIA-ERD-01
      Purp: "Definir visión compartida, ejes, objetivos y líneas de acción de largo plazo."
      Req:
        - "Liderazgo del Gobernador/a y DIPLADE."
        - "Participación ciudadana y de actores clave."
        - "Fundamento en diagnóstico riguroso."
        - "Aprobación por CORE y actualización periódica."
    Definiciones_Estrategicas_Clave:
      ID: GORE-ESTRATEGIA-DEFINICIONES-01
      Cpt:
        - "Segmentación y priorización de ciudadanos y usuarios regionales."
        - "Cartera de servicios y productos GORE alineada con ERD."
        - "Canales de entrega y participación, con énfasis en transformación digital."
        - "Propuesta de valor público regional clara y coherente."
        - "Recursos y procesos críticos para cumplir la propuesta de valor."
    Formulacion_y_Alineamiento:
      ID: GORE-ESTRATEGIA-FORMULACION-01
      Proc:
        - "Formulación estratégica con participación y evidencia."
        - "Alineamiento multinivel con políticas nacionales y planes comunales."
        - "Implementación y seguimiento mediante POA, presupuesto y sistemas de monitoreo."

  Arquitectura_Organizacional_GORE:
    ID: GORE-MODERNIZACION-ARQUITECTURA-01
    Purp: "Diseñar o ajustar arquitectura organizacional para implementar la estrategia."
    Estructura_Formal:
      ID: GORE-ARQUITECTURA-ESTRUCTURA-FORMAL-01
      Src: "Ley 19.175 y Ley 21.074."
      Ref:
        - GORE-GLOS-DAF
        - GORE-GLOS-DIPLADE
        - GORE-GLOS-DIPIR
        - GORE-GLOS-DIDESOH
        - GORE-GLOS-UCI
      Componentes:
        - "Autoridades electas: Gobernador/a Regional, CORE."
        - "Gestión administrativa: Administrador/a Regional, UCI, divisiones mínimas (DAF, DIPLADE, DIPIR, Fomento, Infraestructura, DIDESOH, Prevención Delito)."
        - "Departamento Área Metropolitana si aplica."
      Warn: "Evitar insularidad y silos divisionales."
    Coordinacion_Interna_y_Externa:
      ID: GORE-ARQUITECTURA-COORDINACION-01
      Cpt:
        - "Coordinación interdivisional (equipos directivos, comités, sistemas compartidos, RACI)."
        - "Coordinación con órganos auxiliares (COSOC, comités de alcaldes, CCTID, corporaciones regionales)."
        - "Mecanismos de coordinación externa con DPR, SEREMIs, municipios, nivel central, asociatividad territorial."
      Ref:
        - GORE-GLOS-COSOC
        - GORE-GLOS-CCTID
        - GORE-GLOS-DPR
        - GORE-GLOS-SEREMI
    RACI_Procesos_Claves:
      ID: GORE-ARQUITECTURA-RACI-01
      Purp: "Clarificar responsabilidades en procesos transversales mediante matriz RACI."

  Sistemas_Control_Gestion_y_Desempeno:
    ID: GORE-MODERNIZACION-CONTROL-GESTION-01
    Purp: "Implementar un Sistema de Control de Gestión (SCG) que conecte estrategia, presupuesto y resultados."
    Ref:
      - GORE-MODERNIZACION-ESTRATEGIA-01
      - GORE-CONTROL-GESTION-INDICADORES-01
    Vinculacion_Estrategia_Presupuesto:
      ID: GORE-CONTROL-GESTION-VINCULACION-01
      Cpt:
        - "ERD como punto de partida."
        - "POA que desagregan ERD en metas divisionales."
        - "Presupuesto regional alineado con ERD y POA."
        - "SCG que cierra ciclo planificación-ejecución-evaluación-retroalimentación."
    Indicadores_Desempeno:
      ID: GORE-CONTROL-GESTION-INDICADORES-01
      Purp: "Medir lo sustantivo para la misión del GORE con indicadores SMART."
      Tipologia:
        - "Eficacia."
        - "Eficiencia (incluyendo throughput de procesos clave)."
        - "Calidad (satisfacción y tiempos de respuesta)."
        - "Impacto (outcomes en empleo, brechas sociales, competitividad, cohesión)."
    Integracion_Sistemas_Nacionales:
      ID: GORE-CONTROL-GESTION-SISTEMAS-NACIONALES-01
      Ref:
        - GORE-GLOS-SNI
        - GORE-GLOS-RF
        - GORE-GLOS-SIGFE
      Cpt:
        - "SNI para inversiones de capital (registro BIP, RS)."
        - "Sistema de evaluación y monitoreo de programas públicos (RF)."
        - "SIGFE para ejecución presupuestaria."
        - "Hacia presupuesto por resultados y convenios de desempeño para directivos y unidades."

  Gestion_Personas_en_GORE:
    ID: GORE-MODERNIZACION-PERSONAS-01
    Purp: "Instalar gestión de personas moderna y estratégica como pilar de la modernización."
    Desafios_GRH:
      ID: GORE-PERSONAS-DESAFIOS-01
      Cpt:
        - "Marco normativo complejo."
        - "Diversos tipos de contratación (planta, contrata, honorarios)."
        - "Atracción y retención de talento en regiones."
        - "Cultura burocrática y aversión al riesgo."
    Procesos_Clave_GRH:
      ID: GORE-PERSONAS-PROCESOS-CLAVE-01
      Proc:
        - "Reclutamiento y selección por mérito."
        - "Inducción estructurada para nuevos funcionarios y autoridades."
        - "Sistema de calificaciones significativo."
        - "Capacitación y desarrollo de competencias (incluyendo oferta Academia SUBDERE)."
        - "Desarrollo de carrera funcionaria transparente."
    Motivacion_y_Clima:
      ID: GORE-PERSONAS-MOTIVACION-01
      Purp: "Aumentar motivación intrínseca mediante reconocimiento, desarrollo, buen clima, autonomía y sentido de impacto público."

  Gestion_Riesgos_en_GORE:
    ID: GORE-MODERNIZACION-RIESGOS-01
    Purp: "Gestionar riesgos de manera proactiva para minimizar impactos y aprovechar oportunidades."
    Ref:
      - GORE-GLOS-UCI
      - GORE-GLOS-SINAPRED
    Identificacion_y_Matriz:
      ID: GORE-RIESGOS-IDENTIFICACION-01
      Cpt: "Mapeo de riesgos políticos, financieros, operacionales, de probidad y reputacionales."
      Herramientas:
        - "Mapa de stakeholders clave y sus intereses/poder."
        - "Matriz de riesgos (probabilidad x impacto, controles, tratamientos, responsables, plazos, monitoreo)."
    Rol_UCI:
      ID: GORE-RIESGOS-UCI-01
      Cpt: "Unidad de Control Interno como asesor metodológico, monitor de controles y promotor de cultura de gestión de riesgos."

  Transformacion_Digital_y_Datos:
    ID: GORE-MODERNIZACION-DIGITAL-01
    Purp: "Abordar pilares legislativos y de gestión para modernización tecnológica y protección de datos."
    Ley_21180_Transformacion_Digital:
      ID: GORE-DIGITAL-LEY-21180-01
      Ejes:
        - "Digitalización de procedimientos administrativos ('cero papel')."
        - "Firma electrónica y gestión documental electrónica."
        - "Interoperabilidad y no repetir información al ciudadano."
        - "Ciberseguridad y protección de infraestructura y datos."
    Ley_21719_Proteccion_Datos:
      ID: GORE-DIGITAL-LEY-21719-01
      Ejes:
        - "Aplicación de principios de protección de datos."
        - "Coordinación con Agencia de Protección de Datos."
        - "Designación y rol del Delegado de Protección de Datos."
        - "Gestión de bases de datos personales (inventario, EIPD, seguridad desde el diseño)."

  Gestion_Procesos_Clave:
    ID: GORE-MODERNIZACION-PROCESOS-01
    Purp: "Optimizar procesos críticos para eficiencia, transparencia y calidad."
    Identificacion_y_Rediseno:
      ID: GORE-PROCESOS-IDENTIFICACION-01
      Cpt: "Procesos críticos: ciclo proyectos FNDR, FRIL, subvenciones 8%, transferencia y asunción de competencias, atención ciudadana y participación."
      Proc: "Mapeo de flujos, métricas, problemas y rediseño (incluyendo automatización y simplificación)."
    Tecnologia_como_Habilitador:
      ID: GORE-PROCESOS-TECNOLOGIA-01
      Warn: "No 'ponerle tecnología' a procesos defectuosos; primero rediseñar, luego automatizar."
    Mejora_Continua_y_Escalabilidad:
      ID: GORE-PROCESOS-MEJORA-CONTINUA-01
      Mech:
        - "Monitoreo con indicadores y dueños de proceso."
        - "Revisiones periódicas y feedback de usuarios."
        - "Diseño de procesos escalables y replicables en territorios."

  Innovacion_Publica_Regional:
    ID: GORE-MODERNIZACION-INNOVACION-01
    Purp: "Fomentar búsqueda de soluciones innovadoras para problemas y oportunidades regionales."
    Ref:
      - GORE-INNOVACION-OMVP-01
      - GORE-INNOVACION-FRPD-01
      - GORE-GLOS-FRPD
    Ecosistema_Innovacion:
      ID: GORE-INNOVACION-ECOSISTEMA-01
      Componentes:
        - "Liderazgo comprometido con experimentación."
        - "Identificación estratégica de desafíos."
        - "Gestión participativa de ideas (embudo de innovación)."
        - "Prototipos, pilotos y tolerancia al fracaso."
        - "Recursos dedicados a innovación."
    OMVP:
      ID: GORE-INNOVACION-OMVP-01
      Def: "Oferta Mínima Viable Pública: versión más simple y de menor costo de un programa/servicio para validar hipótesis con beneficiarios reales."
    FRPD_como_Instrumento:
      ID: GORE-INNOVACION-FRPD-01
      Cpt: "FRPD como instrumento clave para fomento productivo, I+D+i y desarrollo regional, alineado con ERD y Política Regional CTCI."

  Gestion_Proyectos_y_Programas:
    ID: GORE-MODERNIZACION-PROYECTOS-01
    Purp: "Gestionar eficazmente cartera de proyectos y programas de desarrollo regional."
    Gestion_por_Fondos:
      ID: GORE-PROYECTOS-FONDOS-01
      Cpt:
        - "FNDR: fondo principal, ciclo SNI completo."
        - "FRIL: infraestructura menor escala municipal, lógica SNI simplificada."
        - "FRPD: productividad e innovación, concursos y transferencias."
        - "Programas Subt. 24: gasto corriente, Marco Lógico y evaluación Glosa 06."
      Ref:
        - GORE-GLOS-FNDR
        - GORE-GLOS-FRIL
        - GORE-GLOS-FRPD
        - GORE-GLOS-SNI
        - GORE-GLOS-IPR
    Oficina_Gestion_Proyectos_PMO:
      ID: GORE-MODERNIZACION-PROYECTOS-PMO-01
      Purp: "Centralizar y profesionalizar gestión de cartera de proyectos y programas."
      Ref:
        - GORE-GLOS-PMO
        - GORE-GLOS-MML
        - GORE-GLOS-SNI
      Funciones:
        - "Gestión de cartera y catastro consolidado."
        - "Apoyo metodológico y capacitación (SNI, MML)."
        - "Monitoreo y alerta temprana."
        - "Coordinación, estandarización y gestión del conocimiento."
    Convenios_Programacion:
      ID: GORE-PROYECTOS-CONVENIOS-PROGRAMACION-01
      Purp: "Abordar inversiones estratégicas de gran escala y largo plazo entre GORE y ministerios."

  Gobernanza_Colaborativa_y_Probidad:
    ID: GORE-MODERNIZACION-COORDINACION-01
    Purp: "Construir gobernanza colaborativa, gestionar expectativas ciudadanas y resguardar probidad y transparencia."
    Ref:
      - GORE-MODERNIZACION-RIESGOS-01
      - GORE-MODERNIZACION-CONTROL-GESTION-01
      - GORE-MODERNIZACION-PROYECTOS-01
    Coordinacion_Interinstitucional:
      ID: GORE-COORDINACION-ESTRATEGIAS-01
      Cpt:
        - "Coordinación con nivel central (DPR, SEREMIs, ministerios, DIPRES, SUBDERE)."
        - "Relación estratégica con municipios y asociaciones de municipios."
        - "Asociatividad interregional y transfronteriza."
    Seguridad_Publica_Regional_y_Adopcion:
      ID: GORE-COORDINACION-SEGURIDAD-01
      Purp:
        - "Definir rol del GORE en prevención del delito y gestión de emergencias."
        - "Guiar la gestión de adopción de programas por parte de comunidad y actores."
      Herramientas_Adopcion:
        ID: GORE-COORDINACION-ADOPCION-01
        Purp: "Identificar y superar barreras de adopción de iniciativas públicas."
    Gestion_Expectativas_Ciudadanas:
      ID: GORE-ENTREGA-VALOR-EXPECTATIVAS-01
      Cpt: "Calidad percibida como diferencia entre rendimiento real y expectativas previas; prometer realista y entregar por sobre lo prometido."
    Probidad_y_Transparencia:
      ID: GORE-MODERNIZACION-PROBIDAD-01
      Purp: "Asegurar probidad, transparencia y prevención de corrupción en el GORE."
      Ref:
        - GORE-RIESGOS-IDENTIFICACION-01
        - GORE-RIESGOS-UCI-01
      Leyes_Claves:
        ID: GORE-PROBIDAD-LEYES-01
        Cpt:
          - "Ley 20.880 (Declaración de Intereses y Patrimonio, deberes de abstención)."
          - "Ley 20.285 (Transparencia activa y pasiva; rol CPLT)."
      Riesgos_y_Estrategias_Preventivas:
        ID: GORE-PROBIDAD-RIESGOS-01
        Ctx: "Licitaciones, transferencias, subvenciones, contratación de personal, ordenamiento territorial, convenios."
        Act:
          - "Fortalecer UCI."
          - "Transparencia proactiva."
          - "Estandarización y digitalización de procesos."
          - "Comités de evaluación plurales."
          - "Rotación en áreas sensibles."
          - "Canales de denuncia seguros."
          - "Capacitación en probidad y fomento de control social."
      Rol_UCI_y_CGR:
        ID: GORE-PROBIDAD-CONTROL-01
        Cpt: "UCI como contraparte técnica de CGR, con rol preventivo y fiscalizador; CGR como órgano de control preventivo y posterior, con dictámenes vinculantes."

  Sintesis_y_Desafios:
    ID: GORE-CONCLUSIONES-SINTESIS-01
    Purp: "Resumir principios y herramientas esenciales y explicitar desafíos persistentes y futuros."
    Principios_Esenciales:
      ID: GORE-SINTESIS-PRINCIPIOS-01
      Ref:
        - GORE-VALOR-PUBLICO-REGIONAL-01
        - GORE-MODERNIZACION-ESTRATEGIA-01
        - GORE-MODERNIZACION-ARQUITECTURA-01
        - GORE-MODERNIZACION-CONTROL-GESTION-01
        - GORE-MODERNIZACION-PROYECTOS-01
        - GORE-MODERNIZACION-PERSONAS-01
        - GORE-MODERNIZACION-RIESGOS-01
        - GORE-MODERNIZACION-DIGITAL-01
        - GORE-MODERNIZACION-PROCESOS-01
        - GORE-MODERNIZACION-INNOVACION-01
        - GORE-MODERNIZACION-PROYECTOS-PMO-01
        - GORE-MODERNIZACION-PROBIDAD-01
        - GORE-MODERNIZACION-COORDINACION-01
      Lista:
        - "Principios que condensan la guía: valor público, estrategia, capacidades, control, innovación y probidad."
        - "Sirven como checklist ejecutivo para orientar decisiones del Gobernador y equipo directivo."
    Desafios_Persistentes:
      ID: GORE-SINTESIS-DESAFIOS-01
      Ref:
        - GORE-ENTORNO-PRINCIPIOS-FISCALES-01
        - GORE-MODERNIZACION-RIESGOS-01
        - GORE-MODERNIZACION-PERSONAS-01
        - GORE-MODERNIZACION-PROYECTOS-01
        - GORE-MODERNIZACION-DIGITAL-01
        - GORE-MODERNIZACION-COORDINACION-01
      Lista:
        - "Desafíos estructurales pendientes en financiamiento, capacidades, coordinación y equidad territorial."
        - "Requieren reformas graduales, fortalecimiento institucional y acuerdos políticos de largo plazo."

Modelos_Mentales_y_Sistemas_para_Gestion_Regional:
  ID: GORE-MODELOS-MENTALES-SISTEMAS-01
  Purp: "Proveer modelos mentales financiero-estratégicos, psicológicos y de pensamiento sistémico para mejorar decisión, acción y resiliencia institucional."
  Ref:
    - GORE-FUNDAMENTOS-MOTOR-VALOR-01
    - GORE-ENTORNO-WICKED-PROBLEMS-01
    - GORE-MODERNIZACION-CONTROL-GESTION-01
    - GORE-MODERNIZACION-PROYECTOS-01

  Modelos_Financiero_Estrategicos:
    ID: GORE-MODERNIZACION-MODELOS-FINANCIEROS-01
    Purp: "Adaptar modelos de finanzas y estrategia privada a la lógica de valor público y sostenibilidad presupuestaria."
    Ref:
      - GORE-PROYECTOS-FONDOS-01
      - GORE-CONTROL-GESTION-SISTEMAS-NACIONALES-01
    Conceptos:
      - ID: GORE-MODELOS-FIN-SOSTENIBILIDAD-01
        Cpt: "Sostenibilidad presupuestaria como fin del GORE (no maximización de ganancias)."
      - ID: GORE-MODELOS-FIN-POTENCIAR-IMPACTO-01
        Cpt: "Cuatro vías para potenciar impacto regional: más beneficiarios, mayor valor por intervención, mayor frecuencia, mejor eficiencia."
      - ID: GORE-MODELOS-FIN-VLT-01
        Cpt: "Valor a Largo Plazo del Territorio/Ciudadano (VLT)."
      - ID: GORE-MODELOS-FIN-CIP-01
        Cpt: "Costo de Involucramiento Permitido (CIP) proporcional al VLT esperado."
      - ID: GORE-MODELOS-FIN-COSTE-HUNDIDO-01
        Cpt: "Falacia del coste hundido y necesidad de decidir por costos/beneficios futuros."
      - ID: GORE-MODELOS-FIN-COSTE-OPORTUNIDAD-01
        Cpt: "Costo de oportunidad en decisión de inversión pública."
      - ID: GORE-MODELOS-FIN-VALOR-TEMPORAL-01
        Cpt: "Valor temporal de recursos públicos y relevancia de la tasa social de descuento."
      - ID: GORE-MODELOS-FIN-APALANCAMIENTO-01
        Cpt: "Apalancamiento regional mediante cofinanciamiento y convenios de programación."
      - ID: GORE-MODELOS-FIN-DEGRADACION-INCREMENTAL-01
        Cpt: "Degradación incremental del valor público por recortes sucesivos."
      - ID: GORE-MODELOS-FIN-ENDEUDAMIENTO-01
        Cpt: "Endeudamiento subnacional responsable y disciplina fiscal."

  Modelos_Mentales_Decision_Accion:
    ID: GORE-MODELOS-MENTALES-DECISION-ACCION-01
    Purp:
      - "Equipar al directivo público con modelos mentales sobre funcionamiento de la mente humana."
      - "Mejorar calidad de decisiones y evitar errores de juicio."
    Bloques:
      - ID: GORE-MODELOS-MENTALES-CEREBRO-FISICO-01
        Cpt: "El rendimiento mental depende del estado fisiológico del cuerpo; cuidado personal como requisito de desempeño sostenido."
      - ID: GORE-MODELOS-MENTALES-CONDUCTA-01
        Cpt: "Modelo operativo de la conducta basado en control de percepciones, ahorro de energía, estructura guía y comprensión del conflicto."
      - ID: GORE-MODELOS-MENTALES-SESGOS-01
        Cpt: "Conjunto de sesgos cognitivos relevantes (aversión a la pérdida, ceguera a la carencia, percepción por contraste, escasez, novedad) y sus implicancias para GORE."

  Metodologias_Eficacia_Personal:
    ID: GORE-METODOLOGIAS-EFICACIA-01
    Purp: "Proveer técnicas para gestionar energía, foco y carga de trabajo de directivos públicos."
    Bloques:
      - ID: GORE-EFICACIA-FOCO-ENERGIA-01
        Cpt: "Estado de flujo, penalización por cambio cognitivo, ciclos de energía."
      - ID: GORE-EFICACIA-TAREAS-OBJETIVOS-01
        Cpt: "Cuatro métodos para afrontar tareas, Tareas Más Importantes (TMI) y 'siguiente acción'."
      - ID: GORE-EFICACIA-MARCOS-MENTALES-01
        Cpt: "Ámbito de control, mentalidad de crecimiento, exteriorización y simulación contrafactual."

  Principios_Interaccion_y_Liderazgo_Equipos:
    ID: GORE-PRINCIPIOS-INTERACCION-LIDERAZGO-01
    Purp: "Entregar un 'manual' de principios para liderar personas y equipos en contexto regional."
    Bloques:
      - ID: GORE-INTERACCION-PODER-INFLUENCIA-01
        Cpt: "Poder, influencia y reputación; liderazgo basado en influencia más que coacción."
      - ID: GORE-INTERACCION-COLABORACION-01
        Cpt: "Ventaja comparativa, tamaño óptimo de equipos, 'objetivo del comandante', apatía del testigo."
      - ID: GORE-INTERACCION-FUNDAMENTOS-HUMANOS-01
        Cpt: "Necesidades humanas de sentirse valorado y seguro, poder del 'porque', prueba social y autoridad, compromiso y coherencia."
      - ID: GORE-INTERACCION-ERRORES-LIDERAZGO-01
        Cpt: "Errores comunes: error fundamental de atribución, efecto Pigmalión, foco en alternativas vs problemas."

  Pensamiento_Sistemico_y_Analisis_Sistemas:
    ID: GORE-MODELOS-MENTALES-SISTEMAS-BASE-01
    Purp: "Aplicar principios de pensamiento sistémico a gestión regional y del GORE."
    Ref:
      - GORE-ENTORNO-WICKED-PROBLEMS-01
      - GORE-MODERNIZACION-RIESGOS-01
    Bloques:
      - ID: GORE-SISTEMAS-LEY-GALL-01
        Cpt: "Ley de Gall: evolucionar sistemas desde versiones simples; evitar megaproyectos 'Big Bang'."
      - ID: GORE-SISTEMAS-FLUJO-STOCK-SLACK-01
        Cpt: "Flujos, existencias y holgura organizacional; equilibrio entre eficiencia y resiliencia."
      - ID: GORE-SISTEMAS-RESTRICCIONES-01
        Cpt: "Teoría de las restricciones: desempeño limitado por cuello de botella principal."
      - ID: GORE-SISTEMAS-FEEDBACK-LOOP-01
        Cpt: "Bucles de feedback y efectos de segundo orden en políticas públicas."
      - ID: GORE-SISTEMAS-ENTORNO-INCERTIDUMBRE-01
        Cpt: "Entorno, controles de selección e incertidumbre (cisnes negros); construir resiliencia en vez de predecir futuro."
      - ID: GORE-SISTEMAS-INTERDEPENDENCIA-01
        Cpt: "Interdependencia y vinculación de sistemas (estrechamente vs débilmente vinculados)."
      - ID: GORE-SISTEMAS-EFECTOS-SECUNDARIOS-01
        Cpt: "Efectos secundarios y consecuencias inesperadas; usar pilotos y monitoreo."

  Herramientas_Analisis_y_Mejora_Sistemas:
    ID: GORE-ANALISIS-SISTEMOS-01
    Purp: "Aplicar herramientas de análisis y mejora de sistemas regionales y organizacionales."
    Ref:
      - GORE-CONTROL-GESTION-INDICADORES-01
      - GORE-MODERNIZACION-PROCESOS-01
    Analisis_Sistemas:
      Bloques:
        - ID: GORE-ANALISIS-DECONSTRUCCION-01
          Cpt: "Deconstrucción de procesos en subsistemas con desencadenantes, flujos, condicionantes y puntos finales."
        - ID: GORE-ANALISIS-MEDICION-KPI-01
          Cpt: "Definición de KPIs estratégicos derivados de los 5 procesos fundamentales del GORE."
        - ID: GORE-ANALISIS-CALIDAD-DATOS-01
          Cpt: "Principio GIGO y honestidad en datos; rol de UCI."
        - ID: GORE-ANALISIS-HERRAMIENTAS-01
          Cpt: "Contexto, muestreo, ratios, correlación vs causalidad, benchmarks, proxies, segmentación y humanización de datos."
    Mejora_y_Resiliencia:
      ID: GORE-MEJORA-SISTEMAS-01
      Bloques:
        - ID: GORE-MEJORA-OPTIMIZACION-REFACTORIZACION-01
          Cpt: "Optimización y refactorización de procesos públicos."
        - ID: GORE-MEJORA-MINORIA-CRUCIAL-01
          Cpt: "Minoría crucial (regla 80-20) aplicada a cartera de proyectos, problemas y ejecución."
        - ID: GORE-MEJORA-FRICCION-AUTOMATIZACION-01
          Cpt: "Fricción y automatización en gestión pública; paradoja de automatización."
        - ID: GORE-MEJORA-POS-CHECKLIST-01
          Cpt: "Procedimientos operativos estándar y checklists para reducir errores."
        - ID: GORE-MEJORA-RESILIENCIA-01
          Cpt: "Resiliencia institucional (pensar como tortuga, no como tigre); evitar optimización cortoplacista a costa de resiliencia."

  Modelo_Innovacion_Adaptativa:
    ID: GORE-MODELO-INNOVACION-ADAPTATIVA-01
    Purp: "Integrar agilidad e innovación abierta en un modelo adaptativo para la gestión regional."
    Componentes:
      - ID: GORE-INNOVACION-FUND-AGIL-01
        Cpt: "Innovación ágil: desarrollo iterativo, equipos transfuncionales, planificación adaptativa, centralidad en ciudadano y mejora continua."
      - ID: GORE-INNOVACION-FUND-ABIERTA-01
        Cpt: "Innovación abierta: flujos de conocimiento outside-in e inside-out, inteligencia colectiva."
      - ID: GORE-INNOVACION-ACTORES-QUADHELIX-01
        Cpt: "Modelo de Cuádruple Hélice: gobierno, academia, industria y sociedad civil como actores clave."
      - ID: GORE-INNOVACION-CICLO-ADAPTIVO-01
        Cpt: "Ciclo de innovación adaptativa de cinco fases: definir áreas de foco, gestionar ideas, desarrollar conceptos, implementar pilotos/OMVP, evaluar y escalar."
