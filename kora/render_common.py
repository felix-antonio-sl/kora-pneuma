"""Shared source locators and availability notices for native realizations."""

from pathlib import Path
import shlex
from dataclasses import replace


def sourced_files(product, files):
    source = {"id": product.id, "kind": product.kind, "name": product.name,
              "fingerprint": product.fingerprint(), "revision": product.revision}
    return {path: replace(file, source=source) for path, file in files.items()}


def resolver_note(catalog, dependencies):
    if not any(product.reference_root is not None for product in dependencies):
        return []
    entrypoint = catalog.root / "kora_cli.py"
    if not entrypoint.is_file():
        entrypoint = Path(__file__).resolve().parents[1] / "kora_cli.py"
    command = shlex.join(["python3", str(entrypoint), "--root", str(catalog.root),
                          "--knowledge-root", str(catalog.knowledge_root), "resolve", "URN"])
    return ["", "El conocimiento publicado es de consulta. Su `object.yaml` indica "
            "el estado de publicación; `legacy` conserva disponibilidad sin una nueva aprobación. "
            "Para editarlo prepara un borrador con KORA; conserva la referencia vigente hasta aprobar la revisión.",
            f"Resuelve otras identidades y las referencias que añada el conocimiento con `{command}`."]


def availability_note(catalog, product, target):
    lines = []
    for edge in catalog.explain(product, target)["edges"]:
        if edge["status"] == "not_applicable":
            continue
        condition = edge.get("condition")
        if edge["status"] == "unavailable":
            scope = f"cuando {condition}" if condition else "necesidad obligatoria"
            lines.append(f"- Recorrido no disponible ({scope}): `{edge['target']}`. "
                         f"{edge.get('error', 'Depende de otro recorrido no disponible')}. "
                         "Detén ese recorrido hasta satisfacer su necesidad.")
        elif condition:
            lines.append(f"- Para {condition}, está disponible `{edge['target']}`; "
                         "úsalo únicamente cuando ese caso corresponda al encargo.")
        elif edge["kind"] == "capability":
            lines.append(f"- Capacidad `{edge['target']}` declarada por el llamador para esta preparación. "
                         "Su uso conserva los permisos efectivos del runtime y del encargo.")
    return ["", "Necesidades y recorridos:", "", *lines] if lines else []
