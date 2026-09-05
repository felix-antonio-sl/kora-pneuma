---
urn: urn:gn:kb:gn-problemas-sociales-cl
nombre: gn-problemas-sociales-cl
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-problemas-sociales-cl; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/02_estrategia/social/kb_gn_004_problemas_sociales_cl_koda.yml (sha256:c02211e1605da78b6b5d2b43077aec9f2463b033e7a91e23b0efa654bd6d6f19); URN KODA legado urn:gorenuble:gn:problemas-sociales-cl:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-15
lang: es
tags: ["gn", "gore-os", "koda", "domains", "02-estrategia", "social", "problemas", "sociales"]
familia: bok
---
_manifest:
  urn: 'urn:gorenuble:gn:problemas-sociales-cl:1.0.0'
  federation:
    visibility: internal
    license: Institutional Use
  compatibility:
    min_consumer_version: 1.0.0
    breaking_changes_from: null
  resolution:
    canonical_url: >-
      file://knowledge/domains/gn/social/kb_gn_004_problemas_sociales_cl_koda.yml
    mirrors: []
  dependencies:
    requires:
      - urn: 'urn:kora:kb:spec:1.0.0'
        reason: KODA/Spec format compliance
      - urn: 'urn:kora:kb:transform:1.0.0'
        reason: Transformation methodology reference
  provenance:
    created_by: FS
    created_at: '2025-12-15'
    last_modified_at: '2025-12-15'
    signature: null
ID: GN-PROBLEMAS-SOCIALES-CL-01
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-CASCADE
AI-Remediator: KODA-TRANSFORMER
Creation-Date: '2025-12-15'
Modification-Date: '2025-12-15'
Ctx: Catálogo de Problemas Sociales de Chile (STS)
Primary-Source: staging/gn/kodeando/kb_gn_004_problemas_sociales_cl_sts.md
LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: >-
    BEGIN_LLM_INSTRUCTIONS You are an AI agent consuming a KODA artifact. Parse
    with absolute fidelity. FIDELITY: Preserve meat (essential information) and
    skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat
    (filler words, rhetoric, stylistic prose). LEXICON (expand before
    processing): Act->Action, Cond->Condition, Ctx->Context,
    Ctx_Required->Required External Reference, Ctx_Optional->Optional External
    Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification,
    Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition,
    Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement,
    Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference,
    XRef_Required->Mandatory Cross-Artifact Reference. REFERENCE POLICY: Ref: is
    internal only—must point to existing ID within THIS document.
    XRef/XRef_Required: external URN (optionally with #ID fragment) only.
    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed),
    content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS
