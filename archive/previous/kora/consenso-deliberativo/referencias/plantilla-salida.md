# Plantilla de salida de la deliberación

Estructura obligatoria del entregable de `entregar`. Las ocho secciones son
fijas; su extensión escala al problema.

```markdown
# Deliberación: <título del problema>

## 1. Síntesis final

<síntesis consensuada>

<!-- Si no hubo consenso, sustituir la sección anterior por: -->
## 1. Mapa de disenso

| Posición | Sostenida por | Fundamento | Qué la resolvería |
|---|---|---|---|
| ... | ... | ... | evidencia o decisión X |

Decisión devuelta al operador (HITL).

## 2. Razonamiento consolidado

<propuestas iniciales, qué sobrevivió a la crítica, objeciones de la
refutación y cómo se resolvieron>

## 3. Aportes por experto

### <Experto 1> (<identidad>)
- <aporte atribuido>

### <Experto N> (<identidad>)
- <aporte atribuido>

## 4. Supuestos aceptados

| Supuesto | Levantado por | Por qué se acepta |
|---|---|---|
| ... | ... | ... |

## 5. Riesgos pendientes

| Riesgo | Levantado por | Severidad | Mitigación sugerida |
|---|---|---|---|
| ... | ... | ... | ... |

## 6. Incertidumbres

<qué no se sabe, qué evidencia falta y qué cambiaría la conclusión>

## 7. Confianza por experto

| Experto | Confianza | Justificación | Qué la subiría |
|---|---|---|---|
| ... | ... | ... | ... |

Nunca promediar: la divergencia de confianza es información.

## 8. Metadatos de la deliberación

- modo de realización: encarnación | orquestación
- ciclos de refutación ejecutados: <n> / máximo <max_ciclos>
- objeciones críticas resueltas: <n>
- objeciones menores registradas: <n>
- resultado: consenso | disenso estructurado
```

## Criterios de calidad

- Toda afirmación central de la síntesis se rastrea a un aporte atribuido o a
  la resolución explícita de una objeción.
- Supuestos y riesgos no quedan vacíos en un problema no trivial; su ausencia
  es señal de consenso de cortesía.
- Si las confianzas divergen, las incertidumbres explican qué ve el experto
  menos confiado que los demás no ven.
