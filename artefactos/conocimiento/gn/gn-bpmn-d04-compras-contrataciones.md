---
urn: urn:gn:kb:gn-bpmn-d04-compras-contrataciones
nombre: gn-bpmn-d04-compras-contrataciones
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – BPMN D04: Compras Públicas y Contrataciones; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/bpmn/D04_compras_contrataciones_koda.yml (sha256:a6205efe5cf52092d647e31ca61b7d1052c172b6ec7c89ec6a8f3ad69db68529); URN KODA legado urn:gorenuble:gn:bpmn-d04-compras-contrataciones:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02. Corrección editorial 1.0.1 (2026-08-09): sustituye enlaces `file://` no portables por URN KORA cuando el dominio existe y conserva como texto la fuente externa sin URN."
autor: "FS"
creado: 2025-12-22
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "bpmn", "d04"]
familia: bok
---
# Artefacto KODA/Spec – BPMN D04: Compras Públicas y Contrataciones
# Fuente: sources/gn/arquitectura/bpmn/D04_compras_contrataciones.md
---
_manifest:
  urn: "urn:gorenuble:gn:bpmn-d04-compras-contrataciones:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/arquitectura/bpmn/D04_compras_contrataciones_koda.yml"
    mirrors: []
  dependencies:
    requires:
      - urn: "urn:kora:kb:spec:1.0.0"
        reason: "KODA/Spec format compliance"
      - urn: "urn:kora:kb:transform:1.0.0"
        reason: "Transformation methodology reference"
      - urn: "urn:gorenuble:gn:bpmn-c4:1.0.0"
        reason: "Marco integrado BPMN/C4"
  provenance:
    created_by: "FS"
    created_at: "2025-12-22"
    last_modified_at: "2025-12-22"
    model_collaborators: ["Cascade", "KODA-TRANSFORMER"]

ID: BPMN-GN-D04-COMPRAS-KODA
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
Ctx: "Especificación STS del dominio D04: Compras Públicas y Contrataciones del GORE Ñuble, modelado en BPMN."
Source:
  Ctx_Required:
    - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml"
  Primary-Source: "sources/gn/arquitectura/bpmn/D04_compras_contrataciones.md"

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
  ID: DOM-COMPRAS
  Criticidad: "🟠 Alta"
  Dueno: "Unidad de Abastecimiento"
  Procesos: 4
  Subprocesos: "~12"
  Ref_Fuente:
    Ctx_Required:
      - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.700-950"

