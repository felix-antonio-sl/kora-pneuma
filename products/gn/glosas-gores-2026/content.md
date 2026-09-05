---
urn: urn:gn:kb:glosas-gores-2026
nombre: glosas-gores-2026
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre glosas gores 2026; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml (sha256:9e705da57dc455abef1e7e2041e138e8d137332e0f91b1a33ac6699b24dd6435); URN KODA legado urn:gorenuble:presupuesto:glosas-gores-2026:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "Unknown"
creado: 2026-01-02
lang: es
tags: [gn, gore-os, koda, glosas, gores, "2026"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:presupuesto:glosas-gores-2026:1.0.0"
  federation:
    visibility: private
    license: "N/A"
  provenance:
    created_by: "FS"
    created_at: "2026-01-02"
    source: "/Users/felixsanhueza/Developer/gorenuble/staging/glosas gores 2026/glosas_gores_2026.md"
    transformed_by: "KODA-TRANSFORMER (GPT-5.2)"

ID: GLOSAS-GORES-2026-01
Version: 1.0.0
Status: Draft
Human-Creator: Unknown
Human-Editor: FS
Model-Collaborator: GPT-5.2
Creation-Date: 2026-01-02
Modification-Date: 2026-01-02
Source: "/Users/felixsanhueza/Developer/gorenuble/staging/glosas gores 2026/glosas_gores_2026.md"
Ctx: "Ley de Presupuestos Año 2026 - Partida: Financiamiento Gobiernos Regionales"

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

Purp: >-
  Transformación KODA de glosas y requerimientos de información de la Ley de Presupuestos Año 2026
  (Partida: Financiamiento Gobiernos Regionales).
Obj:
  - "FS=100%: preservar contenido normativo + estructura (tablas, numerales, listas)."
  - "Deduplicación: usar Ref para entidades recurrentes."
  - "Estructura RAG: secciones, actores, restricciones, montos, reporting."

Definitions:
  - ID: ACTOR-GORES
    Def: gobiernos regionales
  - ID: ENTITY-GORE
    Def: Gobierno Regional
  - ID: BODY-CONSEJO-REGIONAL
    Def: Consejo Regional
  - ID: BODY-CEMP
    Def: Comisión Especial Mixta de Presupuestos
  - ID: ORG-DIPRES
    Def: Dirección de Presupuestos
  - ID: ORG-SUBDERE
    Def: Subsecretaría de Desarrollo Regional y Administrativo
  - ID: ORG-MDSF
    Def: Ministerio de Desarrollo Social y Familia
  - ID: ORG-MTT
    Def: Ministerio de Transportes y Telecomunicaciones
  - ID: ORG-SUBINTERIOR
    Def: Subsecretaría del Interior
  - ID: LAW-DFL-1-19175
    Def: D.F.L N°1-19.175
  - ID: LAW-20378
    Def: "Ley N°20.378 (Fondo de Apoyo al Transporte Público y la Conectividad Regional)"
  - ID: LAW-18091
    Def: ley N°18.091
  - ID: LAW-20285
    Def: "Ley N°20.285 (acceso a la información pública)"
  - ID: SUBTITULO-24
    Def: Subtítulo 24
  - ID: ITEM-3303
    Def: Ítem 33.03
  - ID: RES-EX-33-2024-MCTCI
    Def: "Resolución Exenta N° 33, de 2024 (Ministerio de Ciencias, Tecnología, Conocimiento e Innovación)"

Law_Budget_2026:
  ID: LAW-PRESUP-2026-GORES
  Title: "LEY DE PRESUPUESTOS AÑO 2026"
  Partida: "Financiamiento Gobiernos Regionales"
  Units: "Miles de $"

  Economic_Classification_Incomes_Expenses:
    ID: TABLE-CLASIF-ECON-ING-GAS-01
    Table:
      Headers:
        - Sub-Título
        - Clasificación Económica
        - "Gobiernos Regionales (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16)"
      Rows:
        - [INGRESOS, "", "1.900.047.503"]
        - ["05", Transferencias Corrientes, "17.827.479"]
        - ["09", Aporte Fiscal, "1.124.303.237"]
        - ["13", Transferencias para Gastos de Capital, "757.916.787"]
        - [GASTOS, "", "1.900.047.503"]
        - ["24", Transferencias Corrientes, "128.872.343"]
        - ["33", Transferencias de Capital, "1.771.175.160"]

  Glosses:
    - ID: GLOSA-01-FUNCIONAMIENTO-REGIONAL
      Title: "01 Aplicable a Funcionamiento Regional"
      Actor:
        Ref: ACTOR-GORES
      Subtitulo_21_Gasto_en_Personal:
        - Req: >-
            No regirá la limitación establecida en el inciso segundo del artículo 10 del D.F.L N°29, de 2005,
            del Ministerio de Hacienda, respecto de los empleos a contrata, incluidos en las dotaciones máximas
            de personal de este programa.
        - Allow: >-
            El personal a contrata podrá desempeñar funciones de carácter directivo que se le asignen o deleguen,
            mediante resolución fundada del Jefe de Servicio.
        - Req: >-
            La resolución fundada del Jefe de Servicio deberá precisar las funciones delegadas.
        - Prohib: >-
            El personal a contrata no podrá exceder del 20% del total del personal a contrata.
        - Allow: >-
            El personal a honorarios podrá tener la calidad de Agente Público, para efectos de lo dispuesto en el
            Decreto Ley N°799, de 1974; para el desempeño de labores de fiscalización o certificación y hacer
            efectiva su responsabilidad administrativa, civil y penal por el desempeño de sus labores, de acuerdo
            con lo que se establezca en el respectivo convenio.
        - Req:
            Actor:
              Ref: ACTOR-GORES
            Text: >-
              Informar durante el primer trimestre del año 2026 a la Comisión de Hacienda de la Cámara de Diputados
              sobre las iniciativas legales y administrativas tendientes al traspaso de la calidad contractual de
              funcionarios de Gobiernos Regionales de Honorarios a Contrata y el fortalecimiento de los derechos
              laborales de estos funcionarios.
        - Req: >-
            No regirá la limitación establecida en el artículo 3° de la Ley N°20.035, en lo relativo a la estructura
            y funciones de los gobiernos regionales.
      Subtitulo_24_Transferencias_Corrientes:
        - Req: >-
            Mediante reglamento regional se determinarán los gastos de traslado y reembolso de los consejeros regionales,
            cuando correspondiese.
        - Req:
            Ctx:
              Ref: SUBTITULO-24
            Text: >-
              Respecto del gasto en cometidos al extranjero de los consejeros regionales se deberá considerar como máximo
              el 10% del gasto del Subtítulo 24 e incorporarlo en las glosas correspondientes en la resolución de
              distribución inicial.
        - Allow:
            Actor:
              Ref: ENTITY-GORE
            Text: >-
              La dotación de vehículos del Gobierno Regional podrá utilizarse en el traslado de los consejeros regionales,
              en cumplimiento de funciones encomendadas por el Consejo Regional.

    - ID: GLOSA-02-INVERSION-REGIONAL
      Title: "02 Aplicable a Inversión Regional"
      Allocation_By_Region:
        ID: TABLE-ASIGNACION-INVERSION-REGIONAL-01
        Table:
          Headers:
            - Gobierno Regional
            - Fondo Nacional de Desarrollo Regional
            - Fondo de Apoyo al Transporte Público y la Conectividad Regional
            - Fondo de Equidad Interregional
            - Fondo para la Productividad y el Desarrollo
            - "Tesoro Público Ley N° 21.210, Modernización Tributaria"
            - Subsecretaría de la Cultura y las Artes
            - "Tesoro Público Ley N° 19.275, Fondo de Desarrollo de Magallanes"
            - "Tesoro Público Ley N° 19.143, Patentes Mineras"
            - "Tesoro Público Ley N° 19.657, Patentes Geotérmicas"
            - "Tesoro Público Art. 129 bis 19 Ley N° 20.017, Código de Aguas"
            - "Tesoro Público D.L. N°430, de 1992 (E.F. y T.), Patentes de Acuicultura"
            - Fondo de Inversión y Reconversión Regional
            - Total
          Rows:
            - ["Tarapacá", "35.359.987", "16.045.986", "0", "10.955.743", "2.639.730", "778.732", "0", "7.523.467", "0", "112.589", "9.737", "2.089.574", "75.515.545"]
            - ["Antofagasta", "44.173.366", "20.880.832", "502.233", "14.256.838", "3.435.113", "1.381.566", "0", "24.188.373", "254.274", "1.128.094", "5.360", "8.668.717", "118.874.766"]
            - ["Atacama", "34.662.339", "16.149.839", "9.064.842", "11.026.651", "2.656.815", "969.124", "0", "14.201.202", "0", "999.449", "34.313", "1.922.722", "91.687.296"]
            - ["Coquimbo", "43.820.007", "19.975.688", "5.982.724", "13.638.832", "3.286.207", "1.009.479", "0", "7.202.479", "0", "758.483", "40.860", "1.926.581", "97.641.340"]
            - ["Valparaíso", "48.891.345", "22.325.871", "7.142.942", "15.243.470", "3.672.836", "1.145.019", "0", "2.789.778", "0", "656.680", "193", "1.966.521", "103.834.655"]
            - ["O'Higgins", "41.527.239", "19.123.418", "7.248.039", "13.056.926", "3.146.000", "1.050.906", "0", "1.119.486", "0", "1.202.029", "116.838", "1.920.840", "89.511.721"]
            - ["Maule", "53.077.751", "24.216.983", "14.506.251", "16.534.668", "3.983.944", "1.232.914", "0", "743.014", "0", "2.985.849", "32", "1.626.617", "118.908.023"]
            - ["Biobío", "55.752.999", "25.391.728", "10.192.165", "17.336.750", "4.177.202", "1.272.645", "0", "639.005", "0", "1.469.115", "14.441", "1.705.522", "117.951.572"]
            - ["Araucanía", "66.258.806", "30.919.504", "50.672.259", "21.110.958", "5.086.578", "1.875.996", "0", "147.793", "0", "2.126.409", "3.258", "2.076.814", "180.278.375"]
            - ["Los Lagos", "45.977.501", "21.235.317", "20.703.621", "14.498.871", "3.493.429", "1.194.176", "0", "255.307", "0", "2.268.623", "3.521.920", "1.426.343", "114.575.108"]
            - ["Aysén", "31.592.880", "14.644.138", "18.091.050", "9.998.601", "2.409.112", "846.314", "0", "573.189", "0", "1.208.534", "1.519.285", "983.623", "81.866.726"]
            - ["Magallanes", "32.703.469", "15.156.260", "7.355.822", "10.348.263", "2.493.361", "757.786", "11.690.896", "225.520", "0", "237.602", "671.521", "1.018.022", "82.658.522"]
            - ["Metropolitana", "99.499.728", "44.794.655", "1.262.043", "30.584.518", "7.369.184", "2.016.392", "0", "3.066.774", "0", "4.579.804", "153.288", "3.412.689", "196.739.075"]
            - ["Los Ríos", "25.727.491", "12.193.520", "24.845.561", "8.325.389", "2.005.960", "820.380", "0", "150.945", "0", "2.962.972", "47.407", "819.019", "77.898.644"]
            - ["Arica y Parinacota", "26.094.386", "11.882.961", "6.269.416", "8.113.349", "1.954.870", "595.047", "0", "1.097.872", "0", "51.491", "4.976", "798.160", "56.862.528"]
            - ["Ñuble", "41.562.476", "18.790.488", "6.353.223", "12.829.611", "3.091.230", "881.003", "0", "299.326", "0", "682.846", "0", "1.262.128", "85.752.331"]
            - ["Total", "726.681.770", "333.727.188", "190.192.191", "227.859.438", "54.901.571", "17.827.479", "11.690.896", "64.223.530", "254.274", "23.430.569", "6.143.429", "33.623.892", "1.690.556.227"]

    - ID: GLOSA-03-RESTRICCIONES-FINANCIAMIENTO
      Title: "03 Restricciones de Financiamiento"
      Prohibitions:
        - Prohib: >-
            Los recursos de los presupuestos de inversión regional no podrán financiar préstamos, gastos en personal,
            o gastos en bienes y servicios de consumo de las entidades receptoras.
        - Prohib: >-
            No podrán destinarse para constituir, efectuar aportes o comprar sociedades o empresas.

    - ID: GLOSA-04-TRASPASO-RECURSOS
      Title: "04 Traspaso de Recursos"
      Allowances:
        - Allow: >-
            Se podrán traspasar recursos desde cualquier Subtítulo e Ítem del presupuesto de inversión del Gobierno Regional
            respectivo a los Subtítulos 24, 26, 29, 31, 32.06, 33 y 34.07.
        - Allow:
            Actor:
              Ref: ACTOR-GORES
            Ctx:
              Ref: LAW-18091
            Text: >-
              Podrán realizar convenios de mandato con los municipios de acuerdo con el artículo 16 de la ley N°18.091,
              para el financiamiento de estudios definidos en el subtítulo 22 ítem 11, del Decreto de Hacienda N° 854 del 2004,
              sobre clasificaciones presupuestarias.

    - ID: GLOSA-05-TRANSFERENCIAS-UNIVERSIDADES
      Title: "05 Transferencias a Universidades"
      Provisions:
        - Ctx: >-
            Transferencias a universidades del artículo 3° del D.F.L. N° 2 (Estatuto Orgánico CRUCH) y aquellas que se han
            adscrito al Consejo conforme con el artículo 6 de la ley N° 21.091 (Educación Superior) y normativa vigente.
        - Req: >-
            Las transferencias de recursos desde los gobiernos regionales solo podrán ser ejecutadas y utilizadas para fines
            dentro del ámbito de competencia del establecimiento de educación superior que se los adjudicó.
        - Rec: >-
            La ejecución de las acciones por las cuales se efectúa la transferencia se hará preferentemente a las universidades
            con sede en la región respectiva.
        - Req: >-
            La ejecución deberá llevarse a cabo de manera íntegra por parte de la propia universidad.
        - Allow: >-
            Estas transferencias se podrán exceptuar del mecanismo de concursabilidad establecido en el articulado de la presente ley.

    - ID: GLOSA-06-OFERTA-PROGRAMATICA-INVERSION-S24
      Title: "06 Oferta Programática e Inversión Regional (Subtítulo 24)"
      Actor:
        Ref: ACTOR-GORES
      Governance:
        - Req:
            Ctx:
              Ref: SUBTITULO-24
            Text: >-
              Las transferencias corrientes del presupuesto de inversión regional se regirán por las siguientes disposiciones.
        - Req:
            Actor:
              Ref: ACTOR-GORES
            Text: >-
              La oferta programática que ejecutan directamente estará sujeta al Sistema de Evaluación y Monitoreo del
              Ministerio de Desarrollo Social y Familia y de la Dirección de Presupuestos.
            Src:
              - Ref: ORG-MDSF
              - Ref: ORG-DIPRES
      Exemptions_From_Ex_Ante_Evaluation:
        - Ex: "a) los programas que hayan iniciado su ejecución en años anteriores."
        - Ex: "b) las subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%."
        - Ex: "c) las transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro."
        - Ex: "d) las ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales, en coordinación con el Ministerio del Interior."
      Principles_And_Execution:
        - Req:
            Actor:
              Ref: ENTITY-GORE
            Text: >-
              La oferta programática de cada Gobierno Regional deberá respetar los principios de coherencia con las políticas públicas nacionales,
              coordinación, unidad de acción, eficiencia y eficacia, evitando la duplicidad o interferencia de funciones con otros órganos de la
              Administración del Estado.
        - Allow: >-
            Estos recursos podrán ser ejecutados por instituciones privadas sin fines de lucro, municipalidades, otras entidades públicas y organismos
            del gobierno central.
        - Req: >-
            La asignación de estos recursos se regirá por las normas contenidas en el articulado de esta ley.
        - Allow:
            Actor:
              Ref: ENTITY-GORE
            Text: >-
              Se podrá destinar hasta un 5% del monto total de la transferencia a gastos que demande la administración de las iniciativas,
              tales como gastos en personal, gastos en bienes y servicios de consumo y en adquisición de activos no financieros,
              asociados con la ejecución del programa.
        - Req: >-
            El personal contratado a honorarios con cargo al 5% señalado tendrá la calidad de agente público.
        - Allow: >-
            Con cargo a esta transferencia se podrá contratar en la entidad pública receptora a personal a honorarios cuyo vínculo cesará de pleno
            derecho una vez finalizado el convenio de transferencia que sirvió de fundamento a su contratación.
        - Prohib: >-
            Lo anterior no podrá ser superior al 5% del total de la transferencia recibida.
        - Req:
            Ctx:
              Ref: LAW-DFL-1-19175
            Text: >-
              La oferta programática deberá regirse dentro de los ámbitos de competencia del D.F.L N°1-19.175.
      Additional_Offer_Outside_Competence:
        Ctx:
          Ref: LAW-DFL-1-19175
        Allow: >-
          Adicionalmente, los gobiernos regionales podrán ejecutar la siguiente oferta programática no considerada en los ámbitos de competencia.
        Categories:
          - ID: CAT-EMERGENCIA
            Title: Emergencia
            Allow:
              - "a) Iniciativas de prevención y mitigación de incendios forestales."
              - "b) Labores preventivas preparatorias para eventos climatológicos."
              - "c) Ejecutar y/o financiar iniciativas asociadas a las fases de mitigación y preparación en la gestión del riesgo de desastres, definidas en la Ley N°21.364, especialmente aquellas que tiendan a atenuar los efectos del déficit hídrico, la inaccesibilidad de agua y dar continuidad a los servicios de agua potable rural."
              - "d) Gastos en sanitización y calefacción de espacios públicos y/o privados, ante catástrofes y emergencias definidas por la autoridad correspondiente."
              - "e) Gasto en las etapas de ayudas tempranas y reconstrucción, previa coordinación con la Subsecretaría del Interior."
              - "f) Demolición de infraestructura en mal estado que represente riesgo de derrumbe; deberá ser certificado por la respectiva municipalidad."
            Reporting:
              Frequency: Semestral
              Req:
                Actor:
                  Ref: ACTOR-GORES
                Recipient:
                  Ref: BODY-CEMP
                Items:
                  - "De las iniciativas en materia de prevención y mitigación de incendios forestales, en particular de las que se desarrollen con la comunidad organizada y redes de prevención."
                  - "De los programas de desarrollo y uso de tecnologías en materias de prevención, y monitoreo y soporte en el combate de emergencias en las regiones y sus provincias."
                  - "De los recursos destinados a la rehabilitación y recuperación que sean destinados post emergencia, en las regiones y sus provincias."
          - ID: CAT-SEGURIDAD-PUBLICA
            Title: Seguridad Pública
            Allow:
              - Iniciativas de prevención y seguridad ciudadana.
          - ID: CAT-SALUD
            Title: Salud
            Allow:
              - "a) Establecimiento de Planes de resolución de lista de espera en coordinación con el Ministerio de Salud, con el objeto de fortalecer la capacidad resolutiva de la red asistencial pública, aumentar las atenciones de salud otorgadas y reducir los tiempos de espera de los pacientes."
              - "b) Programas de cuidado de personas con discapacidad en centros regionales de rehabilitación, a cargo de instituciones privadas que ejecutan políticas públicas."
          - ID: CAT-CUIDADOS
            Title: Cuidados
            Allow:
              - "a) Atención de adultos mayores e integración y promoción del envejecimiento activo, previa coordinación con el Servicio Nacional del Adulto Mayor."
              - "b) Funcionamiento de condominios de viviendas tuteladas del Servicio Nacional del Adulto Mayor."
              - "c) Funcionamiento de establecimientos de larga estadía para adultos mayores."
              - "d) Actividades de auxilio a personas en situación de calle de manera extraordinaria en coordinación con el Ministerio de Desarrollo Social y Familia."
              - "e) Distribución de medicamentos a domicilio a adultos mayores y enfermos crónicos, en coordinación con el Servicio de Salud respectivo."
          - ID: CAT-CLIMA-RESIDUOS
            Title: Cambio Climático y Gestión de Residuos
            Allow:
              - "a) Protección del medioambiente y educación ambiental."
              - "b) Mantención de parques, áreas verdes y/o jardines botánicos."
              - "c) Operación de instalaciones para el tratamiento adecuado de los residuos sólidos domiciliarios e iniciativas de reciclaje y valorización de residuos; se podrán financiar subsidios a las municipalidades para el servicio de disposición final de residuos sólidos domiciliarios; parámetros y características técnicas según Resolución N° 09, de fecha 10 de marzo de 2025 de SUBDERE y sus modificaciones; excepcionalmente, continuidad subsidios 2025 según Resolución N°09 del 2025 de SUBDERE."
              - "d) Iniciativas de adopción, rescate, atención y tratamiento veterinario, y de gestión de residuos de animales."
          - ID: CAT-ENERGIA-TRANSPORTE-TELECOM
            Title: Energía, Transporte y Telecomunicaciones
            Allow:
              - "a) Funcionamiento y continuidad de servicio de los sistemas de autogeneración de energía, reconocidos por la Subsecretaría de Energía."
              - "b) Operación, mantención, renovación y administración de servicios y bienes destinados a conectividad a internet y equipos de radiocomunicación."
              - "c) Subsidios entregados en el marco de la Ley N°20.378 (Fondo de Apoyo al Transporte Público y la Conectividad Regional)."
              - "d) Servicio de Transporte Escolar Rural."
          - ID: CAT-GESTION-HIDRICA
            Title: Gestión Hídrica
            Allow:
              - "a) Funcionamiento, mantención y reparación de sistemas de agua potable y sanitarios rurales y/o sistemas de desalinización de aguas."
              - "b) Operación de alcantarillado."
          - ID: CAT-ASISTENCIA-TECNICA
            Title: Asistencia Técnica
            Allow:
              - Programas destinados a financiar asistencia técnica a municipalidades para fortalecer su cartera de proyectos.

    - ID: GLOSA-07-S24-CONCURSO-VINCULACION-COMUNIDAD-8
      Title: "07 Aplicable al Subtítulo 24 de los presupuestos de inversión de los gobiernos regionales"
      Actor:
        Ref: ACTOR-GORES
      Allowances:
        - Allow: >-
            En las transferencias corrientes se podrá financiar el Concurso de Vinculación con la Comunidad 8%.
        - Allow: >-
            Podrán destinar hasta un 8% del total de los recursos del presupuesto de inversión regional para subvencionar las siguientes actividades:
        - Allow_List:
            - "a) deportivas y del programa Elige Vivir Sano,"
            - "b) de seguridad ciudadana,"
            - "c) de participación de niños, niñas, adolescentes y jóvenes de acuerdo a lo establecido en el artículo N°6, letra p) de la Ley N°21.302,"
            - "d) de carácter social, incluyendo programas y actividades para la atención de personas discapacitadas con dependencia severa, y de prevención y rehabilitación de drogas,"
            - "e) de atención de adultos mayores e integración y promoción del envejecimiento activo,"
            - "f) de protección del medioambiente y de educación ambiental,"
            - "g) asociadas con adopción, rescate, atención y tratamiento veterinario, y gestión de residuos de animales,"
            - "h) de funcionamiento de establecimientos de larga estadía para adultos mayores, residencias familiares para niños, niñas, adolescentes y/o jóvenes del Servicio Nacional de Protección Especializada a la Niñez y Adolescencia, Centro de Internación Provisoria e Internación en régimen cerrado y Libertad Asistida Especial con Internación Parcial, del Servicio de Reinserción Social Juvenil,"
            - "i) funcionamiento de teatros municipales o regionales y/o monumentos históricos con atención a público, que operen en la región,"
            - "j) culturales y patrimoniales."
        - Allow: >-
            Estas actividades podrán ser ejecutadas por municipalidades, otras entidades públicas, instituciones privadas sin fines de lucro,
            organizaciones de la sociedad civil y organizaciones comunitarias sin fines de lucro.
        - Req: >-
            La asignación de estos recursos deberá cumplir con lo dispuesto en el articulado de esta ley en lo que corresponda.
        - Allow:
            Preconditions:
              - "Previo acuerdo del Consejo Regional."
            Text: >-
              Se podrá asignar hasta un 10% de los recursos del Concurso de Vinculación con la Comunidad 8% para financiar,
              mediante asignaciones directas, actividades asociadas con casos emblemáticos, excepcionales y emergentes,
              como por ejemplo deportistas destacados.
        - Req: >-
            Lo anterior sujeto a lo dispuesto en la Resolución N°72 de fecha 08.01.2025 de la Dirección de Presupuestos y sus modificaciones,
            que imparte instrucciones sobre asignación directa en concurso de vinculación con la comunidad.

    - ID: GLOSA-08-INFORMACION-CORPORACIONES
      Title: "08 Información sobre Corporaciones"
      Actor:
        Ref: ACTOR-GORES
      Reporting:
        - Req:
            Recipient:
              Ref: ORG-DIPRES
            Timing: "A más tardar al término del primer trimestre"
            Channels:
              - "Publicar en la página web de la corporación."
              - "Publicar en la página web del respectivo Gobierno Regional."
            Items:
              - "Nombre o razón social de la corporación."
              - "Misión, objetivos estratégicos y productos."
              - "Composición del directorio."
              - "Organigrama."
              - "Instituciones que participan de su financiamiento (Gobierno Regional y otras entidades, públicas y privadas)."
              - "Vínculo de los objetivos de la corporación con los objetivos del Gobierno Regional."
              - "Planificación anual (incluyendo objetivos del periodo, principales resultados esperados y actividades relevantes necesarias para alcanzarlos)."
        - Req:
            Timing: "Trimestral; dentro de los 30 días siguientes al término de cada trimestre"
            Items:
              - "Número de profesionales de la corporación, remuneración asociada y perfil profesional."
              - "Concursos para contratación de personal realizados en el periodo (perfiles de cargos postulados y resultados)."
              - "Recursos transferidos por el Gobierno Regional y ejecutados por la corporación en el periodo y acumulados en el año."
              - "Indicadores de gestión (avance físico y financiero de iniciativas encomendadas y financiadas por el Gobierno Regional)."
        - Req:
            Actor: "Corporaciones y fundaciones constituidas con participación del Gobierno Regional"
            Items:
              - "Dar cuenta pública anual de su gestión."
              - "Mantener publicados sus estados financieros en su página web y en la del Gobierno Regional."
              - "Regirse por la Ley N° 20.285 sobre acceso a la información pública, en lo aplicable."
            Ctx:
              Ref: LAW-20285

    - ID: GLOSA-09-S29-ACTIVOS-NO-FINANCIEROS
      Title: "09 Aplica a Subtítulo 29 (presupuesto de inversión regional)"
      Actor:
        Ref: ACTOR-GORES
      Allowances_And_Requirements:
        - Allow: >-
            Financiar la adquisición de activos no financieros de reposición al Gobierno Central y a otras instituciones públicas.
        - Allow: >-
            Excepcionalmente, comprar nuevos activos no financieros incorporando un certificado de disponibilidad presupuestaria
            para los gastos recurrentes que generen dichos activos.
        - Req: >-
            El certificado deberá ser emitido por el Ministerio o la Secretaría respectiva.
        - Allow:
            Ctx:
              Ref: LAW-18091
            Text: >-
              Realizar convenios de mandato con los receptores públicos de acuerdo con el artículo 16 de la ley N°18.091.
        - Req: >-
            Las compras para Fuerzas de Orden y Seguridad Pública deberán contar con certificado de pertinencia de la respectiva contratación,
            donación o transferencia de recursos con los planes estratégicos de desarrollo policial; emitido por el Ministerio de Seguridad Pública,
            a solicitud de las Fuerzas de Orden y Seguridad Pública.
        - Allow: >-
            Financiar adquisición de activos no financieros a cuerpos de bomberos regionales; deberán contar con certificado de pertinencia técnica
            emitido por la Junta Nacional de Bomberos de Chile.
        - Allow: >-
            Financiar compra de terrenos; adquisiciones en coordinación con el SERVIU de la región respectiva, cuando corresponda.

    - ID: GLOSA-10-S31-INVERSION-PUBLICA
      Title: "10 Aplica a Subtítulo 31 (presupuesto de inversión)"
      Actor:
        Ref: ACTOR-GORES
      Governance:
        - Req:
            Ctx:
              Ref: LAW-DFL-1-19175
            Text: "La inversión pública deberá regirse dentro de los ámbitos de competencia del D.F.L. N°1-19.175."
        - Allow: "Adicionalmente, podrán ejecutarse las siguientes iniciativas de inversión pública:"
      Allowed_Initiatives:
        - "a) Construcción, conservación y mejoramiento de infraestructura pública en coordinación con el Ministerio sectorial respectivo."
        - "b) Iniciativas de inversión en transporte en coordinación con el Ministerio de Transportes y Telecomunicaciones, en el marco de la Ley N°20.378 (Fondo de Apoyo al Transporte Público y la Conectividad Regional)."
        - "c) Iniciativas de inversión de interés social en las áreas de electrificación, gas, generación de energía, conectividad digital, telefonía celular y comunicaciones, incluyendo las conexiones domiciliarias."
        - "d) Iniciativas de inversión en agua potable y alcantarillado."
        - "e) Proyectos sanitarios correspondientes a áreas de concesión de empresas del sector público."
        - "f) Iniciativas de inversión en Agua Potable Rural y obras para mitigación y reparación del daño producido por cambio climático a pequeños productores agrícolas y habitantes rurales."
        - "g) Excepcionalmente, durante el año 2026, respecto del diseño y la ejecución de proyectos de saneamiento rural o proyectos ubicados en territorios insulares (agua potable, alcantarillado, disposición y tratamiento de aguas servidas, entre otros), el Gobierno Regional podrá, mediante resolución fundada, determinar como Unidad Técnica a la empresa, pública o privada, que opere en la región en el marco de las funciones indicadas en la Ley N°20.998 de 2017 (Servicios Sanitarios Rurales). La Dirección de Obras Hidráulicas y la Subdirección de Servicios Sanitarios Rurales deberán informar a los Gobiernos Regionales y la Contraloría Regional respectiva, a más tardar los días 20 de enero y 30 de junio, las regiones que no disponen de especialistas en los proyectos mencionados."
        - "h) Proyectos de conservación de huellas y caminos vecinales privados de uso público, a través de administración directa, por contrato de obra pública o compra de servicio; previo compromiso formal de la transferencia de la faja respectiva; y requerirá previamente el visto bueno de la Dirección Regional de Vialidad respectiva."
      Oversight:
        - Req:
            Src:
              - Ref: ORG-MDSF
              - Ref: ORG-DIPRES
            Text: "La inversión estará sujeta al Sistema Nacional de Inversiones por parte del Ministerio de Desarrollo Social y Familia y de la Dirección de Presupuestos."
        - Req: >-
            En el ejercicio de esta facultad, cada Gobierno Regional deberá respetar los principios de coherencia con las políticas públicas nacionales,
            coordinación, unidad de acción, eficiencia y eficacia, evitando la duplicidad o interferencia de funciones con otros órganos de la
            Administración del Estado.
        - Allow: >-
            Las identificaciones presupuestarias de las iniciativas contratadas en años anteriores en ejecución y aquellas creadas en el mismo año,
            no requerirán una nueva aprobación del Consejo Regional, si los montos totales o resultantes son iguales o menores al 10% de los costos
            totales ya aprobados por el Consejo Regional, reajustados a la moneda del año en curso.
        - Req: "El personal contratado a honorarios para ejecución de proyectos tendrá la calidad de agente público."

    - ID: GLOSA-11-S33-TRANSFERENCIAS-CAPITAL
      Title: "11 Transferencias de Capital (Subtítulo 33)"
      Actor:
        Ref: ACTOR-GORES
      Scope:
        - "Aplica al subtítulo 33 del presupuesto de inversión de los gobiernos regionales."
      Governance:
        - Req:
            Ctx:
              Ref: LAW-DFL-1-19175
            Text: "Las transferencias de capital deberán regirse por los ámbitos de competencia del D.F.L N°1-19.175."
        - Allow: "Adicionalmente, podrán financiarse las siguientes iniciativas:"
      Allowed_Initiatives:
        - "a) Proyectos de tipología PMU/PMB en coordinación con la Subsecretaría de Desarrollo Regional y Administrativo."
        - "b) Iniciativas de infraestructura social o deportiva en inmuebles: bienes comunes de comunidades agrícolas; condominios de viviendas sociales; conformados según leyes N°15.020 y N°16.640 (Reforma Agraria) y N°19.253 (Ley Indígena); otros inmuebles de similar calidad jurídica; e inmuebles fiscales en tuición de organizaciones privadas sin fines de lucro con fines sociales."
        - "c) Iniciativas de construcción, habilitación, conservación y mejoramiento de caminos comunitarios ubicados en territorios regidos por la Ley N°19.253 o de propiedad de comunidades agrícolas."
        - "d) Intervenciones en fachadas de inmuebles de propiedad privada con protección patrimonial."
        - "e) Estudios de factibilidad e iniciativas para mejoramiento de eficiencia del sistema portuario de territorios insulares."
        - "f) Iniciativas de protección y puesta en valor de inmuebles y bienes muebles declarados Monumento Nacional, Inmueble de Conservación Histórica, o ubicados en zona de conservación histórica según plano regulador; sitios de patrimonio mundial UNESCO o Lista Tentativa UNESCO; incluyendo ejecución conjunta con sector privado."
        - "g) Subsidios a empresas públicas o privadas para proyectos de inversión de interés social en electrificación, gas, generación de energía, telefonía celular y comunicaciones; evaluación como iniciativa de inversión según metodología de MDSF."
        - "h) Iniciativas de inversión en establecimientos educacionales, incluidos jardines infantiles, con objetivo de obtención y mantención del Reconocimiento Oficial del Ministerio de Educación."
        - "i) Subsidio para habilitación de infraestructura de centros regionales de tratamiento y rehabilitación de personas discapacitadas."
        - "j) Subsidios para mantención y reparación de sistemas y/o programas de Agua Potable Rural (APR) y sanitarios rurales y/o sistemas de desalinización de aguas; transferencia mediante resolución fundada del Gobernador Regional (produce efectos sin esperar total tramitación); requiere pronunciamiento técnico favorable de la Subdirección de Servicios Sanitarios Rurales."
        - "k) Subsidio para habilitación de establecimientos de larga estadía para adultos mayores."
      Execution_And_Controls:
        - Allow: >-
            Estos recursos podrán ser ejecutados por instituciones privadas sin fines de lucro, otras entidades públicas y organismos del gobierno central.
        - Req: >-
            La asignación de estos recursos se regirá por el articulado de esta ley.
        - Allow: >-
            Podrán efectuarse transferencias de recursos a municipalidades y a las respectivas empresas sanitarias de la región para financiar:
            monitoreo, mantenciones, diseño de soluciones y trabajos preventivos ante filtraciones de redes de agua potable y alcantarillado de viviendas
            unifamiliares, conjuntos habitacionales de interés público, infraestructuras públicas y otros usos de suelo afectados; previa visación del
            órgano competente de la región.
        - Allow: >-
            Con estos recursos se podrá también financiar a las entidades señaladas, la pavimentación de sectores en que hayan efectuado recambio de redes
            de agua potable y alcantarillado.
        - Req: >-
            Para proyectos de Construcción de Infraestructura Sanitaria financiados por los Gobiernos Regionales regirá el límite de costo del artículo 8°
            del Decreto Supremo N° 829 de 1998 del Ministerio del Interior y sus modificaciones.
        - Req: >-
            Las entidades receptoras deberán rendir cuenta de su utilización al Gobierno Regional y, cuando corresponda, a la Contraloría General de la
            República.
        - Req: >-
            Los recursos transferidos se regirán por la normativa de la institución receptora y en los convenios respectivos se establecerán los
            procedimientos y condiciones bajo los cuales se efectuará la aplicación de los recursos que se transfieren.
      Transport_Connectivity_Fund:
        - Req:
            Ctx:
              Ref: ITEM-3303
            Text: >-
              Al momento de efectuar la distribución inicial del presupuesto de inversión regional, crear una asignación de provisión sin distribuir para
              el Fondo de Apoyo al Transporte y la Conectividad Regional dentro del Ítem 33.03.
        - Allow: >-
            En el transcurso del año presupuestario, reasignar desde esta provisión para financiamiento de iniciativas elegibles para este Fondo, a los
            subtítulos 24, 29, 31 y 33, respectivamente.
        - Allow: >-
            En la resolución de apertura, crear asignaciones de arrastres que se financien con estos fondos.
        - Allow: >-
            Según letra b) del numeral 1 del artículo 4° transitorio de la ley N°20.378 y sus modificaciones, financiar inversiones complementarias de
            infraestructura (en cualquiera de sus etapas) que consideren obras de tipologías de dicha letra (ej.: construcción, mejoramiento, conservación
            y/o reposición de obras viales y/o urbanas; iniciativas relacionadas con seguridad vial).
        - Req: >-
            Al menos el 50% de los recursos del Fondo de Apoyo al Transporte y la Conectividad Regional se destinarán al financiamiento de iniciativas
            regionales de transporte público mayor y menor.
        - Req:
            Recipient:
              - "Comisión de Obras Públicas, Transportes y Telecomunicaciones de la Cámara de Diputados"
              - Ref: BODY-CEMP
            Text: "Se deberá informar sobre el destino de los fondos restantes."
        - Req: >-
            Contemplar, con cargo a los recursos del Fondo de Apoyo al Transporte Público y la Conectividad Regional, los montos necesarios para financiar
            compromisos, obligaciones y efectos derivados de Convenios suscritos con el Ministerio de Transportes y Telecomunicaciones, proyectados más allá
            del período de vigencia, previa evaluación entre ambas instituciones.
        - Req: >-
            Lo anterior deberá reflejarse en la programación presupuestaria regional, para garantizar continuidad de acciones y sostenibilidad de
            iniciativas de conectividad y transporte público regional.
        - Allow: >-
            Las identificaciones presupuestarias de iniciativas contratadas en años anteriores en ejecución y aquellas creadas en el mismo año no
            requerirán nueva aprobación del Consejo Regional, si los montos totales o resultantes son iguales o menores al 10% de los costos totales ya
            aprobados por el Consejo Regional, reajustados a la moneda del año en curso.
        - Req: "El personal contratado a honorarios para ejecución de proyectos y/o programas tendrá la calidad de agente público."
      FRIL:
        - Allow: >-
            Las transferencias de capital del presupuesto de inversión podrán financiar proyectos de municipalidades asociados al Fondo Regional de Iniciativa
            Local (FRIL).
        - Req: >-
            Los proyectos deberán contar con informe favorable del Ministerio de Desarrollo Social y Familia y destinarse a ejecutar, mantener o conservar
            infraestructura pública.
        - Allow: >-
            Mediante resolución, aprobar instructivos o bases que establezcan metodología de distribución de recursos entre comunas, procedimientos de
            ejecución, entrega de recursos, rendición de gasto al Gobierno Regional y otros que permitan mejor utilización de recursos FRIL, siguiendo los
            lineamientos de la Guía Operativa del FRIL publicada por SUBDERE contenida en la Resolución Exenta N°15.051 del 29 de diciembre de 2023.
        - Req: >-
            Una vez aprobados los montos para cada municipio, el compromiso de financiamiento será informado por el Gobierno Regional mediante oficio al
            municipio respectivo.
        - Allow: >-
            Proyectos ejecutados con recursos transferidos a municipios con costo total por proyecto inferior a 5000 UTM (valorizadas al 1 de enero del
            ejercicio vigente) no requerirán informe favorable del Ministerio de Desarrollo Social y Familia.
        - Req: >-
            Sin perjuicio de lo anterior, deberá ingresarse al Sistema Nacional de Inversiones la información necesaria, según Oficio Ordinario N°2 del
            26 de enero de 2024 e instructivo asociado, del Ministerio de Hacienda y del Ministerio de Desarrollo Social y Familia.
      Regional_Productivity_Development_Fund:
        - Req: >-
            Los recursos con cargo al Fondo Regional para la Productividad y el Desarrollo se destinarán a fines del inciso segundo del artículo 13 de la
            ley N° 21.591, el Decreto N°1699 de fecha 6 de diciembre de 2025 del Ministerio de Hacienda, la Resolución Exenta N° 33, de 2024 del Ministerio
            de Ciencias, Tecnología, Conocimiento e Innovación y sus modificaciones, y la Resolución Exenta N°08, de 2025 de la Subsecretaría de Economía y
            Empresas de Menor Tamaño y sus modificaciones.
        - Req:
            Ctx:
              Ref: ITEM-3303
            Text: >-
              Crear una asignación de provisión sin distribuir para este Fondo dentro del Ítem 33.03; durante el año reasignar desde la provisión para
              financiamiento de iniciativas con cargo al Fondo; en resolución de apertura, crear asignaciones de arrastres financiadas con estos fondos.
        - Allow:
            Ctx:
              Ref: RES-EX-33-2024-MCTCI
            Text: >-
              Transferir directamente recursos a iniciativas ejecutadas en la región, seleccionadas por concurso CORFO o ANID, cuyas instituciones
              ejecutoras estén incluidas en la Resolución Exenta N° 33, de 2024 (MCTCI) y sus modificaciones.
        - Allow: >-
            Efectuar creaciones y modificaciones de asignaciones para pago de compromisos de arrastre de iniciativas ejecutadas por instituciones elegibles
            del Fondo de Innovación y Competitividad.
        - Allow: >-
            Participar del financiamiento de iniciativas de Programas de Desarrollo Productivo Sostenible del Ministerio de Economía, Fomento y Turismo,
            e iniciativas del Programa de Financiamiento Estructural I+D+i Universitario del Ministerio de Ciencia, Tecnología, Conocimiento e Innovación.
      Emergency_Transfers_To_Interior:
        - Allow: >-
            Traspasar hasta un 3% del presupuesto de inversión aprobado por el Congreso Nacional de cada Gobierno Regional, a requerimiento de la
            Subsecretaría del Interior, a asignaciones 24.03.002 y/o 33.03.001 del presupuesto de dicha Subsecretaría para enfrentar situaciones de
            emergencia.
        - Req:
            Actor:
              Ref: ORG-SUBINTERIOR
            Recipient:
              - Ref: BODY-CEMP
              - Ref: ACTOR-GORES
            Frequency: Semestral
            Text: "Informar sobre el uso de esos recursos de emergencia."
        - Allow: >-
            Destinar hasta un 2% del presupuesto de Inversión Regional aprobado por el Congreso Nacional para enfrentar situaciones de emergencia (en todas
            sus etapas) definidas mediante resolución por el Ministro o Subsecretario del Interior; coordinarse con la Subsecretaría del Interior.
        - Allow: "La ejecución de estos recursos se podrá efectuar sin esperar la total tramitación del acto administrativo del Gobierno Regional."
        - Req:
            Recipient:
              - Ref: BODY-CEMP
              - Ref: ORG-DIPRES
            Frequency: Trimestral
            Text: "Informar sobre el uso de estos recursos."
      Land_For_Indigenous_Cemeteries:
        - Allow: >-
            Financiar adquisición de terrenos para municipios y/o comunidades indígenas, destinados a habilitación y/o ampliación de cementerios rurales
            situados en comunidades indígenas y en actual funcionamiento.
        - Req: >-
            Si el inmueble a adquirir es tierra indígena, se entenderá que la superficie destinada a ampliación cumple con la finalidad comunitaria del
            artículo 17 inciso segundo de la ley N° 19.253.
        - Req: >-
            La autorización exigida por esta disposición deberá otorgarse dentro del plazo de 30 días hábiles, contados desde el ingreso de la respectiva
            solicitud.
        - Req: "Beneficiarios de la adquisición se harán cargo de los gastos derivados de esta."

  Information_Requirements:
    ID: INFO-REQS-2026-GORES-01
    Items:
      - ID: INFO-REQ-01
        Req:
          Actor:
            Ref: ORG-SUBDERE
          Recipient:
            Ref: BODY-CEMP
          Frequency: Semestral
          Text: >-
            Informará los montos destinados regionalmente para proyectos de conectividad digital, que incluyan servicios de telecomunicaciones y cobertura
            digital, de zonas rezagadas que no sean cubiertas por el Fondo de Desarrollo para las Telecomunicaciones.
      - ID: INFO-REQ-02
        Req:
          Actor:
            Ref: ACTOR-GORES
          Requirements:
            - Req:
                Frequency: Mensual
                Channels:
                  - "Publicar en sus respectivas páginas web."
                Text: >-
                  La cartera de proyectos financiada con cargo a los presupuestos de inversión de los gobiernos regionales deberá ser publicada
                  mensualmente en sus respectivas páginas web.
            - Req:
                Deadline: "Dentro de los 5 días hábiles siguientes, contados desde la adopción del respectivo acuerdo."
                Channels:
                  - "Publicar en sus respectivas páginas web."
                Text: >-
                  Asimismo, deberán ser publicados los acuerdos adoptados por los respectivos consejos regionales.
      - ID: INFO-REQ-03
        Req:
          Actor:
            Ref: ACTOR-GORES
          Recipient:
            - Ref: BODY-CEMP
            - "Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara de Diputados"
            - Ref: ORG-SUBDERE
          Frequency: Trimestral
          Text: "Informar:"
          Items:
            - "a) El uso de los recursos con cargo a los presupuestos de inversión de los gobiernos regionales, listado de beneficiarios, comuna respectiva, instituciones a las cuales se transfiere, monto, productos del convenio y su aplicación a nivel regional."
            - "b) El destino de los recursos del Fondo Nacional de Desarrollo Regional a proyectos de desarrollo económico y los proyectos adjudicados por sectores según la actividad económica. Esta información deberá ser publicada en los mismos plazos en la página web de los gobiernos regionales, y un consolidado en la página web de la Subsecretaría de Desarrollo Regional y Administrativo."
      - ID: INFO-REQ-04
        Req:
          Actor:
            Ref: ACTOR-GORES
          Frequency: Trimestral
          Text: >-
            Informarán acerca de la disponibilidad presupuestaria para que las universidades reconocidas por el Estado accedan a asignaciones directas de
            recursos provenientes del Fondo Regional para la Productividad y el Desarrollo, específicamente destinados a proyectos relacionados con ciencia,
            investigación, tecnología e innovación. Asimismo, informarán sobre las solicitudes de asignación directa de recursos que recibieren de las
            universidades que tengan como objetivo fomentar la investigación, desarrollo tecnológico, innovación y actividades relacionadas con el desarrollo
            científico y aeroespacial a nivel nacional.
      - ID: INFO-REQ-05
        Req:
          Actor:
            Ref: ENTITY-GORE
          Frequency: Trimestral
          Channels:
            - "Publicar en su página web."
          Recipient:
            - "Senadores y diputados de la respectiva región"
          Text: >-
            Con el objeto de mejorar los estándares de transparencia, integridad y control social, cada Gobierno Regional deberá, en forma trimestral,
            publicar en su página web e informar a los senadores y diputados de la respectiva región de todos los proyectos adjudicados o contratados con
            cargo a los siguientes recursos presupuestarios: la oferta programática del presupuesto de inversión correspondiente al `Subtítulo 24` y los
            proyectos, contratos y convenios financiados con cargo a los `Subtítulos 31 y 33`.
          Items:
            - "Nombre del proyecto."
            - "Monto estimado."
            - "Postulantes."
            - "Pauta de evaluación."
            - "Postulante seleccionado y presupuesto aprobado."
            - "Votación de los consejeros regionales en comisiones y en el Consejo Regional."
      - ID: INFO-REQ-06
        Req:
          Actor:
            Ref: ORG-SUBDERE
          Frequency: Trimestral
          Text: >-
            Publicará trimestralmente en su página web:
          Items:
            - "Distribución de los recursos entre regiones."
            - "Criterios que fundan dicha distribución."
            - "Cartera de proyectos que con ellos se financie."
            - "Costo de cada uno de dichos proyectos."
            - "Ejecución presupuestaria del Plan Especial de Zonas Extremas por región."
      - ID: INFO-REQ-07
        Req:
          Actor:
            Ref: ORG-DIPRES
          Deadline: "30-04-2026"
          Recipient:
            - Ref: BODY-CEMP
            - "Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara"
            - "Comisión de Gobierno, Descentralización y Regionalización del Senado"
          Text: >-
            Informará los saldos iniciales de caja incorporados al presupuesto de cada Gobierno Regional a dicha fecha (programa de funcionamiento e inversión).
      - ID: INFO-REQ-08
        Req:
          Actor:
            Ref: ACTOR-GORES
          Frequency: Semestral
          Recipient:
            - Ref: BODY-CEMP
            - "Comisión de Vivienda, Desarrollo Urbano y Bienes Nacionales de la Cámara de Diputados"
          Text: "Informar sobre avances en compra de terrenos para viviendas sociales."
      - ID: INFO-REQ-09
        Req:
          Actor: "Cada gobierno regional beneficiario del Fondo Regional para la Productividad y el Desarrollo"
          Mode: "Publicación permanente en Transparencia Activa"
          Text: >-
            Publicar montos recibidos e informes de ejecución presupuestaria, incluyendo detalle de transferencias efectuadas, conforme al literal k) del
            artículo 7° del artículo primero de la ley N° 20.285; omisión o falta de actualización reclamable según artículo 8° de dicha ley.
      - ID: INFO-REQ-10
        Req:
          Actor:
            Ref: ORG-DIPRES
          Deadline: "30-09-2026"
          Recipient:
            - Ref: BODY-CEMP
            - Ref: ACTOR-GORES
          Text: >-
            Informará criterios aplicados para asignación de recursos adicionales dentro de la Partida 31, indicando nivel de ejecución presupuestaria por
            región y decisiones de distribución adoptadas.
      - ID: INFO-REQ-11
        Req:
          Actor:
            Ref: ORG-SUBDERE
          Frequency: Trimestral
          Recipient:
            - "Gobierno Regional del Maule"
            - Ref: BODY-CEMP
          Text: >-
            Informará estado de implementación del Fondo de Apoyo al Transporte Público y la Conectividad Regional en la región, señalando aplicación de
            reglas sectoriales vigentes y evaluaciones sobre alternativas de flexibilidad dentro del marco normativo aplicable para financiar iniciativas
            de interés regional.
      - ID: INFO-REQ-12
        Req:
          Actor:
            Ref: ENTITY-GORE
          Frequency: Trimestral
          Recipient:
            - "Comisiones de Gobierno, Descentralización y Regionalización y de Hacienda del Senado"
            - "Comisiones de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados"
          Text: >-
            Informar todas las iniciativas y proyectos de inversión que superen las 500 UTM, individualizando: proyecto, antecedentes, montos, plazo de
            ejecución, identidad a quien se entregarán los recursos.
      - ID: INFO-REQ-12B
        Req:
          Actor:
            Ref: ENTITY-GORE
          Deadline: "Último día hábil de marzo 2026"
          Recipient:
            - "Comisiones de Hacienda de ambas Cámaras"
          Text: >-
            Informar nombre y cargo del responsable de evacuar esta información, así como del funcionario que lo subrogará en caso de ausencia.
      - ID: INFO-REQ-13
        Req:
          Actor: "Gobernador regional"
          Frequency: Trimestral
          Recipient:
            - "Comisiones de Gobierno, Descentralización y Regionalización y de Hacienda del Senado"
            - "Comisiones de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados"
          Text: >-
            Informar toda transferencia con cargo al Fondo de Vinculación con la Comunidad: beneficiario, comuna, objeto del financiamiento, montos totales
            transferidos y fecha de cada transferencia.
      - ID: INFO-REQ-13B
        Req:
          Actor:
            Ref: ENTITY-GORE
          Deadline: "Último día hábil de marzo 2026"
          Recipient:
            - "Comisiones de Hacienda de ambas Cámaras"
          Text: >-
            Informar nombre y cargo de la persona responsable de evacuar la información solicitada y de quien le subrogará en su ausencia.
      - ID: INFO-REQ-14
        Req:
          Actor:
            Ref: ACTOR-GORES
          Frequency: Semestral
          Recipient:
            Ref: BODY-CEMP
          Text: >-
            Informar, a través de informe consolidado, ejecución presupuestaria e información sobre avance de iniciativas financiadas a través de Planes
            Especiales de Zonas Extremas.
      - ID: INFO-REQ-15
        Req:
          Actor:
            Ref: ACTOR-GORES
          Frequency: Anual
          Recipient:
            Ref: BODY-CEMP
          Text: "Informarán recursos destinados a abastecimiento mediante camiones aljibe en situaciones de emergencia hídrica."
      - ID: INFO-REQ-16
        Req:
          Actor:
            Ref: ENTITY-GORE
          Frequency: Anual
          Recipient:
            Ref: BODY-CEMP
          Text: "Informará acciones de coordinación con Dirección de Obras Hidráulicas para atender emergencias APR, detallando tiempos de respuesta y mecanismos de seguimiento."

Validation_Report:
  ID: VALIDATION-REPORT-01
  Syntax:
    Res: "YAML parse OK (ruby psych)."
  References:
    Res: "IDs únicos y Refs resolubles (verificación automática)."
  Metrics:
    TER_Approx:
      Formula: "(source_tokens - artifact_tokens) / source_tokens"
      Method: "Heurística chars/4; misma regla en ambos."
      Res: "TER ≈ -2,9%: artefacto > fuente (fuente legal ya es densa; overhead YAML/metadata/estructura semántica aumenta tamaño)."
    RD:
      Formula: "Ref_usages / total_definitions"
      Ref_Usages: 65
      Definitions: 16
      RD: 4.06
    FS:
      Formula: "(preserved_facts / source_facts) * 100"
      Method: "Revisión manual/estructural (sin extracción automática de hechos)."
      Target: 100
      FS: 100
      Warn: "FS=100 declarado por revisión manual; si necesitas auditoría estricta, hacemos diff factual (CM-DIFF-ENGINE) con checklist."
