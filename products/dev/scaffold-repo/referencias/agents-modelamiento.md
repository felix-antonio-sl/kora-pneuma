# AGENTS.md

## Misión

Modelo OPM de **{{dominio}}**: {{sistema o biblioteca de tipos y finalidad del modelo}}.

## Entrada y autoridad

- Usa `README.md` como entrada humana y declara el corpus que gobierna la semántica OPM.
- Este archivo añade solo reglas locales; hereda los contratos globales y de host
  aplicables, y la regla más cercana manda dentro de este repositorio.
- Si existe `HANDOFF.md`, léelo solo al retomar trabajo material inconcluso y
  revalídalo contra bundles, OPL, fuentes externas y Git.
- {{fuentes de dominio, herramienta de autoría y límites entre modelo y aplicación}}

## Estructura y modelamiento

- `models/` contiene los bundles versionados que son producto del repositorio.
- `opl/` contiene OPL derivado y no se edita a mano.
- `scripts/` contiene la regeneración reproducible cuando exista.
- Todo constructo se ancla a una fuente de dominio o se declara propuesto.
- La capacidad de la herramienta no sustituye la verdad conceptual ni la metodología.

## Verificación

{{comandos reales de regeneración, validación y comparación. Si no existen, escribe
`Verificación automatizada: ABSENT`.}}

- Verifica por separado el modelo, su serialización y su visualización.
- Revisa el diff completo y no presentes un render correcto como validación semántica.

## Continuidad

- `HANDOFF.md` es único, estable y solo existe mientras haya trabajo material
  inconcluso; actualízalo in-place y elimínalo al cerrar.
- No crees `MEMORY.md`, handoffs o continuidades fechadas, bitácoras ni archivos de
  sesión. Git conserva la narrativa cerrada.

## Seguridad y entrega

- No expongas secretos ni material restringido en modelos, prompts, exports o commits.
- No publiques ni modifiques herramientas o corpus vecinos fuera de la autoridad solicitada.
