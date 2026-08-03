# -*- coding: utf-8 -*-
"""Contrato v3 de perspectivas sintéticas situadas HODOM-HSC para Codex."""
import hashlib
import json
import subprocess
import tomllib
import unittest
from pathlib import Path

import kora


RAIZ = Path(__file__).resolve().parent.parent
ZONA = RAIZ / "artefactos/agentes/salud"
SKILL = (
    RAIZ
    / "artefactos/skills/salud/participacion-usuario-sintetico-hodom-hsc"
    / "SKILL.md"
)
SKILL_URN = "urn:salud:artefacto:participacion-usuario-sintetico-hodom-hsc"
PROFILE_URN = "urn:salud:kb:perfil-dev-personal-full"
SKILL_MAPA_SHA256 = "59ec4814155a8e5613f109f837693f8339485531b6e2a41c5a49a64f1e987f79"
ROLE_SOURCE_MAPA_SHA256 = (
    "bdf70433a767f2f3df466b76177da0773c2196fb560cb54f1dc27e3a208b2bdd"
)
CATALOGO_SHA256 = "d4af558d2dc5bf57db07d21ea81d3435843132873c59bd830ae16bf2a61296c6"
EVALUACION_SHA256 = "0003c3693936bd188bae4dab07653454c6b9c5fb10b9267963222b5a086286db"

ROLES = {
    "hodom-hsc-direccion-tecnica": (
        "direccion-tecnica", ("capacidad", "cartera", "interfaces", "decisor universal")),
    "hodom-hsc-enfermera-coordinadora": (
        "enfermera-coordinadora", ("cola única", "compuertas", "acuse", "autoridad clínica")),
    "hodom-hsc-medico-atencion-directa": (
        "medico-atencion-directa", ("elegibilidad clínica", "plan", "rescate", "presión de camas")),
    "hodom-hsc-medico-regulador": (
        "medico-regulador", ("respuesta real", "handoff", "teléfono", "fallback")),
    "hodom-hsc-enfermero-clinico": (
        "enfermero-clinico", ("plan de cuidados", "dispositivos", "educación", "escalamiento")),
    "hodom-hsc-kinesiologo": (
        "kinesiologo", ("función respiratoria", "función motora", "respuesta", "continuidad")),
    "hodom-hsc-tecnico-enfermeria": (
        "tecnico-enfermeria", ("asignación", "supervisión", "competencia", "administrativa")),
    "hodom-hsc-trabajador-social": (
        "trabajador-social", ("domicilio", "cuidador", "redes", "dotación ausente")),
    "hodom-hsc-fonoaudiologo": (
        "fonoaudiologo", ("deglución", "comunicación", "educación", "handoff")),
    "hodom-hsc-otro-profesional": (
        "otro-profesional", ("cartera", "competencia", "mínimo privilegio", "disciplina")),
    "hodom-hsc-seremi": (
        "seremi", ("fiscalización", "diseño", "operación", "cadena clínica")),
    "hodom-hsc-administrador-seguridad": (
        "administrador-seguridad", ("identidad", "mínimo privilegio", "auditoría", "break-glass")),
    "hodom-hsc-conductor": (
        "conductor", ("ruta", "vehículo", "custodia", "decisiones clínicas")),
    "hodom-hsc-administrativo": (
        "administrativo", ("completitud", "agenda", "elegibilidad", "alta clínica")),
}

CONOCIMIENTO_COMUN = {
    "urn:salud:kb:hodom-reglamento-ds1-2022",
    "urn:salud:kb:hodom-norma-tecnica-2024",
    "urn:salud:kb:hsc-pro-002-hospitalizacion-domiciliaria",
    "urn:salud:kb:hodom-invariante-no-equivale-cerrada",
    "urn:salud:kb:hodom-direccion-tecnica",
    "urn:salud:kb:post-agudo-ltss-transiciones",
}

INHIBIDORES = (
    "ROLE_REVIEW",
    "phi-detected",
    "non-demonstrated-practice",
    "human_decision_required",
    "no mutas",
    "No eres la persona titular",
    "perspectiva regulatoria simulada",
    "usuario sintético ideal",
    "representa el oficio completo",
)

