# Handoff vigente — 2026-07-18 — auditoría categorial integral de KORA

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git ni el estado vivo de los runtimes.

## Objetivo y alcance

Auditar `kora-pneuma` de extremo a extremo —mecánica, modelo de datos, ley,
transmutación, corpus categorial, consumidores OPM y skills— usando
`mente-omega` y `cat-thinking`; remediar errores demostrables sin expandir el
shape ni inventar una formalización mayor que la implementada.

Supuestos aplicados:

1. La teoría matemática tiene precedencia sobre metáforas heredadas y URNs.
2. Se conserva el núcleo formal que puede probarse; el resto se declara
   modelo, heurística o metáfora según su evidencia.
3. No se cambia el formato estable del sello ni los bytes del emisor cuando la
   corrección es doctrinal.
4. `no-instalada` no autoriza instalar una capacidad nueva por sorpresa.

## Veredicto

El repositorio ya tenía una mecánica sólida, pero su discurso categorial
confundía repetidamente clasificación con identidad y semejanza estructural con
teorema. El problema principal no era ausencia de teoría de categorías, sino
**sobreafirmación**: se llamaban funtores, adjunciones, bisimulaciones,
pushouts, sheaves, topoi u operads a mappings y patrones aún no tipados.

Tras este incremento:

- la firma PMI×LFS **clasifica** y no individúa;
- la proyección numérica por target es el único funtor propio de KORA
  demostrado en este alcance;
- esa proyección es un coreflector entre categorías delgadas;
- la emisión completa es serialización determinista, no funtor demostrado;
- el sello certifica procedencia, proyección y congruencia, no naturalidad,
  safety, bisimulación ni composición Kleisli;
- las relaciones del frontmatter son grafos generadores; la categoría libre de
  caminos y el orden por alcanzabilidad son construcciones derivadas;
- el corpus ICAS declara localmente si una aplicación es formal, un modelo bajo
  hipótesis, una heurística o una metáfora.

## Núcleo formal añadido

`urn:kora:kb:cat-kora-kernel` prueba:

1. las firmas bien formadas constituyen un subretículo acotado `V`;
2. cada dominio soportado `D_T` y su imagen `I_T` son categorías delgadas;
3. `P_T(v)=min(v,c_T)` es monótono, descendente e idempotente;
4. para la inclusión `J_T : I_T -> D_T`, se cumple `J_T ⊣ P_T`;
5. el coreflector no se extiende automáticamente al transporte de cuerpos,
   archivos o conducta.

El contraejemplo vivo `cat-thinking`/`ifml` demuestra que igual arnés, forma,
vector y sigma no implican mismo artefacto, tipo semántico ni bisimulación.

## Superficies corregidas

- `ALMA.md` y `ley/0..4`: identidad, frontera formal, coreflexión, relaciones,
  alcance del sello y estatus de koraficación.
- `kora.py`: terminología y documentación del contrato; el algoritmo y los
  bytes emitidos no cambiaron.
- `cat-agent-coalgebra`: tipo reactivo corregido a
  `H(X)=(M(O×X))^I` y `c:U->H(U)`.
- `cat-agent-modulo`, `cat-foundations`, `aufbau-persona-agente` y
  `alma-de-kora`: retirada de isomorfismos y puentes no demostrados.
- 24 piezas ICAS: correcciones locales de functorialidad, adjunciones,
  universalidad, (co)álgebras, efectos, enriquecimiento, topoi, temporalidad,
  infraestructura, calidad y procesos.
- Puente OPM y cuatro consumidores: una firma de frontera solo expresa
  equivalencia observacional relativa; merge/pushout y dualidades quedan
  condicionados a su construcción.
- `cat-thinking` y referencias: regla adversarial de estatus más débil,
  fuentes primarias y obligación de tipar categorías, morfismos y leyes.
- `autoria-de-persona`, `agent-architect`,
  `auditoria-artefactos-kora`, `modelamiento-opm` y canon de diseño:
  eliminación de inferencias de identidad o garantía a partir de firma/sello.

