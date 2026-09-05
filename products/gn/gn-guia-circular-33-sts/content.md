---
urn: urn:gn:kb:gn-guia-circular-33-sts
nombre: gn-guia-circular-33-sts
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Guía Operativa para Formulación y Evaluación de Iniciativas Circular 33 (GORE Ñuble); migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_029_guia_circ33_koda.yml (sha256:f899708196b4b89eec1439d71bc5bdd1debdbdb96567b17270e389220fa4c700); URN KODA legado urn:gorenuble:gn:guia-circular-33-sts:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "guia"]
familia: bok
---
# Artefacto KODA/Spec – Guía Operativa para Formulación y Evaluación de Iniciativas Circular 33 (GORE Ñuble)
# Fuente principal: kb_gn_029_guia_circ33_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:guia-circular-33-sts:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_029_guia_circ33_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"

provenance:
  created_by: "FS"
  created_at: "2025-11-28"
  last_modified_at: "2025-11-28"
  signature: null

ID: GN-GUIA-CIRC33-STS-2025-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Guía operativa del Gobierno Regional de Ñuble para la formulación, evaluación,
  reevaluación y ejecución de iniciativas financiadas bajo el Oficio Circular 33,
  con foco en requisitos documentales, categorización de iniciativas, procesos
  de admisibilidad, evaluación técnica (RATE) y reglas de conservación, ANF y
  emergencias.

