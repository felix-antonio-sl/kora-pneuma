# KORA

Maquinaria personal de Félix Korvo para convertir fuentes en conocimiento útil,
autorar agentes y skills agnósticos, y realizarlos en **Codex y Hermes**.
La única raíz de uso es `/home/felix/kora-pneuma`.

En Codex, `$kora` activa su perspectiva en la conversación actual; su rol nativo
permite delegar una tarea explícita. En Hermes, KORA se usa desde el perfil
`kora`. La [guía de operación](products/kora/guia-rapida-pneuma/content.md)
explica cómo localizar fuentes, autorarlas, instalarlas y recuperar cambios.

La interfaz también funciona sin una conversación:

```sh
python3 /home/felix/kora-pneuma/kora_cli.py --help
```

Los productos se mantienen en `products/<namespace>/<name>/object.yaml` y su
archivo de contenido. El catálogo se deriva al operar. Edita la fuente resuelta;
las realizaciones nativas se actualizan desde ella.

- [Guía de operación y comprobaciones](products/kora/guia-rapida-pneuma/content.md).
- [Instrucciones para trabajar en este repositorio](AGENTS.md).
- [Diseño de la maquinaria](docs/diseno.md).
- Contratos efectivos de [Codex](docs/codex.md) y [Hermes](docs/hermes.md).
- [Historia y evidencia de la reconstrucción del 2026-09-05](docs/migracion.md).

La historia de construcción también se conserva en `/home/felix/kora-rebuild`.
Las actualizaciones se realizan en esta raíz.
