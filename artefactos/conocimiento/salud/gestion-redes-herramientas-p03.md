---
urn: urn:salud:kb:gestion-redes-herramientas-p03
nombre: gestion-redes-herramientas-p03
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Herramientas y Anexos - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/05-herramientas-anexos--p03.md (sha256:8bc10e3a8b65a786bf2302208740a712d5d05fc1dbb0e8c22adb60b8ef31adeb) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-herramientas."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, kpi, bpmn, plantillas, fhir, simulacion, madurez, herramientas]
familia: bok
cita: [urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-indice]
---


# Gestión de Redes Asistenciales — Herramientas y Anexos - Parte 03

## Anexo E: Simulación y analítica

### E.1 Modelado de demanda y colas

**Modelo base**: M/M/s (Erlang-C) para dimensionamiento de boxes y dotación.

| Parámetro | Símbolo | Descripción |
|-----------|---------|-------------|
| Tasa de llegada | λ | Pacientes/hora (por segmento ESI) |
| Tasa de servicio | μ | Pacientes atendidos/hora por servidor |
| Servidores | s | Boxes o profesionales disponibles |
| Intensidad de tráfico | ρ = λ/(s·μ) | Utilización; **mantener ρ < 0.85** |

**Fórmulas clave**:
- Probabilidad de espera (Erlang-C): P(espera) = C(s, λ/μ)
- Tiempo medio en cola: Wq = C(s, λ/μ) / (s·μ − λ)
- Tiempo medio en sistema: W = Wq + 1/μ

**Regla operativa**: si ρ ≥ 0.85 → activar plan de contingencia (apertura box adicional, redirección, fast-track).

### E.2 Simulación SUH

| Escenario | λ base | Δ λ | s disponible | ρ esperado | Acción |
|-----------|--------|-----|-------------|------------|--------|
| Operación normal (lunes AM) | 8 pac/h | — | 6 boxes | 0.67 | Estándar |
| Peak estacional (invierno IRA) | 8 pac/h | +40 % | 6 boxes | 0.93 | Apertura 2 boxes + fast-track respiratorio |
| Cierre 2 boxes mantención | 8 pac/h | — | 4 boxes | 1.00 | Desvío ESI-4/5 a SAPU + refuerzo turnos |
| MCI (incidente masivo) | — | +200 % puntual | 6+4 contingencia | Variable | Activación plan MCI, triaje START, cancelación electiva |
| Pandemia (surge capacity) | 8 pac/h | +80 % sostenido | 6+6 reconversión | 0.87 | Reconversión áreas, cohorting, telemedicina pre-SUH |

### E.3 Estratificación de riesgo en salud mental

**Variables de estratificación**:

| Variable | Fuente | Peso relativo |
|----------|--------|---------------|
| Intentos suicidio previos | HCE | Alto |
| Puntaje Columbia Suicide Severity (C-SSRS) | Evaluación | Alto |
| Hospitalización psiquiátrica ≤12m | HCE | Medio-alto |
| Comorbilidad TUS activa | HCE | Medio-alto |
| Aislamiento social / sin red apoyo | Evaluación social | Medio |
| Abandono tratamiento previo | HCE | Medio |
| Edad 15-24 o >65 | Demográfico | Medio |
| Evento vital reciente (duelo, desempleo) | Evaluación | Bajo-medio |
| PHQ-9 ≥20 (depresión severa) | Escala | Medio |
| Acceso a medios letales | Evaluación | Alto |

**Modelo de priorización**:

| Nivel riesgo | Criterio | Acción |
|--------------|----------|--------|
| Crítico | C-SSRS ≥4 o intento activo | EMC inmediato; hospitalización; contacto ≤24h post-alta |
| Alto | C-SSRS 3 + factores agravantes | Evaluación psiquiátrica ≤24h; seguimiento semanal |
| Moderado | PHQ-9 ≥15 o TUS activo sin red apoyo | Atención SM ≤7d; plan de cuidado integral |
| Bajo | PHQ-9 10-14, red apoyo presente | Atención SM ≤15d; seguimiento APS |
| Mínimo | PHQ-9 <10, estable | Control APS habitual |

---

## Anexo F: Infraestructura y diseño funcional

### F.1 Criterios de superficie y flujo

