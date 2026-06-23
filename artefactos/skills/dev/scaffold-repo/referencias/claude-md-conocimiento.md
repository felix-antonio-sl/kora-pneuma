# CLAUDE.md

Fuente operativa única para agentes que trabajen en este repositorio. Si otra fuente
(handoff, README externo, memoria vieja) contradice este archivo, manda **este archivo
y las specs/checks vigentes**. `README.md` y `AGENTS.md` solo redirigen aquí.

Versionado independiente. Para concerns cross-cutting del host, ver `~/CLAUDE.md`.

## Qué es este corpus

<!-- Qué tipo de conocimiento alberga, para qué se consume, quién/qué lo produce.
     Si hay un estándar de autoría (KORA/MD, etc.), nómbralo. -->
{{overview}}

<!-- Si aplica: tipos de artefacto que admite y cuáles NO. Un corpus bien acotado
     dice explícitamente qué queda fuera. -->
{{tipos-de-artefacto}}

## Bootstrap de sesión

Al abrir una sesión nueva sobre este repo:

1. Lee este archivo (`CLAUDE.md`).
2. {{Lee la gobernanza/precedencia cuando importe política — si existe}}.
3. {{Lee el **handoff vigente** — el `handoff-AAAA-MM-DD.md` de fecha máxima; los
   previos viven en `_archivo/` (ver §Vigencia documental) — si existe}}.
4. Verifica estado antes de tocar nada:
   ```bash
   {{comando de índice/health/check, o "n/a"}}
   ```

## Estructura

| Path | Contiene | Cuándo entrar |
|------|----------|---------------|
| `{{...}}` | {{...}} | {{...}} |
| `BITACORA.md` | registro cronológico append-only de sesiones/decisiones (se versiona, no entra en `_archivo/`) | Al cerrar una sesión o hito |

<!-- Si hay vistas generadas/derivadas, deja explícito que son regenerables y que el
     filesystem con manifests válidos es la fuente de verdad, no las vistas. -->

## Principio curatorial

<!-- La regla que decide qué entra y qué se referencia. Un corpus sin esta regla
     acumula ruido. Ej.: "Entra lo que se produce/mantiene aquí; el insumo estable
     se referencia, no se copia." -->
> {{regla de entrada}}

## Cómo agregar material

| Tipo | Destino | Acción adicional |
|------|---------|------------------|
| {{...}} | `{{...}}` | {{registro en índice, check, etc.}} |

## Vigencia documental

Handoffs, informes, auditorías y todo documento que evoluciona obedecen tres invariantes:

1. **Un solo vigente por especie.** A lo más un handoff vigente; a lo más una versión
   vigente de cada serie. La *especie* es el slug del nombre sin la fecha
   (`handoff`, `auditoria-{{tema}}`, `informe-{{tema}}`…).
2. **Versionado por fecha, inmutable.** Cada versión es un documento nuevo
   `{{especie}}-AAAA-MM-DD.md` (colisión el mismo día → sufijo `-2`). No se edita
   in-place ni se sobrescribe; el vigente es el de **fecha máxima** de su especie.
3. **El previo se archiva, no se descarta.** Al publicar una versión nueva, la anterior
   se **mueve** a `_archivo/` — directorio **gitignorado** con todo lo no vigente,
   superado o deprecado. Es historia local, no SSOT; el árbol versionado y los manifests
   contienen solo lo vigente.

> Actualizar = partir del vigente previo, escribir `{{especie}}-<fecha-de-hoy>.md`, y
> mover la anterior a `_archivo/`. Nunca dos vigentes de la misma especie versionados.

## Convenciones

Hereda de `~/CLAUDE.md`: docs en **es-CL**, términos técnicos en **inglés**; fechas
**ISO absolutas**; nombres de archivo en kebab-case sin tildes.

Propias:
- {{estándar de autoría, naming de URN/IDs, extensiones autorizadas}}

## Qué NO hacer

- {{no duplicar lo que vive autorizadamente en otro repo — referenciarlo}}
- {{no tratar vistas derivadas como fuente; no normalizar deuda que un check marca}}
