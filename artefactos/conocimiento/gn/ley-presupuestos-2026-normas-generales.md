---
urn: urn:gn:kb:ley-presupuestos-2026-normas-generales
nombre: ley-presupuestos-2026-normas-generales
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre ley presupuestos 2026 normas generales; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml (sha256:990bfd73f1f762c3d9c3958603921bb2b8eec945af4517fca1535789c0833017); URN KODA legado urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-14
lang: es
tags: [gn, gore-os, koda, ley, presupuestos, "2026", normas, generales]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml"
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

ID: GN-LEY-PPTO-2026-NORMAS-GENERALES-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-12-14
Modification-Date: 2025-12-15
Primary-Source: staging/ppto_2026.md
Ctx: "Ley N° 21.796: Ley de Presupuestos del Sector Público correspondiente al año 2026. Normas Generales."

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

Ley_de_Presupuestos_Sector_Publico_2026:
  ID: GN-LEY-PPTO-2026-NORMAS-GENERALES
  Ley:
    Numero: "21.796"
    Titulo: "LEY DE PRESUPUESTOS DEL SECTOR PÚBLICO CORRESPONDIENTE AL AÑO 2026"
    Fuente:
      Src: "DIARIO OFICIAL DE LA REPUBLICA DE CHILE"
      Fecha: "Viernes 12 de Diciembre de 2025"
      CVE: "2741100"
  Definiciones_Reutilizables:
    - ID: CEMP
      Def: "Comisión Especial Mixta de Presupuestos"
    - ID: BCN
      Def: "Biblioteca del Congreso Nacional"
    - ID: DIPRES
      Def: "Dirección de Presupuestos"
    - ID: CGR
      Def: "Contraloría General de la República"
    - ID: P30TERM
      Def: "dentro de los treinta días siguientes al término"
    - ID: DL1263
      Def: "decreto ley N° 1.263, de 1975"
    - ID: DL1263_ART19BIS
      Def: "artículo 19 bis del decreto ley N° 1.263, de 1975"
    - ID: DL1263_ART70
      Def: "artículo 70 del decreto ley N° 1.263, de 1975"
    - ID: LEY20285
      Def: "ley N° 20.285, sobre Acceso a la Información Pública"
    - ID: LEY19886
      Def: "ley N° 19.886, de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios"
    - ID: LEY18834
      Def: "ley N° 18.834, sobre Estatuto Administrativo"
    - ID: LEY19862
      Def: "ley N° 19.862, sobre Registro de Personas Jurídicas Receptoras de Fondos Públicos"
    - ID: MINHACIENDA
      Def: "Ministerio de Hacienda"
    - ID: UTM
      Def: "unidades tributarias mensuales"
    - ID: LEY19983
      Def: "ley N° 19.983, que regula la transferencia y otorga mérito ejecutivo a copia de la factura"
    - ID: DFL29_2004
      Def: "decreto con fuerza de ley N° 29, de 2004, del Ministerio de Hacienda"
    - ID: DFL29_2004_ART151
      Def: "artículo 151 del decreto con fuerza de ley N° 29, de 2004, del Ministerio de Hacienda"
    - ID: MINREL
      Def: "Ministerio de Relaciones Exteriores"
    - ID: SEGEGOB
      Def: "Ministerio Secretaría General de Gobierno"
    - ID: CPLT
      Def: "Consejo para la Transparencia"
    - ID: LEY18045
      Def: "ley N° 18.045"
    - ID: LEY19896
      Def: "ley N° 19.896"
    - ID: LEY21730
      Def: "ley N° 21.730"
    - ID: LEY20128
      Def: "ley N° 20.128"
    - ID: DL3001_1979
      Def: "decreto ley N° 3.001, de 1979"
    - ID: DL1056_1975
      Def: "decreto ley N° 1.056, de 1975"
    - ID: LEY18382
      Def: "ley N° 18.382"
    - ID: LEY19104
      Def: "ley N° 19.104"
    - ID: LEY19300
      Def: "ley N° 19.300"
    - ID: DS900_1996_MOP
      Def: "decreto 900, de 1996, del Ministerio de Obras Públicas"
    - ID: DFL164_1991_MOP
      Def: "decreto con fuerza de ley N° 164, de 1991, del Ministerio de Obras Públicas"
    - ID: RES30_2015_CGR
      Def: "resolución N° 30, de 2015, de la Contraloría General de la República"
    - ID: TGR
      Def: "Tesorería General de la República"
    - ID: ISAPRE
      Def: "Institución de Salud Previsional"
    - ID: CAIGG
      Def: "Consejo de Auditoría Interna General de Gobierno"
    - ID: TVN
      Def: "Televisión Nacional de Chile"
    - ID: CODELCO
      Def: "Corporación Nacional del Cobre de Chile"
    - ID: BANCOESTADO
      Def: "Banco del Estado de Chile"
    - ID: LEY18575
      Def: "ley N° 18.575, orgánica constitucional de Bases Generales de la Administración del Estado"
    - ID: DFL1_19653_2000
      Def: "decreto con fuerza de ley N° 1-19.653, de 2000, del Ministerio Secretaría General de la Presidencia"
    - ID: LEY18918
      Def: "ley N° 18.918, orgánica constitucional del Congreso Nacional"
    - ID: DL1263_ART28
      Def: "artículo 28 del decreto ley N° 1.263, de 1975"
    - ID: LEY21174
      Def: "ley N° 21.174"
    - ID: LEY18948
      Def: "ley N° 18.948"
    - ID: LEY19863
      Def: "ley N° 19.863"
    - ID: LEY19908
      Def: "ley N° 19.908"
    - ID: LEY16282
      Def: "ley N° 16.282"
    - ID: LEY21364
      Def: "ley N° 21.364"
    - ID: LEY21040
      Def: "ley N° 21.040"
    - ID: MINEDUC
      Def: "Ministerio de Educación"
    - ID: DS162_2022_MINEDUC
      Def: "decreto N° 162, de 2022, del Ministerio de Educación"
    - ID: MDSF
      Def: "Ministerio de Desarrollo Social y Familia"
    - ID: DS2_2024_MDSF
      Def: "decreto supremo N° 2, de 2024, del Ministerio de Desarrollo Social y Familia"
    - ID: SUBINT
      Def: "Subsecretaría del Interior"
    - ID: SENAPRED
      Def: "Servicio Nacional de Prevención y Respuesta ante Desastres"
    - ID: INDAP
      Def: "Instituto de Desarrollo Agropecuario"
    - ID: SAG
      Def: "Servicio Agrícola y Ganadero"
    - ID: SERCOTEC
      Def: "Servicio de Cooperación Técnica"
    - ID: SUBAGRI
      Def: "Subsecretaría de Agricultura"
    - ID: DL1263_ART6
      Def: "artículo 6° del decreto ley N° 1.263, de 1975"
    - ID: LEY18575_ART5_INC2
      Def: "inciso segundo del artículo 5° de la ley N° 18.575"
    - ID: LEY20903
      Def: "ley N° 20.903"
    - ID: DFL1_1996_MINEDUC
      Def: "decreto con fuerza de ley N° 1, de 1996, del Ministerio de Educación"
    - ID: DFL1_1996_ART19K
      Def: "artículo 19K del decreto con fuerza de ley N° 1, de 1996, del Ministerio de Educación"
    - ID: DFL1_1996_ART19Q
      Def: "artículo 19Q del decreto con fuerza de ley N° 1, de 1996, del Ministerio de Educación"
    - ID: SUPEREDUC
      Def: "Superintendencia de Educación"
    - ID: MININTERIOR
      Def: "Ministerio del Interior"
    - ID: LEY21543
      Def: "ley N° 21.543"
    - ID: FGE
      Def: "Fondo de Garantías Especiales"
    - ID: LEY21325
      Def: "ley N° 21.325, de Migración y Extranjería"
    - ID: LEY21600
      Def: "ley N° 21.600"
    - ID: LEY20248
      Def: "ley N° 20.248"
    - ID: DFL2_1998_MINEDUC
      Def: "decreto con fuerza de ley N° 2, de 1998, del Ministerio de Educación"
    - ID: DL3063_1979
      Def: "decreto ley N° 3.063, de 1979, sobre Rentas Municipales"
    - ID: DS2385_1996_MININTERIOR
      Def: "decreto supremo N° 2.385, de 1996, del Ministerio del Interior"
    - ID: SUBDERE
      Def: "Subsecretaría de Desarrollo Regional y Administrativo"
    - ID: SUBEDUC
      Def: "Subsecretaría de Educación"
    - ID: FCM
      Def: "Fondo Común Municipal"
    - ID: CPC
      Def: "Código de Procedimiento Civil"
  Preambulo:
    ID: GN-LEY-PPTO-2026-PREAMBULO-01
    Contenido: |-
      I
      SECCIÓN
      LEYES, REGLAMENTOS, DECRETOS Y RESOLUCIONES DE ORDEN GENERAL
      Normas Generales
      MINISTERIO DE HACIENDA
      LEY NÚM. 21.796
      LEY DE PRESUPUESTOS DEL SECTOR PÚBLICO
      CORRESPONDIENTE AL AÑO 2026
      Teniendo presente que el H. Congreso Nacional ha dado su aprobación al siguiente
      Proyecto de ley:
  Articulos:
    Articulo_01:
      ID: GN-LEY-PPTO-2026-ART01
      Purp: Aprobar Presupuesto Ingresos y Gastos Sector Público 2026.
      Presupuesto_Moneda_Nacional:
        ID: GN-LEY-PPTO-2026-ART01-MN
        Unidad: Miles de $
        Ingresos:
          ID: GN-LEY-PPTO-2026-ART01-MN-ING
          Total_Resumen: 98.173.137.392
          Deducciones_Transferencias: 3.365.139.677
          Total_Neto: 94.807.997.715
          Detalle:
            - Concepto: IMPUESTOS
              Resumen_Partidas: 67.592.676.590
              Deducciones: null
              Total: 67.592.676.590
            - Concepto: IMPOSICIONES PREVISIONALES
              Resumen_Partidas: 3.909.386.418
              Deducciones: null
              Total: 3.909.386.418
            - Concepto: TRANSFERENCIAS CORRIENTES
              Resumen_Partidas: 1.622.734.866
              Deducciones: 1.584.091.522
              Total: 38.643.344
            - Concepto: RENTAS DE LA PROPIEDAD
              Resumen_Partidas: 1.202.172.520
              Deducciones: null
              Total: 1.202.172.520
            - Concepto: INGRESOS DE OPERACIÓN
              Resumen_Partidas: 1.269.297.707
              Deducciones: null
              Total: 1.269.297.707
            - Concepto: OTROS INGRESOS CORRIENTES
              Resumen_Partidas: 3.703.738.501
              Deducciones: null
              Total: 3.703.738.501
            - Concepto: VENTA DE ACTIVOS NO FINANCIEROS
              Resumen_Partidas: 10.596.573
              Deducciones: null
              Total: 10.596.573
            - Concepto: VENTA DE ACTIVOS FINANCIEROS
              Resumen_Partidas: -1.216.034.984
              Deducciones: null
              Total: -1.216.034.984
            - Concepto: RECUPERACIÓN DE PRÉSTAMOS
              Resumen_Partidas: 1.657.992.008
              Deducciones: null
              Total: 1.657.992.008
            - Concepto: TRANSFERENCIAS PARA GASTOS DE CAPITAL
              Resumen_Partidas: 1.801.320.105
              Deducciones: 1.781.048.155
              Total: 20.271.950
            - Concepto: ENDEUDAMIENTO
              Resumen_Partidas: 16.604.590.449
              Deducciones: null
              Total: 16.604.590.449
            - Concepto: SALDO INICIAL DE CAJA
              Resumen_Partidas: 14.666.639
              Deducciones: null
              Total: 14.666.639
        Gastos:
          ID: GN-LEY-PPTO-2026-ART01-MN-GAS
          Total_Resumen: 98.173.137.392
          Deducciones_Transferencias: 3.365.139.677
          Total_Neto: 94.807.997.715
          Detalle:
            - Concepto: GASTOS EN PERSONAL
              Resumen_Partidas: 17.124.393.592
              Deducciones: null
              Total: 17.124.393.592
            - Concepto: BIENES Y SERVICIOS DE CONSUMO
              Resumen_Partidas: 6.666.677.160
              Deducciones: null
              Total: 6.666.677.160
            - Concepto: PRESTACIONES DE SEGURIDAD SOCIAL
              Resumen_Partidas: 16.015.546.743
              Deducciones: null
              Total: 16.015.546.743
            - Concepto: TRANSFERENCIAS CORRIENTES
              Resumen_Partidas: 29.829.223.314
              Deducciones: 1.039.105.570
              Total: 28.790.117.744
            - Concepto: INTEGROS AL FISCO
              Resumen_Partidas: 578.591.428
              Deducciones: 544.985.952
              Total: 33.605.476
            - Concepto: OTROS GASTOS CORRIENTES
              Resumen_Partidas: 39.977.244
              Deducciones: null
              Total: 39.977.244
            - Concepto: ADQUISICIÓN DE ACTIVOS NO FINANCIEROS
              Resumen_Partidas: 354.577.240
              Deducciones: null
              Total: 354.577.240
            - Concepto: ADQUISICIÓN DE ACTIVOS FINANCIEROS
              Resumen_Partidas: 2.078.114.027
              Deducciones: null
              Total: 2.078.114.027
            - Concepto: INICIATIVAS DE INVERSIÓN
              Resumen_Partidas: 4.760.596.621
              Deducciones: null
              Total: 4.760.596.621
            - Concepto: PRÉSTAMOS
              Resumen_Partidas: 2.900.239.419
              Deducciones: null
              Total: 2.900.239.419
            - Concepto: TRANSFERENCIAS DE CAPITAL
              Resumen_Partidas: 9.393.255.741
              Deducciones: 1.781.048.155
              Total: 7.612.207.586
            - Concepto: SERVICIO DE LA DEUDA
              Resumen_Partidas: 8.418.942.393
              Deducciones: null
              Total: 8.418.942.393
            - Concepto: SALDO FINAL DE CAJA
              Resumen_Partidas: 13.002.470
              Deducciones: null
              Total: 13.002.470
      Presupuesto_Moneda_Extranjera:
        ID: GN-LEY-PPTO-2026-ART01-ME
        Unidad: Miles de US$
        Ingresos:
          ID: GN-LEY-PPTO-2026-ART01-ME-ING
          Total_Resumen: 12.368.561
          Deducciones_Transferencias: 20
          Total_Neto: 12.368.541
          Detalle:
            - Concepto: IMPUESTOS
              Resumen_Partidas: 308.200
              Deducciones: null
              Total: 308.200
            - Concepto: TRANSFERENCIAS CORRIENTES
              Resumen_Partidas: null
              Deducciones: 20
              Total: 20
            - Concepto: RENTAS DE LA PROPIEDAD
              Resumen_Partidas: 1.797.058
              Deducciones: null
              Total: 1.797.058
            - Concepto: INGRESOS DE OPERACIÓN
              Resumen_Partidas: 5.239
              Deducciones: null
              Total: 5.239
            - Concepto: OTROS INGRESOS CORRIENTES
              Resumen_Partidas: 16.552
              Deducciones: null
              Total: 16.552
            - Concepto: VENTA DE ACTIVOS NO FINANCIEROS
              Resumen_Partidas: 10
              Deducciones: null
              Total: 10
            - Concepto: VENTA DE ACTIVOS FINANCIEROS
              Resumen_Partidas: 10.112.541
              Deducciones: null
              Total: 10.112.541
            - Concepto: RECUPERACIÓN DE PRÉSTAMOS
              Resumen_Partidas: 2.375
              Deducciones: null
              Total: 2.375
            - Concepto: ENDEUDAMIENTO
              Resumen_Partidas: 124.526
              Deducciones: null
              Total: 124.526
            - Concepto: SALDO INICIAL DE CAJA
              Resumen_Partidas: 2.040
              Deducciones: null
              Total: 2.040
        Gastos:
          ID: GN-LEY-PPTO-2026-ART01-ME-GAS
          Total_Resumen: 12.368.561
          Deducciones_Transferencias: 20
          Total_Neto: 12.368.541
          Detalle:
            - Concepto: GASTOS EN PERSONAL
              Resumen_Partidas: 140.724
              Deducciones: null
              Total: 140.724
            - Concepto: BIENES Y SERVICIOS DE CONSUMO
              Resumen_Partidas: 141.591
              Deducciones: null
              Total: 141.591
            - Concepto: PRESTACIONES DE SEGURIDAD SOCIAL
              Resumen_Partidas: 375
              Deducciones: null
              Total: 375
            - Concepto: TRANSFERENCIAS CORRIENTES
              Resumen_Partidas: 97.003
              Deducciones: null
              Total: 97.003
            - Concepto: INTEGROS AL FISCO
              Resumen_Partidas: null
              Deducciones: 20
              Total: 20
            - Concepto: OTROS GASTOS CORRIENTES
              Resumen_Partidas: 110
              Deducciones: null
              Total: 110
            - Concepto: ADQUISICIÓN DE ACTIVOS NO FINANCIEROS
              Resumen_Partidas: 2.676
              Deducciones: null
              Total: 2.676
            - Concepto: ADQUISICIÓN DE ACTIVOS FINANCIEROS
              Resumen_Partidas: 8.467.195
              Deducciones: null
              Total: 8.467.195
            - Concepto: INICIATIVAS DE INVERSIÓN
              Resumen_Partidas: 414
              Deducciones: null
              Total: 414
            - Concepto: PRÉSTAMOS
              Resumen_Partidas: 2.375
              Deducciones: null
              Total: 2.375
            - Concepto: SERVICIO DE LA DEUDA
              Resumen_Partidas: 3.514.078
              Deducciones: null
              Total: 3.514.078
            - Concepto: SALDO FINAL DE CAJA
              Resumen_Partidas: 2.000
              Deducciones: null
              Total: 2.000
    Articulo_02:
      ID: GN-LEY-PPTO-2026-ART02
      Purp: Autorizar garantía estatal a créditos/bonos empresas públicas y universidades estatales.
      Garantia_Estatal:
        Monto_Maximo: US$500.000.000
        Equivalencia: otras monedas extranjeras o moneda nacional
        Beneficiarios:
          - Empresas del Sector Público
          - Universidades estatales
        Cobertura: capital, reajustes, intereses, comisiones, contratos canje monedas, demás gastos
        Mecanismo:
          Act: Decretos supremos expedidos por
          Ref: MINHACIENDA
        Req_Empresas: Convenio programación con Comité Sistema Empresas CORFO (objetivos, resultados, programa inversiones)
      Emprestitos_Universidades_Estatales:
        Plazo_Maximo: 20 años
        Limite_Endeudamiento: 100% del patrimonio
        Fines_Permitidos:
          - Capital de trabajo
          - Remuneraciones (excepto incrementos)
          - Refinanciamiento pasivos
          - Proyectos inversión
        Req:
          - "Visación previa"
          - "Propuesta pública para selección entidades financieras"
        Ref: MINHACIENDA
        Plazos_Visacion:
          General: 90 días corridos desde recepción antecedentes
          Vencimiento_Periodo_Presidencial: 20 días corridos
        Prohib:
          Desc: No sujeta a
          Ref: LEY19886
        Informe_Obligatorio:
          Destinatarios:
            - Ministerio de Educación
            - CEMP
            - DIPRES
          Plazo: 10 días siguientes a contratación
          Contenido: monto, condiciones, objetivos, resultados esperados
    Articulo_03:
      ID: GN-LEY-PPTO-2026-ART03
      Purp: Autorizar endeudamiento público 2026.
      Autorizacion_Endeudamiento:
        Monto_Principal: US$17.400.000 miles
        Concepto: Ingresos Generales de la Nación
        Monto_Adicional: US$600.000 miles
        Ambito: país o exterior, moneda nacional o extranjera
      Instrumentos:
        Tipos:
          - Bonos
          - Otros documentos
        Firma: Tesorero General de la República (impresa)
      Exclusiones_Computo:
        - Obligaciones amortizadas dentro ejercicio 2026
        - Pago anticipado deudas ejercicios anteriores (deducidas amortizaciones 2026)
      Mecanismo:
        Act: Decretos supremos expedidos por
        Ref: MINHACIENDA
        Contenido: destino específico, fuentes recursos servicio deuda
        Informe:
          Destinatarios: Comisiones Hacienda Senado y Cámara Diputados
          Plazo: 15 días siguientes a total tramitación
    Articulo_04:
      ID: GN-LEY-PPTO-2026-ART04
      Purp: Establecer límites incremento gastos corrientes y de capital.
      Ctx:
        Ref: DL1263
      Gastos_Corrientes:
        Req: Autorización legal para incrementar suma valor neto
        Subtitulos_Afectos:
          - Gastos en personal
          - Bienes y servicios de consumo
          - Prestaciones de seguridad social
          - Transferencias corrientes
          - Otros gastos corrientes
        Excepciones:
          - Ítems legalmente excedibles (art. 28 DL 1.263)
          - Glosa 01 Programa Operaciones Complementarias
          - Mayores saldos iniciales caja (excepto Partida Tesoro Público)
          - Venta activos financieros
          - Ingresos propios asignables
          - Recursos fondos concursables entes públicos
          - Art. 21 DL 1.263
      Gastos_Capital:
        Req: Autorización legal para aumentar >10% suma aprobada Art.1
        Subtitulos_Afectos:
          - Adquisición activos no financieros
          - Iniciativas de inversión
          - Transferencias capital a organismos/empresas no incluidas
        Excepciones:
          - Reasignaciones presupuestarias desde gastos corrientes
          - Mayores saldos iniciales caja (excepto Tesoro Público)
          - Venta activos
          - Fondos concursables
          - Recuperación anticipos
        Limite_Empresas: Aportes pueden elevarse hasta 10%
      FEES:
        Def: Fondo de Estabilización Económica y Social (ley N° 20.128)
        Req: Autorización legal si uso acumulado anual >0,3% PIB
    Articulo_05:
      ID: GN-LEY-PPTO-2026-ART05
      Purp: Suspender compatibilidad planta-contrata 2026.
      Suspension:
        Norma_Suspendida: letra d) artículo 87
        Ref: LEY18834
        Materia: Compatibilidad cargos planta con designación contrata
        Vigencia: Año 2026
      Prohib: Contratar personal suplente en cargos planta no desempeñados por titular (por aplicación mecanismo anterior)
      Excepcion: Personas usando excepciones al momento publicación ley
    Articulo_06:
      ID: GN-LEY-PPTO-2026-ART06
      Purp: Establecer umbrales licitación pública inversión 2026.
      Licitacion_Publica_Obligatoria:
        Umbrales_Generales:
          Proyectos_Programas_Inversion: ">1.000 UTM"
          Estudios_Basicos: ">500 UTM"
        Umbrales_MOP_MINVU:
          Proyectos_Programas_Inversion: ">10.000 UTM"
          Estudios_Basicos: ">3.000 UTM"
        Excepcion: Situaciones emergencia según legislación
      Montos_Inferiores:
        Proc: DS N° 151/2003 Ministerio de Hacienda
      Sanciones_Contratistas:
        Cond: Incumplimiento leyes laborales/previsionales (determinado autoridad competente)
        Res: Calificación nota deficiente área administración contrato
        Res_Adicional: Registro para futuras licitaciones
      Req_Instituciones_Privadas:
        Req: Certificado cumplimiento obligaciones laborales y remuneración
        Prohib: Contratar con Estado si incumplimiento registrado o sin certificado
    Articulo_07:
      ID: GN-LEY-PPTO-2026-ART07
      Purp: Reglas para decretos con transferencias (Subtítulos 24 y 33).
      Ctx_Transferencias:
        Cond: Dispuestas en esta ley o creadas en virtud del artículo 26
        Ref: DL1263
      Decretos_Transferencias:
        Subtitulos:
          - "Subtítulo 24: Transferencias Corrientes"
          - "Subtítulo 33: Transferencias de Capital"
        Puede_Indicar:
          - Uso o destino que la institución receptora deberá dar a los recursos
          - Condiciones o modalidades de reintegro
          - Información sobre aplicación a remitir y organismo destinatario
      Transferencias_Subtitulo24_Unidades_Programas:
        Cond: Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste
        Req:
          Desc: Desglose previo a la ejecución presupuestaria en conceptos de gasto
          Ref: DIPRES
        Req_Reporte:
          Frecuencia: Mensual
          Destinatario: DIPRES
          Contenido:
            - Informe avance actividades
            - Información ejecución presupuestaria
        Res: Desglose constituye autorización máxima de gasto por concepto
        Proc_Modificacion: Modificaciones mediante igual procedimiento
        Ctx:
          Visacion: Puede efectuarse desde fecha publicación de esta ley
        Prohib:
          Desc: No incluir recursos para gastos en personal ni bienes y servicios de consumo
          Cond: Salvo autorización por norma expresa en el respectivo presupuesto
        Res_Personal:
          Res: Personal contratado con cargo a dichos recursos no forma parte de la dotación del Servicio
    Articulo_08:
      ID: GN-LEY-PPTO-2026-ART08
      Purp: Pagos 2026 a proveedores mediante transferencia electrónica y cumplimiento Ley 19.983.
      Ctx:
        Cond: Órganos de la Administración del Estado, año 2026
      Req_Pago:
        Req: Transferencia electrónica de fondos
        Ctx: Incluye contratos de obra o infraestructura
      Reconocimiento_Ejecucion_Presupuestaria:
        Req:
          Desc: Pleno cumplimiento
          Ref: LEY19983
      Proc_Contratacion:
        Req:
          - Desc: Requerir información necesaria a proveedores para realizar transferencias
          - Desc: Cumplir instrucciones técnicas generales emitidas por
            Ref: DIPRES
    Articulo_09:
      ID: GN-LEY-PPTO-2026-ART09
      Purp: Prohibir edificios para casas habitación personal; establecer excepciones.
      Prohib:
        Desc: Adquisición, construcción o arrendamiento de edificios para destinarlos a casas habitación del personal
        Ambito: Órganos y servicios públicos
      Excepcion:
        - Programas sobre esta materia incorporados en presupuestos del Poder Judicial
        - Programas sobre esta materia incorporados en presupuestos del Ministerio Público
        - Programas sobre esta materia incorporados en presupuestos del Ministerio de Defensa Nacional
        - Programas sobre esta materia incorporados en presupuestos de Carabineros de Chile
        - Programas sobre esta materia incorporados en presupuestos de la Policía de Investigaciones de Chile
        - Programas sobre esta materia incorporados en presupuestos de Gendarmería de Chile
        - Inversión regional de gobiernos regionales: viviendas para personal de educación y de la salud en zonas apartadas y localidades rurales
    Articulo_10:
      ID: GN-LEY-PPTO-2026-ART10
      Purp: Reglas 2026 para dotación, horas, cupos honorarios/contrata y reposiciones.
      Ajuste_Dotacion_Horas:
        Cond: Dotación máxima personal o horas semanales fijadas en este presupuesto
        Act: Aumentar dotación u horas semanales de un servicio con cargo a disminución de otro
        Act_Alternativo: Aumentar dotación u horas con cargo a la misma cantidad de cupos de honorarios
        Proc:
          Desc: Decreto dictado en la forma dispuesta en
          Ref: DL1263_ART70
        Prohib:
          Desc: No aumentar dotación máxima o número de horas semanales del conjunto de los servicios del ministerio respectivo
      Ajuste_Cupos_Honorarios:
        Act: Aumentar cupos honorarios fijados a servicios públicos y programas presupuestarios
        Origen:
          - Disminución de otro
          - Misma cantidad de cupos de contrata
        Prohib:
          Desc: No aumentar cupos de honorarios del conjunto de los servicios del ministerio respectivo
      Limite_Maximo_Honorarios_Primer_Trimestre_2026:
        Cond: Solicitud de servicios e instituciones del sector público
        Act:
          Autoridad: Ministro de Hacienda
          Desc: Modificar límite máximo de personas contratadas a honorarios (glosas Subtítulos 21 y 24)
        Informe:
          Autoridad: Ministerio de Hacienda
          Destinatario: CEMP
          Plazo: Dentro de los treinta días corridos siguientes al término del trimestre
          Contenido:
            - Detalle ejercicio facultad (agregado)
            - Detalle ejercicio facultad (desagregado por Partida, Capítulo y Programa)
            - Ítems o asignaciones donde la facultad fue ejercida
      Reposiciones_Cupos_Vacantes_2026:
        Regla: Sólo reponer 1 cupo por cada 3 cupos vacantes
        Cond: Servicios públicos con dotación máxima fijada en esta ley
        Causales_Vacancia:
          - Beneficio de retiro previsto en la ley
          - Obtención de jubilación
          - Obtención de pensión
          - Obtención de renta vitalicia en un régimen previsional (funcionarios)
        Req:
          Desc: Disponibilidad presupuestaria suficiente para financiar reposiciones
          Evidencia: Certificado autoridad del Servicio basado en informe unidad de finanzas
          Adjunta: Certificación se acompaña al acto administrativo
        Req_Acto_Administrativo:
          Desc: Acto que disponga reposición debe contener identificación decretos o resoluciones de cesación de funciones en que se fundamenta
    Articulo_11:
      ID: GN-LEY-PPTO-2026-ART11
      Purp: Reglas para contratación de reemplazos en servicios públicos.
      Reemplazos:
        Cond: Funcionarias/os imposibilitados para desempeñar labores por período >30 días corridos
        Act: Contratar personal de reemplazo
        Req:
          Desc: Vigencia contrato no superior a seis meses
        Res:
          Desc: Contratos de reemplazo no se imputan a dotación máxima de personal
        Req_Autorizacion:
          Desc: Sólo pueden efectuarse previa autorización
          Ref: DIPRES
          Verifica: Disponibilidad presupuestaria que corresponda
        Excepcion_Autorizacion:
          Cond:
            - Licencias maternales
            - Postnatal parental
            - Licencia por enfermedad grave de hijo menor de un año
          Req:
            Desc: Informar a
            Ref: DIPRES
      Licencia_Medica_Prolongada:
        Cond: Reemplazo de funcionaria/o con licencia médica (lapso continuo o discontinuo) >6 meses en últimos dos años
        Req: Jefe superior del servicio considerar ejercicio declaración salud incompatible con desempeño del cargo
        Ctx:
          Ref: DFL29_2004_ART151
    Articulo_12:
      ID: GN-LEY-PPTO-2026-ART12
      Purp: Autorizaciones previas DIPRES para TIC y adquisiciones de vehículos; excepciones; parámetros e instrucciones.
      Ctx:
        Cond: Órganos y servicios públicos regidos presupuestariamente por DL 1.263
        Ref: DL1263
        Exclusion:
          - Congreso Nacional
          - Poder Judicial
          - Ministerio Público
          - Contraloría General de la República
      TIC:
        Obj: Inversiones y gastos en proyectos nuevos, de continuidad o arrastre en Tecnologías de la Información y Comunicaciones (TIC)
        Req:
          Desc: Autorización previa
          Ref: DIPRES
        Cond:
          - No aprobadas durante el proceso EVALTIC correspondiente
          - No aprobadas por el Ministerio de Seguridad Pública (letra h) del artículo 6 de la ley Nº 21.730), considerando directrices técnicas proporcionadas por EVALTIC
          - No forman parte de un proceso de compras coordinadas comunicado por la Dirección de Compras y Contratación Pública y autorizado por la Dirección de Presupuestos
      Vehiculos_Motorizados:
        Obj: Adquirir, a cualquier título, vehículos motorizados transporte terrestre de pasajeros y de carga
        Req:
          Desc: Autorización previa
          Ref: DIPRES
        Cond: Precio supere el que fije DIPRES
      Excepcion:
        Ambito: Disposiciones anteriores
        Sujetos:
          - Agencia Nacional de Inteligencia
          - Fuerzas Armadas
          - Fuerzas de Orden y Seguridad Pública
        Solo_Respecto_De:
          - Compras de material bélico
          - Vehículos de color institucional (Reglamento Vehículos Carabineros de Chile N° 20 y su directiva)
          - Vehículos operativos Policía de Investigaciones
          - Compras asociadas a labores de inteligencia
      DIPRES_Parametros_Instrucciones:
        Act:
          - Establecer parámetros técnicos y montos máximos
          - Impartir instrucciones específicas respecto de autorizaciones anteriores
          - Impartir instrucciones específicas respecto de autorizaciones para celebrar contratos señalados en artículo 14 de ley N° 20.128 (responsabilidad fiscal)
        Rec: Establecer mecanismos de adquisición de productos o contratación de servicios, y otras modalidades o procedimientos que determine
    Articulo_13:
      ID: GN-LEY-PPTO-2026-ART13
      Purp: Distribución producto ventas bienes inmuebles fiscales 2026; excepciones; regla reventa; uso recursos Fuerzas Armadas.
      Ctx:
        Cond: Ventas bienes inmuebles fiscales no destinados por art. 56 DL 1.939/1977
        Autoridad: Ministerio de Bienes Nacionales
        Periodo:
          - Ventas efectuadas durante año 2026
          - Cuotas recibidas en 2026 por ventas efectuadas en años anteriores
      Distribucion:
        - Porcentaje: 65%
          Destino: Gobierno regional de la región donde está ubicado el inmueble enajenado
          Uso: Programa de inversión (glosa 01 común Partida 31 "Financiamiento Gobiernos Regionales")
        - Porcentaje: 10%
          Destino: Ministerio de Bienes Nacionales
        - Porcentaje: 25%
          Destino: Beneficio fiscal (rentas generales de la Nación)
      Excepcion:
        Desc: "Norma no rige respecto de ventas del ministerio a:"
        A:
          - Órganos y servicios públicos
          - Empresas donde Estado/sus instituciones o empresas tengan aporte de capital >=50%
        Cond: Destinadas a satisfacer necesidades propias del adquirente
      Regla_Reventa:
        Cond: Empresas referidas en Excepcion enajenan todo o parte de bienes inmuebles adquiridos al ministerio dentro de 1 año desde inscripción del dominio
        Res: Fisco aporta al gobierno regional respectivo 65% del precio pagado al ministerio (o proporción si venta parcial)
      Fuerzas_Armadas:
        Cond: Bienes inmuebles de las Fuerzas Armadas
        Req:
          - Aplicaciones con cargo a recursos de enajenaciones se incorporan anualmente en Ley de Presupuestos (Capítulos Partida Ministerio de Defensa Nacional)
          - Identificar ingresos y gastos estimados en cada caso
        Prohib:
          Desc: "Recursos sólo podrán emplearse en:"
          Permite:
            - Proyectos de infraestructura (incluye proyectos de inversión social: habitabilidad y mejoramiento condiciones de vida de todo el personal integrante)
            - Proyectos de infraestructura militar
    Articulo_14:
      ID: GN-LEY-PPTO-2026-ART14
      Contenido:
        - "Artículo 14.- Los órganos del Estado regidos por esta ley, o los que se especifiquen en los numerales siguientes, informarán a la"
        - Ref: CEMP
        - ", con copia a la"
        - Ref: BCN
        - ", lo siguiente: 1. Un cronograma mensual, desagregado por programa presupuestario y por Subtítulos, de gastos del año en curso, que deberá ser enviado durante el mes de marzo, y actualizado en el mes de julio, junto con una explicación de los principales cambios ocurridos en el transcurso del primer semestre y consignados en dicha actualización. 2. Copia de los informes derivados de estudios e investigaciones contratados en virtud de la asignación 22.11.001, dentro de los ciento ochenta días siguientes a la recepción de su informe final. 3. La nómina de los proyectos o programas desarrollados interna y/o externamente que permitan, en lo específico, su posterior uso como tecnologías duales, con identificación de proyectos nuevos o de arrastre, breve descripción de su objetivo, presupuesto anual, organismos involucrados, y su fecha de inicio y de término, lo que será informado antes del 31 de marzo, mediante documento electrónico que permita el tratamiento de sus datos. En el mismo formato y con igual desagregación, se enviará trimestralmente el presupuesto vigente, treinta días después de terminado el trimestre respectivo, estado de avance físico y financiero de los proyectos o programas, así como las modificaciones que en el período informado hayan experimentado. 4. Cada gobierno regional deberá informar los estudios básicos, proyectos y programas de inversión que realizará en la región y que haya identificado conforme a lo dispuesto en el"
        - Ref: DL1263_ART19BIS
        - ". Tal información comprenderá el nombre del estudio, proyecto o programa, su monto y demás características, y se remitirá"
        - Ref: P30TERM
        - "del mes de total tramitación de los respectivos decretos. 5. El Comité Sistema de Empresas de la Corporación de Fomento de la Producción o quien lo suceda o reemplace, remitirá un informe financiero trimestral de las empresas del Estado, y de aquellas en que el Estado, sus instituciones o empresas tengan aportes de capital igual o superior al cincuenta por ciento, que comprenderá un balance consolidado por empresa y estado de resultados, a nivel consolidado y por empresa. Dicho informe será remitido dentro de los quince días siguientes a la fecha de vencimiento del respectivo plazo de presentación fijado por la Comisión para el Mercado Financiero. La misma obligación tendrán Televisión Nacional de Chile y la Corporación Nacional del Cobre de Chile (CODELCO), las cuales deberán remitir los informes financieros trimestrales directamente a la"
        - Ref: CEMP
        - ". 6. El monto ejecutado por concepto de publicidad y difusión, imputados al Subtítulo 22, ítem 07, en que haya incurrido, por programa presupuestario, en el formato que definirá para tal efecto el Ministerio Secretaría General de Gobierno. Asimismo, informará el detalle del gasto por concepto de publicidad, difusión o relaciones públicas en general, y para ello distinguirá entre avisos, promoción en periódicos, radios, televisión, medios digitales, cines, teatros, revistas, contratos con agencias publicitarias y/o servicios de exposiciones e indicará los proveedores de cada uno de ellos, si éstos tienen una clara identificación local y si pertenecen a un holding, conglomerado o cadena de comunicación. Respecto de estos últimos, se adjuntará además la nómina de las entidades ejecutoras de dichas actividades, su mecanismo de contratación y el monto adjudicado, desagregado por programa. Esta información se remitirá trimestralmente,"
        - Ref: P30TERM
        - "del respectivo trimestre. 7. Sobre las comisiones de servicio en el país y en el extranjero. Se deberá detallar el número de comisiones y cometidos funcionarios, funcionarias y funcionarios designados, su destino, viático recibido y sus fundamentos y el detalle de los pasajes utilizados en dichas comisiones de servicios, y se indicará el titular de éstos, destino, valor y fecha, a excepción de aquellas que tengan el carácter de reservadas, las que deberán informarse en sesión secreta. Esta información se remitirá trimestralmente. 8. Las contrataciones y desvinculaciones realizadas durante cada trimestre. En ambos casos, se deberá consignar el nombre, cargo y título de educación superior si lo hubiera. En el caso de las desvinculaciones, deberá consignarse la cantidad de funcionarias y funcionarios que cesen en sus funciones en cada uno de los servicios públicos con los que se relacionen, la antigüedad en el cargo, la fecha y la causal de cesación. 9. Los recursos que son implementados directamente por la institución, aquellos que son ejecutados por medio de convenio marco, licitación pública, licitación privada o trato directo, en cada uno de los programas que constituyen la respectiva Partida. Esta información se remitirá trimestralmente,"
        - Ref: P30TERM
        - "del respectivo trimestre e incluirá a la Comisión de Hacienda de la Cámara de Diputados. 10. Los gastos asociados a remuneraciones de trabajadores, con indicación de la calidad jurídica de los contratos y los porcentajes de tipos de contratación en relación con el total del personal, diferenciado según género y por estamento, la duración media y promedio de cada contrato, y el número de veces que ha sido contratado bajo esta modalidad por la entidad pública referida. Esta información se remitirá semestralmente e incluirá a la Comisión de Hacienda de la Cámara de Diputados. 11. Los gastos asociados al arriendo de terrenos u otros bienes inmuebles que sirvan de dependencias para las actividades propias del ministerio. Se informará trimestralmente, treinta días después del término del trimestre respectivo, e incluirá a la Comisión de Vivienda y Urbanismo del Senado, y a la Comisión de Vivienda, Desarrollo Urbano y Bienes Nacionales de la Cámara de Diputados. 12. El Ministerio del Interior informará antes del 31 de enero de 2026 acerca de los resultados de la implementación y desarrollo del Plan Buen Vivir durante el año 2025, salvo en lo relativo al Programa de Infraestructura del referido Plan, que corresponderá informar, en igual fecha, al Ministerio de Obras Públicas. Asimismo, los ministerios indicados en el párrafo anterior deberán informar, en el mismo plazo y cada uno en el ámbito de sus competencias relativas al Plan, sobre la planificación presupuestaria, objetivos y metas que éste tendrá para el año 2026. Además, trimestralmente, el Ministerio del Interior informará de las actividades desarrolladas en el marco del Plan Buen Vivir. En tanto, el Ministerio de Obras Públicas informará de las obras ejecutadas y su nivel de avance, con indicación de la cobertura de población, desagregadas por comuna. 13. Durante el año 2026, la Empresa Nacional de Minería, creada por el decreto con fuerza de ley N° 153, de 1960, del Ministerio de Hacienda, deberá informar respecto de las enajenaciones de activos que su directorio apruebe realizar. 14. Los ministerios de Obras Públicas, de Vivienda y Urbanismo, de Salud y de Educación, y la Subsecretaría de Desarrollo Regional y Administrativo y los gobiernos regionales informarán, a más tardar en el mes de enero de 2026, la nómina con los proyectos de inversión identificados de acuerdo con lo establecido en el"
        - Ref: DL1263_ART19BIS
        - ", incluidos en esta ley. Esa nómina contendrá el nombre, localización por comuna y región, estado, fecha de ejecución e inversión estimada total y de cada una de las etapas que conforman el proyecto, y precisará, específicamente, las obras y recursos que se ejecutarán durante el año 2026. Asimismo, a partir de febrero de 2026, deberán enviar mensualmente un informe de actualización que contenga, respecto de cada uno de ellos, su estado de avance y la inversión materializada durante el año 2026. 15. Mensualmente la"
        - Ref: DIPRES
        - "deberá informar la nómina de proyectos de inversión presupuestados en los Subtítulos 29, 31 y 33 por Partida, y para ello desagregará la información por etapa de diseño, ejecución y fecha de entrega prevista. 16. Trimestralmente se informará sobre las instituciones de las señaladas en el artículo 2 y el monto, la duración y las condiciones en que han tomado deuda con garantía estatal. 17. Semestralmente, las empresas públicas creadas por ley, las empresas del Estado y las sociedades en que éste tenga aporte, participación accionaria superior al cincuenta por ciento o mayoría en el directorio, cualquiera sea el estatuto por el que se rijan, incluso aquellas que de acuerdo a su ley orgánica deban ser expresamente mencionadas para quedar obligadas al cumplimiento de ciertas disposiciones, deberán remitir la información relativa al total de deuda que poseen, con indicación del porcentaje de ella que ha sido tomada con garantía estatal y las fechas y condiciones de su vencimiento. 18. Un reporte trimestral desagregado por ministerio y por región, que dé cuenta de los proyectos o programas identificados con el etiquetado de “Género” y de “Cambio Climático” a nivel de Subtítulo. 19. El Ministerio de Economía, Fomento y Turismo informará semestralmente el estado de la implementación del Plan de Acción del Corredor Bioceánico Vial, con detalle de los convenios suscritos y su estado de ejecución. Esta información se remitirá semestralmente, treinta días después de terminado el semestre respectivo, e incluirá a la Comisión de Economía, Fomento; Micro, Pequeña y Mediana Empresa; Protección de los Consumidores y Turismo de la Cámara de Diputados y a la Comisión de Economía del Senado. Asimismo, los órganos del Estado regidos por esta ley deberán cumplir con las siguientes obligaciones de información y publicación: a) Publicar en su sitio electrónico institucional un informe trimestral que contenga, en su caso, la individualización de los proyectos beneficiados con cargo a los Subtítulos 24 y 33, nómina de beneficiarios, metodología de elección de éstos, las personas o entidades ejecutoras de los recursos, los montos asignados, la modalidad de asignación, las actividades financiadas, los objetivos y metas anuales, los montos y porcentajes de ejecución, desagregados por programa presupuestario, región y comuna según sea el caso,"
        - Ref: P30TERM
        - "del respectivo trimestre. En caso de contener coberturas y recursos asignados en glosa, la información deberá presentarse con dicho nivel de desagregación. Si las asignaciones a las que hace mención el párrafo precedente corresponden a transferencias a municipios, el informe respectivo también deberá contener una copia de los convenios firmados con los alcaldes, el desglose por municipio de los montos transferidos y el criterio bajo el cual éstos fueron distribuidos. La precitada información deberá ser remitida en igual plazo y con el mismo detalle a la"
        - Ref: CEMP
        - ". b) Publicar en sus respectivos portales de transparencia activa las actas de evaluación emitidas por las comisiones evaluadoras de licitaciones y compras públicas de bienes y servicios que realicen en el marco de la ley N° 19.886,"
        - Ref: P30TERM
        - "del respectivo proceso. La precitada información deberá ser remitida a la"
        - Ref: CEMP
        - "trimestralmente, dentro de los treinta días posteriores al término del trimestre respectivo con el mismo detalle. c) Cada ministerio y los demás órganos de la Administración del Estado deberán publicar en sus respectivos sitios electrónicos institucionales la información relativa al presupuesto asignado por esta ley. Para estos efectos procurarán utilizar un lenguaje claro que permita ser comprendido por la mayor cantidad de personas, con utilización de gráficos y otros mecanismos que permitan comprender, de manera sencilla, la composición del presupuesto y de los distintos elementos que lo integran, y vincularán esta información a las orientaciones estratégicas, objetivos prioritarios y resultados esperados para el período. Se deberán contemplar mecanismos de participación ciudadana que permitan recoger inquietudes y realizar consultas sobre iniciativas en estudio o para la priorización de acciones futuras, a través de consejos de la sociedad civil, de carácter consultivo, conformados acorde con lo establecido en el artículo 74 del decreto con fuerza de ley N° 1-19.653, de 2000, del Ministerio Secretaría General de la Presidencia. Toda información deberá ser proporcionada en formato digital, legible y procesable, que no consista solamente en imagen de la respectiva documentación, desagregada por sexo, cuando corresponda. Asimismo, todo deber de información que no señale una fecha de entrega deberá ser cumplido antes del comienzo de la tramitación de la Ley de Presupuestos del Sector Público para el año siguiente. La información que, de acuerdo con lo establecido en esta ley, deba ser remitida a cualquiera de las comisiones de la Cámara de Diputados o del Senado, se entenderá que debe ser remitida también a la"
        - Ref: CEMP
        - ". La Cámara de Diputados y el Senado deberán disponer en un repositorio electrónico de acceso público la información remitida de acuerdo con lo establecido en esta ley. Para tal efecto, se podrá disponer de una plataforma web, a través de la cual las instituciones públicas incluidas en la presente ley deberán disponer la respectiva información. Sin perjuicio de lo anterior, la"
        - Ref: CEMP
        - "deberá remitir la información que le corresponda recibir a las comisiones permanentes de la Cámara de Diputados y del Senado cuyas materias de competencia se relacionen con la Partida respectiva, dentro del plazo de treinta días contado desde su recepción. La información que se remita de acuerdo con lo establecido en el presente artículo deberá considerar las particularidades, condiciones y desagregación vigente en la Ley de Presupuestos. Para dar cumplimiento a lo señalado en este artículo, la información indicada deberá ser puesta a disposición por los organismos correspondientes de conformidad a las instrucciones impartidas para tal efecto por la"
        - Ref: DIPRES
        - ". Asimismo, los organismos públicos obligados a remitir la información señalada en el presente artículo deberán ponerla a disposición en los sitios electrónicos en los que dan cumplimiento a las obligaciones de transparencia activa. La omisión de la publicación en la forma señalada o su falta de actualización podrá reclamarse en conformidad con lo dispuesto en el artículo 8 de la Ley de Transparencia de la Función Pública y de Acceso a la Información de la Administración del Estado, contenida en el artículo primero de la"
        - Ref: LEY20285
        - ", sobre Acceso a la Información Pública."
    Articulo_15:
      ID: GN-LEY-PPTO-2026-ART15
      Purp: Regular traspaso honorarios suma alzada a contrata y ajustes asociados, año 2026.
      Traspasos_Honorarios_A_Contrata:
        Periodo: Año 2026
        Limite_Maximo_Personas: 6.500
        Act: Modificar calidad jurídica de honorario a suma alzada a contrata
        Req_Asimilacion:
          Desc: Asimilar al grado del estamento correspondiente según sistema de remuneraciones del servicio
        Cond:
          Desc: Remuneración líquida mensualizada permita mantener honorario líquido mensual
      Ajuste_Limite_Dotacion:
        Cond:
          Desc: Posterior al 31 de marzo de 2026; a solicitud de servicios e instituciones del Sector Público
        Act: Modificar límite máximo de dotación de personal (glosas presupuestarias de esta ley)
        Ctx:
          Compensacion: Equivalente en número de personas contratadas a honorarios a suma alzada (glosas presupuestarias asociadas a Subtítulos 21 y 24)
      Decretos_Ajustes:
        Act:
          Desc: Establecer ajustes derivados de la aplicación de este artículo
          Ref: MINHACIENDA
        Proc:
          Desc: Conforme a lo dispuesto en
          Ref: DL1263_ART70
        Informe_Mensual:
          Destinatario: CEMP
          Plazo: Dentro de los treinta días siguientes al término del mes respectivo
      Decretos_Requisitos_Procedimiento:
        Act:
          - Desc: Establecer requisitos para el traspaso
            Ref: MINHACIENDA
          - Desc: Establecer forma de determinar remuneración líquida mensualizada
            Ref: MINHACIENDA
        Prohib:
          Desc: Para el cálculo no procederá descontar los impuestos
        Ctx:
          Incluye:
            - Honorario líquido mensual
            - Grado de asimilación al estamento que corresponda (según sistema de remuneraciones del servicio)
            - Criterios de priorización que deben establecer jefas y jefes superiores de servicio si hay más personal a honorarios que cupos disponibles
            - Demás normas de procedimiento necesarias para la implementación
      Renovacion_Honorarios_2026:
        Cond: Año 2026
        Act: Renovar contrataciones de personal a honorarios sin quedar sujeto a limitaciones del artículo 11
        Ref: LEY18834
        Res: Reemplazos del personal a honorarios no quedan afectos a la limitación antes señalada
    Articulo_16:
      ID: GN-LEY-PPTO-2026-ART16
      Contenido:
        - "Artículo 16.- La"
        - Ref: DIPRES
        - "proporcionará a las comisiones de Hacienda del Senado y de la Cámara de Diputados, a la"
        - Ref: CEMP
        - "y a la"
        - Ref: BCN
        - "los informes y documentos que se señalan, en la forma y oportunidades que a continuación se indican: 1. Informe de ejecución presupuestaria mensual de ingresos y gastos del Gobierno Central, a nivel de Subtítulos,"
        - Ref: P30TERM
        - "del respectivo mes. Este informe deberá incluir la ejecución mensual de gastos correspondientes a los Subtítulos 30 “Adquisición de Activos Financieros” y 32 “Préstamos”, del clasificador de gastos. 2. Informe de ejecución presupuestaria trimestral de ingresos y gastos del Gobierno Central, a nivel de Subtítulos,"
        - Ref: P30TERM
        - "del respectivo trimestre, e incluirá en anexos un desglose de los ingresos tributarios del período, otras fuentes de financiamiento y saldo de la deuda bruta del Gobierno Central. Del mismo modo, deberá incluir en anexos información del gasto devengado en el Gobierno Central del Subtítulo 22, ítem 07, Publicidad y Difusión, desagregado por asignación, y detallará el gasto por Partida y su variación real respecto de igual trimestre del año anterior y de las asignaciones comprendidas en los Subtítulos 24 y 33, para cada uno de los programas de esta ley. 3. Informe de la ejecución trimestral del presupuesto de ingresos y gastos de las Partidas de esta ley, al nivel de Partidas, Capítulos y Programas aprobados respecto de cada una de ellas, estructurado en presupuesto inicial, presupuesto vigente y monto ejecutado a la fecha respectiva, incluido el gasto de todas las glosas de esta ley,"
        - Ref: P30TERM
        - "del respectivo trimestre. 4. Copia de los decretos de modificaciones presupuestarias totalmente tramitados durante cada mes y un informe consolidado de las modificaciones presupuestarias efectuadas en dicho mes por Partida, que contenga una descripción que indique si se trata de incrementos por aplicación de leyes, reducciones por ajuste fiscal, o modificaciones por decisiones de política, con especificación de los montos incrementados o disminuidos por Subtítulo y Partida, dentro de los treinta días siguientes a su término. 5. Informe semestral de la deuda pública bruta y neta del Gobierno Central con sus notas explicativas y antecedentes complementarios, dentro de los sesenta y noventa días siguientes al término del correspondiente semestre, respectivamente. 6. Informe trimestral sobre los Activos Financieros del Tesoro Público,"
        - Ref: P30TERM
        - "del respectivo trimestre. 7. Informe trimestral sobre el Fondo de Reserva de Pensiones y el Fondo de Estabilización Económica y Social, dentro de los noventa días siguientes al término del respectivo trimestre. 8. Informe trimestral de las operaciones de cobertura de riesgo de activos y pasivos autorizados en el artículo 5 de la ley N° 19.908,"
        - Ref: P30TERM
        - "del respectivo trimestre. 9. Informe trimestral con la actualización del escenario fiscal que considere una proyección de ingresos y gastos, junto a la correspondiente proyección del balance efectivo y cíclicamente ajustado, la proyección de deuda y la posición financiera neta para el año 2026 y para el programa financiero en cada caso, adicional al Informe sobre Finanzas Públicas establecido en el número 22 del artículo 2° del decreto con fuerza de ley N° 106, de 1960, del Ministerio de Hacienda. En la misma oportunidad se informará acerca de la necesidad de financiamiento que deba ser atendida con cargo a la autorización de endeudamiento otorgada de conformidad al artículo 3. La entrega de esa información respetará los deberes de reserva de información establecidos en leyes especiales. En estos informes se actualizará la proyección de ingresos efectivos y estructurales del Gobierno Central, habida consideración de la recaudación efectiva del año 2025, los ajustes metodológicos que se implementen y la actualización de proyecciones macroeconómicas para el año. Sobre esta base la"
        - Ref: DIPRES
        - "determinará el nivel de gastos compatible con el cumplimiento de la meta fiscal del año y los ajustes que se requieran para su logro. 10. Antecedentes relativos a la planificación estratégica de los órganos de la Administración del Estado, excluidos el Congreso Nacional, el Poder Judicial, la"
        - Ref: CGR
        - ", el Ministerio Público, el Servicio Electoral y las Fuerzas Armadas. Dichos antecedentes deberán contemplar, a lo menos: a) Definiciones estratégicas, incluida la misión institucional, identificación de sus prioridades a través de objetivos estratégicos y bienes y servicios provistos a sus usuarios. b) Indicadores de desempeño vinculados a los objetivos estratégicos institucionales. c) Medición efectiva de los indicadores de desempeño del año anterior. Para lo anterior, la"
        - Ref: DIPRES
        - "podrá enviar instrucciones específicas. La información correspondiente a la medición de los indicadores de desempeño del año anterior se remitirá durante el mes de mayo y la información correspondiente a la planificación estratégica del periodo 2026–2029 se remitirá en el mes de septiembre. 11. Antecedentes relativos al diseño y desempeño de la oferta programática vigente de los órganos de la Administración del Estado. Se entenderá por tales a los ministerios y sus respectivos órganos desconcentrados, y servicios públicos. Dichos antecedentes deberán contemplar: a) La información que la"
        - Ref: DIPRES
        - "y la Subsecretaría de Evaluación Social recaben en virtud del monitoreo del desempeño de los programas públicos correspondientes a la oferta programática ejecutada el año anterior. Esta información deberá remitirse en el mes de mayo. b) La información que la"
        - Ref: DIPRES
        - "y la Subsecretaría de Evaluación Social recaben en virtud de la evaluación ex ante de diseño de los programas nuevos o aquellos que reformulen su diseño en forma significativa presentados en el marco del proceso de formulación presupuestaria del año siguiente. Dicha información deberá remitirse cuarenta y cinco días antes de que comience la discusión presupuestaria del año siguiente. c) La información recabada de la Evaluación de Programas Gubernamentales (EPG) de acuerdo con lo establecido en el artículo 52 del"
        - Ref: DL1263
        - ", Orgánico de Administración Financiera del Estado y en el reglamento fijado a través del decreto N° 2.068, de 2022, del Ministerio de Hacienda. Esta información deberá remitirse quince días antes de que comience la discusión presupuestaria del año siguiente. 12. Durante el primer trimestre del año la"
        - Ref: DIPRES
        - "informará, de forma agregada, y a nivel de Partida, Capítulo y Programa, los gastos en personal que son imputados al Subtítulo 24, y señalará el monto que la Ley de Presupuestos autoriza al respecto y, a la fecha, la ejecución de dichos recursos y el número de personas que se desempeñan en dichos cargos, según corresponda. De la misma forma, y como parte integrante de los antecedentes que acompañan los contenidos del proyecto de ley de presupuestos del año siguiente, se informará de forma agregada, y a nivel de Partida, Capítulo y Programa, los gastos en personal que se propone serán imputados al Subtítulo 24, junto con una estimación del número de personas que se espera se desempeñen en dichos cargos. Se actualizará la información señalada precedentemente, de forma que permita su comparación respecto de los recursos autorizados por la ley, su ejecución a la fecha y el número de personas que se desempeñan en dichos cargos, según corresponda. 13. En el marco de la regla fiscal el Ministerio de Hacienda, por intermedio de la"
        - Ref: DIPRES
        - ", remitirá mensualmente a la"
        - Ref: CEMP
        - "un informe de avance hacia la meta de balance estructural comprometida para el año 2026, e incluirá: a) la estimación de balance estructural acumulado. b) la comparación con la trayectoria trimestral de referencia. c) las medidas de corrección adoptadas. La información señalada en los párrafos precedentes, además, deberá publicarse en el sitio electrónico de la"
        - Ref: DIPRES
        - ". Para dar cumplimiento a lo señalado en los numerales 1 al 11 anteriores, la información indicada deberá ser entregada por los organismos correspondientes de conformidad a las instrucciones impartidas para tal efecto por la"
        - Ref: DIPRES
        - ". Además, dicha información deberá ser publicada en los mismos plazos en los respectivos sitios electrónicos de los organismos obligados a proporcionarla. Durante el mes de marzo de 2026 se conformará una instancia de coordinación entre ambas cámaras del Congreso Nacional y la"
        - Ref: DIPRES
        - ", para efectos de acordar formatos y precisiones respecto de la información de la que trata este artículo."
    Articulo_17:
      ID: GN-LEY-PPTO-2026-ART17
      Purp: Reglas para afiliación/asociación a organismos internacionales y aumento de cuotas.
      Autorizacion_Previa:
        Req: Autorización previa del ministerio del ramo
        Req_Visacion:
          Desc: Visada por
          Ref:
            - MINREL
            - MINHACIENDA
      Act_Permitidas:
        - Afiliarse o asociarse a organismos internacionales
        - Renovar afiliaciones existentes
        - Convenir aumento de cuotas
      Condicion_Disponibilidad_Presupuestaria:
        Cond:
          Desc: Incorporación o renovación demande efectuar contribuciones o aportes o aumentos de éstos; o convenios consisten en aumentos del monto de cuotas
        Req: Visación condicionada a disponibilidad presupuestaria
        Verifica: DIPRES
    Articulo_18:
      ID: GN-LEY-PPTO-2026-ART18
      Purp: Reglas para decretos supremos, visaciones, autorizaciones y procedimientos DIPRES/MH.
      Decretos_Supremos_MINHACIENDA:
        Cond: Decretos supremos que deban dictarse en cumplimiento de artículos de esta ley y los que correspondan para ejecución presupuestaria
        Req:
          Desc: Ajustarse a lo establecido en
          Ref: DL1263_ART70
      Visaciones_Autorizaciones_Ministerio_Hacienda:
        Cond: Otorgamiento no se exija expresamente por decreto supremo
        Proc:
          Desc: Cumplirse mediante oficio o visación de
          Ref: DIPRES
        Rec:
          Desc: DIPRES podrá delegar facultades total o parcialmente
        Incluye:
          - Desc: Aprobaciones, visaciones y autorizaciones del Ministerio de Hacienda establecidas en esta ley
          - Desc: Autorizaciones artículos 22 y 24
            Ref: DL3001_1979
          - Desc: Oración final del inciso segundo del artículo 8
            Ref: DL1056_1975
          - Desc: Artículo 4
            Ref: LEY19896
          - Desc: Artículo 19
            Ref: LEY18382
          - Desc: Excepción inciso final artículo 9
            Ref: LEY19104
          - Desc: Autorizaciones artículo 14
            Ref: LEY20128
          - Desc: Autorizaciones artículo 27
            Ref: DL1263
          - Desc: Literal r) artículo 70
            Ref: LEY19300
      Modificaciones_Concesiones_Compensaciones:
        Ctx:
          Cond: Modificaciones incorporadas a contratos de concesión y convenios con compensaciones derivadas
        Base_Legal:
          Ctx: Artículo 19
          Ref: DS900_1996_MOP
          Ctx_Adicional:
            Desc: Texto refundido, coordinado y sistematizado
            Ref: DFL164_1991_MOP
        Req:
          Desc: Decreto supremo fundado del Ministerio de Obras Públicas
          Ctx: Dictado bajo la fórmula "por orden del Presidente de la República"
          Req_Adicional: Debe llevar, además, la firma del Ministro de Hacienda
      Identificaciones_Art19bis_DL1263:
        Cond:
          Ref: DL1263_ART19BIS
        Proc:
          Desc: Resolución de
          Ref: DIPRES
      Visaciones_Art5_Ley19896:
        Cond:
          Ref: LEY19896
        Proc: Subsecretaria o subsecretario respectivo
        Rec: Puede delegar en secretaria o secretario regional ministerial correspondiente
    Articulo_19:
      ID: GN-LEY-PPTO-2026-ART19
      Purp: Establecer calidad de agentes públicos y deber de probidad para encargados de programas a honorarios.
      Cond: Personas encargadas de programas presupuestarios previstos en esta ley, contratadas a honorarios
      Res_Calidad:
        Res:
          - Tendrán la calidad de agentes públicos
          - Responsabilidad penal y administrativa
        Ctx: Sin perjuicio de la responsabilidad correspondiente de su superior jerárquico
      Req_Probidad:
        Req: Ajustar su labor al principio de probidad administrativa contemplado en las leyes
    Articulo_20:
      ID: GN-LEY-PPTO-2026-ART20
      Purp: Reglas de avisaje/publicaciones en medios y obligaciones de transparencia asociadas.
      Medios_Comunicacion_Social:
        Cond: Órganos y servicios públicos realicen avisaje y publicaciones en medios de comunicación social
        Req:
          - Desc: Efectuarlos, al menos en
            Porcentaje: "40%"
          - Desc: Medios de comunicación con clara identificación local
          - Desc: Distribuidos territorialmente de manera equitativa
        Prohib:
          Desc: "Este porcentaje no podrá destinarse a medios que sean parte de conglomerados, holdings o cadenas de medios de comunicación"
          Cond:
            - Se relacionen en los términos de los artículos 99 y 100
            - Tengan sedes o sucursales en más de una región
          Ref: LEY18045
      Transparencia_Publicacion:
        Req:
          - Desc: Sujetarse a lo señalado en el artículo 7
            Ref: LEY20285
          - "Poner a disposición, al menos, la siguiente información"
        Informacion_Minima:
          - "Monto total y desglose de los gastos en avisaje y publicidad"
          - "Identificación de los proveedores (razón social y rut)"
          - "Tipo de medio de comunicación (televisión, radio, prensa u otro)"
          - "Identificación territorial (local, regional, nacional)"
          - "Pertenencia o no a un holding, conglomerado o cadena de comunicación"
        Rec: Publicar en formato de datos abiertos y reutilizables, para facilitar acceso y utilización por ciudadanos
        Act:
          Desc: Impartir instrucciones sobre cumplimiento
          Ref: CPLT
      Planificacion_Avisaje_Publicaciones:
        Req: Remitir planificación anual de avisaje y publicaciones
        Plazo: A más tardar en marzo de 2026
        Destinatario:
          Ref: SEGEGOB
        Ctx: Formato y lineamientos serán proporcionados oportunamente por SEGEGOB
        Res:
          Desc: SEGEGOB hará seguimiento del cumplimiento de la obligación establecida en el inciso anterior
    Articulo_21:
      ID: GN-LEY-PPTO-2026-ART21
      Purp: Límites y reglas para gastos publicidad y difusión 2026 (por Partida) y definiciones asociadas.
      Limite_Gastos_Publicidad_Difusion_2026:
        Cond: Gastos con cargo a cada Partida presupuestaria, año 2026
        Prohib:
          Desc: No superar suma fijada en el respectivo presupuesto
      Distribucion_Recursos_Publicidad_Difusion:
        Cond: Mes de diciembre de 2025
        Req:
          Desc: Cada ministerio debe enviar a
          Ref: DIPRES
          Contenido: Distribución de recursos por Programa presupuestario
        Proc_Fijacion_Distribucion:
          Act:
            Desc: Fijar distribución respecto de cada Programa presupuestario mediante decreto del
            Ref: MINHACIENDA
          Proc:
            Desc: Expedido bajo la fórmula establecida en
            Ref: DL1263_ART70
          Req:
            Desc: Copia del decreto (totalmente tramitado) debe ser enviada a
            Ref: CEMP
      Reasignacion_Programas:
        Act: Aumentar monto asignado a un Programa presupuestario para gastos en publicidad y difusión
        Cond: Con cargo a disminución de otro u otros
        Prohib:
          Desc: En ningún caso aumentar por esta vía el monto total fijado para la Partida
      Actividades_Publicidad_Difusion:
        Sujetos:
          - Ministerios
          - Delegaciones presidenciales regionales
          - Delegaciones presidenciales provinciales
          - Gobiernos regionales
          - Órganos y servicios públicos que integran la Administración del Estado
        Req:
          Desc: Sujetarse a lo dispuesto en artículo 3
          Ref: LEY19896
        Prohib:
          Desc: Campañas publicitarias con objeto único enumerar logros de una autoridad específica o del Gobierno en general
          Excepcion: Cuentas públicas que realicen los organismos señalados en el citado artículo
      Def_Gastos_Publicidad_Difusion:
        Def: Gastos de publicidad y difusión para cumplimiento de funciones
        Incluye:
          - Necesarios para adecuado desarrollo de procesos de contratación
          - Acceso, comunicación o concursabilidad de beneficios o prestaciones sociales (ejercicio de derechos o acceso a becas, subsidios, créditos, bonos, transferencias monetarias u otros programas o servicios)
          - Orientación y educación de la población para situaciones de emergencia o alarma pública
          - Gastos que, por su naturaleza, resulten impostergables para gestión eficaz de los organismos
      Publicaciones_Memorias:
        Prohib:
          Desc: Sólo podrán editar memorias y otras publicaciones por medios electrónicos
          Excepcion: Salvo que la ley que los regule indique expresamente publicación en medios impresos
      Prohib_Promocion_Institucional:
        Prohib: Incurrir en gastos para elaboración de artículos de promoción institucional
      Suscripciones_Servicios_Informacion:
        Cond: Suscripciones a revistas, diarios y servicios de información (papel o medios electrónicos de transmisión de datos)
        Req: Limitar gasto al estrictamente indispensable para el quehacer de los servicios
    Articulo_22:
      ID: GN-LEY-PPTO-2026-ART22
      Purp: Regular comisiones de servicio, comitivas, plan anual de viajes al extranjero y prohibición duplicidad viáticos.
      Comisiones_Servicio:
        Ambito: País y extranjero
        Req: Reducir a las imprescindibles para cumplimiento de tareas institucionales
        Ctx: Especialmente aquellas en el extranjero
        Prohib:
          Desc: Comisiones en el extranjero no podrán exceder de dos personas por actividad
        Excepcion:
          Autoridad: DIPRES
          Act: Autorizar comisión de servicio mayor al número señalado
          Cond: Motivos fundados
      Comitivas_Extranjero:
        Req: Sólo Presidente de la República y ministras/ministros de Estado en comisiones de servicio en el extranjero podrán ser acompañados por comitivas
        Ministros:
          Limite_Acompanantes: 1
          Cond: Sólo en caso de ser estrictamente necesario
          Excepcion_Segundo_Acompanante:
            Cond: Situaciones debidamente justificadas
            Req:
              Desc: Solicitar autorización previa a
              Ref: DIPRES
        MinRel:
          Ref: MINREL
          Limite_Acompanantes: 3
      Plan_Anual_Viajes_Extranjero:
        Req:
          - Desc: Servicios públicos deberán informar a
            Ref: DIPRES
          - "Adecuarse al presupuesto aprobado en esta ley"
        Inicio: A partir de la publicación de esta ley
        Plazo: 31 de enero de 2026
        Modificacion:
          Cond: No implique un mayor gasto
          Req:
            Desc: Informar a
            Ref: DIPRES
      Visitas_Estado_Oficiales_Trabajo:
        Cond: Presidente de la República o ministras/ministros de Estado convoquen como parte de la delegación a autoridades
        Incluye:
          - Miembros del Congreso Nacional
          - Ministras y ministros de la Corte Suprema
          - Contralora o Contralor General de la República
          - Otras autoridades superiores de la Administración del Estado
        Res: Consideradas comisiones de servicio de interés para la política exterior del país
        Prohib: Duplicidad en el pago de viáticos
    Articulo_23:
      ID: GN-LEY-PPTO-2026-ART23
      Purp: Reglas para asignación de recursos (transferencias corrientes y de capital) a instituciones privadas.
      Regla_General_Asignacion:
        Ambito: Organismos públicos contenidos en esta ley
        Ctx:
          Recursos: Transferencias corrientes y de capital
        Excepcion:
          - Ley expresamente señale lo contrario
          - Asignaciones nominadas en esta ley
        Req:
          Desc: Resultado de concurso público abierto y transparente
        Req_Garantias:
          - Probidad
          - Eficiencia y eficacia en uso de recursos públicos
          - Igualdad
          - Libre concurrencia de potenciales beneficiarios de la transferencia
        Req_Convenio:
          Req: Transferencias se materializarán previa suscripción de convenio
      Ejecucion_Politica_Publica:
        Req: Concurso y convenio obligatorios para seleccionar institución privada ejecutora de política pública
        Rec: Concursos podrán no considerar soluciones específicas en sus bases
      Asignacion_Directa_Sin_Concurso:
        Warn: Permitida excepcionalmente
        Casos:
          - ID: GN-LEY-PPTO-2026-ART23-EXC-A
            Cond: En concursos públicos respectivos no se presentaron interesados
          - ID: GN-LEY-PPTO-2026-ART23-EXC-B
            Cond: Sólo existe una persona jurídica como posible beneficiario de los recursos o como su ejecutor
          - ID: GN-LEY-PPTO-2026-ART23-EXC-C
            Cond: Emergencia, urgencia o imprevisto
            Req: Calificados de conformidad a lo establecido en el inciso siguiente
            Ctx: Sin perjuicio de disposiciones especiales para sismos y catástrofes contenidas en legislación pertinente
        Req_Acreditacion:
          Req: Acreditar concurrencia de circunstancia que justifica asignación directa
          Proc: Resolución fundada del jefe superior de la entidad que asigne los recursos o de quien tenga delegada la facultad
      Incumplimiento_Grave:
        Cond:
          - Casos graves, debidamente calificados según lo dispuesto en el convenio
          - Incumplimiento de disposiciones de esta ley o términos de respectivos convenios
        Res: Imposibilidad de efectuar cualquier nueva transferencia de recursos públicos a la institución privada respectiva hasta subsanar
        Ctx:
          Sin_Perjuicio:
            - Ref: RES30_2015_CGR
            - Responsabilidad administrativa que pueda derivarse en órgano responsable
      Req_Ley19862:
        Cond:
          Desc: Instituciones receptoras de fondos no cumplan obligaciones
          Ref: LEY19862
        Prohib: No podrán recibir fondos públicos establecidos en esta ley hasta subsanar
        Req:
          Desc: Ministerios y servicios públicos deberán resguardar registro de información correspondiente
          Ref: LEY19862
      Publicacion_Transferencias:
        Req: Publicar información relativa a transferencias
        Ctx:
          Ref: LEY20285
          Ctx_Adicional: Letras f) y k) del artículo 7 del artículo primero
      Alcance_Reglas:
        Ctx: Disposiciones del presente artículo y artículos 24, 25 y 26 siguientes
        Aplica_A: Transferencias corrientes y de capital con regulación propia para asignación
        Ctx_Adicional: Incluye casos en que transferencias se efectúen sin concurso por disposición de esta ley u otro cuerpo normativo
        Cond: En todo aquello en que no sean contradictorias
    Articulo_24:
      ID: GN-LEY-PPTO-2026-ART24
      Contenido:
        - "Artículo 24.- Los convenios de transferencia a los que hace referencia el artículo anterior estarán sujetos a las siguientes obligaciones y prohibiciones, tanto cuando se trate de transferencias corrientes a instituciones privadas beneficiarias como a instituciones privadas ejecutoras de políticas públicas: 1. Deberán indicar el objeto social o fines que establecen los estatutos o el acta de constitución de la institución privada con la cual se suscriba el convenio. El objeto social se acreditará de manera previa a la suscripción del convenio de transferencia, y deberá ser pertinente con la actividad a desarrollar. 2. Deberán indicar las actividades específicas a desarrollar y/o los conceptos de gastos que se financiarán. 3. No podrán establecer compromisos financieros que excedan el ejercicio presupuestario, salvo que cuenten con la autorización previa de la"
        - Ref: DIPRES
        - ". 4. Deberán condicionar la suscripción del convenio al cumplimiento íntegro de las obligaciones establecidas en la ley N° 19.862. 5. Las rendiciones de cuentas se deberán realizar a través del Sistema de Rendición Electrónica de Cuentas de la"
        - Ref: CGR
        - ". La incorporación al sistema y las modalidades de uso se deberán realizar de acuerdo con las instrucciones que la"
        - Ref: CGR
        - "emita al efecto. Lo anterior, sin perjuicio de las autorizaciones vigentes otorgadas por la"
        - Ref: CGR
        - "a determinados organismos públicos para el uso de sistemas digitales propios de rendición de cuentas. Será responsabilidad de los órganos y servicios públicos velar por el buen uso de la plataforma y por la veracidad de la información que en ella se registre. Asimismo, será responsabilidad de dichos órganos y servicios exigir que los receptores cumplan con la obligación de rendir cuentas, verificar el correcto uso de los recursos y exigir sus restituciones, si correspondiere. Salvo que los respectivos convenios dispongan un plazo diferente, los organismos públicos tendrán el plazo máximo de tres meses para pronunciarse de manera fundada acerca de la rendición de cuentas otorgadas por las instituciones privadas respectivas. 6. Deberá acreditarse que el receptor ha cumplido con las obligaciones de rendir cuenta respecto de cualquier otro convenio suscrito con el órgano que efectúa la transferencia, en su caso. Deberá incorporarse una cláusula que exija la restitución de los recursos transferidos en caso de que éstos sean destinados a una finalidad distinta de aquella para la cual fueron asignados, o bien, no hayan sido utilizados o rendidos o hayan sido observados en el proceso de revisión de la rendición de cuentas."
    Articulo_25:
      ID: GN-LEY-PPTO-2026-ART25
      Contenido:
        - "Artículo 25.- Además de los requisitos del artículo anterior, los convenios que se suscriban en que se establezcan transferencias de recursos a instituciones privadas ejecutoras de políticas públicas deberán cumplir con lo siguiente: a) Sólo se podrán suscribir convenios con aquellas instituciones privadas que al momento de la postulación tengan a lo menos dos años de antigüedad contados desde su constitución, y que demuestren experiencia en el área de ejecución del convenio. Para estos efectos, al momento de suscribir el convenio se deberá requerir un certificado de vigencia otorgado por el organismo competente en que se acredite la antigüedad de la institución. Asimismo, al momento de la postulación, se requerirán antecedentes que demuestren la experiencia de la institución privada o de los responsables del equipo de trabajo que ejecuten el proyecto asociado al convenio. b) Las instituciones privadas que suscriban convenios deberán constituir una o más garantías a favor del órgano de la Administración, con el objeto de garantizar el fiel cumplimiento de las obligaciones establecidas en el convenio, cuando el total del monto de los recursos que se transfieran supere las 1.000 unidades tributarias mensuales. Dichas garantías deberán consistir en vales vistas, boletas de garantía, pólizas de seguro, depósitos a plazo, certificados de fianza u otros instrumentos que permitan su cobro inmediato, y deberán ascender al cinco por ciento del monto total de los recursos a transferir. Para estos efectos, se considerará el valor de la unidad tributaria mensual correspondiente al mes de enero del año de suscripción del convenio de transferencia. Los costos financieros en que incurran las instituciones privadas con motivo del proyecto o iniciativa podrán ser considerados en los convenios de transferencias correspondientes. c) Deberán considerar, como condición a la transferencia de los recursos, el cumplimiento de hitos diferidos en el tiempo, relacionados con el cumplimiento del objetivo para el que fueran asignados. Se podrán realizar anticipos por hasta el veinte por ciento, de conformidad a lo que establezca el convenio. Si es que la prestación carece de hitos específicos, se deberán establecer transferencias parceladas en el tiempo. d) Se podrá autorizar la subcontratación con terceros para las actividades que no constituyan el objeto principal del convenio, las cuales deberán estar claramente precisadas en éste. Excepcionalmente, se podrá autorizar la subcontratación del objeto principal del convenio cuando se advierta la imposibilidad de darle cumplimiento. Para estos efectos, el jefe de servicio deberá emitir una resolución fundada que especifique las razones de la subcontratación. El convenio deberá incorporar todas las actividades, los montos y las instituciones que serán subcontratadas. En ningún caso dicha subcontratación se podrá realizar con personas relacionadas, en conformidad a lo dispuesto en el artículo 100 de la ley N° 18.045. Se deberá enviar a las Comisiones de Hacienda de la Cámara de Diputados y del Senado una copia de la resolución y el convenio de cada excepcionalidad. e) No se podrá fraccionar en distintos convenios la asignación de recursos a una misma institución privada, cuando éstos estén destinados a un mismo objetivo dentro de una región o a nivel nacional y, además, provengan de una misma asignación o programa presupuestario. Para estos efectos, deberá dejarse constancia en el convenio de la existencia de otros convenios suscritos por la institución privada con el mismo organismo y que se encuentren vigentes. Los organismos públicos deberán publicar el llamado a postulación al concurso público, su acta de evaluación, el acto administrativo de adjudicación, el proyecto y presupuesto adjudicado y el convenio asociado a éste en los sitios electrónicos en los que dan cumplimiento a las obligaciones de transparencia activa, de forma permanente, completa y actualizada, en el plazo no mayor de quince días corridos una vez firmado el mencionado convenio. La misma obligación recaerá sobre la institución privada receptora de transferencias por un monto mayor a 2.000 unidades tributarias mensuales, la cual además del proyecto y presupuesto adjudicado y el convenio asociado a éste, deberá publicar en su sitio electrónico los estados financieros, balance y memoria anual de actividades. Asimismo, deberá publicar la nómina de su directorio en ejercicio o de su órgano superior de administración, administradores principales y los recursos recibidos por fecha, monto y organismo otorgante. La institución privada receptora, en la misma oportunidad en la que realice las mencionadas publicaciones, deberá remitir dicha información al organismo público correspondiente, el cual deberá publicarla en el sitio electrónico en el que da cumplimiento a las obligaciones de transparencia activa. De acuerdo con lo dispuesto en el artículo 8° del artículo primero de la"
        - Ref: LEY20285
        - ", sobre acceso a la información pública, cualquier persona podrá reclamar ante el Consejo para la Transparencia, si el organismo público correspondiente no realiza las publicaciones indicadas en este inciso, o no actualiza la información. El Ministerio de Hacienda podrá impartir instrucciones complementarias de aplicación general respecto del contenido de los convenios, o de las reglas a que deben atenerse los concursos para su adjudicación. El jefe de servicio o la máxima autoridad del órgano respectivo velará por el íntegro cumplimiento de estas instrucciones."
    Articulo_26:
      ID: GN-LEY-PPTO-2026-ART26
      Contenido:
        - "Artículo 26.- Los organismos públicos receptores de recursos provenientes de transferencias, que deban reintegrarlos a rentas generales de la nación, porque no han sido utilizados o por cualquier otro motivo, deberán hacerlo a más tardar dentro del mes siguiente al cierre de la rendición de cuentas del respectivo convenio. El proceso de rendición de cuentas no podrá extenderse por más de seis meses contados desde la finalización de la ejecución del convenio. Los receptores privados que se encuentren en la obligación de restituir recursos transferidos deberán hacerlo al organismo público correspondiente, dentro del plazo máximo de sesenta días hábiles contado desde el término del respectivo convenio. Luego de la recepción de los recursos, el organismo público deberá reintegrar dichos recursos a rentas generales de la Nación, a más tardar al mes siguiente de su recepción. En el caso de los organismos públicos, se entenderá por recursos transferidos no utilizados, los saldos no utilizados al término de la ejecución de las actividades convenidas. Si se trata de instituciones privadas, serán los que se encuentren en dicha situación al término del respectivo convenio. Si se trata de transferencias consolidables entre organismos del Sector Público, éstas podrán efectuarse sin necesidad de suscripción de un convenio por parte de los organismos involucrados, mediante resoluciones exentas de los respectivos jefes de servicio, sin perjuicio de su posterior envío a la"
        - Ref: CGR
        - ". Lo anterior, no obstante lo que dispongan las glosas aplicables de esta ley o de las facultades de las jefas y los jefes de servicio en este sentido. Los convenios de transferencias a municipalidades deberán incluir la información de las contrataciones de personal que se vayan a celebrar para el cumplimiento del objeto del convenio, así como su calidad jurídica. Los convenios de transferencia deberán regular el destino de los bienes muebles adquiridos con cargo a los recursos transferidos, al término de la ejecución de los programas. Con autorización previa de la"
        - Ref: DIPRES
        - "los órganos públicos podrán comprometer transferencias a otros órganos del Sector Público que excedan el ejercicio presupuestario."
    Articulo_27:
      ID: GN-LEY-PPTO-2026-ART27
      Contenido:
        - "Artículo 27.- Sin perjuicio de lo dispuesto en el artículo 12 de la ley N° 19.880, las autoridades, las funcionarias y los funcionarios públicos y el personal contratado sobre la base de honorarios, no podrán participar o intervenir en modo alguno en el proceso de concursabilidad, adjudicación o suscripción de un convenio, cuando se encuentren en las siguientes situaciones: 1. Cuando tengan la calidad de cónyuge, conviviente civil, o parientes hasta el cuarto grado de consanguinidad o tercero de afinidad inclusive, o tengan hijo o hija en común, con los miembros del directorio o de los ejecutivos o administradores principales de una institución privada que forme parte de un proceso concursal. 2. Cuando hayan trabajado, prestado servicios remunerados o no, o desempeñado labores directivas en una institución privada que forme parte de un proceso concursal, en los dos años inmediatamente anteriores contados desde que asumieron el cargo público que desempeñan. 3. Cuando hayan emitido opinión, por cualquier medio, sobre un procedimiento concursal en curso y cuya resolución de adjudicación se encuentre pendiente. En el acta o las actas que se levanten durante el proceso concursal deberá dejarse constancia de la nómina de las funcionarias y los funcionarios públicos y del personal contratado sobre la base de honorarios que intervinieron en éste."
    Articulo_28:
      ID: GN-LEY-PPTO-2026-ART28
      Purp: Permitir asignación conjunta de transferencias corrientes/capital con mismo objeto y denominación.
      Cond: Organismos públicos regidos por esta ley
      Ctx_Asignaciones:
        Transferencias_Corrientes:
          - Sector privado
          - Otras entidades públicas
          - Instituciones privadas ejecutoras de política pública
        Transferencias_Capital:
          - Sector privado
          - Otras entidades públicas
        Cond_Adicional: Destinadas al mismo objeto y con la misma denominación
      Proc_Asignacion_Conjunta:
        Act:
          - Efectuar procesos de asignación en forma conjunta
          - Imputar gasto a ítems 01, 03 y 08 según corresponda
      Regularizacion:
        Proc: Decreto de modificación presupuestaria
        Cond: Dictado con posterioridad a la adjudicación
        Req: Regularizar asignación de recursos asociados a estas transferencias
      Prohib:
        Desc: Asignación de recursos no podrá superar la suma de los ítems involucrados en conjunto
    Articulo_29:
      ID: GN-LEY-PPTO-2026-ART29
      Purp: Mantener vigencia de actos/contratos previos con imputación distinta, hasta su terminación.
      Cond: Actos y contratos ejecutados/celebrados con anterioridad a la entrada en vigencia de la presente ley
      Cond_Adicional: Imputación presupuestaria afecta a asignación/ítem/subtítulo distinto del que corresponde según este ordenamiento
      Res: Continuarán produciendo efectos hasta su terminación
      Ctx: Con cargo a la asignación/ítem/subtítulo que corresponda de acuerdo con esta ley
    Articulo_30:
      ID: GN-LEY-PPTO-2026-ART30
      Purp: Reglas sobre arriendo de infraestructura, recuperación subsidios licencias médicas, aplicabilidad y obligatoriedad de instructivos.
      Arriendo_Infraestructura_Actividades_Institucionales:
        Obj: Arriendo infraestructura para actividades institucionales (reuniones, jornadas planificación u otras similares)
        Req:
          Desc: Sólo autorizarse si el servicio no cuenta con infraestructura propia para ello
        Req_Adicional:
          Desc: Ni pueda ser facilitada por otro servicio público
      Recuperacion_Subsidios_Licencias_Medicas:
        Req: Servicios públicos deben efectuar gestiones necesarias para recuperar montos de subsidios por licencias médicas
        Origen: Instituciones de salud previsional
        Ctx:
          Ref: ISAPRE
        Devengamiento:
          Cond: Recuperación de licencias médicas de beneficiarios de ISAPRE
          Req: Realizarse dentro del mes siguiente al que se presentó la situación
        Cobro_Integro:
          Req: Realizar todas las gestiones para percibir el íntegro
          Plazo: 45 días corridos desde fecha de pago de la respectiva remuneración mensual
          Req_Adicional: Ingresarlos a rentas generales de la Nación
        Instrucciones_Tecnicas:
          Act: Emitir instrucciones técnicas generales para materializar estos procesos
          Ref: TGR
        Auditoria_Interna:
          Req: Unidades de auditoría interna deben verificar cumplimiento estricto de lo dispuesto en este inciso
          Req_Reporte:
            Frecuencia: Trimestral
            Destinatario:
              Ref: CAIGG
      Aplicabilidad:
        Ctx:
          - Ref: GN-LEY-PPTO-2026-ART22
          - Incisos anteriores del presente artículo
        Aplica:
          - Empresas del Estado (incluye Ref: TVN)
          - Empresas del Estado (incluye Ref: CODELCO)
          - Empresas del Estado (incluye Ref: BANCOESTADO)
          - Sociedades donde el Estado/sus instituciones o empresas tengan aporte de capital >=50%
        Cond: En lo pertinente
      Instructivos_Buen_Uso_Recursos_Fiscales:
        Act: Dictar instructivos sobre buen uso de recursos fiscales
        Autoridad:
          - Presidente de la República
          - Ref: MINHACIENDA
        Res: Serán obligatorios
        Sujetos:
          - Órganos de la Administración Central del Estado
          - Gobiernos regionales
    Articulo_31:
      ID: GN-LEY-PPTO-2026-ART31
      Purp: Facultar al Ministerio de Hacienda para impartir instrucciones a empresas del Estado y sociedades con capital estatal >=50%.
      Instrucciones_MINHACIENDA:
        Act: Impartir instrucciones generales
        Ref: MINHACIENDA
        Materias_Generales:
          - Presupuesto de caja
          - Endeudamiento
          - Personal
          - Proyectos de inversión
        Act_Adicional: Impartir instrucciones específicas
        Materias_Especificas:
          - Viajes al exterior
          - Gastos de publicidad
          - Responsabilidad empresarial
        Aplicabilidad:
          Aplica:
            - Empresas del Estado (incluye Ref: TVN)
            - Empresas del Estado (incluye Ref: CODELCO)
            - Empresas del Estado (incluye Ref: BANCOESTADO)
            - Sociedades donde el Estado/sus instituciones o empresas tengan aporte de capital >=50%
        Informe:
          Req: Enviar copia de estas instrucciones a
          Ref: CEMP
          Plazo: A más tardar treinta días después de que sean emitidas
    Articulo_32:
      ID: GN-LEY-PPTO-2026-ART32
      Purp: Prohibir dieta/remuneración por integrar órganos en empresas/entidades públicas que incrementen remuneración del cargo.
      Sujetos:
        - Desc: Funcionarias y funcionarios públicos regulados por
          Ref: LEY18834
          Ctx:
            Desc: Texto refundido, coordinado y sistematizado fijado por
            Ref: DFL29_2004
        - Presidente de la República
        - Ministras y ministros de Estado
        - Subsecretarias y subsecretarios
        - Gobernadoras y gobernadores regionales
        - Delegadas y delegados presidenciales regionales
        - Desc: Jefas y jefes superiores de servicios públicos regidos por Título II
          Ref: LEY18575
          Ctx:
            Desc: Texto refundido, coordinado y sistematizado fija
            Ref: DFL1_19653_2000
      Prohib:
        Desc: No tendrán derecho a percibir dieta o remuneración por integrar consejos o juntas directivas, presidencias, vicepresidencias, directorios, comités u otros equivalentes con cualquier nomenclatura
        Cond: Empresas o entidades públicas que incrementen la remuneración correspondiente a los cargos regulados por las leyes señaladas
    Articulo_33:
      ID: GN-LEY-PPTO-2026-ART33
      Purp: Reglas dotación máxima vehículos motorizados y procedimiento de aumento/traspaso.
      Dotacion_Maxima_Vehiculos:
        Ctx: Fijada en Partidas de esta ley para servicios públicos
        Alcance: Transporte terrestre de pasajeros y de carga
        Incluye: Vehículos adquiridos directamente con cargo a proyectos de inversión
      Aumento_Dotacion:
        Act: Aumentar dotación respecto de alguno de los vehículos
        Proc:
          Desc: Decreto dictado en la forma dispuesta en
          Ref: DL1263_ART70
        Cond: Con cargo a disminución dotación máxima de otros servicios
        Prohib: No aumentar en caso alguno la dotación máxima del ministerio de que se trate
      Traspaso_Vehiculos:
        Res:
          - Decreto supremo respectivo dispondrá traspaso de vehículos desde el servicio en que se disminuye a aquel en que se aumenta
          - Decreto servirá de suficiente título para transferir dominio
        Req:
          - Vehículos deberán ser debidamente identificados
          - Inscripción en Registro de Vehículos Motorizados del Servicio de Registro Civil e Identificación
    Articulo_34:
      ID: GN-LEY-PPTO-2026-ART34
      Purp: Autorizar pagos/giros excedibles y regularización posterior por decretos.
      Sujetos: Órganos y servicios públicos del Gobierno Central incluidos en esta ley
      Act:
        - Efectuar pagos imputables a "Subtítulo 34, ítem 07: Deuda Flotante"
        - Efectuar giros imputables a "Subtítulo 25, ítem 99: Otros Integros al Fisco"
        - Excederse de las sumas fijadas
      Ctx:
        Desc: En los términos señalados en
        Ref: DL1263_ART28
      Regularizacion_Excesos:
        Act: Exceder montos establecidos en respectivas asignaciones
        Act_Adicional: Sancionar posteriormente excesos
        Proc:
          Desc: Mediante decretos del
          Ref: MINHACIENDA
        Proc_Adicional:
          Desc: Dictados en la forma dispuesta en
          Ref: DL1263_ART70
    Articulo_35:
      ID: GN-LEY-PPTO-2026-ART35
      Purp: Estándar de entrega de información digital procesable y consecuencias por incumplimiento.
      Req_Formato_Informacion:
        Cond: Información que deba ser puesta a disposición según artículos de esta ley y respectivas glosas
        Sujetos:
          - Cualquier órgano de la Administración del Estado
          - Principalmente ministerios
          - Ref: DIPRES
        Destinatarios: Diversas instancias del Congreso Nacional
        Req: Proporcionar sólo en formato digital procesable por software de análisis de datos
        Formatos:
          - Planillas de cálculos
          - Archivos de texto plano
      Incumplimiento:
        Cond: Incumplimiento de cualquiera de los deberes de información contenidos en esta ley
        Res: Procedimiento y sanciones según artículo 10
        Ref: LEY18918
      Proc_Envio_Antecedentes_CGR:
        Cond: Solicitud de cualquier diputado o senador
        Act: Presidenta o Presidente de la Cámara de Diputados o del Senado remitirá antecedentes a
        Ref: CGR
        Req: Dar cuenta de dicha acción en la respectiva sesión
    Articulo_36:
      ID: GN-LEY-PPTO-2026-ART36
      Purp: Autorizar postergar cumplimiento obligación transitoria Ley 21.174 hasta vigencia de esta ley; resguardar obligaciones Ley 18.948.
      Postergacion:
        Autoridad: Fisco
        Inicio: Desde fecha de publicación de esta ley
        Fin: Hasta vigencia de esta ley
        Obj: Cumplimiento obligación contenida en artículo tercero transitorio
        Ref: LEY21174
        Ctx: Traspaso de saldos al Fondo de Contingencia Estratégico
      Resguardo:
        Prohib:
          Desc: Lo dispuesto en el inciso anterior no afectará en modo alguno el cumplimiento de obligaciones derivadas de la aplicación del artículo 102
          Ref: LEY18948
    Articulo_37:
      ID: GN-LEY-PPTO-2026-ART37
      Purp: Reglas informe CGR para gastos reservados 2026 (suscripción conjunta + visto bueno ministro + contenido suficiente).
      Ctx:
        Cond: Gastos reservados asignados para año 2026
      Informe_CGR:
        Ctx:
          Base_Legal:
            Desc: Inciso tercero del artículo 4
            Ref: LEY19863
        Req_Suscripcion:
          Req: Suscribirse en conjunto por
          Sujetos:
            - Jefa o jefe de servicio
            - Jefas o jefes de unidades operativas con gastos reservados a su cargo
        Req_Visto_Bueno:
          Req: Contar además con visto bueno del ministro o ministra respectiva
          Incluye:
            - Subsecretaría del Interior
            - Subsecretaría de Relaciones Exteriores
            - Subsecretarías de Defensa
            - Subsecretarías de las Fuerzas Armadas
        Req_Contenido:
          Req: Contar con información suficiente para permitir al Contralor General de la República verificar
          Verifica:
            - Cumplimiento fines establecidos en artículo 2
            - Cumplimiento de lo dispuesto en artículo 6
          Ref: LEY19863
    Articulo_38:
      ID: GN-LEY-PPTO-2026-ART38
      Purp: Visaciones e informes previos para enajenación de inmuebles (patrimonios afectación fiscal) durante 2026.
      Periodo: Año 2026
      Visacion_Inmuebles_FFAA:
        Cond: Enajenación de bienes inmuebles que formen parte del patrimonio de afectación fiscal de
          - Comando de Industria Militar e Ingeniería del Ejército
          - Servicios de Bienestar de las Fuerzas Armadas
        Req: Visación del Ministerio de Defensa Nacional y del Ministerio de Bienes Nacionales
      Visacion_Inmuebles_Carabineros_PDI:
        Cond: Enajenación de bienes inmuebles que formen parte del patrimonio de afectación fiscal de
          - Comando de Industria Militar e Ingeniería del Ejército
          - Servicio de Bienestar de Carabineros de Chile
          - Jefatura de Bienestar de la Policía de Investigaciones de Chile
        Req: Visación del Ministerio de Seguridad Pública y del Ministerio de Bienes Nacionales
      Informe_Previo:
        Req: Enajenaciones deberán ser informadas previamente
        Autoridad:
          - Ministerio de Defensa Nacional
          - Ministerio de Seguridad Pública
        Cond: Según corresponda
        Destinatarios:
          - Ministerio de Vivienda y Urbanismo
          - Ref: CEMP
    Articulo_39:
      ID: GN-LEY-PPTO-2026-ART39
      Purp: Límite anual 2026 para operaciones cobertura riesgos financieros (entidades autorizadas Ley 19.908).
      Periodo: Año 2026
      Limite_Montos:
        Cond: Suma montos involucrados en operaciones de cobertura de riesgos financieros celebradas por entidades autorizadas en artículo 5
        Ref: LEY19908
        Prohib: No exceder de US$4.000.000 miles o equivalente en moneda nacional
      Req:
        Desc: Operaciones deben efectuarse con sujeción a lo dispuesto en
        Ref: LEY19908
    Articulo_40:
      ID: GN-LEY-PPTO-2026-ART40
      Purp: Coordinación y excepciones presupuestarias ante emergencias/desastres/catástrofes; reglas rehabilitación/reconstrucción.
      Emergencia_Declarada:
        Cond: Emergencia, desastre o catástrofe declarada
        Ref: LEY16282
      Rehabilitacion:
        Cond: Requieran recursos para financiar etapa de rehabilitación
        Ref: LEY21364
        Req:
          Desc: Solicitudes de diferentes servicios públicos coordinadas por
          Ref: SUBINT
        Comite_Ayudas_Tempranas:
          Act: Coordinar comité
          Ref: SUBINT
          Integrantes:
            - Subsecretaría de Servicios Sociales
            - Ref: SENAPRED
          Obj: Proponer plan del Gobierno Central en ayuda inmediata a los afectados
          Proc:
            Req: Presentar plan a
            Ref: DIPRES
            Obj: Aprobar financiamiento
      Reconstruccion:
        Cond: Requieran recursos para financiar etapa de reconstrucción
        Ref: LEY21364
        Req: Solicitudes de diferentes servicios públicos coordinadas por Comité de Reconstrucción
        Proc:
          Req: Funcionamiento regulado por
          Ref: DS2_2024_MDSF
          Ctx: Eventuales modificaciones o norma que lo reemplace
      Exencion_Articulos_23_26:
        Cond: Situaciones de emergencia declaradas según normas sectoriales pertinentes
        Ctx: Asignaciones presupuestarias habilitadas para la respuesta
        Ejemplos_Asignaciones:
          - Desc: Asignación Para Atender Situaciones de Emergencia (Subsecretaría del Interior)
          - Desc: Asignación Emergencias Agrícolas (Subsecretaría de Agricultura)
            Ref: SUBAGRI
          - Desc: Asignación Emergencias (Instituto de Desarrollo Agropecuario)
            Ref: INDAP
          - Desc: Asignación Emergencias Sanitarias (Servicio Agrícola y Ganadero)
            Ref: SAG
          - Desc: Asignación Programas Especiales (Servicio de Cooperación Técnica)
            Ref: SERCOTEC
        Condicion:
          Res: Podrán eximirse de la aplicación de
          Ref:
            - GN-LEY-PPTO-2026-ART23
            - GN-LEY-PPTO-2026-ART24
            - GN-LEY-PPTO-2026-ART25
            - GN-LEY-PPTO-2026-ART26
        Publicacion:
          Req: Publicar planes y estrategias vigentes en sitio electrónico del
          Ref: MINHACIENDA
        Informe_Mensual:
          Req: Informar contenido y ejecución mensual a
          Ref: CEMP
      Intervencion_MOP:
        Cond: Emergencia, desastre o catástrofe declarada
        Ref: LEY16282
        Act: Ministerio de Obras Públicas podrá intervenir infraestructura vial y de canales de propiedad privada
        Req: Previa autorización del o los adquirentes
      Procedimiento_Abreviado_Admisibilidad:
        Ctx: Proyectos de fomento productivo, conservación y reconstrucción de infraestructura dañada producto de las ocurrencias señaladas en el inciso anterior
        Act: Disponer procedimiento abreviado para declaración de admisibilidad de iniciativas
        Autoridad:
          - Ref: MDSF
          - Ref: MINHACIENDA
        Plazo: Debe estar publicado a más tardar el 31 de enero de 2026
    Articulo_41:
      ID: GN-LEY-PPTO-2026-ART41
      Purp: Suspender traspaso servicio educacional a SLEP durante 2026; habilitar ajustes presupuestarios por decreto.
      Traspaso_Servicio_Educacional:
        Ctx:
          Base_Legal: Artículo octavo transitorio
          Ref: LEY21040
        Origen: Municipalidades y corporaciones municipales que correspondan
        Destino: Servicios Locales de Educación Pública señalados en
        Ctx_Decreto:
          Ref: DS162_2022_MINEDUC
          Ctx: Capítulo II Títulos I (Antofagasta) y VII (Valle Cachapoal); Capítulo III Títulos I (Litoral), II (Hanga Roa), IV (La Quebrada), V (Talagante); VII (Los Cerezos), IX (Los Copihues), X (Reloncaví), XI (Chacabuco) y XII (Los Viñedos) y sus modificaciones
        Res: No se producirá el año 2026
      Ajustes_Presupuestarios:
        Cond: Para efectos de lo dispuesto en el inciso anterior
        Act: Presidente de la República podrá crear, suprimir o modificar Capítulos, Programas, Subtítulos, ítems, asignaciones y glosas presupuestarias pertinentes
        Proc:
          Desc: Decreto expedido por intermedio del
          Ref: MINHACIENDA
          Ctx: Bajo la fórmula "por orden del Presidente de la República"
    Articulo_42:
      ID: GN-LEY-PPTO-2026-ART42
      Purp: Plataforma informática MINHACIENDA para publicación de recursos asignados, ejecución transaccional y respaldos.
      Plataforma_Informatica:
        Autoridad:
          Ref: MINHACIENDA
        Req: Mantener plataforma
        Req_Publicacion:
          Req: Publicar información detallada sobre
          Contenido:
            - Recursos asignados
            - Ejecución mensual a nivel transaccional para organismos del Gobierno Central
            - Respaldos documentales respectivos
        Publicacion_Detalle:
          - Por regiones
          - Principales receptores de recursos
          - Proveedores del Estado
    Articulo_43:
      ID: GN-LEY-PPTO-2026-ART43
      Purp: Habilitar uso de caja (recursos autorizados + ingresos propios) para financiar conceptos legales de gasto, resguardando fines.
      Ctx:
        Ref: DL1263_ART6
      Criterio:
        Purp: Garantizar criterios de buena administración en función de la liquidez de recursos disponibles
      Caja_Disponible:
        Act: Habilitar a órganos y servicios públicos para disponer de caja resultante de
        Fuentes:
          - Totalidad de recursos autorizados por la presente ley
          - Ingresos propios
        Obj: Financiamiento de cualquiera de sus conceptos legales de gasto
      Resguardo_Fines:
        Prohib: En caso alguno supone destinar recursos a fines distintos a los establecidos por la ley
        Res: Garantiza atender de manera más eficaz y eficiente necesidades de los órganos o servicios públicos
    Articulo_44:
      ID: GN-LEY-PPTO-2026-ART44
      Purp: Ajustar fecha obligatoriedad de régimen Título III DFL 1/1996 para profesionales de educación (Ley 20.903); establecer excepción por evaluación.
      Regla_Obligatoriedad:
        Cond: Profesionales de la educación dependientes de sostenedores o administradores regidos por Párrafo Tercero disposiciones transitorias
        Ref: LEY20903
        Cond_Adicional:
          Desc: No hayan pasado a regirse por Título III
          Ref: DFL1_1996_MINEDUC
          Ctx: A la fecha de publicación de la presente ley
        Res:
          Desc: Regirse obligatoriamente a contar de julio de 2027
        Ctx:
          Desc: En lugar del momento dispuesto por el artículo trigésimo transitorio
          Ref: LEY20903
        Ctx_Adicional:
          Desc: Sin perjuicio del derecho consagrado en el artículo vigésimo cuarto transitorio
          Ref: LEY20903
      Excepcion:
        Cond:
          Desc: Profesionales de la educación que hayan rendido instrumentos de evaluación contemplados en
          Ref: DFL1_1996_ART19K
        Cond_Adicional:
          - Proceso evaluación docente año 2025
          - Proceso evaluación docente año 2026
        Req:
          Desc: Además sean reconocidos en resolución que establece
          Ref: DFL1_1996_ART19Q
    Articulo_45:
      ID: GN-LEY-PPTO-2026-ART45
      Purp: Traspasar personal Programa Asuntos Indígenas desde MDSF a Ministerio del Interior, sin solución de continuidad.
      Traspaso:
        Inicio: Desde fecha de publicación de esta ley
        Ctx: Sin solución de continuidad
        Limites:
          Funcionarios_Contrata_Max: 8
          Personas_Honorarios_Max: 9
        Cond: Se desempeñan en Programa Asuntos Indígenas (Partida 21.01.01 Ley de Presupuestos del Sector Público 2025)
        Origen:
          Ref: MDSF
        Destino:
          Ref: MININTERIOR
      Decreto_Exento_Individualizacion:
        Proc:
          Desc: Decreto exento del
          Ref: MDSF
        Req:
          Desc: Suscrito además por el Ministro de Hacienda
          Ref: MINHACIENDA
        Ctx: Expedido bajo la fórmula "por orden del Presidente de la República"
        Res: Individualizará a funcionarios a contrata y personas contratadas sobre base honorarios traspasados
    Articulo_46:
      ID: GN-LEY-PPTO-2026-ART46
      Purp: Autorizar aporte fiscal 2026 a Fondo de Garantías Especiales.
      Periodo: Año 2026
      Aporte_Fiscal:
        Autoridad: Fisco
        Monto_Maximo: 100.000.000 dólares de los Estados Unidos de América
        Equivalencia: Moneda nacional
        Destino:
          Ctx: Persona jurídica de derecho público denominada
          Ref: FGE
        Ctx:
          Desc: Creada por
          Ref: LEY21543
    Articulo_47:
      ID: GN-LEY-PPTO-2026-ART47
      Purp: Plan de Ejecución y Recuperación de Saldos para sostenedores con saldos SEP registrados por Superintendencia de Educación; reintegros, cobro y reportes.
      Sujetos:
        Cond: Sostenedores de establecimientos educacionales
        Cond_Adicional:
          Desc: Hayan percibido subvención escolar preferencial regulada en
          Ref: LEY20248
        Cond_Saldos:
          Ctx:
            Desc: Conforme a lo registrado por
            Ref: SUPEREDUC
          Cond: Cuenten con saldos acreditados o no acreditados derivados de Convenios de Igualdad de Oportunidades y Excelencia Educativa
          Cond_Adicional: Convenios hayan expirado a la fecha de entrada en vigencia de la presente ley
      Plan:
        ID: GN-LEY-PPTO-2026-ART47-PLAN
        Req: Presentar Plan de Ejecución y Recuperación de Saldos
        Destinatario:
          Ref: MINEDUC
        Plazo: A más tardar el 30 de abril de 2026
        Req_Formato:
          Req: De acuerdo al formato que el Ministerio ponga a disposición de los sostenedores
          Ref: MINEDUC
        Alcance_Saldos:
          Req: Considerará todo o parte de los saldos indicados en el inciso primero que se encuentren registrados por
          Ref: SUPEREDUC
          Act_Adicional:
            Desc: Informará tales saldos
            Ref: SUPEREDUC
            Inicio: A partir de la publicación de la presente ley
        Obj:
          Desc: Permitir ejecutar acciones comprometidas en el Plan
          Req: Acciones deberán financiarse con cargo a los saldos señalados
        Ejecucion:
          Req: Contener acciones a financiar y oportunidad en la cual serán ejecutadas
          Prohib: Oportunidad no podrá exceder del 30 de septiembre de 2026
        Acciones_Permitidas:
          - ID: GN-LEY-PPTO-2026-ART47-A
            Desc: Financiar mantenimiento, reparación, construcción y habilitación de infraestructura y mobiliario esencial para funcionamiento de establecimientos educacionales
          - ID: GN-LEY-PPTO-2026-ART47-B
            Desc: Financiar acciones destinadas a reducir brechas de aprendizaje, promover inclusión y fortalecer trayectorias escolares
          - ID: GN-LEY-PPTO-2026-ART47-C
            Desc: Financiar acciones orientadas a fortalecer eficiencia y eficacia en gestión administrativa y financiera de establecimientos educacionales
            Incluye: Podrá considerar pago de deuda previsional respecto del personal docente y asistente de la educación que se desempeñe en los establecimientos educacionales del respectivo sostenedor
          - ID: GN-LEY-PPTO-2026-ART47-D
            Desc: Destinar recursos para fines educativos establecidos en el artículo 3
            Ref: DFL2_1998_MINEDUC
          - ID: GN-LEY-PPTO-2026-ART47-E
            Desc: Racionalizar dotación de profesionales y asistentes de la educación para optimizar estructuras de costos y garantizar sostenibilidad financiera en el tiempo
            Req: No se requerirá modificar el Plan Anual de Desarrollo Educativo Municipal
            Req_Adicional: Deberá dar cuenta de los ajustes correspondientes el plan anual del año siguiente
        Literal_A_Anio_2026:
          Cond: Para acciones previstas en literal a) precedente
          Res: Plan podrá considerar posibilidad de que se ejecuten durante el año 2026
      Resolucion_NoPresentacion_O_Parcial:
        Autoridad:
          Ref: MINEDUC
        Act: Dictar una o más resoluciones que individualicen sostenedores
        Cond:
          - No presenten el Plan dentro del plazo indicado en el inciso primero
          - Lo presenten por sólo parte de los saldos registrados
        Plazo_Emision: A más tardar en el mes de mayo de 2026
        Reintegro:
          Sujetos:
            - Sostenedor que no presente el Plan
            - Sostenedor que presente uno por sólo parte de los saldos registrados
          Req: Reintegrar dichos saldos, en una sola cuota, a rentas generales de la Nación
          Plazo: Dentro de treinta días hábiles a partir de la fecha en que se le notifique la resolución
          Notificacion:
            - De acuerdo a las reglas generales
            - Mediante correo electrónico
            - Mediante otra plataforma que usualmente el Ministerio de Educación utilice
      Resolucion_Constancia_Presentacion:
        Autoridad:
          Ref: MINEDUC
        Act: Dictar una o más resoluciones que dejen constancia de presentación del Plan ante el Ministerio, por el total o parte de los saldos registrados, según corresponda
        Req: Establecer mecanismos de rendición de cuentas simplificadas respecto del uso de dichos recursos
        Incumplimiento:
          Cond: Sostenedor incumpla total o parcialmente el Plan
          Req: Reintegrar a rentas generales de la Nación
          Plazos:
            - Plazo: A más tardar el 31 de julio de 2026
              Obj: Totalidad de montos no ejecutados
            - Plazo: A más tardar el 30 de octubre de 2026
              Cond: En el caso del literal a) del inciso tercero
      Merito_Ejecutivo:
        Res: Resoluciones señaladas en los incisos quinto y sexto tendrán mérito ejecutivo
        Proc:
          Req: Acción se deducirá ante tribunal ordinario competente
          Proc: Se someterá a normas del juicio ejecutivo establecidas en
          Ref: CPC
          Plazo_Prescripcion: 3 años desde fecha de dictación de la resolución
          Ctx: Podrá, en todo caso, subsistir como una acción de cobro ordinaria
      Municipalidades_Corporaciones_Municipales:
        Cond: Municipios y corporaciones municipales deban reintegrar los saldos registrados
        Res: Montos podrán ser descontados, luego de ser debidamente reajustados, de recursos que a la municipalidad respectiva le corresponda percibir por participación en
        Ref: FCM
        Ctx:
          Desc: Establecido en
          Ref: DL3063_1979
          Ctx_Adicional:
            Desc: Texto refundido, coordinado y sistematizado fue fijado por
            Ref: DS2385_1996_MININTERIOR
        Cuotas_2026:
          Autoridad:
            Ref: SUBDERE
          Act: Determinar, mediante resolución exenta de carácter general o particular, el número de cuotas en que se reintegrarán durante el año 2026 a rentas generales de la Nación los montos correspondientes
      Instrucciones_Implementacion:
        Inicio: A partir de la publicación de esta ley
        Autoridad:
          Ref: SUBEDUC
        Act: Mediante resolución exenta, podrá impartir instrucciones de general aplicación para efectos de la implementación de este artículo
      Informe_Trimestral:
        Req: Información respecto de avances del Plan y del reintegro de recursos debe ser remitida trimestralmente
        Plazo: Dentro de los treinta días siguientes al término del respectivo trimestre
        Remitente:
          Ref: MINEDUC
        Destinatarios:
          - Ref: CEMP
          - Comisiones de Educación de la Cámara de Diputados
          - Comisiones de Educación del Senado
    Articulo_48:
      ID: GN-LEY-PPTO-2026-ART48
      Purp: Vigencia ley 2026 y habilitación de actos desde publicación.
      Vigencia:
        Fecha: 1 de enero de 2026
      Ctx:
        Desc: Sin perjuicio de decretos, resoluciones y convenios necesarios para posibilitar ejecución presupuestaria
        Inicio: A contar de la fecha de publicación de esta ley
      Publicacion:
        Rec: Esta ley y las instrucciones para su ejecución podrán ser publicadas en su integridad para su distribución
    Articulo_49:
      ID: GN-LEY-PPTO-2026-ART49
      Purp: Prohibir celebraciones con gasto fiscal; establecer excepción.
      Prohib:
        Desc: Ministerios y servicios públicos no podrán realizar celebraciones generales ni de aniversarios que impliquen desembolsar gasto fiscal
      Excepcion:
        Cond: Embajadas y consulados en el extranjero
        Ctx: Conmemoración del día de la independencia nacional
    Articulo_50:
      ID: GN-LEY-PPTO-2026-ART50
      Purp: Instrucciones DIPRES para resguardar cumplimiento política fiscal.
      Cond:
        - Presentación informe finanzas públicas cuarto trimestre 2025
        - Revisión comportamiento ingresos y otras variables macroeconómicas
      Act:
        Desc: Impartirá instrucciones con objetivo resguardar cumplimiento de política fiscal
        Ref: DIPRES
      Ctx:
        Desc: Política fiscal establecida de conformidad con el artículo 1°
        Ref: LEY20128
    Articulo_51:
      ID: GN-LEY-PPTO-2026-ART51
      Purp: Preferencia asignación vacantes admisión escolar 2027 según nacionalidad/regularidad migratoria.
      Cond: Proceso de Admisión Escolar correspondiente al año 2027
      Req:
        Desc: Ministerio de Educación debe ejecutar acciones necesarias para otorgar preferencia en asignación de vacantes
        Ref: MINEDUC
      Beneficiarios_Preferencia:
        - Personas de nacionalidad chilena
        - Extranjeros en situación migratoria regular
      Postulantes_Migratoria_Irregular:
        Cond: Postulantes en condición migratoria irregular
        Req: Establecimientos educacionales deberán proceder a enrolamiento y registro conforme a artículo 44
        Ref: LEY21325
    Articulo_52:
      ID: GN-LEY-PPTO-2026-ART52
      Purp: Condicionar dictación de decreto supremo (Ley 21.600) a dictación previa de reglamento.
      Periodo: Año 2026
      Cond:
        Desc: Dictación del decreto supremo al que hace referencia el artículo octavo transitorio
        Ref: LEY21600
      Req:
        Desc: Requerirá previamente dictación del reglamento a que se refiere el artículo 29 de la misma ley
        Ref: LEY21600
    Articulo_53:
      ID: GN-LEY-PPTO-2026-ART53
      Purp: Reporte semestral DIPRES sobre deudas públicas/obligaciones pago del Estado (consolidado + detalle).
      Informe_Semestral_Deudas_Publicas:
        Req: Remitir informe consolidado y detallado
        Autoridad:
          Ref: DIPRES
        Destinatario:
          Ref: CEMP
        Plazos:
          - Dentro del último día hábil del mes de junio de cada año
          - Dentro del último día hábil del mes de diciembre de cada año
        Periodo_Informado: Semestre inmediatamente anterior
        Contenido:
          Req: Identificar, para cada Partida, Capítulo y, cuando corresponda, Programa, a lo menos
          Desglose:
            - ID: GN-LEY-PPTO-2026-ART53-1
              Desc: "Deuda directa del Estado"
              Contenido: Saldo total de obligaciones devengadas y pendientes de pago del Fisco y de órganos del sector público comprendidos en la Ley de Presupuestos del Sector Público, incluidos compromisos contabilizados y toda otra obligación exigible con cargo a gastos presupuestarios
            - ID: GN-LEY-PPTO-2026-ART53-2
              Desc: "Desglose por antigüedad de la deuda"
              Contenido: Monto total de obligaciones pendientes de pago, clasificadas según tiempo transcurrido desde su devengamiento o recepción de la factura
              Tramos:
                - 0 a 30 días
                - 31 a 90 días
                - Más de 90 días
        Formato:
          Req: Presentarse en formato consolidado y en detalle por Partida y Capítulo
          Obj: Facilitar fiscalización parlamentaria gestión financiera
          Obj_Adicional: Servir de insumo para formulación de la Ley de Presupuestos del Sector Público del año siguiente
    Articulo_54:
      ID: GN-LEY-PPTO-2026-ART54
      Purp: Reportes sobre procedimientos disciplinarios por uso indebido de licencias médicas (a DIPRES, CEMP y otros destinatarios) y deber coordinación.
      Informe_Servicios_A_DIPRES:
        Sujetos: Jefes superiores de servicio de subsecretarías y de servicios públicos dependientes de ministerios o que se relacionen con Presidente de la República a través de ellos
        Req: Informar a
        Destinatario:
          Ref: DIPRES
        Materia: Procedimientos disciplinarios instruidos por uso indebido de licencias médicas
        Periodo_Procedimientos: Desde mayo de 2025 en adelante
        Plazo: A más tardar el 15 de enero de 2026
        Estado_Informacion: Actualizada al 31 de diciembre de 2025
        Contenido_Minimo:
          - ID: GN-LEY-PPTO-2026-ART54-1
            Desc: Número de funcionarios que presentaron su renuncia antes de instruirse un procedimiento disciplinario en su contra
          - ID: GN-LEY-PPTO-2026-ART54-2
            Desc: Número de procedimientos disciplinarios instruidos
          - ID: GN-LEY-PPTO-2026-ART54-3
            Desc: Número de funcionarios con procedimiento disciplinario instruido
          - ID: GN-LEY-PPTO-2026-ART54-4
            Desc: Duración promedio de la o las licencias investigadas (días corridos)
          - ID: GN-LEY-PPTO-2026-ART54-5
            Desc: Remuneraciones promedio de funcionarios objeto del procedimiento disciplinario (remuneración bruta mensualizada durante periodo en que se extendió la o las licencias investigadas)
          - ID: GN-LEY-PPTO-2026-ART54-6
            Desc: Número de funcionarios con procedimientos disciplinarios en etapa de investigación
          - ID: GN-LEY-PPTO-2026-ART54-7
            Desc: Número de funcionarios con procedimientos disciplinarios con vista de fiscal emitida
          - ID: GN-LEY-PPTO-2026-ART54-8
            Desc: Número de funcionarios cuyos procedimientos disciplinarios fueron resueltos por el Jefe Superior del Servicio
          - ID: GN-LEY-PPTO-2026-ART54-9
            Desc: Número de funcionarios a quienes se aplicó medida disciplinaria de censura
          - ID: GN-LEY-PPTO-2026-ART54-10
            Desc: Número de funcionarios a quienes se aplicó medida disciplinaria de multa
          - ID: GN-LEY-PPTO-2026-ART54-11
            Desc: Número de funcionarios a quienes se aplicó medida disciplinaria de suspensión del empleo
          - ID: GN-LEY-PPTO-2026-ART54-12
            Desc: Número de funcionarios a quienes se aplicó medida disciplinaria de destitución
          - ID: GN-LEY-PPTO-2026-ART54-13
            Desc: Número de funcionarios absueltos de cargos formulados en procedimiento disciplinario
          - ID: GN-LEY-PPTO-2026-ART54-14
            Desc: Número de funcionarios que impugnaron la resolución que aplica medida disciplinaria
          - ID: GN-LEY-PPTO-2026-ART54-15
            Desc: Número de funcionarios cuya resolución de término del procedimiento disciplinario fue enviada a
            Destinatario:
              Ref: CGR
            Ctx: Trámite de toma de razón, según corresponda
          - ID: GN-LEY-PPTO-2026-ART54-16
            Desc: Número de funcionarios cuya resolución de término del procedimiento disciplinario se encuentra ejecutoriada
          - ID: GN-LEY-PPTO-2026-ART54-17
            Desc: Toda otra información que solicite la Dirección de Presupuestos
      Informe_DIPRES_A_CEMP:
        Autoridad:
          Ref: DIPRES
        Req: Enviar a
        Destinatario:
          Ref: CEMP
        Plazo: A más tardar el 30 de enero de 2026
        Contenido: Informe consolidado sobre estado de procedimientos disciplinarios instruidos por uso indebido de licencias médicas, con la información de los numerales anteriores
      Informe_Trimestral:
        Sujetos:
          - Órganos y servicios públicos indicados en el inciso primero
          - Poder Judicial
          - Congreso Nacional
        Req: Informar trimestralmente lo indicado en los numerales anteriores, junto con descuentos aplicados a los funcionarios por uso indebido de licencias médicas
        Destinatarios:
          - Ref: DIPRES
          - Ref: CGR
          - Comisiones de Salud del Senado
          - Comisiones de Salud de la Cámara de Diputados
        Req_Adicional:
          Desc: Dar cumplimiento al deber de coordinación establecido en
          Ref: LEY18575_ART5_INC2
    Articulo_55:
      ID: GN-LEY-PPTO-2026-ART55
      Purp: Determinar sujeto responsable de deber de informar (Ley 20.285) y sanciones por incumplimiento.
      Responsable_Informacion:
        Cond: Para todos los efectos de esta ley
        Req: Obligación de informar o proporcionar antecedentes recaerá en autoridad, jefe o superior del servicio señalado conforme al artículo 16
        Ref: LEY20285
      Incumplimiento:
        Cond: En caso de incumplimiento
        Res:
          Desc: Aplicación de sanciones previstas en artículo 45
          Ref: LEY20285
    Articulo_56:
      ID: GN-LEY-PPTO-2026-ART56
      Purp: Informar reasignaciones que disminuyan presupuestos de instituciones de defensa/seguridad/justicia.
      Cond:
        Desc: Reasignaciones que signifiquen en definitiva una disminución del presupuesto de
        Sujetos:
          - Fuerzas Armadas
          - Carabineros de Chile
          - Policía de Investigaciones
          - Ministerio Público
          - Poder Judicial
      Req:
        Desc: Deberán ser informadas dentro del mes siguiente a
        Destinatarios:
          - Ref: CEMP
          - Comisiones de Defensa Nacional de ambas ramas del Congreso Nacional
          - Comisión de Seguridad Pública del Senado
          - Comisión de Seguridad Ciudadana de la Cámara de Diputados
    Articulo_57:
      ID: GN-LEY-PPTO-2026-ART57
      Purp: Promover coordinación interinstitucional formal y rendición de cuentas; reporte trimestral de convenios/colaboraciones.
      Ambito:
        Sujetos: Órganos, servicios públicos y entidades del Estado comprendidos en la presente ley
        Cond: Durante el ejercicio presupuestario
      Req_Coordinacion_Rendicion:
        Cond: Suscriban convenios, colaboraciones, transferencias, solicitudes de coordinación o instrumentos de ejecución conjunta
        Contrapartes:
          - Otros órganos de la Administración del Estado
          - Instituciones privadas
        Req: Propenderán a utilización de mecanismos formales de coordinación interinstitucional y de rendición de cuentas
        Ctx:
          - Desc: De conformidad a lo establecido en el artículo 5
            Ref: LEY18575
          - Ref: RES30_2015_CGR
      Informe_Trimestral_Convenios:
        Plazo: Dentro de los treinta días siguientes al término de cada trimestre
        Sujetos: Órganos y servicios públicos
        Req: Remitir informe consolidado
        Destinatario:
          Ref: CEMP
        Copia:
          Ref: DIPRES
        Contenido:
          - ID: GN-LEY-PPTO-2026-ART57-1
            Desc: Nómina de convenios y colaboraciones vigentes o suscritos en el período informado
          - ID: GN-LEY-PPTO-2026-ART57-2
            Desc: Entidades públicas y/o privadas participantes
          - ID: GN-LEY-PPTO-2026-ART57-3
            Desc: Montos comprometidos y ejecutados
          - ID: GN-LEY-PPTO-2026-ART57-4
            Desc: Objetivos y resultados esperados
          - ID: GN-LEY-PPTO-2026-ART57-5
            Desc: Estado de avance de ejecución material y financiero
          - ID: GN-LEY-PPTO-2026-ART57-6
            Desc: Dificultades detectadas en coordinación interinstitucional o implementación, y medidas adoptadas para superarlas
  Promulgacion:
    ID: GN-LEY-PPTO-2026-PROMULGACION-01
    Contenido: |-
      Habiéndose cumplido con lo establecido en el Nº 1 del Artículo 93 de la Constitución
      Política de la República y por cuanto he tenido a bien aprobarlo y sancionarlo; por tanto,
      promúlguese y llévese a efecto como Ley de la República.
      Santiago, 11 de diciembre de 2025.- GABRIEL BORIC FONT, Presidente de la República.-
      Nicolás Grau Veloso, Ministro de Hacienda.
      Lo que transcribo a usted para su conocimiento.- Saluda Atte. a usted, Heidi Berner
      Herrera, Subsecretaria de Hacienda.
  Tribunal_Constitucional:
    ID: GN-LEY-PPTO-2026-TC-01
    Contenido: |-
      Tribunal Constitucional
      Proyecto de ley de Presupuestos del Sector Público correspondiente al año 2026, Boletín N°
      17.870-05
      El Secretario Abogado (i) del Tribunal Constitucional, quien suscribe, certifica que la
      Honorable Cámara de Diputadas y Diputados envió el proyecto enunciado en el rubro, aprobado
      por el Congreso Nacional, a fin de que este Tribunal ejerza el control de constitucionalidad
      respecto de la totalidad del proyecto de ley; y por sentencia de 10 de diciembre de 2025, en
      el proceso Rol Nº 17.163-25-CPR.
      Se declara:
      Que no se emite pronunciamiento, en examen preventivo de constitucionalidad, respecto de
      la glosa 07, asociada a las glosas comunes a los servicios regionales de Vivienda y Urbanismo;
      del inciso primero de la glosa 04, asociada al subtítulo 24, ítem 03, asignación 003, y al subtítulo
      33, ítem 03, asignación 003, programa 02, capítulo 1; de la glosa 04, asociada al subtítulo 24,
      ítem 03, asignación 002, y al subtítulo 33, ítem 03, asignación 002, programa 04, capítulo
      01; y de la glosa 07, asociada al subtítulo 24, ítem 03, asignación 106, y al subtítulo 33, ítem
      03, asignación 106, programa 04, capítulo 01, todas de la partida 18; de la glosa 05, asociada
      al ítem 02, subtítulo 31, programa 04, capítulo 01, de la partida 19; y del inciso final de la
      glosa 14, asociada a la asignación 006, ítem 09, subtítulo 24, programa 01, capítulo 01, de
      la partida 21, todas contenidas en el Proyecto de Ley de Presupuestos para el Sector Público
      correspondiente al año 2026, boletín N° 17.870-05, aprobado por el Congreso Nacional, por
      no regular materias reservadas a la Ley Orgánica Constitucional.
      Santiago, 11 de diciembre de 2025.- Sebastián Andrés López Magnasco, Secretario
      Abogado (i), Tribunal Constitucional.
