---
urn: urn:gn:kb:gn-bpmn-d09-cies-sitia
nombre: gn-bpmn-d09-cies-sitia
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – BPMN D09: Gestión Operativa CIES/SITIA (Seguridad Pública); migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/bpmn/D09_cies_sitia_koda.yml (sha256:241ec2453eb13b93bd85c83aa69bb696852a42af43d8073533ffd7e95ff6e685); URN KODA legado urn:gorenuble:gn:bpmn-d09-cies-sitia:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02. Corrección editorial 1.0.1 (2026-08-09): sustituye enlaces `file://` no portables por URN KORA cuando el dominio existe y conserva como texto la fuente externa sin URN."
autor: "FS"
creado: 2025-12-22
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "bpmn", "d09"]
familia: bok
---
# Artefacto KODA/Spec – BPMN D09: Gestión Operativa CIES/SITIA (Seguridad Pública)
# Fuente: sources/gn/arquitectura/bpmn/D09_cies_sitia.md
---
_manifest:
  urn: "urn:gorenuble:gn:bpmn-d09-cies-sitia:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/arquitectura/bpmn/D09_cies_sitia_koda.yml"
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

ID: BPMN-GN-D09-CIES-SITIA-KODA
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
Ctx: "Especificación STS del dominio D09: Gestión Operativa CIES/SITIA (Seguridad Pública) del GORE Ñuble, modelado en BPMN."
Source:
  Ctx_Required:
    - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml"
  Primary-Source: "sources/gn/arquitectura/bpmn/D09_cies_sitia.md"

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
  ID: DOM-CIES
  Criticidad: "🟠 Alta"
  Dueno: "Supervisor CIES"
  Procesos: 3
  Subprocesos: "~8"
  Ref_Fuente:
    Ctx_Required:
      - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.4142-4306"

