# KORA — encarnación pneuma

KORA es el repositorio, catálogo y sistema de producción y mantenimiento de
artefactos que consumen o ejecutan sistemas LLM. Gestiona **tres tipos de
artefacto, y solo tres** — conocimiento (se lee), agentes y skills (se
proyectan a runtimes) — los resuelve por nombre verdadero (URN), los mantiene
coherentes en el tiempo y los transmuta a encarnaciones concretas declarando
toda pérdida.

Esta es la **encarnación pneuma**: el cuerpo que quedó cuando la encarnación
anterior (`~/kora`, "la bestia": 16k líneas de toolchain, 8k de specs, 37
checks, 24 comandos) ardió hacia adentro y soltó la coraza. La entidad es la
misma; los URN no cambiaron. Léase en este orden:

1. **`ALMA.md`** — qué es KORA cuando se le quita todo cuerpo. Documento
   fundacional: lo que el alma no exige, este cuerpo no lo carga.
2. **`GENESIS.md`** — el sello de la reencarnación: qué ascendió, qué cayó
   (con razón, pieza por pieza), qué se ganó, qué se debe.
3. **`ley/`** — la ley en cuatro estratos y cinco documentos: constitución,
   ontología (PMI × LFS), forma (el shape y su gramática en `ley/2`, la
   producción korificada en `ley/4` — mismo estrato), transmutación (el
   funtor y sus matrices).

La ley entera más el alma caben en ~17k tokens: **KORA completa es cargable
como contexto de un LLM**. Ese es el punto.

## Los seis gestos

```bash
python3 kora.py censo                  # el catálogo, siempre derivado, jamás autoridad
python3 kora.py nombre <urn>           # resolver un nombre verdadero (también muertos)
python3 kora.py velar [--estricto]     # los 13 checks: que nada se contradiga
python3 kora.py transmutar --urn U --target T [--aplicar|--stdout]
                                       # proyección funtorial con sello y pérdida declarada
python3 kora.py ciclo <urn> <estado>   # lifecycle: solo hacia adelante, jamás de vuelta
python3 kora.py ley                    # toda la ley a stdout — KORA en un contexto
```

Targets realizados: `claude-code`, `codex`, `opencode`, `openclaw` (este último
emite un **workspace** multi-archivo: AGENTS.md + SOUL.md; `ley/3 §7.1`, cierra la
deuda de GENESIS §4 sin editar GENESIS). Reconocido pero no realizado: `hermes`.

## Topología

```
ALMA.md                  el alma (fundacional)
GENESIS.md               la reencarnación, proof-carrying
ley/0-constitucion.md    identidad, precedencia, lifecycle, URN
ley/1-ontologia.md       el axioma, los 6 ejes, las 5 leyes inter-eje, el arnés
ley/2-forma.md           gramática del frontmatter, shape, zonas, relaciones
ley/3-transmutacion.md   el funtor, las matrices, el sello, la honestidad
ley/4-koraficacion.md    la fábrica: FS=100%, CR, prueba ácida, telegrafización
kora.py                  el núcleo entero (stdlib puro, Python ≥ 3.11)
artefactos/
  conocimiento/{ns}/{id}.md
  agentes/{ns}/{nombre}.md
  skills/{ns}/{nombre}/SKILL.md
tests/test_kora.py       la suite de unidad del núcleo
_emision/                emisiones transmutadas (derivado, gitignored)
censo.json               vista derivada opcional (gitignored)
```

Un artefacto es **un archivo**: frontmatter plano (subconjunto regular de
YAML, gramática en `ley/2`) + cuerpo markdown. El tipo no se declara — se
deriva de la posición: con `vector` y `forma: habilidad` es skill; con
`vector` y otra forma es agente; sin `vector` es conocimiento.

## Verificación

```bash
python3 -m unittest discover -s tests   # suite completa
python3 kora.py velar --estricto        # gate de mantenimiento
```

## Relación con la bestia

`~/kora` sigue viva y es autoritativa para su corpus —legacy en
estrangulamiento, congelada salvo correcciones de verdad (`ley/0` §1)—.
Pneuma nació el 2026-06-11 con 3 semillas (`alma-de-kora`, `mente-omega`,
`polymath`) y se gana el corpus artefacto por artefacto, demostrando que la
ley leve basta en vez de heredarlo por decreto: con URN preservado y
procedencia con hash, como manda `GENESIS.md`. Cuánto lleva ganado lo dice
el censo vivo (`python3 kora.py censo`), nunca un número escrito aquí.
