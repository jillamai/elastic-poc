"""Environment-backed configuration for the Elasticsearch POC."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    elasticsearch_url: str = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
    elasticsearch_api_key: str | None = os.getenv("ELASTICSEARCH_API_KEY") or None
    elasticsearch_username: str | None = os.getenv("ELASTICSEARCH_USERNAME") or None
    elasticsearch_password: str | None = os.getenv("ELASTICSEARCH_PASSWORD") or None
    verify_certs: bool = os.getenv("ELASTICSEARCH_VERIFY_CERTS", "true").lower() == "true"
    candidates_index: str = os.getenv("CANDIDATES_INDEX", "candidates")
    documents_index: str = os.getenv("DOCUMENTS_INDEX", "documents")
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )


settings = Settings()
