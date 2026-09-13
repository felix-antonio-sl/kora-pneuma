# Repo shaping checklist — agent-friendly

Disenar repos para que **agentes** puedan trabajar con minima friccion.
La estructura y las instrucciones ayudan a recuperar contexto. Aplica sólo
los criterios que tengan un consumidor y una consecuencia verificable; no
crees comandos, documentación o carpetas para llenar la tabla.

## Checklist

| Aspecto | Que verificar |
|---|---|
| Estructura obvia | Paths y documentación pertinente permiten localizar responsabilidades |
| Nombres claros | Carpetas y archivos nombran su funcion, no su tipo abstracto |
| Documentación suficiente | Las decisiones y límites necesarios están localizables, sin repetir manuales por módulo |
| CLIs para operaciones importantes | Ops repetibles disponibles como comando, no como ritual humano |
| Convenciones repetibles | Mismo patron en archivos hermanos: testing, naming, estructura interna |
| Ejemplos concretos | Las interfaces cuyo uso lo requiera tienen ejemplos suficientes |
| Acceso simple a logs/DB/deploy | Comandos directos, sin pasos manuales encadenados |
| Responsabilidades comprensibles | Dividir archivos cuando permita entender, cambiar o comprobar mejor una responsabilidad |
| Superficies operables (CLI > GUI-only) | La superficie permite realizar y comprobar la operación; una GUI puede ser adecuada |
| Auth/env correcto | Un ejemplo de configuracion de auth y variables de entorno |
| Operaciones repetibles con un comando | Las operaciones repetidas pertinentes tienen entradas claras, sin crear un wrapper sin función |
| AGENTS.md utilizable por Codex y Hermes | Instrucciones del repo: comandos, convenciones y condiciones relevantes |

## Heuristicas

- **Si un agente necesita exploracion extensa** para encontrar como hacer
  algo trivial, el repo no es agent-friendly.
- **Si los comandos importantes viven en docs humanos** (Notion, README
  largo) en vez de scripts/Makefile, el repo penaliza al agente.
- **Si la estructura de directorios refleja la org humana** (frontend-team,
  backend-team) y no la arquitectura, el agente se confunde.
- **Si los nombres de archivos son genericos** (`utils.ts`, `helpers.py`,
  `core/`), el agente pierde tiempo abriendo archivos para entender.

## Instrucciones en AGENTS.md

Un archivo agent-facing en la raiz del repo. Contiene:

- proposito del repo en 1-2 frases,
- comandos comunes (`build`, `test`, `lint`, `dev`, `deploy`),
- convenciones de naming y de archivos,
- estructura del codigo (que vive donde),
- gotchas conocidas (zonas fragiles),
- decisiones del encargo que requieren intervención del operador.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| Layout por organizacion humana | Estructura no refleja arquitectura | Reorganizar por dominio o subsistema |
| Docs solo en humano-friendly | Notion/Confluence sin equivalente in-repo | Dar acceso a la fuente canónica; copiar sólo cuando sea necesario y no duplique autoridad |
| Magic configs | Archivos con efectos no documentados | Comentar el porque, no solo el que |
| Responsabilidades mezcladas | Cambios independientes se interfieren | Separar cuando reduzca ese acoplamiento |
| Scripts shell sueltos sin doc | `deploy.sh` sin saber que hace | Header con proposito + uso |
