# Handoff vigente — 2026-08-03 — skills de ingeniería con evidencia de uso

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, las
> fuentes canónicas, Git ni el estado vivo de los runtimes. El handoff anterior
> se preservó reversiblemente en
> `_archivo/HANDOFF-2026-08-03-pre-simplificacion-skills.md`.

## Resultado actual

Se migraron selectivamente dos capacidades de `mattpocock/skills`, sin copiar
el repositorio completo:

- `urn:dev:artefacto:diagnosing-bugs` v1.0.0: disciplina de diagnóstico con
  bucle red-capaz, hipótesis falsables, probes y regresión ligada al candidato;
- `urn:dev:artefacto:code-review` v1.0.0: revisión read-only desde punto fijo,
  con paquetes Standards y Spec independientes y baseline auxiliar inspirado
  en Fowler.

Fugaz v2.1.0 usa `diagnosing-bugs` dentro de la misma sesión de corrección,
sin descendencia ni expansión de autoridad. Steipete v1.3.0 activa
`code-review` sólo en Codex; la skill conserva la fuente única del protocolo
bifocal y Steipete declara únicamente su adaptador.

La procedencia de ambas reescrituras está ligada al upstream
`2ab958093e83e0ec752e6c1c5932da465bf23e0c` y a los SHA-256 de sus archivos
fuente. No depende de un path temporal del host y cada skill lleva consigo el
aviso MIT íntegro de la fuente adaptada.

### Evaluación que fundamentó la selección

El snapshot upstream fijado contiene 41 archivos `SKILL.md`; el manifest del
plugin promueve 22 (17 de ingeniería y cinco de productividad). Se ensayaron
cuatro candidatas antes de migrar:

- `diagnosing-bugs` reprodujo y corrigió un fallo sintético: **MIGRAR**;
- `code-review` encontró defectos sembrados por los ejes Standards y Spec:
  **MIGRAR**;
- `to-tickets` produjo cinco tickets útiles, pero además escribió un sexto
  duplicado fuera de su alcance y declaró un PASS falso: absorber conceptos,
  no adoptar la skill;
- `writing-great-skills` aportó una rúbrica útil, pero su forma de autoría no
  respeta directamente el shape KORA: diferida como posible rúbrica adaptada.

`grill-with-docs`, TDD y `domain-modeling` quedaron como candidatas futuras;
no son requisitos omitidos de esta entrega. Los residuos y commits de esos
ensayos permanecen aislados bajo `/tmp`, no en la fuente canónica.

## Sesiones independientes y evidencia de uso

En toda la interacción se abrieron 16 sesiones delegadas independientes. En 15
logs persistidos se verificó `gpt-5.6-luna` con esfuerzo `max`; el smoke test
efímero `019fc51a-11d4-7c33-a1e1-20c1a8c57f14` lo confirmó en el comando y la
salida, pero por `--ephemeral` no dejó `turn_context` durable. La sesión central
permaneció en `gpt-5.6-sol`/`max` y no se cuenta como sesión delegada. Esta es
evidencia de la evaluación runtime; el modelo no forma parte de la identidad,
contrato, tests ni proyección de los artefactos.

Evaluación inicial independiente:

- diagnosing-bugs: `019fc51d-6fde-7a33-9abd-d873391b1090`;
- code-review central: `019fc51d-7006-76c3-828f-46a831355574`, con Standards
  `019fc51e-af23-7c41-b293-d235580efe1b` y Spec
  `019fc51e-af79-7ec3-bd95-ff9b97877fe9` solapados temporalmente;
- to-tickets: `019fc51d-708a-7621-ba11-638f4406458c`;
- writing-great-skills: `019fc51f-be48-7fd3-809d-7bc5144a6f0b`;
- verificación adversarial: `019fc528-3e53-7010-9c0a-d02b9c232514`.

Autoría independiente:

