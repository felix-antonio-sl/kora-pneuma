---
urn: urn:salud:kb:gestion-redes-salud-mental-p04
nombre: gestion-redes-salud-mental-p04
version: 2.0.0
estado: publicado
descripcion: "Gestión de Redes — Salud Mental y Adicciones - Parte 04"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/gestion-redes/04-salud-mental--p04.md (sha256:3b1193ea98c95bec952e8b163b9b6415d4679396e35ba2c899ccc1108acf02b2) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:gestion-redes-salud-mental."
autor: FS
creado: 2026-03-03
lang: es
tags: [gestion-redes, salud-mental, adicciones, crisis, suicidio, TUS, derechos, PROMs]
familia: bok
cita: [urn:salud:kb:gestion-redes-salud-mental, urn:salud:kb:gestion-redes-general]
---


# Gestión de Redes — Salud Mental y Adicciones - Parte 04

## 32.4 PROMs en SM

Instrumentos estandarizados de resultados reportados por paciente para monitoreo clínico y evaluación de servicios SM.

**Instrumentos principales:**

| Instrumento | Dominio | Población | Corte clínico | Cambio significativo | Ref |
|-------------|---------|-----------|---------------|---------------------|-----|
| PHQ-9 | Depresión | Adultos | ≥10 moderada; ≥20 severa | ↓≥5 puntos | Kroenke 2001 |
| GAD-7 | Ansiedad | Adultos | ≥10 moderada | ↓≥4 puntos | Spitzer 2006 |
| HoNOS | Funcionamiento global | Adultos | Por ítem (0-4) | ↓≥2 total | Wing 1998 |
| SDQ | SM infanto-juvenil | 4-17 años | ≥17 anormal | — | Goodman 1997 |
| AUDIT | Consumo alcohol | Adultos | ≥8 riesgo; ≥20 dependencia | — | OMS |
| C-SSRS | Riesgo suicida | Todos | Niveles 1-5 | — | Posner 2011 |
| Edinburgh (EPDS) | Depresión perinatal | Perinatal | ≥13 probable depresión | — | Cox 1987 |
| Zarit | Sobrecarga cuidador | Cuidadores | ≥47 sobrecarga | — | Zarit 1980 |
| ASSIST | Consumo sustancias | Adultos | Moderado ≥4-26; Alto ≥27 | — | OMS |
| WHO-DAS 2.0 | Discapacidad funcional | Adultos | Percentiles por población | — | OMS 2010 |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Monitoreo rutinario (ROM) | Aplicación seriada de PROMs en cada contacto clínico, registro en HCE |
| Feedback al clínico | Visualización gráfica de trayectoria PROMs para ajuste tratamiento |
| Feedback al usuario | Compartir resultados con usuario como herramienta de co-decisión |
| Agregación para gestión | Dashboards por dispositivo, programa, red — análisis de outcomes |
| Benchmarking | Comparación inter-dispositivos ajustada por case-mix |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura PROMs | Usuarios con ≥2 mediciones PROMs / Total usuarios activos × 100 | ≥70 % | UK IAPT 95 % | NHS IAPT 2022 | Trimestral |
| Reliable improvement (PHQ-9) | Usuarios con ↓≥6 puntos / Total con PHQ-9 pre-post × 100 | ≥50 % | IAPT 50 % | Clark 2018 | Semestral |
| Recovery rate (PHQ-9 <10 post) | Usuarios que cruzan umbral clínico / Total sobre umbral al inicio × 100 | ≥40 % | IAPT 50 % | Clark 2018 | Semestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| PROMs como carga burocrática sin uso clínico | Integrar en sesión clínica, feedback visual, capacitación |
| Gaming (manipulación de scores) | Triangulación con HoNOS clínico + indicadores funcionales |
| Instrumentos no validados culturalmente | Usar versiones chilenas validadas, adaptación pueblos originarios |

Ref: Kroenke 2001 (PHQ-9); Spitzer 2006 (GAD-7); Wing 1998 (HoNOS); Clark 2018 (IAPT outcomes); ICHOM Standard Sets MH 2017.

## 32.5 Ética de datos y consentimiento

