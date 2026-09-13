# scaffold-repo

Crea la entrada suficiente para trabajar en un espacio nuevo: repositorio,
biblioteca o cuaderno. Git es opcional según el encargo. Usa sólo los archivos
que necesita ese espacio:

- `README.md` orienta a Félix: qué es, para qué sirve y cómo usarlo.
- `AGENTS.md` reúne las instrucciones propias del repositorio para Codex y
  Hermes, que admiten este archivo como contexto de proyecto.
- `.gitignore` excluye secretos y residuos que realmente produce el proyecto.

Cada archivo añade lo propio de su función. Las instrucciones locales operan
dentro de la autoridad y precedencia del runtime; no repiten las instrucciones
generales ni prometen que ambos destinos descubran el contexto del mismo modo.
Git conserva la historia cerrada. `HANDOFF.md` sirve solo para trabajo material
que deba continuar después de una interrupción.

## Resolver el destino

Identifica el propósito, la ubicación y el tipo de trabajo: desarrollo,
conocimiento, cuaderno de rol o modelamiento. Infiérelos del encargo y del
directorio cuando haya evidencia suficiente; consulta solo una ambigüedad que
cambie materialmente la creación.

Antes de escribir, resuelve la raíz Git cuando exista y lee las instrucciones
aplicables. Distingue fuente, realización, instalación y archivo histórico.
Trabaja sobre la fuente autorizada. Un directorio generado o un perfil de
runtime requiere su procedimiento de autoría, no este scaffold.

Lee los archivos existentes y conserva sus cambios. Crea lo que falte dentro
del encargo; adapta entradas existentes solo si esa actualización está
autorizada. La presencia de un archivo de otro runtime no autoriza a borrarlo
ni obliga a reproducirlo en repositorios nuevos.

## Crear las entradas

Usa solo las plantillas que aporten al repositorio concreto:

| Salida | Referencia |
|---|---|
| `README.md` | `referencias/README.md` |
| `AGENTS.md` desarrollo | `referencias/agents-desarrollo.md` |
| `AGENTS.md` conocimiento | `referencias/agents-conocimiento.md` |
| `AGENTS.md` cuaderno de rol | `referencias/agents-cuaderno-rol.md` |
| `AGENTS.md` modelamiento | `referencias/agents-modelamiento.md` |
| `.gitignore` | `referencias/gitignore-base` |

Sustituye los placeholders y elimina comentarios guía y secciones que no
apliquen. Expresa los datos todavía desconocidos de forma útil, sin inventarlos.
`AGENTS.md` debe permitir ubicar la fuente, realizar el trabajo y comprobarlo:
incluye los comandos que existen y los límites propios del proyecto. Describe
la ausencia de comprobaciones automatizadas solo cuando afecte cómo verificar.

Conserva las exclusiones de secretos y respaldos; añade los residuos del
lenguaje y las herramientas efectivamente usados. Crea directorios adicionales
solo para contenido o procesos presentes. Las plantillas de modelamiento son
una referencia que se adapta a la herramienta y al formato del encargo.

## Continuidad y cierre

Si queda trabajo material que otra sesión debe retomar, mantén un único
`HANDOFF.md` en la raíz con el estado comprobado, pendiente y próxima acción.
Se actualiza mientras siga abierto y se retira al terminar. La creación de un
repositorio no requiere memorias, bitácoras o archivos de sesión paralelos.

Comprueba que no quedan placeholders ni instrucciones de herramientas ausentes
y que el diff contiene solo las entradas previstas. Si el encargo incluye
inicializar Git, hazlo cuando aún no exista; un commit o una publicación siguen
la autoridad vigente. Entrega los archivos creados y cualquier pendiente que
impida usar el repositorio.

Cuando una decisión dependa de la carga nativa de instrucciones, contrasta la
versión instalada y la documentación oficial de
[Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) o
[Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files).
