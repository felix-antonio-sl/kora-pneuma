---
urn: urn:salud:kb:salubrista-body-of-knowledge
nombre: salubrista-body-of-knowledge
version: 1.0.0
estado: publicado
descripcion: "Body of Knowledge Salubrista: El salubrista opera sobre sistemas sanitarios, no sobre encuentros clinicos"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/body-of-knowledge-salubrista.md (sha256:7c161f3eeb1750136d6c1640f243eb64b8c086e44ea27235dcf84e05bed995d0) el 2026-06-12; cuerpo byte-fiel (renombrado de body-of-knowledge-salubrista.md a salubrista-body-of-knowledge.md por lugar-coincide). Fuente original: Sintesis canonica desde gestion-redes, HODOM y fuentes base fisicas del corpus salubrista."
autor: FS
creado: 2026-04-27
lang: es
tags: [salubrista, body-of-knowledge, salud-publica, gestion-redes, hospitalista, hodom]
familia: bok
depende: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-atlas-integrado]
cita: [urn:salud:kb:gestion-redes-indice, urn:salud:kb:salubrista-fuentes-base-curadas, urn:salud:kb:salubrista-fuente-salud-publica-global, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026]
---

# Body of Knowledge Salubrista

## 0. Objeto Formal

El salubrista opera sobre sistemas sanitarios, no sobre encuentros clinicos
aislados. Su objeto formal es la transformacion de evidencia epidemiologica,
clinica, operacional y normativa en decisiones de red: priorizar problemas,
disenar servicios, gestionar capacidad, evaluar resultados y sostener equidad.

## 1. Escala Como Control Epistemico

Toda inferencia debe declarar escala:

| Escala | Pregunta tipica | Riesgo si se confunde |
|--------|-----------------|-----------------------|
| Unidad | proceso, dotacion, KPI local | sobregeneralizar a la red |
| Establecimiento | cartera, camas, flujo, seguridad | ignorar territorio |
| Red | continuidad, derivacion, gobernanza | diluir responsabilidades |
| Territorio | inequidad, carga, acceso | perder capacidad operativa |
| Nacional | politica, financiamiento, regulacion | sobreprometer implementacion local |

El control de saltos indebidos entre caso clinico, programa, establecimiento y
poblacion pertenece a la skill `urn:salud:artefacto:firs-razonamiento-sanitario`,
no al corpus de conocimiento.

## 2. Salud Publica Aplicada A Decision

El nucleo no es describir enfermedad, sino traducirla en decision:

- carga y distribucion del problema;
- poblaciones afectadas y brechas de acceso;
- tendencia, alerta y vigilancia;
- oportunidad de intervencion;
- impacto esperado y factibilidad;
- indicadores para seguimiento.

## 3. Gestion De Redes

Gestion-redes aporta el lenguaje operativo: gobernanza, procesos, calidad,
digital, personas, finanzas, abastecimiento, infraestructura, participacion,
cambio, docencia, unidades, urgencias, salud mental y herramientas.

Una recomendacion salubrista debe identificar el nivel de decision, el duenio
operativo, el indicador, el riesgo y el circuito de retroalimentacion.

## 4. Hospitalista De Red

El modo hospitalista mira la hospitalizacion como sistema de capacidad y
continuidad:

- cama fisica y cama virtual;
- ocupacion, estancia, altas, boarding y backfill;
- urgencia como puerta de entrada y sensor de saturacion;
- unidad hospitalaria como nodo, no silo;
- alta segura y continuidad con APS, rehabilitacion, cuidados paliativos y
  domicilio;
- seguridad del paciente durante transiciones.

El hospitalista de red no reemplaza a medicina interna ni a gestion de camas.
Su funcion es integrar evidencia, flujo, capacidad y gobernanza para que el
humano conductor decida.

## 5. Hospitalista A Domicilio / HODOM

La hospitalizacion domiciliaria es atencion cerrada desplazada al domicilio, no
atencion ambulatoria simple. Debe cumplir simultaneamente:

- indicacion medica;
- control medico;
- plan terapeutico y de cuidados;
- condicion clinica estable;
- domicilio apto y red de apoyo;
- consentimiento informado;
- capacidad de respuesta, escalamiento y reingreso;
- Direccion Tecnica y coordinacion reguladas;
- registros, confidencialidad, IAAS, insumos, equipos y transporte.

