"""Extract candidate records from an upstream source."""

from collections.abc import Iterable
from typing import Any


def extract_candidates(source: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Materialize candidate records from the configured source."""
    return list(source)
