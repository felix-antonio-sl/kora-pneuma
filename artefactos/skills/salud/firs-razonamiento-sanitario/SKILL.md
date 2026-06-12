---
urn: urn:salud:artefacto:firs-razonamiento-sanitario
nombre: firs-razonamiento-sanitario
version: 1.1.0
estado: activo
descripcion: "Skill para aplicar el Framework Integrado de Razonamiento en Salud como metodo operativo: separar escala micro/meso/macro, evitar falacia ecologica, distinguir evidencia clinica, poblacional y de gestion, y estructurar decisiones sanitarias."
fuente: "Sublimada el 2026-06-12 desde la bestia artifacts/skills/salud/firs-razonamiento-sanitario/SKILL.md v1.0.1 (sha256:2c80bff69df0ef69cee182107f0186a4a04463b0a95c8b9da75a6310c2815e37); payload YAML vertido a cuerpo Markdown (consolidacion salud, bump minor): metodo de razonamiento transversal citado por salubrista y los modos asistenciales; fibra referencias/ copiada byte-identica. Herramientas OpenClaw mapeadas al idiom estandar. Omitido con razon: target openclaw (GENESIS seccion 4)."
autor: FS
creado: 2026-04-27
lang: es
tags: [salud, razonamiento-sanitario, firs, escalas, falacia-ecologica, evidencia]
vector: [2, 1, 2, 0, 1]
sigma: [3, 3, 3, 2, 3]
arnes: disciplina
forma: habilidad
herramientas: [Read, Grep, Glob]
targets: [claude-code, codex, opencode]
estados: [fijar-escala, separar-niveles, identificar-evidencia, detectar-saltos-indebidos, proponer-puentes, decision-con-inferencia-controlada]
conocimiento: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-body-of-knowledge, urn:salud:kb:salubrista-fuentes-base-curadas, urn:salud:kb:salubrista-fuente-salud-publica-global, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:health-systems-science-fundamentos, urn:salud:kb:health-systems-science-operativa, urn:salud:kb:health-systems-science-indice, urn:salud:kb:gestion-redes-general, urn:salud:kb:gestion-redes-herramientas]
componible: [urn:salud:artefacto:salubrista, urn:salud:artefacto:hospitalista, urn:salud:artefacto:hospitalizacion-domiciliaria]
---

# firs-razonamiento-sanitario

## Propósito

Aplicar FIRS (Framework Integrado de Razonamiento en Salud) como método, no
como corpus de conocimiento. La skill controla la calidad inferencial de las
respuestas salubristas cuando una pregunta cruza clínica, epidemiología,
gestión, red, territorio o política: separa escalas micro/meso/macro, evita la
falacia ecológica, distingue evidencia clínica, poblacional y de gestión, y
estructura la decisión sanitaria.

La entrada esperada es una pregunta sanitaria con cruce de escala, inferencia o
decisión multinivel. Dominio: razonamiento sanitario, escala, inferencia,
epidemiología, gestión y sistemas. Permisos de lectura de KB; no usar la web
salvo que el agente principal requiera vigencia normativa o datos actuales.

## Cuándo usar

- Consulta que mezcla caso individual, población, red, establecimiento o
  política.
- Riesgo de falacia ecológica, extrapolación indebida o salto de escala.
- Necesidad de separar evidencia clínica, epidemiológica y operacional.
- Decisión sanitaria con incertidumbre, trade-offs o múltiples niveles.

## Workflow

### fijar-escala

Fijar la escala de la pregunta: individuo, equipo, unidad, establecimiento,
red, territorio, nacional o multi-escala. Es el estado inicial.

### separar-niveles

Separar los niveles y las capas lógicas:

- **micro**: caso clínico, diagnóstico, tratamiento, riesgo individual;
- **meso**: inferencia epidemiológica, población, causalidad, vigilancia;
- **macro**: gestión sanitaria, capacidad, gobernanza, calidad, política.

En cada nivel, distinguir las capas de Lillrank: social logic (normas, valores,
cultura), technical logic (efectividad clínica, variabilidad, calidad) y
economic logic (eficiencia, incentivos, sostenibilidad).

### identificar-evidencia

Identificar qué tipo de evidencia sostiene cada afirmación — clínica,
epidemiológica/poblacional u operacional/de gestión — y distinguir dato,
inferencia, decisión y recomendación antes de cruzar niveles.

### detectar-saltos-indebidos

Detectar saltos indebidos de nivel: falacia ecológica, extrapolación de caso,
paradoja de Simpson, causalidad no identificada o métricas fuera de contexto.

### proponer-puentes

Elegir el puente metodológico que el cruce de niveles requiere:

- **clinical epidemiology** para evidencia poblacional aplicada a decisión
  individual;
- **modelos multinivel** para población, territorio y red;
- **systems thinking** para interdependencias, feedback y efectos no
  intencionales;
- **management engineering** para hospitalista, capacidad, colas, variabilidad
  y forecast;
- **health systems science** para demanda/oferta, estratificación y acceso
  (`urn:salud:kb:health-systems-science-operativa`).

### decision-con-inferencia-controlada

Emitir la respuesta con supuestos, incertidumbre, evidencia usada y la decisión
humana requerida. Estado terminal: marco de escala, inferencias permitidas,
riesgos y puentes metodológicos.

## Reglas duras

1. No trasladar conclusiones poblacionales a individuos sin puente metodológico
   explícito.
2. No trasladar observaciones individuales a política o red sin agregación,
   contexto y sesgo declarado.
3. Distinguir dato, inferencia, decisión y recomendación.
4. Separar herramienta de marco: KPI, BSC, FODA, DES o QAT no reemplazan el
   juicio de sistema.
5. Declarar incertidumbre, supuestos, nivel temporal y unidad de decisión.

## Composición

Método de razonamiento transversal del namespace salud: lo cita el agente
`urn:salud:artefacto:salubrista` y lo invocan tanto las skills de gestión meso
como los modos asistenciales del agente medico-hospitalista
(asistencial-hospital y asistencial-hodom), a ambos lados de la frontera
micro-asistencial / meso-gestión que organiza la consolidación del namespace.

- Con `urn:salud:artefacto:salubrista`: controla la calidad inferencial de sus
  respuestas cuando cruzan clínica, epidemiología, gestión, red, territorio o
  política.
- Con `urn:salud:artefacto:hospitalista`: cuando hay salto de escala o mezcla
  de juicio clínico, poblacional, operacional o político en problemas de flujo
  y capacidad.
- Con `urn:salud:artefacto:hospitalizacion-domiciliaria`: cuando la escala no
  está clara o la respuesta mezcla decisión clínica, gestión y política
  sanitaria.

## Salidas

- Marco de escala y nivel de análisis.
- Separación micro/meso/macro.
- Puentes metodológicos requeridos.
- Riesgos de inferencia.
- Preguntas de verificación antes de recomendar.

## Compromisos

Transparencia inferencial: toda respuesta declara incertidumbre, supuestos,
nivel temporal, unidad de decisión y la decisión humana requerida; las
inferencias permitidas y los riesgos quedan explícitos.

## Recursos

### Referencias

- `referencias/firs-framework-integrado.source.txt`: fuente completa legacy del
  marco FIRS, preservada como evidencia no indexada (copiada byte-idéntica
  desde la bestia). No cargarla completa salvo que se requiera auditar una
  regla, concepto o sección específica.
