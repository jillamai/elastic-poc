"""Matching and result-ranking utilities."""

from typing import Any


def ranked_ids(response: dict[str, Any]) -> list[str]:
    """Extract document IDs in score order from an Elasticsearch response."""
    return [str(hit["_id"]) for hit in response.get("hits", {}).get("hits", [])]
