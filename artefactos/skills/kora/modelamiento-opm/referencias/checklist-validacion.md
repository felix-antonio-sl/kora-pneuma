# Checklist de validacion — reglas prescriptivas + anti-patrones + heuristicas

Validacion en niveles operativos segun el corpus OPM/Forja SSOT ES. Cada nivel cita su capa propietaria y severidad. La autoridad primaria es `urn:fxsl:kb:reglas-opm-estrictas-es`; `spec-forja-opd-es`, `spec-forja-opl-es`, `metodologia-forja-opm-es` y `opm-categorial-es` completan modalidad, metodo y lectura formal. Las capas base se usan solo por delegacion.

## Nivel 0 — Anti-patrones canonicos (politica AP-* especifica)

30 anti-patrones de `reglas-opm-estrictas-es` §11. No todos tienen la misma accion: aplicar la politica de la tabla maestra (bloqueo, reporte, supresion, o no-canonizado/extension declarada). Referencia completa en `referencias/anti-patrones-opforja.md`.

| AP-NN | Construccion no-canonica | Politica |
|-------|--------------------------|-------------------|
| AP-01 | Resultado + modificador `c` | DEBE bloquearse: resultado pertenece a Post(P) |
| AP-02 | Resultado + modificador `e` | DEBE bloquearse: resultado no puede ser disparador |
| AP-03 | Abanico XOR/OR de resultado + `c` o `e` | DEBE bloquearse: hereda AP-01/AP-02 |
| AP-04 | Resultado conectado a estado inicial | DEBE bloquearse por V-8 |
| AP-05 | Agente conectado a robot, software, IA o maquina | DEBE bloquearse: agente = humano |
| AP-06 | Consumo o resultado en contorno exterior de proceso descompuesto | DEBE bloquearse por V-37, V-103 |
| AP-07 | Efecto entrada-salida sin escision al descomponer | DEBE bloquearse por V-40, V-110 |
| AP-08 | Enlace escindido TS4/TS5 + `c` o `e` | DEBE bloquearse por V-41, V-110 |
| AP-09 | `c` o `e` sobre enlace estructural | DEBE bloquearse: estructural es invariante temporal |
| AP-10 | `c` o `e` sobre invocacion | DEBE bloquearse: la invocacion es familia autonoma |
| AP-11 | Bidireccional o reciproco con estado solo en destino | DEBE bloquearse por V-30 |
| AP-12 | Estados de proceso | DEBE bloquearse: OPM reserva estados para objetos |
| AP-13 | Refinamiento con un solo subproceso o refinador | DEBE bloquearse en cierre/export canonico |
| AP-14 | Duplicar estados para evitar inicial+final simultaneo | DEBE bloquearse como sinonimo falso |
| AP-15 | Instancia visual entre tipos distintos | DEBE bloquearse por V-102 |
| AP-16 | Refinamiento ciclico transitivo | DEBE bloquearse por V-100 |
| AP-17 | `SDx.y` como identificador estable externo | DEBE bloquearse por V-247–V-249 |
| AP-18 | Modificar referencia externa en modelo consumidor | DEBE bloquearse por V-184 |
| AP-19 | Sombra decorativa en cosa informacional | DEBE suprimirse en canon-diagrama por V-124 |
| AP-20 | Triangulo estructural sin topologia interna requerida | DEBE bloquearse por V-128 |
| AP-21 | Evento sistemico cruzando frontera de descomposicion | DEBE bloquearse por V-38 |
| AP-22 | Sinonimos multiples para la misma cosa | DEBE reportarse por violar unicidad nominal |
| AP-23 | Truncamiento silencioso de rotulo en export canonico | DEBE bloquearse por V-194, V-212 |
| AP-24 | Reutilizar canales semanticos para UI/validacion | DEBE bloquearse por V-198, V-203, V-220, V-224 |
| AP-25 | Proceso explicito para soporte/mantenimiento sin esfuerzo | DEBE reportarse como mala clasificacion metodologica |
| AP-26 | Objeto transiente creado y consumido sin observacion | DEBE reportarse como objeto artificial |
| AP-27 | Evento a subproceso intermedio sin justificar omision previa | DEBE bloquearse si previos no son opcionales |
| AP-28 | `c` y `e` simultaneos sobre el mismo enlace | NO CANONIZADO (R-ZNC-1) |
| AP-29 | Enlaces heredados dibujados como explicitos | DEBE bloquearse salvo vista derivada no nuclear |
| AP-30 | Resultado+resultado o consumo+consumo al recomponer | DEBE bloquearse por V-43 |

