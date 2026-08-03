---
urn: urn:gn:kb:gn-manual-servicios-flotas
nombre: gn-manual-servicios-flotas
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-manual-servicios-flotas; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/gestion/manuales-operaciones/kb_gn_047_manual_flotas_koda.yml (sha256:95e81b92cd994f636a4781d76695628afecdd7776f3880b2d61f2323148b318d); URN KODA legado urn:gorenuble:gn:manual-servicios-flotas:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "KODA-TRANSFORMER"
creado: 2025-12-14
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "gestion", "manuales-operaciones", "manual"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:manual-servicios-flotas:1.0.0"
  title: "Manual 2.4: Servicios Generales y Gestión de Flotas"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_4_servicios_flotas_koda.yml"
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

ID: GN-MANUAL-SERVICIOS-FLOTAS-KODA-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: "GORE Ñuble"
Human-Editor: "FS"
Model-Collaborator: "IA-CASCADE"
AI-Remediator: "KODA-TRANSFORMER"
Creation-Date: "2025-12-14"
Modification-Date: "2025-12-16"
Source_ID: MANUAL-SERVICIOS-FLOTAS-01
Primary-Source: "staging/brow_speculativo/manual_2_4_servicios_flotas.md"
Ctx: "Operativizar servicios de soporte institucional y administrar flota vehicular del GORE."

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

