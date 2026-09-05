---
urn: urn:salud:kb:perfil-dev-personal-full
nombre: perfil-dev-personal-full
version: 1.0.0
estado: publicado
descripcion: "Perfil operativo para desarrollo y preparación HODOM en host privado mono-usuario: habilita PII/PHI y fuentes crudas sin trasladar esa excepción a Git, producción o publicación externa."
fuente: "Autoría de novo 2026-07-30 por decisión explícita del operador para /home/felix/projects, /home/felix/openclaw-fleet y /home/felix/kora-pneuma; generaliza el perfil personal ya aplicado a urgenciologo v3.13.0 y medico-hospitalista v1.10.0."
autor: FS
creado: 2026-07-30
lang: es
tags: [salud, hodom, desarrollo, pii, phi, monousuario, migracion]
familia: nota
---

# Perfil `DEV_PERSONAL_FULL`

## Finalidad y activación

`DEV_PERSONAL_FULL` es el perfil activo de desarrollo y preparación HODOM en
el host personal de `/home/felix`. Se aplica cuando coinciden todas estas
condiciones:

1. un único operador controla la cuenta, los procesos y los directorios;
2. la superficie es privada y no productiva;
3. el operador está autorizado a consultar las fuentes involucradas;
4. la tarea pertenece a desarrollo, preparación, conciliación, migración,
   prueba local, soporte clínico personal o continuidad del propio operador.

El perfil es una autorización operacional del propietario del host. No
constituye autorización institucional, aprobación regulatoria, piloto ni
habilitación productiva. Si una superficie deja de cumplir las cuatro
condiciones, se usa `INSTITUTIONAL_CONTROLLED`.

## Capacidades habilitadas

Dentro de superficies privadas del host:

- procesar, persistir, recuperar, cruzar y visualizar PII/PHI;
- usar nombre, RUT, domicilio, teléfono, texto clínico y geopuntos crudos para
  identidad, deduplicación, conciliación, trazabilidad y migración;
- consultar Drive, `hsc-agent-cli`, bases locales, extracts, archivos privados,
  memoria, sesiones y mensajería autorizada sin desidentificar primero;
- conservar staging, cuarentena, snapshots, salidas diagnósticas y bases
  persistentes mientras aporten al trabajo;
- usar la protección del host o volumen como control de reposo, sin exigir
  cifrado adicional por archivo;
- concentrar iniciación, ejecución, aprobación y revisión en el mismo
  operador; la segregación de funciones no es requisito local;
- transferir el mínimo pertinente a los proveedores ya configurados de
  inferencia, embeddings, web o conectores como parte del flujo privado;
- usar datos reales en pruebas locales deliberadas. Los fixtures versionados
  y la evidencia publicable siguen siendo sintéticos.

La minimización, desidentificación, destrucción temprana, cifrado por archivo y
doble aprobación quedan disponibles como técnicas, no como compuertas
universales del perfil.

## Límites que permanecen

1. **Secretos:** credenciales, tokens, llaves y cadenas de conexión no entran
   en Git, prompts persistidos, memoria agéntica ni logs.
2. **Frontera versionada:** repositorios Git, commits, PR, documentación
   publicable, fixtures y screenshots versionados no contienen PII/PHI. Los
   payloads viven en rutas privadas o gitignored.
3. **Fuentes:** lectura de sistemas clínicos por defecto. Una mutación,
   extracción destructiva o ampliación de alcance requiere orden explícita.
4. **Destinos:** el flujo privado y sus proveedores configurados están
   autorizados; publicar, enviar a un destinatario nuevo o abrir acceso
   externo requiere orden explícita.
5. **Calidad:** identidad, procedencia, temporalidad, idempotencia,
   reconciliación y distinción entre ausencia y no observabilidad no se
   relajan: evitan corrupción clínica, no son fricción de privacidad.
6. **Autoridad clínica:** el agente prepara, propone y documenta; la decisión
   clínica final y los actos institucionales permanecen en humanos competentes.
7. **Producción:** `DEV_PERSONAL_FULL` nunca se infiere desde el hostname ni se
   convierte en default de un despliegue institucional. La activación técnica
   debe ser explícita y observable.

## Matriz de realización

| Superficie | Realización del perfil |
|---|---|
| KORA | Esta URN es la fuente doctrinal; agentes y skills consumidores la resuelven antes de imponer una compuerta de privacidad. |
| OpenClaw | Workspaces privados pueden conservar PII/PHI; `BOOT.md` declara el perfil y la configuración efectiva conserva capacidades por rol. |
| `/home/felix/projects` | El contrato del workspace activa el perfil; cada repo mantiene payloads en rutas privadas o gitignored. |
| `hd-dt` | Fuentes A–D pueden inspeccionarse en crudo para gobernanza y migración; sólo la síntesis no identificable entra al árbol Git. |
| `hsc-agent-cli` | La salida clínica y la caché privada pueden conservar PII/PHI; identidad y adquisición permanecen fail-closed. |
| `hd-hsc-os` | Los carriles locales de extracción, staging, cuarentena, conciliación y base de desarrollo pueden usar datos reales; prerelease público y producción conservan sus perfiles propios. |

## Cambio de perfil

Antes de compartir un artefacto, desplegar fuera del host o incorporar otro
usuario, clasificar destino y audiencia. La transición a
`INSTITUTIONAL_CONTROLLED` exige retirar payloads identificables de superficies
versionadas o compartidas y reactivar los controles proporcionales del
entorno; no se presume equivalencia entre ambos perfiles.