El modo HODOM usa DS 1/2022, DE 31/2024, Norma Tecnica HD 2024, manual de
Direccion Tecnica, manual de alta complejidad y situacion Chile 2026 como base.

## 6. Capacidad Y Camas

La pregunta hospitalaria se organiza por capacidad:

- demanda esperada y variabilidad;
- camas habilitadas, ocupadas, bloqueadas y virtuales;
- estancia media, altas antes de mediodia, reingresos y boarding;
- criterios de derivacion a HD/HaH;
- backfill: cama liberada por HD permite ingreso de mayor complejidad;
- contingencia cuando ocupacion o boarding superan umbrales.

Las recomendaciones deben diferenciar efecto real de capacidad, traslado de
carga al cuidador y riesgo de inequidad territorial.

## 7. Seguridad Y Calidad

Las decisiones deben preservar:

- continuidad clinica y de informacion;
- IAAS y seguridad medicamentosa;
- respuesta ante deterioro;
- trazabilidad del responsable;
- experiencia del paciente y del cuidador;
- equidad de acceso;
- auditoria de reingresos, eventos adversos, mortalidad y escalamiento.

## 8. Interoperabilidad Y Herramientas

Gestion-redes herramientas aporta KPI, BPMN, FHIR/HL7, plantillas, simulacion y
madurez. El salubrista debe transformar una recomendacion en artefacto operable:
tablero, flujo, criterio, matriz RACI, SLA, plan de medicion o contrato de
interoperabilidad.

## 9. Evaluacion De Programas

Evaluar un programa exige al menos:

1. problema y teoria de cambio;
2. poblacion objetivo;
3. indicadores de acceso, calidad, seguridad, costo, experiencia y equidad;
4. linea base;
5. comparador;
6. seguimiento temporal;
7. riesgos y efectos no deseados;
8. decision posible segun resultado.

## 10. Politica Sanitaria

La respuesta politica debe presentar escenarios, trade-offs, costos de
oportunidad, factibilidad, gobernanza y riesgo residual. No basta con declarar
beneficio poblacional; debe mostrar como se implementa, quien responde y como se
medira.

## 11. Guardrail De Dominio

Fuera de scope:

- prescripcion farmacologica individual;
- diagnostico clinico individual;
- reemplazo de direccion tecnica o conduccion estrategica humana;
- afirmaciones regulatorias vigentes sin verificar cuando la fecha importe.

## 12. Salida Canonica

La salida preferida del salubrista debe contener:

1. sintesis ejecutiva;
2. escala y modo;
3. evidencia o corpus usado;
4. brechas y riesgos;
5. opciones con trade-offs;
6. indicadores y umbrales;
7. decision humana requerida;
8. vacios o verificaciones pendientes.

## 13. Fuentes Base Curadas

La base cruda integrada al corpus aporta tres lentes que no deben duplicarse:

1. salud publica global: determinantes, inequidad, transicion epidemiologica,
   sindemias, clima, resistencia antimicrobiana, salud mental, envejecimiento,
   violencia, migracion e intervenciones estructurales;
2. management engineering: variabilidad, simulacion de eventos discretos,
   teoria de colas, pooling, capacidad reservada, load leveling, bottlenecks,
   forecasting, BI, PCA, clustering y teoria de juegos;
3. continuidad post-aguda y LTSS: home health, hospital-at-home, cuidado de
   larga duracion, equipos interdisciplinarios, direccion medica, transiciones,
   readmisiones, 4M/5M geriatricas y derechos del paciente.

Estas fuentes son insumo curado, no autoridad directa por si mismas. Toda
recomendacion debe bajar al nodo canonico aplicable: gestion-redes para diseno
operativo, HODOM para normativa chilena de hospitalizacion domiciliaria, y
skill FIRS para control epistemico.

## 14. Regla Anti-Redundancia

El corpus considera duplicacion como defecto critico. Por eso:

- el atomizado `publihealth.md` se trata como alias editorial del atomizado
  Oxford y no como segunda evidencia;
- las copias `*.source.txt` de KB publicada son procedencia, no nuevos nodos;
- el conocimiento legacy hospitalista se conserva solo como modo interno de
  `salubrista` y skill HODOM;
- una salida debe citar la fuente productiva mas especifica, no repetir todos
  los nodos relacionados;
- si una afirmacion depende de norma, tarifa, cobertura, fecha o regulacion
  vigente, debe verificarse contra fuente oficial actual antes de presentarse
  como valida.
