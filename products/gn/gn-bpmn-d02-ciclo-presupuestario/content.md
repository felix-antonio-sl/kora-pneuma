---
urn: urn:gn:kb:gn-bpmn-d02-ciclo-presupuestario
nombre: gn-bpmn-d02-ciclo-presupuestario
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – BPMN D02: Ciclo Presupuestario Regional; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml (sha256:bbb3612714e061f306087001083128ae701c0fa6da781ed7a46cf7318b4e4bd7); URN KODA legado urn:gorenuble:gn:bpmn-d02-ciclo-presupuestario:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02. Corrección editorial 1.0.1 (2026-08-09): reemplaza rutas `file://` no portables de referencias cruzadas por URN KORA resolubles."
autor: "FS"
creado: 2025-12-22
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "bpmn", "d02"]
familia: bok
---
# Artefacto KODA/Spec – BPMN D02: Ciclo Presupuestario Regional
# Fuente: sources/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md
---
_manifest:
  urn: "urn:gorenuble:gn:bpmn-d02-ciclo-presupuestario:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:gestion-prpto:1.0.0"
        reason: "Guía integral de gestión presupuestaria regional"
  provenance:
    created_by: "FS"
    created_at: "2025-12-22"
    last_modified_at: "2025-12-22"
    model_collaborators: ["Cascade", "KODA-TRANSFORMER"]

ID: BPMN-GN-D02-CICLO-PRESUPUESTARIO-KODA
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
Ctx: "Especificación STS del dominio D02: Ciclo Presupuestario Regional del GORE Ñuble, modelado en BPMN."
Source:
  Ctx_Required:
    - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml"
    - "knowledge/domains/gn/presupuesto/kb_gn_018_gestion_prpto_koda.yml"
  Primary-Source: "sources/gn/arquitectura/bpmn/D02_ciclo_presupuestario.md"

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
  ID: DOM-PRESUPUESTO
  Criticidad: "🔴 Crítica"
  Dueno: "DAF (Funcionamiento) / DIPIR (Inversión)"
  Procesos: 5
  Subprocesos: "~15"
  Ref_Fuente:
    Ctx_Required:
      - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.500-1886"

Mapa_General_Dominio:
  ID: BPMN-GN-PRESUPUESTO-MAPA-01
  Cpt: "Mapa general del ciclo anual del presupuesto regional (P1–P5) y proceso transversal de modificaciones presupuestarias."
  Mermaid: |
    flowchart LR
        subgraph CICLO["📅 Ciclo Anual"]
            P1["P1: Formulación<br/>(May-Jun)"]
            P2["P2: Aprobación<br/>(Sep-Nov)"]
            P3["P3: Distribución<br/>(Dic-Ene)"]
            P4["P4: Ejecución<br/>(Todo el año)"]
            P5["P5: Control y<br/>Cierre (Dic-Ene)"]
        end

        subgraph TRANSVERSAL["🔄 Transversal"]
            PM["Modificaciones<br/>Presupuestarias"]
        end

        P1 --> P2 --> P3 --> P4 --> P5
        P4 <--> PM
        P5 -.->|"Retroalimentación"| P1

        style P1 fill:#2196F3,color:#fff
        style P2 fill:#4CAF50,color:#fff
        style P3 fill:#FF9800,color:#fff
        style P4 fill:#9C27B0,color:#fff
        style P5 fill:#607D8B,color:#fff
        style PM fill:#E91E63,color:#fff

P1_Formulacion_del_Presupuesto:
  ID: BPMN-GN-PRESUPUESTO-FORMULACION-01
  Periodo: "Mayo-Junio (año anterior)"
  Diagrama_de_Flujo:
    Mermaid: |
      flowchart TD
          A["📜 DIPRES emite<br/>instructivo y clasificador"] --> B["Definir techos<br/>preliminares"]

          subgraph INVERSION["💼 Inversión (DIPIR)"]
              C1["Propuesta marco<br/>de inversión"]
              C2["Cartera proyectos<br/>con RS vigente"]
              C3["Asignaciones por<br/>fuente (FNDR/FRIL/FRPD)"]
          end

          subgraph FUNCIONAMIENTO["🏢 Funcionamiento (DAF)"]
              D1["Personal (Subt. 21)"]
              D2["Bienes/Servicios (Subt. 22)"]
              D3["Transferencias (Subt. 24)"]
          end

          B --> C1 & D1
          C1 --> C2 --> C3
          D1 --> D2 --> D3
          C3 & D3 --> E["Consolidación<br/>propuesta"]
          E --> F["Presentación a<br/>Gobernador/a"]
          F --> G["Ajustes según<br/>prioridades ERD"]
          G --> H["📤 Envío a DIPRES"]

          style A fill:#2196F3,color:#fff
          style H fill:#4CAF50,color:#fff
  Estructura_Presupuesto:
    ID: BPMN-GN-PRESUPUESTO-ESTRUCTURA-01
    Filas:
      - Subtitulo: 21
        Concepto: "Personal"
        Responsable: "DAF"
      - Subtitulo: 22
        Concepto: "Bienes y Servicios"
        Responsable: "DAF"
      - Subtitulo: 24
        Concepto: "Transferencias Corrientes"
        Responsable: "DAF/DIPIR"
      - Subtitulo: 29
        Concepto: "Activos No Financieros"
        Responsable: "DAF"
      - Subtitulo: 31
        Concepto: "Inversión (Iniciativas)"
        Responsable: "DIPIR"
      - Subtitulo: 33
        Concepto: "Transferencias de Capital"
        Responsable: "DIPIR"

