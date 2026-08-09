---
urn: urn:gn:kb:gn-bpmn-d01-actos-administrativos
nombre: gn-bpmn-d01-actos-administrativos
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – BPMN D01: Tramitación de Actos Administrativos; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml (sha256:4a0d3d345ad0d6641f7c8529de3ab73f4cdde1e3894b9bdc936e02f32ce2f419); URN KODA legado urn:gorenuble:gn:bpmn-d01-actos-administrativos:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02. Corrección editorial 1.0.1 (2026-08-09): reemplaza rutas `file://` no portables de referencias cruzadas por URN KORA resolubles."
autor: "FS"
creado: 2025-12-22
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "bpmn", "d01"]
familia: bok
---
# Artefacto KODA/Spec – BPMN D01: Tramitación de Actos Administrativos
# Fuente: sources/gn/arquitectura/bpmn/D01_actos_administrativos.md
---
_manifest:
  urn: "urn:gorenuble:gn:bpmn-d01-actos-administrativos:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/arquitectura/bpmn/D01_actos_administrativos_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:bpmn-c4:1.0.0"
        reason: "Marco integrado de procesos BPMN y arquitectura C4"
  provenance:
    created_by: "FS"
    created_at: "2025-12-22"
    last_modified_at: "2025-12-22"
    model_collaborators: ["Cascade", "KODA-TRANSFORMER"]

ID: BPMN-GN-D01-ACTOS-ADMIN-KODA
Version: 1.0.0
Status: Draft
Format: KODA/Spec
Human-Creator: FS
Human-Editor: FS
Model-Collaborator:
  - Cascade
AI-Remediator: KODA-TRANSFORMER
Creation-Date: 2025-12-22
Modification-Date: 2025-12-22
Ctx: "Especificación STS del dominio D01: Tramitación de Actos Administrativos del GORE Ñuble, modelado en BPMN."
Source:
  Ctx_Required:
    - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml"
  Primary-Source: "sources/gn/arquitectura/bpmn/D01_actos_administrativos.md"

LLM_Parsing_Instructions:
  ID: KODA-LLM-PARSER-01
  Req: Mandatory block following Metadata.
  Prohib: Using for artifact creation or translation.
  Content: |
    BEGIN_LLM_INSTRUCTIONS
    You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

    FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

    LEXICON (expand before processing): Act->Action, Cond->Condition, Cpt->Concept, Ctx->Context, Def->Definition, Fnd->Foundation, ID->ID, Mech->Mechanism, Mssn->Mission, Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Resp->Responsible, Src->Source, Warn->Warning.

    REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx: or Src:.

    LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
    END_LLM_INSTRUCTIONS

Metadatos_Dominio:
  ID: DOM-ACTOS-ADMIN
  Criticidad: "🟠 Alta"
  Dueno: "Unidad Jurídica"
  Procesos: 2
  Subprocesos: "~14 fases"
  Ref_Fuente:
    Ctx_Required:
      - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.100-499"

Mapa_General_Dominio:
  ID: BPMN-GN-ACTOS-ADMIN-MAPA-01
  Cpt: "Mapa general de los procesos de actos administrativos (resoluciones exentas y convenios/transferencias) y elementos transversales."
  Mermaid: |
    flowchart LR
        subgraph PROCESOS["📋 Procesos de Actos Administrativos"]
            P1["P1: Resoluciones<br/>Exentas"]
            P2["P2: Convenios y<br/>Transferencias"]
        end

        subgraph TRANSVERSAL["🔧 Elementos Transversales"]
            T1["Expediente<br/>Electrónico"]
            T2["Firma Electrónica<br/>Avanzada"]
            T3["Toma de Razón<br/>(cuando aplica)"]
        end

        P1 --> T1 & T2
        P2 --> T1 & T2 & T3

        style P1 fill:#2196F3,color:#fff
        style P2 fill:#4CAF50,color:#fff

