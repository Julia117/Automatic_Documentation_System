# cluster_questions (function)

**Code:**
```python
def cluster_questions(questions: List[Question], num_clusters: int, is_show_graph: bool, algorithm: str = "kmeans"):
    """
    Cluster questions using the specified algorithm.

    Parameters
    ----------
    questions : List[Question]
        A list of Question objects to cluster.
    num_clusters : int
        The number of clusters to create (only applicable for kmeans).
    is_show_graph : bool
        Whether to visualize the clusters.
    algorithm : str
        The clustering algorithm to use. Options are "kmeans" (default) or "deterministic".

    Returns
    -------
    df : pd.DataFrame
        A DataFrame with the questions and their assigned cluster numbers.
    sil_score : float or None
        The silhouette score for the clustering (None if the algorithm does not calculate it).
    """
    questions_list = [question.question_text for question in questions]
    embedding_matrix = convert_texts_to_vector(questions_list)

    if algorithm == "kmeans":
        kmeans_labels = perform_kmeans(embedding_matrix, num_clusters)
        sil_score = silhouette_score(embedding_matrix, kmeans_labels) if num_clusters > 1 else None

        if is_show_graph:
            visualize_clusters(embedding_matrix, kmeans_labels)

        df = pd.DataFrame({
            "question_text": questions_list,
            "cluster_number": kmeans_labels
        })

    elif algorithm == "deterministic":
        similarity_matrix = cosine_similarity(embedding_matrix)

        clusters = find_clusters_deterministic(questions, similarity_matrix)

        cluster_labels = []
        for question_idx in range(len(questions)):
            for cluster in clusters:
                if question_idx in cluster.item_ids:
                    cluster_labels.append(cluster.cluster_id)
                    break

        sil_score = None  
        df = pd.DataFrame({
            "question_text": questions_list,
            "cluster_number": cluster_labels
        })

    else:
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Please use 'kmeans' or 'deterministic'.")

    return df, sil_score
```

**Explanation:**
**`cluster_questions` – quick‑start clustering helper**

| What it does | How it works | What you get back |
|--------------|--------------|-------------------|
| Takes a list of `Question` objects and groups them into clusters. | 1. Pulls the raw text from each `Question`. <br>2. Converts all texts to embeddings (`convert_texts_to_vector`). <br>3. Depending on `algorithm`: <br>   * **kmeans** – runs `perform_kmeans` with the requested `num_clusters`, optionally shows a 2‑D scatter plot (`visualize_clusters`), and calculates a silhouette score if more than one cluster. <br>   * **deterministic** – builds a cosine‑similarity matrix, feeds it to `find_clusters_deterministic`, then maps each question to the cluster ID it belongs to. No silhouette score is produced. | Returns a `pandas.DataFrame` with two columns: `question_text` and `cluster_number`. Also returns the silhouette score (or `None` if not computed). |

**Key points for developers**

* `questions` must be a list of `Question` objects that expose a `question_text` attribute.  
* `num_clusters` is only used when `algorithm == "kmeans"`.  
* `is_show_graph` triggers a quick Matplotlib scatter plot of the clusters (only for k‑means).  
* If you pass an unsupported algorithm string, a `ValueError` is raised.  
* The function is a thin wrapper that orchestrates the heavy lifting done in the helper functions (`perform_kmeans`, `find_clusters_deterministic`, etc.) and packages the results into a convenient DataFrame.

**Imports:**
```
import sys, from typing import List, import pandas as pd, from sklearn.cluster import KMeans, from sklearn.decomposition import PCA, from sklearn.metrics import silhouette_score, from harmony.matching.default_matcher import convert_texts_to_vector, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, import numpy as np, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.deterministic_clustering import find_clusters_deterministic
```
