"""Index candidate records in Elasticsearch."""

from collections.abc import Iterable
from typing import Any


def index_candidates(client: Any, index_name: str, candidates: Iterable[dict[str, Any]]) -> None:
    """Index candidate records using the Elasticsearch client."""
    for candidate in candidates:
        client.index(index=index_name, id=candidate.get("candidate_id"), document=candidate)
