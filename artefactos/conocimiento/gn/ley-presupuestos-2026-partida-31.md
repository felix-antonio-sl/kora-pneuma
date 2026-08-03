---
urn: urn:gn:kb:ley-presupuestos-2026-partida-31
nombre: ley-presupuestos-2026-partida-31
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre ley presupuestos 2026 partida 31; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml (sha256:27b8d7f69b97ec4aad33167c4183f49cc22fa578a729730b7f9c6056c4b8fc4a); URN KODA legado urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-14
lang: es
tags: [gn, gore-os, koda, ley, presupuestos, "2026", partida, "31"]
familia: bok
---
---
_manifest:
  urn: "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml"
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

ID: GN-LEY-PPTO-2026-P31-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-12-14
Modification-Date: 2025-12-14
Ctx: "Ley de Presupuestos Año 2026. Partida 31: Financiamiento Gobiernos Regionales. Unidad: Miles de $."
Primary-Source: staging/ppto_2026_p31/p31.md

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

Ley_Presupuestos_2026_Partida_31:
  ID: GN-LEY-PPTO-2026-P31
  Purp: "Preservar glosas y cuadros presupuestarios (ingresos/gastos) de Partida 31 para Gobiernos Regionales (Ley de Presupuestos 2026)."
  Unidad_Monetaria: "Miles de $"

  Resumen_Partida_31:
    ID: GN-LEY-PPTO-2026-P31-RES-01
    Asunto: "Partida 31: Financiamiento Gobiernos Regionales"
    Unidad_Monetaria: "Miles de $"
    Alcance: "Gobiernos Regionales (01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16)"
    Tabla_Resumen_Ingresos_Gastos:
      ID: GN-LEY-PPTO-2026-P31-RES-T01
      Columns:
        - "Sub-Título"
        - "Clasificación Económica"
        - "Total Bruto"
        - "Transferencias"
        - "Total"
      Rows:
        - ["", "INGRESOS", "1.900.047.503", "", "1.900.047.503"]
        - ["05", "TRANSFERENCIAS CORRIENTES", "17.827.479", "", "17.827.479"]
        - ["09", "APORTE FISCAL", "1.124.303.237", "", "1.124.303.237"]
        - ["13", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "757.916.787", "", "757.916.787"]
        - ["", "GASTOS", "1.900.047.503", "", "1.900.047.503"]
        - ["24", "TRANSFERENCIAS CORRIENTES", "128.872.343", "", "128.872.343"]
        - ["33", "TRANSFERENCIAS DE CAPITAL", "1.771.175.160", "", "1.771.175.160"]
      Src:
        - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.15.png"
        - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.22.png"

  Glosas:
    Glosa_01:
      ID: GN-LEY-PPTO-2026-P31-GLO-01
      Asunto: "Aplicable a Funcionamiento Regional"
      Asociada_al_Subtitulo_21_Gasto_en_Personal:
        ID: GN-LEY-PPTO-2026-P31-GLO-01-ST21
        Content: |
          No regirá la limitación establecida en el inciso segundo del artículo 10 del D.F.L N°29, de 2005, del Ministerio de Hacienda, respecto de los empleos a contrata, incluidos en las dotaciones máximas de personal de este programa.
          El personal a contrata podrá desempeñar funciones de carácter directivo que se le asignen o deleguen, mediante resolución fundada del Jefe de Servicio, la que deberá precisar las funciones delegadas. Dicho personal no podrá exceder del 20% del total del personal a contrata.
          El personal a honorarios podrá tener la calidad de Agente Público, para efectos de lo dispuesto en el Decreto Ley N°799, de 1974; para el desempeño de labores de fiscalización o certificación y hacer efectiva su responsabilidad administrativa, civil y penal por el desempeño de sus labores, de acuerdo con lo que se establezca en el respectivo convenio.
          Los Gobiernos Regionales deberán informar durante el primer trimestre del año 2026 a la Comisión de Hacienda de la Cámara de Diputados, sobre las iniciativas legales y administrativas tendientes al traspaso de la calidad contractual de funcionarios de Gobiernos Regionales de Honorarios a Contrata y el fortalecimiento de los derechos laborales de estos funcionarios.
          No regirá la limitación establecida en el artículo 3° de la Ley N°20.035, en lo relativo a la estructura y funciones de los gobiernos regionales.
      Asociada_al_Subtitulo_24_Transferencias_Corrientes:
        ID: GN-LEY-PPTO-2026-P31-GLO-01-ST24
        Content: |
          Mediante reglamento regional se determinarán los gastos de traslado y reembolso de los consejeros regionales, cuando correspondiese.
          Respecto del gasto en cometidos al extranjero de los consejeros regionales se deberá considerar como máximo el 10% del gasto del Subtítulo 24 e incorporarlo en las glosas correspondientes en la resolución de distribución inicial.
          La dotación de vehículos del Gobierno Regional podrá utilizarse en el traslado de los consejeros regionales, en cumplimiento de funciones encomendadas por el Consejo Regional.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_02:
      ID: GN-LEY-PPTO-2026-P31-GLO-02
      Asunto: "Aplicable a Inversión Regional"
      Unidad_Monetaria: "Miles de $"
      Tabla_Distribucion_02A:
        ID: GN-LEY-PPTO-2026-P31-GLO-02-T02A
        Columns:
          - "Gobierno Regional"
          - "Fondo Nacional de Desarrollo Regional"
          - "Fondo de Apoyo al Transporte Público y la Conectividad Regional"
          - "Fondo de Equidad Interregional"
          - "Fondo para la Productividad y el Desarrollo"
          - "Tesoro Público Ley N° 21.210, Modernización Tributaria"
        Rows:
          - ["Tarapacá", "35.359.987", "16.045.986", "", "10.955.743", "2.639.730"]
          - ["Antofagasta", "44.173.366", "20.880.832", "502.233", "14.256.838", "3.435.113"]
          - ["Atacama", "34.662.339", "16.149.839", "9.064.842", "11.026.651", "2.656.815"]
          - ["Coquimbo", "43.820.007", "19.975.688", "5.982.724", "13.638.832", "3.286.207"]
          - ["Valparaíso", "48.891.345", "22.325.871", "7.142.942", "15.243.470", "3.672.836"]
          - ["O'Higgins", "41.527.239", "19.123.418", "7.248.039", "13.056.926", "3.146.000"]
          - ["Maule", "53.077.751", "24.216.983", "14.506.251", "16.534.668", "3.983.944"]
          - ["Biobío", "55.752.999", "25.391.728", "10.192.165", "17.336.750", "4.177.202"]
          - ["Araucanía", "66.258.806", "30.919.504", "50.672.259", "21.110.958", "5.086.578"]
          - ["Los Lagos", "45.977.501", "21.235.317", "20.703.621", "14.498.871", "3.493.429"]
          - ["Aysén", "31.592.880", "14.644.138", "18.091.050", "9.998.601", "2.409.112"]
          - ["Magallanes", "32.703.469", "15.156.260", "7.355.822", "10.348.263", "2.493.361"]
          - ["Metropolitana", "99.499.728", "44.794.655", "1.262.043", "30.584.518", "7.369.184"]
          - ["Los Ríos", "25.727.491", "12.193.520", "24.845.561", "8.325.389", "2.005.960"]
          - ["Arica y Parinacota", "26.094.386", "11.882.961", "6.269.416", "8.113.349", "1.954.870"]
          - ["Ñuble", "41.562.476", "18.790.488", "6.353.223", "12.829.611", "3.091.230"]
          - ["Total", "726.681.770", "333.727.188", "190.192.191", "227.859.438", "54.901.571"]
        Src: "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.29.png"
      Tabla_Distribucion_02B:
        ID: GN-LEY-PPTO-2026-P31-GLO-02-T02B
        Columns:
          - "Gobierno Regional"
          - "Subsecretaría de la Cultura y las Artes"
          - "Tesoro Público Ley N° 19.275, Fondo de Desarrollo de Magallanes"
          - "Tesoro Público - Ley N° 19.143, Patentes Mineras"
          - "Tesoro Público Ley N° 19.657, Patentes Geotérmicas"
          - "Tesoro Público Art. 129 bis 19 Ley N° 20.017, Código de Aguas"
        Rows:
          - ["Tarapacá", "778.732", "", "7.523.467", "", "112.589"]
          - ["Antofagasta", "1.381.566", "", "24.188.373", "254.274", "1.128.094"]
          - ["Atacama", "969.124", "", "14.201.202", "", "999.449"]
          - ["Coquimbo", "1.009.479", "", "7.202.479", "", "758.483"]
          - ["Valparaíso", "1.145.019", "", "2.789.778", "", "656.680"]
          - ["O'Higgins", "1.050.906", "", "1.119.486", "", "1.202.029"]
          - ["Maule", "1.232.914", "", "743.014", "", "2.985.849"]
          - ["Biobío", "1.272.645", "", "639.005", "", "1.469.115"]
          - ["Araucanía", "1.875.996", "", "147.793", "", "2.126.409"]
          - ["Los Lagos", "1.194.176", "", "255.307", "", "2.268.623"]
          - ["Aysén", "846.314", "", "573.189", "", "1.208.534"]
          - ["Magallanes", "757.786", "11.690.896", "225.520", "237.602", ""]
          - ["Metropolitana", "2.016.392", "", "3.066.774", "", "4.579.804"]
          - ["Los Ríos", "820.380", "", "150.945", "", "2.962.972"]
          - ["Arica y Parinacota", "595.047", "", "1.097.872", "", "51.491"]
          - ["Ñuble", "881.003", "", "299.326", "", "682.846"]
          - ["Total", "17.827.479", "11.690.896", "64.223.530", "254.274", "23.430.569"]
        Src: "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.33.png"

      Tabla_Distribucion_02C:
        ID: GN-LEY-PPTO-2026-P31-GLO-02-T02C
        Columns:
          - "Gobierno Regional"
          - "Tesoro Público D.L. N°430, de 1992 (E.F. y T.), Patentes de Acuicultura"
          - "Fondo de Inversión y Reconversión Regional"
          - "Total"
        Rows:
          - ["Tarapacá", "9.737", "2.089.574", "75.515.545"]
          - ["Antofagasta", "5.360", "8.668.717", "118.874.766"]
          - ["Atacama", "34.313", "1.922.722", "91.687.296"]
          - ["Coquimbo", "40.860", "1.926.581", "97.641.340"]
          - ["Valparaíso", "193", "1.966.521", "103.834.655"]
          - ["O'Higgins", "116.838", "", "89.511.721"]
          - ["Maule", "32", "1.626.617", "118.908.023"]
          - ["Biobío", "14.441", "1.705.522", "117.951.572"]
          - ["Araucanía", "3.258", "2.076.814", "180.278.375"]
          - ["Los Lagos", "3.521.920", "1.426.343", "114.575.108"]
          - ["Aysén", "1.519.285", "983.623", "81.866.726"]
          - ["Magallanes", "671.521", "1.018.022", "82.658.522"]
          - ["Metropolitana", "153.288", "3.412.689", "196.739.075"]
          - ["Los Ríos", "47.407", "819.019", "77.898.644"]
          - ["Arica y Parinacota", "4.976", "798.160", "56.862.528"]
          - ["Ñuble", "1.262.128", "", "85.752.331"]
          - ["Total", "6.143.429", "33.623.892", "1.690.556.227"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.37.png"
          - "staging/ppto_2026_p31/p31.md"

    Glosa_03:
      ID: GN-LEY-PPTO-2026-P31-GLO-03
      Content: |
        Los recursos de los presupuestos de inversión regional no podrán financiar préstamos, gastos en personal, o gastos en bienes y servicios de consumo de las entidades receptoras. Asimismo, no podrán destinarse para constituir, efectuar aportes o comprar sociedades o empresas.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_04:
      ID: GN-LEY-PPTO-2026-P31-GLO-04
      Content: |
        Se podrán traspasar recursos desde cualquier Subtítulo e Ítem del presupuesto de inversión del Gobierno Regional respectivo a los Subtítulos 24, 26, 29, 31, 32.06, 33 y 34.07.
        Los gobiernos regionales podrán realizar convenios de mandato con los municipios de acuerdo con el artículo 16 de la ley N°18.091, para el financiamiento de estudios definidos en el subtítulo 22 ítem 11, del Decreto de Hacienda N° 854 del 2004, sobre clasificaciones presupuestarias.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_05:
      ID: GN-LEY-PPTO-2026-P31-GLO-05
      Content: |
        Las transferencias de recursos realizadas a las universidades del artículo 3° del D.F.L. N° 2, que fija el texto refundido, coordinado y sistematizado del Estatuto Orgánico del Consejo de Rectores de las Universidades Chilenas, y aquellas que se han adscrito al Consejo conforme con el artículo 6 de la ley N° 21.091, sobre Educación Superior, y su normativa vigente, desde los gobiernos regionales, solo podrán ser ejecutadas y utilizadas para fines dentro del ámbito de competencia del establecimiento de educación superior que se los adjudicó. La ejecución de las acciones por las cuales se efectúa la transferencia de estos recursos se hará preferentemente a las universidades con sede en la región respectiva. Asimismo, deberá llevarse a cabo de manera íntegra por parte de la propia universidad. Estas transferencias se podrán exceptuar del mecanismo de concursabilidad establecido en el articulado de la presente ley.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_06:
      ID: GN-LEY-PPTO-2026-P31-GLO-06
      Content: |
        Las transferencias corrientes del presupuesto de inversión regional de los gobiernos regionales (subtítulo 24) se regirán por las siguientes disposiciones:
        La oferta programática que ejecutan directamente los gobiernos regionales estará sujeta al Sistema de Evaluación y Monitoreo del Ministerio de Desarrollo Social y Familia y de la Dirección de Presupuestos.
        Se exceptuarán del proceso de evaluación ex ante:
        a) los programas que hayan iniciado su ejecución en años anteriores.
        b) las subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%.
        c) las transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro.
        d) las ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales, en coordinación con el Ministerio del Interior.
        La oferta programática de cada Gobierno Regional deberá respetar los principios de coherencia con las políticas públicas nacionales, coordinación, unidad de acción, eficiencia y eficacia, evitando la duplicidad o interferencia de funciones con otros órganos de la Administración del Estado.
        Asimismo, estos recursos podrán ser ejecutados por instituciones privadas sin fines de lucro, municipalidades, otras entidades públicas y organismos del gobierno central. La asignación de estos recursos se regirá por las normas contenidas en el articulado de esta ley.
        Se podrá destinar hasta un 5% del monto total de la transferencia a gastos que demande la administración de las iniciativas en el Gobierno Regional, tales como gastos en personal, gastos en bienes y servicios de consumo y en adquisición de activos no financieros, asociados con la ejecución del programa. El personal contratado a honorarios con cargo al 5% señalado tendrá la calidad de agente público.
        Con cargo a esta transferencia se podrá contratar en la entidad pública receptora a personal a honorarios cuyo vínculo cesará de pleno derecho una vez finalizado el convenio de transferencia que sirvió de fundamento a su contratación. Lo anterior, no podrá ser superior al 5% del total de la transferencia recibida.
        La oferta programática deberá regirse dentro de los ámbitos de competencia del D.F.L N°1-19.175.
        Adicionalmente, los gobiernos regionales podrán ejecutar la siguiente oferta programática no considerada en los ámbitos de competencia establecidos en el D.F.L N°1-19.175:
        Emergencia:
        a) Iniciativas de prevención y mitigación de incendios forestales.
        b) Labores preventivas preparatorias para eventos climatológicos.
        c) Ejecutar y/o financiar iniciativas asociadas a las fases de mitigación y preparación en la gestión del riesgo de desastres, definidas en la Ley Nº21.364, especialmente aquellas que tiendan a atenuar los efectos del déficit hídrico, la inaccesibilidad de agua y dar continuidad a los servicios de agua potable rural.
        d) Gastos en sanitización y calefacción de espacios públicos y/o privados, ante catástrofes y emergencias definidas por la autoridad correspondiente.
        e) Gasto en las etapas de ayudas tempranas y reconstrucción, previa coordinación con la Subsecretaría del Interior.
        f) Demolición de infraestructura en mal estado que represente riesgo de derrumbe. Lo anterior deberá ser certificado por la respectiva municipalidad.
        Se deberá informar semestralmente a la Comisión Especial Mixta de Presupuestos:
        - De las iniciativas en materia de prevención y mitigación de incendios forestales, en particular de las que se desarrollen con la comunidad organizada y redes de prevención.
        - De los programas de desarrollo y uso de tecnologías en materias de prevención, y monitoreo y soporte en el combate de emergencias en las regiones y sus provincias.
        - De los recursos destinados a la rehabilitación y recuperación que sean destinados post emergencia, en las regiones y sus provincias.
        Seguridad Pública:
        Iniciativas de prevención y seguridad ciudadana.
        Salud:
        a) Establecimiento de Planes de resolución de lista de espera en coordinación con el Ministerio de Salud, con el objeto de fortalecer la capacidad resolutiva de la red asistencial pública, aumentar las atenciones de salud otorgadas y reducir los tiempos de espera de los pacientes.
        b) Programas de cuidado de personas con discapacidad en centros regionales de rehabilitación, a cargo de instituciones privadas que ejecutan políticas públicas.
        Cuidados:
        a) Atención de adultos mayores e integración y promoción del envejecimiento activo, previa coordinación con el Servicio Nacional del Adulto Mayor.
        b) Funcionamiento de condominios de viviendas tuteladas del Servicio Nacional del Adulto Mayor.
        c) Funcionamiento de establecimientos de larga estadía para adultos mayores.
        d) Actividades de auxilio a personas en situación de calle de manera extraordinaria en coordinación con el Ministerio de Desarrollo Social y Familia.
        e) Distribución de medicamentos a domicilio a adultos mayores y enfermos crónicos, en coordinación con el Servicio de Salud respectivo.
        Cambio Climático y Gestión de Residuos:
        a) Protección del medioambiente y educación ambiental.
        b) Mantención de parques, áreas verdes y/o jardines botánicos.
        c) Operación de instalaciones para el tratamiento adecuado de los residuos sólidos domiciliarios e iniciativas de reciclaje y valorización de residuos.
        Asimismo, se podrán financiar subsidios a las municipalidades para el servicio de disposición final de residuos sólidos domiciliarios. Los parámetros para el monto del subsidio y las características técnicas se regularán mediante Resolución N° 09, de fecha 10 de marzo de 2025 de la Subsecretaría de Desarrollo Regional y Administrativo y sus modificaciones. Excepcionalmente, se podrá dar continuidad a los subsidios otorgados el año 2025 de acuerdo a los parámetros de la Resolución N°09 del 2025 de la Subsecretaría de Desarrollo Regional y Administrativo.
        d) Iniciativas de adopción, rescate, atención y tratamiento veterinario, y de gestión de residuos de animales.
        Energía, Transporte y Telecomunicaciones:
        a) Funcionamiento y continuidad de servicio de los sistemas de autogeneración de energía, reconocidos por la Subsecretaría de Energía.
        b) Operación, mantención, renovación y administración de servicios y bienes destinados a conectividad a internet y equipos de radiocomunicación.
        c) Subsidios entregados en el marco de la Ley N°20.378 Fondo de Apoyo al Transporte Público y la Conectividad Regional.
        d) Servicio de Transporte Escolar Rural.
        Gestión Hídrica:
        a) Funcionamiento, mantención y reparación de sistemas de agua potable y sanitarios rurales y/o sistemas de desalinización de aguas.
        b) Operación de alcantarillado.
        Asistencia Técnica:
        Programas destinados a financiar asistencia técnica a municipalidades para fortalecer su cartera de proyectos.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_07:
      ID: GN-LEY-PPTO-2026-P31-GLO-07
      Content: |
        Aplicable al Subtítulo 24 de los presupuestos de inversión de los gobiernos regionales.
        En las transferencias corrientes se podrá financiar el Concurso de Vinculación con la Comunidad 8%.
        Los gobiernos regionales podrán destinar hasta un 8% del total de los recursos del presupuesto de inversión regional para subvencionar las siguientes actividades:
        a) deportivas y del programa Elige Vivir Sano,
        b) de seguridad ciudadana,
        c) de participación de niños, niñas, adolescentes y jóvenes de acuerdo a lo establecido en el artículo N°6, letra p) de la Ley N°21.302,
        d) de carácter social, incluyendo programas y actividades para la atención de personas discapacitadas con dependencia severa, y de prevención y rehabilitación de drogas,
        e) de atención de adultos mayores e integración y promoción del envejecimiento activo,
        f) de protección del medioambiente y de educación ambiental,
        g) asociadas con adopción, rescate, atención y tratamiento veterinario, y gestión de residuos de animales,
        h) de funcionamiento de establecimientos de larga estadía para adultos mayores, residencias familiares para niños, niñas, adolescentes y/o jóvenes del Servicio Nacional de Protección Especializada a la Niñez y Adolescencia, Centro de Internación Provisoria e Internación en régimen cerrado y Libertad Asistida Especial con Internación Parcial, del Servicio de Reinserción Social Juvenil,
        i) funcionamiento de teatros municipales o regionales y/o monumentos históricos con atención a público, que operen en la región,
        j) culturales y patrimoniales.
        Estas actividades podrán ser ejecutadas por municipalidades, otras entidades públicas, instituciones privadas sin fines de lucro, organizaciones de la sociedad civil y organizaciones comunitarias sin fines de lucro. La asignación de estos recursos deberá cumplir con lo dispuesto en el articulado de esta ley en lo que corresponda.
        Asimismo, se podrá asignar hasta un 10% de los recursos del Concurso de Vinculación con la Comunidad 8% para financiar, previo acuerdo del Consejo Regional, mediante asignaciones directas actividades asociadas con casos emblemáticos, excepcionales y emergentes, como por ejemplo deportistas destacados. Lo anterior, sujeto a lo dispuesto en la Resolución N°72 de fecha 08.01.2025 de la Dirección de Presupuestos y sus modificaciones, que imparte instrucciones sobre asignación directa en concurso de vinculación con la comunidad.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_08:
      ID: GN-LEY-PPTO-2026-P31-GLO-08
      Content: |
        Respecto a los recursos que se destinen a las corporaciones, los gobiernos regionales deberán informar a la Dirección de Presupuestos, además de publicar en las páginas web de la corporación y del respectivo Gobierno Regional, a más tardar al término del primer trimestre: nombre o razón social de la corporación; misión, objetivos estratégicos y productos; composición del directorio; organigrama; instituciones que participan de su financiamiento (Gobierno Regional y otras entidades, públicas y privadas); vínculo de los objetivos de la corporación con los objetivos del Gobierno Regional; planificación anual (incluyendo objetivos del periodo, principales resultados esperados y actividades relevantes necesarias para alcanzarlos).
        En forma trimestral, dentro de los 30 días siguientes al término de cada trimestre: número de profesionales de la corporación, la remuneración asociada a éstos y su perfil profesional; concursos para la contratación de personal realizados en el periodo, identificando los perfiles de los cargos postulados y los resultados del concurso; recursos transferidos por el Gobierno Regional y ejecutados por la corporación en el periodo, y acumulados en el año; indicadores de gestión de la corporación, que den cuenta del avance físico y financiero de las iniciativas que le han sido encomendadas y financiadas por el Gobierno Regional.
        Las corporaciones y fundaciones constituidas con la participación del Gobierno Regional deberán dar cuenta pública anual de su gestión, mantener publicados sus estados financieros en su respectiva página web y en la del Gobierno Regional, y se regirán por la Ley N° 20.285 sobre acceso a la información pública, en todo aquello que le fuera aplicable.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_09:
      ID: GN-LEY-PPTO-2026-P31-GLO-09
      Content: |
        La siguiente glosa aplica al Subtítulo 29 del presupuesto de inversión regional de los gobiernos regionales.
        Los gobiernos regionales podrán financiar la adquisición de activos no financieros de reposición al Gobierno Central y a otras instituciones públicas.
        Excepcionalmente se podrá comprar nuevos activos no financieros incorporando un certificado de disponibilidad presupuestaria para los gastos recurrentes que generen dichos activos. Este certificado deberá ser emitido por el Ministerio o la Subsecretaría respectiva.
        Para lo anterior, los gobiernos regionales podrán realizar convenios de mandato con los receptores públicos de acuerdo con el artículo 16 de la ley N°18.091.
        Las compras que realicen para las Fuerzas de Orden y Seguridad Pública deberán contar con un certificado de pertinencia de la respectiva contratación, donación o transferencia de recursos, con los planes estratégicos de desarrollo policial.
        El referido certificado deberá ser emitido por el Ministerio de Seguridad Pública, a solicitud de las Fuerzas de Orden y Seguridad Pública.
        Los gobiernos regionales podrán financiar la adquisición de activos no financieros a los cuerpos de bomberos regionales, para lo cual deberán contar con un certificado de pertinencia técnica emitido por la Junta Nacional de Bomberos de Chile.
        Los gobiernos regionales podrán financiar la compra de terrenos. Estas adquisiciones deberán efectuarse en coordinación con el SERVIU de la región respectiva, cuando corresponda.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_10:
      ID: GN-LEY-PPTO-2026-P31-GLO-10
      Content: |
        La siguiente glosa aplica al Subtítulo 31 del presupuesto de inversión de los gobiernos regionales.
        La inversión pública deberá regirse dentro de los ámbitos de competencia del D.F.L. N°1-19.175. Adicionalmente, podrán ejecutarse las siguientes iniciativas de inversión pública:
        a) Construcción, conservación y mejoramiento de infraestructura pública en coordinación con el Ministerio sectorial respectivo.
        b) Iniciativas de inversión en transporte en coordinación con el Ministerio de Transportes y Telecomunicaciones, en el marco de la Ley N°20.378 Fondo de Apoyo al Transporte Público y la Conectividad Regional.
        c) Iniciativas de inversión de interés social en las áreas de electrificación, gas, generación de energía, conectividad digital, telefonía celular y comunicaciones, incluyendo las conexiones domiciliarias.
        d) Iniciativas de inversión en agua potable y alcantarillado.
        e) Proyectos sanitarios correspondientes a áreas de concesión de empresas del sector público.
        f) Iniciativas de inversión en Agua Potable Rural y obras que tengan por objeto la mitigación y reparación del daño producido por cambio climático a pequeños productores agrícolas y habitantes rurales.
        g) Excepcionalmente, durante el año 2026, respecto del diseño y la ejecución de proyectos de saneamiento rural o proyectos ubicados en territorios insulares
        –como agua potable, alcantarillado y disposición y tratamiento de aguas
        servidas, entre otros- el Gobierno Regional podrá, mediante resolución fundada,
        determinar como Unidad Técnica a la empresa, pública o privada, que opere en la
        región en el marco de las funciones indicadas en la Ley N°20.998 de 2017 que
        regula los Servicios Sanitarios Rurales.
        La Dirección de Obras Hidráulicas y la Subdirección de Servicios Sanitarios
        Rurales deberán informar a los Gobiernos Regionales y la Contraloría Regional
        respectiva, a más tardar los días 20 de enero y 30 de junio, las regiones que no
        disponen de especialistas en los proyectos mencionados.
        h) Proyectos de conservación de huellas y caminos vecinales privados de uso
        público, a través de administración directa, por contrato de obra pública o
        compra de servicio. Lo anterior, previo compromiso formal de la transferencia de
        la faja respectiva de estos últimos. Asimismo, se requerirá previamente el visto
        bueno de la Dirección Regional de Vialidad respectiva.
        La inversión estará sujeta al Sistema Nacional de Inversiones por parte del
        Ministerio de Desarrollo Social y Familia, y de la Dirección de Presupuestos.
        En el ejercicio de esta facultad, cada Gobierno Regional deberá respetar los
        principios de coherencia con las políticas públicas nacionales, coordinación,
        unidad de acción, eficiencia y eficacia, evitando la duplicidad o interferencia
        de funciones con otros órganos de la Administración del Estado.
        Las identificaciones presupuestarias de las iniciativas contratadas en años
        anteriores en ejecución y aquellas creadas en el mismo año, no requerirán una
        nueva aprobación del Consejo Regional, si los montos totales o resultantes son
        iguales o menores al 10% de los costos totales ya aprobados por el Consejo
        Regional, reajustados a la moneda del año en curso.
        El personal contratado a honorarios para ejecución de proyectos tendrá la
        calidad de agente público.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_11:
      ID: GN-LEY-PPTO-2026-P31-GLO-11
      Content: |
        La siguiente glosa aplica al subtítulo 33 del presupuesto de inversión de los gobiernos regionales.
        Las transferencias de capital deberán regirse por los ámbitos de competencia del D.F.L N°1-19.175. Adicionalmente, podrán financiarse las siguientes iniciativas:
        a) Proyectos de tipología PMU/PMB en coordinación con la Subsecretaría de Desarrollo Regional y Administrativo.
        b) Iniciativas de infraestructura social o deportiva, en los inmuebles que constituyan bienes comunes de propiedad de comunidades agrícolas, o ubicados en condominios de viviendas sociales y aquellos conformados de acuerdo a las leyes N°15.020 y N°16.640, sobre Reforma Agraria, y N°19.253, Ley Indígena, y en otros inmuebles de similar calidad jurídica e inmuebles de propiedad de carácter fiscal en tuición de organizaciones privadas sin fines de lucro con fines sociales.
        c) Iniciativas de construcción, habilitación, conservación y mejoramiento de caminos comunitarios ubicados en territorios regidos por la Ley N°19.253 o de propiedad de comunidades agrícolas.
        d) Intervenciones en las fachadas de inmuebles de propiedad privada que cuenten con protección patrimonial.
        e) Estudios de factibilidad e iniciativas que propendan al mejoramiento de la eficiencia del sistema portuario de los territorios insulares.
        f) Iniciativas de protección y puesta en valor de inmuebles y bienes muebles declarados Monumento Nacional, Inmueble de Conservación Histórica, o que se ubiquen en zona de conservación histórica de acuerdo a plano regulador y los sitios de patrimonio mundial de la UNESCO o de la Lista Tentativa de los Bienes Culturales de Chile postulados como Patrimonio Mundial de la UNESCO, incluyendo aquellos que se ejecuten en conjunto con el sector privado.
        g) Subsidios a empresas de los sectores público o privado para proyectos de inversión de interés social en materias de electrificación, gas, generación de energía, telefonía celular y comunicaciones. Los proyectos que se financien con estos subsidios se evaluarán al igual que una iniciativa de inversión con la metodología establecida por el Ministerio de Desarrollo Social y Familia.
        h) Iniciativas de inversión en establecimientos educacionales, incluidos jardines infantiles, con el objetivo de la obtención y mantención del Reconocimiento Oficial del Ministerio de Educación.
        i) Subsidio para la habilitación de infraestructura de centros regionales de tratamiento y rehabilitación de personas discapacitadas.
        j) Subsidios para la mantención y reparación de sistemas y/o programas de Agua Potable Rural (APR) y sanitarios rurales y/o sistemas de desalinización de aguas. En este caso la transferencia se efectuará mediante resolución fundada del Gobernador Regional, la que producirá sus efectos sin esperar su total tramitación. Asimismo, deberá contar con pronunciamiento técnico favorable de la Subdirección de Servicios Sanitarios Rurales.
        k) Subsidio para la habilitación de establecimientos de larga estadía para adultos mayores.
        Estos recursos podrán ser ejecutados por instituciones privada sin fines de lucro, otras entidades públicas y organismos del gobierno central. La asignación de estos recursos se regirá por el articulado de esta ley.
        Los gobiernos regionales podrán efectuar transferencias de recursos a las municipalidades y a las respectivas empresas sanitarias de la región para financiar el monitoreo, las mantenciones, diseño de soluciones y los trabajos preventivos ante filtraciones de las redes de agua potable y alcantarillado de viviendas unifamiliares, conjuntos habitacionales de interés público, infraestructuras públicas, y en otros usos de suelo afectados por dichas filtraciones, previa visación del órgano competente de la región.
        Con estos recursos se podrá también financiar a las entidades señaladas en el inciso anterior, la pavimentación de aquellos sectores en que éstas hayan efectuado recambio de redes de agua potable y alcantarillado. Durante el presente año, para los proyectos de Construcción de Infraestructura Sanitaria financiados por los Gobiernos Regionales, regirá el límite de costo establecido en el artículo 8°, del Decreto Supremo N° 829 de 1998, del Ministerio del Interior, y sus modificaciones.
        Las entidades receptoras de estos recursos deberán rendir cuenta de su utilización al Gobierno Regional y, cuando corresponda, a la Contraloría General de la República. Los recursos transferidos se regirán por la normativa de la institución receptora y en los convenios respectivos, celebrados por el Gobierno Regional y dichas instituciones, se establecerán los procedimientos y condiciones bajo los cuales se efectuará la aplicación de los recursos que se transfieren.
        Los gobiernos regionales, al momento de efectuar la distribución inicial de sus presupuestos de inversión regional, deberán crear una asignación de provisión sin distribuir para el Fondo de Apoyo al Transporte y la Conectividad Regional dentro del Ítem 33.03. En el transcurso del año presupuestario podrán reasignar desde esta provisión para el financiamiento de las iniciativas elegibles para este Fondo, a los subtítulos 24, 29, 31 y 33, respectivamente. No obstante lo anterior, en la resolución de apertura, los gobiernos regionales podrán crear las asignaciones de arrastres que se financien con estos fondos.
        Asimismo, de acuerdo a lo señalado en la letra b) del numeral 1 del artículo 4° transitorio de la ley N°20.378 y sus modificaciones, se podrán financiar inversiones complementarias de infraestructura, en cualquiera de sus etapas, cuyas iniciativas consideren obras de las tipologías comprendidas en la letra b) señalada, tales como: iniciativas de construcción, mejoramiento, conservación y/o reposición de obras viales y/o urbanas, así como aquellas iniciativas relacionadas con la seguridad vial.
        Al menos el 50% de los recursos del Fondo de Apoyo al Transporte y la Conectividad Regional, se destinarán al financiamiento de iniciativas regionales de transporte público mayor y menor. Se deberá informar sobre el destino de los fondos restantes a la Comisión de Obras Públicas, Transportes y Telecomunicaciones de la Cámara de Diputados y a la Comisión Especial Mixta de Presupuestos.
        Los Gobiernos Regionales deberán contemplar, con cargo a los recursos del Fondo de Apoyo al Transporte Público y la Conectividad Regional, los montos necesarios para financiar los compromisos, obligaciones y efectos que se deriven de los Convenios suscritos con el Ministerio de Transportes y Telecomunicaciones, para que éstos se proyecten más allá del período de vigencia de dichos convenios, previa evaluación entre ambas instituciones. Lo anterior deberá reflejarse en la programación presupuestaria regional correspondiente, a fin de garantizar la continuidad de las acciones comprometidas y la sostenibilidad de las iniciativas de conectividad y del transporte público regional.
        Las identificaciones presupuestarias de las iniciativas contratadas en años anteriores en ejecución y aquellas creadas en el mismo año, no requerirán una nueva aprobación del Consejo Regional, si los montos totales o resultantes son iguales o menores al 10% de los costos totales ya aprobados por el Consejo Regional, reajustados a la moneda del año en curso.
        El personal contratado a honorarios para ejecución de proyectos y/o programas tendrá la calidad de agente público.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_12:
      ID: GN-LEY-PPTO-2026-P31-GLO-12
      Content: |
        Las transferencias de capital del presupuesto de inversión de los gobiernos regionales podrán financiar proyectos de municipalidades asociados al Fondo Regional de Iniciativa Local (FRIL). Estos proyectos deberán contar con informe favorable del Ministerio de Desarrollo Social y Familia y destinarse a ejecutar, mantener o conservar infraestructura pública.
        Los gobiernos regionales, siguiendo los lineamientos de la Guía Operativa del Fondo Regional de Iniciativa Local publicada por la Subsecretaría de Desarrollo Regional y Administrativo contenida en la Resolución Exenta N°15.051 del 29 de diciembre de 2023, mediante resolución podrán aprobar instructivos o bases que establezcan la metodología de distribución de los recursos entre comunas, los procedimientos de ejecución, de entrega de recursos, de rendición de gasto al Gobierno Regional y otros que permitan la mejor utilización de los recursos del Fondo Regional de Iniciativa Local. Una vez aprobados los montos para cada municipio, el compromiso de financiamiento será informado por el Gobierno Regional mediante oficio dirigido al municipio respectivo.
        Los proyectos que se ejecuten con recursos transferidos a los municipios, cuyo costo total por proyecto sea inferior a 5000 UTM, valorizadas al 1 de enero del ejercicio presupuestario vigente, no requerirán informe favorable del Ministerio de Desarrollo Social y Familia. Sin perjuicio de lo anterior, deberá ser ingresada al Sistema Nacional de Inversiones la información necesaria, según lo dispuesto en el Oficio Ordinario N°2 del 26 de enero de 2024, e instructivo asociado, del Ministerio de Hacienda y del Ministerio de Desarrollo Social y Familia.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_13:
      ID: GN-LEY-PPTO-2026-P31-GLO-13
      Content: |
        Los recursos que se ejecuten con cargo al Fondo Regional para la Productividad y el Desarrollo se deberán destinar a los fines establecidos en el inciso segundo del artículo 13 de la ley N° 21.591, el Decreto N°1699 de fecha 6 de diciembre de 2025 del Ministerio de Hacienda, Resolución Exenta N° 33, de 2024, del Ministerio de Ciencias, Tecnología, Conocimiento e Innovación, y sus modificaciones, y la Resolución Exenta N°08, de 2025, de la Subsecretaria de Economía y Empresas de Menor Tamaño y sus modificaciones.
        Los gobiernos regionales, al momento de efectuar la distribución inicial de sus presupuestos de inversión regional, deberán crear una asignación de provisión sin distribuir para el Fondo Regional para la Productividad y el Desarrollo dentro del Ítem 33.03. En el transcurso del año presupuestario podrán reasignar desde esta provisión para el financiamiento de las iniciativas con cargo a este Fondo. No obstante lo anterior, en la resolución de apertura, los gobiernos regionales podrán crear las asignaciones de arrastres que se financien con estos fondos.
        Los gobiernos regionales podrán transferir directamente recursos a iniciativas que se ejecuten en la región y hayan sido seleccionadas mediante concurso convocado por CORFO o la ANID, y cuyas instituciones ejecutoras estén incluidas en la Resolución Exenta N° 33, de 2024, del Ministerio de Ciencias, Tecnología, Conocimiento e Innovación, y sus modificaciones.
        Asimismo, se faculta a los gobiernos regionales para efectuar las creaciones y modificaciones de asignaciones en sus presupuestos de inversión regional para el pago de los compromisos de arrastre de iniciativas ejecutadas por las instituciones elegibles del Fondo de Innovación y Competitividad.
        Con cargo a estos recursos, los gobiernos regionales podrán participar del financiamiento de iniciativas de los Programas de Desarrollo Productivo Sostenible del Ministerio de Economía, Fomento y Turismo, así como de iniciativas del Programa de Financiamiento Estructural I+D+i Universitario del Ministerio de Ciencia, Tecnología, Conocimiento e Innovación.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_14:
      ID: GN-LEY-PPTO-2026-P31-GLO-14
      Content: |
        Se podrá traspasar hasta un 3% del presupuesto de inversión aprobado por el Congreso Nacional de cada Gobierno Regional, a requerimiento de la Subsecretaría del Interior a las asignaciones 24.03.002 y/o 33.03.001 del presupuesto de dicha Subsecretaría para enfrentar situaciones de emergencia.
        La Subsecretaría del Interior informará semestralmente sobre el uso de esos recursos de emergencia a la Comisión Especial Mixta de Presupuestos y a los Gobiernos Regionales que aportaron a ese Fondo de Emergencia.
        Asimismo, los gobiernos regionales podrán destinar hasta un 2% del presupuesto de Inversión Regional aprobado por el Congreso Nacional, para enfrentar situaciones de emergencia (en todas sus etapas) definidas mediante resolución por el Ministro o Subsecretario del Interior. Para materializar lo anterior, los gobiernos regionales deberán coordinarse con la Subsecretaría del Interior. La ejecución de estos recursos se podrá efectuar sin esperar la total tramitación del acto administrativo del Gobierno Regional.
        Trimestralmente, los gobiernos regionales informarán a la Comisión Especial Mixta de Presupuestos y a la Dirección de Presupuestos, sobre el uso de estos recursos.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_15:
      ID: GN-LEY-PPTO-2026-P31-GLO-15
      Content: |
        Los gobiernos regionales podrán financiar la adquisición de terrenos para municipios y/o comunidades indígenas, destinados a la habilitación y/o ampliación de cementerios rurales situados en comunidades indígenas y que se encuentren en actual funcionamiento.
        En caso de que el inmueble a adquirir tenga la calidad de tierra indígena, se entenderá que el mismo, en la superficie destinada a la ampliación, cumple con la finalidad comunitaria exigida por el artículo 17 inciso segundo de la ley N° 19.253.
        La autorización exigida por esta disposición deberá otorgarse dentro del plazo de 30 días hábiles, contados desde el ingreso de la respectiva solicitud.
        Los beneficiarios de la adquisición se harán cargo de los gastos derivados de esta.
      Src: "staging/ppto_2026_p31/p31.md"

    Glosa_16:
      ID: GN-LEY-PPTO-2026-P31-GLO-16
      Content: |
        Requerimientos de información:
        1.- La Subsecretaría de Desarrollo Regional y Administrativo informará semestralmente a la Comisión Especial Mixta de Presupuestos los montos destinados regionalmente para proyectos de conectividad digital, que incluyan servicios de telecomunicaciones y cobertura digital, de zonas rezagadas que no sean cubiertas por el Fondo de Desarrollo para las Telecomunicaciones.
        2.- La cartera de proyectos financiada con cargo a los presupuestos de inversión de los gobiernos regionales deberá ser publicada mensualmente en sus respectivas páginas web. Asimismo, deberán ser publicados los acuerdos adoptados por los respectivos consejos regionales, dentro de los 5 días hábiles siguientes, contados desde la adopción del respectivo acuerdo.
        3.- Trimestralmente los gobiernos regionales deberán informar a la Comisión Especial Mixta de Presupuestos, a la Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara de Diputados y a la Subsecretaría de Desarrollo Regional y Administrativo:
        a) El uso de los recursos con cargo a los presupuestos de inversión de los gobiernos regionales, listado de beneficiarios, comuna respectiva, instituciones a las cuales se transfiere, monto, productos del convenio y su aplicación a nivel regional.
        b) El destino de los recursos del Fondo Nacional de Desarrollo Regional a proyectos de desarrollo económico y los proyectos adjudicados por sectores según la actividad económica. Esta información deberá ser publicada en los mismos plazos en la página web de los gobiernos regionales, y un consolidado en la página web de la Subsecretaría de Desarrollo Regional y Administrativo.
        4.- Los gobiernos regionales informarán trimestralmente acerca de la disponibilidad presupuestaria para que las universidades reconocidas por el Estado accedan a asignaciones directas de recursos provenientes del Fondo Regional para la Productividad y el Desarrollo, específicamente destinados a proyectos relacionados con ciencia, investigación, tecnología e innovación. Asimismo, informarán sobre las solicitudes de asignación directa de recursos que recibieren de las universidades que tengan como objetivo fomentar la investigación, desarrollo tecnológico, innovación y actividades relacionadas con el desarrollo científico y aeroespacial a nivel nacional.
        5.- Con el objeto de mejorar los estándares de transparencia, integridad y control social, cada Gobierno Regional deberá, en forma trimestral, publicar en su página web e informar a los senadores y diputados de la respectiva región de todos los proyectos adjudicados o contratados con cargo a los siguientes recursos presupuestarios: la oferta programática del presupuesto de inversión correspondiente al Subtítulo 24 y los proyectos, contratos y convenios financiados con cargo a los Subtítulos 31 y 33. En esta información se deberá, al menos, identificar el nombre del proyecto; el monto estimado; los postulantes; la pauta de evaluación; el postulante seleccionado y presupuesto aprobado, y la votación de los consejeros regionales en comisiones y en el Consejo Regional.
        6.- La Subsecretaría de Desarrollo Regional y Administrativo deberá publicar trimestralmente en su página web, la distribución de los recursos entre regiones, los criterios que fundan dicha distribución, la cartera de proyectos que con ellos se financie, individualizando el costo de cada uno de dichos proyectos y la ejecución presupuestaria del Plan Especial de Zonas Extremas por región.
        7.- La Dirección de Presupuestos deberá informar a más tardar el 30 de abril de 2026 a la Comisión Especial Mixta de Presupuestos, a la Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara, y a la Comisión de Gobierno, Descentralización y Regionalización del Senado, los saldos iniciales de caja que se incorporaron al presupuesto de cada Gobierno Regional a dicha fecha(tanto del programa de funcionamiento como de inversión).
        8.- Semestralmente los Gobiernos Regionales deberán informar a la Comisión Especial Mixta de Presupuestos, y a la Comisión de Vivienda, Desarrollo Urbano y Bienes Nacionales de la Cámara de Diputados, sobre los avances en la compra de terrenos para viviendas sociales.
        9.- Cada gobierno regional beneficiario de los recursos provenientes del Fondo Regional para la Productividad y el Desarrollo deberá publicar en el sitio electrónico en el que se da cumplimiento a las obligaciones de Transparencia Activa, de forma permanente, completa y actualizada, los montos recibidos y los informes de ejecución presupuestaria, incluyendo el detalle de las transferencias efectuadas, de conformidad con lo dispuesto en el literal k) del artículo 7° del artículo primero de la ley N° 20.285, sobre acceso a la información pública, los que deberán contemplar el detalle de la ejecución de los recursos provenientes del mencionado Fondo. La omisión de la publicación en la forma señalada o su falta de actualización podrá reclamarse de acuerdo con lo dispuesto en el artículo 8° de dicha ley.
        10.- La Dirección de Presupuestos deberá informar a la Comisión Especial Mixta de Presupuestos y a los Gobiernos Regionales, antes del 30 de septiembre de 2026, los criterios aplicados para la asignación de recursos adicionales dentro de la Partida 31, indicando expresamente el nivel de ejecución presupuestaria considerado para cada región y las decisiones de distribución adoptadas de conformidad con dichos criterios.
        11.- La Subsecretaría de Desarrollo Regional y Administrativo deberá informar trimestralmente al Gobierno Regional del Maule y a la Comisión Especial Mixta de Presupuestos el estado de implementación del Fondo de Apoyo al Transporte Público y la Conectividad Regional en la región, señalando la aplicación de las reglas sectoriales vigentes y las evaluaciones realizadas respecto de alternativas de flexibilidad dentro del marco normativo aplicable para financiar iniciativas de interés regional.
        12.- El Gobierno Regional deberá informar trimestralmente a las Comisiones de Gobierno, Descentralización y Regionalización y de Hacienda del Senado, y de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados, todas las iniciativas y proyectos de inversión que superen las 500 UTM, individualizando: el proyecto, los antecedentes tenidos a la vista para su aprobación, montos, plazo de ejecución y la identidad a quien se entregarán los recursos. El Gobierno Regional respectivo, deberá informar a la Comisiones de Hacienda, de ambas Cámaras, a más tardar hasta el último día hábil de marzo del año 2026 el nombre y cargo del responsable de evacuar esta información, así como del funcionario que lo subrogará en caso de ausencia.
        13.- Toda transferencia de recursos con cargo al Fondo de Vinculación con la Comunidad, deberá ser informada por el gobernador regional de forma trimestral a las Comisiones de Gobierno Descentralización y Regionalización y de Hacienda del Senado, y de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización y de Hacienda de la Cámara de Diputados, indicando especialmente: la individualización del beneficiario, comuna a la que pertenece, objeto del financiamiento, montos totales del dinero transferido y la fecha en que se concretó cada transferencia. El Gobierno Regional respectivo, deberá informar a la Comisiones de Hacienda de ambas Cámaras, a más tardar hasta el último día hábil del mes de marzo del año 2026, el: nombre y cargo de la persona responsable de evacuar la información solicitada y de quien le subrogará en su ausencia.
        14.- Los Gobiernos Regionales deberán informar semestralmente a la Comisión Especial Mixta de Presupuestos, a través de un informe consolidado, respecto de la ejecución presupuestaria e información sobre el avance de las iniciativas financiadas a través de los Planes Especiales de Zonas Extremas.
        15.- Los Gobiernos Regionales informarán anualmente a la Comisión Especial Mixta de Presupuestos los recursos destinados a abastecimiento mediante camiones aljibe en situaciones de emergencia hídrica.
        16.- El Gobierno Regional informará anualmente a la Comisión Especial Mixta de Presupuestos las acciones de coordinación con la Dirección de Obras Hidráulicas para atender emergencias APR, detallando tiempos de respuesta y mecanismos de seguimiento.
        17.- El Gobierno Regional deberá remitir a la Comisión Especial Mixta de Presupuestos, a la Comisión de Zonas Extremas y Antártica Chilena de la Cámara de Diputados y a la Comisión de Zonas Extremas y Territorios Especiales del Senado, a más tardar el 1 de junio del 2025, un informe consolidado del avance financiero de sus programas de inversión asociados a políticas de zonas extremas, especificando las iniciativas financiadas mediante el FONDEMA y Planes de Desarrollo para Territorios Rezagados.
      Src: "staging/ppto_2026_p31/p31.md"

  Programas:
    Programa_03_Asociatividad_y_Planes_Especiales:
      ID: GN-LEY-PPTO-2026-P31-PROG-03
      Partida: "31"
      Capitulo: "01"
      Programa: "03"
      Asunto: "Asociatividad y Planes Especiales (01,06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-PROG-03-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["09", "", "", "INGRESOS", "", "80.618.943"]
          - ["09", "", "", "APORTE FISCAL", "", "78.556.943"]
          - ["09", "01", "", "Libre", "", "78.556.943"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "2.062.000"]
          - ["13", "02", "", "Del Gobierno Central", "", "2.062.000"]
          - ["13", "02", "004", "Subsecretaría de Desarrollo Regional y Administrativo - Programa 05", "", "2.062.000"]
          - ["24", "", "", "GASTOS", "", "80.618.943"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "10"]
          - ["24", "01", "", "Al Sector Privado", "", "10"]
          - ["24", "01", "040", "Asociatividad Regional", "02", "10"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "80.618.933"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "80.618.933"]
          - ["33", "03", "060", "Planes Especiales de Zonas Extremas", "03", "70.442.245"]
          - ["33", "03", "070", "Planes de Desarrollo para Territorios Rezagados", "04", "8.114.688"]
          - ["33", "03", "090", "Fondo Áreas Metropolitanas", "05", "2.062.000"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.47.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-01
          Content: |
            Se deberá informar trimestralmente a la Comisión Especial Mixta de Presupuestos respecto a los avances en el proceso de elaboración de los Estatutos Especiales para las comunas de Rapa Nui y Juan Fernández, así como la implementación del estudio de capacidad de carga para esta última.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-02
          Content: |
            Los gobiernos regionales, con cargo a su programa de funcionamiento, podrán transferir recursos al Programa Asociatividad y Planes Especiales para el financiamiento de la operación de la Asociación de Gobernadores Regionales en ejercicio. Los recursos transferidos podrán destinarse a financiar todo tipo de gastos, incluyendo gastos en personal para un máximo de 5 personas, y bienes y servicios de consumo. La transferencia de estos recursos a dicha Asociación se efectuará por decreto conjunto emitido por el Ministerio de Hacienda y el Ministerio del Interior, dictado bajo la fórmula “Por orden del Presidente de la República”.
            Trimestralmente, la Asociación de Gobernadores Regionales informará a la Comisión Especial Mixta de Presupuestos sobre la ejecución y el destino de los recursos asignados.
            Asimismo, con cargo a los recursos para funcionamiento regional, los Gobiernos Regionales podrán contribuir al financiamiento de la operación de la Asociación Nacional de Consejeros Regionales en ejercicio.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-03
          Content: |
            Estos recursos se destinarán a la ejecución de iniciativas de los Planes Especiales de Zonas Extremas o de la Política Nacional de Zonas Extremas. Los gobiernos regionales podrán solicitar la aplicación de estos recursos una vez publicada esta Ley de Presupuestos, indicando las iniciativas que priorizan y el programa de ejecución que proponen para cada una de ellas. Corresponderá a la Subsecretaría de Desarrollo Regional y Administrativo, en conjunto con la Dirección de Presupuestos, distribuir los recursos e informar lo resuelto a los gobiernos regionales respectivos. A más tardar dentro del primer trimestre del año de vigencia de la presente ley deberán estar distribuidos los recursos comprometidos en proyectos de arrastre.
            Semestralmente el Gobierno Regional respectivo informará a la Comisión de Zonas Extremas y Antártica Chilena de la Cámara de Diputados y a la Comisión Especial de Zonas Extremas y Territorios Especiales del Senado, como asimismo a la Comisión Especial Mixta de Presupuestos, acerca de la ejecución presupuestaria y los planes generados en virtud de la Política Nacional de Zonas Extremas, correspondiente a la Región de Aysén del General Carlos Ibáñez del Campo.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-04
          Content: |
            Estos recursos se destinarán a iniciativas en los territorios incluidos en el Plan de Desarrollo para Territorios Rezagados, establecido mediante el Decreto N° 90 de 2023 del Ministerio del Interior y Seguridad Pública, y sus modificaciones.
            Un monto no superior a $388.359 miles podrá ser destinado a cualquier tipo de gasto, incluso en bienes y servicios de consumo y en personal para actividades transitorias, así como para la elaboración de estudios, realización de talleres e información a la comunidad, para fortalecer los equipos de apoyo para la formulación de nuevos planes de territorios rezagados, en conformidad al reglamento definido en el Decreto N° 90 de 2023, del Ministerio del Interior y Seguridad Pública y sus modificaciones, y para el monitoreo de los planes definidos para los territorios rezagados. Con este objeto, los recursos podrán transferirse a los programas de funcionamiento de esta Partida o a programas de la Subsecretaría de Desarrollo Regional y Administrativo.
            Los gobiernos regionales que tengan aprobados Territorios Rezagados definidos por la Subsecretaría de Desarrollo Regional y Administrativo podrán solicitar a esta misma la aplicación de estos recursos una vez publicada esta Ley de Presupuestos, indicando las iniciativas de arrastres y nuevas que priorizan, y el programa de ejecución que proponen para cada una de ellas. Adicionalmente, dicha Subsecretaría deberá publicar trimestralmente en su página web el criterio y distribución de los recursos entre regiones y la cartera de proyectos que con ellos se financie.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-05
          Content: |
            Estos recursos se podrán incorporar en los presupuestos de los gobiernos regionales que hayan constituido áreas metropolitanas de acuerdo con lo establecido en la Ley N° 21.074 y el Decreto N° 98, de 2019 del Ministerio del Interior, que aprueba reglamento que fija los estándares mínimos para el establecimiento de las áreas metropolitanas y establece normas para su constitución y sus modificaciones.
            El financiamiento de las etapas de inversión o preinversión de infraestructura y servicios urbanos a escala metropolitana que incluye, entre otras, proyectos de gestión de residuos, iniciativas que tengan incidencia o impacto en dos o más comunas de una misma región, que provean servicios a población de dos más comunas de una región, o se emplacen en un área metropolitana constituida mediante decreto supremo, se regularán por las siguientes reglas especiales:
            a) Mediante resolución, la Subsecretaria de Desarrollo Regional y Administrativo deberá calificar las iniciativas de infraestructura o servicios urbanos a escala metropolitana factibles de ejecutar y financiar con este fondo.
            b) Estos recursos podrán incorporarse en los presupuestos de los gobiernos regionales, que tengan aprobadas áreas metropolitanas, para el financiamiento de los gastos necesarios que permitan el cumplimiento de las iniciativas aprobadas.
            c) Asimismo, con estos recursos se podrá financiar adquisición de equipos y equipamiento, asistencias técnicas e inspecciones técnicas y legales, para el diseño, ejecución, supervisión y seguimiento de iniciativas aprobadas.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-PROG-03-GLO-06
          Content: |
            Los Gobiernos Regionales deberán remitir a la Comisión Especial Mixta de Presupuesto, a la Comisión de Zonas Extremas de la Cámara de Diputados y Diputadas y a la Comisión de Zonas Extremas del Senado, a mas tardar el 01 de junio del 2026, un informe consolidado del avance financiero de sus programas de inversión asociados a políticas de zonas extremas, especificando las iniciativas financiadas mediante el FONDEMA, el PEDZE y Planes de Desarrollo para Territorios Rezagados.
          Src: "staging/ppto_2026_p31/p31.md"

  Capitulos_Regionales:
    Region_Tarapaca_Programa_04:
      ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04
      Region: "Tarapacá"
      Partida: "31"
      Capitulo: "01"
      Programa: "04"
      Asunto: "Gobierno Regional Región de Tarapacá"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "82.524.282"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "778.732"]
          - ["05", "02", "", "Del Gobierno Central", "", "778.732"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "778.732"]
          - ["09", "", "", "APORTE FISCAL", "", "42.368.724"]
          - ["09", "01", "", "Libre", "", "42.368.724"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "39.376.826"]
          - ["13", "02", "", "Del Gobierno Central", "", "39.376.826"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "7.523.467"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "112.589"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "2.089.574"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "9.737"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "16.045.986"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "2.639.730"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "10.955.743"]
          - ["24", "", "", "GASTOS", "", "82.524.282"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "7.008.737"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "7.008.737"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "7.008.737"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "75.515.545"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "75.515.545"]
          - ["33", "03", "150", "Inversión Regional", "", "75.515.545"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.37.55.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-GLO-02
          Content: |
            Gastos en personal, en miles de $5.514.029
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 136
            b) Horas extraordinarias año
            - Miles de $ 20.367
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 29.702
            - En el Exterior, en Miles de $ 8.978
            d) Convenios con personas naturales
            - N° de Personas 1
            - Miles de $ 30.994
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 3
            - Miles de $ 44.591
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 17.113
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-TAR-PROG-04-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 13.547
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Antofagasta_Programa_05:
      ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05
      Region: "Antofagasta"
      Partida: "31"
      Capitulo: "01"
      Programa: "05"
      Asunto: "Gobierno Regional Región de Antofagasta"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "126.952.256"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.381.566"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.381.566"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.381.566"]
          - ["09", "", "", "APORTE FISCAL", "", "52.753.089"]
          - ["09", "01", "", "Libre", "", "52.753.089"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "72.817.601"]
          - ["13", "02", "", "Del Gobierno Central", "", "72.817.601"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "24.188.373"]
          - ["13", "02", "009", "Tesoro Público Ley N°19.657, Patentes Geotérmicas", "", "254.274"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "1.128.094"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "8.668.717"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "5.360"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "20.880.832"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.435.113"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "14.256.838"]
          - ["24", "", "", "GASTOS", "", "126.952.256"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.077.490"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.077.490"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.077.490"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "118.874.766"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "118.874.766"]
          - ["33", "03", "135", "Fondo de Desarrollo Región de Antofagasta Convenio Litio", "06", "10"]
          - ["33", "03", "150", "Inversión Regional", "", "118.874.756"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.02.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-02
          Content: |
            Gastos en personal, en miles de $5.895.380
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 133
            b) Horas extraordinarias año
            - Miles de $ 12.906
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 49.502
            - En el Exterior, en Miles de $ 13.680
            d) Convenios con personas naturales
            - N° de Personas 6
            - Miles de $ 174.299
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 3
            - Miles de $ 39.290
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 12.279
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 85.799
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-ANT-PROG-05-GLO-06
          Content: |
            Estos recursos se deberán destinar al financiamiento de proyectos/o programas según los estipulados en el Convenio de Aportes entre SQM Salar S.A. y el Gobierno Regional de Antofagasta con la presencia de la Corporación de Fomento de la Producción.
            Trimestralmente el Gobierno Regional deberá informar a la Comisión Especial Mixta de Presupuestos sobre el uso de estos recursos.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Atacama_Programa_06:
      ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06
      Region: "Atacama"
      Partida: "31"
      Capitulo: "01"
      Programa: "06"
      Asunto: "Gobierno Regional Región de Atacama"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "98.620.736"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "969.124"]
          - ["05", "02", "", "Del Gobierno Central", "", "969.124"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "969.124"]
          - ["09", "", "", "APORTE FISCAL", "", "50.660.621"]
          - ["09", "01", "", "Libre", "", "50.660.621"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "46.990.991"]
          - ["13", "02", "", "Del Gobierno Central", "", "46.990.991"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "14.201.202"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "999.449"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.922.722"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "34.313"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "16.149.839"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "2.656.815"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "11.026.651"]
          - ["24", "", "", "GASTOS", "", "98.620.736"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "6.933.440"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "6.933.440"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "6.933.440"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "91.687.296"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "91.687.296"]
          - ["33", "03", "150", "Inversión Regional", "", "91.687.296"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.09.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-02
          Content: |
            Gastos en personal, en miles de $5.486.858
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 135
            b) Horas extraordinarias año
            - Miles de $ 19.856
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 55.297
            - En el Exterior, en Miles de $ 25.650
            d) Convenios con personas naturales
            - N° de Personas 5
            - Miles de $ 77.644
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 52.913
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 12.826
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 5.922
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-ATA-PROG-06-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Coquimbo_Programa_07:
      ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07
      Region: "Coquimbo"
      Partida: "31"
      Capitulo: "01"
      Programa: "07"
      Asunto: "Gobierno Regional Región de Coquimbo(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "105.304.167"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.009.479"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.009.479"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.009.479"]
          - ["09", "", "", "APORTE FISCAL", "", "57.465.558"]
          - ["09", "01", "", "Libre", "", "57.465.558"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "46.829.130"]
          - ["13", "02", "", "Del Gobierno Central", "", "46.829.130"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "7.202.479"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "758.483"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.926.581"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "40.860"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "19.975.688"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.286.207"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "13.638.832"]
          - ["24", "", "", "GASTOS", "", "105.304.167"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "7.662.827"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "7.662.827"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "7.662.827"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "97.641.340"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "97.641.340"]
          - ["33", "03", "150", "Inversión Regional", "", "97.641.340"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.15.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-01
          Content: |
            Dotación máxima de vehículos 7
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-02
          Content: |
            Gastos en personal, en miles de $5.902.999
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 154
            b) Horas extraordinarias año
            - Miles de $ 9.928
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 59.402
            - En el Exterior, en Miles de $ 21.375
            d) Convenios con personas naturales
            - N° de Personas 16
            - Miles de $ 367.034
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 58.638
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 25.669
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 20.069
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-COQ-PROG-07-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Valparaiso_Programa_08:
      ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08
      Region: "Valparaíso"
      Partida: "31"
      Capitulo: "01"
      Programa: "08"
      Asunto: "Gobierno Regional Región de Valparaíso"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "112.490.763"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.145.019"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.145.019"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.145.019"]
          - ["09", "", "", "APORTE FISCAL", "", "64.690.395"]
          - ["09", "01", "", "Libre", "", "64.690.395"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "46.655.349"]
          - ["13", "02", "", "Del Gobierno Central", "", "46.655.349"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "2.789.778"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "656.680"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.966.521"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "193"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "22.325.871"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.672.836"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "15.243.470"]
          - ["24", "", "", "GASTOS", "", "112.490.763"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.656.108"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.656.108"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.656.108"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "103.834.655"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "103.834.655"]
          - ["33", "03", "150", "Inversión Regional", "06", "103.834.655"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.21.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-01
          Content: |
            Dotación máxima de vehículos 7
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-02
          Content: |
            Gastos en personal, en miles de $6.342.041
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 161
            b) Horas extraordinarias año
            - Miles de $ 39.710
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 39.601
            - En el Exterior, en Miles de $ 4.275
            d) Convenios con personas naturales
            - N° de Personas 17
            - Miles de $ 460.000
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 5
            - Miles de $ 71.919
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 23.957
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 72.251
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-VAP-PROG-08-GLO-06
          Content: |
            Incluye recursos para ser destinados a la adquisición de activos no financieros y a la ejecución de programas e iniciativas de inversión en los territorios insulares, proyectos de inversión de mejoramiento de obras portuarias, mantención y reparación que sean administradas por la empresa Sociedad Agrícola y Servicios Isla de Pascua (SASIPA) Sociedad por Acciones (Spa), que decida financiar el Gobierno Regional. En tales casos la unidad técnica será la empresa SASIPA. Estos proyectos podrán, dentro de sus objetivos, mejorar accesibilidad de servicios, el turismo y la recreación. El Gobierno Regional podrá efectuar transferencias a la Dirección de Obras Portuarias para financiar estudios de factibilidad e iniciativas que propendan al mejoramiento de la eficiencia del sistema portuario de los territorios insulares y podrá transferir los resultados y las obras en administración a SASIPA Sociedad por Acciones (SpA).
            Asimismo, se podrá financiar subsidios o aportes reembolsables a empresas de los sectores público o privado incluyendo a SASIPA Sociedad por Acciones (SpA), para proyectos de inversión de interés social en las áreas de electrificación, gas, generación de energía, telefonía celular y comunicaciones, en áreas rurales, y de agua potable y alcantarillado, previamente identificados de acuerdo al procedimiento que establece el artículo 19 bis del decreto ley N°1.263, de 1975.
            Los recursos que reciban las delegaciones presidenciales provinciales de Isla de Pascua y Valparaíso, para ser invertidos en los territorios insulares de la región, podrán aplicarse en la adquisición de activos no financieros, en iniciativas de inversión que cuenten con recomendación favorable del Ministerio de Desarrollo Social y Familia, en proyectos menores de 2.000 UTM y de conservación de infraestructura pública.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_OHiggins_Programa_09:
      ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09
      Region: "O'Higgins"
      Partida: "31"
      Capitulo: "01"
      Programa: "09"
      Asunto: "Gobierno Regional Región del Libertador General Bernardo O'higgins(07,08)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "96.010.047"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.050.906"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.050.906"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.050.906"]
          - ["09", "", "", "APORTE FISCAL", "", "55.273.604"]
          - ["09", "01", "", "Libre", "", "55.273.604"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "39.685.537"]
          - ["13", "02", "", "Del Gobierno Central", "", "39.685.537"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "1.119.486"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "1.202.029"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.920.840"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "116.838"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "19.123.418"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.146.000"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "13.056.926"]
          - ["24", "", "", "GASTOS", "", "96.010.047"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "6.498.326"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "6.498.326"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "6.498.326"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "89.511.721"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "89.511.721"]
          - ["33", "03", "150", "Inversión Regional", "06", "89.511.721"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.28.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-01
          Content: |
            Dotación máxima de vehículos 6
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-02
          Content: |
            Gastos en personal, en miles de $4.823.380
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 135
            b) Horas extraordinarias año
            - Miles de $ 24.819
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 44.552
            - En el Exterior, en Miles de $ 4.275
            d) Convenios con personas naturales
            - N° de Personas 5
            - Miles de $ 71.392
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 46.483
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 21.391
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 18.063
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-06
          Content: |
            El Gobierno Regional podrá financiar iniciativas de gastos de capital asociadas con el proyecto de ampliación de la Universidad de O´Higgins.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_07:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-07
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_08:
          ID: GN-LEY-PPTO-2026-P31-REG-OHI-PROG-09-GLO-08
          Content: |
            El Gobierno Regional de la Región del Libertador General Bernardo O’higgins, informará trimestralmente a la Comisión de Gobierno Interior, Nacionalidad, Ciudadanía y Regionalización de la Cámara de Diputados, sobre la cartera de proyectos a financiar. La información proporcionada deberá incluir detalles de localización geográfica, estado de avance, descripción de los proyectos, y entidades responsables de la ejecución. Además, se incluirá el monto de la inversión, los plazos de ejecución y los objetivos específicos a lograr.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Maule_Programa_10:
      ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10
      Region: "Maule"
      Partida: "31"
      Capitulo: "01"
      Programa: "10"
      Asunto: "Gobierno Regional Región del Maule(07)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "127.029.466"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.232.914"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.232.914"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.232.914"]
          - ["09", "", "", "APORTE FISCAL", "", "75.705.445"]
          - ["09", "01", "", "Libre", "", "75.705.445"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "50.091.107"]
          - ["13", "02", "", "Del Gobierno Central", "", "50.091.107"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "743.014"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "2.985.849"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.626.617"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "32"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "24.216.983"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.983.944"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "16.534.668"]
          - ["24", "", "", "GASTOS", "", "127.029.466"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.121.443"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.121.443"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.121.443"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "118.908.023"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "118.908.023"]
          - ["33", "03", "150", "Inversión Regional", "06", "118.908.023"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.37.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-01
          Content: |
            Dotación máxima de vehículos 6
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-02
          Content: |
            Gastos en personal, en miles de $5.829.780
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 166
            b) Horas extraordinarias año
            - Miles de $ 7.448
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 54.920
            - En el Exterior, en Miles de $ 8.550
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 5
            - Miles de $ 63.746
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 13.543
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 27.095
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-06
          Content: |
            El Gobierno Regional de la región del Maule informará a las Comisiones de Obras Públicas de ambas Cámaras, a los parlamentarios de la Región del Maule y a la Comisión Especial Mixta de Presupuestos, antes del 31 de enero de 2026, sobre la cartera de proyectos a financiar. La información proporcionada deberá incluir detalles de localización geográfica, estado de avance, descripción de los proyectos, y entidades responsables de la ejecución. Además, se incluirá el monto de la inversión, los plazos de ejecución y los objetivos específicos a lograr. Se suministrarán informes trimestrales a partir del 31 de marzo de 2026 para actualizar sobre los avances de los proyectos.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_07:
          ID: GN-LEY-PPTO-2026-P31-REG-MAU-PROG-10-GLO-07
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Biobio_Programa_11:
      ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11
      Region: "Biobío"
      Partida: "31"
      Capitulo: "01"
      Programa: "11"
      Asunto: "Gobierno Regional Región del Biobío(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "127.429.893"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.272.645"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.272.645"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.272.645"]
          - ["09", "", "", "APORTE FISCAL", "", "75.423.485"]
          - ["09", "01", "", "Libre", "", "75.423.485"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "50.733.763"]
          - ["13", "02", "", "Del Gobierno Central", "", "50.733.763"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "639.005"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "1.469.115"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.705.522"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "14.441"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "25.391.728"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "4.177.202"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "17.336.750"]
          - ["24", "", "", "GASTOS", "", "127.429.893"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "9.478.321"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "9.478.321"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "9.478.321"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "117.951.572"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "117.951.572"]
          - ["33", "03", "150", "Inversión Regional", "", "117.951.572"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.44.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-01
          Content: |
            Dotación máxima de vehículos 7
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-02
          Content: |
            Gastos en personal, en miles de $7.172.977
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 188
            b) Horas extraordinarias año
            - Miles de $ 29.784
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 89.103
            - En el Exterior, en Miles de $ 15.000
            d) Convenios con personas naturales
            - N° de Personas 7
            - Miles de $ 183.851
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 5
            - Miles de $ 69.070
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 42.840
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 45.157
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-BIO-PROG-11-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_La_Araucania_Programa_12:
      ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12
      Region: "Araucanía"
      Partida: "31"
      Capitulo: "01"
      Programa: "12"
      Asunto: "Gobierno Regional Región de La Araucanía(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "188.641.356"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.875.996"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.875.996"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.875.996"]
          - ["09", "", "", "APORTE FISCAL", "", "125.294.046"]
          - ["09", "01", "", "Libre", "", "125.294.046"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "61.471.314"]
          - ["13", "02", "", "Del Gobierno Central", "", "61.471.314"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "147.793"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "2.126.409"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "2.076.814"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "3.258"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "30.919.504"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "5.086.578"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "21.110.958"]
          - ["24", "", "", "GASTOS", "", "188.641.356"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.362.981"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.362.981"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.362.981"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "180.278.375"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "180.278.375"]
          - ["33", "03", "150", "Inversión Regional", "", "180.278.375"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.49.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-01
          Content: |
            Dotación máxima de vehículos 7
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-02
          Content: |
            Gastos en personal, en miles de $6.595.633
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 158
            b) Horas extraordinarias año
            - Miles de $ 5.956
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 69.303
            - En el Exterior, en Miles de $ 4.275
            d) Convenios con personas naturales
            - N° de Personas 9
            - Miles de $ 302.580
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 63.577
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 12.835
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 36.806
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-ARA-PROG-12-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Los_Lagos_Programa_13:
      ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13
      Region: "Los Lagos"
      Partida: "31"
      Capitulo: "01"
      Programa: "13"
      Asunto: "Gobierno Regional Región de Los Lagos(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "123.678.898"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "1.194.176"]
          - ["05", "02", "", "Del Gobierno Central", "", "1.194.176"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "1.194.176"]
          - ["09", "", "", "APORTE FISCAL", "", "75.784.912"]
          - ["09", "01", "", "Libre", "", "75.784.912"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "46.699.810"]
          - ["13", "02", "", "Del Gobierno Central", "", "46.699.810"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "255.307"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "2.268.623"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.426.343"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "3.521.920"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "21.235.317"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.493.429"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "14.498.871"]
          - ["24", "", "", "GASTOS", "", "123.678.898"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "9.103.790"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "9.103.790"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "9.103.790"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "114.575.108"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "114.575.108"]
          - ["33", "03", "150", "Inversión Regional", "", "114.575.108"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.38.55.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-01
          Content: |
            Dotación máxima de vehículos 6
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-02
          Content: |
            Gastos en personal, en miles de $6.821.700
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 177
            b) Horas extraordinarias año
            - Miles de $ 5.311
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 61.773
            - En el Exterior, en Miles de $ 1.235
            d) Convenios con personas naturales
            - N° de Personas 5
            - Miles de $ 111.747
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 70.917
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 30.802
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 25.534
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-LLA-PROG-13-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Aysen_Programa_14:
      ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14
      Region: "Aysén"
      Partida: "31"
      Capitulo: "01"
      Programa: "14"
      Asunto: "Gobierno Regional Región de Aysén del General Carlos Ibáñez del Campo"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "90.284.722"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "846.314"]
          - ["05", "02", "", "Del Gobierno Central", "", "846.314"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "846.314"]
          - ["09", "", "", "APORTE FISCAL", "", "58.101.926"]
          - ["09", "01", "", "Libre", "", "58.101.926"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "31.336.482"]
          - ["13", "02", "", "Del Gobierno Central", "", "31.336.482"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "573.189"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "1.208.534"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "983.623"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "1.519.285"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "14.644.138"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "2.409.112"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "9.998.601"]
          - ["24", "", "", "GASTOS", "", "90.284.722"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.417.996"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.417.996"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.417.996"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "81.866.726"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "81.866.726"]
          - ["33", "03", "150", "Inversión Regional", "06", "81.866.726"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.02.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-02
          Content: |
            Gastos en personal, en miles de $6.763.065
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 143
            b) Horas extraordinarias año
            - Miles de $ 12.906
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 59.402
            - En el Exterior, en Miles de $ 4.275
            d) Convenios con personas naturales
            - N° de Personas 13
            - Miles de $ 222.735
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 52.610
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 10.268
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 58.705
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-AYS-PROG-14-GLO-06
          Content: |
            El Gobierno Regional deberá informar semestralmente a la Comisión Especial Mixta de Presupuestos sobre los proyectos de inversión financiados con esta Asignación, identificando el efecto empleo en la región.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Magallanes_Programa_15:
      ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15
      Region: "Magallanes"
      Partida: "31"
      Capitulo: "01"
      Programa: "15"
      Asunto: "Gobierno Regional Región de Magallanes y de la Antártica Chilena"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "90.994.887"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "757.786"]
          - ["05", "02", "", "Del Gobierno Central", "", "757.786"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "757.786"]
          - ["09", "", "", "APORTE FISCAL", "", "48.395.656"]
          - ["09", "01", "", "Libre", "", "48.395.656"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "41.841.445"]
          - ["13", "02", "", "Del Gobierno Central", "", "41.841.445"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "225.520"]
          - ["13", "02", "007", "Tesoro Público Ley N°19.275, Fondo de Desarrollo de Magallanes", "", "11.690.896"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "237.602"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.018.022"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "671.521"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "15.156.260"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "2.493.361"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "10.348.263"]
          - ["24", "", "", "GASTOS", "", "90.994.887"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "8.336.365"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "8.336.365"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "8.336.365"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "82.658.522"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "82.658.522"]
          - ["33", "03", "120", "Fondo de Desarrollo de Magallanes", "", "11.690.896"]
          - ["33", "03", "150", "Inversión Regional", "", "70.967.626"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.08.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-GLO-02
          Content: |
            Gastos en personal, en miles de $6.144.017
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 134
            b) Horas extraordinarias año
            - Miles de $ 15.649
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 71.795
            - En el Exterior, en Miles de $ 8.550
            d) Convenios con personas naturales
            - N° de Personas 7
            - Miles de $ 307.541
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 3
            - Miles de $ 43.777
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 11.392
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-MAG-PROG-15-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 17.399
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Metropolitana_Programa_16:
      ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16
      Region: "Metropolitana"
      Partida: "31"
      Capitulo: "01"
      Programa: "16"
      Asunto: "Gobierno Regional Región Metropolitana de Santiago(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "208.994.880"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "2.016.392"]
          - ["05", "02", "", "Del Gobierno Central", "", "2.016.392"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "2.016.392"]
          - ["09", "", "", "APORTE FISCAL", "", "113.017.576"]
          - ["09", "01", "", "Libre", "", "113.017.576"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "93.960.912"]
          - ["13", "02", "", "Del Gobierno Central", "", "93.960.912"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "3.066.774"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "4.579.804"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "3.412.689"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "153.288"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "44.794.655"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "7.369.184"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "30.584.518"]
          - ["24", "", "", "GASTOS", "", "208.994.880"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "12.255.805"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "12.255.805"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "12.255.805"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "196.739.075"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "196.739.075"]
          - ["33", "03", "150", "Inversión Regional", "", "196.739.075"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.15.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-01
          Content: |
            Dotación máxima de vehículos 6
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-02
          Content: |
            Gastos en personal, en miles de $9.402.278
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 223
            b) Horas extraordinarias año
            - Miles de $ 69.494
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 11.882
            - En el Exterior, en Miles de $ 23.085
            d) Convenios con personas naturales
            - N° de Personas 26
            - Miles de $ 897.039
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 8
            - Miles de $ 92.096
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 34.225
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 5.017
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-MET-PROG-16-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Los_Rios_Programa_17:
      ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17
      Region: "Los Ríos"
      Partida: "31"
      Capitulo: "01"
      Programa: "17"
      Asunto: "Gobierno Regional Región de Los Ríos(06,07)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "85.160.781"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "820.380"]
          - ["05", "02", "", "Del Gobierno Central", "", "820.380"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "820.380"]
          - ["09", "", "", "APORTE FISCAL", "", "57.835.189"]
          - ["09", "01", "", "Libre", "", "57.835.189"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "26.505.212"]
          - ["13", "02", "", "Del Gobierno Central", "", "26.505.212"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "150.945"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "2.962.972"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "819.019"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "47.407"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "12.193.520"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "2.005.960"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "8.325.389"]
          - ["24", "", "", "GASTOS", "", "85.160.781"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "7.262.137"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "7.262.137"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "7.262.137"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "77.898.644"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "77.898.644"]
          - ["33", "03", "150", "Inversión Regional", "", "77.898.644"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.23.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-02
          Content: |
            Gastos en personal, en miles de $5.707.506
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 147
            b) Horas extraordinarias año
            - Miles de $ 14.891
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 69.303
            - En el Exterior, en Miles de $ 5.985
            d) Convenios con personas naturales
            - N° de Personas 7
            - Miles de $ 122.118
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 4
            - Miles de $ 72.028
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 15.133
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 27.095
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_07:
          ID: GN-LEY-PPTO-2026-P31-REG-LRI-PROG-17-GLO-07
          Content: |
            Se informará trimestralmente a la Cámara de Diputados sobre los avances en la planificación, acciones y desarrollo de las inversiones y proyectos destinados exclusivamente al Plan Bicentenario de Chiloé que se conmemorará el año 2026.
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Arica_y_Parinacota_Programa_18:
      ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18
      Region: "Arica y Parinacota"
      Partida: "31"
      Capitulo: "01"
      Programa: "18"
      Asunto: "Gobierno Regional Región de Arica y Parinacota"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "63.927.888"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "595.047"]
          - ["05", "02", "", "Del Gobierno Central", "", "595.047"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "595.047"]
          - ["09", "", "", "APORTE FISCAL", "", "39.429.162"]
          - ["09", "01", "", "Libre", "", "39.429.162"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "23.903.679"]
          - ["13", "02", "", "Del Gobierno Central", "", "23.903.679"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "1.097.872"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "51.491"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "798.160"]
          - ["13", "02", "020", "Tesoro Público Ley N°18.892, Patentes de Acuicultura", "", "4.976"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "11.882.961"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "1.954.870"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "8.113.349"]
          - ["24", "", "", "GASTOS", "", "63.927.888"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "7.065.360"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "7.065.360"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "7.065.360"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "56.862.528"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "56.862.528"]
          - ["33", "03", "150", "Inversión Regional", "", "56.862.528"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.28.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-GLO-02
          Content: |
            Gastos en personal, en miles de $5.558.914
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 144
            b) Horas extraordinarias año
            - Miles de $ 17.870
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 29.702
            - En el Exterior, en Miles de $ 8.550
            d) Convenios con personas naturales
            - N° de Personas 16
            - Miles de $ 267.937
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 3
            - Miles de $ 48.111
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 12.835
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-ARI-PROG-18-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 46.162
          Src: "staging/ppto_2026_p31/p31.md"

    Region_Nuble_Programa_19:
      ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19
      Region: "Ñuble"
      Partida: "31"
      Capitulo: "01"
      Programa: "19"
      Asunto: "Gobierno Regional Región de Ñuble(06)"
      Unidad_Monetaria: "Miles de $"
      Tabla_Presupuesto:
        ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-T01
        Columns:
          - "Sub-Título"
          - "Ítem"
          - "Asig."
          - "Denominaciones"
          - "Glosa N°"
          - "Moneda Nacional (Miles de $)"
        Rows:
          - ["05", "", "", "INGRESOS", "", "91.383.538"]
          - ["05", "", "", "TRANSFERENCIAS CORRIENTES", "", "881.003"]
          - ["05", "02", "", "Del Gobierno Central", "", "881.003"]
          - ["05", "02", "029", "Subsecretaría de las Culturas y las Artes", "", "881.003"]
          - ["09", "", "", "APORTE FISCAL", "", "53.546.906"]
          - ["09", "01", "", "Libre", "", "53.546.906"]
          - ["13", "", "", "TRANSFERENCIAS PARA GASTOS DE CAPITAL", "", "36.955.629"]
          - ["13", "02", "", "Del Gobierno Central", "", "36.955.629"]
          - ["13", "02", "006", "Tesoro Público Ley N°19.143, Patentes Mineras", "", "299.326"]
          - ["13", "02", "013", "Tesoro Público Artículo 129 bis Ley N°20.017, Código de Aguas", "", "682.846"]
          - ["13", "02", "019", "Fondo de Inversión y Reconversión Regional", "", "1.262.128"]
          - ["13", "02", "030", "Fondo de Apoyo al Transporte Público y la Conectividad Regional", "", "18.790.488"]
          - ["13", "02", "040", "Tesoro Público Ley N°21.210, Modernización Tributaria", "", "3.091.230"]
          - ["13", "02", "060", "Fondo de Productividad y Desarrollo", "", "12.829.611"]
          - ["24", "", "", "GASTOS", "", "91.383.538"]
          - ["24", "", "", "TRANSFERENCIAS CORRIENTES", "", "5.631.207"]
          - ["24", "03", "", "A Otras Entidades Públicas", "", "5.631.207"]
          - ["24", "03", "150", "Funcionamiento Regional", "01,02,03,04,05", "5.631.207"]
          - ["33", "", "", "TRANSFERENCIAS DE CAPITAL", "", "85.752.331"]
          - ["33", "03", "", "A Otras Entidades Públicas", "", "85.752.331"]
          - ["33", "03", "150", "Inversión Regional", "07", "85.752.331"]
        Src:
          - "staging/ppto_2026_p31/Vista Previa 2025-12-12 16.39.38.png"
          - "staging/ppto_2026_p31/p31.md"
      Glosas:
        Glosa_01:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-01
          Content: |
            Dotación máxima de vehículos 5
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_02:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-02
          Content: |
            Gastos en personal, en miles de $ 4.222.003
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_03:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-03
          Content: |
            Incluye:
            a) Dotación máxima de personal 101
            b) Horas extraordinarias año
            - Miles de $ 9.928
            c) Autorización máxima para gastos en viáticos
            - En Territorio Nacional, en Miles de $ 19.802
            - En el Exterior, en Miles de $ 17.100
            d) Convenios con personas naturales
            - N° de Personas 3
            - Miles de $ 115.294
            e) Autorización máxima para cumplimiento artículo septuagésimo tercero de la Ley N° 19.882, Asignación por Funciones Críticas:
            - N° de personas 2
            - Miles de $ 23.242
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_04:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-04
          Content: |
            Incluye:
            Capacitación y perfeccionamiento, D.F.L. N°1 / 19.653, de 2001, Ministerio Secretaría General de la Presidencia
            - Miles de $ 12.835
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_05:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-05
          Content: |
            Monto máximo para gastos en el ítem de publicidad Miles de $ 84.272
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_06:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-06
          Content: |
            El Gobierno Regional informará trimestralmente a la Comisión Especial Mixta de Presupuestos sobre los convenios que se suscriban y montos que se destinan para la compra y distribución de agua vía camiones aljibe u otros medios similares, con indicación de las comunas de la región, la población beneficiada, y las políticas o acciones llevadas a cabo para incentivar la competencia e incorporación de nuevos actores que puedan proveer de este servicio a la población regional.
          Src: "staging/ppto_2026_p31/p31.md"
        Glosa_07:
          ID: GN-LEY-PPTO-2026-P31-REG-NUB-PROG-19-GLO-07
          Content: |
            El Gobierno Regional informará trimestralmente a las Comisiones de Economía del Senado y de Comisión de Economía, Fomento; Micro, Pequeña y Mediana Empresa; Protección de los Consumidores y Turismo de la Cámara de Diputados sobre los proyectos de inversión que se implementarán en la Región de Ñuble y el efecto en la generación de empleo regional.
          Src: "staging/ppto_2026_p31/p31.md"
