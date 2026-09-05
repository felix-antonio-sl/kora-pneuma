# Baseline auxiliar de smells inspirado en Fowler

Esta selección es una adaptación auxiliar del baseline incluido en
`mattpocock/skills` al commit
`2ab958093e83e0ec752e6c1c5932da465bf23e0c`; no es una reproducción literal ni
un canon exhaustivo de Martin Fowler. Usarla solo como heurística etiquetada.
Un estándar documentado del repositorio prevalece cuando acepta la forma
observada; una herramienta que ya impone la regla no produce un hallazgo de
smell. Cada smell responde a qué mirar y a una dirección de mejora, no a una
condena automática.

1. **Nombre misterioso (Mysterious Name)** — un nombre de función, variable o
   tipo no revela qué hace o qué contiene. → Renombrarlo; si no aparece un
   nombre honesto, revisar el diseño opaco.
2. **Código duplicado (Duplicated Code)** — la misma forma lógica aparece en
   más de un hunk o archivo del cambio. → Extraer la forma compartida y
   llamarla desde ambos lugares.
3. **Envidia de funcionalidad (Feature Envy)** — un método consulta más los
   datos de otro objeto que los propios. → Moverlo al objeto cuyos datos
   envidia.
4. **Grumos de datos (Data Clumps)** — los mismos campos o parámetros viajan
   juntos repetidamente. → Agruparlos en un tipo pequeño y pasar ese tipo.
5. **Obsesión por primitivos (Primitive Obsession)** — un primitivo o string
   representa un concepto de dominio que merece tipo propio. → Darle un tipo
   pequeño y explícito.
6. **Condicionales repetidos (Repeated Switches)** — el mismo `switch` o
   cascada de `if` sobre el mismo tipo se repite en el cambio. → Sustituirlo
   por polimorfismo o por un mapa compartido por ambos sitios.
7. **Cirugía a escopetazos (Shotgun Surgery)** — un cambio lógico obliga a
   editar muchos lugares dispersos del diff. → Reunir lo que cambia en un
   módulo.
8. **Cambio divergente (Divergent Change)** — un archivo o módulo se edita por
   varias razones no relacionadas. → Separarlo para que cada módulo cambie
   por una sola razón.
9. **Generalidad especulativa (Speculative Generality)** — se agregan
   abstracciones, parámetros o hooks para necesidades que la spec no tiene.
   → Eliminarlos y volver a inline hasta que exista una necesidad real.
10. **Cadenas de mensajes (Message Chains)** — navegación larga como
    `a.b().c().d()` que el llamador no debería conocer. → Ocultar el recorrido
    tras un método del primer objeto.
11. **Hombre de paja intermedio (Middle Man)** — una clase o función se limita
    casi por completo a delegar. → Eliminarla y llamar directamente al destino.
12. **Herencia rechazada (Refused Bequest)** — una subclase o implementador
    ignora o sobrescribe la mayor parte de lo heredado. → Retirar la herencia
    y usar composición.
