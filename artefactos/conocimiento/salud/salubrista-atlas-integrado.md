---
urn: urn:salud:kb:salubrista-atlas-integrado
nombre: salubrista-atlas-integrado
version: 1.0.0
estado: publicado
descripcion: "Atlas integrado Salubrista: Este atlas une el corpus salubrista como un solo cuerpo de conocimiento para"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/atlas-integrado.md (sha256:653a07b9edb9b53415b85ea12066dcd96f1036d821f422ec9724680455086481) el 2026-06-12; cuerpo byte-fiel (renombrado de atlas-integrado.md a salubrista-atlas-integrado.md por lugar-coincide). Fuente original: Integracion organica del corpus salubrista, gestion-redes, HODOM y fuentes base fisicas sin perdida de informacion."
autor: FS
creado: 2026-04-27
lang: es
tags: [salubrista, atlas, gestion-redes, hospitalista, hospitalizacion-domiciliaria, hodom]
familia: bok
depende: [urn:salud:kb:salubrista]
cita: [urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:salubrista-fuentes-base-curadas, urn:salud:kb:salubrista-fuente-salud-publica-global, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:gestion-redes-indice, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:gestion-redes-salud-mental, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-decreto-exento-31-2024, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026]
---

# Atlas integrado Salubrista

Este atlas une el corpus salubrista como un solo cuerpo de conocimiento para
salud publica aplicada, gestion de redes y hospitalizacion integrada. No fusiona
mecanicamente los documentos fuente. Define como se compone el corpus y como
bajar desde una consulta a los nodos correctos.

## Principio De Integracion

La unidad basica del corpus salubrista es:

`problema sanitario + escala + capacidad + continuidad + gobernanza + evidencia`

La pregunta no debe resolverse solo por tema clinico o por dispositivo. Debe
explicitar escala, decision, restricciones, indicadores y consecuencias para la
red.

## Capas Canonicas

| Capa | URN | Funcion |
|------|-----|---------|
| Entrada canonica | `urn:salud:kb:salubrista` | Punto de entrada y contrato de corpus |
| Atlas integrado | `urn:salud:kb:salubrista-atlas-integrado` | Mapa de rutas, modos y partes |
| BOK salubrista | `urn:salud:kb:salubrista-body-of-knowledge` | Doctrina integrada y competencias |
| Fuentes base curadas | `urn:salud:kb:salubrista-fuentes-base-curadas` | Mapa curatorial de fuentes fisicas, alias y no duplicacion |
| Salud publica global | `urn:salud:kb:salubrista-fuente-salud-publica-global` | Determinantes, inequidad, funciones e intervenciones de salud publica |
| Management engineering | `urn:salud:kb:salubrista-fuente-management-engineering` | Variabilidad, colas, capacidad, forecast, BI y cooperacion |
| PAC/LTSS | `urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss` | Continuidad post-aguda, home health, LTSS y readmisiones |
| Gestion de redes | `urn:salud:kb:gestion-redes-indice` | Operacion de redes, unidades, urgencias, salud mental y herramientas |
| HODOM normativo y directivo | familia `hodom-*` | Reglas, direccion tecnica, alta complejidad y situacion Chile |

## Rutas De Uso

### Ruta 1: Diagnostico Situacional

Usar cuando se pida leer un territorio, red, establecimiento o unidad.

1. Entrar por salubrista.
2. Recuperar fuentes base curadas si hay determinantes, inequidad, politica o
   exposiciones ambientales/sociales.
3. Recuperar gestion-redes general y el modulo de unidad/red pertinente.
4. Activar skill FIRS si hay salto de escala o inferencia mixta.
5. Salida: brechas, prioridades, indicadores, riesgos y opciones de accion.

### Ruta 2: Diseno De Red O Unidad

Usar para modelos de atencion, cartera de servicios, procesos, dotacion,
interoperabilidad, indicadores y gobernanza.

