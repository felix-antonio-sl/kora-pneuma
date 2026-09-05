---
urn: urn:gn:kb:gn-manual-tesoreria
nombre: gn-manual-tesoreria
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-tesoreria; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_045_manual_tesoreria_koda.yml (sha256:e4c24fbc5ae42c1d26b8d29806c8cabe4219ef8d8700962982f8760156a65dd4); URN KODA legado urn:gorenuble:gn:manual-tesoreria:1.0.0; estado original published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-tesoreria:1.0.0"
  title: "Manual 1.3: Tesorería y Gestión de Ingresos"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/kb_gn_045_manual_tesoreria_koda.yml"
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
  provenance:
    created_by: "KODA-TRANSFORMER"
    created_at: "2025-12-18"
    last_modified_at: "2025-12-18"

ID: GN-MANUAL-TESORERIA-01
Version: 1.0.0
Status: published
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-18"
Primary-Source: "staging/brow_speculativo/manual_1_3_tesoreria.md"
Ctx: "Control de flujo de caja, ejecución de pagos y recaudación de ingresos del GORE Ñuble."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    Parse with absolute fidelity. Preserve meat (essential info) and skeleton (structure) with zero loss.
    LEXICON: Act->Action, Ctx->Context, Def->Definition, Obj->Objective, Proc->Process, Req->Requirement, Res->Result, Src->Source, Warn->Warning, Prohib->Prohibition.
    END_LLM_INSTRUCTIONS

Definitions:
  - ID: DEF-TESORERO
    Def: "Funcionario responsable de la custodia de fondos, valores y administración de cuentas corrientes."
  - ID: DEF-PAC
    Def: "Programación Anual de Caja; herramienta de proyección de liquidez."
  - ID: DEF-CUF
    Def: "Cuenta Única Fiscal del Banco Estado."
  - ID: DEF-TEF
    Def: "Transferencia Electrónica de Fondos."

Manual_1_3_Tesoreria_y_Gestión_de_Ingresos:
  ID: GN-MANUAL-TESORERIA-ROOT-01
  Obj: "Controlar el flujo de caja, la ejecución de pagos y la recaudación de ingresos, asegurando la disponibilidad financiera y el resguardo de los recursos regionales."

  Seccion_I_Organizacion_y_Normas:
    ID: GN-MANUAL-TESORERIA-S1-01

    1_Rol_del_Tesorero_Regional:
      ID: GN-MANUAL-TESORERIA-S1-ROL-01
      Ref: DEF-TESORERO
      Funciones:
        - Act: "Custodia de Fondos: Administración de cuentas corrientes."
        - Act: "Custodia de Valores: Resguardo de boletas de garantía, pólizas, vales vista."
        - Act: "Firma Conjunta: Autorización de pagos junto a Jefe DAF o Jefe Finanzas."

    2_Seguridad_de_Valores:
      ID: GN-MANUAL-TESORERIA-S1-SEG-01
      Reqs:
        - Act: "Arqueo de Caja sorpresivo (realizado por Finanzas o Auditoría)."
        - Req: "Uso de Caja Fuerte ignífuga con acceso restringido."
        - Req: "Póliza de Fidelidad Funcionaria para personal con manejo de fondos."

    3_Marco_Normativo:
      ID: GN-MANUAL-TESORERIA-S1-NORMA-01
      Fuentes:
        - Src: "DL 1.263 (1975): Arts. 11, 12 (Anualidad) y 30 (CUF)."
        - Src: "Ley 21.180 (Transformación Digital): Expediente electrónico obligatorio."
        - Src: "Ley de Presupuestos (Partida 31): Glosas FNDR."

  Seccion_II_Gestion_Bancaria_y_Programacion:
    ID: GN-MANUAL-TESORERIA-S2-01

    4_Administracion_de_Cuentas_CUF:
      ID: GN-MANUAL-TESORERIA-S2-CUF-01
      Ref: DEF-CUF
      Tipos_Cuenta:
        - "FNDR (Inversión)"
        - "Funcionamiento (Gasto Administrativo)"
        - "Fondos de Terceros (Custodia)"
      Req: "Cierre/Apertura requiere Resolución + Autorización Hacienda."

    5_Programacion_de_Caja_PAC:
      ID: GN-MANUAL-TESORERIA-S2-PAC-01
      Ref: DEF-PAC
      Proc:
        - Act: "Informa semanalmente disponibilidad real a DIPIR/DAF."
        - Act: "Solicita remesas a DIPRES vía SIGFE según devengo exigible."
      Warn: "Saldos no ejecutados al 31/12 deben reintegrarse a Rentas Generales (salvo SIC autorizado)."

  Seccion_III_Proceso_de_Egresos_Pagos:
    ID: GN-MANUAL-TESORERIA-S3-01

    6_Ciclo_de_Pago_a_Proveedores:
      ID: GN-MANUAL-TESORERIA-S3-PROV-01
      Cond: "Solo tras validación del Devengo."
      Reqs:
        - Req: "Recepción Conforme."
        - Req: "Factura aceptada (8 días)."
        - Req: "OC y Resolución vigente."
        - Req: "Imputación presupuestaria registrada."
      Escala_de_Aprobaciones:
        - Rango: "< 100 UTM"
          Resp: "Jefe Finanzas + Tesorero"
        - Rango: "100 - 1.000 UTM"
          Resp: "Jefe DAF + Jefe Finanzas"
        - Rango: "> 1.000 UTM"
          Resp: "Requiere V°B° Administrador Regional"

    7_Medios_de_Pago:
      ID: GN-MANUAL-TESORERIA-S3-MEDIOS-01
      Ref: DEF-TEF
      Preferente: "Transferencia Electrónica (TEF Masiva) con doble apoderado."
      Excepcion: "Cheques nominativos y cruzados (finiquitos, devoluciones menores)."

    8_Remuneraciones_y_Cotizaciones:
      ID: GN-MANUAL-TESORERIA-S3-REM-01
      Reqs:
        - Req: "Confidencialidad: nómina encriptada."
        - Req: "Pago de Cotizaciones vía PREVIRED antes del día 10."

  Seccion_IV_Gestion_de_Ingresos_y_Garantias:
    ID: GN-MANUAL-TESORERIA-S4-01

    9_Percepcion_de_Ingresos:
      ID: GN-MANUAL-TESORERIA-S4-ING-01
      Tipos:
        - "Transferencias DIPRES/SUBDERE."
        - "Ingresos Propios (Venta bases, activos)."
        - "Recuperaciones (Licencias médicas SIL, viáticos)."
        - "Multas a proveedores (descuento o pago directo)."

    10_Control_de_Garantias:
      ID: GN-MANUAL-TESORERIA-S4-GAR-01
      Proc:
        - Act: "Recepción de documento físico o certificado digital."
        - Act: "Registro detallado (Vencimiento, Monto, Aseguradora)."
        - Act: "Alerta de Vencimiento (30 y 15 días de anticipación a Unidad Técnica)."
        - Act: "Cobro inmediato ante resolución de incumplimiento."
      Req: "Devolución exige Acta de Recepción Conforme Final."

  Seccion_V_Control_Diario:
    ID: GN-MANUAL-TESORERIA-S5-01
    Act: "Cuadratura de Caja diaria (Ingresos vs Egresos)."
    Prohib: "Pasar diferencias al día siguiente sin aclarar."
    Reporte: "Informe Diario de Disponibilidades y Deuda Flotante Diaria."

Referencias_Cruzadas:
  ID: GN-MANUAL-TESORERIA-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml"