Source:
  Primary-Source: "kb_gn_029_guia_circ33_sts.md"
  Ctx_Required:
    - "Oficio Circular N°33 del Ministerio de Hacienda (2009)."
    - "Ley N°21.796 de Presupuestos del Sector Público 2026 (Partida 31, Programa 02)."
    - "Normas de Inversión Pública (NIP) y metodologías SNI complementarias."
    - "Resolución Exenta que aprueba la Guía Operativa Circular 33 del GORE Ñuble."
  Ctx_Optional:
    - "Estrategia Regional de Desarrollo Ñuble 2022-2030."
    - "Metodología General de evaluación de proyectos sociales SNI."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-GUIA-CIRC33-STS-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure:
    headers, IDs, lists, tables) with zero loss. Ignore fat (filler words,
    retórica, redundancias).

    LEXICON (expand before processing):
      Act->Action, Cause->Cause, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
      Just->Justification, Mech->Mechanism, Mdl->Model,
      Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
      Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
      Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY:
      - Ref: is internal only—must point to an existing ID defined within
        THIS document.
      - External documents (leyes, oficios, glosas, metodologías, sitios web)
        se mencionan bajo Ctx:, Src:, Ctx_Required: o Ctx_Optional:, nunca bajo Ref:.

    LANGUAGE POLICY:
      - Keywords in English (and abbreviated forms as listed).
      - Content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Guia_Circular_33_GORE_Nuble:
  ID: GN-GUIA-CIRC33-STS-2025-01
  Titulo: "Guía Operativa para la Formulación y Evaluación de Iniciativas Circular 33 del GORE Ñuble"
  Purp: |
    Orientar a las instituciones públicas que postulan iniciativas de inversión
    financiadas vía Oficio Circular 33 a través del GORE Ñuble, definiendo
    categorías de iniciativas, requisitos documentales, procesos de
    admisibilidad, evaluación, reevaluación y ejecución de proyectos C33.
  Destinatarios:
    - "Equipos del GORE Ñuble (Divisiones de Planificación, Presupuesto e Inversión Regional)."
    - "Municipalidades y servicios públicos que formulan y postulan iniciativas C33."
    - "Profesionales responsables de la formulación, evaluación y seguimiento de proyectos FNDR bajo C33."
  Alcance:
    - "Aplica a iniciativas que se acogen al Oficio Circular 33 financiadas con recursos FNDR vía GORE Ñuble."
    - "Incluye estudios propios del giro, adquisición/reposición de Activos No Financieros (ANF), conservación de caminos,
       conservación de infraestructura pública y gastos por situaciones de emergencia."
    - "Excluye proyectos de inversión tramitados por vías ordinarias SNI no acogidos al Oficio Circular 33."
  Objetivos_Especificos:
    - "Precisar el marco normativo y administrativo que sustenta la Guía y su vigencia."
    - "Definir categorías C33 y sus restricciones de uso, financiamiento y evaluación."
    - "Estandarizar la documentación requerida por tipo de iniciativa mediante una matriz única."
    - "Describir las fases del proceso de postulación, admisibilidad, evaluación técnica (RATE) y reevaluación."
    - "Clarificar el flujo de ejecución, convenios, transferencias y seguimiento de iniciativas C33."
  Estructura_Secciones:
    - ID: C33-SEC-1-ACTO-ADMIN
      Cpt: "Resolución aprobatoria, base legal, justificación y disposiciones de la Guía."
    - ID: C33-SEC-2-GUIA-CUERPO
      Cpt: "Contexto, alcances, marco normativo y categorías de iniciativas postulables."
    - ID: C33-SEC-3-REQ-DOC
      Cpt: "Matriz y detalle de requisitos documentales por tipo de iniciativa."
    - ID: C33-SEC-4-PROCESOS
      Cpt: "Proceso de evaluación, admisibilidad, reevaluación y ejecución de iniciativas."
    - ID: C33-SEC-5-ANEXOS
      Cpt: "Formularios y anexos estándar asociados a la Guía (Anexos 1, 2, 3, 4, 4B y 5)."

  Categorias_Principales:
    Estudios_Propios_Del_Giro:
      ID: C33-CAT-ESTUDIOS-GIRO-01
      Def: "Estudios propios del giro institucional de la entidad postulante."
      Warn:
        - "No confundir con estudios básicos (Ítem 01, Subtítulo 31) que generan nuevas iniciativas de inversión."
      Req:
        - "Si se postula un estudio bajo modalidad C33, debe financiarse con cargo al subtítulo 22, ítem 11."
        - "Estudios propios del giro de los GORE deben financiarse con recursos del Programa Gastos de Funcionamiento (01)."
      Proc:
        - "Para estudios de importancia regional que no sean del giro del GORE, éste debe solicitar a DIPRES creación del subtítulo 22 con recursos del Programa de Inversión."
        - "Para dicha autorización, el GORE debe enviar a DIPRES los TDR del Estudio y el Anexo 1 de la Guía."

    ANF_Adquisicion_y_Reposicion:
      ID: C33-CAT-ANF-01
      Def: |
        Adquisición y/o reposición de Activos No Financieros (ANF) asociados a inversión
        regional, sin formar parte de proyectos de inversión más amplios.
      Req:
        - "Se exigirá financiamiento compartido con la institución solicitante (aporte propio mínimo 20% del monto final del proyecto)."
        - "ANF corresponden al subtítulo 29 (formación de capital y compra de activos físicos existentes)."
        - "La adquisición de ANF sólo es posible si los activos no forman parte de un proyecto de inversión mayor."
      Tipos_ANF:
        - "Item-01-Terrenos: adquisición o expropiación de terrenos (requiere patrocinio de la División de Planificación y Desarrollo Regional GORE y autorización DIPRES)."
        - "Item-02-Edificios: compra o expropiación de viviendas, edificios y locales (mismos requisitos que terrenos)."
        - "Item-03-Vehiculos: automóviles, furgones, buses y otros vehículos no ligados a proyectos de inversión."
        - "Item-04-Mobiliario: mobiliario de oficinas, educacional, hospitalario y otros enseres."
        - "Item-05-MaquinasyEquipos: máquinas y equipos para funcionamiento, producción o mantenimiento."
        - "Item-06-EquiposInformaticos: equipos computacionales, periféricos y comunicaciones."
        - "Item-07-ProgramasInformaticos: adquisición y uso de software y sistemas de información."
        - "Item-99-Otros: otros activos definidos en la ley de presupuesto vigente."
      Distincion_Maquinaria_Vehiculo:
        ID: C33-CAT-ANF-MAQ-VEH-01
        Mdl: |
          |Criterio|Maquinaria|Vehículos|
          |-|-|-|
          |Capacidad|Cabina para 1 persona (conductor).|Cabina para >1 persona (conductor + acompañantes).|
          |Clasificador|Subt. 29, item 05.|Subt. 29, item 03.|
          |Ejemplos|Motoniveladoras, retroexcavadoras.|Camión aljibe, limpia fosas.|

    Conservacion_Caminos:
      ID: C33-CAT-CONS-CAMINOS-01
      Purp: "Invertir en conservación, reparación y mantención de infraestructura vial (pavimentos y caminos básicos)."
      Cond:
        - "La intervención no debe afectar la capacidad ni materialidad de la vía."
        - "No debe modificar significativamente la geometría de la vía."
      Alcance:
        - "Conservación/reposición de pavimentos, caminos básicos y obras anexas."
        - "Obras viales urbanas o rurales, enroladas o de tuición municipal."
      Tipos_Vias:
        - "Calles."
        - "Caminos."
        - "Veredas."
        - "Avenidas."
        - "Otros con carácter de conservación vial."
      Obras_Anexas:
        - "Vías interurbanas: obras de arte, señales, elementos de seguridad, saneamiento."
        - "Vías urbanas: veredas y soleras."
      Req:
        - "Para mantenimiento vial urbano debe utilizarse el software MANVU SIMP del MINVU."

    Conservacion_Infraestructura_Publica:
      ID: C33-CAT-CONS-INFRA-01
      Cond:
        - "No requerirán evaluación por parte de MIDESO si cumplen condiciones específicas de costo y vida útil."
      Req:
        - "Las iniciativas deben ingresar al Banco Integrado de Proyectos (BIP) para ser identificadas en el subtítulo 31."
      Criterios_Postulacion:
        - "Costo: reparaciones con costo total ≤ 30% del costo de reponer el activo."
        - "Vida útil dentro de período original: justificar en función del monto y características de la mantención incluida en el flujo de caja original; presentar a DIPRES con Ficha IDI (sin RATE)."
        - "Vida útil concluida: presentar estudio que evalúe alternativas (reponer vs. mantener) usando Costo Anual Equivalente (CAE)."
        - "Si la mejor solución es mantener y el costo ≤ 30% de reposición: presentar a DIPRES con Ficha IDI (sin RATE)."
        - "Si el costo supera 30% o se requiere reposición: la iniciativa debe presentarse al SNI y obtener recomendación de MIDESO."
      Limites_Presupuestarios:
        - "Equipamiento: se puede destinar hasta 20% del monto total del proyecto (requiere presupuesto anexo con 3 cotizaciones)."
        - "Gastos administrativos: no pueden superar 5% del valor total del proyecto (deben estar respaldados y detallados en el presupuesto, Anexo 5)."
      Req_Adicionales:
        - "Para proyectos de reposición total de pavimento, presentar informe de empresas concesionarias con redes subterráneas (ubicación y cotas)."
        - "Para conservación de infraestructura, aplicar criterios del Anexo 4B (Certificado de Conservación 30%)."

    Gastos_Situaciones_Emergencia:
      ID: C33-CAT-EMERGENCIA-01
      Ctx: "Desastres de origen natural y antrópico con fases sucesivas de atención."
      Fases_Post_Desastre:
        - "Emergencia."
        - "Rehabilitación."
        - "Reconstrucción (única fase que implica gastos de inversión)."
      Fase_Emergencia:
        Proc:
          - "Gastos se imputan al ítem 'Para atender Situaciones de Emergencia' del presupuesto de la Subsecretaría del Interior."
        Resp:
          - "Subsecretaría del Interior califica la situación y autoriza el gasto."
      Fase_Rehabilitacion:
        Nat: "Fase de transición para preparar la reconstrucción."
        Cpt:
          - "Incluye soluciones transitorias (viviendas de emergencia, despeje de caminos, retiro de escombros)."
        Resp:
          - "Gestión y asignación de recursos es realizada por el GORE."
        Prohib:
          - "No se puede postular esta fase vía Circular 33."
      Fase_Reconstruccion:
        Ctx: "Para territorios declarados como Zona de Catástrofe."
        Proc:
          - "Se aplica proceso de agilización para formulación y análisis de iniciativas."
          - "Las iniciativas de inversión deben ser enviadas al SNI para análisis."
        Ex:
          - "Si la intervención corresponde a 'Reparaciones Menores', se procede como 'Conservación de Infraestructura Pública'."
        Inversion_vs_Gasto:
          Def:
            - "Etapas de emergencia y rehabilitación corresponden a gasto (paliativo), no inversión."
            - "Etapa de reconstrucción corresponde a inversión (carácter permanente)."

  Sec_1_Acto_Administrativo_y_Base_Legal:
    ID: C33-SEC-1-ACTO-ADMIN
    Resolucion_Aprobatoria:
      ID: C33-RESOLUCION-APROB-01
      Nat: "Resolución Exenta."
      Metadatos:
        - "ID-Documento: 4A/00269/18.03.2025."
        - "Materia: Actualiza y aprueba Guía Operativa para la Formulación y Evaluación de Iniciativas Circular 33 al GORE Ñuble."
        - "Firmante: Gobernador Regional de Ñuble (s)."
        - "Fecha-Firma: 2025-03-18 09:40 CLT."
        - "Validador-Digital: https://doc.digital.gob.cl/validador/V0DWCS-931."
    Base_Legal_y_Regulatoria:
      ID: C33-VISTOS-01
      Fnd:
        - "Artículo 111 de la Constitución Política de la República."
        - "Ley N° 19.175 Orgánica Constitucional sobre Gobierno y Administración Regional (art. 24, literal ñ))."
        - "Ley N° 21.074 sobre Fortalecimiento de la Regionalización del País."
        - "Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado."
        - "Ley N° 21.796, Presupuestos Sector Público 2026 (Partida 31, Programa 02, glosas comunes)."
        - "Ley N° 19.880, Bases de los Procedimientos Administrativos."
        - "Resolución N°36/2024 CGR (Normas sobre exención de Toma de Razón)."
        - "Oficio Circular 33 (13-07-2009) del Ministerio de Hacienda."
        - "Resolución Exenta 811/2020 del GORE Ñuble (procedimiento Gestión Preinversional)."
        - "Acta de Proclamación de Elección de Gobernadores Regionales 2025-2029 (Sentencia Rol N°817-2024)."
        - "Certificado N°1131 (2025-01-07) del Consejo Regional de Ñuble."
        - "Resolución Exenta N°35 (2025-01-08) del Servicio Administrativo del GORE Ñuble."
        - "Resolución Exenta N°206 (2025-02-28) del GORE Ñuble (orden de subrogancias)."
    Justificacion_y_Fundamentos:
      ID: C33-CONSIDERANDO-01
      Cpt:
        - "La administración superior de la región radica en el GORE, que persigue desarrollo social, cultural y económico usando el Presupuesto de Inversión Regional como instrumento fundamental."
        - "El servicio administrativo del GORE Ñuble y el Departamento de Preinversión iniciaron funciones de evaluación de iniciativas de inversión en 2018."
        - "Se priorizan iniciativas con recomendación satisfactoria tipología C33 por instrucción de la División de Planificación y Desarrollo Regional."
        - "Es necesario orientar técnica y administrativamente la solicitud de financiamiento, optimizando el trabajo bajo principios de eficiencia y eficacia."
        - "La Guía Operativa es de carácter indefinido, sujeta a modificaciones futuras mediante nuevas resoluciones exentas."
    Disposiciones_Resuelvo:
      ID: C33-RESUELVO-01
      Instr:
        - "Aprobar la Guía Operativa para formulación y evaluación de iniciativas Circular 33 para el año presupuestario vigente y posteriores."
        - "Dejar sin efecto la Resolución Exenta 4A N°103 del 05-03-2024."
        - "Declarar que el texto aprobado corresponde al contenido del documento de la Guía."
        - "Establecer como mecanismo oficial de postulación la plataforma GESDOC."
        - "Mientras GESDOC se encuentra en implementación, el mecanismo de postulación será el ingreso formal por Oficina de Partes con antecedentes en el BIP."
        - "Ordenar la publicación de la resolución en el sitio web del GORE Ñuble y en el Portal de Transparencia Activa."
      Cond:
        - "La vigencia de la Guía está sujeta a la no existencia de modificaciones en la normativa legal vigente que la sustenta."

  Sec_2_Cuerpo_Guia_Operativa:
    ID: C33-SEC-2-GUIA-CUERPO
    Introduccion:
      ID: C33-INTRO-01
      Ctx:
        - "Los GORE son responsables de la administración superior de cada región, velando por el desarrollo armónico y equitativo del territorio."
        - "La Ley de Presupuestos 2026 modifica alcances de financiamiento y categorías de postulación para los GORE, otorgándoles clasificación institucional propia (Partida 31, Programa 02)."
        - "El instructivo regula el procedimiento de postulación, evaluación, aprobación y ejecución de iniciativas C33 financiadas con FNDR."
      Mssn:
        - "Velar por el desarrollo armónico y equitativo de Ñuble mediante uso eficiente del FNDR."
      Purp:
        - "Proveer una guía operativa clara para formuladores y evaluadores de iniciativas C33 del GORE Ñuble."
    Alcances_y_Modificaciones:
      ID: C33-ALCANCE-MOD-01
      Obj:
        - "Establecer requisitos y procedimientos para postulación y evaluación de proyectos C33."
      Ctx:
        - "Las instrucciones no son aplicables a otros tipos de evaluación o financiamiento fuera del Oficio Circular 33."
      Cpt:
        - "Cada institución pública puede postular una o más iniciativas."
      Warn:
        - "La postulación no implica obligación de financiamiento por parte del GORE."
      Dep:
        - "El financiamiento está sujeto a disponibilidad presupuestaria FNDR y naturaleza del proyecto."
      Purp:
        - "Estandarizar y normalizar procesos internos de formulación, revisión y tramitación administrativa para mejorar eficiencia en la ejecución presupuestaria."
    Marco_Normativo_Referencia:
      ID: C33-MARCO-NORM-REF-01
      Fuentes:
        - ID: C33-NORM-OFICIO-33-01
          Cpt: "Oficio Circular N°33 (2009)."
          Src:
            - "Ministerio de Hacienda; establece procedimiento expedito para asignación de recursos a estudios del giro, ANF, emergencias y mantención de infraestructura pública."
            - "URL de referencia en la guía original (sni.gob.cl)."
        - ID: C33-NORM-LEY-21796-01
          Cpt: "Ley N°21.796 (Presupuesto 2026)."
          Nat: "Norma legal vigente sobre ingresos y gastos del sector público para 2026."
          Ctx:
            - "Clasificación institucional propia de los GORE en la partida 31."
            - "Glosas comunes establecen mecanismo de financiamiento vía programa de inversión."
        - ID: C33-NORM-METOD-GRAL-01
          Cpt: "Metodología general de evaluación de proyectos sociales."
          Ctx:
            - "Metodología base cuando no existe metodología sectorial definida."
            - "Validada por el Sistema Nacional de Inversiones (SNI), MIDESO."
        - ID: C33-NORM-REEMPLAZO-EQUIPOS-01
          Cpt: "Metodología de reemplazo de equipos."
          Purp:
            - "Entregar elementos para decidir adquisición o reemplazo de equipos y facilitar selección de alternativas."
          Ctx:
            - "Sirve como guía para análisis de costo marginal en reposición de ANF."
        - ID: C33-NORM-NIP-01
          Cpt: "Normas de Inversión Pública (NIP)."
          Def: "Normas que rigen la inversión del Estado bajo estándares técnicos y económicos para distribución eficiente de recursos."

    Categorias_Iniciativas_Postulables:
      ID: C33-CAT-POSTULABLES-01
      Obj:
        - "Financiar proyectos en cuatro grandes líneas de inversión a través de Circular 33: estudios del giro, ANF, conservación de caminos, conservación de infraestructura pública y gastos en emergencias."
      Ref:
        - C33-CAT-ESTUDIOS-GIRO-01
        - C33-CAT-ANF-01
        - C33-CAT-CONS-CAMINOS-01
        - C33-CAT-CONS-INFRA-01
        - C33-CAT-EMERGENCIA-01

  Sec_3_Requisitos_Documentacion:
    ID: C33-SEC-3-REQ-DOC
    Ctx:
      - "La documentación requerida varía según categoría de iniciativa; se resume en una matriz y se detalla por tipo de documento."
    Matriz_Documentacion:
      ID: C33-MATRIZ-DOC-01
      Src:
        - "Tabla 'Documento' (pág. 11 de la guía original)."
      Mdl: |
        |#|Documento|Estudio Propio Giro|ANF (Terrenos/Edificios)|ANF (Vehíc/Maquinaria)|Conserv. Caminos|Conserv. Infra. Pública|Emergencia|
        |-|-|-|-|-|-|-|-|
        |1|Oficio Conductor|X|X|X|X|X|X|
        |2|Ficha IDI|X|X|X|X|X|X|
        |3|Ficha C-33 (Anexo 1)|X|X|X|||X|
        |4|Formulario Estudios (Anexo 2)|X||||||
        |5|Términos de Referencia|X|X|||||
        |6|Especificaciones Técnicas|X|Sólo si procede|X|X|X|Sólo si procede|
        |7|Presupuesto Detallado|X|Sólo si procede|X|X|X|Sólo si procede|
        |8|Formulario Proyectos (Anexo 3)||X|X|X|||
        |9|Planilla Evaluación Económica||X|X|X|X|Sólo si procede|
        |10|3 Cotizaciones / Tasaciones||Tasaciones|X||||
        |11|Cert. Dotación Vehículos|||Sólo motorizados|||
        |12|Cert. Técnico Mal Estado ANF|||Solo reposición|||
        |13|Planilla Costo Marginal|||Solo reposición|||
        |14|Cert. Compromiso Baja Activo|||Solo reposición|||
        |15|Cert. Compromiso Costo Op/Man||X|X|X|X|Sólo si procede|
        |16|Cert. de Pertinencia||Sólo si procede|Sólo si procede|X|Sólo si procede|Sólo si procede|
        |17|Formulario Conservación (Anexo 4)||||X|X||
        |18|Informe Manvu SIMP||||X|||
        |19|Certificado de Terreno||X|Sólo si procede|X|X|X|
        |20|Cert. Participación Ciudadana||||X|X|Sólo si procede|
        |21|Visación del Servicio||||X|Sólo si procede|Sólo si procede|
        |22|Cert. Título Profesional||||X|X|X|
        |23|Fotografías, KMZ y Presentación|X|X|X|X|X|X|
        |24|Planilla de Cubicaciones||||X|X|X|
        |25|Planos del Proyecto||X||X|X|X|
        |26|Proyecto de Cálculo||||Sólo si procede|X|X|
        |27|Cert. Recepción Obra Existente||X||X|X|X|
        |28|Cronograma de Actividades|X|X||X|X|X|
        |29|Decreto de Emergencia||||||X|
        |30|Compromiso Financiamiento Compartido||X|X|||
        |31|Cert. Conservación 30% (Anexo 4B)||||X|||

    Reglas_Generales_Documentacion:
      ID: C33-REQ-DOC-REGLAS-01
      Cpt:
        - "Toda la trazabilidad del proyecto debe desarrollarse en la plataforma GESDOC."
        - "Los antecedentes finales deben quedar respaldados en el Banco Integrado de Proyectos (BIP) del SNI de manera ordenada y definitiva."

    Detalle_Documentos:
      Doc_1_Oficio_Conductor:
        ID: C33-DOC-01-OFICIO
        Req:
          - "Firmado por Jefe de Servicio o Alcalde(sa)."
          - "Dirigido al Gobernador Regional."
          - "Debe contener nombre del proyecto (concordante con Ficha IDI) y código BIP."
          - "Debe explicitar relación con Estrategia Regional de Desarrollo Ñuble 2022-2030 (Eje, Lineamiento, Objetivo, Acción)."
          - "Si postula Municipalidad, debe indicar relación con PLADECO comunal (Eje, Lineamiento, Acción)."
        Proc:
          - "Ingresar a plataforma GESDOC."
          - "Cargar oficio firmado en carpeta digital del BIP, subcarpeta 'oficios'."
        Warn:
          - "El incumplimiento de requisitos de contenido o carga de archivos resultará en declaración de INADMISIBLE de la iniciativa."

      Doc_2_Ficha_IDI:
        ID: C33-DOC-02-FICHA-IDI
        Req:
          - "Descargada del BIP con el código del proyecto."
          - "Debe corresponder al año presupuestario en ejercicio."
          - "La etapa a postular debe ser 'Ejecución'."
          - "Para ANF, el descriptor debe indicar 'Subtítulo 29'."
          - "Información coherente con antecedentes de respaldo y presupuesto."
          - "Clasificador presupuestario alineado con presupuesto detallado."
          - "En cofinanciamiento, registrar aporte en cuadro de solicitud de financiamiento."
          - "El monto total (FNDR, Sectorial, otros) debe ser igual en ficha IDI, presupuesto y oficio conductor."
        Proc:
          - "Ingresar en plataforma GESDOC."
          - "Cargar como antecedente en carpeta digital del BIP."

      Doc_3_Ficha_Circular_33:
        ID: C33-DOC-03-FICHA-C33
        Def: "Ficha general para iniciativas de estudios del giro, ANF y gastos de emergencia."
        Ctx:
          - "No es necesaria para categorías de conservación."
        Ref:
          - "Formato disponible en sitio web del GORE Ñuble (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01)."
        Proc:
          - "Cargar como antecedente en carpeta digital del BIP, subcarpeta 'Estudio Preinversional'."

      Doc_4_Formulario_Estudios:
        ID: C33-DOC-04-FORM-ESTUDIOS
        Def: "Documento metodológico que explica origen de la problemática, alternativas y consistencia del estudio."
        Req:
          - "Información coherente con anexos y complementos."
        Ref:
          - "Formato disponible en sitio web del GORE Ñuble (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01)."

      Doc_5_Terminos_Referencia:
        ID: C33-DOC-05-TDR
        Def: "Presentación detallada de materias del estudio/proyecto; base técnica para licitación."
        Req:
          - "Deben ser detallados y precisos."
          - "Respaldados por cotizaciones desglosadas."
          - "Coherentes con objetivos del estudio/proyecto."
        Contenido_Minimo:
          - "Diagnóstico y definición del problema."
          - "Objetivos generales y específicos."
          - "Localización geográfica y cobertura."
          - "Variables a medir/controlar."
          - "Descripción de actividades."
          - "Metodología a utilizar."
          - "Cronograma de actividades (Carta Gantt)."
          - "Resultados o productos esperados, valorizados."
          - "Mecanismos de difusión de la información."
          - "Definición de número, tipo, contenido y resultados de informes de avance."
        Proc:
          - "Cargar en carpeta digital del BIP, subcarpeta 'Especificaciones Técnicas'."

      Doc_6_Especificaciones_Tecnicas:
        ID: C33-DOC-06-EETT
        Req:
          - "Detalladas y precisas (materialidad, dimensiones, métodos de ejecución)."
          - "Suscritas por profesional competente y Director SECPLAN (si postula Municipalidad)."
          - "Desglosadas por partidas, coherentes con presupuesto."
        Ctx:
          - "Para ANF, pueden contener marcas/modelos referenciales."
          - "Para conservaciones, deben ser por cada partida con ítems iguales a presupuesto y planimetría."
          - "Deben referenciar el Manual de Normas Gráficas del GORE Ñuble."
        Proc:
          - "Cargar en carpeta digital del BIP, subcarpeta 'Especificaciones Técnicas'."
          - "Incorporar en postulación vía GESDOC."

      Doc_7_Presupuesto_Detallado:
        ID: C33-DOC-07-PRESUPUESTO
        Req:
          - "Información cargada en BIP coherente con cada actividad."
        Requisitos_Elaboracion:
          - "Ingresar a BIP en PDF y Excel."
          - "Ítems coherentes con clasificadores presupuestarios."
          - "Detallar al máximo (unidad, cantidad, precio unitario)."
          - "Incluir IVA en compras y tributación en servicios."
          - "Analista GORE puede solicitar Análisis de Precio Unitario (APU)."
          - "En financiamiento compartido, contar con V°B° de Unidad Financiera del servicio."
          - "Gastos administrativos no pueden superar 5% del costo total."
        Proc:
          - "Cargar en BIP y GESDOC."

      Doc_8_Formulario_ANF:
        ID: C33-DOC-08-FORM-ANF
        Def: "Formulario metodológico para proyectos de Adquisición de ANF."
        Req:
          - "Información coherente con anexos."
        Ref:
          - "Formato disponible en sitio web del GORE Ñuble (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01)."

      Doc_9_Planilla_Evaluacion_Economica:
        ID: C33-DOC-09-EVAL-ECO
        Ctx:
          - "Aplica a ANF y conservaciones."
        Def: "Cálculo de indicadores económicos (VAC, CAE) para evaluar rentabilidad o costo-eficiencia."
        Req:
          - "Justificar datos con cotizaciones, presupuesto y otros antecedentes."
          - "Enfoque costo-eficiencia."
          - "Considerar vida útil según tabla del SII."
          - "Señalar fórmula y datos para valor residual."
          - "Realizar análisis a precios sociales vigentes."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Evaluación Económica') y GESDOC."

      Doc_10_Cotizaciones_Tasaciones:
        ID: C33-DOC-10-COTIZ-TAS
        Ctx:
          - "Para adquisición/reposición de ANF."
        Req:
          - "Adjuntar 3 cotizaciones de distintos proveedores."
          - "En proveedor único, adjuntar informe justificando inexistencia de más proveedores, firmado por Jefe de Servicio o Alcalde."
          - "Para terrenos y edificios, presentar Certificado de Avalúo Fiscal vigente (<60 días) y 3 tasaciones de distintos proveedores."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_11_Cert_Dotacion_Vehiculos:
        ID: C33-DOC-11-CERT-VEH
        Def: "Detalle de toda la flota de la institución postulante (marca, año, patente, estado)."
        Ctx:
          - "Si postula Municipalidad, debe ser avalado por el Concejo Municipal."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_12_Cert_Tecnico_Mal_Estado:
        ID: C33-DOC-12-CERT-MAL-ESTADO
        Ctx:
          - "Aplica sólo para reposición de activo."
        Def: "Informe sobre el estado actual del activo a reponer."
        Req:
          - "Emitido por profesional competente (interno o externo)."
          - "Debe incluir bitácora de fallas y razones para la reposición."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_13_Planilla_Costo_Marginal:
        ID: C33-DOC-13-COSTO-MARGINAL
        Ctx:
          - "Aplica sólo para reposición de activo."
        Def: "Cálculo del costo de mantener vigente el ANF un año adicional, argumentando optimización de la situación base."
        Proc:
          - "Formato Excel libre; cargar en BIP (subcarpeta 'Evaluación Económica') y GESDOC."

      Doc_14_Cert_Compromiso_Baja_Activo:
        ID: C33-DOC-14-CERT-BAJA
        Ctx:
          - "Aplica sólo para reposición de activo."
        Def: "Compromiso de que el activo antiguo no seguirá en operaciones una vez financiada la iniciativa."
        Ctx_Adicional:
          - "Si postula Municipalidad, debe ser avalado por Concejo Municipal."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_15_Cert_Compromiso_Costo_Op_Mant:
        ID: C33-DOC-15-CERT-OP-MANT
        Def: "Documento con detalle de costos de operación y mantención de la alternativa seleccionada."
        Req:
          - "Utilizar precios privados."
          - "Indicar nombre de la iniciativa y código BIP."
          - "Incluir montos para todo el período de vida útil del proyecto."
        Ctx:
          - "Si postula Municipalidad, debe ser emitido por Concejo Municipal u organización usuaria."
          - "Si postula otro servicio, debe ser emitido por Jefe de Servicio con visación de Finanzas."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_16_Cert_Pertinencia:
        ID: C33-DOC-16-CERT-PERT
        Req:
          - "Emitido por servicios competentes o por el alcalde, según tipo de proyecto."
        Purp:
          - "Acreditar que el proyecto no se asocia a otra iniciativa de inversión ni tiene doble financiamiento."
        Mdl: |
          |Tipo de Proyecto|Servicio/Municipalidad Emisora|
          |-|-|
          |Deportivos (formativo/competitivo)|Instituto Nacional de Deportes|
          |Deportivos (recreativo)|Municipalidad|
          |Infraestructura de salud|SEREMI de Salud|
          |Infraestructura educacional|SEREMI de Educación|
          |Obras en cauces de ríos|DOH, Asociación de Canalistas|
          |Obras viales rurales|Dirección de Vialidad|
          |Obras viales urbanas|SERVIU|
          |Redes alcantarillado/agua potable|SEREMI de Salud, DOH, Empresa Sanitaria|
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_17_Form_Conservacion:
        ID: C33-DOC-17-FORM-CONS
        Def: "Formulario metodológico para proyectos de conservación (Anexo 4)."
        Ref:
          - "Formato disponible en sitio web del GORE Ñuble (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01)."

      Doc_18_Informe_MANVU_SIMP:
        ID: C33-DOC-18-MANVU
        Ctx:
          - "Aplica sólo a conservación de vialidad urbana."
        Def: "Informe del software MANVU SIMP para proyectos de mantenimiento vial urbano."
        Src:
          - "Solicitado por Oficio C33 y NIP."
        Proc:
          - "Imprimir resultados en PDF y cargar en BIP (subcarpeta 'Anexos')."

      Doc_19_Cert_Terreno:
        ID: C33-DOC-19-CERT-TERRENO
        Req:
          - "Escritura de propiedad, dominio vigente y avalúo fiscal actualizados (<60 días)."
        Cpt:
          - "Para Bien Nacional de Uso Público (BNUP), presentar certificado DOM que acredite condición."
          - "Si no está bajo tuición municipal, adjuntar concesión o autorización de uso."
          - "Para caminos vecinales, adjuntar documentos que acrediten cumplimiento del Decreto 293 del MOP."
        Proc:
          - "Cargar en BIP (subcarpeta 'Terrenos') y GESDOC."

      Doc_20_Cert_Participacion_Ciudadana:
        ID: C33-DOC-20-CERT-PART
        Req:
          - "Realizar al menos una instancia de Participación Ciudadana (recomendable dos)."
          - "Debe existir reunión con beneficiarios, municipio y representante de División de Desarrollo Social del GORE como ministro de fe."
        Proc:
          - "Cargar certificado firmado en BIP (subcarpeta 'Anexos')."

      Doc_21_Visacion_Servicio:
        ID: C33-DOC-21-VISACION
        Req:
          - "Proyectos que involucren competencia de otros servicios deben acreditar su aprobación."
          - "Para riberas (lagos, ríos, playas), se requiere concesión de uso."
          - "Intervenciones en cursos de agua pueden requerir visación de Gobernación Marítima."
          - "Proyectos con resolución sanitaria (plantas de tratamiento, piscinas) deben presentar proyecto aprobado por SEREMI de Salud."
          - "Conservación de graderías (>100 personas) requiere memoria de cálculo."
          - "Construcción en área rural requiere Informe Favorable para la Construcción (Art. 55 LGUC)."
        Proc:
          - "Cargar antecedentes con timbres de visación en BIP y GESDOC."

      Doc_22_Cert_Titulo_Profesional:
        ID: C33-DOC-22-CERT-TITULO
        Ctx:
          - "Exigible sólo para proyectos de Conservación."
        Def: "Antecedentes del profesional competente responsable de documentos técnicos."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_23_Fotografias_KMZ_Presentacion:
        ID: C33-DOC-23-FOTOS-KMZ
        Cpt:
          - "Fotografías: mínimo 4 de la situación actual, con antigüedad ≤ 6 meses."
          - "KMZ/KML: localización en coordenadas UTM (Huso 18S, WGS84) o archivo KML/KMZ."
          - "Presentación: formato PPT, Prezi, Canva u otro, explicando finalidad del proyecto e impacto regional."
        Proc:
          - "Cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_24_Planilla_Cubicaciones:
        ID: C33-DOC-24-CUBICACIONES
        Ctx:
          - "Aplica a conservación de caminos e infraestructura pública."
        Req:
          - "Archivo Excel con cubicaciones coherentes con EETT, Presupuesto y Planos."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Planimetría') y GESDOC."

      Doc_25_Planos_Proyecto:
        ID: C33-DOC-25-PLANOS
        Req:
          - "Tamaño A1, formatos PDF y DWG."
        Contenido_Minimo:
          - "Render (para proyectos de arquitectura)."
          - "Planos de Ubicación (escala mínima 1:500)."
          - "Plano de Emplazamiento (escala mínima 1:100)."
          - "Planos de Arquitectura (escala mínima 1:50)."
          - "Planos de Detalle (escalas 1:25 y/o 1:10)."
          - "Planos informativos de especialidades (agua, gas, etc.)."
          - "Planos topográficos cuando el evaluador lo solicite."
        Proc:
          - "Cargar en BIP (subcarpeta 'Planimetría') y GESDOC."

      Doc_26_Proyecto_Calculo:
        ID: C33-DOC-26-PROY-CALC
        Ctx:
          - "Requerido cuando normativa (LGUC, OGUC, etc.) lo exija."
        Req:
          - "Memoria de Cálculo, Planimetría estructural y EETT detalladas."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Planos') y GESDOC."

      Doc_27_Cert_Recepcion_Obra_Existente:
        ID: C33-DOC-27-CERT-RECEP
        Ctx:
          - "Aplica para conservación de infraestructura."
        Def: "Documento de DOM que acredita que el inmueble a intervenir cumple OGUC."
        Proc:
          - "Formato libre; cargar en BIP (subcarpeta 'Planimetría') y GESDOC."

      Doc_28_Cronograma_Actividades:
        ID: C33-DOC-28-CRONOGRAMA
        Def: "Carta Gantt de actividades y financiera."
        Req:
          - "Identificar tareas, hitos y prelación."
          - "Gantt financiera debe especificar costos de cada actividad en el tiempo."
        Proc:
          - "Formato libre (Excel, Project, etc.) exportado a PDF; cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_29_Decreto_Emergencia:
        ID: C33-DOC-29-DEC-EMERG
        Ctx:
          - "Aplica para iniciativas de reconstrucción."
        Def: "Documento oficial que decreta la situación de emergencia."
        Proc:
          - "Cargar en BIP (subcarpeta 'Anexos') y GESDOC."

      Doc_30_Compromiso_Financiamiento_Compartido:
        ID: C33-DOC-30-COMP-FINAN
        Def: "Certificado de la División/Dirección de Finanzas del servicio autorizando el aporte para financiamiento compartido."
        Ctx:
          - "Relaciona con ANF (Subt. 29, ítems 03-05)."

      Doc_31_Cert_Conservacion_30:
        ID: C33-DOC-31-CERT-30
        Def: "Certificado que indica que el costo del proyecto de conservación es ≤ 30% del costo de reposición total del activo."
        Ref:
          - "Formato Anexo 4B (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01)."

  Sec_4_Proceso_Evaluacion_y_Tramitacion:
    ID: C33-SEC-4-PROCESOS
    Unidades_Responsables_y_Directrices:
      ID: C33-PROC-UNID-01
      Unidades_Responsables:
        - "División de Planificación y Desarrollo Regional, a través del Departamento de Análisis y Evaluación: evalúa pertinencia, admisibilidad y determina elegibilidad/ejecutabilidad."
        - "Jefe de División de Planificación y Desarrollo Regional: puede encargar evaluación a profesionales de otras unidades mediante resolución exenta."
        - "Departamento de Análisis y Evaluación: realiza seguimiento de tramitación hasta resolución presupuestaria."
        - "División de Presupuesto e Inversión Regional: responsable de gestión financiera para puesta en marcha y ejecución una vez aprobados los recursos."
      Directrices_Generales:
        Req:
          - "Sólo se revisarán iniciativas alineadas con el progreso de la región."
          - "Iniciativas deben considerar y señalar alineación con Estrategia Regional de Desarrollo Ñuble 2022-2030."
        Warn:
          - "La postulación no obliga al GORE a financiar la totalidad de los proyectos."
          - "Un mal desempeño en ejecución de proyectos anteriores puede limitar nuevo financiamiento."
        Dep:
          - "Financiamiento depende de obtención de RS, priorización regional y disponibilidad presupuestaria."
        Prohib:
          - "Postular iniciativas FNDR a otras fuentes de financiamiento público (evitar doble financiamiento)."

    Ciclo_Vida_Postulacion:
      ID: C33-PROC-CICLO-01
      Fase_1_Plazos:
        ID: C33-PROC-FASE1-01
        Cpt:
          - "Difusión: durante todo el año mediante web institucional."
          - "Postulación: desde aprobación del marco presupuestario hasta el 31 de octubre de cada año."
          - "Asesoría técnica: acompañamiento metodológico disponible durante todo el período, solicitada por correo al Jefe del Departamento de Análisis y Evaluación."
      Fase_2_Ingreso_Iniciativas:
        ID: C33-PROC-FASE2-01
        Mech:
          - "Ingreso mediante banner 'CIRCULAR 33' en la web www.goredenuble.cl."
        Req:
          - "Adjuntar oficio conductor y Ficha IDI."
        Proc:
          - "Oficina de Partes deriva a Depto. de Análisis y Evaluación para registro y derivación al Comité de Pertinencia para evaluación inicial."
      Fase_3_Admisibilidad:
        ID: C33-PROC-FASE3-ADM-01
        Resultados_Posibles:
          Admisible:
            Def: "Proyecto cuenta con toda la documentación y está en condiciones para análisis técnico."
            Proc:
              - "Analista informa por correo electrónico."
          Admisible_con_Observaciones:
            Def: "Proyecto presenta errores de forma o falta de patrocinio, pero es comprensible en su generalidad."
            Req:
              - "Plazo máximo de subsanación: 5 días hábiles."
            Res:
              - "Si no se cumple plazo, la iniciativa queda INADMISIBLE."
          Inadmisible:
            Def: "Proyecto con errores de forma y fondo, sin coherencia o incumplimiento normativo."
            Cause:
              - "No presenta archivos requeridos en BIP."
              - "No se alinea con Estrategia Regional de Desarrollo."
              - "Está postulada a otras fuentes de financiamiento."
              - "No se subsanaron observaciones en plazo de 5 días."
            Proc:
              - "Se informa mediante oficio del Jefe de División."
      Fase_4_Etapa_Revision_Tecnica:
        ID: C33-PROC-FASE4-REV-01
        Proc:
          - "Se realiza evaluación técnica de iniciativas declaradas admisibles."
        Resultados_RATE:
          RS:
            Cpt: "Recomendado Satisfactoriamente (RS)."
            Def: "Aprobación técnica de la iniciativa; queda en condiciones de ser presentada para aprobación de financiamiento."
            Cpt_Adicional:
              - "La certificación RS es válida para el año en que se obtiene."
              - "RS no reemplaza responsabilidades civiles y administrativas de profesionales que diseñaron la iniciativa."
          No_Recomendado:
            Subtipos:
              - "FI (Falta Información): antecedentes insuficientes, errores de cálculo o necesidad de actualización."
              - "OT (Objetado Técnicamente): iniciativa mal formulada, con problemas técnicos o normativos insubsanables."
              - "NV (No Vigente): no se cumplen plazos de subsanación, el formulador desiste o existen incompatibilidades normativas."
              - "IN (Incumplimiento de Normativa): se han asignado recursos o ejecutado gasto sin informe favorable previo del GORE."
        Respuesta_Observaciones:
          ID: C33-PROC-RESP-OBS-01
          Proc:
            - "Formulador debe resolver observaciones y adjuntar antecedentes en BIP dentro del plazo fijado."
            - "Respuesta debe ser informada mediante oficio ingresado por web del GORE."
            - "Se puede solicitar ampliación de plazo con fundamentos claros."

    Proceso_Reevaluacion:
      ID: C33-PROC-REEVAL-01
      Ctx:
        - "Solicitud debe realizarse entre 60 días post-aprobación técnica y 30 días antes del término del plazo de ejecución."
      Req:
        - "Dirigir solicitud al GORE con antecedentes de respaldo (resumen ejecutivo, informe ITO GORE, presupuestos, etc.)."
      Proc:
        - "Solicitud es revisada por Departamento de Presupuesto o de Inversiones, según etapa administrativa de la iniciativa."
      Casos_Permitidos:
        - "Cambios en actividades que no afecten componentes."
        - "Eliminación o incorporación de actividades."
        - "Aumentos de plazos sustanciales (>30 días)."
      Warn:
        - "El GORE no aceptará reevaluaciones que impliquen cambios en el objetivo del proyecto."
        - "No se aceptan cambios de materialidad, salvo casos que afecten habitabilidad."
        - "No se aceptan cambios de ubicación que originen cambio de rol, con excepciones justificadas."
      Fase_Reemplazo_Iniciativas:
        ID: C33-PROC-REEMPLAZO-01
        Prohib:
          - "En general no se permite el reemplazo de iniciativas."
        Cond:
          - "Sólo se admiten reemplazos en situaciones particulares, debidamente fundamentadas y aprobadas por resolución exenta del Gobernador Regional."

    Proceso_Ejecucion:
      ID: C33-PROC-EJEC-01
      Solicitud_Financiamiento:
        ID: C33-PROC-EJEC-FINAN-01
        Proc:
          - "Departamento de Análisis y Evaluación emite reporte semanal de iniciativas con RS al Gobernador para solicitar financiamiento."
          - "Se elabora resolución exenta que incorpora la iniciativa al marco presupuestario, previa consulta de disponibilidad al Departamento de Presupuesto."
      Elaboracion_Convenio:
        ID: C33-PROC-EJEC-CONVENIO-01
        Resp:
          - "Departamento de Presupuestos de la División de Presupuesto e Inversión Regional."
        Proc:
          - "Una vez emitida la resolución presupuestaria, se inicia la suscripción del convenio de transferencia."
      Transferencia_Recursos:
        ID: C33-PROC-EJEC-TRANSF-01
        Mech:
          - "Transferencia vía estados de pago, según avance efectivo avalado por Inspector Técnico GORE."
        Req:
          - "Servicio receptor debe mantener cuenta corriente exclusiva para recursos FNDR."
      Seguimiento:
        ID: C33-PROC-EJEC-SEG-01
        Resp:
          - "Inspector Técnico designado."
        Act:
          - "Hacer seguimiento físico y financiero de la iniciativa."
        Req:
          - "Reportar bimensualmente al Jefe de División correspondiente."
      Duracion_Iniciativa:
        ID: C33-PROC-EJEC-DURACION-01
        Def:
          - "La ejecución se establece hasta la extinción de su recomendación técnica (año en curso + 2 años calendario)."
        Cond:
          - "Si pasado este período el proyecto está en ejecución, debe terminar dentro del tiempo del convenio."
          - "Si pasado este período el proyecto no está en ejecución, se entenderá como no vigente y el GORE puede dejar sin efecto el convenio."

  Sec_5_Anexos_y_Formularios:
    ID: C33-SEC-5-ANEXOS
    Ctx:
      - "Los anexos se implementan como formularios estructurados; la Guía incluye versiones maestras referenciadas por otros sistemas (ej. GUIDE-SFD-STS-MASTER-01)."
    Formularios_Principales:
      - ID: C33-ANEXO-1-FICHA-C33
        Cpt: "Ficha de Postulación Circular 33 (Anexo N°1)."
        Purp: "Recopilar información básica de la iniciativa (identificación, tipología, montos, justificación)."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-C33-ANEXO1-V1 (bloque embebido en fuente STS)."
      - ID: C33-ANEXO-2-FORM-ESTUDIOS
        Cpt: "Perfil para Proyectos de Estudios (Anexo N°2)."
        Purp: "Estructurar diagnóstico, objetivos, alcance y productos esperados del estudio."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-ESTUDIOS-ANEXO2-V1."
      - ID: C33-ANEXO-3-FORM-ANF
        Cpt: "Perfil para Proyectos de Adquisición de Activos No Financieros (ANF) (Anexo N°3)."
        Purp: "Caracterizar situación actual, beneficiarios, descripción del proyecto y evaluación económica resumida."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-ANF-ANEXO3-V1."
      - ID: C33-ANEXO-4-FORM-CONS
        Cpt: "Perfil para Proyectos de Conservación (Anexo N°4)."
        Purp: "Documentar diagnóstico de infraestructura, obras de conservación propuestas y pertinencia técnica/económica."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-CONSERVACION-ANEXO4-V1."
      - ID: C33-ANEXO-4B-CERT-CONS-30
        Cpt: "Certificado de Conservación de Infraestructura Pública (Anexo N°4B)."
        Purp: "Certificar que el costo de la conservación es ≤ 30% del costo de reposición y que el proyecto no enfrenta restricciones técnicas/legales."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-CERTIFICADO-ANEXO4B-V1."
      - ID: C33-ANEXO-5-PRESUPUESTO-DETALLADO
        Cpt: "Presupuesto Detallado para Proyectos de Conservación (Anexo N°5)."
        Purp: "Estructurar partidas, unidades, cantidades, precios unitarios y totales, además del resumen de costos."
        Ref_Embedding:
          - "GUIDE-SFD-STS-MASTER-01 FORM-PRESUPUESTO-ANEXO5-V1."
