# pars_dist_emd_emdrelaxed (function)

**Code:**
```python
def pars_dist_emd_emdrelaxed(par1,par2,vectorisation_function):
    relax_cache = libwmdrelax.emd_relaxed_cache_init(int(100)) 
    cache = libwmdrelax.emd_cache_init(int(100)) 
 
    vecs1,vecs2 = par_to_vecs(par1,vectorisation_function),par_to_vecs(par2,vectorisation_function)
    dist_,nw1,nw2 = dist(vecs1,vecs2)
    emd = libwmdrelax.emd(nw1,nw2,dist_,cache)
    emd_relaxed = libwmdrelax.emd_relaxed(nw1,nw2,dist_,relax_cache)
    return emd,emd_relaxed
```

**Explanation:**
**What the function does (in plain language)**  

`pars_dist_emd_emdrelaxed` takes two “paragraphs” (`par1` and `par2`) and a text‑vectorisation function.  
It returns two similarity scores:

1. **EMD (Earth‑Mover Distance)** – the classic distance between the two sets of word vectors.  
2. **Relaxed EMD** – a softer version that allows a little “slack” in the matching.

**Step‑by‑step**

| Step | What happens | Why |
|------|--------------|-----|
| 1 | `relax_cache = libwmdrelax.emd_relaxed_cache_init(100)` and `cache = libwmdrelax.emd_cache_init(100)` | Create two small caches (size 100) that the underlying C library uses to speed up repeated EMD calculations. |
| 2 | `vecs1, vecs2 = par_to_vecs(par1, vectorisation_function), par_to_vecs(par2, vectorisation_function)` | Convert every sentence in each paragraph into a numeric vector using the supplied `vectorisation_function`. |
| 3 | `dist_, nw1, nw2 = dist(vecs1, vecs2)` | Build a distance matrix between all vectors in the two paragraphs (`dist_`) and create two weight vectors (`nw1`, `nw2`) that simply say “each sentence counts equally”. |
| 4 | `emd = libwmdrelax.emd(nw1, nw2, dist_, cache)` | Call the C routine that computes the standard Earth‑Mover Distance using the distance matrix and the cache. |
| 5 | `emd_relaxed = libwmdrelax.emd_relaxed(nw1, nw2, dist_, relax_cache)` | Call the relaxed version of the routine, which allows a bit of flexibility in how the mass is moved. |
| 6 | `return emd, emd_relaxed` | Return both scores to the caller. |

**Bottom line**  
The function is a thin wrapper that turns two paragraphs into vectors, builds the pairwise distance matrix, and then asks the `libwmdrelax` library to compute both the standard and relaxed Earth‑Mover Distances. It’s useful when you need a robust similarity measure between two sets of sentences.

**Imports:**
```
from wmd import WMD, import numpy as np, import math, import libwmdrelax
```
