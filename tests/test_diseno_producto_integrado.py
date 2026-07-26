# -*- coding: utf-8 -*-
"""Contrato de la triada KORA para direccion integrada de producto UI/UX."""
import subprocess
import sys
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
CANON = (
    RAIZ
    / "artefactos/conocimiento/dev/canon-diseno-producto-integrado.md"
)
SKILL = (
    RAIZ
    / "artefactos/skills/dev/diseno-producto-integrado/SKILL.md"
)
AGENTE = (
    RAIZ
    / "artefactos/agentes/dev/director-diseno-producto.md"
)


class TestDisenoProductoIntegrado(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.canon_campos, cls.canon_cuerpo = kora.parsear_archivo(
            CANON.read_text("utf-8"))
        cls.skill_campos, cls.skill_cuerpo = kora.parsear_archivo(
            SKILL.read_text("utf-8"))
        cls.agente_campos, cls.agente_cuerpo = kora.parsear_archivo(
            AGENTE.read_text("utf-8"))

    def test_triada_tiene_formas_y_estados_correctos(self):
        self.assertEqual(
            self.canon_campos["urn"],
            "urn:dev:kb:canon-diseno-producto-integrado")
        self.assertEqual(self.canon_campos["familia"], "bok")
        self.assertEqual(self.canon_campos["estado"], "publicado")

        self.assertEqual(
            self.skill_campos["urn"],
            "urn:dev:artefacto:diseno-producto-integrado")
        self.assertEqual(self.skill_campos["version"], "1.2.0")
        self.assertEqual(self.skill_campos["forma"], "habilidad")
        self.assertEqual(self.skill_campos["arnes"], "disciplina")
        self.assertEqual(self.skill_campos["estado"], "activo")
        self.assertEqual(
            self.skill_campos["targets"],
            ["codex"])

        self.assertEqual(
            self.agente_campos["urn"],
            "urn:dev:artefacto:director-diseno-producto")
        self.assertEqual(self.agente_campos["version"], "1.2.0")
        self.assertEqual(self.agente_campos["forma"], "agente")
        self.assertEqual(self.agente_campos["arnes"], "persona")
        self.assertEqual(self.agente_campos["estado"], "activo")
        self.assertEqual(
            self.agente_campos["targets"],
            ["codex"])

    def test_canon_separa_evidencia_inferencia_y_contraprueba(self):
        cuerpo = " ".join(self.canon_cuerpo.split())
        for perfil in (
                "Alan Dye", "Tobias van Schneider", "Imran Chaudhri",
                "Karri Saarinen"):
            self.assertIn(perfil, cuerpo)
        for seccion in (
                "## Método epistémico", "#### Evidencia pública",
                "#### Inferencia operativa", "#### Límite y contraprueba",
                "## Propiedades emergentes"):
            self.assertIn(seccion, self.canon_cuerpo)
        self.assertIn("Meta Reality Labs", cuerpo)
        self.assertIn("Humane Ai Pin", cuerpo)
        self.assertIn("no es diseño", cuerpo.lower())

    def test_skill_cablea_canon_design_y_ux_sin_fingir_composicion(self):
        self.assertEqual(
            self.skill_campos["conocimiento"],
            ["urn:dev:kb:canon-diseno-producto-integrado"])
        self.assertEqual(
            self.skill_campos["componible"],
            ["urn:dev:artefacto:design", "urn:kora:artefacto:ux-design"])
        cuerpo = " ".join(self.skill_cuerpo.split())
        for testigo in (
                "`I_design`", "`O_design`", "`I_ux`", "`O_ux`",
                "candidatos declarados", "no prueba composicion",
                "`DESIGN_PACKET`", "`DESIGN_ERROR`"):
            self.assertIn(testigo, cuerpo)

    def test_skill_exige_loop_completo_y_prueba_de_realidad(self):
        cuerpo = " ".join(self.skill_cuerpo.split())
        for estado in (
                "encuadrar", "resolver-tensiones", "divergir", "decidir",
                "prototipar", "probar", "integrar", "entregar"):
            self.assertIn(estado, self.skill_campos["estados"])
        for prueba in (
                "latencia", "legibilidad", "reversibilidad", "privacidad",
                "estados vacios", "WCAG 2.2 AA", "bucle completo"):
            self.assertIn(prueba, cuerpo)

    def test_agente_es_sintesis_no_imitacion_y_tiene_u_phen(self):
        cuerpo = " ".join(self.agente_cuerpo.split())
        self.assertIn("<!-- kora:soul -->", self.agente_cuerpo)
        self.assertIn("<!-- kora:soul:fin -->", self.agente_cuerpo)
        for testigo in (
                "no imita", "Fin.", "Estilo", "Registro.",
                "Direccion (C sobre B)", "`I_self`", "`O_self`",
                "`DESIGN_PACKET`", "`DESIGN_ERROR`"):
            self.assertIn(testigo, cuerpo)
        self.assertEqual(
            self.agente_campos["componible"],
            ["urn:dev:artefacto:diseno-producto-integrado"])

    def test_agente_declara_frontera_de_autoridad_runtime(self):
        cuerpo = " ".join(self.agente_cuerpo.split()).lower()
        self.assertIn(
            "herramientas declaradas no prueban autoridad efectiva", cuerpo)
        self.assertIn("spec", cuerpo)
        self.assertIn("runtime", cuerpo)

    def test_agente_y_skill_prohiben_evidencia_fabricada(self):
        for cuerpo in (self.agente_cuerpo, self.skill_cuerpo):
            normalizado = " ".join(cuerpo.split()).lower()
            self.assertIn("fuente observable de esta ejecución", normalizado)
            self.assertIn("no invent", normalizado)
            self.assertIn("métricas", normalizado)
            self.assertIn("tests", normalizado)
            self.assertIn("owners", normalizado)
            self.assertIn("sin artefacto ejecutable", normalizado)
            self.assertIn("`inferido` o `pendiente`", normalizado)
            self.assertIn("`evidence_ledger`", normalizado)
            self.assertIn("[e#]", normalizado)
            self.assertIn("no puede verificarse a sí mism", normalizado)
            self.assertIn("independiente de", normalizado)
            self.assertIn("`spec_only`", normalizado)
            self.assertIn("`propuesto`", normalizado)
            self.assertIn("normativo", normalizado)
            self.assertIn("ausentes de la entrada", normalizado)

    def test_no_reintroduce_ancla_obsoleta_de_encapsulacion(self):
        fuentes = "\n".join((
            self.canon_cuerpo, self.skill_cuerpo, self.agente_cuerpo))
        self.assertNotIn("cat-agent-modulo §5", fuentes)
        self.assertNotIn("vector = tipo", fuentes)

    def test_target_operativo_queda_concentrado_en_codex(self):
        for campos in (self.skill_campos, self.agente_campos):
            self.assertEqual(campos["targets"], ["codex"])
            fuente = campos["fuente"].lower()
            self.assertIn("retira opencode", fuente)
            self.assertIn("retira claude code", fuente)
            self.assertIn("alcance explicito", fuente)
            self.assertIn("canario conductual verde", fuente)

    def test_las_emisiones_codex_son_materializables(self):
        urns = (
            "urn:dev:artefacto:diseno-producto-integrado",
            "urn:dev:artefacto:director-diseno-producto",
        )
        targets = ("codex",)
        emisiones = {}

        for urn in urns:
            for target in targets:
                with self.subTest(urn=urn, target=target):
                    resultado = subprocess.run(
                        [
                            sys.executable,
                            str(RAIZ / "kora.py"),
                            "transmutar",
                            "--urn", urn,
                            "--target", target,
                            "--stdout",
                        ],
                        cwd=RAIZ,
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                    self.assertEqual(
                        resultado.returncode, 0, resultado.stderr)
                    self.assertIn(f"target: {target}", resultado.stdout)
                    emisiones[(urn, target)] = resultado.stdout

        agente_codex = emisiones[(urns[1], "codex")]
        self.assertIn(
            "codex/agents/director-diseno-producto.toml",
            agente_codex)
        self.assertIn(
            "codex/skills/director-diseno-producto/SKILL.md",
            agente_codex)


if __name__ == "__main__":
    unittest.main()
