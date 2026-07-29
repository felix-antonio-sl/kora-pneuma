# Handoff vigente — 2026-07-29 — perfil clínico personal

> Memoria operativa auxiliar. No legisla ni sustituye `ALMA.md`, `ley/`, los
> artefactos canónicos, Git, los sistemas clínicos ni el estado vivo del host.

## Objetivo vigente

`urgenciologo` y `medico-hospitalista` operan como agentes de uso personal en
un servidor controlado, mono usuario. Por decisión explícita del operador:

- pueden procesar, persistir, recuperar y transferir PII/PHI cuando sea
  pertinente al encargo;
- la desidentificación y `/new` no son requisitos previos;
- pueden usar autónomamente archivos, ejecución, web, memoria, mensajería,
  sesiones y subagentes disponibles;
- la memoria y el historial aportan continuidad, pero los hechos que sostienen
  decisiones clínicas se revalidan en HSC.

Persisten cuatro límites: no conservar credenciales o secretos; no publicar
fuera del flujo privado autorizado; no mutar HSC mediante `hsc-agent-cli`; y
mantener confirmación explícita para operaciones destructivas o de
control-plane.

## Fuente y versiones

```text
urn:salud:artefacto:urgenciologo
  artefactos/agentes/salud/urgenciologo.md
  versión 3.13.0

urn:salud:artefacto:medico-hospitalista
  artefactos/agentes/salud/medico-hospitalista.md
  versión 1.10.0
```

Ambos declaran `targets: [claude-code, codex, opencode, openclaw]` y alcance
`usuario`. Las cuatro emisiones y las cuatro instalaciones de cada agente
quedaron materialmente fieles.

## Runtime OpenClaw

La configuración efectiva de ambos agentes usa:

```text
tools.profile       full
tools.exec.mode     full
exec security       full
exec ask            off
exec askFallback    full
```

Se conserva una allowlist funcional exacta orientada a adquisición de
información clínica; Gateway, nodos, cron y otras superficies de control no son
necesarias para ese propósito. Los workspaces materializados incorporan el
perfil nuevo en `AGENTS.md`, `BOOT.md` y `TOOLS.md`. Sus memorias privadas
permiten PII/PHI y continuidad, sin indexación masiva de transcripciones.

El host es mono usuario, pero inferencia, embeddings, web y otros proveedores
configurados pueden ser servicios externos. La decisión del operador autoriza
el tránsito necesario de PII/PHI por esas superficies; esta entrega no prueba
por sí sola sus condiciones contractuales, regulatorias ni de retención.

## Evidencia

```text
pruebas focales KORA             19/19
suite KORA                       306/306
velar --estricto                 13/13
paridad por agente               5/5 fiel; 0 desviadas
materialización OpenClaw         check fiel en ambos workspaces
configuración OpenClaw           válida y recargada
política exec efectiva           full/full/off/full en ambos
canarios runtime                 2/2; una ejecución directa exitosa por agente
memoria focal                    indexada y consultable en ambos
```

La verificación viva integral del fleet conserva incidencias ajenas a este
cambio: cola histórica `outbound/failed`, estados de memoria de otros agentes,
ausencia de una observación Active Memory en 24 horas y drift de documentación
upstream. No invalidan los checks focales anteriores y no fueron corregidas en
este incremento.

## Próxima acción

Usar ambos agentes en un turno clínico real supervisado y revisar que:

1. seleccionen inequívocamente paciente y episodio;
2. obtengan la información necesaria sin bloqueos heredados de privacidad;
3. revaliden en HSC los hechos decisivos;
4. no expongan credenciales ni publiquen fuera del flujo autorizado.

El handoff anterior quedó archivado en
`_archivo/HANDOFF-2026-07-28-reporte-diario-hodom-manual.md`.
