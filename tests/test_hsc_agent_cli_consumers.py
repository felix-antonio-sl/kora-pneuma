# -*- coding: utf-8 -*-
"""Fuentes clínicas KORA libres de identificadores concretos."""
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
FUENTES = (
    RAIZ / "artefactos/agentes/salud/medico-hospitalista.md",
    RAIZ / "artefactos/agentes/salud/urgenciologo.md",
    RAIZ / "artefactos/conocimiento/salud/manual-agente-hsc-agent-cli.md",
    RAIZ / "artefactos/conocimiento/salud/perfil-dev-personal-full.md",
    RAIZ / "artefactos/skills/salud/reporte-diario-hodom/SKILL.md",
    RAIZ / (
        "artefactos/skills/salud/reporte-diario-hodom/"
        "referencias/playbook-hsc-agent-cli.md"
    ),
)


class TestFuentesClinicasSinIdentificadores(unittest.TestCase):

    def test_fuentes_y_tests_no_contienen_identificadores_concretos(self):
        patrones = (
            r"\b(?:(?:\d{1,2}\.)?\d{3}\.\d{3}|\d{7,8})-[\dkK]\b",
            r"\bhospitalizacion:sgh:\d",
            r"\burgencia:dau:\d",
            r"\bpaciente:(?:identidad:|timeline/|lis/)\d",
            r'--nombre\s+["“](?!<)',
        )
        for path in (*FUENTES, Path(__file__)):
            contenido = path.read_text(encoding="utf-8")
            for patron in patrones:
                self.assertNotRegex(contenido, patron, str(path))


if __name__ == "__main__":
    unittest.main()
