---
urn: urn:gn:kb:gn-loc-gore
nombre: gn-loc-gore
version: "0.1.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre KODA Artifact: LOC Gobierno y Administración Regional (DFL 1-19.175); migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/01_fundamentos/legal/kb_gn_031_loc_gore_koda.yml (sha256:f252f50c71741c47fd0f07a4d080f21be729011ebfd217dc347488aed537a70e); URN KODA legado urn:gorenuble:gn:loc-gore:1.0.0; estado original published; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2025-11-27
lang: es
tags: ["gn", "gore-os", "koda", "domains", "01-fundamentos", "legal", "loc", "gore"]
familia: bok
---
_manifest:
  urn: "urn:gorenuble:gn:loc-gore:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use Only"
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2026-02-19"
    last_modified_at: "2026-02-19"

# KODA Artifact: LOC Gobierno y Administración Regional (DFL 1-19.175)
# Transformación desde: 19175.md
# Estado: BORRADOR INICIAL
---
ID: KB-GN-031-LOC-GORE-KODA
Version: 0.1.0
Status: published
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: Cascade
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-11-27
Modification-Date: 2025-11-27
Ctx: LOC sobre Gobierno Interior y Administración de la Región (DFL 1-19.175)
Primary-Source: 19175.md

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-LOC-GORE
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, relationships) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents use Ctx:, Ctx_Required:, or Ctx_Optional:.

    LANGUAGE POLICY: Keywords in English, content in original language (es-CL). Never translate content.
    END_LLM_INSTRUCTIONS

Definiciones_Centralizadas:
  ID: DEF-LOC-GORE
  Def: Conceptos orgánicos claves de la LOC de Gobierno y Administración Regional (DFL 1-19.175)

  GORE:
    ID: DEF-GORE
    Def: Gobierno Regional. Administración superior de cada región, con personalidad jurídica de derecho público y patrimonio propio.

  Gobierno_Interior_Region:
    ID: DEF-GOB-INTERIOR
    Def: Función de gobierno interior en cada región, ejercida por el Delegado Presidencial Regional como representante del Presidente.

  Delegado_Presidencial_Regional:
    ID: DEF-DEL-PRES-REG
    Def: Representante natural e inmediato del Presidente de la República en la región; jefe del gobierno interior regional.
    Ref:
      - DEF-GOB-INTERIOR
      - ORG-PRESIDENTE-CL

  Delegado_Presidencial_Provincial:
    ID: DEF-DEL-PRES-PROV
    Def: Órgano territorialmente desconcentrado del Delegado Presidencial Regional que ejerce gobierno interior en la provincia.

  Gobernador_Regional:
    ID: DEF-GOBERNADOR-REG
    Def: Órgano ejecutivo del Gobierno Regional, elegido por sufragio universal, que preside el consejo regional.

  Consejo_Regional:
    ID: DEF-CONSEJO-REG
    Def: Órgano colegiado que, junto al Gobernador Regional, integra el Gobierno Regional y aprueba acuerdos y políticas regionales.

  Competencia_Administrativa:
    ID: DEF-COMPETENCIA-ADM
    Def: Facultad, función o atribución de ministerios o servicios públicos para satisfacer necesidades públicas en materias definidas por ley, excluida Ley de Presupuestos.

  Presidente_Republica:
    ID: ORG-PRESIDENTE-CL
    Def: Jefe de Estado y de Gobierno; ejerce el gobierno y la administración del Estado y designa a los delegados presidenciales regionales y provinciales.

  Contraloria_General:
    ID: ORG-CGR
    Def: Órgano superior de control de la legalidad de los actos de la Administración del Estado y del examen y juzgamiento de las cuentas.

  Tribunal_Calificador_Elecciones:
    ID: ORG-TRICEL
    Def: Órgano jurisdiccional que conoce, califica y proclama elecciones y resuelve reclamaciones y causales de cesación en cargos de elección popular cuando la Constitución o la ley lo establecen.

  SUBDERE:
    ID: ORG-SUBDERE
    Def: Subsecretaría de Desarrollo Regional y Administrativo. Órgano responsable de lineamientos operativos de descentralización y apoyo a gobiernos regionales y municipalidades.

Contexto_General:
  ID: CTX-LOC-GORE
  Purp: Sintetizar la arquitectura orgánica y funcional del Gobierno Interior de la Región y del Gobierno Regional.
  Src_Oficial:
    ID: CTX-LOC-GORE-SRC
    Def: DFL N° 1-19.175 que fija texto refundido, coordinado, sistematizado y actualizado de la Ley N° 19.175.
  Ambito_Material:
    ID: CTX-LOC-GORE-AMBITO
    Items:
      - Gobierno interior regional (Delegados Presidenciales Regionales y Provinciales).
      - Administración superior de la región (Gobierno Regional).
      - Competencias, funciones y atribuciones del Gobierno Regional.
      - Procedimiento de transferencia y revocación de competencias desde nivel central.
      - Órganos del Gobierno Regional y estatuto del Gobernador Regional.

