import hashlib
import json
from pathlib import Path
import stat
import tempfile
import unittest

import yaml

import kora.authoring as authoring
import kora.product_versions as product_versions
from kora.authoring import alias, admit, create, prepare, review, revise, retire
from kora.catalog import Catalog, KoraError, digest, read_product
from kora.product_versions import at_revision, preserve, residue_digest, source_digest


class ProductLifecycleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-products-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.body = self.root / "body.md"
        self.body.write_text("# Fuente\n\nConservar sus excepciones.\n")

    def product(self, kind="skill", name="reader", *, targets=("codex", "hermes"), requires=()):
        return create(
            self.root, kind, "test", name, f"urn:test:{kind}:{name}",
            f"Usar {name} conservando límites", self.body,
            targets=list(targets), requires=list(requires),
        )

    def test_both_native_contract_failures_keep_candidate_and_diagnostic(self):
        candidate = prepare(
            self.root, "skill", "test", "too-long", "urn:test:skill:too-long",
            "x" * 1025, self.body, targets=["codex", "hermes"], candidate="failed",
        )
        report = review(self.root, candidate.id, candidate="failed")

        self.assertFalse(report["realizable"])
        self.assertEqual(report["realizable_targets"], {"codex": False, "hermes": False})
        self.assertTrue(all(report["errors"]))
        self.assertTrue(candidate.directory.exists())
        state = json.loads(json.dumps(
            __import__("yaml").safe_load((candidate.directory.parent / "state.yaml").read_text())
        ))
        self.assertEqual(state["status"], "failed")
        self.assertTrue(state["diagnostics"])
        with self.assertRaises(KoraError):
            admit(self.root, candidate.id, report["reviewed_sha256"], candidate="failed")
        self.assertNotIn(candidate.id, Catalog(self.root).products)

    def test_missing_need_is_review_failure_but_candidate_is_recoverable(self):
        candidate = prepare(
            self.root, "skill", "test", "missing", "urn:test:skill:missing",
            "Resolver una necesidad", self.body, targets=["codex", "hermes"],
            requires=["urn:test:skill:not-present"], candidate="missing",
        )
        report = review(self.root, candidate.id, candidate="missing")

        self.assertFalse(report["realizable"])
        self.assertTrue(any("not-present" in error for error in report["errors"]))
        self.assertTrue(candidate.directory.exists())
        self.assertFalse((self.root / "products" / "test" / "missing").exists())

    def test_formally_invalid_candidate_is_preserved_with_stable_diagnostic_path(self):
        with self.assertRaisesRegex(KoraError, r"candidates/test/Invalid Name/formal"):
            prepare(
                self.root, "skill", "test", "Invalid Name", "urn:test:skill:invalid",
                "", self.body, targets=["codex"], candidate="formal",
            )

        candidate_root = self.root / "candidates" / "test" / "Invalid Name" / "formal"
        state = yaml.safe_load((candidate_root / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")
        self.assertTrue(state["diagnostics"])
        self.assertIn(str(candidate_root / "product"), state["errors"][0])
        self.assertEqual(
            (candidate_root / "product/content.md").read_text(), self.body.read_text()
        )

    def test_admission_preserves_fixed_revision_after_a_later_admission(self):
        first = self.product(targets=("codex",))
        first_revision = first.revision
        first_body = first.body
        candidate = revise(self.root, first.id, candidate="second")
        candidate.content_path.write_text("# Segunda fuente\n\nLa excepción sigue vigente.\n")
        report = review(self.root, first.id, candidate="second")
        second = admit(self.root, first.id, report["reviewed_sha256"], candidate="second")

        self.assertEqual(second.revision, source_digest(second))
        self.assertNotEqual(second.revision, first_revision)
        old = at_revision(self.root, second, first_revision)
        self.assertEqual(old.body, first_body)
        self.assertEqual(old.revision, first_revision)
        self.assertTrue((self.root / "versions" / "products" / "test" / "reader" / first_revision).is_dir())

    def test_two_candidates_from_one_base_leave_the_second_stale_and_preserved(self):
        first = self.product(targets=("codex",))
        left = revise(self.root, first.id, candidate="left")
        right = revise(self.root, first.id, candidate="right")
        left.content_path.write_text("left\n")
        right.content_path.write_text("right\n")
        left_review = review(self.root, first.id, candidate="left")
        right_review = review(self.root, first.id, candidate="right")

        admitted = admit(self.root, first.id, left_review["reviewed_sha256"], candidate="left")
        with self.assertRaisesRegex(KoraError, "base|cambió"):
            admit(self.root, first.id, right_review["reviewed_sha256"], candidate="right")

        self.assertEqual(Catalog(self.root).get(first.id).body, admitted.body)
        self.assertTrue(right.directory.exists())
        state = __import__("yaml").safe_load((right.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")
        self.assertIn("base", " ".join(state["errors"]).lower())
        displaced = admitted.directory.parent.parent.parent.parent  # keep path assertion below readable
        self.assertTrue(displaced.exists())

    def test_admission_recovers_after_state_write_fails_post_exchange(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="interrupted")
        candidate.content_path.write_text("interrupted update\n")
        report = review(self.root, first.id, candidate="interrupted")
        original_save = authoring._save_candidate_state

        def fail_final(root, record, changes):
            if changes.get("status") == "admitted":
                raise KoraError("fallo sintético después del intercambio")
            return original_save(root, record, changes)

        authoring._save_candidate_state = fail_final
        try:
            with self.assertRaisesRegex(KoraError, "después del intercambio"):
                admit(self.root, first.id, report["reviewed_sha256"], candidate="interrupted")
        finally:
            authoring._save_candidate_state = original_save

        state_path = candidate.directory.parent / "state.yaml"
        admitting = yaml.safe_load(state_path.read_text())
        self.assertEqual(admitting["status"], "admitting")
        displaced = Path(admitting["displaced_path"])
        self.assertTrue(displaced.is_dir())
        self.assertEqual(Catalog(self.root).get(first.id).body, "interrupted update\n")

        recovered = admit(
            self.root, first.id, report["reviewed_sha256"], candidate="interrupted"
        )
        self.assertEqual(recovered.revision, report["reviewed_sha256"])
        final = yaml.safe_load(state_path.read_text())
        self.assertEqual(final["status"], "admitted")
        self.assertTrue(Path(final["displaced_path"]).is_dir())
        self.assertEqual(
            review(self.root, first.id, candidate="interrupted")["state"], "admitted"
        )

    def test_generated_cache_does_not_block_review_or_admission(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="cache")
        candidate.content_path.write_text("Reviewed update\n")
        for directory in (first.directory, candidate.directory):
            cache = directory / "__pycache__"
            cache.mkdir()
            (cache / "example.pyc").write_bytes(b"generated before review")
        report = review(self.root, first.id, candidate="cache")
        self.assertTrue(report["realizable"], report["errors"])
        for directory in (first.directory, candidate.directory):
            (directory / "__pycache__/example.pyc").write_bytes(b"regenerated after review")
        admitted = admit(self.root, first.id, report["reviewed_sha256"], candidate="cache")
        self.assertEqual(admitted.body, "Reviewed update\n")
        self.assertFalse((admitted.directory / "__pycache__").exists())
        self.assertEqual((candidate.directory / "__pycache__/example.pyc").read_bytes(),
                         b"regenerated after review")

    def legacy_candidate(self, name):
        first = self.product(name=name, targets=("codex",))
        cache = first.directory / "__pycache__"
        cache.mkdir()
        (cache / "example.pyc").write_bytes(b"legacy generated bytes")
        (first.directory / ".env").write_text("TOKEN=synthetic-original\n")
        (first.directory / "notes.tmp").write_text("temporary local work\n")
        # Reproduce the old on-disk aggregate, not the new compatibility helper.
        records = [(relative, mode, data)
                   for relative, mode, data in product_versions._all_regular_files(first.directory)
                   if product_versions._resource_exclusion(relative) is not None]
        legacy_stamp = product_versions._digest_records(
            b"kora-product-residue-v1\0", records, portable=False
        )
        candidate = revise(self.root, first.id, candidate="historical")
        state_path = candidate.directory.parent / "state.yaml"
        state = yaml.safe_load(state_path.read_text())
        state["base_residue"] = legacy_stamp
        state_path.write_text(yaml.safe_dump(state))
        candidate.content_path.write_text("Historical candidate update\n")
        return first, candidate

    def test_historical_candidate_with_unchanged_cache_is_admitted(self):
        first, candidate = self.legacy_candidate("legacy-cache")
        report = review(self.root, first.id, candidate="historical")
        admitted = admit(self.root, first.id, report["reviewed_sha256"], candidate="historical")
        self.assertEqual(admitted.body, "Historical candidate update\n")
        for name in ("__pycache__", ".env", "notes.tmp"):
            self.assertFalse((admitted.directory / name).exists())
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        displaced = Path(state["displaced_path"])
        self.assertEqual((displaced / "__pycache__/example.pyc").read_bytes(), b"legacy generated bytes")
        self.assertEqual((displaced / ".env").read_text(), "TOKEN=synthetic-original\n")
        self.assertEqual((displaced / "notes.tmp").read_text(), "temporary local work\n")

    def test_historical_candidate_still_rejects_changed_sensitive_residue(self):
        for index, (location, relative) in enumerate(
                ((location, relative) for location in ("active", "candidate")
                 for relative in (".env", "notes.tmp"))):
            with self.subTest(location=location, relative=relative):
                first, candidate = self.legacy_candidate("legacy-private-" + str(index))
                report = review(self.root, first.id, candidate="historical")
                directory = first.directory if location == "active" else candidate.directory
                changed = directory / relative
                changed.write_text("late private work\n")
                with self.assertRaisesRegex(KoraError, "operacionales"):
                    admit(self.root, first.id, report["reviewed_sha256"], candidate="historical")
                self.assertEqual(changed.read_text(), "late private work\n")
                self.assertEqual(Catalog(self.root).get(first.id).body, first.body)

    def test_changed_historical_cache_has_conservative_continuation(self):
        first, candidate = self.legacy_candidate("legacy-changed-cache")
        report = review(self.root, first.id, candidate="historical")
        (candidate.directory / "__pycache__/example.pyc").write_bytes(b"new cache")
        with self.assertRaisesRegex(KoraError, "prepara otra candidata"):
            admit(self.root, first.id, report["reviewed_sha256"], candidate="historical")
        # The old aggregate cannot prove which bytes changed. Rebase via the
        # existing candidate flow, explicitly preserving authored work.
        replacement = revise(self.root, first.id, candidate="continued")
        replacement.content_path.write_bytes(candidate.content_path.read_bytes())
        checked = review(self.root, first.id, candidate="continued")
        admitted = admit(self.root, first.id, checked["reviewed_sha256"], candidate="continued")
        self.assertEqual(admitted.body, candidate.body)
        self.assertTrue(candidate.directory.exists())

    def test_admission_rejects_active_residue_changed_since_revise(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="active-residue")
        candidate.content_path.write_text("candidate update\n")
        report = review(self.root, first.id, candidate="active-residue")

        private = first.directory / ".env"
        private.write_text("TOKEN=late\n")
        self.assertEqual(source_digest(first), first.revision)
        self.assertNotEqual(residue_digest(first), report["base_residue"])
        with self.assertRaisesRegex(KoraError, "operacionales"):
            admit(self.root, first.id, report["reviewed_sha256"], candidate="active-residue")

        self.assertEqual(Catalog(self.root).get(first.id).body, first.body)
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")
        self.assertTrue(candidate.directory.exists())
        self.assertEqual(private.read_text(), "TOKEN=late\n")

    def test_admission_rejects_candidate_residue_changed_after_review(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="candidate-residue")
        candidate.content_path.write_text("candidate update\n")
        report = review(self.root, first.id, candidate="candidate-residue")
        private = candidate.directory / ".env"
        private.write_text("TOKEN=edited\n")

        self.assertEqual(source_digest(candidate), report["reviewed_sha256"])
        self.assertEqual(report["state"], "reviewed")
        with self.assertRaisesRegex(KoraError, "operacionales"):
            admit(self.root, first.id, report["reviewed_sha256"], candidate="candidate-residue")

        self.assertEqual(Catalog(self.root).get(first.id).body, first.body)
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")
        self.assertTrue(private.exists())

    def test_admission_rolls_back_when_active_changes_during_exchange(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="active-race")
        candidate.content_path.write_text("candidate update\n")
        report = review(self.root, first.id, candidate="active-race")
        original_exchange = authoring.exchange
        changed = False

        def exchange_with_late_edit(source, destination):
            nonlocal changed
            if not changed:
                changed = True
                (destination / "content.md").write_text("late active edit\n")
            return original_exchange(source, destination)

        authoring.exchange = exchange_with_late_edit
        try:
            with self.assertRaisesRegex(KoraError, "durante el intercambio"):
                admit(self.root, first.id, report["reviewed_sha256"], candidate="active-race")
        finally:
            authoring.exchange = original_exchange

        self.assertEqual(Catalog(self.root).get(first.id).body, "late active edit\n")
        self.assertTrue(candidate.directory.exists())
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")

    def test_admission_keeps_candidate_when_it_changes_while_preserving(self):
        first = self.product(targets=("codex",))
        candidate = revise(self.root, first.id, candidate="candidate-race")
        candidate.content_path.write_text("candidate update\n")
        report = review(self.root, first.id, candidate="candidate-race")
        original_preserve = product_versions.preserve
        changed = {"value": False}

        def preserve_with_late_edit(root, product):
            revision = original_preserve(root, product)
            if (product.directory.absolute() == candidate.directory.absolute()
                    and not changed["value"]):
                changed["value"] = True
                candidate.content_path.write_text("late candidate edit\n")
            return revision

        product_versions.preserve = preserve_with_late_edit
        try:
            with self.assertRaisesRegex(KoraError, "fuente cambió|cambió"):
                admit(self.root, first.id, report["reviewed_sha256"], candidate="candidate-race")
        finally:
            product_versions.preserve = original_preserve

        self.assertEqual(Catalog(self.root).get(first.id).body, first.body)
        self.assertEqual(candidate.content_path.read_text(), "late candidate edit\n")
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")

    def test_admission_rechecks_dependency_context_before_effect(self):
        dependency = self.product(name="dependency", targets=("codex",))
        candidate = prepare(
            self.root, "skill", "test", "dependent", "urn:test:skill:dependent",
            "Usar dependencia activa", self.body, targets=["codex"],
            requires=[dependency.id], candidate="dependency-race",
        )
        report = review(self.root, candidate.id, candidate="dependency-race")
        original_context = authoring._dependency_context
        calls = {"value": 0}

        def context_with_late_edit(root, item, knowledge=None):
            context = original_context(root, item, knowledge=knowledge)
            calls["value"] += 1
            if calls["value"] == 1:
                dependency.content_path.write_text("late dependency edit\n")
            return context

        authoring._dependency_context = context_with_late_edit
        try:
            with self.assertRaisesRegex(KoraError, "dependencias|alias"):
                admit(self.root, candidate.id, report["reviewed_sha256"], candidate="dependency-race")
        finally:
            authoring._dependency_context = original_context

        self.assertEqual(Catalog(self.root).get(dependency.id).body, "late dependency edit\n")
        self.assertFalse((self.root / "products" / "test" / "dependent").exists())
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        self.assertEqual(state["status"], "failed")

    def test_admission_copies_selected_source_and_displaces_residue(self):
        first = self.product(targets=("codex",))
        private = first.directory / ".env"
        private.write_text("TOKEN=keep-with-old\n")
        candidate = revise(self.root, first.id, candidate="selected-source")
        candidate.content_path.write_text("selected candidate\n")
        report = review(self.root, first.id, candidate="selected-source")

        admitted = admit(self.root, first.id, report["reviewed_sha256"], candidate="selected-source")
        self.assertFalse((admitted.directory / ".env").exists())
        state = yaml.safe_load((candidate.directory.parent / "state.yaml").read_text())
        displaced = Path(state["displaced_path"])
        self.assertEqual((displaced / ".env").read_text(), "TOKEN=keep-with-old\n")
        self.assertEqual(admitted.body, "selected candidate\n")

    def test_alias_and_retirement_preserve_snapshot_and_derived_impact(self):
        retired = self.product(name="old", targets=("codex",))
        consumer = self.product(
            name="consumer", targets=("codex",), requires=(retired.id,)
        )
        replacement = self.product(name="new", targets=("codex",))
        alias_id = "urn:previous:skill:old"
        alias(self.root, alias_id, retired.id)
        report = retire(
            self.root, retired.id, "La capacidad fue sustituida", replacement=replacement.id
        )

        self.assertEqual(Catalog(self.root).get(alias_id).id, retired.id)
        self.assertIn(
            {"consumer": consumer.id, "id": consumer.id, "relation": "requires",
             "target": retired.id, "target_id": retired.id, "target_runtime": None},
            report["impact"],
        )
        self.assertTrue(Path(report["archive"]).is_dir())
        self.assertTrue(Path(report["sidecar"]).is_file())
        self.assertTrue(
            (self.root / "versions" / "products" / "test" / "old" / report["revision"]).is_dir()
        )
        archived = Catalog(self.root).get(retired.id)
        self.assertNotIn("reason", archived.metadata)
        self.assertNotIn("replacement", archived.metadata)
        self.assertEqual(__import__("yaml").safe_load(Path(report["sidecar"]).read_text())["reason"],
                         "La capacidad fue sustituida")
        with self.assertRaises(KoraError):
            Catalog(self.root).dependencies(Catalog(self.root).get(consumer.id), "codex")

    def test_source_digest_rejects_links_and_normalizes_non_executable_modes(self):
        product = self.product(targets=("codex",))
        content = product.content_path
        original = source_digest(product)
        content.chmod(0o664)
        self.assertEqual(source_digest(product), original)
        content.chmod(0o755)
        self.assertNotEqual(source_digest(product), original)
        content.chmod(0o644)
        external = self.root / "outside.txt"
        external.write_text("outside")
        link = product.directory / "references"
        link.symlink_to(external)
        with self.assertRaises(KoraError):
            source_digest(product)

    def test_source_digest_ignores_operational_residue_but_preserves_originals(self):
        product = self.product(targets=("codex",))
        original = product.directory / "sources/original.md"
        original.parent.mkdir()
        original.write_text("original\n")
        metadata = yaml.safe_load((product.directory / "object.yaml").read_text())
        metadata["provenance"] = {"sources": [{
            "path": "sources/original.md", "sha256": digest(original.read_bytes())
        }]}
        (product.directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        product = Catalog(self.root).get(product.id)
        before = source_digest(product)
        for relative, data in {
            ".env": b"TOKEN=private\n",
            "__pycache__/compiled.pyc": b"cache-v1",
            "stale.tmp": b"temporary-v1",
        }.items():
            path = product.directory / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.assertEqual(source_digest(product), before)
        (product.directory / ".env").write_bytes(b"TOKEN=changed\n")
        (product.directory / "__pycache__/compiled.pyc").write_bytes(b"cache-v2")
        (product.directory / "stale.tmp").write_bytes(b"temporary-v2")
        self.assertEqual(source_digest(product), before)
        original.write_text("original changed\n")
        self.assertNotEqual(source_digest(product), before)
        revision = preserve(self.root, product)
        snapshot = self.root / "versions/products/test/reader" / revision
        self.assertTrue((snapshot / "sources/original.md").is_file())
        self.assertFalse((snapshot / ".env").exists())
        self.assertFalse((snapshot / "__pycache__").exists())
        self.assertFalse((snapshot / "stale.tmp").exists())

    def test_source_digest_delimits_files_that_old_framing_could_absorb(self):
        metadata = {
            "id": "urn:test:skill:framing",
            "kind": "skill",
            "name": "framing",
            "description": "Comprueba el límite de registros.",
            "content": "content.md",
            "targets": ["codex"],
        }
        one = self.root / "one"
        two = self.root / "two"
        one.mkdir()
        two.mkdir()
        (one / "object.yaml").write_text(yaml.safe_dump(metadata))
        (two / "object.yaml").write_text(yaml.safe_dump(metadata))
        extra_path = "content.md-extra"
        extra_data = b"tail\n"
        extra_header = extra_path.encode() + b"\0" + str(0o644).encode() + b"\0"
        (one / "content.md").write_bytes(b"prefix\n" + extra_header + extra_data)
        (two / "content.md").write_bytes(b"prefix\n")
        (two / extra_path).parent.mkdir(exist_ok=True)
        (two / extra_path).write_bytes(extra_data)
        for directory in (one, two):
            (directory / "object.yaml").chmod(0o644)
            (directory / "content.md").chmod(0o644)
        (two / extra_path).chmod(0o644)
        first = read_product(one)
        second = read_product(two)

        def old_framing(item):
            digest_value = hashlib.sha256()
            entries = []
            for path in item.directory.rglob("*"):
                if path.is_file():
                    entries.append((path.relative_to(item.directory).as_posix(),
                                    stat.S_IMODE(path.stat().st_mode), path.read_bytes()))
            for relative, mode, data in sorted(entries):
                digest_value.update(relative.encode() + b"\0")
                digest_value.update(str(mode).encode() + b"\0")
                digest_value.update(data)
            return digest_value.hexdigest()

        self.assertEqual(old_framing(first), old_framing(second))
        self.assertNotEqual(source_digest(first), source_digest(second))

    def test_review_rejects_a_provenance_hash_even_when_source_snapshot_is_consistent(self):
        source = self.root / "original.md"
        source.write_text("Original conservado.\n")
        candidate = prepare(
            self.root, "skill", "test", "provenance", "urn:test:skill:provenance",
            "Verificar procedencia", self.body, sources=[source], targets=["codex"],
            candidate="provenance",
        )
        metadata_path = candidate.directory / "object.yaml"
        metadata = yaml.safe_load(metadata_path.read_text())
        metadata["provenance"]["sources"][0]["sha256"] = "0" * 64
        metadata_path.write_text(yaml.safe_dump(metadata))

        report = review(self.root, candidate.id, candidate="provenance")
        self.assertFalse(report["realizable"])
        self.assertTrue(any("Original modificado" in error for error in report["errors"]))
        self.assertTrue(candidate.directory.exists())


if __name__ == "__main__":
    unittest.main()
