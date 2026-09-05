# AGENTS.md

## Misión

Modelo OPM de **{{dominio}}**: {{sistema o biblioteca de tipos y finalidad del modelo}}.

## Entrada y autoridad

- Usa `README.md` como entrada humana y declara el corpus que gobierna la semántica OPM.
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

{{regeneración, validación y comparación que permite la herramienta real; indica
la revisión manual necesaria cuando no exista una comprobación automática}}

- Verifica por separado el modelo, su serialización y su visualización.
- Revisa el diff completo y no presentes un render correcto como validación semántica.

## Seguridad y entrega

- No expongas secretos ni material restringido en modelos, prompts, exports o commits.
- No publiques ni modifiques herramientas o corpus vecinos fuera de la autoridad solicitada.
