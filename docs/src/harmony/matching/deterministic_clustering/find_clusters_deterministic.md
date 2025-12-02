# find_clusters_deterministic (function)

**Code:**
```python
def find_clusters_deterministic(
    questions: List[Question],
    item_to_item_similarity_matrix: np.ndarray,
    threshold: float = 0.5
) -> List[HarmonyCluster]:
    """
    Deterministic clustering using Sentence Transformers for cluster keywords.

    Parameters
    ----------
    questions : List[Question]
        The list of questions to be clustered.

    item_to_item_similarity_matrix : np.ndarray
        A cosine similarity matrix of shape (N, N) for the questions, where
        N is the number of questions.

    threshold : float, optional
        The minimum similarity score required to cluster two items together.
        Default is 0.5.

    Returns
    -------
    List[HarmonyCluster]
        A list of HarmonyCluster objects, each containing items that meet
        the specified similarity threshold.
    """

    # Basic assertions to ensure valid input data
    assert len(questions) > 0, "There must be at least one question."
    assert item_to_item_similarity_matrix.size > 0, "Similarity matrix cannot be empty."
    assert len(questions) == item_to_item_similarity_matrix.shape[0], \
        "Number of questions must match the similarity matrix's row count."
    assert len(questions) == item_to_item_similarity_matrix.shape[1], \
        "Number of questions must match the similarity matrix's column count."
    assert item_to_item_similarity_matrix.shape[0] == item_to_item_similarity_matrix.shape[1], \
        "Similarity matrix must be square."
    assert np.allclose(item_to_item_similarity_matrix, item_to_item_similarity_matrix.T), \
        "Similarity matrix must be symmetric."
    assert np.all(np.round(item_to_item_similarity_matrix, 3) >= -1.), \
        "All similarity scores must be >= -1."
    assert np.all(np.round(item_to_item_similarity_matrix, 3) <= 1.), \
        "All similarity scores must be <= 1."
    assert np.allclose(np.diag(item_to_item_similarity_matrix), 1.), \
        "Diagonal elements of similarity matrix should be 1."

    # Ensure the matrix is of type float64
    if item_to_item_similarity_matrix.dtype != np.float64:
        item_to_item_similarity_matrix = item_to_item_similarity_matrix.astype(np.float64)

    # We take the absolute value to focus on the magnitude of similarity
    abs_similarities = np.abs(item_to_item_similarity_matrix)

    # Create a dictionary mapping (row, col) -> similarity value
    coord_to_sim = {
        (y, x): abs_similarities[y, x]
        for y in range(abs_similarities.shape[0])
        for x in range(abs_similarities.shape[1])
    }

    total_score = Counter()
    edges = set()
    vertices = set()

    # Sort all pairwise similarities in descending order and form clusters
    for (y, x), sim in sorted(coord_to_sim.items(), key=lambda kv: kv[1], reverse=True):
        # Only consider upper or lower triangle once (x < y) and check threshold
        if x < y and sim >= threshold:
            # If either node hasn't been added to the graph yet, create an edge
            if x not in vertices or y not in vertices:
                edges.add((x, y))
                vertices.add(x)
                vertices.add(y)
                total_score[x] += sim
                total_score[y] += sim

    # Assign each question index to a group index
    question_idx_to_group_idx = {}
    for x, y in edges:
        # If both x and y are not in any group, create a new group for them
        if x not in question_idx_to_group_idx and y not in question_idx_to_group_idx:
            group_idx = min(x, y)
            question_idx_to_group_idx[x] = group_idx
            question_idx_to_group_idx[y] = group_idx
        # If x is already in a group, but y is not, assign y to x's group
        elif x in question_idx_to_group_idx and y not in question_idx_to_group_idx:
            group_idx = question_idx_to_group_idx[x]
            question_idx_to_group_idx[y] = group_idx
        # If y is already in a group, but x is not, assign x to y's group
        elif y in question_idx_to_group_idx and x not in question_idx_to_group_idx:
            group_idx = question_idx_to_group_idx[y]
            question_idx_to_group_idx[x] = group_idx

    # If some questions are isolated (no edges), they form their own group
    for idx in range(len(questions)):
        if idx not in question_idx_to_group_idx:
            question_idx_to_group_idx[idx] = idx

    # Build HarmonyCluster objects
    clusters_to_return = []
    all_groups = set(question_idx_to_group_idx.values())

    for group_no, group_idx in enumerate(sorted(all_groups)):
        items = []
        item_ids = []
        candidate_scores = {}

        # Collect all questions belonging to the current group
        for question_idx, grp in question_idx_to_group_idx.items():
            if grp == group_idx:
                items.append(questions[question_idx])
                item_ids.append(question_idx)
                candidate_scores[question_idx] = total_score.get(question_idx, 0)

        # The question with the highest total_score is used as the centroid
        best_question_idx = max(candidate_scores, key=candidate_scores.get)
        text_description = questions[best_question_idx].question_text

        # Create the HarmonyCluster object
        cluster = HarmonyCluster(
            cluster_id=group_no,
            centroid_id=best_question_idx,
            centroid=questions[best_question_idx],
            items=items,
            item_ids=item_ids,
            text_description=text_description,  # This can be updated below if needed
            keywords=[],
        )
        clusters_to_return.append(cluster)

    # Generate cluster topics for all clusters at once (instead of repeatedly inside the loop)
    cluster_topics = generate_cluster_topics(clusters_to_return, top_k_topics=5)

    # Assign the generated topics to each cluster
    for cluster, topics in zip(clusters_to_return, cluster_topics):
        cluster.keywords = topics

    return clusters_to_return
```

**Explanation:**
**`find_clusters_deterministic` – quick, rule‑based clustering**

1. **Input checks** – The function first verifies that the list of `Question` objects and the cosine‑similarity matrix are non‑empty, square, symmetric, and have 1’s on the diagonal.  
2. **Prepare data** –  
   * Convert the similarity matrix to `float64`.  
   * Take the absolute value of every similarity (so negative values are treated as positive).  
   * Build a dictionary `coord_to_sim` that maps each pair of indices `(row, col)` to its similarity score.  
3. **Greedy edge selection** –  
   * Sort all pairwise similarities in descending order.  
   * For each pair `(x, y)` with `x < y` and similarity ≥ `threshold`:  
     * If either node has not yet been added to the graph, add an edge `(x, y)`.  
     * Record the two nodes as vertices and accumulate a “total score” for each node (sum of similarities of edges it participates in).  
4. **Group assignment** –  
   * Walk through the edges and assign each node to a group:  
     * If both nodes are new → create a new group (use the smaller index as the group id).  
     * If one node already has a group → add the other node to that group.  
   * Any node that never appeared in an edge becomes its own singleton group.  
5. **Build `HarmonyCluster` objects** – For each group:  
   * Gather all `Question` objects and their indices.  
   * Pick the question with the highest total score as the cluster’s centroid.  
   * Create a `HarmonyCluster` with the centroid, items, ids, and a placeholder description.  
6. **Generate keywords** – Call `generate_cluster_topics` once for all clusters, then attach the resulting keyword lists to each cluster.  
7. **Return** – A list of `HarmonyCluster` instances, one per detected group.

In short, it builds a simple similarity‑based graph, greedily connects pairs above a threshold, groups connected nodes, and then creates cluster objects with centroids and topic keywords.

**Imports:**
```
from collections import Counter, from typing import List, import numpy as np, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster, from harmony.matching.generate_cluster_topics import generate_cluster_topics
```
