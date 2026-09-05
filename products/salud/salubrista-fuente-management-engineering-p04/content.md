---
urn: urn:salud:kb:salubrista-fuente-management-engineering-p04
nombre: salubrista-fuente-management-engineering-p04
version: 1.0.0
estado: publicado
descripcion: "healthcare management engineering - Parte 04"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/fuentes/management-engineering-sanitario--p04.md (sha256:bfe24c9697e52a8a84e6bd8de1c14f7863a6423c9853d8dd2e22208c4118274b) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:salubrista-fuente-management-engineering."
autor: FS
creado: 2026-04-10
lang: es
tags: [salubrista, fuente, gestion-sanitaria, management-engineering, capacidad, colas, simulacion]
familia: fuente
depende: [urn:salud:kb:salubrista]
cita: [urn:salud:kb:salubrista-fuente-management-engineering]
---

# healthcare management engineering - Parte 04

## 6.1 Fair Distribution of Savings Between Cooperating Providers
- [P244] **HECHO** — hospitales: numerosos conflictos interés departamentos (ED↔ICU transferencia rápida vs capacidad; unidad prolonga stay vs otras quieren alta)
- [P245] **DEFINICIÓN** — payment bundling (reforma 2010): pago único organización cubriendo hospital + grupo médicos + SNF + HHA; organización asigna pagos y gain-sharing
- [P246] **HECHO** — bypass cardíaco bundled: Hospital $15K, Grupo Médicos $8K, SNF $6K, HHA $3K (total $32K); Medicare -13% → $4,160 ahorros distribuir
- [P247] **HECHO** — división igual $4,160/4 = $1,040 — injusta contribución difiere
- [P248] **HECHO** — proporcional costo: Hospital $1,950, PG $1,040, SNF $780, HHA $390 — desalienta participantes pequeños
- [P249] **DEFINICIÓN** — Shapley value = asignación justa ganancias/ahorros colectivos; miembro k compensado proporcional contribución marginal V(s)-V(s-k) promediada todos órdenes formación coalición
- [P250] **DEFINICIÓN** — coalición s = grupo cooperando; gran coalición S = todos; V(s) = valor coalición; Shapley promedia contribuciones marginales todos ordenamientos
- [P251] **REGLA** — incentivo permanecer coalición: (1) racionalidad individual — costo miembro < standalone; (2) racionalidad subgrupo — costo subgrupo < suma standalone; (3) distribución completa
- [P252] **DEFINICIÓN** — core = asignaciones satisfaciendo racionalidad individual + subgrupo; core no vacío → Shapley satisface; Shapley calculable core vacío
- [P253] **HECHO** — Shapley bypass 4 participantes: Hospital $1,598 (10.7%), PG $1,000 (12.5%), SNF $953 (15.9%), HHA $608 (20.3%); core no vacío
- [P254] **HECHO** — Shapley asigna mayor % ahorros participantes menor costo (SNF, HHA) vs proporcional → alienta cooperación
- [P255] **REGLA** — Shapley value = mejor enfoque asignación justa costos/ganancias sistemas economías escala no lineales o socios cooperativos
- [P256] **ALCANCE** — game theory aplica: bundled payment, ahorros recursos pooled, costos quirúrgicos con colas, centros diagnóstico/quirúrgicos conjuntos

