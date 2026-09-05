
# custodio-kora

## Proposito

Custodiar la coherencia normativa de KORA. La skill carga el canon vigente,
audita tensiones entre specs, artefactos, toolchain y docs derivadas, y ayuda a
mejorar la norma o su implementacion con cambios pequenos, verificables y
trazables.

No es un agente always-on ni una autoridad nueva. Es una habilidad portable
para que un operador o agente anfitrion mantenga KORA alineado con su fuente de
verdad: filesystem con manifests validos y specs vigentes.

## Cuando Usar

- Auditar una spec o cambio normativo antes de promoverlo.
- Corregir una contradiccion entre `governance/`, `ontology/`,
  `serialization/`, `runtime/`, artefactos y toolchain.
- Revisar si un agente, skill o conocimiento nuevo respeta URNs, lifecycle,
  vector PMI x LFS, `autoria-spec` o `knowledge-spec`.
- Diagnosticar fallos de `python3 toolchain/kora check --strict`.
- Decidir donde vive una regla: constitucion, ontologia, serializacion,
  runtime, extension, artefacto o documento derivado.
- Mantener KORA a punto despues de una reorg, migracion o transmutacion.

## Cuando No Usar

- Contenido de dominio no-KORA: delegar al agente o skill de dominio.
- Diseno categorial puro: usar `urn:kora:artefacto:cat-thinking`.
- Modelado formal de sistemas con OPM: usar `urn:kora:artefacto:modelamiento-opm`.
- Publicacion, push o despliegue: esta skill prepara y verifica; el operador
  decide la operacion externa.
- Reconstruccion desde artefactos meta-KORA historicos: esta prohibido como
  fuente de diseno por `urn:kora:kb:meta-kora-rebuild-directive`.

## Workflow

### 1. `triaje`

Clasificar la solicitud:

| Modo | Pregunta guia | Salida |
|------|---------------|--------|
| `auditar` | que incoherencia o riesgo se quiere comprobar | findings priorizados |
| `mejorar` | que regla o spec debe cambiar y por que | patch minimo + gates |
| `reparar` | que check, test o artefacto falla | causa raiz + fix |
| `orientar` | donde vive la autoridad normativa | capa propietaria + URNs |

Si la solicitud afecta `master`, host roles o push, verificar
`python3 toolchain/kora host` antes de recomendar acciones operativas.

### 2. `cargar-canon`

Resolver las URNs necesarias con `python3 toolchain/kora resolve`. Leer siempre
la regla propietaria, no solo referencias indirectas. Para el mapa completo,
usar `referencias/canon-operativo.md`.

Canon minimo para cambios agenticos:

1. `urn:kora:kb:gobernanza`
2. `urn:kora:kb:harness-spec`
3. `urn:kora:kb:autoria-spec`
4. `urn:kora:kb:autoria-spec (absorbe metodologia desde v2.0)`

Canon minimo para knowledge:

1. `urn:kora:kb:gobernanza`
2. `urn:kora:kb:md-spec`
3. `urn:kora:kb:knowledge-spec`

Canon minimo para runtime:

1. `urn:kora:kb:runtime-spec-md`
2. `urn:kora:kb:multiagente-spec`
3. `urn:kora:kb:transmutation-spec`
4. runtime-extension concreta.

### 3. `localizar-propietario`

Antes de cambiar nada, decidir la capa propietaria:

| Sintoma | Propietario probable |
|---------|----------------------|
| identidad, precedencia, lifecycle, source of truth | `gobernanza` |
| vector, atlas, leyes inter-eje | `harness-spec` |
| `AGENT.md`/`SKILL.md`, forma material, fibras | `autoria-spec` |
| KORA/MD, relations, traces, knowledge | `md-spec` o `knowledge-spec` |
| ejecucion o proyeccion a target | `runtime-spec-md`, `multiagente-spec`, `transmutation-spec` o extension |
| comandos, gates, catalogo, checks | `procesos-spec` y toolchain |

No mover la regla a otra capa por conveniencia.

### 4. `diagnosticar-invariantes`

Aplicar `referencias/checklist-auditoria-normativa.md`. Cada finding debe
contener:

- regla propietaria por URN y archivo local.
- evidencia concreta: linea, comando, test o check.
- impacto: que se rompe si no se corrige.
- fix recomendado: artifact fix, spec fix, check fix o deuda declarada.

Separar hechos verificados de inferencias.

### 5. `disenar-cambio`

Si hay que mejorar la norma, usar `referencias/protocolo-mejora-specs.md`.
Principios:

- cambio minimo en la capa propietaria.
- no alterar docs derivadas salvo regeneracion deliberada.
- no relajar specs para encubrir un artefacto mal formado.
- si se cambia una regla, actualizar checks o tests que la hacen ejecutable.
- declarar perdida, excepcion o deuda residual de forma explicita.

### 6. `aplicar-cambio`

Editar solo el perimetro necesario. Para artefactos agenticos, conservar el
shape unificado de `autoria-spec`: `_manifest`, `version` fuera del URN,
`extensions.kora.vector_ontologico` y payload bajo `artefacto:`.

Para specs, conservar el perfil KORA/MD, `relations`, versionado y precedencia.

### 7. `verificar-gates`

Para un artefacto o subtree concreto en staging, empezar por gates acotados:

```bash
python3 toolchain/kora check --strict --path <subtree>
python3 toolchain/kora lint-md <subtree>
```

Si el artefacto es una habilidad en staging, la CLI publica de transmutacion
puede no resolverla por `--agent` hasta que viva en `artifacts/skills/{ns}/{id}`.
En ese caso, validar shape, URNs y dominio con gates acotados; ejecutar
`transmute --target agentskills --dry-run` despues de promocion o con un helper
interno deliberado.

Gate base de repositorio:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

Si se tocaron specs, toolchain o comportamiento compartido:

```bash
python3 -m unittest discover -s tests
```

Si se tocaron knowledge o relaciones:

```bash
python3 toolchain/kora kb-graph --json --orphans
```

Si se tocaron docs derivadas deliberadamente:

```bash
python3 toolchain/kora sync-docs
```

## Reglas De Diagnostico

1. Una contradiccion normativa se corrige en la capa propietaria mas alta que
   la causa, no en el consumidor mas visible.
2. Un fallo de check puede significar tres cosas: artefacto invalido, check
   desalineado o spec incompleta. Diagnosticar antes de editar.
3. Un runtime output no es fuente. Si diverge, se regenera desde IR.
4. Una URN desconocida no se normaliza a path; se indexa, corrige o elimina.
5. Una excepcion nueva debe entrar como regla, riesgo o deuda, nunca como
   silencio operativo.

## Recursos

### Referencias

- `referencias/canon-operativo.md`: mapa de capas, URNs y autoridad.
- `referencias/checklist-auditoria-normativa.md`: checklist para findings.
- `referencias/protocolo-mejora-specs.md`: protocolo para cambios normativos.
