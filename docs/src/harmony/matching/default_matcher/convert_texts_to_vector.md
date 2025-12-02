# convert_texts_to_vector (function)

**Code:**
```python
def convert_texts_to_vector(texts: List, batch_size=1000, max_batches=2000) -> ndarray:
    if batch_size == 0:
        embeddings = model.encode(sentences=texts, convert_to_numpy=True)

        return embeddings

    embeddings = []
    batch_count = 0

    # Process texts in batches
    for i in range(0, len(texts), batch_size):
        if batch_count >= max_batches:
            break
        batch = texts[i:i + batch_size]
        batch_embeddings = model.encode(sentences=batch, convert_to_numpy=True)
        embeddings.append(batch_embeddings)
        batch_count += 1

    # Concatenate all batch embeddings into a single NumPy array
    return np.concatenate(embeddings, axis=0)
```

**Explanation:**
**`convert_texts_to_vector` – quick‑look**

```python
def convert_texts_to_vector(texts: List, batch_size=1000, max_batches=2000) -> ndarray:
```

- **Purpose** – Turn a list of strings into a NumPy array of embeddings (one row per text).  
- **Model call** – Uses `model.encode(sentences=…, convert_to_numpy=True)` to get the raw vectors.  
- **Batching** –  
  - If `batch_size == 0` the whole list is sent to the model at once.  
  - Otherwise the texts are split into chunks of `batch_size`.  
  - `max_batches` caps how many chunks are processed (useful for very large inputs).  
- **Result** – All chunk embeddings are concatenated (`np.concatenate(..., axis=0)`) and returned.  
- **Output shape** – `(len(texts), embedding_dim)` – e.g., `(10, 384)` in the test.  

In short: it safely feeds a potentially huge list of texts to the encoder in manageable pieces and stitches the results back together.

**Imports:**
```
import os, from typing import List, import numpy as np, from harmony import match_instruments_with_function, from harmony.schemas.requests.text import Instrument, from numpy import ndarray, from sentence_transformers import SentenceTransformer, from harmony.schemas.responses.text import MatchResult
```
