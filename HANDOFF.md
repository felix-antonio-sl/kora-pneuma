# Handoff vigente — 2026-07-31 — revisión sintética situada HODOM-HSC

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, la aplicación, la aceptación humana ni el estado
> vivo del host.

## Objetivo vigente

El panel R01–R14 debe poder revisar una aplicación en desarrollo desde una
perspectiva profesional situada sin presentarse como ser humano, usuario
promedio ni representante exhaustivo del oficio.

La fuente metodológica es:

```text
urn:salud:artefacto:participacion-usuario-sintetico-hodom-hsc v2.0.0
ROLE_PACKET schema                                             3.0
urn:salud:artefacto:hodom-hsc-*                               v3.0.0
```

Los 14 agentes conservan competencia, antirol y voz propios. La skill común
posee la mecánica de participación y revisión.

## Evidencia que motivó la reparación

La evaluación
`hd-hsc-os/docs/05-especificaciones/evidencia-prerelease-product/evaluacion-usuarios-sinteticos-2026-07-30.md`
tiene SHA-256
`0003c3693936bd188bae4dab07653454c6b9c5fb10b9267963222b5a086286db`.

Su informe registra 14 roles, 140 revisiones de journey y 280 observaciones de
viewport, con 12 desajustes de identidad y bloqueos de fixture/superficie. La
inspección de las sesiones fuente mostró además:

- uso no homogéneo de Playwright: algunos roles operaron por coordenadas y
  capturas; otros usaron locators, árbol de accesibilidad, extracción de texto
  y enumeración de controles;
- lectura previa de dossiers, criterios y matrices antes del primer contacto
  con la UI, lo que convirtió la prueba en auditoría informada;
- cobertura amplia repetida por una sola instancia, sin límites de tarea,
  fatiga, interrupción ni independencia real entre viewports;
- ausencia de un estado inconcluso, que empujó fallas de identidad, fixture o
  entorno hacia veredictos del producto;
- carga cognitiva y confianza expresadas como si fueran observaciones humanas,
  aunque sólo podían ser predicciones sintéticas.

La evidencia histórica no se reescribió. Sus hallazgos sobre candidato y
montaje conservan el estado original; esta reparación cambia el método de una
próxima evaluación.

## Contrato corregido

- Cada REVIEW de UI recibe `use_context`: experiencia, fluidez digital,
  contexto, presión, interrupciones, accesibilidad, conocimiento previo,
  objetivo y señal de éxito.
- El preflight verifica candidato, superficie, identidad, fixture, viewport y
  driver antes de puntuar.
- La primera pasada es ciega: pantalla, puntero y teclado, sin DOM, locators,
  selectores, texto programático, consola, red, API, test IDs ni código.
- La segunda pasada profesional ocurre sólo después de preservar la evidencia
  experiencial; no puede reescribirla.
- Cada rol ejecuta como máximo tres tareas críticas por sesión, con presupuesto
  de acciones y recuperación acotada.
- Cada viewport usa contexto de navegador y fixture nuevos. Redimensionar una
  sesión resuelta no prueba un journey móvil.
- Un lector de pantalla u otra ayuda sólo se declara probado con tecnología de
  asistencia real; en otro caso queda `NOT_RUN`.
- Defectos del candidato usan `P0..P3`; montaje, fixture, entorno o causa
  desconocida usan `E0..E1`.
- REVIEW admite `INCONCLUSIVE`; ACCEPT lo rechaza con
  `inconclusive-review`.
- Hechos visibles, interpretación profesional, predicción sintética y brecha
  de validación humana son capas distintas. Carga, confianza o comprensión no
  son mediciones humanas.

## Emisión e instalación

- Skill y 14 agentes fueron retransmutados a Codex.
- La skill emitida pasó `quick_validate.py`.
- Los 15 artefactos se aplicaron con alcance de proyecto en
  `/home/felix/projects/hd-hsc-os`.
- La paridad manual emisión↔instalación quedó `PROJECT_PARITY=PASS`.
- El consumidor quedó publicado en `hd-hsc-os/master` mediante
  `52c5e18d352895a7ce1e32ebe433ee7c67fb668d`, en paridad
  local↔tracking↔remoto.
- El commit fue selectivo sobre los 15 artefactos; no incorporó tres cambios
  concurrentes ajenos en migración y pruebas PostgreSQL.