## Nivel 1 — Reglas prescriptivas operativas (CRITICO)

Reglas ejecutables de `reglas-opm-estrictas-es`. Cada regla cita su fuente.

### Ontologia de entidades

- [ ] **R-COSA-1**: solo objetos y procesos son cosas. Sin "entidades", "nodos", "actores".
- [ ] **R-COSA-2**: perseverancia inferida del tipo (objeto=persistente, proceso=transitoria).
- [ ] **R-COSA-3**: el estado NO es una cosa. Es situacion de un objeto.
- [ ] **R-OBJ-1**: objeto representa cosa con existencia fisica o informacional potencial.
- [ ] **R-OBJ-2**: objeto con/sin estados; sin estados solo puede crearse o consumirse.
- [ ] **R-OBJ-3**: cada objeto tiene esencia (fisica/informacional) y afiliacion (sistemica/ambiental).
- [ ] **R-OBJ-5**: default de esencia no sobrescribe esencia explicita.
- [ ] **R-OBJ-6**: atributos de objetos ambientales deben ser ambientales.
- [ ] **R-OBJ-7**: procesos ejecutados por cosas ambientales = procesos ambientales.
- [ ] **R-PROC-1**: un proceso transforma uno o mas objetos.
- [ ] **R-PROC-2**: todo proceso explicito no persistente debe transformar al menos un objeto.
- [ ] **R-PROC-2A**: proceso persistente solo cierra si declara objeto afectado e invariancia neta.
- [ ] **R-PROC-4**: OPM no admite estados de proceso ("iniciado", "en proceso", "terminado").
- [ ] **R-PROC-5**: proceso persistente canonico solo si temporalidad/esfuerzo/condicion son hecho de modelo.
- [ ] **R-PROC-6**: proceso persistente no debe usarse para eludir cierre transformador.

### Nombres validos

- [ ] **R-NOM-OBJ-1**: nombre de objeto = sustantivo singular con palabras lexicas capitalizadas.
- [ ] **R-NOM-OBJ-2**: objeto plural = sufijo **Conjunto** (inanimados) o **Grupo** (humanos).
- [ ] **R-NOM-PROC-1**: nombre de proceso comienza con infinitivo o nominalizacion.
- [ ] **R-NOM-PROC-2**: 2 a 4 palabras, salvo termino de dominio registrado.
- [ ] **R-NOM-PROC-3**: palabras lexicas capitalizadas; articulos/preposiciones en minuscula.
- [ ] **R-NOM-EST-1**: nombre de estado en minusculas, forma pasiva o descriptiva.

### Estados

- [ ] **R-EST-1**: estado existe solo dentro de su objeto propietario (V-4).
- [ ] **R-EST-2**: designaciones validas: inicial (borde grueso), final (doble borde), default (flecha diagonal), Current (pin). Default unico por entidad.
- [ ] **R-EST-3**: estado puede ser inicial y final simultaneo. No duplicar.

### Instancias y ejecucion

- [ ] **R-INS-1**: toda cosa en modelo conceptual implica >=1 instancia operacional.
- [ ] **R-INS-2**: distinguir instancia visual (misma cosa, otra apariencia) de instancia logica (clasificacion-instanciacion).
- [ ] **R-EJEC-7**: durante simulacion, enlace con `c` se evalua antes de transiciones; si falla, proceso se omite (bypass), no espera.
- [ ] **R-EJEC-8**: multiples condiciones de entrada = AND para ejecutar, OR para omitir.
- [ ] **R-EJEC-9**: tras proceso con invocacion explicita, runtime toma el invocado como siguiente paso.

### Zonas no canonizadas (R-ZNC-1/2)

- [ ] Combinacion `c + e` sobre el mismo enlace: NO CANONIZADA (AP-28).
- [ ] Enlace probabilistico sin fan: no tiene canonicidad.
- [ ] Etiquetas de ruta sobre enlaces habilitadores: no canonizadas sobre agente/instrumento.

## Nivel 2 — Checklist de cierre OPD↔OPL (Anexo A)

