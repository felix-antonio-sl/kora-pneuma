# Wizard SD — del proposito a las cosas iniciales

Condensado operativo del wizard de System Diagram segun `urn:fxsl:kb:metodologia-forja-opm-es`, con validez gobernada por `urn:fxsl:kb:reglas-opm-estrictas-es` y superficie OPD/OPL gobernada por `spec-forja-opd-es` / `spec-forja-opl-es`. El manual base queda como procedencia delegada, no como autoridad primaria de esta skill.

> **Dos arranques hermanos (metodologia §A1.5, desde v1.6.0).** Este wizard
> realiza el arranque **SD-primero** (default del asistente guiado A2). El
> arranque **bottom-up** (bosquejo: fragmentos sueltos → reconciliacion por
> adopcion → SD0) es su hermano de primera clase y **no pasa por este wizard
> hasta la reconciliacion** — en ese momento las etapas de este documento se
> exigen sobre el SD resultante. Ver SKILL.md §Regimen bosquejo y spec-opd
> `R-OPD-REF-20`. No forzar este wizard a un operador que esta bosquejando.

## Paso 0 — Verificar aplicabilidad de OPM

Antes de modelar, confirmar que el sistema tiene **funcion transformadora identificable**. Pregunta clave:

> "¿Que cosa cambia, se crea o se destruye por la accion del sistema?"

Si la respuesta es nula o solo describe estructura estatica, OPM no es la herramienta adecuada. Sugerir alternativa (`data-modeling`, `ontologista-gist`, BPMN, etc.) y abortar.

> Nota: en sistemas **naturales** el transformee es el afectado que porta el outcome; su ausencia sigue invalidando OPM, pero la ausencia de beneficiario humano (o de purpose, problem occurrence y agentes humanos) NO invalida.

## Paso 1 — Clasificar el sistema

Determinar el tipo del sistema antes de hablar de proposito:

| Tipo | Implicancia para el SD |
|------|------------------------|
| Artificial | modelar purpose, problem occurrence, agentes humanos si existen e instrumentos. |
| Natural | modelar outcome/affectee; no forzar purpose, problem occurrence ni agentes humanos. |
| Social | 5 componentes completos: purpose, problem occurrence, agentes humanos, instrumentos y entorno; condiciones ambientales/sociales por enlace habilitador con estado especificado. |
| Socio-tecnico | modelar purpose, beneficiario, agentes humanos, instrumentos tecnicos y contexto externo. |

La clasificacion no es decorativa: decide que preguntas son legales. Si no se
puede clasificar, entrar a `aclarar` antes de plasmar.

## Paso 2 — Identificar el proposito u outcome

Una sola frase: **"Este sistema sirve para ___"**. Ejemplos:

- "transformar agua y cafe molido en cafe hecho"
- "diagnosticar pacientes en urgencia"
- "convertir solicitudes ciudadanas en resoluciones administrativas"

El proposito es la **funcion principal**, no una descripcion de estructura.

Para sistemas naturales, sustituir proposito por **outcome**: que cambia u
ocurre, sin atribuir intencion.

## Paso 3 — Nominalizar la funcion como proceso central

La funcion → un proceso del SD. Convencion de nombre: gerundio o sustantivo derivado de verbo activo.

| Funcion | Proceso |
|---------|---------|
| transformar agua y cafe en cafe hecho | Hacer Cafe |
| diagnosticar pacientes | Diagnosticar |
| convertir solicitudes en resoluciones | Resolver Solicitud |

Una sola idea por proceso. Si necesitas varios verbos, probablemente son sub-procesos para una iteracion posterior de in-zooming.

## Paso 4 — Identificar beneficiario o affectee primario

El SD debe declarar quien o que recibe el valor/cambio principal:

- **Beneficiario**: stakeholder humano u organizacional que extrae valor.
- **Affectee primario**: objeto que cambia cuando no corresponde hablar de beneficiario, especialmente en sistemas naturales.

