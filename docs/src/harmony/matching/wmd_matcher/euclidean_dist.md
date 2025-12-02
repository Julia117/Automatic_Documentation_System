# euclidean_dist (function)

**Code:**
```python
def euclidean_dist(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions")

    squared_distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance
```

**Explanation:**
**`euclidean_dist(point1, point2)` – a quick distance calculator**

- **Purpose**: Computes the straight‑line (Euclidean) distance between two points in the same‑dimensional space.
- **Input check**: If the two points don’t have the same number of coordinates, it raises a `ValueError`.
- **Computation**:
  1. For each pair of corresponding coordinates `(p1, p2)`, it calculates the squared difference `(p1 - p2) ** 2`.
  2. Sums all those squared differences to get the *squared distance*.
  3. Takes the square root of that sum to get the actual Euclidean distance.
- **Return**: The numeric distance value (a float).

**Imports:**
```
from wmd import WMD, import numpy as np, import math, import libwmdrelax
```
