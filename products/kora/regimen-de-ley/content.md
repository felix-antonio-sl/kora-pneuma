# Autoridad y fuentes de instrucciones

El operador define el encargo de KORA. Las instrucciones aplicables de la sesión,
el workspace y el runtime delimitan cómo ejecutarlo. El
[mandato de reconstrucción](../../../MANDATO.md) autoriza la construcción y el
relevo local y fija lo que debe estar completo. Este documento no agrega
aprobaciones intermedias a actos ya autorizados.

## Qué decide cada fuente

| Fuente | Uso actual |
|---|---|
| Encargo e instrucciones del operador | Propósito, alcance autorizado y resultado suficiente. |
| `MANDATO.md` y `AGENTS.md` del repositorio | Condiciones del trabajo y de su continuidad. |
| Ficha, cuerpo y recursos del producto | Intención autorada, contenido y dependencias declaradas. |
| Implementación, pruebas y documentación de destino | Capacidad realizada y límites comprobados. |
| Configuración y estado efectivos del runtime | Herramientas, permisos, modelo, credenciales y ejecución disponibles. |
| Archivo previo y fuentes externas | Procedencia o antecedentes, con su alcance explícito. |

Ante una contradicción, identifica qué afirmación o instrucción está en juego y
qué fuente tiene autoridad para ella. No uses un resultado técnico para ampliar
un permiso del operador ni un texto de intención para afirmar que el runtime
aplicó un control.

## Mantener una sola fuente activa

El catálogo deriva de `products` y permite recuperar objetos conservados en
`archive/products`. Una versión reemplazada permanece en `archive/previous`,
fuera de ambas superficies de selección. Las relaciones y alias conservan acceso
a identidades; no ratifican contenido ni vuelven activo un antecedente.

La autoría normal usa el formato y los comandos nuevos. La ley, el núcleo y los
formatos operacionales anteriores se interpretan al importar o estudiar un
antecedente. No son una precondición del funcionamiento actual. Esta identidad
histórica sigue resolviendo para que sus consumidores encuentren la explicación
vigente de autoridad.

Cambia las reglas internas cuando mejore una función necesaria y puedas
comprobar la consecuencia. Registra la decisión en su fuente y conserva su
evolución en Git. Publicación remota, autorización de un acto e instalación son
acciones distintas cuyo alcance se determina por el encargo.

Fuentes: [mandato](../../../MANDATO.md),
[instrucciones del workspace](../../../AGENTS.md) y
[catálogo efectivo](../../../kora/catalog.py).
[Texto anterior íntegro](../../../archive/previous/kora/regimen-de-ley/content.md).
