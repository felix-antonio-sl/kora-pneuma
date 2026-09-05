---
urn: urn:salud:kb:salubrista
nombre: salubrista
version: 1.0.0
estado: publicado
descripcion: "Corpus Salubrista: Indice canonico del corpus `salud/salubrista`"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/index.md (sha256:9d7d28d7e70bf95025aaf09040c07d0b9efbc9e22d1d23db75adf52a75ae3c68) el 2026-06-12; cuerpo byte-fiel (renombrado de index.md a salubrista.md por lugar-coincide). Fuente original: Corpus consolidado fisicamente desde gestion-redes, HODOM y fuentes base curadas de salud publica, management engineering y PAC/LTSS."
autor: FS
creado: 2026-04-27
lang: es
tags: [salubrista, salud-publica, gestion-redes, hospitalista, hospitalizacion-domiciliaria, hodom, corpus, indice]
familia: bok
cita: [urn:salud:kb:salubrista-atlas-integrado, urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:salubrista-fuentes-base-curadas, urn:salud:kb:salubrista-fuente-salud-publica-global, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:gestion-redes-indice, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-unidades, urn:salud:kb:gestion-redes-urgencias, urn:salud:kb:gestion-redes-salud-mental, urn:salud:kb:gestion-redes-herramientas, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-decreto-exento-31-2024, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026]
---

# Corpus Salubrista

Indice canonico del corpus `salud/salubrista`. Fija
`urn:salud:kb:salubrista` como punto de entrada productivo para el agente
salubrista y para sus modos de activacion como hospitalista de red y
hospitalista a domicilio.

El corpus se integra mediante el
[Atlas integrado Salubrista](urn:salud:kb:salubrista-atlas-integrado), que
define capas, rutas de uso, modos operativos y regla de preservacion de shards.

## Capas Del Corpus

- [Body of Knowledge Salubrista](urn:salud:kb:salubrista-body-of-knowledge):
  marco integrado de salud publica aplicada, gestion de redes, hospitalizacion
  como sistema, HODOM/HaH, evaluacion, politica y seguridad.
- [Fuentes base curadas](urn:salud:kb:salubrista-fuentes-base-curadas):
  mapa curatorial de las fuentes fisicas integradas y de los duplicados
  excluidos del corpus.
- [Salud publica global](urn:salud:kb:salubrista-fuente-salud-publica-global):
  determinantes, inequidad, funciones de salud publica, transicion
  epidemiologica, clima, salud mental e intervenciones.
- [Management engineering sanitario](urn:salud:kb:salubrista-fuente-management-engineering):
  variabilidad, colas, simulacion, capacidad, forecast, BI y cooperacion entre
  actores.
- [Continuidad post-aguda y LTSS](urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss):
  home health, transiciones, readmisiones, direccion medica, equipos y cuidado
  de larga duracion como conocimiento comparado.
- [Atlas integrado](urn:salud:kb:salubrista-atlas-integrado): mapa de rutas
  para consultas de territorio, red, establecimiento, unidad hospitalaria,
  hospitalizacion domiciliaria y evaluacion.
- [Gestion de Redes Asistenciales](urn:salud:kb:gestion-redes-indice): corpus
  operativo para diseno, operacion y mejora continua de redes y unidades.
- [HODOM](urn:salud:kb:hodom-reglamento-ds1-2022): normativa y manuales de
  hospitalizacion domiciliaria.

## Modos De Activacion

### Salubrista General

Usar para diagnostico situacional, vigilancia, gestion territorial, diseno de
redes, evaluacion de programas, politica sanitaria y lectura de inequidad.

### Hospitalista De Red

Usar cuando la pregunta trate cama, capacidad, flujo hospitalario, unidad de
agudos, UCI, altas, boarding, transiciones, continuidad asistencial o
coordinacion hospital-red. La base primaria es gestion-redes + management
engineering sanitario + HODOM cuando exista continuidad domiciliaria.

### Hospitalista A Domicilio

Usar cuando la pregunta trate hospitalizacion domiciliaria, HODOM, HaH, alta
precoz con domicilio, direccion tecnica HD, cumplimiento normativo, criterios de
ingreso/egreso, escalamiento, reingreso, cuidador, entorno domiciliario,
monitoreo remoto o camas virtuales. La base primaria es HODOM + continuidad
post-aguda/LTSS + gestion-redes unidades/herramientas.

## Regla De Uso

Toda consulta entra por `urn:salud:kb:salubrista` y se baja a una ruta:

1. determinar escala: unidad, establecimiento, red, territorio, nacional o
   multi;
2. clasificar modo: salubrista general, hospitalista de red u hospitalista a
   domicilio;
3. recuperar fuentes base fisicas cuando la pregunta dependa de determinantes,
   inequidad, operaciones cuantitativas, PAC/LTSS o procedencia del corpus;
4. activar la skill FIRS si hay riesgo de mezclar inferencias clinicas,
   poblacionales y de gestion;
5. recuperar gestion-redes para diseno y operacion;
6. recuperar HODOM cuando exista componente domiciliario, normativo o de
   capacidad virtual;
7. declarar vacio o necesidad de verificacion vigente cuando el corpus no cubra
   una norma, fecha, precio, regulacion o dato operacional actual.

Este corpus no reemplaza la conduccion humana ni las normas vigentes. Su uso
previsto es apoyo tecnico a decisiones de sistema con supuestos explicitos,
trazabilidad y preservacion de responsabilidad humana.