P2_Aprobacion_del_Presupuesto:
  ID: BPMN-GN-PRESUPUESTO-APROBACION-01
  Cpt: "Proceso de aprobación del presupuesto regional (Gobernador, CORE, DIPRES, CGR)."
  # Diagrama completo y tablas de requisitos se modelarían aquí siguiendo el detalle del markdown fuente.

P3_Distribucion_Inicial:
  ID: BPMN-GN-PRESUPUESTO-DISTRIBUCION-01
  Cpt: "Distribución inicial del presupuesto aprobado y carga en SIGFE."

P4_Ejecucion_Presupuestaria:
  ID: BPMN-GN-PRESUPUESTO-EJECUCION-01
  Cpt: "Ejecución durante el año, con seguimiento de compromisos, devengos y pagos."

P5_Control_y_Cierre_de_Ejercicio:
  ID: BPMN-GN-PRESUPUESTO-CIERRE-01
  Periodo: "Diciembre-Enero"
  Diagrama_de_Flujo:
    Mermaid: |
      flowchart TD
          subgraph CONTROL["🔍 Control Durante el Año"]
              A["Control interno<br/>(DAF, DIPIR, U. Control)"]
              B["Seguimiento DIPRES<br/>(mensual)"]
              C["Sistema KPIs y<br/>alertas tempranas"]
          end

          subgraph CIERRE["📅 Cierre 31/12"]
              D["Consolidar<br/>información (DAF)"]
              E["Cerrar cuentas<br/>en SIGFE"]
              F["Calcular deuda<br/>flotante"]
              G["Regularizar<br/>deuda flotante"]
              H["Informe cierre<br/>a DIPRES/CGR"]
          end

          subgraph EVALUACION["📊 Evaluación"]
              I["Evaluar resultados<br/>físicos y financieros"]
              J["Informe evaluación<br/>ex post (DIPIR)"]
          end

          A & B & C --> D --> E --> F --> G --> H
          H --> I --> J

          style H fill:#607D8B,color:#fff
          style J fill:#9C27B0,color:#fff
  Deuda_Flotante:
    ID: BPMN-GN-PRESUPUESTO-DEUDA-FLOTANTE-01
    Mermaid: |
      flowchart TD
          A["Obligaciones devengadas<br/>al 31/12 pendientes<br/>de pago"] --> B{"¿SIC<br/>suficiente?"}
          B -->|"Sí"| C["Financiar con<br/>SIC"]
          B -->|"No"| D["SIC + Mayor<br/>aporte fiscal"]
          C & D --> E["Incorporar en<br/>presupuesto año siguiente"]
          E --> F["Primera prioridad<br/>de pago"]

          style F fill:#FF9800,color:#fff
  Reporteria_Oficial:
    ID: BPMN-GN-PRESUPUESTO-REPORTES-01
    Filas:
      - Reporte: "Informe Ejecución Mensual"
        Frecuencia: "Mensual"
        Destinatario: "DIPRES, CORE"
      - Reporte: "Informes por Glosas"
        Frecuencia: "Trimestral"
        Destinatario: "Transparencia"
      - Reporte: "Cartera de Proyectos"
        Frecuencia: "Mensual"
        Destinatario: "Web institucional"
      - Reporte: "Acuerdos CORE"
        Frecuencia: "5 días hábiles"
        Destinatario: "Web institucional"

Sistemas_Involucrados:
  ID: BPMN-GN-PRESUPUESTO-SISTEMAS-01
  Filas:
    - Sistema: "SYS-SIGFE"
      Funcion: "Gestión financiera central"
    - Sistema: "SYS-BIP-SNI"
      Funcion: "Inversión pública"
    - Sistema: "SYS-TRANSPARENCIA"
      Funcion: "Publicación información"

Normativa_Aplicable:
  ID: BPMN-GN-PRESUPUESTO-NORMATIVA-01
  Filas:
    - Norma: "LOC 19.175 Art. 72-73"
      Alcance: "Competencias presupuestarias"
    - Norma: "Decreto 854/2004 Hacienda"
      Alcance: "Clasificador presupuestario"
    - Norma: "Ley de Presupuestos (anual)"
      Alcance: "Marco legal ejercicio"
    - Norma: "Glosa 14 Partida 31"
      Alcance: "3% emergencias"
    - Norma: "Glosa 16 Partida 31"
      Alcance: "Transparencia"
    - Norma: "NICSP-CGR"
      Alcance: "Contabilidad gubernamental"
    - Norma: "Resolución 30/2015 CGR"
      Alcance: "Rendiciones"

Referencias_Cruzadas:
  ID: BPMN-GN-PRESUPUESTO-REFERENCIAS-01
  Filas:
    - Dominio_Relacionado: "D03 Gestión IPR"
      Ctx_Optional:
        - "urn:gn:kb:gn-bpmn-d03-gestion-ipr"
      Vinculo: "CDP, financiamiento proyectos"
    - Dominio_Relacionado: "D08 Rendiciones"
      Ctx_Optional:
        - "urn:gn:kb:bpmn-d08-rendiciones"
      Vinculo: "Contabilización, SIGFE"
    - Dominio_Relacionado: "D04 Compras"
      Ctx_Optional:
        - "urn:gn:kb:gn-bpmn-d04-compras-contrataciones"
      Vinculo: "Órdenes de compra, contratos"

Ultima_Actualizacion:
  ID: BPMN-GN-PRESUPUESTO-ULT-ACT-01
  Cpt: "Última actualización: 2025-12-16"
