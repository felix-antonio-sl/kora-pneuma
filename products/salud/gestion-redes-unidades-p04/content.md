---
urn: urn:salud:kb:gestion-redes-unidades-p04
nombre: gestion-redes-unidades-p04
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes Asistenciales — Gestión por Tipo de Unidad - Parte 04"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/02-unidades-asistenciales--p04.md (sha256:15d4f40b13c17af30f89830902302609a24c26c1ea2a8b826d569a3f15982360) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-unidades."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, unidades, ambulatorio, hospitalario, hospital-at-home, HaH, asistencial]
familia: bok
cita: [urn:salud:kb:gestion-redes-unidades]
---

# Gestión de Redes Asistenciales — Gestión por Tipo de Unidad - Parte 04

## 17.5 Vías clínicas prevalentes

Protocolos clínico-operativos por patología. Cada vía define: tratamiento estándar, monitoreo específico, criterios de switch terapéutico y umbrales de escalamiento.

**ICC descompensada:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Diuréticos IV (furosemida) → transición oral según respuesta, IECA/ARA2, betabloqueadores |
| Monitoreo | Peso diario (alerta +1.5 kg/24h), balance hídrico, SpO2, PA, FC, ingesta Na |
| Switch IV→oral | IF diuresis >1 L en 4h + peso descendente + SpO2 >93 % THEN switch a oral |
| Escalamiento | IF no respuesta diurético 48h OR SpO2 <88 % OR edema pulmonar THEN retorno hospital |

**EPOC exacerbado:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Broncodilatadores nebulizados, corticoides sistémicos (5d), O2 titulado (meta SpO2 88-92 %), antibiótico si purulento |
| Monitoreo | SpO2 continuo, FR, volumen esputo, disnea (escala mMRC), flujo espiratorio |
| Switch | IF SpO2 estable >90 % sin O2 + FR <24 + mejoría subjetiva THEN suspender O2, mantener inhaladores |
| Escalamiento | IF SpO2 <85 % OR FR >30 OR deterioro conciencia THEN retorno hospital/UCI |

**NAC (Neumonía adquirida en la comunidad):**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antibiótico IV (ceftriaxona ± azitromicina según CURB-65/PSI), switch therapy |
| Monitoreo | Temperatura, SpO2, FR, respuesta clínica 48-72h, Rx portátil control |
| Switch IV→oral | IF afebril ≥24h + SpO2 >93 % + tolerancia oral + mejoría clínica THEN switch amoxicilina-clavulánico oral |
| Escalamiento | IF fiebre persistente >72h OR SpO2 <90 % OR inestabilidad THEN retorno hospital, re-evaluación |

**ITU/Pielonefritis:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antimicrobiano IV (ceftriaxona/gentamicina), hidratación, control función renal |
| Monitoreo | Temperatura, diuresis, creatinina seriada, urocultivo control |
| Switch IV→oral | IF afebril ≥24h + creatinina estable/descendente THEN switch ciprofloxacino/cefalosporina oral |
| Escalamiento | IF fiebre >72h OR deterioro función renal OR sepsis THEN retorno hospital |

**Celulitis:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Antibiótico IV (cloxacilina/cefazolina), elevación, marcación diaria del borde |
| Monitoreo | Fotografía diaria con regla, temperatura, marcación borde lesión, PCR seriada |
| Switch IV→oral | IF reducción eritema + afebril 24h + PCR descendente THEN switch cloxacilina oral |
| Escalamiento | IF progresión pese a 48h IV OR fiebre persistente OR sospecha fascitis THEN retorno hospital |

**TVP/TEP estable:**

