---
urn: urn:gn:kb:kb-estructura-estado-chile
nombre: kb-estructura-estado-chile
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre KODA/Spec Artifact for Estructura del Estado de Chile; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/estadocl/kb_core_007_estructura_estado_chile_koda.yml (sha256:0adadbcfe5bfa1f05868d62a645f07a9875e5741a4ce0f825fa5745c550d5a28); URN KODA legado urn:gorenuble:kb:estructura-estado-chile:1.0.0; estado original Published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-27
lang: es
tags: ["gn", "gore-os", "koda", "domains", "estadocl", "kb", "estructura", "estado"]
familia: bok
---
# KODA/Spec Artifact for Estructura del Estado de Chile
# Derived from kb_core_007_estructura_estado_chile.md

_manifest:
  urn: "urn:gorenuble:kb:estructura-estado-chile:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/core/kb_core_007_estructura_estado_chile_koda.yml"
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
    model_collaborators: ["Cascade"]

ID: GOBCL-MASTER-01
Version: 1.0.0
Status: Published
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: Cascade
Creation-Date: 2025-11-27
Modification-Date: 2025-11-27
Source:
  Ctx_Required:
    - "staging/gn/kb_core_007_estructura_estado_chile.md"
    - "DFL N° 1-19.175 (LOC GORE)"
Ctx: "Síntesis estructurada de la gobernanza y estructura del Estado de Chile, como marco general para la administración regional y los GORE."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External legal and policy sources are mentioned under Ctx: or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_Conceptos_Clave:
  ID: GOBCL-GLOSARIO-01
  Purp: "Definir conceptos estructurales recurrentes del Estado de Chile."
  Terminos:
    - ID: GOBCL-GLOS-ESTADO
      Cpt: "Estado"
      Def: "Fenómeno colectivo compuesto por población, territorio, poder y organización jurídica, orientado al bien común."
    - ID: GOBCL-GLOS-POBLACION
      Cpt: "Población"
      Def: "Conjunto de personas que habitan el territorio del Estado, sin distinción de edad, género o condición."
    - ID: GOBCL-GLOS-NACIONALIDAD
      Cpt: "Nacionalidad"
      Def: "Vínculo jurídico que une a una persona con un Estado determinado."
      Src: "CPR Art. 10."
    - ID: GOBCL-GLOS-CIUDADANIA
      Cpt: "Ciudadanía"
      Def: "Calidad que emana de requisitos constitucionales y habilita para ejercer derechos políticos."
      Src: "CPR Art. 13 y 17."
    - ID: GOBCL-GLOS-GORE
      Cpt: "Gobierno Regional (GORE)"
      Def: "Institución descentralizada con personalidad jurídica y patrimonio propio, a cargo de la administración superior de la región."
      Src: "Ley N° 19.175 (DFL 1-19.175)."
    - ID: GOBCL-GLOS-MUNICIPALIDAD
      Cpt: "Municipalidad"
      Def: "Órgano encargado de la administración de una comuna, liderado por alcalde y concejo municipal."

Normativa_Clave:
  ID: GOBCL-NORMATIVA-01
  Purp: "Definir fuentes normativas principales referenciadas en el artefacto."
  Normas:
    - ID: GOBCL-NORM-CPR-01
      Cpt: "Constitución Política de la República"
      Def: "Norma suprema del ordenamiento jurídico chileno."
    - ID: GOBCL-NORM-LOC-GORE-01
      Cpt: "Ley N° 19.175 (LOC GORE)"
      Def: "Ley Orgánica Constitucional sobre Gobierno y Administración Regional, texto refundido en DFL N° 1-19.175/2005."
    - ID: GOBCL-NORM-DL-1263-01
      Cpt: "DL N° 1.263"
      Def: "Ley Orgánica de Administración Financiera del Estado."
    - ID: GOBCL-NORM-LEY-18575-01
      Cpt: "Ley N° 18.575"
      Def: "Ley Orgánica Constitucional de Bases Generales de la Administración del Estado."
    - ID: GOBCL-NORM-LEY-19886-01
      Cpt: "Ley N° 19.886"
      Def: "Ley de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios (Compras Públicas)."
    - ID: GOBCL-NORM-LEY-19862-01
      Cpt: "Ley N° 19.862"
      Def: "Ley sobre Registros de Personas Jurídicas Receptoras de Fondos Públicos."
    - ID: GOBCL-NORM-LEY-20128-01
      Cpt: "Ley N° 20.128"
      Def: "Ley de Responsabilidad Fiscal."
    - ID: GOBCL-NORM-CC-01
      Cpt: "Código Civil"
      Def: "Cuerpo legal que define normas generales de derecho civil en Chile."

