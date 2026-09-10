"""Linux name operations which never discard an occupied destination.

renameat2(2): https://man7.org/linux/man-pages/man2/rename.2.html
The caller owns durability (directory fsync) and recovery of exchanged objects.
There is deliberately no overwrite fallback when the filesystem lacks support.
"""

import ctypes
from contextlib import contextmanager
import os
from pathlib import Path


_libc = ctypes.CDLL(None, use_errno=True)
_renameat2 = _libc.renameat2
_renameat2.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int,
                       ctypes.c_char_p, ctypes.c_uint]
_renameat2.restype = ctypes.c_int


@contextmanager
def _parent(path: Path):
    # openat + O_NOFOLLOW on EVERY component: a parent replaced by a symlink
    # cannot redirect the operation after a caller's path preflight. Directory
    # descriptors pin the objects that were actually opened.
    # https://man7.org/linux/man-pages/man2/open.2.html
    path = Path(path).absolute()
    # A dirfd for renameat2 needs traversal, not directory listing permission.
    # O_PATH keeps the pinned-directory and no-symlink guarantees without read access.
    flags = os.O_PATH | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(path.anchor, flags)
    try:
        for component in path.parts[1:-1]:
            next_fd = os.open(component, flags, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        yield fd, os.fsencode(path.name)
    finally:
        os.close(fd)


def _rename(source: Path, destination: Path, flags: int) -> None:
    with _parent(source) as (source_fd, source_name), \
         _parent(destination) as (destination_fd, destination_name):
        if _renameat2(source_fd, source_name, destination_fd, destination_name, flags):
            error = ctypes.get_errno()
            raise OSError(error, os.strerror(error), os.fspath(source), None,
                          os.fspath(destination))


def rename_new(source: Path, destination: Path) -> None:
    """Move a name only when destination is absent (RENAME_NOREPLACE)."""
    _rename(source, destination, 1)


def exchange(source: Path, destination: Path) -> None:
    """Exchange two existing names atomically (RENAME_EXCHANGE)."""
    _rename(source, destination, 2)
