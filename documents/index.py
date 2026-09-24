"""Index source documents in Elasticsearch."""

from collections.abc import Iterable
from typing import Any


def index_documents(client: Any, index_name: str, documents: Iterable[dict[str, Any]]) -> None:
    """Index source documents using the Elasticsearch client."""
    for document in documents:
        client.index(index=index_name, id=document.get("document_id"), document=document)
