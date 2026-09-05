# Autorar agentes y skills con evidencia proporcionada

Una fuente agnóstica permite comprender qué trabajo realiza el producto, cuándo
usarlo, qué necesita y cómo reconocer un resultado suficiente. El
[modelo del núcleo](../cat-kora-kernel/content.md) mantiene esa fuente y sus
relaciones; la realización concreta depende de Codex o Hermes.

## Elegir y expresar el producto

Usa una skill para un procedimiento reutilizable dentro de una sesión. Usa un
agente para una perspectiva y una conducta estables seleccionables como
identidad. Mantén conocimiento separado cuando tenga utilidad propia o requiera
recuperación directa.

Escribe un cuerpo que permita actuar: propósito, entradas necesarias, acciones,
resultado y respuesta ante una excepción o un dato ausente. Da instrucciones
concretas para los límites materiales del encargo. La personalidad se expresa
en decisiones y comunicación observables; un adjetivo no sustituye una conducta.
Ajusta el detalle y reutiliza recursos que ya tengan una fuente suficiente.

La ficha declara `id`, `kind`, `name`, `description`, `content` y destinos
admitidos. Incluye en `requires` solo acceso indispensable y en `relations`
vínculos informativos o de colaboración. Una llamada a otro agente requiere
una superficie real de ejecución: una relación o un nombre no la implementa.

## Decidir diferencias de destino

En Codex, KORA realiza el agente como TOML nativo y también una skill para cargar
su perspectiva en la sesión actual. Esa activación no crea una sesión hija ni
cambia permisos. La delegación usa el tipo nativo. Los campos del TOML siguen la
[configuración oficial de agentes](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents);
la realización KORA está en [el adaptador](../../../kora/render_codex.py).

En Hermes, KORA realiza el agente como perfil con `SOUL.md`, manifiesto y skills
requeridas; una dependencia de otro agente no produce una llamada entre perfiles.
La [distribución oficial de perfiles](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)
informa su forma; [el adaptador](../../../kora/render_hermes.py) y
[su contraste local](../../../docs/hermes.md) explican la realización y la
conservación del estado del operador.

Las skills usan [Agent Skills](https://agentskills.io/specification), con
instrucciones y recursos. La descripción debe ayudar a elegirlas ante la
necesidad correcta. Un campo de herramientas o texto restrictivo no demuestra
que el runtime imponga permisos. Modelo, autenticación y opciones efectivas se
comprueban en ese entorno cuando cambian el resultado esperado.

## Comprobar la afirmación que importa

| Afirmación | Evidencia pertinente |
|---|---|
| La fuente expresa el encargo | Lectura contra propósito, entradas, condiciones, excepciones y límites. |
| La realización conserva contenido necesario | Comparación de cuerpo, recursos y dependencias en la forma nativa. |
| El runtime encuentra y carga el producto | Descubrimiento y carga observados en el destino. |
| El producto actúa como se espera | Caso representativo, una excepción y una incertidumbre pertinentes. |
| La actualización conserva trabajo y permite recuperación | Cambios locales y un fallo relevante ejercitados con contenido observable después. |

Elige comprobaciones por la consecuencia de equivocarte. Conserva el insumo,
la observación suficiente y sus límites sin guardar secretos ni datos personales.
Un caso observado sustenta ese recorrido; no demuestra conducta universal,
equivalencia entre runtimes o aceptación del usuario. Una pérdida de capacidad
se resuelve o declara con su efecto concreto, sin sustituirla por una promesa
del archivo.

Fuentes: [mandato](../../../MANDATO.md),
[diseño implementado](../../../docs/diseno.md) y contratos de
[Codex](../../../docs/codex.md) y [Hermes](../../../docs/hermes.md).
[Contrato anterior con sus relaciones](../../../archive/previous/kora/cat-contrato-ingenieria-agentica/content.md).
