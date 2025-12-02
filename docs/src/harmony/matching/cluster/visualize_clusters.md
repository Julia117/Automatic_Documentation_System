# visualize_clusters (function)

**Code:**
```python
def visualize_clusters(embeddings_in, kmeans_labels):
    try:
        import matplotlib.pyplot as plt
        pca = PCA(n_components=2)
        reduced_embeddings = pca.fit_transform(embeddings_in)
        plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=kmeans_labels, cmap='viridis', s=50)
        plt.colorbar()
        plt.title("Question Clusters")

        for i, point in enumerate(reduced_embeddings):
            plt.annotate(
                str(i),  # Label each point with its question number
                (point[0], point[1]),  # Coordinates from reduced_embeddings
                fontsize=8,
                ha="center"
            )

        plt.show()
    except ImportError as e:
        print(
            "Matplotlib is not installed. Please install it using:\n"
            "pip install matplotlib==3.7.0"
        )
        sys.exit(1)
```

**Explanation:**
**`visualize_clusters` – quick 2‑D plot of K‑Means clusters**

```python
def visualize_clusters(embeddings_in, kmeans_labels):
```

* **Inputs**
  * `embeddings_in` – a NumPy array of high‑dimensional embeddings (one row per question).
  * `kmeans_labels` – the integer cluster label assigned to each embedding by K‑Means.

* **What it does**
  1. **Import matplotlib** – if it isn’t installed, prints a friendly message and exits.
  2. **Reduce dimensionality** – uses `PCA(n_components=2)` to project the embeddings onto a 2‑D plane.
  3. **Scatter plot** – draws each point in the 2‑D space, coloring it by its cluster label (`c=kmeans_labels`) with the `viridis` colormap.
  4. **Add a color bar** – shows the mapping from colors to cluster numbers.
  5. **Title** – “Question Clusters”.
  6. **Annotate points** – labels each point with its index (`0, 1, 2, …`) so you can see which question is which.
  7. **Display** – calls `plt.show()` to open the plot window.

* **Why it’s useful**
  * Gives a quick visual sanity check that the K‑Means clustering produced distinct groups.
  * The 2‑D PCA projection is a common way to inspect high‑dimensional data in a single figure.

* **Error handling**
  * If `matplotlib` is missing, it prints an install hint (`pip install matplotlib==3.7.0`) and exits the program.

In short, `visualize_clusters` turns your high‑dimensional question embeddings into a colored scatter plot, letting developers see how the K‑Means algorithm has grouped the questions.

**Imports:**
```
import sys, from typing import List, import pandas as pd, from sklearn.cluster import KMeans, from sklearn.decomposition import PCA, from sklearn.metrics import silhouette_score, from harmony.matching.default_matcher import convert_texts_to_vector, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, import numpy as np, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.deterministic_clustering import find_clusters_deterministic
```