Parte_1_Fundamentos_Estado_Chileno:
  ID: GOBCL-FUNDAMENTOS-01
  Ctx: "Basado en sección 1 del documento fuente."

  Concepto_y_Elementos_Estado_Moderno:
    ID: GOBCL-FUNDAMENTOS-CONCEPTO-01
    Ref: GOBCL-GLOS-ESTADO
    Def: "Fenómeno colectivo compuesto por población, territorio, poder y organización jurídica, orientado al bienestar de los asociados."
    Componentes_Centrales:
      - Cpt: "Población"
        Def: "Grupo de personas que habitan el territorio del Estado."
      - Cpt: "Territorio"
        Def: "Espacio físico y jurídico sobre el cual el Estado ejerce poder."
      - Cpt: "Poder"
        Def: "Capacidad de conducción hacia el bien común y de imponer conductas."
      - Cpt: "Organización Jurídica"
        Def: "Sistema normativo e institucional que regula relaciones entre órganos del Estado y personas."
      - Cpt: "Finalidad"
        Def: "Bien común, según mandato constitucional."

  Elemento_Poblacion:
    ID: GOBCL-FUNDAMENTOS-ELEM-POBLACION-01
    Ref: GOBCL-GLOS-POBLACION
    Def: "Componente sociológico del Estado."
    Distinciones_Clave:
      - Cpt: "Pueblo"
        Def: "Conjunto de personas que habitan el territorio del Estado."
      - Cpt: "Criterio de inclusión"
        Def: "Sin distinción de edad, género, condición económica o cultural, etnia, credo o lengua."
      - Cpt: "Alcance"
        Def: "Incluye nacionales y extranjeros transeúntes."
      - Cpt: "Ciudadanos"
        Def: "Subconjunto del pueblo definido por la Constitución."
    Nacionalidad:
      ID: GOBCL-POBLACION-NACIONALIDAD-01
      Def: "Vínculo jurídico con el Estado."
      Ref_Normativa:
        - Ref: GOBCL-NORM-CPR-01
          Detalle: "Art. 10."
      Causales_Chilenidad:
        - "Ius Solis: Nacidos en territorio de Chile."
        - "Ius Sanguinis: Hijos de padre o madre chilenos, nacidos en el extranjero."
        - "Por gracia o carta: Concesión legal de nacionalización."
    Ciudadania:
      ID: GOBCL-POBLACION-CIUDADANIA-01
      Def: "Calidad que habilita ejercicio de derechos políticos."
      Ref_Normativa:
        - Ref: GOBCL-NORM-CPR-01
          Detalle: "Art. 13 y 17."
      Req:
        - "Ser chileno."
        - "18 años o más."
        - "No haber sido condenado a pena aflictiva."
      Derechos_Politicos:
        - "Derecho a sufragio."
        - "Derecho a optar a cargos de elección popular."
        - "Otros derechos conferidos por CPR o ley."

  Elemento_Territorio:
    ID: GOBCL-FUNDAMENTOS-ELEM-TERRITORIO-01
    Def: "Espacio geográfico y jurídico donde el Estado ejerce su poder."
    Componentes:
      - Cpt: "Territorio Físico"
        Def: "Suelo y subsuelo delimitado por límites jurídicos, incluyendo aguas internas."
      - Cpt: "Territorio Marítimo"
        Def: "Prolongación del espacio terrestre hacia el mar."
        Subzonas:
          - "Mar Territorial: soberanía hasta 12 millas."
          - "Zona Contigua: jurisdicción hasta 24 millas."
          - "Zona Económica Exclusiva: hasta 200 millas."
      - Cpt: "Espacio Aéreo"
        Def: "Columna de atmósfera sobre territorio y mar territorial."
      - Cpt: "Territorio Jurídico"
        Def: "Lugares reconocidos como jurisdicción estatal (naves, embajadas, etc.)."

  Elemento_Poder:
    ID: GOBCL-FUNDAMENTOS-ELEM-PODER-01
    Def: "Fuerza de la voluntad social destinada al bien común, con capacidad de imponer conductas."
    Manifestaciones_Funcionales:
      - Cpt: "Función Legislativa"
        Def: "Dictar normas vinculantes."
        Resp: "Congreso Nacional y Presidente (co-legislador)."
      - Cpt: "Función Ejecutiva"
        Def: "Aplicar las normas dictadas."
        Resp: "Gobierno."
      - Cpt: "Función Judicial"
        Def: "Resolver conflictos con resoluciones exigibles, con potestad de imperio."
        Resp: "Tribunales de Justicia."

  Elemento_Organizacion_Juridica:
    ID: GOBCL-FUNDAMENTOS-ELEM-ORG-JURIDICA-01
    Def: "Institucionalidad basada en normas, valores y principios jurídicos vigentes."
    Purp: "Regular relaciones entre miembros e instituciones de la sociedad."
    Jerarquia_Normativa:
      - "Constitución Política de la República (CPR)."
      - "Leyes."
      - "Decretos con Fuerza de Ley (DFL)."
      - "Decretos Supremos."
      - "Reglamentos."
    Distinciones_Derecho:
      - Cpt: "Derecho Público"
        Purp: "Regula relaciones entre órganos del Estado y personas."
        Fnd: "Solo se puede hacer lo que la ley permite (CPR Art. 6 y 7)."
      - Cpt: "Derecho Privado"
        Purp: "Regula relaciones entre particulares y el Estado actuando como tal."
        Fnd: "Se puede hacer todo lo que no esté prohibido."

  Elemento_Finalidad:
    ID: GOBCL-FUNDAMENTOS-ELEM-FINALIDAD-01
    Def: "El fin último del Estado es el bien común."
    Ref_Normativa:
      - Ref: GOBCL-NORM-CPR-01
        Detalle: "Art. 1."
    Mandato_CPR:
      Def: "El Estado está al servicio de la persona humana y su finalidad es promover el bien común."
    Bien_Comun_Segun_CPR:
      Def: "Deber del Estado de crear condiciones sociales para la realización espiritual y material de cada persona, respetando derechos y garantías."

  Principios_Rectores:
    ID: GOBCL-FUNDAMENTOS-PRINCIPIOS-01
    Estado_de_Derecho:
      ID: GOBCL-PRINCIPIOS-ESTADO-DERECHO-01
      Def: "Sumisión del poder político a un ordenamiento jurídico que respeta estándares internacionales de DDHH."
      Bases_Fundamentales:
        - "Imperio de la ley."
        - "Distribución del poder estatal."
        - "Legalidad y responsabilidad de autoridades."
        - "Respeto y garantía de DDHH."
        - "Juridicidad de órganos públicos."
        - "Soberanía popular."
        - "Probidad en la función pública (CPR Art. 8)."
    Estado_Democratico:
      ID: GOBCL-PRINCIPIOS-ESTADO-DEMOCRATICO-01
      Def: "Gobierno del pueblo, por el pueblo y para el pueblo."
      Pilares:
        - Cpt: "Soberanía Popular"
          Def: "Participación en decisiones de interés general mediante elecciones, consultas, plebiscitos."
        - Cpt: "Representación Política"
          Def: "Ejercicio del poder a través de representantes electos."

