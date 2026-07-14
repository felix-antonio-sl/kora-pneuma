# Handoff vigente — 2026-07-14

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> frontmatters canónicos, git o GitHub. Verificar siempre el estado vivo antes
> de actuar. Cuando este handoff sea reemplazado, desplazarlo a `_archivo/`.

## Estado al cierre

- La resincronización de `modelamiento-opm` quedó publicada en `master` mediante
  el commit [`b119f8b`](https://github.com/felix-antonio-sl/kora-pneuma/commit/b119f8b).
- [`kora-pneuma#1`](https://github.com/felix-antonio-sl/kora-pneuma/issues/1)
  está cerrado como completado, con evidencia de validación en su comentario
  final.
- La skill canónica está en v1.14.0. Fue emitida e instalada con paridad fiel
  para Claude Code, Codex y OpenCode al cierre de esta sesión.
- `velar --estricto` y la suite completa estaban verdes al cierre.
- El único pendiente derivado quedó aislado en
  [`deep-opm-pro#1`](https://github.com/felix-antonio-sl/deep-opm-pro/issues/1):
  ampliar `cordon:skill` a una matriz multi-target y contrastar las versiones
  del resolutor SSOT con las fuentes KORA vivas.
- Los archivos locales no versionados
  `informe-desempeno-medico-hospitalista-2026-07-11.md` e
  `informe-turno-urgenciologo-2026-07-10.md` pertenecen al operador y quedaron
  deliberadamente fuera de staging y commits.

## Decisiones tomadas

1. El cambio mínimo quedó limitado a la skill canónica y su fibra
   `bundle-deep-opm-pro.md`; las demás fibras revisadas no tenían
   afirmaciones dependientes que corregir.
2. El salto `1.13.0 → 1.14.0` es minor: amplía doctrina operacional y corrige
   fibras sin introducir semántica OPM nueva ni romper el contrato previo.
3. `R-ENT-2-APUNTE` aplica únicamente a la especie apunte: los placeholders
   emiten OPL en todas las superficies, conservan el diagnóstico de nominación
   y vuelven al rigor ordinario al graduar. La autoría headless sigue estricta.
4. La UI vigente se documentó contra código y pruebas de opforja: Inspector
   continuo sin tabs, graduación visible solo por
   `CintaApunte → DialogoGraduar` y comando «Copiar log de decisiones para la
   skill».
5. Un OPD suelto es un estado transitorio legítimo de `R-OPD-REF-20`; no debe
   confundirse con una referencia rota. Las referencias colgantes continúan
   siendo fallos duros de integridad.
6. La prueba de despliegue debe ser específica por runtime. El cordón actual de
   deep-opm-pro prueba Claude Code, pero no demuestra por sí mismo la instalación
   Codex; esa deuda quedó en el issue downstream.

## Artefactos y evidencia relevante

- Fuente canónica: `artefactos/skills/kora/modelamiento-opm/SKILL.md`.
- Fibra corregida:
  `artefactos/skills/kora/modelamiento-opm/referencias/bundle-deep-opm-pro.md`.
- SSOT absorbida: `artefactos/conocimiento/fxsl/spec-forja-opl-es.md`, v1.3.0,
  §2.0 `R-ENT-2-APUNTE`.
- Evidencia opforja consultada: `app/src/opl/opciones.ts`,
  `app/e2e/45-opl-proceso-apunte.spec.ts`, `app/src/ui/CommandPalette.tsx`,
  `app/src/modelo/tipos/{apariencia,enlace}.ts` y
  `app/src/serializacion/validarIntegridad.ts` en `deep-opm-pro`.
- Commits opforja de procedencia: `6ae55b52` para la realización de
  `R-ENT-2-APUNTE` y `be3ac65c` como corte revisado durante la sesión.

## Aprendizajes destilados

- La documentación de integración envejece antes que los tipos: contrastar las
  fibras con los tipos, validadores y E2E reales antes de corregirlas.
- Un resultado verde para un target no prueba otro target. La paridad se
  verifica por cada combinación de fuente, emisión, sello e instalación.
- Tras editar una fuente transmutable, `velar --estricto` puede señalar
  únicamente emisiones rancias. Solo en ese caso acotado, re-transmutar es la
  reparación requerida; cualquier otro fallo debe resolverse antes de emitir.
- Las búsquedas de texto obsoleto deben distinguir doctrina vigente de
  procedencia histórica: borrar términos antiguos del historial destruiría
  trazabilidad, no corregiría el presente.
- `bun run mesa modelos` es un smoke de lectura útil para comprobar el puente
  sin mutar modelos; un `mesa push` exige el protocolo completo de no-clobber.
- En pneuma no hay una ceremonia de iniciación nombrada. La entrada efectiva es
  leer el canon indicado por `CLAUDE.md`, consultar el estado vivo y ejecutar
  las gates antes de intervenir.

## Cómo retomar

1. Leer `CLAUDE.md` y este handoff; si divergen, gana el canon.
2. Ejecutar `git fetch --prune origin`, revisar `git status -sb` y preservar los
   archivos del operador.
3. Consultar el estado vivo de ambos issues; el frente pendiente esperado es
   `deep-opm-pro#1`.
4. Antes de cerrar cualquier nuevo cambio, ejecutar:

   ```bash
   python3 kora.py velar --estricto
   python3 -m unittest discover -s tests
   ```

5. Si se modifica una fuente transmutable, reemitir solo mediante `kora.py` y
   verificar `transmutar --paridad`; nunca editar `_emision/` a mano.
