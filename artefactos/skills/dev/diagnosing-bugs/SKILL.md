---
urn: urn:dev:artefacto:diagnosing-bugs
nombre: diagnosing-bugs
version: 1.0.0
estado: activo
descripcion: "Diagnóstico disciplinado de bugs difíciles y regresiones de rendimiento mediante reproducción, bucles de feedback, hipótesis falsables y evidencia ligada al candidato."
fuente: "Reescritura KORA de mattpocock/skills/skills/engineering/diagnosing-bugs/SKILL.md; upstream commit: 2ab958093e83e0ec752e6c1c5932da465bf23e0c; sha256:7a0779480f323a66d109404646bcc1a14bf0232b45b3e3ea93b652a035718acb; licencia MIT: referencias/mattpocock-skills-MIT.txt"
autor: Codex
creado: 2026-08-03
lang: es
tags: [diagnostico, depuracion, reproduccion, regresion, rendimiento]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob, Write, Edit, Bash]
targets: [codex]
---

# diagnosing-bugs

## Propósito y contrato observable

Usar esta skill ante un bug, fallo intermitente, salida incorrecta o regresión
de rendimiento. Preservar el síntoma exacto, el candidato evaluado y el alcance
autorizado. Leer CONTEXT.md si existe y revisar los ADR del área antes de
interpretar módulos.

La salida es un recibo de diagnóstico con:

- síntoma y entorno reproducible;
- bucle elegido, comando ejecutado y resultado observado;
- reproducción mínima, hipótesis ordenadas, predicciones y probes;
- test de regresión, cambio aplicado, limpieza y post-mortem;
- evidencia por fase y estado final.

Cada evidencia debe registrar exactamente uno de estos estados:

- PASS: el criterio se ejecutó y quedó demostrado para el candidato indicado.
- FAIL: el criterio se ejecutó y no se cumplió para ese candidato.
- ABSENT: se buscó una evidencia requerida y no existe en el alcance evaluado.
- NOT_RUN: no se ejecutó por un gate fallido, una autorización ausente o una
  condición explícita.

Cada registro liga status, candidato (commit o árbol), comando o ruta,
observación y límite de inferencia. No convertir un PASS local en aceptación
humana, safety, causalidad universal ni garantía de runtime. No fijar nombres
de modelo ni niveles de razonamiento: pertenecen al runtime y no al contrato.

## Fase 1 — Construir un bucle de feedback

Tratar el bucle como el gate previo a toda hipótesis. Construirlo en este orden
preferente, adaptándolo al seam real:

1. test fallido en el seam que alcanza el bug;
2. curl o script HTTP contra un servidor reproducible;
3. invocación CLI con fixture y comparación contra salida conocida;
4. navegador headless con aserciones de DOM, consola y red;
5. replay de una traza, payload o registro capturado;
6. harness descartable con el mínimo de dependencias;
7. loop de propiedades o fuzz con entradas controladas;
8. harness de bisección entre commits, versiones o datasets;
9. loop diferencial entre una versión, configuración o implementación;
10. script HITL estructurado como último recurso.

Después de construirlo, apretarlo: reducir inicialización, afirmar el síntoma
exacto y fijar tiempo, semilla, filesystem y red cuando corresponda. Un bucle
rápido y determinista vale más que una suite amplia que no pueda ponerse roja
por este bug.

Para un caso no determinista, aumentar la tasa de reproducción con repeticiones,
stress, paralelismo controlado o ventanas temporales acotadas. Registrar la
tasa y el método; no llamar determinista a una señal que no lo es.

Si no se puede construir un bucle, detener la investigación con un bloqueo
honesto. Enumerar lo intentado y solicitar solo una de estas entradas:
acceso al entorno que reproduce, artefacto capturado (HAR, logs, core dump o
grabación con marcas de tiempo) o autorización para instrumentación temporal.
Sin bucle no formular hipótesis ni presentar una teoría como diagnóstico.

**Criterio de completitud comprobable.** Marcar PASS solo si existe un comando
ya ejecutado al menos una vez que recorre el código real, aserta el síntoma
exacto y forma un bucle red-capaz que puede ponerse rojo, entrega el mismo
veredicto en cada corrida o tiene
alta reproducción documentada, tarda segundos y corre sin intervención. Si
falta cualquiera de esas pruebas, marcar FAIL o ABSENT según corresponda y
dejar las fases posteriores como NOT_RUN.

## Fase 2 — Reproducir y minimizar

Ejecutar el bucle y comparar su salida con lo que la persona reportó. Confirmar
que falla el mismo caso, repetirlo varias veces o medir su tasa si es no
determinista y conservar el mensaje, salida, tiempo o traza exactos.

