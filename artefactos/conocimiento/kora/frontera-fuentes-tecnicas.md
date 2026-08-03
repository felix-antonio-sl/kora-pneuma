---
urn: urn:kora:kb:frontera-fuentes-tecnicas
nombre: frontera-fuentes-tecnicas
version: 1.0.0
estado: borrador
descripcion: "Criterio para decidir qué conocimiento se korafica y qué fuentes técnicas se conserva, archiva o descarta fuera de KORA."
fuente: "Decisión confirmada por el operador después de la auditoría de fuentes del host y del corpus GN el 2026-08-03; doctrina operativa interna, sin hash externo."
autor: FS
creado: 2026-08-03
lang: es
tags: [kora, fuentes-tecnicas, archivo, symlink]
cita: [urn:kora:kb:guia-rapida-pneuma]
familia: nota
---

# Frontera de fuentes técnicas

## Regla de decisión

El conocimiento curado tiene una sola fuente canónica en KORA. Una fuente se
korafica cuando su contenido puede representarse en el shape de conocimiento
KORA sin perder hechos, referencias ni semántica relevante.

Las ontologías OWL/SKOS, los catálogos XML, los esquemas de máquina y los datos
raw permanecen fuera de KORA cuando su formato aporta una semántica técnica
que no puede preservarse fielmente en Markdown. Pueden conservarse como fuentes
externas y ser citados o resumidos desde KORA, sin convertir el resumen en la
fuente original.

## Destinos

- **KORAFICAR**: conocimiento curado cuya fidelidad semántica puede verificarse.
- **CONSERVAR-EXTERNO**: fuente técnica cuyo formato es parte de su significado
  o que debe seguir siendo consumida como artefacto de máquina.
- **ARCHIVAR**: fuente sin consumidor físico vigente, después de comprobar
  referencias, symlinks, destino e inventario, crear una copia reversible y
  verificar un manifiesto SHA-256.
- **DESCARTAR**: solo con redundancia u obsolescencia completa verificada y
  autoridad explícita. La ausencia de referencias, por sí sola, no autoriza
  borrar.

## Symlinks

Un symlink solo se crea cuando un consumidor físico real necesita el artefacto
en otro repositorio o workspace. El symlink facilita el acceso, pero el
consumidor nunca se convierte en fuente de verdad: la autoridad permanece en
KORA para conocimiento curado o en la zona externa correspondiente para una
fuente técnica.
