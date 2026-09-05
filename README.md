# KORA

Maquinaria personal de Félix Korvo para convertir fuentes en conocimiento útil,
autorar agentes y skills agnósticos, y realizarlos en **Codex y Hermes**.
Esta raíz contiene el núcleo, los métodos, las fuentes y las pruebas necesarias
para operarla y mantenerla. En el host de Félix vive en `/home/felix/kora-pneuma`;
la CLI toma como raíz el directorio donde está, sin depender de esa ruta fija.

En Codex, `$kora` activa su perspectiva en la conversación actual; su rol nativo
permite delegar una tarea explícita. En Hermes, KORA se usa desde el perfil
`kora`. La [guía de operación](products/kora/guia-rapida-pneuma/content.md)
explica cómo localizar fuentes, autorarlas, instalarlas y recuperar cambios.

Para empezar desde una copia del repositorio, en Linux con Python 3.12:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 kora_cli.py --help
```

Con Codex o Hermes ya disponibles, `install codex urn:kora:artefacto:kora` o
`install hermes urn:kora:artefacto:kora` instala KORA y las skills que necesita.
Son subcomandos de `python3 kora_cli.py`. La CLI también funciona sin modelo,
credenciales ni red; la conversación usa el runtime y proveedor configurados
por Félix. La [guía](products/kora/guia-rapida-pneuma/content.md) explica instalación,
traslado y recuperación.

Los productos se mantienen en `products/<namespace>/<name>/object.yaml` y su
archivo de contenido. El catálogo se deriva al operar. Edita la fuente resuelta;
las realizaciones nativas se actualizan desde ella.

- [Guía de operación y comprobaciones](products/kora/guia-rapida-pneuma/content.md).
- [Instrucciones para trabajar en este repositorio](AGENTS.md).
- [Diseño de la maquinaria](docs/diseno.md).
- Contratos efectivos de [Codex](docs/codex.md) y [Hermes](docs/hermes.md).
- [Antecedentes conservados](archive/reconstruction/migracion.md), de consulta opcional.
