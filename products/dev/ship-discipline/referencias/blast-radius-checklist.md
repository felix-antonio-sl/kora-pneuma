# Blast radius checklist

Estimacion del impacto de un cambio antes de ejecutarlo.

## Criterios de estimacion

Antes de actuar, responder:

1. Cuantos archivos toca (directos + indirectos)?
2. Si sale mal, cuanto cuesta revertir?
3. Necesito explorar primero o ya se por donde va?
4. Puedo cerrar el loop solo (sin esperar a humano)?
5. El cuello de botella es implementacion o diseno?
6. Esto merece tooling nuevo o solo una instruccion mejor?
7. El contexto actual ayuda o ensucia?

## Tabla de niveles

| Nivel | Criterio | Topologia | Cuidados |
|---|---|---|---|
| **Bajo** | 1-3 archivos, reversible, sin deps cruzadas | Accion directa | Commit corto basta |
| **Medio** | 4-10 archivos, reversible, algunas deps | Secuencial con checkpoints | Tests relevantes + commit atomico |
| **Alto** | 10+ archivos, potencialmente irreversible, multiples deps | Plan antes de ejecutar | Validacion humana antes de actuar |

## Defaults

- Ante duda, estimar **hacia arriba**.
- **Schema** (DB, API, types) → siempre alto.
- **Dependencias** (add/remove/upgrade) → siempre alto.
- **Boundaries** (server/client, modulo/modulo) → siempre alto.
- **Estilo, formatting, docs** → siempre bajo.
- **Renombrado masivo** → medio o alto segun cobertura.

## Reglas

- Documentar la estimacion en una linea **antes** de actuar.
- Si la estimacion sube despues de empezar, **detener** y replanear.
- Comandos destructivos (rm -rf, drop table, force push) requieren
  confirmacion explicita, sin importar el blast radius nominal.
- Migraciones de DB siempre se tratan como blast radius alto.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| "Cambio chico" sin estimar | Subestimar acoplamiento | Estimar siempre, aunque parezca trivial |
| Estimacion optimista | Sesgo del autor | Estimar hacia arriba en duda |
| Plan elaborado para cambio bajo | Ceremonia ridicula | Estimar bajo, ejecutar directo |
| Cambio alto sin plan | Riesgo no gestionado | Plan + validacion humana antes de exec |
