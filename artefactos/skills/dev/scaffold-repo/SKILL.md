---
urn: urn:dev:artefacto:scaffold-repo
nombre: scaffold-repo
version: 1.1.0
estado: activo
descripcion: "Andamia un repo nuevo en este host (Hetzner/Ubuntu) con su CLAUDE.md como SSOT, README.md y AGENTS.md como punteros, y .gitignore base. Úsala cuando el operador quiera crear, iniciar, andamiar o «scaffoldear» un repositorio, proyecto o cuaderno nuevo en ~/projects/ (o un corpus de conocimiento / cuaderno de rol), aunque no diga «skill» ni «scaffold»: «creemos un repo para X», «arranquemos el proyecto Y», «necesito un cuaderno para el rol Z», «inicializa el corpus W». Destila el patrón CLAUDE.md del host en tres arquetipos: desarrollo, conocimiento y cuaderno de rol. Instaura además la vigencia documental: un solo vigente por especie, versionado por fecha sin sobrescritura, y los previos a una papelera _archivo/ gitignorada."
fuente: "Autorada runtime-first en ~/.claude/skills/scaffold-repo/ el 2026-06-21 (SKILL.md sha256:8d91319442a4232185ece0b28505b8c2d62a47d5b5306b0939bae15bdd12dd2d; assets/ preservados verbatim); absorbida a fuente canónica pneuma el 2026-06-21. No proviene de la bestia. Normalización aplicada: assets/ → referencias/ (única fibra legal de skill, ley/2 §6); descripcion plegada a una sola línea (sobre cerrado, ley/2 §1); frontmatter agéntico completo (vector/sigma/arnes/forma). Cuerpo preservado salvo el reapunte de rutas assets/ → referencias/. v1.1.0 (2026-06-21): añade la política de vigencia documental (handoff único + series por fecha + papelera _archivo/ gitignorada); unifica y reescribe las reglas de handoff divergentes de las 3 plantillas (cuaderno-rol descartaba el previo; conocimiento acumulaba docs/handoffs; desarrollo usaba docs/archive versionado) hacia _archivo/; gitignore-base suma _archivo/."
autor: FS
creado: 2026-06-21
lang: es
tags: [scaffold, repo, claude-md, ssot, host-conventions, bootstrap, vigencia-documental, archivo]
vector: [2, 0, 2, 0, 1]
sigma: [1, 1, 2, 1, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Write, Bash]
targets: [claude-code]
estados: [resolver-parametros, cargar-plantilla, escribir-satelites, cerrar]
---

# scaffold-repo

Crea el esqueleto documental mínimo de un repo nuevo conforme a las convenciones
del host: **`CLAUDE.md` es la única fuente de verdad (SSOT) del repo**; `README.md`
y `AGENTS.md` solo redirigen a él. Esto materializa el principio de delegación del
host (`~/CLAUDE.md`): "antes de operar en un subsistema, leer su propio CLAUDE.md"
— que solo es confiable si *todo* repo nace con uno.

## Cuándo NO aplicar

- El repo es un **workspace de flota OpenClaw** (`~/openclaw-fleet/*`): ahí
  `AGENTS.md` es una **definición de agente**, no un puntero. No lo sobreescribas.
- Ya existe un `CLAUDE.md` en el destino: no lo pises; ofrece auditarlo/mejorarlo
  con `claude-md-management` en su lugar.

## Flujo

### 1. Resolver los tres parámetros

Antes de escribir nada, fija:

- **`nombre`** — kebab-case, sin tildes. Será el directorio.
- **`ubicación`** — por la disciplina del host, casi siempre `~/projects/{{nombre}}/`.
  Excepciones que vive en `~` directamente: corpus tipo KORA. Si hay duda, `~/projects/`.
- **`arquetipo`** — uno de:
  - **`desarrollo`** — tiene código: build, tests, dependencias, ADRs. (ej. opmodel, hsc)
  - **`conocimiento`** — corpus de artefactos `.md` para consumo/producción gobernada. (ej. kora)
  - **`cuaderno-rol`** — no hay código; un rol produce/decide/firma/presenta. Maneja
    handoff vivo y referencia sistemas vecinos. (ej. hd-dt)

Si el operador no lo dijo y no es inequívoco por contexto, **pregunta el arquetipo**
— es la decisión que más cambia la plantilla. El nombre y propósito suelen inferirse
de la conversación; confírmalos en una línea, no interrogues de más.

### 2. Cargar y rellenar la plantilla del arquetipo