Gobierno_Interior_Region:
  ID: MOD-GOB-INTERIOR
  Ref:
    - DEF-DEL-PRES-REG
    - DEF-DEL-PRES-PROV

  Delegado_Presidencial_Regional:
    ID: MOD-DEL-PRES-REG
    Ref_Def: DEF-DEL-PRES-REG
    Ref:
      - ORG-PRESIDENTE-CL

    Naturaleza_Cargo:
      ID: DEL-PRES-REG-NAT
      Def: Gobierno interior de cada región reside en el Delegado Presidencial Regional como representante inmediato del Presidente en el territorio.
      Req:
        - Nombrado y removido libremente por el Presidente.
        - Permanece en el cargo mientras goce de la confianza presidencial.
        - Ejerce funciones conforme a las leyes y a instrucciones del Presidente directamente o vía Ministerio del Interior.

    Rol_Coordinacion:
      ID: DEL-PRES-REG-COORD
      Def: Coordina a nivel regional la acción de gobierno y vela por adecuada gestión de servicios públicos, planes y programas en ejecución.
      Req:
        - Puede requerir informes a Secretarías Regionales Ministeriales sobre cumplimiento de funciones e instrucciones técnicas/administrativas de sus ministerios.

    Subrogancia_y_Suplencia:
      ID: DEL-PRES-REG-SUBR
      Def: Subrogado por Delegado Presidencial Provincial que designe el Presidente.
      Req:
        - Presidente puede designar suplente sin límite temporal de subrogación previsto en Estatuto Administrativo.

    Atribuciones_Principales:
      ID: DEL-PRES-REG-FUNC
      Def: Conjunto de atribuciones en Art.2.
      Items:
        - Dirigir tareas de gobierno interior en la región según orientaciones e instrucciones del Presidente o Ministerio del Interior.
        - Velar por tranquilidad y protección de personas y bienes en la región.
        - Instruir auxilio de la fuerza pública vía Secretario Regional Ministerial de Seguridad Pública.
        - Mantener informado al Presidente sobre cumplimiento de funciones de gobierno interior y desempeño de delegados provinciales y jefes regionales de organismos públicos.
        - Informar reservadamente al Presidente sobre faltas en conducta ministerial de jueces y funcionarios del Poder Judicial.
        - Conocer y resolver recursos administrativos contra resoluciones de delegados presidenciales provinciales.
        - Aplicar Ley de Extranjería y disponer expulsiones de extranjeros conforme a dicha ley.
        - Efectuar denuncias o presentar requerimientos ante tribunales de justicia.
        - Representar extrajudicialmente al Estado en la región para actos y contratos dentro de su competencia.
        - Coordinar, fiscalizar y supervigilar servicios públicos de la Administración que operen en la región y dependan o se relacionen con el Presidente vía ministerios; informar semestralmente al Ministerio del Interior sobre su estado y funcionamiento.
        - Proponer al Presidente ternas para designación de Secretarios Regionales Ministeriales.
        - Proponer al Presidente o ministros sectoriales la remoción de SEREMI y jefes regionales de organismos públicos según corresponda.
        - Formular conjuntamente con el Gobernador Regional las necesidades de la región ante autoridades del nivel central.
        - Coordinar adecuada administración de complejos fronterizos de la región.
        - Adoptar medidas necesarias para prevenir y enfrentar emergencias o catástrofes regionales.
        - Dictar resoluciones e instrucciones necesarias para ejercicio de sus atribuciones.
        - Ejercer otras funciones legales y atribuciones delegadas por el Presidente, incluyendo otorgar personalidad jurídica a corporaciones y fundaciones con ámbito regional.
        - Coordinar prevención y respuesta frente a conflictos sociales sin riesgo para seguridad pública.
        - Ejercer en la región funciones legales del Ministerio del Interior, conforme a instrucciones ministeriales.

    Delegacion_Atribuciones:
      ID: DEL-PRES-REG-DELEG
      Def: Puede delegar atribuciones en delegados presidenciales provinciales.
      Prohib:
        - No puede ejercer competencia delegada sin revocar previamente la delegación.
      Req_Interactivo:
        - Debe desempeñar el cargo dialogando con autoridades locales.
        - Debe respetar irrestrictamente planes de desarrollo comunales y regionales.

  Delegado_Presidencial_Provincial:
    ID: MOD-DEL-PRES-PROV
    Ref_Def: DEF-DEL-PRES-PROV
    Ref:
      - DEF-DEL-PRES-REG

    Naturaleza_Cargo:
      ID: DEL-PRES-PROV-NAT
      Def: Delegación presidencial provincial es órgano territorialmente desconcentrado del Delegado Presidencial Regional.
      Req:
        - Delegado Presidencial Provincial es nombrado y removido libremente por el Presidente.
        - Ejerce, según instrucciones del Delegado Presidencial Regional, supervigilancia de servicios públicos existentes en la provincia que dependan o se relacionen con el Presidente vía ministerios.

    Subrogancia:
      ID: DEL-PRES-PROV-SUBR
      Def: Subrogación regulada por Estatuto Administrativo.
      Req:
        - Se aplica régimen del Art.80 de la Ley N° 18.834, sin perjuicio de facultad presidencial para designar suplente sin sujeción a requisitos de tiempo.

    Atribuciones_Principales:
      ID: DEL-PRES-PROV-FUNC
      Def: Atribuciones propias más delegadas (Art.4).
      Items:
        - Ejercer tareas de gobierno interior en la provincia.
        - Aplicar en la provincia la normativa de extranjería.
        - Autorizar reuniones en lugares públicos conforme normativa vigente e informar a Carabineros.
        - Requerir auxilio de fuerza pública vía Director Provincial de Seguridad Pública.
        - Adoptar medidas para prevenir y enfrentar emergencias o catástrofes.
        - Velar por buen uso de la Bandera Nacional y autorizar uso de pabellones extranjeros conforme a ley.
        - Autorizar circulación de vehículos de servicios públicos fuera de horario laboral y excepciones de uso de disco fiscal.
        - Vigilar bienes del Estado, especialmente de uso público: impedir ocupaciones ilegales, usos ilegítimos y exigir restitución administrativa.
        - Dictar resoluciones e instrucciones necesarias para ejercicio de atribuciones propias o delegadas.
        - Supervisar programas y proyectos de desarrollo de servicios públicos en la provincia que no dependan del Gobierno Regional.
        - Disponer medidas de coordinación para desarrollo provincial.
        - Representar necesidades del territorio al Delegado Presidencial Regional o SEREMI respectivos.
        - Ejercer en la provincia funciones que la ley entrega al Ministerio del Interior, conforme a instrucciones ministeriales.

    Encargados_Locales:
      ID: DEL-PRES-PROV-ENCARGADOS
      Def: Designación de encargados con atribuciones específicas en localidades aisladas (Art.5).
      Req:
        - Requiere autorización del Delegado Presidencial Regional.
        - Encargado debe ser ciudadano con derecho a sufragio y cumplir requisitos generales de ingreso a Administración Pública.
        - Resolución de designación debe fijar facultades específicas, plazo y ámbito territorial.
        - Si encargado es funcionario público, actúa en comisión de servicio sin límite de tiempo.
        - Si es persona ajena a la Administración, se desempeña ad honorem.
      Res:
        - Encargado queda sujeto a responsabilidades administrativas, civiles y penales como funcionario público.
        - Extracto de la resolución se publica en Diario Oficial y diario de mayor circulación provincial.

  Disposiciones_Comunes_Delegados:
    ID: MOD-DELEG-COMUN
    Ref:
      - DEF-DEL-PRES-REG
      - DEF-DEL-PRES-PROV

    Requisitos_Para_Cargo:
      ID: DEL-COMUN-REQ-CARGO
      Def: Requisitos para ser Delegado Presidencial Regional o Provincial (Art.6).
      Ref:
        - DEF-DEL-PRES-REG
        - DEF-DEL-PRES-PROV
      Req:
        - Ser ciudadano con derecho a sufragio.
        - Tener al menos 21 años y cumplir requisitos generales de ingreso a Administración Pública.
        - No estar inhabilitado para funciones o cargos públicos.
        - No haber sido condenado por crimen o simple delito.
        - Residir en la región respectiva al menos 2 años previos a la designación.
        - No tener dependencia de sustancias o drogas estupefacientes o sicotrópicas ilegales, salvo uso médico justificado.
      Proc_Acreditacion:
        ID: DEL-COMUN-REQ-ACRED
        Def: Interesado debe prestar declaración jurada que acredite no encontrarse afecto a inhabilidad por dependencia de drogas.

    Incompatibilidades_Cargos:
      ID: DEL-COMUN-INCOMP
      Def: Incompatibilidad entre cargos regionales y locales (Art.7).
      Prohib:
        - No se puede ejercer simultáneamente: Gobernador Regional, Delegado Presidencial Regional, Consejero Regional, Alcalde, Concejal, Delegado Presidencial Provincial ni Consejero Comunal de organizaciones de la sociedad civil.

    Causales_Cese:
      ID: DEL-COMUN-CESE
      Def: Causales de cesación para Delegados Presidenciales Regionales y Provinciales (Art.8).
      Items:
        - Pérdida de requisitos habilitantes.
        - Aceptación de cargo incompatible.
        - Inscripción como candidato a cargo de elección popular.
        - Aceptación de renuncia.
        - Remoción dispuesta por el Presidente.
        - Destitución por acuerdo del Senado conforme Art.53 N°1 de la Constitución.

    Ejercicio_Funciones:
      ID: DEL-COMUN-EJERC
      Def: Reglas de ejercicio territorial y deberes de información (Arts.9–12).
      Ref:
        - ORG-CGR
      Req:
        - Ejercer funciones en capital regional o provincial, pudiendo hacerlo transitoriamente en otras localidades del territorio.
        - Pueden solicitar a jefes de organismos sujetos a su fiscalización los informes y antecedentes necesarios, quienes deben entregarlos oportunamente.
        - Deben poner en conocimiento de Contraloría General y tribunal competente hechos plausibles de responsabilidad administrativa, civil o penal de funcionarios fiscalizados.
        - Servicio de Gobierno Interior debe apoyar ejercicio de funciones y atribuciones de Delegados y prestar apoyo administrativo a SEREMI y Departamentos Provinciales de Seguridad Pública.

