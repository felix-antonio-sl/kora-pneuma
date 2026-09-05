---
urn: urn:gn:kb:gn-bpmn-d06-flota-vehicular
nombre: gn-bpmn-d06-flota-vehicular
version: "1.0.1"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre Artefacto KODA/Spec – BPMN D06: Gestión de Flota Vehicular; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/arquitectura/bpmn/D06_flota_vehicular_koda.yml (sha256:064e7007a7d539e354ec9cb679c3d9c1054ebc12fafe97d7e399d12edc9031ef); URN KODA legado urn:gorenuble:gn:bpmn-d06-flota-vehicular:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02. Corrección editorial 1.0.1 (2026-08-09): sustituye enlaces `file://` no portables por URN KORA cuando el dominio existe y conserva como texto la fuente externa sin URN."
autor: "FS"
creado: 2025-12-22
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "arquitectura", "bpmn", "d06"]
familia: bok
---
# Artefacto KODA/Spec – BPMN D06: Gestión de Flota Vehicular
# Fuente: sources/gn/arquitectura/bpmn/D06_flota_vehicular.md
---
_manifest:
  urn: "urn:gorenuble:gn:bpmn-d06-flota-vehicular:1.0.0"
  federation:
    visibility: internal
    license: "Institutional Use"
  compatibility:
    min_consumer_version: "1.0.0"
    breaking_changes_from: null
  resolution:
    canonical_url: "file://knowledge/domains/gn/arquitectura/bpmn/D06_flota_vehicular_koda.yml"
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

ID: BPMN-GN-D06-FLOTA-KODA
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
Ctx: "Especificación STS del dominio D06: Gestión de Flota Vehicular del GORE Ñuble, modelado en BPMN."
Source:
  Ctx_Required:
    - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml"
  Primary-Source: "sources/gn/arquitectura/bpmn/D06_flota_vehicular.md"

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
  ID: DOM-FLOTA
  Criticidad: "🟡 Media"
  Dueno: "Jefe Servicios Generales"
  Procesos: 1
  Subprocesos: "6 subprocesos"
  Ref_Fuente:
    Ctx_Required:
      - "knowledge/domains/gn/arquitectura/kb_gn_054_bpmn_c4_koda.yml L.1210-1400"