- diagnosing-bugs: `019fc542-3346-7531-aa68-c3346076e7fe`;
- code-review: `019fc542-3578-7c43-b560-58cb817bd634`.

### Piloto A/B de diagnóstico

Ambos brazos partieron del mismo commit
`9302b677b21490b7d63577bc6a8347b75137a369`, recibieron la misma corrección y
autoridad sobre `kora.py` y `tests/test_kora.py`, y cerraron `COMPLETE` con
182/182 pruebas y `velar` 13/13:

| Brazo | Sesión | Tokens totales | Duración por timestamps | Trazabilidad observable |
|---|---|---:|---:|---|
| con diagnosing-bugs | `019fc550-0f49-7200-adb0-c18beebb115a` | 1.390.391 | 382,751 s | tres hipótesis ordenadas, predicciones y probes explícitos antes del fix |
| control normal | `019fc550-0e7f-70e3-b6cd-5681295c7475` | 825.719 | 416,700 s | sin lista equivalente de hipótesis/probes en el stream del asistente |

Resultado: no hubo mejora de éxito binario. El brazo con skill dejó mayor
trazabilidad causal observable, consumió 68,4% más tokens y terminó 8,1% antes
según timestamps. Es una sola tarea histórica, no evidencia estadística ni una
promesa de eficiencia general. Los tokens son el campo `total_tokens` de los
logs y la duración es tiempo de pared entre sus timestamps extremos.

### Piloto de revisión bifocal

- Standards aislado `019fc55a-9caf-7c92-a781-37d09c910ca4`: detectó
  duplicación heurística del protocolo;
- Spec aislado `019fc55a-9da3-75f2-8e9d-828a08777e77`: detectó la procedencia
  ligada a `/tmp`;
- control monolítico `019fc55a-9e43-7683-a222-e7f4f7449614`: detectó la misma
  procedencia y la continuidad obsoleta.

Los paquetes aislados y el control aportaron hallazgos complementarios. La
procedencia se estabilizó, Steipete dejó de duplicar el método y este handoff
reemplazó la continuidad anterior.

## Evidencia técnica del candidato

- upstream: `git ls-remote` confirma que `main` sigue en el commit fijado y los
  dos SHA-256 declarados coinciden byte a byte;
- pruebas focales de las dos skills y sus adaptadores en candidato limpio:
  24/24 PASS (el circuito 44/44 anterior incluía pruebas concurrentes ajenas);
- suite completa en el workspace escribible: 338/338 PASS;
- `velar --estricto`: 13/13 PASS;
- `git diff --check`: PASS;
- scan explícito de whitespace sobre archivos propios no trackeados: PASS;
- verificación adversarial inicial: skills y adaptadores PASS; pidió corregir
  únicamente continuidad y evidencia A/B;
- reevaluación adversarial `019fc569-af10-7983-9771-d620a7901a44`: `READY`
  para el candidato temporal exacto
  `bd8ee251c837b8a06e81115a3e67d3c17fb03210`; fue anterior a las correcciones
  finales de licencia, procedencia y consistencia del candidato, que se
  auditaron y probaron centralmente, no en una nueva sesión adversarial.

La auditoría final incorporó el aviso MIT íntegro, estabilizó la procedencia de
`diagnosing-bugs`, hizo autoritaria la `spec_source` explícita y bloqueó el join
si `HEAD` cambia durante `code-review`. Las dos skills se reemitieron y sus
referencias licenciadas quedaron incluidas en los derivados.

La fuente quedó separada en tres commits funcionales sobre `master`:

- `85492e4` — `feat(skill): add disciplined bug diagnosis`;
- `d33715b` — `feat(skill): add bifocal code review`;
- `ca24738` — `feat(agents): integrate diagnosis and review workflows`.