Codex no puede imponer una allowlist exacta de herramientas built-in. La
emisión declara esa pérdida para `[Bash]` y `[Read,Grep,Glob,Bash]`; el control
observable reside en el protocolo, la separación de evidencia y las pruebas.

## Evidencia de cierre KORA

```text
test_hodom_hsc_role_agents       20/20
suite KORA                       314/314
velar --estricto                 13/13
skill emitida                    valid
snapshot de fuentes              6da0907322a85b25ba97a07612b8d6926fa8c878c1dd3df37410c02b6d263457
paridad proyecto                 PASS
commit fuente KORA               7721184aac54e4ca838ff45d827d1fa66eb824cd
commit consumidor                52c5e18d352895a7ce1e32ebe433ee7c67fb668d
pre-push consumidor              21/21 archivos; 118/118 pruebas
```

## Preparación operativa de la próxima revisión

En esta sesión se entregó un `/goal` listo para pegar de 3.679 caracteres. El
Goal no se ejecutó desde esta conversación y no modifica el contrato canónico:
lo operacionaliza con un integrador único, oleadas de hasta tres agentes,
aislamiento entre roles, primera pasada visual ciega, segunda pasada
profesional, evidencia tipada y cierre `COMPLETE|PARTIAL|BLOCKED`.

La configuración recomendada vive fuera del Goal:

```text
integrador           gpt-5.6-sol / max
agentes R01–R14      gpt-5.6-sol / xhigh
concurrencia         3
```

Se descartó `Ultra` como valor por defecto porque añade delegación proactiva y
la evaluación necesita conservar exactamente la división R01–R14 y sus
oleadas. Si sólo existe un selector global, usar `gpt-5.6-sol / max`. El modelo
y el esfuerzo efectivos deben comprobarse al iniciar; el prompt no los impone.

No se creó un segundo documento para el Goal: este handoff conserva el contrato
de continuidad y evita dos fuentes operativas divergentes. Tampoco se publicó
evidencia de evaluación desde esta sesión.

Estado concurrente observado en el consumidor al cerrar:

- comenzó en
  `hd-hsc-os/master == origin/master ==
  bc2bfcf5b827e390ac09d8d61843826cc2da5fcf`;
- mientras se cerraba KORA, otro trabajo movió `master`, publicó un commit y
  dejó el checkout local nuevamente adelantado respecto del remoto;
- inicialmente había cambios ajenos en `MEMORY.md` y
  `docs/04-arquitectura/continuidad-operativa-2026-07-22-3.md`; el primero fue
  confirmado por ese trabajo concurrente y el segundo seguía modificado;
- ya existían sin seguimiento el informe, manifiesto y paquetes R01–R14 bajo
  `docs/05-especificaciones/evidencia-prerelease-product/*UX-v3*` y
  `usuarios-sinteticos-v3/`.

Esos archivos no fueron creados, revisados, preparados ni publicados por este
cierre. Su procedencia, candidato, cumplimiento visual-only y validez semántica
siguen pendientes; no deben sobrescribirse ni mezclarse con el cierre KORA. El
estado exacto del consumidor debe releerse en vivo: los SHA anteriores prueban
concurrencia, no vigencia.

## Límites

- Revisión sintética no equivale a prueba, aceptación ni utilidad humana.
- REVIEW/ACCEPT no producen autoridad clínica, directiva, administrativa,
  regulatoria, institucional ni productiva.
- Esta corrección no arregla la app, sus fixtures, identidades ni journeys y no
  reevalúa el candidato histórico.
- `DEV_PERSONAL_FULL` sigue permitiendo fuentes privadas en el host personal,
  pero no relaja secretos, Git, publicación ni autoridad profesional.

## Próxima acción

Primero resolver la propiedad y procedencia del trabajo concurrente en
`hd-hsc-os`. Después, sin sobrescribirlo, comprobar su binding
candidato↔runtime, los 14 schemas, la evidencia visual-only, PHI/secretos y el
diff exacto. Sólo entonces decidir si esos artefactos se corrigen, publican o se
reemplazan mediante una nueva corrida con rutas propias. Mantener
`HUMAN_UTILITY`, `HUMAN_SAFETY`, `HUMAN_WORKFLOW_FIT` y `HUMAN_ACCEPTANCE` en
`NOT_RUN` hasta participación humana real.
