# -*- coding: utf-8 -*-
"""Tests del núcleo kora.py — corpus sintéticos en tempdir (contrato §7)."""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from itertools import product
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

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

    def test_conocimiento_no_requiere_familia(self):
        campos = conocimiento_campos()
        del campos["familia"]
        self.escribir_conocimiento(campos)
        self.assert_todo_coherente()

    def test_familia_presente_sigue_siendo_enum_cerrado(self):
        self.escribir_conocimiento(conocimiento_campos(familia="otra"))
        self.assert_fallo("forma-valida", "familia inválida: 'otra'")

    def test_artefacto_agentico_no_requiere_targets(self):
        campos = skill_campos()
        del campos["targets"]
        self.escribir_skill(campos)
        self.assert_todo_coherente()

    def test_targets_presentes_siguen_siendo_lista_no_vacia(self):
        self.escribir_skill(skill_campos(targets=[]))
        self.assert_fallo("forma-valida", "targets no puede ser una lista vacía")


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

    def test_camino_compuesto_y_salto_coinciden_en_dominio_comun(self):
        path = self.escribir_skill(skill_campos(estado="borrador"))
        original = path.read_text(encoding="utf-8")
        for estado in ("activo", "deprecado", "retirado"):
            codigo, _, _ = self.correr(
                ["ciclo", "urn:kora:artefacto:util-x", estado])
            self.assertEqual(codigo, 0, estado)
        compuesto = path.read_bytes()

        path.write_text(original, encoding="utf-8")
        codigo, _, _ = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "retirado"])
        self.assertEqual(codigo, 0)
        self.assertEqual(
            path.read_bytes(), compuesto,
            "en el dominio común, componer avances y saltar debe dejar "
            "el mismo snapshot")

    def test_promocion_evalua_dignidad_del_estado_destino(self):
        path = self.escribir_conocimiento(conocimiento_campos(
            estado="borrador", fuente='""'))
        codigo, _, err = self.correr(
            ["ciclo", "urn:kora:kb:nota-x", "publicado"])
        self.assertEqual(codigo, 1)
        self.assertIn("[publicacion-digna]", err)
        self.assertIn("'fuente' no vacío", err)
        self.assertIn("estado: borrador", path.read_text(encoding="utf-8"))


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

    def test_depende_no_exige_cierre_transitivo_materializado(self):
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:a", nombre="a", depende=["urn:kora:kb:b"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:b", nombre="b", depende=["urn:kora:kb:c"]))
        self.escribir_conocimiento(conocimiento_campos(
            urn="urn:kora:kb:c", nombre="c"))
        self.assert_todo_coherente()


# ------------------------------------------ 10b. núcleo categorial demostrable

class TestNucleoCategorial(CasoPneuma):

    def test_cada_matriz_realiza_una_coreflexion_escalar(self):
        """La proyección por coordenada es monótona, descendente e idempotente.

        Para a en la imagen y d en el dominio soportado verifica además:
        a <= d  sii  a <= P(d), la adjunción inclusión ⊣ proyección.
        """
        for target in kora.TARGETS_REALIZADOS:
            matriz = kora.MATRICES[target]
            for eje in kora.EJES:
                with self.subTest(target=target, eje=eje):
                    tabla = matriz[eje]
                    dominio_total = list(range(kora.RANGO_EJE[eje] + 1))
                    self.assertEqual(sorted(tabla), dominio_total)
                    dominio = [d for d in dominio_total
                               if tabla[d][0] is not None]
                    self.assertEqual(
                        dominio, list(range(max(dominio) + 1)),
                        "el dominio soportado debe ser un segmento inicial")
                    imagen = sorted({tabla[d][0] for d in dominio})
                    for d in dominio:
                        pd = tabla[d][0]
                        self.assertLessEqual(pd, d)
                        self.assertEqual(tabla[pd][0], pd)
                    for d1 in dominio:
                        for d2 in dominio:
                            if d1 <= d2:
                                self.assertLessEqual(
                                    tabla[d1][0], tabla[d2][0])
                    for a in imagen:
                        for d in dominio:
                            self.assertEqual(a <= d, a <= tabla[d][0])

            for i, nombre in enumerate(kora.SIGMA_NOMBRES):
                with self.subTest(target=target, sigma=nombre):
                    tope = matriz["sigma-max"][i]
                    p = lambda valor: min(valor, tope)
                    imagen = range(tope + 1)
                    for d in range(4):
                        self.assertLessEqual(p(d), d)
                        self.assertEqual(p(p(d)), p(d))
                    for d1 in range(4):
                        for d2 in range(d1, 4):
                            self.assertLessEqual(p(d1), p(d2))
                    for a in imagen:
                        for d in range(4):
                            self.assertEqual(a <= d, a <= p(d))

    def test_proyeccion_preserva_las_cinco_leyes_inter_eje(self):
        for target in kora.TARGETS_REALIZADOS:
            matriz = kora.MATRICES[target]

            def soportados(eje):
                return [x for x, (px, _, _) in matriz[eje].items()
                        if px is not None]

            def p(eje, valor):
                return matriz[eje][valor][0]

            for pi, mu in product(soportados("pi"), soportados("mu")):
                if not (pi >= 3 and mu < 1):
                    self.assertFalse(
                        p("pi", pi) >= 3 and p("mu", mu) < 1,
                        (target, "ley 1", pi, mu))

            for xi, lam in product(soportados("xi"),
                                   soportados("lambda")):
                if not (xi == 4 and lam < 1):
                    self.assertFalse(
                        p("xi", xi) == 4 and p("lambda", lam) < 1,
                        (target, "ley 2", xi, lam))

            for phi, mu in product(soportados("phi"), soportados("mu")):
                if not (phi >= 2 and mu < 1):
                    self.assertFalse(
                        p("phi", phi) >= 2 and p("mu", mu) < 1,
                        (target, "ley 3", phi, mu))

            maximos = matriz["sigma-max"]
            for transparency, accountability in product(range(4), repeat=2):
                if not (accountability >= 2 and transparency < 2):
                    pt = min(transparency, maximos[2])
                    pa = min(accountability, maximos[3])
                    self.assertFalse(
                        pa >= 2 and pt < 2,
                        (target, "ley 4", transparency, accountability))

            for lam in soportados("lambda"):
                for sigma in product(range(4), repeat=5):
                    if not (lam == 3 and min(sigma) < 2):
                        plam = p("lambda", lam)
                        psigma = [min(x, maximos[i])
                                  for i, x in enumerate(sigma)]
                        self.assertFalse(
                            plam == 3 and min(psigma) < 2,
                            (target, "ley 5", lam, sigma))

    def test_fidelidad_es_antitona_en_la_demanda(self):
        """Más demanda fuente nunca puede mejorar la fidelidad declarada."""
        rango = {"none": 0, "partial": 1, "full": 2}
        for target in kora.TARGETS_REALIZADOS:
            matriz = kora.MATRICES[target]
            for eje in kora.EJES:
                tabla = matriz[eje]
                for menor in tabla:
                    for mayor in tabla:
                        if menor <= mayor:
                            self.assertGreaterEqual(
                                rango[tabla[menor][1]],
                                rango[tabla[mayor][1]],
                                (target, eje, menor, mayor))
                for valor, (proyectado, fidelidad, razon) in tabla.items():
                    if fidelidad == "full":
                        self.assertEqual(
                            proyectado, valor,
                            (target, eje, valor, "full exige no perder ordinal"))
                    if fidelidad == "none":
                        self.assertIsNone(
                            proyectado,
                            (target, eje, valor, "none exige no proyectable"))
                    if fidelidad != "full":
                        self.assertTrue(
                            razon, (target, eje, valor,
                                    "toda pérdida exige razón"))

            maximos = matriz["sigma-max"]
            firmas = list(product(range(4), repeat=5))

            def fidelidad_sigma(firma):
                return 2 if all(
                    valor <= maximos[i]
                    for i, valor in enumerate(firma)) else 1

            for menor in firmas:
                for mayor in firmas:
                    if all(x <= y for x, y in zip(menor, mayor)):
                        self.assertGreaterEqual(
                            fidelidad_sigma(menor),
                            fidelidad_sigma(mayor),
                            (target, "sigma", menor, mayor))

    def test_velar_estricto_extiende_el_mismo_registro_base(self):
        self.escribir_conocimiento()
        base = kora.velar_todo(self.raiz)
        estricto = kora.velar_todo(self.raiz, estricto=True)
        self.assertEqual(list(base), list(kora.CHECKS))
        self.assertEqual(
            list(estricto), list(kora.CHECKS) + list(kora.CHECKS_ESTRICTOS))
        for check in kora.CHECKS:
            self.assertEqual(base[check], estricto[check], check)

    def test_firmas_iguales_no_colapsan_identidades(self):
        self.escribir_skill(skill_campos())
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:util-y", nombre="util-y"))
        self.assert_todo_coherente()


# ---------------------------------------------------------- 11. transmutación

