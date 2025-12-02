# perform_kmeans (function)

**Code:**
```python
def perform_kmeans(embeddings_in, num_clusters=5):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans_labels = kmeans.fit_predict(embeddings_in)
    return kmeans_labels
```

**Explanation:**
**`perform_kmeans` – quick summary for developers**

```python
def perform_kmeans(embeddings_in, num_clusters=5):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans_labels = kmeans.fit_predict(embeddings_in)
    return kmeans_labels
```

- **Purpose**: Cluster a set of vector embeddings into a specified number of groups.
- **How it works**:
  1. Create a `KMeans` object from scikit‑learn with `n_clusters` set to `num_clusters`.
  2. Call `fit_predict` on the input embeddings (`embeddings_in`).  
     - `fit` learns the cluster centroids.  
     - `predict` assigns each embedding to the nearest centroid.
  3. Return the resulting array of cluster labels (one integer per embedding).

- **Typical use**: Pass a NumPy array of shape `(n_samples, n_features)` and get back an array of cluster indices that you can attach to your data or use for downstream processing.

**Imports:**
```
import sys, from typing import List, import pandas as pd, from sklearn.cluster import KMeans, from sklearn.decomposition import PCA, from sklearn.metrics import silhouette_score, from harmony.matching.default_matcher import convert_texts_to_vector, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, import numpy as np, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.deterministic_clustering import find_clusters_deterministic
```
