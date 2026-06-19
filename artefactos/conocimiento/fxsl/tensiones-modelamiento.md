---
urn: urn:fxsl:kb:tensiones-modelamiento
nombre: tensiones-modelamiento
version: 1.0.0
estado: publicado
descripcion: "Marco de las 52 tensiones del modelado de sistemas en tres capas anidadas (sustantivas, praxis, contexto): el mapa de decisiones que todo acto de modelado navega, agnostico al formalismo."
fuente: "Koraficado del documento del operador 'Tensiones del Modelamiento de Sistemas' v2.2 (2025-12-13); fuente humana externa, sin sha256."
autor: FS
creado: 2026-06-19
lang: es
tags: [tensiones-modelamiento, modelado-conceptual, praxis-de-modelado, metamodelado, decision-de-modelado, formalismo, mbse]
familia: bok
---

# Tensiones del Modelamiento

Todo acto de modelado —en cualquier formalismo— es **navegación de tensiones**:
decisiones entre dos polos, cada una con su pregunta. Este marco las nombra. Son
**52 tensiones** organizadas en **tres capas anidadas**:

```text
C: CONTEXTO     (condiciones que modulan)        12 tensiones
  B: PRAXIS     (cómo decide el modelador)       16 tensiones
    A: SUSTANTIVAS (qué debe decidirse)          24 tensiones
```

Las sustantivas (A) viven dentro de la praxis (B), que vive dentro del contexto (C).

## Clave de lectura

Un **formalismo es un sistema de resoluciones congeladas de las tensiones
sustantivas** (capa A): elige de antemano cómo resolver "objeto o evento",
"todo o partes", etc., y ofrece primitivas que encarnan esa elección. Las
tensiones de **praxis** (B) y de **contexto** (C) **no las resuelve ningún
formalismo**: las navega el modelador, nombrándolas. Ahí vive el juicio que
distingue a un experto en sintaxis de un experto en modelar.

El contexto (C) modula **profundidad, alcance y ritmo**; jamás la corrección. Un
modelo pequeño tiene derecho a ser menos profundo, no a estar mal formado.

---

## A. Tensiones sustantivas — qué debe decidirse (24)

### A1. Ser

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Entidad ↔ Evento | Persiste | Ocurre | ¿Es algo o sucede? |
| Concreto ↔ Abstracto | Material | Informacional | ¿Ocupa espacio? |
| Token ↔ Type | Este específico | Del tipo | ¿Instancia o clase? |
| Todo ↔ Partes | Agregado | Componentes | ¿Composición? |
| General ↔ Particular | Superclase | Subclase | ¿Generalización? |
| Simétrico ↔ Asimétrico | A↔B = B↔A | A→B ≠ B→A | ¿Recíproca? |

### A2. Devenir

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Estático ↔ Dinámico | Invariante | Cambiante | ¿Cambia? |
| Instantáneo ↔ Durativo | Punto | Intervalo | ¿Duración? |
| Secuencial ↔ Paralelo | En serie | Simultáneo | ¿Orden fijo? |
| Causa ↔ Efecto | Produce | Es producido | ¿Qué origina qué? |
| Agente ↔ Paciente | Actúa | Es afectado | ¿Quién a quién? |
| Determinista ↔ Probabilista | Certeza | Distribución | ¿Predecible? |

### A3. Conocer

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Conocido ↔ Desconocido | Tenemos info | Falta info | ¿Lo sabemos? |
| Cierto ↔ Incierto | Alta confianza | Duda | ¿Cuánta certeza? |
| Hecho ↔ Supuesto | Verificado | Asumido | ¿Confirmado? |
| Explícito ↔ Tácito | Declarado | Implícito | ¿Formalizado? |
| Situado ↔ Universal | Contextual | General | ¿Depende del caso? |
| AND ↔ OR ↔ XOR | Todos | Alguno / Uno | ¿Combinación? |

