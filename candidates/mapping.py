"""Elasticsearch mapping for candidate documents."""

CANDIDATE_MAPPING = {
    "properties": {
        "candidate_id": {"type": "keyword"},
        "name": {"type": "text"},
        "title": {"type": "text"},
        "summary": {"type": "text"},
        "skills": {"type": "keyword"},
        "full_text": {"type": "text"},
    }
}
