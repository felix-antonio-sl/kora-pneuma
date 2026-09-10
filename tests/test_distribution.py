import hashlib
import os
import tempfile
import unittest
from pathlib import Path

import yaml

from kora.catalog import Catalog, KoraError, _digest_mode


class DistributionSelectionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kora-distribution-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def product(self, name="witness", kind="skill", **updates):
        directory = self.root / "products" / "test" / name
        directory.mkdir(parents=True)
        metadata = {
            "id": f"urn:test:{kind}:{name}",
            "kind": kind,
            "name": name,
            "description": "Selección de recursos para una realización.",
            "content": "content.md",
            "targets": ["codex", "hermes"] if kind != "knowledge" else [],
        }
        metadata.update(updates)
        (directory / "object.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
        (directory / "content.md").write_text("Cuerpo de prueba.\n", encoding="utf-8")
        return directory

    def item(self, identifier="urn:test:skill:witness"):
        return Catalog(self.root).get(identifier)

    def test_resource_content_cannot_absorb_the_next_file_header(self):
        directory = self.product()
        first = directory / "references/a"
        second = directory / "references/b"
        first.parent.mkdir()
        first.write_bytes(b"A")
        second.write_bytes(b"B")
        mode = _digest_mode("references/b", second.stat().st_mode & 0o7777,
                            portable=True, legacy_modes=None)
        original = self.item().fingerprint()
        first.write_bytes(b"A" + b"references/b\0" + str(mode).encode() + b"\0B")
        second.unlink()
        self.assertNotEqual(original, self.item().fingerprint())

    def test_fallback_keeps_allowed_containers_and_excludes_provenance_original(self):
        directory = self.product(
            provenance={"original_path": "products/test/witness/sources/original.md"},
        )
        for relative, data in {
            "referencias/guide.md": b"guide",
            "references/protocol.md": b"protocol",
            "scripts/run.sh": b"#!/bin/sh\nexit 0\n",
            "agents/openai.yaml": b"interface: example\n",
            "sources/operational.bin": bytes(range(8)),
            "sources/original.md": b"preserved provenance only",
        }.items():
            path = directory / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        (directory / "scripts/run.sh").chmod(0o755)

        resources = self.item().resources()

        self.assertEqual(
            set(resources),
            {
                "referencias/guide.md",
                "references/protocol.md",
                "scripts/run.sh",
                "agents/openai.yaml",
                "sources/operational.bin",
            },
        )
        self.assertNotIn("sources/original.md", resources)

    def test_explicit_files_and_directories_are_the_only_selected_resources(self):
        directory = self.product(
            resources=[
                ".env.example", ".env.sample", ".env.template", "assets", "scripts/run.sh",
                "sources/original.md",
            ],
            provenance={"original_path": "sources/original.md"},
        )
        (directory / ".env.example").write_text("TOKEN=fake\n", encoding="utf-8")
        (directory / ".env.sample").write_text("TOKEN=fake\n", encoding="utf-8")
        (directory / ".env.template").write_text("TOKEN=fake\n", encoding="utf-8")
        (directory / "assets/data.bin").parent.mkdir(parents=True)
        (directory / "assets/data.bin").write_bytes(bytes(range(256)))
        (directory / "assets/nested.txt").write_text("nested\n", encoding="utf-8")
        script = directory / "scripts/run.sh"
        script.parent.mkdir()
        script.write_bytes(b"#!/bin/sh\nexit 0\n")
        script.chmod(0o755)
        (directory / "sources/original.md").parent.mkdir(parents=True)
        (directory / "sources/original.md").write_text("original\n", encoding="utf-8")

        resources = self.item().resources()

        self.assertEqual(
            set(resources),
            {
                ".env.example", ".env.sample", ".env.template", "assets/data.bin", "assets/nested.txt",
                "scripts/run.sh", "sources/original.md",
            },
        )
        self.assertEqual(resources[".env.example"].data, b"TOKEN=fake\n")
        self.assertEqual(resources[".env.sample"].data, b"TOKEN=fake\n")
        self.assertEqual(resources[".env.template"].data, b"TOKEN=fake\n")
        self.assertEqual(resources["assets/data.bin"].data, bytes(range(256)))
        self.assertEqual(resources["scripts/run.sh"].mode, 0o755)

    def test_excluded_residue_does_not_change_fingerprint_but_selected_resource_does(self):
        directory = self.product()
        script = directory / "scripts/run.sh"
        script.parent.mkdir()
        script.write_bytes(b"#!/bin/sh\nexit 0\n")
        script.chmod(0o755)
        private = directory / ".env"
        private.write_text("TOKEN=fake\n", encoding="utf-8")
        cache = directory / "scripts/__pycache__/run.cpython-312.pyc"
        cache.parent.mkdir(parents=True)
        cache.write_bytes(b"cache-v1")
        (directory / ".git/config").parent.mkdir(parents=True)
        (directory / ".git/config").write_text("private\n", encoding="utf-8")
        (directory / "stale.tmp").write_text("temporary\n", encoding="utf-8")

        item = self.item()
        before = item.fingerprint()
        private.write_text("TOKEN=changed\n", encoding="utf-8")
        cache.write_bytes(b"cache-v2")
        (directory / ".git/config").write_text("private-changed\n", encoding="utf-8")
        (directory / "stale.tmp").write_text("temporary-changed\n", encoding="utf-8")
        self.assertEqual(item.fingerprint(), before)

        script.write_bytes(b"#!/bin/sh\nexit 1\n")
        self.assertNotEqual(item.fingerprint(), before)

    def test_unknown_auxiliary_requires_explicit_declaration(self):
        directory = self.product()
        (directory / "notes.txt").write_text("outside the policy\n", encoding="utf-8")

        with self.assertRaisesRegex(KoraError, "fuera de la política"):
            self.item().resources()

    def test_provenance_original_is_omitted_even_when_explicit_selection_is_empty(self):
        directory = self.product(
            name="empty",
            resources=[],
            provenance={"sources": [{"path": "sources/original.md", "sha256": "ignored"}]},
        )
        source = directory / "sources/original.md"
        source.parent.mkdir(parents=True)
        source.write_text("provenance only\n", encoding="utf-8")

        self.assertEqual(self.item("urn:test:skill:empty").resources(), {})

    def test_resource_declaration_rejects_escape_and_glob(self):
        for index, resources in enumerate((["../outside.txt"], ["*.txt"])):
            with self.subTest(resources=resources):
                self.product(name=f"candidate-{index}", resources=resources)
                with self.assertRaisesRegex(KoraError, "recurso|Ruta"):
                    Catalog(self.root)

    def test_resource_declaration_rejects_symlink(self):
        directory = self.product(resources=["assets/link.txt"])
        (directory / "assets").mkdir()
        outside = self.root / "outside.txt"
        outside.write_text("outside\n", encoding="utf-8")
        (directory / "assets/link.txt").symlink_to(outside)

        with self.assertRaisesRegex(KoraError, "enla|enlace"):
            Catalog(self.root)

    def test_fallback_rejects_a_symlink_inside_an_allowed_container(self):
        directory = self.product()
        (directory / "scripts").mkdir()
        target = self.root / "outside.sh"
        target.write_text("#!/bin/sh\n", encoding="utf-8")
        (directory / "scripts/run.sh").symlink_to(target)

        with self.assertRaisesRegex(KoraError, "enla|enlace"):
            self.item().resources()

    def test_fallback_rejects_non_regular_entries_without_reading_them(self):
        directory = self.product()
        scripts = directory / "scripts"
        scripts.mkdir()
        fifo = scripts / "input.pipe"
        os.mkfifo(fifo)

        with self.assertRaisesRegex(KoraError, "no regular"):
            self.item().resources()

    def test_knowledge_keeps_legacy_resource_and_fingerprint_algorithm(self):
        directory = self.product(kind="knowledge", name="reference")
        extra = directory / "unclassified.bin"
        extra.write_bytes(bytes(range(4)))
        item = Catalog(self.root).get("urn:test:knowledge:reference")

        self.assertEqual(item.resources()["unclassified.bin"].data, bytes(range(4)))
        expected = hashlib.sha256()
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                relative = path.relative_to(directory).as_posix()
                expected.update(relative.encode() + b"\0")
                expected.update(str(path.stat().st_mode & 0o7777).encode() + b"\0")
                expected.update(path.read_bytes())
        self.assertEqual(item.fingerprint(portable=False), expected.hexdigest())


if __name__ == "__main__":
    unittest.main()
