# ClusteringAlgorithm (class)

**Code:**
```python
class ClusteringAlgorithm(str, Enum):
    affinity_propagation: str = 'affinity_propagation'
    deterministic: str = 'deterministic'
    kmeans: str = 'kmeans'
    hdbscan: str = 'hdbscan'
```

**Explanation:**
**ClusteringAlgorithm** is a tiny helper that lets you refer to the four supported clustering methods by name instead of typing raw strings everywhere.

```python
class ClusteringAlgorithm(str, Enum):
    affinity_propagation: str = 'affinity_propagation'
    deterministic: str = 'deterministic'
    kmeans: str = 'kmeans'
    hdbscan: str = 'hdbscan'
```

* It inherits from `str` and `Enum`, so each member behaves like a string (`'kmeans'`, `'hdbscan'`, …) but also gives you the safety of an enum (e.g., `ClusteringAlgorithm.kmeans`).
* Use it when you need to pass or compare the algorithm name, e.g.:

```python
def cluster_questions(..., algorithm: ClusteringAlgorithm = ClusteringAlgorithm.kmeans):
    if algorithm == ClusteringAlgorithm.kmeans:
        ...
```

This keeps your code readable, prevents typos, and makes refactoring easier.

**Imports:**
```
from enum import Enum
```
