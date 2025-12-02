# vectorise_texts (function)

**Code:**
```python
def vectorise_texts(text_vectors, vectorisation_function):
    for index, text_dict in enumerate(text_vectors):
        if not text_dict.vector:
            text_vectors[index].vector = vectorisation_function([text_dict.text]).tolist()[0]
    return text_vectors
```

**Explanation:**
**`vectorise_texts` – quick‑look**

```python
def vectorise_texts(text_vectors, vectorisation_function):
    for index, text_dict in enumerate(text_vectors):
        if not text_dict.vector:
            text_vectors[index].vector = vectorisation_function([text_dict.text]).tolist()[0]
    return text_vectors
```

* **What it does**  
  *Iterates over a list of `TextVector` objects (`text_vectors`).*  
  For each object that still has no `vector` (i.e., `vector` is `None` or empty), it calls the supplied `vectorisation_function` with a single‑item list containing that object's `text`.  
  The function is expected to return a NumPy array (or similar) of embeddings; `.tolist()[0]` converts the first (and only) embedding to a plain Python list and stores it back in `text_dict.vector`.

* **Why it’s useful**  
  It lazily fills in missing embeddings for a batch of texts, reusing any cached vectors that may already exist.  
  After the loop, the original list is returned, now with all `vector` fields populated where possible.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
