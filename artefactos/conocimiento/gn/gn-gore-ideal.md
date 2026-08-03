---
urn: urn:gn:kb:gn-gore-ideal
nombre: gn-gore-ideal
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre KODA/Spec Artifact for GORE Ñuble Ideal / GORE 4.0; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/01_fundamentos/intro/kb_gn_900_gore_ideal_koda.yml (sha256:0d088a195da79bde9daaf1d082054a5f70fde8bebb5d7e69c16b7f7b735cd002); URN KODA legado urn:gorenuble:gn:gore-ideal:1.0.0; estado original published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-27
lang: es
tags: ["gn", "gore-os", "koda", "domains", "01-fundamentos", "intro", "gore", "ideal"]
familia: bok
---
# KODA/Spec Artifact for GORE Ñuble Ideal / GORE 4.0
# Derived from kb_gn_900_gore_ideal.md

_manifest:
  urn: "urn:gorenuble:gn:gore-ideal:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_900_gore_ideal_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:intro-gores-nuble:1.0.0"
        reason: "Contexto institucional GORE Ñuble"
      - urn: "urn:gorenuble:kb:estructura-estado-chile:1.0.0"
        reason: "Marco general del Estado de Chile"
  provenance:
    created_by: "FS"
    created_at: "2025-11-27"
    last_modified_at: "2025-11-27"
    model_collaborators: ["Cascade", "KODA-TRANSFORMER"]

ID: GN-GORE-IDEAL-ARTIFACT-01
Version: 1.0.0
Status: published
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: Cascade
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-11-27
Modification-Date: 2025-11-27
Ctx: "Ensayo analítico sobre anatomía, límites y potencial del Gobierno Regional como base para la visión de un GORE ideal/GORE 4.0."
Source:
  Ctx_Required:
    - "staging/gn/kb_gn_900_gore_ideal.md"
    - "DFL N° 1-19.175 (LOC GORE)"
  Ctx_Optional:
    - "knowledge/domains/gn/kb_gn_000_intro_gores_nuble_koda.yml"
  Primary-Source: "kb_gn_900_gore_ideal.md"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-GORE-IDEAL-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_Conceptos_Clave:
  ID: GN-GORE-IDEAL-GLOSARIO-01
  Purp: "Definir conceptos estructurales recurrentes del Gobierno Regional y del modelo GORE 4.0."
  Terminos:
    - ID: GN-GORE-IDEAL-GLOS-GORE
      Cpt: "Gobierno Regional (GORE)"
      Def: "Institución descentralizada con personalidad jurídica de derecho público y patrimonio propio, encargada de la administración superior de la región y del desarrollo social, cultural y económico del territorio."
      Src: "Ley N° 19.175, Art. 13."
    - ID: GN-GORE-IDEAL-GLOS-GOBERNADOR
      Cpt: "Gobernador Regional"
      Def: "Máxima autoridad ejecutiva del GORE, elegida por sufragio universal directo, responsable de conducir políticamente el gobierno regional."
      Src: "Ley N° 19.175, Art. 23."
    - ID: GN-GORE-IDEAL-GLOS-CORE
      Cpt: "Consejo Regional (CORE)"
      Def: "Órgano colegiado del GORE que representa territorialmente a la comunidad regional y ejerce funciones normativas, resolutivas y fiscalizadoras."
      Src: "Ley N° 19.175, Art. 28."
    - ID: GN-GORE-IDEAL-GLOS-DPR
      Cpt: "Delegado Presidencial Regional (DPR)"
      Def: "Representante natural e inmediato del Presidente en la región, a cargo del gobierno interior y de la coordinación de servicios públicos nacionales."
    - ID: GN-GORE-IDEAL-GLOS-ERD
      Cpt: "Estrategia Regional de Desarrollo (ERD)"
      Def: "Instrumento de planificación de largo plazo que define visión, ejes y objetivos estratégicos para el desarrollo regional."
      Src: "Ley N° 19.175, Art. 16."
    - ID: GN-GORE-IDEAL-GLOS-PROT
      Cpt: "Plan Regional de Ordenamiento Territorial (PROT)"
      Def: "Instrumento vinculante que orienta el uso del territorio regional y la localización de inversiones."
      Src: "Ley N° 19.175, Art. 17."
    - ID: GN-GORE-IDEAL-GLOS-FONDO-FNDR
      Cpt: "Fondo Nacional de Desarrollo Regional (FNDR)"
      Def: "Principal fondo de inversión regional, destinado a financiar proyectos y programas priorizados por el GORE."
      Src: "Ley N° 19.175, Art. 74."
    - ID: GN-GORE-IDEAL-GLOS-FONDO-FRPD
      Cpt: "Fondo Regional para la Productividad y el Desarrollo (FRPD)"
      Def: "Fondo financiado por el Royalty Minero para apoyar iniciativas de innovación, competitividad y fomento productivo."
    - ID: GN-GORE-IDEAL-GLOS-FONDO-ISAR
      Cpt: "Inversiones Sectoriales de Asignación Regional (ISAR)"
      Def: "Recursos de ministerios sectoriales cuya destinación territorial final es decidida por el GORE según prioridades regionales."
      Src: "Ley N° 19.175, Art. 80."
    - ID: GN-GORE-IDEAL-GLOS-DIGITAL-TWIN
      Cpt: "Gemelo Digital (Digital Twin) del territorio"
      Def: "Modelo virtual dinámico que integra datos territoriales, sociales, económicos y ambientales de la región para simular escenarios de política pública."
    - ID: GN-GORE-IDEAL-GLOS-GORE-4-0
      Cpt: "GORE 4.0"
      Def: "Modelo ideal de Gobierno Regional que integra tecnologías de la Cuarta Revolución Industrial (IA, IoT, ciencia de datos) con su mandato de desarrollo territorial y gobernanza participativa."

