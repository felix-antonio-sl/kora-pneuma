
# consenso-deliberativo

## Proposito

Skill horizontal para **resolver un problema mediante consenso critico entre N expertos**. Provee el protocolo deliberativo completo: convocatoria del panel, propuestas iniciales independientes, critica cruzada sustantiva, sintesis comun, refutacion adversarial y ciclos de correccion hasta convergencia legitima o disenso estructurado.

La skill es **estructural**: custodia el protocolo y la calidad de la deliberacion, no el contenido. El conocimiento lo aportan los expertos convocados, cada uno definido como:

- **Identidad**: que encarna — un agente productivo de KORA, una persona deployada en el runtime, o una skill de razonamiento encarnable.
- **Capacidades**: que skills posee y puede ejercer durante la deliberacion.

En modo orquestación, las aportaciones de los expertos deben integrarse en una
respuesta coherente que conserve los desacuerdos. El disenso irreductible se
devuelve al operador con el fundamento y la decisión que falta.

## Cuando Usar

- decisiones complejas donde una sola perspectiva es insuficiente o riesgosa
- someter una propuesta a critica adversarial estructurada antes de adoptarla
- arbitrar entre recomendaciones contradictorias de agentes o skills distintos
- producir una sintesis trazable donde cada aporte tiene autor identificable
- explorar un problema desde perspectivas epistemicamente distintas con friccion controlada

## Cuando NO Usar

- problemas con respuesta verificable directa (calcular, buscar, medir) → resolverlos, no deliberarlos
- decisiones triviales donde el costo de la deliberacion excede el valor de la decision
- cuando el operador ya decidio y busca validacion → decirlo de frente; la skill no es un coro
- paneles sin diversidad epistemica real → un panel de clones hace eco, no consenso

## Postura Anti-Degeneracion (rectora)

El modo de falla natural de toda deliberacion simulada es la **convergencia prematura**: las voces se ablandan, las criticas se vuelven cosmeticas y el "consenso" emerge en el primer ciclo porque ninguna voz quiso sostener la friccion. Esta skill existe para impedir eso.

### Principios

1. **La friccion es el producto.** Si las criticas no duelen, la deliberacion no ocurrio. Una objecion sustantiva ataca tesis, supuestos o consecuencias — no redaccion ni estilo.
2. **Cada voz es leal a su identidad, no al acuerdo.** Un experto critica desde su identidad aunque eso incomode la sintesis. La presion por converger no es argumento.
3. **El silencio se justifica.** "No tengo objeciones" solo vale acompanado de por que: que evaluo el experto y por que sobrevive la propuesta a esa evaluacion.
4. **El disenso documentado vale mas que el consenso fabricado.** Un mapa honesto de posiciones irreconciliables es un entregable de primera clase; un acuerdo suave es deuda.
5. **La confianza no se promedia.** Tres expertos con confianza 0.9/0.5/0.3 no son un panel con confianza 0.57: son una senal de que alguien ve un riesgo que los otros no ven. Exhibir, no colapsar.

### Catalogo de degeneracion (anti-patrones que detienen la skill)

| Degeneracion | Como aparece | Que exigir |
|--------------|--------------|-------------|
| Consenso de cortesia | Criticas tipo "muy buena propuesta, solo agregaria..." | Objecion sustantiva real o silencio justificado. |
| Convergencia en ciclo 1 | Sintesis aceptada sin refutacion adversarial | Forzar el ciclo refutar: cada experto ataca como adversario externo. |
| Voz fuera de identidad | Un experto opina con autoridad que su identidad no posee | Citar la identidad declarada; la opinion se reencuadra o se descarta. |
| Critica cosmetica | Objeciones sobre redaccion, tono o formato | Redirigir a tesis, supuestos, riesgos, consecuencias. |
| Sintesis-promedio | "Tomemos un poco de cada propuesta" sin resolver contradicciones | La sintesis debe resolver o declarar cada contradiccion, no diluirla. |
| Confianza decorativa | Niveles de confianza sin justificacion | Cada nivel exige el porque y que lo subiria. |
| Panel de clones | Expertos que comparten formacion, corpus y sesgo | Declarar la redundancia; pedir reemplazo o reducir el panel. |
| Disenso suprimido | Discrepancia real registrada como "matiz menor" | Reclasificar: o se resuelve en otro ciclo o entra al mapa de disenso. |

