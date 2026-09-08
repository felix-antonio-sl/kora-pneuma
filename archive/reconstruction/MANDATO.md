# Reconstrucción completa de la maquinaria KORA

## Autoridad y continuidad

El 2026-09-05 Félix Korvo autorizó a la tarea de origen y a su siguiente tarea a
crear el repositorio y ejecutar autónomamente la reconstrucción. Solicitó que la
nueva tarea use **`gpt-6-astra` con esfuerzo `max`**. El encargo se ejecuta como un
Goal nativo durable, sin presupuesto de tokens impuesto. No es una solicitud de
otra evaluación ni de una propuesta pendiente de aprobación.

La autorización comprende las decisiones de diseño, implementación, reglas
internas, migración, pruebas, adaptación de los artefactos de maquinaria,
instalaciones KORA de Codex y Hermes, commits e integración locales necesarios
para el resultado. Incluye delegación acotada con integración a cargo de esta
tarea. No requiere confirmaciones intermedias para esos actos.

No incluye publicar Git remotamente, borrar instalaciones ajenas de otros
runtimes, modificar sus servicios ni destruir estado personal. Si falta una
capacidad externa imprescindible, identifica la acción concreta y el bloqueo;
continúa todo el trabajo independiente que sí puedas completar.

## Finalidad y destinatario

KORA pertenece a **Félix Korvo y sirve a Félix Korvo**, único usuario y operador
en un host seguro. Su valor es reducir el esfuerzo de obtener, mantener y usar
conocimiento, agentes y skills que le resulten útiles. La maquinaria debe producir
ese valor con menos trabajo de mantenimiento y carga cognitiva.

Separa la maquinaria de sus productos. La maquinaria comprende las reglas,
formatos, herramientas, procesos y artefactos que permiten producir, mantener y
realizar los productos. Los productos comprenden conocimiento, agentes y skills
de uso. Un archivo con aspecto de producto puede formar parte de la maquinaria
si su función es autorar, auditar o gobernar KORA; también debe reconstruirse.

## Funciones que deben quedar completas

1. **Koraficación:** transformar fuentes en conocimiento útil, verificable y
   recuperable, conservando procedencia, alcance, condiciones, excepciones,
   incertidumbre y relaciones relevantes. La compresión está subordinada a la
   fidelidad y a la utilidad. Separar datos o fuentes técnicas externas cuando
   representarlos como prosa destruya su función.
2. **Autoría agnóstica de agentes y skills:** mantener una fuente de intención,
   conducta esperada, conocimiento y capacidades reutilizables. Hacer explícitas
   solo las diferencias de destino que cambian realmente la realización. No
   prometer comportamiento, portabilidad ni enforcement por la forma del archivo.
3. **Realización y mantenimiento en Codex y Hermes:** producir formas nativas,
   instalarlas, actualizarlas, retirarlas y recuperar un estado funcional ante
   fallos, sin perder ediciones ni estado ajeno. La fuente y lo instalado deben
   poder relacionarse y diagnosticarse sin inventarios mantenidos a mano.

Los únicos destinos son **Codex y Hermes**. Se eliminan de la maquinaria activa
los adaptadores, obligaciones y operaciones para Claude Code, OpenClaw, OpenCode
y cualquier otro runtime. Su aparición en historia o fuentes no exige borrarla.
La fuente agnóstica no se convierte en una plataforma para destinos hipotéticos.

## Qué significa reconstruir desde cero

El área de construcción es `/home/felix/kora-rebuild`, con una raíz Git nueva.
`/home/felix/kora-pneuma` se estudia como fuente de productos, historia, usos y
fallos; permanece sin modificaciones durante la construcción independiente.
No se clona su implementación ni se importa su historial como base del diseño ni
se copian `kora.py`, la ley, serializadores o esquemas para empezar.

La arquitectura, el núcleo y las reglas operacionales nacen de las funciones
anteriores y de las capacidades nativas actuales. Ningún concepto heredado se
preserva solo por existir. Un importador puede entender los formatos anteriores;
la operación normal nueva no debe depender del núcleo ni de la ley anteriores.
Las pruebas antiguas sirven para investigar intenciones y fallos, sin convertirse
automáticamente en requisitos del nuevo sistema.

