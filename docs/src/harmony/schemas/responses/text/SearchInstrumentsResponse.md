# SearchInstrumentsResponse (class)

**Code:**
```python
class SearchInstrumentsResponse(BaseModel):
    instruments: List[Instrument] = Field(description="A list of instruments")
```

**Explanation:**
**SearchInstrumentsResponse**

- **What it is**: A Pydantic model that represents the JSON payload returned by the “search instruments” API endpoint.
- **Key field**:
  - `instruments`: a list of `Instrument` objects (each instrument contains its metadata, questions, etc.).
- **Why it matters**: When a client calls the search endpoint, the server wraps the found instruments in this model so FastAPI can automatically serialize it to JSON and validate the structure.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