Parte_2_Poderes_Centrales_Estado:
  ID: GOBCL-PODERES-CENTRALES-01
  Ctx: "Basado en sección 2 del documento fuente."

  Poder_Legislativo_Congreso_Nacional:
    ID: GOBCL-PODERES-LEGISLATIVO-01
    Funcion_Esencial:
      ID: GOBCL-LEGISLATIVO-ESTRUCTURA-01
      Cpt: "Función Legislativa"
      Def: "Participar en la creación, modificación o derogación de la ley."
      Estructura:
        Def: "Congreso bicameral."
        Componentes:
          - "Senado."
          - "Cámara de Diputadas y Diputados."
      Composicion_Basica:
        Diputados:
          Eleccion: "Votación directa."
          Periodo: "4 años, renovación total."
          Base_Electoral: "Distritos electorales."
          Reeleccion: "Sin limitaciones."
        Senadores:
          Eleccion: "Votación directa."
          Periodo: "8 años, renovación parcial cada 4 años."
          Base_Electoral: "Circunscripciones senatoriales (regiones)."
          Reeleccion: "Sin limitaciones."
    Proceso_Formacion_Ley:
      ID: GOBCL-LEGISLATIVO-FORMACION-LEY-01
      Def: "Declaración de la voluntad soberana que manda, prohíbe o permite, según forma prescrita por la Constitución."
      Ref_Normativa:
        - Ref: GOBCL-NORMATIVA-01
          Detalle: "Código Civil Art. 1."
      Etapas:
        - Cpt: "Origen"
          Def: "Cámara de origen y cámara revisora; excepciones para materias iniciadas solo en Diputados o en Senado."
        - Cpt: "Iniciativa"
          Actores:
            - "Presidente de la República (mensaje)."
            - "Parlamentarios (moción, con límites de firmas)."
          Iniciativa_Exclusiva_Presidente:
            Ref_Normativa:
              - Ref: GOBCL-NORMATIVA-01
                Detalle: "Art. 65 de la Constitución Política de la República."
            Ejemplos:
              - "División político-administrativa."
              - "Empleos y remuneraciones públicas."
              - "Tributos."
              - "Seguridad social."
        - Cpt: "Discusión"
          Purp: "Analizar proyecto hasta aprobación de texto definitivo."
        - Cpt: "Aprobación"
          Req: "Quórum mínimo según tipo de ley (interpretativa, orgánica constitucional, quórum calificado, ordinaria)."
        - Cpt: "Sanción"
          Def: "Aprobación presidencial."
        - Cpt: "Promulgación"
          Def: "Acto solemne que reconoce el texto de ley aprobado."
        - Cpt: "Publicación"
          Def: "Inserción en Diario Oficial; ley entra en vigencia."
      Mecanismo_Urgencias:
        Purp: "Acelerar tramitación."
        Tipos:
          - "Urgencia simple: 30 días."
          - "Suma urgencia: 15 días."
          - "Discusión inmediata: 6 días."

  Poder_Judicial:
    ID: GOBCL-PODERES-JUDICIAL-01
    Principios_y_Atribuciones:
      ID: GOBCL-JUDICIAL-PRINCIPIOS-01
      Mssn: "Administrar justicia."
      Def: "Resolver conflictos de relevancia jurídica con resoluciones exigibles, incluso por la fuerza."
      Exclusividad: "Radicada en Tribunales de Justicia (CPR Art. 76)."
      Principios_Constitucionales:
        - "Independencia."
        - "Legalidad (tribunales creados por ley)."
        - "Inamovilidad relativa de jueces."
        - "Inexcusabilidad (deben resolver siempre)."
        - "Responsabilidad por actos ministeriales."
      Atribuciones_Principales:
        - "Conocer conflictos."
        - "Resolver mediante sentencias y resoluciones."
        - "Hacer ejecutar lo juzgado (potestad de imperio)."
    Organizacion_Tribunales:
      ID: GOBCL-JUDICIAL-ORGANIZACION-01
      Clasificacion:
        Tribunales_Ordinarios:
          Def: "Conocen generalidad de materias no entregadas a otros tribunales."
          Ejemplos:
            - "Juzgados de Letras."
            - "Juzgados de Garantía."
            - "Tribunales de Juicio Oral en lo Penal."
            - "Cortes de Apelaciones."
            - "Corte Suprema."
        Tribunales_Especiales:
          Def: "Creados por ley para materias específicas."
          Ejemplos:
            - "Juzgados de Familia."
            - "Juzgados del Trabajo."
            - "Tribunales Militares."
            - "Tribunales Tributarios y Aduaneros."
            - "Tribunales Ambientales."
            - "Juzgados de Policía Local."

  Poder_Ejecutivo_Gobierno_Central:
    ID: GOBCL-PODERES-EJECUTIVO-01
    Presidente_Republica:
      ID: GOBCL-EJECUTIVO-PRESIDENTE-01
      Cpt: "Función Ejecutiva"
      Actividades:
        - "Gobernar: fijar fines, rumbos y órdenes."
        - "Administrar: ejecutar acciones para cumplir fines."
      Rol_Presidente:
        - "Jefe de Estado y Jefe de Gobierno."
        - "Conservación del orden público interno y seguridad externa."
        - "Dirección del gobierno y administración del Estado."
        - "Promulgación de leyes."
        - "Conducción de relaciones exteriores."
        - "Jefatura suprema de las FF.AA."
      Ref_Normativa:
        - Ref: GOBCL-NORMATIVA-01
          Detalle: "Art. 24 de la Constitución Política de la República."
    Ministerios:
      ID: GOBCL-EJECUTIVO-MINISTERIOS-ESTRUCTURA-01
      Cpt: "Ministros de Estado"
      Def: "Colaboradores directos e inmediatos del Presidente."
      Ministerios_Def:
        Def: "Organismos superiores de colaboración en funciones de gobierno y administración sectorial."
        Ref_Normativa:
          - Ref: GOBCL-NORMATIVA-01
            Detalle: "Art. 22 de la Ley N° 18.575."
      Funciones_Generales:
        - "Proponer, ejecutar y evaluar políticas y planes."
        - "Estudiar y proponer normas sectoriales."
        - "Velar por cumplimiento de normas."
        - "Asignar recursos."
        - "Fiscalizar actividades del sector."
      Estructura_Basica:
        - Cpt: "Subsecretarías"
          Resp: "Subsecretario, colaborador inmediato del ministro."
        - Cpt: "Secretarías Regionales Ministeriales (SEREMI)"
          Nat: "Desconcentración territorial."
        - Cpt: "Organización Interna"
          Def: "Divisiones, departamentos, secciones, oficinas."
    Ministerios_Principales_y_Misiones:
      ID: GOBCL-EJECUTIVO-MINISTERIOS-DETALLE-01
      Lista_Ministerios:
        - ID: GOBCL-MIN-INTERIOR-01
          Nombre: "Ministerio del Interior y Seguridad Pública"
          Mssn: "Gestionar seguridad interna, orden público, coordinación del desarrollo regional/local y asuntos de las Fuerzas de Orden y Seguridad."
          Estructura:
            - "Subsecretaría de Desarrollo Regional y Administrativo (SUBDERE)."
            - "Subsecretaría de Prevención del Delito."
            - "Subsecretaría del Interior."
          Dependencias_Claves:
            - "Carabineros, PDI, ANI."
            - "Delegaciones Presidenciales, Gobiernos Regionales, municipalidades."
            - "SENAPRED, SENDA, Servicio Nacional de Migraciones."
        - ID: GOBCL-MIN-EXTERIORES-01
          Nombre: "Ministerio de Relaciones Exteriores"
          Mssn: "Formular y ejecutar la política exterior, proteger a chilenos en el extranjero y negociar tratados internacionales."
          Estructura:
            - "Subsecretaría de Relaciones Exteriores."
            - "Subsecretaría de Relaciones Económicas Internacionales (SUBREI)."
          Dependencias_Claves:
            - "ProChile, AGCID, DIFROL, INACH."
        - ID: GOBCL-MIN-DEFENSA-01
          Nombre: "Ministerio de Defensa Nacional"
          Mssn: "Dirigir las Fuerzas Armadas para la defensa y seguridad nacional."
          Estructura:
            - "Subsecretaría para las Fuerzas Armadas."
            - "Subsecretaría de Defensa."
            - "Estado Mayor Conjunto (EMCO)."
          Dependencias_Claves:
            - "Ejército, Armada, Fuerza Aérea."
            - "DGAC, DIRECTEMAR, DGMN, FAMAE, ASMAR, ENAER."
        - ID: GOBCL-MIN-HACIENDA-01
          Nombre: "Ministerio de Hacienda"
          Mssn: "Gestionar las finanzas públicas, el presupuesto nacional, la recaudación fiscal y la política económica."
          Estructura:
            - "Subsecretaría de Hacienda."
            - "Dirección de Presupuestos (DIPRES)."
            - "Servicio de Tesorerías."
          Dependencias_Claves:
            - "SII, Aduanas, CMF, ChileCompra, Servicio Civil, UAF."
        - ID: GOBCL-MIN-SEGPRES-01
          Nombre: "Ministerio Secretaría General de la Presidencia (SEGPRES)"
          Mssn: "Coordinar la relación entre el Poder Ejecutivo y el Congreso Nacional, y apoyar la formulación de leyes."
          Dependencias_Claves:
            - "INDH, Consejo para la Transparencia, Defensoría de la Niñez."
        - ID: GOBCL-MIN-SEGEGOB-01
          Nombre: "Ministerio Secretaría General de Gobierno (SEGEGOB)"
          Mssn: "Actuar como portavoz del Gobierno, gestionar la comunicación y difundir las políticas públicas."
          Dependencias_Claves:
            - "TVN, CNTV."
        - ID: GOBCL-MIN-ECONOMIA-01
          Nombre: "Ministerio de Economía, Fomento y Turismo"
          Mssn: "Promover el desarrollo económico, la competitividad, la innovación, el turismo y apoyar a las MIPYMES."
          Estructura:
            - "Subsecretaría de Economía y Empresas de Menor Tamaño."
            - "Subsecretaría de Turismo."
            - "Subsecretaría de Pesca y Acuicultura."
          Dependencias_Claves:
            - "CORFO, SERNAC, INE, FNE, SERNATUR, SERNAPESCA."
        - ID: GOBCL-MIN-DESARROLLO-SOCIAL-01
          Nombre: "Ministerio de Desarrollo Social y Familia"
          Mssn: "Diseñar políticas de protección social para mejorar la calidad de vida, especialmente de los grupos vulnerables."
          Estructura:
            - "Subsecretaría de Evaluación Social."
            - "Subsecretaría de la Niñez."
            - "Subsecretaría de Servicios Sociales."
          Dependencias_Claves:
            - "FOSIS, SENAMA, CONADI, INJUV, SENADIS."
            - "Servicio de Protección Especializada a la Niñez y Adolescencia."
        - ID: GOBCL-MIN-EDUCACION-01
          Nombre: "Ministerio de Educación (MINEDUC)"
          Mssn: "Formular y aplicar políticas educativas en todos los niveles para asegurar calidad y equidad."
          Estructura:
            - "Subsecretaría de Educación."
            - "Subsecretaría de Educación Parvularia."
            - "Subsecretaría de Educación Superior."
          Dependencias_Claves:
            - "JUNAEB, JUNJI, Superintendencia de Educación, Agencia de Calidad."
            - "Dirección de Educación Pública, Servicios Locales de Educación."
        - ID: GOBCL-MIN-JUSTICIA-DDHH-01
          Nombre: "Ministerio de Justicia y Derechos Humanos"
          Mssn: "Articular la administración de justicia, proteger los derechos humanos y gestionar el sistema penitenciario."
          Estructura:
            - "Subsecretaría de Justicia."
            - "Subsecretaría de Derechos Humanos."
          Dependencias_Claves:
            - "Gendarmería, SML, Registro Civil, Defensoría Penal Pública."
            - "Corporaciones de Asistencia Judicial, Servicio de Reinserción Social Juvenil."
        - ID: GOBCL-MIN-TRABAJO-01
          Nombre: "Ministerio del Trabajo y Previsión Social"
          Mssn: "Diseñar y gestionar las políticas laborales y de seguridad social del país."
          Estructura:
            - "Subsecretaría del Trabajo."
            - "Subsecretaría de Previsión Social."
          Dependencias_Claves:
            - "SENCE, Dirección del Trabajo, IPS, ISL, Superintendencia de Pensiones, Superintendencia de Seguridad Social."
        - ID: GOBCL-MIN-MOP-01
          Nombre: "Ministerio de Obras Públicas (MOP)"
          Mssn: "Planificar, construir y mantener la infraestructura pública del país."
          Estructura:
            - "Subsecretaría de Obras Públicas."
            - "Dirección General de Obras Públicas (DGOP)."
            - "Dirección General de Concesiones de Obras Públicas."
            - "Dirección General de Aguas (DGA)."
        - ID: GOBCL-MIN-SALUD-01
          Nombre: "Ministerio de Salud (MINSAL)"
          Mssn: "Construir un modelo de salud centrado en el paciente y basado en una atención primaria fortalecida."
          Estructura:
            - "Subsecretaría de Salud Pública."
            - "Subsecretaría de Redes Asistenciales."
          Dependencias_Claves:
            - "Servicios de Salud, FONASA, ISP, CENABAST, Superintendencia de Salud."
        - ID: GOBCL-MIN-MINVU-01
          Nombre: "Ministerio de Vivienda y Urbanismo (MINVU)"
          Mssn: "Formular políticas de vivienda y urbanismo para mejorar la habitabilidad y el desarrollo equilibrado de las ciudades."
          Estructura:
            - "Subsecretaría de Vivienda y Urbanismo."
          Dependencias_Claves:
            - "Servicios Regionales de Vivienda y Urbanización (SERVIU)."
        - ID: GOBCL-MIN-AGRICULTURA-01
          Nombre: "Ministerio de Agricultura"
          Mssn: "Promover el desarrollo sostenible del sector agrícola, forestal y ganadero."
          Dependencias_Claves:
            - "INDAP, SAG, CONAF, CNR, ODEPA."
        - ID: GOBCL-MIN-MINERIA-01
          Nombre: "Ministerio de Minería"
          Mssn: "Regular y promover el desarrollo sostenible y eficiente del sector minero."
          Dependencias_Claves:
            - "CODELCO, ENAMI, COCHILCO, SERNAGEOMIN."
        - ID: GOBCL-MIN-MTT-01
          Nombre: "Ministerio de Transportes y Telecomunicaciones (MTT)"
          Mssn: "Desarrollar y regular el funcionamiento eficiente de los sistemas de transporte y telecomunicaciones."
          Estructura:
            - "Subsecretaría de Transportes."
            - "Subsecretaría de Telecomunicaciones (SUBTEL)."
          Dependencias_Claves:
            - "EFE, Correos de Chile, Empresas Portuarias, JAC."
        - ID: GOBCL-MIN-BIENES-NACIONALES-01
          Nombre: "Ministerio de Bienes Nacionales"
          Mssn: "Administrar el patrimonio fiscal para su uso eficiente y conservación."
        - ID: GOBCL-MIN-ENERGIA-01
          Nombre: "Ministerio de Energía"
          Mssn: "Formular políticas para un suministro energético seguro, sostenible y accesible."
          Dependencias_Claves:
            - "SEC, CCHEN, CNE, ENAP."
        - ID: GOBCL-MIN-MMA-01
          Nombre: "Ministerio del Medio Ambiente (MMA)"
          Mssn: "Diseñar y aplicar políticas para proteger los recursos naturales y promover el desarrollo sostenible."
          Dependencias_Claves:
            - "SEA, SMA, Servicio de Biodiversidad y Áreas Protegidas."
        - ID: GOBCL-MIN-DEPORTE-01
          Nombre: "Ministerio del Deporte"
          Mssn: "Fomentar y desarrollar la actividad física y el deporte en la población."
          Dependencias_Claves:
            - "Instituto Nacional de Deportes (IND)."
        - ID: GOBCL-MIN-MUJER-EG-01
          Nombre: "Ministerio de la Mujer y la Equidad de Género"
          Mssn: "Promover la igualdad de derechos y oportunidades, y erradicar la violencia de género."
          Dependencias_Claves:
            - "Servicio Nacional de la Mujer y la Equidad de Género (SERNAMEG)."
        - ID: GOBCL-MIN-CULTURAS-01
          Nombre: "Ministerio de las Culturas, las Artes y el Patrimonio"
          Mssn: "Fomentar la cultura, las artes y la preservación del patrimonio nacional."
          Estructura:
            - "Subsecretaría de las Culturas y las Artes."
            - "Subsecretaría del Patrimonio Cultural."
          Dependencias_Claves:
            - "Servicio Nacional del Patrimonio Cultural, Consejo de Monumentos Nacionales."
        - ID: GOBCL-MIN-CIENCIA-01
          Nombre: "Ministerio de Ciencia, Tecnología, Conocimiento e Innovación"
          Mssn: "Fomentar la investigación científica, el desarrollo tecnológico y la innovación."
          Dependencias_Claves:
            - "Agencia Nacional de Investigación y Desarrollo (ANID)."

    Servicios_Publicos_Nacionales:
      ID: GOBCL-EJECUTIVO-SERVICIOS-PUBLICOS-01
      Def: "Órganos administrativos encargados de satisfacer necesidades colectivas de manera regular y continua."
      Ref_Normativa:
        - Ref: GOBCL-NORMATIVA-01
          Detalle: "Art. 28 de la Ley N° 18.575."
      Dependencia:
        - "Centralizados: personalidad jurídica y recursos del Fisco; dependencia directa del Presidente."
        - "Descentralizados: personalidad jurídica y patrimonio propio; supervigilancia del Presidente."
      Desconcentracion:
        - Cpt: "Territorial"
          Def: "Direcciones regionales bajo dependencia jerárquica de la Dirección Nacional."
        - Cpt: "Funcional"
          Def: "Atribuciones radicadas por ley en órganos específicos dentro de un servicio."

