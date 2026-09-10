"""Normalize dependency declarations without rewriting their source metadata."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Need:
    id: str
    kind: str | None = None
    revision: str | None = None
    target: str | None = None
    condition: str | None = None
    purpose: str | None = None

    @classmethod
    def read(cls, value):
        if isinstance(value, str) and value.strip():
            return cls(value)
        fields = {"id", "kind", "revision", "target", "condition", "purpose"}
        if not isinstance(value, dict) or set(value) - fields:
            raise ValueError("Una necesidad debe ser una identidad o un mapa de necesidad conocido")
        if any(not isinstance(item, str) or not item.strip() for item in value.values()):
            raise ValueError("Los campos de una necesidad deben ser textos no vacíos")
        if "id" not in value:
            raise ValueError("La necesidad requiere id")
        need = cls(**value)
        if need.kind not in (None, "product", "knowledge", "capability"):
            raise ValueError(f"Tipo de necesidad desconocido: {need.kind}")
        if need.target not in (None, "codex", "hermes"):
            raise ValueError(f"Destino de necesidad desconocido: {need.target}")
        if need.revision is not None and not re.fullmatch(r"[0-9a-f]{64}", need.revision):
            raise ValueError("La revisión fijada debe ser un SHA-256 completo")
        if need.kind == "capability" and need.revision is not None:
            raise ValueError("Una capacidad no fija una revisión de producto")
        return need


def normalize(values):
    if not isinstance(values, (tuple, list)):
        raise ValueError("requires debe ser una lista de necesidades")
    return tuple(Need.read(value) for value in values)