Reglas:

- Si hay beneficiario humano/colectivo, nombrarlo como objeto singular o como
  `Grupo` cuando represente coleccion humana.
- Si el beneficiario es inanimado o conjunto de cosas, usar `Conjunto`.
- Si no aplica beneficiario, registrar explicitamente `sin beneficiario humano`
  y usar affectee/outcome.

## Paso 5 — Fijar atributo de valor y estados input/output

Definir que atributo cambia y sus estados:

```text
<Proceso Central> cambia <Atributo de Valor> de <Beneficiario/Affectee>
de <estado input> a <estado output>.
```

Si el operador no puede nombrar el atributo de valor, el SD no tiene funcion
auditable. Entrar a `aclarar`.

## Paso 6 — Identificar transformees y benefit-providing object

Las cosas que **cambian** por la accion del proceso. Tres patrones:

### 3a. Consumo / Produccion

El proceso consume una cosa y produce otra distinta.

- *Hacer Cafe* consume **Agua** y **Cafe Molido**; genera **Cafe Hecho**.

### 3b. Cambio de estado

Una misma cosa pasa de estado A a estado B por la accion del proceso.

- *Diagnosticar* cambia **Paciente** de `no-diagnosticado` a `diagnosticado`.

### 3c. Creacion / Destruccion

El proceso crea o destruye una cosa que antes no existia / dejara de existir.

- *Resolver Solicitud* genera **Resolucion Administrativa**.

Si hay multiples transformees, distinguir el **benefit-providing object**: la
cosa cuya transformacion materializa la funcion principal para el beneficiario.
Los otros transformees pueden ser inputs, consumibles, residuos o resultados
secundarios, pero no definen la funcion.

En sistemas **naturales** no hay beneficiario humano ni purpose: la funcion la
define el afectado/resultado que porta el outcome, NO un benefit-providing
object para un beneficiario (metodologia-opm §5.1). El outcome puede ser
beneficioso O PERJUDICIAL (`Fetus Developing` → `embryo`/`baby`; `Rain Storm
Forming`). Basta que la cosa transformada porte el resultado.

## Paso 7 — Resolver agencia humana

Preguntar por agentes humanos u organizacionales. Si no existen, registrar
`sin agentes humanos`; no inventar un agent placeholder.

OPM reserva `agent` exclusivamente para un humano o grupo de humanos (ISO 3.3 /
R-AG-1). Robots, software, IA, maquinas y sistemas externos van por enlace de
INSTRUMENTO, aunque en lenguaje comun se les llame agentes (R-AG-1A). El
criterio NO es voluntad/responsabilidad: es ser humano.

## Paso 8 — Nombrar sistema y frontera

Nombrar el sistema y decidir que cosas son sistemicas vs. ambientales.

- Sistema: suele nombrarse desde el proceso central (`<Proceso> Sistema`), salvo
  termino de dominio mejor.
- Frontera: cada cosa queda sistemica o ambiental. No dejar alcance implicito.

## Paso 9 — Identificar instrumentos

Cosas necesarias para que el proceso ocurra **pero que no son consumidas ni transformadas**:

- **Instrument** (herramienta, dispositivo, sistema externo):
  - *Hacer Cafe* requiere **Cafetera**.
  - *Diagnosticar* requiere **Historia Clinica**.
  - *Resolver Solicitud* requiere **Sistema Documental**.

## Paso 10 — Delimitar contexto externo

Identificar objetos/procesos ambientales que interactuan con el sistema pero no
pertenecen a el. Si una cosa cruza frontera, explicitar el rol de cada extremo
en vez de dejarla doblemente afiliada.

## Paso 11 — Problem occurrence o no-aplicacion

Para sistemas artificiales, sociales y socio-tecnicos, declarar el problema
inicial que justifica el sistema cuando el modelo lo requiere. Para sistemas
naturales, cerrar como `NO APLICA`.

