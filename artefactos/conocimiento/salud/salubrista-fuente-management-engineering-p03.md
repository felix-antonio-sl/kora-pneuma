---
urn: urn:salud:kb:salubrista-fuente-management-engineering-p03
nombre: salubrista-fuente-management-engineering-p03
version: 1.0.0
estado: publicado
descripcion: "healthcare management engineering - Parte 03"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/fuentes/management-engineering-sanitario--p03.md (sha256:005aea1491c2372bbcc2b46b710bc78f1c8216b268ce3c5ebf7e6268eee2919e) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:salubrista-fuente-management-engineering."
autor: FS
creado: 2026-04-10
lang: es
tags: [salubrista, fuente, gestion-sanitaria, management-engineering, capacidad, colas, simulacion]
familia: fuente
depende: [urn:salud:kb:salubrista]
cita: [urn:salud:kb:salubrista-fuente-management-engineering]
---

# healthcare management engineering - Parte 03

## 2.4.5 Outpatient Clinic Costs and Staffing
- [P106] **HECHO** — tradicional: 2 FTE → 600 pac/sem, revenue $15,567; DES: 2 FTE → 474-476 (-21%), 121-123 (20%) se van sin atención
- [P107] **HECHO** — 2 FTE regular: revenue real $12,054; 2 FTE + 1h overtime: 513-515 pac, revenue $12,912
- [P108] **HECHO** — +0.6 FTE mañana (8am-1pm): 508 pac, revenue $12,620; mismo 0.6 FTE tarde (1-6pm): 557 pac, solo 38 se van, revenue $14,000
- [P109] **REGLA** — colocación FTE turno correcto > conteo total: mismo 0.6 FTE tarde vs mañana genera ~$1,400 más revenue/sem y ~50 más pacientes
- [P110] **HECHO** — 4 FTE: ~594 pac revenue $14,149; 4.6 FTE: ~599 pac revenue $13,933 — 0.6 extra no compensado por 5 pac más
- [P111] **REGLA** — revenue neto crece solo cuando ingreso pacientes adicionales compensa costo recurso; más allá punto óptimo, costo staff > revenue marginal

## 3.1 Optimization of Patient Service Volumes
- [P112] **DEFINICIÓN** — LP estructura: (1) variables decisión, (2) función objetivo, (3) restricciones, (4) parámetros valores numéricos definidos
- [P113] **DEFINICIÓN** — función objetivo LP = meta cuantitativa con variables decisión y parámetros fijos en combinaciones lineales
- [P114] **DEFINICIÓN** — restricciones LP = desigualdades/ecuaciones lineales limitando alternativas/recursos
- [P115] **REGLA** — LP: maximizar/minimizar objetivo sujeto restricciones variando variables decisión; conjunto cumpliendo meta = solución
- [P116] **HECHO** — hospital 3 líneas servicio, 5 recursos: LOS, enfermería, radiología intervencionista, laboratorio, ORs
- [P117] **HECHO** — revenue neto/pac: línea 1 $560, línea 2 $790, línea 3 $1,100
- [P118] **RESTRICCIÓN** — límites recursos anuales: LOS 19,710 pac-días; enfermería 16,200h; radiología 3,000h; laboratorio 6,000h; ORs 1,040h
- [P119] **RESTRICCIÓN** — no-negatividad requerida: variables decisión (volúmenes) ≥ 0
- [P120] **RESTRICCIÓN** — restricción entera preferida para variables volumen pacientes; redondeo soluciones reales a veces aceptable
- [P121] **HECHO** — solución LP óptima: línea 1=520, línea 2=2,740, línea 3=0 pac; revenue máximo $2,455,800
- [P122] **HECHO** — línea 3 (mayor revenue/pac $1,100) eliminada completamente en óptimo porque viola restricciones recursos → `contraintuitivo`
- [P123] **HECHO** — restricciones binding: radiología (3,000h), laboratorio (6,000h), ORs (1,040h) — todas al límite
- [P124] **HECHO** — línea 3 a 100 pac: laboratorio excedido 350h, ORs excedido 400h
- [P125] **HECHO** — cirugía línea 3 reducida 4→1h + lab a 1.5h: óptimo cambia línea 1=261, 2=2,617, 3=518; revenue $2,783,390
- [P126] **REGLA** — LP permite evaluar muchos escenarios cambio parámetros, similar DES → `what-if analysis`
- [P127] **⚠ TENSIÓN** — LP determinístico usa promedios como ciertos; variables aleatorias pueden producir soluciones estructuralmente diferentes en LP estocástico
- [P128] **DEFINICIÓN** — LP estocástico (SLO): ≥1 datos representados variables aleatorias; incertidumbre afecta factibilidad y optimalidad
- [P129] **HECHO** — 2 enfoques LP estocástico: (1) modelado recurso; (2) restricciones probabilísticas limitando prob violación nivel preespecificado
- [P130] **HECHO** — LP ampliamente aplicado ingeniería/negocios/academia decades; menos usado gestión práctica healthcare
- [P131] **HECHO** — solución LP obtenible Microsoft Excel Solver con 'Assume Linear Model' + 'Assume Nonnegativity'