| Unidad | Superficie mínima | Flujos diferenciados | Requisitos especiales |
|--------|-------------------|---------------------|----------------------|
| SUH (boxes) | 12 m² por box; triaje 15 m² | Limpio/sucio; ambulante/camilla; crítico/general | Presión negativa sala aislamiento; acceso directo ambulancia; señalización por código color |
| Reanimación | 25 m² por puesto | Acceso 360° camilla; circuito directo desde triaje | Gases medicinales (O2, aire, vacío); tomas eléctricas ≥16 por puesto; iluminación ≥500 lux |
| Observación/UOCS | 8-10 m² por puesto | Separación por sexo; circuito corto a imagenología | Monitoreo centralizado; llamado enfermería |
| Unidad SM agudos | 12 m² habitación individual; salón grupal 40 m² | Ingreso controlado; zonas seguras; patio terapéutico | Anti-ligadura (sin puntos de anclaje); visibilidad enfermería; materiales irrompibles |
| HaH (domicilio) | N/A (domicilio paciente) | Zona paciente delimitada; almacenamiento insumos | Conectividad internet ≥10 Mbps; tomacorriente junto a cama; acceso para equipo clínico |

### F.2 Señalética y accesibilidad

- Señalización bilingüe (español + mapudungun en zona pertinente) y pictográfica universal
- Código color por servicio: rojo (urgencias), azul (hospitalización), verde (ambulatorio), morado (SM)
- Wayfinding digital (pantallas) + físico (piso, paredes)
- Accesibilidad universal: rampas ≤8 %, ascensores camilleros, baños adaptados, señalización Braille
- Cumplimiento OGUC (Ordenanza General de Urbanismo y Construcciones) + Ley 20.422

### F.3 Biocontención y decontaminación

- Sala aislamiento presión negativa: ≥12 recambios aire/hora, presión diferencial −2.5 Pa
- Antesala con lavamanos quirúrgico y EPP
- Zona decontaminación (MCI HAZMAT): exterior SUH, drenaje independiente, duchas
- Protocolo donning/doffing señalizado con mirror check
- Gestión REAS (residuos establecimientos asistenciales) según DS 6/2009

---

## Anexo G: Cadena de suministro

### G.1 Listados mínimos por dispositivo

**SUH / EMS:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Monitoreo | Monitor multiparamétrico, desfibrilador (manual + DEA), oxímetro, capnógrafo |
| Vía aérea | Laringoscopio (convencional + video), tubos ET (rango pediátrico-adulto), dispositivos supraglóticos, set cricotirotomía |
| Circulatorio | Bombas infusión, calentador de fluidos, IO (intraóseo), set de toracostomía |
| Imagenología | Ecógrafo point-of-care (POCUS), acceso a TC 24/7 |
| Farmacología | Carro de paro estandarizado (AHA), kit RSI, kit sedación procedural |
| Inmovilización | Tabla espinal, collar cervical, férulas, pelvic binder |

**Salud mental:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Evaluación | Escalas impresas (PHQ-9, GAD-7, Columbia, HoNOS), material psicoeducativo |
| Contención | Contención mecánica certificada (uso excepcional, protocolo estricto), sala de contención acolchada |
| Farmacología | Kit sedación de emergencia (haloperidol, midazolam, lorazepam IM) |
| Seguridad | Alarmas personales staff, botón pánico, CCTV zonas comunes |
| Rehabilitación | Material terapia ocupacional, sala multiuso, espacios exteriores seguros |

**HaH:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Monitoreo RPM | Oxímetro BLE, tensiómetro BLE, termómetro, tablet/hub transmisión |
| Tratamiento | Bomba infusión portátil, concentrador O2 portátil, nebulizador |
| Diagnóstico | Point-of-care testing (glucómetro, INR, PCR rápido) |
| Comunicación | Tablet paciente (videollamada), conectividad 4G/WiFi backup |
| Logística | Kit curación, insumos EV, contenedor REAS domiciliario |

### G.2 Stock crítico y cadena de frío

| Categoría | Criterio stock mínimo | Cadena de frío |
|-----------|----------------------|---------------|
| Medicamentos críticos (carro paro, RSI, AB 1ra línea) | 72h consumo promedio + 50 % buffer | 2-8 °C refrigerados; monitoreo continuo T° |
| Hemoderivados | Según convenio banco de sangre; O− emergencia in situ | 2-6 °C (GR), 20-24 °C (plaquetas), −18 °C (PFC) |
| Vacunas (si aplica) | Según PAI; stock campaña estacional | 2-8 °C; registro digital T° cada 30 min |
| Insumos descartables | 30d consumo; punto reorden automatizado (HCE/ERP) | N/A |
| Gases medicinales | Respaldo ≥48h; manifold con switch automático | N/A |

### G.3 Mantenimiento y ciclo de vida

