"""Normalize documents before indexing."""

from typing import Any


def transform_document(document: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized document record."""
    transformed = dict(document)
    transformed["full_text"] = " ".join(
        str(transformed.get(field, ""))
        for field in ("title", "description", "content")
    ).strip()
    return transformed