Actores_Clave:
  ID: GN-GORE-IDEAL-ACTORES-01
  Purp: "Identificar actores institucionales clave que intervienen en el ciclo del GORE y en sus límites funcionales."
  Entidades:
    - ID: GN-GORE-IDEAL-ACTOR-MDSF
      Cpt: "Ministerio de Desarrollo Social y Familia (MDSF)"
      Def: "Órgano que emite la Recomendación Satisfactoria (RS) para proyectos de inversión pública registrados en el Sistema Nacional de Inversiones."
    - ID: GN-GORE-IDEAL-ACTOR-DIPRES
      Cpt: "Dirección de Presupuestos (DIPRES)"
      Def: "Órgano responsable de la arquitectura programática y del control macro presupuestario del Estado, incluyendo lineamientos y visación de modificaciones presupuestarias."
    - ID: GN-GORE-IDEAL-ACTOR-CGR
      Cpt: "Contraloría General de la República (CGR)"
      Def: "Órgano superior de control de legalidad de los actos de la Administración del Estado y del examen de cuentas."
    - ID: GN-GORE-IDEAL-ACTOR-CORE
      Cpt: "Consejo Regional (CORE)"
      Ref: GN-GORE-IDEAL-GLOS-CORE
      Rol: "Actor político clave en la aprobación del presupuesto regional y en el control político interno sobre el Gobernador Regional."

