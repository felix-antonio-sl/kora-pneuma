# Plantillas OPL-ES por tipo de hecho

Plantillas operativas ancladas primero a `urn:fxsl:kb:spec-forja-opl-es`, SSOT bidireccional del OPL de OPFORJA con vocabulario cerrado. `urn:fxsl:kb:opl-es` queda como capa base delegada cuando la spec Forja lo cita; no se usa para saltarse el enum, los GAPs ni el contrato de roundtrip de opforja.

## Vocabulario cerrado de verbos y copulas (spec-forja-opl-es §1)

El vocabulario OPL-ES para opforja es un **enum cerrado** (`spec-forja-opl-es` §1.1). La generacion no debe emitir un verbo fuera de esa seccion; el parseo no debe reconocer como verbo OPL un token ausente. La lista siguiente separa entradas alineadas de entradas GAP-* para no prometer roundtrip donde la app aun no lo tiene.

### Verbos procedurales

| Verbo | Significado | Familia de oracion |
|-------|-------------|-------------------|
| `consume` | el proceso destruye el objeto | consumo (T1, TS1) |
| `genera` | el proceso crea el objeto | resultado (T2, TS2) |
| `afecta` | el proceso modifica el objeto sin estados explicitos | efecto (T3, TS3) |
| `cambia … de … a` | el proceso transforma el estado del objeto | cambio de estado |
| `maneja` | el agente humano habilita el proceso | agente |
| `requiere` | el proceso depende del instrumento | instrumento |
| `inicia` | el objeto/estado dispara el proceso | evento |
| `invoca` | un proceso dispara otro proceso | invocacion; autoinvocacion |
| `ocurre` | el proceso se ejecuta bajo condicion o excepcion | condicion; excepcion |
| `existe` | el objeto esta presente como precondicion | condicion de existencia |
| `se omite` | el proceso no se ejecuta (rama negativa) | condicion (alternativa) |
| `se consume` | el objeto se destruye (voz pasiva refleja) | condicion de consumo |

### Verbos estructurales

| Verbo | Significado | Familia de oracion |
|-------|-------------|-------------------|
| `consta de` | el todo agrega las partes | agregacion-participacion |
| `exhibe` | el exhibidor caracteriza atributos/operaciones | exhibicion-caracterizacion |
| `son` | varias especializaciones son la general | especializacion jerarquica (plural) |
| `es un` / `es una` | una especializacion es la general | especializacion jerarquica (singular) |
| `es una instancia de` | la instancia pertenece a la clase | clasificacion-instanciacion |
| `se relaciona con` | enlace estructural etiquetado nulo | tagged sin etiqueta de usuario |

### Verbos de refinamiento y estados

| Verbo | Significado | Familia de oracion |
|-------|-------------|-------------------|
| `puede estar` | el objeto enumera sus estados posibles | enumeracion de estados (D5, D6) |
| `puede ser` | especializacion XOR de generales mutuamente excluyentes | especializacion XOR (RX1, RX2); GAP-XOR-FEATURE/GAP-XOR-PARSER |
| `se descompone` | el proceso se descompone (in-zooming) | descomposicion sincrona |
| `se despliega` | la cosa se despliega (unfolding) | despliegue asincrono |

### Verbos con GAP (canonicos pero no emitidos por el generador opforja v0)

| Verbo | Significado | Estado en opforja v0 |
|-------|-------------|---------------------|
| `varia de … a` | el atributo recorre un rango de valores | GAP-VARIA |
| `es de tipo` | la cosa declara su tipo | GAP-TIPO |
| `se refina` | refinamiento explicito entre OPDs | GAP-REFINA |
| `se pliega` | supresion de hechos refinados en OPD ascendente | GAP-PLIEGA |
| `se recompone` | recomposicion desde refinados | GAP-RECOMPONE |

### Reglas duras de verbos

- **R-VERB-EST-1**: enumeracion de estados DEBE usar **puede estar**.
  Correcto: `**Pedido** puede estar \`pendiente\`, \`despachado\` o \`cerrado\`.`
  Incorrecto: `**Pedido** puede ser \`pendiente\`, \`despachado\` o \`cerrado\`.`
- **R-VERB-EST-2**: **puede ser** solo para especializacion XOR. Nunca para estados.
- `existe`, `se omite` y `se consume` solo dentro de plantillas condicionales/excepcion, no como oracion autonoma.

## Existencia de cosa

| Hecho | Plantilla |
|-------|-----------|
| una cosa es objeto | `**<Cosa>** es un objeto.` |
| una cosa es proceso | `*<Cosa>* es un proceso.` |
| una cosa es objeto fisico | `**<Cosa>** es un objeto fisico.` |
| una cosa es objeto informacional | `**<Cosa>** es un objeto informacional.` |
| una cosa es proceso fisico | `*<Cosa>* es un proceso fisico.` |

