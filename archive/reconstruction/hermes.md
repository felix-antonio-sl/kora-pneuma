# Antecedentes de Hermes del 2026-09-05

Registro de preparación, adopción y comprobaciones ya realizadas. Los comandos
pertenecen a aquella etapa. El [contrato vigente](../../docs/hermes.md) describe
la realización y las comprobaciones actuales.

## Consumidores encontrados antes del relevo

Este es un corte inicial **2026-09-05**, útil para preparar la migración; el
filesystem se vuelve a consultar antes de alterar un consumidor. La siguiente
tabla identifica solo contenido con procedencia KORA. No atribuye a KORA las
otras skills, identidad o configuración de los perfiles mixtos.

| Raíz bajo `~/.hermes` | Identidad KORA | Skills KORA activas observadas |
| --- | --- | --- |
| `skills/` | — | `auditoria-exposicion-kora`, `conducir-decisiones-hodom`, `hermes-agent-specialist`, `hospitalizacion-domiciliaria`, `modelamiento-opm`, `ship-discipline` |
| `profiles/dev/` | — | Las mismas seis de la raíz default |
| `profiles/director-tecnico-hodom/` | `urn:salud:artefacto:director-tecnico-hodom` | `conducir-decisiones-hodom`, `hospitalizacion-domiciliaria` |
| `profiles/dov-dori/` | `urn:fxsl:artefacto:dov-dori` | `modelamiento-opm` |
| `profiles/kora/` | `urn:kora:artefacto:kora` | `util-x` |
| `profiles/steipete/` | `urn:dev:artefacto:steipete` | `ship-discipline`, `util-x` |
| `profiles/hodom-dt/`, `profiles/hospitalista/`, `profiles/telemedicina/`, `profiles/urgencia/` | — | En cada perfil: `hermes-agent-specialist`, `ship-discipline` |

Los cuatro manifiestos de agentes carecen de `source`; `hermes profile update`
no tiene un origen registrado para ellos. `util-x` aparece fuera de las listas
de propiedad de sus perfiles; su nombre no autoriza descartarlo. La raíz default
y `dev` también conservan una versión de `hermes-agent-specialist` en `.archive`,
excluida del discovery. El inventario reproducible no lee `.env`, `auth.json`,
memoria ni sesiones:

```sh
python3 scripts/probe_hermes.py --inventory
```

La preparación de adopción compara **bytes y modos** de cada archivo con
`_emision/hermes` anterior. Para versiones rezagadas identifica el contenido
fuente por el hash del sello en Git y exige igualdad del archivo instalado
completo, incluyendo wrapper y modo. No ejecuta el núcleo antiguo. El script
produce solo un JSON privado bajo `._local/`, con modo `0600`, hashes, paths y
conteos de estado ajeno; no registra sus cuerpos:

```sh
python3 scripts/plan_hermes_adoption.py --legacy-root /ruta/al/repositorio-legado-preservado
```

El origen legado debe indicarse explícitamente y ser distinto del catálogo
activo. Esta utilidad prepara una migración; el mantenimiento normal utiliza
`install`, `status`, `recover` y `rollback`.

El corte de preparación dio **96 archivos adoptables, 4 candidatos a retiro,
0 ambiguos, 26 bundles y 13 archivos nuevos**. Las cuatro versiones antiguas
identificadas exactamente son SOUL Steipete `1.6.0`, Modelamiento OPM `3.0.0`,
Hermes Specialist `2.3.0` y Ship Discipline `1.2.0`. El plan guarda el commit y
hash fuente que justifican cada igualdad. En perfiles mixtos, cada bundle
declara el producto del catálogo nuevo y el prefijo del perfil actual: permite
actualizar sus skills in situ conservando personalidad, configuración y estado.
Incluye también los perfiles nuevos `fugaz` y `agent-architect` y la clausura de
skills de los seis agentes. Estos conteos se regeneran tras cambios de fuente;
constituyen un plan, no un recibo de instalación.