Marco ético-legal para protección de datos sensibles de SM, consentimiento informado digital y autonomía del usuario.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Datos sensibles SM | Diagnósticos, notas terapéuticas, TUS, conducta suicida — protección reforzada |
| Consentimiento informado digital | Proceso documentado para recolección, almacenamiento y uso de datos SM |
| Derecho a rectificación | Usuario puede solicitar corrección de datos SM inexactos |
| Derecho a restricción | Usuario puede limitar compartición de datos SM entre servicios |
| Investigación con datos SM | Comité ética obligatorio, anonimización, consentimiento específico |
| IA y datos SM | Algoritmos predictivos requieren evaluación ética, transparencia, consentimiento |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Consentimiento digital documentado | Usuarios con consentimiento datos registrado / Total usuarios SM × 100 | 100 % | — | Ley 21.331 | Trimestral |
| Solicitudes rectificación atendidas | Solicitudes resueltas <30d / Total solicitudes × 100 | ≥95 % | — | Ley 19.628 | Trimestral |
| Brechas de datos SM | Incidentes seguridad datos SM / año | 0 | — | Gestión TI | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Uso secundario de datos SM sin consentimiento | Gobernanza de datos con comité ética, auditoría uso |
| Sesgos algorítmicos en IA aplicada a SM | Evaluación de equidad por grupo vulnerable, validación externa |
| Re-identificación en datos anonimizados | k-anonimato ≥5, eliminación de cuasi-identificadores |

Ref: Ley 21.331 art. 15; Ley 19.628; GDPR art. 9 (referencia comparativa); OMS Ethics and Governance of AI for Health 2021.

## 33. Calidad, seguridad y derechos en SM

Marco base: ver [Calidad, seguridad y gestión de riesgos](urn:salud:kb:gestion-redes-general) cap 10. Esta sección agrega los deltas específicos de salud mental y el marco de derechos.

## 33.1 Ambientes terapéuticos seguros

Diseño y gestión del entorno físico para prevenir autolesiones, heteroagresiones y promover la recuperación.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Ligature-free | Eliminación de puntos de ligadura: barras, perillas, bisagras, duchas — diseño anti-ligadura certificado |
| Observación diferenciada | Niveles: general (cada 60 min), intermitente (cada 15 min), continua (1:1), constante (arms-length) |
| Espacio de desescalada | Sala sensorial de baja estimulación, disponible 24/7, acceso voluntario |
| Objetos peligrosos | Control de objetos cortantes, cuerdas, medicamentos — inventario por turno |
| Espacio exterior | Acceso a patio/jardín terapéutico, actividad física supervisada |
| Rondas de seguridad ambiental | Inspección diaria de infraestructura, puntos de riesgo, puertas |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Autolesiones intrahospitalarias | N° eventos autolesión / 1.000 días-cama SM | ≤2 | — | Joint Commission | Mensual |
| Rondas seguridad completadas | Rondas realizadas / Rondas programadas × 100 | 100 % | — | Gestión interna | Diaria |
| Evaluación ambiental ligature-free | % áreas evaluadas sin puntos ligadura / Total áreas × 100 | 100 % | — | Joint Commission | Semestral |
| Incidentes heteroagresión | N° agresiones / 1.000 días-cama SM | ≤3 | — | Gestión interna | Mensual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Infraestructura antigua con puntos de ligadura | Plan de inversión priorizado, auditoría joint commission, mitigaciones transitorias |
| Falsa sensación de seguridad post-intervención | Rondas periódicas, cultura de reporte, evaluación continua |

Ref: Joint Commission Environmental Risk Assessment 2019; NHS Ligature Risk Reduction Standards 2018; NICE NG10 2015.

## 33.2 Prevención del suicidio

Estrategia integral de prevención del suicidio a nivel de red, dispositivos y comunidad.

**Screening:**

| Instrumento | Umbral | Acción |
|-------------|--------|--------|
| PHQ-9 ítem 9 | ≥1 (cualquier respuesta positiva) | Activa evaluación C-SSRS completa |
| C-SSRS nivel 1-2 | Ideación pasiva | Safety plan + seguimiento ambulatorio <7d |
| C-SSRS nivel 3 | Ideación activa con método | Evaluación psiquiátrica <24h |
| C-SSRS nivel 4-5 | Intención/plan/intento | Hospitalización o contención terapéutica inmediata |

**Safety Planning (modelo Stanley-Brown, 6 pasos):**

