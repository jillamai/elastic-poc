"""Parse raw document payloads into structured records."""

from typing import Any


def parse_document(raw_document: dict[str, Any]) -> dict[str, Any]:
    """Return a parsed document payload."""
    return dict(raw_document)