| Componente | Detalle |
|------------|---------|
| Tratamiento | Anticoagulación (HBPM → DOAC), compresión elástica (TVP), analgesia |
| Monitoreo | Edema (circunferencia), SpO2 (TEP), signos sangrado, adherencia anticoagulante |
| Switch | IF HBPM ≥5d + estable THEN switch DOAC oral |
| Escalamiento | IF aumento edema + dolor OR SpO2 <92 % OR sangrado THEN retorno hospital |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Switch IV→oral oportuno | Switches en criterio / Total elegibles × 100 | ≥85 % | — | Buena práctica HaH | Mensual |
| Escalamiento a hospital | Retornos / Total episodios por patología × 100 | ≤10 % | 7-10 % global | Levine 2020 | Mensual |
| Cumplimiento protocolo vía | Auditoría adherencia protocolo / Total casos × 100 | ≥90 % | — | Buena práctica | Trimestral |
| Resolución clínica | Pacientes con resolución completa al egreso HaH / Total × 100 | ≥85 % | — | HaH literature | Mensual |
| Rx portátil en NAC | Rx realizado en domicilio / Rx indicado × 100 | ≥90 % | — | Buena práctica | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Switch prematuro → recaída | Criterios objetivos documentados, evaluación médica presencial pre-switch |
| Demora en escalamiento | Umbrales claros, educación cuidador en signos alarma, alerta RPM |
| Resistencia antimicrobiana | Cultivo previo a antibiótico, de-escalamiento según antibiograma |

Ref: IDSA/ATS NAC Guidelines 2019; ESC ICC Guidelines 2021; GOLD EPOC 2023; NICE CG191 TEP; Johns Hopkins HaH clinical pathways; Hospital Clínic Barcelona vías clínicas HaH.

## 17.6 Calidad, seguridad y experiencia del paciente

Marco de calidad específico HaH: seguridad medicamentosa, evaluación ambiental, protocolos de escalamiento, preservación funcional y experiencia superior del paciente.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Seguridad medicamentosa | Conciliación al ingreso HaH, doble verificación IV, almacenamiento seguro domicilio, devolución al egreso |
| Checklist ambiental domicilio | Caídas (alfombras, iluminación, baño), seguridad O2 (no fumar, ventilación), eléctrica (enchufes, extensiones), mascotas |
| Protocolo escalamiento | Criterios retorno hospital predefinidos por patología, umbral bajo, tasa retorno ~10 % aceptable |
| Preservación funcional | Menos inmovilización que hospital, accelerómetro: +17 min/d ambulando, menos delirium (9 % vs 24 %) |
| Experiencia paciente | Confort domicilio, privacidad, sueño no interrumpido, alimentación propia, acompañamiento familiar continuo |
| Eventos adversos | Registro, análisis, clasificación (medicamentosos, caídas, deterioro, infección dispositivo) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Eventos adversos HaH | EA / 1.000 días-paciente HaH | <10 ‰ | Similar o menor a hospitalización | Levine 2020 | Mensual |
| Satisfacción paciente HaH | Score encuesta experiencia | ≥90 % | 90.7 % HaH vs 83.9 % convencional | Leff 2005 | Trimestral |
| Delirium incidente | Nuevos delirium / Total pacientes >65 años × 100 | <10 % | 9 % HaH vs 24 % convencional | Caplan 2006 | Trimestral |
| Caídas con daño | Caídas con lesión / 1.000 días-paciente | <3 ‰ | Similar hospitalización | Cochrane 2016 | Mensual |
| Checklist ambiental cumplido | Checklists completos / Total ingresos × 100 | 100 % | — | Buena práctica | Mensual |
| Tasa retorno hospital | Retornos / Total episodios × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Caída domiciliaria | Evaluación ambiental pre-ingreso, adaptaciones, kinesiólogo |
| Incidente con O2 domiciliario | Checklist seguridad O2, educación no fumar, ventilación |
| Subregistro de EA | Cultura reporte, entrevista egreso, seguimiento post-alta |

Ref: Levine et al. Annals IM 2020; Leff et al. JAGS 2005; Caplan et al. MJA 2006; AHRQ Patient Safety in HaH 2022; IHI Framework for Safe Reliable and Effective Care.

## 17.7 Cuidadores informales y entorno

