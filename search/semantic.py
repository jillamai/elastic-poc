"""Semantic search helpers."""

from typing import Any, Sequence


def semantic_search(
    client: Any, index_name: str, embedding: Sequence[float], field: str = "embedding"
) -> Any:
    """Search indexed vectors with Elasticsearch k-nearest-neighbor search."""
    return client.search(
        index=index_name,
        knn={"field": field, "query_vector": list(embedding), "k": 10, "num_candidates": 100},
    )