Se ejecutaron siete reemisiones iniciales por combinación URN/target y dos
reemisiones finales de las skills, siempre sin `--aplicar`. La paridad final
clasifica `diagnosing-bugs` y `code-review` como `no-instalada` (una unidad
Codex cada una), y las instalaciones previas como `desviada`: Fugaz 1/1 y
Steipete 5/5. No hay unidades `sin-emision`. Por tanto, fuente y derivados
locales quedan coherentes, pero el cierre runtime permanece bloqueado hasta una
tarea de despliegue autorizada. No se ejecutó instalación runtime, `--aplicar`
ni despliegue. La publicación Git de los commits anteriores y de esta
continuidad fue autorizada expresamente y debe verificarse contra el remoto
vivo al cierre.

## Límites y siguiente paso

Shape, hashes, tests, emisión y paridad no prueban wiring runtime, creación real
de dos sesiones por el artefacto instalado, least privilege, conducta
universal, aceptación humana ni calidad estadística. El verificador
adversarial fue una sesión independiente, pero la política global le exigió un
quick-pass de memoria y acceso a recibos previos; no fue una evaluación ciega
ni memory-zero.

El candidato funcional ya está identificado de forma inmutable por los tres
commits anteriores, construidos sobre
`c4306488703a48dc6a6a536b942963c679545d94`. El árbol principal conserva además
cambios concurrentes no incluidos en esos commits; la verificación publicable
debe ejecutarse desde un worktree limpio del `HEAD` documental final.

Evidencia temporal preservada para auditoría: snapshot upstream en
`/tmp/mattpocock-skills-study.9yJmrI`, ensayos iniciales en
`/tmp/matt-skills-eval.YFIOAV` y piloto/candidato en
`/tmp/kora-matt-migration-20260803`. Este último conserva tres worktrees Git
registrados (`diag-control`, `diag-treatment` y `review-candidate`). Un resumen
inicial de code-review tiene enlaces absolutos incompletos, aunque los archivos
y logs subyacentes existen. Los dos worktrees de diagnóstico conservan
deliberadamente sus cambios de piloto en `kora.py` y `tests/test_kora.py`; el de
revisión está limpio. No se reescribieron ni eliminaron estos recibos.

Si el operador decide desplegar después, corresponde una tarea separada:
releer instalaciones vivas, obtener autoridad explícita para `--aplicar`,
respaldar y canariar. Esta entrega termina en fuente KORA, evidencia de uso y
derivados locales coherentes; no declara paridad ni conducta runtime.

---

## Cierre de auditoría de fuentes del host — 2026-08-03

> Recibo histórico del corte publicado en
> `c4306488703a48dc6a6a536b942963c679545d94`. Sus referencias al working tree y
> a cambios de skills “no publicados por este cierre” describen ese corte, no
> la publicación posterior documentada arriba.

Esta sección registra el frente de auditoría y consolidación documental. Se
añade sin absorber los cambios concurrentes de skills presentes sólo en el
working tree y no publicados por este cierre.

### Objetivo, alcance y resultado

Se revisaron fuentes candidatas del host para decidir entre koraficar,
conservar externamente, archivar o descartar. El criterio confirmado quedó
publicado como `urn:kora:kb:frontera-fuentes-tecnicas`: KORA es la fuente única
del conocimiento curado; los formatos cuya semántica depende de OWL/SKOS, XML,
schemas o datos raw permanecen externos; un consumidor real usa symlink; y la
ausencia de referencias no autoriza borrar.

Resultado material:

- 96 conocimientos incorporados a `artefactos/conocimiento/`: 11 publicados,
  84 GN en borrador y el tutorial OPCloud en borrador;
- nueve raíces de archivo externas y reversibles con manifiestos SHA-256
  completos para 210 archivos de contenido;
- siete symlinks consumidores vivos y resolubles: cinco en OpenClaw Fleet, uno
  en Ñuble AI y el directorio sanitario ya existente de `hd-dt`;
- Fleet valida symlinks de fuente restringidos a archivos regulares bajo
  `KORA/artefactos` y los materializa como archivos runtime regulares;
