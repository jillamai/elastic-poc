"""Extract source documents."""

from collections.abc import Iterable
from typing import Any


def extract_documents(source: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Materialize documents from the configured source."""
    return list(source)
