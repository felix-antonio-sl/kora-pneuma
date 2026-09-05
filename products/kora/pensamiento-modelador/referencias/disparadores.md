# Disparadores — síntoma de decisión trabada → capa / tensión

Mapa operativo. La SSOT son las 52 tensiones del kb
`urn:fxsl:kb:tensiones-modelamiento`. Esta tabla solo orienta la entrada.

| Síntoma del operador | Capa | Tensión(es) a consultar |
|---|---|---|
| "no sé si esto es una cosa o algo que pasa" | A | Entidad ↔ Evento |
| "no sé si modelar la clase o el caso concreto" | A | Token ↔ Type; General ↔ Particular |
| "esto se conecta con aquello pero no sé cómo" | A | Todo ↔ Partes; Causa ↔ Efecto; Agente ↔ Paciente |
| "¿esto cambia o se queda quieto?" | A | Estático ↔ Dinámico; Instantáneo ↔ Durativo |
| "no sé si esto lo sabemos o lo estamos asumiendo" | A | Hecho ↔ Supuesto; Conocido ↔ Desconocido |
| "¿lo dibujo o lo escribo? ¿cuánto detalle?" | A | Visual ↔ Textual; Detalle ↔ Abstracción |
| "modelo lo que es o lo que debería ser" | A | Prescriptivo ↔ Descriptivo |
| "no sé si incluir esto en el modelo" | B | Incluir ↔ Omitir; Ahora ↔ Después |
| "¿lo decido ya o sigo explorando?" | B | Compromiso ↔ Exploración |
| "¿por dónde empiezo, por la visión o por las piezas?" | B | Top-down ↔ Bottom-up |
| "el modelo está mal, ¿lo ajusto o lo rehago?" | B | Refinar ↔ Reestructurar |
| "pasó los checks pero algo no convence" | B | Verificar ↔ Validar; Modelo ↔ Realidad |
| "¿cuándo paro?" | B | Completar ↔ Entregar |
| "no sé cuánto rigor poner" | C | Tiempo ↔ Calidad; Tolerante ↔ Crítico |
| "¿esto es desechable o lo van a mantener?" | C | Temporal ↔ Permanente; Explorar ↔ Especificar |
| "¿quién va a consumir esto, gente o máquinas?" | C | Comunicar ↔ Computar |

Si el síntoma no cae en ninguna fila, recorrer las capas en orden A → B → C y
nombrar la primera tensión que la decisión activa.
