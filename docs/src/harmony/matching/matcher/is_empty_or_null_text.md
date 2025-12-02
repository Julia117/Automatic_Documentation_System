# is_empty_or_null_text (function)

**Code:**
```python
def is_empty_or_null_text(text: Optional[str]) -> bool:
    if text is None:
        return True
    if isinstance(text, str) and text.strip() == "":
        return True
    return False
```

**Explanation:**
**`is_empty_or_null_text` – quick sanity check for a string**

```python
def is_empty_or_null_text(text: Optional[str]) -> bool:
    if text is None:
        return True
    if isinstance(text, str) and text.strip() == "":
        return True
    return False
```

- **Purpose**: Decide whether a given `text` value should be treated as “empty”.
- **Logic**:
  1. If `text` is `None` → return `True`.
  2. If `text` is a string and, after removing leading/trailing whitespace, it’s an empty string (`""`) → return `True`.
  3. In all other cases (non‑empty string, non‑string types) → return `False`.

- **Use case**: Before processing a question or answer, you can call this to skip or handle empty inputs gracefully.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
