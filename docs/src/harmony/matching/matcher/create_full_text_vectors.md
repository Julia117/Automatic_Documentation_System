# create_full_text_vectors (function)

**Code:**
```python
def create_full_text_vectors(
        all_questions: List[str],
        query: Optional[str],
        vectorisation_function: Callable,
        texts_cached_vectors: dict[str, list[float]],
        is_negate: bool
) -> tuple[List[TextVector], dict]:
    """
    Create full text vectors.
    """

    # Create a list of text vectors
    text_vectors = process_questions(all_questions, texts_cached_vectors, is_negate=is_negate)

    # Add query
    if query:
        text_vectors = add_text_to_vec(query, texts_cached_vectors, text_vectors, False, True)

    # Texts with no cached vector
    texts_not_cached = [x.text for x in text_vectors if not x.vector]

    # Get vectors for all texts not cached
    new_vectors_list: List = process_items_in_batches(texts_not_cached, vectorisation_function)

    # Create a dictionary with new vectors
    new_vectors_dict = {}
    for vector, text in zip(new_vectors_list, texts_not_cached):
        new_vectors_dict[text] = vector

    # Add new vectors to all_texts
    for index, text_dict in enumerate(text_vectors):
        if not text_dict.vector:
            new_vector: ndarray = new_vectors_list.pop(0)
            text_vectors[index].vector = new_vector.tolist()

    return text_vectors, new_vectors_dict
```

**Explanation:**
**`create_full_text_vectors` – quick rundown**

| Step | What it does | Why it matters |
|------|--------------|----------------|
| **1. Build base list** | Calls `process_questions` on all supplied question texts. This creates a `TextVector` object for each question, marking whether it’s negated and whether it already has a cached vector. | Gives us a uniform list of objects to work with. |
| **2. Add the query (if any)** | If a query string is supplied, it’s appended to the list with `is_query=True`. | Lets the query participate in similarity calculations later. |
| **3. Find missing vectors** | Pulls out the texts that still have an empty `vector` field. | These are the ones that need to be vectorised. |
| **4. Vectorise in batches** | Calls `process_items_in_batches` (which internally uses the supplied `vectorisation_function`) on the missing texts. | Avoids calling the expensive vectoriser one‑by‑one. |
| **5. Build a lookup dict** | Creates `new_vectors_dict` mapping each text to its freshly‑computed vector. | Useful for caching or debugging. |
| **6. Attach vectors back** | Pops vectors off the batch list and assigns them to the corresponding `TextVector` objects. | Now every `TextVector` has a real vector. |
| **7. Return** | Returns the full list of `TextVector` objects **and** the dict of new vectors. | The caller can use the list for similarity work and the dict to update the cache. |

**Bottom line:**  
`create_full_text_vectors` takes raw question strings (and an optional query), ensures every one has a vector (using cached ones when available), vectorises the rest in bulk, and returns both the enriched objects and a mapping of the new vectors. This keeps vectorisation efficient and cache‑friendly.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
