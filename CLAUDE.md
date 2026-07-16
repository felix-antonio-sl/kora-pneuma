Hereda de ~/CLAUDE.md

# CLAUDE.md — orientación de agente (corpus KORA pneuma)

> **Este archivo es un doc auxiliar** (`ley/0` §5, estrato 5): orienta a quien
> entra, **no legisla**. No es la fuente de verdad y no la duplica. Ante
> cualquier conflicto mandan `ALMA.md` y `ley/0..4`. Si algo aquí contradice la
> ley, la ley gana y este archivo está mal.

**Qué es esto.** `~/kora-pneuma/` es la encarnación vigente de KORA: el
repositorio que produce, cataloga y mantiene los **tres tipos de artefacto, y
solo tres** —conocimiento (se lee), agentes y skills (se proyectan a runtimes)—
resolviéndolos por URN y transmutándolos con pérdida declarada. Arquetipo:
**conocimiento**. No es una app: no hay build; el «núcleo» es `kora.py` (stdlib
puro). KORA completa cabe en un contexto LLM (`python3 kora.py ley`).

**Fuente única de verdad (en este orden).** No la repitas; léela:

1. `ALMA.md` — qué es KORA sin cuerpo (fundacional; del que desciende la ley).
2. `GENESIS.md` — sello proof-carrying de la reencarnación. **Acta histórica:
   no se edita** (sus conteos son del 2026-06-11, por diseño).
3. `ley/0..4` — la ley, con **precedencia**: constitución › ontología ›
   forma+koraficación › transmutación › derivados. Un estrato inferior puede
   estrechar, nunca relajar.
4. `README.md` — la puerta de entrada y la topología.

Atajos consumibles: `urn:kora:kb:guia-rapida-pneuma` y
`urn:kora:kb:regimen-de-ley` (régimen de estrangulamiento bestia→pneuma).

**Los seis gestos** (`kora.py`): `censo`, `nombre <urn>`, `velar [--estricto]`,
`transmutar`, `ciclo`, `ley`. El censo y `_emision/` son **derivados** (jamás
autoridad, gitignored): el filesystem con frontmatters válidos es la única
fuente. Nunca edites un derivado a mano. No persistas recuentos ni estimaciones
de inventario, tamaño o cobertura en docs vivas: obtén el dato bajo demanda con
el gesto que corresponda.

**Gate de mantenimiento** (correr siempre antes de cerrar):

```bash
python3 kora.py velar --estricto    # gate completo de coherencia
python3 -m unittest discover -s tests
```

**Doctrina operativa del frente** (no negociable):

- pneuma es la **fuente única** de doctrina futura; `~/kora` (la bestia) es
  **legacy congelada**. Para traer algo de la bestia: **migrar-o-omitir**, nunca
  desarrollar nuevo conocimiento allí.
- **Reemitir no es desplegar.** La reemisión local sin `--aplicar` solo renueva
  un derivado: no sustituye las gates ni autoriza desplegar. `--aplicar` exige
  las gates verdes. La emisión porta su versión y `hash-fuente`; los
  consumidores externos leen ese sello, no el frontmatter.
- **Cierre de despliegue proporcional.** Tras las gates, verificar cada
  artefacto agéntico modificado con `transmutar --paridad --urn <URN>`. Si
  cambia el contrato o la implementación de transmutación (`ley/3` o el tramo
  correspondiente de `kora.py`), ejecutar paridad global; usar `--target` solo
  si el cambio está contenido en un target. `desviada` y `sin-emision`
  bloquean; `no-instalada` solo informa. La paridad permanece fuera de `velar`
  porque observa instalaciones externas.
- **Verificar contra el estado real** (censo, `git diff`, line-refs), no contra
  el reporte ni la hipótesis de un subagente.
- **`velar` valida forma, no verdad.** La fidelidad semántica (FS=100% de una
  koraficación, `ley/4`) es obligación declarada del productor: el núcleo no la
  mecaniza y la ley lo confiesa. No finjas demostrado el puente prometido.

**Vigencia documental.** Un solo vigente por especie; los docs operativos
muertos (informes, auditorías ya ejecutadas) se desplazan a `_archivo/`
(gitignored), no se borran. Los **artefactos** no se mueven: se deprecan/retiran
in-place y su URN sigue resolviendo (KORA no borra: jubila).

**Continuidad operativa.** Antes de retomar trabajo heredado, leer
`HANDOFF.md`: es la única memoria de sesión vigente y siempre está subordinada
al canon y al estado verificable del repositorio. Al reemplazarla, mover la
anterior a `_archivo/` y no mantener dos handoffs activos.