| Paso | Contenido |
|------|-----------|
| 1. Señales de alarma | Pensamientos, imágenes, situaciones que preceden a la crisis |
| 2. Estrategias internas | Técnicas de afrontamiento autónomas (distracción, relajación, ejercicio) |
| 3. Personas/lugares de distracción | Contactos sociales y espacios que distraen de pensamientos suicidas |
| 4. Personas que pueden ayudar | Familiares/amigos a quienes pedir apoyo, con teléfono |
| 5. Profesionales/agencias | Clínico tratante, línea crisis (*4141), SUH más cercano |
| 6. Restricción de medios | Identificar y restringir acceso a medios letales (armas, medicamentos, tóxicos) |

**Contacto post-alta:**

| Plazo | Evidencia | Acción |
|-------|-----------|--------|
| <24h (riesgo alto) | Reduce mortalidad post-alta | Llamada estructurada + verificación safety plan |
| <72h (todos con riesgo) | Ventana máximo riesgo: 30 % mortalidad reducida (Motto & Bostrom 2001) | Contacto telefónico o presencial |
| 7 días | Cita ambulatoria primera | Sesión presencial COSAM/APS |
| 30 días | Período crítico | Al menos 4 contactos durante primer mes |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Screening PHQ-9 ítem 9 | Evaluaciones con ítem 9 revisado / Total PHQ-9 aplicados × 100 | 100 % | — | Joint Commission NPSG | Mensual |
| Safety plans completados (riesgo moderado+) | Safety plans / Usuarios C-SSRS ≥3 × 100 | 100 % | — | Stanley 2012 | Mensual |
| Contacto post-alta <72h | Contactos <72h / Total altas con riesgo suicida × 100 | ≥95 % | UK 80 %; meta 95 % | NICE NG225 | Mensual |
| Restricción de medios documentada | Intervenciones restricción medios / Usuarios riesgo alto × 100 | ≥90 % | — | Yip 2012 | Mensual |
| Tasa suicidio en usuarios activos SM | Suicidios / 100.000 usuarios activos SM | ≤50 | UK 40-60 | NCISH 2023 | Anual |
| Suicidio intrahospitalario | N° suicidios / 100.000 admisiones SM | 0 objetivo | UK <1 | NCISH 2023 | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Safety plan no actualizado post-crisis | Revisión obligatoria después de cada evento crisis |
| No contactar post-alta (ventana letal) | Alerta automática en HCE, responsable designado, escalamiento si no contactable |
| Acceso persistente a medios letales | Intervención activa con familia, seguimiento restricción, coordinación judicial si armas |
| Contagio/efecto Werther en unidades | Protocolo post-vención, seguimiento de co-pacientes, debrief equipo |

Ref: Stanley & Brown 2012; Posner 2011 (C-SSRS); NICE NG225 2022; Motto & Bostrom 2001; Yip 2012 (means restriction); NCISH Annual Report 2023.

## 33.3 Contenciones proporcionales

Uso de contenciones mecánicas y farmacológicas como último recurso, regulado por Ley 21.331 y estándares internacionales.

**IF/THEN — Escalonamiento:**

| Condición | Acción | Requisito |
|-----------|--------|-----------|
| Agitación leve | Desescalada verbal exclusiva | Siempre primer abordaje |
| Agitación moderada, verbal insuficiente | Contención farmacológica (BZD VO preferente) | Prescripción médica, consentimiento si posible |
| Riesgo inminente de daño | Contención mecánica transitoria | Orden médica, tiempo máximo definido, revisión cada 15 min |
| Contención >2h continua | Reevaluación médica obligatoria | Justificación documentada, alternativa explorada |
| Post-contención | Debriefing con usuario y equipo <24h | Registro en HCE, reporte evento adverso |

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Registro obligatorio | Motivo, hora inicio/fin, tipo contención, evaluaciones periódicas, estado usuario |
| Tiempo máximo | Definido por protocolo local; Ley 21.331 exige proporcionalidad y temporalidad |
| Monitoreo continuo | Signos vitales cada 15 min, estado emocional, necesidades básicas (hidratación, baño) |
| Debriefing | Revisión con usuario: experiencia vivida, alternativas futuras, disculpa si corresponde |
| Reporte | Todo episodio contención como evento centinela, análisis de causa raíz si recurrente |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa contención mecánica | N° contenciones mecánicas / 1.000 días-cama SM | ≤3 | UK ≤2 (NICE) | NICE NG10 | Mensual |
| Duración promedio contención | Minutos promedio por episodio | ≤30 min | — | Ley 21.331 | Mensual |
| Debriefing post-contención | Debriefings realizados / Total contenciones × 100 | 100 % | — | Gestión interna | Mensual |
| Lesiones durante contención | N° lesiones (usuario o personal) / Total contenciones × 100 | ≤5 % | — | Gestión riesgo | Mensual |
| Tendencia reducción | Variación tasa contención trimestre actual vs anterior | Tendencia ↓ | — | Gestión interna | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Normalización de contenciones por cultura institucional | Liderazgo visible en reducción, benchmark público, meta cero |
| Lesiones durante contención | Capacitación técnica certificada, equipos ≥4 personas, protocolo estandarizado |
| Retraumatización del usuario | Debriefing empático, inclusión en plan prevención futura, reparación vincular |

