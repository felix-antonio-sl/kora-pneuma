---
urn: urn:gn:kb:gn-indicadores-nuble
nombre: gn-indicadores-nuble
version: "1.0.0"
estado: borrador
descripcion: "Conocimiento GN heredado de KODA sobre gn-indicadores-nuble; migrado como borrador y no publicado."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-gore-os-remaining/migrated/domains/gn/02_estrategia/estadisticas/kb_gn_005_indicadores_nuble_koda.yml (sha256:64a14aa9bdbaee49cbefa94542dd034637268d08cf22086abaf66c1d27219c97); URN KODA legado urn:gorenuble:gn:indicadores-nuble:1.0.0; estado original Draft; cuerpo original completo preservado; migración KORA 2026-08-02."
autor: "FS"
creado: 2025-12-15
lang: es
tags: ["gn", "gore-os", "koda", "domains", "02-estrategia", "estadisticas", "indicadores", "nuble"]
familia: bok
---
{
  "_manifest": {
    "urn": "urn:gorenuble:gn:indicadores-nuble:1.0.0",
    "federation": {
      "visibility": "internal",
      "license": "Institutional Use"
    },
    "compatibility": {
      "min_consumer_version": "1.0.0",
      "breaking_changes_from": null
    },
    "resolution": {
      "canonical_url": "file://knowledge/domains/gn/estadisticas/kb_gn_005_indicadores_nuble_koda.yml",
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
  "ID": "GN-INDICADORES-NUBLE-01",
  "Version": "1.0.0",
  "Status": "Draft",
  "Format": "KODA/Spec",
  "Human-Creator": "FS",
  "Human-Editor": "FS",
  "Model-Collaborator": "IA-CASCADE",
  "AI-Remediator": "KODA-TRANSFORMER",
  "Creation-Date": "2025-12-15",
  "Modification-Date": "2025-12-15",
  "Ctx": "Indicadores regionales y comunales de la Región de Ñuble (Actualización BCN: Junio 2025).",
  "Primary-Source": "staging/gn/kodeando/kb_gn_005_indicadores_nuble.md",
  "LLM_Parsing_Instructions": {
    "ID": "KODA-LLM-PARSER-01",
    "Req": "Mandatory block following Metadata.",
    "Prohib": "Using for artifact creation or translation.",
    "Content": "BEGIN_LLM_INSTRUCTIONS\nYou are an AI agent consuming a KODA artifact. Parse with absolute fidelity.\n\nFIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).\n\nLEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, ID->ID, Just->Justification, Mssn->Mission, Obj->Objective, Proc->Process, Prohib->Prohibition, Purp->Purpose, Rec->Recommendation, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Warn->Warning, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference.\n\nREFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: external URN (optionally with #ID fragment) only.\nLANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.\nEND_LLM_INSTRUCTIONS"
  },
  "Indicadores_Nuble": {
    "ID": "GN-INDICADORES-NUBLE-DOC-01",
    "Title": "Indicadores regionales y comunales región de Ñuble",
    "Update": "Actualización BCN: Junio 2025",
    "Sections": {
      "indicadores_demograficos": {
        "ID": "GN-IND-SEC-0001",
        "Title": "Indicadores Demográficos",
        "Content": "",
        "Sections": {
          "poblacion_total_fuente_censo_de_poblacion_y_vivienda_2017_y_2024_ine": {
            "ID": "GN-IND-SEC-0002",
            "Title": "Población Total (Fuente: Censo de Población y Vivienda 2017 y 2024, INE)",
            "Content": "\n|Comuna|Censo 2017|Censo 2024|Variación (%)|\n|-|-|-|-|\n|Bulnes|21493|23863|11.0|\n|Chillán|184739|190382|3.1|\n|Chillán Viejo|30907|32688|5.8|\n|Cobquecura|5012|5495|9.6|\n|Coelemu|15995|15895|-0.6|\n|Coihueco|26881|29766|10.7|\n|El Carmen|12044|13186|9.5|\n|Ninhue|5213|5763|10.6|\n|Ñiquén|11152|12797|14.8|\n|Pemuco|8448|8930|5.7|\n|Pinto|10827|12502|15.5|\n|Portezuelo|4862|5203|7.0|\n|Quillón|17485|19165|9.6|\n|Quirihue|11594|11746|1.3|\n|Ránquil|5755|6508|13.1|\n|San Carlos|53024|55847|5.3|\n|San Fabián|4308|5245|21.8|\n|San Ignacio|16079|17405|8.2|\n|San Nicolás|11603|15099|30.1|\n|Treguaco|5401|6124|13.4|\n|Yungay|17787|18680|5.0|\n|Región de Ñuble|480609|512289|6.6|\n|País|17574003|18480432|5.2|"
          },
          "poblacion_por_area_urbana_rural_fuente_censo_de_poblacion_y_vivienda_2017_proyec": {
            "ID": "GN-IND-SEC-0003",
            "Title": "Población por Área Urbana-Rural (Fuente: Censo de Población y Vivienda 2017, Proyecciones de Población 2024, INE)",
            "Content": "\n|Comuna|Urbana (2017)|Rural (2017)|Urbana (2024)|Rural (2024)|% Ruralidad 2017|% Ruralidad 2024|\n|-|-|-|-|-|-|-|\n|Bulnes|13491|8002|14450|8304|37.2|36.5|\n|Chillán|168647|16092|186949|17142|8.7|8.4|\n|Chillán Viejo|27409|3498|32208|3372|11.3|9.5|\n|Cobquecura|1453|3559|1489|3735|71.0|71.5|\n|Coelemu|10142|6809|10287|6462|40.2|38.6|\n|Coihueco|9098|17783|10577|18490|66.2|63.6|\n|El Carmen|4861|7183|5141|7056|59.6|57.9|\n|Ninhue|1152|2964|1192|2945|72.0|71.2|\n|Ñiquén|2146|3100|2263|3107|59.1|57.8|\n|Pemuco|4168|4280|4344|4239|50.7|49.4|\n|Pinto|5458|5369|6341|5838|49.6|47.9|\n|Portezuelo|1804|3058|1892|2984|62.9|61.2|\n|Quillón|10423|7062|12436|6868|40.4|35.6|\n|Quirihue|3319|4527|3455|4736|57.7|57.8|\n|Ránquil|1374|2999|1329|2973|68.6|69.1|\n|San Carlos|38452|14738|40277|14585|27.7|26.6|\n|San Fabián|1694|2614|1762|3031|60.7|63.2|\n|San Ignacio|7514|8605|8127|8879|53.4|52.2|\n|San Nicolás|4887|6716|5542|6945|57.9|55.6|\n|Treguaco|2242|3322|2366|3279|59.7|58.1|\n|Yungay|13303|4484|14857|3978|25.2|21.1|\n|Región de Ñuble|333680|146929|372096|149615|30.6|28.7|\n|País|15424263|2149740|17824977|2261400|12.2|11.3|"
          },
          "poblacion_por_sexo_e_indice_de_masculinidad_fuente_censo_de_poblacion_y_vivienda": {
            "ID": "GN-IND-SEC-0004",
            "Title": "Población por Sexo e Índice de Masculinidad (Fuente: Censo de Población y Vivienda 2017 y 2024, INE)",
            "Content": "\n|Comuna|Hombres (2017)|Mujeres (2017)|Hombres (2024)|Mujeres (2024)|IM 2017|IM 2024|\n|-|-|-|-|-|-|-|\n|Bulnes|10382|11111|11472|12391|93.4|92.6|\n|Chillán|87521|97218|89482|100900|90.0|88.7|\n|Chillán Viejo|14581|16326|15486|17202|89.3|90.0|\n|Cobquecura|2525|2487|2693|2802|101.5|96.1|\n|Coelemu|7873|8122|7760|8135|96.9|95.4|\n|Coihueco|13424|13457|14681|15085|99.8|97.3|\n|El Carmen|5967|6077|6548|6638|98.2|98.6|\n|Ninhue|2567|2646|2831|2932|97.0|96.6|\n|Ñiquén|5616|5536|6416|6381|101.4|100.5|\n|Pemuco|4221|4227|4416|4514|99.9|97.8|\n|Pinto|5336|5491|6120|6382|97.2|95.9|\n|Portezuelo|2416|2446|2588|2615|98.8|99.0|\n|Quillón|8664|8821|9375|9790|98.2|95.8|\n|Quirihue|5679|5915|5685|6061|96.0|93.8|\n|Ránquil|2842|2913|3197|3311|97.6|96.6|\n|San Carlos|25425|27599|26745|29102|92.1|91.9|\n|San Fabián|2203|2105|2569|2676|104.7|96.0|\n|San Ignacio|7882|8197|8556|8849|96.2|96.7|\n|San Nicolás|5796|5807|7516|7583|99.8|99.1|\n|Treguaco|2703|2698|3069|3055|100.2|100.5|\n|Yungay|8964|8823|9232|9448|101.6|97.7|\n|Región de Ñuble|232587|248022|246437|265852|93.8|92.7|\n|País|8601989|8972014|8967033|9513399|95.9|94.3|"
          },
          "poblacion_por_grupos_de_edad_fuente_censo_de_poblacion_y_vivienda_2017_y_2024_in": {
            "ID": "GN-IND-SEC-0005",
            "Title": "Población por Grupos de Edad (Fuente: Censo de Población y Vivienda 2017 y 2024, INE)",
            "Content": "\n|Comuna|0 a 14 (2017)|0 a 14 (2024)|15 a 29 (2017)|15 a 29 (2024)|30 a 44 (2017)|30 a 44 (2024)|45 a 64 (2017)|45 a 64 (2024)|65 o más (2017)|65 o más (2024)|Total (2017)|Total (2024)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|4248|4139|4349|4357|4016|4656|5855|6598|3025|4113|21493|23863|\n|Chillán|36393|33121|41966|38278|37189|41623|46756|48544|22435|28816|184739|190382|\n|Chillán Viejo|6942|6012|7013|6931|6672|6975|7356|8635|2924|4135|30907|32688|\n|Cobquecura|740|738|742|804|1006|1109|1509|1553|1015|1291|5012|5495|\n|Coelemu|3191|2697|3095|2915|2954|3023|4399|4304|2356|2956|15995|15895|\n|Coihueco|5616|5492|5933|5949|5362|6071|6892|8021|3078|4233|26881|29766|\n|El Carmen|2276|2195|2276|2411|2340|2514|3242|3773|1910|2293|12044|13186|\n|Ninhue|863|843|893|947|925|1015|1545|1731|987|1227|5213|5763|\n|Ñiquén|2005|1976|1851|2070|1899|2197|3392|3773|2005|2781|11152|12797|\n|Pemuco|1657|1517|1752|1719|1634|1671|2230|2520|1175|1503|8448|8930|\n|Pinto|1964|2006|2172|2174|2035|2526|3052|3559|1604|2237|10827|12502|\n|Portezuelo|862|738|836|868|826|895|1493|1578|845|1124|4862|5203|\n|Quillón|3156|3012|3249|3173|3149|3635|4944|5292|2987|4053|17485|19165|\n|Quirihue|2184|1915|2113|2037|2294|2379|3163|3188|1840|2227|11594|11746|\n|Ránquil|1017|1049|900|964|1006|1138|1730|1873|1102|1484|5755|6508|\n|San Carlos|10358|9506|11008|10563|9838|11136|14275|15133|7545|9509|53024|55847|\n|San Fabián|799|950|841|841|843|1127|1088|1367|737|960|4308|5245|\n|San Ignacio|3031|2792|3152|3079|2942|3346|4574|5018|2380|3170|16079|17405|\n|San Nicolás|2155|2588|2238|2697|2202|2969|3316|4264|1692|2581|11603|15099|\n|Treguaco|983|945|940|1092|1002|1173|1594|1742|882|1172|5401|6124|\n|Yungay|3446|3065|3423|3247|3453|3707|4873|5292|2592|3369|17787|18680|\n|Región de Ñuble|93680|88193|96966|94042|91823|100108|118758|129647|63595|77722|480609|512289|\n|País|3094540|3265532|3611435|3880891|3686064|4213539|4260941|4532821|2921023|2587649|17574003|18480432|"
          },
          "indice_de_dependencia_demografica_idd_e_indice_de_adultos_mayores_iam_fuente_cen": {
            "ID": "GN-IND-SEC-0006",
            "Title": "Índice de Dependencia Demográfica (IDD) e Índice de Adultos Mayores (IAM) (Fuente: Censo de Población y Vivienda 2017 y 2024, INE)",
            "Content": "\n|Comuna|IDD 2017|IDD 2024|IAM 2017|IAM 2024|\n|-|-|-|-|-|\n|Bulnes|51.1|52.9|71.2|99.4|\n|Chillán|46.7|48.2|61.6|87.0|\n|Chillán Viejo|46.9|45.0|42.1|68.8|\n|Cobquecura|53.9|58.5|137.2|174.9|\n|Coelemu|53.1|55.2|73.8|109.6|\n|Coihueco|47.8|48.5|54.8|77.1|\n|El Carmen|53.3|51.6|83.9|104.5|\n|Ninhue|55.0|56.1|114.4|145.6|\n|Ñiquén|56.1|59.2|100.0|140.7|\n|Pemuco|50.4|51.1|70.9|99.1|\n|Pinto|49.2|51.4|81.7|111.5|\n|Portezuelo|54.1|55.7|98.0|152.3|\n|Quillón|54.2|58.4|94.6|134.6|\n|Quirihue|53.2|54.5|84.2|116.3|\n|Ránquil|58.3|63.7|108.4|141.5|\n|San Carlos|51.0|51.6|72.8|100.0|\n|San Fabián|55.4|57.3|92.2|101.1|\n|San Ignacio|50.7|52.1|78.5|113.5|\n|San Nicolás|49.6|52.1|78.5|99.7|\n|Treguaco|52.7|52.8|89.7|124.0|\n|Yungay|51.4|52.5|75.2|109.9|\n|Región de Ñuble|49.4|50.8|69.4|97.6|\n|País|45.9|46.5|56.9|79.0|"
          }
        }
      },
      "indice_de_desarrollo_humano_por_comuna": {
        "ID": "GN-IND-SEC-0007",
        "Title": "Indice de Desarrollo Humano por comuna",
        "Content": "\n|Comuna|Tramo IDH|IDH|Tasa de Años de Vida Potencialmente Perdidos|Educación|Ingreso|\n|-|-|-|-|-|-|\n|Chillán|medio-alto|0.646|0.746|0.824|0.439|\n|Chillán Viejo|medio-bajo|0.613|0.817|0.794|0.355|\n|Ñiquén|medio-bajo|0.582|0.842|0.708|0.331|\n|Ránquil|medio-bajo|0.578|0.854|0.737|0.307|\n|Yungay|medio-bajo|0.569|0.699|0.798|0.330|\n|Coelemu|medio-bajo|0.566|0.734|0.733|0.338|\n|Quirihue|medio-bajo|0.554|0.728|0.758|0.309|\n|San Carlos|bajo|0.549|0.707|0.729|0.320|\n|Bulnes|bajo|0.548|0.711|0.732|0.316|\n|San Nicolás|bajo|0.546|0.793|0.718|0.285|\n|Quillón|bajo|0.529|0.729|0.722|0.282|\n|Pinto|bajo|0.521|0.708|0.674|0.296|\n|Cobquecura|bajo|0.506|0.703|0.699|0.264|\n|San Fabián|bajo|0.503|0.795|0.713|0.224|\n|Pemuco|bajo|0.497|0.798|0.659|0.234|\n|Coihueco|bajo|0.496|0.746|0.697|0.235|\n|Treguaco|bajo|0.487|0.622|0.725|0.256|\n|El Carmen|bajo|0.472|0.733|0.684|0.210|\n|Portezuelo|bajo|0.444|0.621|0.705|0.200|\n|San Ignacio|bajo|0.437|0.667|0.690|0.181|"
      },
      "indicadores_sociales": {
        "ID": "GN-IND-SEC-0008",
        "Title": "Indicadores Sociales",
        "Content": "\nLos datos presentados a continuación, fueron extraídos de la Encuesta de Caracterización Socioeconómica Nacional (CASEN) 2017 y 2022 y Sistema Integrado de Información Social, instrumentos gestionados por el Ministerio de Desarrollo Social y Familia (MDSyF)",
        "Sections": {
          "tasa_de_pobreza_por_ingresos_fuente_encuesta_casen_2017_y_2022_mdsyf": {
            "ID": "GN-IND-SEC-0009",
            "Title": "Tasa de Pobreza por Ingresos (Fuente: Encuesta CASEN 2017 y 2022, MDSyF)",
            "Content": "\n|Comuna|CASEN 2017|CASEN 2022|\n|-|-|-|\n|Bulnes|14.9%|12.7%|\n|Chillán|11.7%|10.5%|\n|Chillán Viejo|19.1%|8.5%|\n|Cobquecura|34.2%|19.1%|\n|Coelemu|18.3%|13.0%|\n|Coihueco|22.0%|13.5%|\n|El Carmen|28.8%|14.9%|\n|Ninhue|25.3%|16.1%|\n|Ñiquén|19.9%|13.8%|\n|Pemuco|23.8%|19.0%|\n|Pinto|25.1%|10.3%|\n|Portezuelo|18.7%|15.1%|\n|Quillón|16.7%|16.0%|\n|Quirihue|18.3%|7.8%|\n|Ránquil|9.5%|16.8%|\n|San Carlos|13.8%|13.7%|\n|San Fabián|13.8%|15.0%|\n|San Ignacio|24.9%|15.7%|\n|San Nicolás|14.3%|10.8%|\n|Treguaco|20.6%|17.1%|\n|Yungay|19.4%|10.8%|\n|Región de Ñuble|16.2%|12.1%|\n|País|8.5%|6.5%|"
          },
          "tasa_de_pobreza_multidimensional_5_dimensiones_fuente_encuesta_casen_2017_y_2022": {
            "ID": "GN-IND-SEC-0010",
            "Title": "Tasa de Pobreza Multidimensional (5 dimensiones) (Fuente: Encuesta CASEN 2017 y 2022, MDSyF)",
            "Content": "\n|Comuna|CASEN 2017|CASEN 2022|\n|-|-|-|\n|Bulnes|28.7%|10.1%|\n|Chillán|17.7%|12.7%|\n|Chillán Viejo|24.0%|15.2%|\n|Cobquecura|47.2%|24.3%|\n|Coelemu|30.7%|18.4%|\n|Coihueco|27.3%|24.5%|\n|El Carmen|34.1%|19.0%|\n|Ninhue|34.8%|21.4%|\n|Ñiquén|30.8%|19.2%|\n|Pemuco|28.5%|20.1%|\n|Pinto|37.1%|22.5%|\n|Portezuelo|35.5%|20.8%|\n|Quillón|30.7%|12.0%|\n|Quirihue|35.3%|18.9%|\n|Ránquil|24.3%|15.5%|\n|San Carlos|27.5%|15.1%|\n|San Fabián|32.4%|15.0%|\n|San Ignacio|32.8%|21.6%|\n|San Nicolás|35.0%|19.7%|\n|Treguaco|23.7%|18.8%|\n|Yungay|19.9%|12.8%|\n|Región de Ñuble|24.7%|15.5%|\n|País|20.3%|16.9%|"
          },
          "porcentaje_de_personas_en_el_rsh_que_declaran_pertenecer_a_pueblos_indigenas_fue": {
            "ID": "GN-IND-SEC-0011",
            "Title": "Porcentaje de Personas en el RSH que Declaran Pertenecer a Pueblos Indígenas (Fuente: marzo 2025, SIIS-T MDSyF)",
            "Content": "\n|Comuna|Pueblos Indígenas (%)|\n|-|-|\n|Bulnes|2.3%|\n|Chillán|2.6%|\n|Chillán Viejo|3.8%|\n|Cobquecura|1.8%|\n|Coelemu|1.4%|\n|Coihueco|1.1%|\n|El Carmen|0.9%|\n|Ninhue|2.0%|\n|Ñiquén|1.8%|\n|Pemuco|1.3%|\n|Pinto|2.0%|\n|Portezuelo|1.4%|\n|Quillón|2.1%|\n|Quirihue|2.3%|\n|Ránquil|1.9%|\n|San Carlos|0.9%|\n|San Fabián|2.0%|\n|San Ignacio|1.6%|\n|San Nicolás|1.8%|\n|Treguaco|1.4%|\n|Yungay|2.0%|\n|Región de Ñuble|2.1%|\n|País|9.2%|"
          },
          "porcentaje_de_personas_en_el_rsh_que_son_extranjeros_as_fuente_marzo_2025_siis_t": {
            "ID": "GN-IND-SEC-0012",
            "Title": "Porcentaje de Personas en el RSH que son Extranjeros/as (Fuente: marzo 2025, SIIS-T MDSyF)",
            "Content": "\n|Comuna|Extranjeros (%)|\n|-|-|\n|Bulnes|0.7%|\n|Chillán|3.2%|\n|Chillán Viejo|1.5%|\n|Cobquecura|0.8%|\n|Coelemu|0.5%|\n|Coihueco|0.9%|\n|El Carmen|0.5%|\n|Ninhue|0.5%|\n|Ñiquén|0.6%|\n|Pemuco|0.2%|\n|Pinto|1.2%|\n|Portezuelo|0.4%|\n|Quillón|1.4%|\n|Quirihue|0.4%|\n|Ránquil|0.4%|\n|San Carlos|1.2%|\n|San Fabián|0.7%|\n|San Ignacio|0.4%|\n|San Nicolás|1.3%|\n|Treguaco|0.2%|\n|Yungay|0.5%|\n|Región de Ñuble|1.7%|\n|País|6.7%|"
          },
          "personas_en_hogares_carentes_de_servicios_basicos_fuente_marzo_2025_siis_t_mdsyf": {
            "ID": "GN-IND-SEC-0013",
            "Title": "Personas en Hogares Carentes de Servicios Básicos (Fuente: marzo 2025, SIIS-T MDSyF)",
            "Content": "\n|Comuna|Personas en Hogares Carentes de Servicios Básicos (%)|\n|-|-|\n|Bulnes|19.3%|\n|Chillán|8.6%|\n|Chillán Viejo|12.6%|\n|Cobquecura|43.3%|\n|Coelemu|31.3%|\n|Coihueco|20.5%|\n|El Carmen|32.8%|\n|Ninhue|50.6%|\n|Ñiquén|31.9%|\n|Pemuco|23.9%|\n|Pinto|28.3%|\n|Portezuelo|34.7%|\n|Quillón|36.8%|\n|Quirihue|19.4%|\n|Ránquil|24.9%|\n|San Carlos|11.8%|\n|San Fabián|17.6%|\n|San Ignacio|23.4%|\n|San Nicolás|24.6%|\n|Treguaco|36.0%|\n|Yungay|19.0%|\n|Región de Ñuble|17.8%|\n|País|13.1%|"
          },
          "hogares_hacinados_fuente_marzo_2025_siis_t_mdsyf": {
            "ID": "GN-IND-SEC-0014",
            "Title": "Hogares Hacinados (Fuente: marzo 2025, SIIS-T MDSyF)",
            "Content": "\n|Comuna|Hogares Hacinados (%)|\n|-|-|\n|Bulnes|8.7%|\n|Chillán|8.0%|\n|Chillán Viejo|8.8%|\n|Cobquecura|4.2%|\n|Coelemu|8.6%|\n|Coihueco|7.7%|\n|El Carmen|8.0%|\n|Ninhue|7.3%|\n|Ñiquén|9.1%|\n|Pemuco|10.1%|\n|Pinto|6.7%|\n|Portezuelo|7.9%|\n|Quillón|6.7%|\n|Quirihue|8.1%|\n|Ránquil|7.7%|\n|San Carlos|9.2%|\n|San Fabián|6.4%|\n|San Ignacio|6.6%|\n|San Nicolás|9.5%|\n|Treguaco|7.4%|\n|Yungay|7.2%|\n|Región de Ñuble|8.1%|\n|País|8.1%|"
          },
          "incidencia_de_la_pobreza_por_ingresos_y_multidimensional_personas_y_hogares_nubl": {
            "ID": "GN-IND-SEC-0015",
            "Title": "Incidencia de la pobreza por ingresos y multidimensional – Personas y Hogares (Ñuble vs Chile, 2017-2022)",
            "Content": "\n|Indicador|Año|Ñuble %|Chile %|Diferencia pp|\n|-|-|-|-|-|\n|Pobreza por ingresos (Personas)|2017|16.2|8.5|7.7|\n|Pobreza por ingresos (Personas)|2022|12.1|6.5|5.6|\n|Pobreza multidimensional (Personas)|2017|24.7|20.3|4.4|\n|Pobreza multidimensional (Personas)|2022|15.5|16.9|-1.4|\n|Pobreza por ingresos (Hogares)|2017|15.3|7.5|7.8|\n|Pobreza por ingresos (Hogares)|2022|10.0|5.6|4.4|\n|Pobreza multidimensional (Hogares)|2017|21.1|16.3|4.8|\n|Pobreza multidimensional (Hogares)|2022|12.7|13.4|-0.7|"
          },
          "brecha_de_genero_e_ingresos_promedio_rsh_junio_2024": {
            "ID": "GN-IND-SEC-0016",
            "Title": "Brecha de género e ingresos promedio (RSH, junio 2024)",
            "Content": "\n|Comuna|Brecha trabajo %|Ingreso trabajo $|Brecha pensiones %|Ingreso pensiones $|Brecha capital %|Ingreso capital $|Ingreso total $|\n|-|-|-|-|-|-|-|-|\n|Chillán|20.6|419.720|30.4|328.630|25.5|18.204|454.064|\n|Bulnes|40.2|344.897|30.3|293.134|39.3|13.240|386.324|\n|Chillán Viejo|31.0|363.376|30.3|292.603|32.7|12.606|392.394|\n|El Carmen|27.8|260.658|16.8|244.052|29.8|18.524|306.383|\n|Pemuco|44.1|294.312|22.0|252.727|40.9|14.967|328.939|\n|Pinto|25.3|286.412|30.7|292.602|32.0|23.838|346.398|\n|Quillón|40.6|289.956|35.4|310.853|39.4|14.227|346.065|\n|San Ignacio|33.7|254.345|23.3|252.129|34.7|17.037|299.355|\n|Yungay|44.0|367.011|33.0|298.907|42.0|8.863|391.730|\n|Quirihue|22.2|308.982|20.9|285.197|23.8|13.117|352.111|\n|Cobquecura|11.4|284.688|22.6|270.086|19.8|16.112|337.144|\n|Coelemu|39.4|355.896|26.0|269.687|37.6|11.976|381.217|\n|Ninhue|17.1|249.778|16.4|247.397|22.4|11.266|293.305|\n|Portezuelo|32.0|251.656|17.8|251.782|30.7|9.880|293.761|\n|Ránquil|36.5|286.882|29.6|279.914|37.2|12.206|355.300|\n|Treguaco|42.1|318.445|23.6|256.447|33.7|10.495|338.256|\n|San Carlos|29.2|329.625|25.4|267.691|32.6|21.781|369.475|\n|Coihueco|36.8|273.475|23.5|240.153|36.8|14.542|309.562|\n|Ñiquén|50.4|254.092|24.6|255.868|46.2|24.050|309.756|\n|San Fabián|21.6|297.134|21.8|279.774|30.1|13.600|345.726|\n|San Nicolás|33.0|299.839|27.9|252.409|35.6|14.366|334.358|\n|Total región|27.9|350.059|27.2|291.285|30.6|16.652|386.917|\n|Total país|25.6|440.919|35.0|319.755|29.4|16.232|468.619|"
          },
          "incidencia_de_la_inseguridad_alimentaria_moderada_o_grave_por_comuna_casen_2022": {
            "ID": "GN-IND-SEC-0017",
            "Title": "Incidencia de la inseguridad alimentaria moderada o grave por comuna (CASEN 2022)",
            "Content": "\n|Comuna|% hogares|\n|-|-|\n|Pemuco|25.2|\n|San Ignacio|22.2|\n|Chillán Viejo|21.5|\n|San Carlos|20.4|\n|Coihueco|19.6|\n|El Carmen|18.3|\n|Ninhue|17.9|\n|Portezuelo|17.1|\n|San Fabián|16.6|\n|Ñiquén|15.8|\n|Ránquil|7.3|\n|Treguaco|4.7|\n|Chillán|10.2|\n|Quillón|9.7|\n|Cobquecura|9.9|\n|Quirihue|10.5|\n|Bulnes|11.4|\n|Yungay|12.5|\n|San Nicolás|13.7|\n|Total región Ñuble|16.6|\n|Total nacional|18.9|"
          },
          "educacion_exclusion_rezago_y_escolaridad_promedio_rsh_junio_2024": {
            "ID": "GN-IND-SEC-0018",
            "Title": "Educación: exclusión, rezago y escolaridad promedio (RSH, junio 2024)",
            "Content": "\n|Comuna|% excluidos|Nº excluidos|% rezago|Nº rezago|Años escolaridad|Nº personas|\n|-|-|-|-|-|-|-|\n|Chillán|1.7|511|1.5|480|12.0|141564|\n|Bulnes|0.8|31|2.0|86|10.4|18811|\n|Chillán Viejo|1.3|80|1.6|105|11.5|25544|\n|El Carmen|0.9|18|1.0|23|9.7|10721|\n|Pemuco|0.6|C*|1.2|21|9.9|7282|\n|Pinto|2.0|41|1.6|36|10.6|10872|\n|Quillón|1.5|46|1.7|58|10.4|16710|\n|San Ignacio|0.9|24|1.4|41|9.9|14500|\n|Yungay|0.5|17|1.5|53|10.7|15736|\n|Quirihue|0.8|15|1.2|24|10.2|9428|\n|Cobquecura|2.0|15|2.2|17|10.0|4674|\n|Coelemu|0.8|20|0.6|18|10.3|13014|\n|Ninhue|0.7|C|1.2|11|9.3|4879|\n|Portezuelo|0.4|C|1.2|11|9.5|4507|\n|Ránquil|1.0|10|0.6|6|10.1|5526|\n|Treguaco|0.1|C|1.4|13|9.6|4934|\n|San Carlos|0.9|84|1.6|159|10.4|44320|\n|Coihueco|1.5|74|1.7|94|9.9|22143|\n|Ñiquén|0.9|17|2.6|54|9.3|10415|\n|San Fabián|3.0|27|2.2|22|10.2|4465|\n|San Nicolás|1.5|40|2.2|60|10.2|12190|\n|Total regional|1.3|1088|1.6|1393|10.9|402235|\n|Total país|3.3|92289|1.9|57768|11.7|13191306|"
          },
          "cobertura_de_pensiones_en_mayores_de_edad_legal_rsh_junio_2024": {
            "ID": "GN-IND-SEC-0019",
            "Title": "Cobertura de pensiones en mayores de edad legal (RSH, junio 2024)",
            "Content": "\n|Comuna|Con pensión|Sin pensión|Total|Cobertura %|\n|-|-|-|-|-|\n|Chillán|29394|3068|32462|90.5|\n|Bulnes|4196|436|4632|90.6|\n|Chillán Viejo|3456|434|3890|88.9|\n|El Carmen|2373|221|2594|91.5|\n|Pemuco|1810|189|1999|90.5|\n|Pinto|1988|230|2218|89.6|\n|Quillón|3839|303|4142|92.7|\n|San Ignacio|2568|258|2826|90.9|\n|Coihueco|3414|338|3752|91.0|\n|Ñiquén|2115|232|2347|90.1|\n|San Carlos|6002|531|6533|91.9|\n|San Fabián|1139|96|1235|92.2|\n|San Nicolás|2052|203|2255|91.0|\n|Treguaco|973|90|1063|91.5|\n|Cobquecura|1001|110|1111|90.1|\n|Ninhue|1254|122|1376|91.1|\n|Portezuelo|991|119|1110|89.3|\n|Quirihue|1948|189|2137|91.2|\n|Ránquil|875|82|957|91.4|\n|Coelemu|2434|271|2705|90.0|\n|Yungay|2574|261|2835|90.8|\n|Total Región|76696|7194|83890|91.4|"
          },
          "prevalencia_de_discapacidad_y_dependencia_por_sexo_endide_2022": {
            "ID": "GN-IND-SEC-0020",
            "Title": "Prevalencia de discapacidad y dependencia por sexo (ENDIDE 2022)",
            "Content": "\n|Sexo|Nº discapacidad|% discapacidad|Nº dependencia|% dependencia|\n|-|-|-|-|-|\n|Mujer|60438|29.6|36222|17.7|\n|Hombre|30093|15.8|15168|7.4|\n|Total regional|90531|22.9|51168|13.1|\n|Total país|2703897|17.6|1978917|11.9|"
          },
          "brecha_de_cuidados_por_comuna_rsh_junio_2024": {
            "ID": "GN-IND-SEC-0021",
            "Title": "Brecha de cuidados por comuna (RSH, junio 2024)",
            "Content": "\n|Comuna|Nº cuidadoras|Nº con cuidador|Nº sin cuidador|Total necesidades|Brecha %|\n|-|-|-|-|-|-|\n|Ránquil|42|45|1038|1083|95.8|\n|Bulnes|133|142|2432|2574|94.5|\n|Ñiquén|80|83|1392|1475|94.4|\n|Cobquecura|38|40|639|679|94.1|\n|Coihueco|163|165|2634|2799|94.1|\n|Ninhue|57|60|879|939|93.6|\n|San Ignacio|152|156|2072|2228|93.0|\n|El Carmen|131|130|1697|1827|92.9|\n|Yungay|150|155|1855|2010|92.3|\n|San Carlos|462|470|5532|6002|92.2|\n|Pemuco|87|89|1033|1122|92.1|\n|Portezuelo|76|80|938|1018|92.1|\n|Coelemu|143|147|1676|1823|91.9|\n|Quillón|181|184|2045|2229|91.7|\n|Chillán|1435|1476|15910|17386|91.5|\n|San Nicolás|172|182|1747|1929|90.6|\n|Pinto|129|131|1270|1401|90.6|\n|San Fabián|50|52|493|545|90.5|\n|Treguaco|80|82|761|843|90.3|\n|Chillán Viejo|380|386|2820|3206|88.0|\n|Quirihue|214|222|1259|1481|85.0|\n|Total regional|4355|4477|50122|54599|91.8|\n|Total país|114228|116776|1014119|1130895|89.7|"
          },
          "programas_publicos_y_gasto_regional_por_dimension_bips_2023": {
            "ID": "GN-IND-SEC-0022",
            "Title": "Programas públicos y gasto regional por dimensión (BIPS 2023)",
            "Content": "\n|Dimensión|Programas N|Gasto $|Gasto regional % país|\n|-|-|-|-|\n|Ciudad-integración-transporte-vivienda|37|116637531|2.7|\n|Cultura y artes|37|1970403|1.3|\n|Derechos humanos y justicia|30|17054475|3.1|\n|Economía y crecimiento|82|30267132|2.0|\n|Educación (formación-inclusión-calidad)|69|420917141|3.1|\n|Grupos específicos|74|84982123|3.7|\n|Medio ambiente y energía|29|69586237|9.1|\n|Política e institucionalidad nacional|31|2114692|1.2|\n|Salud-deporte-vida sana|60|36392574|2.2|\n|Trabajo-ingresos-seguridad social|48|337073065|3.3|\n|Total general|497|1116995373|3.2|"
          },
          "programas_publicos_y_gasto_por_poblacion_beneficiada_bips_2023": {
            "ID": "GN-IND-SEC-0023",
            "Title": "Programas públicos y gasto por población beneficiada (BIPS 2023)",
            "Content": "\n|Población beneficiada|Programas N|Promedio beneficiarios|Gasto $|\n|-|-|-|-|\n|Agentes Culturales|9|19|840337|\n|Barrios|5|9|765314|\n|Bienes Culturales|2|39|14940|\n|Comunas|17|10|11365644|\n|Empresas|37|141|7551914|\n|Estab. educacionales|15|132|8493591|\n|Hectáreas|2|23535|2478772|\n|Hogares / Familias|25|10154|181954056|\n|Localidades|3|7|985836|\n|Organizaciones|37|16|7161146|\n|Personas|300|18479|866496812|\n|Servicios de Salud|2|2|1883917|\n|Unidades|42|491|26999220|\n|Total general|497|–|1116995373|"
          },
          "proyectos_sni_en_ejecucion_por_comuna_pp_2023": {
            "ID": "GN-IND-SEC-0024",
            "Title": "Proyectos SNI en ejecución por comuna (PP 2023)",
            "Content": "\n|Comuna|Nº proyectos|Costo total $|Participación regional %|Habitantes|Inversión per cápita|\n|-|-|-|-|-|-|\n|Bulnes|2|1382593|0.2|22732|61|\n|Chillán|10|136614079|19.1|202826|674|\n|Chillán Viejo|6|6854514|1.0|35176|195|\n|Cobquecura|3|3919831|0.5|5238|748|\n|Coelemu|3|3519171|0.5|16894|208|\n|Coihueco|2|4520486|0.6|28908|156|\n|El Carmen|–|–|–|12234|–|\n|Ninhue|2|2188939|0.3|5370|408|\n|Ñiquén|–|–|–|11541|–|\n|Pemuco|–|–|–|8600|–|\n|Pinto|2|1361800|0.2|12110|112|\n|Portezuelo|–|–|–|4891|–|\n|Quillón|1|967109|0.1|19182|50|\n|Quirihue|1|3341215|0.5|12234|273|\n|Ránquil|–|–|–|6290|–|\n|San Carlos|3|9072035|1.3|56886|159|\n|San Fabián|–|–|–|4761|–|\n|San Ignacio|2|3949568|0.6|16614|238|\n|San Nicolás|2|4034017|0.6|12414|325|\n|Treguaco|–|–|–|5752|–|\n|Yungay|–|–|–|18784|–|\n|Intercomunal/Regional|25|534951479|74.6|–|–|\n|Total regional|57|716676836|100.0|519437|1380|"
          },
          "cobertura_del_registro_social_de_hogares_por_comuna_abril_2025": {
            "ID": "GN-IND-SEC-0025",
            "Title": "Cobertura del Registro Social de Hogares por comuna (abril 2025)",
            "Content": "\n|Comuna|Personas RSH|Personas %|Hogares RSH|Hogares %|\n|-|-|-|-|-|\n|Chillán|182223|35.19|89857|34.69|\n|Bulnes|24447|4.72|11930|4.61|\n|Chillán Viejo|34391|6.64|17191|6.64|\n|El Carmen|13664|2.64|6825|2.63|\n|Pemuco|9296|1.80|4664|1.80|\n|Pinto|13836|2.67|7511|2.90|\n|Quillón|21215|4.10|11419|4.41|\n|San Ignacio|18347|3.54|9838|3.80|\n|Yungay|20159|3.89|10283|3.97|\n|Quirihue|11899|2.30|5961|2.30|\n|Cobquecura|5685|1.10|2917|1.13|\n|Coelemu|16593|3.20|8006|3.09|\n|Ninhue|6106|1.18|3400|1.31|\n|Portezuelo|5569|1.08|2911|1.12|\n|Ránquil|6995|1.35|3822|1.48|\n|Treguaco|6121|1.18|3265|1.26|\n|San Carlos|57082|11.02|27763|10.72|\n|Coihueco|29223|5.64|13546|5.23|\n|Ñiquén|13025|2.52|6733|2.60|\n|San Fabián|5837|1.13|3216|1.24|\n|San Nicolás|16147|3.12|7984|3.08|"
          },
          "hogares_con_ninos_ninas_o_adolescentes_pais_vs_region_de_nuble_abril_2025": {
            "ID": "GN-IND-SEC-0026",
            "Title": "Hogares con niños, niñas o adolescentes – País vs Región de Ñuble (abril 2025)",
            "Content": "\n|Presencia|Hogares País|% País|Hogares Región|% Región|\n|-|-|-|-|-|\n|No|6701312|73.4|187618|72.4|\n|Sí|2423209|26.6|71424|27.6|\n|Total|9124521|100.0|259042|100.0|"
          },
          "hogares_con_personas_60_anos_pais_vs_region_de_nuble_abril_2025": {
            "ID": "GN-IND-SEC-0027",
            "Title": "Hogares con personas ≥ 60 años – País vs Región de Ñuble (abril 2025)",
            "Content": "\n|Presencia|Hogares País|% País|Hogares Región|% Región|\n|-|-|-|-|-|\n|No|6204069|68.0|162762|62.8|\n|Sí|2920452|32.0|96280|37.2|\n|Total|9124521|100.0|259042|100.0|"
          },
          "estudiantes_con_inasistencia_escolar_pais_vs_region_de_nuble_rex_241_2024": {
            "ID": "GN-IND-SEC-0028",
            "Title": "Estudiantes con inasistencia escolar – País vs Región de Ñuble (REX 241/2024)",
            "Content": "\n|Tipo Inasistencia|Estudiantes País|% País|Estudiantes Región|% Región|\n|-|-|-|-|-|\n|Inasistencia reiterada|487635|11.1|12173|9.6|\n|Inasistencia grave|878359|19.9|19540|15.4|\n|Total|4405011|100.0|127107|100.0|"
          },
          "personas_que_requieren_cuidados_region_de_nuble_abril_2025": {
            "ID": "GN-IND-SEC-0029",
            "Title": "Personas que requieren cuidados – Región de Ñuble (abril 2025)",
            "Content": "\n|Situación|Personas|\n|-|-|\n|PSDF con cuidador|6523|\n|PSDF sin cuidador|51212|\n|Total|57735|"
          },
          "origen_de_las_diadas_cuidador_receptor_region_de_nuble_abril_2025": {
            "ID": "GN-IND-SEC-0030",
            "Title": "Origen de las díadas cuidador-receptor – Región de Ñuble (abril 2025)",
            "Content": "\n|Origen|N|%|\n|-|-|-|\n|Estipendio|1333|19.97|\n|PRLAC|246|3.69|\n|Estipendio + PRLAC|106|1.59|\n|Solicitudes|4989|74.75|\n|Total|6674|100.00|"
          },
          "personas_identificadas_como_cuidadoras_por_comuna_region_de_nuble_abril_2025": {
            "ID": "GN-IND-SEC-0031",
            "Title": "Personas identificadas como cuidadoras por comuna – Región de Ñuble (abril 2025)",
            "Content": "\n|Comuna|Personas RSH|Personas cuidadoras|% Personas cuidadoras|\n|-|-|-|-|\n|Chillán|182223|2131|1.17|\n|Bulnes|24447|194|0.79|\n|Chillán Viejo|34391|503|1.46|\n|El Carmen|13664|196|1.43|\n|Pemuco|9296|114|1.23|\n|Pinto|13836|188|1.36|\n|Quillón|21215|289|1.36|\n|San Ignacio|18347|197|1.07|\n|Yungay|20159|232|1.15|\n|Quirihue|11899|273|2.29|\n|Cobquecura|5685|84|1.48|\n|Coelemu|16593|201|1.21|\n|Ninhue|6106|77|1.26|\n|Portezuelo|5569|112|2.01|\n|Ránquil|6995|132|1.89|\n|Treguaco|6121|104|1.70|\n|San Carlos|57082|657|1.15|\n|Coihueco|29223|242|0.83|\n|Ñiquén|13025|126|0.97|\n|San Fabián|5837|69|1.18|\n|San Nicolás|16147|244|1.51|\n|Total|517860|6365|1.23|"
          },
          "cobertura_de_prestaciones_sociales_region_de_nuble_2024": {
            "ID": "GN-IND-SEC-0032",
            "Title": "Cobertura de prestaciones sociales – Región de Ñuble (2024)",
            "Content": "\n|Categoría|% Cobertura RSH|\n|-|-|\n|Al menos un programa|71|\n|Niñas y niños|96|\n|Personas ≥ 60 años|77|\n|Tramo 40 CSE|79|"
          },
          "transferencias_monetarias_recibidas_region_de_nuble_2024": {
            "ID": "GN-IND-SEC-0033",
            "Title": "Transferencias monetarias recibidas – Región de Ñuble (2024)",
            "Content": "\n|Indicador|Personas|% Población RSH|\n|-|-|-|\n|Personas con transferencia|250202|48.0|"
          },
          "programas_con_mayor_cobertura_regional_region_de_nuble_2024": {
            "ID": "GN-IND-SEC-0034",
            "Title": "Programas con mayor cobertura regional – Región de Ñuble (2024)",
            "Content": "\n* Subsidio Familiar (SUF)\n* Subvención Escolar Regular\n* Programa Modernización de Textos Escolares\n* Centro de Lectura y Biblioteca Escolar (CRA)\n* Pensión Garantizada Universal\n* Otras Subvenciones Escolares\n* Bono Invierno\n* Subsidio al Pago Electrónico Útiles Escolares\n* Tarjeta Nacional Estudiantil (TNE)"
          }
        }
      },
      "indicadores_de_vivienda_y_servicios_basicos_fuente_censo_2024_ine": {
        "ID": "GN-IND-SEC-0035",
        "Title": "Indicadores de Vivienda y Servicios Básicos (Fuente: Censo 2024, INE)",
        "Content": "",
        "Sections": {
          "promedio_de_personas_por_hogar": {
            "ID": "GN-IND-SEC-0036",
            "Title": "Promedio de Personas por Hogar",
            "Content": "\n|Código comuna|Comuna|Hogares censados|Promedio de personas por hogar|\n|-|-|-|-|\n|16302|Coihueco|10.468|2,8|\n|16103|Chillán Viejo|11.738|2,8|\n|16|Ñuble|190.402|2,7|\n|16304|San Fabián|2.022|2,6|\n|16205|Portezuelo|2.045|2,5|\n|16202|Cobquecura|2.305|2,4|\n|16204|Ninhue|2.308|2,5|\n|16207|Trehuaco|2.336|2,6|\n|16206|Ránquil|2.615|2,5|\n|16301|San Carlos|20.672|2,7|\n|16105|Pemuco|3.243|2,7|\n|16201|Quirihue|4.642|2,5|\n|16106|Pinto|4.774|2,6|\n|16303|Ñiquén|4.920|2,6|\n|16104|El Carmen|5.008|2,6|\n|16305|San Nicolás|5.442|2,8|\n|16203|Coelemu|5.638|2,8|\n|0|País|6.596.527|2,8|\n|16108|San Ignacio|6.620|2,6|\n|16109|Yungay|7.309|2,5|\n|16107|Quillón|7.523|2,5|\n|16101|Chillán|70.003|2,7|\n|16102|Bulnes|8.771|2,7|"
          },
          "fuente_de_energia_para_cocinar": {
            "ID": "GN-IND-SEC-0037",
            "Title": "Fuente de Energía para Cocinar",
            "Content": "\n|Código comuna|Comuna|Hogares censados|Gas|Parafina o petróleo|Leña|Pellet|Carbón|Electricidad|Energía solar (ej. cocina u horno solar)|No utiliza fuente de energía o combustible para cocinar|Fuente de energía o combustible para cocinar no declarada|\n|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.596.527|5.780.274|3.832|339.220|1.960|1.520|439.520|639|28.860|702|\n|16|Ñuble|190.402|172.674|109|14.236|73|109|2.541|11|643|6|\n|16101|Chillán|70.003|66.907|42|933|20|57|1.808|3|230|3|\n|16102|Bulnes|8.771|8.139|7|531|2|2|56|1|33|0|\n|16103|Chillán Viejo|11.738|11.252|12|292|5|8|134|1|34|0|\n|16104|El Carmen|5.008|3.935|5|1.036|3|4|10|1|14|0|\n|16105|Pemuco|3.243|2.629|0|590|4|1|8|0|10|1|\n|16106|Pinto|4.774|4.114|1|585|4|2|50|0|18|0|\n|16107|Quillón|7.523|6.670|3|774|2|1|49|0|24|0|\n|16108|San Ignacio|6.620|5.592|0|975|4|2|15|2|30|0|\n|16109|Yungay|7.309|6.365|9|860|3|0|42|0|30|0|\n|16201|Quirihue|4.642|3.704|2|857|5|0|51|0|23|0|\n|16202|Cobquecura|2.305|1.608|0|670|3|0|13|0|11|0|\n|16203|Coelemu|5.638|4.789|0|804|4|0|19|1|21|0|\n|16204|Ninhue|2.308|1.905|0|388|1|0|5|0|9|0|\n|16205|Portezuelo|2.045|1.587|1|443|1|1|3|0|9|0|\n|16206|Ránquil|2.615|2.120|1|473|1|0|10|0|10|0|\n|16207|Trehuaco|2.336|1.658|1|661|0|0|8|0|8|0|\n|16301|San Carlos|20.672|19.278|10|1.175|4|17|128|1|57|2|\n|16302|Coihueco|10.468|9.313|9|1.031|3|5|69|0|38|0|\n|16303|Ñiquén|4.920|4.443|3|435|1|5|14|0|19|0|\n|16304|San Fabián|2.022|1.820|2|181|0|1|15|1|2|0|\n|16305|San Nicolás|5.442|4.846|1|542|3|3|34|0|13|0|"
          },
          "fuente_de_energia_para_calefaccion": {
            "ID": "GN-IND-SEC-0038",
            "Title": "Fuente de Energía para Calefacción",
            "Content": "\n|Código comuna|Comuna|Hogares censados|Gas|Parafina o petróleo|Leña|Pellet|Carbón|Electricidad|Otra|No utiliza fuente de energía o combustible para calefaccionar|Fuente de energía o combustible para calefaccionar no declarada|\n|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.596.527|1.688.313|680.755|1.606.997|137.853|13.426|1.283.687|24.691|1.159.827|978|\n|16|Ñuble|190.402|20.541|16.277|115.396|10.566|1.033|19.348|526|6.706|9|\n|16101|Chillán|70.003|10.500|10.753|25.175|7.882|288|12.463|237|2.700|5|\n|16102|Bulnes|8.771|1.010|591|5.949|139|58|660|24|339|1|\n|16103|Chillán Viejo|11.738|1.727|1.564|4.967|1.271|56|1.619|63|471|0|\n|16104|El Carmen|5.008|260|87|4.220|33|29|225|14|140|0|\n|16105|Pemuco|3.243|127|49|2.832|27|10|102|3|92|1|\n|16106|Pinto|4.774|198|107|4.151|74|23|120|6|95|0|\n|16107|Quillón|7.523|680|319|5.619|92|27|486|22|278|0|\n|16108|San Ignacio|6.620|298|136|5.693|38|41|214|11|189|0|\n|16109|Yungay|7.309|352|198|6.131|66|9|276|19|258|0|\n|16201|Quirihue|4.642|383|109|3.674|27|29|235|3|182|0|\n|16202|Cobquecura|2.305|216|66|1.660|23|47|132|3|158|0|\n|16203|Coelemu|5.638|301|80|4.920|89|11|119|11|107|0|\n|16204|Ninhue|2.308|162|31|1.866|8|36|82|6|117|0|\n|16205|Portezuelo|2.045|184|38|1.598|8|16|93|7|101|0|\n|16206|Ránquil|2.615|233|54|2.053|34|11|138|5|87|0|\n|16207|Trehuaco|2.336|101|37|2.033|23|9|59|2|72|0|\n|16301|San Carlos|20.672|2.439|1.377|13.902|445|178|1.548|54|728|1|\n|16302|Coihueco|10.468|498|310|8.917|162|49|335|13|183|1|\n|16303|Ñiquén|4.920|322|120|4.122|36|47|123|7|143|0|\n|16304|San Fabián|2.022|98|31|1.785|27|9|46|3|23|0|\n|16305|San Nicolás|5.442|452|220|4.129|62|50|273|13|243|0|"
          },
          "equipamiento_y_servicios_en_el_hogar": {
            "ID": "GN-IND-SEC-0039",
            "Title": "Equipamiento y Servicios en el Hogar",
            "Content": "\n|Código comuna|Comuna|Disponibilidad de equipo o servicio|Teléfono móvil, celular o smartphone|Computador (escritorio, portátil)|Tablet|Internet fija|Internet móvil desde un celular, tablet o BAM|Internet por conexión satelital|\n|-|-|-|-|-|-|-|-|-|\n|0|País|Sí|6.475.071|3.621.619|1.645.321|4.250.122|5.734.118|288.473|\n|0|País|No|119.949|2.964.123|4.939.222|2.338.834|854.837|6.293.135|\n|0|País|Disponibilidad no declarada|1.507|10.785|11.984|7.571|7.572|14.919|\n|16|Ñuble|Sí|186.354|83.435|31.446|84.705|155.864|8.212|\n|16|Ñuble|No|4.030|106.795|158.783|105.570|34.447|182.006|\n|16|Ñuble|Disponibilidad no declarada|18|172|173|127|91|184|\n|16101|Chillán|Sí|68.953|38.122|15.229|45.657|60.869|2.772|\n|16101|Chillán|No|1.042|31.795|54.687|24.299|9.090|67.142|\n|16101|Chillán|Disponibilidad no declarada|8|86|87|47|44|89|\n|16102|Bulnes|Sí|8.542|3.472|1.305|3.126|7.016|501|\n|16102|Bulnes|No|229|5.295|7.461|5.640|1.752|8.262|\n|16102|Bulnes|Disponibilidad no declarada|0|4|5|5|3|8|\n|16103|Chillán Viejo|Sí|11.548|5.610|2.052|6.583|9.675|673|\n|16103|Chillán Viejo|No|190|6.121|9.680|5.151|2.061|11.056|\n|16103|Chillán Viejo|Disponibilidad no declarada|0|7|6|4|2|9|\n|16104|El Carmen|Sí|4.856|1.646|575|1.274|3.811|77|\n|16104|El Carmen|No|152|3.360|4.431|3.731|1.194|4.929|\n|16104|El Carmen|Disponibilidad no declarada|0|2|2|3|3|2|\n|16105|Pemuco|Sí|3.156|1.100|334|590|2.526|80|\n|16105|Pemuco|No|86|2.140|2.906|2.650|715|3.160|\n|16105|Pemuco|Disponibilidad no declarada|1|3|3|3|2|3|\n|16106|Pinto|Sí|4.633|1.870|630|1.133|3.799|195|\n|16106|Pinto|No|140|2.900|4.139|3.637|971|4.574|\n|16106|Pinto|Disponibilidad no declarada|1|4|5|4|4|5|\n|16107|Quillón|Sí|7.355|2.635|1.034|2.359|6.002|323|\n|16107|Quillón|No|167|4.877|6.478|5.159|1.516|7.191|\n|16107|Quillón|Disponibilidad no declarada|1|11|11|5|5|9|\n|16108|San Ignacio|Sí|6.429|2.102|643|1.301|4.968|153|\n|16108|San Ignacio|No|191|4.511|5.971|5.316|1.648|6.460|\n|16108|San Ignacio|Disponibilidad no declarada|0|7|6|3|4|7|\n|16109|Yungay|Sí|7.129|2.687|997|2.437|5.840|305|\n|16109|Yungay|No|179|4.618|6.307|4.868|1.467|7.000|\n|16109|Yungay|Disponibilidad no declarada|1|4|5|4|2|4|\n|16201|Quirihue|Sí|4.518|1.670|635|1.918|3.325|212|\n|16201|Quirihue|No|124|2.972|4.007|2.723|1.316|4.430|\n|16201|Quirihue|Disponibilidad no declarada|0|0|0|1|1|0|\n|16202|Cobquecura|Sí|2.232|766|291|351|1.756|50|\n|16202|Cobquecura|No|73|1.539|2.013|1.953|548|2.254|\n|16202|Cobquecura|Disponibilidad no declarada|0|0|1|1|1|1|\n|16203|Coelemu|Sí|5.513|2.297|808|2.270|4.549|111|\n|16203|Coelemu|No|125|3.339|4.829|3.366|1.088|5.526|\n|16203|Coelemu|Disponibilidad no declarada|0|2|1|2|1|1|\n|16204|Ninhue|Sí|2.248|724|240|336|1.678|93|\n|16204|Ninhue|No|60|1.584|2.068|1.972|630|2.215|\n|16204|Ninhue|Disponibilidad no declarada|0|0|0|0|0|0|\n|16205|Portezuelo|Sí|1.970|629|231|351|1.504|111|\n|16205|Portezuelo|No|75|1.416|1.814|1.694|541|1.934|\n|16205|Portezuelo|Disponibilidad no declarada|0|0|0|0|0|0|\n|16206|Ránquil|Sí|2.541|848|317|537|2.134|66|\n|16206|Ránquil|No|74|1.766|2.297|2.077|480|2.548|\n|16206|Ránquil|Disponibilidad no declarada|0|1|1|1|1|1|\n|16207|Trehuaco|Sí|2.257|798|284|665|1.774|34|\n|16207|Trehuaco|No|79|1.538|2.052|1.671|562|2.302|\n|16207|Trehuaco|Disponibilidad no declarada|0|0|0|0|0|0|\n|16301|San Carlos|Sí|20.200|8.069|2.994|8.522|16.305|1.215|\n|16301|San Carlos|No|468|12.579|17.652|12.126|4.358|19.434|\n|16301|San Carlos|Disponibilidad no declarada|4|24|26|24|9|23|\n|16302|Coihueco|Sí|10.233|3.915|1.268|2.689|8.571|635|\n|16302|Coihueco|No|234|6.542|9.190|7.768|1.892|9.821|\n|16302|Coihueco|Disponibilidad no declarada|1|11|10|11|5|12|\n|16303|Ñiquén|Sí|4.721|1.401|472|473|3.685|172|\n|16303|Ñiquén|No|198|3.515|4.445|4.442|1.233|4.745|\n|16303|Ñiquén|Disponibilidad no declarada|1|4|3|5|2|3|\n|16304|San Fabián|Sí|1.975|865|305|520|1.691|109|\n|16304|San Fabián|No|47|1.157|1.717|1.502|331|1.913|\n|16304|San Fabián|Disponibilidad no declarada|0|0|0|0|0|0|\n|16305|San Nicolás|Sí|5.345|2.209|802|1.613|4.386|325|\n|16305|San Nicolás|No|97|3.231|4.639|3.825|1.054|5.110|\n|16305|San Nicolás|Disponibilidad no declarada|0|2|1|4|2|7|"
          },
          "regimen_de_tenencia_de_la_vivienda": {
            "ID": "GN-IND-SEC-0040",
            "Title": "Régimen de Tenencia de la Vivienda",
            "Content": "\n|Código comuna|Comuna|Hogares censados|Propia pagada|Propia pagándose|Arrendada con contrato|Arrendada sin contrato|Cedida por trabajo o servicio|Cedida por familiar u otro|Usufructo: solo uso y goce|Ocupada de hecho|Propiedad en sucesión y litigio|Tenencia de la vivienda no declarada|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.596.527|3.120.238|910.247|1.229.328|498.871|90.697|511.118|61.019|57.788|116.125|1.096|\n|16|Ñuble|190.402|117.256|14.927|20.062|11.148|3.445|16.661|1.919|775|4.195|14|\n|16101|Chillán|70.003|35.656|10.905|11.679|4.163|618|4.685|692|192|1.408|5|\n|16102|Bulnes|8.771|5.877|424|586|445|248|779|79|73|259|1|\n|16103|Chillán Viejo|11.738|6.514|1.418|1.551|805|133|976|127|38|175|1|\n|16104|El Carmen|5.008|3.490|38|210|293|154|541|109|14|158|1|\n|16105|Pemuco|3.243|2.315|37|141|181|80|369|29|15|75|1|\n|16106|Pinto|4.774|3.183|58|324|313|255|544|24|22|51|0|\n|16107|Quillón|7.523|5.156|132|514|418|277|819|67|36|104|0|\n|16108|San Ignacio|6.620|4.572|57|316|385|168|853|48|20|201|0|\n|16109|Yungay|7.309|4.688|212|570|581|163|737|99|40|219|0|\n|16201|Quirihue|4.642|3.236|55|398|322|43|369|33|24|162|0|\n|16202|Cobquecura|2.305|1.703|23|108|140|36|189|31|12|63|0|\n|16203|Coelemu|5.638|3.550|83|471|413|76|653|132|50|210|0|\n|16204|Ninhue|2.308|1.827|20|63|87|25|225|11|7|43|0|\n|16205|Portezuelo|2.045|1.589|11|51|75|39|215|6|22|37|0|\n|16206|Ránquil|2.615|1.907|34|103|97|47|286|41|14|86|0|\n|16207|Trehuaco|2.336|1.778|18|130|118|26|186|12|8|60|0|\n|16301|San Carlos|20.672|13.815|1.011|1.751|1.173|342|1.895|173|78|431|3|\n|16302|Coihueco|10.468|7.323|251|459|620|344|1.168|77|39|187|0|\n|16303|Ñiquén|4.920|3.713|29|206|131|165|474|44|25|133|0|\n|16304|San Fabián|2.022|1.383|16|158|145|58|197|25|12|28|0|\n|16305|San Nicolás|5.442|3.981|95|273|243|148|501|60|34|105|2|"
          },
          "tipo_de_vivienda_particular_ocupada": {
            "ID": "GN-IND-SEC-0041",
            "Title": "Tipo de Vivienda Particular Ocupada",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Casa con acceso directo desde la calle|Casa en condominio cerrado|Departamento en edificio con ascensor|Departamento en edificio sin ascensor|Vivienda tradicional indígena (ruka u otras)|Pieza en casa antigua o conventillo|Mediagua, mejora, vivienda de emergencia, rancho o choza|Móvil (carpa, casa rodante o similar)|Otro tipo de vivienda particular|\n|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|4.622.485|417.769|715.486|558.890|1.237|45.788|19.936|1.323|25.258|\n|16|Ñuble|187.513|173.396|6.237|1.534|4.836|15|103|379|38|975|\n|16101|Chillán|68.623|60.285|2.767|1.384|3.886|4|70|71|10|146|\n|16102|Bulnes|8.668|8.129|261|71|104|0|3|74|1|25|\n|16103|Chillán Viejo|11.522|10.616|333|4|509|0|0|28|5|27|\n|16104|El Carmen|4.966|4.927|29|0|1|0|1|6|0|2|\n|16105|Pemuco|3.207|3.023|93|0|0|0|0|8|1|82|\n|16106|Pinto|4.714|4.408|278|10|4|1|4|3|0|6|\n|16107|Quillón|7.432|7.076|304|1|0|0|2|29|1|19|\n|16108|San Ignacio|6.533|6.398|112|2|0|0|2|12|1|6|\n|16109|Yungay|7.238|7.088|105|2|6|2|4|13|0|18|\n|16201|Quirihue|4.586|4.444|68|27|9|0|3|24|0|11|\n|16202|Cobquecura|2.276|2.241|23|0|0|1|1|4|1|5|\n|16203|Coelemu|5.555|5.423|105|0|0|1|3|11|0|12|\n|16204|Ninhue|2.296|2.275|14|0|1|0|2|0|0|4|\n|16205|Portezuelo|2.019|1.985|17|6|0|0|0|8|0|3|\n|16206|Ránquil|2.586|2.348|203|0|0|0|2|7|0|26|\n|16207|Trehuaco|2.317|2.294|6|0|0|0|0|9|0|8|\n|16301|San Carlos|20.385|18.903|786|24|304|2|3|26|13|324|\n|16302|Coihueco|10.350|9.895|216|1|5|0|1|21|0|211|\n|16303|Ñiquén|4.869|4.478|364|0|2|0|0|10|3|12|\n|16304|San Fabián|2.007|1.944|50|1|1|0|0|6|0|5|\n|16305|San Nicolás|5.364|5.216|103|1|4|4|2|9|2|23|"
          },
          "materialidad_de_paredes_exteriores": {
            "ID": "GN-IND-SEC-0042",
            "Title": "Materialidad de Paredes Exteriores",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Hormigón armado|Albañilería: bloque de cemento, ladrillo o piedra|Tabique forrado por ambas caras|Tabique sin forro interior|Adobe, barro, pirca, quincha u otro material artesanal|Materiales precarios o de desecho|Material paredes exteriores no declarado|\n|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|1.499.949|2.754.185|1.854.738|176.313|106.790|14.752|1.445|\n|16|Ñuble|187.513|18.390|65.809|94.254|6.070|2.492|479|19|\n|16101|Chillán|68.623|11.960|34.256|20.466|1.447|407|84|3|\n|16102|Bulnes|8.668|521|2.109|5.467|414|110|47|0|\n|16103|Chillán Viejo|11.522|1.031|5.210|4.887|299|71|23|1|\n|16104|El Carmen|4.966|159|864|3.656|222|52|13|0|\n|16105|Pemuco|3.207|138|957|1.834|136|133|8|1|\n|16106|Pinto|4.714|191|618|3.604|258|32|11|0|\n|16107|Quillón|7.432|273|1.415|5.318|328|71|24|3|\n|16108|San Ignacio|6.533|215|1.349|4.523|302|112|31|1|\n|16109|Yungay|7.238|351|1.134|5.375|332|20|23|3|\n|16201|Quirihue|4.586|137|1.142|2.944|185|168|8|2|\n|16202|Cobquecura|2.276|64|356|1.669|65|121|1|0|\n|16203|Coelemu|5.555|296|1.524|3.462|185|69|19|0|\n|16204|Ninhue|2.296|50|377|1.681|81|98|8|1|\n|16205|Portezuelo|2.019|68|232|1.481|91|146|1|0|\n|16206|Ránquil|2.586|131|351|1.904|129|60|11|0|\n|16207|Trehuaco|2.317|101|629|1.490|53|41|3|0|\n|16301|San Carlos|20.385|1.902|8.081|9.391|589|331|91|0|\n|16302|Coihueco|10.350|360|1.811|7.670|435|56|17|1|\n|16303|Ñiquén|4.869|194|2.060|2.160|219|209|27|0|\n|16304|San Fabián|2.007|105|394|1.388|83|27|10|0|\n|16305|San Nicolás|5.364|143|940|3.884|217|158|19|3|"
          },
          "materialidad_de_la_cubierta_del_techo": {
            "ID": "GN-IND-SEC-0043",
            "Title": "Materialidad de la Cubierta del Techo",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Teja o tejuelas de arcilla, metálicas, de cemento, de madera, asfálticas o plásticas|Losa hormigón|Planchas metálicas de zinc, cobre, etc.|Planchas de fibrocemento tipo pizarreño|Fonolita o plancha de fieltro embreado|Paja, coirón, totora o caña|Materiales precarios o de desecho|Sin cubierta sólida de techo|Material cubierta de techo no declarado|\n|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|1.069.613|958.191|3.658.013|699.395|10.847|1.090|6.800|1.872|2.351|\n|16|Ñuble|187.513|16.231|3.220|161.559|6.178|205|18|63|24|15|\n|16101|Chillán|68.623|9.943|2.689|52.681|3.196|79|4|18|5|8|\n|16102|Bulnes|8.668|438|74|7.911|221|15|1|4|4|0|\n|16103|Chillán Viejo|11.522|557|195|10.277|473|10|3|4|1|2|\n|16104|El Carmen|4.966|305|3|4.554|98|4|1|0|0|1|\n|16105|Pemuco|3.207|141|2|3.017|43|1|0|1|1|1|\n|16106|Pinto|4.714|383|12|4.246|66|4|0|0|3|0|\n|16107|Quillón|7.432|385|2|6.863|162|10|1|8|1|0|\n|16108|San Ignacio|6.533|278|4|6.139|105|2|0|3|1|1|\n|16109|Yungay|7.238|245|11|6.829|142|5|0|2|3|1|\n|16201|Quirihue|4.586|276|29|4.144|134|2|1|0|0|0|\n|16202|Cobquecura|2.276|217|2|1.936|119|2|0|0|0|0|\n|16203|Coelemu|5.555|325|7|4.908|310|2|1|2|0|0|\n|16204|Ninhue|2.296|73|1|2.177|41|4|0|0|0|0|\n|16205|Portezuelo|2.019|76|1|1.900|38|4|0|0|0|0|\n|16206|Ránquil|2.586|173|4|2.319|85|4|0|1|0|0|\n|16207|Trehuaco|2.317|65|0|2.194|54|2|1|0|0|1|\n|16301|San Carlos|20.385|1.204|168|18.498|474|27|1|10|3|0|\n|16302|Coihueco|10.350|531|6|9.614|183|12|1|2|1|0|\n|16303|Ñiquén|4.869|264|3|4.475|121|4|1|1|0|0|\n|16304|San Fabián|2.007|111|2|1.878|6|7|1|2|0|0|\n|16305|San Nicolás|5.364|241|5|4.999|107|5|1|5|1|0|"
          },
          "materialidad_del_piso": {
            "ID": "GN-IND-SEC-0044",
            "Title": "Materialidad del Piso",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|\"Parquet, piso flotante cerámico, madera, alfombra, flexit, cubrepiso u otro similar; sobre radier o vigas de madera\"|Radier sin revestimiento|Baldosa de cemento|Capa de cemento sobre tierra|Tierra|Material del piso no declarado|\n|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.036.357|145.177|143.611|63.853|17.010|2.164|\n|16|Ñuble|187.513|175.708|6.632|2.920|1.785|442|26|\n|16101|Chillán|68.623|66.141|1.231|846|343|55|7|\n|16102|Bulnes|8.668|8.099|354|150|49|14|2|\n|16103|Chillán Viejo|11.522|11.015|364|73|52|16|2|\n|16104|El Carmen|4.966|4.398|315|84|150|19|0|\n|16105|Pemuco|3.207|2.900|162|56|79|8|2|\n|16106|Pinto|4.714|4.422|163|72|41|13|3|\n|16107|Quillón|7.432|6.726|367|214|106|19|0|\n|16108|San Ignacio|6.533|5.878|455|74|103|23|0|\n|16109|Yungay|7.238|6.604|395|144|78|15|2|\n|16201|Quirihue|4.586|4.294|146|53|61|32|0|\n|16202|Cobquecura|2.276|2.101|92|39|29|14|1|\n|16203|Coelemu|5.555|5.308|84|121|33|9|0|\n|16204|Ninhue|2.296|2.001|175|50|50|20|0|\n|16205|Portezuelo|2.019|1.858|109|24|17|11|0|\n|16206|Ránquil|2.586|2.227|139|193|17|10|0|\n|16207|Trehuaco|2.317|2.175|65|23|41|13|0|\n|16301|San Carlos|20.385|18.786|859|396|278|61|5|\n|16302|Coihueco|10.350|9.738|357|142|94|18|1|\n|16303|Ñiquén|4.869|4.404|327|57|48|33|0|\n|16304|San Fabián|2.007|1.853|70|40|30|14|0|\n|16305|San Nicolás|5.364|4.780|403|69|86|25|1|"
          },
          "estado_de_conservacion_de_la_vivienda": {
            "ID": "GN-IND-SEC-0045",
            "Title": "Estado de Conservación de la Vivienda",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Viviendas irrecuperables|Viviendas sin requerimientos de reemplazo|Viviendas con requerimiento de reemplazo ignorado|\n|-|-|-|-|-|-|\n|0|País|6.408.172|72.642|6.331.142|4.388|\n|16|Ñuble|187.513|2.180|185.281|52|\n|16101|Chillán|68.623|347|68.260|16|\n|16102|Bulnes|8.668|143|8.523|2|\n|16103|Chillán Viejo|11.522|90|11.429|3|\n|16104|El Carmen|4.966|40|4.925|1|\n|16105|Pemuco|3.207|102|3.103|2|\n|16106|Pinto|4.714|29|4.682|3|\n|16107|Quillón|7.432|89|7.340|3|\n|16108|San Ignacio|6.533|68|6.463|2|\n|16109|Yungay|7.238|62|7.172|4|\n|16201|Quirihue|4.586|70|4.514|2|\n|16202|Cobquecura|2.276|24|2.251|1|\n|16203|Coelemu|5.555|50|5.505|0|\n|16204|Ninhue|2.296|31|2.264|1|\n|16205|Portezuelo|2.019|23|1.996|0|\n|16206|Ránquil|2.586|50|2.536|0|\n|16207|Trehuaco|2.317|29|2.287|1|\n|16301|San Carlos|20.385|488|19.892|5|\n|16302|Coihueco|10.350|257|10.091|2|\n|16303|Ñiquén|4.869|78|4.791|0|\n|16304|San Fabián|2.007|34|1.973|0|\n|16305|San Nicolás|5.364|76|5.284|4|"
          },
          "numero_de_dormitorios_por_vivienda": {
            "ID": "GN-IND-SEC-0046",
            "Title": "Número de Dormitorios por Vivienda",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|0 dormitorios|1 dormitorio|2 dormitorios|3 dormitorios|4 dormitorios|5 dormitorios|6 o más dormitorios|Cantidad de dormitorios no declarado|\n|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|36.835|1.575.168|2.419.639|1.785.285|451.532|100.036|38.643|1.034|\n|16|Ñuble|187.513|399|47.543|72.638|52.546|11.775|2.055|547|10|\n|16101|Chillán|68.623|148|14.573|27.092|21.166|4.652|790|198|4|\n|16102|Bulnes|8.668|31|2.324|3.366|2.311|526|83|27|0|\n|16103|Chillán Viejo|11.522|27|2.087|4.904|3.628|704|140|31|1|\n|16104|El Carmen|4.966|7|762|1.754|1.781|505|126|31|0|\n|16105|Pemuco|3.207|9|811|1.130|927|261|51|17|1|\n|16106|Pinto|4.714|15|1.629|1.743|1.057|212|47|11|0|\n|16107|Quillón|7.432|12|2.391|2.768|1.795|364|76|25|1|\n|16108|San Ignacio|6.533|17|1.883|2.331|1.844|400|45|13|0|\n|16109|Yungay|7.238|9|2.116|2.630|1.902|478|76|26|1|\n|16201|Quirihue|4.586|20|1.424|1.808|1.012|262|42|18|0|\n|16202|Cobquecura|2.276|9|927|779|440|101|13|7|0|\n|16203|Coelemu|5.555|4|1.668|2.013|1.473|305|76|16|0|\n|16204|Ninhue|2.296|4|755|792|603|114|21|7|0|\n|16205|Portezuelo|2.019|3|708|749|439|98|18|4|0|\n|16206|Ránquil|2.586|4|943|956|551|117|12|3|0|\n|16207|Trehuaco|2.317|5|615|957|574|148|15|3|0|\n|16301|San Carlos|20.385|32|5.174|8.307|5.389|1.218|209|55|1|\n|16302|Coihueco|10.350|23|2.749|3.948|2.798|692|108|31|1|\n|16303|Ñiquén|4.869|6|1.771|1.766|1.065|216|38|7|0|\n|16304|San Fabián|2.007|3|566|836|476|107|16|3|0|\n|16305|San Nicolás|5.364|11|1.667|2.009|1.315|295|53|14|0|"
          },
          "hacinamiento_en_viviendas": {
            "ID": "GN-IND-SEC-0047",
            "Title": "Hacinamiento en Viviendas",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Viviendas sin hacinamiento|Viviendas con hacinamiento medio|Viviendas con hacinamiento crítico|Índice de hacinamiento ignorado|\n|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.018.851|330.955|57.332|1.034|\n|16|Ñuble|187.513|179.006|7.773|724|10|\n|16101|Chillán|68.623|65.708|2.653|258|4|\n|16102|Bulnes|8.668|8.235|377|56|0|\n|16103|Chillán Viejo|11.522|10.975|499|47|1|\n|16104|El Carmen|4.966|4.799|154|13|0|\n|16105|Pemuco|3.207|3.033|158|15|1|\n|16106|Pinto|4.714|4.467|228|19|0|\n|16107|Quillón|7.432|7.077|325|29|1|\n|16108|San Ignacio|6.533|6.223|281|29|0|\n|16109|Yungay|7.238|6.967|251|19|1|\n|16201|Quirihue|4.586|4.369|187|30|0|\n|16202|Cobquecura|2.276|2.183|81|12|0|\n|16203|Coelemu|5.555|5.261|277|17|0|\n|16204|Ninhue|2.296|2.226|63|7|0|\n|16205|Portezuelo|2.019|1.946|69|4|0|\n|16206|Ránquil|2.586|2.491|87|8|0|\n|16207|Trehuaco|2.317|2.231|80|6|0|\n|16301|San Carlos|20.385|19.388|919|77|1|\n|16302|Coihueco|10.350|9.821|492|36|1|\n|16303|Ñiquén|4.869|4.621|235|13|0|\n|16304|San Fabián|2.007|1.910|91|6|0|\n|16305|San Nicolás|5.364|5.075|266|23|0|"
          },
          "numero_de_hogares_por_vivienda": {
            "ID": "GN-IND-SEC-0048",
            "Title": "Número de Hogares por Vivienda",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Viviendas con 1 hogar|Viviendas con 2 hogares|Viviendas con 3 hogares|Viviendas con 4 o más hogares|\n|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.254.479|127.917|20.256|5.520|\n|16|Ñuble|187.513|184.986|2.236|248|43|\n|16101|Chillán|68.623|67.463|987|145|28|\n|16102|Bulnes|8.668|8.575|86|5|2|\n|16103|Chillán Viejo|11.522|11.337|158|24|3|\n|16104|El Carmen|4.966|4.925|40|1|0|\n|16105|Pemuco|3.207|3.177|26|3|1|\n|16106|Pinto|4.714|4.659|51|3|1|\n|16107|Quillón|7.432|7.346|81|5|0|\n|16108|San Ignacio|6.533|6.453|74|5|1|\n|16109|Yungay|7.238|7.170|65|3|0|\n|16201|Quirihue|4.586|4.533|50|3|0|\n|16202|Cobquecura|2.276|2.251|22|2|1|\n|16203|Coelemu|5.555|5.482|63|10|0|\n|16204|Ninhue|2.296|2.285|10|1|0|\n|16205|Portezuelo|2.019|1.997|19|2|1|\n|16206|Ránquil|2.586|2.560|23|3|0|\n|16207|Trehuaco|2.317|2.299|17|1|0|\n|16301|San Carlos|20.385|20.129|235|17|4|\n|16302|Coihueco|10.350|10.241|100|9|0|\n|16303|Ñiquén|4.869|4.822|44|2|1|\n|16304|San Fabián|2.007|1.992|15|0|0|\n|16305|San Nicolás|5.364|5.290|70|4|0|"
          },
          "origen_del_agua": {
            "ID": "GN-IND-SEC-0049",
            "Title": "Origen del Agua",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Red pública|Pozo o noria|Camión aljibe|Río, vertiente, estero, canal, lago, agua lluvia, etc|Fuente de origen del agua no declarado|\n|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|5.914.136|263.309|131.141|98.243|1.343|\n|16|Ñuble|187.513|152.864|27.256|5.049|2.332|12|\n|16101|Chillán|68.623|63.917|4.322|326|55|3|\n|16102|Bulnes|8.668|6.691|1.737|216|24|0|\n|16103|Chillán Viejo|11.522|10.054|1.029|411|27|1|\n|16104|El Carmen|4.966|2.715|1.720|293|238|0|\n|16105|Pemuco|3.207|2.369|670|147|20|1|\n|16106|Pinto|4.714|2.998|1.139|177|400|0|\n|16107|Quillón|7.432|4.464|2.611|278|79|0|\n|16108|San Ignacio|6.533|4.313|2.044|145|31|0|\n|16109|Yungay|7.238|5.719|1.222|222|73|2|\n|16201|Quirihue|4.586|3.574|496|352|164|0|\n|16202|Cobquecura|2.276|1.242|480|196|358|0|\n|16203|Coelemu|5.555|3.865|985|390|315|0|\n|16204|Ninhue|2.296|704|1.003|538|50|1|\n|16205|Portezuelo|2.019|1.494|340|149|36|0|\n|16206|Ránquil|2.586|1.675|676|142|93|0|\n|16207|Trehuaco|2.317|1.356|731|146|84|0|\n|16301|San Carlos|20.385|17.783|2.073|492|35|2|\n|16302|Coihueco|10.350|8.036|2.012|209|92|1|\n|16303|Ñiquén|4.869|3.914|871|66|17|1|\n|16304|San Fabián|2.007|1.830|54|7|116|0|\n|16305|San Nicolás|5.364|4.151|1.041|147|25|0|"
          },
          "sistema_de_distribucion_del_agua": {
            "ID": "GN-IND-SEC-0050",
            "Title": "Sistema de Distribución del Agua",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Con llave dentro de la vivienda|Con llave dentro del sitio, pero fuera de la vivienda|No tiene sistema, la acarrea|Sistema de distribución del agua no declarado|\n|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.196.815|160.098|49.617|1.642|\n|16|Ñuble|187.513|181.464|4.530|1.493|26|\n|16101|Chillán|68.623|67.418|1.083|117|5|\n|16102|Bulnes|8.668|8.375|230|63|0|\n|16103|Chillán Viejo|11.522|11.232|220|66|4|\n|16104|El Carmen|4.966|4.580|250|136|0|\n|16105|Pemuco|3.207|3.048|104|53|2|\n|16106|Pinto|4.714|4.552|117|43|2|\n|16107|Quillón|7.432|7.077|244|109|2|\n|16108|San Ignacio|6.533|6.232|199|102|0|\n|16109|Yungay|7.238|6.927|235|73|3|\n|16201|Quirihue|4.586|4.329|182|75|0|\n|16202|Cobquecura|2.276|2.138|106|31|1|\n|16203|Coelemu|5.555|5.391|141|23|0|\n|16204|Ninhue|2.296|2.053|176|67|0|\n|16205|Portezuelo|2.019|1.894|80|45|0|\n|16206|Ránquil|2.586|2.413|139|34|0|\n|16207|Trehuaco|2.317|2.174|107|36|0|\n|16301|San Carlos|20.385|19.786|409|189|1|\n|16302|Coihueco|10.350|10.053|219|77|1|\n|16303|Ñiquén|4.869|4.698|107|59|5|\n|16304|San Fabián|2.007|1.949|46|12|0|\n|16305|San Nicolás|5.364|5.145|136|83|0|"
          },
          "disponibilidad_de_servicio_higienico": {
            "ID": "GN-IND-SEC-0051",
            "Title": "Disponibilidad de Servicio Higiénico",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Dentro de la vivienda, conectado a una red de alcantarillado|Fuera de la vivienda, conectado a una red de alcantarillado|Conectado a una fosa séptica|Conectado a pozo negro (letrina sanitaria o cajón)|En un cajón sobre acequia o canal|En un cajón conectado a otro sistema|Baño químico|Conectado a baño seco|No tiene servicio higiénico|Sistema de servicio higiénico no declarado|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|5.344.651|104.723|767.214|164.499|3.868|2.310|2.141|2.443|14.794|1.529|\n|16|Ñuble|187.513|118.847|2.173|59.820|5.690|105|126|58|106|568|20|\n|16101|Chillán|68.623|60.017|611|7.479|381|20|12|14|7|71|11|\n|16102|Bulnes|8.668|5.082|119|3.138|281|3|1|1|3|40|0|\n|16103|Chillán Viejo|11.522|9.551|170|1.618|148|0|2|3|5|24|1|\n|16104|El Carmen|4.966|1.969|78|2.371|498|5|21|0|10|14|0|\n|16105|Pemuco|3.207|1.722|41|1.245|168|5|8|0|2|15|1|\n|16106|Pinto|4.714|1.624|94|2.737|218|7|6|2|13|13|0|\n|16107|Quillón|7.432|3.535|71|3.531|242|10|4|2|2|34|1|\n|16108|San Ignacio|6.533|2.427|74|3.538|451|2|10|0|1|28|2|\n|16109|Yungay|7.238|4.055|143|2.724|270|0|7|2|3|33|1|\n|16201|Quirihue|4.586|3.246|102|1.000|214|1|7|1|2|13|0|\n|16202|Cobquecura|2.276|747|23|1.337|144|0|2|1|11|11|0|\n|16203|Coelemu|5.555|3.105|214|2.012|191|8|5|1|3|15|1|\n|16204|Ninhue|2.296|730|33|1.312|181|2|6|0|5|27|0|\n|16205|Portezuelo|2.019|782|17|1.075|120|1|0|1|4|19|0|\n|16206|Ránquil|2.586|594|34|1.806|124|5|2|2|1|18|0|\n|16207|Trehuaco|2.317|1.094|37|1.058|112|3|1|0|1|11|0|\n|16301|San Carlos|20.385|12.586|179|6.925|600|15|11|14|14|40|1|\n|16302|Coihueco|10.350|3.409|48|6.136|692|6|9|1|1|48|0|\n|16303|Ñiquén|4.869|989|32|3.405|373|5|7|5|4|49|0|\n|16304|San Fabián|2.007|63|5|1.817|104|2|2|0|5|9|0|\n|16305|San Nicolás|5.364|1.520|48|3.556|178|5|3|8|9|36|1|"
          },
          "disponibilidad_de_energia_electrica": {
            "ID": "GN-IND-SEC-0052",
            "Title": "Disponibilidad de Energía Eléctrica",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|Red pública|Generador con diésel o bencina|Placa solar|Energía eólica (viento)|Otro|No tiene energía eléctrica|Fuente de energía eléctrica no declarada|\n|-|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.316.147|16.021|32.343|695|16.430|24.917|1.619|\n|16|Ñuble|187.513|185.063|400|548|13|431|1.034|24|\n|16101|Chillán|68.623|68.262|65|89|7|81|108|11|\n|16102|Bulnes|8.668|8.534|17|17|1|33|66|0|\n|16103|Chillán Viejo|11.522|11.389|28|30|0|24|50|1|\n|16104|El Carmen|4.966|4.866|22|28|1|10|39|0|\n|16105|Pemuco|3.207|3.102|24|18|0|10|51|2|\n|16106|Pinto|4.714|4.655|10|16|0|8|25|0|\n|16107|Quillón|7.432|7.315|18|23|1|13|61|1|\n|16108|San Ignacio|6.533|6.430|20|14|0|23|46|0|\n|16109|Yungay|7.238|7.085|18|23|0|38|72|2|\n|16201|Quirihue|4.586|4.507|20|16|0|7|36|0|\n|16202|Cobquecura|2.276|2.216|7|22|0|4|27|0|\n|16203|Coelemu|5.555|5.471|13|11|0|25|35|0|\n|16204|Ninhue|2.296|2.231|6|15|0|13|31|0|\n|16205|Portezuelo|2.019|1.979|2|8|1|6|23|0|\n|16206|Ránquil|2.586|2.542|7|10|0|7|20|0|\n|16207|Trehuaco|2.317|2.274|5|14|0|7|17|0|\n|16301|San Carlos|20.385|20.174|43|50|1|30|83|4|\n|16302|Coihueco|10.350|10.172|14|40|0|42|80|2|\n|16303|Ñiquén|4.869|4.725|12|19|0|16|96|1|\n|16304|San Fabián|2.007|1.964|6|20|0|2|15|0|\n|16305|San Nicolás|5.364|5.170|43|65|1|32|53|0|"
          },
          "sistema_de_eliminacion_de_basura": {
            "ID": "GN-IND-SEC-0053",
            "Title": "Sistema de Eliminación de Basura",
            "Content": "\n|Código comuna|Comuna|Viviendas particulares ocupadas con moradores presentes|La recogen los servicios de aseo|La entierra y/o quema|La deja en terreno eriazo, quebrada o zanja|La tira al río, laguna o mar|Otro|Medio de eliminación de basura no declarado|\n|-|-|-|-|-|-|-|-|-|\n|0|País|6.408.172|6.221.171|111.904|14.058|1.009|58.798|1.232|\n|16|Ñuble|187.513|178.845|6.362|497|22|1.771|16|\n|16101|Chillán|68.623|68.249|187|45|7|132|3|\n|16102|Bulnes|8.668|8.434|153|22|1|57|1|\n|16103|Chillán Viejo|11.522|11.263|106|13|1|135|4|\n|16104|El Carmen|4.966|4.306|601|22|1|36|0|\n|16105|Pemuco|3.207|3.042|144|7|0|13|1|\n|16106|Pinto|4.714|4.471|169|12|0|62|0|\n|16107|Quillón|7.432|6.943|343|68|1|76|1|\n|16108|San Ignacio|6.533|6.011|461|21|0|39|1|\n|16109|Yungay|7.238|6.958|181|13|0|85|1|\n|16201|Quirihue|4.586|4.158|330|33|1|64|0|\n|16202|Cobquecura|2.276|1.859|334|11|0|72|0|\n|16203|Coelemu|5.555|5.351|180|7|1|16|0|\n|16204|Ninhue|2.296|1.497|658|53|0|88|0|\n|16205|Portezuelo|2.019|1.844|140|27|0|8|0|\n|16206|Ránquil|2.586|2.345|154|9|1|77|0|\n|16207|Trehuaco|2.317|1.693|548|13|0|63|0|\n|16301|San Carlos|20.385|19.296|789|80|5|211|4|\n|16302|Coihueco|10.350|9.999|265|15|0|71|0|\n|16303|Ñiquén|4.869|4.521|321|12|1|14|0|\n|16304|San Fabián|2.007|1.930|46|3|0|28|0|\n|16305|San Nicolás|5.364|4.675|252|11|2|424|0|"
          },
          "tipo_de_vivienda_censada": {
            "ID": "GN-IND-SEC-0054",
            "Title": "Tipo de Vivienda Censada",
            "Content": "\n|Código comuna|Comuna|Viviendas censadas|Casa con acceso directo desde la calle|Casa en condominio cerrado|Departamento en edificio con ascensor|Departamento en edificio sin ascensor|Vivienda tradicional indígena (ruka u otras)|Pieza en casa antigua o conventillo|Mediagua, mejora, vivienda de emergencia, rancho o choza|Móvil (carpa, casa rodante o similar)|Otro tipo de vivienda particular|Viviendas Colectivas|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|0|País|7.642.716|5.397.387|539.897|915.728|664.242|1.967|51.305|27.490|1.557|38.823|4.320|\n|16|Ñuble|234.845|213.761|9.221|2.780|6.675|16|123|564|50|1.516|139|\n|16101|Chillán|81.042|69.092|3.386|2.607|5.484|5|87|96|10|217|58|\n|16102|Bulnes|10.531|9.759|415|80|140|0|3|85|2|43|4|\n|16103|Chillán Viejo|13.027|11.932|388|5|611|0|0|39|10|32|10|\n|16104|El Carmen|6.212|6.139|46|0|1|0|1|9|0|10|6|\n|16105|Pemuco|4.204|3.889|142|0|0|0|0|17|1|153|2|\n|16106|Pinto|7.664|6.844|774|10|4|1|4|5|0|13|9|\n|16107|Quillón|13.489|12.332|1.073|2|0|0|3|38|1|34|6|\n|16108|San Ignacio|7.990|7.802|149|2|0|0|3|20|1|12|1|\n|16109|Yungay|10.342|10.112|154|3|8|2|4|21|0|31|7|\n|16201|Quirihue|5.628|5.375|106|31|14|0|3|47|2|44|6|\n|16202|Cobquecura|3.897|3.778|82|0|0|1|1|6|3|20|6|\n|16203|Coelemu|7.087|6.908|127|0|2|1|3|19|0|25|2|\n|16204|Ninhue|2.908|2.865|29|0|1|0|2|2|0|8|1|\n|16205|Portezuelo|2.700|2.611|33|8|0|0|0|18|0|28|2|\n|16206|Ránquil|3.563|3.220|294|0|0|0|2|9|1|34|3|\n|16207|Trehuaco|3.053|3.014|13|1|0|0|0|12|0|13|0|\n|16301|San Carlos|23.905|21.945|1.041|28|394|2|3|37|13|431|11|\n|16302|Coihueco|12.130|11.519|281|1|6|0|1|25|0|296|1|\n|16303|Ñiquén|6.008|5.518|444|0|5|0|0|11|3|26|1|\n|16304|San Fabián|3.137|2.975|104|1|1|0|0|37|1|17|1|\n|16305|San Nicolás|6.328|6.132|140|1|4|4|3|11|2|29|2|"
          }
        }
      },
      "indicadores_sanitarios": {
        "ID": "GN-IND-SEC-0055",
        "Title": "Indicadores sanitarios",
        "Content": "\nLos datos presentados a continuación, fueron extraídos del Departamento de Estadísticas e Información en Salud (DEIS) del Ministerio de Salud y SINIM desde datos FONASA. Se presenta la cantidad de establecimientos de salud al 12 de enero de 2024, las tasas de fecundidad, natalidad, mortalidad general y mortalidad infantil para el año 2020, la población inscrita validada en servicios de salud municipal al año 2022. Este año se incorpora información sobre la Cobertura de vacunación Bivalente COVID-19.",
        "Sections": {
          "numero_de_establecimientos_de_salud_segun_tipo_version_29_04_2025_fuente_deis_mi": {
            "ID": "GN-IND-SEC-0056",
            "Title": "Número de Establecimientos de Salud, según tipo. Versión 29-04-2025 (Fuente: DEIS, MINSAL)",
            "Content": "\n|Comuna|CECOSF|COSAM|CONIN|CESFAM|PSR|Clínica|Clínica Dental|Dirección Servicio de Salud|Hospital|Laboratorio Clínico|Centro de Salud Privado|Centro de Diálisis|SAPU|SAR|SUR|Servicio Médico Legal|Unidad de Salud Funcionarios|Vacunatorio|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|1|0|0|1|0|0|0|0|1|0|0|1|0|0|1|0|0|0|\n|Chillán|4|2|1|7|2|2|2|1|1|10|8|3|2|2|0|0|1|3|\n|Chillán Viejo|0|0|0|2|2|0|0|0|0|0|0|0|1|1|0|0|0|0|\n|Cobquecura|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Coelemu|0|0|0|0|3|0|0|0|1|0|0|0|0|0|0|0|0|0|\n|Coihueco|0|0|0|2|4|0|0|0|0|0|0|1|0|1|0|0|0|0|\n|El Carmen|0|0|0|0|10|0|0|0|1|0|0|0|0|0|0|0|0|0|\n|Ninhue|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Ñiquén|1|0|0|1|4|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Pemuco|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Pinto|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Portezuelo|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Quillón|1|0|0|1|3|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Quirihue|0|0|0|0|1|0|0|0|1|0|0|0|0|0|0|0|0|0|\n|Ránquil|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|San Carlos|2|1|0|2|5|0|0|0|1|0|0|2|1|0|0|0|0|0|\n|San Fabián|0|0|0|1|2|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|San Ignacio|0|0|0|3|1|0|0|0|0|0|0|0|0|0|2|0|0|0|\n|San Nicolás|0|0|0|1|1|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Treguaco|0|0|0|1|3|0|0|0|0|0|0|0|0|0|1|0|0|0|\n|Yungay|0|0|0|1|1|0|0|0|1|0|0|0|0|0|0|0|0|0|\n|Región de Ñuble|9|3|1|29|54|2|2|1|7|10|8|7|4|4|14|0|1|3|\n|País|293|102|5|602|1111|157|224|29|228|362|697|97|234|97|168|0|29|118|\n\nABREVIATURAS\n\n* CECOSF: Centro Comunitario de Salud Familiar\n* COSAM: Centro Comunitario de Salud Mental\n* CONIN: Centro Corporación para la Nutrición Infantil\n* CESFAM: Centro de Salud Familiar\n* PSR: Posta de Salud Rural\n* SAPU: Servicio de Atención Primaria de Urgencia\n* SAR: Servicio de Atención Primaria de Urgencia de Alta Resolutividad\n* SUR: Servicio de Urgencia Rural\n\nLos siguientes tipos de establecimientos de salud no se encontraron presentes en ninguna comuna de la región:\n\n* Atención Remota\n* Centro de Apoyo Comunitario para personas con Demencia\n* Centro de Diagnóstico y Terapeútico (CDT)\n* Centro de Especialidad\n* Centro de Especialidades Primarias\n* Centro de Referencia de Salud (CRS)\n* Centro de Regulación Médica de las Urgencias (SAMU)\n* Centro de Rehabilitación\n* Centro de Salud\n* Centro de Salud Mental\n* Centro de Tratamiento de Adicciones (CTA)\n* Centro Médico y Dental\n* Centro Radiológico\n* Centros de Diagnóstico y Tratamiento Privados\n* Centros Exclusivos de Atención Respiratoria (CEAR)\n* Consultorio General Rural (CGR)\n* Consultorio General Urbano (CGU)\n* Dispositivo Incorporado por Crisis Sanitaria\n* Especialidades Primarias\n* Hospital de Día Adulto\n* Hospital de Día Infanto Adolescente\n* Laboratorio Clínico o Dental\n* Oficina Sanitaria\n* Policlínico Funcionarios (Minería)\n* Puesto de Atención Médica Especializado (PAME) Incorporado por Crisis Sanitaria\n* Sala Externa de Toma de Muestras (SETM)\n* Unidad de Atención Primaria Oftalmológica (UAPO)\n* Unidad de Procedimientos Móvil\n* Vacunatorio Móvil"
          },
          "poblacion_inscrita_validada_en_servicios_de_salud_municipal_ano_2023_fuente_sini": {
            "ID": "GN-IND-SEC-0057",
            "Title": "Población Inscrita Validada en Servicios de Salud Municipal, año 2023 (Fuente: SINIM, desde datos FONASA)",
            "Content": "\n|Comuna|Población Inscrita|\n|-|-|\n|Bulnes|17185|\n|Chillán|164617|\n|Chillán Viejo|35683|\n|Cobquecura|5740|\n|Coelemu|3607|\n|Coihueco|28282|\n|El Carmen|9363|\n|Ninhue|5863|\n|Ñiquén|11425|\n|Pemuco|8873|\n|Pinto|13637|\n|Portezuelo|5328|\n|Quillón|18926|\n|Quirihue|1315|\n|Ránquil|5926|\n|San Carlos|53946|\n|San Fabián|5202|\n|San Ignacio|18026|\n|San Nicolás|13762|\n|Treguaco|5830|\n|Yungay|5827|\n|Región de Ñuble|438363|\n|País|15051673|"
          },
          "tasa_global_de_fecundidad_c_1000_habitantes_ano_2022_fuente_deis_minsal": {
            "ID": "GN-IND-SEC-0058",
            "Title": "Tasa Global de Fecundidad, c/1000 habitantes, año 2022 (Fuente: DEIS, MINSAL)",
            "Content": "\n|Comuna|Tasa de Fecundidad|\n|-|-|\n|Bulnes|1.7|\n|Chillán|1.4|\n|Chillán Viejo|1.1|\n|Cobquecura|1.3|\n|Coelemu|1.4|\n|Coihueco|1.4|\n|El Carmen|1.3|\n|Ninhue|1.2|\n|Ñiquén|1.4|\n|Pemuco|1.2|\n|Pinto|1.6|\n|Portezuelo|1.0|\n|Quillón|1.2|\n|Quirihue|1.1|\n|Ránquil|1.3|\n|San Carlos|1.5|\n|San Fabián|1.4|\n|San Ignacio|1.5|\n|San Nicolás|1.3|\n|Treguaco|1.2|\n|Yungay|1.2|\n|Región de Ñuble|1.4|\n|País|1.3|"
          },
          "tasa_de_natalidad_c_1000_habitantes_ano_2022_fuente_deis_minsal": {
            "ID": "GN-IND-SEC-0059",
            "Title": "Tasa de Natalidad, c/1000 habitantes, año 2022 (Fuente: DEIS, MINSAL)",
            "Content": "\n|Comuna|Tasa de Natalidad|\n|-|-|\n|Bulnes|11.1|\n|Chillán|10.0|\n|Chillán Viejo|8.7|\n|Cobquecura|7.2|\n|Coelemu|9.2|\n|Coihueco|9.8|\n|El Carmen|8.2|\n|Ninhue|6.7|\n|Ñiquén|8.0|\n|Pemuco|7.7|\n|Pinto|10.6|\n|Portezuelo|5.3|\n|Quillón|7.7|\n|Quirihue|7.0|\n|Ránquil|7.2|\n|San Carlos|10.3|\n|San Fabián|9.7|\n|San Ignacio|9.0|\n|San Nicolás|8.3|\n|Treguaco|7.3|\n|Yungay|7.8|\n|Región de Ñuble|9.4|\n|País|9.6|"
          },
          "tasa_de_mortalidad_general_c_1000_habitantes_ano_2022_fuente_deis_minsal": {
            "ID": "GN-IND-SEC-0060",
            "Title": "Tasa de Mortalidad General, c/1000 habitantes, año 2022 (Fuente: DEIS, MINSAL)",
            "Content": "\n|Comuna|Tasa de Mortalidad General|\n|-|-|\n|Bulnes|10.0|\n|Chillán|7.9|\n|Chillán Viejo|5.8|\n|Cobquecura|10.7|\n|Coelemu|10.0|\n|Coihueco|7.4|\n|El Carmen|10.5|\n|Ninhue|13.0|\n|Ñiquén|9.1|\n|Pemuco|9.6|\n|Pinto|9.4|\n|Portezuelo|12.4|\n|Quillón|9.5|\n|Quirihue|10.6|\n|Ránquil|9.4|\n|San Carlos|10.0|\n|San Fabián|9.3|\n|San Ignacio|10.6|\n|San Nicolás|8.1|\n|Treguaco|9.1|\n|Yungay|10.1|\n|Región de Ñuble|8.7|\n|País|6.9|"
          },
          "tasa_de_mortalidad_infantil_c_1000_nacidos_vivos_anos_2020_fuente_deis_minsal": {
            "ID": "GN-IND-SEC-0061",
            "Title": "Tasa de Mortalidad Infantil, c/1000 nacidos vivos, años 2020 (Fuente: DEIS, MINSAL)",
            "Content": "\n|Comuna|Tasa de Mortalidad Infantil|\n|-|-|\n|Chillán|5.6|\n|Chillán Viejo|5.7|\n|Cobquecura|6.0|\n|Coelemu|5.9|\n|Coihueco|6.2|\n|El Carmen|5.8|\n|Ninhue|6.1|\n|Ñiquén|6.4|\n|Pemuco|6.3|\n|Pinto|5.7|\n|Portezuelo|6.2|\n|Quillón|6.5|\n|Quirihue|5.9|\n|Ránquil|6.0|\n|San Carlos|5.8|\n|San Fabián|6.1|\n|San Ignacio|6.3|\n|San Nicolás|5.8|\n|Treguaco|6.0|\n|Yungay|5.9|\n|Región de Ñuble|5.7|\n|País|5.6|"
          }
        }
      },
      "indicadores_educacionales": {
        "ID": "GN-IND-SEC-0062",
        "Title": "Indicadores educacionales",
        "Content": "\nLos datos presentados a continuación, fueron extraídos de las bases puestas a disposición por el Ministerio de Educación, a través de los portales Datos Abiertos y Centro de Estudios. Se presenta el número de establecimientos educacionales y matrícula escolar según dependencia administrativa y nivel de enseñanza impartidos para los años 2021 y 2023. En esta entrega de Reportes Comunales, se incluye los puntajes de las pruebas SIMCE para 4to básico y 2do medio rendidas en año 2022.",
        "Sections": {
          "numero_de_establecimientos_educacionales_segun_dependencia_administrativa_2022_y": {
            "ID": "GN-IND-SEC-0063",
            "Title": "Número de establecimientos educacionales según dependencia administrativa (2022 y 2024) (Fuente: Centro de Estudios, MINEDUC)",
            "Content": "\n|Comuna|Municipal (2022)|Municipal (2024)|Part. Subvencionado (2022)|Part. Subvencionado (2024)|Part. Pagado (2022)|Part. Pagado (2024)|CAD (2022)|CAD (2024)|SLE (2022)|SLE (2024)|Total (2022)|Total (2024)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|14|14|7|7|0|0|0|0|0|0|21|21|\n|Chillán|34|33|60|58|4|4|4|4|0|0|102|99|\n|Chillán Viejo|7|7|10|9|0|0|0|0|0|0|17|16|\n|Cobquecura|15|15|1|1|0|0|0|0|0|0|16|16|\n|Coelemu|14|14|3|3|0|0|0|0|0|0|17|17|\n|Coihueco|20|0|8|8|0|0|0|0|0|20|28|28|\n|El Carmen|20|20|2|2|0|0|0|0|0|0|22|22|\n|Ninhue|8|8|1|1|0|0|0|0|0|0|9|9|\n|Ñiquén|9|0|1|1|0|0|0|0|0|9|10|10|\n|Pemuco|12|11|2|2|0|0|0|0|0|0|14|13|\n|Pinto|11|0|2|2|0|0|0|0|0|11|13|13|\n|Portezuelo|6|6|1|1|0|0|0|0|0|0|7|7|\n|Quillón|10|10|4|4|0|0|0|0|0|0|14|14|\n|Quirihue|8|8|3|3|0|0|0|0|0|0|11|11|\n|Ránquil|9|8|1|1|0|0|0|0|0|0|10|9|\n|San Carlos|29|0|10|10|0|0|0|0|0|29|39|39|\n|San Fabián|6|0|0|0|0|0|0|0|0|6|6|6|\n|San Ignacio|13|13|3|3|0|0|0|0|0|0|16|16|\n|San Nicolás|8|8|1|1|0|0|0|0|0|0|9|9|\n|Treguaco|11|10|0|0|0|0|0|0|0|0|11|10|\n|Yungay|13|11|4|4|0|0|0|0|0|0|17|15|\n|Región Ñuble|277|196|124|121|4|4|4|4|0|75|409|400|\n|País|4371|4104|5521|5440|618|604|70|70|636|830|11216|11048|"
          },
          "matricula_escolar_segun_dependencia_administrativa_2022_y_2024_fuente_centro_de_": {
            "ID": "GN-IND-SEC-0064",
            "Title": "Matrícula escolar según dependencia administrativa (2022 y 2024) (Fuente: Centro de Estudios, MINEDUC)",
            "Content": "\n|Comuna|Municipal (2022)|Municipal (2024)|Subvencionada (2022)|Subvencionada (2024)|Part. Pagado (2022)|Part. Pagado (2024)|CAD (2022)|CAD (2024)|SLE (2022)|SLE (2024)|Total (2022)|Total (2024)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|2311|2383|2396|2437|0|0|0|0|0|0|4707|4820|\n|Chillán|8139|7802|31058|30541|1131|1279|2022|1846|0|0|42350|41468|\n|Chillán Viejo|1089|1107|3112|2832|0|0|0|0|0|0|4201|3939|\n|Cobquecura|589|654|68|59|0|0|0|0|0|0|657|713|\n|Coelemu|2850|2795|656|631|0|0|0|0|0|0|3506|3426|\n|Coihueco|3026|0|1771|1766|0|0|0|0|0|3008|4797|4774|\n|El Carmen|2447|2445|208|208|0|0|0|0|0|0|2655|2653|\n|Ninhue|750|782|101|86|0|0|0|0|0|0|851|868|\n|Ñiquén|1614|0|134|177|0|0|0|0|0|1492|1748|1669|\n|Pemuco|1205|1209|151|144|0|0|0|0|0|0|1356|1353|\n|Pinto|1254|0|836|779|0|0|0|0|0|1273|2090|2052|\n|Portezuelo|519|532|338|325|0|0|0|0|0|0|857|857|\n|Quillón|2005|1856|1206|1368|0|0|0|0|0|0|3211|3224|\n|Quirihue|1707|1679|563|557|0|0|0|0|0|0|2270|2236|\n|Ránquil|835|887|251|246|0|0|0|0|0|0|1086|1133|\n|San Carlos|4226|0|6679|6700|0|0|0|0|0|4250|10905|10950|\n|San Fabián|916|0|0|0|0|0|0|0|0|974|916|974|\n|San Ignacio|1742|1608|826|965|0|0|0|0|0|0|2568|2573|\n|San Nicolás|3461|3560|53|55|0|0|0|0|0|0|3514|3615|\n|Treguaco|627|618|0|0|0|0|0|0|0|0|627|618|\n|Yungay|1896|1988|1972|1983|0|0|0|0|0|0|3868|3971|\n|Región Ñuble|43208|31905|52379|51859|1131|1279|2022|1846|0|10997|98740|97886|\n|País|1116914|1034121|1972241|1939429|334438|340318|44869|44202|176074|224862|3644536|3582932|"
          },
          "matricula_escolar_segun_nivel_de_ensenanza_impartido_2022_y_2024_fuente_centro_d": {
            "ID": "GN-IND-SEC-0065",
            "Title": "Matrícula escolar según nivel de enseñanza impartido (2022 y 2024) (Fuente: Centro de Estudios, MINEDUC)",
            "Content": "\n|Comuna|Parvularia (2022)|Parvularia (2024)|Básica Niños (2022)|Básica Niños (2024)|Básica Adultos (2022)|Básica Adultos (2024)|Especial (2022)|Especial (2024)|Humanístico-Científica Jóvenes (2022)|Humanístico-Científica Jóvenes (2024)|Técnico Profesional Jóvenes (2022)|Técnico Profesional Jóvenes (2024)|Total (2022)|Total (2024)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|318|337|2599|2620|-|16|287|297|1208|1247|251|291|4707|4820|\n|Chillán|3842|4068|22448|21915|94|117|2429|2299|10135|10441|2229|1958|42350|41468|\n|Chillán Viejo|279|312|2551|2348|19|11|455|326|490|640|288|244|4201|3939|\n|Cobquecura|47|32|433|453|-|0|76|63|82|108|34|42|657|713|\n|Coelemu|290|308|1937|1932|-|0|219|189|900|910|118|86|3506|3426|\n|Coihueco|458|503|3061|3039|-|0|302|281|657|767|221|229|4797|4774|\n|El Carmen|220|218|1506|1526|-|0|123|111|688|694|97|71|2655|2653|\n|Ninhue|90|101|505|513|-|0|8|4|59|62|178|199|851|868|\n|Ñiquén|155|182|1150|1100|-|0|110|93|228|222|78|99|1748|1669|\n|Pemuco|164|137|805|788|23|20|86|74|252|230|5|27|1356|1353|\n|Pinto|176|161|1137|1082|-|0|126|131|348|364|318|299|2090|2052|\n|Portezuelo|95|110|497|499|-|0|-|0|250|263|-|0|857|857|\n|Quillón|234|266|1979|1984|-|0|288|262|529|639|149|105|3211|3224|\n|Quirihue|143|150|1231|1143|18|23|185|185|395|452|291|290|2270|2236|\n|Ránquil|128|129|664|702|-|0|29|10|181|232|83|61|1086|1133|\n|San Carlos|1055|1028|6024|5881|18|26|461|511|1785|1809|1446|1554|10905|10950|\n|San Fabián|108|89|597|596|-|0|5|5|189|223|36|42|916|974|\n|San Ignacio|250|260|1407|1432|10|7|122|129|387|386|292|318|2568|2573|\n|San Nicolás|284|260|1845|1909|21|10|53|55|1023|1007|260|286|3514|3615|\n|Treguaco|29|32|314|291|-|0|32|29|151|190|98|79|627|618|\n|Yungay|366|386|2165|2172|15|16|185|168|828|941|241|253|3868|3971|\n|Región Ñuble|9069|8731|54855|53925|218|246|5581|5222|20765|21827|6713|6533|98740|97886|\n|País|352678|323073|2052053|1998308|15065|15499|178744|172275|705105|742516|241663|241425|3644536|3582928|"
          },
          "puntaje_prueba_simce_2024_fuente_agencia_de_la_educacion_mineduc": {
            "ID": "GN-IND-SEC-0066",
            "Title": "Puntaje Prueba SIMCE (2024) (Fuente: Agencia de la Educación, MINEDUC)",
            "Content": "\n|Comuna|Lectura (4to básico)|Matemática (4to básico)|Lectura (6to básico)|Matemática (6to básico)|Lectura (2do medio)|Matemática (2do medio)|\n|-|-|-|-|-|-|-|\n|Bulnes|260|254|236|229|232|236|\n|Chillán|282|270|253|247|253|267|\n|Chillán Viejo|275|260|254|240|247|247|\n|Cobquecura|255|263|246|236|232|230|\n|Coelemu|279|268|246|239|242|241|\n|Coihueco|276|272|250|248|244|252|\n|El Carmen|283|273|244|237|241|255|\n|Ninhue|254|245|238|238|240|239|\n|Ñiquén|272|259|231|238|231|237|\n|Pemuco|264|252|236|221|223|218|\n|Pinto|285|269|250|234|243|238|\n|Portezuelo|279|266|230|230|209|222|\n|Quillón|284|270|251|236|239|261|\n|Quirihue|284|266|234|234|264|273|\n|Ránquil|286|268|245|241|229|241|\n|San Carlos|279|273|247|246|246|267|\n|San Fabián|285|255|235|236|237|228|\n|San Ignacio|270|261|234|231|221|229|\n|San Nicolás|315|308|275|292|296|344|\n|Treguaco|270|252|246|229|242|236|\n|Yungay|267|251|249|243|241|258|\n|Región Ñuble|279|268|249|244|279|-|\n|País|278|264|249|245|249|259|"
          },
          "alfabetismo_de_la_poblacion_de_5_anos_y_mas_por_grupos_de_edad_censo_2024": {
            "ID": "GN-IND-SEC-0067",
            "Title": "Alfabetismo de la población de 5 años y más por grupos de edad (Censo 2024)",
            "Content": "\n|Código comuna|Comuna|Sabe leer y escribir|Población de 5 años o más|5-14 años|15-64 años|65 años o más|\n|-|-|-|-|-|-|-|\n|0|País|Total País|17.609.739|2.403.955|12.618.546|2.587.238|\n|0|País|Sí|16.768.987|1.988.549|12.377.415|2.403.023|\n|0|País|No|725.878|395.026|166.492|164.360|\n|0|País|Sabe leer y escribir no declarado|114.874|20.380|74.639|19.855|\n|16|Ñuble|Total Región|488.842|63.849|339.759|85.234|\n|16|Ñuble|Sí|457.226|52.174|329.995|75.057|\n|16|Ñuble|No|29.713|11.273|8.580|9.860|\n|16|Ñuble|Sabe leer y escribir no declarado|1.903|402|1.184|317|\n|16101|Chillán|Total Comuna|181.437|24.176|128.445|28.816|\n|16101|Chillán|Sí|172.564|19.801|125.921|26.842|\n|16101|Chillán|No|8.002|4.218|1.946|1.838|\n|16101|Chillán|Sabe leer y escribir no declarado|871|157|578|136|\n|16102|Bulnes|Total Comuna|22.749|3.025|15.611|4.113|\n|16102|Bulnes|Sí|21.142|2.471|15.090|3.581|\n|16102|Bulnes|No|1.547|539|482|526|\n|16102|Bulnes|Sabe leer y escribir no declarado|60|15|39|6|\n|16103|Chillán Viejo|Total Comuna|31.105|4.429|22.541|4.135|\n|16103|Chillán Viejo|Sí|29.408|3.599|22.048|3.761|\n|16103|Chillán Viejo|No|1.580|791|424|365|\n|16103|Chillán Viejo|Sabe leer y escribir no declarado|117|39|69|9|\n|16104|El Carmen|Total Comuna|12.581|1.590|8.698|2.293|\n|16104|El Carmen|Sí|11.652|1.276|8.442|1.934|\n|16104|El Carmen|No|895|313|249|333|\n|16104|El Carmen|Sabe leer y escribir no declarado|34|1|7|26|\n|16105|Pemuco|Total Comuna|8.492|1.079|5.910|1.503|\n|16105|Pemuco|Sí|7.828|861|5.726|1.241|\n|16105|Pemuco|No|635|213|165|257|\n|16105|Pemuco|Sabe leer y escribir no declarado|29|5|19|5|\n|16106|Pinto|Total Comuna|11.914|1.418|8.259|2.237|\n|16106|Pinto|Sí|11.169|1.178|8.039|1.952|\n|16106|Pinto|No|686|233|214|239|\n|16106|Pinto|Sabe leer y escribir no declarado|59|7|6|46|\n|16107|Quillón|Total Comuna|18.379|2.226|12.100|4.053|\n|16107|Quillón|Sí|17.018|1.839|11.639|3.540|\n|16107|Quillón|No|1.261|366|400|495|\n|16107|Quillón|Sabe leer y escribir no declarado|100|21|61|18|\n|16108|San Ignacio|Total Comuna|16.656|2.043|11.443|3.170|\n|16108|San Ignacio|Sí|15.277|1.624|10.956|2.697|\n|16108|San Ignacio|No|1.329|402|455|472|\n|16108|San Ignacio|Sabe leer y escribir no declarado|50|17|32|1|\n|16109|Yungay|Total Comuna|17.914|2.299|12.246|3.369|\n|16109|Yungay|Sí|16.821|1.848|11.986|2.987|\n|16109|Yungay|No|1.037|438|228|371|\n|16109|Yungay|Sabe leer y escribir no declarado|56|13|32|11|\n|16201|Quirihue|Total Comuna|11.233|1.402|7.604|2.227|\n|16201|Quirihue|Sí|10.417|1.185|7.327|1.905|\n|16201|Quirihue|No|804|214|271|319|\n|16201|Quirihue|Sabe leer y escribir no declarado|12|3|6|3|\n|16202|Cobquecura|Total Comuna|5.291|534|3.466|1.291|\n|16202|Cobquecura|Sí|4.815|437|3.314|1.064|\n|16202|Cobquecura|No|469|92|150|227|\n|16202|Cobquecura|Sabe leer y escribir no declarado|7|5|2|0|\n|16203|Coelemu|Total Comuna|15.189|1.991|10.242|2.956|\n|16203|Coelemu|Sí|14.072|1.618|9.916|2.538|\n|16203|Coelemu|No|1.076|360|300|416|\n|16203|Coelemu|Sabe leer y escribir no declarado|41|13|26|2|\n|16204|Ninhue|Total Comuna|5.551|631|3.693|1.227|\n|16204|Ninhue|Sí|4.982|525|3.496|961|\n|16204|Ninhue|No|566|105|195|266|\n|16204|Ninhue|Sabe leer y escribir no declarado|3|1|2|0|\n|16205|Portezuelo|Total Comuna|5.021|556|3.341|1.124|\n|16205|Portezuelo|Sí|4.534|460|3.141|933|\n|16205|Portezuelo|No|483|95|197|191|\n|16205|Portezuelo|Sabe leer y escribir no declarado|4|1|3|0|\n|16206|Ránquil|Total Comuna|6.249|790|3.975|1.484|\n|16206|Ránquil|Sí|5.758|642|3.838|1.278|\n|16206|Ránquil|No|475|141|130|204|\n|16206|Ránquil|Sabe leer y escribir no declarado|16|7|7|2|\n|16207|Trehuaco|Total Comuna|5.866|687|4.007|1.172|\n|16207|Trehuaco|Sí|5.350|568|3.822|960|\n|16207|Trehuaco|No|509|118|182|209|\n|16207|Trehuaco|Sabe leer y escribir no declarado|7|1|3|3|\n|16301|San Carlos|Total Comuna|53.247|6.906|36.832|9.509|\n|16301|San Carlos|Sí|49.483|5.631|35.720|8.132|\n|16301|San Carlos|No|3.558|1.229|987|1.342|\n|16301|San Carlos|Sabe leer y escribir no declarado|206|46|125|35|\n|16302|Coihueco|Total Comuna|28.276|4.002|20.041|4.233|\n|16302|Coihueco|Sí|25.881|3.247|19.138|3.496|\n|16302|Coihueco|No|2.259|727|799|733|\n|16302|Coihueco|Sabe leer y escribir no declarado|136|28|104|4|\n|16303|Ñiquén|Total Comuna|12.292|1.471|8.040|2.781|\n|16303|Ñiquén|Sí|11.234|1.220|7.662|2.352|\n|16303|Ñiquén|No|1.027|245|357|425|\n|16303|Ñiquén|Sabe leer y escribir no declarado|31|6|21|4|\n|16304|San Fabián|Total Comuna|4.994|699|3.335|960|\n|16304|San Fabián|Sí|4.574|562|3.253|759|\n|16304|San Fabián|No|413|134|78|201|\n|16304|San Fabián|Sabe leer y escribir no declarado|7|3|4|0|\n|16305|San Nicolás|Total Comuna|14.406|1.895|9.930|2.581|\n|16305|San Nicolás|Sí|13.247|1.582|9.521|2.144|\n|16305|San Nicolás|No|1.102|300|371|431|\n|16305|San Nicolás|Sabe leer y escribir no declarado|57|13|38|6|"
          },
          "nivel_educativo_alcanzado_por_la_poblacion_censada_censo_2024": {
            "ID": "GN-IND-SEC-0068",
            "Title": "Nivel educativo alcanzado por la población censada (Censo 2024)",
            "Content": "\n|Código comuna|Comuna|Población censada|Nunca asistió|Diferencial|Parvularia|Básica|Media|Superior|Nivel educativo no declarado|\n|-|-|-|-|-|-|-|-|-|-|\n|0|País|18.480.432|552.698|100.691|821.251|4.432.723|6.745.582|5.711.299|116.188|\n|16|Ñuble|512.289|18.651|2.564|22.237|159.476|184.582|122.943|1.836|\n|16101|Chillán|190.382|5.183|1.175|8.769|44.228|67.752|62.416|859|\n|16102|Bulnes|23.863|885|113|1.051|8.174|8.938|4.647|55|\n|16103|Chillán Viejo|32.688|957|212|1.517|8.418|13.300|8.171|113|\n|16104|El Carmen|13.186|629|46|510|5.531|4.474|1.986|10|\n|16105|Pemuco|8.930|415|22|384|3.458|3.276|1.348|27|\n|16106|Pinto|12.502|456|58|496|4.320|4.650|2.469|53|\n|16107|Quillón|19.165|771|55|734|6.688|7.152|3.668|97|\n|16108|San Ignacio|17.405|712|54|644|7.113|6.219|2.616|47|\n|16109|Yungay|18.680|625|70|787|6.074|7.424|3.641|59|\n|16201|Quirihue|11.746|458|34|489|4.404|3.979|2.374|8|\n|16202|Cobquecura|5.495|278|26|275|2.187|1.590|1.134|5|\n|16203|Coelemu|15.895|687|50|591|5.683|5.591|3.254|39|\n|16204|Ninhue|5.763|280|12|194|2.642|1.749|884|2|\n|16205|Portezuelo|5.203|207|13|192|2.338|1.610|840|3|\n|16206|Ránquil|6.508|254|15|245|2.573|2.265|1.144|12|\n|16207|Trehuaco|6.124|239|18|263|2.550|2.032|1.016|6|\n|16301|San Carlos|55.847|2.488|326|2.366|18.500|21.031|10.938|198|\n|16302|Coihueco|29.766|1.459|128|1.469|11.725|9.783|5.061|141|\n|16303|Ñiquén|12.797|634|63|424|5.656|4.441|1.549|30|\n|16304|San Fabián|5.245|371|16|222|1.653|1.871|1.106|6|\n|16305|San Nicolás|15.099|663|58|615|5.561|5.455|2.681|66|"
          },
          "anos_de_escolaridad_promedio_por_sexo_censo_2024": {
            "ID": "GN-IND-SEC-0069",
            "Title": "Años de escolaridad promedio por sexo (Censo 2024)",
            "Content": "\n|Código comuna|Comuna|Sexo|Años de escolaridad promedio|Años de escolaridad promedio para la población de 18 años o más|\n|-|-|-|-|-|\n|0|País|Total País|10.4|12.1|\n|0|País|Hombre|10.3|12.1|\n|0|País|Mujer|10.5|12.1|\n|16|Ñuble|Total Región|9.6|11.0|\n|16|Ñuble|Hombre|9.4|10.9|\n|16|Ñuble|Mujer|9.8|11.2|\n|16101|Chillán|Total Comuna|10.6|12.3|\n|16101|Chillán|Hombre|10.4|12.3|\n|16101|Chillán|Mujer|10.7|12.3|\n|16102|Bulnes|Total Comuna|9.2|10.5|\n|16102|Bulnes|Hombre|9.0|10.4|\n|16102|Bulnes|Mujer|9.3|10.6|\n|16103|Chillán Viejo|Total Comuna|9.9|11.6|\n|16103|Chillán Viejo|Hombre|9.7|11.5|\n|16103|Chillán Viejo|Mujer|10.1|11.7|\n|16104|El Carmen|Total Comuna|8.6|9.7|\n|16104|El Carmen|Hombre|8.3|9.4|\n|16104|El Carmen|Mujer|8.8|9.9|\n|16105|Pemuco|Total Comuna|8.7|9.9|\n|16105|Pemuco|Hombre|8.4|9.6|\n|16105|Pemuco|Mujer|8.9|10.1|\n|16106|Pinto|Total Comuna|9.2|10.5|\n|16106|Pinto|Hombre|9.0|10.2|\n|16106|Pinto|Mujer|9.5|10.7|\n|16107|Quillón|Total Comuna|9.1|10.3|\n|16107|Quillón|Hombre|9.0|10.2|\n|16107|Quillón|Mujer|9.2|10.3|\n|16108|San Ignacio|Total Comuna|8.6|9.7|\n|16108|San Ignacio|Hombre|8.4|9.5|\n|16108|San Ignacio|Mujer|8.8|9.9|\n|16109|Yungay|Total Comuna|9.3|10.6|\n|16109|Yungay|Hombre|9.2|10.6|\n|16109|Yungay|Mujer|9.4|10.6|\n|16201|Quirihue|Total Comuna|9.0|10.2|\n|16201|Quirihue|Hombre|8.7|9.8|\n|16201|Quirihue|Mujer|9.3|10.5|\n|16202|Cobquecura|Total Comuna|8.9|9.8|\n|16202|Cobquecura|Hombre|8.5|9.4|\n|16202|Cobquecura|Mujer|9.3|10.2|\n|16203|Coelemu|Total Comuna|9.1|10.3|\n|16203|Coelemu|Hombre|8.8|10.1|\n|16203|Coelemu|Mujer|9.3|10.5|\n|16204|Ninhue|Total Comuna|8.4|9.3|\n|16204|Ninhue|Hombre|8.2|9.0|\n|16204|Ninhue|Mujer|8.6|9.6|\n|16205|Portezuelo|Total Comuna|8.4|9.3|\n|16205|Portezuelo|Hombre|8.2|9.1|\n|16205|Portezuelo|Mujer|8.6|9.6|\n|16206|Ránquil|Total Comuna|8.8|9.9|\n|16206|Ránquil|Hombre|8.6|9.8|\n|16206|Ránquil|Mujer|9.0|10.1|\n|16207|Trehuaco|Total Comuna|8.7|9.8|\n|16207|Trehuaco|Hombre|8.4|9.5|\n|16207|Trehuaco|Mujer|9.1|10.1|\n|16301|San Carlos|Total Comuna|9.2|10.5|\n|16301|San Carlos|Hombre|9.0|10.4|\n|16301|San Carlos|Mujer|9.4|10.7|\n|16302|Coihueco|Total Comuna|8.7|10.0|\n|16302|Coihueco|Hombre|8.4|9.7|\n|16302|Coihueco|Mujer|8.9|10.3|\n|16303|Ñiquén|Total Comuna|8.3|9.2|\n|16303|Ñiquén|Hombre|8.1|9.0|\n|16303|Ñiquén|Mujer|8.5|9.5|\n|16304|San Fabián|Total Comuna|9.1|10.5|\n|16304|San Fabián|Hombre|8.9|10.3|\n|16304|San Fabián|Mujer|9.4|10.7|\n|16305|San Nicolás|Total Comuna|8.9|10.1|\n|16305|San Nicolás|Hombre|8.7|9.9|\n|16305|San Nicolás|Mujer|9.1|10.3|"
          },
          "tasa_de_asistencia_neta_por_nivel_educativo_censo_2024": {
            "ID": "GN-IND-SEC-0070",
            "Title": "Tasa de asistencia neta por nivel educativo (Censo 2024)",
            "Content": "\n|Código comuna|Comuna|Tasa de asistencia neta Educación Parvularia|Tasa de asistencia neta Educación Básica|Tasa de asistencia neta Educación Media|Tasa de asistencia neta Educación Superior|\n|-|-|-|-|-|-|\n|0|País|52.3|95.4|87.4|46.6|\n|16|Ñuble|51.6|95.3|88.7|45.9|\n|16101|Chillán|55.5|95.7|88.9|51.7|\n|16102|Bulnes|53.0|95.1|87.5|42.5|\n|16103|Chillán Viejo|52.2|95.3|88.0|46.5|\n|16104|El Carmen|47.1|96.5|90.0|40.8|\n|16105|Pemuco|49.7|94.2|89.2|31.3|\n|16106|Pinto|48.6|94.7|89.6|38.9|\n|16107|Quillón|50.1|94.1|86.6|40.4|\n|16108|San Ignacio|45.5|94.0|88.7|40.0|\n|16109|Yungay|51.3|95.4|88.4|41.7|\n|16201|Quirihue|59.9|95.7|88.9|46.6|\n|16202|Cobquecura|45.8|95.0|90.6|34.0|\n|16203|Coelemu|46.4|94.4|89.7|46.5|\n|16204|Ninhue|43.0|96.5|87.5|50.9|\n|16205|Portezuelo|55.1|95.3|92.5|39.9|\n|16206|Ránquil|40.4|93.1|88.8|36.5|\n|16207|Trehuaco|55.5|96.2|92.8|41.0|\n|16301|San Carlos|48.6|95.5|89.7|43.1|\n|16302|Coihueco|47.3|94.9|87.0|39.8|\n|16303|Ñiquén|43.3|95.7|88.8|39.2|\n|16304|San Fabián|44.2|94.4|86.8|36.7|\n|16305|San Nicolás|47.9|95.2|86.8|43.3|"
          }
        }
      },
      "indicadores_economicos": {
        "ID": "GN-IND-SEC-0071",
        "Title": "Indicadores económicos",
        "Content": "\nLos datos presentados a continuación, fueron extraídos desde las Estadísticas de Empresa del Servicio de Impuestos Internos (SII). Se presenta el número de empresas y número de trabajadores dependientes, según tamaño de empresa y rubro en el cual desarrolla su actividad económica, para los años 2020 y 2021.",
        "Sections": {
          "cantidad_de_empresas_segun_tamano_2021_2022_y_2023_fuente_estadisticas_sii": {
            "ID": "GN-IND-SEC-0072",
            "Title": "Cantidad de empresas según tamaño (2021, 2022 y 2023) (Fuente: Estadísticas SII)",
            "Content": "\n|Comuna|Micro (2021)|Micro (2022)|Micro (2023)|Pequeña (2021)|Pequeña (2022)|Pequeña (2023)|Mediana (2021)|Mediana (2022)|Mediana (2023)|Grande (2021)|Grande (2022)|Grande (2023)|Sin ventas/Sin información (2021)|Sin ventas/Sin información (2022)|Sin ventas/Sin información (2023)|Total (2021)|Total (2022)|Total (2023)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|955|1008|1079|250|257|240|31|30|31|14|17|16|345|359|324|1595|1671|1690|\n|Chillán|9180|9571|9706|2442|2548|2515|292|307|302|88|99|85|3149|3151|2838|15151|15676|15446|\n|Chillán Viejo|971|1079|1097|218|209|219|36|35|31|18|18|20|307|304|296|1550|1645|1663|\n|Cobquecura|215|221|250|29|31|28|0|1|0|0|0|0|62|61|65|306|314|343|\n|Coelemu|756|821|871|177|183|174|25|25|25|8|9|9|221|232|224|1187|1270|1303|\n|Coihueco|1213|1284|1373|335|387|335|33|36|29|3|4|6|466|436|461|2050|2147|2204|\n|El Carmen|692|733|772|140|147|141|11|16|11|4|3|2|213|201|195|1060|1100|1121|\n|Ninhue|207|215|238|31|35|28|3|2|2|0|0|0|41|50|45|282|302|313|\n|Ñiquén|684|698|728|102|103|99|6|7|8|0|1|2|201|210|174|993|1019|1011|\n|Pemuco|305|334|340|61|66|66|3|2|3|1|3|2|113|99|101|483|504|512|\n|Pinto|726|770|799|146|171|165|17|11|12|2|4|1|214|231|217|1105|1187|1194|\n|Portezuelo|209|237|241|38|35|32|3|3|3|0|0|1|55|57|52|305|332|329|\n|Quillón|959|1007|1089|193|188|177|13|15|11|1|3|1|257|302|289|1423|1515|1567|\n|Quirihue|461|517|532|120|118|120|8|6|8|3|5|3|190|185|189|782|831|852|\n|Ránquil|329|336|329|32|32|32|2|3|4|4|5|4|61|81|83|428|457|452|\n|San Carlos|3206|3277|3352|608|633|595|66|59|54|11|15|16|872|883|815|4763|4867|4832|\n|San Fabián|241|253|269|36|42|44|4|3|4|0|1|1|62|69|75|343|368|393|\n|San Ignacio|724|750|778|140|154|152|13|13|16|6|4|2|208|206|197|1091|1127|1145|\n|San Nicolás|583|633|652|97|92|103|6|13|8|3|1|2|164|157|163|853|896|928|\n|Treguaco|178|182|186|33|32|31|1|6|8|4|3|3|50|54|60|266|277|288|\n|Yungay|730|731|814|152|163|147|18|18|18|3|3|3|242|264|237|1145|1179|1219|\n|Región Ñuble|23524|24657|25495|5380|5626|5443|591|611|588|173|198|179|7493|7592|7100|37161|38684|38805|\n|País|830292|875571|905520|244596|257671|251469|37733|39517|37266|18231|18680|17341|316823|320157|291977|1447675|1511596|1503573|"
          },
          "numero_de_trabajadores_dependientes_informados_segun_tamano_de_la_empresa_2021_2": {
            "ID": "GN-IND-SEC-0073",
            "Title": "Número de trabajadores dependientes informados según tamaño de la empresa (2021, 2022, 2023) (Fuente: Estadísticas SII)",
            "Content": "\n|Comuna|Micro (2021)|Micro (2022)|Micro (2023)|Pequeña (2021)|Pequeña (2022)|Pequeña (2023)|Mediana (2021)|Mediana (2022)|Mediana (2023)|Grande (2021)|Grande (2022)|Grande (2023)|Sin ventas/Sin información (2021)|Sin ventas/Sin información (2022)|Sin ventas/Sin información (2023)|Total (2021)|Total (2022)|Total (2023)|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|742|727|742|2002|1572|1465|1318|1648|1304|2563|2512|2123|1017|1098|1142|7642|7557|6776|\n|Chillán|6963|6254|6252|22263|20619|19148|16379|19025|17918|19460|21400|19050|5858|6755|7209|70923|74053|69577|\n|Chillán Viejo|648|664|442|1437|1522|1674|1498|1671|1311|2992|2863|3066|890|1015|1134|7465|7735|7627|\n|Cobquecura|122|129|82|153|139|126|0|1|0|0|0|0|505|514|518|780|783|726|\n|Coelemu|1441|1439|1479|879|896|1078|564|790|812|851|929|1282|7|14|7|3742|4068|4658|\n|Coihueco|607|808|900|3505|3743|2839|2753|2453|1856|5839|6252|5721|1243|1179|1321|13947|14435|12637|\n|El Carmen|472|456|443|767|874|759|859|532|505|471|913|536|858|940|970|3427|3715|3213|\n|Ninhue|100|53|55|162|314|299|43|34|26|0|0|0|385|386|438|690|787|818|\n|Ñiquén|740|818|845|692|751|635|81|93|149|0|0|0|34|44|51|1547|1706|1680|\n|Pemuco|321|269|101|303|256|289|20|14|11|437|561|470|387|444|654|1468|1544|1525|\n|Pinto|419|494|344|584|703|914|606|655|1423|1403|1691|581|835|718|891|3847|4261|4153|\n|Portezuelo|122|107|140|415|440|380|67|91|72|0|0|83|263|296|313|867|934|988|\n|Quillón|443|414|380|1084|1080|881|110|124|290|27|0|41|780|874|988|2444|2492|2580|\n|Quirihue|496|485|573|1562|1541|1563|241|53|98|275|325|499|290|316|328|2864|2720|3061|\n|Ránquil|92|50|67|139|181|146|62|41|150|484|538|438|405|450|490|1182|1260|1291|\n|San Carlos|2779|2536|2667|5627|4673|3463|2880|2882|2951|4287|3664|3008|2183|2719|2419|17756|16474|14508|\n|San Fabián|164|149|143|218|493|331|364|92|25|0|6|0|462|490|489|1208|1230|988|\n|San Ignacio|400|328|1341|1385|1682|1545|950|352|446|689|432|66|1148|1237|157|4572|4031|3555|\n|San Nicolás|426|607|359|1585|1142|958|322|495|211|277|254|336|744|807|859|3354|3305|2723|\n|Treguaco|64|53|72|305|313|283|35|170|224|626|552|529|362|378|413|1392|1466|1521|\n|Yungay|618|231|608|921|1305|1024|2200|2050|1493|291|293|404|849|930|1640|4879|4809|5169|\n|Región Ñuble|18179|17071|18035|45988|44239|39800|31352|33266|31275|40972|43185|38233|19505|21604|22431|155996|159365|149774|\n|País|722558|725656|646948|2171938|2153280|2036727|1454623|1563999|1480918|4794592|5045103|4798002|696290|709238|746020|9840001|10197276|9708615|"
          },
          "cantidad_de_empresas_segun_rubro_economico_ano_2023_fuente_estadisticas_sii": {
            "ID": "GN-IND-SEC-0074",
            "Title": "Cantidad de empresas según rubro económico, año 2023 (Fuente: Estadísticas SII)",
            "Content": "\n|Comuna|Agricultura ganadería silvicultura y pesca|Explotación de minas y canteras|Industria manufacturera|Suministro de electricidad gas vapor y aire acondicionado|Suministro de agua; evacuación de aguas residuales gestión de desechos y descontaminación|Construcción|Comercio al por mayor y al por menor; reparación de vehículos automotores y motocicletas|Transporte y almacenamiento|Actividades de alojamiento y de servicio de comidas|Información y comunicaciones|Actividades financieras y de seguros|Actividades inmobiliarias|Actividades profesionales científicas y técnicas|Actividades de servicios administrativos y de apoyo|Administración pública y defensa; planes de seguridad social de afiliación obligatoria|Enseñanza|Actividades de atención de la salud humana y de asistencia social|Actividades artísticas de entretenimiento y recreativas|Otras actividades de servicios|Actividades de los hogares como empleadores; actividades no diferenciadas de los hogares|Actividades de organizaciones y órganos extraterritoriales|Sin información|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|428|8|112|3|16|94|528|205|96|9|21|25|28|34|1|9|17|17|37|0|0|2|\n|Chillán|960|21|1145|18|58|1269|5398|1532|1083|209|144|452|755|625|12|208|639|177|701|0|0|40|\n|Chillán Viejo|101|3|179|5|14|179|574|224|119|17|8|25|46|68|1|18|14|19|45|0|0|4|\n|Cobquecura|47|0|19|0|5|11|99|18|88|3|2|16|8|6|1|3|2|3|11|0|0|1|\n|Coelemu|253|1|129|2|10|44|435|159|89|11|13|18|24|44|1|5|18|7|37|0|0|3|\n|Coihueco|829|0|95|3|21|138|560|189|95|13|16|28|36|75|2|12|13|19|59|0|0|1|\n|El Carmen|473|2|47|1|5|40|296|110|58|4|3|9|14|12|1|5|5|5|31|0|0|0|\n|Ninhue|85|1|17|0|0|20|89|53|22|1|2|1|5|7|1|1|2|2|4|0|0|0|\n|Ñiquén|573|1|39|1|15|38|202|59|28|4|0|3|7|11|2|2|7|3|14|0|0|2|\n|Pemuco|168|0|33|1|9|24|158|42|42|0|0|1|3|11|1|3|4|1|9|0|0|2|\n|Pinto|264|6|75|2|8|71|318|79|183|7|8|47|22|42|1|6|9|17|28|0|0|1|\n|Portezuelo|91|0|47|1|5|16|77|41|9|2|1|4|3|10|0|2|2|0|16|0|0|2|\n|Quillón|331|1|126|0|21|109|500|122|162|6|3|33|24|41|2|7|19|12|43|0|0|5|\n|Quirihue|128|1|50|2|2|38|312|118|72|9|5|7|17|29|0|6|15|10|29|0|0|2|\n|Ránquil|149|2|30|1|10|22|132|33|37|2|0|5|6|8|1|3|1|1|7|0|0|1|\n|San Carlos|1352|6|332|7|38|293|1440|472|240|30|20|75|125|100|3|37|62|31|159|0|0|9|\n|San Fabián|48|1|24|0|7|26|126|17|71|4|3|16|6|11|1|1|5|11|13|0|0|2|\n|San Ignacio|438|1|49|2|18|74|328|111|42|8|5|3|12|17|1|5|4|5|21|0|0|1|\n|San Nicolás|291|3|73|1|22|74|215|77|68|3|4|17|16|28|1|5|5|4|20|0|0|1|\n|Treguaco|57|0|35|1|4|23|89|32|19|1|0|3|7|6|2|0|2|2|5|0|0|0|\n|Yungay|151|3|108|1|16|83|473|109|128|8|1|22|19|28|1|5|14|14|34|0|0|0|\n|Región de Ñuble|7217|61|2764|52|304|2686|12349|3802|2751|351|259|810|1183|1213|36|343|859|360|1323|0|3|79|\n|País|98707|5352|114584|3560|7565|115293|463661|140897|87899|31850|50620|53898|92443|66825|958|20016|49360|16354|78591|7|103|5030|"
          },
          "numero_de_trabajadores_dependientes_informados_segun_rubro_economico_de_la_empre": {
            "ID": "GN-IND-SEC-0075",
            "Title": "Número de trabajadores dependientes informados según rubro económico de la empresa, año 2023 (Fuente: Estadísticas SII)",
            "Content": "\n|Comuna|Agricultura ganadería silvicultura y pesca|Explotación de minas y canteras|Industria manufacturera|Suministro de electricidad gas vapor y aire acondicionado|Suministro de agua; evacuación de aguas residuales gestión de desechos y descontaminación|Construcción|Comercio al por mayor y al por menor; reparación de vehículos automotores y motocicletas|Transporte y almacenamiento|Actividades de alojamiento y de servicio de comidas|Información y comunicaciones|Actividades financieras y de seguros|Actividades inmobiliarias|Actividades profesionales científicas y técnicas|Actividades de servicios administrativos y de apoyo|Administración pública y defensa; planes de seguridad social de afiliación obligatoria|Enseñanza|Actividades de atención de la salud humana y de asistencia social|Actividades artísticas de entretenimiento y recreativas|Otras actividades de servicios|Actividades de los hogares como empleadores; actividades no diferenciadas de los hogares|Actividades de organizaciones y órganos extraterritoriales|Sin información|\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n|Bulnes|1799|103|1096|0|76|194|1342|260|87|4|32|41|33|61|976|261|386|4|21|0|0|0|\n|Chillán|10875|126|5121|308|749|6190|10188|3910|3388|360|135|432|1248|6484|1682|8407|7634|470|1816|0|0|54|\n|Chillán Viejo|427|18|617|0|233|1288|1333|1434|187|42|0|5|85|286|904|716|30|13|8|0|0|1|\n|Cobquecura|38|0|8|0|11|4|43|21|82|3|0|3|0|0|484|19|0|0|10|0|0|0|\n|Coelemu|504|0|251|23|4|332|562|159|160|10|0|18|517|753|862|131|362|0|10|0|0|0|\n|Coihueco|9341|0|177|4|53|468|370|198|58|20|9|5|17|64|986|321|213|319|14|0|0|0|\n|El Carmen|1437|0|19|0|4|57|270|122|38|7|0|4|10|5|946|31|262|0|1|0|0|0|\n|Ninhue|158|0|11|0|0|15|70|40|6|0|0|0|0|77|59|262|2|0|118|0|0|0|\n|Ñiquén|546|2|24|9|23|71|131|68|54|3|0|0|7|8|679|32|16|0|7|0|0|0|\n|Pemuco|217|0|480|0|17|28|78|23|10|0|0|1|0|3|72|381|14|0|201|0|0|0|\n|Pinto|1368|4|42|1|20|136|330|68|1176|8|7|16|6|55|523|148|209|28|8|0|0|0|\n|Portezuelo|329|0|78|0|6|102|50|51|0|4|1|0|1|47|0|231|78|0|10|0|0|0|\n|Quillón|110|0|210|0|33|372|411|110|217|2|0|15|12|84|674|95|218|1|16|0|0|0|\n|Quirihue|454|1|35|0|2|554|1012|59|55|14|1|2|27|226|0|109|267|16|227|0|0|0|\n|Ránquil|136|0|319|0|7|120|62|107|21|0|0|1|4|25|438|50|0|0|1|0|0|0|\n|San Carlos|3225|15|923|0|205|602|3164|628|375|36|5|117|176|302|776|2323|1266|44|316|0|5|5|\n|San Fabián|212|0|10|0|18|68|95|4|75|0|7|8|1|2|476|0|0|7|4|0|0|1|\n|San Ignacio|1699|0|37|0|32|140|318|74|11|1|7|40|4|8|1023|142|4|0|15|0|0|0|\n|San Nicolás|988|0|89|0|38|260|135|45|27|11|0|8|22|48|72|842|136|0|2|0|0|0|\n|Treguaco|180|0|405|0|6|128|249|28|24|0|0|7|4|29|313|0|96|0|2|0|0|0|\n|Yungay|1437|21|435|0|24|312|1280|113|48|23|0|9|37|63|715|308|336|0|8|0|0|0|\n|Región de Ñuble|35480|290|10387|345|1611|11441|21493|7522|6099|548|204|732|2211|8630|12660|14809|11529|902|2815|0|5|61|\n|País|775844|152718|778025|34306|75964|1133791|1346496|548224|486469|227293|228411|70362|366888|1387230|664974|668023|453957|56112|244278|5|799|8446|"
          },
          "distribucion_de_energia_electrica_por_sector_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0076",
            "Title": "Distribución de energía eléctrica por sector, Región de Ñuble (marzo 2025)",
            "Content": "\n|Sector|MWh|% participación|Interanual %|Mensual %|Acumulada %|\n|-|-|-|-|-|-|\n|Residencial|29.908|44.2|0.6|–14.9|–0.8|\n|Comercial|11.246|16.6|3.8|–4.3|1.1|\n|Industrial|8.331|12.3|9.3|–15.8|5.1|\n|Agrícola|5.737|8.5|–0.9|–32.8|9.4|\n|Otros|12.367|18.3|0.8|11.0|6.5|\n|Total|67.589|100|2.0|–11.6|2.4|"
          },
          "generacion_de_energia_electrica_por_fuente_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0077",
            "Title": "Generación de energía eléctrica por fuente, Región de Ñuble (marzo 2025)",
            "Content": "\n|Fuente|MWh|% participación|Interanual %|Mensual %|Acumulada %|\n|-|-|-|-|-|-|\n|Térmica|35.513|42.3|1.9|22.6|5.5|\n|Otras fuentes|48.527|57.7|37.7|–1.2|31.7|\n|Total|84.040|100|19.9|7.6|20.0|"
          },
          "indicadores_laborales_generales_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0078",
            "Title": "Indicadores laborales generales, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Indicador|Valor %|Δ pp|\n|-|-|-|\n|Desocupación|9.6|0.5|\n|Participación|58.8|1.3|\n|Ocupación|53.1|0.9|\n|Ocupación informal|33.0|–3.7|\n|Presión laboral|20.6|2.2|\n|SU1|9.9|0.4|\n|SU2|18.7|1.6|\n|SU3|20.5|–0.5|"
          },
          "tasa_de_desocupacion_por_sexo_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0079",
            "Title": "Tasa de desocupación por sexo, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Sexo|Tasa %|Δ pp|\n|-|-|-|\n|Mujeres|11.0|1.3|\n|Hombres|8.6|–0.2|\n|Total|9.6|0.5|"
          },
          "tasa_de_ocupacion_informal_por_sexo_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0080",
            "Title": "Tasa de ocupación informal por sexo, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Sexo|Tasa %|Δ pp|\n|-|-|-|\n|Mujeres|34.1|–2.2|\n|Hombres|32.2|–4.8|\n|Total|33.0|–3.7|"
          },
          "ocupados_informales_por_tramo_etario_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0081",
            "Title": "Ocupados informales por tramo etario, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Tramo etario|TOI %|Δ pp|Variación ocupados %|\n|-|-|-|-|\n|15–34 años|33.2|1.4|—|\n|35–54 años|27.0|–7.1|–18.5|\n|55 y más|43.1|–4.1|—|\n|Total|33.0|–3.7|–7.7|"
          },
          "tiempo_parcial_en_ocupacion_informal_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0082",
            "Title": "Tiempo parcial en ocupación informal, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Categoría|% informales|Δ %|\n|-|-|-|\n|Tiempo parcial 1–30 h|50.1|–3.7|\n|Voluntario|61.1|–5.4|\n|Involuntario|37.8|3.2|\n|≥ 45 h|4.2|—|"
          },
          "variacion_de_ocupados_por_categoria_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0083",
            "Title": "Variación de ocupados por categoría, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Categoría|Variación % 12 m|\n|-|-|\n|Asalariado formal|6.0|\n|Cuenta propia|6.7|"
          },
          "variacion_de_ocupados_por_actividad_economica_region_de_nuble_ene_mar_2025": {
            "ID": "GN-IND-SEC-0084",
            "Title": "Variación de ocupados por actividad económica, Región de Ñuble (ene-mar 2025)",
            "Content": "\n|Actividad|Variación % 12 m|\n|-|-|\n|Enseñanza|31.3|\n|Industria manufacturera|24.2|\n|Construcción|–16.7|"
          },
          "indicadores_laborales_provincia_de_diguillin_ene_mar_2025": {
            "ID": "GN-IND-SEC-0085",
            "Title": "Indicadores laborales, Provincia de Diguillín (ene-mar 2025)",
            "Content": "\n|Indicador|Valor %|Δ pp|\n|-|-|-|\n|Desocupación|10.4|1.4|\n|Ocupación|54.0|–0.1|\n|Participación|60.3|0.0|"
          },
          "exportaciones_por_sector_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0086",
            "Title": "Exportaciones por sector, Región de Ñuble (marzo 2025)",
            "Content": "\n|Sector|MM US$|Participación %|Variación %|\n|-|-|-|-|\n|Industria|146.4|91.9|42.7|\n|Silvoagropecuario|12.7|8.0|–58.8|\n|Total|159.3|100|19.2|"
          },
          "exportaciones_industriales_por_rama_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0087",
            "Title": "Exportaciones industriales por rama, Región de Ñuble (marzo 2025)",
            "Content": "\n|Rama|MM US$|Participación %|Variación %|\n|-|-|-|-|\n|Alimentos|46.5|29.2|136.5|\n|Forestales|30.7|19.3|42.3|"
          },
          "exportaciones_por_continente_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0088",
            "Title": "Exportaciones por continente, Región de Ñuble (marzo 2025)",
            "Content": "\n|Continente|MM US$|Participación %|Variación %|\n|-|-|-|-|\n|Asia|87.7|55.1|27.7|\n|América|59.6|37.4|3.2|\n|Europa|6.8|4.3|99.7|\n|Oceanía|4.6|2.9|—|\n|África|0.5|0.3|—|\n|Total|159.3|100|19.2|"
          },
          "exportaciones_por_bloque_economico_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0089",
            "Title": "Exportaciones por bloque económico, Región de Ñuble (marzo 2025)",
            "Content": "\n|Bloque|MM US$|Variación %|\n|-|-|-|\n|APEC|144.4|13.3|\n|NAFTA|54.4|–1.1|\n|ALADI|7.1|58.6|\n|UE|6.4|123.4|\n|Comunidad Andina|1.7|38.6|\n|MERCOSUR|1.3|150.5|\n|MCCA|1.3|283.1|"
          },
          "exportaciones_por_pais_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0090",
            "Title": "Exportaciones por país, Región de Ñuble (marzo 2025)",
            "Content": "\n|País|MM US$|Participación %|Variación %|\n|-|-|-|-|\n|China|62.3|39.1|12.4|\n|Estados Unidos|45.3|28.4|39.7|\n|Japón|8.1|5.1|164.2|"
          },
          "exportaciones_de_berries_y_cerezas_por_subcontinente_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0091",
            "Title": "Exportaciones de berries y cerezas por subcontinente, Región de Ñuble (marzo 2025)",
            "Content": "\n|Subcontinente|MM US$|Participación %|Variación %|\n|-|-|-|-|\n|América del Norte|19.6|59.6|42.5|\n|Asia|7.5|22.8|151.9|\n|Oceanía|3.0|9.1|6.8|\n|Total|32.9|100|51.9|"
          },
          "isup_a_precios_constantes_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0092",
            "Title": "ISUP a precios constantes, Región de Ñuble (marzo 2025)",
            "Content": "\n|Indicador|Variación %|\n|-|-|\n|Interanual|–3.4|\n|Mensual|2.8|\n|Acumulada|–3.3|"
          },
          "ventas_corrientes_de_supermercados_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0093",
            "Title": "Ventas corrientes de supermercados, Región de Ñuble (marzo 2025)",
            "Content": "\n|Medida|Valor|Variación %|\n|-|-|-|\n|Ventas MM $|28.582|0.6|\n|Establecimientos|32|—|\n|Superficie m²|61.756|3.3|\n|Ventas por m² $|462.830|–2.7|"
          },
          "indicadores_de_alojamiento_turistico_region_de_nuble_marzo_2025": {
            "ID": "GN-IND-SEC-0094",
            "Title": "Indicadores de alojamiento turístico, Región de Ñuble (marzo 2025)",
            "Content": "\n|Indicador|Valor|Variación % / pp|\n|-|-|-|\n|Pernoctaciones|27.591|–1.9|\n|Llegadas|15.657|–4.8|\n|Ocupación habitaciones %|24.0|0.88|\n|RevPAR $|16.364|22.3|\n|ADR $|68.075|17.8|"
          },
          "molienda_de_trigo_region_de_nuble_diciembre_2024": {
            "ID": "GN-IND-SEC-0095",
            "Title": "Molienda de trigo, Región de Ñuble (diciembre 2024)",
            "Content": "\n|Concepto|Ton|Interanual %|Mensual %|Acumulada %|\n|-|-|-|-|-|\n|Total molienda|8.053|–7.6|–10.7|–2.7|\n|Productos|6.171|–6.9|–11.1|–4.0|\n|Subproductos|1.882|–9.8|–9.4|1.7|"
          },
          "subproductos_de_trigo_region_de_nuble_diciembre_2024": {
            "ID": "GN-IND-SEC-0096",
            "Title": "Subproductos de trigo, Región de Ñuble (diciembre 2024)",
            "Content": "\n|Subproducto|Ton|Participación %|Interanual %|\n|-|-|-|-|\n|Afrechillo|872|46.3|–12.8|\n|Afrecho|535|28.4|–14.7|\n|Harinilla|474|25.2|3.0|"
          },
          "ganado_beneficiado_y_carne_region_de_nuble_diciembre_2024": {
            "ID": "GN-IND-SEC-0097",
            "Title": "Ganado beneficiado y carne, Región de Ñuble (diciembre 2024)",
            "Content": "\n|Especie|Cabezas|Δ %|Carne t|Δ %|% nacional|\n|-|-|-|-|-|-|\n|Bovinos|5.911|15.3|1.403|11.5|8.0|\n|Porcinos|1.911|–13.1|160|–15.8|0.3|"
          },
          "remates_en_ferias_nuble_biobio_diciembre_2024": {
            "ID": "GN-IND-SEC-0098",
            "Title": "Remates en ferias, Ñuble-Biobío (diciembre 2024)",
            "Content": "\n|Especie|Cabezas|Δ %|\n|-|-|-|\n|Bovinos|13.446|3.6|\n|Ovinos|2.734|2.2|\n|Porcinos|1.225|1.7|\n|Equinos|1.301|–17.7|"
          },
          "broilers_beneficiados_o_higgins_nuble_diciembre_2024": {
            "ID": "GN-IND-SEC-0099",
            "Title": "Broilers beneficiados, O'Higgins + Ñuble (diciembre 2024)",
            "Content": "\n|Indicador|Unidades|Carnes t|Δ % unidades|Δ % t|\n|-|-|-|-|-|\n|Broilers|16.594.255|41.431|8.8|11.1|"
          }
        }
      },
      "indicadores_municipales": {
        "ID": "GN-IND-SEC-0100",
        "Title": "Indicadores Municipales",
        "Content": "\nLos datos presentados a continuación, fueron extraídos desde la sección Datos Municipales del Sistema Nacional de Información Municipal (SINIM), Año 2023",
        "Sections": {
          "datos_financieros": {
            "ID": "GN-IND-SEC-0101",
            "Title": "Datos Financieros",
            "Content": "\n|Comuna|Ingresos municipales totales (M$)|Ingresos propios permanentes (IPP) (M$)|Dependencia del FCM (%)|Gastos municipales totales (M$)|Gastos en personal municipal (M$)|Gastos en bienes y servicios de consumo (M$)|\n|-|-|-|-|-|-|-|\n|Bulnes|7528646|1695432|72.81|7799165|2805283|2351390|\n|Chillán|53872403|23087421|49.43|57458323|20138558|16498529|\n|Chillán Viejo|10694189|3063494|64.30|10612400|3263044|3425285|\n|Cobquecura|5337050|593823|85.41|5311785|2064440|1306390|\n|Coelemu|7082328|1176028|80.23|6683476|2489376|2090516|\n|Coihueco|11225566|1562835|83.33|10103229|2525687|2439273|\n|El Carmen|5737797|1027784|77.69|5822824|2626368|1266919|\n|Ñiquén|4973856|885404|79.85|5133895|1919777|901950|\n|Ninhue|4245116|293973|90.66|4035910|1584566|891022|\n|Pemuco|4424605|1281204|65.35|4643122|1619267|947053|\n|Pinto|6118385|1487507|66.21|6981076|1790010|1667402|\n|Portezuelo|4431771|272610|90.96|4184371|1639131|748883|\n|Quillón|12648863|1501682|86.65|13176760|4813266|3375642|\n|Quirihue|5589828|693994|84.90|6705828|2155922|1865515|\n|Ránquil|4939263|1161070|67.96|5325150|1547326|949024|\n|San Carlos|16665138|3703231|74.93|19051367|5822777|5366750|\n|San Fabián|3273210|652183|76.02|3509456|1324783|386569|\n|San Ignacio|6606724|774900|85.71|7670501|3208285|1143536|\n|San Nicolás|7311720|1984714|59.10|7892616|2786776|1593436|\n|Trehuaco|4432665|403881|87.86|4783268|2061933|645260|\n|Yungay|8567121|1552032|79.35|8392712|2544843|2489324|"
          },
          "recursos_humanos": {
            "ID": "GN-IND-SEC-0102",
            "Title": "Recursos Humanos",
            "Content": "\n|Comuna|Total funcionarios|Nivel de profesionalización (%)|Funcionarios de planta|Funcionarios a contrata|Funcionarios a honorarios|\n|-|-|-|-|-|-|\n|Bulnes|101|43.48|52|40|9|\n|Chillán|544|34.19|241|227|1080|\n|Chillán Viejo|136|67.89|34|75|6|\n|Cobquecura|No disponible|No disponible|No disponible|No disponible|No disponible|\n|Coelemu|86|32.50|54|26|6|\n|Coihueco|117|38.37|64|22|3|\n|El Carmen|187|28.71|61|40|86|\n|Ñiquén|78|45.45|30|25|23|\n|Ninhue|48|43.75|23|25|0|\n|Pemuco|63|50.82|30|31|2|\n|Pinto|71|38.24|41|27|3|\n|Portezuelo|66|100.00|34|30|2|\n|Quillón|160|29.41|60|76|24|\n|Quirihue|157|91.04|43|24|90|\n|Ránquil|47|51.11|30|15|2|\n|San Carlos|90|61.63|35|51|4|\n|San Fabián|42|59.52|25|17|0|\n|San Ignacio|No disponible|No disponible|No disponible|No disponible|No disponible|\n|San Nicolás|68|41.18|33|35|0|\n|Trehuaco|104|32.43|33|41|30|\n|Yungay|85|48.24|58|27|0|"
          },
          "educacion_municipal": {
            "ID": "GN-IND-SEC-0103",
            "Title": "Educación Municipal",
            "Content": "\n|Comuna|Cobertura (%)|Nº establecimientos|Aporte municipal (M$)|Ingresos educación (M$)|Gastos educación (M$)|\n|-|-|-|-|-|-|\n|Bulnes|58.57|19|370000|10164976|10611186|\n|Chillán|20.52|55|3724800|37861103|39970919|\n|Chillán Viejo|13.87|13|660815|6755404|6875251|\n|Cobquecura|87.71|No disponible|546262|3903305|4117321|\n|Coelemu|98.92|14|30460|11818899|11658477|\n|Coihueco|55.06|24|900000|9462082|9605339|\n|El Carmen|114.13|20|150831|11181494|11503629|\n|Ñiquén|87.76|14|909000|8432180|8989491|\n|Ninhue|93.43|9|370000|4526232|4751724|\n|Pemuco|78.35|11|571980|5546779|5539251|\n|Pinto|62.40|15|587300|5956682|6626962|\n|Portezuelo|66.75|8|223594|3439025|3446869|\n|Quillón|64.45|13|503777|8865003|8981255|\n|Quirihue|83.86|8|495000|8226388|8398913|\n|Ránquil|90.63|8|534999|4501427|4614994|\n|San Carlos|40.15|29|1544254|21901286|22318311|\n|San Fabián|124.49|8|41000|4120789|4655880|\n|San Ignacio|55.25|No disponible|648026|8229149|8521711|\n|San Nicolás|159.59|8|12900|14086256|14429960|\n|Trehuaco|64.77|13|640313|3467638|3901972|\n|Yungay|57.61|12|852000|8382094|7720855|"
          },
          "salud_municipal": {
            "ID": "GN-IND-SEC-0104",
            "Title": "Salud Municipal",
            "Content": "\n|Comuna|Tipo administración|Aporte municipal (M$)|Ingresos salud (M$)|Gastos salud (M$)|\n|-|-|-|-|-|\n|Bulnes|Depto. o Dirección|120208|2722661|2781189|\n|Chillán|Depto. o Dirección|3166667|32779901|32806741|\n|Chillán Viejo|Depto. o Dirección|112000|8163946|9136473|\n|Cobquecura|Depto. o Dirección|156593|2098545|2150204|\n|Coelemu|Depto. o Dirección|387029|1101988|1085286|\n|Coihueco|Depto. o Dirección|300000|8660822|8961901|\n|El Carmen|Depto. o Dirección|414500|1940189|1961808|\n|Ñiquén|Depto. o Dirección|412236|3391471|3035511|\n|Ninhue|Depto. o Dirección|180000|2267597|2252620|\n|Pemuco|Depto. o Dirección|400000|3037179|3064063|\n|Pinto|Depto. o Dirección|321000|3874601|3860882|\n|Portezuelo|Depto. o Dirección|170000|1844866|1769554|\n|Quillón|Depto. o Dirección|295000|4402375|4793440|\n|Quirihue|Depto. o Dirección|239000|627559|623759|\n|Ránquil|Depto. o Dirección|325000|2258412|2211576|\n|San Carlos|Depto. o Dirección|1900000|15949728|15765602|\n|San Fabián|Depto. o Dirección|548029|2335145|2293550|\n|San Ignacio|Depto. o Dirección|490000|6014576|6167296|\n|San Nicolás|Depto. o Dirección|337000|3664356|3505536|\n|Trehuaco|Depto. o Dirección|50500|2019570|2044219|\n|Yungay|Depto. o Dirección|460000|2697230|2535762|"
          },
          "desarrollo_territorial": {
            "ID": "GN-IND-SEC-0105",
            "Title": "Desarrollo Territorial",
            "Content": "\n|Comuna|Plan Regulador Comunal|PLADECO|Año actualización PLADECO|Nº propiedades municipales|\n|-|-|-|-|-|\n|Bulnes|Sí|Sí|2015|66|\n|Chillán|Sí|Sí|2019|429|\n|Chillán Viejo|Sí|Sí|2023|51|\n|Cobquecura|Sí|Sí|2014|43|\n|Coelemu|Sí|Sí|2017|50|\n|Coihueco|No|Sí|2023|138|\n|El Carmen|Sí|Sí|2016|77|\n|Ñiquén|No|Sí|2015|35|\n|Ninhue|Sí|Sí|2020|37|\n|Pemuco|Sí|Sí|2011|35|\n|Pinto|No|Sí|2018|47|\n|Portezuelo|Sí|Sí|2020|169|\n|Quillón|Sí|Sí|2021|83|\n|Quirihue|Sí|Sí|2022|65|\n|Ránquil|Sí|Sí|2016|43|\n|San Carlos|Sí|Sí|2017|245|\n|San Fabián|Sí|Sí|2020|125|\n|San Ignacio|No disponible|No disponible|No disponible|58|\n|San Nicolás|No|Sí|2018|113|\n|Trehuaco|No|Sí|2012|44|\n|Yungay|Sí|Sí|2019|65|"
          },
          "transferencias_y_compensaciones": {
            "ID": "GN-IND-SEC-0106",
            "Title": "Transferencias y Compensaciones",
            "Content": "\n|Comuna|Monto FCM (M$)|Compensación predios exentos (M$)|FIGEM (M$)|\n|-|-|-|-|\n|Bulnes|4541150|108258|88749|\n|Chillán|22563102|663399|129144|\n|Chillán Viejo|5518831|122309|0|\n|Cobquecura|3475906|57992|0|\n|Coelemu|4772379|76810|88942|\n|Coihueco|7812989|112576|94049|\n|El Carmen|3578995|72764|89954|\n|Ñiquén|3590528|75472|0|\n|Ninhue|2852028|51196|87667|\n|Pemuco|2415957|44150|89662|\n|Pinto|2915008|69607|91133|\n|Portezuelo|2741629|42435|92529|\n|Quillón|9742674|135670|88671|\n|Quirihue|3961720|83459|0|\n|Ránquil|2463248|48405|83979|\n|San Carlos|10939424|250054|123131|\n|San Fabián|2068009|25833|95064|\n|San Ignacio|4648293|108624|0|\n|San Nicolás|2881019|74301|102131|\n|Trehuaco|2917779|48698|0|\n|Yungay|5964021|89899|0|\n\nAbreviaturas\n\n* FCM: Fondo Común Municipal\n* IPP: Ingresos Propios Permanentes\n* M$: Miles de pesos chilenos\n* PLADECO: Plan de Desarrollo Comunal\n* FIGEM: Fondo de Incentivo al Mejoramiento de la Gestión Municipal"
          }
        }
      },
      "indicadores_de_seguridad_publica": {
        "ID": "GN-IND-SEC-0107",
        "Title": "Indicadores de seguridad Pública",
        "Content": "\nA continuación se presentan los principales indicadores de seguridad pública para la Región de Ñuble, incluyendo datos de delitos registrados por las policías y los resultados de la Encuesta Nacional Urbana de Seguridad Ciudadana (ENUSC).",
        "Sections": {
          "casos_policiales_por_tipo_de_delito_tasa_cada_100_000_habitantes": {
            "ID": "GN-IND-SEC-0108",
            "Title": "Casos Policiales por tipo de delito (Tasa cada 100.000 habitantes)",
            "Content": "\nFuente: Sistema Táctico de Operación Policial (STOP), Carabineros de Chile.",
            "Sections": {
              "abigeato": {
                "ID": "GN-IND-SEC-0109",
                "Title": "Abigeato",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|12,4|14,8|\n|Región de Ñuble|29|39,3|\n|Chillán|8,4|5,4|\n|Bulnes|30,8|70,4|\n|Chillán Viejo|20,1|45,5|\n|El Carmen|24,4|73,6|\n|Pemuco|58|34,9|\n|Pinto|41,5|90,8|\n|Quillón|31,5|31,3|\n|San Ignacio|18|36,1|\n|Yungay|42,7|47,9|\n|Quirihue|73,6|73,6|\n|Cobquecura|19|76,4|\n|Coelemu|23,7|5,9|\n|Ninhue|55,7|93,1|\n|Portezuelo|0|143,1|\n|Ránquil|31,8|31,8|\n|Treguaco|17,4|34,8|\n|San Carlos|42,3|59,8|\n|Coihueco|55,7|86,5|\n|Ñiquén|103,9|104|\n|San Fabián|211,5|189|\n|San Nicolás|56,7|56,4|"
              },
              "delitos_sexuales": {
                "ID": "GN-IND-SEC-0110",
                "Title": "Delitos Sexuales",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|124,5|109,1|\n|Región de Ñuble|116,4|99,5|\n|Chillán|102,2|95,2|\n|Bulnes|123,3|118,8|\n|Chillán Viejo|109,3|82,4|\n|El Carmen|154,8|106,3|\n|Pemuco|116,1|93|\n|Pinto|124,6|99,1|\n|Quillón|131,2|119,9|\n|San Ignacio|144,4|156,5|\n|Yungay|170,8|127,8|\n|Quirihue|122,7|73,6|\n|Cobquecura|114,2|171,8|\n|Coelemu|47,4|88,8|\n|Ninhue|167,1|93,1|\n|Portezuelo|142,6|102,2|\n|Ránquil|143,2|15,9|\n|Treguaco|122|121,7|\n|San Carlos|119,9|77,3|\n|Coihueco|114,8|124,5|\n|Ñiquén|60,6|86,6|\n|San Fabián|465,3|252|\n|San Nicolás|113,5|72,5|"
              },
              "infracciones_a_la_ley_de_drogas": {
                "ID": "GN-IND-SEC-0111",
                "Title": "Infracciones a la Ley de Drogas",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|78,3|83,3|\n|Región de Ñuble|70,2|75,5|\n|Chillán|78,9|94,7|\n|Bulnes|74,9|74,8|\n|Chillán Viejo|43,2|42,6|\n|El Carmen|40,7|0|\n|Pemuco|325|186|\n|Pinto|58,1|66,1|\n|Quillón|73,5|62,6|\n|San Ignacio|36,1|36,1|\n|Yungay|69,4|122,4|\n|Quirihue|81,8|57,2|\n|Cobquecura|38,1|57,3|\n|Coelemu|11,8|35,5|\n|Ninhue|0|0|\n|Portezuelo|20,4|0|\n|Ránquil|47,7|47,7|\n|Treguaco|0|69,5|\n|San Carlos|72,3|52,7|\n|Coihueco|90,5|121,1|\n|Ñiquén|26|17,3|\n|San Fabián|84,6|42|\n|San Nicolás|56,7|88,6|"
              },
              "robo_de_vehiculo_motorizado": {
                "ID": "GN-IND-SEC-0112",
                "Title": "Robo de Vehículo Motorizado",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|168,2|148,3|\n|Región de Ñuble|116,2|104,5|\n|Chillán|233,7|182,9|\n|Bulnes|48,5|52,8|\n|Chillán Viejo|106,5|125,1|\n|El Carmen|48,9|8,2|\n|Pemuco|23,2|46,5|\n|Pinto|8,3|24,8|\n|Quillón|73,5|78,2|\n|San Ignacio|24,1|12|\n|Yungay|0|42,6|\n|Quirihue|40,9|32,7|\n|Cobquecura|0|19,1|\n|Coelemu|23,7|47,4|\n|Ninhue|0|0|\n|Portezuelo|20,4|0|\n|Ránquil|15,9|47,7|\n|Treguaco|17,4|17,4|\n|San Carlos|54,7|93,2|\n|Coihueco|13,9|17,3|\n|Ñiquén|34,6|17,3|\n|San Fabián|0|21|\n|San Nicolás|32,4|40,3|"
              },
              "robo_en_lugar_habitado_y_no_habitado": {
                "ID": "GN-IND-SEC-0113",
                "Title": "Robo en Lugar Habitado y No Habitado",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|446,5|464,2|\n|Región de Ñuble|578,5|629,3|\n|Chillán|575,1|739,1|\n|Bulnes|784|510,3|\n|Chillán Viejo|702,1|645,3|\n|El Carmen|366,7|506,8|\n|Pemuco|684,8|558,1|\n|Pinto|490,1|536,7|\n|Quillón|771,3|808|\n|San Ignacio|481,2|433,4|\n|Yungay|667,4|638,8|\n|Quirihue|458|425|\n|Cobquecura|342,7|305,5|\n|Coelemu|438,3|497,2|\n|Ninhue|315,7|316,6|\n|Portezuelo|326|490,7|\n|Ránquil|461,5|1287,8|\n|Treguaco|557,9|521,6|\n|San Carlos|737,2|548,5|\n|Coihueco|309,7|428,9|\n|Ñiquén|302,9|502,6|\n|San Fabián|655,7|546,1|\n|San Nicolás|648,4|652,5|"
              },
              "robos_con_violencia_o_sorpresa": {
                "ID": "GN-IND-SEC-0114",
                "Title": "Robos con Violencia o Sorpresa",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|541,2|583,3|\n|Región de Ñuble|192,8|200,4|\n|Chillán|297,2|335,8|\n|Bulnes|171,8|132|\n|Chillán Viejo|296,4|264,4|\n|El Carmen|24,4|49|\n|Pemuco|232,1|162,8|\n|Pinto|33,2|66,1|\n|Quillón|78,7|114,7|\n|San Ignacio|84,2|48,2|\n|Yungay|96,1|47,9|\n|Quirihue|106,3|73,6|\n|Cobquecura|38,1|19,1|\n|Coelemu|100,7|94,7|\n|Ninhue|0|18,6|\n|Portezuelo|0|0|\n|Ránquil|95,5|31,8|\n|Treguaco|69,7|69,5|\n|San Carlos|176,4|181,1|\n|Coihueco|48,7|48,4|\n|Ñiquén|77,9|69,3|\n|San Fabián|63,5|21|\n|San Nicolás|113,5|88,6|"
              },
              "violencia_intrafamiliar": {
                "ID": "GN-IND-SEC-0115",
                "Title": "Violencia Intrafamiliar",
                "Content": "\n|Unidad Territorial|2022|2023|\n|-|-|-|\n|TOTAL PAÍS|737,3|716,9|\n|Región de Ñuble|754,8|695,9|\n|Chillán|723,5|662,6|\n|Bulnes|858,9|901,8|\n|Chillán Viejo|748,1|668,1|\n|El Carmen|708,9|686,6|\n|Pemuco|719,6|697,7|\n|Pinto|573,1|578|\n|Quillón|1107,1|834,1|\n|San Ignacio|751,9|872,8|\n|Yungay|902,3|771,9|\n|Quirihue|409|531,3|\n|Cobquecura|571,2|496,4|\n|Coelemu|533|520,9|\n|Ninhue|612,8|744,9|\n|Portezuelo|346,4|429,4|\n|Ránquil|652,5|604,1|\n|Treguaco|802|765|\n|San Carlos|932,9|757,7|\n|Coihueco|706,3|684,9|\n|Ñiquén|623,2|589,2|\n|San Fabián|1099,8|1134,2|\n|San Nicolás|842,9|757,2|"
              }
            }
          },
          "riesgos_y_fragilidad_territorial": {
            "ID": "GN-IND-SEC-0116",
            "Title": "Riesgos y Fragilidad Territorial",
            "Content": "",
            "Sections": {
              "poblacion_e_infraestructura_critica_expuesta_a_amenazas": {
                "ID": "GN-IND-SEC-0117",
                "Title": "Población e Infraestructura Crítica Expuesta a Amenazas",
                "Content": "\n|Amenaza|Comuna expuesta|Población Expuesta|Infraestructura Crítica expuesta|\n|-|-|-|-|\n|Incendio Forestal|Región de Ñuble|489029 habitantes|\"69938 Viviendas ; 629 Establecimientos Educacionales ;  112 Servicios de Salud ; 41 Cuarteles de Carabineros ; 46 Compañías de Bomberos\"|\n|Erupción Volcánica|Pinto, El Carmen, San Ignacio, Coihueco y San Fabián de Alico|6626 habitantes|\"1704 Viviendas ; 7 Establecimientos Educacionales ; 1 Servicios de Salud ; 2 Cuarteles de Carabineros ; 2 Compañías de Bomberos\"|\n|Tsunami|Cobquecura, Trehuaco y Coelemu|11249 habitantes|\"5939 Viviendas ; 22 Establecimientos Educacionales ; 6 Servicios de Salud ; 3 Cuarteles de Carabineros ; 3 Compañías de Bomberos\"|\n|Marejadas|Coelemu y Trehuaco|906 habitantes|\"514 Viviendas ; 5 Establecimientos Educacionales ; 1 Servicios de Salud ; 1 Cuarteles de Carabineros\"|\n|Déficit Hídrico|Región de Ñuble|26126 habitantes|"
              },
              "indice_comunal_de_fragilidad_socio_residencial_icfsr": {
                "ID": "GN-IND-SEC-0118",
                "Title": "Índice Comunal de Fragilidad Socio-Residencial (ICFSR)",
                "Content": "\n|Comuna|Rk|ICFSR|Clasif. Global|\n|-|-|-|-|\n|Cobquecura|2|0,78|alto|\n|Trehuaco|34|0,58|alto|\n|Pinto|47|0,55|alto|\n|Coelemu|51|0,54|alto|\n|Coihueco|70|0,5|alto|\n|Ninhue|79|0,49|alto|\n|El Carmen|88|0,48|alto|\n|San Fabián|91|0,48|alto|\n|San Ignacio|99|0,46|alto|\n|San Carlos|105|0,46|alto|\n|Yungay|130|0,43|moderado|\n|Quirihue|137|0,42|moderado|\n|Quillón|146|0,41|moderado|\n|San Nicolás|155|0,4|moderado|\n|Ránquil|176|0,37|moderado|\n|Chillán Viejo|213|0,34|moderado|\n|Portezuelo|226|0,32|moderado|\n|Bulnes|249|0,29|moderado|\n|Ñiquén|262|0,28|moderado|\n|Chillán|264|0,27|moderado|\n|Pemuco|288|0,23|moderado|"
              }
            }
          },
          "encuesta_nacional_urbana_de_seguridad_ciudadana_enusc_2024_region_de_nuble": {
            "ID": "GN-IND-SEC-0119",
            "Title": "Encuesta Nacional Urbana de Seguridad Ciudadana (ENUSC) 2024 - Región de Ñuble",
            "Content": "",
            "Sections": {
              "percepcion_de_aumento_de_la_delincuencia": {
                "ID": "GN-IND-SEC-0120",
                "Title": "Percepción de aumento de la delincuencia",
                "Content": "\n|Nivel Territorial|2023|2024|\n|-|-|-|\n|PAÍS|91,8%|92,8%|\n|COMUNA|84,7%|79,6%|\n|BARRIO|54,3%|47,2%|"
              },
              "percepcion_de_aumento_de_la_delincuencia_en_el_pais_por_region": {
                "ID": "GN-IND-SEC-0121",
                "Title": "Percepción de aumento de la delincuencia en el PAÍS, por región",
                "Content": "\n|Región|2023|2024|\n|-|-|-|\n|Arica y Parinacota|88,8%|93,5%|\n|Tarapacá|86,0%|94,6%|\n|Antofagasta|93,2%|91,4%|\n|Atacama|91,2%|92,4%|\n|Coquimbo|87,4%|88,4%|\n|Valparaíso|87,9%|94,9%|\n|Metropolitana|96,2%|95,9%|\n|O´Higgins|89,5|87,5%|\n|Maule|88,4%|89,3%|\n|Ñuble|91,8%|93,7%|\n|Biobío|95,7%|93,8%|\n|Araucanía|94,0|88,9%|\n|Los Ríos|85,4%|82,8%|\n|Los Lagos|89,3|85,9%|\n|Aysén|90,1%|87,5%|\n|Magallanes|85,7%|86,6%|"
              },
              "percepcion_de_aumento_de_la_delincuencia_en_la_comuna_por_region": {
                "ID": "GN-IND-SEC-0122",
                "Title": "Percepción de aumento de la delincuencia en la COMUNA, por región",
                "Content": "\n|Región|2023|2024|\n|-|-|-|\n|Arica y Parinacota|87,2%|81,1%|\n|Tarapacá|81,2%|79,8%|\n|Antofagasta|89,0%|84,2%|\n|Atacama|84,4%|83,2%|\n|Coquimbo|81,6%|79,8%|\n|Valparaíso|77,9%|79,5%|\n|Metropolitana|72,6%|79,0%|\n|O´Higgins|79,1%|76,1%|\n|Maule|80,4%|79,7%|\n|Ñuble|84,7%|79,6%|\n|Biobío|79,3|79,4%|\n|Araucanía|77,7%|65,9%|\n|Los Ríos|78,6%|72,8%|\n|Los Lagos|76,6%|70,8%|\n|Aysén|71,9%|59,4%|\n|Magallanes|56,4%|48,4%|"
              },
              "percepcion_de_aumento_de_la_delincuencia_en_el_barrio_por_region": {
                "ID": "GN-IND-SEC-0123",
                "Title": "Percepción de aumento de la delincuencia en el BARRIO, por región",
                "Content": "\n|Región|2023|2024|\n|-|-|-|\n|Arica y Parinacota|61,8%|56,1%|\n|Tarapacá|53,1%|44,7%|\n|Antofagasta|55,7%|55,4%|\n|Atacama|52,6%|53,2%|\n|Coquimbo|51,5%|50,1%|\n|Valparaíso|53,4%|36,3%|\n|Metropolitana|57,0%|54,5%|\n|O´Higgins|54,3%|45,2%|\n|Maule|49,3%|47,0%|\n|Ñuble|54,3%|47,2%|\n|Biobío|53,2%|50,9%|\n|Araucanía|35,4%|38,4%|\n|Los Ríos|45,1%|43,3%|\n|Los Lagos|42,8%|33,6%|\n|Aysén|29,8%|34,1%|\n|Magallanes|17,5%|26,4%|"
              },
              "fuente_de_percepcion_sobre_delincuencia_en_el_pais": {
                "ID": "GN-IND-SEC-0124",
                "Title": "Fuente de percepción sobre delincuencia en el PAÍS",
                "Content": "\n|Fuente|2023|2024|\n|-|-|-|\n|Televisión|49,1%|52,1%|\n|Redes sociales|33,8%|33,0%|\n|Familiares otras personas|5,9%|5,3%|\n|Radio|4,1%|3,6%|\n|Periódicos|1,8%|2,8%|\n|Experiencia personal|5,0%|2,8%|"
              },
              "fuente_de_percepcion_sobre_delincuencia_en_la_comuna": {
                "ID": "GN-IND-SEC-0125",
                "Title": "Fuente de percepción sobre delincuencia en la COMUNA",
                "Content": "\n|Fuente|2023|2024|\n|-|-|-|\n|Redes sociales|47,7%|48,5%|\n|Radio|16,9%|18,1%|\n|Familiares otras personas|17,2%|16,3%|\n|Televisión|7,3%|9,3%|\n|Periódicos|3,2%|4,3%|\n|Experiencia personal|7,5%|3,2%|"
              },
              "fuente_de_percepcion_sobre_delincuencia_en_el_barrio": {
                "ID": "GN-IND-SEC-0126",
                "Title": "Fuente de percepción sobre delincuencia en el BARRIO",
                "Content": "\n|Fuente|2024|\n|-|-|\n|Familiares otras personas|59,5%|\n|Redes sociales|27,1%|\n|Experiencia personal|7,5%|\n|Radio|4,0%|\n|Televisión|1,1%|\n|Periódicos|0,4%|"
              },
              "percepcion_de_problemas_de_delincuencia_en_el_barrio": {
                "ID": "GN-IND-SEC-0127",
                "Title": "Percepción de problemas de delincuencia en el barrio",
                "Content": "\n|Situación Delictiva|2023|2024|\n|-|-|-|\n|Balaceras o disparos|7,8%|7,1%|\n|Robos o asaltos en la vía pública|5,7%|5,4%|\n|Presencia de pandillas violentas|4,3%|4,5%|\n|Amenazas o peleas entre vecinos|3,1%|4,1%|\n|Vandalismo o daño a la propiedad (excluyendo rayados)|6,0%|4,1%|\n|Peleas callejeras sin armas|4,5%|3,1%|\n|Peleas callejeras con armas blancas o de fuego|3,4%|3,1%|"
              },
              "percepcion_de_desordenes_e_incivilidades_en_el_barrio": {
                "ID": "GN-IND-SEC-0128",
                "Title": "Percepción de desórdenes e incivilidades en el barrio",
                "Content": "\n|Desorden|2023|2024|\n|-|-|-|\n|Consumo de alcohol o droga en la vía pública|22,0%|22,6%|\n|Sitios eriazos descuidados o acumulación de basura|16,8%|20,5%|\n|Lanzamiento de fuegos artificiales|13,2%|17,0%|\n|Presencia de comercio ilegal|13,7%|13,0%|\n|Presencia de personas que habitan y/o duermen en la calle|8,2%|9,9%|\n|Rayados, marcas o pinturas en la propiedad pública o privada|6,3%|6,4%|\n|Venta clandestina de alcohol|6,7%|6,4%|\n|Prostitución o comercio sexual|2,6%|1,3%|"
              },
              "percepcion_de_presencia_de_armas_en_el_barrio": {
                "ID": "GN-IND-SEC-0129",
                "Title": "Percepción de presencia de armas en el barrio",
                "Content": "\n|Percepción|2023|2024|\n|-|-|-|\n|Siempre|0,6%|1,0%|\n|Casi siempre|1,1%|1,7%|\n|Ocasionalmente|6,1%|6,2%|\n|Casi Nunca|4,5%|7,6%|\n|Nunca|87,2%|83,2%|\n|NS/NR/SD|0,4%|0,3%|"
              },
              "percepcion_de_presencia_de_drogas_en_el_barrio": {
                "ID": "GN-IND-SEC-0130",
                "Title": "Percepción de presencia de drogas en el barrio",
                "Content": "\n|Percepción|2023|2024|\n|-|-|-|\n|Siempre|5,2%|5,1%|\n|Casi siempre|7,8%|4,9%|\n|Ocasionalmente|12,1%|11,4%|\n|Casi Nunca|6,6%|9,2%|\n|Nunca|67,1%|69,0%|\n|NS/NR/SD|1,1%|0,3%|"
              },
              "percepcion_del_trabajo_de_carabineros_en_la_comuna": {
                "ID": "GN-IND-SEC-0131",
                "Title": "Percepción del trabajo de Carabineros en la comuna",
                "Content": "\n|Aspecto|Percepción|2023|2024|\n|-|-|-|-|\n|Control del tránsito|Muy bueno y bueno|44,9%|46,7%|\n|| Muy mal y Malo|22,2%|25,5%|\n|Frecuencia con que patrulla y vigila las calles|Muy bueno y bueno|42,9%|43,2%|\n|| Muy mal y Malo|25,9%|26,0%|\n|Coordinación y comunicación con los/as vecinos/as de su barrio|Muy bueno y bueno|38,2%|42,1%|\n|| Muy mal y Malo|25,5%|26,5%|\n|Prevención de delitos y faltas en la comuna|Muy bueno y bueno|31,6%|31,1%|\n|| Muy mal y Malo|27,8%|31,4%|\n|Control del tráfico de drogas|Muy bueno y bueno|23,2%|24,2%|\n|| Muy mal y Malo|35,1%|37,5%|\n|Control de armas|Muy bueno y bueno|19,6%|23,7%|\n|| Muy mal y Malo|26,7%|28,1%|"
              },
              "percepcion_de_la_presencia_policial_carabineros_en_el_barrio_en_los_ultimos_12_m": {
                "ID": "GN-IND-SEC-0132",
                "Title": "Percepción de la presencia policial (Carabineros) en el barrio en los últimos 12 meses",
                "Content": "\n|Percepción|2023|2024|\n|-|-|-|\n|Aumentó|20,7%|18,2%|\n|Se mantuvo|51,2%|51,2%|\n|Disminuyó|25,6%|28,4%|\n|NS/NR/SD|2,5%|2,2%|"
              },
              "percepcion_de_riesgo_de_ser_victima_de_un_delito": {
                "ID": "GN-IND-SEC-0133",
                "Title": "Percepción de riesgo de ser víctima de un delito",
                "Content": "\n|Año|Respuesta|Porcentaje|\n|-|-|-|\n|2023|Sí|43,5%|\n|2023|No|43,8%|\n|2023|No Sabe|12,7%|\n|2024|Sí|44,8%|\n|2024|No|52,7%|\n|2024|No Sabe|2,5%|"
              },
              "actividades_que_ha_dejado_de_hacer_por_temor_a_ser_victima_de_un_delito": {
                "ID": "GN-IND-SEC-0134",
                "Title": "Actividades que ha dejado de hacer por temor a ser víctima de un delito",
                "Content": "\n|Actividad|2023|2024|\n|-|-|-|\n|Caminar por ciertas áreas o lugares|67,6%|67,7%|\n|Usar celular y/o artículos electrónicos en público|55,3%|57,4%|\n|Salir de noche|49,5%|56,1%|\n|Llevar o usar dinero en efectivo|50,4%|46,2%|\n|Usar joyas, reloj u objetos de lujo|40,0%|36,5%|\n|Caminar solo/a|38,6%|35,2%|\n|Realizar actividades deportivas, de recreación o esparcimiento en...|16,7% ||\n|Ir al banco|21,4%|16,5%|\n|Tomar micros o buses|19,4%|14,0%|\n|Tomar taxis o colectivos|14,5%|10,8%|\n|Manejar vehículos, motos y/o estacionar fuera de la vivienda (nueva)|| 10,4%|\n|Tomar o usar Uber, Cabify, Didi o similares|11,4%|9,9%|"
              },
              "victimizacion_de_hogares": {
                "ID": "GN-IND-SEC-0135",
                "Title": "Victimización de hogares",
                "Content": "\n|Año|Percepción Aumento Delincuencia (País)|Victimización Hogares (DMCS)|\n|-|-|-|\n|2018|74,6%|23,8%|\n|2019|83,3%|19,1%|\n|2020|73,1%|19,3%|\n|2021|80,8%|13,8%|\n|2022|90,5%|14,3%|\n|2023|92,2%|15,4%|\n|2024|92,2%|17,9%|"
              },
              "victimizacion_de_hogares_por_tipo_de_delito": {
                "ID": "GN-IND-SEC-0136",
                "Title": "Victimización de hogares por tipo de delito",
                "Content": "",
                "Sections": {
                  "delitos_violentos": {
                    "ID": "GN-IND-SEC-0137",
                    "Title": "Delitos Violentos",
                    "Content": "\n|Tipo de delito|2023|2024|\n|-|-|-|\n|Amenaza violenta|2,2%|2,8%|\n|Robo con violencia o intimidación|1,7%|1,3%|\n|Agresiones/lesiones|0,7%|0,9%|\n|Robo por sorpresa con violencia|0,3%|0,3%|\n|Extorsión violenta|0,3%|0,2%|\n|Robo de vehículo con violencia|0,6%|0,0%|\n|Robo de vivienda con violencia|0,1%|0,0%|"
                  },
                  "robos_no_violentos": {
                    "ID": "GN-IND-SEC-0138",
                    "Title": "Robos no violentos",
                    "Content": "\n|Tipo de Robo|2023|2024|\n|-|-|-|\n|Robo desde vehículo|8,9%|10,3%|\n|Robo en la vivienda no violento|4,1%|4,7%|\n|Robo por sorpresa no violento|1,2%|1,3%|\n|Robo de vehículo no violento|0,9%|0,8%|"
                  },
                  "hurtos": {
                    "ID": "GN-IND-SEC-0139",
                    "Title": "Hurtos",
                    "Content": "\n|Año|Porcentaje|\n|-|-|\n|2023|3,4%|\n|2024|5,0%|"
                  },
                  "vandalismo": {
                    "ID": "GN-IND-SEC-0140",
                    "Title": "Vandalismo",
                    "Content": "\n|Tipo|2023|2024|\n|-|-|-|\n|Vehículos|5,6%|6,9%|\n|Viviendas|1,9%|1,6%|"
                  },
                  "delitos_economicos": {
                    "ID": "GN-IND-SEC-0141",
                    "Title": "Delitos económicos",
                    "Content": "\n|Tipo de Delito|2023|2024|\n|-|-|-|\n|Fraudes|2,7%|5,9%|\n|Estafas|2,5%|3,3%|"
                  },
                  "delitos_ciberneticos": {
                    "ID": "GN-IND-SEC-0142",
                    "Title": "Delitos cibernéticos",
                    "Content": "\n|Tipo de Delito|2023|2024|\n|-|-|-|\n|Hackeo redes sociales o correo electrónico|2,6%|3,9%|\n|Software Malicioso|0,8%|1,0%|\n|Acoso por internet o Ciberbullying|0,9%|0,9%|\n|Suplantación Identidad|0,6%|0,7%|"
                  },
                  "delitos_de_odio": {
                    "ID": "GN-IND-SEC-0143",
                    "Title": "Delitos de odio",
                    "Content": "\n|Año|Porcentaje|\n|-|-|\n|2023|0,2%|\n|2024|0,1%|"
                  }
                }
              },
              "victimizacion_personal_por_region": {
                "ID": "GN-IND-SEC-0144",
                "Title": "Victimización personal por región",
                "Content": "\n|Región|2023|2024|\n|-|-|-|\n|Total País|5,7%|5,8%|\n|Arica y Parinacota|5,3%|7,2%|\n|Tarapacá|6,1%|6,5%|\n|Antofagasta|5,0%|3,6%|\n|Atacama|5,7%|4,3%|\n|Coquimbo|2,9%|4,5%|\n|Valparaíso|4,8%|5,9%|\n|Metropolitana|7,1%|7,2%|\n|O'Higgins|3,6%|4,8%|\n|Maule|3,1%|3,4%|\n|Ñuble|3,4%|2,9%|\n|Biobío|4,9%|3,8%|\n|Araucanía|3,7%|4,8%|\n|Los Ríos|3,5%|4,8%|\n|Los Lagos|2,8%|3,0%|\n|Aysén|2,1%|2,0%|\n|Magallanes|2,0%|2,6%|"
              },
              "victimizacion_personal_por_tipo_de_delito_violento": {
                "ID": "GN-IND-SEC-0145",
                "Title": "Victimización personal por tipo de delito violento",
                "Content": "\n|Tipo de delito|2023|2024|\n|-|-|-|\n|Amenazas Violentas|1,4%|1,9%|\n|Agresiones y lesiones|0,4%|0,5%|\n|Robo con violencia e intimidación|1,1%|0,5%|\n|Extorsión|0,1%|0,1%|\n|Robo por sorpresa|0,3%|0,1%|\n|Robo de Vehículo|0,3%|0,0%|\n|Robo en la vivienda|0,1%|0,0%|"
              },
              "denuncia_de_delitos_violentos_contra_el_hogar": {
                "ID": "GN-IND-SEC-0146",
                "Title": "Denuncia de delitos violentos contra el hogar",
                "Content": "\n|Año|Denunciaron (Sí)|No Denunciaron (No)|\n|-|-|-|\n|2023|57,7%|42,3%|\n|2024|46,3%|53,7%|"
              },
              "denuncia_por_tipo_de_delito_violento_contra_el_hogar": {
                "ID": "GN-IND-SEC-0147",
                "Title": "Denuncia por tipo de delito violento contra el hogar",
                "Content": "\n|Delito|2023|2024|\n|-|-|-|\n|Agresiones / Lesiones|48,5%|63,6%|\n|Extorsión violenta|60,9%|88,5%|\n|Robo con violencia o intimidación|54,5%|56,2%|\n|Amenaza violenta|49,8%|35,2%|\n|Robo por sorpresa con violencia|71,8%|28,8%|\n|Robo de vehículo con violencia|0,0%|100,0%|\n|Robo de vivienda con violencia|0,0%|100,0%|"
              },
              "confianza_en_las_instituciones": {
                "ID": "GN-IND-SEC-0148",
                "Title": "Confianza en las instituciones",
                "Content": "",
                "Sections": {
                  "conocimiento_de_instituciones": {
                    "ID": "GN-IND-SEC-0149",
                    "Title": "Conocimiento de instituciones",
                    "Content": "\n|Institución|2023 (% Sí)|2024 (% Sí)|\n|-|-|-|\n|Carabineros de Chile|63,9%|75,7%|\n|Policía de Investigaciones (PDI)|47,9%|54,7%|\n|Fiscalía o Ministerio Público|32,4%|35,7%|"
                  },
                  "confianza_en_carabineros_de_chile": {
                    "ID": "GN-IND-SEC-0150",
                    "Title": "Confianza en Carabineros de Chile",
                    "Content": "\n|Confianza|2023|2024|\n|-|-|-|\n|Mucha y bastante confianza|69,3%|68,5%|\n|Poco o Nada de confianza|30,4%|31,4%|"
                  },
                  "confianza_en_la_pdi": {
                    "ID": "GN-IND-SEC-0151",
                    "Title": "Confianza en la PDI",
                    "Content": "\n|Confianza|2023|2024|\n|-|-|-|\n|Mucha y bastante confianza|80,5%|80,8%|\n|Poco o Nada de confianza|18,9%|18,2%|"
                  },
                  "confianza_en_la_fiscalia_o_ministerio_publico": {
                    "ID": "GN-IND-SEC-0152",
                    "Title": "Confianza en la Fiscalía o Ministerio Público",
                    "Content": "\n|Confianza|2023|2024|\n|-|-|-|\n|Mucha y bastante confianza|44,5%|43,3%|\n|Poco o Nada de confianza|54,5%|56,6%|"
                  }
                }
              }
            }
          }
        }
      }
    },
    "Content": "# Indicadores regionales y comunales región de Ñuble\n\nActualización BCN: Junio 2025"
  }
}
