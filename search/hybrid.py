"""Hybrid retrieval helpers."""

from typing import Any, Sequence


def hybrid_search(
    client: Any, index_name: str, query: str, embedding: Sequence[float]
) -> Any:
    """Combine lexical and semantic retrieval with reciprocal rank fusion."""
    return client.search(
        index=index_name,
        query={"multi_match": {"query": query, "fields": ["title", "summary", "full_text"]}},
        knn={"field": "embedding", "query_vector": list(embedding), "k": 10, "num_candidates": 100},
    )
