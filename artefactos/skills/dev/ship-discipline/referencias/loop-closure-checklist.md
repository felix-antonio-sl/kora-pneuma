# Loop closure checklist

Una tarea **NO esta lista** hasta que el loop cierra. Sin excepciones.

## Pasos del loop

1. **Build** — compilar/transpilar el proyecto. Si falla, corregir antes de seguir.
2. **Test** — ejecutar tests relevantes al cambio. Si no hay y el cambio es no trivial, escribirlos.
3. **Lint** — corregir warnings criticos.
4. **Integracion** — el cambio se integra sin romper imports, tipos o deps existentes.
5. **Feel** — la solucion se siente correcta al usarla; no solo compila, esta bien.
6. **Commit atomico** — un cambio = un commit, mensaje descriptivo.

## Reglas

- Si el **build** falla, NO seguir adelante. Corregir primero.
- Si los **tests** fallan, diagnosticar y arreglar antes de continuar.
- **No saltear pasos** aunque el cambio parezca trivial.
- Si el proyecto no tiene test runner configurado, declararlo y sugerir setup minimo (no fingir que el loop cerro).
- **Watch mode no cuenta** como validacion: ejecutar build/test explicitamente.

## Gotchas

- **Monorepo**: builds parciales — verificar que el build del paquete afectado pasa.
- **Tests lentos de integracion**: ejecutar solo los relevantes, no la suite completa.
- **Deps lockfile**: si cambian deps, regenerar lockfile y commitear ambos juntos.
- **Migraciones**: si tocan schema, correr migracion en local + verificar rollback antes de commit.
- **Type checking**: en TS, type-check no es lo mismo que build; correr ambos cuando aplique.

## Antipatrones

| Antipatron | Falla | Correccion |
|---|---|---|
| "Cambio chico, no testeo" | Skip silencioso del loop | No saltear; sumar test si no hay |
| Loop abierto declarado hecho | Tarea reportada cerrada sin verificar | Solo declarar hecho post-loop |
| Watch mode como validacion | False positive: cambio se rompe en CI | Build/test explicito en cada cierre |
| Commit gigante | Multiples cambios mezclados | Commit atomico: un cambio, una intencion |

## Cierre

Reporte minimo al cerrar:

- build: verde / falla
- tests: verde / falla / no aplica
- lint: verde / warnings ignorables / falla
- integracion: verde / pendiente
- commit: hash o pendiente
