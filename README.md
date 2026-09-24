# Pro Industry Elastic POC

Proof of concept for indexing candidate and document data in Elasticsearch and evaluating keyword, semantic, and hybrid retrieval.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set Elasticsearch and embedding configuration in `.env`. The modules are organized by extraction, transformation, mapping, indexing, search, and evaluation concerns.

## Evaluation

Edit `evaluation/queries.json` with representative queries, then run:

```bash
python evaluation/benchmark.py
```

The notebook in `notebooks/elastic_poc.ipynb` provides an interactive workflow.