## 3.2 Optimization of Clinical Unit Staffing 24/7
- [P132] **DEFINICIÓN** — enfermera ICU full-time: 5 días/semana, 2 días libres consecutivos rotativos, turnos rotativos; 3 turnos 8h/día
- [P133] **HECHO** — tarifa: $50/h (base + overhead) lun-vie; +50% ($75/h) sáb-dom
- [P134] **HECHO** — 7 días × 3 turnos = 21 schedules enfermera posibles
- [P135] **HECHO** — ratio enfermera-paciente 1:2 todos turnos; demanda mínima staff = censo promedio turno × ratio
- [P136] **REGLA** — staffing tradicional reduce costo total pero no garantiza restricciones turno; resulta ajustes diarios + overtime eliminando ahorros
- [P137] **REGLA** — función objetivo LP staffing: minimizar costo semanal enfermería asignando staff correcto turno correcto
- [P138] **DEFINICIÓN** — variable binaria I(s,ds) = 1 si enfermeras schedule s asignadas día-turno ds, 0 si no
- [P139] **HECHO** — LP óptimo: pool = 36 enfermeras; costo semanal = $77,800
- [P140] **REGLA** — LP staffing acomoda ratios/tarifas variables por turno, part-time; puede maximizar satisfacción vía puntajes preferencia
- [P141] **⚠ TENSIÓN** — censo tratado fijo en LP staffing pero son variables aleatorias; problema estrictamente LP estocástico
- [P142] **HECHO** — variables decisión = Xs enfermeras por cada s=21 schedules; restricciones: cobertura real/turno ≥ demanda mínima

## 3.3 Resident Physician Restricted Work Hours
- [P143] **HECHO** — evidencia científica: fatiga horas largas + privación sueño → déficits rendimiento, accidentes, errores médicos (IOM 2009, Ulmer et al.)
- [P144] **HECHO** — horas largas y privación sueño típicas programas formación residentes US previo IOM 2009
- [P145] **RESTRICCIÓN** — IOM 2009: turnos residentes ≤12-16h máximo; ≥10h descanso entre turnos
- [P146] **RESTRICCIÓN** — IOM: ≥1 período 24h libre/semana sin promediar; + período 24h adicional → ≥48h continuas libres/mes ("golden weekend")
- [P147] **RESTRICCIÓN** — IOM: turno nocturno ≤4 noches consecutivas; ≥48h continuas libres tras 3-4 noches
- [P148] **RESTRICCIÓN** — ICU día: ≥4 residentes lun-vie, ≥3 sáb-dom
- [P149] **RESTRICCIÓN** — ICU noche: ≥3 residentes lun-vie, ≥2 sáb-dom
- [P150] **HECHO** — IOM requiere schedule mensual (4 sem) implementar golden weekend/mes + día libre/semana
- [P151] **HECHO** — turno día IOM genera 196 schedules posibles: 7 × 4 semanas × 7 patrones = 196
- [P152] **HECHO** — LP óptimo scheduling diurno: pool mínimo = 5 residentes cumpliendo todas restricciones IOM
- [P153] **HECHO** — scheduling nocturno: restricción IOM (≤4 noches + ≥48h libres) → patrón deslizante 6 semanas; solo 6 schedules
- [P154] **HECHO** — LP óptimo noche: rotación 4 noches trabajo + 2 días libres consecutivos, repitiendo cada 6 semanas
- [P155] **REGLA** — LP preferido sobre DES staffing cuando poca aleatoriedad y meta = staffing mínimo cobertura por seguridad/regulación, independiente workload
- [P156] **REGLA** — DES más apropiado que LP balance dinámico oferta/demanda con procesos aleatorios donde staffing depende volúmenes (workload)
- [P157] **REGLA** — scheduling tradicional residentes manual o software: manual impracticable; software cobertura pero no staffing mínimo optimizado

