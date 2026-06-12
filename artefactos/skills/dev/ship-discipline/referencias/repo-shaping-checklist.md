# Repo shaping checklist — agent-friendly

Disenar repos para que **agentes** puedan trabajar con minima friccion.
La ingenieria del repo **es** ingenieria de contexto.

## Checklist

| Aspecto | Que verificar |
|---|---|
| Estructura obvia | El layout se entiende leyendo solo paths; no requiere explicacion |
| Nombres claros | Carpetas y archivos nombran su funcion, no su tipo abstracto |
| Docs locales por subsistema | Cada modulo grande tiene README breve sobre proposito y limites |
| CLIs para operaciones importantes | Ops repetibles disponibles como comando, no como ritual humano |
| Convenciones repetibles | Mismo patron en archivos hermanos: testing, naming, estructura interna |
| Ejemplos concretos | Cada API publica tiene ejemplo minimo de uso |
| Acceso simple a logs/DB/deploy | Comandos directos, sin pasos manuales encadenados |
| Archivos no excesivamente grandes | Files >1KLOC se cuestionan; >2KLOC casi siempre dividir |
| Superficies operables (CLI > GUI-only) | Operaciones criticas accesibles sin GUI |
| Auth/env correcto | Un ejemplo de configuracion de auth y variables de entorno |
| Operaciones repetibles con un comando | Build, test, deploy, migrate accesibles como `make x` o equivalente |
| AGENTS.md o CLAUDE.md presente | Resumen agent-facing del repo: comandos, convenciones, gotchas |

## Heuristicas

- **Si un agente necesita exploracion extensa** para encontrar como hacer
  algo trivial, el repo no es agent-friendly.
- **Si los comandos importantes viven en docs humanos** (Notion, README
  largo) en vez de scripts/Makefile, el repo penaliza al agente.
- **Si la estructura de directorios refleja la org humana** (frontend-team,
  backend-team) y no la arquitectura, el agente se confunde.
- **Si los nombres de archivos son genericos** (`utils.ts`, `helpers.py`,
  `core/`), el agente pierde tiempo abriendo archivos para entender.

## Patron CLAUDE.md / AGENTS.md

Un archivo agent-facing en la raiz del repo. Contiene:

- proposito del repo en 1-2 frases,
- comandos comunes (`build`, `test`, `lint`, `dev`, `deploy`),
- convenciones de naming y de archivos,
- estructura del codigo (que vive donde),
- gotchas conocidas (zonas fragiles),
- como contactar al humano si hay decision irreducible.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Layout por organizacion humana | Estructura no refleja arquitectura | Reorganizar por dominio o subsistema |
| Docs solo en humano-friendly | Notion/Confluence sin equivalente in-repo | Llevar lo critico a `docs/` o AGENTS.md |
| Magic configs | Archivos con efectos no documentados | Comentar el porque, no solo el que |
| One huge file | 5KLOC en `index.ts` | Dividir por responsabilidad |
| Scripts shell sueltos sin doc | `deploy.sh` sin saber que hace | Header con proposito + uso |
