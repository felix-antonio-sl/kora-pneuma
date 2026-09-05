# Modelo operativo del núcleo KORA

El núcleo relaciona productos autorados con archivos utilizables en Codex y
Hermes. Su representación actual es un catálogo derivado de directorios, un
recorrido de dependencias y realizadores que producen archivos. Se conserva la
identidad histórica de este conocimiento; las formulaciones anteriores permanecen
en su [fuente previa](../../../archive/previous/kora/cat-kora-kernel/content.md).

## Objeto fuente

Cada producto tiene una ficha `object.yaml`, un archivo de contenido y los
recursos necesarios. Esta es una ficha mínima de conocimiento:

```yaml
id: urn:kora:kb:cat-kora-kernel
kind: knowledge
name: cat-kora-kernel
description: Modelo de productos, dependencias y realizaciones de KORA.
content: content.md
```

`id` conserva identidad aunque cambie la ubicación. `kind` distingue conocimiento,
skill y agente. `name` determina el nombre nativo cuando hay realización. El
archivo de `content` pertenece al directorio del producto; los recursos conservan
rutas relativas y modos. Dos identidades pueden compartir nombre documental,
pero no ocupar el mismo archivo nativo con contenido diferente.

Los activos viven bajo `products`. `archive/products` permite resolver objetos
conservados sin habilitar su realización. `archive/previous` conserva versiones
reemplazadas fuera de ambos catálogos. Un alias de `aliases.yaml` lleva a una
identidad sin modificar su actividad.

## Dependencias y relaciones

`requires` expresa acceso necesario. Al realizar un producto se recorre su
cierre de dependencias, comprobando identidad, actividad y destino admitido.
El conocimiento permanece en la fuente y se expone mediante una ruta comprobada.
Las skills requeridas se realizan en la superficie correspondiente. El recorrido
evita repetir identidades; la lista no describe por sí misma una secuencia de
ejecución.

`relations` conserva vínculos tipados que no provocan instalación. Una cita,
un reemplazo histórico o una colaboración mencionada no equivale a llamar un
agente. En Hermes, requerir un agente como dependencia de realización produce
un error: el perfil no realiza esa llamada por declararla.

## De la fuente al uso

El realizador transforma el producto y sus dependencias en un mapa de rutas,
bytes y modos. La CLI comprueba colisiones y cambios de fuente antes de entregar
el plan. El instalador reconcilia ese plan con lo que administra en el home del
operador y conserva un estado de recuperación privado.

Identidades, rutas y huellas de contenido relacionan la fuente, su realización
y lo instalado. Permiten detectar diferencias materiales; no demuestran
equivalencia conductual entre modelos ni que se leyó cada recurso. Atribuye cada
propiedad al componente que la implementa y al alcance de su evidencia.

Fuentes locales: [catalog.py](../../../kora/catalog.py),
[cli.py](../../../kora/cli.py), [realizador Codex](../../../kora/render_codex.py)
y [realizador Hermes](../../../kora/render_hermes.py). La
[semántica operacional](../cat-kora-semantica-operacional/content.md) explica
efectos y fallos de los comandos.
