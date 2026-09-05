---
urn: urn:openclaw-fleet:kb:fleet-canon-policy
nombre: fleet-canon-policy
version: 3.1.0
estado: publicado
descripcion: "Política de propiedad, precedencia y frontera entre KORA, la documentación oficial de OpenClaw, los blueprints y el runtime de la flota."
fuente: "Migrado desde el blob Git 8b26f4b4825544dcb35f2c928d8e5f8b73f4e74b:docs/fleet-canon-policy.md de /home/felix/openclaw-fleet; sha256:ac14f42878acddf3a0ff3ab3768f9147a61972d10da4ac55921a84ba068c0ea5. El cuerpo preserva paridad exacta con ese blob y el frontmatter se normaliza al shape plano de KORA. El path vivo /home/felix/openclaw-fleet/docs/fleet-canon-policy.md es un symlink consumidor hacia este artefacto, no otra fuente de verdad."
autor: FS
creado: 2026-08-02
lang: es
tags: [openclaw, kora, canon, flota, politica]
familia: fuente
depende: [urn:kora:kb:regimen-de-ley]
---

# Política de canon OpenClaw/KORA de la flota v3.1.0

Esta política fija propiedad y precedencia entre KORA, la flota, la
documentación oficial de OpenClaw y el runtime. No contiene modelos, cuentas ni
proveedores concretos: ese estado es volátil y pertenece a la configuración
viva validada y a su snapshot versionado y redactado.

## Matriz de autoridad

| Superficie | Fuente de verdad | Regla |
| --- | --- | --- |
| Doctrina KORA | `~/kora-pneuma/ley/` y `~/kora-pneuma/artefactos/` | Única autoridad doctrinal activa; resolver por URN. |
| Semántica OpenClaw | `docs/openclaw/` | SSOT local de la documentación oficial; no editar a mano. |
| Procedencia documental OpenClaw | `.upstream-source`, `.content-manifest` y `.web-overlay-manifest` | Demuestran el árbol Git oficial, la integridad local y las rutas publicadas solo en la web. |
| Config runtime | `~/.openclaw/openclaw.json` validado por CLI | Autoridad del estado vivo; nunca se versiona. |
| Config versionada | `openclaw.json.reference` | Copia redactada de la config viva; debe quedar sin drift. |
| Membresía de flota | igualdad entre `blueprints/`, reference y config viva | Solo una relación positiva local autoriza despliegue. |
| Doctrina versionada | `blueprints/<agent-id>/` | Fuente declarativa gestionada por Git; sin estado mutable. |
| Workspace vivo | `~/.openclaw/workspaces/<agent-id>/` | Runtime privado materializado; memoria y estado no se versionan. |
| Operación del repo | `CLAUDE.md` y políticas bajo `docs/` | Scaffolding, seguridad, memoria y continuidad locales. |
| Perfil de datos | `urn:salud:kb:perfil-dev-personal-full` realizado por `docs/data-handling-profiles.md` | Autoriza datos reales en la superficie privada; no amplía herramientas, rol ni destinos. |
| Instrucciones agénticas emitidas | Fuente Pneuma nombrada en `kora:sello` | `AGENTS.md` y `SOUL.md` sellados son derivados; se retransmutan. |

## Reglas primarias

1. La config viva validada manda sobre cualquier resumen, memoria o handoff.
2. `openclaw.json.reference` se sincroniza y redacta después de cambiar la
   config viva. `bash scripts/diff-reference.sh` debe quedar verde.
3. Un handoff conserva continuidad y evidencia; no anula una configuración
   posterior ni reemplaza doctrina KORA u OpenClaw.
4. Para cualquier asunto de OpenClaw se consulta primero `docs/openclaw/`.
   Se actualiza solo mediante los scripts de sincronización. Si una verificación
   de frescura detecta divergencia con las fuentes oficiales, se bloquea la
   decisión y se repara el sync; no se elige una fuente en silencio. La
   frescura Git compara el árbol `docs/`, no cambios vecinos del mismo commit,
   y los overlays web se comparan byte a byte.
5. Todo `AGENTS.md` o `SOUL.md` con sello `kora:sello` se modifica en
   `~/kora-pneuma/artefactos/` y se retransmuta. No se parchea a mano.
6. `IDENTITY.md`, `TOOLS.md`, `HEARTBEAT.md` y `BOOT.md` son scaffolding
   declarativo de la flota. `USER.md`, memoria y archivos operativos son
   privados del runtime.
7. El conocimiento de consulta nuevo no se copia a `reference/` o `kb/` en la
   raíz de un agente. Se autora en Pneuma y se referencia por URN. Una skill sí
   puede empaquetar referencias autocontenidas que formen parte de su propia
   capacidad; no puede convertirlas en una copia de un corpus externo.
8. La encarnación Kora anterior, los symlinks externos y las bibliotecas
   locales no son fallback. Una ausencia se escala a curaduría en Pneuma.
9. Capacidad global y membresía son distintas, pero también lo son membresía
   y visibilidad de skills. Una persona retirada puede conservarse para otros
   runtimes en Kora-Pneuma o `~/.agents/skills`; en OpenClaw debe quedar
   explícitamente deshabilitada bajo `skills.entries` para que no reaparezca
   en prompts, comandos ni snapshots de sesión.
10. Los operativos siguen `docs/handoff-policy.md`; la memoria sigue
    `docs/memory-policy.md`.
11. El tratamiento de PII/PHI sigue `docs/data-handling-profiles.md`. Detectar
    PII no es por sí solo un bloqueo bajo `DEV_PERSONAL_FULL`; secretos, Git,
    destinos nuevos, mutaciones clínicas y autoridad final conservan sus
    gates.

## Frontera fuente/runtime

- **Fuente agéntica**: artefacto bajo `~/kora-pneuma/artefactos/agentes/`.
- **Emisión**: `AGENTS.md` y `SOUL.md` con sello; derivada y regenerable.
- **Blueprint fleet**: emisión más scaffolding declarativo bajo
  `blueprints/<agent-id>/`.
- **Materialización**: `scripts/materialize-workspace.sh`, limitada a archivos
  trackeados y con manifiesto de propiedad.
- **Runtime**: `~/.openclaw/`, workspaces vivos, memoria, sesiones, índices,
  secretos y estado del gateway; nunca se versiona.

Antes de editar un blueprint, comprobar si el archivo porta `kora:sello`. Si lo
porta, detener la edición local y cambiar la fuente Pneuma. Si no lo porta,
aplicar el cambio mínimo en fleet, materializar y verificar una sesión nueva.

## Estado volátil

Modelos, auth, plugins, embeddings, cuentas y bindings se consultan en este
orden:

1. CLI/config viva para el estado real.
2. `openclaw.json.reference` para el snapshot versionado.
3. El handoff vigente para contexto de continuidad, nunca como autoridad.

No se duplican en esta política.

## Límites

- El material bajo `docs/legacy/` es histórico y no puede prevalecer sobre las
  fuentes de la matriz.
- Una regla local puede ser más estricta que esta política, pero no invertir su
  precedencia ni convertir un derivado en fuente.
