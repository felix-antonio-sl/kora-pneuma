---
urn: urn:salud:kb:salubrista-fuente-management-engineering-p02
nombre: salubrista-fuente-management-engineering-p02
version: 1.0.0
estado: publicado
descripcion: "healthcare management engineering - Parte 02"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/fuentes/management-engineering-sanitario--p02.md (sha256:4765edab2a3b51caaddad9c98a8d587ecb32f7f2baee9cdc7705025038ad6d2d) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:salubrista-fuente-management-engineering."
autor: FS
creado: 2026-04-10
lang: es
tags: [salubrista, fuente, gestion-sanitaria, management-engineering, capacidad, colas, simulacion]
familia: fuente
depende: [urn:salud:kb:salubrista]
cita: [urn:salud:kb:salubrista-fuente-management-engineering]
---

# healthcare management engineering - Parte 02

## 2.3.6 Mixed Patient Arrival Patterns
- [P061] **HECHO** — llegadas mixtas (8 programadas + 6 emergencia/día, 1h procedimiento, 1 sala): DES → cola 0.62, wait 1h
- [P062] **HECHO** — QAT llegadas mixtas (tratando todas aleatorias): cola 0.82, wait 1.4h — sobreestima +32% cola, +40% wait vs DES
- [P063] **REGLA** — mayor aleatoriedad llegada/servicio → menor rendimiento operacional; QAT sobreestima congestión cuando variabilidad real < Poisson

## 2.3.7 Small vs Large Hospital: Scale Effect
- [P064] **HECHO** — hospital grande 250 camas, 50 admisiones/día: wait 0.001-0.003h, 0.02-0.06% >2h, utilización 81%
- [P065] **HECHO** — hospital pequeño 25 camas, 5 admisiones/día (mismo ratio): wait 2.5-3.0h, 15.5-17.5% >2h, utilización 81%
- [P066] **REGLA** — hospitales grandes siempre mejor performance que pequeños mismo ratio input/capacidad; benchmarking lineal y ajustes proporcionales = inválidos → `scaling effect`
- [P067] **⚠ TENSIÓN** — hospital 25 camas: reducir LOS moda 4→3d elimina wait admisión pero utilización 81% → 53% — trade-off inevitable

## 2.3.8 Daily Load-Leveling of Elective Procedures
- [P068] **HECHO** — schedule electivo sin suavizar (3 ORs): wait emergencia 0.74h, electivo 1.2h
- [P069] **HECHO** — daily load-leveling (mismos totales, 3 ORs): wait emergencia 0.58h (-21%), electivo 0.82h (-32%)
- [P070] **REGLA** — load-leveling schedule electivo = estrategia poderosa reducir wait; Leapfrog Group (2011) incluyó en Patient Experience of Care
- [P071] **HECHO** — Kolker (2009): cap 5 electivos/día → reducir ICU diversion; confirmado Ryckman et al. (2009) Cincinnati Children's Hospital ≈ eliminación total
- [P072] **REGLA** — variabilidad carga quirúrgica programada = fuente "artificial" reducible estrés ICU; disponibilidad camas determinada más por variación demanda programada que no programada (McManus 2003)

## 2.3.9 Separate or Interchangeable ORs
- [P073] **HECHO** — Wullink et al. (2007) DES Erasmus Medical Center: ORs pooled redujeron wait emergencia 74 → 8 min vs dedicado → cierre OR emergencia dedicado
- [P074] **HECHO** — mayoría electivos (6/día): wait electivo dedicado 2.3-2.9h vs pooled 0.14-0.17h — >orden magnitud; dedicado utilización 99%, emergencia dedicado 35%
- [P075] **HECHO** — mayoría emergencias: wait emergencia dedicado 6.3-7.7h vs pooled 0.55-0.65h; pooled más cirugías emergencia (59-60 vs 53-54)
- [P076] **REGLA** — ORs pooled superan dedicados: (1) capacidad compartida buferea variabilidad vía overflow; (2) emergencias simultáneas posibles; (3) idle dedicado no absorbe overflow
- [P077] **⚠ TENSIÓN** — pooling puede no beneficiar si gran diferencia tiempo proceso entre tipos paciente o targets wait urgencia muy diferentes (Joustra 2010, radioterapia)
- [P078] **REGLA** — recomendación tradicional separar ORs scheduled/emergencia (Haraden 2003) contradicha por DES cuantitativo — pooled más eficiente ambos escenarios

