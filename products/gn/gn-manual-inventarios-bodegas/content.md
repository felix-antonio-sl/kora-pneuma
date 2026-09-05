---
urn: urn:gn:kb:gn-manual-inventarios-bodegas
nombre: gn-manual-inventarios-bodegas
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-inventarios-bodegas; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_040_manual_inventarios_bodegas_koda.yml (sha256:067c88c96456336c80d693f5f753523111a8170b145abe458f332bede82ea17c); URN KODA legado urn:gorenuble:gn:manual-inventarios-bodegas:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-inventarios-bodegas:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml"
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

ID: KB-GN-040-MANUAL-INVENTARIOS-BODEGAS-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "GORE Ñuble"
Model-Collaborator: "CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Primary-Source: "staging/brow_speculativo/manual_2_2_inventarios.md"
Ctx: "Manual 2.2: Gestión de Inventarios y Bodegas."

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

Manual_2_2_Gestion_de_Inventarios_y_Bodegas:
  ID: GN-MANUAL-INVENTARIOS-BODEGAS-01

  Titulo:
    Def: "Manual 2.2: Gestión de Inventarios y Bodegas"

  Objetivo:
    Obj: "Controlar el flujo físico de existencias y materiales, asegurando la disponibilidad oportuna de insumos para la operación institucional y el correcto registro contable de los movimientos."

  Seccion_I_Marco_Normativo_y_Organizacion:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S01

    Fundamentos_Legales:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S01-01
      Ctx: "La gestión de inventarios se rige por:"
      Src:
        - "NICSP (Normas Internacionales de Contabilidad del Sector Público): Tratamiento contable de existencias y valorización."
        - "Resoluciones CGR: Normativa sobre control patrimonial y rendición de cuentas."
        - "Reglamento Interno de Bodegas: Documento institucional que define procedimientos operativos y responsabilidades."
        - "Ley 21.180 (Transformación Digital): Obligatoriedad del registro electrónico de movimientos."

    Estructura_Organizacional_de_Bodegas:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S01-02
      Roles:
        - Rol: "Jefe de Bodega Central"
          Def: "Responsable de la administración general del sistema de bodegas."
        - Rol: "Encargados de Bodega"
          Def: "Funcionarios designados para cada bodega, responsables de custodia y operación."
        - Rol: "Usuarios Solicitantes"
          Def: "Funcionarios autorizados para generar pedidos de consumo."
        - Rol: "Aprobadores"
          Def: "Jefaturas con atribución para autorizar despachos según monto y tipo de artículo."

    Catalogo_de_Bodegas_Institucionales:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S01-03
      Ctx: "El GORE puede operar múltiples bodegas especializadas:"
      Bodegas:
        - Bodega: "Bodega Central"
          Def: "Almacenamiento principal de insumos de consumo general."
        - Bodega: "Bodega de Economato"
          Def: "Materiales de oficina y papelería."
        - Bodega: "Bodega de Aseo"
          Def: "Productos de limpieza e higiene."
        - Bodega: "Bodega de Mantención"
          Def: "Repuestos, herramientas y materiales técnicos."
        - Bodega: "Bodega de Vestuario"
          Def: "Uniformes y elementos de seguridad personal (EPP)."
        - Bodega: "Bodegas Satélite"
          Def: "Ubicaciones descentralizadas por edificio o servicio."

  Seccion_II_Catalogo_de_Articulos:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S02

    Codificacion_y_Clasificacion:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S02-01
      Req: "Todo artículo debe estar registrado en el Catálogo Maestro antes de cualquier movimiento."
      Campos:
        - Campo: "Código Interno"
          Def: "Identificador único alfanumérico generado por el sistema."
        - Campo: "Código de Barras"
          Def: "EAN-13 o Code-128 para lectura automática."
        - Campo: "Clasificación Jerárquica"
          Items:
            - "Familia (ej. Insumos de Oficina)."
            - "Línea (ej. Papelería)."
            - "Grupo (ej. Cuadernos)."
        - Campo: "Unidad de Medida"
          Def: "Unidad base de control (unidad, caja, resma, litro, etc.)."
        - Campo: "Conversiones"
          Def: "Tabla de equivalencias (ej. 1 caja = 12 unidades)."

    Atributos_del_Articulo:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S02-02
      Campos:
        - Campo: "Cuenta Contable"
          Def: "Asociación para generación automática de asientos."
        - Campo: "Concepto de Gasto"
          Def: "Imputación presupuestaria (Subtítulo 22 generalmente)."
        - Campo: "Umbral de Capitalización"
          Def: "Bienes sobre 3 UTM se registran como Activo Fijo, no como existencias."
          Ctx_Optional: "Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md)."
        - Campo: "Control de Lote"
          Def: "Para artículos que requieren trazabilidad (medicamentos, alimentos)."
        - Campo: "Fecha de Vencimiento"
          Req: "Obligatorio para artículos perecibles."
        - Campo: "Imagen Referencial"
          Def: "Fotografía para identificación visual."
        - Campo: "Stock Mínimo/Máximo"
          Def: "Parámetros para generación de alertas de reposición."

    Proveedores_Habituales:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S02-03
      Ctx: "El sistema permite asociar proveedores frecuentes a cada artículo para facilitar:"
      Res:
        - "Consulta de precios referenciales."
        - "Generación de requerimientos de reposición."
        - "Análisis histórico de compras."

  Seccion_III_Procesos_de_Ingreso:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S03

    Recepcion_de_Productos_por_Orden_de_Compra:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S03-01
      Ctx: "Flujo estándar para ingresos desde proveedores externos."
      Pasos:
        - Paso: 1
          Act: "Aviso de Entrega"
          Def: "El proveedor coordina fecha y hora de despacho."
        - Paso: 2
          Act: "Verificación Inicial"
          Def: "Contrastar guía de despacho con Orden de Compra."
        - Paso: 3
          Act: "Inspección Física"
          Items:
            - "Contar unidades."
            - "Verificar estado y calidad."
            - "Controlar lotes y vencimientos (si aplica)."
        - Paso: 4
          Act: "Registro en Sistema"
          Def: "Ingresar cantidades recibidas, vinculando a OC."
        - Paso: 5
          Act: "Documento Tributario"
          Def: "Asociar factura electrónica o guía de despacho."
        - Paso: 6
          Act: "Ubicación"
          Def: "Asignar ubicación física dentro de la bodega."
        - Paso: 7
          Act: "Recepción Conforme"
          Def: "Firma del Encargado de Bodega que habilita el devengo."
      Ctx_Clasificacion_Bienes:
        Ctx: "Los bienes recibidos deben clasificarse por tipología. Existencias (consumibles) van a Bodega según este manual; Activos Fijos (capitalizables) van al proceso de alta."
        Ctx_Optional: "Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md)."

    Recepcion_con_Capturador_de_Datos:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S03-02
      Items:
        - "Lectura de códigos de barras del proveedor o etiquetas institucionales."
        - "Validación automática contra OC (cantidad, artículo, precio)."
        - "Generación de alertas por discrepancias."
        - "Actualización inmediata de stock."

    Otros_Tipos_de_Ingreso:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S03-03
      Tipos:
        - Tipo: "Devolución de Préstamo"
          Def: "Artículos retornados por otras bodegas o unidades."
        - Tipo: "Préstamo Recibido"
          Def: "Artículos temporales de otra institución o bodega."
        - Tipo: "Donación"
          Def: "Bienes recibidos sin costo (requiere resolución de aceptación)."
        - Tipo: "Canje"
          Def: "Intercambio de artículos con proveedores."
        - Tipo: "Ajuste por Inventario"
          Def: "Regularización de diferencias positivas detectadas."
        - Tipo: "Devolución de Consumo"
          Def: "Artículos retornados por usuarios por no uso."

  Seccion_IV_Procesos_de_Egreso:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S04

    Solicitud_de_Consumo:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S04-01
      Ctx: "Mecanismo formal para retirar artículos de bodega."
      Proc:
        - Paso: "Generación"
          Def: "Usuario solicitante crea pedido en sistema indicando artículos y cantidades."
        - Paso: "Justificación"
          Req: "Campo obligatorio que describe el uso previsto."
        - Paso: "Validación"
          Def: "El sistema verifica stock disponible antes de enviar a aprobación."
        - Paso: "Flujo de Aprobación"
          Def: "Según monto o tipo de artículo, puede requerir V°B° de jefatura."

    Despacho_de_Productos:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S04-02
      Proc:
        - Paso: "Preparación (Picking)"
          Def: "El bodeguero reúne los artículos del pedido."
        - Paso: "Verificación"
          Def: "Contrastar físico con digital antes de entregar."
        - Paso: "Documento de Despacho"
          Def: "Guía interna firmada por el receptor."
        - Paso: "Descuento de Stock"
          Def: "Actualización automática al confirmar entrega."
        - Paso: "Valorización"
          Def: "El sistema aplica método de costeo (Precio Promedio Ponderado o FIFO)."

    Despacho_con_Capturador_de_Datos:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S04-03
      Items:
        - "Lectura de códigos de barras al momento de armar el pedido."
        - "Validación automática de artículos y cantidades."
        - "Generación de documento de despacho electrónico."
        - "Firma digital del receptor (si el dispositivo lo permite)."

    Otros_Tipos_de_Egreso:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S04-04
      Tipos:
        - Tipo: "Préstamo Otorgado"
          Def: "Entrega temporal a otra unidad o institución (con compromiso de devolución)."
        - Tipo: "Merma"
          Def: "Pérdida por deterioro, vencimiento o rotura (requiere acta de baja)."
        - Tipo: "Donación"
          Def: "Entrega gratuita a terceros (requiere resolución)."
        - Tipo: "Devolución a Proveedor"
          Def: "Retorno por no conformidad o cambio."
        - Tipo: "Venta"
          Def: "Enajenación de excedentes (poco frecuente, requiere autorización especial)."

  Seccion_V_Control_de_Inventarios:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S05

    Toma_de_Inventario_Fisico:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S05-01
      Ctx: "Proceso obligatorio de verificación periódica."
      Frecuencia:
        - Tipo: "Inventario General"
          Req: "Al menos una vez al año (obligatorio al 31/12)."
        - Tipo: "Inventarios Parciales"
          Def: "Por familia, ubicación o artículos críticos (mensual o trimestral)."
      Planificacion:
        Act: "Definir alcance, fechas, equipos de conteo y corte de operaciones."
      Ejecucion:
        Items:
          - "Conteo ciego (sin ver saldos teóricos)."
          - "Segundo conteo para discrepancias."
          - "Registro en planillas o capturador de datos."
      Conciliacion:
        Act: "Comparar conteo físico vs. saldo en sistema."
      Ajustes:
        Act: "Generar movimientos de ajuste por diferencias (positivas o negativas)."

    Ajuste_de_Inventario:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S05-02
      Tipos:
        - Tipo: "Ajuste Positivo (Sobrante)"
          Def: "Cuando el físico excede al teórico."
        - Tipo: "Ajuste Negativo (Faltante)"
          Def: "Cuando el teórico excede al físico."
      Documentacion:
        Req: "Acta de inventario firmada por comisión, con explicación de causas."
      Responsabilidad:
        Warn: "Faltantes injustificados pueden derivar en sumario administrativo."
      Contabilizacion:
        Res: "Generación automática de asiento contable por ajuste."

    Control_de_Vencimientos:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S05-03
      Items:
        - "El sistema emite alertas automáticas con 90/60/30 días de anticipación."
        - "Prioridad de despacho: FEFO (First Expired, First Out)."
        - "Artículos vencidos: Retiro inmediato, acta de baja, destrucción certificada si corresponde."

    Stock_Critico_y_Reposicion:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S05-04
      Definiciones:
        - Termino: "Punto de Reorden"
          Def: "Nivel de stock que dispara la necesidad de reposición."
        - Termino: "Stock de Seguridad"
          Def: "Margen para cubrir variaciones de demanda o atrasos de proveedor."
      Proc:
        - "Alerta Automática: El sistema notifica a Abastecimiento cuando se alcanza el punto de reorden."
        - "Análisis de Consumo: Reportes históricos para ajustar parámetros de stock."

  Seccion_VI_Valorizacion_y_Cierre_Contable:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S06

    Metodos_de_Valorizacion:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S06-01
      Ctx: "El GORE debe adoptar un método consistente según NICSP:"
      Metodos:
        - Metodo: "Precio Promedio Ponderado (PPP)"
          Def: "Costo promedio recalculado con cada ingreso."
        - Metodo: "FIFO (First In, First Out)"
          Def: "Primeros ingresos se asignan a primeros egresos."
        - Metodo: "Costo Identificado"
          Def: "Para artículos de alto valor con trazabilidad individual."

    Recosteo:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S06-02
      Ctx: "Proceso para actualizar el costo de artículos ante cambios significativos."
      Cond:
        - "Aplicable cuando hay diferencias relevantes entre costo registrado y costo de reposición."
      Res:
        - "Genera comprobante contable de ajuste de valor."

    Cierre_Mensual_de_Bodega:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S06-03
      Pasos:
        - Paso: 1
          Act: "Corte de Movimientos"
          Req: "No ingresan ni egresan productos después del cierre."
        - Paso: 2
          Act: "Valorización Final"
          Def: "Cálculo del stock valorizado al último día del mes."
        - Paso: 3
          Act: "Generación de Comprobante"
          Def: "Asiento contable que registra el costo de lo consumido."
        - Paso: 4
          Act: "Cuadratura"
          Req: "Stock valorizado debe coincidir con cuenta contable de Existencias."

    Cierre_Anual:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S06-04
      Req:
        - "Inventario físico obligatorio."
        - "Ajustes de inventario procesados antes del cierre."
      Res:
        - "Emisión de informe anual de existencias para CGR."
        - "Traspaso de saldos al ejercicio siguiente."

  Seccion_VII_Reporteria_y_Auditoria:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-S07

    Reportes_Estandar:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S07-01
      Reportes:
        - "Cartola de Artículos: Detalle de movimientos por artículo en un período."
        - "Stock Valorizado: Existencias actuales con su valor monetario."
        - "Consumos por Unidad: Análisis de uso por departamento/división."
        - "Artículos sin Movimiento: Identificación de obsolescencia."
        - "Vencimientos Próximos: Listado de artículos a vencer."
        - "Diferencias de Inventario: Resumen de ajustes realizados."

    Trazabilidad_y_Auditoria:
      ID: GN-MANUAL-INVENTARIOS-BODEGAS-S07-02
      Req:
        - "Cada movimiento registra: usuario, fecha, hora, documento de respaldo."
        - "Historial de eventos inalterable (log de auditoría)."
        - "Acceso restringido por perfil (bodeguero, supervisor, auditor)."
        - "Documentos de respaldo digitalizados y vinculados a cada transacción."

  Referencias_y_Alcance:
    ID: GN-MANUAL-INVENTARIOS-BODEGAS-REF-01
    Ctx: "Este manual complementa otros manuales de abastecimiento/patrimonio, enfocándose en la gestión física de existencias (consumibles) desde la recepción hasta el consumo."
    Ctx_Optional:
      - "Manual 2.1: Compras Públicas (./manual_2_1_compras.md)."
      - "Manual 2.3: Activo Fijo (./manual_2_3_activo_fijo.md)."

Referencias_Cruzadas:
  ID: GN-MANUAL-INVENTARIOS-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml"
