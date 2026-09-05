---
urn: urn:salud:kb:salubrista-fuentes-base-curadas
nombre: salubrista-fuentes-base-curadas
version: 1.0.0
estado: publicado
descripcion: "Fuentes Base Curadas Salubrista: Este nodo integra las fuentes base que estaban en `INBOX/salud/salubrista` y"
fuente: "Migrado de la bestia (~/kora @ 017dc1b9) artifacts/knowledge/salud/salubrista/fuentes-base-curadas.md (sha256:9db0e6c7a9b7fff297e2931762750828d1da4254ad250dfbf221a741d9a06661) el 2026-06-12; cuerpo byte-fiel (renombrado de fuentes-base-curadas.md a salubrista-fuentes-base-curadas.md por lugar-coincide). Fuente original: Fusion curatorial de INBOX/salud/salubrista y salubrista-base-2026-04-27 sobre el corpus productivo salud/salubrista."
autor: FS
creado: 2026-04-27
lang: es
tags: [salubrista, fuentes-curadas, salud-publica, gestion-sanitaria, pac-ltss, management-engineering, hodom]
familia: fuente
depende: [urn:salud:kb:salubrista, urn:salud:kb:salubrista-atlas-integrado, urn:salud:kb:salubrista-body-of-knowledge]
cita: [urn:salud:kb:salubrista-fuente-salud-publica-global, urn:salud:kb:salubrista-fuente-management-engineering, urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss, urn:salud:kb:gestion-redes-indice, urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-decreto-exento-31-2024, urn:salud:kb:hodom-norma-tecnica-2024, urn:salud:kb:hodom-direccion-tecnica, urn:salud:kb:hodom-manual-alta-complejidad, urn:salud:kb:hodom-situacion-chile-2026]
---

# Fuentes Base Curadas Salubrista

## 0. Objeto

Este nodo integra las fuentes base que estaban en `INBOX/salud/salubrista` y
`INBOX/salud/salubrista-base-2026-04-27` dentro del corpus productivo
`urn:salud:kb:salubrista`.

Las fuentes de conocimiento no redundantes fueron movidas fisicamente a
`artifacts/knowledge/salud/salubrista/fuentes/`. Este nodo conserva la decision
curatorial que decide que informacion entra al corpus, donde se ubica
semanticamente y que no debe duplicarse.

Cuando KORA divide un documento fuente en partes `--pNN.md`, esas partes son
fragmentos fisicos de la misma fuente canonica; no crean una fuente nueva ni
autorizan duplicacion semantica.

## 1. Regla Capital De No Duplicacion

1. La KB publicada de gestion-redes y HODOM vive fisicamente bajo
   `salud/salubrista`; las copias `*.source.txt` del dossier base son evidencia
   de procedencia, no nuevos nodos.
2. `publihealth.md` es espejo semantico del atomizado Oxford: conserva el mismo
   conjunto de 174 proposiciones con un titulo de fantasia. Se preserva
   fisicamente bajo `fuentes/duplicados/` como alias deprecado y no cuenta como
   segunda fuente independiente.
3. Los agentes legacy y staging aportan patrones de capacidad, activacion y
   estilo; no son fuente primaria de dominio sanitario.
4. Los documentos operativos y runtime aportan memoria de decisiones, no
   conocimiento clinico ni normativo.
5. Las proposiciones clinicas individuales de PAC/LTSS se usan solo para
   diseno de sistemas, transiciones, roles, riesgos y continuidad. No autorizan
   prescripcion, diagnostico individual ni protocolos terapeuticos locales.

## 2. Mapa De Fuentes

| Fuente | Contenido unico | Calidad documental | Cumplimiento KORA | Calidad dominio | Decision |
|--------|-----------------|--------------------|-------------------|-----------------|----------|
| `fuentes/salud-publica-global.md` | alcance de salud publica, determinantes, funciones, SDH, inequidad, clima, infecciosas, NCD, salud mental, intervenciones | Media | Alto | Alta | Fuente fisica canonica |
| `fuentes/management-engineering-sanitario.md` | DES/QAT, variabilidad, capacidad, colas, pooling, forecasting, BI, PCA, teoria de juegos | Media | Alto | Alta para gestion | Fuente fisica canonica |
| `fuentes/continuidad-post-aguda-ltss.md` | post-agudos, home health, LTSS, PACE, direccion medica, equipos, transiciones y readmisiones | Media | Alto | Alta para continuidad | Fuente fisica canonica |
| `fuentes/duplicados/publihealth-oxford-alias.md` | espejo editorial del atomizado Oxford | Media-Baja | Alias deprecado | Redundante | Preservar fisicamente, no usar como corpus |
| Dossier salubrista-base | inventario, copias de agentes, KB publicada, HODOM, perfiles, docs operativos y runtime | Alta como inventario | Medio | Media-Alta | Usar como ledger de procedencia y decisiones |

