from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from kora.catalog import Catalog, KoraError
from kora.authoring import create


class AuthoringTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "new-kora"
        self.root.mkdir()
        self.source = Path(self.temp.name) / "source.csv"
        self.source.write_bytes(b"item,value,exception\r\na,3,unless_b\r\n")
        self.body = Path(self.temp.name) / "knowledge.md"
        self.body.write_text("# Alcance\n\na tiene valor 3, salvo b. Se desconoce la vigencia.\n")

    def test_authored_knowledge_keeps_source_bytes_and_provenance_separate(self):
        item = create(self.root, "knowledge", "test", "condition", "urn:test:kb:condition",
                      "Condición y excepción de la tabla", self.body, sources=[self.source])
        self.assertEqual(item.body, "# Alcance\n\na tiene valor 3, salvo b. Se desconoce la vigencia.\n")
        provenance = item.metadata["provenance"]["sources"][0]
        self.assertEqual((item.directory / provenance["path"]).read_bytes(),
                         b"item,value,exception\r\na,3,unless_b\r\n")
        self.assertEqual(Catalog(self.root).get(item.id).content_path, item.content_path)

    def test_failed_reference_does_not_leave_a_product(self):
        with self.assertRaisesRegex(KoraError, "missing"):
            create(self.root, "skill", "test", "use-condition", "urn:test:skill:use",
                   "Aplicar condición", self.body, targets=["codex", "hermes"],
                   requires=["urn:test:kb:missing"])
        self.assertEqual(Catalog(self.root).products, {})

    def test_repeated_creation_cannot_overwrite_authored_work(self):
        item = create(self.root, "agent", "test", "reader", "urn:test:agent:reader",
                      "Lee condiciones", self.body, targets=["codex"])
        self.body.write_text("replace")
        with self.assertRaises(KoraError):
            create(self.root, "agent", "test", "reader", item.id, "Replace", self.body, targets=["codex"])
        self.assertIn("salvo b", item.body)

    def test_namespace_symlink_does_not_publish_outside_the_catalog(self):
        outside = self.root.parent / "outside"
        outside.mkdir()
        (self.root / "products").mkdir()
        (self.root / "products/test").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(KoraError):
            create(self.root, "agent", "test", "reader", "urn:test:agent:reader",
                   "Read", self.body, targets=["codex"])
        self.assertEqual(list(outside.iterdir()), [])

    def test_concurrent_creation_of_same_identity_cannot_corrupt_catalog(self):
        script = '''
from pathlib import Path
import os,sys,time
import kora.authoring as authoring
from kora.catalog import KoraError
root,body,name=Path(sys.argv[1]),Path(sys.argv[2]),sys.argv[3]
original=authoring.rename_new if hasattr(authoring,"rename_new") else os.rename
def synchronized_publish(source,destination):
    (root.parent/('ready-'+name)).touch()
    deadline=time.monotonic()+1
    while len(list(root.parent.glob('ready-*')))<2 and time.monotonic()<deadline:
        time.sleep(.01)
    original(source,destination)
authoring.rename_new=synchronized_publish
os.rename=synchronized_publish
try:
    authoring.create(root,"agent","test",name,"urn:test:agent:shared","Read",body,targets=["codex"])
except KoraError:
    raise SystemExit(1)
'''
        processes = [subprocess.Popen([sys.executable, "-c", script, str(self.root), str(self.body), name],
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE) for name in ("one", "two")]
        outputs = [process.communicate(timeout=10) for process in processes]
        self.assertEqual(sorted(p.returncode for p in processes), [0, 1], outputs)
        self.assertEqual(len(Catalog(self.root).products), 1)


if __name__ == "__main__":
    unittest.main()