Body_MD:
  ID: BPMN-GN-D06-FLOTA-BODY-01
  Src: "sources/gn/arquitectura/bpmn/D06_flota_vehicular.md"
  Content: |
    # D06: Gestión de Flota Vehicular

    ## Metadatos del Dominio

    | Campo           | Valor                                                                                                                                                  |
    | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | **ID**          | `DOM-FLOTA`                                                                                                                                            |
    | **Criticidad**  | 🟡 Media                                                                                                                                                |
    | **Dueño**       | Jefe Servicios Generales                                                                                                                               |
    | **Procesos**    | 1 (con 6 subprocesos)                                                                                                                                  |
    | **Ref. Fuente** | `kb_gn_054_bpmn_c4_koda.yml` (fuente externa archivada; sin URN KORA) L.1210-1400 |

    ---

    ## Mapa General del Dominio

    ```mermaid
    flowchart LR
        subgraph CICLO_FLOTA["🚗 Gestión de Flota"]
            S1["Registro<br/>vehículos"]
            S2["Asignación<br/>y uso"]
            S3["Bitácora<br/>de viaje"]
            S4["Combustible<br/>y kilometraje"]
            S5["Mantención<br/>vehicular"]
            S6["Siniestros y<br/>accidentes"]
        end

        S1 --> S2 --> S3 --> S4
        S4 --> S5
        S2 --> S6

        style S1 fill:#2196F3,color:#fff
        style S5 fill:#FF9800,color:#fff
        style S6 fill:#f44336,color:#fff
    ```

    ---

    ## P1: Gestión de Flota Vehicular

    | Campo         | Valor                        |
    | ------------- | ---------------------------- |
    | **ID**        | `BPMN-GN-FLOTA-VEHICULAR-01` |
    | **Normativa** | D.L. 799 (restricción uso)   |

    ### S1: Registro de Vehículos y Conductores

    ```mermaid
    flowchart TD
        subgraph VEHICULOS["🚗 Registro de Vehículos"]
            A["Adquisición de<br/>vehículo"]
            B["Registrar en<br/>sistema interno"]
            C["Datos:<br/>• Patente<br/>• Modelo<br/>• Año<br/>• Tipo combustible"]
            D["Asignar a<br/>división/área"]
            E["Inscribir en<br/>Registro Automotor"]
        end

        subgraph CONDUCTORES["👤 Registro de Conductores"]
            F["Funcionario solicita<br/>autorización"]
            G["Verificar:<br/>• Licencia vigente<br/>• Clase apropiada<br/>• Hoja de vida"]
            H["Autorización de<br/>Jefe Servicios"]
            I["Registrar en<br/>nómina conductores"]
        end

        A --> B --> C --> D --> E
        F --> G --> H --> I

        style E fill:#2196F3,color:#fff
        style I fill:#4CAF50,color:#fff
    ```

    ### S2: Solicitud y Asignación

    ```mermaid
    flowchart TD
        A["Funcionario solicita<br/>vehículo"] --> B["Ingresar solicitud:<br/>• Fecha/hora<br/>• Destino<br/>• Motivo<br/>• Pasajeros"]
        B --> C["Jefatura directa<br/>autoriza"]
        C --> D["Servicios Generales<br/>verifica disponibilidad"]
        D --> E{"¿Disponible?"}
        E -->|"Sí"| F["Asignar vehículo<br/>y conductor si aplica"]
        E -->|"No"| G["Buscar alternativa<br/>o reprogramar"]
        F --> H["Entregar llaves<br/>y bitácora"]

        style H fill:#4CAF50,color:#fff
    ```

    ### S3: Bitácora de Viaje

    ```mermaid
    flowchart TD
        A["Recibir vehículo"] --> B["Registrar en bitácora:<br/>• Fecha/hora salida<br/>• Km inicial<br/>• Estado combustible"]
        B --> C["Realizar viaje"]
        C --> D["Al regresar registrar:<br/>• Fecha/hora llegada<br/>• Km final<br/>• Observaciones"]
        D --> E["Firmar bitácora"]
        E --> F["Devolver llaves<br/>a Servicios Generales"]

        style E fill:#FF9800,color:#fff
    ```

    ### S4: Gestión de Combustible

    ```mermaid
    flowchart TD
        A["Vehículo requiere<br/>combustible"] --> B["Conductor solicita<br/>cupón/tarjeta"]
        B --> C["Servicios Generales<br/>autoriza"]
        C --> D["Cargar combustible<br/>en estación"]
        D --> E["Registrar:<br/>• Litros<br/>• Monto<br/>• Km actual"]
        E --> F["Devolver cupón<br/>con factura"]
        F --> G["Consolidar consumos<br/>mensuales"]
        G --> H["Analizar rendimiento<br/>km/litro"]

        style H fill:#9C27B0,color:#fff
    ```

    ### S5: Mantención Vehicular

    ```mermaid
    flowchart TD
        subgraph PREVENTIVA["🔧 Mantención Preventiva"]
            A["Programar según<br/>km/tiempo"]
            B["Alertar próxima<br/>mantención"]
            C["Agendar con<br/>taller"]
            D["Ejecutar mantención"]
            E["Registrar en<br/>historial"]
        end

        subgraph CORRECTIVA["⚠️ Mantención Correctiva"]
            F["Detectar falla"]
            G["Reportar a<br/>Servicios Generales"]
            H["Evaluar:<br/>• Taller interno<br/>• Taller externo"]
            I["Reparar"]
            J["Certificar OK<br/>para uso"]
        end

        A --> B --> C --> D --> E
        F --> G --> H --> I --> J

        style E fill:#4CAF50,color:#fff
        style J fill:#FF9800,color:#fff
    ```

    ### Programa de Mantención

    | Tipo           | Frecuencia | Acciones                  |
    | -------------- | ---------- | ------------------------- |
    | **Básica**     | 5.000 km   | Cambio aceite, filtros    |
    | **Intermedia** | 15.000 km  | Frenos, neumáticos        |
    | **Mayor**      | 30.000 km  | Revisión completa         |
    | **Documentos** | Anual      | Revisión técnica, permiso |

    ### S6: Siniestros y Accidentes

    ```mermaid
    flowchart TD
        A["Ocurre accidente"] --> B["Conductor toma<br/>medidas inmediatas"]
        B --> C["Llamar a<br/>Carabineros"]
        C --> D["Constancia<br/>policial"]
        D --> E["Reportar a<br/>Servicios Generales"]
        E --> F["Levantar acta<br/>de siniestro"]
        F --> G{"¿Daños a<br/>terceros?"}
        G -->|"Sí"| H["Activar seguro<br/>y procedimiento"]
        G -->|"No"| I["Evaluar daños<br/>propios"]
        H --> J["Seguimiento<br/>aseguradora"]
        I --> K["Cotizar<br/>reparación"]
        J & K --> L["Resolución<br/>administrativa"]
        L --> M["Determinar<br/>responsabilidades"]

        style D fill:#f44336,color:#fff
        style M fill:#9C27B0,color:#fff
    ```

    ### Información del Acta de Siniestro

    | Dato         | Descripción          |
    | ------------ | -------------------- |
    | Fecha y hora | Del accidente        |
    | Lugar        | Dirección exacta     |
    | Conductor    | Funcionario a cargo  |
    | Descripción  | Circunstancias       |
    | Testigos     | Identificación       |
    | Daños        | Propios y a terceros |
    | N° Parte     | Carabineros          |

    ---

    ## Restricciones Normativas

    ### D.L. 799 (Uso de Vehículos Fiscales)

    | Restricción            | Detalle                                 |
    | ---------------------- | --------------------------------------- |
    | **Fines de semana**    | Prohibido uso sin autorización especial |
    | **Uso particular**     | Prohibido                               |
    | **Fuera de la región** | Requiere autorización                   |
    | **Horario**            | Jornada laboral (salvo excepciones)     |

    > ⚠️ **Incumplimiento genera responsabilidad administrativa y patrimonial.**

    ---

    ## Métricas de Control

    | Indicador                | Fórmula                        | Meta       |
    | ------------------------ | ------------------------------ | ---------- |
    | Rendimiento combustible  | Km / Litros                    | > 10 km/lt |
    | % Mantención cumplida    | Mantenciones OK / Programadas  | > 95%      |
    | Tasa de accidentabilidad | Accidentes / Vehículos         | < 5%       |
    | Disponibilidad flota     | Días operativos / Días totales | > 90%      |

    ---

    ## Sistemas Involucrados

    | Sistema                  | Función                 |
    | ------------------------ | ----------------------- |
    | `SYS-SIGAS`              | Inventario de vehículos |
    | Sistema interno de flota | Bitácoras, mantenciones |

    ---

    ## Referencias Cruzadas

    | Dominio Relacionado                                                                                                                           | Vínculo                            |
    | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
    | [D05 Inventarios y AF](urn:gn:kb:gn-bpmn-d05-inventarios-activo-fijo) | Vehículos como activo fijo         |
    | [D04 Compras](urn:gn:kb:gn-bpmn-d04-compras-contrataciones)           | Adquisición vehículos, combustible |

    ---

    *Última actualización: 2025-12-16*
