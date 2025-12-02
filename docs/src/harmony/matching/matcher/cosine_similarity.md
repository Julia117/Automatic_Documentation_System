# cosine_similarity (function)

**Code:**
```python
def cosine_similarity(vec1: ndarray, vec2: ndarray) -> ndarray:
    dp = dot(vec1, vec2.T)
    m1 = matrix(norm(vec1, axis=1))
    m2 = matrix(norm(vec2.T, axis=0))

    return np.asarray(dp / matmul(m1.T, m2))
```

**Explanation:**
**What it does**

`cosine_similarity` takes two 2‑D NumPy arrays (`vec1` and `vec2`) where each row is a vector.  
It returns a matrix where the entry `(i, j)` is the cosine similarity between row `i` of `vec1` and row `j` of `vec2`.

**How it works**

1. **Dot products** – `dp = dot(vec1, vec2.T)` gives a matrix of all pairwise dot products.  
2. **Norms** –  
   * `m1` holds the L2 norm of each row in `vec1`.  
   * `m2` holds the L2 norm of each row in `vec2`.  
3. **Normalize** – Divide each dot product by the product of the corresponding norms (`matmul(m1.T, m2)`).  
4. **Return** – Convert the result to a plain NumPy array.

The result is a cosine‑similarity matrix with values in the range `[-1, 1]`.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
