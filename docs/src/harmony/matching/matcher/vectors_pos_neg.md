# vectors_pos_neg (function)

**Code:**
```python
def vectors_pos_neg(text_vectors):
    vectors_pos = np.array(
        [
            x.vector
            for x in text_vectors
            if (x.is_negated is False and x.is_query is False)
        ]
    )

    # Create numpy array of negated texts vectors
    vectors_neg = np.array(
        [
            x.vector
            for x in text_vectors
            if (x.is_negated is True and x.is_query is False)
        ]
    )
    return vectors_pos, vectors_neg
```

**Explanation:**
**`vectors_pos_neg` – quick filter into “positive” and “negative” vectors**

```python
def vectors_pos_neg(text_vectors):
    vectors_pos = np.array(
        [x.vector for x in text_vectors
         if (x.is_negated is False and x.is_query is False)]
    )
    vectors_neg = np.array(
        [x.vector for x in text_vectors
         if (x.is_negated is True and x.is_query is False)]
    )
    return vectors_pos, vectors_neg
```

* **Input** – a list of `TextVector` objects (each has a `vector`, `is_negated`, and `is_query` flag).
* **What it does**  
  * Builds a NumPy array of all vectors that are **not negated** and **not a query** (`vectors_pos`).  
  * Builds a second array of all vectors that **are negated** and **not a query** (`vectors_neg`).
* **Return** – a tuple `(vectors_pos, vectors_neg)`.

In short, it splits the collection into two groups: normal (positive) text vectors and their negated counterparts, ignoring any vectors that were added as queries.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
