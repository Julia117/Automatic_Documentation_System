# dist (function)

**Code:**
```python
def dist(vecs1,vecs2):
    vec_union = list(vecs1 + vecs2)
    n1,n2 = len(vecs1),len(vecs2)
    n = len(vec_union)
    dist_ = np.zeros((n,n))
    for i in range(n):
        for j in range(i):
            dist_[i,j] = dist_[j,i] = euclidean_dist(vec_union[i],vec_union[j])

    nw1 = [1. for i in range(n1)]+[0. for i in range(n2)]
    nw2 = [0. for i in range(n1)] +[1. for i in range(n2)]
    return np.array(dist_,dtype=np.float32),np.array(nw1,dtype=np.float32),np.array(nw2,dtype=np.float32)
```

**Explanation:**
**`dist(vecs1, vecs2)` – quick summary**

1. **Combine the vectors**  
   `vec_union = list(vecs1 + vecs2)` – puts all vectors from both lists into one list.

2. **Build a distance matrix**  
   * `n = len(vec_union)` – total number of vectors.  
   * `dist_` is an `n × n` zero matrix.  
   * For every pair `(i, j)` with `j < i` it calculates the Euclidean distance between the two vectors and stores it symmetrically:  
     `dist_[i, j] = dist_[j, i] = euclidean_dist(vec_union[i], vec_union[j])`.

3. **Create weight vectors for the two original sets**  
   * `nw1` has a `1` for each vector that came from `vecs1` and a `0` for each from `vecs2`.  
   * `nw2` is the opposite: `0` for `vecs1` elements, `1` for `vecs2` elements.

4. **Return**  
   * The distance matrix (`float32`).  
   * `nw1` and `nw2` as `float32` arrays.

This function is used to prepare the inputs for Earth‑Mover Distance calculations: a full pairwise distance matrix and two “mass” vectors indicating which vectors belong to each of the two sets.

**Imports:**
```
from wmd import WMD, import numpy as np, import math, import libwmdrelax
```