## 3.4 Optimized Pooled Screening Testing
- [P158] **HECHO** — CDC recomienda screening HIV todos pacientes 13-64 en todos settings healthcare: hospital EDs, urgent care, inpatient, STD/TB clinics, primary care
- [P159] **HECHO** — laboratorio capacidad 60 especímenes HIV/día; CDC nuevas recomendaciones → ~100/día, backlog + overtime
- [P160] **REGLA** — tradicional escasez capacidad: presupuestar staff/equipo adicional; restringido aprobación tight
- [P161] **DEFINICIÓN** — pooled testing: lote muestras combinado; lote negativo → todas negativas 1 test; lote positivo → retesteo individual
- [P162] **HECHO** — trade-off: reducción tests (lote negativo) vs retesteo (lote positivo); tamaño lote óptimo minimiza tests/espécimen
- [P163] **HECHO** — tests esperados/espécimen N = [1-(1-P)^n](n+1)/n + (1-P)^n; n=tamaño lote, P=prob positivo
- [P164] **RESTRICCIÓN** — reducción tests (N<1) solo si prevalencia P < ~30.6%
- [P165] **REGLA** — P 12.4-30.6%: lote óptimo = 3; P < 11.1%: lote ≈ 1/√P + 0.5 redondeado
- [P166] **HECHO** — CDC 2008: prevalencia HIV US fin 2006 P ≈ 0.447% (95% CI: 0.427-0.468%)
- [P167] **HECHO** — P=0.447%: lote óptimo 15; tests/espécimen ≈ 0.13 → reducción 87% — de 100 a ~13 diarios
- [P168] **HECHO** — grupo alto riesgo P=10%: lote óptimo 4; tests/espécimen ≈ 0.594 → ~59 diarios, dentro capacidad 60
- [P169] **RESTRICCIÓN** — dilución lote puede reducir especificidad/sensibilidad analítica; considerar en implementación
- [P170] **REGLA** — pooled testing mejorado sorting especímenes alto/bajo riesgo; ahorros adicionales con grupos alto riesgo identificables prevalencia mucho mayor
- [P171] **REGLA** — multistage testing: lotes positivos → lotes más pequeños retesteo; más eficiente prevalencia muy baja + pérdida sensibilidad mínima
- [P172] **ALCANCE** — pooled testing aplicable testing masivo cualquier fluido/espécimen, no limitado HIV

## 3.5 Projected Patients Discharged from ED
- [P173] **DEFINICIÓN** — ESI (Emergency Severity Index) clasifica pacientes ED; datos históricos LOS por ESI
- [P174] **HECHO** — predicción alta ED tradicional: evaluación médico/enfermera subjetiva; inexacta por dificultad integrar múltiples fuentes
- [P175] **REGLA** — LOS promedio insuficiente predecir altas; distribuciones LOS muy diferentes pueden compartir mismo promedio
- [P176] **DEFINICIÓN** — probabilidad condicional alta q(T,t): prob paciente no dado alta LOS=T será dado alta próximo período t
- [P177] **HECHO** — fórmula: q(T,t) = [F_ESI(T+t) - F_ESI(T)] / [1 - F_ESI(T)]; F_ESI = distribución acumulada LOS por ESI
- [P178] **HECHO** — Littig & Isken (2007): hazard ratio similar → prob condicional salida 24h dado LOS actual → predicción ocupación hospital
- [P179] **HECHO** — distribuciones acumuladas LOS por ESI aproximadas polinomios 3er orden → calculadora Excel
- [P180] **HECHO** — altas esperadas período t: N_ESI(T,t) = N_ESI(T) × q_ESI(T,t) redondeado
- [P181] **HECHO** — ejemplo lead time 2h: 44 pacientes ESI 1-4 → ~29 altas esperadas (ESI-1:7, ESI-2:8, ESI-3:9, ESI-4:5)
- [P182] **REGLA** — precisión predicciones depende calidad datos LOS; recolectar ≥1 año capturando variación estacional
- [P183] **ALCANCE** — anticipar altas ED → unidades inpatient downstream lead time agilizar camas, alta/transferencia pacientes existentes

