---
urn: urn:salud:kb:hodom-glosario-ontologia
nombre: hodom-glosario-ontologia
version: 1.0.0
estado: publicado
descripcion: "Glosario y ontologia canonica de dominio de la Hospitalizacion Domiciliaria (HODOM): objetos-frontera, ciclo de vida del episodio, compuertas de admision, modalidades y capacidad, prestaciones, roles clinicos normativos e interfaces de red, con sinonimos prohibidos y anclas normativas (DS 1/2022, NT 2024, RPE)."
fuente: "Koraficado de hd-dt/05-gobernanza-datos/inf-14-glosario-ontologia-canonica.md (sha256:8776c537239ff51541ebfbc944c265b130125fb643c62c7b7653a23c24d3ce9f, 2026-06-22). Recorte de alcance declarado (ley/4 §8.3): se korafica solo la ontologia de DOMINIO generalizable. Quedan FUERA por ser curaduria HSC-local (viven en hd-dt): el catalogo RBAC de 14 roleType institucionales, las banderas de estado-app (hd-opm/hd-hsc-os), los codigos GOB-* de la maquina de consistencia del corpus archivado y las referencias al manual marketplace (metafora retirada). FS=100% sobre el alcance de dominio; CR>1,5."
autor: FS
creado: 2026-06-22
lang: es
tags: [salud, hodom, hospitalizacion-domiciliaria, glosario, ontologia, vocabulario-canonico, dominio]
familia: bok
cita: [urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-invariante-no-equivale-cerrada, urn:salud:kb:hodom-direccion-tecnica]
---

# Glosario y ontología canónica de dominio HODOM

Vocabulario único del dominio de la Hospitalización Domiciliaria: un término, un significado, su ancla normativa y sus sinónimos prohibidos. Sirve de fuente de vocabulario para cualquier artefacto, protocolo o sistema que modele HODOM. **HODOM** = Hospitalización Domiciliaria; siglas expandidas en su primera aparición, luego sin expandir.

## Invariante de dominio

HODOM en hospitalización activa es atención bajo **estándar de atención cerrada**, pero **no** es hospitalización cerrada/tradicional: **HODOM ⊂ atención cerrada** (subconjunto condicionado). La diferencia esencial no es el lugar, sino la menor capacidad de rescate y la mayor latencia del domicilio. Doctrina completa: `urn:salud:kb:hodom-invariante-no-equivale-cerrada`. Ningún término de este glosario equipara HODOM con hospitalización cerrada ni usa «hospitalización» a secas para el domicilio.

## Objetos-frontera del dominio

Interfaz mínima del modelo: cuatro objetos por los que entra y se gestiona el cuidado.

| Término canónico | Definición | Sinónimos prohibidos |
|---|---|---|
| **Solicitud** | Petición de ingreso que entra a la doble compuerta con identificador de caso y estado. Nunca por decisión verbal en chat. | derivación, interconsulta, pedido |
| **Cupo** | Unidad de capacidad clínica **ofertable del día** (cama virtual asignable). Recurso escaso. | cama (a secas), plaza, cama virtual |
| **Cartera** | Conjunto de prestaciones autorizadas por disciplina que HODOM puede entregar. | canasta (salvo «canasta HODOM» de RPE-34), catálogo de prestaciones |
| **Episodio** | Instancia de hospitalización domiciliaria de un paciente, con ciclo de vida y máquina de estados propios. | estadía, caso, ingreso (en prosa de dominio) |

## Ciclo de vida del episodio — siete estados

Secuencia canónica; se nombra por su función clínica, no por metáfora.

| # | Estado | Definición | Umbral / ancla |
|---|---|---|---|
| 1 | **Captación** | Captación de demanda y de cupo; la Solicitud entra con identificador y estado. | — |
| 2 | **Doble compuerta** | Matching concurrente social-territorial + clínico. | Evaluación médica ≤ 4 h (DS 1/2022 art. 15) |
| 3 | **Ingreso** | Activación del domicilio: consentimiento informado, Carta de Derechos, primera visita médica, apertura de ficha, educación del cuidador. | DS 1/2022 art. 15; Ley 20.584 |
| 4 | **Hospitalización activa** | El paciente ocupa cama virtual bajo plan terapéutico con estándar de atención cerrada. | NEWS2 en cada visita |
| 5 | **Vigilancia y escalamiento** | Monitoreo y escalamiento mediante el Semáforo HODOM + NEWS2. | DS 1/2022 art. 19 (contacto 24/7) |
| 6 | **Egreso** | Egreso por causal normada; produce epicrisis, contrarreferencia y retiro de equipamiento. | DS 1/2022 |
| 7 | **Cierre de loop** | Anti-reingreso: encuesta de satisfacción, seguimiento telefónico y contrarreferencia efectiva a la atención primaria. | Seguimiento 48–72 h |

