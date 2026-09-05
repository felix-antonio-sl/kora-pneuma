---
urn: urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss-p27
nombre: salubrista-fuente-continuidad-post-aguda-ltss-p27
version: 1.0.0
estado: publicado
descripcion: "Crónicas del Crepúsculo Geriátrico - Parte 27"
fuente: "Migrado de la bestia (~/kora @ 9de5dc38b78c23574d24a481a5f84d70173c2203) artifacts/knowledge/salud/salubrista/fuentes/continuidad-post-aguda-ltss--p27.md (sha256:b141279edb38ff15691ad61b36d6207dfd638ef03bdf6e8796ee5468c11c85e6) el 2026-07-17; cuerpo byte-fiel; frontmatter normalizado a ley/2; shard enlazado por cita a urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss."
autor: FS
creado: 2026-04-10
lang: es
tags: [salubrista, fuente, continuidad, post-agudo, ltss, home-health, readmisiones]
familia: fuente
depende: [urn:salud:kb:salubrista]
cita: [urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss]
---

# Crónicas del Crepúsculo Geriátrico - Parte 27

## Multi-Site Same Day Visits

- [P1799] **RESTRICCIÓN** — Medicare pays for same-physician same-patient same-day different-site services ONLY for hospital discharge (99238/99239) + NF admission (99304/99305/99306)
- [P1800] **EXCLUSIÓN** — NF admission H&P cannot reference hospital discharge H&P ("see hospital discharge H&P" not acceptable)

## Split or Shared Visits

- [P1801] **HECHO** — Starting 2022, CMS permits split/shared E/M visits in NF for new/established patients, initial/subsequent visits, critical care, prolonged visits, SNF visits
- [P1802] **EXCLUSIÓN** — Split/shared visits NOT permitted for visits required to be done by attending physician

## "Incident To" Services

- [P1803] **EXCLUSIÓN** — "Incident to" services in NF NOT recognized by Medicare; not reimbursable
- [P1804] **PERMISO** — "Incident to" services billable if physician has discrete rented office space in NF; billed using office E/M codes

## Prolonged Face-to-Face Service Codes

- [P1805] **HECHO** — E/M codes 99354-99357 (prolonged service, direct contact) deleted as of January 1, 2023
- [P1806] **REGLA** — Prolonged E/M outpatient/home → code 99417; prolonged E/M NF face-to-face → code 993X0

## Prolonged Non-Face-to-Face Service Codes

- [P1807] **REGLA** — Codes 99358/99359 used for prolonged service on date other than face-to-face visit date
- [P1808] **RESTRICCIÓN** — 99358/99359 must relate to prior face-to-face visit; performed on single day, not accumulated over several days
- [P1809] **RESTRICCIÓN** — 99358/99359 cannot overlap with chronic care management codes
- [P1810] **REGLA** — 99358 = first 60 min on given date; used once per date. 99359 = each additional 30 min beyond first 60 min
- [P1811] **RESTRICCIÓN** — Initial service time <30 min not reportable/reimbursable for prolonged non-face-to-face codes

## Chronic Care Management Services

- [P1812] **TENSIÓN** — CCM services for NF/ALF residents: billing may succeed but erroneous payment could put practitioners at fraud risk → `CMS`

## Annual Nursing Facility Resident Assessment (AWVs)

- [P1813] **HECHO** — AWV codes G0438 (initial), G0439 (subsequent); applicability to NF/ALF residents unclear; contact CMS/MAC for clarification

## Telehealth Services

- [P1814] **HECHO** — During COVID-19, CMS authorized telehealth for NF and ALF (domiciliary) for new/established patients
- [P1815] **RESTRICCIÓN** — Telehealth visits for NF residents limited to once every 14 days during COVID
- [P1816] **HECHO** — CMS proposing NF initial service codes 99304-99306 removed from telehealth list 151 days after PHE ends
- [P1817] **REGLA** — All regulatory visits must be done in person; initial visit = regulatory visit

## Visits by Qualified Nonphysician Practitioners

- [P1818] **DEFINICIÓN** — NPP = nurse practitioners (NP), physician assistants (PA), clinical nurse specialists (CNS)
- [P1819] **REQUISITO** — All NPP E/M visits must be within State scope of practice/licensure; federal/state physician collaboration/supervision requirements must be met
- [P1820] **EXCLUSIÓN** — SNF: PA/NP/CNS (facility-employed) cannot: order admission, write admission treatment orders, perform initial comprehensive visit, or certify/recertify
- [P1821] **PERMISO** — SNF: PA/NP/CNS (facility-employed) can: perform alternate required visits, medically necessary visits, medically necessary orders
- [P1822] **EXCLUSIÓN** — SNF: PA/NP/CNS (not facility employee) cannot: order admission, write admission treatment orders, perform initial comprehensive visit
- [P1823] **PERMISO** — SNF: PA/NP/CNS (not facility employee) can: perform alternate required visits, medically necessary visits/orders, certify/recertify
- [P1824] **EXCLUSIÓN** — NF: NP/CNS/PA (facility-employed) cannot: order admission, write admission treatment orders, perform initial comprehensive visit, alternate required visits
- [P1825] **PERMISO** — NF: NP/CNS/PA (facility-employed) can: medically necessary visits/orders + certify/recertify
- [P1826] **PERMISO** — NF: NP/CNS/PA (not facility employee) can: ALL functions (admit, orders, initial visit, required visits, necessary visits/orders, certify/recertify)

## Services Not Reimbursable by Medicare

- [P1827] **EXCLUSIÓN** — Care plan oversight, telephone calls, medical team conferences (IDT meetings) not reimbursable by Medicare in NF/SNF
- [P1828] **HECHO** — Prolonged services without face-to-face visit may not be reimbursable
