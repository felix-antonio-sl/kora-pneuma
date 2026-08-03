---
urn: urn:openclaw-fleet:kb:handoff-policy
nombre: handoff-policy
version: 3.0.0
estado: publicado
descripcion: "Política simple de continuidad para OpenClaw Fleet: un único HANDOFF.md raíz, estable y temporal, solo mientras exista trabajo material inconcluso; Git conserva la historia y auditorías e informes permanecen como evidencia, no como continuidad."
fuente: "Migrada desde el blob Git 8b26f4b4825544dcb35f2c928d8e5f8b73f4e74b:docs/handoff-policy.md de /home/felix/openclaw-fleet (sha256:1d8dd86026325f0bada308ddeb6cb5b4abb8f53b83d3ccc34c317e0e461ad300) y publicada en KORA como fuente única, consumida por symlink desde Fleet. v3.0.0 (2026-08-03): sustituye handoffs fechados, metadata primary_handoff, replaces y desplazamiento a _archivo/ por un único HANDOFF.md raíz, editable in-place y eliminable al cierre; separa continuidad de auditorías e informes fechados y prohíbe MEMORY.md o archivos de sesión como continuidad del repositorio."
autor: FS
creado: 2026-08-02
lang: es
tags: [openclaw, handoff, politica, continuidad, fleet]
familia: fuente
---

# Política de continuidad OpenClaw Fleet

La continuidad del repositorio tiene una sola superficie: `HANDOFF.md` en la raíz.
Existe únicamente cuando otra sesión debe retomar trabajo material inconcluso.

## Reglas

1. **Un solo archivo.** El nombre es siempre `HANDOFF.md`: sin fecha, sufijo,
   versión paralela, carpeta de sesiones ni metadata de reemplazo.
2. **Existencia condicional.** Si no queda trabajo material inconcluso, el archivo no
   existe. No se crea para registrar un cierre ni por ceremonia.
3. **Actualización directa.** Mientras el trabajo siga abierto, se edita el mismo
   archivo in-place. Git conserva sus estados anteriores.
4. **Contenido mínimo.** Declara estado actual, pendiente material, riesgos o límites
   que cambian la acción y el siguiente paso verificable. No acumula crónica.
5. **Revalidación.** Un handoff orienta; no prueba actualidad. Antes de actuar se
   contrasta con Git, configuración, documentación oficial y runtime autorizado.
6. **Precedencia.** Nunca anula `AGENTS.md`, la configuración viva,
   `openclaw.json.reference`, la ley KORA ni `docs/openclaw/`.
7. **Cierre.** Se elimina cuando el pendiente se resuelve o deja de ser material.
   Git conserva la narrativa cerrada.

## Lo que no es continuidad

- Auditorías, informes, actas y evidencias pueden conservar fecha cuando la fecha es
  parte de su identidad observacional. No sustituyen `HANDOFF.md` ni se promueven por
  ser más recientes.
- `MEMORY.md` y `memory/` pertenecen al runtime privado de agentes OpenClaw bajo su
  política específica; no son memoria del repositorio ni handoff de Codex/Claude.
- No se crean `MEMORY.md`, bitácoras, cierres, resúmenes o archivos de sesión para
  suplir la ausencia de un pendiente real.

## Estructura recomendada

```markdown
# HANDOFF

Estado: <frase observable>

## Pendiente material

<solo lo que debe continuar>

## Al retomar

1. <primera verificación viva>
2. <siguiente acción>

## Riesgos o límites

<solo si cambian la conducta>
```

La fuente canónica de esta política vive en KORA. El symlink consumidor de Fleet no
se convierte en autoridad ni se edita como copia.
