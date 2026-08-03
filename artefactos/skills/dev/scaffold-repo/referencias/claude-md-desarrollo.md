# CLAUDE.md

Contrato operativo de Claude Code para este repositorio. Codex usa su contrato
autónomo en `AGENTS.md`; las fuentes de verdad del producto se declaran por separado.

Versionado independiente. Para concerns cross-cutting del host, ver `~/CLAUDE.md`.

## Qué es este repositorio

<!-- 1-3 líneas: el problema que resuelve y para quién. El porqué, no solo el qué.
     Nombra el stack y si es monorepo. Ej.: "X es un power tool single-user para Y.
     Monorepo con packages/core (motor) y packages/web (editor)." -->
{{overview}}

## Estructura

<!-- Solo los tramos que ya existen. Una fila por directorio principal. -->

| Path | Contiene |
|------|----------|
| `{{src/}}` | {{...}} |
| `{{tests/}}` | {{...}} |
| `docs/` | {{solo documentos vigentes y vinculantes; no-vigentes en `_archivo/` (gitignorado)}} |
| `CHANGELOG.md` | registro de cambios append-only (Keep a Changelog); se versiona, no entra en `_archivo/` |

## Desarrollo

<!-- Comandos canónicos. Si aún no existen, márcalo honesto: {{pendiente}}. -->

| Acción | Comando |
|--------|---------|
| Runtime | {{Node 24 / Bun / Python 3.12 / Go 1.24}} |
| Instalar | `{{pnpm install}}` |
| Build | `{{pnpm build}}` |
| Tests | `{{pnpm test}}` |
| Dev / run | `{{pnpm dev}}` |
| Type check | `{{...}}` |

**Baseline verde:** {{qué comandos deben pasar antes de considerar un cambio terminado}}.

## Convenciones

Hereda de `~/CLAUDE.md`: docs en **es-CL**, identificadores y términos técnicos en
**inglés**; fechas **ISO absolutas** (`2026-06-21`); nombres de archivo en kebab-case.

Propias de este repo:
- {{patrón de commits, IDs de backlog, taxonomías, patrón arquitectónico clave}}

## Decisiones arquitectónicas

<!-- Opcional al inicio; agrega cuando tomes la primera decisión vinculante.
     Una fila por ADR/DA con estado. Borra esta sección si aún no hay ninguna. -->

| # | Decisión | Estado |
|---|----------|--------|
| {{DA-1}} | {{...}} | {{Definida / Implementada}} |

## Continuidad de sesión

El **estado vivo del repo manda** sobre handoffs viejos. Verifica comandos, tests y
comportamiento en el código antes de asumir que una nota de sesión sigue vigente.

**Vigencia documental.** Handoff e informes/auditorías que evolucionan siguen la regla
del host: un solo vigente por especie, versionado por fecha
(`{{especie}}-AAAA-MM-DD.md`, inmutable, sin sobrescritura); al publicar uno nuevo, el
previo se **mueve** a `_archivo/` (gitignorado, historia local no-SSOT). Para historia de
**código** mandan git y `git log`; `_archivo/` es para **documentos** superados.

## Qué NO hacer

- {{fronteras de scope: qué está fuera de este repo}}
- No modificar {{paths de referencia read-only, archivos preservados por el operador}}.
- No volcar secretos ni `.env` al repo.