catalogo_de_problemas_sociales_de_chile_sts:
  ID: GN-PROBLEMAS-SOCIALES-CL-DOC-01
  Title: Catálogo de Problemas Sociales de Chile (STS)
  Sections:
    s_1_salud:
      ID: GN-SEC-0001
      Title: 1. Salud
      Content: 'ID: STS-PS-CH-SALUD'
      Sections:
        s_1_1_salud_general:
          ID: GN-SEC-0002
          Title: 1.1. Salud General
          Content: 'ID: STS-PS-CH-SALUD-GENERAL'
          Sections:
            s_1_1_1_acceso_y_cobertura:
              ID: GN-SEC-0003
              Title: 1.1.1. Acceso y Cobertura
              Content: 'ID: STS-PS-CH-SALUD-GENERAL-ACCESO'
              Sections:
                s_1_1_1_1_falla_acceso_a_atencion_tratamiento_salud_ante_necesidad:
                  ID: GN-SEC-0004
                  Title: >-
                    1.1.1.1. Falla acceso a atención/tratamiento salud ante
                    necesidad
                  Content: |-
                    ID: STS-PS-CH-SALUD-GENERAL-ACCESO-P01
                    Def: Desigualdad estructural en acceso a servicios de salud.
                    Cause:
                    - Cobertura insuficiente.
                    - Tiempos de espera excesivos.
                    - Otras barreras.
                    Cpt: Indicador.
                    - Ctx: Pobreza Multidimensional.
                    - Def: Falta de atención médica frente a necesidad.
                    Ctx: Inclusiones.
                    - Atención primaria.
                    - Urgencias.
                    - Enfermedades no transmisibles.
                    Ctx: Exclusiones.
                    - Programas exclusivos salud reproductiva.
                    - Programas exclusivos salud conductual.
                    - Programas exclusivos salud mental.
                    - Programas exclusivos salud dental.
                s_1_1_1_2_deficit_de_especialistas_medicos:
                  ID: GN-SEC-0005
                  Title: 1.1.1.2. Déficit de especialistas médicos
                  Content: >-
                    ID: STS-PS-CH-SALUD-GENERAL-ACCESO-P02 Def: Insuficiencia de
                    profesionales salud para cubrir demanda (número y
                    especialidad). Ctx: Alcance. - Todas las especialidades
                    médicas.
                s_1_1_1_3_barreras_de_acceso_a_inmunizacion_universal:
                  ID: GN-SEC-0006
                  Title: 1.1.1.3. Barreras de acceso a inmunización universal
                  Content: >-
                    ID: STS-PS-CH-SALUD-GENERAL-ACCESO-P03 Def: Dificultad para
                    acceder a vacunas contra enfermedades transmisibles e
                    inmunoprevenibles.
            s_1_1_2_costos:
              ID: GN-SEC-0007
              Title: 1.1.2. Costos
              Content: 'ID: STS-PS-CH-SALUD-GENERAL-COSTOS'
              Sections:
                s_1_1_2_1_costo_elevado_de_medicamentos:
                  ID: GN-SEC-0008
                  Title: 1.1.2.1. Costo elevado de medicamentos
                  Content: |-
                    ID: STS-PS-CH-SALUD-GENERAL-COSTOS-P01
                    Def: Gasto excesivo en fármacos para la población.
                    Ctx: Exclusiones.
                    - Programas exclusivos para medicamentos de salud mental.
                s_1_1_2_2_costo_elevado_de_servicios_de_salud:
                  ID: GN-SEC-0009
                  Title: 1.1.2.2. Costo elevado de servicios de salud
                  Content: >-
                    ID: STS-PS-CH-SALUD-GENERAL-COSTOS-P02 Def: Gasto excesivo
                    en hospitalización, procedimientos, exámenes y tratamientos.
                    Cause: Acceso a salud condicionado por capacidad de pago del
                    hogar. Ctx: Inclusiones. - Enfermedades catastróficas. Ctx:
                    Exclusiones. - Programas exclusivos para costos de salud
                    mental y dental.
            s_1_1_3_calidad:
              ID: GN-SEC-0010
              Title: 1.1.3. Calidad
              Content: 'ID: STS-PS-CH-SALUD-GENERAL-CALIDAD'
              Sections:
                s_1_1_3_1_calidad_deficiente_en_atencion_de_salud:
                  ID: GN-SEC-0011
                  Title: 1.1.3.1. Calidad deficiente en atención de salud
                  Content: |-
                    ID: STS-PS-CH-SALUD-GENERAL-CALIDAD-P01
                    Def: Fallas en la calidad del servicio de salud.
                    Cpt: Componentes.
                    - Calidad de atención directa.
                    - Oportunidad de información.
                    - Infraestructura.
                    - Equipamiento.
                    - Competencia profesional.
                    Ctx: Alcance.
                    - Todas las temáticas de salud.
            s_1_1_4_prevencion_y_promocion:
              ID: GN-SEC-0012
              Title: 1.1.4. Prevención y Promoción
              Content: 'ID: STS-PS-CH-SALUD-GENERAL-PREVENCION'
              Sections:
                s_1_1_4_1_deficit_en_prevencion_y_promocion_de_la_salud_general:
                  ID: GN-SEC-0013
                  Title: >-
                    1.1.4.1. Déficit en prevención y promoción de la salud
                    general
                  Content: >-
                    ID: STS-PS-CH-SALUD-GENERAL-PREVENCION-P01 Def: Insuficiente
                    fomento de conductas saludables para mejorar la salud
                    poblacional. Ctx: Exclusiones. - Programas exclusivos para
                    promoción en salud reproductiva, conductual, mental, dental.
        s_1_2_salud_especifica:
          ID: GN-SEC-0014
          Title: 1.2. Salud Específica
          Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA'
          Sections:
            s_1_2_1_salud_dental:
              ID: GN-SEC-0015
              Title: 1.2.1. Salud Dental
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-DENTAL'
              Sections:
                s_1_2_1_1_costo_elevado_de_tratamientos_dentales:
                  ID: GN-SEC-0016
                  Title: 1.2.1.1. Costo elevado de tratamientos dentales
                  Content: |-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-DENTAL-P01
                    Def: Gasto excesivo en servicios odontológicos.
                s_1_2_1_2_falla_acceso_a_atencion_tratamiento_dental:
                  ID: GN-SEC-0017
                  Title: 1.2.1.2. Falla acceso a atención/tratamiento dental
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-DENTAL-P02 Def: Barreras que
                    impiden a personas con problemas odontológicos acceder a
                    atención. Ctx: Inclusiones. - Atención preventiva. -
                    Atención recuperativa. - Rehabilitación protésica.
                s_1_2_1_3_deficit_en_prevencion_y_promocion_de_salud_dental:
                  ID: GN-SEC-0018
                  Title: 1.2.1.3. Déficit en prevención y promoción de salud dental
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-DENTAL-P03 Def: Insuficiente
                    promoción, educación y acciones preventivas para el cuidado
                    bucal.
            s_1_2_2_salud_mental:
              ID: GN-SEC-0019
              Title: 1.2.2. Salud Mental
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-MENTAL'
              Sections:
                s_1_2_2_1_deficit_en_prevencion_de_problemas_de_salud_mental:
                  ID: GN-SEC-0020
                  Title: 1.2.2.1. Déficit en prevención de problemas de salud mental
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-MENTAL-P01 Def: Insuficiente
                    prevención, promoción y educación para la salud mental.
                s_1_2_2_2_costo_elevado_de_tratamiento_y_medicamentos_de_salud_mental:
                  ID: GN-SEC-0021
                  Title: >-
                    1.2.2.2. Costo elevado de tratamiento y medicamentos de
                    salud mental
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-MENTAL-P02 Def: Gasto
                    excesivo en tratamientos y fármacos psiquiátricos.
                s_1_2_2_3_falla_acceso_a_atencion_tratamiento_de_salud_mental:
                  ID: GN-SEC-0022
                  Title: 1.2.2.3. Falla acceso a atención/tratamiento de salud mental
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-MENTAL-P03 Def: Barreras que
                    impiden a personas con trastornos (depresión, demencia,
                    etc.) acceder a atención preventiva o de tratamiento.
            s_1_2_3_salud_sexual_y_reproductiva:
              ID: GN-SEC-0023
              Title: 1.2.3. Salud Sexual y Reproductiva
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-SEXUAL'
              Sections:
                s_1_2_3_1_deficit_en_educacion_y_prevencion_en_salud_sexual_reproductiva:
                  ID: GN-SEC-0024
                  Title: >-
                    1.2.3.1. Déficit en educación y prevención en salud
                    sexual/reproductiva
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-SEXUAL-P01 Def: Carencia de
                    información, prevención y educación que limita la autonomía
                    y el ejercicio de derechos sexuales y reproductivos.
                s_1_2_3_2_acceso_limitado_a_metodos_anticonceptivos:
                  ID: GN-SEC-0025
                  Title: 1.2.3.2. Acceso limitado a métodos anticonceptivos
                  Content: |-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-SEXUAL-P02
                    Def: Dificultad para obtener anticonceptivos.
                    Cause:
                    - Oferta insuficiente.
                    - Costos elevados.
                s_1_2_3_3_falla_acceso_a_servicios_de_salud_sexual_reproductiva:
                  ID: GN-SEC-0026
                  Title: >-
                    1.2.3.3. Falla acceso a servicios de salud
                    sexual/reproductiva
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-SEXUAL-P03 Def: Barreras para
                    acceder a consultas, tratamientos, medicamentos y otros
                    servicios del área.
            s_1_2_4_consumo_de_sustancias:
              ID: GN-SEC-0027
              Title: 1.2.4. Consumo de Sustancias
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-SUSTANCIAS'
              Sections:
                s_1_2_4_1_abordaje_insuficiente_del_consumo_problematico_de_sustancias:
                  ID: GN-SEC-0028
                  Title: >-
                    1.2.4.1. Abordaje insuficiente del consumo problemático de
                    sustancias
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-SUSTANCIAS-P01 Def: Carencias
                    en la prevención del consumo problemático y en el
                    tratamiento/rehabilitación de adicciones (alcohol, drogas,
                    tabaco).
            s_1_2_5_nutricion:
              ID: GN-SEC-0029
              Title: 1.2.5. Nutrición
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-NUTRICION'
              Sections:
                s_1_2_5_1_abordaje_insuficiente_de_la_malnutricion:
                  ID: GN-SEC-0030
                  Title: 1.2.5.1. Abordaje insuficiente de la malnutrición
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-NUTRICION-P01 Def: Carencias
                    en tratamiento de sobrepeso, obesidad, desnutrición (o
                    riesgo) y en la prevención de sus causas.
                s_1_2_5_2_promocion_deficiente_de_alimentacion_saludable:
                  ID: GN-SEC-0031
                  Title: 1.2.5.2. Promoción deficiente de alimentación saludable
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-NUTRICION-P02 Def:
                    Insuficiente fomento de conductas y estilos de vida
                    saludables. Ctx: Barreras. - Alto costo de alimentos
                    saludables. - Entornos alimentarios no saludables. - Déficit
                    nutricional.
            s_1_2_6_vih_e_its:
              ID: GN-SEC-0032
              Title: 1.2.6. VIH e ITS
              Content: 'ID: STS-PS-CH-SALUD-ESPECIFICA-VIH'
              Sections:
                s_1_2_6_1_abordaje_insuficiente_del_vih_e_infecciones_de_transmision_sexual_its:
                  ID: GN-SEC-0033
                  Title: >-
                    1.2.6.1. Abordaje insuficiente del VIH e Infecciones de
                    Transmisión Sexual (ITS)
                  Content: >-
                    ID: STS-PS-CH-SALUD-ESPECIFICA-VIH-P01 Def: Carencias en
                    promoción del autocuidado para control de VIH/ITS y en el
                    tratamiento de estas enfermedades.
    s_2_desarrollo_social:
      ID: GN-SEC-0034
      Title: 2. Desarrollo Social
      Content: 'ID: STS-PS-CH-DESOC'
      Sections:
        s_2_1_pobreza_y_hogar:
          ID: GN-SEC-0035
          Title: 2.1. Pobreza y Hogar
          Content: 'ID: STS-PS-CH-DESOC-POBREZA'
          Sections:
            s_2_1_1_capacidades_debiles_del_hogar_para_superar_pobreza:
              ID: GN-SEC-0036
              Title: 2.1.1. Capacidades débiles del hogar para superar pobreza
              Content: >-
                ID: STS-PS-CH-DESOC-POBREZA-P01 Def: Familias/hogares carecen de
                herramientas para salir de la condición de pobreza. Ctx:
                Inclusiones. - Educación financiera familiar.
            s_2_1_2_bajos_ingresos_del_hogar:
              ID: GN-SEC-0037
              Title: 2.1.2. Bajos ingresos del hogar
              Content: >-
                ID: STS-PS-CH-DESOC-POBREZA-P02 Def: Carencia de recursos
                económicos en familias/hogares para cubrir necesidades mínimas.
                Req: Aporte complementario para satisfacer necesidades
                específicas no cubiertas por recursos propios. Ex:
                Transferencias monetarias.
        s_2_2_dependencia_y_cuidado:
          ID: GN-SEC-0038
          Title: 2.2. Dependencia y Cuidado
          Content: 'ID: STS-PS-CH-DESOC-DEPENDENCIA'
          Sections:
            s_2_2_1_deficit_de_profesionales_y_espacios_especializados_para_dependencia:
              ID: GN-SEC-0039
              Title: >-
                2.2.1. Déficit de profesionales y espacios especializados para
                dependencia
              Content: >-
                ID: STS-PS-CH-DESOC-DEPENDENCIA-P01 Def: Pacientes con
                dependencia severa carecen de espacios adecuados y personal
                especializado para su cuidado y mejora de calidad de vida. Ctx:
                Inclusiones. - Profesionales. - Técnicos. - Educación en
                dependencia (para personas con y sin dependencia).
            s_2_2_2_entornos_inaccesibles_y_barreras_contextuales_generan_dependencia_exclus:
              ID: GN-SEC-0040
              Title: >-
                2.2.2. Entornos inaccesibles y barreras contextuales generan
                dependencia/exclusión
              Content: >-
                ID: STS-PS-CH-DESOC-DEPENDENCIA-P02 Def: Personas con
                dependencia moderada/severa enfrentan dificultades para realizar
                actividades de la vida diaria. Cause: Barreras en el entorno
                físico y social.
            s_2_2_3_apoyo_insuficiente_a_cuidadores_de_personas_dependientes:
              ID: GN-SEC-0041
              Title: 2.2.3. Apoyo insuficiente a cuidadores de personas dependientes
              Content: >-
                ID: STS-PS-CH-DESOC-DEPENDENCIA-P03 Def: Cuidadores de personas
                dependientes enfrentan malas condiciones, falta de apoyo e
                ingresos insuficientes.
            s_2_2_4_condiciones_precarias_en_centros_residenciales:
              ID: GN-SEC-0042
              Title: 2.2.4. Condiciones precarias en centros residenciales
              Content: >-
                ID: STS-PS-CH-DESOC-DEPENDENCIA-P04 Def: Deficiencias en
                residencias protegidas para personas que lo requieren. Ctx:
                Población. - NNA con derechos vulnerados. - Personas con
                discapacidad. - Adultos mayores. - Otros.
            s_2_2_5_provision_insuficiente_de_ayudas_tecnicas_y_servicios_de_rehabilitacion:
              ID: GN-SEC-0043
              Title: >-
                2.2.5. Provisión insuficiente de ayudas técnicas y servicios de
                rehabilitación
              Content: >-
                ID: STS-PS-CH-DESOC-DEPENDENCIA-P05 Def: Carencia de apoyos
                necesarios para que personas en situación de discapacidad
                superen barreras del entorno.
        s_2_3_ninez_y_familia:
          ID: GN-SEC-0044
          Title: 2.3. Niñez y Familia
          Content: 'ID: STS-PS-CH-DESOC-NINEZ'
          Sections:
            s_2_3_1_riesgo_de_retraso_en_desarrollo_biopsicosocial_infantil:
              ID: GN-SEC-0045
              Title: 2.3.1. Riesgo de retraso en desarrollo biopsicosocial infantil
              Content: >-
                ID: STS-PS-CH-DESOC-NINEZ-P01 Def: Niños/as en riesgo de
                retraso, rezago en el desarrollo o riesgo biopsicosocial. Ctx:
                Alcance. - Incluye falta de desarrollo integral y de
                protección/promoción de este en cualquier circunstancia.
            s_2_3_2_vulneracion_de_derechos_de_ninos_ninas_y_adolescentes_nna:
              ID: GN-SEC-0046
              Title: >-
                2.3.2. Vulneración de derechos de Niños, Niñas y Adolescentes
                (NNA)
              Content: |-
                ID: STS-PS-CH-DESOC-NINEZ-P02
                Def: Ocurrencia de situaciones de maltrato infantil.
                Ex:
                - Abandono.
                - Trabajo infantil.
                - Abuso sexual.
                - Violencia.
            s_2_3_3_debilitamiento_del_espacio_sociofamiliar:
              ID: GN-SEC-0047
              Title: 2.3.3. Debilitamiento del espacio sociofamiliar
              Content: |-
                ID: STS-PS-CH-DESOC-NINEZ-P03
                Def: Deterioro del núcleo y las relaciones sociofamiliares.
                Ex:
                - Falta de preparación para la adopción.
                - Separación familiar.
                - No reconocimiento del matrimonio.
            s_2_3_4_competencias_parentales_de_crianza_debiles:
              ID: GN-SEC-0048
              Title: 2.3.4. Competencias parentales/de crianza débiles
              Content: >-
                ID: STS-PS-CH-DESOC-NINEZ-P04 Def: Ausencia de habilidades
                personales, parentales y sociales en adultos a cargo de la
                crianza de NNA. Ctx: Alcance. - Incluye cuidadores principales,
                no solo padres/madres.
            s_2_3_5_falta_de_apoyo_a_adolescentes_embarazadas:
              ID: GN-SEC-0049
              Title: 2.3.5. Falta de apoyo a adolescentes embarazadas
              Content: >-
                ID: STS-PS-CH-DESOC-NINEZ-P05 Def: Madres adolescentes y
                adolescentes embarazadas con derechos vulnerados o necesidad de
                apoyo (físico/psicológico) durante la gestación.
    s_3_grupos_vulnerables:
      ID: GN-SEC-0050
      Title: 3. Grupos Vulnerables
      Content: 'ID: STS-PS-CH-GRUPOS'
      Sections:
        s_3_1_derechos_por_grupo:
          ID: GN-SEC-0051
          Title: 3.1. Derechos por Grupo
          Content: 'ID: STS-PS-CH-GRUPOS-DERECHOS'
          Sections:
            s_3_1_1_personas_mayores:
              ID: GN-SEC-0052
              Title: 3.1.1. Personas Mayores
              Content: 'ID: STS-PS-CH-GRUPOS-MAYORES'
              Sections:
                s_3_1_1_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_personas_mayores:
                  ID: GN-SEC-0053
                  Title: >-
                    3.1.1.1. Reconocimiento y ejercicio de derechos débiles para
                    personas mayores
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-MAYORES-P01 Def: Baja valoración social
                    y violación de derechos de personas mayores. Ex: - Maltrato.
                    - Abandono. - Discriminación.
            s_3_1_2_personas_con_discapacidad:
              ID: GN-SEC-0054
              Title: 3.1.2. Personas con Discapacidad
              Content: 'ID: STS-PS-CH-GRUPOS-DISCAPACIDAD'
              Sections:
                s_3_1_2_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_personas_con_disca:
                  ID: GN-SEC-0055
                  Title: >-
                    3.1.2.1. Reconocimiento y ejercicio de derechos débiles para
                    personas con discapacidad/dependencia
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-DISCAPACIDAD-P01 Def: Baja valoración
                    social y violación de derechos de personas en situación de
                    discapacidad o dependencia funcional. Ex: - Maltrato. -
                    Abandono. - Discriminación.
            s_3_1_3_personas_en_situacion_de_calle:
              ID: GN-SEC-0056
              Title: 3.1.3. Personas en Situación de Calle
              Content: 'ID: STS-PS-CH-GRUPOS-CALLE'
              Sections:
                s_3_1_3_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_personas_en_situac:
                  ID: GN-SEC-0057
                  Title: >-
                    3.1.3.1. Reconocimiento y ejercicio de derechos débiles para
                    personas en situación de calle
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-CALLE-P01 Def: Baja valoración social y
                    violación de derechos de personas en situación de calle. Ex:
                    - Maltrato. - Abandono. - Discriminación.
            s_3_1_4_pueblos_indigenas:
              ID: GN-SEC-0058
              Title: 3.1.4. Pueblos Indígenas
              Content: 'ID: STS-PS-CH-GRUPOS-INDIGENAS'
              Sections:
                s_3_1_4_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_pueblos_indigenas:
                  ID: GN-SEC-0059
                  Title: >-
                    3.1.4.1. Reconocimiento y ejercicio de derechos débiles para
                    pueblos indígenas
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-INDIGENAS-P01 Def: Baja valoración
                    social y violación de derechos de pueblos indígenas. Ex: -
                    Falta de reconocimiento constitucional. - Maltrato. -
                    Discriminación.
            s_3_1_5_personas_lgbti:
              ID: GN-SEC-0060
              Title: 3.1.5. Personas LGBTI+
              Content: 'ID: STS-PS-CH-GRUPOS-LGBTI'
              Sections:
                s_3_1_5_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_personas_lgbti:
                  ID: GN-SEC-0061
                  Title: >-
                    3.1.5.1. Reconocimiento y ejercicio de derechos débiles para
                    personas LGBTI+
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-LGBTI-P01 Def: Baja valoración social y
                    violación de derechos de personas LGBTI+. Ex: - Maltrato. -
                    Abandono. - Desconocimiento de género en registros. -
                    Discriminación.
            s_3_1_6_personas_migrantes:
              ID: GN-SEC-0062
              Title: 3.1.6. Personas Migrantes
              Content: 'ID: STS-PS-CH-GRUPOS-MIGRANTES'
              Sections:
                s_3_1_6_1_reconocimiento_y_ejercicio_de_derechos_debiles_para_personas_migrantes:
                  ID: GN-SEC-0063
                  Title: >-
                    3.1.6.1. Reconocimiento y ejercicio de derechos débiles para
                    personas migrantes
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-MIGRANTES-P01 Def: Baja valoración
                    social y violación de derechos de personas migrantes. Ex: -
                    Falta de institucionalidad migratoria. - Maltrato. -
                    Discriminación.
            s_3_1_7_mujeres:
              ID: GN-SEC-0064
              Title: 3.1.7. Mujeres
              Content: 'ID: STS-PS-CH-GRUPOS-MUJERES'
              Sections:
                s_3_1_7_1_violencia_y_discriminacion_contra_la_mujer:
                  ID: GN-SEC-0065
                  Title: 3.1.7.1. Violencia y discriminación contra la mujer
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-MUJERES-P01 Def: Violencia sufrida por
                    mujeres y falta de acompañamiento y protección a las
                    víctimas.
                s_3_1_7_2_bajo_empoderamiento_y_ejercicio_de_derechos_de_las_mujeres:
                  ID: GN-SEC-0066
                  Title: >-
                    3.1.7.2. Bajo empoderamiento y ejercicio de derechos de las
                    mujeres
                  Content: >-
                    ID: STS-PS-CH-GRUPOS-MUJERES-P02 Def: Brecha en
                    empoderamiento e igualdad de derechos entre mujeres y
                    hombres. Ctx: Inclusiones. - Desigual distribución de
                    labores de cuidado. - Trabajo no remunerado.
    s_4_justicia_y_derechos_humanos:
      ID: GN-SEC-0067
      Title: 4. Justicia y Derechos Humanos
      Content: 'ID: STS-PS-CH-JUSTICIA'
      Sections:
        s_4_1_derechos_humanos:
          ID: GN-SEC-0068
          Title: 4.1. Derechos Humanos
          Content: 'ID: STS-PS-CH-JUSTICIA-DDHH'
          Sections:
            s_4_1_1_proteccion_y_acompanamiento_insuficientes_a_personas_vulneradas_en_sus_d:
              ID: GN-SEC-0069
              Title: >-
                4.1.1. Protección y acompañamiento insuficientes a personas
                vulneradas en sus derechos
              Content: >-
                ID: STS-PS-CH-JUSTICIA-DDHH-P01 Def: Carencia de soporte legal y
                no legal durante procesos (judiciales, policiales, psicológicos,
                cambios de vida) para personas vulneradas.
            s_4_1_2_reparacion_insuficiente_por_violacion_de_ddhh:
              ID: GN-SEC-0070
              Title: 4.1.2. Reparación insuficiente por violación de DDHH
              Content: >-
                ID: STS-PS-CH-JUSTICIA-DDHH-P02 Def: Carencia de mecanismos
                efectivos para la reparación de violaciones a los derechos
                humanos. Ctx: Mecanismos. - Justicia. - Institucionalidad. -
                Acciones concretas.
            s_4_1_3_proteccion_promocion_y_difusion_insuficientes_de_los_ddhh:
              ID: GN-SEC-0071
              Title: >-
                4.1.3. Protección, promoción y difusión insuficientes de los
                DDHH
              Content: >-
                ID: STS-PS-CH-JUSTICIA-DDHH-P03 Def: Necesidad de promover,
                proteger y difundir activamente los derechos fundamentales de
                todas las personas.
        s_4_2_sistema_judicial:
          ID: GN-SEC-0072
          Title: 4.2. Sistema Judicial
          Content: 'ID: STS-PS-CH-JUSTICIA-SISTEMA'
          Sections:
            s_4_2_1_acceso_dificil_y_discriminatorio_al_sistema_de_justicia:
              ID: GN-SEC-0073
              Title: 4.2.1. Acceso difícil y discriminatorio al sistema de justicia
              Content: >-
                ID: STS-PS-CH-JUSTICIA-SISTEMA-P01 Def: Barreras de acceso o
                déficit de representación en procedimientos judiciales. Cpt:
                Característica-Problema. - Sistema no oportuno. - Ineficiente. -
                Poco transparente. - Sesgado contra ciertos grupos.
            s_4_2_2_carencia_de_informacion_pericial_oportuna_para_el_sistema_judicial:
              ID: GN-SEC-0074
              Title: >-
                4.2.2. Carencia de información pericial oportuna para el sistema
                judicial
              Content: >-
                ID: STS-PS-CH-JUSTICIA-SISTEMA-P02 Def: Falta de insumos
                periciales necesarios para el desarrollo adecuado de las causas
                judiciales.
        s_4_3_sistema_penitenciario:
          ID: GN-SEC-0075
          Title: 4.3. Sistema Penitenciario
          Content: 'ID: STS-PS-CH-JUSTICIA-CARCEL'
          Sections:
            s_4_3_1_vulneracion_de_derechos_y_malas_condiciones_de_vida_de_poblacion_privada:
              ID: GN-SEC-0076
              Title: >-
                4.3.1. Vulneración de derechos y malas condiciones de vida de
                población privada de libertad
              Content: >-
                ID: STS-PS-CH-JUSTICIA-CARCEL-P01 Def: Violación de derechos y
                condiciones de vida precarias dentro del sistema penitenciario.
                Ctx: Alcance. - Privación de libertad total. - Condenas
                parciales.
            s_4_3_2_sistema_carcelario_y_gendarmeria_no_modernizados:
              ID: GN-SEC-0077
              Title: 4.3.2. Sistema carcelario y Gendarmería no modernizados
              Content: >-
                ID: STS-PS-CH-JUSTICIA-CARCEL-P02 Def: Necesidad de
                modernización institucional del sistema penitenciario y de
                profesionalización/capacitación de Gendarmería.
            s_4_3_3_insercion_y_reinsercion_social_deficientes_de_personas_en_conflicto_con_:
              ID: GN-SEC-0078
              Title: >-
                4.3.3. Inserción y reinserción social deficientes de personas en
                conflicto con la ley
              Content: >-
                ID: STS-PS-CH-JUSTICIA-CARCEL-P03 Def: Fallas en los procesos de
                inserción/reinserción social para adolescentes y adultos en
                conflicto con la ley o con alto riesgo sociodelictual.
    s_5_cultura_y_patrimonio:
      ID: GN-SEC-0079
      Title: 5. Cultura y Patrimonio
      Content: 'ID: STS-PS-CH-CULTURA'
      Sections:
        s_5_1_fomento_y_desarrollo:
          ID: GN-SEC-0080
          Title: 5.1. Fomento y Desarrollo
          Content: 'ID: STS-PS-CH-CULTURA-FOMENTO'
          Sections:
            s_5_1_1_valorizacion_transmision_y_revitalizacion_insuficientes_de_culturas_y_ar:
              ID: GN-SEC-0081
              Title: >-
                5.1.1. Valorización, transmisión y revitalización insuficientes
                de culturas y artes
              Content: >-
                ID: STS-PS-CH-CULTURA-FOMENTO-P01 Def: Carencia de acciones para
                valorar, transmitir o revitalizar culturas y artes. Ex: -
                Artistas nacionales (visibilidad nacional/internacional). -
                Prácticas culturales de comunidades. - Lenguas en desuso.
            s_5_1_2_proteccion_y_valorizacion_insuficientes_del_patrimonio:
              ID: GN-SEC-0082
              Title: 5.1.2. Protección y valorización insuficientes del patrimonio
              Content: >-
                ID: STS-PS-CH-CULTURA-FOMENTO-P02 Def: Necesidad de protección,
                salvaguardia, gestión y valorización del patrimonio cultural y/o
                natural. Ctx: Inclusiones. - Capacidades institucionales
                (recursos, técnica) para cumplir esta función.
            s_5_1_3_apoyo_insuficiente_al_desarrollo_de_artistas_y_agentes_culturales:
              ID: GN-SEC-0083
              Title: >-
                5.1.3. Apoyo insuficiente al desarrollo de artistas y agentes
                culturales
              Content: >-
                ID: STS-PS-CH-CULTURA-FOMENTO-P03 Def: Carencia de educación
                especializada, reconocimiento de escuelas artísticas y apoyo
                para el desarrollo de artistas.
        s_5_2_acceso:
          ID: GN-SEC-0084
          Title: 5.2. Acceso
          Content: 'ID: STS-PS-CH-CULTURA-ACCESO'
          Sections:
            s_5_2_1_acceso_desigual_a_manifestaciones_culturales_y_artisticas:
              ID: GN-SEC-0085
              Title: 5.2.1. Acceso desigual a manifestaciones culturales y artísticas
              Content: >-
                ID: STS-PS-CH-CULTURA-ACCESO-P01 Def: Desigualdad en acceso,
                acercamiento y/o participación en arte y cultura. Ex: -
                Expresiones artísticas. - Espacios de muestra. - Exposiciones.
            s_5_2_2_acceso_desigual_al_patrimonio_natural_y_o_cultural:
              ID: GN-SEC-0086
              Title: 5.2.2. Acceso desigual al patrimonio natural y/o cultural
              Content: >-
                ID: STS-PS-CH-CULTURA-ACCESO-P02 Def: Desigualdad en acceso,
                acercamiento y/o participación en el patrimonio. Cpt:
                Tipo-Patrimonio. - Cultural (material/inmaterial). -
                Histórico-cultural. - Natural.
            s_5_2_3_acceso_desigual_a_formacion_en_culturas_artes_y_o_patrimonio:
              ID: GN-SEC-0087
              Title: >-
                5.2.3. Acceso desigual a formación en culturas, artes y/o
                patrimonio
              Content: >-
                ID: STS-PS-CH-CULTURA-ACCESO-P03 Def: Precariedad y/o
                desigualdad en procesos formativos (todas las edades) a través
                del arte y/o cultura. Ctx: Inclusiones. - Escasez de espacios de
                creación y desarrollo de expresiones artísticas/culturales.
            s_5_2_4_acceso_reducido_de_la_ciudadania_al_libro_y_la_lectura:
              ID: GN-SEC-0088
              Title: 5.2.4. Acceso reducido de la ciudadanía al libro y la lectura
              Content: >-
                ID: STS-PS-CH-CULTURA-ACCESO-P04 Def: Acceso reducido y/o
                desigual al libro en todos sus formatos y soportes para todas
                las edades.
    s_6_seguridad_publica:
      ID: GN-SEC-0089
      Title: 6. Seguridad Pública
      Content: 'ID: STS-PS-CH-SEGURIDAD'
      Sections:
        s_6_1_prevencion_y_sistema:
          ID: GN-SEC-0090
          Title: 6.1. Prevención y Sistema
          Content: 'ID: STS-PS-CH-SEGURIDAD-SISTEMA'
          Sections:
            s_6_1_1_mecanismos_de_prevencion_del_delito_deficientes:
              ID: GN-SEC-0091
              Title: 6.1.1. Mecanismos de prevención del delito deficientes
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-SISTEMA-P01 Def: Fallas en la prevención
                temprana del delito. Cpt: Enfoque-Persona. - Def: No se reducen
                factores de riesgo que causan comportamientos delictivos. Cpt:
                Enfoque-Organización. - Def: No se generan sistemas de
                información para elaborar planes de prevención.
            s_6_1_2_protocolos_de_detencion_y_procedimientos_policiales_judiciales_deficient:
              ID: GN-SEC-0092
              Title: >-
                6.1.2. Protocolos de detención y procedimientos
                policiales/judiciales deficientes
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-SISTEMA-P02 Def: Protocolos y
                procedimientos defectuosos en la actuación de fuerzas policiales
                y judiciales durante detenciones y otras acciones.
        s_6_2_victimas_y_percepcion:
          ID: GN-SEC-0093
          Title: 6.2. Víctimas y Percepción
          Content: 'ID: STS-PS-CH-SEGURIDAD-VICTIMAS'
          Sections:
            s_6_2_1_apoyo_y_tratamiento_insuficientes_para_victimas_de_violencia_y_denuncian:
              ID: GN-SEC-0094
              Title: >-
                6.2.1. Apoyo y tratamiento insuficientes para víctimas de
                violencia (y denunciantes)
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-VICTIMAS-P01 Def: Víctimas de delitos
                violentos sufren consecuencias negativas (psicológicas,
                sociales, jurídicas) sin apoyo y tratamiento adecuados. Ctx:
                Inclusiones. - Falta de apoyo a denunciantes. - Falta de
                mecanismos de denuncia protegida (ej. anónima).
            s_6_2_2_alta_percepcion_de_inseguridad_en_la_poblacion:
              ID: GN-SEC-0095
              Title: 6.2.2. Alta percepción de inseguridad en la población
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-VICTIMAS-P02 Def: Ocurrencia recurrente
                de situaciones que ponen en riesgo la seguridad de la población.
                Cpt: Indicador. - Ctx: Pobreza Multidimensional. - Def:
                Percepción de inseguridad.
        s_6_3_delincuencia_compleja:
          ID: GN-SEC-0096
          Title: 6.3. Delincuencia Compleja
          Content: 'ID: STS-PS-CH-SEGURIDAD-CRIMEN'
          Sections:
            s_6_3_1_abordaje_insuficiente_del_crimen_organizado_y_narcotrafico:
              ID: GN-SEC-0097
              Title: >-
                6.3.1. Abordaje insuficiente del crimen organizado y
                narcotráfico
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-CRIMEN-P01 Def: Carencia de políticas
                públicas, coordinación y organización de acciones para combatir
                todas las formas de crimen organizado y narcotráfico.
        s_6_4_tenencia_de_animales:
          ID: GN-SEC-0098
          Title: 6.4. Tenencia de Animales
          Content: 'ID: STS-PS-CH-SEGURIDAD-ANIMALES'
          Sections:
            s_6_4_1_baja_cultura_de_tenencia_responsable_de_animales:
              ID: GN-SEC-0099
              Title: 6.4.1. Baja cultura de tenencia responsable de animales
              Content: >-
                ID: STS-PS-CH-SEGURIDAD-ANIMALES-P01 Def: Baja formación de la
                población en tenencia responsable de mascotas y animales de
                compañía. Ctx: Inclusiones. - Acceso insuficiente a servicios
                veterinarios, vacunación, esterilización, identificación de
                animales.
    s_7_gobernanza_y_estado:
      ID: GN-SEC-0100
      Title: 7. Gobernanza y Estado
      Content: 'ID: STS-PS-CH-GOBERNANZA'
      Sections:
        s_7_1_relaciones_internacionales:
          ID: GN-SEC-0101
          Title: 7.1. Relaciones Internacionales
          Content: 'ID: STS-PS-CH-GOBERNANZA-RRII'
          Sections:
            s_7_1_1_relaciones_internacionales_e_imagen_pais_debiles:
              ID: GN-SEC-0102
              Title: 7.1.1. Relaciones internacionales e imagen país débiles
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-RRII-P01 Def: Escasa relación
                internacional y política exterior del país. Posicionamiento
                internacional y/o imagen país débiles.
            s_7_1_2_apoyo_insuficiente_a_connacionales_en_el_exterior:
              ID: GN-SEC-0103
              Title: 7.1.2. Apoyo insuficiente a connacionales en el exterior
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-RRII-P02 Def: Falta de apoyo,
                protección y asistencia consular adecuada a chilenos residentes
                en el extranjero.
        s_7_2_sistema_democratico_y_participacion:
          ID: GN-SEC-0104
          Title: 7.2. Sistema Democrático y Participación
          Content: 'ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA'
          Sections:
            s_7_2_1_baja_confianza_en_instituciones_politicas_y_partidos:
              ID: GN-SEC-0105
              Title: 7.2.1. Baja confianza en instituciones políticas y partidos
              Content: |-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P01
                Def: Baja confianza ciudadana en instituciones políticas.
                Cause:
                - Percepción de corrupción.
                - Falta de transparencia.
                - Desconfianza en cumplimiento de promesas.
            s_7_2_2_desconexion_entre_instituciones_democraticas_y_ciudadania:
              ID: GN-SEC-0106
              Title: 7.2.2. Desconexión entre instituciones democráticas y ciudadanía
              Content: |-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P02
                Def: Comunicación deficiente entre el gobierno y la ciudadanía.
            s_7_2_3_bajo_involucramiento_y_participacion_social_de_la_poblacion:
              ID: GN-SEC-0107
              Title: >-
                7.2.3. Bajo involucramiento y participación social de la
                población
              Content: |-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P03
                Def: Bajo acceso a acciones de participación ciudadana.
                Ex:
                - Acceso no efectivo al voto para ciertas poblaciones.
                - Baja participación política (mujeres, indígenas).
                - Baja participación comunitaria.
                - Carencia de formación en liderazgo.
                - Bajo involucramiento social.
            s_7_2_4_ausencia_de_educacion_civica:
              ID: GN-SEC-0108
              Title: 7.2.4. Ausencia de educación cívica
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P04 Def: Bajo desarrollo y
                formación ciudadana en la población general de todas las edades.
            s_7_2_5_organizaciones_de_la_sociedad_civil_osc_debiles:
              ID: GN-SEC-0109
              Title: 7.2.5. Organizaciones de la sociedad civil (OSC) débiles
              Content: |-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P05
                Def: Falta de desarrollo y/o fortalecimiento de las OSC.
                Ctx: Áreas.
                - Gestión.
                - Planificación.
                - Financiamiento.
                - Asociatividad.
            s_7_2_6_relacion_inestable_o_deficiente_entre_poderes_del_estado:
              ID: GN-SEC-0110
              Title: 7.2.6. Relación inestable o deficiente entre poderes del Estado
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-DEMOCRACIA-P06 Def: Funcionamiento no
                óptimo o inestable en la relación entre los poderes ejecutivo,
                legislativo y judicial.
        s_7_3_gestion_publica:
          ID: GN-SEC-0111
          Title: 7.3. Gestión Pública
          Content: 'ID: STS-PS-CH-GOBERNANZA-GESTION'
          Sections:
            s_7_3_1_falta_de_probidad_transparencia_e_integridad_en_la_funcion_publica:
              ID: GN-SEC-0112
              Title: >-
                7.3.1. Falta de probidad, transparencia e integridad en la
                función pública
              Content: |-
                ID: STS-PS-CH-GOBERNANZA-GESTION-P01
                Def: Necesidad de sistemas de integridad más robustos.
                Req:
                - Asegurar probidad.
                - Prevenir/combatir corrupción.
                - Evitar conflictos de interés.
                - Fomentar transparencia activa.
            s_7_3_2_capacidad_estatal_deficiente_en_gestion_y_fiscalizacion:
              ID: GN-SEC-0113
              Title: 7.3.2. Capacidad estatal deficiente en gestión y fiscalización
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-GESTION-P02 Def: Problemas de alta
                burocracia (inter-servicios y atención a público) y baja
                modernización general. Ctx: Inclusiones. - Deficiencias en
                capacidades regulatorias, fiscalización, gestión de procesos.
            s_7_3_3_administracion_ineficiente_de_los_recursos_del_estado:
              ID: GN-SEC-0114
              Title: 7.3.3. Administración ineficiente de los recursos del Estado
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-GESTION-P03 Def: Gestión y
                administración ineficaz de bienes, servicios e infraestructuras
                públicas, y propiedad fiscal. Ctx: Inclusiones. - Administración
                de recursos humanos del Estado, no solo económicos.
        s_7_4_finanzas_publicas:
          ID: GN-SEC-0115
          Title: 7.4. Finanzas Públicas
          Content: 'ID: STS-PS-CH-GOBERNANZA-FINANZAS'
          Sections:
            s_7_4_1_fiscalizacion_y_recaudacion_a_contribuyentes_deficiente:
              ID: GN-SEC-0116
              Title: 7.4.1. Fiscalización y recaudación a contribuyentes deficiente
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-FINANZAS-P01 Def: Baja capacidad del
                Fisco para recaudar y fiscalizar la recaudación fiscal.
            s_7_4_2_incremento_de_acciones_legales_contra_el_fisco:
              ID: GN-SEC-0117
              Title: 7.4.2. Incremento de acciones legales contra el Fisco
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-FINANZAS-P02 Def: Alto número de
                demandas buscando compensación económica del Fisco. Req: Cubrir
                esta demanda de forma eficaz y con soluciones colaborativas.
            s_7_4_3_actividades_irregulares_que_atentan_contra_recaudacion_fiscal_y_buen_gas:
              ID: GN-SEC-0118
              Title: >-
                7.4.3. Actividades irregulares que atentan contra recaudación
                fiscal y buen gasto público
              Content: >-
                ID: STS-PS-CH-GOBERNANZA-FINANZAS-P03 Def: Existencia de
                acciones (algunas ilegales) que afectan la recaudación fiscal o
                la eficiencia del gasto público.
    s_8_medioambiente_y_energia:
      ID: GN-SEC-0119
      Title: 8. Medioambiente y Energía
      Content: 'ID: STS-PS-CH-MA'
      Sections:
        s_8_1_cambio_climatico_y_degradacion:
          ID: GN-SEC-0120
          Title: 8.1. Cambio Climático y Degradación
          Content: 'ID: STS-PS-CH-MA-CLIMATICO'
          Sections:
            s_8_1_1_alta_emision_de_gases_de_efecto_invernadero_gei:
              ID: GN-SEC-0121
              Title: 8.1.1. Alta emisión de gases de efecto invernadero (GEI)
              Content: >-
                ID: STS-PS-CH-MA-CLIMATICO-P01 Def: Emisión elevada de GEI por
                actividades humanas, causando daño a ecosistemas. Cause: -
                Actividad económica. - Combustión de fósiles. - Deforestación. -
                Erosión del suelo. - Crianza animal.
            s_8_1_2_sequia_y_escasez_hidrica:
              ID: GN-SEC-0122
              Title: 8.1.2. Sequía y escasez hídrica
              Content: >-
                ID: STS-PS-CH-MA-CLIMATICO-P02 Def: Períodos de sequía y escasez
                hídrica en territorios, con riesgo de déficit estructural de
                agua.
            s_8_1_3_deforestacion_y_degradacion_forestal:
              ID: GN-SEC-0123
              Title: 8.1.3. Deforestación y degradación forestal
              Content: |-
                ID: STS-PS-CH-MA-CLIMATICO-P03
                Def: Pérdida y/o degradación de bosques por actividades humanas.
                Cause:
                - Explotación de recursos naturales y patrimonio.
                Cpt: Impacto.
                - Directo en el cambio climático.
            s_8_1_4_desertificacion_degradacion_del_suelo_y_desplazamiento_agroclimatico:
              ID: GN-SEC-0124
              Title: >-
                8.1.4. Desertificación, degradación del suelo y desplazamiento
                agroclimático
              Content: >-
                ID: STS-PS-CH-MA-CLIMATICO-P04 Def: Riesgo de desertificación
                y/o degradación del suelo en territorios. Res: - Cambios en el
                potencial agrícola. - Desplazamiento de zonas agrícolas.
            s_8_1_5_degradacion_de_ecosistemas_terrestres_y_oceanicos:
              ID: GN-SEC-0125
              Title: 8.1.5. Degradación de ecosistemas terrestres y oceánicos
              Content: >-
                ID: STS-PS-CH-MA-CLIMATICO-P05 Def: Pérdida de biodiversidad y
                degradación/alteración de ecosistemas. Cause: Manejo poco
                sustentable de recursos.
            s_8_1_6_existencia_de_zonas_de_sacrificio_medioambiental:
              ID: GN-SEC-0126
              Title: 8.1.6. Existencia de zonas de sacrificio medioambiental
              Content: >-
                ID: STS-PS-CH-MA-CLIMATICO-P06 Def: Zonas con exposición
                desproporcionada a actividades productivas contaminantes,
                generando desigualdades en el impacto ambiental. Ex: - Plantas
                termoeléctricas. - Relaves mineros. - Basureros.
        s_8_2_gestion_ambiental:
          ID: GN-SEC-0127
          Title: 8.2. Gestión Ambiental
          Content: 'ID: STS-PS-CH-MA-GESTION'
          Sections:
            s_8_2_1_falta_de_preparacion_y_respuesta_ante_desastres_naturales_y_antropicos:
              ID: GN-SEC-0128
              Title: >-
                8.2.1. Falta de preparación y respuesta ante desastres naturales
                y antrópicos
              Content: >-
                ID: STS-PS-CH-MA-GESTION-P01 Def: Insuficiente preparación y
                capacidad de respuesta frente a desastres. Ex: Naturales. -
                Terremotos, tsunamis, inundaciones, aluviones, erupciones, mega
                sequía. Ex: Antrópicos. - Incendios.
            s_8_2_2_prevencion_proteccion_y_o_conservacion_del_medioambiente_ausentes_o_insu:
              ID: GN-SEC-0129
              Title: >-
                8.2.2. Prevención, protección y/o conservación del medioambiente
                ausentes o insuficientes
              Content: |-
                ID: STS-PS-CH-MA-GESTION-P02
                Def: Escasa protección efectiva del medioambiente.
                Cause:
                - Capacidades institucionales limitadas.
                - Marco regulatorio débil.
                - Falta de adopción de prácticas productivas sustentables.
            s_8_2_3_contaminacion_atmosferica_y_o_manejo_inadecuado_de_residuos_solidos:
              ID: GN-SEC-0130
              Title: >-
                8.2.3. Contaminación atmosférica y/o manejo inadecuado de
                residuos sólidos
              Content: >-
                ID: STS-PS-CH-MA-GESTION-P03 Def: Problemas en el retiro,
                disposición y tratamiento de residuos sólidos. Ctx: Inclusiones.
                - Reciclaje. - Contaminación del aire.
        s_8_3_energia:
          ID: GN-SEC-0131
          Title: 8.3. Energía
          Content: 'ID: STS-PS-CH-MA-ENERGIA'
          Sections:
            s_8_3_1_ineficiencia_energetica_en_sectores_de_consumo:
              ID: GN-SEC-0132
              Title: 8.3.1. Ineficiencia energética en sectores de consumo
              Content: >-
                ID: STS-PS-CH-MA-ENERGIA-P01 Def: Zonas, industrias u hogares
                que no cuentan con tecnologías de eficiencia energética. Ctx:
                Sectores. - Residencial. - Industrial. - Otros.
            s_8_3_2_bajo_desarrollo_produccion_y_o_uso_de_energias_renovables:
              ID: GN-SEC-0133
              Title: >-
                8.3.2. Bajo desarrollo, producción y/o uso de energías
                renovables
              Content: >-
                ID: STS-PS-CH-MA-ENERGIA-P02 Def: Insuficiente desarrollo,
                producción y uso de energía desde fuentes renovables.
            s_8_3_3_bajo_desarrollo_produccion_y_o_uso_de_energias_limpias:
              ID: GN-SEC-0134
              Title: '8.3.3. Bajo desarrollo, producción y/o uso de energías limpias'
              Content: >-
                ID: STS-PS-CH-MA-ENERGIA-P03 Def: Insuficiente desarrollo y uso
                de energía desde fuentes limpias. Ex: Transporte.
            s_8_3_4_problemas_de_transmision_de_energia_en_el_territorio:
              ID: GN-SEC-0135
              Title: 8.3.4. Problemas de transmisión de energía en el territorio
              Content: |-
                ID: STS-PS-CH-MA-ENERGIA-P04
                Def: Territorios con bajo suministro de energía.
                Cause:
                - Falta de canales de transmisión.
                - Altos costos de transmisión.
    s_9_mercado_laboral:
      ID: GN-SEC-0136
      Title: 9. Mercado Laboral
      Content: 'ID: STS-PS-CH-LABORAL'
      Sections:
        s_9_1_derechos_y_participacion:
          ID: GN-SEC-0137
          Title: 9.1. Derechos y Participación
          Content: 'ID: STS-PS-CH-LABORAL-DERECHOS'
          Sections:
            s_9_1_1_baja_tasa_de_sindicalizacion_y_formacion_sindical:
              ID: GN-SEC-0138
              Title: 9.1.1. Baja tasa de sindicalización y formación sindical
              Content: >-
                ID: STS-PS-CH-LABORAL-DERECHOS-P01 Def: Baja tasa de
                sindicalización, escasas instancias de diálogo social
                empleador-sindicato, escasa formación en habilidades sindicales.
                Ctx: Inclusiones. - Falta de desarrollo gremial y asociación
                entre trabajadores.
            s_9_1_2_bajo_conocimiento_de_derechos_laborales:
              ID: GN-SEC-0139
              Title: 9.1.2. Bajo conocimiento de derechos laborales
              Content: >-
                ID: STS-PS-CH-LABORAL-DERECHOS-P02 Def: Desconocimiento general
                de la población sobre sus derechos laborales.
        s_9_2_empleo_y_empleabilidad:
          ID: GN-SEC-0140
          Title: 9.2. Empleo y Empleabilidad
          Content: 'ID: STS-PS-CH-LABORAL-EMPLEO'
          Sections:
            s_9_2_1_baja_participacion_laboral_y_o_desempleo:
              ID: GN-SEC-0141
              Title: 9.2.1. Baja participación laboral y/o desempleo
              Content: >-
                ID: STS-PS-CH-LABORAL-EMPLEO-P01 Def: Baja participación en la
                fuerza de trabajo y baja tasa de ocupación de la población
                activa.
            s_9_2_2_baja_empleabilidad:
              ID: GN-SEC-0142
              Title: 9.2.2. Baja empleabilidad
              Content: >-
                ID: STS-PS-CH-LABORAL-EMPLEO-P02 Def: Insuficientes capacidades
                laborales (técnicas y blandas) de las personas para lograr una
                inserción laboral efectiva.
            s_9_2_3_bajo_emprendimiento:
              ID: GN-SEC-0143
              Title: 9.2.3. Bajo emprendimiento
              Content: >-
                ID: STS-PS-CH-LABORAL-EMPLEO-P03 Def: Bajo nivel de desarrollo y
                sostenibilidad de emprendimientos. Cause: - Dificultad acceso a
                financiamiento. - Falta de capacidades. - Iniciativas
                precarias/estacionales. - Problemas de formalización.
            s_9_2_4_necesidad_de_educacion_continua:
              ID: GN-SEC-0144
              Title: 9.2.4. Necesidad de educación continua
              Content: >-
                ID: STS-PS-CH-LABORAL-EMPLEO-P04 Def: Bajo acceso a instancias
                de aprendizaje y desarrollo de competencias (laborales,
                técnicas, transversales) y escasez de capital humano avanzado.
            s_9_2_5_falta_de_mecanismos_para_certificacion_de_competencias:
              ID: GN-SEC-0145
              Title: 9.2.5. Falta de mecanismos para certificación de competencias
              Content: >-
                ID: STS-PS-CH-LABORAL-EMPLEO-P05 Def: Inexistencia de
                reconocimiento formal para competencias laborales u otras
                capacidades.
        s_9_3_condiciones_laborales:
          ID: GN-SEC-0146
          Title: 9.3. Condiciones Laborales
          Content: 'ID: STS-PS-CH-LABORAL-CONDICIONES'
          Sections:
            s_9_3_1_bajos_salarios:
              ID: GN-SEC-0147
              Title: 9.3.1. Bajos salarios
              Content: >-
                ID: STS-PS-CH-LABORAL-CONDICIONES-P01 Def: Salarios
                insuficientes para cubrir necesidades básicas y superar la
                pobreza. Ctx: Inclusiones. - Brechas salariales entre distintos
                grupos de población.
            s_9_3_2_alta_rotacion_e_inestabilidad_laboral:
              ID: GN-SEC-0148
              Title: 9.3.2. Alta rotación e inestabilidad laboral
              Content: >-
                ID: STS-PS-CH-LABORAL-CONDICIONES-P02 Def: Irregularidad en
                trayectorias laborales, baja permanencia, trabajos temporales o
                a tiempo parcial.
            s_9_3_3_baja_formalizacion_del_mercado_laboral:
              ID: GN-SEC-0149
              Title: 9.3.3. Baja formalización del mercado laboral
              Content: |-
                ID: STS-PS-CH-LABORAL-CONDICIONES-P03
                Def: Alta proporción de personas trabajando en la informalidad.
            s_9_3_4_condiciones_de_trabajo_precarias:
              ID: GN-SEC-0150
              Title: 9.3.4. Condiciones de trabajo precarias
              Content: |-
                ID: STS-PS-CH-LABORAL-CONDICIONES-P04
                Def: Deficiencias en condiciones laborales.
                Ctx: Áreas.
                - Horarios.
                - Seguridad laboral.
                - Condiciones del lugar.
                - Higiene.
                - Otros factores.
            s_9_3_5_adaptacion_deficiente_a_automatizacion_y_nuevas_tecnologias:
              ID: GN-SEC-0151
              Title: >-
                9.3.5. Adaptación deficiente a automatización y nuevas
                tecnologías
              Content: >-
                ID: STS-PS-CH-LABORAL-CONDICIONES-P05 Def: Impacto negativo de
                la automatización/digitalización y poca adaptación de
                empresas/organizaciones a estos cambios.
    s_10_seguridad_social:
      ID: GN-SEC-0152
      Title: 10. Seguridad Social
      Content: 'ID: STS-PS-CH-SEGSOC'
      Sections:
        s_10_1_pensiones:
          ID: GN-SEC-0153
          Title: 10.1. Pensiones
          Content: 'ID: STS-PS-CH-SEGSOC-PENSIONES'
          Sections:
            s_10_1_1_bajas_pensiones:
              ID: GN-SEC-0154
              Title: 10.1.1. Bajas pensiones
              Content: |-
                ID: STS-PS-CH-SEGSOC-PENSIONES-P01
                Def: Personas reciben pensiones insuficientes al jubilar.
                Cause:
                - Bajos salarios.
                - Irregularidad en trayectorias laborales.
                - Otras.
            s_10_1_2_baja_formacion_en_materia_previsional:
              ID: GN-SEC-0155
              Title: 10.1.2. Baja formación en materia previsional
              Content: >-
                ID: STS-PS-CH-SEGSOC-PENSIONES-P02 Def: Desconocimiento general
                de la población sobre el funcionamiento del sistema previsional,
                sus derechos, deberes y requisitos.
        s_10_2_proteccion_social:
          ID: GN-SEC-0156
          Title: 10.2. Protección Social
          Content: 'ID: STS-PS-CH-SEGSOC-PROTECCION'
          Sections:
            s_10_2_1_desproteccion_frente_al_desempleo:
              ID: GN-SEC-0157
              Title: 10.2.1. Desprotección frente al desempleo
              Content: >-
                ID: STS-PS-CH-SEGSOC-PROTECCION-P01 Def: Carencia de protección
                para trabajadores y sus familias durante períodos de cesantía.
            s_10_2_2_desproteccion_frente_a_la_invalidez:
              ID: GN-SEC-0158
              Title: 10.2.2. Desprotección frente a la invalidez
              Content: >-
                ID: STS-PS-CH-SEGSOC-PROTECCION-P02 Def: Vulnerabilidad
                económica de personas con discapacidad o capacidad disminuida.
            s_10_2_3_desproteccion_frente_a_la_sobrevivencia:
              ID: GN-SEC-0159
              Title: 10.2.3. Desprotección frente a la sobrevivencia
              Content: >-
                ID: STS-PS-CH-SEGSOC-PROTECCION-P03 Def: Vulnerabilidad
                económica de deudos de una persona fallecida o gastos excesivos
                para quienes se hacen cargo de procesos post-fallecimiento.
    s_11_economia_y_empresas:
      ID: GN-SEC-0160
      Title: 11. Economía y Empresas
      Content: 'ID: STS-PS-CH-ECONOMIA'
      Sections:
        s_11_1_consumidores_y_propiedad_intelectual:
          ID: GN-SEC-0161
          Title: 11.1. Consumidores y Propiedad Intelectual
          Content: 'ID: STS-PS-CH-ECONOMIA-CONSUMIDOR'
          Sections:
            s_11_1_1_desproteccion_de_los_derechos_del_consumidor:
              ID: GN-SEC-0162
              Title: 11.1.1. Desprotección de los derechos del consumidor
              Content: >-
                ID: STS-PS-CH-ECONOMIA-CONSUMIDOR-P01 Def: Consumidores en
                situación de inferioridad frente a grandes empresas. Cause: -
                Prácticas comerciales abusivas. - Falta de información para
                decisiones libres. - Mecanismos de reclamo ineficaces.
            s_11_1_2_falencias_en_el_resguardo_de_la_propiedad_industrial:
              ID: GN-SEC-0163
              Title: 11.1.2. Falencias en el resguardo de la Propiedad Industrial
              Content: >-
                ID: STS-PS-CH-ECONOMIA-CONSUMIDOR-P02 Def: Protección
                insuficiente del producto del intelecto humano (científico,
                literario, artístico, industrial).
        s_11_2_desarrollo_empresarial:
          ID: GN-SEC-0164
          Title: 11.2. Desarrollo Empresarial
          Content: 'ID: STS-PS-CH-ECONOMIA-EMPRESAS'
          Sections:
            s_11_2_1_baja_inversion_y_uso_de_nuevas_tecnologias_en_empresas:
              ID: GN-SEC-0165
              Title: 11.2.1. Baja inversión y uso de nuevas tecnologías en empresas
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P01 Def: Baja inversión y/o uso
                de tecnología en procesos productivos, gestión o negocio. Ctx:
                Inclusiones. - Todo tipo de tecnología, digital o no.
            s_11_2_2_acceso_bajo_a_instrumentos_financieros_para_empresas_mipymes:
              ID: GN-SEC-0166
              Title: >-
                11.2.2. Acceso bajo a instrumentos financieros para empresas
                (MIPYMES)
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P02 Def: Micro, pequeñas y
                medianas empresas con acceso bajo o de alto costo a instrumentos
                financieros. Ctx: Usos. - Capital de trabajo. - Inversiones. -
                Necesidades de corto plazo.
            s_11_2_3_baja_sostenibilidad_de_empresas_y_emprendimientos:
              ID: GN-SEC-0167
              Title: 11.2.3. Baja sostenibilidad de empresas y emprendimientos
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P03 Def: Empresas sin
                capacidades para sostener su negocio en el tiempo. Cause: -
                Falta de inversiones. - Capacidades técnicas. - Capital humano.
            s_11_2_4_barreras_en_la_creacion_de_empresas_y_negocios_nuevos:
              ID: GN-SEC-0168
              Title: 11.2.4. Barreras en la creación de empresas y negocios nuevos
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P04 Def: Obstáculos para la
                creación de nuevas actividades productivas o emprendimientos.
                Ex: - Bajo acceso o alto costo de financiamiento. - Barreras de
                entrada. - Falta de equipamiento. - Falta de apoyo técnico.
            s_11_2_5_dificultades_para_realizar_actividad_emprendedora:
              ID: GN-SEC-0169
              Title: 11.2.5. Dificultades para realizar actividad emprendedora
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P05 Def: Dificultades
                específicas del ecosistema emprendedor. Ex: - Falta de
                financiamiento para prototipos/validación comercial. -
                Ecosistema inmaduro (falta de mentoría, valoración de activos,
                co-work).
            s_11_2_6_baja_asociatividad_y_o_desarrollo_gremial_empresarial:
              ID: GN-SEC-0170
              Title: 11.2.6. Baja asociatividad y/o desarrollo gremial empresarial
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P06 Def: Baja gestión de
                empresas a través de redes, baja promoción de asociatividad y
                vinculación con canales de comercialización.
            s_11_2_7_bajas_tasas_de_innovacion_en_empresas:
              ID: GN-SEC-0171
              Title: 11.2.7. Bajas tasas de innovación en empresas
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P07 Def: Baja inversión y uso de
                I+D y nuevas tecnologías. Ctx: Inclusiones. - Tecnologías de
                comunicación, información, producción, transformación digital.
            s_11_2_8_baja_colaboracion_universidad_empresa:
              ID: GN-SEC-0172
              Title: 11.2.8. Baja colaboración universidad-empresa
              Content: >-
                ID: STS-PS-CH-ECONOMIA-EMPRESAS-P08 Def: Escasa colaboración
                entre universidades, centros de investigación, empresas y sector
                público. Ctx: Actividades. - Proyectos I+D aplicada,
                prototipaje, asesorías, talleres, etc. Ctx: Inclusiones. - Bajo
                fomento a la transformación en facultades para aportar a la
                innovación y el emprendimiento.
        s_11_3_competitividad_y_mercado:
          ID: GN-SEC-0173
          Title: 11.3. Competitividad y Mercado
          Content: 'ID: STS-PS-CH-ECONOMIA-MERCADO'
          Sections:
            s_11_3_1_existencia_de_comercio_y_actividades_productivas_ilegales_o_no_regulada:
              ID: GN-SEC-0174
              Title: >-
                11.3.1. Existencia de comercio y actividades productivas
                ilegales o no reguladas
              Content: >-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P01 Def: Actividades productivas
                y comerciales ilegales, no declaradas o no reglamentadas. Ex: -
                Pesca ilegal. - Comercio de especies amenazadas.
            s_11_3_2_alta_y_persistente_concentracion_de_recursos:
              ID: GN-SEC-0175
              Title: 11.3.2. Alta y persistente concentración de recursos
              Content: >-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P02 Def: Concentración de
                propiedad (empresas, tierra, etc.) y de mercado en grupos
                reducidos. Ctx: Inclusiones. - Barreras de entrada para nuevos
                competidores.
            s_11_3_3_ineficiencia_de_mercados_por_fallas_de_competencia:
              ID: GN-SEC-0176
              Title: 11.3.3. Ineficiencia de mercados por fallas de competencia
              Content: |-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P03
                Def: Mercados ineficientes por ausencia de libre competencia.
                Ex:
                - Prácticas colusorias.
                - Abuso de posición monopólica.
                - Barreras de entrada.
            s_11_3_4_baja_productividad:
              ID: GN-SEC-0177
              Title: 11.3.4. Baja productividad
              Content: |-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P04
                Def: Baja productividad de empresas y del sistema productivo.
                Cause:
                - Baja innovación.
                - Alta burocracia.
                - Otras.
            s_11_3_5_bajo_desarrollo_industrial:
              ID: GN-SEC-0178
              Title: 11.3.5. Bajo desarrollo industrial
              Content: |-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P05
                Def: Bajo desarrollo de ciertos sectores económicos.
                Cpt: Indicador.
                - Bajas exportaciones.
                - Baja contribución al PIB.
                - Pocos recursos para desarrollo.
                Ctx: Inclusiones.
                - Procesos y fortalecimiento de capacidades.
            s_11_3_6_baja_diversificacion_productiva:
              ID: GN-SEC-0179
              Title: 11.3.6. Baja diversificación productiva
              Content: >-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P06 Def: Matriz productiva del
                país poco diversificada, generando dependencia de pocas
                actividades económicas.
            s_11_3_7_bajo_numero_de_empresas_exportadoras:
              ID: GN-SEC-0180
              Title: 11.3.7. Bajo número de empresas exportadoras
              Content: >-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P07 Def: Número reducido de
                empresas que exportan o tienen bajo posicionamiento
                internacional. Cause: No cumplen requerimientos para acceder a
                mercados internacionales.
            s_11_3_8_nivel_comercial_debil:
              ID: GN-SEC-0181
              Title: 11.3.8. Nivel comercial débil
              Content: >-
                ID: STS-PS-CH-ECONOMIA-MERCADO-P08 Def: Problemas de
                posicionamiento económico-comercial de Chile en el exterior y
                posición competitiva débil.
    s_12_territorio_y_vivienda:
      ID: GN-SEC-0182
      Title: 12. Territorio y Vivienda
      Content: 'ID: STS-PS-CH-TERRITORIO'
      Sections:
        s_12_1_transporte_y_conectividad:
          ID: GN-SEC-0183
          Title: 12.1. Transporte y Conectividad
          Content: 'ID: STS-PS-CH-TERRITORIO-TRANSPORTE'
          Sections:
            s_12_1_1_problemas_de_movilidad_y_acceso_a_medios_de_transporte:
              ID: GN-SEC-0184
              Title: 12.1.1. Problemas de movilidad y acceso a medios de transporte
              Content: >-
                ID: STS-PS-CH-TERRITORIO-TRANSPORTE-P01 Def: Bajo desarrollo de
                la movilidad y conectividad de personas a través de servicios de
                transporte. Cpt: Característica-Problema. - Servicios no
                eficientes, inseguros, insostenibles o de baja calidad. Ctx:
                Alcance. - Aéreo, terrestre, marítimo. Ctx: Inclusiones. -
                Infraestructura (aeropuertos, estaciones, puertos).
            s_12_1_2_incumplimiento_de_normativas_de_transporte:
              ID: GN-SEC-0185
              Title: 12.1.2. Incumplimiento de normativas de transporte
              Content: >-
                ID: STS-PS-CH-TERRITORIO-TRANSPORTE-P02 Def: Incumplimiento de
                leyes y normativas en transporte aéreo, terrestre y marítimo
                (carga y pasajeros). Ctx: Inclusiones. - Inseguridad vial. -
                Conductas peligrosas.
            s_12_1_3_ineficiencias_y_externalidades_negativas_de_medios_de_transporte:
              ID: GN-SEC-0186
              Title: >-
                12.1.3. Ineficiencias y externalidades negativas de medios de
                transporte
              Content: |-
                ID: STS-PS-CH-TERRITORIO-TRANSPORTE-P03
                Def: Existencia de problemas derivados del transporte.
                Ex:
                - Tráfico.
                - Contaminación.
                - Tiempos de traslado.
                - Ruido.
            s_12_1_4_falta_de_conectividad_fisica_caminos_rutas:
              ID: GN-SEC-0187
              Title: '12.1.4. Falta de conectividad física (caminos, rutas)'
              Content: |-
                ID: STS-PS-CH-TERRITORIO-TRANSPORTE-P04
                Def: Dificultad de acceso al territorio o conectividad escasa.
                Cause:
                - Lejanía.
                - Falta de caminos.
                - Caminos de mala calidad.
                - Falta de pavimentación.
        s_12_2_vivienda_y_habitat:
          ID: GN-SEC-0188
          Title: 12.2. Vivienda y Hábitat
          Content: 'ID: STS-PS-CH-TERRITORIO-VIVIENDA'
          Sections:
            s_12_2_1_acceso_y_calidad_deficientes_de_servicios_basicos_en_vivienda:
              ID: GN-SEC-0189
              Title: >-
                12.2.1. Acceso y calidad deficientes de servicios básicos en
                vivienda
              Content: |-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P01
                Def: Dificultad de acceso a servicios básicos en la vivienda.
                Ex: Agua potable, alcantarillado, electricidad.
                Cpt: Indicador.
                - Ctx: Pobreza Multidimensional.
                - Def: Acceso a servicios básicos.
            s_12_2_2_tomas_irregulares_de_terreno:
              ID: GN-SEC-0190
              Title: 12.2.2. Tomas irregulares de terreno
              Content: |-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P02
                Def: Ocupación irregular de terrenos.
                Ex: Campamentos, que generan inseguridad de tenencia.
            s_12_2_3_segregacion_residencial:
              ID: GN-SEC-0191
              Title: 12.2.3. Segregación residencial
              Content: >-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P03 Def: Alta concentración
                espacial de hogares de ingresos similares en una ciudad o
                comuna.
            s_12_2_4_deterioro_de_infraestructura_y_espacios_publicos_comunitarios:
              ID: GN-SEC-0192
              Title: >-
                12.2.4. Deterioro de infraestructura y espacios públicos
                comunitarios
              Content: >-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P04 Def: Déficit de espacios
                públicos, áreas verdes, equipamiento y entornos urbanos de
                calidad en barrios/comunidades.
            s_12_2_5_dificultad_de_acceso_a_la_vivienda:
              ID: GN-SEC-0193
              Title: 12.2.5. Dificultad de acceso a la vivienda
              Content: >-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P05 Def: Dificultad prolongada
                o definitiva para acceder a una vivienda (propiedad o arriendo).
            s_12_2_6_problemas_de_financiamiento_para_la_vivienda:
              ID: GN-SEC-0194
              Title: 12.2.6. Problemas de financiamiento para la vivienda
              Content: >-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P06 Def: Dificultad para
                acceder a financiamiento (crédito hipotecario, ahorro) o
                incapacidad para pagar deudas adquiridas.
            s_12_2_7_deterioro_del_stock_de_viviendas:
              ID: GN-SEC-0195
              Title: 12.2.7. Deterioro del stock de viviendas
              Content: |-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P07
                Def: Viviendas con carencias de habitabilidad.
                Ctx: Áreas.
                - Calidad de materiales.
                - Aislamiento térmico.
                - Equipamiento básico.
                - Seguridad estructural.
                - Daños por contingencias.
            s_12_2_8_hacinamiento:
              ID: GN-SEC-0196
              Title: 12.2.8. Hacinamiento
              Content: >-
                ID: STS-PS-CH-TERRITORIO-VIVIENDA-P08 Def: Viviendas con
                carencias de habitabilidad por falta de espacio. Req:
                Ampliaciones u otras soluciones para mejorar espacio habitable y
                funcionalidad.
        s_12_3_planificacion_territorial:
          ID: GN-SEC-0197
          Title: 12.3. Planificación Territorial
          Content: 'ID: STS-PS-CH-TERRITORIO-PLANIF'
          Sections:
            s_12_3_1_irregularidad_juridica_en_dominio_de_tierras:
              ID: GN-SEC-0198
              Title: 12.3.1. Irregularidad jurídica en dominio de tierras
              Content: >-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P01 Def: Tenencia de tierras no
                regularizada jurídicamente. Ex: Familias o pueblos indígenas
                ocupando tierras fiscales/privadas solo de hecho.
            s_12_3_2_segregacion_territorial_subnacional:
              ID: GN-SEC-0199
              Title: 12.3.2. Segregación territorial subnacional
              Content: >-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P02 Def: Disparidad o
                desigualdad entre territorios (regiones, comunas). Ctx:
                Dimensiones. - Económica. - Social. - Política. - Ambiental. -
                Calidad de vida. - Servicios.
            s_12_3_3_altos_niveles_de_centralizacion_politica_y_administrativa:
              ID: GN-SEC-0200
              Title: >-
                12.3.3. Altos niveles de centralización política y
                administrativa
              Content: |-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P03
                Def: Centralización excesiva del poder y los recursos.
                Ex:
                - Gasto público.
                - Capacidad de agencia fiscal y política.
                - Acceso a datos confiables.
            s_12_3_4_competencias_limitadas_de_instituciones_y_gobiernos_subnacionales:
              ID: GN-SEC-0201
              Title: >-
                12.3.4. Competencias limitadas de instituciones y gobiernos
                subnacionales
              Content: >-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P04 Def: Capacidades
                institucionales limitadas para el desarrollo de actividades,
                coordinación y gestión a nivel local/regional. Ctx: Inclusiones.
                - Bajo fortalecimiento de instituciones públicas y/o privadas
                subnacionales.
            s_12_3_5_provision_deficiente_de_bienes_y_servicios_en_zonas_o_territorios:
              ID: GN-SEC-0202
              Title: >-
                12.3.5. Provisión deficiente de bienes y servicios en zonas o
                territorios
              Content: >-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P05 Def: Difícil acceso a
                ciertos bienes y servicios en algunos territorios. Cause:
                Aislamiento, lejanía. Ctx: Exclusiones. - Acceso a servicios
                básicos a nivel de vivienda. Ref:
                STS-PS-CH-TERRITORIO-VIVIENDA-P01.
            s_12_3_6_zonas_sin_o_con_bajo_acceso_a_telecomunicaciones:
              ID: GN-SEC-0203
              Title: 12.3.6. Zonas sin o con bajo acceso a telecomunicaciones
              Content: |-
                ID: STS-PS-CH-TERRITORIO-PLANIF-P06
                Def: Bajo acceso a telecomunicaciones en ciertas zonas.
                Cause:
                - Aislamiento.
                - Económicas.
                - Otras.
                Res:
                - Alta brecha digital.
                - Baja capacidad/velocidad.
                - Falta de conectividad digital.
    s_13_educacion:
      ID: GN-SEC-0204
      Title: 13. Educación
      Content: 'ID: STS-PS-CH-EDUCACION'
      Sections:
        s_13_1_educacion_parvularia_y_escolar:
          ID: GN-SEC-0205
          Title: 13.1. Educación Parvularia y Escolar
          Content: 'ID: STS-PS-CH-EDUCACION-ESCOLAR'
          Sections:
            s_13_1_1_acceso_y_costos:
              ID: GN-SEC-0206
              Title: 13.1.1. Acceso y Costos
              Content: 'ID: STS-PS-CH-EDUCACION-ESCOLAR-ACCESO'
              Sections:
                s_13_1_1_1_problemas_de_acceso_a_educacion_parvularia:
                  ID: GN-SEC-0207
                  Title: 13.1.1.1. Problemas de acceso a educación parvularia
                  Content: |-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-ACCESO-P01
                    Def: Barreras de acceso a la educación parvularia.
                    Cause:
                    - Dificultad de financiamiento (arancel, matrícula).
                    - Contingencias.
                    - Barreras culturales.
                    - Barreras físicas.
                s_13_1_1_2_problemas_de_acceso_a_educacion_escolar:
                  ID: GN-SEC-0208
                  Title: 13.1.1.2. Problemas de acceso a educación escolar
                  Content: |-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-ACCESO-P02
                    Def: Barreras de acceso a la educación escolar.
                    Cause:
                    - Dificultad de financiamiento (arancel, matrícula).
                    - Contingencias.
                    - Barreras culturales.
                    - Barreras físicas.
                s_13_1_1_3_alto_costo_de_mantencion_de_escolares:
                  ID: GN-SEC-0209
                  Title: 13.1.1.3. Alto costo de mantención de escolares
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-ACCESO-P03 Def: Dificultad
                    para financiar gastos derivados de estudios parvularios y
                    escolares. Ctx: Gastos. - Transporte. - Materiales. -
                    Alimentación. - Residencia.
            s_13_1_2_calidad_y_pertinencia:
              ID: GN-SEC-0210
              Title: 13.1.2. Calidad y Pertinencia
              Content: 'ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD'
              Sections:
                s_13_1_2_1_ausencia_de_educacion_intercultural:
                  ID: GN-SEC-0211
                  Title: 13.1.2.1. Ausencia de educación intercultural
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P01 Def: Falta de
                    educación sobre otras culturas o existencia de barreras
                    culturales que impiden la inclusión. Ctx: Población. -
                    Estudiantes, familias y docentes extranjeros. - Pueblos
                    indígenas. Ctx: Niveles. - Escolar. - Parvularia.
                s_13_1_2_2_falta_de_educacion_inclusiva:
                  ID: GN-SEC-0212
                  Title: 13.1.2.2. Falta de educación inclusiva
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P02 Def: Prácticas
                    pedagógicas e institucionales homogéneas, estandarizadas y
                    normalizadoras. Res: Contradice principios de inclusión y
                    crea barreras para personas con mayores dificultades o
                    necesidades especiales. Ctx: Niveles. - Escolar. -
                    Parvularia.
                s_13_1_2_3_baja_calidad_de_la_educacion_parvularia:
                  ID: GN-SEC-0213
                  Title: 13.1.2.3. Baja calidad de la educación parvularia
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P03 Def: Baja
                    calidad de los procesos de aprendizaje en educación
                    parvularia. Ctx: Áreas. - Currículum. - Metodologías de
                    enseñanza. - Innovación.
                s_13_1_2_4_baja_calidad_de_los_procesos_de_ensenanza_aprendizaje_escolar:
                  ID: GN-SEC-0214
                  Title: >-
                    13.1.2.4. Baja calidad de los procesos de
                    enseñanza-aprendizaje escolar
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P04 Def: Baja
                    calidad de procesos de aprendizaje en educación básica y
                    media. Ctx: Áreas. - Currículum. - Metodologías. Ctx:
                    Inclusiones. - Brechas de calidad entre establecimientos.
                s_13_1_2_5_bajos_logros_academicos_escolares:
                  ID: GN-SEC-0215
                  Title: 13.1.2.5. Bajos logros académicos escolares
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P05 Def: Logros
                    académicos bajos en comparación con estándares
                    internacionales.
                s_13_1_2_6_infraestructura_equipamiento_y_o_material_educativo_deficiente_o_falt:
                  ID: GN-SEC-0216
                  Title: >-
                    13.1.2.6. Infraestructura, equipamiento y/o material
                    educativo deficiente o faltante
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P06 Def: Necesidad
                    de adquisición/renovación en establecimientos educacionales.
                    Ctx: Ítems. - Infraestructura. - Mobiliario. - Equipamiento
                    (ej. TIC). - Material educativo. Cause: - Falta de
                    financiamiento. - Gestión. - Recursos. - Contingencias. Ctx:
                    Niveles. - Escolar. - Parvularia.
                s_13_1_2_7_baja_calidad_en_formacion_de_docentes:
                  ID: GN-SEC-0217
                  Title: 13.1.2.7. Baja calidad en formación de docentes
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P07 Def: Baja
                    calidad en la formación inicial de docentes y/o necesidad de
                    formación permanente. Ctx: Niveles. - Todos (párvulos,
                    básica, media, superior).
                s_13_1_2_8_capacidades_institucionales_debiles_en_establecimientos_educacionales:
                  ID: GN-SEC-0218
                  Title: >-
                    13.1.2.8. Capacidades institucionales débiles en
                    establecimientos educacionales
                  Content: |-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-CALIDAD-P08
                    Def: Falta de capacidades institucionales y/o directivas.
                    Ctx: Niveles.
                    - Escolar.
                    - Parvularia.
            s_13_1_3_trayectoria_educativa:
              ID: GN-SEC-0219
              Title: 13.1.3. Trayectoria Educativa
              Content: 'ID: STS-PS-CH-EDUCACION-ESCOLAR-TRAYECTORIA'
              Sections:
                s_13_1_3_1_desercion_escolar:
                  ID: GN-SEC-0220
                  Title: 13.1.3.1. Deserción escolar
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-TRAYECTORIA-P01 Def:
                    Estudiantes abandonan el sistema escolar interrumpiendo su
                    trayectoria. Ctx: Inclusiones. - Problemas de asistencia
                    como precursor de la deserción. Cpt: Indicador. - Ctx:
                    Pobreza Multidimensional. - Def: Problemas de asistencia.
                s_13_1_3_2_rezago_escolar_menores_de_21_anos:
                  ID: GN-SEC-0221
                  Title: 13.1.3.2. Rezago escolar (menores de 21 años)
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-TRAYECTORIA-P02 Def:
                    Personas de 21 años o menos que asisten a ed. básica/media
                    con dos o más años de retraso respecto a su edad. Cpt:
                    Indicador. - Ctx: Pobreza Multidimensional. - Def: Atraso
                    escolar.
                s_13_1_3_3_desescolarizacion_mayores_de_18_anos:
                  ID: GN-SEC-0222
                  Title: 13.1.3.3. Desescolarización (mayores de 18 años)
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-TRAYECTORIA-P03 Def:
                    Personas mayores de 18 años con menos años de escolaridad
                    que los establecidos por ley para su edad. Cpt: Indicador. -
                    Ctx: Pobreza Multidimensional. - Def: Escolaridad.
            s_13_1_4_comunidad_educativa:
              ID: GN-SEC-0223
              Title: 13.1.4. Comunidad Educativa
              Content: 'ID: STS-PS-CH-EDUCACION-ESCOLAR-COMUNIDAD'
              Sections:
                s_13_1_4_1_violencia_en_la_cultura_escolar:
                  ID: GN-SEC-0224
                  Title: 13.1.4.1. Violencia en la cultura escolar
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-COMUNIDAD-P01 Def: Acciones
                    de daño entre integrantes de la comunidad escolar (alumnos,
                    profesores, directivos, padres, personal).
                s_13_1_4_2_poca_participacion_de_padres_y_comunidad_en_decisiones_educativas:
                  ID: GN-SEC-0225
                  Title: >-
                    13.1.4.2. Poca participación de padres y comunidad en
                    decisiones educativas
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-ESCOLAR-COMUNIDAD-P02 Def: Baja
                    participación de padres/madres en la comunidad escolar,
                    especialmente en la toma de decisiones.
        s_13_2_educacion_superior:
          ID: GN-SEC-0226
          Title: 13.2. Educación Superior
          Content: 'ID: STS-PS-CH-EDUCACION-SUPERIOR'
          Sections:
            s_13_2_1_acceso_y_financiamiento:
              ID: GN-SEC-0227
              Title: 13.2.1. Acceso y Financiamiento
              Content: 'ID: STS-PS-CH-EDUCACION-SUPERIOR-ACCESO'
              Sections:
                s_13_2_1_1_problemas_de_acceso_y_o_permanencia_en_educacion_superior:
                  ID: GN-SEC-0228
                  Title: >-
                    13.2.1.1. Problemas de acceso y/o permanencia en educación
                    superior
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-SUPERIOR-ACCESO-P01 Def: Barreras de
                    acceso o permanencia en la educación superior. Cause: -
                    Dificultad de financiamiento (arancel, matrícula). -
                    Contingencias. - Barreras culturales. - Barreras físicas.
                s_13_2_1_2_alto_costo_de_mantencion_de_estudiantes_de_educacion_superior:
                  ID: GN-SEC-0229
                  Title: >-
                    13.2.1.2. Alto costo de mantención de estudiantes de
                    educación superior
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-SUPERIOR-ACCESO-P02 Def: Dificultad
                    para financiar gastos derivados de estudios superiores. Ctx:
                    Gastos. - Transporte. - Materiales. - Alimentación. -
                    Residencia.
                s_13_2_1_3_alto_endeudamiento_de_estudiantes_de_educacion_superior:
                  ID: GN-SEC-0230
                  Title: >-
                    13.2.1.3. Alto endeudamiento de estudiantes de educación
                    superior
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-SUPERIOR-ACCESO-P03 Def:
                    Endeudamiento estudiantil por costos de entrada, mantención
                    u otros.
            s_13_2_2_calidad_y_pertinencia:
              ID: GN-SEC-0231
              Title: 13.2.2. Calidad y Pertinencia
              Content: 'ID: STS-PS-CH-EDUCACION-SUPERIOR-CALIDAD'
              Sections:
                s_13_2_2_1_desarticulacion_entre_educacion_superior_y_mercado_laboral:
                  ID: GN-SEC-0232
                  Title: >-
                    13.2.2.1. Desarticulación entre educación superior y mercado
                    laboral
                  Content: >-
                    ID: STS-PS-CH-EDUCACION-SUPERIOR-CALIDAD-P01 Def:
                    Insuficiente actualización o adaptación de competencias de
                    docentes y estudiantes a las necesidades del mercado
                    laboral. Cpt: Brecha. - Conocimientos y habilidades.
                s_13_2_2_2_falta_de_financiamiento_de_instituciones_de_educacion_superior_ies:
                  ID: GN-SEC-0233
                  Title: >-
                    13.2.2.2. Falta de financiamiento de instituciones de
                    educación superior (IES)
                  Content: |-
                    ID: STS-PS-CH-EDUCACION-SUPERIOR-CALIDAD-P02
                    Def: Falta de financiamiento en IES para disminuir brechas.
                    Ctx: Áreas.
                    - Infraestructura.
                    - Académicos.
                    - Relación con el entorno.
                    - Gestión.
                    - Contribución al desarrollo regional.
    s_14_ciencia_tecnologia_e_innovacion:
      ID: GN-SEC-0234
      Title: '14. Ciencia, Tecnología e Innovación'
      Content: 'ID: STS-PS-CH-CTI'
      Sections:
        s_14_1_desarrollo_cti:
          ID: GN-SEC-0235
          Title: 14.1. Desarrollo CTI
          Content: 'ID: STS-PS-CH-CTI-DESARROLLO'
          Sections:
            s_14_1_1_bajo_nivel_de_investigacion_y_produccion_cientifica:
              ID: GN-SEC-0236
              Title: 14.1.1. Bajo nivel de investigación y producción científica
              Content: >-
                ID: STS-PS-CH-CTI-DESARROLLO-P01 Def: Falta de desarrollo y
                producción científica y de innovación. Ctx: Instituciones. -
                Universidades. - IES. - Centros de investigación.
        s_14_2_adopcion_y_cultura_cti:
          ID: GN-SEC-0237
          Title: 14.2. Adopción y Cultura CTI
          Content: 'ID: STS-PS-CH-CTI-ADOPCION'
          Sections:
            s_14_2_1_escaso_conocimiento_de_la_poblacion_en_temas_cientificos_y_tecnologicos:
              ID: GN-SEC-0238
              Title: >-
                14.2.1. Escaso conocimiento de la población en temas científicos
                y tecnológicos
              Content: |-
                ID: STS-PS-CH-CTI-ADOPCION-P01
                Def: Bajo conocimiento y cultura de la población general en CTI.
