# KORA

Maquinaria personal de Félix Korvo para convertir fuentes en conocimiento útil,
autorar agentes y skills agnósticos, y realizarlos en **Codex y Hermes**.
Esta raíz contiene el núcleo, los métodos, los agentes, las skills y las pruebas.
En h289 vive en `/home/felix/kora-pneuma`. La biblioteca central de conocimiento
vive por separado en `/home/felix/kora-knowledge`, accesible desde el enlace
`knowledge`. Ambos repositorios usan archivos legibles y Git.

Un conocimiento KORA es un artefacto de referencia. Los recursos entran a
`inbox`, la koraficación produce un borrador y la publicación aprobada lo deja
disponible por su identidad. Una revisión conserva la referencia anterior hasta
que se aprueba la nueva. Los conocimientos heredados mantienen su disponibilidad
como `legacy`, sin atribuirles una aprobación nueva de Félix.

En Codex, `$kora` activa su perspectiva en la conversación actual; se emite además un rol personalizado cuya invocación depende del contrato
efectivo de la sesión (véase el límite observado en `docs/codex.md`). En Hermes, KORA se usa desde el perfil
`kora`. La [guía de operación](docs/operacion.md) explica cómo ingresar recursos,
preparar y publicar conocimiento, autorar agentes y skills, instalarlos y recuperar
cambios.

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
por Félix. Mantén la biblioteca junto a esta raíz o selecciona otra ubicación con
`--knowledge-root RUTA`, antes del subcomando. `--root RUTA` selecciona otra raíz
de agentes y skills; por defecto se usa la del programa invocado.

Agentes y skills se mantienen en `products/<namespace>/<name>/object.yaml` y su
archivo de contenido. El conocimiento tiene sus borradores, versiones y
referencias en la biblioteca. El catálogo se deriva al operar; `list` y `resolve`
consultan referencias publicadas, sin exponer borradores como conocimiento
aprobado. Los agentes y skills leen esas referencias sin incorporar una copia.

La autoría de agentes y skills conserva candidatas y revisiones completas antes
de admitir una fuente. La instalación permite simular efectos con `--dry-run`,
aplicar un plan guardado y comparar el estado nativo con la fuente mediante
`status --compare-source`. Las pruebas de carga y conducta observan qué usa
efectivamente el runtime. `check` informa su alcance: un resultado verde no
acredita fidelidad del conocimiento, utilidad diferencial de un agente ni
conducta futura. Un recibo `current` compara la realización; el conocimiento
consultado por una referencia viva puede cambiar sin reinstalar el agente.

