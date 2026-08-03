# CLAUDE.md

Contrato operativo de Claude Code para este repositorio. Codex usa su contrato autónomo
en `AGENTS.md`. Versionado independiente; para concerns cross-cutting del host, ver
`~/CLAUDE.md`.

## Qué es este repo

<!-- Modelo OPM (ISO 19450) de {{dominio}}, construido con opforja. NO es software
     ejecutable: es un corpus de modelos versionados (bundle JSON OPM + OPL derivado).
     Di cuál de los dos sabores es: modelo de SISTEMA (top-down SD0 → in-zoom) o
     biblioteca de TIPOS/greda (proyección reproducible desde una ontología upstream). -->
Modelo OPM de **{{dominio}}** — {{una línea: qué sistema o greda, y para qué}}.

## Estructura

| Path | Contiene |
|------|----------|
| `models/` | Bundles `JSON OPM` exportados de opforja. **Se versionan** (son el producto). |
| `opl/` | OPL derivado del generador. **Nunca se edita a mano.** |
| `scripts/` | `generar-bundle.ts` — regenera bundle/OPL; consume la librería de autoría de opforja. |
| `docs/` | {{derivaciones y decisiones de modelado con su ancla externa — agrégalas cuando las tengas}} |

## Herramienta: opforja

- App: `https://opforja.sanixai.com` · librería de autoría: `~/projects/deep-opm-pro/app/src/autoria/`.
- **El bundle se regenera, no se edita a mano** (`bun scripts/generar-bundle.ts`); el `opl/` es derivado.
- **El agente NO opera opforja por el browser:** Felix opera la app; el agente dirige paso a paso
  (elemento, nombre exacto, tipo, esencia/afiliación, enlace, OPL esperado).
- Disciplina de modelado: skill **`modelamiento-opm`** (dialéctica de construcción) + persona
  **`dov-dori`** / skill `pensamiento-modelador` (razonamiento). El lenguaje OPM y el OPL se anclan al
  corpus OPM/Forja SSOT (`urn:fxsl:kb:reglas-opm-estrictas-es` y specs forja, en `~/kora-pneuma`).
- **Anclaje externo:** todo objeto/proceso/estado/enlace cita su fuente (normativa o dominio, o el
  propósito ya derivado); sin ancla → *propuesto*, no descriptivo.

## Bitácora y vigencia

- `BITACORA.md` — registro cronológico **append-only** de sesiones, decisiones e hitos de versión del
  bundle. Se versiona; no entra en `_archivo/`.
- **Vigencia documental** (handoff e informes-serie): un solo vigente por especie, versionado por fecha
  (`<especie>-AAAA-MM-DD.md`, inmutable); el previo se mueve a `_archivo/` (gitignorado). La bitácora
  **no** entra en vigencia.

## Convenciones

Hereda de `~/CLAUDE.md`: docs en **es-CL**, identificadores en **inglés**, fechas **ISO**, kebab-case.
OPL en es-ES; nombres de constructos OPM según el corpus.

## Qué NO hacer

- No editar `opl/` ni el bundle a mano — se regeneran desde `scripts/`.
- No justificar una regla de modelado por lo que opforja sabe dibujar: la verdad del dominio ≠ la
  capacidad de la herramienta.
- No volcar secretos ni código de aplicación: esto es modelado, no software.
