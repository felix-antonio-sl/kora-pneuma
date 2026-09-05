# AGENTS.md

KORA es la maquinaria personal de Félix Korvo para transformar fuentes en
conocimiento útil, autorar agentes y skills y realizarlos en Codex y Hermes.
La única raíz de uso es `/home/felix/kora-pneuma`. El repositorio
`kora-rebuild` conserva la historia de construcción y no es otra fuente activa.

Lee el `README.md` actual y solo la documentación necesaria para el encargo.
`MANDATO.md` conserva la autorización y los criterios de la reconstrucción del
2026-09-05. Mientras su Goal nativo siga activo, completa esos criterios; después
no lo recrees ni conviertas cada tarea nueva en otra reconstrucción.

## Fuente e interfaz

Los productos se mantienen en `products/<namespace>/<name>/object.yaml` y su
archivo de contenido. El catálogo se deriva al operar. `requires` declara
necesidades de realización; `relations` conserva otros vínculos. Los originales
archivados y la historia sirven para investigar procedencia, sin gobernar la
operación actual. `artefactos/conocimiento` contiene solo enlaces de lectura
necesarios para consumidores existentes; edita la fuente a la que resuelven.

La interfaz es `python3 kora_cli.py --help`. `catalog.py` representa y resuelve;
`authoring.py` conserva y publica fuentes; `render_codex.py` y `render_hermes.py`
producen archivos nativos; `install.py` reconoce cambios y recupera operaciones;
`cli.py` conecta esos recorridos. El importador y su auditoría leen formatos
anteriores únicamente para preservar y comprobar originales.

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
Usa `--root` para corpus independientes y `--home` para pruebas de instalación.
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