MODE_SCHEMA = {
    "DISCOVER": {
        "candidate": "not-required",
        "context_guard": "none",
        "candidate_binding": "forbidden",
        "payload": "needs,journey_deltas,user_stories",
    },
    "SYNTHESIZE": {
        "candidate": "optional",
        "context_guard": "at-least-one-context-packet",
        "candidate_binding": "forbidden",
        "payload": "requirements,seams,conflicts,decision_owners",
    },
    "REVIEW": {
        "candidate": "required",
        "context_guard": "none",
        "candidate_binding": "required-equals-candidate",
        "payload": (
            "review_state,task_attempts,evaluation_blockers,findings,"
            "acceptance_criteria,verdict"
        ),
    },
    "ACCEPT": {
        "candidate": "required",
        "context_guard": "matching-review-same-role-run-and-binding",
        "candidate_binding": "required-equals-candidate",
        "payload": "verdict,conditions,blocking_items,scope_of_acceptance",
    },
}

ACCEPTANCE_LAW = {
    "PASS": {
        "accept_verdict": "ACCEPTED",
        "conditions": "empty",
        "blocking_items": "empty",
    },
    "PASS_WITH_CHANGES": {
        "accept_verdict": "ACCEPTED_WITH_CONDITIONS",
        "conditions": "non-empty",
        "blocking_items": "empty",
    },
    "FAIL": {
        "accept_verdict": "REJECTED",
        "conditions": "empty",
        "blocking_items": "non-empty",
    },
}

MODE_GUARDS = {
    "DISCOVER": {
        "guard": "valid-I_ROLE",
        "error": "malformed-input",
    },
    "SYNTHESIZE": {
        "guard": "at-least-one-context-packet",
        "error": "missing-context-packets",
    },
    "REVIEW": {
        "guard": "candidate-present",
        "error": "missing-candidate",
    },
    "ACCEPT": {
        "guard": "candidate-and-exactly-one-conclusive-matching-review",
        "error": (
            "missing-candidate-or-revision-mismatch-or-ambiguous-review-or-"
            "inconclusive-review"
        ),
    },
}

TRANSITION_LAWS = {
    "transition_owner": "external-orchestrator",
    "internal_fsm": "forbidden",
    "self_invocation": "forbidden",
    "revision_change": "invalidates-prior-review-and-acceptance",
    "idempotence_basis": "normalized-I_ROLE-plus-context",
    "idempotence_projection": (
        "packet_id,role,mode,candidate_binding,review_state,verdict,conditions,"
        "blocking_items,scope_of_acceptance"
    ),
}

PROVENANCE_VOCABULARY = {
    "N": (
        "norma o doctrina sanitaria del corpus KORA",
        "obligación o criterio general según el corpus al corte",
    ),
    "L": (
        "documento oficial/local HSC",
        "regla o diseño documental local; no prueba ejecución",
    ),
    "O": (
        "hecho operacional o de interfaz observado",
        "acción y resultado visibles al corte; no acredita experiencia humana interna",
    ),
    "D": (
        "diseño objetivo o necesidad derivada",
        "estado deseado que debe ratificarse",
    ),
    "V": (
        "validación propietaria pendiente",
        "no se puede presentar todavía como contrato local",
    ),
}

EXCEPTION_CONTRACTS = {
    "hodom-hsc-trabajador-social": {
        "role": "R08",
        "modes": "DISCOVER,SYNTHESIZE,REVIEW,ACCEPT",
        "guard": "missing-staffing-is-assumption",
        "acceptance_scope": "social-work-design",
    },
    "hodom-hsc-otro-profesional": {
        "role": "R10",
        "discover_guard": "none",
        "other_modes_guard": "authority_packet.discipline-required",
        "error": "discipline-unbound",
    },
    "hodom-hsc-conductor": {
        "role": "R11",
        "acceptance_scope": "logistics",
        "excluded_scope": "clinical-decisions",
        "handoff": "clinical-owner",
    },
    "hodom-hsc-seremi": {
        "role": "R14",
        "acceptance_scope": "regulatory-readiness",
        "excluded_act": "real-administrative-act",
        "handoff": "real-health-authority",
    },
}