Manual_2_4_Servicios_Generales_y_Gestion_de_Flotas:
  ID: GN-MANUAL-SERV-FLOTAS-CONTENT-01
  Title: "Manual 2.4: Servicios Generales y Gestión de Flotas"

  Objetivo:
    ID: GN-MANUAL-SERV-FLOTAS-OBJ-01
    Obj: "Operativizar los servicios de soporte institucional y administrar eficientemente la flota vehicular del GORE, garantizando disponibilidad, seguridad y control de costos."

  Seccion_I_Servicios_Generales:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-I-01
    Title: "Sección I: Servicios Generales"

    1_Alcance_de_Servicios_Generales:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-I-ALCANCE-01
      Def: "Servicios transversales de apoyo a la operación institucional:"
      Servicios:
        - Servicio: "Mantención de Infraestructura"
          Alcance: "Edificios, instalaciones, sistemas eléctricos, sanitarios."
        - Servicio: "Aseo y Ornato"
          Alcance: "Limpieza de oficinas, áreas comunes, jardines."
        - Servicio: "Seguridad Física"
          Alcance: "Vigilancia, control de acceso, circuito cerrado."
        - Servicio: "Cafetería y Servicios de Alimentación"
          Ctx: "Si aplica."
        - Servicio: "Correo y Mensajería"
          Alcance: "Distribución interna y externa de correspondencia."
        - Servicio: "Gestión de Estacionamientos"
          Alcance: "Asignación y control de espacios."

    2_Organizacion_del_Area:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-I-ORG-01
      Roles:
        - Rol: "Jefe de Servicios Generales"
          Def: "Responsable de la coordinación integral."
        - Rol: "Supervisores por Área"
          Areas: ["Mantención", "Aseo", "Seguridad"]
        - Rol: "Personal Operativo"
          Def: "Funcionarios propios o empresas contratadas."
        - Rol: "Coordinación con DAF"
          Purp: "Para contrataciones, pagos y control presupuestario."

    3_Contratos_de_Servicios_Externalizados:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-I-CONTRATOS-01
      Def: "La mayoría de servicios generales se ejecutan mediante contratos externos:"
      Contratos:
        - Servicio: "Aseo"
          Def: "Contrato de servicio con empresa especializada."
        - Servicio: "Seguridad"
          Def: "Contrato de vigilancia privada."
        - Servicio: "Mantención de Áreas Verdes"
          Def: "Contrato de jardinería."
        - Servicio: "Mantención de Ascensores/Equipos"
          Def: "Contratos especializados."

      Administracion_de_Contratos:
        ID: GN-MANUAL-SERV-FLOTAS-SEC-I-ADMIN-CONTRATOS-01
        Act:
          - "Designación de Administrador del Contrato."
          - "Verificación de cumplimiento de dotaciones y horarios."
          - "Libro de novedades para registro de incidencias."
          - "Evaluación periódica del servicio."
          - "Aplicación de multas según bases contractuales."

  Seccion_II_Mantencion_de_Infraestructura:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-II-01
    Title: "Sección II: Mantención de Infraestructura"

    4_Tipos_de_Mantencion:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-II-TIPOS-01
      Tipos:
        - Tipo: "Preventiva"
          Def: "Programada para evitar fallas (revisiones periódicas)."
        - Tipo: "Correctiva"
          Def: "Reparación de fallas o daños detectados."
        - Tipo: "Emergencia"
          Def: "Atención inmediata ante situaciones críticas (filtraciones, cortes eléctricos)."

    5_Plan_de_Mantencion_Preventiva:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-II-PLAN-PREV-01
      Elaboracion:
        Frecuencia: "Anual"
        Base: "Inventario de instalaciones y equipos."
      Contenido:
        - "Listado de equipos e instalaciones a mantener."
        - "Frecuencia de intervención (mensual, trimestral, anual)."
        - "Responsable de ejecución (interno o contratista)."
        - "Presupuesto estimado."
      Seguimiento:
        Def: "Calendario de actividades con alertas automáticas."

    6_Ordenes_de_Trabajo:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-II-OT-01
      Def: "Instrumento formal para solicitar y documentar intervenciones."
      Generacion:
        - "Por usuario (falla reportada)"
        - "Automática (plan preventivo)"
      Contenido:
        - "Descripción del requerimiento."
        - "Ubicación y equipo afectado."
        - "Prioridad (alta, media, baja)."
        - "Fecha de solicitud."
      Asignacion:
        - "A técnico interno"
        - "Derivación a contratista"
      Ejecucion:
        - "Registro de trabajos realizados"
        - "Materiales usados"
        - "Horas"
      Cierre:
        - "Validación por solicitante"
        - "Actualización de hoja de vida del equipo"

    7_Control_de_Elementos_de_Seguridad:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-II-SEG-01
      Elementos:
        - "Extintores: Carga, vencimiento, ubicación, señalética."
        - "Red húmeda y seca: Pruebas periódicas."
        - "Iluminación de emergencia."
        - "Señalética de evacuación."
        - "Detectores de humo y alarmas."

  Seccion_III_Gestion_de_Flota_Vehicular:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-III-01
    Title: "Sección III: Gestión de Flota Vehicular"

    Restricciones_Legales_Adquisicion:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-RESTR-LEY-01
      Req: |
        Autorización Previa de DIPRES (Art. 12 Ley Presupuestos)
        La adquisición de vehículos motorizados, a cualquier título, requiere autorización previa de la Dirección de Presupuestos (DIPRES) cuando su precio supere el monto fijado por dicha dirección. Esta restricción aplica también a vehículos adquiridos vía proyectos de inversión.

    8_Registro_de_Vehiculos:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-REG-VEH-01
      Req: "Cada vehículo institucional debe tener ficha completa:"

      Datos_de_Identificacion:
        - "Patente."
        - "Marca, modelo, año."
        - "Número de chasis y motor."
        - "Color."
        - "Tipo (sedan, camioneta, minibús, etc.)."

      Datos_Administrativos:
        - "Código de activo fijo (vinculación con Manual 2.3)."
        - "Fecha de adquisición y valor."
        - "Responsable asignado."
        - "Centro de costo."

      Documentacion_Vigente:
        - "Permiso de circulación."
        - "Revisión técnica."
        - "Seguro obligatorio (SOAP)."
        - "Seguro automotriz voluntario."

      Equipamiento:
        - "Accesorios instalados (GPS, radio, botiquín, extintor)."
        - "Kit de emergencia."

    9_Registro_de_Conductores:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-REG-CONDUCT-01
      Req: "Nómina de funcionarios autorizados para conducir vehículos institucionales."
      Requisitos:
        - "Licencia de conducir vigente (clase apropiada)."
        - "Hoja de vida sin infracciones graves."
        - "Autorización formal (resolución o memorando)."
      Actualizacion:
        Def: "Control de vencimiento de licencias con alertas."

    10_Solicitud_y_Asignacion_de_Vehiculos:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-SOL-ASIG-01
      Proc:
        - Paso: "1. Solicitud"
          Def: "Funcionario requiere vehículo indicando fecha, hora, destino, propósito."
        - Paso: "2. Aprobación"
          Def: "Jefatura del solicitante autoriza."
        - Paso: "3. Asignación"
          Def: "Encargado de Flota verifica disponibilidad y asigna vehículo + conductor."
        - Paso: "4. Confirmación"
          Def: "Notificación al solicitante y conductor."

      Criterios_de_Prioridad:
        - "Comisiones de servicio oficiales."
        - "Actividades del Gobernador y autoridades."
        - "Emergencias institucionales."
        - "Traslados programados."

      Warn: |
        Restricción de Uso (D.L. 799)
        Los vehículos estatales no pueden circular en días sábados, domingos ni festivos, salvo autorización expresa y fundada por razones de servicio impostergables.

    11_Bitacora_de_Uso:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-BITACORA-01
      Req: "Registro obligatorio de cada salida:"
      Campos:
        - "Fecha y hora de salida/retorno."
        - "Conductor."
        - "Destino y propósito."
        - "Kilometraje inicial y final."
        - "Observaciones (estado del vehículo, incidentes)."
      Modalidad:
        - "Digital: Registro en sistema o aplicación móvil."
        - "Física: Cuaderno en el vehículo (respaldo)."

    12_Control_de_Combustible:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-COMBUST-01
      Tarjeta_de_Combustible:
        Def: "Asignada a cada vehículo (ej. ServiEstado, Copec)."
      Registro_de_Cargas:
        - "Fecha y estación de servicio."
        - "Litros cargados."
        - "Monto."
        - "Kilometraje al momento de carga."
      Analisis_de_Rendimiento:
        - "Km/litro por vehículo."
        - "Comparación con estándar del fabricante."
        - "Alertas por consumos anómalos."

    13_Control_de_Kilometraje:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-III-KM-01
      Req:
        - "Registro mensual del odómetro de cada vehículo."
        - "Proyección de mantenciones según kilometraje."
        - "Detección de usos no autorizados."

  Seccion_IV_Mantencion_de_Vehiculos:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-IV-01
    Title: "Sección IV: Mantención de Vehículos"

    14_Plan_de_Mantencion_Vehicular:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-IV-PLAN-01

      Mantencion_Preventiva:
        - "Según manual del fabricante y kilometraje."
        - "Típico: Cada 5.000, 10.000, 20.000 km."
        - "Incluye: Cambio de aceite, filtros, revisión de frenos, neumáticos."

      Mantencion_Correctiva:
        - "Reparación de fallas detectadas."
        - "Prioridad según criticidad."

      Mantencion_Mayor:
        - "Overhaul de motor, transmisión."
        - "Evaluación costo/beneficio vs. reemplazo del vehículo."

    15_Ordenes_de_Trabajo_Vehicular:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-IV-OT-01
      Def: "Similar a mantención de infraestructura:"
      Proc:
        - "Generación por plan o por reporte de falla."
        - "Asignación a taller interno o externo (contratista autorizado)."
        - "Registro de trabajos, repuestos, costos."
        - "Actualización de hoja de vida del vehículo."

    16_Control_de_Documentacion:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-IV-DOC-01
      Def: "Alertas automáticas para vencimientos:"
      Table:
        Columns: [Documento, Frecuencia, Responsable]
        Rows:
          - Documento: "Permiso de Circulación"
            Frecuencia: "Anual"
            Responsable: "Encargado Flota"
          - Documento: "Revisión Técnica"
            Frecuencia: "Semestral/Anual"
            Responsable: "Encargado Flota"
          - Documento: "SOAP"
            Frecuencia: "Anual"
            Responsable: "Encargado Flota"
          - Documento: "Seguro Automotriz"
            Frecuencia: "Anual"
            Responsable: "Encargado Flota"
          - Documento: "Licencia Conductor"
            Frecuencia: "Según vencimiento"
            Responsable: "RRHH / Conductor"

    17_Siniestros_y_Accidentes:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-IV-ACC-01
      Title: "Procedimiento ante accidente:"
      Proc:
        - "1. Asegurar integridad de personas."
        - "2. Notificar a Carabineros y compañía de seguros."
        - "3. Documentar con fotografías y croquis."
        - "4. Reportar a Encargado de Flota y jefatura."
        - "5. Gestionar denuncia y reclamo al seguro."
        - "6. Evaluar responsabilidad del conductor (posible sumario)."
        - "7. Reparación o baja del vehículo según daño."

  Seccion_V_Control_y_Reporteria:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-V-01
    Title: "Sección V: Control y Reportería"

    18_Indicadores_de_Gestion_de_Flota:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-V-IND-01
      Indicadores:
        - "Disponibilidad: % de tiempo operativo vs. mantenimiento."
        - "Utilización: % de uso efectivo vs. capacidad disponible."
        - "Costo por Kilómetro: (Combustible + Mantención + Seguros) / Km recorridos."
        - "Costo por Vehículo: Gastos totales mensuales/anuales."
        - "Incidentes: Número de accidentes, multas de tránsito."

    19_Reportes_Periodicos:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-V-REP-01
      Reportes:
        - Reporte: "Informe Mensual de Flota"
          Contenido:
            - "Estado de cada vehículo."
            - "Kilometraje recorrido."
            - "Consumo de combustible."
            - "Mantenciones realizadas."
            - "Costos incurridos."
        - Reporte: "Informe de Vencimientos"
          Def: "Documentos próximos a vencer."
        - Reporte: "Ranking de Conductores"
          Def: "Por consumo, incidentes, multas."

    20_Auditoria_de_Uso:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-V-AUD-01
      Act:
        - "Verificación de coherencia entre bitácora, combustible y kilometraje."
        - "Detección de usos no autorizados o fuera de horario."
        - "Cruce con comisiones de servicio autorizadas."

  Seccion_VI_Disposiciones_Especiales:
    ID: GN-MANUAL-SERV-FLOTAS-SEC-VI-01
    Title: "Sección VI: Disposiciones Especiales"

    21_Vehiculos_en_Comodato_o_Arriendo:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-VI-COMODATO-01
      Tipos:
        - Tipo: "Comodato Recibido"
          Def: "Vehículos de otras instituciones en uso temporal."
        - Tipo: "Arriendo Operativo"
          Def: "Contratos de leasing o arriendo sin transferencia de propiedad."
      Control:
        Def: "Mismo régimen de bitácora, combustible y mantención."
      Contabilidad:
        Def: "Registro como gasto de arriendo, no como activo fijo."

    22_Baja_de_Vehiculos:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-VI-BAJA-01
      Ctx: "Procedimiento según Manual 2.3 (Activo Fijo):"
      Proc:
        - "Informe técnico de obsolescencia o siniestro."
        - "Resolución de baja."
        - "Destino: Remate, donación o destrucción."
        - "Trámites legales: Transferencia de dominio o baja registral."

    23_Responsabilidades:
      ID: GN-MANUAL-SERV-FLOTAS-SEC-VI-RESP-01
      Roles:
        - Rol: "Conductor"
          Resp:
            - "Uso correcto"
            - "Registro de bitácora"
            - "Reporte de fallas"
        - Rol: "Encargado de Flota"
          Resp: "Planificación, asignación, control documental."
        - Rol: "Jefe de Servicios Generales"
          Resp: "Supervisión integral del área."
        - Rol: "DAF"
          Resp: "Control presupuestario y de contratos."

  Nota_de_Cierre:
    ID: GN-MANUAL-SERV-FLOTAS-CIERRE-01
    Def: "Este manual establece los procedimientos para mantener la operatividad de los servicios de soporte institucional y la flota vehicular del GORE."

Referencias_Cruzadas:
  ID: GN-MANUAL-SERV-FLOTAS-XREF-01
  Ctx_Optional:
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_3_activo_fijo.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_1_compras_koda.yml"
    - "knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml"
