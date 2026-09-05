---
urn: urn:gn:kb:gn-guia-programas-directos-gore
nombre: gn-guia-programas-directos-gore
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Guía de Formulación de Programas Públicos Regionales (PPR) de Ejecución Directa GORE (Vía Glosa 06); migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_025_guia_programas_koda.yml (sha256:b913429daf080084fbf48ac709e6fb860ee22162518954980325668826ac21c9); URN KODA legado urn:gorenuble:gn:guia-programas-directos-gore:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "guia"]
familia: bok
---
# Artefacto KODA/Spec – Guía de Formulación de Programas Públicos Regionales (PPR) de Ejecución Directa GORE (Vía Glosa 06)
# Fuente principal: kb_gn_025_guia_programas_sts.md
---
_manifest:
  urn: "urn:gorenuble:gn:guia-programas-directos-gore:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/kb_gn_025_guia_programas_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:transferencia-ppr:1.0.0"
        reason: "Distinción entre PPR de ejecución directa y PPR transferidos a entidades públicas"
  provenance:
    created_by: "FS"
    created_at: "2025-11-28"
    last_modified_at: "2025-11-28"
    signature: null

ID: GN-GUIA-PPR-GORE-DIRECTO-2025-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Guía metodológica y operativa para la formulación, evaluación ex ante y diseño
  de Programas Públicos Regionales (PPR) de ejecución directa del Gobierno
  Regional (GORE), sujetos a evaluación de DIPRES y SES vía Glosa 06.

Source:
  Primary-Source: "kb_gn_025_guia_programas_sts.md"
  Ctx_Required:
    - "Glosa 06 de la Ley de Presupuestos vigente (Inversión Regional)."
    - "Normativa y oficios circulares DIPRES sobre evaluación de programas GORE."
    - "Normativa SES/MDSF sobre evaluación ex ante de programas."
    - "Formularios oficiales de Perfil y Diseño de Programas Públicos GORE."
  Ctx_Optional:
    - "Banco Integrado de Programas Sociales (BIPS)."
    - "Estrategia Regional de Desarrollo (ERD) y planes regionales vigentes."

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-GUIA-PPR-GORE-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure:
    headers, IDs, lists, tables) with zero loss. Ignore fat (filler words,
    retórica, redundancias).

    LEXICON (expand before processing):
      Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dest->Destination, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
      Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
      Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
      Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
      Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY:
      - Ref: is internal only—must point to an existing ID defined within
        THIS document.
      - External documents (leyes, oficios, glosas, formularios, guías
        complementarias, sitios web) se mencionan bajo Ctx:, Src:,
        Ctx_Required: o Ctx_Optional:, nunca bajo Ref:.

    LANGUAGE POLICY:
      - Keywords in English (and abbreviated forms as listed).
      - Content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Glosario_PPR:
  ID: GN-PPR-GLOSARIO-01
  Purp: "Definir conceptos, siglas y normas clave recurrentes en la guía de PPR de ejecución directa del GORE."
  Terminos:
    - ID: GN-PPR-GLOS-PPR
      Sigla: "PPR"
      Cpt: "Programa Público Regional"
      Def: "Conjunto integrado y articulado de acciones, prestaciones y beneficios destinados a un propósito específico en una población objetivo, para resolver un problema o necesidad."
    - ID: GN-PPR-GLOS-FNDR
      Sigla: "FNDR"
      Cpt: "Fondo Nacional de Desarrollo Regional"
      Def: "Principal fuente de financiamiento de proyectos y programas regionales administrada por los Gobiernos Regionales."
    - ID: GN-PPR-GLOS-GORE
      Sigla: "GORE"
      Cpt: "Gobierno Regional"
      Def: "Administración superior de la región, con personalidad jurídica y patrimonio propio, responsable de la inversión y programas regionales."
    - ID: GN-PPR-GLOS-DAE
      Sigla: "DAE"
      Cpt: "Departamento de Análisis y Evaluación"
      Def: "Unidad del GORE responsable de la evaluación técnica de programas y proyectos."
    - ID: GN-PPR-GLOS-DIPIR
      Sigla: "DIPIR"
      Cpt: "División de Presupuesto e Inversión Regional"
      Def: "División encargada del presupuesto de inversión y de la oferta programática regional."
    - ID: GN-PPR-GLOS-DIPRES
      Sigla: "DIPRES"
      Cpt: "Dirección de Presupuestos"
      Def: "Órgano técnico del Ministerio de Hacienda a cargo de la formulación, ejecución y control del Presupuesto del Sector Público."
    - ID: GN-PPR-GLOS-SES
      Sigla: "SES"
      Cpt: "Subsecretaría de Evaluación Social"
      Def: "Unidad del Ministerio de Desarrollo Social y Familia responsable de la evaluación ex ante de programas sociales y de la metodología de Marco Lógico."
    - ID: GN-PPR-GLOS-ERD
      Sigla: "ERD"
      Cpt: "Estrategia Regional de Desarrollo"
      Def: "Instrumento estratégico que orienta las prioridades de desarrollo regional y con el que deben alinearse los PPR."
    - ID: GN-PPR-GLOS-FRPD
      Sigla: "FRPD"
      Cpt: "Fondo Regional para la Productividad y el Desarrollo"
      Def: "Fondo asociado al Royalty Minero destinado a financiar iniciativas de innovación, competitividad, ciencia, tecnología e infraestructura habilitante."
    - ID: GN-PPR-GLOS-RSH
      Sigla: "RSH"
      Cpt: "Registro Social de Hogares"
      Def: "Principal instrumento de caracterización socioeconómica de hogares en Chile."
    - ID: GN-PPR-GLOS-BPC
      Sigla: "BPC"
      Cpt: "Base de Personas Cuidadoras"
      Def: "Módulo complementario del Registro Social de Hogares que identifica a personas cuidadoras y a quienes requieren cuidados."
    - ID: GN-PPR-GLOS-SIVUST
      Sigla: "SIVUST"
      Cpt: "Sistema de Indicadores de Vulnerabilidad Socioterritorial"
      Def: "Sistema que mide vulnerabilidad socioterritorial mediante un índice global y otros indicadores a nivel territorial."
    - ID: GN-PPR-GLOS-BIPS
      Sigla: "BIPS"
      Cpt: "Banco Integrado de Programas Sociales"
      Def: "Plataforma del Ministerio de Desarrollo Social y Familia para consultar la oferta programática evaluada y sus principales características."

