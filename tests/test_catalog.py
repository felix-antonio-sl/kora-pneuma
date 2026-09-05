import tempfile
import unittest
from pathlib import Path

import yaml

from kora.catalog import Catalog, KoraError


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def product(self, folder="one", **updates):
        directory = self.root / "products" / "test" / folder
        directory.mkdir(parents=True)
        metadata = dict(id="urn:test:skill:one", kind="skill", name="one",
                        description=r"Reconoce \d+ sin perder excepciones.",
                        content="body.md", targets=["codex", "hermes"])
        metadata.update(updates)
        (directory / "object.yaml").write_text(yaml.safe_dump(metadata))
        (directory / "body.md").write_text("# Fuente\n\nConservar si x > 3, salvo y.\n")
        return directory

    def test_resolves_content_and_keeps_auxiliary_bytes_and_mode(self):
        directory = self.product()
        script = directory / "scripts" / "run.py"
        script.parent.mkdir()
        script.write_bytes(b"#!/usr/bin/env python3\nprint('usable')\n")
        script.chmod(0o755)
        item = Catalog(self.root).get("urn:test:skill:one")
        self.assertEqual(item.body, "# Fuente\n\nConservar si x > 3, salvo y.\n")
        self.assertEqual(item.description, r"Reconoce \d+ sin perder excepciones.")
        self.assertEqual(item.resources()["scripts/run.py"].mode, 0o755)
        self.assertEqual(item.resources()["scripts/run.py"].data,
                         b"#!/usr/bin/env python3\nprint('usable')\n")
        self.assertNotIn("object.yaml", item.resources())

    def test_missing_dependency_is_rejected_by_dependency_consumer(self):
        self.product(requires=["urn:test:knowledge:missing"])
        catalog = Catalog(self.root)
        with self.assertRaisesRegex(KoraError, "urn:test:knowledge:missing"):
            catalog.dependencies(catalog.get("urn:test:skill:one"), "codex")

    def test_body_preserves_original_line_endings(self):
        directory = self.product()
        (directory / "body.md").write_bytes(b"First\r\n\r\nSecond\r\n")
        self.assertEqual(Catalog(self.root).get("urn:test:skill:one").body.encode(),
                         b"First\r\n\r\nSecond\r\n")

    def test_duplicate_identity_is_rejected_but_disjoint_native_names_are_valid(self):
        self.product(targets=["codex"])
        self.product("two", id="urn:test:skill:two", targets=["hermes"])
        self.assertEqual(len(Catalog(self.root).products), 2)
        self.product("three")
        with self.assertRaisesRegex(KoraError, "duplicad"):
            Catalog(self.root)

    def test_dependency_cycle_terminates_without_losing_members(self):
        self.product(requires=["urn:test:skill:two"])
        self.product("two", id="urn:test:skill:two", name="two",
                     requires=["urn:test:skill:one"])
        catalog = Catalog(self.root)
        self.assertEqual([p.id for p in catalog.dependencies(catalog.get("urn:test:skill:one"), "hermes")],
                         ["urn:test:skill:two"])

    def test_historical_relation_is_not_turned_into_an_install_dependency(self):
        self.product(relations={"replaces": ["urn:history:retired:one"]})
        catalog = Catalog(self.root)
        self.assertEqual(catalog.dependencies(catalog.get("urn:test:skill:one"), "codex"), [])

    def test_content_cannot_escape_its_product(self):
        self.product(content="../../outside.md")
        (self.root / "products" / "outside.md").write_text("personal")
        with self.assertRaises(KoraError):
            Catalog(self.root)

    def test_duplicate_yaml_keys_are_not_silently_overwritten(self):
        directory = self.product()
        with (directory / "object.yaml").open("a") as stream:
            stream.write("id: urn:test:skill:overwritten\n")
        with self.assertRaises(KoraError):
            Catalog(self.root)

    def test_dependency_must_exist_on_requested_runtime(self):
        self.product(requires=["urn:test:skill:two"])
        self.product("two", id="urn:test:skill:two", name="two", targets=["codex"])
        catalog = Catalog(self.root)
        with self.assertRaisesRegex(KoraError, "hermes"):
            catalog.dependencies(catalog.get("urn:test:skill:one"), "hermes")


if __name__ == "__main__":
    unittest.main()