No omitir silenciosamente este punto: `NO APLICA` es una decision de modelo.

Con esto cierran las **11 etapas canonicas (0..11)** del wizard de SD segun
`metodologia-forja-opm-es` §A2. Lo que sigue —conectar links y decidir si
refinar— es **post-cierre**, no etapa del wizard, y debe unificarse con el
bootstrap-sd de `SKILL.md`.

## Post-cierre A — Conectar con links procedurales

Tipos canonicos segun `reglas-opm-estrictas-es`, realizados en OPD/OPL por las specs Forja:

| Link | Cuando | OPL-ES |
|------|--------|--------|
| consumption | proceso consume objeto entero | `*<Proceso>* consume **<Objeto>**.` |
| result | proceso genera objeto nuevo | `*<Proceso>* genera **<Objeto>**.` |
| effect | proceso cambia estado de objeto | `*<Proceso>* cambia **<Objeto>** de \`<estado-A>\` a \`<estado-B>\`.` |
| agent | humano/organizacion activa el proceso | `**<Agente>** maneja *<Proceso>*.` |
| instrument | herramienta requerida sin consumirse | `*<Proceso>* requiere **<Instrumento>**.` |
| condition | precondicion habilitante | `*<Proceso>* ocurre si **<Objeto>** esta en \`<estado>\`.` |

Validar primero contra `reglas-opm-estrictas-es`; luego realizar la firma visual con `spec-forja-opd-es` y la sentencia con `spec-forja-opl-es`.

## Post-cierre B — Bimodalidad y gate de cierre

Para cada hecho del SD, emitir la sentencia OPL-ES correspondiente. Si una sentencia OPL no se puede formular sin ambiguedad, el OPD esta mal construido.

Ejemplo minimo (cafetera):

```
SD del sistema Hacer Cafe.

**Cafe Hecho** es un objeto fisico.
**Agua** es un objeto fisico.
**Cafe Molido** es un objeto fisico.
**Persona** es un objeto fisico.
**Cafetera** es un objeto fisico.
*Hacer Cafe* es un proceso fisico.

*Hacer Cafe* consume **Agua** y **Cafe Molido**.
*Hacer Cafe* genera **Cafe Hecho**.
**Persona** maneja *Hacer Cafe*.
*Hacer Cafe* requiere **Cafetera**.
```

Gate de cierre minimo:

- [ ] sistema clasificado.
- [ ] proposito/outcome declarado.
- [ ] proceso central nombrado.
- [ ] beneficiario o affectee primario identificado.
- [ ] atributo de valor + estados input/output declarados.
- [ ] transformees y benefit-providing object distinguidos.
- [ ] agentes humanos resueltos o `sin agentes humanos` declarado.
- [ ] instrumentos identificados.
- [ ] frontera sistemico/ambiental cerrada.
- [ ] problem occurrence declarado o `NO APLICA`.
- [ ] cada link tiene firma legal confirmada.
- [ ] cada hecho tiene OPL-ES validado por el operador.

## Post-cierre C — Decidir si el SD basta

Tres criterios:

1. **Suficiencia de detalle**: ¿el SD responde la pregunta del usuario? Si si → entregar; si no → refinar.
2. **Audiencia**: ¿el destinatario necesita ver sub-procesos? Si si → in-zooming.
3. **Validez**: pasar al estado `validar-modelo` antes de cualquier refinement.

## Anti-patrones del SD

- SD con **mas de un proceso central**: senal de que la funcion no esta bien identificada. Refinar el proposito.
- SD **sin transformee**: si nada cambia, OPM no aplica.
- SD con **agent no humano**: si activa una maquina, es instrument.
- SD que **excede el techo de claridad de 20-25 entidades por OPD** (A4.2): senal de que necesitas in-zooming inmediato. Como heuristica subordinada de la skill, ya >~7 cosas en el SD sugieren in-zoom temprano.
- SD que **describe estructura sin proceso**: usar otra herramienta (ERD, OWL).
