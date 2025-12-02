# model_post_init (function)

**Code:**
```python
def model_post_init(self, ctx) -> None:
        # Assign instrument ID if missing
        if not self.instrument_id:
            self.instrument_id = uuid.uuid4().hex

        # Assign instrument ID to questions
        for question in self.questions or []:
            question.instrument_id = self.instrument_id
```

**Explanation:**
**`model_post_init` – what it does**

```python
def model_post_init(self, ctx) -> None:
    # 1. If the instrument doesn’t already have an ID, generate a new UUID‑4
    #    and store it in `self.instrument_id`.

    # 2. Loop over every `Question` in `self.questions` (or an empty list if
    #    there are none) and copy that same instrument ID into each
    #    question’s `instrument_id` field.
```

In short: after an `Instrument` object is created, this hook guarantees that the instrument has a unique identifier and that every question inside it carries the same identifier for easy grouping and lookup.

**Imports:**
```
import uuid, from typing import List, Optional, from pydantic import ConfigDict, BaseModel, Field, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.enums.file_types import FileType, from harmony.schemas.enums.languages import Language, from pydantic import ConfigDict, BaseModel, Field, from typing import Any, Dict, List, Optional
```
