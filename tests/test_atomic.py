from pathlib import Path
import tempfile
import unittest

from kora.atomic import exchange, rename_new


class AtomicTraversalTests(unittest.TestCase):
    def test_rename_and_exchange_need_search_not_read_on_ancestors(self):
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary) / "search-only"
            work = parent / "writable"
            work.mkdir(parents=True)
            source, destination, other = (work / name for name in ("source", "destination", "other"))
            source.write_bytes(b"source")
            other.write_bytes(b"other")
            parent.chmod(0o100)
            try:
                try:
                    rename_new(source, destination)
                    exchange(destination, other)
                except PermissionError as error:
                    self.fail(f"Path traversal incorrectly requires ancestor read access: {error}")
                self.assertFalse(source.exists())
                self.assertEqual(destination.read_bytes(), b"other")
                self.assertEqual(other.read_bytes(), b"source")
            finally:
                parent.chmod(0o700)