Ref: Ley 21.331 art. 12; NICE NG10 2015; Sailas & Fenton 2000 (Cochrane); OMS QualityRights 2019.

## 33.4 Revisión por pares y casos complejos

Mecanismo de revisión clínica colaborativa para casos de alta complejidad, no-respondedores y eventos adversos.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Reunión clínica semanal | Revisión de casos complejos por equipo multidisciplinario ampliado |
| Revisión por pares (peer review) | Evaluación externa de decisiones clínicas en eventos adversos y casos refractarios |
| Supervisión clínica | Supervisión individual y grupal regular para todo profesional SM |
| Análisis de mortalidad/suicidio | Revisión sistemática de cada muerte en tratamiento (NCISH model) |
| Comité ética clínica | Consulta para dilemas: contenciones, involuntariedad, capacidad, riesgo vs autonomía |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Casos complejos revisados | Casos revisados / Casos identificados como complejos × 100 | ≥90 % | — | Gestión interna | Mensual |
| Supervisión clínica regular | Profesionales con supervisión mensual / Total profesionales SM × 100 | ≥80 % | — | NICE | Trimestral |
| Análisis mortalidad completados | Análisis realizados / Muertes en tratamiento × 100 | 100 % | — | NCISH model | Trimestral |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Revisión punitiva que inhibe reporte | Cultura justa, foco en sistema no en individuo |
| Falta de tiempo protegido para supervisión | Horas supervisión en contrato, carga asistencial ajustada |

Ref: NCISH Annual Report methodology 2023; NICE supervisión clínica 2019; Balint groups; Schwartz Rounds.

## 33.5 Participación de usuarios en mejora de calidad

Integración de personas con experiencia vivida en procesos de evaluación, mejora y gobernanza de calidad SM.

**Componentes:**

| Componente | Detalle |
|------------|---------|
| Comité de calidad SM con usuarios | Representación formal con voz y voto |
| Evaluadores pares | Usuarios capacitados que participan en auditorías de calidad y visitas |
| Encuestas de experiencia (PREMs SM) | Diseñadas con participación de usuarios, adaptadas a SM |
| Co-diseño de servicios | Talleres de mejora con usuarios, cuidadores y equipo |
| Storytelling terapéutico | Narrativas de recuperación como insumo de mejora y capacitación |

**KPI:**

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Sesiones calidad con usuarios | Sesiones con participación usuario / Total sesiones comité × 100 | ≥80 % | — | Ley 21.331 art. 7 | Trimestral |
| PREMs SM aplicados | Usuarios con PREM SM completado / Total usuarios activos × 100 | ≥40 % | UK IAPT 40 % | NHS 2022 | Semestral |
| Mejoras implementadas desde co-diseño | Mejoras implementadas / Propuestas co-diseño × 100 | ≥50 % | — | Gestión interna | Anual |

**Riesgos:**

| Riesgo | Mitigación |
|--------|------------|
| Participación simbólica sin impacto real | Indicadores de implementación, presupuesto asignado a propuestas |
| Sobrecarga emocional de usuarios evaluadores | Acompañamiento, remuneración, límites de participación |

Ref: Ley 21.331 art. 7; OMS QualityRights 2019; NICE Patient and Public Involvement 2019; Ocloo & Matthews 2016.