1. Recuperar gestion-redes indice y general.
2. Bajar a unidades, urgencias, salud mental o herramientas.
3. Recuperar fuentes base curadas si el diseno requiere DES/QAT, pooling,
   forecast, PAC/LTSS o intervenciones publicas.
4. Activar skill FIRS para separar evidencia clinica, epidemiologica y operacional.
5. Salida: diseno, supuestos, trade-offs y plan de implementacion.

### Ruta 3: Hospitalista De Red

Usar cuando la pregunta trate hospitalizacion intrahospitalaria, capacidad,
camas, altas, boarding, flujo, continuidad y transiciones.

1. Recuperar perfil de hospitalizacion integrada.
2. Recuperar gestion-redes unidades y general.
3. Recuperar fuentes base curadas para variabilidad, colas, pooling, load
   leveling, bottleneck y forecasting.
4. Recuperar herramientas si se requieren KPI, BPMN, madurez o interoperabilidad.
5. Salida: lectura de capacidad, cuello de botella, plan de flujo, tablero y
   criterios de transicion.

### Ruta 4: Hospitalista A Domicilio

Usar para HODOM, HaH, alta precoz, camas virtuales, direccion tecnica, criterios
de ingreso/egreso, reingreso, cuidador y cumplimiento normativo.

1. Recuperar HODOM normativo: DS 1/2022, DE 31/2024 y Norma Tecnica 2024.
2. Recuperar direccion tecnica y manual de alta complejidad.
3. Recuperar fuentes base curadas para continuidad post-aguda, equipos,
   cuidador, readmision, direccion medica y analogias PAC/LTSS.
4. Recuperar gestion-redes unidades y herramientas.
5. Activar skill FIRS para controlar que la respuesta no confunda caso individual,
   programa, establecimiento y red.
6. Salida: check normativo, ruta operativa, riesgos de seguridad, indicadores y
   gatillos de escalamiento.

### Ruta 5: Evaluacion Y Politica

Usar cuando se soliciten resultados, evaluacion de programa, politica sanitaria,
escenarios o decision de inversion.

1. Recuperar fuentes base curadas.
2. Recuperar gestion-redes general y herramientas para KPI y madurez.
3. Recuperar HODOM situacion Chile cuando el tema sea hospitalizacion
   domiciliaria o capacidad virtual.
4. Activar skill FIRS cuando la evaluacion requiera controlar inferencia
   causal, salto de escala o trade-offs multinivel.
5. Salida: escenario, evidencia, equidad, sostenibilidad, costo y riesgos
   residuales.

### Ruta 6: Curaduria Y Procedencia

Usar cuando se pregunte de donde viene el conocimiento salubrista, que fue
absorbido desde `INBOX`, que se considera duplicado o que debe verificarse.

1. Recuperar fuentes base curadas.
2. Identificar si el material es KB publicada, crudo atomizado, agente legacy,
   memoria operativa o runtime.
3. Citar el nodo canonico publicado si existe.
4. Declarar vacio si la fuente fue reportada como perdida o no versionada.

## Regla De Preservacion De Shards

Los archivos `--pNN` son partes materiales del documento raiz indicado por
`extensions.kora.shard_root_urn`. No deben tratarse como corpus independientes.
La entrada canonica siempre es el URN raiz sin sufijo `pNN`.

## Regla De Preservacion De Fuentes

Las fuentes crudas de `INBOX/salud/salubrista` fueron integradas fisicamente
como nodos KORA en `salud/salubrista/fuentes/`. `publihealth.md` se conserva
como `.source.txt` no indexado porque duplica semanticamente el atomizado
Oxford. Los perfiles y FIRS no son corpus de conocimiento: viven en agentes o
skills.

## Limite De Seguridad

El corpus apoya decisiones de sistema. No prescribe tratamientos individuales,
no reemplaza juicio clinico, no reemplaza normativa vigente y no debe crear una
indicacion de hospitalizacion domiciliaria sin validar estabilidad clinica,
entorno, cuidador, cobertura, consentimiento y capacidad de reingreso.