### A4. Expresar

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Visual ↔ Textual | Diagrama | Lenguaje | ¿Cómo se representa? |
| Formal ↔ Informal | Estricto | Libre | ¿Procesable? |
| Compacto ↔ Verboso | Denso | Explícito | ¿Economía? |
| Prescriptivo ↔ Descriptivo | Debe ser | Es | ¿Norma o realidad? |
| Detalle ↔ Abstracción | Fino | Grueso | ¿Cuánto zoom? |
| Modular ↔ Monolítico | Piezas | Bloque | ¿Separable? |

---

## B. Praxis — cómo decide el modelador (16)

Ningún formalismo decide esto. Lo navega el modelador.

### B1. Decidir

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Incluir ↔ Omitir | Agregar | Dejar fuera | ¿Es relevante? |
| Ahora ↔ Después | Resolver ya | Postergar | ¿Urgente? |
| Compromiso ↔ Exploración | Fijar | Mantener opciones | ¿Decido o exploro? |
| Regla ↔ Excepción | Adherir | Excepcionar | ¿Estricto? |

### B2. Comunicar

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Mi visión ↔ Compartida | Lo que yo sé | Lo acordado | ¿Refleja quién? |
| Experto ↔ Novato | Técnico | General | ¿Para quién? |
| Consenso ↔ Autoridad | Acuerdo | Decisión | ¿Cómo resuelvo? |
| Fidelidad ↔ Utilidad | Preciso | Práctico | ¿Exacto o suficiente? |

### B3. Proceder

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Top-down ↔ Bottom-up | Desde visión | Desde partes | ¿Por dónde empiezo? |
| Análisis ↔ Síntesis | Descomponer | Componer | ¿Separo o integro? |
| Planificar ↔ Improvisar | Diseñar antes | Descubrir | ¿Plan o emergente? |
| Refinar ↔ Reestructurar | Mejorar | Rehacer | ¿Ajusto o rehago? |

### B4. Validar

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Modelo ↔ Realidad | Coherente | Correspondiente | ¿Bien formado o representa? |
| Verificar ↔ Validar | Bien hecho | Correcto | ¿Cumple reglas o propósito? |
| Foco ↔ Contexto | Detalle | Visión general | ¿Zoom in o out? |
| Completar ↔ Entregar | Seguir | Terminar | ¿Cuándo suficiente? |

---

## C. Contexto — condiciones que modulan (12)

Modulan profundidad, alcance y ritmo. **Nunca la corrección.**

### C1. Recursos

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Tiempo ↔ Calidad | Rápido | Riguroso | ¿Prioridad? |
| Individual ↔ Colectivo | Solo | Equipo | ¿Quién modela? |
| Herramientas ↔ Manual | Software | Papel | ¿Con qué? |

### C2. Propósito

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Explorar ↔ Especificar | Descubrir | Documentar | ¿Fase? |
| Comunicar ↔ Computar | Humanos | Máquinas | ¿Quién consume? |
| Temporal ↔ Permanente | Desechable | Mantenible | ¿Vida útil? |

### C3. Dominio

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Conocido ↔ Novedoso | Familiar | Nuevo | ¿Sé del tema? |
| Estable ↔ Volátil | Cambia poco | Cambia mucho | ¿Frecuencia? |
| Simple ↔ Complejo | Pocos elementos | Muchos | ¿Escala? |

### C4. Cultura

| Tensión | Polo A | Polo B | Pregunta |
|---|---|---|---|
| Formal ↔ Informal | Estricto | Flexible | ¿Rigor? |
| Ágil ↔ Planificado | Iterativo | Fases | ¿Metodología? |
| Tolerante ↔ Crítico | Aproximaciones | Precisión | ¿Estándar? |

---

## Métricas

| Capa | Categorías | Tensiones |
|---|---|---|
| A: Sustantivas | 4 | 24 |
| B: Praxis | 4 | 16 |
| C: Contexto | 4 | 12 |
| **Total** | **12** | **52** |
