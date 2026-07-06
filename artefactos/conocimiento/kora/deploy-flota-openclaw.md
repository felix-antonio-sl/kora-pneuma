---
urn: urn:kora:kb:deploy-flota-openclaw
nombre: deploy-flota-openclaw
version: 1.0.0
estado: publicado
descripcion: "Runbook del deploy pneuma→flota openclaw viva: gate de canon del runtime, diff anti-despotenciación, escalones por riesgo con HITL clínico, renombre atómico de agente, guardias path-dependientes y paridad de cierre. Destilado de la ejecución real 2026-07-06."
fuente: "Destilado el 2026-07-06 de la ejecución real de la Fase A del plan tres-frentes (kora-pneuma commits 0d1e76b..e8745ff; openclaw-fleet ec12ac6..3ed79f4): 9 escalones, 3 renombres, 4 absorciones upstream con HITL, 2 hallazgos post-gate (guardias PII, identidad en preservados). Directivas duraderas del operador (FS): canon del runtime en cada transmutación; anti-despotenciación. El procedimiento vivía solo en la memoria del agente ejecutor y en un ledger gitignored; este kb lo hace resoluble por URN."
autor: FS
creado: 2026-07-06
lang: es
tags: [deploy, openclaw, flota, runbook, paridad, anti-despotenciacion, canon-runtime, hitl]
cita: [urn:kora:kb:regimen-de-ley]
familia: nota
---

# deploy-flota-openclaw

Runbook del despliegue de agentes pneuma a la flota OpenClaw viva
(`~/openclaw-fleet/workspaces/`, gateway systemd `:18790`). El funtor emite
(`ley/3 §7.1`); **desplegar es otra cosa**: instala sobre un runtime con
estado, memoria y gobernanza propios. Sobrescribir un bot vivo es
producción.

## Precondiciones (gates de entrada)

1. `python3 kora.py velar --estricto` → 13/13. Nunca transmutar en rojo.
2. **Canon del runtime, leído en cada corrida** (directiva del operador): el
   canon muta. Mirror local `~/openclaw-fleet/docs/openclaw/` (sync diario;
   verificar frescura < 48 h). Páginas clave: `concepts/system-prompt.md`
   (bootstrap files y **límites de inyección**: `bootstrapMaxChars` 20000
   chars/archivo, 60000/workspace — medir las emisiones SIEMPRE; si un
   AGENTS.md excede, override per-agent `agents.list[].bootstrapMaxChars`
   ANTES de aplicar, o el runtime trunca en silencio),
   `gateway/config-agents.md` (registro `agents.list[]`).
3. **Gobernanza de la flota**: leer `~/openclaw-fleet/CLAUDE.md` (config viva
   vía CLI y nunca a mano; el reference se sincroniza DESPUÉS con
   `scripts/diff-reference.sh`; hook PII pre-commit activo).

## Diff anti-despotenciación (antes de pisar nada)

Por cada agente, comparar el `AGENTS.md`/`SOUL.md` **vivo** contra la
emisión, clasificando cada capacidad del vivo: **cubierta** (equivalente en
la emisión) · **preservada** (vive en archivo que no se pisa) ·
**legacy-reemplazada** (infraestructura obsoleta; adjudicar) · **EN RIESGO**
(solo en el vivo). Un ítem EN RIESGO bloquea su escalón hasta resolverse con
HITL: **absorber upstream** (editar la fuente pneuma, `velar`,
re-transmutar) o **pérdida aceptada declarada**. Jamás editar workspace o
emisión a mano. Dos superficies que el diff de capacidades no cubre y se
barren aparte:

- **Identidad en preservados**: `USER.md`/`IDENTITY.md`/`BOOT.md` se
  inyectan al prompt y pueden portar nomenclatura vieja (caso real: un
  `USER.md` decía «usa KORA como copiloto» y el agente se presentaba como
  KORA). Barrer `rg` de nombres viejos/genéricos.
- **Parches del operador en el vivo** (secciones añadidas a mano): detectar,
  y decidir destino con HITL antes del deploy.

## Escalones (orden por riesgo, uno a la vez)

1. Piloto: blueprint no-vivo, nombre ya alineado.
2. Renombres solo-filesystem (workspaces sin registro en gateway).
3. Vivos nombre-alineado, no clínicos.
4. Clínicos e íntimos AL FINAL, cada uno con pausa HITL del operador.

Ciclo por escalón: `transmutar --urn U --target openclaw --aplicar` (escribe
SOLO `AGENTS.md`+`SOUL.md`; preserva el resto) → verificar con
`git -C ~/openclaw-fleet status --short workspaces/<n>/` que NADA más cambió
→ `openclaw gateway restart` → `openclaw health` verde → sonda de un turno
(`openclaw agent --agent <id> -m "..."`: identidad, frontera, capacidad
rescatada) → commit en la flota **stageando solo los 2 archivos por
pathspec** (jamás el directorio: riesgo PII en `MEMORY.md` clínicos).
Rollback: `git checkout <commit> -- workspaces/<n>/ && openclaw gateway
restart`.

## Renombre de agente (operación mayor)

`--aplicar` es name-keyed: sin renombrar antes el workspace vivo, crea un
huérfano duplicado. Con **gateway detenido**:

1. `git mv workspaces/<viejo> workspaces/<nuevo>` (preserva historia y
   memoria).
2. `mv ~/.openclaw/agents/<viejo> ~/.openclaw/agents/<nuevo>` (estado
   runtime; `agentDir` por defecto deriva del id).
3. Config viva: el renombre es **multi-campo** (`agents.list[].id/name/
   workspace/agentDir/identity.name`, `tools.agentToAgent.allow[]`,
   `bindings[].agentId`, listas de plugins como `active-memory.agents[]`) y
   `openclaw config set` valida atómicamente POR CAMPO — rechaza todo estado
   intermedio. Editar el JSON vivo en **una sola escritura atómica**, luego
   `openclaw config validate` y espejar al reference
   (`scripts/diff-reference.sh` debe dar OK).
4. Las **cuentas Telegram conservan su nombre** (`match.accountId`): son
   canal de entrega, no identidad del agente.
5. **Barrer el nombre viejo en artefactos operativos path-dependientes**:
   `.gitignore` (guardias de `memory/` clínicos), hooks
   (`scripts/check-pii.sh`), scripts, workspaces vecinos, autorreferencias
   de los preservados. Regla: `rg <nombre-viejo>` y repuntar cada match
   leído — la config del gateway no es la única superficie.

## Gates de cierre

- Cero workspaces duplicados; sellos `kora:sello` presentes en todos los
  desplegados; `openclaw health` verde; `velar --estricto` 13/13.
- **Paridad de despliegue** (`ley/3 §9.1`): `python3 kora.py transmutar
  --paridad` → 0 desviadas en TODOS los targets — `velar` no ve las
  instalaciones; solo la paridad detecta stale silencioso o edición manual
  del runtime.
- Actualizar `~/openclaw-fleet/CLAUDE.md` (inventario, nombres) y pushear
  ambos repos al cerrar: un remote a medias hace que otra sesión diagnostique
  sobre una foto incompleta.

## Fronteras de este runbook

No gobierna: la config de deploy del gateway (modelos, bindings nuevos,
canales — gobernanza de la flota), la memoria de los agentes (memory-policy
de la flota), ni la autoría de fuentes (ley/2 y `agent-architect`). El
régimen de fondo es `urn:kora:kb:regimen-de-ley`: pneuma es la fuente única;
el workspace desplegado es derivado — editarlo a mano es drift.
