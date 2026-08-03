---
urn: urn:gn:kb:manual-presupuesto
nombre: manual-presupuesto
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre manual presupuesto; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_043_manual_presupuesto_koda.yml (sha256:68158a98458b593670d74ab9534a87a5a1748de44f22818a3e34a39c475f9b43); URN KODA legado urn:gorenuble:gn:manual-presupuesto:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2025-12-14
lang: es
tags: [gn, gore-os, koda, manual, presupuesto]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-presupuesto:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/kb_gn_043_manual_presupuesto_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2025-12-16"
    last_modified_at: "2025-12-16"
    signature: null

ID: GN-MANUAL-PPTO-FORM-EJEC-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "GORE Ñuble"
Model-Collaborator: "CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Ctx: "Estandarizar ciclo de vida de recursos financieros regionales: planificación -> formulación -> aprobación -> ejecución -> control -> cierre; cumplimiento Ley de Presupuestos y SAF del Estado."
Primary-Source: "staging/brow_speculativo/manual_1_1_presupuesto.md"
Authoritative-Source:
  Path: "staging/temp/brutos ordenados/02_finanzas_control/OF CIRCULAR 11 (038FF)_30.01_INSTRUCCIONES APLICACIÓN GLOSAS GORES.koda.yml"
  Priority: 1
  Type: "Official-Circular-DIPRES"
  Last-Validated: "2025-12-18"
Source-Hierarchy:
  - Level: 1
    Description: "Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*)"
  - Level: 2
    Description: "Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*)"
  - Level: 3
    Description: "Fuentes Especulativas (staging/brow_speculativo/*)"

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

Definitions:
  Organos_y_Unidades:
    - ID: DEF-DIPRES
      Def: "DIPRES (Dirección de Presupuestos): Ente rector que define instrucciones, techos y autoriza modificaciones mayores."
    - ID: DEF-GOBERNADOR-REGIONAL
      Def: "Gobernador Regional: Responsable de proponer el presupuesto al CORE y ejecutarlo."
    - ID: DEF-CORE
      Def: "Consejo Regional (CORE): Aprueba presupuesto inicial y modificaciones mayores; fiscaliza la ejecución."
    - ID: DEF-DIPIR
      Def: "División de Presupuesto e Inversión Regional (DIPIR): Unidad técnica responsable de gestión diaria del presupuesto, control de saldos y visación de gastos."
  Sistemas_y_Codigos:
    - ID: DEF-SIGFE
      Def: "SIGFE: Sistema central (módulo formulación y registro ejecución) para gestión financiera del Estado."
    - ID: DEF-BIP
      Def: "BIP: Banco Integrado de Proyectos; código requerido para proyectos de inversión."
    - ID: DEF-IDI
      Def: "IDI: Iniciativa (proyecto) de inversión; se controla por código (BIP) y no se mezclan fondos entre proyectos."
  Instrumentos_y_Fondos:
    - ID: DEF-FNDR
      Def: "FNDR: Principal fuente de recursos para inversiones; se subdivide en asignaciones regionales (decisión GORE) y provisiones (decisión central/mixta)."
    - ID: DEF-FRPD
      Def: "FRPD: Recursos destinados a fomento productivo, ciencia e innovación."
    - ID: DEF-PAC
      Def: "PAC (Programación Anual de Caja): Proyecta flujo de ingresos y egresos para asegurar liquidez para cumplir obligaciones."
  Cadena_Presupuestaria:
    - ID: DEF-CDP
      Def: "CDP (Certificado de Disponibilidad Presupuestaria): Documento previo obligatorio que certifica saldo; ningún proceso de compra o convenio inicia sin CDP."
    - ID: DEF-COMPROMISO
      Def: "Compromiso: Acto administrativo (OC/Contrato/Resolución Convenio) que afecta el presupuesto; reserva recursos definitivamente para un tercero."
    - ID: DEF-DEVENGO
      Def: "Devengo: Hito de recepción conforme; genera obligación de pago y pasivo contable; debe ser simultáneo a recepción de factura/bien."
    - ID: DEF-PAGO
      Def: "Pago: Egreso efectivo de fondos que extingue la obligación."
  Cierre:
    - ID: DEF-SIC
      Def: "SIC: Saldo Inicial de Caja."
    - ID: DEF-DEUDA-FLOTANTE
      Def: "Deuda Flotante: Obligaciones devengadas al 31/12 pendientes de pago."
    - ID: DEF-ITEM-DEUDA-FLOTANTE
      Def: "Ítem 34.07 'Deuda Flotante': se crea en presupuesto del año siguiente para registrar financiamiento."