12 gates ejecutables de `reglas-opm-estrictas-es` Anexo A. Falla en cualquier gate ALTO → bloqueo.

| Gate | Regla | Falla si | Severidad |
|------|-------|----------|-----------|
| Identidad | Cada cosa, estado, enlace y OPD con identidad persistente | se usa `SDx.y` como unico identificador externo | Alta |
| Firma | Cada enlace respeta familia, direccion y tipos de extremos | procedural conecta objeto-objeto, structural conecta estado, invocacion toca objeto | Alta |
| Estado | Todo estado con objeto propietario y designaciones validas | estado flotante, doble default, Current runtime serializado como designacion | Alta |
| OPL | Todo hecho nuclear visible emite plantilla OPL-ES canonica | forma visual persistente sin plantilla ni metadato de vista | Alta |
| Parseo | Toda oracion OPL aceptada reconstruye el mismo hecho | el parser crea entidades plausibles ante ambiguedad | Alta |
| Modificadores | `c/e` solo en input-side canonico | resultado, estructural, invocacion o TS4/TS5 reciben `c/e` | Alta |
| Refinamiento | OPD hijo agrega detalle motivado, no contradice al padre | replica layout, crea ciclo, cambia nombre/esencia/perseverancia | Alta |
| Distribucion | Al descomponer, enlaces del padre migran segun V-103/V-104/V-105 | consumo/resultado quedan en contorno exterior | Alta |
| Vistas | Vistas, Bring, sub-modelos y requirement views tipificados | vista se confunde con OPD jerarquico ordinario | Media |
| UI | Handles, overlays, grid, tutorial, validacion y runtime separados del canon | canal UI reutiliza contorno, sombra, piruleta, triangulo o halo semantico | Alta |
| Export | Todo perfil de export declara canon-diagrama/canon-documento | captura raster como prueba de canonicidad | Media |
| Deuda | Toda zona no canonizada registrada como extension, bloqueo o deuda explicita | se acepta silenciosamente construccion sin soporte SSOT | Alta |

## Nivel 3 — Realizacion visual (`spec-forja-opd-es` + base delegada `opd-es`)

Subset critico sobre las 263 reglas V-*. Para cada validacion, cita la regla.

### V-0 a V-10 (gramatica base)

- [ ] **V-1**: cada cosa tiene exactamente uno de `objeto` o `proceso` como tipo.
- [ ] **V-2**: rectangulos rectos = objetos; rectangulos redondeados = procesos.
- [ ] **V-3**: estados son sub-rectangulos redondeados dentro de un objeto.
- [ ] **V-5**: enlaces tienen exactamente un origen y un destino.
- [ ] **V-7**: contornos respetan distintivos de esencia (fisica vs informatica).

### V-11 a V-30 (composicion de enlaces)

- [ ] **V-13**: enlaces procedurales conectan proceso ↔ (objeto | estado).
- [ ] **V-14**: enlaces estructurales conectan cosas del mismo perseverance.
- [ ] **V-18**: triangulos estructurales tienen hijos visibles.
- [ ] **V-25**: operadores logicos (AND/OR/XOR) en fans de enlaces respetan precedencia.

### V-100 a V-130 (refinamiento entre OPDs)

- [ ] **V-105**: arbol de in-zooming es aciclico.
- [ ] **V-110**: sub-procesos en in-zoom estan ordenados temporalmente (top-down por defecto).
- [ ] **V-115**: links del padre se preservan en el hijo (visibles o referenciados).
- [ ] **V-120**: unfolding mantiene una sola dimension por descomposicion.

### V-200 a V-263 (canon-diagrama, sub-modelo, requisitos)

- [ ] **V-242**: sub-model es el cuarto par canonico de refinamiento-abstraccion.
- [ ] **V-251**: clausura OPD↔OPL local; el modelo compuesto es DAG.
- [ ] **V-252**: cada cosa cross-model tiene URI persistente.

## Nivel 4 — Semantica base delegada (`opm-es`, bajo reglas Forja)

### Clases de cosas

- [ ] cada cosa pertenece a `objeto`, `proceso` o `estado`. Sin clases inventadas.
- [ ] esencia (fisica/informatica) declarada para cada cosa donde aplique.
- [ ] `agent` es humano u organizacion; nunca maquina. Las maquinas son `instrument`.