## Core Principles
- [P257] **REGLA** — recursos pooled (intercambiables) más eficientes que dedicados misma capacidad/carga en wait time y throughput → `pooled resources`
- [P258] **REGLA** — recursos especializados requeridos (privacidad, infecciones, equipo fijo): planificar capacidad adicional compensar pérdida eficiencia
- [P259] **REGLA** — recursos especializados cuestan más que pooled intercambiables
- [P260] **REGLA** — variabilidad llegadas/servicio requiere capacidad reservada (hasta 40%) evitar problemas regulares
- [P261] **REGLA** — mayor aleatoriedad → menor rendimiento (cola mayor, wait mayor, utilización menor)
- [P262] **REGLA** — reducción variabilidad proceso = clave mejora patient flow, throughput, reducir delays
- [P263] **REGLA** — hospitales grandes siempre mejor performance que pequeños mismo ratio → `economies of scale`
- [P264] **REGLA** — benchmarking lineal/ajustes proporcionales misguided si efecto escala no considerado
- [P265] **⚠ TENSIÓN** — mayor utilización (bueno organización) → mayor wait (malo pacientes); utilización >80-85% → aumento significativo wait
- [P266] **REGLA** — workload leveling procedimientos electivos = estrategia efectiva reducir wait y mejorar flow
- [P267] **REGLA** — optimización local departamentos ≠ mejora sistema; sistema óptimos locales puede ser muy ineficiente → `theory of constraints`
- [P268] **REGLA** — análisis sistema complejo incompleto si interdependencias no consideradas
- [P269] **REGLA** — scheduling orden variabilidad creciente → menor cycle time y wait global
- [P270] **DEFINICIÓN** — bottleneck = recurso capacidad ≤ demanda; serie actividades dependientes: solo bottleneck define throughput
- [P271] **REGLA** — backlog puede existir estable incluso demanda promedio < capacidad con alta variabilidad
- [P272] **REGLA** — estimaciones capacidad/staffing/financieras basadas promedios sin variabilidad → sub/sobreestimación significativa → `flaw of averages`
- [P273] **REGLA** — prevalencia <30%: pooled specimen testing más eficiente que individual → `pooled testing`
- [P274] **REGLA** — forecasting: solo datos pasados recientes fuertemente correlacionados; excluir débilmente correlacionados → `ACF`
- [P275] **REGLA** — factores independientes de dataset correlacionado: descomponer en componentes no correlacionados vía PCA
- [P276] **REGLA** — PCA reduce variables; cluster analysis reduce observaciones; ambos reducción volumen datos

## Concluding Remarks
- [P277] **DEFINICIÓN** — healthcare management engineering: decisiones gerenciales → asignación eficiente recursos para care alta calidad mediante métodos analíticos/simulación
- [P278] **HECHO** — traditional management carece medios contabilizar variabilidad, incertidumbre, escala, interconexiones → outcomes inexactos/efímeros
- [P279] **HECHO** — tendencia humana evitar incertidumbre ignorándola o convirtiendo certeza artificial → outcomes inexactos
- [P280] **HECHO** — management engineering revela interconexiones sistemas complejos, contabiliza economías escala, predice rendimiento real → decision-makers proactivos
- [P281] **ALCANCE** — 26 problemas: capacidad clínica/camas/OR, patient flow, staffing/scheduling, optimización recursos, forecasting, BI/DM, teoría juegos

## Appendix: Quantitative Methods
- [P282] **ALCANCE** — inventario métodos: data envelopment analysis, árboles decisión, DES, forecasting, teoría grafos, programación entera, just-in-time, LP, optimización no lineal, programación estocástica, Markov, inventario, Monte Carlo, ruta crítica, QAT, regresión PCA, control calidad, theory of constraints, system dynamics, game theory

## Definitions of Key Terms
- [P283] **DEFINICIÓN** — operations research = modelos matemáticos sistemas complejos variabilidad aleatoria → decisiones operacionales justificadas
- [P284] **DEFINICIÓN** — management science = metodología cuantitativa asignar recursos → metas operacionales sistema; basada operations research
- [P285] **DEFINICIÓN** — sistema complejo = interdependencia mutua componentes; cambio input → cambio no proporcional output
- [P286] **DEFINICIÓN** — DES = modelos computacionales sistemas reales rastreando eventos momentos discretos tiempo → analizar rendimiento
- [P287] **DEFINICIÓN** — QAT = métodos matemáticos colas sistemas simples sin interdependencia; fórmulas analíticas supuestos estrictos
- [P288] **DEFINICIÓN** — simulation package = software interfaz construir/procesar modelos DES; = simulation environment
- [P289] **DEFINICIÓN** — bottleneck/constraint = recurso capacidad ≤ demanda uso
- [P290] **DEFINICIÓN** — PCA = correlación multivariante; identifica variables redundantes; retiene componentes principales no correlacionados (combinaciones lineales originales)
