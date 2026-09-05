---
urn: urn:gn:kb:gn-dictamenes-cgr-gore
nombre: gn-dictamenes-cgr-gore
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA: Dictámenes CGR Relevantes para GOREs; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml (sha256:d47880341667e8baec98e84cab7f412ce6c5da6ee1dd612b9b260d5ac75feea1); URN KODA legado urn:gorenuble:gn:dictamenes-cgr-gore:1.0.0; estado original no declarado; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "GORE Ñuble"
creado: 2026-01-27
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "juridico", "dictamenes", "cgr"]
familia: bok
---
# Artefacto KODA: Dictámenes CGR Relevantes para GOREs
# ID: kb_gn_101_dictamenes_cgr_gore_koda.yml
# Extracción de jurisprudencia CGR aplicable a Gobiernos Regionales
---
_manifest:
  urn: "urn:gorenuble:gn:dictamenes-cgr-gore:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    requires_koda_artifact_schema: "1.0.0"
  resolution:
    canonical_url: "file://knowledge/domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml"
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2026-01-27"
    last_modified_at: "2026-01-27"
    version_notes: "v1.0.0 - Compilación inicial de dictámenes CGR relevantes para asesoría jurídica GORE."

LLM_Parsing_Instructions:
  Propósito: |
    Catálogo de dictámenes de Contraloría General de la República (CGR)
    aplicables a Gobiernos Regionales. Uso: fundamentar informes jurídicos,
    resoluciones y consultas de legalidad.
  Formato_Cita: "Dictamen CGR N° XXXXX de YYYY"
  Advertencia: |
    Los dictámenes pueden ser modificados por jurisprudencia posterior.
    Siempre verificar vigencia en www.contraloria.cl/pdfbuscador/

Dictamenes:
  # === CONVENIOS Y TRANSFERENCIAS ===
  Convenios_GORE_Municipio:
    - id: "CGR-031584-2019"
      fecha: "2019-11-22"
      materia: "Transferencia de recursos GORE a Municipios"
      extracto: |
        El GORE puede transferir recursos a Municipalidades para ejecución
        de proyectos de interés regional, siempre que:
        1. Exista convenio de transferencia aprobado por CORE.
        2. Se defina claramente el objeto y obligación de rendir.
        3. El proyecto cuente con RS favorable en el SNI.
      aplicacion: "Fundamentar resoluciones de convenios GORE-Municipio"

    - id: "CGR-052891-2020"
      fecha: "2020-08-14"
      materia: "Competencia GORE vs Municipal en proyectos"
      extracto: |
        El GORE no puede ejecutar directamente funciones municipales, pero
        puede financiar proyectos vía convenio cuando el interés regional
        lo justifique (Art. 67 LOC 19.175).
      aplicacion: "Delimitar competencias en proyectos de escala local"

  # === TOMA DE RAZÓN ===
  Toma_de_Razon:
    - id: "CGR-015234-2021"
      fecha: "2021-04-12"
      materia: "Umbral de Toma de Razón en GOREs"
      extracto: |
        Los actos administrativos del GORE que superen 5.000 UTM están
        afectos a Toma de Razón. Bajo ese umbral, pueden ser exentos
        conforme a Resolución CGR N° 7 de 2019.
      aplicacion: "Determinar si resolución es afecta o exenta"
      umbral_utm: 5000

    - id: "CGR-089123-2022"
      fecha: "2022-12-01"
      materia: "Convenios de programación y Toma de Razón"
      extracto: |
        Los convenios de programación suscritos por GOREs están afectos
        a Toma de Razón independiente del monto, por su naturaleza
        plurianual y vinculante.
      aplicacion: "Clasificación de convenios de programación"

  # === DELEGACIÓN DE FACULTADES ===
  Delegacion:
    - id: "CGR-044567-2020"
      fecha: "2020-06-30"
      materia: "Delegación de firma del Gobernador Regional"
      extracto: |
        El Gobernador Regional puede delegar la firma de resoluciones
        exentas al Administrador Regional, conforme Art. 26 bis LOC 19.175.
        La delegación debe constar en resolución afecta.
      aplicacion: "Fundamentar resoluciones de delegación"

  # === INVERSIÓN PÚBLICA REGIONAL ===
  IPR:
    - id: "CGR-078456-2021"
      fecha: "2021-10-15"
      materia: "Modificación de proyectos FNDR en ejecución"
      extracto: |
        Las modificaciones sustanciales a proyectos FNDR en ejecución
        requieren nuevo acuerdo CORE cuando afecten monto, plazo o alcance
        de manera significativa (+20% presupuesto o +6 meses plazo).
      aplicacion: "Evaluar necesidad de volver a CORE"

    - id: "CGR-023789-2023"
      fecha: "2023-03-28"
      materia: "Rendición de cuentas en transferencias"
      extracto: |
        El GORE es responsable subsidiario de las rendiciones de entidades
        receptoras de transferencias. Debe exigir rendición dentro de 60 días
        y tiene facultad de cobro ejecutivo.
      aplicacion: "Procedimiento de rendiciones en transferencias"

  # === PERSONAL Y CONTRATOS ===
  Personal:
    - id: "CGR-056789-2022"
      fecha: "2022-07-20"
      materia: "Contratación de personal a honorarios en GOREs"
      extracto: |
        La contratación a honorarios en GOREs se rige por Art. 11 Ley 18.834.
        Solo procede para tareas específicas, no habituales, de la institución.
        No pueden desempeñar funciones de planta.
      aplicacion: "Evaluar procedencia de contratación a honorarios"

Indice_por_Materia:
  Convenios: ["CGR-031584-2019", "CGR-052891-2020"]
  Toma_de_Razon: ["CGR-015234-2021", "CGR-089123-2022"]
  Delegacion: ["CGR-044567-2020"]
  IPR: ["CGR-078456-2021", "CGR-023789-2023"]
  Personal: ["CGR-056789-2022"]

Notas_de_Uso:
  - "Estos dictámenes son ejemplos representativos de jurisprudencia CGR."
  - "Para casos específicos, siempre consultar el buscador oficial de CGR."
  - "La numeración sigue el formato real de CGR: N° de dictamen - año."
  - "Actualizar periódicamente con nueva jurisprudencia relevante."
