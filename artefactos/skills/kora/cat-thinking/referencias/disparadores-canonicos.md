# Disparadores canonicos — sintoma → pieza del corpus

Tabla de routing rapida desde el sintoma practico hacia la pieza del ICAS-BoK que aplica. Cuando la skill activa un disparador, abre la URN correspondiente con `Read` antes de aplicar el patron.

## Composicion y traduccion

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "encadeno A → B → C y se rompe en algun punto" | `urn:fxsl:kb:icas-composicion` | leyes de asociatividad e identidad violadas |
| "el orden de operaciones cambia el resultado" | `urn:fxsl:kb:icas-composicion` | dualidad / commutatividad de diagrama |
| "migro de X a Y y pierdo datos" | `urn:fxsl:kb:icas-preservacion` | funtor faithful falla; declarar perdida |
| "el ORM tira algo en serializacion" | `urn:fxsl:kb:icas-preservacion` | axioma de funtor (composicion/identidad) |
| "dos implementaciones se afirman equivalentes pero discrepan" | `urn:fxsl:kb:icas-comparacion` | transformacion natural rota |
| "compilo y el binario hace algo distinto que el codigo" | `urn:fxsl:kb:icas-preservacion` + `urn:fxsl:kb:icas-comparacion` | funtor + naturalidad |

## Combinaciones optimas

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "necesito JOIN entre tablas X e Y" | `urn:fxsl:kb:icas-universales` | pullback |
| "necesito MERGE entre repos X e Y" | `urn:fxsl:kb:icas-universales` | pushout |
| "tengo que combinar dos tipos en uno" | `urn:fxsl:kb:icas-universales` | producto |
| "tengo que ofrecer eleccion entre dos tipos" | `urn:fxsl:kb:icas-universales` | coproducto |
| "tengo que resolver una ecuacion sobre dos morfismos" | `urn:fxsl:kb:icas-universales` | ecualizador |

## Adjunciones y relajacion

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "un lado relaja, el otro formaliza" | `urn:fxsl:kb:icas-adjunciones` | unit/counit |
| "construyo libremente un X a partir de un Y" | `urn:fxsl:kb:icas-adjunciones` | free/forgetful |
| "migracion entre schemas X → Y" | `urn:fxsl:kb:icas-adjunciones` | Sigma-Delta-Pi |
| "currying / uncurrying / closures" | `urn:fxsl:kb:icas-composicion-estructura` | CCC, Curry-Howard-Lambek |

## Identidad y observabilidad

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "¿como entiendo este servicio sin abrir el codigo?" | `urn:fxsl:kb:icas-identidad-relacion` | Yoneda, hom-funtor |
| "¿como entiendo esta tabla sin mirar las filas?" | `urn:fxsl:kb:icas-identidad-relacion` | queries y FK como representante |
| "verifico que el refactor preservo comportamiento observable" | `urn:fxsl:kb:icas-efectos` | bisimulacion sobre coalgebra |
| "blue-green deployment afirma equivalencia" | `urn:fxsl:kb:icas-efectos` | bisimulacion |

## Efectos

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "funciones con efectos no componen" | `urn:fxsl:kb:icas-efectos` | monada, Kleisli |
| "tengo que componer dos efectos distintos" | `urn:fxsl:kb:icas-efectos` | ley distributiva, monad transformer |
| "necesito hacer fold/reduce sobre estructura recursiva" | `urn:fxsl:kb:icas-efectos` | catamorfismo como query |
| "el sistema mantiene estado y produce observaciones" | `urn:fxsl:kb:icas-efectos` | coalgebra |

## Logica interna y multi-tenancy

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "permisos no son binarios" | `urn:fxsl:kb:icas-topoi` | clasificador de subobjetos no-booleano |
| "feature flags por usuario / cohorte / rol" | `urn:fxsl:kb:icas-topoi` | presheaves, topos |
| "eventual consistency: lo que aun no se decidio" | `urn:fxsl:kb:icas-topoi` | logica intuicionista |
| "datos compartidos entre tenants con visibilidad parcial" | `urn:fxsl:kb:icas-topoi` | sheaves |