## 2.3.10 Surgical Capacity Special Procedure ORs
- [P079] **HECHO** — fórmula tradicional (promedios): 4 camas recovery + 1 SPR suficiente 2,036 procedimientos/año; DES muestra subestimación seria
- [P080] **HECHO** — 4 camas + 1 SPR: 23% pacientes >1h wait SPR y 23% >5min wait recovery (ambos exceden 5% aceptable)
- [P081] **HECHO** — DES distribuciones reales (sesgadas): mínimo 6 camas + 2 SPR requeridos (~2% exceden límites)
- [P082] **REGLA** — cantidad correcta recursos healthcare variable solo predecible simulación; tiempos procedimiento/recovery distribuciones sesgadas colas largas excediendo promedios

## 2.3.11 Entire Hospital System Patient Flow
- [P083] **HECHO** — hospital comunitario grande típico: ED 25 camas, ICU 49, 12 ORs, 360 nursing; volumen mensual ~4,478 (ambulancia ~18%, walk-in ~82%)
- [P084] **REGLA** — patient flow = propiedad sistema hospital completo, no departamentos; interdependencia subsistemas debe modelarse → `system thinking`
- [P085] **HECHO** — reducción agresiva LOS ED (<6h): 4/9 métricas empeoran al mover bottleneck a OR/ICU; reducción moderada (<11h): 9/9 métricas ≥ baseline
- [P086] **REGLA** — balance patient flow: (1) admisiones entrando, (2) altas saliendo tras tiempo variable, (3) capacidad limitada; desequilibrio → overflow/bottleneck/subutilización
- [P087] **REGLA** — mejora subsistemas separados (optimización local) ≠ mejora sistema global; sistema óptimos locales puede ser muy ineficiente (Goldratt & Cox 2004) → `theory of constraints`
- [P088] **HECHO** — prioridad mejora: ICU (mayor % wait admisión >1h), luego OR, luego ED; reducción ED debe coordinarse capacidad downstream

## 2.4.1 Scheduling Order for Appointments
- [P089] **REGLA** — orden citas afecta wait time: menor variabilidad primero significativamente mejor que aleatorio o mayor variabilidad primero
- [P090] **HECHO** — menor variabilidad primero: wait 6-7.3 min, clínica 9.6-9.9h; mayor variabilidad primero: wait 17.7-21.6 min, clínica 11.9-12.8h
- [P091] **HECHO** — Monte Carlo IHI (25 días): menor variabilidad wait 6.3 min vs mayor 19.2 min — ratio ~3×; confirmado Klassen & Rohleder (1996), Cayirli et al. (2006)
- [P092] **REGLA** — principio scheduling fundamental (manufactura): orden variabilidad creciente → menor cycle time y wait global
- [P093] **HECHO** — overtime clínica = consecuencia variabilidad duración citas, no del promedio; enfoque tradicional subestima tiempo total

## 2.4.2 Centralized Discharge vs Individual Units
- [P094] **HECHO** — 4 enfermeras unidad (propias altas): ~74/semana; enfermera dedicada centralizada: ~60/semana — 19% menos
- [P095] **REGLA** — centralizar altas crea bottleneck: altas → serie eventos dependientes; delay una impacta todas subsiguientes
- [P096] **REGLA** — serie eventos dependientes: solo bottleneck define throughput sistema; capacidad extra días buenos se pierde, backlog días malos acumula (Goldratt & Cox 2004)
- [P097] **REGLA** — backlog solicitudes servicio puede existir estable incluso demanda promedio alta variabilidad < capacidad (Savin 2006)

## 2.4.3 Staffing Hospital Receiving Center
- [P098] **HECHO** — tradicional (10 min/paquete, 127,139/año): 11.1 FTE suficientes; DES: 11 FTE solo procesan 118,744 — crónicamente understaffed
- [P099] **HECHO** — DES: 12.5 FTE requeridos (12 full + 1 half) procesar todos 127,139 paquetes; utilización ~88%
- [P100] **REGLA** — staffing tradicional basado promedios siempre subestima recursos; cálculo correcto requiere distribución tiempos procesamiento reales
- [P101] **HECHO** — staffing 11 FTE: reducir procesamiento a 9 min rango 7-12 min permite procesar todo; estandarización reduce variabilidad

## 2.4.4 Staffing with Cross-trained Staff
- [P102] **HECHO** — fórmula tradicional (medias): 3.1 FTE case management (0.3 reservas + 1.4 admisión + 1.4 preregistro)
- [P103] **HECHO** — distribuciones altamente sesgadas: tiempos reales hasta 18, 38, 26 min (vs medias 4.1, 8.3, 4.5 min)
- [P104] **HECHO** — DES distribuciones reales + cross-training: 4.5 FTE requeridos vs tradicional 3.1 — 45% más staff
- [P105] **REGLA** — cross-trained staff aumenta productividad por soporte mutuo; fórmulas tradicionales no contabilizan sharing carga