Parte_I_Identidad_y_Motor_GORE:
  ID: GN-GORE-IDEAL-PARTE-I-01
  Ref:
    - GN-GORE-IDEAL-GLOS-GORE
    - GN-GORE-IDEAL-GLOS-GOBERNADOR
    - GN-GORE-IDEAL-GLOS-CORE

  Introduccion:
    ID: GN-GORE-IDEAL-INTRO-ANATOMIA-01
    Purp: "Introducir la anatomía conceptual, operativa y potencial del Gobierno Regional."
    Def: "Presenta al GORE como institución autónoma de nivel intermedio, nacida del proceso de descentralización, que opera tensionada entre su legitimidad democrática y un Estado históricamente centralizado."
    Obj:
      - "Ofrecer una comprensión multidimensional del GORE más allá de la mera lectura legal."
      - "Conectar diseño normativo, restricciones operativas y visión de máximo potencial institucional."

  Cinco_Pilares_Identidad_GORE:
    ID: GN-GORE-IDEAL-PILARES-IDENTIDAD-01

    Pilar_1_Definicion_Esencial:
      ID: GN-GORE-IDEAL-PILAR-DEF-ESENCIAL-01
      Ref: GN-GORE-IDEAL-GLOS-GORE
      Def: "El GORE es la administración superior de la región, concebida como territorio con características e intereses propios, que acerca decisiones de desarrollo al lugar donde se producen sus efectos."
      Purp:
        - "Adaptar la acción pública a particularidades locales."
        - "Materializar el principio de descentralización del Estado."

    Pilar_2_Naturaleza_Juridica:
      ID: GN-GORE-IDEAL-PILAR-NATURALEZA-01
      Def: "El GORE es una persona jurídica de derecho público, autónoma patrimonial y de gestión."
      Src:
        - "Ley N° 19.175, Art. 13 y 69."
      Componentes:
        - Cpt: "Personalidad jurídica de derecho público"
          Res: "Puede adquirir derechos, contraer obligaciones, poseer bienes y ser parte en juicios."
        - Cpt: "Autonomía patrimonial"
          Res: "Dispone de patrimonio propio, administra y enajena bienes con acuerdo del CORE, para cumplir sus fines."
        - Cpt: "Autonomía de gestión"
          Res: "Define su organización interna y la administración de sus recursos dentro del marco legal."
        - Cpt: "Descentralización vs. desconcentración"
          Def: "El GORE es un ente descentralizado con autoridades electas, mientras que el Delegado Presidencial Regional es un órgano desconcentrado que representa directamente al nivel central."

    Pilar_3_Mision_Estrategica:
      ID: GN-GORE-IDEAL-PILAR-MISION-01
      Def: "El propósito del GORE es el desarrollo social, cultural y económico integral de la región."
      Caracteristicas:
        - "Foco estratégico de largo plazo, no solo administración cotidiana."
        - "Uso de la planificación como herramienta central (ERD, PROT y otros instrumentos técnicos vinculantes)."
        - "Orientación a armonizar decisiones públicas con una visión de 5–20 años para el territorio."

    Pilar_4_Origen_Poder_Legitimidad:
      ID: GN-GORE-IDEAL-PILAR-LEGITIMIDAD-01
      Def: "El poder político del GORE emana del sufragio universal que elige al Gobernador Regional y a los Consejeros Regionales."
      Src:
        - "Ley N° 19.175, Art. 23 y 29."
      Res:
        - "Otorga una legitimidad democrática única en el nivel intermedio del Estado."
        - "Permite al Gobernador hablar 'en nombre de la región' y defender una agenda propia frente al nivel central."

    Pilar_5_Arquitectura_Dual_Poder:
      ID: GN-GORE-IDEAL-PILAR-ARQUITECTURA-01
      Def: "El diseño interno del GORE equilibra eficiencia decisional y representación democrática mediante un sistema dual de poder."
      Componentes:
        - Cpt: "Gobernador Regional"
          Ref: GN-GORE-IDEAL-GLOS-GOBERNADOR
          Res: "Máxima autoridad ejecutiva, motor de iniciativa política, responsable de proponer políticas, planes y presupuesto."
        - Cpt: "Consejo Regional (CORE)"
          Ref: GN-GORE-IDEAL-GLOS-CORE
          Res: "Órgano colegiado que delibera, aprueba, modifica o rechaza las principales decisiones, y fiscaliza la gestión del Gobernador."
        - Cpt: "Equilibrio Ejecutivo–Colegiado"
          Def: "Ninguna decisión estratégica relevante se toma de forma unilateral; requiere negociación constante entre el órgano ejecutivo regional y el CORE."

    Pilar_6_Rol_Coordinador:
      ID: GN-GORE-IDEAL-PILAR-COORDINACION-01
      Def: "La función coordinadora es el eje distintivo del GORE en un ecosistema con múltiples actores y jerarquías."
      Mech:
        - "Utiliza la planificación (ERD, PROT) para fijar un marco común de acción para el territorio."
        - "Usa el financiamiento (FNDR, FRPD, ISAR) como palanca para alinear servicios públicos y municipios."
        - "Compra coordinación a través de incentivos presupuestarios más que por mando jerárquico."

  Motor_Cinco_Funciones:
    ID: GN-GORE-IDEAL-MOTOR-05-FUNC-01
    Def: "El GORE opera mediante un ciclo integrado de cinco funciones: planificar, financiar, ejecutar, coordinar y normar."
    Ref:
      - GN-GORE-IDEAL-GLOS-GORE
    Funciones:
      - Cpt: "Planificar"
        Def: "Traducir la misión estratégica en instrumentos técnicos y vinculantes como la ERD y el PROT, validados por el CORE."
        Ref:
          - GN-GORE-IDEAL-GLOS-ERD
          - GN-GORE-IDEAL-GLOS-PROT
      - Cpt: "Financiar"
        Def: "Administrar y asignar recursos de fondos como FNDR, FRPD e ISAR de acuerdo con la estrategia regional y con criterios técnicos de elegibilidad."
        Ref:
          - GN-GORE-IDEAL-GLOS-FONDO-FNDR
          - GN-GORE-IDEAL-GLOS-FONDO-FRPD
          - GN-GORE-IDEAL-GLOS-FONDO-ISAR
      - Cpt: "Ejecutar"
        Def: "Implementar programas propios (principalmente 'blandos') y viabilizar proyectos de inversión a través de convenios donde el GORE actúa como unidad financiera y otra entidad como unidad técnica."
      - Cpt: "Coordinar"
        Def: "Alinear servicios sectoriales, municipios y nivel central en torno a la estrategia regional, usando información, convenios y recursos como palancas de coordinación."
      - Cpt: "Normar"
        Def: "Dictar normas generales dentro de su competencia para regular procedimientos e instrumentos regionales, siempre subordinadas a la ley y a decretos supremos, y sujetas a control de legalidad externo."

