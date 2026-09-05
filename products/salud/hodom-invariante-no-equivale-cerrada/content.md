---
urn: urn:salud:kb:hodom-invariante-no-equivale-cerrada
nombre: hodom-invariante-no-equivale-cerrada
version: 1.0.0
estado: publicado
descripcion: "Invariante de dominio HODOM: la hospitalizacion domiciliaria no equivale a la cerrada; la diferencia esencial es la capacidad de vigilancia/rescate y su latencia, lo que restringe su dominio a pacientes seleccionados por bajo riesgo, con reversibilidad obligatoria."
fuente: "Establecido por la Direccion Tecnica de HODOM-HSC (Felix), destilado con mente-omega, anclado en la normativa HODOM (DS 1/2022). Registro de origen: hodom-opm/docs/hechos-establecidos.md HE-13, 2026-06-19. Fuente humana del operador, sin sha256. Perfil fuente-ya-densa: enunciado conceptual breve, CR aproximado 1.0, sin grasa; FS=100%."
autor: FS
creado: 2026-06-19
lang: es
tags: [hodom, hospitalizacion-domiciliaria, invariante, capacidad-de-rescate, seleccion-de-pacientes, reversibilidad]
cita: [urn:salud:kb:hodom-reglamento-ds1-2022, urn:salud:kb:hodom-norma-tecnica-2024]
familia: nota
---

# Invariante — HODOM no equivale a hospitalización cerrada

Invariante de dominio que gobierna propósito, frontera y seguridad de la
hospitalización domiciliaria. La hospitalización en cama básica intrahospital (A)
**no es equivalente** a la hospitalización domiciliaria (B).

## La diferencia esencial

No es el lugar. Es la **capacidad de detección y respuesta ante el empeoramiento**
—intensidad de vigilancia/monitoreo más acceso a prestaciones complejas (estudios
y tratamientos de menor disponibilidad)— y su **latencia**.

| Modalidad | Capacidad de rescate | Latencia |
|---|---|---|
| Cama cerrada (A) | alta: monitoreo continuo + arsenal complejo inmediato | baja |
| Domicilio / HODOM (B) | menor: vigilancia menos intensa, complejidad más lejana | mayor |

## Consecuencia: dominio restringido

HODOM no es sustituible universalmente: **B ⊂ A**, no B = A. Su dominio válido se
restringe a pacientes seleccionados por **baja probabilidad de empeorar mientras se
tratan**, cuyos requerimientos de vigilancia y de complejidad la menor capacidad
domiciliaria basta para cubrir. La «equivalencia» normativa (DS 1/2022, «equivalente
en calidad y cantidad») es equivalencia de **adecuación para el paciente seleccionado**,
no paridad de capacidad.

Reductio: si A = B, se hospitalizaría en domicilio a todo paciente con requerimiento
de cama básica. No es posible, porque el domicilio no rescata tan rápido ni tan completo.

## Dos compensaciones obligatorias

La menor capacidad de rescate exige dos compuertas de seguridad, no opcionales:

1. **Selección de ingreso** (front gate): bajo riesgo de empeorar más requerimientos
   cubribles por la capacidad domiciliaria. Es el criterio de la indicación/elegibilidad.
2. **Reversibilidad / escalamiento** (back gate): re-internación cuando el riesgo se
   materializa. La reversión es parte constitutiva del modelo, no una falla.

Corolario para el modelado: la provisión de cuidado se nombra «de nivel/régimen
hospitalario», no «de intensidad hospitalaria» —la intensidad de vigilancia/rescate
es menor; lo que se preserva es el régimen (responsabilidad clínica continua), con la
selección por bajo riesgo como precondición.
