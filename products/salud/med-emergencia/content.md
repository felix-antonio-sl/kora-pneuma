---
urn: urn:salud:kb:med-emergencia
nombre: med-emergencia
version: 2.1.0
estado: publicado
descripcion: "Corpus de Medicina de Emergencia: Indice canonico del corpus `salud/med-emergencia`"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/med-emergencia/index.md (sha256:6a468e593966980516d7a1d0c695159a8f85634f4aa51b9dd8a15f0013f10aee) el 2026-06-12; cuerpo byte-fiel (renombrado de index.md a med-emergencia.md por lugar-coincide). Fuente original: Corpus consolidado desde el indice raiz previo, TOC de urgencia, BOK diferencial y shards publicados de artifacts/knowledge/salud/med-emergencia/"
autor: FS
creado: 2026-04-15
lang: es
tags: [medicina-emergencia, urgencias, body-of-knowledge, corpus, indice, salud]
familia: bok
cita: [urn:salud:kb:me-body-of-knowledge-diferencial, urn:salud:kb:me-atlas-integrado, urn:salud:kb:me-toc-body-of-knowledge, urn:salud:kb:me-perfil-urgenciologo, urn:salud:kb:me-razonamiento-clinico, urn:salud:kb:me-evaluacion-primaria, urn:salud:kb:me-sincope, urn:salud:kb:me-dolor-toracico, urn:salud:kb:me-disnea, urn:salud:kb:me-tec-leve, urn:salud:kb:me-compromiso-conciencia, urn:salud:kb:me-mareo-vertigo, urn:salud:kb:me-deficit-neurologico, urn:salud:kb:me-cefalea-convulsiones, urn:salud:kb:me-dolor-abdominal, urn:salud:kb:me-fiebre-sin-foco, urn:salud:kb:me-hemorragia-digestiva, urn:salud:kb:me-infecciones-gastrointestinales, urn:salud:kb:me-infecciones-respiratorias-altas, urn:salud:kb:me-infecciones-respiratorias-bajas, urn:salud:kb:me-sintomas-urinarios, urn:salud:kb:me-traumatismos-frecuentes]
---

# Corpus de Medicina de Emergencia

Indice canonico del corpus `salud/med-emergencia`. Este archivo reemplaza el
placeholder raiz y fija `urn:salud:kb:med-emergencia` como punto de entrada
productivo del corpus.

El corpus se integra como un solo cuerpo clinico mediante el
[Atlas integrado de Medicina de Emergencia](urn:salud:kb:me-atlas-integrado),
que define capas, rutas, agrupaciones organicas y regla de preservacion de
shards.

## Capas Del Corpus

- [Body of Knowledge diferencial poblado](urn:salud:kb:me-body-of-knowledge-diferencial): marco extenso de fundamentos, arquitectura, tareas nucleares, presentaciones, farmacoterapia, reevaluacion, transiciones y competencias del emergenciologo.
- [Atlas integrado](urn:salud:kb:me-atlas-integrado): mapa clinico de composicion del corpus, rutas de uso, agrupaciones organicas, partes materiales y regla para no tratar shards como nodos independientes.
- [TOC del Body of Knowledge](urn:salud:kb:me-toc-body-of-knowledge): mapa curricular completo de 370+ secciones por acuidad, tareas, presentaciones, sistemas, procedimientos, farmacologia, gestion, seguridad, etica y docencia.
- [Perfil diferencial del emergenciologo](urn:salud:kb:me-perfil-urgenciologo): identidad profesional, perfil cognitivo, operativo, procedimental, comunicacional, sistemico, etico y docente.
- [Razonamiento clinico avanzado en emergencia](urn:salud:kb:me-razonamiento-clinico): loop de decision bajo incertidumbre, amenaza vital, diferencial priorizado, estrategia diagnostica, reevaluacion y disposicion.
- [Evaluacion primaria](urn:salud:kb:me-evaluacion-primaria): ABC/ABCDE, signos vitales, acuidad y estabilizacion inicial.

## Presentaciones Clinicas Publicadas

- [Sincope](urn:salud:kb:me-sincope)
- [Dolor toracico](urn:salud:kb:me-dolor-toracico)
- [Disnea](urn:salud:kb:me-disnea)
- [TEC leve](urn:salud:kb:me-tec-leve)
- [Compromiso de conciencia](urn:salud:kb:me-compromiso-conciencia)
- [Mareo y vertigo](urn:salud:kb:me-mareo-vertigo)
- [Deficit neurologico](urn:salud:kb:me-deficit-neurologico)
- [Cefalea y convulsiones](urn:salud:kb:me-cefalea-convulsiones)
- [Dolor abdominal](urn:salud:kb:me-dolor-abdominal)
- [Fiebre sin foco](urn:salud:kb:me-fiebre-sin-foco)
- [Hemorragia digestiva](urn:salud:kb:me-hemorragia-digestiva)
- [Infecciones gastrointestinales](urn:salud:kb:me-infecciones-gastrointestinales)
- [Infecciones respiratorias altas](urn:salud:kb:me-infecciones-respiratorias-altas)
- [Infecciones respiratorias bajas](urn:salud:kb:me-infecciones-respiratorias-bajas)
- [Sintomas urinarios](urn:salud:kb:me-sintomas-urinarios)
- [Traumatismos frecuentes](urn:salud:kb:me-traumatismos-frecuentes)

## Regla De Uso

El corpus se consulta desde `urn:salud:kb:med-emergencia` y se baja a la capa
mas especifica segun la pregunta: BOK poblado para orientacion doctrinal, TOC
para cobertura curricular, razonamiento/perfil para competencias transversales
y shards de presentacion para soporte clinico operativo.

Este corpus no reemplaza el juicio clinico humano ni guias locales vigentes. Su
uso previsto es apoyo al equipo de urgencia, con incertidumbre explicita,
priorizacion por amenaza vital y trazabilidad al artefacto consultado.