| Tipo mantenimiento | Frecuencia | Responsable | Registro |
|--------------------|-----------|-------------|---------|
| Preventivo programado | Según fabricante (mensual/trimestral/anual) | Biomédica / proveedor | Ficha equipo + HCE integrada |
| Correctivo | Ante falla; respuesta ≤4h equipos críticos | Biomédica / proveedor | Orden trabajo + downtime log |
| Calibración | Semestral o según norma (INN/NCh) | Laboratorio acreditado | Certificado calibración |
| Obsolescencia | Vida útil según fabricante; evaluación cada 5 años | Comité inversiones | Informe técnico-económico |
| Baja y disposición | Al cumplir vida útil o falla irreparable | Biomédica + finanzas | Acta de baja + disposición REAS |

---

## Anexo H: Marco normativo (adaptación local)

Referencia: [00-indice §5](urn:salud:kb:gestion-redes-indice) — Marco normativo y regulatorio completo.

### Plantilla de adaptación territorial

```yaml
adaptación_territorial:
 servicio_salud: "[Nombre Servicio de Salud]"
 región: "[Región]"
 fecha_adaptación: "YYYY-MM-DD"
 responsable: "[Cargo + nombre]"

 normativa_local:
 - norma: "Resolución exenta N° XXX"
 materia: "[Tema específico]"
 impacto_corpus: "[Capítulo/sección que modifica o complementa]"

 recursos_disponibles:
 establecimientos:
 - nombre: "[Hospital/CESFAM]"
 nivel: "[Primario/Secundario/Terciario]"
 camas: N
 servicios: "[Lista]"
 dotación_total_fte: N
 presupuesto_anual_mm: N

 brechas_identificadas:
 - dominio: "[Ej: Urgencias, SM, HaH]"
 brecha: "[Descripción]"
 plan_cierre: "[Acción + plazo]"

 adaptaciones_específicas:
 - sección_corpus: "[Ej: Cap. 18 Triaje]"
 adaptación: "[Modificación local justificada]"
 aprobado_por: "[Cargo]"

 indicadores_territoriales:
 - indicador: "[KPI adicional local]"
 fórmula: "[Fórmula]"
 meta: "[Meta local]"
 justificación: "[Por qué difiere del corpus]"
```

---

## Anexo I: Referencias clave

**Gestión de redes y sistemas de salud:**
1. OPS/OMS. Redes Integradas de Servicios de Salud (RISS): Conceptos, opciones de política y hoja de ruta. 2010.
2. WHO. Framework on Integrated People-Centred Health Services. 2016.
3. Starfield B. Primary Care: Balancing Health Needs, Services, and Technology. 1998.
4. OCDE. Health at a Glance 2023: OECD Indicators. 2023.
5. MINSAL Chile. Modelo de Atención Integral en Salud Familiar y Comunitaria. 2019.
6. MINSAL Chile. Orientaciones para la implementación del modelo de atención integral. 2023.

**Calidad y seguridad:**
7. IHI. Framework for Improving Joy in Work. 2017.
8. IHI. Psychology of Change Framework. 2020.
9. Donabedian A. The Quality of Care: How Can It Be Assessed? JAMA. 1988.
10. OMS. Marco de acción para la seguridad del paciente 2021-2030. 2021.
11. AHRQ. Making Healthcare Safer III. 2022.

**Urgencias:**
12. ACEP. Emergency Department Benchmarking Alliance. 2023.
13. Gilboy N et al. Emergency Severity Index (ESI) v4. AHRQ. 2020.
14. AHA. Guidelines for CPR and ECC. 2023.
15. Surviving Sepsis Campaign. International Guidelines. 2021.
16. NICE. Emergency and Acute Medical Care for Adults. 2022.
17. ATLS. Advanced Trauma Life Support, 10th ed. ACS. 2018.
18. NFPA. Standard 1710: Organization and Deployment of Fire Suppression Operations, EMS. 2020.

**Salud mental:**
19. OMS. Plan de Acción sobre Salud Mental 2013-2030. 2021.
20. OMS. mhGAP Intervention Guide v2.0. 2022.
21. NICE. Self-harm: Assessment, Management and Preventing Recurrence. 2022.
22. NHS England. Mental Health Services Data Set (MHSDS). 2023.
23. Safewards. Intervention to Reduce Conflict and Containment. 2022.
24. Posner K et al. Columbia-Suicide Severity Rating Scale (C-SSRS). 2011.