class TestTransmutacion(CasoPneuma):

    def test_sin_target_emite_codex_por_defecto(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        codigo, _, error = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
        ])
        self.assertEqual(codigo, 0, error)
        self.assertTrue((self.raiz /
                         "_emision/codex/skills/util-x/SKILL.md").is_file())

    def test_sin_target_no_busca_fallback_fuera_de_codex(self):
        self.escribir_skill(skill_campos(targets=["claude-code"]))
        codigo, _, error = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
        ])
        self.assertEqual(codigo, 1, error)
        self.assertIn("no declara el target 'codex'", error)
        self.assertFalse((self.raiz / "_emision/claude-code").exists())

    def test_sin_targets_admite_target_explicito_realizado(self):
        campos = skill_campos()
        del campos["targets"]
        self.escribir_skill(campos)
        codigo, _, error = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])
        self.assertEqual(codigo, 0, error)
        self.assertTrue((self.raiz /
                         "_emision/claude-code/skills/util-x/SKILL.md").is_file())
        self.assert_todo_coherente()

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
        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])

    def test_contrato_conocimiento_en_sello(self):
        # Una skill con corpus declarado: el sello porta el contrato
        # (ancla + resolución por censo + URN), sin materializar paths.
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:identidad-estable",
            conocimiento=["urn:fxsl:kb:icas-sintesis",
                          "urn:fxsl:kb:icas-efectos"],
            componible=["urn:kora:artefacto:identidad-estable"]))
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:identidad-estable",
             "--target", "claude-code", "--stdout"])
        self.assertEqual(codigo, 0)
        self.assertIn("contrato-conocimiento:", salida)
        self.assertIn("ancla: ~/kora-pneuma", salida)
        self.assertIn("resolucion-bash: python3 {ancla}/kora.py nombre <URN>",
                      salida)
        self.assertIn("resolucion-lectura: Grep exacto '^urn: <URN>$' bajo "
                      "{ancla}/artefactos; exigir coincidencia unica", salida)
        self.assertNotIn("derivacion:", salida)
        # Los URN van listados; NINGÚN path concreto se hornea.
        self.assertIn("conocimiento: urn:fxsl:kb:icas-sintesis "
                      "urn:fxsl:kb:icas-efectos", salida)
        self.assertIn("componible: urn:kora:artefacto:identidad-estable",
                      salida)
        self.assertNotIn("artefactos/conocimiento/fxsl/icas-sintesis.md",
                         salida)
        # URN id != nombre: nunca se inventa un path desde el id estable.
        self.assertNotIn("artefactos/skills/kora/identidad-estable", salida)
        # El contrato no se interpone entre las dos líneas fijas y el cierre.
        cola = salida[salida.rindex("preservado-por-construccion"):]
        self.assertNotIn("contrato-conocimiento", cola)

    def test_sello_distingue_depende_operacional_de_componible_candidato(self):
        self.escribir_skill(skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["codex"]), ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"],
            componible=["urn:kora:artefacto:candidato-x"]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex", "--stdout",
        ])

        self.assertEqual(codigo, 0, salida or err)
        self.assertIn(
            "depende: urn:dev:artefacto:disciplina-x", salida)
        self.assertIn(
            "componible: urn:kora:artefacto:candidato-x", salida)

    def test_sin_corpus_no_emite_contrato(self):
        # Un agéntico sin conocimiento ni componible no carga bloque vacío:
        # la emisión queda byte-idéntica a la previa al contrato.
        self.escribir_skill()
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code", "--stdout"])
        self.assertEqual(codigo, 0)
        self.assertNotIn("contrato-conocimiento", salida)

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
        self.assertIn("nativo de delegación del runtime", texto)
        self.assertNotIn("Task()", texto)

    def test_mu3_a_claude_code_falla(self):
        self.escribir_agente(agente_campos(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 3, 1, 1], sigma=[2, 1, 2, 1, 1],
            targets=["claude-code", "openclaw"]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("mu=3", err)
        self.assertIn("openclaw", err)
        self.assertNotIn("hermes", err)

    def test_determinismo_byte_a_byte(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        argv = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "codex"]
        self.assertEqual(self.correr(argv)[0], 0)
        emitido = self.raiz / "_emision/codex/skills/util-x/SKILL.md"
        primera = emitido.read_bytes()
        self.assertEqual(self.correr(argv)[0], 0)
        self.assertEqual(primera, emitido.read_bytes())

    def test_target_realizado_emite(self):
        # Hermes está realizado desde ley/3 v3.0.0 para habilidades y v4.0.0
        # para agentes completos; este caso fija el contrato skill v1.
        self.escribir_skill(skill_campos(targets=["hermes"]))
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 0)
        self.assertIn("_emision/hermes/skills/util-x/SKILL.md", salida)

    def test_codex_persona_emite_agente_y_skill_explicito(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        agente = self.raiz / "_emision/codex/agents/agente-x.toml"
        skill = self.raiz / "_emision/codex/skills/agente-x/SKILL.md"
        politica = self.raiz / (
            "_emision/codex/skills/agente-x/agents/openai.yaml")
        self.assertTrue(agente.is_file())
        self.assertTrue(skill.is_file())
        self.assertTrue(politica.is_file())
        datos = tomllib.loads(agente.read_text(encoding="utf-8"))
        self.assertEqual(datos["name"], "agente-x")
        self.assertIn("Texto sintético.", datos["developer_instructions"])
        self.assertIn("funtor: T-codex-pneuma-v2",
                      datos["developer_instructions"])
        self.assertNotIn("codex no registra agentes",
                         datos["developer_instructions"])
        self.assertIn("nativo de delegación del runtime",
                      datos["developer_instructions"])
        self.assertNotIn("Task()", datos["developer_instructions"])
        self.assertIn("fidelidad-campos: herramientas:partial",
                      datos["developer_instructions"])
        self.assertIn(
            "herramientas: allowlist[Read,Write]->"
            "sin-allowlist-builtins-local ::",
                      datos["developer_instructions"])
        self.assertNotIn("->sesion-padre", datos["developer_instructions"])
        self.assertIn("allow_implicit_invocation: false",
                      politica.read_text(encoding="utf-8"))

    def test_codex_depende_emite_skill_requerida_como_unidad_propia(self):
        dependencia = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["codex"])
        self.escribir_skill(dependencia, ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])

        self.assertEqual(codigo, 0, salida or err)
        requerida = self.raiz / (
            "_emision/codex/skills/disciplina-x/SKILL.md")
        self.assertTrue(requerida.is_file())
        texto = requerida.read_text(encoding="utf-8")
        self.assertIn("fuente: urn:dev:artefacto:disciplina-x", texto)
        self.assertNotIn("fuente: urn:dev:artefacto:agente-x", texto)

    def test_depende_materializa_cierre_transitivo_de_skills(self):
        base = skill_campos(
            urn="urn:dev:artefacto:base-x",
            nombre="base-x", targets=["codex"])
        disciplina = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["codex"],
            depende=["urn:dev:artefacto:base-x"])
        self.escribir_skill(base, ns="dev")
        self.escribir_skill(disciplina, ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])

        self.assertEqual(codigo, 0, salida or err)
        self.assertTrue((self.raiz /
                         "_emision/codex/skills/base-x/SKILL.md").is_file())
        self.assertTrue((self.raiz /
                         "_emision/codex/skills/disciplina-x/SKILL.md").is_file())

    def test_dependencia_agentica_no_realizable_falla_antes_de_emitir(self):
        self.escribir_skill(skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["claude-code"]), ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("dependencia", err)
        self.assertIn("no declara el target 'codex'", err)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_dependencia_agentica_inactiva_falla_antes_de_emitir(self):
        self.escribir_skill(skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", estado="deprecado",
            targets=["codex"]), ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("dependencia agentica", err)
        self.assertIn("no esta activa (estado: deprecado)", err)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_depende_agentico_rechaza_agente_como_requisito_no_realizado(self):
        self.escribir_agente(agente_campos(
            urn="urn:dev:artefacto:agente-y", nombre="agente-y",
            targets=["codex"]))
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:agente-y"]))

        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("dependencia agentica", err)
        self.assertIn("solo realiza dependencias de forma habilidad", err)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_codex_skill_transporta_sidecar_fuente_sin_aplanarlo(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        metadata = (
            'interface:\n'
            '  display_name: "Util X"\n'
            'policy:\n'
            '  allow_implicit_invocation: false\n'
        )
        self.escribir(
            "artefactos/skills/kora/util-x/agents/openai.yaml", metadata)
        codigo, salida, error = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "codex",
        ])
        self.assertEqual(codigo, 0, error)
        emitido = self.raiz / (
            "_emision/codex/skills/util-x/agents/openai.yaml")
        self.assertEqual(emitido.read_text("utf-8"), metadata)
        self.assertIn("agents/openai.yaml", salida)

        with mock.patch.dict(
                kora.RUTAS_APLICAR,
                {("codex", "skill"): str(
                    self.raiz / "runtime/skills/{nombre}")},
                clear=False):
            codigo, _, error = self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "codex", "--aplicar",
            ])
        self.assertEqual(codigo, 0, error)
        instalado = self.raiz / (
            "runtime/skills/util-x/agents/openai.yaml")
        self.assertEqual(instalado.read_text("utf-8"), metadata)
        self.assertFalse(
            (self.raiz / "runtime/skills/util-x/openai.yaml").exists())

    def test_codex_subagente_emite_solo_custom_agent(self):
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 1], sigma=[1, 1, 1, 1, 1],
            targets=["codex"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        self.assertTrue((self.raiz /
                         "_emision/codex/agents/agente-x.toml").is_file())
        self.assertFalse((self.raiz /
                          "_emision/codex/skills/agente-x").exists())

    def test_codex_v2_retira_skill_v1_huerfana_de_subagente(self):
        viejo = self.raiz / "_emision/codex/skills/agente-x/SKILL.md"
        viejo.parent.mkdir(parents=True)
        viejo.write_text("derivado v1\n", encoding="utf-8")
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 1], sigma=[1, 1, 1, 1, 1],
            targets=["codex"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        self.assertFalse(viejo.parent.exists())

    def test_codex_sello_v2_tambien_en_skill(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/codex/skills/util-x/SKILL.md").read_text("utf-8")
        self.assertIn("funtor: T-codex-pneuma-v2", texto)
        self.assertIn("fidelidad-campos: herramientas:partial", texto)
        self.assertIn("herramientas: allowlist[Read]->"
                      "sin-allowlist-builtins-local ::", texto)
        self.assertIn("no ofrece una allowlist exacta", texto)
        self.assertNotIn("->sesion-padre", texto)

    def test_target_no_declarado_falla(self):
        self.escribir_skill(skill_campos(targets=["claude-code"]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex"])
        self.assertEqual(codigo, 1)
        self.assertIn("no declara el target 'codex'", err)

    def test_aplicar_exige_artefacto_activo(self):
        self.escribir_skill(skill_campos(
            estado="deprecado", targets=["codex"]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex", "--aplicar"])
        self.assertEqual(codigo, 1)
        self.assertIn("--aplicar exige estado 'activo'", err)

    def test_opencode_emite_modo(self):
        self.escribir_agente()
        self.escribir_agente(agente_campos(
            urn="urn:dev:artefacto:sub-x", nombre="sub-x",
            forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 1], sigma=[1, 1, 1, 1, 1]))
        for urn, modo, nombre in (
                ("urn:dev:artefacto:agente-x", "mode: all", "agente-x"),
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
        self.assert_fallo(
            "sello-fresco", "emisión rancia, re-transmutar", estricto=True)

    def test_conocimiento_no_se_transmuta(self):
        self.escribir_conocimiento()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:kb:nota-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 1)
        self.assertIn("no se transmuta", err)


# ------------------------------------- 11b. openclaw: workspace multi-archivo

def cuerpo_persona(operativa, voz):
    """Cuerpo de agente persona con el span de U_phen delimitado por el
    centinela canónico kora:soul (ley/2 §10 r6)."""
    return (f"# agente-x\n\n## Operativa\n\n{operativa}\n\n"
            f"{kora.SOUL_ABRE}\n## Voz\n\n{voz}\n{kora.SOUL_CIERRA}\n")


class TestOpenclaw(CasoPneuma):
    """openclaw realizado (ley/3 v1.3.0): emite un WORKSPACE multi-archivo
    (AGENTS.md = operativa sin U_phen; SOUL.md = voz/U_phen), no un
    monolito. Conformidad real verificada contra ~/openclaw-fleet."""

    def _emitir_persona(self, **over):
        campos = agente_campos(targets=["openclaw"], **over)
        self.escribir("artefactos/agentes/dev/agente-x.md",
                      doc(campos, cuerpo_persona("Regla de operacion uno.",
                                                 "Tono directo y denso.")))
        return self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "openclaw"])

    def test_workspace_segrega_voz_de_operativa(self):
        codigo, _, _ = self._emitir_persona()
        self.assertEqual(codigo, 0)
        ws = self.raiz / "_emision/openclaw/workspaces/agente-x"
        agents = ws / "AGENTS.md"
        soul = ws / "SOUL.md"
        self.assertTrue(agents.is_file())
        self.assertTrue(soul.is_file())
        ta = agents.read_text(encoding="utf-8")
        ts = soul.read_text(encoding="utf-8")
        # AGENTS.md = operativa: el span de voz no se duplica ni se filtra a
        # subagentes que sólo reciben las reglas operativas.
        self.assertFalse(ta.startswith("---"))   # markdown plano, sin frontmatter
        self.assertIn("Regla de operacion uno.", ta)
        self.assertNotIn("Tono directo y denso.", ta)
        self.assertNotIn(kora.SOUL_ABRE, ta)
        self.assertNotIn(kora.SOUL_CIERRA, ta)
        self.assertIn("funtor: T-openclaw-pneuma-v1", ta)
        self.assertIn("target: openclaw", ta)
        # SOUL.md = voz PURA: tiene la voz, NO la operativa. La doc de openclaw
        # prohíbe operativa en SOUL.md.
        self.assertIn("Tono directo y denso.", ts)
        self.assertIn("## Voz", ts)
        self.assertNotIn("Regla de operacion uno.", ts)
        self.assertNotIn("## Operativa", ts)
        self.assertNotIn(kora.SOUL_ABRE, ts)
        self.assertNotIn(kora.SOUL_CIERRA, ts)
        # Ambos archivos se auto-certifican con el sello.
        self.assertIn("<!-- kora:sello", ta)
        self.assertIn("<!-- kora:sello", ts)
        # sello fresco no reclama sobre el workspace recién emitido.
        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])

    def test_otros_targets_conservan_el_cuerpo_completo(self):
        campos = agente_campos(targets=["claude-code", "openclaw"])
        cuerpo = cuerpo_persona("Regla operativa.", "Voz inconfundible.")
        self.escribir("artefactos/agentes/dev/agente-x.md",
                      doc(campos, cuerpo))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "claude-code"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/claude-code/agents/agente-x.md").read_text("utf-8")
        self.assertIn("Regla operativa.", texto)
        self.assertIn("Voz inconfundible.", texto)
        self.assertIn(kora.SOUL_ABRE, texto)
        self.assertIn(kora.SOUL_CIERRA, texto)

    def test_sello_declara_frontera_sin_fingir_realizacion(self):
        codigo, _, _ = self._emitir_persona()
        self.assertEqual(codigo, 0)
        ws = self.raiz / "_emision/openclaw/workspaces/agente-x"
        for archivo in ("AGENTS.md", "SOUL.md"):
            texto = (ws / archivo).read_text(encoding="utf-8")
            self.assertIn(
                "frontera-herramientas-declarada: [Read,Write]", texto)
            self.assertIn(
                "frontera-herramientas-realizacion: openclaw.json/deploy "
                "(fuera del funtor; no verificada por este sello)", texto)

    def test_matriz_mu3_xi4_full(self):
        # plataforma/servicio con mu=3 y xi=4: openclaw los proyecta FULL —
        # único target que lo logra (techo más alto, ley/3 §4.4).
        codigo, _, _ = self._emitir_persona(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 4, 1, 2], sigma=[2, 1, 2, 1, 1])
        self.assertEqual(codigo, 0)
        ta = (self.raiz /
              "_emision/openclaw/workspaces/agente-x/AGENTS.md").read_text(
                  encoding="utf-8")
        self.assertIn("vector-proyectado: [2,3,4,1,2] sigma [2,1,2,1,1]", ta)
        self.assertIn("fidelidad: pi:full mu:full xi:full lambda:full "
                      "phi:full sigma:full", ta)
        self.assertNotIn("perdidas:", ta)

    def test_mu3_califica_realiza_difiere(self):
        # mu=3: el sello califica realiza/difiere en AMBOS archivos del
        # workspace (ley/3 §7.1 r5) — el funtor realiza la emisión conforme al
        # techo always-on (TIPO), difiere la conducta always-on al deploy
        # (TOKEN). Observable en el proof-carrier, no sólo en la ley.
        codigo, _, _ = self._emitir_persona(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 4, 1, 2], sigma=[2, 1, 2, 1, 1])
        self.assertEqual(codigo, 0)
        ws = self.raiz / "_emision/openclaw/workspaces/agente-x"
        for archivo in ("AGENTS.md", "SOUL.md"):
            t = (ws / archivo).read_text(encoding="utf-8")
            self.assertIn("realiza: workspace-mu3-conforme", t)
            self.assertIn("difiere: conducta-always-on", t)

    def test_mu_menor_3_sin_calificacion(self):
        # mu<3 (persona default mu=2): no hay always-on que diferir.
        codigo, _, _ = self._emitir_persona()
        self.assertEqual(codigo, 0)
        ta = (self.raiz /
              "_emision/openclaw/workspaces/agente-x/AGENTS.md").read_text(
                  encoding="utf-8")
        self.assertNotIn("realiza: workspace-mu3", ta)
        self.assertNotIn("difiere: conducta-always-on", ta)

    def test_lambda3_partial_unico_target(self):
        # lambda=3: openclaw es el ÚNICO target que lo proyecta (partial).
        codigo, _, _ = self._emitir_persona(
            forma="plataforma", arnes="servicio",
            vector=[2, 3, 3, 3, 2], sigma=[2, 2, 2, 2, 2])
        self.assertEqual(codigo, 0)
        ta = (self.raiz /
              "_emision/openclaw/workspaces/agente-x/AGENTS.md").read_text(
                  encoding="utf-8")
        self.assertIn("lambda: 3->3 :: society-in-the-loop", ta)
        self.assertIn("lambda:partial", ta)

    def test_persona_sin_centinela_falla_honesto(self):
        # arnes con U_phen + openclaw, sin centinela: el núcleo no fabrica voz.
        campos = agente_campos(targets=["openclaw"])
        self.escribir("artefactos/agentes/dev/agente-x.md", doc(campos))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "openclaw"])
        self.assertEqual(codigo, 1)
        self.assertIn("centinela", err)
        self.assertIn("forma-no-verdad", err)
        self.assertFalse((self.raiz / "_emision").exists())

    def test_delegado_sin_soul(self):
        # subagente/delegado NO porta U_phen: workspace con AGENTS.md y SIN
        # SOUL.md (no hay persona que segregar).
        campos = agente_campos(
            urn="urn:dev:artefacto:sub-x", nombre="sub-x",
            forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 1], sigma=[1, 1, 1, 1, 1],
            targets=["openclaw"])
        self.escribir("artefactos/agentes/dev/sub-x.md", doc(campos))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:sub-x",
             "--target", "openclaw"])
        self.assertEqual(codigo, 0)
        ws = self.raiz / "_emision/openclaw/workspaces/sub-x"
        self.assertTrue((ws / "AGENTS.md").is_file())
        self.assertFalse((ws / "SOUL.md").exists())

    def test_skill_a_openclaw(self):
        self.escribir_skill(skill_campos(targets=["openclaw"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "openclaw"])
        self.assertEqual(codigo, 0)
        sk = self.raiz / "_emision/openclaw/skills/util-x/SKILL.md"
        self.assertTrue(sk.is_file())
        texto = sk.read_text(encoding="utf-8")
        self.assertIn("name: util-x", texto)
        self.assertIn("funtor: T-openclaw-pneuma-v1", texto)

    def test_byte_determinismo_workspace(self):
        self.assertEqual(self._emitir_persona()[0], 0)
        ws = self.raiz / "_emision/openclaw/workspaces/agente-x"
        a1 = (ws / "AGENTS.md").read_bytes()
        s1 = (ws / "SOUL.md").read_bytes()
        self.assertEqual(self._emitir_persona()[0], 0)
        self.assertEqual(a1, (ws / "AGENTS.md").read_bytes())
        self.assertEqual(s1, (ws / "SOUL.md").read_bytes())

    def test_sello_rancio_en_workspace(self):
        self.assertEqual(self._emitir_persona()[0], 0)
        fuente = self.raiz / "artefactos/agentes/dev/agente-x.md"
        fuente.write_text(fuente.read_text(encoding="utf-8") + "\nx\n",
                          encoding="utf-8")
        self.assert_fallo(
            "sello-fresco", "emisión rancia, re-transmutar", estricto=True)

    def test_stdout_multi_archivo(self):
        campos = agente_campos(targets=["openclaw"])
        self.escribir("artefactos/agentes/dev/agente-x.md",
                      doc(campos, cuerpo_persona("Op uno.", "Voz dos.")))
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "openclaw", "--stdout"])
        self.assertEqual(codigo, 0)
        self.assertIn("=== openclaw/workspaces/agente-x/AGENTS.md ===", salida)
        self.assertIn("=== openclaw/workspaces/agente-x/SOUL.md ===", salida)
        self.assertFalse((self.raiz / "_emision").exists())


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

    def test_rechaza_modos_de_salida_incompatibles(self):
        combinaciones = (
            ("--json", "--escribir"),
            ("--json", "--huerfanos"),
            ("--escribir", "--huerfanos"),
        )
        for izquierda, derecha in combinaciones:
            with self.subTest(izquierda=izquierda, derecha=derecha):
                codigo, salida, err = self.correr(
                    ["censo", izquierda, derecha])
                self.assertEqual(codigo, 2)
                self.assertEqual(salida, "")
                self.assertIn("modos de salida incompatibles", err)
                self.assertFalse((self.raiz / "censo.json").exists())

    def test_nombre_inexistente_falla(self):
        codigo, _, err = self.correr(["nombre", "urn:kora:kb:fantasma"])
        self.assertEqual(codigo, 1)
        self.assertIn("no resuelve", err)

    def test_nombre_resuelve_sin_confundir_id_urn_con_nombre(self):
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:identidad-estable",
            nombre="nombre-runtime"))
        codigo, salida, _ = self.correr(
            ["nombre", "urn:kora:artefacto:identidad-estable"])
        self.assertEqual(codigo, 0)
        self.assertIn(
            "path: artefactos/skills/kora/nombre-runtime/SKILL.md", salida)
        self.assertNotIn("artefactos/skills/kora/identidad-estable", salida)

    def test_gestos_rechazan_urn_duplicado_sin_mutar(self):
        urn = "urn:kora:artefacto:util-x"
        primera = self.escribir_skill(skill_campos(nombre="alpha"))
        segunda = self.escribir_skill(skill_campos(nombre="beta"))
        originales = (primera.read_bytes(), segunda.read_bytes())
        gestos = (
            ["nombre", urn],
            ["transmutar", "--urn", urn, "--target", "claude-code",
             "--stdout"],
            ["transmutar", "--paridad", "--urn", urn,
             "--target", "claude-code"],
            ["ciclo", urn, "deprecado"],
        )
        for argv in gestos:
            with self.subTest(argv=argv):
                codigo, _, err = self.correr(argv)
                self.assertEqual(codigo, 1)
                self.assertIn("URN ambiguo", err)
                self.assertIn(primera.relative_to(self.raiz).as_posix(), err)
                self.assertIn(segunda.relative_to(self.raiz).as_posix(), err)
        self.assertEqual(
            (primera.read_bytes(), segunda.read_bytes()), originales)
        self.assertFalse((self.raiz / "_emision").exists())


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

    def test_velar_base_ignora_emision_rancia_y_estricto_la_detecta(self):
        fuente = self.escribir_skill()
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])[0], 0)
        fuente.write_text(
            fuente.read_text(encoding="utf-8") + "\nCambio válido.\n",
            encoding="utf-8",
        )
        self.assertEqual(self.correr(["velar"])[0], 0)
        self.assertNotIn("sello-fresco", kora.velar_todo(self.raiz))
        self.assert_fallo(
            "sello-fresco", "emisión rancia", estricto=True)

    def test_publicacion_no_exige_cantidad_arbitraria_de_tags(self):
        self.escribir_conocimiento(conocimiento_campos(tags=["uno"]))
        self.assertEqual(
            self.fallos("publicacion-digna", estricto=True), [])

    def test_publicacion_exige_procedencia_no_vacia(self):
        self.escribir_conocimiento(conocimiento_campos(fuente='""'))
        self.assert_fallo(
            "publicacion-digna", "'fuente' no vacío", estricto=True)

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
        self.escribir_skill(skill_campos(targets=["codex"]), cuerpo=cuerpo)
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

    def test_nombre_inseguro_falla_antes_de_recrear_directorios(self):
        self.escribir_agente(agente_campos(
            nombre="..", targets=["codex"]))
        self.assert_fallo("forma-valida", "nombre inseguro para una ruta")
        centinela = self.escribir(
            "_emision/codex/NO-BORRAR.md", "producto ajeno al intento\n")
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])
        self.assertEqual(codigo, 1)
        self.assertIn("nombre inseguro para una ruta", err)
        self.assertEqual(centinela.read_text("utf-8"),
                         "producto ajeno al intento\n")
        codigo_paridad, _, err_paridad = self.correr(
            ["transmutar", "--paridad"])
        self.assertEqual(codigo_paridad, 1)
        self.assertIn("paridad no deriva rutas", err_paridad)

    def test_nombre_de_runtime_exige_slug_canonico(self):
        for nombre in ("util x", "Util-X", "util_x", "util\nx", "\x1butil"):
            with self.subTest(nombre=repr(nombre)):
                self.assertFalse(kora._nombre_ruta_seguro(nombre))
        self.assertTrue(kora._nombre_ruta_seguro("util-x2"))


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

    def test_sello_fresco_no_sigue_raiz_emision_symlink(self):
        externo = self.raiz / "externo"
        externo.mkdir()
        (self.raiz / "_emision").symlink_to(externo)
        self.assert_fallo(
            "sello-fresco",
            "emisión es enlace simbólico; no se recorrió",
            estricto=True,
        )

    def test_sello_fresco_no_sigue_symlink_de_emision(self):
        self.escribir_skill()
        externo = self.raiz / "externo/skills"
        (externo / "util-x").mkdir(parents=True)
        (externo / "util-x/SKILL.md").write_text("no leer\n", "utf-8")
        target = self.raiz / "_emision/claude-code"
        target.mkdir(parents=True)
        (target / "skills").symlink_to(externo)
        self.assert_fallo(
            "sello-fresco",
            "emisión contiene enlace simbólico; no se siguió",
            estricto=True,
        )

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
        self.assertEqual(self.fallos("sello-fresco", estricto=True), [],
                         "el sello real (último) está fresco")


