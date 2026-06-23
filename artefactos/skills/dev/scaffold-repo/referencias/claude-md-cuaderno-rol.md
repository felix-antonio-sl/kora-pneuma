# CLAUDE.md

Guía de trabajo para agentes de código en este repositorio. **`CLAUDE.md` es la única
fuente de verdad documental**; `README.md` y `AGENTS.md` solo redirigen aquí.

Versionado independiente. Para concerns cross-cutting del host, ver `~/CLAUDE.md`.

## Qué es este repositorio

<!-- Cuaderno operativo de un rol. NO es repo de código: no hay build, tests ni
     dependencias. Es donde el rol produce, decide, firma, presenta y dirige.
     Material en Markdown + referencias a documentos oficiales (PDF/DOCX/XLSX). -->
Cuaderno operativo del **{{rol}}** — {{contexto institucional}}.

{{1-2 líneas más: qué decide/produce este rol y por qué existe el cuaderno}}.

## Orden de lectura para una sesión nueva

1. Este archivo (`CLAUDE.md`).
2. **Handoff vigente** (el `handoff-AAAA-MM-DD.md` de fecha máxima en {{p. ej.
   `00-rol/`}}; los previos viven en `_archivo/`) — estado operativo actual: frentes
   activos, pendientes, supuestos y riesgos. Entrada obligatoria.
3. {{marco/eval del rol — qué hace y por qué}}.
4. {{backlog de decisiones abiertas, si existe}}.

## Estado y dirección

El **estado operativo vivo siempre está en el handoff vigente**. Esta sección da solo
el esqueleto estable; no duplica métricas ni frentes, que caducan y viven en el handoff.

El handoff y todo documento-serie de este cuaderno se rigen por la **§Vigencia
documental**: un solo vigente, versionado por fecha, sin sobrescritura; el previo se
archiva en `_archivo/`.

## Vigencia documental

Todo documento operativo que evoluciona —el handoff, y cada serie de informe, acta,
minuta o auditoría— obedece tres invariantes:

1. **Un solo vigente por especie.** A lo más un handoff vigente; a lo más una versión
   vigente de cada serie. La *especie* es el slug del nombre sin la fecha (`handoff`,
   `acta-comite`, `auditoria-{{tema}}`…).
2. **Versionado por fecha, inmutable.** Cada versión es un documento nuevo
   `{{especie}}-AAAA-MM-DD.md` (colisión el mismo día → sufijo `-2`). No se edita
   in-place ni se sobrescribe un archivo ya escrito; el vigente es el de **fecha
   máxima** de su especie.
3. **El previo se archiva, no se descarta.** Al publicar una versión nueva, la
   anterior se **mueve** a `_archivo/`. Ese directorio está **gitignorado**: guarda
   todo lo no vigente, superado o deprecado. Es historia local, no SSOT; el árbol
   versionado contiene solo lo vigente. `git log` complementa, no reemplaza.

> Actualizar = partir del vigente previo (la nueva versión *es* su actualización),
> escribir `{{especie}}-<fecha-de-hoy>.md`, y mover la anterior a `_archivo/`. Nunca
> conviven dos vigentes de la misma especie en el árbol versionado.

## Principio curatorial

<!-- Qué entra al cuaderno y qué se referencia. Sin esta regla, el cuaderno se
     convierte en un vertedero. -->
> Entra lo que el rol **produce, firma, presenta o usa**. El insumo estable
> (normativa, corpus doctrinal) se **referencia**, no se copia. El código queda **fuera**.

## Mapa del repositorio

| Tramo | Contiene | Cuándo entrar |
|-------|----------|---------------|
| `{{00-rol/}}` | {{marco, handoff vigente}} | Entrada del visitante nuevo |
| `BITACORA.md` | registro histórico append-only (≠ handoff, que es el snapshot vigente) | Al cerrar una sesión |
| `{{...}}` | {{...}} | {{...}} |

## Sistemas y corpus vecinos

<!-- El rol se apoya en un ecosistema que NO vive aquí. Antes de actuar sobre
     cualquiera, leer su propio CLAUDE.md. Borra esta sección si el cuaderno es
     autónomo. -->

| Vecino | Ruta | Función |
|--------|------|---------|
| `{{...}}` | `{{...}}` | {{...}} |

## Convenciones

Hereda de `~/CLAUDE.md`: material en **es-CL**, términos técnicos en **inglés**;
fechas **ISO absolutas** (`2026-06-21`); nombres en kebab-case sin tildes (los PDFs
oficiales conservan su nombre original).

- **Extensiones autorizadas:** `.md`, `.pdf`, `.docx`, `.xlsx`, `.html`, `.json`. Nada de código.
- {{otras propias del rol}}

## Qué NO hacer aquí

- Ejecutar código, agregar dependencias o levantar servicios.
- Duplicar contenido que viva autorizadamente en un vecino — referenciarlo.
- {{volcar datos sensibles al repo, si maneja PII — solo síntesis desidentificada}}.
