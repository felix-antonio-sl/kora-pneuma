# Loop closure checklist

Una tarea **NO esta lista** hasta que su aceptacion y sus riesgos reales quedan
cubiertos sobre el arbol exacto.

## Pasos del loop

1. **Outcome** — verificar el comportamiento o journey solicitado.
2. **Prueba focal** — ejecutar la comprobacion mas cercana al cambio.
3. **Ampliacion proporcional** — sumar build, tests, typecheck, lint o
   integracion solo cuando existen y la superficie cambiada puede afectarlos.
4. **Feel** — usar o revisar la solucion; no basta con que compile.
5. **Patch listo** — un cambio coherente y verificable; commit solo si fue
   autorizado.

## Reglas

- Un `FAIL` relevante bloquea; diagnosticar y corregir antes de cerrar.
- Registrar cada comprobacion pertinente como `PASS`, `FAIL`, `ABSENT` o
  `NOT_RUN`. Los dos ultimos no aportan evidencia: si el check cubre aceptacion
  o un riesgo real, bloquean; si no, se declaran con razon y limite exactos.
- `ABSENT` no obliga a crear build, test runner o linter para satisfacer una
  lista; agregar tooling requiere valor propio y alcance explicito.
- Un check global ajeno a la superficie no se vuelve gate por existir;
  ejecutarlo solo si el blast radius lo justifica.
- En watch mode, identifica la ejecución, candidato y resultado final; un
  proceso abierto sin resultado atribuible no demuestra una comprobación.

## Gotchas

- **Monorepo**: builds parciales — verificar que el build del paquete afectado pasa.
- **Tests lentos de integracion**: ejecutar solo los relevantes, no la suite completa.
- **Deps lockfile**: si cambian deps, regenerar lockfile y commitear ambos juntos.
- **Migraciones**: ensayar compatibilidad y recuperación con datos sintéticos
  o autorizados; distinguir rollback disponible de restauración o reparación
  hacia adelante. No afirmar reversión cuando se pierde información.
- **Type checking**: en TS, type-check no es lo mismo que build; correr ambos cuando aplique.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| "Cambio chico, no verifico" | Skip silencioso del outcome | Ejecutar la prueba focal aplicable |
| "No hay linter, creo uno" | Tooling inventado para llenar una casilla | Declarar `ABSENT`; no expandir alcance |
| Loop abierto declarado hecho | Tarea reportada cerrada sin verificar | Solo declarar hecho post-loop |
| Watch abierto sin resultado atribuible | No identifica qué se comprobó | Conservar resultado y candidato de la ejecución focal |
| Suite global por reflejo | Tiempo sin reduccion de riesgo | Ampliar solo por blast radius |

## Cierre

Reporte minimo al cerrar:

- outcome: `PASS` / `FAIL`
- checks aplicables: `PASS` / `FAIL` / `ABSENT` / `NOT_RUN`
- integracion y feel: estado o limite exacto
- patch o commit autorizado: identidad reproducible