Nota: la tipografia (negrita para objetos, cursiva para procesos) es portadora de tipo. Sin ella el parser no distingue objeto de proceso.

## Estados de un objeto

| Hecho | Plantilla |
|-------|-----------|
| enumeracion de estados | `**<Objeto>** puede estar \`<estado1>\`, \`<estado2>\`, ..., \`<estadoN>\`.` |
| estado inicial | `**<Objeto>** esta inicialmente en \`<estado>\`.` |
| estado final | `**<Objeto>** esta terminalmente en \`<estado>\`.` |

Ejemplos:
```
**Paciente** puede estar `no-diagnosticado` o `diagnosticado`.
**Paciente** esta inicialmente en `no-diagnosticado`.
```

## Enlaces procedurales transformadores

| Tipo | Plantilla | Verbo canónico opforja |
|------|-----------|------------------------|
| consumo | `*<Proceso>* consume **<Objeto>**.` | `consume` |
| resultado | `*<Proceso>* genera **<Objeto>**.` | `genera` |
| efecto | `*<Proceso>* afecta **<Objeto>**.` | `afecta` |
| cambio de estado | `*<Proceso>* cambia **<Objeto>** de \`<estado-A>\` a \`<estado-B>\`.` | `cambia … de … a` |

Ejemplos:
```
*Preparar Cafe* consume **Cafe en Grano**.
*Preparar Cafe* genera **Cafe Bebida**.
*Diagnosticar* cambia **Paciente** de `no-diagnosticado` a `diagnosticado`.
```

## Enlaces procedurales habilitantes

| Tipo | Plantilla | Verbo canónico opforja |
|------|-----------|------------------------|
| agente | `**<Agente>** maneja *<Proceso>*.` | `maneja` |
| instrumento | `*<Proceso>* requiere **<Instrumento>**.` | `requiere` |

Ejemplos:
```
**Persona** maneja *Preparar Cafe*.
*Preparar Cafe* requiere **Cafetera**.
```

## Enlaces de control

| Tipo | Plantilla | Verbo canónico opforja |
|------|-----------|------------------------|
| evento | `**<Objeto>** \`<estado>\` inicia *<Proceso>*.` | `inicia` |
| condicion | `*<Proceso>* ocurre si **<Objeto>** esta en \`<estado>\`.` | `ocurre si` |
| condicion de existencia | `*<Proceso>* ocurre si **<Objeto>** existe.` | `ocurre si … existe` |
| excepcion sobretiempo | `*<Manejo>* ocurre si duracion de *<Fuente>* excede <valor> <unidad>.` | `ocurre` + cota EX1 |
| excepcion subtiempo | `*<Manejo>* ocurre si duracion de *<Fuente>* es menor que <valor> <unidad>.` | `ocurre` + cota EX2 |
| invocacion | `*<Proceso-A>* invoca *<Proceso-B>*.` | `invoca` |
| autoinvocacion | `*<Proceso>* se invoca a si mismo.` | `invoca` / autoinvocacion |

Ejemplos:
```
**Solicitud** `pendiente` inicia *Resolver Solicitud*.
*Resolver Solicitud* ocurre si **Expediente** existe.
*Manejar Excepcion* ocurre si duracion de *Procesar* excede 5 minutos.
*Diagnosticar* invoca *Pedir Examen*.
```

## Enlaces estructurales

### Agregacion-participacion

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| simple | `**<Todo>** consta de **<Parte1>**, **<Parte2>**, ..., **<ParteN>**.` | `consta de` |
| con multiplicidad | `**<Todo>** consta de <N> **<Parte>**.` | `consta de` |

Ejemplo: `**Cafe Bebida** consta de **Liquido** y **Aroma**.`

### Generalizacion-especializacion

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| singular | `**<Especifico>** es un **<General>**.` | `es un` / `es una` |
| plural | `**<Especifico1>**, **<Especifico2>** y **<EspecificoN>** son **<General>**.` | `son` |
| XOR | `**<General>** puede ser **<Espec1>** o **<Espec2>**.` | `puede ser` |

Ejemplos:
```
**Auto** es un **Vehiculo**.
**Auto**, **Camion** y **Bus** son **Vehiculo**.
**Vehiculo** puede ser **Auto** o **Camion**.
```

### Clasificacion-instanciacion

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| simple | `**<Instancia>** es una instancia de **<Clase>**.` | `es una instancia de` |

Ejemplo: `**Chile** es una instancia de **Pais**.`

### Exhibicion-caracterizacion

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| simple | `**<Exhibidor>** exhibe **<Atributo1>**, **<Atributo2>**, ..., **<AtributoN>**.` | `exhibe` |