class TestCongruenciaGenerador(CasoPneuma):
    """sello-fresco prueba fuente, generador, sidecars y referencias/."""

    def test_rechaza_factor_fuera_de_un_producto_kora(self):
        self.escribir(
            "_emision/hermes/instruccion-sesion.md",
            "puente manual sin sello ni fuente KORA\n",
        )
        self.assert_fallo(
            "sello-fresco",
            "factor no atribuible a un producto KORA",
            estricto=True,
        )

    def test_detecta_cambio_del_generador_sin_cambio_de_fuente(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "claude-code"])[0], 0)
        doctrina_nueva = kora.DOCTRINA_DUAL_MODE + "\n\nCambio del generador."
        with mock.patch.object(kora, "DOCTRINA_DUAL_MODE", doctrina_nueva):
            self.assert_fallo("sello-fresco",
                              "no coincide con el generador vigente",
                              estricto=True)

    def test_detecta_derivado_manipulado_con_hash_valido(self):
        self.escribir_skill()
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])[0], 0)
        emitido = self.raiz / "_emision/claude-code/skills/util-x/SKILL.md"
        emitido.write_text(
            emitido.read_text("utf-8").replace(
                "Texto sintético.", "Texto manipulado.", 1), "utf-8")
        self.assert_fallo("sello-fresco",
                          "no coincide con el generador vigente",
                          estricto=True)

    def test_detecta_sidecar_codex_rancio(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])[0], 0)
        sidecar = self.raiz / (
            "_emision/codex/skills/agente-x/agents/openai.yaml")
        sidecar.write_text("policy:\n  allow_implicit_invocation: true\n",
                           "utf-8")
        self.assert_fallo("sello-fresco",
                          "no coincide con el generador vigente",
                          estricto=True)

    def test_detecta_sidecar_codex_extra(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex"])[0], 0)
        extra = self.raiz / (
            "_emision/codex/skills/agente-x/agents/obsoleto.yaml")
        extra.write_text("policy: {}\n", "utf-8")
        self.assert_fallo(
            "sello-fresco", "factor obsoleto", estricto=True)

    def test_rechaza_emision_de_target_no_declarado(self):
        # hermes ya no está en TARGETS_REALIZADOS como agujero: una emisión
        # falsificada bajo hermes/ ahora se atribuiría a un producto válido,
        # así que la protección que importa es el allowlist de la fuente.
        self.escribir_skill(skill_campos(targets=["claude-code"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])[0], 0)
        origen = self.raiz / (
            "_emision/claude-code/skills/util-x/SKILL.md")
        destino = self.raiz / "_emision/codex/skills/util-x/SKILL.md"
        destino.parent.mkdir(parents=True)
        destino.write_text(
            origen.read_text("utf-8").replace(
                "target: claude-code", "target: codex"), "utf-8")
        self.assert_fallo(
            "sello-fresco", "no declarado por la fuente", estricto=True)

    def test_detecta_referencia_rancia(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        ref = self.escribir(
            "artefactos/skills/kora/util-x/referencias/motor.md", "v1\n")
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex"])[0], 0)
        ref.write_text("v2\n", "utf-8")
        self.assert_fallo("sello-fresco",
                          "fibra referencias/ no coincide",
                          estricto=True)

    def test_retransmutar_retira_referencias_eliminadas(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        ref = self.escribir(
            "artefactos/skills/kora/util-x/referencias/motor.md", "v1\n")
        gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "codex"]
        self.assertEqual(self.correr(gesto)[0], 0)
        destino = self.raiz / "_emision/codex/skills/util-x/referencias"
        self.assertTrue(destino.is_dir())
        ref.unlink()
        ref.parent.rmdir()
        self.assertEqual(self.correr(gesto)[0], 0)
        self.assertFalse(destino.exists())
        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])

    def test_retransmutar_retira_factor_obsoleto_del_producto(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        gesto = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                 "--target", "codex"]
        self.assertEqual(self.correr(gesto)[0], 0)
        extra = self.raiz / (
            "_emision/codex/skills/agente-x/agents/obsoleto.yaml")
        extra.write_text("policy: {}\n", "utf-8")
        self.assert_fallo(
            "sello-fresco", "factor obsoleto", estricto=True)
        self.assertEqual(self.correr(gesto)[0], 0)
        self.assertFalse(extra.exists())
        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])


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

    def test_promocion_exige_corpus_global_verde(self):
        path = self.escribir_skill(skill_campos(estado="borrador"))
        self.escribir_agente(agente_campos(
            urn="urn:dev:artefacto:roto", nombre="roto",
            estado="borrador", vector=[2, 0, 2, 0, 2]))  # phi=2 exige mu>=1
        codigo, _, err = self.correr(
            ["ciclo", "urn:kora:artefacto:util-x", "activo"])
        self.assertEqual(codigo, 1)
        self.assertIn("corpus completo no pasa velar", err)
        self.assertIn("estado: borrador", path.read_text(encoding="utf-8"))

    def test_promocion_no_depende_de_emision_rancia(self):
        fuente = self.escribir_skill()
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])[0], 0)
        fuente.write_text(
            fuente.read_text(encoding="utf-8") + "\nCambio válido.\n",
            encoding="utf-8",
        )
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:util-y",
            nombre="util-y", estado="borrador",
        ))
        codigo, _, err = self.correr([
            "ciclo", "urn:kora:artefacto:util-y", "activo",
        ])
        self.assertEqual(codigo, 0, err)


