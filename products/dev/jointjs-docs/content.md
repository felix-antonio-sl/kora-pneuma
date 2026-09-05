---
urn: urn:dev:kb:jointjs-docs
nombre: jointjs-docs
version: 1.0.0
estado: publicado
descripcion: "Puntero curado a la documentación oficial viva de JointJS open-source (docs.jointjs.com): conocimiento web vivo para render estático de diagramas — things, links, layout y exportación SVG/PNG. No se copia: se consulta en la fuente."
fuente: "Fuente web viva: https://docs.jointjs.com/ (documentación oficial de JointJS open-source). Procedencia web no versionada — sin sha256 porque el contenido es vivo: ley/2 §76 exige sha256 solo para procedencia desde la bestia, y ley/4 acepta una referencia estable equivalente (la URL canónica) en su lugar. Creado 2026-06-15 como puntero de conocimiento web para modelamiento-opm (render estático OPM vía JointJS), bajo la doctrina centralizado+URN aplicada a la web: se cataloga la referencia, no se copia el contenido vivo."
autor: FS
creado: 2026-06-15
lang: es
tags: [jointjs, render, diagramas, svg, web-viva, opm-render, documentacion-oficial]
familia: fuente
---
# jointjs-docs

Puntero curado a la **documentación oficial viva de JointJS open-source**. Es
**conocimiento web vivo**: no se copia al repo (cambia con cada release de la
librería); se consulta en la fuente cuando se necesita.

## Fuente canónica

- **Documentación oficial**: https://docs.jointjs.com/
- Librería: [JointJS](https://www.jointjs.com/) open-source (`jointjs` en npm),
  diagramación interactiva y render estático (SVG/PNG) en JavaScript.
- La SSOT del render es la doc oficial viva, **no este puntero**: este kb solo
  cataloga la referencia, su alcance y cómo consultarla.

## Alcance relevante para render OPM

JointJS es, en KORA, el **render estático secundario** de modelos OPM: producir
un diagrama OPD sin abrir un modelador interactivo (para informe, lámina,
markdown o presentación). Lo pertinente de su doc:

- Construcción de `things` (shapes para objetos/procesos) y `links` (enlaces con
  extremos, estilo, multiplicidad).
- Layout y posicionamiento de elementos.
- Exportación a SVG/PNG sin UI interactiva.
- Personalización de shapes para la gramática gráfica OPD (objetos
  rectangulares, procesos elípticos, estados, anotaciones).

## Cómo consultar

Antes de generar render con JointJS, consultar la sección pertinente de
`docs.jointjs.com` (la API evoluciona entre versiones) con la herramienta web
disponible (`WebFetch`/`WebSearch`) o, en su defecto, `curl`. No asumir la API
de memoria: la fuente viva manda.
