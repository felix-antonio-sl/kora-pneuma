---
urn: urn:gn:kb:ssot-legal
nombre: ssot-legal
version: 1.1.0
estado: borrador
descripcion: "Documento SSOT GORE Ñuble migrado como conocimiento borrador; su estado no implica validación institucional."
fuente: "Fuente externa archivada en /home/felix/kora-external-sources/_archivo/2026-08-02-gn-ssot/ssot-legal.md (sha256:8a809b8d016caad4965e5f87b58861cba5b93935c2cd4fd922bf3ae6baa58546); cuerpo preservado íntegramente durante la migración KORA del 2026-08-02."
autor: FS
creado: 2026-03-10
lang: es
tags: [ssot, legal, normativo, glosas, loc-gore, presupuestos]
familia: bok
---

# SSOT — Marco normativo GORE Ñuble

## Resumen

3 cuerpos legales, 8 artículos modelados, 6 mandatos, 10 glosas presupuestarias. Marco normativo que rige la gestión del GORE, con énfasis en LOC GORE y Ley de Presupuestos 2026 Partida 31.

## Cuerpos legales

| Documento | Descripción | URI ontología |
|-----------|-------------|---------------|
| LOC GORE (DFL 1-19.175) | Ley Orgánica Constitucional de Gobiernos Regionales, texto refundido | `_LegalDoc_LOC_GORE` |
| Ley 21.033 | Creación de la Región de Ñuble | `_LegalDoc_Ley21033` |
| Ley de Presupuestos 2026 | Partida 31 GORE — presupuesto sector público 2026 | `_LegalDoc_LeyPresupuestos2026` |

## Artículos modelados

| Artículo | Cuerpo legal | Materia |
|----------|-------------|---------|
| Art. 2 | LOC GORE | Atribuciones del Delegado Presidencial Regional |
| Art. 16 | LOC GORE | Funciones generales del Gobierno Regional |
| Art. 17 | LOC GORE | Funciones de ordenamiento territorial |
| Art. 18 | LOC GORE | Funciones de fomento productivo |
| Art. 19 | LOC GORE | Funciones de desarrollo social y cultural |
| Art. 20 | LOC GORE | Atribuciones generales del Gobierno Regional |
| Art. 21 bis | LOC GORE | Transferencia de competencias desde nivel central |
| Art. 6 | Ley Presupuestos 2026 | Umbrales para licitación pública |

## Mandatos legales

| Mandato | Deriva de | Obliga a |
|---------|-----------|----------|
| Aprobar Presupuesto Regional | Art. 16 LOC | GORE Ñuble |
| Aprobar PROT | Art. 17 LOC | GORE Ñuble |
| Fomentar Turismo Regional | Art. 18 LOC | GORE Ñuble |
| Coordinar Seguridad Pública | Art. 2 LOC | DPR Ñuble |
| Licitación pública proyectos > 1.000 UTM | Art. 6 Ley 2026 | GORE Ñuble |
| Licitación pública estudios > 500 UTM | Art. 6 Ley 2026 | GORE Ñuble |

## Glosas presupuestarias (Ley Presupuestos 2026, Partida 31)

| Glosa | Asunto | Gastos personal | Restricciones clave |
|-------|--------|-----------------|---------------------|
| 01 | Marco general FNDR / Funcionamiento | — | LegalData: reglas asignación FNDR. IPRData: reglas funcionamiento regional (S21). Definiciones incompatibles entre fuentes — requiere reconciliación en ontología |
| 03 | Prohibiciones inversión | Prohibido | NO préstamos, NO gastos personal/bienes consumo receptores, NO aportes sociedades |
| 04 | Traspaso de recursos | — | Permite traspasos entre subtítulos de inversión (excepto hacia S22) |
| 06 | Programas públicos regionales (S24) | Permitido | Evaluación ex-ante DIPRES/SES. Admin GORE max 5%, honorarios receptor max 5% |
| 07 | Subvenciones 8% FNDR | — | Concurso público. Asignaciones directas ≤10% (Res. 72/2025 DIPRES). Inhabilita si rendiciones pendientes |
| 10 | Aumentos inversión S31 | — | ≤10% costo aprobado NO requiere nueva aprobación CORE |
| 11 | Aumentos transferencias S33 | — | ≤10% costo aprobado NO requiere nueva aprobación CORE |
| 12 | FRIL | Prohibido | Transferencias a municipalidades. Exención RS < 4.545 UTM (Ñuble; nacional 5.000 UTM). Solo obras |
| 13 | FRPD (Royalty Minero) | — | I+D+i, instituciones habilitadas |
| 14 | Emergencias | — | 3% traspasable a Subsec. Interior + 2% uso interno GORE |

[impl: GORE_OS implementa 7/7 glosas. `check_glosa_rules()` en `ipr.py`. `_check_glosa03_prohibition()` bloquea FNDR→PERSONAL. `check_glosa07_transfer_limits()` en `presupuesto.py`. CLAUDE.md §Rules 36-38]

## Tipos de glosa

| Tipo | Descripción |
|------|-------------|
| Numérica | Limita montos/cantidades |
| Textual | Condiciones, prohibiciones, mandatos |
| Mixta | Límites numéricos + condiciones textuales |
| Estructural | Define estructura/desagregación |

## Regla cofinanciamiento C33

Circular 33: exige 20% aporte propio en Activos No Financieros. `requiresCoFinancing = true`.

[impl: `_check_c33_conservation()` gate F1→F2, informational. CLAUDE.md §Rule 38]

## Jerarquía presupuestaria

[ver clasificador completo](urn:gn:kb:ssot-presupuesto)