class TestTransmutacionProyecto(CasoPneuma):
    """ley/3 §7: --proyecto instala a nivel proyecto; modo opencode agente=all."""

    def test_opencode_agente_emite_mode_all(self):
        # forma agente (persona dual-mode) -> mode: all, no primary.
        self.escribir_agente()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/opencode/agents/agente-x.md").read_text("utf-8")
        self.assertIn("mode: all", texto)
        self.assertNotIn("mode: primary", texto)

    def test_opencode_subagente_emite_mode_subagent(self):
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado", vector=[2, 1, 2, 0, 1],
            sigma=[1, 1, 1, 1, 1]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/opencode/agents/agente-x.md").read_text("utf-8")
        self.assertIn("mode: subagent", texto)

    def test_proyecto_instala_agente_en_dot_opencode(self):
        self.escribir_agente()
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0)
        destino = proj / ".opencode/agents/agente-x.md"
        self.assertTrue(destino.is_file())
        self.assertIn("mode: all", destino.read_text("utf-8"))
        self.assertIn(f"aplicado: {destino}", salida)

    def test_proyecto_instala_skill_en_dot_claude(self):
        self.escribir_skill()
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0)
        self.assertTrue((proj / ".claude/skills/util-x/SKILL.md").is_file())

    def test_proyecto_sin_aplicar_es_error(self):
        self.escribir_agente()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--proyecto", str(self.raiz)])
        self.assertEqual(codigo, 1)
        self.assertIn("--proyecto requiere --aplicar", err)

    def test_proyecto_codex_instala_skill_en_dot_agents(self):
        self.escribir_skill(skill_campos(targets=["claude-code", "codex"]))
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "codex", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0, err)
        self.assertTrue((proj / ".agents/skills/util-x/SKILL.md").is_file())

    def test_proyecto_codex_instala_persona_dual(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "codex", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0, err)
        self.assertTrue((proj / ".codex/agents/agente-x.toml").is_file())
        self.assertTrue((proj /
                         ".agents/skills/agente-x/SKILL.md").is_file())

    def test_proyecto_inexistente_es_error(self):
        self.escribir_agente()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar",
             "--proyecto", str(self.raiz / "no-existe")])
        self.assertEqual(codigo, 1)
        self.assertIn("no es un directorio", err)

    def test_opencode_permission_deniega_elevadas_no_concedidas(self):
        # herramientas=[Read, Write] -> deniega bash/webfetch/websearch/task.
        self.escribir_agente()  # default: herramientas=[Read, Write]
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/opencode/agents/agente-x.md").read_text("utf-8")
        self.assertIn("permission:", texto)
        for k in ("bash", "webfetch", "websearch", "task"):
            self.assertIn(f"  {k}: deny", texto)

    def test_opencode_permission_respeta_concedidas(self):
        # Bash y WebFetch concedidas -> NO se deniegan; sí websearch/task.
        self.escribir_agente(agente_campos(
            herramientas=["Read", "Write", "Bash", "WebFetch"]))
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode"])
        self.assertEqual(codigo, 0)
        texto = (self.raiz /
                 "_emision/opencode/agents/agente-x.md").read_text("utf-8")
        self.assertNotIn("bash: deny", texto)
        self.assertNotIn("webfetch: deny", texto)
        self.assertIn("  websearch: deny", texto)
        self.assertIn("  task: deny", texto)

    def test_alcance_invalido_falla_velar(self):
        self.escribir_agente(agente_campos(alcance="global"))
        self.assert_fallo("forma-valida", "alcance inválido")

    def test_alcance_usuario_rechaza_proyecto(self):
        self.escribir_agente(agente_campos(alcance="usuario"))
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 1)
        self.assertIn("alcance 'usuario'", err)

    def test_alcance_proyecto_exige_proyecto(self):
        self.escribir_agente(agente_campos(alcance="proyecto"))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar"])
        self.assertEqual(codigo, 1)
        self.assertIn("alcance 'proyecto'", err)

    def test_alcance_proyecto_con_proyecto_ok(self):
        self.escribir_agente(agente_campos(alcance="proyecto"))
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0)
        self.assertTrue((proj / ".opencode/agents/agente-x.md").is_file())

    def test_alcance_ausente_es_ambos(self):
        # Sin campo alcance: --aplicar user y --proyecto ambos validos.
        self.escribir_agente()
        proj = self.raiz / "proj"
        proj.mkdir()
        codigo, _, _ = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "opencode", "--aplicar", "--proyecto", str(proj)])
        self.assertEqual(codigo, 0)


# ------------------------------------------------------------- paridad (ley/3 §9.1)

