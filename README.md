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

El [estado y plan de productos](docs/estado-y-plan-productos.md) fija el corte
vigente del 2026-09-14: contratos reconstruidos y admitidos, integración personal
pendiente y utilidad parcialmente demostrada. Conserva la evidencia, las
brechas y el plan por recorridos completos para Félix, único usuario y
desarrollador de este host.

La [propuesta anterior](docs/propuesta-refactorizacion-productos.md) conserva
el diagnóstico y los dictámenes de los lotes KORA, ingeniería, salud, GTD
general, compatibilidad, organización, proyecto, modelado y Diseño. Sus estados
de instalación corresponden a esos cortes históricos. La suite de maquinaria
y los casos sintéticos no certifican utilidad diferencial, eficacia clínica ni
validación de toda la biblioteca.

- [Guía de operación y comprobaciones](docs/operacion.md).
- [Instrucciones para trabajar en este repositorio](AGENTS.md).
- [Diseño de la maquinaria](docs/diseno.md).
- [Especificación de referencia](docs/kora-version-oro.md): contrato de destino;
  su existencia no certifica cumplimiento de todos los requisitos.
- Contratos efectivos de [Codex](docs/codex.md) y [Hermes](docs/hermes.md).
- Antecedentes de consulta: [reconstrucción](archive/reconstruction/migracion.md)
  y [plan de implementación concluido](docs/plan-implementacion-kora-oro.md).