Administracion_Region_GORE:
  ID: MOD-ADM-REG
  Ref:
    - DEF-GORE
    - DEF-CONSEJO-REG
    - DEF-GOBERNADOR-REG

  Naturaleza_y_Objetivo_GORE:
    ID: GORE-NAT-OBJ
    Def: Administración superior de cada región radicada en un Gobierno Regional (Art.13).
    Req:
      - GORE tiene personalidad jurídica de derecho público y patrimonio propio.
      - Ejerce funciones y atribuciones que la ley le confiere.
      - Puede ejercer competencias directamente o con colaboración de otros órganos de la Administración.
      - Administración financiera se rige por DL N° 1.263 y normas de administración financiera del Estado.
      - Nuevas funciones o atribuciones deben identificar fuente de financiamiento y contemplar recursos para su ejercicio.

  Principios_Gestion_Regional:
    ID: GORE-PRINCIPIOS
    Def: Principios rectores de la administración interna de las regiones (Art.14).
    Items:
      - Desarrollo armónico y equitativo de territorios regionales en dimensiones económica, social y cultural.
      - Equidad, eficiencia y eficacia en asignación y uso de recursos públicos y en prestación de servicios.
      - Participación efectiva de la comunidad regional.
      - Preservación y mejoramiento del medio ambiente.
      - Sujeción a principios del Art.3 de la Ley N° 18.575.

  Sede_GORE:
    ID: GORE-SEDE
    Def: Sede y ejercicio territorial (Art.15).
    Req:
      - Sede del Gobierno Regional se ubica en la capital de la región.
      - Puede ejercer funciones transitoriamente en otras localidades de la región.

  Funciones_Generales_GORE:
    ID: GORE-FUNC-GEN
    Def: Funciones generales del GORE (Art.16).
    Ref: DEF-GORE
    Items:
      - Diseñar, elaborar, aprobar y aplicar políticas, planes, programas y proyectos de desarrollo regional, ajustados al Presupuesto de la Nación, Estrategia Regional de Desarrollo e instrumentos de planificación comunal.
      - Realizar estudios, análisis y proposiciones sobre desarrollo regional.
      - Orientar desarrollo territorial en coordinación con servicios públicos y municipalidades.
      - Elaborar y aprobar proyecto de presupuesto regional, conforme orientaciones de Ley de Presupuestos y atribuciones del Gobernador Regional.
      - Administrar fondos y programas de aplicación regional.
      - Decidir inversión de recursos del FNDR y otros que procedan, según normativa aplicable.
      - Decidir destinación a proyectos específicos de recursos de programas de inversión sectorial de asignación regional.
      - Dictar normas generales para materias de su competencia, sujetas a toma de razón y publicación.
      - Asesorar a municipalidades que lo soliciten, especialmente en formulación de planes y programas de desarrollo.
      - Adoptar medidas para enfrentar emergencias o catástrofes, y desarrollar programas de prevención y protección ante desastres.
      - Participar en acciones de cooperación internacional en la región dentro del marco de tratados y legislación aplicable.
      - Ejercer competencias que le sean transferidas conforme procedimiento legal.
      - Mantener relación permanente con gobierno nacional y sus organismos para armonizar funciones.
      - Ejecutar obras de pavimentación de aceras y calzadas en áreas urbanas con cargo a recursos asignados, pudiendo celebrar convenios con municipalidades y otros órganos.
      - Elaborar y aprobar planes de inversiones en infraestructura de movilidad y espacio público asociados a planes reguladores metropolitanos o intercomunales, con consulta a municipalidades.
      - Coparticipar con el Comité Regional para el cambio climático en instrumentos de gestión del cambio climático a nivel regional.

  Ordenamiento_Territorial:
    ID: GORE-ORD-TERR
    Def: Funciones en materia de ordenamiento territorial (Art.17).
    Plan_Regional_Ordenamiento_Territorial:
      ID: GORE-PROT
      Def: Instrumento que orienta uso del territorio regional para desarrollo sustentable mediante lineamientos estratégicos y macrozonificación.
      Req:
        - Debe ser coherente con Estrategia Regional de Desarrollo, política nacional de ordenamiento territorial, estrategia climática de largo plazo y plan de acción regional de cambio climático.
        - Establece condiciones vinculantes de localización para disposición de residuos y para infraestructura y actividades productivas en zonas no urbanizadas, incluyendo áreas de localización preferente.
        - Reconoce áreas bajo protección oficial según legislación especial.
        - Es obligatorio para ministerios y servicios públicos que operen en la región.
        - No puede regular materias que excedan territorio regional ni áreas sometidas a planificación urbanística.
      Proc_Elaboracion:
        ID: GORE-PROT-PROC
        Def: Procedimiento de elaboración, consulta y actualización.
        Steps:
          - Diagnóstico de características, tendencias, restricciones y potencialidades del territorio regional.
          - Consulta pública mínima de 60 días sobre imagen objetivo y elementos de estructuración territorial, con consulta paralela a municipalidades y organismos del Gobierno Regional.
          - Convocatoria debe difundirse en al menos un medio nacional y uno regional.
          - Debe ajustarse a normativa ambiental (Ley N° 19.300, Párrafo 1° bis Título II).
          - Evaluación y actualización en ciclos no superiores a 10 años.
      Rol_Comision_Interministerial:
        ID: GORE-PROT-COMISION
        Def: Comisión Interministerial de Ciudad, Vivienda y Territorio propone políticas nacionales de ordenamiento territorial y reglamentos de procedimientos aplicables al plan regional.
        Composicion:
          ID: GORE-PROT-COMISION-COMP
          Items:
            - "Ministro de Vivienda y Urbanismo (preside la comisión)."
            - "Ministro del Interior y Seguridad Pública."
            - "Ministro Secretaría General de la Presidencia."
            - "Ministro de Economía, Fomento y Turismo."
            - "Ministro de Desarrollo Social."
            - "Ministro de Obras Públicas."
            - "Ministro de Agricultura."
            - "Ministro de Minería."
            - "Ministro de Transportes y Telecomunicaciones."
            - "Ministro de Bienes Nacionales."
            - "Ministro de Energía."
            - "Ministro del Medio Ambiente."
        Src: Decreto supremo expedido por Ministerio del Interior y Seguridad Pública y suscrito por ministros integrantes.

    Otras_Funciones_Ordenamiento:
      ID: GORE-ORD-TERR-OTRAS
      Items:
        - Establecer políticas y objetivos para desarrollo integral y armónico de asentamientos humanos de la región.
        - Participar en programas y proyectos de infraestructura y equipamiento regional.
        - Fomentar protección y mejoramiento del medio ambiente regional.
        - Fomentar y velar por buen funcionamiento del transporte intercomunal, interprovincial y fronterizo, coordinando transporte interregional.
        - Fomentar desarrollo de áreas rurales y localidades aisladas mediante infraestructura económica y social.
        - Proponer localización de SEREMI y direcciones regionales de servicios públicos.
        - Financiar estudios sobre localización y tratamiento de residuos, coordinando con SEREMI competentes.
        - Proponer territorios como zonas rezagadas en materia social y sus planes de desarrollo.

  Fomento_Actividades_Productivas:
    ID: GORE-FOMENTO-PROD
    Def: Funciones en materia productiva (Art.18).
    Ref: DEF-GORE
    Items:
      - Formular políticas regionales de fomento productivo, apoyo al emprendimiento, innovación, capacitación, ciencia y tecnología aplicada, gestión y competitividad.
      - Establecer prioridades estratégicas regionales en fomento e innovación, creando condiciones favorables para inversión y desarrollo empresarial sustentable.
      - Aprobar plan regional de desarrollo turístico en niveles regional, provincial y local.
      - Promover y diseñar programas y proyectos de fomento considerando aporte de instituciones de educación superior regionales.
      - Promover y apoyar, con municipios, oficinas comunales de fomento productivo e innovación.
      - Promover investigación científica y tecnológica, y desarrollo de educación superior y media técnico profesional.
      - Elaborar y aprobar Política Regional de Ciencia, Tecnología, Conocimiento e Innovación para el Desarrollo, con lineamientos estratégicos y ámbitos de acción priorizados.

  Desarrollo_Social_y_Cultural:
    ID: GORE-DES-SOC-CULT
    Def: Funciones de desarrollo social y cultural (Art.19).
    Ref: DEF-GORE
    Items:
      - Establecer prioridades regionales para erradicación de la pobreza.
      - Participar, con autoridades competentes, en acciones que faciliten acceso de población vulnerable a salud, educación, cultura, vivienda, seguridad social, deporte, recreación y asistencia judicial.
      - Proponer programas y proyectos con foco en grupos vulnerables o en riesgo social.
      - Distribuir recursos entre municipalidades para financiamiento de programas sociales que administren.
      - Realizar estudios sobre condiciones, nivel y calidad de vida de habitantes de la región.
      - Fomentar expresiones culturales y cautelar patrimonio histórico, artístico y cultural, incluidos monumentos y pueblos originarios.
      - Financiar y difundir actividades y programas culturales, fortaleciendo identidad regional.
      - Proponer programas y proyectos de formación y práctica deportiva.
      - Mantener información actualizada sobre situación socioeconómica regional y proponer programas para superar pobreza y extrema pobreza.

  Atribuciones_Generales_GORE:
    ID: GORE-ATRIB-GEN
    Def: Atribuciones para cumplir funciones (Art.20 y 20 bis, 21).
    Ref: DEF-GORE
    Items:
      - Aprobar y modificar normas reglamentarias regionales encargadas por ley, sin agregar requisitos adicionales a la normativa superior.
      - Adquirir, administrar y disponer de bienes y recursos propios conforme a ley.
      - Celebrar convenios de inversión con ministerios, servicios públicos, municipalidades u otros gobiernos regionales.
      - Disponer, supervisar y fiscalizar iniciativas financiadas con su presupuesto.
      - Aplicar políticas definidas en Estrategia Regional de Desarrollo.
      - Aprobar planes regionales de ordenamiento territorial, planes reguladores y planes de inversión en movilidad y espacio público.
      - Formular y priorizar proyectos de infraestructura social básica y evaluar programas.
      - Proponer criterios y, cuando proceda, distribuir subvenciones a programas sociales.
      - Aplicar tributos de carácter regional destinados a obras de desarrollo regional, dentro del marco legal.
      - Aprobar símbolos regionales (banderas, escudos, himnos) conforme a reglamento.
      - Diseñar, elaborar, aprobar y ejecutar políticas, planes, programas y proyectos dentro de su territorio.
      - Coparticipar en instrumentos regionales de gestión del cambio climático.

    Coherencia_Politicas_Nacionales:
      ID: GORE-COHER-NAC
      Def: Las funciones generales, de ordenamiento territorial, fomento y desarrollo social/cultural deben ejercerse coherentemente con políticas públicas nacionales vigentes (Art.20 bis).
      Req:
        - Ejercicio de funciones no puede contradecir políticas nacionales ni principios que éstas establecen.
        - Debe actuarse coordinadamente, evitando duplicidad o interferencia de funciones, conforme Art.5 Ley N° 18.575.
      Roles:
        - Ministro sectorial respectivo vela por coherencia entre ejercicio de funciones regionales y políticas nacionales.

    Coordinacion_Informacion_Con_Otros_Organos:
      ID: GORE-COORD-INFO
      Def: Deber de información y coordinación con órganos y servicios del Estado (Art.21).
      Ref: DEF-GORE
      Req:
        - Órganos y servicios de la Administración, empresas con participación fiscal y servicios públicos deben informar oportunamente a GORE sobre planes, programas y proyectos a ejecutar en la región.
        - Municipios deben remitir a GORE sus planes de desarrollo, políticas de prestación de servicios, políticas y proyectos de inversión, presupuestos y modificaciones.

  Transferencia_de_Competencias:
    ID: MOD-TRANSF-COMP
    Ref:
      - DEF-COMPETENCIA-ADM
      - DEF-GORE

  Definicion_y_Ambito:
    ID: TRANSF-COMP-DEF
    Def: Mecanismo por el cual el Presidente transfiere competencias de ministerios y servicios públicos a gobiernos regionales (Art.21 bis).
    Ref:
      - DEF-COMPETENCIA-ADM
      - ORG-PRESIDENTE-CL
    Req:
      - Competencias transferibles se refieren a ordenamiento territorial, fomento productivo y desarrollo social y cultural.
      - Transferencias pueden ser temporales o definitivas.
      - Presidente ordena adecuaciones necesarias en órganos que ceden competencias.
      - Se entiende por competencia toda facultad, función o atribución legalmente asignada, excluyendo Ley de Presupuestos.

  Admisibilidad_Solicitudes:
    ID: TRANSF-COMP-ADMIS
    Def: Criterios de admisibilidad de solicitudes de transferencia (Art.21 ter).
    Req:
      - Solicitudes fuera de ámbitos de ordenamiento territorial, fomento productivo y desarrollo social/cultural son inadmisibles de plano.
      - Inadmisibilidad se declara por decreto exento fundado del Ministerio del Interior y Seguridad Pública, suscrito además por Ministros de Hacienda y Secretaría General de la Presidencia.
      - Gobernador Regional debe rechazar solicitudes del Consejo Regional que pidan competencias fuera de dichos ámbitos.

  Principios_Seleccion_Competencias:
    ID: TRANSF-COMP-PRINC
    Def: Criterios para privilegiar competencias a transferir (Art.21 quáter).
    Items:
      - Competencias con clara aplicación regional.
      - Ejercicio en nivel regional mejora calidad y oportunidad de decisiones.
      - Mejor adecuación de política nacional al territorio sin perjudicar otras regiones.
      - Idealmente susceptibles de ser ejercidas por mayoría de regiones, salvo casos específicamente territoriales.
      - Transferencia puede incluir adaptación, priorización y focalización de instrumentos nacionales y ejecución directa de recursos.

  Requisitos_Generales_Transferencia:
    ID: TRANSF-COMP-REQ-GEN
    Def: Condiciones mínimas de toda transferencia (Art.21 quinquies).
    Recursos_y_Personal:
      ID: TRANSF-COMP-REQ-REC
      Def: Debe considerar recursos económicos y personal necesario, según competencia y presupuesto disponible.
      Req:
        - En transferencias temporales, ministerio/servicio puede designar funcionarios en comisión de servicio en GORE, por plazo equivalente a duración de competencia.
        - En transferencias definitivas, comisión de servicio solo puede extenderse hasta plazo máximo del Estatuto Administrativo.
        - Órgano que transfiere no puede crear empleos a contrata para labores similares a las transferidas.
        - Recursos para ejercicio de competencia se transfieren mediante convenios GORE–órgano central o por Ley de Presupuestos.
        - Consejo de Evaluación de Competencias evalúa ejecución de recursos, considerando diversidad regional.
    No_Duplicidad:
      ID: TRANSF-COMP-REQ-NO-DUP
      Def: Debe evitarse duplicidad o interferencia con funciones de otros órganos.
    Plazo_Temporalidad:
      ID: TRANSF-COMP-REQ-PLAZO
      Def: Transferencias temporales deben indicar período de vigencia, no inferior a 1 año.

  Actores_Involucrados:
    ID: TRANSF-COMP-ACTORES
    Def: Actores formales del procedimiento (Art.21 sexies).
    Ref:
      - ORG-PRESIDENTE-CL
      - ORG-SUBDERE
    Items:
      - Presidente de la República: inicia procedimiento de oficio, resuelve transferencias mediante decreto supremo fundado cuando informe del Comité es positivo.
      - Comité Interministerial de Descentralización: presidido por Ministro del Interior, integrado por Ministros de Hacienda, Secretaría General de la Presidencia y ministros sectoriales; asesora al Presidente, cuenta con Secretaría Ejecutiva ejercida por la Subsecretaría de Desarrollo Regional y Administrativo, y formula recomendaciones sobre transferencias.
      - Comisiones de Estudios por Materias: integradas paritariamente por representantes del nivel central y del Gobierno Regional; analizan antecedentes y emiten informes fundados.

  Procedimiento_Transferencia:
    ID: TRANSF-COMP-PROC
    Def: Reglas procedimentales comunes y específicas (Art.21 septies).
    Procedimiento_Solicitado_por_GORE:
      ID: TRANSF-COMP-PROC-GORE
      Steps:
        - Consejo Regional aprueba solicitud (mayoría absoluta con propuesta del Gobernador o 2/3 si iniciativa propia), dentro de 24 meses desde inicio periodo presidencial.
        - Solicitud debe incluir estudios de impacto financiero, eficacia y eficiencia.
        - Comité Interministerial instruye comisión de estudios para analizar antecedentes y emitir informe fundado.
        - Informe puede proponer transferir competencia en mismos términos o con condiciones diferentes; modificaciones requieren nueva aprobación del Consejo Regional.
        - Comité Interministerial aprueba o rechaza recomendación. Si aprueba, remite al Presidente; si rechaza, se dicta decreto fundado de rechazo.
        - Presidente dicta decreto supremo fundado aprobando o rechazando transferencia, suscrito por ministros competentes.
        - Falta de pronunciamiento en 6 meses obliga al Comité a responder expresa y fundadamente.

    Procedimiento_Iniciado_de_Oficio:
      ID: TRANSF-COMP-PROC-OFICIO
      Steps:
        - Presidente instruye al Comité iniciar evaluación de transferencia específica.
        - Si Comité recomienda transferir, se remite propuesta al Gobierno Regional para ratificación del Consejo Regional (mayoría absoluta con Gobernador o 2/3 sin él).
        - Ratificada la propuesta, Presidente resuelve mediante decreto supremo suscrito por ministros competentes.
        - Si Comité recomienda no transferir o GORE no ratifica, procedimiento concluye sin transferencia, sin perjuicio de futura solicitud regional.

    Reglas_Comunes_y_Evaluacion:
      ID: TRANSF-COMP-PROC-COMUN
      Req:
        - Decreto de transferencia debe indicar competencias y recursos transferidos, carácter temporal o definitivo, gradualidad, condiciones de ejercicio, exclusividad o coparticipación, mecanismos de seguimiento y evaluación, indicadores y fuentes de información.
        - Procedimiento tiene duración máxima de 6 meses desde solicitud o instrucción presidencial.
        - Reglamento dictado por Ministerio del Interior y Seguridad Pública (con Ministros de Hacienda y Secretaría General) fija condiciones y plazos detallados.
      Evaluacion_Ejercicio_Competencias:
        ID: TRANSF-COMP-EVAL
        Def: Consejo de Evaluación de Competencias evalúa objetivamente el ejercicio (Art.21 septies D).
        Ref:
          - ORG-SUBDERE
        Req:
          - Evaluación posterior al término del plazo temporal o a 3 años en transferencias definitivas.
          - Considera indicadores cualitativos y cuantitativos y formula recomendaciones de mejora.
          - Resultados pueden incorporarse en programas de mejoramiento de la gestión y metas de desempeño institucional.
          - Reglamento específico define procedimiento y metodología de la evaluación.
          - Resultados de la evaluación deben remitirse por la Subsecretaría de Desarrollo Regional y Administrativo, dentro de 30 días, al Presidente de la República, al Congreso Nacional y al gobierno regional respectivo.

  Revocacion_Competencias:
    ID: TRANSF-COMP-REVOC
    Def: Reglas de revocación de competencias transferidas (Art.21 octies).
    Req:
      - Competencias transferidas definitivamente solo pueden revocarse por ley.
      - Transferencias temporales pueden revocarse de oficio en forma fundada por:
          - Incumplimiento de condiciones de ejercicio.
          - Deficiente prestación del servicio a la comunidad.
          - Ejercicio incompatible con políticas públicas nacionales dictadas con posterioridad, sin que GORE ajuste dentro de 6 meses.
      - GORE puede solicitar revocación de competencias transferidas mediante acuerdo del Consejo Regional (mayoría absoluta con Gobernador o 2/3 sin él).
      - Comité Interministerial instruye comisión de estudio para recabar antecedentes, definir condiciones de corrección y plazo; si no se corrige, informa al Comité para decisión presidencial.
      - Revocación se resuelve por decreto supremo dictado a más tardar 30 de junio y entra en vigencia el 1 de enero del año siguiente.