Guia_PPR_Ejecucion_Directa_GORE:
  ID: GN-GUIA-PPR-GORE-DIRECTO-2025-01
  Titulo: "Guía de Formulación de Programas Públicos Regionales (PPR) de Ejecución Directa del GORE vía Glosa 06"
  Purp: |
    Orientar a los equipos del Gobierno Regional en el diseño, formulación y
    evaluación ex ante de Programas Públicos Regionales (PPR) de ejecución
    directa, asegurando cumplimiento normativo, calidad metodológica y
    pertinencia territorial, de acuerdo con Glosa 06 y lineamientos DIPRES/SES.
  Destinatarios:
    - "Profesionales y equipos del GORE que formulan y gestionan PPR de ejecución directa."
    - "Unidades técnicas sectoriales del GORE (DIPIR, divisiones de fomento, social, etc.)."
    - "Autoridades regionales que deciden sobre priorización programática."
  Alcance:
    - "Aplica exclusivamente a programas de ejecución directa GORE financiados con FNDR (Subt. 24) vía Glosa 06."
    - "No aplica a proyectos de inversión (SNI) ni a PPR transferidos a entidades públicas u organizaciones privadas (ver guía específica de transferencias PPR)."
  Objetivos_Especificos:
    - "Definir el marco conceptual y normativo de los PPR GORE de ejecución directa."
    - "Explicar el proceso de evaluación ex ante bifásico (Perfil y Diseño) conducido por DIPRES/SES."
    - "Guiar el uso de la Metodología de Marco Lógico (MML) para formular PPR."
    - "Orientar el llenado de los formularios oficiales de Perfil y Diseño."
    - "Proveer checklists de autoevaluación y herramientas de apoyo (Sistemas de Información Social, catálogos de beneficios, etc.)."
  Ref:
    - GN-PPR-GLOS-PPR
    - GN-PPR-GLOS-GORE
  Estructura_Secciones:
    - ID: GN-PPR-SEC-1-MARCO
      Cpt: "Marco conceptual, ciclo de vida y rol estratégico de los PPR GORE."
    - ID: GN-PPR-SEC-2-EVAL-EXANTE
      Cpt: "Proceso bifásico de evaluación ex ante vía Glosa 06."
    - ID: GN-PPR-SEC-3-MML
      Cpt: "Metodología de Marco Lógico aplicada a PPR (diagnóstico, lógica de intervención, monitoreo y presupuesto)."
    - ID: GN-PPR-SEC-4-FORMULARIOS
      Cpt: "Guía de llenado de Formularios de Perfil y Diseño de PPR GORE."
    - ID: GN-PPR-SEC-5-CHECKLISTS
      Cpt: "Checklists de calidad, uso de sistemas de información social y recursos complementarios."

  Nodos_Centrales:
    ID: GN-PPR-NODOS-CENTRALES-01
    Reglas_Sobre_Uso_Instrumentos_Oficiales:
      ID: GN-PPR-REG-INSTR-OFICIALES-01
      Def: "Reglas generales sobre uso obligatorio de instrumentos oficiales específicos para PPR GORE y prohibición de usar instrumentos del sistema central cuando no corresponda."
      Req:
        - "Utilizar siempre los formularios oficiales vigentes de Perfil y Diseño para PPR GORE."
        - "Aplicar metodologías, checklists y plantillas emitidas por SES y DIPRES para programas del GORE."
      Prohib:
        - "Usar Ficha IDI, RIS y formularios del Sistema Nacional de Inversiones para PPR de ejecución directa."
        - "Mezclar versiones desactualizadas de instrumentos con versiones vigentes sin justificación."
    Importancia_Diagnostico:
      ID: GN-PPR-IMPORT-DIAG-01
      Def: "Principio que establece que un diagnóstico robusto y basado en evidencia es la base del diseño de todo PPR."
      Req:
        - "Invertir tiempo significativo en caracterizar problema, población, oferta y brechas."
        - "Respaldar el diagnóstico con evidencia cuantitativa y cualitativa actualizada y trazable."
      Warn:
        - "Un diagnóstico débil puede invalidar la propuesta, aunque el problema sea real."
    Alineacion_con_ERD_y_Plan_Regional:
      ID: GN-PPR-ALINE-ERD-PLAN-01
      Def: "Regla de alineamiento estratégico obligatorio entre los PPR de ejecución directa, la ERD y los principales planes regionales."
      Req:
        - "Citar explícitamente los ejes, lineamientos y objetivos de la ERD y planes regionales que justifican el programa."
        - "Verificar coherencia entre objetivos del programa y prioridades estratégicas regionales vigentes."
      Warn:
        - "Una baja alineación con la ERD y los planes regionales reduce la atingencia del programa y la probabilidad de obtener RF."

  Sec_1_Marco_Conceptual_y_Rol_Estrategico:
    ID: GN-PPR-SEC-1-MARCO

    Definicion_PPR:
      ID: GN-PPR-DEF-01
      Cpt: "Programa Público Regional (PPR) de Ejecución Directa."
      Def: |
        Conjunto integrado y articulado de acciones, prestaciones y beneficios
        (componentes) orientados a un propósito específico sobre una población
        objetivo regional, ejecutados directamente por el GORE a través de
        gasto corriente o mixto.
      Purp:
        - "Resolver un problema público definido o atender una necesidad específica de la población objetivo."
      Caracteristicas_Claves:
        - "Enfoque en servicios, cambios de comportamiento o capacidades; no en creación de activos físicos durables como objetivo principal."
        - "Financiamiento típico en Subtítulo 24 (Transferencias Corrientes) u otros subtítulos corrientes/mix."
        - "Duración definida; no confundir con funciones permanentes del GORE."
      Distincion_vs_Proyectos_Inversion:
        ID: GN-PPR-DEF-DIF-IDI-01
        Cpt: "Diferencia principal entre PPR y proyectos de inversión (IDI)."
        Def: |
          Los PPR se centran en la provisión de servicios y beneficios a
          personas, hogares u organizaciones, mientras que los proyectos de
          inversión (IDI) del SNI se enfocan en infraestructura, equipamiento
          y otros activos físicos.
        Warn:
          - "No utilizar formularios, metodologías ni RIS del Sistema Nacional de Inversiones para PPR."
          - "Confundir PPR con proyectos de inversión conlleva rechazo o derivación de la iniciativa."

    Ciclo_Vida_PPR:
      ID: GN-PPR-CICLO-VIDA-01
      Cpt: "Fases principales de un PPR GORE."
      Fases:
        - ID: GN-PPR-CICLO-1-DISENO-FORM
          Cpt: "Fase 1 – Diseño y Formulación."
          Ctx: "Foco principal de la guía."
          SubEtapas:
            - ID: GN-PPR-DISENO-ETAPA-1-DIAG
              Cpt: "Sub-etapa 1: Identificación y diagnóstico."
              Act:
                - "Detectar y analizar el problema público (causas, efectos, población afectada)."
            - ID: GN-PPR-DISENO-ETAPA-2-FORM
              Cpt: "Sub-etapa 2: Formulación."
              Act:
                - "Definir propósito, componentes, actividades, indicadores, población objetivo, estrategia y presupuesto."
                - "Aplicar Metodología de Marco Lógico (MML) como requisito metodológico."
            - ID: GN-PPR-DISENO-ETAPA-3-EVAL-EXANTE
              Cpt: "Sub-etapa 3: Evaluación ex ante del diseño."
              Act:
                - "Someter el diseño a revisión técnica de DIPRES y/o SES."
              Resp:
                - "DIPRES y Subsecretaría de Evaluación Social (SES)."
        - ID: GN-PPR-CICLO-2-EJECUCION
          Cpt: "Fase 2 – Ejecución e implementación."
          Act:
            - "Puesta en marcha del programa y operación regular."
            - "Gestión de recursos, ejecución de actividades y monitoreo continuo."
        - ID: GN-PPR-CICLO-3-EVAL-RETRO
          Cpt: "Fase 3 – Evaluación y retroalimentación."
          Act:
            - "Medición de resultados e impactos (evaluación ex post)."
            - "Rendición de cuentas y aprendizaje para mejora continua."

    Rol_Estrategico_PPR_GORE:
      ID: GN-PPR-ROL-ESTRATEGICO-01
      Purp: "Ubicar a los PPR como herramienta estratégica del GORE."
      Funciones_Claves:
        - ID: GN-PPR-ROL-RESPUESTA-PERT-01
          Cpt: "Respuesta pertinente al territorio."
          Def: "Permitir soluciones ajustadas a necesidades y características específicas de la región (ej. Ñuble)."
        - ID: GN-PPR-ROL-FOMENTO-ENDOGENO-01
          Cpt: "Fomento endógeno."
          Def: "Desarrollar capacidades locales, innovación y diversificación económica o social."
        - ID: GN-PPR-ROL-BRECHAS-01
          Cpt: "Reducción de brechas y equidad."
          Def: "Focalizar en grupos vulnerables y territorios rezagados para disminuir brechas."
        - ID: GN-PPR-ROL-ARTICULACION-01
          Cpt: "Articulación de actores."
          Def: "Movilizar y coordinar sector público, privado y sociedad civil."
        - ID: GN-PPR-ROL-AUTONOMIA-RESP-01
          Cpt: "Ejercicio de autonomía responsable."
          Def: "Usar recursos regionales de forma eficaz para generar valor público."

    Marco_Normativo_Claves:
      ID: GN-PPR-MARCO-NORM-01
      Purp: "Identificar las normas que habilitan y regulan los PPR GORE de ejecución directa."
      Ref:
        - GN-PPR-GLOS-ERD
        - GN-PPR-GLOS-FNDR
      Componentes:
        - ID: GN-PPR-NORM-LOCGAR-01
          Cpt: "LOCGAR."
          Def: "Habilita a los Gobiernos Regionales para diseñar y ejecutar programas."
          Ctx: "Define competencias y marco de actuación regional."
        - ID: GN-PPR-NORM-GLOSA06-01
          Cpt: "Ley de Presupuestos – Glosa 06."
          Def: "Norma anualmente la vía programática sobre FNDR para programas regionales, estableciendo la obligación de evaluación ex ante."
        - ID: GN-PPR-NORM-LEY20530-01
          Cpt: "Ley N° 20.530 y normativa DIPRES."
          Def: "Regulan rol de SES y DIPRES en evaluación ex ante de programas públicos."
        - ID: GN-PPR-NORM-OFICIOS-DIPRES-01
          Cpt: "Oficios Circulares DIPRES anuales."
          Def: "Detallan procedimientos operativos, formatos, plazos y requisitos para evaluación de programas GORE."

    Principios_Rectores_Formulacion:
      ID: GN-PPR-PRINCIPIOS-01
      Ctx: "Principios de administración pública aplicables a la formulación de PPR."
      Principios:
        - ID: GN-PPR-PRINC-PROBIDAD-01
          Cpt: "Probidad administrativa."
          Act:
            - "Actuar con rectitud y primacía del interés general."
          Req:
            - "Diseñar mecanismos transparentes y objetivos para selección de beneficiarios y uso de fondos."
        - ID: GN-PPR-PRINC-TRANSPARENCIA-01
          Cpt: "Transparencia y publicidad."
          Act:
            - "Asegurar acceso a información clave: objetivos, beneficiarios, presupuesto, resultados."
        - ID: GN-PPR-PRINC-PARTICIPACION-01
          Cpt: "Participación ciudadana."
          Act:
            - "Involucrar a la comunidad y beneficiarios en diagnóstico y diseño."
          Rec:
            - "Utilizar insumos del Consejo de la Sociedad Civil (COSOC) y otros espacios participativos."
        - ID: GN-PPR-PRINC-EFICIENCIA-01
          Cpt: "Eficiencia y eficacia."
          Act:
            - "Buscar la forma óptima de alcanzar objetivos minimizando costos (eficiencia)."
            - "Asegurar el logro de los cambios esperados (eficacia)."
        - ID: GN-PPR-PRINC-EQUIDAD-01
          Cpt: "Equidad e inclusión."
          Act:
            - "Focalizar en grupos vulnerables y territorios rezagados."
          Req:
            - "Promover igualdad de oportunidades y no discriminación (género, discapacidad, etc.)."
        - ID: GN-PPR-PRINC-RESPONSABILIDAD-01
          Cpt: "Responsabilidad."
          Act:
            - "Asumir cumplimiento de objetivos y correcta administración de fondos públicos."
        - ID: GN-PPR-PRINC-COORDINACION-01
          Cpt: "Coordinación."
          Act:
            - "Articular el programa con otros órganos del Estado y programas existentes para evitar duplicidades y potenciar sinergias."

  Sec_2_Proceso_Evaluacion_ExAnte_Glosa06:
    ID: GN-PPR-SEC-2-EVAL-EXANTE

    Vision_General_Proceso:
      ID: GN-PPR-EVAL-EXANTE-01
      Obj: "Describir el flujo operativo desde la idea de programa hasta su habilitación para financiamiento."
      Cpt:
        - "Proceso bifásico y secuencial con dos filtros obligatorios (Perfil y Diseño)."
        - "Sin aprobación satisfactoria de ambas fases no se puede financiar el programa con cargo a FNDR vía Glosa 06."
      Resp:
        - "Subsecretaría de Evaluación Social (SES)."
        - "Dirección de Presupuestos (DIPRES)."
      Interlocutor_GORE:
        Cpt: "Contraparte única designada por el GORE (idealmente Jefatura de DIPIR o Administración Regional)."
      Ref:
        - GN-PPR-GLOS-SES
        - GN-PPR-GLOS-DIPRES
        - GN-PPR-GLOS-DIPIR

    Fase_1_Perfil_Programa:
      ID: GN-PPR-EVAL-FASE1-PERFIL-01
      Obj: "Presentar una visión concisa y fundamentada de la iniciativa para el primer filtro de pertinencia y factibilidad."
      Instrumento_Clave:
        Cpt: "Formulario de Perfil de Programa Público GORE."
      Actores_y_Flujo:
        - "El formulador completa rigurosamente el Formulario de Perfil."
        - "La contraparte operativa del GORE presenta el Perfil a SES/DIPRES."
      Resultados_Posibles:
        - ID: GN-PPR-PERFIL-APROBADO-01
          Cpt: "Perfil aprobado."
          Def: "La iniciativa corresponde efectivamente a un programa y es pertinente; se solicita formalmente al GORE elaborar el diseño detallado (Fase 2)."
        - ID: GN-PPR-PERFIL-RECHAZADO-01
          Cpt: "Perfil rechazado."
          Def: "La iniciativa no corresponde a programa (ej. es proyecto de inversión) o presenta debilidades conceptuales insalvables; el proceso se detiene hasta subsanar."

    Fase_2_Diseno_Programa:
      ID: GN-PPR-EVAL-FASE2-DISENO-01
      Cond_Previa:
        - "Haber recibido solicitud formal de DIPRES/SES tras aprobación del Perfil."
      Obj: "Desarrollar en profundidad todos los aspectos del programa aplicando Metodología de Marco Lógico (MML)."
      Instrumento_Clave:
        Cpt: "Formulario de Diseño de Programa Público GORE."
      Plazos_Clave:
        - "El GORE debe enviar el Formulario de Diseño en un plazo máximo de 20 días hábiles desde la notificación de la solicitud."
        - "Tras cada retroalimentación, el GORE dispone de 20 días hábiles para corregir y reenviar."
      Proceso_Evaluacion:
        Cpt: "Iterativo, con observaciones, subsanaciones y reenvíos hasta alcanzar un resultado definitivo."
      Calificaciones_Finales:
        - ID: GN-PPR-CALIF-RF-01
          Cpt: "RF – Recomendado Favorablemente."
          Def: "Cumple requisitos técnicos; única calificación que habilita a solicitar financiamiento."
        - ID: GN-PPR-CALIF-OT-01
          Cpt: "OT – Objetado Técnicamente."
          Def: "Presenta deficiencias importantes en el diseño; no financiable hasta reformulación sustantiva."
        - ID: GN-PPR-CALIF-FI-01
          Cpt: "FI – Falta de Información."
          Def: "Antecedentes insuficientes para emitir juicio; el GORE debe complementar."

    Alcance_y_Excepciones_Evaluacion:
      ID: GN-PPR-ALCANCE-EXCEPCIONES-01
      Regla_General:
        Def: "Un programa debe entrar a evaluación ex ante si cumple simultáneamente todas las condiciones siguientes."
        Cond:
          - "Es un Programa Público (no un proyecto de inversión)."
          - "Es nuevo o corresponde a una reformulación sustantiva."
          - "Se financia con cargo a Subtítulo 24 del presupuesto de inversión regional (FNDR)."
          - "La responsabilidad principal de implementación recae en el GORE (ejecución directa)."
          - "Se enmarca en facultades del GORE (LOCGAR o habilitaciones especiales de Glosa 06)."
      Excepciones_Evaluacion:
        Def: "Casos exentos del proceso bifásico central. Deben revisarse anualmente según Glosa 06 y oficios DIPRES."
        Casos_Tipicos:
          - "Programas en continuidad sin cambios sustantivos."
          - "Subvenciones de concursos 8% FNDR para organizaciones privadas (ver guías específicas)."
          - "Transferencias a otras entidades públicas para que estas ejecuten el programa (responsabilidad y evaluación recaen en el receptor público)."
          - "Ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias según normativa anual."
          - "Programas que ya obtuvieron calificación RF en ciclo anterior y no han sido modificados."

    Criterios_Clave_Evaluacion_DIPRES_SES:
      ID: GN-PPR-CRITERIOS-EVAL-01
      Criterios:
        - ID: GN-PPR-CRIT-ATINGENCIA-01
          Cpt: "Atingencia del programa."
          Pregunta_Clave: "¿Es el programa correcto para el problema y el contexto?"
          SubCriterios:
            - "Vínculo consistente Problema–Diagnóstico–Intervención."
            - "Relación clara con la Estrategia Regional de Desarrollo (ERD) y otras políticas relevantes."
            - "Definición correcta de la población objetivo."
            - "No duplicidad con programas existentes."
        - ID: GN-PPR-CRIT-COHERENCIA-01
          Cpt: "Coherencia interna del diseño."
          Pregunta_Clave: "¿La lógica del programa es sólida y está bien articulada?"
          SubCriterios:
            - "Coherencia de la cadena causal MML (Problema -> Propósito -> Componentes)."
            - "Estrategia y modelo de gestión claros."
            - "Incorporación de enfoques transversales pertinentes."
        - ID: GN-PPR-CRIT-CONSISTENCIA-01
          Cpt: "Consistencia del diseño."
          Pregunta_Clave: "¿La propuesta es operativamente viable y monitoreable?"
          SubCriterios:
            - "Indicadores de desempeño SMART y suficientes."
            - "Sistemas de información adecuados."
            - "Presupuesto coherente y suficiente con las metas."

  Sec_3_Metodologia_Marco_Logico_PPR:
    ID: GN-PPR-SEC-3-MML

    Fase_Diagnostico:
      ID: GN-PPR-MML-DIAGNOSTICO-01
      Obj: "Fundamentar la necesidad, pertinencia y alcance del programa."
      Ref:
        - GN-PPR-IMPORT-DIAG-01
        - GN-PPR-ALINE-ERD-PLAN-01

      Definicion_Problema_Publico:
        ID: GN-PPR-PROBLEMA-PUBLICO-01
        Def: |
          Situación negativa, concreta y verificable que afecta a una población
          regional definida y cuya solución corresponde al interés colectivo y
          al ámbito de competencias del GORE.
        Cond:
          - "La solución es de interés colectivo y corresponde a competencias GORE."
          - "El problema no puede ser resuelto solo por los afectados."
        Criterios_Buena_Definicion:
          - "Concreto y específico; evitar generalidades y problemas múltiples en una sola frase."
          - "Formulado como situación existente, no como falta de un programa o solución."
          - "Población afectada claramente identificada."
          - "Respaldado por evidencia cuantitativa y cualitativa de fuentes confiables (INE, CASEN, RSH, estudios sectoriales)."
          - "Relevancia regional y alineamiento con ERD."
        Ejemplos_Buenos_Malos:
          Ex:
            - "Correcto: 'Bajos niveles de empleabilidad juvenil en la comuna X'."
            - "Incorrecto: 'Falta de programas para jóvenes'."

      Analisis_Causal_Arbol_Problemas:
        ID: GN-PPR-ARBOL-PROBLEMAS-01
        Purp: "Entender por qué ocurre el problema (causas) y qué consecuencias genera (efectos)."
        Conceptos_Claves:
          - "Problema central (tronco)."
          - "Causas directas e indirectas (raíces)."
          - "Efectos directos e indirectos (ramas)."
        Metodologia:
          Proc:
            - "Redactar problema central."
            - "Identificar causas directas preguntando '¿por qué ocurre este problema?'."
            - "Para cada causa directa, identificar causas indirectas."
            - "Identificar efectos directos e indirectos preguntando '¿qué consecuencias genera este problema?'."
        Reglas_Disenyo:
          - "El programa debe focalizarse en causas donde el GORE puede incidir."
          - "Cada causa abordada debe ser atendida por al menos un componente."
          - "Las causas deben estar respaldadas por datos o análisis técnico."

      Poblacion_Potencial_Objetivo_Beneficiaria:
        ID: GN-PPR-POBLACION-01
        Ctx: "Identificar y cuantificar correctamente quiénes experimentan el problema, quiénes serán objetivo del programa y quiénes serán beneficiarios anuales."
        Tipos_Poblacion:
          - ID: GN-PPR-POB-POTENCIAL-01
            Cpt: "Población potencial."
            Def: "Universo total de unidades (personas, hogares, empresas, organizaciones) que experimentan el problema."
            Act:
              - "Caracterizar atributos relevantes (demográficos, socioeconómicos, geográficos)."
              - "Cuantificar con fuentes oficiales y actualizadas."
          - ID: GN-PPR-POB-OBJETIVO-01
            Cpt: "Población objetivo."
            Def: "Subconjunto de la población potencial al que se desea llegar a mediano plazo mediante criterios de focalización."
            Cpt_Criterios_Focalizacion: "Condiciones objetivas y verificables (edad, tramo RSH, comuna, situación de discapacidad, etc.)."
          - ID: GN-PPR-POB-BENEF-ANUAL-01
            Cpt: "Población beneficiaria anual."
            Def: "Subconjunto de la población objetivo que el programa espera atender efectivamente en un año, según cupos y capacidad operativa."
        Errores_Comunes:
          - "Definir población objetivo que no es subconjunto de la población potencial."
          - "No cuantificar con fuentes o hacerlo con fuentes no confiables."
          - "Confundir criterios de focalización con mera descripción general."

      Justificacion_Intervencion_Regional:
        ID: GN-PPR-JUST-INTERV-01
        Purp: "Argumentar por qué el GORE debe implementar el programa y cómo aporta valor agregado."
        Componentes:
          - "Atingencia con ERD y prioridades regionales."
          - "Pertinencia regional: valor agregado del GORE (cubre brechas, adapta a especificidades territoriales, pilota innovación)."
          - "Análisis de oferta y no duplicidad: mapeo de programas existentes (nacionales, GORE, municipales) para evitar superposición."
          - "Vinculación con competencias GORE (LOCGAR, habilitaciones especiales de Glosa 06)."

    Fase_Diseno_Logica_Intervencion:
      ID: GN-PPR-MML-DISENO-01

      Proposito_Programa:
        ID: GN-PPR-PROPOSITO-01
        Def: "Cambio específico esperado en la población objetivo que constituye el núcleo del programa."
        Regla_Formulacion: "Debe ser la reversión positiva del problema central."
        Estructura_Rec: "[Población objetivo] + [Verbo de cambio] + [Variable a cambiar]."
        Criterios:
          - "Único por programa."
          - "Orientado a la población objetivo (no a actividades internas del GORE)."
          - "Realista y alcanzable con los recursos disponibles."
          - "Medible mediante indicadores adecuados."
        Errores_Comunes:
          - "Confundir el propósito con fines superiores o con componentes/actividades."
          - "Formular un propósito múltiple, vago o sin población identificada."

      Diseno_Componentes:
        ID: GN-PPR-COMPONENTES-01
        Def: "Productos (bienes) o resultados directos (servicios) entregados a la población objetivo para alcanzar el propósito."
        Regla_Vinculacion: "Cada componente debe abordar al menos una causa directa relevante del problema."
        Caracteristicas:
          - "Tangibles y claramente definibles."
          - "Necesarios y en conjunto suficientes para lograr el propósito."
          - "Orientados a beneficiarios finales o intermedios relevantes."
        Distincion_Importante:
          - "Componentes son bienes/servicios entregados a beneficiarios."
          - "Actividades de gestión interna del GORE (estudios, sistemas, contratación de personal) forman parte de la estrategia y presupuesto, pero no son componentes por sí mismos."
        Req_Definicion_Por_Componente:
          - "Nombre del componente."
          - "Tipo de beneficio y beneficio específico según catálogos oficiales."
          - "Causa del problema que atiende."
          - "Descripción detallada del bien/servicio."
          - "Población destinataria."
          - "Forma de producción/entrega."
          - "Unidad de medida y producción estimada."
          - "Gasto asociado por componente."

      Estrategia_Intervencion_y_Modelo_Gestion:
        ID: GN-PPR-ESTRATEGIA-01
        Def: "Combinación de componentes y definiciones operativas que explican cómo se logrará el propósito."
        Preguntas_Guia:
          - "¿Qué hace el programa?"
          - "¿Cómo lo hace (modalidades y secuencia)?"
          - "¿Con quién se implementa (colaboraciones)?"
          - "¿Quién ejecuta y con qué responsabilidades?"
        Elementos_Claves:
          - "Articulación y secuencia de componentes (simultáneos, consecutivos, por cohortes)."
          - "Flujo del beneficiario (ingreso, ruta de atención, egreso)."
          - "Modalidad de ejecución principal: ejecución directa GORE (obligatoria para aplicación de Glosa 06)."
          - "Opciones de colaboración y complementariedad con otras instituciones sin trasladar responsabilidad principal de ejecución."
        Ctx_Transferencias:
          Cpt: "Cuando la ejecución se transfiere a otra entidad pública, el régimen normativo y de evaluación cambia; se rige por la guía de transferencias PPR."

      Supuestos_y_Riesgos:
        ID: GN-PPR-SUP-RIESGOS-01
        Supuestos_Criticos:
          Def: "Condiciones externas necesarias para que la cadena Actividades -> Componentes -> Propósito -> Fin funcione adecuadamente."
        Analisis_Riesgos:
          Def: "Identificación de eventos inciertos con impacto negativo (externos, de gestión, de participación), priorizando los más críticos."
        Estrategias_Mitigacion:
          Cpt: "Medidas preventivas o correctivas para riesgos prioritarios, integradas en el diseño y en el modelo de gestión."

    Fase_Monitoreo_Indicadores_y_Presupuesto:
      ID: GN-PPR-MML-MONITOREO-01

      Indicadores_Desempeno:
        ID: GN-PPR-INDICADORES-01
        Def: "Herramientas para medir objetivamente cambios y desempeño del programa."
        Req_SMART:
          Def: "Indicadores Específicos, Medibles, Alcanzables, Relevantes y Acotados en el tiempo."
        Dimensiones:
          - "Eficacia (grado de cumplimiento de objetivos)."
          - "Eficiencia (relación productos/recursos)."
          - "Economía (capacidad de administrar recursos financieros)."
          - "Calidad (atributos de bienes/servicios para satisfacer necesidades)."
        Tipos:
          - ID: GN-PPR-IND-PROPOSITO-01
            Cpt: "Indicadores de propósito (resultado)."
          - ID: GN-PPR-IND-COMPONENTE-01
            Cpt: "Indicadores de componente (producto/proceso)."
        Req_Definicion:
          - "Nombre claro del indicador."
          - "Fórmula y descripción de variables."
          - "Unidad de medida y sentido (ascendente/descendente)."
          - "Medios de verificación y fuentes."
          - "Línea base y metas cuantificables."

      Fuentes_y_Medios_Verificacion:
        ID: GN-PPR-FUENTES-MDV-01
        Req:
          - "Definir para cada indicador cómo se obtendrán los datos."
        Medios_Verificacion:
          - "Listas de asistencia, registros de sistemas, encuestas, evaluaciones."
        Fuentes_Informacion:
          - "Primarias: datos recolectados por el propio programa."
          - "Secundarias: registros administrativos (RSH, bases sectoriales), estadísticas oficiales."

      Linea_Base_y_Metas:
        ID: GN-PPR-LINEA-METAS-01
        Def_Linea_Base: "Valor del indicador antes de la intervención."
        Def_Metas: "Valores esperados del indicador en puntos específicos del tiempo, coherentes y fundamentados."
        Rec:
          - "Fundamentar metas en comportamiento histórico, benchmarks y resultados de programas similares."

      Sistemas_Informacion:
        ID: GN-PPR-SISTEMAS-INFO-01
        Req:
          - "Todo programa debe contar con un sistema de registro y monitoreo proporcional a su escala."
        Funcionalidades_Claves:
          - "Registro de beneficiarios y seguimiento de atenciones/beneficios."
          - "Cálculo y seguimiento de indicadores."
          - "Reportes para gestión interna y rendición de cuentas."
        Tipos:
          - "Desde planillas electrónicas estructuradas hasta software especializado."
        Req_Legal:
          - "Cumplir Ley N°19.628 de Protección de Datos Personales y normativa asociada."

      Presupuesto_Detallado:
        ID: GN-PPR-PRESUPUESTO-01
        Principios:
          - "Integralidad, coherencia, eficiencia y transparencia."
        Fuentes_Financiamiento:
          - "FNDR (Subt. 24, Glosa 06)."
          - "FRPD (Royalty) y otros fondos regionales cuando corresponda."
        Enfoques_Estimacion_Costos:
          - "Por componentes (costos directos por bien/servicio)."
          - "Por tipo de gasto según Clasificador Presupuestario (Subt. 21, 22, 24, 29, etc.)."
        Rec_Metodologia:
          - "Uso de costos unitarios multiplicados por cantidades (ej. valor hora relator x N° horas)."
          - "Respaldo mediante cotizaciones, precios de Mercado Público o convenios marco."
        Restricciones_Gastos_Administrativos:
          Ctx: "Glosa 06 y oficios DIPRES fijan límites estrictos al gasto administrativo."
          Warn:
            - "El GORE solo puede destinar hasta un porcentaje máximo (p.ej. 5% según normativa vigente) del monto total a gastos administrativos propios de gestión del programa; debe justificarse detalladamente."
        Req_Coherencia:
          - "El presupuesto debe ser realista y suficiente para alcanzar las metas definidas."
        Ref:
          - GN-PPR-GLOS-FNDR
          - GN-PPR-GLOS-FRPD

    Enfoques_Transversales:
      ID: GN-PPR-ENFOQUES-TRANS-01
      Purp: "Asegurar que el programa promueva equidad, respete derechos y responda a brechas específicas."
      Enfoques_Claves:
        - ID: GN-PPR-ENF-GENERO-01
          Cpt: "Perspectiva de género."
          Act:
            - "Realizar diagnóstico diferenciado por sexo/género."
            - "Diseñar acciones afirmativas o transformadoras."
            - "Definir indicadores desagregados."
        - ID: GN-PPR-ENF-DDHH-01
          Cpt: "Enfoque de Derechos Humanos."
          Req:
            - "Considerar particularidades de NNA, personas con discapacidad, pueblos indígenas, migrantes y otros grupos."
        - ID: GN-PPR-ENF-TERRITORIAL-01
          Cpt: "Pertinencia territorial e interculturalidad."
          Act:
            - "Adaptar el programa a contextos urbanos/rurales y a diversidad cultural."
            - "Usar herramientas como SIVUST para identificar territorios prioritarios."

  Sec_4_Guia_Llenado_Formularios_Oficiales:
    ID: GN-PPR-SEC-4-FORMULARIOS

    Formulario_Perfil_Programa_Publico_GORE:
      ID: GN-PPR-FORM-PERFIL-01
      Purp: "Entrega visión concisa y completa de la iniciativa para el filtro de pertinencia (Fase 1)."
      Dest: "Sistema de evaluación ex ante administrado por DIPRES y SES."
      Secciones_Claves:
        - ID: GN-PPR-PERFIL-SEC-I-ANTECEDENTES-01
          Cpt: "Sección I: Antecedentes."
          Campos_Ejemplo:
            - "Nombre de la iniciativa: debe ser breve, claro y representar el propósito (evitar nombres genéricos/extensos)."
            - "Gobierno Regional proponente."
            - "Contraparte operativa: nombre completo, rol y correo institucional."
        - ID: GN-PPR-PERFIL-SEC-II-PERFIL-01
          Cpt: "Sección II: Perfil del Programa."
          Campos_Claves:
            - "Ejecución anterior: identifica si la iniciativa es nueva o de continuidad."
            - "Entidad responsable de ejecución: define si corresponde a ejecución directa GORE o colaboración."
            - "Competencia principal en que se enmarca el programa (LOCGAR o habilitación de Glosa 06)."
            - "Vinculación con FRPD cuando aplica."
            - "Justificación frente a programas similares: valor agregado y no duplicidad."
            - "Definición del problema público que se busca solucionar."
            - "Población afectada directamente y su cuantificación preliminar."
            - "Resultado específico esperado en la población (propósito)."
            - "Bienes y servicios principales (componentes) a entregar."
            - "Idea preliminar de cómo se verificará el logro del cambio (variables, fuentes)."
      Reglas_Estimadas:
        - "Respetar extensiones máximas por campo (palabras/caracteres)."
        - "Redactar problema como situación negativa y concreta, no como ausencia de programa."
        - "Describir brevemente componentes, sin perder claridad sobre su vínculo con el propósito."
      Ref:
        - GN-PPR-REG-INSTR-OFICIALES-01
        - GN-PPR-IMPORT-DIAG-01
        - GN-PPR-ALINE-ERD-PLAN-01

    Formulario_Diseno_Programa_Publico_GORE:
      ID: GN-PPR-FORM-DISENO-01
      Purp: "Documenta en detalle el diseño del programa para evaluación de fondo (Fase 2)."
      Cond_Previa:
        - "Solo se completa cuando el Perfil ha sido aprobado y SES/DIPRES solicitan su envío."
      Secciones_Claves:
        - ID: GN-PPR-DISENO-SEC-I-ANTECEDENTES-01
          Cpt: "Sección I: Antecedentes."
          Cont:
            - "Nombre del programa (usualmente precargado)."
            - "Código del programa asignado por la entidad evaluadora."
        - ID: GN-PPR-DISENO-SEC-II-DIAGNOSTICO-01
          Cpt: "Sección II: Diagnóstico."
          Campos:
            - "Problema que el programa busca resolver (coherente con Perfil)."
            - "Desarrollo del diagnóstico con datos (magnitud, evolución, caracterización)."
            - "Causas principales del problema y respaldo de evidencia."
            - "Listado de fuentes y bibliografía utilizada."
        - ID: GN-PPR-DISENO-SEC-III-PROPOSITO-FOCALIZACION-01
          Cpt: "Sección III: Propósito y Focalización."
          Cont:
            - "Propósito del programa (único, medible y reversión del problema)."
            - "Población potencial, objetivo y beneficiaria: descripción, cuantificación y fuente."
            - "Unidad de medida de la población (personas, hogares, empresas, etc.)."
            - "Metodología para cuantificar población objetivo y beneficiaria."
        - ID: GN-PPR-DISENO-SEC-IV-ESTRATEGIA-01
          Cpt: "Sección IV: Estrategia."
          Campos:
            - "Descripción de la estrategia de intervención y flujo del beneficiario."
            - "Número de componentes y tabla de detalle para cada uno (nombre, tipo de beneficio, descripción, población, forma de entrega, unidad de medida, metas)."
            - "Duración del programa y criterio de egreso."
            - "Reglas sobre reingreso o acceso más de una vez."
        - ID: GN-PPR-DISENO-SEC-V-EJECUTORES-01
          Cpt: "Sección V: Ejecutores y Complementariedades."
          Cont:
            - "Participación de otras instituciones en ejecución (sin traspasar responsabilidad principal)."
            - "Número de instituciones y roles definidos para cada una."
            - "Complementariedad con otros programas (servicio responsable, programa, acciones conjuntas)."
        - ID: GN-PPR-DISENO-SEC-VI-ENFOQUES-01
          Cpt: "Sección VI: Enfoques y Derechos Humanos."
          Campos:
            - "Objetivo principal en igualdad de género, si aplica."
            - "Medidas afirmativas y/o transformadoras para igualdad de género."
            - "Enfoques de Derechos Humanos aplicados (discapacidad, pertinencia territorial, etc.) y acciones concretas."
        - ID: GN-PPR-DISENO-SEC-VII-INDICADORES-01
          Cpt: "Sección VII: Indicadores."
          Cont:
            - "Al menos un indicador de propósito (resultado) pertinente."
            - "Indicadores de componente (producto/proceso)."
            - "Metodología de cálculo, medios de verificación, línea base y metas."
        - ID: GN-PPR-DISENO-SEC-VIII-SISTEMAS-INFO-01
          Cpt: "Sección VIII: Sistemas de Información."
          Cont:
            - "Descripción de sistemas existentes o a desarrollar para registro y seguimiento."
        - ID: GN-PPR-DISENO-SEC-IX-GASTOS-01
          Cpt: "Sección IX: Gastos."
          Cont:
            - "Tabla detallada de gastos por componente e ítems presupuestarios."
            - "Identificación y justificación de gastos administrativos, resguardando el límite normativo."
      Advertencias_Generales:
        Warn:
          - "Indicadores de simple cobertura, planificación o satisfacción usuaria no son suficientes para medir logro del propósito."
          - "Un diseño débil en diagnóstico, indicadores o presupuesto reduce significativamente las probabilidades de obtener RF."
      Ref:
        - GN-PPR-REG-INSTR-OFICIALES-01
        - GN-PPR-IMPORT-DIAG-01
        - GN-PPR-ALINE-ERD-PLAN-01

  Sec_5_Checklists_Herramientas_y_Recursos:
    ID: GN-PPR-SEC-5-CHECKLISTS

    Checklists_Evaluacion:
      ID: GN-PPR-CHECKLISTS-01
      Purp: "Permitir autoevaluar la calidad del Perfil y del Diseño antes de su envío oficial."
      Checklist_Perfil:
        ID: GN-PPR-CHECKLIST-PERFIL-01
        Criterios:
          - "Nombre de la iniciativa claro y representativo."
          - "Contraparte única designada con datos de contacto."
          - "Correcta identificación de si es iniciativa nueva o de continuidad."
          - "Modalidad de ejecución definida y coherente con Glosa 06 (ejecución directa GORE)."
          - "Competencia principal correctamente seleccionada."
          - "Uso o no de FRPD claramente indicado."
          - "Justificación de valor agregado y no duplicidad."
          - "Problema definido como situación negativa, concreta y con población afectada."
          - "Población descrita y cuantificada preliminarmente."
          - "Resultado esperado como reversión positiva del problema, medible."
          - "Componentes coherentes con problema y resultado."
          - "Idea plausible de cómo se medirá el éxito."
      Checklist_Diseno:
        ID: GN-PPR-CHECKLIST-DISENO-01
        Dimensiones:
          - Cpt: "Problema público central."
            Criterios:
              - "Definido como situación negativa, concreta y verificable."
              - "Específico y no múltiple."
              - "No formulado como ausencia de solución."
              - "Población afectada clara y respaldada por evidencia reciente."
          - Cpt: "Análisis causal y de efectos."
            Criterios:
              - "Causas directas/indirectas relevantes e incidibles por el programa."
              - "Efectos principales identificados."
          - Cpt: "Población y justificación."
            Criterios:
              - "Población potencial/objetivo/beneficiaria bien definidas y cuantificadas con fuentes."
              - "Análisis de oferta existente y valor agregado del GORE."
          - Cpt: "Propósito y componentes."
            Criterios:
              - "Propósito es reversión del problema, único, claro y medible."
              - "Componentes son bienes/servicios principales y no tareas internas."
              - "Cada componente vinculado a una causa relevante."
          - Cpt: "Estrategia, enfoques y riesgos."
            Criterios:
              - "Estrategia de intervención y flujo del beneficiario descritos."
              - "Enfoques transversales incorporados con medidas concretas."
              - "Supuestos y riesgos críticos identificados con estrategias de mitigación."
          - Cpt: "Indicadores, sistemas y presupuesto."
            Criterios:
              - "Indicadores de propósito y componente de calidad (SMART)."
              - "Medios de verificación y fuentes definidos."
              - "Línea base y metas justificadas."
              - "Sistema de información planificado."
              - "Presupuesto completo, coherente y compatible con límites normativos (incluyendo tope a gastos administrativos)."
      Ref:
        - GN-PPR-IMPORT-DIAG-01
        - GN-PPR-ALINE-ERD-PLAN-01

    Sistemas_Informacion_Social:
      ID: GN-PPR-SISTEMAS-SOCIALES-01
      Ctx: "Herramientas clave provistas por MDSF para diagnóstico y focalización de PPR."
      Herramientas:
        - ID: GN-PPR-RSH-01
          Cpt: "Registro Social de Hogares (RSH)."
          Def: "Principal instrumento de caracterización socioeconómica de hogares en Chile."
          Utilidad_PPR:
            - "Cuantificación y caracterización de población potencial y objetivo."
            - "Focalización mediante la Calificación Socioeconómica y otros módulos."
          Ctx:
            - "GOREs pueden solicitar acceso a datos vía SES y Repositorio de Información Social (RIS)."
          Ref:
            - GN-PPR-GLOS-RSH
        - ID: GN-PPR-BPC-01
          Cpt: "Base de Personas Cuidadoras (BPC)."
          Purp: "Identificar y focalizar programas relacionados con cuidados y dependencia."
          Ref:
            - GN-PPR-GLOS-BPC
        - ID: GN-PPR-SIVUST-01
          Cpt: "Sistema de Indicadores de Vulnerabilidad Socioterritorial (SIVUST)."
          Def: "Sistema que mide vulnerabilidad socioterritorial mediante un índice global y otros indicadores a nivel territorial."
          Utilidad_PPR:
            - "Diagnóstico territorial."
            - "Focalización territorial de programas y justificación de pertinencia regional."
          Ref:
            - GN-PPR-GLOS-SIVUST
        - ID: GN-PPR-OTROS-RECURSOS-MDSF-01
          Cpt: "Otros recursos MDSF."
          Ctx:
            - "Banco Integrado de Datos (BIDAT)."
            - "Analista Digital de Información Social (ADIS)."
            - "Observatorio Social (CASEN, otros estudios)."

    Catalogo_Beneficios_y_Unidades_Medida:
      ID: GN-PPR-CATALOGO-BENEF-01
      Purp: "Apoyar la clasificación de componentes según catálogos estandarizados DIPRES/SES."
      Categorias_Ejemplo:
        - "Apoyo psicosocial (unidades: N° sesiones, N° personas atendidas)."
        - "Monetario – bonos, subsidios, becas (N° beneficios, monto transferido)."
        - "Capacitaciones/cursos (N° personas certificadas, N° cursos ejecutados)."
        - "Servicios generales – alimentación, transporte, residencial (N° raciones, cupos)."
        - "Financiamiento de proyectos – fomento productivo, capital semilla (N° proyectos, monto)."
        - "Asesorías técnicas (N° personas/empresas asesoradas, horas de asistencia)."
        - "Materiales y campañas (material distribuido, alcance)."

    Directorio_Contactos_y_Enlaces:
      ID: GN-PPR-DIRECTORIO-01
      Cpt_Contactos:
        - "DIPRES – www.dipres.gob.cl (metodologías, informes de evaluación, circulares)."
        - "SES/MDSF – www.desarrollosocialyfamilia.gob.cl (metodologías MML, evaluación de programas)."
        - "Correo evaluación ex ante GORE – evaluacionexantegore@desarrollosocial.gob.cl."
        - "Correo asistencia técnica – asistenciatecnicadps@desarrollosocial.gob.cl."
        - "BIPS – https://bips.ministeriodesarrollosocial.gob.cl (oferta programática y evaluaciones)."
        - "CGR – www.contraloria.cl (rendición de cuentas, dictámenes, SISREC)."
        - "SUBDERE – www.subdere.gov.cl (programas de financiamiento regional)."
        - "BCN/Ley Chile – www.bcn.cl/leychile (normativa actualizada)."
      Ref:
        - GN-PPR-GLOS-BIPS

    Recomendaciones_Formulacion_Exitosa:
      ID: GN-PPR-RECOMENDACIONES-01
      Estrategia_Formulacion:
        - "Invertir tiempo significativo en un diagnóstico robusto, con evidencia suficiente."
        - "Utilizar siempre los instrumentos oficiales específicos para PPR GORE (Perfil y Diseño) y versiones vigentes."
        - "Coordinar tempranamente con SES/DIPRES para resolver dudas metodológicas."
        - "Usar checklists antes de enviar los formularios para minimizar observaciones."
        - "Alinear el programa con la ERD y planes sectoriales regionales para fortalecer atingencia."
      Advertencias:
        - "Un diagnóstico débil o sin evidencia invalida la propuesta, incluso si el problema es real."
        - "El uso incorrecto de instrumentos del sistema central (no adaptados a GORE) puede llevar al rechazo."
        - "Subestimar el tiempo requerido para ajustar observaciones retrasa la obtención de RF y el acceso a financiamiento."
      Ref:
        - GN-PPR-IMPORT-DIAG-01
        - GN-PPR-REG-INSTR-OFICIALES-01
        - GN-PPR-ALINE-ERD-PLAN-01