El saneamiento de la maquinaria tiene sus recorridos comprobados con casos
sintéticos; ese resultado no valida los contenidos, métodos o utilidad de los
productos. La [propuesta de reconstrucción](docs/propuesta-refactorizacion-productos.md)
reúne el diagnóstico, la arquitectura candidata, la migración y el goal preparado
para ejecutar esa etapa. El primer lote de KORA está admitido: autoría,
transformación, evaluación y realización, con siete referencias operacionales
revisadas. Sesiones nuevas acreditaron autoría y transformación operativas
mediante `$kora` en Codex y el SOUL de KORA en Hermes; ambas instalaciones
personales gestionadas están actualizadas. El rol delegado Codex no quedó
acreditado. El lote de ingeniería también está admitido e instalado en ambos
destinos: diez productos con sus especialidades accesibles, y cuatro casos
sintéticos por runtime que acreditan diagnóstico provisional, continuidad
autorizada, revisión vacía y no activación vecina. El lote sanitario incorpora
18 productos, incluidos los gemelos de Dirección Técnica HODOM y Jefatura de
Telemedicina, con seis referencias revisadas y siete casos sintéticos por
destino. Sus instalaciones están actualizadas; no se ejecutaron actos clínicos
ni institucionales. El lote GTD general también está admitido e instalado en ambos
destinos: `david-allen`, `gtd-flow` con sus cuatro referencias y
`memorizacion-espaciada` con sus reglas de formulación. Cinco casos sintéticos
por runtime en sesiones nuevas acreditaron claridad, retención con excepción,
espera como responsabilidad ajena y no activación vecina; los oráculos de
formato se reevaluaron posthoc sin repetir inferencia. Los tres accesos
especializados KORA se conservan como identidades propias en ambos destinos:
`agent-architect`, `autoria-de-persona` y `auditoria-exposicion-kora`, con su
caso de verificación cada uno; retirar y aliasar no redirige la identidad
nativa y no se afirma utilidad diferencial. Las seis instalaciones personales
quedaron `current` en ambos destinos, sin dependencia efectiva del servicio
excluido gtd-felix. El lote de organización también está admitido e instalado
en ambos destinos: `cell-design` (método), `consenso-deliberativo` (deliberación
con disenso preservado) y `allan-kelly` (entrada que compone el método sin
duplicarlo), con carga y conducta acreditadas en fixtures sintéticos —Hermes
Sol/high y Codex Sol sin esfuerzo declarado (casos previos con el default del
perfil)—, comparación de fuentes contra vigente y sin-producto, y Allan
provisional sin superioridad afirmada sobre Dori. Instalaciones personales
`current` sin cambios ni recuperación pendiente. Las dos especialidades de
proyecto quedaron admitidas e instaladas en Codex (su destino prometido, sin
ampliar a Hermes): `lineas-paralelas` (partición con ownership y convergencia,
entrega mínima suficiente) y `test-vivo-iterativo-opmkv` (auditoría in-vivo
con clasificación contra evidencia e informe ajeno intocable), con conducta
acreditada en fixtures sintéticos Codex Sol/high —sin browser vivo certificado
ni utilidad diferencial—. Instalación personal `current`, originales
preservados en fuentes. El lote de modelado quedó admitido e instalado en
ambos destinos: `modelamiento-opm`, `cat-thinking`, `mente-omega`,
`pensamiento-modelador`, `jointjs-open-source`, `ifml`, `opm-specialist` y
`dov-dori`, con conducta acreditada en fixtures sintéticos Sol/high en ambos
destinos y envoltura Hermes compacta que conserva identidades, paths,
condiciones y ruteo (SOUL Dori personal 65.223; presupuesto 65.280 comprobado
sólo con Sol/ventana 272.000, sin promesa universal). Instalaciones personales
`current` sin cambios ni recuperación pendiente. El lote de diseño quedó admitido
e instalado en ambos destinos: `diseno-producto-integrado` (método),
`design` (materialización SPEC_ONLY), `ux-design` (auditoría con criterio y
evidencia), `ux-research-design-ai` (agente: protocolo sin hallazgos inventados),
`steve-jobs` (agente: crítica con principios por nombre, recuperación
preservada), `director-diseno-producto` (agente: propuesta no probada como
pendiente) y `diseno-ui-clinica-web-movil` (datos sintéticos, excepción
documentada, phi-boundary), con conducta acreditada en fixtures sintéticos
Sol/high en ambos destinos (16/16; Hermes research con timeout de transporte
documentado) y 4 KB Jobs aprobados como lente consultable. Instalaciones
personales `current` sin cambios ni recuperación pendiente. La colección queda
cerrada; estos lotes no validan utilidad diferencial, eficacia clínica ni
biblioteca completa.

- [Guía de operación y comprobaciones](docs/operacion.md).
- [Instrucciones para trabajar en este repositorio](AGENTS.md).
- [Diseño de la maquinaria](docs/diseno.md).
- [Especificación de referencia](docs/kora-version-oro.md): contrato de destino;
  su existencia no certifica cumplimiento de todos los requisitos.
- Contratos efectivos de [Codex](docs/codex.md) y [Hermes](docs/hermes.md).
- Antecedentes de consulta: [reconstrucción](archive/reconstruction/migracion.md)
  y [plan de implementación concluido](docs/plan-implementacion-kora-oro.md).