Minimizar después de observar el rojo: quitar una entrada, caller, configuración,
dato o paso por vez y ejecutar de nuevo. Conservar únicamente lo que sea
load-bearing para la falla. El repro es mínimo cuando quitar cualquier elemento
restante vuelve el bucle verde. No avanzar por haber encontrado un fallo
cercano pero distinto.

**Criterio de completitud comprobable.** Marcar PASS con el comando, número de
corridas, síntoma capturado y repro mínimo ligados al mismo candidato. Marcar
FAIL si no reproduce el síntoma exacto; marcar ABSENT si el artefacto necesario
no está disponible; marcar NOT_RUN si la Fase 1 no pasó.

## Fase 3 — Formular hipótesis falsables

Generar primero 3–5 hipótesis rankeadas. Para cada una declarar causa propuesta,
predicción observable y condición de refutación:

Si X es la causa, cambiar Y debe eliminar el bug o cambiar Z debe empeorarlo.

No aceptar intuiciones sin predicción. Hacer un checkpoint humano no bloqueante:
mostrar la lista rankeada para recibir conocimiento de dominio y continuar con
el ranking vigente si no llega respuesta. Registrar si la respuesta reordenó o
descartó alguna hipótesis; no esperar esa respuesta para seguir.

**Criterio de completitud comprobable.** Marcar PASS solo con entre tres y
cinco hipótesis, orden explícito, predicción falsable por hipótesis y
checkpoint emitido. Marcar FAIL si alguna hipótesis no puede ser refutada;
marcar NOT_RUN si no existe repro mínimo.

## Fase 4 — Ejecutar probes ligados a predicciones

Para cada probe nombrar la hipótesis y la predicción que discrimina. Cambiar una
sola variable por corrida. Preferir debugger o REPL; después logs dirigidos en
los límites que separan hipótesis. Etiquetar cada log temporal con un prefijo
único como [DEBUG-a4f2] y eliminarlo al cerrar. No registrar todo para buscar a
ciegas.

### Rama de rendimiento

Si el bug es lento, medir antes de modificar: establecer baseline con harness
temporal, profiler, reloj monotónico o plan de consulta, fijar entradas y
reportar unidades y variación. Luego bisectar o comparar configuraciones. Una
impresión de logs no sustituye una medición.

**Criterio de completitud comprobable.** Marcar PASS cuando cada probe tenga
hipótesis, predicción, una variable, resultado y candidato; la rama de
rendimiento exige además baseline antes del fix. Marcar FAIL ante probes
ambiguos o múltiples variables; marcar NOT_RUN si la Fase 3 no pasó.

## Fase 5 — Fijar y probar en el seam correcto

Escribir el test de regresión antes del fix solo si existe un seam correcto:
debe recorrer el patrón real del bug en el call site, no una unidad demasiado
profunda que produzca falsa confianza. Convertir el repro mínimo en test,
observarlo rojo, aplicar el cambio mínimo y observarlo verde. Reejecutar luego
el bucle original no minimizado.

Si no existe seam correcto, registrar esa ausencia como hallazgo arquitectónico
y no fabricar un test decorativo. Elevar la necesidad de un seam a la fase de
post-mortem, preservando el bloqueo como evidencia.

**Criterio de completitud comprobable.** Marcar PASS solo con test rojo antes
del fix en el seam correcto, verde después, bucle original verde y resultados
ligados al candidato final. Marcar ABSENT si no hay seam; marcar FAIL si el
test no reproduce el patrón; marcar NOT_RUN si una fase previa no pasó.

## Fase 6 — Limpiar y hacer post-mortem

Antes de cerrar:

- reejecutar el bucle original;
- reejecutar el test de regresión o conservar documentada la ausencia de seam;
- buscar y retirar todos los prefijos [DEBUG-...];
- borrar prototipos descartables o moverlos a una zona de debug explícita;
- declarar qué hipótesis resultó correcta y por qué la evidencia la distingue.

Preguntar qué cambio de arquitectura habría prevenido el bug. Recomendar
transferir ese hallazgo a una skill de mejora arquitectónica solo después del
fix y con el seam, acoplamiento o callers concretos identificados.

**Criterio de completitud comprobable.** Marcar PASS cuando el repro original
no falla, la regresión está verde o el seam ausente está documentado, no quedan
instrumentos temporales y el post-mortem identifica prevención y límites.
Marcar FAIL si queda residuo o el bug original persiste; marcar NOT_RUN si una
fase previa no pasó.

## Recibo de cierre

Entregar una fila por fase con PASS, FAIL, ABSENT o NOT_RUN y:
candidato evaluado, comando o ruta, observación, cambios propios, límites y
siguiente acción. El cierre técnico no autoriza aceptación humana ni afirma
causalidad universal. Si el entorno impidió un gate, conservar el bloqueo y no
rellenarlo con hipótesis, confianza o el color de una suite.
