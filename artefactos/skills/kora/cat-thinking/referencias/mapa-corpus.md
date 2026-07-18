# Mapa del corpus ICAS-BoK

Las 24 piezas del corpus, resueltas por URN a su versión viva. Para cada pieza:
URN canónica, vocablo central y cuándo activarla. Esta es **navegación**, no
evidencia matemática. Las URNs son SSOT interna; una afirmación formal exige
además prueba o fuente primaria.

## Arco I — Fundamentos (00–05)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-sintesis` | ADN cognitivo, mapa, transicion | duda sobre que pieza usar; primer contacto con el corpus |
| `urn:fxsl:kb:icas-composicion` | categoria, morfismo, asociatividad, identidad, dualidad | algo no compone; la falla parece de "encadenamiento" |
| `urn:fxsl:kb:icas-preservacion` | funtor, faithful, full, schema → instancia, migracion | una traduccion entre sistemas pierde algo |
| `urn:fxsl:kb:icas-comparacion` | transformacion natural, polimorfismo, equivalencia, 2-cat | dos implementaciones se afirman equivalentes pero discrepan |
| `urn:fxsl:kb:icas-identidad-relacion` | hom-funtor, Yoneda, embedding, presheaves | duda sobre como entender un componente desde afuera (API, queries, interaccion) |
| `urn:fxsl:kb:icas-universales` | producto, coproducto, pullback, pushout, limite, colimite, sketch | hay que evaluar si combinar/ajustar/JOIN/MERGE satisface un problema universal |

## Arco II — Estructura adjunta y enriquecida (06–08b)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-adjunciones` | unit, counit, free/forgetful, Sigma-Delta-Pi, Galois | tradeoff relajacion/formalizacion; migracion entre schemas; preservacion de constraints |
| `urn:fxsl:kb:icas-composicion-estructura` | categoria monoidal, string diagram, simetria, CCC, Curry-Howard-Lambek | composicion con paralelismo, currying, comunicacion via diagramas |
| `urn:fxsl:kb:icas-enriquecimiento` | Bool/Cost-category, Lawvere, profunctor, cambio de base | la relacion no es binaria sino cuantitativa (latencia, fiabilidad, costo) |
| `urn:fxsl:kb:icas-higher-categories` | 2-cat, (∞,1)-cat, simplicial set, HoTT | relaciones entre relaciones; "igualdad" debilitada a homotopia |

## Arco III — Efectos, extension, interaccion (09–11)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-efectos` | monada, Kleisli, Eilenberg-Moore, comonada, coalgebra, bisimulacion, ley distributiva | funciones con efectos no componen; observabilidad necesita estructura; bisimular comportamiento |
| `urn:fxsl:kb:icas-extension` | end, coend, Kan extension, Grothendieck, fibration | extender un funtor parcial; integrar contextos; evaluar modelos de atencion por Kan extension |
| `urn:fxsl:kb:icas-interaccion` | polynomial functor, lente dependiente, comonoide, sistemas dinamicos | API como contrato bidireccional; sistemas que interactuan via interfaces tipadas |

## Arco IV — Logica interna y safety (12–12b)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-topoi` | presheaf, sheaf, clasificador subobjetos, logica intuicionista, geometric morphism, multi-tenancy | evaluar modelos de verdad contextual, permisos, consistencia y visibilidad cuando estructuras mas simples no bastan |
| `urn:fxsl:kb:icas-safety-alignment` | alineamiento, ICAR, Goodhart, coherencia, verificacion vs validacion | safety, alineamiento, riesgo de proxy/Goodhart |

## Arco V — Escala y agencia (13–14b)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-escala` | operad, wiring diagram, double cat, structured cospan, megamodelo, SoS | jerarquia de composicion; modulos con interfaces compartidas; verificacion composicional |
| `urn:fxsl:kb:icas-agencia` | free monad, cofree comonad, plan/sustrato, P-D-A, pattern runs on matter, contextad, memoria | sistemas agenticos; delegacion; uso de herramientas; emergencia |
| `urn:fxsl:kb:icas-protocolos` | session type, coreografia, saga, tolerancia a fallas | protocolos distribuidos; orquestacion vs coreografia |

## Arco VI — Tiempo, lifecycle, procesos (15–17)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-tiempo` | behavior type, sheaf temporal, hybrid sheaf, contrato composicional, delay aditivo | invariantes temporales; SLA; circuit breaker; event sourcing |
| `urn:fxsl:kb:icas-lifecycle` | V-model, DevOps, drift, deuda tecnica categorial, version | gobierno del lifecycle; medir drift; describir deuda con vocabulario formal |
| `urn:fxsl:kb:icas-procesos` | requirements, design, testing, maintenance, factorizacion | hablar de la actividad de ingenieria misma como proceso categorico |

## Arco VII — Calidad, patrones, infra (18–20)

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:fxsl:kb:icas-calidad-riesgo` | quality attribute, RAM, riesgo, resiliencia, garantia | hablar de calidad/riesgo con vocabulario formal |
| `urn:fxsl:kb:icas-patrones` | patron arquitectonico, agentico, anti-patron, wrapper functor | reconocer patron; nombrar anti-patron; multi-modelo |
| `urn:fxsl:kb:icas-infraestructura` | candidatos: tool use como profunctor, IaC como funtor, SoS, 2-cat | evaluar modelos formales para infraestructura autonoma, uso de herramientas y gobernanza |

## Núcleo propio de KORA

| URN | Vocablo central | Activar cuando |
|-----|-----------------|----------------|
| `urn:kora:kb:cat-kora-kernel` | retículo de firmas, coreflexión por target, fidelidad contravariante, grafos generadores | evaluar la firma, matrices o relaciones de KORA |
| `urn:kora:kb:cat-kora-semantica-operacional` | subobjetos de validación, lifecycle parcial, censo, emisión, paridad, ley | evaluar categorialmente un gesto concreto de KORA sin forzar functorialidad |
| `urn:kora:kb:cat-contrato-ingenieria-agentica` | `Spec/Model/Runtime`, coálgebra, efectos, wiring, capabilities, safety | afirmar que un agente compone, preserva conducta, está limitado o es seguro |

## Como navegar el corpus

1. Si **no sabes por donde empezar**, abre `00-sintesis` (`icas-sintesis`). Tiene el ADN cognitivo y el mapa completo del corpus.
2. Si **conoces el sintoma** del problema, abre `disparadores-canonicos.md` (esta misma fibra).
3. Si **conoces el vocablo categorial**, usa esta tabla.
4. Si **ninguno aplica**, usa `Grep`/`Read` sobre los archivos `icas-*.md` del corpus en el catalogo central de KORA pneuma.
5. Si **el corpus no cubre el problema**, declararlo. No inventar.
6. Si una afirmación formal es dudosa, consulta una fuente primaria y corrige
   o degrada el corpus si existe conflicto.
