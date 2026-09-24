"""Elasticsearch mapping for source documents."""

DOCUMENT_MAPPING = {
    "properties": {
        "document_id": {"type": "keyword"},
        "title": {"type": "text"},
        "description": {"type": "text"},
        "content": {"type": "text"},
        "full_text": {"type": "text"},
    }
}
