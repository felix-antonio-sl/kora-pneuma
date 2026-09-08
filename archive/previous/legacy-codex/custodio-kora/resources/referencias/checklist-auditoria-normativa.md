# Checklist De Auditoria Normativa

Usar esta checklist para revisar specs, artefactos, toolchain o cambios
estructurales. Cada item que falle debe convertirse en finding con regla,
evidencia, impacto y fix.

## 1. Fuente Y Precedencia

- La fuente primaria es clara y no es derivada.
- La regla usada pertenece a la capa correcta.
- No hay contradiccion con una capa de mayor precedencia.
- El cambio no usa README, handoff viejo o output runtime como autoridad.

## 2. Identidad Y Lifecycle

- URN usa regimen correcto: `kb` para conocimiento/spec, `artefacto` para
  agentes y skills.
- Version esta fuera del URN.
- `status` pertenece al lifecycle del tipo de objeto.
- `supersedes`, `depends`, `cites` o relaciones equivalentes apuntan a URNs
  resolubles.

## 3. Artefactos Agenticos

- Existe fuente primaria `SKILL.md` para `forma_material: habilidad` o
  `AGENT.md` para las demas formas.
- El frontmatter usa `_manifest`, `version`, `status`, `nombre`,
  `descripcion`, `extensions.kora` y `artefacto`.
- `vector_ontologico` cumple rangos y leyes inter-eje.
- `atlas.forma_material` encaja con el vector y la topologia.
- `conocimiento_permitido` usa URNs, no paths.
- Riesgos no triviales tienen invariantes, `qa_budget` o `risk_register`.
- Las habilidades con subdirs tienen `## Recursos` y solo usan `scripts/`,
  `referencias/` o `recursos/`.

## 4. Knowledge Y Specs

- El documento sigue KORA/MD y el perfil aplicable.
- La precedencia esta declarada por `relations` o seccion explicita.
- `relations.depends` expresa autoridad; `relations.cites` expresa apoyo.
- `Traces to:` solo apunta a la Formal Layer oficial cuando se usa esa forma.
- No hay paths duros sustituyendo URNs en relaciones gobernadas.
- Las tablas normativas tienen enforcement cuando la spec lo exige.

## 5. Runtime Y Transmutacion

- El IR canonico existe antes del runtime output.
- El target esta dentro del dominio de su runtime-extension.
- La perdida de proyeccion esta declarada; no se oculta como warning informal.
- `_BUILD/` y `_transmutation.yml` no suplantan la fuente primaria.
- Cambios runtime no alteran el vector salvo decision normativa explicita.

## 6. Toolchain Y Docs Derivadas

- `docs/generated/catalog.yml` se regenera por `python3 toolchain/kora index`.
- No se escriben conteos materializados a mano.
- Un check nuevo tiene spec_ref y severidad coherentes.
- Tests cubren cambio de comportamiento compartido.
- Si se toca knowledge graph, se revisa `kb-graph --json --orphans`.

## Finding Minimo

```text
[severity] titulo
Regla: URN + seccion o archivo propietario
Evidencia: archivo:linea, comando o test
Impacto: que invariantes rompe
Fix: artefacto, spec, check, test o deuda residual
```