## Compuertas de admisión

La admisión se resuelve en dos hojas concurrentes sobre la misma Solicitud; ninguna sustituye a la otra.

| Compuerta | Verifica | Responsable | Plazo / ancla |
|---|---|---|---|
| **Compuerta social-territorial** | Cuidador competente, domicilio en radio ≤ 20 km/circuitos, contacto factible, ruta operativa. Determinante de equidad. | Enfermera Coordinadora | precede a la clínica (DS 1/2022 art. 12.g) |
| **Compuerta clínica** | Estabilidad, pertinencia, intensidad hospitalaria real, vía de escalamiento. | Médico de Atención Directa | ≤ 4 h tras la social (DS 1/2022 art. 12.a, art. 15; RPE-34) |

**Verificación vs. decisión** — la *verificación clínica* de admisión la realiza el Médico de Atención Directa (DS 1/2022 art. 12.a), nunca el Médico Regulador. La *decisión de aceptar o rechazar* la Solicitud es un acto **separado** de la verificación; su atribución de decisor es punto de modelado abierto, no se asume cerrado.

## Modalidades y capacidad

| Término canónico | Definición | Sinónimos prohibidos |
|---|---|---|
| **Modalidad presencial** | Prestación ejecutada en visita domiciliaria física. | en terreno (sin ancla), visita (a secas) |
| **Modalidad telemática** | Prestación a distancia (teleatención/telemonitoreo) bajo RPE-9 / Ley 21.541. | remoto (a secas), virtual, online |
| **Cama virtual** | Inventario instalado de capacidad HODOM. Distinta del Cupo. | cama (a secas), cupo, plaza |
| **Sobre-cupo** | Cupos asignados por encima de la cama virtual declarada; se expresa siempre como porcentaje sobre la cama virtual. Sostenido alto = síntoma de falla, no logro. | sobreocupación informal |
| **Campaña de invierno** | Modo de operación estacional de refuerzo (~4 meses): dotación ampliada y cobertura horaria extendida. No es la operación permanente que exige la norma. | operación permanente, modelo definitivo |
| **Semáforo HODOM** | Instrumento de vigilancia y escalamiento apoyado en NEWS2: verde = plan; amarillo = deterioro leve, respuesta ≤ 30 min; naranja = deterioro significativo, médico ≤ 15 min; rojo = emergencia, SAMU 131 inmediato. | semáforo (a secas), triage de colores |

## Prestaciones del dominio

| Término canónico | Definición | Ancla |
|---|---|---|
| **EV cada 12 h** | Antibioticoterapia/sueroterapia endovenosa con ventana terapéutica c/12 h; la ventana del fármaco manda sobre la eficiencia de ruta. | cartera; OPAT |
| **Telemonitoreo** | Seguimiento asincrónico de parámetros entre visitas: recolección y verificación contra umbral más escalamiento; no interpreta ni ajusta. | DS 90/2017 |
| **Teleatención** | Prestación clínica **sincrónica** a distancia (teleconsulta), registrada con especialidad, modalidad, resumen e indicaciones. | RPE-9; Ley 21.541 |
| **Telesupervisión** | Modalidad RPE-9 en que un profesional supervisa **en vivo** el acto de un cuidador o actor del equipo extendido; con criterio de detención y escalamiento. | RPE-9 |
| **Delivery a domicilio** | Entrega programada de medicamentos, insumos u oxígeno al domicilio, con cadena de frío y trazabilidad despacho→administración. | cartera |
| **Autoadministración supervisada** | Administración de una dosis EV por cuidador entrenado bajo telesupervisión profesional, solo si el binomio cuidador/hogar es elegible. | RPE-9 |
| **REM A21 C.1 (0201408)** | Reporte estadístico mensual oficial; código arancelario FONASA 0201408 (Día Cama HD Baja Complejidad). Se genera desde el sistema, no se redigita a mano. | normativa REM |

