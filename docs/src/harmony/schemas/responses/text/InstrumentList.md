# InstrumentList (class)

**Code:**
```python
class InstrumentList(RootModel):
    root: List[Instrument]
```

**Explanation:**
**InstrumentList** is a tiny wrapper that turns a plain Python list of `Instrument` objects into a Pydantic model.  
- It inherits from `RootModel`, so the entire list is stored in the `root` field.  
- This lets you validate, serialize, and deserialize a collection of instruments as a single Pydantic object, which is handy when sending or receiving JSON that contains many instruments.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
