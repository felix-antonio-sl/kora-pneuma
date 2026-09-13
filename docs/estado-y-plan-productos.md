# Productos KORA: estado y dirección

Fecha de corte: 2026-09-14. Fuente gobernante: encargo de Félix de fijar y
publicar una línea de estado, repensar la reconstrucción y proponer su ejecución
con `steipete` y `cat-thinking`, para un usuario y desarrollador en un host.
La [especificación confirmada](kora-version-oro.md) conserva los requisitos;
la [guía](operacion.md), la operación; este documento reúne el corte y el plan
de productos. La [propuesta anterior](propuesta-refactorizacion-productos.md)
conserva diagnóstico y evidencias por lote, sin gobernar el siguiente paso.

## Línea de estado publicada

**Contratos reconstruidos y admitidos, maquinaria comprobada, conducta sintética
acotada; integración personal incompleta y mejora de utilidad parcialmente
demostrada.** No corresponde declarar terminada la misión de reconstruir
mejorando los productos, ni volver a empezar su autoría.

El corte de fuentes es `a494e9c` en pneuma/master y `9af3696` en
knowledge/main. Los commits `f827636` y `03d4a5f` añaden a Git la historia ya
existente de seis productos; no cambian las fuentes activas del corte.

| Parte | Hecho comprobado o antecedente identificado | Límite / pendiente |
|---|---|---|
| Colección | 61 fuentes activas: 16 agentes y 45 skills. 58 declaran ambos destinos; 3 sólo Codex. | Cantidad descriptiva, sin cuota de reducción. `codex-route` se conserva; los otros 60 están integrados en lotes de reconstrucción. |
| Lotes | KORA operativo, ingeniería, salud, GTD general, compatibilidad, organización, especialidades de proyecto, modelado y Diseño están admitidos y confirmados en Git. Diseño cerró en `a494e9c`. | Admisión y documentación de ensayos no equivalen a utilidad personal demostrada. |
| Maquinaria | `check`: 523 activos, 18 archivados, 0 incidencias. Suite ejecutada en este corte: 251 pruebas, OK. | No acredita fidelidad de toda la biblioteca, carga de todos los cuerpos o utilidad. |
| Codex personal | 61 instancias gestionadas en alcance: fuente y dependencias `current`. | Estado material; no es observación de sesiones personales. |
| Hermes personal | 62 instancias en alcance: 58 productos y 4 instancias adicionales de skills en perfiles. 29 `current`; 33 con fuente cambiada, de las cuales 14 también tienen dependencias cambiadas. | Falta reconciliar. No hay cambios nativos detectados ni recuperación pendiente. La cifra anterior de 40 ha quedado superada. |
| Conservación | Se incorporan candidatas admitidas y 12 versiones de los seis productos GTD/compatibilidad. Candidata, fuente activa y revisión registrada coinciden en los seis. | Se verificaron estas versiones con el verificador nativo; no se auditó toda la historia ni se atribuye aprobación nueva. |
| Biblioteca | Sigue en `9af3696`; incluye cuatro referencias Jobs publicadas y revisiones anteriores conservadas. | El corpus general heredado conserva su estatus. No se declara reconstruido, íntegramente revisado ni optimizado en tokens. |
| Git | El corte de fuentes estaba publicado y en paridad 0/0 tras fetch. La línea de estado y conservación se publica con este incremento. | Los cambios locales archivados OpenClaw y material privado en knowledge quedan fuera; `.hermes/` local se conserva. Paridad Git no implica igualdad del workspace completo con el remoto. |

Las seis historias son `fxsl/{david-allen,gtd-flow,memorizacion-espaciada}`,
`dev/agent-architect` y `kora/{autoria-de-persona,auditoria-exposicion-kora}`.
Se conservaron `product`, `state.yaml` y las versiones publicables. Los
directorios `displaced-*` permanecen locales e ignorados según la política
existente; no son una fuente operativa nueva.

### Qué evidencia tiene cada afirmación

| Dimensión | Estado defendible |
|---|---|
| Integridad mecánica | PASS en el catálogo actual y 251 pruebas de maquinaria; verificación focal de las 12 versiones preservadas. |
| Fidelidad semántica | Revisiones y correcciones documentadas por lote. Hay tensiones focales aún examinables; no se releyeron todos los cuerpos para este corte. |
| Carga nativa | Evidencia histórica de sesiones nuevas sobre casos y configuraciones concretas. KORA mediante skill directa Codex y SOUL Hermes; rol personalizado KORA no acreditado en su campaña. Dori Codex sólo lectura parcial observada; Hermes con margen estrecho bajo Sol/272K. |
| Conducta | Casos sintéticos de los lotes documentados. Diseño registra 16/16, pero `SPEC_ONLY` y errores fundados ante contexto insuficiente no acreditan todo el recorrido positivo de diseño y materialización. No se repitió inferencia en este corte. |
| Utilidad | Correcciones concretas y capacidades conservadas. Comparación de esfuerzo, errores, resultado y costo frente a alternativas simples mayormente pendiente; no equivale a inutilidad demostrada. |
| Efectos | Fuentes admitidas y publicadas; instalaciones focales previas. El estado actual identifica 33 realizaciones Hermes pendientes. No se realizaron actos clínicos, institucionales ni envíos. |

La cobertura se apoya en los dictámenes por lote de la propuesta anterior y en
la ejecución mecánica de este corte. Los recibos temporales son evidencia
auxiliar: antes de reutilizar una afirmación decisiva se comprueba que existan y
correspondan al caso, revisiones y entorno. Si faltan, se declara la limitación;
no se reconstruyen logs ni se repiten campañas enteras para llenar un archivo.

### Reproducir y mantener el corte

Usar `python3 kora_cli.py check`, `python3 -m unittest discover -s tests -v`
y `git diff --check`. Derivar productos desde `products/*/*/object.yaml`,
seleccionar sus identidades con `status --compare-source --id URN` repetible,
excluyendo `gtd-felix` y `gtd-operations`, y resumir `source_comparison` por
destino, perfil y estado. Las instancias adicionales son `ship-discipline` y
`hermes-agent-specialist` en los perfiles `hospitalista` y `urgencia`.
No publicar recibos completos del home, credenciales o respaldos privados.

Esta tabla es un **corte fechado**, no un inventario manual que deba acompañar
cada instalación. El estado vivo se deriva por CLI. Sólo se actualiza el
dictamen cuando cambie una conclusión material; Git conserva el corte anterior.

## Decisiones del corte

1. Conservar la colección admitida y su historia como punto de partida.
2. Corregir la declaración prematura de cierre. Instalación actualizada,
   conducta acotada y utilidad comparada son afirmaciones diferentes.
3. Mantener el núcleo, la biblioteca separada, las fuentes agnósticas y los dos
   adaptadores. No hay evidencia que justifique una nueva plataforma.
4. La reconciliación personal es el primer incremento del plan posterior;
   este corte no cambia instalaciones para hacer que la fotografía salga verde.
5. `gtd-felix`/`gtd-operations`, sus dependencias protegidas, los espacios
   institucionales y los datos privados conservan las exclusiones del encargo.
   Un solo usuario no elimina errores, interrupciones o procesos concurrentes;
   sí elimina la necesidad de diseñar tenants, roles empresariales o servicios
   de coordinación sin consumidor.
