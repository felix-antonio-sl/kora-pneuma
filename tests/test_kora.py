# -*- coding: utf-8 -*-
"""Tests del núcleo kora.py — corpus sintéticos en tempdir (contrato §7)."""
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import kora  # noqa: E402


def linea(clave, valor):
    if isinstance(valor, list):
        return f"{clave}: [" + ", ".join(str(x) for x in valor) + "]"
    return f"{clave}: {valor}"


def doc(campos, cuerpo="# Cuerpo\n\nTexto sintético.\n"):
    fm = "\n".join(linea(k, v) for k, v in campos.items())
    return f"---\n{fm}\n---\n\n{cuerpo}"


def skill_campos(**over):
    base = dict(
        urn="urn:kora:artefacto:util-x", nombre="util-x", version="1.0.0",
        estado="activo", descripcion="Skill sintética de prueba.",
        fuente="corpus sintético de test", vector=[1, 0, 1, 0, 1],
        sigma=[1, 1, 1, 1, 1], arnes="utilidad", forma="habilidad",
        herramientas=["Read"], targets=["claude-code"])
    base.update(over)
    return base


def agente_campos(**over):
    base = dict(
        urn="urn:dev:artefacto:agente-x", nombre="agente-x", version="1.0.0",
        estado="activo", descripcion="Agente sintético de prueba.",
        fuente="corpus sintético de test", vector=[2, 2, 2, 0, 2],
        sigma=[2, 1, 2, 1, 1], arnes="persona", forma="agente",
        herramientas=["Read", "Write"], targets=["claude-code", "opencode"])
    base.update(over)
    return base


def conocimiento_campos(**over):
    base = dict(
        urn="urn:kora:kb:nota-x", nombre="nota-x", version="1.0.0",
        estado="publicado", descripcion="Nota sintética de prueba.",
        fuente="corpus sintético de test", familia="nota",
        tags=["uno", "dos", "tres"])
    base.update(over)
    return base


