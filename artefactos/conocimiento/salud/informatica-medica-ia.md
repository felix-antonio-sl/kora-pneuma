---
urn: urn:salud:kb:informatica-medica-ia
nombre: informatica-medica-ia
version: 1.0.0
estado: publicado
descripcion: "Inteligencia Artificial en Salud: Aplicacion: prediccion de deterioro, readmisiones, sepsis"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/informatica-medica/ia-en-salud.md (sha256:9b930b98af22f77e073232e3f2940a7f3568da15b4aa879577dbd4ddc8a0023f) el 2026-06-12; cuerpo byte-fiel (renombrado de ia-en-salud.md a informatica-medica-ia.md por lugar-coincide). Fuente original: Bridging AI and Human Intelligence in Healthcare (Hubner et al, Springer 2026). INBOX/salud/"
autor: FS
creado: 2026-05-07
lang: es
tags: [salud, ia, cdss, machine-learning, nlp, etica-ia, implementacion]
familia: bok
cita: [urn:salud:kb:informatica-medica-indice]
---

# Inteligencia Artificial en Salud

## Principios de IA en salud

- **Machine Learning**: aprendizaje supervisado/no-supervisado.
 Aplicacion: prediccion de deterioro, readmisiones, sepsis.
- **Deep Learning**: redes neuronales multicapa. Aplicacion: imagenologia,
 dermatologia, patologia digital.
- **NLP (Natural Language Processing)**: extraccion de texto clinico.
 Aplicacion: codificacion automatica, extraccion de fenotipos, summarizacion.

## Clinical Decision Support Systems (CDSS)

Sistemas que asisten la decision clinica con conocimiento basado en evidencia.
Tipos:
- **Basados en conocimiento**: reglas if-then, arboles de decision, guias
- **Basados en datos**: modelos predictivos entrenados en datos historicos
- **Hibridos**: combinacion de ambos

### Desafios de implementacion

1. **Alerta fatiga**: exceso de alertas → el clinico las ignora todas.
 Solucion: estratificar por severidad, learning loop de dismissals.
2. **Integracion con EHR**: el CDSS debe operar dentro del flujo clinico,
 no como sistema externo.
3. **Explicabilidad**: el clinico necesita entender POR QUE el sistema
 recomienda algo (no solo que lo recomienda).
4. **Sesgo algoritmico**: datos de entrenamiento no representativos producen
 recomendaciones inequitativas.

## Etica y regulacion de IA en salud

- **EU AI Act**: clasifica sistemas de IA en salud como "alto riesgo"
- **FDA Software as Medical Device (SaMD)**: marco regulatorio para software
 que toma decisiones clinicas sin intervencion humana
- **Principios eticos**: transparencia, equidad, no maleficencia,
 responsabilidad, privacidad
- **Brecha digital**: la IA puede ampliar desigualdades si no se disena
 para poblaciones diversas

## Implementacion de proyectos de IA

Framework de implementation science aplicado a IA en salud:
1. Evaluacion de preparacion organizacional
2. Seleccion del problema clinico (no tecnologico)
3. Desarrollo con datos locales representativos
4. Validacion prospectiva (no solo retrospectiva)
5. Integracion en el flujo de trabajo (no como add-on)
6. Monitoreo continuo de desempeno y equidad