class TestParidad(CasoPneuma):
    """ley/3 §9.1: `transmutar --paridad` compara emisión↔instalación
    (nivel usuario) y reporta fiel / desviada / no-instalada."""

    def rutas_tmp(self):
        base = self.raiz / "runtime"
        return {
            ("claude-code", "skill"): str(base / "claude/skills/{nombre}"),
            ("claude-code", "agente"): str(base / "claude/agents/{nombre}.md"),
            ("codex", "skill"): str(base / "agents/skills/{nombre}"),
            ("codex", "agente"): str(base / "codex/agents/{nombre}.toml"),
            ("opencode", "skill"): str(base / "oc/skills/{nombre}"),
            ("opencode", "agente"): str(base / "oc/agents/{nombre}.md"),
            ("openclaw", "skill"): str(base / "claw/skills/{nombre}"),
            ("openclaw", "agente"): str(base / "fleet/blueprints/{nombre}"),
        }

    def con_rutas(self):
        fleet = self.raiz / "runtime/fleet"
        (fleet / "blueprints/agente-x").mkdir(parents=True, exist_ok=True)
        (fleet / "openclaw.json.reference").write_text(json.dumps({
            "agents": {"list": [{"id": "agente-x"}]}
        }), encoding="utf-8")
        return mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True)

    def snapshot_arbol(self, raiz):
        snapshot = {}
        for path in sorted(raiz.rglob("*")):
            rel = path.relative_to(raiz).as_posix()
            if path.is_symlink():
                snapshot[rel] = ("symlink", os.readlink(path))
            elif path.is_dir():
                snapshot[rel] = ("directorio", None)
            else:
                snapshot[rel] = ("archivo", path.read_bytes())
        return snapshot

    def test_fuente_sin_targets_promete_codex_no_emision_historica(self):
        campos = skill_campos()
        del campos["targets"]
        self.escribir_skill(campos)
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
        ])[0], 0)
        with self.con_rutas():
            codigo, salida, error = self.correr([
                "transmutar", "--paridad",
                "--urn", "urn:kora:artefacto:util-x",
                "--target", "codex",
            ])
        self.assertEqual(codigo, 0, error or salida)
        self.assertIn("paridad: no-instalada  codex  util-x", salida)
        self.assertNotIn("emisión histórica", salida)

    def test_fuente_sin_targets_admite_paridad_explicita_de_compatibilidad(self):
        campos = skill_campos()
        del campos["targets"]
        self.escribir_skill(campos)
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])[0], 0)
        with self.con_rutas():
            codigo, salida, error = self.correr([
                "transmutar", "--paridad",
                "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code",
            ])
        self.assertEqual(codigo, 0, error or salida)
        self.assertIn("paridad: no-instalada  claude-code  util-x", salida)
        self.assertNotIn("emisión histórica", salida)

    def test_paridad_focal_hermes_no_falla_por_target(self):
        # hermes es target realizado desde ley/3 v3.0.0: la auditoría focal
        # ya no rechaza el target. Fuente agnóstica sin emisión previa:
        # corrida informativa vacía (nada promete hermes), sin error de
        # realización.
        campos = skill_campos()
        del campos["targets"]
        self.escribir_skill(campos)
        with self.con_rutas():
            codigo, salida, error = self.correr([
                "transmutar", "--paridad", "--target", "hermes",
            ])
        self.assertEqual(codigo, 0, salida or error)
        self.assertIn("sin artefactos activos que verificar", salida)
        self.assertNotIn("no está realizado", error)

    def test_paridad_focal_rechaza_target_fuera_de_allowlist(self):
        self.escribir_skill(skill_campos(targets=["claude-code"]))
        with self.con_rutas():
            codigo, salida, error = self.correr([
                "transmutar", "--paridad",
                "--urn", "urn:kora:artefacto:util-x",
                "--target", "codex",
            ])
        self.assertEqual(codigo, 1, salida or error)
        self.assertIn("no declara el target 'codex'", error)
        self.assertNotIn("sin artefactos activos", salida)

    def test_paridad_proyecto_codex_persona_dual_es_fiel_y_solo_lectura(self):
        urn = "urn:dev:artefacto:agente-x"
        self.escribir_agente(agente_campos(
            targets=["codex"], alcance="proyecto"))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        self.assertEqual(self.correr([
            "transmutar", "--urn", urn, "--target", "codex",
            "--aplicar", "--proyecto", str(proyecto),
        ])[0], 0)
        proyecto_antes = self.snapshot_arbol(proyecto)
        emision_antes = self.snapshot_arbol(self.raiz / "_emision")

        codigo, salida, err = self.correr([
            "transmutar", "--paridad", "--urn", urn,
            "--target", "codex", "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 0, err or salida)
        self.assertEqual(salida.count("paridad: fiel"), 2, salida)
        self.assertIn("codex  agente-x", salida)
        self.assertEqual(self.snapshot_arbol(proyecto), proyecto_antes)
        self.assertEqual(
            self.snapshot_arbol(self.raiz / "_emision"), emision_antes)

    def test_paridad_proyecto_drift_bloquea(self):
        urn = "urn:kora:artefacto:util-x"
        self.escribir_skill(skill_campos(
            targets=["codex"], alcance="proyecto"))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        self.assertEqual(self.correr([
            "transmutar", "--urn", urn, "--target", "codex",
            "--aplicar", "--proyecto", str(proyecto),
        ])[0], 0)
        instalada = proyecto / ".agents/skills/util-x/SKILL.md"
        instalada.write_text(
            instalada.read_text("utf-8") + "\nDRIFT\n", "utf-8")

        codigo, salida, _ = self.correr([
            "transmutar", "--paridad", "--urn", urn,
            "--target", "codex", "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 1, salida)
        self.assertIn("paridad: desviada", salida)
        self.assertIn("difiere SKILL.md", salida)

    def test_paridad_proyecto_path_inexistente_falla(self):
        self.escribir_skill(skill_campos(targets=["codex"]))
        inexistente = self.raiz / "no-existe"

        codigo, _, err = self.correr([
            "transmutar", "--paridad", "--target", "codex",
            "--proyecto", str(inexistente),
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("no es un directorio", err)
        self.assertFalse(inexistente.exists())

    def test_paridad_proyecto_target_sin_layout_falla(self):
        self.escribir_skill(skill_campos(targets=["openclaw"]))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()

        codigo, _, err = self.correr([
            "transmutar", "--paridad", "--target", "openclaw",
            "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("no soporta instalacion a nivel proyecto", err)

    def test_paridad_usuario_omite_unidad_solo_proyecto(self):
        urn = "urn:kora:artefacto:util-x"
        self.escribir_skill(skill_campos(
            targets=["codex"], alcance="proyecto"))
        self.assertEqual(self.correr([
            "transmutar", "--urn", urn, "--target", "codex",
        ])[0], 0)

        codigo, salida, err = self.correr([
            "transmutar", "--paridad", "--target", "codex",
        ])

        self.assertEqual(codigo, 0, err or salida)
        self.assertNotIn("util-x", salida)
        self.assertNotIn("paridad: no-instalada", salida)

    def test_paridad_focal_rechaza_alcance_incompatible(self):
        urn = "urn:kora:artefacto:util-x"
        self.escribir_skill(skill_campos(
            targets=["codex"], alcance="usuario"))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()

        codigo, _, err = self.correr([
            "transmutar", "--paridad", "--urn", urn,
            "--target", "codex", "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 1)
        self.assertIn("alcance 'usuario'", err)

    def test_paridad_proyecto_detecta_residual_de_alcance_usuario(self):
        urn = "urn:kora:artefacto:util-x"
        fuente = self.escribir_skill(skill_campos(
            targets=["codex"], alcance="ambos"))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        self.assertEqual(self.correr([
            "transmutar", "--urn", urn, "--target", "codex",
            "--aplicar", "--proyecto", str(proyecto),
        ])[0], 0)
        fuente.write_text(doc(skill_campos(
            targets=["codex"], alcance="usuario")), "utf-8")

        codigo, salida, err = self.correr([
            "transmutar", "--paridad", "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 1, err or salida)
        self.assertIn(
            "paridad: desviada      codex  util-x :: "
            "instalación residual de unidad no vigente", salida)
        self.assertNotIn("paridad: no-instalada", salida)

    def test_paridad_usuario_detecta_residual_de_alcance_proyecto(self):
        urn = "urn:kora:artefacto:util-x"
        fuente = self.escribir_skill(skill_campos(
            targets=["codex"], alcance="ambos"))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", urn, "--target", "codex",
                "--aplicar",
            ])[0], 0)
            fuente.write_text(doc(skill_campos(
                targets=["codex"], alcance="proyecto")), "utf-8")

            codigo, salida, err = self.correr([
                "transmutar", "--paridad",
            ])

        self.assertEqual(codigo, 1, err or salida)
        self.assertIn(
            "paridad: desviada      codex  util-x :: "
            "instalación residual de unidad no vigente", salida)
        self.assertNotIn("paridad: no-instalada", salida)

    def test_paridad_proyecto_barre_target_completo(self):
        urn_skill = "urn:kora:artefacto:util-x"
        urn_agente = "urn:dev:artefacto:agente-x"
        self.escribir_skill(skill_campos(
            targets=["codex"], alcance="ambos"))
        self.escribir_agente(agente_campos(
            targets=["codex"], alcance="proyecto"))
        self.escribir_skill(skill_campos(
            urn="urn:kora:artefacto:solo-openclaw",
            nombre="solo-openclaw", targets=["openclaw"], alcance="ambos"))
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        for urn in (urn_skill, urn_agente):
            self.assertEqual(self.correr([
                "transmutar", "--urn", urn, "--target", "codex",
                "--aplicar", "--proyecto", str(proyecto),
            ])[0], 0)

        codigo, salida, err = self.correr([
            "transmutar", "--paridad", "--proyecto", str(proyecto),
        ])

        self.assertEqual(codigo, 0, err or salida)
        self.assertEqual(salida.count("paridad: fiel"), 3, salida)
        self.assertNotIn("solo-openclaw", salida)

    def test_recorrido_cotidiano_focal_es_fiel(self):
        urn = "urn:kora:artefacto:util-x"
        target = "claude-code"
        self.escribir_skill()
        with self.con_rutas():
            codigo, salida, err = self.correr(["velar"])
            self.assertEqual(codigo, 0, err or salida)
            codigo, _, err = self.correr([
                "transmutar", "--urn", urn, "--target", target,
                "--aplicar",
            ])
            self.assertEqual(codigo, 0, err)
            codigo, salida, err = self.correr([
                "transmutar", "--paridad", "--urn", urn,
                "--target", target,
            ])
        self.assertEqual(codigo, 0, err or salida)
        self.assertIn("paridad: fiel", salida)
        self.assertTrue(
            (self.raiz / "runtime/claude/skills/util-x/SKILL.md").is_file())

    def test_urn_de_conocimiento_no_audita_homonimo_agentico(self):
        nombre = "colision-x"
        urn_conocimiento = "urn:kora:kb:colision-x"
        urn_skill = "urn:kora:artefacto:colision-x"
        self.escribir_conocimiento(conocimiento_campos(
            urn=urn_conocimiento, nombre=nombre))
        self.escribir_skill(skill_campos(
            urn=urn_skill, nombre=nombre, targets=["claude-code"]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", urn_skill,
            "--target", "claude-code",
        ])[0], 0)

        codigo, salida, err = self.correr([
            "transmutar", "--paridad", "--urn", urn_conocimiento,
            "--target", "claude-code",
        ])

        self.assertEqual(codigo, 1)
        self.assertEqual(salida, "")
        self.assertIn("el conocimiento no se transmuta", err)

    def test_paridad_focal_ignora_emision_homonima_de_otro_urn(self):
        nombre = "colision-x"
        urn_agente = "urn:dev:artefacto:colision-agent"
        urn_skill = "urn:kora:artefacto:colision-skill"
        self.escribir_agente(agente_campos(
            urn=urn_agente, nombre=nombre, targets=["claude-code"]))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", urn_agente,
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            self.escribir_skill(skill_campos(
                urn=urn_skill, nombre=nombre, targets=["claude-code"]))

            codigo, salida, err = self.correr([
                "transmutar", "--paridad", "--urn", urn_skill,
                "--target", "claude-code",
            ])

        self.assertEqual(codigo, 1, err or salida)
        self.assertIn(
            "sin-emision    claude-code  colision-x (skill)", salida)
        self.assertNotIn("emisión histórica", salida)

    def test_paridad_desviada_exit_1(self):
        self.escribir_skill()
        with self.con_rutas():
            self.correr(["transmutar", "--urn", "urn:kora:artefacto:util-x",
                         "--target", "claude-code", "--aplicar"])
            instalado = (self.raiz / "runtime/claude/skills/util-x/SKILL.md")
            instalado.write_text(
                instalado.read_text("utf-8") + "\nEDITADO A MANO\n", "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("desviada", salida)
        self.assertIn("SKILL.md", salida)

    def test_paridad_detecta_factor_extra_en_skill(self):
        self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            extra = self.raiz / (
                "runtime/claude/skills/util-x/recursos/obsoleto.md")
            extra.parent.mkdir()
            extra.write_text("residuo\n", "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sobra recursos/obsoleto.md", salida)

    def test_reaplicar_skill_retira_factor_extra(self):
        self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            extra = self.raiz / (
                "runtime/claude/skills/util-x/recursos/obsoleto.md")
            extra.parent.mkdir()
            extra.write_text("residuo\n", "utf-8")
            self.assertEqual(self.correr(gesto)[0], 0)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertFalse(extra.exists())
        self.assertEqual(codigo, 0, salida)

    def test_paridad_no_lee_bytes_de_factor_sobrante(self):
        self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            extra = self.raiz / (
                "runtime/claude/skills/util-x/recursos/ilegible.md")
            extra.parent.mkdir()
            extra.write_text("residuo\n", "utf-8")
            read_bytes = Path.read_bytes

            def leer(path):
                if path == extra:
                    raise AssertionError("paridad no debe leer factores sobrantes")
                return read_bytes(path)

            with mock.patch.object(Path, "read_bytes", leer):
                codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sobra recursos/ilegible.md", salida)

    def test_paridad_detecta_symlink_en_factor_esperado(self):
        self.escribir_skill()
        self.escribir(
            "artefactos/skills/kora/util-x/referencias/nota.md",
            "referencia\n")
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            instalado = self.raiz / (
                "runtime/claude/skills/util-x/referencias/nota.md")
            emitido = self.raiz / (
                "_emision/claude-code/skills/util-x/referencias/nota.md")
            instalado.unlink()
            instalado.symlink_to(emitido)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("enlace simbólico referencias/nota.md", salida)

    def test_paridad_detecta_nodo_especial_sobrante(self):
        self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            fifo = self.raiz / "runtime/claude/skills/util-x/canal"
            os.mkfifo(fifo)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("nodo especial canal", salida)

    def test_paridad_no_instalada_es_informativa(self):
        self.escribir_skill()
        with self.con_rutas():
            self.correr(["transmutar", "--urn", "urn:kora:artefacto:util-x",
                         "--target", "claude-code"])
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 0, salida)
        self.assertIn("no-instalada", salida)

    def test_paridad_ruta_con_tipo_incompatible_es_desviada(self):
        self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code",
            ])[0], 0)
            destino = self.raiz / "runtime/claude/skills/util-x"
            destino.parent.mkdir(parents=True)
            destino.write_text("ocupa la ruta de directorio\n", "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("desviada", salida)
        self.assertIn("tipo incompatible", salida)

    def test_paridad_agente_file_based_con_directorio_es_desviada(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "claude-code",
            ])[0], 0)
            destino = self.raiz / "runtime/claude/agents/agente-x.md"
            destino.mkdir(parents=True)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("desviada", salida)
        self.assertIn(
            "tipo incompatible: esperado archivo regular, observado directorio",
            salida)

    def test_aplicar_skill_no_reemplaza_directorio_sin_propiedad(self):
        self.escribir_skill()
        with self.con_rutas():
            destino = self.raiz / "runtime/claude/skills/util-x"
            destino.mkdir(parents=True)
            ajeno = destino / "SKILL.md"
            ajeno.write_text("---\nname: util-x\n---\n\nAjena.\n", "utf-8")
            centinela = destino / "NO-BORRAR.md"
            centinela.write_text("propiedad externa\n", "utf-8")
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])
            codigo_paridad, salida_paridad, _ = self.correr(
                ["transmutar", "--paridad"])
        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertEqual(codigo_paridad, 1, salida_paridad)
        self.assertIn("conflicto de propiedad", salida_paridad)
        self.assertEqual(ajeno.read_text("utf-8"),
                         "---\nname: util-x\n---\n\nAjena.\n")
        self.assertEqual(centinela.read_text("utf-8"),
                         "propiedad externa\n")

    def test_aplicar_companion_codex_no_reemplaza_skill_ajena(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        with self.con_rutas():
            skill = self.raiz / "runtime/agents/skills/agente-x"
            skill.mkdir(parents=True)
            ajeno = skill / "SKILL.md"
            ajeno.write_text("---\nname: agente-x\n---\n\nAjena.\n", "utf-8")
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "codex", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertEqual(ajeno.read_text("utf-8"),
                         "---\nname: agente-x\n---\n\nAjena.\n")
        self.assertFalse(
            (self.raiz / "runtime/codex/agents/agente-x.toml").exists())

    def test_aplicar_agente_file_based_preserva_archivo_ajeno(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        with self.con_rutas():
            destino = self.raiz / "runtime/claude/agents/agente-x.md"
            destino.parent.mkdir(parents=True)
            destino.write_text("agente ajeno\n", "utf-8")
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "claude-code", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertEqual(destino.read_text("utf-8"), "agente ajeno\n")

    def test_aplicar_agente_file_based_no_sigue_symlink(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        externo = self.escribir("externo/agente.md", "no tocar\n")
        with self.con_rutas():
            destino = self.raiz / "runtime/claude/agents/agente-x.md"
            destino.parent.mkdir(parents=True)
            destino.symlink_to(externo)
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "claude-code", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("enlace simbólico", err)
        self.assertTrue(destino.is_symlink())
        self.assertEqual(externo.read_text("utf-8"), "no tocar\n")

    def test_aplicar_agente_file_based_no_sigue_ancestro_symlink(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        externo = self.raiz / "externo/agents"
        externo.mkdir(parents=True)
        with self.con_rutas():
            runtime = self.raiz / "runtime/claude"
            runtime.mkdir(parents=True)
            (runtime / "agents").symlink_to(externo)
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "claude-code", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("jerarquía insegura", err)
        self.assertFalse((externo / "agente-x.md").exists())

    def test_transmutar_no_sigue_ancestro_symlink_en_emision(self):
        self.escribir_skill()
        externo = self.raiz / "externo/skills/util-x"
        externo.mkdir(parents=True)
        centinela = externo / "NO-BORRAR.md"
        centinela.write_text("externo\n", "utf-8")
        target = self.raiz / "_emision/claude-code"
        target.mkdir(parents=True)
        (target / "skills").symlink_to(externo.parent)
        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])
        self.assertEqual(codigo, 1)
        self.assertIn("emisión bloqueada", err)
        self.assertEqual(centinela.read_text("utf-8"), "externo\n")

    def test_transmutar_reemplaza_leaf_symlink_sin_tocar_destino_externo(self):
        self.escribir_agente(agente_campos(targets=["claude-code"]))
        externo = self.escribir("externo/agente.md", "no tocar\n")
        destino = self.raiz / (
            "_emision/claude-code/agents/agente-x.md")
        destino.parent.mkdir(parents=True)
        destino.symlink_to(externo)
        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "claude-code",
        ])
        self.assertEqual(codigo, 0, err)
        self.assertFalse(destino.is_symlink())
        self.assertTrue(destino.is_file())
        self.assertEqual(externo.read_text("utf-8"), "no tocar\n")

    def test_transmutar_preflighta_derivado_codex_a_retirar(self):
        self.escribir_agente(agente_campos(
            targets=["codex"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        externo = self.raiz / "externo/skills/agente-x"
        externo.mkdir(parents=True)
        centinela = externo / "NO-BORRAR.md"
        centinela.write_text("externo\n", "utf-8")
        codex = self.raiz / "_emision/codex"
        codex.mkdir(parents=True)
        (codex / "skills").symlink_to(externo.parent)
        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "codex",
        ])
        self.assertEqual(codigo, 1)
        self.assertIn("emisión bloqueada", err)
        self.assertEqual(centinela.read_text("utf-8"), "externo\n")

    def test_retirar_ruta_gestionada_elimina_nodo_especial(self):
        fifo = self.raiz / "canal"
        os.mkfifo(fifo)
        kora._retirar_ruta_gestionada(fifo)
        self.assertFalse(fifo.exists())

    def test_aplicar_codex_preflight_no_muta_companion_si_agente_es_ajeno(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        externo = self.escribir("externo/agente.toml", "no tocar\n")
        with self.con_rutas():
            agente = self.raiz / "runtime/codex/agents/agente-x.toml"
            agente.parent.mkdir(parents=True)
            agente.symlink_to(externo)
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "codex", "--aplicar",
            ])
        companion = self.raiz / "runtime/agents/skills/agente-x"
        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertEqual(externo.read_text("utf-8"), "no tocar\n")
        self.assertFalse(companion.exists())

    def test_paridad_instalacion_de_fuente_deprecada_es_residual(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            fuente.write_text(doc(skill_campos(estado="deprecado")), "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("residual de unidad no vigente", salida)

    def test_paridad_emision_de_target_ya_no_vigente_es_residual(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            fuente.write_text(
                doc(skill_campos(targets=["opencode"])), "utf-8")
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "opencode",
            ])[0], 0)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("residual de unidad no vigente", salida)
        self.assertIn("no-instalada  opencode", salida)

    def test_paridad_emision_historica_ausente_no_obliga_despliegue(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "claude-code"]
            self.assertEqual(self.correr(gesto)[0], 0)
            fuente.write_text(doc(skill_campos(estado="deprecado")), "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 0, salida)
        self.assertIn("no-instalada", salida)

    def test_paridad_detecta_residual_aunque_falte_emision_derivada(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            fuente.write_text(doc(skill_campos(estado="retirado")), "utf-8")
            shutil.rmtree(self.raiz / "_emision")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("residual de unidad no vigente", salida)

    def test_paridad_detecta_residual_de_forma_anterior_sin_emision(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            shutil.rmtree(fuente.parent)
            self.escribir_agente(agente_campos(
                urn="urn:kora:artefacto:util-x", nombre="util-x",
                targets=["claude-code"], forma="subagente", arnes="delegado",
                vector=[2, 1, 2, 0, 2]))
            shutil.rmtree(self.raiz / "_emision")
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code",
            ])[0], 0)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("residual de unidad no vigente", salida)
        self.assertIn("no-instalada  claude-code  util-x", salida)

    def test_paridad_residuo_no_depende_del_sello_de_emision_historica(self):
        fuente = self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            fuente.write_text(doc(skill_campos(estado="retirado")), "utf-8")
            emitido = self.raiz / (
                "_emision/claude-code/skills/util-x/SKILL.md")
            emitido.write_text(
                emitido.read_text("utf-8").replace(
                    "fuente: urn:kora:artefacto:util-x",
                    "fuente: urn:otra:artefacto:util-x"),
                "utf-8",
            )
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertEqual(
            salida.count("residual de unidad no vigente"), 1, salida)
        self.assertNotIn("(emisión histórica)", salida)

    def test_paridad_sello_incorrecto_no_puede_resultar_fiel(self):
        self.escribir_skill()
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "claude-code", "--aplicar",
            ])[0], 0)
            emitido = self.raiz / (
                "_emision/claude-code/skills/util-x/SKILL.md")
            instalado = self.raiz / (
                "runtime/claude/skills/util-x/SKILL.md")
            adulterado = emitido.read_text("utf-8").replace(
                "fuente: urn:kora:artefacto:util-x",
                "fuente: urn:otra:artefacto:util-x")
            emitido.write_text(adulterado, "utf-8")
            instalado.write_text(adulterado, "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("el sello de emisión no atribuye", salida)
        self.assertNotIn("paridad: fiel", salida)
        self.assertNotIn("paridad: sin-emision", salida)

    def test_paridad_sello_toml_no_string_no_revienta(self):
        self.escribir_agente(agente_campos(
            targets=["codex"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "codex",
            ])[0], 0)
            emitido = self.raiz / "_emision/codex/agents/agente-x.toml"
            emitido.write_text(
                'name = "agente-x"\n'
                'description = "corrupto"\n'
                "developer_instructions = 1\n",
                "utf-8",
            )
            self.assert_fallo(
                "sello-fresco", "emisión TOML inválida", estricto=True)
            codigo, salida, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("el sello de emisión no atribuye", salida)
        self.assertNotIn("paridad: sin-emision", salida)

    def test_paridad_emision_duplicada_da_un_solo_veredicto(self):
        self.escribir_agente(agente_campos(
            targets=["openclaw"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "openclaw",
        ])[0], 0)
        agents = self.raiz / "_emision/openclaw/agents"
        agents.mkdir()
        shutil.copyfile(
            self.raiz / "_emision/openclaw/workspaces/agente-x/AGENTS.md",
            agents / "agente-x.md",
        )
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        fila = "paridad: desviada      openclaw  agente-x"
        self.assertEqual(codigo, 1, salida)
        self.assertEqual(salida.count(fila), 1, salida)
        self.assertIn("emisión ambigua", salida)
        self.assertNotIn("paridad: fiel          openclaw  agente-x", salida)

    def test_paridad_no_sigue_coleccion_de_emision_symlink(self):
        self.escribir_skill()
        externo = self.raiz / "externo/skills"
        (externo / "util-x").mkdir(parents=True)
        (externo / "util-x/SKILL.md").write_text("no leer\n", "utf-8")
        target = self.raiz / "_emision/claude-code"
        target.mkdir(parents=True)
        (target / "skills").symlink_to(externo)
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn(
            "skills/ es enlace simbólico; no se recorrió", salida)
        self.assertIn("sin-emision    claude-code  util-x", salida)

    def test_paridad_no_declara_fiel_a_traves_de_ancestro_symlink(self):
        self.escribir_skill()
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "claude-code",
        ])[0], 0)
        externo = self.raiz / "externo/skills/util-x"
        shutil.copytree(
            self.raiz / "_emision/claude-code/skills/util-x", externo)
        runtime = self.raiz / "runtime/claude"
        runtime.mkdir(parents=True)
        (runtime / "skills").symlink_to(externo.parent)
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("jerarquía insegura", salida)
        self.assertNotIn("paridad: fiel", salida)

    def test_paridad_detecta_artefacto_activo_sin_emision(self):
        self.escribir_skill()
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("sin-emision", salida)
        self.assertIn("util-x", salida)

    def test_paridad_corpus_sin_activos_no_falla(self):
        self.escribir_skill(skill_campos(estado="deprecado"))
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 0, salida)
        self.assertIn("sin artefactos activos", salida)

    def test_paridad_codex_persona_exige_dos_unidades(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        with self.con_rutas():
            self.correr(["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                         "--target", "codex"])
            codigo, salida, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
        self.assertEqual(codigo, 0, salida)
        self.assertEqual(salida.count("no-instalada"), 3)  # 2 filas + resumen
        self.assertIn("0 sin-emision", salida)

    def test_paridad_workspace_openclaw_detecta_soul_desviado(self):
        campos = agente_campos(targets=["openclaw"])
        self.escribir("artefactos/agentes/dev/agente-x.md",
                      doc(campos, cuerpo_persona("Hace X.", "Voz sobria.")))
        with self.con_rutas():
            self.correr(["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                         "--target", "openclaw", "--aplicar"])
            soul = self.raiz / "runtime/fleet/blueprints/agente-x/SOUL.md"
            soul.write_text(soul.read_text("utf-8") + "\nDRIFT\n", "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("desviada", salida)
        self.assertIn("SOUL.md", salida)

    def test_paridad_blueprint_vacio_es_no_instalada(self):
        self.escribir_agente(agente_campos(
            targets=["openclaw"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "openclaw",
        ])[0], 0)
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 0, salida)
        self.assertIn("no-instalada  openclaw  agente-x", salida)
        self.assertNotIn("falta AGENTS.md", salida)

    def test_paridad_detecta_soul_residual_sin_agents_ni_emision(self):
        campos = agente_campos(targets=["openclaw"])
        cuerpo = cuerpo_persona("Hace X.", "Voz sobria.")
        fuente = self.escribir(
            "artefactos/agentes/dev/agente-x.md", doc(campos, cuerpo))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "openclaw", "--aplicar",
            ])[0], 0)
            fuente.write_text(doc(
                agente_campos(targets=["openclaw"], estado="retirado"),
                cuerpo), "utf-8")
            shutil.rmtree(self.raiz / "_emision")
            (self.raiz / (
                "runtime/fleet/blueprints/agente-x/AGENTS.md")).unlink()
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("residual de unidad no vigente", salida)

    def test_paridad_blueprint_openclaw_no_sigue_agents_symlink(self):
        campos = agente_campos(targets=["openclaw"])
        self.escribir("artefactos/agentes/dev/agente-x.md",
                      doc(campos, cuerpo_persona("Hace X.", "Voz sobria.")))
        with self.con_rutas():
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "openclaw", "--aplicar",
            ])[0], 0)
            instalado = self.raiz / (
                "runtime/fleet/blueprints/agente-x/AGENTS.md")
            emitido = self.raiz / (
                "_emision/openclaw/workspaces/agente-x/AGENTS.md")
            instalado.unlink()
            instalado.symlink_to(emitido)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1, salida)
        self.assertIn("enlace simbólico AGENTS.md", salida)

    def test_aplicar_blueprint_openclaw_no_sigue_agents_symlink(self):
        self.escribir_agente(agente_campos(
            targets=["openclaw"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        externo = self.escribir("externo/AGENTS.md", "no tocar\n")
        with self.con_rutas():
            agents = self.raiz / (
                "runtime/fleet/blueprints/agente-x/AGENTS.md")
            agents.symlink_to(externo)
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "openclaw", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("enlace simbólico", err)
        self.assertTrue(agents.is_symlink())
        self.assertEqual(externo.read_text("utf-8"), "no tocar\n")

    def test_workspace_openclaw_bloquea_agente_fuera_de_roster(self):
        self.escribir(
            "artefactos/agentes/dev/agente-x.md",
            doc(agente_campos(targets=["openclaw"]),
                cuerpo_persona("Hace X.", "Voz sobria.")))
        with self.con_rutas():
            reference = self.raiz / "runtime/fleet/openclaw.json.reference"
            reference.write_text(json.dumps({
                "agents": {"list": [{"id": "otro-agente"}]}
            }), encoding="utf-8")
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "openclaw", "--aplicar",
            ])
        blueprint = self.raiz / "runtime/fleet/blueprints/agente-x"
        self.assertEqual(codigo, 1)
        self.assertIn("no pertenece a la roster", err)
        self.assertFalse((blueprint / "AGENTS.md").exists())

    def test_workspace_openclaw_no_crea_blueprint_ausente(self):
        self.escribir(
            "artefactos/agentes/dev/agente-x.md",
            doc(agente_campos(targets=["openclaw"]),
                cuerpo_persona("Hace X.", "Voz sobria.")))
        with self.con_rutas():
            blueprint = self.raiz / "runtime/fleet/blueprints/agente-x"
            blueprint.rmdir()
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "openclaw", "--aplicar",
            ])
        self.assertEqual(codigo, 1)
        self.assertIn("debe preexistir", err)
        self.assertFalse(blueprint.exists())

    def test_blueprint_openclaw_preserva_runtime_y_retira_soul_residual(self):
        self.escribir_agente(agente_campos(
            targets=["openclaw"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                     "--target", "openclaw", "--aplicar"]
            workspace = self.raiz / "runtime/fleet/blueprints/agente-x"
            memoria = workspace / "memory/nota.md"
            memoria.parent.mkdir()
            memoria.write_text("propia del runtime\n", "utf-8")
            soul = workspace / "SOUL.md"
            soul.write_text(
                "<!-- kora:sello\n"
                "fuente: urn:dev:artefacto:agente-x\n"
                "target: openclaw\n"
                "-->\n",
                "utf-8")
            self.assertEqual(self.correr(gesto)[0], 0)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertFalse((workspace / "SOUL.md").exists())
        self.assertEqual(memoria.read_text("utf-8"), "propia del runtime\n")
        self.assertEqual(codigo, 0, salida)

    def test_workspace_openclaw_preserva_soul_ajeno_no_emitido(self):
        self.escribir_agente(agente_campos(
            targets=["openclaw"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                     "--target", "openclaw", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            soul = self.raiz / "runtime/fleet/blueprints/agente-x/SOUL.md"
            soul.write_text("voz local sin sello KORA\n", "utf-8")
            self.assertEqual(self.correr(gesto)[0], 0)
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(soul.read_text("utf-8"), "voz local sin sello KORA\n")
        self.assertEqual(codigo, 0, salida)

    def test_codex_companion_es_exacto_y_reaplicar_lo_reconcilia(self):
        self.escribir_agente(agente_campos(targets=["codex"]))
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                     "--target", "codex", "--aplicar"]
            self.assertEqual(self.correr(gesto)[0], 0)
            extra = self.raiz / (
                "runtime/agents/skills/agente-x/agents/obsoleto.yaml")
            extra.write_text("policy: {}\n", "utf-8")
            codigo_roto, salida_rota, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
            self.assertEqual(self.correr(gesto)[0], 0)
            codigo_fiel, salida_fiel, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
        self.assertEqual(codigo_roto, 1, salida_rota)
        self.assertIn("sobra agents/obsoleto.yaml", salida_rota)
        self.assertFalse(extra.exists())
        self.assertEqual(codigo_fiel, 0, salida_fiel)

    def test_codex_subagente_retira_solo_companion_propio(self):
        self.escribir_agente(agente_campos(
            targets=["codex"], forma="subagente", arnes="delegado",
            vector=[2, 1, 2, 0, 2]))
        with self.con_rutas():
            gesto = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                     "--target", "codex", "--aplicar"]
            self.assertEqual(self.correr(gesto[:-1])[0], 0)
            skill = self.raiz / "runtime/agents/skills/agente-x"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "<!-- kora:sello\n"
                "fuente: urn:dev:artefacto:agente-x\n"
                "target: codex\n"
                "-->\n",
                "utf-8")
            codigo_roto, salida_rota, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
            self.assertEqual(self.correr(gesto)[0], 0)
            self.assertFalse(skill.exists())
            skill.mkdir(parents=True)
            ajeno = skill / "SKILL.md"
            ajeno.write_text("---\nname: agente-x\n---\n\nAjeno.\n", "utf-8")
            self.assertEqual(self.correr(gesto)[0], 0)
            codigo, salida, _ = self.correr(
                ["transmutar", "--paridad", "--target", "codex"])
        self.assertEqual(codigo_roto, 1, salida_rota)
        self.assertIn("sobra skill complementaria gestionada", salida_rota)
        self.assertEqual(ajeno.read_text("utf-8"),
                         "---\nname: agente-x\n---\n\nAjeno.\n")
        self.assertEqual(codigo, 0, salida)

    def test_paridad_filtra_por_target(self):
        self.escribir_skill(skill_campos(targets=["claude-code", "opencode"]))
        with self.con_rutas():
            for t in ("claude-code", "opencode"):
                self.correr(["transmutar", "--urn", "urn:kora:artefacto:util-x",
                             "--target", t, "--aplicar"])
            roto = self.raiz / "runtime/claude/skills/util-x/SKILL.md"
            roto.write_text("pisado\n", "utf-8")
            codigo_oc, _, _ = self.correr(
                ["transmutar", "--paridad", "--target", "opencode"])
            codigo_todo, _, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo_oc, 0)
        self.assertEqual(codigo_todo, 1)

    def test_directorio_skill_sin_archivo_raiz_es_sin_emision(self):
        self.escribir_skill(skill_campos(targets=["claude-code"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "claude-code"])[0], 0)
        (self.raiz /
         "_emision/claude-code/skills/util-x/SKILL.md").unlink()
        with self.con_rutas():
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1)
        self.assertIn("sin-emision    claude-code  util-x (skill)", salida)

    def test_openclaw_no_aplica_bajo_skill_personal_codex(self):
        self.escribir_skill(skill_campos(targets=["openclaw"]))
        sombra = self.raiz / "runtime/agents/skills/util-x/SKILL.md"
        sombra.parent.mkdir(parents=True)
        sombra.write_text("---\nname: util-x\n---\n", "utf-8")
        with self.con_rutas():
            codigo, _, err = self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "openclaw", "--aplicar"])
        self.assertEqual(codigo, 1)
        self.assertIn("sombrea la instalación managed", err)
        self.assertFalse((self.raiz /
                          "runtime/claw/skills/util-x").exists())

    def test_paridad_detecta_managed_sombreada_por_skill_personal(self):
        self.escribir_skill(skill_campos(targets=["openclaw"]))
        with self.con_rutas():
            self.assertEqual(self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "openclaw", "--aplicar"])[0], 0)
            sombra = self.raiz / "runtime/agents/skills/util-x/SKILL.md"
            sombra.parent.mkdir(parents=True)
            sombra.write_text("---\nname: util-x\n---\n", "utf-8")
            codigo, salida, _ = self.correr(["transmutar", "--paridad"])
        self.assertEqual(codigo, 1)
        self.assertIn("sombreada globalmente", salida)

    def test_paridad_excluye_aplicar(self):
        self.escribir_skill()
        codigo, _, err = self.correr(
            ["transmutar", "--paridad", "--aplicar"])
        self.assertEqual(codigo, 1)
        self.assertIn("--paridad", err)


