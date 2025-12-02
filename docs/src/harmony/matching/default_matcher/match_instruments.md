# match_instruments (function)

**Code:**
```python
def match_instruments(
        instruments: List[Instrument],
        query: str = None,
        topics: List = [],
        mhc_questions: List = [],
        mhc_all_metadatas: List = [],
        mhc_embeddings: np.ndarray = np.zeros((0, 0)),
        texts_cached_vectors: dict[str, List[float]] = {}, batch_size: int = 1000, max_batches: int = 2000,
        is_negate: bool = True,
        clustering_algorithm: str = "affinity_propagation",
        num_clusters_for_kmeans: int = None
) -> MatchResult:
    return match_instruments_with_function(
        instruments=instruments,
        query=query,
        vectorisation_function=lambda texts: convert_texts_to_vector(texts, batch_size=batch_size,
                                                                     max_batches=max_batches),
        topics=topics,
        mhc_questions=mhc_questions,
        mhc_all_metadatas=mhc_all_metadatas,
        mhc_embeddings=mhc_embeddings,
        texts_cached_vectors=texts_cached_vectors,
        is_negate=is_negate,
        clustering_algorithm=clustering_algorithm,
        num_clusters_for_kmeans=num_clusters_for_kmeans
    )
```

**Explanation:**
**`match_instruments` – a thin wrapper around the core matching logic**

```python
def match_instruments(
        instruments: List[Instrument],
        query: str = None,
        topics: List = [],
        mhc_questions: List = [],
        mhc_all_metadatas: List = [],
        mhc_embeddings: np.ndarray = np.zeros((0, 0)),
        texts_cached_vectors: dict[str, List[float]] = {},
        batch_size: int = 1000,
        max_batches: int = 2000,
        is_negate: bool = True,
        clustering_algorithm: str = "affinity_propagation",
        num_clusters_for_kmeans: int = None
) -> MatchResult:
```

* **What it does**  
  * Builds a *vectorisation function* that turns any list of texts into embeddings by calling `convert_texts_to_vector`.  
  * Passes that function, along with all the other arguments, to the real implementation `match_instruments_with_function`.  
  * Returns the `MatchResult` produced by that implementation.

* **Why it exists**  
  * Keeps the public API simple: callers only need to provide the instruments, an optional query, and optional metadata.  
  * The heavy lifting (vectorisation, similarity calculations, clustering, MHC matching, etc.) lives in `match_instruments_with_function`.  
  * Allows the vectorisation logic to be swapped out or configured (batch size, max batches, caching) without changing the rest of the code.

* **Key parameters**  
  * `instruments`: list of `Instrument` objects to analyse.  
  * `query`: optional search string; if supplied, similarity to the query is computed.  
  * `topics`, `mhc_*`: optional data for topic tagging and MHC‑based matching.  
  * `texts_cached_vectors`: cache of already‑computed embeddings to avoid re‑calling the LLM.  
  * `batch_size` / `max_batches`: control how many texts are sent to the LLM at once.  
  * `is_negate`: whether to also compute embeddings for negated versions of the texts.  
  * `clustering_algorithm`: which clustering method to use (`affinity_propagation`, `deterministic`, `kmeans`, `hdbscan`).  
  * `num_clusters_for_kmeans`: number of clusters to request when using k‑means (auto‑computed if `None`).

In short, `match_instruments` is a convenience entry point that configures the vectorisation step and delegates all the matching logic to `match_instruments_with_function`.

**Imports:**
```
import os, from typing import List, import numpy as np, from harmony import match_instruments_with_function, from harmony.schemas.requests.text import Instrument, from numpy import ndarray, from sentence_transformers import SentenceTransformer, from harmony.schemas.responses.text import MatchResult
```