## Roles clínicos del modelo (anclas normativas)

Roles del dominio nombrados por su función normativa. El cuidador **no** es rol del sistema: es equipo extendido, sin sesión ni permiso clínico propios; cuando ejecuta un acto, este se atribuye bajo el profesional supervisor.

| Rol canónico | Función | Ancla |
|---|---|---|
| **Médico de Atención Directa** | Evalúa, indica, coordina y **verifica la admisión clínica** en domicilio. | DS 1/2022 art. 12.a |
| **Médico Regulador** | Regulación remota: clasifica escalamiento y decide rescate. **No** verifica la admisión. | DS 1/2022 |
| **Enfermera Coordinadora** | Resuelve la compuerta social-territorial, arma rutas, conduce la coordinación. | DS 1/2022 art. 12.g |
| **Enfermero Clínico** | Ejecuta prestaciones de enfermería en domicilio, registra evolución, verifica voluntariedad del paciente. | DS 1/2022 |
| **Técnico en Enfermería (TENS)** | Signos, curación, HGT, muestras y administración **delegada** de medicamento (con competencia delegada, indicación vigente y habilitación). | DS 90/2017 |
| **Kinesiólogo** | Rehabilitación y kinesiterapia respiratoria; registra nota propia. | RPE-14 |
| **Fonoaudiólogo** | Deglución, comunicación y cognición; registra nota propia. | cartera |
| **Trabajador Social** | Evaluación socio-sanitaria, consentimiento y coordinación de redes. | DS 1/2022 art. 12.g |

## Interfaces de red

Cada interacción declara su artefacto trazable (solicitud/estado/resultado), nunca una coordinación informal.

| Interfaz | Función | Ancla |
|---|---|---|
| **Gestión de Camas** | Acople diario de la torre HODOM con Gestión de Camas: cupos y sobre-cupo; el «pull» que libera cama. | DS 1/2022 art. 17 |
| **Laboratorio** | Intercambio de exámenes con acuerdo de nivel de servicio operacional. | RPE-33 |
| **Imagenología** | Solicitud y resultado de imágenes. | RPE-27 |
| **Farmacia** | Despacho de fármacos e insumos a domicilio con cadena de frío. | cartera |
| **UEH/UEA** | Unidad de Emergencia Hospitalaria/de Atención: handoff de escalamiento y de cierre de ventana horaria, con nivel de servicio en minutos. | DS 1/2022 |
| **Pabellón** | Coordinación de procedimientos quirúrgicos del episodio. | — |
| **CAE** | Centro de Atención Especializada: interconsultas de especialidad. | — |
| **Telemedicina** | Interfaz de prestación a distancia; alimenta teleatención y telemonitoreo. | RPE-9; Ley 21.541 |
| **APS/CESFAM** | Atención Primaria/Centro de Salud Familiar: contrarreferencia efectiva al cierre del loop. | — |
| **SAMU** | Servicio de Atención Médica de Urgencia: escalamiento rojo, línea 24/7 (131), inmediato. | DS 1/2022 art. 17 |

## Anclas normativas del glosario

| Ancla | Qué fija |
|---|---|
| **DS 1/2022** (Reglamento HODOM) | art. 12.a (verificación de admisión), art. 12.g (función social), art. 15 (criterios de ingreso), art. 17 (coordinación, retorno, contacto 24/7), arts. 18–19 (información y contacto). |
| **DE 31/2024 + NT HODOM 2024** | Estándar técnico del modelo, intensidad hospitalaria real, invariante de atención cerrada. |
| **Ley 21.541 (RPE-9)** | Encuadra teleatención, telemonitoreo, telesupervisión y la modalidad telemática. |
| **RPE-14 / RPE-27 / RPE-33 / RPE-34** | Rehabilitación; imagenología; laboratorio; canasta y criterios HODOM. |
| **DS 90/2017** | Delegación al Técnico en Enfermería con gate de competencia. |
| **Ley 20.584** | Consentimiento, información y derecho a atención presencial. |