## 4.1 Forecasting Patient Volumes
- [P184] **HECHO** — forecasting volumen pacientes = paso crítico planificación capacidad, presupuesto, asignación recursos
- [P185] **HECHO** — método más simple: % crecimiento anual fijo (2-3%); asume crecimiento ilimitado sin insight tendencias
- [P186] **DEFINICIÓN** — métodos smoothing: regresión polinomial, Box-Jenkins, exponential smoothing, Holt-Winters, promedios móviles ponderados, ARIMA
- [P187] **REGLA** — smoothing: encontrar patrones series temporales → extrapolar patrón como forecast
- [P188] **REGLA** — antes forecast: identificar número datos pasados necesarios para predicciones
- [P189] **HECHO** — datos demasiado antiguos no afectan prácticamente datos recientes; recencia determina relevancia predictiva
- [P190] **DEFINICIÓN** — ACF (autocorrelation function) = interdependencia lineal datos separados k unidades tiempo (time lag)
- [P191] **REGLA** — datos fuertemente correlacionados (sobre umbral significancia) incluir; débilmente/no correlacionados excluir → evitar forecasts sesgados
- [P192] **⚠ TENSIÓN** — más datos reduce error pero riesgo overfitting; puntos recientes fuertemente correlacionados preferidos forecast más allá datos disponibles
- [P193] **REGLA** — ACF(k): 1 en k=0 → 0 para k grande; cutoff = máx k donde ACF(k) estadísticamente ≠ 0 (95% confianza)
- [P194] **HECHO** — volumen pacientes 1997-2009: ACF significativo k=1-4; solo 5 años recientes (2005-2009) correlación >0.8 usar
- [P195] **HECHO** — validación 2005-2008 → predecir 2009 (real=18,225): Growth curve 11.8%, Exponential 15.3%, S-curve 1.9%, Winters' 12.2%, Polynomial 11.9%, Moving avg 5%, ARIMA 7.2% error
- [P196] **HECHO** — ningún smoothing tradicional bueno prediciendo 1 año; improbable forecasts largo plazo confiables
- [P197] **HECHO** — polinomios producen tendencias descendentes espurias >2011; growth/Winters' sobrepredicen (35K/30.5K para 2015)
- [P198] **DEFINICIÓN** — recursive linear prediction: técnica señal digital; próximo dato = combinación lineal m valores previos con coeficientes d_j minimizando discrepancia
- [P199] **REGLA** — recursivo estable solo si raíces complejas polinomio característico |z| ≤ 1; coeficientes malos → output exponencial
- [P200] **HECHO** — forecast recursivo 2009: predicción 18,114 vs real 18,225 — error 0.6%, muy superior todos smoothing
- [P201] **HECHO** — recursivo predijo crecimiento moderado 2013, aplanamiento 2014, declive leve 2015 — más plausible que ilimitado/constante
- [P202] **REGLA** — ningún forecast perfectamente preciso; imposible predecir futuro desde pasado con certeza
- [P203] **REGLA** — recursivo confiable cuando factores subyacentes estables y datos recientes fuertemente correlacionados usados
- [P204] **HECHO** — forecast recursivo vastamente más poderoso que smoothing/extrapolación polinomial (Press et al. 1988)

## 4.2 Forecasting with Seasonal Variation
- [P205] **HECHO** — procesos fisiológicos varían estacionalmente (PA, FC, lípidos); eventos cardiovasculares, ACV, mortalidad fluctuación estacional
- [P206] **HECHO** — Tseng et al. (2005): variación estacional significativa A1C mensual veteranos diabéticos US; mayor invierno, menor verano
- [P207] **DEFINICIÓN** — descomposición estacional: (1) media móvil centrada, (2) valores estacionales brutos, (3) medianas/período, (4) índices promedio 1, (5) desestacionalizar, (6) tendencia lineal, reaplicar índices
- [P208] **HECHO** — Winters' calcula 3 componentes dinámicos (nivel, tendencia, estacional) vía Holt-Winters; estimaciones actualizan con valores vecinos
- [P209] **DEFINICIÓN** — ARIMA: filtra datos (autoregresivo → integrado → media móvil) hasta ruido aleatorio; flexible pero no automatizable y lento identificar/ajustar
- [P210] **HECHO** — descomposición, Winters', ARIMA: forecasts similares variación estacional; difícil identificar mejor
- [P211] **REGLA** — forecast recursivo no requiere descomposición tendencia/estacional; aplica directo datos originales
- [P212] **HECHO** — A1C 24 meses: ACF k=4-8 y k=15-16 no significativos; k=10-14 y k=17-21 significativos por patrón estacional; 22 meses necesarios
- [P213] **HECHO** — ACF A1C desestacionalizado significativa k=21; confirma usar 22 datos forecast 12 meses
- [P214] **HECHO** — recursivo A1C refleja estacionalidad máx Feb-Mar, mín Sep-Oct; amplitud menor que tradicionales porque directamente forecasteada