class CasoPneuma(unittest.TestCase):
    """Base: corpus sintético en tempdir, KORA_RAIZ inyectada."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)
        os.environ["KORA_RAIZ"] = str(self.raiz)

    def tearDown(self):
        os.environ.pop("KORA_RAIZ", None)
        self._tmp.cleanup()

    def escribir(self, rel, texto):
        path = self.raiz / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(texto, encoding="utf-8")
        return path

    def escribir_skill(self, campos=None, ns="kora", cuerpo=None):
        campos = campos or skill_campos()
        texto = doc(campos) if cuerpo is None else doc(campos, cuerpo)
        return self.escribir(
            f"artefactos/skills/{ns}/{campos['nombre']}/SKILL.md", texto)

    def escribir_agente(self, campos=None, ns="dev"):
        campos = campos or agente_campos()
        return self.escribir(
            f"artefactos/agentes/{ns}/{campos['nombre']}.md", doc(campos))

    def escribir_conocimiento(self, campos=None, ns="kora"):
        campos = campos or conocimiento_campos()
        return self.escribir(
            f"artefactos/conocimiento/{ns}/{campos['nombre']}.md", doc(campos))

    def fallos(self, check, estricto=False):
        res = kora.velar_todo(self.raiz, estricto)
        return [f"{p} :: {m}" for p, m in res[check]]

    def assert_fallo(self, check, fragmento, estricto=False):
        mensajes = self.fallos(check, estricto)
        self.assertTrue(
            any(fragmento in m for m in mensajes),
            f"{check}: esperaba fallo con '{fragmento}'; hubo: {mensajes}")

    def assert_todo_coherente(self, estricto=True):
        res = kora.velar_todo(self.raiz, estricto)
        planos = [f"[{c}] {p} :: {m}"
                  for c, fs in res.items() for p, m in fs]
        self.assertEqual(planos, [], f"corpus debía ser coherente: {planos}")

    def correr(self, argv):
        """Ejecuta la CLI en proceso; devuelve (exit, stdout, stderr)."""
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            codigo = kora.principal(argv)
        return codigo, out.getvalue(), err.getvalue()


# ------------------------------------------------------------- 1. parser

class TestParser(unittest.TestCase):

    def test_frontmatter_valido_completo(self):
        texto = (
            "---\n"
            "# comentario en línea propia\n"
            "urn: urn:kora:artefacto:util-x\n"
            "nombre: util-x\n"
            "version: 1.0.0  # semver al final\n"
            'descripcion: "con # adentro y, comas"\n'
            "creado: 2026-06-11\n"
            "vector: [1, 0, 1, 0, 1]\n"
            "\n"
            "tags: [a, \"b, c\", d]\n"
            "---\n"
            "\nCuerpo.\n")
        campos, cuerpo = kora.parsear_archivo(texto)
        self.assertEqual(campos["version"], "1.0.0")
        self.assertEqual(campos["descripcion"], "con # adentro y, comas")
        self.assertEqual(campos["creado"], "2026-06-11")
        self.assertEqual(campos["vector"], [1, 0, 1, 0, 1])
        self.assertEqual(campos["tags"], ["a", "b, c", "d"])
        self.assertIn("Cuerpo.", cuerpo)

    def test_lista_inline_vacia(self):
        campos, _ = kora.parsear_archivo("---\nherramientas: []\n---\n")
        self.assertEqual(campos["herramientas"], [])

    def test_clave_duplicada_es_error(self):
        with self.assertRaises(kora.ErrorDeForma) as ctx:
            kora.parsear_archivo("---\nnombre: a\nnombre: b\n---\n")
        self.assertIn("duplicada", str(ctx.exception))
        self.assertEqual(ctx.exception.linea, 3)

    def test_anidamiento_es_error(self):
        with self.assertRaises(kora.ErrorDeForma) as ctx:
            kora.parsear_archivo("---\nplan:\n  paso: uno\n---\n")
        self.assertIn("anidad", str(ctx.exception))
        with self.assertRaises(kora.ErrorDeForma):
            kora.parsear_archivo("---\nnombre: a\n  indentada: x\n---\n")
        with self.assertRaises(kora.ErrorDeForma):
            kora.parsear_archivo("---\nmapa: {a: 1}\n---\n")

    def test_multilinea_es_error(self):
        with self.assertRaises(kora.ErrorDeForma) as ctx:
            kora.parsear_archivo("---\ndescripcion: |\n  texto\n---\n")
        self.assertIn("multilínea", str(ctx.exception))
        self.assertEqual(ctx.exception.linea, 2)

    def test_sin_frontmatter_es_error(self):
        with self.assertRaises(kora.ErrorDeForma):
            kora.parsear_archivo("# Solo cuerpo\n")


# -------------------------------------------------- 2. derivación de tipo

class TestDerivacion(CasoPneuma):

    def test_tipos_derivados(self):
        self.escribir_skill()
        self.escribir_agente()
        self.escribir_conocimiento()
        censo = kora.construir_censo(kora.cargar_corpus(self.raiz))
        tipos = {e["urn"]: e["tipo"] for e in censo}
        self.assertEqual(tipos["urn:kora:artefacto:util-x"], "skill")
        self.assertEqual(tipos["urn:dev:artefacto:agente-x"], "agente")
        self.assertEqual(tipos["urn:kora:kb:nota-x"], "conocimiento")

    def test_vector_sin_forma_es_error(self):
        campos = skill_campos()
        del campos["forma"]
        self.escribir_skill(campos)
        self.assert_fallo("forma-valida", "'forma' es obligatorio")


# --------------------------------------------------------------- 3. URN

class TestUrn(CasoPneuma):

    def test_regex_acepta_y_rechaza(self):
        for bueno in ("urn:kora:artefacto:mente-omega",
                      "urn:fx-sl:kb:a-b-c", "urn:dev:artefacto:x9"):
            self.assertTrue(kora.RE_URN.match(bueno), bueno)
        for malo in ("urn:kora:skill:x", "urn:Kora:artefacto:x",
                     "urn:kora:artefacto:x@1.0.0",
                     "urn:kora:artefacto:x:1.0.0",
                     "urn:kora:artefacto:años", "kora:artefacto:x"):
            self.assertFalse(kora.RE_URN.match(malo), malo)

    def test_version_embebida_rechazada(self):
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:util-x@1.0.0"))
        self.assert_fallo("nombre-verdadero", "no cumple la gramática")

    def test_regimen_coincide_con_tipo(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:artefacto:nota-x"))
        self.assert_fallo("nombre-verdadero", "exige 'kb'")

    def test_unicidad_violada(self):
        self.escribir_skill()
        self.escribir_skill(skill_campos(nombre="util-y"))
        self.assert_fallo("nombre-verdadero", "URN duplicado")


# ----------------------------------------------------- 4. retículo del vector

class TestVectorEnReticulo(CasoPneuma):

    def test_cada_eje_fuera_de_rango(self):
        casos = {"pi": [4, 0, 1, 0, 1], "mu": [1, 4, 1, 0, 1],
                 "xi": [1, 0, 5, 0, 1], "lambda": [1, 0, 1, 4, 1],
                 "phi": [1, 0, 1, 0, 5]}
        for eje, vector in casos.items():
            with self.subTest(eje=eje):
                self.escribir_skill(skill_campos(vector=vector))
                valor = vector[kora.EJES.index(eje)]
                self.assert_fallo("vector-en-reticulo", f"{eje}={valor}")

    def test_sigma_fuera_de_rango(self):
        self.escribir_skill(skill_campos(sigma=[1, 4, 1, 1, 1]))
        self.assert_fallo("vector-en-reticulo", "sigma.fairness=4")


# ----------------------------------------------------- 5. leyes inter-eje

class TestLeyesInterEje(CasoPneuma):

    def test_ley_1_pi_exige_mu(self):
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado",
            vector=[3, 0, 2, 0, 1], sigma=[1, 1, 1, 1, 1]))
        self.assert_fallo("leyes-inter-eje", "ley 1")

    def test_ley_2_xi4_exige_lambda(self):
        self.escribir_agente(agente_campos(
            arnes="orquestador", vector=[2, 2, 4, 0, 2]))
        self.assert_fallo("leyes-inter-eje", "ley 2")

    def test_ley_3_phi_exige_mu(self):
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado",
            vector=[2, 0, 2, 0, 2], sigma=[1, 1, 1, 1, 1]))
        self.assert_fallo("leyes-inter-eje", "ley 3")

    def test_ley_4_accountability_exige_transparency(self):
        self.escribir_skill(skill_campos(sigma=[1, 1, 1, 2, 1]))
        self.assert_fallo("leyes-inter-eje", "ley 4")

    def test_ley_5_lambda3_exige_sigma_pleno(self):
        self.escribir_agente(agente_campos(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 3, 3, 1], sigma=[2, 2, 2, 2, 1],
            targets=["openclaw"]))
        self.assert_fallo("leyes-inter-eje", "ley 5")


# ----------------------------------------------------- 6. dominio por forma

class TestDominioForma(CasoPneuma):

    def test_habilidad_con_mu2(self):
        self.escribir_skill(skill_campos(vector=[1, 2, 1, 0, 1]))
        self.assert_fallo("dominio-forma", "'habilidad': mu=2")

    def test_plataforma_con_mu2(self):
        self.escribir_agente(agente_campos(
            forma="plataforma", arnes="servicio",
            vector=[2, 2, 3, 1, 1], sigma=[2, 1, 2, 1, 1],
            targets=["openclaw"]))
        self.assert_fallo("dominio-forma", "'plataforma': mu=2")


# ----------------------------------------------------- 7. arnés × forma

class TestArnesForma(CasoPneuma):

    def test_persona_con_habilidad(self):
        self.escribir_skill(skill_campos(arnes="persona"))
        self.assert_fallo("arnes-compatible", "incompatible")

    def test_arquetipo_nunca_se_materializa(self):
        self.escribir_agente(agente_campos(arnes="arquetipo"))
        self.assert_fallo("arnes-compatible", "arquetipo")


# ------------------------------------------------------------ 8. lifecycle

class TestCiclo(CasoPneuma):

    def test_avance_simple_y_salto(self):
        path = self.escribir_skill(skill_campos(estado="borrador"))
        original = path.read_text(encoding="utf-8")
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 0)
        nuevo = path.read_text(encoding="utf-8")
        self.assertEqual(
            original.replace("estado: borrador", "estado: activo"), nuevo,
            "solo la línea estado puede cambiar; el resto byte-idéntico")
        # salto hacia adelante: activo -> retirado es válido
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "retirado"])
        self.assertEqual(codigo, 0)
        self.assertIn("estado: retirado", path.read_text(encoding="utf-8"))

    def test_inversas_invalidas(self):
        self.escribir_skill(skill_campos(estado="deprecado"))
        codigo, _, err = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 1)
        self.assertIn("transición inválida", err)

    def test_retirado_no_se_reactiva(self):
        self.escribir_skill(skill_campos(estado="retirado"))
        for destino in ("borrador", "activo", "deprecado", "retirado"):
            codigo, _, err = self.correr(
                ["ciclo", "urn:kora:artefacto:util-x", destino])
            self.assertEqual(codigo, 1, destino)
            self.assertIn("transición inválida", err)

    def test_cadena_del_conocimiento(self):
        self.escribir_conocimiento(conocimiento_campos(estado="borrador"))
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:kb:nota-x", "publicado"])
        self.assertEqual(codigo, 0)
        # retirado no existe en la cadena del conocimiento
        codigo, _, err = self.correr(
            ["ciclo", "urn:kora:kb:nota-x", "retirado"])
        self.assertEqual(codigo, 1)
        self.assertIn("cadena del tipo", err)


# ----------------------------------------------- 9. dignidad del URN muerto

class TestDignidad(CasoPneuma):

    def test_retirado_sigue_resolviendo(self):
        self.escribir_skill(skill_campos(estado="retirado"))
        codigo, salida, _ = self.correr(
            ["nombre", "urn:kora:artefacto:util-x"])
        self.assertEqual(codigo, 0)
        self.assertIn("retirado", salida)
        self.assertIn("sigue resolviendo", salida)
        codigo, salida, _ = self.correr(["censo", "--json"])
        self.assertEqual(codigo, 0)
        self.assertIn("urn:kora:artefacto:util-x", salida)


# ------------------------------------------------------------ 10. relaciones

class TestRelaciones(CasoPneuma):

    def test_ciclo_en_depende(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:a", nombre="a", depende=["urn:kora:kb:b"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:b", nombre="b", depende=["urn:kora:kb:a"]))
        self.assert_fallo("relaciones-legales", "ciclo en 'depende'")

    def test_reemplaza_antisimetria(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:a", nombre="a", estado="deprecado",
            reemplaza=["urn:kora:kb:b"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:b", nombre="b", estado="deprecado",
            reemplaza=["urn:kora:kb:a"]))
        self.assert_fallo("relaciones-legales", "ciclo en 'reemplaza'")
        self.assert_fallo("relaciones-legales", "antisimetría")

    def test_reemplaza_target_debe_estar_muerto(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:a", nombre="a", reemplaza=["urn:kora:kb:b"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:b", nombre="b"))  # publicado: vivo
        self.assert_fallo("relaciones-legales",
                          "exige target deprecado o retirado")

    def test_cita_circular_es_legal(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:a", nombre="a", cita=["urn:kora:kb:b"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:b", nombre="b", cita=["urn:kora:kb:a"]))
        self.assert_todo_coherente()

    def test_referencia_que_no_resuelve(self):
        self.escribir_conocimiento(conocimiento_campos(
            cita=["urn:kora:kb:fantasma"]))
        self.assert_fallo("referencias-resuelven", "no resuelve")


# ---------------------------------------------------------- 11. transmutación

class TestTransmutacion(CasoPneuma):

    def test_emision_porta_sello_y_hash(self):
        fuente = self.escribir_skill()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 0)
        emitido = self.raiz / "_emision/claude-code/skills/util-x/SKILL.md"
        self.assertTrue(emitido.is_file())
        texto = emitido.read_text(encoding="utf-8")
        self.assertIn("<!-- kora:sello", texto)
        hash_real = hashlib.sha256(fuente.read_bytes()).hexdigest()
        self.assertIn(f"hash-fuente: sha256:{hash_real}", texto)
        self.assertIn("funtor: T-claude-code-pneuma-v1", texto)
        self.assertIn("allowed-tools: Read", texto)
        self.assertNotIn("perdidas:", texto)
        # con sello fresco, velar no reclama
        self.assertEqual(self.fallos("sello-fresco"), [])

    def test_perdida_declarada_cuando_partial(self):
        self.escribir_agente(agente_campos(
            vector=[2, 2, 2, 0, 3], sigma=[3, 2, 3, 3, 1]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/claude-code/agents/agente-x.md").read_text(
                     encoding="utf-8")
        self.assertIn("perdidas:", texto)
        self.assertIn("phi: 3->2 :: cognición híbrida no nativa", texto)
        self.assertIn("sigma.accountability: 3->2 ::", texto)
        self.assertIn(
            "fidelidad: pi:full mu:full xi:full lambda:full "
            "phi:partial sigma:partial", texto)
        self.assertIn("vector-fuente: [2,2,2,0,3] sigma [3,2,3,3,1]", texto)
        self.assertIn("vector-proyectado: [2,2,2,0,2] sigma [3,2,3,2,1]",
                      texto)
        # persona: doctrina dual-mode en el body
        self.assertIn("## Modos de invocacion", texto)

    def test_mu3_a_claude_code_falla(self):
        self.escribir_agente(agente_campos(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 3, 1, 1], sigma=[2, 1, 2, 1, 1],
            targets=["openclaw"]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("mu=3", err)
        self.assertIn("openclaw", err)

    def test_determinismo_byte_a_byte(self):
        self.escribir_skill()
        argv = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "codex"]
        self.assertEqual(self.correr(argv)[0], 0)
        emitido = self.raiz / "_emision/codex/skills/util-x/SKILL.md"
        primera = emitido.read_bytes()
        self.assertEqual(self.correr(argv)[0], 0)
        self.assertEqual(primera, emitido.read_bytes())

    def test_target_no_realizado_falla_honesto(self):
        self.escribir_skill()
        for target in ("openclaw", "hermes"):
            codigo, _, err = self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", target])
            self.assertEqual(codigo, 1, target)
            self.assertIn("GENESIS", err)

    def test_codex_colapsa_agente_a_skill(self):
        self.escribir_agente()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        emitido = self.raiz / "_emision/codex/skills/agente-x/SKILL.md"
        texto = emitido.read_text(encoding="utf-8")
        self.assertIn(
            "forma: agente->habilidad :: codex no registra agentes", texto)

    def test_opencode_emite_modo(self):
        self.escribir_agente()
        self.escribir_agente(agente_campos(
            urn="urn:dev:artefacto:sub-x", nombre="sub-x",
            forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 1], sigma=[1, 1, 1, 1, 1]))
        for urn, modo, nombre in (
                ("urn:dev:artefacto:agente-x", "mode: primary", "agente-x"),
                ("urn:dev:artefacto:sub-x", "mode: subagent", "sub-x")):
            codigo, _, _ = self.correr(
                ["transmutar", "--urn", urn, "--target", "opencode"])
            self.assertEqual(codigo, 0)
            texto = (self.raiz /
                     f"_emision/opencode/agents/{nombre}.md").read_text(
                         encoding="utf-8")
            self.assertIn(modo, texto)

    def test_stdout_no_escribe(self):
        self.escribir_skill()
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code", "--stdout"])
        self.assertEqual(codigo, 0)
        self.assertIn("<!-- kora:sello", salida)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_sello_rancio_detectado(self):
        fuente = self.escribir_skill()
        self.correr(["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code"])
        fuente.write_text(
            fuente.read_text(encoding="utf-8") + "\nLínea nueva.\n",
            encoding="utf-8")
        self.assert_fallo("sello-fresco", "emisión rancia, re-transmutar")

    def test_conocimiento_no_se_transmuta(self):
        self.escribir_conocimiento()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:kb:nota-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("no se transmuta", err)


# ------------------------------------------------------------- 12. censo

class TestCenso(CasoPneuma):

    def test_derivado_y_regenerable(self):
        self.escribir_skill()
        self.escribir_conocimiento()
        primera = self.correr(["censo", "--json"])[1]
        segunda = self.correr(["censo", "--json"])[1]
        self.assertEqual(primera, segunda)
        # el censo nunca contradice el filesystem: lo nuevo aparece
        self.escribir_agente()
        tercera = self.correr(["censo", "--json"])[1]
        self.assertIn("urn:dev:artefacto:agente-x", tercera)
        self.assertNotIn("urn:dev:artefacto:agente-x", primera)

    def test_escribir_censo_json(self):
        self.escribir_skill()
        codigo, _, _ = self.correr(["censo", "--escribir"])
        self.assertEqual(codigo, 0)
        contenido = (self.raiz / "censo.json").read_text(encoding="utf-8")
        self.assertEqual(contenido, self.correr(["censo", "--json"])[1])

    def test_nombre_inexistente_falla(self):
        codigo, _, err = self.correr(["nombre", "urn:kora:kb:fantasma"])
        self.assertEqual(codigo, 1)
        self.assertIn("no resuelve", err)


# ------------------------------------------- 13. velar sobre corpus válido

class TestVelarCorpusValido(CasoPneuma):

    def test_corpus_completo_coherente(self):
        self.escribir_conocimiento()
        self.escribir_agente(agente_campos(
            conocimiento=["urn:kora:kb:nota-x"]))
        self.escribir_skill(skill_campos(
            cita=["urn:kora:kb:nota-x"], depende=["urn:kora:kb:nota-x"],
            componible=["urn:dev:artefacto:agente-x"]))
        self.assert_todo_coherente(estricto=True)
        codigo, salida, _ = self.correr(["velar", "--estricto"])
        self.assertEqual(codigo, 0)
        self.assertIn("todo coherente", salida)

    def test_publicacion_digna_solo_estricto(self):
        self.escribir_conocimiento(conocimiento_campos(tags=["uno"]))
        codigo, _, _ = self.correr(["velar"])
        self.assertEqual(codigo, 0)
        self.assert_fallo("publicacion-digna", ">=3 tags", estricto=True)
        codigo, _, _ = self.correr(["velar", "--estricto"])
        self.assertEqual(codigo, 1)

    def test_ley_ausente_falla_limpio(self):
        codigo, _, err = self.correr(["ley"])
        self.assertEqual(codigo, 1)
        self.assertIn("faltan", err)


# --------------------------------- 14. revisión adversarial: fixes cerrados

class TestEmisionReferencias(CasoPneuma):
    """Fix 1: la emisión conserva el nombre referencias/ — sin enlaces rotos."""

    def test_referencias_conserva_nombre_y_enlaces(self):
        cuerpo = ("# Skill\n\nVer referencias/motor.md y "
                  "referencias/sub/extra.md para el detalle.\n")
        self.escribir_skill(cuerpo=cuerpo)
        self.escribir("artefactos/skills/kora/util-x/referencias/motor.md",
                      "# Motor\n")
        self.escribir(
            "artefactos/skills/kora/util-x/referencias/sub/extra.md",
            "# Extra\n")
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        emitido_dir = self.raiz / "_emision/codex/skills/util-x"
        self.assertTrue((emitido_dir / "referencias").is_dir(),
                        "la fibra emitida debe llamarse referencias/")
        self.assertFalse((emitido_dir / "references").exists(),
                         "no debe haber rename a references/")
        texto = (emitido_dir / "SKILL.md").read_text(encoding="utf-8")
        citados = re.findall(r"referencias/[\w./-]+", texto)
        self.assertTrue(citados, "el cuerpo emitido debe citar referencias/")
        for ref in citados:
            self.assertTrue((emitido_dir / ref).is_file(),
                            f"enlace roto en la emisión: {ref}")


class TestTransmutarVelaFuente(CasoPneuma):
    """Fix 2: transmutar valida su fuente con los checks ontológicos."""

    def test_pi_fuera_de_reticulo_exit_1_sin_traceback(self):
        self.escribir_skill(skill_campos(vector=[7, 0, 1, 0, 1]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("la fuente no pasa velar", err)
        self.assertIn("[vector-en-reticulo]", err)
        self.assertIn("transmutar exige fuente coherente", err)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_sigma_fuera_de_reticulo_no_emite(self):
        self.escribir_skill(skill_campos(sigma=[1, 1, 1, 1, 5]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("la fuente no pasa velar", err)
        self.assertIn("sigma.sustainability=5", err)
        self.assertFalse((self.raiz / "_emision").exists(),
                         "una violación de sigma no se normaliza como pérdida")


class TestColisionEmision(CasoPneuma):
    """Fix 3: dos artefactos con el mismo nombre no se pisan en _emision/."""

    def test_mismo_nombre_distinto_urn_aborta(self):
        self.escribir_skill()  # urn:kora:artefacto:util-x en ns kora
        self.escribir_skill(
            skill_campos(urn="urn:dev:artefacto:util-x"), ns="dev")
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("colisión de nombre 'util-x'", err)
        self.assertIn("urn:kora:artefacto:util-x", err)
        self.assertIn("urn:dev:artefacto:util-x", err)
        self.assertIn("renombra uno", err)
        self.assertFalse((self.raiz / "_emision").exists())


class TestCicloQuirurgico(CasoPneuma):
    """Fix 4: ciclo solo toca el valor de estado; CRLF y comentarios viven."""

    def test_crlf_byte_identico_salvo_valor(self):
        texto = doc(skill_campos(estado="borrador")).replace("\n", "\r\n")
        path = self.raiz / "artefactos/skills/kora/util-x/SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(texto.encode("utf-8"))
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 0)
        esperado = texto.replace(
            "estado: borrador", "estado: activo").encode("utf-8")
        self.assertEqual(path.read_bytes(), esperado,
                         "los terminadores CRLF deben preservarse")

    def test_comentario_inline_sobrevive(self):
        campos = skill_campos(estado="borrador  # nota del operador")
        path = self.escribir_skill(campos)
        original = path.read_text(encoding="utf-8")
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 0)
        nuevo = path.read_text(encoding="utf-8")
        self.assertIn("estado: activo  # nota del operador", nuevo)
        self.assertEqual(
            original.replace("estado: borrador  # nota del operador",
                             "estado: activo  # nota del operador"),
            nuevo, "solo el valor de estado puede cambiar")


class TestSelloUltimoBloque(CasoPneuma):
    """Fix 5: sello-fresco lee el ÚLTIMO bloque; los citados no dan rancia."""

    def test_sello_citado_en_cuerpo_no_da_rancia(self):
        cuerpo = (
            "# Doc\n\nEjemplo de sello citado de la ley:\n\n"
            "<!-- kora:sello\n"
            "fuente: urn:kora:artefacto:ejemplo-citado\n"
            "hash-fuente: sha256:deadbeef\n"
            "-->\n\nFin del cuerpo.\n")
        self.escribir_skill(cuerpo=cuerpo)
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 0)
        emitido = self.raiz / "_emision/claude-code/skills/util-x/SKILL.md"
        texto = emitido.read_text(encoding="utf-8")
        self.assertGreaterEqual(texto.count("<!-- kora:sello"), 2,
                                "el escenario exige sello citado + sello real")
        self.assertEqual(self.fallos("sello-fresco"), [],
                         "el sello real (último) está fresco")


class TestListaEstricta(unittest.TestCase):
    """Fix 6: la forma de lista es estricta; corchetes de más son error."""

    def test_doble_cierre_es_error(self):
        with self.assertRaises(kora.ErrorDeForma) as ctx:
            kora.parsear_archivo("---\nherramientas: [Read, Grep]]\n---\n")
        self.assertIn("']'", str(ctx.exception))
        self.assertEqual(ctx.exception.linea, 2)

    def test_texto_tras_cierre_es_error(self):
        with self.assertRaises(kora.ErrorDeForma) as ctx:
            kora.parsear_archivo("---\nherramientas: [Read] extra\n---\n")
        self.assertIn("después del cierre", str(ctx.exception))


class TestCiclosProfundos(unittest.TestCase):
    """Fix 7: detección de ciclos iterativa; cadenas de 2000 no revientan."""

    def test_cadena_de_2000_sin_recursion(self):
        grafo = {f"n{i:04d}": [f"n{i + 1:04d}"] for i in range(2000)}
        grafo["n2000"] = []
        self.assertEqual(kora._ciclos_en(grafo), [])

    def test_ciclo_de_2000_detectado(self):
        grafo = {f"n{i:04d}": [f"n{(i + 1) % 2000:04d}"]
                 for i in range(2000)}
        ciclos = kora._ciclos_en(grafo)
        self.assertEqual(len(ciclos), 1)
        self.assertEqual(len(ciclos[0]), 2000)


class TestZonaSkillsLimpia(CasoPneuma):
    """Fix 8: solo skills/{ns}/{nombre}/SKILL.md es artefacto."""

    def test_skill_md_en_referencias_no_se_indexa(self):
        self.escribir_skill()
        self.escribir("artefactos/skills/kora/util-x/referencias/SKILL.md",
                      "esto no es un artefacto y no debe parsearse\n")
        censo = kora.construir_censo(kora.cargar_corpus(self.raiz))
        self.assertEqual(len(censo), 1)
        self.assertEqual(censo[0]["path"],
                         "artefactos/skills/kora/util-x/SKILL.md")
        self.assert_todo_coherente()

    def test_md_suelto_en_skills_falla_claro(self):
        self.escribir_skill()
        self.escribir("artefactos/skills/kora/nota-suelta.md", "# suelta\n")
        self.assert_fallo("lugar-coincide", "fuera de lugar")
        censo = kora.construir_censo(kora.cargar_corpus(self.raiz))
        self.assertEqual(len(censo), 1, "el .md suelto no se indexa")


class TestBom(CasoPneuma):
    """Fix 9: el BOM UTF-8 se acepta y se descarta al leer artefactos."""

    def test_bom_aceptado_y_descartado(self):
        texto = doc(skill_campos())
        path = self.raiz / "artefactos/skills/kora/util-x/SKILL.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"\xef\xbb\xbf" + texto.encode("utf-8"))
        arts = kora.cargar_corpus(self.raiz)
        self.assertEqual(len(arts), 1)
        self.assertIsNone(arts[0].error_parse)
        self.assertEqual(arts[0].urn, "urn:kora:artefacto:util-x")
        self.assert_todo_coherente()


class TestPipeCerrado(unittest.TestCase):
    """Fix 10: `kora.py ley | head` no debe reventar con BrokenPipeError."""

    def test_ley_con_pipe_cerrado_sale_limpio(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            relleno = ("x" * 78 + "\n") * 4000  # ~316 KB > buffer del pipe
            (raiz / "ALMA.md").write_text("# ALMA\n" + relleno,
                                          encoding="utf-8")
            (raiz / "ley").mkdir()
            for pieza in ("0-constitucion", "1-ontologia", "2-forma",
                          "3-transmutacion", "4-koraficacion"):
                (raiz / "ley" / f"{pieza}.md").write_text(
                    f"# {pieza}\n", encoding="utf-8")
            env = dict(os.environ, KORA_RAIZ=str(raiz))
            proc = subprocess.Popen(
                [sys.executable, str(Path(kora.__file__)), "ley"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            proc.stdout.readline()   # consume una línea, como `head -1`
            proc.stdout.close()      # cierra el pipe aguas abajo
            err = proc.stderr.read()
            proc.stderr.close()
            codigo = proc.wait(timeout=30)
            self.assertEqual(codigo, 0, err.decode("utf-8", "replace"))
            self.assertNotIn(b"Traceback", err)
            self.assertNotIn(b"BrokenPipeError", err)


class TestGatePromocion(CasoPneuma):
    """Fix 11: nadie asciende a publicado/activo sin pasar velar."""

    def test_borrador_violatorio_no_asciende(self):
        path = self.escribir_skill(skill_campos(
            estado="borrador", vector=[1, 2, 1, 0, 1]))  # mu=2: ilegal
        codigo, _, err = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 1)
        self.assertIn("promoción rechazada", err)
        self.assertIn("no pasa velar", err)
        self.assertIn("estado: borrador", path.read_text(encoding="utf-8"),
                      "el archivo no debe modificarse al rechazar")

    def test_deprecar_no_exige_gate(self):
        path = self.escribir_skill(skill_campos(
            estado="borrador", vector=[1, 2, 1, 0, 1]))
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "deprecado"])
        self.assertEqual(codigo, 0)
        self.assertIn("estado: deprecado", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