Body_MD:
  ID: BPMN-GN-D09-CIES-SITIA-BODY-01
  Src: "sources/gn/arquitectura/bpmn/D09_cies_sitia.md"
  Content: |
    # D09: Gestión Operativa CIES/SITIA (Seguridad Pública)

    ## Metadatos del Dominio

    | Campo           | Valor                                                                                                                                                  |
    | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **ID**          | `DOM-CIES`                                                                                                                                             |
    | **Criticidad**  | 🟠 Alta                                                                                                                                                 |
    | **Dueño**       | Supervisor CIES                                                                                                                                        |
    | **Procesos**    | 3                                                                                                                                                      |
    | **Subprocesos** | ~8                                                                                                                                                     |
    | **Ref. Fuente** | `kb_gn_054_bpmn_c4_koda.yml` (fuente externa archivada; sin URN KORA) L.4142-4306 |

    ---

    ## Mapa General del Dominio

    ```mermaid
    flowchart LR
        subgraph CIES["🎥 Centro CIES-ÑUBLE"]
            P1["P1: Monitoreo y<br/>Detección"]
            P2["P2: Coordinación<br/>Interinstitucional"]
            P3["P3: Gestión de<br/>Evidencias"]
        end

        subgraph SITIA["🤖 Integración SITIA"]
            S1["SITIA-Patentes"]
            S2["SITIA-Armas"]
            S3["SITIA-Evidencia"]
            S4["SITIA-Unificación"]
        end

        P1 --> P2
        P1 --> P3
        P1 <--> S1 & S2 & S4
        P3 <--> S3

        style P1 fill:#2196F3,color:#fff
        style P2 fill:#FF9800,color:#fff
        style P3 fill:#9C27B0,color:#fff
    ```

    ---

    ## Contexto Operativo

    | Aspecto          | Detalle                                 |
    | ---------------- | --------------------------------------- |
    | **Cobertura**    | 16 horas (08:00-00:00), proyección 24/7 |
    | **Ubicación**    | Sala de monitoreo GORE Ñuble            |
    | **Coordinación** | Policías, emergencias, 21 municipios    |
    | **Marco legal**  | Ley 21.427, Ley 20.965, Ley 20.502      |

    ---

    ## P1: Monitoreo, Detección y Escalamiento

    | Campo       | Valor                             |
    | ----------- | --------------------------------- |
    | **ID**      | `BPMN-GN-CIES-SITIA-MONITOREO-01` |
    | **Sistema** | HikCentral VMS                    |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        subgraph MONITOREO["🎥 Monitoreo Continuo"]
            A["Operador CIES<br/>monitorea cámaras"]
            B["Sistemas SITIA<br/>detectan automáticamente:<br/>• Patentes alertadas<br/>• Armas visibles"]
        end

        subgraph DETECCION["⚡ Detección"]
            C["Identificar evento/<br/>incidente"]
            D{"Clasificar<br/>prioridad"}
            D -->|"🔴 Alta"| E["Alarma inmediata"]
            D -->|"🟠 Media"| F["Registro y seguimiento"]
            D -->|"🟢 Baja"| G["Solo registro"]
        end

        subgraph ESCALAMIENTO["📢 Escalamiento"]
            E --> H["Supervisor CIES<br/>evalúa"]
            H --> I["Activar protocolo<br/>según tipo"]
            I --> J["Coordinar con:<br/>• Carabineros<br/>• PDI<br/>• Bomberos<br/>• SAMU"]
        end

        A --> C
        B --> C
        C --> D
        F --> H

        style E fill:#f44336,color:#fff
        style J fill:#4CAF50,color:#fff
    ```

    ### Clasificación de Incidentes

    | Prioridad   | Tipo                              | Acción                   |
    | ----------- | --------------------------------- | ------------------------ |
    | 🔴 **Alta**  | Delito en curso, emergencia vital | Activación inmediata     |
    | 🟠 **Media** | Sospecha, situación anómala       | Seguimiento y evaluación |
    | 🟢 **Baja**  | Evento menor, registro            | Solo documentar          |

    ---

    ## P2: Coordinación Interinstitucional

    | Campo         | Valor                                        |
    | ------------- | -------------------------------------------- |
    | **ID**        | `BPMN-GN-CIES-SITIA-COORD-01`                |
    | **Entidades** | Carabineros, PDI, Bomberos, SAMU, Municipios |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        A["Incidente<br/>clasificado"] --> B["Enlace CIES<br/>activa canal"]
        B --> C{"Tipo de<br/>emergencia"}

        C -->|"Seguridad"| D["📞 Carabineros<br/>133"]
        C -->|"Investigación"| E["📞 PDI<br/>134"]
        C -->|"Incendio"| F["📞 Bomberos<br/>132"]
        C -->|"Salud"| G["📞 SAMU<br/>131"]

        D & E & F & G --> H["Confirmar recepción<br/>y unidades"]
        H --> I["Seguimiento<br/>en tiempo real"]
        I --> J["Registro de<br/>respuesta"]
        J --> K["Cierre de<br/>incidente"]

        style K fill:#4CAF50,color:#fff
    ```

    ### Protocolos de Comunicación

    | Canal                  | Uso                           |
    | ---------------------- | ----------------------------- |
    | Radio VHF              | Comunicación directa policías |
    | Líneas directas        | Centrales de emergencia       |
    | WhatsApp institucional | Coordinación municipal        |
    | Plataforma SITIA       | Integración nacional          |

    ---

    ## P3: Gestión de Evidencias Digitales

    | Campo          | Valor                               |
    | -------------- | ----------------------------------- |
    | **ID**         | `BPMN-GN-CIES-SITIA-EVIDENCIA-01`   |
    | **Plataforma** | SITIA-Evidencia (Genetec Clearance) |

    ### Diagrama de Flujo

    ```mermaid
    flowchart TD
        subgraph SOLICITUD["📋 Solicitud"]
            A["Fiscalía/Tribunal<br/>solicita evidencia"]
            B["Recepción oficio<br/>en GORE"]
            C["Verificar:<br/>• Orden judicial<br/>• Requerimiento MP"]
        end

        subgraph EXTRACCION["🎬 Extracción"]
            D["Supervisor CIES<br/>autoriza"]
            E["Localizar grabación<br/>en HikCentral"]
            F["Exportar clip<br/>seguro"]
            G["Subir a<br/>SITIA-Evidencia"]
        end

        subgraph ENTREGA["📤 Entrega"]
            H["Generar cadena<br/>de custodia"]
            I["Entrega por medio<br/>controlado"]
            J["Acta de entrega"]
            K["Registro para<br/>trazabilidad"]
        end

        A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K

        style J fill:#4CAF50,color:#fff
    ```

    ### Cadena de Custodia Digital

    | Elemento        | Verificación      |
    | --------------- | ----------------- |
    | Hash de archivo | Integridad        |
    | Metadatos       | Fecha/hora/cámara |
    | Log de accesos  | Quién manipuló    |
    | Firma digital   | Autenticidad      |

    ---

    ## Capacidades SITIA

    ### SITIA-Patentes

    ```mermaid
    flowchart LR
        A["Red de pórticos<br/>públicos/privados"] --> B["Lectura automática<br/>de placas"]
        B --> C["Contraste en<br/>tiempo real"]
        C --> D{"¿Encargo de<br/>búsqueda?"}
        D -->|"Sí"| E["🚨 Alerta a CIES<br/>y policías"]
        D -->|"No"| F["Registro histórico"]

        style E fill:#f44336,color:#fff
    ```

    ### SITIA-Armas

    ```mermaid
    flowchart LR
        A["Cámaras CIES"] --> B["Modelo IA<br/>(YOLOv11)"]
        B --> C{"¿Arma<br/>detectada?"}
        C -->|"Sí"| D["🚨 Alerta automática"]
        C -->|"No"| E["Continuar monitoreo"]
        D --> F["Operador verifica"]
        F --> G["Escalar si confirma"]

        style D fill:#f44336,color:#fff
    ```

    ---

    ## Gestión de Privacidad y Retención

    ### Política de Retención

    | Aspecto               | Regla                           |
    | --------------------- | ------------------------------- |
    | **Retención normal**  | 30 días                         |
    | **Eliminación**       | Segura e irreversible           |
    | **Cautela ciudadana** | Hasta 6 meses (víctima/testigo) |

    ### Cumplimiento Normativo

    ```mermaid
    flowchart TD
        A["Grabación<br/>generada"] --> B["Almacenar<br/>30 días"]
        B --> C{"¿Solicitud de<br/>cautela?"}
        C -->|"Sí"| D["Extender retención<br/>hasta 6 meses"]
        C -->|"No"| E["Eliminar<br/>automáticamente"]
        D --> F["Revisar al<br/>vencimiento"]
        F --> E

        style E fill:#607D8B,color:#fff
    ```

    > ⚠️ **Ley 19.628**: Tratamiento de datos personales debe respetar licitud, finalidad y proporcionalidad.

    ---

    ## Sostenibilidad Operativa

    ### Modelo de Financiamiento

    | Componente         | Fuente                          |
    | ------------------ | ------------------------------- |
    | Personal CIES      | Presupuesto anual GORE          |
    | Mantención equipos | Garantía 22 meses + presupuesto |
    | Servicios SITIA    | Convenio marco con SPD          |

    ### Mantención

    ```mermaid
    flowchart LR
        A["Mantención<br/>preventiva"] -->|"Trimestral"| B["Revisión equipos"]
        B --> C["Actualizaciones<br/>software"]
        C --> D["Reporte estado"]

        style D fill:#4CAF50,color:#fff
    ```

    ---

    ## Sistemas Involucrados

    | Sistema               | Función             |
    | --------------------- | ------------------- |
    | `SYS-HIKCENTRAL`      | VMS gestión cámaras |
    | `SYS-SITIA`           | Plataforma nacional |
    | `SYS-SITIA-EVIDENCIA` | Gestión evidencias  |
    | `SYS-SITIA-PATENTES`  | Lectura placas      |
    | `SYS-SITIA-ARMAS`     | Detección IA        |

    ---

    ## Normativa Aplicable

    | Norma          | Alcance                    |
    | -------------- | -------------------------- |
    | **Ley 21.427** | Sistema Nacional Seguridad |
    | **Ley 20.965** | Cámaras vigilancia         |
    | **Ley 20.502** | ONEMI/funcionamiento       |
    | **Ley 19.628** | Protección vida privada    |
    | **Ley 21.719** | Datos personales           |

    ---

    ## Referencias Cruzadas

    | Dominio Relacionado                                                                                                                              | Vínculo                 |
    | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
    | [D01 Actos Administrativos](urn:gn:kb:gn-bpmn-d01-actos-administrativos) | Convenios con entidades |

    ---

    *Última actualización: 2025-12-16*