Parte_3_Estructura_Territorial_Estado:
  ID: GOBCL-ESTRUCTURA-TERRITORIAL-01
  Ctx: "Basado en sección 3 del documento fuente."

  Administracion_Regional:
    ID: GOBCL-TERRITORIAL-ADMIN-REGIONAL-01
    Componentes:
      - Cpt: "Administración sectorial"
        Def: "Desconcentración de ministerios y servicios (SEREMI, direcciones regionales)."
      - Cpt: "Administración descentralizada"
        Def: "A cargo de Gobiernos Regionales (GORE)."
      - Cpt: "Gobierno Interior"
        Def: "Estructura del Estado unitario ejercida por Delegado Presidencial Regional."

    Gobierno_Interior_Delegaciones:
      ID: GOBCL-ADMIN-REGIONAL-GOB-INTERIOR-01
      Fnd: "La función de gobierno en un Estado unitario no es descentralizable."
      Resp: "Presidente, a través del Ministerio del Interior y Seguridad Pública."
      Materias_No_Descentralizables:
        - "Orden público y seguridad ciudadana."
        - "Coordinación y supervisión de servicios públicos nacionales en la región."
        - "Extranjería."
      Estructura:
        - Cpt: "Delegación Presidencial Regional (DPR)"
          Def: "Órgano del gobierno interior que sucede a la intendencia."
        - Cpt: "Delegación Presidencial Provincial (DPP)"
          Def: "Órgano desconcentrado del Delegado Presidencial Regional."

    Administracion_Desconcentrada:
      ID: GOBCL-ADMIN-REGIONAL-DESCONCENTRADA-01
      SEREMI:
        Def: "Órganos desconcentrados que representan ministerios en la región."
        Resp: "Secretario Regional Ministerial."
        Funciones_Claves:
          - "Representar al ministerio."
          - "Aplicar políticas nacionales sectoriales."
          - "Subordinarse al Delegado Presidencial Regional en materias de gobierno interior."
      Direcciones_Regional_Servicios:
        Def: "Órganos desconcentrados de servicios públicos nacionales."
        Resp: "Director Regional (Alta Dirección Pública)."

    Administracion_Descentralizada_GORE:
      ID: GOBCL-ADMIN-REGIONAL-DESCENTRALIZADA-01
      Def: "Institución descentralizada con personalidad jurídica y patrimonio propio."
      Purp: "Conducir asuntos comunitarios y satisfacer necesidades públicas para el desarrollo regional."
      Ref_Normativa:
        - Ref: GOBCL-NORMATIVA-01
          Detalle: "Ley N° 19.175."
      Estructura_GORE:
        Gobernador_Regional:
          Rol: "Órgano ejecutivo del GORE."
          Eleccion: "Sufragio universal, período de 4 años, reelección inmediata una vez."
        Consejo_Regional:
          Rol: "Órgano normativo, resolutivo y fiscalizador."
          Eleccion: "Sufragio universal, período de 4 años, reelección inmediata hasta dos veces."
      Funciones_y_Principios:
        ID: GOBCL-GORE-FUNCIONES-PRINCIPIOS-01
        Funciones_Claves:
          - "Planificación del desarrollo regional."
          - "Decisión sobre inversión pública regional (FNDR, otros fondos)."
          - "Ejecución de planes y programas."
          - "Dictación de normas generales de su competencia."
          - "Coordinación con gobierno nacional."
          - "Ordenamiento territorial regional."
          - "Fomento productivo e innovación."
          - "Desarrollo social y cultural."
          - "Prevención del delito y apoyo a víctimas."
          - "Gestión de emergencias."
        Principios_Rectores:
          - "Equidad, eficacia, eficiencia."
          - "Participación efectiva de la comunidad."
          - "Preservación y mejora del medio ambiente."
          - "Probidad, transparencia y responsabilidad."
      Estructura_Organica_Detalle:
        ID: GOBCL-GORE-ORGANIZACION-01
        Componentes:
          - "Gobernador Regional (máxima autoridad ejecutiva, preside CORE)."
          - "Consejo Regional (órgano colegiado normativo y fiscalizador)."
          - "Servicio Administrativo del GORE (liderado por Gobernador y Administrador Regional)."
          - "Divisiones técnicas (DAF, DIPLADE, DIPIR, DIDESOH, DIT, DIFOI)."
          - "Unidad de Control (auditoría interna)."
      Instrumentos_Planificacion_e_Inversion:
        ID: GOBCL-GORE-INSTRUMENTOS-01
        Instrumentos_Planificacion_Estrategica:
          - "Estrategia Regional de Desarrollo (ERD)."
          - "Plan Regional de Ordenamiento Territorial (PROT)."
          - "Zonificación de Uso del Borde Costero (ZUBC)."
          - "Planes Reguladores Intercomunales/Metropolitanos (PRI/PRM)."
        Instrumentos_Inversion:
          - "Fondo Nacional de Desarrollo Regional (FNDR)."
          - "Convenios de Programación GORE-Ministerios."
          - "Anteproyecto Regional de Inversiones (ARI)."
      Transferencia_Competencias:
        ID: GOBCL-GORE-TRANSFERENCIA-COMPETENCIAS-01
        Prop: "Regular traspaso de facultades desde ministerios y servicios públicos a los GORE."
        Materias_Transferibles:
          - "Ordenamiento territorial."
          - "Fomento productivo."
          - "Desarrollo social y cultural."
        Modalidad: "Temporal o definitiva."
        Iniciativa: "De oficio (Presidente) o a solicitud del GORE."

  Administracion_Comunal_Municipalidades:
    ID: GOBCL-TERRITORIAL-ADMIN-MUNICIPAL-01
    Ref: GOBCL-GLOS-MUNICIPALIDAD
    Def: "Órgano encargado de la administración de una comuna."
    Mssn: "Satisfacer necesidades locales y asegurar el progreso comunal."
    Organos:
      - "Alcalde (órgano ejecutivo)."
      - "Concejo Municipal (órgano normativo y fiscalizador)."
    Funciones_Municipalidad:
      ID: GOBCL-MUNICIPAL-FUNCIONES-01
      Funciones_Privativas:
        - "PLADECO: elaboración y ejecución del plan de desarrollo comunal."
        - "Aplicar planes reguladores y normar edificación."
        - "Promover desarrollo comunitario."
        - "Gestionar tránsito y transporte público local."
        - "Gestionar aseo y ornato."
      Funciones_Compartidas:
        - "Educación y cultura."
        - "Salud primaria y medio ambiente."
        - "Asistencia social y jurídica."
        - "Capacitación y fomento productivo."
        - "Deporte, recreación y turismo."
        - "Vivienda y urbanización."
        - "Seguridad pública local."
    Rol_Alcalde:
      ID: GOBCL-MUNICIPAL-ALCALDE-01
      Rol: "Máxima autoridad municipal; dirección y administración de la municipalidad."
      Eleccion: "Voto directo cada 4 años, reelegible."
      Atribuciones_Claves:
        - "Representar judicial y extrajudicialmente a la municipalidad."
        - "Proponer y gestionar presupuesto municipal."
        - "Administrar bienes municipales y nacionales de uso público."
        - "Nombrar y remover funcionarios de confianza."
        - "Rendir cuenta pública anual."
    Rol_Concejo_Municipal:
      ID: GOBCL-MUNICIPAL-CONCEJO-01
      Rol: "Entidad normativa, resolutiva y fiscalizadora de la gestión municipal."
      Eleccion: "Voto directo cada 4 años."
      Atribuciones_Claves:
        - "Aprobar presupuesto municipal y PLADECO."
        - "Dictar ordenanzas comunales."
        - "Fiscalizar gestión del Alcalde."
        - "Aprobar concesiones y licitaciones relevantes."
    Participacion_Ciudadana_Local:
      ID: GOBCL-MUNICIPAL-PARTICIPACION-01
      Mecanismos:
        - "Consejo Comunal de Organizaciones de la Sociedad Civil (COSOC)."
        - "Plebiscitos comunales."
        - "Audiencias públicas."
        - "Ordenanza de participación ciudadana."
        - "Consejo Comunal de Seguridad Pública."

