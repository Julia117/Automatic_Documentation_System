# CacheResponse (class)

**Code:**
```python
class CacheResponse(BaseModel):
    instruments: List[Instrument] = Field(description="A list of instruments")
    vectors: List[dict] = Field(description="A list of vectors")
```

**Explanation:**
**CacheResponse** – a tiny data container used by the API to return two pieces of information in one response:

| Field | What it holds | Why it matters |
|-------|---------------|----------------|
| `instruments` | A list of `Instrument` objects (the full instrument data that was just processed or matched). | Lets the caller get the enriched instrument objects back in a single payload. |
| `vectors` | A list of dictionaries, each representing a cached text‑vector (e.g., `{ "text": "...", "vector": [0.12, …] }`). | Provides the raw vector data that can be stored locally so future calls don’t need to re‑vectorise the same texts. |

In short, `CacheResponse` bundles the processed instruments together with the vectors that were generated for them, making it easy to cache and reuse the results.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