P1_Flujo_Resoluciones_Exentas:
  ID: BPMN-GN-RES-EXENTAS-FLUJO-01
  Fases: 7
  SLA: "15 días hábiles"
  Diagrama_de_Flujo_Completo:
    Mermaid: |
      flowchart TD
          subgraph FASE1["1️⃣ Iniciación"]
              A["Área Requirente:<br/>Elaborar borrador"]
              B["Adjuntar<br/>antecedentes"]
              C["Ingresar al SGD"]
          end

          subgraph FASE2["2️⃣ Revisión Jurídica"]
              D["Jurídica recibe<br/>expediente"]
              E["Verificar legalidad<br/>y forma"]
              F{"¿OK?"}
              G["✅ V°B° Jurídico"]
              H["❌ Observar"]
          end

          subgraph FASE3["3️⃣ Gestión"]
              I["Centro Gestión:<br/>Asignar N° resolución"]
              J["Completar<br/>formalidades"]
          end

          subgraph FASE4["4️⃣ Control"]
              K["Unidad Control:<br/>Verificar procedencia"]
              L{"¿Conforme?"}
              M["✅ V°B° Control"]
              N["❌ Reparar"]
          end

          subgraph FASE5["5️⃣ V°B° Administrador/a"]
              O["Administrador/a Regional:<br/>Revisar y visar"]
          end

          subgraph FASE6["6️⃣ Firma"]
              P["Gobernador/a:<br/>Firma con FEA"]
          end

          subgraph FASE7["7️⃣ Notificación y Archivo"]
              Q["Oficina Partes:<br/>Numerar y fechar"]
              R["Notificar a<br/>interesados"]
              S["Publicar si<br/>corresponde"]
              T["Archivar expediente"]
          end

          A --> B --> C --> D --> E --> F
          F -->|"Sí"| G --> I --> J --> K --> L
          F -->|"No"| H --> A
          L -->|"Sí"| M --> O --> P --> Q --> R --> S --> T
          L -->|"No"| N --> A

          style P fill:#4CAF50,color:#fff
          style T fill:#607D8B,color:#fff
  Roles_por_Fase:
    ID: BPMN-GN-RES-EXENTAS-ROLES-01
    Filas:
      - Fase: "Iniciación"
        Responsable: "Área Requirente"
      - Fase: "Revisión Jurídica"
        Responsable: "Unidad Jurídica"
      - Fase: "Gestión"
        Responsable: "Centro de Gestión"
      - Fase: "Control"
        Responsable: "Unidad de Control"
      - Fase: "V°B° Administrador/a"
        Responsable: "Administrador/a Regional"
      - Fase: "Firma"
        Responsable: "Gobernador/a Regional"
      - Fase: "Notificación y Archivo"
        Responsable: "Oficina de Partes"

P2_Convenios_y_Transferencias:
  ID: BPMN-GN-CONVENIOS-TRANSFERENCIAS-01
  Cpt: "Proceso para la tramitación de convenios y transferencias asociadas a actos administrativos."
  Diagrama_de_Flujo:
    Mermaid: |
      flowchart TD
          A["Área requirente<br/>propone convenio"] --> B["Elaborar borrador<br/>de convenio"]
          B --> C["Revisión Jurídica"]
          C --> D{"¿Ajustes?"}
          D -->|"Sí"| B
          D -->|"No"| E["Resolución que<br/>aprueba convenio"]
          E --> F["Toma de Razón<br/>si corresponde"]
          F --> G["Firma de partes"]
          G --> H["Ejecución y<br/>seguimiento"]
  Contenido_Minimo_Convenio:
    ID: BPMN-GN-CONVENIOS-CONTENIDO-01
    Filas:
      - Elemento: "Partes"
        Descripcion: "GORE + Entidad receptora"
      - Elemento: "Objeto"
        Descripcion: "Descripción del programa/proyecto"
      - Elemento: "Monto"
        Descripcion: "Valor total y calendario"
      - Elemento: "Plazos"
        Descripcion: "Duración y fechas clave"
      - Elemento: "Obligaciones"
        Descripcion: "Deberes de cada parte"
      - Elemento: "Rendicion"
        Descripcion: "Modalidad, plazos, SISREC"
      - Elemento: "Restitucion"
        Descripcion: "Condiciones de devolución"
      - Elemento: "Probidad"
        Descripcion: "Cláusulas anticorrupción"
  Criterios_Toma_de_Razon:
    ID: BPMN-GN-CONVENIOS-TOMA-RAZON-01
    Mermaid: |
      flowchart TD
          A["Convenio<br/>firmado"] --> B{"Monto y<br/>naturaleza"}
          B -->|"Supera umbral<br/>CGR"| C["Requiere<br/>Toma de Razón"]
          B -->|"Bajo umbral"| D["Exento"]
          B -->|"Normativa<br/>específica"| E["Consultar<br/>Res. CGR"]

          style C fill:#f44336,color:#fff
          style D fill:#4CAF50,color:#fff