**Hospitalización domiciliaria:**
25. Levine DM et al. Hospital-Level Care at Home for Acutely Ill Adults. Ann Intern Med. 2020.
26. Federman AD et al. Association of a Bundled Hospital-at-Home and 30-Day Postacute Transitional Care Program. JAMA Intern Med. 2018.
27. Shepperd S et al. Hospital at Home: Home-Based End-of-Life Care. Cochrane. 2021.
28. Leff B. Defining and Disseminating the Hospital-at-Home Model. CMAJ. 2009.

**Interoperabilidad y salud digital:**
29. HL7 FHIR. Release 4 (R4) Specification. 2019.
30. MINSAL Chile. Guía de interoperabilidad HL7 FHIR CL Core. 2023.
31. HIMSS. Electronic Medical Record Adoption Model (EMRAM). 2023.

**Gestión del cambio y mejora continua:**
32. Kotter JP. Leading Change. Harvard Business Review Press. 2012.
33. Langley GJ et al. The Improvement Guide (Model for Improvement / PDSA). Jossey-Bass. 2009.
34. PMI. A Guide to the Project Management Body of Knowledge (PMBOK), 7th ed. 2021.

**Normativa chilena:**
35. Ley 19.937. Autoridad Sanitaria y Gestión (Redes asistenciales). 2004.
36. Ley 19.966. Régimen de Garantías Explícitas en Salud (GES/AUGE). 2004.
37. Ley 20.584. Derechos y Deberes del Paciente. 2012.
38. Ley 20.422. Igualdad de Oportunidades e Inclusión Social de Personas con Discapacidad. 2010.
39. DS 6/2009. Reglamento sobre manejo de residuos de establecimientos de atención de salud (REAS). 2009.

---

## Anexo J: Índice analítico

| Palabra clave | Archivo | Sección(es) |
|---------------|---------|-------------|
| Alta segura | 01-general, 05-herramientas | Cap. 10; Anexo B.3, C.2 |
| Boarding | 05-herramientas | Anexo A.2, B.1 |
| Cadena de frío | 05-herramientas | Anexo G.2 |
| Camas (gestión) | 01-general, 05-herramientas | Cap. 9; Anexo B.1, C.2 |
| Ciberseguridad | 05-herramientas | Anexo D.4 |
| Columbia (C-SSRS) | 05-herramientas | Anexo A.3, B.4, E.3 |
| Contención (SM) | 05-herramientas | Anexo A.3, G.1 |
| Contrarreferencia | 01-general, 05-herramientas | Cap. 1, 7; Anexo A.1, B.2 |
| Cuádruple Meta | 00-indice, 01-general | §1; Cap. 1.2 |
| DRG / GRD | 01-general, 05-herramientas | Cap. 11; Anexo A.1, A.5 |
| EMS / SAMU | 05-herramientas | Anexo A.2, B.1, B.5, G.1 |
| eReferral | 01-general, 05-herramientas | Cap. 7; Anexo B.2, B.3, D.1 |
| ESI (triaje) | 05-herramientas | Anexo A.2, B.1, C.4, E.1 |
| FHIR | 01-general, 05-herramientas | Cap. 8; Anexo D.1, D.2, D.3 |
| GES / AUGE | 01-general, 05-herramientas | Cap. 5; Anexo A.1 |
| Gobernanza | 00-indice, 01-general, 05-herramientas | §1; Cap. 2; Anexo C.2, K |
| HaH | 05-herramientas | Anexo A.4, B.5, C.1, G.1, K |
| HoNOS | 05-herramientas | Anexo A.3, D.1 |
| IAM (infarto) | 05-herramientas | Anexo A.2, B.1 |
| IAAS | 05-herramientas | Anexo A.4, A.5 |
| KPI | 01-general, 05-herramientas | Cap. 1-14; Anexo A (completo) |
| LOS (estancia) | 05-herramientas | Anexo A.1, A.2, A.4 |
| LWBS | 05-herramientas | Anexo A.2 |
| Madurez (modelo) | 05-herramientas | Anexo K |
| MCI (incidente masivo) | 05-herramientas | Anexo E.2 |
| Mejora continua (PDSA) | 01-general, 05-herramientas | Cap. 4; Anexo C.2 |
| NPS | 05-herramientas | Anexo A.1, A.5 |
| PDSA | 01-general, 05-herramientas | Cap. 4; Anexo C.2, I |
| PHQ-9 | 05-herramientas | Anexo A.3, E.3 |
| PREMs | 05-herramientas | Anexo A.1, A.2, A.3, A.4 |
| RACI | 05-herramientas | Anexo C.2 |
| RPM (monitoreo remoto) | 05-herramientas | Anexo A.4, B.5, D.2, G.1 |
| Sepsis | 05-herramientas | Anexo A.2, B.1 |
| Simulación | 05-herramientas | Anexo E.1, E.2 |
| SLA | 05-herramientas | Anexo C.1 |
| SM (salud mental) | 05-herramientas | Anexo A.3, B.4, C.1, E.3, K |
| SNOMED CT | 05-herramientas | Anexo D.3 |
| SOP | 05-herramientas | Anexo A.1, C.4 |
| Suicidio | 05-herramientas | Anexo A.3, B.4, C.1, E.3 |
| Triaje | 05-herramientas | Anexo A.2, B.1, C.4, E.1 |
| Trombolisis / trombectomía | 05-herramientas | Anexo A.2, C.1 |