Los candidatos a retiro son dos copias de un script de auditoría que ya no
pertenece al bundle reconstruido y dos copias de `util-x`. Para este último se
acreditó la función: sus metadatos, cuerpo y sello coinciden con la skill
sintética definida en `tests/test_kora.py:29-44` del producto anterior. No existe
como producto activo ni está declarado en los manifiestos de sus perfiles. El
evento que lo instaló **no está acreditado**; no se revisaron conversaciones
personales para atribuirlo. El plan registra sus hashes como candidatos y no
borra archivos. Las skills en `.archive` y el resto del estado ajeno permanecen
fuera de adopción y retiro.


## Independencia e instalación observadas

El 2026-09-05 el catálogo externo creado y actualizado por la KORA nueva pasó
además **la inferencia real de independencia**. El runtime, la autenticación y
los productos estaban montados en lectura; los repositorios anteriores y el de
construcción eran inaccesibles. Con seis llamadas API, `gpt-6-astra` y esfuerzo
`max`, Hermes cargó `evaluar-envios`, leyó la fuente vigente y devolvió el JSON
completo esperado: `AUTORIZADA`, `DIFERIDA`, `UNKNOWN`, `AUTORIZADA`, `DENEGADA`
para los casos A–E, distancia `UNKNOWN` y versión `PZ_6139_V2`.

El oracle no formó parte del prompt. Los productos y la metadata del auth
permanecieron intactos y no se persistió material de credenciales. La prueba
dispuso solo de herramientas de lectura: leyó el conocimiento por el mapa de
rutas nativo, sin ejecutar el comando `resolve` que la skill también ofrece.
Los pasos de autoría, actualización e instalación de ese mismo corpus, y su
alcance probatorio, están en [independencia](migracion.md#independencia-comprobada).

## Instalación comprobada después del relevo

El 2026-09-05 se actualizaron las realizaciones desde la raíz activa
`/home/felix/kora-pneuma`. Hermes quedó con 37 bundles administrados, incluidas
las instancias de skills en perfiles mixtos. La adopción y el retiro se hicieron
por archivos de propiedad acreditada, conservando los originales desplazados.
Las seis ubicaciones manuales de maquinaria se sustituyeron por sus funciones
vigentes según la [revisión de migración](migracion.md#consumidores-manuales-de-hermes).

La comprobación final leyó los perfiles instalados `agent-architect`,
`director-tecnico-hodom`, `dov-dori`, `fugaz`, `kora` y `steipete` en una vista
temporal de solo lectura, con red bloqueada. Los archivos coincidieron con el
renderer activo en bytes y modos; los seis SOUL y sus mapas completos llegaron
al prompt nativo con `openai-codex/gpt-6-astra`, esfuerzo `max` y ventana
reconocida de 1.050.000 tokens. Las once instancias de skills requeridas se
descubrieron y `skill_view(preprocess=False)` devolvió sus cuerpos completos.

El comprobador registró cero intentos de leer autenticación, memoria o sesiones
personales. Esta revisión no inició conversación; la inferencia real corresponde
al recorrido independiente descrito arriba. Sus recibos privados permanecen bajo
`._local`; no forman un inventario manual de mantenimiento.

El mantenimiento general instaló después las tres skills declaradas que aún
faltaban en la raíz: `auditoria-artefactos-kora`, `autoria-de-persona` y
`mente-omega`. Se comprobaron sus nueve archivos, incluidos los seis recursos
de mente omega, contra fuente y recibos. Las tres pasaron el parser, discovery
y `skill_view` nativos en una vista de solo lectura, sin autenticación personal
ni conversación. El registro final contiene 19 bundles Hermes de raíz y agentes,
más 18 instancias en perfiles mixtos. Repetir la instalación conserva tanto
los archivos como el diario del último rollback.
