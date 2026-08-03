# HANDOFF

Estado: política de iniciación verificada y parcialmente publicada

## Frente actual

- `scaffold-repo` 2.0.0 y `handoff-policy` 3.0.0 son fuentes KORA válidas.
- `scaffold-repo` fue emitida y aplicada a Codex y Claude Code; ambas paridades
  resultan `fiel`.
- La arquitectura `README.md` humano -> `AGENTS.md` Codex -> `CLAUDE.md` con
  import exacto está presente en 25 raíces pertinentes. Los `AGENTS.md` bajo
  `_emision/openclaw/workspaces` siguen siendo contratos runtime excluidos.
- La fuente KORA y 11 repositorios consumidores tienen commits acotados y push
  normal confirmado. Los contratos de tres raíces host no versionadas también
  quedaron actualizados localmente.

## Publicación pendiente o bloqueada

- `firecrawl`: commit local `31271ee03` en `codex/onboarding-contract`; `origin`
  es el upstream público y `origin/main` está 626 commits por delante. No empujar.
- `hdos`: commit local `e5ae1cd`; `main` ya incluía el commit previo no publicado
  `5957da0`, por lo que un push publicaría trabajo anterior no autorizado.
- `hdos-app`: commit local `fb81d6f`; mismo bloqueo por `9556a7f` previo.
- `he-hsc`: commit local `8ca028d`; mismo bloqueo por `b24315a` previo.
- `korvo` (`5b9f0b6`) y `sanixai` (`a232fa9`): no tienen remoto configurado.
- GORE_OS conserva 126 rutas ajenas preparadas en el índice. El commit documental
  `9c970033` se creó con `--only` y fue publicado sin incluirlas; no alterar ese
  índice sin adjudicación del operador.

## Frente previo independiente

Las fuentes y emisiones locales de `urn:dev:artefacto:diagnosing-bugs` y
`urn:dev:artefacto:code-review` existen, pero sus instalaciones Codex siguen
`no-instalada`. No mezclar su eventual aplicación con esta entrega documental.

La integración y materialización de consumidores KORA en OpenClaw Fleet es un
frente externo. Su `main` local está adelantado y contiene cambios sin cerrar;
no lo mezcles con una operación KORA.

## Al retomar

1. Resuelve cada bloqueo anterior por separado: fork/remote para Firecrawl,
   adjudicación de commits previos en los tres repos adelantados y remoto explícito
   para `korvo`/`sanixai`.
2. Audita el índice de GORE_OS antes de cualquier nuevo commit allí.
3. Repite los gates pertinentes si cambia algún árbol; no hagas staging masivo.
4. Mantén instalación, publicación Git y despliegue como acciones distintas.

El cierre histórico y otros pendientes curatoriales se recuperan desde
`0f9ed3b`; no se duplican aquí. Elimina este archivo cuando no quede trabajo
material inconcluso.