## Evidencia de cierre

- `python3 kora.py velar --estricto`: 13/13 checks.
- `python3 -m unittest discover -s tests`: 189 pruebas, todas verdes.
- Se añadieron propiedades exhaustivas de matrices: dominio inicial,
  monotonía, descenso, idempotencia, adjunción y preservación de las cinco
  leyes inter-eje.
- Se añadió prueba de que dos URNs pueden compartir firma sin colapsar
  identidad y de que `depende` no exige cierre transitivo materializado.
- `git diff --check` y `python3 -m py_compile kora.py`: verdes.
- Paridad global: `116 fiel`, `0 desviadas`, `11 no-instaladas`,
  `0 sin-emisión`.

## Emisiones e instalaciones

Se regeneraron las 18 superficies derivadas de:

- `auditoria-artefactos-kora`;
- `autoria-de-persona`;
- `cat-thinking`;
- `modelamiento-opm`;
- `agent-architect`.

Se actualizaron las doce instalaciones que ya existían en Claude Code, Codex y
OpenCode para las cuatro skills. No se instaló `agent-architect` en targets
donde ya figuraba ausente ni la variante OpenClaw de `autoria-de-persona`;
`no-instalada` es informativo y no bloquea.

## Fuentes primarias contrastadas

- Libkind y Spivak, *Pattern Runs on Matter*:
  https://arxiv.org/abs/2404.16321
- Riehl, *Category Theory in Context*:
  https://emilyriehl.github.io/files/context.pdf
- Rutten, *Universal Coalgebra*:
  https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf
- Stacks Project, *Sheafification*:
  https://stacks.math.columbia.edu/tag/007X
- Schultz y Spivak, *Temporal Type Theory*:
  https://arxiv.org/abs/1710.10258
- Schultz, Spivak y Vasilakopoulou, *Dynamical Systems and Sheaves*:
  https://arxiv.org/abs/1609.08086

## Deudas explícitas

1. No existe todavía una categoría de artefactos y otra de productos runtime
   con acción del emisor sobre morfismos.
2. `naturalidad-xi`, `cierre-safety` y `composicion-kleisli` son nombres
   históricos de deuda, no propiedades verificadas.
3. No hay puente formal demostrado PMI×LFS -> `Poly` ni desde la firma hacia
   la coálgebra conductual.
4. La auditoría corrige afirmaciones categoriales; no valida empíricamente cada
   paper aplicado ni convierte todo ICAS en un desarrollo formal completo.
5. La continuidad clínica/OpenClaw anterior permanece en
   `_archivo/HANDOFF-2026-07-18-agentes-clinicos-openclaw.md` y en el handoff
   vigente de `openclaw-fleet`; sus pendientes operativos no fueron alterados.

## Siguiente acción recomendada

Si se desea ampliar el núcleo formal, elegir **un solo puente** con valor
operacional —preferentemente una categoría mínima de artefactos y una semántica
de observación del emisor—, definir objetos/morfismos y probar leyes antes de
recuperar términos como naturalidad o bisimulación. No expandir PMI×LFS ni el
sello mientras esa utilidad no esté demostrada.

## Cómo retomar

1. Leer `CLAUDE.md`, este handoff y el estado Git vivo.
2. Ejecutar `python3 kora.py velar --estricto` y la suite completa.
3. Leer `urn:kora:kb:cat-kora-kernel` antes de modificar ley o transmutación.
4. Aplicar la rúbrica de `cat-thinking`: formal > modelo > heurística >
   metáfora, usando siempre el estatus más débil suficiente.
5. Ante cambios agénticos, reemitir, pasar gates y verificar paridad por URN;
   ante cambios de `ley/3` o del emisor, ejecutar paridad global.

## Rollback

Usar `git revert`, nunca `reset --hard`. Tras revertir, regenerar las cinco URNs
afectadas y repetir `velar`, tests y paridad global. Las instalaciones externas
deben reconciliarse mediante `transmutar --aplicar`, no editarse a mano.
