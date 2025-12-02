# add_text_to_vec (function)

**Code:**
```python
def add_text_to_vec(text, texts_cached_vectors, text_vectors, is_negated_, is_query_) -> list[TextVector]:
    if text not in texts_cached_vectors:
        text_vectors.append(
            TextVector(
                text=text, vector=[], is_negated=is_negated_, is_query=is_query_
            )
        )
    else:
        vector = texts_cached_vectors[text]
        text_vectors.append(
            TextVector(
                text=text,
                vector=vector,
                is_negated=is_negated_,
                is_query=is_query_,
            )
        )
    return text_vectors
```

**Explanation:**
**What it does**

`add_text_to_vec` takes a single piece of text and adds it to a growing list of `TextVector` objects.

* If the text already has a cached vector (`texts_cached_vectors`), that vector is used.
* If not, an empty vector (`[]`) is stored so the caller knows the vector still needs to be computed later.
* The two boolean flags `is_negated_` and `is_query_` are copied into the new `TextVector` so the caller can later distinguish normal, negated, or query‑only vectors.

Finally it returns the updated list of `TextVector` objects.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
