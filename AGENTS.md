# AGENTS.md

KORA es la maquinaria personal de Félix Korvo para transformar fuentes en
conocimiento útil, autorar agentes y skills y realizarlos en Codex y Hermes.
Esta raíz contiene su implementación, métodos, agentes, skills y pruebas. En
h289 se mantiene en `/home/felix/kora-pneuma`; puede operar desde otra ubicación.
El conocimiento de referencia vive en `/home/felix/kora-knowledge`, accesible
mediante el enlace `knowledge` o la opción `--knowledge-root`.

Lee el `README.md` actual y solo la documentación necesaria para el encargo.
El encargo vigente delimita la autoridad y el resultado. La historia archivada
sirve para investigar una decisión cuando haga falta; no agrega obligaciones
de reconstrucción ni requiere consultar otros repositorios o conversaciones.

## Fuente e interfaz

Agentes y skills se mantienen en `products/<namespace>/<name>/object.yaml` y su
archivo de contenido. La biblioteca separada contiene `inbox`, `drafts`,
`versions` y `references`: originales de entrada, borradores, versiones
conservadas y referencias estables a lo publicado. El catálogo se deriva al
operar. `requires` declara necesidades de realización o consulta; `relations`
conserva otros vínculos. Una cita documental no obliga a instalar su destino.

`create knowledge` prepara un borrador. `review` identifica el contenido concreto
y `approve --reviewed` publica esa revisión cuando Félix aprobó el contenido o
delegó explícitamente esa decisión. La autoridad para modificar la maquinaria
no aprueba conocimiento. Para actualizar una referencia, usa `revise`; conserva
disponible la versión anterior hasta publicar la nueva. No edites directamente
las versiones publicadas ni sus enlaces. Los conocimientos heredados se
conservan como `legacy`, sin inventarles una aprobación nueva.

`docs/operacion.md` es la guía vigente. Los originales archivados y las guías
anteriores sirven para investigar procedencia, sin gobernar la operación actual.
`artefactos/conocimiento` mantiene solo los enlaces de lectura necesarios para
consumidores existentes, dirigidos a las referencias de la biblioteca.

La interfaz es `python3 kora_cli.py --help`. `catalog.py` representa y resuelve;
`authoring.py` conserva y crea fuentes; `knowledge.py` conduce entrada, borrador
y publicación de referencias; `render_codex.py` y `render_hermes.py`
producen archivos nativos; `install.py` reconoce cambios y recupera operaciones;
`cli.py` conecta esos recorridos. Los instrumentos de la reconstrucción concluida
se conservan en `archive/reconstruction`, fuera del núcleo y de sus pruebas.

Consulta las capacidades contrastadas y sus fuentes oficiales en `docs/codex.md`
y `docs/hermes.md`. Verifica la versión instalada cuando una decisión dependa de
ella. Los únicos adaptadores y operaciones de runtime son Codex y Hermes.
No agregues soporte a destinos hipotéticos ni cambies instalaciones ajenas.

## Cambiar y comprobar

Actúa dentro de la autoridad del encargo y completa el menor cambio útil.
Preserva ediciones locales, recursos, identidades y relaciones necesarias.
Una reparación de maquinaria no autoriza a reescribir conocimiento de dominio.
Mantén secretos, datos sensibles, credenciales, memoria y estado personal fuera
de Git y de evidencia compartida. Los respaldos privados no son fuente activa.

Comprueba con `python3 kora_cli.py check`, las pruebas pertinentes de
`python3 -m unittest discover -s tests -v` y `git diff --check`.
Usa `--root` y `--knowledge-root` para corpus independientes y `--home` para
pruebas de instalación.
Distingue forma válida, comparación semántica, estado de instalación y conducta
observada. Los cambios nativos se realizan desde su fuente; el estado y la
recuperación se consultan con `status`, `recover` y `rollback`.

Puedes delegar subtareas acotadas con propiedad explícita de archivos y una sola
autoridad de integración. Conserva el trabajo ajeno. Usa ramas con prefijo
`fxai`, commits autocontenidos por intención y staging de paths exactos.
Publicar Git remotamente requiere autoridad específica del usuario.

Escribe documentación y explicaciones en español de Chile, fechas `AAAA-MM-DD`
y código e identificadores en inglés. Documenta solo lo necesario para operar,
comprobar o continuar. Usa un único `HANDOFF.md` temporal si se interrumpe trabajo
material; no mantengas registros paralelos del catálogo ni del estado instalado.
