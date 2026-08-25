---
urn: urn:salud:kb:hsc-pro-043-ingreso-de-usuarios
nombre: hsc-pro-043-ingreso-de-usuarios
version: 1.0.1
estado: publicado
descripcion: "Protocolo local HSC PRO-043, Ingreso de Usuarios/as (tercera edición agosto 2019): proceso institucional de ingreso a atención cerrada y ambulatoria — vías de ingreso (CAE, gestión quirúrgica, teleprocesos, urgencia, re-hospitalización), orden de hospitalización escrita, asignación de camas UGCC hábil/enfermería fuera de hora, registro DGU y egreso con epicrisis y devolución de ficha en 72 horas."
fuente: "PDF primario Drive institucional HSC, Drive ID 1H5J0AWoiFqiiVJfheStE1NRNVnpkOTNP (sha256:b5fc4f3bfb76929059ee9dfdac2c8ed3d4ec82e99a18000d09f7177fb361a020), 38 páginas; capa textual nativa, koraficación íntegra de las secciones normativas 1-9; anexos formulario descritos estructuralmente; oficialidad y vigencia por regla D-025BN"
autor: FS
creado: 2026-08-23
lang: es
tags: [hospital-san-carlos, hodom, pro-043, daiu, dgu, ingreso-hospitalario, admision, ugcc, protocolo-local]
familia: fuente
---

# PRO-043: Ingreso de Usuarios/as — Hospital de San Carlos

## Identidad documental y cautelas

Documento **PRO-043**, tercera edición, agosto de 2019, vigencia impresa
declarada hasta agosto de 2023. Encargados del cumplimiento: Subdirector Médico
y Subdirección de Gestión del Cuidado. Por D-025BN la copia del Drive
institucional es oficial y vigente mientras no exista actualización, sucesor o
retiro identificado. Describe la norma; no menciona hospitalización domiciliaria.

## Objeto, alcance y responsables

Establecer el proceso de ingreso de usuarios a prestaciones de **atención
cerrada y ambulatoria**. Alcance: todo personal que intervenga ingresos para CAE,
hospitalización en servicios clínicos o pabellón. Vías de ingreso por Admisión:
CAE, Gestión Quirúrgica, Teleprocesos, Recaudación (previa indicación médica),
re-hospitalizaciones, ingreso electivo ambulatorio (DGU) y Urgencia (consulta
espontánea adulto/pediátrica/ginecológica, derivación o rescate).

Responsables clave:

| Actividad | Responsable |
|---|---|
| Orden de hospitalización | Médico especialista CAE; cirujano electivo; tratante que re-hospitaliza; médico de turno UE adulto/pediátrica; urgencia maternal-ginecológica; médico de teleproceso (telecardiología/teletraumatología) |
| Registro de ingreso | DIG, Encargada de Hospitalizaciones DGU, servicios de Emergencias |
| Asignación de camas hábil (lun–jue 08:00–17:00, vie hasta 16:00) | Enfermera Gestora de Camas — UGCC |
| Asignación de camas no hábil | Enfermera Jefa de turno de Servicio Clínico o Emergencia según designación SDGC |
| Traslados intra/extra servicios | Indica médico tratante; ejecuta enfermera clínica; coordina gestora de camas |
| Egreso | Epicrisis por médico tratante |

## Desarrollo

### Orden de hospitalización
Escrita en todos los casos: CAE en ficha clínica; cirugía programada por médico
coordinador; urgencia y urgencia maternal en **hoja DAU** (anexo N°1).

### Ingresos
Flujo detallado por vía: CAE (citación timbrada en recaudación, TENS verifica y
registra signos vitales/antropometría), urgencia (registro DAU y comunicación a
DGU con recepción de correo hasta 16:30 lun–jue y 15:30 viernes), maternidad y
teleprocesos. Cada hospitalización hábil queda en Libro de Hospitalizaciones y
planillas Excel internas del DGU; las inhábiles en libro de emergencia.

### Egreso (alta)
Alta registrada en ficha → **epicrisis** (anexo N°13) con indicaciones → ficha a
Recaudación de Atención Cerrada (24/7) → Estadística DIG → devolución al Archivo
por DGU dentro de **72 horas** del alta, con registro de entrega/recepción de la
ficha única (anexo N°14). La devolución de la ficha se hace inmediatamente tras
entregar el alta al usuario/familiar.

## Relevancia HODOM-HSC

Describe ingreso y cierre intramural HSC. Es un contraste útil para diseñar la
interfaz HODOM, pero no menciona la unidad, no demuestra que sus anexos sean los
formatos usados por ella y no fija cama virtual, aceptación ni cambio de
responsabilidad. UGCC, Estadística/Archivo, Calidad y HODOM deben validar qué
pasos y registros se reutilizan antes de incorporarlos al protocolo de ingreso
o egreso domiciliario.

## Fuentes relacionadas

- `urn:salud:kb:hsc-normativa-hodom-indice` — índice del corpus local.
- `urn:salud:kb:hsc-pro-053-hospitalizacion-desde-unidad-emergencia` — compuerta UE→cama.
- `urn:salud:kb:hsc-mo-ugdp-mov-002-organizacion-copia-observada` — gestión centralizada de camas.
- `urn:salud:kb:hodom-reglamento-ds1-2022` — canon nacional de ingresos/egresos.
