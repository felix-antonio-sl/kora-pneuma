---
urn: urn:gn:kb:gn-manual-activo-fijo
nombre: gn-manual-activo-fijo
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-activo-fijo; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_041_manual_activo_fijo_koda.yml (sha256:f7b23018aa0ccdece812404ce72bcb49e7db3499c7dcacac778572c3ee70e8f8); URN KODA legado urn:gorenuble:gn:manual-activo-fijo:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-activo-fijo:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml"
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

ID: KB-GN-041-MANUAL-ACTIVO-FIJO-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "GORE Ñuble"
Model-Collaborator: "CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Primary-Source: "staging/brow_speculativo/manual_2_3_activo_fijo.md"
Authoritative-Source:
  Path: "staging/temp/brutos ordenados/04_adquisiciones_activos/RES. EXTA N°1123 APRUEBA POLÍTICA CSEU V.2 (CON PCSEU).md"
  Priority: 1
  Type: "Official-Policy"
  Last-Validated: "2025-12-18"
Source-Hierarchy:
  - Level: 1
    Description: "Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*)"
  - Level: 2
    Description: "Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*)"
  - Level: 3
    Description: "Fuentes Especulativas (staging/brow_speculativo/*)"
Ctx: "Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo."

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

Manual_2_3_Gestion_del_Ciclo_de_Vida_del_Activo_Fijo:
  ID: GN-MANUAL-ACTIVO-FIJO-01

  Titulo:
    Def: "Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo"

  Objetivo:
    Obj: "Administrar el patrimonio físico institucional, asegurando el correcto registro, valorización, control y disposición de los bienes conforme a las Normas Internacionales de Contabilidad del Sector Público (NICSP)."

  Seccion_I_Marco_Normativo_y_Clasificacion:
    ID: GN-MANUAL-ACTIVO-FIJO-S01

    Fundamentos_Legales:
      ID: GN-MANUAL-ACTIVO-FIJO-S01-01
      Ctx: "La gestión de activos fijos se rige por:"
      Src:
        - "NICSP 17: Propiedad, Planta y Equipo."
        - "NICSP 21: Deterioro del Valor de Activos No Generadores de Efectivo."
        - "NICSP 31: Activos Intangibles."
        - "Resoluciones CGR: Normativa sobre control patrimonial, bajas y remates."
        - "DL 1.263/1975: Ley de Administración Financiera del Estado."
        - "Ley 21.180: Obligatoriedad del registro electrónico del inventario."

    Clasificacion_de_Bienes:
      ID: GN-MANUAL-ACTIVO-FIJO-S01-02

      Por_Naturaleza:
        ID: GN-MANUAL-ACTIVO-FIJO-S01-02-01
        Items:
          - "Bienes Muebles: Mobiliario, equipos computacionales, maquinaria, vehículos."
          - "Bienes Inmuebles: Terrenos, edificios, instalaciones, infraestructura."
          - "Bienes Intangibles: Software, licencias, derechos, patentes."

      Por_Tratamiento_Contable:
        ID: GN-MANUAL-ACTIVO-FIJO-S01-02-02
        Items:
          - "Patrimoniales: Registrados en el balance (valor ≥ umbral de capitalización)."
          - "Inventario Administrativo: Bienes menores controlados pero no capitalizados."

      Por_Uso:
        ID: GN-MANUAL-ACTIVO-FIJO-S01-02-03
        Items:
          - "En Uso: Asignados a funcionarios o unidades."
          - "En Bodega: Disponibles para asignación."
          - "En Comodato: Cedidos temporalmente a terceros."
          - "Dados de Baja: Fuera de servicio, pendientes de disposición final."

    Umbral_de_Capitalizacion:
      ID: GN-MANUAL-ACTIVO-FIJO-S01-03
      Items:
        - 'El GORE define un umbral monetario (típicamente 3 UTM) bajo el cual los bienes se consideran "gasto" y no se capitalizan.'
        - "Bienes bajo el umbral pueden registrarse en inventario administrativo para control físico sin impacto patrimonial."

  Seccion_II_Alta_de_Bienes:
    ID: GN-MANUAL-ACTIVO-FIJO-S02

    Recepcion_y_Prealta:
      ID: GN-MANUAL-ACTIVO-FIJO-S02-01

      Origen_de_los_Bienes:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-01-01
        Items:
          - "Compra Directa (Subtítulo 29): Adquisición de Activos No Financieros (vehículos, equipos, terrenos) con presupuesto de funcionamiento."
          - "Proyectos de Inversión (Subtítulo 31): Bienes adquiridos en el marco de iniciativas de inversión propia o programas ejecutados directamente (Glosa 06/10)."
          - "Donaciones recibidas."
          - "Traspasos desde otras instituciones públicas."
          - "Construcción o fabricación propia."

      Registro_Preliminar_Prealta:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-01-02
        Ctx: "Registro Preliminar (Prealta):"
        Items:
          - "Verificación física del bien recibido."
          - "Asignación de tipología y clasificación."
          - "Registro de datos: fecha de ingreso, documento tributario, valor de adquisición."
          - "Indicación de ubicación física provisional."
          - "Asociación de responsable temporal."

    Codificacion_y_Etiquetado:
      ID: GN-MANUAL-ACTIVO-FIJO-S02-02
      Campos:
        - Campo: "Código Único de Bien"
          Def: "Identificador alfanumérico secuencial generado por el sistema."
        - Campo: "Etiqueta Física"
          Def: "Placa metálica o adhesivo con código de barras/QR."
        - Campo: "Información de Etiqueta"
          Def: "Código, descripción abreviada, año de alta."
        - Campo: "Impresión"
          Def: "El sistema permite imprimir etiquetas individuales o masivas."

    Datos_del_Alta:
      ID: GN-MANUAL-ACTIVO-FIJO-S02-03

      Datos_de_Adquisicion:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-03-01
        Items:
          - "Proveedor."
          - "Número de factura u OC."
          - "Valor de compra (incluido IVA si no recuperable)."
          - "Fecha de puesta en marcha (inicio de depreciación)."

      Datos_Tecnicos:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-03-02
        Items:
          - "Marca, modelo, número de serie."
          - "Color, dimensiones, características técnicas."
          - "Imagen fotográfica."

      Datos_de_Gestion:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-03-03
        Items:
          - "Ubicación física (edificio, piso, sala)."
          - "Responsable asignado."
          - "Centro de costo asociado."

      Documentos_Adjuntos:
        ID: GN-MANUAL-ACTIVO-FIJO-S02-03-04
        Items:
          - "Factura, garantía, manual, póliza de seguro."

    Tipos_de_Alta:
      ID: GN-MANUAL-ACTIVO-FIJO-S02-04
      Tipos:
        - Tipo: "Alta Normal"
          Def: "Bien nuevo adquirido por compra."
        - Tipo: "Alta por Donación"
          Def: "Requiere resolución de aceptación y valorización por perito si no hay documento de respaldo."
        - Tipo: "Alta por Traspaso"
          Def: "Desde otra entidad pública, con valor libro informado."
        - Tipo: "Alta por Revalorización"
          Def: "Bienes detectados en inventario sin registro previo (regularización)."
        - Tipo: "Alta Postergada"
          Def: "Permite registrar el bien sin contabilizarlo inmediatamente (útil para proyectos en curso)."

  Seccion_III_Valorizacion_y_Depreciacion:
    ID: GN-MANUAL-ACTIVO-FIJO-S03

    Valor_Inicial:
      ID: GN-MANUAL-ACTIVO-FIJO-S03-01
      Ctx: "El bien se registra a su costo de adquisición, que incluye:"
      Items:
        - "Precio de compra."
        - "Impuestos no recuperables."
        - "Costos de transporte e instalación."
        - "Costos de desmantelamiento estimados (si aplica provisión)."

    Depreciacion:
      ID: GN-MANUAL-ACTIVO-FIJO-S03-02
      Def: "Distribución sistemática del valor del bien a lo largo de su vida útil."
      Parametros:
        - Campo: "Método"
          Def: "Línea recta (más común en sector público)."
        - Campo: "Inicio"
          Def: "Mes siguiente a la fecha de puesta en marcha."
        - Campo: "Vida Útil Estimada"
          Def: "Según tablas NICSP o definición institucional."
          Items:
            - "Edificios: 50-80 años."
            - "Vehículos: 7-10 años."
            - "Equipos computacionales: 3-5 años."
            - "Mobiliario: 10-15 años."
        - Campo: "Valor Residual"
          Def: "Valor estimado al final de la vida útil (puede ser cero)."
        - Campo: "Cálculo Mensual"
          Def: "Depreciación = (Valor Inicial - Valor Residual) / Vida Útil en meses."
        - Campo: "Contabilización"
          Def: "Asiento mensual automático (Gasto Depreciación / Depreciación Acumulada)."

    Revalorizacion:
      ID: GN-MANUAL-ACTIVO-FIJO-S03-03
      Def: "Ajuste del valor contable a valor razonable."
      Parametros:
        - Campo: "Periodicidad"
          Def: "Al menos cada 5 años para bienes significativos."
        - Campo: "Método"
          Def: "Tasación por perito o índices oficiales (IPC, UF)."
        - Campo: "Efecto"
          Def: "Incremento de valor se registra en Patrimonio (Superávit por Revalorización)."
        - Campo: "Aplicación"
          Def: "Principalmente para bienes inmuebles y terrenos."

    Deterioro_Impairment:
      ID: GN-MANUAL-ACTIVO-FIJO-S03-04
      Def: "Reconocimiento de pérdida de valor cuando el valor recuperable es inferior al valor libro."
      Parametros:
        - Campo: "Indicadores"
          Items:
            - "Daño físico."
            - "Obsolescencia tecnológica."
            - "Cambio de uso."
        - Campo: "Evaluación"
          Def: "Al menos anual para bienes significativos."
        - Campo: "Registro"
          Def: "Gasto por deterioro y reducción del valor libro."
        - Campo: "Reversión"
          Def: "Posible si las circunstancias cambian (con límite del valor original depreciado)."

  Seccion_IV_Movimientos_de_Bienes:
    ID: GN-MANUAL-ACTIVO-FIJO-S04

    Traslado:
      ID: GN-MANUAL-ACTIVO-FIJO-S04-01
      Def: "Cambio de ubicación física dentro de la institución."
      Tipos:
        - "Entre edificios o pisos."
        - "Entre centros de costo."
        - "Cambio de responsable."
      Procedimiento:
        - "Solicitud del área origen."
        - "Aceptación del área destino."
        - "Actualización en sistema con nuevo responsable y ubicación."
        - "Respaldar con acta de entrega-recepción."

    Prestamo_y_Comodato:
      ID: GN-MANUAL-ACTIVO-FIJO-S04-02
      Casos:
        - Caso: "Préstamo Interno"
          Def: "Cesión temporal a otra unidad del GORE."
        - Caso: "Comodato Externo"
          Def: "Cesión gratuita a terceros (municipalidades, organizaciones)."
          Req:
            - "Requiere resolución fundada."
            - "Contrato de comodato con plazo y obligaciones."
            - 'Registro del bien como "En Comodato" sin baja patrimonial.'
            - "Seguimiento de fecha de devolución."

    Mantencion_Mayor:
      ID: GN-MANUAL-ACTIVO-FIJO-S04-03
      Def: "Erogaciones que extienden la vida útil o mejoran el rendimiento del bien."
      Criterios:
        - Tipo: "Capitalizable"
          Cond: "Si cumple criterios NICSP, se suma al valor del activo."
        - Tipo: "Gasto"
          Cond: "Si solo mantiene capacidades actuales, se registra como gasto del período."
      Ejemplos_Capitalizables:
        - "Ampliación de edificio."
        - "Overhaul de maquinaria."
      Registro:
        - "Actualización del valor y recálculo de depreciación futura."

    Descomponetizacion:
      ID: GN-MANUAL-ACTIVO-FIJO-S04-04
      Def: "Separación de un bien en sus componentes significativos para depreciación diferenciada."
      Parametros:
        - Campo: "Aplicación"
          Def: "Típico en bienes inmuebles (estructura, instalaciones, acabados)."
        - Campo: "Beneficio"
          Def: "Reflejar con mayor precisión el consumo de valor de cada componente."
        - Campo: "Registro"
          Def: "Cada componente con su propia vida útil y valor."

  Seccion_V_Baja_de_Bienes:
    ID: GN-MANUAL-ACTIVO-FIJO-S05

    Causales_de_Baja:
      ID: GN-MANUAL-ACTIVO-FIJO-S05-01
      Items:
        - "Obsolescencia: Tecnológica o funcional."
        - "Deterioro Irreparable: Daño que hace inviable la reparación."
        - "Siniestro: Robo, incendio, catástrofe."
        - "Término de Vida Útil: Bien completamente depreciado y sin utilidad."
        - "Venta o Remate: Enajenación mediante proceso público."
        - "Donación: Cesión gratuita a otra entidad."
        - "Canje: Intercambio con proveedor."

    Procedimiento_de_Baja:
      ID: GN-MANUAL-ACTIVO-FIJO-S05-02
      Pasos:
        - Paso: 1
          Act: "Informe Técnico"
          Def: "El área usuaria o mantención certifica el estado del bien."
        - Paso: 2
          Act: "Resolución de Baja"
          Def: "Acto administrativo firmado por autoridad competente."
        - Paso: 3
          Act: "Registro en Sistema"
          Def: 'Cambio de estado a "Dado de Baja", fecha y causal.'
        - Paso: 4
          Act: "Contabilización"
          Def: "Reverso del valor libro (Activo y Depreciación Acumulada) y reconocimiento de pérdida/utilidad si aplica."
        - Paso: 5
          Act: "Disposición Final"
          Items:
            - "Destrucción certificada."
            - "Entrega a beneficiario (donación)."
            - "Venta/remate."

    Remate_de_Bienes:
      ID: GN-MANUAL-ACTIVO-FIJO-S05-03
      Campos:
        - Campo: "Normativa"
          Def: "Según instrucciones CGR y reglamento interno."
        - Campo: "Publicidad"
          Def: "Aviso público con descripción, valor base y fecha de remate."
        - Campo: "Modalidad"
          Def: "Presencial o electrónica."
        - Campo: "Adjudicación"
          Def: "Al mejor postor sobre valor base."
        - Campo: "Registro"
          Def: "Baja del bien e ingreso contable por venta."

    Donacion_de_Bienes:
      ID: GN-MANUAL-ACTIVO-FIJO-S05-04
      Req:
        - "Requiere resolución fundada del Gobernador Regional."
      Ctx:
        - "Beneficiarios típicos: Municipalidades, organizaciones sin fines de lucro, otras entidades públicas."
        - "El bien se da de baja sin generar ingreso."

  Seccion_VI_Control_e_Inventario:
    ID: GN-MANUAL-ACTIVO-FIJO-S06

    Toma_de_Inventario_Fisico:
      ID: GN-MANUAL-ACTIVO-FIJO-S06-01
      Ctx: "Verificación periódica obligatoria."
      Frecuencia:
        Req: "Al menos anual (obligatorio al 31/12)."
      Alcance:
        Def: "Totalidad de bienes o por ubicación/responsable."
      Metodo:
        Items:
          - "Lectura de códigos de barras/QR con capturador."
          - "Verificación visual del estado."
          - "Registro de ubicación real."
          - "Actualización de fotografía (opcional)."
      Conciliacion:
        Act: "Comparar inventario físico vs. registro en sistema."

    Tratamiento_de_Diferencias:
      ID: GN-MANUAL-ACTIVO-FIJO-S06-02
      Casos:
        - Caso: "Sobrante"
          Def: "Bien físico sin registro. Investigar origen y regularizar con alta por revalorización."
        - Caso: "Faltante"
          Def: "Registro sin respaldo físico."
          Proc:
            - "Investigación administrativa."
            - "Si hay responsabilidad: sumario y reintegro."
            - "Si no hay responsabilidad demostrable: baja por pérdida."

    Asignacion_de_Responsables:
      ID: GN-MANUAL-ACTIVO-FIJO-S06-03
      Req:
        - "Cada bien debe tener un funcionario responsable de su custodia."
        - "El cambio de responsable se formaliza con acta de entrega-recepción."
        - "El responsable tiene obligación de informar daños, pérdidas o traslados."
        - "La desvinculación de un funcionario obliga a reasignar sus bienes."

  Seccion_VII_Cierre_y_Reporteria:
    ID: GN-MANUAL-ACTIVO-FIJO-S07

    Cierre_Mensual:
      ID: GN-MANUAL-ACTIVO-FIJO-S07-01
      Items:
        - "Ejecución de depreciación del período."
        - "Generación de comprobante contable (Depreciación/Deterioro)."
        - "Cuadratura entre módulo de Activo Fijo y Contabilidad Patrimonial."

    Cierre_Anual:
      ID: GN-MANUAL-ACTIVO-FIJO-S07-02
      Items:
        - "Inventario físico obligatorio."
        - "Ajustes de deterioro si corresponde."
        - "Informe de Activos Fijos para CGR y memorias institucionales."
        - "Traspaso de saldos al ejercicio siguiente."

    Reportes_Estandar:
      ID: GN-MANUAL-ACTIVO-FIJO-S07-03
      Reportes:
        - "Inventario Valorizado: Listado de bienes con valor libro actual."
        - "Bienes por Responsable: Asignación por funcionario."
        - "Bienes por Ubicación: Distribución geográfica/física."
        - "Cuadro de Depreciación: Valores iniciales, depreciación acumulada, valor libro."
        - "Bienes Totalmente Depreciados: Para evaluación de baja o continuidad de uso."
        - "Movimientos del Período: Altas, bajas, traslados, revalorizaciones."

  Seccion_VIII_Casos_Especiales:
    ID: GN-MANUAL-ACTIVO-FIJO-S08

    Bienes_Inmuebles:
      ID: GN-MANUAL-ACTIVO-FIJO-S08-01
      Items:
        - "Registro detallado: Rol de avalúo, superficie, inscripción CBR."
        - "Avalúo fiscal actualizado anualmente."
        - "Seguros y pólizas asociadas."
        - "Control de concesiones o arriendos si aplica."

    Vehiculos:
      ID: GN-MANUAL-ACTIVO-FIJO-S08-02
      Items:
        - "Datos específicos: Patente, año, kilometraje, revisión técnica."
        - "Integración con módulo de Flota."
        - "Seguros obligatorios (SOAP) y voluntarios."
        - "Control de mantenciones y combustible."
      Ctx_Optional: "Manual 2.4: Servicios y Flotas (./manual_2_4_servicios_flotas.md)."

    Equipamiento_TIC:
      ID: GN-MANUAL-ACTIVO-FIJO-S08-03
      Items:
        - "Registro de licencias asociadas."
        - "Control de garantías y soporte técnico."
        - "Vida útil acelerada (3-5 años)."
        - "Procedimiento de sanitización de datos antes de baja."

    Concesiones:
      ID: GN-MANUAL-ACTIVO-FIJO-S08-04
      Def: "Bienes recibidos o entregados en concesión con tratamiento NICSP específico."
      Campos:
        - Campo: "Fases"
          Items:
            - "Construcción."
            - "Explotación."
            - "Devolución."
        - Campo: "Registro"
          Def: "Según modelo NICSP 32 (Acuerdos de Concesión de Servicios)."
        - Campo: "Control"
          Def: "Seguimiento de obligaciones del concesionario."

  Alcance:
    ID: GN-MANUAL-ACTIVO-FIJO-ALCANCE-01
    Ctx: "Este manual establece el marco integral para la gestión patrimonial del GORE, desde la adquisición hasta la disposición final de los bienes."

Referencias_Cruzadas:
  ID: GN-MANUAL-ACTIVO-FIJO-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_4_servicios_flotas_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml"
