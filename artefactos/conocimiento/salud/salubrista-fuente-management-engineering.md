---
urn: urn:salud:kb:salubrista-fuente-management-engineering
nombre: salubrista-fuente-management-engineering
version: 1.0.0
estado: publicado
descripcion: "healthcare management engineering: <!-- /atomize · 290 proposiciones · ~125 entidades · 1 archivo · 2026-04-10 -->"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/fuentes/management-engineering-sanitario.md (sha256:7315105cef61a341538a7692891f9c15ec46e192408140f15e2e6b3272d31f78) el 2026-06-12; cuerpo byte-fiel (renombrado de management-engineering-sanitario.md a salubrista-fuente-management-engineering.md por lugar-coincide). Fuente original: Movido desde artifacts/knowledge/_SCRIPTORIUM/INBOX/salud/salubrista/healthcare management engineering.md; integrado fisicamente al corpus salubrista el 2026-04-27."
autor: FS
creado: 2026-04-10
lang: es
tags: [salubrista, fuente, gestion-sanitaria, management-engineering, capacidad, colas, simulacion]
familia: fuente
depende: [urn:salud:kb:salubrista]
---

# healthcare management engineering


<!-- /atomize · 290 proposiciones · ~125 entidades · 1 archivo · 2026-04-10 -->
<!-- Consultar: buscar por [P###], por tipo (REQUISITO, DEFINICIÓN, REGLA...), o por entidad -->

## What Is This Book About?
- [P001] **DEFINICIÓN** — healthcare management engineering = desarrollo sistemático decisiones gerenciales → asignación eficiente recursos (materiales, humanos, financieros) mediante métodos matemáticos/simulación
- [P002] **DEFINICIÓN** — sinónimos management engineering: operations research, system engineering, industrial engineering, operations management, management science
- [P003] **HECHO** — autor Alexander Kolker, Children's Hospital Milwaukee WI; Springer 2012; ISBN 978-1-4614-2067-5
- [P004] **HECHO** — libro cubre 26 problemas gestión operacional hospital/clínica comparando enfoque tradicional vs management engineering
- [P005] **DEFINICIÓN** — sistema = elementos interconectados formando todo complejo comportándose diferente a elementos independientes
- [P006] **DEFINICIÓN** — sistema salud definible nivel nacional (hospitales, clínicas, aseguradoras, CMS) o hospital individual (ED, cirugía, ICU)
- [P007] **ALCANCE** — enfoque libro: management engineering escala hospital individual o clínica grande
- [P008] **ALCANCE** — dominios: capacidad, staffing, scheduling, patient flow, asignación recursos, forecasting, ubicación, workflow, productividad, supply chain, BI/DM
- [P009] **HECHO** — 5 tipos problema: (1) balance dinámico oferta/demanda DES/QAT, (2) optimización lineal/probabilística, (3) forecasting series temporales, (4) BI/data mining, (5) teoría juegos
- [P010] **HECHO** — software DES: ProcessModel 5.3.0; alternativas ProModel, Arena, Simul8, AnyLogic, Simio, FlexSim
- [P011] **⚠ TENSIÓN** — QAT frecuentemente recomendado para capacidad/patient flow hospitalario pero subestima limitaciones prácticas serias (D'Alesandro 2008) y sobreestima dificultad DES
- [P012] **HECHO** — reporte NAE/IOM (Reid et al. 2005): pocos profesionales salud equipados pensar analíticamente sobre healthcare delivery como sistema
- [P013] **HECHO** — Mayo Clinic definió Science of Healthcare Delivery como 1/4 direcciones estratégicas (Quality, Individualized Medicine, Integration)

## Who Is This Book For?
- [P014] **ALCANCE** — libro para líderes hospital/clínica (directores, VPs, COOs, CEOs, board) y estudiantes MBA/Healthcare Management

## Definitions and Comparison
- [P015] **DEFINICIÓN** — traditional management = experiencia pasada, intuición, estimaciones, proyecciones lineales, valores promedio variables input
- [P016] **DEFINICIÓN** — management engineering pasos: (1) meta medible clara, (2) identificar recursos aprovechables, (3) modelos matemáticos testear escenarios/consecuencias
- [P017] **REGLA** — decisiones management engineering frecuentemente diferentes de tradicionales — a veces contraintuitivas
- [P018] **REGLA** — ambientes altamente variables; tratar promedios como fijos → conclusiones seriamente inexactas → `flaw of averages`
- [P019] **REGLA** — sistemas healthcare contienen interconexiones ocultas → consecuencias no intencionadas decisiones aparentemente razonables
- [P020] **REGLA** — efecto escala no lineal: sistemas grandes → mayor utilización + menor wait time que pequeños con mismo ratio volumen/capacidad (Green 2006, Kolker 2011)

## 2.1 Discrete Event Simulation Methodology
- [P021] **DEFINICIÓN** — DES = modelo computacional imitando comportamiento dinámico sistema → visualizar y analizar cuantitativamente rendimiento
- [P022] **DEFINICIÓN** — DES rastrea entidades moviéndose por sistema en puntos discretos tiempo (eventos), registrando tiempos procesamiento/espera
- [P023] **REGLA** — múltiples replicaciones DES necesarias capturar variabilidad sistema; cada replicación usa nuevos números aleatorios mismas distribuciones
- [P024] **HECHO** — promedio simple wait time engañoso para procesos altamente variables sin info dispersión
- [P025] **REGLA** — promedio ponderado por tiempo queue length = mejor métrica rendimiento que promedio aritmético; pondera duración cada paciente en cola
- [P026] **DEFINICIÓN** — bloques básicos DES: flow chart, entidades, actividades, recursos, ruteos entidades
- [P027] **HECHO** — DES sin restricción tipo distribución llegadas/servicio → modelar sistemas más complejos
- [P028] **ALCANCE** — aplicaciones DES: scheduling staff/producción, capacity planning, reducción cycle time, throughput, utilización, encontrar bottlenecks, what-if analysis

## 2.2 Queuing Analytic Theory
- [P029] **DEFINICIÓN** — QAT = técnicas analíticas como fórmulas matemáticas cerradas describiendo propiedades procesos con demanda/oferta aleatoria (colas)
- [P030] **RESTRICCIÓN** — fórmulas QAT tractables solo si flujo eventos = proceso Poisson steady-state con tasa llegada promedio constante
- [P031] **DEFINICIÓN** — modelo M/M/s: Markov con llegadas Poisson, tiempo servicio exponencial, cola ilimitada, s servidores
- [P032] **ALCANCE** — M/M/s calcula: probabilidad 0/K clientes, queue length promedio, wait time promedio, cycle time promedio, utilización servidor
- [P033] **RESTRICCIÓN** — fórmulas QAT intratables conforme complejidad sistema aumenta; no captura complejidad mayoría sistemas healthcare interés práctico
- [P034] **RESTRICCIÓN** — supuestos QAT inválidos muchos procesos healthcare: llegadas batch (accidentes), tasa dependiente llegadas previas, tasas variables temporalmente
- [P035] **REGLA** — test bondad ajuste requerido verificar distribución Poisson antes aplicar QAT; media debe = varianza para Poisson
- [P036] **RESTRICCIÓN** — Poisson usado supuesto teórico estándar operations research por conveniencia matemática pese aplicabilidad limitada patrones reales llegada pacientes
- [P037] **RESTRICCIÓN** — fórmulas QAT no aplicar si flujo contiene componente no aleatoria (llegadas programadas); componente no aleatoria debe eliminarse primero
- [P038] **REGLA** — QAT usable procesos steady-state simplemente estructurados si supuestos Poisson/exponencial se cumplen o coeficiente variación ≈ 1

## 2.3.1 Outpatient Clinic: Centralized or Separate Locations?
- [P039] **HECHO** — clínica gripe centralizada 4 enfermeras (28 pac/h, servicio 8 min): QAT → cola 11.9, wait 25.5 min, utilización 93%
- [P040] **HECHO** — dividir central 4 enfermeras → 2 clínicas × 2 enfermeras (14 pac/h): wait 25.5 → 54 min pese mismo ratio staff/paciente
- [P041] **REGLA** — recursos pooled con flujo aleatorio + cola ilimitada más eficientes que separados con misma carga total; separación ≈ duplica wait time
- [P042] **HECHO** — DES y QAT resultados prácticamente idénticos comparación centralizado/separado: DES cola 11.8, wait 25.3 min (vs QAT 11.9, 25.5)
- [P043] **REGLA** — recursos especializados (dedicados) requieren capacidad adicional planificada compensar pérdida eficiencia vs pooled

## 2.3.2 Outpatient Clinic: Nonsteady-State Operations
- [P044] **HECHO** — servicio promedio 8.0 → 8.6 min (solo +7.5%) empuja rho <1 a 1.003 → fórmulas QAT inaplicables
- [P045] **RESTRICCIÓN** — condición steady-state QAT: rho < 1; si rho ≥ 1 cola crece indefinidamente, no existe solución
- [P046] **HECHO** — DES maneja nonsteady-state y demuestra crecimiento indefinido cola; QAT no puede modelar nonsteady-state
- [P047] **REGLA** — sistemas colas healthcare no lineales: cambio pequeño input puede causar transición dramática steady → nonsteady — "consecuencias no intencionadas"

## 2.3.3 Limited Queue Size with Leaving Patients
- [P048] **HECHO** — cola limitada 15 sillas + pacientes abandonando 10-25 min (moda 15) convierte nonsteady → steady: wait ≈ 6 min, cola ≈ 3.2
- [P049] **⚠ TENSIÓN** — cola limitada + abandono mejora métricas espera solo porque ~10-11% pacientes perdidos; servir menos ≠ mejora real — pérdida revenue

## 2.3.4 Outpatient Clinic: Time-Varying Arrival Rates
- [P050] **HECHO** — enfoque SIPP (tasa promediada) + QAT da resultado engañoso; tasa entra no linealmente en exponencial Poisson; promediar antes sustituir = inválido
- [P051] **HECHO** — QAT SIPP sobreestima cola inicio día, subestima final; sin resultado para períodos rho > 1 (mediodía-3pm)
- [P052] **HECHO** — DES llegadas variables: cola/wait acumulan hacia final día; 3-6pm cola 4.9 vs 8-10am cola 0.15 — lag congestión tras pico
- [P053] **RESTRICCIÓN** — parche SIPP para QAT no confiable; pico congestión lag significativo vs pico llegada; Lag-SIPP más efectiva pero compleja

## 2.3.5 ICU Capacity and Access to Care
- [P054] **HECHO** — ICU 10 camas promedio 5 ocupadas: Poisson → >6 camas necesarias ~24% tiempo; recortar a 6 crea escasez regular
- [P055] **HECHO** — ICU 6 camas (QAT Poisson 2/día, LOS exponencial 2.5d): cola 2.9, wait ~35h, utilización 83%
- [P056] **HECHO** — DES mismos supuestos (Poisson + exponencial): cola 3.1, wait 28-34h (99% CI); 46% pacientes esperan >6h — confirma QAT
- [P057] **HECHO** — DES LOS acotado (triángulo 1-3d, misma media 2.5): cola baja a 1, wait 6-6.6h, 26% >6h — mucho mejor que exponencial ilimitada
- [P058] **REGLA** — variabilidad llegadas/LOS requiere capacidad reservada (a veces hasta 40%) evitar problemas operacionales regulares
- [P059] **REGLA** — QAT produce mismo resultado con mismos promedios independiente forma distribución; no distingue distribuciones diferentes misma media → `flaw of averages`
- [P060] **REGLA** — decisiones capacidad/staffing solo promedios sin distribuciones → miscálculos significativos
