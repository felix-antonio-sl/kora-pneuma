# KORA pneuma

KORA pneuma es un repositorio de **conocimiento gobernado** con una herramienta
de soporte. Mantiene una fuente canónica por objeto, identifica cada artefacto
mediante URN y proyecta agentes y skills a distintos runtimes declarando toda
pérdida de fidelidad.

El problema que resuelve es la deriva: que una capacidad tenga versiones
aparentemente equivalentes, pero semánticamente distintas, repartidas entre
documentos, prompts, instalaciones y runtimes. KORA conserva el significado en
la fuente y hace que las demás representaciones sean derivables y auditables.

No es una aplicación ni un runtime. `kora.py` y `tests/` sostienen el corpus;
no cambian su arquetipo principal.

## Orientación en cinco minutos

1. Lee este archivo para ubicarte.
2. Revisa el [estado vigente](docs/handoffs/handoff-2026-08-09.md) antes de
   asumir que una versión, un conteo o un runtime siguen iguales.
3. Lee [ALMA.md](ALMA.md) y el estrato pertinente de `ley/` si la decisión es
   estructural o normativa.
4. Lee [AGENTS.md](AGENTS.md) antes de modificar fuentes. `CLAUDE.md` importa
   ese contrato sin duplicarlo.
5. Usa `python3 kora.py nombre <urn>` para resolver un objeto y sigue las URN
   que declare su frontmatter.

## Mapa de autoridad y vigencia

| Superficie | Función | Vigencia |
|---|---|---|
| `README.md` | Introducción y navegación humana | vigente, no normativa |
| `ALMA.md` | Finalidad y criterio de interpretación | fundacional |
| `ley/0..4` | Especificaciones y decisiones normativas | vigentes; prevalecen por estrato |
| `artefactos/` | Fuentes canónicas de conocimiento, agentes y skills | manda el `estado` de cada frontmatter |
| [Guía rápida](artefactos/conocimiento/kora/guia-rapida-pneuma.md) | Operación detallada | vigente, subordinada a la ley |
| `AGENTS.md` y `CLAUDE.md` | Contrato operativo para agentes de desarrollo | vigente, no normativo para KORA |
| `docs/handoffs/` | Estado verificable y próximos pasos | solo el archivo ISO más reciente está activo |
| Notas exploratorias fuera del canon | Hipótesis y trabajo en curso aún no clasificado | no autoritativas |
| `GENESIS.md` | Decisiones de fundación y pérdidas de la sublimación | histórico e inmutable |
| Git y `_archivo/` | Trazabilidad histórica | no describen por sí solos el estado actual |

Un artefacto `publicado` o `activo` está vigente. `borrador` es material en
elaboración y no equivale a conocimiento publicado. `deprecado` y `retirado`
son obsoletos para uso nuevo, pero sus URN siguen resolviendo por diseño.

## Organización

- `ley/`: constitución, ontología, forma, transmutación y koraficación.
- `artefactos/conocimiento/`: corpus que consumen sistemas LLM.
- `artefactos/agentes/`: especificaciones gobernadas de actores.
- `artefactos/skills/`: capacidades proyectables y sus referencias.
- `docs/handoffs/`: un solo corte operativo vigente por especie.
- `_archivo/`: versiones operativas históricas, fuera del árbol Git activo.
- `kora.py`: censo, resolución, validación, lifecycle y transmutación.
- `tests/`: pruebas del núcleo y de contratos focales.

`censo.json` y `_emision/` son derivados regenerables. Los conteos, reportes,
instalaciones runtime y notas locales ignoradas tampoco son autoridad.

## Operación básica

Requiere Python 3.11 o superior y no instala dependencias externas.

```bash
python3 kora.py censo
python3 kora.py nombre <urn>
python3 kora.py velar --estricto
python3 kora.py transmutar --urn <urn> --target <target> --stdout
python3 kora.py transmutar --paridad
python3 -m unittest discover -s tests
```

`transmutar` sin `--aplicar` solo materializa una emisión local derivada.
Instalación, lifecycle, publicación Git, despliegue y aceptación humana son
acciones distintas y requieren su autoridad correspondiente. Forma válida,
paridad o tests verdes no prueban conducta, safety ni autorización runtime.

## Dónde vive cada decisión

- Una regla normativa durable vive en `ley/`.
- El significado de una capacidad o cuerpo de conocimiento vive en su fuente
  bajo `artefactos/`.
- Un mecanismo vive en `kora.py` y queda respaldado por pruebas.
- Una exploración no es autoridad hasta incorporarse en una de esas
  superficies.
- El estado temporal y el próximo paso viven en el handoff vigente; no se
  duplican en informes acumulativos.

La documentación y las explicaciones se escriben en español de Chile. Código,
comandos e identificadores permanecen en inglés. Las fechas se expresan como
`AAAA-MM-DD`.