La prueba de independencia exige operar la nueva maquinaria sin acceso al núcleo
ni a la ley anteriores: koraficar una fuente, autorar un skill y un agente
agnósticos, realizarlos según sus capacidades en Codex y Hermes, actualizarlos y
recuperarse de un fallo. Implementar en un directorio nuevo sin satisfacer esa
independencia sería insuficiente.

## Investigación y criterio de diseño

Estudia en profundidad la documentación oficial web vigente al decidir cada
integración y contrástala con versiones, esquemas, código instalado y pruebas
reales. Parte de estos sitios y sigue sus enlaces canónicos actuales:

- Codex: <https://developers.openai.com/codex/> y
  <https://learn.chatgpt.com/docs/>; skills, instrucciones, agentes/subagentes,
  configuración y superficies nativas necesarias para esta maquinaria.
- Hermes: <https://hermes-agent.nousresearch.com/docs/>; skills, contextos,
  perfiles, distribuciones, configuración y demás superficies que correspondan.
- Formato de skills cuando corresponda: <https://agentskills.io/specification>.

Identifica la fecha y versión pertinentes sin confundir la documentación más
reciente con la capacidad ya instalada. No agregues compatibilidad especulativa.

Aplica un criterio exigente: cada regla, campo, documento, módulo, prueba o paso
debe tener un consumidor y un efecto útil actual. Conserva controles concretos
de fidelidad, actualización, reconocimiento de cambios y recuperación. Rechaza
ceremonias de aprobación, duplicación de fuentes, complejidad institucional para
un único usuario, generalización prematura y remiendos convertidos en doctrina.

Revisa críticamente tanto decisiones humanas como de agentes: inercia, sesgo de
confirmación, costo hundido, complacencia, sustitución de resultados por conteos,
autovalidación de formas y reglas nacidas de incidentes sin necesidad vigente.
Sustenta observaciones con evidencia; no atribuyas estados mentales como hechos.
Evita también el sesgo de borrar por borrar: una reducción que pierda una función
necesaria fracasa aunque produzca menos líneas.

## Migración, relevo y término

Antes de migrar, inspecciona el filesystem vivo y el estado Git, incluidos cambios
no confirmados, archivos no seguidos, enlaces y consumidores efectivos. Conserva
una base recuperable. No asumas que HEAD contiene todo el trabajo de Félix ni que
los inventarios históricos siguen vigentes.

Migra el corpus completo que deba conservarse, manteniendo contenido útil,
procedencia, identidades/referencias necesarias y relaciones. No autoriza reescribir
arbitrariamente conocimiento de dominio. Resuelve explícitamente las pérdidas o
incompatibilidades; el silencio y el descarte masivo no constituyen migración.
Reconstruye los artefactos que forman parte de la maquinaria para que enseñen y
operen el sistema nuevo. Actualiza sus consumidores reales.

Al validar la construcción independiente, realiza el relevo local en
`/home/felix/kora-pneuma`, conservando su historia Git y el trabajo concurrente.
Integra la nueva maquinaria y los productos migrados por cambios semánticos
verificables. Conserva reversibilidad hasta probar el relevo. El repositorio de
construcción queda como historia de origen, sin una segunda autoridad activa.

El Goal termina únicamente cuando:

- Las tres funciones operan de extremo a extremo y se demuestra independencia.
- El corpus conservado está migrado con fidelidad y referencias resueltas; se
  justifican las excepciones concretas y se preservan sus fuentes recuperables.
- Las realizaciones e instalaciones KORA de Codex y Hermes del alcance están
  actualizadas y comprobadas. La evidencia distingue forma, semántica, instalación
  y comportamiento real, y declara límites sin sustituir prueba con un sello.
- La actualización conserva el estado ajeno y se verifica recuperación ante
  fallos relevantes, con pruebas que detecten consecuencias observables.
- La maquinaria anterior, sus instrucciones contradictorias y el soporte a
  destinos retirados salen de la superficie activa. Hay una sola autoridad por
  objeto y una interfaz simple documentada con comandos reales.
- El relevo local, los commits semánticos y las verificaciones finales están
  cerrados. El estado de Git y cualquier limitación residual quedan declarados.

La construcción de un núcleo mínimo, un plan, una muestra migrada o un reporte de
tests por sí solos no satisfacen este mandato. La tarea mantiene su autonomía y
continúa hasta completar el resultado o acreditar un bloqueo externo real.