EXPECTED_SOURCE_SNAPSHOT_SHA256 = (
    "2c57ddd43c036e75a9041bfe59284aa38258f1f85dcce60b40f7f388a0b98721"
)


def _section(body, heading, level=2):
    marker = f"{'#' * level} {heading}\n"
    start = body.index(marker) + len(marker)
    boundary = f"\n{'#' * level} "
    end = body.find(boundary, start)
    return body[start:] if end == -1 else body[start:end]


def _table(section):
    lines = [line.strip() for line in section.splitlines()
             if line.strip().startswith("|")]
    if len(lines) < 3:
        raise AssertionError("table not found")
    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != len(headers):
            raise AssertionError(f"malformed table row: {line}")
        rows.append(dict(zip(headers, cells)))
    return rows


def _properties(section):
    return {row["property"]: row["value"] for row in _table(section)}


def _source_snapshot_sha256():
    paths = [SKILL]
    paths.extend(sorted(ZONA.glob("hodom-hsc-*.md")))
    digest = hashlib.sha256()
    for path in paths:
        relative = str(path.relative_to(RAIZ)).encode()
        payload = path.read_bytes()
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)
    return digest.hexdigest()


def _accept_reference(law, request, review):
    candidate = request["candidate"]
    binding = review["candidate_binding"]
    if binding != {"id": candidate["id"], "revision": candidate["revision"]}:
        return {"status": "error", "code": "candidate-revision-mismatch"}
    if review["verdict"] == "INCONCLUSIVE":
        return {"status": "error", "code": "inconclusive-review"}

    row = law[review["verdict"]]
    conditions = review["condition_items"] if row["conditions"] == "non-empty" else []
    blocking = (
        review["blocking_items"]
        if row["blocking_items"] == "non-empty"
        else []
    )
    if row["conditions"] == "non-empty" and not conditions:
        return {"status": "error", "code": "malformed-input"}
    if row["blocking_items"] == "non-empty" and not blocking:
        return {"status": "error", "code": "malformed-input"}

    canonical = json.dumps(
        {"request": request, "review": review},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return {
        "status": "complete",
        "packet_id": hashlib.sha256(canonical).hexdigest(),
        "candidate_binding": binding,
        "payload": {
            "verdict": row["accept_verdict"],
            "conditions": conditions,
            "blocking_items": blocking,
            "scope_of_acceptance": request["scope_of_acceptance"],
        },
    }


class TestPanelRolesHodomHscV3(unittest.TestCase):

    def test_catalogo_cerrado_de_catorce_subagentes(self):
        self.assertEqual(len(ROLES), 14)
        presentes = {path.stem for path in ZONA.glob("hodom-hsc-*.md")}
        self.assertEqual(presentes, set(ROLES))
        self.assertNotIn("hodom-hsc-superusuario-dev", presentes)

    def test_skill_es_ssot_metodologica_sin_persona(self):
        self.assertTrue(SKILL.is_file())
        campos, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        self.assertEqual(campos["urn"], SKILL_URN)
        self.assertEqual(campos["nombre"],
                         "participacion-usuario-sintetico-hodom-hsc")
        self.assertEqual(campos["version"], "2.0.1")
        self.assertIn(PROFILE_URN, campos["conocimiento"])
        self.assertEqual(campos["estado"], "activo")
        self.assertEqual(campos["forma"], "habilidad")
        self.assertEqual(campos["arnes"], "disciplina")
        self.assertEqual(campos["vector"], [2, 0, 2, 0, 1])
        self.assertEqual(campos["sigma"], [3, 3, 3, 3, 2])
        self.assertEqual(campos["herramientas"], ["Bash"])
        self.assertEqual(campos["targets"], ["codex"])
        self.assertEqual(campos["alcance"], "proyecto")
        self.assertIn(SKILL_MAPA_SHA256, campos["fuente"])
        self.assertIn(SKILL_MAPA_SHA256, cuerpo)
        self.assertNotIn("estados", campos)
        self.assertNotIn("<!-- kora:soul -->", cuerpo)

        for testigo in (
                "DISCOVER | SYNTHESIZE | REVIEW | ACCEPT",
                "`I_ROLE`", "`ROLE_PACKET`", "`ROLE_ERROR`",
                "`run_id`", "`authority_packet`", "`candidate`",
                "`context_packets`", "`decision_handoffs`",
                "needs:", "journey_deltas:", "user_stories:",
                "requirements:", "seams:", "conflicts:",
                "decision_owners:", "findings:",
                "review_state:", "task_attempts:",
                "evaluation_blockers:",
                "acceptance_criteria:", "conditions:",
                "blocking_items:", "scope_of_acceptance:",
                "status: complete | complete-with-assumptions | partial | blocked",
                "`malformed-input`", "`missing-candidate`",
                "`missing-context-packets`",
                "`candidate-revision-mismatch`",
                "`missing-use-context`",
                "`inconclusive-review`",
                "`scope-outside-profession`",
                "`authority-packet-conflict`",
                "`discipline-unbound`",
                "N/L/O/D/V",
        ):
            self.assertIn(testigo, cuerpo)

    def test_schema_discriminado_por_modo_y_candidate_binding(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        rows = _table(_section(cuerpo, "Esquema discriminado por modo"))
        actual = {
            row["mode"]: {
                "candidate": row["candidate"],
                "context_guard": row["context_guard"],
                "candidate_binding": row["candidate_binding"],
                "payload": row["payload"],
            }
            for row in rows
        }
        self.assertEqual(actual, MODE_SCHEMA)

        packet_fields = {
            row["field"]: (row["type"], row["requirement"])
            for row in _table(_section(cuerpo, "Esquema base ROLE_PACKET"))
        }
        self.assertEqual(
            packet_fields["candidate_binding"],
            ("object{id:string,revision:string}",
             "required-in-REVIEW-and-ACCEPT"),
        )

    def test_ley_review_accept_es_total_y_determinista(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        rows = _table(_section(cuerpo, "Ley determinista REVIEW a ACCEPT"))
        actual = {
            row["review_verdict"]: {
                "accept_verdict": row["accept_verdict"],
                "conditions": row["conditions"],
                "blocking_items": row["blocking_items"],
            }
            for row in rows
        }
        self.assertEqual(actual, ACCEPTANCE_LAW)
        self.assertEqual(set(actual), {"PASS", "PASS_WITH_CHANGES", "FAIL"})

    def test_review_inconcluso_no_puede_convertirse_en_accept(self):
        request = {
            "run_id": "run-setup-blocked",
            "role": "R01",
            "candidate": {"id": "app", "revision": "rev-1"},
            "scope_of_acceptance": "technical-direction",
        }
        review = {
            "candidate_binding": {"id": "app", "revision": "rev-1"},
            "verdict": "INCONCLUSIVE",
            "condition_items": [],
            "blocking_items": [],
        }
        self.assertEqual(
            _accept_reference(ACCEPTANCE_LAW, request, review),
            {"status": "error", "code": "inconclusive-review"},
        )

    def test_guards_de_modo_son_explicitos(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        rows = _table(_section(cuerpo, "Guards de invocación"))
        actual = {
            row["mode"]: {
                "guard": row["guard"],
                "error": row["error"],
            }
            for row in rows
        }
        self.assertEqual(actual, MODE_GUARDS)

    def test_transiciones_externas_idempotencia_e_invalidacion(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        actual = _properties(
            _section(cuerpo, "Transiciones externas e idempotencia"))
        self.assertEqual(actual, TRANSITION_LAWS)

    def test_referencia_accept_es_idempotente_e_invalida_revision_previa(self):
        request = {
            "run_id": "run-1",
            "role": "R08",
            "candidate": {"id": "journey-J2", "revision": "rev-2"},
            "scope_of_acceptance": "social-work-design",
        }
        review = {
            "candidate_binding": {"id": "journey-J2", "revision": "rev-2"},
            "verdict": "PASS_WITH_CHANGES",
            "condition_items": ["documentar receptor social"],
            "blocking_items": [],
        }
        first = _accept_reference(ACCEPTANCE_LAW, request, review)
        second = _accept_reference(ACCEPTANCE_LAW, request, review)
        self.assertEqual(first, second)
        self.assertEqual(
            first["payload"]["verdict"], "ACCEPTED_WITH_CONDITIONS")
        self.assertTrue(first["payload"]["conditions"])
        self.assertEqual(first["payload"]["blocking_items"], [])

        revised_request = {
            **request,
            "candidate": {"id": "journey-J2", "revision": "rev-3"},
        }
        invalidated = _accept_reference(
            ACCEPTANCE_LAW, revised_request, review)
        self.assertEqual(
            invalidated,
            {"status": "error", "code": "candidate-revision-mismatch"},
        )

    def test_vocabulario_de_procedencia_es_autosuficiente(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        rows = _table(_section(cuerpo, "Vocabulario de procedencia"))
        actual = {
            row["label"]: (row["meaning"], row["claim_limit"])
            for row in rows
        }
        self.assertEqual(actual, PROVENANCE_VOCABULARY)

    def test_firma_semver_procedencia_y_composicion_son_homogeneas(self):
        for nombre, (role_type, _) in ROLES.items():
            campos, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            with self.subTest(nombre=nombre):
                self.assertEqual(campos["urn"],
                                 f"urn:salud:artefacto:{nombre}")
                self.assertEqual(campos["nombre"], nombre)
                self.assertEqual(campos["version"], "3.0.0")
                self.assertEqual(campos["estado"], "activo")
                self.assertEqual(campos["forma"], "subagente")
                self.assertEqual(campos["arnes"], "persona")
                self.assertEqual(campos["vector"], [2, 1, 2, 1, 2])
                self.assertEqual(campos["sigma"], [3, 3, 3, 3, 2])
                self.assertEqual(
                    campos["herramientas"], ["Read", "Grep", "Glob", "Bash"])
                self.assertEqual(campos["targets"], ["codex"])
                self.assertEqual(campos["alcance"], "proyecto")
                self.assertNotIn("estados", campos)
                self.assertIn(SKILL_URN, campos["componible"])
                self.assertTrue(
                    CONOCIMIENTO_COMUN.issubset(campos["conocimiento"]))
                self.assertIn(ROLE_SOURCE_MAPA_SHA256, campos["fuente"])
                self.assertIn(CATALOGO_SHA256, campos["fuente"])
                self.assertIn(EVALUACION_SHA256, campos["fuente"])
                self.assertIn(f"`{role_type}`", cuerpo)
                self.assertNotIn("/home/felix", campos["fuente"])
                self.assertNotIn("/home/felix", cuerpo)

    def test_adaptador_activa_skill_y_preserva_supuestos_disenso(self):
        for nombre in ROLES:
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            cuerpo_normalizado = " ".join(cuerpo.split())
            with self.subTest(nombre=nombre):
                for testigo in (
                        "## Adaptador de participación",
                        SKILL_URN,
                        "resolver la URN",
                        "leer su `SKILL.md` completa",
                        "aplicar su método",
                        "DISCOVER", "SYNTHESIZE", "REVIEW", "ACCEPT",
                        "`I_ROLE`", "`ROLE_PACKET`",
                        "`authority_packet`", "`context_packets`",
                        "`use_context`", "`review_setup`",
                        "`assumptions`", "`dissent`",
                        "`decision_handoffs`", "N/L/O/D/V",
                        "persona sintética situada",
                ):
                    self.assertIn(testigo, cuerpo_normalizado)

    def test_review_ui_es_situada_ciega_visual_y_acotada(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        for testigo in (
                "Primera pasada ciega",
                "capturas de pantalla",
                "coordenadas de puntero",
                "teclas físicas",
                "árbol de accesibilidad",
                "selectores CSS",
                "identificadores de test",
                "código de la aplicación",
                "matriz de aceptación",
                "máximo tres tareas críticas",
                "contexto de navegador nuevo",
                "cada viewport",
                "tecnología de asistencia real",
                "NOT_RUN",
        ):
            self.assertIn(testigo, cuerpo)

    def test_bloqueos_de_evaluacion_no_son_defectos_del_producto(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        for testigo in (
                "evaluation-setup | fixture | environment | unknown",
                "E0 | E1",
                "candidate | evaluation-setup | fixture | environment | unknown",
                "Una identidad incorrecta",
                "no determina `FAIL`",
                "P0",
                "daño inmediato, creíble",
                "INCONCLUSIVE",
        ):
            self.assertIn(testigo, cuerpo)

    def test_prediccion_sintetica_no_se_presenta_como_medicion_humana(self):
        _, cuerpo = kora.parsear_archivo(SKILL.read_text("utf-8"))
        for testigo in (
                "hecho_visible",
                "interpretacion_del_rol",
                "prediccion_sintetica",
                "brecha_de_validacion_humana",
                "carga cognitiva",
                "confianza",
                "no son mediciones humanas",
        ):
            self.assertIn(testigo, cuerpo)

    def test_cada_persona_declara_una_situacion_de_uso_observable(self):
        lentes = set()
        for nombre in ROLES:
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            with self.subTest(nombre=nombre):
                seccion = _section(cuerpo, "Situación humana de uso")
                self.assertIn("Primera tarea visible:", seccion)
                self.assertIn("Presión e interrupción:", seccion)
                self.assertIn("Límite de simulación:", seccion)
                lentes.add(" ".join(seccion.split()))
        self.assertEqual(len(lentes), len(ROLES))

    def test_no_quedan_inhibidores(self):
        textos = [SKILL.read_text("utf-8")]
        textos.extend(
            (ZONA / f"{nombre}.md").read_text("utf-8")
            for nombre in ROLES
        )
        for inhibidor in INHIBIDORES:
            for texto in textos:
                self.assertNotIn(inhibidor, texto)

    def test_cada_persona_conserva_voz_competencias_y_antirol(self):
        voces = set()
        for nombre, (_, marcadores) in ROLES.items():
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            voz = cuerpo.split("<!-- kora:soul -->", 1)[1].split(
                "<!-- kora:soul:fin -->", 1)[0]
            voces.add(" ".join(voz.split()))
            cuerpo_minusculas = cuerpo.lower()
            with self.subTest(nombre=nombre):
                self.assertIn("## Oficio encarnado", cuerpo)
                self.assertIn("antirol:", cuerpo_minusculas)
                for marcador in marcadores:
                    self.assertIn(marcador.lower(), cuerpo_minusculas)
        self.assertEqual(len(voces), len(ROLES))

    def test_excepciones_r08_r10_r11_r14_tienen_contrato_estructural(self):
        for nombre, expected in EXCEPTION_CONTRACTS.items():
            _, cuerpo = kora.parsear_archivo(
                (ZONA / f"{nombre}.md").read_text("utf-8"))
            role = expected["role"]
            with self.subTest(nombre=nombre):
                actual = _properties(
                    _section(cuerpo, f"Excepción {role}", level=3))
                self.assertEqual(actual, expected)

    def test_snapshot_de_fuentes_es_estable(self):
        self.assertEqual(
            _source_snapshot_sha256(), EXPECTED_SOURCE_SNAPSHOT_SHA256)

    def test_emision_codex_es_parseable_y_porta_el_contrato(self):
        for nombre in ROLES:
            urn = f"urn:salud:artefacto:{nombre}"
            proceso = subprocess.run(
                ["python3", "kora.py", "transmutar", "--urn", urn,
                 "--target", "codex", "--stdout"],
                cwd=RAIZ, check=True, capture_output=True, text=True)
            datos = tomllib.loads(proceso.stdout)
            self.assertEqual(datos["name"], nombre)
            instrucciones = datos["developer_instructions"]
            self.assertIn(SKILL_URN, instrucciones)
            self.assertIn("DISCOVER", instrucciones)
            self.assertIn("ACCEPT", instrucciones)
            self.assertIn("<!-- kora:sello", instrucciones)

        proceso_skill = subprocess.run(
            ["python3", "kora.py", "transmutar", "--urn", SKILL_URN,
             "--target", "codex", "--stdout"],
            cwd=RAIZ, check=True, capture_output=True, text=True)
        self.assertIn(
            "name: participacion-usuario-sintetico-hodom-hsc",
            proceso_skill.stdout)
        self.assertIn("<!-- kora:sello", proceso_skill.stdout)


if __name__ == "__main__":
    unittest.main()
