---
urn: urn:gn:kb:gn-guia-idi-sni-sts
nombre: gn-guia-idi-sni-sts
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – Guía Formulación Iniciativas de Inversión (IDI) en SNI para GOREs; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/ipr/guias_iprs/kb_gn_024_guia_idi_sni_koda.yml (sha256:fdf0d99029aa2bfef65551992311fb867d74ca7819ebd1abfc55e235bb78203f); URN KODA legado urn:gorenuble:gn:guia-idi-sni-sts:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-11-28
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "ipr", "guias-iprs", "guia"]
familia: bok
---
# Artefacto KODA/Spec – Guía Formulación Iniciativas de Inversión (IDI) en SNI para GOREs
# Fuente principal: kb_gn_024_guia_idi_sni_sts.md

_manifest:
  urn: "urn:gorenuble:gn:guia-idi-sni-sts:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file:///Users/felixsanhueza/Developer/gorenuble/knowledge/domains/gn/kb_gn_024_guia_idi_sni_koda.yml"
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

ID: GN-GUIA-IDI-SNI-STS-2025-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: KODA-TRANSFORMER
Creation-Date: 2025-11-28
Modification-Date: 2025-11-28

Ctx: |
  Guía práctica para profesionales del GORE Ñuble que formulan, evalúan y gestionan
  Iniciativas de Inversión (IDI) en el Sistema Nacional de Inversiones (SNI), basada
  en NIP 2025 y en la Metodología General SNI, con foco en el uso de RIS, BIP y
  principios clave como proporcionalidad, separabilidad y evaluación social.

