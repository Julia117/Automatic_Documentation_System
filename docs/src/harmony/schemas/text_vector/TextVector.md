# TextVector (class)

**Code:**
```python
class TextVector(BaseModel):
    text: str = Field()
    vector: List[float] = Field()
    is_negated: bool = Field()
    is_query: bool = Field()
```

**Explanation:**
**TextVector** is a lightweight data container (a Pydantic `BaseModel`) that holds:

| Field | Type | Purpose |
|-------|------|---------|
| `text` | `str` | The raw text string. |
| `vector` | `List[float]` | Numerical embedding of the text (e.g., from a transformer). |
| `is_negated` | `bool` | Flag indicating the text is a negated version of the original. |
| `is_query` | `bool` | Flag indicating the text is a query (used for search or filtering). |

Use it to keep a text together with its vector and metadata so you can easily pass it around, cache it, or filter by negation/query status.

**Imports:**
```
from typing import List, from pydantic import BaseModel, Field
```
