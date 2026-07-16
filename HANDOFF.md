# Handoff vigente — 2026-07-16 — transición Claude Code → Codex

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, Git ni la configuración viva de los runtimes. El
> cierre previo de Clawforge 1.1.0 quedó archivado en
> `_archivo/HANDOFF-2026-07-16-clawforge-1.1.0.md`.

## Alcance y veredicto

Se retomó el repo desde `CLAUDE.md` y el handoff vigente, se censó el corpus,
la fábrica de emisiones, sus pruebas y las instalaciones de Claude Code,
Codex, OpenCode y OpenClaw. La revisión combinó disciplina de envío,
razonamiento categorial y tres auditorías adversariales independientes.

El ciclo **Codex + núcleo Pneuma** queda cerrado y desplegado. No equivale a un
cierre multi-runtime: OpenClaw y Hermes conservan deudas explícitas descritas
abajo.

## Resultado entregado

- El defecto principal quedó corregido: `sello-fresco` ya no valida solo el
  hash de la fuente. Regenera cada par `(URN,target)` y contrasta fuente,
  generador y producto byte a byte.
- La comparación incluye factores doctrinales, sidecars Codex y la fibra
  `referencias/`; detecta factores ausentes, manipulados, extra u obsoletos.
- Una emisión se rechaza si su target no coincide con la ruta, no está declarado
  por la fuente o aún no está realizado. Paridad ya no cuenta como unidad un
  directorio sin `SKILL.md` o `AGENTS.md`.
- Re-transmutar elimina ahora una fibra `referencias/` derivada cuando la fuente
  la retira; antes el gate podía indicar una corrección que el propio gesto no
  conseguía materializar.
- La pérdida Codex de `herramientas` quedó tipada sin mezclar allowlists con el
  lugar de resolución: `fidelidad-campos: herramientas:partial` y
  `allowlist[...] -> sin-allowlist-builtins-local`.
- Codex y OpenClaw comparten `~/.agents/skills`. Si la proyección personal
  homónima ya existe, KORA impide instalar debajo una copia managed OpenClaw
  inefectiva. El guard es deliberadamente estrecho: layouts agrupados,
  workspaces y config viva pertenecen al deploy por agente.
- Las 119 parejas realizadas se reemitieron. Se aplicaron 114 parejas que
  estaban desviadas; las instalaciones terminaron en 125 unidades fieles,
  ninguna desviada y ninguna sin emisión.
- El valor único del runtime antiguo de `consenso-deliberativo` fue absorbido
  antes de sobrescribir: caso original, mapeo frase→estado, distinción
  identidad/capacidades, plantilla completa, riesgos, supuestos y confianza.
- Se repararon referencias activas a capas retiradas:
  `steve-jobs → agent-architect`, el cambio de ley OPM pasa por el estrato dueño
  y `scaffold-repo` dejó de depender de `claude-md-management` inexistente.

## Hallazgo que originó el cambio

En el corte inicial, 126 de 137 archivos primarios emitidos diferían del
generador vigente aunque `velar --estricto` y paridad estuvieran verdes. Emisión
e instalación podían ser idénticas entre sí y estar ambas obsoletas. También
quedaban fuera del control 11 fibras `referencias/` y los sidecars sin sello.

El nuevo contrato cierra el diagrama:

`fuente actual → generador vigente → producto completo → instalación`.

`velar` gobierna los tres primeros términos; paridad sigue gobernando
producto→instalación. Ninguno sustituye las pruebas de config efectiva del
runtime.

## Configuración Codex viva

Se corrigió `/home/felix/.codex/config.toml` fuera de Git:

- se retiró `sandbox_mode = "danger-full-access"`, que anulaba la semántica del
  perfil moderno `default_permissions = ":workspace"`;
- se mantuvieron sin cambios `model = "gpt-5.6-sol"` y
  `model_reasoning_effort = "max"` por ser una elección explícita del operador;
- quedaron 12 tombstones reversibles `skills.config.enabled=false`:
  `custodio-kora`, `kora-agentic-lifecycle`, `kora-agents`, `kora-skills`,
  `koraficacion-knowledge`, `transmute-claude-code`, `ifml-architect`,
  `graphic-design`, `gtd-integral`, `steve-jobs-agentic-designer`,
  `jobs-web-ux` y `jobs-healthcare-ux`;
- `jointjs-open-source` se conserva como capacidad externa independiente.

Un proceso Codex nuevo confirmó que los 12 nombres ya no aparecen en discovery.
`codex doctor --summary`: 17 controles correctos, 0 fallos; solo persiste la
advertencia ambiental previa sobre rollout files ausentes de la base de tasks.
Esta tarea conserva el catálogo inyectado al inicio: abrir una tarea nueva o
reiniciar la app materializa la poda en la conversación.

## Verificación final

- `python3 kora.py velar --estricto`: **13/13**.
- `python3 -m unittest discover -s tests`: **134/134**.
- `python3 -m py_compile kora.py`: correcto.
- `git diff --check`: correcto.
- `python3 kora.py transmutar --paridad`:
  **125 fieles · 0 desviadas · 2 no instaladas · 0 sin emisión**.
