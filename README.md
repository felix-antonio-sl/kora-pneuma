# KORA pneuma

KORA pneuma es la fuente canónica para conocimiento curado, agentes y skills
resueltos por URN. Preserva una fuente por objeto y proyecta artefactos a
runtimes mediante transmutaciones con pérdida declarada.

## Autoridad

- `ALMA.md`: finalidad y naturaleza de KORA.
- `ley/0-constitucion.md` a `ley/4-koraficacion.md`: norma y precedencia.
- `artefactos/`: fuentes canónicas de conocimiento, agentes y skills.
- `kora.py`: núcleo ejecutable de censo, resolución, validación, transmutación
  y lifecycle.

`GENESIS.md` es un acta histórica inmutable. `censo.json`, `_emision/`,
reportes e instalaciones son derivados; no se editan como autoridad.

## Entrada

- [AGENTS.md](AGENTS.md): postura operativa y contrato para Codex.
- Lee solo la ley y las fuentes pertinentes a la tarea.
- Si existe `HANDOFF.md`, úsalo únicamente para retomar trabajo inconcluso y
  revalídalo contra el filesystem y Git.

`CLAUDE.md` importa el mismo contrato de `AGENTS.md`.

## Operación

Requiere Python 3.11 o superior; `kora.py` usa solo la biblioteca estándar.

```bash
python3 kora.py censo
python3 kora.py nombre <urn>
python3 kora.py velar --estricto
python3 kora.py transmutar --urn <urn> --target <target> --stdout
python3 kora.py transmutar --paridad --urn <urn>
python3 -m unittest discover -s tests
```

`--aplicar`, cambios de lifecycle y operaciones sobre runtimes requieren
autoridad explícita. Validez formal, emisión o paridad no demuestran conducta,
safety, aceptación humana ni autorización del runtime.
