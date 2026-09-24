"""Keyword search helpers."""

from typing import Any


def keyword_search(client: Any, index_name: str, query: str) -> Any:
    """Search indexed text fields with a multi-match query."""
    return client.search(
        index=index_name,
        query={"multi_match": {"query": query, "fields": ["title", "summary", "full_text"]}},
    )