- KORA y Ñuble fueron publicados en sus ramas principales; Fleet se publicó
  selectivamente desde una rama limpia.

No se eliminó ninguna fuente. No hubo despliegue ni materialización sobre
runtime vivo. La validez formal no se presenta como aprobación semántica,
institucional, clínica o productiva.

### Decisiones y alternativas descartadas

1. **Una fuente KORA por conocimiento curado.** Se descartaron copias activas
   iguales en varios repositorios.
2. **Conservar semántica técnica externa.** No se convirtieron
   indiscriminadamente ontologías, catálogos, schemas ni datos raw a Markdown.
3. **Archivar antes que borrar.** `DESCARTAR` exige redundancia u obsolescencia
   completa y autoridad explícita; no se ejerció en este trabajo.
4. **Symlink sólo para un consumidor físico.** Los enlaces OPM se hicieron
   relativos. Fleet rechaza enlaces rotos, directorios y destinos fuera de
   KORA, y el runtime recibe archivos regulares.
5. **Ingestión no equivale a aceptación semántica.** Los 84 documentos GN no
   se promovieron en bloque; OPCloud sigue siendo evidencia pedagógica, no
   canon OPM.
6. **Publicar primero la fuente.** KORA se publicó antes de sus consumidores.
7. **No empujar Fleet `main`.** Esa rama contenía cinco commits anteriores al
   cambio y acumuló modificaciones concurrentes; se publicó sólo el delta
   propio desde `origin/main`.

### Artefactos y propósito

| Ruta | Propósito |
|---|---|
| `artefactos/conocimiento/dev/nuble-plan-ia-2026.md` | fuente KORA del plan regional |
| `artefactos/conocimiento/fxsl/information-system-usage-theory-alter.md` | koraficación acotada de ISUT |
| `artefactos/conocimiento/fxsl/{metodologia-modelamiento-opm,opm-iso-19450,opm-opl-es}.md` | fuentes OPM consumidas por Mente Omega |
| `artefactos/conocimiento/fxsl/opcloud-tutorial-videos.md` | evidencia tutorial en borrador |
| `artefactos/conocimiento/kora/frontera-fuentes-tecnicas.md` | criterio curatorial publicado |
| `artefactos/conocimiento/openclaw-fleet/{fleet-canon-policy,handoff-policy}.md` | políticas Fleet canónicas |
| `artefactos/conocimiento/salud/{hsc-cartera-servicios-2024,minsal-decreto-exento-74-2024-mcc,minsal-rem-2026}.md` | fuentes sanitarias trazables |
| `artefactos/conocimiento/gn/*.md` | 84 fuentes GN migradas como borrador |
| `/home/felix/openclaw-fleet/blueprints/mente-omega/{AGENTS,SOUL}.md` | declara la capacidad KORA consumida |
| `/home/felix/openclaw-fleet/blueprints/mente-omega/skills/opm-modeler/references/*.md` | tres consumidores OPM relativos |
| `/home/felix/openclaw-fleet/docs/{fleet-canon-policy,handoff-policy}.md` | dos consumidores de políticas KORA |
| `/home/felix/openclaw-fleet/scripts/{materialize-workspace,verify-repo}.sh` | aplica y verifica la frontera KORA |
| `/home/felix/openclaw-fleet/tests/{test-materialize-workspace,test-verify-repo}.sh` | regresiones de symlinks KORA |
| `/home/felix/projects/nuble_ai_oc/PLAN_IA_NUBLE_2026.md` | consumidor del plan KORA |
| `/home/felix/kora-external-sources/_archivo/*/sha256-manifest.txt` | nueve recibos de contenido archivado |
| `/home/felix/.codex/memories/extensions/ad_hoc/notes/20260803T022819Z-kora-host-audit-closeout.md` | aprendizajes durables y pendientes |
| `HANDOFF.md` | continuidad única; no se creó un handoff paralelo |

