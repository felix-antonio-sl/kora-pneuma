# Catálogo de topologías S0–S9

Elegir la topología más pequeña que represente dependencias reales. El árbol de
gobierno y el DAG de trabajo son estructuras distintas.

## S0 — Monosession

```text
DIRECTORA: inspect → act → verify → finish
```

Usar para trabajo simple o serial, un escritor y poca integración.

## S1 — Directora con sidecar

```text
DIRECTORA ──TASK──> SIDECAR
DIRECTORA <─RESULT─ SIDECAR
```

Usar para documentación, inspección, log, hipótesis secundaria o test que no
bloquea el siguiente paso. Sin comunicación lateral.

## S2 — Estrella directora

```text
       DIRECTORA
      /    |    \
     A     B     C
      \    |    /
        síntesis
```

Usar para exploración, revisión por perspectivas, fuentes independientes o
secciones separables. La directora integra; los pares no se comunican.

## S3 — Pipeline

```text
A → B → C → D
```

Usar cuando cada etapa produce la entrada estable de la siguiente:
requisitos→arquitectura→implementación→verificación o
extracción→normalización→análisis→redacción. El traspaso puede ser directo;
la autoridad sigue en la directora.

## S4 — Torneo de hipótesis

```text
          PROBLEMA
        /    |    \
       A     B     C
        \    |    /
       ADJUDICADORA
```

Usar para debugging causal, diagnóstico diferencial, demostraciones,
creatividad o crítica adversarial. A/B/C no se comunican antes de entregar.
Después puede existir una ronda dirigida de `CHALLENGE`.

## S5 — Árbol jerárquico

```text
          DIRECTORA
          /       \
     SUPERV A    SUPERV B
      /   \          \
     A1   A2          B1
```

Usar para dominios completos o descomposición recursiva natural. Cada
supervisora recibe frontera, integra su subárbol y devuelve un resultado
reducido. Parent↔child por defecto; cross-branch solo por arista explícita.

## S6 — DAG contractual

```text
ARQUITECTURA → IMPLEMENTACIÓN → VERIFICACIÓN
       \            ↑
        └→ DATOS ───┘
```

Usar para ingeniería con dependencias cruzadas y contratos estables. Mensajes
laterales solo como `CONTRACT`, `EVIDENCE`, `RESULT` o `CHALLENGE`. Si la
comunicación se vuelve continua, fusionar nodos o volver a pipeline.

## S7 — Map-reduce

```text
CORPUS → MAPPER 1 ┐
       → MAPPER 2 ├→ REDUCER → AUDITOR
       → MAPPER N ┘
```

Usar para corpus, auditoría masiva o clasificación. Mappers no se comunican y
devuelven el mismo schema. El reducer sintetiza; el auditor desafía.

## S8 — Evaluador–optimizador

```text
BASELINE → OPTIMIZADOR → CANDIDATO → EVALUADOR FIJO
              ↑                 keep | revert
              └───────────────────────┘
```

Exige baseline, métrica objetiva, superficie mutable acotada, evaluador
inmutable, rollback, presupuesto y criterio keep/revert. El optimizador no
puede modificar el oráculo.

## S9 — Escritores federados

```text
              DIRECTORA
             /    |    \
       WRITER A WRITER B WRITER C
             \    |    /
              INTEGRADORA
```

Usar solo con interfaces estables, write sets explícitos y disjuntos, pruebas
de contrato e integrador único. La comunicación lateral se limita a dudas de
contrato. Aislar por workspace/worktree cuando las escrituras simultáneas
puedan interferir.

## Selección rápida

| Señal dominante | Base |
|---|---|
| Serial, un escritor | S0 |
| Un apoyo no bloqueante | S1 |
| Perspectivas independientes | S2 |
| Dependencia estricta por etapas | S3 |
| Hipótesis rivales o creatividad | S4 |
| Descomposición recursiva | S5 |
| Contratos cruzados | S6 |
| Muchos lotes homogéneos | S7 |
| Métrica fuerte e iteración | S8 |
| Varios dominios de escritura disjuntos | S9 |

No combinar códigos por gusto. Declarar una topología base y las aristas
adicionales imprescindibles.