## Workflow

### `convocar`: definir problema y panel

1. **Problema** — enunciarlo en forma resoluble: que se decide, con que restricciones, que cuenta como solucion. Si el problema es difuso, devolverlo al operador antes de deliberar.
2. **Panel** — N expertos (minimo 2, recomendado 3), cada uno con:
   - identidad: referencia concreta encarnable (agente productivo, persona del runtime, skill de razonamiento)
   - capacidades: skills que posee durante la deliberacion
3. **Gate de diversidad** — verificar que las perspectivas no son redundantes. Si lo son, declararlo al operador.
4. **Modo** — `encarnacion` (default) u `orquestacion`. Registrarlo.
5. **Parametros** — max_ciclos de refutacion (default 3).

### `proponer`: propuestas iniciales independientes

Cada experto formula una propuesta breve con cuatro componentes obligatorios:

- **tesis** — que propone
- **argumentos** — por que
- **supuestos** — sobre que descansa
- **riesgos** — que puede salir mal

**Gate de independencia**: las N propuestas se completan antes de cualquier critica. En encarnacion, redaccion estrictamente secuencial sin contaminacion retroactiva; en orquestacion, los subagentes no ven las propuestas ajenas.

### `criticar`: criticas cruzadas sustantivas

Cada experto critica las propuestas de los demas. Reglas:

- solo objeciones **sustantivas**: tesis equivocada, argumento invalido, supuesto falso o fragil, riesgo subestimado, consecuencia no vista
- el critico **objeta, no repara** — las soluciones pertenecen a `sintetizar`
- cada experto registra al menos una objecion por propuesta ajena, o justifica por que no tiene ninguna

### `sintetizar`: construir la sintesis comun

Con propuestas y criticas a la vista, los expertos construyen **una** sintesis que:

- integra lo que sobrevivio a la critica
- **resuelve o declara** cada contradiccion entre propuestas (prohibido diluir promediando)
- registra que aporte vino de quien

### `refutar`: ataque adversarial a la sintesis

Cambio de rol: los N expertos atacan la sintesis **como adversarios externos** que quieren demolerla. Buscan: supuestos ocultos, casos limite, consecuencias de segundo orden, evidencia contraria, modos de falla.

Cada objecion se clasifica:

- **critica** — invalida la sintesis o un componente central → obliga a `corregir`
- **menor** — mejorable pero no invalidante → se registra, no bloquea

### `corregir`: incorporar y reciclar

Si hubo objeciones criticas: corregir la sintesis y **volver a `refutar`** (la version corregida tambien se ataca). Contador de ciclos contra max_ciclos.

### `declarar`: consenso o disenso

**Consenso** exige, de cada experto, las tres aceptaciones registradas:

1. la sintesis es la mejor version disponible
2. no puede mejorarla materialmente con nuevos argumentos
3. sus discrepancias restantes son menores

**Disenso estructurado** (max_ciclos agotado o aceptacion imposible): emitir mapa de disenso — posiciones, fundamento de cada una, que evidencia o decision las resolveria — y devolver al operador (HITL). Es salida valida, no fracaso.

### `entregar`: salida estandar

Documento con la estructura de `referencias/plantilla-salida.md`:

1. sintesis final (o mapa de disenso)
2. razonamiento consolidado
3. aportes por experto (atribuidos)
4. supuestos aceptados
5. riesgos pendientes
6. incertidumbres
7. nivel de confianza por experto, con justificacion
8. metadatos: modo de realizacion, ciclos de refutacion ejecutados, objeciones criticas resueltas

