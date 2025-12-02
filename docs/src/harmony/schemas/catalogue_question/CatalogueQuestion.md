# CatalogueQuestion (class)

**Code:**
```python
class CatalogueQuestion(BaseModel):
    question: str = Field(description="The catalogue question")
    seen_in_instruments: list[CatalogueInstrument] = Field(
        description="The instruments from the catalogue were the question was seen in"
    )
```

**Explanation:**
**CatalogueQuestion** – a tiny data container that tells you two things:

1. **`question`** – the text of a question that lives in the catalogue.  
2. **`seen_in_instruments`** – a list of `CatalogueInstrument` objects that show which catalogue instruments actually contain that question.

Think of it as a “question‑lookup” record: you give it a question string, and it tells you every instrument in the catalogue that has that exact question. This is used when matching user‑submitted questions to the reference catalogue.

**Imports:**
```
from pydantic import BaseModel, Field, from harmony.schemas.catalogue_instrument import CatalogueInstrument
```