Ejemplo: `**Paciente** exhibe **Edad**, **Sexo** y **Diagnostico**.`

## Enlace estructural etiquetado

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| sin etiqueta | `**<Origen>** se relaciona con **<Destino>**.` | `se relaciona con` |
| con etiqueta | `**<Origen>** <etiqueta> **<Destino>**.` | etiqueta como verbo |

## Refinamiento entre OPDs

| Hecho | Plantilla | Verbo canónico opforja |
|-------|-----------|------------------------|
| descomposicion | `*<Proceso>* se descompone en *<Sub1>*, *<Sub2>*, ..., *<SubN>*.` | `se descompone` |
| despliegue | `**<Cosa>** se despliega en **<Ref1>**, **<Ref2>**, ..., **<RefN>**.` | `se despliega` |

## Operadores logicos en fans de enlaces

| Tipo | Plantilla |
|------|-----------|
| AND | `*<Proceso>* consume **<Obj1>** y **<Obj2>**.` |
| OR | `*<Proceso>* consume **<Obj1>** o **<Obj2>**.` |
| XOR | `*<Proceso>* consume exactamente uno de **<Obj1>** o **<Obj2>**.` |

## Sub-modelo (composicion inter-modelo)

| Hecho | Plantilla |
|-------|-----------|
| uso | `*<Proceso>* requiere **<Sub-Modelo>**.` |
| referencia externa | `**<Cosa-Externa>** esta referenciada desde **<Sub-Modelo>**.` |

## Reglas de surface form

1. **Capitalizacion**: nombres propios (cosas, procesos) en title case. Conectores en minuscula.
2. **Tipografia**: objetos en **negrita**, procesos en *cursiva*, estados en \`backticks\`. La tipografia es portadora de tipo; sin ella el parser no distingue objeto de proceso.
3. **Plurales**: `consume Agua y Cafe Molido` (and-fan), nunca `consume Aguas y Cafes Molidos`.
4. **Puntuacion**: cada sentencia termina en punto. Una sentencia por hecho.
5. **Idioma**: prosa de la skill en espanol. Sentencias OPL en espanol por defecto. Si el usuario pide OPL-EN explicitamente, traducir manteniendo equivalencia semantica.
6. **Nombres de cosas**: identicos en OPD y OPL-ES. Si el OPD dice `Hacer Cafe`, OPL-ES dice `Hacer Cafe`.

## Invariantes de equivalencia (roundtrip)

Tomados de `spec-forja-opl-es`:

1. **Roundtrip generacion→parseo**: toda oracion OPL emitida debe poder parsearse de vuelta al mismo hecho del modelo.
2. **Roundtrip parseo→generacion**: todo hecho parseado desde OPL debe poder regenerar la misma oracion OPL (modulo normalizaciones canonicas de presentacion).
3. **No ambiguedad**: el parser no debe crear entidades plausibles ante ambiguedad; debe rechazar o pedir desambiguacion.
4. **Display-vs-canonico**: distinguir entre la forma visible de una oracion (presentacion) y su forma canonica normalizada (equivalencia).

## GAPs documentados y divergencias canonicas

Conocer estas brechas evita prometer roundtrip donde `spec-forja-opl-es` lo declara parcial:

1. `spec-forja-opl-es` §1.4 declara divergencias entre la familia Forja y capas base: `se pliega` y `se recompone` pertenecen al enum por `reglas §4.3`, aunque no esten en `opm-opl-es §2`; las designaciones de estado no son verbos del enum.
2. `spec-forja-opl-es` §20 consolida GAPs: `varia de ... a`, `es de tipo`, `puede ser` XOR, `se refina`, `se pliega`, `se recompone`, `se relaciona con`/tags, `se descompone`, fan `m de f` y composicion de predicados tienen cobertura parcial o ausente.
3. Una entrada GAP-* puede ser canon textual, pero no debe presentarse como salida importable roundtrip de deep-opm-pro hasta cerrar generador, parser y fixture.

Estas brechas son deuda trazada, no permiso para inventar sinonimos ni para usar verbos fuera del enum cerrado.

## Cuando consultar la SSOT directa

Cualquier sentencia que no encaja en las plantillas anteriores requiere consulta directa a:
- `urn:fxsl:kb:reglas-opm-estrictas-es` si esta en juego validez, severidad o extension.
- `urn:fxsl:kb:spec-forja-opl-es` si esta en juego vocabulario, plantilla, parseo o roundtrip.
- `urn:fxsl:kb:spec-forja-opd-es` si la sentencia debe corresponder a una realizacion visual concreta.
- `urn:fxsl:kb:opl-es` solo como capa base delegada por la spec Forja.

Las plantillas son el subset operativo, no el lenguaje completo.