El inventario Salubrista registra seis fuentes perdidas desde un working tree
no versionado antes de esta auditoría. No fueron recuperadas y no se afirma que
estén archivadas o sean restaurables.

### Comprobaciones

```text
KORA velar --estricto                                    13/13 PASS
KORA unittest en `origin/master` limpio                  322/322 PASS
KORA unittest en working tree concurrente                338/338 PASS informativo
GN: fuente, SHA declarado y cuerpo normalizado            84/84 PASS
archivos externos: sha256sum --check           9/9; 210 entradas PASS
scan de claves privadas/tokens de proveedor              0 hallazgos
Fleet test-materialize-workspace.sh                      28/28 PASS
Fleet test-verify-repo.sh                                74/74 PASS
Fleet materialización + check en destino temporal        PASS
Fleet symlinks de fuente KORA                              3/3 PASS
Ñuble blob d404f81 vs cuerpo KORA             SHA-256 idéntico PASS
symlinks consumidores del host                             7/7 PASS
git diff --check en cambios propios                        PASS
```

El último `verify-repo.sh --live` del candidato Fleet limpio terminó
`40 PASS / 10 FAIL / 0 WARN / 0 SKIP`. Fallaron `live-drift`,
`runtime-materialization`, `openclaw-health`, `memory-runtime`,
`memory-search`, `active-memory-e2e`, `docs-upstream-live`, `docs-web-live`,
`kora-velar` y `kora-parity`. Los dos últimos observaron una ventana de cambios
concurrentes; el `velar` directo posterior pasó. No se mutó runtime para forzar
verde.

### Git y publicación

KORA `master`:

- `dda9b132f9667b5e75e3845effb41667557fa098`
  `feat(knowledge): consolidate canonical host sources`;
- `f29d9b68ef491439a1557844834f2ad94062e2e4`
  `feat(knowledge): stage audited GN corpus`;
- `46a4d137c26408a4ce5f0e4af4d77b38910386f2`
  `docs(knowledge): publish technical source boundary`;
- el hash del commit documental se obtiene del `git log` vivo para evitar una
  referencia circular.

OpenClaw Fleet:

- commits equivalentes locales sobre `main`:
  `f264a3d54c94e144d3fe8aecebdd135f0edc5d87` y
  `6dce01b76e5465c54095284ed2d4bf81c7c860cc`;
- commits limpios publicados:
  `768b9f64ed9d5e146b4ea997d37039df33b84410` y
  `1e39b451d1860c1835aa4282b829409d14e91608`;
- rama remota `origin/codex/kora-consumers-20260803`, paridad confirmada;
- `main` no fue empujada y conserva historial/cambios concurrentes ajenos.

Ñuble AI `master`:

- `9d7f152bd0b7b3c242d8824c3ddb693f901e8ba8`
  `docs: consume canonical KORA plan`, confirmado en `origin/master`.

### Riesgos, pendientes y siguiente acción

- Permanecen 85 conocimientos en borrador: 84 GN y OPCloud. Su forma es válida;
  su promoción semántica no está demostrada en bloque.
- Las seis fuentes Salubrista perdidas requieren otra copia verificable.
- Los archivos externos y manifiestos son locales y no están publicados en
  Git; dependen de conservar esa zona del host.
- La rama Fleet publicada no fue integrada ni desplegada; el runtime vivo
  conserva drift y fallos de memoria, salud y documentación.
- KORA y Fleet mantienen modificaciones concurrentes no incluidas en estos
  commits. La limpieza se afirma sólo para los commits y ramas exactos.

Siguiente acción recomendada: revisar e integrar
`codex/kora-consumers-20260803` sobre un Fleet `main` limpio; después,
materializar en una operación runtime autorizada y repetir el gate live. En un
frente documental separado, revisar los 84 borradores GN por lotes pequeños y
promover únicamente los que demuestren fuente, vigencia y fidelidad.