Parte_II_Limites_y_Restricciones_Modelo:
  ID: GN-GORE-IDEAL-PARTE-II-01

  Introduccion:
    ID: GN-GORE-IDEAL-LIM-INTRO-01
    Def: "La autonomía del GORE está acotada por un entramado de leyes, jerarquías y contrapesos que condicionan significativamente cada una de sus cinco funciones motoras."

  Limites_Funcion_Planificar:
    ID: GN-GORE-IDEAL-LIM-PLAN-01
    Items:
      - Cpt: "Coherencia con políticas nacionales y presupuesto"
        Def: "La planificación regional (ERD, PROT y otros instrumentos) debe ser coherente con las políticas públicas nacionales y con el Presupuesto de la Nación. No puede contradecir lineamientos sectoriales ni planificar más allá de los marcos de financiamiento nacionales."
        Src:
          - "Ley N° 19.175, Art. 20 bis y 16 letra a)."
      - Cpt: "Competencia material y ámbitos excluidos"
        Def: "El GORE solo puede planificar materias para las cuales tiene competencias legales en los Art. 16–19 de la LOC GORE. Ámbitos como relaciones exteriores, defensa nacional, administración de justicia y orden público interno son no descentralizables y permanecen en el nivel central."
      - Cpt: "Coordinación obligatoria con entes sectoriales y municipios"
        Def: "Incluso dentro de sus competencias, la planificación debe realizarse en coordinación con organismos sectoriales y municipalidades, por ejemplo en seguridad pública preventiva y desarrollo territorial. La planificación regional se transforma en un ejercicio de negociación y acuerdo, no de imposición unilateral."
        Src:
          - "Ley N° 19.175, Art. 16 letras i) y c)."
      - Cpt: "Planificación anidada y jerarquía multiescalar"
        Def: "La ERD y otros instrumentos regionales deben articularse con políticas nacionales hacia arriba y con instrumentos comunales hacia abajo, actuando como una capa intermedia en un sistema de planificación anidado."

  Limites_Funcion_Financiar:
    ID: GN-GORE-IDEAL-LIM-FIN-01
    Items:
      - Cpt: "Control técnico externo (MDSF)"
        Ref:
          - GN-GORE-IDEAL-ACTOR-MDSF
        Def: "Ningún proyecto de inversión puede ser financiado con fondos regionales sin contar con informe técnico-económico favorable (Recomendación Satisfactoria, RS) del Ministerio de Desarrollo Social y Familia."
        Src:
          - "Ley N° 19.175, Art. 75."
      - Cpt: "Control presupuestario central (DIPRES)"
        Ref:
          - GN-GORE-IDEAL-ACTOR-DIPRES
        Def: "La Dirección de Presupuestos define la arquitectura de programas, revisa el diseño de programas no sujetos al SNI y visa modificaciones relevantes en la Ley de Presupuestos, limitando la discrecionalidad regional."
      - Cpt: "Control de legalidad (Contraloría General)"
        Ref:
          - GN-GORE-IDEAL-ACTOR-CGR
        Def: "Los actos administrativos que aprueban gastos y transferencias deben someterse a la Toma de Razón de la Contraloría. Si ésta estima que el acto es ilegal, el gasto no puede ejecutarse."
      - Cpt: "Control político interno (CORE y umbral 7.000 UTM)"
        Ref:
          - GN-GORE-IDEAL-ACTOR-CORE
        Def: "El Gobernador propone, pero el CORE aprueba la distribución del presupuesto de inversión. Los proyectos que superan un umbral de 7.000 UTM requieren aprobaciones específicas, reforzando el rol resolutivo del Consejo."
        Src:
          - "Ley N° 19.175, Art. 36 letras d) y e), Art. 78."
      - Cpt: "Topes numéricos a transferencias a corporaciones"
        Def: "Los aportes a corporaciones privadas sin fines de lucro están sujetos a límites porcentuales tanto sobre el presupuesto de inversión como sobre el costo total del proyecto, y se prohíbe que el GORE garantice deudas de estas entidades."
        Src:
          - "Ley N° 19.175, Art. 101."
      - Cpt: "Restricciones por elegibilidad y rendición de cuentas"
        Def: "Fondos como ISAR solo pueden destinarse a iniciativas que cumplan los criterios del ministerio de origen, y la normativa de rendiciones impide nuevas transferencias a entidades con rendiciones pendientes, operando como freno inmediato al financiamiento."

  Limites_Funcion_Ejecutar:
    ID: GN-GORE-IDEAL-LIM-EJECUTAR-01
    Items:
      - Cpt: "Rol predominante como unidad financiera, no técnica"
        Def: "En la mayoría de los proyectos de inversión, el GORE actúa como unidad financiera que transfiere recursos a otra entidad pública que ejerce el rol de unidad técnica responsable de diseñar, licitar, construir y recepcionar las obras."
        Src:
          - "Ley N° 19.175, Art. 81 ter."
      - Cpt: "Ejecución directa restringida a programas 'blandos'"
        Def: "La ejecución directa del GORE se concentra en programas sin infraestructura compleja (capacitaciones, estudios, fomento productivo, cultura), reflejando limitaciones estructurales para operar como 'constructora' de grandes obras."
      - Cpt: "Prohibición de usurpar funciones sectoriales"
        Def: "Las competencias del GORE no alteran las funciones de la Administración central del Estado. No puede asumir de facto roles propios de ministerios como MOP o MINSAL; su lugar es financiar y coordinar, no reemplazar a los servicios especializados."
        Src:
          - "Ley N° 19.175, Art. 106."
      - Cpt: "Limitaciones prácticas de capacidades técnicas internas"
        Def: "La dotación de personal y capacidades del GORE está diseñada para planificación, evaluación y supervisión, no para ejecución en terreno; carece de masa crítica de ingenieros, inspectores y equipos necesarios para obras de gran escala."

  Limites_Funcion_Coordinar:
    ID: GN-GORE-IDEAL-LIM-COORDINAR-01
    Items:
      - Cpt: "Ausencia de mando directo sobre servicios públicos"
        Def: "Los SEREMI dependen jerárquicamente de sus ministerios y colaboran con el Delegado Presidencial, no del Gobernador. La coordinación del GORE se ejerce sin subordinación formal sobre la mayoría de los servicios regionales."
        Src:
          - "Ley N° 19.175, Art. 62 y 63."
      - Cpt: "Autoridad paralela del Delegado Presidencial"
        Def: "El Delegado Presidencial Regional tiene atribuciones explícitas de coordinación, fiscalización y supervigilancia de servicios públicos nacionales, generando un polo de poder paralelo con frecuencia más fuerte en la cadena jerárquica que el del Gobernador."
      - Cpt: "Vínculo condicionado a relaciones financieras o competenciales"
        Def: "El poder de coordinación del Gobernador es más robusto cuando existe una relación directa (por ejemplo, a través de convenios de financiamiento o competencias transferidas); en ausencia de estos vínculos, su influencia es principalmente política."
      - Cpt: "Poder blando: convocar e informar, no instruir"
        Def: "La ley habilita al GORE a convocar y requerir información a servicios y municipios, pero no a impartir instrucciones jerárquicas. La coordinación efectiva depende de la calidad de la negociación y del uso estratégico del presupuesto como incentivo."

  Limites_Funcion_Normar:
    ID: GN-GORE-IDEAL-LIM-NORMAR-01
    Items:
      - Cpt: "Subordinación jerárquica a la ley y a los decretos supremos"
        Def: "Las normas regionales deben dictarse con sujeción a las leyes y a los decretos supremos; un reglamento regional que los contradiga es ilegal."
        Src:
          - "Ley N° 19.175, Art. 16 letra h)."
      - Cpt: "Competencia material acotada a funciones propias"
        Def: "La potestad reglamentaria del GORE se restringe a materias vinculadas a sus funciones legales; no puede regular ámbitos reservados a otros ministerios o niveles de gobierno."
      - Cpt: "Control externo de legalidad (Toma de Razón)"
        Def: "Toda norma regional está sujeta a control preventivo obligatorio de la Contraloría; actos que excedan competencias o vulneren jerarquía normativa pueden ser objetados."
      - Cpt: "Procedimiento interno con contrapesos"
        Def: "El Gobernador tiene iniciativa reglamentaria, pero el CORE debe aprobar los reglamentos de funcionamiento y otras normas internas, evitando que un solo órgano concentre el poder normativo."
      - Cpt: "Publicidad como condición de vigencia"
        Def: "Las normas regionales solo adquieren fuerza obligatoria una vez publicadas en el Diario Oficial, reforzando la transparencia y la publicidad de las reglas de juego."