## Cuantitativo

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "latencias se acumulan al componer" | `urn:fxsl:kb:icas-enriquecimiento` | Cost-category, Lawvere |
| "fiabilidades multiplicativas" | `urn:fxsl:kb:icas-enriquecimiento` | [0,1]-category |
| "QoS, SLA con metricas continuas" | `urn:fxsl:kb:icas-enriquecimiento` + `urn:fxsl:kb:icas-tiempo` | enriquecimiento + behavior types |
| "threshold convierte cuantitativo en booleano" | `urn:fxsl:kb:icas-enriquecimiento` | cambio de base |

## Sistemas agenticos

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "diseno un agente con plan y ejecutor" | `urn:fxsl:kb:icas-agencia` | free monad / cofree comonad |
| "el agente usa herramientas" | `urn:fxsl:kb:icas-agencia` + `urn:fxsl:kb:icas-infraestructura` | profunctor agente↔herramienta |
| "memoria del agente" | `urn:fxsl:kb:icas-agencia` | contextad |
| "un patron corre sobre cualquier motor" | `urn:fxsl:kb:icas-agencia` | pattern runs on matter |
| "delegacion entre agentes" | `urn:fxsl:kb:icas-agencia` + `urn:fxsl:kb:icas-protocolos` | session types, coreografia |
| "tolerancia a fallas en orquestacion" | `urn:fxsl:kb:icas-protocolos` | sagas, compensaciones |

## Tiempo y lifecycle

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "valor que dura en el tiempo" | `urn:fxsl:kb:icas-tiempo` | behavior type, sheaf temporal |
| "circuit breaker, timeout" | `urn:fxsl:kb:icas-tiempo` | hybrid sheaf |
| "delays se suman" | `urn:fxsl:kb:icas-tiempo` | composicion aditiva con prueba |
| "drift entre version desplegada y especificada" | `urn:fxsl:kb:icas-lifecycle` | naturalidad rota |
| "deuda tecnica medida formalmente" | `urn:fxsl:kb:icas-lifecycle` | distancia a ideal categorial |
| "DevOps como bucle" | `urn:fxsl:kb:icas-lifecycle` | trace en categoria monoidal traced |

## Escala y SoS

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "pods en services en namespaces en clusters" | `urn:fxsl:kb:icas-escala` | operad |
| "interfaces compartidas entre modulos" | `urn:fxsl:kb:icas-escala` | structured cospan via pushout |
| "data flow vs functional dep" | `urn:fxsl:kb:icas-escala` | double category |
| "system of systems" | `urn:fxsl:kb:icas-infraestructura` + `urn:fxsl:kb:icas-escala` | 2-categoria con 2-celdas |

## Calidad y patrones

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "reconozco un Observer / Factory / Decorator / Strategy" | `urn:fxsl:kb:icas-patrones` | lectura categorica de patron clasico |
| "anti-patron: God Object" | `urn:fxsl:kb:icas-patrones` | falla de factorizacion |
| "anti-patron: tight coupling" | `urn:fxsl:kb:icas-patrones` | interfaz mal calibrada |
| "calidad medida con probabilidades" | `urn:fxsl:kb:icas-calidad-riesgo` | Kleisli sobre monada de prob |
| "garantia de SLA" | `urn:fxsl:kb:icas-calidad-riesgo` + `urn:fxsl:kb:icas-tiempo` | proposicion temporal sobre sheaf |

## Safety y alineamiento

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "metric proxy diverge del objetivo real" | `urn:fxsl:kb:icas-safety-alignment` | Goodhart |
| "verificacion formal vs validacion empirica" | `urn:fxsl:kb:icas-safety-alignment` | end vs coend |
| "alineamiento entre agente y principal" | `urn:fxsl:kb:icas-safety-alignment` | coherencia |

## Procesos de ingenieria

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "requirements vs design" | `urn:fxsl:kb:icas-procesos` | factorizacion de Needs → Capabilities |
| "testing como verificacion de conmutatividad" | `urn:fxsl:kb:icas-procesos` | bisimulacion + ends |
| "refactoring preserva comportamiento" | `urn:fxsl:kb:icas-procesos` | isomorfismo natural |

## Cuando ningun disparador encaja

1. Re-leer la pregunta del usuario y aplicar el protocolo de `reformulacion-categorial.md`.
2. Si tras reformular ningun disparador encaja, usar `Grep -rn "<vocablo>" ~/kora/artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`.
3. Si tampoco encuentra, declarar que el corpus no cubre el caso. **No inventar**.