## 3. Conocimiento Absorbido: Salud Publica

El corpus salubrista incorpora de la fuente Oxford:

- salud publica como esfuerzo organizado de la sociedad para crear condiciones
  de salud, no como suma de atenciones individuales;
- funciones nucleares: vigilancia, investigacion de problemas, formulacion de
  politicas, organizacion de servicios costo-efectivos, reduccion de
  disparidades, proteccion ambiental, preparacion ante desastres, investigacion,
  fuerza laboral y evaluacion de programas;
- control de escala mediante determinantes biologicos, conductuales,
  ambientales, sociales, comerciales y politicos;
- lectura de inequidad como distribucion injusta y modificable de poder,
  ingreso, educacion, empleo, territorio y acceso;
- decision poblacional basada en carga de enfermedad, DALY/YPLL cuando aplique,
  transicion epidemiologica, doble carga, sindemias y curso de vida;
- intervenciones publicas en cuatro familias: social/biologica/ambiental,
  conductual, politica y estructural;
- cautela frente a desinformacion, antivacunismo, resistencia antimicrobiana,
  cambio climatico, migracion, violencia, envejecimiento y salud mental como
  problemas de red y no solo de caso.

Regla de uso: cuando una consulta salubrista sea territorial, poblacional,
ambiental, de inequidad o politica, recuperar esta capa como conocimiento de
dominio. Si la consulta requiere control de inferencia o salto de escala, el
agente debe activar la skill `urn:salud:artefacto:firs-razonamiento-sanitario`.

## 4. Conocimiento Absorbido: Management Engineering

El corpus incorpora de management engineering las siguientes reglas operativas:

- las decisiones de capacidad no deben basarse solo en promedios; hay que mirar
  distribuciones, variabilidad, colas y cola larga;
- DES es preferible para sistemas no estacionarios, con llegadas mixtas,
  interdependencias, recursos compartidos y cuellos de botella;
- QAT solo es confiable si sus supuestos de Poisson, estacionariedad,
  independencia y estructura simple son defendibles;
- recursos pooled suelen mejorar espera y throughput, pero la especializacion
  clinica, infecciosa o tecnologica exige capacidad adicional explicita;
- utilizacion alta aumenta espera de forma no lineal; por sobre umbrales altos
  la red debe reservar capacidad de variabilidad;
- load leveling de actividad electiva puede reducir congestion aguas abajo;
- optimizacion local de servicios puede empeorar el sistema completo;
- el bottleneck define throughput en series dependientes;
- forecasting debe privilegiar datos recientes correlacionados y reconocer
  estacionalidad, incertidumbre y riesgo de extrapolacion;
- PCA, clustering y BI ayudan a reducir redundancia de variables y observaciones,
  pero requieren validacion para no generar patrones espurios;
- Shapley value y teoria de juegos son utiles cuando varios actores cooperan y
  deben distribuir ahorros, costos o beneficios de forma justa.

Regla de uso: en camas, urgencia, pabellones, UPC, HODOM, staffing, turnos,
alta, readmision o red territorial, una recomendacion debe declarar si esta
razonando por promedio, distribucion, simulacion, forecast, optimizacion o
criterio experto.

## 5. Conocimiento Absorbido: PAC, LTSS Y Continuidad

La fuente PAC/LTSS se integra como lente de continuidad post-aguda y de
servicios de larga duracion. Aporta:

- distincion entre cuidado agudo, post-agudo, rehabilitacion, cuidado de largo
  plazo, cuidado custodial, home health, hospital-at-home y domicilio con apoyo;
- valor de estrategias Home First y atencion domiciliaria cuando reducen
  hospitalizaciones evitables sin transferir riesgo oculto al paciente o
  cuidador;
- equipos interdisciplinarios con medicina, enfermeria, rehabilitacion, trabajo
  social, farmacia, nutricion, salud mental, soporte domiciliario y cuidador;
- direccion medica como funcion de gobierno clinico, politicas, coordinacion de
  practitioners, calidad, seguridad, derechos, infecciones y mejora continua;
- transiciones como punto critico de error: resumen oportuno, reconciliacion de
  medicamentos, metas de cuidado, responsable, signos de alarma y seguimiento;
