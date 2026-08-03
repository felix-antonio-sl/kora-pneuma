---
urn: urn:gn:kb:gn-guia-comunicaciones
nombre: gn-guia-comunicaciones
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-guia-comunicaciones; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/04_habilitadores/comunicaciones/kb_gn_030_guia_comunicaciones_koda.yml (sha256:526c79013eba3783546dd2e6aa91f9608f62481ba62ea9c37b5821871a4bef08); URN KODA legado urn:gorenuble:gn:guia-comunicaciones:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-15
lang: es
tags: ["gn", "gore-os", "koda", "domains", "04-habilitadores", "comunicaciones", "guia"]
familia: bok
---
{
  "_manifest": {
    "urn": "urn:gorenuble:gn:guia-comunicaciones:1.0.0",
    "federation": {
      "visibility": "internal",
      "license": "Institutional Use"
    },
    "compatibility": {
      "min_consumer_version": "1.0.0",
      "breaking_changes_from": null
    },
    "resolution": {
      "canonical_url": "file://knowledge/domains/gn/comunicaciones/kb_gn_030_guia_comunicaciones_koda.yml",
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
  "ID": "GN-GUIA-COMUNICACIONES-01",
  "Version": "1.0.0",
  "Status": "Draft",
  "Format": "KODA/Spec",
  "Human-Creator": "FS",
  "Human-Editor": "FS",
  "Model-Collaborator": "IA-CASCADE",
  "AI-Remediator": "KODA-TRANSFORMER",
  "Creation-Date": "2025-12-15",
  "Modification-Date": "2025-12-15",
  "Ctx": "Guía integral de comunicaciones del GORE Ñuble (fuente STS). Fundamentos, ecosistema, audiencias, operación, marca, métricas y formatos administrativos.",
  "Primary-Source": "staging/gn/kodeando/kb_gn_030_guia_comunicaciones_sts.md",
  "LLM_Parsing_Instructions": {
    "ID": "KODA-LLM-PARSER-01",
    "Req": "Mandatory block following Metadata.",
    "Prohib": "Using for artifact creation or translation.",
    "Content": "BEGIN_LLM_INSTRUCTIONS\nYou are an AI agent consuming a KODA artifact. Parse with absolute fidelity.\n\nFIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).\n\nLEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.\n\nREFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: external URN (optionally with #ID fragment) only.\nLANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.\nEND_LLM_INSTRUCTIONS"
  },
  "Guia_Comunicaciones_GORE_Nuble": {
    "ID": "GN-GUIA-COMUNICACIONES-DOC-01",
    "Title": "Guía Integral de Comunicaciones GORE Ñuble",
    "Sections": {
      "parte_i_fundamentos_estrategicos_y_principios_rectores": {
        "ID": "GN-GCOM-SEC-0001",
        "Title": "Parte I: Fundamentos Estratégicos y Principios Rectores",
        "Content": "\nID: GNC-COM-P1-FUNDAMENTOS-01\nPurp: Establecer bases conceptuales, desafíos del entorno y principios inmutables de la comunicación del GORE.",
        "Sections": {
          "capitulo_1_mision_y_proposito_de_la_comunicacion": {
            "ID": "GN-GCOM-SEC-0002",
            "Title": "Capítulo 1: Misión y Propósito de la Comunicación",
            "Content": "\nID: GNC-COM-P1-MISION-01\n\n- Cpt: Comunicación Clásica (Lasswell).\n  - Def: Quién dice qué, en qué canal, a quién, con qué efecto.\n  - Ctx: Foco en transmisión lineal.\n- Cpt: Comunicación Moderna (K&J).\n  - Def: Proceso de creación de sentido sobre el ejercicio compartido del poder.\n  - Ctx: Foco en intercambio simbólico y construcción de realidad.\n- Cpt: Aplicación GORE.\n  - Purp: Construir la realidad política de Ñuble, gestionar poder simbólico, facilitar gobernanza.\n- Purp: Servir como marco estratégico-operativo para Jefatura de Comunicaciones GORE Ñuble.\n- Obj: Aplicar conceptos de comunicación política a contexto y desafíos de la región.\n- Ctx: Alcance desde análisis del entorno hasta diseño de tácticas y gestión de percepción pública.\n- Ctx: Foco en maximizar eficacia comunicacional para objetivos de la Estrategia Regional de Desarrollo (ERD)."
          },
          "capitulo_2_principios_rectores_de_la_comunicacion": {
            "ID": "GN-GCOM-SEC-0003",
            "Title": "Capítulo 2: Principios Rectores de la Comunicación",
            "Content": "\nID: GNC-COM-P1-PRINCIPIOS-01\nPurp: Definir los pilares no negociables de toda pieza de comunicación.\n\n| Principio | Clave Práctica |\n|-|-|\n| Cpt: Lenguaje claro y preciso | Prohib: Evitar tecnicismos innecesarios. Req: Ordenar info (relevante -> accesorio). Res: Reducción de consultas, refuerzo de confianza. |\n| Cpt: Corrección idiomática (RAE) | Req: Usar tildes, mayúsculas, siglas, numerales según Libro de estilo RAE (2018). Prohib: Excluir anglicismos si existe equivalente (ej. \"evento híbrido\"). |\n| Cpt: Redacción periodística | Req: Titular directo (< 12 palabras). Req: Párrafo ≤ 70 palabras. Req: Estilo con verbos activos, imágenes mentales (ej. “subsidio llegará al refrigerador de 20.000 hogares”). |\n| Cpt: Storytelling público | Req: Toda pieza debe responder: ¿Quién se beneficia? ¿Qué problema resuelve? ¿Cómo invito a la acción? Cpt: Estructura Narrativa. Proc: Situación -> Conflicto -> Solución -> Llamado a la acción. |\n| Cpt: Enfoque ciudadano y territorial | Req: Anclar mensajes en cifras locales, testimonios de usuarios de Ñuble, ejemplos de servicios cercanos. |\n| Cpt: Identidad visual única | Req: Respetar logo, tipografía (Museo Sans), colores (Pantone 185C/293C) según manuales 2022-25. Ref: GNC-COM-P6-MARCA-01. |"
          },
          "capitulo_3_desafios_comunicacionales_especificos_de_nuble": {
            "ID": "GN-GCOM-SEC-0004",
            "Title": "Capítulo 3: Desafíos Comunicacionales Específicos de Ñuble",
            "Content": "\nID: GNC-COM-P1-DESAFIOS-01\n\n- Cpt: Desafío 1 - Pobreza y Desigualdad Estructural.\n  - Ctx: Pobreza por ingresos Ñuble 12.1% vs 6.5% nacional (CASEN 2022).\n  - Ctx: Pobreza multidimensional Ñuble 15.5% vs 16.9% nacional (CASEN 2022).\n  - Act: Comunicar políticas sociales con empatía, evitar estigmatización, enfocar en oportunidades.\n- Cpt: Desafío 2 - Alta Ruralidad.\n  - Ctx: Población rural Ñuble 28.7% vs 11.3% nacional.\n  - Act: Usar canales que superen brecha digital. Asegurar pertinencia cultural de mensajes (urbano vs. rural).\n- Cpt: Desafío 3 - Construcción de Identidad Regional.\n  - Cause: Región de reciente creación (2018).\n  - Act: Forjar un \"nosotros\" ñublensino. Articular visión de futuro compartida que integre 3 provincias (Diguillín, Itata, Punilla).\n- Cpt: Desafío 4 - Bajo Capital Humano.\n  - Ctx: Años de escolaridad promedio 10.9 vs 11.7 nacional.\n  - Act: Crear mensajes claros, accesibles y sin jerga técnica."
          }
        }
      },
      "parte_ii_ecosistema_politico_y_narrativa": {
        "ID": "GN-GCOM-SEC-0005",
        "Title": "Parte II: Ecosistema Político y Narrativa",
        "Content": "\nID: GNC-COM-P2-ECOSISTEMA-01\nPurp: Mapear el entorno de poder y definir el relato central del GORE.",
        "Sections": {
          "capitulo_4_mapeo_del_entorno_institucional": {
            "ID": "GN-GCOM-SEC-0006",
            "Title": "Capítulo 4: Mapeo del Entorno Institucional",
            "Content": "\nID: GNC-COM-P2-MAPEO-01",
            "Sections": {
              "s_4_1_el_gore_como_institucion_comunicadora": {
                "ID": "GN-GCOM-SEC-0007",
                "Title": "4.1. El GORE como Institución Comunicadora",
                "Content": "\nID: GNC-COM-P2-GORE-01\n\n- Mssn: Liderar e impulsar desarrollo sustentable de Ñuble.\n- Cpt: Visión. Def: Ser institución que inspira, lidera e impulsa la integración territorial.\n- Res: Toda comunicación debe reflejar y reforzar esta misión y visión. Cada acción comunica."
              },
              "s_4_2_relacion_con_nivel_central_dpr_y_seremis": {
                "ID": "GN-GCOM-SEC-0008",
                "Title": "4.2. Relación con Nivel Central (DPR y SEREMIs)",
                "Content": "\nID: GNC-COM-P2-CENTRAL-01\n\n- Cpt: Rol DPR. Def: Gobierno interior, orden público. Representa al Presidente.\n- Cpt: Rol SEREMIs. Def: Ejecutan políticas ministeriales sectoriales.\n- Ctx: Dinámica. Def: Tensión inherente entre autonomía regional (GORE) y poder central (DPR).\n- Act: Gestionar tensión buscando coordinación sin subordinación. Establecer canales fluidos para evitar duplicidad y conflictos públicos."
              },
              "s_4_3_dinamica_con_gobiernos_locales_21_municipalidades": {
                "ID": "GN-GCOM-SEC-0009",
                "Title": "4.3. Dinámica con Gobiernos Locales (21 Municipalidades)",
                "Content": "\nID: GNC-COM-P2-MUNI-01\n\n- Cpt: Rol GORE. Def: Transfiere recursos (FRIL, FNDR), asiste técnicamente, busca coherencia con PLADECOs.\n- Ctx: Dinámica. Def: Relación de poder asimétrica (GORE financia, municipios ejecutan). Potencial de conflicto.\n- Act: Comunicación proactiva con alcaldes y SECPLAs. Posicionar al GORE como socio estratégico, no como mero financiador."
              },
              "s_4_4_el_consejo_regional_core": {
                "ID": "GN-GCOM-SEC-0010",
                "Title": "4.4. El Consejo Regional (CORE)",
                "Content": "\nID: GNC-COM-P2-CORE-01\n\n- Cpt: Rol CORE. Def: Aprueba presupuesto, planes, estrategias. Fiscaliza al Gobernador.\n- Res: El CORE es la primera y más importante audiencia política interna. Su apoyo es vital para la gobernabilidad.\n- Act: Mantener flujo de información constante. Presentar propuestas de forma clara y persuasiva. Anticipar y gestionar objeciones."
              }
            }
          },
          "capitulo_5_construyendo_la_narrativa_del_gore_nuble": {
            "ID": "GN-GCOM-SEC-0011",
            "Title": "Capítulo 5: Construyendo la Narrativa del GORE Ñuble",
            "Content": "\nID: GNC-COM-P2-NARRATIVA-01",
            "Sections": {
              "s_5_1_del_mensaje_central_al_relato_politico": {
                "ID": "GN-GCOM-SEC-0012",
                "Title": "5.1. Del Mensaje Central al Relato Político",
                "Content": "\nID: GNC-COM-P2-RELATO-01\n\n- Src: Desafíos y Oportunidades de la Estrategia Regional de Desarrollo (ERD).\n- Act: Traducir ejes de la ERD en un relato coherente, simple y movilizador.\n- Ex: Relato. \"Ñuble, la región que se levanta desde sus raíces para construir un futuro más justo y sostenible\"."
              },
              "s_5_2_el_discurso_del_gobernador_a_generos_y_funciones": {
                "ID": "GN-GCOM-SEC-0013",
                "Title": "5.2. El Discurso del Gobernador/a: Géneros y Funciones",
                "Content": "\nID: GNC-COM-P2-DISCURSO-01\nPurp: Cada tipo de discurso cumple una función específica.\n\n- Cpt: Cuenta Pública Anual. Purp: Enmarcar gestión, definir futuro, reforzar visión regional.\n- Cpt: Anuncios Inversión/Proyectos. Purp: Materializar estrategia. Comunicar \"qué\" (obra) y \"porqué\" (beneficio).\n- Cpt: Discursos en Crisis. Purp: Proyectar calma, autoridad y empatía. Ser la \"voz de la región\".\n- Cpt: Discursos de Identidad Regional. Purp: Fortalecer pertenencia celebrando hitos, tradiciones y personajes locales."
              },
              "s_5_3_navegando_el_partisanismo": {
                "ID": "GN-GCOM-SEC-0014",
                "Title": "5.3. Navegando el Partisanismo",
                "Content": "\nID: GNC-COM-P2-PARTIDOS-01\n\n- Ctx: Gobernador y CORE tienen afiliaciones partidistas. La comunicación no puede ignorarlo.\n- Cpt: Estilo Republicano (Teórico). Ctx: Tiende a ser más directo, enfocado en principios y valores.\n- Cpt: Estilo Demócrata (Teórico). Ctx: Tiende a ser más pragmático, enfocado en circunstancias y grupos específicos.\n- Act: Identificar estilos discursivos de actores políticos de Ñuble (autoridades, oposición) para anticipar argumentos.\n- Act: Aspirar a un tono transversal, pero reconociendo el lenguaje de la propia coalición."
              }
            }
          }
        }
      },
      "parte_iii_la_audiencia_ciudadana": {
        "ID": "GN-GCOM-SEC-0015",
        "Title": "Parte III: La Audiencia Ciudadana",
        "Content": "\nID: GNC-COM-P3-AUDIENCIA-01\nPurp: Comprender las características demográficas, sociales y de consumo de medios de los habitantes de Ñuble.",
        "Sections": {
          "capitulo_6_perfil_demografico_y_sociocultural": {
            "ID": "GN-GCOM-SEC-0016",
            "Title": "Capítulo 6: Perfil Demográfico y Sociocultural",
            "Content": "\nID: GNC-COM-P3-PERFIL-01",
            "Sections": {
              "s_6_1_nuble_en_cifras_implicancias_comunicacionales": {
                "ID": "GN-GCOM-SEC-0017",
                "Title": "6.1. Ñuble en Cifras: Implicancias Comunicacionales",
                "Content": "\nID: GNC-COM-P3-CIFRAS-01\n\n- Cpt: Población. Ctx: 512,289 hab. (2024). Crecimiento del 6.6% (superior al nacional).\n- Cpt: Composición. Ctx: Concentración en Chillán (37%). Provincias de Itata y Punilla con comunas pequeñas y dispersas.\n  - Res: Estrategia de medios diferenciada: masiva para Chillán, hiperlocal/comunitaria para resto del territorio.\n- Cpt: Envejecimiento. Ctx: Comunas como Cobquecura, Portezuelo, Ránquil con >20% de población 65+.\n  - Res: Segmentar mensajes para adultos mayores. Usar canales tradicionales (radio). Temas de interés: salud, pensiones, seguridad."
              },
              "s_6_2_brechas_sociales_y_como_comunicarlas": {
                "ID": "GN-GCOM-SEC-0018",
                "Title": "6.2. Brechas Sociales y Cómo Comunicarlas",
                "Content": "\nID: GNC-COM-P3-BRECHAS-01\n\n- Cpt: Pobreza. Ctx: Especial dureza en comunas rurales.\n  - Act: Evitar lenguaje tecnocrático. Comunicar impacto concreto de la inversión en la vida de las personas. Usar testimonios.\n- Cpt: Inseguridad Alimentaria. Ctx: 16.6% de hogares.\n  - Act: Comunicar programas de fomento productivo (INDAP, GORE) como solución directa.\n- Cpt: Carencia Servicios Básicos. Ctx: 17.8% de la población (vs 13.1% país), especialmente alto en Ninhue (50.6%), Cobquecura (43.3%).\n  - Act: Inversión en APR e infraestructura es un mensaje de alto impacto. Visualizar \"antes y después\"."
              },
              "s_6_3_capital_humano_foco_en_educacion_salud_calidad_de_vida": {
                "ID": "GN-GCOM-SEC-0019",
                "Title": "6.3. Capital Humano: Foco en Educación, Salud, Calidad de Vida",
                "Content": "\nID: GNC-COM-P3-CAPITAL-01\n\n- Cpt: Educación. Ctx: Escolaridad promedio inferior al nacional. Inasistencia grave (15.4%) es preocupación.\n  - Act: Mensajes simples y directos. Apelar a aspiraciones de padres por el futuro de sus hijos.\n- Cpt: Salud. Ctx: Alta inscripción en salud municipal (438k personas).\n  - Act: Posicionar al GORE como actor clave en fortalecimiento de la red de salud (CESFAM, Postas Rurales). Comunicar inversión en equipamiento es altamente valorado."
              }
            }
          },
          "capitulo_7_el_consumo_de_medios_en_la_region": {
            "ID": "GN-GCOM-SEC-0020",
            "Title": "Capítulo 7: El Consumo de Medios en la Región",
            "Content": "\nID: GNC-COM-P3-MEDIOS-01",
            "Sections": {
              "s_7_1_canales_de_informacion_broadcasting_vs_narrowcasting": {
                "ID": "GN-GCOM-SEC-0021",
                "Title": "7.1. Canales de Información: Broadcasting vs. Narrowcasting",
                "Content": "\nID: GNC-COM-P3-CANALES-01\n\n- Cpt: Broadcasting (Masivo). Ctx: Cobertura regional amplia (ej. Radio Ñuble, La Discusión). Mensajes generales para audiencias diversas.\n- Cpt: Narrowcasting (De Nicho). Ctx: Audiencias segmentadas (ej. radios comunitarias, grupos WhatsApp locales). Mensajes específicos, alta credibilidad en nicho.\n- Act: Estrategia dual. Usar broadcasting para construir agenda y narrowcasting para movilizar y persuadir."
              },
              "s_7_2_la_dieta_mediatica_del_ciudadano_de_nuble": {
                "ID": "GN-GCOM-SEC-0022",
                "Title": "7.2. La Dieta Mediática del Ciudadano de Ñuble",
                "Content": "\nID: GNC-COM-P3-DIETA-01\n\n- Req: Realizar estudio/encuesta de consumo de medios en la región para validar estas hipótesis.\n- Cpt: Hipótesis 1. Ctx: Alta penetración de la radio (zonas rurales, adultos mayores).\n- Cpt: Hipótesis 2. Ctx: Diario La Discusión como principal formador de opinión de la élite regional.\n- Cpt: Hipótesis 3. Ctx: Jóvenes urbanos consumen noticias vía redes sociales (Instagram, Facebook, TikTok).\n- Cpt: Hipótesis 4. Ctx: Creciente importancia de medios digitales locales y páginas \"noticias\" comunales en Facebook."
              },
              "s_7_3_conectividad_digital_brechas_y_oportunidades": {
                "ID": "GN-GCOM-SEC-0023",
                "Title": "7.3. Conectividad Digital: Brechas y Oportunidades",
                "Content": "\nID: GNC-COM-P3-DIGITAL-01\n\n- Ctx: 94.9% acceso a internet, PERO 49.7% es solo móvil.\n- Cpt: Problema. Def: Dependencia de conexiones móviles implica menor estabilidad/velocidad. Brecha rural en fibra óptica.\n- Act: Campañas digitales no pueden depender de videos alta resolución. Privilegiar formatos bajo consumo de datos (texto, imágenes livianas).\n- Warn: Estrategia \"Digital First\" no es viable para toda la región."
              }
            }
          }
        }
      },
      "parte_iv_caja_de_herramientas_comunicacionales": {
        "ID": "GN-GCOM-SEC-0024",
        "Title": "Parte IV: Caja de Herramientas Comunicacionales",
        "Content": "\nID: GNC-COM-P4-HERRAMIENTAS-01\nPurp: Detallar el conjunto de herramientas, tácticas, formatos y lineamientos editoriales para la ejecución de la estrategia.",
        "Sections": {
          "capitulo_8_lineamientos_editoriales_y_tono_de_voz": {
            "ID": "GN-GCOM-SEC-0025",
            "Title": "Capítulo 8: Lineamientos Editoriales y Tono de Voz",
            "Content": "\nID: GNC-COM-P4-EDITORIAL-01",
            "Sections": {
              "s_8_1_tono_y_estructura": {
                "ID": "GN-GCOM-SEC-0026",
                "Title": "8.1. Tono y Estructura",
                "Content": "\nID: GNC-COM-P4-TONO-01\nPurp: Definir los tonos de voz aplicables a las comunicaciones para asegurar coherencia y adecuación al contexto.\n\n- Cpt: Tono-Principal (Resolutivo e Imparcial).\n  - Def: Tono por defecto para todos los actos administrativos formales.\n  - Ctx: Refleja la autoridad, seriedad y objetividad del GORE como órgano del Estado. Se aplica de manera estricta en las partes dispositivas (`RESUELVO:`).\n  - Rec: Cercano en la comunicación ciudadana. Ex: “Usted puede postular…” en lugar de “El interesado deberá…”.\n- Cpt: Tono-Secundario (Claro y Didáctico).\n  - Def: Obligación de explicar las razones de una decisión de manera que un ciudadano informado pueda comprenderlas. No implica informalidad.\n  - Ctx: Aplicable preferentemente en las secciones de fundamentación (`CONSIDERANDO:`) y en el cuerpo de los oficios informativos.\n- Cpt: Tono-Funcional (Directo y Conciso).\n  - Def: Aplicable exclusivamente a comunicaciones internas (Memorándums).\n  - Ctx: Foco en la eficiencia operativa, la claridad de la instrucción y la agilidad.\n- Cpt: Tono-Inclusivo.\n  - Req: Utilizar un lenguaje no sexista en todas las comunicaciones.\n  - Mech: Priorizar el uso de sustantivos genéricos o colectivos (ej. \"el personal\", \"la ciudadanía\", \"el funcionariado\").\n  - Prohib: Uso de desdoblamientos de género (ej. \"los y las funcionarios/as\") y caracteres como \"@\" o \"x\".\n\n| Elemento | Recomendación |\n|-|-|\n| Cpt: Titular | Rec: Verbo + beneficio (“Amplían Beca Rural a 1.500 estudiantes”) |\n| Cpt: Lead (1er párrafo) | Req: Responde Qué-Quién-Cuándo-Dónde-Por qué en ≤ 40 palabras. |\n| Cpt: Cuerpo | Rec: Datos, contexto, citas breves (≤ 20 palabras). |\n| Cpt: Cierre | Req: Llamado a la acción y contacto oficial (teléfono, URL gob.cl). |"
              },
              "s_8_2_principios_rectores_de_redaccion_administrativa": {
                "ID": "GN-GCOM-SEC-0027",
                "Title": "8.2. Principios Rectores de Redacción Administrativa",
                "Content": "\nID: GNC-COM-P4-PRINCIPIOS-REDACT-01\nPurp: Establecer las reglas no negociables que deben regir la redacción de toda comunicación administrativa del GORE Ñuble.\n\n- Cpt: Principio-1-Claridad-y-Precisión.\n  - Req: Evitar ambigüedades, jerga técnica innecesaria, y acrónimos sin definir en su primera aparición. El lenguaje debe ser directo y sin adornos retóricos.\n  - Fnd: Principio de Lenguaje Claro, orientado a facilitar la comprensión por parte de la ciudadanía y otros organismos.\n- Cpt: Principio-2-Corrección-Idiomática.\n  - Req: Adhesión estricta a las normas gramaticales y ortográficas de la Real Academia Española (RAE).\n  - Prohib: Uso de anglicismos o extranjerismos si existe un equivalente asentado en español (ej. \"correo electrónico\" en lugar de \"e-mail\"; \"reunión\" en lugar de \"meeting\").\n- Cpt: Principio-3-Legalidad-y-Fundamentación.\n  - Req: Todo acto administrativo que cree, modifique o extinga derechos u obligaciones debe citar explícitamente su fundamento normativo en la sección VISTOS:.\n  - Fnd: Principio de Legalidad (Art. 2, Ley N° 18.575) y Deber de Motivación de los actos administrativos (Art. 41, Ley N° 19.880)."
              },
              "s_8_3_recursos_narrativos_storytelling": {
                "ID": "GN-GCOM-SEC-0028",
                "Title": "8.3. Recursos Narrativos (Storytelling)",
                "Content": "\nID: GNC-COM-P4-STORYTELLING-01\n\n- Cpt: Recurso 1. Def: Personaje guía (funcionario, usuaria, vecino).\n- Cpt: Recurso 2. Def: Conflicto (brecha, problema social).\n- Cpt: Recurso 3. Def: Solución (programa, trámite digital).\n- Cpt: Recurso 4. Def: Resultado medible (cifras o testimonios).\n- Ref: GNC-COM-P1-PRINCIPIOS-01"
              }
            }
          },
          "capitulo_9_el_mix_de_canales_y_formatos": {
            "ID": "GN-GCOM-SEC-0029",
            "Title": "Capítulo 9: El Mix de Canales y Formatos",
            "Content": "\nID: GNC-COM-P4-MIX-01",
            "Sections": {
              "s_9_1_comunicacion_masiva_broadcasting": {
                "ID": "GN-GCOM-SEC-0030",
                "Title": "9.1. Comunicación Masiva (Broadcasting)",
                "Content": "\nID: GNC-COM-P4-MASIVA-01\n\n- Purp: Generar conocimiento y recordación de alto nivel sobre prioridades del GORE.\n- Ctx: Foco en simplicidad, repetición, alcance.\n- Cpt: Canales-Ñuble. Def: Radios (jingles, frases cortas), Prensa Escrita (para audiencias influyentes), TV Local/Regional (impacto visual).\n- Cpt: Contenido-Tipo. Def: Hitos de gestión, campañas de bien público, llamados a participación.\n- Warn: Costosa, efectividad a corto plazo, requiere consistencia."
              },
              "s_9_2_comunicacion_segmentada_narrowcasting": {
                "ID": "GN-GCOM-SEC-0031",
                "Title": "9.2. Comunicación Segmentada (Narrowcasting)",
                "Content": "\nID: GNC-COM-P4-SEGMENTADA-01\n\n- Purp: Entregar mensajes específicos y relevantes a audiencias particulares para maximizar persuasión.\n- Cpt: Segmentos Clave en Ñuble.\n  - Cpt: Agricultores. Ctx: Medios sectoriales. Foco en riego, fomento.\n  - Cpt: Jóvenes. Ctx: Plataformas digitales (Instagram, TikTok). Foco en educación, emprendimiento, cultura.\n  - Cpt: Adultos Mayores. Ctx: Radios locales, prensa. Foco en salud, seguridad.\n  - Cpt: Emprendedores. Ctx: Redes (LinkedIn), alianzas con cámaras de comercio. Foco en fondos (FRPD), capacitación."
              },
              "s_9_3_medios_digitales_y_plataformas_sociales": {
                "ID": "GN-GCOM-SEC-0032",
                "Title": "9.3. Medios Digitales y Plataformas Sociales",
                "Content": "\nID: GNC-COM-P4-DIGITAL-01\n\n- Act: Evolucionar de \"sitio web-folleto\" (brochureware) a \"plataforma de servicio y comunidad\".\n- Cpt: Componentes Integrados.\n  - Cpt: Sitio Web GORE. Def: Hub central de información oficial. Req: Claro, fácil de navegar, móvil.\n  - Cpt: Facebook. Def: Principal canal masivo-digital. Rec: Anuncios segmentados, transmisiones en vivo.\n  - Cpt: Twitter/X. Def: Comunicación rápida con periodistas, líderes de opinión. Rec: Monitoreo en tiempo real.\n  - Cpt: Instagram/TikTok. Def: Audiencias jóvenes. Rec: Contenido visual, historias cortas, \"lado humano\".\n  - Cpt: YouTube. Def: Repositorio de videos (testimonios, resúmenes, explicaciones).\n  - Cpt: WhatsApp. Def: Comunicación directa con líderes comunitarios, dirigentes, medios locales."
              },
              "s_9_4_portafolio_de_productos_y_formatos_especificos": {
                "ID": "GN-GCOM-SEC-0033",
                "Title": "9.4. Portafolio de Productos y Formatos Específicos",
                "Content": "\nID: GNC-COM-P4-PORTAFOLIO-01\n\n| Tipología | Extensión | Elementos Obligatorios |\n|-|-|-|\n| Cpt: Decreto / Resolución | Req: ≤ 10 págs | Req: Vistos – Considerandos – Resuelvo; logo sin slogan |\n| Cpt: Oficio | Req: ≤ 300 palabras | Req: Nº folio, materia, saludo, cuerpo, firma |\n| Cpt: Minuta / Informe | Req: 1-3 págs | Req: Antecedentes → Análisis → Conclusión; gráficos paleta oficial |\n| Cpt: Post RR.SS. | Req: 120-150 car. + img 1:1 | Req: Título, link corto, ALT descriptivo |\n| Cpt: Nota de prensa | Req: 350-450 palabras | Req: Titular noticia, lead, cita Gobernador/a, call to action |\n| Cpt: Landing page | Req: 3 scrolls máx. | Req: H1 visible, subtítulos H2-H3, botón CTA, video ≤ 1 min. |"
              }
            }
          }
        }
      },
      "parte_v_gestion_del_debate_y_relacion_con_medios": {
        "ID": "GN-GCOM-SEC-0034",
        "Title": "Parte V: Gestión del Debate y Relación con Medios",
        "Content": "\nID: GNC-COM-P5-DEBATE-01\nPurp: Establecer las estrategias para interactuar con el debate público y los medios de comunicación como actores políticos.",
        "Sections": {
          "capitulo_10_la_gestion_del_debate_publico": {
            "ID": "GN-GCOM-SEC-0035",
            "Title": "Capítulo 10: La Gestión del Debate Público",
            "Content": "\nID: GNC-COM-P5-GESTION-DEBATE-01",
            "Sections": {
              "s_10_1_debatir_para_educar_y_persuadir": {
                "ID": "GN-GCOM-SEC-0036",
                "Title": "10.1. Debatir para Educar y Persuadir",
                "Content": "\nID: GNC-COM-P5-EDUCAR-01\n\n- Cpt: Cualquier foro público es una instancia de debate.\n- Cpt: Preparación.\n  - Req: Definir 2-3 mensajes clave a instalar.\n  - Req: Preparar respuestas a críticas probables.\n  - Req: Adaptar lenguaje y ejemplos a la audiencia.\n- Cpt: Ejecución.\n  - Req: Disciplina del Mensaje (volver siempre a los mensajes clave).\n  - Rec: Técnica del Puente. Reconocer pregunta y \"puentear\" hacia el mensaje propio. Ex: \"Esa es una pregunta interesante, pero lo que realmente preocupa a la gente de Ñuble es...\"."
              },
              "s_10_2_fomentando_la_participacion_deliberativa": {
                "ID": "GN-GCOM-SEC-0037",
                "Title": "10.2. Fomentando la Participación Deliberativa",
                "Content": "\nID: GNC-COM-P5-DELIBERAR-01\n\n- Purp: Canalizar participación ciudadana para legitimar gestión y mejorar políticas.\n- Cpt: Mecanismos Presenciales.\n  - Cpt: COSOC Regional. Def: Órgano consultivo. Req: Comunicaciones debe proveerle información clara y oportuna. Ref: `kb_023_intro_gores.md#GORE-GUIA-ESTRUCTURA-COSOC-01`.\n  - Cpt: Consultas Públicas. Ctx: Para planes importantes (ERD, PROT). Req: Asegurar convocatoria amplia y diversa.\n- Cpt: Mecanismos Online.\n  - Cpt: Encuestas y Votaciones. Rec: En redes sociales para temas de bajo conflicto.\n  - Cpt: Foros de Discusión Temáticos. Rec: En sitio web del GORE sobre proyectos específicos. Req: Moderación activa."
              }
            }
          },
          "capitulo_11_los_medios_como_actor_politico": {
            "ID": "GN-GCOM-SEC-0038",
            "Title": "Capítulo 11: Los Medios como Actor Político",
            "Content": "\nID: GNC-COM-P5-MEDIOS-ACTOR-01",
            "Sections": {
              "s_11_1_los_medios_como_segunda_legislatura": {
                "ID": "GN-GCOM-SEC-0039",
                "Title": "11.1. Los Medios como \"Segunda Legislatura\"",
                "Content": "\nID: GNC-COM-P5-SEGUNDA-LEGIS-01\n\n- Cpt: Cambio de Paradigma. Def: Los medios no solo reportan la política, la *hacen* (negocian, interpretan, amplifican).\n- Res: Tratar a periodistas y editores como actores políticos con intereses propios.\n- Act: Construir relaciones, entender sus agendas, ofrecer historias (proactivo), no solo enviar comunicados (reactivo)."
              },
              "s_11_2_fijando_la_agenda_agenda_setting": {
                "ID": "GN-GCOM-SEC-0040",
                "Title": "11.2. Fijando la Agenda (Agenda-Setting)",
                "Content": "\nID: GNC-COM-P5-AGENDA-01\n\n- Def: Lograr que los temas prioritarios para el GORE sean también los temas prioritarios para los medios y el público.\n- Act: Consistencia de mensaje, creación de hitos noticiables, provisión de datos, acceso a voceros."
              },
              "s_11_3_la_lucha_por_el_encuadre_framing": {
                "ID": "GN-GCOM-SEC-0041",
                "Title": "11.3. La Lucha por el Encuadre (Framing)",
                "Content": "\nID: GNC-COM-P5-FRAMING-01\n\n- Def: No es solo *qué* se discute, sino *cómo* se discute.\n- Cpt: Guerra de Marcos.\n  - Cpt: Marco GORE (Ej). Def: Inversión en camino rural -> \"Conectividad para el Desarrollo Productivo\".\n  - Cpt: Marco Oposición (Potencial). Def: Inversión en camino rural -> \"Gasto injustificado que beneficia a unos pocos\".\n- Act: Anticipar marcos negativos, inocular el marco propio proactivamente, usar metáforas y lenguaje simple (\"Justicia territorial\")."
              }
            }
          },
          "capitulo_12_gestionando_la_percepcion_mediatica": {
            "ID": "GN-GCOM-SEC-0042",
            "Title": "Capítulo 12: Gestionando la Percepción Mediática",
            "Content": "\nID: GNC-COM-P5-PERCEPCION-01",
            "Sections": {
              "s_12_1_el_efecto_de_medio_hostil": {
                "ID": "GN-GCOM-SEC-0043",
                "Title": "12.1. El \"Efecto de Medio Hostil\"",
                "Content": "\nID: GNC-COM-P5-HOSTIL-01\n\n- Cpt: Principio. Def: Partidarios de cualquier causa tienden a percibir la cobertura neutral como sesgada en su contra.\n- Res: Es imposible lograr que los adherentes más fervientes se sientan 100% satisfechos.\n- Act: No sobrerreaccionar a quejas internas. Gestionar expectativas: el objetivo es cobertura justa, no propaganda."
              },
              "s_12_2_construyendo_confianza_con_los_medios": {
                "ID": "GN-GCOM-SEC-0044",
                "Title": "12.2. Construyendo Confianza con los Medios",
                "Content": "\nID: GNC-COM-P5-CONFIANZA-01\n\n- Purp: La confianza no es en el medio, sino en el GORE como fuente de información.\n- Act: Ser fuente confiable (nunca mentir), transparencia (reconocer errores), disponibilidad (incluso para malas noticias), relaciones profesionales."
              },
              "s_12_3_la_exposicion_selectiva_y_las_burbujas_informativas": {
                "ID": "GN-GCOM-SEC-0045",
                "Title": "12.3. La Exposición Selectiva y las Burbujas Informativas",
                "Content": "\nID: GNC-COM-P5-SELECTIVA-01\n\n- Cpt: Las audiencias eligen medios que confirman sus creencias, creando \"cámaras de eco\".\n- Res: Una estrategia basada en un solo tipo de medio está destinada al fracaso.\n- Act: Estrategia multicanal para alcanzar diferentes burbujas. Usar mensajeros diversos con credibilidad en distintas audiencias."
              }
            }
          }
        }
      },
      "parte_vi_gobernanza_y_procesos_internos": {
        "ID": "GN-GCOM-SEC-0046",
        "Title": "Parte VI: Gobernanza y Procesos Internos",
        "Content": "\nID: GNC-COM-P6-GOBERNANZA-01\nPurp: Definir la estructura, roles, flujos de trabajo y métricas para la operación comunicacional.",
        "Sections": {
          "capitulo_13_identidad_visual_y_uso_de_marca": {
            "ID": "GN-GCOM-SEC-0047",
            "Title": "Capítulo 13: Identidad Visual y Uso de Marca",
            "Content": "\nID: GNC-COM-P6-MARCA-01\n\n- Cpt: Logo. Req: Versiones *sintetizada* (≥ 15 mm) y *detalle* (≥ 25 mm).\n- Cpt: Área de Resguardo. Req: Mínimo la altura de la “x” del logotipo.\n- Cpt: Fotografía Oficial. Rec: Luz natural, fondos sobrios, protagonistas en primer plano."
          },
          "capitulo_14_flujo_de_produccion_y_gobernanza": {
            "ID": "GN-GCOM-SEC-0048",
            "Title": "Capítulo 14: Flujo de Producción y Gobernanza",
            "Content": "\nID: GNC-COM-P6-FLUJO-01\n\n- Proc: Flujo de Producción (Estándar 5 días hábiles).\n  1. Req: Solicitud interna.\n  2. Act: Redacción borrador (Periodista).\n  3. Act: Revisión estilo y RAE (Editor).\n  4. Act: Validación jurídica/técnica.\n  5. Act: Diseño gráfico y accesibilidad.\n  6. Act: Aprobación Gobernador/a.\n  7. Act: Publicación y archivo en GEDOC.\n\n| Rol | Responsabilidad | Herramientas Clave |\n|-|-|-|\n| Cpt: Jefatura Com. | Resp: Custodia de marca, vocería principal | Req: KitDigital, esta guía |\n| Cpt: Editor/a | Resp: Calidad lingüística, RAE, lenguaje inclusivo | Req: Libro de estilo RAE |\n| Cpt: Periodista | Resp: Redacción, entrevistas, storytelling | Req: Manual Salas 2007 |\n| Cpt: Diseñador/a | Resp: Piezas gráficas, adaptación | Req: Manuales gráficos 2024-25 |\n| Cpt: Webmaster | Resp: SEO, UX, accesibilidad | Req: Recomendaciones Web 2024 |\n| Cpt: Analista RRSS | Resp: Métricas, escucha social | Req: Suite RRSS institucional |"
          },
          "capitulo_15_indicadores_de_exito_kpis": {
            "ID": "GN-GCOM-SEC-0049",
            "Title": "Capítulo 15: Indicadores de Éxito (KPIs)",
            "Content": "\nID: GNC-COM-P6-KPIS-01\n\n- Obj: Comprensión. Def: Tiempo de lectura de decreto-tipo ≤ 4 min.\n- Obj: Claridad. Def: Reducción de reclamos por comprensión de texto en -25% vs 2024.\n- Obj: Alcance. Def: Alcance promedio RR.SS. +30% seguidores únicos.\n- Obj: Reputación. Def: Cobertura positiva en prensa local ≥ 75% de notas sobre programas regionales."
          }
        }
      },
      "parte_vii_topicos_especiales_y_desafios_futuros": {
        "ID": "GN-GCOM-SEC-0050",
        "Title": "Parte VII: Tópicos Especiales y Desafíos Futuros",
        "Content": "\nID: GNC-COM-P7-ESPECIALES-01\nPurp: Abordar escenarios comunicacionales complejos y anticipar tendencias.",
        "Sections": {
          "capitulo_16_comunicacion_en_tiempos_de_crisis": {
            "ID": "GN-GCOM-SEC-0051",
            "Title": "Capítulo 16: Comunicación en Tiempos de Crisis",
            "Content": "\nID: GNC-COM-P7-CRISIS-01",
            "Sections": {
              "s_16_1_identificacion_de_riesgos_en_nuble": {
                "ID": "GN-GCOM-SEC-0052",
                "Title": "16.1. Identificación de Riesgos en Ñuble",
                "Content": "\nID: GNC-COM-P7-RIESGOS-01\n\n- Cpt: Amenaza 1 - Incendios Forestales. Ctx: Prob. alta, impacto muy alto.\n- Cpt: Amenaza 2 - Sequía / Déficit Hídrico. Ctx: Prob. muy alta, impacto alto.\n- Cpt: Amenaza 3 - Erupción Volcánica. Ctx: Prob. baja, impacto catastrófico (Nevados de Chillán).\n- Cpt: Amenaza 4 - Crisis Social/Política. Ex: Protestas, acusaciones de corrupción."
              },
              "s_16_2_protocolo_de_respuesta_mediatica": {
                "ID": "GN-GCOM-SEC-0053",
                "Title": "16.2. Protocolo de Respuesta Mediática",
                "Content": "\nID: GNC-COM-P7-PROTOCOLO-01\n\n- Proc: Fase 0 - Preparación. Act: Listados de prensa actualizados, voceros entrenados, mensajes pre-aprobados.\n- Proc: Fase 1 - Primeras 24h. Act: Comunicar rápido (\"estamos trabajando en...\"), unificar vocería, mostrar empatía.\n- Proc: Fase 2 - Desarrollo. Act: Actualizaciones regulares, combatir desinformación con datos, mostrar acción concreta."
              }
            }
          },
          "capitulo_17_conclusiones_y_futuro_de_la_comunicacion": {
            "ID": "GN-GCOM-SEC-0054",
            "Title": "Capítulo 17: Conclusiones y Futuro de la Comunicación",
            "Content": "\nID: GNC-COM-P7-FUTURO-01",
            "Sections": {
              "s_17_1_sintesis_de_principios_estrategicos": {
                "ID": "GN-GCOM-SEC-0055",
                "Title": "17.1. Síntesis de Principios Estratégicos",
                "Content": "\nID: GNC-COM-P7-SINTESIS-01\n\n- Cpt: Principio 1 - Proactividad. Def: La comunicación modela la política, no la sigue.\n- Cpt: Principio 2 - Coherencia. Def: Todos los actos del GORE comunican.\n- Cpt: Principio 3 - Conocimiento de Audiencia. Def: La segmentación es clave.\n- Cpt: Principio 4 - Adaptabilidad. Def: Estrategia flexible, abierta a nuevos canales.\n- Cpt: Principio 5 - Autenticidad. Def: La confianza se basa en credibilidad y transparencia."
              },
              "s_17_2_tendencias_y_desafios_futuros": {
                "ID": "GN-GCOM-SEC-0056",
                "Title": "17.2. Tendencias y Desafíos Futuros",
                "Content": "\nID: GNC-COM-P7-TENDENCIAS-01\n\n- Cpt: Tendencia 1 - Hiper-personalización. Def: Uso de datos para mensajes micro-segmentados.\n- Cpt: Tendencia 2 - Inteligencia Artificial. Purp: Para monitoreo, análisis y generación de contenido.\n- Cpt: Tendencia 3 - Desinformación como Arma. Req: Capacidades de respuesta rápida y fact-checking.\n- Cpt: Tendencia 4 - Video Vertical. Ctx: Formato (Reels, TikTok) se consolida para audiencias jóvenes."
              }
            }
          }
        }
      },
      "anexo_guia_de_estilo_y_formato_para_comunicaciones_administrativas": {
        "ID": "GN-GCOM-SEC-0057",
        "Title": "Anexo: Guía de Estilo y Formato para Comunicaciones Administrativas",
        "Content": "\nID: GNC-COM-ANEXO-FORMATOS-01\nPurp: Servir como guía de referencia rápida, estableciendo una taxonomía clara para el agente de IA, y detallando la estructura y estilo de los documentos administrativos más comunes.",
        "Sections": {
          "s_1_principios_generales_de_estilo_y_voz_institucional": {
            "ID": "GN-GCOM-SEC-0058",
            "Title": "1. Principios Generales de Estilo y Voz Institucional",
            "Content": "\nID: GNC-GORENUBLE-ESTILO-VOZ-01\nPurp: Establecer el marco conceptual y los principios rectores que definen la identidad comunicacional del Gobierno Regional de Ñuble en sus actos y comunicaciones administrativas, asegurando consistencia, claridad y cumplimiento normativo.",
            "Sections": {
              "s_1_1_mision_comunicacional": {
                "ID": "GN-GCOM-SEC-0059",
                "Title": "1.1. Misión Comunicacional",
                "Content": "\nID: GNC-GORENUBLE-ESTILO-MISION-01\nPurp: Ejercer la autoridad pública y comunicar las decisiones administrativas del Gobierno Regional de Ñuble con la máxima claridad, precisión, transparencia y un enfoque centrado en el ciudadano.\nObj: Garantizar que todo acto administrativo, independientemente de su formalidad, sea comprensible, esté debidamente fundamentado en la normativa vigente y refleje los valores de una administración pública moderna, eficiente y al servicio de la comunidad de la Región de Ñuble.\nFnd: Ley N° 19.880, que Establece Bases de los Procedimientos Administrativos que Rigen los Actos de los Órganos de la Administración del Estado.\nFnd: Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado."
              },
              "s_1_2_tono_de_voz_institucional": {
                "ID": "GN-GCOM-SEC-0060",
                "Title": "1.2. Tono de Voz Institucional",
                "Content": "\nID: GNC-GORENUBLE-ESTILO-TONO-01\nPurp: Definir los tonos de voz aplicables a las comunicaciones administrativas para asegurar la coherencia y adecuación al contexto de cada documento.\n\n- Cpt: Tono-Principal.\n  - Def: Formal, resolutivo e imparcial.\n  - Ctx: Tono por defecto para todos los actos administrativos formales. Refleja la autoridad, seriedad y objetividad del GORE como órgano del Estado. Se aplica de manera estricta en las partes dispositivas (RESUELVO:) de las resoluciones.\n- Cpt: Tono-Secundario.\n  - Def: Claro y didáctico.\n  - Ctx: Este tono no implica informalidad, sino la obligación de explicar las razones de una decisión de manera que un ciudadano informado pueda comprenderlas. Se aplica preferentemente en las secciones de fundamentación (CONSIDERANDO:) de las resoluciones y en el cuerpo de los oficios informativos. Su objetivo es maximizar la transparencia y la comprensión.\n- Cpt: Tono-Funcional.\n  - Def: Directo y conciso.\n  - Ctx: Aplicable exclusivamente a comunicaciones internas, como los memorándums. El foco es la eficiencia operativa, la claridad de la instrucción y la agilidad.\n- Cpt: Tono-Inclusivo.\n  - Req: Utilizar un lenguaje no sexista en todas las comunicaciones.\n  - Mech: Se debe priorizar el uso de sustantivos genéricos o colectivos (ej. \"el personal\", \"la ciudadanía\", \"el funcionariado\", \"la contraparte\").\n  - Prohib: Evitar el uso de desdoblamientos de género (ej. \"los y las funcionarios/as\") y el uso de caracteres como \"@\" o \"x\", ya que dificultan la lectura y el procesamiento automático."
              },
              "s_1_3_principios_rectores_de_redaccion": {
                "ID": "GN-GCOM-SEC-0061",
                "Title": "1.3. Principios Rectores de Redacción",
                "Content": "\nID: GNC-GORENUBLE-ESTILO-PRINCIPIOS-01\nPurp: Establecer las reglas no negociables que deben regir la redacción de toda comunicación administrativa del GORE Ñuble.\n\n- Cpt: Principio-1-Claridad-y-Precisión.\n  - Req: Evitar ambigüedades, jerga técnica innecesaria, y acrónimos sin definir en su primera aparición. El lenguaje debe ser directo y sin adornos retóricos.\n  - Fnd: Principio de Lenguaje Claro, orientado a facilitar la comprensión por parte de la ciudadanía y otros organismos.\n- Cpt: Principio-2-Corrección-Idiomática.\n  - Req: Adhesión estricta a las normas gramaticales y ortográficas de la Real Academia Española (RAE).\n  - Prohib: Uso de anglicismos o extranjerismos si existe un equivalente asentado en español (ej. \"correo electrónico\" en lugar de \"e-mail\"; \"reunión\" en lugar de \"meeting\").\n- Cpt: Principio-3-Legalidad-y-Fundamentación.\n  - Req: Todo acto administrativo que cree, modifique o extinga derechos u obligaciones debe citar explícitamente su fundamento normativo en la sección VISTOS:.\n  - Fnd: Principio de Legalidad (Art. 2, Ley N° 18.575) y Deber de Motivación de los actos administrativos (Art. 41, Ley N° 19.880).\n- Cpt: Principio-4-Enfoque-Ciudadano.\n  - Req: La justificación de los actos (CONSIDERANDO:) debe, siempre que sea pertinente, anclar la decisión en el beneficio público, el impacto territorial en la Región de Ñuble y los objetivos de la Estrategia Regional de Desarrollo."
              }
            }
          },
          "s_2_guia_de_formatos_de_documentos_administrativos": {
            "ID": "GN-GCOM-SEC-0062",
            "Title": "2. Guía de Formatos de Documentos Administrativos",
            "Content": "\nID: GNC-GORENUBLE-FORMATOS-01\nPurp: Servir como contenedor principal y punto de referencia para las guías de formato de cada tipo de documento, estableciendo una taxonomía clara.\nObj: Permitir identificar el tipo de documento correcto a generar en función del propósito y la audiencia de la comunicación solicitada.",
            "Sections": {
              "s_2_1_taxonomia_de_documentos_administrativos": {
                "ID": "GN-GCOM-SEC-0063",
                "Title": "2.1. Taxonomía de Documentos Administrativos",
                "Content": "\nID: GNC-GORENUBLE-FORMATOS-TAXONOMIA-01\nCpt: La selección del formato de documento no es arbitraria; responde a una función jurídica y administrativa específica. La siguiente tabla establece un mapa decisional, vinculando el propósito de la comunicación con el artefacto documental correspondiente.\n\n| Documento | Propósito Principal | Audiencia Típica | Nivel de Formalidad | Fundamento Normativo Primario |\n|-|-|-|-|-|\n| Resolución Exenta | Expresar una decisión formal de la autoridad; crear, modificar o extinguir derechos y obligaciones; aprobar actos o contratos. | Ciudadanía, otras entidades públicas, entidades privadas, personal interno. | Muy Alto | Ley N° 19.880, Art. 3 |\n| Oficio | Comunicar formalmente entre órganos de la Administración del Estado o con entidades externas. Solicitar o remitir información, transcribir resoluciones, formular consultas. | Otros servicios públicos, autoridades (nacionales, regionales, locales), entidades privadas, organismos internacionales. | Alto | D.S. N° 291 de 1974, Ministerio del Interior. |\n| Memorándum | Comunicar internamente instrucciones, solicitudes, información o decisiones de carácter operativo. | Funcionarios y unidades internas del GORE Ñuble (Gobernador/a, Jefes de División, Jefes de Departamento, etc.). | Medio-Alto (Formalidad Interna) | Costumbre administrativa y normativa interna. |"
              }
            }
          },
          "s_3_la_resolucion_exenta": {
            "ID": "GN-GCOM-SEC-0064",
            "Title": "3. La Resolución Exenta",
            "Content": "\nID: GNC-GORENUBLE-FORMATO-RESOLUCION-01\nPurp: Establecer la definición, estructura canónica, estilo y ejemplo de una Resolución Exenta para su correcta generación.",
            "Sections": {
              "s_3_1_definicion_y_contexto_juridico": {
                "ID": "GN-GCOM-SEC-0065",
                "Title": "3.1. Definición y Contexto Jurídico",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-RESOLUCION-DEF-01\nDef: Acto administrativo terminal, formal y escrito, que contiene una declaración de voluntad de la autoridad competente (Gobernador/a Regional), destinada a producir efectos jurídicos sobre un caso particular o general.\nNat: Corresponde a la forma que toma un acto administrativo según el Artículo 3 de la Ley N° 19.880.\nCtx: Exenta.\n\n- Def: Calificativo que indica que la resolución se encuentra exenta del trámite de Toma de Razón por parte de la Contraloría General de la República (CGR), de acuerdo con las resoluciones de la propia CGR que fijan las materias y montos exentos de dicho control previo.\n- Warn: La exención de la Toma de Razón no implica que el acto esté exento de un control de legalidad posterior por parte de la CGR o de los tribunales de justicia. El acto debe igualmente cumplir con todo el ordenamiento jurídico."
              },
              "s_3_2_estructura_canonica": {
                "ID": "GN-GCOM-SEC-0066",
                "Title": "3.2. Estructura Canónica",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-RESOLUCION-ESTRUCTURA-01\nPurp: Detallar la estructura obligatoria de una Resolución Exenta, explicando el propósito lógico de cada componente.\nFnd: La estructura VISTOS / CONSIDERANDO / RESUELVO no es una mera convención estilística, sino que refleja el proceso de razonamiento lógico-jurídico que fundamenta toda decisión administrativa.\n\n| Componente | Propósito Lógico | Contenido Clave y Directrices de Redacción |\n|-|-|-|\n| Encabezado | Identificación y Trazabilidad | - Título en mayúsculas: RESOLUCIÓN EXENTA N° [Número Correlativo]. - Lugar y fecha de dictación: CHILLÁN, [día] de [mes] de [año]. - El número es asignado por la unidad de Gestión Documental al momento de su despacho. |\n| VISTOS: | INPUT / Fundamento Normativo y Fáctico | - Sección que enumera, sin describir, todos los antecedentes que sirven de base a la decisión. - Req: Inicia con la palabra \"VISTOS:\" en mayúsculas y seguida de dos puntos. - Req: Cada antecedente se separa por punto y coma (;). - Req: Se deben citar: la potestad legal para actuar (ej. \"Lo dispuesto en la Ley N° 19.175...\"), los cuerpos normativos aplicables (leyes, decretos, resoluciones), y los documentos específicos del caso (oficios, informes, solicitudes). - Req: Se redacta en tercera persona, usando participios (ej. \"Visto el Oficio...\", \"Lo dispuesto en...\"). |\n| CONSIDERANDO: | PROCESO / Justificación y Motivación | - Sección que expone los razonamientos de hecho y de derecho que conectan los antecedentes (VISTOS) con la decisión final (RESUELVO). - Req: Inicia con la palabra \"CONSIDERANDO:\" en mayúsculas y seguida de dos puntos. - Req: Se estructura en párrafos numerados, cada uno desarrollando una idea o argumento. - Req: Debe cumplir con el deber de motivación del acto administrativo (Art. 41, Ley 19.880). Explica el porqué de la decisión. - Req: Se redacta en tercera persona, usando gerundios o frases introductorias (ej. \"1.- Que, siendo necesario...\", \"2.- Que, de acuerdo al informe técnico...\"). |\n| RESUELVO: | OUTPUT / Decisión o Mandato | - Parte dispositiva y central del acto. Contiene la decisión de la autoridad. - Req: Inicia con la palabra \"RESUELVO:\" en mayúsculas y seguida de dos puntos. - Req: Se estructura en artículos numerados, cada uno estableciendo una orden, aprobación o mandato de forma clara, imperativa e inequívoca. - Req: Se redacta utilizando verbos en modo imperativo o en presente indicativo con fuerza de mandato (ej. \"1.- Apruébase el convenio...\", \"2.- Modifícase la resolución...\", \"3.- Instrúyese a la División...\"). |\n| Cierre y Firma | Formalización y Autorización | - Req: Incluye la fórmula de cierre en mayúsculas: ANÓTESE, COMUNÍQUESE Y ARCHÍVESE. - Req: A continuación, la firma (manuscrita o electrónica avanzada) de la autoridad. - Req: Debajo de la firma, el nombre completo en mayúsculas y el cargo: \\`\\` GOBERNADOR/A REGIONAL REGIÓN DE ÑUBLE. |\n| Distribución | Comunicación y Archivo | - Req: Al final del documento, se lista a quiénes debe ser distribuida la resolución para su conocimiento y ejecución. - Ex: Distribución: - [Unidad Interna 1] - [Unidad Interna 2] - [Entidad Externa] - Oficina de Partes - Archivo |"
              },
              "s_3_3_lineamientos_de_redaccion_y_estilo": {
                "ID": "GN-GCOM-SEC-0067",
                "Title": "3.3. Lineamientos de Redacción y Estilo",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-RESOLUCION-ESTILO-01\n\n- Cpt: Tono.\n  - Req: Impersonal, formal, objetivo y autoritativo. El documento habla por la institución, no por el individuo que firma.\n- Cpt: Verbos-Clave.\n  - Req: La selección del tiempo y modo verbal es crucial y depende de la sección.\n  - Ctx: VISTOS: Utiliza participios pasados y frases nominales. Ex: \"Visto el informe...\", \"Lo dispuesto en la ley...\".\n  - Ctx: CONSIDERANDO: Utiliza gerundios o la conjunción \"Que\". Ex: \"Considerando que es necesario...\", \"Que, el informe técnico señala...\".\n  - Ctx: RESUELVO: Utiliza verbos en presente de indicativo con valor imperativo o directamente en imperativo. Ex: \"Apruébase...\", \"Modifícase...\", \"Déjase sin efecto...\".\n- Cpt: Referencias-Normativas.\n  - Req: Toda referencia a una ley, decreto o resolución debe incluir su número completo y año de dictación. Si es relevante, se puede incluir el ministerio de origen. Ex: \"Ley N° 19.880\", \"Decreto Supremo N° 250, de 2004, del Ministerio de Hacienda\".\n- Cpt: Numeración.\n  - Req: Los párrafos en CONSIDERANDO: y los artículos en RESUELVO: deben estar siempre numerados con números arábigos seguidos de un punto y un guion (ej. 1.-, 2.-)."
              },
              "s_3_4_ejemplo_de_aplicacion_sts": {
                "ID": "GN-GCOM-SEC-0068",
                "Title": "3.4. Ejemplo de Aplicación (STS)",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-RESOLUCION-EJEMPLO-STS-01\nPurp: Presentar un ejemplo completo de una Resolución Exenta refactorizada a formato STS.\nCpt: Escenario.\n\n- Def: Aprobación de un convenio de transferencia de recursos a una municipalidad para la ejecución de un proyecto FRIL (Fondo Regional de Iniciativa Local).\n\nCpt: Transcripción-STS.\n\n```sts\n# Resolución Exenta N° 4587\n\nID: GORENUBLE-REX-4587-20250710-01\nNat: Acto Administrativo.\nCpt: Tipo - Resolución Exenta.\nDln: Fecha-Dictacion - 2025-07-10.\nCtx: Lugar - Chillán."
              }
            }
          }
        }
      },
      "vistos": {
        "ID": "GN-GCOM-SEC-0069",
        "Title": "VISTOS",
        "Content": "\nID: GORENUBLE-REX-4587-VISTOS-01\n\n- Cpt: Marco-Legal-General.\n  - Fnd: Constitución Política de la República.\n  - Fnd: D.F.L. N° 1-19.175, LOC sobre Gobierno y Administración Regional.\n  - Fnd: Ley N° 19.880, Bases de los Procedimientos Administrativos.\n- Cpt: Marco-Presupuestario.\n  - Fnd: Ley N° 21.722, Ley de Presupuestos del Sector Público para el año 2025.\n  - Ctx: Partida 31, Capítulo 02, Programa 02.\n  - Fnd: Glosa 12, Partida 31, Ley N° 21.722.\n- Cpt: Actos-Habilitantes.\n  - Fnd: Certificado de Acuerdo N° 123-2025, Consejo Regional de Ñuble.\n  - Fnd: Oficio Ordinario N° 345, I. Municipalidad de San Carlos, 15-JUN-2025.\n  - Ctx: Solicitud de financiamiento para proyecto \"Mejoramiento Plaza de Armas de San Carlos\", código BIP 40012345-0.\n- Cpt: Potestad-Autoridad.\n  - Fnd: Artículo 24 letra o), Ley N° 19.175."
      },
      "considerando": {
        "ID": "GN-GCOM-SEC-0070",
        "Title": "CONSIDERANDO",
        "Content": "\nID: GORENUBLE-REX-4587-CONSIDERANDO-01\n\n- Cpt: Párrafo-1.\n  - Cause: Es función del Gobierno Regional promover el desarrollo social, cultural y económico de la región.\n  - Act: Resolver la inversión de los recursos que le corresponden.\n- Cpt: Párrafo-2.\n  - Act: La Municipalidad de San Carlos ha presentado un proyecto de inversión para el mejoramiento de su Plaza de Armas.\n  - Cond: Proyecto cuenta con recomendación técnica favorable (RS) de la Secretaría Comunal de Planificación.\n- Cpt: Párrafo-3.\n  - Ctx: El proyecto se enmarca en los objetivos de la Estrategia Regional de Desarrollo de Ñuble.\n  - Obj: Eje de mejoramiento de espacios públicos y calidad de vida urbana.\n- Cpt: Párrafo-4.\n  - Act: El Consejo Regional de Ñuble aprobó la asignación de recursos para el proyecto.\n  - Ctx: Sesión ordinaria N° 35, 05-JUL-2025.\n  - Fnd: Certificado de Acuerdo N° 123-2025.\n  - Ctx: Financiamiento con cargo al Fondo Regional de Iniciativa Local (FRIL).\n- Cpt: Párrafo-5.\n  - Cond: Existe disponibilidad presupuestaria.\n  - Ctx: Subtítulo 33, Ítem 03, Asignación 123, Presupuesto GORE Ñuble 2025."
      },
      "resuelvo": {
        "ID": "GN-GCOM-SEC-0071",
        "Title": "RESUELVO",
        "Content": "\nID: GORENUBLE-REX-4587-RESUELVO-01\n\n- Cpt: Artículo-1.\n  - Act: APRUÉBASE el Convenio de Transferencia de Recursos.\n  - Cpt: Partes - Gobierno Regional de Ñuble, Ilustre Municipalidad de San Carlos.\n  - Obj: Ejecución del proyecto \"Mejoramiento Plaza de Armas de San Carlos\", código BIP 40012345-0.\n- Cpt: Artículo-2.\n  - Act: TRANSFIÉRASE a la Ilustre Municipalidad de San Carlos.\n  - Cpt: Monto-Numérico - 150000000.\n  - Cpt: Monto-Texto - ciento cincuenta millones de pesos.\n  - Cpt: Moneda - CLP.\n  - Src: Presupuesto de inversión GORE Ñuble, Subtítulo 33, Ítem 03, Asignación 123, Glosa 12 \"Provisión Fondo Regional de Iniciativa Local\".\n- Cpt: Artículo-3.\n  - Act: ESTABLÉCESE la obligación de la Municipalidad de San Carlos de rendir cuenta de la inversión.\n  - Fnd: Resolución N° 30 de 2015, Contraloría General de la República.\n  - Fnd: Cláusulas del convenio respectivo.\n- Cpt: Artículo-4.\n  - Act: IMPÚTESE el gasto al presupuesto del Gobierno Regional de Ñuble para el año 2025."
      },
      "cierre": {
        "ID": "GN-GCOM-SEC-0072",
        "Title": "CIERRE",
        "Content": "\nID: GORENUBLE-REX-4587-CIERRE-01\n\n- Instr: ANÓTESE, COMUNÍQUESE Y ARCHÍVESE.\n- Cpt: Firma.\n  - Resp: JUAN PÉREZ GONZÁLEZ\n  - Cpt: Cargo - GOBERNADOR REGIONAL\n  - Cpt: Entidad - REGIÓN DE ÑUBLE\n- Cpt: Distribución.\n  - Dest: I. Municipalidad de San Carlos\n  - Dest: División de Presupuesto e Inversión Regional\n  - Dest: División de Administración y Finanzas\n  - Dest: Oficina de Partes\n  - Dest: Archivo\n```",
        "Sections": {
          "s_3_5_como_deberia_ser_la_salida_para_el_humano": {
            "ID": "GN-GCOM-SEC-0073",
            "Title": "3.5. Como debería ser la salida para el humano",
            "Content": "\n```plaintext\nRESOLUCIÓN EXENTA N° 4587\n\nCHILLÁN, 10 de julio de 2025\n\nVISTOS: Lo dispuesto en la Constitución Política de la República; el D.F.L. N° 1-19.175, que fija el texto refundido, coordinado, sistematizado y actualizado de la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional; la Ley N° 19.880, que establece Bases de los Procedimientos Administrativos; la Ley N° 21.722 de Presupuestos del Sector Público para el año 2025, Partida 31, Capítulo 02, Programa 02; la Glosa 12 asociada a dicha partida; el Certificado de Acuerdo N° 123-2025 del Consejo Regional de Ñuble; el Oficio Ordinario N° 345 de la Municipalidad de San Carlos, de fecha 15 de junio de 2025, que solicita financiamiento para el proyecto \"Mejoramiento Plaza de Armas de San Carlos\", código BIP 40012345-0; y la facultad que me confiere el artículo 24 letra o) de la citada Ley N° 19.175.\n\nCONSIDERANDO:\n\n1.- Que, es función del Gobierno Regional promover el desarrollo social, cultural y económico de la región, resolviendo la inversión de los recursos que le corresponden.  \n2.- Que, la Municipalidad de San Carlos ha presentado un proyecto de inversión para el mejoramiento de su Plaza de Armas, el cual cuenta con recomendación técnica favorable (RS) de la Secretaría Comunal de Planificación.  \n3.- Que, el referido proyecto se enmarca en los objetivos de la Estrategia Regional de Desarrollo de Ñuble, en su eje de mejoramiento de espacios públicos y calidad de vida urbana.  \n4.- Que, el Consejo Regional de Ñuble, en su sesión ordinaria N° 35, de fecha 05 de julio de 2025, según consta en el Certificado de Acuerdo N° 123-2025, aprobó la asignación de recursos para el financiamiento del mencionado proyecto con cargo al Fondo Regional de Iniciativa Local (FRIL).  \n5.- Que, existe disponibilidad presupuestaria en el subtítulo 33, ítem 03, asignación 123, del presupuesto del Gobierno Regional de Ñuble para el presente ejercicio.\n\nRESUELVO:\n\n1.- APRUÉBASE el Convenio de Transferencia de Recursos entre el Gobierno Regional de Ñuble y la Ilustre Municipalidad de San Carlos, para la ejecución del proyecto \"Mejoramiento Plaza de Armas de San Carlos\", código BIP 40012345-0.  \n2.- TRANSFIÉRASE a la Ilustre Municipalidad de San Carlos la suma de $150.000.000 (ciento cincuenta millones de pesos), con cargo al presupuesto de inversión del Gobierno Regional de Ñuble, Subtítulo 33, Ítem 03, Asignación 123, Glosa 12 \"Provisión Fondo Regional de Iniciativa Local\".  \n3.- ESTABLÉCESE que la Municipalidad de San Carlos deberá rendir cuenta de la inversión de los recursos transferidos, en conformidad con lo dispuesto en la Resolución N° 30 de 2015 de la Contraloría General de la República y las cláusulas del convenio respectivo.  \n4.- IMPÚTESE el gasto al presupuesto del Gobierno Regional de Ñuble para el año 2025.\n\nANÓTESE, COMUNÍQUESE Y ARCHÍVESE.\n\nJUAN PÉREZ GONZÁLEZ  \nGOBERNADOR REGIONAL  \nREGIÓN DE ÑUBLE\n\nDistribución:  \n- I. Municipalidad de San Carlos  \n- División de Presupuesto e Inversión Regional  \n- División de Administración y Finanzas  \n- Oficina de Partes  \n- Archivo\n```"
          },
          "s_4_el_oficio": {
            "ID": "GN-GCOM-SEC-0074",
            "Title": "4. El Oficio",
            "Content": "\nID: GNC-GORENUBLE-FORMATO-OFICIO-01\nPurp: Establecer la definición, estructura canónica, estilo y ejemplo de un Oficio.",
            "Sections": {
              "s_4_1_definicion_y_contexto_de_uso": {
                "ID": "GN-GCOM-SEC-0075",
                "Title": "4.1. Definición y Contexto de Uso",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-OFICIO-DEF-01\nDef: Documento oficial que sirve como vehículo para la comunicación formal y escrita entre distintas reparticiones de la Administración del Estado, y entre estas y entidades externas o particulares.\nPurp: Su propósito es variado y puede incluir solicitar o remitir información, impartir instrucciones a otros órganos, transcribir resoluciones, formular consultas, elevar antecedentes a una autoridad superior, entre otros.\nFnd: Su estructura y uso están normados principalmente por el Decreto Supremo N° 291, de 1974, del Ministerio del Interior, que fija normas para la elaboración de documentos oficiales."
              },
              "s_4_2_estructura_canonica": {
                "ID": "GN-GCOM-SEC-0076",
                "Title": "4.2. Estructura Canónica",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-OFICIO-ESTRUCTURA-01\nPurp: Detallar la estructura obligatoria de un Oficio, conforme a la normativa vigente.\n\n| Componente | Propósito | Contenido y Formato |\n|-|-|-|\n| Encabezado | Identificación Institucional | - Membrete oficial del GORE Ñuble en el margen superior izquierdo. |\n| Clasificación y Numeración | Identificación y Trazabilidad | - Margen superior derecho. - ORD. N° [Correlativo]/[Año]: Oficio Ordinario (comunicación de carácter público). - RES. N° [Correlativo]/[Año]: Oficio Reservado (conocimiento restringido a la unidad destinataria). - SEC. N° [Correlativo]/[Año]: Oficio Secreto (conocimiento restringido a la autoridad destinataria). |\n| ANT.: | Contextualización | - Abreviatura de \"Antecedentes\". - Enumera documentos previos que motivan o se relacionan con el oficio (ej. ANT.: Oficio ORD. N° 123, de fecha...). Si no hay, se omite. |\n| MAT.: | Asunto | - Abreviatura de \"Materia\". - Descripción muy breve y concisa del contenido del oficio (ej. MAT.: Remite informe de ejecución presupuestaria.). |\n| Lugar y Fecha | Datación | - Al centro, bajo la línea de MAT. - CHILLÁN, [día] de [mes] de [año]. |\n| DE: / A: | Remitente / Destinatario | - Margen izquierdo. - DE: GOBERNADOR/A REGIONAL, REGIÓN DE ÑUBLE. - A: [CARGO Y NOMBRE DESTINATARIO], [INSTITUCIÓN]. |\n| Cuerpo | Contenido Principal | - Párrafos numerados (1.-, 2.-, etc.). - Redacción clara, precisa y concisa. - Req: Cada oficio debe tratar una sola materia principal para facilitar su gestión y respuesta. |\n| Saludo de Cierre | Cortesía Formal | - Fórmula de despedida protocolar. La más común es Saluda atentamente a Ud., o Saluda atentamente a US., si el destinatario es una alta autoridad. |\n| Firma y Posfirma | Autorización | - Firma (manuscrita o electrónica avanzada). - Nombre completo en mayúsculas. - Cargo del firmante. |\n| Iniciales y Distribución | Trazabilidad Interna y Externa | - Margen inferior izquierdo. - Iniciales del firmante y transcriptor (ej. JPG/mfa). - Distribución: Lista de unidades o personas que reciben copia del documento. |"
              },
              "s_4_3_lineamientos_de_redaccion_y_estilo": {
                "ID": "GN-GCOM-SEC-0077",
                "Title": "4.3. Lineamientos de Redacción y Estilo",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-OFICIO-ESTILO-01\n\n- Cpt: Tono.\n  - Req: Formal, respetuoso, directo y objetivo. La comunicación es entre instituciones.\n- Cpt: Claridad-y-Concisión.\n  - Req: Ir directamente al punto. Los párrafos numerados deben facilitar la referencia y una eventual respuesta punto por punto.\n- Cpt: Estructura-Párrafo.\n  - Req: Cada párrafo numerado debe desarrollar una idea completa. El primer párrafo usualmente establece el propósito del oficio.\n- Cpt: Referencias.\n  - Req: Al referirse a otros documentos, se debe indicar su tipo, número y fecha."
              },
              "s_4_4_ejemplo_de_aplicacion_sts": {
                "ID": "GN-GCOM-SEC-0078",
                "Title": "4.4. Ejemplo de Aplicación (STS)",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-OFICIO-EJEMPLO-STS-01\nPurp: Presentar un ejemplo completo de un Oficio refactorizado a formato STS.\nCpt: Escenario.\n\n- Def: El Gobernador Regional solicita al SEREMI de Economía un informe detallado sobre el estado de avance de un programa financiado con fondos FNDR.\n\nCpt: Transcripción-STS.\n\n```sts\n# Oficio Ordinario N° 1250/2025\n\nID: GORENUBLE-OF-1250-20250710-01\nNat: Comunicación Oficial.\nCpt: Tipo - Oficio Ordinario.\nCpt: Clasificacion - Público."
              }
            }
          }
        }
      },
      "encabezado": {
        "ID": "GN-GCOM-SEC-0079",
        "Title": "ENCABEZADO",
        "Content": "\nID: GORENUBLE-OF-1250-ENCABEZADO-01\n\n- Cpt: Numero-Correlativo. Def: 1250/2025.\n- Cpt: Antecedente. Fnd: Convenio de Transferencia FNDR, Res. Ex. N° 3456 de 2024.\n- Cpt: Materia. Def: Solicita informe de avance de Programa \"Fomento Pyme Ñuble\".\n- Cpt: Lugar-Fecha. Def: CHILLÁN, 10 de julio de 2025."
      },
      "remitente_y_destinatario": {
        "ID": "GN-GCOM-SEC-0080",
        "Title": "REMITENTE Y DESTINATARIO",
        "Content": "\nID: GORENUBLE-OF-1250-PARTES-01\n\n- Cpt: Remitente.\n  - Cpt: Nombre - JUAN PÉREZ GONZÁLEZ.\n  - Cpt: Cargo - GOBERNADOR REGIONAL.\n  - Cpt: Entidad - REGIÓN DE ÑUBLE.\n- Cpt: Destinatario.\n  - Cpt: Nombre - SRA. MARÍA LUISA SOTO.\n  - Cpt: Cargo - SECRETARIA REGIONAL MINISTERIAL DE ECONOMÍA, FOMENTO Y TURISMO.\n  - Cpt: Entidad - REGIÓN DE ÑUBLE."
      },
      "cuerpo": {
        "ID": "GN-GCOM-SEC-0081",
        "Title": "CUERPO",
        "Content": "\nID: GORENUBLE-OF-1250-CUERPO-01\n\n- Cpt: Párrafo-1.\n  - Ctx: Saludo protocolar.\n  - Ctx: Referencia al programa \"Fomento Pyme Ñuble\".\n  - Fnd: Financiado por GORE Ñuble según ANT.\n  - Obj: Fortalecer capacidades de gestión de 200 Pymes de la región.\n- Cpt: Párrafo-2.\n  - Fnd: En virtud de facultades de supervisión del GORE.\n  - Act: Se solicita remitir informe detallado sobre estado de avance del programa.\n- Cpt: Párrafo-3.\n  - Req: Contenido mínimo del informe.\n  - Cpt: Requisito-a - Estado de ejecución presupuestaria desglosado por ítem.\n  - Cpt: Requisito-b - Avance en cumplimiento de indicadores y metas del convenio.\n  - Cpt: Requisito-c - Nómina de empresas beneficiarias a la fecha.\n  - Cpt: Requisito-d - Dificultades detectadas y medidas correctivas adoptadas.\n- Cpt: Párrafo-4.\n  - Req: Remitir información solicitada.\n  - Dln: Plazo máximo - 31 de julio de 2025.\n  - Purp: Información será presentada al Consejo Regional."
      },
      "cierre_2": {
        "ID": "GN-GCOM-SEC-0082",
        "Title": "CIERRE",
        "Content": "\nID: GORENUBLE-OF-1250-CIERRE-01\n\n- Cpt: Saludo-Despedida. Def: Saluda atentamente a Ud.,\n- Cpt: Firma.\n  - Resp: JUAN PÉREZ GONZÁLEZ.\n  - Cpt: Cargo - GOBERNADOR REGIONAL.\n  - Cpt: Entidad - REGIÓN DE ÑUBLE.\n- Cpt: Trazabilidad-Interna.\n  - Cpt: Iniciales - JPG/mfa.\n  - Cpt: Distribución.\n    - Dest: División de Fomento e Industria\n    - Dest: División de Presupuesto e Inversión Regional\n    - Dest: Oficina de Partes\n    - Dest: Archivo\n```",
        "Sections": {
          "s_4_5_como_deberia_ser_la_salida_para_el_humano": {
            "ID": "GN-GCOM-SEC-0083",
            "Title": "4.5. Como debería ser la salida para el humano",
            "Content": "\n```plaintext\nORD. N° 1250/2025\n\nANT.: Convenio de Transferencia FNDR, Res. Ex. N° 3456 de 2024.\nMAT.: Solicita informe de avance de Programa \"Fomento Pyme Ñuble\".\n\nCHILLÁN, 10 de julio de 2025\n\nDE: JUAN PÉREZ GONZÁLEZ\n    GOBERNADOR REGIONAL\n    REGIÓN DE ÑUBLE\n\nA:  SRA. MARÍA LUISA SOTO\n    SECRETARIA REGIONAL MINISTERIAL DE ECONOMÍA, FOMENTO Y TURISMO\n    REGIÓN DE ÑUBLE\n\n1.- Junto con saludar, me dirijo a Ud. en relación al programa \"Fomento Pyme Ñuble\", financiado por este Gobierno Regional mediante los recursos individualizados en el antecedente, cuyo objetivo es fortalecer las capacidades de gestión de 200 pequeñas y medianas empresas de la región.\n\n2.- Al respecto, y en virtud de las facultades de supervisión que competen a este Gobierno Regional, se solicita a Ud. tener a bien remitir un informe detallado sobre el estado de avance del mencionado programa a la fecha.\n\n3.- Dicho informe deberá contener, a lo menos, los siguientes elementos:\n    a) Estado de ejecución presupuestaria, desglosado por ítem de gasto.\n    b) Avance en el cumplimiento de los indicadores y metas comprometidos en el convenio.\n    c) Nómina de empresas beneficiarias a la fecha.\n    d) Dificultades detectadas en la ejecución y medidas correctivas adoptadas.\n\n4.- Se agradece remitir la información solicitada a más tardar el día 31 de julio del presente año, a fin de ser presentada ante el Consejo Regional.\n\nSaluda atentamente a Ud.,\n\n[Firma]\nJUAN PÉREZ GONZÁLEZ\nGOBERNADOR REGIONAL\nREGIÓN DE ÑUBLE\n\nJPG/mfa\nDistribución:\n- División de Fomento e Industria\n- División de Presupuesto e Inversión Regional\n- Oficina de Partes\n- Archivo\n```"
          },
          "s_5_el_memorandum": {
            "ID": "GN-GCOM-SEC-0084",
            "Title": "5. El Memorándum",
            "Content": "\nID: GNC-GORENUBLE-FORMATO-MEMO-01\nPurp: Establecer la definición, estructura canónica, estilo y ejemplo de un Memorándum.",
            "Sections": {
              "s_5_1_definicion_y_contexto_de_uso": {
                "ID": "GN-GCOM-SEC-0085",
                "Title": "5.1. Definición y Contexto de Uso",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-MEMO-DEF-01\nDef: Documento de comunicación interna, de carácter breve y funcional, utilizado para transmitir información, instrucciones o solicitudes entre las distintas unidades y funcionarios del Gobierno Regional.\nFnd: A diferencia de la Resolución y el Oficio, el Memorándum no posee una estructura rígidamente definida en la legislación nacional. Su formato se basa en la costumbre administrativa y en las normas internas de cada servicio.\nPurp: Su objetivo principal es la agilidad y la eficiencia en la gestión operativa interna. Se utiliza para impartir instrucciones, solicitar informes, comunicar decisiones de rutina, coordinar acciones, entre otros.\nNat: Es menos formal que un Oficio y está orientado exclusivamente a la comunicación dentro del GORE Ñuble."
              },
              "s_5_2_estructura_canonica": {
                "ID": "GN-GCOM-SEC-0086",
                "Title": "5.2. Estructura Canónica",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-MEMO-ESTRUCTURA-01\nPurp: Estandarizar el formato del Memorándum para el GORE Ñuble.\nReq: La siguiente estructura es la norma oficial para todos los memorándums generados en el GORE Ñuble.\n\n| Componente | Propósito | Contenido y Formato |\n|-|-|-|\n| Encabezado | Identificación del Documento | - Título en mayúsculas: MEMORÁNDUM. - Número correlativo: N° [Correlativo]/[Año]. |\n| Metadatos de Ruta | Direccionamiento y Contexto | - DE: Nombre y cargo del remitente. - PARA: Nombre y cargo del destinatario. - FECHA: Fecha de emisión del documento. - MATERIA: o ASUNTO: Descripción breve y directa del contenido. |\n| Cuerpo | Contenido Principal | - Mensaje directo, claro y conciso. - Se puede estructurar en párrafos o usar viñetas para listar instrucciones o puntos específicos. - No requiere la formalidad de los párrafos numerados del Oficio. |\n| Cierre | Autorización | - Saludo de despedida breve (ej. \"Atentamente,\"). - Firma del remitente. - Nombre y cargo del remitente. |"
              },
              "s_5_3_lineamientos_de_redaccion_y_estilo": {
                "ID": "GN-GCOM-SEC-0087",
                "Title": "5.3. Lineamientos de Redacción y Estilo",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-MEMO-ESTILO-01\n\n- Cpt: Tono.\n  - Req: Profesional pero directo. Es más funcional y menos protocolar que el Oficio. Se enfoca en la acción y la claridad.\n- Cpt: Brevedad.\n  - Req: El mensaje debe ser lo más breve posible y centrarse en un único tema para máxima eficiencia. Si el tema es complejo, es preferible adjuntar un informe y usar el memo como conductor.\n- Cpt: Claridad.\n  - Req: La solicitud, instrucción o información debe ser inequívoca para evitar malas interpretaciones y re-consultas."
              },
              "s_5_4_ejemplo_de_aplicacion_sts": {
                "ID": "GN-GCOM-SEC-0088",
                "Title": "5.4. Ejemplo de Aplicación (STS)",
                "Content": "\nID: GNC-GORENUBLE-FORMATO-MEMO-EJEMPLO-STS-01\nPurp: Presentar un ejemplo completo de un Memorándum refactorizado a formato STS.\nCpt: Escenario.\n\n- Def: El Jefe de la División de Administración y Finanzas (DAF) instruye al Jefe del Departamento de Recursos Humanos preparar un informe sobre ausentismo laboral.\n\nCpt: Transcripción-STS.\n\n```sts\n# Memorándum N° 550/2025\n\nID: GORENUBLE-MEMO-550-20250710-01\nNat: Comunicación Interna.\nCpt: Tipo - Memorándum."
              }
            }
          }
        }
      },
      "metadatos": {
        "ID": "GN-GCOM-SEC-0089",
        "Title": "METADATOS",
        "Content": "\nID: GORENUBLE-MEMO-550-METADATOS-01\n\n- Cpt: Remitente.\n  - Cpt: Nombre - ANA CASTRO ROJAS.\n  - Cpt: Cargo - JEFA DIVISIÓN DE ADMINISTRACIÓN Y FINANZAS.\n- Cpt: Destinatario.\n  - Cpt: Nombre - CARLOS LÓPEZ SOTO.\n  - Cpt: Cargo - JEFE DEPARTAMENTO DE RECURSOS HUMANOS.\n- Cpt: Fecha. Def: 10 de julio de 2025.\n- Cpt: Materia. Def: Solicita informe de ausentismo laboral primer semestre 2025."
      },
      "cuerpo_2": {
        "ID": "GN-GCOM-SEC-0090",
        "Title": "CUERPO",
        "Content": "\nID: GORENUBLE-MEMO-550-CUERPO-01\n\n- Cpt: Saludo. Def: Protocolar.\n- Cpt: Instrucción-Principal.\n  - Act: Preparar y remitir informe consolidado sobre ausentismo laboral del personal del GORE.\n  - Ctx: Período - 01-ENE-2025 al 30-JUN-2025.\n- Cpt: Requisitos-Informe.\n  - Req: Tasa de ausentismo general y por división.\n  - Req: Desglose de ausencias por tipo (licencia médica, permisos administrativos, otros).\n  - Req: Análisis comparativo con el mismo período del año 2024.\n- Cpt: Plazo.\n  - Dln: Fecha máxima de entrega - 25 de julio de 2025."
      },
      "cierre_3": {
        "ID": "GN-GCOM-SEC-0091",
        "Title": "CIERRE",
        "Content": "\nID: GORENUBLE-MEMO-550-CIERRE-01\n\n- Cpt: Despedida. Def: Atentamente,\n- Cpt: Firma.\n  - Resp: Ana Castro Rojas.\n  - Cpt: Cargo - Jefa DAF.\n```",
        "Sections": {
          "s_5_5_como_deberia_ser_la_salida_para_el_humano": {
            "ID": "GN-GCOM-SEC-0092",
            "Title": "5.5. Como debería ser la salida para el humano",
            "Content": "\n```plaintext\nMEMORÁNDUM N° 550/2025\n\nDE:      ANA CASTRO ROJAS\n         JEFA DIVISIÓN DE ADMINISTRACIÓN Y FINANZAS\n\nPARA:    CARLOS LÓPEZ SOTO\n         JEFE DEPARTAMENTO DE RECURSOS HUMANOS\n\nFECHA:   10 de julio de 2025\n\nMATERIA: Solicita informe de ausentismo laboral primer semestre 2025.\n\nJunto con saludar, le solicito preparar y remitir a esta Jefatura un informe consolidado sobre el ausentismo laboral del personal del Gobierno Regional, correspondiente al período comprendido entre el 1 de enero y el 30 de junio de 2025.\n\nEl informe deberá incluir, como mínimo:\n- Tasa de ausentismo general y por división.\n- Desglose de ausencias por tipo (licencia médica, permisos administrativos, otros).\n- Análisis comparativo con el mismo período del año anterior.\n\nAgradeceré disponer de dicho informe a más tardar el día 25 de julio del presente.\n\nAtentamente,\n\n[Firma]\nAna Castro Rojas\nJefa DAF\n```"
          },
          "s_6_tipologia_ampliada_de_documentos_oficiales": {
            "ID": "GN-GCOM-SEC-0093",
            "Title": "6. Tipología Ampliada de Documentos Oficiales",
            "Content": "\nID: GNC-COM-ANEXO-TIPOLOGIA-AMPLIADA-01\nPurp: Servir como guía de referencia rápida para la identificación y redacción de una gama más amplia de documentos administrativos comunes, complementando la taxonomía detallada.\n\n| Documento | Uso Principal | Autoridad Emisora | Características Formales | Enfoque Redacción/Asistencia |\n|-|-|-|-|-|\n| Cpt: Decreto | Purp: Establecer normas, actos administrativos obligatorios. | Resp: Presidente o Ministro. | Ctx: Vistos, considerandos, parte resolutiva. | Act: Estructurar considerandos con base en normativa y antecedentes; redactar parte resolutiva clara. |\n| Cpt: Decreto Exento | Purp: Igual, pero no requiere toma de razón de Contraloría. | Resp: Ministro o Jefe de Servicio. | Ctx: Misma estructura que decreto. | Act: Similar al decreto, enfatizando justificación de la exención. |\n| Cpt: Resolución | Purp: Disponer medidas administrativas internas o actos resolutorios. | Resp: Jefaturas superiores. | Ctx: Vistos, considerandos, parte resolutiva. | Act: Redactar para Gobernador u otros jefes de servicio, asegurando claridad en lo resuelto. |\n| Cpt: Oficio | Purp: Comunicación oficial entre autoridades o servicios. | Resp: Toda autoridad administrativa. | Ctx: Breve, directo, formal. Con Nº, fecha, destinatario, materia. | Act: Generar borradores concisos, precisos, con lenguaje formal interinstitucional. |\n| Cpt: Memorándum | Purp: Comunicación interna. | Resp: Funcionario con facultad. | Ctx: Breve, sin saludos. Con \"De:\", \"A:\", \"Materia:\", \"Fecha:\". | Act: Redactar comunicaciones internas claras para decisiones, solicitudes o coordinación. |\n| Cpt: Carta | Purp: Comunicación formal a entidades o personas externas. | Resp: Jefatura administrativa. | Ctx: Encabezado y despedida formal. | Act: Elaborar cartas formales, con tono respetuoso y profesional. |\n| Cpt: Certificado | Purp: Acreditar hechos o situaciones constatadas. | Resp: Jefatura o unidad competente. | Ctx: Preciso, objetivo, con respaldo documental. | Act: Redactar certificados basados en información verificable, asegurando exactitud. |\n| Cpt: Acta | Purp: Dejar constancia escrita de reuniones o decisiones. | Resp: Secretario o designado. | Ctx: Detalla fecha, asistentes, temas, acuerdos. | Act: Estructurar actas claras que reflejen fielmente lo discutido y acordado. |\n| Cpt: Circular | Purp: Instrucción interna sobre interpretación o aplicación de normas. | Resp: Jefatura administrativa. | Ctx: Redacción general, tono instructivo. | Act: Redactar borradores que expliquen procedimientos de manera clara y uniforme. |\n| Cpt: Informe | Purp: Exponer antecedentes, análisis o propuestas. | Resp: Técnico o profesional. | Ctx: Intro, desarrollo, conclusión, recomendaciones. | Act: Asistir en la estructuración y redacción, organizando la información de forma lógica. |\n| Cpt: Proposición | Purp: Documento base para resolver una materia (ej. adjudicación). | Resp: Unidad técnica o de asesoría. | Ctx: Acompaña resolución/decreto. Fundamenta la decisión. | Act: Articular fundamentos técnicos y legales para respaldar una decisión. |\n| Cpt: Minuta | Purp: Resumir información clave para autoridades o reuniones. | Resp: Técnicos, asesores, jefaturas. | Ctx: Concisa, estructurada (antecedentes, análisis, conclusiones). | Act: Sintetizar información relevante, estructurar puntos clave de manera lógica. |"
          }
        }
      }
    },
    "Content": "# Guía Integral de Comunicaciones GORE Ñuble\n\nID: KB-GN-030-GUIA-COMUNICACIONES-V2\nVersion: 2.0.0\nStatus: Published\nHuman-Creator: FS\nHuman-Editor: FS\nModel-Collaborator: IA-GEMINI\nCreation-Date: 2025-06-30\nModification-Date: 2025-07-10\nRef-STS-Guide: GUIDE-STS-MASTER-01"
  }
}
