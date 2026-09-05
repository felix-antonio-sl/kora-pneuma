---
urn: urn:kora:artefacto:decision-operable
nombre: decision-operable
version: 1.0.0
estado: deprecado
descripcion: "Usar cuando una pregunta de decisión sea ambigua, abstracta, burocrática o difícil de responder; cuando mezcle autoridad, evidencia y ejecución; o cuando se necesite convertir contexto disperso en una recomendación y una pre-respuesta breve, comprensible, adoptable y recuperable sin inventar hechos ni permisos."
fuente: "Autoría de novo KORA del 2026-08-25. Destila un patrón recurrente de conducción decisional observado en preguntas complejas de producto, operación y organización; conserva el método genérico y excluye las decisiones y fuentes particulares de los casos que permitieron descubrirlo."
autor: FS
creado: 2026-08-25
lang: es
tags: [decision, elicitacion, autoridad, evidencia, recomendacion, pre-respuesta, antiburocracia]
vector: [2, 0, 2, 0, 1]
sigma: [2, 1, 3, 2, 1]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [codex, hermes]
alcance: usuario
estados: [encuadrar, resolver-autoridad, reconstruir-acto, decidir-estado, redactar, comprobar]
---

# decision-operable

## Finalidad

Convertir una pregunta difícil de contestar en una **decisión que una persona
pueda comprender, adoptar, modificar o dejar explícitamente abierta**.

La skill transforma la representación del problema; no aporta por sí misma
conocimiento de dominio, autoridad institucional ni evidencia. Su principio es:

> Reducir la carga de decidir sin reducir la realidad que cambia la decisión.

La salida debe ser breve y directa. La comprobación interna puede ser más
completa, pero solo se exponen las distinciones que cambian la respuesta, su
validez o su recuperación.

## Cuándo usar

- La pregunta usa categorías vagas como «beneficiario», «responsable»,
  «receptor capaz», «cobertura» o «registro propietario» sin nombrar el objeto.
- El operador ya entregó hechos útiles, pero la respuesta vuelve a pedirlos o
  se refugia en «necesita evidencia».
- Una decisión mezcla propuesta técnica, permiso, ratificación, ejecución y
  prueba de resultado.
- Se necesita una recomendación fundada y una pre-respuesta lista para adoptar
  o editar, no una clase teórica ni otro cuestionario.
- Un traspaso parece completo con un envío, aunque falten aceptación,
  responsabilidad sucesora o recuperación.

No usar para inventar el contenido que una fuente competente todavía no
adjudica. Si la solicitud es una pregunta factual simple, responderla
directamente.

## Contrato interno

Antes de redactar, reconstruir solo lo necesario:

1. **Beneficiario:** quién mejora o queda protegido si se decide bien.
2. **Objeto de decisión:** qué cosa concreta se está eligiendo, autorizando,
   asignando o dejando abierta.
3. **Plano y autoridad:** quién puede proponer, ratificar, implementar,
   verificar y operar; estas facultades no se heredan entre sí.
4. **Hechos vigentes:** lo ya declarado o comprobado. No volver a preguntar al
   operador por un hecho que ya entregó.
5. **Incertidumbre decisiva:** qué falta y si realmente cambia la validez, la
   autoridad, la seguridad, la reversibilidad o la alternativa elegida.

Separar siempre estas clases cuando aparezcan:

| Clase | Significado |
|---|---|
| Hecho | afirmación respaldada por la entrada o una fuente observable |
| Inferencia | conclusión razonable que todavía depende de supuestos |
| Propuesta | solución recomendada, aún no adoptada |
| Ratificación | acto de la autoridad competente que adopta una propuesta |
| Implementación | materialización de lo decidido |
| Validación | evidencia de que la implementación cumple el criterio evaluado |

Una clase no prueba la siguiente. Ratificar una respuesta en una herramienta
de apoyo adopta esa respuesta en dicha superficie; no crea por sí solo un
permiso externo, una ejecución ni una validación.

## Flujo

### 1. Encuadrar en lenguaje concreto

Reescribir mentalmente la pregunta como:

> ¿Quién debe decidir o hacer qué, sobre cuál objeto, para qué resultado y
> dentro de qué autoridad?

Si el sustantivo no tiene objeto —«beneficiario de qué», «usuarios de qué»,
«acceso a qué»— completarlo con el contexto disponible. Preguntar al operador
solo si falta una elección material que no puede recuperarse de las fuentes.

### 2. Resolver la frontera de autoridad

Asignar cada verbo al plano correcto. Una misma persona puede ocupar varios
planos, pero la respuesta debe expresar con qué mandato actúa en cada uno.

- La autoridad técnica puede decidir construcción y preparación sin aprobar
  operación institucional.
- La capacidad de registrar no concede capacidad de decidir.
- Una recomendación automática no sustituye al decisor competente.
- Una prueba satisfactoria demuestra solo el criterio que evaluó.

Si la autoridad no está adjudicada, proponer una asignación para el alcance
actual y declarar quién debe confirmarla antes del efecto que excede ese
alcance.

### 3. Reconstruir el acto material cuando corresponda

Para decisiones que crean efectos o transfieren responsabilidad, comprobar la
cadena completa:

