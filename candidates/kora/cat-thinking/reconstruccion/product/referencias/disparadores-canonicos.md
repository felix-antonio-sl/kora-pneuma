# Disparadores canonicos — sintoma → pieza del corpus

Tabla de routing rapida desde el sintoma practico hacia una pieza candidata del ICAS-BoK. Un disparador **no demuestra** el patron de la tercera columna: obliga a abrir la URN, tipar la construccion y asignarle estatuto epistemico antes de usarla.

## Composicion y traduccion

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "encadeno A → B → C y se rompe en algun punto" | `urn:fxsl:kb:icas-composicion` | leyes de asociatividad e identidad violadas |
| "el orden de operaciones cambia el resultado" | `urn:fxsl:kb:icas-composicion` | dualidad / commutatividad de diagrama |
| "migro de X a Y y pierdo datos" | `urn:fxsl:kb:icas-preservacion` | identificar la propiedad concreta no preservada; *faithful* solo si hay funtor y falla en hom-sets |
| "el ORM tira algo en serializacion" | `urn:fxsl:kb:icas-preservacion` | comprobar primero si existe un funtor; si no, diagnosticar el mapping concreto |
| "dos implementaciones se afirman equivalentes pero discrepan" | `urn:fxsl:kb:icas-comparacion` | elegir la equivalencia observable; naturalidad solo con funtores tipados |
| "compilo y el binario hace algo distinto que el codigo" | `urn:fxsl:kb:icas-preservacion` + `urn:fxsl:kb:icas-comparacion` | buscar una propiedad semantica no preservada; funtor/naturalidad son modelos candidatos |

## Combinaciones y problemas universales

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "necesito JOIN entre tablas X e Y" | `urn:fxsl:kb:icas-universales` | evaluar un pullback sobre funciones tipadas; SQL con `NULL`, bags o outer joins requiere otra semantica |
| "necesito MERGE entre repos X e Y" | `urn:fxsl:kb:icas-universales` | evaluar si existe un cospan y un pushout en una categoria declarada; Git no lo garantiza |
| "tengo que combinar dos tipos en uno" | `urn:fxsl:kb:icas-universales` | posible producto, si satisface su propiedad universal |
| "tengo que ofrecer eleccion entre dos tipos" | `urn:fxsl:kb:icas-universales` | posible coproducto, si satisface su propiedad universal |
| "tengo que resolver una ecuacion sobre dos morfismos" | `urn:fxsl:kb:icas-universales` | posible ecualizador, con diagrama y universalidad explicitos |

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
| "verifico que el refactor preservo comportamiento observable" | `urn:fxsl:kb:icas-efectos` | bisimulacion solo con coalgebras y lifting relacional; si no, equivalencia observacional/test |
| "blue-green deployment afirma equivalencia" | `urn:fxsl:kb:icas-efectos` | candidato a bisimulacion; exige transiciones y observaciones tipadas |

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
| "permisos no son binarios" | `urn:fxsl:kb:icas-topoi` | empezar por un reticulo/Heyting; clasificador de subobjetos solo si se construye un topos |
| "feature flags por usuario / cohorte / rol" | `urn:fxsl:kb:icas-topoi` | presheaf/topos como modelo candidato, no consecuencia de tener flags |
| "eventual consistency: lo que aun no se decidio" | `urn:fxsl:kb:icas-topoi` | posible lectura intuicionista; no equivale a condicion de sheaf |
| "datos compartidos entre tenants con visibilidad parcial" | `urn:fxsl:kb:icas-topoi` | sheaf solo con sitio, restricciones, compatibilidad y pegado |

## Cuantitativo

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "latencias se acumulan al componer" | `urn:fxsl:kb:icas-enriquecimiento` | Cost-category, Lawvere |
| "fiabilidades multiplicativas" | `urn:fxsl:kb:icas-enriquecimiento` | [0,1]-category |
| "QoS, SLA con metricas continuas" | `urn:fxsl:kb:icas-enriquecimiento` + `urn:fxsl:kb:icas-tiempo` | enriquecimiento + behavior types |
| "threshold convierte cuantitativo en booleano" | `urn:fxsl:kb:icas-enriquecimiento` | comprobar laxitud monoidal; un umbral positivo sobre distancias puede romper composicion |

