---
urn: urn:openclaw-fleet:kb:handoff-policy
nombre: handoff-policy
version: 2.0.3
estado: publicado
descripcion: "Política de vigencia, inmutabilidad, desplazamiento y trazabilidad de handoffs, auditorías e informes operativos de OpenClaw Fleet."
fuente: "Migrado desde el blob Git 8b26f4b4825544dcb35f2c928d8e5f8b73f4e74b:docs/handoff-policy.md de /home/felix/openclaw-fleet; sha256:1d8dd86026325f0bada308ddeb6cb5b4abb8f53b83d3ccc34c317e0e461ad300. El cuerpo preserva paridad exacta con ese blob. El path vivo /home/felix/openclaw-fleet/docs/handoff-policy.md es un symlink consumidor hacia este artefacto, no otra fuente de verdad. La política es local a la continuidad documental de la flota; no sustituye la configuración viva, la ley Pneuma ni la documentación oficial de OpenClaw."
autor: FS
creado: 2026-08-02
lang: es
tags: [openclaw, handoff, politica, vigencia, fleet]
familia: fuente
---

# Política de vigencia documental OpenClaw-Fleet v2.0.3

Esta política gobierna handoffs, auditorías, informes, actas y otros documentos
operativos fechados. Su objetivo es que el árbol visible contenga un solo punto
de continuación por especie, sin perder trazabilidad en Git.

## Reglas

1. **Un vigente por especie.** La especie es el slug estable sin fecha, por
   ejemplo `handoff` o `auditoria-documental`.
2. **Nombre.** Toda versión nueva usa `<especie>-AAAA-MM-DD.md`; si ya existe
   una versión del mismo día, agrega `-2`, `-3`, etc.
3. **Inmutabilidad.** Un operativo ya escrito no se edita ni sobrescribe. Una
   actualización crea una versión nueva.
4. **Desplazamiento.** Antes de escribir la versión nueva, la anterior se mueve
   a `_archivo/`. El directorio está ignorado por Git; la versión anterior
   permanece recuperable en la historia.
5. **Trazabilidad.** La versión nueva nombra la anterior en `replaces` y explica
   qué verdad durable conserva o corrige.
6. **Precedencia.** Un handoff explica continuidad; nunca anula la config viva,
   `openclaw.json.reference`, la ley Pneuma ni `docs/openclaw/`, SSOT local de
   la documentación oficial de OpenClaw.
7. **Movimiento destructivo.** Desplazar documentos versionados requiere
   confirmación humana explícita y un diff revisado antes del commit.

## Metadata mínima de un handoff

El documento vigente declara:

- `status: publicado`;
- `extensions.openclaw_fleet.primary_handoff: true`;
- `extensions.openclaw_fleet.scope`;
- `extensions.openclaw_fleet.replaces` cuando tenga predecesor;
- secciones `Reemplaza`, `Estado verificado`, `Decisiones vigentes` y
  `Siguiente dirección`.

Los slugs, scopes, comandos e identificadores se escriben en inglés. La prosa
se escribe en español de Chile y las fechas son ISO absolutas.

## Migración aplicada

El 2026-07-12, con autorización explícita del operador, los handoffs y
auditorías históricos se desplazaron a `_archivo/`. El resultado y la deuda
remanente quedaron preservados en la historia y en
`docs/audits/_archivo/auditoria-documental-2026-07-12-2.md`.
