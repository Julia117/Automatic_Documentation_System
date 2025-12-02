# cluster_questions_hdbscan_from_embeddings (function)

**Code:**
```python
def cluster_questions_hdbscan_from_embeddings(questions: List[Question], embedding_matrix: np.ndarray,
                                              min_cluster_size=5):
    """
    Cluster questions with HDBSCAN

    Parameters
    ----------
    questions : List[Question]
        The set of questions to cluster.

    embedding_matrix : np.ndarray
        Array of text embedding of each question.

    min_cluster_size : int
        The minimum amount of points in a cluster.
        Defaults to 5.

    Returns
    -------
    List[HarmonyCluster]
        A list of HarmonyCluster objects representing the clusters.
    """

    hdbscan = perform_hdbscan(embedding_matrix, min_cluster_size)
    cluster_labels = hdbscan.labels_
    probabilities = np.array(hdbscan.probabilities_)  # Probability/confidence for each datapoint.

    # Create dict with a key for each cluster, with each key storing a list of datapoint's
    # index in the labels list, its corresponding probability, and Question
    cluster_indices = {}
    for i, val in enumerate(cluster_labels):
        if val not in cluster_indices:
            cluster_indices[val] = []
        cluster_indices[val].append((i, probabilities[i], questions[i]))

    # Find the index of the highest probability datapoint for each cluster. For HDBSCAN, these are the "centroids".
    cluster_centroids = {
        cluster: max(cluster_indices[cluster], key=lambda x: x[1])[0]
        for cluster in cluster_indices.keys()
    }

    # Build HarmonyClusters, extract relevant data
    clusters_to_return = []
    for cluster_id, cluster_data in cluster_indices.items():
        centroid_id = cluster_centroids[cluster_id]

        # Retrieve centroid question
        centroid_question = None
        for ind, _, question in cluster_data:
            if ind == centroid_id:
                centroid_question = question
                break

        cluster = HarmonyCluster(
            cluster_id=cluster_id,
            centroid_id=centroid_id,
            centroid=centroid_question,
            item_ids=[ind for ind, _, _ in cluster_data],
            items=[question for _, _, question in cluster_data],
            text_description=centroid_question.question_text,
            keywords=[],
        )

        clusters_to_return.append(cluster)

        # generate cluster topics
        cluster_topics = generate_cluster_topics(clusters_to_return, top_k_topics=5)
        for cluster, topics in zip(clusters_to_return, cluster_topics):
            cluster.keywords = topics

    return clusters_to_return
```

**Explanation:**
**Function Explanation: `cluster_questions_hdbscan_from_embeddings`**

This function clusters a list of questions using the HDBSCAN algorithm, which is a density-based clustering algorithm. It takes in a list of questions and their corresponding text embeddings, and returns a list of clusters, where each cluster is represented by a `HarmonyCluster` object.

Here's a step-by-step breakdown:

1. **Perform HDBSCAN clustering**: The function uses the `perform_hdbscan` function to perform HDBSCAN clustering on the input embeddings.
2. **Get cluster labels and probabilities**: The function retrieves the cluster labels and probabilities from the HDBSCAN model.
3. **Create a dictionary of cluster indices**: The function creates a dictionary where each key is a cluster label, and the value is a list of tuples containing the index of each data point in the cluster, its probability, and the corresponding question.
4. **Find the centroid of each cluster**: The function finds the index of the data point with the highest probability in each cluster, which is considered the centroid of the cluster.
5. **Build HarmonyClusters**: The function creates a `HarmonyCluster` object for each cluster, using the centroid question, item IDs, items, and text description.
6. **Generate cluster topics**: The function generates topics for each cluster using the `generate_cluster_topics` function.
7. **Return the list of clusters**: The function returns the list of `HarmonyCluster` objects, each representing a cluster of questions.

In simple terms, this function takes in a list of questions and their embeddings, and returns a list of clusters, where each cluster is a group of questions that are similar to each other.

**Imports:**
```
from typing import List, import numpy as np, from sklearn.cluster import HDBSCAN, from harmony.matching.generate_cluster_topics import generate_cluster_topics, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster
```