Organos_Gobierno_Regional_y_Gobernador:
  ID: MOD-ORG-GORE
  Ref:
    - DEF-GORE
    - DEF-GOBERNADOR-REG
    - DEF-CONSEJO-REG

  Organos_Del_GORE:
    ID: ORG-GORE-LIST
    Def: Órganos que integran el Gobierno Regional (Art.22).
    Ref:
      - DEF-GORE
      - DEF-CONSEJO-REG
    Items:
      - Gobernador Regional.
      - Consejo Regional.
    Req:
      - Cuando la ley requiere opinión o acuerdo del Gobierno Regional, el Gobernador, como órgano ejecutivo, debe someterlo previamente al acuerdo del Consejo Regional.

  Gobernador_Regional:
    ID: ORG-GOBERNADOR
    Ref_Def: DEF-GOBERNADOR-REG

    Naturaleza_y_Eleccion:
      ID: GOB-REG-NAT-ELEC
      Def: Órgano ejecutivo del Gobierno Regional, preside el Consejo Regional (Art.23).
      Req:
        - Ejercicio de funciones conforme a la Constitución.
        - Es elegido por sufragio universal, en votación directa, en cédula separada y conjuntamente con la elección de consejeros regionales, conforme normas legales.

    Requisitos_Para_Ser_Elegido:
      ID: GOB-REG-REQ-ELEC
      Def: Requisitos de elegibilidad (Art.23 bis).
      Req:
        - Ser ciudadano con derecho a sufragio.
        - No estar inhabilitado para funciones o cargos públicos.
        - No estar sujeto a procedimiento concursal de liquidación ni haber sido condenado por crimen o simple delito.
        - Haber cursado enseñanza media o equivalente.
        - Residir en la región respectiva al menos 2 años antes de la elección.
        - No estar afecto a inhabilidades especiales establecidas en la ley.
        - No tener dependencia de drogas estupefacientes o sicotrópicas ilegales salvo uso médico justificado, acreditado mediante declaración jurada.

    Inhabilidades_Para_Candidaturas:
      ID: GOB-REG-INHAB-CAND
      Def: Personas inhabilitadas para ser candidatas a Gobernador Regional (Art.23 ter).
      Items:
        - Altas autoridades del nivel central (ministros, subsecretarios, delegados presidenciales, SEREMI, miembros de Banco Central, Contralor).
        - Diputados y senadores.
        - Alcaldes y concejales.
        - Miembros y funcionarios del Poder Judicial, Ministerio Público, Contraloría, Tribunal Constitucional, tribunales especiales y electorales, Consejo para la Transparencia, SERVEL y miembros activos de FF.AA. y de Orden y Seguridad.
        - Personas con contratos o cauciones significativos (≥200 UTM) o litigios pendientes con el respectivo GORE, incluyendo representantes o socios relevantes de sociedades en similar situación.
        - Personas condenadas por crimen o simple delito con pena aflictiva.
        - Personas sancionadas por infracciones graves a normas sobre financiamiento electoral.
        - Personas inscritas en el Registro Nacional de Deudores de Pensiones de Alimentos.
      Extensiones_Temporales:
        ID: GOB-REG-INHAB-TIEMPO
        Def: Algunas inhabilidades se aplican a quienes hayan ejercido cargos mencionados dentro del año anterior a la elección.

    Incompatibilidades_Del_Cargo:
      ID: GOB-REG-INCOMP
      Def: Incompatibilidades funcionales del Gobernador Regional (Art.23 quáter).
      Prohib:
        - No puede ejercer simultáneamente cargos de Presidente de la República, parlamentario, consejero regional, alcalde, concejal u otros empleos o comisiones retribuidos con fondos públicos, salvo docencia hasta 12 horas semanales.
        - No puede ser director o consejero, aun ad honorem, en entidades autónomas fiscales, semifiscales o empresas estatales o con participación estatal.

    Inhabilidades_Sobrevinientes:
      ID: GOB-REG-INHAB-SOBR
      Def: Supuestos que inhabilitan para desempeñar el cargo (Art.23 quinquies).
      Items:
        - Configuración de situaciones de conflicto económico con el GORE análogas a las de candidatos (contratos, cauciones, litigios).
        - Actuar como abogado o mandatario en juicios contra el respectivo GORE.

    Causales_y_Procedimiento_Cese:
      ID: GOB-REG-CESE
      Def: Causales de cesación y procedimientos (Art.23 sexies).
      Causales:
        ID: GOB-REG-CESE-CAUS
        Items:
          - Pérdida de calidad de ciudadano.
          - Incapacidad psíquica o física para el cargo.
          - Contravención grave al principio de probidad, notable abandono de deberes o incompatibilidades graves.
          - Renuncia aceptada por el Consejo Regional (salvo renuncia por postulación a otro cargo de elección popular, que no requiere acuerdo).
          - Inhabilidad sobreviniente.
          - Condena en acusación constitucional.
          - Infracción grave a normas de transparencia, límites y control del gasto electoral.
      Organos_Competentes_y_Procedimientos:
        ID: GOB-REG-CESE-PROC
        Ref:
          - DEF-GOBERNADOR-REG
          - DEF-CONSEJO-REG
          - ORG-TRICEL
        Items:
          - Tribunal Calificador de Elecciones declara pérdida de ciudadanía, incapacidad o inhabilidades sobrevinientes, a requerimiento de un tercio de consejeros o por acción pública según causal.
          - Mismo Tribunal declara notable abandono de deberes o contravención grave a probidad, a requerimiento de al menos un tercio de consejeros regionales.
          - Tribunal Calificador puede imponer cesación o medidas disciplinarias del Estatuto Administrativo.
          - Cesación por algunas causales solo produce efectos una vez ejecutoriada la resolución; en probidad/abandono, puede haber suspensión desde sentencia de primera instancia.
          - En caso de condena firme por probidad/abandono, inhabilidad para cualquier cargo público por 5 años.
          - En procedimientos por notable abandono de deberes o contravención grave a probidad se aplica el procedimiento de la ley N° 18.593 sobre tribunales electorales regionales y no se requiere patrocinio de abogado.
          - El Tribunal Calificador debe acumular antecedentes para evitar doble pronunciamiento sobre una misma materia.
          - El Gobernador Regional que estime estar afecto a una causal de inhabilidad debe informarla al Consejo Regional tan pronto tenga conocimiento de ella.
          - Se detalla concepto de notable abandono de deberes asociado a infracción grave de obligaciones constitucionales/legales o grave detrimento al patrimonio o servicios del GORE.