```text
ejecutor + acción + objeto + autorización + resultado
→ receptor capaz + acuse
→ obligación sucesora o cierre válido
→ recuperación ante silencio, rechazo o falla
```

No imprimir la cadena como formulario. Integrar en la pre-respuesta solo los
eslabones que evitan una ambigüedad real. Un envío no equivale a recepción; un
acuse técnico no equivale a aceptación humana; un cierre administrativo no
equivale necesariamente al resultado buscado.

Si la pregunta trata de entrega, notificación, escalamiento, traspaso o cierre,
la pre-respuesta tiene esta forma mínima, expresada en prosa:

```text
quién entrega qué resultado → quién lo acepta y asume qué siguiente paso
→ quién conserva la responsabilidad mientras falta el acuse
→ qué ocurre ante rechazo, silencio o falla
```

Los cuatro slots son obligatorios en ese caso, aunque la respuesta solicitada
sea concisa. No exigirlos en decisiones sin transferencia de responsabilidad.

### 4. Decidir el estado correcto

| Estado | Usarlo cuando |
|---|---|
| `RESUELTA` | existe base suficiente para adoptar una respuesta dentro del alcance |
| `NECESITA EVIDENCIA` | una afirmación propuesta requiere respaldo que cambie su validez o autorización |
| `ABIERTA` | la autoridad competente todavía debe adjudicar el contenido de la decisión |
| `BLOQUEADA` | no existe un movimiento seguro o útil antes de resolver la dependencia nombrada |
| `DIFERIBLE` | decidir ahora no cambia el incremento ni un riesgo actual |
| `DESCONOCIDA` | se ignora un hecho y aún no corresponde inferirlo |
| `NO APLICA` | el supuesto de la pregunta no existe en el alcance actual |

`NECESITA EVIDENCIA` no es una respuesta por defecto ni reemplaza una
recomendación. Si los hechos disponibles permiten decidir el desarrollo
reversible pero no la operación posterior, resolver el primer plano y dejar
la condición posterior en su frontera exacta.

### 5. Redactar para adopción

Entregar, en este orden y omitiendo lo que no aporte:

1. **Pregunta en lenguaje directo:** una frase que nombra el objeto real.
2. **Síntesis contextual:** qué se decide y por qué importa, en dos a cuatro
   frases.
3. **Recomendación:** la solución preferida y su frontera.
4. **Pre-respuesta:** texto en primera persona institucional o en la voz
   solicitada, listo para ratificar o modificar.
5. **Estado:** uno de los estados anteriores.
6. **Evidencia decisiva:** solo la fuente o comprobación que puede cambiar la
   adopción, la autoridad o la validez.
7. **Límite:** qué no queda autorizado, ejecutado o demostrado.

Si el operador pide solo la redacción final, entregar solo la pre-respuesta y
el límite indispensable.

### 6. Comprobar y detenerse

Antes de cerrar:

- ¿La pregunta dice de qué objeto habla?
- ¿La respuesta usa los hechos ya aportados?
- ¿La recomendación decide lo decidible y conserva abierto solo lo irreducible?
- ¿Cada autoridad queda limitada a su plano?
- ¿Un traspaso conserva receptor, acuse, sucesión y recuperación suficientes?
- ¿La evidencia solicitada tiene una consecuencia real?
- ¿La salida puede adoptarse sin descifrar jerga ni completar otra plantilla?

Si todo pasa, detenerse. No agregar matrices, módulos, escalas o gates sin un
consumidor actual.

## Ejemplo

**Entrada:** «¿Quién recibe el cierre de una incidencia crítica entre Soporte
y Plataforma?»

**Pregunta en lenguaje directo:** ¿Qué función acepta que la incidencia quedó
resuelta y asume el siguiente paso frente al usuario?

**Recomendación:** Plataforma entrega la corrección y su evidencia; la persona
responsable del caso en Soporte acepta o devuelve el cierre. El caso solo se
cierra tras ese acuse. Si rechaza o no responde dentro del plazo operativo,
vuelve a Plataforma con causa y responsable vigente.

**Pre-respuesta:** «La persona responsable del caso en Soporte recibe y acepta
el cierre. Plataforma entrega la resolución y la evidencia; Soporte confirma
el restablecimiento, comunica el resultado y conserva la relación con el
usuario. Sin aceptación, el caso permanece abierto y retorna a Plataforma con
la observación pendiente.»

**Estado:** `RESUELTA`, si esa asignación cabe en la autoridad del decisor;
`ABIERTA`, si todavía debe adjudicarla el dueño del proceso.

## Errores frecuentes

| Error | Corrección |
|---|---|
| Repetir la pregunta con términos más solemnes | nombrar objeto, actor y resultado concreto |
| Pedir evidencia sobre un hecho ya declarado | usarlo y pedir respaldo solo si cambia la decisión |
| Responder únicamente «levantar» o «definir» | proponer una solución adoptable con estado y límite |
| Confundir quien registra con quien decide | separar autoría del registro y autoridad del acto |
| Dar por cerrado un envío | exigir receptor capaz, acuse y recuperación |
| Resolver todos los futuros posibles | decidir el incremento actual y diferir lo que no lo afecta |
| Convertir rigor en carga para el operador | hacer completa la comprobación interna y breve la salida |