Parte_III_Vision_GORE_Ideal_4_0:
  ID: GN-GORE-IDEAL-PARTE-III-01

  Introduccion:
    ID: GN-GORE-IDEAL-VISION-INTRO-01
    Def: "Describe el despliegue máximo del potencial del Gobierno Regional en un escenario de condiciones ideales: alta colaboración intergubernamental, capacidades tecnológicas avanzadas y participación ciudadana robusta."
    Cpt:
      - "El GORE deja de ser una entidad principalmente reactiva y se convierte en motor proactivo de desarrollo, innovación y gobernanza territorial."
      - "Se configura un modelo 'GORE 4.0' que fusiona mandato de desarrollo con tecnologías de la Cuarta Revolución Industrial."

  Funcion_Planificar_4_0:
    ID: GN-GORE-IDEAL-PLAN-4-0-01
    Mssn: "Posicionar al GORE como arquitecto del territorio inteligente mediante planificación basada en datos y simulaciones."
    Dimensiones:
      - Cpt: "Gemelo Digital del territorio"
        Ref: GN-GORE-IDEAL-GLOS-DIGITAL-TWIN
        Def: "La planificación se apoya en un modelo vivo que integra variables territoriales, sociales, económicas y ambientales y permite simular impactos de políticas y proyectos antes de implementarlos."
      - Cpt: "ERD y PROT como capas lógicas vinculantes"
        Ref:
          - GN-GORE-IDEAL-GLOS-ERD
          - GN-GORE-IDEAL-GLOS-PROT
        Def: "La ERD opera como hoja de ruta dinámica y el PROT como 'constitución territorial', ambos programados en el Gemelo Digital de modo que cualquier proyecto pueda ser testeado respecto de su alineamiento y coherencia multiescalar."
      - Cpt: "Centro de inteligencia territorial"
        Def: "El GORE lidera un sistema de información territorial integrado, con datos en tiempo real y analítica avanzada, que permite pasar de una planificación reactiva a una planificación predictiva y prospectiva (clima, demografía, movilidad, riesgos, participación)."
      - Cpt: "Convenios y ARI como herramientas de simulación y co-diseño"
        Def: "Los Convenios de Programación y el Anteproyecto Regional de Inversiones (ARI) se negocian utilizando simulaciones del Gemelo Digital, convirtiéndose en instrumentos de co-diseño con el nivel central basados en evidencia."
      - Cpt: "Participación ciudadana aumentada por IA"
        Def: "La 'efectiva participación de la comunidad' se amplifica mediante plataformas de deliberación masiva apoyadas por IA, que sintetizan miles de aportes ciudadanos en argumentos estructurados que alimentan la planificación."

  Funcion_Financiar_4_0:
    ID: GN-GORE-IDEAL-FIN-4-0-01
    Mssn: "Transformar al GORE en una banca de desarrollo regional inteligente que maximiza el impacto de cada peso público."
    Dimensiones:
      - Cpt: "Financiamiento estratégico y catalítico"
        Def: "Cada decisión de financiamiento se evalúa por su contribución a objetivos estratégicos de la ERD, utilizando un motor de recomendación algorítmico, supervisado por equipos humanos, para priorizar proyectos de mayor impacto social, territorial y productivo."
      - Cpt: "Portafolio diversificado de instrumentos"
        Ref:
          - GN-GORE-IDEAL-GLOS-FONDO-FNDR
          - GN-GORE-IDEAL-GLOS-FONDO-FRPD
          - GN-GORE-IDEAL-GLOS-FONDO-ISAR
        Def: "El GORE gestiona activamente un portafolio de fondos (FNDR, FRPD, ISAR y otros), combinándolos de forma estratégica para cerrar brechas sociales, habilitar infraestructura y sofisticar la estructura productiva."
      - Cpt: "Smart contracts y trazabilidad total"
        Def: "La ejecución financiera se automatiza parcialmente mediante contratos inteligentes asociados a hitos verificables (sensores, BIM, reportes digitales), de modo que los desembolsos se liberan solo cuando se comprueba el cumplimiento de metas. La trazabilidad de los fondos es pública y auditable, potencialmente reforzada por tecnologías tipo blockchain."
      - Cpt: "Ventanilla única digital con asistencia de IA"
        Def: "Los proponentes acceden a una plataforma única donde la IA guía la formulación de iniciativas, reduce errores y agiliza la obtención de la RS y demás visaciones, simplificando el ciclo burocrático."

  Funcion_Ejecutar_4_0:
    ID: GN-GORE-IDEAL-EJEC-4-0-01
    Mssn: "Consolidar al GORE como orquestador de la ejecución 4.0, garantizando calidad y oportunidad más que hacer directamente las obras."
    Dimensiones:
      - Cpt: "PMO Regional como 'torre de control'"
        Def: "Se crea una Oficina de Gestión de Proyectos (PMO) regional que opera como torre de control predictiva, monitoreando convenios y obras con datos en tiempo real (drones, sensores, sistemas de gestión) para anticipar retrasos, sobrecostos y riesgos."
      - Cpt: "Programas habilitantes para región inteligente"
        Def: "La limitada ejecución directa del GORE se concentra en programas habilitantes que fortalecen capacidades digitales y de gestión de municipios y servicios (plataformas de IA como servicio, capacitación, estándares de datos), creando las bases para la infraestructura inteligente."
      - Cpt: "Unidades de desbloqueo aumentadas por IA"
        Def: "Se implementa una unidad especializada en 'desbloquear' procesos burocráticos críticos (permisología, compras públicas, coordinación multi-actor), apoyada por IA para mapear cuellos de botella y rediseñar procesos de forma sistémica."

  Funcion_Coordinar_4_0:
    ID: GN-GORE-IDEAL-COORD-4-0-01
    Mssn: "Convertir al GORE en plataforma de gobernanza como servicio (GaaP), habilitando colaboración descentralizada entre actores públicos y privados."
    Dimensiones:
      - Cpt: "Co-diseño vertical con el nivel central"
        Def: "La relación con el gobierno nacional evoluciona hacia un co-diseño de políticas públicas, donde los datos y simulaciones del Gemelo Digital regional informan ajustes en políticas nacionales y convenios de inversión conjunta."
      - Cpt: "Sincronización horizontal del aparato público regional"
        Def: "El Gobernador lidera un 'gabinete regional de desarrollo' de facto en el que la interoperabilidad de sistemas y una 'fuente única de verdad' de datos permiten coordinar agendas y presupuestos entre servicios, GORE y municipios."
      - Cpt: "Empoderamiento territorial de los municipios"
        Def: "El GORE provee a los municipios servicios de alto valor (plataforma de datos, herramientas de IA, asistencia técnica avanzada), nivelando capacidades y reduciendo brechas institucionales entre comunas."
      - Cpt: "Articulación ampliada vía APIs y datos abiertos"
        Def: "La coordinación con privados, academia y sociedad civil se realiza mediante APIs y catálogos de datos abiertos que permiten construir servicios y soluciones sobre la infraestructura de información regional, con el GORE como broker de conocimiento."

  Funcion_Normar_4_0:
    ID: GN-GORE-IDEAL-NORM-4-0-01
    Mssn: "Usar la potestad reglamentaria como palanca habilitante y basada en evidencia para acelerar el desarrollo territorial."
    Dimensiones:
      - Cpt: "Regulación basada en misiones y estándares"
        Def: "El GORE dicta reglamentos que dan fuerza ejecutiva a sus planes y establecen estándares de calidad, sostenibilidad e interoperabilidad de datos que toda iniciativa financiada por recursos regionales debe cumplir."
      - Cpt: "Proceso normativo dinámico y co-diseñado"
        Def: "Las normas se elaboran mediante procesos abiertos con consultas públicas tempranas y análisis de impacto regulatorio, y se actualizan en ciclos cortos a partir de evidencia sobre su efectividad, en diálogo permanente con la Contraloría."
      - Cpt: "Simplificación y sandboxes regulatorios"
        Def: "La prioridad normativa es simplificar y unificar procedimientos críticos y, en paralelo, crear sandboxes regulatorios que permitan experimentar con nuevas tecnologías (IA, movilidad autónoma, energías distribuidas) en entornos controlados, posicionando a la región como laboratorio vivo de innovación pública."
