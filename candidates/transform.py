"""Normalize candidate records before indexing."""

from typing import Any


def transform_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """Return a normalized candidate record."""
    transformed = dict(candidate)
    transformed["full_text"] = " ".join(
        str(transformed.get(field, ""))
        for field in ("name", "title", "summary", "skills")
    ).strip()
    return transformed