- readmisiones como resultado de comunicacion, capacidad, competencias
  geriatricas, acceso a evaluacion 24-48 h, y respuesta a cambios agudos;
- 4M/5M geriatricas como lente de continuidad: mente, movilidad, medicamentos,
  lo que importa, y multimorbilidad;
- servicios residenciales y larga estadia como nodos de red con derechos,
  riesgo de medicalizacion insuficiente o excesiva, desastres, IAAS y tecnologia.

Regla de localizacion: toda referencia a Medicare, CMS, OBRA, PDPM, SNF, IRF,
LTACH, PACE, VA o codigos de facturacion se considera extranjera y no normativa
para Chile u otro pais. Solo puede usarse como analogia estructural salvo
verificacion juridica vigente.

## 6. Integracion Del Dossier Salubrista-Base

El dossier base queda absorbido asi:

- `agentes-productivos/`: confirma que `salubrista` es el agente productivo y
  que el modo hospitalista/HODOM fue subsumido como capacidad interna + skill HODOM;
- `agentes-staging/`: conserva capacidades legacy de vigilancia, analisis de
  red, HAH, calidad y reporte como patrones de tarea, no como arquitectura viva;
- `kb-publicada/`: gestion-redes y HODOM ya existen como nodos canonicos bajo
  `salud/salubrista`; no se replican desde copias `.source.txt`;
- `perfiles/`: queda fuera del corpus de conocimiento; se absorbe en
  `urn:salud:artefacto:salubrista` y en la skill HODOM;
- `docs-operativos/`: preserva decisiones de blueprint, HODOM ideal y handoff;
  se usa como contexto de trazabilidad, no como fuente sanitaria primaria;
- `runtime-toolchain/`: informa transmutacion y despliegue OpenClaw, no cambia
  el corpus de dominio;
- `fuentes-crudas/salubrista/`: queda publicado fisicamente como tres fuentes
  KORA dentro de `salud/salubrista/fuentes/`.

Riesgo residual: seis fuentes no versionadas declaradas perdidas en el
inventario no se incorporan porque no existen en el filesystem actual. No se
debe reconstruir su contenido por memoria.

## 7. Rutas Canonicas De Uso

| Pregunta | Ruta |
|----------|------|
| Diagnostico territorial o inequidad | `salubrista` -> fuente salud publica -> gestion-redes |
| Politica sanitaria o programa | `salubrista` -> fuente salud publica -> gestion-redes herramientas |
| Capacidad, camas o flujo | `salubrista` -> fuente management engineering -> gestion-redes general/unidades |
| Urgencia saturada o boarding | `salubrista` -> gestion-redes urgencias -> fuente management engineering |
| Hospitalizacion domiciliaria | `salubrista` -> HODOM -> fuente PAC/LTSS -> skill HODOM |
| Transicion post-aguda o readmision | `salubrista` -> fuente PAC/LTSS -> gestion-redes unidades/herramientas |
| Evaluacion de intervencion | `salubrista` -> fuentes base -> KPI/herramientas -> skill FIRS si hay salto inferencial |

## 8. Criterios De Calidad Del Corpus

Un uso valido de este nodo debe cumplir:

1. declarar escala y modo operativo;
2. separar evidencia de dominio, analogia extranjera y norma local;
3. no duplicar texto ni proposiciones ya cubiertas por gestion-redes, HODOM o
   fuentes canonicas;
4. citar el nodo canonico publicado cuando exista;
5. declarar vacio cuando una fuente este perdida, no verificada o fuera de fecha;
6. verificar en web o fuente oficial toda norma, tarifa, fecha regulatoria o
   dato operacional inestable;
7. preservar responsabilidad humana en decisiones clinicas, directivas y
   regulatorias.

## 9. Guardrails Semanticos

- Salud publica no equivale a consejo medico individual.
- HODOM no equivale a atencion domiciliaria ambulatoria ni a cuidado custodial.
- PAC/LTSS no equivale a normativa chilena de hospitalizacion domiciliaria.
- Eficiencia operacional no puede desplazar seguridad, equidad, continuidad ni
  derechos del paciente.
- Una reduccion de hospitalizacion o espera no es mejora si se logra mediante
  abandono, seleccion adversa, carga no compensada al cuidador o invisibilizacion
  de riesgo.
- La fuente cruda atomizada permite recuperar proposiciones, pero el corpus
  productivo debe responder desde este mapa curado y sus nodos canonicos.