---

## Anexo K: Modelo de madurez

### Rúbrica de madurez: 7 dominios × 5 niveles

| Dominio | 1 — Inicial | 2 — Definido | 3 — Estandarizado | 4 — Gestionado | 5 — Optimizado |
|---------|-------------|-------------|-------------------|----------------|----------------|
| **Gobernanza** | Sin estructura formal; decisiones reactivas ad-hoc | Organigrama definido; comités constituidos sin periodicidad regular | Roles RACI asignados; reuniones programadas; convenios inter-nodos vigentes | KPIs de gestión monitoreados; decisiones basadas en datos; rendición de cuentas activa | Gobernanza adaptativa; benchmarking sistemático; ciclos OKR integrados con planificación estratégica |
| **Integración clínica** | Derivaciones en papel; sin contrarreferencia; fragmentación severa | Proceso de referencia definido; contrarreferencia esporádica (<30 %) | eReferral electrónico; contrarreferencia ≥60 %; protocolos derivación por patología | Trazabilidad completa paciente en red; navigator; contrarreferencia ≥80 % en ≤7d | Continuidad longitudinal medida (UPC ≥0.75); integración bidireccional tiempo real; coordinación proactiva |
| **Calidad y seguridad** | Sin reporte de incidentes; auditorías inexistentes | Sistema reporte incidentes implementado; comité calidad constituido | SOPs vigentes ≥80 %; auditorías programadas; cultura de reporte incipiente | Ciclos PDSA con mejoras sostenidas; EA monitoreados; acreditación vigente | Cultura justa instalada; HRO (alta confiabilidad); mejora continua basada en analítica predictiva |
| **Salud digital** | HCE parcial o en papel; sin interoperabilidad | HCE en producción; interfaces punto a punto | HCE integrada red; perfiles FHIR CL Core; terminologías estandarizadas (SNOMED, LOINC) | Bus de eventos clínicos; dashboards KPI en tiempo real; uptime ≥99.5 % | Analítica predictiva; IA embebida en flujos clínicos; interoperabilidad semántica completa |
| **Urgencias** | Sin triaje estructurado; tiempos no medidos | ESI implementado; door-to-triage medido; protocolos tiempo-dependientes documentados | Cumplimiento door-to-doctor ≤30 min; LWBS ≤5 %; boarding monitorizado | Boarding ≤2h; protocolos tiempo-dependientes con cumplimiento ≥85 %; gestión de flujo activa | Full-capacity protocol automatizado; predicción demanda; zero-boarding sostenido; integración EMS-SUH seamless |
| **Salud mental** | Atención episódica; sin seguimiento post-alta; sin equipo comunitario | Equipo SM constituido; protocolo crisis documentado; seguimiento post-alta definido | Retención ≥50 %; EMC operativo; PCI en ≥60 % usuarios; contenciones en descenso | Seguimiento post-alta suicidio 100 %; outcomes medidos (PHQ-9, HoNOS); integración SM-APS | Recovery-oriented; cero contención como meta; estratificación predictiva; red comunitaria articulada |
| **HaH** | Sin programa; todo paciente se hospitaliza convencionalmente | Piloto HaH en marcha; criterios elegibilidad definidos; equipo dedicado | RPM operativo 24/7; escalamiento ≤10 %; LOS ≤3.2d; SLA respuesta deterioro definido | Costo por episodio ≤80 % DRG; readmisión ≤8.6 %; PREMs ≥85; integración con APS egreso | Modelo predicción elegibilidad; HaH como opción por defecto para diagnósticos elegibles; analítica en tiempo real |

**Uso**: evaluar cada dominio independientemente. Nivel global = mínimo entre dominios (cadena más débil). Plan de mejora prioriza dominios en nivel 1-2.

---

*Ref cruzada*: [00-indice](urn:salud:kb:gestion-redes-indice) | [01-general](urn:salud:kb:gestion-redes-general)