## 5.1 Multivariate Database Analysis (PCA)
- [P215] **DEFINICIÓN** — BI = métodos cuantitativos extraer info/patrones bases datos grandes → decisiones gerenciales
- [P216] **DEFINICIÓN** — DM = análisis datasets observacionales → relaciones insospechadas, resúmenes novedosos (Hand et al. 2001)
- [P217] **DEFINICIÓN** — contribution margin (CM) = pagos cobrados paciente − costos variables paciente
- [P218] **HECHO** — dataset CM por zip code: 32 variables demográficas — 8 edad, 9 educación, 10 ingreso, 5 ocupación — 10 zip codes
- [P219] **HECHO** — categorías demográficas altamente correlacionadas: 'some HS'/ingreso <$15K r=0.899; master/$150-250K r=0.873 → info redundante
- [P220] **HECHO** — regresión 32 variables: R-sq(adj)=8.6%, coeficientes no significativos (p 0.1-0.97), VIF docenas-millones — fallo multicolinealidad
- [P221] **REGLA** — muchas variables correlacionadas → regresión tradicional falla extraer factores; PCA requerida
- [P222] **DEFINICIÓN** — PCA = identificar variables redundantes, retener pocos componentes principales no correlacionados (combinaciones lineales originales) con toda info; caso especial SVD
- [P223] **REGLA** — mayor correlación columnas → menos variables principales necesarias describir dataset
- [P224] **REGLA** — eigenvalues suman total variables originales p; grandes = alto contenido info; PCA reorganiza no destruye info
- [P225] **HECHO** — PCA 32 variables (Minitab 15): 9 PCs cubren 32 variables; primeros 5 PCs = 94% datos → alta redundancia
- [P226] **REGLA** — regresión con PCs: PCs menores (eigenvalue ≈ 0) NO eliminar — introduce sesgo; excepción pura reducción variables
- [P227] **REGLA** — PCs ortogonales → VIF=1 todos predictores; términos no significativos removibles sin afectar restantes → elimina multicolinealidad
- [P228] **HECHO** — best subset 7 PCs (PC1-4, PC6-8): R-sq=95.9%, R-sq(adj)=81.6%; solo PC6 significativo p=0.05
- [P229] **HECHO** — contribuyentes negativos PC6 a CM: edad 18-24/60-64; educación 'some HS'/'HS'; ingreso '$500K+'/'<$15K'; ocupación 'service'/'public service'
- [P230] **HECHO** — 'some HS' + <$15K correlacionados = misma población pobreza/baja educación asistencia gubernamental usando frecuentemente servicios hospital
- [P231] **REGLA** — aumentar CM: marketing zip codes mayores factores demográficos negativos PC6

## 5.2 Cluster Analysis
- [P232] **DEFINICIÓN** — cluster analysis = agrupar observaciones similitud intra-cluster >> similitud inter-cluster; cuando poca info estructura datos
- [P233] **HECHO** — ANOVA no válido datos población completa (no aleatorios); cluster analysis apropiado sin supuestos muestra aleatoria
- [P234] **REGLA** — PCA reduce variables (columnas); cluster analysis reduce observaciones (filas); ambos reducción volumen datos
- [P235] **DEFINICIÓN** — tres métodos DM: clasificación, clustering, asociación (Hand et al. 2001)
- [P236] **DEFINICIÓN** — hierarchical clustering (aglomerativo): observaciones separadas → unir par más cercano iterativamente; dendrogram; lento datasets grandes
- [P237] **DEFINICIÓN** — K-means (particional): k centroides aleatorios → reubicar objetos similitud iterativamente; más preciso/rápido que hierarchical; requiere k previo
- [P238] **DEFINICIÓN** — proximidad cluster: single linkage (nearest), complete (furthest), average, centroid; distancias: Euclidean, Mahalanobis, Manhattan, Minkowski
- [P239] **REGLA** — average linkage + centroid + Euclidean más usados: insensibilidad relativa outliers
- [P240] **HECHO** — K-means generalmente más preciso que hierarchical; hierarchical más lento, datasets menores
- [P241] **HECHO** — cluster 29 zip codes CM k=5 K-means: partición más intuitiva que hierarchical; 29 → 5 grupos
- [P242] **HECHO** — aplicaciones DM healthcare: fraude seguros, subdiagnóstico, marketing/costos, patrones frecuentes, relaciones enfermedades/fármacos (Yoo 2011)
- [P243] **RESTRICCIÓN** — cluster analysis siempre produce clusters incluso datos aleatorios; riesgo clusters espurios; métodos validación existen (Tibshirani 2001)