Parte_4_Organos_Autonomos_y_Control:
  ID: GOBCL-ORGANOS-AUTONOMOS-01
  Def: "Órganos creados por CPR o ley que no integran los poderes Legislativo, Ejecutivo o Judicial, ni dependen del Presidente."

  Contraloria_General_Republica:
    ID: GOBCL-ORGANOS-CGR-01
    Def: "Órgano superior de fiscalización de la Administración del Estado."
    Ref_Normativa:
      - Ref: GOBCL-NORM-CPR-01
        Detalle: "Art. 98."
    Funciones_Principales:
      - "Control de legalidad de actos de la Administración (toma de razón)."
      - "Fiscalizar ingreso e inversión de fondos públicos."
      - "Examinar y juzgar cuentas de quienes administran bienes públicos."
      - "Llevar la contabilidad general de la Nación."

  Banco_Central:
    ID: GOBCL-ORGANOS-BC-01
    Def: "Organismo autónomo, con patrimonio propio y carácter técnico."
    Obj_Principal: "Velar por estabilidad de la moneda y buen funcionamiento de pagos internos y externos."
    Atribuciones:
      - "Emisión de billetes y monedas."
      - "Regulación de dinero y crédito."
      - "Supervisión del sistema financiero (en coordinación con otros órganos)."

  Ministerio_Publico:
    ID: GOBCL-ORGANOS-MP-01
    Def: "Organismo autónomo y jerarquizado, fuera de los tres poderes del Estado."
    Ref_Normativa:
      - Ref: GOBCL-NORM-CPR-01
        Detalle: "Art. 83."
    Funciones_Principales:
      - "Dirigir investigación de delitos."
      - "Ejercer acción penal pública."
      - "Adoptar medidas de protección a víctimas y testigos."
    Prohibicion: "No puede ejercer funciones jurisdiccionales."

  Consejo_Defensa_Estado:
    ID: GOBCL-ORGANOS-CDE-01
    Def: "Organismo autónomo descentralizado, que se relaciona directamente con el Presidente."
    Mssn: "Representar y defender judicialmente los intereses del Estado."
    Rol: "Proteger patrimonio estatal y perseguir delitos contra el Estado."

