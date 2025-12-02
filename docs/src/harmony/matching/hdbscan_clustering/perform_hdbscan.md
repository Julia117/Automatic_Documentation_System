# perform_hdbscan (function)

**Code:**
```python
def perform_hdbscan(embeddings_in: np.ndarray, min_cluster_size=5):
    """
       Cluster data using HDBScan.

       See an explanation of HDBScan here:
        - https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html

       Parameters
       ----------
       embeddings_in : np.ndarray
           Text embeddings.
       min_cluster_size : int
           The minimum amount of points in a cluster.
           Lower values can include noise in clusters.
           Defaults to 5.
       Returns
       -------
       HDBSCAN : hdbscan.HDBSCAN
           A fitted HDBSCAN model.
       """

    # Ensure min_cluster_size is not greater than the dataset length
    min_cluster_size = min([embeddings_in.shape[0], min_cluster_size])

    hdbscan = HDBSCAN(min_cluster_size=min_cluster_size)
    hdbscan_model = hdbscan.fit(embeddings_in)

    return hdbscan_model
```

**Explanation:**
**Function Explanation: `perform_hdbscan`**

This function clusters data using the HDBSCAN algorithm. HDBSCAN is a density-based clustering algorithm that can handle varying densities of data points.

**Key Parameters:**

* `embeddings_in`: a 2D NumPy array containing text embeddings.
* `min_cluster_size`: the minimum number of points required to form a cluster (default is 5).

**Functionality:**

1. Ensures that `min_cluster_size` is not greater than the number of data points.
2. Creates an HDBSCAN model with the specified `min_cluster_size`.
3. Fits the HDBSCAN model to the input data (`embeddings_in`).
4. Returns the fitted HDBSCAN model.

**In Simple Terms:**

This function takes in a set of text embeddings and uses the HDBSCAN algorithm to group similar data points together based on their density and proximity. The `min_cluster_size` parameter controls the minimum number of points required to form a cluster.

**Imports:**
```
from typing import List, import numpy as np, from sklearn.cluster import HDBSCAN, from harmony.matching.generate_cluster_topics import generate_cluster_topics, from harmony.schemas.requests.text import Question, from harmony.schemas.responses.text import HarmonyCluster
```
