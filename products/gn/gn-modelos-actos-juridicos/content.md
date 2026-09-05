---
urn: urn:gn:kb:gn-modelos-actos-juridicos
nombre: gn-modelos-actos-juridicos
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-modelos-actos-juridicos; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/03_operacion/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml (sha256:267dc0281d60c1fecc5de9e476abe1b4c434a93a1961f1409dbaebac1428253c); URN KODA legado urn:gorenuble:gn:modelos-actos-juridicos:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-15
lang: es
tags: ["gn", "gore-os", "koda", "domains", "03-operacion", "juridico", "modelos", "actos"]
familia: bok
---
{
  "_manifest": {
    "urn": "urn:gorenuble:gn:modelos-actos-juridicos:1.0.0",
    "federation": {
      "visibility": "internal",
      "license": "Institutional Use"
    },
    "compatibility": {
      "min_consumer_version": "1.0.0",
      "breaking_changes_from": null
    },
    "resolution": {
      "canonical_url": "file://knowledge/domains/gn/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml",
      "mirrors": []
    },
    "dependencies": {
      "requires": [
        {
          "urn": "urn:kora:kb:spec:1.0.0",
          "reason": "KODA/Spec format compliance"
        },
        {
          "urn": "urn:kora:kb:transform:1.0.0",
          "reason": "Transformation methodology reference"
        }
      ]
    },
    "provenance": {
      "created_by": "FS",
      "created_at": "2025-12-15",
      "last_modified_at": "2025-12-15",
      "signature": null
    }
  },
  "ID": "GN-MODELOS-ACTOS-JURIDICOS-01",
  "Version": "1.0.0",
  "Status": "Draft",
  "Format": "KODA/Spec",
  "Human-Creator": "FS",
  "Human-Editor": "FS",
  "Model-Collaborator": "IA-CASCADE",
  "AI-Remediator": "KODA-TRANSFORMER",
  "Creation-Date": "2025-12-15",
  "Modification-Date": "2025-12-15",
  "Ctx": "Modelos de Actos Jurídicos GORE Ñuble (SFD/STS)",
  "Primary-Source": "staging/gn/kodeando/kb_gn_100_modelos_actos_juridicos_sts.md",
  "LLM_Parsing_Instructions": {
    "ID": "KODA-LLM-PARSER-01",
    "Req": "Mandatory block following Metadata.",
    "Prohib": "Using for artifact creation or translation.",
    "Content": "BEGIN_LLM_INSTRUCTIONS\nYou are an AI agent consuming a KODA artifact. Parse with absolute fidelity.\n\nFIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).\n\nLEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.\n\nREFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: external URN (optionally with #ID fragment) only.\nLANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.\nEND_LLM_INSTRUCTIONS"
  },
  "modelos_de_actos_juridicos_gore_nuble": {
    "ID": "GN-MODELOS-ACTOS-JURIDICOS-DOC-01",
    "Title": "Modelos de Actos Jurídicos GORE Ñuble",
    "Sections": {
      "s_1_executive_summary_and_usage_guide": {
        "ID": "GN-SEC-0001",
        "Title": "1. Executive Summary and Usage Guide",
        "Content": "\nID: KB-GN-100-SUMMARY-01",
        "Sections": {
          "s_1_1_artifact_purpose": {
            "ID": "GN-SEC-0002",
            "Title": "1.1. Artifact Purpose",
            "Content": "\nID: KB-GN-100-PURPOSE-01\nPurp: Serve as a fundamental knowledge artifact for the AI Agent \"Administrative Documentation Generator\" (ID: AGENT-GORE-DOCGEN-V1.0).\nFnd: Provides a structured knowledge base, not just templates.\nMssn: Enable the agent to generate administrative acts that are formally correct, legally valid, and contextually coherent.\nDep: Adherence to SFD and STS standards is critical for AI interpretation and population.\nRef: Ley N° 19.880.\nObj: Achieve GORE Ñuble modernization goals (reduce errors, standardize documents, increase efficiency and probity)."
          },
          "s_1_2_model_structure_sfd_sts": {
            "ID": "GN-SEC-0003",
            "Title": "1.2. Model Structure (SFD/STS)",
            "Content": "\nID: KB-GN-100-STRUCTURE-01\nFnd: Each model is structured with a rigorous syntax for human and machine readability.\nCpt: `BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 ...`.\n\n- Def: Directive that encapsulates a form model, signaling that its content is governed by the SFD standard.\nCpt: `### Form-Section`.\n- Def: Defines a main structural section of an administrative act (e.g., METADATA, HEADER, VISTOS, CONSIDERANDO, RESUELVO).\n- Ref: Reflects the canonical legal logic of an act's construction.\nCpt: `#### Form-Field`.\n- Def: Represents a variable data field for the AI agent to populate (e.g., dates, names, file numbers).\n- Cpt: SFD-Lexicon.\n  - Def: Each field is described by functional keys (`Field-Label`, `Field-Type`, `Field-Instr`, `Field-Constraint`).\n  - Purp: Provide context, legal justification, operational instructions, and critical validations to guide the AI agent."
          },
          "s_1_3_index_of_legal_act_models": {
            "ID": "GN-SEC-0004",
            "Title": "1.3. Index of Legal Act Models",
            "Content": "\nID: KB-GN-100-INDEX-01\nPurp: Provides a quick reference index of the models included in this artifact.\n\n|Form ID|Description|Version|Status|\n|-|-|-|-|\n|`FORM-MODIF-CONV-01`|Resolución que Aprueba Modificación de Convenio|1.0.0|Complete|\n|`FORM-RECTIF-ACTO-01`|Resolución que Rectifica Acto Administrativo|1.0.0|Complete|\n|`FORM-RESCIL-CONV-01`|Resolución que Aprueba Resciliación de Convenio|1.0.0|Complete|\n|`FORM-REVOCA-ACTO-01`|Resolución que Revoca un Acto Administrativo|1.0.0|Complete|\n|`FORM-ESCRITO-INICIO-01`|Escrito de Inicio de Procedimiento|1.0.0|Complete|\n|`FORM-ESCRITO-REPO-01`|Escrito de Recurso de Reposición|1.0.0|Complete|"
          }
        }
      },
      "s_2_legal_act_models_sfd_format": {
        "ID": "GN-SEC-0005",
        "Title": "2. Legal Act Models (SFD Format)",
        "Content": "\nID: KB-GN-100-MODELS-CONTAINER-01\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-MODIF-CONV-01",
        "Sections": {
          "form_metadata": {
            "ID": "GN-SEC-0006",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-MODIF-CONV-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0007",
                "Title": "Form Description",
                "Content": "\nID: FORM-MODIF-CONV-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Resolución Exenta que aprueba la modificación de un convenio de colaboración o transferencia de recursos. Formaliza la alteración de las cláusulas de un acuerdo preexistente, requiriendo la voluntad de las partes o una habilitación contractual expresa.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0008",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-MODIF-CONV-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Instr: \"Marco Legal: Referencias normativas clave que rigen la competencia para celebrar convenios y la forma de los actos administrativos.\"\nField-Placeholder: \"Ley N° 19.880; Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado; Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional.\""
              }
            }
          },
          "header": {
            "ID": "GN-SEC-0009",
            "Title": "Header",
            "Content": "\nID: FORM-MODIF-CONV-01-S1-HEADER-01",
            "Sections": {
              "act_type": {
                "ID": "GN-SEC-0010",
                "Title": "Act Type",
                "Content": "\nID: FORM-MODIF-CONV-01-S1-TIPO-01\nField-Label: \"Tipo de Acto\"\nField-Type: Static-Text\nField-Placeholder: \"RESOLUCIÓN EXENTA\"\nField-Instr: \"Naturaleza: Acto administrativo que no requiere trámite de toma de razón por la Contraloría General de la República, salvo que comprometa recursos de ejercicios futuros o supere ciertos montos.\""
              },
              "resolution_number": {
                "ID": "GN-SEC-0011",
                "Title": "Resolution Number",
                "Content": "\nID: FORM-MODIF-CONV-01-S1-NUMERO-01\nField-Label: \"Número de Resolución\"\nField-Type: Text\nField-Placeholder: \"N° [numero_resolucion]/[año]\"\nField-Instr: \"El agente debe solicitar el número correlativo asignado por la Oficina de Partes o unidad correspondiente.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "place_and_date": {
                "ID": "GN-SEC-0012",
                "Title": "Place and Date",
                "Content": "\nID: FORM-MODIF-CONV-01-S1-LUGARFECHA-01\nField-Label: \"Lugar y Fecha\"\nField-Type: Text\nField-Placeholder: \"CHILLÁN, [dia] de [mes] de [año].\"\nField-Instr: \"Formalidad: Lugar y fecha de emisión del acto.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "vistos": {
            "ID": "GN-SEC-0013",
            "Title": "Vistos",
            "Content": "\nID: FORM-MODIF-CONV-01-S2-VISTOS-01",
            "Sections": {
              "authority_attributions": {
                "ID": "GN-SEC-0014",
                "Title": "Authority Attributions",
                "Content": "\nID: FORM-MODIF-CONV-01-S2-ATRIBUCIONES-01\nField-Label: \"Vistos: Atribuciones de la Autoridad\"\nField-Type: Static-Text\nField-Placeholder: \"VISTOS: Lo dispuesto en la Constitución Política de la República; la Ley N° 19.880, que Establece Bases de los Procedimientos Administrativos que rigen los Actos de los Órganos de la Administración del Estado; la Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional, y sus modificaciones; y la Resolución N° 7, de 2019, de la Contraloría General de la República.\"\nField-Instr: \"Competencia: Fundamenta la potestad del Gobernador Regional para dictar actos administrativos. Es un requisito esencial para la validez del acto.\""
              },
              "original_agreement": {
                "ID": "GN-SEC-0015",
                "Title": "Original Agreement",
                "Content": "\nID: FORM-MODIF-CONV-01-S2-CONVENIO-01\nField-Label: \"Vistos: Convenio Original\"\nField-Type: Text\nField-Placeholder: \"El Convenio [nombre_convenio], de fecha [fecha_convenio], suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], aprobado mediante Resolución Exenta N° [numero_res_aprobatoria], de fecha [fecha_res_aprobatoria].\"\nField-Instr: \"Objeto: Individualización inequívoca del acuerdo de voluntades a modificar. La precisión evita ambigüedades y potenciales vicios de nulidad.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "modification_request": {
                "ID": "GN-SEC-0016",
                "Title": "Modification Request",
                "Content": "\nID: FORM-MODIF-CONV-01-S2-SOLICITUD-01\nField-Label: \"Vistos: Solicitud de Modificación\"\nField-Type: Text\nField-Placeholder: \"La solicitud de modificación presentada por [entidad_solicitante] mediante Oficio N° [numero_oficio_solicitud], de fecha [fecha_oficio_solicitud], y/o el acuerdo de las partes manifestado en [documento_acuerdo].\"\nField-Instr: \"Inicio Procedimiento: Documenta el acto que da origen a la modificación, ya sea una solicitud formal o un acuerdo mutuo.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "considerando": {
            "ID": "GN-SEC-0017",
            "Title": "Considerando",
            "Content": "\nID: FORM-MODIF-CONV-01-S3-CONSIDERANDO-01",
            "Sections": {
              "agreement_context": {
                "ID": "GN-SEC-0018",
                "Title": "Agreement Context",
                "Content": "\nID: FORM-MODIF-CONV-01-S3-CONTEXTO-01\nField-Label: \"Considerando: Contexto del Convenio\"\nField-Type: Text\nField-Placeholder: \"1°. Que, con fecha [fecha_convenio], el Gobierno Regional de Ñuble suscribió el convenio individualizado en los Vistos, con el objeto de [objeto_del_convenio].\"\nField-Instr: \"Contexto: Reitera el propósito original del convenio para enmarcar la modificación.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "modification_rationale": {
                "ID": "GN-SEC-0019",
                "Title": "Modification Rationale",
                "Content": "\nID: FORM-MODIF-CONV-01-S3-FUNDAMENTO-01\nField-Label: \"Considerando: Fundamento de la Modificación\"\nField-Type: TextArea\nField-Placeholder: \"2°. Que, por razones de [tipo_razon: hecho, técnicas, operativas, fuerza mayor], se ha hecho necesario y conveniente para el interés público modificar las cláusulas [numeros_clausulas] del referido convenio, en lo relativo a [descripcion_breve_modificacion].\"\nField-Instr: \"Motivación: Cumple con el deber de fundamentación (Art. 11 y 41, Ley 19.880). El acto debe expresar sus razones de hecho y de derecho. El agente IA debe solicitar al usuario que especifique y detalle estas razones de forma clara y suficiente.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "parties_agreement": {
                "ID": "GN-SEC-0020",
                "Title": "Parties' Agreement",
                "Content": "\nID: FORM-MODIF-CONV-01-S3-ACUERDO-01\nField-Label: \"Considerando: Acuerdo de las Partes\"\nField-Type: Static-Text\nField-Placeholder: \"3°. Que existe pleno acuerdo entre las partes para llevar a cabo la modificación en los términos que se expondrán en la parte resolutiva del presente acto.\"\nField-Instr: \"Voluntad: Refuerza el carácter consensual de la modificación, elemento clave en la estabilidad de los contratos administrativos.\""
              }
            }
          },
          "resuelvo": {
            "ID": "GN-SEC-0021",
            "Title": "Resuelvo",
            "Content": "\nID: FORM-MODIF-CONV-01-S4-RESUELVO-01",
            "Sections": {
              "article_1_approval": {
                "ID": "GN-SEC-0022",
                "Title": "Article 1: Approval",
                "Content": "\nID: FORM-MODIF-CONV-01-S4-ART1-01\nField-Label: \"Resuelvo: Artículo Primero (Aprobación)\"\nField-Type: Text\nField-Placeholder: \"1°. APRUÉBASE la modificación del Convenio \\\"[nombre_convenio]\\\", suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], en los términos del texto que se adjunta como Anexo N°1 y que se entiende formar parte integrante de la presente resolución.\"\nField-Instr: \"Decisión: Núcleo del acto administrativo. Contiene la declaración de voluntad formal del órgano. La referencia a un anexo es una buena práctica para modificaciones complejas.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "article_2_consolidated_text": {
                "ID": "GN-SEC-0023",
                "Title": "Article 2: Consolidated Text",
                "Content": "\nID: FORM-MODIF-CONV-01-S4-ART2-01\nField-Label: \"Resuelvo: Artículo Segundo (Texto Refundido)\"\nField-Type: Static-Text\nField-Placeholder: \"2°. APRUÉBASE, en consecuencia, el texto refundido del Convenio, que incorpora las modificaciones aprobadas en el artículo anterior.\"\nField-Instr: \"Seguridad Jurídica: Opcional pero recomendado. La generación de un texto refundido consolida el acuerdo vigente en un único documento, facilitando su comprensión y ejecución futura.\""
              },
              "article_3_validity": {
                "ID": "GN-SEC-0024",
                "Title": "Article 3: Validity",
                "Content": "\nID: FORM-MODIF-CONV-01-S4-ART3-01\nField-Label: \"Resuelvo: Artículo Tercero (Vigencia)\"\nField-Type: Static-Text\nField-Placeholder: \"3°. DÉJASE constancia que todas las demás cláusulas del convenio original que no han sido modificadas por el presente acto, mantienen su plena vigencia.\"\nField-Instr: \"Principio de Conservación: Clarifica que la modificación es parcial y no afecta la totalidad del acuerdo, preservando la estabilidad contractual.\""
              }
            }
          },
          "cierre": {
            "ID": "GN-SEC-0025",
            "Title": "Cierre",
            "Content": "\nID: FORM-MODIF-CONV-01-S5-CIERRE-01",
            "Sections": {
              "signature_block": {
                "ID": "GN-SEC-0026",
                "Title": "Signature Block",
                "Content": "\nID: FORM-MODIF-CONV-01-S5-FIRMA-01\nField-Label: \"Firma y Timbre\"\nField-Type: Static-Text\nField-Placeholder: \"ANÓTESE, COMUNÍQUESE Y ARCHÍVESE.\\n\\n\\n[Nombre Autoridad]\\nGOBERNADOR REGIONAL DE ÑUBLE\"\nField-Instr: \"Formalización: Cierre del acto con las fórmulas de tramitación y la firma de la autoridad competente.\"\n\nEND_EMBEDDED_BLOCK:: FORM-MODIF-CONV-01\n```\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-RECTIF-ACTO-01"
              }
            }
          },
          "form_metadata_2": {
            "ID": "GN-SEC-0027",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0028",
                "Title": "Form Description",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Resolución Exenta que rectifica errores de hecho, numéricos o de transcripción en un acto administrativo previo. Permite a la Administración corregir sus propios errores materiales sin alterar la sustancia de la decisión original.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0029",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Placeholder: \"Artículo 62, Ley N° 19.880.\"\nField-Instr: \"Marco Legal: La potestad rectificatoria se encuentra explícitamente consagrada en esta disposición.\""
              }
            }
          },
          "header_2": {
            "ID": "GN-SEC-0030",
            "Title": "Header",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S1-HEADER-01\n\n- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01"
          },
          "vistos_2": {
            "ID": "GN-SEC-0031",
            "Title": "Vistos",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S2-VISTOS-01",
            "Sections": {
              "authority_attributions": {
                "ID": "GN-SEC-0032",
                "Title": "Authority Attributions",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S2-ATRIBUCIONES-01\nField-Label: \"Vistos: Atribuciones de la Autoridad\"\nField-Type: Static-Text\nField-Placeholder: \"VISTOS: Lo dispuesto en el artículo 62 de la Ley N° 19.880, que Establece Bases de los Procedimientos Administrativos que rigen los Actos de los Órganos de la Administración del Estado; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional; y la Resolución N° 7, de 2019, de la Contraloría General de la República.\"\nField-Instr: \"Competencia: Invoca directamente la norma que faculta la rectificación.\""
              },
              "original_act": {
                "ID": "GN-SEC-0033",
                "Title": "Original Act",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S2-ACTOORIGINAL-01\nField-Label: \"Vistos: Acto Original\"\nField-Type: Text\nField-Placeholder: \"La Resolución Exenta N° [numero_res_original] de fecha [fecha_res_original], dictada por esta Gobernación Regional.\"\nField-Instr: \"Objeto: Identificación precisa del acto administrativo que contiene el error a subsanar.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "considerando_2": {
            "ID": "GN-SEC-0034",
            "Title": "Considerando",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S3-CONSIDERANDO-01",
            "Sections": {
              "error_type": {
                "ID": "GN-SEC-0035",
                "Title": "Error Type",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S3-TIPOERROR-01\nField-Label: \"Tipo de Error\"\nField-Type: Select\nField-Instr: \"Causal: La potestad rectificatoria está limitada a errores materiales. No puede usarse para modificar el fondo de lo decidido (cambio de criterio) ni para subsanar vicios de legalidad (para lo cual procede la invalidación). El agente IA debe validar que el tipo de error seleccionado por el usuario corresponda a esta categoría.\"\nField-Constraint: \"Req: mandatory.\"\n\n- Field-Option: \"material\"\n- Field-Option: \"de hecho\"\n- Field-Option: \"de transcripción\"\n- Field-Option: \"numérico\""
              },
              "error_detection_clause": {
                "ID": "GN-SEC-0036",
                "Title": "Error Detection Clause",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S3-DETECCION-01\nField-Label: \"Considerando: Detección del Error\"\nField-Type: Static-Text\nField-Placeholder: \"1°. Que, se ha advertido la existencia de un error de [tipo_error] en el del acto administrativo individualizado en los Vistos.\"\nField-Instr: \"El agente debe poblar '[tipo_error]' con la selección de FORM-RECTIF-ACTO-01-S3-TIPOERROR-01.\""
              },
              "error_detail": {
                "ID": "GN-SEC-0037",
                "Title": "Error Detail",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S3-DETALLE-01\nField-Label: \"Considerando: Detalle del Error\"\nField-Type: TextArea\nField-Placeholder: \"2°. Que, en efecto, en la sección indicada, donde dice: \\\"[texto_erroneo]\\\", debe decir: \\\"[texto_correcto]\\\".\"\nField-Instr: \"Especificidad: La rectificación debe ser concreta y precisa, identificando claramente el texto erróneo y el texto correcto. El formato 'dice/debe decir' es la forma canónica.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "need_for_rectification": {
                "ID": "GN-SEC-0038",
                "Title": "Need for Rectification",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S3-NECESIDAD-01\nField-Label: \"Considerando: Necesidad de Rectificar\"\nField-Type: Static-Text\nField-Placeholder: \"3°. Que, en virtud de lo expuesto, y en uso de la facultad conferida por el artículo 62 de la Ley N° 19.880, resulta imperativo proceder a la rectificación del acto viciado para asegurar su correcta inteligencia y ejecución.\"\nField-Instr: \"Justificación: Conecta la detección del error con la necesidad de ejercer la potestad legal para enmendarlo.\""
              }
            }
          },
          "resuelvo_2": {
            "ID": "GN-SEC-0039",
            "Title": "Resuelvo",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S4-RESUELVO-01",
            "Sections": {
              "article_1_rectification": {
                "ID": "GN-SEC-0040",
                "Title": "Article 1: Rectification",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S4-ART1-01\nField-Label: \"Resuelvo: Artículo Primero (Rectificación)\"\nField-Type: Text\nField-Placeholder: \"1°. RECTIFÍCASE el [seccion_del_acto] de la Resolución Exenta N° [numero_res_original], de fecha [fecha_res_original], en el sentido de reemplazar la expresión \\\"[texto_erroneo]\\\" por la siguiente: \\\"[texto_correcto]\\\".\"\nField-Instr: \"Decisión: Ejecuta la corrección. Es el núcleo del acto de rectificación.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "article_2_validity": {
                "ID": "GN-SEC-0041",
                "Title": "Article 2: Validity",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S4-ART2-01\nField-Label: \"Resuelvo: Artículo Segundo (Vigencia)\"\nField-Type: Static-Text\nField-Placeholder: \"2°. ESTABLÉCESE que la presente rectificación forma parte integrante de la Resolución Exenta N° [numero_res_original], entendiéndose que sus efectos se retrotraen a la fecha de dictación de esta última.\"\nField-Instr: \"Efecto: La rectificación tiene efecto retroactivo ('ex tunc'), pues se entiende que el acto original siempre debió contener el texto correcto. No crea un nuevo acto, sino que enmienda el preexistente.\""
              }
            }
          },
          "cierre_2": {
            "ID": "GN-SEC-0042",
            "Title": "Cierre",
            "Content": "\nID: FORM-RECTIF-ACTO-01-S5-CIERRE-01",
            "Sections": {
              "signature_block": {
                "ID": "GN-SEC-0043",
                "Title": "Signature Block",
                "Content": "\nID: FORM-RECTIF-ACTO-01-S5-FIRMA-01\nField-Label: \"Firma y Timbre\"\nField-Type: Static-Text\nField-Placeholder: \"ANÓTESE, NOTIFÍQUESE Y ARCHÍVESE.\\n\\n\\n[Nombre Autoridad]\\nGOBERNADOR REGIONAL DE ÑUBLE\"\nField-Instr: \"Formalización: Cierre del acto. La notificación es crucial para que los interesados conozcan la versión corregida del acto.\"\n\nEND_EMBEDDED_BLOCK:: FORM-RECTIF-ACTO-01\n```\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-RESCIL-CONV-01"
              }
            }
          },
          "form_metadata_3": {
            "ID": "GN-SEC-0044",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-RESCIL-CONV-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0045",
                "Title": "Form Description",
                "Content": "\nID: FORM-RESCIL-CONV-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Resolución Exenta que aprueba la terminación de un convenio por mutuo acuerdo de las partes (resciliación o mutuo disenso). Formaliza la extinción de las obligaciones de un convenio, basada en la voluntad concordante de los suscriptores.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0046",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-RESCIL-CONV-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Placeholder: \"Artículo 1545 y 1567 del Código Civil (aplicable supletoriamente); Ley N° 19.880; Ley N° 19.175.\"\nField-Instr: \"Marco Legal: Se basa en el principio de autonomía de la voluntad, aplicable a los contratos de la Administración en lo que no contravenga el derecho público.\""
              }
            }
          },
          "header_3": {
            "ID": "GN-SEC-0047",
            "Title": "Header",
            "Content": "\nID: FORM-RESCIL-CONV-01-S1-HEADER-01\n\n- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01"
          },
          "vistos_3": {
            "ID": "GN-SEC-0048",
            "Title": "Vistos",
            "Content": "\nID: FORM-RESCIL-CONV-01-S2-VISTOS-01",
            "Sections": {
              "authority_attributions": {
                "ID": "GN-SEC-0049",
                "Title": "Authority Attributions",
                "Content": "\nID: FORM-RESCIL-CONV-01-S2-ATRIBUCIONES-01\nField-Label: \"Vistos: Atribuciones de la Autoridad\"\nField-Type: Static-Text\nField-Placeholder: \"VISTOS: Lo dispuesto en la Ley N° 19.880; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional; y la Resolución N° 7, de 2019, de la Contraloría General de la República.\"\nField-Instr: \"Competencia: Fundamenta la potestad del Gobernador para dictar el acto.\""
              },
              "original_agreement": {
                "ID": "GN-SEC-0050",
                "Title": "Original Agreement",
                "Content": "\nID: FORM-RESCIL-CONV-01-S2-CONVENIO-01\nField-Label: \"Vistos: Convenio Original\"\nField-Type: Text\nField-Placeholder: \"El Convenio [nombre_convenio], de fecha [fecha_convenio], suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], aprobado por Resolución Exenta N° [numero_res_aprobatoria].\"\nField-Instr: \"Objeto: Individualización del acuerdo de voluntades que se extinguirá.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "resciliation_agreement": {
                "ID": "GN-SEC-0051",
                "Title": "Resciliation Agreement",
                "Content": "\nID: FORM-RESCIL-CONV-01-S2-ACUERDO-01\nField-Label: \"Vistos: Acuerdo de Resciliación\"\nField-Type: Text\nField-Placeholder: \"El acuerdo de resciliación suscrito por las partes con fecha [fecha_acuerdo_resciliacion], en el cual manifiestan su voluntad de poner término anticipado al referido convenio.\"\nField-Instr: \"Documento Fundante: La resolución aprueba un acuerdo previo. Es esencial que este acuerdo exista y se cite.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "considerando_3": {
            "ID": "GN-SEC-0052",
            "Title": "Considerando",
            "Content": "\nID: FORM-RESCIL-CONV-01-S3-CONSIDERANDO-01",
            "Sections": {
              "agreement_existence": {
                "ID": "GN-SEC-0053",
                "Title": "Agreement Existence",
                "Content": "\nID: FORM-RESCIL-CONV-01-S3-EXISTENCIA-01\nField-Label: \"Considerando: Existencia del Convenio\"\nField-Type: Text\nField-Placeholder: \"1°. Que, mediante el instrumento singularizado en los Vistos, las partes acordaron [objeto_del_convenio], estableciendo obligaciones recíprocas.\"\nField-Instr: \"Contexto: Describe la relación contractual que se va a extinguir.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "mutual_agreement": {
                "ID": "GN-SEC-0054",
                "Title": "Mutual Agreement",
                "Content": "\nID: FORM-RESCIL-CONV-01-S3-MUTUOACUERDO-01\nField-Label: \"Considerando: Mutuo Acuerdo\"\nField-Type: Static-Text\nField-Placeholder: \"2°. Que las partes, de común acuerdo y por así convenir a sus intereses, han decidido poner término anticipado al mencionado convenio, manifestando su voluntad expresa en el documento de resciliación citado en los Vistos.\"\nField-Instr: \"Voluntad: La resciliación se fundamenta en el 'mutuo disenso'. Es el pilar de este acto. A diferencia de la revocación (unilateral por mérito) o la invalidación (por ilegalidad), este acto es bilateral y consensual.\""
              },
              "status_of_obligations": {
                "ID": "GN-SEC-0055",
                "Title": "Status of Obligations",
                "Content": "\nID: FORM-RESCIL-CONV-01-S3-OBLIGACIONES-01\nField-Label: \"Considerando: Estado de Obligaciones\"\nField-Type: Select\nField-Instr: \"Efectos Patrimoniales: Define el estado de situación final para evitar litigios futuros. El agente IA debe ofrecer ambas opciones al usuario.\"\nField-Constraint: \"Req: mandatory.\"\n\n- Field-Option: \"no existen obligaciones pendientes entre las partes\"\n- Field-Option: \"las obligaciones pendientes se regularán de la forma que se detalla en el acuerdo\"\nField-Logic: \"Cond: (Ref: SELF.Value) -> Visibility: show. Req: mandatory.\""
              }
            }
          },
          "resuelvo_3": {
            "ID": "GN-SEC-0056",
            "Title": "Resuelvo",
            "Content": "\nID: FORM-RESCIL-CONV-01-S4-RESUELVO-01",
            "Sections": {
              "article_1_approval": {
                "ID": "GN-SEC-0057",
                "Title": "Article 1: Approval",
                "Content": "\nID: FORM-RESCIL-CONV-01-S4-ART1-01\nField-Label: \"Resuelvo: Artículo Primero (Aprobación)\"\nField-Type: Text\nField-Placeholder: \"1°. APRUÉBASE la resciliación del Convenio \\\"[nombre_convenio]\\\", suscrito con fecha [fecha_convenio] entre el Gobierno Regional de Ñuble y [nombre_contraparte].\"\nField-Instr: \"Decisión: Formaliza la aprobación del mutuo disenso.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "article_2_effects": {
                "ID": "GN-SEC-0058",
                "Title": "Article 2: Effects",
                "Content": "\nID: FORM-RESCIL-CONV-01-S4-ART2-01\nField-Label: \"Resuelvo: Artículo Segundo (Efectos)\"\nField-Type: Text\nField-Placeholder: \"2°. DÉJASE constancia que, en virtud de la resciliación aprobada, el referido convenio se extingue a contar de [fecha_efectiva_termino], cesando todos sus efectos para el futuro.\"\nField-Instr: \"Efecto Temporal: La resciliación, por regla general, opera 'ex nunc' (hacia el futuro), sin afectar los actos ya ejecutados.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "article_3_settlement": {
                "ID": "GN-SEC-0059",
                "Title": "Article 3: Settlement",
                "Content": "\nID: FORM-RESCIL-CONV-01-S4-ART3-01\nField-Label: \"Resuelvo: Artículo Tercero (Finiquito)\"\nField-Type: Text\nField-Placeholder: \"3°. DECLÁRASE que las partes se otorgan el más completo y total finiquito respecto de las obligaciones emanadas del convenio que se rescilia, [clausula_opcional_finiquito: con la sola excepción de las que se establecen en el propio acuerdo de resciliación].\"\nField-Instr: \"Finiquito: Cierra la relación contractual. El agente IA debe permitir la inclusión de excepciones si el acuerdo de resciliación así lo estipula.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "cierre_3": {
            "ID": "GN-SEC-0060",
            "Title": "Cierre",
            "Content": "\nID: FORM-RESCIL-CONV-01-S5-CIERRE-01\n\n- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S5-CIERRE-01\n\nEND_EMBEDDED_BLOCK:: FORM-RESCIL-CONV-01\n```\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-REVOCA-ACTO-01"
          },
          "form_metadata_4": {
            "ID": "GN-SEC-0061",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0062",
                "Title": "Form Description",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Resolución Exenta que deja sin efecto un acto administrativo anterior por razones de mérito, oportunidad o conveniencia. Potestad discrecional de la Administración para retirar un acto VÁLIDO por razones de interés público. No aplica a actos ilegales.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0063",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Placeholder: \"Artículo 61, Ley N° 19.880.\"\nField-Instr: \"Marco Legal: Disposición clave que regula la potestad revocatoria y sus límites.\""
              }
            }
          },
          "header_4": {
            "ID": "GN-SEC-0064",
            "Title": "Header",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S1-HEADER-01\n\n- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01"
          },
          "vistos_4": {
            "ID": "GN-SEC-0065",
            "Title": "Vistos",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S2-VISTOS-01",
            "Sections": {
              "authority_attributions": {
                "ID": "GN-SEC-0066",
                "Title": "Authority Attributions",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S2-ATRIBUCIONES-01\nField-Label: \"Vistos: Atribuciones de la Autoridad\"\nField-Type: Static-Text\nField-Placeholder: \"VISTOS: Lo dispuesto en el artículo 61 de la Ley N° 19.880; la Ley N° 19.175; y la Resolución N° 7, de 2019, de la Contraloría General de la República.\"\nField-Instr: \"Competencia: Invoca la norma que confiere la potestad revocatoria.\""
              },
              "act_to_be_revoked": {
                "ID": "GN-SEC-0067",
                "Title": "Act to be Revoked",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S2-ACTOREVOCAR-01\nField-Label: \"Vistos: Acto a Revocar\"\nField-Type: Text\nField-Placeholder: \"La Resolución Exenta N° [numero_res_original] de fecha [fecha_res_original], dictada por esta Gobernación Regional, que [descripcion_acto_original].\"\nField-Instr: \"Objeto: Identificación del acto administrativo válido que se pretende dejar sin efecto.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "considerando_4": {
            "ID": "GN-SEC-0068",
            "Title": "Considerando",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S3-CONSIDERANDO-01",
            "Sections": {
              "merits_rationale": {
                "ID": "GN-SEC-0069",
                "Title": "Merits Rationale",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S3-FUNDAMENTO-01\nField-Label: \"Considerando: Fundamento de Mérito\"\nField-Type: TextArea\nField-Placeholder: \"1°. Que, por razones de mérito, oportunidad y conveniencia, sobrevinientes a la dictación del acto individualizado y fundadas en [descripcion_detallada_del_fundamento_de_interes_publico], se ha estimado necesario para el interés público dejar sin efecto el referido acto administrativo.\"\nField-Instr: \"Causal: La revocación es discrecional pero no arbitraria. Debe fundarse en un cambio de circunstancias o una nueva apreciación del interés público. No puede fundarse en la ilegalidad del acto original. El agente IA debe exigir al usuario la explicitación de este fundamento.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "no_effect_on_rights": {
                "ID": "GN-SEC-0070",
                "Title": "No Effect on Rights",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S3-DERECHOS-01\nField-Label: \"Considerando: No Afectación de Derechos Adquiridos\"\nField-Type: Static-Text\nField-Placeholder: \"2°. Que el acto que por este medio se revoca no ha generado derechos adquiridos por parte de los interesados, o bien, habiéndolos generado, estos han consentido expresamente en la revocación.\"\nField-Instr: \"Límite Esencial: Condición crítica del artículo 61 de la Ley 19.880. La revocación es improcedente si lesiona derechos legítimamente adquiridos por los particulares. Este considerando es una declaración de cumplimiento legal y el agente IA debe tratarlo como una validación obligatoria.\""
              }
            }
          },
          "resuelvo_4": {
            "ID": "GN-SEC-0071",
            "Title": "Resuelvo",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S4-RESUELVO-01",
            "Sections": {
              "article_1_revocation": {
                "ID": "GN-SEC-0072",
                "Title": "Article 1: Revocation",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S4-ART1-01\nField-Label: \"Resuelvo: Artículo Único (Revocación)\"\nField-Type: Text\nField-Placeholder: \"1°. REVÓCASE, por las razones de mérito, oportunidad y conveniencia expuestas en la parte considerativa, la Resolución Exenta N° [numero_res_original], de fecha [fecha_res_original].\"\nField-Instr: \"Decisión: Contiene la declaración de voluntad que extingue el acto anterior.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "article_2_effects": {
                "ID": "GN-SEC-0073",
                "Title": "Article 2: Effects",
                "Content": "\nID: FORM-REVOCA-ACTO-01-S4-ART2-01\nField-Label: \"Resuelvo: Artículo Segundo (Efectos)\"\nField-Type: Static-Text\nField-Placeholder: \"2°. DÉJASE constancia que la presente revocación produce sus efectos a contar de la fecha de su total tramitación, sin afectar las situaciones jurídicas consolidadas bajo la vigencia del acto revocado.\"\nField-Instr: \"Efecto Temporal: La revocación opera 'ex nunc' (hacia el futuro). No tiene efecto retroactivo, a diferencia de la invalidación. Esto protege la seguridad jurídica.\""
              }
            }
          },
          "cierre_4": {
            "ID": "GN-SEC-0074",
            "Title": "Cierre",
            "Content": "\nID: FORM-REVOCA-ACTO-01-S5-CIERRE-01\n\n- Field-Group: Contiene los mismos campos que FORM-RECTIF-ACTO-01-S5-CIERRE-01\n\nEND_EMBEDDED_BLOCK:: FORM-REVOCA-ACTO-01\n```\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-ESCRITO-INICIO-01"
          },
          "form_metadata_5": {
            "ID": "GN-SEC-0075",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-ESCRITO-INICIO-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0076",
                "Title": "Form Description",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Modelo de escrito para que un particular o interesado inicie un procedimiento administrativo ante el GORE Ñuble. Estructura una solicitud formal de un administrado, asegurando que contenga los elementos mínimos para ser acogida a trámite.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0077",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Placeholder: \"Artículos 18, 21, 30 de la Ley N° 19.880.\"\nField-Instr: \"Marco Legal: Rige el derecho de los interesados a iniciar procedimientos y los requisitos de sus solicitudes.\""
              }
            }
          },
          "header_5": {
            "ID": "GN-SEC-0078",
            "Title": "Header",
            "Content": "\nID: FORM-ESCRITO-INICIO-01-S1-HEADER-01",
            "Sections": {
              "summary": {
                "ID": "GN-SEC-0079",
                "Title": "Summary",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S1-SUMILLA-01\nField-Label: \"Sumilla\"\nField-Type: Text\nField-Placeholder: \"EN LO PRINCIPAL: [descripcion_breve_solicitud]; EN EL OTROSÍ: Acompaña documentos.\"\nField-Instr: \"Claridad: La sumilla resume la petición principal y las secundarias para una rápida identificación por parte de la Oficina de Partes.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "addressee": {
                "ID": "GN-SEC-0080",
                "Title": "Addressee",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S1-DESTINATARIO-01\nField-Label: \"Destinatario\"\nField-Type: Static-Text\nField-Placeholder: \"S.S. EL GOBERNADOR REGIONAL DE ÑUBLE\"\nField-Instr: \"Autoridad: Identifica al órgano ante el cual se presenta la solicitud.\""
              }
            }
          },
          "body": {
            "ID": "GN-SEC-0081",
            "Title": "Body",
            "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-BODY-01",
            "Sections": {
              "applicant_identification": {
                "ID": "GN-SEC-0082",
                "Title": "Applicant Identification",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-IDENTIFICACION-01\nField-Label: \"Identificación del Solicitante\"\nField-Type: TextArea\nField-Placeholder: \"[nombre_completo], Cédula de Identidad N° [rut], profesión u oficio [profesion_oficio], domiciliado para estos efectos en [direccion], comuna de [comuna], correo electrónico [email], a US. respetuosamente digo:\"\nField-Instr: \"Legitimación: Identifica al interesado conforme al Art. 21 de la Ley 19.880. La indicación de un medio electrónico es fundamental bajo la nueva normativa de procedimiento administrativo electrónico.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "optional_representation": {
                "ID": "GN-SEC-0083",
                "Title": "Optional Representation",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-REPRESENTACION-01\nField-Label: \"Representación (Opcional)\"\nField-Type: TextArea\nField-Placeholder: \"(Opcional) Actúo en representación de [nombre_representado], C.I./RUT N° [rut_representado], domiciliado en [direccion_representado], calidad que acredito con [documento_poder], que se acompaña.\"\nField-Instr: \"Apoderamiento: Permite la actuación a través de un apoderado, conforme al Art. 22 de la Ley 19.880.\"\nField-Constraint: \"Req: optional.\""
              },
              "facts": {
                "ID": "GN-SEC-0084",
                "Title": "Facts",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-HECHOS-01\nField-Label: \"Hechos\"\nField-Type: TextArea\nField-Placeholder: \"1. Que, con fecha [fecha_hechos], [descripcion_clara_y_circunstanciada_de_los_hechos].\"\nField-Instr: \"Fundamento Fáctico: Base fáctica de la petición. Los hechos deben ser expuestos con claridad y precisión para que la Administración pueda comprender la solicitud.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "law": {
                "ID": "GN-SEC-0085",
                "Title": "Law",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-DERECHO-01\nField-Label: \"Derecho\"\nField-Type: TextArea\nField-Placeholder: \"2. Que, en virtud de lo dispuesto en [normativa_aplicable_al_caso], y en atención a los hechos expuestos, me asiste el derecho a [descripcion_del_derecho_o_interes_legitimo].\"\nField-Instr: \"Fundamento Jurídico: Conecta los hechos con la norma que ampara la solicitud. Aunque no es estrictamente obligatorio para el particular, su inclusión facilita la tramitación.\"\nField-Constraint: \"Req: optional.\""
              },
              "specific_request": {
                "ID": "GN-SEC-0086",
                "Title": "Specific Request",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S2-PETICION-01\nField-Label: \"Petición Concreta\"\nField-Type: TextArea\nField-Placeholder: \"3. Que, en mérito de lo expuesto, solicito a US. se sirva dictar el acto administrativo que [lista_de_peticiones_claras_y_concretas].\"\nField-Instr: \"Petitorio: Debe ser claro, preciso y específico. La Administración debe resolver sobre lo pedido (Principio Conclusivo, Art. 8, Ley 19.880).\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "cierre_5": {
            "ID": "GN-SEC-0087",
            "Title": "Cierre",
            "Content": "\nID: FORM-ESCRITO-INICIO-01-S3-CIERRE-01",
            "Sections": {
              "por_tanto": {
                "ID": "GN-SEC-0088",
                "Title": "Por Tanto",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S3-PORTANTO-01\nField-Label: \"Por Tanto\"\nField-Type: Static-Text\nField-Placeholder: \"POR TANTO,\\n\\nRUEGO A US. acceder a lo solicitado.\"\nField-Instr: \"Fórmula de cierre de la petición principal.\""
              },
              "otrosi": {
                "ID": "GN-SEC-0089",
                "Title": "Otrosí",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S3-OTROSI-01\nField-Label: \"Otrosí\"\nField-Type: TextArea\nField-Placeholder: \"OTROSÍ: Ruego a US. tener por acompañados los siguientes documentos:\\n\\n1. [lista_documentos_adjuntos].\"\nField-Instr: \"Prueba: Permite adjuntar los antecedentes que sustentan la petición, conforme al Art. 30 de la Ley 19.880.\"\nField-Constraint: \"Req: optional.\""
              },
              "signature": {
                "ID": "GN-SEC-0090",
                "Title": "Signature",
                "Content": "\nID: FORM-ESCRITO-INICIO-01-S3-FIRMA-01\nField-Label: \"Firma\"\nField-Type: Static-Text\nField-Placeholder: \"\\n\\n\\n[Firma]\\nC.I. N° [RUT]\"\nField-Instr: \"Autenticación: El escrito debe ser firmado por el interesado o su apoderado.\"\n\nEND_EMBEDDED_BLOCK:: FORM-ESCRITO-INICIO-01\n```\n\n```plaintext\nBEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-ESCRITO-REPO-01"
              }
            }
          },
          "form_metadata_6": {
            "ID": "GN-SEC-0091",
            "Title": "Form Metadata",
            "Content": "\nID: FORM-ESCRITO-REPO-01-S0-METADATA-01",
            "Sections": {
              "form_description": {
                "ID": "GN-SEC-0092",
                "Title": "Form Description",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S0-DESC-01\nField-Label: \"Descripción del Formulario\"\nField-Type: Static-Text\nField-Instr: \"Propósito: Modelo de escrito para interponer un recurso de reposición en contra de un acto administrativo del GORE Ñuble. Es el principal medio de impugnación en sede administrativa, permitiendo que la misma autoridad que dictó el acto revise su legalidad.\""
              },
              "applicable_regulations": {
                "ID": "GN-SEC-0093",
                "Title": "Applicable Regulations",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S0-NORMATIVA-01\nField-Label: \"Normativa Aplicable\"\nField-Type: Static-Text\nField-Placeholder: \"Artículo 59, Ley N° 19.880.\"\nField-Instr: \"Marco Legal: Regula el recurso de reposición y el recurso jerárquico.\""
              }
            }
          },
          "header_6": {
            "ID": "GN-SEC-0094",
            "Title": "Header",
            "Content": "\nID: FORM-ESCRITO-REPO-01-S1-HEADER-01\n\n- Field-Group: Contiene los campos `Sumilla` y `Destinatario` de forma similar a FORM-ESCRITO-INICIO-01."
          },
          "body_2": {
            "ID": "GN-SEC-0095",
            "Title": "Body",
            "Content": "\nID: FORM-ESCRITO-REPO-01-S2-BODY-01",
            "Sections": {
              "appellant_identification": {
                "ID": "GN-SEC-0096",
                "Title": "Appellant Identification",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S2-IDENTIFICACION-01\nField-Label: \"Identificación del Recurrente\"\nField-Type: Text\nField-Placeholder: \"[nombre_completo], Cédula de Identidad N° [rut], en mi calidad de interesado en el procedimiento [identificacion_expediente], a US. respetuosamente digo:\"\nField-Instr: \"Legitimación: Identifica al recurrente como parte interesada en el procedimiento.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "contested_act": {
                "ID": "GN-SEC-0097",
                "Title": "Contested Act",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S2-ACTOIMPUGNADO-01\nField-Label: \"Acto Impugnado\"\nField-Type: TextArea\nField-Placeholder: \"Que, por este acto, y encontrándome dentro del plazo legal de cinco días hábiles establecido en el artículo 59 de la Ley N° 19.880, vengo en interponer recurso administrativo de reposición en contra de la Resolución Exenta N° [numero_res_impugnada], de fecha [fecha_res_impugnada], que me fuera notificada con fecha [fecha_notificacion], y que resolvió [resumen_decision_impugnada].\"\nField-Instr: \"Objeto y Plazo: Identifica el acto recurrido y declara expresamente la oportunidad del recurso. El plazo de 5 días hábiles desde la notificación es fatal. El agente IA debe calcular o advertir sobre este plazo.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "grounds_for_illegality": {
                "ID": "GN-SEC-0098",
                "Title": "Grounds for Illegality",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S2-FUNDAMENTOS-01\nField-Label: \"Fundamentos de Ilegalidad\"\nField-Type: TextArea\nField-Placeholder: \"El acto recurrido adolece de los siguientes vicios de ilegalidad que lo hacen impugnable:\\n\\n1. [Vicio 1: descripción del vicio, norma infringida y argumento jurídico].\\n2. [Vicio 2:...].\"\nField-Instr: \"Causa de Pedir: El recurso debe fundarse en vicios de legalidad del acto (incompetencia, vicios de forma, desviación de poder, ilegalidad en el contenido, falta de fundamentación), no en meros desacuerdos de mérito. La argumentación debe ser precisa.\"\nField-Constraint: \"Req: mandatory.\""
              },
              "specific_request": {
                "ID": "GN-SEC-0099",
                "Title": "Specific Request",
                "Content": "\nID: FORM-ESCRITO-REPO-01-S2-PETICION-01\nField-Label: \"Petición Concreta\"\nField-Type: TextArea\nField-Placeholder: \"En mérito de los fundamentos de hecho y de derecho expuestos, solicito a US. tener por interpuesto el presente recurso de reposición y, en definitiva, acogerlo, y en consecuencia, proceder a [peticion: dejar sin efecto, modificar, reemplazar] el acto recurrido, dictando en su lugar el acto que en derecho corresponda.\"\nField-Instr: \"Petitorio: Define el alcance de la impugnación. La solicitud debe ser coherente con los vicios alegados.\"\nField-Constraint: \"Req: mandatory.\""
              }
            }
          },
          "cierre_6": {
            "ID": "GN-SEC-0100",
            "Title": "Cierre",
            "Content": "\nID: FORM-ESCRITO-REPO-01-S3-CIERRE-01\n\n- Field-Group: Contiene los campos `Por Tanto`, `Otrosí` y `Firma` de forma similar a FORM-ESCRITO-INICIO-01.\n\nEND_EMBEDDED_BLOCK:: FORM-ESCRITO-REPO-01\n```"
          }
        }
      }
    },
    "Content": "# Modelos de Actos Jurídicos GORE Ñuble\n\nID: KB-GN-100-MODELOS-ACTOS-JURIDICOS-STS-V3\nVersion: 3.0.0\nStatus: Draft\nHuman-Creator: FS\nHuman-Editor: FS\nModel-Collaborator: IA-GEMINI\nCreation-Date: 2025-07-10\nModification-Date: 2025-07-10\nRef-STS-Guide: GUIDE-STS-MASTER-01"
  }
}
