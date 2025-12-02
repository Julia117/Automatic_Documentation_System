# par_to_vecs (function)

**Code:**
```python
def par_to_vecs(par,vectorisation_function):
    return [vectorisation_function(sent) for sent in par]
```

**Explanation:**
**`par_to_vecs(par, vectorisation_function)`**

- **Purpose**: Convert a list of sentences (`par`) into a list of vector representations.
- **How it works**:  
  1. Iterate over each sentence in `par`.  
  2. Apply `vectorisation_function` to that sentence.  
  3. Collect the resulting vectors into a new list.  
- **Result**: A list where each element is the vector produced by `vectorisation_function` for the corresponding sentence in `par`.

**Imports:**
```
from wmd import WMD, import numpy as np, import math, import libwmdrelax
```
