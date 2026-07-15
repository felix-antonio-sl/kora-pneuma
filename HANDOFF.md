# Handoff vigente — 2026-07-15

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, git o GitHub. Verificar siempre el estado vivo antes
> de actuar. El handoff anterior quedó en
> `_archivo/HANDOFF-2026-07-14-modelamiento-opm.md`.

## Estado al cierre

- `hsc-agent-cli` v3.0.0 / contrato beta-3 está publicado en
  `felix-antonio-sl/hsc-agent-cli`, tag `v3.0.0`, commit `804bb37`.
- Manual canónico `urn:salud:kb:manual-agente-hsc-agent-cli` actualizado a
  v1.0.14.
- Agentes consumidores actualizados: `urgenciologo` v3.8.0 y
  `medico-hospitalista` v1.6.0.
- Ambos agentes fueron reemitidos y aplicados en Claude Code, Codex, OpenCode y
  OpenClaw. La paridad reporta 5 fiel, 0 desviadas y 0 no instaladas para cada
  uno.
- `python3 kora.py velar --estricto`: 13 checks coherentes.
- `python3 -m unittest discover -s tests`: 120 tests verdes.
- Los archivos locales no versionados
  `informe-desempeno-medico-hospitalista-2026-07-11.md` e
  `informe-turno-urgenciologo-2026-07-10.md` pertenecen al operador y
  permanecen fuera de staging y commits.

## Decisiones tomadas

1. La migración cambia solo el contrato de consumo del CLI; no altera la lógica
   clínica, los workflows ni la autoridad humana de los agentes.
2. `summary.source_issues[]` reemplaza brechas/severidades fabricadas por el
   CLI. `summary.bundle_integrity` se lee solo como identidad y adquisición,
   nunca como permiso terapéutico o suficiencia clínica.
3. `batch_plan.requests[]` es la única superficie de lotes. Los aliases
   `recommended_*` no se conservan.
4. SGH y Drive tienen temporalidad y gobernanza distintas. Los consumidores
   leen procedencia y discrepancias; ni CLI ni manual fijan precedencia.
5. HODOM usa presencia censal trivalente y solo direcciona Drive desde
   identidad documental con `identity_check.match=true` e
   `ingreso_id_verified=true` para el ingreso exacto.
6. La trazabilidad histórica del frontmatter conserva nombres de contratos
   retirados; el cuerpo vigente y los tests prohíben depender de ellos.

## Artefactos relevantes

- Manual:
  `artefactos/conocimiento/salud/manual-agente-hsc-agent-cli.md`.
- Agentes:
  `artefactos/agentes/salud/urgenciologo.md` y
  `artefactos/agentes/salud/medico-hospitalista.md`.
- Evals estructurales:
  `tests/test_hsc_agent_cli_consumers.py`.
- Decisión y evidencia upstream:
  `~/projects/hsc-agent-cli/docs/decision-beta-3-declinicalizacion-2026-07-15.md`
  y
  `~/projects/hsc-agent-cli/docs/handoff-2026-07-15-beta3-integridad-factual-v3.0.0.md`.

## Cómo retomar

1. Leer `CLAUDE.md` y este handoff; si divergen, gana el canon.
2. Ejecutar `git status -sb` y preservar los dos informes del operador.
3. Verificar `hsc-agent-cli --version`: `v3.0.0`, `beta-3`,
   `modified=false`.
4. Antes de cerrar cambios KORA, ejecutar:

   ```bash
   python3 kora.py velar --estricto
   python3 -m unittest discover -s tests
   ```

5. Si cambia alguno de los agentes, reemitir solo con `kora.py transmutar`,
   aplicar cada target y comprobar `--paridad`; nunca editar `_emision/` a
   mano.
