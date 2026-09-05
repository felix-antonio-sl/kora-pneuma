# Modelo de fuente y realización KORA

El catálogo relaciona identidades estables con productos conservados en archivos.
Se deriva al operar; cada producto tiene una ficha `object.yaml`, un contenido
legible y los recursos necesarios. Ficha mínima de conocimiento:

```yaml
id: urn:kora:kb:cat-kora-kernel
kind: knowledge
name: cat-kora-kernel
description: Modelo de productos, dependencias y realizaciones de KORA.
content: content.md
```

`id` conserva identidad aunque cambie la ubicación. `kind` distingue `knowledge`,
`skill` y `agent`; `name` determina el nombre nativo al realizar. `content` apunta
a un archivo del producto. Los recursos conservan rutas relativas y modos.
Agentes y skills declaran en `targets` sus destinos, Codex y/o Hermes.
`provenance` conserva procedencia y fuentes recuperables.

## Actividad e identidad

Los productos activos viven bajo `products`. `archive/products` conserva objetos
resolubles sin habilitar su realización; `archive/previous` guarda versiones
reemplazadas fuera de ambos catálogos. Un alias de `aliases.yaml` conduce a una
identidad sin modificar su actividad. Nombres documentales iguales solo son un
conflicto cuando ocupan el mismo destino físico con contenido distinto.

## Dependencias y realización

`requires` expresa acceso necesario. La realización recorre su cierre y comprueba
identidad, actividad y destino. El conocimiento se expone mediante rutas resueltas;
las skills se realizan en la superficie correspondiente. El recorrido evita
repetir identidades y no declara una secuencia de ejecución.

`relations` conserva otros vínculos tipados sin provocar instalación. Citar,
reemplazar o mencionar colaboración no implementa una llamada a otro agente.
En Hermes, requerir un agente como dependencia de realización produce un error:
el perfil no puede realizar esa llamada por declararla.

El realizador deriva un mapa de rutas, bytes y modos. El instalador lo reconcilia
con los archivos que administra y el estado real del home. La
[semántica operacional](../cat-kora-semantica-operacional/content.md) explica qué
puede concluirse de esos cambios; el [diseño](../../../docs/diseno.md) explica las
decisiones de implementación y la [guía](../guia-rapida-pneuma/content.md) su uso.

Implementación: [catálogo](../../../kora/catalog.py) y realizadores de
[Codex](../../../kora/render_codex.py) y [Hermes](../../../kora/render_hermes.py).
[Modelo anterior conservado](../../../archive/previous/kora/cat-kora-kernel/content.md).