Body_MD:
  ID: BPMN-GN-D04-COMPRAS-BODY-01
  Src: "sources/gn/arquitectura/bpmn/D04_compras_contrataciones.md"
  Content: |
    # D04: Compras Públicas y Contrataciones

    ## Metadatos del Dominio

    | Campo           | Valor                                                                                                                                                |
    | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **ID**          | `DOM-COMPRAS`                                                                                                                                        |
    | **Criticidad**  | 🟠 Alta                                                                                                                                               |
    | **Dueño**       | Unidad de Abastecimiento                                                                                                                             |
    | **Procesos**    | 4                                                                                                                                                    |
    | **Subprocesos** | ~12                                                                                                                                                  |
    | **Ref. Fuente** | `kb_gn_054_bpmn_c4_koda.yml` (fuente externa archivada; sin URN KORA) L.700-950 |

    ---

    ## Mapa General del Dominio

    ```mermaid
    flowchart LR
        subgraph CICLO["📋 Ciclo de Compras"]
            P1["P1: Plan Anual<br/>de Compras"]
            P2["P2: Licitación<br/>Pública"]
            P3["P3: Órdenes<br/>de Compra"]
            P4["P4: Gestión de<br/>Contratos"]
        end

        P1 --> P2 --> P3 --> P4
        P1 -->|"Convenio Marco"| P3

        style P1 fill:#2196F3,color:#fff
        style P2 fill:#FF9800,color:#fff
        style P3 fill:#4CAF50,color:#fff
        style P4 fill:#9C27B0,color:#fff
    ```

    ---

    ## P1: Plan Anual de Compras (PAC)

    | Campo       | Valor                    |
    | ----------- | ------------------------ |
    | **ID**      | `BPMN-GN-COMPRAS-PAC-01` |
    | **Período** | Anual (Diciembre-Enero)  |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        A["Divisiones identifican<br/>necesidades"] --> B["Unidades envían<br/>requerimientos"]
        B --> C["Abastecimiento consolida"]
        C --> D["Clasificar por:<br/>• Convenio Marco<br/>• Licitación<br/>• Compra Directa"]
        D --> E["Validación<br/>presupuestaria (DAF)"]
        E --> F["Aprobación<br/>Gobernador/a"]
        F --> G["Publicar PAC en<br/>Mercado Público"]
        G --> H["Monitoreo y<br/>ajustes trimestrales"]

        style G fill:#4CAF50,color:#fff
    ```

    ### Contenido del PAC

    | Elemento          | Descripción              |
    | ----------------- | ------------------------ |
    | Producto/Servicio | Descripción detallada    |
    | Cantidad estimada | Unidades requeridas      |
    | Monto estimado    | Valor en pesos           |
    | Período           | Trimestre de adquisición |
    | Mecanismo         | CM/LP/CD/TDP             |

    ---

    ## P2: Licitación Pública

    | Campo      | Valor                           |
    | ---------- | ------------------------------- |
    | **ID**     | `BPMN-GN-COMPRAS-MECANISMOS-01` |
    | **Umbral** | > 1.000 UTM                     |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        subgraph PREPARACION["📋 Preparación"]
            A["Elaborar bases<br/>técnicas y admin."]
            B["Revisión jurídica"]
            C["Resolución que<br/>aprueba bases"]
        end

        subgraph PUBLICACION["📤 Publicación"]
            D["Publicar en<br/>Mercado Público"]
            E["Período de<br/>consultas"]
            F["Respuestas y<br/>aclaraciones"]
            G["Recepción<br/>de ofertas"]
        end

        subgraph EVALUACION["🔍 Evaluación"]
            H["Comisión evaluadora<br/>revisa ofertas"]
            I["Aplicar criterios:<br/>• Precio<br/>• Calidad<br/>• Experiencia"]
            J["Acta de evaluación"]
            K["Propuesta de<br/>adjudicación"]
        end

        subgraph ADJUDICACION["✅ Adjudicación"]
            L["Resolución de<br/>adjudicación"]
            M["Publicar resultado"]
            N["Notificar a<br/>oferentes"]
            O["Período de<br/>impugnación"]
        end

        A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N --> O

        style L fill:#4CAF50,color:#fff
    ```

    ### Mecanismos de Compra

    ```mermaid
    flowchart TD
        A["Necesidad de<br/>adquisición"] --> B{"Monto<br/>estimado"}

        B -->|"> 1.000 UTM"| C["🏛️ Licitación<br/>Pública"]
        B -->|"100-1.000 UTM"| D["📋 Licitación<br/>Privada"]
        B -->|"< 100 UTM"| E["💳 Compra<br/>Directa"]

        A --> F{"¿Existe<br/>Convenio Marco?"}
        F -->|"Sí"| G["🛒 Convenio<br/>Marco"]
        F -->|"No"| B

        style C fill:#f44336,color:#fff
        style G fill:#4CAF50,color:#fff
    ```

    ---

    ## P3: Ejecución de Órdenes de Compra

    | Campo       | Valor                   |
    | ----------- | ----------------------- |
    | **ID**      | `BPMN-GN-COMPRAS-OC-01` |
    | **Sistema** | Mercado Público         |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        A["Adjudicación/<br/>Contrato vigente"] --> B["Abastecimiento:<br/>Generar OC"]
        B --> C["Asociar CDP y<br/>partida presupuestaria"]
        C --> D["Firma jefatura<br/>respectiva"]
        D --> E["Enviar OC a<br/>proveedor"]
        E --> F["Proveedor<br/>acepta OC"]
        F --> G["Recepción de<br/>bienes/servicios"]
        G --> H{"¿Conforme?"}
        H -->|"Sí"| I["Acta de<br/>recepción"]
        H -->|"No"| J["Rechazo/<br/>Devolución"]
        I --> K["Facturación"]
        K --> L["Pago"]

        style L fill:#4CAF50,color:#fff
    ```

    ### Estados de la OC

    | Estado       | Descripción                 |
    | ------------ | --------------------------- |
    | Generada     | OC creada en el sistema     |
    | Enviada      | Notificada al proveedor     |
    | Aceptada     | Proveedor confirma          |
    | Recepcionada | Bienes/servicios entregados |
    | Pagada       | Proceso completado          |

    ---

    ## P4: Gestión de Contratos

    | Campo           | Valor                          |
    | --------------- | ------------------------------ |
    | **ID**          | `BPMN-GN-COMPRAS-CONTRATOS-01` |
    | **Responsable** | Administrador de Contrato      |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        subgraph FORMALIZACION["📋 Formalización"]
            A["Elaborar contrato"]
            B["Revisión jurídica"]
            C["Firma de partes"]
            D["Resolución aprobatoria"]
            E["Garantías:<br/>• Fiel cumplimiento<br/>• Anticipo"]
        end

        subgraph EJECUCION["⚙️ Ejecución"]
            F["Designar administrador<br/>de contrato"]
            G["Seguimiento<br/>de hitos"]
            H["Verificar<br/>cumplimiento"]
            I["Estados de pago<br/>parciales"]
        end

        subgraph CIERRE["✅ Cierre"]
            J["Recepción<br/>definitiva"]
            K["Acta de cierre"]
            L["Devolución<br/>garantías"]
            M["Evaluación<br/>proveedor"]
        end

        A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M

        style M fill:#4CAF50,color:#fff
    ```

    ### Funciones del Administrador de Contrato

    | Función       | Descripción                    |
    | ------------- | ------------------------------ |
    | Supervisión   | Verificar cumplimiento técnico |
    | Comunicación  | Enlace con proveedor           |
    | Documentación | Mantener expediente            |
    | Hitos         | Certificar avances             |
    | Pagos         | Autorizar estados de pago      |

    ---

    ## Control y Transparencia

    ### Obligaciones de Publicación

    | Información       | Plataforma           |
    | ----------------- | -------------------- |
    | PAC               | Mercado Público      |
    | Licitaciones      | Mercado Público      |
    | Adjudicaciones    | Mercado Público      |
    | Contratos         | Transparencia Activa |
    | Órdenes de Compra | Mercado Público      |

    ### Prohibiciones

    > ⚠️ **Fraccionamiento prohibido**: No dividir compras para eludir umbrales.

    > ⚠️ **Conflicto de intereses**: Funcionarios deben declarar inhabilidades.

    ---

    ## Sistemas Involucrados

    | Sistema           | Función                           |
    | ----------------- | --------------------------------- |
    | `ORG-CHILECOMPRA` | Mercado Público, OC, licitaciones |
    | `SYS-SIGFE`       | CDP, compromisos, pagos           |
    | `SYS-DOCDIGITAL`  | Contratos, resoluciones           |

    ---

    ## Normativa Aplicable

    | Norma                      | Alcance            |
    | -------------------------- | ------------------ |
    | **Ley 19.886**             | Compras públicas   |
    | **Reglamento D.S. 250**    | Procedimientos     |
    | **Directivas ChileCompra** | Operativas         |
    | **Ley 20.730**             | Lobby y conflictos |

    ---

    ## Referencias Cruzadas

    | Dominio Relacionado                                                                                                                              | Vínculo                      |
    | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
    | [D02 Ciclo Presupuestario](urn:gn:kb:gn-bpmn-d02-ciclo-presupuestario)   | CDP, compromisos             |
    | [D05 Inventarios](urn:gn:kb:gn-bpmn-d05-inventarios-activo-fijo)         | Recepción de bienes          |
    | [D01 Actos Administrativos](urn:gn:kb:gn-bpmn-d01-actos-administrativos) | Resoluciones de adjudicación |

    ---

    *Última actualización: 2025-12-16*