Expediente_Electronico_Ley_21180:
  ID: BPMN-GN-ACTOS-EXPEDIENTE-01
  Estructura_Expediente:
    Mermaid: |
      flowchart TD
          subgraph EXPEDIENTE["📁 Expediente Electrónico"]
              A["Metadatos:<br/>• ID único<br/>• Fecha creación<br/>• Tipo acto"]
              B["Documentos:<br/>• Borrador<br/>• Antecedentes<br/>• Visaciones"]
              C["Firmas:<br/>• FEA funcionarios<br/>• FEA autoridad"]
              D["Trazabilidad:<br/>• Log de acciones<br/>• Fechas/horas"]
          end

          A --> B --> C --> D

          style C fill:#2196F3,color:#fff
  Principios_TDE:
    ID: BPMN-GN-ACTOS-TDE-PRINCIPIOS-01
    Filas:
      - Principio: "Equivalencia funcional"
        Aplicacion: "Documento digital = papel"
      - Principio: "Neutralidad tecnológica"
        Aplicacion: "Sin dependencia de proveedor"
      - Principio: "Interoperabilidad"
        Aplicacion: "Comunicación entre sistemas"
      - Principio: "Seguridad"
        Aplicacion: "Integridad, autenticidad, no repudio"

Sistemas_Involucrados:
  ID: BPMN-GN-ACTOS-SISTEMAS-01
  Filas:
    - Sistema: "SYS-DOCDIGITAL"
      Funcion: "Gestión documental, expediente"
    - Sistema: "SYS-FIRMAGOB"
      Funcion: "Firma Electrónica Avanzada"
    - Sistema: "SYS-SIGFE"
      Funcion: "Registro de compromisos"
    - Sistema: "SYS-TRANSPARENCIA"
      Funcion: "Publicación"

Normativa_Aplicable:
  ID: BPMN-GN-ACTOS-NORMATIVA-01
  Filas:
    - Norma: "Ley 19.880 LBPA"
      Alcance: "Procedimiento administrativo"
    - Norma: "Ley 21.180 TDE"
      Alcance: "Expediente electrónico"
    - Norma: "Ley 19.799"
      Alcance: "Firma electrónica"
    - Norma: "Resolución 30/2015 CGR"
      Alcance: "Rendiciones"
    - Norma: "Ley 19.886"
      Alcance: "Contratación pública"

Referencias_Cruzadas:
  ID: BPMN-GN-ACTOS-REFERENCIAS-01
  Filas:
    - Dominio_Relacionado: "D03 Gestión IPR"
      Ctx_Optional:
        - "urn:gn:kb:gn-bpmn-d03-gestion-ipr"
      Vinculo: "Fase 4 Formalización"
    - Dominio_Relacionado: "D02 Ciclo Presupuestario"
      Ctx_Optional:
        - "urn:gn:kb:gn-bpmn-d02-ciclo-presupuestario"
      Vinculo: "Modificaciones, resoluciones"
    - Dominio_Relacionado: "D08 Rendiciones"
      Ctx_Optional:
        - "urn:gn:kb:bpmn-d08-rendiciones"
      Vinculo: "Convenios de transferencia"

Ultima_Actualizacion:
  ID: BPMN-GN-ACTOS-ULT-ACT-01
  Cpt: "Última actualización: 2025-12-16"
