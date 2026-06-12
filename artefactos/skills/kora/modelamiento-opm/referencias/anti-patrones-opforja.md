# Anti-patrones canonicos de opforja (AP-01 a AP-30)

Referencia operativa tomada de `urn:fxsl:kb:reglas-opm-estrictas-es` §11. Cada anti-patron conserva la politica exacta de la tabla maestra: algunos bloquean, otros se reportan, se suprimen del canon-diagrama o se clasifican como zona no canonizada/extension declarada. No elevar severidades por memoria.

## AP-01 a AP-10

| AP | Construccion no-canonica | Accion canonica |
|----|--------------------------|-----------------|
| AP-01 | **Resultado + modificador `c`** (sobre T2/TS2). Resultado pertenece a Post(P), no puede ser precondicion. | Mover el control al lado de entrada: consumo, efecto, agente o instrumento condicional. |
| AP-02 | **Resultado + modificador `e`**. Resultado pertenece a Post(P), no puede ser disparador. | Colocar el evento sobre consumo, efecto, agente o instrumento. |
| AP-03 | **Abanico XOR/OR de resultado + `c` o `e`**. Cada enlace del fan sigue siendo resultado y hereda AP-01/AP-02. | Mover control al lado de entrada o usar fan probabilistico sin `c/e`. |
| AP-04 | **Resultado conectado a estado inicial** (V-8). | Conectar al rectangulo del objeto o a un estado no inicial. |
| AP-05 | **Agente conectado a robot, software, IA o maquina** (glosario 3.3). | Usar enlace de instrumento. Agente = humano con voluntad/responsabilidad. |
| AP-06 | **Consumo o resultado en contorno exterior de proceso descompuesto** (V-37, V-103). | Reasignar consumo al primer subproceso y resultado al ultimo subproceso. |
| AP-07 | **Efecto entrada-salida sin escision al descomponer** (V-40, V-110). | Reemplazar por TS4 en subproceso temprano y TS5 en subproceso tardio. |
| AP-08 | **Enlace escindido TS4/TS5 (par acoplado) + `c` o `e`** (V-41, V-110). No aplica a ETS3/ETS4 standalone. | Modelar opcionalidad sobre el efecto entrada-salida completo o con control externo. |
| AP-09 | **`c` o `e` sobre enlace estructural**. Los modificadores son procedimentales; estructural es invariante temporal. | Usar enlace estructural con estado especificado solo cuando la variante este definida. |
| AP-10 | **`c` o `e` sobre invocacion**. La invocacion es familia autonoma (R-INV-1A). | Usar nodo de decision booleano, fan de invocacion, u objeto booleano/condicion sobre proceso previo. |

## AP-11 a AP-20

| AP | Construccion no-canonica | Accion canonica |
|----|--------------------------|-----------------|
| AP-11 | **Bidireccional o reciproco con estado solo en destino** (V-30). | Usar unidireccional con estado en destino o agregar estado en origen. |
| AP-12 | **Estados de proceso**. OPM reserva estados para objetos. | Descomponer en subprocesos o usar atributo exhibido `Estado del Proceso`. |
| AP-13 | **Refinamiento con un solo subproceso o refinador**. | Eliminar, postergar o ampliar a >=2 hijos. |
| AP-14 | **Duplicar estados para evitar inicial+final simultaneo**. | Marcar el estado unico como inicial y final. |
| AP-15 | **Instancia visual entre tipos distintos** (V-102). | Usar apariencia del mismo tipo o clasificacion-instanciacion logica. |
| AP-16 | **Refinamiento ciclico transitivo** (V-100). | Romper el ciclo de refinamiento. |
| AP-17 | **`SDx.y` como identificador estable externo** (V-247–V-249). | Usar identificador persistente (URI/handle), no etiqueta de navegacion. |
| AP-18 | **Modificar referencia externa en modelo consumidor** (V-184). | Modificar en modelo propietario o crear cosa distinta. |
| AP-19 | **Sombra decorativa en cosa informacional** (V-124). | Reservar sombra a esencia fisica. |
| AP-20 | **Triangulo estructural sin topologia interna requerida** (V-128). | Renderizar triangulo interior o circulo interior segun relacion. |

## AP-21 a AP-30

| AP | Construccion no-canonica | Accion canonica |
|----|--------------------------|-----------------|
| AP-21 | **Evento sistemico cruzando frontera de descomposicion** (V-38). | Mover evento dentro de la descomposicion o reclasificar como ambiental. |
| AP-22 | **Sinonimos multiples para la misma cosa**. Viola unicidad nominal. | Elegir nombre canonico y mapear variantes de superficie. |
| AP-23 | **Truncamiento silencioso de rotulo en export canonico** (V-194, V-212). | Ajustar bounding box, layout o tamano antes de exportar. |
| AP-24 | **Reutilizar canales semanticos para UI/validacion** (V-198, V-203, V-220, V-224). | Usar canal visual reservado a UI. |
| AP-25 | **Proceso explicito para soporte/mantenimiento sin esfuerzo sostenido relevante**. | Usar enlace estructural etiquetado. |
| AP-26 | **Objeto transiente creado y consumido sin observacion intermedia**. | Usar enlace de invocacion. |
| AP-27 | **Evento a subproceso intermedio sin justificar omision previa**. Bloquea si previos tienen efectos obligatorios no omitibles. | Conectar al primer subproceso o declarar omision valida de previos. |
| AP-28 | **`c` y `e` simultaneamente sobre el mismo enlace**. NO CANONIZADO (silencio SSOT). | Clasificar como no canonizado. Modelar control externo explicito. |
| AP-29 | **Enlaces heredados dibujados como explicitos**. | Inferirlos por herencia desde generalizacion-especializacion. |
| AP-30 | **Resultado+resultado o consumo+consumo sobre el mismo objeto al recomponer** (V-43). | Corregir el nivel hijo antes de recomponer. |

## Zonas no canonizadas (R-ZNC-1/2)

Construcciones que no aparecen explicitamente prohibidas ni canonizadas por la SSOT. La skill debe clasificarlas como no canonizadas, no como prohibiciones.

| Zona | Estado |
|------|--------|
| Combinacion `c + e` sobre el mismo enlace | NO CANONIZADA (AP-28). Tratar como extension declarada. |
| Enlace probabilistico sin fan | `Pr=p` solo dentro de abanicos; fuera no tiene canonicidad. |
| Etiquetas de ruta sobre enlaces habilitadores | Solo canonizadas sobre consumo/resultado; no sobre agente/instrumento. |

## Uso en la skill

Cuando el modelo activo, un OPD, o un bundle presenta alguna de estas construcciones:
1. Citar el AP-NN y la regla propietaria en `reglas-opm-estrictas-es`; las citas V-* o SSOT-* son procedencia/base delegada, no autoridad primaria de la skill.
2. Aplicar la politica de la tabla maestra: bloquear solo cuando dice **DEBE bloquearse**; reportar o suprimir cuando dice **DEBE reportarse** o **DEBE suprimirse**.
3. Sugerir la accion canonica de la tabla.
4. Si la construccion cae en zona no canonizada (AP-28, o silencio SSOT): clasificar como no canonizada, permitir como extension declarada, no emitir como OPM nuclear.
