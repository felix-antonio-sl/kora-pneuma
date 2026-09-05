---
urn: urn:gn:kb:manual-compras
nombre: manual-compras
version: 1.0.0
estado: borrador
descripcion: "Documento GN heredado de KODA sobre manual compras; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-active/kb_gn_046_manual_compras_koda.yml (sha256:2dcbbded61f33b02dacf7b650ad1da97ce6ff8959233ca8bce881f56965b8f20); URN KODA legado urn:gorenuble:gn:manual-compras:1.0.0; estado KODA original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2025-12-14
lang: es
tags: [gn, gore-os, koda, manual, compras]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-compras:1.0.0"
  title: "Manual 2.1: Compras Públicas y Contrataciones"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/kb_gn_046_manual_compras_koda.yml"
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

ID: MANUAL-COMPRAS-CONTRATACIONES-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-12-14
Modification-Date: 2025-12-16
Primary-Source: staging/brow_speculativo/manual_2_1_compras.md
Ctx: "Manual: Compras Públicas y Contrataciones (GORE Ñuble)."
Authoritative-Source:
  Path: "staging/temp/brutos ordenados/04_adquisiciones_activos/Manual-de-Adquisiciones-GORE_Ñuble_3R.md"
  Priority: 1
  Type: "Official-Manual-DAF"
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

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Manual_2_1_Compras_Publicas_y_Contrataciones:
  ID: MANUAL-COMPRAS-CONTRATACIONES-CONTENT-01

  Obj: "Normar la adquisición de bienes y servicios garantizando transparencia, eficiencia y cumplimiento de la Ley N° 19.886 de Compras Públicas y su Reglamento."

  Seccion_I_Marco_Normativo_y_Principios_Rectores:
    ID: MANUAL-COMPRAS-SEC-I-01

    1_Fundamentos_Legales:
      ID: MANUAL-COMPRAS-SEC-I-FUND-01
      Ctx: "La gestión de compras del GORE se rige por:"
      Fuentes:
        - Src: "Ley N° 19.886 y Modificación Ley 21.634 (Compras 2.0): Moderniza la gestión de compras públicas."
        - Src: "Decreto N° 661 (2024): Nuevo Reglamento de la Ley de Compras (vigencia 12/2024)."
        - Src: "Ley de Presupuestos (Partida 31)."
        - Src: "Directivas ChileCompra."
        - Src: "Ley 21.180 (Transformación Digital)."

    Nuevos_Umbrales_y_Modalidades (Decreto 661/2024):
      ID: MANUAL-COMPRAS-SEC-I-UMBRALES-01
      Tabla_Maestra:
        - Rango: "< 3 UTM"
          Modalidad: "Fondos Globales (Caja Chica) o Portal Mercado Público."
        - Rango: "3 a 100 UTM"
          Modalidad: "Compra Ágil (Preferente). Mínimo 3 cotizaciones en el sistema."
        - Rango: "100 a 1.000 UTM"
          Modalidad: "Licitación Pública (Normas Simplificadas). Contrato opcional (puede formalizarse con OC)."
        - Rango: "> 1.000 UTM"
          Modalidad: "Licitación Pública (Normas Generales). Contrato obligatorio y Garantía de Fiel Cumplimiento."
        - Rango: "> 5.000 UTM"
          Req: "Garantía de Seriedad de la Oferta obligatoria (máximo 3% del monto)."

    2_Principios_Rectores:
      ID: MANUAL-COMPRAS-SEC-I-PRINCIPIOS-01
      Principios:
        - Principio: "Libre Concurrencia"
          Req: "Garantizar la participación de todos los proveedores que cumplan requisitos."
        - Principio: "Igualdad de Trato"
          Req: "No discriminar entre oferentes por razones ajenas al mérito técnico-económico."
        - Principio: "Transparencia"
          Req: "Publicar bases, aclaraciones, evaluaciones y adjudicaciones en www.mercadopublico.cl."
        - Principio: "Eficiencia"
          Req: "Optimizar la relación calidad-precio en las adquisiciones."
        - Principio: "Probidad"
          Req: "Evitar conflictos de interés y declarar inhabilidades."

    3_Glosario_de_Terminos:
      ID: MANUAL-COMPRAS-SEC-I-GLOSARIO-01
      Terminos:
        - ID: MANUAL-COMPRAS-GLOS-PAC
          Sigla: "PAC"
          Def: "Plan Anual de Compras."
        - ID: MANUAL-COMPRAS-GLOS-OC
          Sigla: "OC"
          Def: "Orden de Compra emitida en Mercado Público."
        - ID: MANUAL-COMPRAS-GLOS-CONVENIO-MARCO
          Termino: "Convenio Marco"
          Def: "Acuerdo suscrito por ChileCompra con proveedores para compras directas a precios predefinidos."
        - ID: MANUAL-COMPRAS-GLOS-CDP
          Sigla: "CDP"
          Def: "Certificado de Disponibilidad Presupuestaria."
        - ID: MANUAL-COMPRAS-GLOS-RECEPCION-CONFORME
          Termino: "Recepción Conforme"
          Def: "Acto formal que valida la entrega satisfactoria del bien o servicio."

  Seccion_II_Planificacion_de_Compras:
    ID: MANUAL-COMPRAS-SEC-II-01

    4_Plan_Anual_de_Compras_PAC:
      ID: MANUAL-COMPRAS-SEC-II-PAC-01
      Def: "El PAC es el instrumento de planificación que articula necesidades con presupuesto disponible."

      Elaboracion:
        Responsable: "Cada División/Departamento"
        Act: "Envía requerimientos a la Unidad de Abastecimiento"
        Plazo: "Antes del 15 de Noviembre del año anterior"

      Consolidacion:
        Responsable: "Unidad de Abastecimiento"
        Act: "Integra y prioriza las necesidades"
        Criterios_de_Priorizacion:
          - Criterio: "Criticidad operativa."
          - Criterio: "Disponibilidad presupuestaria."
          - Criterio: "Alineamiento con metas institucionales."

      Aprobacion:
        Responsable: "Administrador Regional"
        Act: "Aprueba el PAC consolidado"
        Ctx: "Mediante Resolución Exenta."

      Publicacion:
        Responsable: "Unidad de Abastecimiento"
        Act: "Publica en Mercado Público"
        Plazo: "Dentro de los primeros 30 días del año calendario"

      Modificaciones:
        Cond: "Durante el año"
        Req: "Permitidas mediante resolución fundada"
        Req_Actualizacion:
          - Req: "Actualizar la publicación en el portal."

    5_Tipos_de_Requerimientos:
      ID: MANUAL-COMPRAS-SEC-II-REQS-01
      Tipos:
        - Tipo: "Planificados (PAC)"
          Def: "Incluidos en la programación anual."
        - Tipo: "Extraordinarios"
          Def: "Necesidades imprevistas que requieren justificación escrita del área solicitante y visación DAF."
        - Tipo: "Urgentes"
          Def: "Situaciones de emergencia que permiten plazos abreviados según Reglamento (Art. 43)."

    6_Reserva_Presupuestaria_Previa:
      ID: MANUAL-COMPRAS-SEC-II-RESERVA-01
      Prohib: "Ningún proceso de compra inicia sin CDP vigente."
      Reqs:
        - Req: "El CDP debe emitirse desde el sistema financiero antes de la publicación del llamado o emisión de la OC."
        - Req: "La pre-afectación bloquea los recursos hasta la adjudicación o desistimiento."

  Seccion_III_Mecanismos_de_Compra:
    ID: MANUAL-COMPRAS-SEC-III-01

    7_Convenio_Marco_CM:
      ID: MANUAL-COMPRAS-SEC-III-CM-01
      Def: "Modalidad preferente para bienes y servicios estandarizados."

      Catalogo_ChileCompra:
        Ctx: "Se accede vía tienda electrónica en www.mercadopublico.cl."

      Proceso:
        Proc:
          - Act: "Selección de producto"
          - Act: "Emisión de OC"
          - Act: "Aceptación proveedor"
          - Act: "Despacho/Prestación"

      Ventaja:
        Res: "No requiere proceso licitatorio individual."

      Restriccion:
        Prohib: "No aplica para bienes o servicios no catalogados."

    8_Licitacion_Publica:
      ID: MANUAL-COMPRAS-SEC-III-LP-01
      Req: "Obligatoria para compras de bienes, servicios y ejecución de proyectos de inversión (Subtítulo 31) superiores a 1.000 UTM (salvo Convenio Marco)."

      Bases_Administrativas:
        Ctx: "Condiciones generales, plazos, garantías, causales de inadmisibilidad."

      Bases_Tecnicas:
        Ctx: "Especificaciones del bien o servicio, criterios de evaluación técnica."

      Publicacion:
        Plazos:
          - "Mínimo 20 días corridos para ofertar (licitación normal)."
          - "10 días (licitación abreviada por monto < 100 UTM)."

      Criterios_de_Evaluacion:
        Req: "Deben definirse en las bases con ponderaciones claras (Técnico, Económico, Plazos, etc.)."

      Comision_Evaluadora:
        Reqs:
          - Req: "Mínimo 3 integrantes designados por resolución."
          - Req: "Incluye al menos un funcionario del área técnica requirente."

      Acta_de_Evaluacion:
        Req: "Documento fundado que justifica la puntuación de cada oferente."

      Adjudicacion:
        Req: "Por Resolución Exenta del Gobernador Regional, publicada en el portal."

    9_Licitacion_Privada_y_Trato_Directo:
      ID: MANUAL-COMPRAS-SEC-III-EXCEPCIONES-01
      Def: "Modalidades excepcionales sujetas a causales legales taxativas."

      Trato_Directo_Art_8_Ley_19886:
        ID: MANUAL-COMPRAS-SEC-III-TD-01
        Causales:
          - Causal: "Proveedor único."
          - Causal: "Emergencias calificadas."
          - Causal: "Compras < 10 UTM."
          - Causal: "Contratos de prórroga por continuidad de servicio (máximo 12 meses)."

        Requisitos:
          - Req: "Resolución fundada que invoque la causal específica."
          - Req: "Publicación en Mercado Público (salvo montos menores)."
          - Req: "Visación del Jefe DAF para montos > 100 UTM."

    10_Grandes_Compras_Licitaciones_mayores_a_5000_UTM:
      ID: MANUAL-COMPRAS-SEC-III-GRANDES-01
      Reqs:
        - Req: "Requieren visación previa de la División Jurídica sobre las bases."
        - Req: "Garantía de seriedad de la oferta obligatoria (generalmente 5% del presupuesto estimado)."
        - Req: "Plazo de ofertas mínimo 30 días corridos."
        - Req: "Evaluación técnica puede incluir visitas a terreno o demostraciones."

  Seccion_IV_Ejecucion_de_Ordenes_de_Compra:
    ID: MANUAL-COMPRAS-SEC-IV-01

    11_Generacion_de_la_OC:
      ID: MANUAL-COMPRAS-SEC-IV-OC-01
      Def: "La OC es el acto administrativo que formaliza el compromiso con el proveedor."
      Reqs:
        - Req: "Se emite en Mercado Público tras la adjudicación (licitaciones) o selección (CM/Trato Directo)."

      Contenido_Obligatorio:
        - Req: "Descripción detallada del bien/servicio."
        - Req: "Cantidad y precio unitario."
        - Req: "Plazo de entrega/ejecución."
        - Req: "Lugar de entrega."
        - Req: "Imputación presupuestaria (Subtítulo/Ítem/Asignación)."

    12_Aceptacion_y_Rechazo:
      ID: MANUAL-COMPRAS-SEC-IV-ACEPTACION-01
      Plazo: "48 horas hábiles"
      Req: "El proveedor tiene 48 horas hábiles para aceptar la OC en el portal (salvo indicación distinta en bases)."
      Res: "OC rechazada o no aceptada permite re-adjudicar al siguiente oferente mejor evaluado."

    13_Recepcion_Conforme:
      ID: MANUAL-COMPRAS-SEC-IV-RECEPCION-01
      Def: "Hito crítico que habilita el devengo y posterior pago."

      Bienes:
        Proc:
          - Act: "La bodega o área solicitante verifica cantidad, calidad y concordancia con OC."
          - Act: "Genera Acta de Recepción física o digital."

      Servicios:
        Proc:
          - Responsable: "Administrador del contrato"
          - Act: "Certifica el cumplimiento mediante Informe de Conformidad."

      Integracion_Contable:
        Res: "La recepción conforme genera automáticamente el devengo presupuestario y el pasivo contable (Cuentas por Pagar)."

      Pago_Electronico_Obligatorio:
        ID: MANUAL-COMPRAS-SEC-IV-PAGO-ELECTRONICO-01
        Src: "Art. 8 de la Ley de Presupuestos"
        Req: "Todos los pagos a proveedores deben realizarse exclusivamente mediante transferencia electrónica de fondos."
        Prohib: "Pago en efectivo o cheque, salvo excepciones legalmente autorizadas."

      Nota_Recepcion_Fisica_Bienes:
        Ctx_Optional: "Para el procedimiento detallado de recepción física de bienes, consulte el Manual 2.2: Inventarios (./manual_2_2_inventarios.md) §7."

    14_Devoluciones_y_Reclamos:
      ID: MANUAL-COMPRAS-SEC-IV-DEVOLUCIONES-01
      Plazo: "8 días corridos"
      Reqs:
        - Req: "Plazo de 8 días corridos desde la recepción para reclamar la factura electrónica en el SII."
        - Req: "Devoluciones por no conformidad deben documentarse con Acta de Rechazo indicando las causales."
        - Req: "El proveedor tiene plazo según contrato/OC para subsanar o reemplazar."

  Seccion_V_Gestion_de_Contratos:
    ID: MANUAL-COMPRAS-SEC-V-01

    15_Formalizacion_de_Contratos:
      ID: MANUAL-COMPRAS-SEC-V-FORMALIZACION-01
      Req: "Obligatorio para:"
      Casos:
        - Caso: "Licitaciones > 100 UTM."
        - Caso: "Servicios de tracto sucesivo."
        - Caso: "Obras civiles."

      Contenido_del_Contrato:
        - Req: "Identificación de las partes."
        - Req: "Objeto y alcance."
        - Req: "Precio y modalidad de pago (hitos, mensualidades, etc.)."
        - Req: "Plazos de ejecución."
        - Req: "Garantías exigidas."
        - Req: "Multas y sanciones."
        - Req: "Causales de término anticipado."

    16_Administracion_del_Contrato:
      ID: MANUAL-COMPRAS-SEC-V-ADMIN-01

      Administrador_del_Contrato:
        Req: "Funcionario designado por resolución, responsable del seguimiento técnico y cumplimiento de hitos."

      Libro_de_Obra_Bitacora:
        Req: "Registro de incidencias, instrucciones y acuerdos durante la ejecución (obligatorio en contratos de obra)."

      Estados_de_Pago:
        Def: "Documentos que certifican el avance para liberar pagos parciales según hitos."

      Modificaciones:
        Reqs:
          - Req: "Aumentos o disminuciones de hasta 30% del monto original requieren resolución fundada."
          - Req: "Sobre 30% requieren nueva licitación."

    17_Garantias_Contractuales:
      ID: MANUAL-COMPRAS-SEC-V-GARANTIAS-01
      Tipos:
        - Tipo: "Seriedad de la Oferta"
          Def: "Devuelta tras adjudicación a oferentes no seleccionados."
        - Tipo: "Fiel Cumplimiento"
          Def: "Generalmente 5% del monto contratado, vigente hasta recepción final + plazo de responsabilidad."
        - Tipo: "Correcta Ejecución (Obras)"
          Def: "Puede exigirse por el plazo de responsabilidad post-recepción (típicamente 12 meses)."

      Custodia:
        Ctx: "Las garantías físicas (boletas, pólizas) se custodian en Tesorería. Las electrónicas se registran en el sistema de garantías."

    18_Multas_y_Sanciones:
      ID: MANUAL-COMPRAS-SEC-V-MULTAS-01
      Reqs:
        - Req: "Deben estar contempladas en las bases y el contrato."
        - Req: "Causales típicas: Atraso en entrega, incumplimiento parcial, calidad deficiente."

      Procedimiento:
        Proc:
          - Act: "Informe del administrador"
          - Act: "Notificación al proveedor"
          - Plazo: "Plazo de descargos (5 días hábiles)"
          - Act: "Resolución que aplica o desestima la multa."

      Cobro:
        Proc:
          - Act: "Descuento directo de estados de pago"
          - Act: "Ejecución de garantía"

    19_Termino_del_Contrato:
      ID: MANUAL-COMPRAS-SEC-V-TERMINO-01
      Tipos:
        - Tipo: "Término Natural"
          Def: "Cumplimiento del objeto en plazo."
        - Tipo: "Término Anticipado"
          Def: "Por incumplimiento grave, mutuo acuerdo, o causales de fuerza mayor."
        - Tipo: "Recepción Final"
          Def: "Acta que cierra el contrato y libera garantías (tras plazo de responsabilidad si aplica)."

  Seccion_VI_Control_Transparencia_y_Evaluacion:
    ID: MANUAL-COMPRAS-SEC-VI-01

    20_Interoperabilidad_con_Mercado_Publico:
      ID: MANUAL-COMPRAS-SEC-VI-INTEROP-01
      Reqs:
        - Req: "Toda operación debe reflejarse en www.mercadopublico.cl."
        - Req: "El sistema institucional (SIGAS o equivalente) debe sincronizar OC, estados de pago y recepciones."
        - Req: "Descarga automática de actas de adjudicación para trazabilidad."

    21_Portal_de_Proveedores:
      ID: MANUAL-COMPRAS-SEC-VI-PORTAL-01
      Def: "Herramienta de transparencia que permite a proveedores consultar:"
      Funcionalidades:
        - Funcionalidad: "Estado de sus órdenes de compra."
        - Funcionalidad: "Estado de facturas y pagos."
        - Funcionalidad: "Historial de transacciones."

    22_Evaluacion_de_Proveedores:
      ID: MANUAL-COMPRAS-SEC-VI-EVAL-01
      Frecuencia:
        - "Al cierre de cada contrato"
        - "Anualmente para contratos de tracto sucesivo"
      Criterios:
        - "Cumplimiento de plazos"
        - "Calidad del producto/servicio"
        - "Respuesta ante incidencias"
      Registro:
        Req: "La calificación se incorpora al Historial de Proveedores institucional."
      Consecuencias:
        Res: "Proveedores con evaluación deficiente pueden ser excluidos de futuras licitaciones (según bases)."

    23_Reportes_y_Auditoria:
      ID: MANUAL-COMPRAS-SEC-VI-REPORTES-01
      Reportes:
        - "Informe Mensual de Compras: Resumen de OC emitidas, montos, mecanismos utilizados."
        - "Informe de Contratos Vigentes: Estado de avance, hitos pendientes, alertas de vencimiento."
      Indicadores_de_Gestion:
        - Indicador: "% de compras vía Convenio Marco."
        - Indicador: "% de licitaciones declaradas desiertas."
        - Indicador: "Tiempo promedio de adjudicación."
        - Indicador: "Cumplimiento de plazos de pago a 30 días."

  Nota_Final:
    Ctx: "Este manual establece los lineamientos para una gestión de compras eficiente, transparente y conforme a la normativa de contratación pública."

Referencias_Cruzadas:
  ID: GN-MANUAL-COMPRAS-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml"