Parte_5_Administracion_Financiera_Estado:
  ID: GOBCL-ADMIN-FINANCIERA-01
  Fnd: "Iniciativa exclusiva del Presidente en materia de presupuesto."
  Def: "Conjunto de procesos para obtener y aplicar recursos para fines del Estado."
  Ref_Normativa_Principal:
    - Ref: GOBCL-NORM-CPR-01
    - Ref: GOBCL-NORM-DL-1263-01
    - Ref: GOBCL-NORM-LEY-18575-01
    - Ref: GOBCL-NORM-LEY-20128-01

  Politica_Fiscal_y_Presupuesto:
    ID: GOBCL-ADMIN-FINANCIERA-POLITICA-FISCAL-01
    Regla_Balance_Estructural:
      Def: "Guiar la política fiscal con perspectiva de mediano plazo, independiente del ciclo económico."
      Principio: "Ahorrar en bonanza y gastar en recesión."
      Organo_Asesor: "Consejo Fiscal Asesor."
    Ciclo_Presupuestario:
      Def: "Ley anual que estima ingresos y autoriza gastos del Sector Público."
      Etapas:
        - "Formulación (liderada por DIPRES, envío al Congreso)."
        - "Discusión y aprobación (plazo de 60 días; Congreso no puede aumentar gasto)."
        - "Ejecución (tras promulgación y publicación)."
        - "Evaluación (uso de recursos del período)."

  Ingresos_y_Gastos_Publicos:
    ID: GOBCL-ADMIN-FINANCIERA-INGRESOS-GASTOS-01
    Fuentes_Ingresos_Principales:
      - "Impuestos (IVA, renta, específicos)."
      - "Transferencias corrientes (donaciones, aportes)."
      - "Rentas de la propiedad (dividendos, intereses)."
      - "Ingresos de operación (venta de bienes y servicios)."
      - "Endeudamiento."
    Tipos_Gasto:
      - "Gasto público para funcionamiento de instituciones."
      - "Gasto social (bienes y servicios públicos, subsidios, transferencias)."

  Compras_y_Contratacion_Publica:
    ID: GOBCL-ADMIN-FINANCIERA-COMPRAS-PUBLICAS-01
    Ref_Normativa:
      - Ref: GOBCL-NORM-LEY-19886-01
    Plataforma: "www.mercadopublico.cl."
    Regla_General: "Licitación pública."
    Excepciones:
      - "Licitación privada."
      - "Trato directo."
    Mecanismo_Eficiencia: "Convenio Marco."
    Principios_Rectores:
      - "Libre concurrencia."
      - "Igualdad de oferentes."
      - "Sujeción estricta a las bases."
      - "Transparencia y probidad."

  Transferencias_y_Subsidios:
    ID: GOBCL-ADMIN-FINANCIERA-TRANSFERENCIAS-SUBSIDIOS-01
    Def: "Herramientas de gasto social para integrar/proteger sectores vulnerables y fomentar actividades productivas."
    Transferencias:
      Def: "Subvenciones a personas jurídicas sin contraprestación recíproca."
    Subsidios:
      Def: "Transferencias de dinero, bienes o prestaciones para alcanzar metas sociales o productivas."
      Ejemplos:
        - "Subsidio habitacional (MINVU)."
        - "Subsidio familiar (MDSF)."
        - "Subsidio de cesantía."
    Publicidad_y_Registro:
      Ref_Normativa:
        - Ref: GOBCL-NORM-LEY-19862-01
      Req: "Registrar y dar publicidad a todas las transferencias."