- TOML Codex parseado y 12/12 tombstones ausentes de un prompt nuevo.
- `origin/master` contiene:
  - `37e1f01` — `fix(artefactos): absorber valor legado para Codex`;
  - `83a15f0` — `fix(kora): probar congruencia del producto emitido`.
- Los commits concurrentes de HSC se conservaron sin mezclar.
- `informe-desempeno-medico-hospitalista-2026-07-11.md` e
  `informe-turno-urgenciologo-2026-07-10.md` permanecen intactos y sin tracking.

## Deuda residual priorizada

### P1 — discovery y deploy OpenClaw

- `autoria-de-persona` y `consenso-deliberativo` siguen como
  `no-instalada` en la raíz managed. OpenClaw consume homónimos de mayor
  precedencia: la proyección Codex personal y, para `main/consenso`, una copia
  workspace legacy v1.0.1 con URNs antiguos.
- No aplicar esas dos mediante `~/.openclaw/skills`: el nuevo guard lo rechaza
  porque no cambiaría la resolución efectiva.
- `agent-architect` y `steve-jobs` tienen workspaces byte-fieles, pero no están
  registrados en `agents.list[]`; una carpeta fiel no prueba que el agente sea
  cargable.
- Paridad OpenClaw es de archivos. No prueba discovery efectivo, registro de
  agentes, sender, `openclaw.json`, gateway ni systemd.
- Las allowlists vivas suelen ser supersets de `herramientas` KORA y una skill
  no tiene autorización de built-ins propia. No afirmar fidelidad completa de
  capacidad hasta mecanizar un gate de deploy por agente.

Siguiente programa recomendado: censar la fuente efectiva de cada skill por
agente, adjudicar la raíz personal compartida Codex/OpenClaw, registrar los
workspaces realmente desplegables y contrastar tools declaradas con config viva.

### P1 — Hermes externo antes de T-Hermes

`hermes` permanece reconocido pero no realizado; `transmutar` lo rechaza con
honestidad. Existen tres bridges clínicos externos activos y únicos en los
perfiles hospitalista/urgencia. No son emisiones KORA, carecen de backup
completo verificado y dos conservan `clinical_warning`, campo ya retirado del
canon HSC. Ambos perfiles usan además el `SOUL.md` genérico de Nous.

Veredicto: **CONSERVAR-EXTERNO**, respaldar y auditar antes de diseñar T-Hermes;
no sobrescribirlos con el stub congelado.

### P2 — eficiencia Codex

- El IR conserva vocabulario de tools nacido en Claude (`Read`, `Grep`,
  `Write`, etc.). Evolución preferida: capacidades abstractas con proyección
  tipada por runtime, sin perder la allowlist Claude existente.
- `salubrista` y `urgenciologo` podrían evaluarse con defaults read-only en
  custom agents, pero las overrides del padre prevalecen y no debe sellarse una
  garantía falsa.
- El discovery todavía carga muchas descripciones. Medir latencia/tokens en
  tareas nuevas y abreviar solo descripciones con bajo poder discriminante.
- `max` privilegia profundidad. Comparar `medium` vs `max` con evals reales
  antes de cambiar el default; no optimizar por intuición.
- `dov-dori` conserva doctrina dual-mode propia además de la inyectada por el
  generador; su deduplicación merece un cambio separado.

## Incidente de auditoría corregido

Una consulta nominalmente read-only usó por error `openclaw --profile main`
en vez de `--agent main`, y el CLI auto-migró `exec-approvals.json` al estado de
ese perfil. Se restauró byte-idéntico el original activo en
`~/.openclaw/exec-approvals.json` (SHA-256
`b0081200c55f6eee832ff0787da2a094aea370541d891fa74b7bbc0bc651d712`). La
copia creada por la consulta quedó fuera de ruta activa en:

`~/.codex/backups/kora-pneuma-2026-07-16-openclaw-profile-audit/exec-approvals.main-profile-created-by-read-audit.json`

No queda mutación funcional residual del incidente.

## Cómo retomar

1. Abrir una tarea Codex nueva y leer `CLAUDE.md` + este handoff.
2. Confirmar `git status`, 13/13 checks, 134/134 tests y paridad antes de tocar
   ley, generador o artefactos agénticos.
3. Tratar OpenClaw como un frente de deploy separado; no inferir efectividad
   desde presencia de carpetas.
4. Respaldar los tres bridges Hermes antes de cualquier transmutación o
   normalización.
5. Medir eficiencia de modelo/descripciones con evals representativos; no
   cambiar `gpt-5.6-sol/max` sin evidencia.

## Rollback

- Núcleo/ley: `git revert 83a15f0`; después reemitir y adjudicar los productos
  creados bajo ley/3 v2.3.0.
- Artefactos: `git revert 37e1f01` solo si se quiere volver a referencias
  legacy; antes preservar la versión rica de `consenso-deliberativo`.
- Config Codex: para reactivar una skill, cambiar solo su tombstone a
  `enabled=true` o retirarlo y reiniciar. Reintroducir
  `sandbox_mode="danger-full-access"` restauraría la ambigüedad antigua y no es
  un rollback recomendado; el estado previo se reconstruye retirando los 12
  bloques y agregando esa línea bajo `web_search`.
- OpenClaw: no revertir el archivo de aprobaciones; ya se restauró el original.
  El respaldo del incidente es evidencia, no configuración activa.