El cuidador informal es co-productor de la atención en HaH. Requiere capacitación, soporte emocional y evaluación de sobrecarga. El entorno domiciliario debe ser clínicamente seguro.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Capacitación cuidador | Lectura dispositivos RPM, administración medicamentos orales, signos alarma por patología, cuándo llamar |
| Soporte emocional | Screening sobrecarga (Zarit abreviado), derivación apoyo psicológico, grupos pares |
| Evaluación ambiental | Visita pre-ingreso: espacio, higiene, accesibilidad, seguridad, almacenamiento medicamentos |
| Brecha digital | Evaluación alfabetización digital, capacitación en dispositivos, soporte técnico |
| Tensiones culturales | Respeto creencias, comunicación intercultural, mediador si necesario |
| Relevo cuidador | Identificar cuidador secundario, planificación turnos, reconocer fatiga |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Zarit cuidador (screening) | Cuidadores evaluados / Total cuidadores × 100 | 100 % | — | Buena práctica | Al ingreso + semanal |
| Sobrecarga cuidador (Zarit ≥24) | Cuidadores con sobrecarga / Total evaluados × 100 | <20 % | — | Zarit literature | Mensual |
| Capacitación completada | Cuidadores capacitados pre-inicio / Total × 100 | 100 % | — | Buena práctica | Por ingreso |
| Llamadas alarma apropiadas | Llamadas por signos alarma reales / Total llamadas cuidador × 100 | ≥60 % | — | Buena práctica | Mensual |
| Satisfacción cuidador | Score encuesta experiencia cuidador | ≥80 % | — | Literature HaH | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Burnout cuidador → abandono | Screening Zarit, relevo, apoyo psicosocial, respiro |
| Incapacidad digital → pérdida monitoreo | Dispositivos simplificados, soporte técnico, visita adicional enfermería |
| Conflicto familiar por decisiones | Mediación, consentimiento claro, rol definido del cuidador |
| Domicilio inseguro (no detectado) | Visita pre-ingreso obligatoria, re-evaluación periódica |

Ref: Zarit Burden Interview validación; Cuidador informal OPS 2019; Levine et al. 2020 (caregiver experience); Hospital Clínic Barcelona programa cuidador HaH.

## 17.8 Economía, sostenibilidad y reembolso

HaH reduce costos 19-38 % por episodio. Efecto backfill amplifica el impacto financiero. Modelos de pago variados según sistema sanitario.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Costo directo por episodio | 19-38 % menor que hospitalización convencional (estudios USA, Australia, España) |
| Efecto backfill | Cama liberada por HaH → ingresa paciente mayor agudeza → mayor ingreso GRD/DRG → margen incremental |
| Costos fijos programa | Centro de mando, flota, equipos RPM, stock medicamentos — requiere volumen mínimo para break-even |
| Break-even | Típicamente 8-12 pacientes simultáneos para programa sostenible |
| Costo evitado sistema | Menos IAAS, menos delirium, menos desacondicionamiento → menores costos downstream |

**Modelos de reembolso:**

| Modelo | País/Sistema | Detalle |
|--------|-------------|---------|
| DRG parity (AHCAH waiver) | USA / CMS | Mismo pago DRG que hospitalización convencional → margen para hospital por menor costo |
| Value-based | USA / ACO-REACH | Ahorro compartido, penalización reingresos, calidad |
| Capitado | Integrados (Kaiser, VA) | HaH como alternativa de menor costo dentro del per cápita |
| Presupuesto global | UK NHS / Virtual Wards | Financiamiento NHS Trusts, eficiencia cama |
| GRD nacional | España, Chile, Australia | Codificación HaH como hospitalización, mismo GRD ajustado |
| Fee-for-service ajustado | Francia | Tarifas específicas HAD (Hospitalisation à Domicile) |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Costo por episodio HaH vs. convencional | Ratio costo HaH / costo convencional | ≤0.80 | 0.62-0.81 | CMS 2023; Levine 2020 | Trimestral |
| Volumen programa (census) | Pacientes simultáneos promedio | ≥8 (break-even) | JHH 15-20 | Johns Hopkins 2022 | Mensual |
| Margen backfill | Ingreso incremental por camas liberadas / mes | >0 (positivo) | — | Análisis interno | Trimestral |
| Costo por día-paciente HaH | Costo total programa / Total días-paciente | Benchmarking interno | USD 400-600/d vs 700-1200/d | USA literature | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Volumen insuficiente → programa deficitario | Criterios elegibilidad amplios, marketing interno, derivación protocolizada |
| No reconocimiento pagador | Advocacy regulatoria, evidencia local, piloto con evaluación |
| Costos ocultos (cuidador, tiempo familia) | Evaluación costo social, apoyo cuidador, comunicación transparente |