Parte_6_Anexo_Caso_Estudio_Region_Nuble:
  ID: GOBCL-ANEXO-NUBLE-01
  Prop: "Ejemplificar desafíos de administración regional y brechas territoriales con datos concretos de la Región de Ñuble."
  Ref_Problema_Central: "PS-TERRITORIO-PLANIF-P02 (Segregación territorial subnacional)."

  Contexto_Socioeconomico:
    ID: GOBCL-NUBLE-CONTEXTO-SOCIOECONOMICO-01
    Indicadores_Claves:
      Pobreza:
        - "Pobreza por ingresos: 12.1% (vs 6.5% nacional)."
        - "Pobreza multidimensional: 15.5% (vs 16.9% nacional)."
      Ingresos:
        - "Ingreso promedio RSH: $386.917 (vs $468.619 nacional)."
        - "Brecha de género en ingresos: 30.6% (vs 29.4% nacional)."
      Mercado_Laboral:
        - "Participación laboral: 51.6% (vs 62% nacional)."
        - "Informalidad laboral: 34.3% (vs ~30% nacional)."
      Cuidados_y_Dependencia:
        - "Prevalencia de discapacidad en adultos: 22.9% (vs 17.6% nacional)."
        - "Dependencia funcional: 13.1% (vs 11.9% nacional)."
      Salud:
        - "Afiliación FONASA: 90.3%, la más alta del país."
      Educacion:
        - "Escolaridad promedio: 10.8 años (vs 11.7 nacional)."

  Oferta_Publica_e_Inversion:
    ID: GOBCL-NUBLE-CONTEXTO-OFERTA-INVERSION-01
    Oferta_Programatica:
      - "Programas vigentes 2023: 497; gasto componente > $1.1 billón."
      - "9.1% del gasto nacional en medio ambiente y energía se ejecuta en Ñuble."
    Inversion_Publica_SNI_2023:
      Proyectos_En_Ejecucion: "Proyectos en ejecución: 57."
      Costo_Total_Inversion: "Costo total de inversión: $717 mil millones (2.2% del total país)."
      Inversion_Per_Capita: "Inversión per cápita: $1.3 millones (vs $1.6 millones nacional)."
      Foco_Inversion:
        - "Salud: 42.5% del costo total, destacando nuevo complejo hospitalario."
        - "Educación/cultura: $0 en proyectos en ejecución 2023."
      Postulacion_Proyectos_Nuevos_2023:
        - "Proyectos postulados: 70."
        - "Con recomendación satisfactoria (RS): 38 (54%)."
