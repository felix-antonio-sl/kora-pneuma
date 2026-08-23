# -*- coding: utf-8 -*-
"""Contrato ejecutable de la auditoría de URNs expuestos por un índice."""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
SCRIPT = (REPO / "artefactos/skills/kora/auditoria-exposicion-kora/"
          "scripts/verify-index-urns.py")


def documento(urn, nombre, *, estado="publicado", cita=None, cuerpo="Cuerpo\n"):
    cita_linea = f"cita: [{', '.join(cita)}]\n" if cita else ""
    return (
        "---\n"
        f"urn: {urn}\n"
        f"nombre: {nombre}\n"
        "version: 1.0.0\n"
        f"estado: {estado}\n"
        f"descripcion: {nombre}\n"
        "fuente: fixture controlada\n"
        f"{cita_linea}"
        "---\n\n"
        f"{cuerpo}"
    )


class TestAuditoriaExposicionKora(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)
        shutil.copy2(REPO / "kora.py", self.raiz / "kora.py")
        self._escribir(
            "artefactos/conocimiento/test/alpha-one.md",
            documento("urn:test:kb:alpha-one", "alpha-one"))
        self._escribir(
            "artefactos/conocimiento/test/alpha-two.md",
            documento("urn:test:kb:alpha-two", "alpha-two"))
        self._escribir(
            "artefactos/conocimiento/test/alpha-old.md",
            documento("urn:test:kb:alpha-old", "alpha-old",
                      estado="deprecado"))

    def tearDown(self):
        self._tmp.cleanup()

    def _escribir(self, rel, contenido):
        path = self.raiz / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(contenido, encoding="utf-8")
        return path

    def _correr(self, indice, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(indice),
             "--root", str(self.raiz), *args],
            capture_output=True, text=True, check=False,
        )

    def test_urn_rota_falla_y_duplicado_del_cuerpo_sigue_informativo(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cuerpo=(
                    "`urn:test:kb:alpha-one`\n"
                    "`urn:test:kb:alpha-one`\n"
                    "`urn:test:kb:no-existe`\n")))

        resultado = self._correr(indice)

        self.assertEqual(resultado.returncode, 1, resultado.stdout)
        self.assertIn(
            "RESOLUCION FAIL citadas=2 no_resuelven=1 "
            "ambiguas=0 invalidas=0", resultado.stdout)
        self.assertIn("NO_RESUELVE urn:test:kb:no-existe", resultado.stdout)
        self.assertIn("DUPLICADOS INFO cuerpo=1", resultado.stdout)
        self.assertIn("DUPLICADA urn:test:kb:alpha-one x2", resultado.stdout)

    def test_cobertura_mira_el_cuerpo_y_omision_no_falla_sin_claim_exhaustivo(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cita=["urn:test:kb:alpha-two"],
                cuerpo="`urn:test:kb:alpha-one`\n"))

        resultado = self._correr(
            indice, "--prefix", "urn:test:kb:alpha-")

        self.assertEqual(resultado.returncode, 0, resultado.stdout)
        self.assertIn("RESOLUCION PASS", resultado.stdout)
        self.assertIn(
            "COBERTURA_TEXTUAL GAP prefijo=urn:test:kb:alpha- "
            "publicadas=2 expuestas=1 omitidas=1",
            resultado.stdout)
        self.assertIn("OMISION urn:test:kb:alpha-two", resultado.stdout)
        self.assertIn(
            "SOLO_FRONTMATTER urn:test:kb:alpha-two", resultado.stdout)
        self.assertNotIn("alpha-old", resultado.stdout)

    def test_claim_exhaustivo_convierte_la_misma_omision_en_fallo(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cuerpo="`urn:test:kb:alpha-one`\n"))

        resultado = self._correr(
            indice, "--prefix", "urn:test:kb:alpha-",
            "--require-complete")

        self.assertEqual(resultado.returncode, 1, resultado.stdout)
        self.assertIn(
            "COBERTURA_TEXTUAL FAIL prefijo=urn:test:kb:alpha-",
            resultado.stdout)
        self.assertIn("OMISION urn:test:kb:alpha-two", resultado.stdout)

    def test_prefijo_sin_corpus_publicado_no_pasa_como_cobertura_vacia(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento("urn:test:kb:indice", "indice"))

        resultado = self._correr(
            indice, "--prefix", "urn:test:kb:familia-inexistente-")

        self.assertEqual(resultado.returncode, 1, resultado.stdout)
        self.assertIn(
            "COBERTURA_TEXTUAL ABSENT "
            "prefijo=urn:test:kb:familia-inexistente- publicadas=0",
            resultado.stdout)

    def test_urn_duplicada_en_censo_es_ambigua_y_no_resolucion_exitosa(self):
        self._escribir(
            "artefactos/conocimiento/test/alpha-one-duplicada.md",
            documento("urn:test:kb:alpha-one", "alpha-one-duplicada"))
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cuerpo="`urn:test:kb:alpha-one`\n"))

        resultado = self._correr(indice)

        self.assertEqual(resultado.returncode, 1, resultado.stdout)
        self.assertIn(
            "RESOLUCION FAIL citadas=1 no_resuelven=0 "
            "ambiguas=1 invalidas=0", resultado.stdout)
        self.assertIn("AMBIGUA urn:test:kb:alpha-one x2", resultado.stdout)

    def test_urn_malformada_no_se_trunca_hasta_otra_urn_valida(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cuerpo="`urn:test:kb:alpha-one_invalida`\n"))

        resultado = self._correr(indice)

        self.assertEqual(resultado.returncode, 1, resultado.stdout)
        self.assertIn(
            "RESOLUCION FAIL citadas=0 no_resuelven=0 "
            "ambiguas=0 invalidas=1", resultado.stdout)
        self.assertIn(
            "URN_INVALIDA urn:test:kb:alpha-one_invalida", resultado.stdout)

    def test_urn_no_kb_queda_fuera_del_subdominio_auditado(self):
        indice = self._escribir(
            "artefactos/conocimiento/test/indice.md",
            documento(
                "urn:test:kb:indice", "indice",
                cita=["urn:test:artefacto:otra-cosa"]))

        resultado = self._correr(indice)

        self.assertEqual(resultado.returncode, 0, resultado.stdout)
        self.assertIn(
            "RESOLUCION PASS citadas=0 no_resuelven=0 "
            "ambiguas=0 invalidas=0", resultado.stdout)
        self.assertNotIn("URN_INVALIDA", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