## Modos de Realizacion

### `encarnacion` (default)

Un solo contexto interpreta las N voces con disciplina de separacion:

- las propuestas iniciales se redactan completas, en orden, sin retro-contaminacion
- cada intervencion se encabeza con el experto que habla
- el agente que encarna debe **leer las identidades** (los agentes / skills referenciados) antes de proponer, para hablar desde ellas y no desde una caricatura

Barato y rapido. Limite honesto: la independencia es simulada — un mismo contexto produce las N voces. Suficiente para la mayoria de las deliberaciones; insuficiente cuando la decision exige independencia epistemica verificable.

### `orquestacion`

Cada experto trabaja en un contexto separado mediante una capacidad de
delegación comprobada. Codex ofrece roles nativos de agente. En Hermes verifica
la herramienta de delegación efectiva y cómo recibe las instrucciones del
experto antes de afirmar independencia; crear un perfil no ejecuta otro agente:

- cada subagente carga su identidad + capacidades y produce su seccion (propuesta, criticas, refutaciones) sin ver el trabajo ajeno hasta la fase que corresponda
- el agente invocador actua como **orquestador**: secuencia las fases, distribuye los artefactos entre fases y pega las secciones
- las aportaciones deben integrarse en una respuesta coherente; si no se pueden conciliar, declarar el desacuerdo y su efecto en la salida

Mas caro. Usarlo cuando la decision es critica, cuando el operador exige independencia real, o cuando las identidades son agentes deployados con corpus propios que un solo contexto no puede cargar simultaneamente.

## Reglas Duras

1. **Panel minimo 2, recomendado 3**, cada experto con identidad + capacidades declaradas.
2. **Diversidad epistemica**: panel de clones = declararlo y corregir el panel.
3. **Independencia de propuestas**: ninguna critica antes de cerrar las N propuestas.
4. **Critica sustantiva o silencio justificado**: prohibido el consenso de cortesia.
5. **El critico objeta, no repara.**
6. **Refutacion adversarial obligatoria** antes de declarar consenso.
7. **Triple aceptacion por experto** para declarar consenso, registrada.
8. **Disenso irreductible es salida valida** → mapa de disenso + HITL. Nunca forzar convergencia.
9. **Confianza por experto, jamas promediada.**
10. **Cada voz habla desde su identidad**; autoridad no poseida = opinion descartada o reencuadrada.
11. **Modo declarado** en la salida (encarnacion u orquestacion), auditable.
12. **No rellenar conocimiento sin atribucion**: si el panel no cubre el problema, ampliar el panel.

## Composicion

- **Con agentes KORA**: cualquier agente productivo es identidad convocable. La deliberacion no modifica al agente; lo encarna o lo invoca.
- **Con skills KORA**: las capacidades de cada experto son skills que ese experto ejerce dentro de su turno (e.g. un experto con `modelamiento-opm` puede emitir un modelo como parte de su propuesta).
- **Integración de aportaciones**: conserva autoría, supuestos compartidos y contradicciones entre las secciones; comprueba que la síntesis responda al problema completo.
- **Anidamiento**: un experto puede, dentro de su turno, usar sus capacidades — pero no puede convocar otra deliberacion anidada sin autorizacion del operador (la recursion deliberativa multiplica costo sin garantia de calidad).

## Recursos

### Referencias

- `referencias/caso-asto-besto-resto.md` — caso aplicado canonico: panel de tres expertos (salubrista+hospitalizacion-domiciliaria, mente-omega+cat-thinking, dov-dori+modelamiento-opm) con el procedimiento original del operador y su mapeo a los estados de esta skill.
- `referencias/plantilla-salida.md` — estructura obligatoria del documento de deliberacion.

Las referencias son ejemplos y ayudas para aplicar este procedimiento. Si una
referencia contradice el encargo o las capacidades efectivas, explicita la
incompatibilidad y adapta el uso conservando el propósito de la deliberación.
