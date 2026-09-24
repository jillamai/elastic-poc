"""Evaluate retrieval results against labeled queries."""

import json
from pathlib import Path
from typing import Any


def load_queries(path: str | Path = Path(__file__).with_name("queries.json")) -> list[dict[str, Any]]:
    """Load benchmark queries from JSON."""
    return json.loads(Path(path).read_text())


def recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int = 10) -> float:
    """Calculate recall at k for one query."""
    if not relevant_ids:
        return 0.0
    return len(set(retrieved_ids[:k]) & relevant_ids) / len(relevant_ids)


if __name__ == "__main__":
    print(f"Loaded {len(load_queries())} benchmark queries")
