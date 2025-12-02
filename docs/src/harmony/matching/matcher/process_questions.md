# process_questions (function)

**Code:**
```python
def process_questions(questions: list, texts_cached_vectors: dict, is_negate: bool) -> list[TextVector]:
    text_vectors: List[TextVector] = []
    for question_text in questions:
        # Skip None or whitespace-only texts
        if question_text is None or str(question_text).strip() == "":
            text_vectors.append(
                TextVector(
                    text=question_text,
                    vector=None,
                    is_negated=False,
                    is_query=False,
                )
            )
            continue

        # Normal non-empty case
        text_vectors = add_text_to_vec(question_text, texts_cached_vectors, text_vectors, False, False)

        if is_negate:
            negated_text = negate(question_text, 'en')
        else:
            negated_text = question_text
        text_vectors = add_text_to_vec(negated_text, texts_cached_vectors, text_vectors, True, False)

    return text_vectors
```

**Explanation:**
**`process_questions` – quick rundown**

| What it does | How it does it | Why it matters |
|--------------|----------------|----------------|
| Takes a list of raw question strings, a cache of pre‑computed vectors, and a flag telling whether to generate “negated” versions of each question. | 1. **Skip empty/whitespace** – if a question is `None` or only spaces, it creates a `TextVector` with `vector=None` and moves on. <br>2. **Add the original text** – calls `add_text_to_vec` to either pull a cached vector or create a placeholder. <br>3. **Add the negated text** – if `is_negate` is `True`, it runs `negate(question_text, 'en')`; otherwise it re‑uses the original. It then calls `add_text_to_vec` again, marking the entry as `is_negated=True`. | This function normalises the input, ensures every question (and its negated form) ends up in a `TextVector` list, and guarantees that empty inputs are represented with `None` vectors so downstream code can safely check for missing embeddings. It also keeps the cache logic isolated in `add_text_to_vec`.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