# ------------------------------------------------- hermes: T-hermes-pneuma-v1
# (ley/3 v3.0.0, 2026-08-23: target realizado para forma habilidad)

class TestHermes(CasoPneuma):
    """ley/3 §7.5: skills y agentes completos hacia Hermes.

    Una habilidad se materializa como SKILL.md agentskills.io. Una fuente con
    ``forma: agente`` se materializa como profile distribution nativa; la forma
    ``subagente`` sigue fallando cerrada porque un perfil es un agente completo.
    """

    def rutas_tmp(self):
        base = self.raiz / "runtime"
        return {
            ("claude-code", "skill"): str(base / "claude/skills/{nombre}"),
            ("claude-code", "agente"): str(base / "claude/agents/{nombre}.md"),
            ("codex", "skill"): str(base / "agents/skills/{nombre}"),
            ("codex", "agente"): str(base / "codex/agents/{nombre}.toml"),
            ("opencode", "skill"): str(base / "oc/skills/{nombre}"),
            ("opencode", "agente"): str(base / "oc/agents/{nombre}.md"),
            ("openclaw", "skill"): str(base / "claw/skills/{nombre}"),
            ("openclaw", "agente"): str(base / "fleet/blueprints/{nombre}"),
            ("hermes", "skill"): str(base / "hermes/skills/{nombre}"),
            ("hermes", "agente"): str(base / "hermes/profiles/{nombre}"),
        }

    def test_skill_emite_frontmatter_oficial(self):
        self.escribir_skill(skill_campos(targets=["hermes"]))
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 0, salida)
        emitido = self.raiz / "_emision/hermes/skills/util-x/SKILL.md"
        texto = emitido.read_text(encoding="utf-8")
        self.assertIn("name: util-x", texto)
        self.assertIn('description: "Skill sintética de prueba."', texto)
        # Campo oficial opcional del canon Hermes
        self.assertRegex(texto, r"(?m)^version: 1\.0\.0$")

    def test_sello_declara_contrato_v1(self):
        self.escribir_skill(skill_campos(targets=["hermes"]))
        self.correr(["transmutar", "--urn", "urn:kora:artefacto:util-x",
                     "--target", "hermes"])
        texto = (self.raiz /
                 "_emision/hermes/skills/util-x/SKILL.md").read_text(
                     encoding="utf-8")
        self.assertIn("target: hermes", texto)
        self.assertIn("funtor: T-hermes-pneuma-v1", texto)

    def test_herramientas_sin_allowlist_es_perdida_declarada(self):
        self.escribir_skill(skill_campos(targets=["hermes"]))
        codigo, salida, _ = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 0, salida)
        texto = (self.raiz /
                 "_emision/hermes/skills/util-x/SKILL.md").read_text(
                     encoding="utf-8")
        # El frontmatter Hermes no tiene allowlist: nada de allowed-tools.
        self.assertNotIn("allowed-tools:", texto.split("---")[1])
        # La frontera queda registrada como pérdida en el sello.
        self.assertIn("fidelidad-campos: herramientas:partial", texto)
        self.assertIn("sin-allowlist-runtime", texto)

    def test_hermes_agente_emite_profile_distribution_nativa(self):
        self.escribir_agente(agente_campos(targets=["claude-code", "hermes"]))
        codigo, salida, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 0, salida or err)
        perfil = self.raiz / "_emision/hermes/profiles/agente-x"
        manifest = (perfil / "distribution.yaml").read_text(encoding="utf-8")
        soul = (perfil / "SOUL.md").read_text(encoding="utf-8")
        self.assertIn("name: agente-x\n", manifest)
        self.assertIn("version: 1.0.0\n", manifest)
        self.assertIn("distribution_owned:\n  - SOUL.md\n", manifest)
        self.assertIn("# Cuerpo\n\nTexto sintético.", soul)
        self.assertIn("funtor: T-hermes-pneuma-v2", soul)
        self.assertFalse(
            (self.raiz / "_emision/hermes/agents/agente-x.md").exists())

    def test_hermes_depende_empaqueta_skill_y_declara_propiedad_exacta(self):
        dependencia = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["hermes"])
        self.escribir_skill(dependencia, ns="dev")
        self.escribir_agente(agente_campos(
            targets=["hermes"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes",
        ])

        self.assertEqual(codigo, 0, salida or err)
        perfil = self.raiz / "_emision/hermes/profiles/agente-x"
        manifest = (perfil / "distribution.yaml").read_text("utf-8")
        requerida = perfil / "skills/disciplina-x/SKILL.md"
        self.assertTrue(requerida.is_file())
        self.assertIn("  - skills/disciplina-x/\n", manifest)
        self.assertIn(
            "fuente: urn:dev:artefacto:disciplina-x",
            requerida.read_text(encoding="utf-8"))

    def test_hermes_componible_no_empaqueta_candidato(self):
        self.escribir_skill(skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["hermes"]), ns="dev")
        self.escribir_agente(agente_campos(
            targets=["hermes"],
            componible=["urn:dev:artefacto:disciplina-x"]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes",
        ])

        self.assertEqual(codigo, 0, salida or err)
        perfil = self.raiz / "_emision/hermes/profiles/agente-x"
        self.assertFalse((perfil / "skills").exists())
        self.assertNotIn(
            "skills/disciplina-x/",
            (perfil / "distribution.yaml").read_text("utf-8"))

    def test_aplicar_hermes_depende_preserva_skills_ajenas_del_perfil(self):
        hermes_root = self.raiz / "hermes-root"
        dependencia = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["hermes"])
        self.escribir_skill(dependencia, ns="dev")
        self.escribir_agente(agente_campos(
            targets=["hermes"],
            depende=["urn:dev:artefacto:disciplina-x"]))
        args = [
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes", "--aplicar",
        ]

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, salida, err = self.correr(args)
            self.assertEqual(codigo, 0, salida or err)
            perfil = hermes_root / "profiles/agente-x"
            ajena = perfil / "skills/operador/SKILL.md"
            ajena.parent.mkdir(parents=True)
            ajena.write_text("---\nname: operador\n---\n", "utf-8")
            codigo, salida, err = self.correr(args)

        self.assertEqual(codigo, 0, salida or err)
        requerida = perfil / "skills/disciplina-x/SKILL.md"
        self.assertTrue(requerida.is_file())
        self.assertIn(
            "fuente: urn:dev:artefacto:disciplina-x",
            requerida.read_text(encoding="utf-8"))
        self.assertEqual(
            ajena.read_text(encoding="utf-8"),
            "---\nname: operador\n---\n")

    def test_aplicar_hermes_no_adquiere_dependencia_anidada_ajena(self):
        hermes_root = self.raiz / "hermes-root"
        dependencia = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["hermes"])
        self.escribir_skill(dependencia, ns="dev")
        fuente_agente = self.escribir_agente(agente_campos(
            targets=["hermes"],
            depende=["urn:dev:artefacto:disciplina-x"]))
        args = [
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes", "--aplicar",
        ]

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            self.assertEqual(self.correr(args)[0], 0)
            perfil = hermes_root / "profiles/agente-x"
            soul_antes = (perfil / "SOUL.md").read_bytes()
            requerida = perfil / "skills/disciplina-x/SKILL.md"
            requerida.write_text(
                "---\nname: disciplina-x\n---\n\n# Ajena\n", "utf-8")
            fuente_agente.write_text(
                fuente_agente.read_text("utf-8") + "\nCambio nuevo.\n",
                "utf-8")
            codigo, _, err = self.correr(args)

        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertIn(str(requerida.parent), err)
        self.assertEqual(
            requerida.read_text("utf-8"),
            "---\nname: disciplina-x\n---\n\n# Ajena\n")
        self.assertEqual((perfil / "SOUL.md").read_bytes(), soul_antes)

    def test_aplicar_codex_depende_instala_skill_requerida_por_su_urn(self):
        base = self.raiz / "runtime"
        dependencia = skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["codex"])
        self.escribir_skill(dependencia, ns="dev")
        self.escribir_agente(agente_campos(
            targets=["codex"],
            depende=["urn:dev:artefacto:disciplina-x"]))

        with mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True):
            codigo, salida, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "codex", "--aplicar",
            ])

        self.assertEqual(codigo, 0, salida or err)
        requerida = base / "agents/skills/disciplina-x/SKILL.md"
        self.assertTrue(requerida.is_file())
        self.assertIn(
            "fuente: urn:dev:artefacto:disciplina-x",
            requerida.read_text(encoding="utf-8"))
        self.assertTrue((base / "codex/agents/agente-x.toml").is_file())

    def test_reemision_perfil_reconcilia_directorio_cerrado(self):
        self.escribir_agente(agente_campos(targets=["hermes"]))
        args = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "hermes"]
        self.assertEqual(self.correr(args)[0], 0)
        perfil = self.raiz / "_emision/hermes/profiles/agente-x"
        (perfil / "factor-obsoleto.txt").write_text(
            "no pertenece a la emisión vigente", encoding="utf-8")

        codigo, salida, err = self.correr(args)

        self.assertEqual(codigo, 0, salida or err)
        self.assertFalse((perfil / "factor-obsoleto.txt").exists())
        self.assertEqual(
            {path.name for path in perfil.iterdir()},
            {"distribution.yaml", "SOUL.md"})

    def test_sello_fresco_reconoce_producto_profile_distribution(self):
        self.escribir_agente(agente_campos(targets=["hermes"]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes"])[0], 0)

        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])

    def test_sello_fresco_reconoce_dependencia_empaquetada_del_perfil(self):
        self.escribir_skill(skill_campos(
            urn="urn:dev:artefacto:disciplina-x",
            nombre="disciplina-x", targets=["hermes"]), ns="dev")
        self.escribir(
            "artefactos/skills/dev/disciplina-x/referencias/guia.md",
            "guia vigente\n")
        self.escribir_agente(agente_campos(
            targets=["hermes"],
            depende=["urn:dev:artefacto:disciplina-x"]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes"])[0], 0)

        self.assertEqual(self.fallos("sello-fresco", estricto=True), [])

    def test_hermes_subagente_falla_cerrado(self):
        self.escribir_agente(agente_campos(
            forma="subagente", arnes="delegado",
            targets=["claude-code", "hermes"]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 1)
        self.assertIn("forma 'subagente'", err)
        self.assertIn("perfil Hermes representa un agente completo", err)

    def test_hermes_agente_rechaza_nombre_reservado_de_perfil(self):
        self.escribir_agente(agente_campos(
            nombre="hermes", targets=["hermes"]))

        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes"])

        self.assertEqual(codigo, 1)
        self.assertIn("nombre de perfil Hermes reservado", err)
        self.assertFalse(
            (self.raiz / "_emision/hermes/profiles/hermes").exists())

    def test_mu3_en_fuente_habilidad_rechazado_por_dominio(self):
        # Dos capas separadas: ley/2 `dominio-forma` rechaza mu=3 declarado
        # en una FUENTE de forma habilidad (permitido {0,1}); el techo mu=3
        # del target hermes es capacidad del RUNTIME (gateway always-on),
        # no alcanzable desde una skill. La matriz lo declara; el dominio
        # de forma manda primero.
        self.escribir_skill(skill_campos(
            targets=["hermes"], vector=[1, 3, 1, 0, 1]))
        codigo, _, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes"])
        self.assertEqual(codigo, 1)
        self.assertIn("dominio-forma", err)
        self.assertIn("mu=3", err)

    def test_mu3_agente_difiere_gateway_al_deploy_del_perfil(self):
        self.escribir_agente(agente_campos(
            targets=["hermes"], vector=[2, 3, 2, 0, 2]))

        codigo, salida, err = self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes"])

        self.assertEqual(codigo, 0, salida or err)
        soul = (self.raiz /
                "_emision/hermes/profiles/agente-x/SOUL.md").read_text(
                    encoding="utf-8")
        self.assertIn("realiza: profile-mu3-conforme", soul)
        self.assertIn(
            "difiere: conducta-always-on (gateway/systemd/config.yaml)",
            soul)

    def test_aplicar_instala_en_ruta_hermes(self):
        base = self.raiz / "runtime"
        with mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True):
            self.escribir_skill(skill_campos(targets=["hermes"]))
            codigo, salida, err = self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "hermes", "--aplicar"])
        self.assertEqual(codigo, 0, salida or err)
        instalado = base / "hermes/skills/util-x/SKILL.md"
        self.assertTrue(instalado.is_file())
        emitido = self.raiz / "_emision/hermes/skills/util-x/SKILL.md"
        self.assertEqual(instalado.read_bytes(), emitido.read_bytes())

    def test_aplicar_honra_hermes_home_del_perfil(self):
        perfil = self.raiz / "perfil-hermes"
        base_default = self.raiz / "runtime/hermes/skills/util-x"
        self.escribir_skill(skill_campos(targets=["hermes"]))
        with mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True), \
                mock.patch.dict(
                    os.environ, {"HERMES_HOME": str(perfil)}, clear=False):
            codigo, salida, err = self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "hermes", "--aplicar"])
        self.assertEqual(codigo, 0, salida or err)
        instalado = perfil / "skills/util-x/SKILL.md"
        self.assertTrue(instalado.is_file())
        self.assertFalse(base_default.exists())
        emitido = self.raiz / "_emision/hermes/skills/util-x/SKILL.md"
        self.assertEqual(instalado.read_bytes(), emitido.read_bytes())

    def test_aplicar_agente_instala_solo_factores_del_perfil(self):
        hermes_root = self.raiz / "hermes-root"
        perfil = hermes_root / "profiles/agente-x"
        self.escribir_agente(agente_campos(targets=["hermes"]))
        args = ["transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "hermes", "--aplicar"]
        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, salida, err = self.correr(args)
            self.assertEqual(codigo, 0, salida or err)
            (perfil / "config.yaml").write_text(
                "model: operator-owned\n", encoding="utf-8")
            memoria = perfil / "memories/MEMORY.md"
            memoria.parent.mkdir()
            memoria.write_text("continuidad", encoding="utf-8")
            codigo, salida, err = self.correr(args)

        self.assertEqual(codigo, 0, salida or err)
        emitido = self.raiz / "_emision/hermes/profiles/agente-x"
        self.assertEqual(
            (perfil / "SOUL.md").read_bytes(),
            (emitido / "SOUL.md").read_bytes())
        self.assertEqual(
            (perfil / "distribution.yaml").read_bytes(),
            (emitido / "distribution.yaml").read_bytes())
        self.assertEqual(
            (perfil / "config.yaml").read_text(encoding="utf-8"),
            "model: operator-owned\n")
        self.assertEqual(memoria.read_text(encoding="utf-8"), "continuidad")

    def test_aplicar_agente_no_adquiere_perfil_hermes_ajeno(self):
        hermes_root = self.raiz / "hermes-root"
        perfil = hermes_root / "profiles/agente-x"
        perfil.mkdir(parents=True)
        soul = perfil / "SOUL.md"
        soul.write_text("identidad del operador\n", encoding="utf-8")
        config = perfil / "config.yaml"
        config.write_text("model: operator-owned\n", encoding="utf-8")
        self.escribir_agente(agente_campos(targets=["hermes"]))

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "hermes", "--aplicar"])

        self.assertEqual(codigo, 1)
        self.assertIn("conflicto de propiedad", err)
        self.assertIn("perfil Hermes", err)
        self.assertEqual(soul.read_text(encoding="utf-8"),
                         "identidad del operador\n")
        self.assertEqual(config.read_text(encoding="utf-8"),
                         "model: operator-owned\n")
        self.assertFalse((perfil / "distribution.yaml").exists())

    def test_aplicar_instala_hermes_a_nivel_proyecto(self):
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        self.escribir_skill(skill_campos(targets=["hermes"]))
        codigo, salida, err = self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes", "--aplicar", "--proyecto",
             str(proyecto)])
        self.assertEqual(codigo, 0, salida or err)
        instalado = proyecto / ".hermes/skills/util-x/SKILL.md"
        self.assertTrue(instalado.is_file())
        emitido = self.raiz / "_emision/hermes/skills/util-x/SKILL.md"
        self.assertEqual(instalado.read_bytes(), emitido.read_bytes())

    def test_aplicar_skill_bloquea_homonimo_anidado_en_hermes(self):
        hermes_root = self.raiz / "hermes-root"
        anidada = hermes_root / "skills/software-development/util-x/SKILL.md"
        anidada.parent.mkdir(parents=True)
        anidada.write_text(
            "---\nname: util-x\ndescription: ajena\n---\n\n# Ajena\n",
            encoding="utf-8")
        self.escribir_skill(skill_campos(targets=["hermes"]))

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, _, err = self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "hermes", "--aplicar"])

        self.assertEqual(codigo, 1)
        self.assertIn("colisión de discovery Hermes", err)
        self.assertIn(str(anidada), err)
        self.assertFalse(
            (hermes_root / "skills/util-x/SKILL.md").exists())

    def test_aplicar_skill_ignora_homonimo_archivado_en_hermes(self):
        hermes_root = self.raiz / "hermes-root"
        archivada = hermes_root / "skills/.archive/util-x/SKILL.md"
        archivada.parent.mkdir(parents=True)
        archivada.write_text(
            "---\nname: util-x\ndescription: archivo\n---\n",
            encoding="utf-8")
        self.escribir_skill(skill_campos(targets=["hermes"]))

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, salida, err = self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "hermes", "--aplicar"])

        self.assertEqual(codigo, 0, salida or err)
        self.assertTrue(
            (hermes_root / "skills/util-x/SKILL.md").is_file())
        self.assertEqual(
            archivada.read_text(encoding="utf-8"),
            "---\nname: util-x\ndescription: archivo\n---\n")

    def test_aplicar_skill_proyecto_bloquea_homonimo_en_agents(self):
        proyecto = self.raiz / "proyecto"
        ajena = proyecto / ".agents/skills/category/util-x/SKILL.md"
        ajena.parent.mkdir(parents=True)
        ajena.write_text(
            "---\nname: util-x\ndescription: ajena\n---\n",
            encoding="utf-8")
        self.escribir_skill(skill_campos(targets=["hermes"]))

        codigo, _, err = self.correr([
            "transmutar", "--urn", "urn:kora:artefacto:util-x",
            "--target", "hermes", "--aplicar", "--proyecto", str(proyecto)])

        self.assertEqual(codigo, 1)
        self.assertIn("colisión de discovery Hermes", err)
        self.assertIn(str(ajena), err)
        self.assertFalse(
            (proyecto / ".hermes/skills/util-x/SKILL.md").exists())

    def test_paridad_focal_verifica_unidad_hermes(self):
        base = self.raiz / "runtime"
        with mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True):
            self.escribir_skill(skill_campos(targets=["hermes"]))
            self.assertEqual(self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "hermes"])[0], 0)
            # Emitida pero sin instalar: no-instalada (informativo, exit 0).
            codigo, salida, _ = self.correr(
                ["transmutar", "--paridad", "--target", "hermes"])
            self.assertEqual(codigo, 0)
            self.assertIn("no-instalada", salida)
            # Instalada byte-idéntica desde la emisión: fiel.
            import shutil
            shutil.copytree(
                self.raiz / "_emision/hermes/skills/util-x",
                base / "hermes/skills/util-x")
            codigo, salida, _ = self.correr(
                ["transmutar", "--paridad", "--target", "hermes"])
            self.assertEqual(codigo, 0, salida)
            self.assertIn("paridad: fiel          hermes  util-x", salida)

    def test_paridad_honra_hermes_home_del_perfil(self):
        perfil = self.raiz / "perfil-hermes"
        self.escribir_skill(skill_campos(targets=["hermes"]))
        with mock.patch.dict(kora.RUTAS_APLICAR, self.rutas_tmp(), clear=True), \
                mock.patch.dict(
                    os.environ, {"HERMES_HOME": str(perfil)}, clear=False):
            self.assertEqual(self.correr(
                ["transmutar", "--urn", "urn:kora:artefacto:util-x",
                 "--target", "hermes"])[0], 0)
            shutil.copytree(
                self.raiz / "_emision/hermes/skills/util-x",
                perfil / "skills/util-x")
            codigo, salida, err = self.correr(
                ["transmutar", "--paridad", "--target", "hermes"])
        self.assertEqual(codigo, 0, salida or err)
        self.assertIn("paridad: fiel          hermes  util-x", salida)

    def test_paridad_perfil_hermes_gobierna_solo_factores_emitidos(self):
        hermes_root = self.raiz / "hermes-root"
        perfil = hermes_root / "profiles/agente-x"
        self.escribir_agente(agente_campos(targets=["hermes"]))
        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:dev:artefacto:agente-x",
                "--target", "hermes", "--aplicar"])[0], 0)
            (perfil / "config.yaml").write_text(
                "model: operator-owned\n", encoding="utf-8")
            codigo, salida, err = self.correr([
                "transmutar", "--paridad", "--urn",
                "urn:dev:artefacto:agente-x", "--target", "hermes"])
            self.assertEqual(codigo, 0, salida or err)
            self.assertIn(
                "paridad: fiel          hermes  agente-x", salida)

            with (perfil / "SOUL.md").open("a", encoding="utf-8") as fh:
                fh.write("\nderiva local\n")
            codigo, salida, _ = self.correr([
                "transmutar", "--paridad", "--urn",
                "urn:dev:artefacto:agente-x", "--target", "hermes"])

        self.assertEqual(codigo, 1)
        self.assertIn("paridad: desviada      hermes  agente-x", salida)
        self.assertIn("difiere SOUL.md", salida)
        self.assertNotIn("sobra config.yaml", salida)

    def test_paridad_perfil_hermes_ajeno_es_conflicto(self):
        hermes_root = self.raiz / "hermes-root"
        perfil = hermes_root / "profiles/agente-x"
        perfil.mkdir(parents=True)
        (perfil / "SOUL.md").write_text(
            "identidad del operador\n", encoding="utf-8")
        self.escribir_agente(agente_campos(targets=["hermes"]))
        self.assertEqual(self.correr([
            "transmutar", "--urn", "urn:dev:artefacto:agente-x",
            "--target", "hermes"])[0], 0)

        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            codigo, salida, _ = self.correr([
                "transmutar", "--paridad", "--urn",
                "urn:dev:artefacto:agente-x", "--target", "hermes"])

        self.assertEqual(codigo, 1)
        self.assertIn("paridad: desviada      hermes  agente-x", salida)
        self.assertIn("conflicto de propiedad", salida)

    def test_paridad_verifica_hermes_a_nivel_proyecto(self):
        proyecto = self.raiz / "proyecto"
        proyecto.mkdir()
        self.escribir_skill(skill_campos(targets=["hermes"]))
        self.assertEqual(self.correr(
            ["transmutar", "--urn", "urn:kora:artefacto:util-x",
             "--target", "hermes", "--aplicar", "--proyecto",
             str(proyecto)])[0], 0)
        codigo, salida, err = self.correr(
            ["transmutar", "--paridad", "--target", "hermes",
             "--proyecto", str(proyecto)])
        self.assertEqual(codigo, 0, salida or err)
        self.assertIn("paridad: fiel          hermes  util-x", salida)

    def test_paridad_skill_hermes_detecta_homonimo_activo(self):
        hermes_root = self.raiz / "hermes-root"
        self.escribir_skill(skill_campos(targets=["hermes"]))
        with mock.patch.dict(
                os.environ, {"HERMES_HOME": str(hermes_root)}, clear=False):
            self.assertEqual(self.correr([
                "transmutar", "--urn", "urn:kora:artefacto:util-x",
                "--target", "hermes", "--aplicar"])[0], 0)
            anidada = hermes_root / "skills/category/util-x/SKILL.md"
            anidada.parent.mkdir(parents=True)
            anidada.write_text(
                "---\nname: util-x\ndescription: duplicada\n---\n",
                encoding="utf-8")
            codigo, salida, _ = self.correr([
                "transmutar", "--paridad", "--urn",
                "urn:kora:artefacto:util-x", "--target", "hermes"])

        self.assertEqual(codigo, 1)
        self.assertIn("paridad: desviada      hermes  util-x", salida)
        self.assertIn("colisión de discovery Hermes", salida)
        self.assertIn(str(anidada), salida)


if __name__ == "__main__":
    unittest.main()
