# cluster_questions_affinity_propagation (function)

**Code:**
```python
def cluster_questions_affinity_propagation(
        questions: List[Question],
        item_to_item_similarity_matrix: np.ndarray
) -> List[HarmonyCluster]:
    """
    Affinity Propagation Clustering using the cosine similarity matrix.

    Parameters
    ----------
    questions : List[Question]
        The set of questions to cluster.

    item_to_item_similarity_matrix : np.ndarray
        The cosine similarity matrix for the questions.

    Returns
    -------
    List[HarmonyCluster]
        A list of HarmonyCluster objects representing the clusters.
    """

    # assert that the number of questions is greater than 0
    assert len(questions) > 0

    # assert that the similarity matrix is not empty
    assert item_to_item_similarity_matrix.size > 0

    # assert that the number of questions is equal to the number of rows in the similarity matrix
    assert len(questions) == item_to_item_similarity_matrix.shape[0]

    # assert that the number of questions is equal to the number of columns in the similarity matrix
    assert len(questions) == item_to_item_similarity_matrix.shape[1]

    # assert that the number of questions is equal to the number of rows and columns in the similarity matrix
    assert len(questions) == item_to_item_similarity_matrix.shape[0]
    assert len(questions) == item_to_item_similarity_matrix.shape[1]

    # assert that the similarity matrix is square
    assert item_to_item_similarity_matrix.shape[0] == item_to_item_similarity_matrix.shape[1]

    # assert that the similarity matrix is symmetric
    assert np.allclose(item_to_item_similarity_matrix, item_to_item_similarity_matrix.T)

    # assert that the similarity matrix is -1 <= x <= 1
    assert np.all(np.round(item_to_item_similarity_matrix, 3) >= -1.)
    assert np.all(np.round(item_to_item_similarity_matrix, 3) <= 1.)

    # assert that the similarity matrix has 1s on its diagonals
    assert np.allclose(np.diag(item_to_item_similarity_matrix), 1.)

    # ensure that the entries of the similarity matrix are floats
    if item_to_item_similarity_matrix.dtype != np.float64:
        item_to_item_similarity_matrix = item_to_item_similarity_matrix.astype(np.float64)

    affinity_propagation = AffinityPropagation(affinity='precomputed', random_state=1, max_iter=10, convergence_iter=5)
    affinity_propagation.fit(np.abs(item_to_item_similarity_matrix))

    exemplars = affinity_propagation.cluster_centers_indices_
    labels = affinity_propagation.labels_

    clusters = []

    for i, exemplar in enumerate(exemplars):
        clusters.append(
            HarmonyCluster(
                cluster_id=i,
                centroid_id=exemplar,
                centroid=questions[exemplar],
                items=[],
                item_ids=[],
                text_description=questions[exemplar].question_text,
                keywords=[]
            )
        )

    cluster_ids = set([cluster.cluster_id for cluster in clusters])
    for i, label in enumerate(labels):
        if label not in cluster_ids:
            clusters.append(
                HarmonyCluster(
                    cluster_id=label,
                    centroid_id=i,
                    centroid=questions[i],
                    items=[],
                    item_ids=[],
                    text_description=questions[i].question_text,
                    keywords=[]
                )
            )
            cluster_ids.add(label)

        clusters[label].items.append(questions[i])
        clusters[label].item_ids.append(i)

    cluster_topics = generate_cluster_topics(clusters, top_k_topics=5)
    for cluster, topics in zip(clusters, cluster_topics):
        cluster.keywords = topics

    return clusters
```

**Explanation:**
**What it does**

`cluster_questions_affinity_propagation` groups a list of `Question` objects into clusters using **Affinity Propagation**.  
It takes a pre‑computed cosine‑similarity matrix (one row/column per question) and returns a list of `HarmonyCluster` objects, each representing one cluster.

**Key steps**

1. **Validate inputs** – a series of `assert` statements check that the matrix is square, symmetric, has values in `[-1, 1]`, and that its size matches the number of questions.

2. **Prepare the matrix** – ensure the matrix is `float64` and take the absolute value (Affinity Propagation expects a similarity matrix).

3. **Run Affinity Propagation**  
   ```python
   affinity_propagation = AffinityPropagation(
       affinity='precomputed', random_state=1,
       max_iter=10, convergence_iter=5)
   affinity_propagation.fit(abs_matrix)
   ```
   The algorithm returns:
   * `cluster_centers_indices_` – indices of exemplar (representative) questions.
   * `labels_` – cluster assignment for every question.

4. **Build cluster objects**  
   * Create a `HarmonyCluster` for each exemplar (the cluster’s centroid).
   * Iterate over all questions, adding each to the cluster whose label it received.  
   * If a label wasn’t already in the cluster list, create a new cluster on the fly.

5. **Add keywords** – call `generate_cluster_topics` to extract the top 5 keywords for each cluster and store them in `cluster.keywords`.

6. **Return** the list of fully populated `HarmonyCluster` objects.

**Why it’s useful**

- No need to choose the number of clusters manually; Affinity Propagation decides it from the similarity data.
- The returned `HarmonyCluster` objects already contain the centroid question, all member questions, and a short keyword list for quick inspection.

**Imports:**
```
from typing import List, import numpy as np, from harmony.matching.generate_cluster_topics import generate_cluster_topics, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, from sklearn.cluster import AffinityPropagation
```