## Sistemas agenticos

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "diseno un agente con plan y ejecutor" | `urn:fxsl:kb:icas-agencia` | modelo *Pattern Runs on Matter* solo si se construyen polinomios y estructuras en `Poly` |
| "el agente usa herramientas" | `urn:fxsl:kb:icas-agencia` + `urn:fxsl:kb:icas-infraestructura` | profunctor como candidato si se tipan dos argumentos y sus acciones |
| "memoria del agente" | `urn:fxsl:kb:icas-agencia` | contextad |
| "un patron corre sobre cualquier motor" | `urn:fxsl:kb:icas-agencia` | el teorema de `Poly` da compatibilidad bajo hipotesis; no significa "cualquier" patron o motor |
| "delegacion entre agentes" | `urn:fxsl:kb:icas-agencia` + `urn:fxsl:kb:icas-protocolos` | session types, coreografia |
| "tolerancia a fallas en orquestacion" | `urn:fxsl:kb:icas-protocolos` | sagas, compensaciones |
| "`componible` dice que A y B componen" | `urn:kora:kb:cat-contrato-ingenieria-agentica` | exigir puertos, wiring, semántica y efectos; el campo solo declara candidato |
| "el allowlist prueba least-privilege o safety" | `urn:kora:kb:cat-contrato-ingenieria-agentica` | separar capacidades declaradas, autoridad runtime e invariante conductual |
| "la emisión conserva el comportamiento del agente" | `urn:kora:kb:cat-contrato-ingenieria-agentica` | hace falta interpretación runtime y un criterio de preservación |
| "diseñar o auditar un sistema agéntico autónomo completo" | `urn:kora:kb:cat-programacion-agentica-autonoma` | ruta transversal para planes, efectos, wiring, delegación, evals, liveness y lifecycle; resolver cada claim con la pieza atómica pertinente |
| "la teoría prueba delegación jerárquica dinámica" | `urn:kora:kb:cat-programacion-agentica-autonoma` + `urn:fxsl:kb:icas-agencia` | el resultado basado en arXiv 2410.08373 está retirado y queda en clase `X`; usar interfaces, protocolos, autoridad y receipts como contratos separados |

## Tiempo y lifecycle

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "valor que dura en el tiempo" | `urn:fxsl:kb:icas-tiempo` | behavior type; sheaf temporal solo con sitio y pegado |
| "circuit breaker, timeout" | `urn:fxsl:kb:icas-tiempo` | posible modelo hibrido; no es sheaf por definicion |
| "delays se suman" | `urn:fxsl:kb:icas-tiempo` | composicion aditiva con prueba |
| "drift entre version desplegada y especificada" | `urn:fxsl:kb:icas-lifecycle` | cuadrado de naturalidad como modelo solo si existen funtores y componentes |
| "deuda tecnica medida formalmente" | `urn:fxsl:kb:icas-lifecycle` | posible metrica/orden respecto de un ideal declarado |
| "DevOps como bucle" | `urn:fxsl:kb:icas-lifecycle` | traza solo si se exhibe una categoria monoidal trazada; un loop no basta |
| "el lifecycle de KORA es un funtor" | `urn:kora:kb:cat-kora-semantica-operacional` | la guía operacional no aporta una categoría ni un funtor; construir y comprobar ese modelo si hace falta |

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
| "garantia de SLA" | `urn:fxsl:kb:icas-calidad-riesgo` + `urn:fxsl:kb:icas-tiempo` | contrato temporal; sheaf solo si el modelo satisface sus hipotesis |

## Safety y alineamiento

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "metric proxy diverge del objetivo real" | `urn:fxsl:kb:icas-safety-alignment` | Goodhart |
| "verificacion formal vs validacion empirica" | `urn:fxsl:kb:icas-safety-alignment` | distincion prueba/evidencia; end/coend solo con bifuntor y universalidad tipados |
| "alineamiento entre agente y principal" | `urn:fxsl:kb:icas-safety-alignment` | coherencia |

## Procesos de ingenieria

| Sintoma | URN del corpus | Por que |
|---------|---------------|---------|
| "requirements vs design" | `urn:fxsl:kb:icas-procesos` | factorizacion de Needs → Capabilities |
| "testing como verificacion de conmutatividad" | `urn:fxsl:kb:icas-procesos` | diagrama conmutativo como especificacion; tests aportan evidencia, no una prueba universal por si solos |
| "refactoring preserva comportamiento" | `urn:fxsl:kb:icas-procesos` | elegir equivalencia observacional; isomorfismo natural solo con funtores tipados |

## Cuando ningun disparador encaja

1. Re-leer la pregunta del usuario y aplicar el protocolo de `reformulacion-categorial.md`.
2. Si tras reformular ningun disparador encaja, usar `Grep`/`Read` sobre los archivos `icas-*.md` del corpus en el catalogo central de KORA pneuma.
3. Si tampoco encuentra, declarar que el corpus no cubre el caso. **No inventar**.
