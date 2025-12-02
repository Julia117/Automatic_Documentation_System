# generate_semantic_keywords (function)

**Code:**
```python
def generate_semantic_keywords(cluster_items: List[Question], top_k: int = 5) -> List[str]:
    """
    Generate representative keywords for a cluster using Sentence Transformers embeddings.

    Parameters
    ----------
    cluster_items : List[Question]
        The list of questions in the cluster.
    top_k : int
        Number of top keywords to extract.

    Returns
    -------
    List[str]
        A list of top keywords representing the cluster.
    """
    texts = [item.question_text for item in cluster_items]
    if not texts:
        return []

    # Generate embeddings for all texts
    embeddings = model.encode(texts)

    # Compute average embedding for the cluster
    cluster_embedding = embeddings.mean(axis=0, keepdims=True)

    # Calculate cosine similarity of each text to the cluster embedding
    similarities = cosine_similarity(cluster_embedding, embeddings)[0]

    # Rank texts based on similarity and select top_k
    top_indices = similarities.argsort()[-top_k:][::-1]  # Sort in descending order
    keywords = [texts[idx] for idx in top_indices]

    return keywords
```

**Explanation:**
**What it does**

`generate_semantic_keywords` picks the most representative questions from a cluster by using sentence embeddings.

1. **Collect the text** – it pulls the `question_text` from every `Question` in `cluster_items`.  
2. **Encode** – it feeds those texts into a pre‑loaded Sentence‑Transformers model (`model.encode`) to get a vector for each question.  
3. **Cluster centre** – it averages all the vectors to get a single “cluster embedding”.  
4. **Similarity** – it computes the cosine similarity between each question’s vector and the cluster centre.  
5. **Select top k** – it sorts the similarities, takes the indices of the `top_k` highest values, and returns the corresponding question texts as the cluster’s keywords.  

If the cluster has no questions, it simply returns an empty list. This gives a quick, semantically‑based list of the most central questions for a cluster.

**Imports:**
```
from sentence_transformers import SentenceTransformer, from harmony.schemas.requests.text import Question, from typing import List, from sklearn.metrics.pairwise import cosine_similarity
```
