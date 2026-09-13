"""One explicit runtime resolution for tests of admitted or candidate resources."""
import os
from pathlib import Path


def runtime_root():
    root = Path(__file__).resolve().parents[2]
    explicit = os.environ.get('GTD_RUNTIME_ROOT')
    if explicit is not None:
        if not explicit.strip():
            raise RuntimeError('gtd_runtime_unavailable')
        selected = Path(explicit).expanduser().resolve()
    else:
        selected = root / 'products/fxsl/gtd-operations/runtime'
    if not (selected / 'gtd_felix/__init__.py').is_file():
        raise RuntimeError('gtd_runtime_unavailable')
    return selected


RUNTIME = runtime_root()