Ref: CMS AHCAH Financial Impact Report 2023; Levine et al. Annals IM 2020; Klein et al. Health Affairs 2022 (backfill); Hospital Clínic Barcelona coste-efectividad 2021.

## 17.9 Normativa, habilitación y consentimiento

Marco regulatorio para operar HaH. Consentimiento informado específico, habilitación sanitaria, privacidad de datos RPM y responsabilidad profesional.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Habilitación sanitaria | Autorización SEREMI/Servicio de Salud según normativa local, estándares de acreditación |
| Consentimiento informado | Documento específico HaH: riesgos, condiciones re-hospitalización, monitoreo, responsabilidades cuidador, derecho a retirarse |
| Privacidad datos RPM | Cumplimiento Ley 19.628 (datos personales), encriptación, consentimiento explícito para monitorización |
| Responsabilidad profesional | Cobertura seguro, protocolos de actuación, registro clínico completo en HCE |
| Derechos del paciente | Ley 20.584 aplicable en domicilio: información, consentimiento, confidencialidad, acompañamiento |
| Acreditación | Integración en proceso acreditación institucional, estándares específicos HaH |

**Contenido mínimo consentimiento HaH:**

| Sección | Contenido |
|---------|-----------|
| Naturaleza | Descripción del programa, equivalencia a hospitalización, equipo tratante |
| Riesgos | Posibilidad deterioro, tiempo respuesta, limitaciones vs. hospital |
| Monitorización | Dispositivos, frecuencia visitas, datos transmitidos, quién accede |
| Condiciones retorno | Criterios clínicos de re-hospitalización, proceso, transporte |
| Responsabilidades cuidador | Rol esperado, capacitación, límites, derecho a solicitar apoyo |
| Derecho retiro | Puede solicitar hospitalización convencional en cualquier momento, sin consecuencias |
| Privacidad | Uso de datos, almacenamiento, compartición con equipo tratante |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Consentimiento firmado | Consentimientos firmados / Total ingresos HaH × 100 | 100 % | Regulatorio | Ley 20.584 | Por ingreso |
| Cumplimiento normativo | Auditoría cumplimiento / Total ítems regulatorios × 100 | 100 % | Regulatorio | SEREMI | Anual |
| Reclamos privacidad | Reclamos relacionados privacidad/datos | 0 | — | Buena práctica | Trimestral |
| Registro clínico completo | Episodios con registro completo HCE / Total × 100 | 100 % | — | Acreditación | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Vacío normativo (Chile: no regulación HaH específica) | Resolución interna, protocolo con respaldo jurídico, advocacy MINSAL |
| Consentimiento insuficiente → litigio | Documento revisado por jurídico, checklist comprensión, testigo |
| Brecha privacidad datos RPM | Encriptación, acceso restringido, auditoría, política datos |

Ref: Ley 20.584 (Derechos del Paciente Chile); Ley 19.628 (Datos Personales); CMS AHCAH Conditions of Participation 2023; RD 1030/2006 (España — HAD); SEHAD recomendaciones jurídicas.

## 17.10 Programas internacionales de referencia

