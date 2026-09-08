import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from kora.catalog import File, KoraError
from kora.install import Installer


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.installer = Installer(self.home)
        self.skill = ".agents/skills/example/SKILL.md"

    def files(self, body=b"version one"):
        return {self.skill: File(body)}

    def test_update_and_retirement_preserve_other_files(self):
        self.installer.apply({"codex:example": self.files()})
        personal = self.home / ".agents/skills/example/notes.txt"
        personal.write_bytes(b"local work")
        self.installer.apply({"codex:example": self.files(b"version two")})
        self.assertEqual((self.home / self.skill).read_bytes(), b"version two")
        self.assertEqual(personal.read_bytes(), b"local work")
        self.installer.apply({}, remove=["codex:example"])
        self.assertFalse((self.home / self.skill).exists())
        self.assertEqual(personal.read_bytes(), b"local work")

    def test_local_edits_abort_update_and_retirement_without_data_loss(self):
        self.installer.apply({"codex:example": self.files()})
        (self.home / self.skill).write_bytes(b"edited locally")
        for bundles, remove in [({"codex:example": self.files(b"new")}, []), ({}, ["codex:example"])]:
            with self.assertRaisesRegex(KoraError, "cambio local"):
                self.installer.apply(bundles, remove=remove)
            self.assertEqual((self.home / self.skill).read_bytes(), b"edited locally")

    def test_an_edited_unrelated_bundle_does_not_block_update_or_retirement(self):
        other = ".agents/skills/unrelated/SKILL.md"
        self.installer.apply({"codex:example": self.files(), "codex:unrelated": {other: File(b"unrelated")}})
        (self.home / other).write_bytes(b"personal edit")
        self.installer.apply({"codex:example": self.files(b"updated")})
        self.installer.apply({}, remove=["codex:example"])
        self.assertEqual((self.home / other).read_bytes(), b"personal edit")
        self.assertEqual(self.installer.status()["changes"], [{"path": other, "state": "modified"}])

    def test_writer_with_open_descriptor_keeps_displaced_inode_recoverable(self):
        # A separate writer opens the live name BEFORE the operation and writes
        # only AFTER it returns. A snapshot or another preflight cannot save it.
        writer_script = '''
import os, sys
with open(sys.argv[1], "r+b", buffering=0) as stream:
    print("opened", flush=True)
    sys.stdin.readline()
    stream.seek(0)
    stream.write(b"late descriptor edit")
    stream.truncate()
    os.fsync(stream.fileno())
'''
        for operation in ("update", "retire", "rollback", "recover"):
            with self.subTest(operation=operation), tempfile.TemporaryDirectory() as directory:
                home = Path(directory)
                installer = Installer(home)
                installer.apply({"codex:example": self.files()})
                if operation in ("rollback", "recover"):
                    if operation == "recover":
                        original = installer._replace

                        def interrupt(source, destination):
                            original(source, destination)
                            raise KeyboardInterrupt()

                        with patch.object(installer, "_replace", side_effect=interrupt):
                            with self.assertRaises(KeyboardInterrupt):
                                installer.apply({"codex:example": self.files(b"version two")})
                    else:
                        installer.apply({"codex:example": self.files(b"version two")})
                path = home / self.skill
                displaced_inode = path.stat().st_ino
                writer = subprocess.Popen([sys.executable, "-c", writer_script, str(path)],
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE, text=True)
                try:
                    self.assertEqual(writer.stdout.readline().strip(), "opened")
                    if operation == "update":
                        installer.apply({"codex:example": self.files(b"version two")})
                    elif operation == "retire":
                        installer.apply({}, remove=["codex:example"])
                    else:
                        getattr(installer, operation)()
                    _, stderr = writer.communicate("continue\n", timeout=10)
                    self.assertEqual(writer.returncode, 0, stderr)
                finally:
                    if writer.poll() is None:
                        writer.kill()
                        writer.communicate()
                if operation == "retire":
                    self.assertFalse(path.exists())
                else:
                    expected = b"version two" if operation == "update" else b"version one"
                    self.assertEqual(path.read_bytes(), expected)
                retained = [p for p in installer.state.rglob("*")
                            if p.is_file() and p.stat().st_ino == displaced_inode]
                self.assertTrue(retained, f"{operation} discarded the writer's inode")
                self.assertTrue(any(p.read_bytes() == b"late descriptor edit" for p in retained))
                reports = installer.status()["preserved_changes"]
                self.assertTrue(any((home / report["backup"]).read_bytes() == b"late descriptor edit"
                                    for report in reports))
                installer.apply({"codex:another": {".agents/skills/another/SKILL.md": File(b"another")}})
                self.assertTrue(any(p.exists() and p.read_bytes() == b"late descriptor edit" for p in retained))

    def test_edit_in_the_last_update_gap_remains_recoverable(self):
        self.installer.apply({"codex:example": self.files()})
        original = self.installer._replace
        edited_inode = (self.home / self.skill).stat().st_ino
        fired = False

        def write_then_replace(source, destination):
            nonlocal fired
            if not fired:
                fired = True
                subprocess.run([sys.executable, "-c",
                                "import pathlib,sys; pathlib.Path(sys.argv[1]).write_bytes(b'concurrent edit')",
                                str(destination)], check=True)
            return original(source, destination)

        with patch.object(self.installer, "_replace", side_effect=write_then_replace):
            try:
                self.installer.apply({"codex:example": self.files(b"version two")})
            except KoraError:
                pass
        retained = [p for p in self.home.rglob("*")
                    if p.is_file() and p.stat().st_ino == edited_inode]
        self.assertTrue(any(p.read_bytes() == b"concurrent edit" for p in retained),
                        "the installer silently discarded a concurrent writer's bytes")

    def test_occupied_foreign_path_is_preserved(self):
        path = self.home / self.skill
        path.parent.mkdir(parents=True)
        path.write_bytes(b"foreign skill")
        with self.assertRaises(KoraError):
            self.installer.apply({"codex:example": self.files()})
        self.assertEqual(path.read_bytes(), b"foreign skill")

    def test_failure_after_first_replace_restores_complete_previous_installation(self):
        other = ".agents/skills/example/reference.txt"
        initial = {self.skill: File(b"old skill"), other: File(b"old reference")}
        self.installer.apply({"codex:example": initial})
        original = self.installer._replace
        calls = 0

        def fail_second(source, destination):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated disk write failure")
            return original(source, destination)

        with patch.object(self.installer, "_replace", side_effect=fail_second):
            with self.assertRaisesRegex(OSError, "disk write"):
                self.installer.apply({"codex:example": {self.skill: File(b"new skill"), other: File(b"new reference")}})
        self.assertEqual((self.home / self.skill).read_bytes(), b"old skill")
        self.assertEqual((self.home / other).read_bytes(), b"old reference")
        self.assertEqual(self.installer.status()["changes"], [])

    def test_shared_dependency_survives_removal_of_one_consumer(self):
        self.installer.apply({"codex:a": self.files(), "codex:b": self.files()})
        self.installer.apply({}, remove=["codex:a"])
        self.assertEqual((self.home / self.skill).read_bytes(), b"version one")
        with self.assertRaisesRegex(KoraError, "compartid"):
            self.installer.apply({"codex:b": self.files(b"different"), "codex:c": self.files()})

    def test_staging_failure_leaves_live_files_and_last_recovery_usable(self):
        self.installer.apply({"codex:example": self.files()})
        from kora.install import _atomic_bytes

        def fail_preparation(path, data, mode=0o600):
            if path.name.endswith(".after"):
                raise OSError("preparation failed")
            return _atomic_bytes(path, data, mode)

        with patch("kora.install._atomic_bytes", side_effect=fail_preparation):
            with self.assertRaisesRegex(OSError, "preparation"):
                self.installer.apply({"codex:example": self.files(b"new")})
        self.assertEqual((self.home / self.skill).read_bytes(), b"version one")
        self.assertEqual(list((self.home / self.skill).parent.glob(".kora-*")), [])
        self.installer.rollback()
        self.assertFalse((self.home / self.skill).exists())

    def test_new_process_recovers_after_abrupt_termination(self):
        self.installer.apply({"codex:example": self.files()})
        script = '''
import os, sys
from pathlib import Path
from kora.catalog import File
from kora.install import Installer
i=Installer(Path(sys.argv[1]))
original=i._replace
def stop_after_replace(source, destination):
    original(source,destination)
    os._exit(41)
i._replace=stop_after_replace
i.apply({"codex:example": {".agents/skills/example/SKILL.md": File(b"interrupted new")}})
'''
        result = subprocess.run([sys.executable, "-c", script, str(self.home)], capture_output=True)
        self.assertEqual(result.returncode, 41, result.stderr.decode())
        self.assertEqual((self.home / self.skill).read_bytes(), b"interrupted new")
        recovered = Installer(self.home)
        recovered.recover()
        self.assertEqual((self.home / self.skill).read_bytes(), b"version one")
        self.assertEqual(recovered.status()["changes"], [])

    def test_crash_at_each_rename_restores_a_mixed_multifile_transaction(self):
        crash_script = '''
import os, sys
from pathlib import Path
import kora.install as module
from kora.catalog import File
installer = module.Installer(Path(sys.argv[1]))
phase, crash_at, action = sys.argv[2], int(sys.argv[3]), sys.argv[4]
calls = 0
def wrap(original):
    def stop(source, destination):
        global calls
        calls += 1
        if calls == crash_at and phase == "before":
            os._exit(42)
        original(source, destination)
        if calls == crash_at and phase == "after":
            os._exit(42)
    return stop
module.exchange = wrap(module.exchange)
module.rename_new = wrap(module.rename_new)
if action == "apply":
    installer.apply({"mixed": {".agents/skills/a/SKILL.md": File(b"new a"),
                               ".agents/skills/c/SKILL.md": File(b"new c")}})
else:
    getattr(installer, action)()
'''
        old = {".agents/skills/a/SKILL.md": File(b"old a"),
               ".agents/skills/b/SKILL.md": File(b"old b")}
        new = {".agents/skills/a/SKILL.md": File(b"new a"),
               ".agents/skills/c/SKILL.md": File(b"new c")}
        for action in ("apply", "rollback", "recover"):
            for phase in ("before", "after"):
                for crash_at in (1, 2, 3):
                    with self.subTest(action=action, phase=phase, crash_at=crash_at):
                        with tempfile.TemporaryDirectory() as directory:
                            home = Path(directory)
                            installer = Installer(home)
                            installer.apply({"mixed": old})
                            personal = home / ".agents/skills/a/notes.txt"
                            personal.write_bytes(b"personal notes")
                            if action == "rollback":
                                installer.apply({"mixed": new})
                            elif action == "recover":
                                # Terminate after the last live mutation, before
                                # the installed-state commit, then crash undo too.
                                first = subprocess.run([sys.executable, "-c", crash_script,
                                                        directory, "after", "3", "apply"], capture_output=True)
                                self.assertEqual(first.returncode, 42, first.stderr.decode())
                            result = subprocess.run([sys.executable, "-c", crash_script,
                                                     directory, phase, str(crash_at), action], capture_output=True)
                            self.assertEqual(result.returncode, 42, result.stderr.decode())
                            fresh = Installer(home)
                            fresh.recover()
                            fresh.recover()  # Recovery must not reverse a second time.
                            for path, file in old.items():
                                self.assertEqual((home / path).read_bytes(), file.data)
                            self.assertFalse((home / ".agents/skills/c/SKILL.md").exists())
                            self.assertEqual(personal.read_bytes(), b"personal notes")
                            self.assertEqual(fresh.status()["changes"], [])
                            self.assertFalse(fresh.status()["recovery_pending"])

    def test_late_edits_during_retirement_and_undo_are_captured(self):
        import kora.install as module

        for operation in ("retire", "rollback", "recover"):
            with self.subTest(operation=operation), tempfile.TemporaryDirectory() as directory:
                installer = Installer(Path(directory))
                installer.apply({"codex:example": self.files()})
                if operation in ("rollback", "recover"):
                    if operation == "recover":
                        original = installer._replace

                        def interrupt(source, destination):
                            original(source, destination)
                            raise KeyboardInterrupt()

                        with patch.object(installer, "_replace", side_effect=interrupt):
                            with self.assertRaises(KeyboardInterrupt):
                                installer.apply({"codex:example": self.files(b"version two")})
                    else:
                        installer.apply({"codex:example": self.files(b"version two")})
                path = Path(directory) / self.skill
                edited_inode = path.stat().st_ino
                fired = False

                def wrap(original):
                    def edit_then_rename(source, destination):
                        nonlocal fired
                        if not fired:
                            fired = True
                            subprocess.run([sys.executable, "-c",
                                            "import pathlib,sys; pathlib.Path(sys.argv[1]).write_bytes(b'late edit')",
                                            str(path)], check=True)
                        return original(source, destination)
                    return edit_then_rename

                with patch("kora.install.exchange", side_effect=wrap(module.exchange)), \
                     patch("kora.install.rename_new", side_effect=wrap(module.rename_new)):
                    with self.assertRaisesRegex(KoraError, "cambio local"):
                        if operation == "retire":
                            installer.apply({}, remove=["codex:example"])
                        else:
                            getattr(installer, operation)()
                retained = [p for p in Path(directory).rglob("*")
                            if p.is_file() and p.stat().st_ino == edited_inode]
                self.assertTrue(any(p.read_bytes() == b"late edit" for p in retained))
                self.assertFalse(installer.status()["recovery_pending"])

    def test_late_creation_is_not_overwritten_by_publish_or_recovery(self):
        import kora.install as module

        for recovery in (False, True):
            with self.subTest(recovery=recovery), tempfile.TemporaryDirectory() as directory:
                home = Path(directory)
                installer = Installer(home)
                if recovery:
                    installer.apply({"codex:example": self.files()})
                    installer.apply({}, remove=["codex:example"])
                path = home / self.skill
                original = module.rename_new

                def create_then_publish(source, destination):
                    if destination == path:
                        subprocess.run([sys.executable, "-c",
                                        "import pathlib,sys; pathlib.Path(sys.argv[1]).write_bytes(b'new personal file')",
                                        str(path)], check=True)
                    return original(source, destination)

                with patch("kora.install.rename_new", side_effect=create_then_publish):
                    with self.assertRaises(FileExistsError):
                        if recovery:
                            installer.rollback()
                        else:
                            installer.apply({"codex:example": self.files()})
                self.assertEqual(path.read_bytes(), b"new personal file")

    def test_crash_after_hardlink_or_commit_resumes_the_recorded_direction(self):
        script = '''
import os, sys
from pathlib import Path
import kora.install as module
from kora.catalog import File
installer = module.Installer(Path(sys.argv[1]))
point = sys.argv[2]
if point == "hardlink":
    original = os.link
    def stop(*args, **kwargs):
        original(*args, **kwargs)
        os._exit(43)
    os.link = stop
    installer.rollback()
else:
    original = module._json_write
    def stop(path, value):
        original(path, value)
        if path == installer.state_file:
            os._exit(43)
    module._json_write = stop
    installer.apply({"codex:example": {".agents/skills/example/SKILL.md": File(b"version two")}})
'''
        for point in ("hardlink", "commit"):
            with self.subTest(point=point), tempfile.TemporaryDirectory() as directory:
                home = Path(directory)
                installer = Installer(home)
                installer.apply({"codex:example": self.files()})
                if point == "hardlink":
                    installer.apply({"codex:example": self.files(b"version two")})
                result = subprocess.run([sys.executable, "-c", script, directory, point], capture_output=True)
                self.assertEqual(result.returncode, 43, result.stderr.decode())
                fresh = Installer(home)
                fresh.recover()
                expected = b"version one" if point == "hardlink" else b"version two"
                self.assertEqual((home / self.skill).read_bytes(), expected)
                self.assertEqual(fresh.status()["changes"], [])
                self.assertFalse(fresh.status()["recovery_pending"])

    def test_installer_cannot_adopt_its_own_journal(self):
        self.installer.apply({"codex:example": self.files()})
        journal_path = self.installer.journal_file
        saved = journal_path.read_bytes()
        from kora.catalog import digest
        relative = str(journal_path.relative_to(self.home))
        with self.assertRaises(KoraError):
            self.installer.apply({"bad": {relative: File(b"overwrite journal")}},
                                 adopt={relative: digest(saved)})
        self.assertEqual(journal_path.read_bytes(), saved)
        self.installer.rollback()
        self.assertFalse((self.home / self.skill).exists())

    def test_recovery_does_not_overwrite_edits_made_after_interruption(self):
        self.installer.apply({"codex:example": self.files()})
        original = self.installer._replace

        def interrupted(source, destination):
            original(source, destination)
            raise KeyboardInterrupt()

        with patch.object(self.installer, "_replace", side_effect=interrupted):
            with self.assertRaises(KeyboardInterrupt):
                self.installer.apply({"codex:example": self.files(b"new")})
        (self.home / self.skill).write_bytes(b"concurrent work")
        with self.assertRaisesRegex(KoraError, "cambio local"):
            self.installer.recover()
        self.assertEqual((self.home / self.skill).read_bytes(), b"concurrent work")

    def test_path_traversal_and_symlink_do_not_touch_outside_content(self):
        with self.assertRaises(KoraError):
            self.installer.apply({"invalid": {"../outside": File(b"overwrite")}})
        outside = self.home / "foreign"
        outside.mkdir()
        (self.home / ".agents").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(KoraError):
            self.installer.apply({"invalid": self.files()})
        self.assertEqual(list(outside.iterdir()), [])

    def test_parent_replaced_by_symlink_in_the_last_gap_cannot_redirect_writes(self):
        self.installer.apply({"codex:example": self.files()})
        outside = self.home / "foreign"
        outside.mkdir()
        (outside / "SKILL.md").write_bytes(b"foreign content")
        live_parent = (self.home / self.skill).parent
        held = live_parent.with_name("moved-by-user")
        original = self.installer._replace

        def redirect_then_replace(source, destination):
            subprocess.run([sys.executable, "-c", '''
from pathlib import Path
import sys
parent, held, outside = map(Path, sys.argv[1:])
parent.rename(held)
parent.symlink_to(outside, target_is_directory=True)
''', str(live_parent), str(held), str(outside)], check=True)
            return original(source, destination)

        with patch.object(self.installer, "_replace", side_effect=redirect_then_replace):
            with self.assertRaises((KoraError, OSError)):
                self.installer.apply({"codex:example": self.files(b"version two")})
        self.assertEqual((outside / "SKILL.md").read_bytes(), b"foreign content")
        self.assertEqual((held / "SKILL.md").read_bytes(), b"version one")

    def test_late_symlink_is_retained_and_reported_without_reading_its_target(self):
        self.installer.apply({"codex:example": self.files()})
        outside = self.home / "foreign.txt"
        outside.write_bytes(b"foreign content")
        original = self.installer._replace

        def link_then_replace(source, destination):
            destination.unlink()
            destination.symlink_to(outside)
            return original(source, destination)

        with patch.object(self.installer, "_replace", side_effect=link_then_replace):
            with self.assertRaises(KoraError):
                self.installer.apply({"codex:example": self.files(b"version two")})
        self.assertEqual(outside.read_bytes(), b"foreign content")
        status = self.installer.status()
        self.assertTrue(status["recovery_pending"])
        self.assertTrue(any((self.home / record["backup"]).is_symlink()
                            for record in status["preserved_changes"]))


if __name__ == "__main__":
    unittest.main()