Manual_1_1_Formulacion_y_Ejecucion_Presupuestaria:
  ID: GN-MANUAL-PPTO-ROOT-01
  Obj:
    - "Estandarizar ciclo de vida de recursos financieros regionales."
    - "Asegurar cumplimiento Ley de Presupuestos del Sector Público y normativa SAF del Estado."

  Seccion_I_Marco_Conceptual_y_Estructura:
    ID: GN-MANUAL-PPTO-S1-01

    Clasificador_Presupuestario:
      ID: GN-MANUAL-PPTO-S1-CLASIF-01
      Src: "Decreto N° 854 (2004) de Hacienda."
      Ctx: "Estructura presupuestaria GORE Ñuble."
      Estructura:
        Partida:
          - Partida: "31"
            Def: "Identifica a los Gobiernos Regionales."
        Capitulos:
          - Capitulo: "01 Gobierno Regional"
            Def: "Ejecución administrativa y operativa."
          - Capitulo: "02 Consejo Regional"
            Def: "Gastos funcionamiento CORE (dietas, viáticos, asesorías)."
        Programas:
          - Programa: "01 Funcionamiento"
            Def: "Gastos administrativos (Personal; Bienes y Servicios)."
          - Programa: "02 Inversión Regional"
            Def: "Ejecución FNDR y otros fondos de capital."
        Subtitulos_Relevantes:
          - "21 Gastos en Personal."
          - "22 Bienes y Servicios de Consumo."
          - "24 Transferencias Corrientes."
          - "29 Adquisición de Activos No Financieros."
          - "31 Iniciativas de Inversión."
          - "33 Transferencias de Capital."

    Fuentes_de_Financiamiento:
      ID: GN-MANUAL-PPTO-S1-FUENTES-01
      Fuentes:
        - Ref: DEF-FNDR
        - Ref: DEF-FRPD
        - Fuente: "Ingresos Propios"
          Def: "Recursos generados por venta de bienes, multas o servicios."
        - Ref: DEF-PAC

    Roles_Presupuestarios:
      ID: GN-MANUAL-PPTO-S1-ROLES-01
      Roles:
        - Ref: DEF-DIPRES
        - Ref: DEF-GOBERNADOR-REGIONAL
        - Ref: DEF-CORE
        - Ref: DEF-DIPIR

  Seccion_II_Ciclo_de_Formulacion_Presupuestaria:
    ID: GN-MANUAL-PPTO-S2-01

    Fase_Exploratoria_Marco_Presupuestario:
      ID: GN-MANUAL-PPTO-S2-F4-01
      Calendario: "Mayo-Junio del año anterior."
      Actividad: "DIPRES comunica 'Marco Exploratorio' (techo global estimado)."
      Analisis_Interno:
        - Resp: "DIPIR"
          Act: "Proyectar 'Arrastres' (compromisos de años anteriores a pagar en año t+1)."
        - Resp: "DIPIR"
          Res: "Determinar 'Espacio Presupuestario' para nuevas iniciativas."
      Ref:
        - DEF-DIPRES
        - DEF-DIPIR

    Formulacion_del_Proyecto_de_Presupuesto:
      ID: GN-MANUAL-PPTO-S2-F5-01
      Programa_01_Funcionamiento:
        ID: GN-MANUAL-PPTO-S2-F5-P01-01
        Proc:
          - "Formular en base a dotación efectiva (remuneraciones)."
          - "Formular en base a contratos de servicios vigentes (luz, agua, seguridad, aseo)."
      Programa_02_Inversion:
        ID: GN-MANUAL-PPTO-S2-F5-P02-01
        Prioridades:
          - Prioridad: "1. Continuidad (Arrastre)."
            Req: "Asegurar financiamiento de obras en ejecución."
          - Prioridad: "2. Nuevas Iniciativas."
            Req:
              - "Seleccionar proyectos con recomendación técnica favorable (RS)."
              - "Alinear con Estrategia Regional de Desarrollo (ERD)."
      Ingreso_SIGFE:
        ID: GN-MANUAL-PPTO-S2-F5-SIGFE-01
        Act: "Cargar formulación en módulo de formulación del sistema central."
        Ref: DEF-SIGFE

    Discusion_y_Aprobacion:
      ID: GN-MANUAL-PPTO-S2-F6-01
      Proc:
        - Etapa: "1. Interna"
          Act: "DIPIR presenta propuesta consolidada a Gobernador y Administrador Regional."
        - Etapa: "2. CORE"
          Act: "Gobernador presenta proyecto al CORE (comisión y aprobación en pleno)."
        - Etapa: "3. DIPRES/Congreso"
          Proc: "Discusión técnica con analistas DIPRES; trámite legislativo (Septiembre-Noviembre)."
        - Etapa: "4. Promulgación"
          Res: "Publicación Ley de Presupuestos (Diciembre)."
      Ref:
        - DEF-DIPIR
        - DEF-GOBERNADOR-REGIONAL
        - DEF-CORE
        - DEF-DIPRES

  Seccion_III_Ejecucion_y_Control_Presupuestario:
    ID: GN-MANUAL-PPTO-S3-01

    Distribucion_Inicial:
      ID: GN-MANUAL-PPTO-S3-F7-01
      Proc:
        - "Promulgada la Ley: emitir Decreto de Identificación Presupuestaria."
        - "Desagregar montos globales en asignaciones específicas e Iniciativas de Inversión (códigos BIP)."
      Ref: DEF-BIP

    Niveles_de_Ejecucion_y_Grados_de_Afectacion:
      ID: GN-MANUAL-PPTO-S3-F8-01
      Req: "Todo gasto debe seguir estrictamente la cadena de afectación en SIGFE para asegurar trazabilidad y control financiero."
      Cadena_Estandar:
        - Etapa: "0. Pre-afectación"
          Def: "Reserva preventiva de recursos al iniciar un proceso de compra o solicitud de gasto (interno)."
        - Etapa: "1. CDP"
          Ref: DEF-CDP
          Act: "Emisión del certificado que bloquea el saldo presupuestario."
        - Etapa: "2. Compromiso"
          Ref: DEF-COMPROMISO
          Act: "Registro del acto administrativo (OC, Contrato, Resolución) que formaliza la obligación con un tercero."
        - Etapa: "3. Devengo"
          Ref: DEF-DEVENGO
          Act: "Reconocimiento de la obligación exigible tras recepción conforme o cumplimiento de hito."
        - Etapa: "4. Pago"
          Ref: DEF-PAGO
          Act: "Extinción de la obligación mediante transferencia electrónica."

    Reglas_Especificas_de_Devengo_para_Transferencias:
      ID: GN-MANUAL-PPTO-S3-F8-REGLAS-01
      Src: "Minuta CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024."
      Casos:
        - Caso: "Transferencias Extrapresupuestarias (Subt. 24.03, 33.03) a Instituciones Ley Ppto"
          Regla: "El devengo ocurre al aprobarse técnicamente la rendición de cuentas, no al momento de la transferencia."
        - Caso: "Transferencias a Municipios y Otros Servicios (Consolidables)"
          Regla: "El devengo ocurre cuando la obligación es exigible según el acto administrativo o convenio tramitado."
        - Caso: "Transferencias a Entidades Privadas (Subt. 24.01, 33.01)"
          Regla: "El devengo ocurre al cumplirse las condiciones de exigibilidad pactadas en el convenio formal."
      Ref: DEF-SIGFE

    Modificaciones_Presupuestarias:
      ID: GN-MANUAL-PPTO-S3-F9-01
      Niveles:
        - Nivel: "1"
          Nombre: "Resolución GORE"
          Alcance: "Reasignaciones entre ítems del mismo subtítulo (con restricciones)."
          Aprobacion: "Gobernador."
        - Nivel: "2"
          Nombre: "Resolución GORE con Toma de Razón"
          Alcance: "Reasignaciones entre subtítulos de misma naturaleza."
        - Nivel: "3"
          Nombre: "Decreto de Hacienda"
          Alcance:
            - "Suplementos de fondos."
            - "Transferencias entre programas."
            - "Creación de asignaciones."
          Req: "Trámite en DIPRES."
      Excepciones_Sin_Acuerdo_CORE_Glosa_01:
        ID: GN-MANUAL-PPTO-S3-F9-EXCEP-01
        Ctx: "Modificaciones que el Gobernador puede autorizar vía Resolución sin acuerdo CORE (Glosa 01, Circular 11)."
        Casos:
          - "Incorporación de Mayores Ingresos Propios percibidos."
          - "Distribución de Saldos Iniciales de Caja (SIC) para Deuda Flotante."
          - "Reasignaciones por aplicación de leyes de Reajuste."
          - "Cumplimiento de sentencias ejecutoriadas."
          - "Desagregación de recursos para Transferencias Consolidadas."
          - "Distribución de Provisiones de la Partida Tesoro Público."
      Rol_CORE:
        ID: GN-MANUAL-PPTO-S3-F9-CORE-01
        Src: "Ley 19.175."
        Req: "CORE debe aprobar modificaciones que impliquen cambios en distribución de inversión o creación de nuevos programas."
        Ref: DEF-CORE
      Ref: DEF-DIPRES

  Seccion_IV_Gestion_de_la_Inversion_Regional_FNDR:
    ID: GN-MANUAL-PPTO-S4-01
    Ref: DEF-FNDR

    Identificacion_de_Iniciativas_IDI:
      ID: GN-MANUAL-PPTO-S4-F10-01
      Req: "Cada proyecto de inversión debe tener código BIP."
      Apertura_IDI:
        ID: GN-MANUAL-PPTO-S4-F10-APERTURA-01
        Resp: "DIPIR"
        Act: "Crear 'ficha IDI' en sistema presupuestario; cargar presupuesto anual y total."
        Ref:
          - DEF-DIPIR
          - DEF-IDI
      Control_por_Codigo:
        ID: GN-MANUAL-PPTO-S4-F10-CONTROL-01
        Req: "Ejecución se controla a nivel de IDI; no usar fondos de proyecto A para pagar proyecto B."
        Ref: DEF-IDI

    Gestion_de_Convenios_de_Transferencia:
      ID: GN-MANUAL-PPTO-S4-F11-01
      Def: "Mecanismo principal para ejecutar proyectos donde GORE no es unidad técnica."
      Tipos:
        - Tipo: "Convenio Mandato"
          Def: "GORE encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos contra avance (Estados de Pago)."
        - Tipo: "Convenio de Transferencia"
          Def: "Entrega recursos para ejecución directa del beneficiario (subvenciones, fondos concursables)."
          Req: "Rendición estricta (SISREC/Contraloría)."
      Ctx:
        - "Unidades técnicas posibles: MOP, SERVIU, Municipalidad."
        - "Estados de Pago: transferencia contra avance."

    Programas_Directos_Glosa_06:
      ID: GN-MANUAL-PPTO-S4-F12-01
      Def: "Oferta programática ejecutada directamente por el GORE."
      Evaluacion_Ex_Ante:
        ID: GN-MANUAL-PPTO-S4-F12-EXANTE-01
        Req: "Programas nuevos o sustancialmente reformulados requieren evaluación favorable DIPRES/MDSF antes de financiamiento."
        Ref: DEF-DIPRES
      Metodologia_Marco_Logico:
        ID: GN-MANUAL-PPTO-S4-F12-ML-01
        Req: "Diseñar programas con objetivos, componentes, actividades e indicadores verificables."
      Gasto_Administrativo:
        ID: GN-MANUAL-PPTO-S4-F12-GA-01
        Req: "Hasta 5% del monto del programa para gastos de administración del GORE (Subtítulos 21, 22, 29)."
      Exencion:
        ID: GN-MANUAL-PPTO-S4-F12-EXENCION-01
        Req: "Exentos de evaluación ex-ante: programas 8% FNDR (Glosa 07) y tipologías FRPD de Innovación."
        Ref:
          - DEF-FNDR
          - DEF-FRPD

    Restricciones_Glosas_2025:
      ID: GN-MANUAL-PPTO-S4-GLOSAS-01
      Src: "Circular 11 DIPRES - Instrucciones Glosas GORES."
      Normas:
        - Glosa: "03 (Gastos en Personal)"
          Prohib: "No se puede imputar a inversión (Subtítulo 31) gastos en personal (Subtítulo 21), salvo contratación de inspección técnica de obras."
        - Glosa: "06 (Programas GORE)"
          Req: "Ejecución directa requiere unidad técnica interna competente y resolución fundada."
        - Glosa: "07 (Subvenciones 8%)"
          Req: "Máximo 8% del presupuesto inversional. Asignación directa solo a entidades públicas o privadas sin fines de lucro, con justificación fundada."
        - Glosa: "12 (FRIL)"
          Req: "Proyectos menores a 5.000 UTM exentos de evaluación MDSyF (solo requieren elegibilidad técnica regional)."

    Programacion_Financiera:
      ID: GN-MANUAL-PPTO-S4-F13-01
      Coordinacion: "DIPIR-Tesorería."
      PAC_de_Inversiones:
        ID: GN-MANUAL-PPTO-S4-F13-PACINV-01
        Def: "PAC vinculada a avance físico de obras."
        Ref: DEF-PAC
      Devengamiento_Oportuno:
        ID: GN-MANUAL-PPTO-S4-F13-DEVOP-01
        Req:
          - "Evitar devengamiento masivo en diciembre."
          - "Procesar estados de pago mensualmente para reflejar ejecución real."
      Ctx_Optional: "Para detalle operativo PAC y gestión de caja: Manual 1.3: Tesorería y Gestión de Ingresos (./manual_1_3_tesoreria.md)."

  Seccion_V_Informes_y_Evaluacion:
    ID: GN-MANUAL-PPTO-S5-01

    Reporteria_Oficial:
      ID: GN-MANUAL-PPTO-S5-F14-01
      Informe_de_Ejecucion_Mensual:
        ID: GN-MANUAL-PPTO-S5-F14-MENSUAL-01
        Proc:
          - "Enviar a DIPRES y CORE dentro de primeros días del mes siguiente."
          - "Mostrar presupuesto vigente vs devengado."
        Ref:
          - DEF-DIPRES
          - DEF-CORE
      Informes_Trimestrales_Glosas:
        ID: GN-MANUAL-PPTO-S5-F14-TRIM-01
        Def: "Reportes exigidos por Ley de Presupuestos (ej.: gastos en publicidad, viáticos, convenios directos)."
        Proc:
          - "Enviar al Congreso."
          - "Publicar en transparencia activa."

    Cierre_Presupuestario:
      ID: GN-MANUAL-PPTO-S5-F15-01
      Regla_31_Diciembre:
        ID: GN-MANUAL-PPTO-S5-F15-REG31-01
        Req:
          - "Presupuesto expira al 31/12."
          - "Saldos no comprometidos no se acumulan para el año siguiente (salvo norma expresa de saldo inicial de caja)."
      Deuda_Flotante:
        ID: GN-MANUAL-PPTO-S5-F15-DF-01
        Ref: DEF-DEUDA-FLOTANTE
        Financiamiento:
          - Cond: "SIC suficiente"
            Res: "Financiar íntegramente con SIC (solo Resolución GORE)."
          - Cond: "SIC insuficiente"
            Res: "Usar todo SIC disponible + diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES)."
        Prioridad:
          ID: GN-MANUAL-PPTO-S5-F15-DF-PRIOR-01
          Req: "Pago Deuda Flotante es primera prioridad al inicio del nuevo ejercicio."
        Registro:
          ID: GN-MANUAL-PPTO-S5-F15-DF-REG-01
          Act: "Crear Ítem 34.07 'Deuda Flotante' en presupuesto del año siguiente."
          Ref: DEF-ITEM-DEUDA-FLOTANTE
      Ref: DEF-SIC

  Ctx_Related_Knowledge:
    ID: GN-MANUAL-PPTO-XREF-01
    XRef:
      - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0"
      - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0"
      - "urn:gorenuble:gn:gestion-prpto:1.0.0"
    Ctx_Optional:
      - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
      - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml"
      - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml"
      - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"

Just: "Manual orientado a disciplina fiscal y cumplimiento de metas de ejecución del Gobierno Regional."