Panorama global de programas HaH consolidados. Modelos, escala, lecciones aprendidas y tendencias.

**Componentes:**

| País/Sistema | Programa | Escala | Modelo predominante | Detalle clave |
|-------------|----------|--------|---------------------|---------------|
| USA — CMS | AHCAH Waiver | >300 hospitales, >140 sistemas | Admission avoidance + ESD | Waiver extendido a 2030, pago DRG parity, 2 visitas/d RN, RPM obligatorio |
| USA — Johns Hopkins | Hospital at Home (pionero) | Desde 1995, modelo replicado globalmente | Admission avoidance | Evidencia fundacional (Leff, Levine), criterios elegibilidad de referencia |
| USA — Mount Sinai | Mobile Acute Care Team | NYC, >5.000 pacientes | Admission avoidance | Integración paramédicos, telemedicina, comunidad urbana |
| USA — MGB | Home Hospital | Boston, Mass General Brigham | Admission avoidance | RCT Levine 2020: -38 % costo, -7d LOS, satisfacción superior |
| UK — NHS | Virtual Wards | ~12.000 camas equivalentes (2024) | Ambos | Scaling nacional, RPM + visitas, integración community trusts |
| España — SEHAD | Hospitalización a Domicilio | >100 unidades, >4.000 camas | Ambos | Hospital Clínic Barcelona: referencia mundial, >30 años experiencia, 80+ camas |
| Australia | HITH (Hospital in the Home) | ~6 % días-cama Victoria | Ambos | Marco regulatorio consolidado, financiamiento estatal, evaluación AIHW |
| Francia | HAD (Hospitalisation à Domicile) | >20.000 plazas | Ambos | Financiamiento específico T2A, cobertura nacional, Fédération FNEHAD |
| Israel | Sheba, Clalit | Programas hospitalarios + HMO | Admission avoidance | Adopción rápida post-COVID, integración digital avanzada |
| Canadá | Ontario, Alberta | Programas hospitalarios provinciales | ESD predominante | Expansión post-COVID, integración home care agencies |

**Lecciones aprendidas (síntesis internacional):**

| Lección | Detalle |
|---------|---------|
| Escala mínima | 8-12 pacientes simultáneos para viabilidad operativa y financiera |
| Tecnología como enabler, no driver | RPM facilita seguridad pero no reemplaza visita presencial |
| Cultura organizacional | Requiere cambio mental: hospital sin paredes, confianza en domicilio |
| Cuidador como aliado | Capacitación y soporte emocional son inversiones, no costos |
| Regulación habilita escala | Sin marco normativo claro, programas permanecen pilotos pequeños |
| COVID como acelerador | Pandemia demostró viabilidad a escala, ahora desafío es sostener post-pandemia |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Benchmark internacional mortalidad | Mortalidad HaH propia vs. publicada | ≤benchmark | RR 0.77-0.84 | Cochrane 2016 | Anual |
| Benchmark reingresos | Reingresos HaH propios vs. publicados | ≤10 % | 7-8.6 % | Levine 2020 | Anual |
| Benchmark costo | Ratio costo propio vs. publicado | ≤0.80 | 0.62-0.81 | CMS 2023 | Anual |
| Adherencia modelo operativo | Cumplimiento estándares CMS/SEHAD / Total ítems × 100 | ≥90 % | — | CMS/SEHAD | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Trasplantar modelo sin adaptación local | Contextualización: geografía, cultura, sistema salud, regulación |
| Dependencia de waiver/excepción regulatoria | Advocacy para regulación permanente, evidencia local |
| Post-COVID deceleration | Institucionalización, demostración valor financiero sostenido |

Ref: CMS AHCAH Waiver Extension 2024; Leff et al. JAGS 2005; Levine et al. Annals IM 2020; NHS England Virtual Wards 2024; SEHAD España; FNEHAD Francia; AIHW HITH Australia 2023; Hospital Clínic Barcelona HaD.