Lee la plantilla correspondiente de `referencias/` y rellénala con juicio, no
mecánicamente — cada sección pide contenido real, no un eco del placeholder:

| arquetipo | plantilla |
|---|---|
| `desarrollo` | `referencias/claude-md-desarrollo.md` |
| `conocimiento` | `referencias/claude-md-conocimiento.md` |
| `cuaderno-rol` | `referencias/claude-md-cuaderno-rol.md` |

Reglas al rellenar:

- Sustituye cada `{{placeholder}}`. Si no tienes el dato (p. ej. comandos de build
  aún inexistentes), pon un marcador honesto (`{{pendiente: definir build}}`) en vez
  de inventar.
- **Borra** los comentarios-guía `<!-- ... -->` una vez aplicados.
- **Borra secciones enteras que no apliquen todavía** — el scaffold es un piso
  mínimo que crece, no un formulario que se llena completo. Un repo recién nacido
  con tres secciones bien puestas vale más que diez vacías.
- No copies el largo de los ejemplares maduros del host (hd-dt tiene 174 líneas
  *porque lleva meses de operación*). El recién nacido arranca corto.

### 3. Escribir los archivos satélite

Desde `referencias/`, instancia tal cual (sustituyendo `{{nombre}}` y `{{una-línea}}`):

- `README.md` ← `referencias/README.md` — puntero de una línea a CLAUDE.md.
- `AGENTS.md` ← `referencias/AGENTS.md` — puntero idéntico (decisión del operador: puntero,
  no symlink — robusto ante tarballs y clones).
- `.gitignore` ← `referencias/gitignore-base`, y **añade** las líneas del runtime real
  (Node → `node_modules/ dist/`; Python → `.venv/ __pycache__/`; Go → `/bin/`).
  Las líneas `*.tar.gz` (backups del host) y `_archivo/` (papelera de no-vigentes,
  §Vigencia documental) son invariantes del host y no se quitan.

### 4. Cerrar

- Crea el directorio y escribe los cuatro archivos.
- Si es repo versionable (`desarrollo`/`conocimiento`/`cuaderno-rol` que llevará git),
  ofrece `git init` + primer commit. No lo des por hecho: pregunta antes de inicializar.
- Reporta en una línea qué creaste y dónde, y nombra la **primera sección que el
  operador debería terminar de llenar** (normalmente "Qué es" y el mapa).

## Vigencia documental

Todo repo andamiado nace con una papelera `_archivo/` gitignorada y con la sección
**Vigencia documental** en su `CLAUDE.md` (las plantillas ya la traen). Rige cualquier
documento operativo que evolucione —el handoff, y cada serie de informe, auditoría,
acta o documento— bajo tres invariantes:

1. **Un solo vigente por especie.** A lo más un handoff vigente en todo el repo; a lo
   más una versión vigente de cada serie. La *especie* es el slug del nombre sin la
   fecha (`handoff`, `auditoria-<tema>`, `informe-<tema>`).
2. **Versionado por fecha, inmutable.** Cada versión es un documento nuevo
   `<especie>-AAAA-MM-DD.md` (mismo día → sufijo `-2`). **Nunca** se edita in-place ni
   se sobrescribe un archivo ya escrito; el vigente es el de **fecha máxima** de su
   especie.
3. **El previo se archiva, no se pierde.** Al publicar una versión nueva, **mueve** la
   anterior a `_archivo/` (`mv` / `git mv`) *antes* de escribir la nueva. `_archivo/`
   es gitignorado: historia local, no SSOT. El árbol versionado contiene solo lo vigente.

**Protocolo de actualización** (handoff o serie), en este orden: (1) lee el vigente
previo — la nueva versión *es* su actualización; (2) mueve el previo a `_archivo/`; (3)
escribe `<especie>-<fecha-de-hoy>.md`. Si tras andamiar el operador pide "actualiza el
handoff" o "nueva auditoría", aplica este protocolo: jamás dejes dos vigentes de la
misma especie en el árbol versionado ni sobrescribas el previo.

## Por qué esta forma y no otra

El host ya impone (`~/CLAUDE.md`, memoria del operador): docs en **es-CL**, código
e identificadores en **inglés**; **CLAUDE.md = SSOT por repo**; **`*.tar.gz` fuera de
git**; **fechas ISO absolutas**. Las plantillas no reinventan esas reglas: las heredan
con una línea (`Hereda de ~/CLAUDE.md`) para no duplicar la ley del host en cada repo.
Lo que cada plantilla añade es solo lo *propio del arquetipo*.