### Clases de relaciones

- [ ] enlaces estructurales: `agregacion-participacion`, `generalizacion-especializacion`, `clasificacion-instanciacion`, `exhibicion-caracterizacion`.
- [ ] enlaces procedurales transformadores: `consumption`, `result`, `effect`.
- [ ] enlaces procedurales habilitantes: `agent`, `instrument`.
- [ ] enlaces de control: `condition`, `event`, `exception`, `invocation`.

### Principios

- [ ] **principio de unicidad**: una sola modalidad por hecho.
- [ ] **principio de minimalidad**: dos cosas indistinguibles = misma cosa.
- [ ] **principio de teorema objeto-proceso**: toda cosa es objeto o proceso, no ambos.

## Nivel 5 — Heuristicas operativas (`metodologia-forja-opm-es` A5 + A8)

### Claridad (cognitive load)

- [ ] cada OPD tiene **≤ 20-25 entidades** (Metodologia Forja A4.2/A8.1).
- [ ] cada OPD tiene **un proceso central distinguible**.
- [ ] enlaces no se cruzan innecesariamente.
- [ ] etiquetas legibles, sin truncar.

### Completitud (cobertura del proposito)

- [ ] el modelo expresa **estructura** (que cosas hay y como se relacionan).
- [ ] el modelo expresa **comportamiento** (como cambian las cosas en el tiempo).
- [ ] el modelo expresa **funcion** (para que sirve el sistema).
- [ ] cada cosa relevante para el proposito esta presente en algun nivel del modelo.

### Bimodalidad efectiva

- [ ] cada hecho del OPD tiene su sentencia OPL-ES correspondiente.
- [ ] cada sentencia OPL-ES tiene su realizacion grafica en algun OPD.
- [ ] no hay hechos solo-OPD (graficos sin OPL).
- [ ] no hay hechos solo-OPL (sentencias sin grafico).

### Equivalencia funcional y composicion (reglas Anexo C)

- [ ] **R-CAT-EQ-2**: realizaciones hermanas comparables comparten firma de frontera para declararse funcionalmente equivalentes.
- [ ] **R-CAT-EQ-3**: toda descomposicion in-zoom preserva la firma de frontera del proceso abstracto out-zoom.
- [ ] **R-CAT-LIN-2**: objetos lineales no son consumidos por mas de un proceso sin XOR.
- [ ] **R-CAT-COMP-1**: composicion de modelos no duplica entidades compartidas ni deja referencias colgantes.

### Validacion continua (A8)

- [ ] bimodalidad activa: tras cada edicion, leer la oracion OPL generada.
- [ ] simulacion conceptual como compuerta de flujo antes de cualquier computo.
- [ ] validacion por niveles: fragmentos/OPDs criticos primero, luego escenarios de sistema.
- [ ] ledger de investigacion (modo reverse/MBRSE): que requisito explica, que estructura satisface, que hecho quedo sin explicacion, que prediccion sale de la brecha.

## Reporte de validacion

Formato sugerido:

```
Reporte de validacion — <nombre del modelo> — <fecha>

Anti-patrones canonicos: X detectados
  ✗ AP-05: Robot declarado como agente — debe ser instrumento

Reglas prescriptivas (reglas-opm-estrictas-es): X/Y pasan
  ✗ R-PROC-2: proceso "Supervisar" sin transformee identificado

Checklist cierre OPD↔OPL (Anexo A): X/Y gates pasan
  ✗ Gate Identidad: OPD "SD1.2" usado como identificador externo

Capa visual (spec-forja-opd-es + opd-es delegado): X/Y pasan
  ✗ V-105: ciclo detectado entre in-zoom

Capa semantica (reglas Forja + opm-es delegado): X/Y pasan
  ✗ Cafetera declarada como agent

Heuristicas (Forja A5+A8): X/Y pasan
  ⚠ SD1.2 tiene 27 entidades (>25, recomienda simplificar)
  ✓ bimodalidad efectiva sostenida
  ✓ equivalencia funcional horizontal/vertical verificada
```

Si un AP-* con politica **DEBE bloquearse**, una regla prescriptiva CRITICAL, o un gate Alta falla -> `validar-modelo` retorna fail, vuelve a `refinar-modelo`.
Si solo fallan WARN/heuristicas → entregable pero con anotacion de tradeoffs.
