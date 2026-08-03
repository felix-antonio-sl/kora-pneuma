# AGENTS.md

## Misión

{{conocimiento que custodia este corpus, para quién y con qué finalidad}}

## Entrada y autoridad

- Usa `README.md` como entrada humana y lee solo las fuentes necesarias para la tarea.
- Este archivo añade solo reglas locales; hereda los contratos globales y de host
  aplicables, y la regla más cercana manda dentro de este repositorio.
- Si existe `HANDOFF.md`, léelo solo al retomar trabajo material inconcluso y
  revalídalo contra el filesystem y Git.
- {{fuente canónica, precedencia, índices derivados y referencias externas}}

## Curaduría y estructura

- {{qué entra al corpus, qué se referencia y qué queda fuera}}
- {{directorios de fuente y derivados; declara explícitamente cuáles no se editan}}
- No hay código ejecutable salvo herramientas curatoriales expresamente declaradas.
- Preserva procedencia, disenso, límites de evidencia y una sola fuente por objeto.

## Verificación

{{comandos reales de forma, índice o consistencia. Si no existen, escribe
`Verificación automatizada: ABSENT`.}}

- Distingue validez formal, verdad semántica y efecto runtime.
- Revisa el diff completo y no presentes memoria o vistas derivadas como estado vivo.

## Continuidad

- `HANDOFF.md` es único, estable y solo existe mientras haya trabajo material
  inconcluso; actualízalo in-place y elimínalo al cerrar.
- No crees `MEMORY.md`, handoffs o continuidades fechadas, bitácoras ni archivos de
  sesión. Git conserva la narrativa cerrada.

## Seguridad y entrega

- No copies secretos, PII/PHI ni material restringido al corpus.
- No publiques, instales ni modifiques consumidores fuera de la autoridad solicitada.
