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
  2. Fit the model to `embeddings_in` and simultaneously predict the cluster label for each embedding (`fit_predict`).
  3. Return an array of integer labels, one per embedding, indicating which cluster each belongs to.

- **Typical use**: Pass the output of an embedding model (e.g., sentence embeddings) and get back cluster assignments that can be used for grouping similar questions, visualizing clusters, or further analysis.

**Imports:**
```
import sys, from typing import List, import pandas as pd, from sklearn.cluster import KMeans, from sklearn.decomposition import PCA, from sklearn.metrics import silhouette_score, from harmony.matching.generate_cluster_topics import generate_cluster_topics, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, import numpy as np, from sklearn.metrics.pairwise import cosine_similarity
```