Source:
  Primary-Source: "kb_gn_024_guia_idi_sni_sts.md"
  Ctx_Required:
    - "NIP 2025 – Normas, Instrucciones y Procedimientos del Sistema Nacional de Inversiones"
    - "Metodología General del SNI (MDSF)"
    - "Metodologías sectoriales y complementarias SNI (Gestión de Riesgo de Desastres, Género, etc.)"
    - "RIS genéricas y sectoriales disponibles en https://sni.gob.cl"
    - "Curso SNI (Unidades 1–3, MDSF)"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-GN-GUIA-IDI-SNI-STS-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables)
    with zero loss. Ignore fat (filler words, rhetoric, redundancies).

    LEXICON (expand before processing):
      Act->Action, Cause->Cause, Cond->Condition, Cpt->Concept, Ctx->Context,
      Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
      Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
      Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
      Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
      Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
      Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY:
      - Ref: is internal only—must point to an existing ID defined within THIS document.
      - External documents (leyes, NIP, metodologías, RIS, cursos SNI, informes) se mencionan
        bajo Ctx:, Src:, Ctx_Required: o Ctx_Optional:, nunca bajo Ref:.

    LANGUAGE POLICY:
      - Keywords in English (and abbreviated forms as listed).
      - Content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Guia_IDI_SNI_GOREs:
  ID: GN-GUIA-IDI-SNI-STS-2025-01
  Titulo: "Guía de Formulación de Iniciativas de Inversión (IDI) en el SNI para Gobiernos Regionales"
  Purp: |
    Orientar a los equipos del GORE en la formulación, postulación, evaluación y ejecución
    de Iniciativas de Inversión (IDI) en el marco del Sistema Nacional de Inversiones (SNI),
    asegurando pertinencia, eficiencia, coherencia normativa y uso adecuado de RIS y BIP.
  Destinatarios:
    - "Profesionales y equipos técnicos del GORE encargados de formular y gestionar IDI."
    - "Unidades Técnicas de municipios y servicios públicos que interactúan con el GORE."
  Alcance:
    - "Aplicable a la mayoría de las IDI financiadas total o parcialmente con recursos públicos."
    - "Incluye Estudio Básico, Proyecto (Subt. 31) y Programa de Inversión (Subt. 31)."
    - "Excluye explícitamente instrumentos con procedimientos especiales (FRIL, Circular 33, concursos exentos de SNI), tratados en guías específicas."
  Objetivos_Especificos:
    - "Explicar fundamentos, actores y herramientas clave del SNI para GOREs."
    - "Describir tipos de IDI y su ciclo de vida (preinversión, inversión, operación)."
    - "Guiar la formulación de proyectos bajo principios de problema, proporcionalidad y separabilidad."
    - "Estándarizar el uso del BIP, Carpeta Digital y RIS en la postulación de IDI."
    - "Clarificar el proceso de evaluación ex ante (RATE) y la vigencia de los pronunciamientos."
    - "Resumir modalidades de ejecución y procedimientos especiales relevantes para GOREs."
  Estructura_Secciones:
    - ID: SNI-GORE-SEC-1-FUNDAMENTOS
      Cpt: "Fundamentos del SNI para GOREs (Obj, subsistemas, importancia, herramientas)."
    - ID: SNI-GORE-SEC-2-TIPOS-IDI-CICLO
      Cpt: "Tipos de IDI (Subt. 31) y fases/etapas del ciclo de vida."
    - ID: SNI-GORE-SEC-3-FORMULACION
      Cpt: "Formulación de proyectos: problema, diagnóstico, alternativas, evaluación social."
    - ID: SNI-GORE-SEC-4-EVAL-SOCIAL
      Cpt: "Evaluación social del proyecto: efectos, beneficios, costos, flujos e indicadores."
    - ID: SNI-GORE-SEC-4-BIP-RIS
      Cpt: "Uso del BIP, RIS y Carpeta Digital para postulación y programación."
    - ID: SNI-GORE-SEC-5-EVAL-EXANTE
      Cpt: "Proceso de evaluación ex ante MDSF y resultados RATE."
    - ID: SNI-GORE-SEC-6-EJECUCION
      Cpt: "Ejecución de la inversión y modalidades de transferencia."
    - ID: SNI-GORE-SEC-7-ESPECIALES
      Cpt: "Procedimientos especiales: FRIL, Circular 33, reconstrucción por emergencias."
    - ID: SNI-GORE-SEC-8-SELECCION
      Cpt: "Selección y presentación de la alternativa de solución."

  Conceptos_Clave:
    Principio_Proporcionalidad:
      ID: SNI-PROPORCIONALIDAD-01
      Def: |
        Esfuerzos y profundidad del análisis de evaluación ex ante deben ser proporcionales
        a magnitud, complejidad, riesgos e impactos de la inversión.
      Aplicaciones:
        - "Permite abreviar etapas de preinversión en proyectos simples o de bajo monto."
        - "Habilita requisitos documentales diferenciados en RIS por tipo de proyecto."
        - "Autoriza uso de metodologías simplificadas en proyectos de menor complejidad."
      Niveles_MDSF:
        - "Nivel-0: Exención de evaluación ex ante para proyectos < 5.000 UTM (condiciones específicas)."
        - "Nivel-1: Análisis simplificado para obras de menor complejidad."
        - "Nivel-2: Análisis estándar (por defecto para la mayoría de los proyectos)."
        - "Nivel-3: Análisis enriquecido para proyectos de gran envergadura o alta complejidad."
      Src:
        - "NIP 2025, Sección 2.1 e instructivo de proporcionalidad."
        - "Curso SNI, Unidad 1."

    Situaciones_Sin_Con_Proyecto:
      ID: SNI-SITUACIONES-01
      Def: |
        Marco conceptual para comparar condiciones actuales y futuras con y sin la ejecución del proyecto,
        evitando sobreestimar beneficios y sobredimensionar la inversión.
      Tipos:
        - ID: SNI-SIT-ACTUAL-01
          Cpt: "Situación Actual"
          Def: "Condición presente del territorio y servicio al momento de formular el proyecto."
        - ID: SNI-SIT-BASE-01
          Cpt: "Situación Base"
          Def: "Proyección de la situación actual al inicio de la operación del proyecto, incorporando cambios tendenciales."
        - ID: SNI-SIT-BASE-OPT-01
          Cpt: "Situación Base Optimizada"
          Def: "Resultado de aplicar medidas de optimización de la oferta antes de la inversión."
        - ID: SNI-SIT-SIN-PROY-01
          Cpt: "Situación Sin Proyecto"
          Def: "Escenario de referencia sin intervención de inversión; base para comparar efectos del proyecto."
        - ID: SNI-SIT-CON-PROY-01
          Cpt: "Situación Con Proyecto"
          Def: "Escenario futuro con el proyecto ejecutado y operando, que genera beneficios y costos incrementales."
      Criterios_Simplificacion:
        - "Para proyectos de baja complejidad y rápida ejecución se pueden igualar algunas situaciones, siempre que se justifique explícitamente en el estudio."

    Tipos_Problema_SNI:
      ID: SNI-PROBLEMAS-01
      Clasificacion:
        - ID: SNI-PROBLEMA-COBERTURA-01
          Cpt: "Cobertura Insuficiente"
          Def: |
            Existencia o tamaño/tipo de instalaciones insuficientes para satisfacer la demanda
            del bien/servicio en el territorio analizado.
        - ID: SNI-PROBLEMA-CALIDAD-01
          Cpt: "Calidad Deficiente"
          Def: |
            Servicio provisto con estándares de calidad inferiores a los esperados o normativos,
            ya sea por infraestructura, equipamiento o condiciones operacionales.
      Prohib:
        - "No formular el problema como 'inexistencia de infraestructura específica' para no sesgar las alternativas."
      Ref: SNI-PROBLEMA-PRINCIPAL-01

    Problema_Principal:
      ID: SNI-PROBLEMA-PRINCIPAL-01
      Def: |
        Dificultad para prestar un servicio en cantidad y/o calidad adecuada que afecta a una
        población definida, en un territorio concreto, y que justifica la necesidad de inversión.
      Reglas:
        - "Debe explicitar quiénes se ven afectados y dónde se localizan."
        - "Debe precisarse qué se entiende por calidad o cantidad insuficiente y cómo se mide."
        - "Problemas secundarios solo se abordan si están estrechamente relacionados con el principal."

    Separabilidad_Componentes:
      ID: SNI-SEPARABILIDAD-01
      Purp: "Definir cuándo analizar componentes de un proyecto de forma independiente, unificada o separada."
      Tipos_Analisis:
        - ID: SNI-SEPARABILIDAD-INDEP-01
          Cpt: "Análisis Independiente"
          Def: "Componentes abordan problemas distintos; deben ser proyectos separados."
        - ID: SNI-SEPARABILIDAD-UNIF-01
          Cpt: "Análisis Unificado"
          Def: "Componentes inseparables o interdependientes que resuelven el mismo problema; se evalúan como un solo proyecto."
        - ID: SNI-SEPARABILIDAD-SEP-01
          Cpt: "Análisis Separado"
          Def: |
            Componentes que contribuyen al mismo problema pero son separables; se analizan
            individualmente (ACE/ACB) y luego se evalúa la conveniencia del conjunto.
      Src:
        - "Principio de Separabilidad y análisis de componentes (Anexo 2 de la guía)."

    Evaluacion_Social_y_Privada:
      ID: SNI-EVAL-SOC-PRIV-01
      Evaluacion_Social:
        Def: "Determinación de la conveniencia de la inversión desde la perspectiva del bienestar de la sociedad, utilizando precios sociales."
      Evaluacion_Privada:
        Def: "Análisis de los efectos netos sobre la riqueza de un inversionista, utilizando precios de mercado."
      Relacion_VAN_Social_Privado:
        Def: "Matriz de decisión que cruza la rentabilidad privada (VANp) con la rentabilidad social (VANs)."
        Casos:
          - "VANs > 0 y VANp > 0: el privado ejecuta el proyecto sin intervención del Estado."
          - "VANs > 0 y VANp < 0: el Estado puede subsidiar o ejecutar directamente el proyecto."
          - "VANs < 0 y VANp > 0: el Estado debiera desincentivar el proyecto (impuestos, regulación)."
          - "VANs < 0 y VANp < 0: el proyecto no debiera ejecutarse."
      Src:
        - "Sección Evaluación Social del proyecto: relación entre evaluación privada y social."
      Ref:
        - SNI-EVAL-PRIV-FLUJOS-01

    Indicadores_Economicos:
      ID: SNI-INDIC-ECO-01
      VAN:
        ID: SNI-VAN-01
        Def: |
          Valor presente de los beneficios netos sociales, descontados a la tasa social de descuento,
          menos la inversión inicial.
        Parametros:
          - "I0: Inversión inicial."
          - "BNt: Beneficios netos en el año t."
          - "n: Horizonte de evaluación."
          - "r: Tasa Social de Descuento (valor de referencia 2025: 5,5%)."
        Formula: "VAN = -I0 + Σ_{t=1..n} [BNt / (1+r)^t]"
        Criterio_Decision:
          - "Seleccionar alternativas con VAN social mayor o igual a 0."
          - "Entre alternativas factibles, preferir la de mayor VAN."
        Acciones_Si_VAN_Negativo:
          - "Reformular el proyecto (ajustar diseño, tamaño, fases) para mejorar el VAN."
          - "Evaluar postergación del proyecto (análisis de momento óptimo de inversión)."
        Req_Analisis:
          - "Realizar análisis de sensibilidad y riesgo sobre variables críticas."

      TIR:
        ID: SNI-TIR-01
        Def: "Tasa de descuento que hace que el VAN social sea igual a cero (rentabilidad social intrínseca del proyecto)."
        Relacion_VAN: "Resuelve -I0 + Σ_{t=1..n} [BNt / (1+TIR)^t] = 0."
        Criterio_Decision:
          - "Si TIR ≥ tasa social de descuento: la alternativa es socialmente conveniente."
          - "Si TIR < tasa social de descuento: la alternativa no es conveniente."
        Uso:
          - "Indicador complementario al VAN; no se recomienda para comparar alternativas entre sí."

      VAC:
        ID: SNI-VAC-01
        Def: "Valor presente de los costos totales del proyecto, considerando beneficios adicionales como reducciones de costo."
        Uso:
          - "Comparar alternativas con igual vida útil y beneficios equivalentes en análisis Costo-Eficiencia."
        Formula: "VAC = I0 + Σ_{t=1..n} [(CTt - BAt) / (1+r)^t]"
        Parametros:
          - "CTt: Costos Totales en el año t."
          - "BAt: Beneficios Adicionales valorizables en el año t."
          - "r: Tasa Social de Descuento."
        Criterio_Decision:
          - "Seleccionar la alternativa con menor VAC."

      CAE:
        ID: SNI-CAE-01
        Def: "Costo anual constante equivalente al VAC, usado para comparar alternativas repetibles con distinta vida útil."
        Formula: "CAE = VAC * [r * (1+r)^n] / [(1+r)^n - 1]"
        Parametros:
          - "VAC: Valor Actual de Costos."
          - "r: Tasa Social de Descuento."
          - "n: Horizonte de evaluación."
        Uso:
          - "Comparar alternativas en análisis Costo-Eficiencia."
          - "Construir indicadores del tipo CAE / unidad de beneficio (ej. beneficiario, atención, viaje, etc.)."
        Req:
          - "Calcular sobre flujos incrementales (Situación Con Proyecto - Sin Proyecto), salvo que metodología o RIS indiquen otra cosa."

  Sec_1_Fundamentos_SNI_GOREs:
    ID: SNI-GORE-SEC-1-FUNDAMENTOS
    Fundamentos_SNI:
      ID: SNI-FUNDAMENTOS-01
      Def: "Sistema que norma y rige el proceso de inversión pública en Chile."
      Purp:
        - "Regular el ciclo de vida de la inversión pública para asegurar uso eficiente y eficaz de recursos."
      Func:
        - "Establecer principios, metodologías, requisitos de información, normas, instrucciones y procedimientos."
      Obj:
        - "Contribuir al desarrollo económico y social del país."
        - "Velar por eficacia y eficiencia en el uso de fondos públicos."
        - "Disminuir efectos adversos del cambio climático a través de la inversión."
      Alineacion_Politicas:
        - "Asegurar coherencia con estrategias y políticas de crecimiento y desarrollo nacionales y regionales."
      Aplicacion_GORE:
        - "Marco de referencia obligatorio para la mayoría de las IDI que financian total o parcialmente con fondos públicos."
      Cond_Aplicacion:
        - "IDI financiada total o parcialmente con recursos públicos."
      Src:
        - "NIP 2025, sección 1.1; Metodología General SNI; Curso SNI, Unidad 1."

    Importancia_Critica_GORE:
      ID: SNI-IMPORTANCIA-GORE-01
      Criterios:
        - ID: SNI-CRIT-CALIDAD-PERT-01
          Cpt: "Calidad y pertinencia"
          Def: "Orientar recursos a iniciativas que maximizan bienestar social y responden a necesidades reales."
        - ID: SNI-CRIT-EFICIENCIA-01
          Cpt: "Eficiencia y eficacia"
          Def: "Evitar asignar fondos a proyectos no pertinentes, mal formulados o con baja rentabilidad social."
        - ID: SNI-CRIT-MARCO-COMUN-01
          Cpt: "Marco común y transparencia"
          Def: |
            Proveer lenguaje y reglas comunes para MDSF, DIPRES, GOREs, municipios y servicios,
            facilitando coordinación y transparencia.
        - ID: SNI-CRIT-ACC-FIN-01
          Cpt: "Acceso a financiamiento"
          Def: |
            Contar con RATE favorable (RS o AD) es requisito crítico para acceder a financiamiento
            público en la mayoría de los casos.
        - ID: SNI-CRIT-COHERENCIA-01
          Cpt: "Coherencia con políticas"
          Def: "Alinear inversiones regionales con estrategias y políticas nacionales y regionales."

    Subsistemas_SNI:
      ID: SNI-SUBSISTEMAS-01
      Subsit:
        - ID: SNI-SUBSIST-EXANTE-01
          Cpt: "Evaluación Ex Ante"
          Def: "Análisis previo a la decisión de invertir; foco principal de la guía."
        - ID: SNI-SUBSIST-FORM-PRES-01
          Cpt: "Formulación Presupuestaria"
          Def: "Asignación de recursos en el presupuesto público."
        - ID: SNI-SUBSIST-EJEC-PRES-01
          Cpt: "Ejecución Presupuestaria"
          Def: "Seguimiento y control durante la materialización de la inversión."
        - ID: SNI-SUBSIST-EXPOST-01
          Cpt: "Evaluación Ex Post"
          Def: "Análisis de resultados e impactos una vez finalizada la inversión."

    Actores_Institucionales:
      ID: SNI-ACTORES-01
      Actores:
        - ID: SNI-ACTOR-MDSF-01
          Cpt: "Ministerio de Desarrollo Social y Familia (MDSF)"
          Resp:
            - "Conducir evaluación ex ante de IDI."
            - "Emitir Resultado del Análisis Técnico-Económico (RATE)."
            - "Definir y actualizar metodologías de formulación y evaluación."
            - "Calcular y publicar precios sociales."
            - "Administrar el BIP en materias de evaluación."
        - ID: SNI-ACTOR-DIPRES-01
          Cpt: "Dirección de Presupuestos (DIPRES)"
          Dep: "Ministerio de Hacienda."
          Resp:
            - "Formulación del presupuesto del sector público."
            - "Asignación de recursos y definición de normativas financieras."
            - "Visar modificaciones presupuestarias de GOREs."
            - "Impartir instrucciones para ejecución presupuestaria."
        - ID: SNI-ACTOR-GORE-01
          Cpt: "Gobiernos Regionales (GORE)"
          Ctx: "Actores fundamentales en el ciclo de IDI a nivel regional."
          Proc:
            - "Identificación de necesidades y priorización."
            - "Formulación de IDI y preparación de estudios preinversionales."
            - "Gestión de financiamiento y, en muchos casos, ejecución y operación."
          Resp:
            - "Profesional o equipo técnico del GORE o contratado para estudios y postulación al SNI."
        - ID: SNI-ACTOR-OTROS-01
          Cpt: "Instituciones clave relacionadas"
          Subactores:
            - "Institución Formuladora: Prepara el estudio (GORE, municipio, servicio público)."
            - "Institución Financiera: Postula y financia la IDI (ej. GORE con FNDR)."
            - "Institución Técnica: Licita, contrata y fiscaliza ejecución."
            - "Institución Responsable de Operación: Opera y mantiene el proyecto."

    Herramientas_y_Normativas:
      ID: SNI-HERRAMIENTAS-01
      Herramientas:
        - ID: SNI-NIP-01
          Cpt: "Normas, Instrucciones y Procedimientos (NIP)"
          Def: "Documento rector anual que define reglas, plazos y procedimientos del proceso de inversión pública."
          Req:
            - "Usar siempre la versión vigente disponible en sni.gob.cl."
          Ctx:
            - "NIP 2025 es la base principal de la guía."
        - ID: SNI-METODOLOGIAS-01
          Cpt: "Metodologías de preparación y evaluación"
          Subtipos:
            - "Metodología General: Marco conceptual y pasos comunes del SNI."
            - "Metodologías Sectoriales: Adaptaciones específicas por sector/tipología."
            - "Metodologías Complementarias: Enfoques transversales (GRD, Género, etc.)."
          Warn:
            - "No aplicar metodologías sectoriales o complementarias cuando corresponda es causal de objeción."
        - ID: SNI-RIS-01
          Cpt: "Requisitos de Información Sectorial (RIS)"
          Def: "Documentos que especifican antecedentes mínimos para admisibilidad y evaluación."
          Tipos:
            - "Genéricos: Requisitos comunes."
            - "Transversales: Temas aplicables a múltiples sectores (terrenos, SEIA, etc.)."
            - "Sectoriales/Específicos: Requisitos particulares que prevalecen sobre genéricos."
          Req:
            - "Cumplimiento estricto para admisibilidad y evaluación."
          Src:
            - "RIS y fichas en sni.gob.cl."
        - ID: SNI-PRECIOS-SOCIALES-01
          Cpt: "Precios Sociales"
          Def: "Valores sombra que reflejan el costo/beneficio real para la sociedad."
          Req:
            - "Uso obligatorio en la evaluación socioeconómica."
          Resp:
            - "MDSF calcula, publica y actualiza los precios sociales."
          Ctx:
            - "Informe de Precios Sociales (ej. 2025)."
        - ID: SNI-BIP-01
          Cpt: "Banco Integrado de Proyectos (BIP)"
          Def: "Plataforma central para registro, postulación, almacenamiento y seguimiento de IDI."
          Func:
            - "Generar código BIP."
            - "Mantener Carpeta Digital."
            - "Registrar programación, solicitudes de financiamiento y RATE."
        - ID: SNI-MARCO-JURIDICO-01
          Cpt: "Marco jurídico principal del SNI"
          Fnd:
            - "DL N°1.263/1975 (Art. 19 bis)."
            - "Ley N°20.530/2011 (crea MDSF)."
            - "DFL 1-19.175 (LOC GORE, Art. 75)."
            - "Ley de Presupuestos anual."
          Ctx:
            - "Detalle ampliado en artefacto de normativa financiera y SNI del GORE."

  Sec_2_Tipos_IDI_y_Ciclo_de_Vida:
    ID: SNI-GORE-SEC-2-TIPOS-IDI-CICLO
    Clasificacion_Presupuestaria_Subt31:
      ID: SNI-TIPOS-IDI-01
      Ctx: "Clasificación presupuestaria de Iniciativas de Inversión en Subtítulo 31."
      Tipos:
        - ID: SNI-ITEM-01-ESTUDIOS-BASICOS-01
          Cpt: "Ítem 01 – Estudios Básicos"
          Def: "Gastos para generar información que permita identificar y formular nuevas IDI."
          Excl:
            - "No incluye estudios preinversionales ni diseños de proyectos ya identificados."
          Procesos_Validos:
            - "Actualización, análisis, diagnóstico, exploración, prospección, investigación."
        - ID: SNI-ITEM-02-PROYECTOS-01
          Cpt: "Ítem 02 – Proyectos"
          Def: |
            Gastos en estudios preinversionales, diseños y ejecución de obras/acciones para crear,
            ampliar, mantener, mejorar o recuperar capacidad de producción de bienes/servicios.
          Asignaciones_Tipicas:
            - "Gastos administrativos."
            - "Consultorías (estudios y diseños)."
            - "Terrenos."
            - "Obras civiles."
            - "Equipamiento y equipos."
            - "Vehículos."
        - ID: SNI-ITEM-03-PROGRAMAS-01
          Cpt: "Ítem 03 – Programas de Inversión (Subt. 31)"
          Def: |
            IDI orientadas a incrementar, mantener o recuperar capacidad de un recurso humano o
            físico, con duración finita y no inherentes a la misión permanente de la institución.
          Procesos_Validos:
            - "Capacitación externa, control de plagas, difusión técnica, prevención, protección, saneamiento, transferencia."
          Warn:
            - "No confundir con programas sociales de gasto corriente (Subt. 24)."
    Ciclo_Vida_IDI:
      ID: SNI-CICLO-VIDA-01
      Fases_Principales:
        - "Preinversión."
        - "Inversión."
        - "Operación."
      Etapas_Preinversion:
        - "Idea."
        - "Perfil."
        - "Prefactibilidad."
        - "Factibilidad."
      Etapas_Inversion:
        - "Diseño."
        - "Ejecución."
      Etapas_Operacion:
        - "Puesta en marcha."
        - "Operación en régimen."
      Ctx:
        - "Tabla comparativa por tipo de IDI (Estudios Básicos, Programas, Proyectos) detalla qué etapas aplican a cada uno."
      Src:
        - "NIP 2025, secciones 1.3 y tablas 1 y 4."
    Proporcionalidad_Niveles:
      Ref: SNI-PROPORCIONALIDAD-01

  Sec_3_Formulacion_Proyecto:
    ID: SNI-GORE-SEC-3-FORMULACION
    Objetivo_General:
      ID: SNI-FORMULACION-OBJ-01
      Obj: |
        Definir y estructurar una propuesta viable para solucionar un problema o necesidad
        mediante inversión pública, justificando la ejecución a partir de antecedentes sólidos.
      Ref:
        - SNI-EVAL-SOC-PRIV-01
        - SNI-INDIC-ECO-01
    Introduccion:
      ID: SNI-FORMULACION-INTRO-01
      Proc:
        - "Identificar y definir el problema."
        - "Caracterizar territorio, demanda y oferta para cuantificar el déficit."
        - "Plantear hipótesis de problema y contrastarlas con diagnóstico en un proceso iterativo."
      Res:
        - "Caracterización consistente del problema y de las alternativas de solución."
    Definicion_Problema:
      Ref: SNI-PROBLEMA-PRINCIPAL-01
      Metodos_Identificacion:
        - "Observación de la realidad: hechos no deseados y efectos negativos."
        - "Detección de oportunidades no aprovechadas."
        - "Contraste situación actual/futura con estándares y valores de referencia."
        - "Revisión de objetivos de políticas públicas e institucionales."
      Tipos_Problema:
        Ref: SNI-PROBLEMAS-01
    Analisis_Efectos_y_Causas:
      ID: SNI-FORMULACION-EFECTOS-CAUSAS-01
      Req:
        - "Identificar y respaldar con evidencia los efectos principales actuales y futuros sin intervención."
        - "Caracterizar causas principales que originan el problema."
      Beneficio:
        - "Facilitar la identificación de beneficios de la solución y el diseño de alternativas."
    Area_Estudio_e_Influencia:
      ID: SNI-AREA-ESTUDIO-INFLUENCIA-01
      Area_Estudio:
        Def: "Zona que da contexto al problema y fija los límites del análisis."
        Cont_Claves:
          - "Características generales del territorio y población."
          - "Red de infraestructura y servicios asociados al problema."
          - "Redes de accesibilidad y conectividad."
          - "Mapa con límites, redes y población."
      Area_Influencia:
        Def: "Territorio donde se manifiestan los efectos directos de las alternativas de solución."
        Beneficio:
          - "Permite determinar déficit, ubicar adecuadamente el proyecto y dimensionar la población objetivo."
      Criterios_Proporcionalidad:
        Ref: SNI-PROPORCIONALIDAD-01
    Analisis_Poblacion_Demanda_Oferta:
      ID: SNI-FORMULACION-POB-DEM-OFE-01
      Poblacion:
        Clasificacion:
          - "Población de referencia."
          - "Población sin problema."
          - "Población con problema."
          - "Población objetivo."
          - "Población postergada."
        Req:
          - "Revisar fuentes primarias y secundarias pertinentes."
          - "Proyectar población en horizonte de evaluación con métodos consistentes."
      Demanda:
        Def: "Requerimiento de la población de referencia por el bien/servicio, por unidad de tiempo y estándar dado."
        Tools:
          - "Proyecciones de población."
          - "Análisis de cambios en ingreso, estándares, preferencias y demanda oculta/inducida."
      Oferta:
        Def: "Capacidad de producción del bien/servicio en el área de influencia."
        Analisis:
          - "Cobertura: red de infraestructura y distribución territorial."
          - "Calidad: cumplimiento normativo, estado de conservación, nivel de servicio."
      Optimización_Oferta:
        ID: SNI-OPTIMIZACION-OFERTA-01
        Proc:
          - "Identificar medidas administrativas y de bajo costo para maximizar oferta."
          - "Justificar explícitamente si no es posible la optimización."
        Res:
          - "Si la optimización resuelve el problema, no se justifica un proyecto de inversión."
      Balance_Deficit:
        ID: SNI-DEFICIT-01
        Def: "Diferencia entre demanda y oferta cuando la primera supera a la segunda en la Situación Sin Proyecto."
        Tipos:
          - "Déficit cuantitativo (cobertura)."
          - "Déficit cualitativo (calidad)."
        Req:
          - "Usar una unidad de medida coherente para demanda y oferta."
    Alternativas_Solucion:
      ID: SNI-ALTERNATIVAS-01
      Proc:
        - "Definir estrategia de intervención para abordar el déficit identificado."
        - "Identificar y analizar preliminarmente todas las alternativas razonables."
        - "Descartar alternativas no viables o evidentemente menos favorables."
      Variables_Principales:
        - "Tamaño."
        - "Localización."
        - "Tecnología."
        - "Diseño."
        - "Organización e institucionalidad."
        - "Aspectos medioambientales."
        - "Relación con procesos SNI."
      Aplicacion_Proporcionalidad:
        Ref: SNI-PROPORCIONALIDAD-01
      Separabilidad_Componentes:
        Ref: SNI-SEPARABILIDAD-01

    Seleccion_y_Presentacion_Alternativa:
      ID: SNI-FORMULACION-SEL-ALT-01
      Pasos:
        - "Presentar la conclusión sobre la alternativa de solución más conveniente, basada en la evaluación social."
        - "Profundizar la especificación técnica, legal, financiera y del Modelo de Gestión de la alternativa seleccionada."
      Obj:
        - "Asegurar la viabilidad y sustentabilidad del proyecto antes de su postulación al SNI."
      Src:
        - "Sección 'Selección y presentación de la alternativa de solución' de la guía."

  Sec_4_Evaluacion_Social:
    ID: SNI-GORE-SEC-4-EVAL-SOCIAL
    Clasificacion_Efectos:
      ID: SNI-EVAL-EFECTOS-01
      Ctx: "Clasificación de efectos generados por la implementación del proyecto."
      Categorias:
        - "Efectos directos: impactos atribuibles directamente al proyecto en el mercado del bien/servicio."
        - "Efectos indirectos: consecuencias en mercados relacionados (sustitución, complementariedad, encadenamientos)."
        - "Externalidades: efectos sobre agentes en mercados no relacionados (ej. ruido, contaminación, emisiones de CO₂)."
    Tipos_Analisis_Evaluacion:
      ID: SNI-EVAL-TIPOS-01
      Tipos:
        - "Analisis Costo-Beneficio (ACB): compara beneficios y costos sociales en valor presente; indicador principal: VAN."
        - "Analisis Costo-Eficiencia (ACE): compara costos sociales cuando los beneficios son difíciles de valorar pero equivalentes entre alternativas; indicadores: VAC y CAE."
      Req:
        - "Usar el tipo de análisis indicado en metodologías específicas y RIS sectoriales."
      Ref:
        - SNI-INDIC-ECO-01
    Determinacion_Beneficios_y_Costos:
      ID: SNI-EVAL-BENEF-COSTOS-01
      Beneficios:
        Tipos:
          - "Aumento del bienestar de la población: mayor consumo o calidad de bienes/servicios, mejoras ambientales o socioculturales."
          - "Liberacion de recursos: reducción de costos de operación, mantenimiento, traslados u otros recursos que quedan disponibles para usos alternativos."
      Costos:
        Clases:
          - "Costos directos: inversión, reinversión, operación, mantenimiento, cierre y costo social de traslado."
          - "Costos indirectos: efectos en mercados relacionados, incluidos si pueden identificarse, cuantificarse y valorarse."
          - "Costos externos: externalidades negativas sobre agentes en otros mercados (ej. emisiones, ruido)."
        Tratamiento:
          - "En etapas tempranas, cuando no es posible cuantificar o valorar costos indirectos o externos, deben al menos identificarse y caracterizarse."
      Ref:
        - SNI-PRECIOS-SOCIALES-01
        - SNI-EVAL-SOC-PRIV-01
    Flujos_de_Caja_y_Estructura:
      ID: SNI-EVAL-FLUJOS-01
      Tipos_Flujo:
        - "Flujos totales: comparan Situación Con Proyecto y Situación Sin Proyecto en forma completa."
        - "Flujos incrementales: consideran solo las diferencias entre Situación Con Proyecto y Sin Proyecto; son el enfoque por defecto en el SNI."
      Aplicacion:
        - "En ACB se construyen flujos de beneficios netos (beneficios sociales menos costos sociales)."
        - "En ACE se presentan flujos de costos de cada alternativa."
      Ref:
        - SNI-VAN-01
        - SNI-VAC-01
        - SNI-CAE-01
    Horizonte_y_Valor_Residual:
      ID: SNI-EVAL-HORIZONTE-VR-01
      Horizonte_Evaluacion:
        Def: "Periodo para el cual se proyectan demanda, oferta y flujos de fondos del proyecto."
        Req:
          - "Utilizar horizontes definidos en metodologías específicas o RIS; en su defecto, justificar un horizonte ad hoc."
          - "Trabajar con flujos anuales desde el inicio de operación, aunque la inversión dure varios años."
      Valor_Residual:
        Def: "Valor remanente de los activos principales al final del horizonte de evaluación cuando su vida útil lo supera."
        Principios:
          - "Se calcula siguiendo métodos contables (valor libro), excluyendo el valor del terreno salvo que se venda o libere para otro uso."
          - "El terreno no se deprecia y su valor representa costo de oportunidad en el mejor uso alternativo."
      Ref:
        - SNI-PRECIOS-SOCIALES-01
        - SNI-EVAL-FLUJOS-01
        - SNI-INDIC-ECO-01

    Evaluacion_Privada_Flujos:
      ID: SNI-EVAL-PRIV-FLUJOS-01
      Proposito:
        - "Describir la estructura de los flujos de caja utilizados en la evaluación privada de proyectos."
        - "Distinguir entre flujo puro del proyecto, flujo de la deuda y flujo del inversionista."
      Flujo_Caja_Puro_Neto:
        ID: SNI-EVAL-PRIV-FLUJO-PURO-01
        Descripcion: "Flujo de caja generado por el proyecto antes de considerar su financiamiento."
        Items_Clave:
          - "Ingresos Totales (IT): ingresos afectos a impuestos."
          - "Egresos de Operacion (EO): costos de operación afectos a impuestos."
          - "EBITDA (EB): IT - EO."
          - "Gastos no desembolsables (Gnd): depreciaciones, amortizaciones y otros cargos sin salida de caja."
          - "Utilidad antes de impuestos (Uai): EB - Gnd."
          - "Impuestos (Imp): tributos sobre la utilidad."
          - "Utilidad despues de impuestos (Udi): Uai - Imp."
          - "Ajuste por Gnd: se suma nuevamente para obtener flujo de caja."
          - "Flujo Operacional Neto (Fop): Udi + Gnd."
          - "Inversiones (Inv): desembolsos de capital en años de inversión."
          - "Valor Residual (VR): valor remanente al final del horizonte."
          - "Flujo Caja Puro Neto (FN): flujo de caja puro del proyecto, incluyendo inversiones y valor residual."
      Flujo_Caja_Deuda:
        ID: SNI-EVAL-PRIV-FLUJO-DEUDA-01
        Descripcion: "Flujo asociado al uso de deuda como fuente de financiamiento."
        Items_Clave:
          - "Intereses de la deuda (Int)."
          - "Utilidad antes de impuestos ajustada por intereses (Uai)."
          - "Ahorro Tributario (AT): reducción de impuestos por efecto de los intereses."
          - "Costo efectivo de la deuda (Ced): intereses menos ahorro tributario."
          - "Amortizacion de la deuda (Amt)."
          - "Prestamo (Pm): monto recibido como financiamiento."
          - "Flujo Caja Deuda (FD): combinación de costo efectivo, amortizaciones y préstamos."
      Flujo_Caja_Inversionista:
        ID: SNI-EVAL-PRIV-FLUJO-INV-01
        Def: "Suma del flujo de caja puro neto y el flujo de la deuda; representa la rentabilidad para el inversionista."
        Componentes:
          - "FN: Flujo Caja Puro Neto."
          - "FD: Flujo Caja Deuda."
          - "FInv: Flujo Caja Inversionista = FN + FD."
      Ref:
        - SNI-EVAL-SOC-PRIV-01

  # Nota: Secciones 4–7 se condensan para mantener el artefacto denso. Pueden expandirse
  # en futuras versiones si necesitas más detalle operativo.

  Sec_4_BIP_RIS_y_Carpeta_Digital:
    ID: SNI-GORE-SEC-4-BIP-RIS
    BIP:
      Ref: SNI-BIP-01
      Func_Claves:
        - "Crear y gestionar el Código BIP (ficha maestra de la IDI)."
        - "Registrar resultados esperados y beneficiarios."
        - "Administrar la Carpeta Digital con toda la documentación de respaldo."
    Carpeta_Digital:
      ID: SNI-CARPETA-DIGITAL-01
      Def: "Repositorio electrónico en BIP para toda la documentación de la IDI."
      Subcarpetas_Tipicas:
        - "01-Estudio-Preinversional."
        - "02-Evaluacion-Economica-Presupuesto."
        - "03-TDR-EETT."
        - "04-Planos-Ingenieria."
        - "05-Anexos."
        - "06-Oficios."
        - "07-Incumplimiento-Normativa."
        - "08-Terreno."
        - "09-Equipos."
        - "10-Resultados-Estudio-Basico."
        - "11-Reevaluaciones."
        - "12-Ejecucion-Presupuestaria."
    RIS:
      Ref: SNI-RIS-01
      Ctx:
        - "Uso obligatorio de RIS genéricas, transversales y sectoriales según tipo de IDI."
        - "La guía RIS de Proyectos de Inversión 2023 se detalla en artefacto GN-RIS-PROYINV-2023-01."

  Sec_5_Evaluacion_ExAnte_y_RATE:
    ID: SNI-GORE-SEC-5-EVAL-EXANTE
    Ref:
      - SNI-EVAL-SOC-PRIV-01
      - SNI-INDIC-ECO-01
    Fases:
      - ID: SNI-ADMSBL-01
        Cpt: "Admisibilidad"
        Def: "Revisión formal y de completitud de antecedentes según RIS."
        Plazo_MDSF: "Máximo 5 días hábiles."
      - ID: SNI-ATE-01
        Cpt: "Análisis Técnico-Económico (ATE)"
        Def: "Evaluación en profundidad de conveniencia y calidad de la IDI."
        Plazo_Primer_RATE: "Máximo 10 días hábiles desde la fecha de ingreso al SNI."
    Resultados_RATE:
      ID: SNI-RATE-01
      Tipos:
        - "RATE-RS: Recomendado Satisfactoriamente; habilita gestión de financiamiento."
        - "RATE-FI: Falta de Información; requiere subsanar observaciones (plazo máx. 60 días hábiles)."
        - "RATE-OT: Objetado Técnica y/o Administrativamente; IDI no conveniente o inviable."
        - "RATE-AD: Admisible para Financiamiento (conservación)."
        - "Otros: IN (Incumplimiento Normativa), CF (Continuidad Favorable), RE (Reevaluación)."
    Vigencia_RATE:
      ID: SNI-RATE-VIGENCIA-01
      Regla:
        - "Vigencia estándar de RATE favorable (RS/CF/AD): 3 años presupuestarios consecutivos."
        - "Requiere actualizar montos y confirmar que no existan cambios significativos."
        - "Pérdida de vigencia si la IDI no inicia ejecución dentro del periodo."

  Sec_6_Ejecucion_y_Transferencias:
    ID: SNI-GORE-SEC-6-EJECUCION
    XRef_Required:
      - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-03"
      - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-04"
      - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART07"
    Restricciones_Presupuesto_2026:
      ID: SNI-RESTR-PPTO-2026-SEC6-01
      Glosa_03:
        ID: SNI-RESTR-PPTO-2026-SEC6-GLO03-01
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-03"
        Content: |
          Los recursos de los presupuestos de inversión regional no podrán financiar préstamos, gastos en personal, o gastos en bienes y servicios de consumo de las entidades receptoras. Asimismo, no podrán destinarse para constituir, efectuar aportes o comprar sociedades o empresas.
      Glosa_04:
        ID: SNI-RESTR-PPTO-2026-SEC6-GLO04-01
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-04"
        Content: |
          Se podrán traspasar recursos desde cualquier Subtítulo e Ítem del presupuesto de inversión del Gobierno Regional respectivo a los Subtítulos 24, 26, 29, 31, 32.06, 33 y 34.07.
          Los gobiernos regionales podrán realizar convenios de mandato con los municipios de acuerdo con el artículo 16 de la ley N°18.091, para el financiamiento de estudios definidos en el subtítulo 22 ítem 11, del Decreto de Hacienda N° 854 del 2004, sobre clasificaciones presupuestarias.
      Articulo_07:
        ID: SNI-RESTR-PPTO-2026-SEC6-ART07-01
        XRef_Required:
          - "urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART07"
        Purp: "Reglas para decretos con transferencias (Subtítulos 24 y 33)."
        Decretos_Transferencias:
          Subtitulos:
            - "Subtítulo 24: Transferencias Corrientes"
            - "Subtítulo 33: Transferencias de Capital"
          Puede_Indicar:
            - "Uso o destino que la institución receptora deberá dar a los recursos"
            - "Condiciones o modalidades de reintegro"
            - "Información sobre aplicación a remitir y organismo destinatario"
        Transferencias_Subtitulo24_Unidades_Programas:
          Cond: "Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste"
          Req:
            Desc: "Desglose previo a la ejecución presupuestaria en conceptos de gasto"
            Ref: SNI-ACTOR-DIPRES-01
          Req_Reporte:
            Frecuencia: Mensual
            Destinatario: DIPRES
            Contenido:
              - "Informe avance actividades"
              - "Información ejecución presupuestaria"
          Res: "Desglose constituye autorización máxima de gasto por concepto"
          Proc_Modificacion: "Modificaciones mediante igual procedimiento"
          Ctx:
            Visacion: "Puede efectuarse desde fecha publicación de esta ley"
          Prohib:
            Desc: "No incluir recursos para gastos en personal ni bienes y servicios de consumo"
            Cond: "Salvo autorización por norma expresa en el respectivo presupuesto"
          Res_Personal:
            Res: "Personal contratado con cargo a dichos recursos no forma parte de la dotación del Servicio"
    Ejecucion_Directa_GORE:
      ID: SNI-EJEC-DIRECTA-01
      Def: "GORE actúa como Unidad Técnica y Financiera, licitando, contratando y pagando directamente."
      Imputacion:
        - "Generalmente Subtítulo 31 – Iniciativas de Inversión."
    Ejecucion_Terceros_Transferencias:
      ID: SNI-TRANSFERENCIAS-01
      Tipos:
        - ID: SNI-TRANSF-NC-01
          Cpt: "Transferencia Directa (No Consolidable)"
          Receptor_Tipico:
            - "Municipalidades."
            - "Entidades privadas sin fines de lucro."
          Mech:
            - "Convenio de transferencia GORE–receptor."
            - "Toma de razón (según corresponda)."
            - "Rendición de cuentas detallada al GORE."
        - ID: SNI-TRANSF-CONS-01
          Cpt: "Transferencia Consolidable"
          Receptor_Tipico:
            - "Ministerios y servicios públicos con presupuesto en Ley de Presupuestos."
          Mech:
            - "Decreto de DIPRES que rebaja presupuesto del GORE y aumenta el de la entidad receptora."
            - "Gasto se registra en presupuesto de la entidad receptora."
      Ctx:
        - "El GORE monitorea avance físico, incluso cuando la ejecución presupuestaria recae en otra entidad."

  Sec_7_Procedimientos_Especiales:
    ID: SNI-GORE-SEC-7-ESPECIALES
    FRIL_Exencion_5000_UTM:
      ID: SNI-ESPECIAL-FRIL-01
      Def: "Proyectos FRIL < 5.000 UTM no requieren informe favorable MDSyF, pero deben ingresar información necesaria al SNI para control/registro."
      Purp: "Agilizar inversión en infraestructura menor a escala local."
      Ctx:
        - "Se rige por glosas específicas y guía operativa detallada del GORE."
        - "kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-12"
    Proyectos_Conservacion_Circular_33:
      ID: SNI-ESPECIAL-CIRC33-01
      Def: "Procedimiento simplificado para proyectos de conservación de infraestructura pública."
      Ctx:
        - "Marco normativo en Circular 33 y normativa asociada."
    Reconstruccion_Emergencias:
      ID: SNI-ESPECIAL-EMERG-01
      Purp: "Permitir inversión ágil para reparar o reponer infraestructura dañada por desastres."
      Clasificacion_BIP:
        - "Con decreto de zona de catástrofe: descriptor BIP específico, ficha de daños obligatoria."
        - "Sin decreto pero con criticidad: descriptor 'Emergencia' más acto administrativo que la declara."
      Proc_Agilizados:
        - "Prioridad de revisión MDSF (plazo máximo 10 días hábiles)."
        - "Posibilidad de postular ejecución incluyendo diseño, con hito de aprobación de diseño previo a obras."
      Tipos_Intervencion:
        - "Reparación: Recupera estándar y capacidad original."
        - "Reposición sin cambio de capacidad."
        - "Reposición con cambio de capacidad (sigue reglas estándar del SNI, no agilizadas)."